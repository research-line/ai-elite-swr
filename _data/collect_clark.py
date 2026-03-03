#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_clark.py
================
Fuegt verifizierbare Aussagen und Handlungen von Jack Clark (person_id=51)
in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Eintraege basieren auf oeffentlich zugaenglichen Quellen,
die per WebSearch am 2026-02-12 recherchiert wurden.

NUTZUNG:
    python collect_clark.py

ACHTUNG: Vor dem Ausfuehren pruefen! Doppelte Ausfuehrung wird durch
         unique-Check auf (person_id, aussage_text) bzw.
         (person_id, beschreibung, datum_handlung) verhindert.
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 51  # Jack Clark
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
    # 1. UN Security Council Briefing (Juli 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "We cannot leave the development of artificial intelligence solely "
            "to private-sector actors. Governments can keep companies accountable — "
            "and companies can earn the world's trust — by developing robust, "
            "reliable evaluation systems."
        ),
        "aussage_kurz": "KI-Entwicklung darf nicht allein dem Privatsektor ueberlassen werden",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Regierungsgremien
        "quell_link": "https://press.un.org/en/2023/sc15359.doc.htm",
        "quell_titel": "UN Security Council Meeting Record - AI Debate",
        "datum_aussage": "2023-07-18",
        "sprache": "en",
        "kontext": "Erste UN-Sicherheitsratsitzung ueber KI und Frieden/Sicherheit; Clark argumentiert fuer staatliche Aufsicht",
    },
    {
        "aussage_text": (
            "Any sensible approach to regulation will start with having the "
            "ability to evaluate an AI system for a given capability or flaw. "
            "Right now, there are no standards or even best practices on how to "
            "test these frontier systems for things like discrimination, misuse "
            "or safety."
        ),
        "aussage_kurz": "Es fehlen Standards fuer KI-Sicherheitstests - das erschwert Regulierung",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://jack-clark.net/2023/07/18/ai-safety-and-corporate-power-remarks-given-at-the-un-security-council/",
        "quell_titel": "AI Safety and Corporate Power - remarks at UN Security Council (Import AI)",
        "datum_aussage": "2023-07-18",
        "sprache": "en",
        "kontext": "Vollstaendiger Text seiner UN-Rede auf seinem Blog Import AI",
    },
    # -----------------------------------------------------------------------
    # 2. Congressional Testimony (Juni 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "As I said in my testimony yesterday, we have a short window of time "
            "to get a sensible federal policy framework in place before an accident "
            "or a misuse leads to a reactive and likely bad regulatory response."
        ),
        "aussage_kurz": "Nur kurzes Zeitfenster fuer sinnvolle Regulierung vor reaktiven Ueberreaktionen",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/jackclarkSF/status/1938293432893772103",
        "quell_titel": "Jack Clark on X/Twitter - Post-Testimony Statement",
        "datum_aussage": "2025-06-26",
        "sprache": "en",
        "kontext": "Tweet nach seiner Aussage vor dem House Select Committee on China",
    },
    {
        "aussage_text": (
            "Powerful AI could be buildable by late 2026 or early 2027. My two "
            "essential points are: the U.S. can win the race to build powerful AI, "
            "but winning the race is a necessary but not sufficient achievement - "
            "we have to get safety right."
        ),
        "aussage_kurz": "Maechtige KI bis Ende 2026/Anfang 2027 - USA kann gewinnen, muss aber Sicherheit priorisieren",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.congress.gov/119/meeting/house/118428/witnesses/HHRG-119-ZS00-Wstate-ClarkJ-20250625.pdf",
        "quell_titel": "Written Testimony of Jack Clark, Co-Founder and Head of Policy, Anthropic",
        "datum_aussage": "2025-06-25",
        "sprache": "en",
        "kontext": "Schriftliche Aussage vor House Select Committee 'Algorithms and Authoritarians'",
    },
    {
        "aussage_text": (
            "When we studied systems from companies like DeepSeek, we found that "
            "they exhibit the same risks as U.S. models, but without the "
            "interventions that companies like Anthropic apply to reduce them."
        ),
        "aussage_kurz": "Chinesische KI-Modelle haben gleiche Risiken wie US-Modelle, aber ohne Sicherheitsinterventionen",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.congress.gov/119/meeting/house/118428/witnesses/HHRG-119-ZS00-Wstate-ClarkJ-20250625.pdf",
        "quell_titel": "Written Testimony of Jack Clark, Anthropic (June 2025)",
        "datum_aussage": "2025-06-25",
        "sprache": "en",
        "kontext": "Warnung vor ungefilterten chinesischen KI-Modellen im Kongress",
    },
    # -----------------------------------------------------------------------
    # 3. DeepSeek-Bewertung
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I think the DeepSeek hype is perhaps a bit overblown. It is a "
            "competent group of engineers and researchers that have read all "
            "of the same research papers all the frontier labs have made and "
            "have clean-sheeted a new system off of that which has some clever "
            "algorithmic ideas. If you actually analyze it, it looks 6 to 8 "
            "months behind where us frontier companies are."
        ),
        "aussage_kurz": "DeepSeek-Hype uebertrieben - chinesische Firma liegt 6-8 Monate hinter US-Frontier-Labs",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://opentools.ai/news/anthropics-jack-clark-downplays-deepseeks-ai-progress",
        "quell_titel": "Anthropic's Jack Clark Downplays DeepSeek's AI Progress (AI News)",
        "datum_aussage": "2025-01-20",
        "sprache": "en",
        "kontext": "Einschaetzung zu chinesischem KI-Startup DeepSeek; Clark argumentiert US-Vorsprung bestehe weiter",
    },
    {
        "aussage_text": (
            "DeepSeek means AI proliferation is guaranteed."
        ),
        "aussage_kurz": "DeepSeek beweist: KI-Proliferation ist unvermeidlich",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://opentools.ai/news/anthropic-co-founder-downplays-deepseeks-ai-buzz-no-threat-to-us-dominance-just-yet",
        "quell_titel": "Anthropic Co-Founder on DeepSeek: No Threat to US Dominance (AI News)",
        "datum_aussage": "2025-01-20",
        "sprache": "en",
        "kontext": "Warnung vor globaler Verbreitung von KI-Faehigkeiten",
    },
    # -----------------------------------------------------------------------
    # 4. "Technological Optimism and Appropriate Fear" Essay (Oktober 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Too many people are pretending that AI cannot threaten humanity. "
            "We need to acknowledge a different reality before figuring out "
            "how to tame it and live together."
        ),
        "aussage_kurz": "Zu viele Menschen leugnen existenzielle KI-Risiken",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://jack-clark.net/2025/10/13/import-ai-431-technological-optimism-and-appropriate-fear/",
        "quell_titel": "Import AI 431: Technological Optimism and Appropriate Fear",
        "datum_aussage": "2025-10-13",
        "sprache": "en",
        "kontext": "Essay im Import AI Newsletter; Clark positioniert sich zwischen Optimismus und Angst",
    },
    {
        "aussage_text": (
            "The world will bend around AI akin to how a black hole pulls and "
            "bends everything around itself."
        ),
        "aussage_kurz": "Die Welt wird sich um KI herum verbiegen wie um ein Schwarzes Loch",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 2,
        "quell_link": "https://x.com/jackclarkSF/status/1977828314871218378",
        "quell_titel": "Jack Clark on X/Twitter - Essay Announcement",
        "datum_aussage": "2025-10-13",
        "sprache": "en",
        "kontext": "Tweet zur Veroeffentlichung seines Essays; drastische Metapher fuer KI-Impact",
    },
    # -----------------------------------------------------------------------
    # 5. AI as Political Technology
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "AI is a political technology, and I think anyone who wants to avoid "
            "that is a little silly. What I mean by political technology is that "
            "it's a general purpose utility which the state can layer over anything, "
            "and augment anything with - especially if you are a creator of systems, "
            "which governments are. It's political in the sense that it will be "
            "used by governments in a major way to help them configure their state."
        ),
        "aussage_kurz": "KI ist eine politische Technologie - Staaten werden sie massiv nutzen",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast
        "plattform_id": 3,     # Podcast-Plattformen
        "quell_link": "https://80000hours.org/podcast/episodes/openai-askell-brundage-clark-latest-in-ai-policy-and-strategy/",
        "quell_titel": "80,000 Hours Podcast - OpenAI Policy Team on AI Advances",
        "datum_aussage": "2019-07-15",
        "sprache": "en",
        "kontext": "Interview als OpenAI Policy Director; fruehe Warnung vor staatlicher KI-Nutzung",
    },
    # -----------------------------------------------------------------------
    # 6. AI as Accelerant
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "AI is an accelerant. It makes the things that are good, better, "
            "and the things that are bad, worse."
        ),
        "aussage_kurz": "KI ist ein Beschleuniger - verstaerkt Gutes und Schlechtes",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.antoinebuteau.com/lessons-from-jack-clark-of-anthropic/",
        "quell_titel": "Lessons from Jack Clark of Anthropic (Antoine Buteau Blog)",
        "datum_aussage": "2024-05-10",
        "sprache": "en",
        "kontext": "Haeufig zitierte Aussage Clarks ueber die duale Natur von KI",
    },
    # -----------------------------------------------------------------------
    # 7. Black Box Problem
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Frontier AI models are, to some extent, black boxes. A significant "
            "part of the safety challenge is developing better techniques to "
            "interpret and understand their internal workings."
        ),
        "aussage_kurz": "Frontier-KI-Modelle sind Black Boxes - Interpretierbarkeit ist zentrale Sicherheitsherausforderung",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.antoinebuteau.com/lessons-from-jack-clark-of-anthropic/",
        "quell_titel": "Lessons from Jack Clark of Anthropic",
        "datum_aussage": "2024-05-10",
        "sprache": "en",
        "kontext": "Clark ueber die Grenzen des Verstaendnisses moderner KI-Systeme",
    },
    {
        "aussage_text": (
            "Situational awareness in AI systems are a symptom of something "
            "fiendishly complex happening inside the system which we can neither "
            "fully explain or predict - this is inherently very scary."
        ),
        "aussage_kurz": "Situatives Bewusstsein in KI ist unerklaerlich und daher beaengstigend",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.antoinebuteau.com/lessons-from-jack-clark-of-anthropic/",
        "quell_titel": "Lessons from Jack Clark of Anthropic",
        "datum_aussage": "2024-05-10",
        "sprache": "en",
        "kontext": "Warnung vor emergenten Faehigkeiten in KI-Systemen",
    },
    # -----------------------------------------------------------------------
    # 8. Tyler Cowen Interview - Economic Impact (Mai 2025)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I am relatively bearish on AI-fueled economic growth. I predict "
            "growth of 3-5% rather than the 20-30% touted by techno-optimists."
        ),
        "aussage_kurz": "Skeptisch gegenueber KI-Wachstumsprognosen - erwartet 3-5%, nicht 20-30%",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://conversationswithtyler.com/episodes/jack-clark/",
        "quell_titel": "Conversations with Tyler: Jack Clark on AI's Uneven Impact",
        "datum_aussage": "2025-03-28",
        "sprache": "en",
        "kontext": "Interview mit Tyler Cowen; Clark aeussert sich zurueckhaltend zu KI-Wirtschaftsimpact",
    },
    {
        "aussage_text": (
            "It will be the era of the manager nerds. Being able to manage "
            "fleets of AI agents and orchestrate them will make people "
            "incredibly powerful."
        ),
        "aussage_kurz": "Zukunft gehoert Manager-Nerds, die KI-Agenten-Flotten orchestrieren",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://conversationswithtyler.com/episodes/jack-clark/",
        "quell_titel": "Conversations with Tyler: Jack Clark on AI's Uneven Impact",
        "datum_aussage": "2025-03-28",
        "sprache": "en",
        "kontext": "Vision zukuenftiger Arbeitswelt mit KI-Agenten",
    },
    # -----------------------------------------------------------------------
    # 9. Journalist Background
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "With a background in journalism and the humanities, I offer a "
            "sober assessment of AI's economic impact."
        ),
        "aussage_kurz": "Journalismus-Hintergrund praegt nuechterne KI-Einschaetzung",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.webpronews.com/ai-reality-check-jack-clarks-sobering-forecast-on-techs-economic-impact/",
        "quell_titel": "AI Reality Check: Jack Clark's Sobering Forecast (WebProNews)",
        "datum_aussage": "2025-05-11",
        "sprache": "en",
        "kontext": "Clark reflektiert ueber seinen journalistischen Background als Kontrapunkt zu Tech-Optimismus",
    },
]


