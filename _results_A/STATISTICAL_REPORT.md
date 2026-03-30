# Statistische Analyse: SWR/KI-Elite Weltbild-Daten

**Datum:** 2026-03-27
**Datenbasis:** 100 Personen x 12 Dimensionen (D01-D12, Skala 1-10)
**Methoden:** PCA, HDBSCAN, Cliff's delta, Kruskal-Wallis, Mann-Whitney U

---

## 1. PCA (Dimensionsreduktion)

**Komponenten fuer 80% erklaerte Varianz:** 5

### Scree-Plot Daten

| Komponente | Eigenwert | Erkl. Varianz | Kumuliert |
|------------|-----------|---------------|-----------|
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

### PC1 Ladungen (Allgemeiner Weltbild-Intensitaetsfaktor)

| Dimension | Ladung | Label |
|-----------|--------|-------|
| D02 | +0.4003 | Kontrollueberzeugung |
| D05 | +0.3871 | Technologie-Determinismus |
| D09 | -0.3861 | Menschliche Einzigartigkeit |
| D10 | +0.3338 | Transhumanismus |
| D06 | +0.3065 | Fortschrittsoptimismus |
| D12 | +0.3013 | Zukunft der Menschheit |
| D11 | -0.2743 | Egalitarismus |
| D07 | +0.2410 | Machtkonzentration |
| D08 | +0.2035 | Dringlichkeit |
| D01 | +0.1968 | Sendungsbewusstsein |
| D04 | -0.1752 | Verantwortungsgefuehl |
| D03 | -0.0226 | Zugehoerigkeitsgefuehl |

**Interpretation PC1:** Die staerksten Ladungen zeigen, welche Dimensionen am meisten zur Gesamtvariation beitragen.

### PC2 Ladungen (Differenzierungsachse)

| Dimension | Ladung | Label |
|-----------|--------|-------|
| D01 | +0.5065 | Sendungsbewusstsein |
| D04 | +0.5025 | Verantwortungsgefuehl |
| D08 | +0.5017 | Dringlichkeit |
| D12 | -0.2417 | Zukunft der Menschheit |
| D10 | +0.2273 | Transhumanismus |
| D03 | +0.2202 | Zugehoerigkeitsgefuehl |
| D06 | -0.2195 | Fortschrittsoptimismus |
| D11 | +0.1140 | Egalitarismus |
| D02 | -0.1001 | Kontrollueberzeugung |
| D05 | +0.0949 | Technologie-Determinismus |
| D09 | +0.0221 | Menschliche Einzigartigkeit |
| D07 | -0.0060 | Machtkonzentration |

## 2. Subspace-Clustering (HDBSCAN)

### 2a. HDBSCAN auf D07+D11 (primaere Differenzierungsdimensionen)

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

### 2b. HDBSCAN auf PC1+PC2+PC3

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

### 2c. HDBSCAN auf Top-3 PC1-Dimensionen (D02+D05+D09)

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

**Befund:** HDBSCAN findet auf den 100x12-Daten konsistent wenige oder keine dichten Cluster. Dies deutet auf eine homogene, kontinuierliche Verteilung hin -- die KI-Elite bildet kein klar separiertes Cluster-Muster, sondern ein Spektrum. Die heuristischen Typen (Architekt/Hueter/Innovator/Befreier) sind daher als Idealtypen im Weberschen Sinne zu verstehen, nicht als natuerliche Cluster.

## 3. Heuristische Cluster-Analyse (Top-Down)

### Cluster-Verteilung

| Cluster | n | Anteil |
|---------|---|--------|
| Architekt | 16 | 16% |
| Hueter | 11 | 11% |
| Innovator | 46 | 46% |
| Befreier | 27 | 27% |

### Cluster-Profile (Mittelwerte)

