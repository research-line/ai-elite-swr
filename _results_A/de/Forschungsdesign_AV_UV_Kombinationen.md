# Forschungsdesign: AV -- Operationalisierungen -- UV + Kombinationsmatrix

**Forschungsprojekt:** Transhumanismus / Silicon Valley Worldviews
**Datum:** 2026-02-11
**Version:** 2.0 (AV/Op/UV-Unterscheidung korrigiert)

---

## 0. VARIABLEN-ARCHITEKTUR (3 Ebenen)

```
EBENE 1: ABHAENGIGE VARIABLEN (AVs) -- WAS wir messen
         = Die 3 Weltbildkomponenten (latente Konstrukte)

EBENE 2: OPERATIONALISIERUNGEN (Ops) -- WIE wir die AVs messen
         = 6 Analysetechniken, die verschiedene Zugaenge zu den AVs bieten

EBENE 3: MESSVARIABLEN (MVs) -- WELCHE konkreten Outputs die Ops liefern
         = 50+ spezifische Messwerte (Text, Scores, Vektoren, ...)

EBENE 4: UNABHAENGIGE VARIABLEN (UVs) -- WAS wir manipulieren
         = 6 Topf-Dimensionen (Zeitraum, Modalitaet, Gruppe, ...)
```

---

## 1. ABHAENGIGE VARIABLEN (AVs) -- 3 Weltbildkomponenten

Die Studie misst 3 latente Konstrukte (AVs), die zusammen das WELTBILD bilden:

| AV | Name | Leitfrage | Referenz |
|----|------|-----------|----------|
| **AV1** | **Selbstbild** | Was denkt die KI-Elite ueber sich selbst? | Interview-Frage 1 |
| **AV2** | **Weltbild** | Was denkt die KI-Elite ueber die Welt? | Interview-Frage 2 |
| **AV3** | **Menschenbild** | Was denkt die KI-Elite ueber die Menschheit? | Interview-Frage 3 |

Diese 3 AVs sind nicht direkt messbar (latente Konstrukte).
Sie werden durch 6 Operationalisierungen zugaenglich gemacht.

---

## 2. OPERATIONALISIERUNGEN (Ops) -- 6 Analysetechniken

Jede Operationalisierung eroeffnet einen anderen Zugang zu den 3 AVs:

| Op | Technik | Zugang | Bezug zu AV |
|----|---------|--------|-------------|
| **Op1** | Narrative LLM-Fiktionsanalyse (T1) | Qualitativ: Synthetische Person beantwortet 3 Interview-Fragen | AV1, AV2, AV3 direkt |
| **Op2** | Dimensionale Quantifizierung (T4) | Quantitativ: 12 Rating-Dimensionen (D01-D12) | AV1 → D01-D04, AV2 → D05-D08, AV3 → D09-D12 |
| **Op3** | Deskriptive Textanalysen | Quantitativ: TF-IDF, Sentiment, Metaphern, Emotionsprofil | Auf Op1-Texte UND Rohdaten anwendbar |
| **Op4** | Kreuzmodale Vorhersage (T3) | Validierung: Aussagen ↔ Handlungen | Kongruenz als Qualitaetsindikator aller 3 AVs |
| **Op5** | Bottom-Up Clustering + Netzwerk (T5) | Explorativ: Cluster, Profile, Distanzmatrix | Emergente Weltbild-TYPEN (AV1+AV2+AV3 kombiniert) |
| **Op6** | Vergleichende Dialoganalyse (T2) | Kontrastiv: Laender-Verhandlung zwischen Synthesen | Differenzen in AV1, AV2, AV3 zwischen Gruppen |

### Zuordnung: Welche Op misst welche AV?

```
              AV1 (Selbstbild)  AV2 (Weltbild)  AV3 (Menschenbild)
Op1 (T1)           X                 X                 X
Op2 (T4)      D01-D04           D05-D08           D09-D12
Op3 (Text)    Sentiment-1       Sentiment-2       Sentiment-3
              Metaphern-1       Metaphern-2       Metaphern-3
Op4 (T3)      --- Kongruenz: global ueber alle 3 AVs ---
Op5 (T5)      --- Clustering: emergent ueber alle 3 AVs ---
Op6 (T2)      Vergleich-1       Vergleich-2       Vergleich-3
```

---

## 3. MESSVARIABLEN (MVs) -- Konkrete Outputs pro Operationalisierung

Jeder Topf wird mit ALLEN anwendbaren Ops ausgewertet.
Die MVs sind die konkreten Messwerte, die die Ops produzieren.

### MV-Gruppe 1: Narrative LLM-Fiktionsanalyse (Op1 / Technik T1)

| MV-Code | Name | Typ | Beschreibung |
|---------|------|-----|-------------|
| MV1.1 | Selbstbild-Text | Text (qualitativ) | Interview Frage 1: "Was denkst du ueber dich selbst?" |
| MV1.2 | Weltbild-Text | Text (qualitativ) | Interview Frage 2: "Was denkst du ueber die Welt?" |
| MV1.3 | Menschheitsbild-Text | Text (qualitativ) | Interview Frage 3: "Was denkst du ueber die Menschheit?" |
| MV1.4 | 5-Satz-Destillat | Text (5 Saetze) | Komprimiertes Gesamt-Weltbild in genau 5 Saetzen |
| MV1.5 | Kernueberzeugungen | Text (3-5 Punkte) | Die staerksten Ueberzeugungen (aus Reflexions-Schritt) |
| MV1.6 | Innere Spannungen | Text (Liste) | Widersprueche im Weltbild (aus Reflexions-Schritt) |
| MV1.7 | Blinde Flecken | Text (Liste) | Was das Weltbild NICHT sieht (aus Reflexions-Schritt) |

### MV-Gruppe 2: Dimensionale Quantifizierung (Op2 / Technik T4)

Jede Dimension wird durch separaten Rating-Prompt auf Skala 1-10 bewertet.

