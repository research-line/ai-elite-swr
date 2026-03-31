#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zur Erfassung von Aussagen und Handlungen von Michael Truell (person_id=34)
in die SQLite-Datenbank aussagen_top100.db

Tier 2 Level: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID für Michael Truell
PERSON_ID = 34

def insert_aussagen(cursor):
    """Fügt Aussagen von Michael Truell in die Datenbank ein"""

    aussagen = [
        {
            'aussage_text': 'If you close your eyes and you don\'t look at the code and you have AIs build things with shaky foundations as you add another floor, and another floor, and another floor, and another floor, things start to kind of crumble.',
            'aussage_kurz': 'Warnung vor "Vibe Coding" - blindes Vertrauen in KI führt zu instabilen Software-Fundamenten',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://fortune.com/2025/12/25/cursor-ceo-michael-truell-vibe-coding-warning-generative-ai-assistant/',
            'quell_titel': 'Cursor CEO warns vibe coding builds shaky foundations',
            'datum_aussage': '2025-12-25',
            'sprache': 'en',
            'kontext': 'Warnung vor den Gefahren des "Vibe Coding" - wenn Entwickler blindlings KI-generierten Code verwenden ohne ihn zu verstehen',
            'aussage_uebersetzung_de': 'Wenn Sie die Augen schließen und nicht auf den Code schauen und KI Dinge mit wackeligen Fundamenten bauen lässt, während Sie ein Stockwerk nach dem anderen hinzufügen, beginnen die Dinge zusammenzubrechen.'
        },
        {
            'aussage_text': 'We didn\'t want to just add AI to existing tools. We wanted to reimagine the entire development environment with AI at its core.',
            'aussage_kurz': 'Vision von Cursor: Komplette Neugestaltung der Entwicklungsumgebung mit KI im Zentrum',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.frederick.ai/blog/michael-truell-cursor-ai',
            'quell_titel': 'Founder Story: Michael Truell of Cursor AI',
            'datum_aussage': '2024-08-01',
            'sprache': 'en',
            'kontext': 'Erklärung der Gründungsphilosophie von Cursor - nicht nur KI hinzufügen, sondern fundamental neu denken',
            'aussage_uebersetzung_de': 'Wir wollten nicht nur KI zu bestehenden Tools hinzufügen. Wir wollten die gesamte Entwicklungsumgebung mit KI im Kern neu gestalten.'
        },
        {
            'aussage_text': 'The goal with the company is to replace coding with something that\'s much better.',
            'aussage_kurz': 'Ziel: Programmieren durch etwas viel Besseres ersetzen',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell',
            'quell_titel': 'The rise of Cursor: The $300M ARR AI tool - Lenny\'s Podcast',
            'datum_aussage': '2024-10-01',
            'sprache': 'en',
            'kontext': 'Interview über die langfristige Vision von Cursor - nicht nur Coding verbessern, sondern transformieren',
            'aussage_uebersetzung_de': 'Das Ziel mit dem Unternehmen ist es, Programmieren durch etwas zu ersetzen, das viel besser ist.'
        },
        {
            'aussage_text': 'I think that this is going to be a decade where just your ability to build will be so magnified... But then I think it\'ll also become accessible for tons more people.',
            'aussage_kurz': 'KI wird Entwicklungsfähigkeiten verstärken und Programmieren für viel mehr Menschen zugänglich machen',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell',
            'quell_titel': 'The rise of Cursor: The $300M ARR AI tool - Lenny\'s Podcast',
            'datum_aussage': '2024-10-01',
            'sprache': 'en',
            'kontext': 'Prognose über die Zukunft der Softwareentwicklung im KI-Zeitalter',
            'aussage_uebersetzung_de': 'Ich denke, dies wird ein Jahrzehnt sein, in dem Ihre Fähigkeit zu bauen so verstärkt wird... Aber ich denke auch, es wird für viel mehr Menschen zugänglich werden.'
        },
        {
            'aussage_text': 'We were really, really intentional about wanting to own the surface.',
            'aussage_kurz': 'Bewusste strategische Entscheidung, die Benutzeroberfläche zu kontrollieren',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://stratechery.com/2025/an-interview-with-cursor-co-founder-and-ceo-michael-truell-about-coding-with-ai/',
            'quell_titel': 'An Interview with Cursor Co-Founder and CEO Michael Truell - Stratechery',
            'datum_aussage': '2025-01-15',
            'sprache': 'en',
            'kontext': 'Erklärung der strategischen Entscheidung, einen VS Code Fork zu erstellen statt nur ein Plugin',
            'aussage_uebersetzung_de': 'Wir waren wirklich sehr bewusst darüber, dass wir die Oberfläche besitzen wollten.'
        },
        {
            'aussage_text': 'It\'s really easy at an executive level to underestimate just how far away we are from the limit of automating software. I think that there\'s a really, really long way to go.',
            'aussage_kurz': 'Warnung: Es gibt noch einen sehr langen Weg bis zur vollständigen Software-Automatisierung',
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 4,  # Konferenzen
            'quell_link': 'https://x.com/a16z/status/1988022546277822651',
            'quell_titel': 'a16z Runtime 2025 - Michael Truell Interview',
            'datum_aussage': '2025-05-08',
            'sprache': 'en',
            'kontext': 'Realistische Einschätzung der aktuellen Grenzen von KI in der Softwareentwicklung',
            'aussage_uebersetzung_de': 'Es ist auf Führungsebene sehr einfach zu unterschätzen, wie weit wir vom Limit der Software-Automatisierung entfernt sind. Ich denke, es gibt noch einen sehr, sehr langen Weg.'
        },
        {
            'aussage_text': 'We built a browser with GPT-5.2 in Cursor. It ran uninterrupted for one week. It\'s 3M+ lines of code across thousands of files. The rendering engine is from-scratch in Rust with HTML parsing, CSS cascade, layout, text shaping, paint, and a custom JS VM. It *kind of* works!',
            'aussage_kurz': 'KI-Agenten bauten in einer Woche einen Browser mit 3M+ Zeilen Code - funktioniert teilweise',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/mntruell/status/2011562190286045552',
            'quell_titel': 'Michael Truell Twitter Post - Browser Project',
            'datum_aussage': '2026-01-14',
            'sprache': 'en',
            'kontext': 'Demonstration der Fähigkeiten von GPT-5.2 und Cursor durch Bau eines funktionsfähigen Browsers',
            'aussage_uebersetzung_de': 'Wir haben einen Browser mit GPT-5.2 in Cursor gebaut. Er lief eine Woche lang ununterbrochen. Es sind über 3 Millionen Zeilen Code über Tausende von Dateien. Die Rendering-Engine ist von Grund auf in Rust mit HTML-Parsing, CSS-Kaskade, Layout, Text-Shaping, Paint und einer benutzerdefinierten JS-VM. Es funktioniert *irgendwie*!'
        },
        {
            'aussage_text': 'What if AI wasn\'t just an assistant, but the foundation of the coding experience?',
            'aussage_kurz': 'Kernfrage: Was wenn KI nicht nur Assistent, sondern das Fundament der Coding-Erfahrung wäre?',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.frederick.ai/blog/michael-truell-cursor-ai',
            'quell_titel': 'Founder Story: Michael Truell of Cursor AI',
            'datum_aussage': '2024-08-01',
            'sprache': 'en',
            'kontext': 'Die zentrale Einsicht die zur Gründung von Cursor führte, nach Launch von GitHub Copilot',
            'aussage_uebersetzung_de': 'Was wäre, wenn KI nicht nur ein Assistent wäre, sondern das Fundament der Coding-Erfahrung?'
        },
        {
            'aussage_text': 'We believed that only a few things really matter, and we stuck to them. We ignored hype, spoke less, built more, and kept a clear focus on building something truly useful for developers.',
            'aussage_kurz': 'Fokus auf das Wesentliche: Hype ignorieren, weniger reden, mehr bauen',
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.educationnext.in/posts/michael-truell-on-the-future-of-ai-and-software-development-with-cursor',
            'quell_titel': 'Michael Truell on the Future of AI and Software Development',
            'datum_aussage': '2024-09-15',
            'sprache': 'en',
            'kontext': 'Erklärung der Unternehmensphilosophie und Erfolgsfaktoren von Cursor',
            'aussage_uebersetzung_de': 'Wir glaubten, dass nur ein paar Dinge wirklich wichtig sind, und wir hielten daran fest. Wir ignorierten den Hype, sprachen weniger, bauten mehr und behielten einen klaren Fokus darauf, etwas wirklich Nützliches für Entwickler zu bauen.'
        },
        {
            'aussage_text': 'I think it\'s going to be more consequential than the internet... it\'s going to take a while, and I think it\'s going to be a multi-decade thing.',
            'aussage_kurz': 'KI wird folgenreicher als das Internet - ein Prozess über mehrere Jahrzehnte',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.educationnext.in/posts/michael-truell-on-the-future-of-ai-and-software-development-with-cursor',
            'quell_titel': 'Michael Truell on the Future of AI and Software Development',
            'datum_aussage': '2024-09-15',
            'sprache': 'en',
            'kontext': 'Langfristige Prognose über den Impact von KI auf die Gesellschaft',
            'aussage_uebersetzung_de': 'Ich denke, es wird folgenreicher sein als das Internet... es wird eine Weile dauern, und ich denke, es wird eine Sache von mehreren Jahrzehnten sein.'
        },
        {
            'aussage_text': 'The hiring team leaned toward people who fit the archetype of "well-known school, very young, had done the things that were high credential." But the hires who stood out — and stuck around — didn\'t always fit that mold.',
            'aussage_kurz': 'Gelernte Lektion: Beste Mitarbeiter kamen nicht immer von Elite-Unis',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.aol.com/ceo-behind-ai-tool-cursor-090120602.html',
            'quell_titel': 'CEO behind AI tool Cursor says he used to hire too slowly',
            'datum_aussage': '2025-05-06',
            'sprache': 'en',
            'kontext': 'Reflexion über Fehler bei der frühen Mitarbeiterrekrutierung bei Cursor',
            'aussage_uebersetzung_de': 'Das Einstellungsteam tendierte zu Leuten, die dem Archetyp "bekannte Schule, sehr jung, hohe Credentials" entsprachen. Aber die Einstellungen, die herausstachen — und blieben — passten nicht immer in diese Form.'
        },
        {
            'aussage_text': 'Cursor seeks to be the best and most powerful way to code with AI. What are the ways in which we could be better?',
            'aussage_kurz': 'Vision: Cursor soll der beste und mächtigste Weg sein, mit KI zu programmieren',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/mntruell/status/2008986746713735195',
            'quell_titel': 'Michael Truell Twitter - Cursor Vision',
            'datum_aussage': '2026-01-02',
            'sprache': 'en',
            'kontext': 'Öffentliche Frage an die Community, um Feedback für Verbesserungen zu sammeln',
            'aussage_uebersetzung_de': 'Cursor strebt danach, der beste und mächtigste Weg zu sein, mit KI zu programmieren. Auf welche Weise könnten wir besser werden?'
        },
        {
            'aussage_text': 'We believe that coding will be the single biggest driver of global productivity over the next decade.',
            'aussage_kurz': 'Überzeugung: Programmieren wird größter Treiber globaler Produktivität im nächsten Jahrzehnt',
            'modus': 'schriftlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.businesswire.com/news/home/20251113939996/en/Cursor-Secures-$2.3-Billion-Series-D-Financing-at-$29.3-Billion-Valuation-to-Redefine-How-Software-is-Written',
            'quell_titel': 'Cursor Secures $2.3 Billion Series D Financing',
            'datum_aussage': '2025-11-13',
            'sprache': 'en',
            'kontext': 'Offizielle Stellungnahme zur Series D Finanzierungsrunde',
            'aussage_uebersetzung_de': 'Wir glauben, dass Programmieren der größte Treiber globaler Produktivität im nächsten Jahrzehnt sein wird.'
        }
    ]

    for aussage in aussagen:
        cursor.execute('''
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
                plattform_id, quell_link, quell_titel, datum_aussage,
                sprache, kontext, aussage_uebersetzung_de
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
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

    print(f"OK - {len(aussagen)} Aussagen eingefuegt")
    return len(aussagen)


def insert_handlungen(cursor):
    """Fügt Handlungen von Michael Truell in die Datenbank ein"""

    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Gründung von Anysphere (Cursor) zusammen mit MIT-Kommilitonen Sualeh Asif, Arvid Lunnemark und Aman Sanger',
            'datum_handlung': '2022-01-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Anysphere',
            'quell_titel': 'Anysphere - Wikipedia',
            'kontext': 'Vier MIT-Studenten gründeten Anysphere, um einen KI-nativen Code-Editor zu entwickeln. Sie verließen MIT um sich vollzeit dem Startup zu widmen.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Erhalt von $11 Millionen Seed-Finanzierung, davon $8 Millionen vom OpenAI Startup Fund',
            'datum_handlung': '2023-10-01',
            'quell_link': 'https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/',
            'quell_titel': 'Anysphere raises $8M from OpenAI - TechCrunch',
            'kontext': 'Seed-Runde geleitet vom OpenAI Startup Fund, mit Beteiligung von Nat Friedman (ex-GitHub CEO) und Arash Ferdowsi (Dropbox Co-Founder)'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Cursor 1.0 - KI-nativer Code-Editor basierend auf VS Code Fork',
            'datum_handlung': '2023-03-01',
            'quell_link': 'https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell',
            'quell_titel': 'The rise of Cursor - Lenny\'s Podcast',
            'kontext': 'Cursor ging von erstem Commit zu Launch in 90 Tagen, mit wöchentlichen Updates. Erreichte $100M ARR innerhalb eines Jahres.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Series A Finanzierung: $60 Millionen bei $400 Millionen Bewertung, geleitet von Andreessen Horowitz und Thrive Capital',
            'datum_handlung': '2024-08-09',
            'quell_link': 'https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/',
            'quell_titel': 'Anysphere raises $60M Series A - TechCrunch',
            'kontext': 'Beeindruckendes Investorenteam: a16z, Thrive, OpenAI, Jeff Dean (Google), Stripe-Gründer Collison-Brüder, GitHub-Gründer, Perplexity- und Ramp-Gründer'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Composer - proprietäres KI-Modell speziell für agentisches Coding optimiert',
            'datum_handlung': '2025-10-29',
            'quell_link': 'https://www.cometapi.com/cursor-2-0-what-changed-and-why-it-matters/',
            'quell_titel': 'Cursor 2.0 and Composer - CometAPI',
            'kontext': 'Cursor 2.0 mit Composer-Modell: 4x schnellere Generierung als vergleichbare Modelle, optimiert für kurze iterative Coding-Sessions im Editor'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Series D Finanzierung: $2.3 Milliarden bei $29.3 Milliarden Bewertung, co-geleitet von Accel und Coatue Management',
            'datum_handlung': '2025-11-13',
            'quell_link': 'https://www.businesswire.com/news/home/20251113939996/en/Cursor-Secures-$2.3-Billion-Series-D-Financing-at-$29.3-Billion-Valuation-to-Redefine-How-Software-is-Written',
            'quell_titel': 'Cursor Secures $2.3 Billion Series D - Business Wire',
            'kontext': 'Massive Finanzierungsrunde mit Beteiligung von Thrive, a16z, Accel, DST, Coatue, NVIDIA und Google. Über $1 Milliarde ARR erreicht.'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Partnerschaft mit Stripe - Teilnahme an Stripe Sessions 2025 Developer Keynote',
            'datum_handlung': '2025-04-15',
            'quell_link': 'https://stripe.com/sessions/2025/developer-keynote',
            'quell_titel': 'Developer keynote - Stripe Sessions 2025',
            'kontext': 'Truell diskutierte die Rolle von KI in der Zukunft der Entwicklung und die Herausforderungen beim Bau von KI-Tools für Entwickler'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Gründung von Halite (Coding-Wettbewerb) als Teenager zusammen mit Benjamin Spector',
            'datum_handlung': '2016-09-01',
            'quell_link': 'https://awards.acm.org/award_winners/truell_7807021',
            'quell_titel': 'Michael Truell - ACM Award Winners',
            'kontext': 'Halite wurde einer der größten zeitlich begrenzten Programmierwettbewerbe mit über 5.500 Nutzern. Open-Source-Plattform für Bot-Programmierung.'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Gewinn des ACM/CSTA Cutler-Bell Prize in High School Computing im Alter von 17 Jahren',
            'datum_handlung': '2018-03-01',
            'quell_link': 'https://www.acm.org/media-center/2018/march/cutler-bell-prize-2017',
            'quell_titel': 'ACM/CSTA Cutler-Bell Prize Winners 2017-2018',
            'kontext': 'Eine der höchsten Auszeichnungen für junge Programmierer, erhalten für die Entwicklung von Halite'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Rede bei Y Combinator AI Startup School über den Aufbau von Cursor',
            'datum_handlung': '2025-06-17',
            'quell_link': 'https://www.ycombinator.com/library/Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students',
            'quell_titel': 'Michael Truell: Building Cursor at 23 - YC',
            'kontext': 'Fireside Chat mit YC General Partner Diana Hu über Lektionen aus gescheiterten Projekten, warum Programmieren trotz KI essentiell bleibt, und wie Cursor GitHub Copilot herausfordert'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Demonstration: Bau eines funktionsfähigen Browsers mit GPT-5.2 in Cursor (FastRender, 3M+ Zeilen Code)',
            'datum_handlung': '2026-01-14',
            'quell_link': 'https://x.com/mntruell/status/2011562190286045552',
            'quell_titel': 'Michael Truell Twitter - Browser Demo',
            'kontext': 'Hunderte von GPT-5.2 Agenten bauten autonom einen Browser von Grund auf in Rust. Lief eine Woche ununterbrochen. Demonstriert Fähigkeiten von agentischem Coding.'
        }
    ]

    for handlung in handlungen:
        cursor.execute('''
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung, datum_handlung,
                quell_link, quell_titel, kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            PERSON_ID,
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))

    print(f"OK - {len(handlungen)} Handlungen eingefuegt")
    return len(handlungen)


