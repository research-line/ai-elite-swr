# Coding Guide: Transhumanism Research Project

## Systematic Coding of Statements from Top 100 AI Personalities

**Version:** 1.0
**Date:** 2026-02-12
**Database:** aussagen_top100.db
**Corpus:** 1,738 statements, 1,394 actions

---

## 1. Introduction

### 1.1 Purpose

This guide serves as binding reference document for systematic coding of all 1,738 public statements from Top 100 AI personalities. Designed so second coder — human or LLM — can produce identical codings based on instructions. Defines all categories, markers, rules and edge cases comprehensively.

### 1.2 Data Foundation

| Element | Description |
|---------|-------------|
| Database | `aussagen_top100.db` (SQLite) |
| Statements | 1,738 public statements (quotes, utterances, statements) |
| Actions | 1,394 documented actions |
| Coding Unit | Individual statement (one quote, utterance) |
| Storage | Junction table `aussagen_kategorien` |

### 1.3 Coding Unit

Coding unit is always **individual statement**: discrete quote, single utterance or coherent statement from one person. Statements never merged or split. Each statement coded as independent unit.

### 1.4 Coding Architecture

Each statement receives:
- **1-2 primary categories** (from 13 categories) — required, minimum one
- **Exactly 1 tonality marker** (OPT, PES or AMB) — required
- **0-n mode markers** (POL, PHI, EMP, ANE, PRO, HA, STR) — optional
- **0-n structure markers** (KON, ZP, BIO) — optional

Codings stored in junction table `aussagen_kategorien` linking statement IDs with category codes.

---

## 2. Primary Categories (13)

### Overview

| Code | Name | Core Question |
|------|------|-----------|
| WV | World Vision | Where is world heading? |
| SB | Self-Image | Who am I / What drives me? |
| MB | Human Nature | What is the human? |
| EP | Epistemology/Knowledge | What can be known? |
| ET | Ethics/Values | What is right/wrong? |
| GE | Society | What does this mean for society? |
| RI | Risk/Safety | What can go wrong? |
| FO | Progress/Acceleration | How do I evaluate progress? |
| MA | Power/Control | Who controls? |
| AR | Work/Economy | What does this mean economically? |
| TR | Transhumanism | What can/should human become? |
| RE | Regulation | Which concrete governance mechanisms? |
| SP/EX | Spirituality/Existential | What does this mean for meaning and consciousness? |

---

### WV — World Vision

**Definition:** Overarching future vision or grand narrative. Statement describes where world as whole is heading, sketches comprehensive picture of future or formulates epochal categorization.

**Inclusion Criteria:**
- Statements about overall direction of human development
- Epochal categorizations ("We stand at beginning of new era")
- Comprehensive future scenarios affecting multiple life domains
- Civilizational narratives ("Humanity will become interplanetary species")

**Exclusion Criteria:**
- Specific evaluation of progress pace (then FO)
- Specific societal consequences (then GE)
- Concrete economic predictions (then AR)
- Pure risk assessment (then RI)

**Anchor Examples:**
1. "AI will be most transformative technology in human history, more impactful than fire or electricity."
2. "We are entering era where intelligence itself becomes commodity — this changes everything about civilization."
3. "Next fifty years will see more change than last five thousand. Humanity is at inflection point."
4. "I believe we're building last invention humanity will ever need to make."
5. "Convergence of AI, biotech, and nanotechnology will reshape human condition fundamentally."

**Distinction:**
- WV vs. FO: WV describes *overall picture*, FO *evaluates* tempo or character of progress. "AI changes everything" = WV. "AI develops faster than expected" = FO.
- WV vs. GE: WV is overarching narrative, GE names specific societal consequences. "World will change fundamentally" = WV. "Education systems must adapt" = GE.

---

### SB — Self-Image

**Definition:** Identity construction of speaker. How does person see themselves? What role, motivation, strengths or responsibility does person attribute to themselves?

**Inclusion Criteria:**
- Self-descriptions ("I'm optimist / engineer / visionary")
- Statements about personal motivation and drive
- Role attributions ("As CEO I bear responsibility")
- Self-assessment of capabilities or limits
- Statements about personal mission or calling

**Anchor Examples:**
1. "I feel deep responsibility to get this right — if we fail, it's on people like me."
2. "I've always been someone who thinks in decades, not quarters."
3. "My role is be adult in room when everyone else caught up in hype."
4. "I'm not philosopher, I'm engineer. I build things that work."
5. "I see myself as bridge between technical community and policymakers."

