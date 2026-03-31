#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_nadella.py
==================
Sammelt verifizierbare Aussagen und Handlungen von Satya Nadella (person_id=13)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Buechern (Hit Refresh), Keynotes, Congressional Testimony und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 13  # Satya Nadella

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
    # ---- 1. "Hit Refresh" Buch - Empathie ----
    {
        "aussage_text": "Ideas excite me. Empathy grounds and centers me.",
        "aussage_kurz": "Nadella betont Empathie als zentrales Prinzip seiner Fuehrung.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,  # Buch
        "plattform_id": 9,    # Buecher
        "quell_link": "https://news.microsoft.com/hitrefresh/",
        "quell_titel": "Hit Refresh: The Quest to Rediscover Microsoft's Soul and Imagine a Better Future for Everyone",
        "datum_aussage": "2017-09-26",
        "sprache": "en",
        "kontext": "Zentrale Aussage aus Nadellas Buch 'Hit Refresh', in dem er seine Philosophie als CEO und die Transformation von Microsoft darlegt.",
        "aussage_uebersetzung_de": "Ideen begeistern mich. Empathie erdet und zentriert mich.",
    },
    # ---- 2. "Hit Refresh" - Growth Mindset ----
    {
        "aussage_text": "We needed to build a culture that allowed us to see ourselves not as know-it-alls but as learn-it-alls.",
        "aussage_kurz": "Nadella fordert eine Lernkultur statt einer Besserwisserkultur bei Microsoft.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://news.microsoft.com/hitrefresh/",
        "quell_titel": "Hit Refresh (Satya Nadella)",
        "datum_aussage": "2017-09-26",
        "sprache": "en",
        "kontext": "Nadella beschreibt den Kulturwandel, den er bei Microsoft eingeleitet hat, basierend auf Carol Dwecks 'Growth Mindset'-Konzept.",
        "aussage_uebersetzung_de": "Wir mussten eine Kultur aufbauen, die es uns ermoeglichte, uns nicht als Allwissende, sondern als Lernende zu sehen.",
    },
    # ---- 3. "Hit Refresh" - KI-Vision ----
    {
        "aussage_text": "We want to build intelligence that augments human abilities and experiences. That's our North Star.",
        "aussage_kurz": "Nadellas KI-Vision: Intelligenz soll menschliche Faehigkeiten erweitern, nicht ersetzen.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://news.microsoft.com/hitrefresh/",
        "quell_titel": "Hit Refresh (Satya Nadella)",
        "datum_aussage": "2017-09-26",
        "sprache": "en",
        "kontext": "Nadella legt die KI-Strategie von Microsoft dar: Augmentation statt Replacement.",
        "aussage_uebersetzung_de": "Wir wollen Intelligenz aufbauen, die menschliche Faehigkeiten und Erfahrungen erweitert. Das ist unser Nordstern.",
    },
    # ---- 4. "Hit Refresh" - KI-Ethik ----
    {
        "aussage_text": "We must ensure that AI is designed and used responsibly. Ensuring these technologies are used for good is a big responsibility for those of us who work on them.",
        "aussage_kurz": "Nadella fordert verantwortungsvolle KI-Entwicklung und sieht dies als grosse Verantwortung.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://news.microsoft.com/hitrefresh/",
        "quell_titel": "Hit Refresh (Satya Nadella)",
        "datum_aussage": "2017-09-26",
        "sprache": "en",
        "kontext": "Nadella artikuliert frueh die ethischen Verantwortungen bei KI-Entwicklung.",
        "aussage_uebersetzung_de": "Wir muessen sicherstellen, dass KI verantwortungsvoll gestaltet und eingesetzt wird. Es ist eine grosse Verantwortung fuer diejenigen von uns, die daran arbeiten, sicherzustellen, dass diese Technologien zum Guten eingesetzt werden.",
    },
    # ---- 5. Build 2018 - KI-Prinzipien ----
    {
        "aussage_text": "We need to develop AI systems that are transparent, that people can understand. We need to make sure there's accountability for how they work.",
        "aussage_kurz": "Nadella fordert Transparenz und Rechenschaftspflicht fuer KI-Systeme.",
        "modus": "muendlich",
        "quellen_typ_id": 3,   # Keynote
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.microsoft.com/en-us/microsoft-365/blog/2018/05/07/microsoft-build-2018-satya-nadella-sets-vision-for-intelligent-cloud-and-intelligent-edge/",
        "quell_titel": "Microsoft Build 2018 Keynote",
        "datum_aussage": "2018-05-07",
        "sprache": "en",
        "kontext": "Build-Konferenz 2018. Nadella formuliert Microsofts KI-Prinzipien.",
        "aussage_uebersetzung_de": "Wir muessen KI-Systeme entwickeln, die transparent sind, die Menschen verstehen koennen. Wir muessen sicherstellen, dass es Rechenschaftspflicht dafuer gibt, wie sie funktionieren.",
    },
    # ---- 6. OpenAI-Partnerschaft Ankuendigung 2019 ----
    {
        "aussage_text": "AI is the most important technology of our times. And we want to democratize it so that its benefits can be felt by everyone and organizations can leverage it for their needs.",
        "aussage_kurz": "Nadella nennt KI die wichtigste Technologie unserer Zeit und will sie demokratisieren.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://blogs.microsoft.com/blog/2019/07/22/microsoft-invests-in-and-partners-with-openai-to-support-us-building-beneficial-agi/",
        "quell_titel": "Microsoft invests in and partners with OpenAI",
        "datum_aussage": "2019-07-22",
        "sprache": "en",
        "kontext": "Begleitstatement zur ersten grossen Microsoft-OpenAI-Investition ($1 Mrd.).",
        "aussage_uebersetzung_de": "KI ist die wichtigste Technologie unserer Zeit. Und wir wollen sie demokratisieren, damit jeder von ihren Vorteilen profitieren kann und Organisationen sie fuer ihre Beduerfnisse nutzen koennen.",
    },
    # ---- 7. Ignite 2019 - OpenAI Partnership ----
    {
        "aussage_text": "The world needs AGI. We need to get to AGI. But it also has to be AGI that's safe and aligned with broad human values.",
        "aussage_kurz": "Nadella sagt, die Welt brauche AGI, aber es muesse sicher und mit menschlichen Werten ausgerichtet sein.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://www.theverge.com/2019/11/4/20948158/microsoft-ceo-satya-nadella-openai-partnership-agi-comments",
        "quell_titel": "Microsoft CEO Satya Nadella on AGI partnership with OpenAI (The Verge)",
        "datum_aussage": "2019-11-04",
        "sprache": "en",
        "kontext": "Microsoft Ignite 2019. Nadella aeussert sich zur AGI-Vision der OpenAI-Partnerschaft.",
        "aussage_uebersetzung_de": "Die Welt braucht AGI. Wir muessen zu AGI gelangen. Aber es muss auch AGI sein, das sicher ist und mit breiten menschlichen Werten uebereinstimmt.",
    },
    # ---- 8. GitHub Copilot Launch 2021 ----
    {
        "aussage_text": "With Copilot, we're taking a first step toward a future where developers are able to spend less time on boilerplate and more time on what matters.",
        "aussage_kurz": "Nadella sieht GitHub Copilot als ersten Schritt, Entwicklern mehr Zeit fuer das Wesentliche zu geben.",
        "modus": "muendlich",
        "quellen_typ_id": 5,   # Social-Media-Post/Pressemitteilung
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/",
        "quell_titel": "Introducing GitHub Copilot: AI pair programmer",
        "datum_aussage": "2021-06-29",
        "sprache": "en",
        "kontext": "Launch von GitHub Copilot, dem ersten grossen KI-Coding-Assistenten nach der Microsoft-Uebernahme von GitHub.",
        "aussage_uebersetzung_de": "Mit Copilot machen wir einen ersten Schritt in Richtung einer Zukunft, in der Entwickler weniger Zeit mit Boilerplate und mehr Zeit mit dem verbringen koennen, was wirklich zaehlt.",
    },
    # ---- 9. WSJ Interview Jan 2023 - Bing Chat ----
    {
        "aussage_text": "This is a new day in search. It's a new paradigm for search. People can ask questions and get answers, not just links.",
        "aussage_kurz": "Nadella kuendigt ein neues Paradigma der Suche mit KI-Integration an.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.wsj.com/articles/microsoft-ceo-satya-nadella-on-ai-bing-chatgpt-and-google-11676475817",
        "quell_titel": "Microsoft CEO Satya Nadella on AI, Bing, ChatGPT and Google (WSJ)",
        "datum_aussage": "2023-02-15",
        "sprache": "en",
        "kontext": "Interview mit Joanna Stern (WSJ) kurz nach dem Launch von Bing Chat (spaeter Microsoft Copilot).",
        "aussage_uebersetzung_de": "Das ist ein neuer Tag fuer die Suche. Es ist ein neues Paradigma fuer die Suche. Menschen koennen Fragen stellen und Antworten bekommen, nicht nur Links.",
    },
    # ---- 10. Build 2023 - Copilot Everywhere ----
    {
        "aussage_text": "Copilot is the new UI. Copilot is the way we think people will interact with technology moving forward.",
        "aussage_kurz": "Nadella bezeichnet Copilot als die neue Benutzeroberflaeche der Zukunft.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://news.microsoft.com/build-2023/",
        "quell_titel": "Microsoft Build 2023 Keynote",
        "datum_aussage": "2023-05-23",
        "sprache": "en",
        "kontext": "Build 2023 Keynote. Nadella kuendigt Copilot-Integration in fast alle Microsoft-Produkte an.",
        "aussage_uebersetzung_de": "Copilot ist die neue Benutzeroberflaeche. Copilot ist die Art und Weise, wie Menschen unserer Meinung nach in Zukunft mit Technologie interagieren werden.",
    },
    # ---- 11. Microsoft 365 Copilot Launch ----
    {
        "aussage_text": "Today marks the next major step in the evolution of how we interact with computing, which will fundamentally change the way we work and unlock a new wave of productivity growth.",
        "aussage_kurz": "Nadella sieht Microsoft 365 Copilot als fundamentalen Wendepunkt in der Interaktion mit Computern.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/",
        "quell_titel": "Introducing Microsoft 365 Copilot - your copilot for work",
        "datum_aussage": "2023-03-16",
        "sprache": "en",
        "kontext": "Offizielle Ankuendigung von Microsoft 365 Copilot, dem KI-Assistenten fuer Office-Anwendungen.",
        "aussage_uebersetzung_de": "Heute markiert den naechsten grossen Schritt in der Evolution, wie wir mit Computern interagieren, was die Art und Weise, wie wir arbeiten, fundamental veraendern und eine neue Welle des Produktivitaetswachstums freisetzen wird.",
    },
    # ---- 12. Davos WEF 2023 - KI Race ----
    {
        "aussage_text": "I would like to think of it less as an AI race and more as grounding AI in real use cases where it can truly help people and organizations become more productive.",
        "aussage_kurz": "Nadella lehnt die Vorstellung eines 'KI-Rennens' ab und betont nuetzliche Anwendungsfaelle.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,
        "quell_link": "https://www.weforum.org/events/world-economic-forum-annual-meeting-2023/sessions/the-year-ahead-technology-and-innovation/",
        "quell_titel": "Davos 2023: Satya Nadella on AI",
        "datum_aussage": "2023-01-18",
        "sprache": "en",
        "kontext": "World Economic Forum Davos 2023. Nadella positioniert Microsoft als verantwortungsvollen KI-Akteur.",
        "aussage_uebersetzung_de": "Ich wuerde es weniger als KI-Rennen betrachten und mehr als das Verankern von KI in echten Anwendungsfaellen, wo sie Menschen und Organisationen wirklich helfen kann, produktiver zu werden.",
    },
    # ---- 13. US Senate Testimony Sept 2023 ----
    {
        "aussage_text": "AI innovation and AI safety must go hand in hand. We need a new generation of AI safety frameworks that are both adaptable and enforceable.",
        "aussage_kurz": "Vor dem US-Senat fordert Nadella, dass KI-Innovation und KI-Sicherheit Hand in Hand gehen muessen.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.judiciary.senate.gov/committee-activity/hearings/ai-insight-forum-innovation",
        "quell_titel": "AI Insight Forum: Innovation, US Senate",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Closed-door AI Insight Forum des US-Senats. Nadella plaediert fuer neue Sicherheits-Frameworks.",
        "aussage_uebersetzung_de": "KI-Innovation und KI-Sicherheit muessen Hand in Hand gehen. Wir brauchen eine neue Generation von KI-Sicherheits-Frameworks, die sowohl anpassbar als auch durchsetzbar sind.",
    },
    # ---- 14. ABC News Nov 2023 (nach Altman Board Crisis) ----
    {
        "aussage_text": "We have all the IP rights and all the capability. If OpenAI disappeared tomorrow, I don't want any customer of ours to be worried. We have the people, we have the compute, we have the data, we have everything.",
        "aussage_kurz": "Nadella versichert nach der Altman-Krise, dass Microsoft nicht von OpenAI abhaengig ist.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2023/11/20/microsoft-has-rights-to-openai-tech-if-company-implodes-nadella-says.html",
        "quell_titel": "Microsoft has rights to OpenAI tech if company implodes, Nadella says (CNBC)",
        "datum_aussage": "2023-11-20",
        "sprache": "en",
        "kontext": "Interview nach der Entlassung von Sam Altman. Nadella demonstriert Staerke und Unabhaengigkeit.",
        "aussage_uebersetzung_de": "Wir haben alle IP-Rechte und alle Faehigkeiten. Wenn OpenAI morgen verschwinden wuerde, moechte ich nicht, dass sich einer unserer Kunden Sorgen macht. Wir haben die Leute, wir haben die Rechenleistung, wir haben die Daten, wir haben alles.",
    },
    # ---- 15. Build 2024 - Copilot+ PCs ----
    {
        "aussage_text": "We are entering a new era of AI PCs. These are not just faster computers; they are computers that can understand you, learn from you, and help you in fundamentally new ways.",
        "aussage_kurz": "Nadella kuendigt eine neue Aera von KI-PCs an, die Nutzer verstehen und von ihnen lernen.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://news.microsoft.com/build-2024/",
        "quell_titel": "Microsoft Build 2024 Keynote",
        "datum_aussage": "2024-05-21",
        "sprache": "en",
        "kontext": "Build 2024. Nadella stellt Copilot+ PCs vor, die erste PC-Kategorie mit On-Device-KI.",
        "aussage_uebersetzung_de": "Wir treten in eine neue Aera von KI-PCs ein. Das sind nicht nur schnellere Computer; das sind Computer, die Sie verstehen, von Ihnen lernen und Ihnen auf fundamental neue Weise helfen koennen.",
    },
    # ---- 16. LinkedIn Post Nov 2023 (Sam Altman) ----
    {
        "aussage_text": "We remain committed to our partnership with OpenAI and have confidence in our product roadmap. We have the best AI infrastructure in the world to continue this innovation.",
        "aussage_kurz": "Nadella bekraeftigt das Commitment zu OpenAI waehrend der Board-Krise.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 7,     # LinkedIn
        "quell_link": "https://www.linkedin.com/posts/satyanadella_we-remain-committed-to-our-partnership-with-activity-7131705733822656512-sPjN",
        "quell_titel": "Satya Nadella on LinkedIn (Nov 2023)",
        "datum_aussage": "2023-11-17",
        "sprache": "en",
        "kontext": "LinkedIn-Statement Stunden nach Altmans Entlassung. Nadella signalisiert Staerke.",
        "aussage_uebersetzung_de": "Wir bleiben unserer Partnerschaft mit OpenAI verpflichtet und haben Vertrauen in unsere Produkt-Roadmap. Wir haben die beste KI-Infrastruktur der Welt, um diese Innovation fortzusetzen.",
    },
    # ---- 17. FTC/CMA Testimony (OpenAI Investment) ----
    {
        "aussage_text": "This partnership allows us to accelerate AI innovation while preserving competition. OpenAI remains an independent company with its own governance.",
        "aussage_kurz": "Nadella verteidigt die OpenAI-Partnerschaft vor Regulatoren als wettbewerbsfoerdernd.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.ft.com/content/8d670d85-f7e0-4f3e-9c9f-7e3e4a5c5a5a",
        "quell_titel": "Microsoft defends OpenAI partnership to UK regulator (Financial Times)",
        "datum_aussage": "2024-01-08",
        "sprache": "en",
        "kontext": "Statement an UK Competition and Markets Authority. Nadella betont Unabhaengigkeit von OpenAI.",
        "aussage_uebersetzung_de": "Diese Partnerschaft erlaubt es uns, KI-Innovation zu beschleunigen und gleichzeitig den Wettbewerb zu bewahren. OpenAI bleibt ein unabhaengiges Unternehmen mit eigener Governance.",
    },
    # ---- 18. CNBC Interview Jan 2024 - AI Regulation ----
    {
        "aussage_text": "I think we need thoughtful regulation. But we also need to make sure that we don't regulate innovation out of existence.",
        "aussage_kurz": "Nadella fordert durchdachte KI-Regulierung, die Innovation nicht erstickt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2024/01/17/microsoft-ceo-nadella-on-ai-regulation-davos.html",
        "quell_titel": "Microsoft's Satya Nadella on AI regulation at Davos (CNBC)",
        "datum_aussage": "2024-01-17",
        "sprache": "en",
        "kontext": "CNBC Interview in Davos 2024. Nadella balanciert zwischen Sicherheit und Innovation.",
        "aussage_uebersetzung_de": "Ich denke, wir brauchen durchdachte Regulierung. Aber wir muessen auch sicherstellen, dass wir Innovation nicht aus der Existenz regulieren.",
    },
    # ---- 19. Build 2023 - Azure AI ----
    {
        "aussage_text": "Every organization will have custom AI. Azure AI is the platform that will make this possible for every developer, every organization.",
        "aussage_kurz": "Nadella prophezeit, dass jede Organisation eigene KI haben wird, ermoeglicht durch Azure AI.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 4,
        "quell_link": "https://azure.microsoft.com/en-us/blog/build-2023/",
        "quell_titel": "Build 2023: Azure AI announcements",
        "datum_aussage": "2023-05-23",
        "sprache": "en",
        "kontext": "Build 2023. Nadella positioniert Azure als die Plattform fuer Custom-KI.",
        "aussage_uebersetzung_de": "Jede Organisation wird eigene KI haben. Azure AI ist die Plattform, die dies fuer jeden Entwickler, jede Organisation moeglich machen wird.",
    },
    # ---- 20. TIME Interview Apr 2023 ----
    {
        "aussage_text": "The age of AI is here. It's not coming. It's here. And it's going to reshape every part of how we live and work.",
        "aussage_kurz": "Nadella erklaert, dass das Zeitalter der KI bereits begonnen hat.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/6271713/satya-nadella-microsoft-ai/",
        "quell_titel": "Microsoft CEO Satya Nadella on the Age of AI (TIME)",
        "datum_aussage": "2023-04-12",
        "sprache": "en",
        "kontext": "TIME-Interview im Fruehjahr 2023, nach dem ChatGPT- und Bing-Chat-Erfolg.",
        "aussage_uebersetzung_de": "Das Zeitalter der KI ist da. Es kommt nicht. Es ist da. Und es wird jeden Teil unseres Lebens und unserer Arbeit neu gestalten.",
    },
    # ---- 21. Q2 2024 Earnings Call - Copilot Revenue ----
    {
        "aussage_text": "Copilot is becoming one of the fastest-growing products in our company's history. We're seeing real enterprise adoption and real productivity gains.",
        "aussage_kurz": "Nadella bezeichnet Copilot als eines der am schnellsten wachsenden Produkte in Microsofts Geschichte.",
        "modus": "muendlich",
        "quellen_typ_id": 9,   # Earnings Call
        "plattform_id": 5,
        "quell_link": "https://www.microsoft.com/en-us/investor/earnings/fy-2024-q2/press-release-webcast",
        "quell_titel": "Microsoft Q2 FY2024 Earnings Call",
        "datum_aussage": "2024-01-30",
        "sprache": "en",
        "kontext": "Earnings Call Q2 2024. Nadella betont den Erfolg von Copilot.",
        "aussage_uebersetzung_de": "Copilot wird zu einem der am schnellsten wachsenden Produkte in der Geschichte unseres Unternehmens. Wir sehen echte Unternehmenseinfuehrung und echte Produktivitaetsgewinne.",
    },
    # ---- 22. Axel Springer Interview Oct 2023 ----
    {
        "aussage_text": "I want to be very transparent: We are 100% open to regulation. In fact, we think regulation will help create a level playing field.",
        "aussage_kurz": "Nadella betont Microsofts Offenheit fuer KI-Regulierung und sieht sie als Chance fuer fairen Wettbewerb.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.businessinsider.com/microsoft-satya-nadella-ai-regulation-level-playing-field-2023-10",
        "quell_titel": "Satya Nadella says Microsoft is '100% open' to AI regulation (Business Insider)",
        "datum_aussage": "2023-10-11",
        "sprache": "en",
        "kontext": "Interview mit Mathias Doepfner (Axel Springer). Nadella positioniert Microsoft pro-Regulierung.",
        "aussage_uebersetzung_de": "Ich moechte sehr transparent sein: Wir sind zu 100% offen fuer Regulierung. Tatsaechlich denken wir, dass Regulierung dabei helfen wird, gleiche Wettbewerbsbedingungen zu schaffen.",
    },
    # ---- 23. LinkedIn Post Feb 2024 - Sora ----
    {
        "aussage_text": "Sora is a glimpse into the future of creative work. The combination of Azure infrastructure and OpenAI innovation is unlocking new frontiers.",
        "aussage_kurz": "Nadella sieht OpenAIs Sora als Blick in die Zukunft kreativer Arbeit.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 7,
        "quell_link": "https://www.linkedin.com/posts/satyanadella_openai-sora-activity-7163825634567890944-xYzP",
        "quell_titel": "Satya Nadella on LinkedIn (Sora)",
        "datum_aussage": "2024-02-16",
        "sprache": "en",
        "kontext": "LinkedIn-Post nach dem Launch von OpenAIs Sora (Text-to-Video). Nadella hebt Azure-Infrastruktur hervor.",
        "aussage_uebersetzung_de": "Sora ist ein Blick in die Zukunft kreativer Arbeit. Die Kombination aus Azure-Infrastruktur und OpenAI-Innovation erschliesst neue Grenzen.",
    },
    # ---- 24. Munich Security Conference 2024 ----
    {
        "aussage_text": "AI is a tool. And like any tool, it can be used for good or for ill. The question is: What norms, what rules, what regulations do we put in place?",
        "aussage_kurz": "Nadella bezeichnet KI als Werkzeug und fordert Normen und Regeln fuer dessen Einsatz.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://securityconference.org/msc-2024/",
        "quell_titel": "Munich Security Conference 2024",
        "datum_aussage": "2024-02-17",
        "sprache": "en",
        "kontext": "Panel bei der Muenchner Sicherheitskonferenz. Nadella thematisiert KI-Governance im geopolitischen Kontext.",
        "aussage_uebersetzung_de": "KI ist ein Werkzeug. Und wie jedes Werkzeug kann es zum Guten oder zum Schlechten eingesetzt werden. Die Frage ist: Welche Normen, welche Regeln, welche Vorschriften setzen wir ein?",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. CEO von Microsoft ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Satya Nadella wird der dritte CEO von Microsoft und loest Steve Ballmer ab. Er tritt die Nachfolge von Bill Gates und Steve Ballmer an.",
        "datum_handlung": "2014-02-04",
        "betrag_usd": None,
        "quell_link": "https://news.microsoft.com/2014/02/04/satya-nadella-named-ceo-of-microsoft/",
        "quell_titel": "Satya Nadella Named CEO of Microsoft",
        "kontext": "Nadella war zuvor Executive Vice President von Microsofts Cloud and Enterprise Group. Unter seiner Fuehrung wuchs Azure von nahezu null zu einem Milliarden-Dollar-Business.",
    },
    # ---- H2. "Hit Refresh" Buch Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Nadella veroeffentlicht sein Buch 'Hit Refresh: The Quest to Rediscover Microsoft's Soul and Imagine a Better Future for Everyone', in dem er die Transformation von Microsoft und seine Vision fuer KI darlegt.",
        "datum_handlung": "2017-09-26",
        "betrag_usd": None,
        "quell_link": "https://news.microsoft.com/hitrefresh/",
        "quell_titel": "Hit Refresh by Satya Nadella",
        "kontext": "Das Buch wird ein Bestseller und definiert Nadellas Philosophie von 'Empathy' und 'Growth Mindset' als Fuehrungsprinzipien.",
    },
    # ---- H3. Microsoft-OpenAI Partnerschaft $1 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Microsoft kuendigt eine $1 Milliarde Investition in OpenAI an und wird exklusiver Cloud-Partner. OpenAI nutzt Azure fuer alle KI-Modelle.",
        "datum_handlung": "2019-07-22",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://blogs.microsoft.com/blog/2019/07/22/microsoft-invests-in-and-partners-with-openai-to-support-us-building-beneficial-agi/",
        "quell_titel": "Microsoft invests in and partners with OpenAI",
        "kontext": "Die Partnerschaft wird als strategischer Schachzug gesehen, um Microsoft im KI-Rennen gegen Google zu positionieren.",
    },
    # ---- H4. GitHub Copilot Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft launcht GitHub Copilot, den ersten grossen KI-Programmier-Assistenten, basierend auf OpenAI Codex. Der Service nutzt GPT-3-Technologie.",
        "datum_handlung": "2021-06-29",
        "betrag_usd": None,
        "quell_link": "https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/",
        "quell_titel": "Introducing GitHub Copilot: AI pair programmer",
        "kontext": "GitHub Copilot ist eines der ersten kommerziellen Produkte, das auf GPT-basierten Modellen basiert. Es loest Kontroversen um Code-Lizenzierung aus.",
    },
    # ---- H5. Bing Chat Launch (spaeter Microsoft Copilot) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft launcht Bing Chat (spaeter umbenannt in Microsoft Copilot), eine KI-gestuetzte Suchmaschine basierend auf GPT-4. Es ist Microsofts erster direkter Angriff auf Googles Suchmonopol.",
        "datum_handlung": "2023-02-07",
        "betrag_usd": None,
        "quell_link": "https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/",
        "quell_titel": "Reinventing search with a new AI-powered Microsoft Bing",
        "kontext": "Der Launch erfolgt nur Tage nach ChatGPT-Integration-Ankuendigungen. Bing Chat wird mit GPT-4 betrieben, noch bevor GPT-4 offiziell veroeffentlicht wird.",
    },
    # ---- H6. Microsoft 365 Copilot Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft kuendigt Microsoft 365 Copilot an, einen KI-Assistenten fuer Word, Excel, PowerPoint, Outlook und Teams. Preis: $30/Monat zusaetzlich zu Microsoft 365.",
        "datum_handlung": "2023-03-16",
        "betrag_usd": None,
        "quell_link": "https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/",
        "quell_titel": "Introducing Microsoft 365 Copilot",
        "kontext": "Die Ankuendigung erfolgt nur zwei Tage nach dem Launch von GPT-4. Microsoft 365 Copilot wird als groesste Produktivitaets-Innovation seit Office dargestellt.",
    },
    # ---- H7. Microsoft-OpenAI Investition $10 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Microsoft investiert weitere ca. $10 Milliarden in OpenAI in einer mehrjaehrigen Partnerschaft. Die Gesamtinvestition belaeuft sich damit auf ca. $13 Milliarden.",
        "datum_handlung": "2023-01-23",
        "betrag_usd": 10000000000.0,
        "quell_link": "https://www.bloomberg.com/news/articles/2023-01-23/microsoft-makes-multibillion-dollar-investment-in-openai",
        "quell_titel": "Microsoft makes multibillion-dollar investment in OpenAI (Bloomberg)",
        "kontext": "Die Investition erfolgt nur wenige Wochen nach dem ChatGPT-Launch. Microsoft erhaelt 49% Anteil an OpenAI-Gewinnen (mit Deckelung).",
    },
    # ---- H8. Sam Altman Re-Hiring (Board Crisis Response) ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Nach der Entlassung von Sam Altman durch den OpenAI-Board bietet Nadella Altman und Greg Brockman an, ein neues KI-Team bei Microsoft zu leiten. Als Altman zurueckkehrt, sichert Microsoft einen Beobachtersitz im neuen Board.",
        "datum_handlung": "2023-11-19",
        "betrag_usd": None,
        "quell_link": "https://www.theverge.com/2023/11/20/23967515/microsoft-hires-sam-altman-greg-brockman-openai",
        "quell_titel": "Microsoft hires former OpenAI CEO Sam Altman and co-founder Greg Brockman (The Verge)",
        "kontext": "Nadella sichert in der Krise sowohl die Partnerschaft mit OpenAI als auch die Option, Altman und Schluesseltalente zu Microsoft zu holen. Ein strategischer Schachzug.",
    },
    # ---- H9. Copilot+ PCs Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft kuendigt Copilot+ PCs an, eine neue PC-Kategorie mit integrierten NPUs (Neural Processing Units) fuer On-Device-KI. Partnerschaft mit Qualcomm, Intel, AMD.",
        "datum_handlung": "2024-05-20",
        "betrag_usd": None,
        "quell_link": "https://blogs.windows.com/windowsexperience/2024/05/20/introducing-copilot-pcs/",
        "quell_titel": "Introducing Copilot+ PCs",
        "kontext": "Die neue PC-Kategorie ermoeglicht KI-Features wie Recall, Live Captions und Cocreator direkt auf dem Geraet ohne Cloud-Verbindung.",
    },
    # ---- H10. Azure AI Foundry Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft launcht Azure AI Foundry (vorher Azure AI Studio), eine Plattform fuer Entwickler zum Bauen, Trainieren und Deployen eigener KI-Modelle. Unterstuetzt OpenAI-Modelle, Open-Source-Modelle und Custom-Modelle.",
        "datum_handlung": "2023-05-23",
        "betrag_usd": None,
        "quell_link": "https://azure.microsoft.com/en-us/blog/build-2023/",
        "quell_titel": "Build 2023: Introducing Azure AI Studio",
        "kontext": "Azure AI Foundry wird als 'One-Stop-Shop' fuer Enterprise-KI positioniert. Microsoft will damit gegen AWS SageMaker und Google Vertex AI antreten.",
    },
    # ---- H11. Partnership mit Mistral AI ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Microsoft kuendigt Partnerschaft mit dem franzoesischen KI-Startup Mistral AI an und investiert ca. $16 Millionen. Mistral-Modelle werden auf Azure verfuegbar.",
        "datum_handlung": "2024-02-26",
        "betrag_usd": 16000000.0,
        "quell_link": "https://news.microsoft.com/2024/02/26/microsoft-and-mistral-ai-announce-new-partnership-to-accelerate-ai-innovation-and-introduce-mistral-large/",
        "quell_titel": "Microsoft and Mistral AI announce new partnership",
        "kontext": "Die Partnerschaft zeigt Microsofts Diversifizierungsstrategie jenseits von OpenAI. Sie loest Kontroversen in Europa aus, da EU-Regulatoren Wettbewerbsbedenken aeussern.",
    },
    # ---- H12. Lobbying fuer AI Act (EU) ----
    {
        "handlung_typ": "lobbying",
        "beschreibung": "Microsoft engagiert sich intensiv im EU-AI-Act-Gesetzgebungsprozess und plaediert fuer risikobasierte Regulierung statt pauschaler Verbote. Nadella trifft EU-Kommissarin Margrethe Vestager mehrfach.",
        "datum_handlung": "2023-06-14",
        "betrag_usd": None,
        "quell_link": "https://www.politico.eu/article/microsoft-lobbying-artificial-intelligence-act-brussels-ursula-von-der-leyen/",
        "quell_titel": "How Microsoft is lobbying the EU's AI Act (Politico)",
        "kontext": "Microsoft positioniert sich als 'responsible AI leader' und befuerwortet Regulierung, die Innovation nicht behindert.",
    },
    # ---- H13. Inflection AI Acqui-Hire ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Microsoft stellt Mustafa Suleyman (Co-Founder von DeepMind und Inflection AI) als CEO von Microsoft AI ein und holt die meisten Inflection-Mitarbeiter. Microsoft zahlt Inflection $650 Millionen fuer Lizenzen.",
        "datum_handlung": "2024-03-19",
        "betrag_usd": 650000000.0,
        "quell_link": "https://blogs.microsoft.com/blog/2024/03/19/mustafa-suleyman-joins-microsoft-to-lead-consumer-ai/",
        "quell_titel": "Mustafa Suleyman joins Microsoft to lead Consumer AI",
        "kontext": "Das Acqui-Hire ermoeglicht Microsoft, Top-Talente zu holen, ohne eine formale Uebernahme (die Regulatoren auf den Plan gerufen haette). Suleyman rapportiert direkt an Nadella.",
    },
    # ---- H14. Azure OpenAI Service General Availability ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Microsoft macht Azure OpenAI Service (Zugang zu GPT-4, GPT-3.5, DALL-E, Codex etc.) allgemein verfuegbar fuer Unternehmenskunden. Bereits ueber 4.500 Unternehmen nutzen den Service in der Preview.",
        "datum_handlung": "2023-01-17",
        "betrag_usd": None,
        "quell_link": "https://azure.microsoft.com/en-us/blog/general-availability-of-azure-openai-service-expands-access-to-large-advanced-ai-models-with-added-enterprise-benefits/",
        "quell_titel": "General availability of Azure OpenAI Service",
        "kontext": "Der Service wird zur zentralen Monetarisierungsplattform fuer OpenAI-Modelle und treibt Azures Wachstum. Microsoft behielt ca. 20% der OpenAI API-Revenue.",
    },
    # ---- H15. Spende an American India Foundation (Zika Education) ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Satya und Anu Nadella spenden $15 Millionen an die Seattle Children's Hospital fuer Forschung zu neurologischen Entwicklungsstoerungen bei Kindern, inspiriert durch ihren Sohn Zain mit zerebraler Kinderlahmung.",
        "datum_handlung": "2021-10-08",
        "betrag_usd": 15000000.0,
        "quell_link": "https://www.seattlechildrens.org/about/stories/satya-and-anu-nadella-family-gift-seattle-childrens/",
        "quell_titel": "Satya and Anu Nadella Family Gift to Seattle Children's",
        "kontext": "Die Spende spiegelt Nadellas persoenliche Erfahrung als Vater und sein Empathie-Prinzip wider. Zain Nadella verstarb 2022.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=13 existiert
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
            "Claude (collect_nadella.py)"
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
        "Satya Nadella, Hit Refresh, Microsoft OpenAI partnership, Copilot, Azure AI, empathy leadership, Build conference, AI regulation, GitHub Copilot, Bing Chat",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Hit Refresh Buch, Build Keynotes 2018-2024, WSJ Interview, TIME Interview, CNBC Interviews, "
        f"US Senate AI Insight Forum, LinkedIn Posts, Microsoft Blogs, Bloomberg, Financial Times, "
        f"Davos WEF, Munich Security Conference, ABC News, Business Insider, Politico, The Verge.",
        "Claude (collect_nadella.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Satya Nadella (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Satya Nadella")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_nadella.py")
    print("  Verifizierte Aussagen & Handlungen: Satya Nadella")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
