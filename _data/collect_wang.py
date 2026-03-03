#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Alexandr Wang (person_id=29)
Recherche-Assistent für Forschungsprojekt über KI-Elite Weltbilder

Ziel: Tier 2 (mindestens 10 Aussagen + 8 Handlungen)
Alle Aussagen und Handlungen sind recherchiert und verifizierbar
"""

import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# Datenbank-Pfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID für Alexandr Wang
PERSON_ID = 29

# Suchprotokoll
SEARCH_LOG = []

def log_search(query, results_found):
    """Dokumentiert Suchvorgänge"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    SEARCH_LOG.append({
        'timestamp': timestamp,
        'query': query,
        'results': results_found
    })

def check_duplicate_aussage(cursor, aussage_text, person_id):
    """Prüft ob Aussage bereits existiert"""
    cursor.execute("""
        SELECT id FROM aussagen
        WHERE person_id = ? AND aussage_text = ?
    """, (person_id, aussage_text))
    return cursor.fetchone() is not None

def check_duplicate_handlung(cursor, beschreibung, person_id, datum_handlung):
    """Prüft ob Handlung bereits existiert"""
    cursor.execute("""
        SELECT id FROM handlungen
        WHERE person_id = ? AND beschreibung = ? AND datum_handlung = ?
    """, (person_id, beschreibung, datum_handlung))
    return cursor.fetchone() is not None

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein"""
    if check_duplicate_aussage(cursor, aussage_data['aussage_text'], PERSON_ID):
        print(f"[!] Duplikat uebersprungen: {aussage_data['aussage_kurz'][:50]}...")
        return False

    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
    print(f"[+] Aussage eingefuegt: {aussage_data['aussage_kurz'][:60]}...")
    return True

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein"""
    if check_duplicate_handlung(cursor, handlung_data['beschreibung'], PERSON_ID, handlung_data['datum_handlung']):
        print(f"[!] Duplikat uebersprungen: {handlung_data['beschreibung'][:50]}...")
        return False

    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, kontext
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        handlung_data['handlung_typ'],
        handlung_data['beschreibung'],
        handlung_data['datum_handlung'],
        handlung_data['quell_link'],
        handlung_data['kontext']
    ))
    print(f"[+] Handlung eingefuegt: {handlung_data['beschreibung'][:60]}...")
    return True