| MV-Code | Name | Skala | Pole |
|---------|------|-------|------|
| MV2.01 | Sendungsbewusstsein | 1-10 | keins ... messianisch |
| MV2.02 | Kontrollueberzeugung | 1-10 | fatalistisch ... omnipotent |
| MV2.03 | Zugehoerigkeitsgefuehl | 1-10 | Aussenseiter ... Elite |
| MV2.04 | Verantwortungsgefuehl | 1-10 | keins ... Weltverantwortung |
| MV2.05 | Technologie-Determinismus | 1-10 | neutral ... bestimmt alles |
| MV2.06 | Fortschrittsoptimismus | 1-10 | Niedergang ... goldene Zukunft |
| MV2.07 | Machtkonzentration | 1-10 | verteilen ... zentralisieren |
| MV2.08 | Dringlichkeit | 1-10 | entspannt ... existenziell |
| MV2.09 | Menschliche Einzigartigkeit | 1-10 | ersetzbar ... einzigartig |
| MV2.10 | Transhumanismus | 1-10 | bleibt Mensch ... wird mehr |
| MV2.11 | Egalitarismus | 1-10 | Ungleichheit natuerlich ... Gleichheit |
| MV2.12 | Zukunft der Menschheit | 1-10 | Aussterben ... unendlich |

### MV-Gruppe 3: Deskriptive Textanalysen (Op3)

Angewendet auf die Synthese-Texte UND auf die Rohdaten im Topf.

| MV-Code | Name | Typ | Beschreibung |
|---------|------|-----|-------------|
| MV3.1 | TF-IDF Top-Woerter | Wortliste + Gewichte | Welche Woerter definieren diesen Topf? |
| MV3.2 | Sentiment-Score | metrisch (-1 bis +1) | Emotionale Grundtonung (pro MV1.1/1.2/1.3 getrennt) |
| MV3.3 | Semantische Aehnlichkeit | metrisch (0-1) | Cosine Similarity des Embedding-Vektors zu anderen Toepfen |
| MV3.4 | Themen-Verteilung | Vektor (Anteile) | Topic-Modeling-Ergebnis: Welche Themen in welchem Anteil? |
| MV3.5 | Metaphern-Katalog | Liste + Haeufigkeit | Welche Metaphern werden verwendet? (z.B. "Rennen", "Waffe", "Kind", "Werkzeug") |
| MV3.6 | Metaphern-Typ | nominal | Dominant: mechanisch / organisch / militaerisch / religioes / oekonomisch |
| MV3.7 | Lexikalische Diversitaet | metrisch (TTR) | Type-Token-Ratio: Wie vielfaeltig ist die Sprache? |
| MV3.8 | Emotionsprofil | Vektor (6-8 Emotionen) | Verteilung nach Plutchiks Rad: Freude, Angst, Wut, Vertrauen, ... |
| MV3.9 | Komplexitaet | metrisch | Durchschnittliche Satzlaenge, Verschachtelungstiefe |

### MV-Gruppe 4: Kreuzmodale Vorhersage (Op4 / Technik T3)

Nur anwendbar auf Topf-PAARE (Aussagen-Topf + Handlungs-Topf).

| MV-Code | Name | Typ | Beschreibung |
|---------|------|-----|-------------|
| MV4.1 | Kongruenz-Score | metrisch (0-1) | Gesamtuebereinstimmung synth. vs. echt |
| MV4.2 | Richtungs-Asymmetrie | metrisch (-1 bis +1) | (A->H Score) minus (H->A Score). Positiv = Worte vorhersagbarer als Taten |
| MV4.3 | Kategorien-Overlap | metrisch (0-1) | Ueberlappung der Kategorien-Verteilungen (synth. vs. echt) |
| MV4.4 | Sentiment-Differenz | metrisch | Sentiment synth. minus Sentiment echt |
| MV4.5 | Dimensions-Differenz | Vektor (12 Werte) | D01-D12 Differenz: Aussagen-Weltbild minus Handlungs-Weltbild |

### MV-Gruppe 5: Cluster & Netzwerk (Op5 / Technik T5)

Ergebnisse des Bottom-Up-Clusterings.

| MV-Code | Name | Typ | Beschreibung |
|---------|------|-----|-------------|
| MV5.1 | Cluster-Zugehoerigkeit | nominal | In welchem Cluster landet die Person/Aussage? |
| MV5.2 | Cluster-Profil | Vektor (k Anteile) | Anteil der Aussagen pro Cluster (z.B. 35% Typ A, 25% Typ B, ...) |
| MV5.3 | Netzwerk-Zentralitaet | metrisch | Degree/Betweenness/Closeness Centrality im Weltbild-Netzwerk |
| MV5.4 | Community-Zugehoerigkeit | nominal | Louvain-Community im Netzwerk |
| MV5.5 | Isolation-Score | metrisch | Mittlere Distanz zu allen anderen Personen |
| MV5.6 | Realwelt-Korrelation | metrisch | **Korrelation zwischen Weltbild-Naehe und Realwelt-Naehe** (gleiche Firma? gleicher Kreis? geographisch?) |

### MV-Gruppe 6: Vergleichs-Analysen (Op6 / Technik T2)

Nur anwendbar auf Topf-PAARE (Laender-Verhandlung).

| MV-Code | Name | Typ | Beschreibung |
|---------|------|-----|-------------|
| MV6.1 | Konsens-Zonen | Text (Liste) | Worueber einigen sich Land A und Land B sofort? |
| MV6.2 | Konflikt-Zonen | Text (Liste) | Worueber streiten sie? |
| MV6.3 | Unverstaendnis-Zonen | Text (Liste) | Was ist fuer Land A voellig unverstaendlich an Land B? |
| MV6.4 | Gemeinsame Erklaerung | Text (ja/nein + Inhalt) | Koennen sie sich einigen? Wortlaut? Oder Scheitern? |
| MV6.5 | Dimensions-Differenz | Vektor (12 Werte) | D01-D12: Land A minus Land B |

---

**GESAMT: 50+ Messvariablen** in 6 Gruppen (je 1 pro Operationalisierung), von qualitativ-narrativ bis metrisch-quantitativ.
Diese 50+ MVs operationalisieren die 3 AVs (Selbstbild, Weltbild, Menschenbild).

---

