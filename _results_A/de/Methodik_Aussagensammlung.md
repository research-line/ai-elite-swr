# Methodik: Systematische Aussagensammlung der Top 100 KI-Persoenlichkeiten

**Forschungsprojekt:** Transhumanismus / Silicon Valley Worldviews
**Datum:** 2026-02-11 (erstellt), 2026-02-11 (revidiert v2)
**Datenbank:** `_data/aussagen_top100.db` (SQLite)
**Methodischer Ansatz:** Induktiv / Grounded Theory (Strauss & Corbin)

---

## 1. Forschungsziel

**Leitfrage:** Was denkt die KI-Elite ueber sich selbst, die Welt und die Menschheit?

Systematische Sammlung und induktive Kategorisierung von oeffentlichen Aussagen der 100 einflussreichsten KI-Persoenlichkeiten (gem. Top100-Recherche vom 2026-02-11). Ziel ist die Rekonstruktion von **Weltbildern, Selbstbildern und Zukunftsvisionen** dieser Personen -- nicht durch vorab definierte Kategorien, sondern durch datengesteuertes Entdecken von Mustern.

**Ergaenzend:** Triangulation durch Handlungsanalyse -- Stimmen Aussagen mit beobachtbarem Handeln (Investitionen, Umstrukturierungen, politische Aktivitaeten) ueberein?

---

## 2. Erhebungszeitraum

**Primaerer Erhebungszeitraum:** 01.01.2010 -- 11.02.2026 (16 Jahre)

| Zeitraum | Begruendung | Erwartete Datendichte |
|----------|-------------|----------------------|
| 2000-2009 | Kontextphase. Fruehe Karrieren, Gruendungen (Google 1998, Facebook 2004, Tesla 2003). Nur bei prominenten Personen systematisch durchsuchbar. | Sehr gering -- nur fuer Top-20 lohnend |
| 2010-2015 | Aufbauphase. Deep Learning Durchbruch (ImageNet 2012), erste oeffentliche KI-Debatten. Viele heutige Akteure noch wenig oeffentlich. | Gering bis mittel |
| 2016-2019 | Beschleunigungsphase. AlphaGo (2016), Transformer-Paper (2017), GPT-2 (2019). KI wird oeffentliches Thema. | Mittel bis hoch |
| 2020-2023 | Explosionsphase. GPT-3, DALL-E, ChatGPT (Nov 2022). Massive Medienpraesenz aller Top-100-Personen. | Sehr hoch |
| 2024-2026 | Konsolidierung. AGI-Debatten, Regulierung, KI-Milliardaere, politische Dimension. | Sehr hoch |

**Praktische Konsequenz:**
- Phase 2010-2026 wird systematisch durchsucht
- Phase 2000-2009 wird opportunistisch erfasst (nur wenn bei Suche gefunden)
- Alle Aussagen erhalten ein `datum_aussage` -- die Zeitraum-Filterung erfolgt spaeter in der Analyse, NICHT beim Sammeln

---

## 3. Datenquellen und Plattformen

### 3.1 Primaere Quellen (hoechste Ergiebigkeit)

| Plattform | Typ | Suchstrategie | Erwartete Ergiebigkeit |
|-----------|-----|---------------|----------------------|
| YouTube | Video-Interviews, Keynotes, Panels | Name + Keyword | Sehr hoch |
| Twitter/X | Posts, Threads, Replies | Profil-Durchsicht + Keyword | Hoch |
| Podcasts | Langform-Interviews | Lex Fridman, All-In, etc. | Sehr hoch |
| Konferenzen | Vortraege, Panels | TED, NeurIPS, Davos, SXSW | Hoch |
| Nachrichtenmedien | Interviews, Profile | NYT, WSJ, Bloomberg, CNBC | Hoch |

### 3.2 Sekundaere Quellen

