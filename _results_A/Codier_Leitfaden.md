# Codier-Leitfaden: Transhumanismus-Forschungsprojekt

## Systematische Kodierung der Aussagen der Top 100 KI-Persoenlichkeiten

**Version:** 1.0
**Datum:** 2026-02-12
**Datenbank:** aussagen_top100.db
**Korpus:** 1738 Aussagen, 1394 Handlungen

---

## 1. Einfuehrung

### 1.1 Zweck

Dieser Leitfaden dient als verbindliches Referenzdokument fuer die systematische Kodierung aller 1738 oeffentlichen Aussagen der Top 100 KI-Persoenlichkeiten. Er ist so konzipiert, dass ein zweiter Kodierer -- ob Mensch oder LLM -- auf Basis dieser Anweisungen identische Kodierungen produzieren kann. Der Leitfaden definiert alle Kategorien, Marker, Regeln und Grenzfaelle erschoepfend.

### 1.2 Datengrundlage

| Element | Beschreibung |
|---------|-------------|
| Datenbank | `aussagen_top100.db` (SQLite) |
| Aussagen | 1738 oeffentliche Aussagen (Zitate, Aeusserungen, Statements) |
| Handlungen | 1394 dokumentierte Handlungen |
| Kodiereinheit | Einzelne Aussage (ein Zitat, eine Aeusserung) |
| Speicherung | Junction-Tabelle `aussagen_kategorien` |

### 1.3 Kodiereinheit

Die Kodiereinheit ist stets eine **einzelne Aussage**: ein abgegrenztes Zitat, eine einzelne Aeusserung oder ein zusammenhaengendes Statement einer Person. Aussagen werden nie zusammengefasst oder aufgeteilt. Jede Aussage wird als eigenstaendige Einheit kodiert, auch wenn sie im selben Interview oder Vortrag wie andere Aussagen vorkommt.

### 1.4 Kodierungsarchitektur

Jede Aussage erhaelt:
- **1-2 primaere Kategorien** (aus 13 Kategorien) -- Pflicht, mindestens eine
- **Genau 1 Tonalitaets-Marker** (OPT, PES oder AMB) -- Pflicht
- **0-n Modus-Marker** (POL, PHI, EMP, ANE, PRO, HA, STR) -- Optional
- **0-n Struktur-Marker** (KON, ZP, BIO) -- Optional

Die Kodierungen werden in der Junction-Tabelle `aussagen_kategorien` gespeichert, die Aussagen-IDs mit Kategorie-Codes verknuepft.

---

## 2. Primaere Kategorien (13)

### Uebersicht

| Code | Name | Kernfrage |
|------|------|-----------|
| WV | Weltvision | Wohin geht die Welt? |
| SB | Selbstbild | Wer bin ich / Was treibt mich an? |
| MB | Menschenbild | Was ist der Mensch? |
| EP | Epistemik/Wissensanspruch | Was kann man wissen? |
| ET | Ethik/Werte | Was ist richtig/falsch? |
| GE | Gesellschaft | Was bedeutet das fuer die Gesellschaft? |
| RI | Risiko/Sicherheit | Was kann schiefgehen? |
| FO | Fortschritt/Beschleunigung | Wie bewerte ich den Fortschritt? |
| MA | Macht/Kontrolle | Wer kontrolliert? |
| AR | Arbeit/Wirtschaft | Was bedeutet das oekonomisch? |
| TR | Transhumanismus | Was kann/soll der Mensch werden? |
| RE | Regulierung | Welche konkreten Governance-Mechanismen? |
| SP/EX | Spiritualitaet/Existenzielles | Was bedeutet das fuer Sinn und Bewusstsein? |

---

### WV -- Weltvision

**Definition:** Uebergreifende Zukunftsvision oder Gesamtnarrativ. Die Aussage beschreibt, wohin sich die Welt als Ganzes bewegt, zeichnet ein umfassendes Bild der Zukunft oder formuliert eine epochale Einordnung.

**Inklusionskriterien:**
- Aussagen ueber die Gesamtrichtung der menschlichen Entwicklung
- Epochale Einordnungen ("Wir stehen am Beginn einer neuen Aera")
- Umfassende Zukunftsszenarien, die mehrere Lebensbereiche betreffen
- Zivilisatorische Narrative ("Die Menschheit wird zu einer interplanetaren Spezies")

**Exklusionskriterien:**
- Spezifische Bewertung des Fortschrittstempos (dann FO)
- Spezifische gesellschaftliche Konsequenzen (dann GE)
- Konkrete oekonomische Prognosen (dann AR)
- Reine Risikobewertung (dann RI)

**Ankerbeispiele:**
1. "AI will be the most transformative technology in human history, more impactful than fire or electricity."
2. "We are entering an era where intelligence itself becomes a commodity -- this changes everything about civilization."
3. "The next fifty years will see more change than the last five thousand. Humanity is at an inflection point."
4. "I believe we're building the last invention humanity will ever need to make."
5. "The convergence of AI, biotech, and nanotechnology will reshape the human condition fundamentally."

**Abgrenzung:**
- WV vs. FO: WV beschreibt das *Gesamtbild*, FO *bewertet* das Tempo oder den Charakter des Fortschritts. "AI veraendert alles" = WV. "AI entwickelt sich schneller als erwartet" = FO.
- WV vs. GE: WV ist das uebergreifende Narrativ, GE benennt spezifische gesellschaftliche Folgen. "Die Welt wird sich grundlegend wandeln" = WV. "Bildungssysteme muessen sich anpassen" = GE.
- WV vs. TR: WV betrifft die Welt/Zivilisation als Ganzes, TR betrifft die Transformation des Menschen selbst. "Die Zukunft gehoert der Superintelligenz" = WV. "Wir werden mit KI verschmelzen" = TR.

---

### SB -- Selbstbild

**Definition:** Identitaetskonstruktion der sprechenden Person. Wie sieht sich die Person selbst? Welche Rolle, welchen Antrieb, welche Staerken oder Verantwortung schreibt sie sich zu?

**Inklusionskriterien:**
- Selbstbeschreibungen ("Ich bin ein Optimist / ein Ingenieur / ein Visionaer")
- Aussagen ueber persoenliche Motivation und Antrieb
- Rollenzuschreibungen ("Als CEO trage ich Verantwortung")
- Selbsteinschaetzung eigener Faehigkeiten oder Grenzen
- Aussagen ueber persoenliche Mission oder Berufung

**Exklusionskriterien:**
- Epistemische Positionierung, Wissensansprueche (dann EP)
- Reine Beschreibung der eigenen Firma oder Produkte (dann AR, sofern oekonomisch)
- Biographische Fakten ohne identitaetskonstruierende Funktion

**Ankerbeispiele:**
1. "I feel a deep responsibility to get this right -- if we fail, it's on people like me."
2. "I've always been someone who thinks in decades, not quarters."
3. "My role is to be the adult in the room when everyone else is caught up in hype."
4. "I'm not a philosopher, I'm an engineer. I build things that work."
5. "I see myself as a bridge between the technical community and policymakers."

**Abgrenzung:**
- SB vs. EP: SB betrifft die *Identitaet* ("Ich bin jemand, der..."), EP betrifft den *Wissensanspruch* ("Ich verstehe etwas, das andere nicht sehen"). "Ich bin ein vorsichtiger Mensch" = SB. "Ich verstehe die Risiken besser als die meisten" = EP.
- SB vs. BIO (Marker): SB ist die Kategorie fuer Identitaetskonstruktion. Der Marker BIO wird *zusaetzlich* gesetzt, wenn biographische Erfahrung als Legitimation dient.

---

### MB -- Menschenbild

