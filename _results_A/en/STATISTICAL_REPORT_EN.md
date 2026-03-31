# Statistical Analysis: SWR/AI-Elite Worldview Data

**Date:** 2026-03-27
**Data basis:** 100 persons x 12 dimensions (D01-D12, scale 1-10)
**Methods:** PCA, HDBSCAN, Cliff's delta, Kruskal-Wallis, Mann-Whitney U

---

## 1. PCA (Dimension Reduction)

**Components for 80% explained variance:** 5

### Scree-Plot Data

| Component | Eigenvalue | Expl. Variance | Cumulative |
|------------|-----------|----------------|-----------|
| PC1 | 4.343 | 35.8% | 35.8% |
| PC2 | 2.322 | 19.2% | 55.0% |
| PC3 | 1.481 | 12.2% | 67.2% |
| PC4 | 1.089 | 9.0% | 76.2% |
| PC5 | 0.816 | 6.7% | 82.9% |
| PC6 | 0.552 | 4.6% | 87.5% |
| PC7 | 0.450 | 3.7% | 91.2% |
| PC8 | 0.354 | 2.9% | 94.1% |
| PC9 | 0.260 | 2.1% | 96.2% |
| PC10 | 0.201 | 1.7% | 97.9% |
| PC11 | 0.166 | 1.4% | 99.3% |
| PC12 | 0.087 | 0.7% | 100.0% |

### PC1 Loadings (General Worldview Intensity Factor)

| Dimension | Loading | Label |
|-----------|--------|-------|
| D02 | +0.4003 | Control Belief |
| D05 | +0.3871 | Technology Determinism |
| D09 | -0.3861 | Human Uniqueness |
| D10 | +0.3338 | Transhumanism |
| D06 | +0.3065 | Progress Optimism |
| D12 | +0.3013 | Future of Humanity |
| D11 | -0.2743 | Egalitarianism |
| D07 | +0.2410 | Power Concentration |
| D08 | +0.2035 | Urgency |
| D01 | +0.1968 | Sense of Mission |
| D04 | -0.1752 | Responsibility Feeling |
| D03 | -0.0226 | Belonging Feeling |

**Interpretation PC1:** The strongest loadings show which dimensions contribute most to overall variation.

### PC2 Loadings (Differentiation Axis)

| Dimension | Loading | Label |
|-----------|--------|-------|
| D01 | +0.5065 | Sense of Mission |
| D04 | +0.5025 | Responsibility Feeling |
| D08 | +0.5017 | Urgency |
| D12 | -0.2417 | Future of Humanity |
| D10 | +0.2273 | Transhumanism |
| D03 | +0.2202 | Belonging Feeling |
| D06 | -0.2195 | Progress Optimism |
| D11 | +0.1140 | Egalitarianism |
| D02 | -0.1001 | Control Belief |
| D05 | +0.0949 | Technology Determinism |
| D09 | +0.0221 | Human Uniqueness |
| D07 | -0.0060 | Power Concentration |

## 2. Subspace Clustering (HDBSCAN)

### 2a. HDBSCAN on D07+D11 (Primary Differentiation Dimensions)

| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |
|-----------------|-------------|---------|-------|--------|------------|
| 5 | 2 | 9 | 12 | 12.0% | 0.567 |
| 5 | 3 | 8 | 19 | 19.0% | 0.537 |
| 5 | 5 | 8 | 23 | 23.0% | 0.501 |
| 8 | 2 | 6 | 17 | 17.0% | 0.443 |
| 8 | 3 | 6 | 24 | 24.0% | 0.417 |
| 8 | 5 | 5 | 30 | 30.0% | 0.330 |
| 10 | 2 | 5 | 26 | 26.0% | 0.378 |
| 10 | 3 | 5 | 32 | 32.0% | 0.346 |
| 10 | 5 | 3 | 26 | 26.0% | 0.245 |
| 12 | 2 | 5 | 26 | 26.0% | 0.378 |
| 12 | 3 | 4 | 43 | 43.0% | 0.236 |
| 12 | 5 | 3 | 26 | 26.0% | 0.245 |
| 15 | 2 | 4 | 18 | 18.0% | 0.310 |
| 15 | 3 | 2 | 19 | 19.0% | 0.316 |
| 15 | 5 | 3 | 26 | 26.0% | 0.245 |

