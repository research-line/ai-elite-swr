# Einfluss-Strata-Vergleich: Top 10 vs. Mitte vs. Bottom 10

> Erstellt: 2026-03-31
> Modell: Claude Opus 4.6 (separate Instanzen pro Stratum)
> Methode: Op1+Op2 auf Rang-basierte Strata der Top-100-Liste

---

## Design

| Stratum | Rang | Personen | Datenpunkte | Quelle |
|---------|------|----------|-------------|--------|
| **Top 10** | 1-10 | 10/10 | 500 (300A + 200H) | `synthese_T10_ges_AH.md` (Batch 1, 2026-02-12) |
| **Mitte** | 40-60 | 14/21 mit Daten | 409 (241A + 168H) | `synthese_STRATA_mitte_AH.md` (2026-03-31) |
| **Bottom 10** | 91-100 | 8/10 mit Daten | 267 (150A + 117H) | `synthese_STRATA_bottom_AH.md` (2026-03-31) |

**Caveat:** Mitte und Bottom basieren auf teilrekonstruierter DB (64/100 Personen). Die Strata-SUs enthalten nicht alle Personen des jeweiligen Rangbereichs.

---

## Dimensionale Ratings

| Dimension | Top 10 | Mitte | Bottom 10 | T-M | T-B | M-B |
|-----------|--------|-------|-----------|-----|-----|-----|
| D01 Sendungsbewusstsein | 9 | 7 | 7 | +2 | +2 | 0 |
| D02 Selbstwirksamkeit | 9 | 7 | 6 | +2 | +3 | +1 |
| D03 Arbeitsethos | 9 | 8 | 8 | +1 | +1 | 0 |
| D04 Verantwortungsgefühl | 8 | 8 | 7 | 0 | +1 | +1 |
| D05 Techno-Determinismus | 9 | 6 | 6 | +3 | +3 | 0 |
| D06 Fortschrittsglaube | 8 | 6 | 6 | +2 | +2 | 0 |
| D07 Machtkonzentration | 7 | 4 | 5 | +3 | +2 | -1 |
| D08 Dringlichkeit | 9 | 8 | 7 | +1 | +2 | +1 |
| D09 Menschliche Wertschätzung | 4 | 6 | 8 | -2 | **-4** | -2 |
| D10 Posthumanismus | 8 | 5 | 3 | +3 | **+5** | +2 |
| D11 Egalitarismus | 4 | 6 | 4 | -2 | 0 | +2 |
| D12 Zukunftskontrolle | 8 | 6 | 6 | +2 | +2 | 0 |
| **Avg** | **7.7** | **6.4** | **6.1** | **+1.2** | **+1.6** | **+0.3** |

---

## Schlüsselbefunde

### 1. Einfluss-Gradient bestätigt
Avg-Rating sinkt monoton mit dem Rang: Top 10 (7.7) > Mitte (6.4) > Bottom 10 (6.1). Die Mächtigsten haben das intensivste Weltbild.

### 2. Stärkste Gradiente (Top→Bottom)
- **D10 Posthumanismus: 8→5→3 (Δ=5)** — die Mächtigsten sind die posthumanistischsten
- **D09 Menschliche Wertschätzung: 4→6→8 (Δ=-4)** — die Mächtigsten schätzen Menschen am wenigsten
- **D05 Techno-Determinismus: 9→6→6 (Δ=3)** — an der Spitze: Technologie bestimmt alles
- **D07 Machtkonzentration: 7→4→5 (Δ=2)** — nur Top 10 will Macht konzentrieren

### 3. Inversions-Dimensionen
Zwei Dimensionen STEIGEN mit sinkendem Rang:
- **D09 Human Appreciation:** Bottom (8) > Mitte (6) > Top (4) — wer weniger Macht hat, schätzt Menschen mehr
- **D11 Egalitarismus:** Mitte (6) > Top (4) = Bottom (4) — die Mitte ist am egalitärsten

### 4. Geteilter Kern (keine Strata-Differenz)
- **D03 Arbeitsethos:** 9/8/8 — universelle Identifikation mit Arbeit
- **D04 Verantwortungsgefühl:** 8/8/7 — durchgehend hohes Verantwortungsgefühl

### 5. Macht-Gemaessigtheits-Paradox bestätigt
Die Top 10 vereinen das extremste Weltbild (höchster Avg) mit der höchsten Ressourcenkontrolle. Das Muster aus RQ6 (F6: Macht) wird durch die Strata-Analyse bestätigt: Je mächtiger, desto techno-deterministischer, posthumanistischer und weniger menschenwertschätzend.

---

## Methodische Einschränkungen

1. **Top 10 Ratings stammen aus Batch 1** (selbe Instanz wie GA_ges_AH etc.) — könnten durch Kontext-Effekte beeinflusst sein
2. **Mitte und Bottom haben teilweise Datenlücken** (14/21 bzw. 8/10 Personen mit Daten)
3. **Keine Inferenzstatistik** — Einzelmessungen pro Stratum; N=30 Runs könnten CIs liefern

---

*Erstellt: 2026-03-31 | Autor: Claude Opus 4.6*