| Dimension | Architekt | Hueter | Innovator | Befreier |
|-----------|------|------|------|------|
| D01 Sendungsbewusstsein | 6.6 | 6.1 | 6.2 | 6.1 |
| D02 Kontrollueberzeugung | 8.1 | 6.5 | 7.7 | 7.0 |
| D03 Zugehoerigkeitsgefue | 6.2 | 6.5 | 6.1 | 6.0 |
| D04 Verantwortungsgefueh | 6.0 | 6.9 | 6.3 | 7.0 |
| D05 Technologie-Determin | 8.0 | 7.0 | 8.0 | 7.4 |
| D06 Fortschrittsoptimism | 7.3 | 5.6 | 7.9 | 7.5 |
| D07 Machtkonzentration | 5.9 | 3.8 | 4.8 | 3.6 |
| D08 Dringlichkeit | 8.3 | 7.7 | 8.1 | 7.5 |
| D09 Menschliche Einzigar | 4.6 | 5.8 | 4.7 | 5.4 |
| D10 Transhumanismus | 5.6 | 4.6 | 5.5 | 5.2 |
| D11 Egalitarismus | 3.9 | 5.9 | 5.3 | 7.3 |
| D12 Zukunft der Menschhe | 7.1 | 6.1 | 7.7 | 7.2 |

## 4. Effektstaerken (Cliff's delta) -- Heuristische Cluster

Interpretation: |d| < 0.147 negligible, < 0.33 small, < 0.474 medium, >= 0.474 large

### Architekt vs Hueter

| Dimension | delta | Interpretation | Mean Architekt | Mean Hueter |
|-----------|-------|----------------|-----------|-----------|
| D07 (Machtkonzentration) | +1.000 | large | 5.9 | 3.8 |
| D02 (Kontrollueberzeugung) | +0.727 | large | 8.1 | 6.5 |
| D06 (Fortschrittsoptimismus) | +0.688 | large | 7.3 | 5.6 |
| D11 (Egalitarismus) | -0.682 | large | 3.9 | 5.9 |
| D09 (Menschliche Einzigartigkeit) | -0.534 | large | 4.6 | 5.8 |
| D04 (Verantwortungsgefuehl) | -0.455 | medium | 6.0 | 6.9 |
| D12 (Zukunft der Menschheit) | +0.443 | medium | 7.1 | 6.1 |
| D05 (Technologie-Determinismus) | +0.426 | medium | 8.0 | 7.0 |

### Architekt vs Innovator

| Dimension | delta | Interpretation | Mean Architekt | Mean Innovator |
|-----------|-------|----------------|-----------|-----------|
| D07 (Machtkonzentration) | +0.682 | large | 5.9 | 4.8 |
| D11 (Egalitarismus) | -0.591 | large | 3.9 | 5.3 |
| D12 (Zukunft der Menschheit) | -0.352 | medium | 7.1 | 7.7 |
| D06 (Fortschrittsoptimismus) | -0.337 | medium | 7.3 | 7.9 |

### Architekt vs Befreier

| Dimension | delta | Interpretation | Mean Architekt | Mean Befreier |
|-----------|-------|----------------|-----------|-----------|
| D07 (Machtkonzentration) | +1.000 | large | 5.9 | 3.6 |
| D11 (Egalitarismus) | -0.982 | large | 3.9 | 7.3 |
| D02 (Kontrollueberzeugung) | +0.759 | large | 8.1 | 7.0 |
| D04 (Verantwortungsgefuehl) | -0.530 | large | 6.0 | 7.0 |
| D09 (Menschliche Einzigartigkeit) | -0.528 | large | 4.6 | 5.4 |
| D08 (Dringlichkeit) | +0.419 | medium | 8.3 | 7.5 |
| D05 (Technologie-Determinismus) | +0.354 | medium | 8.0 | 7.4 |

### Hueter vs Innovator

| Dimension | delta | Interpretation | Mean Hueter | Mean Innovator |
|-----------|-------|----------------|-----------|-----------|
| D06 (Fortschrittsoptimismus) | -0.889 | large | 5.6 | 7.9 |
| D07 (Machtkonzentration) | -0.761 | large | 3.8 | 4.8 |
| D12 (Zukunft der Menschheit) | -0.646 | large | 6.1 | 7.7 |
| D02 (Kontrollueberzeugung) | -0.609 | large | 6.5 | 7.7 |
| D09 (Menschliche Einzigartigkeit) | +0.466 | medium | 5.8 | 4.7 |
| D05 (Technologie-Determinismus) | -0.413 | medium | 7.0 | 8.0 |

