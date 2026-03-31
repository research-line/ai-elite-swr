# Analysis: Instance Separation in Historical Executions

> Created: 2026-03-31
> Occasion: TODO v7.0 — Task "G6/Say-Do Instance Separation clarify"
> Method: Systematic review of all rating files, synthesis files, batch scripts, and session logs

---

## Research Question

Were the various analyses (in particular Batch 1: GA_ges_A, GA_ges_H, GA_ges_AH as well as G6 control experiment) conducted in SEPARATE LLM instances or in the same session/instance?

**Core Principle (v7.0): Each analysis = separate instance. No exceptions.**

---

## Findings

### 1. Batch 1 (Core Syntheses) — SAME INSTANCE

**Evidence:**
- `rating_batch1_D01-D12.md`: ALL 5 SUs (GA_ges_AH, T10_ges_AH, HOM_haeuf_A, GA_ges_A, GA_ges_H) in **ONE file**
- Rater: Claude Opus 4.6 (not the 9 parallel Sonnet batch agents)
- Date: 2026-02-12
- At end: **"Comparative Observations"** — the rater directly compares GA_ges_A vs. GA_ges_H
- The synthesis files (synthese_GA_ges_A.md, synthese_GA_ges_H.md, synthese_GA_ges_AH.md) all bear the same date
- The comparison file (vergleich_VG01_sagen_vs_handeln.md) also 2026-02-12

**Assessment:** NOT SEPARATED. The rater had the GA_ges_A values in context when rating GA_ges_H.

### 2. Batch 4 (Group Syntheses) — SEPARATE INSTANCES

**Evidence:**
- 3 separate rating files: `rating_gruppen_A_D01-D12.md` (roles+gender), `rating_gruppen_B_D01-D12.md` (companies), `rating_gruppen_C_D01-D12.md` (attitudes)
- Rater: Claude Sonnet 4.5
- Consolidated file `rating_gruppen_D01-D12.md` explicitly references "Sources: rating_gruppen_A/B/C_D01-D12.md"

**Assessment:** AT LEAST 3 separate instances (one per A/B/C file).

### 3. 100 Individual Ratings — SEPARATE INSTANCES

**Evidence:**
- `rating_GESAMT_D01-D12.md`, Line 5: "Rater: Claude Sonnet 4.5 (9 parallel batch agents + 1 Opus pilot)"

**Assessment:** 9 separate instances confirmed.

### 4. G5 v2 Cross-Modal Prediction — SEPARATE INSTANCES

**Evidence:**
- `G5_BERICHT_NEU.md`: Explicitly documented as "Op4a/Op4b separate instances"
- v1 (88% confirmed) was invalidated precisely due to missing instance separation

**Assessment:** SEPARATED (explicitly documented).

### 5. Blind Test (Placeholder vs. Fictitious Names) — SEPARATE INSTANCES

**Evidence:**
- `BLINDTEST_BERICHT.md`: "Separate agent instances (no contamination)"

**Assessment:** SEPARATED (explicitly documented).

### 6. G1 Run Convergence — SEPARATE RUNS

**Evidence:**
- `g1_g6_results.json`: Contains "original", "run1", "run2" for 5 groups
- run1 and run2 conducted on 2026-03-30 as new independent runs

**Assessment:** SEPARATED (by design).

### 7. G6 Expected-Discrepancy Control — UNCLEAR

**Evidence:**
- `g1_g6_results.json`: Contains "aussagen" and "handlungen" rating vectors
- Conducted on 2026-03-30 (same session as G1)
- No explicit documentation whether statement and action ratings were in separate instances

**Assessment:** UNCLEAR — likely same instance, as G1 and G6 documented in one session.

### 8. Session Logs

- No conversation protocols from February 2026 (time of Batch 1 execution) available
- Claude project logs in Desktop folder begin only in March 2026
- Reconstruction from logs therefore NOT POSSIBLE

---

## Overall Summary

| Analysis | Model | Instance Separation | Affected Finding |
|---------|--------|-------------------|------------------|
| **Batch 1 Ratings** (GA_ges_A, GA_ges_H, GA_ges_AH, T10, HOM) | Opus 4.6 | **NO** — one file, one rater | RQ3 Say-Do comparison |
| **VG01 Say vs. Do** | Opus 4.6 | **NO** — based on Batch 1 ratings | RQ3 result |
| **Batch 4 Groups** (15 groups) | Sonnet 4.5 | **YES** — 3 separate files | All group comparisons |
| **100 Individual Ratings** | Sonnet 4.5 | **YES** — 9 parallel agents | PCA, HDBSCAN, KW |
| **G5 v2 Cross-Modal** | Opus 4.6 | **YES** — explicitly documented | Cross-Modal Prediction |
| **Blind Test** | Opus 4.6 | **YES** — explicitly documented | Anonymization robustness |
| **G1 Run Convergence** | Opus 4.6 | **YES** — by design | Test-Retest ICC=0.902 |
| **G6 Expected-Discrepancy** | Opus 4.6 | **UNCLEAR** | Control experiment |

---

## Consequences

### MUST be repeated:
1. **GA_ges_A** — Op1+Op2 in separate instance (no context from GA_ges_H)
2. **GA_ges_H** — Op1+Op2 in separate instance (no context from GA_ges_A)
3. **G6** — Statement rating and action rating in separate instances

### Can remain:
- **GA_ges_AH** — not compared against GA_ges_A/H, own synthesis unit
- **T10_ges_AH, HOM_haeuf_A** — no methodological dependency on each other
- **All Batch 4 groups** — already separated
- **G1, G5 v2, Blind Test** — already clean

### Automatically resolved:
- **VG01** — emerges anew from the independent GA_ges_A/H ratings

---

*Created: 2026-03-31 | Method: File analysis + structural evidence | Author: Claude Opus 4.6*