| Plattform | Typ | Suchstrategie | Erwartete Ergiebigkeit |
|-----------|-----|---------------|----------------------|
| LinkedIn | Posts, Artikel | Profil-Durchsicht | Mittel |
| Reddit | AMAs, Kommentare | r/MachineLearning, r/technology | Mittel |
| Buecher/Aufsaetze | Monographien, Gastbeitraege | Amazon, Google Scholar | Mittel |
| Blogs | Persoenliche Blogs, Firmenblogs | Google-Suche | Mittel |
| Congressional Testimonies | Offizielle Anhoerungen | senate.gov, house.gov | Niedrig |

### 3.3 Tertiare Quellen (Aggregatoren)

| Plattform | Typ | Suchstrategie |
|-----------|-----|---------------|
| Wikiquote | Zitatesammlungen | Direkte Abfrage |
| Goodreads | Buchzitate | Autorenprofil |
| BrainyQuote | Allgemeine Zitate | Namenssuche |
| Substack | Newsletter | Autorensuche |

---

## 4. Suchbegriffe (Search Terms)

### 4.1 Personen-Identifier
Jede Suche wird mit dem **vollstaendigen Namen** der Person kombiniert.

### 4.2 Inhaltliche Suchbegriffe (mit Person kombinieren)

**Kategorie A: Weltbild / Zukunftsvision**
- "future of humanity", "future of AI", "Zukunft der Menschheit"
- "vision for the world", "world in 10 years", "world in 2030"
- "society", "civilization", "Gesellschaft"
- "superintelligence", "AGI", "artificial general intelligence"
- "singularity", "post-human", "transhumanism"

**Kategorie B: Selbstbild / Identitaet**
- "my mission", "what drives me", "why I do this"
- "my philosophy", "I believe", "my worldview"
- "responsibility", "legacy", "Verantwortung"

**Kategorie C: Ethik / Werte**
- "AI safety", "AI risk", "existential risk"
- "AI ethics", "alignment", "beneficial AI"
- "inequality", "power", "democracy"
- "open source vs closed", "regulation"

**Kategorie D: Menschenbild**
- "what makes us human", "consciousness"
- "human intelligence vs AI", "uniquely human"
- "creativity", "meaning", "purpose"
- "jobs", "work", "automation", "replacement"

**Kategorie E: Technologie und Gesellschaft**
- "technology and society", "progress"
- "disruption", "innovation", "acceleration"
- "universal basic income", "UBI", "wealth distribution"
- "education", "healthcare", "climate"

**Kategorie F: Alltag / Informelles** (NEU -- auch alltaegliche Aussagen koennen aufschlussreich sein)
- "I think", "personally", "honestly"
- "my kids", "my family", "when I was young"
- "what I learned", "mistake", "failure"
- "fun", "hobby", "life"

### 4.3 Plattformspezifische Suchen
- YouTube: `"[Name]" interview philosophy | vision | future | humanity | believes`
- Twitter/X: `from:[handle] (believe OR future OR humanity OR world OR society OR vision)`
- Google: `"[Name]" "I believe" OR "my vision" OR "humanity" OR "future" site:nytimes.com OR site:wsj.com OR site:bloomberg.com`

---

## 5. Sprachregelung

**Grundregel:** Alle Aussagen werden in der **Originalsprache** erfasst (`aussage_text`).

| Feld | Inhalt |
|------|--------|
| `aussage_text` | Originalwortlaut in Originalsprache |
| `sprache` | Sprachcode des Originals (en, de, zh, ja, fr, ...) |
| `aussage_uebersetzung_de` | Deutsche Uebersetzung (wird spaeter ergaenzt, anfangs leer) |

Die Uebersetzung erfolgt erst in einer separaten Phase, um den Erhebungsprozess nicht zu verlangsamen und Uebersetzungsfehler vom Originalzitat zu trennen.

---

## 6. Methodischer Ansatz: Induktive Kategorienbildung

### 6.1 Warum NICHT vorab filtern?

Die urspruengliche Methodik (v1) definierte Einschluss- und Ausschlusskriterien VOR der Datenerhebung. Das birgt Risiken:

