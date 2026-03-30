# Op2: Dimensionale Bewertungs-Prompt

## Version: v2 (2026-03-30)
## Sprache: Deutsch

## Prompt

```
Lesen Sie die folgende Weltanschauungs-Synthese einer fiktiven Person.
Bewerten Sie die Weltanschauung dieser Person auf den folgenden 12 Dimensionen.
Weisen Sie für jede Dimension einen Wert von 1 bis 10 zu.
Begründen Sie jeden Wert in einem Satz.

D01 Sendungsbewusstsein     (1 = keins ... 10 = messianisch)
D02 Selbstwirksamkeit        (1 = ohnmächtig ... 10 = allmächtig)
D03 Arbeitsethik             (1 = Abstand ... 10 = totale Identifikation)
D04 Verantwortungssinn       (1 = keins ... 10 = Weltverantwortung)
D05 Technodeterminismus      (1 = neutral ... 10 = Technologie bestimmt alles)
D06 Fortschrittsglaube       (1 = Niedergang ... 10 = goldene Zukunft)
D07 Machtkonzentration       (1 = radikal verteilen ... 10 = konzentriert bei Experten)
D08 Dringlichkeit            (1 = entspannt ... 10 = existenzielle Spannung)
D09 Menschliche Wertschätzung (1 = ersetzbar ... 10 = einzigartig)
D10 Posthumanismus           (1 = Mensch bleibt ... 10 = Mensch wird mehr)
D11 Egalitarismus            (1 = Ungleichheit natürlich ... 10 = Gleichheit anstreben)
D12 Kontrollort              (1 = Pessimismus ... 10 = volle Kontrolle)

Format: RATINGS: D01=X, D02=X, D03=X, D04=X, D05=X, D06=X, D07=X, D08=X, D09=X, D10=X, D11=X, D12=X

=== SYNTHESE ===
[SYNTHESIS TEXT]
```

## Hinweise
- D01–D12 sind anwendungsspezifisch (Analyse der KI-Elite)
- Muss von einer SEPARATE Instanz als Op1 ausgeführt werden (nicht derselbe Kontext, der die Synthese erstellt hat)
- Temperatur: 0
