# Topf-Dimensionsanalyse: Systematische Bestimmung aller moeglichen Toepfe

**Forschungsprojekt:** Transhumanismus / Silicon Valley Worldviews
**Datum:** 2026-02-11
**Methode:** Kombinatorische Aufzaehlung aller Topf-Dimensionen

---

## 1. Verfuegbare Variablen (Dimensionen)

Jeder Topf ist ein FILTER auf den Gesamtdatensatz. Die Filter-Dimensionen sind:

### Dimension A: PERSON (Wessen Daten?)

| Stufe | Code | Beschreibung | Anzahl Optionen |
|-------|------|-------------|-----------------|
| A1 | Einzelperson | Genau 1 Person | 100 |
| A2 | Top-N | Die N hoechstbewerteten | Top 5, 10, 20, 50 = 4 |
| A3 | Alle | Alle 100 | 1 |
| A4 | Rolle | Vordefinierte Rollengruppe | CEOs, Akademiker, Investoren, Gruender, Politik = ~5 |
| A5 | Firma | Firmenzugehoerigkeit | Anthropic, OpenAI, Google, Meta, xAI, ... = ~10 |
| A6 | Haltung | Inhaltliche Gruppierung (nach Kodierung) | Open/Closed, Risiko/Speed, Reg-pro/contra = ~6 |
| A7 | Demographie | Geschlecht, Alter, Herkunft | m/w, jung/alt, US/nicht-US = ~6 |
| A8 | Cluster | Emergentes Bottom-Up-Cluster | k (unbekannt, ~3-8) |

### Dimension B: MODALITAET (Welche Datenart?)

| Stufe | Code | Beschreibung |
|-------|------|-------------|
| B1 | Nur Aussagen (A) | Nur aussage_text |
| B2 | Nur Handlungen (H) | Nur handlungen |
| B3 | Beides (A+H) | Aussagen und Handlungen zusammen |

### Dimension C: ZEIT (Welcher Zeitraum?)

| Stufe | Code | Beschreibung | Anzahl Optionen |
|-------|------|-------------|-----------------|
| C1 | Einzeljahr | Genau 1 Jahr | 2010-2026 = 17 |
| C2 | Zeitreihe | Zusammenhaengender Zeitraum | siehe Liste unten |
| C3 | Gesamt | Gesamter Zeitraum | 1 |

**Definierte Zeitreihen (C2):**

| Code | Zeitraum | Begruendung |
|------|----------|-------------|
| C2a | 2000-2009 | Vor-Deep-Learning-Aera (nur opportunistisch) |
| C2b | 2010-2015 | Aufbauphase (ImageNet bis vor AlphaGo) |
| C2c | 2016-2019 | Beschleunigungsphase (AlphaGo bis GPT-2) |
| C2d | 2020-2022 | Explosionsphase (GPT-3 bis ChatGPT) |
| C2e | 2023-2026 | Post-ChatGPT (Regulierung, AGI-Debatte) |
| C2f | 2010-2016 | Fruehphase komplett |
| C2g | 2016-2026 | Seit KI-Revolution |
| C2h | 2010-2026 | Gesamter systematischer Erhebungszeitraum |
| C2i | 2000-2026 | Maximalzeitraum inkl. opportunistisch |

### Dimension D: INHALT/KATEGORIE (Welche Themen?)

| Stufe | Code | Beschreibung | Anzahl Optionen |
|-------|------|-------------|-----------------|
| D1 | Alle Kategorien | Kein thematischer Filter | 1 |
| D2 | Primaere Kategorie | Nur 1 primaere Kategorie | WV,SB,MB,ET,GE,RI,FO,MA,AR,TR,RE,SP = 12 |
| D3 | Sekundaerer Code | Nur 1 sekundaerer Code | OPT,PES,AMB,POL,PHI,EMP,ANE,PRO = 8 |
| D4 | Themen-Cluster | Emergentes Themen-Cluster (nach Kodierung) | unbekannt, ~5-10 |

### Dimension E: KONGRUENZ (Welche Sagen-Handeln-Beziehung?)

