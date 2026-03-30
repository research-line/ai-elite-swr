# G5: Cross-Modal Prediction (Op4)

> Datum: 2026-03-30
> Methode: Aussagen → Weltbild → vorhergesagte Handlungen → Abgleich mit echten Handlungen
> Instrument: Claude Opus 4.6 (5 unabhängige Agenten)

---

## Fragestellung

Kann das aus öffentlichen Aussagen rekonstruierte Weltbild die tatsächlichen Handlungen einer Gruppe vorhersagen? Dies ist der stärkste integrale Validierungstest der SWR-Methode (Operationalisierung 4).

## Methode

Für jede Gruppe:
1. Agent liest NUR die Aussagen (HANDLUNGEN werden ignoriert)
2. Agent konstruiert ein Weltbild aus den Aussagen
3. Agent generiert 10 vorhergesagte Handlungen
4. Agent liest die echten Handlungen
5. Agent vergleicht: BESTÄTIGT / PLAUSIBEL / WIDERLEGT
6. Agent nennt die 3 größten Überraschungen (nicht vorhersagbare Handlungen)

## Ergebnisse

| Gruppe | n (Aussagen/Handlungen) | Bestätigt | Plausibel | Widerlegt |
|--------|-------------------------|-----------|-----------|-----------|
| CEOs | ~300/285 | 10/10 | 0/10 | 0/10 |
| Akademiker | ~246/183 | 10/10 | 0/10 | 0/10 |
| Risiko-Warner | ~139/92 | 9/10 | 1/10 | 0/10 |
| Investoren | ~135/108 | 9/10 | 1/10 | 0/10 |
| Beschleuniger | ~140/100 | 6/10 | 4/10 | 0/10 |
| **GESAMT** | | **44/50 (88%)** | **6/50 (12%)** | **0/50 (0%)** |

### Bewertung
- **88% der vorhergesagten Handlungen** wurden durch echte Handlungen direkt bestätigt
- **0% widerlegt** — keine einzige Vorhersage wurde durch das Gegenteil in den Handlungen falsifiziert
- **12% plausibel** — konsistent, aber ohne direktes Match (meist fehlende Handlungskodierung)

### Gruppenvergleich
- **CEOs und Akademiker (100%):** Höchste Vorhersagekraft. Bei CEOs folgen die Handlungen fast lehrbuchmäßig der Rhetorik. Bei Akademikern ist das Weltbild hochgradig konsistent.
- **Risiko-Warner und Investoren (95%):** Sehr hohe Vorhersagekraft. Einzige Lücke: Mars/Raumfahrt (nicht in Handlungs-Kodierung) bzw. Robotik (noch keine Investments dokumentiert).
- **Beschleuniger (80%):** Niedrigste, aber immer noch hohe Vorhersagekraft. 4 plausible statt bestätigte Items, vor allem weil Medienauftritte und Lobbying nicht als separate Handlungen kodiert waren.

## Die wichtigsten Überraschungen (nicht vorhersagbar)

### Systematische Muster in den Überraschungen

1. **Opportunistische politische Kehrtwenden** (CEOs, Investoren): Von Anti-Trump zu Pro-Trump, von Biden-Spenden zu Trump-Inaugurationsspenden. Die Aussagen zeigen Werte, die Handlungen zeigen Pragmatismus.

2. **Kommerzielle Verwertung bei altruistischer Rhetorik** (Akademiker): Milliarden-Börsengänge (Coursera $4,3 Mrd., World Labs $1 Mrd.) bei gleichzeitigem Fokus auf Open Science und Bildung für alle.

3. **Widersprüchliches Krisenverhalten** (Risiko-Warner): Board-Krisen, Supercomputer-Bau bei gleichzeitiger Warnung vor zu schneller Entwicklung, Milliarden-Fundraising bei Extinction-Risk-Warnungen.

4. **Strategische Fehler** (Beschleuniger): WeWork-Desaster ($14 Mrd. Abschreibung), NVIDIA-Stake-Verkauf ("größter Fehler"). Aus optimistischen Aussagen nicht ableitbar.

5. **Ethik-Rücknahmen** (CEOs): Google entfernt KI-Ethik-Prinzipien zu Waffen/Überwachung (2025), obwohl Aussagen bis zuletzt "responsible AI" betonten.

## Methodische Implikation

Die Cross-Modal Prediction validiert die SWR auf einer fundamentalen Ebene: **Das aus Aussagen rekonstruierte Weltbild hat genuine Vorhersagekraft für Handlungen.** Die 88%-Bestätigungsrate bei 0% Widerlegung ist ein starkes Ergebnis.

Gleichzeitig zeigen die **Überraschungen** genau den Mehrwert der Sagen-Handeln-Analyse (RQ3): Die Handlungen, die NICHT vorhersagbar waren, sind systematisch die, in denen der Say-Do-Gap am größten ist — politischer Opportunismus, kommerzielle Verwertung, Ethik-Rücknahmen. Diese "Lücken" in der Vorhersagekraft SIND der inhaltliche Befund.

---
*Analyse: Claude Opus 4.6 | 5 unabhängige Agenten auf 5 Gruppen-Topf-Dateien*
