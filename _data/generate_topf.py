#!/usr/bin/env python3
"""
generate_topf.py - Topf (Syntheseeinheit) Generator
=====================================================
Phase 7.02 des UNTERSUCHUNGSPLAN

Generiert beliebige Toepfe (geblindete Datenkorpora) aus der DB
fuer die LLM-gestuetzte Weltbild-Rekonstruktion.

TOPF = gefilterte Sammlung von Aussagen + Handlungen, geblindet.
Aus jedem Topf wird eine synthetische Weltbild-Person erschaffen.

Usage:
    python generate_topf.py --list                  # Alle Toepfe auflisten
    python generate_topf.py --all                   # Alle Toepfe generieren
    python generate_topf.py GA_ges_AH               # Einzelnen Topf generieren
    python generate_topf.py --batch kern             # Batch: kern, zeit, epochen, kongruenz, gruppen, alle
    python generate_topf.py --stats                  # Statistiken pro Topf
    python generate_topf.py --validate               # Alle Toepfe pruefen (K2: min 15 DPs)

Autor: Claude Opus 4.6
Datum: 2026-02-12
"""

import sqlite3
import os
import sys
import json
from datetime import datetime

# Import Blindung aus extract_blinded.py (gleicher Ordner)
from extract_blinded import blind_text

# ============================================================
# KONSTANTEN
# ============================================================

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_results", "toepfe")
MIN_DATAPOINTS = 15  # K2: Mindesttopfgroesse

# ============================================================
# GRUPPEN-DEFINITIONEN
# ============================================================
# Jede Gruppe ist eine Liste von person_id-Werten.
# Gruppen koennen sich ueberlappen (eine Person kann in mehreren sein).
# Klassifikation basiert auf aktueller Hauptrolle + Firmenaffiliation.

