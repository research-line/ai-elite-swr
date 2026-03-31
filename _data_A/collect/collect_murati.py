# -*- coding: utf-8 -*-
"""
Script zur Sammlung von Aussagen und Handlungen von Mira Murati (person_id=26)
für die KI-Elite Weltbilder Forschungsdatenbank
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 26  # Mira Murati

def get_db_connection():
    """Erstellt eine Datenbankverbindung."""
    return sqlite3.connect(DB_PATH)

def check_duplicate_aussage(cursor, person_id, aussage_text):
    """Prüft, ob eine Aussage bereits existiert."""
    cursor.execute("""
        SELECT COUNT(*) FROM aussagen
        WHERE person_id = ? AND aussage_text = ?
    """, (person_id, aussage_text))
    return cursor.fetchone()[0] > 0

def check_duplicate_handlung(cursor, person_id, beschreibung):
    """Prüft, ob eine Handlung bereits existiert."""
    cursor.execute("""
        SELECT COUNT(*) FROM handlungen
        WHERE person_id = ? AND beschreibung = ?
    """, (person_id, beschreibung))
    return cursor.fetchone()[0] > 0

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
            person_id, handlung_typ, beschreibung,
            datum_handlung, quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)

def main():
    print("="*80)
    print("MIRA MURATI - Datensammlung für Tier 2")
    print("="*80)
    print(f"Person ID: {PERSON_ID}")
    print(f"Ziel: Mindestens 10 Aussagen + 8 Handlungen")
    print("="*80)
    print()

    # Suchprotokoll
    search_log = []
    search_log.append("SUCHPROTOKOLL - Mira Murati")
    search_log.append("="*60)
    search_log.append("Datum: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    search_log.append("")
    search_log.append("SUCHSTRATEGIE:")
    search_log.append("1. TIME Magazine Interview (Feb 2023) - AI Regulation")
    search_log.append("2. Wall Street Journal Sora Interview (Mar 2024)")
    search_log.append("3. Dartmouth Speech (Jun 2024) - AI Future")
    search_log.append("4. GPT-4o Launch Demo (May 2024)")
    search_log.append("5. Creative Jobs Interview (Jun 2024)")
    search_log.append("6. Resignation Announcement (Sep 2024)")
    search_log.append("7. Thinking Machines Lab Founding (Feb 2025)")
    search_log.append("8. Career History (Tesla, Leap Motion, OpenAI)")
    search_log.append("")

    conn = get_db_connection()
    cursor = conn.cursor()

    aussagen_count = 0
    handlungen_count = 0
    duplicates_aussagen = 0
    duplicates_handlungen = 0

    # ========================================================================
    # AUSSAGEN (Ziel: mindestens 10)
    # ========================================================================

    aussagen = [
        # 1. TIME Magazine - AI Regulation (Feb 2023)
        (PERSON_ID,
         "It's important for OpenAI and companies like ours to bring this into the public consciousness in a way that's controlled and responsible. But we're a small group of people and we need a ton more input into the system from, you know, from people in the world, from society, from regulators and governments and so on.",
         "OpenAI braucht Input von Gesellschaft und Regierungen für verantwortungsvolle KI-Entwicklung",
         "schriftlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://time.com/6252404/mira-murati-chatgpt-openai-interview/",
         "Mira Murati, Creator of ChatGPT, Thinks AI Should Be Regulated | TIME",
         "2023-02-01",
         "en",
         "Interview mit TIME Magazine über ChatGPT und die Notwendigkeit von KI-Regulierung",
         "Es ist wichtig für OpenAI und ähnliche Unternehmen, dies auf kontrollierte und verantwortungsvolle Weise ins öffentliche Bewusstsein zu bringen. Aber wir sind eine kleine Gruppe von Menschen und brauchen viel mehr Input von Menschen in der Welt, von der Gesellschaft, von Regulierungsbehörden und Regierungen."
        ),

        # 2. TIME Magazine - AI Safety
        (PERSON_ID,
         "For capabilities and safety, they're actually not separate domains. They go hand-in-hand. It's much easier to direct a smarter system by telling it, okay, just don't do these things.",
         "Fähigkeiten und Sicherheit gehen Hand in Hand - intelligentere Systeme sind leichter zu steuern",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://time.com/6252404/mira-murati-chatgpt-openai-interview/",
         "Mira Murati, Creator of ChatGPT, Thinks AI Should Be Regulated | TIME",
         "2023-02-01",
         "en",
         "TIME Interview über die Beziehung zwischen KI-Fähigkeiten und Sicherheit",
         "Für Fähigkeiten und Sicherheit sind es eigentlich keine getrennten Bereiche. Sie gehen Hand in Hand. Es ist viel einfacher, ein intelligenteres System zu steuern, indem man ihm sagt: Okay, mach diese Dinge einfach nicht."
        ),

        # 3. Creative Jobs Interview (Jun 2024)
        (PERSON_ID,
         "Some creative jobs maybe will go away, but maybe they shouldn't have been there in the first place.",
         "Einige kreative Jobs könnten verschwinden, aber vielleicht sollten sie von Anfang an nicht da gewesen sein",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://www.cnbc.com/2024/06/26/openai-cto-mira-murati-ai-may-cause-some-creative-jobs-to-disappear.html",
         "OpenAI CTO Mira Murati: AI may cause some creative jobs to disappear",
         "2024-06-21",
         "en",
         "Interview über die Auswirkungen von KI auf kreative Berufe - führte zu erheblichem Backlash",
         "Einige kreative Jobs werden vielleicht verschwinden, aber vielleicht hätten sie von vornherein nicht existieren sollen."
        ),

        # 4. Dartmouth Speech - AI Impact
        (PERSON_ID,
         "Everything. There's not going to be an area that won't be affected in terms of cognitive work.",
         "KI wird alle Bereiche kognitiver Arbeit beeinflussen",
         "muendlich",
         3,  # Keynote/Vortrag
         4,  # Konferenzen
         "https://engineering.dartmouth.edu/news/openai-cto-mira-murati-th12-shares-optimism-for-ais-future",
         "OpenAI CTO Mira Murati Th'12 Shares Optimism for AI's Future",
         "2024-06-01",
         "en",
         "Antwort auf die Frage, welche Industrien am meisten von KI betroffen sein werden, bei Dartmouth Event",
         "Alles. Es wird keinen Bereich geben, der im Hinblick auf kognitive Arbeit nicht betroffen sein wird."
        ),

        # 5. Dartmouth - PhD-Level AI
        (PERSON_ID,
         "Computers may exhibit PhD-level intelligence for specific tasks in coming years, and while that rings alarm bells for many, she believes smarter AI will not only be more helpful—but also safer.",
         "KI mit Doktoranden-Niveau wird nicht nur hilfreicher, sondern auch sicherer sein",
         "muendlich",
         3,  # Keynote/Vortrag
         4,  # Konferenzen
         "https://engineering.dartmouth.edu/news/openai-cto-mira-murati-th12-shares-optimism-for-ais-future",
         "OpenAI CTO Mira Murati Th'12 Shares Optimism for AI's Future",
         "2024-06-01",
         "en",
         "Dartmouth Event über die Zukunft von KI und Sicherheit fortgeschrittener Systeme",
         "Computer könnten in den kommenden Jahren Intelligenz auf Doktoranden-Niveau für spezifische Aufgaben zeigen, und obwohl das bei vielen Alarmglocken läuten lässt, glaubt sie, dass intelligentere KI nicht nur hilfreicher, sondern auch sicherer sein wird."
        ),

        # 6. GPT-4o Launch
        (PERSON_ID,
         "GPT-4o provides GPT-4 intelligence, but it is much faster, and it improves on its capabilities across text, vision and audio.",
         "GPT-4o bietet GPT-4-Intelligenz, aber viel schneller und mit besseren Fähigkeiten bei Text, Vision und Audio",
         "muendlich",
         3,  # Keynote/Vortrag
         4,  # Konferenzen
         "https://www.ciodive.com/news/openai-faster-cheaper-gpt-4o-model/715965/",
         "OpenAI introduces faster, cheaper GPT-4o model",
         "2024-05-13",
         "en",
         "Präsentation von GPT-4o bei OpenAI Spring Update Event",
         "GPT-4o bietet GPT-4-Intelligenz, aber es ist viel schneller und verbessert seine Fähigkeiten über Text, Vision und Audio hinweg."
        ),

        # 7. Wall Street Journal - Sora Training Data
        (PERSON_ID,
         "I'm actually not sure about that.",
         "Murati war unsicher über Sora-Trainingsdaten",
         "muendlich",
         1,  # Video-Interview
         5,  # Nachrichtenmedien
         "https://the-decoder.com/openai-cto-mira-murati-doesnt-know-what-data-sora-was-trained-on/",
         "OpenAI CTO Mira Murati doesn't know what data Sora was trained on",
         "2024-03-13",
         "en",
         "Antwort auf WSJ-Frage, ob Sora mit YouTube, Instagram oder Facebook-Daten trainiert wurde - führte zu Kontroverse",
         "Ich bin mir darüber tatsächlich nicht sicher."
        ),

        # 8. Resignation Announcement
        (PERSON_ID,
         "My six-and-a-half years with the OpenAI team have been an extraordinary privilege. I'm stepping away because I want to create the time and space to do my own exploration.",
         "Nach 6,5 Jahren verlässt Murati OpenAI für eigene Exploration",
         "muendlich",
         10,  # Offizielle Stellungnahme
         2,   # Twitter/X
         "https://www.cnbc.com/2024/09/25/openai-cto-mira-murati-announces-shes-leaving-the-company.html",
         "OpenAI considering restructuring to for-profit, CTO Mira Murati and two top research execs depart",
         "2024-09-25",
         "en",
         "Offizielle Rücktrittserklärung von Mira Murati als CTO von OpenAI",
         "Meine sechseinhalb Jahre mit dem OpenAI-Team waren ein außergewöhnliches Privileg. Ich gehe, weil ich mir die Zeit und den Raum schaffen möchte, um meine eigene Erkundung durchzuführen."
        ),

        # 9. AI Engineering Philosophy
        (PERSON_ID,
         "AI is a really incredible and magical technology, but the breadth, the reach, the consequence, is also great. Our entire world is engineering—like our cities, our bridges, everything—and there's always risk that comes with that, and you manage that risk with responsibility.",
         "KI ist magische Technologie mit großer Reichweite - Risiken müssen verantwortungsvoll gemanagt werden",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://washingtondc.jhu.edu/news/what-mira-murati-wants-you-to-know-about-openai/",
         "What Mira Murati wants you to know about OpenAI",
         "2023-04-01",
         "en",
         "Johns Hopkins Interview über KI-Entwicklung und Verantwortung",
         "KI ist eine wirklich unglaubliche und magische Technologie, aber die Breite, die Reichweite, die Konsequenzen sind ebenfalls groß. Unsere gesamte Welt ist Engineering - wie unsere Städte, unsere Brücken, alles - und damit kommt immer ein Risiko, und man managt dieses Risiko mit Verantwortung."
        ),

        # 10. ChatGPT AP Interview
        (PERSON_ID,
         "I expect that we will collaborate with it and it's going to make our creativity expand. It's going to lower the barrier for anyone to think of themselves as creative.",
         "KI wird Kreativität erweitern und die Barriere für kreatives Denken senken",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://www.ocregister.com/2023/04/24/insider-qa-openai-cto-mira-murati-on-shepherding-chatgpt/",
         "Insider Q&A: OpenAI CTO Mira Murati on shepherding ChatGPT",
         "2023-04-24",
         "en",
         "Associated Press Interview über ChatGPT und kreative Zusammenarbeit mit KI",
         "Ich erwarte, dass wir damit zusammenarbeiten werden und es unsere Kreativität erweitern wird. Es wird die Barriere für jeden senken, sich selbst als kreativ zu betrachten."
        ),

        # 11. Thinking Machines Lab Mission
        (PERSON_ID,
         "We're building multimodal AI that will be compatible with the ways that people naturally interact with the world, including through conversation and sight.",
         "Thinking Machines baut multimodale KI, die mit natürlichen menschlichen Interaktionen kompatibel ist",
         "muendlich",
         10,  # Offizielle Stellungnahme
         5,   # Nachrichtenmedien
         "https://techcrunch.com/2025/02/18/thinking-machines-lab-is-ex-openai-cto-mira-muratis-new-startup/",
         "Thinking Machines Lab is ex-OpenAI CTO Mira Murati's new startup",
         "2025-02-18",
         "en",
         "Ankündigung der Mission von Thinking Machines Lab",
         "Wir bauen multimodale KI, die mit den Arten kompatibel sein wird, wie Menschen natürlich mit der Welt interagieren, einschließlich durch Konversation und Sehen."
        ),

        # 12. GPT-4o Free Access
        (PERSON_ID,
         "This allows us to bring GPT-4 class intelligence to our free users.",
         "GPT-4-Intelligenz wird für kostenlose Nutzer verfügbar gemacht",
         "muendlich",
         3,  # Keynote/Vortrag
         4,  # Konferenzen
         "https://www.analyticsvidhya.com/blog/2024/05/openais-latest-gpt-o-unveiled-in-spring-update/",
         "GPT-4o: Free GPT-4 for All Unveiled in OpenAI's Spring Update",
         "2024-05-13",
         "en",
         "GPT-4o Launch Event - Ankündigung des kostenlosen Zugangs",
         "Dies ermöglicht es uns, GPT-4-Klasse-Intelligenz unseren kostenlosen Nutzern zu bringen."
        ),
    ]

    print("AUSSAGEN werden eingefügt...")
    print("-" * 60)

    for aussage in aussagen:
        aussage_text = aussage[1]
        if check_duplicate_aussage(cursor, PERSON_ID, aussage_text):
            duplicates_aussagen += 1
            print(f"  [DUPLIKAT] {aussage[2][:60]}...")
        else:
            insert_aussage(cursor, aussage)
            aussagen_count += 1
            print(f"  [NEU] {aussage[2][:60]}...")

    print()

    # ========================================================================
    # HANDLUNGEN (Ziel: mindestens 8)
    # ========================================================================

    handlungen = [
        # 1. Joined Tesla
        (PERSON_ID,
         "einstellung",
         "Senior Product Manager bei Tesla für Model X und Autopilot (2013-2016)",
         "2013-01-01",
         "https://en.wikipedia.org/wiki/Mira_Murati",
         "Mira Murati - Wikipedia",
         "Murati arbeitete 3 Jahre bei Tesla als Senior Product Manager für das Model X-Programm und war während der frühen Entwicklung von Autopilot dort."
        ),

        # 2. Joined Leap Motion
        (PERSON_ID,
         "einstellung",
         "Vice President of Product and Engineering bei Leap Motion (2016-2018)",
         "2016-01-01",
         "https://en.wikipedia.org/wiki/Mira_Murati",
         "Mira Murati - Wikipedia",
         "Nach Tesla wechselte Murati zu Leap Motion als VP of Product and Engineering, bevor sie zu OpenAI kam."
        ),

        # 3. Joined OpenAI
        (PERSON_ID,
         "einstellung",
         "Vice President of Applied AI and Partnerships bei OpenAI (Juni 2018)",
         "2018-06-01",
         "https://en.wikipedia.org/wiki/Mira_Murati",
         "Mira Murati - Wikipedia",
         "Murati kam zu OpenAI als VP of Applied AI and Partnerships - der Beginn ihrer 6,5-jährigen Karriere bei OpenAI."
        ),

        # 4. Promoted to CTO
        (PERSON_ID,
         "einstellung",
         "Beförderung zur Chief Technology Officer bei OpenAI (2022)",
         "2022-01-01",
         "https://techcrunch.com/2023/11/17/who-is-mira-murati-openais-new-interim-ceo/",
         "Who is Mira Murati, OpenAI's new interim CEO?",
         "Nach Beförderungen zu SVP of Research, Product and Partnerships wurde Murati 2022 zur CTO ernannt und leitete ChatGPT, DALL-E und Codex."
        ),

        # 5. Interim CEO
        (PERSON_ID,
         "einstellung",
         "Interim CEO von OpenAI nach Entlassung von Sam Altman (17.-21. November 2023)",
         "2023-11-17",
         "https://www.cnbc.com/2023/11/17/sam-altman-leaves-openai-mira-murati-appointed-interim-boss.html",
         "OpenAI's Sam Altman exits as CEO because 'board no longer has confidence'",
         "Nach Altmans Entlassung wurde Murati für 5 Tage zur Interim CEO ernannt, bevor Altman wieder eingesetzt wurde."
        ),

        # 6. GPT-4o Product Launch
        (PERSON_ID,
         "produktlaunch",
         "Leitung der GPT-4o Launch-Veranstaltung bei OpenAI Spring Update (13. Mai 2024)",
         "2024-05-13",
         "https://www.ciodive.com/news/openai-faster-cheaper-gpt-4o-model/715965/",
         "OpenAI introduces faster, cheaper GPT-4o model",
         "Murati präsentierte GPT-4o mit Echtzeit-Demos für multimodale Konversation, Vision und Übersetzung."
        ),

        # 7. Resignation from OpenAI
        (PERSON_ID,
         "ruecktritt",
         "Rücktritt als CTO von OpenAI nach 6,5 Jahren (25. September 2024)",
         "2024-09-25",
         "https://www.cnbc.com/2024/09/25/openai-cto-mira-murati-announces-shes-leaving-the-company.html",
         "OpenAI CTO Mira Murati announces she's leaving the company",
         "Murati kündigte ihren Rücktritt an, um 'Zeit und Raum für eigene Erkundungen zu schaffen' - Teil eines größeren Exodus von OpenAI-Führungskräften."
        ),

        # 8. Founded Thinking Machines Lab
        (PERSON_ID,
         "gruendung",
         "Gründung von Thinking Machines Lab als CEO (Februar 2025)",
         "2025-02-18",
         "https://techcrunch.com/2025/02/18/thinking-machines-lab-is-ex-openai-cto-mira-muratis-new-startup/",
         "Thinking Machines Lab is ex-OpenAI CTO Mira Murati's new startup",
         "Murati gründete Thinking Machines Lab mit ehemaligen OpenAI-Kollegen John Schulman (Chief Scientist) und Barret Zoph (CTO)."
        ),

        # 9. Thinking Machines Fundraising
        (PERSON_ID,
         "investition",
         "Abschluss einer 2 Milliarden Dollar Seed-Finanzierung bei 12 Milliarden Dollar Bewertung (Juli 2025)",
         "2025-07-15",
         "https://www.cnbc.com/2025/07/15/openai-mira-murati-thinking-machines-lab.html",
         "Former OpenAI CTO Mira Murati raises $2 billion for new AI startup Thinking Machines Lab",
         "Andreessen Horowitz führte die Finanzierungsrunde an. Auch die albanische Regierung investierte 10 Millionen Dollar."
        ),

        # 10. Tinker API Launch
        (PERSON_ID,
         "produktlaunch",
         "Launch von Tinker, einer API zum Fine-Tuning von Sprachmodellen (1. Oktober 2025)",
         "2025-10-01",
         "https://builtin.com/articles/what-is-thinking-machines-lab",
         "Inside Thinking Machines Lab, Mira Murati's New AI Startup",
         "Erstes Produkt von Thinking Machines Lab - eine API für Fine-Tuning verschiedener Open-Weight-Modelle auf interner Infrastruktur."
        ),
    ]

    print("HANDLUNGEN werden eingefügt...")
    print("-" * 60)

    for handlung in handlungen:
        beschreibung = handlung[2]
        if check_duplicate_handlung(cursor, PERSON_ID, beschreibung):
            duplicates_handlungen += 1
            print(f"  [DUPLIKAT] {beschreibung[:60]}...")
        else:
            insert_handlung(cursor, handlung)
            handlungen_count += 1
            print(f"  [NEU] {beschreibung[:60]}...")

    # Änderungen speichern
    conn.commit()
    conn.close()

    print()
    print("="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"Neu eingefügte Aussagen:        {aussagen_count}")
    print(f"Duplikate (Aussagen):            {duplicates_aussagen}")
    print(f"Neu eingefügte Handlungen:       {handlungen_count}")
    print(f"Duplikate (Handlungen):          {duplicates_handlungen}")
    print("="*80)

    # Tier-2-Status prüfen
    if aussagen_count >= 10 and handlungen_count >= 8:
        print("STATUS: TIER 2 ERREICHT [OK]")
    else:
        print(f"STATUS: Tier 2 noch nicht erreicht")
        print(f"  Benoetigt: 10 Aussagen (aktuell: {aussagen_count}), 8 Handlungen (aktuell: {handlungen_count})")

    print()

    # Suchprotokoll speichern
    search_log.append("ERGEBNISSE:")
    search_log.append(f"  - Neue Aussagen: {aussagen_count}")
    search_log.append(f"  - Neue Handlungen: {handlungen_count}")
    search_log.append(f"  - Duplikate Aussagen: {duplicates_aussagen}")
    search_log.append(f"  - Duplikate Handlungen: {duplicates_handlungen}")
    search_log.append("")
    search_log.append("QUELLEN:")
    search_log.append("  - TIME Magazine Interview (Feb 2023)")
    search_log.append("  - Associated Press Interview (Apr 2023)")
    search_log.append("  - Wall Street Journal Sora Interview (Mar 2024)")
    search_log.append("  - GPT-4o Launch Event (May 2024)")
    search_log.append("  - Dartmouth Speech (Jun 2024)")
    search_log.append("  - Creative Jobs Interview (Jun 2024)")
    search_log.append("  - Resignation Announcement (Sep 2024)")
    search_log.append("  - Thinking Machines Lab Launch (Feb 2025)")
    search_log.append("  - Seed Funding Announcement (Jul 2025)")
    search_log.append("  - Tinker API Launch (Oct 2025)")
    search_log.append("")

    log_file = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\collect_murati_log.txt"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(search_log))

    print(f"Suchprotokoll gespeichert: {log_file}")
    print()

if __name__ == "__main__":
    main()