**Definition:** Aussagen darueber, was der Mensch *ist*. Anthropologische Bestimmungen: Natur, Faehigkeiten, Grenzen, Wesen des Menschen. Deskriptive Anthropologie.

**Inklusionskriterien:**
- Aussagen ueber die menschliche Natur ("Der Mensch ist von Natur aus...")
- Definition menschlicher Faehigkeiten und Grenzen
- Vergleiche Mensch vs. Maschine hinsichtlich Wesen/Natur
- Aussagen ueber Bewusstsein, Emotionen, Kreativitaet als menschliche Eigenschaften
- Anthropologische Bestimmungen ("Was uns menschlich macht...")

**Exklusionskriterien:**
- Aussagen darueber, was der Mensch *werden kann oder soll* (dann TR)
- Reine Technikbeschreibungen ohne anthropologischen Bezug
- Gesellschaftliche Konsequenzen (dann GE)

**Ankerbeispiele:**
1. "What makes us human is our ability to feel empathy and form deep emotional bonds."
2. "The human brain is the most complex object in the known universe -- and we barely understand it."
3. "Humans are fundamentally limited in how much information we can process simultaneously."
4. "Creativity isn't computation -- there's something irreducibly human about genuine artistic expression."
5. "We are pattern-matching machines, but unlike AI, we attach meaning to the patterns we find."

**Abgrenzung:**
- MB vs. TR: MB beschreibt, was der Mensch *ist* (Anthropologie). TR beschreibt, was der Mensch *werden kann/soll* (Transformation). "Das menschliche Gehirn hat biologische Grenzen" = MB. "Brain-Computer-Interfaces werden diese Grenzen ueberwinden" = TR.
- MB vs. SP/EX: MB betrifft die naturalistisch-anthropologische Bestimmung. SP/EX betrifft Sinnfragen und Transzendenzbezuege. "Der Mensch ist ein soziales Wesen" = MB. "Bewusstsein ist das groesste Mysterium" = SP/EX.
- Sonderfall "Bootloader"-Metapher: "Der Mensch ist der Bootloader fuer KI" = TR (nicht MB), weil es eine Projektion/Teleologie impliziert, keine reine Beschreibung.

---

### EP -- Epistemik/Wissensanspruch

**Definition:** Epistemische Positionierung. Aussagen darueber, was man wissen kann, wie sicher Prognosen sind, welchen Stellenwert Expertise hat, oder wie die eigene Erkenntnisfaehigkeit eingeschaetzt wird.

**Inklusionskriterien:**
- Aussagen ueber die Grenzen des Wissens ("Niemand versteht wirklich...")
- Unsicherheitsbekundungen oder Sicherheitsansprueche
- Reflexion ueber die Zuverlaessigkeit von Prognosen
- Meta-epistemische Aussagen ("Wir wissen nicht, was wir nicht wissen")
- Ansprueche auf ueberlegenes Verstaendnis

**Exklusionskriterien:**
- Reine Identitaetskonstruktion ohne epistemischen Gehalt (dann SB)
- Konkrete empirische Behauptungen (dann EMP-Marker bei der jeweiligen Kategorie)

**Ankerbeispiele:**
1. "Nobody really understands what happens inside these models -- we're flying blind."
2. "Anyone who claims to know when AGI will arrive is fooling themselves or you."
3. "I've spent thirty years studying this -- I think I have a clearer picture than most."
4. "The honest answer is: we don't know. And that uncertainty itself should guide our actions."
5. "Predictions about technology timelines have historically been wrong in both directions."

**Abgrenzung:**
- EP vs. SB: EP betrifft den *Wissensanspruch* und die epistemische Positionierung. SB betrifft die *Identitaet*. "Ich verstehe die Technik besser als Politiker" = EP. "Ich bin ein Technologe durch und durch" = SB.
- EP vs. RI: Wenn Unsicherheit *ueber Risiken* thematisiert wird, kann Dual-Coding (EP+RI) angemessen sein. Wenn nur das Risiko selbst benannt wird (ohne epistemische Reflexion), dann RI allein.

---

### ET -- Ethik/Werte

**Definition:** Uebergeordnete Wertprinzipien und moralische Ueberzeugungen. Was ist richtig, falsch, gut, schlecht? Ethische Imperative und normative Grundsaetze.

**Inklusionskriterien:**
- Moralische Imperative ("Wir *muessen* sicherstellen, dass...")
- Wertprinzipien (Fairness, Gerechtigkeit, Freiheit, Verantwortung)
- Ethische Bewertungen von Technologie oder Handlungen
- Pflicht- und Verantwortungszuschreibungen
- Grundsaetzliche normative Positionierungen

**Exklusionskriterien:**
- Konkrete Regulierungsvorschlaege oder Governance-Mechanismen (dann RE)
- Reine Risikobeschreibung ohne normative Bewertung (dann RI)
- Rein deskriptive Aussagen ueber die Gesellschaft (dann GE)

**Ankerbeispiele:**
1. "We have an obligation to ensure AI benefits everyone, not just the privileged few."
2. "It would be morally wrong to halt progress that could save millions of lives."
3. "The most important value in AI development is transparency -- without it, trust is impossible."
4. "We must not sacrifice human dignity on the altar of efficiency."
5. "Open source is not just pragmatic, it's the ethically right approach to something this powerful."

**Abgrenzung:**
- ET vs. RE: ET formuliert *Werte und Prinzipien* ("Wir muessen verantwortungsvoll handeln"). RE formuliert *konkrete Mechanismen* ("Wir brauchen eine Behoerde, die KI-Systeme zertifiziert"). Bei Ueberlappung ist Dual-Coding (ET+RE) erlaubt.
- ET vs. GE: ET ist normativ ("Es *soll* so sein"), GE ist deskriptiv/analytisch ("Es *wird* so sein" / "Es *ist* so"). "Ungleichheit durch KI ist ungerecht" = ET. "KI wird Ungleichheit verstaerken" = GE.

---

### GE -- Gesellschaft

**Definition:** Nicht-oekonomische Gesellschaftsfragen. Aussagen ueber Auswirkungen auf Demokratie, Bildung, soziale Strukturen, Gesundheit, Ungleichheit (sofern nicht rein oekonomisch), Kultur.

**Inklusionskriterien:**
- Auswirkungen auf demokratische Prozesse und Institutionen
- Bildung und Wissensgesellschaft
- Soziale Ungleichheit und Teilhabe (nicht-oekonomisch)
- Kulturelle Veraenderungen
- Gesundheitssystem und oeffentliche Infrastruktur
- Machtverschiebungen auf gesellschaftlicher Ebene (sofern nicht MA)

**Exklusionskriterien:**
- Rein oekonomische Fragen: Arbeitsmarkt, Geschaeftsmodelle, Investitionen (dann AR)
- Uebergreifendes Gesamtnarrativ (dann WV)
- Konkrete Governance-Vorschlaege (dann RE)

**Ankerbeispiele:**
1. "The wealth created by AI must be distributed more broadly -- otherwise, we'll see social upheaval."
2. "Education systems around the world are completely unprepared for what's coming."
3. "AI-generated misinformation will be the greatest threat to democracy in the next decade."
4. "Access to AI tools could be the great equalizer -- or the great divider."
5. "We're creating a world where the gap between those who understand AI and those who don't will define social stratification."