| Stufe | Code | Beschreibung |
|-------|------|-------------|
| E1 | Alle | Kein Kongruenz-Filter |
| E2 | Konsistent | Nur Aussagen mit konsistenten Handlungen |
| E3 | Widerspruch | Nur Aussagen mit widerspruch-Handlungen |
| E4 | Ohne Handlungsbezug | Aussagen ohne verknuepfte Handlung |

### Dimension F: HOMOGENISIERUNG (Vorverarbeitung)

| Stufe | Code | Beschreibung |
|-------|------|-------------|
| F1 | Roh | Daten wie erhoben, keine Vorverarbeitung |
| F2 | Cluster-homogenisiert | Nur Aussagen/Handlungen aus einem Bottom-Up-Cluster |
| F3 | Dedupliziert | Originalitaets-Zaehler > 1 entfernt (nur Unikate) |

---

## 2. Kombinatorischer Raum

### 2.1 Formel

```
Topf = A x B x C x D x E x F
```

### 2.2 Maximale Kombinationen (theoretisch)

| Dimension | Stufen |
|-----------|--------|
| A (Person) | 100 + 4 + 1 + 5 + 10 + 6 + 6 + ~5 = ~137 |
| B (Modalitaet) | 3 |
| C (Zeit) | 17 + 9 + 1 = 27 |
| D (Inhalt) | 1 + 12 + 8 + ~7 = ~28 |
| E (Kongruenz) | 4 |
| F (Homogenisierung) | 3 |

**Theoretisches Maximum: 137 x 3 x 27 x 28 x 4 x 3 = ~3.7 Millionen**

Das ist absurd viel. Die meisten Kombinationen sind sinnlos oder leer.

### 2.3 Sinnvolle Reduktionsregeln

| Regel | Begruendung |
|-------|-------------|
| R1: F=F1 als Default | Homogenisierung nur fuer Bottom-Up-Analyse |
| R2: D=D1 als Default | Kategorie-Filter erst nach Kodierung sinnvoll |
| R3: E nur mit B=B3 oder B=B1 | Kongruenz braucht Handlungsbezug |
| R4: A8 (Cluster) erst nach Clustering | Nicht vorab planbar |
| R5: C2a nur mit A2(Top20) | Vor 2010 zu wenig Daten fuer alle |
| R6: Mindest-Topfgroesse >= 15 | Zu kleine Toepfe erzeugen fragile Synthesen |
| R7: A1 x C1 nur fuer Top 20 | Einzelperson x Einzeljahr meist zu duenn |

---

## 3. Systematische Aufzaehlung: ALLE sinnvollen Topf-Typen

### EBENE 1: Basis-Toepfe (A x B x C, mit D=D1, E=E1, F=F1)

Die Grundstruktur: Wer x Was x Wann

```
                        B1 (Aussagen)    B2 (Handlungen)    B3 (Beides)
                        =============    ================    ===========

A3 (Alle 100):
  C3 (gesamt)               [1]               [2]               [3]
  C1 (pro Jahr, 17x)        [4a-q]            [5a-q]            [6a-q]
  C2 (Zeitreihen, 9x)       [7a-i]            [8a-i]            [9a-i]

A2 (Top N):
  C3 (gesamt)               [10a-d]           [11a-d]           [12a-d]
  C1 (pro Jahr)             [13]              [14]              [15]
  C2 (Zeitreihen)           [16]              [17]              [18]

A1 (Einzelperson):
  C3 (gesamt)               [19: 100x]        [20: 100x]        [21: 100x]
  C2 (Zeitreihen)           [22: 20x9]        [23: 20x9]        [24: 20x9]
  C1 (pro Jahr)             (nur Top 5, nur dichte Jahre)        [25: ~50]

A4-A7 (Gruppen):
  C3 (gesamt)               [26: ~27x]        [27: ~27x]        [28: ~27x]
  C2 (Zeitreihen)           [29: selektiv]    [30: selektiv]    [31: selektiv]
```

### ZAEHLUNG EBENE 1:

