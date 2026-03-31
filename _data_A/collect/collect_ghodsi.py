#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collect Ali Ghodsi (person_id=38) - Tier 2 Data Collection
Research project: Weltbilder der KI-Elite
"""

import sqlite3
from datetime import datetime

# Database path
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID for Ali Ghodsi
PERSON_ID = 38

def insert_aussage(cursor, aussage_text, aussage_kurz, modus, quellen_typ_id, plattform_id,
                   quell_link, quell_titel, datum_aussage, sprache, kontext, aussage_uebersetzung_de):
    """Insert a statement (Aussage) into the database."""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quellen_typ_id, plattform_id,
            quell_link, quell_titel, datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (PERSON_ID, aussage_text, aussage_kurz, modus, quellen_typ_id, plattform_id,
          quell_link, quell_titel, datum_aussage, sprache, kontext, aussage_uebersetzung_de))

def insert_handlung(cursor, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext):
    """Insert an action (Handlung) into the database."""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (PERSON_ID, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext))

def main():
    """Main function to collect Ali Ghodsi's statements and actions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        print("Starting data collection for Ali Ghodsi (person_id=38)")
        print("=" * 70)

        # ============================================================================
        # AUSSAGEN (Statements) - Minimum 10 for Tier 2
        # ============================================================================

        # Aussage 1: AGI is already here
        insert_aussage(
            cursor,
            aussage_text="If all AI progress was frozen today, I think we have what we need to proceed with what we are doing.",
            aussage_kurz="KI-Fortschritt könnte heute eingefroren werden, wir haben bereits was wir brauchen",
            modus="muendlich",
            quellen_typ_id=1,  # Video-Interview
            plattform_id=5,    # Nachrichtenmedien
            quell_link="https://time.com/7338006/ai-agi-databricks-ali-ghodsi/",
            quell_titel="Databricks' CEO Believes AGI Is Already Here",
            datum_aussage="2025-12-02",
            sprache="EN",
            kontext="TIME Interview über AGI-Diskussion. Ghodsi argumentiert, dass AGI bereits erreicht ist basierend auf Fähigkeiten wie sprechen, logisch denken und Muster in großen Datenmengen erkennen.",
            aussage_uebersetzung_de="Wenn der gesamte KI-Fortschritt heute eingefroren würde, denke ich, haben wir bereits das, was wir brauchen, um mit dem fortzufahren, was wir tun."
        )

        # Aussage 2: AI Bubble Warning
        insert_aussage(
            cursor,
            aussage_text="Companies that are worth, you know, billions of dollars with zero revenue, that's clearly a bubble, right, and it's, like, insane.",
            aussage_kurz="Unternehmen mit Milliardenbewertung ohne Umsatz sind eine Blase",
            modus="muendlich",
            quellen_typ_id=3,  # Keynote/Vortrag
            plattform_id=4,    # Konferenzen
            quell_link="https://fortune.com/2025/12/24/databricks-ceo-ali-ghodsi-bubble-insane-zero-revenue-ai-circular/",
            quell_titel="CEO blasts companies with billions in funding but zero revenue",
            datum_aussage="2025-12-24",
            sprache="EN",
            kontext="Fortune Brainstorm AI Konferenz. Ghodsi warnt vor einer KI-Blase bei Startups mit hohen Bewertungen aber ohne Umsätze.",
            aussage_uebersetzung_de="Unternehmen, die Milliarden Dollar wert sind mit null Umsatz, das ist eindeutig eine Blase, oder, und es ist einfach wahnsinnig."
        )

        # Aussage 3: 80% of databases built by AI agents
        insert_aussage(
            cursor,
            aussage_text="Over 80% of the databases that are being launched on Databricks are not being launched by humans, but by AI agents.",
            aussage_kurz="Über 80% der Datenbanken auf Databricks werden von KI-Agenten erstellt",
            modus="muendlich",
            quellen_typ_id=3,  # Keynote/Vortrag
            plattform_id=4,    # Konferenzen
            quell_link="https://fortune.com/2025/12/09/databticks-ceo-1-trillion-valuation-agents-brainstorm-ai/",
            quell_titel="Databricks CEO says his company will be worth $1 trillion by doing these three things",
            datum_aussage="2025-12-09",
            sprache="EN",
            kontext="Fortune Brainstorm AI über die Transformation durch KI-Agenten in der Softwareentwicklung.",
            aussage_uebersetzung_de="Über 80% der Datenbanken, die auf Databricks gestartet werden, werden nicht von Menschen gestartet, sondern von KI-Agenten."
        )

        # Aussage 4: Data governance as bottleneck
        insert_aussage(
            cursor,
            aussage_text="It's actually the governance of the data that's the problem. It's not like we can't access that data, that data is there... It's because of privacy.",
            aussage_kurz="Daten-Governance ist das Hauptproblem, nicht technischer Zugang",
            modus="muendlich",
            quellen_typ_id=1,  # Video-Interview
            plattform_id=5,    # Nachrichtenmedien
            quell_link="https://www.cnbc.com/video/2025/09/08/concerns-around-corporate-data-privacy-and-security-holding-back-ai-says-databricks-ceo-ghodsi.html",
            quell_titel="Concerns around corporate data privacy and security holding back AI",
            datum_aussage="2025-09-08",
            sprache="EN",
            kontext="CNBC Interview über Hindernisse für Enterprise-KI-Adoption. Ghodsi identifiziert Governance und Privacy als Haupthindernisse.",
            aussage_uebersetzung_de="Es ist tatsächlich die Governance der Daten, die das Problem ist. Es ist nicht so, dass wir nicht auf diese Daten zugreifen können, diese Daten sind da... Es liegt an der Privatsphäre."
        )

        # Aussage 5: SaaS companies will be wiped out
        insert_aussage(
            cursor,
            aussage_text="Some of these SaaS companies are going to be wiped out. They are going to focus on short-term revenue... not innovate... and then in a year or two, those businesses will go out of business.",
            aussage_kurz="Viele SaaS-Unternehmen werden durch KI ausgelöscht werden",
            modus="muendlich",
            quellen_typ_id=1,  # Video-Interview
            plattform_id=5,    # Nachrichtenmedien
            quell_link="https://www.storyboard18.com/brand-makers/short-term-thinking-will-kill-them-databricks-ceo-says-saas-firms-risk-collapse-in-ai-era-89400.htm",
            quell_titel="Short-term thinking will kill them - Databricks CEO says SaaS firms risk collapse in AI era",
            datum_aussage="2026-02-09",
            sprache="EN",
            kontext="Interview über die Zukunft der SaaS-Industrie im KI-Zeitalter. Warnung vor kurzfristigem Denken.",
            aussage_uebersetzung_de="Einige dieser SaaS-Unternehmen werden ausgelöscht werden. Sie werden sich auf kurzfristige Umsätze konzentrieren... nicht innovieren... und dann werden diese Unternehmen in ein oder zwei Jahren pleite gehen."
        )

        # Aussage 6: Democratize AI for startups
        insert_aussage(
            cursor,
            aussage_text="Every organization should be able to benefit from the AI revolution with more control over how their data is used. Databricks and MosaicML have an incredible opportunity to democratize AI.",
            aussage_kurz="Jede Organisation sollte von der KI-Revolution mit Kontrolle über ihre Daten profitieren",
            modus="schriftlich",
            quellen_typ_id=10,  # Offizielle Stellungnahme
            plattform_id=17,    # Sonstige
            quell_link="https://www.cnbc.com/video/2023/06/26/mosaicml-acquisition-will-allow-us-to-democratize-a-i-for-startups-says-databricks-ceo-ali-ghodsi.html",
            quell_titel="MosaicML acquisition will allow us to democratize A.I. for startups",
            datum_aussage="2023-06-26",
            sprache="EN",
            kontext="Statement zur MosaicML-Akquisition. Vision der KI-Demokratisierung für alle Organisationen.",
            aussage_uebersetzung_de="Jede Organisation sollte in der Lage sein, von der KI-Revolution zu profitieren und dabei mehr Kontrolle darüber zu haben, wie ihre Daten verwendet werden. Databricks und MosaicML haben eine unglaubliche Möglichkeit, KI zu demokratisieren."
        )

        # Aussage 7: Open source decision for Spark
        insert_aussage(
            cursor,
            aussage_text="We need to get adoption first.",
            aussage_kurz="Adoption vor Monetarisierung - Open Source Strategie",
            modus="muendlich",
            quellen_typ_id=7,  # Nachrichtenartikel
            plattform_id=5,    # Nachrichtenmedien
            quell_link="https://kitrum.com/blog/the-inspiring-story-ali-ghodsi-ceo-of-databricks/",
            quell_titel="How Ali Ghodsi, CEO of Databricks, Revolutionized Data and AI",
            datum_aussage="2012-12-01",
            sprache="EN",
            kontext="Entscheidung 2012, Apache Spark als Open Source zu veröffentlichen statt sofort zu kommerzialisieren. Zeigt strategische Vision: Adoption vor Monetarisierung.",
            aussage_uebersetzung_de="Wir müssen zuerst eine breite Adoption erreichen."
        )

        # Aussage 8: IPO timing
        insert_aussage(
            cursor,
            aussage_text="We will go public at some point. But to us, it's not a really big deal.",
            aussage_kurz="Börsengang irgendwann, aber keine Priorität",
            modus="muendlich",
            quellen_typ_id=1,  # Video-Interview
            plattform_id=5,    # Nachrichtenmedien
            quell_link="https://www.cnbc.com/video/2025/12/16/databricks-ceo-ali-ghodsi-wouldnt-rule-out-going-public-in-2026.html",
            quell_titel="Databricks CEO Ali Ghodsi: Wouldn't rule out going public in 2026",
            datum_aussage="2025-12-16",
            sprache="EN",
            kontext="CNBC Interview über IPO-Pläne nach $134B Bewertung. Zeigt Fokus auf Produktentwicklung über Finanzmarkt-Ereignisse.",
            aussage_uebersetzung_de="Wir werden irgendwann an die Börse gehen. Aber für uns ist es keine wirklich große Sache."
        )

        # Aussage 9: Delta Lake to Linux Foundation
        insert_aussage(
            cursor,
            aussage_text="I am confident that Delta Lake will quickly become the standard for data storage in data lakes.",
            aussage_kurz="Delta Lake wird zum Standard für Data Lakes werden",
            modus="schriftlich",
            quellen_typ_id=10,  # Offizielle Stellungnahme
            plattform_id=17,    # Sonstige
            quell_link="https://www.techmonitor.ai/technology/emerging-technology/databricks-delta-lake",
            quell_titel="Databricks Gifts Delta Lake to the Linux Foundation",
            datum_aussage="2019-10-15",
            sprache="EN",
            kontext="Spende von Delta Lake an die Linux Foundation. Zeigt Commitment zu Open Source und Vision für Industriestandards.",
            aussage_uebersetzung_de="Ich bin zuversichtlich, dass Delta Lake schnell zum Standard für Datenspeicherung in Data Lakes werden wird."
        )

        # Aussage 10: Data replication necessity
        insert_aussage(
            cursor,
            aussage_text="To build analytical dashboards, data applications, and AI models, data needs to be replicated from the systems of record like CRM, ERP, and enterprise apps to the Lakehouse.",
            aussage_kurz="Datenreplikation ist essentiell für Analytics und KI-Modelle",
            modus="schriftlich",
            quellen_typ_id=10,  # Offizielle Stellungnahme
            plattform_id=17,    # Sonstige
            quell_link="https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-arcion-leading-provider-real-time",
            quell_titel="Databricks Agrees to Acquire Arcion",
            datum_aussage="2023-10-23",
            sprache="EN",
            kontext="Statement zur Arcion-Akquisition. Erklärt technische Notwendigkeit von Echtzeit-Datenreplikation für Enterprise-KI.",
            aussage_uebersetzung_de="Um analytische Dashboards, Datenanwendungen und KI-Modelle zu erstellen, müssen Daten aus den Quellsystemen wie CRM, ERP und Enterprise-Apps zum Lakehouse repliziert werden."
        )

        # Aussage 11: Trillion dollar path
        insert_aussage(
            cursor,
            aussage_text="If we just did that, we could maybe get all the way to a trillion.",
            aussage_kurz="KI-Agenten allein könnten zu Trillion-Dollar-Bewertung führen",
            modus="muendlich",
            quellen_typ_id=3,  # Keynote/Vortrag
            plattform_id=4,    # Konferenzen
            quell_link="https://fortune.com/2025/12/09/databticks-ceo-1-trillion-valuation-agents-brainstorm-ai/",
            quell_titel="Databricks CEO says his company will be worth $1 trillion by doing these three things",
            datum_aussage="2025-12-09",
            sprache="EN",
            kontext="Fortune Brainstorm AI über Wachstumsstrategie. Bezieht sich auf KI-Agenten, die Datenbanken erstellen.",
            aussage_uebersetzung_de="Wenn wir nur das tun würden, könnten wir vielleicht den ganzen Weg bis zu einer Billion schaffen."
        )

        # Aussage 12: Your AI on your data
        insert_aussage(
            cursor,
            aussage_text="Your AI built on your data is what will set you apart.",
            aussage_kurz="Eigene KI auf eigenen Daten schafft Differenzierung",
            modus="muendlich",
            quellen_typ_id=3,  # Keynote/Vortrag
            plattform_id=4,    # Konferenzen
            quell_link="https://analyticsindiamag.com/people/ali-ghodsi/",
            quell_titel="Ali Ghodsi - Co-founder of Databricks",
            datum_aussage="2023-06-27",
            sprache="EN",
            kontext="Data + AI Summit. Vision für Enterprise-KI: proprietäre Daten als Wettbewerbsvorteil.",
            aussage_uebersetzung_de="Ihre KI, die auf Ihren Daten aufgebaut ist, ist das, was Sie abheben wird."
        )

        print(f"[OK] Inserted 12 statements (Aussagen)")

        # ============================================================================
        # HANDLUNGEN (Actions) - Minimum 8 for Tier 2
        # ============================================================================

        # Handlung 1: Databricks founding
        insert_handlung(
            cursor,
            handlung_typ="gruendung",
            beschreibung="Mitgründung von Databricks als einer von sieben Co-Founders ('Apache Spark Seven') zusammen mit Ion Stoica, Matei Zaharia, Patrick Wendell, Reynold Xin, Andy Konwinski und Arsalan Tavakoli-Shiraji",
            datum_handlung="2013-01-01",
            quell_link="https://en.wikipedia.org/wiki/Ali_Ghodsi",
            quell_titel="Ali Ghodsi - Wikipedia",
            kontext="Ausgründung aus UC Berkeley AMPLab. Apache Spark wurde 2013 als Open Source freigegeben, im selben Jahr gründeten die Entwickler Databricks."
        )

        # Handlung 2: CEO appointment
        insert_handlung(
            cursor,
            handlung_typ="einstellung",
            beschreibung="Übernahme der CEO-Position bei Databricks (zuvor Co-Founder und verschiedene technische Rollen)",
            datum_handlung="2016-01-01",
            quell_link="https://en.wikipedia.org/wiki/Ali_Ghodsi",
            quell_titel="Ali Ghodsi - Wikipedia",
            kontext="Ali Ghodsi wurde Anfang 2016 zum CEO ernannt und führt seitdem Databricks als Chief Executive Officer."
        )

        # Handlung 3: Delta Lake to Linux Foundation
        insert_handlung(
            cursor,
            handlung_typ="spende",
            beschreibung="Spende von Delta Lake an die Linux Foundation als Open-Source-Projekt unter Apache 2.0 Lizenz",
            datum_handlung="2019-10-15",
            quell_link="https://techcrunch.com/2019/10/15/databricks-brings-its-delta-lake-open-source-project-to-the-linux-foundation/",
            quell_titel="Databricks brings its Delta Lake project to the Linux Foundation",
            kontext="Strategische Open-Source-Spende zur Etablierung von Delta Lake als Industrie-Standard. Wahl der Linux Foundation statt Apache Foundation."
        )

        # Handlung 4: MosaicML acquisition
        insert_handlung(
            cursor,
            handlung_typ="kauf",
            beschreibung="Akquisition von MosaicML, einer führenden Generative-AI-Plattform, für $1.3 Milliarden (inklusive Retention Packages). MosaicML ist bekannt für MPT Large Language Models.",
            datum_handlung="2023-07-19",
            quell_link="https://fortune.com/2023/07/19/databricks-mosaicml-ai-acquisition/",
            quell_titel="Behind the scenes of Databricks' $1.3 billion MosaicML deal",
            kontext="Akquisition abgeschlossen am 19. Juli 2023. Strategisch zur Demokratisierung von Generative AI für Enterprises. Eine der größten AI-Akquisitionen 2023."
        )

        # Handlung 5: Okera acquisition
        insert_handlung(
            cursor,
            handlung_typ="kauf",
            beschreibung="Akquisition von Okera, der weltweit ersten KI-zentrierten Data-Governance-Plattform. Okera hatte zuvor knapp $30 Millionen Funding erhalten.",
            datum_handlung="2023-05-03",
            quell_link="https://techcrunch.com/2023/05/03/databricks-acquires-ai-centric-data-governance-platform-okera/",
            quell_titel="Databricks acquires AI-centric data governance platform Okera",
            kontext="Akquisition zur Stärkung von Unity Catalog mit KI-gestützter automatischer Datenklassifizierung und Governance-Funktionen. Okera-CEO Nong Li (Apache Parquet Entwickler) kam zu Databricks."
        )

        # Handlung 6: Arcion acquisition
        insert_handlung(
            cursor,
            handlung_typ="kauf",
            beschreibung="Akquisition von Arcion, führender Anbieter für Echtzeit-Enterprise-Datenreplikation, für über $100 Millionen (inklusive Incentives)",
            datum_handlung="2023-10-23",
            quell_link="https://techcrunch.com/2023/10/23/after-43b-valuation-databricks-acquires-data-replication-startup-arcion-for-100m/",
            quell_titel="After $43B valuation, Databricks acquires data replication startup Arcion for $100M",
            kontext="Akquisition zur nativen Integration von Change Data Capture (CDC) für über 20 Enterprise-Datenbanken und Data Warehouses in die Databricks Lakehouse Platform."
        )

        # Handlung 7: Tabular acquisition
        insert_handlung(
            cursor,
            handlung_typ="kauf",
            beschreibung="Akquisition von Tabular für über $2 Milliarden. Tabular wurde von den Erfindern von Apache Iceberg gegründet. Databricks gewann Bieterwettbewerb gegen Snowflake und Confluent.",
            datum_handlung="2024-06-04",
            quell_link="https://www.cnbc.com/2024/06/04/databricks-is-buying-data-optimization-startup-tabular.html",
            quell_titel="Databricks acquires data optimization startup Tabular in fresh challenge to Snowflake",
            kontext="Strategische Akquisition für Interoperabilität zwischen Delta Lake und Apache Iceberg. Sowohl offensiv (Iceberg-Expertise) als auch defensiv (Verhinderung von Snowflake-Akquisition)."
        )

        # Handlung 8: Series J funding $10B
        insert_handlung(
            cursor,
            handlung_typ="investition",
            beschreibung="Einwerbung von $10 Milliarden in Series J Funding bei $62 Milliarden Bewertung. Led by Thrive Capital, co-led by Andreessen Horowitz, DST Global, Insight Partners, WCM, GIC. Neue Investoren: Iconiq Growth, Sands Capital, Wellington Management, MGX.",
            datum_handlung="2024-12-17",
            quell_link="https://fortune.com/2024/12/17/databricks-ceo-ali-ghodsi-on-raising-10-billion-ai-talent-going-public/",
            quell_titel="Databricks CEO Ali Ghodsi on raising $10 billion, fighting for AI talent, and someday going public",
            kontext="Eine der größten VC-Finanzierungen aller Zeiten. $8.6 Milliarden bereits abgeschlossen von $10 Milliarden. Ghodsi berichtete von $18-19 Milliarden Interesse. Für KI-Produkte, Akquisitionen und internationale Expansion."
        )

        # Handlung 9: Series K funding $5B
        insert_handlung(
            cursor,
            handlung_typ="investition",
            beschreibung="Abschluss einer $5 Milliarden Finanzierungsrunde (davon $3B Equity, $2B Debt) bei $134 Milliarden Bewertung. Mehr als Verdopplung der Bewertung seit Series J.",
            datum_handlung="2026-02-09",
            quell_link="https://www.cnbc.com/2026/02/09/databricks-completes-5-billion-funding-round-with-2-billion-in-debt.html",
            quell_titel="Databricks completes $5 billion funding round at $134 billion valuation",
            kontext="Bewertungssteigerung von $62B (Dez 2024) auf $134B (Feb 2026). Vorbereitung für möglichen IPO 2026. Databricks erreichte >$3B revenue run-rate und Cash-Flow-Positivität."
        )

        # Handlung 10: Delta Lake 2.0 Open Source
        insert_handlung(
            cursor,
            handlung_typ="spende",
            beschreibung="Open-Sourcing aller Delta Lake Features und APIs als Delta Lake 2.0. Vollständige Donation aller proprietären Erweiterungen zur Linux Foundation.",
            datum_handlung="2022-06-28",
            quell_link="https://siliconangle.com/2022/06/28/databricks-donates-delta-lake-framework-mlflow-operations-platform-entirely-open-source/",
            quell_titel="Databricks donates Delta Lake framework and MLflow operations platform entirely to open source",
            kontext="Data + AI Summit Ankündigung. Komplette Open-Source-Spende aller Delta Lake APIs und Features. Auch MLflow vollständig open-sourced. Zeigt langfristiges Commitment zu Open Source."
        )

        print(f"[OK]Inserted 10 actions (Handlungen)")

        # Commit changes
        conn.commit()
        print("=" * 70)
        print(f"[OK]Successfully committed all data to database")
        print(f"[OK]Ali Ghodsi (person_id={PERSON_ID}) - Tier 2 collection COMPLETE")
        print(f"  - 12 Aussagen (Statements)")
        print(f"  - 10 Handlungen (Actions)")

    except sqlite3.Error as e:
        print(f"[ERROR]Database error: {e}")
        conn.rollback()
        raise
    except Exception as e:
        print(f"[ERROR]Error: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    main()
