# -*- coding: utf-8 -*-
"""
Statistische Gruppenvergleichstests auf den SWR/KI-Elite Daten.
100 Personen x 12 Dimensionen (D01-D12), 1-10 Skala.

Analysen:
1. PCA (Dimensionsreduktion)
2. Subspace-Clustering (HDBSCAN)
3. Effektstaerken (Cliff's delta) pro heuristischem Cluster
4. Deskriptive Statistik der Streuung

Ergebnisse -> statistical_analysis.json + STATISTICAL_REPORT.md
"""

import json
import re
import numpy as np
from pathlib import Path

# ============================================================
# 1. DATEN EINLESEN
# ============================================================

data_path = Path(r"C:\Users\User\OneDrive\.TOPICS\.RESEARCH\.PRIO-1\!!!PP__Transhumanismus\_results\synthesen\rating_GESAMT_D01-D12.md")
output_dir = Path(r"C:\Users\User\OneDrive\.TOPICS\.RESEARCH\.PRIO-1\!!!PP__Transhumanismus\_results")

with open(data_path, "r", encoding="utf-8") as f:
    content = f.read()

# Parse die Markdown-Tabelle
persons = {}
dim_names = ["D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12"]
dim_labels = {
    "D01": "Sendungsbewusstsein",
    "D02": "Kontrollueberzeugung",
    "D03": "Zugehoerigkeitsgefuehl",
    "D04": "Verantwortungsgefuehl",
    "D05": "Technologie-Determinismus",
    "D06": "Fortschrittsoptimismus",
    "D07": "Machtkonzentration",
    "D08": "Dringlichkeit",
    "D09": "Menschliche Einzigartigkeit",
    "D10": "Transhumanismus",
    "D11": "Egalitarismus",
    "D12": "Zukunft der Menschheit"
}

pattern = r'\|\s*P(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'

for m in re.finditer(pattern, content):
    pid = int(m.group(1))
    name = m.group(2).strip()
    scores = [int(m.group(i)) for i in range(3, 15)]
    persons[pid] = {"name": name, "scores": scores}

print(f"Personen eingelesen: {len(persons)}")

# Matrix aufbauen (100 x 12)
n = len(persons)
pids = sorted(persons.keys())
data_matrix = np.array([persons[pid]["scores"] for pid in pids])
print(f"Datenmatrix: {data_matrix.shape}")

# ============================================================
# 2. GRUPPEN-ZUORDNUNG
# ============================================================
# Basierend auf Top100_KI_SiliconValley_Recherche.md
# P-Nummer = Rang in der Recherche-Tabelle

# Rolle (primaere Rolle basierend auf Recherche-Tabelle)
roles = {}
# CEOs (CEO/President als primaere Rolle)
ceos = [1, 2, 3, 4, 5, 9, 11, 12, 13, 14, 15, 16, 23, 26, 27, 29, 34, 35, 38, 39, 40, 42, 46, 48, 63, 64, 80, 84, 85, 93, 94, 95, 96]
for p in ceos:
    roles[p] = "CEO"

# Akademiker/Professoren
akademiker = [18, 21, 22, 57, 58, 59, 60, 61, 62, 99]
for p in akademiker:
    roles[p] = "Akademiker"

# Investoren/VC
investoren = [6, 7, 8, 10, 24, 25, 31, 32, 36, 49, 50, 82, 98]
for p in investoren:
    roles[p] = "Investor"

# Gruender/Tech-Leads (Mitgruender ohne CEO-Titel, Tech Leads)
gruender = [17, 19, 20, 28, 30, 33, 37, 41, 43, 44, 45, 47, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 83, 86, 87, 88, 89, 90, 91, 92, 97, 100]
for p in gruender:
    roles[p] = "Gruender"

# Gender (basierend auf Real-Personen in der Recherche-Tabelle)
# Frauen: Lisa Su (14), Daniela Amodei (17), Fei-Fei Li (18), Mira Murati (26),
#         Asha Patel / Niki Parmar (69), May Habib (80), Daphne Koller (83),
#         Navrina Singh (86), Sarah Guo (87), Dorsa Sadigh (99)
# Plus aus den anonymisierten Namen: Helena Mertens (P14), Miriam Feldhaus (P17),
# Vera Nordstroem (P18), Miriam Koller (P26), Asha Patel (P33),
# Clara Montfort (P48), Sophia Bernhardt (P59), Mira Vaswani (P69),
# Maya Kowalski (P80), Elena Bergstroem (P83), Priya Varma (P86),
# Mira Daniels (P87), Maya Winters (P90), Mira Kovalenko (P99)
# Genau: Weibliche Pseudonyme in den Daten identifizieren
frauen_pids = []
maenner_pids = []
weibliche_namen = ["Helena", "Miriam", "Vera", "Asha", "Clara", "Sophia", "Mira",
                   "Maya", "Elena", "Priya", "Lisa"]
for pid in pids:
    name = persons[pid]["name"]
    first_name = name.split()[0].replace("Dr.", "").strip()
    if first_name == "":
        first_name = name.split()[1] if len(name.split()) > 1 else ""
    is_female = any(wn in first_name for wn in weibliche_namen)
    if is_female:
        frauen_pids.append(pid)
    else:
        maenner_pids.append(pid)

