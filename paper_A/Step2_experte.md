# Experten-Review: Worldview Reconstruction of the AI Elite

**Reviewer-Perspektive:** Führender Fachexperte für Computational Social Science und LLM-basierte Forschungsmethoden
**Datum:** 2026-03-30
**Dokument:** KI_Elite_v2_en.tex (englische Version)
**Vorgänger:** Step1_konstruktiv.md (konstruktives Review)

---

## A: Pflicht-Korrekturen (vor Einreichung zwingend)

### A1. Eigenständiger Methodik-Abschnitt (bestätigt Step-1, B1 -- kritischster Punkt)

**Problem:** Section 3.2 umfasst ca. einen Absatz zur SWR-Kernlogik. Für Reviewer, die das Companion Paper nicht kennen, ist die Methode eine Black Box. Das ist der wahrscheinlichste Ablehnungsgrund.

**Fix:** In Section 3.2 einen eigenständigen Unterabschnitt einfügen (ca. 1.5 Seiten), der folgende Elemente enthält:
1. Das inverse Problem formal definieren: "Gegeben: beobachtbare Outputs $O = \{s_1, ..., s_n, a_1, ..., a_m\}$ einer Gruppe $G$. Gesucht: das latente Überzeugungssystem $W$ das $O$ am kohärentesten erzeugt."
2. Die fünf SWR-Schritte als nummerierte Prozedur mit je 2-3 Sätzen
3. Ein Minimalbeispiel (z.B. eine vereinfachte Gruppen-Synthese mit 3 Datenpunkten → Ergebnis)
4. Den Focus-Control-Mechanismus (Anonymisierung) in 3-4 Sätzen erklären

**Wo genau:** Nach Zeile 223, vor Section 3.2.1 (Data Aggregation Procedure). Neuer Unterabschnitt: `\subsubsection{The SWR Procedure in Brief}`.

### A2. Cluster als Idealtypen durchgängig framen (bestätigt Step-1, B2 -- aber radikaler)

**Problem:** Das Paper schwankt zwischen zwei epistemischen Registern: Zeile 470 nennt die Typen "distinct worldview types" (klingt nach emergenten Clustern), Zeile 513 sagt "Weberian ideal types" (klingt nach heuristischer Konstruktion). Diese Ambiguität wird von quantitativ orientierten Reviewern als interne Inkonsistenz gewertet.

**Fix:** Drei Stellen ändern:

1. **Zeile 470**, ändern von:
   > "Four distinct worldview types can be identified from the data"

   zu:
   > "Four heuristic worldview types -- ideal types in the Weberian sense -- were constructed from the data"

2. **Zeile 504**, den Satz nach "Core finding RQ4" ergänzen:
   > "These types are analytical condensations, not natural kinds; their utility lies in rendering the multidimensional continuum interpretable, not in claiming discrete population segments."

3. **Table 5 Caption (Zeile 477)**, ändern von:
   > "The four worldview types of the AI elite."

   zu:
   > "Four heuristic worldview types of the AI elite (ideal-typical construction)."

### A3. Mills-Referenz im Text einbauen (bestätigt Step-1, B4)

**Problem:** Mills (1956) steht im Literaturverzeichnis (Zeile 1090), wird aber nirgends zitiert. Das ist für Reviewer ein sofort sichtbares Versäumnis -- *The Power Elite* ist die kanonische Referenz für genau dieses Thema.

**Fix:** In Section 5.4 (Societal and Political Implications, Zeile 695), nach dem Satz über das Power-Moderation Paradox einfügen:

> "This finding resonates with Mills' (\citeyear{Mills1956}) classic analysis of power elites: small, socially interconnected groups that develop self-reinforcing worldviews legitimizing their structural position -- a pattern that the inter-group comparisons (RQ5--RQ6) now document empirically for the AI field."

### A4. Power-Operationalisierung schärfen (bestätigt Step-1, B5 -- aber konkreter)

