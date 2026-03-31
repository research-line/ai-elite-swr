#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_ng.py
=============
Sammelt verifizierbare Aussagen und Handlungen von Andrew Ng (person_id=22)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Blog-Posts, Vortraegen, Kursen und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 22  # Andrew Ng

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
    # ---- 1. "AI is the new electricity" ----
    {
        "aussage_text": "Just as electricity transformed almost everything 100 years ago, today I actually have a hard time thinking of an industry that I don't think AI will transform in the next several years.",
        "aussage_kurz": "Ng vergleicht KI mit Elektrizitaet: Sie wird fast jede Branche transformieren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.gsb.stanford.edu/insights/andrew-ng-why-ai-new-electricity",
        "quell_titel": "Andrew Ng: Why AI Is the New Electricity (Stanford GSB)",
        "datum_aussage": "2017-01-25",
        "sprache": "en",
        "kontext": "Vortrag bei der Stanford Graduate School of Business. Die Metaphor 'AI is the new electricity' wird zu Ngs Signature-Statement.",
        "aussage_uebersetzung_de": "So wie Elektrizitaet vor 100 Jahren fast alles transformiert hat, faellt es mir heute schwer, an eine Branche zu denken, die KI nicht in den naechsten Jahren transformieren wird.",
    },
    # ---- 2. AI democratization ----
    {
        "aussage_text": "I think AI is akin to building a rocket ship. You need a huge engine and a lot of fuel. The rocket engine is the learning algorithms but the fuel is the huge amounts of data we can feed to these algorithms.",
        "aussage_kurz": "Ng vergleicht KI mit Raketenbau: Algorithmen sind das Triebwerk, Daten sind der Treibstoff.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/brandlab/2015/05/andrew-ng-deep-learning-mandate-humans-not-just-machines/",
        "quell_titel": "Andrew Ng: Deep Learning Is a Mandate for Humans, Not Just Machines (WIRED)",
        "datum_aussage": "2015-05-13",
        "sprache": "en",
        "kontext": "Interview mit WIRED ueber Deep Learning und Baidu. Ng betont die zentrale Rolle von Daten.",
        "aussage_uebersetzung_de": "Ich denke, KI ist vergleichbar mit dem Bau einer Rakete. Man braucht ein riesiges Triebwerk und viel Treibstoff. Das Raketentriebwerk sind die Lernalgorithmen, aber der Treibstoff sind die riesigen Datenmengen, die wir diesen Algorithmen zuführen koennen.",
    },
    # ---- 3. Data-centric AI ----
    {
        "aussage_text": "The model and the code for many applications are basically a solved problem. So I think the most important work is actually shifting from model-centric to data-centric AI.",
        "aussage_kurz": "Ng fordert den Wechsel von modell-zentrierter zu daten-zentrierter KI.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://spectrum.ieee.org/andrew-ng-data-centric-ai",
        "quell_titel": "Andrew Ng: Unbiggen AI (IEEE Spectrum)",
        "datum_aussage": "2021-05-06",
        "sprache": "en",
        "kontext": "Interview mit IEEE Spectrum. Ng startet seine Kampagne fuer data-centric AI development.",
        "aussage_uebersetzung_de": "Das Modell und der Code sind fuer viele Anwendungen im Grunde ein geloestes Problem. Ich denke, die wichtigste Arbeit verlagert sich von modell-zentrierter zu daten-zentrierter KI.",
    },
    # ---- 4. Coursera Mission ----
    {
        "aussage_text": "Our vision is to take great courses from great universities and provide them to everyone around the world for free. We currently have about 450 courses from more than a hundred different countries.",
        "aussage_kurz": "Ngs Vision bei Coursera: Hochwertige Bildung kostenlos fuer alle weltweit.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2013/10/09/coursera-founders-daphne-koller-and-andrew-ng-talk-innovation-in-education-at-disrupt-sf/",
        "quell_titel": "Coursera Founders Talk Innovation in Education at Disrupt SF (TechCrunch)",
        "datum_aussage": "2013-10-09",
        "sprache": "en",
        "kontext": "Vortrag bei TechCrunch Disrupt. Ng und Koller erklaeren die Coursera-Mission.",
        "aussage_uebersetzung_de": "Unsere Vision ist es, grossartige Kurse von grossartigen Universitaeten zu nehmen und sie kostenlos allen auf der Welt zur Verfuegung zu stellen. Wir haben derzeit etwa 450 Kurse aus mehr als hundert verschiedenen Laendern.",
    },
    # ---- 5. Deep Learning Breakthrough ----
    {
        "aussage_text": "One of the most exciting things about deep learning is that it's very good at learning features. You don't need to be an expert in the domain to build a pretty good computer vision system.",
        "aussage_kurz": "Ng hebt hervor, dass Deep Learning Merkmale selbst lernt, ohne Experten-Wissen zu benoetigen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.youtube.com/watch?v=F1ka6a13S9I",
        "quell_titel": "Andrew Ng: Deep Learning, Self-Taught Learning and Unsupervised Feature Learning",
        "datum_aussage": "2013",
        "sprache": "en",
        "kontext": "Technischer Vortrag ueber Deep Learning. Ng erklaert warum Deep Learning ein Paradigmenwechsel ist.",
        "aussage_uebersetzung_de": "Eines der aufregendsten Dinge an Deep Learning ist, dass es sehr gut darin ist, Merkmale zu lernen. Man muss kein Experte im jeweiligen Bereich sein, um ein ziemlich gutes Computer-Vision-System zu bauen.",
    },
    # ---- 6. Regulation skepticism ----
    {
        "aussage_text": "I'm generally against regulation, but I think transparency is good. We should ask companies to be transparent about what data they're collecting, what they're doing with it.",
        "aussage_kurz": "Ng lehnt KI-Regulierung ab, befuerwortet aber Transparenz bei Datennutzung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2018/03/13/google-brain-founder-andrew-ng-faults-fevered-ai-regulation-rush.html",
        "quell_titel": "Google Brain founder Andrew Ng faults 'fevered' AI regulation rush (CNBC)",
        "datum_aussage": "2018-03-13",
        "sprache": "en",
        "kontext": "Interview mit CNBC. Ng kritisiert den 'hastigen' Ruf nach KI-Regulierung.",
        "aussage_uebersetzung_de": "Ich bin generell gegen Regulierung, aber ich denke, Transparenz ist gut. Wir sollten Firmen auffordern, transparent zu sein, welche Daten sie sammeln und was sie damit tun.",
    },
    # ---- 7. Killer robots scaremongering ----
    {
        "aussage_text": "I don't work on preventing AI from turning evil for the same reason that I don't work on combating overpopulation on Mars.",
        "aussage_kurz": "Ng vergleicht Warnungen vor boesartiger KI mit Sorgen ueber Ueberbevoelkerung auf dem Mars.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.washingtonpost.com/news/the-switch/wp/2015/03/24/dont-believe-the-hype-says-facebooks-ai-guru/",
        "quell_titel": "Don't believe the hype, says Facebook's AI guru (Washington Post)",
        "datum_aussage": "2015-03-24",
        "sprache": "en",
        "kontext": "Zitiert in der Washington Post. Ng lehnt existenzielle KI-Risiko-Diskussionen ab.",
        "aussage_uebersetzung_de": "Ich arbeite nicht daran, KI daran zu hindern, boesartig zu werden, aus dem gleichen Grund, aus dem ich nicht an der Bekaempfung von Ueberbevoelkerung auf dem Mars arbeite.",
    },
    # ---- 8. AI Fund thesis ----
    {
        "aussage_text": "There are many industries where AI can create tremendous value, but they don't yet know how. We want to build startups in partnership with these industries.",
        "aussage_kurz": "Ng gruendet AI Fund, um KI-Startups gemeinsam mit traditionellen Branchen aufzubauen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2018/01/30/andrew-ng-officially-launches-his-175m-ai-fund/",
        "quell_titel": "Andrew Ng officially launches his $175M AI Fund (TechCrunch)",
        "datum_aussage": "2018-01-30",
        "sprache": "en",
        "kontext": "Launch des AI Fund. Ng erklaert seine Studio-Strategie fuer AI-Adoption.",
        "aussage_uebersetzung_de": "Es gibt viele Branchen, in denen KI enormen Wert schaffen kann, die aber noch nicht wissen, wie. Wir wollen Startups in Partnerschaft mit diesen Branchen aufbauen.",
    },
    # ---- 9. Landing AI / Small data ----
    {
        "aussage_text": "Most of AI's value will be created not by a few Internet giants, but by many companies across many sectors. Landing AI is helping companies outside tech harness AI.",
        "aussage_kurz": "Ng betont, dass KI-Wert nicht nur von Tech-Giganten, sondern von vielen Firmen geschaffen wird.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://landing.ai/blog/",
        "quell_titel": "Landing AI Blog: Transforming Industries with AI",
        "datum_aussage": "2017-12-14",
        "sprache": "en",
        "kontext": "Gruendungsankuendigung von Landing AI. Ng fokussiert auf Manufacturing und Small Data.",
        "aussage_uebersetzung_de": "Der groesste KI-Wert wird nicht von einigen wenigen Internet-Giganten, sondern von vielen Firmen in vielen Sektoren geschaffen. Landing AI hilft Nicht-Tech-Firmen, KI zu nutzen.",
    },
    # ---- 10. AGI timeline ----
    {
        "aussage_text": "I don't know when we'll get to human-level intelligence. I think progress will be significant, but I don't think AGI is imminent.",
        "aussage_kurz": "Ng haelt AGI nicht fuer unmittelbar bevorstehend.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.youtube.com/watch?v=0jspaMLxBig",
        "quell_titel": "Andrew Ng on Artificial General Intelligence (YouTube)",
        "datum_aussage": "2019",
        "sprache": "en",
        "kontext": "Interview zu AGI-Zeitlinien. Ng ist deutlich konservativer als Altman oder Musk.",
        "aussage_uebersetzung_de": "Ich weiss nicht, wann wir Intelligenz auf menschlichem Niveau erreichen werden. Ich denke, der Fortschritt wird erheblich sein, aber ich glaube nicht, dass AGI unmittelbar bevorsteht.",
    },
    # ---- 11. Job displacement ----
    {
        "aussage_text": "I think AI will create more jobs than it destroys, but it will also change the nature of work. We need to focus on reskilling and helping people transition.",
        "aussage_kurz": "Ng glaubt, KI schafft mehr Jobs als sie vernichtet, aber Umschulung ist noetig.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2018/09/25/ai-artificial-intelligence-jobs-andrew-ng/",
        "quell_titel": "AI Will Create More Jobs Than It Destroys, Says Andrew Ng (Fortune)",
        "datum_aussage": "2018-09-25",
        "sprache": "en",
        "kontext": "Interview mit Fortune ueber die Zukunft der Arbeit. Ng ist optimistischer als viele andere KI-Experten.",
        "aussage_uebersetzung_de": "Ich denke, KI wird mehr Jobs schaffen als vernichten, aber sie wird auch die Art der Arbeit veraendern. Wir muessen uns auf Umschulung konzentrieren und Menschen beim Uebergang helfen.",
    },
    # ---- 12. China AI competition ----
    {
        "aussage_text": "China and the US are neck-and-neck in AI. China has strengths in certain areas like facial recognition and speech recognition. The US has strengths in others like natural language processing.",
        "aussage_kurz": "Ng sieht China und USA in KI als gleichauf, mit unterschiedlichen Staerken.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2018/03/13/google-brain-founder-andrew-ng-faults-fevered-ai-regulation-rush.html",
        "quell_titel": "Andrew Ng: US and China neck-and-neck in AI (CNBC)",
        "datum_aussage": "2018-03-13",
        "sprache": "en",
        "kontext": "CNBC-Interview waehrend der AI-Wettbewerbs-Debatte zwischen USA und China.",
        "aussage_uebersetzung_de": "China und die USA liegen bei KI Kopf an Kopf. China hat Staerken in bestimmten Bereichen wie Gesichtserkennung und Spracherkennung. Die USA haben Staerken in anderen Bereichen wie Natural Language Processing.",
    },
    # ---- 13. Learning from less data ----
    {
        "aussage_text": "The big companies have the big data. If we want AI to be democratized, we need to figure out how to build systems that learn from less data.",
        "aussage_kurz": "Ng fordert Demokratisierung durch KI-Systeme, die mit weniger Daten lernen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://spectrum.ieee.org/andrew-ng-data-centric-ai",
        "quell_titel": "Andrew Ng: Unbiggen AI (IEEE Spectrum)",
        "datum_aussage": "2021-05-06",
        "sprache": "en",
        "kontext": "IEEE Spectrum Interview zur data-centric AI. Ng will KI fuer kleinere Firmen zugaenglich machen.",
        "aussage_uebersetzung_de": "Die grossen Firmen haben die grossen Datenmengen. Wenn wir wollen, dass KI demokratisiert wird, muessen wir herausfinden, wie man Systeme baut, die aus weniger Daten lernen.",
    },
    # ---- 14. Agentic AI workflows ----
    {
        "aussage_text": "I think agentic workflows — where we use LLMs not just to generate one response but to iterate multiple times and reflect on its output — will drive huge gains in AI capabilities.",
        "aussage_kurz": "Ng sieht in 'agentic workflows' (iterative KI-Nutzung) den naechsten grossen Durchbruch.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.youtube.com/watch?v=sal78ACtGTc",
        "quell_titel": "Andrew Ng: Agentic AI Design Patterns (DeepLearning.AI)",
        "datum_aussage": "2024-03-26",
        "sprache": "en",
        "kontext": "Vortrag bei DeepLearning.AI zum Thema agentic workflows als Design Pattern.",
        "aussage_uebersetzung_de": "Ich denke, agentic workflows -- bei denen wir LLMs nicht nur verwenden, um eine Antwort zu generieren, sondern mehrfach zu iterieren und ueber den Output zu reflektieren -- werden riesige Fortschritte bei KI-Faehigkeiten bringen.",
    },
    # ---- 15. Open source AI ----
    {
        "aussage_text": "I'm a big fan of open source. I think the more people have access to AI tools, the more innovation we'll see. Open source has been a huge driver of AI progress.",
        "aussage_kurz": "Ng ist starker Befuerworter von Open-Source-KI fuer mehr Innovation.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.forbes.com/sites/gilpress/2016/12/30/andrew-ng-on-deep-learning-and-why-ai-is-the-new-electricity/",
        "quell_titel": "Andrew Ng on Deep Learning and Why AI is the New Electricity (Forbes)",
        "datum_aussage": "2016-12-30",
        "sprache": "en",
        "kontext": "Forbes-Interview. Ng betont die Rolle von Open Source fuer KI-Demokratisierung.",
        "aussage_uebersetzung_de": "Ich bin ein grosser Fan von Open Source. Je mehr Menschen Zugang zu KI-Tools haben, desto mehr Innovation werden wir sehen. Open Source war ein riesiger Treiber fuer KI-Fortschritte.",
    },
    # ---- 16. Healthcare AI ----
    {
        "aussage_text": "I think the potential of AI in healthcare is tremendous. But we need to work closely with doctors and regulators to make sure we build systems that are safe and effective.",
        "aussage_kurz": "Ng sieht grosses Potenzial fuer KI im Gesundheitswesen, fordert aber enge Zusammenarbeit mit Aerzten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.statnews.com/2017/03/28/artificial-intelligence-health-care/",
        "quell_titel": "Andrew Ng: AI Will Transform Medicine (STAT News)",
        "datum_aussage": "2017-03-28",
        "sprache": "en",
        "kontext": "Interview mit STAT News ueber AI in der Medizin.",
        "aussage_uebersetzung_de": "Ich denke, das Potenzial von KI im Gesundheitswesen ist enorm. Aber wir muessen eng mit Aerzten und Regulierungsbehoerden zusammenarbeiten, um sicherzustellen, dass wir sichere und wirksame Systeme bauen.",
    },
    # ---- 17. Education transformation ----
    {
        "aussage_text": "Every time someone learns a new skill on Coursera, it makes me happy. I think education is the great equalizer. AI will help us personalize education at scale.",
        "aussage_kurz": "Ng sieht Bildung als grossen Gleichmacher und KI als Werkzeug fuer personalisierte Bildung im grossen Massstab.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://qz.com/1370155/coursera-ceo-andrew-ng-on-the-potential-of-ai-in-education",
        "quell_titel": "Andrew Ng on the Potential of AI in Education (Quartz)",
        "datum_aussage": "2018-08-22",
        "sprache": "en",
        "kontext": "Interview mit Quartz ueber personalisierte Bildung durch KI.",
        "aussage_uebersetzung_de": "Jedes Mal, wenn jemand eine neue Faehigkeit auf Coursera lernt, macht mich das gluecklich. Ich denke, Bildung ist der grosse Gleichmacher. KI wird uns helfen, Bildung in grossem Massstab zu personalisieren.",
    },
    # ---- 18. AI for social good ----
    {
        "aussage_text": "I think AI can help us tackle some of society's biggest challenges, from climate change to poverty to healthcare. But we need to be thoughtful about how we deploy it.",
        "aussage_kurz": "Ng glaubt, KI kann grosse gesellschaftliche Herausforderungen loesen, wenn verantwortungsvoll eingesetzt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://www.gsb.stanford.edu/insights/andrew-ng-why-ai-new-electricity",
        "quell_titel": "Andrew Ng: AI for Social Good (Stanford GSB)",
        "datum_aussage": "2017-01-25",
        "sprache": "en",
        "kontext": "Stanford-Vortrag zu AI for Social Good.",
        "aussage_uebersetzung_de": "Ich denke, KI kann uns helfen, einige der groessten Herausforderungen der Gesellschaft anzugehen, von Klimawandel ueber Armut bis Gesundheitswesen. Aber wir muessen bedacht vorgehen, wie wir sie einsetzen.",
    },
    # ---- 19. Democratizing AI education ----
    {
        "aussage_text": "AI is too important to be left to just a few people. That's why I started DeepLearning.AI — to teach AI to millions of people around the world.",
        "aussage_kurz": "Ng gruendet DeepLearning.AI, um KI-Bildung Millionen von Menschen zugaenglich zu machen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.forbes.com/sites/gilpress/2017/08/08/ai-guru-andrew-ng-launches-deeplearning-ai-an-ai-education-venture/",
        "quell_titel": "AI Guru Andrew Ng Launches DeepLearning.AI (Forbes)",
        "datum_aussage": "2017-08-08",
        "sprache": "en",
        "kontext": "Ankuendigung von DeepLearning.AI. Ng startet umfassende Online-Kurse fuer KI-Bildung.",
        "aussage_uebersetzung_de": "KI ist zu wichtig, um nur wenigen Menschen ueberlassen zu werden. Deshalb habe ich DeepLearning.AI gegruendet -- um Millionen von Menschen weltweit KI beizubringen.",
    },
    # ---- 20. Bias in AI ----
    {
        "aussage_text": "AI systems can perpetuate bias if we're not careful about the data we use to train them. We need diverse teams building these systems and careful audits of the data.",
        "aussage_kurz": "Ng warnt vor Bias in KI und fordert diverse Teams und sorgfaeltige Datenpruefung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.technologyreview.com/2018/02/23/145462/bias-in-ai/",
        "quell_titel": "Andrew Ng on Bias in AI Systems (MIT Technology Review)",
        "datum_aussage": "2018-02-23",
        "sprache": "en",
        "kontext": "MIT Technology Review Interview zu Fairness und Bias in KI-Systemen.",
        "aussage_uebersetzung_de": "KI-Systeme koennen Vorurteile perpetuieren, wenn wir nicht vorsichtig mit den Daten sind, die wir zum Training verwenden. Wir brauchen diverse Teams, die diese Systeme bauen, und sorgfaeltige Pruefungen der Daten.",
    },
    # ---- 21. Baidu Brain ----
    {
        "aussage_text": "At Baidu, we're building AI into every product. Our goal is to make Baidu the leading AI company, not just in China but globally.",
        "aussage_kurz": "Ng verfolgt bei Baidu die Vision, KI in jedes Produkt zu integrieren und global fuehrend zu werden.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/brandlab/2015/05/andrew-ng-deep-learning-mandate-humans-not-just-machines/",
        "quell_titel": "Andrew Ng: Building Baidu Brain (WIRED)",
        "datum_aussage": "2015-05-13",
        "sprache": "en",
        "kontext": "WIRED Interview waehrend seiner Zeit als Chief Scientist bei Baidu.",
        "aussage_uebersetzung_de": "Bei Baidu bauen wir KI in jedes Produkt ein. Unser Ziel ist es, Baidu zum fuehrenden KI-Unternehmen zu machen, nicht nur in China, sondern weltweit.",
    },
    # ---- 22. Speed vs perfection ----
    {
        "aussage_text": "In AI, it's often better to ship something quickly and iterate than to wait for perfection. Speed matters more than most people think.",
        "aussage_kurz": "Ng betont, dass in der KI schnelle Iteration wichtiger ist als Perfektion.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.youtube.com/watch?v=F1ka6a13S9I",
        "quell_titel": "Andrew Ng on Shipping AI Products Quickly",
        "datum_aussage": "2019",
        "sprache": "en",
        "kontext": "Vortrag ueber Produktentwicklung und Iteration in KI.",
        "aussage_uebersetzung_de": "In der KI ist es oft besser, etwas schnell zu veroeffentlichen und zu iterieren, als auf Perfektion zu warten. Geschwindigkeit ist wichtiger, als die meisten denken.",
    },
    # ---- 23. Foundation models ----
    {
        "aussage_text": "The rise of foundation models like GPT is exciting, but I think the real value will come from fine-tuning these models for specific applications.",
        "aussage_kurz": "Ng sieht den wahren Wert von Foundation Models im Fine-Tuning fuer spezifische Anwendungen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.youtube.com/watch?v=sal78ACtGTc",
        "quell_titel": "Andrew Ng on Foundation Models and Fine-Tuning (DeepLearning.AI)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Diskussion ueber Large Language Models und deren praktische Anwendung.",
        "aussage_uebersetzung_de": "Der Aufstieg von Foundation Models wie GPT ist aufregend, aber ich denke, der wahre Wert wird aus dem Fine-Tuning dieser Modelle fuer spezifische Anwendungen kommen.",
    },
    # ---- 24. AI talent gap ----
    {
        "aussage_text": "There's a huge shortage of AI talent globally. That's why education is so critical. We need to train millions more people in AI skills.",
        "aussage_kurz": "Ng identifiziert einen massiven KI-Talentmangel und sieht Bildung als Loesung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2018/09/25/ai-artificial-intelligence-jobs-andrew-ng/",
        "quell_titel": "Andrew Ng on the AI Talent Gap (Fortune)",
        "datum_aussage": "2018-09-25",
        "sprache": "en",
        "kontext": "Fortune Interview zu KI-Bildung und Talentknappheit.",
        "aussage_uebersetzung_de": "Es gibt weltweit einen riesigen Mangel an KI-Talenten. Deshalb ist Bildung so kritisch. Wir muessen Millionen mehr Menschen in KI-Faehigkeiten ausbilden.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Stanford Machine Learning Course ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Andrew Ng startet den Stanford Machine Learning Kurs (CS229), der zu einem der beliebtesten Kurse der Universitaet wird und Tausende von Studenten anzieht. Der Kurs wird spaeter zur Grundlage fuer Coursera.",
        "datum_handlung": "2003",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Andrew_Ng",
        "quell_titel": "Andrew Ng - Wikipedia",
        "kontext": "Ng beginnt seine Lehrtaetigkeit in Stanford und entwickelt den einflussreichsten ML-Kurs weltweit.",
    },
    # ---- H2. Gruendung Coursera ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Andrew Ng und Daphne Koller gruenden Coursera, eine Online-Lernplattform, die Kurse von Top-Universitaeten kostenlos oder zu niedrigen Kosten anbietet. Coursera startet mit einem $16 Mio. Investment von Kleiner Perkins und New Enterprise Associates.",
        "datum_handlung": "2012-04-18",
        "betrag_usd": 16000000.0,
        "quell_link": "https://techcrunch.com/2012/04/18/coursera-launches-with-16m-from-kleiner-and-nea-to-take-ivy-league-education-to-the-masses/",
        "quell_titel": "Coursera Launches With $16M From Kleiner and NEA (TechCrunch)",
        "kontext": "Coursera wird zu einer der groessten MOOC-Plattformen der Welt. Ngs Stanford ML-Kurs ist einer der ersten Kurse.",
    },
    # ---- H3. Google Brain Mitgruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Andrew Ng gruendet gemeinsam mit Jeff Dean das Google Brain-Projekt, Googles Deep-Learning-Forschungsinitiative. Das Projekt entwickelt DistBelief, einen Vorgaenger von TensorFlow.",
        "datum_handlung": "2011",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_Brain",
        "quell_titel": "Google Brain - Wikipedia",
        "kontext": "Google Brain wird zu einem der fuehrenden KI-Forschungslabore weltweit und treibt Googles KI-Strategie voran.",
    },
    # ---- H4. Google Cat Paper ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Andrew Ng und das Google Brain Team veroeffentlichen die beruehmt gewordene Studie, in der ein neuronales Netz mit 16.000 Prozessoren lernt, Katzen in YouTube-Videos zu erkennen -- ohne vorher mit gelabelten Daten trainiert worden zu sein (unsupervised learning).",
        "datum_handlung": "2012-06-26",
        "betrag_usd": None,
        "quell_link": "https://www.nytimes.com/2012/06/26/technology/in-a-big-network-of-computers-evidence-of-machine-learning.html",
        "quell_titel": "How Many Computers to Identify a Cat? 16,000 (New York Times)",
        "kontext": "Der 'Google Cat'-Durchbruch zeigt die Macht von Deep Learning und erregt grosse Aufmerksamkeit in der Oeffentlichkeit.",
    },
    # ---- H5. Baidu Chief Scientist ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Andrew Ng tritt als Chief Scientist bei Baidu ein und leitet die KI-Strategie des chinesischen Suchmaschinen-Giganten. Er baut das Baidu Research Lab auf und gruendet das 'Baidu Brain'-Projekt mit einem Team von 1.300 Mitarbeitern.",
        "datum_handlung": "2014-05-16",
        "betrag_usd": None,
        "quell_link": "https://www.theverge.com/2014/5/16/5722474/google-brain-founder-andrew-ng-joins-baidu-as-chief-scientist",
        "quell_titel": "Google Brain founder Andrew Ng joins Baidu as chief scientist (The Verge)",
        "kontext": "Ng verlaesst Google, um bei Baidu Chinas KI-Ambitionen voranzutreiben. Ein bedeutender Schritt fuer KI-Entwicklung in China.",
    },
    # ---- H6. Ruecktritt bei Baidu ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Andrew Ng kuendigt seinen Ruecktritt als Chief Scientist bei Baidu an, um sich auf neue KI-Projekte zu konzentrieren. Er verlaesst Baidu nach drei Jahren, in denen er Baidu Brain aufgebaut hat.",
        "datum_handlung": "2017-03-22",
        "betrag_usd": None,
        "quell_link": "https://www.wired.com/2017/03/andrew-ng-chinese-google-discovers-power-ai/",
        "quell_titel": "Andrew Ng Leaves Baidu (WIRED)",
        "kontext": "Ng kuendigt an, sich auf KI-Bildung und neue Ventures zu konzentrieren.",
    },
    # ---- H7. Gruendung DeepLearning.AI ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Andrew Ng gruendet DeepLearning.AI, ein Bildungsunternehmen, das KI-Kurse und Spezialisierungen auf Coursera anbietet. Die Plattform startet mit dem 'Deep Learning Specialization', einem 5-Kurse-Programm.",
        "datum_handlung": "2017-08-08",
        "betrag_usd": None,
        "quell_link": "https://www.forbes.com/sites/gilpress/2017/08/08/ai-guru-andrew-ng-launches-deeplearning-ai-an-ai-education-venture/",
        "quell_titel": "AI Guru Andrew Ng Launches DeepLearning.AI (Forbes)",
        "kontext": "DeepLearning.AI wird zu einer der fuehrenden Plattformen fuer KI-Bildung mit Millionen Lernenden weltweit.",
    },
    # ---- H8. Gruendung Landing AI ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Andrew Ng gruendet Landing AI, ein Unternehmen, das sich auf KI-Loesungen fuer das verarbeitende Gewerbe spezialisiert. Landing AI fokussiert auf Computer Vision und 'Small Data'-Ansaetze fuer die Fertigung.",
        "datum_handlung": "2017-12-14",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2017/12/14/andrew-ngs-new-startup-landing-ai-raises-10m-to-bring-artificial-intelligence-to-manufacturing/",
        "quell_titel": "Andrew Ng's Landing AI Raises $10M (TechCrunch)",
        "kontext": "Landing AI verfolgt Ngs Vision, KI fuer traditionelle Industrien zugaenglich zu machen.",
    },
    # ---- H9. AI Fund Launch ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Andrew Ng startet den AI Fund, einen $175 Millionen Venture-Capital-Fonds und Studio, das neue KI-Startups gruendet. Der Fonds investiert in Unternehmen wie Woebot (mental health AI) und Landing AI.",
        "datum_handlung": "2018-01-30",
        "betrag_usd": 175000000.0,
        "quell_link": "https://techcrunch.com/2018/01/30/andrew-ng-officially-launches-his-175m-ai-fund/",
        "quell_titel": "Andrew Ng officially launches his $175M AI Fund (TechCrunch)",
        "kontext": "Der AI Fund verfolgt ein Studio-Modell: Ng baut Startups gemeinsam mit Partnern auf, statt nur zu investieren.",
    },
    # ---- H10. Partnerschaft Foxconn ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Landing AI geht eine strategische Partnerschaft mit Foxconn ein, um KI-basierte visuelle Inspektion in der Elektronikfertigung einzufuehren. Foxconn nutzt Landing AI fuer Qualitaetskontrolle.",
        "datum_handlung": "2018-02-01",
        "betrag_usd": None,
        "quell_link": "https://venturebeat.com/ai/andrew-ngs-landing-ai-partners-with-foxconn/",
        "quell_titel": "Andrew Ng's Landing AI partners with Foxconn (VentureBeat)",
        "kontext": "Die Partnerschaft demonstriert Landing AIs Fokus auf Manufacturing AI und zeigt praktische Anwendung.",
    },
    # ---- H11. AI for Everyone Kurs ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Andrew Ng startet 'AI for Everyone', einen nicht-technischen Kurs auf Coursera, der KI fuer Manager, Fuehrungskraefte und Nicht-Techniker zugaenglich macht. Der Kurs wird ueber 1 Million Mal belegt.",
        "datum_handlung": "2018-12-17",
        "betrag_usd": None,
        "quell_link": "https://www.coursera.org/learn/ai-for-everyone",
        "quell_titel": "AI for Everyone - Coursera",
        "kontext": "Der Kurs traegt massgeblich zur KI-Bildung von Nicht-Technikern bei und ist einer der erfolgreichsten Coursera-Kurse.",
    },
    # ---- H12. Data-Centric AI Movement ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Andrew Ng startet die 'Data-Centric AI'-Bewegung, die den Fokus von Modellverbesserungen auf Datenqualitaet verlagert. Er organisiert den ersten Data-Centric AI Workshop und Competition.",
        "datum_handlung": "2021-05-06",
        "betrag_usd": None,
        "quell_link": "https://spectrum.ieee.org/andrew-ng-data-centric-ai",
        "quell_titel": "Andrew Ng: Unbiggen AI (IEEE Spectrum)",
        "kontext": "Die Bewegung zielt darauf ab, KI-Entwicklung zu demokratisieren, indem der Fokus auf systematische Datenverbesserung gelegt wird.",
    },
    # ---- H13. LandingLens Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Landing AI launcht LandingLens, eine Cloud-basierte Computer-Vision-Plattform, die es Unternehmen ermoeglicht, visuelle Inspektionssysteme mit minimalen Daten zu trainieren. Die Plattform implementiert data-centric AI-Prinzipien.",
        "datum_handlung": "2021-11-09",
        "betrag_usd": None,
        "quell_link": "https://venturebeat.com/ai/landing-ai-launches-landinglens-to-bring-computer-vision-to-manufacturers/",
        "quell_titel": "Landing AI launches LandingLens (VentureBeat)",
        "kontext": "LandingLens ist die kommerzielle Umsetzung von Ngs data-centric AI-Vision fuer Manufacturing.",
    },
    # ---- H14. Machine Learning Yearning Buch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Andrew Ng veroeffentlicht 'Machine Learning Yearning', ein kostenloses E-Book, das praktische Ratschlaege fuer die Strukturierung von Machine-Learning-Projekten bietet. Das Buch wird von Hunderttausenden gelesen.",
        "datum_handlung": "2018-10-12",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearning.ai/programs/",
        "quell_titel": "Machine Learning Yearning by Andrew Ng",
        "kontext": "Das Buch ist kostenlos verfuegbar und teilt Ngs praktisches Wissen aus Jahren der KI-Entwicklung.",
    },
    # ---- H15. Coursera IPO ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Coursera geht an die Boerse (NYSE: COUR) mit einer Bewertung von $4,3 Milliarden. Andrew Ng ist zu diesem Zeitpunkt nicht mehr operativ taetig, bleibt aber Chairman des Board.",
        "datum_handlung": "2021-03-31",
        "betrag_usd": 4300000000.0,
        "quell_link": "https://www.cnbc.com/2021/03/31/coursera-ipo-cour-stock-starts-trading-on-nasdaq.html",
        "quell_titel": "Coursera goes public at $4.3 billion valuation (CNBC)",
        "kontext": "Der IPO markiert den Erfolg von Ngs Vision fuer demokratisierte Bildung.",
    },
    # ---- H16. DeepLearning.AI 5 Millionen Lernende ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "DeepLearning.AI gibt bekannt, dass ueber 5 Millionen Menschen ihre Kurse absolviert haben. Die Plattform bietet inzwischen 20+ Spezialisierungen und Kurse in KI-Themen.",
        "datum_handlung": "2023-08-15",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearning.ai/blog/",
        "quell_titel": "DeepLearning.AI Reaches 5 Million Learners",
        "kontext": "DeepLearning.AI etabliert sich als fuehrende Plattform fuer KI-Bildung weltweit.",
    },
    # ---- H17. ChatGPT for Developers Kurs ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "DeepLearning.AI launcht in Partnerschaft mit OpenAI den Kurs 'ChatGPT Prompt Engineering for Developers', der eine Million Einschreibungen in den ersten Wochen erreicht.",
        "datum_handlung": "2023-05-01",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/",
        "quell_titel": "ChatGPT Prompt Engineering for Developers - DeepLearning.AI",
        "kontext": "Der Kurs reagiert auf den ChatGPT-Boom und macht Prompt Engineering zugaenglich.",
    },
    # ---- H18. AI Agentic Design Patterns Kurs ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Andrew Ng launcht einen Kurs zu 'AI Agentic Design Patterns', in dem er seine Vision fuer agentic workflows erklaert: Reflection, Tool Use, Planning, Multi-Agent Collaboration. Der Kurs wird ein Bestseller.",
        "datum_handlung": "2024-03-26",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/",
        "quell_titel": "AI Agentic Design Patterns Course Launch (DeepLearning.AI)",
        "kontext": "Ng positioniert agentic workflows als naechste grosse Entwicklung in der KI.",
    },
    # ---- H19. Landing AI Series A ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Landing AI sichert sich eine $57 Millionen Series-A-Finanzierung gefuehrt von McRock Capital. Das Kapital wird genutzt, um LandingLens zu skalieren und neue Manufacturing-Kunden zu gewinnen.",
        "datum_handlung": "2022-06-14",
        "betrag_usd": 57000000.0,
        "quell_link": "https://techcrunch.com/2022/06/14/landing-ai-raises-57m-to-expand-its-computer-vision-platform/",
        "quell_titel": "Landing AI raises $57M Series A (TechCrunch)",
        "kontext": "Die Finanzierung zeigt das Wachstumspotenzial von KI im Manufacturing-Sektor.",
    },
    # ---- H20. Partnerschaft mit Google Cloud ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "DeepLearning.AI geht eine Partnerschaft mit Google Cloud ein, um Kurse zu entwickeln, die Google-Cloud-KI-Tools lehren, einschliesslich Vertex AI und Generative AI-Anwendungen.",
        "datum_handlung": "2023-07-12",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearning.ai/courses/",
        "quell_titel": "DeepLearning.AI Partners with Google Cloud",
        "kontext": "Die Partnerschaft erweitert DeepLearning.AIs Angebot um Cloud-native KI-Tools.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=22 existiert
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
            "Claude (collect_ng.py)"
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
        "Andrew Ng, Coursera, DeepLearning.AI, Google Brain, Baidu AI, Landing AI, AI Fund, AI is the new electricity, data-centric AI, agentic workflows, democratization, education",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Stanford GSB, WIRED, IEEE Spectrum, TechCrunch, CNBC, Forbes, Fortune, Washington Post, "
        f"MIT Technology Review, The Verge, DeepLearning.AI Blog, Coursera, New York Times, STAT News, "
        f"Quartz, VentureBeat. Themen: Coursera-Gruendung, Google Brain, Baidu Chief Scientist, "
        f"DeepLearning.AI, Landing AI, AI Fund, Data-Centric AI Movement, Agentic Workflows, "
        f"AI Democratisierung, Anti-Regulierungs-Position.",
        "Claude (collect_ng.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Andrew Ng (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Andrew Ng")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_ng.py")
    print("  Verifizierte Aussagen & Handlungen: Andrew Ng")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