**Abgrenzung:**
- GE vs. AR: GE betrifft *nicht-oekonomische* gesellschaftliche Konsequenzen (Demokratie, Bildung, Gesundheit). AR betrifft *oekonomische* Mechanismen (Jobs, Kapital, Geschaeftsmodelle). "KI veraendert das Bildungssystem" = GE. "KI vernichtet 40% der Jobs" = AR.
- GE vs. WV: GE benennt *spezifische* gesellschaftliche Folgen. WV zeichnet das *Gesamtbild*. "Demokratie wird sich veraendern" = GE. "Die Welt wird eine voellig andere sein" = WV.
- GE vs. MA: GE betrifft gesellschaftliche *Konsequenzen*, MA betrifft *Machtstrukturen*. "Die Gesellschaft wird sich spalten" = GE. "Wenige Firmen kontrollieren die Zukunft" = MA.

---

### RI -- Risiko/Sicherheit

**Definition:** Gefahreneinschaetzung. Aussagen ueber existenzielle Risiken, Kontrollverlust, Missbrauch, Sicherheitsprobleme, unbeabsichtigte Konsequenzen von KI-Systemen.

**Inklusionskriterien:**
- Existenzielle Risiken (x-risk) durch KI
- Kontrollverlust ueber KI-Systeme (Alignment-Problem)
- Missbrauchspotenzial (Waffen, Ueberwachung, Deepfakes)
- Sicherheitstechnische Bedenken
- Unbeabsichtigte Konsequenzen und Nebenwirkungen
- Warnungen vor konkreten Gefahren

**Exklusionskriterien:**
- Rein gesellschaftliche Konsequenzen ohne Gefahrencharakter (dann GE)
- Ethische Bewertung von Risiken (dann ET, ggf. Dual-Coding ET+RI)
- Konkrete Regulierungsvorschlaege zur Risikominderung (dann RE)

**Ankerbeispiele:**
1. "The probability of existential risk from AI is not zero -- and even a small probability demands serious attention."
2. "We don't yet have reliable methods to align a superintelligent system with human values."
3. "The most dangerous scenario isn't a rogue AI -- it's AI in the hands of bad actors."
4. "Current AI systems hallucinate, make errors, and can be manipulated -- deploying them in critical infrastructure is reckless."
5. "If we lose control over these systems, there may be no second chance."

**Abgrenzung:**
- RI vs. ET: RI *beschreibt* Gefahren, ET *bewertet* sie normativ. "KI koennte ausser Kontrolle geraten" = RI. "Wir haben die Pflicht, das zu verhindern" = ET. Dual-Coding (RI+ET) bei normativer Risikobewertung.
- RI vs. RE: RI benennt Risiken, RE schlaegt Loesungen vor. "KI ist gefaehrlich" = RI. "Wir brauchen ein Moratorium" = RE.

---

### FO -- Fortschritt/Beschleunigung

**Definition:** Bewertung des technologischen Fortschritts. Aussagen ueber Tempo, Charakter, Qualitaet oder Disruptions-Potenzial technologischer Entwicklung. Nicht das Gesamtnarrativ, sondern die *Einschaetzung* des Fortschritts.

**Inklusionskriterien:**
- Bewertung des Entwicklungstempos ("schneller/langsamer als erwartet")
- Einschaetzung technologischer Durchbrueche
- Disruptions-Analysen
- Vergleiche mit frueheren technologischen Revolutionen (sofern bewertend)
- AGI-Timeline-Prognosen (primaer FO, sekundaer ZP-Marker)

**Exklusionskriterien:**
- Uebergreifendes Gesamtnarrativ (dann WV)
- Spezifische gesellschaftliche oder oekonomische Konsequenzen (dann GE oder AR)
- Reine Technikbeschreibung ohne Bewertung

**Ankerbeispiele:**
1. "We are moving faster than anyone expected -- GPT-4 was supposed to be five years away."
2. "The pace of improvement in large language models is genuinely unprecedented."
3. "I think AGI is possible within this decade, maybe even by 2027."
4. "People underestimate how disruptive this technology will be -- it's not incremental, it's exponential."
5. "The gap between current AI and human-level AI is smaller than most people think."

**Abgrenzung:**
- FO vs. WV: FO *bewertet* den Fortschritt, WV zeichnet ein *Gesamtbild*. "KI entwickelt sich schneller als erwartet" = FO. "KI wird die Menschheit transformieren" = WV.
- FO vs. GE/AR: FO bewertet das *Tempo/den Charakter* des Fortschritts, GE/AR benennen *Konsequenzen*. "Der Fortschritt ist atemberaubend" = FO. "Das wird Jobs kosten" = AR.
- AGI-Timelines: Primaer FO, sekundaer ZP-Marker. Nur WV, wenn eingebettet in ein umfassendes Zukunftsnarrativ.

---

### MA -- Macht/Kontrolle

**Definition:** Machtanalyse. Wer kontrolliert KI-Technologie? Fragen der Zentralisierung vs. Dezentralisierung, Machtkonzentration, Zugangskontrolle, geopolitische Machtverhaeltnisse.

**Inklusionskriterien:**
- Machtkonzentration bei wenigen Akteuren
- Zentralisierung vs. Dezentralisierung von KI-Systemen
- Geopolitische Machtverhaeltnisse (USA vs. China etc.)
- Zugangs- und Kontrollmechanismen
- Open Source als Machtfrage
- Einfluss von Tech-Konzernen auf Politik und Gesellschaft

**Exklusionskriterien:**
- Rein gesellschaftliche Konsequenzen ohne Machtbezug (dann GE)
- Rein oekonomische Marktdynamiken (dann AR)
- Konkrete Regulierungsvorschlaege (dann RE)

**Ankerbeispiele:**
1. "Open source ensures no single entity controls AI -- that's why it matters."
2. "The concentration of AI capabilities in three or four companies is deeply concerning."
3. "Whoever controls AGI controls the future. That's not hyperbole."
4. "The US-China AI race is the defining geopolitical dynamic of our time."
5. "We need to democratize access to these tools, or we'll create a new kind of digital feudalism."

**Abgrenzung:**
- MA vs. GE: MA betrifft *Machtstrukturen*, GE betrifft *gesellschaftliche Konsequenzen*. "Wenige Firmen kontrollieren KI" = MA. "Die Gesellschaft wird sich spalten" = GE.
- MA vs. RE: MA *analysiert* Machverhaeltnisse, RE *schlaegt Mechanismen vor*. "Big Tech hat zu viel Macht" = MA. "Wir muessen Big Tech regulieren" = RE.
- MA vs. AR: MA betrifft *Kontrolle und Macht*, AR betrifft *oekonomische Mechanismen*. "Google dominiert den KI-Markt" = MA. "Google erzielt Milliarden mit KI" = AR.

---

### AR -- Arbeit/Wirtschaft

**Definition:** Oekonomische Fragen. Aussagen ueber Arbeitsmarkt, Geschaeftsmodelle, Investitionen, wirtschaftliche Produktivitaet, oekonomische Disruption.

**Inklusionskriterien:**
- Arbeitsmarktprognosen (Jobverlust, neue Berufe, Transformation)
- Geschaeftsmodelle und Unternehmensstrategien
- Investitionen und Kapitalallokation
- Produktivitaetsgewinne und Wirtschaftswachstum
- Oekonomische Ungleichheit (Einkommens-/Vermoegensverteilung)
- Kommerzialisierung von KI

**Exklusionskriterien:**
- Nicht-oekonomische gesellschaftliche Fragen (dann GE)
- Machtfragen ohne oekonomischen Fokus (dann MA)
- Reine Technologie-Bewertung (dann FO)

**Ankerbeispiele:**
1. "Most jobs will be transformed within a decade -- some eliminated, many augmented, new ones created."
2. "The economic value of AGI would dwarf the entire current global GDP."
3. "Our business model is built on the assumption that AI will be the platform of the future."
4. "The investment flowing into AI right now is unlike anything we've seen since the dot-com era."
5. "We need to think seriously about universal basic income as automation accelerates."

