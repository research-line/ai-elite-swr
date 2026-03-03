# What Does the AI Elite Think?

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18736737.svg)](https://doi.org/10.5281/zenodo.18736737)

An LLM-based worldview reconstruction of the 100 most influential AI leaders (2010--2026), using the Synthetic Worldview Reconstruction (SWR) method.

> **Was denkt die KI-Elite?** Eine LLM-gestuetzte Weltbild-Rekonstruktion der 100 einflussreichsten KI-Akteure (2010--2026).

## Overview

This repository contains the data collection pipeline, analysis scripts, and preprint for a study that reconstructs the latent worldviews of 100 top AI actors (Altman, Hassabis, Musk, Zuckerberg, et al.) across 12 semantic dimensions -- from *Transhumanism* and *Accelerationism* to *Safetyism* and *Spirituality*.

### Method: Synthetic Worldview Reconstruction (SWR)

The SWR method uses LLMs as analytical instruments to systematically process publicly available statements into coherent worldview profiles. Each actor is rated on 12 dimensions (1--10 scale), enabling quantitative comparison across the full sample.

The methodological foundation is described in a companion paper:

> **Geiger, L.** (2026). *Synthetic Worldview Reconstruction (SWR): An LLM-Based Method for Systematic Worldview Analysis.* Zenodo. [https://doi.org/10.5281/zenodo.18736720](https://doi.org/10.5281/zenodo.18736720)

### Key Findings

- **4 actor clusters**: Architects (n=35), Guardians (n=25), Liberators (n=22), Accelerationists (n=18)
- **12 semantic dimensions**: Transhumanism, AI Autonomy, Safety Orientation, Acceleration Pressure, Regulation Preference, Power Concentration, Economic Disruption, Urgency, Anthropocentrism, Spirituality, Gender Equity, Techno-Optimism
- **7 visualizations**: Temporal trends, heatmaps, radar charts, correlation matrices, cluster comparisons
- **Temporal analysis**: Systematic tracking of worldview shifts across 2010--2026

## Scientific Papers

The preprint is available in English, German, and a combined bilingual edition:

- [`paper/KI_Elite_v2_en.pdf`](paper/KI_Elite_v2_en.pdf) -- English
- [`paper/KI_Elite_v2_ger.pdf`](paper/KI_Elite_v2_ger.pdf) -- German
- [`paper/KI_Elite_v2_kombi.pdf`](paper/KI_Elite_v2_kombi.pdf) -- Bilingual (DE+EN)

## Project Structure

```
paper/                          # Preprint (EN + DE + Kombi, .tex + .pdf)
_data/                          # Data collection & analysis pipeline
  create_db.py                  # SQLite database schema (6 tables, 4 views)
  update_db_v2.py               # Schema migration (v1 -> v2)
  collect_*.py                  # 56 data collection scripts (one per actor)
  insert_*.py                   # 29 additional actor insertion scripts
  kodierung_*.py                # 12 qualitative coding scripts (P01-P100)
  extract_blinded.py            # Blinded data extraction for validation
  generate_topf.py              # Synthesis unit ("Topf") generation
  fix_tonalitaet.py             # Tonality correction
  kodierung_nachtrag.py         # Supplementary coding
  visualisierungen.py           # Figure generation (fig1-fig7)
  zeitreihen_analyse.py         # Temporal trend analysis
_results/                       # Analysis outputs
  figures/                      # 7 figures (PNG + SVG)
  toepfe/                       # Synthesis units by group/time period
  synthesen/                    # Individual and collective worldview syntheses
  Phase*.md                     # Analysis phase documentation
  Codier_Leitfaden.md           # Coding manual
  Forschungsdesign_*.md         # Research design documentation
README.md
LICENSE                         # CC-BY 4.0
```

## Reproducibility

### Database Setup

The SQLite database schema can be recreated from the provided scripts:

```bash
cd _data
python create_db.py             # Creates aussagen_top100.db with schema + master data
python update_db_v2.py          # Applies v2 schema migration
```

### Data Collection

Each `collect_*.py` and `insert_*.py` script populates the database with statements from one AI actor. Scripts contain the collected statements as structured data.

```bash
python collect_altman.py        # Example: Sam Altman (767 lines, ~50 statements)
python collect_hassabis.py      # Example: Demis Hassabis
# ... (85 actor scripts total)
```

### Analysis Pipeline

```bash
python kodierung_P01-P10.py     # Qualitative coding (12 dimensions, 1-10 scale)
# ... (10 coding batches, P01-P100)
python generate_topf.py         # Generate synthesis units
python visualisierungen.py      # Generate figures (fig1-fig7)
python zeitreihen_analyse.py    # Temporal trend analysis
```

## The 12 Semantic Dimensions

| Code | Dimension | Poles (1 = low, 10 = high) |
|------|-----------|---------------------------|
| D01 | Transhumanism | Human-centric -- Post-human |
| D02 | AI Autonomy | Tool -- Agent |
| D03 | Safety Orientation | Move fast -- Safety first |
| D04 | Acceleration Pressure | Gradual -- Full speed |
| D05 | Regulation Preference | Deregulate -- Regulate |
| D06 | Power Concentration | Democratize -- Concentrate |
| D07 | Economic Disruption | Continuity -- Disruption |
| D08 | Urgency | Long-term -- Immediate |
| D09 | Anthropocentrism | Replaceable -- Unique |
| D10 | Spirituality | Materialist -- Spiritual |
| D11 | Gender Equity | Status quo -- Equity-oriented |
| D12 | Techno-Optimism | Skeptical -- Optimistic |

## The 100 AI Actors

The sample includes CEOs, founders, researchers, investors, and policymakers from the global AI ecosystem. Selection criteria and the full ranked list are documented in the paper (Section 3).

Top 10: Jensen Huang, Sam Altman, Elon Musk, Sundar Pichai, Mark Zuckerberg, Larry Page, Larry Ellison, Sergey Brin, Dario Amodei, Jeff Bezos.

## Citation

If you use this data or methodology in your research, please cite:

```bibtex
@article{geiger2026aielite,
  title={What Does the AI Elite Think? An LLM-Based Worldview Reconstruction
         of 100 Key AI Leaders (2010--2026)},
  author={Geiger, Lukas},
  year={2026},
  doi={10.5281/zenodo.18736737},
  publisher={Zenodo}
}
```

## Companion Paper

The SWR method used in this study is described in detail in:

> **Geiger, L.** (2026). *Synthetic Worldview Reconstruction (SWR).* Zenodo. DOI: [10.5281/zenodo.18736720](https://doi.org/10.5281/zenodo.18736720)

## License

CC-BY 4.0. See [LICENSE](LICENSE) for details.

## Author

**Lukas Geiger** -- Independent Researcher, Bernau im Schwarzwald, Germany

*AI-assisted development: Claude Opus 4.6 (Anthropic), Gemini (Google DeepMind)*
