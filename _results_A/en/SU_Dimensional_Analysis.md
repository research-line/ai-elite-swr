# Vessel Dimensional Analysis: Systematic Determination of All Possible Vessels

**Research Project:** Transhumanism / Silicon Valley Worldviews
**Date:** 2026-02-11
**Method:** Combinatorial enumeration of all vessel dimensions

---

## 1. Available Variables (Dimensions)

Each vessel is a FILTER on the overall dataset. The filter dimensions are:

### Dimension A: PERSON (Whose data?)

| Level | Code | Description | Number of Options |
|-------|------|-------------|-----------------|
| A1 | Individual person | Exactly 1 person | 100 |
| A2 | Top-N | The N highest-rated | Top 5, 10, 20, 50 = 4 |
| A3 | All | All 100 | 1 |
| A4 | Role | Predefined role group | CEOs, academics, investors, founders, politics = ~5 |
| A5 | Company | Company affiliation | Anthropic, OpenAI, Google, Meta, xAI, ... = ~10 |
| A6 | Stance | Content-based grouping (after coding) | Open/Closed, risk/speed, reg-pro/contra = ~6 |
| A7 | Demographics | Gender, age, origin | m/f, young/old, US/non-US = ~6 |
| A8 | Cluster | Emergent bottom-up cluster | k (unknown, ~3-8) |

### Dimension B: MODALITY (Which data type?)

| Level | Code | Description |
|-------|------|-------------|
| B1 | Statements only (S) | Only statement_text |
| B2 | Actions only (A) | Only actions |
| B3 | Both (S+A) | Statements and actions combined |

### Dimension C: TIME (Which time period?)

| Level | Code | Description | Number of Options |
|-------|------|-------------|-----------------|
| C1 | Single year | Exactly 1 year | 2010-2026 = 17 |
| C2 | Time series | Connected time period | See list below |
| C3 | Overall | Complete time period | 1 |

**Defined Time Series (C2):**

| Code | Period | Justification |
|------|--------|-----------|
| C2a | 2000-2009 | Pre-deep-learning era (opportunity only) |
| C2b | 2010-2015 | Build phase (ImageNet to pre-AlphaGo) |
| C2c | 2016-2019 | Acceleration phase (AlphaGo to GPT-2) |
| C2d | 2020-2022 | Explosion phase (GPT-3 to ChatGPT) |
| C2e | 2023-2026 | Post-ChatGPT (regulation, AGI debate) |
| C2f | 2010-2016 | Early phase complete |
| C2g | 2016-2026 | Since AI revolution |
| C2h | 2010-2026 | Complete systematic survey period |
| C2i | 2000-2026 | Maximum period incl. opportunistic |

### Dimension D: CONTENT/CATEGORY (Which topics?)

| Level | Code | Description | Number of Options |
|-------|------|-------------|-----------------|
| D1 | All categories | No thematic filter | 1 |
| D2 | Primary category | Only 1 primary category | WV,SB,MB,ET,GE,RI,FO,MA,AR,TR,RE,SP = 12 |
| D3 | Secondary code | Only 1 secondary code | OPT,PES,AMB,POL,PHI,EMP,ANE,PRO = 8 |
| D4 | Topic cluster | Emergent topic cluster (after coding) | unknown, ~5-10 |

### Dimension E: CONGRUENCE (Which statement-action relationship?)

| Level | Code | Description |
|-------|------|-------------|
| E1 | All | No congruence filter |
| E2 | Consistent | Only statements with consistent actions |
| E3 | Contradiction | Only statements with contradicting actions |
| E4 | No action relation | Statements without linked action |

### Dimension F: HOMOGENIZATION (Preprocessing)

| Level | Code | Description |
|-------|------|-------------|
| F1 | Raw | Data as collected, no preprocessing |
| F2 | Cluster-homogenized | Only statements/actions from one bottom-up cluster |
| F3 | Deduplicated | Originality counter > 1 removed (uniqueness only) |

---

## 2. Combinatorial Space

### 2.1 Formula

```
Vessel = A x B x C x D x E x F
```

### 2.2 Maximum Combinations (theoretically)

| Dimension | Levels |
|-----------|--------|
| A (Person) | 100 + 4 + 1 + 5 + 10 + 6 + 6 + ~5 = ~137 |
| B (Modality) | 3 |
| C (Time) | 17 + 9 + 1 = 27 |
| D (Content) | 1 + 12 + 8 + ~7 = ~28 |
| E (Congruence) | 4 |
| F (Homogenization) | 3 |

**Theoretical maximum: 137 x 3 x 27 x 28 x 4 x 3 = ~3.7 million**

This is absurdly large. Most combinations are meaningless or empty.

### 2.3 Sensible Reduction Rules

