# Konstruktives Review -- Runde 2: Worldview Reconstruction of the AI Elite

**Reviewer-Perspektive:** Zweite Runde, konstruktiv. Annahme: Pflicht-Korrekturen A1--A7 aus Step 2 wurden umgesetzt.
**Datum:** 2026-03-30
**Dokument:** KI_Elite_v2_en.tex (englische Version)
**Vorgänger:** Step1_konstruktiv.md, Step2_experte.md

---

## A: Was hat sich verbessert? (Annahme: A1--A7 umgesetzt)

1. **Eigenständiger Methodik-Abschnitt (A1).** Wenn Section 3.2 nun einen ca. 1,5-seitigen Unterabschnitt "The SWR Procedure in Brief" enthält, der das inverse Problem, die fünf Schritte, ein Minimalbeispiel und den Focus-Control-Mechanismus erklärt, dann ist die größte strukturelle Schwäche des Papers beseitigt. Das Paper wird als Stand-alone-Einreichung beurteilbar -- vorher war das nicht der Fall.

2. **Idealtypen-Framing durchgängig (A2).** Die konsequente Bezeichnung als "heuristic worldview types -- ideal types in the Weberian sense" in Zeile 470, die Ergänzung "analytical condensations, not natural kinds" bei RQ4, und die angepasste Table-5-Caption beseitigen die epistemische Ambiguität, die quantitativ orientierte Reviewer sofort angegriffen hätten. Das ist ein wesentlicher Schutzschild.

3. **Mills im Text (A3).** Die Einbindung von Mills (1956) in die Discussion (Section 5.4) schließt eine offensichtliche Lücke. Das Paper analysiert eine Machtelite -- den kanonischen Referenztext dafür nicht zu zitieren, wäre für jeden soziologisch geschulten Reviewer ein Störsignal gewesen.

4. **Power-Operationalisierung (A4).** Die Ergänzung konkreter Proxies (Marktkapitalisierung, Frontier-Compute-Kontrolle, Time 100 AI) in Table 6 oder als Textpassage gibt der zentralen These (Power-Moderation Paradox) die empirische Bodenhaftung, die vorher fehlte. Der Unterschied zwischen "Highest" und konkreten Indikatoren ist erheblich.

5. **Gender-Befund herabgestuft (A5).** Die Fußnote in Table 5 und die verschärfte Formulierung ("preliminary hypothesis requiring independent validation") entschärfen das prominenteste Angriffsziel des Papers. Der Befund bleibt berichtet (keine Datensuppression), wird aber epistemisch korrekt eingeordnet.

6. **SU-IDs erklärt (A6).** Die Übersetzungstabelle oder Fußnote zu den deutschen Abkürzungen beseitigt den "sloppy work"-Eindruck, der bei einem englischsprachigen Paper mit deutschen Labels entsteht.

7. **Op4-Inkonsistenz behoben (A7).** Die Korrektur der Tabelle-1-Fußnote (von "not conducted" zu "conducted as validation experiment but not as systematic operationalization") beseitigt einen faktischen Widerspruch, der die Glaubwürdigkeit des gesamten Qualitätssicherungsabschnitts untergraben hätte.

**Gesamteinschätzung der Step-2-Korrekturen:** Alle sieben Fixes adressieren reale Schwachstellen. Keine der Korrekturen ist kosmetisch; jede erhöht die Reviewer-Resistenz des Papers messbar.

---

## B: Verbleibende Vorschläge (neue Perspektive)

Die folgenden Punkte wurden weder in Step 1 noch in Step 2 adressiert.

### B1. Der Abstract enthält keinen einzigen Zahlenwert als Ergebnis

**Problem:** Der Abstract (Zeile 91--97) beschreibt die Methode und die konzeptionellen Befunde (technological messianism, say-do gap, four types, power-moderation paradox), nennt aber keine einzige konkrete Zahl als Ergebnis. Kein $\Delta = -3$, kein $N = 100$, kein "3,132 data points", kein "88% cross-modal confirmation". Reviewer und Leser, die nur den Abstract scannen, bekommen keinen Eindruck davon, wie substanziell die Befunde sind.

**Empfehlung:** Zwei bis drei Schlüsselzahlen in den Abstract einbauen. Beispiel: "A systematic say-do gap emerges at the group level, with the largest discrepancy in egalitarianism ($\Delta = -3$ on a 10-point scale). [...] Based on 3,132 data points from 100 actors spanning 16 years [...]." Das verankert die Befunde und signalisiert empirische Substanz.