| Block | Toepfe | Beschreibung |
|-------|--------|-------------|
| [1]-[3] | 3 | Alle 100, gesamt, nach Modalitaet |
| [4]-[6] | 51 | Alle 100, pro Jahr (17), nach Modalitaet (3) |
| [7]-[9] | 27 | Alle 100, pro Zeitreihe (9), nach Modalitaet (3) |
| [10]-[12] | 12 | Top N (4 Stufen), gesamt, nach Modalitaet (3) |
| [13]-[18] | ~30 | Top N, nach Zeit (selektiv), nach Modalitaet |
| [19]-[21] | 300 | Einzelperson (100), gesamt, nach Modalitaet (3) |
| [22]-[24] | ~540 | Einzelperson (Top 20), Zeitreihen (9), Modalitaet (3) |
| [25] | ~50 | Einzelperson x Einzeljahr (nur dichte Kombinationen) |
| [26]-[31] | ~100 | Gruppen (~27), gesamt + selektiv, Modalitaet |
| **Summe Ebene 1** | **~1.113** | |

### EBENE 2: Kongruenz-Filter (E2, E3, E4 auf Ebene-1-Toepfe)

Nur auf ausgewaehlte Ebene-1-Toepfe anwendbar:

| Basis-Topf | x E2 (konsistent) | x E3 (widerspruch) | Fragestellung |
|------------|-------------------|---------------------|---------------|
| [1] (Alle, A, gesamt) | [1-E2] | [1-E3] | Aussagenweltbild bei konsistenten vs. inkonsistenten |
| [3] (Alle, A+H, gesamt) | [3-E2] | [3-E3] | Gesamtweltbild der Authentischen vs. Inkongruenten |
| [21] (Einzel, A+H, gesamt) | [21-E2: 20x] | [21-E3: 20x] | Pro Person: kongruentes vs. inkongruentes Selbst |
| [6a-q] (Alle, A+H, Jahr) | [6-E2: 17x] | [6-E3: 17x] | Pro Jahr: kongruent vs. inkongruent |

**Zusaetzliche Toepfe durch Kongruenz: ~100**

### EBENE 3: Kategorie-Filter (D2 auf ausgewaehlte Ebene-1-Toepfe)

Nur nach Kodierung (Phase 4) moeglich. Nur auf Aussagen-Toepfe (B1):

| Basis-Topf | x 12 Kategorien | Fragestellung |
|------------|----------------|---------------|
| [1] (Alle, A, gesamt) | [1-WV], [1-SB], ..., [1-SP] = 12 | Weltbild NUR aus Zukunftsvisionen / NUR aus Ethik / etc. |
| [4a-q] (Alle, A, Jahr) | 17 x 12 = 204 | Wie veraendert sich z.B. Risiko-Diskurs pro Jahr? |
| [19] (Einzel, A, gesamt) | 20 x 12 = 240 (Top 20) | Wieviel % von Altmans Aussagen sind "Risiko"? |

**Zusaetzliche Toepfe durch Kategorien: ~460 (viele zu klein -> Mindestgroesse-Filter)**

### EBENE 4: Bottom-Up-Cluster (A8, F2)

Ergibt sich aus Clustering. Geschaetzt:

| Block | Toepfe | Beschreibung |
|-------|--------|-------------|
| Aussagen-Cluster | ~5-8 | Homogene Aussagen-Buendel |
| Handlungs-Cluster | ~3-5 | Homogene Handlungs-Buendel |
| Cluster x Zeit | ~30-50 | Cluster pro Zeitreihe (um Drift zu messen) |
| **Summe Ebene 4** | **~40-65** | |

---

## 4. Gesamter Topf-Raum

| Ebene | Toepfe (geschaetzt) | Beschreibung |
|-------|---------------------|-------------|
| Ebene 1 (Basis) | ~1.113 | Person x Modalitaet x Zeit |
| Ebene 2 (Kongruenz) | ~100 | + Kongruenz-Filter |
| Ebene 3 (Kategorie) | ~460 | + Kategorie-Filter |
| Ebene 4 (Cluster) | ~65 | + Bottom-Up-Cluster |
| **THEORETISCH MOEGLICH** | **~1.738** | |

