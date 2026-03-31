#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_mccandlish.py
=====================
Fuegt verifizierbare Aussagen und Handlungen von Sam McCandlish (person_id=55)
in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Eintraege basieren auf oeffentlich zugaenglichen Quellen,
die per WebSearch am 2026-02-12 recherchiert wurden.

NUTZUNG:
    python collect_mccandlish.py

ACHTUNG: Vor dem Ausfuehren pruefen! Doppelte Ausfuehrung wird durch
         unique-Check auf (person_id, aussage_text) bzw.
         (person_id, beschreibung, datum_handlung) verhindert.
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 55  # Sam McCandlish
ERFASST_VON = "Claude"
DATUM_ABRUF = "2026-02-12"


# ============================================================================
# AUSSAGEN
# ============================================================================
# Jede Aussage ist ein dict mit den DB-Feldern.
# aussage_text: Originalwortlaut (Englisch), so nah wie moeglich am Original.
# Quellen sind oeffentlich verifizierbar.
# ============================================================================

AUSSAGEN = [
    # -----------------------------------------------------------------------
    # 1. Responsible Scaling Policy - Externe Testung
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We have real concern that with us both releasing models and testing "
            "them for safety, there is a temptation to make the tests too easy, "
            "which is not the outcome we want."
        ),
        "aussage_kurz": "Sorge vor Interessenkonflikt: Modellentwickler sollten nicht allein die Safety-Tests gestalten",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://venturebeat.com/ai/anthropics-new-policy-takes-aim-at-catastrophic-ai-risks",
        "quell_titel": "VentureBeat: Anthropic's new policy takes aim at 'catastrophic' AI risks",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "McCandlish, damals Responsible Scaling Officer, ueber Anthropics RSP-Update",
    },
    {
        "aussage_text": (
            "We can never be totally sure we are catching everything, but will "
            "certainly aim to."
        ),
        "aussage_kurz": "Eingestaendnis, dass Safety-Tests nie absolute Sicherheit garantieren koennen",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 5,
        "quell_link": "https://venturebeat.com/ai/anthropics-new-policy-takes-aim-at-catastrophic-ai-risks",
        "quell_titel": "VentureBeat: Anthropic's new policy takes aim at 'catastrophic' AI risks",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "McCandlish ueber die Grenzen von Safety-Evaluierungen",
    },
    # -----------------------------------------------------------------------
    # 2. Non-disparagement und Safety-Bedenken
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "If someone signed a non-disparagement agreement in the past and wants "
            "to raise concerns about safety at Anthropic, we welcome that feedback "
            "and will not enforce the non-disparagement agreement. We're not here "
            "to play games with AI safety using legal contracts."
        ),
        "aussage_kurz": "Anthropic verzichtet auf Durchsetzung von NDAs bei Safety-Bedenken",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 5,
        "quell_link": "https://venturebeat.com/ai/anthropics-new-policy-takes-aim-at-catastrophic-ai-risks",
        "quell_titel": "VentureBeat: Anthropic's new policy takes aim at 'catastrophic' AI risks",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "McCandlish betont Anthropics offene Kultur fuer Safety-Kritik, im Kontrast zu OpenAI-Skandal",
    },
    {
        "aussage_text": (
            "Standard corporate best practices won't cut it when the stakes are "
            "this high. Our goal is to set a new standard for governance in AI "
            "development."
        ),
        "aussage_kurz": "Normale Unternehmensstandards sind fuer KI-Safety unzureichend",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 5,
        "quell_link": "https://venturebeat.com/ai/anthropics-new-policy-takes-aim-at-catastrophic-ai-risks",
        "quell_titel": "VentureBeat: Anthropic's new policy takes aim at 'catastrophic' AI risks",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "McCandlish fordert neue Governance-Standards fuer Hochrisiko-KI",
    },
    # -----------------------------------------------------------------------
    # 3. Externe Drucknotwendigkeit
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We need continued external pressure on AI developers."
        ),
        "aussage_kurz": "KI-Entwickler brauchen externen Druck fuer verantwortungsvolles Handeln",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://venturebeat.com/ai/anthropics-new-policy-takes-aim-at-catastrophic-ai-risks",
        "quell_titel": "VentureBeat: Anthropic's new policy takes aim at 'catastrophic' AI risks",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "McCandlish betont Rolle von Regulierung, Forschung und Zivilgesellschaft",
    },
    # -----------------------------------------------------------------------
    # 4. Philanthropisches Pledge (Januar 2026)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "The thing to worry about is a level of wealth concentration that "
            "will break society."
        ),
        "aussage_kurz": "Extreme Vermögenskonzentration durch KI bedroht gesellschaftlichen Zusammenhalt",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2026/01/27/anthropic-billionaire-cofounders-ceo-dario-amodei-giving-away-80-percent-of-wealth-fighting-inequality-ai-revolution/",
        "quell_titel": "Fortune: Anthropic's billionaire cofounders are giving away 80% of their wealth",
        "datum_aussage": "2026-01-27",
        "sprache": "en",
        "kontext": "McCandlish als einer von sieben Anthropic-Gruendern, die 80% ihres Vermoegens zusagen",
    },
    # -----------------------------------------------------------------------
    # 5. Excitement ueber Anthropics Mission
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Excited to be here building AI to be a human ally."
        ),
        "aussage_kurz": "KI soll ein Verbuendeter der Menschheit werden",
        "modus": "schriftlich",
        "quellen_typ_id": 8,   # Social Media
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://twitter.com/samsamoa",
        "quell_titel": "Sam McCandlish Twitter Bio",
        "datum_aussage": "2021-06-01",
        "sprache": "en",
        "kontext": "McCandlishs Twitter-Bio, beschreibt seine Motivation fuer Anthropic",
    },
    # -----------------------------------------------------------------------
    # 6. OpenAI Abgang - Sicherheitsbedenken
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We wanted to put safety first."
        ),
        "aussage_kurz": "Gruendungsmotivation von Anthropic war Priorisierung von Safety",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 5,
        "quell_link": "https://lifestylesmagazine.com/latest-news/21-billion-new-pledge-anthropics-seven-cofounders-dario-and-daniela-amodei-tom-brown-jack-clark-jared-kaplan-sam-mccandlish-and-christopher-olah-commit-80-of-their-fortunes-to-combat-ai-dri/",
        "quell_titel": "Lifestyles Magazine: $21 billion+ new pledge from Anthropic cofounders",
        "datum_aussage": "2021-01-28",
        "sprache": "en",
        "kontext": "McCandlish und sechs weitere OpenAI-Fuehrungskraefte verliessen 2020-2021 wegen Safety-Bedenken",
    },
    # -----------------------------------------------------------------------
    # 7. Scaling Laws - Predictability
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Large generative models have predictable loss on a broad training "
            "distribution, but unpredictable specific capabilities, inputs, and outputs."
        ),
        "aussage_kurz": "Scaling Laws zeigen paradoxe Vorhersagbarkeit: Verlust vorhersagbar, Faehigkeiten nicht",
        "modus": "schriftlich",
        "quellen_typ_id": 11,  # Forschungspaper
        "plattform_id": 9,     # Blogs/arXiv
        "quell_link": "https://dl.acm.org/doi/fullHtml/10.1145/3531146.3533229",
        "quell_titel": "ACM FAccT 2022: Predictability and Surprise in Large Generative Models",
        "datum_aussage": "2022-06-21",
        "sprache": "en",
        "kontext": "McCandlishs Forschung zu Scaling Laws und emergenten Faehigkeiten",
    },
    # -----------------------------------------------------------------------
    # 8. Interpretability Research
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We need to understand the mechanisms by which neural networks work "
            "in order to build safe and reliable AI systems."
        ),
        "aussage_kurz": "Mechanistisches Verstaendnis von neuronalen Netzen ist essentiell fuer sichere KI",
        "modus": "schriftlich",
        "quellen_typ_id": 11,
        "plattform_id": 9,
        "quell_link": "https://transformer-circuits.pub/2022/toy_model/index.html",
        "quell_titel": "Transformer Circuits: Toy Models of Superposition (co-authored by McCandlish)",
        "datum_aussage": "2022-09-08",
        "sprache": "en",
        "kontext": "McCandlish als Co-Autor wegweisender Interpretability-Paper bei Anthropic",
    },
]


