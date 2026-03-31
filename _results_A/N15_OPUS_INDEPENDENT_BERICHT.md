# N=15 Opus Independent Runs: Statistische Auswertung

> Erstellt: 2026-03-31
> Modell: Claude Opus 4.6 (N=15 unabhängige Einzelinstanz-Runs)
> Vergleich: Claude Haiku 4.5 (N=30 Runs, voller Op1+Op2 Prompt)
> Prompt: Identisch für alle Runs (Op1-Synthese + Op2-Rating mit exakten Skalenpolen)
> Design: Jeder Run = separate Agenten-Instanz (kein geteilter Kontext)

---

## 1. Einzelergebnisse Opus N=15

| Run | D01 | D02 | D03 | D04 | D05 | D06 | D07 | D08 | D09 | D10 | D11 | D12 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 01  | 9  | 8  | 9  | 8  | 8  | 8  | 7  | 9  | 5  | 7  | 5  | 7  |
| 02  | 9  | 8  | 9  | 8  | 7  | 9  | 7  | 9  | 6  | 7  | 5  | 8  |
| 03  | 9  | 8  | 8  | 8  | 7  | 7  | 6  | 9  | 6  | 7  | 5  | 7  |
| 04  | 9  | 8  | 9  | 8  | 7  | 9  | 6  | 8  | 7  | 7  | 6  | 8  |
| 05  | 8  | 8  | 9  | 8  | 7  | 8  | 5  | 9  | 6  | 7  | 6  | 7  |
| 06  | 9  | 8  | 9  | 8  | 7  | 9  | 6  | 9  | 6  | 8  | 5  | 7  |
| 07  | 9  | 8  | 9  | 8  | 7  | 8  | 6  | 8  | 7  | 7  | 6  | 8  |
| 08  | 8  | 8  | 9  | 8  | 7  | 8  | 6  | 9  | 7  | 6  | 5  | 7  |
| 09  | 8  | 8  | 9  | 8  | 7  | 8  | 6  | 8  | 6  | 7  | 5  | 7  |
| 10  | 9  | 8  | 9  | 8  | 7  | 9  | 6  | 9  | 7  | 6  | 6  | 8  |
| 11  | 9  | 8  | 9  | 9  | 7  | 8  | 5  | 9  | 7  | 7  | 6  | 8  |
| 12  | 8  | 8  | 9  | 9  | 7  | 8  | 6  | 9  | 7  | 6  | 6  | 8  |
| 13  | 9  | 8  | 9  | 9  | 7  | 8  | 6  | 9  | 7  | 7  | 6  | 8  |
| 14  | 9  | 8  | 9  | 9  | 7  | 8  | 4  | 8  | 7  | 6  | 6  | 8  |
| 15  | 9  | 8  | 9  | 8  | 7  | 8  | 6  | 9  | 7  | 7  | 6  | 7  |

---

## 2. Deskriptive Statistik

### Opus (N=15, unabhängige Einzelinstanzen)

| Dimension | Mean | SD | 95%-CI |
|-----------|------|-----|--------|
| D01 Mission | 8.73 | 0.46 | [8.5, 9.0] |
| D02 Efficacy | 8.00 | 0.00 | [8.0, 8.0] |
| D03 WorkEthic | 8.93 | 0.26 | [8.8, 9.1] |
| D04 Responsibility | 8.27 | 0.46 | [8.0, 8.5] |
| D05 TechnoDet | 7.07 | 0.26 | [6.9, 7.2] |
| D06 Progress | 8.20 | 0.56 | [7.9, 8.5] |
| D07 PowerConc | 5.87 | 0.74 | [5.5, 6.3] |
| D08 Urgency | 8.73 | 0.46 | [8.5, 9.0] |
| D09 HumanAppr | 6.53 | 0.64 | [6.2, 6.9] |
| D10 Posthuman | 6.80 | 0.56 | [6.5, 7.1] |
| D11 Egalitar | 5.60 | 0.51 | [5.3, 5.9] |
| D12 Control | 7.53 | 0.52 | [7.2, 7.8] |

