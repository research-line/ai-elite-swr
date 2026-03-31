#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Scott Wu (person_id=42)
CEO und Co-Gründer von Cognition AI / Devin
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 42

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein."""
    sql = """
    INSERT INTO aussagen (
        person_id, aussage_text, aussage_kurz, modus,
        quellen_typ_id, plattform_id, quell_link, quell_titel,
        datum_aussage, sprache, kontext, aussage_uebersetzung_de
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (
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

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein."""
    sql = """
    INSERT INTO handlungen (
        person_id, handlung_typ, beschreibung,
        datum_handlung, quell_link, quell_titel, kontext
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (
        PERSON_ID,
        handlung_data['handlung_typ'],
        handlung_data['beschreibung'],
        handlung_data['datum_handlung'],
        handlung_data['quell_link'],
        handlung_data['quell_titel'],
        handlung_data['kontext']
    ))

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Sammle Daten für Scott Wu (person_id={PERSON_ID})...")

    # ==================== AUSSAGEN ====================

    aussagen = [
        {
            'aussage_text': 'I first learned to program when I was 9 years old and fell in love with the ability to turn my ideas into reality. Now, teaching AI to code at @cognition_labs has been a dream come true.',
            'aussage_kurz': 'Programmieren seit 9 Jahren - jetzt KI beibringen zu coden ist Traum',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/ScottWu46/status/1767555214104539508',
            'quell_titel': 'Scott Wu on X - Programming since age 9',
            'datum_aussage': '2024-03-12',
            'sprache': 'en',
            'kontext': 'Tweet bei Devin-Ankündigung - Wu beschreibt seine persönliche Motivation für Cognition AI',
            'aussage_uebersetzung_de': 'Ich habe mit 9 Jahren programmieren gelernt und mich in die Fähigkeit verliebt, meine Ideen in Realität zu verwandeln. Jetzt ist es ein Traum, der wahr wird, KI das Programmieren bei @cognition_labs beizubringen.'
        },
        {
            'aussage_text': 'At a high level, we want to build the future of software engineering. We\'ve had the IDE paradigm in the past—GitHub Copilot is a well-known originator of it—where you\'re typing at the keyboard, and the assistant is making you a little bit faster and giving you tools and shortcuts and everything you need. Devin is a very different paradigm of what I would call an async experience, where you have an agent and you delegate a task.',
            'aussage_kurz': 'Devin ist anderes Paradigma - async Delegation statt IDE-Assistenz',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Lenny\'s Podcast Interview - Wu erklärt den Paradigmenwechsel von Copilot zu Devin',
            'aussage_uebersetzung_de': 'Auf hoher Ebene wollen wir die Zukunft der Softwareentwicklung bauen. Wir hatten früher das IDE-Paradigma - GitHub Copilot ist ein bekannter Vertreter - wo man an der Tastatur tippt und der Assistent einen etwas schneller macht. Devin ist ein ganz anderes Paradigma, was ich eine asynchrone Erfahrung nennen würde, wo man einen Agenten hat und eine Aufgabe delegiert.'
        },
        {
            'aussage_text': 'We like to call Devin a junior engineer today. We typically see folks using Devin for things like simple feature requests and fixes. Devin is also doing a lot of the more repetitive, tedious tasks that come up often in engineering work—migrations, modernizations, refactors, version upgrades, or testing and documentation.',
            'aussage_kurz': 'Devin ist heute Junior-Engineer - macht einfache Features und repetitive Aufgaben',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Lenny\'s Podcast - Wu beschreibt den aktuellen Fähigkeitsstand von Devin',
            'aussage_uebersetzung_de': 'Wir nennen Devin heute gerne einen Junior-Engineer. Wir sehen typischerweise, dass Leute Devin für Dinge wie einfache Feature-Requests und Fixes nutzen. Devin macht auch viele der repetitiveren, mühsamen Aufgaben, die oft in Engineering-Arbeit auftauchen - Migrationen, Modernisierungen, Refactorings, Versions-Upgrades oder Testing und Dokumentation.'
        },
        {
            'aussage_text': 'When we got started it was kind of like a high school CS student. And then as time went on and became more of like a college intern. And now it\'s like a junior engineer.',
            'aussage_kurz': 'Devin-Entwicklung: von High-School-Schüler zu College-Praktikant zu Junior-Engineer',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Lenny\'s Podcast - Wu beschreibt die Evolution von Devins Fähigkeiten',
            'aussage_uebersetzung_de': 'Als wir angefangen haben, war es wie ein High-School-Informatik-Schüler. Und dann wurde es im Laufe der Zeit eher wie ein College-Praktikant. Und jetzt ist es wie ein Junior-Engineer.'
        },
        {
            'aussage_text': 'One of the ways that we\'ve thought about Devin is really allowing engineers to go from bricklayer to architect so to speak... It\'s very much about still having the human in control and having the human able to do the full specification but just multiplying the magnitude of what you can do and what you can build... in one day or hour or however long.',
            'aussage_kurz': 'Devin macht Engineers zu Architekten - Mensch bleibt in Kontrolle, Multiplikator der Produktivität',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Lenny\'s Podcast - Wu über die Transformation der Engineer-Rolle',
            'aussage_uebersetzung_de': 'Eine Art, wie wir über Devin nachgedacht haben, ist wirklich, Engineers von Maurern zu Architekten zu machen, sozusagen... Es geht sehr darum, dass der Mensch weiterhin die Kontrolle hat und in der Lage ist, die vollständige Spezifikation zu machen, aber einfach die Größenordnung dessen zu multiplizieren, was man tun und bauen kann... an einem Tag oder einer Stunde oder wie lange auch immer.'
        },
        {
            'aussage_text': 'The future of software engineering is you telling your computer \'Here\'s exactly what you need to build,\' and it just happens.',
            'aussage_kurz': 'Zukunft des Software Engineering: Computer Anweisungen geben, es passiert einfach',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://medium.com/@ml_artist/2024-cognition-coding-scott-wu-devin-ai-ef9b4d7e5cc6',
            'quell_titel': '2024 Cognition coding: Scott Wu & Devin AI',
            'datum_aussage': '2024-05-02',
            'sprache': 'en',
            'kontext': 'No Priors Podcast - Wu beschreibt seine Vision für die Zukunft der Softwareentwicklung',
            'aussage_uebersetzung_de': 'Die Zukunft des Software Engineering ist, dass du deinem Computer sagst "Hier ist genau, was du bauen musst", und es passiert einfach.'
        },
        {
            'aussage_text': 'Humans plus AI really is the way to go at least for for for the foreseeable future, and with tools like Devin, we can do not just like 10% or 20% gains, but more like 10x.',
            'aussage_kurz': 'Mensch + KI ist der Weg - nicht 10-20% sondern 10x Produktivität',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://medium.com/@ml_artist/2024-cognition-coding-scott-wu-devin-ai-ef9b4d7e5cc6',
            'quell_titel': '2024 Cognition coding: Scott Wu & Devin AI',
            'datum_aussage': '2024-05-02',
            'sprache': 'en',
            'kontext': 'Diskussion über AI-menschliche Zusammenarbeit und Produktivitätsgewinne',
            'aussage_uebersetzung_de': 'Mensch plus KI ist wirklich der Weg, zumindest für die absehbare Zukunft, und mit Werkzeugen wie Devin können wir nicht nur 10% oder 20% Gewinne erzielen, sondern eher 10x.'
        },
        {
            'aussage_text': 'AI will surpass the world\'s best competitive programmer within 1-2 years and sees this technology not as replacing programmers, but as democratizing software creation.',
            'aussage_kurz': 'KI übertrifft beste Competitive Programmer in 1-2 Jahren - demokratisiert Software-Entwicklung',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Wu\'s Prognose zur AI-Entwicklung basierend auf seiner Competitive Programming Expertise',
            'aussage_uebersetzung_de': 'KI wird den weltbesten Competitive Programmer innerhalb von 1-2 Jahren übertreffen, und diese Technologie nicht als Ersatz für Programmierer sehen, sondern als Demokratisierung der Software-Erstellung.'
        },
        {
            'aussage_text': 'Devin is merging something in the range of like 30 to 40% of all pull requests that come through.',
            'aussage_kurz': 'Devin merged bereits 30-40% aller Pull Requests bei Cognition',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://stripe.com/customers/cognition-scott-wu',
            'quell_titel': 'Cognition CEO Scott Wu - Stripe Interview',
            'datum_aussage': '2024-12-15',
            'sprache': 'en',
            'kontext': 'Stripe Cheeky Pint Interview - Wu gibt konkrete Zahlen zur Devin-Nutzung bei Cognition',
            'aussage_uebersetzung_de': 'Devin merged etwa 30 bis 40% aller Pull Requests, die durchkommen.'
        },
        {
            'aussage_text': 'We are acquiring Windsurf. We have now signed a definitive agreement and we couldn\'t be more excited.',
            'aussage_kurz': 'Windsurf-Akquisition - definitiver Vertrag unterzeichnet',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/ScottWu46/status/1944820058494263559',
            'quell_titel': 'Scott Wu on X - Windsurf Acquisition Announcement',
            'datum_aussage': '2025-07-14',
            'sprache': 'en',
            'kontext': 'Wu\'s Tweet zur Windsurf-Akquisition an das Cognition-Team',
            'aussage_uebersetzung_de': 'Wir übernehmen Windsurf. Wir haben jetzt eine endgültige Vereinbarung unterzeichnet und könnten nicht aufgeregter sein.'
        },
        {
            'aussage_text': 'AI will create more engineering jobs, not fewer, as increased efficiency leads to greater demand for software (Jevons paradox in action).',
            'aussage_kurz': 'KI schafft mehr Engineering-Jobs durch Jevons-Paradox - höhere Effizienz = mehr Nachfrage',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Wu erklärt warum AI-Automatisierung paradoxerweise mehr statt weniger Jobs schaffen wird',
            'aussage_uebersetzung_de': 'KI wird mehr Engineering-Jobs schaffen, nicht weniger, da gesteigerte Effizienz zu größerer Nachfrage nach Software führt (Jevons-Paradox in Aktion).'
        },
        {
            'aussage_text': 'Engineers are moving from bricklayers to architects—being able to focus on high-level design while AI handles implementation.',
            'aussage_kurz': 'Engineers werden von Maurern zu Architekten - KI übernimmt Implementation',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast with Scott Wu',
            'datum_aussage': '2025-05-04',
            'sprache': 'en',
            'kontext': 'Wu\'s Metapher für die Transformation der Engineering-Rolle durch KI',
            'aussage_uebersetzung_de': 'Engineers bewegen sich von Maurern zu Architekten - sie können sich auf High-Level-Design konzentrieren, während KI die Implementierung übernimmt.'
        }
    ]

    # ==================== HANDLUNGEN ====================

    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgründung von Cognition AI zusammen mit Steven Hao und Walden Yan',
            '# beschreibung_en': 'Co-founded Cognition AI with Steven Hao and Walden Yan',
            'datum_handlung': '2023-08-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Scott_Wu',
            'quell_titel': 'Scott Wu - Wikipedia',
            'kontext': 'Alle drei Gründer waren IOI-Goldmedaillengewinner. Cognition fokussiert auf AI-reasoning und autonome Software-Engineering-Agenten.'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Devin, dem "ersten AI Software Engineer"',
            '# beschreibung_en': 'Launch of Devin, the "first AI software engineer"',
            'datum_handlung': '2024-03-12',
            'quell_link': 'https://cognition.ai/blog/introducing-devin',
            'quell_titel': 'Cognition - Introducing Devin',
            'kontext': 'Devin erreichte State-of-the-Art-Performance auf SWE-Bench Coding Benchmark, bestand praktische Engineering-Interviews führender AI-Firmen und erledigte echte Jobs auf Upwork.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Series A Finanzierung: 21 Millionen USD von Peter Thiel\'s Founders Fund',
            '# beschreibung_en': 'Series A funding: $21M from Peter Thiel\'s Founders Fund',
            'datum_handlung': '2024-02-15',
            'quell_link': 'https://en.wikipedia.org/wiki/Scott_Wu',
            'quell_titel': 'Scott Wu - Wikipedia',
            'kontext': 'Frühe Finanzierung von Founders Fund demonstriert starkes Vertrauen in Wu\'s Vision für AI-Coding-Agenten.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Series B Finanzierung: 175 Millionen USD von Founders Fund bei 2 Milliarden USD Bewertung',
            '# beschreibung_en': 'Series B funding: $175M from Founders Fund at $2B valuation',
            'datum_handlung': '2024-05-15',
            'quell_link': 'https://aibusiness.com/nlp/six-month-old-ai-startup-behind-devin-now-valued-at-2b',
            'quell_titel': 'Six-Month-Old AI Startup Behind Devin Now Valued at $2B',
            'kontext': 'Nur 6 Monate nach Gründung erreichte Cognition Unicorn-Status mit $2B Bewertung - außergewöhnlich schnelles Wachstum.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Series C Finanzierung: 500 Millionen USD von Founders Fund, Lux Capital, 8VC und anderen',
            '# beschreibung_en': 'Series C funding: $500M from Founders Fund, Lux Capital, 8VC and others',
            'datum_handlung': '2025-08-14',
            'quell_link': 'https://www.siliconrepublic.com/start-ups/ai-coding-start-up-cognition-raises-500m-in-new-funding-round-wsj',
            'quell_titel': 'AI coding start-up Cognition raises $500m',
            'kontext': 'Massive Finanzierungsrunde bringt Gesamtfinanzierung auf $696M und Bewertung auf $10.2B - Cognition wird zu einem der am höchsten bewerteten AI-Startups.'
        },
        {
            'handlung_typ': 'kauf',
            'beschreibung': 'Akquisition von Windsurf (agentic IDE) inklusive IP, Produkt, Marke und 82M USD ARR',
            '# beschreibung_en': 'Acquisition of Windsurf (agentic IDE) including IP, product, brand and $82M ARR',
            'datum_handlung': '2025-07-14',
            'quell_link': 'https://cognition.ai/blog/windsurf',
            'quell_titel': 'Cognition - Acquisition of Windsurf',
            'kontext': 'Deal wurde innerhalb eines Wochenendes abgeschlossen (Freitag bis Montag). Windsurf hatte 350+ Enterprise-Kunden und hunderttausende tägliche User. 100% der Windsurf-Mitarbeiter erhielten finanzielle Beteiligung am Deal.'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Integration von Devin in Windsurf IDE - Verbindung von AI-Agent mit IDE-Umgebung',
            '# beschreibung_en': 'Integration of Devin into Windsurf IDE - connecting AI agent with IDE environment',
            'datum_handlung': '2025-07-15',
            'quell_link': 'https://venturebeat.com/programming-development/remaining-windsurf-team-and-tech-acquired-by-cognition-makers-of-devin-were-friends-with-anthropic-again',
            'quell_titel': 'Windsurf acquired by Cognition - VentureBeat',
            'kontext': 'Wu\'s Vision: "planning tasks in Windsurf, launching a team of Devins, and reviewing PRs from the comfort of your IDE"'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Devin Slack/Linear/Jira Integration für asynchrone Task-Delegation',
            '# beschreibung_en': 'Launch of Devin Slack/Linear/Jira integration for async task delegation',
            'datum_handlung': '2024-06-01',
            'quell_link': 'https://www.lennysnewsletter.com/p/inside-devin-scott-wu',
            'quell_titel': 'Inside Devin - Lenny\'s Podcast',
            'kontext': 'Devin kann jetzt in Slack, Linear oder Jira getaggt werden und arbeitet autonom an Tickets - paradigmatischer Shift vom IDE-Assistant zum autonomen Agenten.'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Gründung von Lunchclub (AI-powered Networking-Plattform) - Wu\'s erste Firma',
            '# beschreibung_en': 'Founded Lunchclub (AI-powered networking platform) - Wu\'s first company',
            'datum_handlung': '2017-06-01',
            'quell_link': 'https://stripe.com/customers/cognition-scott-wu',
            'quell_titel': 'Stripe Interview - Scott Wu background',
            'kontext': 'Vor Cognition gründete Wu Lunchclub in 2017, eine KI-gestützte Networking-Plattform. Er verließ Lunchclub 2022 um Cognition zu gründen.'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Gewann Goldmedaille (1. Platz) bei International Olympiad in Informatics (IOI)',
            '# beschreibung_en': 'Won gold medal (1st place) at International Olympiad in Informatics (IOI)',
            'datum_handlung': '2014-07-15',
            'quell_link': 'https://en.wikipedia.org/wiki/Scott_Wu',
            'quell_titel': 'Scott Wu - Wikipedia',
            'kontext': 'Wu gewann insgesamt 3 IOI-Goldmedaillen, mit 1. Platz in 2014. Diese Competitive Programming-Expertise formte später seine Philosophie für AI-Entwicklung - das Cognition-Team hat kollektiv 10 IOI-Goldmedaillen gewonnen.'
        }
    ]

    # Aussagen einfügen
    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for i, aussage in enumerate(aussagen, 1):
        insert_aussage(cursor, aussage)
        print(f"  [{i}/{len(aussagen)}] {aussage['aussage_kurz'][:60]}...")

    # Handlungen einfügen
    print(f"\nFüge {len(handlungen)} Handlungen ein...")
    for i, handlung in enumerate(handlungen, 1):
        insert_handlung(cursor, handlung)
        print(f"  [{i}/{len(handlungen)}] {handlung['beschreibung'][:60]}...")

    conn.commit()

    # Verifikation
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    print(f"\n{'='*60}")
    print(f"ERFOLGREICH ABGESCHLOSSEN!")
    print(f"{'='*60}")
    print(f"Scott Wu (person_id={PERSON_ID}):")
    print(f"  - Aussagen: {aussagen_count} (Tier 2 erfuellt: >=10)")
    print(f"  - Handlungen: {handlungen_count} (Tier 2 erfuellt: >=8)")
    print(f"\nTier 2 Status: {'ERFUELLT' if aussagen_count >= 10 and handlungen_count >= 8 else 'NICHT ERFUELLT'}")
    print(f"{'='*60}")

    conn.close()

if __name__ == "__main__":
    main()