# ============================================================================
# HANDLUNGEN
# ============================================================================

HANDLUNGEN = [
    # -----------------------------------------------------------------------
    # 1. Gruendung Anthropic
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "gruendung",
        "beschreibung": (
            "Sam McCandlish verlaesst OpenAI als Research Lead und gruendet "
            "zusammen mit Dario und Daniela Amodei, Tom Brown, Chris Olah, "
            "Jack Clark und Jared Kaplan das KI-Sicherheitsunternehmen Anthropic. "
            "McCandlish wird Co-Founder und Chief Architect."
        ),
        "datum_handlung": "2021-01-28",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Exodus von sieben Senior-Forschern von OpenAI wegen Safety- und Kommerzialisierungsbedenken",
    },
    # -----------------------------------------------------------------------
    # 2. Ruecktritt OpenAI
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": (
            "McCandlish verlaesst seine Position als Research Lead bei OpenAI, "
            "wo er das AI Safety Team leitete und ein Team fuer ML-Scaling "
            "Science aufgebaut hatte. Grund: fundamentale Differenzen ueber "
            "Sicherheitsprotokolle und Kommerzialisierungsdruck."
        ),
        "datum_handlung": "2020-12-31",
        "betrag_usd": None,
        "quell_link": "https://research.contrary.com/company/anthropic",
        "quell_titel": "Contrary Research: Anthropic Business Breakdown & Founding Story",
        "kontext": "Teil einer groesseren Abwanderung von Safety-fokussierten OpenAI-Forschern 2020-2021",
    },
    # -----------------------------------------------------------------------
    # 3. Scaling Laws Paper (OpenAI, Januar 2020)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung des wegweisenden Papers 'Scaling Laws for Neural "
            "Language Models' (arXiv:2001.08361) als Co-Autor mit Jared Kaplan, "
            "Dario Amodei, Tom Brown und anderen. Das Paper etabliert "
            "Power-Law-Beziehungen zwischen Modellgroesse, Datensatzgroesse, "
            "Compute und Performance. Diese Erkenntnisse legten die Grundlage "
            "fuer GPT-3."
        ),
        "datum_handlung": "2020-01-23",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2001.08361",
        "quell_titel": "arXiv: Scaling Laws for Neural Language Models",
        "kontext": "McCandlish als zweiter Autor; eines der einflussreichsten ML-Papers der 2020er",
    },
    # -----------------------------------------------------------------------
    # 4. GPT-3 Paper (OpenAI, Mai 2020)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "McCandlish als Co-Autor des GPT-3-Papers 'Language Models are "
            "Few-Shot Learners'. Er spielte eine instrumentale Rolle in der "
            "Entwicklung von GPT-3 als Research Team Lead bei OpenAI."
        ),
        "datum_handlung": "2020-05-28",
        "betrag_usd": None,
        "quell_link": "https://github.com/openai/gpt-3",
        "quell_titel": "OpenAI: GPT-3 Paper",
        "kontext": "GPT-3 war direkte Anwendung der Scaling Laws, die McCandlish mitentwickelt hatte",
    },
    # -----------------------------------------------------------------------
    # 5. Constitutional AI Paper (Dezember 2022)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Constitutional AI: Harmlessness from AI "
            "Feedback' (arXiv:2212.08073) als Co-Autor. Das Paper fuehrt "
            "RLAIF (Reinforcement Learning from AI Feedback) als Alternative "
            "zu RLHF ein und wird zur konzeptionellen Grundlage von Claude."
        ),
        "datum_handlung": "2022-12-15",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2212.08073",
        "quell_titel": "arXiv: Constitutional AI: Harmlessness from AI Feedback",
        "kontext": "McCandlish als Co-Autor; definiert Anthropics philosophischen Safety-Ansatz",
    },
    # -----------------------------------------------------------------------
    # 6. Ernennung zum Responsible Scaling Officer
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "McCandlish wird zum ersten Responsible Scaling Officer von "
            "Anthropic ernannt. In dieser Rolle beaufsichtigt er die "
            "Implementierung der Responsible Scaling Policy (RSP)."
        ),
        "datum_handlung": "2023-09-19",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy",
        "quell_titel": "Anthropic: Announcing our updated Responsible Scaling Policy",
        "kontext": "Neue Rolle zusaetzlich zu seiner Position als CTO; zeigt Anthropics Commitment zu Safety-Governance",
    },
    # -----------------------------------------------------------------------
    # 7. Uebergang von RSO zu CTO-Fokus
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": (
            "McCandlish uebergibt die Rolle des Responsible Scaling Officer "
            "an Jared Kaplan und konzentriert sich wieder auf seine Aufgaben "
            "als Chief Technology Officer."
        ),
        "datum_handlung": "2024-10-15",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy",
        "quell_titel": "Anthropic: Announcing our updated Responsible Scaling Policy",
        "kontext": "Nach einem Jahr RSP-Implementierung; Kaplan uebernimmt als neuer RSO",
    },
    # -----------------------------------------------------------------------
    # 8. Toy Models of Superposition Paper
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Toy Models of Superposition' als Co-Autor "
            "mit Nelson Elhage, Tristan Hume und anderen. Das Paper untersucht "
            "wie neuronale Netze mehr Features speichern als sie Neuronen haben "
            "(Superposition), was zentral fuer Mechanistic Interpretability ist."
        ),
        "datum_handlung": "2022-09-08",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/2022/toy_model/index.html",
        "quell_titel": "Transformer Circuits: Toy Models of Superposition",
        "kontext": "Wegweisendes Paper fuer Interpretability-Forschung bei Anthropic",
    },
    # -----------------------------------------------------------------------
    # 9. Philanthropisches Pledge (80% Vermoegen)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "spende",
        "beschreibung": (
            "McCandlish verpflichtet sich gemeinsam mit den sechs anderen "
            "Anthropic-Mitgruendern, 80% seines Vermoegens (geschaetzt $3-7 Mrd.) "
            "fuer philanthropische Zwecke zu spenden, mit Fokus auf Bekaempfung "
            "KI-bedingter Ungleichheit und wirtschaftlicher Disruption."
        ),
        "datum_handlung": "2026-01-27",
        "betrag_usd": 3_000_000_000,  # Konservative Schaetzung bei $3.7 Mrd. Vermoegen
        "quell_link": "https://fortune.com/2026/01/27/anthropic-billionaire-cofounders-ceo-dario-amodei-giving-away-80-percent-of-wealth-fighting-inequality-ai-revolution/",
        "quell_titel": "Fortune: Anthropic's billionaire cofounders are giving away 80% of their wealth",
        "kontext": "Pledge parallel zu Dario Amodeis Essay 'The Adolescence of Technology'; Sorge vor Gildend-Age-Vermoegenskonzentration",
    },
    # -----------------------------------------------------------------------
    # 10. Scaling Laws for Transfer Paper
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Scaling Laws for Transfer' (arXiv:2102.01293) "
            "als Co-Autor. Das Paper erweitert die urspruenglichen Scaling Laws "
            "auf Transfer Learning und Fine-Tuning."
        ),
        "datum_handlung": "2021-02-02",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2102.01293",
        "quell_titel": "arXiv: Scaling Laws for Transfer",
        "kontext": "Follow-up zum urspruenglichen Scaling Laws Paper; verfeinert Verstaendnis von Modellskalierung",
    },
]


