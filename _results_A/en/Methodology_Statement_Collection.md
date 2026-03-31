# Methodology: Systematic Statement Collection of Top 100 AI Personalities

**Research Project:** Transhumanism / Silicon Valley Worldviews
**Date:** 2026-02-11 (created), 2026-02-11 (revised v2)
**Database:** `_data/aussagen_top100.db` (SQLite)
**Methodological Approach:** Inductive / Grounded Theory (Strauss & Corbin)

---

## 1. Research Goal

**Central Question:** What does the AI elite think about itself, the world and humanity?

Systematic collection and inductive categorization of public statements from 100 most influential AI personalities (per Top100 research 2026-02-11). Goal is reconstruction of **worldviews, self-images and future visions** of these persons — not through pre-defined categories, but through data-driven pattern discovery.

**Complementary:** Triangulation through action analysis — do statements align with observable actions (investments, restructurings, political activities)?

---

## 2. Collection Timeframe

**Primary Collection Period:** 01.01.2010 — 11.02.2026 (16 years)

| Timeframe | Justification | Expected Data Density |
|----------|---------------|----------------------|
| 2000-2009 | Context phase. Early careers, founding (Google 1998, Facebook 2004, Tesla 2003). Only for prominent persons systematically searchable. | Very low — only worthwhile for Top-20 |
| 2010-2015 | Build phase. Deep Learning breakthrough (ImageNet 2012), first public AI debates. Many current actors still little public. | Low to medium |
| 2016-2019 | Acceleration phase. AlphaGo (2016), Transformer paper (2017), GPT-2 (2019). AI becomes public topic. | Medium to high |
| 2020-2023 | Explosion phase. GPT-3, DALL-E, ChatGPT (Nov 2022). Massive media presence all Top-100 persons. | Very high |
| 2024-2026 | Consolidation. AGI debates, regulation, AI billionaires, political dimension. | Very high |

**Practical consequence:**
- Phase 2010-2026 searched systematically
- Phase 2000-2009 captured opportunistically (only if found during search)
- All statements receive `datum_aussage` — timeframe filtering occurs later in analysis, NOT during collection

---

## 3. Data Sources and Platforms

### 3.1 Primary Sources (Highest Yield)

| Platform | Type | Search Strategy | Expected Yield |
|-----------|-----|---------------|----------------|
| YouTube | Video interviews, keynotes, panels | Name + keyword | Very high |
| Twitter/X | Posts, threads, replies | Profile review + keyword | High |
| Podcasts | Long-form interviews | Lex Fridman, All-In, etc. | Very high |
| Conferences | Talks, panels | TED, NeurIPS, Davos, SXSW | High |
| News Media | Interviews, profiles | NYT, WSJ, Bloomberg, CNBC | High |

### 3.2 Secondary Sources

| Platform | Type | Search Strategy | Expected Yield |
|-----------|-----|---------------|----------------|
| LinkedIn | Posts, articles | Profile review | Medium |
| Reddit | AMAs, comments | r/MachineLearning, r/technology | Medium |
| Books/Essays | Monographs, guest contributions | Amazon, Google Scholar | Medium |
| Blogs | Personal blogs, company blogs | Google search | Medium |
| Congressional Testimonies | Official hearings | senate.gov, house.gov | Low |

### 3.3 Tertiary Sources (Aggregators)

| Platform | Type | Search Strategy |
|-----------|-----|---------------|
| Wikiquote | Quote collections | Direct query |
| Goodreads | Book quotes | Author profile |
| BrainyQuote | General quotes | Name search |
| Substack | Newsletters | Author search |

---

## 4. Search Terms (Search Terms)

### 4.1 Person Identifier
Each search combined with **full name** of person.

### 4.2 Content Search Terms (combined with person)

**Category A: Worldview / Future Vision**
- "future of humanity", "future of AI"
- "vision for the world", "world in 10 years", "world in 2030"
- "society", "civilization"
- "superintelligence", "AGI", "artificial general intelligence"
- "singularity", "post-human", "transhumanism"

