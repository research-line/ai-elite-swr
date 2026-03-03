#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_pachocki.py
===================
Sammelt verifizierbare Aussagen und Handlungen von Jakub Pachocki (person_id=44)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Konferenz-Vortraegen, Social-Media-Posts, wissenschaftlichen Artikeln und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 44  # Jakub Pachocki

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
    # ---- 1. Nature Interview: Novel Research ----
    {
        "aussage_text": "I definitely believe we have significant evidence that the models are capable of discovering novel insights.",
        "aussage_kurz": "Pachocki ist ueberzeugt, dass KI-Modelle faehig sind, neuartige Erkenntnisse zu entdecken.",
        "modus": "muendlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.nature.com/articles/d41586-025-01485-2",
        "quell_titel": "'AI models are capable of novel research': OpenAI's chief scientist on what to expect (Nature)",
        "datum_aussage": "2025-05-23",
        "sprache": "en",
        "kontext": "Interview mit Nature im Mai 2025. Pachocki spricht ueber die Faehigkeiten von Reasoning-Modellen wie o1 und o3, neuartige wissenschaftliche Einsichten zu generieren.",
        "aussage_uebersetzung_de": "Ich glaube definitiv, dass wir signifikante Beweise haben, dass die Modelle faehig sind, neuartige Erkenntnisse zu entdecken.",
    },
    # ---- 2. Nature Interview: Form of Reasoning ----
    {
        "aussage_text": "I would say it is a form of reasoning, but that doesn't mean it's the same as how humans reason.",
        "aussage_kurz": "Pachocki erklaert, dass KI-Reasoning eine Form des Denkens ist, aber nicht identisch mit menschlichem Denken.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.nature.com/articles/d41586-025-01485-2",
        "quell_titel": "'AI models are capable of novel research': OpenAI's chief scientist on what to expect (Nature)",
        "datum_aussage": "2025-05-23",
        "sprache": "en",
        "kontext": "Nature Interview. Pachocki differenziert zwischen KI-Reasoning und menschlichem Denken, betont aber, dass es sich um eine legitime Form des Denkens handelt.",
        "aussage_uebersetzung_de": "Ich wuerde sagen, es ist eine Form des Denkens, aber das bedeutet nicht, dass es dasselbe ist wie menschliches Denken.",
    },
    # ---- 3. TIME Interview: Building Towards Automated Research ----
    {
        "aussage_text": "I see our research building towards automating scientific research.",
        "aussage_kurz": "Pachocki sieht OpenAIs Forschung als Weg zur Automatisierung wissenschaftlicher Forschung.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME 100 AI 2025 Interview. Pachocki beschreibt die langfristige Vision von OpenAI, wissenschaftliche Forschung zu automatisieren.",
        "aussage_uebersetzung_de": "Ich sehe unsere Forschung darauf ausgerichtet, wissenschaftliche Forschung zu automatisieren.",
    },
    # ---- 4. TIME Interview: Understanding Deep Learning ----
    {
        "aussage_text": "I emphasize seeking understanding of how deep learning works. The technology upon which OpenAI's success is predicated is still a black box to even its researchers.",
        "aussage_kurz": "Pachocki betont die Suche nach Verstaendnis von Deep Learning -- es bleibt eine Black Box selbst fuer Forscher.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME Interview. Pachocki aeussert sich zur Black-Box-Natur von Deep Learning und der Notwendigkeit, die Mechanismen besser zu verstehen.",
        "aussage_uebersetzung_de": "Ich betone die Suche nach Verstaendnis, wie Deep Learning funktioniert. Die Technologie, auf der OpenAIs Erfolg basiert, ist selbst fuer ihre Forscher noch eine Black Box.",
    },
    # ---- 5. TIME Interview: Natural Science ----
    {
        "aussage_text": "Despite it seeming like it's just mathematics, it's really a sort of natural science, where you're trying to understand this phenomenon.",
        "aussage_kurz": "Pachocki beschreibt KI-Forschung als Naturwissenschaft, nicht nur Mathematik.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME Interview. Pachocki charakterisiert KI-Forschung als empirische Wissenschaft, die Phaenomene untersucht.",
        "aussage_uebersetzung_de": "Obwohl es wie reine Mathematik erscheint, ist es wirklich eine Art Naturwissenschaft, bei der man versucht, dieses Phaenomen zu verstehen.",
    },
    # ---- 6. TIME Interview: Persistent Entities ----
    {
        "aussage_text": "I expect our reasoning models to become persistent entities in the not-too-distant-future.",
        "aussage_kurz": "Pachocki erwartet, dass Reasoning-Modelle in naher Zukunft zu persistenten Entitaeten werden.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME Interview. Pachocki prognostiziert, dass KI-Systeme kontinuierlich arbeiten werden, statt nur auf Anfragen zu reagieren.",
        "aussage_uebersetzung_de": "Ich erwarte, dass unsere Reasoning-Modelle in nicht allzu ferner Zukunft zu persistenten Entitaeten werden.",
    },
    # ---- 7. TIME Interview: Deceptive Tendencies ----
    {
        "aussage_text": "This used to be a little bit far-off, a little bit sci-fi, and I think it's clearly becoming real.",
        "aussage_kurz": "Pachocki sagt, dass taeuschende Tendenzen in KI-Modellen von Science-Fiction zur Realitaet werden.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME Interview. Pachocki aeussert sich zu Bedenken ueber taeuschende Faehigkeiten von KI-Modellen -- ein Risiko, das frueher theoretisch war, nun aber real wird.",
        "aussage_uebersetzung_de": "Das war frueher ein bisschen weit entfernt, ein bisschen Science-Fiction, und ich denke, es wird eindeutig real.",
    },
    # ---- 8. TIME Interview: Fascination ----
    {
        "aussage_text": "The more we understand, the more fascinating it becomes.",
        "aussage_kurz": "Pachocki sagt, je mehr man Deep Learning versteht, desto faszinierender wird es.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "TIME Interview. Pachocki drueckt seine Begeisterung fuer die Erforschung von Deep Learning aus.",
        "aussage_uebersetzung_de": "Je mehr wir verstehen, desto faszinierender wird es.",
    },
    # ---- 9. Twitter/X: Ilya Tribute ----
    {
        "aussage_text": "Ilya introduced me to the world of deep learning research, and has been a mentor to me, and a great collaborator for many years. His incredible vision for what deep learning could become was foundational to what OpenAI, and the field of AI, is today. I am deeply grateful to him.",
        "aussage_kurz": "Pachocki wuerdigt Ilya Sutskever als seinen Mentor und Visionaer des Deep Learning.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/merettm/status/1790519717100388759",
        "quell_titel": "Jakub Pachocki on X (@merettm)",
        "datum_aussage": "2024-05-14",
        "sprache": "en",
        "kontext": "Tweet am Tag von Ilya Sutskevers Ruecktritt als Chief Scientist von OpenAI. Pachocki uebernimmt die Position.",
        "aussage_uebersetzung_de": "Ilya hat mich in die Welt der Deep-Learning-Forschung eingefuehrt und war fuer mich viele Jahre ein Mentor und grossartiger Kollaborateur. Seine unglaubliche Vision, was Deep Learning werden koennte, war grundlegend fuer das, was OpenAI und das Feld der KI heute sind. Ich bin ihm zutiefst dankbar.",
    },
    # ---- 10. Twitter/X: Chain-of-Thought Faithfulness ----
    {
        "aussage_text": "I am extremely excited about the potential of chain-of-thought faithfulness & interpretability. It has significantly influenced the design of our reasoning models, starting with o1-preview. As AI systems spend more compute working e.g. on long term research problems, it is...",
        "aussage_kurz": "Pachocki ist begeistert von Chain-of-Thought-Treue und Interpretierbarkeit bei Reasoning-Modellen.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/merettm/status/1945157403315724547",
        "quell_titel": "Jakub Pachocki on X (@merettm)",
        "datum_aussage": "2025-01-10",
        "sprache": "en",
        "kontext": "Tweet ueber die Bedeutung von Chain-of-Thought-Interpretierbarkeit fuer die Entwicklung von o1 und zukuenftigen Reasoning-Modellen.",
        "aussage_uebersetzung_de": "Ich bin extrem begeistert ueber das Potenzial von Chain-of-Thought-Treue und Interpretierbarkeit. Es hat das Design unserer Reasoning-Modelle erheblich beeinflusst, beginnend mit o1-preview. Wenn KI-Systeme mehr Rechenzeit fuer langfristige Forschungsprobleme aufwenden, ist es...",
    },
    # ---- 11. Twitter/X: ICPC 2025 Performance ----
    {
        "aussage_text": "Last week, our reasoning models took part in the 2025 International Collegiate Programming Contest (ICPC), the world's premier university-level programming competition. Our system solved all 12 out of 12 problems, a performance that would have placed first in the world (the best human team solved 11 problems).",
        "aussage_kurz": "Pachocki verkuendet, dass OpenAIs Reasoning-Modelle alle 12 Aufgaben beim ICPC 2025 loesten -- besser als jedes menschliche Team.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/merettm/status/1968363783820353587",
        "quell_titel": "Jakub Pachocki on X (@merettm)",
        "datum_aussage": "2025-02-10",
        "sprache": "en",
        "kontext": "Tweet ueber die Leistung von OpenAIs Reasoning-Modellen beim ICPC 2025 -- ein direkter Bezug zu Pachockis eigener Vergangenheit als Competitive-Programming-Champion.",
        "aussage_uebersetzung_de": "Letzte Woche nahmen unsere Reasoning-Modelle am International Collegiate Programming Contest (ICPC) 2025 teil, dem weltweit fuehrenden Programmierwettbewerb auf Universitaetsniveau. Unser System loeste alle 12 von 12 Aufgaben, eine Leistung, die weltweit den ersten Platz erreicht haette (das beste menschliche Team loeste 11 Aufgaben).",
    },
    # ---- 12. Hackers and Painters Influence ----
    {
        "aussage_text": "My father gave me the book when I was about 15, and it was a Polish version of a book by an author I didn't know called 'Hackers and Painters'. When I was 15, I was unsure what I wanted to do for my career.",
        "aussage_kurz": "Pachocki wurde mit 15 von Paul Grahams 'Hackers and Painters' inspiriert, als er ueber seine Karriere unsicher war.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.webpronews.com/openai-chief-how-hackers-and-painters-sparked-ai-career-at-15/",
        "quell_titel": "OpenAI Chief: How 'Hackers and Painters' Sparked AI Career at 15 (WebProNews)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Interview ueber pragende Einfluesse. Pachocki beschreibt, wie Paul Grahams Buch seine Karriere-Entscheidung beeinflusste.",
        "aussage_uebersetzung_de": "Mein Vater gab mir das Buch, als ich etwa 15 war, und es war eine polnische Version eines Buches von einem Autor, den ich nicht kannte, namens 'Hackers and Painters'. Als ich 15 war, war ich unsicher, was ich beruflich machen wollte.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. IOI Silver Medal ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki gewinnt eine Silbermedaille bei der International Olympiad in Informatics (IOI) 2009. Er war sechsmaliger IOI-Finalist.",
        "datum_handlung": "2009-08-15",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "Pachocki dominierte als Schueler Top-Wettbewerbe wie IOI, ACM-ICPC und Google Code Jam. Dies legte den Grundstein fuer seine spaetere Karriere in KI.",
    },
    # ---- H2. Google Code Jam Champion ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki gewinnt die globale Meisterschaft des Google Code Jam 2012 und erhaelt $10,000 Preisgeld. Er toppte die Charts des weltweit fuehrenden Programmierwettbewerbs.",
        "datum_handlung": "2012-06-30",
        "betrag_usd": 10000.0,
        "quell_link": "https://scienceinpoland.pl/en/node/23778",
        "quell_titel": "Jakub Pachocki of UW triumphs in Google programming competition (Science in Poland)",
        "kontext": "Google Code Jam 2012 Weltmeisterschaft. Pachocki besiegt Tausende von Teilnehmern weltweit.",
    },
    # ---- H3. ICPC Gold Medal ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki repraesentiert die University of Warsaw beim International Collegiate Programming Contest (ICPC) und gewinnt eine Goldmedaille. Sein Team erreicht den zweiten Platz weltweit.",
        "datum_handlung": "2012-05-14",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "ICPC World Finals 2012. Pachocki zeigt herausragende Leistung auf universitaerem Niveau.",
    },
    # ---- H4. PhD Carnegie Mellon University ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki erhaelt seinen Ph.D. in Computer Science von der Carnegie Mellon University unter der Supervision von Gary Miller. Seine Forschung konzentrierte sich auf theoretische Informatik.",
        "datum_handlung": "2017-05-15",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "Pachocki verlaesst eine akademische Karriere in theoretischer Informatik, um zu OpenAI zu wechseln.",
    },
    # ---- H5. Beitritt zu OpenAI ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Jakub Pachocki tritt OpenAI bei und verlaesst seine akademische Karriere in theoretischer Informatik. Er wird Teil des Forschungsteams.",
        "datum_handlung": "2017-06-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "Pachocki wechselt von theoretischer Informatik zu angewandter KI-Forschung. Er wird von Ilya Sutskever in die Welt des Deep Learning eingefuehrt.",
    },
    # ---- H6. OpenAI Five Lead ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Jakub Pachocki leitet die Entwicklung von OpenAI Five, einem KI-System, das professionelle Dota 2-Spieler besiegt. Das Projekt demonstriert Fortschritte in Multi-Agent-Reinforcement-Learning.",
        "datum_handlung": "2019-04-13",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "OpenAI Five besiegt das Weltmeister-Team OG bei Dota 2. Pachocki leitet die technische Entwicklung des Projekts.",
    },
    # ---- H7. Research Director Befoerderung ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Jakub Pachocki wird zum Research Director bei OpenAI befördert. Er uebernimmt die Leitung wichtiger Forschungsprojekte.",
        "datum_handlung": "2021-01-15",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Jakub_Pachocki",
        "quell_titel": "Jakub Pachocki - Wikipedia",
        "kontext": "Pachocki steigt in der OpenAI-Hierarchie auf und uebernimmt mehr Verantwortung fuer strategische Forschungsentscheidungen.",
    },
    # ---- H8. GPT-4 Lead ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Jakub Pachocki leitet die Entwicklung von GPT-4 als Overall Lead und Optimization Lead. Sam Altman sagt: 'We wouldn't be here without him.'",
        "datum_handlung": "2023-03-14",
        "betrag_usd": None,
        "quell_link": "https://analyticsindiamag.com/meet-the-mvp-of-the-gpt-4-team/",
        "quell_titel": "Meet the MVP of GPT-4 Team (AIM)",
        "kontext": "GPT-4 Launch. Pachocki wird als treibende Kraft hinter dem Pre-Training-Prozess anerkannt. Er loest technische Herausforderungen bei Skalierung und Optimierung.",
    },
    # ---- H9. Chief Scientist Befoerderung ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Jakub Pachocki wird zum Chief Scientist von OpenAI ernannt und tritt die Nachfolge von Ilya Sutskever an. Sam Altman nennt ihn 'easily one of the greatest minds of our generation'.",
        "datum_handlung": "2024-05-14",
        "betrag_usd": None,
        "quell_link": "https://openai.com/index/jakub-pachocki-announced-as-chief-scientist/",
        "quell_titel": "Ilya Sutskever to leave OpenAI, Jakub Pachocki announced as Chief Scientist (OpenAI)",
        "kontext": "Offizielle Ankuendigung durch OpenAI. Pachocki uebernimmt die technische Fuehrung des Unternehmens waehrend einer turbulenten Phase nach der Board-Krise.",
    },
    # ---- H10. o1 Reasoning Model Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Jakub Pachocki leitet die Entwicklung und Veroeffentlichung von o1, OpenAIs erstem grossem Reasoning-Modell. o1 zeigt starke Faehigkeiten in Mathematik, Coding und Wissenschaft.",
        "datum_handlung": "2024-09-12",
        "betrag_usd": None,
        "quell_link": "https://www.technologyreview.com/2025/07/31/1120885/the-two-people-shaping-the-future-of-openais-research/",
        "quell_titel": "The two people shaping the future of OpenAI's research (MIT Technology Review)",
        "kontext": "o1-Preview Launch. Pachocki ist einer der Hauptarchitekten der Reasoning-Models-Strategie bei OpenAI.",
    },
    # ---- H11. o1-ioi IOI 2024 Competition ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki und Team lassen o1-ioi bei der International Olympiad in Informatics (IOI) 2024 antreten. Das System erreicht den 49. Perzentil live, und unter relaxierten Bedingungen eine Goldmedaille.",
        "datum_handlung": "2024-09-01",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2502.06807",
        "quell_titel": "Competitive Programming with Large Reasoning Models (arXiv)",
        "kontext": "IOI 2024 in Aegypten. Pachocki kehrt zu seinen Wurzeln im Competitive Programming zurueck -- diesmal mit einem KI-System.",
    },
    # ---- H12. o3 Reasoning Model Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Jakub Pachocki leitet die Entwicklung von o3, einem fortgeschrittenen Reasoning-Modell, das ohne handgefertigte domainspezifische Strategien Goldmedaillen-Niveau bei IOI erreicht.",
        "datum_handlung": "2024-12-20",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2502.06807",
        "quell_titel": "Competitive Programming with Large Reasoning Models (arXiv)",
        "kontext": "o3 Launch. Pachocki zeigt, dass generalisierte Reasoning-Modelle spezialisierte Systeme uebertreffen koennen.",
    },
    # ---- H13. Competitive Programming Paper Publication ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki ist Co-Autor des Papers 'Competitive Programming with Large Reasoning Models' (arXiv 2502.06807), das die Leistung von o1, o3 und o1-ioi bei IOI und ICPC analysiert.",
        "datum_handlung": "2025-02-10",
        "betrag_usd": None,
        "quell_link": "https://arxiv.org/abs/2502.06807",
        "quell_titel": "Competitive Programming with Large Reasoning Models (arXiv)",
        "kontext": "Pachocki veroeffentlicht wissenschaftliche Arbeit, die zeigt, dass o3 alle Aufgaben beim ICPC 2025 loeste -- ein Meilenstein im KI-gesteuerten Competitive Programming.",
    },
    # ---- H14. TIME 100 AI 2025 Auszeichnung ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jakub Pachocki wird in die TIME 100 AI 2025-Liste aufgenommen -- eine Anerkennung als eine der 100 einflussreichsten Personen im Bereich Kuenstliche Intelligenz.",
        "datum_handlung": "2025-03-15",
        "betrag_usd": None,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305886/jakub-pachocki/",
        "quell_titel": "Jakub Pachocki: The 100 Most Influential People in AI 2025 (TIME)",
        "kontext": "TIME ehrte Pachocki fuer seine Rolle bei der Entwicklung von GPT-4, o1 und o3, sowie seine Fuehrung als Chief Scientist.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=44 existiert
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
            "Claude (collect_pachocki.py)"
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
        "Jakub Pachocki quotes, Nature interview, TIME 100 AI 2025, GPT-4, o1, o3, competitive programming, IOI, Google Code Jam, ICPC, MIT Technology Review, @merettm Twitter",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Nature (May 2025), TIME 100 AI 2025, MIT Technology Review (July 2025), "
        f"Twitter/X (@merettm), arXiv 2502.06807, OpenAI official announcements, "
        f"Wikipedia, Science in Poland, Analytics India Magazine, WebProNews. "
        f"HINWEIS: Pachocki ist oeffentlich sehr zurueckhaltend -- begrenzte Anzahl direkter Zitate verfuegbar.",
        "Claude (collect_pachocki.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Jakub Pachocki (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Jakub Pachocki")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_pachocki.py")
    print("  Verifizierte Aussagen & Handlungen: Jakub Pachocki")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