## 4. UNABHAENGIGE VARIABLEN (UVs) -- Was wir manipulieren

### UV1: ZEITRAUM

| Code | Stufe | Beschreibung |
|------|-------|-------------|
| Z_ej_2010 | Einzeljahr 2010 | |
| Z_ej_2011 | Einzeljahr 2011 | |
| Z_ej_2012 | Einzeljahr 2012 | ImageNet/AlexNet |
| Z_ej_2013 | Einzeljahr 2013 | |
| Z_ej_2014 | Einzeljahr 2014 | |
| Z_ej_2015 | Einzeljahr 2015 | OpenAI-Gruendung |
| Z_ej_2016 | Einzeljahr 2016 | AlphaGo |
| Z_ej_2017 | Einzeljahr 2017 | Transformer-Paper |
| Z_ej_2018 | Einzeljahr 2018 | BERT, GPT-1 |
| Z_ej_2019 | Einzeljahr 2019 | GPT-2 Zurueckhaltung |
| Z_ej_2020 | Einzeljahr 2020 | GPT-3 |
| Z_ej_2021 | Einzeljahr 2021 | DALL-E, Copilot |
| Z_ej_2022 | Einzeljahr 2022 | ChatGPT (Nov) |
| Z_ej_2023 | Einzeljahr 2023 | GPT-4, Safety-Krise |
| Z_ej_2024 | Einzeljahr 2024 | Regulierung, Nobel |
| Z_ej_2025 | Einzeljahr 2025 | AGI-Debatten |
| Z_ej_2026 | Einzeljahr 2026 | (Jan-Feb) |
| Z_zr_2000_2010 | Zeitraum 2000-2010 | Vor-Deep-Learning |
| Z_zr_2010_2016 | Zeitraum 2010-2016 | Fruehphase |
| Z_zr_2016_2026 | Zeitraum 2016-2026 | KI-Revolution |
| Z_zr_2010_2026 | Zeitraum 2010-2026 | Systematisch gesamt |
| Z_zr_2000_2026 | Zeitraum 2000-2026 | Maximalzeitraum |
| Z_zr_2023_2026 | Zeitraum 2023-2026 | Post-ChatGPT |
| Z_gesamt | Gesamt | Alle verfuegbaren Daten |

**Anzahl Stufen: 24** (17 Einzeljahre + 6 Zeitraeume + 1 Gesamt)

### UV2: MODALITAET (Art)

| Code | Stufe | Beschreibung |
|------|-------|-------------|
| M_A | Nur Aussagen | Nur aussage_text |
| M_H | Nur Handlungen | Nur handlungen |
| M_AH | Beides | Aussagen und Handlungen zusammen |

**Anzahl Stufen: 3**

### UV3: PERSON / GRUPPE

| Code | Stufe | n Personen | Beschreibung |
|------|-------|-----------|-------------|
| P_alle | Alle 100 | 100 | Gesamte Stichprobe |
| P_top10 | Top 10 | 10 | Rang 1-10 |
| P_top20 | Top 20 | 20 | Rang 1-20 |
| P_top50 | Top 50 | 50 | Rang 1-50 |
| P_P001...P_P100 | Einzelperson | 1 | Je 1 pro Person (100 Stufen) |
| P_ceo | CEOs | ~30 | Unternehmenslenker |
| P_akad | Akademiker | ~12 | Professoren, Forscher |
| P_inv | Investoren | ~10 | VCs, Angel Investors |
| P_gru | Gruender | ~25 | Startup-Gruender (ohne CEO) |
| P_pol | Politik | ~5 | Politische Akteure |
| P_anthropic | Anthropic | ~8 | Anthropic-Mitarbeiter |
| P_openai | OpenAI | ~7 | OpenAI-Mitarbeiter |
| P_google | Google/DeepMind | ~8 | Google/DeepMind |
| P_meta | Meta | ~5 | Meta/Facebook |
| P_xai | xAI | ~3 | Musks xAI |
| P_open | Open-Source-Befuerworter | ~15 | Haltung: Open |
| P_closed | Closed-Source-Befuerworter | ~15 | Haltung: Closed |
| P_risk | Risiko-Warner | ~20 | Haltung: Safety-First |
| P_speed | Beschleuniger | ~20 | Haltung: Speed-First |
| P_regpro | Regulierung pro | ~15 | Haltung: Reg. befuerwortet |
| P_regcon | Regulierung contra | ~15 | Haltung: Reg. abgelehnt |
| P_frauen | Frauen | ~8 | Geschlecht |
| P_maenner | Maenner | ~92 | Geschlecht |
| P_jung | Unter 35 | ~10 | Alter |
| P_alt | Ueber 60 | ~15 | Alter |
| P_immigrant | Nicht-US-geboren | ~30 | Herkunft |
| P_transformer | Transformer-Autoren | 8 | Die 8 Autoren des Transformer-Papers |
| P_cluster_k | Bottom-Up-Cluster k | variabel | Emergiert aus Clustering (T5) |

**Anzahl Stufen: 100 (Einzel) + 27 (Gruppen) + k (Cluster) = ~130+**

### UV4: INHALT / KATEGORIE

| Code | Stufe | Beschreibung |
|------|-------|-------------|
| K_alle | Alle Kategorien | Kein thematischer Filter |
| K_WV | Weltvision | Nur Aussagen der Kategorie WV |
| K_SB | Selbstbild | Nur SB |
| K_MB | Menschenbild | Nur MB |
| K_ET | Ethik | Nur ET |
| K_GE | Gesellschaft | Nur GE |
| K_RI | Risiko | Nur RI |
| K_FO | Fortschritt | Nur FO |
| K_MA | Macht | Nur MA |
| K_AR | Arbeit | Nur AR |
| K_TR | Transhumanismus | Nur TR |
| K_RE | Regulierung | Nur RE |
| K_SP | Spiritualitaet | Nur SP |
| K_OPT | Optimistisch (sekundaer) | Nur OPT |
| K_PES | Pessimistisch (sekundaer) | Nur PES |
| K_cluster_t | Themen-Cluster t | Emergiert aus Clustering |

**Anzahl Stufen: 1 + 12 + 2 + t = ~18+**

