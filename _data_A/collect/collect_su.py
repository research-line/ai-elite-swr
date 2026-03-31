#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datenerfassung für Lisa Su (ID 14) - CEO AMD
Sozialwissenschaftliche Studie zu Weltbildern der KI-/Tech-Elite
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 14

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Beginne Datenerfassung für Lisa Su (Person ID: {PERSON_ID})")

    # ========== AUSSAGEN ==========
    # quellen_typ_id: 1=Interview, 2=Rede, 3=Artikel, 4=Buch, 5=Social Media, 6=Sonstiges
    aussagen = [
        {
            "aussage_text": "AI is the most important technology of the last 50 years, and I can say it's absolutely our number one priority at AMD.",
            "datum_aussage": "2026-01-05",
            "quellen_typ_id": 2,  # Keynote = Rede
            "kontext": "CES 2026 Keynote - Lisa Su betont die zentrale Bedeutung von KI für AMD und die Industrie",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "AI is the most powerful technology that has ever been created. And it can be everywhere for everyone.",
            "datum_aussage": "2026-01-05",
            "quellen_typ_id": 2,  # Keynote = Rede
            "kontext": "CES 2026 - Su präsentiert Vision einer allumfassenden, zugänglichen KI",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "AI is accelerating at a pace that I would not have imagined.",
            "datum_aussage": "2026-02-04",
            "quellen_typ_id": 1,  # Interview
            "kontext": "CNBC Interview - Su über die rasante Entwicklung der KI-Technologie",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "The demand for AI is just incredible. It's going through the roof.",
            "datum_aussage": "2026-01-06",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Fox Business Interview über explodierende Nachfrage nach KI-Chips",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "We will need 10 yottaflops of computing power by 2030 to support five billion AI users.",
            "datum_aussage": "2026-01-05",
            "quellen_typ_id": 2,  # Keynote = Rede
            "kontext": "CES 2026 - Su präsentiert Konzept der 'Yottascale era' für KI-Computing",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "Artificial intelligence has not slowed the pace of hiring at AMD, but the candidates who have truly embraced the technology have become a priority.",
            "datum_aussage": "2026-01-06",
            "quellen_typ_id": 1,  # Interview
            "kontext": "CNBC Interview - Su über KI's Einfluss auf Einstellungspolitik, KI als Enabler statt Ersatz",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "There should be a balance between export controls for national security as well as ensuring that we get the widest possible adoption of our technology.",
            "datum_aussage": "2025-05-07",
            "quellen_typ_id": 1,  # Interview
            "kontext": "CNBC Interview - Su warnt vor zu strikten US-Chip-Exportkontrollen gegen China",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "China is a large opportunity for the semiconductor and artificial intelligence industry.",
            "datum_aussage": "2025-05-07",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Statement zu China als strategischem Markt trotz geopolitischer Spannungen",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "We are only in year two of a massive ten-year cycle of rapid AI advancements and infrastructure build-out.",
            "datum_aussage": "2025-09-17",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Axios Interview - Su prognostiziert langfristigen KI-Boom über ein Jahrzehnt",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "We need to bring more semiconductor manufacturing back to the United States. Taiwan today still has the vast majority of all advanced semiconductors, but more of it will move and it's the right thing to do because you need resiliency in the supply chain.",
            "datum_aussage": "2024-12-01",
            "quellen_typ_id": 1,  # Interview
            "kontext": "TIME Magazine CEO of the Year Interview - Su über strategische Bedeutung von US-Chip-Produktion",
            "modus": "schriftlich",
            "einschluss": 1
        },
        {
            "aussage_text": "AMD could achieve double-digit share in the data center AI chip market over the next three to five years.",
            "datum_aussage": "2025-11-11",
            "quellen_typ_id": 2,  # Presentation/Rede
            "kontext": "AMD Analyst Day - Su skizziert Marktanteilsziele gegen NVIDIA-Dominanz",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "There will never be a case where there's only one technology used for something. There's quite a bit of AI training being done on AMD today.",
            "datum_aussage": "2024-08-15",
            "quellen_typ_id": 1,  # Interview
            "kontext": "HotHardware Interview - Su über technologische Vielfalt und NVIDIA-Wettbewerb",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "Everyone in the semiconductor industry, everyone in the technology industry, would benefit from more diversity in the business.",
            "datum_aussage": "2020-06-10",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Statement zu Diversität und Frauen in Tech-Führungspositionen",
            "modus": "schriftlich",
            "einschluss": 1
        },
        {
            "aussage_text": "Engineering is about how to solve problems and how can you very analytically solve a problem. We should make that fun as one of the key parts of making STEM interesting, especially to women and underrepresented minorities.",
            "datum_aussage": "2019-10-15",
            "quellen_typ_id": 2,  # Rede
            "kontext": "Rede über STEM-Förderung und Problemlösungskultur in der Technik",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "In tech there's no such thing as cutting yourself to be a winner. You have to decide what do we want to be when we grow up. The decisions that we make today, you will really see the impact three to five years down the road.",
            "datum_aussage": "2024-04-20",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Stratechery Interview - Su über langfristige Strategieplanung in der Tech-Industrie",
            "modus": "schriftlich",
            "einschluss": 1
        },
        {
            "aussage_text": "AMD is on the path to a 100x power efficiency improvement by 2027. Energy efficiency is one of the most important challenges to face computing in the next ten years.",
            "datum_aussage": "2024-06-12",
            "quellen_typ_id": 2,  # Keynote = Rede
            "kontext": "imec's ITF World 2024 - Su über kritische Bedeutung von Energieeffizienz für Computing",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "Some supercomputers could require as much as 500 megawatts apiece within a decade. The demand for compute continues to be immense.",
            "datum_aussage": "2023-02-20",
            "quellen_typ_id": 2,  # Rede
            "kontext": "IEEE International Solid State Circuits Conference - Su warnt vor enormem Energiebedarf",
            "modus": "muendlich",
            "einschluss": 1
        },
        {
            "aussage_text": "Leaders are trained. Leadership is about hard work, continuous learning, and training.",
            "datum_aussage": "2021-05-10",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Leadership-Philosophie Interview - Su über erlernbare Führungsqualitäten",
            "modus": "schriftlich",
            "einschluss": 1
        },
        {
            "aussage_text": "AI is not a zero-sum game. There are multiple winners in this market. We're partnering with many companies because no one company has all of the good ideas.",
            "datum_aussage": "2024-11-05",
            "quellen_typ_id": 1,  # Interview
            "kontext": "Conference Board Podcast - Su über Kooperation statt reinen Wettbewerb in der Chip-Industrie",
            "modus": "muendlich",
            "einschluss": 1
        }
    ]

    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, datum_aussage, quellen_typ_id, kontext, modus, einschluss)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            aussage["aussage_text"],
            aussage["datum_aussage"],
            aussage["quellen_typ_id"],
            aussage["kontext"],
            aussage["modus"],
            aussage["einschluss"]
        ))

    # ========== HANDLUNGEN ==========
    handlungen = [
        {
            "handlung_typ": "einstellung",
            "beschreibung": "Lisa Su wird CEO von AMD, übernimmt Führung eines krisengeschüttelten Unternehmens mit Aktienkurs unter 2 USD",
            "datum_handlung": "2014-10-08",
            "betrag_usd": None
        },
        {
            "handlung_typ": "umstrukturierung",
            "beschreibung": "Su initiiert strategische Neuausrichtung: Fokus auf High-Performance Computing, Gaming und KI; R&D-Budget wird um ca. 45% erhöht (2014-2017)",
            "datum_handlung": "2015-03-15",
            "betrag_usd": None
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "AMD wechselt Chip-Produktion zu TSMC (Taiwan), transformative Entscheidung für Produktqualität und Wettbewerbsfähigkeit",
            "datum_handlung": "2018-06-01",
            "betrag_usd": None
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch der Ryzen-Prozessoren mit neuer Zen-Architektur - AMD kehrt zurück in CPU-Wettbewerb mit Intel",
            "datum_handlung": "2017-03-02",
            "betrag_usd": None
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch der EPYC Server-Prozessoren für Rechenzentren - strategischer Eintritt in lukrativen Data Center Markt",
            "datum_handlung": "2017-06-20",
            "betrag_usd": None
        },
        {
            "handlung_typ": "kauf",
            "beschreibung": "AMD kündigt Übernahme von Xilinx (FPGA-Hersteller) an - eine der größten Chip-Deals überhaupt, Stärkung adaptiver Computing-Fähigkeiten",
            "datum_handlung": "2020-10-27",
            "betrag_usd": 35000000000
        },
        {
            "handlung_typ": "kauf",
            "beschreibung": "Abschluss der Xilinx-Übernahme; Su wird Chair von AMD, kombiniertes Unternehmen entsteht",
            "datum_handlung": "2022-02-14",
            "betrag_usd": 49000000000
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch der MI300 AI-Beschleuniger-Serie - AMD's direkter Angriff auf NVIDIA's KI-Chip-Dominanz",
            "datum_handlung": "2023-12-06",
            "betrag_usd": None
        },
        {
            "handlung_typ": "kauf",
            "beschreibung": "AMD gibt Übernahme von ZT Systems bekannt (Compute-Infrastruktur für Hyperscaler), Stärkung der Datacenter-Präsenz",
            "datum_handlung": "2024-08-19",
            "betrag_usd": 4900000000
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "AMD und OpenAI verkünden massive Partnerschaft: OpenAI kauft AMD Instinct AI-Chips für 6 Gigawatt Deployment, Start 2026 mit 1 GW",
            "datum_handlung": "2025-10-15",
            "betrag_usd": None
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "AMD stellt Gesamtinvestitionen von über 100 Milliarden USD für organisches und anorganisches Wachstum über 5 Jahre dar (2020-2025)",
            "datum_handlung": "2025-11-11",
            "betrag_usd": 100000000000
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "AMD kündigt MI450 GPUs an, Teil des OpenAI-Deals für 2026 Deployment - nächste Generation KI-Beschleuniger",
            "datum_handlung": "2025-11-11",
            "betrag_usd": None
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Su verkündet Kooperation mit GE Vernova zur Integration von Kernenergie in Tech-Infrastruktur für KI-Rechenzentren",
            "datum_handlung": "2024-09-10",
            "betrag_usd": None
        },
        {
            "handlung_typ": "sonstiges",
            "beschreibung": "AMD gibt Warrant für bis zu 160 Millionen AMD-Aktien an OpenAI aus, vesting bei Erreichen technischer/kommerzieller Meilensteine",
            "datum_handlung": "2025-10-15",
            "betrag_usd": None
        }
    ]

    print(f"Füge {len(handlungen)} Handlungen ein...")
    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, betrag_usd)
            VALUES (?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            handlung["handlung_typ"],
            handlung["beschreibung"],
            handlung["datum_handlung"],
            handlung["betrag_usd"]
        ))

    conn.commit()

    # Statistik
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    anzahl_aussagen = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    anzahl_handlungen = cursor.fetchone()[0]

    print(f"\n{'='*60}")
    print(f"ERFOLGREICH ABGESCHLOSSEN")
    print(f"{'='*60}")
    print(f"Person: Lisa Su (ID {PERSON_ID})")
    print(f"Aussagen eingefügt: {anzahl_aussagen}")
    print(f"Handlungen eingefügt: {anzahl_handlungen}")
    print(f"Zeitraum: 2014-2026")
    print(f"{'='*60}")

    conn.close()

if __name__ == "__main__":
    try:
        insert_data()
    except Exception as e:
        print(f"\nFEHLER beim Einfügen der Daten: {e}")
        raise
