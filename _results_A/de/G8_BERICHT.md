# G8: Aggregierte Einzelprofile vs. Direkte Gruppensynthese

> Datum: 2026-03-30
> Methode: Vergleich der D01-D12 Ratings aus zwei Ansätzen
> Script: `g8_aggregation_comparison.py`
> Daten: `g8_comparison_results.json`

---

## Fragestellung

Liefert die direkte Gruppensynthese (alle Daten einer Gruppe → Claude → Weltbild) dasselbe Ergebnis wie die Aggregation individueller Profile (100 Einzelprofile → Gruppen-Mittelwert)?

## Methode

- **Aggregierter Ansatz:** D01-D12 Mittelwerte aus den 100 Einzelprofil-Ratings (Claude Sonnet 4.5) pro Gruppe berechnet
- **Direkter Ansatz:** D01-D12 Ratings aus den direkten Gruppen-Synthesen (Batch 4), die aus gepoolten Rohdaten erzeugt wurden
- **Metriken:** Pearson r, MAE, RMSE, Amplifikationsanalyse
- **15 Gruppen** verglichen: 4 Rollen, 3 Firmen, 6 Haltungen, 2 Gender

## Ergebnisse

### Konvergenz-Metriken

| Gruppe | n | Pearson r | MAE | RMSE | Bewertung |
|--------|---|-----------|-----|------|-----------|
| CEOs | 19 | 0.572 | 1.67 | 2.02 | Akzeptabel |
| Akademiker | 12 | 0.807 | 0.51 | 0.68 | Gut |
| Investoren | 8 | 0.608 | 2.29 | 2.66 | Schwach |
| Gründer | 36 | 0.614 | 1.13 | 1.48 | Akzeptabel |
| Anthropic | 9 | 0.777 | 0.73 | 0.94 | Gut |
| OpenAI | 7 | 0.774 | 1.06 | 1.31 | Gut |
| Google/DM | 7 | 0.489 | 1.85 | 2.25 | Schwach |
| Open Source | 6 | 0.857 | 0.75 | 0.91 | Gut |
| Closed Source | 5 | 0.567 | 1.08 | 1.22 | Akzeptabel |
| Risiko-Warner | 6 | 0.715 | 1.56 | 1.82 | Akzeptabel |
| Beschleuniger | 7 | 0.855 | 1.21 | 1.29 | Gut |
| Reg-Pro | 8 | 0.759 | 0.86 | 1.18 | Gut |
| Reg-Contra | 5 | 0.715 | 1.17 | 1.34 | Gut |
| Frauen | 10 | 0.428 | 1.02 | 1.27 | Schwach |
| Männer | 90 | 0.549 | 2.56 | 2.78 | Schwach |
| **GESAMT** | | **0.623** | **1.30** | **1.66** | |

### Dimensionale Verzerrungen

| Dimension | Avg Delta | Richtung |
|-----------|-----------|----------|
| D01 Sendungsbewusstsein | +1.76 | Direkte Synthese HÖHER |
| D02 Selbstwirksamkeit | +0.40 | ~Gleich |
| D03 Arbeitsethik | +1.64 | Direkte Synthese HÖHER |
| D04 Verantwortung | +0.66 | Direkte Synthese HÖHER |
| D05 Techno-Determinismus | -0.58 | Direkte Synthese TIEFER |
| D06 Fortschrittsoptimismus | +0.52 | Direkte Synthese HÖHER |
| D07 Machtkonzentration | +1.71 | Direkte Synthese HÖHER |
| D08 Dringlichkeit | +0.38 | ~Gleich |
| D09 Menschliche Wertschätzung | -0.13 | ~Gleich |
| D10 Posthumanismus | +0.39 | ~Gleich |
| D11 Egalitarismus | -0.65 | Direkte Synthese TIEFER |
| D12 Kontrollüberzeugung | +0.66 | Direkte Synthese HÖHER |

### Amplifikationseffekt

- **71.7%** aller Dimension-Gruppen-Kombinationen werden durch direkte Synthese **verstärkt** (weiter vom Skalenmittelpunkt)
- **23.9%** werden gedämpft
- **4.4%** bleiben gleich

## Interpretation

### 1. Moderate Konvergenz (r = 0.623)
Die beiden Ansätze liefern keine identischen, aber deutlich korrelierte Ergebnisse. Die Rangfolge der Dimensionen bleibt weitgehend erhalten — wer in der Aggregation hoch/niedrig ist, ist es tendenziell auch in der direkten Synthese.

### 2. Systematischer Amplifikationseffekt
Die direkte Gruppensynthese erzeugt **schärfere Konturen** als die Einzelprofil-Aggregation. Dies ist interpretierbar als:
- **Kohärenz-Verstärkung:** Wenn alle Daten einer Gruppe gebündelt werden, identifiziert das LLM dominante Muster stärker
- **Averaging-Dämpfung:** Einzelprofile haben natürliche Varianz, die beim Mitteln die Extremwerte abflacht
- **Analogie:** Ähnlich wie Gruppenidentität in der Sozialpsychologie (Group Polarization) schärfer ist als der Durchschnitt der Individuen

### 3. Heterogene Konvergenz
- **Beste Konvergenz (r > 0.75):** Akademiker, Open Source, Beschleuniger, Anthropic, OpenAI, Reg-Pro, Reg-Contra — ideologisch kohärente Gruppen
- **Schwächste Konvergenz (r < 0.55):** Frauen, Google/DM, Männer — heterogenere Gruppen
- **Muster:** Je ideologisch homogener die Gruppe, desto besser die Konvergenz

### 4. Investoren als Ausreißer
Die Investoren-Gruppe (r=0.608, MAE=2.29) zeigt den stärksten Amplifikationseffekt (D07 Machtkonzentration: Delta +6.2). Die direkte Synthese zeichnet ein extrem zugespitztes Bild; die Einzelprofile sind moderater.

## Methodische Implikationen

1. **Beide Ansätze sind komplementär:** Aggregation = konservativer, direkter = expressiver
2. **Für das Paper:** Die Gruppensynthese-Ratings (direkt) beibehalten, aber den Amplifikationseffekt als methodisches Merkmal berichten
3. **Run-Konvergenz (G1):** Muss als nächstes auf den direkten Gruppen-Synthesen getestet werden
4. **Expected-Discrepancy (G6):** Muss den Amplifikationseffekt als Baseline berücksichtigen

---
*Analyse: Claude Opus 4.6 | Daten: 100 Einzelprofile (Sonnet 4.5) + 15 Gruppen-Synthesen (Sonnet 4.5)*