1. **Vorab-Ausschluss verzerrt:** "Rein technische" Aussagen koennen implizite Weltbilder enthalten ("Wir brauchen mehr Compute" -> Fortschrittsglaube)
2. **Alltaegliches ist aufschlussreich:** Wie jemand ueber Familie, Freizeit oder Fehler spricht, verraet Werte
3. **Kategorien-Zwang:** Vorab-Kategorien lenken den Blick und verhindern das Entdecken unerwarteter Muster
4. **Datenverlust:** Zu fruehes Ausschliessen ist irreversibel

### 6.2 Revidierter Ansatz: Grounded Theory (Strauss & Corbin)

```
PRINZIP: Erst sammeln, dann sichten, dann Kategorien bilden,
         dann zuordnen, dann Ein-/Ausschluss definieren,
         dann filtern.
```

Die Kategorien in Abschnitt 7 (WV, SB, MB, ...) dienen als **Sensitizing Concepts** -- sie lenken die Aufmerksamkeit, sind aber NICHT bindend. Neue Kategorien koennen und sollen aus den Daten entstehen.

---

## 7. Vorlaeufige Kategorien (Sensitizing Concepts)

### 7.1 Primaere Inhaltskategorien (vorlaeufig, aenderbar)

| Code | Kategorie | Beschreibung | Beispiel |
|------|-----------|-------------|---------|
| WV | Weltvision | Aussagen ueber die Zukunft der Welt/Menschheit | "AI will be the most transformative technology in human history" |
| SB | Selbstbild | Aussagen ueber die eigene Rolle, Mission, Motivation | "I feel a deep responsibility to get this right" |
| MB | Menschenbild | Aussagen ueber das Wesen des Menschen, Bewusstsein | "What makes us human is our ability to..." |
| ET | Ethik/Werte | Aussagen ueber Moral, Verantwortung, richtig/falsch | "We have an obligation to ensure AI benefits everyone" |
| GE | Gesellschaft | Aussagen ueber Gesellschaftsstruktur, Ungleichheit, Politik | "The wealth created by AI must be distributed more broadly" |
| RI | Risiko/Sicherheit | Aussagen ueber KI-Risiken, existenzielle Bedrohung | "The probability of doom is..." |
| FO | Fortschritt/Beschleunigung | Aussagen ueber Tempo, Disruption, Acceleration | "We're moving faster than anyone expected" |
| MA | Macht/Kontrolle | Aussagen ueber Machtkonzentration, Zugang, Kontrolle | "Open source ensures no single entity controls AI" |
| AR | Arbeit/Wirtschaft | Aussagen ueber Arbeitsmarkt, UBI, Automatisierung | "Most jobs will be transformed within a decade" |
| TR | Transhumanismus | Aussagen ueber Verschmelzung Mensch-Maschine, Post-Humanity | "Brain-computer interfaces will extend human cognition" |
| RE | Regulierung | Aussagen ueber Gesetze, Governance, internationale Kooperation | "We need global AI governance frameworks" |
| SP | Spiritualitaet/Sinn | Aussagen ueber Sinn, Zweck, Spiritualitaet, Transzendenz | "AI raises profound questions about consciousness" |

**Hinweis:** Diese Kategorien werden nach Phase 2 (Stichproben-Sichtung) ueberarbeitet. Neue Kategorien koennen hinzukommen, bestehende koennen zusammengelegt oder aufgeteilt werden.

### 7.2 Sekundaere Codes (ergaenzend, Mehrfachzuordnung moeglich)

| Code | Beschreibung |
|------|-------------|
| OPT | Optimistischer Tenor |
| PES | Pessimistischer Tenor |
| AMB | Ambivalenter Tenor |
| POL | Politisch konnotiert |
| PHI | Philosophisch reflektiert |
| EMP | Empirisch gestuetzt |
| ANE | Anekdotisch |
| PRO | Provokant/Kontrovers |
| HA | Handlungsbezug -- Aussage steht in Bezug zu konkreter Handlung |

---

## 8. Handlungsanalyse: Sagen vs. Handeln

### 8.1 Konzept

Aussagen allein sind unzureichend, um Weltbilder zu rekonstruieren. Menschen koennen bewusst oder unbewusst anders handeln als sie sprechen. Daher wird parallel zu den Aussagen eine **Handlungsdatenbank** gefuehrt.

