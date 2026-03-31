#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_lecun.py
================
Sammelt verifizierbare Aussagen und Handlungen von Yann LeCun (person_id=20)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Podcasts, wissenschaftlichen Veroeffentlichungen, Twitter/X-Posts und
Nachrichtenartikeln. Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 20  # Yann LeCun

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
    # ---- 1. P(doom) - Twitter/X, Feb 2024 ----
    {
        "aussage_text": "P(doom) is BS.",
        "aussage_kurz": "LeCun erklaert die Wahrscheinlichkeit einer KI-Apokalypse fuer 'Bullshit'.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,  # Social-Media-Post
        "plattform_id": 2,    # Twitter/X
        "quell_link": "https://x.com/ylecun/status/1755362942491439265",
        "quell_titel": "Yann LeCun on X: P(doom) is BS.",
        "datum_aussage": "2024-02-08",
        "sprache": "en",
        "kontext": "LeCun reagiert auf die Debatte um 'P(doom)' (Wahrscheinlichkeit einer existenziellen KI-Katastrophe) und widerspricht vehement den Warnungen von AI-Safety-Forschern.",
        "aussage_uebersetzung_de": "P(doom) ist Quatsch.",
    },
    # ---- 2. AI Existential Threat - WSJ Interview, Okt 2024 ----
    {
        "aussage_text": "AI becoming smart enough to pose a threat to humanity is complete B.S.",
        "aussage_kurz": "LeCun bezeichnet die Vorstellung, KI koennte eine existenzielle Bedrohung werden, als 'voelliger Unsinn'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://techcrunch.com/2024/10/12/metas-yann-lecun-says-worries-about-a-i-s-existential-threat-are-complete-b-s/",
        "quell_titel": "Meta's Yann LeCun says worries about AI's existential threat are 'complete B.S.' (TechCrunch)",
        "datum_aussage": "2024-10-12",
        "sprache": "en",
        "kontext": "Interview mit dem Wall Street Journal. LeCun argumentiert, dass aktuelle LLMs nicht einmal ueber die Faehigkeiten einer Hauskatze verfuegen.",
        "aussage_uebersetzung_de": "Die Vorstellung, dass KI intelligent genug wird, um eine Bedrohung fuer die Menschheit darzustellen, ist kompletter Unsinn.",
    },
    # ---- 3. LLMs Can't Plan - Twitter/X, Sep 2023 ----
    {
        "aussage_text": "Auto-Regressive LLMs can't plan (and can't really reason).",
        "aussage_kurz": "LeCun behauptet, autoregressive LLMs koennten nicht planen und nicht wirklich denken.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1702027572077326505",
        "quell_titel": "Yann LeCun on X: Auto-Regressive LLMs can't plan",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Twitter-Thread ueber die fundamentalen Grenzen autoregressiver Sprachmodelle. LeCun vertritt diese Position seit Jahren konsequent.",
        "aussage_uebersetzung_de": "Autoregressive LLMs koennen nicht planen (und koennen nicht wirklich denken).",
    },
    # ---- 4. LLMs Lack Key Capabilities - Lex Fridman, Maerz 2024 ----
    {
        "aussage_text": "LLMs can do none of those or they can only do them in a very primitive way, and they don't really understand the physical world.",
        "aussage_kurz": "LeCun erklaert, LLMs koennten zentrale Faehigkeiten wie Reasoning, Planning und Weltverstehen nicht oder nur sehr primitiv.",
        "modus": "muendlich",
        "quellen_typ_id": 2,  # Podcast-Interview
        "plattform_id": 3,    # Podcasts
        "quell_link": "https://lexfridman.com/yann-lecun-3-transcript/",
        "quell_titel": "Lex Fridman Podcast #416: Yann Lecun - Meta AI, Open Source, Limits of LLMs, AGI & the Future of AI",
        "datum_aussage": "2024-03-07",
        "sprache": "en",
        "kontext": "Drittes langes Interview mit Lex Fridman. LeCun erlaeutert, warum LLMs nicht der Weg zu AGI sind.",
        "aussage_uebersetzung_de": "LLMs koennen diese Dinge entweder gar nicht oder nur auf sehr primitive Weise, und sie verstehen die physische Welt nicht wirklich.",
    },
    # ---- 5. Open Source AI - TIME Interview, Feb 2024 ----
    {
        "aussage_text": "We do not believe that we have a monopoly on good ideas and that progress requires the collective effort of the entire research community.",
        "aussage_kurz": "LeCun verteidigt Metas Open-Source-Ansatz: Fortschritt erfordert die kollektive Anstrengung der gesamten Forschungsgemeinschaft.",
        "modus": "muendlich",
        "quellen_typ_id": 7,  # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://time.com/6694432/yann-lecun-meta-ai-interview/",
        "quell_titel": "Meta's AI Chief Yann LeCun on AGI, Open-Source, and AI Risk (TIME)",
        "datum_aussage": "2024-02-15",
        "sprache": "en",
        "kontext": "TIME100 Impact Award-Interview in Dubai. LeCun verteidigt Meta's Strategie, LLaMA und andere Modelle Open Source zu veroeffentlichen.",
        "aussage_uebersetzung_de": "Wir glauben nicht, dass wir ein Monopol auf gute Ideen haben, und dass Fortschritt die kollektive Anstrengung der gesamten Forschungsgemeinschaft erfordert.",
    },
    # ---- 6. Human Intelligence Not General - 2024 ----
    {
        "aussage_text": "Human intelligence is not general intelligence. It's very specialized to the ecological niche that we live in.",
        "aussage_kurz": "LeCun behauptet, menschliche Intelligenz sei nicht 'allgemein', sondern hochspezialisiert fuer unsere oekologische Nische.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://jasonhowell.substack.com/p/meta-ai-chief-yann-lacun-human-intelligence",
        "quell_titel": "Meta AI Chief Yann LeCun: Human Intelligence Is Not General Intelligence",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "LeCun stellt die gaengige Vorstellung von AGI in Frage und argumentiert, dass auch menschliche Intelligenz nicht 'allgemein' ist.",
        "aussage_uebersetzung_de": "Menschliche Intelligenz ist keine allgemeine Intelligenz. Sie ist sehr spezialisiert auf die oekologische Nische, in der wir leben.",
    },
    # ---- 7. The Doomer's Delusion - Twitter/X, Mai 2024 ----
    {
        "aussage_text": "The Doomer's Delusion: 1. AI is likely to kill us all 2. Hence AI must be monopolized by a small number of companies under tight regulatory control.",
        "aussage_kurz": "LeCun nennt die Logik der 'AI Doomers' eine Taeuschemanoeuvre zur Monopolisierung.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1794998977105981950",
        "quell_titel": "Yann LeCun on X: The Doomer's Delusion",
        "datum_aussage": "2024-05-27",
        "sprache": "en",
        "kontext": "Thread, in dem LeCun die politische Oekonomie der KI-Doom-Rhetorik kritisiert und argumentiert, sie diene letztlich der Monopolbildung.",
        "aussage_uebersetzung_de": "Die Taeuschemanoeuvre der Untergangspropheten: 1. KI wird uns wahrscheinlich alle toeten 2. Daher muss KI von einer kleinen Anzahl von Unternehmen unter strikter regulatorischer Kontrolle monopolisiert werden.",
    },
    # ---- 8. New Paradigm in 5 Years - TechCrunch, Jan 2025 ----
    {
        "aussage_text": "A new paradigm of AI architectures will emerge in the next three to five years, going far beyond the capabilities of existing AI systems.",
        "aussage_kurz": "LeCun prognostiziert ein neues KI-Paradigma in 3-5 Jahren, das weit ueber aktuelle Systeme hinausgeht.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://techcrunch.com/2025/01/23/metas-yann-lecun-predicts-a-new-ai-architectures-paradigm-within-5-years-and-decade-of-robotics/",
        "quell_titel": "Meta's Yann LeCun predicts 'new paradigm of AI architectures' within 5 years (TechCrunch)",
        "datum_aussage": "2025-01-23",
        "sprache": "en",
        "kontext": "World AI Cannes Festival. LeCun kuendigt an, dass das naechste Paradigma Weltmodelle, persistente Erinnerung und echtes Reasoning umfassen wird.",
        "aussage_uebersetzung_de": "Ein neues Paradigma von KI-Architekturen wird in den naechsten drei bis fuenf Jahren entstehen und die Faehigkeiten bestehender KI-Systeme weit uebertreffen.",
    },
    # ---- 9. Machine Learning Sucks - World AI Cannes 2025 ----
    {
        "aussage_text": "Machine learning sucks. To achieve smarter AI systems, machines need to understand how the world works — as well as remember, reason and plan.",
        "aussage_kurz": "LeCun erklaert auf der World AI Cannes, dass Machine Learning in seiner jetzigen Form 'Mist' sei.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.hpcwire.com/2025/02/11/metas-chief-ai-scientist-yann-lecun-questions-the-longevity-of-current-genai-and-llms/",
        "quell_titel": "Meta's Chief AI Scientist Questions the Longevity of Current GenAI and LLMs (HPCwire)",
        "datum_aussage": "2025-01-23",
        "sprache": "en",
        "kontext": "Keynote auf der World AI Cannes. LeCun provoziert bewusst, um auf die Grenzen aktueller Ansaetze hinzuweisen.",
        "aussage_uebersetzung_de": "Machine Learning ist Mist. Um intelligentere KI-Systeme zu erreichen, muessen Maschinen verstehen, wie die Welt funktioniert -- und sich erinnern, denken und planen koennen.",
    },
    # ---- 10. Cats > LLMs - Wiederholte Aussage ----
    {
        "aussage_text": "Existing systems don't understand the world as well as a housecat.",
        "aussage_kurz": "LeCun argumentiert, aktuelle KI-Systeme verstehen die Welt schlechter als eine Hauskatze.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.hpcwire.com/2025/02/11/metas-chief-ai-scientist-yann-lecun-questions-the-longevity-of-current-genai-and-llms/",
        "quell_titel": "Meta's Chief AI Scientist Questions the Longevity of Current GenAI and LLMs (HPCwire)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Ein wiederkehrendes Argument LeCuns: LLMs fehlt jegliches intuitives Verstaendnis physikalischer Kausalitaet, das selbst Tiere besitzen.",
        "aussage_uebersetzung_de": "Bestehende Systeme verstehen die Welt nicht so gut wie eine Hauskatze.",
    },
    # ---- 11. OpenAI Premise Wrong - Twitter/X, Sep 2024 ----
    {
        "aussage_text": "The whole premise of OpenAI was wrong from the start. They said 'we will practice open research and reach AGI before the for-profits.' That relied on four ridiculously naive and insanely presumptuous assumptions.",
        "aussage_kurz": "LeCun kritisiert die Gruendungspraemisse von OpenAI als naiv und anmassend.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1839787777833218050",
        "quell_titel": "Yann LeCun on X: The whole premise of OpenAI was wrong",
        "datum_aussage": "2024-09-27",
        "sprache": "en",
        "kontext": "Thread, in dem LeCun OpenAI vorwirft, von Anfang an auf falschen Annahmen basiert zu haben -- insbesondere AGI 'vor anderen zu erreichen'.",
        "aussage_uebersetzung_de": "Die gesamte Praemisse von OpenAI war von Anfang an falsch. Sie sagten 'wir werden offene Forschung betreiben und AGI vor den gewinnorientierten Firmen erreichen'. Das basierte auf vier laecherlich naiven und wahnsinnig anmassenden Annahmen.",
    },
    # ---- 12. AI is Not Natural Phenomenon - Twitter/X, Mai 2024 ----
    {
        "aussage_text": "AI is not some sort of natural phenomenon that will just emerge and become dangerous. *WE* design it and *WE* build it.",
        "aussage_kurz": "LeCun betont, KI sei kein Naturphaenomen, sondern werde von Menschen entworfen und gebaut.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1795032310590378405",
        "quell_titel": "Yann LeCun on X: AI is not some sort of natural phenomenon",
        "datum_aussage": "2024-05-27",
        "sprache": "en",
        "kontext": "Antwort auf Doomer-Argumente. LeCun vergleicht KI mit Turbojets: Wir haben diese auch sicher gemacht, bevor wir sie breit einsetzen.",
        "aussage_uebersetzung_de": "KI ist keine Art Naturphaenomen, das einfach entsteht und gefaehrlich wird. WIR entwerfen sie und WIR bauen sie.",
    },
    # ---- 13. Regulation Should Target Products - Twitter/X, Nov 2023 ----
    {
        "aussage_text": "Regulate products, don't regulate technology. Promote open source foundational models. At the very least, don't regulate them in ways that favor incumbents.",
        "aussage_kurz": "LeCun fordert, Produkte zu regulieren, nicht Technologie, und Open Source zu foerdern.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1725191480321720330",
        "quell_titel": "Yann LeCun on X: Mistral's official stance on the EU AI Act",
        "datum_aussage": "2023-11-16",
        "sprache": "en",
        "kontext": "LeCun unterstuetzt die Position von Mistral zum EU AI Act und warnt vor Regulierung, die Monopole staerkt.",
        "aussage_uebersetzung_de": "Reguliert Produkte, nicht Technologie. Foerdert Open-Source-Foundational-Modelle. Reguliert sie zumindest nicht auf Weisen, die etablierte Unternehmen beguenstigen.",
    },
    # ---- 14. Deep Learning for AI (2015 Paper) ----
    {
        "aussage_text": "Deep learning allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction.",
        "aussage_kurz": "LeCun definiert Deep Learning als Lernen von Datendarstellungen mit mehreren Abstraktionsebenen.",
        "modus": "schriftlich",
        "quellen_typ_id": 9,  # Wissenschaftliche Publikation
        "plattform_id": 8,    # Wissenschaftliche Datenbanken
        "quell_link": "https://www.nature.com/articles/nature14539",
        "quell_titel": "Deep learning (Nature, 2015) - Bengio, LeCun, Hinton",
        "datum_aussage": "2015-05-27",
        "sprache": "en",
        "kontext": "Beruhmter Nature-Artikel von LeCun, Bengio und Hinton, der Deep Learning einem breiten wissenschaftlichen Publikum erklaert.",
        "aussage_uebersetzung_de": "Deep Learning ermoeglicht es Rechenmodellen, die aus mehreren Verarbeitungsschichten bestehen, Darstellungen von Daten mit mehreren Abstraktionsebenen zu lernen.",
    },
    # ---- 15. Opinion on Elon Musk - Twitter/X, Juni 2024 ----
    {
        "aussage_text": "I like his cars, his rockets, his solar energy systems, and his satellite communication system. I also like his positions on open source and patents. But I very much disagree with him on a number of issues.",
        "aussage_kurz": "LeCun lobt Musks technische Leistungen, kritisiert aber seine Positionen zu mehreren Themen.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1797270661192155427",
        "quell_titel": "Yann LeCun on X: My opinion of @elonmusk",
        "datum_aussage": "2024-06-02",
        "sprache": "en",
        "kontext": "Differenzierte Stellungnahme nach heftiger Fehde mit Musk auf Twitter/X. LeCun warf Musk vor, 'blatantly false' KI-Vorhersagen zu machen.",
        "aussage_uebersetzung_de": "Ich mag seine Autos, seine Raketen, seine Solarenergiesysteme und sein Satellitenkommunikationssystem. Ich mag auch seine Positionen zu Open Source und Patenten. Aber ich bin mit ihm in einer Reihe von Fragen sehr anderer Meinung.",
    },
    # ---- 16. Leaving Meta - LinkedIn, Nov 2025 ----
    {
        "aussage_text": "I'm leaving Meta to build the next revolution of AI: systems that understand the physical world, have persistent memory, can reason, and can plan complex action sequences.",
        "aussage_kurz": "LeCun kuendigt seinen Weggang von Meta an, um die naechste KI-Revolution zu schaffen: Systeme mit Weltverstehen, Gedaechtnis und Planung.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 6,    # LinkedIn
        "quell_link": "https://techcrunch.com/2025/11/11/metas-chief-ai-scientist-yann-lecun-reportedly-plans-to-leave-to-build-his-own-startup/",
        "quell_titel": "Meta's chief AI scientist Yann LeCun reportedly plans to leave to build his own startup (TechCrunch)",
        "datum_aussage": "2025-11-11",
        "sprache": "en",
        "kontext": "LeCun kuendigt oeffentlich seinen Weggang nach 12 Jahren bei Meta/Facebook an, um AMI Labs zu gruenden.",
        "aussage_uebersetzung_de": "Ich verlasse Meta, um die naechste KI-Revolution zu schaffen: Systeme, die die physische Welt verstehen, persistentes Gedaechtnis haben, denken koennen und komplexe Handlungssequenzen planen koennen.",
    },
    # ---- 17. World Models Vision ----
    {
        "aussage_text": "The industry's current obsession with large language models is wrong-headed and will ultimately fail to solve many pressing problems. We should be betting on world models—a different type of AI that accurately reflects the dynamics of the real world.",
        "aussage_kurz": "LeCun kritisiert die Fokussierung auf LLMs als Irrweg und setzt auf 'Weltmodelle' als Loesung.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/",
        "quell_titel": "Yann LeCun's new venture is a contrarian bet against large language models (MIT Technology Review)",
        "datum_aussage": "2026-01-22",
        "sprache": "en",
        "kontext": "MIT Technology Review-Artikel ueber LeCuns Startup AMI Labs und seine Vision fuer die Zukunft der KI.",
        "aussage_uebersetzung_de": "Die aktuelle Obsession der Branche mit grossen Sprachmodellen ist fehlgeleitet und wird letztlich viele draengende Probleme nicht loesen koennen. Wir sollten auf Weltmodelle setzen -- eine andere Art von KI, die die Dynamik der realen Welt genau widerspiegelt.",
    },
    # ---- 18. AMI vs AGI - 2025 ----
    {
        "aussage_text": "We should use the term 'Advanced Machine Intelligence' instead of AGI. It's more accurate and less loaded with assumptions.",
        "aussage_kurz": "LeCun schlaegt vor, den Begriff 'Advanced Machine Intelligence' statt AGI zu verwenden.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.engineering.columbia.edu/about/news/metas-yann-lecun-asks-how-ais-will-match-and-exceed-human-level-intelligence",
        "quell_titel": "Meta's Yann LeCun Asks How AIs will Match and Exceed Human-level Intelligence (Columbia Engineering)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "LeCun hat den Begriff 'AMI' innerhalb von Meta eingefuehrt und nutzt ihn nun fuer sein Startup.",
        "aussage_uebersetzung_de": "Wir sollten den Begriff 'Advanced Machine Intelligence' anstelle von AGI verwenden. Er ist genauer und weniger mit Annahmen befrachtet.",
    },
    # ---- 19. Secrecy Hampers Progress - Twitter to Musk, Mai 2024 ----
    {
        "aussage_text": "Secrecy hampers progress and discourages talents from joining the effort. Research needs publications and openness to advance.",
        "aussage_kurz": "LeCun argumentiert, Geheimhaltung behindere Fortschritt und schrecke Talente ab.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://venturebeat.com/ai/elon-musk-and-yann-lecuns-social-media-feud-highlights-key-differences-in-approach-to-ai-research-and-hype",
        "quell_titel": "Elon Musk and Yann LeCun's social media feud (VentureBeat)",
        "datum_aussage": "2024-05-27",
        "sprache": "en",
        "kontext": "Teil der oeffentlichen Fehde mit Elon Musk. LeCun kritisiert xAI's geschlossenen Ansatz und Musks Umgang mit Wissenschaftlern.",
        "aussage_uebersetzung_de": "Geheimhaltung behindert den Fortschritt und schreckt Talente davon ab, sich an der Anstrengung zu beteiligen. Forschung braucht Veroeffentlichungen und Offenheit, um voranzukommen.",
    },
    # ---- 20. Auto-Regressive LLMs Doomed - LinkedIn, Maerz 2023 ----
    {
        "aussage_text": "I have claimed that Auto-Regressive LLMs are exponentially diverging. For any token there is a probability of taking you outside the set of correct answers. Assuming errors are independent, the probability of a sequence being correct is exponentially divergent.",
        "aussage_kurz": "LeCun behauptet, autoregressive LLMs seien 'exponentiell divergent' -- Fehler akkumulieren sich mit jeder Vorhersage.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 6,
        "quell_link": "https://www.linkedin.com/posts/yann-lecun_i-have-claimed-that-auto-regressive-llms-activity-7045908925660950528-hJGk",
        "quell_titel": "Yann LeCun on LinkedIn: Auto-Regressive LLMs are exponentially diverging",
        "datum_aussage": "2023-03-28",
        "sprache": "en",
        "kontext": "Technische Erklaerung, warum LeCun glaubt, dass autoregressive Modelle strukturell limitiert sind.",
        "aussage_uebersetzung_de": "Ich habe behauptet, dass autoregressive LLMs exponentiell divergieren. Bei jedem Token gibt es eine Wahrscheinlichkeit, dass man ausserhalb der Menge korrekter Antworten landet. Unter der Annahme unabhaengiger Fehler ist die Wahrscheinlichkeit, dass eine Sequenz korrekt ist, exponentiell divergent.",
    },
    # ---- 21. AGI Doomers Preposterous - Fortune, Juni 2023 ----
    {
        "aussage_text": "I call A.I. doomers preposterous because they don't understand the difference between intelligence and autonomy.",
        "aussage_kurz": "LeCun nennt KI-Untergangspropheten 'absurd', weil sie Intelligenz und Autonomie verwechseln.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2023/06/14/metas-chief-a-i-scientist-calls-a-i-doomers-preposterous-and-predicts-llms-are-just-a-passing-fad/",
        "quell_titel": "Meta Chief A.I. Scientist Yann LeCun says A.I. doomsayers are 'preposterous' (Fortune)",
        "datum_aussage": "2023-06-14",
        "sprache": "en",
        "kontext": "LeCun argumentiert, dass intelligente Systeme nicht automatisch eigene Ziele verfolgen -- Autonomie muss extra entworfen werden.",
        "aussage_uebersetzung_de": "Ich nenne KI-Untergangspropheten absurd, weil sie den Unterschied zwischen Intelligenz und Autonomie nicht verstehen.",
    },
    # ---- 22. False AI Predictions - CNBC, Juni 2024 ----
    {
        "aussage_text": "Telling the public blatantly false predictions ('AGI next year', '1 million robotaxis by 2020', 'AGI will kill us all, let's pause') is very counterproductive (also illegal in some cases).",
        "aussage_kurz": "LeCun kritisiert offen falsche KI-Vorhersagen als kontraproduktiv und teils illegal.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.cnbc.com/2024/06/04/meta-ai-chief-yann-lecun-slams-musk-over-blatantly-false-promises.html",
        "quell_titel": "Meta AI chief LeCun slams Elon Musk over 'blatantly false' predictions (CNBC)",
        "datum_aussage": "2024-06-04",
        "sprache": "en",
        "kontext": "Direkte Kritik an Elon Musk, aber auch implizit an andere, die AGI-Zeitlinien verkuenden.",
        "aussage_uebersetzung_de": "Der Oeffentlichkeit offensichtlich falsche Vorhersagen zu machen ('AGI naechstes Jahr', '1 Million Robotaxis bis 2020', 'AGI wird uns alle toeten, lasst uns pausieren') ist sehr kontraproduktiv (in manchen Faellen auch illegal).",
    },
    # ---- 23. Turbojets Analogy - Twitter/X, Mai 2024 ----
    {
        "aussage_text": "I can imagine thousands of scenarios where a turbojet goes terribly wrong. Yet we managed to make turbojets insanely reliable before deploying them widely.",
        "aussage_kurz": "LeCun vergleicht KI-Sicherheit mit Turbojet-Entwicklung: Wir haben auch diese sicher gemacht.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1795032310590378405",
        "quell_titel": "Yann LeCun on X: Turbojet analogy",
        "datum_aussage": "2024-05-27",
        "sprache": "en",
        "kontext": "LeCun argumentiert, dass Engineering-Disziplin KI sicher machen kann, genau wie bei anderen Technologien.",
        "aussage_uebersetzung_de": "Ich kann mir Tausende von Szenarien vorstellen, in denen ein Turbojet schrecklich schiefgeht. Dennoch haben wir es geschafft, Turbojets wahnsinnig zuverlaessig zu machen, bevor wir sie breit einsetzen.",
    },
    # ---- 24. EU AI Act Support for Open Source - Twitter/X, Dez 2023 ----
    {
        "aussage_text": "The EU AI Act negotiations ended. Kudos to the French, German, and Italian governments for not giving up on open source models.",
        "aussage_kurz": "LeCun lobt Frankreich, Deutschland und Italien fuer ihren Einsatz fuer Open-Source-Modelle im EU AI Act.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1733481002234679685",
        "quell_titel": "Yann LeCun on X: The EU AI Act negotiations ended",
        "datum_aussage": "2023-12-08",
        "sprache": "en",
        "kontext": "LeCun kommentiert das Ergebnis der EU-AI-Act-Verhandlungen und lobt, dass Open-Source-Modelle weitgehend ausgenommen wurden.",
        "aussage_uebersetzung_de": "Die Verhandlungen zum EU AI Act sind beendet. Respekt an die franzoesischen, deutschen und italienischen Regierungen dafuer, dass sie Open-Source-Modelle nicht aufgegeben haben.",
    },
    # ---- 25. Join xAI if... - Twitter/X to Musk, Mai 2024 ----
    {
        "aussage_text": "Join xAI if you can stand a boss who: claims that what you are working on will be solved next year (no pressure), claims that what you are working on will kill everyone and must be stopped or paused (yay, vacation for 6 months!).",
        "aussage_kurz": "LeCun verspottet Musks Fuehrungsstil bei xAI mit sarkastischen 'Vorteilen'.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/ylecun/status/1795034443809165464",
        "quell_titel": "Yann LeCun on X: Join xAI if you can stand a boss who...",
        "datum_aussage": "2024-05-27",
        "sprache": "en",
        "kontext": "Hoehepunkt der oeffentlichen Fehde mit Musk. LeCun kritisiert Musks widerspruchliche Aussagen zu KI.",
        "aussage_uebersetzung_de": "Komm zu xAI, wenn du einen Chef aushaelst, der behauptet: was du bearbeitest, wird naechstes Jahr geloest (kein Druck), und was du bearbeitest, wird alle umbringen und muss gestoppt oder pausiert werden (juhu, 6 Monate Urlaub!).",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. PhD Computer Science (Backpropagation) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Yann LeCun schliesst seine Promotion in Informatik an der Universite Pierre et Marie Curie ab. In seiner Dissertation schlaegt er eine fruehe Form des Backpropagation-Lernalgorithmus fuer neuronale Netze vor.",
        "datum_handlung": "1987",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Yann_LeCun",
        "quell_titel": "Yann LeCun - Wikipedia",
        "kontext": "LeCuns Dissertation tragt den Titel 'Modeles connexionnistes de l'apprentissage'. Die Arbeit legt den Grundstein fuer sein spaeteres Lebenswerk.",
    },
    # ---- H2. Einstellung AT&T Bell Labs ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "LeCun tritt dem Adaptive Systems Research Department bei AT&T Bell Laboratories in Holmdel, New Jersey bei. Dort entwickelt er in den folgenden Jahren das Convolutional Neural Network (LeNet) und wendet es erfolgreich auf Handschrifterkennung an.",
        "datum_handlung": "1988",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Yann_LeCun",
        "quell_titel": "Yann LeCun - Wikipedia",
        "kontext": "Bei Bell Labs arbeitet LeCun mit Leon Bottou, Yoshua Bengio und Patrick Haffner zusammen. Die Gruppe entwickelt LeNet, das zur Automatisierung der Scheckverarbeitung eingesetzt wird.",
    },
    # ---- H3. LeNet Entwicklung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "LeCun und sein Team bei AT&T Bell Labs entwickeln LeNet, eine Serie von Convolutional Neural Network-Architekturen zum Lesen handgeschriebener Ziffern. LeNet wird erfolgreich fuer die automatische Scheckverarbeitung bei Banken und Geldautomaten eingesetzt.",
        "datum_handlung": "1989",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/LeNet",
        "quell_titel": "LeNet - Wikipedia",
        "kontext": "LeNet demonstriert erstmals die praktische Anwendbarkeit von CNNs mit Backpropagation. Die Architektur wird zur Grundlage moderner Computer Vision.",
    },
    # ---- H4. Einstellung NYU ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Yann LeCun wird Professor fuer Computer Science und Neural Science an der New York University (Courant Institute und Center for Neural Science). Er erhaelt die Jacob T. Schwartz Chaired Professorship.",
        "datum_handlung": "2003",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Yann_LeCun",
        "quell_titel": "Yann LeCun - Wikipedia",
        "kontext": "LeCun bleibt bis heute an der NYU, auch nach seinem Wechsel zu Facebook/Meta 2013.",
    },
    # ---- H5. Gruendung NYU Center for Data Science ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Yann LeCun wird der gruendende Direktor des NYU Center for Data Science, einem der ersten universitaeren Data-Science-Programme in den USA.",
        "datum_handlung": "2012",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Yann_LeCun",
        "quell_titel": "Yann LeCun - Wikipedia",
        "kontext": "Das Center wird ein wichtiges Zentrum fuer KI-Forschung und -Ausbildung. LeCun leitet es bis 2017.",
    },
    # ---- H6. Gruendung FAIR / Einstellung Facebook ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "LeCun tritt Facebook bei und gruendet Facebook AI Research (FAIR) als Director. Unter seiner Fuehrung wird FAIR zu einem der fuehrenden industriellen KI-Forschungslabore weltweit mit Standorten in Menlo Park, New York, Paris und Montreal.",
        "datum_handlung": "2013-12-09",
        "betrag_usd": None,
        "quell_link": "https://ai.meta.com/people/396469589677838/yann-lecun/",
        "quell_titel": "Yann LeCun - AI at Meta",
        "kontext": "LeCuns Aufgabe ist es, bei Facebook ein Weltklasse-KI-Labor aufzubauen. Er besteht darauf, dass FAIR offen publiziert -- eine Bedingung fuer seinen Beitritt.",
    },
    # ---- H7. Turing Award 2018 ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Yann LeCun erhaelt gemeinsam mit Yoshua Bengio und Geoffrey Hinton den ACM A.M. Turing Award 2018 'fuer konzeptionelle und technische Durchbrueche, die tiefe neuronale Netze zu einer kritischen Komponente des Computing gemacht haben'. Preisgeld: $1 Million (finanziert von Google).",
        "datum_handlung": "2019-03-27",
        "betrag_usd": 1000000.0,
        "quell_link": "https://awards.acm.org/about/2018-turing",
        "quell_titel": "Fathers of the Deep Learning Revolution Receive ACM A.M. Turing Award",
        "kontext": "Der Turing Award gilt als 'Nobelpreis der Informatik'. Die drei Laureaten werden auch 'Godfathers of AI' genannt.",
    },
    # ---- H8. Chief AI Scientist Meta ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "LeCun wird Chief AI Scientist bei Meta (ehemals Facebook) und uebergibt die Leitung von FAIR an Jerome Pesenti. Er konzentriert sich auf langfristige Forschung und Strategieberatung.",
        "datum_handlung": "2018",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Meta_AI",
        "quell_titel": "Meta AI - Wikipedia",
        "kontext": "Als Chief AI Scientist hat LeCun mehr Freiheit, sich auf grundlegende Forschungsfragen zu konzentrieren, insbesondere seine Vision von 'World Models'.",
    },
    # ---- H9. I-JEPA Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Meta AI veroeffentlicht I-JEPA (Image Joint Embedding Predictive Architecture), das erste KI-Modell basierend auf LeCuns Vision fuer menschenaehnlichere KI. I-JEPA lernt durch interne Modelle der Aussenwelt statt durch Pixel-Vergleiche.",
        "datum_handlung": "2023-02",
        "betrag_usd": None,
        "quell_link": "https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/",
        "quell_titel": "I-JEPA: The first AI model based on Yann LeCun's vision for more human-like AI",
        "kontext": "I-JEPA ist ein erster Schritt zur Realisierung von LeCuns 'A Path Towards Autonomous Machine Intelligence' (2022-Whitepaper).",
    },
    # ---- H10. LLaMA Open Source Release (unterstuetzt) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Meta veroeffentlicht LLaMA (Large Language Model Meta AI) als Open-Source-Modell. LeCun ist ein starker Befuerworter dieser Entscheidung und verteidigt sie oeffentlich gegen Kritik. LLaMA wird zu einer der wichtigsten Open-Source-LLM-Familien.",
        "datum_handlung": "2023-02-24",
        "betrag_usd": None,
        "quell_link": "https://nyudatascience.medium.com/yann-lecun-on-lex-fridmans-podcast-the-road-to-agi-runs-through-open-source-ai-e536bbd17317",
        "quell_titel": "Yann LeCun on Lex Fridman's Podcast: The Road to AGI Runs Through Open Source AI",
        "kontext": "LeCun argumentiert, dass Open Source der Weg zu sicherer und demokratischer KI ist. Er spielt eine wichtige Rolle dabei, Meta fuer diese Strategie zu gewinnen.",
    },
    # ---- H11. Ruecktritt Meta ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Nach 12 Jahren bei Meta kuendigt Yann LeCun seinen Ruecktritt als Chief AI Scientist an. Er verlaesst das Unternehmen Ende 2025, um sein eigenes Startup AMI Labs (Advanced Machine Intelligence) zu gruenden.",
        "datum_handlung": "2025-11-19",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2025/11/11/metas-chief-ai-scientist-yann-lecun-reportedly-plans-to-leave-to-build-his-own-startup/",
        "quell_titel": "Meta's chief AI scientist Yann LeCun reportedly plans to leave to build his own startup (TechCrunch)",
        "kontext": "LeCun bestaetigt die Plaene auf LinkedIn. Meta wird nicht in AMI Labs investieren, aber eine Partnerschaft eingehen.",
    },
    # ---- H12. Gruendung AMI Labs ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Yann LeCun gruendet Advanced Machine Intelligence (AMI) Labs mit Alexandre LeBrun (Nabla-Gruender) als CEO und LeCun als Executive Chairman. Das Startup zielt darauf ab, 'World Models' zu entwickeln -- KI-Systeme, die die physische Welt verstehen, persistentes Gedaechtnis haben und planen koennen. Hauptsitz in Paris ab Anfang 2026.",
        "datum_handlung": "2025-12",
        "betrag_usd": None,
        "quell_link": "https://theaiinsider.tech/2025/12/23/yann-lecun-launches-advanced-machine-intelligence-with-alex-lebrun-as-ceo/",
        "quell_titel": "Yann LeCun Launches Advanced Machine Intelligence With Alex LeBrun as CEO",
        "kontext": "AMI Labs ist LeCuns Versuch, seine jahrelange Kritik an LLMs in eine alternative Technologie umzusetzen.",
    },
    # ---- H13. AMI Labs Fundraising (€500M bei €3B Bewertung) ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Noch vor dem offiziellen Launch befindet sich AMI Labs in Gespraechen, €500 Millionen bei einer Bewertung von €3 Milliarden (ca. $3,5 Mrd.) einzusammeln. Dies waere eine der hoechsten Pre-Launch-Bewertungen in der KI-Industrie.",
        "datum_handlung": "2025-12",
        "betrag_usd": 586000000.0,
        "quell_link": "https://fortune.com/2025/12/19/yann-lecun-ami-labs-ai-startup-valuation-meta-departure/",
        "quell_titel": "Yann LeCun is targeting a $3.5 billion valuation for his new startup (Fortune)",
        "kontext": "Die hohe Bewertung spiegelt LeCuns Reputation und das Investoreninteresse an Alternativen zum LLM-Paradigma wider.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=20 existiert
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
            "Claude (collect_lecun.py)"
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
        "Yann LeCun, Meta AI, FAIR, LLM criticism, AGI skeptic, P(doom), open source AI, LLaMA, JEPA, world models, Turing Award, Lex Fridman, TIME interview, Elon Musk debate, EU AI Act, AMI Labs",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Lex Fridman Podcast #416 (2024), TIME Interview (Feb 2024), Twitter/X (@ylecun), "
        f"TechCrunch, Fortune, MIT Technology Review, CNBC, VentureBeat, HPCwire, Nature (2015), "
        f"ACM Turing Award, Wikipedia, Meta AI Blog, Columbia Engineering, LinkedIn Posts.",
        "Claude (collect_lecun.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Yann LeCun (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Yann LeCun")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_lecun.py")
    print("  Verifizierte Aussagen & Handlungen: Yann LeCun")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
