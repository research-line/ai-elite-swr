#!/usr/bin/env python3
"""
migrate_db_v2.py
================
Ticket T-20260723-01, user decision D-20260727-004 "Option C" (2026-07-28):
controlled migration into a NEW versioned database. The published DB
(_data_A/tools/aussagen_top100.db, analysis basis of Paper A v8.1 /
Paper B v6.1) stays byte-identical and is frozen hash-bound.

What this does (--apply):
  1. Copies the published DB to aussagen_top100_v2.db via the SQLite backup
     API (transactional, consistent, source opened read-only).
  2. Restores RAW (unblinded) text for rows whose text field currently holds
     blinded placeholder text ([PERSON]/[FIRMA]/...), using the raw recovery
     snapshot _data_A/_raw_recovery_2026-03-31/aussagen_top100.db. A row is
     only restored when blind_text(raw) == current text exactly (unique or
     safely resolvable multi-match). Only the text column is touched
     (aussagen.aussage_text, handlungen.beschreibung).
  3. Inserts the 9 statements that exist only in the recovery snapshot
     (person_ids 34, 57, 66, 86, 88; recovery holds 11 rows = 9 unique texts).
  4. Installs guard triggers rejecting placeholder text in future
     INSERT/UPDATE on the text columns (root-cause fix for v2) and sets
     PRAGMA user_version = 2.
  5. Writes a machine-readable manifest to
     _data_A/_raw_recovery_2026-03-31/migration_v2_manifest.json.

Modes:
  python migrate_db_v2.py            dry-run: prints the plan, writes nothing
  python migrate_db_v2.py --apply    executes the migration
  python migrate_db_v2.py --verify   read-only post-checks, exit 1 on failure

Reproducibility property checked by --verify: re-blinding every restored row
yields exactly the published blinded text, so the blinded extraction corpus
that the published analyses consumed is unchanged (the 9 new statements are
additive on top).
"""

import hashlib
import json
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
LIVE_DB = TOOLS_DIR / "aussagen_top100.db"
V2_DB = TOOLS_DIR / "aussagen_top100_v2.db"
RECOVERY_DIR = TOOLS_DIR.parent / "_raw_recovery_2026-03-31"
RECOVERY_DB = RECOVERY_DIR / "aussagen_top100.db"
MANIFEST = RECOVERY_DIR / "migration_v2_manifest.json"

sys.path.insert(0, str(TOOLS_DIR))
from extract_blinded import blind_text  # noqa: E402

PLACEHOLDERS = ("[PERSON]", "[FIRMA]", "[PRODUKT]", "[PLATTFORM]", "[UNI]", "[PROJEKT]")
TEXT_COLS = (("aussagen", "aussage_text"), ("handlungen", "beschreibung"))
EXPECTED_MISSING_AUSSAGEN = 9  # hard acceptance criterion from the diagnosis


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def has_placeholder(text):
    return bool(text) and any(p in text for p in PLACEHOLDERS)


def ro_connect(path):
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def table_columns(conn, table):
    return [r[1] for r in conn.execute(f"PRAGMA table_info({table})")]