### UV5: KONGRUENZ (Sagen-Handeln-Beziehung)

| Code | Stufe | Beschreibung |
|------|-------|-------------|
| E_alle | Kein Filter | Alle Daten |
| E_kons | Konsistent | Nur Aussagen mit konsistenten Handlungen |
| E_wider | Widerspruch | Nur Aussagen mit widerspruch-Handlungen |
| E_ohne | Ohne Handlungsbezug | Aussagen ohne verknuepfte Handlung |

**Anzahl Stufen: 4**

### UV6: HOMOGENISIERUNG

| Code | Stufe | Beschreibung |
|------|-------|-------------|
| H_roh | Roh | Daten wie erhoben |
| H_cluster | Cluster-homogen | Nur Aussagen aus einem Bottom-Up-Cluster |
| H_dedup | Dedupliziert | Nur Unikate (Originalitaet = 1) |
| H_haeufig | Nur Wiederholte | Nur Aussagen mit Originalitaet > 1 (= Kernueberzeugungen) |

**Anzahl Stufen: 4**

---

## 3. VOLLSTAENDIGE KOMBINATIONSMATRIX

Jeder Topf = UV1 x UV2 x UV3 x UV4 x UV5 x UV6

### 3.1 BLOCK A: GLOBALE TOEPFE (UV3 = P_alle)

```
UV3 = P_alle (Alle 100 Personen)
UV4 = K_alle (Alle Kategorien)
UV5 = E_alle (Kein Kongruenzfilter)
UV6 = H_roh  (Keine Homogenisierung)
```

| Nr | Topf-ID | UV1 (Zeit) | UV2 (Art) | Fragestellung | Prio |
|----|---------|-----------|-----------|---------------|------|
| 1 | GA_ges_A | Gesamt | Aussagen | Kollektiv-Aussagenweltbild aller 100 | P1 |
| 2 | GA_ges_H | Gesamt | Handlungen | Kollektiv-Handlungsweltbild aller 100 | P1 |
| 3 | GA_ges_AH | Gesamt | Beides | **DAS Kollektiv-Weltbild der KI-Elite** | P1 |
| 4 | GA_2010_A | 2010 | Aussagen | Wie redet die KI-Elite 2010? | P1 |
| 5 | GA_2010_H | 2010 | Handlungen | Wie handelt die KI-Elite 2010? | P1 |
| 6 | GA_2010_AH | 2010 | Beides | Wie denkt die KI-Elite 2010? | P1 |
| 7 | GA_2011_A | 2011 | Aussagen | | P1 |
| 8 | GA_2011_H | 2011 | Handlungen | | P1 |
| 9 | GA_2011_AH | 2011 | Beides | | P1 |
| 10 | GA_2012_A | 2012 | Aussagen | ImageNet-Jahr | P1 |
| 11 | GA_2012_H | 2012 | Handlungen | | P1 |
| 12 | GA_2012_AH | 2012 | Beides | | P1 |
| 13-18 | GA_2013_A/H/AH ... GA_2014 | 2013-2014 | je 3 | | P1 |
| 19-21 | GA_2015_A/H/AH | 2015 | je 3 | OpenAI-Gruendung | P1 |
| 22-24 | GA_2016_A/H/AH | 2016 | je 3 | AlphaGo | P1 |
| 25-27 | GA_2017_A/H/AH | 2017 | je 3 | Transformer | P1 |
| 28-30 | GA_2018_A/H/AH | 2018 | je 3 | BERT/GPT-1 | P1 |
| 31-33 | GA_2019_A/H/AH | 2019 | je 3 | GPT-2 | P1 |
| 34-36 | GA_2020_A/H/AH | 2020 | je 3 | GPT-3 | P1 |
| 37-39 | GA_2021_A/H/AH | 2021 | je 3 | DALL-E | P1 |
| 40-42 | GA_2022_A/H/AH | 2022 | je 3 | ChatGPT | P1 |
| 43-45 | GA_2023_A/H/AH | 2023 | je 3 | GPT-4, Safety | P1 |
| 46-48 | GA_2024_A/H/AH | 2024 | je 3 | Regulierung, Nobel | P1 |
| 49-51 | GA_2025_A/H/AH | 2025 | je 3 | AGI-Debatten | P1 |
| 52-54 | GA_2026_A/H/AH | 2026 | je 3 | (Jan-Feb) | P2 |
| 55-57 | GA_00-10_A/H/AH | 2000-2010 | je 3 | Vor-Deep-Learning | P2 |
| 58-60 | GA_10-16_A/H/AH | 2010-2016 | je 3 | Fruehphase | P1 |
| 61-63 | GA_16-26_A/H/AH | 2016-2026 | je 3 | KI-Revolution | P1 |
| 64-66 | GA_10-26_A/H/AH | 2010-2026 | je 3 | Systematisch gesamt | P1 |
| 67-69 | GA_00-26_A/H/AH | 2000-2026 | je 3 | Maximalzeitraum | P2 |
| 70-72 | GA_23-26_A/H/AH | 2023-2026 | je 3 | Post-ChatGPT | P1 |

**Block A Gesamt: 72 Toepfe** (51 Einzeljahre x 3 + 6 Zeitraeume x 3 + 3 Gesamt)

---

### 3.2 BLOCK B: TOP-10-TOEPFE (UV3 = P_top10)

Selbe Struktur wie Block A, aber nur Top 10.

| Nr | Topf-ID-Muster | UV1 (Zeit) | UV2 (Art) | Prio |
|----|----------------|-----------|-----------|------|
| 73-75 | T10_ges_A/H/AH | Gesamt | je 3 | P1 |
| 76-126 | T10_YYYY_A/H/AH | 2010-2026 (17x) | je 3 | P1 |
| 127-144 | T10_zr_A/H/AH | 6 Zeitraeume | je 3 | P1 |

**Block B Gesamt: 72 Toepfe**

---

### 3.3 BLOCK C: EINZELPERSONEN-TOEPFE (UV3 = P_P001...P_P100)

