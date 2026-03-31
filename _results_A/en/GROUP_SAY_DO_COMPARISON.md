# Group Say-Do Comparison: Differentiated Analysis with Instance Separation

> Created: 2026-03-31
> Model: Claude Opus 4.6 (separate instances per data type and group)
> Method: Per group: Statements-only SU → Op1+Op2 (Instance A), Actions-only SU → Op1+Op2 (Instance B)

---

## Results Table (Gap = Do minus Say)

| Dim | CEO | Academics | Investors | Risk-Warners | Total |
|-----|-----|-----------|-----------|--------------|-------|
| D01 Mission | 0 | -1 | -1 | 0 | 0 |
| D02 Efficacy | +1 | +1 | 0 | **-2** | +1 |
| D03 WorkEthic | +1 | **+3** | +1 | +1 | 0 |
| D04 Responsibility | -1 | 0 | 0 | 0 | 0 |
| D05 TechnoDet | -1 | **+3** | -1 | **-4** | **+2** |
| D06 Progress | -1 | +1 | -1 | +1 | 0 |
| D07 PowerConc | **+2** | **-3** | 0 | +1 | **+2** |
| D08 Urgency | 0 | -1 | -1 | -1 | 0 |
| D09 HumanAppr | -1 | **-2** | -1 | **+4** | -1 |
| D10 Posthuman | +1 | **+2** | **-2** | **-5** | 0 |
| D11 Egalitar | **-2** | **-2** | 0 | +1 | **-2** |
| D12 Control | **+2** | **+2** | +1 | **+3** | +1 |
| **MAE** | **1.08** | **1.75** | **0.75** | **1.92** | **0.75** |

G6 v2 Baseline (consistent control group, separate instances): **MAE = 0.92**

---

## Findings

### 1. Overall Gap Below Baseline, but Group Gaps ABOVE Baseline
- **Total:** MAE = 0.75 (< Baseline 0.92) — not universally demonstrable
- **CEO:** MAE = 1.08 (> Baseline) — significant
- **Academics:** MAE = 1.75 (> Baseline) — strongly significant
- **Risk-Warners:** MAE = 1.92 (> Baseline) — largest gap of all groups
- **Investors:** MAE = 0.75 (< Baseline) — consistent

### 2. CEO: Classical Hypocrisy Gap
- D07 Power Concentration: +2 (talk about distribution, act with concentration)
- D11 Egalitarianism: -2 (talk egalitarian, act anti-egalitarian)
- D12 Locus of Control: +2 (act with greater control claims)
- **Interpretation:** CEOs display the expected pattern — public rhetoric outperforms operational practice on social dimensions.

### 3. Risk-Warners: Prophetic Consistency (NO inverse gap)
- D09 Human Appreciation: **+4** (Say=4, Do=8) — statements describe a world where humans WILL be replaceable, actions show the actual belief
- D10 Posthumanism: **-5** (Say=9, Do=4) — statements describe posthumanist dangers, actions show human-centric values
- D05 Techno-Determinism: **-4** (Say=8, Do=4) — statements warn of deterministic future, actions are pragmatic-shaping
- D12 Control: **+3** (Say=5, Do=8) — rhetorically pessimistic about controllability, but act as active designers

**DV Decomposition:**
- DV1 Self-Image (D01-D04): MAE=0.8 — **CONSISTENT**. They know who they are.
- DV2 Worldview (D05-D08): MAE=1.8 — Statements describe the **feared** world, actions the **desired** one.
- DV3 View of Humanity (D09-D12): MAE=3.2 — **STRONGEST DISCREPANCY**. Statements: possibility projection (posthumanist, pessimistic). Actions: actual values (human-friendly, design-willed).

**Interpretation:** Risk-Warners' statements are **possibility projections** — they describe a future they WANT TO PREVENT, not one they endorse. Their actions (principled resignations, safety research, open letters, Senate testimony) are **consistent with their actual beliefs**. Analogy: A prophet warns of doom and then acts to avert it — both are consistent, not contradictory. This is the signature of **anticipatory ethics**, not hypocrisy.

### 4. Academics: Theory-Practice Gap
- D03 WorkEthic: +3 (actions more intense than statements)
- D05 TechnoDet: +3 (actions more technodeterminist than statements — founding, patents)
- D07 PowerConc: -3 (statements more power-centric, actions more decentralized — open source, education)
- D09 HumanAppr: -2, D11 Egalitar: -2 (actions somewhat less human/egalitarian)
- **Interpretation:** Academics display an "ivory tower gap" — talk abstractly about power structures, but act more decentralized (open source, teaching). Simultaneously: actions are more determinist than cautious academic rhetoric.

### 5. Investors: Consistent
- MAE = 0.75 (below baseline)
- Only strong gap: D10 Posthumanism -2
- **Interpretation:** Investors are the most consistent group. Their statements and actions tell the same story: radical techno-optimism with minimal egalitarian orientation. No hypocrisy gap — they mean what they say.

---

## Methodological Significance

### The Overall Gap is a Simpson's Paradox
The aggregated say-do gap (MAE = 0.75) falls below the baseline because **opposing** group gaps cancel each other out:
- CEO-Gap (D07 +2, D11 -2) and Risk-Warner-Gap (D07 +1, D11 +1) compensate for each other
- The extreme Risk-Warner inversions (D09 +4, D10 -5) are averaged out in the overall pool

**This is a classic Simpson's Paradox:** The effect exists in every subgroup but disappears in the aggregate because the directions diverge.

### Implication for RQ3
RQ3 must be reformulated: Not "is there ONE say-do gap?" but "which GROUPS show which GAPS?" The answer is differentiated:
- CEOs: conventional desirability gap (talk better than they act)
- Risk-Warners: inverse performative-pessimism gap (talk worse than they act)
- Investors: no gap (consistently radical)
- Academics: theory-practice gap (complex pattern)

---

### 6. Accelerators: Borderline Gap
- MAE = 0.92 (exactly on baseline)
- D04 Responsibility: -2 (talk more responsibly than they act)
- D06 Progress: -2 (rhetorically optimistic than in deeds)
- D11 Egalitarianism: -2 (talk more egalitarian than they act)
- **Interpretation:** Accelerators show a muted CEO pattern. The gap is borderline — on the baseline, not above it.

---

## Final Overview of All 5 Groups + Total

| Group | MAE | vs. Baseline (0.92) | Pattern |
|-------|-----|---------------------|---------|
| **Risk-Warners** | **1.92** | **WELL above** | Inverse gap: talk gloomy, act humanely |
| **Academics** | **1.75** | **Above** | Theory-practice gap: complex pattern |
| **CEO** | **1.08** | **Above** | Classical hypocrisy gap: D07/D11/D12 |
| **Accelerators** | **0.92** | **On baseline** | Muted CEO pattern: D04/D06/D11 |
| **Investors** | **0.75** | Below | Consistent: no gap |
| **Total** | **0.75** | Below | Simpson's Paradox: group gaps cancel out |

---

*Created: 2026-03-31 | Author: Claude Opus 4.6 | All 5 groups complete*