### 8.2 Erfasste Handlungstypen

| Typ | Beschreibung | Beispiel |
|-----|-------------|---------|
| investition | Finanzielle Beteiligung an Unternehmen/Projekten | Bezos investiert $4 Mrd. in Anthropic |
| verkauf | Abstossung von Anteilen/Assets | Musk verkauft Tesla-Aktien |
| kauf | Uebernahme von Firmen/Assets | Microsoft kauft Activision |
| umstrukturierung | Organisatorische Veraenderungen | OpenAI wandelt sich in For-Profit |
| gruendung | Neue Firmengründung | Sutskever gruendet Safe Superintelligence |
| ruecktritt | Aufgabe einer Position | Hinton verlaesst Google |
| entlassung | Personalabbau | Meta entlaesst 11.000 Mitarbeiter |
| einstellung | Signifikante Personalentscheidungen | Anthropic stellt ex-OpenAI Safety-Team ein |
| lobbying | Politische Einflussnahme | Tech-CEOs treffen Biden/Trump |
| spende | Philantropische Aktivitaeten | Altman spendet $8M an GiveDirectly UBI |
| klage | Rechtliche Auseinandersetzungen | NYT vs. OpenAI |
| partnerschaft | Strategische Kooperationen | Google + Anthropic Cloud-Deal |
| produktlaunch | Produktveroeffenlichungen | Release von GPT-4, Claude 3, Gemini |
| politisch | Politische Aktivitaeten/Aemter | Sacks wird AI Czar |
| sonstiges | Andere relevante Handlungen | - |

### 8.3 Verknuepfung Aussage <-> Handlung

Jede Aussage kann mit null oder mehreren Handlungen verknuepft werden:

| Beziehungstyp | Beschreibung | Beispiel |
|---------------|-------------|---------|
| `konsistent` | Handlung passt zur Aussage | Sagt "AI safety first" + investiert in Safety-Forschung |
| `widerspruch` | Handlung widerspricht der Aussage | Sagt "Open Source ist wichtig" + schliesst Modell-Zugang |
| `unklar` | Beziehung nicht eindeutig bestimmbar | - |
| `kontext` | Handlung liefert Kontext fuer die Aussage | Sagt "Wir mussten handeln" nach Entlassungswelle |

---

## 9. Workflow: Revidierter 7-Phasen-Prozess

