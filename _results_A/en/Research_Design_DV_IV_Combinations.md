# Research Design: DV — Operationalizations — IV + Combination Matrix

**Research Project:** Transhumanism / Silicon Valley Worldviews
**Date:** 2026-02-11
**Version:** 2.0 (DV/Op/IV distinction corrected)

---

## 0. VARIABLES ARCHITECTURE (4 Levels)

```
LEVEL 1: DEPENDENT VARIABLES (DVs) — WHAT we measure
         = 3 worldview components (latent constructs)

LEVEL 2: OPERATIONALIZATIONS (Ops) — HOW we measure DVs
         = 6 analysis techniques providing different access to DVs

LEVEL 3: MEASUREMENT VARIABLES (MVs) — WHICH concrete outputs Ops deliver
         = 50+ specific measured values (text, scores, vectors, ...)

LEVEL 4: INDEPENDENT VARIABLES (IVs) — WHAT we manipulate
         = 6 pool dimensions (timeframe, modality, group, ...)
```

---

## 1. DEPENDENT VARIABLES (DVs) — 3 Worldview Components

Study measures 3 latent constructs (DVs) that together form WORLDVIEW:

| DV | Name | Research Question | Reference |
|----|------|-----------|----------|
| **DV1** | **Self-Image** | What does AI elite think about itself? | Interview Question 1 |
| **DV2** | **Worldview** | What does AI elite think about world? | Interview Question 2 |
| **DV3** | **Human Image** | What does AI elite think about humanity? | Interview Question 3 |

These 3 DVs not directly measurable (latent constructs).
Made accessible through 6 operationalizations.

---

## 2. OPERATIONALIZATIONS (Ops) — 6 Analysis Techniques

Each operationalization opens different access to 3 DVs:

| Op | Technique | Access | DV Relations |
|----|-----------|--------|-------------|
| **Op1** | Narrative LLM-Fiction Analysis | Qualitative: Synthetic person answers 3 interview questions | DV1, DV2, DV3 direct |
| **Op2** | Dimensional Quantification | Quantitative: 12 rating dimensions (D01-D12) | DV1 → D01-D04, DV2 → D05-D08, DV3 → D09-D12 |
| **Op3** | Typology (4 ideal types) | Categorical: Top-down Weberian ideal types | DV1 + DV2 combined → Architect/Guardian/Innovator/Liberator |
| **Op4** | Cross-Modal Prediction | Behavioral: Predicted vs. actual actions (say-do gap) | DV1, DV2, DV3 predictive validity |
| **Op5** | Linguistic-Semantic Analysis | Textual: Frequent themes, semantic networks | DV1, DV2, DV3 from language patterns |
| **Op6** | Longitudinal Trends | Time-Series: Dimension changes over 16-17 years | DV1, DV2, DV3 temporal dynamics |

---

## 3. MEASUREMENT VARIABLES (MVs) — Outputs of Operationalizations

Each Op produces specific measured variables (MVs):

### Op1 Outputs (Fiction Analysis)
- Synthetic person profile (narrative text)
- Dimensional ratings (12 dimensions × 3 person types)
- Thematic codes (extracted from narrative)

### Op2 Outputs (Dimensional Quantification)
- 12-dimension rating scores per group (scale 1-10)
- Pearson correlations between dimensions
- PCA components
- Clustering metrics (Silhouette, HDBSCAN)

### Op3 Outputs (Typology)
- 4 ideal type profiles (narrative + average ratings)
- Type membership probabilities per person
- Cliff's delta effect sizes between types
- Type frequency distribution

### Op4 Outputs (Cross-Modal Prediction)
- Prediction accuracy (% confirmed/plausible/refuted)
- Surprise surprises (unpredictable actions)
- Say-do gap scores per dimension
- Congruence matrix (statements vs. actions)

### Op5 Outputs (Linguistic Analysis)
- Frequency histograms of themes
- Semantic network maps
- Similarity metrics (cosine, Jaccard)
- Thematic clustering

### Op6 Outputs (Temporal Trends)
- Slope coefficients (dimension change per year)
- Breakpoint years (structural changes)
- Correlation matrices (2010, 2015, 2020, 2025)
- Volatility scores per dimension

---

## 4. INDEPENDENT VARIABLES (IVs) — 6 Pool Dimensions

IVs are dimensions we "manipulate" by pooling data differently:

| IV | Definition | Values/Combinations |
|----|-----------|-------------------|
| **IV1: Timeframe** | Time period of statements | 2010-2015, 2015-2020, 2020-2025, 2022-2026, Whole-Period |
| **IV2: Modality** | Statements vs. Actions | Statements-Only, Actions-Only, Combined |
| **IV3: Group** | Selection of persons | CEOs, Academics, Founders, Investors, All-100, Top-10 |
| **IV4: Attitude** | Grouping by worldview stance | Risk-Warner, Accelerator, Open-Source, Closed-Source, Pro-Reg, Anti-Reg |
| **IV5: Gender** | Gender of persons | Women, Men |
| **IV6: Company** | Organization affiliation | Anthropic, OpenAI, Google, Meta, Tesla, Other |

---

## 5. COMBINATION MATRIX — Research Design

Complete research design = **Cartesian product of IV combinations**:

```
IV1 (Timeframe) × IV2 (Modality) × IV3 (Group) × IV4 (Attitude) × IV5 (Gender) × IV6 (Company)
```

### Example Combinations (subset):

**Combination G1:** All-100 persons, Statements-Only, Whole-Period, All-Attitudes, All-Gender, All-Companies
→ Global worldview profile of AI elite

