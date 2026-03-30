#!/usr/bin/env python3
"""
G8: Aggregation vs. Direct Group Synthesis Comparison
=====================================================
Compares individual-profile-aggregated D01-D12 ratings with
direct group synthesis ratings for each sociological group.

This is the core validation step: Do pooled raw data → group synthesis
yield the same worldview as averaging individual profiles?

Author: Claude Opus 4.6
Date: 2026-03-30
"""

import json
import math
import os

# ============================================================
# DATA: Individual ratings (from rating_GESAMT_D01-D12.md)
# P1-P100, D01-D12
# ============================================================

INDIVIDUAL_RATINGS = {
    1:  [7, 8, 7, 7, 9, 9, 4, 9, 4, 6, 7, 8],
    2:  [8, 7, 7, 8, 8, 8, 5, 9, 4, 6, 8, 7],
    3:  [9, 9, 6, 9, 9, 6, 6, 10, 5, 9, 3, 6],
    4:  [5, 7, 5, 7, 8, 8, 4, 8, 6, 5, 7, 7],
    5:  [7, 9, 6, 6, 9, 9, 6, 8, 4, 7, 6, 9],
    6:  [6, 8, 6, 6, 9, 9, 6, 7, 4, 8, 4, 9],
    7:  [6, 9, 7, 5, 9, 10, 7, 8, 3, 5, 4, 9],
    8:  [5, 7, 5, 7, 8, 7, 3, 6, 5, 5, 8, 7],
    9:  [7, 6, 7, 9, 7, 7, 4, 10, 6, 5, 7, 7],
    10: [6, 8, 5, 6, 7, 9, 5, 6, 6, 5, 5, 10],
    11: [7, 7, 7, 8, 8, 8, 5, 9, 7, 6, 5, 8],
    12: [8, 8, 6, 9, 8, 7, 5, 10, 5, 7, 6, 6],
    13: [5, 7, 6, 7, 7, 8, 4, 7, 6, 5, 7, 7],
    14: [4, 8, 6, 6, 7, 8, 5, 6, 6, 4, 6, 8],
    15: [5, 6, 7, 7, 6, 6, 4, 6, 7, 4, 7, 6],
    16: [10, 9, 5, 8, 9, 10, 7, 10, 3, 9, 5, 10],
    17: [6, 7, 7, 8, 7, 7, 4, 8, 6, 5, 7, 7],
    18: [7, 6, 7, 9, 7, 7, 4, 7, 6, 5, 9, 7],
    19: [5, 7, 6, 7, 8, 8, 5, 7, 5, 5, 6, 7],
    20: [6, 7, 7, 6, 7, 7, 3, 6, 5, 6, 7, 6],
    21: [6, 4, 6, 8, 8, 4, 4, 9, 5, 6, 6, 4],
    22: [5, 7, 5, 6, 7, 8, 4, 6, 5, 4, 8, 7],
    23: [8, 7, 6, 9, 8, 7, 5, 10, 4, 6, 7, 6],
    24: [8, 9, 7, 5, 9, 9, 3, 9, 3, 5, 2, 10],
    25: [7, 9, 7, 4, 8, 6, 3, 8, 3, 8, 2, 9],
    26: [6, 8, 6, 7, 8, 8, 5, 8, 4, 5, 6, 8],
    27: [5, 8, 6, 5, 7, 8, 4, 7, 4, 4, 5, 8],
    28: [7, 7, 6, 8, 8, 8, 5, 9, 4, 6, 6, 8],
    29: [8, 8, 7, 6, 9, 7, 4, 9, 3, 5, 3, 7],
    30: [4, 8, 6, 4, 9, 8, 5, 6, 3, 5, 4, 7],
    31: [6, 7, 7, 6, 8, 9, 4, 7, 5, 6, 7, 8],
    32: [7, 7, 6, 7, 9, 9, 5, 9, 4, 7, 8, 7],
    33: [6, 6, 5, 8, 7, 7, 3, 7, 6, 5, 8, 7],
    34: [6, 8, 5, 5, 9, 8, 5, 8, 5, 6, 5, 8],
    35: [7, 7, 5, 8, 7, 8, 4, 8, 5, 5, 7, 8],
    36: [7, 9, 8, 6, 8, 8, 7, 9, 4, 5, 3, 7],
    37: [7, 8, 7, 6, 8, 8, 6, 9, 4, 5, 4, 7],
    38: [5, 8, 6, 5, 8, 7, 6, 7, 5, 5, 4, 7],
    39: [8, 8, 6, 7, 9, 6, 7, 9, 4, 5, 2, 6],
    40: [5, 7, 5, 6, 8, 7, 4, 8, 6, 5, 6, 7],
    41: [6, 8, 6, 6, 8, 8, 5, 7, 5, 4, 6, 8],
    42: [7, 9, 6, 5, 9, 9, 4, 8, 4, 7, 8, 9],
    43: [7, 8, 5, 6, 7, 5, 7, 9, 4, 5, 3, 5],
    44: [6, 7, 7, 7, 8, 7, 5, 8, 6, 6, 5, 7],
    45: [6, 8, 7, 6, 9, 8, 5, 8, 5, 6, 5, 8],
    46: [6, 8, 7, 6, 8, 9, 6, 7, 5, 5, 5, 9],
    47: [5, 7, 6, 7, 7, 7, 6, 6, 6, 4, 6, 7],
    48: [8, 7, 6, 8, 6, 8, 3, 7, 6, 4, 9, 8],
    49: [7, 8, 7, 5, 8, 7, 5, 8, 4, 5, 4, 7],
    50: [8, 8, 7, 7, 7, 8, 3, 7, 5, 5, 7, 8],
    51: [6, 6, 7, 8, 7, 6, 4, 9, 5, 4, 7, 6],
    52: [7, 8, 6, 7, 9, 7, 5, 10, 4, 6, 6, 6],
    53: [6, 8, 5, 6, 9, 8, 5, 8, 4, 5, 6, 7],
    54: [5, 7, 6, 6, 6, 7, 4, 6, 6, 4, 6, 7],
    55: [7, 8, 6, 8, 8, 7, 4, 8, 5, 5, 8, 6],
    56: [6, 7, 6, 6, 7, 7, 5, 8, 6, 5, 6, 7],
    57: [8, 6, 7, 9, 6, 5, 3, 10, 8, 3, 7, 5],
    58: [5, 7, 6, 6, 7, 8, 5, 6, 5, 6, 6, 8],
    59: [5, 6, 7, 7, 5, 6, 4, 5, 7, 3, 7, 6],
    60: [6, 7, 7, 7, 5, 4, 4, 6, 8, 2, 8, 5],
    61: [5, 7, 6, 7, 8, 7, 4, 7, 5, 5, 7, 7],
    62: [6, 6, 7, 8, 8, 5, 4, 9, 5, 4, 6, 5],
    63: [7, 8, 7, 5, 8, 8, 6, 9, 4, 6, 4, 7],
    64: [5, 8, 5, 6, 7, 7, 5, 8, 4, 4, 3, 6],
    65: [6, 7, 6, 6, 8, 8, 4, 7, 4, 6, 5, 8],
    66: [7, 7, 6, 7, 7, 7, 2, 9, 5, 5, 8, 6],
    67: [5, 7, 7, 6, 8, 7, 4, 8, 5, 5, 5, 6],
    68: [6, 7, 6, 5, 8, 6, 4, 8, 5, 6, 4, 7],
    69: [4, 6, 6, 6, 7, 7, 4, 6, 6, 5, 6, 6],
    70: [6, 8, 6, 5, 8, 9, 4, 9, 4, 5, 5, 8],
    71: [6, 8, 6, 6, 7, 8, 5, 8, 5, 5, 6, 8],
    72: [7, 8, 5, 6, 9, 6, 4, 7, 5, 6, 5, 6],
    73: [6, 6, 7, 9, 7, 7, 4, 9, 6, 5, 7, 7],
    74: [7, 8, 6, 5, 8, 8, 5, 9, 4, 6, 4, 8],
    75: [7, 8, 6, 5, 8, 8, 5, 9, 4, 6, 4, 8],
    76: [7, 8, 6, 6, 8, 7, 5, 9, 5, 6, 6, 7],
    77: [5, 7, 5, 4, 7, 8, 4, 7, 4, 4, 5, 7],
    78: [5, 8, 5, 4, 8, 7, 4, 8, 4, 5, 5, 7],
    79: [5, 7, 5, 5, 8, 7, 4, 7, 5, 5, 6, 7],
    80: [7, 7, 6, 7, 8, 7, 5, 8, 6, 5, 8, 7],
    81: [6, 7, 6, 6, 8, 8, 4, 7, 5, 6, 7, 8],
    82: [5, 8, 6, 6, 8, 7, 3, 8, 5, 5, 4, 7],
    83: [6, 7, 6, 7, 7, 8, 5, 7, 6, 5, 7, 8],
    84: [5, 8, 5, 6, 8, 8, 5, 7, 5, 5, 5, 9],
    85: [8, 9, 6, 7, 9, 9, 6, 9, 4, 8, 4, 9],
    86: [6, 7, 7, 8, 6, 7, 5, 8, 6, 4, 8, 7],
    87: [6, 8, 7, 5, 7, 8, 4, 9, 5, 5, 3, 8],
    88: [7, 9, 7, 8, 8, 8, 5, 10, 5, 7, 6, 8],
    89: [6, 8, 6, 7, 8, 8, 5, 10, 5, 6, 6, 8],
    90: [6, 8, 6, 7, 9, 8, 5, 8, 5, 7, 5, 8],
    91: [4, 7, 5, 6, 8, 8, 4, 8, 4, 6, 5, 8],
    92: [6, 7, 6, 7, 8, 8, 3, 8, 5, 6, 8, 8],
    93: [5, 8, 5, 5, 7, 9, 5, 6, 5, 5, 6, 8],
    94: [5, 7, 6, 5, 7, 6, 6, 7, 6, 4, 4, 6],
    95: [8, 7, 5, 8, 8, 7, 2, 10, 5, 7, 9, 7],
    96: [6, 8, 6, 6, 7, 7, 5, 7, 7, 5, 5, 8],
    97: [5, 7, 5, 7, 7, 8, 4, 8, 6, 5, 6, 8],
    98: [7, 7, 6, 8, 7, 6, 5, 8, 6, 5, 3, 7],
    99: [5, 6, 6, 7, 7, 7, 4, 6, 7, 4, 7, 7],
    100:[6, 8, 7, 6, 8, 8, 5, 9, 4, 4, 3, 8],
}