GRUPPEN = {
    # --- Top-N ---
    "top10": [1, 2, 3, 4, 5, 6, 8, 9, 10, 11],

    # --- ROLLEN (F5a) ---
    # CEOs: Leiten grosse/etablierte Unternehmen (>$10B oder Top-20)
    "rolle_ceo": [
        1,   # Jensen Huang (NVIDIA)
        2,   # Sam Altman (OpenAI)
        3,   # Elon Musk (xAI/Tesla/SpaceX)
        4,   # Sundar Pichai (Alphabet)
        5,   # Mark Zuckerberg (Meta)
        7,   # Larry Ellison (Oracle)
        9,   # Dario Amodei (Anthropic)
        11,  # Demis Hassabis (Google DeepMind)
        13,  # Satya Nadella (Microsoft)
        14,  # Lisa Su (AMD)
        15,  # Tim Cook (Apple)
        16,  # Masayoshi Son (SoftBank)
        23,  # Mustafa Suleyman (Microsoft AI)
        38,  # Ali Ghodsi (Databricks)
        39,  # Alex Karp (Palantir)
        46,  # Andy Jassy (Amazon)
        64,  # Lip-Bu Tan (Intel)
        84,  # Rene Haas (ARM)
        94,  # Steve Huffman (Reddit)
    ],

    # Akademiker: Primaer universitaer affiliiert, Forschungsfokus
    "rolle_akad": [
        18,  # Fei-Fei Li (Stanford)
        20,  # Yann LeCun (Meta FAIR, akademisch gepraegt)
        21,  # Geoffrey Hinton (U Toronto, emeritus)
        22,  # Andrew Ng (Stanford, AI Fund)
        57,  # Stuart Russell (UC Berkeley)
        58,  # Pieter Abbeel (UC Berkeley)
        59,  # Christopher Manning (Stanford)
        60,  # Michael I. Jordan (UC Berkeley)
        61,  # Trevor Darrell (UC Berkeley)
        62,  # Yoshua Bengio (MILA, Montreal)
        83,  # Daphne Koller (ex-Stanford, insitro)
        99,  # Dorsa Sadigh (Stanford)
    ],

    # Investoren: Primaerrolle ist VC/Investment
    "rolle_inv": [
        24,  # Marc Andreessen (a16z)
        25,  # Peter Thiel (Founders Fund)
        31,  # Reid Hoffman (Greylock)
        32,  # Vinod Khosla (Khosla Ventures)
        49,  # Ben Horowitz (a16z)
        50,  # Chris Dixon (a16z)
        82,  # Martin Casado (a16z)
        87,  # Sarah Guo (Conviction)
    ],

    # Gruender: Startup-Gruender, technische Mitgruender, nicht Mega-Corp
    "rolle_gru": [
        6,   # Larry Page (Gruender Google, zurueckgezogen)
        8,   # Sergey Brin (Gruender Google, zurueckgezogen)
        10,  # Jeff Bezos (Gruender Amazon, zurueckgezogen)
        12,  # Ilya Sutskever (SSI)
        17,  # Daniela Amodei (Anthropic)
        26,  # Mira Murati (Thinking Machines Lab)
        27,  # Bret Taylor (Sierra AI)
        28,  # Greg Brockman (OpenAI)
        29,  # Alexandr Wang (ex-Scale AI)
        30,  # Noam Shazeer (Google DeepMind)
        33,  # Ashish Vaswani (Essential AI)
        34,  # Michael Truell (Cursor)
        35,  # Aravind Srinivas (Perplexity)
        40,  # Aidan Gomez (Cohere)
        41,  # Michael Intrator (CoreWeave)
        42,  # Scott Wu (Cognition)
        43,  # Palmer Luckey (Anduril)
        48,  # Clement Delangue (Hugging Face)
        51,  # Jack Clark (Anthropic)
        52,  # Jared Kaplan (Anthropic)
        53,  # Tom Brown (Anthropic)
        54,  # Chris Olah (Anthropic)
        55,  # Sam McCandlish (Anthropic)
        63,  # Winston Weinberg (Harvey AI)
        65,  # Jakob Uszkoreit (Inceptive)
        66,  # Illia Polosukhin (NEAR Protocol)
        67,  # Lukasz Kaiser (Sakana AI)
        68,  # Llion Jones (Sakana AI)
        69,  # Niki Parmar (ex-Google Brain)
        72,  # Naveen Rao (Unconventional AI)
        80,  # May Habib (Writer)
        85,  # Brett Adcock (Figure AI)
        86,  # Navrina Singh (Credo AI)
        90,  # Karol Hausman (Physical Intelligence)
        95,  # Emad Mostaque (Stability AI)
        96,  # Edwin Chen (Surge AI)
    ],

    # --- FIRMEN (F5d) ---
    # Aktuelle + ehemalige Kernmitglieder
    "firma_anthropic": [
        9, 17, 51, 52, 53, 54, 55, 56, 73,
        # 9 Dario, 17 Daniela, 51 Jack Clark, 52 Kaplan,
        # 53 Tom Brown, 54 Olah, 55 McCandlish, 56 Krieger, 73 Leike
    ],

    "firma_openai": [
        2, 28, 44, 45, 81, 91, 67,
        # 2 Altman, 28 Brockman, 44 Pachocki, 45 Mark Chen,
        # 81 D'Angelo (Board), 91 Zoph, 67 Kaiser (ex)
        # Hinweis: 12 Sutskever, 26 Murati sind ex-OpenAI (jetzt eigene Firmen)
    ],

    "firma_google_dm": [
        4, 6, 8, 11, 19, 30, 77,
        # 4 Pichai, 6 Larry Page, 8 Sergey Brin, 11 Hassabis,
        # 19 Jeff Dean, 30 Shazeer, 77 Bavor (ex, jetzt Sierra)
    ],

    # --- HALTUNG (F5b, F5c, F5f) ---
    # Open-Source-Befuerworter: Aktiv OS-Modelle publiziert oder propagiert
    "haltung_open": [
        5,   # Zuckerberg (Llama)
        20,  # Yann LeCun (FAIR, OS-Advocacy)
        48,  # Delangue (Hugging Face)
        66,  # Polosukhin (NEAR, OS)
        92,  # Chintala (PyTorch)
        95,  # Mostaque (Stability AI, SD)
    ],

    # Closed-Source: Bewusst proprietaere Modelle, gegen Offenlegung
    "haltung_closed": [
        2,   # Altman (OpenAI, GPT closed)
        4,   # Pichai (Gemini, closed)
        9,   # Dario Amodei (Anthropic, closed aus Sicherheitsgruenden)
        11,  # Hassabis (DeepMind, closed)
        13,  # Nadella (Microsoft, Copilot closed)
    ],

    # Risiko-Warner: Oeffentlich vor existenziellen KI-Risiken gewarnt
    "haltung_risk": [
        3,   # Musk (warnte frueh, gruendete dann xAI)
        12,  # Sutskever (verliess OpenAI, Sicherheitsfokus)
        21,  # Hinton (verliess Google, warnt seitdem)
        57,  # Russell (Human Compatible, CHAI)
        62,  # Bengio (unterschrieb Moratorium-Brief)
        73,  # Leike (verliess OpenAI wegen Safety-Bedenken)
    ],

    # Beschleuniger: Explizit fuer schnelles Voranschreiten
    "haltung_speed": [
        1,   # Huang (NVIDIA: "AI factories", Skalierung)
        2,   # Altman (OpenAI: schnelle Iteration)
        3,   # Musk (xAI: "truth-seeking AI", schnell gebaut)
        16,  # Son ($100B Vision Fund, $500B Stargate)
        24,  # Andreessen ("It's time to build", Techno-Optimist)
        32,  # Khosla (aggressive KI-Investitionen)
        43,  # Luckey (Anduril: "build fast, deploy fast")
    ],

    # Regulierung pro: Unterstuetzen KI-Regulierung aktiv
    "haltung_regpro": [
        9,   # Dario Amodei (RSP, kooperiert mit Gesetzgebern)
        17,  # Daniela Amodei (Anthropic Policy)
        21,  # Hinton (ruft zu Regulierung auf)
        23,  # Suleyman (Co-Autor "The Coming Wave")
        57,  # Russell (CHAI, Regulierungsberatung)
        62,  # Bengio (UN-Panel, Moratorium)
        73,  # Leike (Safety-Regulierung)
        86,  # Navrina Singh (Credo AI: responsible AI)
    ],

    # Regulierung contra: Kritisch gegenueber KI-Regulierung
    "haltung_regcon": [
        20,  # LeCun (gegen Ueberregulierung, open-source)
        22,  # Andrew Ng (gegen uebertriebene Safety-Rhetorik)
        24,  # Andreessen (Techno-Optimist Manifest, gegen Regulierung)
        32,  # Khosla (Regulierung bremst Innovation)
        49,  # Horowitz (a16z, gegen overreach)
    ],

    # --- GENDER (F5e) ---
    "gender_frauen": [
        14,  # Lisa Su
        17,  # Daniela Amodei
        18,  # Fei-Fei Li
        26,  # Mira Murati
        69,  # Niki Parmar
        80,  # May Habib
        83,  # Daphne Koller
        86,  # Navrina Singh
        87,  # Sarah Guo
        99,  # Dorsa Sadigh
    ],

    # Maenner: Alle ausser Frauen-Gruppe (wird dynamisch berechnet)
    "gender_maenner": "ALLE_MINUS_FRAUEN",
}

