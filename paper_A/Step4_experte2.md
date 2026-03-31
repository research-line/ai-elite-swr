# Experten-Review, Runde 2: Minimaler Einreichungsplan

**Reviewer-Perspektive:** Führender Fachexperte für Computational Social Science, zweite Runde
**Datum:** 2026-03-30
**Dokument:** KI_Elite_v2_en.tex (englische Version)
**Vorgänger:** Step1_konstruktiv.md, Step2_experte.md, Step3_konstruktiv2.md
**Auftrag:** Minimaler Einreichungsplan -- was MUSS, was KANN warten

---

## A: Pflicht-Korrekturen (minimal für Einreichung)

Nur das, was ohne Umsetzung zur Ablehnung führt. Alles andere gehört in Abschnitt B.

### A1. Op4-Widerspruch in Tabelle 1 korrigieren (5 Minuten)

**Problem:** Tabelle 1 (Zeile 251) sagt: "Op4 was not conducted in this study." Section 3.5 (Zeile 283) berichtet Op4 als durchgeführte Validierung (44/50, 88%). Das ist ein Faktenfehler im Manuskript. Jeder Reviewer wird ihn finden, und er untergräbt das Vertrauen in die gesamte Qualitätssicherung.

**Fix:** Fußnote in Tabelle 1 (Zeile 251) ersetzen:

Alt:
> "$^*$Op4 was not conducted in this study."

Neu:
> "$^*$Op4 was conducted as a validation experiment (5 groups, 50 predictions, 88\% confirmed; see Section 3.5) but not as a systematic operationalization across all synthesis units."

### A2. Eigenständiger Methodik-Kurzabschnitt (2--3 Stunden)

**Problem:** Section 3.2 umfasst einen einzigen Absatz (Zeile 223) zur SWR-Kernlogik. Ohne das Companion Paper ist die Methode eine Black Box. Dies ist der wahrscheinlichste Desk-Rejection-Grund.

**Fix:** Nach Zeile 223 (vor Section 3.2.1 "Data Aggregation Procedure") einen neuen Unterabschnitt einfügen: `\subsubsection{The SWR Procedure in Brief}`. Umfang: ca. 1 Seite (nicht 1,5 -- minimaler Ansatz). Inhalt:

1. Formale Definition des inversen Problems: "Given observable outputs $O = \{s_1, \ldots, s_n, a_1, \ldots, a_m\}$ of a sociologically defined group $G$, SWR infers the latent collective belief system $W$ that most coherently generates $O$."
2. Die fünf SWR-Schritte als nummerierte Liste mit je einem Satz
3. Den Focus-Control-Mechanismus in zwei Sätzen (Anonymisierung, warum)
4. Einen Verweis-Satz: "For the full prompt protocol, validation framework, and epistemological discussion, see \citet{Geiger2026SWR}."

**Kein** Minimalbeispiel nötig (Step 2, A1 schlägt eines vor -- das ist nice-to-have, nicht Pflicht). Die Reviewer brauchen den Algorithmus, nicht ein Tutorial.

### A3. Cluster als Idealtypen durchgängig -- zwei chirurgische Eingriffe (15 Minuten)

**Problem:** Zeile 470 sagt "Four distinct worldview types can be identified from the data" -- klingt wie emergente Cluster. Zeile 513 sagt "Weberian ideal types". Die Ambiguität ist ein bekannter Angriffspunkt.

**Fix 1:** Zeile 470 ändern:

Alt:
> "Four distinct worldview types can be identified from the data"

Neu:
> "Four heuristic worldview types -- ideal types in the Weberian sense -- were constructed from the data"

**Fix 2:** Table 5 Caption (Zeile 476) ändern:

Alt:
> "The four worldview types of the AI elite."

Neu:
> "Four heuristic worldview types of the AI elite (ideal-typical construction)."

Das reicht. Step 2 schlägt zusätzlich einen Satz bei Zeile 504 vor ("analytical condensations, not natural kinds") -- empfehlenswert, aber nicht Pflicht, weil der Gedanke bereits in Zeile 513 und im Validierungsabschnitt (Zeile 509ff.) ausführlich steht.

### A4. Mills-Zitat einbauen (5 Minuten)