### Haiku (N=30, voller Prompt)

| Dimension | Mean | SD | 95%-CI |
|-----------|------|-----|--------|
| D01 Mission | 7.23 | 1.36 | [6.7, 7.7] |
| D02 Efficacy | 7.20 | 1.13 | [6.8, 7.6] |
| D03 WorkEthic | 8.33 | 0.92 | [8.0, 8.7] |
| D04 Responsibility | 7.60 | 1.33 | [7.1, 8.1] |
| D05 TechnoDet | 6.13 | 1.53 | [5.6, 6.7] |
| D06 Progress | 7.13 | 1.36 | [6.6, 7.6] |
| D07 PowerConc | 5.67 | 1.71 | [5.0, 6.3] |
| D08 Urgency | 7.07 | 1.36 | [6.6, 7.6] |
| D09 HumanAppr | 7.60 | 1.04 | [7.2, 8.0] |
| D10 Posthuman | 4.80 | 2.06 | [4.0, 5.6] |
| D11 Egalitar | 6.30 | 1.64 | [5.7, 6.9] |
| D12 Control | 7.27 | 1.28 | [6.8, 7.7] |

---

## 3. Inter-Modell-Vergleich (Welch t-Tests)

| Dimension | Opus Mean | Haiku Mean | Δ | t | p | Sig? |
|-----------|-----------|------------|---|---|---|------|
| D01 Mission | 8.73 | 7.23 | +1.50 | 5.47 | 0.000 | *** |
| D02 Efficacy | 8.00 | 7.20 | +0.80 | 3.89 | 0.001 | *** |
| D03 WorkEthic | 8.93 | 8.33 | +0.60 | 3.31 | 0.002 | ** |
| D04 Responsibility | 8.27 | 7.60 | +0.67 | 2.47 | 0.018 | * |
| D05 TechnoDet | 7.07 | 6.13 | +0.93 | 3.26 | 0.003 | ** |
| D06 Progress | 8.20 | 7.13 | +1.07 | 3.72 | 0.001 | *** |
| D07 PowerConc | 5.87 | 5.67 | +0.20 | 0.55 | 0.588 | n.s. |
| D08 Urgency | 8.73 | 7.07 | +1.67 | 6.05 | 0.000 | *** |
| D09 HumanAppr | 6.53 | 7.60 | -1.07 | -4.24 | 0.000 | *** |
| D10 Posthuman | 6.80 | 4.80 | +2.00 | 4.97 | 0.000 | *** |
| D11 Egalitar | 5.60 | 6.30 | -0.70 | -2.14 | 0.039 | * |
| D12 Control | 7.53 | 7.27 | +0.27 | 0.99 | 0.329 | n.s. |

---

## 4. Batch-1-Vergleich

| Dimension | Opus Mean | 95%-CI | Batch-1 | Δ | In CI? |
|-----------|-----------|--------|---------|---|--------|
| D01 Mission | 8.73 | [8.5, 9.0] | 8 | -0.73 | no |
| D02 Efficacy | 8.00 | [8.0, 8.0] | 8 | +0.00 | YES |
| D03 WorkEthic | 8.93 | [8.8, 9.1] | 8 | -0.93 | no |
| D04 Responsibility | 8.27 | [8.0, 8.5] | 7 | -1.27 | no |
| D05 TechnoDet | 7.07 | [6.9, 7.2] | 8 | +0.93 | no |
| D06 Progress | 8.20 | [7.9, 8.5] | 7 | -1.20 | no |
| D07 PowerConc | 5.87 | [5.5, 6.3] | 6 | +0.13 | YES |
| D08 Urgency | 8.73 | [8.5, 9.0] | 8 | -0.73 | no |
| D09 HumanAppr | 6.53 | [6.2, 6.9] | 5 | -1.53 | no |
| D10 Posthuman | 6.80 | [6.5, 7.1] | 7 | +0.20 | YES |
| D11 Egalitar | 5.60 | [5.3, 5.9] | 5 | -0.60 | no |
| D12 Control | 7.53 | [7.2, 7.8] | 8 | +0.47 | no |

