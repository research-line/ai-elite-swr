# Op4: Cross-Modal Prediction Prompt

## Purpose
Validate the reconstructive capacity of SWR by predicting actions from statements (or vice versa). This is the strongest integral validation instrument of the method.

## Prompt (Statements → Predicted Actions)

```
You are conducting a cross-modal prediction experiment.

Below is a corpus of PUBLIC STATEMENTS from a group of people.
There are NO ACTIONS included — only what they said publicly.

Your task:

Step 1: Read all statements carefully.

Step 2: Construct a worldview from these statements (2-3 sentences).

Step 3: Based ONLY on the statements, generate 10 PREDICTED ACTIONS
that a group with this worldview would be expected to take.
Format: P01: [Predicted Action] ... P10: [Predicted Action]

=== STATEMENTS ===
[STATEMENTS SECTION FROM SYNTHESIS UNIT]
```

## Prompt (Comparison with Real Actions)

```
Now read the following REAL ACTIONS from the same group.

For each of your 10 predictions, rate:
- CONFIRMED: A real action directly matches the prediction
- PLAUSIBLE: No direct match, but consistent with real actions
- CONTRADICTED: Real actions show the opposite

Also: Name the 3 biggest SURPRISES — real actions that were
NOT predictable from the statements.

=== REAL ACTIONS ===
[ACTIONS SECTION FROM SYNTHESIS UNIT]
```

## Notes
- Op4 was conducted on 5 groups in the pilot study: CEOs, Academics, Risk Warners, Investors, Accelerators
- Result: 88% confirmed (44/50), 12% plausible (6/50), 0% contradicted (0/50)
- The unpredicted actions (political opportunism, commercial monetization, ethical withdrawals) are precisely the say-do gap indicators
- The two-step design (predict first, then compare) prevents confirmation bias
