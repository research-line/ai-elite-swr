# Daten-/Strukturdesign Paper A 2026-07-04

Projekt: `PP__SWR_AB`  
Paper: Paper A / KI-Elite (`paper_A/KI_Elite_v3_en.tex`, `paper_A/KI_Elite_v3_ger.tex`)  
Automation: `research-data-and-structural-design`  
Datum: 2026-07-04  

## Auswahlgrund

Paper B hatte am 2026-06-03 bereits einen dedizierten Daten-/Strukturdesignlauf. Für Paper A stand im aktuellen Register kein eigener Daten-/Strukturdesigncheck; zugleich hatte der Forschungsstands-Nachcheck vom 2026-06-26 eine belegte neue Tabellenaufgabe geliefert: einen expliziten Crosswalk zwischen Techno-Supremacy-/2026er Literatur und den vorhandenen SWR-Dimensionen.

Der Arbeitsbaum war vor der Bearbeitung bereits dirty und `master` lag einen Commit hinter `origin/master`. Bestehende Änderungen in `paper_A/KI_Elite_v3_ger.tex`, `paper_A/KI_Elite_v3_ger.pdf`, `paper_A/KI_Elite_v3_kombi.pdf`, `paper_B/SWR_v4_ger.tex`, `paper_B/SWR_v4_ger.pdf`, `paper_B/SWR_v4_kombi.pdf` und `paper_A/tmp_stilcheck_de_paper_a_2026-06-25.txt` wurden nicht zurückgesetzt.

## Prüfung

Gelesen/geprüft:

- `FORSCHUNGSSTAND.md`, besonders Update 2026-06-26
- `UNTERSUCHUNGSERGEBNISSE.md` als Ergebnis-Truth
- `TODO.md` und `AKTIONSPLAN.md`
- `paper_A/KI_Elite_v3_en.tex` und `paper_A/KI_Elite_v3_ger.tex`
- Quellenpaket `_sources/2026-06-26_forschungsstand/README.md`
- PDF-Validierung `_sources/2026-06-26_forschungsstand/PDF_VALIDATION_2026-06-26.json`

## Befund

Die vorhandenen Ergebnis-Tabellen und Abbildungen tragen den empirischen Kern weiterhin gut: RQ-Tabellen, Heatmap, Zeitreihen, Korrelationen, Sagen-Handeln-Figur, Typen-/Subgruppenübersichten und Validierungsübersicht sind nicht redundant, sondern decken unterschiedliche Ebenen ab.

Der akute Präsentations-Gap lag in der Diskussions-Einordnung: Die validierten 2026er Quellen waren bereits projektlokal gesichert, aber noch nicht sichtbar gegen die vorhandenen SWR-Oberflächen, Befunde und Claim-Grenzen gemappt. Ohne Tabelle drohte entweder Unterintegration der neuen Literatur oder eine Überdehnung der Paper-A-Claims.

## Umsetzung

Sofort umgesetzt:

- EN: neue Tabelle `tab:research_update_ledger` in `Situating the Findings in the Literature`.
- GER: neue Tabelle `tab:forschungsupdate_ledger` in `Einordnung in den Forschungsstand`.
- Vier 2026er Bibitems synchron in EN/GER ergänzt:
  - Amin et al. 2026 zu GenAI-Persona-Evaluation
  - Birhane et al. 2026 zu Big-AI-Regulatory-Capture
  - Cruzesa 2026 zu AI Infrastructure Sovereignty
  - Pérez-Urbina 2026 zur Techno-Supremacy Doctrine

Die neue Tabelle ordnet Techno-Supremacy, Regulatory Capture, Infrastruktur-Souveränität und GenAI-Persona-Evaluation den bestehenden SWR-Ankern zu und setzt pro Zeile eine Claim-Grenze. Sie ergänzt keine neuen Ratings, keine neuen Messwerte und keine Kausal- oder Intentionsbehauptungen.

## Empfohlen

Für v9/Journal empfohlen:

- Den kompakten Forschungsupdate-Ledger zu einer vollständigen TSD-SWR-Crosswalk-Tabelle mit `TSD_pattern`, `SWR_dimension`, `elite_cluster`, `text_evidence`, `counter_evidence`, `claim_limit` ausbauen. Begründung: Der aktuelle Ledger verbessert die Datenpräsentation und begrenzt Claims, ersetzt aber noch keine quellnahe Evidenzmatrix.
- Regulatory-Capture- und Infrastruktur-Souveränität als eigenes Governance-Ledger prüfen. Begründung: So bleiben empirische Weltbildrekonstruktion, institutionelle Capture-Mechanismen und materielle Infrastrukturmacht analytisch getrennt.
- Falls der 2026-Block weiter wächst, die Forschungsstandseinordnung in klassische Theorieanker und `2026 Research Update` gliedern. Begründung: Weitere 2026er Artefakte würden den aktuellen Diskussionsabschnitt sonst überladen.

## Verifikation

Build:

- `pdflatex -interaction=nonstopmode -halt-on-error KI_Elite_v3_en.tex` zweimal erfolgreich.
- `pdflatex -interaction=nonstopmode -halt-on-error KI_Elite_v3_ger.tex` zweimal erfolgreich.
- `pdfunite KI_Elite_v3_en.pdf KI_Elite_v3_ger.pdf KI_Elite_v3_kombi.pdf` erfolgreich.

Harter Logscan:

- Keine Treffer auf `LaTeX Error`, `Undefined control sequence`, undefinierte Zitate, undefinierte Referenzen, `Rerun to get`, `Overfull`, `Fatal error`, `Emergency stop` oder `Missing character`.
- Verblieben sind nur nicht blockierende `Underfull \hbox`-Hinweise und der bekannte MiKTeX-Update-Hinweis.

PDFs:

| Datei | Seiten | SHA-256 |
|---|---:|---|
| `paper_A/KI_Elite_v3_en.pdf` | 48 | `C2D767A1528CABC2D3CE5CBE63AAE2EBD1C6FBD73B9AD01F5B0FCD841085418A` |
| `paper_A/KI_Elite_v3_ger.pdf` | 53 | `A84D505A3182CEDC1CFDB38A65B3F035AB69B8AFD5C7CA193BDBAB2346C1984F` |
| `paper_A/KI_Elite_v3_kombi.pdf` | 101 | `48DE3D5E502575BF602A11FD94AC941102D6705E36F47DF818F184BC61805FA1` |

PDF-Textspur:

- EN enthält `Table 11: 2026 research-update ledger for Paper A`, `Presentation gain`, `Claim boundary` und `Infrastructure-sovereignty constraint`.
- GER enthält `Tabelle 11: Forschungsupdate-Ledger 2026 für Paper A`, `Präsentationsgewinn`, `Claim-Grenze`, `Infrastruktur-Souveränitätsgrenze` und `prüfbare Capture-Mechanismen`.

## Git-/Upload-Status

Kein Zenodo-Upload in diesem Lauf. Git-Commit/Push ist wegen vorbestehendem dirty Arbeitsbaum und Branch-Rückstand nur nach separater Bereinigung sicher. Die in diesem Lauf relevanten eigenen Änderungen betreffen die neuen Paper-A-Tabellen/Bibitems, die neu gebauten Paper-A-PDFs, dieses Ergebnisdokument sowie Projekt-/Root-Registereinträge.
