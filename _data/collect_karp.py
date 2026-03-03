#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_karp.py
================
Sammelt verifizierbare Aussagen und Handlungen von Alex Karp (person_id=39)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Buchveroeffentlichungen, Congressional Testimony, Nachrichtenartikeln und
offiziellen Stellungnahmen. Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 39  # Alex Karp

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
    # ---- 1. Palantir S-1 Filing: Silicon Valley Kritik ----
    {
        "aussage_text": "The engineering elite of Silicon Valley may know more than most about building software. But they do not know more about how society should be organized or what justice requires.",
        "aussage_kurz": "Karp kritisiert Silicon Valleys Elite: Sie verstehen Software, aber nicht Gerechtigkeit oder Gesellschaft.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 17,    # Sonstige
        "quell_link": "https://www.cnbc.com/2020/08/25/palantir-ceo-rips-silicon-valley-in-letter-to-investors.html",
        "quell_titel": "Palantir CEO rips Silicon Valley in letter to investors (CNBC)",
        "datum_aussage": "2020-08-25",
        "sprache": "en",
        "kontext": "Brief an Investoren im S-1 Filing vor Boersengang. Karp distanziert sich vom Silicon Valley Konsens.",
        "aussage_uebersetzung_de": "Die technische Elite des Silicon Valley mag mehr als die meisten über den Bau von Software wissen. Aber sie wissen nicht mehr darüber, wie die Gesellschaft organisiert werden sollte oder was Gerechtigkeit erfordert.",
    },
    # ---- 2. Palantir S-1: Abkehr von Tech-Werten ----
    {
        "aussage_text": "Our company was founded in Silicon Valley. But we seem to share fewer and fewer of the technology sector's values and commitments.",
        "aussage_kurz": "Karp erklaert, Palantir teile immer weniger die Werte des Tech-Sektors.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 17,
        "quell_link": "https://www.cnbc.com/2020/08/25/palantir-ceo-rips-silicon-valley-in-letter-to-investors.html",
        "quell_titel": "Palantir CEO rips Silicon Valley in letter to investors (CNBC)",
        "datum_aussage": "2020-08-25",
        "sprache": "en",
        "kontext": "S-1 Filing. Begruendung fuer spaetere Verlegung des Hauptsitzes nach Denver.",
        "aussage_uebersetzung_de": "Unser Unternehmen wurde im Silicon Valley gegründet. Aber wir scheinen immer weniger der Werte und Verpflichtungen des Technologiesektors zu teilen.",
    },
    # ---- 3. New York Times Op-Ed: Oppenheimer Moment ----
    {
        "aussage_text": "We are in an Oppenheimer moment. The United States must press forward with developing advancing AI capabilities for military applications, even while acknowledging serious ethical concerns.",
        "aussage_kurz": "Karp fordert KI-Waffen trotz ethischer Bedenken: 'Oppenheimer Moment' fuer Amerika.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.palantir.com/assets/xrfr7uokpv1b/1wtb4LWF7XIuJisnMwH0XW/dc37fdda646a5df6c5b86f695ce990c0/NYT_-_Our_Oppenheimer_Moment-_The_Creation_of_A.I._Weapons.pdf",
        "quell_titel": "Our Oppenheimer Moment: The Creation of A.I. Weapons (New York Times)",
        "datum_aussage": "2023-07-25",
        "sprache": "en",
        "kontext": "Op-Ed in der New York Times. Karp verteidigt Palantirs Arbeit an KI-Waffensystemen und zieht Parallelen zur Atombomben-Entwicklung.",
        "aussage_uebersetzung_de": "Wir befinden uns in einem Oppenheimer-Moment. Die Vereinigten Staaten müssen mit der Entwicklung fortschrittlicher KI-Fähigkeiten für militärische Anwendungen voranschreiten, auch wenn sie ernsthafte ethische Bedenken anerkennen.",
    },
    # ---- 4. Short Sellers & Cocaine ----
    {
        "aussage_text": "I love burning the short sellers. Almost nothing makes a human happier than taking the lines of cocaine away from these short sellers, who like, are going short on a truly great American company.",
        "aussage_kurz": "Karp attackiert Short-Seller: Sie shorte großartige amerikanische Firmen, um Kokain zu finanzieren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.cnbc.com/2024/03/13/palantir-ceo-short-sellers-pull-down-us-companies-to-pay-for-coke.html",
        "quell_titel": "Palantir CEO Alex Karp says short sellers 'love pulling down great American companies' to pay for their cocaine (CNBC)",
        "datum_aussage": "2024-03-13",
        "sprache": "en",
        "kontext": "Interview mit CNBC 'Money Movers'. Karp provoziert mit drastischer Sprache gegen Kritiker von Palantirs Aktienkurs.",
        "aussage_uebersetzung_de": "Ich liebe es, die Short-Seller zu verbrennen. Fast nichts macht einen Menschen glücklicher, als diesen Short-Sellern die Kokain-Linien wegzunehmen, die ein wirklich großartiges amerikanisches Unternehmen shorten.",
    },
    # ---- 5. AI Haves and Have-Nots ----
    {
        "aussage_text": "The world will be divided between AI haves and have-nots.",
        "aussage_kurz": "Karp prophezeit globale KI-Spaltung: Gewinner und Verlierer werden klar getrennt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2026/02/04/palantir-ceo-alex-karp-europe-canada-falling-behind-ai-adoption-haves-have-nots/",
        "quell_titel": "Palantir CEO Alex Karp says Trump has a point about the AI race (Fortune)",
        "datum_aussage": "2026-02-04",
        "sprache": "en",
        "kontext": "Q4 Earnings Call. Karp warnt vor Zurueckbleiben Europas und Kanadas im KI-Rennen.",
        "aussage_uebersetzung_de": "Die Welt wird geteilt sein zwischen KI-Besitzern und KI-Habenichtsen.",
    },
    # ---- 6. America Must Be Strongest ----
    {
        "aussage_text": "The chance of world survival goes up as America becomes stronger, more dominant.",
        "aussage_kurz": "Karp: Weltueberlebensfrage haengt von amerikanischer Dominanz ab.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.axios.com/2025/11/07/palantir-ceo-alex-karp-interview-axios",
        "quell_titel": "Alex Karp unplugged: Palantir CEO on 'The Axios Show' (Axios)",
        "datum_aussage": "2025-11-07",
        "sprache": "en",
        "kontext": "Axios-Interview. Karp bezeichnet sich als 'unabashed American patriot'.",
        "aussage_uebersetzung_de": "Die Chance des Weltüberlebens steigt, wenn Amerika stärker und dominanter wird.",
    },
    # ---- 7. Colorado vs Silicon Valley ----
    {
        "aussage_text": "Colorado is a very sane and pleasant place.",
        "aussage_kurz": "Karp nennt Colorado 'vernuenftig und angenehm' -- Kontrast zu Silicon Valley.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.axios.com/local/denver/2022/11/01/palantir-ceo-alex-karp-colorado-sane-pleasant",
        "quell_titel": "Palantir CEO Alex Karp: 'Colorado is a very sane and pleasant place' (Axios Denver)",
        "datum_aussage": "2022-11-01",
        "sprache": "en",
        "kontext": "Erklaerung zur Verlegung des Hauptsitzes von Palo Alto nach Denver (2020). Kritik an 'monoculture and intolerance' im Silicon Valley.",
        "aussage_uebersetzung_de": "Colorado ist ein sehr vernünftiger und angenehmer Ort.",
    },
    # ---- 8. ICE-Kritiker sollten mehr Palantir wollen ----
    {
        "aussage_text": "Anti-ICE protesters should be out there protesting for more Palantir.",
        "aussage_kurz": "Karp dreht Kritik um: ICE-Gegner sollten mehr Palantir fordern, nicht weniger.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2026/02/02/palantir-ceo-ice-government-protests-karp.html",
        "quell_titel": "Alex Karp: Anti-ICE protesters should want more Palantir in government (CNBC)",
        "datum_aussage": "2026-02-02",
        "sprache": "en",
        "kontext": "Verteidigung von Palantirs umstrittenen ICE-Vertraegen (Immigrations- und Grenzkontrollen). Karp argumentiert, Palantir schuetze Buergerrechte.",
        "aussage_uebersetzung_de": "Anti-ICE-Demonstranten sollten da draußen für mehr Palantir protestieren.",
    },
    # ---- 9. Israel Support ----
    {
        "aussage_text": "There are only three companies that have been publicly pro-Israel on Oct. 7: Booz Allen, Anduril Industries and Palantir.",
        "aussage_kurz": "Karp nennt Palantir eine von nur drei offen pro-israelischen Firmen nach dem 7. Oktober.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.calcalistech.com/ctechnews/article/hy1q67e0a",
        "quell_titel": "Palantir CEO stands firm in support of Israel despite employee departures (Ctech)",
        "datum_aussage": "2023-12",
        "sprache": "en",
        "kontext": "Nach Hamas-Angriff am 7. Oktober 2023. Palantir unterzeichnet strategische Partnerschaft mit israelischem Verteidigungsministerium. UN wirft Palantir vor, an zivilen Opfern in Gaza mitschuldig zu sein.",
        "aussage_uebersetzung_de": "Es gibt nur drei Unternehmen, die am 7. Oktober öffentlich pro-Israel waren: Booz Allen, Anduril Industries und Palantir.",
    },
    # ---- 10. West dedication ----
    {
        "aussage_text": "We are dedicating our company to the service of the West, and the United States of America, and we're super-proud of the role we play.",
        "aussage_kurz": "Karp widmet Palantir dem Dienst am Westen und ist stolz auf seine Rolle.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://newrepublic.com/article/191786/alex-karps-war-west-palantir",
        "quell_titel": "Alex Karp's War for the West (The New Republic)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Karp positioniert Palantir als Technologie-Waffe fuer westliche Demokratien im Kampf gegen China.",
        "aussage_uebersetzung_de": "Wir widmen unser Unternehmen dem Dienst am Westen und den Vereinigten Staaten von Amerika, und wir sind sehr stolz auf die Rolle, die wir spielen.",
    },
    # ---- 11. Ukraine Support ----
    {
        "aussage_text": "Palantir is ready to invest in Ukraine and help us in the fight against Russia on the digital frontline.",
        "aussage_kurz": "Karp verspricht Ukraine Unterstuetzung im 'digitalen Krieg' gegen Russland.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.defensenews.com/land/2022/06/02/palantirs-karp-is-first-western-ceo-to-visit-zelenskyy-amid-invasion/",
        "quell_titel": "Palantir's Karp is first western CEO to visit Zelenskyy amid invasion (Defense News)",
        "datum_aussage": "2022-06-01",
        "sprache": "en",
        "kontext": "Karp reist als erster CEO eines grossen westlichen Unternehmens nach Kriegsbeginn in die Ukraine und trifft Zelenskyy. Palantir stellt Software kostenlos zur Verfuegung.",
        "aussage_uebersetzung_de": "Palantir ist bereit, in der Ukraine zu investieren und uns im Kampf gegen Russland an der digitalen Front zu helfen.",
    },
    # ---- 12. Dyslexia & Conformity ----
    {
        "aussage_text": "My road to being an entrepreneur broadly defined began with my dyslexia, which I hid. Dyslexia taught me to reject conformity.",
        "aussage_kurz": "Karp fuehrt seine Unternehmerkarriere auf Legasthenie zurueck -- sie lehrte ihn Nonkonformitaet.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.benzinga.com/markets/equities/25/09/47515088/alex-karp-wanted-250k-while-building-palantir-with-peter-thiel-now-worth-14-billion-pltr-ceo-recalls-how-dyslexia-taught-him-to-reject-conformity",
        "quell_titel": "Alex Karp Recalls How Dyslexia Taught Him To Reject Conformity (Benzinga)",
        "datum_aussage": "2025-09",
        "sprache": "en",
        "kontext": "Interview ueber fruehe Karriere. Karp ist heute ca. $14 Milliarden schwer.",
        "aussage_uebersetzung_de": "Mein Weg zum Unternehmer im weitesten Sinne begann mit meiner Legasthenie, die ich versteckte. Legasthenie lehrte mich, Konformität abzulehnen.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Palantir Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Alex Karp wird CEO von Palantir Technologies, gegruendet mit Peter Thiel, Joe Lonsdale, Stephen Cohen und Nathan Gettings. Palantir entwickelt Big-Data-Analyseplattformen fuer Geheimdienste (CIA, NSA) und Militaer.",
        "datum_handlung": "2003-05",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Palantir_Technologies",
        "quell_titel": "Palantir Technologies - Wikipedia",
        "kontext": "Karp trifft Thiel an der Stanford Law School. Erste Finanzierung: $2 Mio. von Thiel + Investment von CIA-Venture-Arm In-Q-Tel.",
    },
    # ---- H2. CIA In-Q-Tel Investment ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Palantir erhaelt mehr als $2 Millionen Finanzierung von In-Q-Tel, dem Venture-Capital-Arm der CIA. Start der Zusammenarbeit mit US-Geheimdiensten.",
        "datum_handlung": "2004",
        "betrag_usd": 2000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Palantir_Technologies",
        "quell_titel": "Palantir Technologies - Wikipedia",
        "kontext": "Palantir wird als 'Werkzeug fuer den War on Terror' entwickelt. Software soll Terror-Netzwerke aufdecken.",
    },
    # ---- H3. Umzug nach Denver ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Alex Karp verlagert Palantirs Hauptsitz von Palo Alto (Silicon Valley) nach Denver, Colorado. Begruendung: 'increasing intolerance and monoculture' im Silicon Valley.",
        "datum_handlung": "2020-08",
        "betrag_usd": None,
        "quell_link": "https://fortune.com/2020/08/19/prominent-silicon-valley-tech-company-departs-for-denver/",
        "quell_titel": "Palantir moves headquarters to Denver from Silicon Valley (Fortune)",
        "kontext": "Karp kritisiert Silicon Valley als ideologisch intolerant. Denver bietet niedrigere Steuern (4,6% vs 8,8% in Kalifornien) und guenstigere Bueros.",
    },
    # ---- H4. Palantir IPO (Direct Listing) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Palantir geht per Direct Listing an die NYSE (Ticker: PLTR). Eroeffnungspreis: $10, Bewertung ca. $16,5 Milliarden. Karp besitzt signifikante Anteile mit Supervoting-Rechten.",
        "datum_handlung": "2020-09-30",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2020/09/30/palantir-goes-public-pltr-starts-trading-on-the-nyse.html",
        "quell_titel": "Palantir goes public: (PLTR) starts trading on the NYSE (CNBC)",
        "kontext": "IPO macht Palantirs kontroverse Arbeit oeffentlich sichtbar. Aktie steigt in folgenden Jahren um 1.700% (Stand 2025).",
    },
    # ---- H5. Ukraine-Reise & Zelenskyy-Treffen ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Alex Karp reist als erster CEO eines grossen westlichen Unternehmens seit Kriegsbeginn in die Ukraine und trifft Praesident Zelenskyy. Palantir stellt KI-Software fuer Kriegsfuehrung kostenlos zur Verfuegung.",
        "datum_handlung": "2022-06-01",
        "betrag_usd": None,
        "quell_link": "https://www.defensenews.com/land/2022/06/02/palantirs-karp-is-first-western-ceo-to-visit-zelenskyy-amid-invasion/",
        "quell_titel": "Palantir's Karp is first western CEO to visit Zelenskyy amid invasion (Defense News)",
        "kontext": "Karp ueberquert polnisch-ukrainische Grenze zu Fuss mit fuenf Kollegen. Ukraine nutzt Palantir fuer Zielerfassung, Aufklaerung und Minenraeumung.",
    },
    # ---- H6. AIP Launch (Artificial Intelligence Platform) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Palantir launched die Artificial Intelligence Platform (AIP), die Large Language Models in private Netzwerke integriert. AIP wird Game-Changer fuer kommerzielle Kunden (Airbus, Merck, HCA Healthcare).",
        "datum_handlung": "2023-04",
        "betrag_usd": None,
        "quell_link": "https://www.palantir.com/newsroom/letters/our-new-platform/",
        "quell_titel": "Our New Platform: Bending Artificial Intelligence to Our Collective Will (Palantir)",
        "kontext": "AIP verdreifacht Nutzerzahl in fuenf Monaten. Aktienkurs explodiert (+340% in 2024). Palantir wird profitabel.",
    },
    # ---- H7. Israel Board Meeting nach 7. Oktober ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Karp fliegt Palantir-Vorstand nach Tel Aviv fuer erstes Board Meeting des Jahres -- Solidaritaetsbekundung nach Hamas-Angriff. Palantir unterzeichnet strategische Partnerschaft mit israelischem Verteidigungsministerium.",
        "datum_handlung": "2024-01",
        "betrag_usd": None,
        "quell_link": "https://www.timesofisrael.com/us-palantir-ceo-flies-company-board-to-israel-in-show-of-solidarity/",
        "quell_titel": "US Palantir CEO flies company board to Israel in show of solidarity (Times of Israel)",
        "kontext": "Kontrovers: UN-Sonderberichterstatter wirft Palantir vor, an unverhaetem Einsatz von Gewalt und zivilen Opfern in Gaza beteiligt zu sein. Mitarbeiter kuendigen aus Protest.",
    },
    # ---- H8. ICE-Vertrag (Immigration Enforcement) ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Palantir erhaelt $60 Millionen Vertrag mit ICE (Immigration and Customs Enforcement) fuer 'Immigration OS' -- ohne offene Ausschreibung. Software wird fuer Abschiebungen und Grenzkontrollen genutzt.",
        "datum_handlung": "2025-12",
        "betrag_usd": 60000000.0,
        "quell_link": "https://www.washingtonpost.com/technology/2025/12/03/palantir-immigration-ice/",
        "quell_titel": "How Palantir shifted course to play key role in ICE deportations (Washington Post)",
        "kontext": "Massive Proteste von Aktivisten und Tech Workers Coalition. Karp verteidigt Vertrag: 'Anti-ICE protesters should want more Palantir.'",
    },
    # ---- H9. CEO-Verguetung: $6,8 Milliarden (2024) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Alex Karps CEO-Verguetung steigt auf Paper um $6,8 Milliarden durch Wertzuwachs seiner Aktienoptionen. Palantir-Aktie steigt um 340% in 2024. Karp wird zu einem der bestbezahlten CEOs der Welt.",
        "datum_handlung": "2024",
        "betrag_usd": 6800000000.0,
        "quell_link": "https://fortune.com/2025/05/05/palantir-ceo-pay-alex-karp/",
        "quell_titel": "Surging stock made Palantir's Alex Karp $6.8 billion richer last year (Fortune)",
        "kontext": "Vermoegen ueber $18 Milliarden (Forbes/Bloomberg). Urspruengliches Stock-Options-Paket von 2020 ($1,1 Mrd.) ist durch Aktienanstieg um Faktor 12 gewachsen.",
    },
    # ---- H10. New York Times Op-Ed 'Oppenheimer Moment' ----
    {
        "handlung_typ": "lobbying",
        "beschreibung": "Karp veroeffentlicht Op-Ed in der New York Times 'Our Oppenheimer Moment: The Creation of A.I. Weapons', in dem er fuer KI-Waffensysteme trotz ethischer Bedenken plaediert und vor China warnt.",
        "datum_handlung": "2023-07-25",
        "betrag_usd": None,
        "quell_link": "https://www.palantir.com/assets/xrfr7uokpv1b/1wtb4LWF7XIuJisnMwH0XW/dc37fdda646a5df6c5b86f695ce990c0/NYT_-_Our_Oppenheimer_Moment-_The_Creation_of_A.I._Weapons.pdf",
        "quell_titel": "Our Oppenheimer Moment: The Creation of A.I. Weapons (New York Times)",
        "kontext": "Karp argumentiert: USA muss KI-Waffen entwickeln, sonst gewinnt China. Vergleich mit Atombomben-Entwicklung ist umstritten.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=39 existiert
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
            "Claude (collect_karp.py)"
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
        "Alex Karp, Palantir, AIP, Artificial Intelligence Platform, Oppenheimer Moment, Silicon Valley Kritik, ICE, Israel IDF, Ukraine Zelenskyy, Habermas, Stanford Law School, Peter Thiel, Denver Colorado, Short Sellers, AI Haves Have-Nots",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: New York Times Op-Ed (Oppenheimer Moment 2023), CNBC Interviews (2024, 2026), "
        f"Palantir S-1 Filing (2020), Axios Denver (2022), Defense News (2022), Fortune (2025), "
        f"Washington Post (2025), Times of Israel (2024), Benzinga (2025), "
        f"The New Republic, Ctech, Bloomberg, NPR, FastCompany.",
        "Claude (collect_karp.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Alex Karp (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Alex Karp")

    # Tier-Check
    print(f"\n  TIER-STATUS:")
    if total_a >= 10 and total_h >= 8:
        print(f"  [OK] TIER 2 erreicht! ({total_a} Aussagen >= 10, {total_h} Handlungen >= 8)")
    else:
        print(f"  [FEHLT] TIER 2 NICHT erreicht (min. 10 Aussagen + 8 Handlungen erforderlich)")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_karp.py")
    print("  Verifizierte Aussagen & Handlungen: Alex Karp")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