```
Phase 1: BREITE SAMMLUNG (keine Filter, keine Kategorien)
======================================================
  Fuer jede Person der Top 100:
  1. YouTube-Suche (Top-5-Interviews, auch aeltere)
  2. Twitter/X-Profildurchsicht (Top-Posts, auch alltaegliche)
  3. Google News (prominente Interviews 2010-2026)
  4. Podcast-Suche (Lex Fridman, All-In, etc.)
  5. Aggregatoren (Wikiquote, BrainyQuote, etc.)
  -> ALLES erfassen was die Person gesagt hat
  -> einschluss = 1 (default), kategorie = leer
  -> Originalsprache, keine Uebersetzung
  -> Parallel: Handlungen erfassen (Investments, Gruendungen, etc.)

Phase 2: STICHPROBEN-SICHTUNG (induktiv)
======================================================
  Zufaellige Stichprobe von ~10 Aussagen pro Person (Top 20 Personen):
  1. Was faellt auf? Welche Themen tauchen auf?
  2. Welche Aussagen passen in keine vorab-Kategorie?
  3. Welche neuen Kategorien draengen sich auf?
  4. Wie reden diese Personen? (Stil, Framing, Selbstinszenierung)
  -> MEMO schreiben: Was habe ich entdeckt?
  -> Kategorien-System ueberarbeiten

Phase 3: KATEGORIENBILDUNG (datengesteuert)
======================================================
  Basierend auf Phase-2-Erkenntnissen:
  1. Vorlaeufige Kategorien bestaetigen, aendern, ergaenzen
  2. Neue Kategorien in DB anlegen
  3. Kategoriendefinitionen verschaerfen (Abgrenzungsregeln)
  4. Codier-Leitfaden erstellen
  -> Ergebnis: Finales Kategoriensystem

Phase 4: SYSTEMATISCHE KODIERUNG
======================================================
  Alle gesammelten Aussagen durchgehen:
  1. Primaere Kategorie(n) zuweisen
  2. Sekundaere Codes ergaenzen (OPT, PES, PHI, ...)
  3. Handlungsbezuege herstellen (HA-Code + Verknuepfung)
  4. Grenzfaelle markieren (grenzfall = 1)
  5. Originalitaets-Check: Gleiche Aussage in mehreren Quellen?
     -> Originalitaets-Zaehler hochsetzen

Phase 5: EIN-/AUSSCHLUSS DEFINIEREN (erst jetzt!)
======================================================
  Basierend auf den kodierten Daten:
  1. Welche Kategorien sind fuer die Forschungsfrage relevant?
  2. Welche Aussagetypen liefern keine Erkenntnisse?
  3. Einschlusskriterien formulieren (datengestuetzt)
  4. Ausschlusskriterien formulieren (datengestuetzt)
  -> Kriterien dokumentieren mit Begruendung
  -> Kriterien an 50 Aussagen testen (Pilottest)

Phase 6: FILTERUNG UND QUALITAETSSICHERUNG
======================================================
  1. Ein-/Ausschlusskriterien anwenden -> einschluss = 0 fuer Ausgeschlossene
  2. Qualitaetskontrolle: Quellen korrekt? Zitate wortgetreu?
  3. Deutsche Uebersetzungen ergaenzen (fuer eingeschlossene Aussagen)
  4. Handlungs-Konsistenzpruefung: Widersprueche markieren

Phase 7: ANALYSE -- Was denkt die KI-Elite?
======================================================
  1. Haeufigkeitsanalyse: Welche Kategorien dominieren?
  2. Personenprofile: Weltbild-Profil pro Person
  3. Sagen-vs-Handeln: Wo gibt es Widersprueche?
  4. Netzwerkanalyse: Wer teilt Positionen? Wer widerspricht wem?
  5. Zeitverlauf: Aendern sich Positionen ueber die Jahre?
  6. Cluster-Analyse: Lassen sich Weltbild-Typen identifizieren?
  7. Synthese: Was ist das Kollektiv-Weltbild der KI-Elite?
```

---

## 10. Voruebergehende Einschlusskriterien (Phase 1 -- nur formale Kriterien)

Waehrend der breiten Sammlung (Phase 1) gelten NUR formale Mindestkriterien:

| Nr. | Kriterium | Beschreibung |
|-----|-----------|-------------|
| F1 | Person in Top 100 | Aussage stammt von einer Person der Top-100-Liste |
| F2 | Attribuierbarkeit | Aussage ist der Person eindeutig zuordenbar |
| F3 | Oeffentlichkeit | Aussage wurde oeffentlich gemacht (kein Leak) |
| F4 | Originalwortlaut | Originaltext verfuegbar (keine reine Paraphrase) |

**KEIN inhaltlicher Filter in Phase 1.** Auch alltaegliche, technische oder scheinbar irrelevante Aussagen werden erfasst. Der inhaltliche Filter kommt erst in Phase 5.

---

## 11. Datenbank-Schema (v2)

Siehe `_data/aussagen_top100.db` (SQLite).

### Tabellen:
1. **personen** - Die 100 Personen (aus Top-100-Recherche)
2. **aussagen** - Alle Aussagen/Zitate (Originalsprache + Uebersetzungsfeld)
3. **kategorien** - Lookup-Tabelle fuer Kategorie-Codes (erweiterbar)
4. **aussagen_kategorien** - n:m-Zuordnung Aussage <-> Kategorien
5. **quellen_typen** - Lookup-Tabelle fuer Quellenarten
6. **plattformen** - Lookup-Tabelle fuer Plattformen
7. **suchprotokolle** - Dokumentation jeder durchgefuehrten Suche
8. **handlungen** - Beobachtbare Handlungen der Personen (NEU)
9. **aussagen_handlungen** - Verknuepfung Aussage <-> Handlung mit Beziehungstyp (NEU)