### B2. Section 5.5 ("What the Study Does Not Show") steht am falschen Ort

**Problem:** Diese Passage (Zeile 702--705) mit den fünf expliziten Negationen ist ein starkes Element der intellektuellen Ehrlichkeit. Aber sie steht mitten in der Discussion, zwischen den Societal Implications (5.4) und den Limitations (6). Funktional gehört sie entweder an den Anfang der Discussion (als Rahmen für alles Folgende) oder in die Limitations. In der aktuellen Position unterbricht sie den Argumentationsfluss.

**Empfehlung:** Section 5.5 an den Anfang von Section 5 verschieben (vor 5.1 Summary and Interpretation) und als einleitenden Disclaimer framen: "Before interpreting the findings, it is essential to state explicitly what the study does *not* show." Oder alternativ: in Section 6 (Limitations) als eigenen Unterabschnitt integrieren.

### B3. Fehlende Reflexion über die Rolle des LLM-Herstellers im Forschungsdesign

**Problem:** Section 8 (AI Disclosure, Zeile 839--843) beschreibt den Einsatz von Claude Sonnet 4.5 und Claude Opus 4.6 detailliert. Aber es fehlt eine Reflexion darüber, dass die *gesamte* analytische Pipeline von Produkten *eines einzigen Herstellers* (Anthropic) abhängt. Das ist nicht nur ein Contamination-Problem (Step 2, Zeile 729), sondern ein *Monokultur-Risiko*: Wenn Claude systematische Biases hat (und jedes LLM hat sie), durchziehen diese die gesamte Studie -- von der Datenerhebung über die Ratings bis zur Validierung. Step 2 adressiert die Anthropic-Zirkularität für die *Personen* im Sample, aber nicht für die methodische Monokultur.

**Empfehlung:** In den Limitations (Section 6.2) einen expliziten Absatz ergänzen:

> "A structural limitation of the present study is its complete dependence on a single LLM provider (Anthropic). All data processing -- individual ratings, group syntheses, statistical analyses, validation experiments -- was conducted using Claude models. Any systematic bias specific to Claude (as opposed to LLMs in general) would therefore affect all findings without internal correction. This mono-provider dependency is distinct from the contamination risk discussed above and constitutes an additional argument for inter-LLM triangulation as a priority for future work."

### B4. Keine Diskussion der Prompt-Sensitivität

**Problem:** Das Paper dokumentiert vorbildlich die Verwendung von temperature=0 und verweist auf die Prompt-Dokumentation im Repository. Aber es fehlt jede Diskussion darüber, wie sensitiv die Ergebnisse gegenüber Prompt-Variationen sind. Was passiert, wenn die Rating-Frage anders formuliert wird? Wenn die Reihenfolge der Dimensionen geändert wird? Wenn der System-Prompt variiert? Das Companion Paper mag dies adressieren, aber ein eigenständig beurteilbares Paper sollte zumindest die Frage aufwerfen.

**Empfehlung:** In Section 3.5 (Quality Assurance) oder in den Limitations einen kurzen Hinweis:

> "Prompt sensitivity -- the degree to which results depend on specific prompt formulations -- was not systematically tested in this study. The prompt protocol follows the standardized templates of the SWR framework (cf. companion paper), and all prompts are archived in the repository. A systematic prompt-variation analysis would complement the run-convergence test and is recommended for future applications of the method."

### B5. Der Ergebnisteil enthält keine Nullbefunde

**Problem:** Alle sechs Forschungsfragen produzieren positive Befunde. Der Say-Do Gap existiert, die Cluster sind unterscheidbar, das Power-Moderation Paradox ist sichtbar. Aber wo sind die *erwarteten* Befunde, die sich *nicht* zeigten? Haben die Autoren Hypothesen gehabt, die sich nicht bestätigten? Gab es Gruppenvergleiche, die keine Unterschiede zeigten? Die Abwesenheit von Nullbefunden wirkt in der empirischen Forschung verdächtig -- nicht weil sie auf Betrug hindeutet, sondern weil sie den Eindruck erweckt, dass nur "passende" Ergebnisse berichtet werden.

