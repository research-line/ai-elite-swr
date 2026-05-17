# Quellencheck Paper B -- 2026-05-17

## Projekt

- Projekt: `PP__SWR_AB`, Paper B / SWR-Methodenpaper
- Geprüfte Ausgangsfassung: `paper_B/SWR_v3_en.tex`, `paper_B/SWR_v3_ger.tex`
- Neue lokale Fassung: `paper_B/SWR_v4_en.tex`, `paper_B/SWR_v4_ger.tex`, `paper_B/SWR_v4_kombi.pdf`
- Live-Zenodo-Stand vor Check: Concept DOI `10.5281/zenodo.18736720`, latest Record `19358418`, Version `6.0`, Live-Dateien `SWR_v3_en.pdf` und `SWR_v3_ger.pdf`

## Externe Quellenprüfung

Geprüft wurden die Paper-B-Bibliographie und der Live-Zenodo-Stand gegen DOI/Crossref, arXiv, PMLR und Zenodo API.

Primär geprüfte Records:

- Zenodo API: `https://zenodo.org/api/records/18736720`
- Barros et al. 2024: `https://arxiv.org/abs/2411.14473`
- Ge et al. 2024: `https://arxiv.org/abs/2406.20094`
- Santurkar et al. 2023: `https://proceedings.mlr.press/v202/santurkar23a.html`
- Ornstein et al. 2025: `https://doi.org/10.1017/psrm.2024.64`
- Hornby 2025: `https://doi.org/10.54195/technophany.18134`
- Wang et al. 2025: `https://doi.org/10.1145/3711022`
- Tai et al. 2024: `https://doi.org/10.1177/16094069241231168`
- Kommers et al. 2026: `https://doi.org/10.3389/frai.2026.1753041`
- Ziems et al. 2024: `https://doi.org/10.1162/coli_a_00502`
- Weitere DOI-Ergänzungen: Argyle `10.1017/pan.2023.2`, Bail `10.1073/pnas.2314021121`, Braun/Clarke `10.1191/1478088706qp063oa`, Fugard/Potts `10.1080/13645579.2015.1005453`, Guest `10.1177/1525822X05279903`, Hallgren `10.20982/tqmp.08.1.p023`, Messeri/Crockett `10.1038/s41586-024-07146-0`, Norman `10.1007/s10459-010-9222-y`, Soysal/Türkmen `10.59455/qietp.19`, Trope/Liberman `10.1037/a0018963`

## Korrekturen

- Ornstein et al. korrigiert von `13(1), 47--64` auf `13(2), 264--281`, DOI ergänzt.
- Hornby korrigiert von 2024 auf 2025, Titel auf den DOI-Record reduziert, Seiten `1--31` und DOI ergänzt.
- Santurkar et al. von Kurzangabe `Proc. ICML 2023` auf PMLR `202, 29971--30004` mit Primär-URL erweitert.
- Tai et al. von `23, 1--14` auf Artikelnummer `16094069241231168` mit DOI erweitert.
- Wang et al. von `9(CSCW), Article 124` auf `9(2), Article 124, 1--28` mit DOI erweitert.
- DOI-/URL-Felder für die übrigen geprüften Zeitschriften-, arXiv-, PMLR- und Zenodo-Quellen ergänzt.
- Beide Sprachfassungen auf `SWR_v4_*` angehoben; deutsche TeX-Quelle mechanisch auf echte Umlaute umgestellt.
- Alte v3-Artefakte archiviert unter `_archive/paper_B_v3_pre_quellencheck_2026-05-17/`.

## Verifikation

- EN/GER je mehrfach mit `pdflatex -interaction=nonstopmode -halt-on-error` gebaut.
- Finaler Logscan: keine LaTeX-Fehler, keine undefinierten Zitate/Referenzen, keine Rerun-Warnungen, keine Duplicate-Destination-Warnungen.
- Verbleibend: bestehende Overfull-HBoxen in Tabellen und Prompt-Appendix-Blöcken (`20` EN, `42` GER); nicht durch DOI-URLs ausgelöst und außerhalb dieses Quellenchecks belassen.
- Kombi-PDF mit `pypdf` aus EN+GER erstellt und per `pdfinfo` geprüft.
- Deutsche TeX-Quelle: keine `\"a/\"o/\"u`- oder `\ss`-Reste; `pdftotext -enc UTF-8` bestätigt echte Umlaute in der PDF-Textspur.

## Artefakte

| Datei | Seiten | MD5 | SHA256 |
|---|---:|---|---|
| `paper_B/SWR_v4_en.pdf` | 21 | `D20AA23A864F9ACF04A5893B604A8D09` | `56BC1DC419472402194B547C05DF147D9E03DF2DB5D51A36636EB52EE14F4552` |
| `paper_B/SWR_v4_ger.pdf` | 23 | `B01272F3C0341071EBEB9F8E0F5E1EAD` | `569E4B845122B3A6272F3D610541E9B5A3AAE5998D621A511BC8DB7F5B4FA244` |
| `paper_B/SWR_v4_kombi.pdf` | 44 | `8AC4CB4265A79B578A8F66A726809020` | `D77E88B30291741965913496B468AB7585D8FBD48ACD2621C076B073258CBC34` |

## Folgeaktion

Da Paper B bereits als Zenodo v6.0 live ist, ist ein New-Version-Upload erforderlich. Empfohlen: Zenodo `v6.1` oder `v7.0` mit `SWR_v4_en.pdf`, `SWR_v4_ger.pdf` und je nach aktueller Dateisatz-Konvention zusätzlich `SWR_v4_kombi.pdf`; dabei auch die bereits offene Zenodo-Description-Klarstellung zur Synthese-vs.-Rating-Trennung mitziehen.
