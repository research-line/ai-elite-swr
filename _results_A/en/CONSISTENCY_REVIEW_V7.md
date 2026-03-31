# Consistency Review v7 -- KI_Elite_v2_en.tex

**Date:** 2026-03-31
**Reviewer:** Claude Opus 4.6 (automated)
**File:** `paper_A/KI_Elite_v2_en.tex`
**Paper status:** 2026-03-27 (according to file header)

---

## Summary

**7 issues found**, of which 2 critical (missing labels), 2 moderate (outdated references), 3 minor (consistency nuances). No outdated v1 values in main text; v1 values are correctly marked as comparison values.

---

## Issues Found

### Issue 1 -- CRITICAL: Missing \label{sec:method} (Line 93)

**Line 93 (Abstract):**
```latex
(described in Section~\ref{sec:method})
```

**Problem:** The label `sec:method` does not exist anywhere in the file. The actual label for the methods section is `sec:methodik` (Line 195). LaTeX will output "??" here.

**Fix:** `\ref{sec:method}` → `\ref{sec:methodik}`

---

### Issue 2 -- CRITICAL: Missing \label{sec:limitations} (Line 707)

**Line 707 (Discussion, Methodological Reflection):**
```latex
are systematically analyzed in the limitations section below (Section~\ref{sec:limitations}).
```

**Problem:** The label `sec:limitations` does not exist. The actual label is `sec:limitationen` (Line 730). LaTeX will output "??" here.

**Fix:** `\ref{sec:limitations}` → `\ref{sec:limitationen}`

---

### Issue 3 -- MODERATE: Old Zenodo DOI + "companion paper" in Data Availability Statement (Line 874)

**Line 874:**
```latex
The companion paper on the SWR method is available at: \url{https://doi.org/10.5281/zenodo.18736720}.
```

**Problem:** Double relic:
1. Reference to "companion paper" contradicts current strategy (Paper B will be written after Paper A submission; Line 945 confirms: "Geiger2026SWR removed -- Paper B will be written after Paper A submission").
2. Old Zenodo DOI 10.5281/zenodo.18736720 is still present.

**Fix:** Remove entire sentence. Alternatively replace with forward reference:
```latex
A companion paper detailing the SWR method is in preparation.
```

---

### Issue 4 -- MODERATE: "companion paper" in File Header (Line 9)

**Line 9:**
```latex
%% Companion Paper: SWR_v1_ger.tex (Synthetische Weltbild-Rekonstruktion)
```

**Problem:** This LaTeX comment is invisible in PDF but references old structure (SWR_v1_ger.tex as separate paper). Can cause confusion in further development.

**Fix:** Update or remove line:
```latex
%% Paper B (SWR method paper) will be written after Paper A submission
```

---

### Issue 5 -- MINOR: Delta=-3 in Discussion instead of v2 value (Line 701)

**Line 701 (Discussion, Agentic Alignment):**
```latex
The say-do gap indicated by RQ3 (largest observed discrepancy: egalitarianism $\Delta = -3$)
```

**Problem:** The value Δ=-3 is the **v1 value** for D11. The current v2 value is Δ=-2 (Line 459, Table 5). While Δ=-3 is correct as "largest observed" (namely v1), the context suggests the current finding is meant. The Conclusion (Line 841) correctly names Δ=-2 for v2. This creates substantive contradiction within Discussion vs. Conclusion.

**Context comparison:**
- Table (L. 459): D11 Δv2 = -2, Δv1 = -3 ✓
- Results text (L. 479): "D11, Δ -2 in v2, -3 in v1" ✓
- Synopsis table (L. 652): "D07 +2, D11 -2; stable across v1/v2" ✓
- Conclusion (L. 841): "D11, Δ -2" ✓
- **Discussion (L. 701): "Δ = -3"** ← Inconsistent

**Fix:** Either update to v2 value:
```latex
(largest observed discrepancy: egalitarianism $\Delta = -2$)
```
Or explicitly mark as v1 value:
```latex
(largest observed discrepancy: egalitarianism $\Delta = -3$ in v1, $-2$ in v2)
```

---

### Issue 6 -- MINOR: MAE=1.25 as v1 comparison value (Line 287)

**Line 287 (Quality Assurance, expected-discrepancy control):**
```latex
By comparison, the real AI elite gap (MAE $= 1.25$) is $2.5\times$ larger
```

**Problem:** The value MAE=1.25 is neither the v1 value (1.42) nor the v2 value (0.75). It likely derives from older calculation or different calculation basis. All other locations in the paper consistently name:
- v1 MAE = 1.42 (L. 290, 463, 468, 749)
- v2 MAE = 0.75 (L. 290, 463, 468, 749)

The value 1.25 appears nowhere else. Moreover: The control-group baseline is MAE=0.50 (v1) or 0.92 (v2). The comparison factor "$2.5\times$ larger" fits 1.25/0.50, but the MAE value 1.25 itself is orphaned.

**Fix:** This passage must be decided:
- If v1 context: "the real AI elite gap (MAE $= 1.42$) is $2.8\times$ larger"
- If v2 context: This passage loses its meaning because v2 MAE (0.75) < Control v2 (0.92). The passage would need rewriting to correctly represent v2 finding.