# ============================================================
# GROUP DEFINITIONS (from generate_topf.py)
# ============================================================

GRUPPEN = {
    "GR_ceo_AH": [1, 2, 3, 4, 5, 7, 9, 11, 13, 14, 15, 16, 23, 38, 39, 46, 64, 84, 94],
    "GR_akad_AH": [18, 20, 21, 22, 57, 58, 59, 60, 61, 62, 83, 99],
    "GR_inv_AH": [24, 25, 31, 32, 49, 50, 82, 87],
    "GR_gru_AH": [6, 8, 10, 12, 17, 26, 27, 28, 29, 30, 33, 34, 35, 40, 41, 42, 43, 48,
                   51, 52, 53, 54, 55, 63, 65, 66, 67, 68, 69, 72, 80, 85, 86, 90, 95, 96],
    "GF_anthropic_AH": [9, 17, 51, 52, 53, 54, 55, 56, 73],
    "GF_openai_AH": [2, 28, 44, 45, 81, 91, 67],
    "GF_google_AH": [4, 6, 8, 11, 19, 30, 77],
    "GH_open_AH": [5, 20, 48, 66, 92, 95],
    "GH_closed_AH": [2, 4, 9, 11, 13],
    "GH_risk_AH": [3, 12, 21, 57, 62, 73],
    "GH_speed_AH": [1, 2, 3, 16, 24, 32, 43],
    "GH_regpro_AH": [9, 17, 21, 23, 57, 62, 73, 86],
    "GH_regcon_AH": [20, 22, 24, 32, 49],
    "GD_frauen_AH": [14, 17, 18, 26, 69, 80, 83, 86, 87, 99],
    "GD_maenner_AH": [],  # will be computed
}