---

### MB — Human Nature

**Definition:** Statements about what human *is*. Anthropological determinations: nature, capabilities, limits, essence of human. Descriptive anthropology.

**Inclusion Criteria:**
- Statements about human nature ("Human is by nature...")
- Definition of human capabilities and limits
- Comparisons human vs. machine regarding essence/nature
- Statements about consciousness, emotions, creativity as human properties
- Anthropological determinations ("What makes us human...")

**Anchor Examples:**
1. "What makes us human is our ability to feel empathy and form deep emotional bonds."
2. "Human brain is most complex object in known universe — and we barely understand it."
3. "Humans fundamentally limited in how much information we can process simultaneously."
4. "Creativity isn't computation — there's something irreducibly human about genuine artistic expression."

---

### EP — Epistemology/Knowledge Claims

**Definition:** Epistemic positioning. Statements about what can be known, certainty of predictions, importance of expertise, or how own knowledge capability is assessed.

**Inclusion Criteria:**
- Statements about limits of knowledge ("Nobody really understands...")
- Uncertainty proclamations or certainty claims
- Reflection on reliability of predictions
- Meta-epistemic statements ("We know what we don't know")
- Claims to superior understanding

**Anchor Examples:**
1. "Nobody really understands what happens inside these models — we're flying blind."
2. "Anyone who claims to know when AGI arrives is fooling themselves or you."
3. "I've spent thirty years studying this — I think I have clearer picture than most."

---

### ET — Ethics/Values

**Definition:** Overarching value principles and moral convictions. What is right, wrong, good, bad? Ethical imperatives and normative foundations.

**Inclusion Criteria:**
- Moral imperatives ("We *must* ensure...")
- Value principles (fairness, justice, freedom, responsibility)
- Ethical evaluations of technology or actions
- Duty and responsibility attributions
- Fundamental normative positionings

**Anchor Examples:**
1. "We have obligation to ensure AI benefits everyone, not just privileged few."
2. "It would be morally wrong to halt progress that could save millions of lives."
3. "Most important value in AI development is transparency — without it, trust impossible."

---

### GE — Society

**Definition:** Non-economic societal questions. Statements about impacts on democracy, education, social structures, health, inequality (if non-economic), culture.

**Inclusion Criteria:**
- Impacts on democratic processes and institutions
- Education and knowledge society
- Social inequality and participation (non-economic)
- Cultural changes
- Health system and public infrastructure
- Power shifts at societal level (if not MA)

**Anchor Examples:**
1. "Wealth created by AI must be distributed more broadly — otherwise we'll see social upheaval."
2. "Education systems around world completely unprepared for what's coming."
3. "AI-generated misinformation will be greatest threat to democracy in next decade."

---

### RI — Risk/Safety

**Definition:** Danger assessment. Statements about existential risks, loss of control, misuse, safety problems, unintended consequences of AI systems.

**Inclusion Criteria:**
- Existential risks (x-risk) from AI
- Loss of control over AI systems (alignment problem)
- Misuse potential (weapons, surveillance, deepfakes)
- Safety technical concerns
- Unintended consequences and side effects
- Warnings about concrete dangers

**Anchor Examples:**
1. "Probability of existential risk from AI not zero — and even small probability demands serious attention."
2. "We don't yet have reliable methods to align superintelligent system with human values."
3. "Most dangerous scenario isn't rogue AI — it's AI in hands of bad actors."

---

### FO — Progress/Acceleration

**Definition:** Assessment of technological progress. Statements about pace, character, quality or disruption potential of technological development. Not overall narrative, but *evaluation* of progress.

**Inclusion Criteria:**
- Evaluation of development pace ("faster/slower than expected")
- Assessment of technological breakthroughs
- Disruption analyses
- Comparisons with earlier technological revolutions (if evaluative)
- AGI timeline predictions (primary FO, secondary ZP marker)

**Anchor Examples:**
1. "We are moving faster than anyone expected — GPT-4 was supposed be five years away."
2. "Pace of improvement in large language models genuinely unprecedented."
3. "I think AGI possible within decade, maybe even by 2027."

---

### MA — Power/Control

**Definition:** Power analysis. Who controls AI technology? Questions of centralization vs. decentralization, power concentration, access control, geopolitical power relations.