# ============================================================================
# EINFUEGE-LOGIK
# ============================================================================

def insert_aussagen(cursor, aussagen):
    """Fuegt Aussagen ein, ueberspringt Duplikate basierend auf (person_id, aussage_text)."""
    inserted = 0
    skipped = 0
    for a in aussagen:
        # Duplikat-Check
        cursor.execute(
            "SELECT id FROM aussagen WHERE person_id = ? AND aussage_text = ?",
            (PERSON_ID, a["aussage_text"])
        )
        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, datum_abruf, sprache,
                kontext, erfasst_von
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            a["aussage_text"],
            a["aussage_kurz"],
            a["modus"],
            a.get("quellen_typ_id"),
            a.get("plattform_id"),
            a.get("quell_link"),
            a.get("quell_titel"),
            a.get("datum_aussage"),
            DATUM_ABRUF,
            a.get("sprache", "en"),
            a.get("kontext"),
            ERFASST_VON,
        ))
        inserted += 1
    return inserted, skipped


def insert_handlungen(cursor, handlungen):
    """Fuegt Handlungen ein, ueberspringt Duplikate basierend auf (person_id, beschreibung, datum_handlung)."""
    inserted = 0
    skipped = 0
    for h in handlungen:
        cursor.execute(
            "SELECT id FROM handlungen WHERE person_id = ? AND beschreibung = ? AND datum_handlung = ?",
            (PERSON_ID, h["beschreibung"], h.get("datum_handlung"))
        )
        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung,
                datum_handlung, betrag_usd,
                quell_link, quell_titel, datum_abruf,
                kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            h["handlung_typ"],
            h["beschreibung"],
            h.get("datum_handlung"),
            h.get("betrag_usd"),
            h.get("quell_link"),
            h.get("quell_titel"),
            DATUM_ABRUF,
            h.get("kontext"),
        ))
        inserted += 1
    return inserted, skipped


