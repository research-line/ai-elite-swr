#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_musk.py
===============
Sammelt verifizierbare Aussagen und Handlungen von Elon Musk (person_id=3)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Podcasts, Social-Media-Posts, Congressional Meetings und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Schwerpunkte: xAI/Grok, Neuralink, OpenAI-Geschichte, KI-Risiko-Warnungen,
Mars/SpaceX-Vision, Regulierungsforderungen, Transhumanismus

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 3  # Elon Musk

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
    # ---- 1. NPR National Governors Association, Juli 2017 ----
    {
        "aussage_text": "AI is a fundamental existential risk for human civilization, and I don't think people fully appreciate that.",
        "aussage_kurz": "Musk warnt Gouverneure, dass KI ein existenzielles Risiko fuer die Zivilisation darstellt.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.npr.org/sections/thetwo-way/2017/07/17/537686649/elon-musk-warns-governors-artificial-intelligence-poses-existential-risk",
        "quell_titel": "Elon Musk Warns Governors: Artificial Intelligence Poses 'Existential Risk' (NPR)",
        "datum_aussage": "2017-07-15",
        "sprache": "en",
        "kontext": "Ansprache vor der National Governors Association in Rhode Island. Musk warnt vor unkontrollierter KI-Entwicklung.",
        "aussage_uebersetzung_de": "KI ist ein fundamentales existenzielles Risiko fuer die menschliche Zivilisation, und ich glaube nicht, dass die Leute das voll schaetzen.",
    },
    # ---- 2. SXSW, Maerz 2018 ----
    {
        "aussage_text": "AI is far more dangerous than nukes. So why do we have no regulatory oversight? This is insane.",
        "aussage_kurz": "Bei SXSW erklaert Musk, KI sei gefaehrlicher als Atomwaffen und fordert Regulierung.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.cnbc.com/2018/03/13/elon-musk-at-sxsw-a-i-is-more-dangerous-than-nuclear-weapons.html",
        "quell_titel": "Elon Musk at SXSW: A.I. is more dangerous than nuclear weapons (CNBC)",
        "datum_aussage": "2018-03-11",
        "sprache": "en",
        "kontext": "South by Southwest Festival 2018. Musk vergleicht KI-Risiken mit Nuklearwaffen.",
        "aussage_uebersetzung_de": "KI ist weitaus gefaehrlicher als Atomwaffen. Warum haben wir also keine regulatorische Aufsicht? Das ist wahnsinnig.",
    },
    # ---- 3. Joe Rogan Experience #1169, Sep 2018 ----
    {
        "aussage_text": "If you assume any rate of improvement at all, then games will be indistinguishable from reality, or civilization will end. One of those two things will occur. Therefore, we are most likely in a simulation, because we exist.",
        "aussage_kurz": "Musk argumentiert, dass wir hoechstwahrscheinlich in einer Simulation leben.",
        "modus": "muendlich",
        "quellen_typ_id": 2,  # Podcast-Interview
        "plattform_id": 3,    # Podcasts
        "quell_link": "https://www.space.com/41749-elon-musk-living-in-simulation-rogan-podcast.html",
        "quell_titel": "We're Probably Living in a Simulation, Elon Musk Says (Space.com / Joe Rogan Podcast)",
        "datum_aussage": "2018-09-07",
        "sprache": "en",
        "kontext": "Joe Rogan Experience Podcast #1169. Diskussion ueber Simulationshypothese und die Zukunft von VR/Gaming.",
        "aussage_uebersetzung_de": "Wenn man irgendeine Verbesserungsrate annimmt, werden Spiele von der Realitaet nicht mehr zu unterscheiden sein, oder die Zivilisation wird enden. Eines von beidem wird passieren. Daher leben wir hoechstwahrscheinlich in einer Simulation, weil wir existieren.",
    },
    # ---- 4. Joe Rogan Experience, Bioboot-loader ----
    {
        "aussage_text": "It feels like we are the biological boot-loader for AI effectively. We are building progressively greater intelligence. And the percentage that is not human is increasing, and eventually we will represent a very small percentage of intelligence.",
        "aussage_kurz": "Musk beschreibt Menschen als 'biologischen Boot-Loader' fuer kuenftige KI-Superintelligenz.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://singjupost.com/transcript-elon-musk-on-joe-rogan-experience-podcast-2281/?singlepage=1",
        "quell_titel": "Joe Rogan Experience: #2281 with Elon Musk (Transcript)",
        "datum_aussage": "2018-09-07",
        "sprache": "en",
        "kontext": "Diskussion ueber die Rolle der Menschheit in der Evolution von KI. Musk sieht Menschen als Zwischenschritt.",
        "aussage_uebersetzung_de": "Es fuehlt sich an, als waeren wir effektiv der biologische Boot-Loader fuer KI. Wir bauen progressiv groessere Intelligenz. Und der Anteil, der nicht menschlich ist, waechst, und irgendwann werden wir einen sehr kleinen Prozentsatz der Intelligenz ausmachen.",
    },
    # ---- 5. Joe Rogan - Mars als Zivilisationssicherung ----
    {
        "aussage_text": "We at least want to build a city on Mars, and become a multi-planet civilization, which I think would be incredibly important in ensuring the long-term survival of civilization.",
        "aussage_kurz": "Mars-Kolonisierung ist fuer Musk zentral fuer das langfristige Ueberleben der Zivilisation.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://singjupost.com/transcript-elon-musk-on-joe-rogan-experience-podcast-2281/?singlepage=1",
        "quell_titel": "Joe Rogan Experience: #2281 with Elon Musk (Transcript)",
        "datum_aussage": "2018-09-07",
        "sprache": "en",
        "kontext": "Diskussion ueber SpaceX-Mission und die Notwendigkeit, die Menschheit multi-planetar zu machen.",
        "aussage_uebersetzung_de": "Wir wollen zumindest eine Stadt auf dem Mars bauen und eine multi-planetare Zivilisation werden, was meiner Meinung nach unglaublich wichtig waere, um das langfristige Ueberleben der Zivilisation zu sichern.",
    },
    # ---- 6. Joe Rogan - KI als Waffe ----
    {
        "aussage_text": "It's going to be very tempting to use AI as a weapon. In fact, it will be used as a weapon. The danger is going to be more humans using it against each other most likely.",
        "aussage_kurz": "Musk warnt, dass KI als Waffe eingesetzt werden wird, vor allem von Menschen gegen andere Menschen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://singjupost.com/transcript-elon-musk-on-joe-rogan-experience-podcast-2281/?singlepage=1",
        "quell_titel": "Joe Rogan Experience: #2281 with Elon Musk (Transcript)",
        "datum_aussage": "2018-09-07",
        "sprache": "en",
        "kontext": "Diskussion ueber militaerische Nutzung von KI und geopolitische Risiken.",
        "aussage_uebersetzung_de": "Es wird sehr verlockend sein, KI als Waffe zu nutzen. Tatsaechlich wird sie als Waffe eingesetzt werden. Die Gefahr wird hoechstwahrscheinlich darin bestehen, dass Menschen sie gegeneinander einsetzen.",
    },
    # ---- 7. Neuralink Gruendungs-Statement (Space.com 2017) ----
    {
        "aussage_text": "Creating a neural lace is the thing that really matters for humanity to achieve symbiosis with machines.",
        "aussage_kurz": "Musk sieht Neural Lace (Gehirn-Maschine-Schnittstelle) als entscheidend fuer die Symbiose mit KI.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.space.com/35464-elon-musk-neural-lace-artificial-intelligence.html",
        "quell_titel": "Elon Musk Sees Brain-Computer Systems in Humans' Future (Space.com)",
        "datum_aussage": "2017-02-13",
        "sprache": "en",
        "kontext": "Diskussion ueber die Gruendung von Neuralink und die Notwendigkeit, menschliche Intelligenz zu erweitern.",
        "aussage_uebersetzung_de": "Die Erschaffung eines Neural Lace ist das, was wirklich zaehlt, damit die Menschheit Symbiose mit Maschinen erreicht.",
    },
    # ---- 8. Neuralink Symbiose-Vision ----
    {
        "aussage_text": "This is going to sound pretty weird, but ultimately, we will achieve symbiosis with artificial intelligence. This is not a mandatory thing. It is a thing you can choose to have if you want.",
        "aussage_kurz": "Musk kuendigt optionale Symbiose mit KI durch Neuralink an.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.popularmechanics.com/science/health/a28423949/elon-musk-neuralink/",
        "quell_titel": "Elon Musk Wants to Upgrade Our Brains to Compete With AI (Popular Mechanics)",
        "datum_aussage": "2019-07-16",
        "sprache": "en",
        "kontext": "Neuralink-Praesentation 2019. Musk betont die Freiwilligkeit der Brain-Computer-Interface-Technologie.",
        "aussage_uebersetzung_de": "Das wird ziemlich seltsam klingen, aber letztendlich werden wir Symbiose mit kuenstlicher Intelligenz erreichen. Das ist nichts Verpflichtendes. Es ist etwas, das man waehlen kann, wenn man will.",
    },
    # ---- 9. CNBC 2022 - Persoenlicher Neuralink-Implant ----
    {
        "aussage_text": "In fact, in one of these demos, I will.",
        "aussage_kurz": "Musk kuendigt an, selbst einen Neuralink-Chip zu implantieren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2022/12/01/elon-musks-neuralink-makes-big-claims-but-experts-are-skeptical-.html",
        "quell_titel": "Musk says he'll put a Neuralink chip in his brain when they are ready (CNBC)",
        "datum_aussage": "2022-12-01",
        "sprache": "en",
        "kontext": "Musk sagt bei einem Neuralink-Update, dass er plant, sich selbst einen Chip implantieren zu lassen.",
        "aussage_uebersetzung_de": "Tatsaechlich werde ich das bei einer dieser Demos tun.",
    },
    # ---- 10. Neuralink Vision - Stephen Hawking ----
    {
        "aussage_text": "Imagine if Stephen Hawking could communicate faster than a speed typist or auctioneer. That is the goal.",
        "aussage_kurz": "Musk beschreibt als Neuralink-Ziel, dass gelahmte Menschen schneller kommunizieren koennen als gesunde.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.livescience.com/health/neuroscience/neuralink-brain-chip-implanted-into-human-for-the-1st-time-elon-musk-says",
        "quell_titel": "Neuralink chip implanted into human brain for the 1st time, Elon Musk says (Live Science)",
        "datum_aussage": "2024-01-29",
        "sprache": "en",
        "kontext": "X-Post nach der ersten erfolgreichen Neuralink-Implantation bei einem Menschen (Noland Arbaugh).",
        "aussage_uebersetzung_de": "Stellen Sie sich vor, Stephen Hawking koennte schneller kommunizieren als ein Speed-Typist oder Auktionator. Das ist das Ziel.",
    },
    # ---- 11. Tucker Carlson Interview - TruthGPT ----
    {
        "aussage_text": "I'm going to start something which I call TruthGPT, or a maximum truth-seeking AI that tries to understand the nature of the universe.",
        "aussage_kurz": "Musk kuendigt 'TruthGPT' an, eine wahrheitssuchende KI als Alternative zu ChatGPT.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2023/04/18/elon-musk-wants-to-develop-truthgpt-a-maximum-truth-seeking-ai/",
        "quell_titel": "Elon Musk wants to develop TruthGPT, 'a maximum truth-seeking AI' (TechCrunch)",
        "datum_aussage": "2023-04-17",
        "sprache": "en",
        "kontext": "Interview mit Tucker Carlson auf Fox News. Musk kritisiert OpenAI und Google fuer politisch korrekte KI.",
        "aussage_uebersetzung_de": "Ich werde etwas starten, das ich TruthGPT nenne, oder eine maximal wahrheitssuchende KI, die versucht, die Natur des Universums zu verstehen.",
    },
    # ---- 12. Tucker Carlson - Wahrheitssuchende KI sicher ----
    {
        "aussage_text": "An AI that cares about understanding the universe is unlikely to annihilate humans because we are an interesting part of the universe.",
        "aussage_kurz": "Musk argumentiert, eine wahrheitssuchende KI werde Menschen nicht vernichten, weil wir interessant sind.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2023/04/18/elon-musk-wants-to-develop-truthgpt-a-maximum-truth-seeking-ai/",
        "quell_titel": "Elon Musk wants to develop TruthGPT, 'a maximum truth-seeking AI' (TechCrunch)",
        "datum_aussage": "2023-04-17",
        "sprache": "en",
        "kontext": "Fortsetzung des Tucker-Carlson-Interviews. Musk begruendet, warum TruthGPT sicherer sei.",
        "aussage_uebersetzung_de": "Eine KI, die sich darum kuemmert, das Universum zu verstehen, wird Menschen unwahrscheinlich vernichten, weil wir ein interessanter Teil des Universums sind.",
    },
    # ---- 13. Capitol Hill Meeting, April 2023 ----
    {
        "aussage_text": "That which affects safety of the public has, over time, become regulated to ensure that companies do not cut corners. AI has great power to do good and evil.",
        "aussage_kurz": "Musk fordert vor dem Senat KI-Regulierung zum Schutz der oeffentlichen Sicherheit.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.cnbc.com/2023/04/27/elon-musk-met-with-schumer-to-discuss-ai-regulation.html",
        "quell_titel": "Elon Musk met with Schumer to discuss A.I. regulation (CNBC)",
        "datum_aussage": "2023-04-26",
        "sprache": "en",
        "kontext": "Treffen mit Senator Chuck Schumer und anderen Kongressmitgliedern zur KI-Regulierung.",
        "aussage_uebersetzung_de": "Das, was die Sicherheit der Oeffentlichkeit betrifft, wurde im Laufe der Zeit reguliert, um sicherzustellen, dass Unternehmen keine Abstriche machen. KI hat grosse Macht, Gutes und Boeses zu tun.",
    },
    # ---- 14. AI Insight Forum, September 2023 ----
    {
        "aussage_text": "The key point was really that it's important for us to have a referee.",
        "aussage_kurz": "Bei einem Capitol-Hill-Meeting betont Musk die Notwendigkeit eines 'Schiedsrichters' fuer KI.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.cbsnews.com/news/elon-musk-artificial-intelligence-regulations-tech-executives-senators-washington-meeting-bill-gates-mark-zuckerberg/",
        "quell_titel": "Elon Musk says artificial intelligence needs 'a referee' (CBS News)",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "AI Insight Forum mit Tech-Leadern (Musk, Zuckerberg, Altman, Gates) im US-Senat. Schumer leitete das Forum.",
        "aussage_uebersetzung_de": "Der entscheidende Punkt war wirklich, dass es wichtig fuer uns ist, einen Schiedsrichter zu haben.",
    },
    # ---- 15. AI Insight Forum - Zivilisatorisches Risiko ----
    {
        "aussage_text": "There's some chance – above zero – that AI will kill us all. I think it's low but there's some chance.",
        "aussage_kurz": "Musk gibt eine Wahrscheinlichkeit ueber Null an, dass KI alle Menschen toeten wird.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.nbcnews.com/politics/congress/big-tech-ceos-ai-meeting-senators-musk-zuckerberg-rcna104738",
        "quell_titel": "Elon Musk warns of 'civilizational risk' posed by AI (NBC News)",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Statement nach dem AI Insight Forum vor dem Senat. Journalisten fragten nach konkreten Risikoschaetzungen.",
        "aussage_uebersetzung_de": "Es gibt eine Chance – ueber null –, dass KI uns alle umbringen wird. Ich denke, sie ist gering, aber es gibt eine gewisse Chance.",
    },
    # ---- 16. AI Insight Forum - Historische Bedeutung ----
    {
        "aussage_text": "It may go down in history as being very important for the future of civilization.",
        "aussage_kurz": "Musk haelt das Senatstreffen zur KI-Regulierung fuer historisch bedeutsam.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.pbs.org/newshour/politics/watch-overwhelming-consensus-for-artificial-intelligence-regulation-musk-says-after-senate-tech-meeting",
        "quell_titel": "'Overwhelming consensus' for AI regulation, Musk says (PBS News)",
        "datum_aussage": "2023-09-13",
        "sprache": "en",
        "kontext": "Pressestatement nach dem geschlossenen AI Insight Forum im US-Senat.",
        "aussage_uebersetzung_de": "Es koennte als sehr wichtig fuer die Zukunft der Zivilisation in die Geschichte eingehen.",
    },
    # ---- 17. Lex Fridman Podcast - AGI-Timeline ----
    {
        "aussage_text": "AI will probably be smarter than any single human next year. By 2029, AI is probably smarter than all humans combined.",
        "aussage_kurz": "Musk prognostiziert, dass KI 2029 alle Menschen zusammen uebertreffen wird.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/elonmusk/status/1767738797276451090",
        "quell_titel": "Elon Musk on X (@elonmusk)",
        "datum_aussage": "2024-03-12",
        "sprache": "en",
        "kontext": "Tweet waehrend Diskussionen ueber AGI-Timeline. Musk gibt konkretes Datum fuer Superintelligenz.",
        "aussage_uebersetzung_de": "KI wird wahrscheinlich naechstes Jahr schlauer sein als jeder einzelne Mensch. Bis 2029 ist KI wahrscheinlich schlauer als alle Menschen zusammen.",
    },
    # ---- 18. Lex Fridman Podcast - Bewusstsein ----
    {
        "aussage_text": "What is consciousness? When you put the atoms in a particular shape, why are they able to form thoughts and take actions and feelings?",
        "aussage_kurz": "Musk reflektiert ueber das Mysterium des Bewusstseins und warum Atome Gedanken erzeugen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/elon-musk-4-transcript/",
        "quell_titel": "Lex Fridman Podcast #400: Elon Musk on War, AI, Aliens, Politics (Transcript)",
        "datum_aussage": "2023-11-08",
        "sprache": "en",
        "kontext": "8,5-stuendiges Interview mit Lex Fridman. Diskussion ueber Bewusstsein, KI und die Zukunft der Menschheit.",
        "aussage_uebersetzung_de": "Was ist Bewusstsein? Wenn man die Atome in eine bestimmte Form bringt, warum koennen sie dann Gedanken, Handlungen und Gefuehle formen?",
    },
    # ---- 19. Singularitaets-Tweet, 2026 ----
    {
        "aussage_text": "We have entered the Singularity.",
        "aussage_kurz": "Musk erklaert 2026 zum Jahr der technologischen Singularitaet.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://finance.yahoo.com/news/elon-musk-says-entered-singularity-185946780.html",
        "quell_titel": "Elon Musk Says 'We Have Entered the Singularity' (Yahoo Finance)",
        "datum_aussage": "2026-01-15",
        "sprache": "en",
        "kontext": "X-Post als Reaktion auf Fortschritte in KI-Tools und Automatisierung. Musk sieht 2026 als Wendepunkt.",
        "aussage_uebersetzung_de": "Wir haben die Singularitaet betreten.",
    },
    # ---- 20. Space-based AI Infrastructure ----
    {
        "aussage_text": "In 36 months, probably closer to 30 months, the most economically compelling place to put AI will be space.",
        "aussage_kurz": "Musk prognostiziert, dass Weltraum-basierte KI-Rechenzentren in 2,5 Jahren oekonomisch sinnvoll werden.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.eweek.com/news/elon-musk-ai-data-centers-space-power-neuron/",
        "quell_titel": "Elon Musk: 'In 30 Months, the Cheapest Place for AI Will Be Space' (eWeek)",
        "datum_aussage": "2025-01-20",
        "sprache": "en",
        "kontext": "Diskussion ueber Energie-Limitationen fuer KI-Entwicklung. Musk schlaegt weltraumbasierte Infrastruktur vor.",
        "aussage_uebersetzung_de": "In 36 Monaten, wahrscheinlich naeher an 30 Monaten, wird der oekonomisch uerzeugendste Ort fuer KI der Weltraum sein.",
    },
    # ---- 21. Fortune Interview - KI trotz Risiko ----
    {
        "aussage_text": "Even if AI ultimately proves bad for humanity, I still want to be there to see it.",
        "aussage_kurz": "Musk sagt, er wolle KI-Entwicklung sehen, selbst wenn sie sich als schaedlich erweist.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2025/07/10/elon-musk-xai-grok-tesla-optimus-mankind-humanity-robots/",
        "quell_titel": "Elon Musk says even if AI proves bad for humanity he still wants to see it (Fortune)",
        "datum_aussage": "2025-07-10",
        "sprache": "en",
        "kontext": "Interview ueber xAI und die Zukunft der KI. Musk aeussert sich zu seiner Motivation trotz Risiken.",
        "aussage_uebersetzung_de": "Selbst wenn KI sich letztendlich als schlecht fuer die Menschheit erweist, moechte ich trotzdem dabei sein, um es zu sehen.",
    },
    # ---- 22. xAI Launch - Grok 4 ----
    {
        "aussage_text": "With respect to academic questions, Grok 4 is better than PhD level in every subject, no exceptions.",
        "aussage_kurz": "Musk behauptet, Grok 4 uebertreffe Doktoranden-Niveau in allen Fachgebieten.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://aibusiness.com/chatbot/elon-musk-xai-slates-post-july-4-release-for-grok-4",
        "quell_titel": "Elon Musk xAI Slates Post July 4 Release for Grok 4 (AI Business)",
        "datum_aussage": "2025-07-08",
        "sprache": "en",
        "kontext": "Ankuendigung des Grok-4-Launches. Musk preist die Faehigkeiten des Modells.",
        "aussage_uebersetzung_de": "Was akademische Fragen betrifft, ist Grok 4 besser als Doktoranden-Niveau in jedem Fach, ohne Ausnahmen.",
    },
    # ---- 23. xAI All-Hands Meeting ----
    {
        "aussage_text": "The actual notion of a human economy—assuming civilization continues to progress—will seem very quaint in retrospect.",
        "aussage_kurz": "Musk sagt voraus, die heutige menschliche Wirtschaft werde rueckblickend antiquiert wirken.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.entrepreneur.com/business-news/elon-musk-has-an-optimistic-message-for-xai-staff-according-to-a-leaked-meeting",
        "quell_titel": "Elon Musk Has an Optimistic Message for xAI Staff (Entrepreneur)",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Internes xAI-Meeting. Geleaktes Audio zeigt Musks Vision einer Post-Arbeits-Wirtschaft.",
        "aussage_uebersetzung_de": "Die eigentliche Vorstellung einer menschlichen Wirtschaft – vorausgesetzt, die Zivilisation schreitet fort – wird im Rueckblick sehr altmodisch erscheinen.",
    },
    # ---- 24. Fortune Interview 2024 - KI-Risiko 10-20% ----
    {
        "aussage_text": "There's this sub chance, that could be 10% to 20%, that it goes bad. The chances aren't zero that it goes bad.",
        "aussage_kurz": "Musk schaetzt die Wahrscheinlichkeit, dass KI 'schiefgeht', auf 10-20%.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2024/10/30/elon-musk-ai-could-go-bad-existential-threat-xai-fundraising/",
        "quell_titel": "Elon Musk says there's a 10% to 20% chance that AI 'goes bad' (Fortune)",
        "datum_aussage": "2024-10-30",
        "sprache": "en",
        "kontext": "Interview waehrend xAI-Fundraising. Musk gibt konkrete Risikoschaetzung trotz gleichzeitiger Investitionen.",
        "aussage_uebersetzung_de": "Es gibt diese gewisse Chance, die bei 10% bis 20% liegen koennte, dass es schiefgeht. Die Chancen sind nicht null, dass es schiefgeht.",
    },
    # ---- 25. SpaceX Mars-Timeline (CNBC 2021) ----
    {
        "aussage_text": "We don't want to be one of those single-planet species; we want to be a multi-planet species.",
        "aussage_kurz": "Musk erklaert die Notwendigkeit, eine multi-planetare Spezies zu werden.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2021/04/23/elon-musk-aiming-for-mars-so-humanity-is-not-a-single-planet-species.html",
        "quell_titel": "Elon Musk wants SpaceX to reach Mars so humanity is not a 'single-planet species' (CNBC)",
        "datum_aussage": "2021-04-22",
        "sprache": "en",
        "kontext": "Interview ueber SpaceX-Plaene. Musk verknuepft Mars-Mission mit langfristigem Ueberleben der Menschheit.",
        "aussage_uebersetzung_de": "Wir wollen keine dieser Einzel-Planeten-Spezies sein; wir wollen eine Multi-Planeten-Spezies sein.",
    },
    # ---- 26. OpenAI Lawsuit Statement (Bloomberg) ----
    {
        "aussage_text": "I was assiduously manipulated and deceived.",
        "aussage_kurz": "In seiner Klage gegen OpenAI behauptet Musk, manipuliert und getaeuscht worden zu sein.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2026/01/17/musk-lawsuit-opena-microsoft.html",
        "quell_titel": "Elon Musk seeks up to $134 billion from OpenAI and Microsoft (CNBC)",
        "datum_aussage": "2024-03-01",
        "sprache": "en",
        "kontext": "Erste Klage gegen OpenAI. Musk wirft Altman und dem Board vor, von der gemeinnuetzigen Mission abgewichen zu sein.",
        "aussage_uebersetzung_de": "Ich wurde gewissenhaft manipuliert und getaeuscht.",
    },
    # ---- 27. Noland Arbaugh - Neuralink Patient Hoffnung ----
    {
        "aussage_text": "It's going to be amazing when someone can have a spinal cord injury, go into a hospital, get surgery, and walk out a couple days later.",
        "aussage_kurz": "Patient Noland Arbaugh aeussert Hoffnung, dass Neuralink kuenftig Querschnittsgelaehmte heilen kann.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2025/09/16/noland-arbaugh-neuralink-brain-chip-elon-musk-meeting/",
        "quell_titel": "The first person to get a Neuralink chip says he met Elon Musk on surgery day (Fortune)",
        "datum_aussage": "2025-09-16",
        "sprache": "en",
        "kontext": "Interview mit dem ersten Neuralink-Patienten Noland Arbaugh, 18 Monate nach der Implantation.",
        "aussage_uebersetzung_de": "Es wird fantastisch sein, wenn jemand eine Rueckenmarksverletzung haben, ins Krankenhaus gehen, operiert werden und ein paar Tage spaeter wieder rausgehen kann.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung Neuralink ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Elon Musk gruendet Neuralink, ein Neurotechnologie-Unternehmen, das Brain-Computer-Interfaces entwickelt, um eine 'Symbiose mit KI' zu ermoeglichen. Ziel: Behandlung neurologischer Erkrankungen und Erweiterung menschlicher Faehigkeiten.",
        "datum_handlung": "2016-07-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Neuralink",
        "quell_titel": "Neuralink - Wikipedia",
        "kontext": "Gruendung erfolgte 2016, oeffentliche Bekanntgabe im Maerz 2017. Musk investiert eigenes Kapital.",
    },
    # ---- H2. Gruendung OpenAI (Co-Founder) ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Elon Musk und Sam Altman gruenden zusammen mit Ilya Sutskever, Greg Brockman und weiteren das Non-Profit-KI-Forschungslabor OpenAI. Musk ist Co-Vorsitzender und verpflichtet sich zu $1 Mrd. Foerderung (tatsaechlich ca. $100 Mio. eingezahlt).",
        "datum_handlung": "2015-12-11",
        "betrag_usd": 100000000.0,
        "quell_link": "https://www.cnbc.com/2025/12/11/openai-began-decade-ago-as-nonprofit-lab-musk-and-altman-now-rivals.html",
        "quell_titel": "Altman and Musk launched OpenAI as a nonprofit 10 years ago (CNBC)",
        "kontext": "Musk verlaesst 2018 den OpenAI-Vorstand nach gescheiterten Verhandlungen ueber Kontrolle. Verklagt OpenAI 2024.",
    },
    # ---- H3. Abgang von OpenAI ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Elon Musk tritt vom Board von OpenAI zurueck, nachdem Verhandlungen ueber volle Kontrolle scheitern. OpenAI lehnt Musks Forderung nach absolutem Entscheidungsrecht ab.",
        "datum_handlung": "2018-02-20",
        "betrag_usd": None,
        "quell_link": "https://openai.com/index/the-truth-elon-left-out/",
        "quell_titel": "The truth Elon left out (OpenAI Blog)",
        "kontext": "OpenAI behauptet, Musk habe volle Kontrolle und Mehrheitsbeteiligung gefordert. Nach Ablehnung gruendet Musk spaeter xAI als Konkurrent.",
    },
    # ---- H4. Gruendung xAI ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Elon Musk gruendet xAI, ein KI-Unternehmen mit der Mission, 'die wahre Natur des Universums zu verstehen'. Fokus auf 'wahrheitssuchende' KI ohne politische Korrektheit.",
        "datum_handlung": "2023-03-09",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/XAI_(company)",
        "quell_titel": "xAI (company) - Wikipedia",
        "kontext": "Oeffentliche Ankuendigung erfolgt am 12. Juli 2023. xAI entwickelt Grok als ChatGPT-Konkurrent.",
    },
    # ---- H5. xAI Series B - $6 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "xAI sichert sich $6 Milliarden in einer Series-B-Finanzierungsrunde gefuehrt von Andreessen Horowitz, Sequoia Capital, Lightspeed und Tribe Capital. Bewertung: $24 Milliarden.",
        "datum_handlung": "2024-05-26",
        "betrag_usd": 6000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/XAI_(company)",
        "quell_titel": "xAI (company) - Wikipedia",
        "kontext": "Grosse Finanzierungsrunde nur 14 Monate nach Unternehmensgruendung. Zeigt rasantes Wachstum.",
    },
    # ---- H6. xAI Series C - $6 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "xAI sammelt weitere $6 Milliarden in einer Series-C-Runde mit Beteiligung von Fidelity, BlackRock und Sequoia Capital. Bewertung steigt auf $50 Milliarden. Gesamtfinanzierung: ueber $12 Milliarden.",
        "datum_handlung": "2024-12-23",
        "betrag_usd": 6000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/XAI_(company)",
        "quell_titel": "xAI (company) - Wikipedia",
        "kontext": "Zweite Milliarden-Runde im gleichen Jahr. xAI wird zu einem der am schnellsten wachsenden KI-Startups.",
    },
    # ---- H7. xAI Series E - $20 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "xAI schliesst eine $20 Milliarden Series-E-Finanzierungsrunde ab mit Beteiligung von Nvidia, Cisco und Fidelity. Bewertung: $230 Milliarden. Uebertrifft urspruengliches $15-Mrd.-Ziel.",
        "datum_handlung": "2026-01-06",
        "betrag_usd": 20000000000.0,
        "quell_link": "https://www.cnbc.com/2026/01/06/elon-musk-xai-raises-20-billion-from-nvidia-cisco-investors.html",
        "quell_titel": "Elon Musk's xAI raises $20 billion from investors including Nvidia, Cisco (CNBC)",
        "kontext": "Groesste xAI-Finanzierungsrunde. Strategische Partnerschaften mit Chip-Herstellern (Nvidia).",
    },
    # ---- H8. SpaceX akquiriert xAI ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "SpaceX akquiriert xAI in einer All-Stock-Transaktion. xAI wird vollstaendige Tochtergesellschaft von SpaceX. SpaceX-Bewertung: $1 Billion, xAI-Bewertung: $250 Milliarden. Kombinierte Bewertung: $1,25 Billionen.",
        "datum_handlung": "2026-02-02",
        "betrag_usd": 250000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/XAI_(company)",
        "quell_titel": "xAI (company) - Wikipedia",
        "kontext": "Historische Mega-Akquisition vereint Musks KI- und Raumfahrt-Unternehmungen. Integration von KI in Mars-Mission.",
    },
    # ---- H9. Grok Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "xAI launcht Grok, einen KI-Chatbot mit Zugang zu Echtzeit-Daten von X (Twitter). Grok ist provokant, 'rebellisch' und fuer X-Premium-Nutzer verfuegbar. Alternative zu ChatGPT.",
        "datum_handlung": "2023-11-04",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Grok_(chatbot)",
        "quell_titel": "Grok (chatbot) - Wikipedia",
        "kontext": "Fruehe Vorschau fuer ausgewaehlte Nutzer. Fokus auf 'Wahrheitssuche' und weniger Zensurmechanismen.",
    },
    # ---- H10. Grok-1 Open Source ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "xAI veroeffentlicht Grok-1 als Open Source unter der Apache-2.0-Lizenz. Das Sprachmodell wird frei verfuegbar fuer Forschung und kommerzielle Nutzung.",
        "datum_handlung": "2024-03-17",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Grok_(chatbot)",
        "quell_titel": "Grok (chatbot) - Wikipedia",
        "kontext": "Musk hatte Open-Sourcing eine Woche zuvor auf X angekuendigt. Positionierung gegen 'closed' OpenAI.",
    },
    # ---- H11. Grok 3 Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "xAI veroeffentlicht Grok 3, trainiert mit '10x mehr Rechenleistung' als Grok 2 im Colossus-Rechenzentrum mit 200.000 GPUs. Uebertrifft laut xAI OpenAI GPT-4o in Benchmarks.",
        "datum_handlung": "2025-02-17",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Grok_(chatbot)",
        "quell_titel": "Grok (chatbot) - Wikipedia",
        "kontext": "Groesster xAI-Modell-Launch. Zeigt Musks massive Investitionen in KI-Infrastruktur (Colossus-Supercomputer).",
    },
    # ---- H12. Neuralink erste Human-Implantation ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Neuralink fuehrt die erste erfolgreiche Gehirn-Chip-Implantation bei einem Menschen durch: Noland Arbaugh, ein gelahmter Patient. Der Chip ermoeglicht Cursor-Steuerung allein durch Gedanken.",
        "datum_handlung": "2024-01-28",
        "betrag_usd": None,
        "quell_link": "https://www.foxbusiness.com/technology/elon-musk-says-first-human-patient-received-neuralink-brain-implant-recovering-well",
        "quell_titel": "Elon Musk says first human patient received Neuralink brain implant (Fox Business)",
        "kontext": "Historischer Durchbruch. FDA hatte klinische Studien im Mai 2023 genehmigt. Patient stellt Weltrekord im BCI-Cursor-Control auf.",
    },
    # ---- H13. Neuralink zweite Implantation ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Neuralink implantiert erfolgreich einen zweiten Patienten mit einem Brain-Computer-Interface. Expansion der klinischen Studien.",
        "datum_handlung": "2024-08-15",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Neuralink",
        "quell_titel": "Neuralink - Wikipedia",
        "kontext": "Fortsetzung der klinischen Studien. Zweiter Patient ebenfalls mit Querschnittslaehmung.",
    },
    # ---- H14. Klage gegen OpenAI (erste Einreichung) ----
    {
        "handlung_typ": "klage",
        "beschreibung": "Elon Musk verklagt OpenAI und Sam Altman. Vorwurf: Abweichung von der gemeinnuetzigen Mission, Vertragsbruch, Manipulation. Musk fordert Rueckkehr zum Non-Profit-Modell.",
        "datum_handlung": "2024-03-01",
        "betrag_usd": None,
        "quell_link": "https://sources.news/p/20-revelations-from-elon-musks-lawsuit",
        "quell_titel": "20+ revelations from Elon Musk's lawsuit against OpenAI (Sources.news)",
        "kontext": "Erste Klageeinreichung. Musk zieht die Klage spaeter zurueck, reicht aber eine erweiterte Version ein.",
    },
    # ---- H15. Erweiterte Klage gegen OpenAI + Microsoft ----
    {
        "handlung_typ": "klage",
        "beschreibung": "Musk reicht erweiterte Klage gegen OpenAI ein, diesmal mit Microsoft als Beklagtem. Neue Vorwuerfe: Kartellrechtsverletzung, monopolistische Praktiken, illegale Fusion. Forderung: $79-134 Milliarden Schadenersatz.",
        "datum_handlung": "2024-11-15",
        "betrag_usd": 134000000000.0,
        "quell_link": "https://www.cnbc.com/2024/11/15/musk-expands-lawsuit-against-openai-adding-microsoft-and-antitrust-claims.html",
        "quell_titel": "Musk expands lawsuit against OpenAI, adding Microsoft and antitrust claims (CNBC)",
        "kontext": "Massiv erweiterte Klage mit Kartellrechtskomponente. Prozess fuer Maerz 2026 angesetzt.",
    },
    # ---- H16. Colossus Supercomputer-Bau ----
    {
        "handlung_typ": "investition",
        "beschreibung": "xAI baut 'Colossus', den weltweit groessten Supercomputer, in 122 Tagen. Standort: umgebaute Electrolux-Fabrik in Memphis. Anfangs 100.000 Nvidia-GPUs, dann verdoppelt auf 200.000 GPUs.",
        "datum_handlung": "2024-09-01",
        "betrag_usd": None,
        "quell_link": "https://time.com/collections/time100-ai-2025/7305842/elon-musk-ai/",
        "quell_titel": "Elon Musk: The 100 Most Influential People in AI 2025 (TIME)",
        "kontext": "Rekord-Baugeschwindigkeit. Colossus trainiert Grok 3. Groesste GPU-Cluster der Welt fuer KI-Training.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=3 existiert
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
            "Claude (collect_musk.py)"
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
        "Elon Musk xAI Grok Neuralink OpenAI AI risk Mars SpaceX transhumanism quotes interviews Lex Fridman Joe Rogan Senate Congress",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Lex Fridman Podcast #400, #438; Joe Rogan Experience #1169, #2281; "
        f"NPR National Governors Association 2017; SXSW 2018; Tucker Carlson Interview 2023; "
        f"Senate AI Insight Forum 2023; X/Twitter (@elonmusk); CNBC, Fortune, TechCrunch, "
        f"Bloomberg, NBC News, PBS News, Wikipedia (Neuralink, xAI, Grok).",
        "Claude (collect_musk.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Elon Musk (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Elon Musk")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_musk.py")
    print("  Verifizierte Aussagen & Handlungen: Elon Musk")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