**Problem:** Zeile 595-596 definiert Power als "resource control", Table 6 ordnet nur "Highest / High / Medium / Lowest" zu. Das ist zu vage für die zentrale These des Papers (Power-Moderation Paradox).

**Fix:** Table 6 (Zeile 600-611) um eine Spalte "Proxy indicators" erweitern:

| Type | Resources | Proxy indicators |
|------|-----------|-----------------|
| I Architect | Highest | Cumulative market cap of affiliated firms >$5T; 8/10 Top-10 members; controls >80% of frontier compute |
| III Innovator | High | Startup valuations $1B--$50B; venture capital access; 6/22 founded unicorns |
| IV Liberator | Medium | VC firms + OSS governance; indirect influence via investment and code |
| II Guardian | Lowest | Academic positions, advisory roles; influence through publications and public discourse, not capital |

Alternativ im Text nach Zeile 596 einen Absatz einfügen:

> "The ordinal ranking is operationalized through three proxies: (1) cumulative market capitalization of firms in which cluster members hold leadership positions, (2) direct control over frontier compute infrastructure, and (3) number of cluster members in the Time 100 AI ranking. By all three measures, Type I dominates; Type II controls effectively no commercial resources."

### A5. Gender-Befund herabstufen (bestätigt Step-1, B3 -- aber pragmatischer)

**Problem:** Der Gender-Kontrast ($\Delta = 6$ bei D11) ist zugleich der größte Befund UND der am stärksten artefaktgefährdete. Er wird in Table 5 (Zeile 556, Rang 3) prominent präsentiert, aber gleichzeitig dreifach eingeschränkt. Reviewer werden diesen Widerspruch angreifen.

**Fix:** Nicht aus der Tabelle entfernen (das wäre Datensuppression), aber:

1. In Table 5 den Eintrag mit Fußnote versehen: "†Preliminary hypothesis; see contamination caveat in Section 4.4 and 5.2."
2. In Zeile 583-584 den Satz "The contamination caveat stated above applies with full force." ersetzen durch: "This finding is classified as a **preliminary hypothesis requiring independent validation** (multi-LLM triangulation, expert ratings) before it can be interpreted substantively. We report it for completeness but caution against using it as a basis for policy recommendations."

### A6. SU-IDs englisch vereinheitlichen (bestätigt Step-1, B7)

**Problem:** Deutsche Abkürzungen in einem englischen Paper (GA_ges_AH, HOM_haeuf_A, GR_*_AH). Das ist ein sofortiger "sloppy work"-Eindruck bei Reviewern.

**Fix:** Appendix D (Zeile 1177-1197): Entweder alle SU-IDs übersetzen (ALL_total_SA, HOM_freq_S, ROLE_*_SA etc.) oder -- pragmatischer -- eine Fußnote am Anfang des Appendix einfügen:

> "SU identifiers follow the German-language conventions of the companion paper \citep{Geiger2026SWR} and are retained here for cross-reference consistency. GA = Gesamtanalyse (full sample), GR = Gruppenrolle (role group), GF = Gruppenfirma (company group), GH = Gruppenhaltung (stance group), GD = Gruppendemografie (demographic group), HOM = Homogenisierung (homogenization), AH/A/H = Aussagen+Handlungen / Aussagen / Handlungen (SA/S/A)."

### A7. Op4-Inkonsistenz in Tabelle 1 korrigieren

**Problem:** Tabelle 1 (Zeile 251) sagt in der Fußnote: "*Op4 was not conducted in this study." Aber in Section 3.5 (Quality Assurance, Zeile 283) wird Cross-Modal Prediction (Op4) als **durchgeführte** Validierung beschrieben (44/50 Vorhersagen bestätigt, 88%). Das ist ein direkter Widerspruch.

**Fix:** Die Fußnote in Tabelle 1 (Zeile 251) ändern von:
> "$^*$Op4 was not conducted in this study."

