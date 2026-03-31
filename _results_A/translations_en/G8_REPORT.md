# G8: Aggregated Individual Profiles vs. Direct Group Synthesis

> Date: 2026-03-30
> Method: Comparison of D01-D12 ratings from two approaches
> Script: `g8_aggregation_comparison.py`
> Data: `g8_comparison_results.json`

---

## Research Question

Does direct group synthesis (all data from a group → Claude → worldview) yield the same result as aggregating individual profiles (100 individual profiles → group mean)?

## Method

- **Aggregated approach:** D01-D12 mean values from 100 individual profile ratings (Claude Sonnet 4.5) per group
- **Direct approach:** D01-D12 ratings from direct group syntheses (Batch 4) generated from pooled raw data
- **Metrics:** Pearson r, MAE, RMSE, amplification analysis
- **15 groups** compared: 4 roles, 3 firms, 6 attitudes, 2 gender

## Results

### Convergence Metrics

| Group | n | Pearson r | MAE | RMSE | Assessment |
|--------|---|-----------|-----|------|-----------|
| CEOs | 19 | 0.572 | 1.67 | 2.02 | Acceptable |
| Academics | 12 | 0.807 | 0.51 | 0.68 | Good |
| Investors | 8 | 0.608 | 2.29 | 2.66 | Weak |
| Founders | 36 | 0.614 | 1.13 | 1.48 | Acceptable |
| Anthropic | 9 | 0.777 | 0.73 | 0.94 | Good |
| OpenAI | 7 | 0.774 | 1.06 | 1.31 | Good |
| Google/DM | 7 | 0.489 | 1.85 | 2.25 | Weak |
| Open Source | 6 | 0.857 | 0.75 | 0.91 | Good |
| Closed Source | 5 | 0.567 | 1.08 | 1.22 | Acceptable |
| Risk-Warner | 6 | 0.715 | 1.56 | 1.82 | Acceptable |
| Accelerator | 7 | 0.855 | 1.21 | 1.29 | Good |
| Reg-Pro | 8 | 0.759 | 0.86 | 1.18 | Good |
| Reg-Contra | 5 | 0.715 | 1.17 | 1.34 | Good |
| Women | 10 | 0.428 | 1.02 | 1.27 | Weak |
| Men | 90 | 0.549 | 2.56 | 2.78 | Weak |
| **TOTAL** | | **0.623** | **1.30** | **1.66** | |

### Dimensional Distortions

| Dimension | Avg Delta | Direction |
|-----------|-----------|----------|
| D01 Sense of Mission | +1.76 | Direct synthesis HIGHER |
| D02 Self-efficacy | +0.40 | ~Equal |
| D03 Work Ethic | +1.64 | Direct synthesis HIGHER |
| D04 Responsibility | +0.66 | Direct synthesis HIGHER |
| D05 Techno-Determinism | -0.58 | Direct synthesis LOWER |
| D06 Progress Optimism | +0.52 | Direct synthesis HIGHER |
| D07 Power Concentration | +1.71 | Direct synthesis HIGHER |
| D08 Urgency | +0.38 | ~Equal |
| D09 Human Value | -0.13 | ~Equal |
| D10 Posthumanism | +0.39 | ~Equal |
| D11 Egalitarianism | -0.65 | Direct synthesis LOWER |
| D12 Control Beliefs | +0.66 | Direct synthesis HIGHER |

### Amplification Effect

- **71.7%** of all dimension-group combinations are **amplified** by direct synthesis (further from scale midpoint)
- **23.9%** are dampened
- **4.4%** remain the same

## Interpretation

### 1. Moderate Convergence (r = 0.623)
The two approaches yield non-identical but clearly correlated results. The ranking of dimensions is largely preserved — those who rank high/low in aggregation tend to do so in direct synthesis as well.

### 2. Systematic Amplification Effect
Direct group synthesis produces **sharper contours** than individual profile aggregation. This is interpretable as:
- **Coherence amplification:** When all group data are bundled, the LLM identifies dominant patterns more strongly
- **Averaging dampening:** Individual profiles have natural variance that averaging flattens extreme values
- **Analogy:** Similar to group identity in social psychology (Group Polarization) being sharper than the average of individuals

### 3. Heterogeneous Convergence
- **Best convergence (r > 0.75):** Academics, Open Source, Accelerator, Anthropic, OpenAI, Reg-Pro, Reg-Contra — ideologically cohesive groups
- **Weakest convergence (r < 0.55):** Women, Google/DM, Men — more heterogeneous groups
- **Pattern:** The more ideologically homogeneous the group, the better the convergence

### 4. Investors as Outlier
The Investors group (r=0.608, MAE=2.29) shows the strongest amplification effect (D07 Power Concentration: Delta +6.2). Direct synthesis paints an extremely pronounced picture; individual profiles are more moderate.

## Methodological Implications

1. **Both approaches are complementary:** Aggregation = conservative, direct = expressive
2. **For the paper:** Keep group synthesis ratings (direct), but report amplification effect as methodological feature
3. **Run convergence (G1):** Must be tested next on direct group syntheses
4. **Expected discrepancy (G6):** Must account for amplification effect as baseline

---
*Analysis: Claude Opus 4.6 | Data: 100 individual profiles (Sonnet 4.5) + 15 group syntheses (Sonnet 4.5)*