def main():
    """Hauptfunktion"""
    print("=" * 80)
    print("MICHAEL TRUELL (person_id=34) - Datenerfassung")
    print("=" * 80)
    print()

    try:
        # Verbindung zur Datenbank
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Aussagen einfügen
        print("Füge Aussagen ein...")
        anzahl_aussagen = insert_aussagen(cursor)

        # Handlungen einfügen
        print("\nFüge Handlungen ein...")
        anzahl_handlungen = insert_handlungen(cursor)

        # Änderungen speichern
        conn.commit()

        print("\n" + "=" * 80)
        print("ZUSAMMENFASSUNG")
        print("=" * 80)
        print(f"Person: Michael Truell (ID: {PERSON_ID})")
        print(f"Aussagen eingefügt: {anzahl_aussagen}")
        print(f"Handlungen eingefügt: {anzahl_handlungen}")

        # Tier-Level prüfen
        tier_level = "TIER 2" if anzahl_aussagen >= 10 and anzahl_handlungen >= 8 else "TIER 1"
        print(f"\nTier-Level erreicht: {tier_level}")

        if tier_level == "TIER 2":
            print("OK - Mindestanforderungen erfuellt (10+ Aussagen, 8+ Handlungen)")

        print("\n" + "=" * 80)
        print("QUELLEN-ÜBERSICHT")
        print("=" * 80)
        print("- Fortune Magazine - Vibe Coding Warnung")
        print("- Lenny's Podcast - Cursor Rise to $300M ARR")
        print("- Stratechery - Interview ueber KI-Coding")
        print("- TechCrunch - Funding Announcements")
        print("- Business Wire - Series D Announcement")
        print("- Y Combinator - AI Startup School")
        print("- Twitter/X - @mntruell Posts")
        print("- ACM - Cutler-Bell Prize")
        print("- Stripe Sessions 2025")
        print("- Wikipedia - Anysphere")
        print()

    except sqlite3.Error as e:
        print(f"\nDatenbankfehler: {e}")
        return 1

    except Exception as e:
        print(f"\nFehler: {e}")
        return 1

    finally:
        if conn:
            conn.close()

    print("Erfolgreich abgeschlossen!")
    return 0


if __name__ == "__main__":
    exit(main())
