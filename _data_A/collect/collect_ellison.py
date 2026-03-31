#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Larry Ellison (id=7)
Mitgründer und CTO von Oracle, KI-Infrastruktur-Investitionen
Zeitraum: 2012-2026
"""

import sqlite3
from datetime import datetime
import sys

# UTF-8 Ausgabe erzwingen
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person-ID für Larry Ellison
PERSON_ID = 7

def insert_data():
    """Fügt Aussagen und Handlungen von Larry Ellison in die Datenbank ein"""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN
    aussagen = [
        {
            'person_id': PERSON_ID,
            'aussage_text': 'AI changes everything. This is the largest, fastest-growing business in human history. It is bigger than the industrial revolution.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 Keynote',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Every police officer is going to be supervised at all times, and if there\'s a problem, AI will report that problem. Citizens will be on their best behavior because we are constantly recording and reporting everything that\'s going on.',
            'datum_aussage': '2024-09-12',
            'kontext': 'Oracle financial analysts meeting - Aussage zu AI-gestützter Massenüberwachung',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'AI will help us solve problems we couldn\'t solve on our own. It will make us much better scientists, engineers, teachers, chefs, bricklayers, surgeons, and what have you. I don\'t think AI will replace all human endeavors.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Vision für AI und menschliche Arbeit',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'I would describe the dinner as Oracle—me and Elon begging Jensen for GPUs. Please take our money. Please take our money. By the way, I got dinner. No, no, take more of it. We need you to take more of our money please.',
            'datum_aussage': '2024-09-16',
            'kontext': 'Beschreibung eines Abendessens mit Elon Musk und Jensen Huang (NVIDIA CEO) im Nobu Palo Alto, um mehr GPUs zu erhalten',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Once cancer tumors are gene-sequenced, AI can design a vaccine for every individual person to vaccinate them against that cancer, and can make that mRNA vaccine robotically using AI in about 48 hours. This is the promise of AI and the promise of the future.',
            'datum_aussage': '2025-01-21',
            'kontext': 'White House Ankündigung des Stargate AI Projekts - Vision für personalisierte Krebsimpfstoffe',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'A single blood test, processed by an IoT-connected gene sequencer, could offer early detection for cancer, with the AI analyzing DNA to identify circulating tumor DNA from nascent cancers and the genetic signatures of pathogens.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Früherkennung von Krebs durch AI',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'When you move beyond training models into the corporate world to do reasoning and inferencing on private corporate data, that\'s an even bigger market than training AI models.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Zwei-Phasen-Revolution der AI',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Several world-class AI companies have chosen Oracle to build large-scale GPU-centric data centers because Oracle builds gigawatt-scale data centers that are faster and more cost-efficient at training AI models than anyone else.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Wettbewerbsvorteil bei AI-Infrastruktur',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'These models are trained with public data, but they don\'t know how your company\'s accounts are calculated. The future value lies in applying AI to private enterprise data.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Enterprise AI-Strategie',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'We are collaborating with the University of Oxford to modify wheat to produce 20% more grain on the same land by using an AI model to simulate how to design more efficient photosynthesis.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - AI für Landwirtschaft und Ernährungssicherheit',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'The training of large models has become a trillion-dollar capital cycle. This is bigger than the railroads, bigger than the industrial revolution.',
            'datum_aussage': '2025-01-15',
            'kontext': 'Oracle AI World 2025 - Größenordnung der AI-Revolution',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'The US can\'t let China cultivate more engineers than the US and let Chinese companies win fierce competition against US companies.',
            'datum_aussage': '2018-06-01',
            'kontext': 'Aussage zum technologischen Wettbewerb mit China',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'When I bought Lāna\'i, I publicly announced plans to transform the island into a model for environmental sustainability. I intend to invest as much as $500 million to improve the island\'s infrastructure and create an environmentally friendly agricultural industry.',
            'datum_aussage': '2012-06-20',
            'kontext': 'Ankündigung nach dem Kauf von 98% der hawaiianischen Insel Lanai',
            'modus': 'schriftlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Oracle is focusing on solving the very important problem of how to enable the most recent AI models to complete multistep reasoning on private enterprise data without compromising the data.',
            'datum_aussage': '2024-12-10',
            'kontext': 'Oracle earnings call - Datensicherheit bei Enterprise AI',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Elon Musk, Mark Zuckerberg and Sam Altman are the smartest engineers in the AI space. They are building the future.',
            'datum_aussage': '2025-10-15',
            'kontext': 'Aussage über führende AI-Unternehmer',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'The US and other countries need to unify all of the national data into a database that can be fed to AI.',
            'datum_aussage': '2025-02-12',
            'kontext': 'Vision für nationale AI-Datenbanken und Überwachungsinfrastruktur',
            'modus': 'muendlich',
            'einschluss': 1
        },
        {
            'person_id': PERSON_ID,
            'aussage_text': 'Stargate will expand to 20 data centers and other locations around the world. This is the largest AI infrastructure project in history.',
            'datum_aussage': '2025-01-21',
            'kontext': 'White House Ankündigung des Stargate-Projekts mit Trump, Sam Altman und Masayoshi Son',
            'modus': 'muendlich',
            'einschluss': 1
        }
    ]

    # HANDLUNGEN
    handlungen = [
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'kauf',
            'beschreibung': 'Kauf von 98% der hawaiianischen Insel Lanai, um sie in ein Modell für ökologische Nachhaltigkeit zu verwandeln',
            'datum_handlung': '2012-06-20',
            'betrag_usd': 300000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'investition',
            'beschreibung': 'Oracle plant massive Kapitalaufnahme von 45-50 Milliarden USD für AI-Cloud-Expansion durch Mischung aus Fremd- und Eigenkapital',
            'datum_handlung': '2026-02-02',
            'betrag_usd': 50000000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'kauf',
            'beschreibung': 'Übernahme von NetSuite für 9,3 Milliarden USD, Ellison besaß 35% und machte persönlich 3,5 Milliarden USD',
            'datum_handlung': '2016-11-01',
            'betrag_usd': 9300000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Oracle sichert sich 300-Milliarden-USD-Vertrag mit OpenAI über fünf Jahre für Cloud-Computing-Ressourcen',
            'datum_handlung': '2025-09-10',
            'betrag_usd': 300000000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'investition',
            'beschreibung': 'Oracle plant Ausgaben von rund 40 Milliarden USD für NVIDIA-Chips, einschließlich etwa 400.000 der leistungsstärksten GB200-Chips',
            'datum_handlung': '2024-06-01',
            'betrag_usd': 40000000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'investition',
            'beschreibung': 'Abilene-Projekt: Baubeginn für AI-Rechenzentrum mit 450.000 NVIDIA GB200 GPUs, 1,2 GW Gesamtleistung auf über 1.000 Acres',
            'datum_handlung': '2024-06-15',
            'betrag_usd': None
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'spende',
            'beschreibung': 'Spende von mehr als 31 Millionen USD an republikanische Kandidaten während der Kongresswahlen 2022',
            'datum_handlung': '2022-11-01',
            'betrag_usd': 31000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'spende',
            'beschreibung': 'Spende von mehr als 30 Millionen USD seit 2021 an Opportunity Matters Fund Super PAC zur Unterstützung von Senator Tim Scott',
            'datum_handlung': '2022-05-01',
            'betrag_usd': 30000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'lobbying',
            'beschreibung': 'Ellison lobbyierte bei Trump, Tim Scott als Vizepräsidentschaftskandidaten zu wählen',
            'datum_handlung': '2024-07-01',
            'betrag_usd': None
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Oracle wird Teil der Investorengruppe, die 80,1% Anteil an der neu gegründeten US TikTok-Einheit erwirbt, nach Ausgliederung von ByteDance',
            'datum_handlung': '2025-12-18',
            'betrag_usd': None
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'investition',
            'beschreibung': 'Gründungsinvestition im Stargate AI-Projekt: Oracle verpflichtet 7 Milliarden USD initial bei geplanten Gesamtinvestitionen von 100-500 Milliarden USD',
            'datum_handlung': '2025-01-21',
            'betrag_usd': 7000000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Start des Baus von 10 Rechenzentren in Abilene, Texas für das Stargate-Projekt mit geplanter Expansion auf 20 Standorte weltweit',
            'datum_handlung': '2025-01-21',
            'betrag_usd': None
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Oracle sichert sich Mehrjahresverträge im Wert von über 300 Milliarden USD mit OpenAI, Meta, NVIDIA, SoftBank und xAI',
            'datum_handlung': '2025-09-01',
            'betrag_usd': 300000000000
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Zusammenarbeit mit University of Oxford zur AI-gestützten Modifikation von Weizen für 20% höhere Erträge durch effizientere Photosynthese',
            'datum_handlung': '2024-12-01',
            'betrag_usd': None
        },
        {
            'person_id': PERSON_ID,
            'handlung_typ': 'investition',
            'beschreibung': 'Ellisons Vermögen steigt an einem Tag um 101 Milliarden USD auf 393 Milliarden USD - größter eintägiger Vermögenszuwachs in der Geschichte',
            'datum_handlung': '2025-09-10',
            'betrag_usd': 101000000000
        }
    ]

    # Aussagen einfügen
    print(f"Fuege {len(aussagen)} Aussagen ein...")
    for aussage in aussagen:
        try:
            cursor.execute("""
                INSERT INTO aussagen (person_id, aussage_text, datum_aussage, kontext, modus, einschluss)
                VALUES (:person_id, :aussage_text, :datum_aussage, :kontext, :modus, :einschluss)
            """, aussage)
            print(f"  OK Aussage eingefuegt: {aussage['datum_aussage']} - {aussage['aussage_text'][:60]}...")
        except sqlite3.Error as e:
            print(f"  FEHLER bei Aussage: {e}")
            print(f"    Datum: {aussage['datum_aussage']}, Text: {aussage['aussage_text'][:60]}...")

    # Handlungen einfügen
    print(f"\nFuege {len(handlungen)} Handlungen ein...")
    for handlung in handlungen:
        try:
            cursor.execute("""
                INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, betrag_usd)
                VALUES (:person_id, :handlung_typ, :beschreibung, :datum_handlung, :betrag_usd)
            """, handlung)
            betrag_info = f"{handlung['betrag_usd']:,.0f} USD" if handlung['betrag_usd'] else "Betrag unbekannt"
            print(f"  OK Handlung eingefuegt: {handlung['datum_handlung']} - {handlung['handlung_typ']} - {betrag_info}")
            print(f"    {handlung['beschreibung'][:80]}...")
        except sqlite3.Error as e:
            print(f"  FEHLER bei Handlung: {e}")
            print(f"    Typ: {handlung['handlung_typ']}, Datum: {handlung['datum_handlung']}")

    # Änderungen speichern
    conn.commit()

    # Statistik
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    total_aussagen = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    total_handlungen = cursor.fetchone()[0]

    print(f"\n{'='*80}")
    print(f"ZUSAMMENFASSUNG")
    print(f"{'='*80}")
    print(f"Person: Larry Ellison (ID={PERSON_ID})")
    print(f"Gesamtanzahl Aussagen in DB:  {total_aussagen}")
    print(f"Gesamtanzahl Handlungen in DB: {total_handlungen}")
    print(f"{'='*80}")

    conn.close()
    print("\nOK Daten erfolgreich eingefuegt!")

if __name__ == "__main__":
    print("="*80)
    print("DATENSAMMLUNG: Larry Ellison (id=7)")
    print("Oracle Co-Founder, CTO, KI-Infrastruktur-Investor")
    print("="*80)
    print()

    insert_data()
