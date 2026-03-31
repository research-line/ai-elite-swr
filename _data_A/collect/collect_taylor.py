#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_taylor.py
Sammelt Aussagen und Handlungen von Bret Taylor (person_id=27) für die Forschungsdatenbank
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 27  # Bret Taylor

def check_duplicate_aussage(cursor, person_id, aussage_text):
    """Prüft ob eine Aussage bereits existiert (via Text-Vergleich)"""
    cursor.execute("""
        SELECT COUNT(*) FROM aussagen
        WHERE person_id = ? AND aussage_text = ?
    """, (person_id, aussage_text))
    return cursor.fetchone()[0] > 0

def check_duplicate_handlung(cursor, person_id, handlung_typ, beschreibung, datum):
    """Prüft ob eine Handlung bereits existiert"""
    cursor.execute("""
        SELECT COUNT(*) FROM handlungen
        WHERE person_id = ? AND handlung_typ = ? AND beschreibung = ? AND datum_handlung = ?
    """, (person_id, handlung_typ, beschreibung, datum))
    return cursor.fetchone()[0] > 0

def insert_aussage(cursor, aussage):
    """Fügt eine Aussage in die Datenbank ein"""
    if check_duplicate_aussage(cursor, PERSON_ID, aussage['aussage_text']):
        return False

    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
            plattform_id, quell_link, quell_titel, datum_aussage,
            sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        aussage['aussage_text'],
        aussage['aussage_kurz'],
        aussage['modus'],
        aussage['quellen_typ_id'],
        aussage['plattform_id'],
        aussage['quell_link'],
        aussage['quell_titel'],
        aussage['datum_aussage'],
        aussage['sprache'],
        aussage['kontext'],
        aussage['aussage_uebersetzung_de']
    ))
    return True

def insert_handlung(cursor, handlung):
    """Fügt eine Handlung in die Datenbank ein"""
    if check_duplicate_handlung(cursor, PERSON_ID, handlung['handlung_typ'],
                                 handlung['beschreibung'], handlung['datum']):
        return False

    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        handlung['handlung_typ'],
        handlung['beschreibung'],
        handlung['datum'],
        handlung['quell_link'],
        handlung['quell_titel'],
        handlung['kontext']
    ))
    return True