| Rule | Justification |
|------|-------------|
| R1: F=F1 as default | Homogenization only for bottom-up analysis |
| R2: D=D1 as default | Category filter only sensible after coding |
| R3: E only with B=B3 or B=B1 | Congruence needs action relation |
| R4: A8 (cluster) only after clustering | Not plannable upfront |
| R5: C2a only with A2(Top20) | Too little data before 2010 for all |
| R6: Minimum vessel size >= 15 | Too-small vessels produce fragile syntheses |
| R7: A1 x C1 only for Top 20 | Individual x single year usually too sparse |

---

## 3. Systematic Enumeration: ALL Sensible Vessel Types

### LEVEL 1: Base Vessels (A x B x C, with D=D1, E=E1, F=F1)

The fundamental structure: who x what x when

```
                        B1 (Statements)    B2 (Actions)    B3 (Both)
                        =============    ================    ===========

A3 (All 100):
  C3 (overall)               [1]               [2]               [3]
  C1 (per year, 17x)        [4a-q]            [5a-q]            [6a-q]
  C2 (time series, 9x)      [7a-i]            [8a-i]            [9a-i]

A2 (Top N):
  C3 (overall)              [10a-d]           [11a-d]           [12a-d]
  C1 (per year)             [13]              [14]              [15]
  C2 (time series)          [16]              [17]              [18]

A1 (Individual):
  C3 (overall)              [19: 100x]        [20: 100x]        [21: 100x]
  C2 (time series)          [22: 20x9]        [23: 20x9]        [24: 20x9]
  C1 (per year)             (only Top 5, dense years only)        [25: ~50]

A4-A7 (Groups):
  C3 (overall)              [26: ~27x]        [27: ~27x]        [28: ~27x]
  C2 (time series)          [29: selectively] [30: selectively] [31: selectively]
```

### COUNTING LEVEL 1:

| Block | Vessels | Description |
|-------|---------|-------------|
| [1]-[3] | 3 | All 100, overall, by modality |
| [4]-[6] | 51 | All 100, per year (17), by modality (3) |
| [7]-[9] | 27 | All 100, per time series (9), by modality (3) |
| [10]-[12] | 12 | Top N (4 levels), overall, by modality (3) |
| [13]-[18] | ~30 | Top N, by time (selectively), by modality |
| [19]-[21] | 300 | Individual (100), overall, by modality (3) |
| [22]-[24] | ~540 | Individual (Top 20), time series (9), modality (3) |
| [25] | ~50 | Individual x single year (dense combinations only) |
| [26]-[31] | ~100 | Groups (~27), overall + selectively, modality |
| **Sum Level 1** | **~1,113** | |

### LEVEL 2: Congruence Filters (E2, E3, E4 on Level-1 vessels)

Only applicable to selected Level-1 vessels:

| Base Vessel | x E2 (consistent) | x E3 (contradiction) | Research Question |
|------------|-------------------|---------------------|---------------|
| [1] (All, S, overall) | [1-E2] | [1-E3] | Statement worldview with consistent vs. inconsistent |
| [3] (All, S+A, overall) | [3-E2] | [3-E3] | Total worldview of authentic vs. incongruent |
| [21] (Individual, S+A, overall) | [21-E2: 20x] | [21-E3: 20x] | Per person: congruent vs. incongruent self |
| [6a-q] (All, S+A, year) | [6-E2: 17x] | [6-E3: 17x] | Per year: congruent vs. incongruent |

**Additional vessels through congruence: ~100**

### LEVEL 3: Category Filters (D2 on selected Level-1 vessels)

Only after coding (Phase 4) possible. Only on statement vessels (B1):

| Base Vessel | x 12 Categories | Research Question |
|------------|----------------|---------------|
| [1] (All, S, overall) | [1-WV], [1-SB], ..., [1-SP] = 12 | Worldview ONLY from future visions / ONLY from ethics / etc. |
| [4a-q] (All, S, year) | 17 x 12 = 204 | How does e.g. risk discourse change per year? |
| [19] (Individual, S, overall) | 20 x 12 = 240 (Top 20) | What % of Altman's statements are "risk"? |

**Additional vessels through categories: ~460 (many too small -> minimum size filter)**

### LEVEL 4: Bottom-Up Clusters (A8, F2)

Emerges from clustering. Estimated:

| Block | Vessels | Description |
|-------|---------|-------------|
| Statement clusters | ~5-8 | Homogeneous statement bundles |
| Action clusters | ~3-5 | Homogeneous action bundles |
| Cluster x time | ~30-50 | Cluster per time series (to measure drift) |
| **Sum Level 4** | **~40-65** | |

---

## 4. Complete Vessel Space