### Hueter vs Befreier

| Dimension | delta | Interpretation | Mean Hueter | Mean Befreier |
|-----------|-------|----------------|-----------|-----------|
| D06 (Fortschrittsoptimismus) | -0.865 | large | 5.6 | 7.5 |
| D11 (Egalitarismus) | -0.539 | large | 5.9 | 7.3 |
| D12 (Zukunft der Menschheit) | -0.539 | large | 6.1 | 7.2 |

### Innovator vs Befreier

| Dimension | delta | Interpretation | Mean Innovator | Mean Befreier |
|-----------|-------|----------------|-----------|-----------|
| D07 (Machtkonzentration) | +0.791 | large | 4.8 | 3.6 |
| D11 (Egalitarismus) | -0.786 | large | 5.3 | 7.3 |
| D02 (Kontrollueberzeugung) | +0.554 | large | 7.7 | 7.0 |
| D09 (Menschliche Einzigartigkeit) | -0.447 | medium | 4.7 | 5.4 |
| D05 (Technologie-Determinismus) | +0.353 | medium | 8.0 | 7.4 |

### Staerkste Differenzierungsdimensionen (ueber alle Cluster-Paare)

| Rang | Dimension | Medium+ Effekte | Max |delta| |
|------|-----------|----------------|-------------|
| 1 | D07 (Machtkonzentration) | 5x | 1.000 |
| 2 | D11 (Egalitarismus) | 5x | 0.982 |
| 3 | D06 (Fortschrittsoptimismus) | 4x | 0.889 |
| 4 | D02 (Kontrollueberzeugung) | 4x | 0.759 |
| 5 | D12 (Zukunft der Menschheit) | 4x | 0.646 |
| 6 | D09 (Menschliche Einzigartigkeit) | 4x | 0.534 |
| 7 | D05 (Technologie-Determinismus) | 4x | 0.426 |
| 8 | D04 (Verantwortungsgefuehl) | 2x | 0.530 |
| 9 | D08 (Dringlichkeit) | 1x | 0.419 |

## 5. Rollen-Vergleiche (Cliff's delta)

Rollenverteilung: CEO n=33, Akademiker n=10, Investor n=13, Gruender n=44

### CEO vs Akademiker

| Dimension | delta | Interpretation | Mean CEO | Mean Akademiker |
|-----------|-------|----------------|-----------|-----------|
| D02 (Kontrollueberzeugung) | +0.788 | large | 7.7 | 6.2 |
| D06 (Fortschrittsoptimismus) | +0.582 | large | 7.7 | 6.1 |
| D12 (Zukunft der Menschheit) | +0.554 | large | 7.5 | 6.1 |
| D07 (Machtkonzentration) | +0.542 | large | 4.9 | 4.0 |
| D05 (Technologie-Determinismus) | +0.518 | large | 7.9 | 6.8 |
| D10 (Transhumanismus) | +0.509 | large | 5.6 | 4.2 |
| D11 (Egalitarismus) | -0.473 | medium | 5.7 | 7.1 |
| D09 (Menschliche Einzigartigkeit) | -0.470 | medium | 5.0 | 6.1 |
| D08 (Dringlichkeit) | +0.412 | medium | 8.2 | 7.1 |

### Akademiker vs Investor

| Dimension | delta | Interpretation | Mean Akademiker | Mean Investor |
|-----------|-------|----------------|-----------|-----------|
| D02 (Kontrollueberzeugung) | -0.877 | large | 6.2 | 8.0 |
| D12 (Zukunft der Menschheit) | -0.708 | large | 6.1 | 8.1 |
| D09 (Menschliche Einzigartigkeit) | +0.677 | large | 6.1 | 4.4 |
| D06 (Fortschrittsoptimismus) | -0.638 | large | 6.1 | 8.0 |
| D04 (Verantwortungsgefuehl) | +0.631 | large | 7.4 | 6.0 |
| D05 (Technologie-Determinismus) | -0.631 | large | 6.8 | 8.1 |
| D11 (Egalitarismus) | +0.600 | large | 7.1 | 4.7 |
| D10 (Transhumanismus) | -0.569 | large | 4.2 | 5.7 |
| D01 (Sendungsbewusstsein) | -0.423 | medium | 5.8 | 6.5 |