zu:
> "$^*$Op4 was conducted as a validation experiment (5 groups, 50 predictions; see Section 3.5) but not as a systematic operationalization across all synthesis units."

---

## B: Empfohlene Verbesserungen (kein Blocker, aber stärkend)

### B1. Abstract straffen (~180 Wörter statt ~250)

Der Abstract ist inhaltlich exzellent, aber für AI & Society oder Big Data & Society zu lang. Die 12 Dimensionen und die 6 Forschungsfragen müssen nicht im Abstract stehen. Vorschlag: Methode in einem Satz ("using synthetic worldview reconstruction, an LLM-assisted procedure"), dann direkt zu den drei stärksten Befunden (Say-Do Gap, Power-Moderation Paradox, Weltbild-Typologie).

### B2. Intersektionalitäts-Passage ergänzen

In Section 6 (Limitations) oder Section 5 (Discussion) fehlt ein Hinweis auf die Konfundierung der Gruppen: CEOs sind >85% männlich; Akademiker sind überproportional Risk Warners. Die Studie kann Rolle, Geschlecht und Ideologie nicht sauber trennen -- das sollte in 3-4 Sätzen explizit benannt werden:

> "A limitation of the present group-comparison design is the substantial overlap between grouping variables: the CEO group is >85% male, the academic group disproportionately contains risk warners, and the female subgroup is overrepresented in Guardian-type positions. The observed group differences therefore reflect *confounded* structural factors that cannot be disentangled without multivariate analysis at the individual level -- an important desideratum for future research."

### B3. Say-Do-Gap als diverging bar chart

Die aktuelle Fig. 6 ist funktional, aber ein diverging bar chart (Dimension links: Do < Say, rechts: Do > Say, sortiert nach $|\Delta|$) wäre visuell einprägsamer und für Konferenzpräsentationen und Policy-Briefings besser geeignet. Kein Muss, aber eine lohnende Investition von ~30 Minuten.

### B4. Kontrolle des Companion-Paper-Status

Das Companion Paper liegt auf Zenodo als Preprint. Für den Review-Prozess bei einem Peer-Reviewed Journal ist das ein Risiko. Pragmatische Lösung: Im Text (Zeile 197) ergänzen: "The companion paper is currently under review at [Journal]; a preprint is available at [Zenodo-DOI]." Selbst wenn noch kein Journal gewählt ist, zeigt die Formulierung "under preparation for submission to" den Reviewern, dass die Methodengrundlage nicht nur ein selbstpubliziertes Dokument ist.

### B5. Historischer Vergleichshorizont (1 Absatz)

In der Discussion fehlt eine kurze historische Einordnung. Ein einzelner Absatz in Section 5.1 würde erhebliche Tiefe hinzufügen:

> "The AI elite is not the first technology elite to exhibit these patterns. The Manhattan Project physicists of the 1940s similarly combined a sense of mission with ambivalence about the consequences of their work (cf. Rhodes, 1986). The internet pioneers of the 1990s exhibited a comparable libertarian-utopian worldview before commercial pressures transformed the field (Turner, 2006). What distinguishes the AI elite is the *scale* of potential impact combined with the *concentration* of power in fewer hands than any previous technology elite."

### B6. Anthropic-Anteil im Sample quantifizieren

Zeile 729 diskutiert die Anthropic-Zirkularität, aber nennt keine Zahl. Reviewer werden fragen: Wie viele der 100 Personen sind Anthropic-affiliiert? Wenn es 2-3 sind, ist der Einfluss auf Gruppensynthesen marginal. Einfach ergänzen: "Of the 100 actors, [N] are directly affiliated with Anthropic, constituting [X]% of the total sample."

### B7. "Western" im Titel oder Subtitle erwägen