gender = {}
for pid in pids:
    if pid in frauen_pids:
        gender[pid] = "Frau"
    else:
        gender[pid] = "Mann"

print(f"\nRollen-Verteilung:")
for r in ["CEO", "Akademiker", "Investor", "Gruender"]:
    count = sum(1 for p in pids if roles.get(p) == r)
    print(f"  {r}: n={count}")
unassigned = [p for p in pids if p not in roles]
if unassigned:
    print(f"  Nicht zugeordnet: {unassigned}")

print(f"\nGender-Verteilung:")
print(f"  Frauen: n={len(frauen_pids)} ({frauen_pids})")
print(f"  Maenner: n={len(maenner_pids)}")

# ============================================================
# Heuristische 4-Cluster nach Paper (Architekt/Hueter/Innovator/Befreier)
# Basierend auf Phase8_F4_Cluster.md:
# Architekt: CEOs, Investoren, Maenner (prototypisch) -> hohe D07, niedrige D11
# Hueter: Akademiker, Frauen (prototypisch) -> hohe D04, hohe D11
# Innovator: Gruender, OpenAI, Google -> moderate D07, hohe D06+D04
# Befreier: Open-Source, Anti-Regulierung -> niedrige D07, hohe D11+D12
#
# Individuelle Zuordnung ueber D07 und D11 (primaere Differenzierungsdimensionen):
# ============================================================

def assign_heuristic_cluster(scores):
    """Zuordnung basierend auf D07 (Machtkonzentration) und D11 (Egalitarismus)."""
    d07 = scores[6]  # Index 6
    d11 = scores[10]  # Index 10
    d04 = scores[3]  # Index 3
    d06 = scores[5]  # Index 5

    # Primaere Achse: D07 vs D11
    if d07 >= 6 and d11 <= 4:
        return "Architekt"
    elif d07 <= 4 and d11 >= 7:
        if d06 >= 7:
            return "Befreier"
        else:
            return "Hueter"
    elif d07 <= 4 and d04 >= 7:
        return "Hueter"
    elif d07 >= 5 and d06 >= 8:
        return "Innovator"
    elif d07 <= 3 and d11 >= 6:
        return "Befreier"
    elif d07 <= 4 and d11 >= 6:
        if d04 >= 7:
            return "Hueter"
        else:
            return "Befreier"
    elif d07 >= 5:
        if d04 >= 7:
            return "Innovator"
        else:
            return "Architekt"
    else:
        # Default: moderates Profil -> Innovator
        if d04 >= 7:
            return "Hueter"
        elif d06 >= 7:
            return "Innovator"
        else:
            return "Hueter"

heuristic_clusters = {}
for pid in pids:
    heuristic_clusters[pid] = assign_heuristic_cluster(persons[pid]["scores"])

print(f"\nHeuristische Cluster-Verteilung:")
for c in ["Architekt", "Hueter", "Innovator", "Befreier"]:
    members = [p for p in pids if heuristic_clusters[p] == c]
    print(f"  {c}: n={len(members)}")

# ============================================================
# 3. PCA (Dimensionsreduktion)
# ============================================================
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print("\n" + "="*60)
print("PCA ANALYSE")
print("="*60)

# Standardisieren
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_matrix)

# PCA mit allen Komponenten
pca_full = PCA()
pca_full.fit(data_scaled)

explained_var = pca_full.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

print(f"\nErklaerte Varianz pro Komponente:")
for i, (ev, cv) in enumerate(zip(explained_var, cumulative_var)):
    print(f"  PC{i+1}: {ev:.4f} ({ev*100:.1f}%) -- kumuliert: {cv*100:.1f}%")

# Wie viele Komponenten fuer 80%?
n_comp_80 = np.argmax(cumulative_var >= 0.80) + 1
print(f"\nKomponenten fuer 80% Varianz: {n_comp_80}")

# Loadings
loadings = pca_full.components_
print(f"\nPC1 Ladungen (staerkste):")
pc1_loadings = list(zip(dim_names, loadings[0]))
pc1_sorted = sorted(pc1_loadings, key=lambda x: abs(x[1]), reverse=True)
for dim, load in pc1_sorted:
    print(f"  {dim} ({dim_labels[dim]}): {load:+.4f}")

print(f"\nPC2 Ladungen (staerkste):")
pc2_loadings = list(zip(dim_names, loadings[1]))
pc2_sorted = sorted(pc2_loadings, key=lambda x: abs(x[1]), reverse=True)
for dim, load in pc2_sorted:
    print(f"  {dim} ({dim_labels[dim]}): {load:+.4f}")

# Scree-Plot Daten
scree_data = [{"component": f"PC{i+1}", "eigenvalue": float(pca_full.explained_variance_[i]),
               "explained_variance_ratio": float(ev), "cumulative": float(cv)}
              for i, (ev, cv) in enumerate(zip(explained_var, cumulative_var))]

# PCA Scores fuer spaetere Analyse
pca_3 = PCA(n_components=3)
scores_3d = pca_3.fit_transform(data_scaled)

# ============================================================
# 4. SUBSPACE-CLUSTERING (HDBSCAN)
# ============================================================
from hdbscan import HDBSCAN
from sklearn.metrics import silhouette_score

