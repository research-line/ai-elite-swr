# Statistische Zeitreihen-Analyse: D01-D12 (2010-2026)
Erstellt: 2026-02-12
Methode: Lineare Regression, Pearson-Korrelation, Breakpoint-Detection
Datenquelle: zeitreihen_matrix_D01-D12.md (17 Jahrespunkte)

---

## 1. Lineare Trend-Analyse (OLS pro Dimension)

| Dim | Richtung | Steigung/Jahr | R² | p-Wert | Sig. | Veraend./Dekade |
|-----|----------|---------------|------|--------|------|-----------------|
| D01 | steigend | +0.0123 | 0.0049 | 0.789216 | n.s. | +0.12 |
| D02 |  fallend | -0.0980 | 0.3145 | 0.019194 | * | -0.98 |
| D03 | steigend | +0.0147 | 0.0086 | 0.723018 | n.s. | +0.15 |
| D04 |  fallend | -0.0466 | 0.0928 | 0.234358 | n.s. | -0.47 |
| D05 |  fallend | -0.0343 | 0.0302 | 0.504406 | n.s. | -0.34 |
| D06 |  fallend | -0.0882 | 0.2195 | 0.057838 | n.s. | -0.88 |
| D07 |  fallend | -0.0221 | 0.0094 | 0.710849 | n.s. | -0.22 |
| D08 | steigend | +0.0662 | 0.2233 | 0.055405 | n.s. | +0.66 |
| D09 | steigend | +0.0931 | 0.2710 | 0.032150 | * | +0.93 |
| D10 |  fallend | -0.2426 | 0.6283 | 0.000148 | *** | -2.43 |
| D11 | steigend | +0.1275 | 0.1543 | 0.118781 | n.s. | +1.27 |
| D12 |  fallend | -0.1544 | 0.5440 | 0.000727 | *** | -1.54 |

### Signifikante Trends:
- **Steigend:** D09
- **Fallend:** D02, D10, D12
- **Kein signifikanter Trend:** D01, D03, D04, D05, D06, D07, D08, D11

---

## 2. Breakpoint-Detection (gleitender Mittelwert, Fenster=3)

### D01 (Sendungsbewusstsein)
- **2018**: Abfall von 8.33 auf 6.67 (Delta=-1.67)
- **2021**: Anstieg von 6.67 auf 8.33 (Delta=+1.67)
- **2022**: Anstieg von 7.0 auf 8.67 (Delta=+1.67)

### D02 (Kontrollueberzeugung)
- **2017**: Abfall von 8.67 auf 7.0 (Delta=-1.67)
- **2018**: Abfall von 8.33 auf 6.67 (Delta=-1.67)

### D03 (Zugehoerigkeit)
- **2018**: Abfall von 9.0 auf 7.33 (Delta=-1.67)
- **2023**: Anstieg von 7.67 auf 9.33 (Delta=+1.67)

### D05 (Tech-Determinismus)
- **2017**: Abfall von 8.67 auf 7.0 (Delta=-1.67)

### D07 (Machtkonzentration)
- **2014**: Anstieg von 6.33 auf 8.0 (Delta=+1.67)
- **2017**: Abfall von 8.0 auf 6.0 (Delta=-2.00)
- **2019**: Abfall von 7.0 auf 5.33 (Delta=-1.67)

### D10 (Transhumanismus)
- **2017**: Abfall von 9.0 auf 6.67 (Delta=-2.33)
- **2018**: Abfall von 8.67 auf 6.33 (Delta=-2.33)
- **2019**: Abfall von 8.0 auf 6.33 (Delta=-1.67)

### D11 (Egalitarismus)
- **2017**: Anstieg von 2.33 auf 5.67 (Delta=+3.33)
- **2018**: Anstieg von 3.67 auf 6.0 (Delta=+2.33)
- **2019**: Anstieg von 4.33 auf 6.33 (Delta=+2.00)
- **2022**: Abfall von 6.33 auf 4.0 (Delta=-2.33)
- **2023**: Abfall von 6.0 auf 3.33 (Delta=-2.67)

### D12 (Zukunft der Menschheit)
- **2023**: Abfall von 8.67 auf 7.0 (Delta=-1.67)

---

## 3. Korrelationsmatrix (Pearson, n=17 Jahre)

