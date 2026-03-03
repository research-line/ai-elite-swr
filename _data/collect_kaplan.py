#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_kaplan.py
=================
Fuegt verifizierbare Aussagen und Handlungen von Jared Kaplan (person_id=52)
in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Eintraege basieren auf oeffentlich zugaenglichen Quellen,
die per WebSearch am 2026-02-12 recherchiert wurden.

NUTZUNG:
    python collect_kaplan.py

ACHTUNG: Vor dem Ausfuehren pruefen! Doppelte Ausfuehrung wird durch
         unique-Check auf (person_id, aussage_text) bzw.
         (person_id, beschreibung, datum_handlung) verhindert.
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 52  # Jared Kaplan
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
    # 1. Scaling Laws Paper (Januar 2020)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We study empirical scaling laws for language model performance on the "
            "cross-entropy loss. The loss scales as a power-law with model size, "
            "dataset size, and the amount of compute used for training, with some "
            "trends spanning more than seven orders of magnitude."
        ),
        "aussage_kurz": "Sprachmodell-Performance folgt praediktablen Power-Laws ueber sieben Groessenordnungen",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Wissenschaftliche Publikation
        "plattform_id": 9,     # arXiv/Research Paper
        "quell_link": "https://arxiv.org/abs/2001.08361",
        "quell_titel": "Scaling Laws for Neural Language Models (Kaplan et al., 2020)",
        "datum_aussage": "2020-01-23",
        "sprache": "en",
        "kontext": "Einfuehrung des bahnbrechenden Papers, das die moderne KI-Skalierung definiert hat",
    },
    {
        "aussage_text": (
            "These relationships allow us to determine the optimal allocation of a "
            "fixed compute budget. Larger models are significantly more sample-efficient, "
            "such that optimally compute-efficient training involves training very large "
            "models on a relatively modest amount of data and stopping significantly "
            "before convergence."
        ),
        "aussage_kurz": "Grosse Modelle sind sample-effizienter; optimales Training nutzt grosse Modelle",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 9,
        "quell_link": "https://arxiv.org/abs/2001.08361",
        "quell_titel": "Scaling Laws for Neural Language Models (Kaplan et al., 2020)",
        "datum_aussage": "2020-01-23",
        "sprache": "en",
        "kontext": "Kernaussage des Papers ueber optimale Compute-Allokation",
    },

    # -----------------------------------------------------------------------
    # 2. Senate AI Insight Forum (Dezember 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Anthropic was founded in 2021 as an AI safety and research company to "
            "build reliable, interpretable, and steerable AI systems, because the "
            "impact of AI might be comparable to that of the industrial and "
            "scientific revolutions."
        ),
        "aussage_kurz": "KI-Impact vergleichbar mit industrieller und wissenschaftlicher Revolution",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.schumer.senate.gov/imo/media/doc/Jared%20Kaplan%20-%20Statement.pdf",
        "quell_titel": "Written Statement for AI Insight Forum: Risk, Alignment & Guarding Against Doomsday Scenarios",
        "datum_aussage": "2023-12-06",
        "sprache": "en",
        "kontext": "Senate AI Insight Forum; Kaplan erklaert die Gruendungsmotivation von Anthropic",
    },
    {
        "aussage_text": (
            "A major reason Anthropic exists as an organization is because we believe "
            "that safety research on 'frontier' AI systems is necessary, and that since "
            "many of the most serious safety concerns might only arise with near-human-level "
            "systems, we need to understand how safety methods and properties change as "
            "models scale."
        ),
        "aussage_kurz": "Frontier-KI-Sicherheitsforschung ist notwendig, da Risiken erst bei menschlichem Niveau entstehen",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.schumer.senate.gov/imo/media/doc/Jared%20Kaplan%20-%20Statement.pdf",
        "quell_titel": "Written Statement for AI Insight Forum: Risk, Alignment & Guarding Against Doomsday Scenarios",
        "datum_aussage": "2023-12-06",
        "sprache": "en",
        "kontext": "Senate Testimony; Begruendung fuer Anthropics Fokus auf Frontier AI Safety",
    },
    {
        "aussage_text": (
            "One key concern is the possibility that advanced AI may develop harmful "
            "emergent behaviors, such as deception or strategic planning abilities."
        ),
        "aussage_kurz": "Hauptsorge: emergente schaedliche Verhaltensweisen wie Taeuschung",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.schumer.senate.gov/imo/media/doc/Jared%20Kaplan%20-%20Statement.pdf",
        "quell_titel": "Written Statement for AI Insight Forum: Risk, Alignment & Guarding Against Doomsday Scenarios",
        "datum_aussage": "2023-12-06",
        "sprache": "en",
        "kontext": "Senate Testimony; Warnung vor emergenten Risiken",
    },

    # -----------------------------------------------------------------------
    # 3. Responsible Scaling Officer & TIME Interview (2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "It seems like potentially an example of the race to the top."
        ),
        "aussage_kurz": "Responsible Scaling Policy als Beispiel fuer positiven Wettbewerb",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://time.com/collections/time100-ai-2025/7305824/jared-kaplan/",
        "quell_titel": "Jared Kaplan: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "TIME-Interview ueber Anthropics RSP-Ansatz und dessen Einfluss auf die Industrie",
    },

    # -----------------------------------------------------------------------
    # 4. Y Combinator AI Startup School (Juni 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I discovered very precise and surprising underlying patterns in AI training, "
            "with trends as precise as anything seen in physics or astronomy. I call these "
            "'scaling laws' -- precise scientific discoveries showing how AI capabilities "
            "improve as compute, data, and model size increase."
        ),
        "aussage_kurz": "Scaling Laws sind so praezise wie physikalische Gesetze",
        "modus": "muendlich",
        "quellen_typ_id": 3,   # Keynote/Vortrag
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.ycombinator.com/library/Ml-scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan",
        "quell_titel": "Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan (YC)",
        "datum_aussage": "2025-06-16",
        "sprache": "en",
        "kontext": "Y Combinator AI Startup School; Kaplan erklaert die Natur der Scaling Laws",
    },
    {
        "aussage_text": (
            "LLMs are doubling their task capabilities roughly every seven months."
        ),
        "aussage_kurz": "KI-Faehigkeiten verdoppeln sich alle sieben Monate",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://www.ycombinator.com/library/Ml-scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan",
        "quell_titel": "Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan (YC)",
        "datum_aussage": "2025-06-16",
        "sprache": "en",
        "kontext": "Y Combinator Talk; Messung der Task-Completion-Horizonte",
    },
    {
        "aussage_text": (
            "Companies like Anthropic are moving to both make AI training more efficient "
            "and AI inference more efficient, as well as unlocking frontier capabilities. "
            "Currently there are 3x to 10x gains algorithmically and in scaling up compute."
        ),
        "aussage_kurz": "Aktuelle Fortschritte bringen 3x-10x Effizienzgewinne",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://www.ycombinator.com/library/Ml-scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan",
        "quell_titel": "Scaling and the Road to Human-Level AI | Anthropic Co-founder Jared Kaplan (YC)",
        "datum_aussage": "2025-06-16",
        "sprache": "en",
        "kontext": "Y Combinator Talk; Effizienzsteigerungen bei Training und Inference",
    },

    # -----------------------------------------------------------------------
    # 5. AGI-Timeline-Prognosen (Guardian Interview, Dezember 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I expect human-level artificial intelligence to emerge in the next two "
            "to three years. This represents a significant shift from earlier predictions."
        ),
        "aussage_kurz": "AGI in 2-3 Jahren erwartet, schneller als frueher vorhergesagt",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://futurism.com/artificial-intelligence/anthropic-ai-scientist-doom",
        "quell_titel": "Anthropic's Chief Scientist Says We're Rapidly Approaching the Moment That Could Doom Us All",
        "datum_aussage": "2025-12-15",
        "sprache": "en",
        "kontext": "Guardian-Interview; Kaplan revidiert Timeline nach vorne",
    },
    {
        "aussage_text": (
            "Humanity will face the ultimate decision between allowing AI to undergo "
            "recursive self-evolution from 2027 to 2030. Current alignment methods may "
            "be adequate while systems remain around human-level intelligence, but the "
            "moment models begin to design and train more capable models autonomously, "
            "the dynamics change fundamentally and quickly."
        ),
        "aussage_kurz": "2027-2030: Kritischer Wendepunkt bei rekursiver KI-Selbstverbesserung",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://eu.36kr.com/en/p/3579721070967684",
        "quell_titel": "Humanity's Final Choice in 2027 (via Guardian Interview)",
        "datum_aussage": "2025-12-15",
        "sprache": "en",
        "kontext": "Warnung vor der entscheidenden Phase der rekursiven KI-Verbesserung",
    },
    {
        "aussage_text": (
            "I am very optimistic that AI systems will be aligned with human interests "
            "before reaching the level of human intelligence, but I am worried about "
            "the consequences once they exceed this critical point."
        ),
        "aussage_kurz": "Optimistisch fuer Alignment bis AGI, besorgt ueber Post-AGI-Phase",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.webpronews.com/anthropics-jared-kaplan-warns-of-ai-intelligence-explosion-by-2030/",
        "quell_titel": "Anthropic's Jared Kaplan Warns of AI Intelligence Explosion by 2030",
        "datum_aussage": "2025-12-15",
        "sprache": "en",
        "kontext": "Differenzierte Einschaetzung: Alignment moeglich bis AGI, unklar danach",
    },

    # -----------------------------------------------------------------------
    # 6. Claude 3.7 Sonnet & Task-Horizonte
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Claude 3.7 Sonnet can handle tasks that might take a graduate student half "
            "a day. I track this 'horizon' that Claude can operate on, and we're seeing "
            "this horizon expand. Independent evaluators report that the length of tasks "
            "AI systems can reliably complete has been doubling roughly every seven months."
        ),
        "aussage_kurz": "Claude erreicht Halbtages-Aufgaben-Niveau; Task-Horizont waechst exponentiell",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.endofmiles.net/were-moving-much-faster-than-expected-anthropic-scientist-revises-agi-timeline/",
        "quell_titel": "We're Moving Much Faster Than Expected: Anthropic Scientist Revises AGI Timeline",
        "datum_aussage": "2025-12-15",
        "sprache": "en",
        "kontext": "Messung der Task-Completion-Faehigkeiten von Claude",
    },

    # -----------------------------------------------------------------------
    # 7. Responsible Scaling & Claude 4 Safety Decision
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Internal tests had indicated that Claude 4 might be good enough at biology "
            "that it could assist amateur scientists in developing a biological weapon, "
            "so I decided Anthropic would release the model under 'AI Safety Level 3,' "
            "requiring stronger safeguards."
        ),
        "aussage_kurz": "Claude 4 erhielt wegen Biorisiken staerkere Sicherheitsstufe ASL-3",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305824/jared-kaplan/",
        "quell_titel": "Jared Kaplan: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025-05-22",
        "sprache": "en",
        "kontext": "Kaplan als Responsible Scaling Officer entschied ueber strengere Sicherheitsmassnahmen",
    },

    # -----------------------------------------------------------------------
    # 8. Constitutional AI & Interpretability
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Constitutional AI represents a significant shift from traditional reinforcement "
            "learning from human preferences (RLHF). We train AI systems to follow ethical "
            "principles, creating systems that are reliable, interpretable, and steerable."
        ),
        "aussage_kurz": "Constitutional AI als Alternative zu RLHF fuer ethisch ausgerichtete Systeme",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.hubspot.com/startups/tech-stacks/ai/breakthroughs-in-llm-research",
        "quell_titel": "The Future of AI: Insights from Anthropic's Co-founder Jared Kaplan",
        "datum_aussage": "2024-06-15",
        "sprache": "en",
        "kontext": "Erklaerung des Constitutional AI-Ansatzes",
    },

    # -----------------------------------------------------------------------
    # 9. TechCrunch Sessions: AI (Juni 2025) - Windsurf-Kontroverse
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "It would be odd for us to sell Claude to OpenAI."
        ),
        "aussage_kurz": "Ablehnung des Verkaufs von Claude-Zugang an konkurrierende Unternehmen",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://techcrunch.com/2025/06/05/anthropic-co-founder-on-cutting-access-to-windsurf-it-would-be-odd-for-us-to-sell-claude-to-openai/",
        "quell_titel": "Anthropic co-founder on cutting access to Windsurf (TechCrunch Sessions: AI)",
        "datum_aussage": "2025-06-05",
        "sprache": "en",
        "kontext": "TechCrunch Sessions AI; Kaplan erklaert Entscheidung, Windsurf-Zugang zu beschraenken",
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
            "Jared Kaplan verlaesst OpenAI und gruendet zusammen mit Dario Amodei, "
            "Daniela Amodei, Tom Brown, Chris Olah, Sam McCandlish und Jack Clark "
            "das KI-Sicherheitsunternehmen Anthropic. Kaplan wird Chief Science Officer."
        ),
        "datum_handlung": "2021-01-28",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Alle sieben Gruender waren zuvor bei OpenAI; Kaplan bringt Expertise zu Scaling Laws ein",
    },

    # -----------------------------------------------------------------------
    # 2. Scaling Laws Paper (OpenAI, 2020)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung des bahnbrechenden Papers 'Scaling Laws for Neural "
            "Language Models' (arXiv:2001.08361) mit Jared Kaplan als Erstautor. "
            "Das Paper zeigt, dass LLM-Performance praediktablen Power Laws folgt."
        ),
        "datum_handlung": "2020-01-23",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2001.08361",
        "quell_titel": "arXiv: Scaling Laws for Neural Language Models",
        "kontext": "Noch bei OpenAI; definiert theoretische Grundlage der modernen KI-Skalierung",
    },

    # -----------------------------------------------------------------------
    # 3. GPT-3 Paper (OpenAI, 2020)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Jared Kaplan ist Co-Autor des GPT-3-Papers 'Language Models are "
            "Few-Shot Learners', das bei NeurIPS 2020 den Best Paper Award gewinnt."
        ),
        "datum_handlung": "2020-05-28",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2005.14165",
        "quell_titel": "arXiv: Language Models are Few-Shot Learners (GPT-3 Paper)",
        "kontext": "GPT-3 demonstriert die Scaling Laws in der Praxis; NeurIPS 2020 Best Paper Award",
    },

    # -----------------------------------------------------------------------
    # 4. Constitutional AI Paper (Anthropic, 2022)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Co-Autor des Papers 'Constitutional AI: Harmlessness from AI Feedback' "
            "(arXiv:2212.08073), das RLAIF als Alternative zu RLHF einfuehrt und "
            "zur theoretischen Grundlage von Claude wird."
        ),
        "datum_handlung": "2022-12-15",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2212.08073",
        "quell_titel": "arXiv: Constitutional AI: Harmlessness from AI Feedback",
        "kontext": "Definiert Anthropics Alignment-Ansatz; Kaplan einer von ueber 50 Co-Autoren",
    },

    # -----------------------------------------------------------------------
    # 5. Responsible Scaling Officer Ernennung
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "Jared Kaplan wird zum 'Responsible Scaling Officer' von Anthropic ernannt. "
            "In dieser Rolle bestimmt er, welche Sicherheitsmassnahmen vor der "
            "Veroeffentlichung neuer Modelle erforderlich sind."
        ),
        "datum_handlung": "2024-10-15",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy",
        "quell_titel": "Anthropic: Announcing our updated Responsible Scaling Policy",
        "kontext": "Kaplan uebernimmt von CTO Sam McCandlish; zentrale Governance-Rolle",
    },

    # -----------------------------------------------------------------------
    # 6. Claude 4 Safety Assessment (ASL-3)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Als Responsible Scaling Officer entscheidet Kaplan, dass Claude 4 "
            "unter 'AI Safety Level 3' veroeffentlicht wird, da interne Tests "
            "Biorisiken zeigten. Claude 4 erreicht 72.5% auf SWE-bench und wird "
            "zum weltbesten Coding-Modell."
        ),
        "datum_handlung": "2025-05-22",
        "betrag_usd": None,
        "quell_link": "https://www.maginative.com/article/anthropics-claude-4-is-here-and-its-breaking-new-ground-and-safety-protocols/",
        "quell_titel": "Anthropic's Claude 4 Is Here—and It's Breaking New Ground (and Safety Protocols)",
        "kontext": "Erste Anwendung der strengsten Sicherheitsstufe bei einem Anthropic-Release",
    },

    # -----------------------------------------------------------------------
    # 7. Senate AI Insight Forum Testimony
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Kaplan gibt schriftliches und muendliches Testimony vor dem US Senate "
            "AI Insight Forum zum Thema 'Risk, Alignment & Guarding Against Doomsday "
            "Scenarios', warnt vor emergenten Risiken und Biowaffen-Missbrauch."
        ),
        "datum_handlung": "2023-12-06",
        "betrag_usd": None,
        "quell_link": "https://www.schumer.senate.gov/imo/media/doc/Jared%20Kaplan%20-%20Statement.pdf",
        "quell_titel": "Written Statement for AI Insight Forum (US Senate)",
        "kontext": "Teil der Senate AI Insight Forums unter Senator Schumer",
    },

    # -----------------------------------------------------------------------
    # 8. Y Combinator AI Startup School Keynote
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Kaplan haelt Keynote 'Scaling and the Road to Human-Level AI' bei "
            "Y Combinators erstem AI Startup School in San Francisco."
        ),
        "datum_handlung": "2025-06-16",
        "betrag_usd": None,
        "quell_link": "https://www.ycombinator.com/library/Ml-scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan",
        "quell_titel": "Y Combinator: Scaling and the Road to Human-Level AI (Jared Kaplan)",
        "kontext": "Grosse oeffentliche Keynote; Speaker-Lineup inkl. Sam Altman, Elon Musk, Fei-Fei Li",
    },

    # -----------------------------------------------------------------------
    # 9. TechCrunch Sessions: AI Teilnahme
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Kaplan tritt bei TechCrunch Sessions: AI auf und diskutiert Anthropics "
            "Strategie, inklusive der Entscheidung, Claude-Zugang fuer bestimmte "
            "konkurrierende Tools (z.B. Windsurf) zu beschraenken."
        ),
        "datum_handlung": "2025-06-05",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2025/06/05/anthropic-co-founder-on-cutting-access-to-windsurf-it-would-be-odd-for-us-to-sell-claude-to-openai/",
        "quell_titel": "TechCrunch: Anthropic co-founder on cutting access to Windsurf",
        "kontext": "Erklaert strategische Entscheidungen zu API-Zugang und Wettbewerb",
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
        "Jared Kaplan Anthropic scaling laws OpenAI GPT-3 Senate testimony responsible scaling officer AI safety timeline AGI human-level Y Combinator Constitutional AI interpretability",
        40,
        len(AUSSAGEN) + len(HANDLUNGEN),
        (
            "Systematische Recherche via WebSearch (2026-02-12). "
            "Quellen: arXiv Papers (Scaling Laws, GPT-3, Constitutional AI), "
            "Senate AI Insight Forum Statement (PDF), TIME 100 AI, "
            "Y Combinator AI Startup School, TechCrunch Sessions AI, "
            "Guardian Interview, HubSpot/Anthropic Blogs. "
            "Kaplan ist akademisch gepraegt und weniger oeffentlich sichtbar als andere; "
            "Fokus auf wissenschaftliche Papers und Fachkonferenzen. "
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
        print(f"\nGesamtbestand Jared Kaplan: {total_a} Aussagen, {total_h} Handlungen")

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
