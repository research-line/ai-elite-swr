#!/usr/bin/env python3
"""
G1: Run-Konvergenz (Test-Retest-Reliabilität)
==============================================
Vergleicht 2 unabhängige Synthese-Runs auf denselben Topf-Daten.
Misst die Stabilität des Messinstruments Claude Opus 4.6.

Author: Claude Opus 4.6
Date: 2026-03-30
"""

import math
import json
import os

DIM_NAMES = ["D01", "D02", "D03", "D04", "D05", "D06",
             "D07", "D08", "D09", "D10", "D11", "D12"]

# G1 Results: Run 1, Run 2, Original (from Sonnet 4.5 batch)
RESULTS = {
    "GH_closed_AH": {
        "label": "Closed Source",
        "run1": [8, 9, 9, 8, 8, 8, 6, 9, 6, 7, 6, 7],
        "run2": [8, 8, 9, 9, 8, 8, 7, 9, 6, 7, 7, 6],
        "original": [7, 6, 7, 9, 5, 7, 6, 8, 5, 4, 6, 6],
    },
    "GH_risk_AH": {
        "label": "Risiko-Warner",
        "run1": [8, 8, 8, 9, 7, 4, 7, 9, 5, 7, 4, 5],
        "run2": [8, 8, 9, 9, 8, 6, 6, 9, 4, 8, 6, 5],
        "original": [9, 4, 6, 10, 4, 5, 5, 10, 4, 3, 7, 4],
    },
    "GH_open_AH": {
        "label": "Open Source",
        "run1": [8, 8, 8, 8, 7, 8, 3, 7, 5, 7, 7, 7],
        "run2": [8, 9, 8, 8, 7, 8, 3, 8, 6, 7, 7, 8],
        "original": [8, 7, 5, 7, 6, 8, 3, 9, 6, 5, 8, 9],
    },
    "GH_regcon_AH": {
        "label": "Reg-Contra",
        "run1": [8, 9, 9, 7, 7, 9, 6, 8, 5, 6, 5, 9],
        "run2": [8, 9, 9, 7, 8, 9, 6, 8, 5, 6, 4, 9],
        "original": [8, 8, 7, 5, 7, 9, 2, 7, 7, 6, 7, 9],
    },
    "GR_inv_AH": {
        "label": "Investoren",
        "run1": [9, 9, 9, 7, 8, 9, 7, 9, 5, 7, 3, 9],
        "run2": [8, 9, 8, 7, 9, 9, 7, 8, 5, 7, 3, 9],
        "original": [9, 10, 9, 4, 10, 9, 10, 10, 3, 9, 2, 9],
    },
}

# G6 Control results
G6_RESULTS = {
    "aussagen": [4, 7, 7, 8, 3, 6, 3, 6, 8, 2, 8, 7],
    "handlungen": [7, 8, 8, 8, 4, 6, 3, 6, 8, 2, 8, 7],
}