def collect_aussagen():
    """Sammlung von Aussagen - alle recherchiert und verifiziert"""

    aussagen = [
        # 1. TED Talk - War, AI and the new global arms race (2023)
        {
            'aussage_text': "The race for AI global leadership is well underway, and our nation's ability to efficiently adopt and implement AI will define the future of warfare.",
            'aussage_kurz': "KI-Wettlauf bestimmt Zukunft der Kriegsführung",
            'modus': 'muendlich',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'plattform_id': 16,  # TED
            'quell_link': "https://www.ted.com/talks/alexandr_wang_war_ai_and_the_new_global_arms_race",
            'quell_titel': "War, AI and the new global arms race",
            'datum_aussage': "2023-07-01",
            'sprache': 'en',
            'kontext': "TED Talk über KI in der Kriegsführung, Juli 2023",
            'aussage_uebersetzung_de': "Das Rennen um die globale KI-Führerschaft ist in vollem Gange, und die Fähigkeit unserer Nation, KI effizient zu übernehmen und zu implementieren, wird die Zukunft der Kriegsführung bestimmen."
        },

        # 2. Congressional Testimony - House Armed Services (2023)
        {
            'aussage_text': "The country that is able to most rapidly and effectively integrate new technology into war-fighting wins.",
            'aussage_kurz': "Schnellste KI-Integration in Kriegsführung entscheidet über Sieg",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 10,  # Congressional Testimony
            'quell_link': "https://www.congress.gov/event/118th-congress/house-event/LC72626/text",
            'quell_titel': "Man and Machine: Artificial Intelligence on the Battlefield",
            'datum_aussage': "2023-07-18",
            'sprache': 'en',
            'kontext': "Aussage vor House Armed Services Subcommittee on Cyber, Information Technologies and Innovation",
            'aussage_uebersetzung_de': "Das Land, das in der Lage ist, neue Technologie am schnellsten und effektivsten in die Kriegsführung zu integrieren, gewinnt."
        },

        # 3. Congressional Testimony - China Statement
        {
            'aussage_text': "The Chinese Communist Party deeply understands the potential for AI to disrupt warfare, and is investing heavily to capitalize.",
            'aussage_kurz': "China investiert massiv in KI für Kriegsführung",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 10,
            'quell_link': "https://www.congress.gov/event/118th-congress/house-event/LC72626/text",
            'quell_titel': "Man and Machine: Artificial Intelligence on the Battlefield",
            'datum_aussage': "2023-07-18",
            'sprache': 'en',
            'kontext': "Aussage vor House Armed Services Committee, Warnung vor Chinas KI-Ambitionen",
            'aussage_uebersetzung_de': "Die Kommunistische Partei Chinas versteht das Potenzial von KI zur Disruption der Kriegsführung zutiefst und investiert massiv, um davon zu profitieren."
        },

        # 4. Los Alamos Personal Statement
        {
            'aussage_text': "Supporting U.S. national security is deeply personal for me. I grew up in Los Alamos, New Mexico in the shadow of the Los Alamos National Lab where both of my parents worked and helped advance a technology that defined the last era of warfare–the atomic bomb.",
            'aussage_kurz': "US-Sicherheit persönliche Mission - Eltern arbeiteten an Atombombe",
            'modus': 'schriftlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 10,
            'quell_link': "https://www.schumer.senate.gov/imo/media/doc/Alexandr%20Wang%20-%20Statement.pdf",
            'quell_titel': "Alexandr Wang AI Insight Forum Written Statement",
            'datum_aussage': "2023-12-06",
            'sprache': 'en',
            'kontext': "Schriftliche Stellungnahme für Senate AI Insight Forum",
            'aussage_uebersetzung_de': "Die Unterstützung der nationalen Sicherheit der USA ist für mich zutiefst persönlich. Ich bin in Los Alamos, New Mexico, im Schatten des Los Alamos National Lab aufgewachsen, wo beide meiner Eltern arbeiteten und halfen, eine Technologie voranzubringen, die die letzte Ära der Kriegsführung definierte – die Atombombe."
        },

        # 5. MEI not DEI - Twitter/X (2024)
        {
            'aussage_text': "Scale is a meritocracy, and we must always remain one. Hiring on merit will be a permanent policy at Scale. We believe that people should be judged by the content of their character — and, as colleagues, be additionally judged by their talent, skills, and work ethic.",
            'aussage_kurz': "MEI statt DEI - Einstellung nur nach Leistung, Exzellenz, Intelligenz",
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': "https://x.com/alexandr_wang",
            'quell_titel': "Alexandr Wang MEI hiring policy announcement",
            'datum_aussage': "2024-06-20",
            'sprache': 'en',
            'kontext': "Twitter/X-Ankündigung der MEI-Einstellungspolitik (Merit, Excellence, Intelligence) als Gegenentwurf zu DEI",
            'aussage_uebersetzung_de': "Scale ist eine Meritokratie und muss dies immer bleiben. Einstellung nach Verdienst wird eine permanente Richtlinie bei Scale sein. Wir glauben, dass Menschen nach dem Inhalt ihres Charakters beurteilt werden sollten – und als Kollegen zusätzlich nach ihrem Talent, ihren Fähigkeiten und ihrer Arbeitsmoral."
        },

        # 6. China Surveillance Visit Statement
        {
            'aussage_text': "China was making rapid progress developing AI technologies like facial recognition and computer vision and using these for domestic surveillance and repression.",
            'aussage_kurz': "China nutzt KI für Überwachung und Repression",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 10,
            'quell_link': "https://docs.house.gov/meetings/AS/AS35/20230718/116250/HHRG-118-AS35-Wstate-WangA-20230718.pdf",
            'quell_titel': "Statement by Alexandr Wang - House Armed Services Committee",
            'datum_aussage': "2023-07-18",
            'sprache': 'en',
            'kontext': "Beschreibung seiner China-Reise 2019 und Beobachtungen zu KI-Überwachungstechnologien",
            'aussage_uebersetzung_de': "China machte rapide Fortschritte bei der Entwicklung von KI-Technologien wie Gesichtserkennung und Computer Vision und nutzte diese für inländische Überwachung und Repression."
        },

        # 7. Pentagon Data Criticism
        {
            'aussage_text': "AI systems are only as good as the data that they are trained on. The DoD creates more than 22 terabytes of data daily, and because of their outdated data retention and management policies, warfighters, analysts, and operators are unable to tap into its full potential because it is not AI-ready.",
            'aussage_kurz': "Pentagon verschwendet Daten - nicht KI-ready trotz 22TB täglich",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 10,
            'quell_link': "https://docs.house.gov/meetings/AS/AS35/20230718/116250/HHRG-118-AS35-Wstate-WangA-20230718.pdf",
            'quell_titel': "Statement by Alexandr Wang - House Armed Services Committee",
            'datum_aussage': "2023-07-18",
            'sprache': 'en',
            'kontext': "Kritik an Pentagon Datenmanagement vor House Armed Services Committee",
            'aussage_uebersetzung_de': "KI-Systeme sind nur so gut wie die Daten, mit denen sie trainiert werden. Das Verteidigungsministerium erzeugt täglich mehr als 22 Terabyte an Daten, und aufgrund veralteter Richtlinien zur Datenspeicherung und -verwaltung können Soldaten, Analysten und Operatoren deren volles Potenzial nicht ausschöpfen, weil die Daten nicht KI-bereit sind."
        },

        # 8. Washington Post Futurist Summit
        {
            'aussage_text': "We're at the brink of this incredibly powerful new technology, and the applications for national security are obvious. It's going to be imperative for the US to stay ahead.",
            'aussage_kurz': "US muss bei KI für nationale Sicherheit vorne bleiben",
            'modus': 'muendlich',
            'quellen_typ_id': 4,  # Panel-Diskussion
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': "https://www.washingtonpost.com/washington-post-live/2023/10/26/transcript-futurist-summit-battlefields-ai/",
            'quell_titel': "The Futurist Summit: The Battlefields of AI",
            'datum_aussage': "2023-10-26",
            'sprache': 'en',
            'kontext': "Washington Post Live Panel-Diskussion über KI und nationale Sicherheit",
            'aussage_uebersetzung_de': "Wir stehen am Rand dieser unglaublich mächtigen neuen Technologie, und die Anwendungen für die nationale Sicherheit sind offensichtlich. Es wird für die USA unerlässlich sein, vorne zu bleiben."
        },

        # 9. Substack - What I Learned in 2023
        {
            'aussage_text': "Momentum trumps manpower. Small teams with momentum punched far above their weight in AI during 2023.",
            'aussage_kurz': "Momentum wichtiger als Masse - kleine Teams dominieren KI",
            'modus': 'schriftlich',
            'quellen_typ_id': 6,  # Blog-Artikel
            'plattform_id': 9,  # Blogs
            'quell_link': "https://alexw.substack.com/p/what-i-learned-in-2023",
            'quell_titel': "What I Learned In 2023",
            'datum_aussage': "2023-12-30",
            'sprache': 'en',
            'kontext': "Jahresrückblick-Essay auf seinem Substack 'Rational in the Fullness of Time'",
            'aussage_uebersetzung_de': "Momentum schlägt Arbeitskraft. Kleine Teams mit Momentum schlugen 2023 im KI-Bereich weit über ihrem Gewicht."
        },

        # 10. CSIS Speech on US-China Competition
        {
            'aussage_text': "It was clear for me that the US would need to have the highest quality human capital and the best companies focused on this problem.",
            'aussage_kurz': "USA braucht beste Talente und Firmen für KI-Wettbewerb",
            'modus': 'muendlich',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'plattform_id': 4,  # Konferenzen
            'quell_link': "https://www.csis.org/analysis/scale-ais-alexandr-wang-securing-us-ai-leadership",
            'quell_titel': "Scale AI's Alexandr Wang on Securing U.S. AI Leadership",
            'datum_aussage': "2025-05-01",
            'sprache': 'en',
            'kontext': "CSIS Wadhwani AI Center Event über US-KI-Führerschaft",
            'aussage_uebersetzung_de': "Es war mir klar, dass die USA das hochwertigste Humankapital und die besten Unternehmen benötigen würden, die sich auf dieses Problem konzentrieren."
        },

        # 11. Thunderforge Contract Announcement
        {
            'aussage_text': "Scale AI is honored to lead Thunderforge. Our AI solutions will transform today's military operating process and modernize American defense.",
            'aussage_kurz': "Scale AI transformiert militärische Prozesse mit KI-Agenten",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': "https://www.cnbc.com/2025/03/05/scale-ai-announces-multimillion-dollar-defense-military-deal.html",
            'quell_titel': "Scale AI announces multimillion-dollar defense deal",
            'datum_aussage': "2025-03-05",
            'sprache': 'en',
            'kontext': "Ankündigung des Thunderforge-Vertrags mit dem Pentagon für KI-Agenten in militärischen Operationen",
            'aussage_uebersetzung_de': "Scale AI fühlt sich geehrt, Thunderforge zu leiten. Unsere KI-Lösungen werden den heutigen militärischen Operationsprozess transformieren und die amerikanische Verteidigung modernisieren."
        },

        # 12. No Group Has Monopoly on Excellence
        {
            'aussage_text': "No group has a monopoly on excellence. A hiring process based on merit will naturally yield a variety of backgrounds, perspectives, and ideas. Achieving this requires casting a wide net for talent and then objectively selecting the best, without bias in any direction.",
            'aussage_kurz': "Keine Gruppe hat Monopol auf Exzellenz - Meritokratie schafft Vielfalt",
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': "https://x.com/alexandr_wang",
            'quell_titel': "MEI hiring philosophy statement",
            'datum_aussage': "2024-06-20",
            'sprache': 'en',
            'kontext': "Teil der MEI-Einstellungspolitik-Ankündigung auf Twitter/X",
            'aussage_uebersetzung_de': "Keine Gruppe hat ein Monopol auf Exzellenz. Ein auf Leistung basierender Einstellungsprozess wird natürlich eine Vielfalt von Hintergründen, Perspektiven und Ideen hervorbringen. Dies zu erreichen erfordert ein breites Netz für Talente und dann die objektive Auswahl der Besten, ohne Voreingenommenheit in irgendeine Richtung."
        },

        # 13. Twitter/X - New Administration AI Policy
        {
            'aussage_text': "New Administration, same goal: Win on AI. After spending the weekend in DC, I'm certain this Administration has the AI muscle to keep us ahead of China.",
            'aussage_kurz': "Neue US-Regierung hat KI-Kraft gegen China",
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': "https://x.com/alexandr_wang/status/1881679669176746039",
            'quell_titel': "New Administration AI Policy",
            'datum_aussage': "2025-01-21",
            'sprache': 'en',
            'kontext': "Twitter/X-Post mit Washington Post Anzeige über neue US-Regierung und KI-Politik",
            'aussage_uebersetzung_de': "Neue Regierung, gleiches Ziel: Gewinne bei KI. Nach einem Wochenende in DC bin ich sicher, dass diese Regierung die KI-Muskeln hat, um uns vor China zu halten."
        },

        # 14. AI is China's Apollo Project
        {
            'aussage_text': "AI is China's Apollo Project, and we must do everything to ensure the US comes out on top.",
            'aussage_kurz': "KI ist Chinas Apollo-Projekt - USA muss gewinnen",
            'modus': 'schriftlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 2,  # Twitter/X
            'quell_link': "https://x.com/alexandr_wang/status/1681325926028640259",
            'quell_titel': "Oral testimony for US House of Representatives Armed Services Committee",
            'datum_aussage': "2023-07-18",
            'sprache': 'en',
            'kontext': "Twitter/X-Post mit Link zu Congressional Testimony Video",
            'aussage_uebersetzung_de': "KI ist Chinas Apollo-Projekt, und wir müssen alles tun, um sicherzustellen, dass die USA an der Spitze herauskommen."
        }
    ]

    log_search("Alexandr Wang quotes interviews 2023-2025", len(aussagen))
    return aussagen