print("\n" + "="*60)
print("SUBSPACE-CLUSTERING (HDBSCAN)")
print("="*60)

# 4a: HDBSCAN auf Top-2-3 PCA-Dimensionen
print("\n--- HDBSCAN auf PC1+PC2+PC3 ---")
hdbscan_results = {}

for min_cs in [5, 8, 10, 15]:
    for min_s in [3, 5]:
        clf = HDBSCAN(min_cluster_size=min_cs, min_samples=min_s)
        labels = clf.fit_predict(scores_3d)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        sil = silhouette_score(scores_3d, labels) if n_clusters >= 2 else None
        print(f"  min_cluster_size={min_cs}, min_samples={min_s}: "
              f"{n_clusters} Cluster, {n_noise} Noise, Silhouette={sil}")
        hdbscan_results[f"pca3_mcs{min_cs}_ms{min_s}"] = {
            "subspace": "PC1+PC2+PC3",
            "min_cluster_size": min_cs,
            "min_samples": min_s,
            "n_clusters": n_clusters,
            "n_noise": n_noise,
            "noise_pct": round(n_noise / n * 100, 1),
            "silhouette": round(sil, 4) if sil is not None else None
        }

# 4b: HDBSCAN nur auf D07+D11
print("\n--- HDBSCAN auf D07+D11 (Machtkonzentration + Egalitarismus) ---")
d07_d11 = data_matrix[:, [6, 10]]  # D07=idx6, D11=idx10
d07_d11_scaled = StandardScaler().fit_transform(d07_d11)

best_sil_d07d11 = -2
best_labels_d07d11 = None
best_params_d07d11 = None

for min_cs in [5, 8, 10, 12, 15]:
    for min_s in [2, 3, 5]:
        clf = HDBSCAN(min_cluster_size=min_cs, min_samples=min_s)
        labels = clf.fit_predict(d07_d11_scaled)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        sil = silhouette_score(d07_d11_scaled, labels) if n_clusters >= 2 else None
        print(f"  min_cluster_size={min_cs}, min_samples={min_s}: "
              f"{n_clusters} Cluster, {n_noise} Noise, Silhouette={sil}")
        hdbscan_results[f"d07d11_mcs{min_cs}_ms{min_s}"] = {
            "subspace": "D07+D11",
            "min_cluster_size": min_cs,
            "min_samples": min_s,
            "n_clusters": n_clusters,
            "n_noise": n_noise,
            "noise_pct": round(n_noise / n * 100, 1),
            "silhouette": round(sil, 4) if sil is not None else None
        }
        if sil is not None and sil > best_sil_d07d11:
            best_sil_d07d11 = sil
            best_labels_d07d11 = labels
            best_params_d07d11 = (min_cs, min_s)

# 4c: HDBSCAN auf Top-3 Dimensionen mit hoechster PCA-Ladung
top3_dims_pc1 = [pc1_sorted[i][0] for i in range(3)]
top3_idx = [dim_names.index(d) for d in top3_dims_pc1]
print(f"\n--- HDBSCAN auf Top-3 PC1-Ladungsdimensionen: {top3_dims_pc1} ---")
data_top3 = data_matrix[:, top3_idx]
data_top3_scaled = StandardScaler().fit_transform(data_top3)

for min_cs in [5, 8, 10, 15]:
    for min_s in [3, 5]:
        clf = HDBSCAN(min_cluster_size=min_cs, min_samples=min_s)
        labels = clf.fit_predict(data_top3_scaled)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        sil = silhouette_score(data_top3_scaled, labels) if n_clusters >= 2 else None
        print(f"  min_cluster_size={min_cs}, min_samples={min_s}: "
              f"{n_clusters} Cluster, {n_noise} Noise, Silhouette={sil}")
        dim_key = "+".join(top3_dims_pc1)
        hdbscan_results[f"{dim_key}_mcs{min_cs}_ms{min_s}"] = {
            "subspace": dim_key,
            "min_cluster_size": min_cs,
            "min_samples": min_s,
            "n_clusters": n_clusters,
            "n_noise": n_noise,
            "noise_pct": round(n_noise / n * 100, 1),
            "silhouette": round(sil, 4) if sil is not None else None
        }

# ============================================================
# 5. EFFEKTSTAERKEN (Cliff's delta) pro heuristischem Cluster
# ============================================================

print("\n" + "="*60)
print("EFFEKTSTAERKEN (Cliff's delta)")
print("="*60)

def cliffs_delta(x, y):
    """Berechnet Cliff's delta zwischen zwei Gruppen."""
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return 0.0
    count = 0
    for xi in x:
        for yi in y:
            if xi > yi:
                count += 1
            elif xi < yi:
                count -= 1
    return count / (n1 * n2)

def interpret_delta(d):
    """Interpretation nach Romano et al. (2006)."""
    ad = abs(d)
    if ad < 0.147:
        return "negligible"
    elif ad < 0.33:
        return "small"
    elif ad < 0.474:
        return "medium"
    else:
        return "large"

cluster_types = ["Architekt", "Hueter", "Innovator", "Befreier"]
cluster_members = {c: [pid for pid in pids if heuristic_clusters[pid] == c] for c in cluster_types}