### 2b. HDBSCAN on PC1+PC2+PC3

| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |
|-----------------|-------------|---------|-------|--------|------------|
| 5 | 3 | 2 | 56 | 56.0% | -0.081 |
| 5 | 5 | 2 | 54 | 54.0% | -0.088 |
| 8 | 3 | 2 | 84 | 84.0% | -0.212 |
| 8 | 5 | 0 | 100 | 100.0% | N/A |
| 10 | 3 | 0 | 100 | 100.0% | N/A |
| 10 | 5 | 0 | 100 | 100.0% | N/A |
| 15 | 3 | 0 | 100 | 100.0% | N/A |
| 15 | 5 | 0 | 100 | 100.0% | N/A |

### 2c. HDBSCAN on Top-3 PC1 Dimensions (D02+D05+D09)

| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |
|-----------------|-------------|---------|-------|--------|------------|
| 5 | 3 | 11 | 11 | 11.0% | 0.550 |
| 5 | 5 | 9 | 13 | 13.0% | 0.422 |
| 8 | 3 | 8 | 9 | 9.0% | 0.400 |
| 8 | 5 | 8 | 9 | 9.0% | 0.405 |
| 10 | 3 | 4 | 36 | 36.0% | 0.151 |
| 10 | 5 | 4 | 25 | 25.0% | 0.206 |
| 15 | 3 | 3 | 27 | 27.0% | 0.131 |
| 15 | 5 | 3 | 25 | 25.0% | 0.153 |

**Finding:** HDBSCAN consistently finds few or no dense clusters on the 100x12 data. This indicates a homogeneous, continuous distribution — the AI elite does not form clearly separated cluster patterns, but rather a spectrum. The heuristic types (Architect/Guardian/Innovator/Liberator) are therefore to be understood as ideal types in the Weberian sense, not as natural clusters.

## 3. Heuristic Cluster Analysis (Top-Down)

### Cluster Distribution

| Cluster | n | Share |
|---------|---|-------|
| Architect | 16 | 16% |
| Guardian | 11 | 11% |
| Innovator | 46 | 46% |
| Liberator | 27 | 27% |

### Cluster Profiles (Mean Values)

| Dimension | Architect | Guardian | Innovator | Liberator |
|-----------|------|------|------|------|
| D01 Sense of Mission | 6.6 | 6.1 | 6.2 | 6.1 |
| D02 Control Belief | 8.1 | 6.5 | 7.7 | 7.0 |
| D03 Belonging Feeling | 6.2 | 6.5 | 6.1 | 6.0 |
| D04 Responsibility Feeling | 6.0 | 6.9 | 6.3 | 7.0 |
| D05 Technology Determinism | 8.0 | 7.0 | 8.0 | 7.4 |
| D06 Progress Optimism | 7.3 | 5.6 | 7.9 | 7.5 |
| D07 Power Concentration | 5.9 | 3.8 | 4.8 | 3.6 |
| D08 Urgency | 8.3 | 7.7 | 8.1 | 7.5 |
| D09 Human Uniqueness | 4.6 | 5.8 | 4.7 | 5.4 |
| D10 Transhumanism | 5.6 | 4.6 | 5.5 | 5.2 |
| D11 Egalitarianism | 3.9 | 5.9 | 5.3 | 7.3 |
| D12 Future of Humanity | 7.1 | 6.1 | 7.7 | 7.2 |

## 4. Effect Sizes (Cliff's delta) -- Heuristic Clusters

Interpretation: |d| < 0.147 negligible, < 0.33 small, < 0.474 medium, >= 0.474 large

### Architect vs Guardian

| Dimension | delta | Interpretation | Mean Architect | Mean Guardian |
|-----------|-------|----------------|-----------|-----------|
| D07 (Power Concentration) | +1.000 | large | 5.9 | 3.8 |
| D02 (Control Belief) | +0.727 | large | 8.1 | 6.5 |
| D06 (Progress Optimism) | +0.688 | large | 7.3 | 5.6 |
| D11 (Egalitarianism) | -0.682 | large | 3.9 | 5.9 |
| D09 (Human Uniqueness) | -0.534 | large | 4.6 | 5.8 |
| D04 (Responsibility Feeling) | -0.455 | medium | 6.0 | 6.9 |
| D12 (Future of Humanity) | +0.443 | medium | 7.1 | 6.1 |
| D05 (Technology Determinism) | +0.426 | medium | 8.0 | 7.0 |