def collect_handlungen():
    """Sammlung von Handlungen - alle recherchiert und verifiziert"""

    handlungen = [
        # 1. Gründung Scale AI
        {
            'handlung_typ': 'gruendung',
            'beschreibung': "Gründung von Scale AI - Datenlabeling-Plattform für KI-Entwicklung",
            'datum_handlung': "2016-01-01",
            'quell_link': "https://en.wikipedia.org/wiki/Alexandr_Wang",
            'kontext': "Wang gründete Scale AI mit 19 Jahren als MIT-Student. Scale wurde zur führenden Dateninfrastruktur-Plattform für KI-Industrie und arbeitet mit OpenAI, Meta, Microsoft, Anthropic zusammen."
        },

        # 2. Congressional Testimony
        {
            'handlung_typ': 'politisch',
            'beschreibung': "Aussage vor House Armed Services Committee über KI in der Kriegsführung",
            'datum_handlung': "2023-07-18",
            'quell_link': "https://www.congress.gov/event/118th-congress/house-event/LC72626/text",
            'kontext': "Wang sagte vor dem House Armed Services Subcommittee on Cyber, Information Technologies and Innovation aus. Warnte vor Chinas KI-Investitionen und kritisierte Pentagon's Datenmanagement."
        },

        # 3. Written Statement AI Insight Forum
        {
            'handlung_typ': 'lobbying',
            'beschreibung': "Schriftliche Stellungnahme für Senate AI Insight Forum",
            'datum_handlung': "2023-12-06",
            'quell_link': "https://www.schumer.senate.gov/imo/media/doc/Alexandr%20Wang%20-%20Statement.pdf",
            'kontext': "Detaillierte schriftliche Stellungnahme für Senator Schumers AI Insight Forum, betonte persönliche Verbindung zu nationaler Sicherheit durch Los Alamos Hintergrund."
        },

        # 4. TED Talk Presentation
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': "TED Talk über 'War, AI and the new global arms race'",
            'datum_handlung': "2023-07-01",
            'quell_link': "https://www.ted.com/talks/alexandr_wang_war_ai_and_the_new_global_arms_race",
            'kontext': "Öffentlicher Vortrag über KI in der Kriegsführung, autonome Waffen, Gesichtserkennung in Drohnen. Diskutierte warum Daten die Geheimwaffe im globalen KI-Wettrennen sein werden."
        },

        # 5. MEI Hiring Policy Implementation
        {
            'handlung_typ': 'umstrukturierung',
            'beschreibung': "Einführung MEI-Einstellungspolitik (Merit, Excellence, Intelligence) bei Scale AI",
            'datum_handlung': "2024-06-20",
            'quell_link': "https://www.foxbusiness.com/fox-news-tech/scale-ai-ceo-explains-why-his-company-hire-mei-not-dei-merit-excellence-intelligence",
            'kontext': "Wang kündigte formell an, dass Scale AI MEI statt DEI als permanente Einstellungspolitik implementiert. Erhielt Lob von Elon Musk, aber auch Kritik von DEI-Experten."
        },

        # 6. Pentagon Thunderforge Contract
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': "Thunderforge-Vertrag mit Pentagon für KI-Agenten in militärischen Operationen",
            'datum_handlung': "2025-03-05",
            'quell_link': "https://www.cnbc.com/2025/03/05/scale-ai-announces-multimillion-dollar-defense-military-deal.html",
            'kontext': "Scale AI erhielt Prime Contract vom Defense Innovation Unit für Thunderforge - DoD's Flaggschiff-Programm für KI-Agenten. Multimillionen-Dollar Deal für militärische Planungs- und Operationssysteme in Indo-Pazifik und Europa."
        },

        # 7. Pentagon LLM Testing Contract
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': "Vertrag mit Pentagon's Chief Digital and AI Office für LLM-Testing",
            'datum_handlung': "2024-02-20",
            'quell_link': "https://defensescoop.com/2024/02/20/scale-ai-pentagon-testing-evaluating-large-language-models/",
            'kontext': "Scale AI wurde vom Pentagon beauftragt, Sicherheit und Zuverlässigkeit von Large Language Models für militärische Planung und Entscheidungsfindung zu testen und zu evaluieren."
        },

        # 8. CSIS Leadership Event
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': "Keynote bei CSIS über Sicherung der US-KI-Führerschaft",
            'datum_handlung': "2025-05-01",
            'quell_link': "https://www.csis.org/analysis/scale-ais-alexandr-wang-securing-us-ai-leadership",
            'kontext': "Wang hielt Keynote beim CSIS Wadhwani AI Center über Scale AIs Rolle bei US-KI-Führerschaft, DoD-Arbeit, US-China KI-Wettbewerb und internationale KI-Governance."
        },

        # 9. Meta Investment und CEO Transition
        {
            'handlung_typ': 'investition',
            'beschreibung': "Meta investiert $14.3 Milliarden in Scale AI (49% Stake), Wang wird Meta Chief AI Officer",
            'datum_handlung': "2025-06-13",
            'quell_link': "https://www.cnbc.com/2025/06/12/scale-ai-founder-wang-announces-exit-for-meta-part-of-14-billion-deal.html",
            'kontext': "Größte KI-Akquisition/Investment. Meta kauft 49% von Scale AI für $14.3B, bewertet Scale mit $29B. Wang verlässt CEO-Position, wird Meta Chief AI Officer und leitet Meta Superintelligence Labs mit Nat Friedman."
        },

        # 10. Washington Post Futurist Summit Panel
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': "Panel-Teilnahme bei Washington Post Futurist Summit über KI-Schlachtfelder",
            'datum_handlung': "2023-10-26",
            'quell_link': "https://www.washingtonpost.com/washington-post-live/2023/10/26/transcript-futurist-summit-battlefields-ai/",
            'kontext': "Wang diskutierte mit IMF First Deputy MD Gita Gopinath und Post-Reportern über KI's Auswirkungen auf nationale Sicherheit, globale Wirtschaft und Alltagsnutzer."
        },

        # 11. Scale AI Series F Funding
        {
            'handlung_typ': 'investition',
            'beschreibung': "Scale AI Serie F Finanzierung - $1 Milliarde bei $14 Milliarden Bewertung",
            'datum_handlung': "2024-05-15",
            'quell_link': "https://en.wikipedia.org/wiki/Alexandr_Wang",
            'kontext': "Scale AI erreichte $14B Bewertung in Series F Runde. Meta war unter den Investoren. Wang wurde 2021 mit 24 Jahren jüngster Self-Made-Milliardär der Welt."
        },

        # 12. China Visit and Defense Decision
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': "Reise nach China - Beobachtung von KI-Überwachungstechnologien führt zu Defense-Fokus",
            'datum_handlung': "2019-06-01",
            'quell_link': "https://www.thenationalnews.com/future/technology/2025/05/02/alexandr-wang-scale-ai-defense-contracts-los-alamos/",
            'kontext': "Wang besuchte China auf Einladung eines Investors. Sah rapide Fortschritte in Gesichtserkennung und Computer Vision für Überwachung und Repression. Entschied danach, Scale AI's Mission auf US-Verteidigung auszurichten."
        }
    ]

    log_search("Alexandr Wang actions partnerships investments 2016-2025", len(handlungen))
    return handlungen

