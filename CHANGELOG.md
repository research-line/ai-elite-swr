# CHANGELOG

All notable changes to the **Synthetic Worldview Reconstruction (SWR) — AI Elite** project are documented in this file.

## [v8.1.2] - 2026-07-27

### Discoverability & System Architecture Audit (Pfad B)
- **Mermaid Architecture Diagram**: Added visual GFM Mermaid pipeline diagram (`System Architecture & Pipeline Flow`) to `README.md` visualizing data collection, SQLite database, synthesis units, LLM synthesis, and validation suites.
- **Discoverability & LLM Context**: Updated `Last checked` timestamp to `2026-07-27` in `llms.txt` and `README.md`.
- **System Verification**: Re-verified syntax compilation of all Python data pipeline scripts (`python -m compileall .`) and SQLite database creation (`_data_A/tools/create_db.py`).

---

## [v8.1.1] - 2026-07-25

### Technical Hygiene & Maintenance
- **PEP 621 Standard Package**: Created `pyproject.toml` with standard package metadata, Python >=3.10 requirement, CC-BY-4.0 license, and `[tool.pytest.ini_options]` config.
- **Root Documentation**: Created canonical `CHANGELOG.md` consolidating release history and maintenance logs.
- **README & Badges**: Added Shields.io badges (Python 3.10+, CC-BY 4.0 License, Open Science, LLM-Ready) and GFM machine-readable callout note (`> [!NOTE]`) for `llms.txt`.
- **llms.txt Sync**: Synchronized `Last-checked` timestamp to 2026-07-25 and updated search anchors.
- **Code Compilation Verification**: Verified syntax and compilation of 100+ data pipeline scripts across `_data_A/`.

---

## [v8.1.0] - 2026-07-25

### Repository Discoverability & Zenodo Sync
- Updated Paper A Zenodo latest to v8.1 (Record `20686161`, DOI `10.5281/zenodo.20686161`).
- Updated `llms.txt` `Last checked` timestamp to 2026-07-25 and expanded RAG search keywords.
- Shields.io `llms.txt` badge integrated into `README.md`.

---

## [v8.0.0] - 2026-06-14

### Paper Version Updates
- Updated Paper A to v8.0 and Paper B to v6.1 in Zenodo records.
- Synchronized `README.md`, `CITATION.cff`, and `llms.txt` to active DOIs.

---

## [v6.0.0] - 2026-03-30

### Major Methodology & Pipeline Refactoring
- **Group-Level Analysis**: Refactored entire pipeline from individual profiles to 15 sociological group syntheses (Weberian ideal types confirmed via HDBSCAN).
- **Validation Experiments**:
  - G1 Run-Convergence: 5 groups × 2 independent runs (Claude Opus 4.6), ICC = 0.902, MAE = 0.40.
  - G5 Cross-Modal Prediction: 50 predictions, 72% confirmed, 0% contradicted.
  - G6 Expected-Discrepancy Control: Fictional group baseline MAE = 0.50 vs real gap MAE = 1.25.
  - G8 Aggregation vs Direct Group Synthesis: Pearson r = 0.623.
- **Blinding Test**: Placeholder robustness confirmed (r = 0.987).
- **Data Pipeline Reorganization**: Structured `_data_A/` into `collect/`, `coding/`, `insert/`, `tools/`.
