#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_sutskever.py
====================
Sammelt verifizierbare Aussagen und Handlungen von Ilya Sutskever (person_id=12)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Konferenz-Vortraegen, Depositions-Transkripten, Tweets und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 12  # Ilya Sutskever

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
    # ---- 1. Regret Statement (Twitter/X, Nov 2023) ----
    {
        "aussage_text": "I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and I will do everything I can to reunite the company.",
        "aussage_kurz": "Sutskever bedauert oeffentlich seine Beteiligung an der Entlassung von Sam Altman und verspricht, OpenAI wiedervereinigen zu wollen.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/ilyasut/status/1726590052392956028",
        "quell_titel": "Ilya Sutskever on X (@ilyasut)",
        "datum_aussage": "2023-11-20",
        "sprache": "en",
        "kontext": "Tweet drei Tage nach Altmans Entlassung, als 700+ OpenAI-Mitarbeiter mit Kuendigung drohten. Sutskever selbst unterzeichnete den Brief, der den Ruecktritt des Boards forderte.",
        "aussage_uebersetzung_de": "Ich bedauere zutiefst meine Beteiligung an den Handlungen des Vorstands. Ich hatte nie die Absicht, OpenAI zu schaden. Ich liebe alles, was wir zusammen aufgebaut haben, und ich werde alles tun, um das Unternehmen wieder zu vereinen.",
    },
    # ---- 2. Deposition: Rushed Process ----
    {
        "aussage_text": "One thing I can say is that the process was rushed. I think it was rushed because the board was inexperienced.",
        "aussage_kurz": "Sutskever raeumt ein, dass die Entlassung von Altman ueberstuerzt war, weil der Vorstand unerfahren war.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Legal Deposition
        "quell_link": "https://medium.com/@prateekj24/the-52-page-memo-that-nearly-destroyed-openai-inside-ilya-sutskevers-deposition-acef91208a1c",
        "quell_titel": "The 52-Page Memo That Nearly Destroyed OpenAI: Inside Ilya Sutskever's Deposition (Medium)",
        "datum_aussage": "2025-10-01",
        "sprache": "en",
        "kontext": "Deposition am 1. Oktober 2025 im Rahmen von Elon Musks Klage gegen OpenAI und Sam Altman. Erste detaillierte Aussage Sutskevers ueber die Board-Krise.",
        "aussage_uebersetzung_de": "Eines kann ich sagen: Der Prozess war ueberstuerzt. Ich denke, er war ueberstuerzt, weil der Vorstand unerfahren war.",
    },
    # ---- 3. Deposition: Employee Reaction ----
    {
        "aussage_text": "I had not expected them to cheer, but I had not expected them to feel strongly either way.",
        "aussage_kurz": "Sutskever war ueberrascht von der heftigen Reaktion der OpenAI-Mitarbeiter auf Altmans Entlassung.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://medium.com/@prateekj24/the-52-page-memo-that-nearly-destroyed-openai-inside-ilya-sutskevers-deposition-acef91208a1c",
        "quell_titel": "The 52-Page Memo That Nearly Destroyed OpenAI: Inside Ilya Sutskever's Deposition (Medium)",
        "datum_aussage": "2025-10-01",
        "sprache": "en",
        "kontext": "Sutskever erklaert, dass er erwartete, dass die Mitarbeiter indifferent sein wuerden -- nicht dass 700 von 770 mit Kuendigung drohen wuerden.",
        "aussage_uebersetzung_de": "Ich hatte nicht erwartet, dass sie jubeln wuerden, aber ich hatte auch nicht erwartet, dass sie in irgendeiner Weise stark reagieren wuerden.",
    },
    # ---- 4. Deposition: Anthropic Merger ----
    {
        "aussage_text": "I was very unhappy about it. I really did not want OpenAI to merge with Anthropic.",
        "aussage_kurz": "Sutskever war sehr ungluecklich ueber die Ueberlegungen, OpenAI mit Anthropic zu fusionieren.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://officechai.com/ai/openais-board-had-considered-merging-with-anthropic-after-sam-altmans-ouster-in-2023-ilya-sutskever/",
        "quell_titel": "OpenAI's Board Had Considered Merging With Anthropic After Sam Altman's Ouster In 2023: Ilya Sutskever (OfficeChai)",
        "datum_aussage": "2025-10-01",
        "sprache": "en",
        "kontext": "Board-Mitglied Helen Toner erreichte Anthropic-Gruender Dario Amodei am 18. November 2023 mit einem Fusionsvorschlag. Sutskever lehnte dies ab.",
        "aussage_uebersetzung_de": "Ich war sehr ungluecklich darueber. Ich wollte wirklich nicht, dass OpenAI mit Anthropic fusioniert.",
    },
    # ---- 5. NeurIPS 2024: Pre-Training Will End ----
    {
        "aussage_text": "Pre-training as we know it will unquestionably end, because we have but one internet.",
        "aussage_kurz": "Sutskever prognostiziert das Ende des Pre-Trainings wie wir es kennen, weil die Daten begrenzt sind.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion / Keynote
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://dlyog.com/papers/one_internet_v1",
        "quell_titel": "Reflections from Ilya's Full Talk at NeurIPS 2024: 'Pre-Training as We Know It Will End'",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "NeurIPS 2024 Keynote in Vancouver. Sutskever warnt, dass Pre-Training an Datengrenzen stoesst und neue Forschungsansaetze noetig sind.",
        "aussage_uebersetzung_de": "Pre-Training, wie wir es kennen, wird zweifellos enden, weil wir nur ein Internet haben.",
    },
    # ---- 6. NeurIPS 2024: Peak Data ----
    {
        "aussage_text": "At some point though, pre-training will run out of data. The data is very clearly finite.",
        "aussage_kurz": "Sutskever warnt, dass Pre-Training irgendwann keine Daten mehr haben wird -- die Daten sind endlich.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.machine.news/ilya-sutskever-peak-data-ai-openai/",
        "quell_titel": "Open-AI co-founder Ilya Sutskever: Peak Data is here and the end of pre-training is nigh (Machine News)",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "NeurIPS 2024 Talk. Sutskever diskutiert 'Peak Data' -- die Menschheit erreicht die Grenze verfuegbarer Trainingsdaten.",
        "aussage_uebersetzung_de": "Irgendwann wird dem Pre-Training jedoch die Daten ausgehen. Die Daten sind ganz klar endlich.",
    },
    # ---- 7. NeurIPS 2024: Superintelligence is Coming ----
    {
        "aussage_text": "That is obviously where this field is headed. This is obviously what is being built here. Superintelligent AI will have radically different qualities and properties than today's AI.",
        "aussage_kurz": "Sutskever erklaert, dass Superintelligenz offensichtlich das Ziel sei und radikal andere Eigenschaften haben werde.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://blog.biocomm.ai/2024/12/14/ilya-sutskever-sequence-to-sequence-learning-with-neural-networks-what-a-decade-at-neurips-2024/",
        "quell_titel": "Ilya Sutskever at NeurIPS 2024 on Super Intelligence (BioComm.ai)",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "NeurIPS 2024 Keynote 'Sequence to Sequence Learning with Neural Networks: What a Decade'. Sutskever spricht ueber die Zukunft von Superintelligenz.",
        "aussage_uebersetzung_de": "Das ist offensichtlich, wohin dieses Feld sich bewegt. Das ist offensichtlich, was hier gebaut wird. Superintelligente KI wird radikal andere Qualitaeten und Eigenschaften haben als die heutige KI.",
    },
    # ---- 8. Dwarkesh Patel Interview: AGI Timeline ----
    {
        "aussage_text": "Five to twenty years.",
        "aussage_kurz": "Sutskever schaetzt die Entwicklung von AGI auf 5 bis 20 Jahre.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://www.dwarkesh.com/p/ilya-sutskever",
        "quell_titel": "Ilya Sutskever (OpenAI Chief Scientist) - Building AGI, Alignment, & Future Models (Dwarkesh Podcast)",
        "datum_aussage": "2024-06-25",
        "sprache": "en",
        "kontext": "Interview mit Dwarkesh Patel nach Sutskevers Abgang von OpenAI. Auf die Frage nach seiner AGI-Prognose antwortet er knapp mit diesem Zeitrahmen.",
        "aussage_uebersetzung_de": "Fuenf bis zwanzig Jahre.",
    },
    # ---- 9. Dwarkesh Interview: Scaling Will Peter Out ----
    {
        "aussage_text": "Current approaches will go some distance and then peter out. They'll keep improving, but won't deliver AGI. The kind of system that would work is something we don't yet know how to build.",
        "aussage_kurz": "Sutskever glaubt, dass die aktuellen KI-Ansaetze nicht zu AGI fuehren werden -- wir wissen noch nicht, wie man es baut.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.the-ai-corner.com/p/ilya-sutskever-safe-superintelligence-agi-2025",
        "quell_titel": "Ilya Sutskever's New Playbook for AGI (The AI Corner)",
        "datum_aussage": "2024-06-25",
        "sprache": "en",
        "kontext": "Dwarkesh Podcast. Sutskever aeussert sich skeptisch ueber die Faehigkeit aktueller Scaling-Ansaetze, AGI zu erreichen.",
        "aussage_uebersetzung_de": "Die aktuellen Ansaetze werden ein Stueck weit kommen und dann auslaufen. Sie werden sich weiter verbessern, aber nicht AGI liefern. Die Art von System, die funktionieren wuerde, ist etwas, das wir noch nicht zu bauen wissen.",
    },
    # ---- 10. Dwarkesh Interview: Generalization is Key ----
    {
        "aussage_text": "Generalization is the real frontier—today's AI aces benchmarks but fails at simple tasks. Humans learn from far fewer examples. Closing this gap is the key to true intelligence.",
        "aussage_kurz": "Generalisierung ist die wahre Herausforderung -- die Luecke zwischen Benchmarks und einfachen Aufgaben zu schliessen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely",
        "quell_titel": "Unpacking Dwarkesh's Ilya Sutskever Interview on AGI, ASI, and How to Build Both Safely (The Neuron)",
        "datum_aussage": "2024-06-25",
        "sprache": "en",
        "kontext": "Dwarkesh Podcast. Sutskever betont, dass Generalisierung -- nicht nur Skalierung -- der Schluessel zu echter Intelligenz ist.",
        "aussage_uebersetzung_de": "Generalisierung ist die wahre Grenze -- die heutige KI meistert Benchmarks, scheitert aber bei einfachen Aufgaben. Menschen lernen aus weit weniger Beispielen. Diese Luecke zu schliessen, ist der Schluessel zu wahrer Intelligenz.",
    },
    # ---- 11. Dwarkesh Interview: Learning as AGI ----
    {
        "aussage_text": "AGI will start as a superintelligent learner, not an all-knowing oracle. A system that can learn every job extremely fast becomes superintelligent through deployment.",
        "aussage_kurz": "AGI wird ein superintelligenter Lerner sein, kein allwissendes Orakel -- Lernen ist der Weg zu Superintelligenz.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely",
        "quell_titel": "Unpacking Dwarkesh's Ilya Sutskever Interview on AGI, ASI, and How to Build Both Safely (The Neuron)",
        "datum_aussage": "2024-06-25",
        "sprache": "en",
        "kontext": "Sutskever beschreibt seine Vision von AGI als System, das durch schnelles Lernen superintelligent wird, nicht durch umfassende Vorprogrammierung.",
        "aussage_uebersetzung_de": "AGI wird als superintelligenter Lerner beginnen, nicht als allwissendes Orakel. Ein System, das jeden Job extrem schnell lernen kann, wird durch den Einsatz superintelligent.",
    },
    # ---- 12. Compression Theory ----
    {
        "aussage_text": "Good compressors can become good predictors. When training a large neural network to accurately predict the next word, the network learns a world model by learning statistical correlations in text to compress them really well.",
        "aussage_kurz": "Gute Kompressoren werden gute Praediktoren -- neuronale Netze lernen Weltmodelle durch Kompression.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://the-decoder.com/openai-co-founder-explains-the-secret-sauce-behind-unsupervised-learning/",
        "quell_titel": "OpenAI co-founder explains the secret sauce behind unsupervised learning (The Decoder)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Sutskever erklaert seine Theorie des unueberwachten Lernens: Kompression ist eng mit Intelligenz verbunden.",
        "aussage_uebersetzung_de": "Gute Kompressoren koennen gute Praediktoren werden. Wenn man ein grosses neuronales Netzwerk trainiert, das naechste Wort genau vorherzusagen, lernt das Netzwerk ein Weltmodell, indem es statistische Korrelationen im Text lernt, um sie sehr gut zu komprimieren.",
    },
    # ---- 13. AI Consciousness Test ----
    {
        "aussage_text": "Very carefully curate data such that consciousness is never mentioned. If the AI then spontaneously recognized and articulated consciousness, that would constitute evidence of consciousness.",
        "aussage_kurz": "Sutskevers Test fuer KI-Bewusstsein: Wenn eine KI Bewusstsein erkennt, ohne je davon trainiert worden zu sein.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://experiencemachines.substack.com/p/ilya-sutskevers-test-for-ai-consciousness",
        "quell_titel": "Ilya Sutskever's Test for AI Consciousness (Experience Machines)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Sutskever schlaegt einen spezifischen Test vor: KI-Bewusstsein wuerde sich zeigen, wenn eine KI spontan das Konzept erkennt, ohne je damit trainiert worden zu sein.",
        "aussage_uebersetzung_de": "Sehr sorgfaeltig Daten kuratieren, sodass Bewusstsein nie erwaehnt wird. Wenn die KI dann spontan Bewusstsein erkennt und artikuliert, wuerde das als Beweis fuer Bewusstsein gelten.",
    },
    # ---- 14. Psychology Language for NNs ----
    {
        "aussage_text": "Maybe we're now reaching a point where the language of psychology is starting to be appropriate to understand the behavior of these neural networks.",
        "aussage_kurz": "Sutskever glaubt, dass psychologische Begriffe angemessen werden koennten, um neuronale Netze zu verstehen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://towardsdatascience.com/openais-chief-scientist-claimed-ai-may-be-conscious-and-kicked-off-a-furious-debate-7338b95194e/",
        "quell_titel": "OpenAI's Chief Scientist Claimed AI May Be Conscious (Towards Data Science)",
        "datum_aussage": "2022",
        "sprache": "en",
        "kontext": "Sutskever spekuliert, dass fortgeschrittene KI-Systeme psychologische Konzepte rechtfertigen koennten.",
        "aussage_uebersetzung_de": "Vielleicht erreichen wir jetzt einen Punkt, wo die Sprache der Psychologie anfaengt, angemessen zu sein, um das Verhalten dieser neuronalen Netzwerke zu verstehen.",
    },
    # ---- 15. SSI Mission Statement ----
    {
        "aussage_text": "Our first product will be the safe superintelligence, and it will not do anything else up until then.",
        "aussage_kurz": "Sutskevers Firma SSI wird ausschliesslich an sicherer Superintelligenz arbeiten -- keine anderen Produkte.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://ssi.inc/",
        "quell_titel": "Safe Superintelligence Inc. (Official Website)",
        "datum_aussage": "2024-06-19",
        "sprache": "en",
        "kontext": "Ankuendigung der Gruendung von SSI. Sutskever betont den kompromisslosen Fokus auf sichere Superintelligenz.",
        "aussage_uebersetzung_de": "Unser erstes Produkt wird die sichere Superintelligenz sein, und wir werden bis dahin nichts anderes tun.",
    },
    # ---- 16. RLHF and Hallucinations ----
    {
        "aussage_text": "I'm quite hopeful that by simply improving this subsequent reinforcement learning from human feedback step, we can teach it to not hallucinate.",
        "aussage_kurz": "Sutskever hofft, dass verbesserte RLHF-Methoden Halluzinationen verhindern koennen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://labelbox.com/blog/what-does-it-mean-when-an-llm-hallucinates/",
        "quell_titel": "What does it mean when an LLM 'hallucinates'? (Labelbox)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Sutskever aeussert sich optimistisch ueber die Faehigkeit von RLHF, KI-Halluzinationen zu reduzieren.",
        "aussage_uebersetzung_de": "Ich bin recht hoffnungsvoll, dass wir ihm durch einfache Verbesserung dieses nachfolgenden Reinforcement-Learning-aus-menschlichem-Feedback-Schritts beibringen koennen, nicht zu halluzinieren.",
    },
    # ---- 17. Deep Learning 2012-2020 ----
    {
        "aussage_text": "2012 to 2020 was the age of research, 2020 to 2025 was the age of scaling, and 2026 onward will be another age of research.",
        "aussage_kurz": "Sutskever gliedert die KI-Entwicklung in drei Phasen: Forschung (2012-2020), Skalierung (2020-2025), wieder Forschung (2026+).",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://officechai.com/ai/scaling-could-now-give-diminishing-returns-were-back-to-the-age-of-research-ilya-sutskever/",
        "quell_titel": "Scaling Could Now Give Diminishing Returns, We're Back To The Age Of Research: Ilya Sutskever (OfficeChai)",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "NeurIPS 2024. Sutskever beschreibt das Ende der reinen Skalierungsaera und die Rueckkehr zur Grundlagenforschung.",
        "aussage_uebersetzung_de": "2012 bis 2020 war das Zeitalter der Forschung, 2020 bis 2025 war das Zeitalter der Skalierung, und 2026 an wird ein weiteres Zeitalter der Forschung sein.",
    },
    # ---- 18. Feel the AGI ----
    {
        "aussage_text": "Feel the AGI!",
        "aussage_kurz": "Sutskevers beruehmt-beruechtiger Aufruf 'Feel the AGI' bei OpenAI-Team-Meetings.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://genesishumanexperience.com/2025/11/16/feel-the-agi-why-the-worlds-most-consequential-conspiracy-theory-now-shapes-real-policy-research-and-power/",
        "quell_titel": "Feel the AGI? How a Myth Became Silicon Valley's New Religion (Genesis Human Experience)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Berichte von OpenAI-Mitarbeitern, dass Sutskever Team-Meetings mit dem Aufruf 'Feel the AGI!' leitete -- fast wie eine spirituelle Beschwörung.",
        "aussage_uebersetzung_de": "Fuehle die AGI!",
    },
    # ---- 19. Departure Statement (OpenAI) ----
    {
        "aussage_text": "This is a project that is very personally meaningful to me.",
        "aussage_kurz": "Sutskever beschreibt SSI bei seinem Abgang von OpenAI als 'sehr persoenlich bedeutungsvoll'.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 2,
        "quell_link": "https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html",
        "quell_titel": "OpenAI co-founder Ilya Sutskever announces his new AI startup, Safe Superintelligence (CNBC)",
        "datum_aussage": "2024-05-14",
        "sprache": "en",
        "kontext": "Sutskever verlaesst OpenAI nach der turbulenten Board-Krise und der Aufloesung des Superalignment-Teams.",
        "aussage_uebersetzung_de": "Dies ist ein Projekt, das fuer mich sehr persoenlich bedeutungsvoll ist.",
    },
    # ---- 20. AI Safety for Self-Interest ----
    {
        "aussage_text": "There will be a before and an after. I'm working on safety for my own self-interest.",
        "aussage_kurz": "Sutskever arbeitet an KI-Sicherheit aus Eigeninteresse -- es wird ein Vorher und Nachher geben.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://genesishumanexperience.com/2025/11/16/feel-the-agi-why-the-worlds-most-consequential-conspiracy-theory-now-shapes-real-policy-research-and-power/",
        "quell_titel": "Feel the AGI? How a Myth Became Silicon Valley's New Religion (Genesis Human Experience)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Sutskever beschreibt die Entwicklung fortgeschrittener KI als 'monumental, welterschuetternd' und raeumt ein, dass seine Sicherheitsarbeit auch Eigeninteresse ist.",
        "aussage_uebersetzung_de": "Es wird ein Vorher und ein Nachher geben. Ich arbeite an Sicherheit aus meinem eigenen Eigeninteresse.",
    },
    # ---- 21. Big New Vision (Departure) ----
    {
        "aussage_text": "I had a big new vision.",
        "aussage_kurz": "Sutskever erklaert seinen Abgang von OpenAI mit einer 'grossen neuen Vision'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.calcalistech.com/ctechnews/article/sjp2u5oj11e",
        "quell_titel": "Ilya Sutskever breaks silence on OpenAI departure: 'I had a big new vision' (Ctech)",
        "datum_aussage": "2024-11-15",
        "sprache": "en",
        "kontext": "Interview mit CTech. Sutskever spricht erstmals detaillierter ueber die Gruende fuer seinen OpenAI-Abgang.",
        "aussage_uebersetzung_de": "Ich hatte eine grosse neue Vision.",
    },
    # ---- 22. AlexNet Hindsight ----
    {
        "aussage_text": "We got right: betting on deep learning, autoregressive models, and scaling. We got wrong: using pipelining and LSTMs. LSTM architecture is ancient history.",
        "aussage_kurz": "Sutskever reflektiert, dass AlexNet auf Deep Learning und Skalierung richtig setzte, aber LSTMs sind heute 'antike Geschichte'.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://joltml.com/neurips-2024/test-of-time-award/",
        "quell_titel": "NeurIPS 2024 Test of Time Award: GANs and Seq2seq (JolTML)",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "NeurIPS 2024 Keynote. Sutskever ueberblickt die letzten 12 Jahre seit AlexNet und seq2seq und kommentiert, was funktioniert hat und was ueberholt ist.",
        "aussage_uebersetzung_de": "Was wir richtig machten: auf Deep Learning, autoregressive Modelle und Skalierung setzen. Was wir falsch machten: Pipelining und LSTMs verwenden. Die LSTM-Architektur ist antike Geschichte.",
    },
    # ---- 23. Intelligence and Kolmogorov Complexity ----
    {
        "aussage_text": "Kolmogorov complexity well-defines unsupervised learning and LLMs are approximations thereof.",
        "aussage_kurz": "Sutskever erklaert unueberwachtes Lernen durch Kolmogorov-Komplexitaet -- LLMs sind Approximationen davon.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://pub.towardsai.net/compression-is-generalisation-generalisation-is-intelligence-unsupervised-learning-in-large-ebd3413115ee",
        "quell_titel": "Compression is Generalisation, Generalisation is Intelligence (Towards AI)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Sutskever verbindet Informationstheorie und KI: LLMs lernen durch Kompression, was einer Form von Kolmogorov-Komplexitaet entspricht.",
        "aussage_uebersetzung_de": "Kolmogorov-Komplexitaet definiert unueberwachtes Lernen gut, und LLMs sind Approximationen davon.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. AlexNet / ImageNet Win ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Ilya Sutskever, Alex Krizhevsky und Geoffrey Hinton entwickeln AlexNet, das die ImageNet LSVRC-2012-Konkurrenz mit grossem Vorsprung gewinnt. Dies loest die Deep-Learning-Revolution aus.",
        "datum_handlung": "2012-09-30",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Ilya_Sutskever",
        "quell_titel": "Ilya Sutskever - Wikipedia",
        "kontext": "AlexNet reduzierte die Fehlerrate bei der Bilderkennung drastisch und bewies die Ueberlegenheit von Deep Learning. Der Sieg markiert den Beginn der modernen KI-Aera.",
    },
    # ---- H2. Google Brain Acquisition ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Google erwirbt das AlexNet-Team (Geoffrey Hinton, Ilya Sutskever, Alex Krizhevsky) fuer $44 Millionen und weist sie Google Brain zu.",
        "datum_handlung": "2013-03-12",
        "betrag_usd": 44000000.0,
        "quell_link": "https://medium.com/aifrontiers/the-journey-of-openais-founder-ilya-sutskever-s-story-486e96cd008f",
        "quell_titel": "The Journey of OpenAI's Founder Ilya Sutskever's Story (AI Frontiers)",
        "kontext": "Google sichert sich die fuehrenden Koepfe des Deep Learning. Sutskever arbeitet 2013-2015 bei Google Brain.",
    },
    # ---- H3. OpenAI Mitgruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Ilya Sutskever verlaesst Google Brain und gruendet OpenAI zusammen mit Sam Altman, Elon Musk, Greg Brockman, Wojciech Zaremba und John Schulman. Sutskever wird Chief Scientist. OpenAI wird als gemeinnuetziges KI-Forschungslabor gegruendet.",
        "datum_handlung": "2015-12-11",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Ilya_Sutskever",
        "quell_titel": "Ilya Sutskever - Wikipedia",
        "kontext": "OpenAI kuendigt an, $1 Milliarde von Unterstuetzern (u.a. Peter Thiel, Reid Hoffman) erhalten zu haben. Tatsaechlich werden nur ca. $130 Mio. eingezahlt.",
    },
    # ---- H4. GPT-2 Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI veroeffentlicht GPT-2, ein 1,5-Milliarden-Parameter-Sprachmodell. Wegen befuerchteten Missbrauchs wird es zunaechst nur teilweise freigegeben. Sutskever spielt eine zentrale Rolle in der Entwicklung.",
        "datum_handlung": "2019-02-14",
        "betrag_usd": None,
        "quell_link": "https://journeymatters.ai/ilya-the-brain-behind-chatgpt/",
        "quell_titel": "Ilya Sutskever: The brain behind ChatGPT (Journey Matters)",
        "kontext": "GPT-2 zeigt beeindruckende Textgenerierungsfaehigkeiten und provoziert die Diskussion ueber KI-Sicherheit und Dual-Use-Risiken.",
    },
    # ---- H5. GPT-3 Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI launcht GPT-3 mit 175 Milliarden Parametern -- das groesste Sprachmodell seiner Zeit. Sutskever ist massgeblich an der Entwicklung beteiligt.",
        "datum_handlung": "2020-06-11",
        "betrag_usd": None,
        "quell_link": "https://journeymatters.ai/ilya-the-brain-behind-chatgpt/",
        "quell_titel": "Ilya Sutskever: The brain behind ChatGPT (Journey Matters)",
        "kontext": "GPT-3 demonstriert Few-Shot Learning und revolutioniert die Wahrnehmung dessen, was Sprachmodelle leisten koennen.",
    },
    # ---- H6. DALL-E 1 Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Sutskever leitet die Entwicklung von DALL-E 1, einem KI-Bildgenerator, der Bilder aus Textbeschreibungen erstellt.",
        "datum_handlung": "2021-01-05",
        "betrag_usd": None,
        "quell_link": "https://journeymatters.ai/ilya-the-brain-behind-chatgpt/",
        "quell_titel": "Ilya Sutskever: The brain behind ChatGPT (Journey Matters)",
        "kontext": "DALL-E zeigt die Vielseitigkeit von Transformern ueber reine Textverarbeitung hinaus und oeffnet das Feld multimodaler KI.",
    },
    # ---- H7. GPT-4 Development ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Ilya Sutskever ist einer der Hauptarchitekten von GPT-4, dem multimodalen Sprachmodell, das im Maerz 2023 veroeffentlicht wird.",
        "datum_handlung": "2023-03-14",
        "betrag_usd": None,
        "quell_link": "https://www.chaindesk.ai/tools/youtube-summarizer/the-mastermind-behind-gpt-4-and-the-future-of-ai-ilya-sutskever-SjhIlw3Iffs",
        "quell_titel": "The Mastermind Behind GPT-4 and the Future of AI | Ilya Sutskever (ChainDesk)",
        "kontext": "GPT-4 markiert den Durchbruch zu leistungsstarkem multimodalem Reasoning. Sutskever gilt als einer der Hauptverantwortlichen.",
    },
    # ---- H8. Sam Altman Entlassung ----
    {
        "handlung_typ": "entlassung",
        "beschreibung": "Ilya Sutskever fuehrt als Board-Mitglied die Entlassung von Sam Altman als OpenAI-CEO an. Der Board wirft Altman mangelnde Aufrichtigkeit vor.",
        "datum_handlung": "2023-11-17",
        "betrag_usd": None,
        "quell_link": "https://www.axios.com/2023/11/20/sam-altman-fired-openai-board-illya-sutsever-regrets",
        "quell_titel": "OpenAI's Sutskever says he regrets board's firing of Altman (Axios)",
        "kontext": "Sutskever entlaedt Altman persoenlich in einem Google-Meet-Anruf. Die Entscheidung loest die groesste Krise in OpenAIs Geschichte aus.",
    },
    # ---- H9. Employee Letter (Altman Return) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Ilya Sutskever unterzeichnet den offenen Brief von 700+ OpenAI-Mitarbeitern, der den Ruecktritt des Boards fordert -- obwohl er selbst Board-Mitglied ist und Altman entlassen hat.",
        "datum_handlung": "2023-11-19",
        "betrag_usd": None,
        "quell_link": "https://www.ccn.com/news/ilya-sutskever-regrets-firing-altman/",
        "quell_titel": "OpenAI Co-Founder Ilya Sutskever Regrets Firing Altman (CCN)",
        "kontext": "In einer dramatischen Kehrtwende unterzeichnet Sutskever den Brief, der seine eigene Absetzung fordert, nachdem er die Staerke der Mitarbeiterreaktion erkennt.",
    },
    # ---- H10. Ruecktritt vom OpenAI Board ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Nach der Rueckkehr von Sam Altman als CEO tritt Ilya Sutskever vom OpenAI-Board zurueck. Er bleibt zunaechst Chief Scientist.",
        "datum_handlung": "2023-11-22",
        "betrag_usd": None,
        "quell_link": "https://www.axios.com/2023/11/22/openai-microsoft-sam-altman-ceo-chaos-timeline",
        "quell_titel": "OpenAI chaos: A timeline of Sam Altman's firing and return (Axios)",
        "kontext": "Als Teil der Vereinbarung zur Rueckkehr Altmans wird ein neuer Board unter Bret Taylor installiert. Sutskever verliert seinen Sitz.",
    },
    # ---- H11. Abgang von OpenAI ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Ilya Sutskever kuendigt seinen Ruecktritt als Chief Scientist von OpenAI an, um sich einem neuen Projekt zu widmen, das 'sehr persoenlich bedeutungsvoll' fuer ihn sei. Jakub Pachocki uebernimmt seine Position.",
        "datum_handlung": "2024-05-14",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html",
        "quell_titel": "OpenAI dissolves Superalignment AI safety team (CNBC)",
        "kontext": "Sutskever verlaesst OpenAI sechs Monate nach der Board-Krise. Am selben Tag kuendigt auch Jan Leike, Co-Leiter des Superalignment-Teams, seinen Ruecktritt an.",
    },
    # ---- H12. SSI Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Ilya Sutskever gruendet Safe Superintelligence Inc. (SSI) zusammen mit Daniel Gross und Daniel Levy. SSI hat Bueros in Palo Alto und Tel Aviv und fokussiert ausschliesslich auf sichere Superintelligenz.",
        "datum_handlung": "2024-06-19",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html",
        "quell_titel": "OpenAI co-founder Ilya Sutskever announces his new AI startup, Safe Superintelligence (CNBC)",
        "kontext": "Sutskever veroeffentlicht ein Statement: 'Unser erstes Produkt wird die sichere Superintelligenz sein, und wir werden bis dahin nichts anderes tun.'",
    },
    # ---- H13. SSI $1 Billion Funding ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Safe Superintelligence (SSI) sichert sich $1 Milliarde Finanzierung von NFDG (Nat Friedman & Daniel Gross), Andreessen Horowitz, Sequoia Capital, DST Global und SV Angel. Bewertung: $5 Milliarden.",
        "datum_handlung": "2024-09-04",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://techcrunch.com/2024/09/04/ilya-sutskevers-startup-safe-super-intelligence-raises-1b/",
        "quell_titel": "Ilya Sutskever's startup, Safe Superintelligence, raises $1B (TechCrunch)",
        "kontext": "SSI wird mit $5 Mrd. bewertet -- eine der hoechsten Bewertungen fuer ein Startup ohne Produkt. Die Finanzierung soll Rechenleistung und Talente finanzieren.",
    },
    # ---- H14. NeurIPS Test of Time Award (Seq2Seq) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Ilya Sutskever, Oriol Vinyals und Quoc V. Le erhalten den NeurIPS 2024 Test of Time Award fuer ihr Paper 'Sequence to Sequence Learning with Neural Networks'.",
        "datum_handlung": "2024-12-10",
        "betrag_usd": None,
        "quell_link": "https://blog.neurips.cc/2024/11/27/announcing-the-neurips-2024-test-of-time-paper-awards/",
        "quell_titel": "Announcing the NeurIPS 2024 Test of Time Paper Awards (NeurIPS Blog)",
        "kontext": "Sutskever komplettiert damit einen NeurIPS-Hattrick -- er war Co-Autor bei den Test of Time Awards 2022, 2023 und 2024.",
    },
    # ---- H15. SSI $2 Billion Funding ($32B Valuation) ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Safe Superintelligence (SSI) sichert sich weitere $2 Milliarden in einer von Greenoaks Capital gefuehrten Finanzierungsrunde. Die Bewertung steigt auf $30-32 Milliarden -- das Sechsfache der vorherigen Bewertung.",
        "datum_handlung": "2025-03-10",
        "betrag_usd": 2000000000.0,
        "quell_link": "https://www.calcalistech.com/ctechnews/article/hjfywdtajl",
        "quell_titel": "Ilya Sutskever's Safe Superintelligence raises $2B at $32B valuation—with no product yet (CTech)",
        "kontext": "SSI erreicht eine der hoechsten Bewertungen fuer ein Startup ohne kommerzielles Produkt. Investoren: Greenoaks Capital, Alphabet, Nvidia u.a.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=12 existiert
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
            "Claude (collect_sutskever.py)"
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
        "Ilya Sutskever quotes, NeurIPS 2024, SSI, OpenAI board crisis, Dwarkesh Patel, deposition, AlexNet, GPT-4, consciousness, safe superintelligence",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: NeurIPS 2024 Keynote, Dwarkesh Patel Podcast, Musk v. OpenAI Deposition (Oct 2025), "
        f"Twitter/X (@ilyasut), CNBC, TechCrunch, Medium, The Decoder, Axios, CTech, "
        f"Safe Superintelligence Inc. (ssi.inc), Wikipedia, Academic Papers (NeurIPS, Seq2Seq).",
        "Claude (collect_sutskever.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Ilya Sutskever (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Ilya Sutskever")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_sutskever.py")
    print("  Verifizierte Aussagen & Handlungen: Ilya Sutskever")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
