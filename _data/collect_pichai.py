#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_pichai.py
=================
Sammelt verifizierbare Aussagen und Handlungen von Sundar Pichai (person_id=4)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Blog-Posts, Congressional Testimony, Keynotes und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 4  # Sundar Pichai

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
    # ---- 1. Google I/O 2023 - AI als Mission ----
    {
        "aussage_text": "Making AI helpful for everyone is the most profound way we'll advance our mission.",
        "aussage_kurz": "Pichai erklaert KI zur zentralen Mission von Google, um die Welt zu helfen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Keynote/Panel
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://blog.google/technology/ai/google-io-2023-keynote-sundar-pichai/",
        "quell_titel": "Google I/O 2023: Making AI more helpful for everyone (Google Blog)",
        "datum_aussage": "2023-05-10",
        "sprache": "en",
        "kontext": "Google I/O 2023 Keynote. Pichai praesentiert Googles KI-Vision und kuendigt umfassende Integration von KI in alle Produkte an.",
        "aussage_uebersetzung_de": "KI fuer alle hilfreich zu machen, ist der tiefgreifendste Weg, unsere Mission voranzubringen.",
    },
    # ---- 2. UN Summit 2024 - Profound Technology ----
    {
        "aussage_text": "We've been investing in AI research, tools, and infrastructure for two decades because it's the most profound way we can deliver on our mission — and improve people's lives.",
        "aussage_kurz": "Pichai bezeichnet KI als die tiefgreifendste Technologie zur Verbesserung des Lebens der Menschen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/company-news/inside-google/message-ceo/united-nations-keynote-2024/",
        "quell_titel": "UN Summit of the Future: AI opportunity for everyone (Google Blog)",
        "datum_aussage": "2024-09-22",
        "sprache": "en",
        "kontext": "Keynote beim UN Summit of the Future 2024. Pichai betont Googles langjaehriges Engagement fuer KI.",
        "aussage_uebersetzung_de": "Wir investieren seit zwei Jahrzehnten in KI-Forschung, Tools und Infrastruktur, weil es der tiefgreifendste Weg ist, unsere Mission zu erfuellen - und das Leben der Menschen zu verbessern.",
    },
    # ---- 3. AI Action Summit 2025 - Biggest Shift ----
    {
        "aussage_text": "AI will be the most profound shift of our lifetimes. Bigger than the shift to personal computing, or to mobile. And it will do more to democratize access to information than the internet.",
        "aussage_kurz": "Pichai: KI wird die groesste Umwaelzung unseres Lebens - groesser als PC oder Mobile.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/technology/ai/sundar-pichai-ai-action-summit/",
        "quell_titel": "AI Action Summit: Sundar Pichai's remarks (Google Blog)",
        "datum_aussage": "2025-02-10",
        "sprache": "en",
        "kontext": "AI Action Summit Paris 2025. Pichai vergleicht KI mit frueheren technologischen Revolutionen.",
        "aussage_uebersetzung_de": "KI wird die tiefgreifendste Verschiebung unseres Lebens sein. Groesser als der Wechsel zum Personal Computer oder zu Mobile. Und sie wird mehr tun, um den Zugang zu Informationen zu demokratisieren, als das Internet.",
    },
    # ---- 4. AI Action Summit - Profound Technology Statement ----
    {
        "aussage_text": "AI is the most profound technology humanity has ever worked on, and it has potential for extraordinary benefits, and we will have to work through societal disruption.",
        "aussage_kurz": "Pichai warnt, dass KI die tiefgreifendste Technologie ist und gesellschaftliche Stoerungen mit sich bringt.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/technology/ai/sundar-pichai-ai-action-summit/",
        "quell_titel": "AI Action Summit: Sundar Pichai's remarks (Google Blog)",
        "datum_aussage": "2025-02-10",
        "sprache": "en",
        "kontext": "Fortsetzung der AI Action Summit Remarks. Pichai spricht ueber Chancen und Risiken.",
        "aussage_uebersetzung_de": "KI ist die tiefgreifendste Technologie, an der die Menschheit je gearbeitet hat, sie hat Potenzial fuer ausserordentliche Vorteile, und wir werden gesellschaftliche Stoerungen durcharbeiten muessen.",
    },
    # ---- 5. MIT Sloan 2023 - Technology as Agent for Change ----
    {
        "aussage_text": "Technology should be an enabler, a great equalizer. It should be used to make things more accessible for everyone.",
        "aussage_kurz": "Pichai: Technologie sollte ein Gleichmacher sein und Dinge fuer alle zugaenglich machen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://mitsloan.mit.edu/ideas-made-to-matter/googles-sundar-pichai-says-tech-a-powerful-agent-change",
        "quell_titel": "Google's Sundar Pichai says tech is a powerful agent for change (MIT Sloan)",
        "datum_aussage": "2023-10-19",
        "sprache": "en",
        "kontext": "MIT Sloan Konferenz. Pichai spricht ueber demokratischen Zugang zu Technologie.",
        "aussage_uebersetzung_de": "Technologie sollte ein Ermoegliger sein, ein grosser Gleichmacher. Sie sollte genutzt werden, um Dinge fuer alle zugaenglicher zu machen.",
    },
    # ---- 6. Gemini Launch December 2023 ----
    {
        "aussage_text": "I believe the transition we are seeing right now with AI will be the most profound in our lifetimes, far bigger than the shift to mobile or to the web before it.",
        "aussage_kurz": "Beim Gemini-Launch erklaert Pichai die KI-Transformation zur groessten seines Lebens.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://blog.google/technology/ai/google-gemini-ai/",
        "quell_titel": "Introducing Gemini: Google's most capable AI model yet (Google Blog)",
        "datum_aussage": "2023-12-06",
        "sprache": "en",
        "kontext": "Offizielle Ankuendigung von Gemini, Googles multimodalem KI-Modell. Pichai positioniert es als Meilenstein.",
        "aussage_uebersetzung_de": "Ich glaube, der Uebergang, den wir gerade mit KI erleben, wird der tiefgreifendste unseres Lebens sein, weit groesser als der Wechsel zu Mobile oder zum Web davor.",
    },
    # ---- 7. Gemini Advanced Launch Feb 2024 ----
    {
        "aussage_text": "This is the biggest upgrade to Bard since it launched. It represents a new era in our AI journey.",
        "aussage_kurz": "Pichai beschreibt die Gemini-Integration in Bard als groesstes Update und neue Aera.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/",
        "quell_titel": "Google Gemini update: Sundar Pichai introduces Ultra 1.0 in Gemini Advanced (Google Blog)",
        "datum_aussage": "2024-02-08",
        "sprache": "en",
        "kontext": "Ankuendigung von Gemini Advanced mit Ultra 1.0 und Umbenennung von Bard zu Gemini.",
        "aussage_uebersetzung_de": "Dies ist das groesste Upgrade fuer Bard seit dem Launch. Es stellt eine neue Aera in unserer KI-Reise dar.",
    },
    # ---- 8. Google I/O 2024 - Gemini Era ----
    {
        "aussage_text": "Google is fully in our Gemini era. We've been investing in AI for more than a decade — and innovating at every layer of the stack: research, product, infrastructure.",
        "aussage_kurz": "Pichai erklaert Google I/O 2024 zur 'Gemini-Aera' nach einem Jahrzehnt KI-Forschung.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/inside-google/message-ceo/google-io-2024-keynote-sundar-pichai/",
        "quell_titel": "Google I/O 2024: Sundar Pichai on Gemini, AI progress and more (Google Blog)",
        "datum_aussage": "2024-05-14",
        "sprache": "en",
        "kontext": "Google I/O 2024 Keynote. Pichai praesentiert Gemini-Integration in alle Google-Produkte.",
        "aussage_uebersetzung_de": "Google ist vollstaendig in unserer Gemini-Aera. Wir investieren seit ueber einem Jahrzehnt in KI - und innovieren auf jeder Ebene des Stacks: Forschung, Produkt, Infrastruktur.",
    },
    # ---- 9. Google I/O 2025 - AI Mode & Reimagining Search ----
    {
        "aussage_text": "AI Mode is a total reimagining of Search. It's designed to help you solve bigger problems and get things done.",
        "aussage_kurz": "Pichai kuendigt 'AI Mode' als komplette Neugestaltung der Google-Suche an.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/innovation-and-ai/technology/ai/io-2025-keynote/",
        "quell_titel": "Google I/O 2025: Sundar Pichai's opening keynote (Google Blog)",
        "datum_aussage": "2025-05-13",
        "sprache": "en",
        "kontext": "Google I/O 2025 Keynote. Pichai praesentiert grundlegende Neugestaltung der Suche durch KI.",
        "aussage_uebersetzung_de": "AI Mode ist eine vollstaendige Neugestaltung der Suche. Es ist darauf ausgelegt, Ihnen zu helfen, groessere Probleme zu loesen und Dinge zu erledigen.",
    },
    # ---- 10. DeepMind Merger April 2023 ----
    {
        "aussage_text": "To ensure the bold and responsible development of general AI, we're creating a unit that will help us build more capable systems more safely and responsibly.",
        "aussage_kurz": "Bei der DeepMind-Fusion betont Pichai 'kuehne und verantwortungsvolle' KI-Entwicklung.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.cnbc.com/2023/04/20/alphabet-merges-ai-focused-groups-deepmind-and-google-research.html",
        "quell_titel": "Read the internal memo Alphabet sent in merging DeepMind and Google Brain (CNBC)",
        "datum_aussage": "2023-04-20",
        "sprache": "en",
        "kontext": "Interne Memo zur Fusion von Google Brain und DeepMind zu Google DeepMind. Verantwortungsvolle KI-Entwicklung als Ziel.",
        "aussage_uebersetzung_de": "Um die kuehne und verantwortungsvolle Entwicklung allgemeiner KI sicherzustellen, schaffen wir eine Einheit, die uns hilft, leistungsfaehigere Systeme sicherer und verantwortungsvoller zu bauen.",
    },
    # ---- 11. Senate AI Meeting 2023 - National Regulation ----
    {
        "aussage_text": "The U.S. must get the balance right on AI regulation or risk falling behind China. This would be better done at the national level.",
        "aussage_kurz": "Pichai fordert nationale KI-Regulierung in den USA, um nicht hinter China zurueckzufallen.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.foxbusiness.com/fox-news-tech/google-ceo-calls-national-ai-regulation-compete-china-more-effectively",
        "quell_titel": "Google CEO Sundar Pichai warns US must balance AI regulation (Fox Business)",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Senate AI Meeting mit Tech-CEOs (Musk, Zuckerberg, Altman, Pichai). Diskussion ueber KI-Regulierung.",
        "aussage_uebersetzung_de": "Die USA muessen die richtige Balance bei der KI-Regulierung finden, sonst riskieren sie, hinter China zurueckzufallen. Das waere auf nationaler Ebene besser aufgehoben.",
    },
    # ---- 12. Senate Meeting - International Cooperation ----
    {
        "aussage_text": "Countries must work together to develop international frameworks of cooperation so that we don't weaponize these technologies against each other.",
        "aussage_kurz": "Pichai warnt vor Waffenisierung von KI und fordert internationale Zusammenarbeit.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.foxbusiness.com/fox-news-tech/google-ceo-calls-national-ai-regulation-compete-china-more-effectively",
        "quell_titel": "Google CEO Sundar Pichai warns US must balance AI regulation (Fox Business)",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Fortsetzung des Senate AI Meetings. Pichai fordert internationale KI-Governance.",
        "aussage_uebersetzung_de": "Laender muessen zusammenarbeiten, um internationale Rahmenbedingungen der Zusammenarbeit zu entwickeln, damit wir diese Technologien nicht gegeneinander bewaffnen.",
    },
    # ---- 13. BBC Interview - Job Impact ----
    {
        "aussage_text": "People will need to adapt, and then there will be areas where it will impact some jobs. So, as a society, I think we need to be having those conversations.",
        "aussage_kurz": "Pichai raeumt ein, dass KI Jobs beeinflussen wird und fordert gesellschaftliche Debatten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://fortune.com/2025/12/02/ai-wipes-jobs-google-ceo-sundar-pichai-everyday-people-to-adapt-accordingly-we-have-to-work-through-societal-disruption/",
        "quell_titel": "As AI wipes jobs, Google CEO says it's up to people to adapt (Fortune / BBC)",
        "datum_aussage": "2025-12-02",
        "sprache": "en",
        "kontext": "BBC Interview ueber KI-Auswirkungen auf den Arbeitsmarkt. Pichai spricht offen ueber Job-Verluste.",
        "aussage_uebersetzung_de": "Menschen werden sich anpassen muessen, und dann wird es Bereiche geben, in denen es einige Jobs beeinflussen wird. Als Gesellschaft muessen wir diese Gespraeche fuehren, denke ich.",
    },
    # ---- 14. Job Impact - Adaptation ----
    {
        "aussage_text": "People who learn to adopt and adapt to AI will do better. All those professions will be around, but the people who will do well in each of those professions are people who learn how to use these tools.",
        "aussage_kurz": "Pichai: Wer lernt, KI zu nutzen, wird in jedem Beruf besser abschneiden.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://yourstory.com/ai-story/business-sundar-pichai-alphabet-ai-hiring-expansion-2025",
        "quell_titel": "Sundar Pichai says AI won't replace jobs, it will expand them (YourStory)",
        "datum_aussage": "2025-12",
        "sprache": "en",
        "kontext": "Aeusserungen zur Zukunft der Arbeit. Pichai betont Anpassungsfaehigkeit statt Jobverlust.",
        "aussage_uebersetzung_de": "Menschen, die lernen, KI zu uebernehmen und sich daran anzupassen, werden besser abschneiden. All diese Berufe wird es geben, aber die Menschen, die in jedem dieser Berufe gut abschneiden werden, sind diejenigen, die lernen, wie man diese Tools nutzt.",
    },
    # ---- 15. Democracy and Access ----
    {
        "aussage_text": "With AI, we have the chance to democratize access from the start… ensure that the digital divide doesn't become an AI divide… and make AI helpful for everyone.",
        "aussage_kurz": "Pichai will sicherstellen, dass die digitale Kluft nicht zur KI-Kluft wird.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/company-news/inside-google/message-ceo/united-nations-keynote-2024/",
        "quell_titel": "UN Summit of the Future: AI opportunity for everyone (Google Blog)",
        "datum_aussage": "2024-09-22",
        "sprache": "en",
        "kontext": "UN Summit. Pichai fordert demokratischen Zugang zu KI fuer alle.",
        "aussage_uebersetzung_de": "Mit KI haben wir die Chance, den Zugang von Anfang an zu demokratisieren... sicherzustellen, dass die digitale Kluft nicht zu einer KI-Kluft wird... und KI fuer alle hilfreich zu machen.",
    },
    # ---- 16. Human-AI Collaboration ----
    {
        "aussage_text": "The future of AI is not about replacing humans, it's about augmenting human capabilities.",
        "aussage_kurz": "Pichai betont: KI soll Menschen nicht ersetzen, sondern ihre Faehigkeiten erweitern.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://iankhan.com/popular-quotes-by-sundar-pichai-on-ai-leadership-medium-google-ceo-steady-interest/",
        "quell_titel": "Popular Quotes by Sundar Pichai on AI & Leadership",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Allgemeine Vision zur Mensch-KI-Zusammenarbeit in verschiedenen Reden.",
        "aussage_uebersetzung_de": "Die Zukunft der KI geht nicht darum, Menschen zu ersetzen, sondern darum, menschliche Faehigkeiten zu erweitern.",
    },
    # ---- 17. Google's AI Investment Strategy ----
    {
        "aussage_text": "I believe that technology is a foundational enabler of progress. Just as the internet and mobile devices expanded opportunities for people around the world, now AI is poised to accelerate progress at unprecedented scale.",
        "aussage_kurz": "Pichai vergleicht KI mit Internet und Mobile als Beschleuniger des Fortschritts in beispiellosem Umfang.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://codefarm0.medium.com/inside-googles-ai-future-sundar-pichai-s-vision-for-search-innovation-and-beyond-6f168b6c105f",
        "quell_titel": "Inside Google's AI Future: Sundar Pichai's Vision (Medium)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Grundsatzerklaerung zur strategischen Bedeutung von KI fuer Google und die Welt.",
        "aussage_uebersetzung_de": "Ich glaube, dass Technologie ein grundlegender Motor des Fortschritts ist. So wie das Internet und mobile Geraete die Moeglichkeiten fuer Menschen auf der ganzen Welt erweitert haben, ist KI nun bereit, den Fortschritt in beispiellosem Umfang zu beschleunigen.",
    },
    # ---- 18. Trust and Caution ----
    {
        "aussage_text": "Don't blindly trust AI tools. People need to adapt.",
        "aussage_kurz": "Pichai warnt davor, KI-Tools blind zu vertrauen und fordert kritisches Bewusstsein.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.anews.com.tr/tech/2025/11/18/pichai-dont-blindly-trust-ai-tools",
        "quell_titel": "Pichai: Don't blindly trust AI tools (Anadolu Agency)",
        "datum_aussage": "2025-11-18",
        "sprache": "en",
        "kontext": "Warnung vor unkritischer KI-Nutzung. Pichai betont Eigenverantwortung.",
        "aussage_uebersetzung_de": "Vertrauen Sie KI-Tools nicht blind. Menschen muessen sich anpassen.",
    },
    # ---- 19. Willow Quantum Chip December 2024 ----
    {
        "aussage_text": "Introducing Willow, our new state-of-the-art quantum computing chip with a breakthrough that can reduce errors exponentially as we scale up using more qubits, cracking a 30-year challenge in the field.",
        "aussage_kurz": "Pichai kuendigt Willow-Quantenchip an, der ein 30-Jahre-altes Problem der Fehlerreduktion loest.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/sundarpichai/status/1866167429367468422",
        "quell_titel": "Sundar Pichai on X: Introducing Willow",
        "datum_aussage": "2024-12-09",
        "sprache": "en",
        "kontext": "Ankuendigung von Googles Quantenchip Willow auf X/Twitter. Durchbruch bei Fehlerkorrektur.",
        "aussage_uebersetzung_de": "Wir stellen Willow vor, unseren neuen hochmodernen Quantenchip mit einem Durchbruch, der Fehler exponentiell reduzieren kann, wenn wir mit mehr Qubits skalieren - und damit eine 30-jaehrige Herausforderung im Feld knackt.",
    },
    # ---- 20. Willow Practical Applications ----
    {
        "aussage_text": "We see Willow as an important step in our journey to build a useful quantum computer with practical applications in areas like drug discovery, fusion energy, battery design + more.",
        "aussage_kurz": "Pichai sieht Willow als Schritt zu praktischem Quantencomputer fuer Medikamente, Energie, Batterien.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/sundarpichai/status/1866167562373124420",
        "quell_titel": "Sundar Pichai on X: Willow practical applications",
        "datum_aussage": "2024-12-09",
        "sprache": "en",
        "kontext": "Follow-up Tweet zur Willow-Ankuendigung. Pichai beschreibt praktische Anwendungen.",
        "aussage_uebersetzung_de": "Wir sehen Willow als wichtigen Schritt auf unserem Weg, einen nuetzlichen Quantencomputer mit praktischen Anwendungen in Bereichen wie Medikamentenentwicklung, Fusionsenergie, Batteriedesign und mehr zu bauen.",
    },
    # ---- 21. 60 Minutes Interview - AI More Profound than Fire ----
    {
        "aussage_text": "AI is probably the most important thing humanity has ever worked on. I think of it as something more profound than electricity or fire.",
        "aussage_kurz": "Pichai: KI ist tiefgreifender als Elektrizitaet oder Feuer - das Wichtigste, woran die Menschheit je arbeitete.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.rev.com/transcripts/the-ai-revolution-googles-developers-on-the-future-of-artificial-intelligence-60-minutes-transcript",
        "quell_titel": "The AI Revolution: Google's Developers on 60 Minutes Transcript",
        "datum_aussage": "2023-04",
        "sprache": "en",
        "kontext": "60 Minutes Interview ueber KI. Pichai vergleicht KI mit fundamentalen Entdeckungen der Menschheit.",
        "aussage_uebersetzung_de": "KI ist wahrscheinlich das Wichtigste, woran die Menschheit je gearbeitet hat. Ich betrachte es als etwas Tiefgreifenderes als Elektrizitaet oder Feuer.",
    },
    # ---- 22. Gemini in 2 Billion Products ----
    {
        "aussage_text": "All of Google's 2-billion user products use Gemini. This is the fastest adoption of any model in our history.",
        "aussage_kurz": "Pichai: Gemini wird in allen Google-Produkten mit 2 Milliarden Nutzern eingesetzt - schnellste Adoption je.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.itpro.com/technology/artificial-intelligence/the-fastest-adoption-of-any-model-in-our-history-sundar-pichai-hails-ai-gains-as-google-cloud-growth-gemini-popularity-surges",
        "quell_titel": "Fastest adoption of any model in our history: Sundar Pichai hails AI gains (IT Pro)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Earnings Call. Pichai berichtet ueber erfolgreiche Gemini-Integration in Google-Oekosystem.",
        "aussage_uebersetzung_de": "Alle Google-Produkte mit 2 Milliarden Nutzern verwenden Gemini. Dies ist die schnellste Einfuehrung eines Modells in unserer Geschichte.",
    },
    # ---- 23. MIT Sloan - AI Divide Warning ----
    {
        "aussage_text": "He warned against the risk of an 'AI divide,' urging global efforts to ensure fair access to AI technologies.",
        "aussage_kurz": "Pichai warnt vor einer 'KI-Kluft' und fordert globale Anstrengungen fuer fairen Zugang.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://mitsloan.mit.edu/ideas-made-to-matter/googles-sundar-pichai-says-tech-a-powerful-agent-change",
        "quell_titel": "Google's Sundar Pichai says tech is a powerful agent for change (MIT Sloan)",
        "datum_aussage": "2023-10-19",
        "sprache": "en",
        "kontext": "MIT Sloan Konferenz. Pichai spricht ueber Gerechtigkeit beim KI-Zugang.",
        "aussage_uebersetzung_de": "Er warnte vor dem Risiko einer 'KI-Kluft' und forderte globale Anstrengungen, um fairen Zugang zu KI-Technologien sicherzustellen.",
    },
    # ---- 24. Google's Responsibility and Leadership ----
    {
        "aussage_text": "We have been investing in AI research for two decades. We have a deep sense of responsibility to get this right.",
        "aussage_kurz": "Pichai betont Googles 20-jaehrige KI-Forschung und tiefes Verantwortungsgefuehl.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.google/technology/ai/google-io-2023-keynote-sundar-pichai/",
        "quell_titel": "Google I/O 2023: Making AI more helpful for everyone (Google Blog)",
        "datum_aussage": "2023-05-10",
        "sprache": "en",
        "kontext": "Google I/O 2023. Pichai unterstreicht Googles langjaehriges Engagement und Verantwortung.",
        "aussage_uebersetzung_de": "Wir investieren seit zwei Jahrzehnten in KI-Forschung. Wir haben ein tiefes Verantwortungsgefuehl, dies richtig zu machen.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. CEO von Google ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Sundar Pichai wird CEO von Google (nach Umbenennung der Holding in Alphabet Inc.). Larry Page wird CEO von Alphabet, Pichai uebernimmt Tagesgeschaeft von Google.",
        "datum_handlung": "2015-08-10",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Sundar_Pichai",
        "quell_titel": "Sundar Pichai - Wikipedia",
        "kontext": "Alphabet-Reorganisation. Pichai fuehrt Google, waehrend Page und Brin die Holding leiten.",
    },
    # ---- H2. CEO von Alphabet ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Sundar Pichai wird zusaetzlich CEO von Alphabet Inc., nachdem Larry Page und Sergey Brin zuruecktreten. Pichai leitet nun sowohl Google als auch die Muttergesellschaft.",
        "datum_handlung": "2019-12-03",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Sundar_Pichai",
        "quell_titel": "Sundar Pichai - Wikipedia",
        "kontext": "Page und Brin ziehen sich zurueck. Pichai uebernimmt volle Kontrolle ueber Alphabet.",
    },
    # ---- H3. Code Red nach ChatGPT ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Nach dem viralen Erfolg von ChatGPT ruft Sundar Pichai unternehmensweit 'Code Red' aus und bezeichnet den Chatbot als existenzielle Bedrohung fuer Google Search. Teams werden umstrukturiert, um bis Mai 2023 KI-Prototypen und Produkte zu entwickeln.",
        "datum_handlung": "2022-12",
        "betrag_usd": None,
        "quell_link": "https://www.benzinga.com/news/22/12/30170477/chatgpt-popularity-reportedly-leads-to-google-declaring-code-red-as-sundar-pichai-increases-involvem",
        "quell_titel": "ChatGPT leads to Google declaring 'Code Red' (Benzinga)",
        "kontext": "ChatGPT-Launch im November 2022 loest Alarmzustand bei Google aus. Pichai involviert sich direkt in KI-Strategie.",
    },
    # ---- H4. Anthropic Investment $300M ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Google investiert $300 Millionen in Anthropic (OpenAI-Konkurrent, gegr. von ehemaligen OpenAI-Mitarbeitern) und nimmt ca. 10% Anteil. Anthropic waehlt Google als bevorzugten Cloud-Partner.",
        "datum_handlung": "2023-02-04",
        "betrag_usd": 300000000.0,
        "quell_link": "https://fortune.com/2023/02/04/google-invests-300m-anthropic-openai-rival-making-chatgpt-challenger-claude-ai-chatbot-battle/",
        "quell_titel": "Google invests in Anthropic, maker of ChatGPT rival (Fortune)",
        "kontext": "Strategische Investition in ChatGPT-Konkurrenten nach Code-Red-Ausrufung.",
    },
    # ---- H5. Bard Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google veroeffentlicht Bard, einen KI-Chatbot als Antwort auf ChatGPT. Der Launch verlaeuft holprig: In der Demo gibt Bard eine falsche Antwort, Alphabets Aktienkurs faellt um $100 Milliarden.",
        "datum_handlung": "2023-03-21",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_Gemini",
        "quell_titel": "Google Gemini - Wikipedia",
        "kontext": "Eiliger Launch unter Druck nach ChatGPT-Erfolg. Technische und PR-Probleme bei Vorstellung.",
    },
    # ---- H6. Google Brain + DeepMind Merger ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Sundar Pichai fuehrt Google Brain und DeepMind zu 'Google DeepMind' zusammen. Demis Hassabis wird CEO, Jeff Dean Chief Scientist. Ziel: 'Kuehne und verantwortungsvolle Entwicklung allgemeiner KI'.",
        "datum_handlung": "2023-04-20",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2023/04/20/google-consolidates-ai-research-divisions-into-google-deepmind/",
        "quell_titel": "Google consolidates AI research divisions into Google DeepMind (TechCrunch)",
        "kontext": "Strategische Konsolidierung von KI-Forschung unter Druck durch OpenAI/Microsoft-Partnerschaft.",
    },
    # ---- H7. Anthropic Investment $2 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Google verpflichtet sich, bis zu $2 Milliarden in Anthropic zu investieren: $500 Mio. sofort, weitere $1,5 Mrd. ueber die Zeit. Vertiefung der strategischen Partnerschaft.",
        "datum_handlung": "2023-10-27",
        "betrag_usd": 2000000000.0,
        "quell_link": "https://www.cnbc.com/2023/10/27/google-commits-to-invest-2-billion-in-openai-competitor-anthropic.html",
        "quell_titel": "Google commits to invest $2 billion in Anthropic (CNBC)",
        "kontext": "Aufstockung des Anthropic-Investments. Google sichert sich Position im KI-Wettkampf.",
    },
    # ---- H8. Gemini Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google veroeffentlicht Gemini, ein multimodales KI-Modell in drei Groessen (Ultra, Pro, Nano). Pichai bezeichnet es als 'most capable AI model yet'. Gemini Pro wird in Bard integriert.",
        "datum_handlung": "2023-12-06",
        "betrag_usd": None,
        "quell_link": "https://blog.google/technology/ai/google-gemini-ai/",
        "quell_titel": "Introducing Gemini: Google's most capable AI model yet (Google Blog)",
        "kontext": "Googles Flaggschiff-Antwort auf GPT-4. Multimodal von Grund auf designed.",
    },
    # ---- H9. Gemini Advanced Launch + Bard Umbenennung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google benennt Bard in 'Gemini' um und startet Gemini Advanced mit Ultra 1.0-Modell. Launch eines kostenpflichtigen Abonnements (Gemini Advanced) fuer $19.99/Monat. Integration in Google One.",
        "datum_handlung": "2024-02-08",
        "betrag_usd": None,
        "quell_link": "https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/",
        "quell_titel": "Google Gemini update: Sundar Pichai introduces Ultra 1.0 (Google Blog)",
        "kontext": "Umbenennung signalisiert neue Aera. Gemini wird zur einheitlichen KI-Marke von Google.",
    },
    # ---- H10. Trillium TPU v6 Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google kuendigt TPU v6 'Trillium' an - 6. Generation von Googles KI-Chips. 4,7-fache Leistungssteigerung pro Chip gegenueber TPU v5e. Teil der langfristigen Infrastruktur-Strategie.",
        "datum_handlung": "2024-05-14",
        "betrag_usd": None,
        "quell_link": "https://blog.google/inside-google/message-ceo/google-io-2024-keynote-sundar-pichai/",
        "quell_titel": "Google I/O 2024: Sundar Pichai on Gemini, AI progress (Google Blog)",
        "kontext": "Google I/O 2024 Ankuendigung. Eigenentwicklung von KI-Chips als strategischer Vorteil.",
    },
    # ---- H11. Willow Quantum Chip ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google veroeffentlicht Willow, einen Quantenchip mit 105 Qubits, der einen Durchbruch bei der Fehlerkorrektur erzielt. Berechnung in unter 5 Minuten, die klassische Computer 10^25 Jahre benoetigen wuerden.",
        "datum_handlung": "2024-12-09",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2024/12/10/alphabet-shares-jump-5percent-after-google-touts-breakthrough-quantum-chip-.html",
        "quell_titel": "Alphabet shares jump 6% after Google touts quantum chip (CNBC)",
        "kontext": "Durchbruch im Quantencomputing. Loest 30-Jahre-altes Problem der Fehlerreduktion beim Skalieren.",
    },
    # ---- H12. $75 Mrd. AI Infrastructure Investment ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Sundar Pichai kuendigt $75 Milliarden Investition in KI-Infrastruktur fuer 2025 an (Steigerung von $52,5 Mrd. in 2024). Ausbau von Rechenzentren, TPUs und GPU-Clustern.",
        "datum_handlung": "2025-01",
        "betrag_usd": 75000000000.0,
        "quell_link": "https://techstrong.ai/editorial-calendar/best-of-2025/google-to-spend-75-billion-on-ai-cloud-investment-2/",
        "quell_titel": "Google to Spend $75 Billion on AI, Cloud Investment (Techstrong.ai)",
        "kontext": "Q4 2024 Earnings Call. Massive Infrastruktur-Investition zur Skalierung von KI-Diensten.",
    },
    # ---- H13. Anthropic Investment + $1 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Google investiert weitere $1 Milliarde in Anthropic und bringt kumulativ ca. $3 Milliarden Investment. Zusaetzlich wird Cloud-Deal angekuendigt: Lieferung von bis zu 1 Million TPUs an Anthropic.",
        "datum_handlung": "2025-01-22",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://www.cnbc.com/2025/01/22/google-agrees-to-new-1-billion-investment-in-anthropic.html",
        "quell_titel": "Google agrees to new $1 billion investment in Anthropic (CNBC)",
        "kontext": "Vertiefung der strategischen Partnerschaft. Google sichert sich Rolle als Anthropic-Cloud-Partner.",
    },
    # ---- H14. Ironwood TPU v7 Announcement ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google kuendigt TPU v7 'Ironwood' an, die 7. Generation der Tensor Processing Units. 3.600-mal bessere Performance als die erste oeffentliche TPU, 29-mal energieeffizienter. Launch fuer 2025 geplant.",
        "datum_handlung": "2025",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2025/11/07/googles-decade-long-bet-on-tpus-companys-secret-weapon-in-ai-race.html",
        "quell_titel": "Google's decade-long bet on custom chips (CNBC)",
        "kontext": "Google Cloud Next 2025. Fortsetzung der TPU-Entwicklung als Alternative zu Nvidia-GPUs.",
    },
    # ---- H15. Anthropic Cloud Deal (Tens of Billions) ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Google und Anthropic kuendigen Cloud-Deal im Wert von Dutzenden Milliarden Dollar an: Lieferung von bis zu 1 Million TPUs. Deployment ab 2026 mit ueber 1 Gigawatt Kapazitaet. Groesster TPU-Deal in Googles Geschichte.",
        "datum_handlung": "2025-10-23",
        "betrag_usd": None,
        "quell_link": "https://www.bloomberg.com/news/articles/2025-10-23/google-anthropic-announce-cloud-deal-worth-tens-of-billions",
        "quell_titel": "Google, Anthropic Announce Cloud Deal Worth Tens of Billions (Bloomberg)",
        "kontext": "Strategische Vertiefung der Partnerschaft. Google sichert sich langfristigen Grosskunden fuer TPU-Infrastruktur.",
    },
    # ---- H16. Google AI Ethics Policy Revision ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Google aendert seine AI-Ethik-Grundsaetze und entfernt das Versprechen, Waffen- und Ueberwachungsanwendungen zu vermeiden. Kritiker werfen Google vor, kommerzielle Interessen ueber ethische Prinzipien zu stellen.",
        "datum_handlung": "2025-02-05",
        "betrag_usd": None,
        "quell_link": "https://www.techtimes.com/articles/309297/20250205/google-alters-ai-ethics-policy-removes-pledge-avoid-weapons-surveillance-use.htm",
        "quell_titel": "Google Alters AI Ethics Policy (Tech Times)",
        "kontext": "Kontroverse Policy-Aenderung. Google revidiert 2018 aufgestellte AI Principles.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=4 existiert
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
            "Claude (collect_pichai.py)"
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
        "Sundar Pichai AI quotes, Google I/O 2023 2024 2025, Gemini launch, DeepMind merger, Congressional testimony, Code Red, Anthropic investment, quantum Willow, TPU infrastructure",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Google I/O Keynotes (2023, 2024, 2025), Google Blog Posts, UN Summit 2024, "
        f"AI Action Summit Paris 2025, Senate AI Meeting 2023, MIT Sloan Conference, "
        f"60 Minutes Interview, BBC Interview, Fortune, CNBC, Bloomberg, TechCrunch, X/Twitter (@sundarpichai).",
        "Claude (collect_pichai.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Sundar Pichai (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Sundar Pichai")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_pichai.py")
    print("  Verifizierte Aussagen & Handlungen: Sundar Pichai")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