Die Stichprobe ist überwiegend anglo-amerikanisch (Zeile 720-721). Das ist korrekt benannt, aber der Titel suggeriert Universalität. Möglichkeit: Subtitle ändern von "An LLM-Assisted Analysis of the 100 Most Influential Actors" zu "An LLM-Assisted Analysis of the 100 Most Influential **Western** Actors" -- oder alternativ: eine Fußnote zum Titel, die den geographischen Scope klarstellt.

---

## C: Abgelehnte Vorschläge aus Step 1

### C1. Step-1-Vorschlag B8 (Say-Do-Gap als eigenständige Figur): TEILWEISE ABGELEHNT

Der Vorschlag ist als visueller Tipp sinnvoll (übernommen als B3 oben), aber die Formulierung "Fig. 6 wird nur einmal gezeigt" impliziert, dass das ein Problem sei. Es ist keines -- eine einzige, gut gemachte Figur reicht. Es fehlt keine Figur; die bestehende könnte nur besser gestaltet werden.

### C2. Step-1-Vorschlag C1 (Worldview Dashboard): ABGELEHNT

Ein interaktives Dashboard ist eine schöne Idee für die Wissenschaftskommunikation, aber es gehört nicht in den Review-Prozess. Es bindet erhebliche Entwicklungszeit, hat keinen Einfluss auf die Akzeptanz bei Reviewern und lenkt vom eigentlichen Paper ab. **Nach** Publikation als Supplementary Material sinnvoll, vorher nicht.

### C3. Step-1-Vorschlag C2 (Deliberation Simulation / "Synthetic Town Hall"): ABGELEHNT

Das wäre ein eigenständiges Paper, kein Appendix-Experiment. Es würde zudem den epistemischen Status des Papers verwässern: Die Stärke liegt in der *rekonstruktiven* Analyse realer Daten, nicht in der *generativen* Simulation fiktiver Dialoge. Jedes generative Experiment würde die Halluzinations-Kritik (D1 im Review-Antizipation) verstärken statt abschwächen.

### C4. Step-1-Vorschlag C4 (Spiegelexperiment: "AI-kritische Öffentlichkeit"): ABGELEHNT für diese Version

Methodisch interessant, aber es würde den Scope des Papers sprengen. Die 100 Personen sind bereits durch eine systematische Auswahlprozedur bestimmt; eine Kontrastgruppe (Gewerkschaften, Zivilgesellschaft, Regulierungsbehörden) bräuchte eine eigene Sampling-Logik, eigene Datenerhebung, eigene Validierung. Das ist ein Follow-up-Paper, kein Revision-Element.

### C5. Step-1-Vorschlag C5 (Alignment-Paradox als eigenständiges Paper): ABGELEHNT als Handlungsempfehlung

Die Einschätzung, dass Section 5.3 (Agentic vs. Worldview Alignment) Potenzial für ein eigenes Paper hätte, ist korrekt. Aber die Empfehlung, es *jetzt* herauszulösen, ist falsch: Es ist einer der stärksten theoretischen Beiträge dieses Papers. Herauslösen würde das Paper schwächen. Die richtige Strategie: Es hier als Provokation belassen und nach Publikation ausbauen.

### C6. Step-1-Vorschlag D5 ("Western" im Titel): ABWEICHEND

Step 1 schlägt "Western AI Elite" im Titel vor. Ich empfehle das als Option (B7 oben), aber *nicht* als Pflicht. Der Titel "AI Elite" ist stärker, einprägsamer und ehrlicher: Die Studie analysiert nicht bewusst nur den Westen, sondern die *de facto* mächtigsten Akteure -- die zufällig überwiegend westlich sind. Der geographische Scope gehört in die Limitations, nicht in den Titel.

### C7. Step-1-Vorschlag D4 (Co-Autor suchen): ABGELEHNT als Review-Empfehlung

