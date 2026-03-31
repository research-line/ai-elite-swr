# Changelog v6.0 -- KI-Elite Paper A

> Zenodo Concept-DOI: 10.5281/zenodo.18736737
> Aktuelle Version: v5.0 (Record 19073386, 2026-03-17)
> Neue Version: v6.0 (geplant)
> Dateien: KI_Elite_v2_en.pdf, KI_Elite_v2_ger.pdf (OHNE Kombi)

---

## Versionshistorie

| Version | Record-ID  | Datum      | Dateien                          |
|---------|------------|------------|----------------------------------|
| v1.0    | 18736738   | 2026-02-23 | EN, DE, Kombi                    |
| v2.0    | 18854319   | 2026-03-03 | EN, DE, Kombi (nach K4-Review)   |
| v3.0    | 18911501   | 2026-03-08 | DE, Kombi                        |
| v4.0    | 19056560   | 2026-03-16 | DE, Kombi                        |
| v5.0    | 19073386   | 2026-03-17 | EN, DE, Kombi                    |
| **v6.0**| *pending*  | 2026-03-30 | **EN, DE** (ohne Kombi)          |

---

## Änderungen v5.0 → v6.0

### 1. Paradigmenwechsel: Individual → Group-Level Analyse

- Gesamtes Paper von Einzelperson-Profilen auf **Gruppen-Synthesen** umgestellt
- 15 Gruppen-Synthesen statt 100 Einzelprofile als primäre Analyseebene
- Einzelprofile dienen nur noch als Datenprovider für Gruppensynthesen
- HDBSCAN-Validierung: Keine natürlichen Cluster in 12D → Weberian Ideal Types bestätigt
- Terminologie: "Synthesis Units (SU)" statt "Töpfe"
- "Data Aggregation Procedure" als neue Subsektion eingefügt

### 2. Vier neue Validierungsexperimente

- **G1 Run-Konvergenz (Test-Retest-Reliabilität):**
  5 Gruppen × 2 unabhängige Runs (Claude Opus 4.6). Gesamt r=0.908, ICC=0.902, MAE=0.40. Messgenauigkeit: ±0.2 Skalenpunkte.

- **G5 Cross-Modal Prediction (Instanztrennung):**
  50 Vorhersagen aus 5 Gruppen, strikte Trennung Op4a/Op4b. 72% confirmed, 26% plausible, 0% contradicted. v1 (kontaminiert) archiviert und als invalidiert markiert.

- **G6 Expected-Discrepancy Kontrollexperiment:**
  Fiktive konsistente Gruppe (Umweltwissenschaftler, 30 Aussagen + 30 Handlungen). Aussagen↔Handlungen r=0.912, MAE=0.50. KI-Elite-Gap (MAE=1.25) ist 2.5× größer → Gap ist real, nicht LLM-Artefakt.

- **G8 Aggregation vs. Direkte Gruppensynthese:**
  15 Gruppen verglichen. Pearson r=0.623. Amplifikationseffekt bei 71.7% der Dimensionen. Beste Konvergenz: Open Source (r=0.857), Beschleuniger (r=0.855).

### 3. Blindungstest

- Platzhalter-Robustheit bestätigt (r=0.987)
- Terminologie korrigiert: "Contamination Control" → "Focus Control"

### 4. Methodik selbstständig

- Paper A ist jetzt **vollständig selbstständig** lesbar (kein Companion Paper nötig)
- Methodik-Sektion erweitert: Inverse Problem, Fictional Synthetic Person, 5-Schritte-Protokoll
- SWR-Companion-Paper nur noch als "see also" referenziert
- SWR-Framework (Paper B): V1 umgeschrieben, Run-Konvergenz statt Inter-LLM als Primärvalidierung

### 5. Systematische Bereinigung (Phase 1-3)

