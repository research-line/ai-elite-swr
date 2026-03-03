"""
Phase 7.22: Visualisierungen fuer das Paper
Projekt: "Was denkt die KI-Elite?"
Erstellt: 2026-02-12

Erzeugt alle Kern-Figuren als PNG/SVG in _results/figures/
Voraussetzung: pip install matplotlib numpy seaborn
"""

import numpy as np
from pathlib import Path

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    print("WARNUNG: matplotlib nicht installiert. Installiere mit: pip install matplotlib")

try:
    import seaborn as sns
    HAS_SNS = True
except ImportError:
    HAS_SNS = False
    print("WARNUNG: seaborn nicht installiert. Installiere mit: pip install seaborn")

# === DATEN ===
YEARS = list(range(2010, 2027))

DIMS = {
    "D01": [9,8,9,8,8,8,9,8,7,6,7,8,9,8,9,9,9],
    "D02": [9,8,9,8,9,8,9,8,7,6,7,7,8,7,8,8,7],
    "D03": [9,8,9,8,9,9,9,9,8,7,7,8,8,9,9,10,9],
    "D04": [9,7,9,9,8,9,8,9,8,9,8,9,9,7,7,8,8],
    "D05": [9,10,9,8,8,9,9,7,8,6,9,7,8,8,9,9,9],
    "D06": [10,7,9,9,8,8,8,8,7,6,7,8,8,7,8,7,8],
    "D07": [8,6,7,6,9,7,8,6,7,5,6,5,6,6,7,8,8],
    "D08": [9,8,9,9,8,9,10,9,8,8,9,9,10,9,9,10,10],
    "D09": [5,4,5,6,4,5,4,6,5,6,5,5,4,6,6,6,7],
    "D10": [10,8,9,9,8,9,10,7,7,6,6,7,8,5,6,6,6],
    "D11": [3,2,2,4,2,3,2,6,5,6,7,6,5,4,3,3,4],
    "D12": [10,8,10,9,9,9,9,9,8,7,8,9,9,7,7,7,7],
}

DIM_LABELS = {
    "D01": "Sendungsbewusstsein",
    "D02": "Kontrollueberzeugung",
    "D03": "Zugehoerigkeit",
    "D04": "Verantwortung",
    "D05": "Tech-Determinismus",
    "D06": "Fortschrittsoptimismus",
    "D07": "Machtkonzentration",
    "D08": "Dringlichkeit",
    "D09": "Menschl. Einzigartigkeit",
    "D10": "Transhumanismus",
    "D11": "Egalitarismus",
    "D12": "Zukunft der Menschheit",
}

DIM_GROUPS = {
    "Selbstbild (D01-D04)": ["D01","D02","D03","D04"],
    "Weltbild (D05-D08)": ["D05","D06","D07","D08"],
    "Menschenbild (D09-D12)": ["D09","D10","D11","D12"],
}

EVENTS = {
    2012: "AlexNet",
    2016: "AlphaGo",
    2017: "Transformer",
    2019: "GPT-2",
    2020: "GPT-3",
    2022: "ChatGPT",
    2023: "GPT-4",
    2024: "Nobel/EU AI Act",
}

GRUPPEN = {
    "GR_ceo":  [9,9,10,8,9,8,9,9,4,7,3,8],
    "GR_akad": [6,7,8,8,6,6,5,7,6,4,7,6],
    "GR_inv":  [9,10,9,4,10,9,10,10,3,9,2,9],
    "GR_gru":  [7,8,9,9,8,8,7,9,5,6,5,8],
    "GD_frauen": [6,7,9,9,6,7,6,6,7,5,8,7],
    "GD_maenner": [10,10,10,7,10,9,9,10,3,8,2,9],
    "GF_anthropic": [8,7,8,9,7,7,5,9,6,5,6,6],
    "GF_openai": [9,8,8,7,9,9,6,8,4,6,5,9],
    "GF_google": [10,9,9,8,8,10,7,7,5,7,4,10],
    "GH_risk": [9,4,6,10,4,5,5,10,4,3,7,4],
    "GH_speed": [9,9,8,6,8,10,7,10,3,8,4,9],
}