**Empfehlung:** In der Discussion oder in einem kurzen Absatz am Ende des Ergebnisteils die wichtigsten Nicht-Befunde benennen. Beispiele: "Contrary to expectation, the company comparison (Anthropic vs. OpenAI vs. Google) yielded the *smallest* group differences ($\Delta = 0.4$), suggesting that company affiliation matters less than ideological stance or institutional role." Oder: "Four of twelve dimensions (D01, D03, D08, D10) showed no significant inter-type differences -- these constitute the shared core of the AI elite worldview." (Letzteres steht zwar in Zeile 542, wird aber nicht als *Nullbefund* geframt, sondern als Nebenbeobachtung.)

### B6. Fehlende Diskussion des Selection-Bias bei der Stichprobenauswahl

**Problem:** Section 6.1 nennt den "Sample dependence" als Limitation (Zeile 722) und erwähnt die subjektive Scoring-Prozedur. Aber es fehlt eine Reflexion über einen tieferen Bias: Die 100 Personen wurden nach *Einfluss* ausgewählt. Einfluss korreliert mit Sichtbarkeit, Sichtbarkeit korreliert mit starken Meinungen, starke Meinungen korrelieren mit extremen Werten auf Weltbild-Dimensionen. Die gesamte Studie ist also möglicherweise verzerrt in Richtung *intensivere* Weltbilder -- nicht weil die AI-Elite tatsächlich so denkt, sondern weil die Auswahlprozedur Personen mit starken öffentlichen Positionen bevorzugt.

**Empfehlung:** In Section 6.1 ergänzen:

> "The influence-based selection procedure may introduce a visibility bias: the most influential actors tend to be the most publicly vocal, which could inflate the reconstructed intensity of collective worldviews. The overall mean of 7.1 on a 10-point scale may partly reflect this selection effect rather than the true central tendency of the broader AI leadership community."

### B7. Die Conclusion enthält keine Selbstkritik

**Problem:** Section 7.1 (Conclusion, Zeile 819--830) fasst fünf "overarching insights" zusammen -- alle positiv formuliert. Es fehlt ein einziger Satz, der die Grenzen des Erreichten anerkennt. Die Limitations stehen in Section 6, aber die Conclusion liest sich so, als seien alle Befunde gesichert. Für ein Paper, das so vorbildlich transparent über seine Grenzen ist, endet die Conclusion zu selbstbewusst.

**Empfehlung:** Nach dem fünften Insight einen sechsten Absatz einfügen:

> "These five insights remain, at this stage, empirically grounded hypotheses -- not proven facts. The study's primary contribution is to demonstrate that systematic group-level worldview analysis is *feasible* and yields *interpretable* results. Whether the specific findings hold up under multi-LLM triangulation, external expert validation, and cross-cultural replication is an open question. The method works; the results await confirmation."

### B8. Abbildungsreferenzen ohne Kontextintegration

**Problem:** Die Figuren (Fig. 1--7) werden referenziert, aber in einigen Fällen nur als Verweis ("see Fig. X"), ohne dass die visuelle Information im Fließtext interpretiert wird. Besonders Fig. 4 (Korrelationsmatrix, Zeile 393) und Fig. 5 (Gruppen-Heatmap, Zeile 572) werden aufgerufen, ohne dass die *visuell* sichtbaren Muster im Text beschrieben werden. Reviewer lesen Figures oft erst nach dem Text -- wenn der Text allein nicht ausreicht, fehlt Information.

**Empfehlung:** Bei jeder Figure-Referenz mindestens einen Satz einfügen, der beschreibt, was der Leser sehen soll. Beispiel bei Fig. 5: "The group heatmap (Fig. 5) reveals a consistent visual pattern: D07 and D11 form the vertical axes of maximal variation across all 15 groups, while D01, D03, and D08 show near-uniform coloring -- the shared core."

---

## C: Journal-Empfehlung

### Kriterien: Einfachheit der Einreichung > Impact

| Kriterium | Gewichtung |
|-----------|------------|
| Thematische Passung | Hoch |
| Offenheit für methodische Innovation | Hoch |
| Toleranz für Independent Researchers | Hoch |
| Einfachheit des Einreichungsprozesses | Hoch |
| Impact Factor | Mittel |
| Bearbeitungsdauer | Mittel |

### Empfehlung: **AI & Society** (Springer)

**Begründung:**

1. **Thematische Passung: perfekt.** AI & Society publiziert explizit an der Schnittstelle von AI, Gesellschaft und Ethik. Das Paper adressiert exakt diesen Nexus. Die Zeitschrift hat Erfahrung mit interdisziplinären Arbeiten, die soziologische, politikwissenschaftliche und technische Perspektiven verbinden.

