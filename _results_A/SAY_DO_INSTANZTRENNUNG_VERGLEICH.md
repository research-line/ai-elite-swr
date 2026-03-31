# Say-Do-Vergleich: Instanztrennung v1 vs v2

> Erstellt: 2026-03-31
> Modell: Claude Opus 4.6
> Methode: GA_ges_A und GA_ges_H in separaten Instanzen (v2) vs. selber Instanz (v1)

---

## Hintergrund

In v1 (2026-02-12) wurden GA_ges_A (Nur Aussagen) und GA_ges_H (Nur Handlungen) in **derselben Instanz** geratet (Batch 1: eine Rating-Datei mit komparativer Analyse). In v2 (2026-03-31) wurden sie in **separaten Instanzen** geratet — kein Agent sah die Daten des anderen.

---

## Ergebnisse

### Dimensionale Ratings

| Dimension | A (v1) | H (v1) | Gap v1 | A (v2) | H (v2) | Gap v2 | Shift |
|-----------|--------|--------|--------|--------|--------|--------|-------|
| D01 Mission | 8 | 7 | -1 | 9 | 9 | 0 | +1 |
| D02 Efficacy | 8 | 9 | +1 | 8 | 9 | +1 | 0 |
| D03 WorkEthic | 8 | 9 | +1 | 9 | 9 | 0 | -1 |
| D04 Responsibility | 7 | 5 | **-2** | 8 | 8 | **0** | +2 |
| D05 TechnoDet | 8 | 9 | +1 | 7 | 9 | +2 | +1 |
| D06 Progress | 7 | 6 | -1 | 8 | 8 | 0 | +1 |
| D07 PowerConc | 6 | 8 | +2 | 6 | 8 | +2 | 0 |
| D08 Urgency | 8 | 9 | +1 | 9 | 9 | 0 | -1 |
| D09 HumanAppr | 5 | 3 | -2 | 6 | 5 | -1 | +1 |
| D10 Posthuman | 7 | 8 | +1 | 7 | 7 | 0 | -1 |
| D11 Egalitar | 5 | 2 | **-3** | 5 | 3 | **-2** | +1 |
| D12 LocControl | 8 | 7 | -1 | 7 | 8 | +1 | +2 |
| **Avg** | **7.1** | **6.8** | | **7.4** | **7.7** | | |

### Statistische Zusammenfassung

| Metrik | v1 (selbe Instanz) | v2 (getrennt) | Veränderung |
|--------|-------------------|---------------|-------------|
| MAE (Aussagen↔Handlungen) | 1.42 | **0.75** | -47% |
| Pearson r | 0.817 | 0.801 | ≈ gleich |
| Max |Gap| | 3 (D11) | 2 (D07, D11) | -1 |
| Dimensionen mit Gap=0 | 0/12 | **7/12** | +7 |
| Dimensionen mit |Gap|≥2 | 5/12 | 2/12 | -3 |

### Vergleich mit G6 Kontrollgruppe

| Konfiguration | Kontrolle (G6) | KI-Elite | Ratio |
|---------------|---------------|----------|-------|
| **v1 (selbe Instanz)** | MAE=0.50 | MAE=1.42 | **2.8×** |
| **v2 (getrennt)** | MAE=0.92 | MAE=0.75 | **0.8×** |

---

## Interpretation

### 1. Der Say-Do-Gap war teilweise ein Instanz-Artefakt
Mit Instanztrennung schrumpft der Gap von MAE=1.42 auf MAE=0.75 (-47%). Der Rater, der in v1 beide Datentypen sah, hat die Unterschiede **amplified** — vermutlich weil die komparative Aufgabe (er sah die Kontrastierung als implizites Ziel) die Differenzierung verstärkte.

### 2. Der Gap fällt unter die Kontroll-Baseline
v2 KI-Elite MAE (0.75) < v2 G6 MAE (0.92). Der Say-Do-Gap ist mit Instanztrennung **kleiner** als das natürliche Rauschen der Methode bei separaten Instanzen. Das bedeutet: Mit Einzelmessungen kann der Gap nicht reliabel nachgewiesen werden.

### 3. Was bleibt bestehen?
- **D07 Machtkonzentration: Gap +2** (Handlungen konzentrieren Macht stärker als Aussagen) — stabil über v1 und v2
- **D11 Egalitarismus: Gap -2** (Handlungen weniger egalitär) — geschrumpft von -3, aber noch vorhanden
- **D05 Techno-Determinismus: Gap +2** (Handlungen deterministischer) — in v2 sogar stärker

### 4. Was verschwindet?
- **D04 Verantwortung:** Gap von -2 auf 0 — mit separater Instanz wird Handlungen ein ähnlich hohes Verantwortungsgefühl zugeschrieben wie Aussagen
- **D09 Human Appreciation:** Gap von -2 auf -1 — teilweise Artefakt
- **D01, D03, D06, D08, D10:** Alle Gaps verschwinden auf 0

### 5. Methodische Konsequenz
Die RQ3-Ergebnisse (Say-Do Gap) müssen im Paper **vorsichtiger formuliert** werden:
- Die qualitativen Richtungen stimmen (D07↑, D11↓ bei Handlungen)
- Die quantitativen Größen waren durch Instanz-Kontamination aufgebläht
- Für robuste Inferenz braucht man N=30 Runs pro Datentyp
- Das stärkste Argument bleibt D07/D11 (konsistent über v1 und v2)

---

## Empfehlung für Paper A

1. **RQ3 Absatz umschreiben:** "Preliminary single-run comparisons suggest directional say-do differences on D07 (power concentration) and D11 (egalitarianism), consistent across independent measurements. However, the magnitude of the overall gap is sensitive to instance separation and falls within the baseline noise range (G6 v2 control MAE=0.92). Formal quantification requires repeated measurements (N≥30)."
2. **D07 und D11 als stabilste Say-Do-Differenzen hervorheben** (Gap +2 bzw. -2 in beiden Versionen)
3. **Alte MAE=1.25/1.42 durch v2-Werte ersetzen** mit Transparenz über die Revision

---

*Erstellt: 2026-03-31 | Autor: Claude Opus 4.6*
