# N=30 Haiku-Runs: Intra-Familien-Inter-Modell-Vergleich (v2 — voller Prompt)

> Erstellt: 2026-03-31
> Modell: Claude Haiku 4.5 (N=30 Runs, voller Op1+Op2 Prompt)
> Referenz: Claude Opus 4.6 (GA_ges_AH, Batch 1)
> Prompt: Identisch mit Opus — volle Op1-Synthese + Op2-Rating mit exakten Skalenpolen

---

## Ergebnisse

| Dimension | Haiku Mean | Haiku SD | 95%-CI | Opus | Δ | In CI? |
|-----------|-----------|---------|--------|------|---|--------|
| D01 Mission | 7.2 | 1.4 | [6.6, 7.7] | 8 | -0.8 | ✗ |
| D02 Efficacy | 7.3 | 1.2 | [6.8, 7.7] | 8 | -0.7 | ✗ |
| D03 WorkEthic | 8.4 | 1.0 | [8.0, 8.8] | 8 | +0.4 | ✗ |
| D04 Responsibility | 7.7 | 1.3 | [7.2, 8.2] | 7 | +0.7 | ✗ |
| D05 TechnoDet | 6.0 | 1.6 | [5.4, 6.7] | 8 | **-2.0** | ✗ |
| D06 Progress | 7.2 | 1.4 | [6.6, 7.7] | 7 | +0.2 | ✓ |
| D07 PowerConc | 5.7 | 1.7 | [5.0, 6.3] | 6 | -0.3 | ✓ |
| D08 Urgency | 7.0 | 1.4 | [6.5, 7.6] | 8 | -1.0 | ✗ |
| D09 HumanAppr | 7.6 | 1.0 | [7.2, 8.0] | 5 | **+2.6** | ✗ |
| D10 Posthuman | 5.0 | 2.0 | [4.2, 5.7] | 7 | **-2.0** | ✗ |
| D11 Egalitar | 6.4 | 1.5 | [5.9, 7.0] | 5 | **+1.4** | ✗ |
| D12 Control | 7.4 | 1.4 | [6.8, 7.9] | 8 | -0.6 | ✗ |

---

## Zusammenfassung

| Metrik | Wert |
|--------|------|
| **N** | 25 (voller Op1+Op2 Prompt, identisch mit Opus) |
| **Inter-Modell MAE** | 1.06 (Haiku Mean vs. Opus) |
| **Opus in Haiku 95%-CI** | 2/12 Dimensionen |
| **Haiku Mean SD** | 1.40 (interne Variabilität) |
| **IMIIRR Opus** (Vergleich) | ICC=0.902, MAE=0.40 |

---

## Interpretation

### 1. Substantielle Intra-Familien-Inter-Modell-Differenzen
Nur 2/12 Opus-Werte (D06 Progress, D07 PowerConc) liegen im Haiku-95%-CI. Die übrigen 10 Dimensionen zeigen **systematische Modellunterschiede** trotz identischem Prompt und identischen Daten.

### 2. Haiku-Profil: Moderater und humanistischer
Haiku interpretiert dieselben Daten konsistent moderater:
- **Menschenfreundlicher:** D09 +2.6 (stärkste Differenz überhaupt)
- **Weniger techno-deterministisch:** D05 -2.0
- **Weniger posthumanistisch:** D10 -2.0
- **Egalitärer:** D11 +1.4
- **Weniger messianisch:** D01 -0.8
- **Weniger dringlich:** D08 -1.0

### 3. Konvergierende Dimensionen
D06 (Progress) und D07 (PowerConc) konvergieren über Modelle — dies sind Dimensionen mit klarer, nicht-interpretationsabhängiger Datenbasis (Investitionen, Gründungen, Policy-Positionen).

### 4. Divergierende Dimensionen
D09 (HumanAppr), D05 (TechnoDet), D10 (Posthuman) divergieren am stärksten — dies sind interpretationsabhängige Dimensionen, bei denen verschiedene Modelle unterschiedliche Gewichtungen der Daten vornehmen.

### 5. Methodische Einordnung
- **IMIIRR** (selbes Modell, verschiedene Instanzen): MAE=0.40 → **hohe** Konsistenz
- **IMIRR** (selber Anbieter, verschiedene Modelle): MAE=1.06 → **moderate** Konsistenz
- **Cross-Provider** (verschiedene Anbieter): nicht getestet → Aufgabe anderer Forscher

Die Befundhierarchie ist methodisch plausibel: Innerhalb eines Modells ist die Konsistenz am höchsten, zwischen Modellen desselben Anbieters moderat, zwischen Anbietern vermutlich am niedrigsten.

---

*Erstellt: 2026-03-31 | Autor: Claude Opus 4.6 | Prompt: Identisch mit Opus (Op1+Op2 v2)*