def build_plans(v2, rec):
    """Compute update/insert plans. Returns (updates, inserts, skipped).

    updates: list of (table, row_id, raw_text)
    inserts: list of recovery-row dicts (aussagen only)
    skipped: list of (table, row_id, reason)
    """
    updates, inserts, skipped = [], [], []

    for table, col in TEXT_COLS:
        rec_idx = defaultdict(set)
        for pid, txt in rec.execute(f"SELECT person_id, {col} FROM {table}"):
            rec_idx[(pid, blind_text(txt))].add(txt)

        # group v2 placeholder rows by (person_id, blinded text)
        groups = defaultdict(list)
        for rid, pid, txt in v2.execute(f"SELECT id, person_id, {col} FROM {table}"):
            if has_placeholder(txt):
                groups[(pid, txt)].append(rid)

        for (pid, blinded), ids in sorted(groups.items()):
            cands = rec_idx.get((pid, blinded), set())
            if len(cands) == 1:
                raw = next(iter(cands))
                for rid in sorted(ids):
                    updates.append((table, rid, raw))
            elif len(cands) == len(ids) and len(cands) > 1:
                # safe only if the live rows are fully interchangeable
                rows = []
                for rid in sorted(ids):
                    row = v2.execute(
                        f"SELECT * FROM {table} WHERE id=?", (rid,)).fetchone()
                    cols = table_columns(v2, table)
                    rows.append({c: v for c, v in zip(cols, row)
                                 if c not in ("id", col)})
                if all(r == rows[0] for r in rows[1:]):
                    for rid, raw in zip(sorted(ids), sorted(cands)):
                        updates.append((table, rid, raw))
                else:
                    for rid in sorted(ids):
                        skipped.append((table, rid, "ambiguous, rows differ"))
            else:
                for rid in sorted(ids):
                    skipped.append((table, rid, "no raw match in recovery"))

    # missing aussagen: present neither raw nor blinded in v2
    v2_keys = set()
    for pid, txt in v2.execute("SELECT person_id, aussage_text FROM aussagen"):
        v2_keys.add((pid, txt))
        v2_keys.add((pid, blind_text(txt)))
    cols = table_columns(rec, "aussagen")
    seen = set()
    rec_rows = rec.execute(
        f"SELECT {', '.join(cols)} FROM aussagen ORDER BY id").fetchall()
    for row in rec_rows:
        d = dict(zip(cols, row))
        key = (d["person_id"], d["aussage_text"])
        if key in seen:
            continue
        seen.add(key)
        if key in v2_keys or (d["person_id"], blind_text(d["aussage_text"])) in v2_keys:
            continue
        inserts.append(d)

    return updates, inserts, skipped


def guard_trigger_sql():
    cond = " OR ".join(f"NEW.{{col}} LIKE '%{p}%'" for p in PLACEHOLDERS)
    stmts = []
    for table, col in TEXT_COLS:
        c = cond.format(col=col)
        stmts.append(f"""
CREATE TRIGGER trg_{table}_no_placeholder_ins
BEFORE INSERT ON {table} WHEN {c}
BEGIN SELECT RAISE(ABORT, 'placeholder text rejected (T-20260723-01 v2 guard)'); END""")
        stmts.append(f"""
CREATE TRIGGER trg_{table}_no_placeholder_upd
BEFORE UPDATE OF {col} ON {table} WHEN {c}
BEGIN SELECT RAISE(ABORT, 'placeholder text rejected (T-20260723-01 v2 guard)'); END""")
    return stmts


def cmd_dry_run():
    v2 = ro_connect(LIVE_DB)   # plan against the published state
    rec = ro_connect(RECOVERY_DB)
    updates, inserts, skipped = build_plans(v2, rec)
    per_table = Counter(t for t, _, _ in updates)
    print("DRY-RUN (no writes)")
    print(f"  updates planned : {len(updates)} ({dict(per_table)})")
    print(f"  inserts planned : {len(inserts)} aussagen "
          f"(person_ids {sorted({d['person_id'] for d in inserts})})")
    print(f"  skipped         : {len(skipped)} "
          f"({Counter(r for _, _, r in skipped)})")
    v2.close()
    rec.close()