# Compute Maenner = all minus Frauen
all_ids = set(range(1, 101))
GRUPPEN["GD_maenner_AH"] = sorted(all_ids - set(GRUPPEN["GD_frauen_AH"]))

# ============================================================
# DIRECT GROUP SYNTHESIS RATINGS (from rating_gruppen_D01-D12.md)
# ============================================================

DIRECT_RATINGS = {
    "GR_ceo_AH":      [9, 9, 10, 8, 9, 8, 9, 9, 4, 7, 3, 8],
    "GR_akad_AH":      [6, 7, 8, 8, 6, 6, 5, 7, 6, 4, 7, 6],
    "GR_inv_AH":       [9, 10, 9, 4, 10, 9, 10, 10, 3, 9, 2, 9],
    "GR_gru_AH":       [7, 8, 9, 9, 8, 8, 7, 9, 5, 6, 5, 8],
    "GF_anthropic_AH": [8, 7, 8, 9, 7, 7, 5, 9, 6, 5, 6, 6],
    "GF_openai_AH":    [9, 8, 8, 7, 9, 9, 6, 8, 4, 6, 5, 9],
    "GF_google_AH":    [10, 9, 9, 8, 8, 10, 7, 7, 5, 7, 4, 10],
    "GH_open_AH":      [8, 7, 5, 7, 6, 8, 3, 9, 6, 5, 8, 9],
    "GH_closed_AH":    [7, 6, 7, 9, 5, 7, 6, 8, 5, 4, 6, 6],
    "GH_risk_AH":      [9, 4, 6, 10, 4, 5, 5, 10, 4, 3, 7, 4],
    "GH_speed_AH":     [9, 9, 8, 6, 8, 10, 7, 10, 3, 8, 4, 9],
    "GH_regpro_AH":    [8, 5, 6, 9, 4, 6, 4, 9, 6, 4, 8, 7],
    "GH_regcon_AH":    [8, 8, 7, 5, 7, 9, 2, 7, 7, 6, 7, 9],
    "GD_frauen_AH":    [6, 7, 9, 9, 6, 7, 6, 6, 7, 5, 8, 7],
    "GD_maenner_AH":   [10, 10, 10, 7, 10, 9, 9, 10, 3, 8, 2, 9],
}