### Architect vs Innovator

| Dimension | delta | Interpretation | Mean Architect | Mean Innovator |
|-----------|-------|----------------|-----------|-----------|
| D07 (Power Concentration) | +0.682 | large | 5.9 | 4.8 |
| D11 (Egalitarianism) | -0.591 | large | 3.9 | 5.3 |
| D12 (Future of Humanity) | -0.352 | medium | 7.1 | 7.7 |
| D06 (Progress Optimism) | -0.337 | medium | 7.3 | 7.9 |

### Architect vs Liberator

| Dimension | delta | Interpretation | Mean Architect | Mean Liberator |
|-----------|-------|----------------|-----------|-----------|
| D07 (Power Concentration) | +1.000 | large | 5.9 | 3.6 |
| D11 (Egalitarianism) | -0.982 | large | 3.9 | 7.3 |
| D02 (Control Belief) | +0.759 | large | 8.1 | 7.0 |
| D04 (Responsibility Feeling) | -0.530 | large | 6.0 | 7.0 |
| D09 (Human Uniqueness) | -0.528 | large | 4.6 | 5.4 |
| D08 (Urgency) | +0.419 | medium | 8.3 | 7.5 |
| D05 (Technology Determinism) | +0.354 | medium | 8.0 | 7.4 |

### Guardian vs Innovator

| Dimension | delta | Interpretation | Mean Guardian | Mean Innovator |
|-----------|-------|----------------|-----------|-----------|
| D06 (Progress Optimism) | -0.889 | large | 5.6 | 7.9 |
| D07 (Power Concentration) | -0.761 | large | 3.8 | 4.8 |
| D12 (Future of Humanity) | -0.646 | large | 6.1 | 7.7 |
| D02 (Control Belief) | -0.609 | large | 6.5 | 7.7 |
| D09 (Human Uniqueness) | +0.466 | medium | 5.8 | 4.7 |
| D05 (Technology Determinism) | -0.413 | medium | 7.0 | 8.0 |

### Guardian vs Liberator

| Dimension | delta | Interpretation | Mean Guardian | Mean Liberator |
|-----------|-------|----------------|-----------|-----------|
| D06 (Progress Optimism) | -0.865 | large | 5.6 | 7.5 |
| D11 (Egalitarianism) | -0.539 | large | 5.9 | 7.3 |
| D12 (Future of Humanity) | -0.539 | large | 6.1 | 7.2 |

### Innovator vs Liberator

| Dimension | delta | Interpretation | Mean Innovator | Mean Liberator |
|-----------|-------|----------------|-----------|-----------|
| D07 (Power Concentration) | +0.791 | large | 4.8 | 3.6 |
| D11 (Egalitarianism) | -0.786 | large | 5.3 | 7.3 |
| D02 (Control Belief) | +0.554 | large | 7.7 | 7.0 |
| D09 (Human Uniqueness) | -0.447 | medium | 4.7 | 5.4 |
| D05 (Technology Determinism) | +0.353 | medium | 8.0 | 7.4 |

### Strongest Differentiation Dimensions (across all cluster pairs)

| Rank | Dimension | Medium+ Effects | Max |delta| |
|------|-----------|----------------|-------------|
| 1 | D07 (Power Concentration) | 5x | 1.000 |
| 2 | D11 (Egalitarianism) | 5x | 0.982 |
| 3 | D06 (Progress Optimism) | 4x | 0.889 |
| 4 | D02 (Control Belief) | 4x | 0.759 |
| 5 | D12 (Future of Humanity) | 4x | 0.646 |
| 6 | D09 (Human Uniqueness) | 4x | 0.534 |
| 7 | D05 (Technology Determinism) | 4x | 0.426 |
| 8 | D04 (Responsibility Feeling) | 2x | 0.530 |
| 9 | D08 (Urgency) | 1x | 0.419 |

## 5. Role Comparisons (Cliff's delta)

Role distribution: CEO n=33, Academic n=10, Investor n=13, Founder n=44

### CEO vs Academic

