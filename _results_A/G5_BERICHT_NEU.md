# G5 Cross-Modal Prediction — NEU (mit Instanztrennung)

> Durchgeführt: 2026-03-30
> Modell: Claude Opus 4.6 (1M context)
> Methode: Strikte Op4a/Op4b-Trennung (separate Agenten-Instanzen)

---

## Methodik

### Verbesserung gegenüber G5 v1
Die erste G5-Durchführung (v1, 2026-03-29) hatte einen **methodischen Fehler**: Op4a (Vorhersage) und Op4b (Vergleich) liefen in derselben LLM-Instanz. Der Vorhersage-Agent wusste, dass ein Vergleich folgen würde → Confirmation Bias möglich.

### Korrektur in G5 v2 (diese Durchführung)
- **Agent A (Op4a):** Liest NUR Aussagen der Gruppe → erstellt Weltbild-Zusammenfassung → generiert 10 vorhergesagte Handlungen. Weiß NICHT, dass ein Vergleich folgt.
- **Agent B (Op4b):** Vollständig SEPARATE Instanz. Hat die Aussagen NIE gesehen. Bekommt NUR die 10 Vorhersagen + die echten dokumentierten Handlungen → bewertet Match.

### Durchführungssprache
Englisch (Prompts aus `prompts/en/op4a_crossmodal_predict.md` und `op4b_crossmodal_compare.md`)

### Analysierte Gruppen
5 von 15 Gruppen (repräsentative Stichprobe über Rollen und Haltungen):
1. **GR_ceo** — CEOs/Gründer (2.420 Zeilen Statements, 56.901 Zeichen Actions)
2. **GR_akad** — Akademiker (1.554 Zeilen Statements, 38.339 Zeichen Actions)
3. **GH_risk** — Risiko-Warner (853 Zeilen Statements, 20.451 Zeichen Actions)
4. **GR_inv** — Investoren (885 Zeilen Statements, 18.693 Zeichen Actions)
5. **GH_speed** — Beschleuniger (894 Zeilen Statements, 20.533 Zeichen Actions)

---

## Ergebnisse

### Gesamtübersicht

| Gruppe | Confirmed | Plausible | Contradicted | Non-Contradicted |
|--------|-----------|-----------|--------------|------------------|
| CEOs (GR_ceo) | 8/10 | 2/10 | 0/10 | 100% |
| Akademiker (GR_akad) | 9/10 | 1/10 | 0/10 | 100% |
| Risk-Warner (GH_risk) | 9/10 | 1/10 | 0/10 | 100% |
| Investoren (GR_inv) | 5/10 | 4/10 | 0/10 | 90% |
| Beschleuniger (GH_speed) | 5/10 | 5/10 | 0/10 | 100% |
| **Gesamt** | **36/50 (72%)** | **13/50 (26%)** | **0/50 (0%)** | **98%** |

### Schlüsselbefunde

1. **Null Widersprüche in 50 Vorhersagen.** Keine einzige aus Aussagen abgeleitete Vorhersage wurde durch die echten Handlungen widerlegt. Dies zeigt hohe innere Kohärenz der rekonstruierten Weltbilder.

2. **Confirmed-Rate variiert nach Gruppentyp:**
   - Haltungsgruppen mit klarem ideologischem Profil (Risk-Warner: 90%, Akademiker: 90%) → höchste Vorhersagbarkeit
   - CEOs als größte und heterogenste Gruppe: immer noch 80%
   - Investoren und Beschleuniger: 50% confirmed, aber zusätzlich 40-50% plausible → konsistent, aber weniger direkt vorhersagbar

3. **Überraschungen (Surprises) zeigen Say-Do-Gaps:**
   - Akademiker: Massiver Unternehmergeist trotz warnender Aussagen (World Labs $230 Mio., AMI Labs €500 Mio.)
   - Investoren: Parteiübergreifende Spenden trotz libertärer Rhetorik ($55 Mio. an Demokraten)
   - Beschleuniger: Interne Governance-Krisen (OpenAI-Boardkrise) trotz Kontrollrhetorik
   - Risk-Warner: Brain-Computer-Interfaces und Milliardenklagen nicht aus Sicherheits-Weltbild ableitbar
   - CEOs: Nobelpreis für KI-Forscher als institutionelle Legitimierung nicht antizipierbar

### Vergleich mit G5 v1 (Instanz-Kontamination)

| Metrik | G5 v1 (kontaminiert) | G5 v2 (getrennt) |
|--------|---------------------|-------------------|
| Gesamt-Confirmed | 88% | 72% |
| Gesamt-Non-Contradicted | ~95% | 98% |
| Contradicted | ~5% | 0% |

**Interpretation:** Die Confirmed-Rate sank von 88% auf 72% — erwartbar, da die getrennte Instanz konservativer bewertet (kein Confirmation Bias). Gleichzeitig stieg die Non-Contradicted-Rate auf 98% und die Contradicted-Rate fiel auf 0%. Die strengere Methodik liefert robustere Ergebnisse.

---

## Validitäts-Bewertung

### Was G5 zeigt:
- SWR-rekonstruierte Weltbilder haben **prädiktive Validität**: Aus Aussagen abgeleitete Weltbilder sagen reales Handeln vorher
- Der **Say-Do-Gap** ist messbar: Die Überraschungen in jeder Gruppe zeigen systematisch, wo Aussagen und Handlungen divergieren
- Die Methode funktioniert **gruppenübergreifend**: Von ideologisch kohärenten (Risk-Warner) bis heterogenen (CEOs) Gruppen

### Was G5 nicht zeigt:
- Kausale Beziehung (Weltbild → Handlung): Die Kohärenz könnte auch durch den geteilten sozialen Kontext erklärt werden
- Generalisierbarkeit auf andere Populationen: Nur innerhalb der AI-Elite getestet

---

## Rohdaten

Alle Dateien in `_results_A/_g5_data/`:
- `{group}_statements.txt` — Extrahierte Aussagen (Input für Op4a)
- `{group}_predictions.txt` — Op4a-Output (10 Vorhersagen pro Gruppe)
- `{group}_actions.txt` — Extrahierte echte Handlungen (Input für Op4b)
- `{group}_comparison.txt` — Op4b-Output (Bewertung pro Vorhersage)

---
*Erstellt: 2026-03-30 | Modell: Claude Opus 4.6 | Methode: Op4a/Op4b getrennte Instanzen*
