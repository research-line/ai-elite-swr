# Konsistenz-Review v7 -- KI_Elite_v2_en.tex

**Datum:** 2026-03-31
**Reviewer:** Claude Opus 4.6 (automatisiert)
**Datei:** `paper_A/KI_Elite_v2_en.tex`
**Stand des Papers:** 2026-03-27 (laut Datei-Header)

---

## Zusammenfassung

**7 Probleme gefunden**, davon 2 schwerwiegend (fehlende Labels), 2 mittelschwer (veraltete Verweise), 3 leicht (Konsistenz-Feinheiten). Keine veralteten v1-Zahlen im Haupttext; die v1-Zahlen werden korrekt als Vergleichswerte markiert.

---

## Gefundene Probleme

### Problem 1 -- SCHWER: Fehlende \label{sec:method} (Zeile 93)

**Zeile 93 (Abstract):**
```latex
(described in Section~\ref{sec:method})
```

**Problem:** Das Label `sec:method` existiert nirgendwo in der Datei. Das tatsächliche Label der Methodik-Sektion ist `sec:methodik` (Zeile 195). LaTeX wird hier "??" ausgeben.

**Fix:** `\ref{sec:method}` → `\ref{sec:methodik}`

---

### Problem 2 -- SCHWER: Fehlende \label{sec:limitations} (Zeile 707)

**Zeile 707 (Discussion, Methodological Reflection):**
```latex
are systematically analyzed in the limitations section below (Section~\ref{sec:limitations}).
```

**Problem:** Das Label `sec:limitations` existiert nicht. Das tatsächliche Label ist `sec:limitationen` (Zeile 730). LaTeX wird hier "??" ausgeben.

**Fix:** `\ref{sec:limitations}` → `\ref{sec:limitationen}`

---

### Problem 3 -- MITTEL: Alte Zenodo-DOI + "companion paper" im Data Availability Statement (Zeile 874)

**Zeile 874:**
```latex
The companion paper on the SWR method is available at: \url{https://doi.org/10.5281/zenodo.18736720}.
```

**Problem:** Doppeltes Relikt:
1. Der Verweis auf "companion paper" widerspricht der aktuellen Strategie (Paper B wird erst nach Paper A geschrieben; Zeile 945 bestätigt: "Geiger2026SWR removed -- Paper B will be written after Paper A submission").
2. Die alte Zenodo-DOI 10.5281/zenodo.18736720 ist noch vorhanden.

**Fix:** Gesamten Satz entfernen. Alternativ ersetzen durch einen Vorwärtsverweis:
```latex
A companion paper detailing the SWR method is in preparation.
```

---

### Problem 4 -- MITTEL: "companion paper" im Datei-Header (Zeile 9)

**Zeile 9:**
```latex
%% Companion Paper: SWR_v1_ger.tex (Synthetische Weltbild-Rekonstruktion)
```

**Problem:** Dieser LaTeX-Kommentar ist zwar unsichtbar im PDF, verweist aber auf die alte Struktur (SWR_v1_ger.tex als separates Paper). Kann bei Weiterentwicklung zu Verwirrung führen.

**Fix:** Zeile aktualisieren oder entfernen:
```latex
%% Paper B (SWR method paper) will be written after Paper A submission
```

---

### Problem 5 -- LEICHT: Delta=-3 in Discussion statt v2-Wert (Zeile 701)

**Zeile 701 (Discussion, Agentic Alignment):**
```latex
The say-do gap indicated by RQ3 (largest observed discrepancy: egalitarianism $\Delta = -3$)
```

**Problem:** Der Wert Δ=-3 ist der **v1-Wert** für D11. Der aktuelle v2-Wert ist Δ=-2 (Zeile 459, Tab. 5). Zwar ist Δ=-3 korrekt als "largest observed" (nämlich v1), aber der Kontext suggeriert, dass der aktuelle Befund gemeint ist. Die Conclusion (Zeile 841) nennt korrekt Δ=-2 für v2. Das erzeugt einen inhaltlichen Widerspruch innerhalb Discussion vs. Conclusion.