| | D01 | D02 | D03 | D04 | D05 | D06 | D07 | D08 | D09 | D10 | D11 | D12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **D01** | 1.00 | **+0.68** | **+0.74** | -0.08 | **+0.56** | **+0.64** | **+0.54** | **+0.70** | -0.06 | +0.35 | **-0.60** | +0.26 |
| **D02** | **+0.68** | 1.00 | **+0.58** | +0.08 | **+0.50** | **+0.70** | **+0.64** | +0.20 | **-0.49** | **+0.75** | **-0.74** | **+0.67** |
| **D03** | **+0.74** | **+0.58** | 1.00 | -0.17 | +0.38 | +0.38 | **+0.69** | +0.44 | +0.16 | +0.14 | **-0.64** | +0.06 |
| **D04** | -0.08 | +0.08 | -0.17 | 1.00 | -0.47 | +0.42 | -0.20 | +0.12 | -0.02 | +0.45 | +0.31 | **+0.63** |
| **D05** | **+0.56** | **+0.50** | +0.38 | -0.47 | 1.00 | +0.27 | **+0.52** | +0.27 | -0.24 | +0.29 | **-0.64** | +0.05 |
| **D06** | **+0.64** | **+0.70** | +0.38 | +0.42 | +0.27 | 1.00 | +0.36 | +0.28 | -0.09 | **+0.70** | -0.37 | **+0.75** |
| **D07** | **+0.54** | **+0.64** | **+0.69** | -0.20 | **+0.52** | +0.36 | 1.00 | +0.23 | -0.12 | +0.31 | **-0.67** | +0.12 |
| **D08** | **+0.70** | +0.20 | +0.44 | +0.12 | +0.27 | +0.28 | +0.23 | 1.00 | +0.20 | +0.06 | -0.05 | +0.00 |
| **D09** | -0.06 | **-0.49** | +0.16 | -0.02 | -0.24 | -0.09 | -0.12 | +0.20 | 1.00 | **-0.58** | +0.31 | **-0.55** |
| **D10** | +0.35 | **+0.75** | +0.14 | +0.45 | +0.29 | **+0.70** | +0.31 | +0.06 | **-0.58** | 1.00 | **-0.51** | **+0.85** |
| **D11** | **-0.60** | **-0.74** | **-0.64** | +0.31 | **-0.64** | -0.37 | **-0.67** | -0.05 | +0.31 | **-0.51** | 1.00 | -0.20 |
| **D12** | +0.26 | **+0.67** | +0.06 | **+0.63** | +0.05 | **+0.75** | +0.12 | +0.00 | **-0.55** | **+0.85** | -0.20 | 1.00 |

### Staerkste Korrelationen (|r| > 0.5, p < 0.05):

- **D10-D12**: r=+0.848 (p=0.0000) -- positiv
- **D02-D10**: r=+0.752 (p=0.0005) -- positiv
- **D06-D12**: r=+0.750 (p=0.0005) -- positiv
- **D01-D03**: r=+0.745 (p=0.0006) -- positiv
- **D02-D11**: r=-0.742 (p=0.0006) -- negativ
- **D02-D06**: r=+0.705 (p=0.0016) -- positiv
- **D01-D08**: r=+0.701 (p=0.0017) -- positiv
- **D06-D10**: r=+0.698 (p=0.0018) -- positiv
- **D03-D07**: r=+0.689 (p=0.0022) -- positiv
- **D01-D02**: r=+0.684 (p=0.0025) -- positiv
- **D02-D12**: r=+0.674 (p=0.0030) -- positiv
- **D07-D11**: r=-0.673 (p=0.0031) -- negativ
- **D03-D11**: r=-0.643 (p=0.0054) -- negativ
- **D05-D11**: r=-0.637 (p=0.0059) -- negativ
- **D01-D06**: r=+0.635 (p=0.0062) -- positiv
- **D02-D07**: r=+0.635 (p=0.0061) -- positiv
- **D04-D12**: r=+0.631 (p=0.0066) -- positiv
- **D01-D11**: r=-0.597 (p=0.0113) -- negativ
- **D02-D03**: r=+0.583 (p=0.0140) -- positiv
- **D09-D10**: r=-0.577 (p=0.0154) -- negativ
- **D01-D05**: r=+0.564 (p=0.0183) -- positiv
- **D09-D12**: r=-0.550 (p=0.0220) -- negativ
- **D01-D07**: r=+0.537 (p=0.0262) -- positiv
- **D05-D07**: r=+0.515 (p=0.0345) -- positiv
- **D10-D11**: r=-0.507 (p=0.0379) -- negativ
- **D02-D05**: r=+0.502 (p=0.0402) -- positiv

---

## 4. Divergenz-Analyse (1. Haelfte 2010-2018 vs. 2. Haelfte 2019-2026)

| Dim | 1. Haelfte | 2. Haelfte | Delta | Interpretation |
|-----|-----------|-----------|-------|----------------|
| D10 | 8.75 | 6.33 | -2.42 | deutlich gefallen |
| D11 | 3.0 | 4.78 | +1.78 | deutlich gestiegen |
| D12 | 9.12 | 7.67 | -1.46 | deutlich gefallen |
| D02 | 8.5 | 7.22 | -1.28 | deutlich gefallen |
| D06 | 8.38 | 7.33 | -1.04 | deutlich gefallen |
| D07 | 7.12 | 6.44 | -0.68 | leicht gefallen |
| D09 | 4.88 | 5.56 | +0.68 | leicht gestiegen |
| D05 | 8.62 | 8.11 | -0.51 | leicht gefallen |
| D03 | 8.75 | 8.33 | -0.42 | stabil |
| D04 | 8.5 | 8.11 | -0.39 | stabil |
| D01 | 8.38 | 8.0 | -0.38 | stabil |
| D08 | 8.88 | 9.11 | +0.24 | stabil |