Der Vorschlag, einen Co-Autor mit institutioneller Anbindung zu suchen, ist strategisch nachvollziehbar, aber wissenschaftsethisch problematisch: Einen Co-Autor nur für die Affiliation hinzuzufügen ist *Gift Authorship*. Die Arbeit ist von einem Einzelautor -- das ist transparent und ehrlich. Die Datenqualität und Methodentransparenz müssen für sich sprechen.

---

## D: Zusätzliche Findings (vom konstruktiven Reviewer übersehen)

### D1. Zirkuläre Validierung bei Kruskal-Wallis

Die Kruskal-Wallis-Tests (Table 7, Zeile 517-542) werden als Validierung der Cluster-Lösung präsentiert. Aber: Die Cluster wurden *auf denselben Daten* gebildet, auf denen dann die Kruskal-Wallis-Tests gerechnet werden. Das ist zirkulär -- natürlich zeigen Gruppen, die nach D07/D11 getrennt wurden, signifikante Unterschiede auf D07/D11. Die Signifikanz auf *anderen* Dimensionen (D02, D06, D09, D12) ist informativer, wird aber nicht als primärer Validierungsindikator hervorgehoben.

**Fix:** Einen Satz nach Zeile 542 einfügen:

> "We note that the significance of D07 and D11 is partly tautological, since these dimensions informed the cluster construction. The non-trivial finding is that four *additional* dimensions (D02, D06, D09, D12) also discriminate significantly -- suggesting that the four types capture real variation beyond the defining axes."

### D2. Fehlende Effektstärken für den Say-Do Gap

Table 4 (Zeile 427-449) berichtet $\Delta$-Werte für die Say-Do-Diskrepanz, aber keine standardisierten Effektstärken. Die Fußnote (Zeile 461) erklärt korrekt, warum Cohen's $d$ nicht berechenbar ist (keine individuelle Streuung). Aber: Wenn für die Subgruppen-Vergleiche Cliff's $\delta$ berechnet wird (Zeile 578), dann sollte für den Say-Do Gap -- der als zentraler Befund gilt -- zumindest ein Vergleichsmaß angegeben werden. Andernfalls werden Reviewer fragen: "Woher weiß ich, dass $\Delta = 3$ auf einer LLM-generierten Skala 'groß' ist?"

**Fix:** Die Expected-Discrepancy-Kontrolle (Zeile 731) liefert einen Benchmark: Real-Gap MAE = 1.25 vs. Kontroll-Gap MAE = 0.50, Ratio 2.5:1. Dieses Verhältnis sollte prominenter als Effektstärke-Ersatz in Table 4 oder im begleitenden Text auftauchen:

> "To contextualize the magnitude of the say-do gap: the real AI elite produces a mean absolute discrepancy 2.5 times larger than a synthetic control group designed to be congruent (MAE 1.25 vs. 0.50), suggesting that the observed gap substantially exceeds the method's baseline noise."

### D3. Fehlende Diskussion der Aggregation-Synthesis-Divergenz

In Section 3.5 (Zeile 283) wird berichtet, dass die Korrelation zwischen direkten Gruppensynthesen und aggregierten Individualprofilen $r = 0.623$ beträgt -- mit einem "Amplification Effect" (71.7% der Werte weiter vom Mittelpunkt). Für heterogene Gruppen (Women $r = 0.428$, Men $r = 0.549$) ist die Konvergenz schwach. Das wird als "interpretable as group-level coherence amplification" geframt, aber es gibt eine alternative Interpretation: **Die Gruppensynthese und die aggregierten Individualprofile messen verschiedene Dinge.** Die eine ist ein LLM-generiertes Narrativ, das auf Kohärenz optimiert ist; die andere ist ein arithmetisches Mittel.

**Fix:** In Section 5.3 (Methodological Reflection) oder Limitations einen Satz ergänzen:

