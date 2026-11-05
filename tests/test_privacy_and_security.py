"""Test suite for repository privacy, data protection, and leak prevention."""

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_no_confidential_files_tracked():
    res = subprocess.run(
        ["git", "ls-files"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    tracked_files = res.stdout.strip().splitlines()

    forbidden_patterns = [
        r"^BEWEISNOTIZ",
        r"^TODO",
        r"^PROJEKTPLAN",
        r"^KONZEPT",
        r"^AKTIONSPLAN",
        r"^GESAMTPLAN",
        r"^TEILPLAN",
        r"^DONE\.md$",
        r"^CLAUDE\.md$",
        r"^AGENTS\.md$",
        r"^ZENODO_CREDENTIALS",
        r"^CHECKS-REG",
        r"^CHECKS-LOG",
        r"_proof-notes",
        r"_bad_bank",
        r"\.env$",
        r"credentials\.json$",
    ]

    leaks = []
    for f in tracked_files:
        for pat in forbidden_patterns:
            if re.search(pat, f, re.IGNORECASE):
                leaks.append((f, pat))

    assert not leaks, f"Found confidential files tracked in git: {leaks}"


def test_gitignore_managed_block():
    gitignore_path = REPO_ROOT / ".gitignore"
    assert gitignore_path.exists(), ".gitignore must exist"
    content = gitignore_path.read_text(encoding="utf-8")
    assert "# >>> RESEARCH-PIPELINE MANAGED GITIGNORE >>>" in content
    assert "# <<< RESEARCH-PIPELINE MANAGED GITIGNORE <<<" in content
    assert "**/BEWEISNOTIZ.md" in content
    assert "**/TODO.md" in content
    assert "**/PROJEKTPLAN.md" in content


def test_no_unblinded_databases_in_repo():
    res = subprocess.run(
        ["git", "ls-files"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    tracked_files = res.stdout.strip().splitlines()
    for f in tracked_files:
        assert not f.endswith(".db"), f"Direct SQLite database {f} must not be tracked in git"
        assert not f.endswith(".db-wal"), f"WAL file {f} must not be tracked"
        assert not f.endswith(".db-shm"), f"SHM file {f} must not be tracked"
        assert "_raw_recovery" not in f, f"Raw recovery directory {f} must not be tracked"