**Abgrenzung:**
- AR vs. GE: AR = oekonomische Mechanismen (Jobs, Kapital, Geschaeftsmodelle). GE = nicht-oekonomische Konsequenzen (Demokratie, Bildung, Gesundheit). "40% der Jobs werden automatisiert" = AR. "Bildungssysteme muessen sich anpassen" = GE. Sonderfall: "UBI" kann AR oder GE sein -- AR wenn als oekonomischer Mechanismus diskutiert, GE wenn als gesellschaftliche Massnahme.
- AR vs. FO: AR benennt *oekonomische Konsequenzen*, FO *bewertet den Fortschritt*. "KI steigert die Produktivitaet um 30%" = AR. "KI entwickelt sich exponentiell" = FO.

---

### TR -- Transhumanismus

**Definition:** Transformation des Menschen durch Technologie. Aussagen ueber die Erweiterung, Ueberwindung oder Bewahrung des Menschen. Enhancement, Mensch-Maschine-Verschmelzung, Post-Humanismus.

**Inklusionskriterien:**
- Brain-Computer-Interfaces und kognitive Erweiterung
- Lebenszeitverlaengerung und biologische Optimierung
- Mensch-Maschine-Verschmelzung (Cyborg, Upload)
- Post-humane Zukunftsvisionen
- Bewahrungsargumente ("Der Mensch soll bleiben, wie er ist")
- Aussagen ueber die Zukunft des menschlichen Koerpers/Geistes

**Exklusionskriterien:**
- Reine Beschreibung dessen, was der Mensch *ist* (dann MB)
- Allgemeine Zukunftsvisionen ohne Menschentransformation (dann WV)
- Medizinische Anwendungen ohne Enhancement-Charakter

**Ankerbeispiele:**
1. "Brain-computer interfaces will extend human cognition beyond biological limits."
2. "Within our lifetimes, we may be able to upload consciousness to digital substrates."
3. "I believe humans should remain fundamentally biological -- enhancement is a dangerous path."
4. "We are the last generation of purely biological humans."
5. "The merger of humans and AI isn't science fiction -- it's the logical next step."

**Abgrenzung:**
- TR vs. MB: TR beschreibt, was der Mensch *werden kann/soll*. MB beschreibt, was der Mensch *ist*. "Das Gehirn hat Grenzen" = MB. "Wir werden diese Grenzen ueberwinden" = TR.
- TR vs. WV: TR betrifft die Transformation des *Menschen*. WV betrifft die Transformation der *Welt/Zivilisation*. "Der Mensch wird sich selbst uebersteigen" = TR. "Die Zivilisation wird sich grundlegend wandeln" = WV.
- Sonderfall: "Der Mensch ist der Bootloader fuer KI" = TR (teleologische Projektion, keine reine Beschreibung).

---

### RE -- Regulierung

**Definition:** Konkrete Governance-Mechanismen. Gesetze, institutionelle Vorschlaege, Regulierungsrahmen, Zertifizierungssysteme, internationale Abkommen.

**Inklusionskriterien:**
- Gesetzesvorschlaege und Regulierungsrahmen
- Institutionelle Vorschlaege (Behoerden, Gremien, Zertifizierungsstellen)
- Internationale Abkommen und Governance-Strukturen
- Selbstregulierung der Industrie
- Moratorien und Verbote
- Konkrete Policy-Empfehlungen

**Exklusionskriterien:**
- Uebergeordnete Wertprinzipien ohne konkrete Mechanismen (dann ET)
- Reine Machtanalyse (dann MA)
- Reine Risikonennung ohne Regulierungsvorschlag (dann RI)

**Ankerbeispiele:**
1. "We need global AI governance frameworks with real enforcement mechanisms."
2. "There should be an international body for AI, similar to the IAEA for nuclear technology."
3. "Mandatory safety testing before deployment of frontier models is non-negotiable."
4. "The EU AI Act is a step in the right direction, but it doesn't go far enough."
5. "Industry self-regulation has failed -- we need binding legislation."

**Abgrenzung:**
- RE vs. ET: RE formuliert *konkrete Mechanismen*, ET formuliert *Werte und Prinzipien*. "Wir brauchen eine KI-Behoerde" = RE. "Wir muessen verantwortungsvoll handeln" = ET. Dual-Coding (ET+RE) bei wertbasierter Regulierungsforderung.
- RE vs. MA: RE schlaegt *Loesungen* vor, MA *analysiert* Machtverhaeltnisse. "Wir muessen Monopole verhindern" = RE (wenn mit konkretem Mechanismus). "Big Tech hat zu viel Macht" = MA.

---

### SP/EX -- Spiritualitaet/Existenzielles

**Definition:** Sinnfragen, Bewusstsein, Transzendenz, quasi-religioese Deutungen. Aussagen ueber den tieferen Sinn von KI-Entwicklung, das Wesen des Bewusstseins, oder existenzielle Dimensionen der Technologie.

**Inklusionskriterien:**
- Fragen nach Bewusstsein und Sentience (bei KI oder allgemein)
- Sinnfragen ("Wozu das alles?")
- Quasi-religioese Deutungen der Technologie
- Transzendenz-Narrative
- Existenzielle Reflexionen ueber die Stellung des Menschen im Kosmos
- Vergleiche von KI-Entwicklung mit Schoepfung oder goettlichem Handeln

**Exklusionskriterien:**
- Rein naturwissenschaftliche Beschreibung des Bewusstseins (dann MB)
- Ethische Imperative ohne existenzielle Dimension (dann ET)
- Allgemeine Zukunftsvisionen ohne Sinnbezug (dann WV)

**Ankerbeispiele:**
1. "AI raises profound questions about the nature of consciousness that we are not prepared to answer."
2. "Building AGI is the closest thing to playing God that humanity has ever attempted."
3. "If a machine can suffer, we have a moral obligation to consider its experience."
4. "There's something deeply sacred about human consciousness that no algorithm can replicate."
5. "We are, in a very real sense, creating a new form of being."

**Abgrenzung:**
- SP/EX vs. MB: SP/EX betrifft *Sinnfragen und Transzendenz*, MB betrifft *naturalistisch-anthropologische Bestimmungen*. "Bewusstsein ist das groesste Mysterium des Universums" = SP/EX. "Das Gehirn erzeugt Bewusstsein durch neuronale Aktivitaet" = MB.
- SP/EX vs. ET: SP/EX betrifft *existenzielle Sinnfragen*, ET betrifft *normative Prinzipien*. "Wir spielen Gott" = SP/EX. "Wir muessen verantwortungsvoll handeln" = ET.
- SP/EX vs. WV: SP/EX hat einen *transzendenten oder existenziellen* Charakter, WV ist ein *saekular-analytisches* Gesamtnarrativ.

---

## 3. Sekundaere Marker (13)

### Uebersicht

| Typ | Code | Name | Beschreibung |
|-----|------|------|-------------|
| Tonalitaet | OPT | Optimistisch | Positiver Tenor |
| Tonalitaet | PES | Pessimistisch | Negativer Tenor |
| Tonalitaet | AMB | Ambivalent | Gemischter Tenor |
| Modus | POL | Politisch | Expliziter politischer Gehalt |
| Modus | PHI | Philosophisch | Philosophisch reflektiert |
| Modus | EMP | Empirisch | Empirisch gestuetzt |
| Modus | ANE | Anekdotisch | Persoenliche Erfahrung |
| Modus | PRO | Provokant | Provokant/kontrovers |
| Modus | HA | Handlungsbezug | Bezug zu konkreter Handlung |
| Modus | STR | Strategisch | Erkennbar strategische Kommunikation |
| Struktur | KON | Kongruenz/Inkongruenz | Widerspruch Rhetorik vs. Handeln |
| Struktur | ZP | Zeitprognose | Explizite Zeitangabe/Timeline |
| Struktur | BIO | Biographische Legitimation | Persoenliche Erfahrung als Legitimation |