2. **Methodische Offenheit: hoch.** AI & Society publiziert qualitative, quantitative und Mixed-Methods-Arbeiten. LLM-basierte Methoden sind kein Ausschlusskriterium -- im Gegenteil, die Zeitschrift hat in den letzten zwei Jahren mehrfach Papers zu LLMs als Forschungsinstrumenten veröffentlicht.

3. **Independent Researcher: kein Problem.** Springer-Journals bewerten nach inhaltlichen Kriterien, nicht nach institutioneller Zugehörigkeit. AI & Society hat historisch auch nicht-universitäre Autoren publiziert.

4. **Einreichungsprozess: Standard-Springer.** Editorial Manager, kein Formatting-Zwang bei Ersteinreichung (LaTeX oder Word), kein Page-Limit für Research Articles. Das Paper kann in seiner aktuellen Form eingereicht werden (nach den A1--A7-Fixes).

5. **Impact Factor: ~3.5** -- nicht herausragend, aber respektabel. Für ein methodisch innovatives Paper eines Independent Researchers ein realistisches Ziel.

6. **Bearbeitungsdauer:** Typisch 3--6 Monate bis zur ersten Entscheidung.

### Alternativen (nach Priorität):

**2. Big Data & Society (SAGE, IF ~7.4).** Höherer Impact, aber strengere quantitative Reviewer. Das Paper müsste hier stärker gegen die "keine echte Empirie"-Kritik bestehen. Die Stärke: BDS publiziert explizit "provocative" Arbeiten. Das Power-Moderation Paradox und die Say-Do-Gap-Analyse wären hier gut aufgehoben. Risiko: Ablehnung wegen methodischer Bedenken durch quantitativ orientierte Reviewer.

**3. Science, Technology & Human Values (SAGE, IF ~5.3).** STS-Perspektive passt gut; die Bourdieu/Weber-Einbettung ist hier ein Plus. Aber: Die Zeitschrift tendiert zu etablierten Methoden. LLM-basierte Analyse wäre methodisches Neuland -- riskant, aber mit hohem Gewinn bei Akzeptanz.

**4. Social Science Computer Review (SAGE, IF ~4.1).** Fokus auf Computational Social Science. Methodisch die beste Passung, aber: Das Paper ist primär substanziell (Was denkt die AI-Elite?), nicht primär methodisch (Wie funktioniert SWR?). Für ein Methoden-Paper wäre SSCR ideal; für dieses Anwendungs-Paper ist AI & Society besser.

**5. Konferenz-Alternative: FAccT oder AIES.** Als Long Paper (8--12 Seiten + Appendix). Vorteil: Schnelles Peer Review (3 Monate), hohe Sichtbarkeit in der AI-Governance-Community. Nachteil: Stark komprimiertes Format; das Paper müsste auf die Hälfte gekürzt werden. Nur empfehlenswert, wenn das Journal-Verfahren zu lange dauert.

**Nicht empfohlen:** Sociological Methods & Research (zu methodenfokussiert für dieses Anwendungspapier), Nature Human Behaviour (unrealistisch ohne institutionelle Anbindung und externe Validierung), PNAS (braucht NAS-Mitglied als Kommunikator).

### Strategie-Empfehlung:

Einreichung bei **AI & Society** als Erstversuch. Falls Ablehnung: sofort weiter zu **Big Data & Society**. Das Paper ist thematisch stark genug für beide Zeitschriften; der Unterschied liegt im methodischen Risikoprofil.

---

## D: Narrative Analyse -- Der rote Faden

### Wo der rote Faden klar ist:

1. **Introduction (Section 1):** Exzellent strukturiert. Der Dreischritt "Relevanz -- Lücke -- Forschungsfragen" ist sauber und überzeugend. Die sechs Forschungsfragen bauen logisch aufeinander auf (deskriptiv -- longitudinal -- validierend -- explorativ -- komparativ -- normativ). Kein Leser verliert hier den Überblick.

2. **Results RQ1--RQ3 (Sections 4.1--4.3):** Klarer narrativer Bogen. Vom Gesamtprofil (RQ1) über die zeitliche Entwicklung (RQ2) zur Kongruenzprüfung (RQ3). Jeder Schritt baut auf dem vorherigen auf. Die "Core Findings" am Ende jeder Section funktionieren als Wegweiser.