> "The moderate correlation between direct group syntheses and aggregated individual profiles ($r = 0.623$) may reflect not only coherence amplification but a fundamental difference in what the two procedures measure: direct synthesis produces a *narrative* coherence (the most plausible collective worldview), while aggregation produces *statistical* central tendency. The two approaches should be understood as complementary perspectives, not as one validating the other."

### D4. Implizite Kausalannahme im Power-Moderation Paradox

Section 4.5 (RQ6) und die Discussion (Section 5.4) formulieren das Power-Moderation Paradox so, dass Macht und Weltbild-Extremität *korrelieren*. Aber die Formulierung "Power intensifies all beliefs except those that question power itself" (Zeile 613) impliziert eine kausale Richtung: Macht → Weltbild-Veränderung. Das wird in Section 5.5 ("What the Study Does Not Show", Zeile 705, Punkt 1) formell ausgeschlossen, aber der rhetorische Sog der Formulierung ist stärker als der Disclaimer.

**Fix:** Zeile 613 umformulieren:

> "At the group level, the data show that higher worldview intensity co-occurs with lower values for human appreciation and egalitarianism. Whether power shapes worldview, worldview attracts power, or both are driven by a third factor (e.g., institutional selection) cannot be determined from the present data."

### D5. Fehlende Sensitivitätsanalyse für Samplegröße

Die Studie verwendet ein Sample von $N = 100$, das "die 100 einflussreichsten AI-Akteure" repräsentieren soll. Aber es fehlt jede Diskussion darüber, wie sensitiv die Ergebnisse gegenüber der Samplezusammensetzung sind. Was passiert, wenn man die 10 "grenzwertigen" Fälle (die knapp in die Top 100 kamen) austauscht? Verschieben sich die Cluster? Ändert sich der Say-Do Gap?

**Fix:** In den Limitations (Section 6.1) ergänzen:

> "The robustness of the findings to sample composition has not been formally tested. A leave-$k$-out sensitivity analysis -- removing 5--10 borderline actors and re-running the group syntheses -- would provide evidence on whether the core findings (say-do gap, four types, power-moderation paradox) are stable or dependent on specific sample members. This is a priority for future validation."

### D6. Sprachlich: "suggests" vs. "shows" -- Inkonsistenz

Das Paper bemüht sich vorbildlich um epistemische Vorsicht ("suggests", "the data indicate", "the reconstructed profiles point to"). Aber an mehreren Stellen rutscht es in stärkere Sprache: Zeile 335 "The profile displays a characteristic dual structure", Zeile 452 "The discrepancies arrange themselves into two complementary clusters", Zeile 576 "The strongest contrast [...] does not concern risk assessment [...] but the ontological pre-commitment". Diese Formulierungen klingen wie empirische Fakten, nicht wie LLM-Rekonstruktionen.

**Fix:** Systematischer Durchgang durch das Results-Kapitel. Alle aktiven, faktischen Formulierungen ("displays", "arrange themselves", "does not concern... but") ersetzen durch epistemisch markierte: "The reconstructed profile displays...", "The reconstructed discrepancies arrange...", "In the reconstructed data, the strongest contrast appears to concern...".

### D7. Run-Convergence nur für 5 von 51-56 Synthesis Units

Die Test-Retest-Validierung ($r = 0.908$, Zeile 283) basiert auf nur 5 von 51-56 Synthesis Units. Das sind <10% des Materials. Die 5 SUs werden nicht namentlich genannt -- es bleibt unklar, ob es sich um die einfachsten (homogenste Gruppen) oder repräsentative SUs handelt.

**Fix:** Im Text (Zeile 283) die 5 SUs identifizieren und begründen, warum diese gewählt wurden:

> "The five tested SUs were [X, Y, Z, W, V], selected to cover the range of group heterogeneity (from ideologically homogeneous to heterogeneous). A broader convergence test across all SUs remains desirable."

### D8. Datenbank-Verifikation und Repository-Status