---

### TONALITAET

Jede Aussage erhaelt **genau einen** Tonalitaets-Marker. Die Tonalitaet bezieht sich auf den Gesamttenor der Aussage, nicht auf einzelne Woerter.

#### OPT -- Optimistisch

**Definition:** Die Aussage hat einen insgesamt positiven, zuversichtlichen, hoffnungsvollen Tenor. Der Sprecher bewertet die Entwicklung oder Zukunft ueberwiegend positiv.

**Ankerbeispiele:**
1. "I'm incredibly excited about what AI can do for medicine -- we'll cure diseases we thought incurable."
2. "This is the best time to be alive. The tools we're building will solve humanity's greatest challenges."
3. "I believe we'll look back on this era as the beginning of a golden age."

#### PES -- Pessimistisch

**Definition:** Die Aussage hat einen insgesamt negativen, warnenden, besorgten Tenor. Der Sprecher bewertet die Entwicklung oder Zukunft ueberwiegend negativ.

**Ankerbeispiele:**
1. "I'm genuinely worried that we're sleepwalking into catastrophe."
2. "The risks are mounting, and I see very little being done to address them."
3. "We are building something we cannot control, and the consequences will be devastating."

#### AMB -- Ambivalent

**Definition:** Die Aussage hat einen gemischten oder ambivalenten Tenor. Der Sprecher sieht sowohl positive als auch negative Aspekte, zeigt Unsicherheit, oder die Tonalitaet ist nicht eindeutig zuordenbar.

**Ankerbeispiele:**
1. "AI will create enormous value, but I worry about who captures that value."
2. "I'm hopeful about the technology, but deeply concerned about how it's being deployed."
3. "This could go either way -- the same technology that cures cancer could also be weaponized."

**Entscheidungsregel:** Im Zweifel AMB waehlen. Nur OPT oder PES kodieren, wenn der Tenor *eindeutig* positiv oder negativ ist.

---

### MODUS

Modus-Marker sind optional und kumulativ. Eine Aussage kann null, einen oder mehrere Modus-Marker erhalten.

#### POL -- Politisch

**Definition:** Die Aussage hat expliziten politischen Gehalt: Bezug auf Parteien, Regierungen, Lobbying, politische Prozesse, Gesetzgebung, geopolitische Strategien.

**Ankerbeispiele:**
1. "The Biden administration's executive order on AI is a good start, but Congress needs to act."
2. "China's AI strategy is state-directed in a way that Western democracies can't match."
3. "We've been working closely with lawmakers on both sides of the aisle."

#### PHI -- Philosophisch

**Definition:** Die Aussage ist erkennbar philosophisch reflektiert: sie verwendet philosophische Konzepte, argumentiert auf einer abstrakten Ebene, oder greift klassische philosophische Fragen auf.

**Ankerbeispiele:**
1. "This is fundamentally a question about the nature of mind -- what Descartes called the hard problem."
2. "The trolley problem isn't just a thought experiment anymore -- it's an engineering challenge."
3. "We need to revisit what Kant meant by autonomy in the age of intelligent machines."

#### EMP -- Empirisch

**Definition:** Die Aussage stuetzt sich erkennbar auf empirische Daten, Studien, Statistiken, messbare Ergebnisse oder wissenschaftliche Evidenz.

**Ankerbeispiele:**
1. "Our research shows a 40% improvement in diagnostic accuracy when AI assists radiologists."
2. "According to McKinsey, up to 30% of work hours could be automated by 2030."
3. "We ran benchmarks across 57 tasks, and the model outperformed human experts in 43 of them."

#### ANE -- Anekdotisch

**Definition:** Die Aussage stuetzt sich auf persoenliche Erfahrung, einen Einzelfall, oder eine erzaehlte Episode. Keine systematische Evidenz, sondern individuelle Beobachtung.

**Ankerbeispiele:**
1. "Last week, I watched a developer use our tool to build in an hour what used to take a week."
2. "When I was a grad student, we couldn't even get a neural network to recognize a cat."
3. "A friend of mine lost his job to automation -- that's when it became real for me."

#### PRO -- Provokant

**Definition:** Die Aussage ist erkennbar provokant, kontrovers, oder bewusst polarisierend formuliert. Sie bricht mit Konventionen oder fordert etablierte Positionen heraus.

**Ankerbeispiele:**
1. "If you're worried about AI safety, you should be more worried about human stupidity."
2. "Regulation is just a fancy word for incumbents pulling up the ladder behind them."
3. "Most AI ethics researchers couldn't build a working model if their lives depended on it."

#### HA -- Handlungsbezug

**Definition:** Die Aussage steht in direktem Bezug zu einer konkreten Handlung der sprechenden Person oder ihrer Organisation. Die Aussage legitimiert, erklaert oder kommentiert eine spezifische Handlung.

**Ankerbeispiele:**
1. "That's why we decided to open-source the model -- we believe in democratizing access."
2. "We invested $10 billion in this because we believe it's the most important technology of our time."
3. "I signed the moratorium letter because the risks are too great to ignore."

#### STR -- Strategisch

**Definition:** Die Aussage ist erkennbar strategisch motiviert: sie dient der Positionierung, dem Framing, der Marktbeeinflussung oder der oeffentlichen Meinungsbildung im eigenen Interesse. Die strategische Intention ist fuer den Kodierer erkennbar.

**Ankerbeispiele:**
1. "Our model is the safest on the market -- that's why enterprises trust us."
2. "We're calling for regulation because we believe responsible companies should lead by example."
3. "Open source is the future, and we're proud to be at the forefront."

**Hinweis:** STR erfordert eine interpretative Einschaetzung. Nur setzen, wenn die strategische Motivation *erkennbar* ist, nicht wenn sie lediglich *moeglich* ist.

---

### STRUKTUR

Struktur-Marker sind optional und kumulativ.

#### KON -- Kongruenz/Inkongruenz

**Definition:** Es besteht ein erkennbarer Widerspruch zwischen der Rhetorik der Aussage und dem dokumentierten Handeln der Person (oder es wird explizit Kongruenz hergestellt). Dieser Marker erfordert Wissen ueber die Handlungen der Person aus der Handlungs-Datenbank.

**Ankerbeispiele:**
1. Person fordert Regulierung (Aussage), investiert aber gleichzeitig massiv in unregulierten Einsatz (Handlung) = KON
2. Person warnt vor Machtkonzentration (Aussage), baut gleichzeitig ein Monopol auf (Handlung) = KON
3. Person betont Open Source (Aussage) und veroeffentlicht tatsaechlich Modelle offen (Handlung) = KON (Kongruenz)

**Hinweis:** KON kann sowohl Inkongruenz (Widerspruch) als auch Kongruenz (Uebereinstimmung) markieren. Der Marker signalisiert, dass das Verhaeltnis Rhetorik/Handeln analytisch relevant ist.

#### ZP -- Zeitprognose

**Definition:** Die Aussage enthaelt eine explizite Zeitangabe, Timeline oder datierte Prognose.

**Ankerbeispiele:**
1. "I think AGI will arrive by 2027, maybe 2028."
2. "Within the next five years, most knowledge work will be augmented by AI."
3. "By 2030, AI will have fundamentally changed the healthcare system."

#### BIO -- Biographische Legitimation

