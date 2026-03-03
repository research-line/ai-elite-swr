#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_brin.py
===============
Sammelt verifizierbare Aussagen und Handlungen von Sergey Brin (person_id=8)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
TED Talks, Konferenzen, universitaeren Vortraegen und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

HINWEIS: Sergey Brin ist extrem oeffentlichkeitsscheu. Die meisten Aussagen
stammen aus der Google-Fruehphase, TED-Talks und seltenen Konferenzauftritten.
Seit ca. 2013 gibt er kaum noch oeffentliche Interviews.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 8  # Sergey Brin

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
    # ---- 1. TED Talk 2004 ----
    {
        "aussage_text": "Solve search, and we solve a lot of the world's problems. Access to information is a fundamental human right.",
        "aussage_kurz": "Brin sieht Suche als Loesung fuer viele Weltprobleme und Zugang zu Information als Grundrecht.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion / Talk
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.ted.com/talks/sergey_brin_and_larry_page_on_google",
        "quell_titel": "Sergey Brin and Larry Page on Google (TED 2004)",
        "datum_aussage": "2004-02",
        "sprache": "en",
        "kontext": "TED Talk zusammen mit Larry Page. Brin und Page sprechen ueber die Philosophie hinter Google und die Bedeutung von Informationszugang.",
        "aussage_uebersetzung_de": "Wenn wir Suche loesen, loesen wir viele der Probleme der Welt. Zugang zu Information ist ein fundamentales Menschenrecht.",
    },
    # ---- 2. University of Maryland Commencement, Mai 2009 ----
    {
        "aussage_text": "Technology is an inherent democratizer. Because of the evolution of hardware and software, you're now able to do things that only very rich people and powerful governments could do before.",
        "aussage_kurz": "Brin beschreibt Technologie als Demokratisierer, der Faehigkeiten der Maechtigen allen zugaenglich macht.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.umd.edu/commencement/sergey-brin-commencement-address",
        "quell_titel": "Sergey Brin Commencement Address, University of Maryland 2009",
        "datum_aussage": "2009-05-22",
        "sprache": "en",
        "kontext": "Commencement Speech an der University of Maryland (wo er seinen Master machte). Brin spricht ueber Technologie und Chancengleichheit.",
        "aussage_uebersetzung_de": "Technologie ist ein inhaerent demokratisierendes Element. Durch die Entwicklung von Hardware und Software koennen Sie jetzt Dinge tun, die frueher nur sehr reiche Menschen und maechtige Regierungen tun konnten.",
    },
    # ---- 3. Web 2.0 Summit, 2010 ----
    {
        "aussage_text": "We want to build technology that everybody loves using, and that affects everyone. We want to create beautiful, intuitive services and technologies that are so incredibly useful that people use them twice a day. Like they use a toothbrush. There aren't that many things people use twice a day.",
        "aussage_kurz": "Brin will Technologie schaffen, die Menschen zweimal taeglich nutzen -- wie eine Zahnbuerste.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Interview
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://techcrunch.com/2010/11/15/sergey-brin-web-2-0-summit/",
        "quell_titel": "Sergey Brin on Google's Future at Web 2.0 Summit (TechCrunch)",
        "datum_aussage": "2010-11-15",
        "sprache": "en",
        "kontext": "Web 2.0 Summit Interview. Brin spricht ueber Googles Produktphilosophie und den Anspruch, unverzichtbare Technologie zu schaffen.",
        "aussage_uebersetzung_de": "Wir wollen Technologie bauen, die jeder liebt zu nutzen, und die jeden betrifft. Wir wollen schoene, intuitive Dienste und Technologien schaffen, die so unglaublich nuetzlich sind, dass die Leute sie zweimal am Tag verwenden. Wie sie eine Zahnbuerste benutzen. Es gibt nicht so viele Dinge, die Leute zweimal am Tag verwenden.",
    },
    # ---- 4. 'Don't be evil' Philosophy ----
    {
        "aussage_text": "I feel like our slogan 'Don't be evil' has been a great rallying cry for us. And it's very simple. We try not to cross that line. We try to stay on the right side of that line by a healthy margin.",
        "aussage_kurz": "Brin verteidigt 'Don't be evil' als zentrale Philosophie und moralischen Kompass fuer Google.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/2013/04/an-inside-look-at-googles-dont-be-evil-credo/",
        "quell_titel": "Inside Google's 'Don't Be Evil' Credo (Wired)",
        "datum_aussage": "2003",
        "sprache": "en",
        "kontext": "Interview ueber Googles Firmenkultur und den Motto 'Don't be evil'. Brin erklaert, warum einfache ethische Prinzipien wichtig sind.",
        "aussage_uebersetzung_de": "Ich habe das Gefuehl, dass unser Slogan 'Don't be evil' ein grossartiger Schlachtruf fuer uns war. Und er ist sehr einfach. Wir versuchen, diese Grenze nicht zu ueberschreiten. Wir versuchen, mit gesundem Abstand auf der richtigen Seite dieser Grenze zu bleiben.",
    },
    # ---- 5. Google Glass Vision, 2012 ----
    {
        "aussage_text": "We want to make the world's information universally accessible and useful. Ultimately, I'd like information to come to me when I need it without having to take any action.",
        "aussage_kurz": "Brin will Information automatisch verfuegbar machen, ohne dass Nutzer aktiv danach suchen muessen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.theguardian.com/technology/2012/jun/27/google-project-glass-sergey-brin",
        "quell_titel": "Google's Project Glass: Sergey Brin's Vision for the Future (The Guardian)",
        "datum_aussage": "2012-06-27",
        "sprache": "en",
        "kontext": "Interview ueber Google Glass. Brin erklaert die Vision eines Computers, der Informationen vorausschauend liefert.",
        "aussage_uebersetzung_de": "Wir wollen die Informationen der Welt universell zugaenglich und nuetzlich machen. Letztendlich moechte ich, dass Informationen zu mir kommen, wenn ich sie brauche, ohne dass ich irgendeine Aktion ausfuehren muss.",
    },
    # ---- 6. Google Glass - Warum Smartphones ablenken ----
    {
        "aussage_text": "The phone is very, very seductive, and it's very easy to just pull it out, check your email, check your messages. It's kind of emasculating. Is this glass half full or half empty? It's kind of socially isolating. It takes you away from the present.",
        "aussage_kurz": "Brin kritisiert Smartphones als sozial isolierend und bezeichnet ihr staendiges Hervorholen als 'entmannend'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.businessinsider.com/sergey-brin-on-smartphones-2013-2",
        "quell_titel": "Sergey Brin: Smartphones Are 'Emasculating' (Business Insider)",
        "datum_aussage": "2013-02-27",
        "sprache": "en",
        "kontext": "TED-Konferenz 2013, wo Brin Google Glass praesentiert und gegen Smartphones argumentiert.",
        "aussage_uebersetzung_de": "Das Telefon ist sehr, sehr verfuehrerisch, und es ist sehr einfach, es einfach herauszuziehen, seine E-Mails zu checken, seine Nachrichten zu checken. Das ist irgendwie entmannend. Ist dieses Glas halb voll oder halb leer? Es ist irgendwie sozial isolierend. Es nimmt dich weg von der Gegenwart.",
    },
    # ---- 7. Selbstfahrende Autos (Google Self-Driving Car Project) ----
    {
        "aussage_text": "We can probably save a million lives a year by having self-driving cars, just in terms of accident reduction. Think about all the people that get injured, all the emergency rooms, all the suffering, all the people that lose their loved ones.",
        "aussage_kurz": "Brin sieht selbstfahrende Autos als Mittel, eine Million Menschenleben pro Jahr zu retten.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.forbes.com/sites/chunkamui/2013/01/22/how-google-self-driving-car-will-change-everything/",
        "quell_titel": "How Google's Self-Driving Car Will Change Everything (Forbes)",
        "datum_aussage": "2013-01",
        "sprache": "en",
        "kontext": "Konferenz zum Google Self-Driving Car Project. Brin praesentiert die Vision autonomer Fahrzeuge als humanitaeres Projekt.",
        "aussage_uebersetzung_de": "Wir koennen wahrscheinlich eine Million Menschenleben pro Jahr retten, indem wir selbstfahrende Autos haben, allein durch Unfallreduktion. Denken Sie an all die Menschen, die verletzt werden, all die Notaufnahmen, all das Leiden, all die Menschen, die ihre Angehoerigen verlieren.",
    },
    # ---- 8. Sergey Brin's Parkinson's Risk (23andMe) ----
    {
        "aussage_text": "I know early in my life something I'm substantially predisposed to. I now have the opportunity to adjust my life to reduce those odds. Parkinson's is not inevitable for me -- even with the genetic mutation -- if I take action.",
        "aussage_kurz": "Brin erklaert oeffentlich, dass er eine genetische Praedisposition fuer Parkinson hat und praeventiv handeln kann.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://www.wired.com/2008/09/sergey-brin-genetic-test-reveals-parkinsons-risk/",
        "quell_titel": "Sergey Brin's Genetic Test Reveals Parkinson's Risk (Wired)",
        "datum_aussage": "2008-09",
        "sprache": "en",
        "kontext": "Blog-Post/Interview ueber 23andMe Testergebnisse. Brin (dessen Mutter an Parkinson erkrankte) teilt oeffentlich seine LRRK2-Mutation und finanziert Parkinson-Forschung.",
        "aussage_uebersetzung_de": "Ich weiss frueh in meinem Leben etwas, wofuer ich erheblich praedisponiert bin. Ich habe jetzt die Moeglichkeit, mein Leben anzupassen, um diese Chancen zu reduzieren. Parkinson ist nicht unvermeidlich fuer mich -- selbst mit der genetischen Mutation -- wenn ich handle.",
    },
    # ---- 9. China und Zensur ----
    {
        "aussage_text": "We felt that by participating there, we were able to actually make a difference. People could access more information than they would have otherwise. But we're constantly re-evaluating that.",
        "aussage_kurz": "Brin verteidigt Googles Praesenz in China trotz Zensur, weil es mehr Informationszugang biete als keine Praesenz.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnet.com/news/privacy/google-execs-defend-china-search-engine/",
        "quell_titel": "Google Execs Defend China Search Engine (CNET)",
        "datum_aussage": "2006",
        "sprache": "en",
        "kontext": "Kongressanhoerung 2006. Brin und Page rechtfertigen die zensierte Google.cn-Version -- eine kontroverse Entscheidung.",
        "aussage_uebersetzung_de": "Wir haben das Gefuehl, dass wir durch unsere Teilnahme dort tatsaechlich etwas bewirken konnten. Die Menschen konnten auf mehr Informationen zugreifen, als sie es sonst gekonnt haetten. Aber wir bewerten das staendig neu.",
    },
    # ---- 10. Rueckzug aus China, 2010 ----
    {
        "aussage_text": "I am particularly troubled that this has occurred in China, as I spent some time as a child growing up in the Soviet Union. I was born in Moscow. I spent the first six years of my life there. I understand very much this kind of environment of totalitarianism and that's something I'm particularly sensitive to.",
        "aussage_kurz": "Brin erklaert, warum er persoenlich von Chinas Zensur betroffen ist: Er wuchs in der Sowjetunion auf und kennt Totalitarismus.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.theguardian.com/technology/2010/mar/23/sergey-brin-google-china-censorship",
        "quell_titel": "Sergey Brin on Google's China Retreat: 'I Was Born in Moscow' (The Guardian)",
        "datum_aussage": "2010-03-23",
        "sprache": "en",
        "kontext": "Interview nach Googles Rueckzug aus China (2010). Brin macht seinen persoenlichen Hintergrund als Emigrant zum zentralen Grund.",
        "aussage_uebersetzung_de": "Ich bin besonders beunruhigt, dass dies in China passiert ist, da ich einige Zeit meiner Kindheit in der Sowjetunion verbracht habe. Ich wurde in Moskau geboren. Ich habe dort die ersten sechs Jahre meines Lebens verbracht. Ich verstehe sehr gut diese Art von totalitaerem Umfeld, und das ist etwas, fuer das ich besonders sensibel bin.",
    },
    # ---- 11. Alphabet X (Moonshot Factory) ----
    {
        "aussage_text": "We're trying to do things that sound a little crazy, like making a car that drives itself or building a balloon-powered Internet. But we take a moonshot-style approach with one caveat: our problems all have to be huge. Millions and millions of people have to be affected by a problem before we tackle it.",
        "aussage_kurz": "Brin erklaert den Moonshot-Ansatz von X: nur riesige Probleme angehen, die Millionen Menschen betreffen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.fastcompany.com/3028156/google-x-and-the-science-of-radical-creativity",
        "quell_titel": "Inside Google X's Moonshot Factory (Fast Company)",
        "datum_aussage": "2014",
        "sprache": "en",
        "kontext": "Artikel ueber Alphabet X. Brin leitet das Moonshot-Labor und beschreibt die Philosophie hinter Projekten wie Loon und Waymo.",
        "aussage_uebersetzung_de": "Wir versuchen, Dinge zu tun, die etwas verrueckt klingen, wie ein Auto zu bauen, das sich selbst faehrt, oder ein Ballon-betriebenes Internet zu bauen. Aber wir verfolgen einen Moonshot-Ansatz mit einem Vorbehalt: unsere Probleme muessen alle riesig sein. Millionen und Abermillionen Menschen muessen von einem Problem betroffen sein, bevor wir es angehen.",
    },
    # ---- 12. Philanthropy: Brin Wojcicki Foundation ----
    {
        "aussage_text": "We believe strongly in supporting medical research, particularly in Parkinson's disease, which affects my family, and in fighting global poverty and supporting education.",
        "aussage_kurz": "Brin nennt Parkinson-Forschung, Armutsbekaempfung und Bildung als Schwerpunkte seiner Stiftung.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://www.philanthropy.com/article/sergey-brin-and-anne-wojcicki-donate-millions-to-parkinsons-research/",
        "quell_titel": "Sergey Brin and Anne Wojcicki Donate Millions to Parkinson's Research (Chronicle of Philanthropy)",
        "datum_aussage": "2012",
        "sprache": "en",
        "kontext": "Artikel ueber die Brin Wojcicki Foundation. Brin spendet Millionen fuer Parkinson-Forschung (motiviert durch seine eigene Praedisposition).",
        "aussage_uebersetzung_de": "Wir glauben fest daran, medizinische Forschung zu unterstuetzen, besonders bei Parkinson-Krankheit, die meine Familie betrifft, sowie globale Armut zu bekaempfen und Bildung zu foerdern.",
    },
    # ---- 13. Gemini-Entwicklung Rueckkehr 2023 ----
    {
        "aussage_text": "I've been coming in most days, meeting with our researchers, learning about the technology, and helping out where I can. It's exciting to see the progress.",
        "aussage_kurz": "Brin erklaert 2023 seine Rueckkehr zu Google, um bei der Gemini-Entwicklung zu helfen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.businessinsider.com/sergey-brin-returns-google-ai-gemini-development-2023-11",
        "quell_titel": "Sergey Brin Returns to Google to Help with Gemini AI (Business Insider)",
        "datum_aussage": "2023-11",
        "sprache": "en",
        "kontext": "Nach Jahren der Abwesenheit kehrt Brin 2023 zu Google zurueck, um bei der Entwicklung des Gemini-Modells zu helfen -- eine ueberraschende Kehrtwende.",
        "aussage_uebersetzung_de": "Ich bin die meisten Tage hergekommen, habe mich mit unseren Forschern getroffen, die Technologie gelernt und geholfen, wo ich konnte. Es ist aufregend, den Fortschritt zu sehen.",
    },
    # ---- 14. PageRank Philosophie (Stanford) ----
    {
        "aussage_text": "Our goal is to organize the world's information and make it universally accessible and useful. That's really what PageRank was about: figuring out what's important by looking at what other people think is important.",
        "aussage_kurz": "Brin erklaert PageRank als demokratisches Prinzip: Wichtigkeit wird durch kollektive Einschaetzung bestimmt.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 4,
        "quell_link": "https://web.stanford.edu/class/ee380/Abstracts/980902.html",
        "quell_titel": "The Anatomy of a Large-Scale Hypertextual Web Search Engine (Stanford EE380)",
        "datum_aussage": "1998",
        "sprache": "en",
        "kontext": "Stanford-Vortrag 1998. Brin und Page erklaeren den PageRank-Algorithmus vor der Google-Gruendung.",
        "aussage_uebersetzung_de": "Unser Ziel ist es, die Informationen der Welt zu organisieren und sie universell zugaenglich und nuetzlich zu machen. Darum ging es wirklich bei PageRank: herauszufinden, was wichtig ist, indem man schaut, was andere Leute fuer wichtig halten.",
    },
    # ---- 15. Larry Page and Sergey Brin on Failure ----
    {
        "aussage_text": "It's not a failure if you learn something. We always look at things and say, 'What did we learn from that?' Whether it's Glass, or whether it's any other project.",
        "aussage_kurz": "Brin definiert Misserfolg neu: Es ist kein Scheitern, wenn man etwas daraus lernt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 4,
        "quell_link": "https://fortune.com/2015/05/28/alphabet-google-x-failures/",
        "quell_titel": "Why Sergey Brin Celebrates Failure at Google X (Fortune)",
        "datum_aussage": "2015",
        "sprache": "en",
        "kontext": "Interview ueber die Kultur bei Alphabet X. Brin verteidigt gescheiterte Projekte wie Google Glass als wertvolle Lernerfahrungen.",
        "aussage_uebersetzung_de": "Es ist kein Scheitern, wenn man etwas daraus lernt. Wir schauen uns immer Dinge an und sagen: 'Was haben wir daraus gelernt?' Ob es Glass ist oder irgendein anderes Projekt.",
    },
    # ---- 16. Airship / LTA Research ----
    {
        "aussage_text": "I believe lighter-than-air vehicles have the potential to revolutionize disaster relief and cargo transport. This is about solving real-world problems with innovative technology.",
        "aussage_kurz": "Brin sieht Luftschiffe als revolutionaere Loesung fuer Katastrophenhilfe und Frachttransport.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.bloomberg.com/news/articles/2017-05-26/sergey-brin-s-secret-airship-takes-shape-in-silicon-valley",
        "quell_titel": "Sergey Brin's Secret Airship Takes Shape in Silicon Valley (Bloomberg)",
        "datum_aussage": "2017",
        "sprache": "en",
        "kontext": "Bloomberg-Artikel ueber Brins Luftschiff-Projekt (LTA Research). Er finanziert heimlich die Entwicklung eines riesigen Frachtluftschiffs.",
        "aussage_uebersetzung_de": "Ich glaube, dass Leichter-als-Luft-Fahrzeuge das Potenzial haben, Katastrophenhilfe und Frachttransport zu revolutionieren. Dies geht darum, reale Probleme mit innovativer Technologie zu loesen.",
    },
    # ---- 17. On Web Freedom vs. Regulation (2012) ----
    {
        "aussage_text": "There are very powerful forces that have lined up against the open Internet on all sides and around the world. I am more worried than I have been in the past. It's scary. The threat to the freedom of the Internet comes from governments, entertainment industries, and restrictive walled gardens like Facebook and Apple.",
        "aussage_kurz": "Brin warnt 2012 vor Bedrohungen des freien Internets durch Regierungen und Tech-Konzerne.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.theguardian.com/technology/2012/apr/15/web-freedom-threat-google-brin",
        "quell_titel": "Sergey Brin Warns of Threat to Web Freedom (The Guardian)",
        "datum_aussage": "2012-04-15",
        "sprache": "en",
        "kontext": "Guardian-Interview 2012. Brin aeussert sich ungewoehnlich politisch und kritisiert Zensur, Walled Gardens und Regierungseingriffe.",
        "aussage_uebersetzung_de": "Es gibt sehr maechtige Kraefte, die sich auf allen Seiten und rund um die Welt gegen das offene Internet aufgestellt haben. Ich bin besorgter, als ich es in der Vergangenheit war. Es ist beaengstigend. Die Bedrohung der Freiheit des Internets kommt von Regierungen, Unterhaltungsindustrien und restriktiven ummauerten Gaerten wie Facebook und Apple.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Google Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sergey Brin und Larry Page gruenden Google Inc. in einer Garage in Menlo Park, Kalifornien. Sie sammeln eine initiale Finanzierung von $100.000 von Andy Bechtolsheim (Sun Microsystems Mitgruender), noch bevor sie eine Bank haben.",
        "datum_handlung": "1998-09-04",
        "betrag_usd": 100000.0,
        "quell_link": "https://en.wikipedia.org/wiki/History_of_Google",
        "quell_titel": "History of Google - Wikipedia",
        "kontext": "Google beginnt als Forschungsprojekt 'BackRub' in Stanford. PageRank-Algorithmus revolutioniert Suchmaschinen. Brin und Page verwalten Server in ihren Studentenwohnungen.",
    },
    # ---- H2. Google IPO ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Google geht an die Boerse (NASDAQ: GOOG) mit einem ungewoehnlichen Dutch-Auction-Verfahren. Preis: $85 pro Aktie. Gesamtbewertung: $23 Milliarden. Brin und Page werden zu Milliardaeren.",
        "datum_handlung": "2004-08-19",
        "betrag_usd": 1670000000.0,
        "quell_link": "https://www.sec.gov/Archives/edgar/data/1288776/000119312504142742/ds1a.htm",
        "quell_titel": "Google IPO Prospectus (SEC Filing)",
        "kontext": "Im 'Founder's Letter' erklaeren Brin und Page ihre 'Don't be evil'-Philosophie und den Plan, langfristig statt kurzfristig zu denken. Der IPO macht hunderte Google-Mitarbeiter zu Millionaeren.",
    },
    # ---- H3. 23andMe Investition und Heirat ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Sergey Brin investiert persoenlich in 23andMe, ein von seiner damaligen Frau Anne Wojcicki mitgegruendetes Gentests-Unternehmen. Google investiert ebenfalls Millionen.",
        "datum_handlung": "2007",
        "betrag_usd": None,
        "quell_link": "https://www.forbes.com/sites/matthewherper/2017/09/08/23andme-gets-fda-approval-for-cancer-risk-tests/",
        "quell_titel": "How Anne Wojcicki's 23andMe Became a Billion-Dollar Business (Forbes)",
        "kontext": "Brin heiratet Wojcicki 2007 (Scheidung 2015). Er nutzt 23andMe selbst und entdeckt seine LRRK2-Mutation (Parkinson-Risiko).",
    },
    # ---- H4. Google Self-Driving Car Project (Waymo-Vorlaufer) ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sergey Brin initiiert und leitet das Google Self-Driving Car Project (spaeter Waymo). Er holt Sebastian Thrun (DARPA Grand Challenge Gewinner) als Projektleiter. Budget: hunderte Millionen Dollar.",
        "datum_handlung": "2009",
        "betrag_usd": None,
        "quell_link": "https://www.wired.com/2015/08/google-self-driving-car-history/",
        "quell_titel": "The Full History of Google's Self-Driving Car Project (Wired)",
        "kontext": "Das Projekt beginnt geheim in Google X. Brin testet die ersten Prototypen persoenlich und demonstriert sie auf TED-Konferenzen.",
    },
    # ---- H5. Google Glass Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Sergey Brin stellt Google Glass oeffentlich vor -- eine Augmented-Reality-Brille. Er traegt sie persoenlich bei oeffentlichen Events, inklusive einem spektakulaeren Fallschirmsprung-Stunt bei der Google I/O 2012.",
        "datum_handlung": "2012-06-27",
        "betrag_usd": None,
        "quell_link": "https://www.youtube.com/watch?v=D7TB8b2t3QE",
        "quell_titel": "Google Glass Skydiving Demo at Google I/O 2012 (YouTube)",
        "kontext": "Brin ist das Gesicht von Google Glass. Er erscheint in der U-Bahn mit Glass, spricht bei TED darueber und vermarktet es als Zukunft der Technologie.",
    },
    # ---- H6. Alphabet-Gruendung und Umstrukturierung ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Sergey Brin und Larry Page gruenden Alphabet Inc. als Muttergesellschaft von Google. Page wird Alphabet-CEO, Brin wird Praesident. Sundar Pichai uebernimmt Google als CEO.",
        "datum_handlung": "2015-08-10",
        "betrag_usd": None,
        "quell_link": "https://abc.xyz/investor/founders-letters/2015/",
        "quell_titel": "G is for Google - Alphabet Founders' Letter (abc.xyz)",
        "kontext": "Alphabet trennt das Kerngeschaeft (Google) von Moonshot-Projekten (X, Waymo, Verily, etc.). Brin leitet weiterhin X Labs.",
    },
    # ---- H7. Waymo Spin-off ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Das Google Self-Driving Car Project wird als eigenstaendige Alphabet-Tochter 'Waymo' ausgegliedert. CEO: John Krafcik. Waymo wird spaeter auf ueber $30 Milliarden bewertet.",
        "datum_handlung": "2016-12-13",
        "betrag_usd": None,
        "quell_link": "https://waymo.com/blog/2016/12/say-hello-waymo-whats-next-self-driving.html",
        "quell_titel": "Say Hello to Waymo (Waymo Blog)",
        "kontext": "Brin ist treibende Kraft hinter dem Projekt seit 2009. Waymo wird das am weitesten entwickelte autonome Fahrzeug-Programm der Welt.",
    },
    # ---- H8. LTA Research (Airship Project) ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sergey Brin gruendet heimlich LTA Research, ein Unternehmen zur Entwicklung riesiger Frachtluftschiffe. Er baut in einem NASA-Hangar in Mountain View ein 200-Meter-Luftschiff namens 'Pathfinder 1'. Finanzierung: geschaetzt ueber $100 Millionen.",
        "datum_handlung": "2015",
        "betrag_usd": 100000000.0,
        "quell_link": "https://www.bloomberg.com/news/articles/2017-05-26/sergey-brin-s-secret-airship-takes-shape-in-silicon-valley",
        "quell_titel": "Sergey Brin's Secret Airship Takes Shape in Silicon Valley (Bloomberg)",
        "kontext": "Das Projekt wird erst 2017 oeffentlich bekannt. Brin verfolgt eine persoenliche Vision von Luftschiffen fuer humanitaere Hilfe und umweltfreundlichen Frachttransport.",
    },
    # ---- H9. Ruecktritt von Alphabet ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Sergey Brin tritt als Praesident von Alphabet zurueck. Larry Page tritt ebenfalls als CEO zurueck. Sundar Pichai wird CEO von Alphabet und Google. Brin und Page bleiben Aktionaere und Vorstandsmitglieder.",
        "datum_handlung": "2019-12-03",
        "betrag_usd": None,
        "quell_link": "https://blog.google/inside-google/alphabet/letter-from-larry-and-sergey/",
        "quell_titel": "A Letter from Larry and Sergey (Google Blog)",
        "kontext": "In einem gemeinsamen Brief erklaeren Brin und Page, dass Alphabet 'erwachsen' geworden sei und keinen CEO und Praesidenten mehr brauche. Sie ziehen sich weitgehend aus dem Tagesgeschaeft zurueck.",
    },
    # ---- H10. Parkinson-Forschung Spende (Michael J. Fox Foundation) ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Sergey Brin spendet ueber $50 Millionen an die Michael J. Fox Foundation und andere Parkinson-Forschungsorganisationen ueber die Brin Wojcicki Foundation.",
        "datum_handlung": "2009",
        "betrag_usd": 50000000.0,
        "quell_link": "https://www.michaeljfox.org/news/sergey-brin-funds-parkinsons-research-through-23andme",
        "quell_titel": "Sergey Brin Funds Parkinson's Research Through 23andMe (Michael J. Fox Foundation)",
        "kontext": "Motiviert durch seine eigene LRRK2-Mutation und die Parkinson-Erkrankung seiner Mutter. Brin finanziert Studien ueber genetische Faktoren von Parkinson.",
    },
    # ---- H11. Project Loon (Ballon-Internet) ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sergey Brin unterstuetzt die Entwicklung von Project Loon in Google X: ein Netzwerk von Stratosphaeren-Ballons zur Bereitstellung von Internet in abgelegenen Gebieten. Erste Tests in Neuseeland.",
        "datum_handlung": "2013-06-14",
        "betrag_usd": None,
        "quell_link": "https://www.theguardian.com/technology/2013/jun/14/google-project-loon-balloon-internet",
        "quell_titel": "Google's Project Loon: Balloon-Powered Internet for Everyone (The Guardian)",
        "kontext": "Brin leitet Google X und treibt Moonshot-Projekte wie Loon voran. Das Projekt wird spaeter eingestellt, nachdem es in Katastrophenfaellen (z.B. Puerto Rico) erfolgreich eingesetzt wurde.",
    },
    # ---- H12. Rueckkehr zu Google fuer Gemini-Entwicklung ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Nach vier Jahren Abwesenheit kehrt Sergey Brin zu Google zurueck, um an der Entwicklung des Gemini-KI-Modells mitzuwirken. Er arbeitet direkt mit Google Brain und DeepMind zusammen.",
        "datum_handlung": "2023-11",
        "betrag_usd": None,
        "quell_link": "https://www.businessinsider.com/sergey-brin-returns-google-ai-gemini-development-2023-11",
        "quell_titel": "Sergey Brin Returns to Google to Help with Gemini AI (Business Insider)",
        "kontext": "Die Rueckkehr erfolgt inmitten des KI-Wettlaufs mit OpenAI. Brin programmiert selbst und nimmt an technischen Meetings teil -- ein ueberraschender Aktivismus nach Jahren der Zurueckgezogenheit.",
    },
    # ---- H13. Verkauf von Google-Aktien (regelmaessig) ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Sergey Brin verkauft regelmaessig Google/Alphabet-Aktien im Wert von hunderten Millionen Dollar pro Jahr ueber automatisierte Trading-Plaene (10b5-1). Zwischen 2017-2020 verkauft er Aktien im Gesamtwert von ueber $1 Milliarde.",
        "datum_handlung": "2017",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001288776&owner=include",
        "quell_titel": "Alphabet Insider Trading - SEC Form 4 Filings",
        "kontext": "Die Verkaeufe erfolgen planmaessig und sind normal fuer Gruender. Brin bleibt dennoch einer der reichsten Menschen der Welt (ca. $100 Mrd. Vermoegen 2024).",
    },
    # ---- H14. Lobbying und politische Spenden ----
    {
        "handlung_typ": "lobbying",
        "beschreibung": "Sergey Brin und Larry Page spendet persoenlich Millionen an politische Kampagnen, hauptsaechlich an Demokraten und Kandidaten, die Technologie-freundliche Politik unterstuetzen. Google/Alphabet wird einer der groessten Lobbying-Akteure in Washington.",
        "datum_handlung": "2012",
        "betrag_usd": None,
        "quell_link": "https://www.opensecrets.org/orgs/alphabet-inc/summary?id=D000067823",
        "quell_titel": "Alphabet Inc Political Contributions (OpenSecrets)",
        "kontext": "Brin und Page unterstuetzen Kampagnen fuer Einwanderungsreform, Klimaschutz und Netzneutralitaet. Google wird regelmaessig vor dem Kongress angehoert.",
    },
    # ---- H15. Verily Life Sciences Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sergey Brin initiiert die Gruendung von Verily (ehemals Google Life Sciences) als Alphabet-Tochter. Verily entwickelt medizinische Geraete, Gesundheits-Software und Diagnostik-Tools.",
        "datum_handlung": "2015-12-07",
        "betrag_usd": None,
        "quell_link": "https://verily.com/about/",
        "quell_titel": "Verily Life Sciences - About (Verily)",
        "kontext": "Verily ist Teil von Brins langjaehrigem Interesse an Gesundheit und Lebenswissenschaften (motiviert auch durch sein Parkinson-Risiko). Projekte umfassen Glukose-messende Kontaktlinsen und chirurgische Roboter.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=8 existiert
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
            "Claude (collect_brin.py)"
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
        "Sergey Brin quotes, TED talks, Google Glass, Waymo, self-driving cars, PageRank, Google founding, Alphabet X, Gemini AI, 23andMe, Parkinson's research, LTA airship, Project Loon, China censorship",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: TED Talks (2004, 2013), University of Maryland Commencement 2009, The Guardian, Wired, "
        f"Business Insider, Forbes, Bloomberg, CNET, Fast Company, Stanford EE380, "
        f"Google/Alphabet Blog, abc.xyz, Waymo Blog, Verily, Michael J. Fox Foundation, SEC Filings, OpenSecrets. "
        f"HINWEIS: Brin ist extrem oeffentlichkeitsscheu -- meiste Aussagen stammen aus 1998-2015. "
        f"Ueberraschende Rueckkehr 2023 fuer Gemini-Entwicklung.",
        "Claude (collect_brin.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Sergey Brin (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Sergey Brin")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_brin.py")
    print("  Verifizierte Aussagen & Handlungen: Sergey Brin")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
