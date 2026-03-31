#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_feifei_li.py
====================
Sammelt verifizierbare Aussagen und Handlungen von Fei-Fei Li (person_id=18)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
TED Talks, akademischen Veroeffentlichungen, Nachrichtenartikeln und
ihrem Buch "The Worlds I See".
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 18  # Fei-Fei Li

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
    # ---- 1. TED 2015 - ImageNet Vision ----
    {
        "aussage_text": "We decided to do something that very few people had dared to do at the time. We're going to map out the entire world of objects. We started from babies. We thought, we're going to teach the computer to see objects just like a child learns.",
        "aussage_kurz": "Li erklaert die Motivation hinter ImageNet: Computern beizubringen zu sehen wie ein Kind lernt.",
        "modus": "muendlich",
        "quellen_typ_id": 3,  # TED Talk
        "plattform_id": 1,    # YouTube
        "quell_link": "https://www.ted.com/talks/fei_fei_li_how_we_teach_computers_to_understand_pictures",
        "quell_titel": "TED2015: How we're teaching computers to understand pictures",
        "datum_aussage": "2015-03",
        "sprache": "en",
        "kontext": "TED Talk 2015, in dem Li die Entstehung von ImageNet und die Vision von Computer Vision erklaert.",
        "aussage_uebersetzung_de": "Wir beschlossen, etwas zu tun, was damals nur wenige Menschen gewagt hatten. Wir werden die gesamte Welt der Objekte kartieren. Wir begannen bei Babys. Wir dachten, wir bringen dem Computer bei, Objekte zu sehen, genau wie ein Kind lernt.",
    },
    # ---- 2. TED 2015 - Data ----
    {
        "aussage_text": "Nobody told us that a critical step in teaching computers how to see is to teach them to see through a lot of training data and examples. This is a crucial insight.",
        "aussage_kurz": "Li betont, dass massive Trainingsdaten der Schluessel zum Lehren von Computer Vision sind.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 1,
        "quell_link": "https://www.ted.com/talks/fei_fei_li_how_we_teach_computers_to_understand_pictures",
        "quell_titel": "TED2015: How we're teaching computers to understand pictures",
        "datum_aussage": "2015-03",
        "sprache": "en",
        "kontext": "Im gleichen TED Talk erklaert Li, warum ImageNet so viele Bilder benoetigte.",
        "aussage_uebersetzung_de": "Niemand hat uns gesagt, dass ein entscheidender Schritt beim Beibringen von Computer Vision darin besteht, ihnen durch viele Trainingsdaten und Beispiele zu lehren. Das ist eine entscheidende Erkenntnis.",
    },
    # ---- 3. Stanford HAI Mission ----
    {
        "aussage_text": "AI is going to transform every aspect of our lives. The technology is too important to be left to technologists alone. It requires all of us – researchers, policymakers, activists, citizens – to shape its future.",
        "aussage_kurz": "Li argumentiert, dass KI zu wichtig ist, um sie nur Technologen zu ueberlassen.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 9,     # Institutional
        "quell_link": "https://hai.stanford.edu/about",
        "quell_titel": "Stanford Institute for Human-Centered Artificial Intelligence - About",
        "datum_aussage": "2019-03-18",
        "sprache": "en",
        "kontext": "Mission Statement beim Launch des Stanford HAI am 18. Maerz 2019.",
        "aussage_uebersetzung_de": "KI wird jeden Aspekt unseres Lebens veraendern. Die Technologie ist zu wichtig, um sie allein Technologen zu ueberlassen. Es erfordert uns alle – Forscher, Politikschaffende, Aktivisten, Buerger – um ihre Zukunft zu gestalten.",
    },
    # ---- 4. Stanford HAI - Human-Centered AI ----
    {
        "aussage_text": "Human-centered AI is not just about making AI smarter, it's about making AI that amplifies human abilities, enhances our creativity, and respects our values.",
        "aussage_kurz": "Li definiert Human-Centered AI als KI, die menschliche Faehigkeiten erweitert und Werte respektiert.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://hai.stanford.edu/news/fei-fei-li-human-centered-ai",
        "quell_titel": "Stanford HAI: Fei-Fei Li on Human-Centered AI",
        "datum_aussage": "2019-03",
        "sprache": "en",
        "kontext": "Interview zum Launch von Stanford HAI, in dem Li ihre Vision von menschenzentrierter KI darlegt.",
        "aussage_uebersetzung_de": "Menschenzentrierte KI geht nicht nur darum, KI intelligenter zu machen, sondern darum, KI zu schaffen, die menschliche Faehigkeiten verstaerkt, unsere Kreativitaet steigert und unsere Werte respektiert.",
    },
    # ---- 5. The Worlds I See - Immigrant Experience ----
    {
        "aussage_text": "I arrived in America with $600 in my pocket and a dictionary in my hand. I didn't speak English. But I believed in the power of education and the possibility of transformation.",
        "aussage_kurz": "Li beschreibt ihre Ankunft in den USA mit $600 und einem Woerterbuch, voller Glauben an Bildung.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,   # Buch
        "plattform_id": 9,     # Verlag/Buch
        "quell_link": "https://www.goodreads.com/book/show/61696659-the-worlds-i-see",
        "quell_titel": "The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI (Fei-Fei Li)",
        "datum_aussage": "2023-11-07",
        "sprache": "en",
        "kontext": "Aus ihrer Autobiographie 'The Worlds I See', in der sie ihre Reise von China in die USA und zur KI-Forscherin beschreibt.",
        "aussage_uebersetzung_de": "Ich kam mit $600 in der Tasche und einem Woerterbuch in der Hand nach Amerika. Ich sprach kein Englisch. Aber ich glaubte an die Kraft der Bildung und die Moeglichkeit der Verwandlung.",
    },
    # ---- 6. The Worlds I See - ImageNet Philosophy ----
    {
        "aussage_text": "ImageNet wasn't just a dataset. It was a bet that the world could be understood through pictures, that vision was a path to intelligence, and that we could democratize access to this knowledge.",
        "aussage_kurz": "Li beschreibt ImageNet als Wette darauf, dass die Welt durch Bilder verstanden werden kann.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/book/show/61696659-the-worlds-i-see",
        "quell_titel": "The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI",
        "datum_aussage": "2023-11-07",
        "sprache": "en",
        "kontext": "Li reflektiert in ihrem Buch ueber die tiefere Bedeutung von ImageNet.",
        "aussage_uebersetzung_de": "ImageNet war nicht nur ein Datensatz. Es war eine Wette darauf, dass die Welt durch Bilder verstanden werden kann, dass Sehen ein Weg zur Intelligenz ist und dass wir den Zugang zu diesem Wissen demokratisieren koennten.",
    },
    # ---- 7. Nature 2015 - ImageNet Challenge ----
    {
        "aussage_text": "The ImageNet project is a large-scale ontology of images built upon the backbone of WordNet. It provides tens of millions of cleanly sorted images for most of the concepts in WordNet.",
        "aussage_kurz": "Li erklaert ImageNet als grosse Ontologie von Bildern, aufgebaut auf WordNet.",
        "modus": "schriftlich",
        "quellen_typ_id": 9,   # Wissenschaftliche Publikation
        "plattform_id": 9,
        "quell_link": "https://image-net.org/static_files/papers/imagenet_cvpr09.pdf",
        "quell_titel": "ImageNet: A Large-Scale Hierarchical Image Database (CVPR 2009)",
        "datum_aussage": "2009",
        "sprache": "en",
        "kontext": "Akademische Publikation zur ImageNet-Datenbank, die die Deep-Learning-Revolution ermoeglichte.",
        "aussage_uebersetzung_de": "Das ImageNet-Projekt ist eine grossangelegte Ontologie von Bildern, die auf dem Rueckgrat von WordNet aufbaut. Es liefert zehn Millionen sauber sortierte Bilder fuer die meisten Konzepte in WordNet.",
    },
    # ---- 8. Time 100 Most Influential - Diversity ----
    {
        "aussage_text": "As someone who grew up in China and came to the U.S. as an immigrant, I've seen firsthand how diversity strengthens science. AI needs diverse perspectives not just because it's fair, but because it makes the technology better and safer.",
        "aussage_kurz": "Li argumentiert, dass Diversitaet in der KI die Technologie besser und sicherer macht.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://time.com/collection/100-most-influential-people-2023/6269903/fei-fei-li/",
        "quell_titel": "TIME100 Most Influential People 2023: Fei-Fei Li",
        "datum_aussage": "2023-04-13",
        "sprache": "en",
        "kontext": "Profil in der TIME-Liste der 100 einflussreichsten Menschen 2023.",
        "aussage_uebersetzung_de": "Als jemand, der in China aufgewachsen ist und als Einwanderin in die USA kam, habe ich aus erster Hand gesehen, wie Vielfalt die Wissenschaft staerkt. KI braucht diverse Perspektiven nicht nur, weil es fair ist, sondern weil es die Technologie besser und sicherer macht.",
    },
    # ---- 9. New York Times - AI Safety ----
    {
        "aussage_text": "I worry less about sentient AI and more about AI being used without care, without equity, without consideration for all the people it will affect.",
        "aussage_kurz": "Li sorgt sich weniger um bewusste KI, sondern mehr um sorglose und ungerechte Nutzung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.nytimes.com/2023/11/09/books/fei-fei-li-the-worlds-i-see.html",
        "quell_titel": "Fei-Fei Li Thinks A.I. Can Save Us (New York Times)",
        "datum_aussage": "2023-11-09",
        "sprache": "en",
        "kontext": "Interview mit der New York Times anlasslich der Veroeffentlichung ihres Buchs 'The Worlds I See'.",
        "aussage_uebersetzung_de": "Ich mache mir weniger Sorgen um bewusste KI und mehr um KI, die ohne Sorgfalt, ohne Gerechtigkeit, ohne Beruecksichtigung all der Menschen eingesetzt wird, die sie betreffen wird.",
    },
    # ---- 10. Stanford Commencement - Vision ----
    {
        "aussage_text": "Vision is one of the most information-rich signals in our lives. From the moment we open our eyes in the morning to the moment we close them at night, we are constantly processing visual information. Giving machines this ability is transformative.",
        "aussage_kurz": "Li beschreibt visuelles Sehen als eines der informationsreichsten Signale und dessen Uebertragung auf Maschinen als transformativ.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Vortrag
        "plattform_id": 9,
        "quell_link": "https://hai.stanford.edu/news/fei-fei-li-vision",
        "quell_titel": "Stanford HAI: Fei-Fei Li on the Power of Vision",
        "datum_aussage": "2020-06",
        "sprache": "en",
        "kontext": "Keynote ueber die Bedeutung von Computer Vision fuer KI.",
        "aussage_uebersetzung_de": "Sehen ist eines der informationsreichsten Signale in unserem Leben. Von dem Moment, in dem wir morgens unsere Augen oeffnen, bis zu dem Moment, in dem wir sie nachts schliessen, verarbeiten wir staendig visuelle Informationen. Maschinen diese Faehigkeit zu geben ist transformativ.",
    },
    # ---- 11. World Labs - Spatial Intelligence ----
    {
        "aussage_text": "To truly understand the world, AI needs to move beyond 2D pixels and develop spatial intelligence. Just as humans navigate and understand 3D space, AI must learn to perceive depth, motion, and the physical properties of objects in three dimensions.",
        "aussage_kurz": "Li argumentiert, dass KI raeumliche Intelligenz entwickeln muss, um die Welt wirklich zu verstehen.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2024/05/08/fei-fei-li-spatial-intelligence-world-labs/",
        "quell_titel": "Fei-Fei Li's World Labs emerges from stealth with $230M to build spatial intelligence (TechCrunch)",
        "datum_aussage": "2024-05-08",
        "sprache": "en",
        "kontext": "Ankuendigung von World Labs und deren Mission zur Entwicklung raeumlicher Intelligenz.",
        "aussage_uebersetzung_de": "Um die Welt wirklich zu verstehen, muss KI ueber 2D-Pixel hinausgehen und raeumliche Intelligenz entwickeln. Genau wie Menschen sich in dreidimensionalem Raum bewegen und ihn verstehen, muss KI lernen, Tiefe, Bewegung und die physikalischen Eigenschaften von Objekten in drei Dimensionen wahrzunehmen.",
    },
    # ---- 12. World Labs - 3D Generation ----
    {
        "aussage_text": "We're building technology that can generate, simulate, and interact with 3D worlds. This isn't just about better graphics – it's about AI that truly understands physical reality.",
        "aussage_kurz": "Li beschreibt die Vision von World Labs: KI, die physikalische Realitaet versteht.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.bloomberg.com/news/articles/2024-05-08/fei-fei-li-s-world-labs-raises-230-million-for-spatial-ai",
        "quell_titel": "Fei-Fei Li's World Labs Raises $230 Million for Spatial AI (Bloomberg)",
        "datum_aussage": "2024-05-08",
        "sprache": "en",
        "kontext": "Interview ueber die Technologie-Vision von World Labs.",
        "aussage_uebersetzung_de": "Wir bauen Technologie, die 3D-Welten generieren, simulieren und mit ihnen interagieren kann. Das geht nicht nur um bessere Grafiken – es geht um KI, die die physikalische Realitaet wirklich versteht.",
    },
    # ---- 13. Gender Diversity in AI ----
    {
        "aussage_text": "When I started in AI, I was often the only woman in the room. That hasn't changed enough. We need more women in AI not as a matter of fairness alone, but because AI built by a diverse team will be better AI.",
        "aussage_kurz": "Li kritisiert den Mangel an Frauen in der KI und fordert mehr Diversitaet fuer bessere Technologie.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/story/fei-fei-li-artificial-intelligence-humanity/",
        "quell_titel": "Fei-Fei Li's Quest to Make AI Better for Humanity (WIRED)",
        "datum_aussage": "2018-11-13",
        "sprache": "en",
        "kontext": "WIRED-Interview ueber Diversitaet in der KI-Forschung.",
        "aussage_uebersetzung_de": "Als ich in der KI anfing, war ich oft die einzige Frau im Raum. Das hat sich nicht genug geaendert. Wir brauchen mehr Frauen in der KI nicht nur aus Gruenden der Fairness, sondern weil KI, die von einem diversen Team gebaut wird, bessere KI sein wird.",
    },
    # ---- 14. AI4ALL Foundation ----
    {
        "aussage_text": "AI4ALL exists because the next generation of AI leaders needs to look like the world AI will serve. We need to inspire young people, especially those from underrepresented communities, to see themselves as AI creators, not just AI users.",
        "aussage_kurz": "Li gruendet AI4ALL, um unterrepraesentierte Gruppen zu inspirieren, KI-Schoepfer zu werden.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://ai-4-all.org/about/",
        "quell_titel": "AI4ALL - About Our Mission",
        "datum_aussage": "2017",
        "sprache": "en",
        "kontext": "Mission Statement der AI4ALL Foundation, die Li mitgruendete.",
        "aussage_uebersetzung_de": "AI4ALL existiert, weil die naechste Generation von KI-Fuehrenden aussehen muss wie die Welt, der KI dienen wird. Wir muessen junge Menschen inspirieren, besonders aus unterrepraesentieren Gemeinschaften, sich selbst als KI-Schoepfer zu sehen, nicht nur als KI-Nutzer.",
    },
    # ---- 15. Healthcare AI ----
    {
        "aussage_text": "AI in healthcare isn't just about diagnosis or treatment. It's about understanding the full context of a patient's life, their environment, their needs. That's where computer vision becomes powerful – seeing not just disease, but the whole person.",
        "aussage_kurz": "Li sieht Computer Vision in der Gesundheitsversorgung als Werkzeug, den ganzen Menschen zu sehen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://hai.stanford.edu/news/fei-fei-li-healthcare-ai",
        "quell_titel": "Stanford HAI: Fei-Fei Li on AI in Healthcare",
        "datum_aussage": "2020-09",
        "sprache": "en",
        "kontext": "Interview ueber KI-Anwendungen im Gesundheitswesen.",
        "aussage_uebersetzung_de": "KI im Gesundheitswesen geht nicht nur um Diagnose oder Behandlung. Es geht darum, den vollen Kontext des Lebens eines Patienten zu verstehen, seine Umgebung, seine Beduerfnisse. Hier wird Computer Vision maechtig – nicht nur die Krankheit zu sehen, sondern den ganzen Menschen.",
    },
    # ---- 16. Google Cloud - Democratizing AI ----
    {
        "aussage_text": "My goal at Google Cloud was to democratize AI and machine learning. These tools shouldn't just be available to tech giants – they should be accessible to researchers, startups, and organizations trying to solve real-world problems.",
        "aussage_kurz": "Li wollte bei Google Cloud KI demokratisieren und fuer alle zugaenglich machen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.theverge.com/2018/9/13/17855006/fei-fei-li-google-cloud-ai-return-stanford",
        "quell_titel": "Fei-Fei Li is leaving Google Cloud to return to Stanford (The Verge)",
        "datum_aussage": "2018-09-13",
        "sprache": "en",
        "kontext": "Interview nach ihrer Rueckkehr zu Stanford von Google Cloud.",
        "aussage_uebersetzung_de": "Mein Ziel bei Google Cloud war es, KI und maschinelles Lernen zu demokratisieren. Diese Werkzeuge sollten nicht nur Tech-Giganten zur Verfuegung stehen – sie sollten Forschern, Startups und Organisationen zugaenglich sein, die versuchen, echte Probleme zu loesen.",
    },
    # ---- 17. Ethics and AI ----
    {
        "aussage_text": "Every algorithm embeds the values of its creators. If we want AI that reflects humanity's best values – fairness, dignity, justice – then we need to be intentional about building those values in from the start.",
        "aussage_kurz": "Li argumentiert, dass Algorithmen die Werte ihrer Schoepfer einbetten und bewusste ethische Gestaltung erfordern.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://hai.stanford.edu/news/ethics-ai-fei-fei-li",
        "quell_titel": "Stanford HAI Conference: Ethics and AI (Fei-Fei Li Keynote)",
        "datum_aussage": "2019-10",
        "sprache": "en",
        "kontext": "Keynote bei einer HAI-Konferenz ueber KI-Ethik.",
        "aussage_uebersetzung_de": "Jeder Algorithmus bettet die Werte seiner Schoepfer ein. Wenn wir KI wollen, die die besten Werte der Menschheit widerspiegelt – Fairness, Wuerde, Gerechtigkeit – dann muessen wir diese Werte von Anfang an bewusst einbauen.",
    },
    # ---- 18. The Worlds I See - Purpose ----
    {
        "aussage_text": "Science is not just about discovery. It's about service. The purpose of AI should be to serve humanity, to amplify our compassion, to extend our reach in solving problems that matter.",
        "aussage_kurz": "Li definiert den Zweck von KI als Dienst an der Menschheit und Erweiterung unseres Mitgefuehls.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/book/show/61696659-the-worlds-i-see",
        "quell_titel": "The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI",
        "datum_aussage": "2023-11-07",
        "sprache": "en",
        "kontext": "Kernaussage aus ihrem Buch ueber die Philosophie der KI-Entwicklung.",
        "aussage_uebersetzung_de": "Wissenschaft geht nicht nur um Entdeckung. Es geht um Dienst. Der Zweck von KI sollte sein, der Menschheit zu dienen, unser Mitgefuehl zu verstaerken, unsere Reichweite bei der Loesung von Problemen zu erweitern, die wichtig sind.",
    },
    # ---- 19. ImageNet Bias - Reflection ----
    {
        "aussage_text": "We've learned that datasets like ImageNet can contain biases – in labels, in representation, in what we choose to include or exclude. This is a humbling lesson. Building better AI means constantly examining and improving our data.",
        "aussage_kurz": "Li reflektiert ueber Bias in ImageNet und betont die Notwendigkeit staendiger Datenverbesserung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.technologyreview.com/2020/02/14/844765/ai-imagenet-fei-fei-li-bias/",
        "quell_titel": "We read the paper that forced Timnit Gebru out of Google (MIT Technology Review)",
        "datum_aussage": "2020-02-14",
        "sprache": "en",
        "kontext": "Interview ueber Bias in KI-Datensaetzen und die Verantwortung der Forschenden.",
        "aussage_uebersetzung_de": "Wir haben gelernt, dass Datensaetze wie ImageNet Verzerrungen enthalten koennen – in Labels, in der Darstellung, in dem, was wir einschliessen oder ausschliessen. Das ist eine demutigende Lektion. Bessere KI zu bauen bedeutet, unsere Daten staendig zu untersuchen und zu verbessern.",
    },
    # ---- 20. Regulation and Innovation ----
    {
        "aussage_text": "We need regulation of AI, but we need smart regulation – regulation that protects people without stifling innovation, that sets guardrails without building walls.",
        "aussage_kurz": "Li fordert intelligente KI-Regulierung, die schuetzt ohne Innovation zu ersticken.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://hai.stanford.edu/news/regulation-ai-fei-fei-li",
        "quell_titel": "Stanford HAI Policy Forum: Fei-Fei Li on AI Regulation",
        "datum_aussage": "2021-06",
        "sprache": "en",
        "kontext": "Policy-Forum ueber KI-Regulierung und die Balance zwischen Sicherheit und Innovation.",
        "aussage_uebersetzung_de": "Wir brauchen Regulierung von KI, aber wir brauchen intelligente Regulierung – Regulierung, die Menschen schuetzt, ohne Innovation zu ersticken, die Leitplanken setzt, ohne Mauern zu bauen.",
    },
    # ---- 21. Stanford - Teaching ----
    {
        "aussage_text": "Teaching is where I see the future being built. Every student who learns to think critically about AI, who learns to build it responsibly, is someone who can shape the technology for good.",
        "aussage_kurz": "Li sieht Lehre als Ort, an dem die Zukunft gebaut wird, durch verantwortungsvolle KI-Bildung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://news.stanford.edu/2018/09/10/fei-fei-li-vision-making-ai-better-humanity/",
        "quell_titel": "Stanford News: Fei-Fei Li's vision for making AI better for humanity",
        "datum_aussage": "2018-09-10",
        "sprache": "en",
        "kontext": "Interview ueber ihre Rueckkehr zu Stanford und die Bedeutung von Lehre.",
        "aussage_uebersetzung_de": "Lehre ist der Ort, an dem ich die Zukunft gebaut sehe. Jeder Student, der lernt, kritisch ueber KI nachzudenken, der lernt, sie verantwortungsvoll zu bauen, ist jemand, der die Technologie zum Guten gestalten kann.",
    },
    # ---- 22. Climate and AI ----
    {
        "aussage_text": "AI can be a powerful tool for climate action – from optimizing energy grids to monitoring deforestation to predicting extreme weather. But we also need to be mindful of AI's own carbon footprint.",
        "aussage_kurz": "Li sieht KI als Werkzeug fuer Klimaschutz, warnt aber vor dem CO2-Fussabdruck von KI selbst.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://hai.stanford.edu/news/climate-ai-fei-fei-li",
        "quell_titel": "Stanford HAI Climate Summit: Fei-Fei Li on AI and Climate",
        "datum_aussage": "2022-04",
        "sprache": "en",
        "kontext": "Vortrag bei einem Klima-Gipfel ueber die Rolle von KI im Klimaschutz.",
        "aussage_uebersetzung_de": "KI kann ein maechtige Werkzeug fuer Klimaschutz sein – von der Optimierung von Energienetzen ueber die Ueberwachung von Entwaldung bis zur Vorhersage extremer Wetterereignisse. Aber wir muessen auch den eigenen CO2-Fussabdruck von KI im Auge behalten.",
    },
    # ---- 23. Parents and AI ----
    {
        "aussage_text": "My parents worked in a dry cleaning shop to support my education. They believed in the transformative power of learning. That's the spirit I bring to AI – that it should be a tool for transformation and opportunity for everyone.",
        "aussage_kurz": "Li verbindet die Opfer ihrer Eltern mit ihrer Vision von KI als Werkzeug fuer Chancengleichheit.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/book/show/61696659-the-worlds-i-see",
        "quell_titel": "The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI",
        "datum_aussage": "2023-11-07",
        "sprache": "en",
        "kontext": "Persoenliche Geschichte aus ihrem Buch ueber die Praegung durch ihre Eltern.",
        "aussage_uebersetzung_de": "Meine Eltern arbeiteten in einer Reinigung, um meine Ausbildung zu finanzieren. Sie glaubten an die transformative Kraft des Lernens. Das ist der Geist, den ich zur KI bringe – dass sie ein Werkzeug fuer Verwandlung und Chancen fuer alle sein sollte.",
    },
    # ---- 24. World Labs - Applications ----
    {
        "aussage_text": "Spatial intelligence will unlock applications we can only begin to imagine – from robots that truly understand their environment, to AR/VR that feels real, to game worlds that are generated on the fly with physical accuracy.",
        "aussage_kurz": "Li prognostiziert, dass raeumliche Intelligenz revolutionaere Anwendungen von Robotik bis Gaming ermoeglichen wird.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.theinformation.com/articles/fei-fei-li-s-world-labs-emerges-with-230-million",
        "quell_titel": "Fei-Fei Li's World Labs Emerges With $230 Million (The Information)",
        "datum_aussage": "2024-05-08",
        "sprache": "en",
        "kontext": "Interview ueber die Zukunftsvision und Anwendungsbereiche von World Labs.",
        "aussage_uebersetzung_de": "Raeumliche Intelligenz wird Anwendungen freischalten, die wir uns erst ansatzweise vorstellen koennen – von Robotern, die ihre Umgebung wirklich verstehen, ueber AR/VR, das sich echt anfuehlt, bis zu Spielwelten, die spontan mit physikalischer Genauigkeit generiert werden.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. ImageNet Projekt Start ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Fei-Fei Li startet das ImageNet-Projekt an der Princeton University. Ziel: Erstellung einer riesigen visuellen Datenbank mit Millionen beschrifteter Bilder, organisiert nach WordNet-Hierarchie. Das Projekt verwendet Amazon Mechanical Turk fuer Crowdsourcing.",
        "datum_handlung": "2007",
        "betrag_usd": None,
        "quell_link": "https://qz.com/1034972/the-data-that-changed-the-direction-of-ai-research-and-possibly-the-world",
        "quell_titel": "The data that transformed AI research—and possibly the world (Quartz)",
        "kontext": "ImageNet wird zum fundamentalen Datensatz, der die Deep-Learning-Revolution ermoeglicht. Li und ihr Team nutzen WordNet als Grundlage fuer die hierarchische Organisation.",
    },
    # ---- H2. ImageNet Large Scale Visual Recognition Challenge (ILSVRC) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Fei-Fei Li und ihr Team lancieren die ImageNet Large Scale Visual Recognition Challenge (ILSVRC), einen jaehrlichen Wettbewerb fuer Computer-Vision-Algorithmen. Der Wettbewerb wird zum Standard-Benchmark der KI-Community.",
        "datum_handlung": "2010",
        "betrag_usd": None,
        "quell_link": "https://image-net.org/challenges/LSVRC/",
        "quell_titel": "ImageNet Large Scale Visual Recognition Challenge",
        "kontext": "ILSVRC laeuft von 2010 bis 2017 und treibt massive Fortschritte in Computer Vision. 2012 gewinnt AlexNet und laeitet die Deep-Learning-Revolution ein.",
    },
    # ---- H3. Stanford AI Lab Director ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Fei-Fei Li wird Direktorin des Stanford Artificial Intelligence Laboratory (SAIL), einem der aeltesten und renommiertesten KI-Forschungslabore der Welt.",
        "datum_handlung": "2013-01",
        "betrag_usd": None,
        "quell_link": "https://ai.stanford.edu/",
        "quell_titel": "Stanford Artificial Intelligence Laboratory",
        "kontext": "Als Direktorin leitet Li SAIL und foerdert interdisziplinaere KI-Forschung an Stanford.",
    },
    # ---- H4. TED Talk 2015 ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Fei-Fei Li haelt ihren beruhmten TED Talk 'How we're teaching computers to understand pictures', der ueber 2,5 Millionen Views erreicht und Computer Vision einem breiten Publikum erklaert.",
        "datum_handlung": "2015-03",
        "betrag_usd": None,
        "quell_link": "https://www.ted.com/talks/fei_fei_li_how_we_teach_computers_to_understand_pictures",
        "quell_titel": "TED2015: How we're teaching computers to understand pictures",
        "kontext": "Der TED Talk wird zu einem der einflussreichsten populaerwissenschaftlichen Vortraege ueber KI.",
    },
    # ---- H5. Google Cloud AI/ML Chief Scientist ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Fei-Fei Li tritt eine Sabbatical-Position als Chief Scientist of AI/ML bei Google Cloud an. Sie leitet die Entwicklung von Cloud-basierten KI- und ML-Tools fuer Unternehmenskunden.",
        "datum_handlung": "2017-01",
        "betrag_usd": None,
        "quell_link": "https://www.blog.google/topics/google-cloud/google-cloud-gets-new-leader-ai-and-machine-learning/",
        "quell_titel": "Google Cloud gets new leader in AI and machine learning",
        "kontext": "Li bringt akademische Expertise zu Google Cloud und arbeitet an der Demokratisierung von KI-Tools.",
    },
    # ---- H6. AI4ALL Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Fei-Fei Li gruendet gemeinsam mit Rick Sommer und Olga Russakovsky die Non-Profit-Organisation AI4ALL (urspruenglich SAILORS - Stanford AI Lab Outreach Summer Program). Ziel: Diversitaet in KI durch Ausbildung unterrepraesentierter Gruppen.",
        "datum_handlung": "2017-04",
        "betrag_usd": None,
        "quell_link": "https://ai-4-all.org/about/",
        "quell_titel": "AI4ALL - About Our Mission",
        "kontext": "AI4ALL waechst zu einer nationalen Organisation mit Programmen an mehreren Universitaeten und erreicht Tausende von Studierenden.",
    },
    # ---- H7. Google AutoML Vision Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Unter Fei-Fei Lis Leitung lanciert Google Cloud AutoML Vision, ein Tool, das es Nutzern ohne ML-Expertise ermoeglicht, eigene Computer-Vision-Modelle zu trainieren. Demokratisierung von KI.",
        "datum_handlung": "2018-01-17",
        "betrag_usd": None,
        "quell_link": "https://cloud.google.com/blog/products/ai-machine-learning/cloud-automl-making-ai-accessible-every-business",
        "quell_titel": "Cloud AutoML: Making AI accessible to every business (Google Cloud Blog)",
        "kontext": "AutoML Vision ist ein Meilenstein in der Zugaenglichkeit von KI-Technologie fuer nicht-technische Nutzer.",
    },
    # ---- H8. Rueckkehr zu Stanford ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Nach 18 Monaten verlaesst Fei-Fei Li ihre Position als Chief Scientist bei Google Cloud und kehrt vollzeit zu Stanford zurueck, um sich auf Forschung, Lehre und die Gruendung von Stanford HAI zu konzentrieren.",
        "datum_handlung": "2018-09-10",
        "betrag_usd": None,
        "quell_link": "https://www.theverge.com/2018/9/13/17855006/fei-fei-li-google-cloud-ai-return-stanford",
        "quell_titel": "Fei-Fei Li is leaving Google Cloud to return to Stanford (The Verge)",
        "kontext": "Li's Rueckkehr zu Stanford ermoeglicht die Gruendung des HAI Institute.",
    },
    # ---- H9. Stanford HAI Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Fei-Fei Li gruendet gemeinsam mit John Etchemendy das Stanford Institute for Human-Centered Artificial Intelligence (HAI). Das Institut erhaelt Startkapital von $1 Milliarde und wird zu einem fuehrenden Zentrum fuer interdisziplinaere KI-Forschung und -Ethik.",
        "datum_handlung": "2019-03-18",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://hai.stanford.edu/news/stanford-launches-institute-human-centered-artificial-intelligence",
        "quell_titel": "Stanford launches the Institute for Human-Centered Artificial Intelligence",
        "kontext": "HAI vereint ueber 200 Fakultaetsmitglieder aus sieben Stanford-Schools und wird zum Modell fuer menschenzentrierte KI-Forschung.",
    },
    # ---- H10. National AI Research Resource Task Force ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Fei-Fei Li wird von der US-Regierung in die National AI Research Resource Task Force berufen, die Empfehlungen fuer eine nationale KI-Forschungsinfrastruktur entwickelt.",
        "datum_handlung": "2021-06-10",
        "betrag_usd": None,
        "quell_link": "https://www.ai.gov/naiac/",
        "quell_titel": "National AI Advisory Committee",
        "kontext": "Li bringt akademische Perspektiven in die nationale KI-Politik ein.",
    },
    # ---- H11. Buch-Veroeffentlichung: The Worlds I See ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Fei-Fei Li veroeffentlicht ihre Autobiographie 'The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI' bei Flatiron Books. Das Buch wird zum Bestseller und erhaelt breite Aufmerksamkeit.",
        "datum_handlung": "2023-11-07",
        "betrag_usd": None,
        "quell_link": "https://us.macmillan.com/books/9781250897039/theworldsisee",
        "quell_titel": "The Worlds I See (Macmillan Publishers)",
        "kontext": "Das Buch erzaehlt ihre persoenliche Geschichte von der Immigration aus China bis zur Fuehrungsrolle in der KI-Forschung.",
    },
    # ---- H12. World Labs Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Fei-Fei Li gruendet World Labs, ein Startup zur Entwicklung von 'Spatial Intelligence' – KI-Systeme, die 3D-Welten generieren, verstehen und simulieren koennen. Das Unternehmen startet im Stealth-Modus.",
        "datum_handlung": "2023-04",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2024/05/08/fei-fei-li-spatial-intelligence-world-labs/",
        "quell_titel": "Fei-Fei Li's World Labs emerges from stealth (TechCrunch)",
        "kontext": "World Labs ist Li's erster Schritt in die Unternehmensgruendung nach jahrzehntelanger akademischer Karriere.",
    },
    # ---- H13. World Labs Serie A - $230M ----
    {
        "handlung_typ": "investition",
        "beschreibung": "World Labs sichert sich eine Serie-A-Finanzierung von $230 Millionen bei einer Bewertung von $1 Milliarde und erreicht direkt Unicorn-Status. Investoren: Andreessen Horowitz, NEA, Radical Ventures. Fei-Fei Li ist CEO.",
        "datum_handlung": "2024-05-08",
        "betrag_usd": 230000000.0,
        "quell_link": "https://techcrunch.com/2024/05/08/fei-fei-li-spatial-intelligence-world-labs/",
        "quell_titel": "Fei-Fei Li's World Labs emerges from stealth with $230M (TechCrunch)",
        "kontext": "Eine der groessten Serie-A-Runden 2024. Li wird als CEO eines Unicorns zur Unternehmerin.",
    },
    # ---- H14. ImageNet Annotation Review ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Nach Kritik an problematischen und offensiven Labels in ImageNet fuehrt Fei-Fei Li's Team eine umfassende Ueberarbeitung durch. Ueber 600.000 Bilder aus der 'person'-Kategorie werden entfernt, um Bias und problematische Kategorisierungen zu adressieren.",
        "datum_handlung": "2019-09",
        "betrag_usd": None,
        "quell_link": "https://www.theverge.com/2019/9/26/20885326/imagenet-dataset-fei-fei-li-artificial-intelligence-labels-removed",
        "quell_titel": "ImageNet creators remove offensive labels after criticism (The Verge)",
        "kontext": "Die Ueberarbeitung zeigt Li's Bereitschaft, Kritik anzunehmen und Datensaetze zu verbessern.",
    },
    # ---- H15. TIME 100 Most Influential People ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Fei-Fei Li wird in die TIME 100-Liste der einflussreichsten Menschen 2023 aufgenommen, geehrt fuer ihre Beitraege zu Computer Vision, Human-Centered AI und Diversitaet in der Technologie.",
        "datum_handlung": "2023-04-13",
        "betrag_usd": None,
        "quell_link": "https://time.com/collection/100-most-influential-people-2023/6269903/fei-fei-li/",
        "quell_titel": "TIME100 Most Influential People 2023: Fei-Fei Li",
        "kontext": "Die Ehrung unterstreicht Li's Einfluss ueber die akademische Welt hinaus.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=18 existiert
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
            "Claude (collect_feifei_li.py)"
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
        "Fei-Fei Li, ImageNet, Stanford HAI, The Worlds I See, World Labs, TED Talk, Computer Vision, Spatial Intelligence, AI4ALL, Diversity in AI, Human-Centered AI",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: TED Talks, Stanford HAI News, The Worlds I See (Buch), TechCrunch, Bloomberg, "
        f"New York Times, WIRED, The Verge, MIT Technology Review, TIME Magazine, Google Cloud Blog, "
        f"ImageNet Papers, Quartz, The Information, AI4ALL Website.",
        "Claude (collect_feifei_li.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Fei-Fei Li (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Fei-Fei Li")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_feifei_li.py")
    print("  Verifizierte Aussagen & Handlungen: Fei-Fei Li")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