# Personen, die in kein Rollen-Topf gefallen sind (politisch, sonstige)
# 19 Jeff Dean (Chief Scientist Google - Grenzfall CEO/Tech)
# 36 David Sacks (AI Czar White House)
# 37 Sriram Krishnan (AI Policy Advisor)
# 44 Jakub Pachocki (CTO OpenAI)
# 45 Mark Chen (SVP Research OpenAI)
# 47 Craig Federighi (SVP Apple)
# 56 Mike Krieger (Head of Product Anthropic)
# 70 Nat Friedman (VP Product Meta)
# 71 Daniel Gross (Superintendent AI Meta)
# 73 Jan Leike (Head of Safety Anthropic)
# 74-79, 88-89, 91, 93, 97-98, 100 (diverse Mitgruender/Tech-Leads)
# -> Diese Personen sind in "Alle"-Toepfen enthalten,
#    aber nicht in den Rollen-Toepfen.

# ============================================================
# TOPF-KATALOG
# ============================================================
# Jeder Eintrag definiert einen Topf durch Filter-Parameter.
# "persons": Liste von IDs, "all", oder Gruppenname
# "modus": "AH" (Aussagen+Handlungen), "A" (nur Aussagen), "H" (nur Handlungen)
# "years": None (alle), (start, end) Tupel, oder einzelnes Jahr
# "frage": Zugeordnete Forschungsfrage
# "beschreibung": Kurzbeschreibung fuer Dokumentation
# "special": Optionaler Sonderfilter