Zeile 852 verweist auf ein GitHub-Repository (https://github.com/lukisch/ai-elite-worldview). Reviewer werden dieses Repository prüfen. Ist es:
- Bereits öffentlich?
- Vollständig (alle Scripts, die $100 \times 12$ Matrix, die Prompts)?
- Mit einer Lizenz versehen?
- Mit einem Zenodo-DOI für Zitierfähigkeit?

**Empfehlung:** Vor Einreichung sicherstellen: Repository öffentlich, README mit Reproduktionsanleitung, Zenodo-DOI für den Datensatz (unabhängig vom Code-Repo). Das ist kein Paper-Fix, aber ein Einreichungs-Prerequisite.

---

## E: Aktualisierter Readiness-Score

### Score: 6.5/10

**Begründung für leichte Herabstufung gegenüber Step 1 (7/10):**

Step 1 hat die Stärken korrekt identifiziert, aber einige strukturelle Probleme unterschätzt:

1. **Die Op4-Inkonsistenz** (A7) ist ein faktischer Fehler im Manuskript, der bei Reviewern sofort Misstrauen weckt: Wenn eine Operationalisierung gleichzeitig als "nicht durchgeführt" und als "durchgeführt (88% bestätigt)" beschrieben wird, untergräbt das die Glaubwürdigkeit des gesamten Qualitätssicherungsabschnitts.

2. **Die zirkuläre Kruskal-Wallis-Validierung** (D1) wird als Stärke präsentiert, ist aber methodisch angreifbar. Dass dies nicht explizit als Limitation adressiert wird, werden quantitative Reviewer bemerken.

3. **Die Aggregation-Synthesis-Divergenz** (D3) -- $r = 0.623$ -- ist nicht nur ein Validierungsergebnis, sondern wirft eine fundamentale Frage auf: Wenn zwei Wege, dieselben Daten zu verarbeiten, nur zu 39% gemeinsamer Varianz führen, wie sicher kann man dann sein, dass die Gruppensynthesen "reale" kollektive Überzeugungen abbilden?

4. **Die sprachliche Inkonsistenz** (D6) zwischen epistemischer Vorsicht und faktischen Formulierungen ist durchgängig und wird von aufmerksamen Reviewern als Zeichen mangelnder Sorgfalt gewertet.

**Was für 6.5 spricht:**
- Die Arbeit ist **konzeptionell stark**: Originalität, gesellschaftliche Relevanz, und die Say-Do-Gap-Analyse als eigenständiger methodischer Beitrag sind genuine Stärken.
- Die **Transparenz** über Limitationen ist vorbildlich -- aber Transparenz allein reicht nicht, wenn die identifizierten Probleme im Ergebnisteil nicht konsequent reflektiert werden.
- Die **Pflicht-Korrekturen (A1-A7)** sind alle in 1-2 Wochen behebbar. Nach Umsetzung steigt der Score auf **8/10**.

**Was für 9-10 fehlt (und nicht schnell behebbar ist):**
- Inter-LLM-Triangulation (mindestens GPT-4o oder Gemini als Zweitmodell)
- Externe Expertenvalidierung (unabhängige Coder, die die Ratings für eine Teilstichprobe nachvollziehen)
- Leave-k-out-Sensitivitätsanalyse für die Samplezusammensetzung

**Empfohlener Workflow:**
1. A1-A7 umsetzen (1-2 Wochen)
2. B1-B7 nach Kapazität einbauen (parallel)
3. Einreichen bei **AI & Society** (beste thematische Passung, toleranter gegenüber methodischer Innovation) oder **Big Data & Society** (höherer Impact Factor, aber strengere quantitative Reviewer)
4. FAccT/AIES als Alternative nur wenn als Long Paper mit Companion Paper als Supplement akzeptiert

---

*Reviewer-Profil: Führender Fachexperte für Computational Social Science und LLM-basierte Forschungsmethoden. Fokus auf epistemische Robustheit, interne Konsistenz und Reviewer-Resistenz.*