| Level | Vessels (estimated) | Description |
|-------|---------------------|-------------|
| Level 1 (Base) | ~1,113 | Person x modality x time |
| Level 2 (Congruence) | ~100 | + congruence filter |
| Level 3 (Category) | ~460 | + category filter |
| Level 4 (Cluster) | ~65 | + bottom-up cluster |
| **THEORETICALLY POSSIBLE** | **~1,738** | |

Of which after minimum size filter (>= 15 data points) probably realizable: **~500-700**

---

## 5. Inclusion/Exclusion Decision by Research Question

### 5.1 The Overarching Research Questions

| Nr. | Question | Abbreviation |
|-----|----------|---------|
| F1 | What does the AI elite think about themselves, the world and humanity? | WORLDVIEW |
| F2 | How has this worldview changed from 2010 to 2026? | CHANGE |
| F3 | Do statements and actions agree? | CONGRUENCE |
| F4 | What worldview types exist, and who belongs where? | CLUSTER |
| F5 | Which subgroups think differently than others? | DIFFERENCE |
| F6 | Which worldview has the most power/resources? | POWER |

### 5.2 Mapping: Research Question -> Necessary Vessels

**F1 (WORLDVIEW) -- What does the AI elite think?**

| Vessel | Priority | Justification |
|--------|----------|-------------|
| All, S+A, overall [3] | P1 | THE collective worldview |
| All, S only, overall [1] | P1 | Worldview only by words |
| All, A only, overall [2] | P1 | Worldview only by deeds |
| Top 10, S+A, overall [12a] | P1 | Worldview of powerful ones |
| Individual x 20, S+A, overall [21: 20x] | P1 | 20 individual worldviews |
| Individual x 80, S+A, overall [21: 80x] | P2 | Remaining 80 persons |
| **Vessels for F1: ~103** | | |

**F2 (CHANGE) -- How has worldview changed?**

| Vessel | Priority | Justification |
|--------|----------|-------------|
| All, S+A, per year [6a-q: 17x] | P1 | **Annual time series (core!)** |
| All, S only, per year [4a-q: 17x] | P1 | Statement time series |
| All, A only, per year [5a-q: 17x] | P2 | Action time series |
| All, S+A, time series [9a-i: 9x] | P1 | Epoch comparison |
| Top 10, S+A, time series early vs. late [selectively] | P1 | Change in Top 10 |
| Individual x 10, S+A, time series early vs. late | P2 | Individual change |
| **Vessels for F2: ~80** | | |

**F3 (CONGRUENCE) -- Do saying and doing agree?**

| Vessel | Priority | Justification |
|--------|----------|-------------|
| All, S only, overall [1] + all, A only, overall [2] | P1 | Global saying-vs-doing comparison |
| All, S only, per year + all, A only, per year | P1 | Congruence time series (17 pairs) |
| All, S+A, overall, consistent [3-E2] | P1 | World of the congruent |
| All, S+A, overall, contradiction [3-E3] | P1 | World of the incongruent |
| Top 20, S only + A only, overall (20 pairs) | P1 | Per-person congruence |
| Cross-modal: S->synth. A, A->synth. S | P1 | Prediction experiment |
| **Vessels for F3: ~80** | | |

**F4 (CLUSTER) -- What worldview types exist?**

| Vessel | Priority | Justification |
|--------|----------|-------------|
| Bottom-up statement clusters (~5-8) | P1 | Emergent statement types |
| Bottom-up action clusters (~3-5) | P1 | Emergent action types |
| Cluster x time series (~30-50) | P2 | Cluster drift over time |
| **Vessels for F4: ~40-65** | | |

**F5 (DIFFERENCE) -- Which subgroups think differently?**

| Vessel | Priority | Justification |
|--------|----------|-------------|
| CEOs, S+A, overall | P1 | |
| Academics, S+A, overall | P1 | |
| Investors, S+A, overall | P1 | |
| Founders, S+A, overall | P1 | |
| Anthropic vs. OpenAI vs. Google | P1 | Company comparison |
| Open-source vs. Closed-source | P1 | Stance comparison |
| Risk-warner vs. Accelerator | P1 | |
| Women vs. Men | P2 | |
| Young vs. Old | P2 | |
| Transformer-authors vs. rest | P2 | |
| **Vessels for F5: ~30** | | |

**F6 (POWER) -- Which worldview has the most power?**

Uses results from F4 (clusters) and weights by score/rank from Top-100 list. No new vessels needed.

### 5.3 Summary: Included Vessels

| Research Question | P1 Vessels | P2 Vessels | Total |
|-----------------|-----------|-----------|-------|
| F1 WORLDVIEW | ~23 | ~80 | ~103 |
| F2 CHANGE | ~55 | ~25 | ~80 |
| F3 CONGRUENCE | ~60 | ~20 | ~80 |
| F4 CLUSTER | ~13 | ~50 | ~65 |
| F5 DIFFERENCE | ~20 | ~10 | ~30 |
| F6 POWER | 0 (uses F4) | 0 | 0 |
| **TOTAL (with overlap)** | **~120** | **~130** | **~250** |