Davon nach Mindestgroesse-Filter (>= 15 Datenpunkte) wahrscheinlich realisierbar: **~500-700**

---

## 5. Einschluss-/Ausschluss-Entscheidung nach Fragestellung

### 5.1 Die uebergeordneten Forschungsfragen

| Nr. | Frage | Kuerzel |
|-----|-------|---------|
| F1 | Was denkt die KI-Elite ueber sich, die Welt und die Menschheit? | WELTBILD |
| F2 | Wie hat sich dieses Weltbild von 2010 bis 2026 veraendert? | WANDEL |
| F3 | Stimmen Aussagen und Handlungen ueberein? | KONGRUENZ |
| F4 | Welche Weltbild-Typen gibt es, und wer gehoert wohin? | CLUSTER |
| F5 | Welche Subgruppen denken anders als andere? | DIFFERENZ |
| F6 | Welches Weltbild hat die meiste Macht/Ressourcen? | MACHT |

### 5.2 Zuordnung: Fragestellung -> Notwendige Toepfe

**F1 (WELTBILD) -- Was denkt die KI-Elite?**

| Topf | Prio | Begruendung |
|------|------|-------------|
| Alle, A+H, gesamt [3] | P1 | DAS Kollektiv-Weltbild |
| Alle, nur A, gesamt [1] | P1 | Weltbild nur nach Worten |
| Alle, nur H, gesamt [2] | P1 | Weltbild nur nach Taten |
| Top 10, A+H, gesamt [12a] | P1 | Weltbild der Maechtigen |
| Einzelperson x 20, A+H, gesamt [21: 20x] | P1 | 20 individuelle Weltbilder |
| Einzelperson x 80, A+H, gesamt [21: 80x] | P2 | Restliche 80 Personen |
| **Toepfe fuer F1: ~103** | | |

**F2 (WANDEL) -- Wie hat sich das Weltbild veraendert?**

| Topf | Prio | Begruendung |
|------|------|-------------|
| Alle, A+H, pro Jahr [6a-q: 17x] | P1 | **Jahres-Zeitreihe (Kern!)** |
| Alle, nur A, pro Jahr [4a-q: 17x] | P1 | Aussagen-Zeitreihe |
| Alle, nur H, pro Jahr [5a-q: 17x] | P2 | Handlungs-Zeitreihe |
| Alle, A+H, Zeitreihen [9a-i: 9x] | P1 | Epochen-Vergleich |
| Top 10, A+H, Zeitreihe frueh vs. spaet [selektiv] | P1 | Wandel der Top 10 |
| Einzelperson x 10, A+H, Zeitreihe frueh vs. spaet | P2 | Individueller Wandel |
| **Toepfe fuer F2: ~80** | | |

**F3 (KONGRUENZ) -- Stimmen Sagen und Handeln ueberein?**

| Topf | Prio | Begruendung |
|------|------|-------------|
| Alle, nur A, gesamt [1] + Alle, nur H, gesamt [2] | P1 | Globaler Sagen-vs-Handeln-Vergleich |
| Alle, nur A, pro Jahr + Alle, nur H, pro Jahr | P1 | Kongruenz-Zeitreihe (17 Paare) |
| Alle, A+H, gesamt, konsistent [3-E2] | P1 | Welt der Kongruenten |
| Alle, A+H, gesamt, widerspruch [3-E3] | P1 | Welt der Inkongruenten |
| Top 20, nur A + nur H, gesamt (20 Paare) | P1 | Pro-Person-Kongruenz |
| Kreuzmodal: A->synth.H, H->synth.A | P1 | Vorhersage-Experiment |
| **Toepfe fuer F3: ~80** | | |

**F4 (CLUSTER) -- Welche Weltbild-Typen gibt es?**

