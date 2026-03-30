# Synthetic Worldview Reconstruction (SWR) — Applied to the AI Elite

[![DOI Paper A](https://zenodo.org/badge/DOI/10.5281/zenodo.18736737.svg)](https://doi.org/10.5281/zenodo.18736737)
[![DOI Paper B](https://zenodo.org/badge/DOI/10.5281/zenodo.18736720.svg)](https://doi.org/10.5281/zenodo.18736720)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## What is this?

This repository contains two companion papers:

- **Paper A (AI Elite):** *What Does the AI Elite Think?* — An application study that reconstructs and compares the collective worldviews of 15 sociologically defined groups within the 100 most influential AI actors (2010–2026).
- **Paper B (SWR):** *Synthetic Worldview Reconstruction* — A methods paper that describes the general method used in Paper A: using LLMs' synthetic integration capability to derive collective worldviews for societal groups.

**Paper A applies the method. Paper B describes it.**

## The Core Idea

SWR exploits a specific capability of Large Language Models: their ability to compose heterogeneous textual fragments into coherent wholes. When you feed an LLM the aggregated public statements and documented actions of a sociological group's members, it can synthesize the group's *collective worldview* — a latent belief system that has never been explicitly articulated anywhere.

This works better at the **group level** than at the individual level, because:
- A group's collective worldview doesn't exist in any training corpus (reduced contamination risk)
- The method creates something genuinely new rather than potentially reproducing stored knowledge
- Inter-group comparison — the method's primary analytical tool — reveals structural differences in how groups see the world

## Key Findings (Paper A)

| Finding | Detail |
|---------|--------|
| **Collective worldview** | Technological messianism with ambivalence (avg. 7.1/10) |
| **Temporal shift** | Utopian certainty eroding; tragic acceleration compulsion |
| **Say-do gap** | Systematic: egalitarianism Δ = −3 (say equality, act elite) |
| **4 worldview types** | Architect, Guardian, Innovator, Liberator (Weberian ideal types) |
| **Power paradox** | Most extreme worldviews control the most resources |

## Validation Status

| Test | Result |
|------|--------|
| Run convergence (test-retest) | ICC = 0.902 (excellent) |
| Cross-modal prediction | 88% of statement-based predictions confirmed by real actions |
| Expected-discrepancy control | No artifactual say-do gap (control MAE = 0.50 vs. real 1.25) |
| Aggregation-synthesis comparison | r = 0.623 with systematic amplification effect |
| PCA | 5 components, 80% variance explained |
| HDBSCAN | No natural clusters (confirms Weberian ideal types) |
| Kruskal-Wallis | 6/12 dimensions p < .001 across types |

## Repository Structure

```
paper_A/            AI Elite papers (EN + DE, .tex + .pdf)
paper_B/            SWR method papers (EN + DE, .tex + .pdf)
_data/              Data collection pipeline
  85 actor-specific collect/insert scripts
  generate_topf.py  — Synthesis unit generator
  extract_blinded.py — Focus control (blinding) script
  create_db.py      — Database schema
_results_A/         Analysis outputs for Paper A
  figures/          7 figures (PNG + SVG)
  toepfe/           54 synthesis units (blinded data corpora)
  synthesen/        Group syntheses + ratings
  G5_BERICHT.md     — Cross-modal prediction results
  G8_BERICHT.md     — Aggregation comparison results
  *.json            — Statistical analysis outputs
```

## Data

- **3,132 data points** (1,738 statements + 1,394 actions)
- **100 AI actors**, organized into **15 sociological groups**
- Time period: 2010–2026
- Storage: SQLite database (rebuild with `create_db.py` + insert scripts)

## How to Reproduce

```bash
# 1. Rebuild database
cd _data && python create_db.py

# 2. Run insert scripts (requires the collect scripts to have run first)
python insert_*.py

# 3. Generate synthesis units
python generate_topf.py --all

# 4. Compile papers
cd ../paper_A && pdflatex KI_Elite_v2_en.tex && pdflatex KI_Elite_v2_en.tex
cd ../paper_B && pdflatex SWR_v2_en.tex && pdflatex SWR_v2_en.tex
```

## Citation

```bibtex
@article{Geiger2026Elite,
  author  = {Geiger, Lukas},
  title   = {What Does the {AI} Elite Think? {A} Synthetic Worldview Reconstruction of the 100 Most Influential {AI} Actors (2010--2026)},
  year    = {2026},
  doi     = {10.5281/zenodo.18736737},
  note    = {Preprint}
}

@article{Geiger2026SWR,
  author  = {Geiger, Lukas},
  title   = {Synthetic Worldview Reconstruction: An {LLM}-Supported Method for Analyzing Latent Collective Belief Systems},
  year    = {2026},
  doi     = {10.5281/zenodo.18736720},
  note    = {Preprint}
}
```

## Author

**Lukas Geiger** — Independent Researcher, Bernau im Schwarzwald
ORCID: [0009-0005-7296-1534](https://orcid.org/0009-0005-7296-1534)

## AI Disclosure (Level 5 — Extensive)

Claude Sonnet 4.5 (Anthropic): All 100 individual-level dimensional ratings.
Claude Opus 4.6 (Anthropic): Group-level syntheses, statistical analyses, validation experiments, manuscript support.
Research design, research questions, methodological decisions, interpretation, and all substantive conclusions originate from the author.

## License

CC-BY 4.0