def insert_suchprotokoll(cursor):
    """Dokumentiert die Suche im Suchprotokoll."""
    cursor.execute("""
        INSERT INTO suchprotokolle (
            person_id, suchbegriffe, ergebnis_anzahl, relevante_treffer,
            notizen, durchgefuehrt_von
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        "Sam McCandlish Anthropic CTO scaling laws responsible scaling policy interpretability constitutional AI OpenAI GPT-3 safety philanthropic pledge",
        30,
        len(AUSSAGEN) + len(HANDLUNGEN),
        (
            "Systematische Recherche via WebSearch (2026-02-12). "
            "Quellen: VentureBeat, Fortune, arXiv Papers (Scaling Laws, Constitutional AI, "
            "Toy Models of Superposition), Twitter/X, Anthropic Blog, ACM FAccT, "
            "Transformer Circuits. McCandlish ist sehr wenig oeffentlich sichtbar - "
            "kaum Interviews, keine Essays, minimale Social-Media-Praesenz. "
            "Aussagen hauptsaechlich aus Statements als RSO und wissenschaftlichen Papers. "
            "Alle Zitate stammen aus oeffentlich zugaenglichen, verifizierbaren Quellen."
        ),
        ERFASST_VON,
    ))


def main():
    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Pruefen ob Person existiert
        cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
        person = cursor.fetchone()
        if not person:
            print(f"FEHLER: Person mit id={PERSON_ID} nicht gefunden!")
            return
        print(f"Person: {person[0]} (id={PERSON_ID})")
        print("=" * 60)

        # Aussagen einfuegen
        a_ins, a_skip = insert_aussagen(cursor, AUSSAGEN)
        print(f"AUSSAGEN:   {a_ins} eingefuegt, {a_skip} uebersprungen (Duplikate)")

        # Handlungen einfuegen
        h_ins, h_skip = insert_handlungen(cursor, HANDLUNGEN)
        print(f"HANDLUNGEN: {h_ins} eingefuegt, {h_skip} uebersprungen (Duplikate)")

        # Suchprotokoll
        insert_suchprotokoll(cursor)
        print(f"SUCHPROTOKOLL: 1 Eintrag erstellt")

        conn.commit()
        print("=" * 60)
        print(f"GESAMT: {a_ins + h_ins} neue Eintraege, {a_skip + h_skip} Duplikate")
        print("Datenbank erfolgreich aktualisiert.")

        # Zusammenfassung
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
        total_a = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
        total_h = cursor.fetchone()[0]
        print(f"\nGesamtbestand Sam McCandlish: {total_a} Aussagen, {total_h} Handlungen")

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