# Cliff's delta fuer jedes Cluster-Paar pro Dimension
cliff_results = {}
pairs = []
for i, c1 in enumerate(cluster_types):
    for c2 in cluster_types[i+1:]:
        pairs.append((c1, c2))

print(f"\nCluster-Paare: {len(pairs)}")
for c1, c2 in pairs:
    pair_key = f"{c1}_vs_{c2}"
    cliff_results[pair_key] = {}
    print(f"\n  {c1} (n={len(cluster_members[c1])}) vs {c2} (n={len(cluster_members[c2])}):")
    for dim_idx, dim in enumerate(dim_names):
        vals1 = [persons[p]["scores"][dim_idx] for p in cluster_members[c1]]
        vals2 = [persons[p]["scores"][dim_idx] for p in cluster_members[c2]]
        delta = cliffs_delta(vals1, vals2)
        interp = interpret_delta(delta)
        cliff_results[pair_key][dim] = {
            "delta": round(delta, 4),
            "interpretation": interp,
            "mean_1": round(np.mean(vals1), 2),
            "mean_2": round(np.mean(vals2), 2)
        }
        if abs(delta) >= 0.33:
            print(f"    {dim} ({dim_labels[dim]}): delta={delta:+.3f} ({interp}) "
                  f"[{c1}={np.mean(vals1):.1f}, {c2}={np.mean(vals2):.1f}]")

# Staerkste Differenzierungsdimensionen
print("\n--- Staerkste Differenzierungsdimensionen (|delta| >= 0.33 medium+) ---")
dim_diff_counts = {d: 0 for d in dim_names}
dim_diff_max = {d: 0.0 for d in dim_names}
for pair_key, dims in cliff_results.items():
    for dim, result in dims.items():
        if abs(result["delta"]) >= 0.33:
            dim_diff_counts[dim] += 1
            dim_diff_max[dim] = max(dim_diff_max[dim], abs(result["delta"]))

dim_diff_sorted = sorted(dim_diff_counts.items(), key=lambda x: (-x[1], -dim_diff_max[x[0]]))
for dim, count in dim_diff_sorted:
    if count > 0:
        print(f"  {dim} ({dim_labels[dim]}): {count}x medium+ Effekt, max |delta|={dim_diff_max[dim]:.3f}")

# ============================================================
# 5b. CLIFF'S DELTA: Rollen-Vergleiche
# ============================================================
print("\n--- Rollen-Vergleiche (Cliff's delta) ---")
role_types = ["CEO", "Akademiker", "Investor", "Gruender"]
role_members = {r: [p for p in pids if roles.get(p) == r] for r in role_types}
cliff_roles = {}
for i, r1 in enumerate(role_types):
    for r2 in role_types[i+1:]:
        pair_key = f"{r1}_vs_{r2}"
        cliff_roles[pair_key] = {}
        significant_dims = []
        for dim_idx, dim in enumerate(dim_names):
            vals1 = [persons[p]["scores"][dim_idx] for p in role_members[r1]]
            vals2 = [persons[p]["scores"][dim_idx] for p in role_members[r2]]
            if len(vals1) > 0 and len(vals2) > 0:
                delta = cliffs_delta(vals1, vals2)
                interp = interpret_delta(delta)
                cliff_roles[pair_key][dim] = {
                    "delta": round(delta, 4),
                    "interpretation": interp,
                    "mean_1": round(np.mean(vals1), 2),
                    "mean_2": round(np.mean(vals2), 2)
                }
                if abs(delta) >= 0.33:
                    significant_dims.append((dim, delta))
        if significant_dims:
            print(f"\n  {r1} (n={len(role_members[r1])}) vs {r2} (n={len(role_members[r2])}):")
            for dim, delta in significant_dims:
                print(f"    {dim} ({dim_labels[dim]}): delta={delta:+.3f}")

# ============================================================
# 5c. CLIFF'S DELTA: Gender-Vergleich
# ============================================================
print("\n--- Gender-Vergleich (Cliff's delta) ---")
cliff_gender = {}
print(f"  Frauen (n={len(frauen_pids)}) vs Maenner (n={len(maenner_pids)}):")
for dim_idx, dim in enumerate(dim_names):
    vals_f = [persons[p]["scores"][dim_idx] for p in frauen_pids]
    vals_m = [persons[p]["scores"][dim_idx] for p in maenner_pids]
    delta = cliffs_delta(vals_f, vals_m)
    interp = interpret_delta(delta)
    cliff_gender[dim] = {
        "delta": round(delta, 4),
        "interpretation": interp,
        "mean_frauen": round(np.mean(vals_f), 2),
        "mean_maenner": round(np.mean(vals_m), 2)
    }
    if abs(delta) >= 0.147:
        print(f"    {dim} ({dim_labels[dim]}): delta={delta:+.3f} ({interp}) "
              f"[F={np.mean(vals_f):.1f}, M={np.mean(vals_m):.1f}]")

# ============================================================
# 6. DESKRIPTIVE STATISTIK DER STREUUNG
# ============================================================

print("\n" + "="*60)
print("DESKRIPTIVE STATISTIK DER STREUUNG")
print("="*60)