| Dimension | delta | Interpretation | Mean CEO | Mean Academic |
|-----------|-------|----------------|-----------|-----------|
| D02 (Control Belief) | +0.788 | large | 7.7 | 6.2 |
| D06 (Progress Optimism) | +0.582 | large | 7.7 | 6.1 |
| D12 (Future of Humanity) | +0.554 | large | 7.5 | 6.1 |
| D07 (Power Concentration) | +0.542 | large | 4.9 | 4.0 |
| D05 (Technology Determinism) | +0.518 | large | 7.9 | 6.8 |
| D10 (Transhumanism) | +0.509 | large | 5.6 | 4.2 |
| D11 (Egalitarianism) | -0.473 | medium | 5.7 | 7.1 |
| D09 (Human Uniqueness) | -0.470 | medium | 5.0 | 6.1 |
| D08 (Urgency) | +0.412 | medium | 8.2 | 7.1 |

### Academic vs Investor

| Dimension | delta | Interpretation | Mean Academic | Mean Investor |
|-----------|-------|----------------|-----------|-----------|
| D02 (Control Belief) | -0.877 | large | 6.2 | 8.0 |
| D12 (Future of Humanity) | -0.708 | large | 6.1 | 8.1 |
| D09 (Human Uniqueness) | +0.677 | large | 6.1 | 4.4 |
| D06 (Progress Optimism) | -0.638 | large | 6.1 | 8.0 |
| D04 (Responsibility Feeling) | +0.631 | large | 7.4 | 6.0 |
| D05 (Technology Determinism) | -0.631 | large | 6.8 | 8.1 |
| D11 (Egalitarianism) | +0.600 | large | 7.1 | 4.7 |
| D10 (Transhumanism) | -0.569 | large | 4.2 | 5.7 |
| D01 (Sense of Mission) | -0.423 | medium | 5.8 | 6.5 |

### Academic vs Founder

| Dimension | delta | Interpretation | Mean Academic | Mean Founder |
|-----------|-------|----------------|-----------|-----------|
| D02 (Control Belief) | -0.700 | large | 6.2 | 7.4 |
| D11 (Egalitarianism) | +0.580 | large | 7.1 | 5.7 |
| D06 (Progress Optimism) | -0.523 | large | 6.1 | 7.4 |
| D09 (Human Uniqueness) | +0.509 | large | 6.1 | 4.9 |
| D12 (Future of Humanity) | -0.493 | large | 6.1 | 7.2 |
| D10 (Transhumanism) | -0.484 | large | 4.2 | 5.3 |
| D04 (Responsibility Feeling) | +0.477 | large | 7.4 | 6.3 |
| D05 (Technology Determinism) | -0.448 | medium | 6.8 | 7.7 |
| D07 (Power Concentration) | -0.373 | medium | 4.0 | 4.5 |
| D08 (Urgency) | -0.357 | medium | 7.1 | 8.0 |

### Investor vs Founder

| Dimension | delta | Interpretation | Mean Investor | Mean Founder |
|-----------|-------|----------------|-----------|-----------|
| D02 (Control Belief) | +0.390 | medium | 8.0 | 7.4 |
| D12 (Future of Humanity) | +0.381 | medium | 8.1 | 7.2 |
| D01 (Sense of Mission) | +0.337 | medium | 6.5 | 5.9 |

## 6. Gender Comparison

Women n=14, Men n=86

### Cliff's delta

| Dimension | delta | Interpretation | Mean Women | Mean Men |
|-----------|-------|----------------|-------------|--------------|
| D01 (Sense of Mission) | -0.171 | small | 5.9 | 6.3 |
| D02 (Control Belief) | -0.379 | medium | 6.9 | 7.5 |
| D04 (Responsibility Feeling) | +0.345 | medium | 7.1 | 6.4 |
| D05 (Technology Determinism) | -0.499 | large | 7.0 | 7.8 |
| D07 (Power Concentration) | -0.168 | small | 4.3 | 4.6 |
| D08 (Urgency) | -0.392 | medium | 7.1 | 8.0 |
| D09 (Human Uniqueness) | +0.588 | large | 5.9 | 4.8 |
| D10 (Transhumanism) | -0.383 | medium | 4.7 | 5.4 |
| D11 (Egalitarianism) | +0.455 | medium | 6.9 | 5.5 |

## 7. Kruskal-Wallis H-Test (4 heuristic clusters)