### ER-Diagramm (v2):

```
personen 1----n aussagen n----m kategorien
    |              |
    |              |-----> quellen_typen
    |              |-----> plattformen
    |              |
    |              n----m handlungen (via aussagen_handlungen)
    |                       |
    1-----------n-----------+
                    (person_id)

suchprotokolle (dokumentiert den Prozess, verknuepft mit Person + Plattform)
```

### Views:
1. **v_aussagen_komplett** - Aussage mit Person, Plattform, Quellentyp, Uebersetzung
2. **v_aussagen_mit_kategorien** - Aussagen mit zugeordneten Kategorien
3. **v_statistik_personen** - Zaehler pro Person (eingeschlossen/ausgeschlossen/grenzfaelle)
4. **v_statistik_kategorien** - Zaehler pro Kategorie
5. **v_sagen_vs_handeln** - Vergleichsansicht Aussagen vs. Handlungen (NEU)

---

## 12. Limitationen

1. **Selektionsbias:** Nur oeffentliche Aussagen; private Ueberzeugungen koennen abweichen
2. **Kontextabhaengigkeit:** Aussagen in Interviews koennen strategisch motiviert sein
3. **Sprachbias:** Primaer englischsprachige Quellen
4. **Plattformbias:** Twitter/YouTube ueberrepraesentiert gegenueber Buechern/Aufsaetzen
5. **Zeitbias:** Neuere Aussagen (2020+) sind deutlich leichter auffindbar als aeltere (2010-2015)
6. **Kategorisierungsbias:** Trotz induktivem Ansatz bleibt die Zuordnung subjektiv
7. **Vollstaendigkeit:** Nicht alle Aussagen aller 100 Personen koennen erfasst werden
8. **Handlungsbias:** Handlungen sind nur teilweise oeffentlich sichtbar; interne Entscheidungen bleiben verborgen
9. **Uebersetzungsbias:** Deutsche Uebersetzungen koennen Nuancen verlieren
10. **Survivorship-Bias:** Nur aktuell einflussreiche Personen; frueher einflussreiche aber inzwischen irrelevante Personen fehlen

---

## 13. Methodische Begruendung: Zeitraum 2010 statt 2016

Die Erweiterung auf 2010 ist sinnvoll weil:

1. **Vor-KI-Boom-Aussagen** zeigen, was diese Personen sagten BEVOR KI zum Mainstream-Thema wurde -- authentischer, weniger PR-gesteuert
2. **Positionsveraenderungen** werden sichtbar: Hat jemand 2012 noch ganz anders ueber KI gesprochen?
3. **Gruendungsmythen** fallen in diesen Zeitraum: DeepMind (2010), Anthropic-Vorgeschichte bei Google Brain (2011)
4. **Datenpraktikabilitaet:** Vor 2010 existieren fuer die meisten Personen kaum oeffentliche Quellen (Ausnahme: Page, Brin, Zuckerberg, Thiel, Musk). Ab 2010 steigt die Verfuegbarkeit merklich.
5. **Deep-Learning-Wende:** Der ImageNet-Durchbruch (2012) und die darauf folgenden Jahre (2013-2015) sind eine Schluesselphase, in der viele Akteure erstmals oeffentlich ueber KI-Zukunft sprachen.

**Erwartete Datenverteilung:**
```
2010-2012:  ~2-5 Aussagen pro Person (nur prominente)     [==]
2013-2015:  ~5-10 Aussagen pro Person                      [====]
2016-2019:  ~10-20 Aussagen pro Person                     [========]
2020-2023:  ~20-50 Aussagen pro Person                     [================]
2024-2026:  ~30-80 Aussagen pro Person                     [====================]
```

---

*Methodik erstellt am 2026-02-11, revidiert am 2026-02-11 (v2)*
*Revision: Grounded-Theory-Ansatz, Zeitraum 2010-2026, Handlungsanalyse, Originalsprache*
*Forschungsprojekt: Transhumanismus / Silicon Valley Worldviews*