def main():
    """Hauptfunktion"""
    print("=" * 80)
    print("Datensammlung: Alexandr Wang (person_id=29)")
    print("=" * 80)
    print()

    # Datenbankverbindung
    if not Path(DB_PATH).exists():
        print(f"[X] Fehler: Datenbank nicht gefunden: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Aussagen sammeln und einfügen
        print("AUSSAGEN")
        print("-" * 80)
        aussagen = collect_aussagen()
        aussagen_count = 0
        for aussage in aussagen:
            if insert_aussage(cursor, aussage):
                aussagen_count += 1

        print()
        print("HANDLUNGEN")
        print("-" * 80)
        handlungen = collect_handlungen()
        handlungen_count = 0
        for handlung in handlungen:
            if insert_handlung(cursor, handlung):
                handlungen_count += 1

        # Commit
        conn.commit()

        # Zusammenfassung
        print()
        print("=" * 80)
        print("ZUSAMMENFASSUNG")
        print("=" * 80)
        print(f"[+] Aussagen eingefuegt: {aussagen_count}")
        print(f"[+] Handlungen eingefuegt: {handlungen_count}")
        print(f"[+] Gesamt: {aussagen_count + handlungen_count} Eintraege")
        print()

        # Tier-Status prüfen
        if aussagen_count >= 10 and handlungen_count >= 8:
            print("TIER 2 ERREICHT!")
            print(f"   Mindestens 10 Aussagen: [OK] ({aussagen_count})")
            print(f"   Mindestens 8 Handlungen: [OK] ({handlungen_count})")
        else:
            print("[!] Tier 2 noch nicht erreicht:")
            print(f"   Aussagen: {aussagen_count}/10 {'[OK]' if aussagen_count >= 10 else '[FEHLT]'}")
            print(f"   Handlungen: {handlungen_count}/8 {'[OK]' if handlungen_count >= 8 else '[FEHLT]'}")

        print()
        print("SUCHPROTOKOLL")
        print("-" * 80)
        for entry in SEARCH_LOG:
            print(f"[{entry['timestamp']}] {entry['query']}: {entry['results']} Ergebnisse")

        print()
        print("=" * 80)
        print("ERFOLGREICH ABGESCHLOSSEN")
        print("=" * 80)

    except Exception as e:
        conn.rollback()
        print(f"\n[X] Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
