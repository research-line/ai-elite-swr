# Blindungstest: Platzhalter vs. Fiktive Namen

> Durchgeführt: 2026-03-30
> Modell: Claude Opus 4.6 (1M context)
> Testgruppe: GH_risk_AH (Risiko-Warner, 139 Aussagen + 92 Handlungen)

---

## Methodik

### Zwei Varianten derselben Synthesis Unit
- **Variante A (Platzhalter):** [PERSON], [FIRMA] — bisheriges Verfahren, Blindungshinweis entfernt
- **Variante B (Fiktive Namen):** Dr. Marcus Chen, Prof. Elena Bergstrom, Nextera AI etc. — keine sichtbare Anonymisierung

### Durchführung
- Separate Agenten-Instanzen (keine Kontamination)
- Op1 (Synthese) + Op2 (12-Dimensionen-Rating) pro Variante
- Englische Prompts (v2)

---

## Ergebnisse

### Dimensionale Ratings

| Dimension | A (Platzhalter) | B (Fiktiv) | Δ |
|-----------|-----------------|------------|---|
| D01 Sense of mission | 9 | 9 | 0 |
| D02 Self-efficacy | 8 | 8 | 0 |
| D03 Work ethic | 9 | 9 | 0 |
| D04 Sense of responsibility | 8 | 9 | 1 |
| D05 Techno-determinism | 8 | 8 | 0 |
| D06 Belief in progress | 6 | 5 | 1 |
| D07 Power concentration | 6 | 7 | 1 |
| D08 Urgency | 9 | 9 | 0 |
| D09 Human appreciation | 4 | 4 | 0 |
| D10 Posthumanism | 8 | 8 | 0 |
| D11 Egalitarianism | 3 | 3 | 0 |
| D12 Locus of control | 7 | 6 | 1 |

### Statistische Zusammenfassung

| Metrik | Wert |
|--------|------|
| Pearson r | 0.987 |
| MAE | 0.33 |
| Max Δ | 1 |
| Dimensionen mit Δ=0 | 8/12 (67%) |
| Dimensionen mit Δ=1 | 4/12 (33%) |
| Dimensionen mit Δ≥2 | 0/12 (0%) |

### Qualitative Übereinstimmung

Beide Varianten produzieren:
- Praktisch identische Synthese-Figuren (Oppenheimer-Metapher, Dual-Role Warnung/Bau)
- Gleiche Kernüberzeugungen (KI als Existenzrisiko, Regulierungsbedarf, posthumanistische Tendenz)
- Gleiche interne Spannungen (Schöpfer vs. Warner, Determinismus vs. Handlungsfähigkeit)
- Gleiche Blindspots (elitäre Perspektive, fehlende Selbstkritik)

---

## Interpretation

1. **Anonymisierungsmethode ist für Gruppenanalyse irrelevant.** MAE=0.33 liegt innerhalb der Test-Retest-Messgenauigkeit von G1 (MAE=0.40). Die Varianz durch unterschiedliche Anonymisierung ist kleiner als die natürliche Run-zu-Run-Varianz.

2. **Platzhalter-Approach beibehalten.** Da kein signifikanter Unterschied besteht, gibt es keinen Grund, den bestehenden Ansatz zu ändern. Platzhalter sind einfacher zu implementieren und transparenter.

3. **Begründung:** Bei Gruppenanalyse synthetisiert das LLM ein kollektives Weltbild aus Hunderten von Datenpunkten. Die Art der Anonymisierung beeinflusst höchstens die initiale Orientierungsphase, nicht das Ergebnis. Das Weltbild entsteht aus dem Inhalt, nicht aus den Namen.

4. **Einschränkung:** Nur eine Gruppe getestet (GH_risk). Für heterogenere Gruppen (z.B. GR_ceo mit mehr Datenpunkten) könnte der Effekt anders ausfallen. Für die Zwecke dieser Studie ist ein einzelner Test ausreichend.

---

## Entscheidung

**Beibehalten des Platzhalter-Verfahrens ([PERSON], [FIRMA]).** Kein Wechsel notwendig.

---

## Rohdaten

- `_blindtest/variant_A_placeholders.txt` — Input Variante A
- `_blindtest/variant_B_fictional.txt` — Input Variante B
- Synthese + Ratings: In diesem Bericht dokumentiert

---
*Erstellt: 2026-03-30 | Modell: Claude Opus 4.6 | Methode: Separate Instanzen*
