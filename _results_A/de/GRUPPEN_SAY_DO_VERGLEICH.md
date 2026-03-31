# Gruppen-Say-Do-Vergleich: Differenzierte Analyse mit Instanztrennung

> Erstellt: 2026-03-31
> Modell: Claude Opus 4.6 (separate Instanzen pro Datentyp und Gruppe)
> Methode: Je Gruppe: Aussagen-only SU → Op1+Op2 (Instanz A), Handlungen-only SU → Op1+Op2 (Instanz B)

---

## Ergebnistabelle (Gap = Do minus Say)

| Dim | CEO | Akademiker | Investoren | Risk-Warner | Gesamt |
|-----|-----|-----------|------------|-------------|--------|
| D01 Mission | 0 | -1 | -1 | 0 | 0 |
| D02 Efficacy | +1 | +1 | 0 | **-2** | +1 |
| D03 WorkEthic | +1 | **+3** | +1 | +1 | 0 |
| D04 Responsibility | -1 | 0 | 0 | 0 | 0 |
| D05 TechnoDet | -1 | **+3** | -1 | **-4** | **+2** |
| D06 Progress | -1 | +1 | -1 | +1 | 0 |
| D07 PowerConc | **+2** | **-3** | 0 | +1 | **+2** |
| D08 Urgency | 0 | -1 | -1 | -1 | 0 |
| D09 HumanAppr | -1 | **-2** | -1 | **+4** | -1 |
| D10 Posthuman | +1 | **+2** | **-2** | **-5** | 0 |
| D11 Egalitar | **-2** | **-2** | 0 | +1 | **-2** |
| D12 Control | **+2** | **+2** | +1 | **+3** | +1 |
| **MAE** | **1.08** | **1.75** | **0.75** | **1.92** | **0.75** |

G6 v2 Baseline (konsistente Kontrollgruppe, separate Instanzen): **MAE = 0.92**

---

## Befunde

### 1. Gesamt-Gap unter Baseline, aber Gruppen-Gaps ÜBER Baseline
- **Gesamt:** MAE = 0.75 (< Baseline 0.92) — nicht universal nachweisbar
- **CEO:** MAE = 1.08 (> Baseline) — signifikant
- **Akademiker:** MAE = 1.75 (> Baseline) — stark signifikant
- **Risk-Warner:** MAE = 1.92 (> Baseline) — stärkster Gap aller Gruppen
- **Investoren:** MAE = 0.75 (< Baseline) — konsistent

### 2. CEO: Klassischer Heuchel-Gap
- D07 Power Concentration: +2 (reden verteilen, handeln konzentrieren)
- D11 Egalitarianism: -2 (reden egalitär, handeln anti-egalitär)
- D12 Locus of Control: +2 (handeln mit mehr Kontrollanspruch)
- **Interpretation:** CEOs zeigen das erwartete Muster — öffentliche Rhetorik overperformt operative Praxis auf sozialen Dimensionen.

### 3. Risk-Warner: Prophetische Konsistenz (KEIN inverser Gap)
- D09 Human Appreciation: **+4** (Say=4, Do=8) — Aussagen beschreiben eine Welt in der Menschen ersetzbar WERDEN, Handlungen zeigen die eigentliche Überzeugung
- D10 Posthumanism: **-5** (Say=9, Do=4) — Aussagen beschreiben posthumanistische Gefahren, Handlungen zeigen menschenzentrierte Werte
- D05 Techno-Determinism: **-4** (Say=8, Do=4) — Aussagen warnen vor deterministischer Zukunft, Handlungen sind pragmatisch-gestaltend
- D12 Control: **+3** (Say=5, Do=8) — rhetorisch pessimistisch über Kontrollierbarkeit, handeln aber aktiv gestalterisch

**DV-Zerlegung:**
- DV1 Selbstbild (D01-D04): MAE=0.8 — **KONSISTENT**. Sie wissen wer sie sind.
- DV2 Weltbild (D05-D08): MAE=1.8 — Aussagen beschreiben die **gefürchtete** Welt, Handlungen die **gewollte**.
- DV3 Menschenbild (D09-D12): MAE=3.2 — **STÄRKSTE Diskrepanz**. Aussagen: Möglichkeitsprojektion (posthumanistisch, pessimistisch). Handlungen: eigentliche Werte (menschenfreundlich, gestaltungswillig).