| Topf | Prio | Begruendung |
|------|------|-------------|
| Bottom-Up Aussagen-Cluster (~5-8) | P1 | Emergente Aussagen-Typen |
| Bottom-Up Handlungs-Cluster (~3-5) | P1 | Emergente Handlungs-Typen |
| Cluster x Zeitreihe (~30-50) | P2 | Cluster-Drift ueber die Zeit |
| **Toepfe fuer F4: ~40-65** | | |

**F5 (DIFFERENZ) -- Welche Subgruppen denken anders?**

| Topf | Prio | Begruendung |
|------|------|-------------|
| CEOs, A+H, gesamt | P1 | |
| Akademiker, A+H, gesamt | P1 | |
| Investoren, A+H, gesamt | P1 | |
| Gruender, A+H, gesamt | P1 | |
| Anthropic vs. OpenAI vs. Google | P1 | Firmen-Vergleich |
| Open-Source vs. Closed-Source | P1 | Haltungs-Vergleich |
| Risiko-Warner vs. Beschleuniger | P1 | |
| Frauen vs. Maenner | P2 | |
| Jung vs. Alt | P2 | |
| Transformer-Autoren vs. Rest | P2 | |
| **Toepfe fuer F5: ~30** | | |

**F6 (MACHT) -- Welches Weltbild hat die meiste Macht?**

Braucht keine eigenen Toepfe -- nutzt Ergebnisse von F4 (Cluster) und
gewichtet mit Score/Rang aus der Top-100-Liste.

### 5.3 Zusammenfassung: Eingeschlossene Toepfe

| Forschungsfrage | Prio-1-Toepfe | Prio-2-Toepfe | Gesamt |
|-----------------|---------------|---------------|--------|
| F1 WELTBILD | ~23 | ~80 | ~103 |
| F2 WANDEL | ~55 | ~25 | ~80 |
| F3 KONGRUENZ | ~60 | ~20 | ~80 |
| F4 CLUSTER | ~13 | ~50 | ~65 |
| F5 DIFFERENZ | ~20 | ~10 | ~30 |
| F6 MACHT | 0 (nutzt F4) | 0 | 0 |
| **GESAMT (mit Overlap)** | **~120** | **~130** | **~250** |

Nach Deduplizierung (viele Toepfe dienen mehreren Fragen):
**Geschaetzt ~200 einzigartige Toepfe, davon ~120 Prio 1.**

---

## 6. Was fehlt noch? Checkliste

| Dimension | Abgedeckt? | Anmerkung |
|-----------|-----------|-----------|
| Person (Einzel) | Ja | 100 Toepfe |
| Person (Top N) | Ja | 4 Stufen |
| Person (Alle) | Ja | |
| Person (Rolle) | Ja | CEO, Akad., Invest., Gruender, Politik |
| Person (Firma) | Ja | Anthropic, OpenAI, Google, ... |
| Person (Haltung) | Ja | Open/Closed, Risk/Speed, Reg+/- |
| Person (Demographie) | Ja | m/w, jung/alt, US/nicht-US |
| Person (Cluster) | Ja | Bottom-Up |
| Modalitaet (A) | Ja | |
| Modalitaet (H) | Ja | |
| Modalitaet (A+H) | Ja | |
| Zeit (Einzeljahr) | Ja | 17 Jahre |
| Zeit (Zeitreihe) | Ja | 9 definierte Reihen |
| Zeit (Gesamt) | Ja | |
| Inhalt (Kategorie) | Ja | 12 primaere, 8 sekundaere |
| Inhalt (Cluster) | Ja | Bottom-Up |
| Kongruenz | Ja | konsistent/widerspruch/ohne |
| Homogenisierung | Ja | roh/cluster/dedupliziert |

### Moegliche Ergaenzungen:

| Dimension | Beschreibung | Einschluss? |
|-----------|-------------|-------------|
| Plattform | Nur YouTube / Nur Twitter / Nur Podcasts | P3 -- Interessant aber sekundaer. Plattform-Bias-Analyse. |
| Sprache | Nur englisch / Nur nicht-englisch | P3 -- Zu wenig nicht-englische Daten erwartet. |
| Modus | Nur muendlich / Nur schriftlich | P2 -- Reden Leute anders als sie schreiben? Spannend! |
| Originalitaet | Nur Aussagen mit Originalitaet > 3 (oft wiederholt) | P2 -- Kernueberzeugungen = das, was jemand immer wieder sagt. |
| Grenzfall | Nur Grenzfaelle | P3 -- Methodisch interessant aber Nische. |

---

## 7. Finale Topf-Architektur (Empfehlung)

```
SCHICHT 1: BASIS-TOEPFE (Prio 1, immer erzeugen)
================================================================

  Globale Toepfe (3):
    [G-A]     Alle 100, nur Aussagen, gesamt
    [G-H]     Alle 100, nur Handlungen, gesamt
    [G-AH]    Alle 100, Aussagen+Handlungen, gesamt

  Jahrestoepfe (51):
    [J-YYYY-A]    Alle 100, nur Aussagen, pro Jahr (17x)
    [J-YYYY-H]    Alle 100, nur Handlungen, pro Jahr (17x)
    [J-YYYY-AH]   Alle 100, A+H, pro Jahr (17x)

  Epochentoepfe (15):
    [E-xx-A]   Alle 100, nur Aussagen, 5 Hauptepochen
    [E-xx-H]   Alle 100, nur Handlungen, 5 Hauptepochen
    [E-xx-AH]  Alle 100, A+H, 5 Hauptepochen

  Einzelpersonen (100):
    [P-xxx-AH]  Je 1 pro Person, A+H, gesamt

  Kongruenz (4):
    [K-A]      Alle, nur Aussagen mit Handlungs-Konsistenz
    [K-H]      Alle, nur Handlungen mit Aussagen-Konsistenz
    [K-W-A]    Alle, nur Aussagen mit Handlungs-Widerspruch
    [K-W-H]    Alle, nur Handlungen mit Aussagen-Widerspruch

  Summe Schicht 1: ~173

SCHICHT 2: GRUPPEN-TOEPFE (Prio 1, fuer Vergleichsanalysen)
================================================================

  Rollengruppen (5 x 3 Modalitaeten = 15):
    [R-ceo-A/H/AH]  [R-akad-A/H/AH]  [R-inv-A/H/AH]
    [R-gru-A/H/AH]  [R-pol-A/H/AH]

  Haltungsgruppen (6 x 1 = 6, nur A+H):
    [H-open-AH]  [H-closed-AH]
    [H-risk-AH]  [H-speed-AH]
    [H-regpro-AH]  [H-regcon-AH]

  Firmengruppen (selektiv, 5 x 1 = 5):
    [F-anthropic-AH]  [F-openai-AH]  [F-google-AH]
    [F-meta-AH]  [F-xai-AH]

  Summe Schicht 2: ~26

SCHICHT 3: BOTTOM-UP-CLUSTER (Prio 1, Anzahl emergiert)
================================================================

  Aussagen-Cluster (~5-8 Toepfe)
  Handlungs-Cluster (~3-5 Toepfe)

  Summe Schicht 3: ~8-13

SCHICHT 4: VERTIEFUNG (Prio 2, selektiv nach Bedarf)
================================================================

  Einzelperson x Epochen (Top 20 x 5 Epochen = 100, nur A+H)
  Kategorie-Toepfe (Alle, nur A, gesamt, x 12 Kategorien = 12)
  Jahrestoepfe x Kongruenz (17 x 2 = 34)
  Modus-Vergleich (Alle muendlich vs. alle schriftlich = 2)
  Originalitaets-Toepfe (nur haeufig wiederholte Aussagen = 1)
  Bottom-Up-Cluster x Epochen (~8 x 5 = 40)

  Summe Schicht 4: ~189

================================================================
GESAMT: ~400-410 Toepfe (davon ~210 Prio 1, ~190 Prio 2)
================================================================
```

---

*Dimensionsanalyse erstellt am 2026-02-11*
*Forschungsprojekt: Transhumanismus / Silicon Valley Worldviews*