| Dimension | H | p-value | Significant? |
|-----------|---|--------|--------------|
| D01 (Sense of Mission) | 2.59 | 0.4592 | n.s. |
| D02 (Control Belief) | 33.55 | 0.0000 | *** |
| D03 (Belonging Feeling) | 3.75 | 0.2901 | n.s. |
| D04 (Responsibility Feeling) | 10.76 | 0.0131 | * |
| D05 (Technology Determinism) | 11.21 | 0.0106 | * |
| D06 (Progress Optimism) | 29.55 | 0.0000 | *** |
| D07 (Power Concentration) | 64.76 | 0.0000 | *** |
| D08 (Urgency) | 6.25 | 0.0999 | n.s. |
| D09 (Human Uniqueness) | 17.50 | 0.0006 | *** |
| D10 (Transhumanism) | 4.04 | 0.2567 | n.s. |
| D11 (Egalitarianism) | 49.57 | 0.0000 | *** |
| D12 (Future of Humanity) | 17.93 | 0.0005 | *** |

## 8. Descriptive Statistics (Dispersion)

Sorted by standard deviation (descending):

| Rank | Dimension | Mean | SD | IQR | Range | Min | Max | Skewness | Kurtosis |
|------|-----------|------|-----|-----|-------|-----|-----|---------|----------|
| 1 | D11 (Egalitarianism) | 5.72 | 1.670 | 2.0 | 7 | 2 | 9 | -0.22 | -0.57 |
| 2 | D04 (Responsibility Feeling) | 6.54 | 1.251 | 1.0 | 5 | 4 | 9 | +0.14 | -0.54 |
| 3 | D08 (Urgency) | 7.91 | 1.232 | 2.0 | 5 | 5 | 10 | -0.09 | -0.79 |
| 4 | D10 (Transhumanism) | 5.32 | 1.162 | 1.0 | 7 | 2 | 9 | +0.64 | +1.53 |
| 5 | D01 (Sense of Mission) | 6.21 | 1.149 | 2.0 | 6 | 4 | 10 | +0.43 | +0.16 |
| 6 | D06 (Progress Optimism) | 7.46 | 1.114 | 1.0 | 6 | 4 | 10 | -0.58 | +0.96 |
| 7 | D12 (Future of Humanity) | 7.29 | 1.113 | 1.0 | 6 | 4 | 10 | -0.06 | +0.39 |
| 8 | D09 (Human Uniqueness) | 4.98 | 1.063 | 2.0 | 5 | 3 | 8 | +0.39 | +0.12 |
| 9 | D07 (Power Concentration) | 4.57 | 1.037 | 1.0 | 5 | 2 | 7 | +0.22 | +0.26 |
| 10 | D05 (Technology Determinism) | 7.72 | 0.900 | 1.0 | 4 | 5 | 9 | -0.51 | +0.31 |
| 11 | D02 (Control Belief) | 7.45 | 0.892 | 1.0 | 5 | 4 | 9 | -0.49 | +1.08 |
| 12 | D03 (Belonging Feeling) | 6.12 | 0.742 | 1.0 | 3 | 5 | 8 | -0.04 | -0.84 |

**Greatest dispersion:** D11 (Egalitarianism) with SD=1.670
**Smallest dispersion:** D03 (Belonging Feeling) with SD=0.742

## 9. Summary of Core Findings

### PCA
- 5 principal components explain 80% of total variance
- PC1 (35.8% variance) loads strongest on: D02 (Control Belief), D05 (Technology Determinism), D09 (Human Uniqueness)
- PC2 (19.2% variance) differentiates primarily via: D01 (Sense of Mission), D04 (Responsibility Feeling)

### Clustering
- HDBSCAN finds NO robust natural clusters — the AI elite form a continuum
- Heuristic types (Architect/Guardian/Innovator/Liberator) are to be interpreted as ideal types, not discrete groups

### Effect Sizes
- Significant Kruskal-Wallis differences (p<0.05) on: D02, D04, D05, D06, D07, D09, D11, D12
- Strongest differentiation dimension: D07 (Power Concentration) with 5x medium+ Cliff's delta

### Dispersion
- Most heterogeneous dimension: D11 (Egalitarianism) — worldviews diverge most here
- Most homogeneous dimension: D03 (Belonging Feeling) — relative consensus here

---

*Generated: 2026-03-27 | Method: PCA + HDBSCAN + Cliff's delta + Kruskal-Wallis + Mann-Whitney U*
*Data basis: rating_GESAMT_D01-D12.md (100 persons x 12 dimensions)*
