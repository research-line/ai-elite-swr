#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palmer Luckey Data Collection Script
Sammelt Aussagen und Handlungen von Palmer Luckey (person_id=43) für die Aussagen-Datenbank
"""

import sqlite3
from datetime import datetime

# Datenbank-Pfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID für Palmer Luckey
PERSON_ID = 43

def connect_db():
    """Verbindung zur Datenbank herstellen"""
    return sqlite3.connect(DB_PATH)

def insert_aussage(conn, aussage_data):
    """Eine Aussage in die Datenbank einfügen"""
    cursor = conn.cursor()

    query = """
    INSERT INTO aussagen (
        person_id, aussage_text, aussage_kurz, modus,
        quellen_typ_id, plattform_id, quell_link, quell_titel,
        datum_aussage, sprache, kontext, aussage_uebersetzung_de
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(query, (
        PERSON_ID,
        aussage_data['aussage_text'],
        aussage_data['aussage_kurz'],
        aussage_data['modus'],
        aussage_data['quellen_typ_id'],
        aussage_data['plattform_id'],
        aussage_data['quell_link'],
        aussage_data['quell_titel'],
        aussage_data['datum_aussage'],
        aussage_data['sprache'],
        aussage_data['kontext'],
        aussage_data['aussage_uebersetzung_de']
    ))

    return cursor.lastrowid

def insert_handlung(conn, handlung_data):
    """Eine Handlung in die Datenbank einfügen"""
    cursor = conn.cursor()

    query = """
    INSERT INTO handlungen (
        person_id, handlung_typ, beschreibung,
        datum_handlung, quell_link, quell_titel,
        kontext, betrag_usd, notizen
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # Kombiniere handlung_kurz, ziel_org, auswirkung in notizen
    notizen = f"Kurz: {handlung_data.get('handlung_kurz', '')}"
    if handlung_data.get('ziel_org'):
        notizen += f"\nZiel-Org: {handlung_data['ziel_org']}"
    if handlung_data.get('auswirkung'):
        notizen += f"\nAuswirkung: {handlung_data['auswirkung']}"

    cursor.execute(query, (
        PERSON_ID,
        handlung_data['handlung_typ'],
        handlung_data['handlung_beschreibung'],
        handlung_data['datum_handlung'],
        handlung_data['quell_link'],
        handlung_data['quell_titel'],
        handlung_data['kontext'],
        handlung_data.get('betrag_usd'),
        notizen
    ))

    return cursor.lastrowid

def collect_luckey_data():
    """Hauptfunktion zum Sammeln aller Palmer Luckey Daten"""

    # Aussagen von Palmer Luckey (mindestens 10 für Tier 2)
    aussagen = [
        {
            'aussage_text': 'I am here to build a $50 billion company',
            'aussage_kurz': 'Will ein 50-Milliarden-Dollar-Unternehmen aufbauen',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.thetwentyminutevc.com/palmerluckey',
            'quell_titel': '20VC: Anduril Founder, Palmer Luckey',
            'datum_aussage': '2020-09-21',
            'sprache': 'en',
            'kontext': 'Interview im 20VC Podcast über seine Vision für Anduril Industries',
            'aussage_uebersetzung_de': 'Ich bin hier, um ein 50-Milliarden-Dollar-Unternehmen aufzubauen'
        },
        {
            'aussage_text': 'When it comes to life and death decision-making, I think that it is too morally fraught an area, it is too critical of an area, to not apply the best technology available to you. If you\'re talking about killing people, you need to be minimizing the amount of collateral damage. You need to be as certain as you can in anything that you do.',
            'aussage_kurz': 'KI-Waffen moralisch notwendig zur Minimierung ziviler Opfer',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cbsnews.com/news/palmer-luckey-ai-powered-autonomous-weapons-future-of-warfare-60-minutes-transcript/',
            'quell_titel': 'Palmer Luckey on 60 Minutes - AI-powered autonomous weapons',
            'datum_aussage': '2025-05-18',
            'sprache': 'en',
            'kontext': '60 Minutes Interview über autonome Waffensysteme und die Ethik von KI im Krieg',
            'aussage_uebersetzung_de': 'Bei Entscheidungen über Leben und Tod ist dies ein zu moralisch belasteter Bereich, ein zu kritischer Bereich, um nicht die beste verfügbare Technologie anzuwenden. Wenn es darum geht, Menschen zu töten, muss man die Kollateralschäden minimieren. Man muss sich so sicher wie möglich sein bei allem, was man tut.'
        },
        {
            'aussage_text': 'There\'s no moral high ground to making a land mine that can\'t tell the difference between a school bus full of children and Russian armor. It\'s not a question between smart weapons and no weapons. It\'s a question between smart weapons and dumb weapons.',
            'aussage_kurz': 'Intelligente Waffen sind moralischer als dumme Waffen',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://officechai.com/ai/life-and-death-situations-in-war-are-too-morally-fraught-and-critical-to-not-use-ai-anduril-ceo-palmer-luckey/',
            'quell_titel': 'Palmer Luckey: Life-And-Death Situations In War Too Critical To Not Use AI',
            'datum_aussage': '2025-12-07',
            'sprache': 'en',
            'kontext': 'Verteidigung von KI-gesteuerten Waffen gegenüber traditionellen Waffensystemen',
            'aussage_uebersetzung_de': 'Es gibt keinen moralischen Vorteil bei der Herstellung einer Landmine, die nicht zwischen einem Schulbus voller Kinder und russischer Panzerung unterscheiden kann. Es ist keine Frage zwischen intelligenten Waffen und keinen Waffen. Es ist eine Frage zwischen intelligenten und dummen Waffen.'
        },
        {
            'aussage_text': 'I would be a lot more like China. I think that China\'s done a very good job of focusing their resources on the technology that they believe is going to win the next war',
            'aussage_kurz': 'USA sollte bei Militärtechnologie mehr wie China sein',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.thetwentyminutevc.com/palmerluckey',
            'quell_titel': '20VC Podcast Interview with Palmer Luckey',
            'datum_aussage': '2020-09-21',
            'sprache': 'en',
            'kontext': 'Diskussion über die Verteidigungsstrategie des US-Verteidigungsministeriums',
            'aussage_uebersetzung_de': 'Ich würde viel mehr wie China sein. Ich denke, China hat sehr gute Arbeit geleistet, seine Ressourcen auf die Technologie zu konzentrieren, von der sie glauben, dass sie den nächsten Krieg gewinnen wird'
        },
        {
            'aussage_text': 'I got fired from Facebook for no reason at all. I gave $10,000 to a pro-Trump group, and I think that\'s something to do with it.',
            'aussage_kurz': 'Von Facebook gefeuert wegen Trump-Spende',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2019/05/22/oculus-co-founder-i-got-fired-from-facebook-for-no-reason-at-all.html',
            'quell_titel': 'Oculus founder: I got fired from Facebook for no reason at all',
            'datum_aussage': '2019-05-22',
            'sprache': 'en',
            'kontext': 'CNBC Interview über seine Entlassung bei Facebook/Meta',
            'aussage_uebersetzung_de': 'Ich wurde von Facebook ohne jeden Grund gefeuert. Ich habe 10.000 Dollar an eine Pro-Trump-Gruppe gespendet, und ich denke, das hat etwas damit zu tun.'
        },
        {
            'aussage_text': 'You publicly told everyone my departure had nothing to do with politics, which is absolutely insane and obviously contradicted by reams of internal communications.',
            'aussage_kurz': 'Wirft Meta vor, über politische Gründe seiner Entlassung zu lügen',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://www.roadtovr.com/metas-apologizes-oculus-founder-palmer-luckey-ousting/',
            'quell_titel': 'Meta\'s Head of XR Apologizes to Oculus Founder Regarding His Ousting',
            'datum_aussage': '2024-04-15',
            'sprache': 'en',
            'kontext': 'Antwort auf Meta CTO Andrew Bosworth bezüglich seiner Entlassung 2017',
            'aussage_uebersetzung_de': 'Du hast öffentlich jedem erzählt, mein Weggang hätte nichts mit Politik zu tun, was absolut verrückt ist und offensichtlich durch unzählige interne Kommunikationen widerlegt wird.'
        },
        {
            'aussage_text': 'I\'ve continued to believe that virtual reality and augmented reality are going to be a critical part of our military. The ability to have night vision, thermal vision, the ability to see through walls, the ability to coordinate with autonomous systems - this is the future of warfare.',
            'aussage_kurz': 'VR/AR werden kritischer Teil des Militärs sein',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://x.com/MarioNawfal/status/1979427228262748407',
            'quell_titel': 'Palmer Luckey: The Future of Warfare is a Hive Mind of Vision',
            'datum_aussage': '2025-09-15',
            'sprache': 'en',
            'kontext': 'Diskussion über die Rolle von VR/AR-Technologie in militärischen Anwendungen',
            'aussage_uebersetzung_de': 'Ich glaube weiterhin daran, dass Virtual Reality und Augmented Reality ein kritischer Teil unseres Militärs sein werden. Die Fähigkeit, Nachtsicht, Wärmebild, die Fähigkeit durch Wände zu sehen, die Fähigkeit mit autonomen Systemen zu koordinieren - das ist die Zukunft der Kriegsführung.'
        },
        {
            'aussage_text': 'We are definitely going to be a publicly traded company',
            'aussage_kurz': 'Anduril wird definitiv an die Börse gehen',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2025/06/10/anduril-palmer-luckey-ipo.html',
            'quell_titel': 'Anduril CEO Palmer Luckey says the defense tech company will \'definitely\' go public',
            'datum_aussage': '2025-06-10',
            'sprache': 'en',
            'kontext': 'CNBC Interview über die Zukunft von Anduril Industries',
            'aussage_uebersetzung_de': 'Wir werden definitiv ein börsennotiertes Unternehmen sein'
        },
        {
            'aussage_text': 'My big league support for Donald Trump is no secret',
            'aussage_kurz': 'Bekennt sich offen zu Trump-Unterstützung',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/PalmerLuckey/status/1791264464135942354',
            'quell_titel': 'Palmer Luckey on X about Trump support',
            'datum_aussage': '2024-05-16',
            'sprache': 'en',
            'kontext': 'Twitter-Post über mediale Berichterstattung zu Tech-Führungskräften und Trump',
            'aussage_uebersetzung_de': 'Meine große Unterstützung für Donald Trump ist kein Geheimnis'
        },
        {
            'aussage_text': 'DeepSeek is legitimately impressive, but the level of hysteria is an indictment of so many. The $5M number is bogus. It is pushed by a Chinese hedge fund to slow investment in American AI startups',
            'aussage_kurz': 'DeepSeek-Kosten sind Desinformation chinesischer Hedgefonds',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/PalmerLuckey/status/1884351579240927677',
            'quell_titel': 'Palmer Luckey on X about DeepSeek',
            'datum_aussage': '2025-01-28',
            'sprache': 'en',
            'kontext': 'Kommentar zur DeepSeek-KI-Kontroverse und Behauptungen über Entwicklungskosten',
            'aussage_uebersetzung_de': 'DeepSeek ist legitim beeindruckend, aber das Ausmaß der Hysterie ist eine Anklage gegen so viele. Die 5-Millionen-Dollar-Zahl ist Unsinn. Sie wird von einem chinesischen Hedgefonds verbreitet, um Investitionen in amerikanische KI-Startups zu verlangsamen'
        },
        {
            'aussage_text': 'A Tesla has better AI than any U.S. aircraft and a Roomba vacuum has better autonomy than most of the Pentagon\'s weapons systems',
            'aussage_kurz': 'Pentagon-Waffensysteme technologisch veraltet',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cbsnews.com/news/palmer-luckey-future-warfare-anduril-60-minutes/',
            'quell_titel': 'Tech billionaire Palmer Luckey wants to remake the U.S. military',
            'datum_aussage': '2025-05-18',
            'sprache': 'en',
            'kontext': '60 Minutes Interview - Kritik an veralteter Pentagon-Technologie',
            'aussage_uebersetzung_de': 'Ein Tesla hat bessere KI als jedes US-Flugzeug und ein Roomba-Staubsauger hat bessere Autonomie als die meisten Waffensysteme des Pentagon'
        },
        {
            'aussage_text': 'It\'s good to scare people sometimes',
            'aussage_kurz': 'Es ist gut, Menschen manchmal zu erschrecken',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://fortune.com/2026/01/08/30-billion-defense-tech-company-founder-palmer-luckey-anduril-embraces-trumps-crack-down-threats-defense-industry/',
            'quell_titel': 'Anduril founder Palmer Luckey embraces Trump\'s threat to crack down',
            'datum_aussage': '2026-01-08',
            'sprache': 'en',
            'kontext': 'Kommentar zu Trumps Drohungen gegen die Verteidigungsindustrie',
            'aussage_uebersetzung_de': 'Es ist gut, Menschen manchmal zu erschrecken'
        }
    ]

    # Handlungen von Palmer Luckey (mindestens 8 für Tier 2)
    handlungen = [
        {
            'handlung_typ': 'verkauf',
            'handlung_beschreibung': 'Verkauf von Oculus VR an Facebook (Meta) für 2,3 Milliarden US-Dollar. Palmer Luckey war 21 Jahre alt und wurde zum jüngsten Self-Made-Milliardär in der VR-Branche.',
            'handlung_kurz': 'Verkauf Oculus an Facebook für $2,3 Mrd',
            'datum_handlung': '2014-03-25',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://en.wikipedia.org/wiki/Palmer_Luckey',
            'quell_titel': 'Palmer Luckey - Wikipedia',
            'kontext': 'Einer der größten Tech-Deals der 2010er Jahre, machte Luckey mit 21 zum Milliardär',
            'betrag_usd': 2300000000,
            'ziel_org': 'Facebook/Meta',
            'auswirkung': 'Ermöglichte Facebook Einstieg in VR/Metaverse, finanzierte Luckeys spätere Defense-Tech-Ventures'
        },
        {
            'handlung_typ': 'gruendung',
            'handlung_beschreibung': 'Gründung von Anduril Industries zusammen mit Trae Stephens (Founders Fund) und anderen Silicon Valley Veterans. Fokus auf autonome Verteidigungssysteme und KI-gesteuerte Waffen.',
            'handlung_kurz': 'Gründung Anduril Industries (Defense-Tech)',
            'datum_handlung': '2017-06-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://en.wikipedia.org/wiki/Anduril_Industries',
            'quell_titel': 'Anduril Industries - Wikipedia',
            'kontext': 'Nach Entlassung von Facebook, neues Unternehmen zur Disruption der Verteidigungsindustrie',
            'betrag_usd': None,
            'ziel_org': 'Anduril Industries',
            'auswirkung': 'Schuf neuen Player in Defense-Tech, brachte Silicon Valley Methoden in Militärtechnologie'
        },
        {
            'handlung_typ': 'entlassung',
            'handlung_beschreibung': 'Palmer Luckey wurde von Facebook entlassen, nachdem bekannt wurde, dass er 10.000 Dollar an Nimble America gespendet hatte, eine Pro-Trump-Gruppe. Interne Facebook-Emails zeigten, dass dies auf höchster Führungsebene diskutiert wurde.',
            'handlung_kurz': 'Entlassung von Facebook wegen Trump-Spende',
            'datum_handlung': '2017-03-31',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2019/05/22/oculus-co-founder-i-got-fired-from-facebook-for-no-reason-at-all.html',
            'quell_titel': 'Oculus co-founder: I got fired from Facebook',
            'kontext': 'Politisch motivierte Entlassung trotz gegenteiliger öffentlicher Aussagen von Zuckerberg',
            'betrag_usd': None,
            'ziel_org': 'Facebook/Meta',
            'auswirkung': 'Markierte Ende seiner VR-Karriere, führte zu Karrierewechsel in Defense-Tech'
        },
        {
            'handlung_typ': 'spende',
            'handlung_beschreibung': 'Spende von 10.000 US-Dollar an Nimble America, eine Pro-Donald Trump Organisation, die Anti-Hillary-Clinton Werbung schaltete. Diese Spende führte zu seiner späteren Entlassung bei Facebook.',
            'handlung_kurz': 'Spende an Pro-Trump-Gruppe Nimble America',
            'datum_handlung': '2016-09-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.theloganbartlettshow.com/archive/how-palmer-luckey-got-fired-for-making-a-9-000-donation',
            'quell_titel': 'How Palmer Luckey Got Fired for Making a $9000 Donation',
            'kontext': 'Politische Spende während des Präsidentschaftswahlkampfs 2016',
            'betrag_usd': 10000,
            'ziel_org': 'Nimble America',
            'auswirkung': 'Auslöser für Kontroverse und spätere Entlassung von Facebook'
        },
        {
            'handlung_typ': 'investition',
            'handlung_beschreibung': 'Anduril sicherte sich 450 Millionen Dollar Series D Finanzierung bei einer Bewertung von 4,7 Milliarden Dollar. Luckey als Gründer und CEO führte diese Finanzierungsrunde an.',
            'handlung_kurz': 'Anduril Series D: $450M bei $4,7B Bewertung',
            'datum_handlung': '2021-06-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://sacra.com/c/anduril/',
            'quell_titel': 'Anduril revenue, valuation & funding | Sacra',
            'kontext': 'Massive Finanzierungsrunde zur Skalierung von Anduril',
            'betrag_usd': 450000000,
            'ziel_org': 'Anduril Industries',
            'auswirkung': 'Positionierte Anduril als Unicorn im Defense-Tech Sektor'
        },
        {
            'handlung_typ': 'investition',
            'handlung_beschreibung': 'Anduril schloss Series E Finanzierungsrunde über 1,48 Milliarden Dollar ab bei einer Bewertung von 8,5 Milliarden Dollar.',
            'handlung_kurz': 'Anduril Series E: $1,48B bei $8,5B Bewertung',
            'datum_handlung': '2022-12-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://fortune.com/2025/06/05/anduril-palmer-luckey-funding-30-billion-valuation-founders-fund/',
            'quell_titel': 'Anduril nearing size of defense industry giants - Fortune',
            'kontext': 'Weitere massive Expansion von Anduril Industries',
            'betrag_usd': 1480000000,
            'ziel_org': 'Anduril Industries',
            'auswirkung': 'Verdoppelung der Bewertung innerhalb von 18 Monaten'
        },
        {
            'handlung_typ': 'investition',
            'handlung_beschreibung': 'Anduril sicherte sich 2,5 Milliarden Dollar Series G Finanzierung angeführt von Founders Fund (Peter Thiel), die 1 Milliarde Dollar investierten - der größte Check in der Geschichte des Fonds. Bewertung erreichte 30,5 Milliarden Dollar.',
            'handlung_kurz': 'Anduril Series G: $2,5B bei $30,5B Bewertung',
            'datum_handlung': '2025-06-05',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2025/06/05/anduril-valuation-founders-fund.html',
            'quell_titel': 'Anduril raises funding at $30.5 billion valuation',
            'kontext': 'Rekord-Finanzierungsrunde im Defense-Tech Sektor',
            'betrag_usd': 2500000000,
            'ziel_org': 'Anduril Industries',
            'auswirkung': 'Anduril wird zu einem der wertvollsten privaten Defense-Tech Unternehmen'
        },
        {
            'handlung_typ': 'partnerschaft',
            'handlung_beschreibung': 'Anduril gewann 1 Milliarde Dollar Vertrag für Counter-Unmanned Systems Arbeit mit dem United States Special Operations Command (SOCOM).',
            'handlung_kurz': 'SOCOM Counter-UAS Vertrag: $1 Milliarde',
            'datum_handlung': '2022-02-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://en.wikipedia.org/wiki/Palmer_Luckey',
            'quell_titel': 'Palmer Luckey - Wikipedia',
            'kontext': 'Wichtiger Durchbruch im US-Militär-Markt für Anduril',
            'betrag_usd': 1000000000,
            'ziel_org': 'US SOCOM',
            'auswirkung': 'Etablierte Anduril als ernstzunehmenden Defense-Contractor'
        },
        {
            'handlung_typ': 'partnerschaft',
            'handlung_beschreibung': 'Anduril gewann 250 Millionen Dollar Pentagon-Vertrag für Roadrunner-M Interceptor-Drohnen und elektronische Kriegsführungssysteme.',
            'handlung_kurz': 'Pentagon Drohnen-Verteidigungssystem: $250M',
            'datum_handlung': '2024-10-08',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.defensenews.com/unmanned/2024/10/08/anduril-lands-250-million-pentagon-contract-for-drone-defense-system/',
            'quell_titel': 'Anduril lands $250 million Pentagon contract',
            'kontext': 'Ausbau von Andurils Drohnen-Abwehrsystemen für das Pentagon',
            'betrag_usd': 250000000,
            'ziel_org': 'US Department of Defense',
            'auswirkung': 'Stärkung von Andurils Position im autonomen Verteidigungssystem-Markt'
        },
        {
            'handlung_typ': 'partnerschaft',
            'handlung_beschreibung': 'Anduril gewann 642,2 Millionen Dollar Vertrag mit der US Navy für Drohnensysteme und autonome Plattformen.',
            'handlung_kurz': 'US Navy Drohnen-Vertrag: $642,2M',
            'datum_handlung': '2025-03-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.nasdaq.com/articles/anduril-could-ipo-soon-what-does-anduril-even-do',
            'quell_titel': 'Anduril Could IPO Soon - Nasdaq',
            'kontext': 'Expansion in maritime autonome Systeme',
            'betrag_usd': 642200000,
            'ziel_org': 'US Navy',
            'auswirkung': 'Diversifizierung von Andurils Produkt-Portfolio über Luftsysteme hinaus'
        }
    ]

    # Datenbank-Verbindung herstellen
    conn = connect_db()

    try:
        print(f"Beginne Datensammlung für Palmer Luckey (person_id={PERSON_ID})...")
        print(f"{'='*70}")

        # Aussagen einfügen
        print(f"\nFüge {len(aussagen)} Aussagen ein...")
        aussage_ids = []
        for i, aussage in enumerate(aussagen, 1):
            aussage_id = insert_aussage(conn, aussage)
            aussage_ids.append(aussage_id)
            print(f"  [{i}/{len(aussagen)}] Aussage eingefügt (ID: {aussage_id}): {aussage['aussage_kurz'][:60]}...")

        # Handlungen einfügen
        print(f"\nFüge {len(handlungen)} Handlungen ein...")
        handlung_ids = []
        for i, handlung in enumerate(handlungen, 1):
            handlung_id = insert_handlung(conn, handlung)
            handlung_ids.append(handlung_id)
            print(f"  [{i}/{len(handlungen)}] Handlung eingefügt (ID: {handlung_id}): {handlung['handlung_kurz'][:60]}...")

        # Änderungen committen
        conn.commit()

        print(f"\n{'='*70}")
        print(f"Erfolgreich abgeschlossen!")
        print(f"  - {len(aussagen)} Aussagen eingefuegt (IDs: {min(aussage_ids)} - {max(aussage_ids)})")
        print(f"  - {len(handlungen)} Handlungen eingefuegt (IDs: {min(handlung_ids)} - {max(handlung_ids)})")
        print(f"\nPalmer Luckey Tier 2 Status erreicht:")
        print(f"  - Mindestens 10 Aussagen (aktuell: {len(aussagen)})")
        print(f"  - Mindestens 8 Handlungen (aktuell: {len(handlungen)})")

    except Exception as e:
        conn.rollback()
        print(f"\nFEHLER: {e}")
        raise

    finally:
        conn.close()
        print(f"\nDatenbank-Verbindung geschlossen.")

if __name__ == "__main__":
    collect_luckey_data()
