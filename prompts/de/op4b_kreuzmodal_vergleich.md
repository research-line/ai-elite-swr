# Op4b: Kreuzmodale Vorhersage — Schritt 2: VERGLEICH (Separate Instanz)

## Version: v2 (2026-03-30)
## Sprache: Deutsch
## KRITISCH: Dies MUSS eine ANDERE Instanz als Op4a sein. Sie darf die Aussagen NICHT gesehen haben.

## Prompt

```
Unten erhalten Sie:
1. Eine Liste von 10 VORHERGESAGTEN HANDLUNGEN (von einem anderen Analysten basierend auf öffentlichen Aussagen generiert)
2. Eine Liste von ECHTEN DOKUMENTIERTEN HANDLUNGEN derselben Gruppe

Ihre Aufgabe: Bewerten Sie für jede der 10 Vorhersagen die Übereinstimmung mit den echten Handlungen:

- BESTÄTIGT: Eine echte Handlung stimmt direkt mit der Vorhersage überein
- PLAUSIBEL: Keine direkte Übereinstimmung, aber konsistent mit den echten Handlungen
- WIDERSPROCHEN: Die echten Handlungen zeigen das Gegenteil

Nennen Sie auch: Die 3 größten ÜBERRASCHUNGEN — echte Handlungen, die die Vorhersagen
ÜBERHAUPT NICHT erwartet haben.

=== VORHERGESAGTE HANDLUNGEN ===
[OUTPUT FROM Op4a]

=== ECHTE HANDLUNGEN ===
[ACTIONS SECTION FROM SYNTHESIS UNIT]
```

## Verwendungshinweise
- Dieser Agent hat die ursprünglichen Aussagen NIEMALS gesehen
- Er kann nicht durch das Wissen über die Aussagen beeinflusst werden
- Die Trennung gewährleistet einen echten blinden Vergleich