OUT_DIR = Path(r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_results\figures")


def setup():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if HAS_MPL:
        plt.rcParams.update({
            'figure.figsize': (12, 6),
            'font.size': 11,
            'axes.grid': True,
            'grid.alpha': 0.3,
        })


def fig1_zeitreihen_panel():
    """Fig 1: 3x4 Panel aller 12 Dimensionen ueber die Zeit"""
    if not HAS_MPL:
        return
    fig, axes = plt.subplots(3, 4, figsize=(16, 10), sharex=True, sharey=True)
    fig.suptitle("Weltbild-Dimensionen D01-D12 (2010-2026)", fontsize=14, fontweight='bold')

    colors = {'Selbstbild': '#2196F3', 'Weltbild': '#4CAF50', 'Menschenbild': '#FF9800'}

    for idx, (dim_id, values) in enumerate(DIMS.items()):
        row, col = divmod(idx, 4)
        ax = axes[row][col]

        if row == 0:
            color = colors['Selbstbild']
        elif row == 1:
            color = colors['Weltbild']
        else:
            color = colors['Menschenbild']

        ax.plot(YEARS, values, 'o-', color=color, markersize=4, linewidth=1.5)
        ax.set_title(f"{dim_id}: {DIM_LABELS[dim_id]}", fontsize=9, fontweight='bold')
        ax.set_ylim(0.5, 10.5)
        ax.set_yticks([2, 4, 6, 8, 10])

        # Markiere 2019 und 2022
        ax.axvline(x=2019, color='red', alpha=0.3, linestyle='--', linewidth=0.8)
        ax.axvline(x=2022, color='orange', alpha=0.3, linestyle='--', linewidth=0.8)

        if row == 2:
            ax.set_xlabel("Jahr")
        if col == 0:
            ax.set_ylabel("Wert (1-10)")

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig1_zeitreihen_panel.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig1_zeitreihen_panel.svg", bbox_inches='tight')
    plt.close()
    print("Fig 1: Zeitreihen-Panel gespeichert")


def fig2_heatmap():
    """Fig 2: Heatmap Jahre x Dimensionen"""
    if not HAS_MPL or not HAS_SNS:
        return

    data = np.array([DIMS[f"D{i:02d}"] for i in range(1, 13)]).T
    dim_labels_short = [f"D{i:02d}" for i in range(1, 13)]

    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(data, annot=True, fmt='d', cmap='RdYlGn',
                xticklabels=dim_labels_short, yticklabels=YEARS,
                vmin=1, vmax=10, linewidths=0.5, ax=ax,
                cbar_kws={'label': 'Wert (1=niedrig, 10=hoch)'})

    ax.set_title("Weltbild der KI-Elite: 12 Dimensionen x 17 Jahre", fontsize=13, fontweight='bold')
    ax.set_xlabel("Dimension")
    ax.set_ylabel("Jahr")

    # Trennlinien zwischen Dimensionsgruppen
    ax.axvline(x=4, color='black', linewidth=2)
    ax.axvline(x=8, color='black', linewidth=2)

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig2_heatmap.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig2_heatmap.svg", bbox_inches='tight')
    plt.close()
    print("Fig 2: Heatmap gespeichert")


def fig3_radar_vergleich():
    """Fig 3: Radar-Charts 2010 vs. 2019 vs. 2025"""
    if not HAS_MPL:
        return

    angles = np.linspace(0, 2 * np.pi, 12, endpoint=False).tolist()
    angles += angles[:1]

    labels = [f"D{i:02d}" for i in range(1, 13)]

    years_to_plot = [2010, 2019, 2025]
    colors_radar = ['#2196F3', '#F44336', '#4CAF50']
    idx_map = {y: YEARS.index(y) for y in years_to_plot}

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for year, color in zip(years_to_plot, colors_radar):
        idx = idx_map[year]
        values = [DIMS[f"D{i:02d}"][idx] for i in range(1, 13)]
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=str(year), color=color, markersize=4)
        ax.fill(angles, values, alpha=0.1, color=color)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_title("Weltbild-Profil: 2010 vs. 2019 vs. 2025", fontsize=13, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig3_radar_vergleich.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig3_radar_vergleich.svg", bbox_inches='tight')
    plt.close()
    print("Fig 3: Radar-Vergleich gespeichert")


def fig4_korrelationsmatrix():
    """Fig 4: Korrelationsmatrix der 12 Dimensionen"""
    if not HAS_MPL or not HAS_SNS:
        return
    from scipy import stats as scipy_stats

    dim_ids = [f"D{i:02d}" for i in range(1, 13)]
    n = 12
    corr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            r, _ = scipy_stats.pearsonr(DIMS[dim_ids[i]], DIMS[dim_ids[j]])
            corr[i][j] = r

    fig, ax = plt.subplots(figsize=(10, 8))
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
                xticklabels=dim_ids, yticklabels=dim_ids,
                vmin=-1, vmax=1, center=0, square=True, ax=ax,
                cbar_kws={'label': 'Pearson r'})

    ax.set_title("Korrelationsmatrix der 12 Weltbild-Dimensionen", fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig4_korrelationsmatrix.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig4_korrelationsmatrix.svg", bbox_inches='tight')
    plt.close()
    print("Fig 4: Korrelationsmatrix gespeichert")


def fig5_gruppen_heatmap():
    """Fig 5: Gruppen-Vergleichs-Heatmap"""
    if not HAS_MPL or not HAS_SNS:
        return

    gruppen_labels = list(GRUPPEN.keys())
    dim_ids = [f"D{i:02d}" for i in range(1, 13)]
    data = np.array(list(GRUPPEN.values()))

    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(data, annot=True, fmt='d', cmap='RdYlGn',
                xticklabels=dim_ids, yticklabels=gruppen_labels,
                vmin=1, vmax=10, linewidths=0.5, ax=ax,
                cbar_kws={'label': 'Wert (1-10)'})

    ax.set_title("Weltbild-Profile nach Gruppen", fontsize=13, fontweight='bold')
    ax.set_xlabel("Dimension")

    # Trennlinien
    ax.axvline(x=4, color='black', linewidth=2)
    ax.axvline(x=8, color='black', linewidth=2)
    ax.axhline(y=4, color='black', linewidth=1)
    ax.axhline(y=6, color='black', linewidth=1)
    ax.axhline(y=9, color='black', linewidth=1)

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig5_gruppen_heatmap.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig5_gruppen_heatmap.svg", bbox_inches='tight')
    plt.close()
    print("Fig 5: Gruppen-Heatmap gespeichert")


def fig6_sagen_vs_handeln():
    """Fig 6: Sagen vs. Handeln Balkendiagramm"""
    if not HAS_MPL:
        return

    sagen =  [8,8,8,7,8,8,6,8,5,7,5,8]
    handeln = [7,9,9,5,9,6,8,9,3,8,2,7]

    dim_ids = [f"D{i:02d}" for i in range(1, 13)]
    x = np.arange(12)
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 6))
    bars1 = ax.bar(x - width/2, sagen, width, label='Aussagen (Sagen)', color='#2196F3', alpha=0.8)
    bars2 = ax.bar(x + width/2, handeln, width, label='Handlungen (Tun)', color='#FF5722', alpha=0.8)

    ax.set_ylabel('Wert (1-10)')
    ax.set_title('Sagen vs. Handeln: Kongruenz-Analyse der KI-Elite', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(dim_ids, fontsize=9)
    ax.legend()
    ax.set_ylim(0, 11)

    # Delta-Annotationen
    for i in range(12):
        delta = handeln[i] - sagen[i]
        if abs(delta) >= 2:
            color = 'red' if delta < 0 else 'darkgreen'
            ax.annotate(f"{delta:+d}", xy=(i, max(sagen[i], handeln[i]) + 0.3),
                       ha='center', fontsize=9, fontweight='bold', color=color)

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig6_sagen_vs_handeln.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig6_sagen_vs_handeln.svg", bbox_inches='tight')
    plt.close()
    print("Fig 6: Sagen vs. Handeln gespeichert")


def fig7_schluesseltrends():
    """Fig 7: Die 4 wichtigsten Trend-Linien"""
    if not HAS_MPL:
        return

    key_dims = {
        "D10 Transhumanismus": ("D10", '#9C27B0'),
        "D11 Egalitarismus": ("D11", '#F44336'),
        "D08 Dringlichkeit": ("D08", '#FF9800'),
        "D01 Sendungsbewusstsein": ("D01", '#2196F3'),
    }

    fig, ax = plt.subplots(figsize=(12, 6))

    for label, (dim_id, color) in key_dims.items():
        ax.plot(YEARS, DIMS[dim_id], 'o-', label=label, color=color, linewidth=2, markersize=5)

    # Events markieren
    for year, event in EVENTS.items():
        ax.axvline(x=year, color='gray', alpha=0.2, linestyle='--')
        ax.text(year, 10.3, event, ha='center', fontsize=7, rotation=45)

    ax.set_xlabel("Jahr")
    ax.set_ylabel("Wert (1-10)")
    ax.set_title("Schluesseltrends im Weltbild der KI-Elite (2010-2026)", fontsize=13, fontweight='bold')
    ax.set_ylim(0.5, 11)
    ax.legend(loc='lower left')

    plt.tight_layout()
    plt.savefig(OUT_DIR / "fig7_schluesseltrends.png", dpi=200, bbox_inches='tight')
    plt.savefig(OUT_DIR / "fig7_schluesseltrends.svg", bbox_inches='tight')
    plt.close()
    print("Fig 7: Schluesseltrends gespeichert")


def main():
    setup()
    if not HAS_MPL:
        print("\nKann keine Figuren erzeugen. Bitte installiere matplotlib:")
        print("  pip install matplotlib seaborn scipy")
        return

    print(f"Ausgabe-Verzeichnis: {OUT_DIR}")
    print()

    fig1_zeitreihen_panel()
    fig2_heatmap()
    fig3_radar_vergleich()
    fig4_korrelationsmatrix()
    fig5_gruppen_heatmap()
    fig6_sagen_vs_handeln()
    fig7_schluesseltrends()

    print(f"\nAlle Figuren gespeichert in: {OUT_DIR}")


if __name__ == "__main__":
    main()