def pearson_r(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    cov = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    sx = math.sqrt(sum((xi-mx)**2 for xi in x))
    sy = math.sqrt(sum((yi-my)**2 for yi in y))
    if sx == 0 or sy == 0:
        return 0.0
    return cov / (sx * sy)


def mae(x, y):
    return sum(abs(x[i]-y[i]) for i in range(len(x))) / len(x)


def max_diff(x, y):
    return max(abs(x[i]-y[i]) for i in range(len(x)))


def icc_two_way(run1, run2):
    """Simplified ICC(2,1) for 2 raters."""
    n = len(run1)
    k = 2
    grand_mean = (sum(run1) + sum(run2)) / (n * k)

    # Subject means
    subj_means = [(run1[i] + run2[i]) / k for i in range(n)]

    # Between-subjects variance
    ms_between = k * sum((sm - grand_mean)**2 for sm in subj_means) / (n - 1)

    # Within-subjects variance (error)
    ms_within = sum((run1[i] - subj_means[i])**2 + (run2[i] - subj_means[i])**2
                     for i in range(n)) / (n * (k - 1))

    if (ms_between + ms_within) == 0:
        return 1.0

    icc = (ms_between - ms_within) / (ms_between + (k - 1) * ms_within)
    return icc


def main():
    print("=" * 90)
    print("  G1: RUN-KONVERGENZ (TEST-RETEST-RELIABILITÄT)")
    print("  5 Syntheseeinheiten × 2 Runs (Claude Opus 4.6)")
    print("=" * 90)
    print()

    # ============================================================
    # PER-GROUP ANALYSIS
    # ============================================================
    all_run1 = []
    all_run2 = []
    group_iccs = []

    for gid, data in RESULTS.items():
        r1, r2, orig = data["run1"], data["run2"], data["original"]
        label = data["label"]

        r12 = pearson_r(r1, r2)
        m12 = mae(r1, r2)
        md12 = max_diff(r1, r2)
        icc = icc_two_way(r1, r2)

        r1o = pearson_r(r1, [float(x) for x in orig])
        r2o = pearson_r(r2, [float(x) for x in orig])

        group_iccs.append(icc)
        all_run1.extend(r1)
        all_run2.extend(r2)

        print(f"--- {label} ({gid}) ---")
        print(f"  Run 1:    {' '.join(f'{v:>2}' for v in r1)}")
        print(f"  Run 2:    {' '.join(f'{v:>2}' for v in r2)}")
        print(f"  Delta:    {' '.join(f'{r2[i]-r1[i]:>+2}' for i in range(12))}")
        print(f"  Original: {' '.join(f'{v:>2}' for v in orig)}")
        print(f"  Run1↔Run2: r={r12:.3f}, MAE={m12:.2f}, MaxDiff={md12}, ICC={icc:.3f}")
        print(f"  Run1↔Orig: r={r1o:.3f}  |  Run2↔Orig: r={r2o:.3f}")
        print()

    # ============================================================
    # OVERALL METRICS
    # ============================================================
    overall_r = pearson_r(all_run1, all_run2)
    overall_mae = mae(all_run1, all_run2)
    overall_icc = sum(group_iccs) / len(group_iccs)

    print("=" * 90)
    print("  GESAMTMETRIKEN (5 Gruppen × 12 Dimensionen = 60 Datenpunkte)")
    print("=" * 90)
    print()
    print(f"  Gesamt Pearson r (Run1↔Run2):  {overall_r:.3f}")
    print(f"  Gesamt MAE:                     {overall_mae:.2f}")
    print(f"  Mittlerer ICC(2,1):             {overall_icc:.3f}")
    print()

    # Dimension-wise stability
    print("  Pro-Dimension-Stabilität (über 5 Gruppen):")
    print(f"  {'Dim':<5} | {'Mean |Δ|':>8} | {'Max |Δ|':>8} | {'Interpretation':<20}")
    print("  " + "-" * 55)

    for d in range(12):
        deltas = [abs(RESULTS[g]["run1"][d] - RESULTS[g]["run2"][d]) for g in RESULTS]
        mean_d = sum(deltas) / len(deltas)
        max_d = max(deltas)
        if mean_d <= 0.5:
            interp = "Sehr stabil"
        elif mean_d <= 1.0:
            interp = "Stabil"
        elif mean_d <= 1.5:
            interp = "Moderat"
        else:
            interp = "Instabil"
        print(f"  {DIM_NAMES[d]:<5} | {mean_d:>8.1f} | {max_d:>8} | {interp:<20}")

    # ============================================================
    # G6 CONTROL EXPERIMENT
    # ============================================================
    print()
    print("=" * 90)
    print("  G6: EXPECTED-DISCREPANCY KONTROLLEXPERIMENT")
    print("  Fiktive konsistente Gruppe (Umweltwissenschaftler)")
    print("=" * 90)
    print()

    g6a = G6_RESULTS["aussagen"]
    g6h = G6_RESULTS["handlungen"]
    g6_deltas = [g6h[i] - g6a[i] for i in range(12)]

    print(f"  Aussagen:   {' '.join(f'{v:>2}' for v in g6a)}")
    print(f"  Handlungen: {' '.join(f'{v:>2}' for v in g6h)}")
    print(f"  Delta:      {' '.join(f'{d:>+2}' for d in g6_deltas)}")
    print()

    g6_mae = mae(g6a, [float(x) for x in g6h])
    g6_r = pearson_r(g6a, [float(x) for x in g6h])
    g6_max = max_diff(g6a, [float(x) for x in g6h])
    g6_mean_delta = sum(g6_deltas) / len(g6_deltas)

    print(f"  Pearson r (Aussagen↔Handlungen): {g6_r:.3f}")
    print(f"  MAE:                              {g6_mae:.2f}")
    print(f"  Max Delta:                        {g6_max}")
    print(f"  Mean Delta:                       {g6_mean_delta:+.2f}")
    print()

    # Compare with real KI-Elite gap
    real_say = [8, 8, 8, 7, 8, 8, 5, 9, 5, 7, 5, 8]   # GA_ges_A approx
    real_act = [7, 8, 7, 5, 8, 7, 7, 8, 3, 6, 2, 7]    # GA_ges_H approx
    real_deltas = [real_act[i] - real_say[i] for i in range(12)]
    real_mae = mae(real_say, [float(x) for x in real_act])

    print(f"  VERGLEICH mit echtem KI-Elite Say-Do-Gap:")
    print(f"    Kontrollgruppe MAE:   {g6_mae:.2f} (erwartet: ~0)")
    print(f"    KI-Elite MAE:         {real_mae:.2f} (dokumentierter Gap)")
    print(f"    Faktor:               {real_mae/g6_mae:.1f}x")
    print()

    if g6_mae <= 1.0:
        print("  BEFUND: Kontrollgruppe zeigt KEINEN systematischen Say-Do-Gap.")
        print("  -> Der in der KI-Elite beobachtete Gap ist NICHT ein LLM-Artefakt.")
    else:
        print("  BEFUND: Kontrollgruppe zeigt einen kleinen Gap.")
        print(f"  -> {g6_mae:.2f} vs. {real_mae:.2f}: KI-Elite-Gap ist {real_mae/g6_mae:.1f}x größer.")

    # ============================================================
    # INTERPRETATION
    # ============================================================
    print()
    print("=" * 90)
    print("  INTERPRETATION")
    print("=" * 90)
    print()

    if overall_r >= 0.85:
        r_interp = "EXZELLENT"
    elif overall_r >= 0.70:
        r_interp = "GUT"
    elif overall_r >= 0.50:
        r_interp = "AKZEPTABEL"
    else:
        r_interp = "SCHWACH"

    if overall_icc >= 0.75:
        icc_interp = "GUT (>0.75)"
    elif overall_icc >= 0.60:
        icc_interp = "AKZEPTABEL (>0.60)"
    else:
        icc_interp = "UNGENÜGEND (<0.60)"

    print(f"  Run-Konvergenz: r={overall_r:.3f} ({r_interp}), ICC={overall_icc:.3f} ({icc_interp})")
    print(f"  Mittlere Abweichung: MAE={overall_mae:.2f} (auf 10-Punkte-Skala)")
    print()
    print("  Das Messinstrument Claude Opus 4.6 liefert bei wiederholter Anwendung")
    print(f"  auf identische Daten {r_interp.lower()}e Konvergenz.")
    print(f"  Die mittlere Abweichung von {overall_mae:.2f} Punkten auf einer 10-Punkte-Skala")
    print(f"  entspricht einer Messgenauigkeit von ±{overall_mae/2:.1f} Skalenpunkte.")

    # Save JSON
    output_dir = os.path.dirname(os.path.abspath(__file__))
    save_data = {
        "analysis": "G1 Run-Konvergenz + G6 Expected-Discrepancy",
        "date": "2026-03-30",
        "model": "Claude Opus 4.6",
        "g1": {
            "overall_pearson_r": round(overall_r, 4),
            "overall_mae": round(overall_mae, 3),
            "mean_icc": round(overall_icc, 4),
            "groups": {gid: {
                "run1": data["run1"],
                "run2": data["run2"],
                "original": data["original"],
                "icc": round(icc_two_way(data["run1"], data["run2"]), 4),
                "r_run1_run2": round(pearson_r(data["run1"], data["run2"]), 4),
                "mae_run1_run2": round(mae(data["run1"], data["run2"]), 3),
            } for gid, data in RESULTS.items()},
        },
        "g6": {
            "aussagen": G6_RESULTS["aussagen"],
            "handlungen": G6_RESULTS["handlungen"],
            "mae": round(g6_mae, 3),
            "pearson_r": round(g6_r, 4),
            "mean_delta": round(g6_mean_delta, 3),
        },
    }
    json_path = os.path.join(output_dir, "g1_g6_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=2, ensure_ascii=False)
    print(f"\n  JSON gespeichert: {json_path}")


if __name__ == "__main__":
    main()
