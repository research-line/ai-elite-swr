# Zitationscheck Paper B -- 2026-05-18

## Projekt

- Projekt: `PP__SWR_AB`, Paper B / SWR-Methodenpaper
- Geprüfte Dateien: `paper_B/SWR_v4_en.tex`, `paper_B/SWR_v4_ger.tex`
- Aktualisierte Artefakte: `paper_B/SWR_v4_en.pdf`, `paper_B/SWR_v4_ger.pdf`, `paper_B/SWR_v4_kombi.pdf`
- Auswahlgrund: Für Paper B lagen bereits Quellen-, German-Style-, Design- und LLM-Muster-Checks vor, aber noch kein zentral registrierter Zitationscheck. Frisch zitationsgeprüfte Projekte wie IUT-Forensik, Zeta Zoo, Spuk, Slepian-Pollak, Theologie/Paper B, HCT/abc, RH Even-Dominance, Frieden Article 1, Hodge, Metaphern, TAA, ADHS, Kant, CRM und Pali-Psycho wurden übersprungen.

## Befund vor Korrektur

- EN und GER hatten jeweils 29 aktive Cite-Keys und 29 Bibitems.
- Es gab keine fehlenden, unzitierten oder doppelten Cite-/Bibitem-Keys.
- Die Inline-Bibliographie war in beiden Sprachfassungen nicht alphabetisch sortiert.
- Die deutschen PDF-Metadaten verwendeten noch ASCII-Ersatzformen (`gestuetzt`, `Reliabilitaet`), obwohl die sichtbare deutsche Textspur bereits echte Umlaute hatte.

## Korrekturen

- Bibitems in `SWR_v4_en.tex` und `SWR_v4_ger.tex` identisch alphabetisch nach Key sortiert.
- Keine neuen Quellen hinzugefügt und keine Quellenmetadaten geändert; der Quellencheck vom 2026-05-17 hatte die Bibliographie bereits gegen DOI/Crossref, arXiv, PMLR und Zenodo API verifiziert.
- Deutsche `\hypersetup`-Metadaten auf echte Umlaute umgestellt: `LLM-gestützte Methodologie`, `Interinstanz-Reliabilität`.

## Verifikation

- `_tools/check_refs.py`: EN/GER jeweils 29 Cite-Keys und 29 Bibitems; keine fehlenden oder unzitierten Keys; Bibliographien alphabetisch sortiert.
- EN und GER mit `pdflatex -interaction=nonstopmode -halt-on-error` gebaut; GER nach Metadatenkorrektur erneut zweimal gebaut.
- Kombi-PDF per `pypdf` aus aktueller EN- und GER-PDF neu gemergt.
- Finaler Logscan ohne LaTeX-Fehler, Fatal Errors, Undefined Control Sequences, undefined references/citations, Citation-Warnings, Rerun-Hinweise oder Overfull-HBox-/VBox-Treffer.
- Seitenzahlen: EN 21 S., GER 23 S., Kombi 44 S.
- `pypdf` bestätigt echte Umlaute in den deutschen PDF-Metadaten; `pdftotext -enc UTF-8` bestätigt echte sichtbare Umlaute in GER/Kombi (`Fähigkeit`, `Äußerungen`, `übertragbaren`, `Qualität`, `gültig`, `Reliabilität`).

## Artefakte

| Datei | Seiten | MD5 | SHA256 |
|---|---:|---|---|
| `paper_B/SWR_v4_en.pdf` | 21 | `7DB8C775049279114C8496A803214483` | `93390478694E817B52F59B4E0A43D36148699BA8DB415E6BBD73089D686EFD1F` |
| `paper_B/SWR_v4_ger.pdf` | 23 | `90A8B0093F4947D80E199C9653A31325` | `D25F0F9B2111169940A5B79D18D38A47C8FDFAB7FCB1A4C009740C3FB5B74B49` |
| `paper_B/SWR_v4_kombi.pdf` | 44 | `A10FFFA8375C2DC0BC18B7766F9E23A2` | `B95F3FB848185569D16F58F76B4C7EAB454A7B5D4034B61E4BD3359D9A2DF781` |

## Folgeaktion

Kein Zenodo-Upload und kein GitHub-Sync in diesem Lauf. Zenodo Paper B bleibt live als v6.1 Record `20260688`; der lokale Zitations-/Metadaten-Cleanup sollte bei der nächsten Paper-B-Maintenance-Version mitgenommen werden.