**Kontext-Vergleich:**
- Tabelle (Z. 459): D11 Δv2 = -2, Δv1 = -3 ✓
- Results-Text (Z. 479): "D11, Δ -2 in v2, -3 in v1" ✓
- Synopsis-Tabelle (Z. 652): "D07 +2, D11 -2; stable across v1/v2" ✓
- Conclusion (Z. 841): "D11, Δ -2" ✓
- **Discussion (Z. 701): "Δ = -3"** ← Inkonsistent

**Fix:** Entweder auf v2-Wert aktualisieren:
```latex
(largest observed discrepancy: egalitarianism $\Delta = -2$)
```
Oder explizit als v1-Wert kennzeichnen:
```latex
(largest observed discrepancy: egalitarianism $\Delta = -3$ in v1, $-2$ in v2)
```

---

### Problem 6 -- LEICHT: MAE=1.25 als v1-Vergleichswert (Zeile 287)

**Zeile 287 (Quality Assurance, expected-discrepancy control):**
```latex
By comparison, the real AI elite gap (MAE $= 1.25$) is $2.5\times$ larger
```

**Problem:** Der Wert MAE=1.25 ist weder der v1-Wert (1.42) noch der v2-Wert (0.75). Er stammt vermutlich aus einer älteren Berechnung oder einer anderen Berechnungsbasis. Alle anderen Stellen im Paper nennen konsistent:
- v1 MAE = 1.42 (Z. 290, 463, 468, 749)
- v2 MAE = 0.75 (Z. 290, 463, 468, 749)

Der Wert 1.25 taucht sonst nirgends auf. Zudem: Die Control-Group-Baseline ist MAE=0.50 (v1) bzw. 0.92 (v2). Der Vergleichsfaktor "$2.5\times$ larger" passt zu 1.25/0.50, aber der MAE-Wert 1.25 selbst ist orphaniert.

**Fix:** Die Passage muss entschieden werden:
- Falls v1-Kontext: "the real AI elite gap (MAE $= 1.42$) is $2.8\times$ larger"
- Falls v2-Kontext: Diese Passage verliert ihre Aussagekraft, da v2 MAE (0.75) < Control v2 (0.92). Die Passage müsste umgeschrieben werden, um den v2-Befund korrekt darzustellen.

**Empfehlung:** Da die Passage in der Quality-Assurance-Sektion steht und den expected-discrepancy control beschreibt, sollte sie den aktuellen v2-Stand reflektieren. Vorschlag:
```latex
The resulting statement--action profiles were highly congruent ($r = 0.912$,
MAE $= 0.50$). Under the original same-instance protocol (v1), the real AI
elite gap (MAE $= 1.42$) was $2.8\times$ larger. Under strict instance
separation (v2), the gap shrank to MAE $= 0.75$, falling below the v2
control baseline (MAE $= 0.92$) -- see Section~\ref{sec:ergebnisse:f3}
for the full analysis.
```

---

### Problem 7 -- LEICHT: "systematic say-do gap" in Discussion vs. "not reliably distinguishable from noise" in Results

**Betroffene Stellen:**
- **Zeile 669 (Discussion):** "RQ3 indicates a systematic say-do gap at the group level as the most salient finding"
- **Zeile 290/468 (Results):** "the overall gap magnitude is not reliably distinguishable from measurement noise in single runs"
- **Zeile 715 (Discussion):** "The systematic group-level say-do gap has a policy implication"

**Problem:** Die Discussion-Sektion spricht wiederholt von "systematic say-do gap" ohne den Vorbehalt, dass der Gesamtgap unter Measurement-Noise fällt. Erst in den Results ist klar, dass nur D07 und D11 robust sind. Die Discussion-Formulierungen könnten als Übertreibung gelesen werden.

**Fix (Zeile 669):** Präzisieren:
```latex
RQ3~indicates directional say-do discrepancies on specific dimensions
(D07, D11) as the most salient finding
```

**Fix (Zeile 715):** Bereits akzeptabel, da der Kontext "entire institutional groups ... exhibit consistent discrepancies" sich auf die robusten Dimensionen beziehen könnte. Optional: "on the D07/D11 axis" ergänzen.

---

## Geprüft und für konsistent befunden

