# Adversarialer Widerlegungsbericht: KI_Elite_v2_en.tex

**Perspektive:** Strikt adversarialer Reviewer, Top-Journal-Ablehnungsmodus
**Datum:** 2026-03-30
**Dokument:** KI_Elite_v2_en.tex (englische Version, Stand 2026-03-27)
**Auftrag:** Falsifizierung, Destabilisierung, Entkräftung -- keine Reparaturvorschläge

---

## 1. Die gesamte Studie ist ein LLM-Zirkel: Das Instrument erzeugt seinen eigenen Gegenstand

**Stelle:** Gesamtarchitektur; AI Disclosure (Zeile 840ff.), Section 3.5 (Zeile 282ff.)

**Warum der Schritt nicht gilt:** Claude Sonnet 4.5 generiert die 100×12 Rating-Matrix. Claude Opus 4.6 führt die Gruppensynthesen durch, berechnet die Statistik (PCA, HDBSCAN, Kruskal-Wallis, Cliff's δ), erstellt die Visualisierungen und unterstützt beim Schreiben des Manuskripts. Es gibt exakt *null* Datenpunkte in dieser Studie, die nicht durch Anthropic-Modelle gelaufen sind. Das ist kein Forscher, der ein Instrument benutzt -- das ist ein Instrument, das sich selbst interpretiert.

**Pathologie:** Man stelle sich vor, die gesamte Studie würde mit GPT-4o statt Claude wiederholt. Wenn GPT-4o systematisch andere Ratings produziert (was bei 12-dimensionalen Weltbildbewertungen hochwahrscheinlich ist), dann sind *alle* Befunde -- Cluster, Say-Do-Gap, Power-Paradox -- Artefakte des spezifischen Modells, nicht der Daten. Die Studie hat genau *eine* Messung mit genau *einem* Instrument. In jeder anderen Wissenschaft wäre das ein Pilotexperiment, kein Paper.

---

## 2. Die "Validierungen" validieren nichts Externes

**Stelle:** Section 3.5 (Zeile 282--283), gesamter Quality-Assurance-Block

**Warum der Schritt nicht gilt:** Die vier "implementierten" Validierungsmaßnahmen sind:
- (a) Run-Convergence: Claude stimmt mit Claude überein (r = 0.908). Das beweist interne Konsistenz des Modells, nicht Validität der Aussagen.
- (b) Expected-Discrepancy-Kontrolle: Ein *fiktiver* Kontrollkorpus (Umweltwissenschaftler), ebenfalls von Claude generiert und von Claude bewertet. Claude sagt, Claude findet keinen Gap bei Daten, die Claude-kongruent entworfen wurden. Das ist ein Test, ob Claude "kein Gap produzieren kann, wenn die Daten kongruent sind" -- nicht ein Test, ob Claude "den echten Gap korrekt misst".
- (c) Aggregation-Synthesis-Vergleich: Vergleicht zwei *Claude-Outputs* miteinander (Gruppensynthesenratings vs. gemittelte Individualratings). Beide Seiten stammen vom selben Modell.
- (d) Cross-Modal Prediction (Op4): Claude sagt aus Statements Handlungen vorher. 44/50 bestätigt. Aber wer prüft die "Bestätigung"? Das Paper sagt es nicht explizit -- wenn Claude die Bestätigung prüft, ist der Zirkel komplett.

**Pathologie:** Ein Thermometer, das man gegen sich selbst kalibriert, zeigt immer "kalibriert". Jede einzelne Validierung in diesem Paper ist *intern*. Es gibt exakt *null* externe Ankerpunkte (keine Expertenbewertungen, keine Survey-Daten, keine Multi-Modell-Vergleiche).

---

## 3. Der Say-Do-Gap könnte ein trainierter Bias sein, nicht ein empirischer Fund

**Stelle:** RQ3, Section 4.3 (Zeile 423--464), Limitations Zeile 731

**Warum der Schritt nicht gilt:** Das Paper räumt selbst ein (Zeile 731), dass LLMs auf sozialwissenschaftlicher Literatur trainiert sind, in der Say-Do-Gaps bei Eliten ein Standardbefund sind. Die "Expected-Discrepancy"-Kontrolle soll dies entkräften: bei einem fiktiven kongruenten Kontrollkorpus produziert Claude einen kleineren Gap. Aber dieser Test beweist nur, dass Claude bei *offensichtlich kongruenten* Daten keinen Gap halluziniert. Er beweist *nicht*, dass Claude bei *ambigen* Realdaten den Gap korrekt misst statt den erwarteten Gap zu reproduzieren.

**Gegenbeispiel:** Füttert man Claude mit denselben Daten, aber mit dem Systemprompt "Diese Gruppe ist bekannt für außergewöhnliche Integrität", könnte der Gap verschwinden. Füttert man dieselben Daten mit dem Prompt "Diese Gruppe ist notorisch heuchlerisch", könnte der Gap sich verdreifachen. Ohne diese Prompt-Sensitivitätsanalyse ist der Say-Do-Gap nicht von einem Framing-Artefakt unterscheidbar.

---

## 4. Die Cluster-"Entdeckung" ist eine LLM-assistierte Autorenentscheidung, keine emergente Struktur

**Stelle:** RQ4, Section 4.4 (Zeile 467--513)

**Warum der Schritt nicht gilt:** Das Paper beschreibt den Identifikationsprozess ehrlich (Zeile 472): "Stage 1 (LLM-assisted): All 15 group syntheses were grouped by similarity patterns [...] Stage 2 (author validation): The four-cluster solution proposed by the LLM was evaluated by the author." Das heißt: Claude schlägt Cluster vor, der Autor akzeptiert. Drei und fünf Cluster wurden "rejected" -- aber nach welchem Kriterium? Substantive Kohärenz, beurteilt vom Autor. Das ist keine Entdeckung, sondern eine informierte Entscheidung.

Das Paper gibt dies zu und nennt die Cluster "Weberian ideal types" (Zeile 513). Aber es betitelt RQ4 als "exploratory" und berichtet Kruskal-Wallis-Tests, Silhouette-Scores und Cliff's δ für diese Cluster -- als ob sie statistisch testbare Entitäten wären. Die HDBSCAN-Analyse im 12D-Raum scheitert (80-100% Noise, Silhouette -0.15). KMeans k=4 liefert 0.169. Im Subspace D07/D11 findet HDBSCAN 9 Cluster (nicht 4) mit 0.57. Die vier "Typen" existieren in den Daten nicht als natürliche Cluster.

**Pathologie:** Nehmen wir an, der Autor hätte Claudes Vorschlag mit 5 Clustern akzeptiert. Dann hätte das Paper 5 Typen, andere Cliff's-δ-Werte und ein anderes Power-Paradox. Die gesamte Typologie hängt an einer nicht-reproduzierbaren Autorenentscheidung, die durch eine LLM-Empfehlung angeregt wurde.

---

## 5. Die Kruskal-Wallis-Tests sind zirkulär und überdies keine valide Inferenzstatistik

**Stelle:** Table 7 (Zeile 517--542), Algorithmic Validation (Zeile 507ff.)

**Warum der Schritt nicht gilt:** Erstens sind D07 und D11 -- die beiden höchsten H-Werte (64.76 und 49.57) -- exakt die Dimensionen, auf denen die Cluster definiert wurden. Das ist tautologisch. Das Paper räumt dies ein (Zeile 511: "circularity caveat"), behauptet aber, die "non-trivial finding" seien die vier weiteren signifikanten Dimensionen. Aber auch diese Dimensionen wurden vom selben LLM generiert, das die Cluster vorgeschlagen hat. Wenn Claude eine kohärente Vier-Cluster-Lösung vorschlägt, wird Claude auch korrelierte Dimensionen innerhalb dieser Cluster kohärent setzen.

Zweitens -- und fundamentaler -- gibt die Fußnote in Table 7 zu: "p-values are nominal and should not be interpreted as inferential hypothesis tests in the classical sense." Dann sind die ***, **, * Sterne in der Tabelle irreführend. Sie suggerieren inferentielle Evidenz, die das Paper selbst als nicht gegeben deklariert.

**Gegenbeispiel:** Generiert man 100 zufällige 12D-Profile mit Claude unter der Anweisung "erstelle kohärente Weltbilder für fiktive AI-Akteure", bildet 4 Cluster auf den Extremdimensionen und rechnet Kruskal-Wallis, erhält man mit hoher Wahrscheinlichkeit ähnlich "signifikante" Ergebnisse -- weil Claude intern kohärente Profile erzeugt.

---

## 6. Die Zeitreihenanalyse hat n=17 mit 43-facher Dichtevarianz

**Stelle:** RQ2, Section 4.2 (Zeile 358--420), Table 3 (Zeile 366ff.)

**Warum der Schritt nicht gilt:** Es gibt 17 jährliche Datenpunkte. Davon haben 2010 und 2011 jeweils nur 17 Rohdatenpunkte, während 2024 735 hat. Die OLS-Regression über 17 Punkte mit R² von 0.27-0.63 für "Trends" wird beschrieben, aber: (a) n=17 für Regressionsanalyse ist extrem wenig; (b) die extremen Dichten-Unterschiede bedeuten, dass die frühen Datenpunkte auf extrem dünner Evidenz ruhen; (c) das Paper erkennt an, dass keine formale Breakpoint-Analyse möglich ist (Zeile 400).

**Pathologie:** Wenn 2010-2015 jeweils nur 2-5 Statements pro Person umfasst und Claude daraus ein 12D-Profil generiert, sind diese Profile im Wesentlichen Claude-Extrapolationen aus Minimalinformation. Der "Trend" D10 von 10 auf 6 könnte einfach reflektieren, dass Claude bei wenig Daten zu extremeren Werten tendiert und bei viel Daten zur Mitte regrediert. Mean-Regression statt Weltbildwandel.

---

## 7. Focus Control beweist nicht, was es zu beweisen beansprucht

**Stelle:** Section 3.5 (Zeile 282), Limitations (Zeile 727--728)

**Warum der Schritt nicht gilt:** Focus Control ersetzt Personennamen, Firmennamen und Produktnamen durch neutrale Platzhalter. Das Paper behauptet, dies stelle sicher, dass "the LLM processes the presented data rather than falling back on stored knowledge" (Zeile 282). Aber:

(a) Ein LLM erkennt Akteure nicht nur am Namen. Ein Datensatz mit den Aussagen "I believe in beneficial AGI", "We restructured from a non-profit to a capped-profit", "AI is the most important technology in human history" + Aktion "Testified before US Congress 2023" ist *eindeutig* Sam Altman, egal ob der Name da steht.

(b) Die Anonymisierung verschleiert die Identität nicht, sie entfernt nur das einfachste Erkennungsmerkmal. Für die Gruppen-Synthese (wo Daten vieler Akteure zusammenfließen) mag dies weniger kritisch sein, aber für die 100 individuellen Ratings (die in PCA/HDBSCAN eingehen) ist es irrelevant -- Claude "erkennt" die meisten dieser Personen an ihren Aussagen.

(c) Das Paper gibt in den Limitations zu (Zeile 727), dass Kontamination "nicht eliminierbar" ist. Trotzdem wird Focus Control als eine der vier "implementierten Maßnahmen" der Qualitätssicherung angeführt.

**Gegenbeispiel:** Man nehme 10 erfundene "AI-Akteure" mit komplett fiktiven Datensätzen. Wenn Claude für diese Profile stabil andere Ergebnisse produziert als für die realen (erkennbaren) Akteure, wäre das ein Signal für Kontaminationsresistenz. Dieser Test wurde nicht durchgeführt.

---

## 8. Die Spot-Checks (Table 10) sind nicht blind und nicht unabhängig

**Stelle:** Section 6.5 (Zeile 765--808), Table 10

**Warum der Schritt nicht gilt:** Die "Spot-Checks" wurden so durchgeführt: Der Autor prüft, ob Claudes Rating für Sam Altman, Geoffrey Hinton und Marc Andreessen mit öffentlich bekannten Positionen übereinstimmen. 30/36 = 83% "confirmed", 6/36 "plausible", 0 widerlegt.

Probleme: (a) Der Prüfer ist der Autor selbst, nicht ein unabhängiger Experte. (b) "Confirmed" und "plausible" sind subjektive Kategorien ohne Operationalisierung. Wann wäre ein Rating "not verifiable"? Wenn Altman D01=9 (Sendungsbewusstsein) hat und der Autor als Beleg "repeated statements about the 'most important technology in human history'" anführt -- wie hätte er das *nicht* bestätigen können? Der Bestätigungs-Bias ist strukturell eingebaut. (c) Es wurden 3 von 100 Akteuren geprüft, und zwar die drei öffentlichsten. Für die 20-30 weniger prominenten Akteure im Sample (mit je 20-25 Datenpunkten) ist die Prüfbarkeit deutlich geringer.

**Pathologie:** Ein adversarialer Test wäre: 5 unabhängige Politikwissenschaftler bewerten blind dieselben 12 Dimensionen für dieselben 3 Personen. Dann vergleicht man Inter-Rater-Reliabilität Mensch vs. Claude. Diesen Test gibt es nicht.

---

## 9. "3.132 Datenpunkte" suggeriert Datenmenge, die nicht existiert

**Stelle:** Section 3.1 (Zeile 209), Introduction (Zeile 146)

**Warum der Schritt nicht gilt:** 3.132 Datenpunkte = 1.738 Statements + 1.394 Aktionen für 100 Personen. Das sind im Mittel 31,3 Datenpunkte pro Person (Range 20-72). Für eine *Weltbild-Rekonstruktion* auf 12 Dimensionen sind 20-30 Datenpunkte pro Person keine "große empirische Datenbasis", sondern das absolute Minimum. Der einzelne Datenpunkt ist dabei ein Statement oder eine Aktion -- keine standardisierte Messung mit bekannter Reliabilität.

Aber das eigentliche Problem: Diese 3.132 Datenpunkte werden nicht direkt analysiert. Sie werden als *Prompt-Input* an Claude übergeben, und Claude produziert *eine einzige Zahl* pro Dimension pro Einheit. Die effektive Stichprobengröße für die Statistik ist also nicht 3.132, sondern die Anzahl der Synthese-Einheiten (51-56 für die Kernanalyse, 100 für die Individualmatrix). Die 3.132 sind Rohmaterial, nicht Datenpunkte im statistischen Sinne.

---

## 10. Das Power-Moderations-Paradox ist ein Circular Reasoning

**Stelle:** RQ6, Section 4.6 (Zeile 592--617), Table 6 (Zeile 597--611)

**Warum der Schritt nicht gilt:** Das "Paradox" lautet: Gruppen mit mehr Ressourcen haben extremere Weltbilder und niedrigere Egalitarismus-Werte. Aber:

(a) Die Power-Zuordnung ("Highest / High / Medium / Lowest") ist nicht operationalisiert. Es gibt keine quantitativen Proxies, keine Berechnung, kein externes Ranking. Der Autor ordnet den Cluster-Typen Machtlevel zu. Die Zuordnung "Architect = Highest" ist plausibel, aber unfalsifizierbar.

(b) Der "Architect" wird definiert durch CEOs und Investoren. CEOs und Investoren haben definitionsgemäß die meisten Ressourcen. Das "Paradox" besagt also: Die Gruppe, die nach mächtigen Leuten benannt und aus mächtigen Leuten zusammengesetzt ist, hat die meiste Macht. Gleichzeitig hat diese Gruppe niedrige D11-Werte -- aber D11 war ein definiierendes Merkmal der Cluster-Zuordnung (Architects haben niedrige D11). Das "Paradox" ist in die Cluster-Konstruktion eingebaut.

**Gegenbeispiel:** Definiert man die Cluster anders (z.B. nach den PCA-Hauptkomponenten statt nach D07/D11), könnte der Zusammenhang Power-Egalitarismus verschwinden.

---

## 11. Die Grounded-Theory-Berufung ist nicht substanziiert

**Stelle:** Section 3.1.3 "Methodological Anchoring" (Zeile 215-217)

**Warum der Schritt nicht gilt:** Das Paper behauptet, Datensammlung folge dem "grounded theory approach of Strauss & Corbin (1990)" in sechs Phasen. Grounded Theory erfordert: (a) theoretical sampling, (b) constant comparison, (c) theoretical saturation als Abbruchkriterium, (d) Memo-Writing. Nichts davon wird im Paper nachgewiesen. Die sechs beschriebenen Phasen (keine Filter → offenes Kodieren → Kategoriensystem → Inklusions-/Exklusionskriterien → QA) sind ein plausibles Datensammlungsprotokoll, aber *keine* Grounded Theory. Die Berufung auf Strauss & Corbin ist ein Autoritätsargument ohne methodische Substanz.

**Pathologie:** Grounded Theory impliziert, dass die Kategorien *aus den Daten* emergieren. Aber die 12 Dimensionen D01-D12 wurden vor der Datenanalyse definiert (sie stammen aus dem Companion Paper). Das ist das Gegenteil von Grounded Theory -- das ist deduktive Anwendung eines vorgefertigten Schemas.

---

## 12. Der Companion-Paper-Verweis als systematische Verantwortungsverlagerung

**Stelle:** Section 3.2 (Zeile 220-223), passim (mindestens 8 Verweise auf Geiger2026SWR)

**Warum der Schritt nicht gilt:** Das Paper verweist für *alle* grundlegenden Methodenfragen auf das Companion Paper: die epistemologische Begründung des inverse problem, das Prompt-Protokoll, die Validierungsarchitektur, das Focus-Control-Design, die Diskussion der Kohärenz-Bias. Das Companion Paper ist ein *Zenodo-Preprint* eines Einzelautors -- kein peer-reviewtes Werk. Die gesamte methodische Legitimation hängt an einem nicht-begutachteten Selbst-Verweis.

**Pathologie:** Ein Reviewer bei AI & Society kann das Companion Paper nicht als gegeben voraussetzen. Wenn die Methode in Paper A nicht eigenständig bewertbar ist, ist Paper A nicht eigenständig einreichungsfähig. Der Companion-Paper-Verweis ist funktional eine Bitte, die Methodenkritik bitte woanders zu üben.

---

## 13. Die 12 Dimensionen sind willkürlich und nicht validiert

**Stelle:** Appendix B (Zeile 1121-1146), Section 3.3 (Zeile 230-256)

**Warum der Schritt nicht gilt:** Die 12 Dimensionen werden als gegeben eingeführt ("defined in the SWR framework"). Es gibt keine faktorenanalytische Herleitung, keine Konstruktvalidierung, keine Pilotstudie mit menschlichen Codierern. Die PCA (Zeile 288-290) zeigt, dass 5 Komponenten 80% der Varianz erklären -- also sind ~7 der 12 Dimensionen teilweise redundant. Das Paper kommentiert dies als "reasonable operationalization for exploratory work" (Zeile 290). Aber wenn die Dimensionen redundant sind, sind auch die auf ihnen basierenden Befunde (Korrelationen, Cluster, Rankings) aufgebläht.

**Gegenbeispiel:** Dimension D09 "Human appreciation" hat die Skalenpole "Replaceable" (1) vs. "Unique" (10). Das mischt anthropologische Ontologie (ist der Mensch einzigartig?) mit technologischer Prognose (ist der Mensch ersetzbar?). Jemand, der glaubt, Menschen seien ontologisch einzigartig aber funktional durch KI ersetzbar, kann auf dieser Skala nicht kohärent bewertet werden. Die Dimension konfundiert zwei verschiedene Konstrukte.

---

## 14. Die Gender-Befunde sind mit hoher Wahrscheinlichkeit ein LLM-Stereotyp-Artefakt

**Stelle:** RQ5, Zeile 561-584, Discussion Zeile 667

**Warum der Schritt nicht gilt:** Das Paper berichtet den größten Einzelkontrast der gesamten Studie bei D11 im Geschlechtervergleich: Frauen 8, Männer 2, Δ=6. Es stuft diesen Befund selbst als "most contamination-prone" ein und verweist auf Santurkar et al. (2023). Aber: Wenn der *kontaminationsanfälligste* Befund gleichzeitig der *größte* ist, dann ist die naheliegendste Erklärung, dass er ein Artefakt ist. Ein Δ von 6 auf einer 10-Punkte-Skala liegt weit jenseits jeder bekannten Gender-Differenz in empirischen Weltbildstudien. Keine psychologische Survey-Studie findet Unterschiede dieser Magnitude.

Das Paper beschreibt den Befund trotzdem über mehrere Absätze, integriert ihn in die RQ5-Kernaussage ("strongest predictors: stance, role, gender") und nutzt ihn in der Discussion (Becker 2025, "broligarchy"). Epistemic hedging und prominente Darstellung widersprechen einander.

**Pathologie:** Wenn man den Gender-Befund als Artefakt klassifiziert, fällt "gender" als drittstärkster Prädiktor aus dem Paper. Die RQ5-Kernaussage müsste zu "stance and role" reduziert werden. Das Paper nutzt die größte Schwäche als eines seiner eindrucksvollsten Ergebnisse.

---

## 15. Die Effektstärken (Cliff's δ) sind keine echten Effektstärken

**Stelle:** RQ5, Zeile 578-582

**Warum der Schritt nicht gilt:** Cliff's δ wird berechnet auf den 100 individuellen LLM-generierten Ratings. Das Paper berichtet δ = +1.0 für Architect vs. Liberator auf D07 -- "perfect separation". Aber diese Ratings wurden vom selben LLM generiert, das kohärente Profile erstellt. Wenn Claude CEOs systematisch hohe D07-Werte und Open-Source-Akteure systematisch niedrige gibt, resultiert daraus ein hohes δ -- nicht weil die Realität so ist, sondern weil Claude konsistente Stereotype implementiert.

Cliff's δ misst den Überlappungsgrad zweier Verteilungen. Bei LLM-generierten Daten misst es den Überlappungsgrad zweier *Modell-Outputs*. Die "Effektstärke" ist die Stärke der LLM-internen Kohärenz, nicht die Stärke eines empirischen Effekts.

---

## 16. Die Kontrolle mit fiktiven Umweltwissenschaftlern ist kein valider Nulltest

**Stelle:** Section 3.5 (Zeile 282-283), Limitations (Zeile 731)

**Warum der Schritt nicht gilt:** Der Kontrollkorpus besteht aus 30 fiktiven Statements + 30 fiktiven Aktionen einer fiktiven Gruppe "Umweltwissenschaftler", die *designt* wurden, um kongruent zu sein. Claude findet bei diesem Korpus einen kleinen Gap (MAE=0.50) vs. den realen Gap (MAE=1.25). Das beweist:
- Claude halluziniert keinen Gap bei *offensichtlich* kongruenten Daten.

Es beweist *nicht*:
- Claude misst den *echten* Gap bei *ambigen* Daten korrekt.

Der relevante Kontrolltest wäre: Man nehme eine *reale* Gruppe, für die unabhängige Evidenz existiert, dass *kein* Say-Do-Gap vorliegt, und prüfe ob Claude trotzdem einen findet. Oder: Man nehme eine reale Gruppe mit einem *bekannten* Gap und prüfe, ob Claude dessen Magnitude korrekt schätzt. Beides fehlt.

**Gegenbeispiel:** Man konstruiere einen fiktiven Kontrollkorpus, der wie die echten AI-Elite-Daten aussieht (heterogen, ambig, widersprüchlich), aber mit definiertem Gap=0. Wenn Claude auch hier einen Gap von ~1.25 produziert, wäre der reale Befund ein Artefakt.

---

## 17. Keine Falsifizierbarkeit der zentralen These

**Stelle:** Core Finding RQ1 (Zeile 355), Core Finding RQ6 (Zeile 616), Conclusion (Zeile 818ff.)

**Warum der Schritt nicht gilt:** Die zentrale These lautet: Die KI-Elite besitzt einen "technologischen Messianismus mit Ambivalenzstruktur". Wann wäre diese These falsifiziert? Das Paper definiert kein Kriterium. Wenn Claude niedrigere Werte bei D01 oder D05 produziert hätte, hätte das Paper vermutlich "pragmatischer Technologismus" statt "Messianismus" geschrieben. Wenn der Say-Do-Gap kleiner wäre, hätte es "moderate Inkongruenz" geschrieben. Die These ist so flexibel formuliert, dass sie jedes Datenmuster aufnehmen kann.

**Pathologie:** "Technologischer Messianismus" ist eine *Interpretation*, keine *Hypothese*. Sie kann nicht widerlegt werden, weil sie kein Vorhersage-Kriterium benennt. Karl Poppers Falsifizierbarkeits-Kriterium ist nicht erfüllt.

---

## 18. Die "9 systematischen Gruppenvergleiche" sind nicht unabhängig

**Stelle:** Introduction (Zeile 146), Results passim

**Warum der Schritt nicht gilt:** Die 9 Vergleiche (nach Rolle, Haltung, Gender, Firma, Epoche) basieren auf *denselben* 100 Akteuren und *derselben* 100×12 Matrix. Ein CEO ist gleichzeitig Mann, Accelerator, OpenAI-Mitglied und Epoch-3-Akteur. Die Vergleiche sind nicht unabhängig voneinander, sondern teilweise Reanalysen derselben Datenpunkte. Wenn CEOs hohe D07-Werte haben und CEOs überwiegend männlich sind, dann hat der Gender-Vergleich einen D07-Effekt *weil* der Rollen-Vergleich einen hat, nicht unabhängig davon.

Das Paper berichtet die 9 Vergleiche als separate Evidenzstücke. In Wirklichkeit sind es korrelierte Schnitte durch denselben 100×12 Datenwürfel.

---

## 19. Die Stichprobe ist handverlesen und nicht replizierbar

**Stelle:** Section 3.1.1 (Zeile 203-206), Appendix A (Zeile 1115-1118)

**Warum der Schritt nicht gilt:** Der Autor wählte 187 Kandidaten über "22 systematic web searches" aus und reduzierte auf 100 mittels eines "6-category scoring system". Die 22 Suchanfragen sind nicht dokumentiert. Das Scoring-System hat keine Inter-Rater-Reliabilität. Ein anderer Forscher mit anderen 22 Suchanfragen hätte andere 187 Kandidaten gefunden und eine andere Top-100-Liste produziert.

Die Entscheidung, *wer zur KI-Elite gehört*, determiniert alle Folgebefunde. Wenn man die 18 Frauen durch 18 andere Frauen ersetzt (es gibt sicher 18 weitere einflussreiche Frauen in der KI), ändern sich Gender-Befunde. Wenn man 10 der 35 "Architects" durch weniger prominente CEOs ersetzt, ändern sich Cluster-Profile.

**Pathologie:** Die Sampling-Strategie ist ein single point of failure für die gesamte Studie, und sie ist vollständig vom Autor abhängig. "Independent Researcher, Bernau" hat keine institutionelle Anbindung, die intersubjektive Kontrolle sicherstellen könnte.

---

## 20. Die Pearson/Spearman-Korrelationen innerhalb der Zeitreihe sind auto-generierte Kohärenz

**Stelle:** Section 4.2 (Zeile 380-381), Fig. 4

**Warum der Schritt nicht gilt:** Die Spearman-Korrelation r_s = +0.85 zwischen D10 und D12 über die 17 Jahresdatenpunkte wird als "connected phenomenon" interpretiert. Aber beide Werte (D10 und D12 für jedes Jahr) wurden vom selben Claude-Lauf für dasselbe Jahr erzeugt. Wenn Claude ein "kohärentes Weltbild" für 2015 generiert, dann korrelieren D10 und D12 nicht, weil Posthumanismus und Locus of Control empirisch zusammenhängen, sondern weil Claude *denkt*, dass sie zusammenhängen.

Das Paper merkt dies in einer Fußnote an (Zeile 380: "could reflect internal coherence of the model rather than empirical relationships in reality"). Aber es baut trotzdem das gesamte "Utopia-Komplex"-Narrativ auf dieser Korrelation auf, inklusive Figur 4 und dem Core Finding RQ2.

---

## 21. Die Begriffe "empirisch", "Daten", "Befund" werden systematisch fehlverwendet

**Stelle:** Gesamtes Paper, besonders Abstract (Zeile 91-97), Introduction (Zeile 146), Core Findings

**Warum der Schritt nicht gilt:** Das Paper spricht durchgehend von "empirically grounded answer" (Zeile 819), "empirically supported hypotheses" (Zeile 93), "data-driven analysis" (Zeile 123), "3,132 data points" (Zeile 146). In der Sozialwissenschaft bedeutet "empirisch" die systematische Erhebung und Auswertung von Beobachtungsdaten. Die Rohdaten (Statements, Aktionen) sind empirisch. Aber die *Analyseergebnisse* (Ratings, Cluster, Gaps) sind LLM-Outputs -- sie sind nicht empirisch, sondern maschinengeneriert. Die 12-dimensionalen Profile sind keine Messwerte, sondern Modell-Schlussfolgerungen. Der durchgehende Gebrauch von "empirisch" für LLM-generierte Artefakte ist irreführend.

---

## 22. Die ethische Legitimation der Studie ist ungeprüft

**Stelle:** Section 6.4 (Zeile 754-762)

**Warum der Schritt nicht gilt:** Das Paper beruft sich auf APA Ethical Principles Standard 8.05 (Forschung an öffentlichen Personen ohne Einwilligung). Aber: (a) APA-Standards gelten für psychologische Forschung; dieses Paper situiert sich in der Computational Social Science. (b) Die SWR rekonstruiert *Weltbilder* -- also Überzeugungssysteme, die weit über öffentliche Äußerungen hinausgehen. Sam Altman hat nie ein 12-Punkte-Profil seiner Überzeugungen veröffentlicht; Claude hat es *inferiert*. Die ethische Frage ist nicht, ob man öffentliche Aussagen analysieren darf (ja), sondern ob man daraus *synthetische Persönlichkeitsprofile* erstellen und publizieren darf (unklar). (c) Es gibt kein Ethikvotum einer institutionellen Ethikkommission, was bei einer Studie über 100 identifizierbare lebende Personen mindestens diskussionswürdig ist.

---

## 23. Die "Expected-Discrepancy-Kontrolle" bestätigt möglicherweise das Gegenteil von dem, was sie soll

**Stelle:** Section 3.5, Zeile 282-283 (Punkt b)

**Warum der Schritt nicht gilt:** Der Kontrollkorpus "Umweltwissenschaftler" produziert MAE=0.50 (nicht null). Das bedeutet: Selbst bei einem Korpus, der *absichtlich kongruent entworfen wurde*, findet Claude einen Say-Do-Gap von 0.50 auf einer 10-Punkte-Skala. Das ist die *Baseline-Halluzinationsrate* des Modells. Der echte Gap ist 1.25, also 0.75 über der Baseline. Ob 0.75 Skalenpunkte auf einer LLM-generierten 10-Punkte-Skala "substantiell" sind, ist unklar -- es gibt keinen externen Benchmark.

Man könnte argumentieren: Der wahre Say-Do-Gap der KI-Elite ist maximal 0.75 (1.25 minus 0.50 Baseline), nicht 1.25. Das Paper rechnet mit 1.25 vs. 0.50 als "2.5× larger", aber die korrekte Rechnung wäre 0.75 über Baseline -- und ob das bei 12 Dimensionen mit LLM-generierten Werten bedeutsam ist, bleibt offen.

---

## 24. Reproduzierbarkeit ist nicht gegeben trotz gegenteiliger Behauptung

**Stelle:** Section 3.5 (Zeile 282, Punkt 3), Data Availability (Zeile 850-852)

**Warum der Schritt nicht gilt:** Das Paper behauptet ein "reproducibility protocol (temperature 0, complete prompt documentation, all prompts archived in the repository)". Aber: (a) Temperature 0 garantiert keine Determinismus bei LLMs -- Anthropic-Modelle können bei T=0 über verschiedene Läufe variieren. (b) Selbst bei exakt gleichem Output müsste die Reproduktion mit *demselben* Modell (Claude Sonnet 4.5 / Opus 4.6) in *derselben Version* stattfinden. LLMs werden laufend aktualisiert. In 6 Monaten existiert das verwendete Modell möglicherweise nicht mehr. (c) Das GitHub-Repository enthält (laut Data Availability Statement) Scripts und die Rating-Matrix -- aber nicht die *vollständigen Prompt-Verläufe* aller 51-56 Synthese-Einheiten. Ohne die exakten Kontextfenster ist Reproduktion unmöglich.

---

## 25. Das Paper Companion (Geiger2026SWR) ist ein nicht-begutachteter Zenodo-Upload desselben Autors

**Stelle:** Gesamte Methodik-Sektion, alle SWR-Verweise

**Warum der Schritt nicht gilt:** Die epistemologische Grundlage (was ist SWR?), die Validierungstheorie, die Diskussion der Limits -- all dies wird an Geiger (2026) delegiert, ein Zenodo-Preprint mit DOI 10.5281/zenodo.18736720. Zenodo vergibt DOIs ohne Peer Review. Der Autor begründet die Methode von Paper A mit Paper B, das er selbst geschrieben hat und das niemand überprüft hat. In der Kette "Paper A → Companion Paper B → keine externe Prüfung" gibt es keinerlei unabhängige Qualitätskontrolle.

---

## Zusammenfassung

Die Studie ist im Kern eine **LLM-Autopoiesis**: Ein Anthropic-Modell generiert Daten, ein Anthropic-Modell analysiert die Daten, ein Anthropic-Modell validiert die Analyse, und die gesamte methodische Legitimation beruft sich auf ein nicht-begutachtetes Preprint desselben Autors. Es gibt keinen einzigen externen Ankerpunkt -- keinen menschlichen Codierer, keinen Multi-Modell-Vergleich, keine Survey-Kreuzvalidierung, kein Experten-Rating, kein Ethikvotum.

Die Befunde (technologischer Messianismus, Say-Do-Gap, Power-Paradox, vier Cluster-Typen) sind nicht falsifizierbar, weil sie von keiner modell-externen Messung gedeckt sind. Sie könnten vollständig korrekt sein -- oder vollständig Artefakte von Claude's internem Weltmodell. Die Studie bietet kein Mittel, zwischen beiden Möglichkeiten zu unterscheiden.

---

*Adversarialer Reviewer, 2026-03-30. Keine Lösungsvorschläge, keine wohlwollende Interpretation.*
