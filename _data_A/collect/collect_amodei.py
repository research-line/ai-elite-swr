#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_amodei.py
=================
Fuegt verifizierbare Aussagen und Handlungen von Dario Amodei (person_id=9)
in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Eintraege basieren auf oeffentlich zugaenglichen Quellen,
die per WebSearch am 2026-02-11 recherchiert wurden.

NUTZUNG:
    python collect_amodei.py

ACHTUNG: Vor dem Ausfuehren pruefen! Doppelte Ausfuehrung wird durch
         unique-Check auf (person_id, aussage_text) bzw.
         (person_id, beschreibung, datum_handlung) verhindert.
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 9  # Dario Amodei
ERFASST_VON = "Claude"
DATUM_ABRUF = "2026-02-11"


# ============================================================================
# AUSSAGEN
# ============================================================================
# Jede Aussage ist ein dict mit den DB-Feldern.
# aussage_text: Originalwortlaut (Englisch), so nah wie moeglich am Original.
# Quellen sind oeffentlich verifizierbar.
# ============================================================================

AUSSAGEN = [
    # -----------------------------------------------------------------------
    # 1. "Machines of Loving Grace" Essay (Oktober 2024)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I think and talk a lot about the risks of powerful AI. "
            "In fact, one of my main reasons for focusing on risks is that "
            "they're the only thing standing between us and what I see as "
            "a fundamentally positive future."
        ),
        "aussage_kurz": "Risikofokus dient dem Ziel einer positiven Zukunft",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://www.darioamodei.com/essay/machines-of-loving-grace",
        "quell_titel": "Machines of Loving Grace (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2024-10-01",
        "sprache": "en",
        "kontext": "Einleitung seines 14.000-Woerter-Essays ueber die positiven Potenziale von KI",
    },
    {
        "aussage_text": (
            "Most people are underestimating just how radical the upside of AI "
            "could be, just as I think most people are underestimating how bad "
            "the risks could be."
        ),
        "aussage_kurz": "Sowohl Chancen als auch Risiken von KI werden unterschaetzt",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/machines-of-loving-grace",
        "quell_titel": "Machines of Loving Grace (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2024-10-01",
        "sprache": "en",
        "kontext": "Essay-Abschnitt ueber die Einschaetzung des KI-Potenzials",
    },
    {
        "aussage_text": (
            "I'll refer to this as the 'compressed 21st century': the idea that "
            "after powerful AI is developed, we will in a few years make all the "
            "progress in biology and medicine that we would have made in the "
            "whole 21st century."
        ),
        "aussage_kurz": "KI komprimiert ein Jahrhundert biomedizinischen Fortschritts auf wenige Jahre",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/machines-of-loving-grace",
        "quell_titel": "Machines of Loving Grace (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2024-10-01",
        "sprache": "en",
        "kontext": "Zentrales Konzept des Essays: KI beschleunigt wissenschaftlichen Fortschritt dramatisch",
    },
    {
        "aussage_text": (
            "I think it is critical to have a genuinely inspiring vision of the "
            "future. [...] there has to be something we're fighting for, some "
            "positive-sum outcome where everyone is better off. [...] Fear is one "
            "kind of motivator, but it's not enough: we need hope as well."
        ),
        "aussage_kurz": "Neben Risikowarnungen braucht es eine positive Zukunftsvision",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/machines-of-loving-grace",
        "quell_titel": "Machines of Loving Grace (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2024-10-01",
        "sprache": "en",
        "kontext": "Abschliessende Reflexion des Essays ueber die Rolle von Hoffnung vs. Angst",
    },

    # -----------------------------------------------------------------------
    # 2. US Senate Testimony (Juli 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "The single most important thing to understand about AI is how "
            "fast it is moving."
        ),
        "aussage_kurz": "Die Geschwindigkeit der KI-Entwicklung ist das Wichtigste",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf",
        "quell_titel": "Written Testimony of Dario Amodei, Ph.D., US Senate Judiciary Subcommittee",
        "datum_aussage": "2023-07-26",
        "sprache": "en",
        "kontext": "Schriftliche Aussage vor dem Senate Judiciary Subcommittee on Privacy, Technology and the Law",
    },
    {
        "aussage_text": (
            "Anthropic is concerned that AI could empower a much larger set of "
            "actors to misuse biology. Today, certain steps in bioweapons "
            "production involve knowledge that can't be found on Google or in "
            "textbooks. [...] a straightforward extrapolation of today's systems "
            "to those we expect to see in 2 to 3 years suggests a substantial "
            "risk that AI systems will be able to fill in all the missing pieces, "
            "enabling many more actors to carry out large-scale biological attacks."
        ),
        "aussage_kurz": "KI koennte in 2-3 Jahren Biowaffen-Wissen fuer viele zugaenglich machen",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf",
        "quell_titel": "Written Testimony of Dario Amodei, Ph.D., US Senate Judiciary Subcommittee",
        "datum_aussage": "2023-07-26",
        "sprache": "en",
        "kontext": "Warnung vor mittelfristigen Biorisiken durch KI, vor US-Senatoren",
    },

    # -----------------------------------------------------------------------
    # 3. AI Safety Summit Bletchley Park (November 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "It is entirely possible for something to go catastrophically wrong "
            "on the scale of human civilisation."
        ),
        "aussage_kurz": "Katastrophale KI-Risiken auf zivilisatorischer Ebene sind moeglich",
        "modus": "muendlich",
        "quellen_typ_id": 3,   # Keynote/Vortrag
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.anthropic.com/news/uk-ai-safety-summit",
        "quell_titel": "Dario Amodei's prepared remarks, UK AI Safety Summit, Bletchley Park",
        "datum_aussage": "2023-11-01",
        "sprache": "en",
        "kontext": "Rede bei Bletchley Park AI Safety Summit; Vorstellung der Responsible Scaling Policy",
    },

    # -----------------------------------------------------------------------
    # 4. "The Adolescence of Technology" Essay (Januar 2026)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I believe we are entering a rite of passage, both turbulent and "
            "inevitable, which will test who we are as a species. Humanity is "
            "about to be handed almost unimaginable power, and it is deeply "
            "unclear whether our social, political, and technological systems "
            "possess the maturity to wield it."
        ),
        "aussage_kurz": "Die Menschheit wird durch KI auf eine beispiellose Probe gestellt",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/the-adolescence-of-technology",
        "quell_titel": "The Adolescence of Technology (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2026-01-26",
        "sprache": "en",
        "kontext": "Einleitung seines 20.000-Woerter-Essays ueber KI-Risiken fuer Sicherheit, Wirtschaft und Demokratie",
    },
    {
        "aussage_text": (
            "We could summarize this as a 'country of geniuses in a datacenter.'"
        ),
        "aussage_kurz": "Leistungsfaehige KI als 'Land von Genies in einem Rechenzentrum'",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/the-adolescence-of-technology",
        "quell_titel": "The Adolescence of Technology (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2026-01-26",
        "sprache": "en",
        "kontext": "Metapher fuer die Faehigkeiten zukuenftiger KI-Systeme, zentral in seiner Argumentation",
    },
    {
        "aussage_text": (
            "During the peak of worries about AI risk in 2023-2024, some of "
            "the least sensible voices rose to the top, often through "
            "sensationalistic social media accounts. These voices used "
            "off-putting language reminiscent of religion or science fiction, "
            "and called for extreme actions without having the evidence that "
            "would justify them."
        ),
        "aussage_kurz": "Kritik an sensationalistischen AI-Doom-Stimmen 2023-2024",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/the-adolescence-of-technology",
        "quell_titel": "The Adolescence of Technology (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2026-01-26",
        "sprache": "en",
        "kontext": "Abgrenzung von extremen Doomer-Positionen, Plaidoyer fuer sachlichen Umgang mit KI-Risiken",
    },
    {
        "aussage_text": (
            "The lesson is that we need to discuss and address risks in a "
            "realistic, pragmatic manner: sober, fact-based, and well equipped "
            "to survive changing tides."
        ),
        "aussage_kurz": "KI-Risikodiskussion muss nuechtern und faktenbasiert sein",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/essay/the-adolescence-of-technology",
        "quell_titel": "The Adolescence of Technology (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2026-01-26",
        "sprache": "en",
        "kontext": "Forderung nach pragmatischem Ansatz bei KI-Governance",
    },

    # -----------------------------------------------------------------------
    # 5. "The Urgency of Interpretability" Essay (April 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "People outside the field are often surprised and alarmed to learn "
            "that we do not understand how our own AI creations work. They are "
            "right to be concerned: this lack of understanding is essentially "
            "unprecedented in the history of technology."
        ),
        "aussage_kurz": "Das Unverstaendnis ueber die Funktionsweise von KI ist beispiellos",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/post/the-urgency-of-interpretability",
        "quell_titel": "The Urgency of Interpretability (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2025-04-24",
        "sprache": "en",
        "kontext": "Essay ueber die Dringlichkeit, KI-Systeme interpretierbar zu machen",
    },
    {
        "aussage_text": (
            "We are thus in a race between interpretability and model intelligence."
        ),
        "aussage_kurz": "Es gibt ein Wettrennen zwischen Interpretierbarkeit und Modellintelligenz",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/post/the-urgency-of-interpretability",
        "quell_titel": "The Urgency of Interpretability (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2025-04-24",
        "sprache": "en",
        "kontext": "Kernthese des Essays: Interpretierbarkeit muss mit der Modellentwicklung Schritt halten",
    },
    {
        "aussage_text": (
            "The progress of the underlying technology is inexorable, driven by "
            "forces too powerful to stop, but the way in which it happens -- the "
            "order in which things are built, the applications we choose, and the "
            "details of how it is rolled out to society -- are eminently possible "
            "to change. [...] We can't stop the bus, but we can steer it."
        ),
        "aussage_kurz": "Technologischer Fortschritt ist unaufhaltsam, aber steuerbar",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.darioamodei.com/post/the-urgency-of-interpretability",
        "quell_titel": "The Urgency of Interpretability (Dario Amodei, persoenlicher Blog)",
        "datum_aussage": "2025-04-24",
        "sprache": "en",
        "kontext": "Pragmatische Position: KI-Entwicklung nicht aufhaltbar, aber gestaltbar",
    },

    # -----------------------------------------------------------------------
    # 6. 60 Minutes / CBS Interview (November 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I think I'm deeply uncomfortable with these decisions being made "
            "by a few companies, by a few people."
        ),
        "aussage_kurz": "Unbehagen darueber, dass wenige Tech-Fuehrungskraefte KI-Zukunft bestimmen",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://fortune.com/2025/11/17/anthropic-ceo-dario-amodei-ai-safety-risks-regulation/",
        "quell_titel": "Anthropic CEO Dario Amodei is 'deeply uncomfortable' with tech leaders determining AI's future (Fortune, via CBS 60 Minutes)",
        "datum_aussage": "2025-11-16",
        "sprache": "en",
        "kontext": "CBS 60 Minutes Interview mit Anderson Cooper; Forderung nach staerkerer Regulierung",
    },
    {
        "aussage_text": (
            "AI is advancing too head-spinningly fast. I believe that these "
            "systems could change the world, fundamentally, within two years; "
            "in 10 years, all bets are off."
        ),
        "aussage_kurz": "KI koennte die Welt in zwei Jahren grundlegend veraendern",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2025/11/17/anthropic-ceo-dario-amodei-ai-safety-risks-regulation/",
        "quell_titel": "Anthropic CEO Dario Amodei is 'deeply uncomfortable' (Fortune, via CBS 60 Minutes)",
        "datum_aussage": "2025-11-16",
        "sprache": "en",
        "kontext": "CBS 60 Minutes Interview, Einschaetzung des Tempos der KI-Entwicklung",
    },

    # -----------------------------------------------------------------------
    # 7. CNN Interview mit Anderson Cooper (Mai 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "AI is starting to get better than humans at almost all intellectual "
            "tasks, and we're going to collectively, as a society, grapple with it."
        ),
        "aussage_kurz": "KI uebertrifft Menschen bald bei fast allen intellektuellen Aufgaben",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2025/05/29/tech/ai-anthropic-ceo-dario-amodei-unemployment",
        "quell_titel": "CNN: Why this leading AI CEO is warning the tech could cause mass unemployment",
        "datum_aussage": "2025-05-29",
        "sprache": "en",
        "kontext": "CNN-Interview ueber Arbeitsmarktauswirkungen von KI",
    },
    {
        "aussage_text": (
            "If AI creates huge total wealth, a lot of that will, by default, "
            "go to the AI companies and less to ordinary people."
        ),
        "aussage_kurz": "KI-generierter Reichtum fliesst standardmaessig zu den Unternehmen",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2025/05/29/tech/ai-anthropic-ceo-dario-amodei-unemployment",
        "quell_titel": "CNN: Why this leading AI CEO is warning the tech could cause mass unemployment",
        "datum_aussage": "2025-05-29",
        "sprache": "en",
        "kontext": "CNN-Interview; Amodei schlaegt Besteuerung von KI-Firmen vor",
    },
    {
        "aussage_text": (
            "It's eerie the extent to which the broader public and politicians, "
            "legislators, I don't think, are fully aware of what's going on."
        ),
        "aussage_kurz": "Oeffentlichkeit und Politiker unterschaetzen die KI-Entwicklung",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2025/05/29/tech/ai-anthropic-ceo-dario-amodei-unemployment",
        "quell_titel": "CNN: Why this leading AI CEO is warning the tech could cause mass unemployment",
        "datum_aussage": "2025-05-29",
        "sprache": "en",
        "kontext": "CNN-Interview; Amodei drueckt Frustration ueber mangelndes Bewusstsein aus",
    },

    # -----------------------------------------------------------------------
    # 8. Axios AI+ DC Summit (September 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I think there's a 25% chance that things go really, really badly."
        ),
        "aussage_kurz": "25% Wahrscheinlichkeit fuer katastrophalen Ausgang der KI-Entwicklung",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.axios.com/2025/09/17/anthropic-dario-amodei-p-doom-25-percent",
        "quell_titel": "Axios: Amodei on AI: There's a 25% chance that things go really, really badly",
        "datum_aussage": "2025-09-17",
        "sprache": "en",
        "kontext": "Axios AI+ DC Summit; Antwort auf Frage nach seinem 'p(doom)'-Wert",
    },

    # -----------------------------------------------------------------------
    # 9. Paris AI Action Summit (Februar 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We must ensure democratic societies lead in AI, and that "
            "authoritarian countries do not use it to establish global "
            "military dominance."
        ),
        "aussage_kurz": "Demokratische Gesellschaften muessen bei KI fuehren, nicht Autokratien",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 4,
        "quell_link": "https://www.anthropic.com/news/paris-ai-summit",
        "quell_titel": "Statement from Dario Amodei on the Paris AI Action Summit (Anthropic)",
        "datum_aussage": "2025-02-11",
        "sprache": "en",
        "kontext": "Offizielle Stellungnahme zum Paris AI Action Summit; Amodei nannte den Gipfel eine 'missed opportunity'",
    },

    # -----------------------------------------------------------------------
    # 10. Lex Fridman Podcast #452 (November 2024)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "As much as I am excited about the benefits of these models, and "
            "we'll talk about that if we talk about Machines of Loving Grace, "
            "I'm worried about the risks and I continue to be worried about "
            "the risks."
        ),
        "aussage_kurz": "Begeisterung ueber KI-Nutzen geht einher mit fortwaehrender Sorge ueber Risiken",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 1,     # YouTube
        "quell_link": "https://lexfridman.com/dario-amodei-transcript/",
        "quell_titel": "Lex Fridman Podcast #452: Dario Amodei on Claude, AGI & the Future of AI",
        "datum_aussage": "2024-11-11",
        "sprache": "en",
        "kontext": "5+ Stunden Podcast-Gespraech mit Lex Fridman; Amodei reflektiert ueber Chancen und Risiken",
    },

    # -----------------------------------------------------------------------
    # 11. Lex Fridman #452 - ueber OpenAI-Abgang
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "The real reason for leaving, is that it is incredibly "
            "unproductive to try and argue with someone else's vision. "
            "[...] Take some people you trust and go make your vision happen."
        ),
        "aussage_kurz": "Verliess OpenAI wegen Visions-Differenzen, nicht wegen Microsoft-Deal",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 1,
        "quell_link": "https://lexfridman.com/dario-amodei-transcript/",
        "quell_titel": "Lex Fridman Podcast #452: Dario Amodei on Claude, AGI & the Future of AI",
        "datum_aussage": "2024-11-11",
        "sprache": "en",
        "kontext": "Erklaerung seines Abgangs von OpenAI; widerspricht Narrativ ueber Microsoft als Grund",
    },

    # -----------------------------------------------------------------------
    # 12. Davos WEF (Januar 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I see a form of AI that's better than almost all humans at almost "
            "all tasks emerging in the next two or three years."
        ),
        "aussage_kurz": "KI wird in 2-3 Jahren die meisten Menschen bei fast allen Aufgaben uebertreffen",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://digitalchew.com/2025/01/23/anthropic-ceo-dario-amodei-predicts-ai-to-surpass-human-abilities-in-two-to-three-years/",
        "quell_titel": "CNBC Interview, World Economic Forum Davos 2025",
        "datum_aussage": "2025-01-23",
        "sprache": "en",
        "kontext": "Interview bei CNBC am Rande des Weltwirtschaftsforums in Davos",
    },

    # -----------------------------------------------------------------------
    # 13. NYT DealBook Summit (Dezember 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I think there are some players who are not managing that risk well "
            "or taking unwise risk. [...] There's an inherent risk when the "
            "timing of the economic value is uncertain."
        ),
        "aussage_kurz": "Einige KI-Unternehmen gehen unkluge wirtschaftliche Risiken ein",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://techcrunch.com/2025/12/04/anthropic-ceo-weighs-in-on-ai-bubble-talk-and-risk-taking-among-competitors/",
        "quell_titel": "TechCrunch: Anthropic CEO weighs in on AI bubble talk (NYT DealBook Summit)",
        "datum_aussage": "2025-12-03",
        "sprache": "en",
        "kontext": "NYT DealBook Summit; Amodei kommentiert KI-Blase und Spending-Risiken der Konkurrenz",
    },

    # -----------------------------------------------------------------------
    # 14. Dwarkesh Patel Podcast (August 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We really have very little idea what we're talking about."
        ),
        "aussage_kurz": "Eingestaendnis, dass das Verstaendnis von KI-Alignment noch sehr begrenzt ist",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.dwarkesh.com/p/dario-amodei",
        "quell_titel": "Dwarkesh Podcast: Dario Amodei - Scaling, Alignment, & AI Progress",
        "datum_aussage": "2023-08-08",
        "sprache": "en",
        "kontext": "Podcast-Gespraech ueber Alignment und Interpretierbarkeit; Demut bezueglich eigener Wissensgrenzen",
    },

    # -----------------------------------------------------------------------
    # 15. Davos WEF (Januar 2026) - Arbeitsmarkt
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "AI could make half of all entry-level white-collar jobs vanish "
            "within one to five years."
        ),
        "aussage_kurz": "50% der Einstiegspositionen im Buerobereich koennten durch KI wegfallen",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://www.cnbc.com/2026/01/27/dario-amodei-warns-ai-cause-unusually-painful-disruption-jobs.html",
        "quell_titel": "CNBC: Dario Amodei warns AI may cause 'unusually painful' disruption to jobs (Davos 2026)",
        "datum_aussage": "2026-01-27",
        "sprache": "en",
        "kontext": "Warnung am Weltwirtschaftsforum in Davos; Forderung nach staatlicher Umschulung",
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
            "Dario Amodei gruendet zusammen mit seiner Schwester Daniela Amodei "
            "und weiteren Ex-OpenAI-Forschern (u.a. Tom Brown, Chris Olah, "
            "Sam McCandlish, Jack Clark, Jared Kaplan) das KI-Sicherheitsunternehmen "
            "Anthropic als Public Benefit Corporation."
        ),
        "datum_handlung": "2021-01-28",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Abspaltung von OpenAI aufgrund von Meinungsverschiedenheiten ueber KI-Sicherheit und Unternehmensstrategie",
    },
    # -----------------------------------------------------------------------
    # 2. Series A Funding
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "investition",
        "beschreibung": (
            "Anthropic schliesst Series-A-Finanzierungsrunde ueber $124 Mio. ab, "
            "mit fruehen Investoren wie Jaan Tallinn (Skype/Kazaa) und anderen."
        ),
        "datum_handlung": "2021-05-31",
        "betrag_usd": 124_000_000,
        "quell_link": "https://www.anthropic.com/news/anthropic-raises-124-million-to-build-more-reliable-general-ai-systems",
        "quell_titel": "Anthropic: Anthropic raises $124 million",
        "kontext": "Erste groessere Finanzierungsrunde nach Gruendung",
    },
    # -----------------------------------------------------------------------
    # 3. Series B (FTX/SBF)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "investition",
        "beschreibung": (
            "Series-B-Runde ueber $580 Mio., angefuehrt von Sam Bankman-Fried "
            "(FTX/Alameda Research). Alameda allein investiert ca. $500 Mio. "
            "Die Investition wird spaeter Teil des FTX-Insolvenzverfahrens."
        ),
        "datum_handlung": "2022-04-29",
        "betrag_usd": 580_000_000,
        "quell_link": "https://www.anthropic.com/news/anthropic-raises-series-b-to-build-safe-reliable-ai",
        "quell_titel": "Anthropic: Series B announcement",
        "kontext": "Groesste Fruehphasen-Finanzierung; FTX-Kollaps Nov 2022 belastet spaeter das Investorenprofil",
    },
    # -----------------------------------------------------------------------
    # 4. Constitutional AI Paper
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung des Papers 'Constitutional AI: Harmlessness from "
            "AI Feedback' (arXiv:2212.08073). Einfuehrung von RLAIF als Alternative "
            "zu RLHF fuer harmlose KI-Systeme. Wird zum zentralen Sicherheitskonzept "
            "hinter Claude."
        ),
        "datum_handlung": "2022-12-15",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2212.08073",
        "quell_titel": "arXiv: Constitutional AI: Harmlessness from AI Feedback",
        "kontext": "Dario Amodei ist Co-Autor; Paper definiert Anthropics philosophischen Ansatz fuer KI-Sicherheit",
    },
    # -----------------------------------------------------------------------
    # 5. Claude 1 Launch
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Anthropic veroeffentlicht Claude 1 als KI-Assistenten, "
            "zunaechst nur fuer ausgewaehlte Partner zugaenglich."
        ),
        "datum_handlung": "2023-03-14",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Claude_(language_model)",
        "quell_titel": "Wikipedia: Claude (language model)",
        "kontext": "Erster oeffentlicher Produktlaunch von Anthropic; basierend auf Constitutional AI",
    },
    # -----------------------------------------------------------------------
    # 6. Series C (Google/Spark)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "investition",
        "beschreibung": (
            "Series-C-Runde ueber $450 Mio., angefuehrt von Spark Capital "
            "mit Beteiligung von Google, Salesforce Ventures und anderen. "
            "Bewertung: $4.1 Mrd."
        ),
        "datum_handlung": "2023-05-23",
        "betrag_usd": 450_000_000,
        "quell_link": "https://www.anthropic.com/news/anthropic-series-c",
        "quell_titel": "Anthropic: Anthropic Raises Series C",
        "kontext": "Erste grosse Post-FTX-Finanzierung; Google wird strategischer Partner",
    },
    # -----------------------------------------------------------------------
    # 7. Claude 2 Launch
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Anthropic veroeffentlicht Claude 2 fuer die breite Oeffentlichkeit "
            "mit signifikanten Verbesserungen bei Coding, Mathematik und Reasoning."
        ),
        "datum_handlung": "2023-07-11",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Claude_(language_model)",
        "quell_titel": "Wikipedia: Claude (language model)",
        "kontext": "Erster frei zugaenglicher Claude-Release; Konkurrenzprodukt zu ChatGPT",
    },
    # -----------------------------------------------------------------------
    # 8. White House Voluntary AI Commitments
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Anthropic unterzeichnet als eines von sieben fuehrenden "
            "US-KI-Unternehmen freiwillige Selbstverpflichtungen gegenueber "
            "der Biden-Administration zu KI-Sicherheit, Transparenz und "
            "externem Testing vor Deployment."
        ),
        "datum_handlung": "2023-07-21",
        "betrag_usd": None,
        "quell_link": "https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2023/07/21/fact-sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/",
        "quell_titel": "White House Fact Sheet: Voluntary Commitments from Leading AI Companies",
        "kontext": "Anthropic, OpenAI, Google, Meta, Microsoft, Amazon, Inflection unterzeichnen gemeinsam",
    },
    # -----------------------------------------------------------------------
    # 9. Responsible Scaling Policy
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Anthropic veroeffentlicht als erstes grosses KI-Unternehmen eine "
            "'Responsible Scaling Policy' (RSP) mit dem AI Safety Levels (ASL) "
            "Framework, angelehnt an biologische Sicherheitsstufen (BSL). "
            "Amodei investierte 10-20% seiner Arbeitszeit ueber 3 Monate in "
            "die Ausarbeitung."
        ),
        "datum_handlung": "2023-09-19",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/uk-ai-safety-summit",
        "quell_titel": "Anthropic: Dario Amodei's remarks on RSP at AI Safety Summit",
        "kontext": "Vorgestellt bei Bletchley Park AI Safety Summit; RSP wird als Formaldirektive des Boards verankert",
    },
    # -----------------------------------------------------------------------
    # 10. Amazon-Partnerschaft ($4 Mrd.)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": (
            "Amazon investiert initial $1.25 Mrd. in Anthropic als Teil eines "
            "geplanten $4 Mrd. Deals. Anthropic wird bevorzugter KI-Partner "
            "fuer Amazon Web Services (AWS) und nutzt AWS-Infrastruktur."
        ),
        "datum_handlung": "2023-09-25",
        "betrag_usd": 4_000_000_000,
        "quell_link": "https://www.datacenterdynamics.com/en/news/amazon-invests-275bn-in-ai-startup-anthropic-as-part-of-planned-4bn-deal/",
        "quell_titel": "DCD: Amazon invests in Anthropic as part of $4bn deal",
        "kontext": "Strategische Partnerschaft; Amazon wird Minderheitsaktionaer; Claude auf AWS Bedrock",
    },
    # -----------------------------------------------------------------------
    # 11. Claude 3 Familie
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Anthropic veroeffentlicht die Claude-3-Modellfamilie mit drei "
            "Varianten: Claude 3 Opus (flaggschiff), Claude 3 Sonnet (mittel) "
            "und Claude 3 Haiku (schnell/guenstig). Opus uebertrifft GPT-4 "
            "in vielen Benchmarks."
        ),
        "datum_handlung": "2024-03-04",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Claude_(language_model)",
        "quell_titel": "Wikipedia: Claude (language model)",
        "kontext": "Erster Release einer gestuften Modellfamilie; macht Anthropic wettbewerbsfaehig mit OpenAI",
    },
    # -----------------------------------------------------------------------
    # 12. Claude 3.5 Sonnet
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Anthropic veroeffentlicht Claude 3.5 Sonnet, der trotz "
            "Mittelklasse-Pricing den bisherigen Flaggschiff-Claude 3 Opus "
            "in den meisten Benchmarks uebertrifft -- bei doppelter "
            "Geschwindigkeit und einem Fuenftel der Kosten."
        ),
        "datum_handlung": "2024-06-20",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/claude-3-5-sonnet",
        "quell_titel": "Anthropic: Introducing Claude 3.5 Sonnet",
        "kontext": "Ungewoehnlich: Mittleres Modell uebertrifft Flaggschiff; Branchenueberraschung",
    },
    # -----------------------------------------------------------------------
    # 13. Long-Term Benefit Trust
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": (
            "Anthropic etabliert den Long-Term Benefit Trust (LTBT): ein "
            "unabhaengiges Gremium aus fuenf Experten fuer KI-Sicherheit, "
            "nationale Sicherheit und Ethik, das schrittweise die Mehrheit "
            "der Sitze im Anthropic-Board waehlen kann. Trustees haben "
            "keine finanziellen Interessen an Anthropic."
        ),
        "datum_handlung": "2023-09-19",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/the-long-term-benefit-trust",
        "quell_titel": "Anthropic: The Long-Term Benefit Trust",
        "kontext": "Corporate-Governance-Innovation zur Absicherung der Sicherheitsmission gegen rein kommerzielle Interessen",
    },
    # -----------------------------------------------------------------------
    # 14. Claude Opus 4 und Sonnet 4
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": (
            "Anthropic veroeffentlicht Claude Opus 4 (leistungstaerkstes Modell, "
            "weltbestes Coding-Modell) und Claude Sonnet 4 mit Extended Thinking "
            "und Hybrid-Modus."
        ),
        "datum_handlung": "2025-05-22",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/claude-4",
        "quell_titel": "Anthropic: Introducing Claude 4",
        "kontext": "Naechste Generation nach Claude 3.5; etabliert Anthropic als Marktfuehrer im Coding",
    },
    # -----------------------------------------------------------------------
    # 15. Series E ($3.5 Mrd.)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "investition",
        "beschreibung": (
            "Anthropic schliesst eine Series-E-Finanzierungsrunde ueber "
            "$3.5 Mrd. ab, angefuehrt von Lightspeed Venture Partners. "
            "Post-Money-Bewertung: $61.5 Mrd."
        ),
        "datum_handlung": "2025-03-01",
        "betrag_usd": 3_500_000_000,
        "quell_link": "https://news.crunchbase.com/ai/anthropic-funding-lightspeed-xai-openai/",
        "quell_titel": "Crunchbase: Anthropic Nears Closing Of $3.5B Funding At $61.5B Valuation",
        "kontext": "Bewertung mehr als verzehnfacht seit Series C ($4.1 Mrd. Mai 2023)",
    },
    # -----------------------------------------------------------------------
    # 16. Amazon-Investition verdoppelt ($8 Mrd. gesamt)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": (
            "Amazon verdoppelt sein Gesamtinvestment in Anthropic auf $8 Mrd. "
            "durch eine weitere Investition von $4 Mrd."
        ),
        "datum_handlung": "2024-11-22",
        "betrag_usd": 4_000_000_000,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Vertiefung der strategischen Partnerschaft; Amazon verdoppelt auf $8 Mrd. gesamt",
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
        "Dario Amodei Anthropic CEO quotes interviews essays Senate testimony Bletchley Paris Davos CNN 60 Minutes Lex Fridman Dwarkesh Machines of Loving Grace Adolescence of Technology Urgency of Interpretability",
        50,
        len(AUSSAGEN) + len(HANDLUNGEN),
        (
            "Systematische Recherche via WebSearch (2026-02-11). "
            "Quellen: Blog-Essays auf darioamodei.com, Senate Testimony (PDF), "
            "Anthropic Blog, Lex Fridman Podcast #452, Dwarkesh Podcast, "
            "CNN/Anderson Cooper, CBS 60 Minutes, Axios AI+ Summit, "
            "NYT DealBook Summit, Davos WEF, Paris AI Summit. "
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
        print(f"\nGesamtbestand Dario Amodei: {total_a} Aussagen, {total_h} Handlungen")

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