### Veraltete Zahlen (v1 vs. v2)
- ✅ MAE=0.75 korrekt in Tabelle (Z. 463), Results-Text (Z. 468, 290), Limitations (Z. 749)
- ✅ MAE=1.42 korrekt als v1-Vergleichswert markiert (Z. 290, 463, 468, 749)
- ✅ D07 Δ=+2 konsistent (Z. 455, 470, 479, 482, 652, 749, 841)
- ✅ D11 Δ=-2 (v2) konsistent (Z. 459, 470, 479, 482, 652, 749, 841)
- ✅ D11 Δ=-3 (v1) korrekt als v1-Wert in Tabelle (Z. 459) und Results (Z. 479)
- ⚠️ AUSNAHME: Z. 701 (s. Problem 5) und Z. 287 (s. Problem 6)

### Geiger2026SWR-Reste
- ✅ `\citet{Geiger2026SWR}` wird nirgendwo aufgerufen
- ✅ bibitem ist korrekt entfernt (Z. 945: Kommentar bestätigt Entfernung)
- ⚠️ AUSNAHME: Zenodo-DOI in Z. 874 (s. Problem 3)

### Inter-LLM / Inter-Model
- ✅ "inter-model replication" (Z. 287) korrekt als "external replication" / "independent research task" formuliert, NICHT als Validierungsvorschlag
- ✅ Kein "inter-LLM" als internes Validierungskriterium

### Terminologie
- ✅ "focus control" konsistent verwendet (Z. 287, 296, 745, 1236)
- ✅ "contamination" nur als "contamination risk" oder "contamination effect" (nicht "contamination control")
- ✅ "IMIIRR" konsistent (Z. 287, 707)
- ✅ Kein "inter-rater" als Methodenbezeichnung (nur als Vergleichswert für Human-Coder)

### Datenkonsistenz Abstract/Results/Discussion/Conclusion
- ✅ "technological messianism with ambivalence structure" konsistent
- ✅ 3,132 Datenpunkte konsistent (Z. 93 via "group-level syntheses", Z. 146, Z. 209, Z. 751, Z. 1142)
- ✅ 12 Dimensionen konsistent
- ✅ 4 Typen (Architect, Guardian, Innovator, Liberator) konsistent
- ✅ 9 inter-group comparisons konsistent (Z. 93, 146, 281)
- ✅ IMIIRR ICC=0.902 konsistent (Z. 287, 707, 759, 761)
- ✅ D09/D11 als "dual trough" konsistent

### Bibliografie-Konsistenz
- ✅ Alle `\citet{}` und `\citep{}` im Text haben entsprechende `\bibitem{}`-Einträge
- ✅ Kein verwaister `\cite{Geiger2026SWR}`

### Label-Referenz-Konsistenz
- ✅ Alle `\ref{tab:...}`, `\ref{fig:...}`, `\ref{app:...}` haben zugehörige Labels
- ✅ Alle `\ref{sec:ergebnisse:...}`, `\ref{sec:methodik:...}`, `\ref{sec:limitationen:...}` haben Labels
- ⚠️ AUSNAHME: `\ref{sec:method}` (Z. 93) und `\ref{sec:limitations}` (Z. 707) -- s. Probleme 1 und 2

---

## Prioritäten-Ranking

| Prio | Problem | Schwere | Zeile |
|------|---------|---------|-------|
| 1 | Fehlende \label{sec:method} | SCHWER (erzeugt "??" im PDF) | 93 |
| 2 | Fehlende \label{sec:limitations} | SCHWER (erzeugt "??" im PDF) | 707 |
| 3 | Alte Zenodo-DOI + companion paper | MITTEL (inhaltlich veraltet) | 874 |
| 4 | MAE=1.25 Orphan-Wert | LEICHT-MITTEL (inkonsistente Zahl) | 287 |
| 5 | Δ=-3 statt v2-Wert in Discussion | LEICHT (missverständlich) | 701 |
| 6 | "systematic say-do gap" Formulierung | LEICHT (Nuance) | 669, 715 |
| 7 | Companion Paper im Header-Kommentar | LEICHT (nur Kommentar) | 9 |
