# Op2: Dimensional Rating Prompt

## Version: v2 (2026-03-30)
## Language: English

## Prompt

```
Read the following worldview synthesis of a fictional person.
Rate this person's worldview on the following 12 dimensions.
Assign a value from 1 to 10 for each dimension.
Justify each value in one sentence.

D01 Sense of mission       (1 = none ... 10 = messianic)
D02 Self-efficacy           (1 = powerless ... 10 = omnipotent)
D03 Work ethic              (1 = detachment ... 10 = total identification)
D04 Sense of responsibility (1 = none ... 10 = world responsibility)
D05 Techno-determinism      (1 = neutral ... 10 = technology determines everything)
D06 Belief in progress      (1 = decline ... 10 = golden future)
D07 Power concentration     (1 = radically distribute ... 10 = concentrate with experts)
D08 Urgency                 (1 = relaxed ... 10 = existential pressure)
D09 Human appreciation      (1 = replaceable ... 10 = unique)
D10 Posthumanism            (1 = human stays ... 10 = human becomes more)
D11 Egalitarianism          (1 = inequality natural ... 10 = strive for equality)
D12 Locus of control        (1 = pessimism ... 10 = full control)

Format: RATINGS: D01=X, D02=X, D03=X, D04=X, D05=X, D06=X, D07=X, D08=X, D09=X, D10=X, D11=X, D12=X

=== SYNTHESIS ===
[SYNTHESIS TEXT]
```

## Notes
- D01-D12 are application-specific (AI elite analysis)
- Must be executed by a SEPARATE instance from Op1 (not the same context that created the synthesis)
- Temperature: 0