def cmd_apply():
    if V2_DB.exists():
        sys.exit(f"ABORT: {V2_DB} already exists - refusing to overwrite.")
    for p in (LIVE_DB, RECOVERY_DB):
        if not p.exists():
            sys.exit(f"ABORT: missing {p}")

    live_hash_before = sha256(LIVE_DB)
    print(f"published DB sha256 (before): {live_hash_before}")

    # 1. transactional copy via backup API, source read-only
    src = ro_connect(LIVE_DB)
    dst = sqlite3.connect(V2_DB)
    src.backup(dst)
    src.close()
    print(f"copied -> {V2_DB.name} (sqlite backup API)")

    rec = ro_connect(RECOVERY_DB)
    updates, inserts, skipped = build_plans(dst, rec)
    rec.close()

    if len(inserts) != EXPECTED_MISSING_AUSSAGEN:
        dst.close()
        V2_DB.unlink(missing_ok=True)
        sys.exit(f"ABORT: expected {EXPECTED_MISSING_AUSSAGEN} missing aussagen, "
                 f"computed {len(inserts)} - no writes performed.")

    cur = dst.cursor()
    try:
        cur.execute("BEGIN")
        # 2. restore raw texts
        for table, rid, raw in updates:
            col = dict(TEXT_COLS)[table]
            cur.execute(f"UPDATE {table} SET {col}=? WHERE id=?", (raw, rid))
        # 3. insert the missing statements (all columns except id)
        cols = [c for c in table_columns(dst, "aussagen") if c != "id"]
        inserted_ids = []
        for d in inserts:
            cur.execute(
                f"INSERT INTO aussagen ({', '.join(cols)}) "
                f"VALUES ({', '.join('?' * len(cols))})",
                [d.get(c) for c in cols])
            inserted_ids.append(cur.lastrowid)
        # 4. guard triggers + version marker
        for stmt in guard_trigger_sql():
            cur.execute(stmt)
        cur.execute(f"PRAGMA user_version=2")
        dst.commit()
    except Exception:
        dst.rollback()
        dst.close()
        V2_DB.unlink(missing_ok=True)
        raise

    cur.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    dst.close()

    live_hash_after = sha256(LIVE_DB)
    if live_hash_after != live_hash_before:
        sys.exit("CRITICAL: published DB changed during migration!")

    manifest = {
        "ticket": "T-20260723-01",
        "decision": "D-20260727-004 Option C",
        "applied_utc": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc).isoformat(),
        "published_db": {
            "path": str(LIVE_DB),
            "sha256_frozen": live_hash_before,
            "sha256_after_migration": live_hash_after,
        },
        "v2_db": {"path": str(V2_DB), "sha256": sha256(V2_DB)},
        "updates": {
            "total": len(updates),
            "per_table": dict(Counter(t for t, _, _ in updates)),
            "ids": {t: sorted(rid for tt, rid, _ in updates if tt == t)
                    for t, _ in TEXT_COLS},
        },
        "inserts": {
            "total": len(inserts),
            "table": "aussagen",
            "new_ids": inserted_ids,
            "person_ids": sorted({d["person_id"] for d in inserts}),
        },
        "skipped": [{"table": t, "id": rid, "reason": r} for t, rid, r in skipped],
        "guards": ["trg_aussagen_no_placeholder_ins", "trg_aussagen_no_placeholder_upd",
                   "trg_handlungen_no_placeholder_ins", "trg_handlungen_no_placeholder_upd"],
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print(f"updates applied : {len(updates)} {manifest['updates']['per_table']}")
    print(f"inserts applied : {len(inserts)} aussagen, new ids {inserted_ids}")
    print(f"skipped         : {len(skipped)} (raw form lost, stays blinded)")
    print(f"v2 sha256       : {manifest['v2_db']['sha256']}")
    print(f"manifest        : {MANIFEST}")
    print("Next: python migrate_db_v2.py --verify")


