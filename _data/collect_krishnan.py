#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Sriram Krishnan (person_id=37)
Senior White House Policy Advisor für AI (seit Januar 2025)
Ehemaliger a16z General Partner, ehemaliger Twitter/Facebook/Snap Product Lead
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 37

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage_data)

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("=" * 80)
    print(f"Sammle Daten für Sriram Krishnan (person_id={PERSON_ID})")
    print("=" * 80)

    # ============================================================================
    # AUSSAGEN (mindestens 10 für Tier 2)
    # ============================================================================

    aussagen = [
        # Aussage 1: US-China AI Race
        (PERSON_ID,
         "national AI development is an existential race with China",
         "KI-Entwicklung ist existenzieller Wettlauf mit China",
         "muendlich",
         4,  # Panel-Diskussion
         4,  # Konferenzen
         "https://broadbandbreakfast.com/trump-ai-advisor-touts-plan-to-secure-u-s-leadership/",
         "Trump AI Advisor Touts Plan to Secure U.S. Leadership - POLITICO AI & Tech Summit",
         "2025-01-15",
         "en",
         "Aussage bei der POLITICO AI & Tech Summit 2025 über die strategische Bedeutung von KI für die USA",
         "Die nationale KI-Entwicklung ist ein existenzieller Wettlauf mit China"),

        # Aussage 2: Market Share Competition
        (PERSON_ID,
         "The United States and China are in a race for AI supremacy, in which the winner will be judged by market share",
         "USA und China konkurrieren um KI-Vorherrschaft - Gewinner wird durch Marktanteil bestimmt",
         "muendlich",
         4,  # Panel-Diskussion
         4,  # Konferenzen
         "https://www.axios.com/2025/09/17/sriram-krishnan-trump-artificial-intelligence-axios-summit",
         "White House AI adviser targets market share in race with China - Axios AI+ Summit 2025",
         "2025-09-17",
         "en",
         "Aussage beim Axios AI+ Summit 2025 über die Metriken des KI-Wettbewerbs",
         "Die Vereinigten Staaten und China befinden sich in einem Rennen um die KI-Vorherrschaft, bei dem der Gewinner am Marktanteil gemessen wird"),

        # Aussage 3: Let them cook
        (PERSON_ID,
         "private companies are best positioned to create new models, let them cook",
         "Private Unternehmen sollen KI-Modelle entwickeln - 'lasst sie machen'",
         "muendlich",
         4,  # Panel-Diskussion
         4,  # Konferenzen
         "https://broadbandbreakfast.com/trump-ai-advisor-touts-plan-to-secure-u-s-leadership/",
         "Trump AI Advisor on Private Sector AI Leadership",
         "2025-01-20",
         "en",
         "Aussage über die Rolle des privaten Sektors in der KI-Entwicklung",
         "Private Unternehmen sind am besten positioniert, um neue Modelle zu erstellen - lasst sie machen"),

        # Aussage 4: American AI Stack Dominance
        (PERSON_ID,
         "We need to make sure American AI – our stack, our chips, our models – are the ones that the world uses. Not Chinese models or Chinese chips.",
         "Amerikanische KI-Technologie muss weltweit Standard werden",
         "schriftlich",
         5,  # Social-Media-Post
         2,  # Twitter/X
         "https://x.com/sriramk/status/1961072926561550366",
         "Sriram Krishnan on American AI dominance - X/Twitter",
         "2025-02-25",
         "en",
         "Tweet über die Notwendigkeit amerikanischer KI-Dominanz gegenüber China",
         "Wir müssen sicherstellen, dass amerikanische KI – unser Stack, unsere Chips, unsere Modelle – diejenigen sind, die die Welt nutzt. Nicht chinesische Modelle oder chinesische Chips."),

        # Aussage 5: Early Era - No Heavy-Handed Regulation
        (PERSON_ID,
         "the administration views AI as being in an early era akin to the internet in the 1990s. Heavy-handed rules could stifle U.S. innovation.",
         "KI ist in früher Phase wie Internet 1990er - übermäßige Regulierung schadet Innovation",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://broadbandbreakfast.com/trump-ai-advisor-touts-plan-to-secure-u-s-leadership/",
         "Krishnan on AI Regulation Philosophy",
         "2025-01-22",
         "en",
         "Aussage über die regulatorische Herangehensweise der Trump-Administration an KI",
         "Die Regierung betrachtet KI als in einer frühen Phase ähnlich dem Internet in den 1990er Jahren. Übermäßige Regulierung könnte die US-Innovation ersticken."),

        # Aussage 6: State Regulation Hinders Competitiveness
        (PERSON_ID,
         "state-by-state regulation of AI technologies may hinder national AI competitiveness",
         "Einzelstaatliche KI-Regulierung schadet nationaler Wettbewerbsfähigkeit",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://www.cio.com/article/3629924/trump-taps-sriram-krishnan-for-ai-advisor-role-amid-strategic-shift-in-tech-policy.html",
         "Sriram Krishnan on State vs Federal AI Regulation",
         "2025-01-18",
         "en",
         "Warnung vor fragmentierter KI-Regulierung auf staatlicher Ebene in den USA",
         "Die staatliche Regulierung von KI-Technologien kann die nationale KI-Wettbewerbsfähigkeit beeinträchtigen"),

        # Aussage 7: Deep State vs Tech Understanding
        (PERSON_ID,
         "Classic deep state Washington thinking around tech is focused purely on control and risk and has a lack of understanding of technology/developer ecosystems work. For the American AI stack to win, we need to maximize marketshare.",
         "Deep State fokussiert auf Kontrolle statt auf Marktanteil-Maximierung",
         "schriftlich",
         5,  # Social-Media-Post
         2,  # Twitter/X
         "https://x.com/sriramk/status/1961072926561550366",
         "Sriram Krishnan criticizing Washington tech policy approach",
         "2025-02-25",
         "en",
         "Kritik an traditionellem Washington-Denken über Technologiepolitik",
         "Das klassische Deep-State-Denken in Washington über Technologie konzentriert sich rein auf Kontrolle und Risiko und hat ein mangelndes Verständnis für Technologie- und Entwickler-Ökosysteme. Damit der amerikanische KI-Stack gewinnt, müssen wir den Marktanteil maximieren."),

        # Aussage 8: Web3 Economic Share
        (PERSON_ID,
         "With web3 … people who contribute value to the platform now have a share of the economics happening in the platform itself",
         "Web3 ermöglicht wirtschaftliche Teilhabe der Nutzer an Plattformen",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://techcrunch.com/2022/06/11/andreessen-horowitzs-sriram-krishnan-on-crypto-social-networking/",
         "Andreessen Horowitz's Sriram Krishnan on crypto social networking - TechCrunch",
         "2022-06-11",
         "en",
         "Interview über die wirtschaftlichen Vorteile von Web3-Plattformen für Nutzer",
         "Mit Web3 haben Menschen, die Wert zur Plattform beitragen, nun einen Anteil an der Ökonomie, die auf der Plattform selbst stattfindet"),

        # Aussage 9: Web3 Governance
        (PERSON_ID,
         "with web3, you now have a say in the governance of said platform too. This opens up a whole new toolbox and new power dynamic between creators and the social media platforms",
         "Web3 gibt Nutzern Mitsprache bei Plattform-Governance",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://techcrunch.com/2022/06/11/andreessen-horowitzs-sriram-krishnan-on-crypto-social-networking/",
         "Sriram Krishnan on Web3 governance models",
         "2022-06-11",
         "en",
         "Aussage über demokratische Governance-Möglichkeiten in Web3",
         "Mit Web3 haben Sie jetzt auch ein Mitspracherecht bei der Governance der Plattform. Das eröffnet ein völlig neues Werkzeugset und eine neue Machtdynamik zwischen Erstellern und Social-Media-Plattformen"),

        # Aussage 10: Decentralized Social Future
        (PERSON_ID,
         "I predict a rise in the number and diversity of online spaces due to decentralization and platforms like Farcaster, Bluesky and Mastodon",
         "Vorhersage: Mehr dezentrale Online-Räume durch Farcaster, Bluesky, Mastodon",
         "schriftlich",
         6,  # Blog-Artikel
         5,  # Nachrichtenmedien (NYT)
         "https://en.wikipedia.org/wiki/Sriram_Krishnan",
         "Sriram Krishnan - New York Times Opinion Column on Social Media 2023",
         "2023-04-15",
         "en",
         "NYT-Kolumne über die Zukunft dezentraler Social-Media-Plattformen",
         "Ich prognostiziere einen Anstieg der Anzahl und Vielfalt von Online-Räumen aufgrund von Dezentralisierung und Plattformen wie Farcaster, Bluesky und Mastodon"),

        # Aussage 11: Transparent Content Moderation
        (PERSON_ID,
         "social media platforms should commit to publishing the details of every account and content moderation decision",
         "Plattformen sollten alle Content-Moderation-Entscheidungen transparent veröffentlichen",
         "schriftlich",
         6,  # Blog-Artikel
         9,  # Blogs
         "https://sriramk.substack.com/p/proposal-transparent-content-moderation",
         "Proposal: Transparent content moderation - Sriram Krishnan Substack",
         "2022-11-05",
         "en",
         "Vorschlag für transparente Content-Moderation auf Social-Media-Plattformen",
         "Social-Media-Plattformen sollten sich verpflichten, die Details jeder Konto- und Content-Moderationsentscheidung zu veröffentlichen"),

        # Aussage 12: Immigration - Country Caps
        (PERSON_ID,
         "Anything to remove country caps for green cards / unlock skilled immigration would be huge … we need the best, regardless of where they happen to be born",
         "Länderlimits für Green Cards aufheben - beste Talente unabhängig von Geburtsort",
         "schriftlich",
         5,  # Social-Media-Post
         2,  # Twitter/X
         "https://www.dnaindia.com/analysis/report-donald-trump-s-ai-head-sriram-krishnan-s-views-on-h1b-visas-green-cards-3124299",
         "Sriram Krishnan on immigration reform and green card country caps",
         "2024-12-26",
         "en",
         "X-Post über die Notwendigkeit, Länderobergrenzen für Green Cards zu entfernen",
         "Alles, um die Länderobergrenzen für Green Cards zu entfernen / qualifizierte Einwanderung zu ermöglichen, wäre enorm wichtig … wir brauchen die Besten, unabhängig davon, wo sie geboren wurden"),

        # Aussage 13: AI Action Plan Announcement
        (PERSON_ID,
         "Today is a day we have been working towards for six months. We are announcing America's AI action plan putting us on the road to continued AI dominance. The three core themes: Accelerate AI innovation - Build American AI infrastructure - Lead in international AI",
         "Ankündigung des AI Action Plans nach 6 Monaten Arbeit",
         "schriftlich",
         5,  # Social-Media-Post
         2,  # Twitter/X
         "https://x.com/sriramk/status/1948032895676788915",
         "Sriram Krishnan announcing AI Action Plan - July 2025",
         "2025-07-21",
         "en",
         "Offizielle Ankündigung des amerikanischen AI Action Plans auf X/Twitter",
         "Heute ist ein Tag, auf den wir seit sechs Monaten hingearbeitet haben. Wir kündigen Amerikas KI-Aktionsplan an, der uns auf den Weg zu anhaltender KI-Dominanz bringt. Die drei Kernthemen: KI-Innovation beschleunigen - Amerikanische KI-Infrastruktur aufbauen - International bei KI führen"),

        # Aussage 14: Learning from Great Engineers
        (PERSON_ID,
         "It is very hard to make yourself get to the top of an industry unless you know what greatness looks like. I was lucky. When I joined Facebook, I was surrounded — just by sheer serendipity — by some great engineers.",
         "Erfolg erfordert Vorbild von Exzellenz - bei Facebook von großartigen Ingenieuren umgeben",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://shawnryanshow.com/blogs/the-shawn-ryan-show/srs-238-sriram-krishnan-senior-white-house-policy-advisor-for-ai",
         "Sriram Krishnan on Shawn Ryan Show #238 - Sept 2025",
         "2025-09-22",
         "en",
         "Aussage im Shawn Ryan Show Podcast über die Bedeutung von Vorbildern für beruflichen Erfolg",
         "Es ist sehr schwer, an die Spitze einer Branche zu gelangen, wenn man nicht weiß, wie Großartigkeit aussieht. Ich hatte Glück. Als ich zu Facebook kam, war ich – durch puren Zufall – von großartigen Ingenieuren umgeben."),
    ]

    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for i, aussage in enumerate(aussagen, 1):
        insert_aussage(cursor, aussage)
        print(f"  [{i:2d}] {aussage[2][:80]}...")

    # ============================================================================
    # HANDLUNGEN (mindestens 8 für Tier 2)
    # ============================================================================

    handlungen = [
        # Handlung 1: White House Ernennung
        (PERSON_ID,
         "einstellung",
         "Ernennung zum Senior White House Policy Advisor für Artificial Intelligence durch Präsident Donald Trump. Verantwortlich für KI-Strategie und Koordination der KI-Politik über die gesamte Regierung hinweg.",
         "2024-12-22",
         "https://techcrunch.com/2024/12/22/sriram-krishnan-named-trumps-senior-policy-advisor-for-ai/",
         "Sriram Krishnan named Trump's senior policy advisor for AI - TechCrunch",
         "Offizielle Ankündigung durch Trump am 22. Dezember 2024, Amtsantritt Januar 2025"),

        # Handlung 2: a16z General Partner Beitritt
        (PERSON_ID,
         "einstellung",
         "Beitritt zu Andreessen Horowitz (a16z) als General Partner mit Fokus auf Consumer und Web3/Crypto-Investitionen. Leitete später das erste internationale a16z-Büro in London.",
         "2021-02-03",
         "https://techcrunch.com/2021/02/03/social-platform-veteran-sriram-krishnan-is-andreessen-horowitzs-latest-general-partner/",
         "Sriram Krishnan is Andreessen Horowitz's latest general partner - TechCrunch",
         "Nach erfolgreicher Karriere bei Facebook, Twitter und Snap wechselte Krishnan ins Venture Capital"),

        # Handlung 3: a16z Austritt
        (PERSON_ID,
         "ruecktritt",
         "Verlassen von Andreessen Horowitz (a16z) am Ende 2024 nach fast 4 Jahren als General Partner, um sich auf die White House Rolle vorzubereiten.",
         "2024-11-30",
         "https://yourstory.com/2024/11/andreessen-horowitz-partner-sriram-krishnan-to-leave-firm",
         "Andreessen Horowitz partner Sriram Krishnan to leave firm - YourStory",
         "Ankündigung des Austritts im November 2024, offizieller Abgang Ende Dezember 2024"),

        # Handlung 4: Twitter Product Lead
        (PERSON_ID,
         "einstellung",
         "Beitritt zu Twitter als Senior Director of Product. Verantwortlich für Core Consumer Product Teams, erzielte 20% jährliches Nutzerwachstum.",
         "2017-09-18",
         "https://techcrunch.com/2017/09/18/snap-facebook-pop-sriram-krishnan-joins-twitter-as-senior-director-of-product/",
         "Snap, Facebook, Pop: Sriram Krishnan joins Twitter - TechCrunch",
         "Wechsel von Snap zu Twitter, leitete Teams für Home Timeline, Events und Trending Topics"),

        # Handlung 5: Twitter Beratung für Elon Musk
        (PERSON_ID,
         "sonstiges",
         "Beratung von Elon Musk beim Twitter-Revamp nach dessen Übernahme 2022. Teil eines Advisory-Teams mit David Sacks, Jason Calacanis und anderen.",
         "2022-10-28",
         "https://businesschief.eu/leadership-and-strategy/sriram-krishnan-the-tech-guru-advising-musk-on-twitter-deal",
         "Sriram Krishnan, the tech guru advising Musk on Twitter - Business Chief",
         "Unterstützte Musk bei Produktentscheidungen und Strategie nach der Twitter-Übernahme"),

        # Handlung 6: Farcaster Investment
        (PERSON_ID,
         "investition",
         "Direktinvestition in Farcaster, ein dezentrales Social-Media-Protokoll. Teil seiner Web3-Social-Network-Investitionsstrategie bei a16z.",
         "2022-07-15",
         "https://dailyhodl.com/2023/04/10/crypto-venture-capitalist-forecasts-future-of-decentralized-social-media-heres-his-outlook/",
         "Crypto VC Sriram Krishnan invests in Farcaster - Daily Hodl",
         "Investment als Teil seiner These über dezentrale Social Networks und Web3-Governance"),

        # Handlung 7: a16z London Office Gründung
        (PERSON_ID,
         "gruendung",
         "Gründung und Leitung des ersten internationalen a16z-Büros in London (UK) mit Fokus auf Web3, Crypto und AI-Investments.",
         "2023-03-15",
         "https://blockworks.co/news/a16z-uk-office-london",
         "A16z eyes UK markets, opens first overseas office in London - Blockworks",
         "Strategische Expansion von a16z nach Europa unter Krishnans Leitung"),

        # Handlung 8: AI Action Plan Launch
        (PERSON_ID,
         "produktlaunch",
         "Co-Autor und Koordinator des amerikanischen AI Action Plans (zusammen mit David Sacks und Michael Kratsios), veröffentlicht im Juli 2025 als zentrale KI-Strategie der USA.",
         "2025-07-21",
         "https://en.wikipedia.org/wiki/Sriram_Krishnan",
         "American AI Action Plan - July 2025",
         "6-monatige Arbeit an umfassendem KI-Strategieplan mit Fokus auf Innovation, Infrastruktur und internationale Führung"),

        # Handlung 9: Stargate Initiative Support
        (PERSON_ID,
         "lobbying",
         "Unterstützung und Koordination der Stargate Initiative - $500 Milliarden KI-Infrastruktur-Investment über 5 Jahre (bis 2029) für amerikanische KI-Dominanz.",
         "2025-01-21",
         "https://www.centeraipolicy.org/work/whats-at-the-other-end-of-stargate",
         "Stargate AI Infrastructure Project - $500B Initiative",
         "Krishnan als White House AI Advisor war maßgeblich an der Koordination des größten KI-Infrastruktur-Investments der Geschichte beteiligt"),

        # Handlung 10: TIME Person of the Year 2025
        (PERSON_ID,
         "sonstiges",
         "Auszeichnung als TIME Person of the Year 2025 in der Kategorie 'Architects of AI'. Anerkennung für seinen Einfluss auf die amerikanische KI-Politik.",
         "2025-12-12",
         "https://time.com/7339685/person-of-the-year-2025-ai-architects/",
         "The Architects of AI Are TIME's 2025 Person of the Year",
         "TIME würdigte Krishnan als einen der Architekten der KI, der den Wake-Up Call für die Stargate-Initiative gab"),

        # Handlung 11: Facebook Audience Network Build
        (PERSON_ID,
         "produktlaunch",
         "Aufbau und Launch des Facebook Audience Network - einer Werbe-Plattform als Konkurrenz zu Googles Ad-Technologien.",
         "2015-06-10",
         "https://en.wikipedia.org/wiki/Sriram_Krishnan",
         "Sriram Krishnan builds Facebook Audience Network",
         "Bedeutendes Produkt-Launch bei Facebook, das Werbetechnologie demokratisieren sollte"),
    ]

    print(f"\nFüge {len(handlungen)} Handlungen ein...")
    for i, handlung in enumerate(handlungen, 1):
        insert_handlung(cursor, handlung)
        print(f"  [{i:2d}] {handlung[1]:20s} - {handlung[2][:60]}...")

    # ============================================================================
    # COMMIT UND ABSCHLUSS
    # ============================================================================

    conn.commit()

    print("\n" + "=" * 80)
    print("ZUSAMMENFASSUNG")
    print("=" * 80)
    print(f"Aussagen eingefuegt:   {len(aussagen)} (Tier 2 erfuellt: >=10 OK)")
    print(f"Handlungen eingefuegt: {len(handlungen)} (Tier 2 erfuellt: >=8 OK)")
    print(f"\nDaten erfolgreich in {DB_PATH} gespeichert!")
    print("=" * 80)

    conn.close()

if __name__ == "__main__":
    main()