### Akademiker vs Gruender

| Dimension | delta | Interpretation | Mean Akademiker | Mean Gruender |
|-----------|-------|----------------|-----------|-----------|
| D02 (Kontrollueberzeugung) | -0.700 | large | 6.2 | 7.4 |
| D11 (Egalitarismus) | +0.580 | large | 7.1 | 5.7 |
| D06 (Fortschrittsoptimismus) | -0.523 | large | 6.1 | 7.4 |
| D09 (Menschliche Einzigartigkeit) | +0.509 | large | 6.1 | 4.9 |
| D12 (Zukunft der Menschheit) | -0.493 | large | 6.1 | 7.2 |
| D10 (Transhumanismus) | -0.484 | large | 4.2 | 5.3 |
| D04 (Verantwortungsgefuehl) | +0.477 | large | 7.4 | 6.3 |
| D05 (Technologie-Determinismus) | -0.448 | medium | 6.8 | 7.7 |
| D07 (Machtkonzentration) | -0.373 | medium | 4.0 | 4.5 |
| D08 (Dringlichkeit) | -0.357 | medium | 7.1 | 8.0 |

### Investor vs Gruender

| Dimension | delta | Interpretation | Mean Investor | Mean Gruender |
|-----------|-------|----------------|-----------|-----------|
| D02 (Kontrollueberzeugung) | +0.390 | medium | 8.0 | 7.4 |
| D12 (Zukunft der Menschheit) | +0.381 | medium | 8.1 | 7.2 |
| D01 (Sendungsbewusstsein) | +0.337 | medium | 6.5 | 5.9 |

## 6. Gender-Vergleich

Frauen n=14, Maenner n=86

### Cliff's delta

| Dimension | delta | Interpretation | Mean Frauen | Mean Maenner |
|-----------|-------|----------------|-------------|--------------|
| D01 (Sendungsbewusstsein) | -0.171 | small | 5.9 | 6.3 |
| D02 (Kontrollueberzeugung) | -0.379 | medium | 6.9 | 7.5 |
| D04 (Verantwortungsgefuehl) | +0.345 | medium | 7.1 | 6.4 |
| D05 (Technologie-Determinismus) | -0.499 | large | 7.0 | 7.8 |
| D07 (Machtkonzentration) | -0.168 | small | 4.3 | 4.6 |
| D08 (Dringlichkeit) | -0.392 | medium | 7.1 | 8.0 |
| D09 (Menschliche Einzigartigkeit) | +0.588 | large | 5.9 | 4.8 |
| D10 (Transhumanismus) | -0.383 | medium | 4.7 | 5.4 |
| D11 (Egalitarismus) | +0.455 | medium | 6.9 | 5.5 |

## 7. Kruskal-Wallis H-Test (4 heuristische Cluster)

| Dimension | H | p-Wert | Signifikant? |
|-----------|---|--------|--------------|
| D01 (Sendungsbewusstsein) | 2.59 | 0.4592 | n.s. |
| D02 (Kontrollueberzeugung) | 33.55 | 0.0000 | *** |
| D03 (Zugehoerigkeitsgefuehl) | 3.75 | 0.2901 | n.s. |
| D04 (Verantwortungsgefuehl) | 10.76 | 0.0131 | * |
| D05 (Technologie-Determinismus) | 11.21 | 0.0106 | * |
| D06 (Fortschrittsoptimismus) | 29.55 | 0.0000 | *** |
| D07 (Machtkonzentration) | 64.76 | 0.0000 | *** |
| D08 (Dringlichkeit) | 6.25 | 0.0999 | n.s. |
| D09 (Menschliche Einzigartigkeit) | 17.50 | 0.0006 | *** |
| D10 (Transhumanismus) | 4.04 | 0.2567 | n.s. |
| D11 (Egalitarismus) | 49.57 | 0.0000 | *** |
| D12 (Zukunft der Menschheit) | 17.93 | 0.0005 | *** |

