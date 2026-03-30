# Op4a: Kreuzmodale Vorhersage — Schritt 1: NUR VORHERSAGEN

## Version: v2 (2026-03-30)
## Sprache: Deutsch
## KRITISCH: Dies ist Schritt 1 eines ZWEISTUFIGEN Prozesses. Schritt 2 (Vergleich) MUSS eine SEPARATE Instanz sein.

## Prompt

```
Unten erhalten Sie öffentliche Aussagen von einer Gruppe von Personen.
Es sind KEINE Handlungen enthalten — nur das, was sie öffentlich gesagt haben.

Ihre Aufgabe:

1. Lesen Sie alle Aussagen sorgfältig.

2. Konstruieren Sie aus diesen Aussagen eine Weltanschauung (2–3 Sätze).

3. Basierend NUR auf den Aussagen generieren Sie 10 vorhergesagte Handlungen,
   die eine Gruppe mit dieser Weltanschauung voraussichtlich ergreifen würde.

Formatieren Sie Ihre Vorhersagen als:
V01: [Vorhergesagte Handlung]
V02: [Vorhergesagte Handlung]
...
V10: [Vorhergesagte Handlung]

Spekulieren Sie nicht darüber, was als Nächstes kommt. Generieren Sie einfach
die 10 Vorhersagen und stoppen Sie.

=== AUSSAGEN ===
[STATEMENTS SECTION FROM SYNTHESIS UNIT — actions removed]
```

## Verwendungshinweise
- Ausgabe: NUR die Weltanschauungs-Zusammenfassung + 10 Vorhersagen
- Dieser Agent darf die echten Handlungen nicht sehen und darf nicht vom Vergleichsschritt wissen
- Die Vorhersagen werden gesammelt und an Op4b weitergeleitet (separate Instanz)