def cmd_verify():
    if not MANIFEST.exists():
        sys.exit("ABORT: no manifest - run --apply first.")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    live = ro_connect(LIVE_DB)
    v2 = ro_connect(V2_DB)

    print("VERIFY migration v2 (read-only)")
    # 1. published DB untouched
    check("published DB hash unchanged",
          sha256(LIVE_DB) == manifest["published_db"]["sha256_frozen"],
          manifest["published_db"]["sha256_frozen"])
    # 2. table counts
    for t in ("personen", "plattformen", "quellen_typen", "kategorien",
              "handlungen", "aussagen"):
        cl = live.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        c2 = v2.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        exp = cl + (manifest["inserts"]["total"] if t == "aussagen" else 0)
        check(f"count {t}: v2={c2} expected={exp}", c2 == exp)
    # 3. row-level: all columns identical except migrated text col;
    #    migrated rows must re-blind to the published text
    for table, col in TEXT_COLS:
        cols = table_columns(live, table)
        others = [c for c in cols if c != col]
        idx = {r[0]: r for r in v2.execute(f"SELECT {', '.join(cols)} FROM {table}")}
        n_reblind_ok = n_other_diff = n_reblind_bad = 0
        for row in live.execute(f"SELECT {', '.join(cols)} FROM {table}"):
            d_live = dict(zip(cols, row))
            d_v2 = dict(zip(cols, idx[d_live["id"]]))
            for c in others:
                if d_live[c] != d_v2[c]:
                    n_other_diff += 1
            if d_live[col] != d_v2[col]:
                if blind_text(d_v2[col]) == d_live[col]:
                    n_reblind_ok += 1
                else:
                    n_reblind_bad += 1
        check(f"{table}: non-text columns identical for all published ids",
              n_other_diff == 0, f"{n_other_diff} diffs")
        check(f"{table}: every migrated text re-blinds to published text",
              n_reblind_bad == 0 and n_reblind_ok == manifest["updates"]["per_table"][table],
              f"{n_reblind_ok} restored, {n_reblind_bad} bad")
    # 4. blinded corpus: published multiset must be subset of v2 multiset,
    #    difference = exactly the inserted statements
    def blinded_multiset(conn, table, col):
        return Counter(blind_text(t) for (t,) in conn.execute(f"SELECT {col} FROM {table}"))
    for table, col in TEXT_COLS:
        ml, m2 = blinded_multiset(live, table, col), blinded_multiset(v2, table, col)
        missing = ml - m2
        extra = m2 - ml
        if table == "aussagen":
            check("aussagen: published blinded corpus fully contained in v2",
                  not missing, f"{sum(missing.values())} missing")
            check("aussagen: v2 adds exactly the 9 new blinded statements",
                  sum(extra.values()) == manifest["inserts"]["total"],
                  f"extra={sum(extra.values())}")
        else:
            check("handlungen: blinded corpus identical published vs v2",
                  not missing and not extra,
                  f"missing={sum(missing.values())} extra={sum(extra.values())}")
    # 5. reference tables byte-identical content
    for t in ("personen", "plattformen", "quellen_typen", "kategorien"):
        dl = live.execute(f"SELECT * FROM {t} ORDER BY 1").fetchall()
        d2 = v2.execute(f"SELECT * FROM {t} ORDER BY 1").fetchall()
        check(f"reference table {t} identical", dl == d2)
    # 6. placeholder share dropped as planned
    for table, col in TEXT_COLS:
        n2 = sum(1 for (t,) in v2.execute(f"SELECT {col} FROM {table}") if has_placeholder(t))
        nl = sum(1 for (t,) in live.execute(f"SELECT {col} FROM {table}") if has_placeholder(t))
        exp = nl - manifest["updates"]["per_table"][table]
        check(f"{table}: placeholder rows {nl} -> {n2} (expected {exp})", n2 == exp)
    # 7. guards present and functional
    trg = {r[0] for r in v2.execute(
        "SELECT name FROM sqlite_master WHERE type='trigger'")}
    check("4 guard triggers installed", all(g in trg for g in manifest["guards"]))
    v2w = sqlite3.connect(V2_DB)
    try:
        v2w.execute("INSERT INTO handlungen (person_id, handlung_typ, beschreibung) "
                    "VALUES (1, 'sonstiges', 'test [PERSON] placeholder')")
        v2w.rollback()
        check("guard trigger rejects placeholder INSERT", False, "no exception raised")
    except sqlite3.IntegrityError:
        v2w.rollback()
        check("guard trigger rejects placeholder INSERT", True)
    # 8. version marker
    uv = v2.execute("PRAGMA user_version").fetchone()[0]
    check("PRAGMA user_version == 2", uv == 2, f"got {uv}")

    live.close()
    v2.close()
    v2w.close()

    print("=" * 60)
    if failures:
        print(f"VERIFY FAILED: {len(failures)} check(s): {failures}")
        sys.exit(1)
    print("VERIFY OK — all checks passed.")


if __name__ == "__main__":
    if "--apply" in sys.argv:
        cmd_apply()
    elif "--verify" in sys.argv:
        cmd_verify()
    else:
        cmd_dry_run()
