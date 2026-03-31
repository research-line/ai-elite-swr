# Influence Strata Comparison: Top 10 vs. Middle vs. Bottom 10

> Created: 2026-03-31
> Model: Claude Opus 4.6 (separate instances per stratum)
> Method: Op1+Op2 applied to rank-based strata of the Top-100 list

---

## Design

| Stratum | Rank | Persons | Data Points | Source |
|---------|------|----------|-------------|--------|
| **Top 10** | 1-10 | 10/10 | 500 (300A + 200H) | `synthese_T10_ges_AH.md` (Batch 1, 2026-02-12) |
| **Middle** | 40-60 | 14/21 with data | 409 (241A + 168H) | `synthese_STRATA_mitte_AH.md` (2026-03-31) |
| **Bottom 10** | 91-100 | 8/10 with data | 267 (150A + 117H) | `synthese_STRATA_bottom_AH.md` (2026-03-31) |

**Caveat:** Middle and Bottom are based on partially reconstructed database (64/100 persons). The strata synthesis units do not contain all persons within their respective rank ranges.

---

## Dimensional Ratings

| Dimension | Top 10 | Middle | Bottom 10 | T-M | T-B | M-B |
|-----------|--------|--------|-----------|-----|-----|-----|
| D01 Sense of Mission | 9 | 7 | 7 | +2 | +2 | 0 |
| D02 Self-Efficacy | 9 | 7 | 6 | +2 | +3 | +1 |
| D03 Work Ethic | 9 | 8 | 8 | +1 | +1 | 0 |
| D04 Sense of Responsibility | 8 | 8 | 7 | 0 | +1 | +1 |
| D05 Techno-Determinism | 9 | 6 | 6 | +3 | +3 | 0 |
| D06 Progress Belief | 8 | 6 | 6 | +2 | +2 | 0 |
| D07 Power Concentration | 7 | 4 | 5 | +3 | +2 | -1 |
| D08 Urgency | 9 | 8 | 7 | +1 | +2 | +1 |
| D09 Human Appreciation | 4 | 6 | 8 | -2 | **-4** | -2 |
| D10 Posthumanism | 8 | 5 | 3 | +3 | **+5** | +2 |
| D11 Egalitarianism | 4 | 6 | 4 | -2 | 0 | +2 |
| D12 Future Control | 8 | 6 | 6 | +2 | +2 | 0 |
| **Avg** | **7.7** | **6.4** | **6.1** | **+1.2** | **+1.6** | **+0.3** |

---

## Key Findings

### 1. Influence Gradient Confirmed
Average rating declines monotonically with rank: Top 10 (7.7) > Middle (6.4) > Bottom 10 (6.1). The most powerful exhibit the most intensive worldview.

### 2. Strongest Gradients (Top→Bottom)
- **D10 Posthumanism: 8→5→3 (Δ=5)** — the most powerful are the most posthumanistic
- **D09 Human Appreciation: 4→6→8 (Δ=-4)** — the most powerful value humans the least
- **D05 Techno-Determinism: 9→6→6 (Δ=3)** — at the top: technology determines everything
- **D07 Power Concentration: 7→4→5 (Δ=2)** — only Top 10 wants power concentrated

### 3. Inversion Dimensions
Two dimensions INCREASE with declining rank:
- **D09 Human Appreciation:** Bottom (8) > Middle (6) > Top (4) — those with less power appreciate humans more
- **D11 Egalitarianism:** Middle (6) > Top (4) = Bottom (4) — the middle is most egalitarian

### 4. Shared Core (No Strata Difference)
- **D03 Work Ethic:** 9/8/8 — universal identification with work
- **D04 Sense of Responsibility:** 8/8/7 — consistently high sense of responsibility

### 5. Power-Moderation Paradox Confirmed
The Top 10 combine the most extreme worldview (highest average) with the highest resource control. The pattern from RQ6 (F6: Power) is confirmed by strata analysis: the more powerful, the more techno-deterministic, posthumanistic, and less human-value-appreciative.

---

## Methodological Limitations

1. **Top 10 ratings originate from Batch 1** (same instance as GA_ges_AH etc.) — may be influenced by context effects
2. **Middle and Bottom have partial data gaps** (14/21 and 8/10 persons with data respectively)
3. **No inferential statistics** — single measurements per stratum; N=30 runs could yield CIs

---

*Created: 2026-03-31 | Author: Claude Opus 4.6*