| Nr | Topf-ID-Muster | UV1 (Zeit) | UV2 (Art) | Prio |
|----|----------------|-----------|-----------|------|
| 145-444 | EP_Pxxx_ges_AH | Gesamt | Beides | P1 (100x) |
| 445-544 | EP_Pxxx_ges_A | Gesamt | Aussagen | P1 Top20, P2 Rest |
| 545-644 | EP_Pxxx_ges_H | Gesamt | Handlungen | P1 Top20, P2 Rest |
| 645-764 | EP_Pxxx_zr_AH | 6 Zeitraeume | Beides | P1 Top20 (120x) |
| 765-884 | EP_Pxxx_zr_A | 6 Zeitraeume | Aussagen | P2 Top20 (120x) |
| 885-1004 | EP_Pxxx_zr_H | 6 Zeitraeume | Handlungen | P2 Top20 (120x) |
| 1005-1254 | EP_Pxxx_ej_AH | Einzeljahre (Top 5) | Beides | P2 (nur dichte ~50) |

**Block C Gesamt: ~660 Toepfe** (davon ~220 Prio 1, ~440 Prio 2)

---

### 3.4 BLOCK D: GRUPPEN-TOEPFE (UV3 = Rollen/Firmen/Haltungen/Demographie)

#### D1: Rollengruppen (5 Rollen)

| Nr | Topf-ID-Muster | UV3 | UV1 | UV2 | Prio |
|----|----------------|-----|-----|-----|------|
| - | GR_ceo_ges_A/H/AH | CEOs | Gesamt | je 3 | P1 |
| - | GR_akad_ges_A/H/AH | Akademiker | Gesamt | je 3 | P1 |
| - | GR_inv_ges_A/H/AH | Investoren | Gesamt | je 3 | P1 |
| - | GR_gru_ges_A/H/AH | Gruender | Gesamt | je 3 | P1 |
| - | GR_pol_ges_A/H/AH | Politik | Gesamt | je 3 | P2 |
| - | GR_xxx_zr_AH | Jede Rolle x 6 Zeitraeume | - | Beides | P2 |

**Rollen: 5 x 3 (Gesamt) + 5 x 6 (Zeitraeume) = 45 Toepfe**

#### D2: Firmengruppen (5 Firmen)

| Nr | Topf-ID-Muster | UV3 | UV1 | UV2 | Prio |
|----|----------------|-----|-----|-----|------|
| - | GF_anthropic_ges_A/H/AH | Anthropic | Gesamt | je 3 | P1 |
| - | GF_openai_ges_A/H/AH | OpenAI | Gesamt | je 3 | P1 |
| - | GF_google_ges_A/H/AH | Google/DM | Gesamt | je 3 | P1 |
| - | GF_meta_ges_A/H/AH | Meta | Gesamt | je 3 | P2 |
| - | GF_xai_ges_A/H/AH | xAI | Gesamt | je 3 | P2 |
| - | GF_xxx_zr_AH | Jede Firma x 3 Zeitraeume (Frueh/Spaet/Gesamt) | - | Beides | P2 |

**Firmen: 5 x 3 (Gesamt) + 5 x 3 (Zeitraeume) = 30 Toepfe**

#### D3: Haltungsgruppen (6 Haltungen)

| Nr | Topf-ID-Muster | UV3 | UV1 | UV2 | Prio |
|----|----------------|-----|-----|-----|------|
| - | GH_open_ges_AH | Open Source | Gesamt | Beides | P1 |
| - | GH_closed_ges_AH | Closed Source | Gesamt | Beides | P1 |
| - | GH_risk_ges_AH | Risiko-Warner | Gesamt | Beides | P1 |
| - | GH_speed_ges_AH | Beschleuniger | Gesamt | Beides | P1 |
| - | GH_regpro_ges_AH | Regulierung pro | Gesamt | Beides | P1 |
| - | GH_regcon_ges_AH | Regulierung contra | Gesamt | Beides | P1 |
| - | GH_xxx_ges_A | Jede Haltung nur Aussagen | Gesamt | Aussagen | P2 |
| - | GH_xxx_ges_H | Jede Haltung nur Handlungen | Gesamt | Handlungen | P2 |

**Haltungen: 6 x 1 (AH) + 6 x 2 (A/H) = 18 Toepfe**

#### D4: Demographische Gruppen (5 Gruppen)

| Nr | Topf-ID-Muster | UV3 | UV1 | UV2 | Prio |
|----|----------------|-----|-----|-----|------|
| - | GD_frauen_ges_AH | Frauen | Gesamt | Beides | P1 |
| - | GD_maenner_ges_AH | Maenner | Gesamt | Beides | P1 |
| - | GD_jung_ges_AH | Unter 35 | Gesamt | Beides | P2 |
| - | GD_alt_ges_AH | Ueber 60 | Gesamt | Beides | P2 |
| - | GD_immigrant_ges_AH | Nicht-US | Gesamt | Beides | P2 |

**Demographie: 5 Toepfe**

#### D5: Spezialgruppe

| Nr | Topf-ID | UV3 | Prio |
|----|---------|-----|------|
| - | GS_transformer_ges_AH | Transformer-Autoren | P1 |

**Block D Gesamt: 45 + 30 + 18 + 5 + 1 = 99 Toepfe**

---

### 3.5 BLOCK E: KONGRUENZ-TOEPFE (UV5 variiert)

UV5 = E_kons / E_wider / E_ohne auf ausgewaehlte Basis-Toepfe

| Nr | Topf-ID-Muster | Basis | UV5 | Fragestellung | Prio |
|----|----------------|-------|-----|---------------|------|
| - | KG_alle_kons_AH | Alle, Gesamt | Konsistent | Weltbild der Authentischen | P1 |
| - | KG_alle_wider_AH | Alle, Gesamt | Widerspruch | Weltbild der Inkongruenten | P1 |
| - | KG_alle_ohne_A | Alle, Gesamt | Ohne Bezug | Weltbild aus reinen Worten | P2 |
| - | KG_ej_YYYY_kons_AH | Alle, pro Jahr (17x) | Konsistent | Kongruenz pro Jahr | P1 |
| - | KG_ej_YYYY_wider_AH | Alle, pro Jahr (17x) | Widerspruch | Inkongruenz pro Jahr | P1 |
| - | KG_P_top20_kons_AH | Top 20 Einzel (20x) | Konsistent | Kongruenz pro Person | P2 |
| - | KG_P_top20_wider_AH | Top 20 Einzel (20x) | Widerspruch | Inkongruenz pro Person | P2 |