**Combination G2:** All-100 persons, Statements-Only, 2022-2026, Risk-Warner vs. Accelerator, All-Gender, All-Companies
→ Worldview contrast over critical period

**Combination G3:** Top-10 persons, Combined (Statements+Actions), 2024-2026, All-Attitudes, All-Gender, Anthropic vs. OpenAI
→ Say-do gap in most powerful actors recent period

**Combination G4:** CEOs, Statements-Only, Whole-Period, Pro-Reg vs. Anti-Reg, All-Gender, All-Companies
→ Regulatory stance correlates with worldview dimensions

**Combination G5:** All-100 persons, Statements-Only, Yearly-Pools (2010, 2015, 2020, 2025), All-Attitudes, Gender-Split
→ Temporal trends with gender comparison

---

## 6. RESEARCH QUESTIONS PER IV COMBINATION

Each IV combination addresses specific research question:

### Timeframe Questions (IV1)
- **Q-T1:** How have worldview dimensions changed over 16 years?
- **Q-T2:** Are there breakpoint years where views shifted sharply?
- **Q-T3:** Which dimensions most volatile? Which most stable?

### Modality Questions (IV2)
- **Q-M1:** Say-do gap: How large is discrepancy between statements and actions?
- **Q-M2:** Are dimensions rated from actions different from dimensions rated from statements?
- **Q-M3:** Which worldview components most predicted by actions?

### Group Questions (IV3)
- **Q-G1:** Does worldview differ by professional role (CEO vs. Academic vs. Founder vs. Investor)?
- **Q-G2:** How do most powerful (Top-10) differ from average?
- **Q-G3:** Are there stable worldview patterns across all groups?

### Attitude Questions (IV4)
- **Q-A1:** Biggest contrast: Risk-Warner vs. Accelerator — how large the worldview gap?
- **Q-A2:** Open-source advocates vs. closed-source: fundamentally different worldviews?
- **Q-A3:** Do pro-regulation vs. anti-regulation advocates have different anthropologies?

### Gender Questions (IV5)
- **Q-GN1:** Do women in AI elite have different worldviews than men?
- **Q-GN2:** Are worldview differences gender-based or role-based (confounding)?

### Company Questions (IV6)
- **Q-C1:** Company culture effect: Does organization shape worldview?
- **Q-C2:** Are Anthropic and OpenAI worldviews fundamentally different?

---

## 7. ANALYSIS PLAN PER OPERATIONALIZATION

### Op1 (Narrative Fiction)
For each IV combination:
- Generate synthetic person via LLM (Claude Opus)
- Have synthetic person answer 3 interview questions
- Extract narratives → score 12 dimensions
- Repeat 3x with different prompts for stability

### Op2 (Dimensional Quantification)
For each IV combination:
- Calculate mean ratings for D01-D12
- Perform PCA on rating matrices
- Run HDBSCAN on reduced spaces
- Calculate Cliff's delta effect sizes
- Produce heatmaps and correlation matrices

### Op3 (Typology)
For each IV combination:
- Assign persons to 4 types (Architect/Guardian/Innovator/Liberator)
- Calculate type frequency distribution
- Analyze type-specific worldviews
- Compare type profiles across IV combinations

### Op4 (Cross-Modal Prediction)
For each IV combination:
- Create statement-only profiles
- Generate predicted action lists
- Compare predictions to actual actions
- Quantify prediction accuracy
- Identify unpredictable actions

### Op5 (Linguistic Analysis)
For each IV combination:
- Extract themes from statements
- Build semantic networks
- Calculate theme frequency rankings
- Identify emergent themes
- Compare theme distributions across groups

### Op6 (Temporal Trends)
- Pool statements into yearly intervals
- Calculate yearly dimension averages
- Fit linear and nonlinear models
- Identify breakpoints (structural changes)
- Analyze correlations between dimensions over time

---

## 8. VALIDATION STRATEGY (Convergent Validity)

**Hypothesis:** If 3 DVs valid, 6 Ops should converge:

| Convergence Test | Expected Result |
|------------------|-----------------|
| Op1 vs. Op2: Do narrative dimensions match quantitative dimensions? | Pearson r > 0.70 |
| Op2 vs. Op3: Do dimensional ratings reproduce type profiles? | Type-typical dimensions match expected direction |
| Op1 vs. Op4: Do predicted actions match narrative worldview? | >80% of predictions confirmed/plausible |
| Op2 vs. Op5: Do frequent themes match high-rated dimensions? | Top themes align with top dimensions |
| All Ops vs. Op6: Are temporal trends consistent across Ops? | Breakpoints appear across Ops |

---

## 9. QUALITY ASSURANCE

- **Blind coding:** 10% random subset re-coded by independent coder
- **Triangulation:** Compare results across 6 Ops
- **Sensitivity analysis:** Repeat key analyses with different coders/prompts
- **Edge case handling:** Document and analyze cases where Ops disagree
- **Power analysis:** Check sample sizes sufficient for planned comparisons

---

## 10. EXPECTED OUTCOMES

### Primary Outputs
- **Worldview profiles** of 100 AI personalities
- **Temporal trends** 2010-2026
- **Say-do gap analysis** across all dimensions
- **4-type typology** with demographic predictors
- **Group contrasts** (roles, attitudes, companies, gender)

### Secondary Outputs
- **Thematic inventory** of AI-elite discourse
- **Semantic networks** of key concepts
- **Inter-rater reliability** scores
- **Convergent validity** metrics
- **Methodological paper** on multi-operationalization approach

---

*Research Design v2.0, 2026-02-11*
*Complete codebook for 6 operationalizations × 4 levels × 6 IV dimensions*