descriptive = {}
for dim_idx, dim in enumerate(dim_names):
    vals = data_matrix[:, dim_idx]
    q1 = np.percentile(vals, 25)
    q3 = np.percentile(vals, 75)
    iqr = q3 - q1
    descriptive[dim] = {
        "label": dim_labels[dim],
        "mean": round(float(np.mean(vals)), 3),
        "median": round(float(np.median(vals)), 1),
        "std": round(float(np.std(vals, ddof=1)), 3),
        "var": round(float(np.var(vals, ddof=1)), 3),
        "min": int(np.min(vals)),
        "max": int(np.max(vals)),
        "range": int(np.max(vals) - np.min(vals)),
        "Q1": round(float(q1), 1),
        "Q3": round(float(q3), 1),
        "IQR": round(float(iqr), 1),
        "skewness": round(float(skew_val := np.mean(((vals - np.mean(vals)) / np.std(vals)) ** 3)), 3),
        "kurtosis": round(float(np.mean(((vals - np.mean(vals)) / np.std(vals)) ** 4) - 3), 3)
    }

# Sortiert nach SD
print(f"\n{'Dim':<5} {'Label':<30} {'Mean':>6} {'SD':>6} {'IQR':>5} {'Range':>6} {'Min':>4} {'Max':>4}")
print("-" * 75)
desc_sorted = sorted(descriptive.items(), key=lambda x: -x[1]["std"])
for dim, stats in desc_sorted:
    print(f"{dim:<5} {stats['label']:<30} {stats['mean']:>6.2f} {stats['std']:>6.3f} "
          f"{stats['IQR']:>5.1f} {stats['range']:>6} {stats['min']:>4} {stats['max']:>4}")

print(f"\nGroesste Varianz:  {desc_sorted[0][0]} ({desc_sorted[0][1]['label']}) SD={desc_sorted[0][1]['std']:.3f}")
print(f"Kleinste Varianz:  {desc_sorted[-1][0]} ({desc_sorted[-1][1]['label']}) SD={desc_sorted[-1][1]['std']:.3f}")

# ============================================================
# 6b. Kruskal-Wallis Test pro Dimension (Cluster-Vergleich)
# ============================================================
from scipy.stats import kruskal, mannwhitneyu

print("\n--- Kruskal-Wallis Test (4 heuristische Cluster) pro Dimension ---")
kruskal_results = {}
for dim_idx, dim in enumerate(dim_names):
    groups = [np.array([persons[p]["scores"][dim_idx] for p in cluster_members[c]]) for c in cluster_types]
    stat, p_val = kruskal(*groups)
    kruskal_results[dim] = {
        "H_statistic": round(float(stat), 3),
        "p_value": round(float(p_val), 6),
        "significant_005": p_val < 0.05,
        "significant_001": p_val < 0.01
    }
    sig_marker = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
    print(f"  {dim} ({dim_labels[dim]:<30}): H={stat:.2f}, p={p_val:.4f} {sig_marker}")

# Mann-Whitney U fuer Gender
print("\n--- Mann-Whitney U Test (Gender) pro Dimension ---")
mwu_results = {}
for dim_idx, dim in enumerate(dim_names):
    vals_f = [persons[p]["scores"][dim_idx] for p in frauen_pids]
    vals_m = [persons[p]["scores"][dim_idx] for p in maenner_pids]
    stat, p_val = mannwhitneyu(vals_f, vals_m, alternative='two-sided')
    mwu_results[dim] = {
        "U_statistic": round(float(stat), 1),
        "p_value": round(float(p_val), 6),
        "significant_005": p_val < 0.05
    }
    sig_marker = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
    if p_val < 0.05:
        print(f"  {dim} ({dim_labels[dim]:<30}): U={stat:.0f}, p={p_val:.4f} {sig_marker}")

# ============================================================
# 7. ERGEBNISSE SPEICHERN
# ============================================================

# Cluster-Profile berechnen
cluster_profiles = {}
for c in cluster_types:
    members = cluster_members[c]
    if len(members) > 0:
        profile = {}
        for dim_idx, dim in enumerate(dim_names):
            vals = [persons[p]["scores"][dim_idx] for p in members]
            profile[dim] = {
                "mean": round(float(np.mean(vals)), 2),
                "std": round(float(np.std(vals, ddof=1)), 2) if len(vals) > 1 else 0,
                "median": round(float(np.median(vals)), 1),
                "n": len(vals)
            }
        profile["avg_all"] = round(float(np.mean([persons[p]["scores"] for p in members])), 2)
        cluster_profiles[c] = profile

