# -*- coding: utf-8 -*-
"""
Script zum Einfügen von Chris Dixon Aussagen und Handlungen in die Datenbank
Person ID: 50
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 50

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage_data)

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)

def main():
    print("Starte Datensammlung für Chris Dixon (person_id=50)...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # ============== AUSSAGEN ==============
        aussagen = [
            # 1. Web3 Definition
            (PERSON_ID,
             "Web3 is the internet owned by the builders and users, orchestrated with tokens.",
             "Web3 ist das Internet, das Entwicklern und Nutzern gehört, koordiniert durch Tokens",
             "schriftlich",
             6,  # Blog-Artikel
             9,  # Blogs
             "https://a16zcrypto.com/posts/article/why-web3-matters/",
             "Why Web3 Matters",
             "2021-09-26",
             "en",
             "Blog-Post über die Vision von Web3 und dezentraler Internet-Governance",
             "Web3 ist das Internet, das den Entwicklern und Nutzern gehört, orchestriert mit Tokens."),

            # 2. Blockchain als Rettung des Internet
            (PERSON_ID,
             "I believe blockchains and the software movement around them — typically called crypto or web3 — provide the only plausible path to sustaining the original vision of the internet as an open platform that incentivizes creativity and entrepreneurship.",
             "Blockchains bieten den einzigen plausiblen Weg, die ursprüngliche Vision des Internets zu erhalten",
             "schriftlich",
             6,  # Blog-Artikel
             9,  # Blogs
             "https://a16zcrypto.com/posts/article/why-web3-matters/",
             "Why Web3 Matters",
             "2021-09-26",
             "en",
             "Erklärung warum Blockchain-Technologie notwendig ist für ein offenes Internet",
             "Ich glaube, dass Blockchains und die Software-Bewegung darum – typischerweise Crypto oder Web3 genannt – den einzigen plausiblen Weg bieten, die ursprüngliche Vision des Internets als offene Plattform zu erhalten, die Kreativität und Unternehmertum fördert."),

            # 3. Casino Culture Warnung
            (PERSON_ID,
             "Using blockchains and tokens purely for gambling — casino culture — distracts from the true potential of this computing movement.",
             "Blockchains nur zum Glücksspiel zu nutzen lenkt vom wahren Potenzial ab",
             "schriftlich",
             7,  # Nachrichtenartikel
             5,  # Nachrichtenmedien
             "https://fortune.com/crypto/2024/01/25/chris-dixon-read-write-own-a16z-andreessen-horowitz-crypto/",
             "Chris Dixon, the philosopher king of crypto, makes a fresh case for blockchain",
             "2024-01-25",
             "en",
             "Warnung vor spekulativem Missbrauch von Blockchain-Technologie",
             "Blockchains und Tokens rein für Glücksspiel zu nutzen – Casino-Kultur – lenkt vom wahren Potenzial dieser Computing-Bewegung ab."),

            # 4. The Next Big Thing
            (PERSON_ID,
             "The next big thing will start out looking like a toy.",
             "Die nächste große Sache wird anfangs wie ein Spielzeug aussehen",
             "schriftlich",
             6,  # Blog-Artikel
             9,  # Blogs
             "https://cdixon.org/2010/01/03/the-next-big-thing-will-start-out-looking-like-a-toy/",
             "The next big thing will start out looking like a toy",
             "2010-01-03",
             "en",
             "Einflussreicher Essay über disruptive Technologien basierend auf Clayton Christensens Theorie",
             "Die nächste große Sache wird anfangs wie ein Spielzeug aussehen."),

            # 5. Hobbies Quote
            (PERSON_ID,
             "What the smartest people do on the weekend is what everyone else will do during the week in ten years.",
             "Was die klügsten Leute am Wochenende tun, werden alle anderen in zehn Jahren unter der Woche tun",
             "schriftlich",
             6,  # Blog-Artikel
             9,  # Blogs
             "https://cdixon.org/2013/03/02/what-the-smartest-people-do-on-the-weekend-is-what-everyone-else-will-do-during-the-week-in-ten-years/",
             "What the smartest people do on the weekend",
             "2013-03-02",
             "en",
             "Blog-Post über Hobbys als Vorläufer zukünftiger Mainstream-Technologien",
             "Was die klügsten Leute am Wochenende tun, werden alle anderen in zehn Jahren unter der Woche tun."),

            # 6. Hobbies und finanzielle Zwänge
            (PERSON_ID,
             "Hobbies are what the smartest people spend time on when they aren't constrained by near-term financial goals.",
             "Hobbys sind das, womit sich die klügsten Menschen beschäftigen, wenn sie nicht durch kurzfristige finanzielle Ziele eingeschränkt sind",
             "schriftlich",
             8,  # Buch
             8,  # Buecher
             "https://readwriteown.com/",
             "Read Write Own: Building the Next Era of the Internet",
             "2024-01-01",
             "en",
             "Aus seinem Buch über Innovation und langfristiges Denken",
             "Hobbys sind das, womit sich die klügsten Menschen beschäftigen, wenn sie nicht durch kurzfristige finanzielle Ziele eingeschränkt sind."),

            # 7. Corporate Network Control
            (PERSON_ID,
             "Giving away the tool makes financial sense only when the company doing the subsidizing—not the community—will own the ultimate prize: the network.",
             "Gratis-Tools machen nur Sinn, wenn die Firma - nicht die Community - das Netzwerk besitzt",
             "schriftlich",
             8,  # Buch
             8,  # Buecher
             "https://www.goodreads.com/work/quotes/184121527-read-write-own-building-the-next-era-of-the-internet",
             "Read Write Own: Building the Next Era of the Internet",
             "2024-01-01",
             "en",
             "Kritik an der Geschäftspraxis von Web2-Plattformen",
             "Ein Tool gratis anzubieten macht finanziell nur Sinn, wenn die Firma, die subventioniert – nicht die Community – den ultimativen Preis besitzen wird: das Netzwerk."),

            # 8. Tokens und Ownership
            (PERSON_ID,
             "The internet's latest phase—read-write-own era—is defined by a new simplifying concept: tokens, which encapsulate ownership.",
             "Die neueste Internet-Phase - read-write-own - wird durch Tokens definiert, die Eigentum verkörpern",
             "schriftlich",
             8,  # Buch
             8,  # Buecher
             "https://www.penguinrandomhouse.com/books/744504/read-write-own-by-chris-dixon/",
             "Read Write Own: Building the Next Era of the Internet",
             "2024-01-01",
             "en",
             "Definition der Web3-Ära durch das Konzept der Tokens",
             "Die neueste Phase des Internets – die read-write-own-Ära – wird durch ein neues vereinfachendes Konzept definiert: Tokens, die Eigentum verkörpern."),

            # 9. Blockchain und digitales Eigentum
            (PERSON_ID,
             "Blockchains represent a radical departure from the status quo. Through tokens, they flip the script on digital ownership—making users, rather than internet services, owners.",
             "Blockchains machen Nutzer statt Internet-Dienste zu Eigentümern",
             "schriftlich",
             8,  # Buch
             8,  # Buecher
             "https://www.goodreads.com/work/quotes/184121527-read-write-own-building-the-next-era-of-the-internet",
             "Read Write Own: Building the Next Era of the Internet",
             "2024-01-01",
             "en",
             "Über die revolutionäre Natur von Blockchain für digitales Eigentum",
             "Blockchains stellen eine radikale Abkehr vom Status quo dar. Durch Tokens drehen sie das Drehbuch über digitales Eigentum um – und machen Nutzer statt Internet-Dienste zu Eigentümern."),

            # 10. Authentizität und Blockchain
            (PERSON_ID,
             "Turing tests no longer distinguish real people from bots, and people can no longer tell real from fake media. The right approach is a credibly neutral, community-owned network—a blockchain network—that makes authenticity a trusted internet primitive.",
             "Blockchain-Netzwerke können Authentizität zu einem vertrauenswürdigen Internet-Primitiv machen",
             "schriftlich",
             8,  # Buch
             8,  # Buecher
             "https://www.goodreads.com/work/quotes/184121527-read-write-own-building-the-next-era-of-the-internet",
             "Read Write Own: Building the Next Era of the Internet",
             "2024-01-01",
             "en",
             "Über die Rolle von Blockchain bei der Verifizierung von Authentizität im KI-Zeitalter",
             "Turing-Tests unterscheiden nicht mehr echte Menschen von Bots, und Menschen können nicht mehr echte von gefälschten Medien unterscheiden. Der richtige Ansatz ist ein glaubwürdig neutrales, gemeinschaftlich besessenes Netzwerk – ein Blockchain-Netzwerk – das Authentizität zu einem vertrauenswürdigen Internet-Primitiv macht."),

            # 11. UK Expansion Statement
            (PERSON_ID,
             "The UK has deep pools of talent, world-leading academic institutions, and a strong entrepreneurial culture. Following a productive dialogue with the Prime Minister, and months of constructive conversations with HM Treasury, UK policymakers, and the Financial Conduct Authority, we're thrilled to open our first international office in a jurisdiction that welcomes blockchain technology.",
             "UK bietet talentierte Menschen, Universitäten und unternehmerische Kultur sowie Blockchain-freundliche Regulierung",
             "schriftlich",
             10,  # Offizielle Stellungnahme
             5,   # Nachrichtenmedien
             "https://www.businesswire.com/news/home/20230611005029/en",
             "Andreessen Horowitz Announces its First International Expansion to the United Kingdom",
             "2023-06-11",
             "en",
             "Offizielle Stellungnahme zur Eröffnung des ersten internationalen a16z-Büros in London",
             "Das Vereinigte Königreich hat tiefe Talentpools, weltweit führende akademische Institutionen und eine starke unternehmerische Kultur. Nach einem produktiven Dialog mit dem Premierminister und monatelangen konstruktiven Gesprächen mit dem britischen Finanzministerium, britischen Politikern und der Financial Conduct Authority freuen wir uns, unser erstes internationales Büro in einer Jurisdiktion zu eröffnen, die Blockchain-Technologie willkommen heißt."),

            # 12. Yuga Labs und Counterweight
            (PERSON_ID,
             "Yuga Labs combined with other emerging Web3 companies are an important counterweight to companies like Meta.",
             "Yuga Labs und andere Web3-Unternehmen sind ein wichtiges Gegengewicht zu Unternehmen wie Meta",
             "schriftlich",
             7,  # Nachrichtenartikel
             5,  # Nachrichtenmedien
             "https://blockchainreporter.net/qa-with-chris-dixon-web3-yuga-labs/",
             "Q&A With Chris Dixon Web3 Yuga Labs",
             "2022-03-01",
             "en",
             "Kommentar nach der 450 Mio. $ Investition in Yuga Labs (Bored Ape Yacht Club)",
             "Yuga Labs kombiniert mit anderen aufstrebenden Web3-Unternehmen sind ein wichtiges Gegengewicht zu Unternehmen wie Meta."),
        ]

        print(f"Füge {len(aussagen)} Aussagen ein...")
        for aussage in aussagen:
            insert_aussage(cursor, aussage)

        # ============== HANDLUNGEN ==============
        handlungen = [
            # 1. Gründung SiteAdvisor
            (PERSON_ID,
             "gruendung",
             "Mitgründung von SiteAdvisor, einem Web-Security-Startup",
             "2005-01-01",
             "https://techcrunch.com/2012/11/19/hunch-siteadvisor-founder-and-angel-investor-chris-dixon-leaves-ebay-to-join-andressen-horowitz-as-general-partner/",
             "Chris Dixon Joins Andreessen Horowitz As General Partner | TechCrunch",
             "Dixon gründete 2005 SiteAdvisor, das Web-Sicherheitslösungen entwickelte"),

            # 2. Verkauf SiteAdvisor
            (PERSON_ID,
             "verkauf",
             "Verkauf von SiteAdvisor an McAfee für 74 Millionen US-Dollar",
             "2006-01-01",
             "https://en.wikipedia.org/wiki/Chris_Dixon",
             "Chris Dixon - Wikipedia",
             "SiteAdvisor wurde 2006 von McAfee für 74 Mio. $ übernommen"),

            # 3. Gründung Hunch
            (PERSON_ID,
             "gruendung",
             "Gründung von Hunch mit Caterina Fake und Tom Pinckney - eine Empfehlungsplattform",
             "2009-01-01",
             "https://en.wikipedia.org/wiki/Hunch_(website)",
             "Hunch (website) - Wikipedia",
             "Dixon gründete 2009 Hunch, eine Empfehlungsmaschine basierend auf maschinellem Lernen"),

            # 4. Verkauf Hunch
            (PERSON_ID,
             "verkauf",
             "Verkauf von Hunch an eBay für 80 Millionen US-Dollar",
             "2011-11-01",
             "https://techcrunch.com/2012/11/19/hunch-siteadvisor-founder-and-angel-investor-chris-dixon-leaves-ebay-to-join-andressen-horowitz-as-general-partner/",
             "Chris Dixon Joins Andreessen Horowitz As General Partner | TechCrunch",
             "Hunch wurde im November 2011 von eBay für 80 Mio. $ (111,8 Mio. $ in 2024-Dollars) übernommen"),

            # 5. Eintritt bei a16z
            (PERSON_ID,
             "einstellung",
             "Beitritt zu Andreessen Horowitz (a16z) als General Partner",
             "2012-11-19",
             "https://techcrunch.com/2012/11/19/hunch-siteadvisor-founder-and-angel-investor-chris-dixon-leaves-ebay-to-join-andressen-horowitz-as-general-partner/",
             "Chris Dixon Joins Andreessen Horowitz As General Partner | TechCrunch",
             "Dixon verließ eBay um zu a16z zu wechseln, Fokus auf Early-Stage Tech-Investments"),

            # 6. Investition Coinbase
            (PERSON_ID,
             "investition",
             "Führte a16z Investitionen in Coinbase - insgesamt fast 50 Millionen US-Dollar in Bitcoin-bezogene Projekte bis 2014",
             "2014-01-01",
             "https://cdixon.org/2013/12/12/coinbase/",
             "Coinbase - Chris Dixon Blog",
             "Dixon wurde früher Verfechter von Bitcoin-Investitionen, a16z investierte bis 2014 fast 50 Mio. $ in Bitcoin-Ventures wie Coinbase"),

            # 7. Gründung a16z crypto
            (PERSON_ID,
             "gruendung",
             "Gründung und Leitung von a16z crypto - dedizierte Krypto-Sparte von Andreessen Horowitz",
             "2018-01-01",
             "https://a16zcrypto.com/team/chris-dixon/",
             "Chris Dixon - a16z crypto",
             "Dixon gründete a16z crypto, das über vier Fonds mit mehr als 7 Milliarden Dollar verwaltet"),

            # 8. Crypto Fund IV Launch
            (PERSON_ID,
             "investition",
             "Launch des vierten a16z Crypto Fund mit 4,5 Milliarden US-Dollar",
             "2022-05-01",
             "https://www.coindesk.com/consensus-magazine/2022/12/05/chris-dixon-most-influential-2022",
             "Keeping the Crypto Industry Bankrolled - CoinDesk",
             "a16z sammelte 4,5 Mrd. $ für seinen vierten Krypto-Fonds, gerade als der Krypto-Abschwung begann"),

            # 9. Crypto Startup School Accelerator
            (PERSON_ID,
             "produktlaunch",
             "Ankündigung eines neuen Accelerator-Programms 'Crypto Startup School' mit 500.000 US-Dollar Seed-Funding",
             "2022-10-18",
             "https://techcrunch.com/2022/10/18/a16z-crypto-web3-startup-school-accelerator-chris-dixon-disrupt-2022/",
             "a16z's Chris Dixon announces new accelerator program for crypto founders in LA | TechCrunch",
             "12-wöchiges Programm mit 500.000$ Seed-Funding und Zugang zu Mentoren für Crypto-Gründer"),

            # 10. Investition Yuga Labs
            (PERSON_ID,
             "investition",
             "Leitung der 450 Millionen US-Dollar Finanzierungsrunde für Yuga Labs (Bored Ape Yacht Club) mit 4 Milliarden US-Dollar Bewertung",
             "2022-03-01",
             "https://www.coinspeaker.com/yuga-labs-valuation-4b/",
             "Yuga Labs, Bored Ape Yacht Club Creator, Raises $450M at Valuation of $4B - Coinspeaker",
             "a16z crypto führte die 450 Mio. $ Runde für Yuga Labs an, Bewertung: 4 Mrd. $"),

            # 11. UK Office Expansion
            (PERSON_ID,
             "partnerschaft",
             "Ankündigung der ersten internationalen Expansion von a16z mit Büro-Eröffnung in London",
             "2023-06-11",
             "https://www.businesswire.com/news/home/20230611005029/en",
             "Andreessen Horowitz Announces its First International Expansion to the United Kingdom",
             "a16z eröffnet erstes internationales Büro in London, plant Crypto Startup School UK 2024"),

            # 12. Buchveröffentlichung
            (PERSON_ID,
             "produktlaunch",
             "Veröffentlichung des Buches 'Read Write Own: Building the Next Era of the Internet' bei Random House",
             "2024-01-01",
             "https://readwriteown.com/",
             "Read Write Own - Chris Dixon",
             "Buch erreichte Platz 9 der New York Times Bestseller-Liste (Combined Print & E-Book Nonfiction)"),
        ]

        print(f"Füge {len(handlungen)} Handlungen ein...")
        for handlung in handlungen:
            insert_handlung(cursor, handlung)

        conn.commit()
        print(f"\nOK Erfolgreich {len(aussagen)} Aussagen und {len(handlungen)} Handlungen eingefügt!")
        print(f"Chris Dixon (person_id={PERSON_ID}) - Tier 2 Status erreicht")

        # Verifikation
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
        aussagen_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
        handlungen_count = cursor.fetchone()[0]

        print(f"\nVerifikation:")
        print(f"  - Aussagen in DB: {aussagen_count}")
        print(f"  - Handlungen in DB: {handlungen_count}")
        print(f"  - Tier 2 Anforderung: >=10 Aussagen, >=8 Handlungen")
        print(f"  - Status: {'OK ERFUELLT' if aussagen_count >= 10 and handlungen_count >= 8 else 'FEHLT NICHT ERFUELLT'}")

    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()
        print("\nDatenbankverbindung geschlossen.")

if __name__ == "__main__":
    main()
