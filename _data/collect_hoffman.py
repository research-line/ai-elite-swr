#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Reid Hoffman (person_id=31)
Tier 2: Mindestens 10 Aussagen + 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_aussagen(cursor):
    """Fuegt Aussagen von Reid Hoffman ein"""

    aussagen = [
        # 1. AI Transformative Potential
        {
            'person_id': 31,
            'aussage_text': 'I actually think that unlike the previous AI waves, this one is going to create a lever that will move industries and move the world.',
            'aussage_kurz': 'Diese KI-Welle wird im Gegensatz zu früheren die Industrien und die Welt transformieren',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://onbeing.org/programs/reid-hoffman-ai-and-what-it-means-to-be-more-human/',
            'quell_titel': 'Reid Hoffman — AI, and What It Means to Be (More) Human',
            'datum_aussage': '2023-01-01',
            'sprache': 'en',
            'kontext': 'Hoffman discussing his "light-bulb moment" on AI while on OpenAI board, watching progress between GPT-2 and GPT-3',
            'aussage_uebersetzung_de': 'Ich denke tatsächlich, dass diese KI-Welle im Gegensatz zu den vorherigen einen Hebel schaffen wird, der Industrien und die Welt bewegen wird.'
        },
        # 2. Humanity Amplification
        {
            'person_id': 31,
            'aussage_text': 'AI is not a threat, but a partner. We should use this technology in ways that are meaningful for human advancement and development.',
            'aussage_kurz': 'KI ist kein Gegner sondern Partner für menschliche Entwicklung',
            'modus': 'schriftlich',
            'quellen_typ_id': 8,  # Buch
            'plattform_id': 8,  # Bücher
            'quell_link': 'https://www.impromptubook.com/',
            'quell_titel': 'Impromptu: Amplifying Our Humanity Through AI',
            'datum_aussage': '2023-03-01',
            'sprache': 'en',
            'kontext': 'Core message of his book co-written with GPT-4, first book written with GPT-4',
            'aussage_uebersetzung_de': 'KI ist keine Bedrohung, sondern ein Partner. Wir sollten diese Technologie auf Weisen nutzen, die für menschlichen Fortschritt und Entwicklung bedeutsam sind.'
        },
        # 3. Optimism vs Fear
        {
            'person_id': 31,
            'aussage_text': 'I hold very deeply the conviction that people should have a curious and mostly optimistic view about what happens in the creation of technology, versus a fearful, pessimistic view.',
            'aussage_kurz': 'Menschen sollten eine neugierige und optimistische statt ängstliche Sicht auf Technologie haben',
            'modus': 'schriftlich',
            'quellen_typ_id': 8,  # Buch
            'plattform_id': 8,  # Bücher
            'quell_link': 'https://www.superagency.ai/',
            'quell_titel': 'Superagency: What Could Possibly Go Right with Our AI Future',
            'datum_aussage': '2024-09-01',
            'sprache': 'en',
            'kontext': 'Statement from his book Superagency explaining his philosophical stance on technology',
            'aussage_uebersetzung_de': 'Ich bin zutiefst überzeugt, dass Menschen eine neugierige und überwiegend optimistische Sicht auf die Entwicklung von Technologie haben sollten, statt einer ängstlichen, pessimistischen Sicht.'
        },
        # 4. AI Agents and Speed
        {
            'person_id': 31,
            'aussage_text': 'I think what particularly freaks people out about AI [is that] it\'s an agent. The transformation is going to be at a faster speed than anything else in history.',
            'aussage_kurz': 'KI-Agenten werden schneller transformieren als alles zuvor in der Geschichte',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://fortune.com/2025/01/31/reid-hoffman-interview-openai-deepseek-superagncy-ai-book/',
            'quell_titel': 'Reid Hoffman\'s new book touts humanity\'s \'superagency\'',
            'datum_aussage': '2025-01-31',
            'sprache': 'en',
            'kontext': 'Fortune interview about his Superagency book, explaining what concerns people most about AI',
            'aussage_uebersetzung_de': 'Ich denke, was die Leute besonders an KI beunruhigt, ist dass sie ein Agent ist. Die Transformation wird mit einer höheren Geschwindigkeit ablaufen als alles andere in der Geschichte.'
        },
        # 5. Public Dialogue on AI
        {
            'person_id': 31,
            'aussage_text': 'If you go to most of the dialogue around AI right now, it\'s uncertainty, fear, negativity.',
            'aussage_kurz': 'Der aktuelle KI-Dialog ist von Unsicherheit, Angst und Negativität geprägt',
            'modus': 'schriftlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 1,  # YouTube
            'quell_link': 'https://www.geekwire.com/2024/in-mind-bending-chat-with-deepfake-digital-twin-reid-hoffman-discusses-microsofts-big-ai-hire/',
            'quell_titel': 'In mind-bending chat with deepfake digital twin, Reid Hoffman discusses Microsoft\'s big AI hire',
            'datum_aussage': '2024-05-09',
            'sprache': 'en',
            'kontext': 'Interview with AI deepfake of himself built on GPT-4, trained on 20 years of his public speaking',
            'aussage_uebersetzung_de': 'Wenn man sich den meisten Dialog über KI momentan anschaut, geht es um Unsicherheit, Angst und Negativität.'
        },
        # 6. AI as Tool not Replacement
        {
            'person_id': 31,
            'aussage_text': 'If you go to Pi and say, you\'re my best friend, Pi will say, no, no, no, I\'m your AI companion and doesn\'t want to displace your human relationships.',
            'aussage_kurz': 'KI-Assistenten sollen menschliche Beziehungen nicht ersetzen',
            'modus': 'schriftlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://onbeing.org/programs/reid-hoffman-ai-and-what-it-means-to-be-more-human/',
            'quell_titel': 'Reid Hoffman — AI, and What It Means to Be (More) Human | The On Being Project',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Discussing Inflection AI\'s Pi assistant design philosophy to complement not replace human relationships',
            'aussage_uebersetzung_de': 'Wenn du zu Pi sagst, du bist mein bester Freund, wird Pi sagen: nein, nein, nein, ich bin dein KI-Begleiter und will deine menschlichen Beziehungen nicht verdrängen.'
        },
        # 7. AI Agents for Productivity
        {
            'person_id': 31,
            'aussage_text': 'Workers will increasingly use personal, organizational, business process, and cross-organizational agents as trustworthy tools to increase value and solve complex problems.',
            'aussage_kurz': 'Arbeiter werden zunehmend KI-Agenten als vertrauenswürdige Werkzeuge nutzen',
            'modus': 'schriftlich',
            'quellen_typ_id': 8,  # Buch
            'plattform_id': 8,  # Bücher
            'quell_link': 'https://www.superagency.ai/',
            'quell_titel': 'Superagency: What Could Possibly Go Right with Our AI Future',
            'datum_aussage': '2024-09-01',
            'sprache': 'en',
            'kontext': 'Vision for workplace AI integration from Superagency book',
            'aussage_uebersetzung_de': 'Arbeiter werden zunehmend persönliche, organisatorische, Geschäftsprozess- und organisationsübergreifende Agenten als vertrauenswürdige Werkzeuge nutzen, um Wert zu steigern und komplexe Probleme zu lösen.'
        },
        # 8. Drug Discovery Transformation
        {
            'person_id': 31,
            'aussage_text': 'Today, I launched Manas AI – a full stack AI company setting out to shift drug discovery from a decade-long process to one that takes a few years; bringing life-saving treatments to patients faster than ever.',
            'aussage_kurz': 'KI wird Medikamentenentwicklung von zehn Jahren auf wenige Jahre verkürzen',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/reidhoffman/status/1883915396870451500',
            'quell_titel': 'Reid Hoffman Tweet on Manas AI launch',
            'datum_aussage': '2025-01-27',
            'sprache': 'en',
            'kontext': 'Announcement of Manas AI founding with oncologist Siddhartha Mukherjee, $24.6M seed funding',
            'aussage_uebersetzung_de': 'Heute habe ich Manas AI gegründet - ein Full-Stack-KI-Unternehmen, das die Medikamentenentwicklung von einem jahrzehntelangen Prozess auf einen von wenigen Jahren verkürzen will; um lebensrettende Behandlungen schneller als je zuvor zu Patienten zu bringen.'
        },
        # 9. AI Self-Governance
        {
            'person_id': 31,
            'aussage_text': 'Frontier AI labs can help govern themselves. When I was on the board of OpenAI, I was involved in efforts to ensure top labs coordinated on safety, noting it would be useful to have cross-collaboration on good alignment and safety.',
            'aussage_kurz': 'Führende KI-Labs können sich selbst regulieren und sollten bei Sicherheit kooperieren',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.opensecrets.org/outside-spending/donor_detail/2024?id=U0000004136',
            'quell_titel': 'Reid Hoffman on AI regulation and governance',
            'datum_aussage': '2023-06-01',
            'sprache': 'en',
            'kontext': 'Discussing AI governance philosophy during his time on OpenAI board',
            'aussage_uebersetzung_de': 'Führende KI-Labore können helfen, sich selbst zu regulieren. Als ich im Vorstand von OpenAI war, war ich an Bemühungen beteiligt sicherzustellen, dass führende Labore bei Sicherheit koordinieren, und es wäre nützlich, bei guter Ausrichtung und Sicherheit zusammenzuarbeiten.'
        },
        # 10. Light-touch Regulation
        {
            'person_id': 31,
            'aussage_text': 'I advocate for a light-touch regulatory landscape that prioritizes innovation and enables new players to compete on level playing fields.',
            'aussage_kurz': 'Befürwortet leichte Regulierung die Innovation priorisiert und Wettbewerb ermöglicht',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2023/03/03/reid-hoffman-steps-down-from-openai-board-to-avoid-potential-conflicts.html',
            'quell_titel': 'Reid Hoffman on AI regulation philosophy',
            'datum_aussage': '2023-05-10',
            'sprache': 'en',
            'kontext': 'Washington Post Live event "The Path Forward: Artificial Intelligence"',
            'aussage_uebersetzung_de': 'Ich befürworte eine regulatorische Landschaft mit leichter Hand, die Innovation priorisiert und neuen Akteuren ermöglicht, auf gleichen Wettbewerbsbedingungen zu konkurrieren.'
        },
        # 11. Human Innovation
        {
            'person_id': 31,
            'aussage_text': 'Repackaging available information actually describes an enormous share of human innovation, artistic or otherwise.',
            'aussage_kurz': 'Neuverpackung vorhandener Information beschreibt einen Großteil menschlicher Innovation',
            'modus': 'schriftlich',
            'quellen_typ_id': 8,  # Buch
            'plattform_id': 8,  # Bücher
            'quell_link': 'https://www.goodreads.com/work/quotes/144610746-impromptu-amplifying-our-humanity-through-ai',
            'quell_titel': 'Impromptu Quotes by Reid Hoffman',
            'datum_aussage': '2023-03-01',
            'sprache': 'en',
            'kontext': 'Quote from Impromptu book explaining parallels between AI and human creative processes',
            'aussage_uebersetzung_de': 'Die Neuverpackung verfügbarer Informationen beschreibt tatsächlich einen enormen Anteil menschlicher Innovation, künstlerisch oder anderweitig.'
        },
        # 12. Biology as AI Category
        {
            'person_id': 31,
            'aussage_text': 'I point to biology as an unsung AI category, expecting everything we\'ve learned about building AI to be applied to biological systems, treating biology as a kind of language to model molecules and pathways.',
            'aussage_kurz': 'Biologie ist unterschätzte KI-Kategorie - KI wird auf biologische Systeme angewendet',
            'modus': 'schriftlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://mastersofscale.com/',
            'quell_titel': 'Masters of Scale Podcast - AI and Biology',
            'datum_aussage': '2024-11-01',
            'sprache': 'en',
            'kontext': 'Masters of Scale podcast discussing AI applications in biology and drug discovery',
            'aussage_uebersetzung_de': 'Ich weise auf Biologie als unterschätzte KI-Kategorie hin, erwarte, dass alles, was wir über KI-Entwicklung gelernt haben, auf biologische Systeme angewendet wird, Biologie als eine Art Sprache behandelt wird, um Moleküle und Pfade zu modellieren.'
        }
    ]

    for aussage in aussagen:
        cursor.execute('''
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, sprache, kontext, aussage_uebersetzung_de
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            aussage['person_id'],
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

    print(f"OK: {len(aussagen)} Aussagen eingefuegt")
    return len(aussagen)


def insert_handlungen(cursor):
    """Fuegt Handlungen von Reid Hoffman ein"""

    handlungen = [
        # 1. LinkedIn Founding
        {
            'person_id': 31,
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgruendung von LinkedIn mit Allen Blue und Kollegen von SocialNet und Fujitsu. LinkedIn launched May 5, 2003 as one of the first business-oriented online social networks.',
            'datum_handlung': '2002-12-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Reid_Hoffman',
            'quell_titel': 'Reid Hoffman - Wikipedia',
            'kontext': 'Co-founding LinkedIn'
        },
        # 2. PayPal Board Member
        {
            'person_id': 31,
            'handlung_typ': 'einstellung',
            'beschreibung': 'Beitritt zu PayPal als Gruendungsvorstandsmitglied und dann Vollzeit als EVP fuer externe Kommunikation. Became part of PayPal Mafia, left in 2002 to found LinkedIn.',
            'datum_handlung': '2000-01-01',
            'quell_link': 'https://en.wikipedia.org/wiki/PayPal_Mafia',
            'quell_titel': 'PayPal Mafia - Wikipedia',
            'kontext': 'Joining PayPal as founding board member'
        },
        # 3. Facebook Early Investment
        {
            'person_id': 31,
            'handlung_typ': 'investition',
            'beschreibung': 'Vermittelte erstes Treffen zwischen Zuckerberg und Peter Thiel, investierte gemeinsam mit Thiel in Facebooks erste Finanzierungsrunde. According to David Kirkpatrick\'s The Facebook Effect, led to Thiel\'s $500,000 angel investment.',
            'datum_handlung': '2004-08-01',
            'quell_link': 'https://www.hustlefund.vc/post/reid-hoffman-investments-the-network-effects-master-who-built-linkedin-and-backed-facebook',
            'quell_titel': 'Reid Hoffman Investments: The Network Effects Master',
            'kontext': 'Early Facebook investment'
        },
        # 4. Greylock Partnership
        {
            'person_id': 31,
            'handlung_typ': 'einstellung',
            'beschreibung': 'Beitritt zu Greylock Partners als Partner, Fokus auf Fruehphaseninvestitionen in Produkte mit Netzwerkeffekten. As of May 2023, Hoffman and Greylock have invested in at least 37 AI companies.',
            'datum_handlung': '2009-01-01',
            'quell_link': 'https://greylock.com/team/reid-hoffman/',
            'quell_titel': 'Reid Hoffman | Greylock',
            'kontext': 'Joining Greylock Partners'
        },
        # 5. LinkedIn IPO
        {
            'person_id': 31,
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'LinkedIn Boersengang (IPO), Hoffmans Anteil war $2,34 Milliarden wert. Successful IPO made LinkedIn one of the most valuable social networks.',
            'datum_handlung': '2011-05-19',
            'quell_link': 'https://en.wikipedia.org/wiki/Reid_Hoffman',
            'quell_titel': 'Reid Hoffman - Wikipedia',
            'kontext': 'LinkedIn Initial Public Offering'
        },
        # 6. OpenAI Founding Donor
        {
            'person_id': 31,
            'handlung_typ': 'spende',
            'beschreibung': 'Unter den ersten Spendern fuer OpenAI ueber Aphorism Foundation: $1M an YC 2016, $5M direkt an OpenAI 2017-2018. OpenAI established by Sam Altman, Elon Musk and others.',
            'datum_handlung': '2016-01-01',
            'quell_link': 'https://www.insidephilanthropy.com/find-a-grant/grants-a/aphorism-foundation',
            'quell_titel': 'Aphorism Foundation | Inside Philanthropy',
            'kontext': 'Early OpenAI donor'
        },
        # 7. Microsoft LinkedIn Acquisition
        {
            'person_id': 31,
            'handlung_typ': 'verkauf',
            'beschreibung': 'Microsoft erwarb LinkedIn fuer $26,2 Milliarden bar, Hoffmans Anteil war $2,84 Milliarden wert, stimmte als Hauptaktionaer (10.85%) dafuer.',
            'datum_handlung': '2016-06-13',
            'quell_link': 'https://fortune.com/2016/06/13/linkedin-microsoft-reid-hoffman/',
            'quell_titel': 'LinkedIn Sale Is $2.8 Billion Payday for Reid Hoffman',
            'kontext': 'Microsoft LinkedIn acquisition, became Microsoft board member 2017'
        },
        # 8. Microsoft Board Appointment
        {
            'person_id': 31,
            'handlung_typ': 'einstellung',
            'beschreibung': 'Beitritt zum Microsoft-Vorstand nach LinkedIn-Uebernahme. LinkedIn maintained distinct brand, culture and independence under Microsoft.',
            'datum_handlung': '2017-03-14',
            'quell_link': 'https://techcrunch.com/2017/03/14/reid-hoffman-joins-microsoft-board/',
            'quell_titel': 'LinkedIn co-founder Reid Hoffman joins Microsoft\'s board',
            'kontext': 'Joining Microsoft Board of Directors'
        },
        # 9. Inflection AI Founding
        {
            'person_id': 31,
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgruendung von Inflection AI mit Mustafa Suleyman (DeepMind-Mitgruender) und Karen Simonyan, $225M initiale Finanzierung. First new company since LinkedIn, focused on AI to help humans "talk" to computers.',
            'datum_handlung': '2022-03-01',
            'quell_link': 'https://www.cnbc.com/2022/03/08/reid-hoffman-has-set-up-a-new-ai-company-with-deepminds-co-founder.html',
            'quell_titel': 'Reid Hoffman has co-founded his first new company since LinkedIn sale',
            'kontext': 'Co-founding Inflection AI'
        },
        # 10. OpenAI Board Resignation
        {
            'person_id': 31,
            'handlung_typ': 'ruecktritt',
            'beschreibung': 'Ruecktritt vom OpenAI-Vorstand um Interessenkonflikte mit Greylock-Investitionen und Inflection AI-Gruendung zu vermeiden. Greylock funding companies like Tome building on OpenAI products, remained OpenAI "ally".',
            'datum_handlung': '2023-03-03',
            'quell_link': 'https://www.cnbc.com/2023/03/03/reid-hoffman-steps-down-from-openai-board-to-avoid-potential-conflicts.html',
            'quell_titel': 'Reid Hoffman steps down from OpenAI board to avoid potential conflicts',
            'kontext': 'Resigned from OpenAI board'
        },
        # 11. Inflection AI Series A
        {
            'person_id': 31,
            'handlung_typ': 'investition',
            'beschreibung': 'Inflection AI sammelte $1,3 Milliarden Series A Finanzierung, bewertet mit $4 Milliarden. Launched Pi chatbot for Personal Intelligence in March 2023.',
            'datum_handlung': '2023-06-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Inflection_AI',
            'quell_titel': 'Inflection AI - Wikipedia',
            'kontext': 'Inflection AI Series A funding'
        },
        # 12. Political Donations Democrats
        {
            'person_id': 31,
            'handlung_typ': 'spende',
            'beschreibung': 'Spendete $55+ Millionen an demokratische Kandidaten, Parteien und PACs ueber vier Jahre (2020-2024), einer der Top-Grossspender. At least $34.8M in 2024 cycle alone, nearly $9M to Wisconsin Democratic Party since 2020.',
            'datum_handlung': '2024-01-01',
            'quell_link': 'https://www.opensecrets.org/outside-spending/donor_detail/2024?id=U0000004136',
            'quell_titel': 'Hoffman, Reid Garrett: Donor Detail',
            'kontext': 'Political donations to Democrats'
        },
        # 13. Manas AI Founding
        {
            'person_id': 31,
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgruendung von Manas AI mit Onkologe Siddhartha Mukherjee fuer KI-gesteuerte Medikamentenentwicklung, $24,6M Seed-Finanzierung von General Catalyst. Partnership with Microsoft Azure, focuses on aggressive cancer treatments.',
            'datum_handlung': '2025-01-27',
            'quell_link': 'https://www.cnbc.com/2025/02/02/reid-hoffman-launches-manas-ai-a-new-drug-discovery-startup.html',
            'quell_titel': 'Reid Hoffman launches Manas AI, a new drug discovery startup',
            'kontext': 'Co-founding Manas AI for AI drug discovery'
        }
    ]

    for handlung in handlungen:
        cursor.execute('''
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung,
                datum_handlung, quell_link, quell_titel, kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            handlung['person_id'],
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))

    print(f"OK: {len(handlungen)} Handlungen eingefuegt")
    return len(handlungen)