**Category B: Self-Image / Identity**
- "my mission", "what drives me", "why I do this"
- "my philosophy", "I believe", "my worldview"
- "responsibility", "legacy"

**Category C: Ethics / Values**
- "AI safety", "AI risk", "existential risk"
- "AI ethics", "alignment", "beneficial AI"
- "inequality", "power", "democracy"
- "open source vs closed", "regulation"

**Category D: Human Image**
- "what makes us human", "consciousness"
- "human intelligence vs AI", "uniquely human"
- "creativity", "meaning", "purpose"
- "jobs", "work", "automation", "replacement"

**Category E: Technology and Society**
- "technology and society", "progress"
- "disruption", "innovation", "acceleration"
- "universal basic income", "UBI", "wealth distribution"
- "education", "healthcare", "climate"

**Category F: Everyday / Informal** (NEW — everyday statements can also be insightful)
- "I think", "personally", "honestly"
- "my kids", "my family", "when I was young"
- "what I learned", "mistake", "failure"
- "fun", "hobby", "life"

### 4.3 Platform-Specific Searches
- YouTube: `"[Name]" interview philosophy | vision | future | humanity | believes`
- Twitter/X: `from:[handle] (believe OR future OR humanity OR world OR society OR vision)`
- Google: `"[Name]" "I believe" OR "my vision" OR "humanity" OR "future" site:nytimes.com OR site:wsj.com OR site:bloomberg.com`

---

## 5. Language Convention

**Core rule:** All statements captured in **original language** (`aussage_text`).

| Field | Content |
|------|---------|
| `aussage_text` | Original wording in original language |
| `sprache` | Language code of original (en, de, zh, ja, fr, ...) |
| `aussage_uebersetzung_de` | German translation (added later, initially empty) |

Translation occurs in separate phase to not slow collection process and separate translation errors from original quotes.

---

## 6. Methodical Approach: Inductive Category Formation

### 6.1 Why NOT pre-filter?

Original methodology (v1) defined inclusion/exclusion criteria BEFORE data collection. Risks:

1. **Pre-exclusion distorts:** "Purely technical" statements may contain implicit worldviews ("We need more compute" → belief in progress)
2. **Everyday is insightful:** How someone speaks about family, leisure or mistakes reveals values
3. **Category coercion:** Pre-categories direct attention and prevent discovering unexpected patterns
4. **Data loss:** Early exclusion is irreversible

### 6.2 Revised Approach: Grounded Theory (Strauss & Corbin)

```
PRINCIPLE: First collect, then review, then form categories,
           then assign, then define inclusion/exclusion,
           then filter.
```

Categories in Section 7 (WV, SB, MB, ...) serve as **sensitizing concepts** — they direct attention but are NOT binding. New categories should emerge from data.

---

## 7. Preliminary Categories (Sensitizing Concepts)

### 7.1 Primary Content Categories (preliminary, changeable)

| Code | Category | Description | Example |
|------|----------|-------------|---------|
| WV | World Vision | Statements about world/humanity future | "AI will be the most transformative technology in human history" |
| SB | Self-Image | Statements about own role, mission, motivation | "I feel a deep responsibility to get this right" |
| MB | Human Nature | Statements about human essence, consciousness | "What makes us human is our ability to..." |
| ET | Ethics/Values | Statements about morality, responsibility, right/wrong | "We have an obligation to ensure AI benefits everyone" |
| GE | Society | Statements about social structure, inequality, politics | "The wealth created by AI must be distributed more broadly" |
| RI | Risk/Safety | Statements about AI risks, existential threat | "The probability of doom is..." |
| FO | Progress/Acceleration | Statements about pace, disruption, acceleration | "We're moving faster than anyone expected" |
| MA | Power/Control | Statements about power concentration, access, control | "Open source ensures no single entity controls AI" |
| AR | Work/Economy | Statements about labor market, UBI, automation | "Most jobs will be transformed within a decade" |
| TR | Transhumanism | Statements about human-machine merger, post-humanity | "Brain-computer interfaces will extend human cognition" |
| RE | Regulation | Statements about laws, governance, international cooperation | "We need global AI governance frameworks" |
| SP | Spirituality/Meaning | Statements about meaning, purpose, spirituality, transcendence | "AI raises profound questions about consciousness" |

