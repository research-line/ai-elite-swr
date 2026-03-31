#!/usr/bin/env python3
"""
Update v2: Extends the database with:
1. Column aussage_uebersetzung_de (German translation of statements)
2. Column originalsprache (language code of original statement)
3. Table handlungen (actions as validity source)
4. View for statement-action comparison
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys=ON")
cur = conn.cursor()

# ============================================================
# 1. New columns in aussagen (statements)
# ============================================================

# Refine original language (was previously 'sprache' with default 'en')
# New column for German translation
try:
    cur.execute("ALTER TABLE aussagen ADD COLUMN aussage_uebersetzung_de TEXT")
    print("[OK] Column aussage_uebersetzung_de added")
except sqlite3.OperationalError as e:
    if "duplicate column" in str(e):
        print("[SKIP] Column aussage_uebersetzung_de already exists")
    else:
        raise

# ============================================================
# 2. Table handlungen (actions as validity source)
# ============================================================

cur.executescript("""
CREATE TABLE IF NOT EXISTS handlungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER NOT NULL,
    handlung_typ TEXT NOT NULL CHECK(handlung_typ IN (
        'investition',
        'verkauf',
        'kauf',
        'umstrukturierung',
        'gruendung',
        'ruecktritt',
        'entlassung',
        'einstellung',
        'lobbying',
        'spende',
        'klage',
        'partnerschaft',
        'produktlaunch',
        'politisch',
        'sonstiges'
    )),
    beschreibung TEXT NOT NULL,
    datum_handlung TEXT,
    datum_bekannt TEXT,
    betrag_usd REAL,
    quell_link TEXT,
    quell_titel TEXT,
    datum_abruf TEXT DEFAULT (date('now')),
    kontext TEXT,
    notizen TEXT,
    erstellt_am TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (person_id) REFERENCES personen(id)
);

CREATE INDEX IF NOT EXISTS idx_handlungen_person ON handlungen(person_id);
CREATE INDEX IF NOT EXISTS idx_handlungen_typ ON handlungen(handlung_typ);
CREATE INDEX IF NOT EXISTS idx_handlungen_datum ON handlungen(datum_handlung);
""")
print("[OK] Table handlungen created")

# ============================================================
# 3. Junction table: aussagen <-> handlungen (statement <-> action)
# ============================================================

cur.executescript("""
CREATE TABLE IF NOT EXISTS aussagen_handlungen (
    aussage_id INTEGER NOT NULL,
    handlung_id INTEGER NOT NULL,
    beziehung TEXT CHECK(beziehung IN (
        'konsistent',
        'widerspruch',
        'unklar',
        'kontext'
    )) DEFAULT 'unklar',
    notizen TEXT,
    PRIMARY KEY (aussage_id, handlung_id),
    FOREIGN KEY (aussage_id) REFERENCES aussagen(id) ON DELETE CASCADE,
    FOREIGN KEY (handlung_id) REFERENCES handlungen(id) ON DELETE CASCADE
);
""")
print("[OK] Table aussagen_handlungen created")

# ============================================================
# 4. View: statement-action comparison
# ============================================================

cur.executescript("""
CREATE VIEW IF NOT EXISTS v_sagen_vs_handeln AS
SELECT
    p.rang,
    p.name AS person,
    a.aussage_kurz,
    a.datum_aussage,
    h.handlung_typ,
    h.beschreibung AS handlung,
    h.datum_handlung,
    h.betrag_usd,
    ah.beziehung,
    ah.notizen AS vergleich_notiz
FROM aussagen_handlungen ah
JOIN aussagen a ON ah.aussage_id = a.id
JOIN handlungen h ON ah.handlung_id = h.id
JOIN personen p ON a.person_id = p.id
ORDER BY p.rang, a.datum_aussage;
""")
print("[OK] View v_sagen_vs_handeln created")

# ============================================================
# 5. Update view: v_aussagen_komplett with translation
# ============================================================

cur.execute("DROP VIEW IF EXISTS v_aussagen_komplett")
cur.execute("""
CREATE VIEW v_aussagen_komplett AS
SELECT
    a.id AS aussage_id,
    p.rang,
    p.name AS person,
    a.aussage_text,
    a.aussage_uebersetzung_de,
    a.aussage_kurz,
    a.modus,
    a.sprache AS originalsprache,
    qt.name AS quellen_typ,
    pl.name AS plattform,
    a.quell_link,
    a.quell_titel,
    a.datum_aussage,
    a.datum_quelle,
    a.datum_abruf,
    a.originalitaet,
    a.einschluss,
    a.grenzfall,
    a.kontext,
    a.notizen
FROM aussagen a
JOIN personen p ON a.person_id = p.id
LEFT JOIN quellen_typen qt ON a.quellen_typ_id = qt.id
LEFT JOIN plattformen pl ON a.plattform_id = pl.id
""")
print("[OK] View v_aussagen_komplett updated (with translation)")

# ============================================================
# 6. New category: HA (action-related)
# ============================================================

try:
    cur.execute("""
        INSERT INTO kategorien (code, name, beschreibung, typ, beispiel)
        VALUES ('HA', 'Handlungsbezug',
                'Aussage steht in direktem Bezug zu einer konkreten Handlung der Person',
                'sekundaer',
                'Says AI should be open source, then closes model access')
    """)
    print("[OK] Category HA (action-related) added")
except sqlite3.IntegrityError:
    print("[SKIP] Category HA already exists")

conn.commit()

# ============================================================
# VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("UPDATE v2 COMPLETED")
print("=" * 60)

# Count table rows
for table in ["personen", "plattformen", "quellen_typen", "kategorien",
              "aussagen", "aussagen_kategorien", "suchprotokolle",
              "handlungen", "aussagen_handlungen"]:
    count = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"  {table:25s} -> {count:4d} entries")

print("-" * 60)
print("Views:")
for view in ["v_aussagen_komplett", "v_aussagen_mit_kategorien",
             "v_statistik_personen", "v_statistik_kategorien",
             "v_sagen_vs_handeln"]:
    try:
        cur.execute(f"SELECT * FROM {view} LIMIT 1")
        print(f"  {view:35s} -> OK")
    except Exception as e:
        print(f"  {view:35s} -> ERROR: {e}")

print("-" * 60)
print("Columns in aussagen (statements):")
for col in cur.execute("PRAGMA table_info(aussagen)").fetchall():
    print(f"  {col[1]:30s} {col[2]:10s} {'NOT NULL' if col[3] else ''}")

print("-" * 60)
print("Action types (handlung_typ):")
# From CHECK constraint -- listed manually here
typen = ['investition', 'verkauf', 'kauf', 'umstrukturierung', 'gruendung',
         'ruecktritt', 'entlassung', 'einstellung', 'lobbying', 'spende',
         'klage', 'partnerschaft', 'produktlaunch', 'politisch', 'sonstiges']
for t in typen:
    print(f"  - {t}")

print("=" * 60)

conn.close()