**Problem:** Mills (1956) im Literaturverzeichnis, aber nirgends zitiert. Für ein Paper über Machteliten ist das ein sofort sichtbares Versäumnis.

**Fix:** In Section 5.4 (Zeile 695), nach dem Satz über AI Governance, einfügen:

> "This pattern echoes Mills' (\citeyear{Mills1956}) classic analysis of power elites: small, socially interconnected groups developing self-reinforcing worldviews that legitimize their structural position."

Ein Satz. Erledigt.

### A5. SU-IDs erklären (10 Minuten)

**Problem:** Deutsche Abkürzungen (GA_ges_AH, HOM_haeuf_A, GR_*_AH) in einem englischen Paper. Wirkt nachlässig.

**Fix:** Fußnote am Anfang von Appendix D (Zeile 1177) einfügen:

> "SU identifiers follow the German-language conventions of the companion paper \citep{Geiger2026SWR} and are retained for cross-reference consistency. Key abbreviations: GA = Gesamtanalyse (full sample), GR = Gruppenrolle (role group), GF = Gruppenfirma (company group), GH = Gruppenhaltung (stance group), GD = Gruppendemografie (demographic group), HOM = Homogenisierung (homogenization), AH/A/H = Aussagen+Handlungen / Aussagen / Handlungen (statements+actions / statements / actions)."

Pragmatischer als Umbenennung aller SU-IDs und konsistent mit dem Companion Paper.

### A6. Zirkuläre Kruskal-Wallis-Validierung offenlegen (5 Minuten)

**Problem:** Table 7 (Zeile 517--542) zeigt hoch-signifikante Kruskal-Wallis-Ergebnisse für D07 und D11 -- aber die Cluster wurden *auf diesen Dimensionen* gebildet. Das ist zirkulär. Aufmerksame quantitative Reviewer werden das sofort sehen.

**Fix:** Nach Zeile 542 einen Satz einfügen:

> "We note that the significance of D07 and D11 is partly tautological, since these dimensions informed the cluster construction. The non-trivial finding is that four *additional* dimensions (D02, D06, D09, D12) also discriminate significantly -- suggesting that the four types capture real variation beyond the defining axes."

Dieser Satz verwandelt eine versteckte Schwäche in ein explizites Argument.

---

**Zusammenfassung Pflicht-Korrekturen:** 6 Eingriffe, geschätzter Aufwand 3--4 Stunden. A2 (Methodik-Abschnitt) ist der einzige mit substantiellem Schreibaufwand.

---

## B: Empfohlene Verbesserungen (kein Blocker, aber R&R-Chancen erhöhend)

Die folgende Liste ist nach Aufwand-Wirkungs-Verhältnis sortiert: oben die Fixes mit maximalem Impact bei minimalem Aufwand.

### B1. Zahlen in den Abstract (15 Minuten)

Der Abstract nennt keinen einzigen Zahlenwert als Ergebnis. Kein $N$, kein $\Delta$, kein "3,132 data points". Zwei bis drei Schlüsselzahlen einbauen:

> "Based on 3,132 data points from 100 actors [...] a systematic say-do gap emerges, with the largest discrepancy in egalitarianism ($\Delta = -3$ on a 10-point scale) [...]"

### B2. Power-Operationalisierung schärfen (20 Minuten)

Table 6 (Zeile 600--611) zeigt nur "Highest / High / Medium / Lowest". Für die zentrale These (Power-Moderation Paradox) ist das zu vage. Einen Absatz nach Zeile 596 einfügen, der drei Proxies benennt: (1) kumulative Marktkapitalisierung der affiliierten Firmen, (2) direkte Kontrolle über Frontier-Compute-Infrastruktur, (3) Anzahl der Cluster-Mitglieder in der Time-100-AI-Rangliste. Keine exakten Zahlen nötig, aber die Rangordnung muss nachvollziehbar begründet werden.

### B3. Gender-Befund epistemisch herabstufen (15 Minuten)

In Zeile 583--584 den Satz ersetzen:

Alt:
> "The contamination caveat stated above applies with full force."

Neu:
> "This finding is classified as a **preliminary hypothesis requiring independent validation** (multi-LLM triangulation, expert ratings) before it can be interpreted substantively. We report it for completeness but caution against drawing policy conclusions from it."

