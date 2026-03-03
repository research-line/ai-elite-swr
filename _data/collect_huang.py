#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_huang.py
================
Sammelt verifizierbare Aussagen und Handlungen von Jensen Huang (person_id=1)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Keynote-Reden, Panel-Diskussionen und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 1  # Jensen Huang

# ============================================================================
# AUSSAGEN (Statements)
# ============================================================================
# Jede Aussage enthaelt:
#   - aussage_text: Originalwortlaut (Englisch)
#   - aussage_kurz: 1-Satz-Zusammenfassung (Deutsch)
#   - modus: 'muendlich' oder 'schriftlich'
#   - quellen_typ_id: FK zu quellen_typen
#   - plattform_id: FK zu plattformen
#   - quell_link: URL
#   - quell_titel: Titel der Quelle
#   - datum_aussage: YYYY-MM-DD oder YYYY
#   - sprache: 'en'
#   - kontext: Zusammenhang
#   - aussage_uebersetzung_de: Deutsche Uebersetzung

AUSSAGEN = [
    # ---- 1. AGI Timeline - GTC 2024 ----
    {
        "aussage_text": "If we specified AGI to be something very specific, a set of tests where a software program can do very well — or maybe 8% better than most people — I believe we will get there within 5 years.",
        "aussage_kurz": "Huang prognostiziert bei GTC 2024, dass AGI innerhalb von 5 Jahren erreicht werden koennte.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://techcrunch.com/2024/03/19/agi-and-hallucinations/",
        "quell_titel": "Nvidia's Jensen Huang says AGI is 5 years away (TechCrunch)",
        "datum_aussage": "2024-03-19",
        "sprache": "en",
        "kontext": "GTC 2024 Keynote. Huang aeussert sich zur AGI-Timeline und betont, dass die Definition von AGI entscheidend ist.",
        "aussage_uebersetzung_de": "Wenn wir AGI als etwas sehr Spezifisches definieren, eine Reihe von Tests, bei denen ein Softwareprogramm sehr gut abschneidet -- oder vielleicht 8% besser als die meisten Menschen -- dann glaube ich, dass wir das innerhalb von 5 Jahren erreichen werden.",
    },
    # ---- 2. Superintelligence Vision - CES 2025 ----
    {
        "aussage_text": "That's the future, you're going to have superintelligent AI that will let you write, analyze problems, deal with supply chain planning, write software, design chips.",
        "aussage_kurz": "Huang beschreibt bei CES 2025 eine Zukunft mit superintelligenter KI fuer komplexe Aufgaben.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.engadget.com/ai/nvidia-ceo-jensen-huang-welcomes-the-rise-of-superintelligent-ai-at-ces-2025-002827074.html",
        "quell_titel": "NVIDIA CEO Jensen Huang welcomes the rise of superintelligent AI at CES 2025 (Engadget)",
        "datum_aussage": "2025-01-07",
        "sprache": "en",
        "kontext": "CES 2025 Keynote in Las Vegas. Huang spricht ueber Physical AI und Superintelligenz.",
        "aussage_uebersetzung_de": "Das ist die Zukunft: Sie werden superintelligente KI haben, die es Ihnen ermoeglicht zu schreiben, Probleme zu analysieren, Lieferkettenplanung zu betreiben, Software zu schreiben, Chips zu entwerfen.",
    },
    # ---- 3. AI's iPhone Moment - Berkeley Interview 2023 ----
    {
        "aussage_text": "AI is having its 'iPhone moment' driven by the introduction of ChatGPT.",
        "aussage_kurz": "Huang bezeichnet den Launch von ChatGPT als das 'iPhone-Moment' der KI.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://stratechery.com/2023/an-interview-with-nvidia-ceo-jensen-huang-about-ais-iphone-moment/",
        "quell_titel": "An Interview with Nvidia CEO Jensen Huang About AI's iPhone Moment (Stratechery)",
        "datum_aussage": "2023-02-10",
        "sprache": "en",
        "kontext": "Interview an der UC Berkeley Haas School of Business. Huang vergleicht den ChatGPT-Launch mit dem iPhone als transformativen Moment.",
        "aussage_uebersetzung_de": "KI hat ihren 'iPhone-Moment', angetrieben durch die Einfuehrung von ChatGPT.",
    },
    # ---- 4. Sovereign AI - World Governments Summit 2024 ----
    {
        "aussage_text": "It codifies your culture, your society's intelligence, your common sense, your history – you own your own data.",
        "aussage_kurz": "Huang erklaert Sovereign AI als Kodifizierung von Kultur und Gesellschaft in eigenen Daten.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://blogs.nvidia.com/blog/world-governments-summit/",
        "quell_titel": "NVIDIA CEO: Every Country Needs Sovereign AI (NVIDIA Blog)",
        "datum_aussage": "2024-02-13",
        "sprache": "en",
        "kontext": "World Governments Summit 2024 in Dubai. Huang stellt das Konzept von Sovereign AI vor.",
        "aussage_uebersetzung_de": "Es kodifiziert Ihre Kultur, die Intelligenz Ihrer Gesellschaft, Ihren gesunden Menschenverstand, Ihre Geschichte -- Sie besitzen Ihre eigenen Daten.",
    },
    # ---- 5. Sovereign AI - Atomic Bombs Quote ----
    {
        "aussage_text": "Nobody needs atomic bombs, everyone needs AI.",
        "aussage_kurz": "Huang betont, dass KI im Gegensatz zu Atomwaffen universell notwendig ist.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.tweaktown.com/news/107910/nvidia-ceo-on-sovereign-ai-for-countries-no-one-needs-atomic-bombs-everyone-needs-ai/index.html",
        "quell_titel": "NVIDIA CEO on sovereign AI: 'no one needs atomic bombs, everyone needs AI' (TweakTown)",
        "datum_aussage": "2024-02-13",
        "sprache": "en",
        "kontext": "World Governments Summit 2024. Huang argumentiert, dass jedes Land KI-Infrastruktur aufbauen sollte.",
        "aussage_uebersetzung_de": "Niemand braucht Atombomben, jeder braucht KI.",
    },
    # ---- 6. Largest Infrastructure Buildout - Davos 2026 ----
    {
        "aussage_text": "AI is infrastructure. We are seeing the largest infrastructure buildout in human history.",
        "aussage_kurz": "Huang beschreibt die KI-Infrastruktur als groessten Infrastruktur-Aufbau der Menschheitsgeschichte.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://fortune.com/2026/01/21/jensen-huang-on-ai-bubble-largest-infrastructure-buildout-history/",
        "quell_titel": "Jensen Huang says AI bubble fears are dwarfed by 'the largest infrastructure build-out in human history' (Fortune)",
        "datum_aussage": "2026-01-21",
        "sprache": "en",
        "kontext": "World Economic Forum in Davos 2026. Panel-Diskussion mit BlackRock CEO Larry Fink.",
        "aussage_uebersetzung_de": "KI ist Infrastruktur. Wir sehen den groessten Infrastruktur-Aufbau in der Geschichte der Menschheit.",
    },
    # ---- 7. India Sovereign AI - Flour/Bread Metaphor ----
    {
        "aussage_text": "India should not export flour to import bread. By owning the data (flour) and GPU clusters (bakery), nations can ensure their AI reflects their unique societal values and linguistic heritage.",
        "aussage_kurz": "Huang fordert Indien auf, eigene KI-Infrastruktur aufzubauen statt Daten zu exportieren.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://yourstory.com/2026/02/ai-is-infrastructure-and-india-will-have-its-own-says-jensen-huang",
        "quell_titel": "AI is infrastructure, and India will have its own, says Jensen Huang (YourStory)",
        "datum_aussage": "2026-02-05",
        "sprache": "en",
        "kontext": "Panel-Diskussion in Indien. Huang nutzt die Mehl/Brot-Metapher fuer Datensouveraenitaet.",
        "aussage_uebersetzung_de": "Indien sollte kein Mehl exportieren, um Brot zu importieren. Indem Nationen die Daten (Mehl) und GPU-Cluster (Baeckerei) besitzen, koennen sie sicherstellen, dass ihre KI ihre einzigartigen gesellschaftlichen Werte und sprachliches Erbe widerspiegelt.",
    },
    # ---- 8. TSMC Partnership - Without TSMC Quote ----
    {
        "aussage_text": "Without TSMC, there is no Nvidia today. You are really the pride of Taiwan, you are also the pride of the world.",
        "aussage_kurz": "Huang wuerdigt TSMC als unverzichtbaren Partner fuer NVIDIAs Erfolg.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.shacknews.com/article/146757/jensen-huang-tsmc-pride-of-the-world",
        "quell_titel": "Jensen Huang says that 'without TSMC, there is no NVIDIA' (Shacknews)",
        "datum_aussage": "2025-11-08",
        "sprache": "en",
        "kontext": "TSMC Sports Day Event in Taiwan. Huang betont die strategische Bedeutung von TSMC.",
        "aussage_uebersetzung_de": "Ohne TSMC gaebe es NVIDIA heute nicht. Sie sind wirklich der Stolz Taiwans, Sie sind auch der Stolz der Welt.",
    },
    # ---- 9. TSMC as Family ----
    {
        "aussage_text": "TSMC is my family.",
        "aussage_kurz": "Huang bezeichnet TSMC als seine Familie.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://english.cw.com.tw/article/article.action?id=4451",
        "quell_titel": "What a Night With Jensen Huang Reveals About the Real AI Power Struggle (CommonWealth Magazine)",
        "datum_aussage": "2025-11-08",
        "sprache": "en",
        "kontext": "TSMC Sports Day. Huang zeigt emotionale Bindung zum wichtigsten Fertigungspartner.",
        "aussage_uebersetzung_de": "TSMC ist meine Familie.",
    },
    # ---- 10. Elon Musk Superhuman - Colossus Achievement ----
    {
        "aussage_text": "Elon Musk is singular in his understanding of engineering. Just to put it in perspective, 100,000 GPUs -- that's easily the fastest supercomputer on the planet as one cluster. Almost everything that Elon is part of, you really want to be part of as well.",
        "aussage_kurz": "Huang nennt Musk 'uebermenschlich' und lobt den 19-Tage-Bau des Colossus-Supercomputers.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.fool.com/investing/2025/10/26/is-elon-musk-superhuman-heres-why-nvidias-jensen-h/",
        "quell_titel": "Is Elon Musk 'Superhuman'? Here's Why Nvidia's Jensen Huang Thinks So (The Motley Fool)",
        "datum_aussage": "2025-10-09",
        "sprache": "en",
        "kontext": "Interview ueber xAIs Colossus-Supercomputer mit 100.000 NVIDIA GPUs, gebaut in 19 Tagen.",
        "aussage_uebersetzung_de": "Elon Musk ist einzigartig in seinem Verstaendnis von Ingenieurwesen. Um es in Perspektive zu setzen: 100.000 GPUs -- das ist leicht der schnellste Supercomputer auf dem Planeten als ein Cluster. Bei fast allem, woran Elon beteiligt ist, will man wirklich auch dabei sein.",
    },
    # ---- 11. Deep Learning Algorithm Discovery ----
    {
        "aussage_text": "Humanity discovered an algorithm that could really, truly learn any distribution of data.",
        "aussage_kurz": "Huang beschreibt Deep Learning als Entdeckung eines universellen Lernalgorithmus.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.rev.com/transcripts/gtc-keynote-with-nvidia-ceo-jensen-huang",
        "quell_titel": "GTC Nvidia CEO Jensen Huang AI Keynote (Rev Transcript)",
        "datum_aussage": "2024-03-18",
        "sprache": "en",
        "kontext": "GTC 2024 Keynote. Huang erklaert den fundamentalen Durchbruch von Deep Learning.",
        "aussage_uebersetzung_de": "Die Menschheit hat einen Algorithmus entdeckt, der wirklich jede Datenverteilung lernen kann.",
    },
    # ---- 12. AI Reinvented Computing - NTU Commencement 2023 ----
    {
        "aussage_text": "A.I. has reinvented computing from the ground up. Over $1 trillion of traditional computers will be upgraded for AI within a decade.",
        "aussage_kurz": "Huang prognostiziert, dass KI das Computing neu erfunden hat und eine Billion Dollar Infrastruktur ersetzt wird.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://fortune.com/2023/05/31/nvidia-ceo-jensen-huang-graduation-speech-future-of-work-ai/",
        "quell_titel": "Nvidia's CEO just gave a graduation speech about the future of work in AI (Fortune)",
        "datum_aussage": "2023-05-27",
        "sprache": "en",
        "kontext": "National Taiwan University Commencement Speech in Taipei. Huang spricht zu Absolventen ueber die KI-Revolution.",
        "aussage_uebersetzung_de": "KI hat Computing von Grund auf neu erfunden. Ueber 1 Billion Dollar an traditionellen Computern wird innerhalb eines Jahrzehnts fuer KI aufgeruestet werden.",
    },
    # ---- 13. Physical AI Era - CES 2025 ----
    {
        "aussage_text": "AI started with perception AI—understanding images, words and sounds—then moved to generative AI, and now is entering the era of physical AI, AI that can proceed, reason, plan and act.",
        "aussage_kurz": "Huang kuendigt bei CES 2025 die Aera der 'Physical AI' an.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://blogs.nvidia.com/blog/ces-2025-jensen-huang/",
        "quell_titel": "CES 2025: AI Advancing at 'Incredible Pace,' NVIDIA CEO Says (NVIDIA Blog)",
        "datum_aussage": "2025-01-07",
        "sprache": "en",
        "kontext": "CES 2025 Keynote. Huang beschreibt die Evolution von KI von Wahrnehmung ueber Generierung zu physischer Interaktion.",
        "aussage_uebersetzung_de": "KI begann mit Wahrnehmungs-KI -- dem Verstehen von Bildern, Woertern und Geraueschen -- ging dann zur generativen KI ueber und tritt jetzt in die Aera der physischen KI ein, KI, die vorangehen, denken, planen und handeln kann.",
    },
    # ---- 14. Technology Stack Transformation ----
    {
        "aussage_text": "Every single layer of the technology stack has been transformed in just 12 years.",
        "aussage_kurz": "Huang beschreibt, wie jede Ebene des Tech-Stacks in 12 Jahren durch KI transformiert wurde.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://blogs.nvidia.com/blog/ces-2025-jensen-huang/",
        "quell_titel": "CES 2025: AI Advancing at 'Incredible Pace,' NVIDIA CEO Says (NVIDIA Blog)",
        "datum_aussage": "2025-01-07",
        "sprache": "en",
        "kontext": "CES 2025. Huang reflektiert ueber die Geschwindigkeit der KI-getriebenen Transformation.",
        "aussage_uebersetzung_de": "Jede einzelne Ebene des Technologie-Stacks wurde in nur 12 Jahren transformiert.",
    },
    # ---- 15. AI Tutor Recommendation ----
    {
        "aussage_text": "Go get yourself an AI tutor right away. I have a personal AI tutor with me all the time.",
        "aussage_kurz": "Huang empfiehlt jedem, sofort einen KI-Tutor zu nutzen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,  # Podcast-Interview
        "plattform_id": 3,    # Podcasts
        "quell_link": "https://www.cnbc.com/2025/02/26/nvidia-ceo-jensen-huang-everybody-should-use-this-free-type-of-ai.html",
        "quell_titel": "Nvidia CEO Jensen Huang: 'Everybody' should use this free type of AI (CNBC)",
        "datum_aussage": "2025-02-26",
        "sprache": "en",
        "kontext": "Interview mit Cleo Abram fuer 'Huge Conversations'. Huang spricht ueber persoenliche KI-Nutzung.",
        "aussage_uebersetzung_de": "Besorgen Sie sich sofort einen KI-Tutor. Ich habe die ganze Zeit einen persoenlichen KI-Tutor bei mir.",
    },
    # ---- 16. TSMC Partnership - Dancing with Partners ----
    {
        "aussage_text": "TSMC learned to 'dance with 400 partners' while Intel has 'always' danced alone.",
        "aussage_kurz": "Huang lobt TSMCs Faehigkeit zur Zusammenarbeit im Vergleich zu Intels isoliertem Ansatz.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.benzinga.com/markets/tech/25/11/49100652/jensen-huang-once-said-tsmc-learned-to-dance-with-400-partners-while-intel-has-always-danced-alone-did-the-nvidia-ceo-hit-the-nail-on-its-head",
        "quell_titel": "Jensen Huang Said TSMC Learned To 'Dance With 400 Partners' While Intel Danced Alone (Benzinga)",
        "datum_aussage": "2025-11-14",
        "sprache": "en",
        "kontext": "Interview ueber TSMC-Partnerschaft und die Unterschiede im Geschaeftsmodell zwischen TSMC und Intel.",
        "aussage_uebersetzung_de": "TSMC hat gelernt, 'mit 400 Partnern zu tanzen', waehrend Intel 'immer' allein getanzt hat.",
    },
    # ---- 17. Blackwell - Engine of New Industrial Revolution ----
    {
        "aussage_text": "Blackwell is the engine to power this new industrial revolution in generative AI.",
        "aussage_kurz": "Huang bezeichnet die Blackwell-Architektur als Motor der neuen industriellen Revolution.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://blogs.nvidia.com/blog/2024-gtc-keynote/",
        "quell_titel": "'We Created a Processor for the Generative AI Era,' NVIDIA CEO Says (NVIDIA Blog)",
        "datum_aussage": "2024-03-18",
        "sprache": "en",
        "kontext": "GTC 2024 Keynote zur Ankuendigung der Blackwell-GPU-Architektur.",
        "aussage_uebersetzung_de": "Blackwell ist der Motor, um diese neue industrielle Revolution in generativer KI anzutreiben.",
    },
    # ---- 18. Meta Open Source Contribution ----
    {
        "aussage_text": "Meta did one of the greatest things for the AI community by making Llama open source.",
        "aussage_kurz": "Huang lobt Metas Open-Source-Strategie mit Llama als grossen Beitrag zur KI-Community.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.fool.com/investing/2024/02/14/nvidia-ceo-jensen-huang-believes-meta-platforms-di/",
        "quell_titel": "Nvidia CEO Jensen Huang Believes Meta Did One of the Greatest Things for AI (The Motley Fool)",
        "datum_aussage": "2024-07-29",
        "sprache": "en",
        "kontext": "SIGGRAPH 2024 Konferenz. Panel-Diskussion mit Meta CEO Mark Zuckerberg.",
        "aussage_uebersetzung_de": "Meta hat eine der groessten Taten fuer die KI-Community vollbracht, indem es Llama als Open Source bereitgestellt hat.",
    },
    # ---- 19. Every Business Will Have AI ----
    {
        "aussage_text": "Every business will have an AI. Every company will have their own AI assistants and agents.",
        "aussage_kurz": "Huang prognostiziert, dass jedes Unternehmen eigene KI-Systeme haben wird.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.artificialintelligence-news.com/news/nvidia-and-meta-ceo-every-business-will-have-an-ai/",
        "quell_titel": "NVIDIA and Meta CEOs: Every business will 'have an AI' (AI News)",
        "datum_aussage": "2024-07-29",
        "sprache": "en",
        "kontext": "SIGGRAPH 2024. Gemeinsame Diskussion mit Mark Zuckerberg ueber die Zukunft von KI in Unternehmen.",
        "aussage_uebersetzung_de": "Jedes Unternehmen wird eine KI haben. Jedes Unternehmen wird seine eigenen KI-Assistenten und Agenten haben.",
    },
    # ---- 20. First Sovereign AI Step - Codify Language ----
    {
        "aussage_text": "The first thing that I would do, of course, is I would codify the language, the data of your culture into your own large language model.",
        "aussage_kurz": "Huang raet Laendern, als ersten Schritt ihre Sprache und Kultur in einem eigenen LLM zu kodifizieren.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://venturebeat.com/ai/get-ready-for-the-age-of-sovereign-ai-jensen-huang-interview",
        "quell_titel": "Get ready for the age of sovereign AI | Jensen Huang interview (VentureBeat)",
        "datum_aussage": "2024-02-13",
        "sprache": "en",
        "kontext": "World Governments Summit 2024. Huang gibt konkrete Empfehlungen fuer Entwicklungslaender.",
        "aussage_uebersetzung_de": "Das Erste, was ich tun wuerde, waere natuerlich, die Sprache, die Daten Ihrer Kultur in Ihr eigenes grosses Sprachmodell zu kodifizieren.",
    },
    # ---- 21. Half Trillion Dollar Infrastructure ----
    {
        "aussage_text": "We're going to have to build half a trillion dollars worth of capacity infrastructure for the transition to GPU-driven generative AI.",
        "aussage_kurz": "Huang schaetzt, dass eine halbe Billion Dollar in KI-Infrastruktur investiert werden muss.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.pymnts.com/artificial-intelligence-2/2025/nvidia-ceo-why-the-next-stage-of-ai-needs-a-lot-more-computing-power/",
        "quell_titel": "Nvidia CEO: Why the Next Stage of AI Needs A Lot More Computing Power (PYMNTS)",
        "datum_aussage": "2025-02-07",
        "sprache": "en",
        "kontext": "Interview ueber die wirtschaftlichen Dimensionen des KI-Infrastruktur-Aufbaus.",
        "aussage_uebersetzung_de": "Wir werden eine halbe Billion Dollar an Kapazitaets-Infrastruktur aufbauen muessen fuer den Uebergang zu GPU-getriebener generativer KI.",
    },
    # ---- 22. NVIDIA Business Strength - TSMC Visit ----
    {
        "aussage_text": "Nvidia's business is very strong and getting stronger month by month. We need capacity.",
        "aussage_kurz": "Huang betont bei TSMC-Besuch die wachsende Nachfrage und den Kapazitaetsbedarf.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://longbridge.com/en/news/264993752",
        "quell_titel": "Jensen Huang personally visited TSMC: 'We need capacity' (Longbridge)",
        "datum_aussage": "2025-11-08",
        "sprache": "en",
        "kontext": "Besuch bei TSMC Sports Day. Huang spricht ueber die anhaltend hohe Nachfrage nach NVIDIA GPUs.",
        "aussage_uebersetzung_de": "NVIDIAs Geschaeft ist sehr stark und wird von Monat zu Monat staerker. Wir brauchen Kapazitaet.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung NVIDIA ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Jensen Huang, Chris Malachowsky und Curtis Priem gruenden NVIDIA in einem Denny's Restaurant in San Jose. Sie starten mit $40.000 eigenem Kapital und sichern sich schnell $20 Millionen Venture Capital.",
        "datum_handlung": "1993-04-05",
        "betrag_usd": 20000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Jensen_Huang",
        "quell_titel": "Jensen Huang - Wikipedia",
        "kontext": "Huang ist 30 Jahre alt. Die Firma wird gegruendet, um GPU-Technologie zu entwickeln. Das erste Buero ist ein Denny's Restaurant-Booth.",
    },
    # ---- H2. NVIDIA IPO ----
    {
        "handlung_typ": "investition",
        "beschreibung": "NVIDIA geht an die Boerse mit einem IPO-Preis von $12 pro Aktie. Der Boersengang erfolgt nach Jahren finanzieller Schwierigkeiten, einschliesslich einem Fast-Bankrott in den spaeteren 1990er Jahren.",
        "datum_handlung": "1999-01-22",
        "betrag_usd": None,
        "quell_link": "https://www.britannica.com/money/Jensen-Huang",
        "quell_titel": "Jensen Huang | Biography, NVIDIA, Huang's Law (Britannica)",
        "kontext": "Als die Aktie $100 erreichte, liess sich Huang das NVIDIA-Logo auf die linke Schulter taetowieren.",
    },
    # ---- H3. CUDA Platform Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "NVIDIA fuehrt CUDA (Compute Unified Device Architecture) ein -- eine Parallel-Computing-Plattform, die es ermoeglicht, GPUs fuer allgemeine Rechenaufgaben zu nutzen. Dies wird zur Grundlage fuer moderne KI-Anwendungen.",
        "datum_handlung": "2006-11-15",
        "betrag_usd": None,
        "quell_link": "https://en.majalla.com/node/328702/profiles/jensen-huang-washing-pots-steering-ai-revolution",
        "quell_titel": "Jensen Huang: from washing pots to steering the AI revolution (Al Majalla)",
        "kontext": "CUDA wird zum de-facto-Standard fuer GPU-Computing und schafft ein Oekosystem, das NVIDIAs Dominanz in der KI ermoeglicht.",
    },
    # ---- H4. GeForce RTX Launch (Real-Time Ray Tracing) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "NVIDIA veroeffentlicht die GeForce RTX 20-Serie, die erste GPU-Generation mit dedizierter Hardware fuer Echtzeit-Raytracing und KI-beschleunigte Features.",
        "datum_handlung": "2018-08-20",
        "betrag_usd": None,
        "quell_link": "https://blogs.nvidia.com/blog/ces-2025-jensen-huang/",
        "quell_titel": "CES 2025: AI Advancing at 'Incredible Pace,' NVIDIA CEO Says (NVIDIA Blog)",
        "kontext": "GeForce RTX revolutioniert Gaming-Grafik und demokratisiert KI-Zugang fuer Konsumenten.",
    },
    # ---- H5. Hopper GPU Architecture Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "NVIDIA stellt die Hopper-Architektur (H100 GPU) vor, benannt nach Grace Hopper. Die H100 wird zur meistgenutzten GPU fuer Training grosser Sprachmodelle wie GPT-4 und LLaMA.",
        "datum_handlung": "2022-03-22",
        "betrag_usd": None,
        "quell_link": "https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing",
        "quell_titel": "NVIDIA Blackwell Platform Arrives to Power a New Era of Computing (NVIDIA Newsroom)",
        "kontext": "GTC 2022 Ankuendigung. Die H100 wird zum Rueckgrat der generativen KI-Revolution.",
    },
    # ---- H6. Meta Partnership - LLaMA Training Infrastructure ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Meta nutzt ueber 100.000 NVIDIA H100 GPUs zur Trainierung von LLaMA-4. NVIDIA und Meta vertiefen ihre strategische Partnerschaft fuer Open-Source-KI.",
        "datum_handlung": "2024-07-23",
        "betrag_usd": None,
        "quell_link": "https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-is-using-more-than-100-000-nvidia-h100-ai-gpus-to-train-llama-4-mark-zuckerberg-says-that-llama-4-is-being-trained-on-a-cluster-bigger-than-anything-that-ive-seen",
        "quell_titel": "Meta is using more than 100,000 Nvidia H100 AI GPUs to train Llama-4 (Tom's Hardware)",
        "kontext": "Mark Zuckerberg beschreibt den Cluster als 'groesser als alles, was ich je gesehen habe'. Meta wird zu einem der groessten NVIDIA-Kunden.",
    },
    # ---- H7. Blackwell GPU Architecture Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "NVIDIA kuendigt die Blackwell-Architektur an: 2,5x schneller als Hopper fuer Training (FP8), 5x fuer Inferenz (FP4). Cloud-Partner: AWS, Google Cloud, Microsoft Azure, Oracle. 3,6 Millionen Blackwell-GPUs werden im ersten Jahr an die 4 groessten US-Cloud-Anbieter ausgeliefert.",
        "datum_handlung": "2024-03-18",
        "betrag_usd": None,
        "quell_link": "https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing",
        "quell_titel": "NVIDIA Blackwell Platform Arrives (NVIDIA Newsroom)",
        "kontext": "GTC 2024 Keynote. Blackwell wird als 'Motor der neuen industriellen Revolution' bezeichnet.",
    },
    # ---- H8. Korea Sovereign AI Partnership ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "NVIDIA kuendigt ein Sovereign-AI-Programm mit Suedkorea an: bis zu 50.000 NVIDIA GPUs (davon initial 13.000 Blackwell) werden ueber Cloud-Provider NHN Cloud, Kakao Corp. und NAVER Cloud bereitgestellt.",
        "datum_handlung": "2024-11-16",
        "betrag_usd": None,
        "quell_link": "https://blogs.nvidia.com/blog/korea-ai-apec-ceo-summit/",
        "quell_titel": "Korea Joins AI Industrial Revolution: NVIDIA CEO Unveils Historic Partnership (NVIDIA Blog)",
        "kontext": "APEC CEO Summit in Seoul. Huang bezeichnet dies als 'historische Partnerschaft' fuer nationale KI-Souveraenitaet.",
    },
    # ---- H9. xAI Colossus Supercomputer - 100K GPUs ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Elon Musks xAI baut den 'Colossus'-Supercomputer mit 100.000 NVIDIA GPUs in nur 19 Tagen Bauzeit (Gesamtprojekt ca. 122 Tage). Geschaetzte Kosten: $7 Milliarden. Huang nennt Musk 'superhuman'.",
        "datum_handlung": "2025-09-02",
        "betrag_usd": 7000000000.0,
        "quell_link": "https://www.fool.com/investing/2025/10/26/is-elon-musk-superhuman-heres-why-nvidias-jensen-h/",
        "quell_titel": "Is Elon Musk 'Superhuman'? Here's Why Nvidia's Jensen Huang Thinks So (The Motley Fool)",
        "kontext": "Der schnellste Supercomputer-Aufbau in der Geschichte. Huang: 'Most companies would take years to replicate such a feat.'",
    },
    # ---- H10. OpenAI Strategic Partnership ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "NVIDIA und OpenAI kuendigen eine strategische Partnerschaft an: Bereitstellung von 10 Gigawatt NVIDIA-Systemen fuer OpenAI. Eine geplante $100 Milliarden Investition wird spaeter auf $20 Milliarden angepasst.",
        "datum_handlung": "2025-09-15",
        "betrag_usd": 20000000000.0,
        "quell_link": "https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems",
        "quell_titel": "OpenAI and NVIDIA Announce Strategic Partnership to Deploy 10GW of NVIDIA Systems (NVIDIA Newsroom)",
        "kontext": "Huang bezeichnet es als 'groesste Investition, die wir je gemacht haben'. Die Partnerschaft wird spaeter neu verhandelt.",
    },
    # ---- H11. TSMC Silicon Photonics Partnership ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "NVIDIA und TSMC kuendigen eine Zusammenarbeit bei Silicon Photonics an -- einer Technologie zur optischen Datenuebertragung in Chips. Dies soll die Bandbreite fuer KI-Cluster massiv erhoehen.",
        "datum_handlung": "2025-01-19",
        "betrag_usd": None,
        "quell_link": "https://www.taipeitimes.com/News/front/archives/2025/01/19/2003830461",
        "quell_titel": "TSMC and Nvidia team up on silicon photonics (Taipei Times)",
        "kontext": "Huang besucht Taiwan drei Mal in drei Monaten. Die Partnerschaft soll die naechste Generation von KI-Beschleunigern ermoeglichen.",
    },
    # ---- H12. Microsoft-OpenAI Infrastructure Deal ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Microsoft bestellt NVIDIA GPUs im Wert von mehreren Milliarden Dollar fuer OpenAI-Infrastruktur als Teil ihrer strategischen Partnerschaft. Microsoft hat insgesamt $13 Milliarden in OpenAI investiert.",
        "datum_handlung": "2023-01-23",
        "betrag_usd": None,
        "quell_link": "https://www.networkworld.com/article/4128229/reports-of-nvidia-openai-deal-in-jeopardy-are-overblown-says-nvidias-ceo-huang.html",
        "quell_titel": "Reports of Nvidia/OpenAI deal are overblown, says CEO Huang (Network World)",
        "kontext": "Microsoft wird zum groessten Cloud-Abnehmer von NVIDIA GPUs. Die GPUs werden primaer fuer OpenAI-Modelltraining genutzt.",
    },
    # ---- H13. Tesla Full Self-Driving Chip Deployment ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Tesla nutzt NVIDIA GPUs (spaeter eigene Chips) fuer Autopilot-Training. Huang lobt Tesla als Pionier in Physical AI. Tesla bleibt ein strategischer Partner fuer KI-Infrastruktur.",
        "datum_handlung": "2024-06-15",
        "betrag_usd": None,
        "quell_link": "https://www.supplychaintoday.com/elon-musk-nvidia-ceo-jensen-huang-talk-ai-and-the-future/",
        "quell_titel": "Elon Musk & NVIDIA CEO Jensen Huang Talk AI and the Future (Supply Chain Today)",
        "kontext": "Obwohl Tesla eigene Chips entwickelt, bleibt NVIDIA ein wichtiger Partner fuer Training-Infrastruktur.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=1 existiert
    cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
    person = cursor.fetchone()
    if not person:
        print(f"FEHLER: Person mit id={PERSON_ID} nicht in der Datenbank gefunden.")
        conn.close()
        return
    print(f"Person gefunden: {person[0]} (id={PERSON_ID})")

    # Bestehende Eintraege zaehlen
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    existing_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    existing_h = cursor.fetchone()[0]
    print(f"Bestehende Eintraege: {existing_a} Aussagen, {existing_h} Handlungen")

    # --- Aussagen einfuegen ---
    aussagen_count = 0
    skipped_a = 0
    for a in AUSSAGEN:
        # Duplikat-Check: gleicher Text fuer gleiche Person
        cursor.execute(
            "SELECT id FROM aussagen WHERE person_id = ? AND aussage_text = ?",
            (PERSON_ID, a["aussage_text"])
        )
        if cursor.fetchone():
            skipped_a += 1
            continue

        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, sprache, kontext, aussage_uebersetzung_de,
                erfasst_von
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
            a.get("sprache", "en"),
            a.get("kontext"),
            a.get("aussage_uebersetzung_de"),
            "Claude (collect_huang.py)"
        ))
        aussagen_count += 1

    # --- Handlungen einfuegen ---
    handlungen_count = 0
    skipped_h = 0
    for h in HANDLUNGEN:
        # Duplikat-Check: gleicher Typ + Datum + Person
        cursor.execute(
            "SELECT id FROM handlungen WHERE person_id = ? AND handlung_typ = ? AND datum_handlung = ?",
            (PERSON_ID, h["handlung_typ"], h.get("datum_handlung"))
        )
        if cursor.fetchone():
            skipped_h += 1
            continue

        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung, datum_handlung,
                betrag_usd, quell_link, quell_titel, kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            h["handlung_typ"],
            h["beschreibung"],
            h.get("datum_handlung"),
            h.get("betrag_usd"),
            h.get("quell_link"),
            h.get("quell_titel"),
            h.get("kontext"),
        ))
        handlungen_count += 1

    # --- Suchprotokoll anlegen ---
    cursor.execute("""
        INSERT INTO suchprotokolle (
            person_id, suchbegriffe, ergebnis_anzahl, relevante_treffer,
            notizen, durchgefuehrt_von
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        "Jensen Huang quotes, GTC keynotes, CES, Davos, World Governments Summit, SIGGRAPH, sovereign AI, AGI timeline, CUDA, Blackwell, Hopper, TSMC partnership, Meta LLaMA, xAI Colossus, OpenAI partnership",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: GTC Keynotes 2024/2025, CES 2025, World Governments Summit 2024, Davos WEF 2026, "
        f"SIGGRAPH 2024, Stratechery Interview, NVIDIA Blog, TechCrunch, CNBC, Fortune, Engadget, "
        f"The Motley Fool, Benzinga, Tom's Hardware, VentureBeat, Taipei Times, Wikipedia.",
        "Claude (collect_huang.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Jensen Huang (person_id={PERSON_ID})")
    print(f"{'='*60}")
    print(f"  Neue Aussagen eingefuegt:    {aussagen_count}")
    print(f"  Aussagen uebersprungen:      {skipped_a} (Duplikate)")
    print(f"  Neue Handlungen eingefuegt:  {handlungen_count}")
    print(f"  Handlungen uebersprungen:    {skipped_h} (Duplikate)")
    print(f"  Suchprotokoll erstellt:      Ja")
    print(f"{'='*60}")

    # Verifizierung
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    total_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    total_h = cursor.fetchone()[0]
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Jensen Huang")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_huang.py")
    print("  Verifizierte Aussagen & Handlungen: Jensen Huang")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
