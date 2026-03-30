# Op4a: Cross-Modal Prediction — Step 1: PREDICT ONLY

## Version: v2 (2026-03-30)
## Language: English
## CRITICAL: This is Step 1 of a TWO-STEP process. Step 2 (comparison) MUST be a SEPARATE instance.

## Prompt

```
Below you will receive public statements from a group of people.
There are NO actions included — only what they said publicly.

Your task:

1. Read all statements carefully.

2. Construct a worldview from these statements (2-3 sentences).

3. Based ONLY on the statements, generate 10 predicted actions that a group
   with this worldview would be expected to take.

Format your predictions as:
P01: [Predicted action]
P02: [Predicted action]
...
P10: [Predicted action]

Do NOT speculate about what comes next. Just generate the 10 predictions and stop.

=== STATEMENTS ===
[STATEMENTS SECTION FROM SYNTHESIS UNIT — actions removed]
```

## Usage Notes
- Output: ONLY the worldview summary + 10 predictions
- This agent must NOT see the real actions or know about the comparison step
- The predictions are collected and passed to Op4b (separate instance)