3. **Discussion Section 5.1--5.2:** Die Zusammenfassung und Literatureinordnung sind prägnant und effektiv. Die Verbindung zu Morozov, Daub, TESCREAL und Bourdieu ist nicht dekorativ, sondern operativ.

### Wo der Leser den Überblick verliert:

1. **Section 3.5 (Quality Assurance) ist zu lang und zu dicht.** Der Absatz ab Zeile 283 enthält *alle* Validierungsmaßnahmen in einem einzigen, ungegliederten Textblock: Run-Convergence, Expected-Discrepancy, Aggregation-Synthesis, Cross-Modal Prediction, plus die Erklärung der Claude-Modelle, plus Focus Control. Das sind sechs verschiedene Themen in einem Absatz. Ein Reviewer, der nach der Run-Convergence-Zahl sucht, muss durch ~400 Wörter scrollen.

   **Empfehlung:** Section 3.5 in Unterabschnitte gliedern: 3.5.1 Run-Convergence, 3.5.2 Expected-Discrepancy Control, 3.5.3 Aggregation-Synthesis Comparison, 3.5.4 Cross-Modal Prediction, 3.5.5 Focus Control and Model Specification. Das ist keine inhaltliche Änderung, nur Strukturierung.

2. **Der Übergang von RQ4 zu RQ5 (Sections 4.4 zu 4.5) ist narrativ holprig.** RQ4 stellt die vier Typen vor, dann folgt die algorithmische Validierung (HDBSCAN, Silhouette-Scores), und dann springt RQ5 zu den Subgroup-Vergleichen. Das Problem: Der Leser weiß nach RQ4+Validierung nicht, ob die Cluster "gelten" oder nicht. Die Validierung relativiert die Cluster (Silhouette 0.169 im Vollraum), aber RQ5 verwendet die Cluster dann als gesetztes Ergebnis. Der narrative Bruch liegt darin, dass die Relativierung im Validierungsabschnitt steht, aber die *Nutzung* der Cluster im nächsten Abschnitt selbstverständlich fortfährt.

   **Empfehlung:** Einen Übergangssatz am Ende von Section 4.4 einfügen: "Despite their heuristic character, the four types serve as an analytically useful framework for the inter-group comparisons that follow. The question shifts from 'Are these real clusters?' to 'Do different structural positions produce systematically different collective worldviews?'" Das gibt dem Leser Orientierung für den Wechsel von der Cluster-Frage zur Vergleichs-Frage.

3. **Section 5.3 (Agentic vs. Worldview Alignment) wirkt wie ein Einschub.** Das Konzept ist brillant, wird aber in der Discussion zwischen der methodischen Reflexion (5.2) und den politischen Implikationen (5.4) eingeklemmt. Es liest sich wie ein eigenständiger Essay-Absatz, der in die Discussion eingepflanzt wurde. Der Leser fragt sich: Wohin gehört das?

   **Empfehlung:** Section 5.3 *nach* Section 5.4 verschieben (also: 5.1 Summary, 5.2 Literature, 5.3 Implications, 5.4 Alignment-Distinction, 5.5 Methodological Reflection). Die Alignment-Diskussion ist das *theoretische Ergebnis* der Implikationen -- sie sollte nach der empirischen Einordnung stehen, nicht davor.

4. **Die Limitations (Section 6) sind so umfangreich, dass sie den Leser erschlagen.** Section 6 enthält 14 verschiedene Limitationen über ca. 3 Seiten. Das ist intellektuell ehrlich, aber narrativ kontraproduktiv: Nach dem Lesen der Limitations hat der Leser das Gefühl, dass die Studie mehr Probleme hat als Ergebnisse. Die Conclusion (Section 7) muss dann dagegen anarbeiten.

   **Empfehlung:** Die Limitations in drei Gruppen priorisieren: (a) Kernlimitationen (3--4 Punkte, die jeder Leser kennen muss: Monokultur-Abhängigkeit, fehlende Inter-LLM-Triangulation, Coherence Bias, Sample-Dependence), (b) technische Limitationen (die restlichen, die für Methodenexperten relevant sind), (c) konzeptuelle Limitationen (Aggregation, keine Kausalerklärung). Gruppe (a) im Haupttext, Gruppen (b) und (c) in einem Appendix. Das kürzt die Limitations auf eine Seite und erhöht die Lesbarkeit, ohne Informationen zu unterdrücken.

### Gesamturteil zum roten Faden:

Der rote Faden ist **grundsätzlich klar und überzeugend**. Die Architektur (6 RQs als Progression) funktioniert. Die Schwächen liegen nicht im *Fehlen* eines roten Fadens, sondern in punktuellen *Unterbrechungen*: zu dichte Textblöcke (3.5), fehlende Übergangssätze (4.4/4.5), ein eingeschobener Exkurs (5.3), und ein überladener Limitations-Abschnitt (6). Alle diese Punkte sind durch Umstrukturierung ohne inhaltliche Änderungen behebbar.

---

## E: Readiness-Score

### Score: 7.5/10 (unter Annahme, dass A1--A7 umgesetzt wurden)

**Begründung:**

Die Step-2-Korrekturen (A1--A7) beseitigen die gravierendsten Schwachstellen: die methodische Blackbox (A1), die epistemische Ambiguität der Cluster (A2), den fehlenden Mills-Bezug (A3), die vage Power-Operationalisierung (A4), den prominenten Gender-Befund (A5), die deutschen Labels (A6) und den Op4-Widerspruch (A7). Ohne diese Korrekturen läge der Score bei 6--6.5 (in Übereinstimmung mit Step 2). Mit diesen Korrekturen ist das Paper einreichungsfähig.

**Was für 7.5 spricht:**

- **Konzeptionelle Stärke:** Die Forschungsfrage ist originell, gesellschaftlich relevant und adressiert eine genuine Lücke. Kein anderes Paper tut das, was dieses Paper tut.
- **Vorbildliche Transparenz:** Die epistemischen Disclaimer sind konsequent und ehrlich. Das ist selten und wird von guten Reviewern honoriert.
- **Starke Befundstruktur:** Say-Do Gap, Power-Moderation Paradox und die Vier-Typen-Lösung sind inhaltlich überzeugend und haben Anschlussfähigkeit.
- **Theoretische Einbettung:** Weber, Bourdieu, Ricoeur, Mills (nach A3) -- nicht dekorativ, sondern operativ genutzt.
- **Datenvolumen:** 3.132 Datenpunkte, 100 Akteure, 16 Jahre, 15 Gruppen -- das ist beeindruckend.

**Was für 9--10 fehlt (strukturell):**

- **Inter-LLM-Triangulation.** Das Fehlen eines Vergleichsmodells bleibt die größte methodische Flanke. Kein noch so guter Disclaimer kompensiert vollständig das Fehlen einer unabhängigen Replikation.
- **Externe Validierung.** Die Spot-Checks (Section 6.5) sind ein Anfang, aber keine systematische externe Validierung durch unabhängige Experten.
- **Prompt-Sensitivitätsanalyse.** Wie robust sind die Ergebnisse gegenüber Prompt-Variationen? Unbekannt.

**Was für 9--10 fehlt (behebbar in 1--2 Wochen):**

- Die in Abschnitt B beschriebenen Verbesserungen (Abstract-Zahlen, Section-5.5-Verschiebung, Mono-Provider-Reflexion, Nullbefunde, Selection-Bias-Reflexion, Conclusion-Selbstkritik, Section-3.5-Gliederung).
- Diese Punkte würden den Score auf **8--8.5** heben.

**Empfohlener Workflow:**

1. A1--A7 sicherstellen (falls noch nicht umgesetzt)
2. B1--B8 aus diesem Review priorisieren: B1 (Abstract-Zahlen), B3 (Mono-Provider), B5 (Nullbefunde) und B7 (Conclusion-Selbstkritik) haben das beste Aufwand-Wirkung-Verhältnis
3. Narrative Fixes aus Section D umsetzen (insbesondere Section 3.5 gliedern)
4. Einreichen bei AI & Society

**Prognose bei Einreichung (mit A1--A7 + den wichtigsten B-Fixes):**

- **Revise & Resubmit: 55--65%** (wahrscheinlichstes Ergebnis; Reviewer werden Inter-LLM-Triangulation und externe Validierung als Revisionsziel formulieren)
- **Ablehnung: 20--30%** (wahrscheinlichster Grund: "keine echte Empirie")
- **Akzeptanz ohne Major Revision: 5--15%** (unwahrscheinlich beim Erstversuch)

Ein Revise & Resubmit wäre ein ausgezeichnetes Ergebnis für ein methodisch innovatives Paper eines Independent Researchers.

---

*Reviewer-Profil: Konstruktiv, zweite Runde. Fokus auf narrative Kohärenz, neue Perspektiven und Journal-Strategie. Ziel ist Einreichungsreife.*