DIM_NAMES = ["D01", "D02", "D03", "D04", "D05", "D06",
             "D07", "D08", "D09", "D10", "D11", "D12"]
DIM_LABELS = [
    "Sendungsbew.", "Selbstwirks.", "Arbeitsethik", "Verantwort.",
    "Techno-Det.", "Fortschr.opt.", "Machtkonz.", "Dringlichk.",
    "Menschl.Wert", "Posthuman.", "Egalitarism.", "Kontrollüberz."
]

GROUP_LABELS = {
    "GR_ceo_AH": "CEOs",
    "GR_akad_AH": "Akademiker",
    "GR_inv_AH": "Investoren",
    "GR_gru_AH": "Gründer",
    "GF_anthropic_AH": "Anthropic",
    "GF_openai_AH": "OpenAI",
    "GF_google_AH": "Google/DM",
    "GH_open_AH": "Open Source",
    "GH_closed_AH": "Closed Source",
    "GH_risk_AH": "Risiko-Warner",
    "GH_speed_AH": "Beschleuniger",
    "GH_regpro_AH": "Reg-Pro",
    "GH_regcon_AH": "Reg-Contra",
    "GD_frauen_AH": "Frauen",
    "GD_maenner_AH": "Männer",
}


def compute_group_mean(group_ids):
    """Compute mean D01-D12 from individual ratings."""
    n = len(group_ids)
    if n == 0:
        return [0.0] * 12
    sums = [0.0] * 12
    for pid in group_ids:
        ratings = INDIVIDUAL_RATINGS[pid]
        for i in range(12):
            sums[i] += ratings[i]
    return [s / n for s in sums]


def compute_group_sd(group_ids, means):
    """Compute SD for each dimension."""
    n = len(group_ids)
    if n < 2:
        return [0.0] * 12
    var = [0.0] * 12
    for pid in group_ids:
        ratings = INDIVIDUAL_RATINGS[pid]
        for i in range(12):
            var[i] += (ratings[i] - means[i]) ** 2
    return [math.sqrt(v / (n - 1)) for v in var]


def pearson_r(x, y):
    """Pearson correlation."""
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    sx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    sy = math.sqrt(sum((yi - my) ** 2 for yi in y))
    if sx == 0 or sy == 0:
        return 0.0
    return cov / (sx * sy)