After deduplication (many vessels serve multiple questions):
**Estimated ~200 unique vessels, of which ~120 P1.**

---

## 6. What's Missing? Checklist

| Dimension | Covered? | Note |
|-----------|----------|------|
| Person (individual) | Yes | 100 vessels |
| Person (top N) | Yes | 4 levels |
| Person (all) | Yes | |
| Person (role) | Yes | CEO, acad., invest., founder, policy |
| Person (company) | Yes | Anthropic, OpenAI, Google, ... |
| Person (stance) | Yes | Open/closed, risk/speed, reg+/- |
| Person (demographics) | Yes | m/f, young/old, US/non-US |
| Person (cluster) | Yes | Bottom-up |
| Modality (S) | Yes | |
| Modality (A) | Yes | |
| Modality (S+A) | Yes | |
| Time (single year) | Yes | 17 years |
| Time (time series) | Yes | 9 defined series |
| Time (overall) | Yes | |
| Content (category) | Yes | 12 primary, 8 secondary |
| Content (cluster) | Yes | Bottom-up |
| Congruence | Yes | consistent/contradiction/without |
| Homogenization | Yes | raw/cluster/deduplicated |

### Possible Additions:

| Dimension | Description | Inclusion? |
|-----------|-------------|-----------|
| Platform | YouTube only / Twitter only / Podcasts only | P3 -- interesting but secondary. Platform-bias analysis. |
| Language | English only / non-English only | P3 -- expect too little non-English data. |
| Mode | Oral only / written only | P2 -- do people talk differently than they write? Interesting! |
| Originality | Only statements with originality > 3 (often repeated) | P2 -- core beliefs = what someone says repeatedly. |
| Edge cases | Only edge cases | P3 -- methodologically interesting but niche. |

---

## 7. Final Vessel Architecture (Recommendation)

```
LAYER 1: BASE VESSELS (Priority 1, always generate)
================================================================

  Global vessels (3):
    [G-S]     All 100, statements only, overall
    [G-A]     All 100, actions only, overall
    [G-SA]    All 100, statements+actions, overall

  Annual vessels (51):
    [Y-YYYY-S]    All 100, statements only, per year (17x)
    [Y-YYYY-A]    All 100, actions only, per year (17x)
    [Y-YYYY-SA]   All 100, S+A, per year (17x)

  Epoch vessels (15):
    [E-xx-S]   All 100, statements only, 5 main epochs
    [E-xx-A]   All 100, actions only, 5 main epochs
    [E-xx-SA]  All 100, S+A, 5 main epochs

  Individual persons (100):
    [P-xxx-SA]  Each 1 per person, S+A, overall

  Congruence (4):
    [C-S]      All, statements with action consistency
    [C-A]      All, actions with statement consistency
    [C-W-S]    All, statements with action contradiction
    [C-W-A]    All, actions with statement contradiction

  Sum Layer 1: ~173

LAYER 2: GROUP VESSELS (Priority 1, for comparative analyses)
================================================================

  Role groups (5 x 3 modalities = 15):
    [R-ceo-S/A/SA]  [R-acad-S/A/SA]  [R-inv-S/A/SA]
    [R-founder-S/A/SA]  [R-policy-S/A/SA]

  Stance groups (6 x 1 = 6, S+A only):
    [H-open-SA]  [H-closed-SA]
    [H-risk-SA]  [H-speed-SA]
    [H-regpro-SA]  [H-regcon-SA]

  Company groups (selective, 5 x 1 = 5):
    [F-anthropic-SA]  [F-openai-SA]  [F-google-SA]
    [F-meta-SA]  [F-xai-SA]

  Sum Layer 2: ~26

LAYER 3: BOTTOM-UP CLUSTERS (Priority 1, count emerges)
================================================================

  Statement clusters (~5-8 vessels)
  Action clusters (~3-5 vessels)

  Sum Layer 3: ~8-13

LAYER 4: DEEPENING (Priority 2, selective by need)
================================================================

  Individual x epochs (Top 20 x 5 epochs = 100, S+A only)
  Category vessels (All, S only, overall, x 12 categories = 12)
  Annual vessels x congruence (17 x 2 = 34)
  Mode comparison (all oral vs. all written = 2)
  Originality vessels (frequently repeated statements only = 1)
  Bottom-up clusters x epochs (~8 x 5 = 40)

  Sum Layer 4: ~189

================================================================
TOTAL: ~400-410 VESSELS (of which ~210 P1, ~190 P2)
================================================================
```

---

*Dimensional analysis created on 2026-02-11*
*Research project: Transhumanism / Silicon Valley Worldviews*