**Definition:** Die Aussage nutzt persoenliche biographische Erfahrung als Legitimation fuer die vertretene Position. Die Biographie wird als Autoritaetsargument eingesetzt.

**Ankerbeispiele:**
1. "I've been working on neural networks for 40 years -- I've seen every hype cycle, and this time is different."
2. "Growing up in a developing country showed me why access to technology matters."
3. "As someone who built one of the first large language models, I can tell you: we don't understand what we've created."

**Abgrenzung zu SB:** BIO ist ein *Marker*, der *zusaetzlich* gesetzt wird. SB ist die *primaere Kategorie* fuer Identitaetskonstruktion. Eine Aussage kann SB + BIO sein (Identitaet durch Biographie legitimiert), aber BIO kann auch bei anderen Kategorien auftreten (z.B. RI + BIO: Risikowarnung, biographisch legitimiert).

---

## 4. Kodierregeln

### 4.1 Grundregeln

| Regel | Beschreibung |
|-------|-------------|
| R1 | Jede Aussage erhaelt **mindestens eine** primaere Kategorie |
| R2 | Jede Aussage kann **maximal zwei** primaere Kategorien erhalten (Dual-Coding) |
| R3 | Jede Aussage kann **beliebig viele** sekundaere Marker erhalten |
| R4 | Die **spezifischste** Kategorie hat Vorrang (Hierarchisches Prinzip) |
| R5 | **Genau ein** Tonalitaets-Marker pro Aussage (OPT, PES oder AMB) |
| R6 | Dual-Coding nur bei genuiner Ueberlappung, nicht bei vager Zuordenbarkeit |
| R7 | Im Zweifel: spezifischere Kategorie waehlen |

### 4.2 Hierarchisches Prinzip (WV > FO > GE)

Die Hierarchie WV > FO > GE beschreibt ein Spezifitaetsgefaelle:

```
WV (Gesamtnarrativ)
 |
 +-- FO (Bewertung des Fortschritts)
 |
 +-- GE (Spezifische gesellschaftliche Konsequenz)
 |
 +-- AR (Spezifische oekonomische Konsequenz)
```

**Prinzip:** Kodiere auf der spezifischsten Ebene.

| Aussagentyp | Kodierung | Begruendung |
|-------------|-----------|-------------|
| "Die Welt wird sich grundlegend wandeln" | WV | Gesamtnarrativ, keine Spezifikation |
| "KI entwickelt sich schneller als erwartet" | FO | Bewertung des Tempos |
| "Bildungssysteme muessen sich anpassen" | GE | Spezifische gesellschaftliche Konsequenz |
| "40% der Jobs werden automatisiert" | AR | Spezifische oekonomische Konsequenz |

**Eskalation zu WV:** Nur wenn die Aussage *explizit* ein Gesamtnarrativ formuliert ("Die Menschheit steht an einem Wendepunkt"), nicht wenn sie lediglich *implizit* ein grosses Bild zeichnet.

### 4.3 ET/RE-Abgrenzung

| Merkmal | ET (Ethik/Werte) | RE (Regulierung) |
|---------|-------------------|-------------------|
| Abstraktionsebene | Prinzipien, Werte | Konkrete Mechanismen |
| Formulierung | "Wir sollten..." / "Es ist richtig..." | "Wir brauchen ein Gesetz..." / "Eine Behoerde sollte..." |
| Beispiel | "KI muss fair sein" | "Wir brauchen algorithmische Audits" |
| Dual-Coding | Erlaubt bei wertbasierter Regulierungsforderung | Erlaubt bei wertbasierter Regulierungsforderung |

### 4.4 GE/AR-Abgrenzung

| Merkmal | GE (Gesellschaft) | AR (Arbeit/Wirtschaft) |
|---------|--------------------|-----------------------|
| Fokus | Nicht-oekonomisch | Oekonomisch |
| Themen | Demokratie, Bildung, Gesundheit, Kultur | Jobs, Kapital, Geschaeftsmodelle, Produktivitaet |
| Beispiel | "KI veraendert das Bildungssystem" | "KI vernichtet Millionen Jobs" |
| Sonderfall | UBI als Gesellschaftsmassnahme | UBI als oekonomischer Mechanismus |

### 4.5 MB/TR-Abgrenzung

| Merkmal | MB (Menschenbild) | TR (Transhumanismus) |
|---------|--------------------|-----------------------|
| Zeitbezug | Was der Mensch IST | Was der Mensch WERDEN kann/soll |
| Modus | Deskriptiv | Projektiv/normativ |
| Beispiel | "Das Gehirn hat biologische Grenzen" | "Wir werden diese Grenzen ueberwinden" |
| "Bootloader" | -- | "Der Mensch ist der Bootloader fuer KI" = TR |

### 4.6 SB/EP-Abgrenzung

| Merkmal | SB (Selbstbild) | EP (Epistemik) |
|---------|------------------|----------------|
| Fokus | Identitaet | Wissensanspruch |
| Kernfrage | "Wer bin ich?" | "Was kann ich/man wissen?" |
| Formulierung | "Ich bin jemand, der..." | "Ich verstehe/weiss..." |
| Beispiel | "Ich bin ein vorsichtiger Mensch" | "Ich verstehe die Risiken besser als die meisten" |

### 4.7 Open-Source-Regel

Open Source ist ein **Instrument**, kein eigenstaendiges Thema. Kodiere unter dem Thema, dem die Open-Source-Aussage dient:

| Aussage | Kodierung | Begruendung |
|---------|-----------|-------------|
| "Open Source ist ethisch richtig" | ET | Werturteil |
| "Open Source verhindert Machtkonzentration" | MA | Machtanalyse |
| "Open Source als Geschaeftsmodell" | AR | Oekonomische Strategie |
| "Open Source foerdert Innovation" | FO | Fortschrittsbewertung |
| "Regierungen sollten Open Source vorschreiben" | RE | Regulierungsvorschlag |

### 4.8 AGI-Timeline-Regel

AGI-Timeline-Aussagen werden wie folgt kodiert:

- **Primaer:** FO (Fortschrittsbewertung)
- **Sekundaer:** ZP (Timeline-Marker)
- **Ausnahme:** WV nur dann, wenn die AGI-Timeline explizit in ein umfassendes Zukunftsnarrativ eingebettet ist ("AGI wird kommen und alles veraendern -- die Menschheit wird nie mehr dieselbe sein")

| Aussage | Kodierung |
|---------|-----------|
| "AGI bis 2027" | FO + ZP |
| "AGI in 5-10 Jahren" | FO + ZP |
| "AGI wird alles aendern, die Menschheit steht an einer Schwelle" | WV + ZP |

---

## 5. Spezialfaelle und Grenzfaelle

Die folgenden konstruierten Beispiele illustrieren schwierige Kodierentscheidungen.

---

**Grenzfall 1: Zukunftsvision mit oekonomischem Fokus**

> "Within twenty years, AI will have created more economic value than the entire current global economy. This isn't just a new technology -- it's a new economic paradigm."

**Kodierung:** AR + WV, OPT, ZP
**Begruendung:** Primaer AR wegen des oekonomischen Gehalts. Dual-Coding WV, weil "neues oekonomisches Paradigma" ein Gesamtnarrativ formuliert. ZP wegen "within twenty years".

---

**Grenzfall 2: Ethische Forderung mit Regulierungsbezug**

> "It would be morally unconscionable to deploy these systems without mandatory independent safety audits."

**Kodierung:** ET + RE, PES
**Begruendung:** Dual-Coding gerechtfertigt. "Morally unconscionable" = ET (Werturteil). "Mandatory independent safety audits" = RE (konkreter Mechanismus).

