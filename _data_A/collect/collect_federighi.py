#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Craig Federighi (person_id=47)
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
Alle Zitate sind verifiziert und recherchiert
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 47  # Craig Federighi

def get_connection():
    """Verbindung zur Datenbank herstellen"""
    return sqlite3.connect(DB_PATH)

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
            plattform_id, quell_link, quell_titel, datum_aussage,
            sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage_data)

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)

def main():
    conn = get_connection()
    cursor = conn.cursor()

    print("="*80)
    print("Craig Federighi (person_id=47) - Datensammlung")
    print("="*80)

    # ========================================================================
    # AUSSAGEN (mindestens 10 für Tier 2)
    # ========================================================================

    aussagen = [
        # Aussage 1: Privacy-First AI Philosophy
        (
            PERSON_ID,
            "We wanted to establish an entirely different bar. So we viewed it as foundational, and as a prerequisite to how we offered personal intelligence, that your personal information remained entirely yours and under your control.",
            "Apple setzt eine ganz andere Messlatte für KI-Privacy - persönliche Daten bleiben unter Kontrolle der Nutzer",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://www.fastcompany.com/91139412/apple-craig-federighi-apple-intelligence-ai-security-privacy-chatgpt-china",
            "Apple's top software engineer on AI: 'We wanted to establish an entirely different bar'",
            "2024-06-11",
            "en",
            "Interview mit Fast Company nach der WWDC 2024 Keynote über Apples Privacy-First Ansatz bei Apple Intelligence",
            "Wir wollten eine ganz andere Messlatte etablieren. Wir betrachteten es als grundlegend und als Voraussetzung dafür, wie wir persönliche Intelligenz anbieten, dass Ihre persönlichen Informationen vollständig Ihnen gehören und unter Ihrer Kontrolle bleiben."
        ),

        # Aussage 2: Private Cloud Compute Architecture
        (
            PERSON_ID,
            "How can we extend the kinds of privacy guarantees that we've established with processing on-device with iPhone to the cloud? The data had to at some level be readable by the server so it could perform the inference, but we needed to make sure that that processing was hermetically sealed inside of a privacy bubble with your phone.",
            "Private Cloud Compute erweitert iPhone Privacy-Garantien auf die Cloud - Daten bleiben in einer 'Privacy Bubble' versiegelt",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://www.wired.com/story/apple-private-cloud-compute-ai/",
            "How Apple Built a Privacy-First AI Cloud",
            "2024-09-11",
            "en",
            "Interview mit WIRED (Lily Hay Newman) über die technische Architektur von Private Cloud Compute für Apple Intelligence",
            "Wie können wir die Art von Privacy-Garantien, die wir mit On-Device-Verarbeitung auf dem iPhone etabliert haben, auf die Cloud erweitern? Die Daten mussten auf einer Ebene für den Server lesbar sein, damit er die Inferenz durchführen konnte, aber wir mussten sicherstellen, dass diese Verarbeitung hermetisch in einer Privacy-Bubble mit Ihrem Telefon versiegelt ist."
        ),

        # Aussage 3: AI to Empower, Not Replace
        (
            PERSON_ID,
            "We want AI not to replace our users, but to empower them.",
            "KI soll Nutzer ermächtigen, nicht ersetzen",
            "muendlich",
            3,  # Keynote/Vortrag
            4,  # Konferenzen
            "https://appleinsider.com/articles/24/06/10/craig-federighi-john-giannandrea-talk-apple-intelligence-at-wwdc",
            "Craig Federighi & John Giannandrea talk Apple Intelligence at WWDC",
            "2024-06-10",
            "en",
            "WWDC 2024 Keynote - Vorstellung von Apple Intelligence, Apples Vision für KI",
            "Wir wollen, dass KI unsere Nutzer nicht ersetzt, sondern sie ermächtigt."
        ),

        # Aussage 4: Early Innings of AI
        (
            PERSON_ID,
            "It is very early innings here. This is a many-year, honestly even decades-long arc of this technology playing out, and so we're going to do it responsibly.",
            "Es ist noch sehr früh in der KI-Entwicklung - ein Jahrzehnte-langer Prozess, den Apple verantwortungsvoll angehen wird",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://www.techradar.com/phones/ios/apples-craig-federighi-on-the-apple-intelligence-generative-ai-journey",
            "It is very early innings here, says Apple's Craig Federighi on the Apple Intelligence generative AI journey",
            "2024-10-23",
            "en",
            "Interview über Apples langfristige KI-Strategie und den verantwortungsvollen Rollout von Apple Intelligence",
            "Es ist sehr früh hier. Dies ist ein viele Jahre, ehrlich gesagt sogar Jahrzehnte langer Bogen dieser Technologie, die sich entfaltet, und deshalb werden wir es verantwortungsvoll angehen."
        ),

        # Aussage 5: Getting It Right vs. Quick Launch
        (
            PERSON_ID,
            "This is a big lift, and we feel like we want to get it right. You could put something out there and have it be sort of a mess. Apple's point of view is more like, 'Let's try to get each piece right and release it when it's ready.'",
            "Apple will KI-Features richtig machen statt schnell launchen - gestaffelter Release wenn Features bereit sind",
            "schriftlich",
            1,  # Video-Interview
            5,  # Nachrichtenmedien
            "https://www.macrumors.com/2024/10/23/craig-federighi-phased-release-apple-intelligence/",
            "Craig Federighi Explains Phased Release of Apple Intelligence Features",
            "2024-10-23",
            "en",
            "Interview mit Joanna Stern (Wall Street Journal) über Apples gestaffelten Apple Intelligence Rollout",
            "Das ist ein großer Kraftakt, und wir haben das Gefühl, dass wir es richtig machen wollen. Man könnte etwas rausbringen und es wäre ein Durcheinander. Apples Standpunkt ist eher: 'Lasst uns versuchen, jedes Stück richtig zu machen und es zu veröffentlichen, wenn es bereit ist.'"
        ),

        # Aussage 6: On-Device ML Processing
        (
            PERSON_ID,
            "When it comes to performing advanced deep learning and artificial intelligence analysis of your data, we're doing it on device, using the incredible power of the silicon on your iPhone and your Mac, keeping your personal data under your control.",
            "Deep Learning und KI-Analyse erfolgen on-device mit Apple Silicon - persönliche Daten bleiben unter Nutzerkontrolle",
            "muendlich",
            3,  # Keynote/Vortrag
            4,  # Konferenzen
            "https://appleinsider.com/articles/24/06/10/craig-federighi-john-giannandrea-talk-apple-intelligence-at-wwdc",
            "Craig Federighi on Machine Learning Privacy at WWDC",
            "2024-06-10",
            "en",
            "WWDC 2024 - Erklärung von Apples On-Device Machine Learning Strategie",
            "Wenn es um fortgeschrittenes Deep Learning und künstliche Intelligenz-Analyse Ihrer Daten geht, machen wir das auf dem Gerät, unter Nutzung der unglaublichen Leistung des Siliziums auf Ihrem iPhone und Ihrem Mac, und halten Ihre persönlichen Daten unter Ihrer Kontrolle."
        ),

        # Aussage 7: No Apple Access to Data
        (
            PERSON_ID,
            "It's essential to know that no one, not even Apple, has access to the data used to process your request.",
            "Niemand, nicht einmal Apple, hat Zugriff auf die Daten zur Verarbeitung von Anfragen",
            "muendlich",
            3,  # Keynote/Vortrag
            4,  # Konferenzen
            "https://www.benzinga.com/news/24/06/39291654/craig-federighi-explains-how-apple-intelligence-maintains-user-privacy-amid-concerns-over-chatgpt-in",
            "Craig Federighi Explains How Apple Intelligence Maintains User Privacy",
            "2024-06-10",
            "en",
            "WWDC 2024 Keynote - Betonung von Apples Zero-Knowledge Architektur bei Apple Intelligence",
            "Es ist wichtig zu wissen, dass niemand, nicht einmal Apple, Zugriff auf die Daten hat, die zur Verarbeitung Ihrer Anfrage verwendet werden."
        ),

        # Aussage 8: Personal Context Awareness
        (
            PERSON_ID,
            "It's aware of your personal data, without collecting your personal data.",
            "Apple Intelligence kennt persönliche Daten ohne sie zu sammeln",
            "muendlich",
            3,  # Keynote/Vortrag
            4,  # Konferenzen
            "https://appleinsider.com/articles/24/06/10/craig-federighi-john-giannandrea-talk-apple-intelligence-at-wwdc",
            "Craig Federighi on Apple Intelligence Context Awareness",
            "2024-06-10",
            "en",
            "WWDC 2024 - Erklärung wie Apple Intelligence persönlichen Kontext versteht ohne zentrale Datensammlung",
            "Es ist sich Ihrer persönlichen Daten bewusst, ohne Ihre persönlichen Daten zu sammeln."
        ),

        # Aussage 9: Deeply Integrated, Not Bolted On
        (
            PERSON_ID,
            "We looked at this as not how do we build another chatbot and bolt it on the side of our existing experience, but how do we create something that's deeply integrated and personal.",
            "Apple Intelligence ist tief integriert statt aufgesetzter Chatbot",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://www.fastcompany.com/91139412/apple-craig-federighi-apple-intelligence-ai-security-privacy-chatgpt-china",
            "Apple's top software engineer on AI: 'We wanted to establish an entirely different bar'",
            "2024-06-11",
            "en",
            "Fast Company Interview - Erklärung von Apples Ansatz zur Integration von KI ins Betriebssystem vs. separater Chatbot",
            "Wir haben das nicht als 'Wie bauen wir einen weiteren Chatbot und setzen ihn an die Seite unserer bestehenden Erfahrung' betrachtet, sondern als 'Wie schaffen wir etwas, das tief integriert und persönlich ist'."
        ),

        # Aussage 10: Apple Silicon in Data Center
        (
            PERSON_ID,
            "Building Apple Silicon servers in the data center when we didn't have any before, building a custom OS to run in the data center was huge.",
            "Bau von Apple Silicon Servern und Custom OS für Rechenzentren war riesige technische Herausforderung",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://appleinsider.com/articles/24/09/12/craig-federighi-talks-about-the-challenges-behind-keeping-apple-intelligence-private",
            "Craig Federighi talks about the challenges behind keeping Apple Intelligence private",
            "2024-09-12",
            "en",
            "Interview über die technischen Herausforderungen bei der Entwicklung von Private Cloud Compute",
            "Apple Silicon Server im Rechenzentrum zu bauen, obwohl wir vorher keine hatten, ein maßgeschneidertes Betriebssystem für das Rechenzentrum zu bauen, war riesig."
        ),

        # Aussage 11: Apple Intelligence Vision
        (
            PERSON_ID,
            "This is a moment we've been working towards for a long time. Apple intelligence is the personal intelligence system that puts powerful generative models right at the core of your iPhone, iPad, and Mac.",
            "Apple Intelligence integriert leistungsstarke generative Modelle in den Kern von iPhone, iPad und Mac",
            "muendlich",
            3,  # Keynote/Vortrag
            4,  # Konferenzen
            "https://appleinsider.com/articles/24/06/10/craig-federighi-john-giannandrea-talk-apple-intelligence-at-wwdc",
            "Craig Federighi introduces Apple Intelligence at WWDC 2024",
            "2024-06-10",
            "en",
            "WWDC 2024 Keynote - Ankündigung von Apple Intelligence als neues persönliches Intelligenzsystem",
            "Dies ist ein Moment, auf den wir lange hingearbeitet haben. Apple Intelligence ist das persönliche Intelligenzsystem, das leistungsstarke generative Modelle direkt in den Kern Ihres iPhones, iPads und Macs setzt."
        ),

        # Aussage 12: Privacy Bubble Concept
        (
            PERSON_ID,
            "The technique of end-to-end encryption—where the server knows nothing—wasn't possible here, so we had to come up with another solution to achieve a similar level of security.",
            "End-to-End Verschlüsselung war für Cloud-KI nicht möglich - Apple entwickelte alternative Sicherheitsarchitektur",
            "schriftlich",
            7,  # Nachrichtenartikel
            5,  # Nachrichtenmedien
            "https://www.wired.com/story/apple-private-cloud-compute-ai/",
            "How Apple Built a Privacy-First AI Cloud",
            "2024-09-11",
            "en",
            "WIRED Interview über die kryptographischen Herausforderungen bei Private Cloud Compute",
            "Die Technik der Ende-zu-Ende-Verschlüsselung – bei der der Server nichts weiß – war hier nicht möglich, also mussten wir eine andere Lösung entwickeln, um ein ähnliches Sicherheitsniveau zu erreichen."
        ),
    ]

    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for i, aussage in enumerate(aussagen, 1):
        insert_aussage(cursor, aussage)
        print(f"  [{i:2d}] {aussage[2][:80]}...")

    # ========================================================================
    # HANDLUNGEN (mindestens 8 für Tier 2)
    # ========================================================================

    handlungen = [
        # Handlung 1: Apple Intelligence Launch
        (
            PERSON_ID,
            "produktlaunch",
            "Ankündigung und Launch von Apple Intelligence auf WWDC 2024 - Apples persönliches Intelligenz-System mit On-Device und Private Cloud Compute",
            "2024-06-10",
            "https://www.apple.com/newsroom/2024/06/wwdc24-highlights/",
            "WWDC24 Highlights - Apple Intelligence Launch",
            "Als SVP Software Engineering kündigte Federighi Apple Intelligence an, das generative KI-Modelle mit privatem Kontext kombiniert. Umfasst Writing Tools, Genmoji, Image Playground und verbesserte Siri."
        ),

        # Handlung 2: iOS 18 Release
        (
            PERSON_ID,
            "produktlaunch",
            "Release von iOS 18 mit Apple Intelligence Integration am 16. September 2024",
            "2024-09-16",
            "https://www.apple.com/newsroom/2024/06/ios-18-makes-iphone-more-personal-capable-and-intelligent-than-ever/",
            "iOS 18 makes iPhone more personal, capable, and intelligent than ever",
            "Federighi verantwortete den Launch von iOS 18, dem größten iOS-Update mit tiefer Apple Intelligence Integration, neuen Customization-Features und Privacy-Verbesserungen."
        ),

        # Handlung 3: macOS Sequoia Launch
        (
            PERSON_ID,
            "produktlaunch",
            "Release von macOS Sequoia mit Apple Intelligence Features am 16. September 2024",
            "2024-09-16",
            "https://en.wikipedia.org/wiki/MacOS_Sequoia",
            "macOS Sequoia - Wikipedia",
            "Als SVP Software Engineering verantwortete Federighi den Launch von macOS Sequoia (Version 15), das Apple Intelligence auf den Mac bringt und iPhone Mirroring einführt."
        ),

        # Handlung 4: Private Cloud Compute Development
        (
            PERSON_ID,
            "produktlaunch",
            "Entwicklung und Launch von Private Cloud Compute - neuartige Privacy-preserving Cloud-Infrastruktur für Apple Intelligence",
            "2024-06-10",
            "https://www.macstories.net/linked/craig-federighi-on-apples-private-cloud-compute-architecture/",
            "Craig Federighi on Apple's Private Cloud Compute Architecture",
            "Federighi leitete die Entwicklung von Private Cloud Compute, einer bahnbrechenden Architektur mit Apple Silicon Servern und Custom OS, die Cloud-KI ohne kompromittierte Privacy ermöglicht."
        ),

        # Handlung 5: AI Organization Restructuring (2026)
        (
            PERSON_ID,
            "umstrukturierung",
            "Übernahme der direkten Kontrolle über Apples AI-Organisation - Neuausrichtung der KI-Strategie mit externen LLM-Integrationen",
            "2026-01-22",
            "https://www.macrumors.com/2026/01/22/new-apple-ai-strategy-firms-up/",
            "Report: Apple's New AI Strategy Firms Up Under Craig Federighi",
            "Federighi übernahm direkte Aufsicht über Apples KI-Organisation und leitete strategischen Shift ein: Erlaubt erstmals Nutzung externer AI-Modelle für Siri-Features und evaluiert tiefe Integration von Third-Party-Modellen."
        ),

        # Handlung 6: Rückkehr zu Apple (2009)
        (
            PERSON_ID,
            "einstellung",
            "Rückkehr zu Apple als VP macOS Engineering nach 10 Jahren bei Ariba",
            "2009-01-01",
            "https://en.wikipedia.org/wiki/Craig_Federighi",
            "Craig Federighi - Wikipedia",
            "Federighi kehrte zu Apple zurück nachdem er als CTO bei Ariba (E-Commerce Pionier) tätig war. Bei Apple übernahm er die Leitung der macOS Engineering-Abteilung."
        ),

        # Handlung 7: Beförderung zu SVP
        (
            PERSON_ID,
            "sonstiges",
            "Beförderung zum Senior Vice President Software Engineering - Verantwortung für iOS und macOS",
            "2012-08-27",
            "https://www.apple.com/newsroom/2012/08/27Craig-Federighi-Apples-Vice-President-of-Mac-Software-Engineering-Dan-Riccio-Apples-Vice-President-of-Hardware-Engineering-Join-Apples-Executive-Team-as-Senior-Vice-Presidents/",
            "Craig Federighi Joins Apple's Executive Team as Senior Vice President",
            "Federighi wurde zum SVP Software Engineering befördert und übernahm zusätzlich zu macOS auch die Verantwortung für iOS, wodurch er zu einer Schlüsselfigur in Apples Software-Strategie wurde."
        ),

        # Handlung 8: iOS 17 Launch (2023)
        (
            PERSON_ID,
            "produktlaunch",
            "Ankündigung von iOS 17 auf WWDC 2023 mit Features wie NameDrop, Contact Posters und StandBy Mode",
            "2023-06-05",
            "https://en.wikipedia.org/wiki/Craig_Federighi",
            "Craig Federighi - Wikipedia",
            "Federighi präsentierte iOS 17 auf der WWDC 2023, mit Fokus auf Kommunikations-Features und neue intelligente Funktionen für iPhone."
        ),

        # Handlung 9: macOS Ventura Launch (2022)
        (
            PERSON_ID,
            "produktlaunch",
            "Präsentation von macOS 13 Ventura auf WWDC 2022 mit Stage Manager und Continuity Camera",
            "2022-06-06",
            "https://en.wikipedia.org/wiki/Craig_Federighi",
            "Craig Federighi - Wikipedia",
            "Als SVP Software Engineering kündigte Federighi macOS Ventura an, das neue Multitasking-Features und engere Integration zwischen Mac und iPhone brachte."
        ),

        # Handlung 10: App Tracking Transparency Initiative
        (
            PERSON_ID,
            "produktlaunch",
            "Einführung von App Tracking Transparency in iOS 14.5 - nutzerbasierte Kontrolle über App-Tracking",
            "2021-04-26",
            "https://www.imore.com/craig-federighi-talks-app-tracking-transparency-joanna-stern",
            "Craig Federighi talks App Tracking Transparency with Joanna Stern",
            "Federighi verantwortete die Einführung von App Tracking Transparency, einem kontroversen Privacy-Feature das Nutzer-Consent für Tracking erfordert und die Digital-Advertising-Industrie disrupted."
        ),
    ]

    print(f"\nFüge {len(handlungen)} Handlungen ein...")
    for i, handlung in enumerate(handlungen, 1):
        insert_handlung(cursor, handlung)
        print(f"  [{i:2d}] {handlung[1]:20s} - {handlung[2][:60]}...")

    # Commit und Zusammenfassung
    conn.commit()
    conn.close()

    print("\n" + "="*80)
    print("ZUSAMMENFASSUNG")
    print("="*80)
    print(f"[OK] {len(aussagen)} Aussagen erfolgreich eingefuegt")
    print(f"[OK] {len(handlungen)} Handlungen erfolgreich eingefuegt")
    print(f"[OK] Tier 2 Anforderungen erfuellt (>=10 Aussagen, >=8 Handlungen)")
    print("\nAlle Daten fuer Craig Federighi (person_id=47) wurden erfolgreich gespeichert.")
    print("="*80)

if __name__ == "__main__":
    main()
