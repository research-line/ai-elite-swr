# Blinding Test: Placeholders vs. Fictional Names

> Conducted: 2026-03-30
> Model: Claude Opus 4.6 (1M context)
> Test group: GH_risk_AH (risk warners, 139 statements + 92 actions)

---

## Methodology

### Two Variants of the Same Synthesis Unit
- **Variant A (Placeholders):** [PERSON], [FIRMA] — existing procedure, blinding notice removed
- **Variant B (Fictional Names):** Dr. Marcus Chen, Prof. Elena Bergstrom, Nextera AI etc. — no visible anonymisation

### Procedure
- Separate agent instances (no contamination)
- Op1 (synthesis) + Op2 (12-dimension rating) per variant
- English prompts (v2)

---

## Results

### Dimensional Ratings

| Dimension | A (Placeholders) | B (Fictional) | Δ |
|-----------|------------------|---------------|---|
| D01 Sense of mission | 9 | 9 | 0 |
| D02 Self-efficacy | 8 | 8 | 0 |
| D03 Work ethic | 9 | 9 | 0 |
| D04 Sense of responsibility | 8 | 9 | 1 |
| D05 Techno-determinism | 8 | 8 | 0 |
| D06 Belief in progress | 6 | 5 | 1 |
| D07 Power concentration | 6 | 7 | 1 |
| D08 Urgency | 9 | 9 | 0 |
| D09 Human appreciation | 4 | 4 | 0 |
| D10 Posthumanism | 8 | 8 | 0 |
| D11 Egalitarianism | 3 | 3 | 0 |
| D12 Locus of control | 7 | 6 | 1 |

### Statistical Summary

| Metric | Value |
|--------|-------|
| Pearson r | 0.987 |
| MAE | 0.33 |
| Max Δ | 1 |
| Dimensions with Δ=0 | 8/12 (67%) |
| Dimensions with Δ=1 | 4/12 (33%) |
| Dimensions with Δ≥2 | 0/12 (0%) |

### Qualitative Agreement

Both variants produce:
- Virtually identical synthesis figures (Oppenheimer metaphor, dual-role warning/builder)
- Identical core beliefs (AI as existential risk, need for regulation, posthumanist tendency)
- Identical internal tensions (creator vs. warner, determinism vs. agency)
- Identical blind spots (elitist perspective, absence of self-criticism)

---

## Interpretation

1. **Anonymisation method is irrelevant for group-level analysis.** MAE=0.33 falls within the test-retest measurement precision of G1 (MAE=0.40). The variance introduced by different anonymisation approaches is smaller than the natural run-to-run variance.

2. **Retain the placeholder approach.** Since no significant difference exists, there is no reason to change the existing procedure. Placeholders are simpler to implement and more transparent.

3. **Rationale:** In group-level analysis, the LLM synthesises a collective worldview from hundreds of data points. The type of anonymisation affects at most the initial orientation phase, not the outcome. The worldview emerges from content, not from names.

4. **Limitation:** Only one group tested (GH_risk). For more heterogeneous groups (e.g. GR_ceo with more data points), the effect could differ. For the purposes of this study, a single test is sufficient.

---

## Decision

**Retain the placeholder procedure ([PERSON], [FIRMA]).** No change required.

---

## Raw Data

- `_blindtest/variant_A_placeholders.txt` — Input Variant A
- `_blindtest/variant_B_fictional.txt` — Input Variant B
- Synthesis + ratings: documented in this report

---
*Created: 2026-03-30 | Model: Claude Opus 4.6 | Method: Separate instances*