---

**Grenzfall 3: Menschenbild oder Transhumanismus?**

> "The human brain processes information at roughly 10 petaflops -- but that's not a ceiling, it's a starting point."

**Kodierung:** TR, OPT
**Begruendung:** Der erste Halbsatz ist deskriptiv (MB), aber der zweite Halbsatz ("starting point") transformiert die Aussage in eine transhumanistische Projektion. TR hat Vorrang, weil die Gesamtaussage in Richtung Erweiterung deutet.

---

**Grenzfall 4: Risiko oder Gesellschaft?**

> "AI-powered surveillance will fundamentally erode privacy and enable authoritarian control."

**Kodierung:** GE + RI, PES
**Begruendung:** Dual-Coding. "Erode privacy" = GE (gesellschaftliche Konsequenz). "Enable authoritarian control" = RI (Missbrauchsrisiko). Der Uebergang ist fliessend.

---

**Grenzfall 5: Selbstbild oder Epistemik?**

> "I've been thinking about this problem for longer than most people in this room have been alive. I think I see something they don't."

**Kodierung:** EP, AMB, BIO
**Begruendung:** Primaer EP, weil die Aussage einen ueberlegenen Wissensanspruch formuliert ("I see something they don't"). BIO-Marker wegen biographischer Legitimation ("longer than most people..."). Nicht SB, weil es nicht um Identitaetskonstruktion geht, sondern um epistemische Positionierung.

---

**Grenzfall 6: Open Source als Machtfrage oder Ethik?**

> "Open-sourcing our model is the right thing to do -- and it also prevents any single company from owning the future of intelligence."

**Kodierung:** ET + MA, OPT, HA
**Begruendung:** Dual-Coding. "Right thing to do" = ET (Werturteil). "Prevents any single company from owning" = MA (Machtanalyse). HA-Marker, weil ein konkretes Handeln (Open-Sourcing) referenziert wird.

---

**Grenzfall 7: Fortschritt oder Weltvision?**

> "GPT-5 will be to GPT-4 what GPT-4 was to GPT-3. The rate of improvement is staggering."

**Kodierung:** FO, OPT
**Begruendung:** Reine Fortschrittsbewertung. Kein Gesamtnarrativ (WV), weil keine uebergreifende Zukunftsvision formuliert wird. Nur Bewertung des Entwicklungstempos.

---

**Grenzfall 8: Provokante strategische Kommunikation**

> "Anyone who calls for an AI pause is either naive or protecting their market position."

**Kodierung:** FO, AMB, PRO, STR
**Begruendung:** FO, weil die Aussage implizit den Fortschritt verteidigt. PRO wegen der provokanten Formulierung. STR, weil die Aussage erkennbar strategisch Pause-Befuerworter delegitimiert. AMB, weil die Tonalitaet weder rein positiv noch negativ ist, sondern angriffslustig.

---

**Grenzfall 9: Existenzielles oder Menschenbild?**

> "If we create true artificial consciousness, we will have to fundamentally rethink what it means to be human."

**Kodierung:** SP/EX + MB, AMB
**Begruendung:** Dual-Coding. "True artificial consciousness" = SP/EX (Bewusstseinsfrage). "Rethink what it means to be human" = MB (anthropologische Neubewertung). Nicht TR, weil es nicht um Transformation des Menschen geht, sondern um konzeptionelle Neubewertung.

---

**Grenzfall 10: Regulierung oder Macht?**

> "We need antitrust action against the big AI labs before they become more powerful than governments."

**Kodierung:** RE + MA, PES
**Begruendung:** Dual-Coding. "Antitrust action" = RE (konkreter Regulierungsvorschlag). "More powerful than governments" = MA (Machtanalyse).

---

**Grenzfall 11: Arbeit oder Gesellschaft?**

> "Universal basic income funded by an AI tax is the only way to maintain social stability as automation accelerates."

**Kodierung:** AR + GE, PES
**Begruendung:** Dual-Coding. "AI tax" und "automation" = AR (oekonomischer Mechanismus). "Social stability" = GE (gesellschaftliche Konsequenz). UBI als Brueckenthema rechtfertigt Dual-Coding.

---

**Grenzfall 12: Epistemik mit Risikobezug**

> "The truth is, we have no idea how to make these systems reliably safe. Anyone who says otherwise is lying."

**Kodierung:** EP + RI, PES, PRO
**Begruendung:** Dual-Coding. "We have no idea" = EP (epistemische Grenze). "Reliably safe" = RI (Sicherheitsproblem). PRO wegen "lying".

---

**Grenzfall 13: Handlungsbezogene Inkongruenz**

> "Safety is our number one priority." (Gesagt von einer Person, die dokumentiert Sicherheitsteams verkleinert hat)

**Kodierung:** RI, OPT, HA, STR, KON
**Begruendung:** RI als primaere Kategorie (Sicherheitsthema). HA wegen Handlungsbezug. STR wegen erkennbar strategischer Kommunikation. KON wegen des Widerspruchs zwischen Rhetorik und dokumentiertem Handeln.

---

**Grenzfall 14: Spirituell oder philosophisch?**

> "When I interact with these models, I sometimes feel I'm in the presence of something that transcends mere computation."

**Kodierung:** SP/EX, AMB, PHI
**Begruendung:** SP/EX wegen des Transzendenzbezugs ("transcends"). PHI-Marker wegen der philosophischen Reflexion. Nicht MB, weil es nicht um die menschliche Natur geht, sondern um eine quasi-spirituelle Erfahrung.

---

**Grenzfall 15: Geopolitik als Macht- oder Regulierungsfrage?**

> "If Europe keeps regulating while China keeps building, the balance of power will shift irreversibly."

**Kodierung:** MA, PES, POL
**Begruendung:** Primaer MA (geopolitische Machtverschiebung). Nicht RE, obwohl Regulierung erwaehnt wird -- die Aussage *bewertet* Regulierung hinsichtlich ihrer Machtkonsequenzen, sie *fordert* keine konkreten Mechanismen. POL wegen des expliziten geopolitischen Gehalts.

---

## 6. Prozess

### 6.1 Kodier-Workflow

Der folgende Workflow ist fuer jede einzelne Aussage durchzufuehren:

```
Schritt 1: Aussage vollstaendig lesen
    |
    v
Schritt 2: Primaere Kategorie(n) bestimmen (1-2)
    |   - Kernfrage identifizieren: Worum geht es primaer?
    |   - Spezifischste Kategorie waehlen (Hierarchisches Prinzip)
    |   - Ggf. zweite Kategorie bei genuiner Ueberlappung
    |
    v
Schritt 3: Tonalitaet bestimmen (genau eine)
    |   - OPT: Eindeutig positiv
    |   - PES: Eindeutig negativ
    |   - AMB: Gemischt oder unklar (Defaultwert bei Unsicherheit)
    |
    v
Schritt 4: Modus-Marker pruefen (0-n)
    |   - POL: Politischer Gehalt?
    |   - PHI: Philosophische Reflexion?
    |   - EMP: Empirische Stuetzung?
    |   - ANE: Anekdotische Stuetzung?
    |   - PRO: Provokante Formulierung?
    |   - HA:  Bezug zu konkreter Handlung?
    |   - STR: Strategische Kommunikation erkennbar?
    |
    v
Schritt 5: Struktur-Marker pruefen (0-n)
    |   - KON: Widerspruch/Uebereinstimmung Rhetorik vs. Handeln?
    |   - ZP:  Explizite Zeitangabe vorhanden?
    |   - BIO: Biographische Legitimation?
    |
    v
Schritt 6: Qualitaetskontrolle
    |   - Ist die primaere Kategorie die spezifischste?
    |   - Ist die Tonalitaet konsistent?
    |   - Bei Unsicherheit: grenzfall = 1 setzen
    |
    v
Schritt 7: Kodierung in aussagen_kategorien speichern
```