Zusätzlich in Table 5 (Zeile 561) den Gender-Eintrag mit Fußnote versehen: "†Preliminary; see contamination caveat in Sections 4.4 and 5.2."

### B4. Mono-Provider-Reflexion (15 Minuten)

In den Limitations (Section 6.2) fehlt eine explizite Reflexion darüber, dass die *gesamte* Pipeline von einem einzigen LLM-Anbieter (Anthropic) abhängt. Die Anthropic-Zirkularität für *Personen* im Sample ist adressiert (Zeile 729), aber das Monokultur-Risiko für die Methode selbst nicht. Einen Absatz einfügen:

> "A structural limitation is the study's complete dependence on a single LLM provider (Anthropic). Any systematic bias specific to Claude would affect all findings without internal correction. This mono-provider dependency constitutes an additional argument for inter-LLM triangulation as a priority for future work."

### B5. Nullbefunde explizit framen (10 Minuten)

Alle sechs RQs produzieren positive Befunde. Das wirkt verdächtig. In der Discussion oder am Ende des Ergebnisteils die wichtigsten Nicht-Befunde als solche benennen:

> "Contrary to common assumption, the company comparison (Anthropic vs. OpenAI vs. Google) yielded the *smallest* group differences ($\Delta = 0.4$), suggesting that company affiliation matters less than ideological stance or institutional role."

Und:

> "Four of twelve dimensions (D01, D03, D08, D10) showed no significant inter-type differences -- these constitute the shared core of the AI elite worldview."

Letzteres steht bereits in Zeile 542, wird aber nicht als Nullbefund geframt.

### B6. Conclusion: Einen Satz Selbstkritik (5 Minuten)

Section 7.1 endet zu selbstbewusst. Nach dem fünften Insight einen sechsten Absatz:

> "These insights remain empirically grounded hypotheses, not proven facts. Whether they hold up under multi-LLM triangulation and external validation is an open question. The method works; the results await confirmation."

### B7. Kausal-Formulierung im Power-Paradox abschwächen (5 Minuten)

Zeile 613 schreibt: "Power intensifies all beliefs except those that question power itself" -- das impliziert Kausalität, die Section 5.5 (Zeile 705) formell ausschließt. Umformulieren:

> "At the group level, higher worldview intensity co-occurs with lower values for human appreciation and egalitarianism. Whether power shapes worldview, worldview attracts power, or both are driven by a third factor cannot be determined from the present data."

### B8. Section 3.5 gliedern (30 Minuten)

Section 3.5 (Quality Assurance) ist ein einziger, massiver Absatz (~400 Wörter) mit sechs verschiedenen Themen. Unterabschnitte einführen: 3.5.1 Run-Convergence, 3.5.2 Expected-Discrepancy Control, 3.5.3 Aggregation-Synthesis Comparison, 3.5.4 Cross-Modal Prediction, 3.5.5 Focus Control. Keine inhaltliche Änderung, nur Struktur.

### B9. Effektstärke-Benchmark für Say-Do-Gap (10 Minuten)

Table 4 berichtet $\Delta$-Werte ohne Bezugsrahmen. Die Expected-Discrepancy-Kontrolle (Zeile 731) liefert einen Benchmark: Real-Gap MAE = 1.25 vs. Kontroll-Gap MAE = 0.50, Ratio 2.5:1. Dieses Verhältnis prominenter als Kontextualisierung in den Text nach Table 4 einbauen:

> "For context: the real AI elite produces a mean absolute discrepancy 2.5 times larger than a synthetic control group designed to be congruent (MAE 1.25 vs. 0.50), confirming that the observed gap substantially exceeds the method's baseline noise."

### B10. Anthropic-Anteil quantifizieren (5 Minuten)

Zeile 729 diskutiert die Anthropic-Zirkularität ohne eine Zahl zu nennen. Reviewer werden fragen: Wie viele der 100 sind Anthropic-affiliiert? Ergänzen:

> "Of the 100 actors, [N] are directly affiliated with Anthropic, constituting [X]% of the total sample."

Wenn es 2--3 Personen sind, entkräftet die Zahl das Argument weitgehend.

---

## C: Abgelehnte Vorschläge aus Steps 1--3

### C1. Minimalbeispiel in den Methodik-Abschnitt (Step 2, A1) -- ABGELEHNT

