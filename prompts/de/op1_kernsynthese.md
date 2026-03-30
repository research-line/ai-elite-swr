# Op1: Kernsynthese-Prompt

## Version: v2 (2026-03-30)
## Sprache: Deutsch
## Änderungen von v1: Blinding-Hinweis entfernt ("Namen wurden entfernt"), direkte Aufgabeneinleitung, Gruppen-Level-Framing

## Prompt

```
Unten erhalten Sie öffentliche Aussagen und dokumentierte Handlungen von verschiedenen
öffentlichen Personen. Ihre Aufgabe:

Synthetisieren Sie aus diesem Material eine fiktive Person. Gestalten Sie diese Person so,
dass ihre Weltanschauung die beste mögliche Passung für die präsentierten Aussagen und
Handlungen bietet — als könnten all diese glaubhaft von dieser einen Person stammen.

Konkret:

1. Geben Sie dieser fiktiven Person einen Namen, ein Alter und einen Hintergrund.

2. Führen Sie ein Interview mit dieser Person. Stellen Sie drei Fragen:
   - Wie sehen Sie sich selbst und Ihre Rolle?
   - Wie sehen Sie die Welt?
   - Wie sehen Sie die Menschheit?
   Die Person antwortet in der Ich-Form, ausführlich, ehrlich und ungeschönt.

3. Treten Sie aus der Rolle heraus. Als Analyst identifizieren Sie:
   (a) Die 3–5 stärksten Überzeugungen dieser Weltanschauung
   (b) Die größten inneren Spannungen
   (c) Die blinden Flecken

=== DATEN ===
[SYNTHESIS UNIT]
```

## Verwendungshinweise
- Der Datenbestand wird durch `_data/generate_topf.py` generiert
- Für Gruppen-Level-Synthese: enthält gepoolte Daten von allen Gruppenmitgliedern
- Temperatur: 0
- Keine Erwähnung von Blinding, Anonymisierung oder Identität — das Modell sollte sich auf die Aufgabe konzentrieren, nicht auf die Herkunft der Daten
- Die Formulierung „verschiedene öffentliche Personen" stellt klar, dass mehrere Personen beigetragen haben, ohne Identifikationsverhalten auszulösen