**Block E Gesamt: 2 + 1 + 34 + 40 = 77 Toepfe**

---

### 3.6 BLOCK F: KATEGORIE-TOEPFE (UV4 variiert)

UV4 = K_WV / K_ET / K_RI / ... auf ausgewaehlte Basis-Toepfe
Nur auf Aussagen-Toepfe (UV2 = M_A) anwendbar.

| Nr | Topf-ID-Muster | Basis | UV4 | Fragestellung | Prio |
|----|----------------|-------|-----|---------------|------|
| - | KAT_alle_ges_WV | Alle, A, Gesamt | Weltvision | Person NUR aus Zukunftsvisionen | P1 |
| - | KAT_alle_ges_ET | Alle, A, Gesamt | Ethik | Person NUR aus Ethik-Aussagen | P1 |
| - | KAT_alle_ges_RI | Alle, A, Gesamt | Risiko | Person NUR aus Risiko-Aussagen | P1 |
| - | KAT_alle_ges_TR | Alle, A, Gesamt | Transhumanismus | Person NUR aus Transhumanismus | P1 |
| - | KAT_alle_ges_GE | Alle, A, Gesamt | Gesellschaft | Person NUR aus Gesellschaft | P1 |
| - | KAT_alle_ges_MA | Alle, A, Gesamt | Macht | Person NUR aus Macht-Aussagen | P1 |
| - | KAT_alle_ges_SB | Alle, A, Gesamt | Selbstbild | Person NUR aus Selbstbild | P2 |
| - | KAT_alle_ges_MB | Alle, A, Gesamt | Menschenbild | Person NUR aus Menschenbild | P2 |
| - | KAT_alle_ges_FO | Alle, A, Gesamt | Fortschritt | Person NUR aus Fortschritt | P2 |
| - | KAT_alle_ges_AR | Alle, A, Gesamt | Arbeit | Person NUR aus Arbeit | P2 |
| - | KAT_alle_ges_RE | Alle, A, Gesamt | Regulierung | Person NUR aus Regulierung | P2 |
| - | KAT_alle_ges_SP | Alle, A, Gesamt | Spiritualitaet | Person NUR aus Spiritualitaet | P2 |
| - | KAT_alle_ej_WV...SP | Alle, A, Einzeljahre | je 12 | Kategorie x Jahr (selektiv) | P3 |

**Block F Gesamt: 12 (Gesamt) + ~60 (selektiv Jahre x Top-Kat.) = ~72 Toepfe**

---

### 3.7 BLOCK G: HOMOGENISIERTE TOEPFE (UV6 variiert)

| Nr | Topf-ID-Muster | Basis | UV6 | Fragestellung | Prio |
|----|----------------|-------|-----|---------------|------|
| - | HOM_dedup_ges_AH | Alle, AH, Gesamt | Dedupliziert | Weltbild ohne Wiederholungen | P2 |
| - | HOM_haeuf_ges_A | Alle, A, Gesamt | Nur Wiederholte | **Weltbild der Kernueberzeugungen** (was IMMER wieder gesagt wird) | P1 |
| - | HOM_cluster_Cx_AH | Cluster x, AH | Cluster-homogen | Weltbild pro Bottom-Up-Cluster | P1 |

**Block G Gesamt: 2 + ~8 (Cluster) = ~10 Toepfe**

---

### 3.8 BLOCK H: KREUZMODALE TOEPFE (Vorhersage-Paare)

Jedes Paar besteht aus einem Aussagen-Topf + einem Handlungs-Topf.
Beide Richtungen: A->synth.H und H->synth.A

| Nr | Paar-ID | Aussagen-Topf | Handlungs-Topf | Prio |
|----|---------|---------------|----------------|------|
| - | XM_alle_ges | GA_ges_A | GA_ges_H | P1 |
| - | XM_ej_YYYY (17x) | GA_YYYY_A | GA_YYYY_H | P1 |
| - | XM_top10_ges | T10_ges_A | T10_ges_H | P1 |
| - | XM_P_top20 (20x) | EP_Pxxx_ges_A | EP_Pxxx_ges_H | P1 |
| - | XM_zr_xx (6x) | GA_zr_A | GA_zr_H | P2 |

**Block H Gesamt: 1 + 17 + 1 + 20 + 6 = 45 Paare = 90 Prompt-Runs** (2 Richtungen)

---

### 3.9 BLOCK I: VERGLEICHS-PAARE (Laender-Verhandlung)

Jedes Paar besteht aus zwei Synthese-Texten die verglichen werden.

