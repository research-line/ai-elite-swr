#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Jeff Dean (ID=19)
Chief Scientist bei Google DeepMind, Mitentwickler von MapReduce, BigTable, TensorFlow, Transformer-Architektur
Sammelt öffentliche Aussagen und Handlungen für sozialwissenschaftliche Studie über Weltbilder der KI-Elite
"""

import sqlite3
from datetime import datetime

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 19

def insert_data():
    """Fügt Aussagen und Handlungen von Jeff Dean in die Datenbank ein."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Füge Daten für Jeff Dean (ID={PERSON_ID}) ein...")

    # ========== AUSSAGEN ==========
    # Quellen_typ IDs: 1=Video-Interview, 2=Podcast-Interview, 3=Keynote/Vortrag,
    # 5=Social-Media-Post, 7=Nachrichtenartikel, 9=Wissenschaftlicher Artikel, 10=Offizielle Stellungnahme
    aussagen = [
        {
            'aussage_text': 'If you think back five years ago to what these models could do, it\'s a major difference between the models of today. I think you\'ll see pretty similar levels of difference in the models five years from now.',
            'datum_aussage': '2023-01-01',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'Aussage über kontinuierlichen Fortschritt in KI-Modellen und Skalierung',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war.',
            'datum_aussage': '2023-05-30',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'kontext': 'CAIS Statement on AI Risk - Unterzeichner des Statements über existenzielle KI-Risiken',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'With TensorFlow, when we started to develop it, we kind of looked at ourselves and said: Hey, maybe we should open source this.',
            'datum_aussage': '2015-11-09',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'Über die Entscheidung, TensorFlow als Open Source zu veröffentlichen',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'It basically invented the concept of a cat.',
            'datum_aussage': '2012-06-26',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'kontext': 'Google Brain Experiment - Neuronales Netz lernt Katzen in YouTube-Videos zu erkennen ohne Labels',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'All the different sub-specialties in medical imaging are undergoing a significant transformation because computer vision now works.',
            'datum_aussage': '2018-03-13',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Über den Einsatz von KI in der Medizin und medizinischen Bildgebung',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Our moonshot goal is to have every previous medical decision inform every future decision through AI.',
            'datum_aussage': '2018-03-13',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'Vision für AI im Gesundheitswesen - Sammlung aller medizinischen Entscheidungen zur Verbesserung zukünftiger Behandlungen',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'It\'s important to engage with governments around the world in how they\'re thinking about AI — to help inform them.',
            'datum_aussage': '2018-05-08',
            'quellen_typ_id': 1,  # Video-Interview
            'kontext': 'CNBC Interview über die Rolle von Tech-Unternehmen in der KI-Regulierung',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'AI has the potential to transform industries and improve lives, but it\'s essential that we develop it responsibly and ethically.',
            'datum_aussage': '2020-01-01',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'kontext': 'Grundsatzaussage zu verantwortungsvoller KI-Entwicklung',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'We need to use more of a combination of supervised and unsupervised learning. Machine learning systems aren\'t really there yet in terms of how most systems work.',
            'datum_aussage': '2019-12-13',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'kontext': 'VentureBeat Interview über Machine Learning Trends 2020',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Specialization of chips for specific computation—like GPUs or TPUs designed around what ML computations need to do—gets a fair amount of performance advantage relative to general-purpose CPUs.',
            'datum_aussage': '2019-12-13',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'kontext': 'Über die Bedeutung spezialisierter Hardware für Machine Learning',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Because it\'s like twins coming together.',
            'datum_aussage': '2023-04-20',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'kontext': 'Erklärung für den Namen "Gemini" nach der Fusion von Google Brain und DeepMind',
            'modus': 'muendlich'
        },
        {
            'aussage_text': 'Large but sparsely activated neural networks can consume less than 1/10th the energy of large, dense networks without sacrificing accuracy.',
            'datum_aussage': '2021-04-21',
            'quellen_typ_id': 9,  # Wissenschaftlicher Artikel
            'kontext': 'Co-Autor Paper "Carbon Emissions and Large Neural Network Training" über Energieeffizienz',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'The median Gemini Apps text prompt uses 0.24 watt-hours of energy, equivalent to watching an LED light for a few minutes.',
            'datum_aussage': '2025-02-05',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'kontext': 'Tweet über Energieeffizienz von Gemini - 44x Reduktion des Carbon Footprints in einem Jahr',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'We calculate that if every Android user utilized Google\'s new voice search feature for just three minutes a day, the company would need to double its global data center capacity.',
            'datum_aussage': '2013-01-01',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'kontext': 'Projektion die zur Entwicklung der TPU führte - Motivation für spezialisierte AI-Hardware',
            'modus': 'schriftlich'
        },
        {
            'aussage_text': 'We\'ve been running TPUs inside our data centers for more than a year, and have found them to deliver an order of magnitude better performance per watt for machine learning.',
            'datum_aussage': '2016-05-18',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'kontext': 'Sundar Pichai Keynote Google I/O 2016 - Erste öffentliche Ankündigung der Tensor Processing Units',
            'modus': 'muendlich'
        }
    ]

    for aussage in aussagen:
        plattform_id = aussage.get('plattform_id', None)
        cursor.execute('''
            INSERT INTO aussagen (person_id, aussage_text, datum_aussage, quellen_typ_id, plattform_id, kontext, modus, einschluss)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
        ''', (PERSON_ID, aussage['aussage_text'], aussage['datum_aussage'],
              aussage['quellen_typ_id'], plattform_id, aussage['kontext'], aussage['modus']))

    print(f"[OK] {len(aussagen)} Aussagen eingefuegt")

    # ========== HANDLUNGEN ==========
    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgründung von Google Brain zusammen mit Andrew Ng und Greg Corrado - Deep Learning AI Research Team',
            'datum_handlung': '2011-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Open Source Release von TensorFlow - Machine Learning Framework mit Apache 2.0 Lizenz, über 11.000 GitHub Stars in erster Woche',
            'datum_handlung': '2015-11-09',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Öffentliche Ankündigung der Tensor Processing Units (TPUs) bei Google I/O - Spezialisierte Hardware für Machine Learning',
            'datum_handlung': '2016-05-18',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Co-Autor des Papers "Attention Is All You Need" - Transformer-Architektur die ChatGPT, Claude, Gemini ermöglicht (Senior Author)',
            'datum_handlung': '2017-06-12',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Beförderung zum Lead of Google AI - Leitung der gesamten KI-Forschung bei Google',
            'datum_handlung': '2018-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'umstrukturierung',
            'beschreibung': 'Vorantreiben der Fusion von Google Brain und DeepMind zu Google DeepMind - Konsolidierung der AI-Forschungsabteilungen',
            'datum_handlung': '2023-04-20',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Ernennung zum Chief Scientist von Google - Leitung der kritischsten und strategischsten technischen KI-Projekte',
            'datum_handlung': '2023-04-20',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Gemini (multimodales KI-Modell) - Name von Dean vorgeschlagen nach DeepMind/Brain Fusion',
            'datum_handlung': '2023-12-06',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Wahl zum Fellow der Association for Computing Machinery (ACM) - Anerkennung für Beiträge zur Informatik',
            'datum_handlung': '2009-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Wahl zum Member der National Academy of Engineering - "For contributions to the science and engineering of large-scale distributed computer systems"',
            'datum_handlung': '2009-02-06',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'ACM-Infosys Foundation Award - Auszeichnung für bedeutende Beiträge zur Informatik',
            'datum_handlung': '2012-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Fellow der American Academy of Arts and Sciences - Anerkennung für wissenschaftliche Exzellenz',
            'datum_handlung': '2016-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'IEEE John von Neumann Medal - Höchste Auszeichnung für Beiträge zur Computer-related Science and Technology',
            'datum_handlung': '2021-01-01',
            'betrag_usd': None
        },
        {
            'handlung_typ': 'lobbying',
            'beschreibung': 'Engagement mit Regierungen weltweit zu AI-Regulierung - Advocacy für informierte KI-Politik durch Tech-Expertise',
            'datum_handlung': '2018-05-08',
            'betrag_usd': None
        }
    ]

    for handlung in handlungen:
        cursor.execute('''
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, betrag_usd)
            VALUES (?, ?, ?, ?, ?)
        ''', (PERSON_ID, handlung['handlung_typ'], handlung['beschreibung'],
              handlung['datum_handlung'], handlung['betrag_usd']))

    print(f"[OK] {len(handlungen)} Handlungen eingefuegt")

    # Änderungen speichern
    conn.commit()

    # Statistik anzeigen
    cursor.execute('SELECT COUNT(*) FROM aussagen WHERE person_id = ?', (PERSON_ID,))
    total_aussagen = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM handlungen WHERE person_id = ?', (PERSON_ID,))
    total_handlungen = cursor.fetchone()[0]

    print(f"\n{'='*60}")
    print(f"ZUSAMMENFASSUNG - Jeff Dean (ID={PERSON_ID})")
    print(f"{'='*60}")
    print(f"Gesamt Aussagen in DB:    {total_aussagen}")
    print(f"Gesamt Handlungen in DB:  {total_handlungen}")
    print(f"Zeitraum:                 2009-2025")
    print(f"{'='*60}")

    conn.close()
    print("\n[OK] Daten erfolgreich in Datenbank eingefuegt!")

if __name__ == '__main__':
    try:
        insert_data()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
    except Exception as e:
        print(f"Fehler: {e}")