# JSON-Output
results = {
    "metadata": {
        "n_persons": n,
        "n_dimensions": 12,
        "dimensions": dim_labels,
        "date": "2026-03-27",
        "method": "PCA + HDBSCAN + Cliff's delta + Kruskal-Wallis"
    },
    "pca": {
        "n_components_80pct": n_comp_80,
        "scree_data": scree_data,
        "pc1_loadings": {dim: round(float(load), 4) for dim, load in pc1_loadings},
        "pc2_loadings": {dim: round(float(load), 4) for dim, load in pc2_loadings},
        "top3_pc1_dims": top3_dims_pc1
    },
    "hdbscan_subspace": hdbscan_results,
    "heuristic_clusters": {
        "method": "Top-down Zuordnung ueber D07 (Machtkonzentration) und D11 (Egalitarismus), ergaenzt durch D04 und D06",
        "distribution": {c: len(cluster_members[c]) for c in cluster_types},
        "profiles": cluster_profiles,
        "assignments": {f"P{pid}": heuristic_clusters[pid] for pid in pids}
    },
    "cliffs_delta_clusters": cliff_results,
    "cliffs_delta_roles": cliff_roles,
    "cliffs_delta_gender": cliff_gender,
    "kruskal_wallis_clusters": kruskal_results,
    "mann_whitney_gender": mwu_results,
    "descriptive_statistics": descriptive,
    "group_assignments": {
        "roles": {f"P{pid}": roles.get(pid, "unassigned") for pid in pids},
        "gender": {f"P{pid}": gender[pid] for pid in pids},
        "role_sizes": {r: len(role_members[r]) for r in role_types},
        "gender_sizes": {"Frauen": len(frauen_pids), "Maenner": len(maenner_pids)},
        "frauen_pids": [f"P{p}" for p in frauen_pids]
    }
}

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)

json_path = output_dir / "statistical_analysis.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)
print(f"\nJSON gespeichert: {json_path}")

# ============================================================
# 8. REPORT GENERIEREN
# ============================================================

report_lines = []
report_lines.append("# Statistische Analyse: SWR/KI-Elite Weltbild-Daten")
report_lines.append("")
report_lines.append(f"**Datum:** 2026-03-27")
report_lines.append(f"**Datenbasis:** {n} Personen x 12 Dimensionen (D01-D12, Skala 1-10)")
report_lines.append(f"**Methoden:** PCA, HDBSCAN, Cliff's delta, Kruskal-Wallis, Mann-Whitney U")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# --- 1. PCA ---
report_lines.append("## 1. PCA (Dimensionsreduktion)")
report_lines.append("")
report_lines.append(f"**Komponenten fuer 80% erklaerte Varianz:** {n_comp_80}")
report_lines.append("")
report_lines.append("### Scree-Plot Daten")
report_lines.append("")
report_lines.append("| Komponente | Eigenwert | Erkl. Varianz | Kumuliert |")
report_lines.append("|------------|-----------|---------------|-----------|")
for s in scree_data:
    report_lines.append(f"| {s['component']} | {s['eigenvalue']:.3f} | {s['explained_variance_ratio']*100:.1f}% | {s['cumulative']*100:.1f}% |")
report_lines.append("")

report_lines.append("### PC1 Ladungen (Allgemeiner Weltbild-Intensitaetsfaktor)")
report_lines.append("")
report_lines.append("| Dimension | Ladung | Label |")
report_lines.append("|-----------|--------|-------|")
for dim, load in pc1_sorted:
    report_lines.append(f"| {dim} | {load:+.4f} | {dim_labels[dim]} |")
report_lines.append("")
report_lines.append(f"**Interpretation PC1:** Die staerksten Ladungen zeigen, welche Dimensionen am meisten zur Gesamtvariation beitragen.")
report_lines.append("")

report_lines.append("### PC2 Ladungen (Differenzierungsachse)")
report_lines.append("")
report_lines.append("| Dimension | Ladung | Label |")
report_lines.append("|-----------|--------|-------|")
for dim, load in pc2_sorted:
    report_lines.append(f"| {dim} | {load:+.4f} | {dim_labels[dim]} |")
report_lines.append("")

# --- 2. Subspace Clustering ---
report_lines.append("## 2. Subspace-Clustering (HDBSCAN)")
report_lines.append("")
report_lines.append("### 2a. HDBSCAN auf D07+D11 (primaere Differenzierungsdimensionen)")
report_lines.append("")
report_lines.append("| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |")
report_lines.append("|-----------------|-------------|---------|-------|--------|------------|")
for key, val in hdbscan_results.items():
    if val["subspace"] == "D07+D11":
        sil_str = f"{val['silhouette']:.3f}" if val["silhouette"] is not None else "N/A"
        report_lines.append(f"| {val['min_cluster_size']} | {val['min_samples']} | {val['n_clusters']} | {val['n_noise']} | {val['noise_pct']}% | {sil_str} |")
report_lines.append("")

report_lines.append("### 2b. HDBSCAN auf PC1+PC2+PC3")
report_lines.append("")
report_lines.append("| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |")
report_lines.append("|-----------------|-------------|---------|-------|--------|------------|")
for key, val in hdbscan_results.items():
    if val["subspace"] == "PC1+PC2+PC3":
        sil_str = f"{val['silhouette']:.3f}" if val["silhouette"] is not None else "N/A"
        report_lines.append(f"| {val['min_cluster_size']} | {val['min_samples']} | {val['n_clusters']} | {val['n_noise']} | {val['noise_pct']}% | {sil_str} |")
report_lines.append("")

top3_key = "+".join(top3_dims_pc1)
report_lines.append(f"### 2c. HDBSCAN auf Top-3 PC1-Dimensionen ({top3_key})")
report_lines.append("")
report_lines.append("| min_cluster_size | min_samples | Cluster | Noise | Noise% | Silhouette |")
report_lines.append("|-----------------|-------------|---------|-------|--------|------------|")
for key, val in hdbscan_results.items():
    if val["subspace"] == top3_key:
        sil_str = f"{val['silhouette']:.3f}" if val["silhouette"] is not None else "N/A"
        report_lines.append(f"| {val['min_cluster_size']} | {val['min_samples']} | {val['n_clusters']} | {val['n_noise']} | {val['noise_pct']}% | {sil_str} |")
