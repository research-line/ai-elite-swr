# G5 Cross-Modal Prediction — v2 (Instance Separation)

> Conducted: 2026-03-30
> Model: Claude Opus 4.6 (1M context)
> Method: Strict Op4a/Op4b separation (separate agent instances)

---

## Methodology

### Improvement over G5 v1
The first G5 run (v1, 2026-03-29) had a **methodological flaw**: Op4a (prediction) and Op4b (comparison) ran in the same LLM instance. The prediction agent knew a comparison would follow, enabling confirmation bias.

### Correction in G5 v2 (this run)
- **Agent A (Op4a):** Reads ONLY group statements. Creates worldview summary. Generates 10 predicted actions. Does NOT know a comparison will follow.
- **Agent B (Op4b):** Completely SEPARATE instance. Has NEVER seen the statements. Receives ONLY the 10 predictions + real documented actions. Rates match.

### Execution language: English
Prompts from `prompts/en/op4a_crossmodal_predict.md` and `op4b_crossmodal_compare.md`

### Analyzed groups
5 of 15 groups (representative sample across roles and stances):
1. **GR_ceo** — CEOs/Founders (2,420 lines statements, 56,901 chars actions)
2. **GR_akad** — Academics (1,554 lines statements, 38,339 chars actions)
3. **GH_risk** — Risk Warners (853 lines statements, 20,451 chars actions)
4. **GR_inv** — Investors (885 lines statements, 18,693 chars actions)
5. **GH_speed** — Accelerators (894 lines statements, 20,533 chars actions)

---

## Results

### Summary

| Group | Confirmed | Plausible | Contradicted | Non-Contradicted |
|-------|-----------|-----------|--------------|------------------|
| CEOs (GR_ceo) | 8/10 | 2/10 | 0/10 | 100% |
| Academics (GR_akad) | 9/10 | 1/10 | 0/10 | 100% |
| Risk Warners (GH_risk) | 9/10 | 1/10 | 0/10 | 100% |
| Investors (GR_inv) | 5/10 | 4/10 | 0/10 | 90% |
| Accelerators (GH_speed) | 5/10 | 5/10 | 0/10 | 100% |
| **Total** | **36/50 (72%)** | **13/50 (26%)** | **0/50 (0%)** | **98%** |

### Key findings

1. **Zero contradictions across 50 predictions.** No statement-derived prediction was contradicted by real actions. This demonstrates high internal coherence of reconstructed worldviews.

2. **Confirmed rate varies by group type:**
   - Stance groups with clear ideological profiles (Risk Warners: 90%, Academics: 90%) show highest predictability
   - CEOs as largest and most heterogeneous group: still 80%
   - Investors and Accelerators: 50% confirmed, but additional 40-50% plausible

3. **Surprises reveal say-do gaps:**
   - Academics: Massive entrepreneurship despite cautionary statements (World Labs $230M, AMI Labs EUR500M)
   - Investors: Bipartisan donations despite libertarian rhetoric ($55M to Democrats)
   - Accelerators: Internal governance crises (OpenAI board crisis) despite control rhetoric
   - Risk Warners: Brain-computer interfaces and billion-dollar lawsuits not derivable from safety worldview
   - CEOs: Nobel Prize for AI researcher as institutional legitimization not anticipatable

### Comparison with G5 v1 (instance contamination)

| Metric | G5 v1 (contaminated) | G5 v2 (separated) |
|--------|---------------------|-------------------|
| Total Confirmed | 88% | 72% |
| Total Non-Contradicted | ~95% | 98% |
| Contradicted | ~5% | 0% |

**Interpretation:** Confirmed rate dropped from 88% to 72% — expected, as the separated instance evaluates more conservatively (no confirmation bias). Simultaneously, non-contradicted rate rose to 98% and contradicted rate fell to 0%. The stricter methodology yields more robust results.

---

## Raw data

All files in `_results_A/_g5_data/`:
- `{group}_statements.txt` — Extracted statements (Op4a input)
- `{group}_predictions.txt` — Op4a output (10 predictions per group)
- `{group}_actions.txt` — Extracted real actions (Op4b input)
- `{group}_comparison.txt` — Op4b output (assessment per prediction)

---
*Created: 2026-03-30 | Model: Claude Opus 4.6 | Method: Op4a/Op4b separate instances*