TOPF_KATALOG = {
    # ============ KOLLEKTIV (3) ============
    "GA_ges_AH": {
        "persons": "all",
        "modus": "AH",
        "years": None,
        "frage": "F1a",
        "beschreibung": "Kollektiv-Weltbild aller 100, Aussagen + Handlungen",
    },
    "GA_ges_A": {
        "persons": "all",
        "modus": "A",
        "years": None,
        "frage": "F3a",
        "beschreibung": "Kollektiv nur Aussagen (fuer Kongruenz-Analyse)",
    },
    "GA_ges_H": {
        "persons": "all",
        "modus": "H",
        "years": None,
        "frage": "F3a",
        "beschreibung": "Kollektiv nur Handlungen (fuer Kongruenz-Analyse)",
    },

    # ============ TOP 10 (1) ============
    "T10_ges_AH": {
        "persons": "top10",
        "modus": "AH",
        "years": None,
        "frage": "F1b",
        "beschreibung": "Weltbild der Top 10 (maechtigste KI-Persoenlichkeiten)",
    },

    # ============ KERNUEBERZEUGUNGEN (1) ============
    "HOM_haeuf_A": {
        "persons": "all",
        "modus": "A",
        "years": None,
        "frage": "F1c",
        "beschreibung": "Haeufig wiederholte Aussagen (Kernueberzeugungen)",
        "special": "haeufig",
    },

    # ============ JAHRESTOEPFE (17) ============
    **{
        f"GA_{y}_AH": {
            "persons": "all",
            "modus": "AH",
            "years": (str(y), str(y)),
            "frage": "F2a",
            "beschreibung": f"Jahrestopf {y}, alle Personen",
        }
        for y in range(2010, 2027)
    },

    # ============ EPOCHEN (4) ============
    "GA_10-16_AH": {
        "persons": "all",
        "modus": "AH",
        "years": ("2010", "2016"),
        "frage": "F2b",
        "beschreibung": "Epoche: Fruehphase KI (2010-2016)",
    },
    "GA_16-22_AH": {
        "persons": "all",
        "modus": "AH",
        "years": ("2016", "2022"),
        "frage": "F2b",
        "beschreibung": "Epoche: Aufstieg (2016-2022)",
    },
    "GA_23-26_AH": {
        "persons": "all",
        "modus": "AH",
        "years": ("2023", "2026"),
        "frage": "F2b",
        "beschreibung": "Epoche: Post-ChatGPT (2023-2026)",
    },
    "GA_10-26_AH": {
        "persons": "all",
        "modus": "AH",
        "years": ("2010", "2026"),
        "frage": "F2b",
        "beschreibung": "Epoche: Gesamtzeitraum (Referenz)",
    },

    # ============ KONGRUENZ (2) ============
    "KG_kons_AH": {
        "persons": "all",
        "modus": "AH",
        "years": None,
        "frage": "F3c",
        "beschreibung": "Konsistente Personen (Sagen = Handeln)",
        "special": "kongruenz_konsistent",
    },
    "KG_wider_AH": {
        "persons": "all",
        "modus": "AH",
        "years": None,
        "frage": "F3c",
        "beschreibung": "Widerspruch-Personen (Sagen != Handeln)",
        "special": "kongruenz_widerspruch",
    },

    # ============ GRUPPEN: ROLLEN (4) ============
    "GR_ceo_AH": {
        "persons": "rolle_ceo",
        "modus": "AH",
        "years": None,
        "frage": "F5a",
        "beschreibung": "CEOs grosser Unternehmen",
    },
    "GR_akad_AH": {
        "persons": "rolle_akad",
        "modus": "AH",
        "years": None,
        "frage": "F5a",
        "beschreibung": "Akademiker/Professoren",
    },
    "GR_inv_AH": {
        "persons": "rolle_inv",
        "modus": "AH",
        "years": None,
        "frage": "F5a",
        "beschreibung": "Investoren/VC",
    },
    "GR_gru_AH": {
        "persons": "rolle_gru",
        "modus": "AH",
        "years": None,
        "frage": "F5a",
        "beschreibung": "Startup-Gruender/Tech-Leads",
    },

    # ============ GRUPPEN: FIRMEN (3) ============
    "GF_anthropic_AH": {
        "persons": "firma_anthropic",
        "modus": "AH",
        "years": None,
        "frage": "F5d",
        "beschreibung": "Anthropic-Team",
    },
    "GF_openai_AH": {
        "persons": "firma_openai",
        "modus": "AH",
        "years": None,
        "frage": "F5d",
        "beschreibung": "OpenAI-Team",
    },
    "GF_google_AH": {
        "persons": "firma_google_dm",
        "modus": "AH",
        "years": None,
        "frage": "F5d",
        "beschreibung": "Google/DeepMind-Team",
    },

    # ============ GRUPPEN: HALTUNG (6) ============
    "GH_open_AH": {
        "persons": "haltung_open",
        "modus": "AH",
        "years": None,
        "frage": "F5b",
        "beschreibung": "Open-Source-Befuerworter",
    },
    "GH_closed_AH": {
        "persons": "haltung_closed",
        "modus": "AH",
        "years": None,
        "frage": "F5b",
        "beschreibung": "Closed-Source-Vertreter",
    },
    "GH_risk_AH": {
        "persons": "haltung_risk",
        "modus": "AH",
        "years": None,
        "frage": "F5c",
        "beschreibung": "Risiko-Warner",
    },
    "GH_speed_AH": {
        "persons": "haltung_speed",
        "modus": "AH",
        "years": None,
        "frage": "F5c",
        "beschreibung": "Beschleuniger/Accelerationists",
    },
    "GH_regpro_AH": {
        "persons": "haltung_regpro",
        "modus": "AH",
        "years": None,
        "frage": "F5f",
        "beschreibung": "Regulierungs-Befuerworter",
    },
    "GH_regcon_AH": {
        "persons": "haltung_regcon",
        "modus": "AH",
        "years": None,
        "frage": "F5f",
        "beschreibung": "Regulierungs-Kritiker",
    },

    # ============ GRUPPEN: GENDER (2) ============
    "GD_frauen_AH": {
        "persons": "gender_frauen",
        "modus": "AH",
        "years": None,
        "frage": "F5e",
        "beschreibung": "Frauen in der KI-Elite",
    },
    "GD_maenner_AH": {
        "persons": "gender_maenner",
        "modus": "AH",
        "years": None,
        "frage": "F5e",
        "beschreibung": "Maenner in der KI-Elite",
    },
}