def mae(x, y):
    """Mean Absolute Error."""
    return sum(abs(x[i] - y[i]) for i in range(len(x))) / len(x)


def rmse(x, y):
    """Root Mean Squared Error."""
    mse = sum((x[i] - y[i]) ** 2 for i in range(len(x))) / len(x)
    return math.sqrt(mse)


def max_abs_diff(x, y):
    """Maximum absolute difference."""
    return max(abs(x[i] - y[i]) for i in range(len(x)))


def main():
    results = {}

    print("=" * 100)
    print("  G8: AGGREGIERTE EINZELPROFILE vs. DIREKTE GRUPPENSYNTHESE")
    print("  Vergleich der D01-D12 Ratings (15 Gruppen)")
    print("=" * 100)
    print()

    # Header
    print(f"{'Gruppe':<16} | {'n':>3} | {'Methode':<10} | ", end="")
    for d in DIM_NAMES:
        print(f"{d:>5}", end=" ")
    print(f"| {'Avg':>5}")
    print("-" * 120)

    all_agg = []
    all_dir = []
    group_metrics = []

    for group_id in DIRECT_RATINGS:
        members = GRUPPEN[group_id]
        n = len(members)

        # Aggregated individual means
        agg_means = compute_group_mean(members)
        agg_sd = compute_group_sd(members, agg_means)

        # Direct synthesis ratings
        dir_ratings = DIRECT_RATINGS[group_id]

        # Compute deltas
        deltas = [dir_ratings[i] - agg_means[i] for i in range(12)]

        label = GROUP_LABELS[group_id]

        # Print aggregated
        agg_avg = sum(agg_means) / 12
        print(f"{label:<16} | {n:>3} | {'Aggreg.':<10} | ", end="")
        for v in agg_means:
            print(f"{v:>5.1f}", end=" ")
        print(f"| {agg_avg:>5.1f}")

        # Print direct
        dir_avg = sum(dir_ratings) / 12
        print(f"{'':>16} |     | {'Direkt':<10} | ", end="")
        for v in dir_ratings:
            print(f"{v:>5.0f}", end=" ")
        print(f"| {dir_avg:>5.1f}")

        # Print delta
        print(f"{'':>16} |     | {'Delta':<10} | ", end="")
        for d in deltas:
            sign = "+" if d >= 0 else ""
            print(f"{sign}{d:>4.1f}", end=" ")
        delta_avg = dir_avg - agg_avg
        sign = "+" if delta_avg >= 0 else ""
        print(f"| {sign}{delta_avg:>4.1f}")
        print("-" * 120)

        # Metrics
        r = pearson_r(agg_means, [float(x) for x in dir_ratings])
        m = mae(agg_means, [float(x) for x in dir_ratings])
        rm = rmse(agg_means, [float(x) for x in dir_ratings])
        md = max_abs_diff(agg_means, [float(x) for x in dir_ratings])

        group_metrics.append({
            "group": label,
            "group_id": group_id,
            "n": n,
            "pearson_r": r,
            "mae": m,
            "rmse": rm,
            "max_diff": md,
            "agg_avg": agg_avg,
            "dir_avg": dir_avg,
            "agg_means": agg_means,
            "dir_ratings": dir_ratings,
            "deltas": deltas,
        })

        all_agg.extend(agg_means)
        all_dir.extend([float(x) for x in dir_ratings])

        results[group_id] = {
            "aggregated": [round(v, 2) for v in agg_means],
            "direct": dir_ratings,
            "deltas": [round(d, 2) for d in deltas],
            "sd": [round(s, 2) for s in agg_sd],
            "n": n,
            "pearson_r": round(r, 3),
            "mae": round(m, 2),
            "rmse": round(rm, 2),
        }

    # ============================================================
    # SUMMARY METRICS
    # ============================================================
    print()
    print("=" * 100)
    print("  KONVERGENZ-METRIKEN")
    print("=" * 100)
    print()

    print(f"{'Gruppe':<16} | {'n':>3} | {'Pearson r':>10} | {'MAE':>6} | {'RMSE':>6} | {'Max Diff':>9} | {'Bewertung':<15}")
    print("-" * 85)

    for gm in group_metrics:
        if gm["pearson_r"] >= 0.7 and gm["mae"] <= 1.5:
            rating = "GUT"
        elif gm["pearson_r"] >= 0.5 and gm["mae"] <= 2.0:
            rating = "AKZEPTABEL"
        elif gm["pearson_r"] >= 0.3:
            rating = "SCHWACH"
        else:
            rating = "DIVERGENT"

        print(f"{gm['group']:<16} | {gm['n']:>3} | {gm['pearson_r']:>10.3f} | {gm['mae']:>6.2f} | {gm['rmse']:>6.2f} | {gm['max_diff']:>9.1f} | {rating:<15}")

    # Overall
    overall_r = pearson_r(all_agg, all_dir)
    overall_mae = mae(all_agg, all_dir)
    overall_rmse = rmse(all_agg, all_dir)

    print("-" * 85)
    print(f"{'GESAMT':<16} | {'':>3} | {overall_r:>10.3f} | {overall_mae:>6.2f} | {overall_rmse:>6.2f} | {'':>9} |")

    # ============================================================
    # DIMENSION-WISE ANALYSIS
    # ============================================================
    print()
    print("=" * 100)
    print("  DIMENSIONS-ANALYSE: Systematische Verzerrungen")
    print("=" * 100)
    print()

    print(f"{'Dimension':<15} | {'Avg Delta':>10} | {'Richtung':<15} | {'Interpretation':<40}")
    print("-" * 90)

    for i in range(12):
        dim_deltas = [gm["deltas"][i] for gm in group_metrics]
        avg_delta = sum(dim_deltas) / len(dim_deltas)

        if avg_delta > 0.5:
            direction = "Direkt HÖHER"
            interp = "Gruppensynthese überzeichnet"
        elif avg_delta < -0.5:
            direction = "Direkt TIEFER"
            interp = "Gruppensynthese dämpft"
        else:
            direction = "~Gleich"
            interp = "Konvergenz"

        print(f"{DIM_NAMES[i]} {DIM_LABELS[i]:<12} | {avg_delta:>+10.2f} | {direction:<15} | {interp:<40}")

    # ============================================================
    # AMPLIFICATION ANALYSIS
    # ============================================================
    print()
    print("=" * 100)
    print("  AMPLIFIKATIONS-ANALYSE: Extremisiert die direkte Synthese?")
    print("=" * 100)
    print()

    amplified = 0
    dampened = 0
    total_dims = 0

    for gm in group_metrics:
        for i in range(12):
            agg_val = gm["agg_means"][i]
            dir_val = gm["dir_ratings"][i]
            midpoint = 5.5

            total_dims += 1

            # Is the direct rating further from midpoint than aggregated?
            if abs(dir_val - midpoint) > abs(agg_val - midpoint):
                amplified += 1
            elif abs(dir_val - midpoint) < abs(agg_val - midpoint):
                dampened += 1

    print(f"Amplifikation (direktes Rating weiter vom Mittelpunkt als aggregiertes):")
    print(f"  Verstärkt:  {amplified}/{total_dims} ({amplified/total_dims*100:.1f}%)")
    print(f"  Gedämpft:   {dampened}/{total_dims} ({dampened/total_dims*100:.1f}%)")
    print(f"  Gleich:     {total_dims - amplified - dampened}/{total_dims}")
    print()

    if amplified > dampened:
        print("-> BEFUND: Direkte Gruppensynthese VERSTÄRKT tendenziell.")
        print("   Die Gruppenperspektive ist extremer als der Durchschnitt der Einzelprofile.")
        print("   Dies ist erwartbar: Gruppen-Kohärenz erzeugt schärfere Konturen.")
    else:
        print("-> BEFUND: Kein systematischer Amplifikationseffekt.")

    # ============================================================
    # SAVE RESULTS
    # ============================================================
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # JSON for further analysis
    json_path = os.path.join(output_dir, "g8_comparison_results.json")
    save_data = {
        "analysis": "G8 Aggregation vs Direct Group Synthesis",
        "date": "2026-03-30",
        "overall_pearson_r": round(overall_r, 4),
        "overall_mae": round(overall_mae, 3),
        "overall_rmse": round(overall_rmse, 3),
        "groups": results,
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=2, ensure_ascii=False)
    print(f"\nJSON gespeichert: {json_path}")

    return save_data


if __name__ == "__main__":
    main()