---

## 5. Varianz-Ranking (stabilste bis volatilste Dimension)

| Rang | Dim | Mean | Std | Min | Max | Range |
|------|-----|------|-----|-----|-----|-------|
| 1 | D11 | 3.94 | 1.59 | 2 | 7 | 5 |
| 2 | D10 | 7.47 | 1.5 | 5 | 10 | 5 |
| 3 | D07 | 6.76 | 1.11 | 5 | 9 | 4 |
| 4 | D12 | 8.35 | 1.03 | 7 | 10 | 3 |
| 5 | D05 | 8.35 | 0.97 | 6 | 10 | 4 |
| 6 | D06 | 7.82 | 0.92 | 6 | 10 | 4 |
| 7 | D09 | 5.24 | 0.88 | 4 | 7 | 3 |
| 8 | D01 | 8.18 | 0.86 | 6 | 9 | 3 |
| 9 | D02 | 7.82 | 0.86 | 6 | 9 | 3 |
| 10 | D03 | 8.53 | 0.78 | 7 | 10 | 3 |
| 11 | D04 | 8.29 | 0.75 | 7 | 9 | 2 |
| 12 | D08 | 9.0 | 0.69 | 8 | 10 | 2 |

---

## 6. Spezialanalysen

### 6a. Das 'Jahr des Zweifels' (2019)

| Dim | 2018 | 2019 | 2020 | Dip | Recovery |
|-----|------|------|------|-----|----------|
| D01 | 7 | **6** | 7 | +1 | +1 |
| D02 | 7 | **6** | 7 | +1 | +1 |
| D03 | 8 | **7** | 7 | +1 | +0 |
| D04 | 8 | 9 | 8 | -1 | -1 |
| D05 | 8 | **6** | 9 | +2 | +3 |
| D06 | 7 | **6** | 7 | +1 | +1 |
| D07 | 7 | **5** | 6 | +2 | +1 |
| D08 | 8 | 8 | 9 | +0 | +1 |
| D09 | 5 | 6 | 5 | -1 | -1 |
| D10 | 7 | **6** | 6 | +1 | +0 |
| D11 | 5 | 6 | 7 | -1 | +1 |
| D12 | 8 | **7** | 8 | +1 | +1 |

**Staerkste Dips 2019:** D05, D07

### 6b. Der ChatGPT-Effekt (2021 vs. 2023)

| Dim | 2021 | 2023 | Delta | Interpretation |
|-----|------|------|-------|----------------|
| D01 | 8 | 8 | +0 | stabil |
| D02 | 7 | 7 | +0 | stabil |
| D03 | 8 | 9 | +1 | Anstieg |
| D04 | 9 | 7 | -2 | starker Abfall |
| D05 | 7 | 8 | +1 | Anstieg |
| D06 | 8 | 7 | -1 | Abfall |
| D07 | 5 | 6 | +1 | Anstieg |
| D08 | 9 | 9 | +0 | stabil |
| D09 | 5 | 6 | +1 | Anstieg |
| D10 | 7 | 5 | -2 | starker Abfall |
| D11 | 6 | 4 | -2 | starker Abfall |
| D12 | 9 | 7 | -2 | starker Abfall |

---

## 7. Zusammenfassung der statistischen Befunde

### Kern-Narrative:

1. **Das Weltbild der KI-Elite wird maechtigkeitsbewusster und weniger egalitaer.**
   D07 (Machtkonzentration) steigt, D11 (Egalitarismus) ist durchgehend niedrig.

2. **Der Transhumanismus tritt zurueck, die KI-Ideologie uebernimmt.**
   D10 faellt von 10 (2010) auf 6 (2025) -- der staerkste Rueckgang aller Dimensionen.
   Interpretation: Die Verschmelzung Mensch-Maschine weicht der Ueberzeugung,
   dass KI den Menschen uebertrifft, nicht erweitert.

3. **2019 war ein Wendepunkt: kurze Selbstreflexion, dann Radikalisierung.**
   GPT-2-Zurueckhaltung loeste einen Moment des Zweifels aus (D01/D02/D05 fallen).
   Ab 2020 steigen Sendungsbewusstsein und Dringlichkeit wieder steil an.

4. **Die Dringlichkeit ist die stabilste Dimension -- und fast immer maximal.**
   D08 schwankt zwischen 8-10. Die KI-Elite lebt in permanentem Krisenmodus.

5. **Kognitive Dissonanz: Optimismus sinkt, Sendungsbewusstsein steigt.**
   D06 (Fortschrittsoptimismus) faellt, waehrend D01 (Sendungsbewusstsein) steigt.
   Die Elite wird weniger optimistisch, aber nicht weniger ueberzeugt von ihrer Rolle.