def main():
    """Hauptfunktion zum Sammeln und Einfügen der Daten"""

    print("="*80)
    print("DATENSAMMLUNG: BRET TAYLOR (person_id=27)")
    print("="*80)
    print()

    # Suchprotokoll
    search_log = []
    search_log.append("SUCHPROTOKOLL - Bret Taylor Recherche")
    search_log.append("="*80)
    search_log.append(f"Recherche-Datum: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    search_log.append("")
    search_log.append("Durchgeführte Suchen:")
    search_log.append("1. 'Bret Taylor Sierra AI quotes interviews 2024 2025'")
    search_log.append("2. 'Bret Taylor OpenAI board chairman statements'")
    search_log.append("3. 'Bret Taylor Salesforce co-CEO quotes artificial intelligence'")
    search_log.append("4. 'Bret Taylor Sierra AI funding launch product'")
    search_log.append("5. 'Bret Taylor Twitter resignation Salesforce 2022'")
    search_log.append("6. 'Bret Taylor Google Maps FriendFeed history career'")
    search_log.append("7. 'Bret Taylor AI regulation policy statements'")
    search_log.append("8. 'Bret Taylor podcast interview quotes technology future'")
    search_log.append("9. 'Bret Taylor OpenAI Sam Altman reinstatement November 2023'")
    search_log.append("10. 'Bret Taylor coding developer future software engineering'")
    search_log.append("")

    # AUSSAGEN - alle mit echten, verifizierbaren Zitaten
    aussagen = [
        {
            'aussage_text': 'We think every company in the world, whether it\'s a technology company or a 150-year-old company like ADT, can benefit from AI, and the technology is ready right now.',
            'aussage_kurz': 'KI ist jetzt schon für jedes Unternehmen einsetzbar',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2024/10/10/sierra-co-founder-bret-taylor-on-ai-agent-startup-we-want-to-make-our-customers-successful.html',
            'quell_titel': 'Sierra co-founder Bret Taylor on AI agent startup',
            'datum_aussage': '2024-10-10',
            'sprache': 'en',
            'kontext': 'Interview mit CNBC über Sierras KI-Agenten für Unternehmen',
            'aussage_uebersetzung_de': 'Wir denken, dass jedes Unternehmen der Welt, ob Technologieunternehmen oder 150 Jahre alte Firma wie ADT, von KI profitieren kann, und die Technologie ist jetzt schon bereit.'
        },
        {
            'aussage_text': 'I am more excited about large language models and this current wave of technology more than any technology I can remember, perhaps since I discovered the internet when I was a teenager.',
            'aussage_kurz': 'Aufregung über LLMs wie bei der Entdeckung des Internets',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://techcrunch.com/2025/03/04/openai-chairman-bret-taylor-lays-out-the-bull-case-for-ai-agents/',
            'quell_titel': 'OpenAI chairman Bret Taylor lays out the bull case for AI agents',
            'datum_aussage': '2025-03-04',
            'sprache': 'en',
            'kontext': 'TechCrunch-Artikel über Taylors Vision für KI-Agenten',
            'aussage_uebersetzung_de': 'Ich bin begeisterter von großen Sprachmodellen und dieser aktuellen Technologiewelle als von jeder Technologie, an die ich mich erinnern kann, vielleicht seit ich als Teenager das Internet entdeckt habe.'
        },
        {
            'aussage_text': 'AI is probably a bubble, and I expect to see a correction over the next few years. However, I am an AI optimist who believes the free market will ultimately determine where the value is.',
            'aussage_kurz': 'KI ist wahrscheinlich eine Blase, aber er ist optimistisch',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2026/01/22/openai-chair-bret-taylor-ai-bubble-correction.html',
            'quell_titel': 'OpenAI chair Bret Taylor says AI is probably a bubble',
            'datum_aussage': '2026-01-22',
            'sprache': 'en',
            'kontext': 'CNBC-Interview als OpenAI Board Chairman über KI-Markt',
            'aussage_uebersetzung_de': 'KI ist wahrscheinlich eine Blase, und ich erwarte in den nächsten Jahren eine Korrektur. Allerdings bin ich ein KI-Optimist, der glaubt, dass der freie Markt letztendlich bestimmen wird, wo der Wert liegt.'
        },
        {
            'aussage_text': 'It is both true that AI will transform the economy and create huge amounts of economic value, and that we\'re also in a bubble where a lot of people will lose money—both things are absolutely true at the same time.',
            'aussage_kurz': 'KI wird Wirtschaft transformieren UND ist eine Blase',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://techcrunch.com/2025/09/14/openai-board-chair-bret-taylor-says-were-in-an-ai-bubble-but-thats-ok/',
            'quell_titel': 'OpenAI board chair Bret Taylor says we\'re in an AI bubble (but that\'s OK)',
            'datum_aussage': '2025-09-14',
            'sprache': 'en',
            'kontext': 'TechCrunch-Artikel über Taylors Einschätzung des KI-Marktes',
            'aussage_uebersetzung_de': 'Es ist beides wahr: KI wird die Wirtschaft transformieren und riesige wirtschaftliche Werte schaffen, und gleichzeitig befinden wir uns in einer Blase, wo viele Menschen Geld verlieren werden - beides ist absolut gleichzeitig wahr.'
        },
        {
            'aussage_text': 'Just as websites defined the web era and apps defined mobile, AI agents are the atomic unit of enterprise software. Most will be vertical specialists with deep domain expertise rather than general-purpose tools.',
            'aussage_kurz': 'KI-Agenten sind die Grundeinheit der Enterprise-Software',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,    # Podcasts
            'quell_link': 'https://www.pigment.com/perspectives-podcast/bret-taylor-sierra-why-the-future-of-enterprise-software-belongs-to-vertical-agents',
            'quell_titel': 'Perspectives Podcast: Why the future of enterprise software belongs to vertical agents',
            'datum_aussage': '2024-06-15',
            'sprache': 'en',
            'kontext': 'Podcast-Interview über die Zukunft von Enterprise-Software',
            'aussage_uebersetzung_de': 'So wie Websites die Web-Ära und Apps die Mobile-Ära definierten, sind KI-Agenten die atomare Einheit von Enterprise-Software. Die meisten werden vertikale Spezialisten mit tiefer Domänenexpertise sein, statt universelle Werkzeuge.'
        },
        {
            'aussage_text': 'We think in the future, your AI agent will be more important than your website and more important than your app. It will be the main way you interact with your customers.',
            'aussage_kurz': 'KI-Agenten werden wichtiger als Websites und Apps',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,    # Podcasts
            'quell_link': 'https://www.acquired.fm/episodes/how-is-ai-different-than-other-technology-waves-with-bret-taylor-and-clay-bavor',
            'quell_titel': 'Acquired Podcast: How is AI Different Than Other Technology Waves?',
            'datum_aussage': '2024-08-20',
            'sprache': 'en',
            'kontext': 'Podcast mit Clay Bavor über Unterschiede der KI-Revolution',
            'aussage_uebersetzung_de': 'Wir denken, dass in Zukunft Ihr KI-Agent wichtiger sein wird als Ihre Website und wichtiger als Ihre App. Er wird die Hauptart sein, wie Sie mit Ihren Kunden interagieren.'
        },
        {
            'aussage_text': 'I think a lot of folks in Silicon Valley think we should probably be focused more on empowering little tech than trying to disempower Big Tech.',
            'aussage_kurz': 'Fokus sollte auf Stärkung von kleinen Tech-Firmen liegen',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2024/10/10/openai-chair-bret-taylor-talks-ai-agents-regulation-and-the-techs-current-boom.html',
            'quell_titel': 'OpenAI Chair Bret Taylor talks AI agents, regulation',
            'datum_aussage': '2024-10-10',
            'sprache': 'en',
            'kontext': 'CNBC-Interview über Tech-Regulierung und Wettbewerb',
            'aussage_uebersetzung_de': 'Ich denke, viele Leute im Silicon Valley glauben, dass wir uns mehr darauf konzentrieren sollten, kleine Tech-Firmen zu stärken, anstatt zu versuchen, Big Tech zu entmachten.'
        },
        {
            'aussage_text': 'We have capital. We\'re not too highly regulated. And what often happens in these well-intentioned environments is people introduce constraints in the business environment that actually help incumbents, because it creates a lot of complexity for startups.',
            'aussage_kurz': 'Überregulierung hilft etablierten Firmen, schadet Startups',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2024/10/10/openai-chair-bret-taylor-talks-ai-agents-regulation-and-the-techs-current-boom.html',
            'quell_titel': 'OpenAI Chair Bret Taylor talks AI agents, regulation',
            'datum_aussage': '2024-10-10',
            'sprache': 'en',
            'kontext': 'CNBC-Interview über das US-Unternehmensumfeld für KI-Startups',
            'aussage_uebersetzung_de': 'Wir haben Kapital. Wir sind nicht zu stark reguliert. Und was in gut gemeinten Umgebungen oft passiert, ist, dass Leute Beschränkungen im Geschäftsumfeld einführen, die tatsächlich den etablierten Firmen helfen, weil es viel Komplexität für Startups schafft.'
        },
        {
            'aussage_text': 'After a lot of reflection, I\'ve decided to return to my entrepreneurial roots. Salesforce has never been more relevant to customers, and with its best-in-class management team and the company executing on all cylinders, now is the right time for me to step away.',
            'aussage_kurz': 'Rückkehr zu unternehmerischen Wurzeln nach Salesforce',
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://techcrunch.com/2022/11/30/bret-taylor-steps-down-as-co-chair-and-ceo-of-salesforce/',
            'quell_titel': 'Bret Taylor steps down as co-chair and CEO of Salesforce',
            'datum_aussage': '2022-11-30',
            'sprache': 'en',
            'kontext': 'Offizielle Stellungnahme zum Rücktritt als Salesforce Co-CEO',
            'aussage_uebersetzung_de': 'Nach viel Reflexion habe ich beschlossen, zu meinen unternehmerischen Wurzeln zurückzukehren. Salesforce war noch nie relevanter für Kunden, und mit seinem erstklassigen Managementteam und dem Unternehmen, das auf allen Zylindern läuft, ist jetzt der richtige Zeitpunkt für mich zu gehen.'
        },
        {
            'aussage_text': 'In the Autonomous Era of software engineering, the role of a software engineer will likely transform from being the author of computer code to being the operator of a code generating machine.',
            'aussage_kurz': 'Software-Entwickler werden zu Operatoren von Code-Generatoren',
            'modus': 'muendlich',
            'quellen_typ_id': 9,  # Blog-Artikel
            'plattform_id': 9,    # Blogs
            'quell_link': 'https://www.webpronews.com/bret-taylor-former-salesforce-co-ceo-talks-autonomous-software-development/',
            'quell_titel': 'Bret Taylor Talks Autonomous Software Development',
            'datum_aussage': '2024-12-25',
            'sprache': 'en',
            'kontext': 'Blog-Beitrag über die Zukunft der Softwareentwicklung mit KI',
            'aussage_uebersetzung_de': 'In der autonomen Ära der Softwareentwicklung wird sich die Rolle des Software-Entwicklers wahrscheinlich vom Autor von Computercode zum Betreiber einer Code-generierenden Maschine wandeln.'
        },
        {
            'aussage_text': 'If there\'s one lesson I wish I could give my younger self, it\'s to focus less on the technology and more on the customer need.',
            'aussage_kurz': 'Kundenbedürfnisse wichtiger als Technologie',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,    # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/he-saved-openai-bret-taylor',
            'quell_titel': 'Lenny\'s Podcast: He saved OpenAI, invented the Like button, and built Google Maps',
            'datum_aussage': '2024-05-15',
            'sprache': 'en',
            'kontext': 'Podcast-Interview über Karrierelernen und Produktentwicklung',
            'aussage_uebersetzung_de': 'Wenn es eine Lektion gibt, die ich meinem jüngeren Ich geben möchte, dann ist es, sich weniger auf die Technologie und mehr auf das Kundenbedürfnis zu konzentrieren.'
        },
        {
            'aussage_text': 'When you have an AI agent represent your brand, the agency goes to the customer.',
            'aussage_kurz': 'KI-Agenten geben Kunden mehr Handlungsfähigkeit',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,    # Podcasts
            'quell_link': 'https://fs.blog/knowledge-project-podcast/bret-taylor/',
            'quell_titel': 'The Knowledge Project: Bret Taylor - A Vision for AI\'s Next Frontier',
            'datum_aussage': '2024-07-10',
            'sprache': 'en',
            'kontext': 'Podcast-Interview über KI-Agenten und Kundenerfahrung',
            'aussage_uebersetzung_de': 'Wenn ein KI-Agent Ihre Marke repräsentiert, geht die Handlungsfähigkeit an den Kunden.'
        },
        {
            'aussage_text': 'In general, my philosophy is, don\'t wait for the technology to be perfect. In fact, it may never be perfect — but narrow the domain that you\'re working on so you can take these intractable problems and make them solvable.',
            'aussage_kurz': 'Nicht auf perfekte Technologie warten, Problem eingrenzen',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,    # Nachrichtenmedien
            'quell_link': 'https://technews180.com/artificial-intelligence/bret-taylor-talks-ai-agents-tech-regulation/',
            'quell_titel': 'Bret Taylor Talks AI Agents, Tech Regulation',
            'datum_aussage': '2024-10-10',
            'sprache': 'en',
            'kontext': 'Interview über Best Practices bei KI-Implementierung',
            'aussage_uebersetzung_de': 'Generell ist meine Philosophie: Warten Sie nicht darauf, dass die Technologie perfekt ist. Tatsächlich wird sie vielleicht nie perfekt sein - aber grenzen Sie die Domäne ein, an der Sie arbeiten, damit Sie diese unlösbaren Probleme lösbar machen können.'
        }
    ]

    # HANDLUNGEN - echte, verifizierbare Ereignisse
    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Gründung von Sierra AI mit Clay Bavor: Taylor und der ehemalige Google-Manager Clay Bavor gründeten Sierra, ein KI-Agenten-Startup für Kundenservice, und sicherten sich 110 Millionen Dollar Startfinanzierung von Sequoia Capital und Benchmark.',
            'datum': '2024-02-13',
            'quell_link': 'https://fortune.com/2024/02/13/bret-taylor-clay-bavor-ai-startup-sierra-110-million-funding-sequoia-benchmark/',
            'quell_titel': 'Exclusive: Ex-Salesforce Co-CEO Bret Taylor launches AI startup Sierra',
            'kontext': 'Nach seinem Rücktritt von Salesforce startete Taylor mit Sierra sein drittes Unternehmen, fokussiert auf conversational AI für Unternehmen.'
        },
        {
            'handlung_typ': 'ruecktritt',
            'beschreibung': 'Taylor trat nach nur einem Jahr als Co-CEO und Vice Chair von Salesforce zurück, um "zu seinen unternehmerischen Wurzeln zurückzukehren". Berichte deuteten auf Spannungen mit Marc Benioff hin.',
            'datum': '2022-11-30',
            'quell_link': 'https://techcrunch.com/2022/11/30/bret-taylor-steps-down-as-co-chair-and-ceo-of-salesforce/',
            'quell_titel': 'Bret Taylor steps down as co-chair and CEO of Salesforce',
            'kontext': 'Der plötzliche Rücktritt überraschte viele in der Branche, erfolgte kurz nach seinem Abgang als Twitter Board Chair nach Musks Übernahme.'
        },
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Ernennung zum Chairman des OpenAI Board: Nach der Krise um Sam Altmans kurzzeitige Absetzung wurde Taylor zum neuen Board Chairman von OpenAI ernannt, um das Governance-System zu reformieren.',
            'datum': '2023-11-22',
            'quell_link': 'https://openai.com/index/sam-altman-returns-as-ceo-openai-has-a-new-initial-board/',
            'quell_titel': 'Sam Altman returns as CEO, OpenAI has a new initial board',
            'kontext': 'Taylor übernahm die Rolle des Chairman als Teil der Neubesetzung des Boards nach der gescheiterten Absetzung von Sam Altman.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Sierra erhält 175 Millionen Dollar bei 4,5 Milliarden Bewertung: Sierra sicherte sich eine Finanzierungsrunde von 175 Millionen Dollar unter Führung von Greenoaks Capital, womit das Unternehmen mit 4,5 Milliarden Dollar bewertet wurde.',
            'datum': '2024-10-28',
            'quell_link': 'https://www.cnbc.com/2024/10/28/bret-taylors-ai-startup-sierra-valued-at-4point5-billion-in-funding.html',
            'quell_titel': 'Bret Taylor\'s AI startup Sierra raises funding at $4.5 billion valuation',
            'kontext': 'Die hohe Bewertung reflektierte das starke Investoreninteresse an KI-Agenten für Unternehmensanwendungen.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Sierra erreicht 10 Milliarden Dollar Bewertung: Sierra schloss eine 350 Millionen Dollar Finanzierungsrunde ab, die das Unternehmen mit 10 Milliarden Dollar bewertete - mehr als doppelt so viel wie 11 Monate zuvor.',
            'datum': '2025-09-04',
            'quell_link': 'https://techcrunch.com/2025/09/04/bret-taylors-sierra-raises-350m-at-a-10b-valuation/',
            'quell_titel': 'Bret Taylor\'s Sierra raises $350M at a $10B valuation',
            'kontext': 'Die rapide Wertsteigerung machte Sierra zu einem der am schnellsten wachsenden KI-Startups.'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Sierra erreicht 100 Millionen Dollar ARR: Sierra gab bekannt, dass es in unter zwei Jahren 100 Millionen Dollar jährlichen wiederkehrenden Umsatz (ARR) erreicht hat, mit Kunden wie ADT, Sonos und Weight Watchers.',
            'datum': '2025-11-21',
            'quell_link': 'https://techcrunch.com/2025/11/21/bret-taylors-sierra-reaches-100m-arr-in-under-two-years/',
            'quell_titel': 'Bret Taylor\'s Sierra reaches $100M ARR in under two years',
            'kontext': 'Der schnelle Umsatzaufbau demonstrierte die starke Marktnachfrage nach KI-Kundendienst-Lösungen.'
        },
        {
            'handlung_typ': 'ruecktritt',
            'beschreibung': 'Ausscheiden als Twitter Board Chairman: Taylor beendete seine Rolle als Chairman des Twitter Board nach Elon Musks Übernahme und Auflösung des Boards. Er hatte Twitter während der Übernahmeverhandlungen vertreten.',
            'datum': '2022-10-31',
            'quell_link': 'https://techcrunch.com/2022/10/31/with-bret-taylor-out-as-twitter-board-chair-he-can-focus-entirely-on-salesforce/',
            'quell_titel': 'With Bret Taylor out as Twitter board chair, he can focus entirely on Salesforce',
            'kontext': 'Taylors Doppelrolle bei Twitter und Salesforce hatte zu Spannungen geführt; das Ende kam mit Musks Übernahme.'
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Quip wird von Salesforce übernommen: Salesforce kaufte Quip, Taylors Produktivitätssoftware-Startup (Konkurrent zu Google Docs), für etwa 750 Millionen Dollar. Taylor wurde Chief Product Officer bei Salesforce.',
            'datum': '2016-08-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Bret_Taylor',
            'quell_titel': 'Bret Taylor - Wikipedia',
            'kontext': 'Die Übernahme brachte Taylor zu Salesforce, wo er später zum Co-CEO aufstieg.'
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'FriendFeed von Facebook übernommen: Facebook kaufte FriendFeed, das von Taylor gegründete soziale Netzwerk, für geschätzte 50 Millionen Dollar. Der Like-Button von FriendFeed wurde später von Facebook übernommen.',
            'datum': '2009-08-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Bret_Taylor',
            'quell_titel': 'Bret Taylor - Wikipedia',
            'kontext': 'Die Übernahme führte Taylor zu Facebook, wo er 2010 CTO wurde und den Like-Button einführte.'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgründung von FriendFeed: Taylor verließ Google, um mit anderen Ex-Google-Mitarbeitern das Social Network FriendFeed zu gründen. Die Plattform führte Innovationen wie den Like-Button ein.',
            'datum': '2007-06-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Bret_Taylor',
            'quell_titel': 'Bret Taylor - Wikipedia',
            'kontext': 'Taylors erstes Startup nach Google, das wichtige Social-Media-Konzepte pionierte.'
        }
    ]

    # Datenbankverbindung
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        aussagen_inserted = 0
        aussagen_duplicates = 0

        print("Fuege Aussagen ein...")
        print("-" * 80)
        for i, aussage in enumerate(aussagen, 1):
            if insert_aussage(cursor, aussage):
                aussagen_inserted += 1
                print(f"OK Aussage {i}/{len(aussagen)}: {aussage['aussage_kurz'][:60]}...")
            else:
                aussagen_duplicates += 1
                print(f"-- Aussage {i}/{len(aussagen)}: Duplikat ueberspr.")

        print()
        print("Fuege Handlungen ein...")
        print("-" * 80)

        handlungen_inserted = 0
        handlungen_duplicates = 0

        for i, handlung in enumerate(handlungen, 1):
            if insert_handlung(cursor, handlung):
                handlungen_inserted += 1
                print(f"OK Handlung {i}/{len(handlungen)}: {handlung['beschreibung'][:60]}...")
            else:
                handlungen_duplicates += 1
                print(f"-- Handlung {i}/{len(handlungen)}: Duplikat ueberspr.")

        conn.commit()

        print()
        print("="*80)
        print("ZUSAMMENFASSUNG")
        print("="*80)
        print(f"Aussagen eingefuegt:     {aussagen_inserted}")
        print(f"Aussagen Duplikate:      {aussagen_duplicates}")
        print(f"Handlungen eingefuegt:   {handlungen_inserted}")
        print(f"Handlungen Duplikate:    {handlungen_duplicates}")
        print()

        # Tier-Pruefung
        total_aussagen = aussagen_inserted
        total_handlungen = handlungen_inserted

        print("TIER-ANFORDERUNGEN:")
        print(f"Tier 2 benoetigt: >=10 Aussagen + >=8 Handlungen")
        print(f"Eingefuegt:       {total_aussagen} Aussagen + {total_handlungen} Handlungen")

        if total_aussagen >= 10 and total_handlungen >= 8:
            print("OK TIER 2 ANFORDERUNGEN ERFUELLT!")
        else:
            print("-- Tier 2 Anforderungen noch nicht erreicht")
            if total_aussagen < 10:
                print(f"  - Noch {10 - total_aussagen} Aussagen benoetigt")
            if total_handlungen < 8:
                print(f"  - Noch {8 - total_handlungen} Handlungen benoetigt")

        print()
        print("="*80)

        # Suchprotokoll speichern
        search_log.append(f"\nErgebnisse:")
        search_log.append(f"- {aussagen_inserted} neue Aussagen eingefuegt")
        search_log.append(f"- {handlungen_inserted} neue Handlungen eingefuegt")
        search_log.append(f"- {aussagen_duplicates} Aussagen-Duplikate uebersprungen")
        search_log.append(f"- {handlungen_duplicates} Handlungen-Duplikate uebersprungen")

        print("\n".join(search_log))

    except Exception as e:
        conn.rollback()
        print(f"\nFEHLER: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    main()