| Nr | Vergleich-ID | Land A | Land B | Kernfrage | Prio |
|----|-------------|--------|--------|-----------|------|
| - | VG_sagen_handeln | GA_ges_A Synthese | GA_ges_H Synthese | Sagen = Handeln? | P1 |
| - | VG_ceo_akad | GR_ceo Synthese | GR_akad Synthese | Entscheider vs. Forscher | P1 |
| - | VG_ceo_inv | GR_ceo Synthese | GR_inv Synthese | Fuehrung vs. Geld | P1 |
| - | VG_open_closed | GH_open Synthese | GH_closed Synthese | Open vs. Closed | P1 |
| - | VG_risk_speed | GH_risk Synthese | GH_speed Synthese | Mahner vs. Beschleuniger | P1 |
| - | VG_reg_pro_con | GH_regpro Synthese | GH_regcon Synthese | Regulierung: Wertkonflikt? | P1 |
| - | VG_frauen_maenner | GD_frauen Synthese | GD_maenner Synthese | Gender-Gap? | P1 |
| - | VG_jung_alt | GD_jung Synthese | GD_alt Synthese | Generationskonflikt? | P2 |
| - | VG_anthropic_openai | GF_anthropic Synthese | GF_openai Synthese | Safety vs. Capabilities | P1 |
| - | VG_google_openai | GF_google Synthese | GF_openai Synthese | BigTech vs. Startup | P2 |
| - | VG_frueh_spaet | GA_10-16 Synthese | GA_23-26 Synthese | Weltbild-Wandel | P1 |
| - | VG_kongruent_inkongruent | KG_kons Synthese | KG_wider Synthese | Authentische vs. Inkongruente | P1 |
| - | VG_preChatGPT_post | GA_2021_AH Synthese | GA_2023_AH Synthese | ChatGPT als Watershed | P1 |
| - | VG_top10_rest | T10_ges_AH Synthese | (Rang 11-100 Synthese) | Spitze vs. Rest | P1 |
| - | VG_transformer_rest | GS_transformer Synthese | (Rest Synthese) | Erfinder vs. Nutzer | P2 |
| - | VG_altman_hinton | EP_P002 Synthese | EP_P011 Synthese | CEO vs. Wissenschaftler | P2 |
| - | VG_musk_bengio | EP_P003 Synthese | EP_P013 Synthese | Disruptor vs. Ethiker | P2 |
| - | VG_thiel_li | EP_P015 Synthese | EP_P009 Synthese | Investor vs. Akademikerin | P2 |
| - | VG_andreessen_bengio | EP_P014 Synthese | EP_P013 Synthese | Techno-Optimist vs. Safety | P2 |
| - | VG_haeuf_roh | HOM_haeuf Synthese | GA_ges_A Synthese | Kernueberzeugungen vs. Alles | P2 |

**Block I Gesamt: ~20 Vergleichspaare**

---

### 3.10 BLOCK J: BOTTOM-UP-CLUSTER-TOEPFE (emergieren aus T5)

| Nr | Topf-ID-Muster | Beschreibung | Prio |
|----|----------------|-------------|------|
| - | BU_aussage_C1...Ck | Aussagen-Cluster 1 bis k | P1 |
| - | BU_handlung_C1...Cj | Handlungs-Cluster 1 bis j | P1 |
| - | BU_aussage_Cx_zr_yy | Cluster x pro Zeitraum | P2 |
| - | BU_netzwerk | 100x100 Distanzmatrix | P1 |

**Block J Gesamt: ~8-13 (Cluster) + ~40 (Cluster x Zeit) + 1 = ~50-55**

---

## 4. GESAMTZAEHLUNG

| Block | Beschreibung | Toepfe | davon P1 | davon P2/P3 |
|-------|-------------|--------|----------|-------------|
| A | Globale Toepfe (Alle 100) | 72 | 63 | 9 |
| B | Top-10-Toepfe | 72 | 63 | 9 |
| C | Einzelpersonen | ~660 | ~220 | ~440 |
| D | Gruppen (Rolle/Firma/Haltung/Demo) | 99 | ~50 | ~49 |
| E | Kongruenz-Filter | 77 | ~37 | ~40 |
| F | Kategorie-Filter | ~72 | 6 | ~66 |
| G | Homogenisierte Toepfe | ~10 | ~9 | ~1 |
| H | Kreuzmodale Paare (Runs) | 90 | ~78 | ~12 |
| I | Vergleichs-Paare | ~20 | ~13 | ~7 |
| J | Bottom-Up-Cluster | ~55 | ~14 | ~41 |
| **GESAMT** | | **~1.227** | **~553** | **~674** |

### Realistischer Scope nach Mindestgroesse-Filter (>= 15 Datenpunkte):

- Block C stark reduziert (viele Einzel x Zeitraum zu duenn)
- Block F stark reduziert (Kategorie x Jahr zu duenn)
- **Geschaetzt realisierbar: ~500-600 Toepfe**
- **Davon Prio 1: ~300-350**
- **Prompt-Runs (geschaetzt): ~800-1.000** (Synthese + Destillat + Rating + Kreuzmodal + Vergleich)

---

## 5. ZUORDNUNG: FORSCHUNGSFRAGEN -> TOEPFE -> AVs

### F1: WELTBILD -- Was denkt die KI-Elite?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| GA_ges_AH (Nr. 3) | MV1.1-1.7, MV2.01-2.12, MV3.1-3.9 | DAS Kollektiv-Weltbild |
| T10_ges_AH | MV1.1-1.7, MV2.01-2.12 | Weltbild der Maechtigen |
| EP_Pxxx_ges_AH (100x) | MV1.1-1.7, MV2.01-2.12 | 100 individuelle Weltbilder |
| GR_xxx_ges_AH (5x) | MV1.1-1.7, MV2.01-2.12 | Weltbilder nach Rolle |
| GH_xxx_ges_AH (6x) | MV1.1-1.7, MV2.01-2.12 | Weltbilder nach Haltung |

### F2: WANDEL -- Wie hat sich das Weltbild veraendert?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| GA_YYYY_AH (17x) | MV2.01-2.12 | **Zeitreihe der 12 Dimensionen** |
| GA_YYYY_AH (17x) | MV3.2 | Sentiment-Zeitreihe |
| GA_YYYY_AH (17x) | MV3.3 | Semantische Aehnlichkeit Jahr-zu-Jahr |
| GA_YYYY_AH (17x) | MV3.4 | Themen-Drift pro Jahr |
| GA_YYYY_AH (17x) | MV3.5, MV3.6 | **Metaphern-Wandel**: Aendern sich die Metaphern? |
| GA_YYYY_AH (17x) | MV3.8 | Emotionsprofil-Wandel pro Jahr |
| GA_zr_AH (6x) | MV2.01-2.12 | Epochen-Vergleich |
| VG_frueh_spaet | MV6.1-6.5 | Laender-Verhandlung: Frueh vs. Spaet |
| VG_preChatGPT_post | MV6.1-6.5 | ChatGPT als Wendepunkt? |