Step 2 empfiehlt ein vereinfachtes Beispiel (3 Datenpunkte -> Ergebnis) im neuen Methodik-Abschnitt. Das bindet Platz und verlangsamt die Darstellung. Die formale Definition + 5-Schritte-Liste + Focus-Control-Erklärung reichen für ein Anwendungspaper. Ein Tutorial gehört ins Companion Paper, wo es bereits steht.

### C2. Section 5.5 verschieben (Step 3, B2) -- ABGELEHNT

Step 3 schlägt vor, Section 5.5 ("What the Study Does Not Show") an den Anfang von Section 5 oder in die Limitations zu verschieben. In der aktuellen Position nach den Societal Implications (5.4) funktioniert sie als Korrektiv nach dem ambitioniertesten Abschnitt -- das ist rhetorisch sinnvoll. Verschiebung an den Anfang würde die Discussion defensiv eröffnen; Integration in die Limitations würde den expliziten Charakter verwässern. Aktuelle Position beibehalten.

### C3. Section 5.3 (Alignment-Distinktion) verschieben (Step 3, D-Abschnitt) -- ABGELEHNT

Step 3 empfiehlt, Section 5.3 nach Section 5.4 zu verschieben. Das Argument (theoretisches Ergebnis der Implikationen) ist nachvollziehbar, aber die aktuelle Reihenfolge (5.2 Literatur -> 5.3 Alignment-Konzept -> 5.4 Implikationen) ist logischer: Erst wird das konzeptuelle Werkzeug eingeführt, dann werden damit Implikationen gezogen. Die Implikationen in 5.4 *nutzen* die Worldview/Agentic-Distinction implizit. Reihenfolge beibehalten.

### C4. "Western" in den Titel (Step 1, D5 / Step 2, B7) -- ABGELEHNT

"AI Elite" ist stärker und ehrlicher als "Western AI Elite". Die Studie analysiert nicht bewusst nur den Westen, sondern die *de facto* mächtigsten Akteure. Der geographische Scope ist in den Limitations (Zeile 720--721) korrekt adressiert. Titeleinschränkung signalisiert falschen Scope -- die Studie will die globale Machtelite analysieren, die zufällig überwiegend westlich ist.

### C5. Co-Autor suchen (Step 1, D4) -- ABGELEHNT

Wissenschaftsethisch problematisch: Gift Authorship. Die Arbeit ist von einem Einzelautor -- das ist transparent. Wenn die Methode und die Daten stark genug sind, spricht die institutionelle Ungebundenheit nicht gegen Akzeptanz. AI & Society beurteilt nach Inhalt, nicht nach Affiliation.

### C6. Limitations aufteilen in Haupttext und Appendix (Step 3, D-Abschnitt) -- ABGELEHNT

Step 3 schlägt vor, die 14 Limitations auf drei Prioritätsgruppen aufzuteilen und Gruppen (b) und (c) in den Appendix zu verschieben. Die umfassende Limitations-Section ist eine *Stärke* dieses Papers, nicht eine Schwäche. Sie signalisiert Reviewern: Der Autor kennt die Probleme. Kürzen würde den Eindruck der intellektuellen Ehrlichkeit schwächen, der das Paper bei methodisch skeptischen Reviewern schützt.

### C7. Diverging Bar Chart für Say-Do-Gap (Step 2, B3) -- WARTEN

Visuell besser, aber Fig. 6 funktioniert bereits. Kann nach einer eventuellen R&R nachgereicht werden, wenn Reviewer es anfordern. Kein Pre-Submission-Aufwand.

### C8. Historischer Vergleichshorizont (Step 1, C3 / Step 2, B5) -- WARTEN

Ein Absatz über Manhattan-Project-Physiker und Internet-Pioniere würde Tiefe hinzufügen. Aber: Er ist inhaltlich riskant (Vergleiche müssen historisch akkurat sein), bindet Recherche-Zeit, und ist kein Einreichungs-Blocker. Kann in einer R&R-Revision hinzugefügt werden, falls Reviewer es vorschlagen.

### C9. Worldview Dashboard / Deliberation Simulation / Spiegelexperiment (Step 1, C1-C4) -- ABGELEHNT