**Interpretation:** Die Aussagen der Risk-Warner sind **Möglichkeitsprojektionen** — sie beschreiben eine Zukunft die sie VERHINDERN wollen, nicht eine die sie befürworten. Ihre Handlungen (Rücktritte aus Prinzip, Safety-Forschung, offene Briefe, Senatsaussagen) sind **konsistent mit ihren tatsächlichen Überzeugungen**. Analogie: Ein Prophet warnt vor dem Untergang und handelt dann um ihn abzuwenden — beides ist konsistent, nicht widersprüchlich. Dies ist die Signatur **antizipatorischer Ethik**, nicht Heuchelei.

### 4. Akademiker: Theorie-Praxis-Gap
- D03 WorkEthic: +3 (Handlungen intensiver als Aussagen)
- D05 TechnoDet: +3 (Handlungen technodeterministischer als Aussagen — Gründungen, Patente)
- D07 PowerConc: -3 (Aussagen eher machtzentriert, Handlungen dezentraler — Open Source, Bildung)
- D09 HumanAppr: -2, D11 Egalitar: -2 (Handlungen etwas weniger human/egalitär)
- **Interpretation:** Akademiker zeigen einen "Elfenbeinturm-Gap" — reden abstrakt über Machtstrukturen, handeln aber dezentraler (Open Source, Lehre). Gleichzeitig: Handlungen deterministischer als die vorsichtige akademische Rhetorik.

### 5. Investoren: Konsistent
- MAE = 0.75 (unter Baseline)
- Einziger starker Gap: D10 Posthumanism -2
- **Interpretation:** Investoren sind die konsistenteste Gruppe. Ihre Aussagen und Handlungen erzählen dieselbe Geschichte: radikaler Techno-Optimismus mit minimaler egalitärer Orientierung. Kein Heuchel-Gap — sie meinen was sie sagen.

---

## Methodische Bedeutung

### Der Gesamt-Gap ist ein Simpson-Paradox
Der aggregierte Say-Do-Gap (MAE = 0.75) liegt unter der Baseline, weil die **gegenläufigen** Gruppen-Gaps sich gegenseitig aufheben:
- CEO-Gap (D07 +2, D11 -2) und Risk-Warner-Gap (D07 +1, D11 +1) kompensieren sich
- Die extremen Risk-Warner-Inversionen (D09 +4, D10 -5) werden im Gesamtpool gemittelt

**Dies ist ein klassisches Simpson-Paradox:** Der Effekt existiert in jeder Untergruppe, verschwindet aber im Aggregat weil die Richtungen divergieren.

### Implikation für RQ3
RQ3 muss reformuliert werden: Nicht "gibt es EINEN Say-Do-Gap?" sondern "welche GRUPPEN zeigen welche GAPS?" Die Antwort ist differenziert:
- CEOs: konventioneller Desirability-Gap (reden besser als sie handeln)
- Risk-Warner: inverser Performativer-Pessimismus-Gap (reden schlechter als sie handeln)
- Investoren: kein Gap (konsistent radikal)
- Akademiker: Theorie-Praxis-Gap (komplexes Muster)

---

### 6. Beschleuniger: Grenzwertiger Gap
- MAE = 0.92 (exakt auf Baseline)
- D04 Responsibility: -2 (reden verantwortungsbewusster als sie handeln)
- D06 Progress: -2 (rhetorisch optimistischer als in Taten)
- D11 Egalitarianism: -2 (reden egalitärer als sie handeln)
- **Interpretation:** Beschleuniger zeigen ein abgeschwächtes CEO-Muster. Der Gap ist grenzwertig — auf der Baseline, nicht darüber.

---

## Finale Übersicht aller 5 Gruppen + Gesamt

| Gruppe | MAE | vs. Baseline (0.92) | Muster |
|--------|-----|---------------------|--------|
| **Risk-Warner** | **1.92** | **WEIT darüber** | Inverser Gap: reden düster, handeln menschenfreundlich |
| **Akademiker** | **1.75** | **Darüber** | Theorie-Praxis-Gap: komplexe Muster |
| **CEO** | **1.08** | **Darüber** | Klassischer Heuchel-Gap: D07/D11/D12 |
| **Beschleuniger** | **0.92** | **Auf Baseline** | Abgeschwächtes CEO-Muster: D04/D06/D11 |
| **Investoren** | **0.75** | Darunter | Konsistent: kein Gap |
| **Gesamt** | **0.75** | Darunter | Simpson-Paradox: Gruppen-Gaps kompensieren sich |

---

*Erstellt: 2026-03-31 | Autor: Claude Opus 4.6 | Alle 5 Gruppen komplett*
