# -*- coding: utf-8 -*-
"""
Datensammlung für Masayoshi Son (Person ID 16)
SoftBank CEO, Tech-Investor, KI-Visionär
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 16

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Mapping für Quellen-Typen (quellen_typen Tabelle)
    # 1=Video-Interview, 2=Podcast-Interview, 3=Keynote/Vortrag, 4=Panel-Diskussion
    # 5=Social-Media-Post, 6=Blog-Artikel, 7=Nachrichtenartikel, 8=Buch
    # 9=Wissenschaftlicher Artikel, 10=Offizielle Stellungnahme, 11=AMA/Q&A

    # ==================== AUSSAGEN ====================
    aussagen = [
        {
            'aussage_text': 'I was born to realize ASI. What is my belief and vision for this investment? I have only one belief — Singularity.',
            'datum_aussage': '2024-06-21',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank Annual General Shareholders Meeting in Tokyo, erklärte sein Lebenswerk als Realisierung von Artificial Super Intelligence',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'AI that is 10,000 times smarter than humans will be here in 10 years. By 2030, AI could be one to 10 times smarter than humans, and by 2035, it might be 10,000 times smarter than human intelligence.',
            'datum_aussage': '2024-06-21',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank AGM 2024, Prognose zur Entwicklung übermenschlicher Intelligenz',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'We believe the singularity is inevitable, and all businesses will be redefined as computers overtake humans in intelligence.',
            'datum_aussage': '2017-09-20',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'CNBC Interview, warnte vor der Singularität und deren transformativer Wirkung auf alle Branchen',
            'modus': 'muendlich'
        },
        {
            'aussage_text': '30 years from now, the number of smart robots, the smart robot population on this earth will be 10 billion. By that time, human population will be around 10 billion. So here on this earth we will have 10 billion population of mankind and 10 billion population of smart robots.',
            'datum_aussage': '2017-09-20',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Präsentation zur Zukunftsvision, Prognose einer Welt mit gleich vielen intelligenten Robotern wie Menschen',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Every industry that mankind created will be redefined. The medical industry, automobile industry, the information industry of course. Every industry that mankind ever defined and created, even agriculture, will be redefined.',
            'datum_aussage': '2017-09-20',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Vision zur umfassenden Transformation aller Branchen durch KI',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'In the future, cancer will no longer be a disease we should be afraid of, because artificial intelligence will solve problems that we cannot solve.',
            'datum_aussage': '2018-06-20',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank Shareholder Meeting, optimistische Vision über KI-basierte Medizin',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'I think this superintelligence is going to be our partner.',
            'datum_aussage': '2024-06-27',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'Fortune Interview, betonte Partnerschaft-Vision zwischen Mensch und ASI',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'In 300 years, we would like to become that company that makes the most contribution to human evolution -- the company that has greatest impact on humanity.',
            'datum_aussage': '2010-06-25',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank Shareholder Meeting, präsentierte seinen berühmten 300-Jahres-Plan',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'In 300 years time, chips planted inside or on our bodies will allow humans to communicate with one another, in any language, via telepathy. People will be able to communicate telepathically with dogs.',
            'datum_aussage': '2010-06-25',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': '133-seitige Präsentation in Tokyo, Vision von Telepathie durch Gehirn-Chips',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'SoftBank might not be a mobile phone company anymore, but instead could be a telepathy service provider.',
            'datum_aussage': '2010-06-25',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Teil des 300-Jahres-Plans, Zukunftsvision des Geschäftsmodells',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'The future of Artificial Super Intelligence requires breakthrough computing power.',
            'datum_aussage': '2025-03-19',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'kontext': 'Ankündigung der Ampere Computing Übernahme für 6,5 Mrd. USD',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'The Singularity will happen by 2047.',
            'datum_aussage': '2017-10-25',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Technologie-Konferenz, spezifische Vorhersage des Singularitäts-Zeitpunkts',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'I am devoting 97% of my time and brain to driving the future of AI.',
            'datum_aussage': '2024-06-21',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank AGM 2024, persönliches Commitment zur KI-Entwicklung',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Artificial general intelligence will come within 10 years.',
            'datum_aussage': '2023-10-04',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'CNN Business Interview, AGI-Prognose für 2030er Jahre',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'AGI will arrive in 2-3 years.',
            'datum_aussage': '2025-02-01',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Aktualisierte Prognose für AGI-Zeitpunkt (2027-2028)',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'I want SoftBank to become the world\'s leading Artificial Super Intelligence platform within ten years.',
            'datum_aussage': '2024-06-21',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'SoftBank AGM 2024, strategische Vision für das Unternehmen',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Everything inspired by the corporate philosophy: Information Revolution — Happiness for everyone.',
            'datum_aussage': '2021-06-23',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Erklärung der Unternehmensphilosophie trotz häufiger Geschäftsmodell-Wechsel',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'I want to be the 21st century Rothschild.',
            'datum_aussage': '2021-06-23',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'CNBC Bericht über SoftBank AGM, verglich seine Investmentrolle mit historischen Finanziers',
            'modus': 'muendlich'
        }
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, datum_aussage, quellen_typ_id, kontext, modus, einschluss)
            VALUES (?, ?, ?, ?, ?, ?, 1)
        """, (PERSON_ID, aussage['aussage_text'], aussage['datum_aussage'],
              aussage['quellen_typ_id'], aussage['kontext'], aussage['modus']))

    print(f"{len(aussagen)} Aussagen eingefügt.")

    # ==================== HANDLUNGEN ====================
    handlungen = [
        {
            'handlung_typ': 'kauf',
            'beschreibung': 'ARM Holdings Übernahme - Kauf des britischen Chip-Designers für Vorbereitung auf KI-Revolution und IoT-Ära',
            'datum_handlung': '2016-09-05',
            'betrag_usd': 32000000000
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'SoftBank Vision Fund - Gründung des weltweit größten Tech-Investmentfonds mit Fokus auf KI, Robotik und IoT',
            'datum_handlung': '2017-05-20',
            'betrag_usd': 100000000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Alibaba frühe Investition - 34% Stake für 20 Mio. USD, später über 200 Mrd. USD wert (eine der erfolgreichsten Tech-Investments aller Zeiten)',
            'datum_handlung': '2000-01-20',
            'betrag_usd': 20000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'WeWork Investment durch Vision Fund - massive Investition in Co-Working Startup (später 14 Mrd. USD Abschreibung)',
            'datum_handlung': '2017-08-25',
            'betrag_usd': 4400000000
        },
        {
            'handlung_typ': 'kauf',
            'beschreibung': 'Aldebaran Robotics Übernahme (später SoftBank Robotics) - Entwicklung des humanoiden Roboters Pepper',
            'datum_handlung': '2013-03-15',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Pepper Roboter Launch - humanoider Roboter für Kundeninteraktion, Co-Design mit Aldebaran',
            'datum_handlung': '2014-06-05',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Nvidia Stake Verkauf - Verkauf der gesamten 4.9% Nvidia Position (später als großer strategischer Fehler bezeichnet, Son "was crying")',
            'datum_handlung': '2019-02-28',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Vision Fund US Portfolio Abbau - Verkauf/Abschreibung von 29 Mrd. USD in US-Aktien (Coupang, DoorDash, Grab) für Pivot zu KI/Chips',
            'datum_handlung': '2024-05-10',
            'betrag_usd': 29000000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Project Izanagi Ankündigung - geplante 100 Mrd. USD AI Chip Venture zum Nvidia-Wettbewerb (Name spielt auf AGI an)',
            'datum_handlung': '2024-02-19',
            'betrag_usd': 100000000000
        },
        {
            'handlung_typ': 'kauf',
            'beschreibung': 'Ampere Computing Übernahme - Erwerb des ARM-basierten Server-Chip Designers für ASI-Computing-Power',
            'datum_handlung': '2025-11-25',
            'betrag_usd': 6500000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'OpenAI Investment Commitment - bis zu 40 Mrd. USD Gesamtverpflichtung, Teil von Project Stargate',
            'datum_handlung': '2025-03-15',
            'betrag_usd': 40000000000
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Project Stargate Ankündigung mit Trump - 500 Mrd. USD KI-Infrastruktur Initiative (SoftBank Chairman), 100k Jobs',
            'datum_handlung': '2025-01-21',
            'betrag_usd': 500000000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'OpenAI Vision Fund 2 Investment - 22,5 Mrd. USD durch SVF2 (dritte Tranche, effektiv 30 Mrd. nach Syndizierung)',
            'datum_handlung': '2025-10-15',
            'betrag_usd': 22500000000
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Nvidia Komplett-Ausstieg - Verkauf aller verbliebenen 32,1 Mio. Nvidia Aktien für Fokus auf eigene AI-Infrastruktur',
            'datum_handlung': '2025-11-11',
            'betrag_usd': 5830000000
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Wayve autonomous driving Investment - 1,05 Mrd. USD Finanzierungsrunde für UK Self-Driving Startup (mit Nvidia, Microsoft)',
            'datum_handlung': '2024-05-07',
            'betrag_usd': 1050000000
        }
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, betrag_usd)
            VALUES (?, ?, ?, ?, ?)
        """, (PERSON_ID, handlung['handlung_typ'], handlung['beschreibung'],
              handlung['datum_handlung'], handlung['betrag_usd']))

    print(f"{len(handlungen)} Handlungen eingefügt.")

    conn.commit()
    conn.close()

    print(f"\n[OK] Datensammlung fuer Masayoshi Son abgeschlossen!")
    print(f"[OK] {len(aussagen)} Aussagen (Ziel: >=15)")
    print(f"[OK] {len(handlungen)} Handlungen (Ziel: >=12)")
    print(f"[OK] Zeitraum: 2000-2025")

if __name__ == "__main__":
    insert_data()
