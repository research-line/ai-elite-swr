# G5: Cross-Modal Prediction (Op4)

> Date: 2026-03-30
> Method: Statements → Worldview → predicted actions → comparison with actual actions
> Instrument: Claude Opus 4.6 (5 independent agents)

---

## Research Question

Can the worldview reconstructed from public statements predict the actual actions of a group? This is the strongest integral validation test of the SWR method (Operationalization 4).

## Method

For each group:
1. Agent reads ONLY the statements (ACTIONS are ignored)
2. Agent constructs a worldview from the statements
3. Agent generates 10 predicted actions
4. Agent reads the actual actions
5. Agent compares: CONFIRMED / PLAUSIBLE / REFUTED
6. Agent names the 3 biggest surprises (unpredictable actions)

## Results

| Group | n (Statements/Actions) | Confirmed | Plausible | Refuted |
|--------|-------------------------|-----------|-----------|-----------|
| CEOs | ~300/285 | 10/10 | 0/10 | 0/10 |
| Academics | ~246/183 | 10/10 | 0/10 | 0/10 |
| Risk-Warner | ~139/92 | 9/10 | 1/10 | 0/10 |
| Investors | ~135/108 | 9/10 | 1/10 | 0/10 |
| Accelerators | ~140/100 | 6/10 | 4/10 | 0/10 |
| **TOTAL** | | **44/50 (88%)** | **6/50 (12%)** | **0/50 (0%)** |

### Assessment
- **88% of predicted actions** were directly confirmed by actual actions
- **0% refuted** — not a single prediction was falsified by the opposite in the actions
- **12% plausible** — consistent, but without direct match (mostly missing action coding)

### Group Comparison
- **CEOs and Academics (100%):** Highest predictive power. For CEOs, actions follow rhetoric almost textbook-like. For Academics, the worldview is highly consistent.
- **Risk-Warner and Investors (95%):** Very high predictive power. Only gap: Mars/space exploration (not in action coding) and robotics (no documented investments yet).
- **Accelerators (80%):** Lowest, but still high predictive power. 4 plausible instead of confirmed items, mainly because media appearances and lobbying were not coded as separate actions.

## The Most Important Surprises (unpredictable)

### Systematic Patterns in Surprises

1. **Opportunistic political reversals** (CEOs, Investors): From anti-Trump to pro-Trump, from Biden donations to Trump inauguration donations. Statements show values, actions show pragmatism.

2. **Commercial exploitation with altruistic rhetoric** (Academics): Billion-dollar IPOs (Coursera $4.3B, World Labs $1B) while focusing on open science and education for all.

3. **Contradictory crisis behavior** (Risk-Warner): Board crises, supercomputer construction while simultaneously warning against overly rapid development, billion-dollar fundraising while warning of extinction risks.

4. **Strategic mistakes** (Accelerators): WeWork disaster ($14B write-down), NVIDIA stake sale ("biggest mistake"). Not derivable from optimistic statements.

5. **Ethics withdrawals** (CEOs): Google removes AI ethics principles for weapons/surveillance (2025), despite statements emphasizing "responsible AI" until the end.

## Methodological Implication

Cross-Modal Prediction validates the SWR on a fundamental level: **The worldview reconstructed from statements has genuine predictive power for actions.** The 88% confirmation rate at 0% refutation is a strong result.

At the same time, the **surprises** show exactly the added value of the Say-Do analysis (RQ3): The actions that were NOT predictable are systematically those where the say-do gap is largest — political opportunism, commercial exploitation, ethics withdrawals. These "gaps" in predictive power ARE the substantive finding.

---
*Analysis: Claude Opus 4.6 | 5 independent agents on 5 group data files*