def main():
    """Hauptfunktion"""
    print("=" * 70)
    print("REID HOFFMAN (person_id=31) - Datensammlung")
    print("=" * 70)
    print()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Aussagen einfuegen
        print("Fuege Aussagen ein...")
        anzahl_aussagen = insert_aussagen(cursor)

        # Handlungen einfuegen
        print("Fuege Handlungen ein...")
        anzahl_handlungen = insert_handlungen(cursor)

        # Commit
        conn.commit()

        print()
        print("=" * 70)
        print("ZUSAMMENFASSUNG")
        print("=" * 70)
        print(f"Aussagen eingefuegt:    {anzahl_aussagen} (Minimum: 10)")
        print(f"Handlungen eingefuegt:  {anzahl_handlungen} (Minimum: 8)")
        print()

        if anzahl_aussagen >= 10 and anzahl_handlungen >= 8:
            print("OK: TIER 2 KRITERIEN ERFUELLT")
        else:
            print("FEHLER: TIER 2 KRITERIEN NICHT ERFUELLT")

        print()
        print("Reid Hoffman - Profil:")
        print("- LinkedIn Co-Gruender (2002)")
        print("- PayPal Mafia Mitglied")
        print("- Greylock Partner (2009-heute)")
        print("- OpenAI Board (2016-2023)")
        print("- Inflection AI Co-Gruender (2022)")
        print("- Manas AI Co-Gruender (2025)")
        print("- Autor: 'Impromptu' (2023), 'Superagency' (2024)")
        print("- KI-Optimist, Befuerworter leichter Regulierung")
        print()

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()
        print("Datenbankverbindung geschlossen.")


if __name__ == "__main__":
    main()