# Batch-Definitionen fuer --batch
BATCHES = {
    "kern": ["GA_ges_AH", "GA_ges_A", "GA_ges_H", "T10_ges_AH", "HOM_haeuf_A"],
    "zeit": [f"GA_{y}_AH" for y in range(2010, 2027)],
    "epochen": ["GA_10-16_AH", "GA_16-22_AH", "GA_23-26_AH", "GA_10-26_AH"],
    "kongruenz": ["KG_kons_AH", "KG_wider_AH"],
    "gruppen_rollen": ["GR_ceo_AH", "GR_akad_AH", "GR_inv_AH", "GR_gru_AH"],
    "gruppen_firmen": ["GF_anthropic_AH", "GF_openai_AH", "GF_google_AH"],
    "gruppen_haltung": ["GH_open_AH", "GH_closed_AH", "GH_risk_AH",
                         "GH_speed_AH", "GH_regpro_AH", "GH_regcon_AH"],
    "gruppen_gender": ["GD_frauen_AH", "GD_maenner_AH"],
    "gruppen": [],  # wird unten befuellt
    "alle": [],     # wird unten befuellt
}
BATCHES["gruppen"] = (BATCHES["gruppen_rollen"] + BATCHES["gruppen_firmen"] +
                       BATCHES["gruppen_haltung"] + BATCHES["gruppen_gender"])
BATCHES["alle"] = list(TOPF_KATALOG.keys())


# ============================================================
# KERN-FUNKTIONEN
# ============================================================

def resolve_person_ids(conn, persons_spec):
    """Loest eine Personen-Spezifikation in eine Liste von IDs auf."""
    if persons_spec == "all":
        c = conn.cursor()
        c.execute("SELECT id FROM personen ORDER BY id")
        return [row[0] for row in c.fetchall()]

    if isinstance(persons_spec, list):
        return persons_spec

    if isinstance(persons_spec, str):
        if persons_spec in GRUPPEN:
            val = GRUPPEN[persons_spec]
            if val == "ALLE_MINUS_FRAUEN":
                all_ids = resolve_person_ids(conn, "all")
                frauen = set(GRUPPEN["gender_frauen"])
                return [pid for pid in all_ids if pid not in frauen]
            return val
        raise ValueError(f"Unbekannte Gruppe: {persons_spec}")

    return persons_spec


def query_aussagen(conn, person_ids, year_start=None, year_end=None):
    """Fragt Aussagen ab (nur einschluss=1)."""
    c = conn.cursor()
    placeholders = ",".join("?" * len(person_ids))
    sql = f"""
        SELECT a.id, a.aussage_text, a.datum_aussage, a.kontext, a.modus
        FROM aussagen a
        WHERE a.person_id IN ({placeholders})
          AND a.einschluss = 1
    """
    params = list(person_ids)

    if year_start and year_end:
        sql += " AND SUBSTR(a.datum_aussage, 1, 4) >= ? AND SUBSTR(a.datum_aussage, 1, 4) <= ?"
        params.extend([year_start, year_end])

    sql += " ORDER BY a.datum_aussage, a.id"
    c.execute(sql, params)
    return c.fetchall()


def query_handlungen(conn, person_ids, year_start=None, year_end=None):
    """Fragt Handlungen ab."""
    c = conn.cursor()
    placeholders = ",".join("?" * len(person_ids))
    sql = f"""
        SELECT h.id, h.handlung_typ, h.beschreibung, h.datum_handlung, h.betrag_usd
        FROM handlungen h
        WHERE h.person_id IN ({placeholders})
    """
    params = list(person_ids)

    if year_start and year_end:
        sql += " AND SUBSTR(h.datum_handlung, 1, 4) >= ? AND SUBSTR(h.datum_handlung, 1, 4) <= ?"
        params.extend([year_start, year_end])

    sql += " ORDER BY h.datum_handlung, h.id"
    c.execute(sql, params)
    return c.fetchall()