**Note:** Categories revised after Phase 2 (sample review). New categories may be added, existing ones merged or split.

### 7.2 Secondary Codes (complementary, multiple assignment possible)

| Code | Description |
|------|-------------|
| OPT | Optimistic tone |
| PES | Pessimistic tone |
| AMB | Ambivalent tone |
| POL | Politically connoted |
| PHI | Philosophically reflected |
| EMP | Empirically grounded |
| ANE | Anecdotal |
| PRO | Provocative/Controversial |
| HA | Action reference — statement relates to concrete action |

---

## 8. Action Analysis: Saying vs. Doing

### 8.1 Concept

Statements alone are insufficient for worldview reconstruction. People can consciously or unconsciously act differently than they speak. Parallel to statements, a **action database** is maintained.

### 8.2 Captured Action Types

| Type | Description | Example |
|-----|-------------|---------|
| investment | Financial participation in companies/projects | Bezos invests $4B in Anthropic |
| sale | Divestment of shares/assets | Musk sells Tesla stock |
| purchase | Acquisition of companies/assets | Microsoft buys Activision |
| restructuring | Organizational changes | OpenAI transforms into for-profit |
| founding | New company founding | Sutskever founds Safe Superintelligence |
| departure | Leaving position | Hinton leaves Google |
| layoff | Personnel reduction | Meta lays off 11,000 employees |
| hiring | Significant personnel decisions | Anthropic hires ex-OpenAI safety team |
| lobbying | Political influence | Tech CEOs meet Biden/Trump |
| donation | Philanthropic activities | Altman donates $8M to GiveDirectly UBI |
| lawsuit | Legal disputes | NYT vs. OpenAI |
| partnership | Strategic cooperation | Google + Anthropic cloud deal |
| product_launch | Product releases | Release of GPT-4, Claude 3, Gemini |
| political | Political activities/positions | Sacks becomes AI Czar |
| other | Other relevant actions | — |

### 8.3 Statement <-> Action Linkage

Each statement can link to zero or more actions:

| Relationship Type | Description | Example |
|---|---|---|
| `consistent` | Action fits statement | Says "AI safety first" + invests in safety research |
| `contradiction` | Action contradicts statement | Says "Open source is important" + closes model access |
| `unclear` | Relationship not clearly determinable | — |
| `context` | Action provides context for statement | Says "We had to act" after layoff wave |

---

## 9. Workflow: Revised 7-Phase Process