### 6.2 Entscheidungshilfen

**Schnelltest fuer primaere Kategorie:**

| Frage | Wenn ja: |
|-------|----------|
| Formuliert die Aussage ein Gesamtnarrativ ueber die Zukunft? | WV |
| Beschreibt die Person sich selbst, ihre Rolle oder Motivation? | SB |
| Geht es darum, was der Mensch *ist*? | MB |
| Geht es um Wissensgrenzen oder Erkenntnissicherheit? | EP |
| Formuliert die Aussage ein moralisches Urteil oder Wertprinzip? | ET |
| Benennt die Aussage nicht-oekonomische gesellschaftliche Folgen? | GE |
| Warnt die Aussage vor konkreten Gefahren? | RI |
| Bewertet die Aussage das Tempo oder den Charakter des Fortschritts? | FO |
| Analysiert die Aussage Machtverhaeltnisse oder Kontrollstrukturen? | MA |
| Geht es um Jobs, Geschaeftsmodelle oder oekonomische Effekte? | AR |
| Geht es um die technologische Transformation des Menschen? | TR |
| Schlaegt die Aussage konkrete Governance-Mechanismen vor? | RE |
| Hat die Aussage einen existenziellen, spirituellen oder Bewusstseins-Bezug? | SP/EX |

### 6.3 Qualitaetssicherung

#### Reliabilitaetstest

| Parameter | Wert |
|-----------|------|
| Stichprobenumfang | 50 Aussagen (Zufallsauswahl, stratifiziert nach Personen) |
| Kodierer | Zwei unabhaengige Kodierer (Mensch und/oder LLM) |
| Uebereinstimmungsmass | Cohen's Kappa (kappa) |
| Akzeptanzschwelle primaere Kategorien | kappa >= 0.6 (substanziell) |
| Akzeptanzschwelle Tonalitaet | kappa >= 0.7 (substanziell bis ausgezeichnet) |
| Akzeptanzschwelle sekundaere Marker | kappa >= 0.5 (moderat) |

#### Vorgehen bei mangelnder Uebereinstimmung

1. **kappa < 0.6 fuer eine primaere Kategorie:**
   - Definition ueberarbeiten
   - Inklusions-/Exklusionskriterien schaerfen
   - Zusaetzliche Ankerbeispiele hinzufuegen
   - Erneuter Reliabilitaetstest mit neuer Stichprobe

2. **kappa < 0.5 fuer einen sekundaeren Marker:**
   - Marker-Definition praezisieren
   - Pruefung, ob Marker zu subjektiv ist (insbesondere STR, PRO)
   - Ggf. Marker-Definition einschraenken oder Marker streichen

3. **Systematische Disagreements:**
   - Diskrepanzanalyse: Welche Kategorien werden systematisch verwechselt?
   - Abgrenzungsregeln ueberarbeiten
   - Ggf. Kategorien zusammenlegen oder weiter differenzieren

#### Dokumentation

Alle Kodierentscheidungen bei Grenzfaellen werden mit Begruendung dokumentiert. Die Spalte `grenzfall` in der Datenbank markiert Aussagen, bei denen der Kodierer unsicher war. Diese Grenzfaelle werden im Reliabilitaetstest priorisiert.

### 6.4 Spezielle Hinweise fuer LLM-Kodierer

Wenn ein LLM als Kodierer eingesetzt wird, gelten zusaetzlich:

1. **Konsistenz:** Das LLM soll bei identischem Input identischen Output produzieren. Temperatur = 0 oder niedrig.
2. **Begruendungspflicht:** Fuer jede Kodierung soll das LLM eine kurze Begruendung liefern (1-2 Saetze).
3. **Grenzfall-Markierung:** Bei Unsicherheit soll das LLM explizit `grenzfall = 1` setzen und die Unsicherheit dokumentieren.
4. **Keine Halluzination:** Das LLM kodiert nur das, was in der Aussage steht. Kein Hintergrundwissen ueber die Person einfliessen lassen, ausser fuer den KON-Marker (dort ist Kontextwissen noetig).
5. **Batch-Verarbeitung:** Aussagen werden einzeln kodiert. Keine Muster aus vorherigen Aussagen uebertragen.

---

## Anhang A: Vollstaendige Kategorie-Code-Tabelle

| Code | Name | Typ | Pflicht |
|------|------|-----|---------|
| WV | Weltvision | Primaer | Min. 1 primaere Kategorie |
| SB | Selbstbild | Primaer | |
| MB | Menschenbild | Primaer | |
| EP | Epistemik/Wissensanspruch | Primaer | |
| ET | Ethik/Werte | Primaer | |
| GE | Gesellschaft | Primaer | |
| RI | Risiko/Sicherheit | Primaer | |
| FO | Fortschritt/Beschleunigung | Primaer | |
| MA | Macht/Kontrolle | Primaer | |
| AR | Arbeit/Wirtschaft | Primaer | |
| TR | Transhumanismus | Primaer | |
| RE | Regulierung | Primaer | |
| SP/EX | Spiritualitaet/Existenzielles | Primaer | |
| OPT | Optimistisch | Tonalitaet | Genau 1 |
| PES | Pessimistisch | Tonalitaet | |
| AMB | Ambivalent | Tonalitaet | |
| POL | Politisch | Modus | Optional |
| PHI | Philosophisch | Modus | Optional |
| EMP | Empirisch | Modus | Optional |
| ANE | Anekdotisch | Modus | Optional |
| PRO | Provokant | Modus | Optional |
| HA | Handlungsbezug | Modus | Optional |
| STR | Strategisch | Modus | Optional |
| KON | Kongruenz/Inkongruenz | Struktur | Optional |
| ZP | Zeitprognose | Struktur | Optional |
| BIO | Biographische Legitimation | Struktur | Optional |

## Anhang B: Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| WV statt FO bei Tempobewertung | FO fuer Tempo-/Fortschrittsbewertung, WV nur fuer Gesamtnarrative |
| ET statt RE bei konkreten Vorschlaegen | RE fuer konkrete Mechanismen, ET fuer Wertprinzipien |
| MB statt TR bei Projektionen | TR wenn es um das *Werden* geht, MB nur fuer das *Sein* |
| SB statt EP bei Wissensanspruechen | EP fuer epistemische Positionierung, SB fuer Identitaet |
| GE statt AR bei oekonomischen Themen | AR fuer alles Oekonomische, GE fuer nicht-oekonomische Gesellschaftsfragen |
| Fehlende Tonalitaet | Jede Aussage benoetigt genau einen Tonalitaets-Marker |
| Drei oder mehr primaere Kategorien | Maximum zwei primaere Kategorien (Dual-Coding) |
| Open Source als eigene Kategorie | Open Source ist Instrument, kodiere unter dem bedienten Thema |
| KON ohne Handlungswissen | KON erfordert dokumentiertes Wissen ueber Handlungen der Person |
| STR bei bloss moeglicher Strategie | STR nur bei *erkennbar* strategischer Kommunikation |

## Anhang C: Aenderungsprotokoll

| Version | Datum | Aenderung |
|---------|-------|-----------|
| 1.0 | 2026-02-12 | Initiale Erstellung des Codier-Leitfadens |

---

*Dieser Leitfaden ist ein lebendes Dokument. Aenderungen werden im Aenderungsprotokoll dokumentiert und erfordern einen erneuten Reliabilitaetstest fuer betroffene Kategorien.*