def query_haeufige_aussagen(conn, person_ids, min_personen_anteil=0.75,
                             min_primary_cats=2):
    """
    Findet 'haeufig wiederholte' Aussagen (Kernueberzeugungen):
    1. Identifiziere primaere Kategorien, die >= 75% aller Personen abdecken
    2. Waehle Aussagen, die >= 2 dieser universellen Kategorien tragen
    -> Ergebnis: Thematisch dichte Aussagen zu universellen Themen
    """
    c = conn.cursor()
    total_persons = len(person_ids)
    min_persons = int(total_persons * min_personen_anteil)

    placeholders = ",".join("?" * len(person_ids))

    # Schritt 1: Universelle Kategorien finden (>= 75% Personen-Abdeckung)
    c.execute(f"""
        SELECT ak.kategorie_id, COUNT(DISTINCT a.person_id) as n_persons
        FROM aussagen_kategorien ak
        JOIN aussagen a ON a.id = ak.aussage_id
        JOIN kategorien k ON k.id = ak.kategorie_id
        WHERE a.person_id IN ({placeholders})
          AND a.einschluss = 1
          AND k.typ = 'primaer'
        GROUP BY ak.kategorie_id
        HAVING n_persons >= ?
    """, list(person_ids) + [min_persons])
    frequent_categories = [row[0] for row in c.fetchall()]

    if not frequent_categories:
        return []

    # Schritt 2: Aussagen mit >= 2 universellen Primaerkategorien
    cat_placeholders = ",".join("?" * len(frequent_categories))
    c.execute(f"""
        SELECT a.id, a.aussage_text, a.datum_aussage, a.kontext, a.modus
        FROM aussagen a
        WHERE a.person_id IN ({placeholders})
          AND a.einschluss = 1
          AND (
            SELECT COUNT(DISTINCT ak.kategorie_id)
            FROM aussagen_kategorien ak
            WHERE ak.aussage_id = a.id
              AND ak.kategorie_id IN ({cat_placeholders})
          ) >= ?
        ORDER BY a.datum_aussage, a.id
    """, list(person_ids) + frequent_categories + [min_primary_cats])
    return c.fetchall()


def stratified_sample(items, max_items, date_index):
    """
    Stratifiziertes Random-Sampling: Erhalt die Jahresverteilung.
    items: Liste von DB-Rows
    max_items: Maximale Anzahl
    date_index: Index des Datums-Feldes in der Row
    """
    import random
    random.seed(42)  # Reproduzierbar

    if len(items) <= max_items:
        return items

    # Nach Jahr gruppieren
    by_year = {}
    for item in items:
        date_val = item[date_index] if item[date_index] else "0000"
        year = date_val[:4]
        by_year.setdefault(year, []).append(item)

    # Proportional samplen
    result = []
    for year in sorted(by_year.keys()):
        year_items = by_year[year]
        n_sample = max(1, round(len(year_items) / len(items) * max_items))
        if n_sample >= len(year_items):
            result.extend(year_items)
        else:
            result.extend(random.sample(year_items, n_sample))

    # Falls zu viele durch Rundung, trimmen
    if len(result) > max_items:
        result = random.sample(result, max_items)
    result.sort(key=lambda x: (x[date_index] or "0000", x[0]))
    return result


# Maximal ~300 Aussagen und ~200 Handlungen pro Topf fuer Prompt-Tauglichkeit
MAX_AUSSAGEN_FOR_PROMPT = 300
MAX_HANDLUNGEN_FOR_PROMPT = 200


def format_topf(aussagen, handlungen, topf_id, beschreibung, modus):
    """Formatiert einen Topf als geblindeten Text."""
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Header
    lines.append("=" * 72)
    lines.append(f"SYNTHESEEINHEIT: {topf_id}")
    lines.append(f"Beschreibung: {beschreibung}")
    lines.append(f"Generiert: {now}")
    lines.append("=" * 72)
    lines.append("")

    # Statistik
    n_a = len(aussagen) if aussagen else 0
    n_h = len(handlungen) if handlungen else 0
    lines.append(f"Datenpunkte: {n_a} Aussagen + {n_h} Handlungen = {n_a + n_h} gesamt")

    if aussagen:
        dates = [a[2] for a in aussagen if a[2]]
        if dates:
            lines.append(f"Zeitraum Aussagen: {min(dates)} bis {max(dates)}")

    if handlungen:
        dates = [h[3] for h in handlungen if h[3]]
        if dates:
            lines.append(f"Zeitraum Handlungen: {min(dates)} bis {max(dates)}")

    lines.append("")
    lines.append("HINWEIS: Alle identifizierenden Informationen wurden entfernt.")
    lines.append("Die Daten stammen von einer oder mehreren Personen.")
    lines.append("Versuchen Sie NICHT, die Identitaet zu rekonstruieren.")
    lines.append("")

    # Aussagen
    if modus in ("AH", "A") and aussagen:
        lines.append("-" * 72)
        lines.append(f"AUSSAGEN ({n_a} Stueck)")
        lines.append("-" * 72)
        lines.append("")

        for i, row in enumerate(aussagen, 1):
            _, text, datum, kontext, modus_a = row
            bt = blind_text(text)
            bk = blind_text(kontext) if kontext else ""
            datum_str = datum if datum else "unbekannt"
            lines.append(f"[A{i:03d}] ({datum_str}, {modus_a})")
            lines.append(f'  "{bt}"')
            if bk:
                lines.append(f"  Kontext: {bk}")
            lines.append("")

    # Handlungen
    if modus in ("AH", "H") and handlungen:
        lines.append("-" * 72)
        lines.append(f"HANDLUNGEN ({n_h} Stueck)")
        lines.append("-" * 72)
        lines.append("")

        for i, row in enumerate(handlungen, 1):
            _, typ, beschr, datum, betrag = row
            bb = blind_text(beschr)
            datum_str = datum if datum else "unbekannt"
            betrag_str = f" (${betrag:,.0f})" if betrag else ""
            lines.append(f"[H{i:03d}] ({datum_str}) [{typ}]{betrag_str}")
            lines.append(f"  {bb}")
            lines.append("")

    return "\n".join(lines)