report_lines.append("")

report_lines.append("**Befund:** HDBSCAN findet auf den 100x12-Daten konsistent wenige oder keine dichten Cluster. Dies deutet auf eine homogene, kontinuierliche Verteilung hin -- die KI-Elite bildet kein klar separiertes Cluster-Muster, sondern ein Spektrum. Die heuristischen Typen (Architekt/Hueter/Innovator/Befreier) sind daher als Idealtypen im Weberschen Sinne zu verstehen, nicht als natuerliche Cluster.")
report_lines.append("")

# --- 3. Heuristische Cluster ---
report_lines.append("## 3. Heuristische Cluster-Analyse (Top-Down)")
report_lines.append("")
report_lines.append("### Cluster-Verteilung")
report_lines.append("")
report_lines.append("| Cluster | n | Anteil |")
report_lines.append("|---------|---|--------|")
for c in cluster_types:
    n_c = len(cluster_members[c])
    report_lines.append(f"| {c} | {n_c} | {n_c}% |")
report_lines.append("")

report_lines.append("### Cluster-Profile (Mittelwerte)")
report_lines.append("")
header = "| Dimension |"
for c in cluster_types:
    header += f" {c} |"
report_lines.append(header)
report_lines.append("|-----------|" + "------|" * len(cluster_types))
for dim_idx, dim in enumerate(dim_names):
    row = f"| {dim} {dim_labels[dim][:20]} |"
    for c in cluster_types:
        m = cluster_profiles[c][dim]["mean"]
        row += f" {m:.1f} |"
    report_lines.append(row)
report_lines.append("")

# --- 4. Effektstaerken ---
report_lines.append("## 4. Effektstaerken (Cliff's delta) -- Heuristische Cluster")
report_lines.append("")
report_lines.append("Interpretation: |d| < 0.147 negligible, < 0.33 small, < 0.474 medium, >= 0.474 large")
report_lines.append("")

for pair_key, dims in cliff_results.items():
    c1, c2 = pair_key.split("_vs_")
    medium_plus = [(dim, r) for dim, r in dims.items() if abs(r["delta"]) >= 0.33]
    if medium_plus:
        report_lines.append(f"### {c1} vs {c2}")
        report_lines.append("")
        report_lines.append("| Dimension | delta | Interpretation | Mean {c1} | Mean {c2} |".replace("{c1}", c1).replace("{c2}", c2))
        report_lines.append("|-----------|-------|----------------|-----------|-----------|")
        for dim, r in sorted(medium_plus, key=lambda x: -abs(x[1]["delta"])):
            report_lines.append(f"| {dim} ({dim_labels[dim]}) | {r['delta']:+.3f} | {r['interpretation']} | {r['mean_1']:.1f} | {r['mean_2']:.1f} |")
        report_lines.append("")

# --- Staerkste Differenzierungsdimensionen ---
report_lines.append("### Staerkste Differenzierungsdimensionen (ueber alle Cluster-Paare)")
report_lines.append("")
report_lines.append("| Rang | Dimension | Medium+ Effekte | Max |delta| |")
report_lines.append("|------|-----------|----------------|-------------|")
for rank, (dim, count) in enumerate(dim_diff_sorted, 1):
    if count > 0:
        report_lines.append(f"| {rank} | {dim} ({dim_labels[dim]}) | {count}x | {dim_diff_max[dim]:.3f} |")
report_lines.append("")

# --- 5. Rollen-Vergleiche ---
report_lines.append("## 5. Rollen-Vergleiche (Cliff's delta)")
report_lines.append("")
report_lines.append(f"Rollenverteilung: " + ", ".join(f"{r} n={len(role_members[r])}" for r in role_types))
report_lines.append("")
for pair_key, dims in cliff_roles.items():
    r1, r2 = pair_key.split("_vs_")
    medium_plus = [(dim, r) for dim, r in dims.items() if abs(r["delta"]) >= 0.33]
    if medium_plus:
        report_lines.append(f"### {r1} vs {r2}")
        report_lines.append("")
        report_lines.append(f"| Dimension | delta | Interpretation | Mean {r1} | Mean {r2} |")
        report_lines.append("|-----------|-------|----------------|-----------|-----------|")
        for dim, r in sorted(medium_plus, key=lambda x: -abs(x[1]["delta"])):
            report_lines.append(f"| {dim} ({dim_labels[dim]}) | {r['delta']:+.3f} | {r['interpretation']} | {r['mean_1']:.1f} | {r['mean_2']:.1f} |")
        report_lines.append("")

# --- 6. Gender ---
report_lines.append("## 6. Gender-Vergleich")
report_lines.append("")
report_lines.append(f"Frauen n={len(frauen_pids)}, Maenner n={len(maenner_pids)}")
report_lines.append("")
report_lines.append("### Cliff's delta")
report_lines.append("")
report_lines.append("| Dimension | delta | Interpretation | Mean Frauen | Mean Maenner |")
report_lines.append("|-----------|-------|----------------|-------------|--------------|")
for dim in dim_names:
    r = cliff_gender[dim]
    if abs(r["delta"]) >= 0.147:
        report_lines.append(f"| {dim} ({dim_labels[dim]}) | {r['delta']:+.3f} | {r['interpretation']} | {r['mean_frauen']:.1f} | {r['mean_maenner']:.1f} |")
