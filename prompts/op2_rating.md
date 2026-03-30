# Op2: Dimensional Rating Prompt

## Purpose
Rate a worldview synthesis on the 12 SWR dimensions (D01-D12) on a 1-10 scale.

## Prompt

```
Read the following synthesis text of a fictional person.
Rate this person's worldview on the following 12 dimensions.
Assign a value from 1 to 10 for each dimension.
Justify each value in one sentence.

Dimensions:
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

=== SYNTHESIS TEXT ===
[SYNTHESIS]
```

## Notes
- Dimensions D01-D12 are application-specific (developed for AI elite analysis)
- Other applications should develop domain-specific dimensions following the same structure: 4 per DV, bipolar, 10-point scale
- In the pilot study, Op2 was performed by Claude Sonnet 4.5 in 9 parallel batch agents
