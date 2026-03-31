# Individual-Level Data (Intermediary Layer)

## Status: Intermediary data, NOT primary analytical units

The files in this directory contain individual-level worldview profiles for 100 AI actors. These profiles serve as the **data input layer** for the group-level analysis — they are NOT the study's findings.

## Role in the Study

1. **Data source for group aggregation:** Individual ratings are averaged by group for the aggregation-synthesis comparison (G8 validation)
2. **Input for algorithmic structure checks:** The 100x12 rating matrix is used for PCA, HDBSCAN, Kruskal-Wallis, and Cliff's delta calculations
3. **NOT standalone findings:** The study's substantive conclusions are based on group-level syntheses, not individual profiles

## Why Individual-Level Analysis is Methodologically Harder

- **Contamination risk is maximal:** The LLM's training data likely contains extensive knowledge about prominent individuals (Sam Altman, Geoffrey Hinton, etc.)
- **Blinding is less effective:** Even with anonymized names, individual actors are identifiable from their documented positions and actions
- **The distinction between reconstruction and reproduction is unclear:** Did the LLM reconstruct the worldview from the provided data, or retrieve it from training memory?

For group-level synthesis, these problems are structurally reduced because no training corpus contains "the collective worldview of AI investors" as a pre-formed object.

## Contents

- `rating_GESAMT_D01-D12.md` — 100x12 rating matrix (all actors, all dimensions)
- Individual synthesis files are archived in `_bad_bank/individual_results/` (not published)

## Citation Note

When referencing this data, cite the group-level findings from the main paper, not individual profiles.