def generate_topf(conn, topf_id, topf_def, dry_run=False, sampled=False):
    """Generiert einen einzelnen Topf und speichert ihn.
    sampled=True: Erstellt eine gesampelte Version fuer grosse Toepfe.
    """
    persons_spec = topf_def["persons"]
    modus = topf_def["modus"]
    years = topf_def.get("years")
    special = topf_def.get("special")
    beschreibung = topf_def["beschreibung"]

    # Personen aufloesen
    person_ids = resolve_person_ids(conn, persons_spec)

    # Zeitfilter
    year_start = years[0] if years else None
    year_end = years[1] if years else None

    # Spezialfilter
    if special == "kongruenz_konsistent":
        print(f"  WARNUNG: {topf_id} verwendet Platzhalter-Filter (Phase 4.05 ausstehend)")
        return None

    if special == "kongruenz_widerspruch":
        print(f"  WARNUNG: {topf_id} verwendet Platzhalter-Filter (Phase 4.05 ausstehend)")
        return None

    # Daten abfragen
    aussagen = None
    handlungen = None

    if modus in ("AH", "A"):
        if special == "haeufig":
            aussagen = query_haeufige_aussagen(conn, person_ids)
        else:
            aussagen = query_aussagen(conn, person_ids, year_start, year_end)

    if modus in ("AH", "H"):
        handlungen = query_handlungen(conn, person_ids, year_start, year_end)

    # Datenpunkte zaehlen (vor Sampling)
    n_a_full = len(aussagen) if aussagen else 0
    n_h_full = len(handlungen) if handlungen else 0
    total_full = n_a_full + n_h_full

    if total_full < MIN_DATAPOINTS:
        print(f"  SKIP: {topf_id} hat nur {total_full} DPs (Minimum: {MIN_DATAPOINTS})")
        return {"topf_id": topf_id, "status": "skip_k2", "n_a": n_a_full, "n_h": n_h_full}

    if dry_run:
        return {"topf_id": topf_id, "status": "ok", "n_a": n_a_full, "n_h": n_h_full}

    # Sampling fuer grosse Toepfe (wenn angefordert)
    sampled_flag = False
    if sampled and (n_a_full > MAX_AUSSAGEN_FOR_PROMPT or n_h_full > MAX_HANDLUNGEN_FOR_PROMPT):
        if aussagen and len(aussagen) > MAX_AUSSAGEN_FOR_PROMPT:
            aussagen = stratified_sample(aussagen, MAX_AUSSAGEN_FOR_PROMPT, 2)  # date_index=2
            sampled_flag = True
        if handlungen and len(handlungen) > MAX_HANDLUNGEN_FOR_PROMPT:
            handlungen = stratified_sample(handlungen, MAX_HANDLUNGEN_FOR_PROMPT, 3)  # date_index=3
            sampled_flag = True

    n_a = len(aussagen) if aussagen else 0
    n_h = len(handlungen) if handlungen else 0

    # Beschreibung anpassen falls gesampled
    if sampled_flag:
        beschreibung += f" [SAMPLED: {n_a}/{n_a_full}A + {n_h}/{n_h_full}H, stratifiziert nach Jahr, seed=42]"

    # Formatieren und speichern
    text = format_topf(aussagen, handlungen, topf_id, beschreibung, modus)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    suffix = "_sampled" if sampled_flag else ""
    outpath = os.path.join(OUTPUT_DIR, f"topf_{topf_id}{suffix}.txt")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(text)

    return {"topf_id": topf_id, "status": "ok", "n_a": n_a, "n_h": n_h,
            "n_a_full": n_a_full, "n_h_full": n_h_full,
            "sampled": sampled_flag, "path": outpath}


# ============================================================
# CLI-INTERFACE
# ============================================================

def cmd_list():
    """Listet alle vordefinierten Toepfe auf."""
    print(f"\n{'ID':<20} {'Modus':<5} {'Frage':<6} {'Beschreibung'}")
    print("-" * 80)
    for topf_id, topf_def in sorted(TOPF_KATALOG.items()):
        special = " *" if topf_def.get("special") else ""
        print(f"{topf_id:<20} {topf_def['modus']:<5} {topf_def['frage']:<6} "
              f"{topf_def['beschreibung']}{special}")
    print(f"\nGesamt: {len(TOPF_KATALOG)} Toepfe")
    print("* = Sonderfilter (haeufig, kongruenz)")
    print(f"\nBatches: {', '.join(BATCHES.keys())}")