```
Phase 1: BROAD COLLECTION (no filters, no categories)
======================================================
  For each Top 100 person:
  1. YouTube search (Top-5 interviews, including older)
  2. Twitter/X profile review (top posts, including everyday)
  3. Google News (prominent interviews 2010-2026)
  4. Podcast search (Lex Fridman, All-In, etc.)
  5. Aggregators (Wikiquote, BrainyQuote, etc.)
  -> CAPTURE everything person said
  -> inclusion = 1 (default), category = empty
  -> Original language, no translation
  -> Parallel: capture actions (investments, founding, etc.)

Phase 2: SAMPLE REVIEW (inductive)
======================================================
  Random sample ~10 statements per person (Top 20 persons):
  1. What stands out? Which themes emerge?
  2. Which statements fit no pre-category?
  3. Which new categories emerge?
  4. How do these people talk? (Style, framing, self-staging)
  -> WRITE MEMO: What did I discover?
  -> Revise category system

Phase 3: CATEGORY FORMATION (data-driven)
======================================================
  Based on Phase 2 findings:
  1. Confirm, change, expand preliminary categories
  2. Create new categories in DB
  3. Refine category definitions (boundary rules)
  4. Create coding guide
  -> Result: Final category system

Phase 4: SYSTEMATIC CODING
======================================================
  Go through all collected statements:
  1. Assign primary category/categories
  2. Add secondary codes (OPT, PES, PHI, ...)
  3. Establish action references (HA-code + link)
  4. Mark edge cases (edge_case = 1)
  5. Originality check: Same statement in multiple sources?
     -> Increment originality counter

Phase 5: INCLUSION/EXCLUSION DEFINITION (only now!)
======================================================
  Based on coded data:
  1. Which categories relevant to research question?
  2. Which statement types provide no insight?
  3. Formulate inclusion criteria (data-grounded)
  4. Formulate exclusion criteria (data-grounded)
  -> Document criteria with justification
  -> Test criteria on 50 statements (pilot test)

Phase 6: FILTERING AND QUALITY ASSURANCE
======================================================
  1. Apply inclusion/exclusion criteria -> inclusion = 0 for excluded
  2. Quality control: Sources correct? Quotes verbatim?
  3. Add German translations (for included statements)
  4. Action congruence check: Mark contradictions

Phase 7: ANALYSIS — What does AI elite think?
======================================================
  1. Frequency analysis: Which categories dominate?
  2. Person profiles: Worldview profile per person
  3. Saying vs. doing: Where are contradictions?
  4. Network analysis: Who shares positions? Who opposes?
  5. Time series: Do positions change over years?
  6. Cluster analysis: Identify worldview types?
  7. Synthesis: What is the collective worldview of AI elite?
```

---

## 10. Preliminary Inclusion Criteria (Phase 1 — formal criteria only)

During broad collection (Phase 1), only formal minimum criteria apply:

| Nr. | Criterion | Description |
|-----|-----------|-------------|
| F1 | Person in Top 100 | Statement from Top-100 person |
| F2 | Attributability | Statement clearly attributable to person |
| F3 | Publicity | Statement publicly made (no leaks) |
| F4 | Original Wording | Original text available (no paraphrase only) |

**NO content filter in Phase 1.** Even everyday, technical or seemingly irrelevant statements captured. Content filter comes in Phase 5.

---

## 11. Database Schema (v2)

See `_data/aussagen_top100.db` (SQLite).

### Tables:
1. **personen** - 100 persons (from Top-100 research)
2. **aussagen** - All statements/quotes (original language + translation field)
3. **kategorien** - Lookup table for category codes (expandable)
4. **aussagen_kategorien** - n:m assignment statement <-> categories
5. **quellen_typen** - Lookup table for source types
6. **plattformen** - Lookup table for platforms
7. **suchprotokolle** - Documentation of each search performed
8. **handlungen** - Observable actions of persons (NEW)
9. **aussagen_handlungen** - Link statement <-> action with relationship type (NEW)

---

## 12. Limitations

1. **Selection bias:** Only public statements; private convictions may differ
2. **Context dependence:** Interview statements may be strategically motivated
3. **Language bias:** Primary English-language sources
4. **Platform bias:** Twitter/YouTube overrepresented vs. books/essays
5. **Time bias:** Recent statements (2020+) more easily found than older (2010-2015)
6. **Categorization bias:** Despite inductive approach, assignment remains subjective
7. **Completeness:** Not all statements of all 100 persons can be captured
8. **Action bias:** Actions only partly publicly visible; internal decisions hidden
9. **Translation bias:** German translations may lose nuances
10. **Survivorship bias:** Only currently influential persons; formerly influential but now irrelevant persons missing

---

*Methodology created 2026-02-11, revised 2026-02-11 (v2)*
*Revision: Grounded-Theory approach, timeframe 2010-2026, action analysis, original language*
*Research Project: Transhumanism / Silicon Valley Worldviews*
