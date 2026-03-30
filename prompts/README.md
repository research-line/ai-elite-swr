# SWR Prompt Templates

## Structure

```
prompts/
├── en/                     English prompts (execution language)
│   ├── op1_core_synthesis.md
│   ├── op2_rating.md
│   ├── op4a_crossmodal_predict.md   ← Step 1: predict ONLY
│   ├── op4b_crossmodal_compare.md   ← Step 2: compare (SEPARATE instance!)
│   ├── op6_comparison.md
│   ├── distillate.md
│   └── blinding_test.md            ← Test protocol for anonymization approaches
├── de/                     German translations (reference)
│   └── [same files, translated]
└── _archive_v1/            Original v1 prompts (before 2026-03-30 revision)
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02 | Original prompts. Problems: blinding hint ("names removed"), Op4 not separated |
| v2 | 2026-03-30 | Removed blinding hint, Op4 split into Op4a/Op4b (separate instances), English as execution language |

## Execution Language

**Decision (2026-03-30): English.** The source data (public statements of AI actors) is predominantly in English. Using English prompts avoids translation artifacts.

German prompt versions in `de/` are provided as reference translations, not as execution prompts.

## Critical Design Principles

1. **Instance separation:** Op4a (predict) and Op4b (compare) MUST run as separate LLM instances. The prediction agent must NOT know that a comparison will follow.
2. **No blinding hints:** The prompt does NOT mention anonymization, removed names, or identity hiding. The model should focus on the synthesis task, not on identification.
3. **Group-level framing:** Prompts say "various public figures" (group data), not "a person" (individual data).
4. **Temperature 0:** All runs at temperature 0 for reproducibility.

## Known Issues (v1, archived)

- v1 Op1 prompt said "All names, company names, and other identifiers have been removed" → alerts the model to the existence of hidden identities
- v1 Op4 was a single prompt combining prediction and comparison → enables confirmation bias
- v1 prompts were in mixed German/English → inconsistent execution language