**Recommendation:** Since the passage is in the Quality-Assurance section describing expected-discrepancy control, it should reflect current v2 status. Proposal:
```latex
The resulting statement--action profiles were highly congruent ($r = 0.912$,
MAE $= 0.50$). Under the original same-instance protocol (v1), the real AI
elite gap (MAE $= 1.42$) was $2.8\times$ larger. Under strict instance
separation (v2), the gap shrank to MAE $= 0.75$, falling below the v2
control baseline (MAE $= 0.92$) -- see Section~\ref{sec:ergebnisse:f3}
for the full analysis.
```

---

### Issue 7 -- MINOR: "systematic say-do gap" in Discussion vs. "not reliably distinguishable from noise" in Results

**Affected passages:**
- **Line 669 (Discussion):** "RQ3 indicates a systematic say-do gap at the group level as the most salient finding"
- **Line 290/468 (Results):** "the overall gap magnitude is not reliably distinguishable from measurement noise in single runs"
- **Line 715 (Discussion):** "The systematic group-level say-do gap has a policy implication"

**Problem:** The Discussion section repeatedly refers to "systematic say-do gap" without caveat that overall gap falls within measurement noise. Only in Results is it clear that only D07 and D11 are robust. Discussion formulations could be read as exaggeration.

**Fix (Line 669):** Specify:
```latex
RQ3~indicates directional say-do discrepancies on specific dimensions
(D07, D11) as the most salient finding
```

**Fix (Line 715):** Already acceptable because context "entire institutional groups ... exhibit consistent discrepancies" could refer to robust dimensions. Optional: add "on the D07/D11 axis."

---

## Checked and Found Consistent

### Outdated Values (v1 vs. v2)
- ✅ MAE=0.75 correct in table (L. 463), results text (L. 468, 290), limitations (L. 749)
- ✅ MAE=1.42 correct as v1 comparison value marked (L. 290, 463, 468, 749)
- ✅ D07 Δ=+2 consistent (L. 455, 470, 479, 482, 652, 749, 841)
- ✅ D11 Δ=-2 (v2) consistent (L. 459, 470, 479, 482, 652, 749, 841)
- ✅ D11 Δ=-3 (v1) correct as v1 value in table (L. 459) and results (L. 479)
- ⚠️ EXCEPTION: L. 701 (see Issue 5) and L. 287 (see Issue 6)

### Geiger2026SWR Remnants
- ✅ `\citet{Geiger2026SWR}` is not called anywhere
- ✅ bibitem correctly removed (L. 945: comment confirms removal)
- ⚠️ EXCEPTION: Zenodo DOI at L. 874 (see Issue 3)

### Inter-LLM / Inter-Model
- ✅ "inter-model replication" (L. 287) correctly formulated as "external replication" / "independent research task", NOT as validation proposal
- ✅ No "inter-LLM" as internal validation criterion

### Terminology
- ✅ "focus control" consistently used (L. 287, 296, 745, 1236)
- ✅ "contamination" only as "contamination risk" or "contamination effect" (not "contamination control")
- ✅ "IMIIRR" consistent (L. 287, 707)
- ✅ No "inter-rater" as method designation (only as comparison value for human coder)

### Data Consistency Abstract/Results/Discussion/Conclusion
- ✅ "technological messianism with ambivalence structure" consistent
- ✅ 3,132 data points consistent (L. 93 via "group-level syntheses", L. 146, L. 209, L. 751, L. 1142)
- ✅ 12 dimensions consistent
- ✅ 4 types (Architect, Guardian, Innovator, Liberator) consistent
- ✅ 9 inter-group comparisons consistent (L. 93, 146, 281)
- ✅ IMIIRR ICC=0.902 consistent (L. 287, 707, 759, 761)
- ✅ D09/D11 as "dual trough" consistent

### Bibliography Consistency
- ✅ All `\citet{}` and `\citep{}` in text have corresponding `\bibitem{}` entries
- ✅ No orphaned `\cite{Geiger2026SWR}`

### Label-Reference Consistency
- ✅ All `\ref{tab:...}`, `\ref{fig:...}`, `\ref{app:...}` have corresponding labels
- ✅ All `\ref{sec:ergebnisse:...}`, `\ref{sec:methodik:...}`, `\ref{sec:limitationen:...}` have labels
- ⚠️ EXCEPTION: `\ref{sec:method}` (L. 93) and `\ref{sec:limitations}` (L. 707) -- see Issues 1 and 2

---

## Priority Ranking

| Prio | Issue | Severity | Line |
|------|-------|----------|------|
| 1 | Missing \label{sec:method} | CRITICAL (produces "??" in PDF) | 93 |
| 2 | Missing \label{sec:limitations} | CRITICAL (produces "??" in PDF) | 707 |
| 3 | Old Zenodo DOI + companion paper | MODERATE (content outdated) | 874 |
| 4 | MAE=1.25 orphan value | MINOR-MODERATE (inconsistent value) | 287 |
| 5 | Δ=-3 instead v2 value in Discussion | MINOR (confusing) | 701 |
| 6 | "systematic say-do gap" phrasing | MINOR (nuance) | 669, 715 |
| 7 | Companion paper in header comment | MINOR (comment only) | 9 |