# ============================================================================
# HANDLUNGEN
# ============================================================================

HANDLUNGEN = [
    # -----------------------------------------------------------------------
    # 1. Journalistische Taetigkeit Bloomberg
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "Jack Clark arbeitet als Neural Network Reporter bei Bloomberg, "
            "spezialisiert auf KI-Berichterstattung ueber Google, AWS und "
            "verteilte Systeme."
        ),
        "datum_handlung": "2014-06-01",
        "betrag_usd": None,
        "quell_link": "https://jack-clark.net/about/",
        "quell_titel": "About | Import AI (Jack Clark)",
        "kontext": "Journalistische Karriere vor OpenAI; schrieb fuer Bloomberg und The Register",
    },
    # -----------------------------------------------------------------------
    # 2. Eintritt bei OpenAI
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "Jack Clark tritt OpenAI bei, zunaechst fuer Strategie und "
            "Kommunikation, spaeter wird er Policy Director."
        ),
        "datum_handlung": "2016-02-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jack_Clark_(AI_policy_expert)",
        "quell_titel": "Wikipedia: Jack Clark (AI policy expert)",
        "kontext": "Wechsel vom Journalismus in die KI-Industrie; arbeitet 4 Jahre bei OpenAI",
    },
    # -----------------------------------------------------------------------
    # 3. AI Index Mitgruender
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "gruendung",
        "beschreibung": (
            "Jack Clark wird Gruendungsmitglied und Co-Chair des AI Index "
            "Steering Committee an der Stanford University, einer jaehrlichen "
            "Berichterstattung ueber den Stand der KI-Forschung."
        ),
        "datum_handlung": "2017-11-01",
        "betrag_usd": None,
        "quell_link": "https://hai.stanford.edu/people/jack-clark",
        "quell_titel": "Jack Clark | Stanford HAI",
        "kontext": "Nebenrolle bei Stanford HAI; AI Index wird zu einflussreichstem KI-Progress-Tracker",
    },
    # -----------------------------------------------------------------------
    # 4. Congressional Testimony als OpenAI Policy Director
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Jack Clark sagt als Policy Director von OpenAI vor dem "
            "US House Science Committee ueber KI-Fortschritte und "
            "politische Herausforderungen aus."
        ),
        "datum_handlung": "2019-06-13",
        "betrag_usd": None,
        "quell_link": "https://docs.house.gov/meetings/IG/IG00/20190613/109620/HHRG-116-IG00-Wstate-ClarkJ-20190613.pdf",
        "quell_titel": "Written Testimony of Jack Clark Policy Director OpenAI",
        "kontext": "Frueher Auftritt vor dem Kongress; etabliert sich als KI-Policy-Experte",
    },
    # -----------------------------------------------------------------------
    # 5. Mitgruendung Anthropic
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "gruendung",
        "beschreibung": (
            "Jack Clark verlaesst OpenAI und gruendet zusammen mit Dario und "
            "Daniela Amodei, Tom Brown, Chris Olah, Sam McCandlish und Jared "
            "Kaplan das KI-Sicherheitsunternehmen Anthropic. Clark wird "
            "Co-Founder und Head of Policy."
        ),
        "datum_handlung": "2021-01-28",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Abspaltung von 7 OpenAI-Mitarbeitern aufgrund von Differenzen ueber KI-Sicherheit und Kommerzialisierung",
    },
    # -----------------------------------------------------------------------
    # 6. NAIAC Mitglied
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Jack Clark wird als eines der 27 Gruendungsmitglieder in das "
            "National Artificial Intelligence Advisory Committee (NAIAC) "
            "berufen, ein Beratungsgremium des US-Handelsministeriums."
        ),
        "datum_handlung": "2022-04-01",
        "betrag_usd": None,
        "quell_link": "https://www.nist.gov/news-events/news/2022/04/us-department-commerce-appoints-27-members-national-ai-advisory-committee",
        "quell_titel": "U.S. Department of Commerce Appoints 27 Members to National AI Advisory Committee",
        "kontext": "NAIAC beraet US-Regierung zu KI-Politik; Clark dient bis 2024",
    },
    # -----------------------------------------------------------------------
    # 7. UN Security Council Briefing
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Jack Clark haelt eine offizielle Rede bei der ersten UN-Sicherheitsratssitzung "
            "ueber KI-Bedrohungen fuer den Weltfrieden, gemeinsam mit UN-Generalsekretaer "
            "Guterres und chinesischem KI-Experten Yi Zeng."
        ),
        "datum_handlung": "2023-07-18",
        "betrag_usd": None,
        "quell_link": "https://press.un.org/en/2023/sc15359.doc.htm",
        "quell_titel": "UN Security Council SC/15359 - AI Debate",
        "kontext": "Historischer Moment: erste KI-Debatte im UN-Sicherheitsrat; Clark argumentiert fuer Regierungsueberwachung",
    },
    # -----------------------------------------------------------------------
    # 8. Responsible Scaling Policy
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Jack Clark ist massgeblich an der Entwicklung der Anthropic "
            "Responsible Scaling Policy (RSP) beteiligt, die als erstes "
            "formales KI-Sicherheitsframework eines Frontier-Labs gilt."
        ),
        "datum_handlung": "2023-09-19",
        "betrag_usd": None,
        "quell_link": "https://www.anthropic.com/news/anthropics-responsible-scaling-policy",
        "quell_titel": "Anthropic's Responsible Scaling Policy",
        "kontext": "RSP wird zum Branchenstandard; andere Labs entwickeln aehnliche Frameworks",
    },
    # -----------------------------------------------------------------------
    # 9. Federal Preemption Lobbying
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "lobbying",
        "beschreibung": (
            "Jack Clark lobbyiert bei Kongressabgeordnetem Jay Obernolte (CA-23) "
            "fuer bundesweite KI-Regulierung, die kalifornische und andere "
            "einzelstaatliche KI-Gesetze praeemptieren wuerde."
        ),
        "datum_handlung": "2024-12-01",
        "betrag_usd": None,
        "quell_link": "https://forum.effectivealtruism.org/posts/JoJwBsGJFWtq72omp/anthropic-announcing-our-updated-responsible-scaling-policy",
        "quell_titel": "EA Forum: Anthropic rewrote its RSP (Discussion of Clark's lobbying)",
        "kontext": "Clark setzt sich fuer Federal Preemption ein, um fragmentierte State-Level-Regulierung zu vermeiden",
    },
    # -----------------------------------------------------------------------
    # 10. Congressional Testimony Anthropic
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Jack Clark sagt vor dem House Science Committee ueber KI-Sicherheit "
            "und Anthropics Responsible Scaling Policy aus."
        ),
        "datum_handlung": "2024-02-06",
        "betrag_usd": None,
        "quell_link": "https://www.congress.gov/118/meeting/house/116790/witnesses/HHRG-118-SY15-Wstate-ClarkJ-20240206.pdf",
        "quell_titel": "Written Testimony of Jack Clark, Co-Founder and Head of Policy, Anthropic",
        "kontext": "Zweites Mal vor Kongress; diesmal als Anthropic-Vertreter, nicht OpenAI",
    },
    # -----------------------------------------------------------------------
    # 11. Congressional Testimony - China Competition
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "politisch",
        "beschreibung": (
            "Jack Clark sagt vor dem House Select Committee on the Chinese "
            "Communist Party zum Thema 'Algorithms and Authoritarians: Why "
            "U.S. AI Must Lead' aus und fordert Export-Controls fuer KI-Chips "
            "nach China."
        ),
        "datum_handlung": "2025-06-25",
        "betrag_usd": None,
        "quell_link": "https://www.congress.gov/119/meeting/house/118428/witnesses/HHRG-119-ZS00-Wstate-ClarkJ-20250625.pdf",
        "quell_titel": "Testimony of Jack Clark, Anthropic (House Select Committee)",
        "kontext": "Clark warnt vor chinesischer KI ohne Sicherheitsinterventionen; empfiehlt haertere Exportkontrollen",
    },
    # -----------------------------------------------------------------------
    # 12. Google Cloud Partnership
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": (
            "Anthropic und Google kuendigen Cloud-Partnership im Wert von "
            "mehreren zehn Milliarden Dollar an. Google stellt Anthropic "
            "Zugang zu bis zu 1 Million TPUs (Tensor Processing Units) zur "
            "Verfuegung, was ueber 1 Gigawatt KI-Rechenkapazitaet bis 2026 "
            "ermoeglicht."
        ),
        "datum_handlung": "2025-10-23",
        "betrag_usd": None,  # "tens of billions" nicht genau spezifiziert
        "quell_link": "https://www.cnbc.com/2025/10/23/anthropic-google-cloud-deal-tpu.html",
        "quell_titel": "CNBC: Google and Anthropic announce cloud deal worth tens of billions",
        "kontext": "Anthropic diversifiziert von Amazon AWS weg; Google investierte bereits $3 Mrd. in Anthropic",
    },
    # -----------------------------------------------------------------------
    # 13. Microsoft/Nvidia Partnership
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": (
            "Anthropic kuendigt $30 Milliarden Server-Compute-Deal mit "
            "Microsoft Azure an. Microsoft und Nvidia investieren gemeinsam "
            "$15 Milliarden in Anthropic. Anthropic wird erste KI-Firma, "
            "die gleichzeitig auf Azure, AWS und Google Cloud verfuegbar ist."
        ),
        "datum_handlung": "2025-11-01",
        "betrag_usd": 15_000_000_000,
        "quell_link": "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-signs-usd30-billion-deal-with-amazon-to-deploy-claude-on-aws-nvidia-and-microsoft-jointly-invest-usd15-billion-into-ai-firm",
        "quell_titel": "Tom's Hardware: Anthropic signs $30B deal with Microsoft, Nvidia invests $15B",
        "kontext": "Multi-Cloud-Strategie; Clark als Policy Head beteiligt an strategischen Deals",
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
        "Jack Clark Anthropic OpenAI Policy Director AI Index UN Security Council Congress testimony Import AI DeepSeek China export controls Responsible Scaling Policy Tyler Cowen journalist Bloomberg",
        40,
        len(AUSSAGEN) + len(HANDLUNGEN),
        (
            "Systematische Recherche via WebSearch (2026-02-12). "
            "Quellen: UN Security Council Briefing (Juli 2023), Congressional "
            "Testimony (2024-2025), Import AI Newsletter, X/Twitter, Tyler Cowen "
            "Podcast, 80,000 Hours Podcast, Wikipedia, Stanford HAI, Anthropic Blog, "
            "NIST, CNBC, Tom's Hardware. Alle Zitate stammen aus oeffentlich "
            "zugaenglichen, verifizierbaren Quellen."
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
        print(f"\nGesamtbestand Jack Clark: {total_a} Aussagen, {total_h} Handlungen")

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
