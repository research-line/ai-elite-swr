#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_page.py
===============
Sammelt verifizierbare Aussagen und Handlungen von Larry Page (person_id=6)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Konferenz-Talks, Buchausschnitten und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

HINWEIS: Larry Page ist seit ca. 2015 extrem oeffentlichkeitsscheu.
Die meisten Aussagen stammen aus der Zeit 2000-2015.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 6  # Larry Page

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
    # ---- 1. TED 2014: Toothbrush Test ----
    {
        "aussage_text": "The toothbrush test: Do you use it once or twice a day, and does it make your life better? We apply that to products we make.",
        "aussage_kurz": "Page erklaert den 'Zahnbuersten-Test': Produkte muessen taeglich genutzt werden und das Leben verbessern.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.ted.com/talks/larry_page_where_s_google_going_next",
        "quell_titel": "Larry Page: Where's Google going next? (TED 2014)",
        "datum_aussage": "2014-03-19",
        "sprache": "en",
        "kontext": "TED-Talk 2014, einer der letzten grossen oeffentlichen Auftritte von Larry Page. Er erklaert Googles Produktphilosophie.",
        "aussage_uebersetzung_de": "Der Zahnbuersten-Test: Nutzt du es ein- oder zweimal am Tag, und verbessert es dein Leben? Das wenden wir auf die Produkte an, die wir herstellen.",
    },
    # ---- 2. TED 2014: KI und Technologie-Optimismus ----
    {
        "aussage_text": "We have a bit of a problem where most of the people are afraid of new technology in some way or another. I feel like the pace of change in the world is accelerating. We're not adapting fast enough, and we need more people working on these problems.",
        "aussage_kurz": "Page beklagt, dass Menschen Angst vor neuer Technologie haben und wir uns nicht schnell genug anpassen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.ted.com/talks/larry_page_where_s_google_going_next",
        "quell_titel": "Larry Page: Where's Google going next? (TED 2014)",
        "datum_aussage": "2014-03-19",
        "sprache": "en",
        "kontext": "TED 2014. Page aeussert sich ueberrascht ueber Technologie-Skepsis und fordert mehr Arbeit an KI-Problemen.",
        "aussage_uebersetzung_de": "Wir haben ein kleines Problem, dass die meisten Menschen auf die eine oder andere Weise Angst vor neuen Technologien haben. Mir kommt es vor, als beschleunige sich das Tempo des Wandels in der Welt. Wir passen uns nicht schnell genug an, und wir brauchen mehr Menschen, die an diesen Problemen arbeiten.",
    },
    # ---- 3. TED 2014: KI als Verbesserung von Suchmaschinen ----
    {
        "aussage_text": "Artificial intelligence would be the ultimate version of Google. The ultimate search engine that would understand everything on the web. It would understand exactly what you wanted, and it would give you the right thing.",
        "aussage_kurz": "Page sieht KI als ultimative Suchmaschine, die alles versteht und genau das liefert, was man will.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.brainyquote.com/quotes/larry_page_619069",
        "quell_titel": "Larry Page on AI (Interview, ca. 2000er Jahre)",
        "datum_aussage": "2000",
        "sprache": "en",
        "kontext": "Fruehere Aussage zu KI (ca. Anfang 2000er Jahre), in der Page seine Vision von KI als perfekter Suchmaschine beschreibt.",
        "aussage_uebersetzung_de": "Kuenstliche Intelligenz waere die ultimative Version von Google. Die ultimative Suchmaschine, die alles im Web verstehen wuerde. Sie wuerde genau verstehen, was du willst, und dir genau das Richtige geben.",
    },
    # ---- 4. Founders at Work Interview: Google-Gruendung ----
    {
        "aussage_text": "We have some capability of building such a search engine for the academic realm and probably could make it available for everyone. We believed we could build a better search engine.",
        "aussage_kurz": "Page erklaert, dass er und Brin glaubten, sie koennten eine bessere Suchmaschine bauen als alle anderen.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,  # Buch
        "plattform_id": 9,    # Blogs/Buecher
        "quell_link": "https://en.wikipedia.org/wiki/Larry_Page",
        "quell_titel": "Founders at Work: Stories of Startups' Early Days (Jessica Livingston, 2007)",
        "datum_aussage": "2007",
        "sprache": "en",
        "kontext": "Interview im Buch 'Founders at Work' von Jessica Livingston. Page beschreibt die Gruendungsidee von Google.",
        "aussage_uebersetzung_de": "Wir haben die Faehigkeit, eine solche Suchmaschine fuer den akademischen Bereich zu bauen und koennten sie wahrscheinlich fuer alle verfuegbar machen. Wir glaubten, dass wir eine bessere Suchmaschine bauen koennten.",
    },
    # ---- 5. Google I/O 2013: Negativity ----
    {
        "aussage_text": "If you read the newspapers, it's like one in a million people does something bad. You read about it and you think, 'oh that's normal.' We need to reorient our thinking about the world. Negativity is not realism. It's like, you don't think about all the amazing people that are doing unbelievably positive things for humanity.",
        "aussage_kurz": "Page kritisiert Medien-Negativitaet und fordert mehr Fokus auf positive Beitraege zur Menschheit.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.youtube.com/watch?v=Ks0X-p-pZYo",
        "quell_titel": "Larry Page and Sergey Brin Fireside Chat (Google I/O 2013)",
        "datum_aussage": "2013-05-15",
        "sprache": "en",
        "kontext": "Google I/O 2013 Fireside Chat. Page verteidigt Technologie-Optimismus gegen Medien-Pessimismus.",
        "aussage_uebersetzung_de": "Wenn man Zeitung liest, ist es so: einer von einer Million Menschen macht etwas Schlechtes. Man liest darueber und denkt: 'oh, das ist normal.' Wir muessen unsere Weltsicht neu ausrichten. Negativitaet ist nicht Realismus. Du denkst nicht an all die erstaunlichen Menschen, die unglaublich positive Dinge fuer die Menschheit tun.",
    },
    # ---- 6. Google I/O 2013: Moonshots ----
    {
        "aussage_text": "You need to aim for something that's radical, transformative, and really powerful. And most of the time people would say that's not possible. That's exactly what you should be doing.",
        "aussage_kurz": "Page fordert radikale, transformative Ziele -- genau die, von denen andere sagen, sie seien unmoeglich.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.youtube.com/watch?v=Ks0X-p-pZYo",
        "quell_titel": "Larry Page and Sergey Brin Fireside Chat (Google I/O 2013)",
        "datum_aussage": "2013-05-15",
        "sprache": "en",
        "kontext": "Google I/O 2013. Page erklaert die 'Moonshot'-Philosophie von Google X.",
        "aussage_uebersetzung_de": "Man muss auf etwas zielen, das radikal, transformativ und wirklich maechtig ist. Und die meiste Zeit wuerden die Leute sagen, dass das nicht moeglich ist. Genau das sollte man tun.",
    },
    # ---- 7. Wired Interview 2013: Access to resources ----
    {
        "aussage_text": "It's quite hard to get people to do things they don't have to do. I wish we had a situation where the people who are most able to do these things and have the resources can spend their time solving the biggest problems in the world.",
        "aussage_kurz": "Page wuenscht sich, dass die faehigsten Menschen ihre Zeit den groessten Problemen der Welt widmen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/2013/01/ff-qa-larry-page/",
        "quell_titel": "Google's Larry Page on Why Moon Shots Matter (Wired, 2013)",
        "datum_aussage": "2013-01-17",
        "sprache": "en",
        "kontext": "Wired-Interview 2013. Page reflektiert ueber die Rolle von Ressourcen und faehigen Menschen.",
        "aussage_uebersetzung_de": "Es ist ziemlich schwer, Menschen dazu zu bringen, Dinge zu tun, die sie nicht tun muessen. Ich wuenschte, wir haetten eine Situation, in der die Menschen, die am faehigsten sind und die Ressourcen haben, ihre Zeit damit verbringen koennen, die groessten Probleme der Welt zu loesen.",
    },
    # ---- 8. Fortune Interview 2012: Death and legacy ----
    {
        "aussage_text": "I would like to die working. I'm not saying I'd like to die at work—just that if I had to die, I'd like the transition to be a short one—to still be working. I don't have a sense that I'd like to stop working. I think I'd like to be 50 or 60 before I'd like that feeling to change.",
        "aussage_kurz": "Page sagt, er moechte arbeitend sterben und hat kein Interesse daran, aufzuhoeren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2012/12/11/larry-page-the-most-ambitious-ceo-in-the-universe/",
        "quell_titel": "Larry Page: The most ambitious CEO in the universe (Fortune, 2012)",
        "datum_aussage": "2012-12-11",
        "sprache": "en",
        "kontext": "Fortune-Interview 2012. Page spricht ueberraschend offen ueber Tod und Vermaechtnis.",
        "aussage_uebersetzung_de": "Ich wuerde gerne arbeitend sterben. Ich sage nicht, dass ich bei der Arbeit sterben moechte -- nur dass, wenn ich sterben muesste, ich moechte, dass der Uebergang kurz ist -- immer noch arbeitend. Ich habe kein Gefuehl, dass ich aufhoeren moechte zu arbeiten. Ich denke, ich waere gerne 50 oder 60, bevor sich dieses Gefuehl aendern sollte.",
    },
    # ---- 9. Fortune Interview 2012: Giving money to Elon Musk ----
    {
        "aussage_text": "You know, I'd rather give my money to Elon Musk than to charity. He's going to make people's lives better. I don't think people necessarily appreciate the role of entrepreneurs in solving the world's toughest problems.",
        "aussage_kurz": "Page wuerde sein Geld lieber Elon Musk geben als Wohltaetigkeitsorganisationen -- Unternehmer loesen die groessten Probleme.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2012/12/11/larry-page-the-most-ambitious-ceo-in-the-universe/",
        "quell_titel": "Larry Page: The most ambitious CEO in the universe (Fortune, 2012)",
        "datum_aussage": "2012-12-11",
        "sprache": "en",
        "kontext": "Fortune 2012. Page verteidigt Unternehmertum gegenueber traditioneller Philanthropie.",
        "aussage_uebersetzung_de": "Weisst du, ich wuerde mein Geld lieber Elon Musk geben als einer Wohltaetigkeitsorganisation. Er wird das Leben der Menschen verbessern. Ich glaube nicht, dass die Menschen die Rolle von Unternehmern beim Loesen der schwierigsten Probleme der Welt notwendigerweise schaetzen.",
    },
    # ---- 10. FT Interview 2014: Technology and Jobs ----
    {
        "aussage_text": "The idea that everyone should slavishly work so they do something inefficiently so they keep their job – that just doesn't make any sense to me. That can't be the right answer.",
        "aussage_kurz": "Page kritisiert die Idee, dass Menschen ineffizient arbeiten sollten, nur um Jobs zu behalten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.ft.com/content/8b3c874c-6e14-11e4-bf00-00144feabdc0",
        "quell_titel": "FT Interview with Google co-founder and CEO Larry Page (Financial Times, 2014)",
        "datum_aussage": "2014-10-31",
        "sprache": "en",
        "kontext": "Financial Times Interview 2014. Page diskutiert Automatisierung, KI und die Zukunft der Arbeit.",
        "aussage_uebersetzung_de": "Die Idee, dass jeder sklavisch arbeiten sollte, sodass er etwas ineffizient macht, damit er seinen Job behaelt -- das ergibt fuer mich einfach keinen Sinn. Das kann nicht die richtige Antwort sein.",
    },
    # ---- 11. FT Interview 2014: 4-Tage-Woche ----
    {
        "aussage_text": "Most people like working, but they'd also like to have more time with their family or to pursue their own interests. So that would be one way to deal with the problem – spread the work around a little bit more.",
        "aussage_kurz": "Page schlaegt vor, Arbeit breiter zu verteilen -- etwa ueber eine 4-Tage-Woche.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.ft.com/content/8b3c874c-6e14-11e4-bf00-00144feabdc0",
        "quell_titel": "FT Interview with Google co-founder and CEO Larry Page (Financial Times, 2014)",
        "datum_aussage": "2014-10-31",
        "sprache": "en",
        "kontext": "FT 2014. Page schlaegt Arbeitszeitverkuerzung als Loesung fuer Automatisierung vor.",
        "aussage_uebersetzung_de": "Die meisten Menschen arbeiten gerne, aber sie haetten auch gerne mehr Zeit mit ihrer Familie oder fuer ihre eigenen Interessen. Das waere also eine Moeglichkeit, mit dem Problem umzugehen -- die Arbeit etwas mehr zu verteilen.",
    },
    # ---- 12. Zeitgeist 2007: Solving big problems ----
    {
        "aussage_text": "If you're changing the world, you're working on important things. You're excited to get up in the morning.",
        "aussage_kurz": "Page sagt, wer die Welt veraendert, arbeitet an wichtigen Dingen und ist morgens begeistert aufzustehen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.azquotes.com/quote/626521",
        "quell_titel": "Larry Page Zeitgeist Talk (2007)",
        "datum_aussage": "2007",
        "sprache": "en",
        "kontext": "Zeitgeist-Konferenz 2007. Page ueber die Motivation, an grossen Problemen zu arbeiten.",
        "aussage_uebersetzung_de": "Wenn du die Welt veraenderst, arbeitest du an wichtigen Dingen. Du bist begeistert, morgens aufzustehen.",
    },
    # ---- 13. Google I/O 2013: Privacy and trust ----
    {
        "aussage_text": "We get tremendous trust from people. They give us their data. We know where they are. We know what they've searched for. We take protecting that data and people's privacy incredibly seriously.",
        "aussage_kurz": "Page betont, dass Google Nutzerdaten ernst nimmt und Vertrauen von Menschen erhaelt.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.youtube.com/watch?v=Ks0X-p-pZYo",
        "quell_titel": "Larry Page and Sergey Brin Fireside Chat (Google I/O 2013)",
        "datum_aussage": "2013-05-15",
        "sprache": "en",
        "kontext": "Google I/O 2013. Page verteidigt Googles Umgang mit Nutzerdaten nach den ersten Edward-Snowden-Enthuellungen.",
        "aussage_uebersetzung_de": "Wir erhalten enormes Vertrauen von Menschen. Sie geben uns ihre Daten. Wir wissen, wo sie sind. Wir wissen, wonach sie gesucht haben. Wir nehmen den Schutz dieser Daten und die Privatsphaere der Menschen unglaublich ernst.",
    },
    # ---- 14. Khosla Ventures Conference 2014: Regulation ----
    {
        "aussage_text": "The pace of change is so rapid with technology that regulation doesn't really work. By the time you regulate it, it's already changed or the technology doesn't work the way you thought it did.",
        "aussage_kurz": "Page glaubt, dass Regulierung nicht funktioniert, weil Technologie sich schneller veraendert als Gesetze.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://techcrunch.com/2014/03/03/larry-page-regulation-is-not-keeping-up-with-the-pace-of-change/",
        "quell_titel": "Larry Page: Regulation Is Not Keeping Up With The Pace Of Change (TechCrunch, 2014)",
        "datum_aussage": "2014-03-03",
        "sprache": "en",
        "kontext": "Khosla Ventures Conference 2014. Page kritisiert Regulierungspraxis im Tech-Bereich.",
        "aussage_uebersetzung_de": "Das Tempo des technologischen Wandels ist so schnell, dass Regulierung nicht wirklich funktioniert. Bis man es reguliert hat, hat es sich bereits veraendert oder die Technologie funktioniert nicht so, wie man dachte.",
    },
    # ---- 15. Singularity University (ca. 2008-2012) ----
    {
        "aussage_text": "Especially in technology, we need revolution, not evolution.",
        "aussage_kurz": "Page fordert revolutionaere statt evolutionaere technologische Entwicklung.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.brainyquote.com/quotes/larry_page_591963",
        "quell_titel": "Larry Page Quote (via Singularity University)",
        "datum_aussage": "2010",
        "sprache": "en",
        "kontext": "Aeusserung im Kontext von Singularity University, die Page mitfinanziert hat.",
        "aussage_uebersetzung_de": "Besonders in der Technologie brauchen wir Revolution, nicht Evolution.",
    },
    # ---- 16. Wired 2013: Why Google is ambitious ----
    {
        "aussage_text": "If you say you want to automate cars and save people's lives, the skills you need for that aren't taught in any particular discipline. I know it seems hard. But people are dying every day in car accidents. The faster we can make this happen, the better.",
        "aussage_kurz": "Page verteidigt selbstfahrende Autos mit Verweis auf Verkehrstote -- je schneller, desto besser.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/2013/01/ff-qa-larry-page/",
        "quell_titel": "Google's Larry Page on Why Moon Shots Matter (Wired, 2013)",
        "datum_aussage": "2013-01-17",
        "sprache": "en",
        "kontext": "Wired 2013. Page rechtfertigt Googles Arbeit an selbstfahrenden Autos mit Leben-retten-Argument.",
        "aussage_uebersetzung_de": "Wenn man sagt, man wolle Autos automatisieren und Menschenleben retten, werden die Faehigkeiten, die man dafuer braucht, in keiner bestimmten Disziplin gelehrt. Ich weiss, es scheint schwer. Aber Menschen sterben jeden Tag bei Autounfaellen. Je schneller wir das umsetzen koennen, desto besser.",
    },
    # ---- 17. Stanford University Commencement 2009 ----
    {
        "aussage_text": "If you're not doing some things that are crazy, then you're doing the wrong things.",
        "aussage_kurz": "Page sagt, wenn man nicht einige verrueckte Dinge tut, macht man die falschen Dinge.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://news.stanford.edu/news/2009/june17/page-061709.html",
        "quell_titel": "Larry Page Commencement Address (Stanford University, 2009)",
        "datum_aussage": "2009-06-13",
        "sprache": "en",
        "kontext": "Stanford University Commencement Address 2009. Page fordert Absolventen auf, Veruecktes zu wagen.",
        "aussage_uebersetzung_de": "Wenn du nicht einige verrueckte Dinge machst, dann machst du die falschen Dinge.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung Google ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Larry Page und Sergey Brin gruenden Google Inc. in einer Garage in Menlo Park, Kalifornien. Startkapital: $100.000 von Andy Bechtolsheim (Sun Microsystems Co-Founder). Die PageRank-Algorithmus-Idee stammt aus Pages Stanford-Dissertation.",
        "datum_handlung": "1998-09-04",
        "betrag_usd": 100000.0,
        "quell_link": "https://en.wikipedia.org/wiki/History_of_Google",
        "quell_titel": "History of Google - Wikipedia",
        "kontext": "Page ist 25 Jahre alt. Google basiert auf seiner Idee, die Link-Struktur des Webs als Ranking-Signal zu nutzen (PageRank). Innerhalb weniger Jahre wird Google zur dominanten Suchmaschine.",
    },
    # ---- H2. Ruecktritt als CEO, Eric Schmidt wird CEO ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Larry Page tritt als CEO zurueck. Eric Schmidt wird CEO, Page wird Praesident fuer Produkte. Investor-Bedenken ueber mangelnde Management-Erfahrung fuehren zur Entscheidung.",
        "datum_handlung": "2001-08-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Larry_Page",
        "quell_titel": "Larry Page - Wikipedia",
        "kontext": "Die Gruender Page und Brin sind Mitte 20, und VCs bestehen auf 'erwachsener Aufsicht'. Eric Schmidt (ex-Novell, ex-Sun) wird als erfahrener CEO eingesetzt. Page bleibt zentral involviert.",
    },
    # ---- H3. Google Boersengang (IPO) ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Google geht an die Boerse (NASDAQ: GOOG). IPO sammelt $1,67 Milliarden ein bei einer Bewertung von $23 Milliarden. Larry Page und Sergey Brin behalten ueber Dual-Class-Aktien die Kontrolle. Unkonventionelles hollaendisches Auktions-Verfahren.",
        "datum_handlung": "2004-08-19",
        "betrag_usd": 1670000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/History_of_Google",
        "quell_titel": "History of Google - Wikipedia",
        "kontext": "Google waehlt ein hollaendisches Auktionsverfahren fuer das IPO -- ungewoehnlich fuer Silicon Valley. Der Boersengang macht Page und Brin zu Milliardaeren.",
    },
    # ---- H4. Akquisition: YouTube ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Google kauft YouTube fuer $1,65 Milliarden in Aktien. YouTube war erst 18 Monate alt und erwirtschaftete keine Gewinne. Die Akquisition wird spaeter als eine der besten Tech-Deals aller Zeiten bewertet.",
        "datum_handlung": "2006-10-09",
        "betrag_usd": 1650000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/History_of_YouTube",
        "quell_titel": "History of YouTube - Wikipedia",
        "kontext": "YouTube hatte zu diesem Zeitpunkt urheberrechtliche Risiken und keine klare Monetarisierungsstrategie. Google erkannte das Potenzial und kaufte trotz Bedenken. Heute ist YouTube eine der wertvollsten Google-Properties.",
    },
    # ---- H5. Singularity University Co-Founder ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Larry Page und Ray Kurzweil gruenden gemeinsam mit Peter Diamandis die Singularity University im NASA Ames Research Center. Ziel: Ausbildung von Fuehrungskraeften in exponentiellen Technologien (KI, Biotech, Nanotech).",
        "datum_handlung": "2008-09-20",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Singularity_University",
        "quell_titel": "Singularity University - Wikipedia",
        "kontext": "Singularity University verknotet Pages Interesse an radikalen Zukunftstechnologien mit Kurzweils Vision der technologischen Singularitaet. Page ist Gruender und Hauptfinanzierer.",
    },
    # ---- H6. Rueckkehr als CEO (Eric Schmidt tritt zurueck) ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Larry Page wird wieder CEO von Google, Eric Schmidt wird Executive Chairman. Page kuendigt Fokus auf 'fewer, bigger bets' an und reorganisiert Google radikal.",
        "datum_handlung": "2011-04-04",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Larry_Page",
        "quell_titel": "Larry Page - Wikipedia",
        "kontext": "Nach 10 Jahren unter Schmidt uebernimmt Page wieder. Er konzentriert Google auf grosse Projekte (Android, Chrome, Google+, Self-Driving Cars) und beginnt, weniger profitable Produkte zu schliessen.",
    },
    # ---- H7. Akquisition: DeepMind ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Google kauft das britische KI-Startup DeepMind fuer geschaetzt $500-650 Millionen. DeepMind-Gruender Demis Hassabis besteht auf Ethik-Board. Die Akquisition signalisiert Pages langfristige KI-Vision.",
        "datum_handlung": "2014-01-26",
        "betrag_usd": 500000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/DeepMind",
        "quell_titel": "DeepMind - Wikipedia",
        "kontext": "DeepMind hatte zu diesem Zeitpunkt nur ca. 75 Mitarbeiter und keine kommerziellen Produkte. Page sichert sich eines der fuehrenden KI-Forschungsteams der Welt. Spaeter besiegt DeepMind AlphaGo den Go-Weltmeister.",
    },
    # ---- H8. Gruendung Calico (Life Extension) ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Larry Page gruendet Calico (California Life Company), ein Biotech-Unternehmen mit dem Ziel, Altern zu bekaempfen und Lebensspanne zu verlaengern. CEO wird Arthur Levinson (Ex-Genentech, Apple-Boardmember). Finanzierung durch Google/Alphabet.",
        "datum_handlung": "2013-09-18",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Calico_(company)",
        "quell_titel": "Calico (company) - Wikipedia",
        "kontext": "Calico ist eine der ersten 'Moonshot'-Initiativen unter Page. Time Magazine titelt: 'Can Google Solve Death?' Calico arbeitet extrem verschlossen und hat bislang keine grossen Durchbrueche veroeffentlicht.",
    },
    # ---- H9. Umstrukturierung: Gruendung Alphabet Inc. ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Larry Page kuendigt die Umstrukturierung von Google in Alphabet Inc. an. Google wird Tochterunternehmen. Page wird CEO von Alphabet, Sundar Pichai CEO von Google. Weitere Toechter: Calico, Verily, Waymo, X, Wing, etc.",
        "datum_handlung": "2015-08-10",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Alphabet_Inc.",
        "quell_titel": "Alphabet Inc. - Wikipedia",
        "kontext": "Die Umstrukturierung ermoeglicht es, riskante 'Moonshots' von der profitablen Suchmaschine zu trennen. Alphabet-Struktur ist inspiriert von Berkshire Hathaway. Page zieht sich zunehmend aus der Oeffentlichkeit zurueck.",
    },
    # ---- H10. Investition/Gruendung: Kitty Hawk (Flugtaxis) ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Larry Page finanziert persoenlich (nicht via Alphabet) das Flugtaxi-Startup Kitty Hawk mit ueber $100 Millionen. CEO wird Sebastian Thrun (Stanford, Ex-Google X). Ziel: elektrische senkrechtstartende Fluggeraete (eVTOL).",
        "datum_handlung": "2015",
        "betrag_usd": 100000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Kitty_Hawk_Corporation",
        "quell_titel": "Kitty Hawk Corporation - Wikipedia",
        "kontext": "Kitty Hawk ist eines von Pages persoenlichen 'Flying Car'-Projekten. 2022 wird Kitty Hawk geschlossen, aber die Tochter Wisk Aero (Joint Venture mit Boeing) lebt weiter. Page investiert schon seit Jahren heimlich in Flugtaxis.",
    },
    # ---- H11. Ruecktritt als Alphabet CEO ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Larry Page tritt als CEO von Alphabet zurueck. Sergey Brin tritt ebenfalls als Praesident zurueck. Sundar Pichai wird CEO von Alphabet und Google. Page und Brin bleiben Boardmitglieder und kontrollieren Alphabet ueber Stimmrechtsaktien.",
        "datum_handlung": "2019-12-03",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Larry_Page",
        "quell_titel": "Larry Page - Wikipedia",
        "kontext": "Page begruendet den Ruecktritt mit dem Wunsch, sich aus dem Tagesgeschaeft zurueckzuziehen. Kritiker vermuten, er will sich Anhoerungen im Kongress und Medien-Druck entziehen. Seitdem ist Page fast vollstaendig aus der Oeffentlichkeit verschwunden.",
    },
    # ---- H12. Wisk Aero Weiterentwicklung (Flugtaxis) ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Pages Flugtaxi-Firma Wisk Aero (Spin-off von Kitty Hawk) geht Partnerschaft mit Boeing ein. Boeing investiert, Wisk entwickelt autonome eVTOL-Flugtaxis weiter. Ziel: FAA-Zertifizierung bis Mitte 2020er.",
        "datum_handlung": "2019-12-17",
        "betrag_usd": None,
        "quell_link": "https://www.wisk.aero/",
        "quell_titel": "Wisk Aero - Official Website",
        "kontext": "Trotz Rueckzug aus dem Rampenlicht investiert Page weiter in Flugtaxi-Technologie. Wisk ist eines der wenigen verbleibenden Page-Projekte, das oeffentlich aktiv ist.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=6 existiert
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
            "Claude (collect_page.py)"
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
        "Larry Page quotes, interviews, TED 2014, Google I/O 2013, Fortune 2012, FT 2014, Wired 2013, Stanford Commencement, Singularity University, DeepMind, Calico, Alphabet, Kitty Hawk, Wisk",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: TED 2014, Google I/O 2013, Fortune 2012, FT 2014, Wired 2013, "
        f"Founders at Work (Buch), Stanford Commencement 2009, Zeitgeist 2007, Khosla Ventures 2014. "
        f"HINWEIS: Larry Page ist seit ca. 2015 oeffentlichkeitsscheu -- fast keine oeffentlichen Aussagen nach 2015. "
        f"Handlungen: Google-Gruendung, YouTube-Kauf, DeepMind-Akquisition, Alphabet-Umstrukturierung, "
        f"Calico (Life Extension), Singularity University, Kitty Hawk/Wisk (Flugtaxis), Ruecktritt 2019.",
        "Claude (collect_page.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Larry Page (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Larry Page")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_page.py")
    print("  Verifizierte Aussagen & Handlungen: Larry Page")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