---

## 5. Zusammenfassung

| Metrik | Wert |
|--------|------|
| **Opus N** | 15 (unabhängige Einzelinstanzen) |
| **Haiku N** | 30 (voller Prompt) |
| **Inter-Modell MAE** | 0.96 |
| **Signifikante Differenzen** | 10/12 (p<0.05) |
| **Opus IMIIRR ICC(3,1)** | 0.847 (single measures, consistency) |
| **Opus IMIIRR ICC(2,k)** | 0.988 (average measures, agreement) |
| **Opus Mean SD** | 0.45 (vs. Haiku 1.39 — 3× konsistenter) |
| **Batch-1 in Opus 95%-CI** | 3/12 |
| **Batch-1 MAE vs Opus Mean** | 0.73 |
| **Batch-1 MAE vs Haiku Mean** | 1.05 |

---

## 6. Interpretation

### IMIIRR (Intra-Model Inter-Instance Rating Reliability)
ICC(3,1) = 0.847 (single measures, consistency) und ICC(2,k) = 0.988 (average measures, agreement)
über N=15 unabhängige Opus-Instanzen. Dies bestätigt, dass dasselbe Modell bei identischem Prompt
und identischen Daten ein **hochkonsistentes** Weltbild-Profil produziert, auch wenn jede Instanz
vollständig unabhängig arbeitet.

Bemerkenswert: D02 (Self-efficacy) zeigt **perfekte Übereinstimmung** — alle 15 Instanzen vergeben
exakt den Wert 8. Die meisten Dimensionen variieren nur um ±1 Punkt (Mean SD = 0.45).

### Inter-Modell-Vergleich (IMIRR)
MAE = 0.96 zwischen Opus und Haiku. 10/12 Dimensionen zeigen signifikante Unterschiede (p<0.05).

**Systematische Modellunterschiede:**
- Opus sieht ein **intensiveres** Profil: höher auf D01 Mission (+1.50), D08 Urgency (+1.67),
  D10 Posthuman (+2.00), D06 Progress (+1.07)
- Haiku sieht ein **humanistischeres** Profil: höher auf D09 HumanAppr (+1.07), D11 Egalitar (+0.70)
- **Konvergierende Dimensionen:** D07 PowerConc (p=0.588) und D12 Control (p=0.329) — keine
  signifikanten Modellunterschiede

**Methodische Hierarchie:**
- IMIIRR (selbes Modell, verschiedene Instanzen): ICC=0.847, Mean SD=0.45 → **hohe** Konsistenz
- IMIRR (selber Anbieter, verschiedene Modelle): MAE=0.96, 10/12 sig. → **moderate** Konsistenz
- Cross-Provider (verschiedene Anbieter): nicht getestet → Aufgabe anderer Forscher

### Batch-1 als Ausreißer
Der ursprüngliche Batch-1-Wert [8,8,8,7,8,7,6,8,5,7,5,8] liegt nur in 3/12 Opus-CIs.
MAE zum Opus-Mean: 0.73. Da die Opus-CIs extrem eng sind (Mean SD=0.45), fallen selbst
moderate Abweichungen außerhalb. Dies bestätigt: N=1-Messungen liefern keine belastbaren
Profilschätzungen. Der N=15-Mean ist die methodisch korrekte Referenz.

### Variabilitätsvergleich
Opus Mean SD (0.45) vs. Haiku Mean SD (1.39): Opus ist **3× konsistenter** als Haiku.
Dies spiegelt vermutlich die höhere Modellkapazität wider — ein leistungsfähigeres Modell
konvergiert stärker auf eine bestimmte Interpretation der Daten.

---

*Erstellt: 2026-03-31 | Autor: Claude Opus 4.6 | Design: 15 unabhängige Einzelinstanzen*