Alles eigenständige Projekte, keine Paper-Revisionen. Nicht vor Einreichung.

### C10. Prompt-Sensitivitäts-Diskussion (Step 3, B4) -- WARTEN

Methodisch korrekt, dass diese fehlt. Aber: Der Hinweis steht implizit im Companion Paper-Verweis und in den Limitations (Reproducibility, Zeile 744--745). Ein expliziter Satz wäre ideal, ist aber kein Ablehnungsgrund. In eine R&R einbauen.

### C11. Selection-Bias-Reflexion (Step 3, B6) -- WARTEN

Die Idee, dass die Influence-basierte Auswahl einen Visibility Bias einführt (laute Personen = extremere Weltbilder), ist klug. Der Punkt ist aber indirekt in "Sample dependence" (Zeile 722) adressiert. Kann bei R&R ergänzt werden.

### C12. Abbildungsreferenzen interpretieren (Step 3, B8) -- ABGELEHNT

Der Vorschlag, bei jeder Figurenreferenz einen interpretierenden Satz einzufügen, ist stilistisch eine Geschmacksfrage. Die Figures sind durch die Captions selbsterklärend. Kein wissenschaftlicher Mangel.

---

## D: Minimaler Einreichungsplan

### Phase 1: Pflicht-Fixes (halber Tag, in dieser Reihenfolge)

| Nr | Fix | Aufwand | Quelle |
|----|-----|---------|--------|
| 1 | A1: Op4-Widerspruch korrigieren (Tabelle 1 Fußnote) | 5 Min | Step 2, A7 |
| 2 | A4: Mills-Zitat einfügen (1 Satz, Section 5.4) | 5 Min | Step 1, B4 |
| 3 | A3: Cluster-Reframing (2 Stellen: Zeile 470 + Tab 5 Caption) | 15 Min | Step 2, A2 |
| 4 | A5: SU-ID-Fußnote (Appendix D) | 10 Min | Step 2, A6 |
| 5 | A6: Kruskal-Wallis-Zirkularität offenlegen (1 Satz, nach Zeile 542) | 5 Min | Step 2, D1 |
| 6 | A2: Methodik-Kurzabschnitt schreiben (ca. 1 Seite) | 2--3 Std | Step 1, B1 |

**Gesamtaufwand Phase 1:** ~3--4 Stunden.

### Phase 2: High-Impact-Quick-Fixes (parallel zu Phase 1 oder am nächsten Tag)

| Nr | Fix | Aufwand | Impact |
|----|-----|---------|--------|
| B1 | Zahlen in Abstract | 15 Min | Hoch |
| B3 | Gender-Befund herabstufen | 15 Min | Hoch |
| B6 | Conclusion-Selbstkritik (1 Satz) | 5 Min | Mittel |
| B7 | Kausalformulierung abschwächen | 5 Min | Mittel |
| B10 | Anthropic-Anteil quantifizieren | 5 Min | Mittel |
| B5 | Nullbefunde explizit framen | 10 Min | Mittel |

**Gesamtaufwand Phase 2:** ~1 Stunde.

### Phase 3: Strukturelle Verbesserungen (optional, wenn Zeit vorhanden)

| Nr | Fix | Aufwand |
|----|-----|---------|
| B2 | Power-Operationalisierung | 20 Min |
| B4 | Mono-Provider-Reflexion | 15 Min |
| B8 | Section 3.5 gliedern | 30 Min |
| B9 | Effektstärke-Benchmark | 10 Min |

**Gesamtaufwand Phase 3:** ~1,5 Stunden.

### Phase 4: Repository-Check (vor Einreichung, nicht-Paper)

- [ ] GitHub-Repository öffentlich schalten
- [ ] README mit Reproduktionsanleitung
- [ ] Alle Prompts archiviert
- [ ] $100 \times 12$ Rating-Matrix vorhanden
- [ ] Optional: Zenodo-DOI für Datensatz

### Mindest-Einreichungsplan:

**Phase 1 allein** reicht für eine Einreichung bei AI & Society. Der Score steigt damit von 6.5 auf 7.5.

**Phase 1 + Phase 2** ist die empfohlene Minimalvariante. Score: 8+. Aufwand: ein Tag.