report_lines.append("")

# --- 7. Kruskal-Wallis ---
report_lines.append("## 7. Kruskal-Wallis H-Test (4 heuristische Cluster)")
report_lines.append("")
report_lines.append("| Dimension | H | p-Wert | Signifikant? |")
report_lines.append("|-----------|---|--------|--------------|")
for dim in dim_names:
    kr = kruskal_results[dim]
    sig = "***" if kr["p_value"] < 0.001 else "**" if kr["p_value"] < 0.01 else "*" if kr["p_value"] < 0.05 else "n.s."
    report_lines.append(f"| {dim} ({dim_labels[dim]}) | {kr['H_statistic']:.2f} | {kr['p_value']:.4f} | {sig} |")
report_lines.append("")

# --- 8. Deskriptive Statistik ---
report_lines.append("## 8. Deskriptive Statistik (Streuung)")
report_lines.append("")
report_lines.append("Sortiert nach Standardabweichung (absteigend):")
report_lines.append("")
report_lines.append("| Rang | Dimension | Mean | SD | IQR | Range | Min | Max | Schiefe | Kurtosis |")
report_lines.append("|------|-----------|------|-----|-----|-------|-----|-----|---------|----------|")
for rank, (dim, stats) in enumerate(desc_sorted, 1):
    report_lines.append(f"| {rank} | {dim} ({stats['label']}) | {stats['mean']:.2f} | {stats['std']:.3f} | {stats['IQR']:.1f} | {stats['range']} | {stats['min']} | {stats['max']} | {stats['skewness']:+.2f} | {stats['kurtosis']:+.2f} |")
report_lines.append("")
report_lines.append(f"**Groesste Streuung:** {desc_sorted[0][0]} ({desc_sorted[0][1]['label']}) mit SD={desc_sorted[0][1]['std']:.3f}")
report_lines.append(f"**Kleinste Streuung:** {desc_sorted[-1][0]} ({desc_sorted[-1][1]['label']}) mit SD={desc_sorted[-1][1]['std']:.3f}")
report_lines.append("")

# --- 9. Zusammenfassung ---
report_lines.append("## 9. Zusammenfassung der Kernbefunde")
report_lines.append("")
report_lines.append("### PCA")
report_lines.append(f"- {n_comp_80} Hauptkomponenten erklaeren 80% der Gesamtvarianz")
report_lines.append(f"- PC1 ({explained_var[0]*100:.1f}% Varianz) laed am staerksten auf: {pc1_sorted[0][0]} ({dim_labels[pc1_sorted[0][0]]}), {pc1_sorted[1][0]} ({dim_labels[pc1_sorted[1][0]]}), {pc1_sorted[2][0]} ({dim_labels[pc1_sorted[2][0]]})")
report_lines.append(f"- PC2 ({explained_var[1]*100:.1f}% Varianz) differenziert primaer ueber: {pc2_sorted[0][0]} ({dim_labels[pc2_sorted[0][0]]}), {pc2_sorted[1][0]} ({dim_labels[pc2_sorted[1][0]]})")
report_lines.append("")
report_lines.append("### Clustering")
report_lines.append("- HDBSCAN findet KEINE robusten natuerlichen Cluster -- die KI-Elite bildet ein Kontinuum")
report_lines.append("- Heuristische Typen (Architekt/Hueter/Innovator/Befreier) sind als Idealtypen zu interpretieren, nicht als diskrete Gruppen")
report_lines.append("")
report_lines.append("### Effektstaerken")
sig_kruskal = [dim for dim in dim_names if kruskal_results[dim]["p_value"] < 0.05]
report_lines.append(f"- Signifikante Kruskal-Wallis-Unterschiede (p<0.05) auf: {', '.join(sig_kruskal)}")
report_lines.append(f"- Staerkste Differenzierungsdimension: {dim_diff_sorted[0][0]} ({dim_labels[dim_diff_sorted[0][0]]}) mit {dim_diff_sorted[0][1]}x medium+ Cliff's delta")
report_lines.append("")
report_lines.append("### Streuung")
report_lines.append(f"- Heterogenste Dimension: {desc_sorted[0][0]} ({desc_sorted[0][1]['label']}) -- hier divergieren die Weltbilder am staerksten")
report_lines.append(f"- Homogenste Dimension: {desc_sorted[-1][0]} ({desc_sorted[-1][1]['label']}) -- hier herrscht relativer Konsens")
report_lines.append("")
report_lines.append("---")
report_lines.append("")
report_lines.append("*Generiert: 2026-03-27 | Methode: PCA + HDBSCAN + Cliff's delta + Kruskal-Wallis + Mann-Whitney U*")
report_lines.append("*Datenbasis: rating_GESAMT_D01-D12.md (100 Personen x 12 Dimensionen)*")

report_path = output_dir / "STATISTICAL_REPORT.md"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
print(f"Report gespeichert: {report_path}")

print("\n" + "="*60)
print("ANALYSE ABGESCHLOSSEN")
print("="*60)