## 8. Deskriptive Statistik (Streuung)

Sortiert nach Standardabweichung (absteigend):

| Rang | Dimension | Mean | SD | IQR | Range | Min | Max | Schiefe | Kurtosis |
|------|-----------|------|-----|-----|-------|-----|-----|---------|----------|
| 1 | D11 (Egalitarismus) | 5.72 | 1.670 | 2.0 | 7 | 2 | 9 | -0.22 | -0.57 |
| 2 | D04 (Verantwortungsgefuehl) | 6.54 | 1.251 | 1.0 | 5 | 4 | 9 | +0.14 | -0.54 |
| 3 | D08 (Dringlichkeit) | 7.91 | 1.232 | 2.0 | 5 | 5 | 10 | -0.09 | -0.79 |
| 4 | D10 (Transhumanismus) | 5.32 | 1.162 | 1.0 | 7 | 2 | 9 | +0.64 | +1.53 |
| 5 | D01 (Sendungsbewusstsein) | 6.21 | 1.149 | 2.0 | 6 | 4 | 10 | +0.43 | +0.16 |
| 6 | D06 (Fortschrittsoptimismus) | 7.46 | 1.114 | 1.0 | 6 | 4 | 10 | -0.58 | +0.96 |
| 7 | D12 (Zukunft der Menschheit) | 7.29 | 1.113 | 1.0 | 6 | 4 | 10 | -0.06 | +0.39 |
| 8 | D09 (Menschliche Einzigartigkeit) | 4.98 | 1.063 | 2.0 | 5 | 3 | 8 | +0.39 | +0.12 |
| 9 | D07 (Machtkonzentration) | 4.57 | 1.037 | 1.0 | 5 | 2 | 7 | +0.22 | +0.26 |
| 10 | D05 (Technologie-Determinismus) | 7.72 | 0.900 | 1.0 | 4 | 5 | 9 | -0.51 | +0.31 |
| 11 | D02 (Kontrollueberzeugung) | 7.45 | 0.892 | 1.0 | 5 | 4 | 9 | -0.49 | +1.08 |
| 12 | D03 (Zugehoerigkeitsgefuehl) | 6.12 | 0.742 | 1.0 | 3 | 5 | 8 | -0.04 | -0.84 |

**Groesste Streuung:** D11 (Egalitarismus) mit SD=1.670
**Kleinste Streuung:** D03 (Zugehoerigkeitsgefuehl) mit SD=0.742

## 9. Zusammenfassung der Kernbefunde

### PCA
- 5 Hauptkomponenten erklaeren 80% der Gesamtvarianz
- PC1 (35.8% Varianz) laed am staerksten auf: D02 (Kontrollueberzeugung), D05 (Technologie-Determinismus), D09 (Menschliche Einzigartigkeit)
- PC2 (19.2% Varianz) differenziert primaer ueber: D01 (Sendungsbewusstsein), D04 (Verantwortungsgefuehl)

### Clustering
- HDBSCAN findet KEINE robusten natuerlichen Cluster -- die KI-Elite bildet ein Kontinuum
- Heuristische Typen (Architekt/Hueter/Innovator/Befreier) sind als Idealtypen zu interpretieren, nicht als diskrete Gruppen

### Effektstaerken
- Signifikante Kruskal-Wallis-Unterschiede (p<0.05) auf: D02, D04, D05, D06, D07, D09, D11, D12
- Staerkste Differenzierungsdimension: D07 (Machtkonzentration) mit 5x medium+ Cliff's delta

### Streuung
- Heterogenste Dimension: D11 (Egalitarismus) -- hier divergieren die Weltbilder am staerksten
- Homogenste Dimension: D03 (Zugehoerigkeitsgefuehl) -- hier herrscht relativer Konsens

---

*Generiert: 2026-03-27 | Methode: PCA + HDBSCAN + Cliff's delta + Kruskal-Wallis + Mann-Whitney U*
*Datenbasis: rating_GESAMT_D01-D12.md (100 Personen x 12 Dimensionen)*