def cmd_stats(conn):
    """Zeigt Statistiken fuer alle Toepfe (ohne Generierung)."""
    print(f"\n{'ID':<20} {'A':>5} {'H':>5} {'Sum':>5} {'Status':<10} {'Frage'}")
    print("-" * 65)
    total_ok = 0
    total_skip = 0
    for topf_id, topf_def in sorted(TOPF_KATALOG.items()):
        result = generate_topf(conn, topf_id, topf_def, dry_run=True)
        if result is None:
            print(f"{topf_id:<20} {'?':>5} {'?':>5} {'?':>5} {'TODO':<10} {topf_def['frage']}")
            continue
        status = "OK" if result["status"] == "ok" else "SKIP(K2)"
        total = result["n_a"] + result["n_h"]
        if result["status"] == "ok":
            total_ok += 1
        else:
            total_skip += 1
        print(f"{topf_id:<20} {result['n_a']:>5} {result['n_h']:>5} {total:>5} "
              f"{status:<10} {topf_def['frage']}")
    print(f"\nOK: {total_ok}, Skip: {total_skip}, TODO: "
          f"{len(TOPF_KATALOG) - total_ok - total_skip}")


def cmd_validate(conn):
    """Validiert alle Toepfe gegen K2 und andere Kriterien."""
    print("\nValidierung aller Toepfe...\n")
    issues = []
    for topf_id, topf_def in sorted(TOPF_KATALOG.items()):
        result = generate_topf(conn, topf_id, topf_def, dry_run=True)
        if result is None:
            issues.append(f"  {topf_id}: Spezialfilter nicht implementiert")
        elif result["status"] == "skip_k2":
            total = result["n_a"] + result["n_h"]
            issues.append(f"  {topf_id}: Nur {total} DPs (K2: min {MIN_DATAPOINTS})")

    if issues:
        print(f"PROBLEME ({len(issues)}):")
        for issue in issues:
            print(issue)
    else:
        print("Alle Toepfe OK!")


def cmd_generate(conn, topf_ids, sampled=False):
    """Generiert eine Liste von Toepfen."""
    mode_str = " (mit Sampling fuer grosse Toepfe)" if sampled else ""
    print(f"\nGeneriere {len(topf_ids)} Toepfe{mode_str}...\n")
    results = {"ok": 0, "skip": 0, "error": 0, "sampled": 0}

    for topf_id in topf_ids:
        if topf_id not in TOPF_KATALOG:
            print(f"  FEHLER: Topf '{topf_id}' nicht im Katalog")
            results["error"] += 1
            continue

        result = generate_topf(conn, topf_id, TOPF_KATALOG[topf_id], sampled=sampled)
        if result is None:
            results["error"] += 1
        elif result["status"] == "ok":
            total = result["n_a"] + result["n_h"]
            s = " [SAMPLED]" if result.get("sampled") else ""
            print(f"  OK: {topf_id} ({result['n_a']}A + {result['n_h']}H = {total}){s}")
            results["ok"] += 1
            if result.get("sampled"):
                results["sampled"] += 1
        else:
            results["skip"] += 1

    print(f"\nErgebnis: {results['ok']} generiert ({results['sampled']} gesampled), "
          f"{results['skip']} uebersprungen (K2), {results['error']} Fehler")
    print(f"Output-Verzeichnis: {OUTPUT_DIR}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python generate_topf.py --list              Alle Toepfe auflisten")
        print("  python generate_topf.py --stats             Statistiken (ohne Generierung)")
        print("  python generate_topf.py --validate          Validierung (K2 etc.)")
        print("  python generate_topf.py --all               Alle Toepfe generieren")
        print("  python generate_topf.py --batch <name>      Batch generieren")
        print(f"    Batches: {', '.join(BATCHES.keys())}")
        print("  python generate_topf.py <TOPF_ID>           Einzelnen Topf generieren")
        print("  python generate_topf.py <ID1> <ID2> ...     Mehrere Toepfe generieren")
        sys.exit(1)

    if sys.argv[1] == "--list":
        cmd_list()
        return

    conn = sqlite3.connect(DB_PATH)

    try:
        # --sampled Flag erkennen
        sampled = "--sampled" in sys.argv
        args = [a for a in sys.argv[1:] if a != "--sampled"]

        if args[0] == "--stats":
            cmd_stats(conn)
        elif args[0] == "--validate":
            cmd_validate(conn)
        elif args[0] == "--all":
            cmd_generate(conn, list(TOPF_KATALOG.keys()), sampled=sampled)
        elif args[0] == "--batch":
            batch_name = args[1] if len(args) > 1 else "alle"
            if batch_name not in BATCHES:
                print(f"Unbekannter Batch: {batch_name}")
                print(f"Verfuegbar: {', '.join(BATCHES.keys())}")
                sys.exit(1)
            cmd_generate(conn, BATCHES[batch_name], sampled=sampled)
        else:
            topf_ids = args
            cmd_generate(conn, topf_ids, sampled=sampled)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