**Inclusion Criteria:**
- Power concentration among few actors
- Centralization vs. decentralization of AI systems
- Geopolitical power relations (USA vs. China etc.)
- Access and control mechanisms
- Open source as power question
- Influence of tech corporations on politics and society

**Anchor Examples:**
1. "Open source ensures no single entity controls AI — that's why it matters."
2. "Concentration of AI capabilities in three or four companies deeply concerning."
3. "Whoever controls AGI controls future. That's not hyperbole."

---

### AR — Work/Economy

**Definition:** Economic questions. Statements about labor market, business models, investments, economic productivity, economic disruption.

**Inclusion Criteria:**
- Labor market predictions (job loss, new professions, transformation)
- Business models and corporate strategies
- Investments and capital allocation
- Productivity gains and economic growth
- Economic inequality (income/wealth distribution)
- Commercialization of AI

**Anchor Examples:**
1. "Most jobs will be transformed within decade — some eliminated, many augmented, new ones created."
2. "Economic value of AGI would dwarf entire current global GDP."
3. "Investment flowing into AI right now unlike anything we've seen since dot-com era."

---

### TR — Transhumanism

**Definition:** Human transformation through technology. Statements about extension, overcoming or preservation of human. Enhancement, human-machine merger, post-humanism.

**Inclusion Criteria:**
- Brain-computer interfaces and cognitive extension
- Lifespan extension and biological optimization
- Human-machine merger (cyborg, upload)
- Post-human future visions
- Preservation arguments ("Human should remain as is")
- Statements about future of human body/mind

**Anchor Examples:**
1. "Brain-computer interfaces will extend human cognition beyond biological limits."
2. "Within our lifetimes, we may able upload consciousness to digital substrates."
3. "I believe humans should remain fundamentally biological — enhancement dangerous path."

---

### RE — Regulation

**Definition:** Concrete governance mechanisms. Laws, institutional proposals, regulatory frameworks, certification systems, international agreements.

**Inclusion Criteria:**
- Law proposals and regulatory frameworks
- Governance institution proposals
- Regulation and monitoring systems
- Certification requirements
- International agreements and treaties
- Patent and property regimes for AI

**Anchor Examples:**
1. "We need global AI governance framework that all nations respect."
2. "There should require AI systems undergo certification before deployment."
3. "International treaty should establish AI research standards."

---

### SP/EX — Spirituality/Existential

**Definition:** Existential and spiritual questions. Meaning, consciousness, transcendence, purpose. What is existential significance of technological development?

**Inclusion Criteria:**
- Consciousness and subjective experience questions
- Meaning and purpose in technological age
- Transcendence and spiritual dimensions
- Existential weight of AI development
- Profound philosophical questions about being

**Anchor Examples:**
1. "AI raises profound questions about consciousness and what it means to be."
2. "Perhaps meaning itself will be redefined in age of artificial intelligence."
3. "This technology touches something sacred about human existence."

---

## 3. Tonality Markers (Mandatory, Mutually Exclusive)

Exactly ONE marker per statement:

| Marker | Definition |
|--------|-----------|
| **OPT** | Overall optimistic or hopeful tone |
| **PES** | Overall pessimistic or fearful tone |
| **AMB** | Ambivalent, mixed or contradictory tone |

---

## 4. Mode Markers (Optional, Multiple Possible)

| Marker | Definition |
|--------|-----------|
| **POL** | Politically charged or politically connoted |
| **PHI** | Philosophically reflected or theoretical depth |
| **EMP** | Empirically grounded with data/evidence |
| **ANE** | Anecdotal or narrative-driven |
| **PRO** | Provocative, controversial, boundary-pushing |
| **HA** | Has direct reference to concrete action (statement-action link) |
| **STR** | Strategic framing or strategic communication |

---

## 5. Assignment Rules

- Each statement gets 1-2 primary categories (not zero, not more than 2)
- Exactly 1 tonality marker
- 0 or more mode markers
- Categories should be non-redundant (avoid coding same semantic content twice)
- If multiple categories equally appropriate, choose max 2 most specific
- Secondary codes (mode markers) should add nuance, not duplicate category meaning

---

## 6. Quality Assurance

- Check that category definitions fit anchor examples in this guide
- When uncertain, consult distinction section of category definition
- Document ambiguous cases for inter-coder reliability review
- Review statement multiple times before final assignment

---

*Coding Guide v1.0, 2026-02-12*
*For systematic coding of 1,738 statements using 13 primary categories + tonality + mode markers*