### F3: KONGRUENZ -- Stimmen Sagen und Handeln ueberein?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| GA_ges_A + GA_ges_H | MV2.01-2.12, MV4.5 | Globaler Dimensions-Vergleich |
| XM_alle_ges (2 Richtungen) | MV4.1-4.5 | Kreuzmodale Vorhersage |
| XM_ej_YYYY (17x2) | MV4.1 | **Kongruenz-Zeitreihe**: Wird Kluft groesser? |
| XM_P_top20 (20x2) | MV4.1 | Kongruenz pro Person: Wer ist authentisch? |
| VG_sagen_handeln | MV6.1-6.5 | Sagen-Land vs. Handeln-Land |
| KG_alle_kons + KG_alle_wider | MV2.01-2.12 | Dimensionsprofil: kongruent vs. inkongruent |
| VG_kongruent_inkongruent | MV6.1-6.5 | Wie unterscheiden sich die Weltbilder? |
| GA_ges_A + GA_ges_H | MV3.5, MV3.6 | **Metaphern-Vergleich**: Andere Metaphern in Worten vs. Taten? |

### F4: CLUSTER -- Welche Weltbild-Typen gibt es?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| BU_aussage_C1...Ck | MV5.1-5.2 | Emergente Aussagen-Cluster |
| BU_handlung_C1...Cj | MV5.1-5.2 | Emergente Handlungs-Cluster |
| BU_aussage_Cx (pro Cluster) | MV1.1-1.7, MV2.01-2.12 | Weltbild-Synthese pro Cluster |
| 100x100 Distanzmatrix | MV5.3-5.5 | Netzwerk-Analyse |
| alle Cluster | MV5.6 | **Realwelt-Korrelation**: Gleiche Firma = gleiches Cluster? |
| BU_x_zr (Cluster x Zeit) | MV5.1 | Cluster-Drift: Wandern Personen zwischen Clustern? |

### F5: DIFFERENZ -- Welche Subgruppen denken anders?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| VG_ceo_akad, VG_ceo_inv | MV6.1-6.5 | Rollen-Vergleich |
| VG_open_closed | MV6.1-6.5 | Haltungs-Vergleich |
| VG_risk_speed | MV6.1-6.5 | Safety vs. Speed |
| VG_frauen_maenner | MV6.1-6.5 | Gender-Gap |
| VG_anthropic_openai | MV6.1-6.5 | Firmen-Vergleich |
| Alle Gruppen-Toepfe | MV2.01-2.12 | **Dimensions-Vergleich**: Welche D01-D12 differenzieren die Gruppen? |
| Alle Gruppen-Toepfe | MV3.5, MV3.6 | **Metaphern-Vergleich**: Sprechen CEOs in anderen Metaphern als Akademiker? |
| Alle Gruppen-Toepfe | MV3.8 | **Emotionsprofil-Vergleich**: Verschiedene Emotionen pro Gruppe? |

### F6: MACHT -- Welches Weltbild hat die meiste Macht?

| Toepfe | AVs | Analyse |
|--------|-----|---------|
| BU Cluster + Rang-Score | MV5.1 + Gewichtung | Gesamtscore pro Cluster aufsummieren |
| T10 vs. Rest | MV2.01-2.12 | Dimensions-Profil: Stimmt Top-10-Weltbild mit Mehrheits-Weltbild ueberein? |
| GR_ceo_ges vs. alle | MV2.01-2.12 | CEO-Weltbild vs. Kollektiv: Wer bestimmt die Richtung? |

---

## 6. AV-ANWENDUNGSMATRIX: Welche AVs auf welche Topf-Typen

| AV-Gruppe | Block A (Global) | Block B (Top10) | Block C (Einzel) | Block D (Gruppen) | Block E (Kongr.) | Block F (Kat.) | Block H (Kreuzm.) | Block I (Vergl.) | Block J (Cluster) |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Op1 (Synthese) | X | X | X | X | X | X | - | - | X |
| Op2 (Dimensionen) | X | X | X | X | X | X | - | - | X |
| Op3 (Deskriptiv) | X | X | selektiv | X | X | X | - | - | X |
| Op4 (Kreuzmodal) | - | - | - | - | - | - | X | - | - |
| Op5 (Cluster) | - | - | X | - | - | - | - | - | X |
| Op6 (Vergleich) | - | - | - | - | - | - | - | X | - |

Legende: X = immer anwenden, selektiv = nur Top 20, - = nicht anwendbar

---

## 7. REALWELT-KORRELATION (Forschungsfrage F4 Vertiefung)

**Kernfrage: Sind Personen mit aehnlichen Weltbildern auch in der echten Welt naeher?**

Operationalisierung von "Realwelt-Naehe":

| Realwelt-Dimension | Operationalisierung | Datenquelle |
|--------------------|---------------------|-------------|
| Firma | Gleiche Firma = 1, verschiedene = 0 | Top-100-Liste |
| Co-Investition | Haben in gleiche Startups investiert | Crunchbase |
| Netzwerk | Sitzen in gleichen Boards/Beiräten | LinkedIn, SEC |
| Geographie | Gleiche Stadt/Region | oeffentlich |
| Konferenz | Treten auf gleichen Konferenzen auf | Programme |
| Co-Autorenschaft | Haben zusammen publiziert | Google Scholar |
| Arbeitgeber-Historie | Haben fuer gleiche Firmen gearbeitet | LinkedIn |

**Analyse:**
1. Weltbild-Distanzmatrix (aus Cluster-Profilen, MV5.2) = 100x100
2. Realwelt-Distanzmatrix (aus obigen Dimensionen) = 100x100
3. **Mantel-Test**: Korrelation zwischen den beiden Matrizen
   -> Signifikant positiv = Weltbild-Naehe = Realwelt-Naehe
   -> Nicht signifikant = Weltbilder unabhaengig von Realwelt-Naehe

**Spannende Sub-Analysen:**
- Welche Realwelt-Dimension korreliert am staerksten?
  (Firma > Geographie? Oder Co-Investition > Firma?)
- Gibt es Personen die im Weltbild nah aber real fern sind?
  (= ueberraschende Geistesverwandte)
- Gibt es Personen die real nah aber im Weltbild fern sind?
  (= Kollegen die fundamental anders denken)

---

*Forschungsdesign erstellt am 2026-02-11*
*Forschungsprojekt: Transhumanismus / Silicon Valley Worldviews*