**Phase 1 + Phase 2 + Phase 3** maximiert die R&R-Wahrscheinlichkeit. Score: 8.5. Aufwand: anderthalb Tage.

---

## E: Readiness-Score

### Aktueller Stand (ohne Fixes): 6.5/10

Konsistent mit Step 2. Die Stärken sind real (Originalität, Transparenz, Befundtiefe), aber der Op4-Widerspruch, die fehlende Methodik-Eigenständigkeit und die Cluster-Ambiguität sind Stolperfallen für aufmerksame Reviewer.

### Nach Phase 1 (Pflicht-Fixes): 7.5/10

Die sechs strukturellen Schwachstellen sind beseitigt. Das Paper ist einreichungsfähig.

### Nach Phase 1 + 2 (empfohlene Minimalvariante): 8.0/10

Das Paper präsentiert sich nun als sorgfältig, epistemisch diszipliniert und selbstkritisch -- genau die Qualitäten, die bei AI & Society honoriert werden.

### Nach Phase 1 + 2 + 3 (vollständig): 8.5/10

Alle von drei unabhängigen Reviews identifizierten Schwachstellen sind adressiert.

### Was für 9--10 fehlt (und nicht in Tagen behebbar ist):

- Inter-LLM-Triangulation (mindestens ein Vergleichsmodell)
- Externe Expertenvalidierung (unabhängige Coder)
- Leave-k-out-Sensitivitätsanalyse für Samplezusammensetzung
- Systematische Prompt-Sensitivitätsanalyse

Diese vier Punkte sind R&R-Ziele, keine Pre-Submission-Aufgaben.

### Prognose bei Einreichung (AI & Society, nach Phase 1+2):

- **Revise & Resubmit: 55--65%** (Reviewer fordern Inter-LLM-Triangulation und externe Validierung)
- **Ablehnung: 20--30%** (Grund: "keine echte Empirie")
- **Akzeptanz ohne Major Revision: 5--15%**

Ein R&R wäre ein ausgezeichnetes Ergebnis für ein methodisch innovatives Paper eines Independent Researchers bei der Ersteinreichung.

---

### Konsens-Matrix: Was die vier Reviews gemeinsam sagen

| Punkt | Step 1 | Step 2 | Step 3 | Step 4 (hier) | Entscheidung |
|-------|--------|--------|--------|----------------|--------------|
| Methodik-Eigenständigkeit | B1 (Pflicht) | A1 (Pflicht) | A (bestätigt) | A2 (Pflicht) | **PFLICHT** |
| Cluster-Reframing | B2 (Pflicht) | A2 (Pflicht) | A (bestätigt) | A3 (Pflicht) | **PFLICHT** |
| Mills-Zitat | B4 (Pflicht) | A3 (Pflicht) | -- | A4 (Pflicht) | **PFLICHT** |
| Op4-Widerspruch | -- | A7 (Pflicht) | A (bestätigt) | A1 (Pflicht) | **PFLICHT** |
| SU-IDs | B7 (Pflicht) | A6 (Pflicht) | -- | A5 (Pflicht) | **PFLICHT** |
| Gender herabstufen | B3 (Pflicht) | A5 (Pflicht) | -- | B3 (empfohlen) | **EMPFOHLEN** |
| Power-Proxies | B5 (Pflicht) | A4 (Pflicht) | A (bestätigt) | B2 (empfohlen) | **EMPFOHLEN** |
| KW-Zirkularität | -- | D1 (neu) | -- | A6 (Pflicht) | **PFLICHT** |
| Mono-Provider | -- | -- | B3 (empfohlen) | B4 (empfohlen) | **EMPFOHLEN** |
| Abstract-Zahlen | B9 (empfohlen) | B1 (empfohlen) | B1 (empfohlen) | B1 (empfohlen) | **EMPFOHLEN** |
| "Western" im Titel | D5 (antizipiert) | B7 (optional) | -- | C4 (abgelehnt) | **ABGELEHNT** |
| Co-Autor suchen | D4 (antizipiert) | C7 (abgelehnt) | -- | C5 (abgelehnt) | **ABGELEHNT** |

---

*Reviewer-Profil: Führender Fachexperte, zweite Runde. Fokus auf minimalem, machbarem Einreichungsplan. Ziel: von 6.5 auf 8+ mit einem Tag Arbeit.*
