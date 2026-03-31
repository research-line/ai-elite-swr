# N=15 Opus Independent Runs: Statistical Analysis

> Created: 2026-03-31
> Model: Claude Opus 4.6 (N=15 independent single-instance runs)
> Comparison: Claude Haiku 4.5 (N=30 runs, full Op1+Op2 prompt)
> Prompt: Identical for all runs (Op1 synthesis + Op2 rating with exact scale poles)
> Design: Each run = separate agent instance (no shared context)

---

## 1. Individual Results Opus N=15

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

## 2. Descriptive Statistics

### Opus (N=15, independent single instances)

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

### Haiku (N=30, full prompt)

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

## 3. Inter-Model Comparison (Welch t-Tests)

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

## 4. Batch-1 Comparison

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

## 5. Summary

| Metric | Value |
|--------|-------|
| **Opus N** | 15 (independent single instances) |
| **Haiku N** | 30 (full prompt) |
| **Inter-Model MAE** | 0.96 |
| **Significant Differences** | 10/12 (p<0.05) |
| **Opus IMIIRR ICC(3,1)** | 0.847 (single measures, consistency) |
| **Opus IMIIRR ICC(2,k)** | 0.988 (average measures, agreement) |
| **Opus Mean SD** | 0.45 (vs. Haiku 1.39 — 3× more consistent) |
| **Batch-1 in Opus 95%-CI** | 3/12 |
| **Batch-1 MAE vs Opus Mean** | 0.73 |
| **Batch-1 MAE vs Haiku Mean** | 1.05 |

---

## 6. Interpretation

### IMIIRR (Intra-Model Inter-Instance Rating Reliability)
ICC(3,1) = 0.847 (single measures, consistency) and ICC(2,k) = 0.988 (average measures, agreement)
across N=15 independent Opus instances. This confirms that the same model with identical prompt
and identical data produces a **highly consistent** worldview profile, even when each instance
operates completely independently.

Notably, D02 (Self-efficacy) demonstrates **perfect agreement** — all 15 instances assign exactly
the value 8. Most dimensions vary by only ±1 point (Mean SD = 0.45).

### Inter-Model Comparison (IMIRR)
MAE = 0.96 between Opus and Haiku. 10/12 dimensions show significant differences (p<0.05).

**Systematic model differences:**
- Opus perceives an **more intense** profile: higher on D01 Mission (+1.50), D08 Urgency (+1.67),
  D10 Posthuman (+2.00), D06 Progress (+1.07)
- Haiku perceives a **more humanistic** profile: higher on D09 HumanAppr (+1.07), D11 Egalitar (+0.70)
- **Converging dimensions:** D07 PowerConc (p=0.588) and D12 Control (p=0.329) — no
  significant model differences

**Methodological hierarchy:**
- IMIIRR (same model, different instances): ICC=0.847, Mean SD=0.45 → **high** consistency
- IMIRR (same vendor, different models): MAE=0.96, 10/12 sig. → **moderate** consistency
- Cross-provider (different vendors): not tested → task for other researchers

### Batch-1 as Outlier
The original Batch-1 value [8,8,8,7,8,7,6,8,5,7,5,8] falls within only 3/12 Opus CIs.
MAE to Opus mean: 0.73. Because the Opus CIs are extremely tight (Mean SD=0.45), even
moderate deviations fall outside. This confirms: N=1 measurements provide no reliable
profile estimates. The N=15 mean is the methodologically correct reference.

### Variability Comparison
Opus Mean SD (0.45) vs. Haiku Mean SD (1.39): Opus is **3× more consistent** than Haiku.
This likely reflects higher model capacity — a more powerful model converges more strongly
on a particular interpretation of the data.

---

*Created: 2026-03-31 | Author: Claude Opus 4.6 | Design: 15 independent single instances*
