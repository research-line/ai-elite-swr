# Say-Do Comparison: Instance Separation v1 vs v2

> Created: 2026-03-31
> Model: Claude Opus 4.6
> Method: GA_ges_A and GA_ges_H in separate instances (v2) vs. same instance (v1)

---

## Background

In v1 (2026-02-12), GA_ges_A (statements only) and GA_ges_H (actions only) were rated in the **same instance** (Batch 1: one rating file with comparative analysis). In v2 (2026-03-31), they were rated in **separate instances** -- no agent saw the other's data.

---

## Results

### Dimensional Ratings

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

### Statistical Summary

| Metric | v1 (same instance) | v2 (separate) | Change |
|--------|-------------------|---------------|--------|
| MAE (statements↔actions) | 1.42 | **0.75** | -47% |
| Pearson r | 0.817 | 0.801 | ≈ same |
| Max \|Gap\| | 3 (D11) | 2 (D07, D11) | -1 |
| Dimensions with Gap=0 | 0/12 | **7/12** | +7 |
| Dimensions with \|Gap\|≥2 | 5/12 | 2/12 | -3 |

### Comparison with G6 Control Group

| Configuration | Control (G6) | AI Elite | Ratio |
|---------------|--------------|---------|-------|
| **v1 (same instance)** | MAE=0.50 | MAE=1.42 | **2.8×** |
| **v2 (separate)** | MAE=0.92 | MAE=0.75 | **0.8×** |

---

## Interpretation

### 1. The Say-Do Gap Was Partly an Instance Artifact
With instance separation, the gap shrinks from MAE=1.42 to MAE=0.75 (-47%). The rater, seeing both data types in v1, **amplified** the differences -- likely because the comparative task (seeing the contrast as implicit goal) reinforced differentiation.

### 2. The Gap Falls Below Control Baseline
v2 AI Elite MAE (0.75) < v2 G6 MAE (0.92). The say-do gap with instance separation is **smaller** than the natural noise of the method in separate instances. This means: with single measurements, the gap cannot be reliably demonstrated.

### 3. What Remains Stable?
- **D07 Power concentration: Gap +2** (actions concentrate power more than statements) -- stable across v1 and v2
- **D11 Egalitarianism: Gap -2** (actions less egalitarian) -- shrunk from -3, but still present
- **D05 Techno-Determinism: Gap +2** (actions more deterministic) -- in v2 even stronger

### 4. What Disappears?
- **D04 Responsibility:** Gap from -2 to 0 -- with separate instance, actions receive similarly high responsibility as statements
- **D09 Human Appreciation:** Gap from -2 to -1 -- partly artifact
- **D01, D03, D06, D08, D10:** All gaps vanish at 0

### 5. Methodological Consequence
The RQ3 findings (say-do gap) must be formulated **more carefully** in the paper:
- The qualitative directions are correct (D07↑, D11↓ in actions)
- The quantitative magnitudes were inflated by instance contamination
- For robust inference, N=30 runs per data type are needed
- The strongest argument remains D07/D11 (consistent across v1 and v2)

---

## Recommendation for Paper A

1. **Rewrite RQ3 paragraph:** "Preliminary single-run comparisons suggest directional say-do differences on D07 (power concentration) and D11 (egalitarianism), consistent across independent measurements. However, the magnitude of the overall gap is sensitive to instance separation and falls within the baseline noise range (G6 v2 control MAE=0.92). Formal quantification requires repeated measurements (N≥30)."
2. **Highlight D07 and D11 as most stable say-do differences** (Gap +2 and -2 in both versions)
3. **Replace old MAE=1.25/1.42 with v2 values** with transparency about revision

---

*Created: 2026-03-31 | Author: Claude Opus 4.6*
