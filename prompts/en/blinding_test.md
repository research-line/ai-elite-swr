# Blinding Approach Test

## Version: v1 (2026-03-30)
## Purpose: Compare two anonymization approaches on the same topf data

## Approach A: Current (Placeholder Blinding)
Names replaced with [PERSON], companies with [COMPANY], etc.
Problem: Placeholders signal "something was hidden" → may trigger identification behavior.

## Approach B: Invisible Blinding (Fictional Names)
Names replaced with plausible fictional names (e.g., "Marcus Chen", "Elena Bergstroem").
Advantage: No visible signal that anonymization occurred.
Disadvantage: Model might still recognize content patterns.

## Approach C: No Names at All
Statements presented without any attribution, just numbered [S001], [S002]...
Advantage: Cleanest separation from identity.
Disadvantage: Loses context of who said what (relevant for group attribution).

## Test Protocol
1. Select ONE topf (e.g., GH_risk_AH — moderate size, distinctive worldview)
2. Run Op1 + Op2 with Approach A (current placeholders)
3. Run Op1 + Op2 with Approach B (fictional names) — SEPARATE instance
4. Compare D01-D12 ratings: If identical → blinding approach doesn't matter
5. If different → investigate which dimensions diverge and why

## Expected Outcome
For GROUP-level synthesis, the blinding approach should matter less than for
individual-level, because the collective worldview is not a retrievable object
in training data regardless of naming.