- **Phase 1 (Entkernung):** 7 fabricierte Behauptungen entfernt, BAD_BANK.md erstellt
- **Phase 2 (Auffüllung):** 6 fehlende Informationen eingefügt (Datendichte, Qualität, Filterung, Kodierung, AI Disclosure)
- **Phase 3 (Kohärenz-Sweep):** 10 Inkonsistenzen gefixt, 90 Referenzen geprüft (5 Fehler korrigiert)
- PersonaCite-Referenz korrigiert (halluzinierter Autor "Rawal" → "Truss")
- Op4/Op5 korrekt als nicht-durchgeführt markiert

### 6. Grafiken und Abbildungen

- fig1-fig7 aktualisiert (7 PNG + 7 SVG in `_results_A/figures/`)
- Statistische Analysen: PCA, Kruskal-Wallis, Cliff's delta, Spearman berechnet und eingebaut

### 7. Ordnerstruktur aufgeräumt

- Paper B archiviert → `_archive/paper_B_v2/`
- `_results_A/` reorganisiert: `toepfe/` → `synthesis_units/`, Review-Chains → `_archive/`
- `_data_A/` in 4 Unterordner: `collect/`, `coding/`, `insert/`, `tools/`
- Kombi-Datei archiviert (v2_kombi.* → `_archive/`)
- 29 englische Übersetzungen in `_results_A/translations_en/`
- 9 Schlüssel-Scripts DE→EN übersetzt

### 8. Weitere Korrekturen

- Bibitem-Referenzen bereinigt (M4)
- Spearman/Hedging-Formulierungen korrigiert (M6)
- Anhänge aktualisiert (M7)
- D02 Benennungsfehler: "locus of control" → "self-efficacy"
- TESCREAL-Framework integriert (Torres & Gebru 2024)
- Hermeneutik des Verdachts (Ricoeur 1970) eingebaut
- DE-Versionen synchronisiert (11 Änderungsblöcke KI-Elite, 4 SWR)

---

## Bekannte offene Punkte (NICHT in v6.0 enthalten)

- [ ] Grafiken fig1-fig7 Labels prüfen (vor/nach Gruppen-Shift)
- [ ] README.md (GitHub) auf Gruppen-Framing reframen
- [ ] BibTeX-Migration (erst bei Journal-Target)
- [ ] LinkedIn-Post aktualisieren
- [ ] Zenodo Keywords bereinigen (TODO-Text in Keywords-Feld entfernen!)

---

## Upload-Checkliste

- [ ] PDFs vorhanden: `paper_A/KI_Elite_v2_en.pdf` ✓, `paper_A/KI_Elite_v2_ger.pdf` ✓
- [ ] Kombi-PDF NICHT hochladen (archiviert)
- [ ] Record-ID für `--new-version`: **19073386** (aktueller Record)
- [ ] Auto-Versionierung: v6.0 (5 bestehende Versionen + 1)
- [ ] Zenodo Keywords bereinigen (TODO-Artefakt entfernen)
- [ ] ORCID-ID ergänzen: 0009-0005-7296-1534
- [ ] Quellencheck aller Literaturverzeichnis-Einträge (Pflicht laut CLAUDE.md)

### Upload-Befehl (Entwurf)

```bash
PYTHONIOENCODING=utf-8 python "C:/Users/User/OneDrive/.RESEARCH/_tools/paper_publisher.py" \
  "C:/Users/User/OneDrive/.RESEARCH/.PRIO-1/PP_SWR_AB" \
  --step zenodo \
  --new-version 19073386 \
  --version 6.0 \
  --pdf "paper_A/KI_Elite_v2_en.pdf" \
  --pdf "paper_A/KI_Elite_v2_ger.pdf" \
  --dry-run
```

> WICHTIG: Zuerst mit `--dry-run` testen, dann ohne `--dry-run` hochladen.
> WICHTIG: Vor Upload Quellencheck durchführen (alle bibitem-Einträge per WebSearch verifizieren).

---

*Erstellt: 2026-03-30 | Autor: Lukas Geiger + Claude Opus 4.6*
