# Analyse: Instanztrennung bei historischen Durchführungen

> Erstellt: 2026-03-31
> Anlass: TODO v7.0 — Aufgabe "G6/Say-Do Instanztrennung klären"
> Methode: Systematische Prüfung aller Rating-Dateien, Synthese-Dateien, Batch-Skripte und Session-Logs

---

## Fragestellung

Wurden die verschiedenen Analysen (insbesondere Batch 1: GA_ges_A, GA_ges_H, GA_ges_AH sowie G6 Kontrollexperiment) in SEPARATEN LLM-Instanzen durchgeführt oder in derselben Session/Instanz?

**Grundprinzip (v7.0): Jede Analyse = separate Instanz. Keine Ausnahmen.**

---

## Befunde

### 1. Batch 1 (Kern-Synthesen) — SELBE INSTANZ

**Evidenz:**
- `rating_batch1_D01-D12.md`: ALLE 5 SUs (GA_ges_AH, T10_ges_AH, HOM_haeuf_A, GA_ges_A, GA_ges_H) in **EINER Datei**
- Rater: Claude Opus 4.6 (nicht die 9 parallelen Sonnet-Batch-Agenten)
- Datum: 2026-02-12
- Am Ende: **"Komparative Beobachtungen"** — der Rater vergleicht direkt GA_ges_A vs. GA_ges_H
- Die Synthese-Dateien (synthese_GA_ges_A.md, synthese_GA_ges_H.md, synthese_GA_ges_AH.md) tragen alle dasselbe Datum
- Die Vergleichsdatei (vergleich_VG01_sagen_vs_handeln.md) ebenfalls 2026-02-12

**Bewertung:** NICHT GETRENNT. Der Rater hatte beim Rating von GA_ges_H die GA_ges_A-Werte im Kontext.

### 2. Batch 4 (Gruppen-Synthesen) — GETRENNTE INSTANZEN

**Evidenz:**
- 3 separate Rating-Dateien: `rating_gruppen_A_D01-D12.md` (Rollen+Gender), `rating_gruppen_B_D01-D12.md` (Firmen), `rating_gruppen_C_D01-D12.md` (Haltung)
- Rater: Claude Sonnet 4.5
- Konsolidierte Datei `rating_gruppen_D01-D12.md` verweist explizit auf "Quellen: rating_gruppen_A/B/C_D01-D12.md"

**Bewertung:** MINDESTENS 3 separate Instanzen (eine pro A/B/C-Datei).

### 3. 100 Individual-Ratings — GETRENNTE INSTANZEN

**Evidenz:**
- `rating_GESAMT_D01-D12.md`, Zeile 5: "Rater: Claude Sonnet 4.5 (9 parallele Batch-Agenten + 1 Opus-Pilot)"

**Bewertung:** 9 separate Instanzen bestätigt.

### 4. G5 v2 Cross-Modal Prediction — GETRENNTE INSTANZEN

**Evidenz:**
- `G5_BERICHT_NEU.md`: Explizit dokumentiert als "Op4a/Op4b getrennte Instanzen"
- v1 (88% confirmed) wurde genau wegen fehlender Instanztrennung invalidiert

**Bewertung:** GETRENNT (explizit dokumentiert).

### 5. Blindtest (Platzhalter vs. Fiktive Namen) — GETRENNTE INSTANZEN

**Evidenz:**
- `BLINDTEST_BERICHT.md`: "Separate Agenten-Instanzen (keine Kontamination)"

**Bewertung:** GETRENNT (explizit dokumentiert).

### 6. G1 Run-Konvergenz — GETRENNTE RUNS

**Evidenz:**
- `g1_g6_results.json`: Enthält "original", "run1", "run2" für 5 Gruppen
- run1 und run2 durchgeführt am 2026-03-30 als neue unabhängige Runs

**Bewertung:** GETRENNT (by design).

### 7. G6 Expected-Discrepancy Kontrolle — UNKLAR

**Evidenz:**
- `g1_g6_results.json`: Enthält "aussagen" und "handlungen" Rating-Vektoren
- Durchgeführt am 2026-03-30 (selbe Session wie G1)
- Keine explizite Dokumentation ob Aussagen- und Handlungen-Rating in separaten Instanzen

**Bewertung:** UNKLAR — wahrscheinlich selbe Instanz, da G1 und G6 in einer Session dokumentiert.

### 8. Session-Logs

- Keine Konversationsprotokolle aus Februar 2026 (Zeitpunkt der Batch-1-Durchführung) vorhanden
- Claude-Projektlogs im Desktop-Ordner beginnen erst im März 2026
- Rekonstruktion aus Logs daher NICHT MÖGLICH

---

## Gesamtübersicht

| Analyse | Modell | Instanztrennung | Betroffener Befund |
|---------|--------|----------------|--------------------|
| **Batch 1 Ratings** (GA_ges_A, GA_ges_H, GA_ges_AH, T10, HOM) | Opus 4.6 | **NEIN** — eine Datei, ein Rater | RQ3 Say-Do-Vergleich |
| **VG01 Sagen vs. Handeln** | Opus 4.6 | **NEIN** — basiert auf Batch-1-Ratings | RQ3-Ergebnis |
| **Batch 4 Gruppen** (15 Gruppen) | Sonnet 4.5 | **JA** — 3 separate Dateien | Alle Gruppenvergleiche |
| **100 Individual Ratings** | Sonnet 4.5 | **JA** — 9 parallele Agenten | PCA, HDBSCAN, KW |
| **G5 v2 Cross-Modal** | Opus 4.6 | **JA** — explizit dokumentiert | Cross-Modal Prediction |
| **Blindtest** | Opus 4.6 | **JA** — explizit dokumentiert | Anonymisierungs-Robustheit |
| **G1 Run-Konvergenz** | Opus 4.6 | **JA** — by design | Test-Retest ICC=0.902 |
| **G6 Expected-Discrepancy** | Opus 4.6 | **UNKLAR** | Kontrollexperiment |

---

## Konsequenzen

### MUSS wiederholt werden:
1. **GA_ges_A** — Op1+Op2 in separater Instanz (kein Kontext von GA_ges_H)
2. **GA_ges_H** — Op1+Op2 in separater Instanz (kein Kontext von GA_ges_A)
3. **G6** — Aussagen-Rating und Handlungen-Rating in getrennten Instanzen

### Kann bleiben:
- **GA_ges_AH** — wird nicht gegen GA_ges_A/H verglichen, eigene Syntheseeinheit
- **T10_ges_AH, HOM_haeuf_A** — keine methodische Abhängigkeit untereinander
- **Alle Batch-4-Gruppen** — bereits getrennt
- **G1, G5 v2, Blindtest** — bereits sauber

### Automatisch gelöst:
- **VG01** — ergibt sich neu aus den unabhängigen GA_ges_A/H Ratings

---

*Erstellt: 2026-03-31 | Methode: Dateianalyse + Strukturevidenz | Autor: Claude Opus 4.6*
