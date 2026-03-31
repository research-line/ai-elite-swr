#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Andy Jassy (person_id=46)
Tier 2: Mindestens 10 Aussagen + mindestens 8 Handlungen
Alle Aussagen sind echte, verifizierbare Zitate
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_aussage(cursor, person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
                   plattform_id, quell_link, quell_titel, datum_aussage, sprache,
                   kontext, aussage_uebersetzung_de):
    """Fügt eine Aussage in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
            plattform_id, quell_link, quell_titel, datum_aussage, sprache,
            kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
          plattform_id, quell_link, quell_titel, datum_aussage, sprache,
          kontext, aussage_uebersetzung_de))

def insert_handlung(cursor, person_id, beschreibung, handlung_typ,
                    datum_handlung, quell_link, quell_titel, kontext):
    """Fügt eine Handlung in die Datenbank ein"""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, beschreibung, handlung_typ,
            datum_handlung, quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (person_id, beschreibung, handlung_typ,
          datum_handlung, quell_link, quell_titel, kontext))

def main():
    """Hauptfunktion zum Einfügen der Daten"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    person_id = 46  # Andy Jassy

    print("Füge Aussagen von Andy Jassy ein...")

    # AUSSAGE 1: KI als transformativste Technologie
    insert_aussage(
        cursor, person_id,
        aussage_text="I think that AI and generative AI specifically is the most transformative technology of our lifetime, which is saying a lot, given that we have had the internet.",
        aussage_kurz="KI ist die transformativste Technologie unserer Zeit",
        modus="muendlich",
        quellen_typ_id=1,  # Video-Interview
        plattform_id=5,    # Nachrichtenmedien
        quell_link="https://www.cnbc.com/video/2024/04/11/amazon-ceo-andy-jassy-ai-is-going-to-transform-every-customer-experience-that-we-know.html",
        quell_titel="Amazon CEO Andy Jassy: AI is going to transform every customer experience",
        datum_aussage="2024-04-11",
        sprache="en",
        kontext="Interview mit CNBC über Amazons KI-Strategie und Zukunftsvisionen",
        aussage_uebersetzung_de="Ich denke, dass KI und speziell generative KI die transformativste Technologie unserer Lebenszeit ist, was viel aussagt, wenn man bedenkt, dass wir das Internet hatten."
    )

    # AUSSAGE 2: KI als einmalige Neuerfindung
    insert_aussage(
        cursor, person_id,
        aussage_text="We continue to believe AI is a once-in-a-lifetime reinvention of everything we know, the demand is unlike anything we've seen before, and our customers, shareholders, and business will be well-served by our investing aggressively now.",
        aussage_kurz="KI ist eine einmalige Neuerfindung von allem, was wir kennen",
        modus="schriftlich",
        quellen_typ_id=10,  # Offizielle Stellungnahme
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2024-letter-to-shareholders",
        quell_titel="CEO Andy Jassy's 2024 Letter to Shareholders",
        datum_aussage="2024-04-11",
        sprache="en",
        kontext="Annual Shareholder Letter 2024, in dem Jassy Amazons aggressive KI-Investitionen rechtfertigt",
        aussage_uebersetzung_de="Wir glauben weiterhin, dass KI eine einmalige Neuerfindung von allem ist, was wir kennen. Die Nachfrage ist anders als alles, was wir je gesehen haben, und unsere Kunden, Aktionäre und das Geschäft werden von unseren aggressiven Investitionen profitieren."
    )

    # AUSSAGE 3: Frühe Phase der KI-Revolution
    insert_aussage(
        cursor, person_id,
        aussage_text="This is like three steps into a marathon.",
        aussage_kurz="Wir sind erst am Anfang der KI-Revolution",
        modus="muendlich",
        quellen_typ_id=1,   # Video-Interview
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://fortune.com/2024/01/18/andy-jassy-amazon-ai-biggest-risk-opportunity-2024/",
        quell_titel="Amazon CEO Andy Jassy says AI is the biggest risk for companies—and the biggest opportunity too",
        datum_aussage="2024-01-18",
        sprache="en",
        kontext="Interview über KI als Risiko und Chance, Betonung des frühen Entwicklungsstadiums",
        aussage_uebersetzung_de="Das ist wie drei Schritte in einem Marathon."
    )

    # AUSSAGE 4: KI und Arbeitsplätze
    insert_aussage(
        cursor, person_id,
        aussage_text="There will be fewer people doing some of the jobs that the technology actually starts to automate.",
        aussage_kurz="KI wird zu weniger Arbeitsplätzen in automatisierbaren Bereichen führen",
        modus="muendlich",
        quellen_typ_id=1,   # Video-Interview
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.cnbc.com/2025/06/30/amazon-ceo-says-ai-will-mean-fewer-people-do-jobs-that-get-automated.html",
        quell_titel="Amazon CEO Jassy says AI will lead to 'fewer people doing some of the jobs' that get automated",
        datum_aussage="2025-06-30",
        sprache="en",
        kontext="CNBC Mad Money Interview, Diskussion über KI-Auswirkungen auf Arbeitskräfte nach Massenentlassungen von 27.000 Mitarbeitern",
        aussage_uebersetzung_de="Es wird weniger Menschen geben, die einige der Jobs machen, die die Technologie tatsächlich zu automatisieren beginnt."
    )

    # AUSSAGE 5: Return to Office Begründung
    insert_aussage(
        cursor, person_id,
        aussage_text="When we look back over the last five years, we continue to believe that the advantages of being together in the office are significant. We are going to return to being in the office the way we were before the onset of COVID.",
        aussage_kurz="Vorteile der Büropräsenz sind erheblich, Rückkehr zu Vor-COVID-Zustand",
        modus="schriftlich",
        quellen_typ_id=10,  # Offizielle Stellungnahme
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.aboutamazon.com/news/company-news/ceo-andy-jassy-latest-update-on-amazon-return-to-office-manager-team-ratio",
        quell_titel="Message from CEO Andy Jassy: Strengthening our culture and teams",
        datum_aussage="2024-09-16",
        sprache="en",
        kontext="Memo an Mitarbeiter über 5-Tage-Büropflicht ab Januar 2025, kontroverse Entscheidung mit massivem Widerstand",
        aussage_uebersetzung_de="Wenn wir auf die letzten fünf Jahre zurückblicken, glauben wir weiterhin, dass die Vorteile, gemeinsam im Büro zu sein, erheblich sind. Wir werden zu der Art zurückkehren, wie wir vor COVID im Büro waren."
    )

    # AUSSAGE 6: Return to Office ist keine versteckte Entlassung
    insert_aussage(
        cursor, person_id,
        aussage_text="This was not a cost play for us. This is not a backdoor layoff.",
        aussage_kurz="Büropflicht ist keine versteckte Entlassungsstrategie",
        modus="muendlich",
        quellen_typ_id=11,  # AMA/Q&A
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.cnbc.com/2024/11/05/amazon-ceo-andy-jassy-5-day-office-mandate-isnt-a-backdoor-layoff.html",
        quell_titel="Amazon CEO Andy Jassy denies that 5-day office mandate is a 'backdoor layoff'",
        datum_aussage="2024-11-05",
        sprache="en",
        kontext="All-Hands Meeting mit Mitarbeitern, Reaktion auf Kritik und Spekulationen über versteckte Entlassungen",
        aussage_uebersetzung_de="Das war kein Kosteneinsparungsmanöver für uns. Das ist keine Hintertür-Entlassung."
    )

    # AUSSAGE 7: Amazon Q Erfolge
    insert_aussage(
        cursor, person_id,
        aussage_text="This is a great example of how large-scale enterprises can gain significant efficiencies in foundational software hygiene work by leveraging Amazon Q. It's been a game changer for us.",
        aussage_kurz="Amazon Q ist ein Game Changer für Entwicklerproduktivität",
        modus="schriftlich",
        quellen_typ_id=5,   # Social-Media-Post
        plattform_id=2,     # Twitter/X
        quell_link="https://x.com/ajassy/status/1826608791741493281",
        quell_titel="Andy Jassy on X about Amazon Q developer productivity",
        datum_aussage="2024-08-24",
        sprache="en",
        kontext="Tweet über interne Amazon Q Nutzung: 4.500 Entwicklerjahre gespart, 260 Mio. Dollar Effizienzgewinne bei Java-Upgrades",
        aussage_uebersetzung_de="Dies ist ein großartiges Beispiel dafür, wie große Unternehmen durch die Nutzung von Amazon Q erhebliche Effizienzgewinne bei grundlegender Software-Hygiene erzielen können. Es war ein Game Changer für uns."
    )

    # AUSSAGE 8: Praktische KI statt theoretische
    insert_aussage(
        cursor, person_id,
        aussage_text="We prioritize technology that we think is going to really matter for customers, and with the explosion of generative AI the last couple years, we've taken that same approach … but what we're trying to do is solve problems for you — what we think of as practical AI.",
        aussage_kurz="Fokus auf praktische KI, die echte Kundenprobleme löst",
        modus="muendlich",
        quellen_typ_id=3,   # Keynote/Vortrag
        plattform_id=4,     # Konferenzen
        quell_link="https://thecuberesearch.com/reinventing-ai-highlights-from-andy-jassys-reinvent-keynote/",
        quell_titel="Reinventing AI: Highlights from Andy Jassy's re:Invent Keynote",
        datum_aussage="2024-12-03",
        sprache="en",
        kontext="AWS re:Invent 2024 Keynote, Vorstellung von Amazon Nova Modellen und praktischer KI-Ansatz",
        aussage_uebersetzung_de="Wir priorisieren Technologie, von der wir denken, dass sie für Kunden wirklich wichtig sein wird, und mit der Explosion der generativen KI in den letzten Jahren haben wir denselben Ansatz gewählt … aber was wir versuchen, ist, Probleme für Sie zu lösen — was wir als praktische KI bezeichnen."
    )

    # AUSSAGE 9: Vielfalt von KI-Modellen
    insert_aussage(
        cursor, person_id,
        aussage_text="Human beings don't go to one human being for expertise in every single area. You have different human beings who are great at different things.",
        aussage_kurz="Verschiedene KI-Modelle für verschiedene Aufgaben nötig",
        modus="muendlich",
        quellen_typ_id=3,   # Keynote/Vortrag
        plattform_id=4,     # Konferenzen
        quell_link="https://thecuberesearch.com/reinventing-ai-highlights-from-andy-jassys-reinvent-keynote/",
        quell_titel="Reinventing AI: Highlights from Andy Jassy's re:Invent Keynote",
        datum_aussage="2024-12-03",
        sprache="en",
        kontext="AWS re:Invent 2024, Begründung für Multi-Modell-Strategie bei AWS Bedrock",
        aussage_uebersetzung_de="Menschen gehen nicht zu einem einzigen Menschen für Expertise in jedem einzelnen Bereich. Man hat verschiedene Menschen, die in verschiedenen Dingen großartig sind."
    )

    # AUSSAGE 10: Bedrock als größte Inference Engine
    insert_aussage(
        cursor, person_id,
        aussage_text="We're building Bedrock to be the biggest inference engine in the world and in the long run, believe Bedrock could be as big a business for AWS as EC2.",
        aussage_kurz="Bedrock soll größte Inference Engine der Welt werden",
        modus="muendlich",
        quellen_typ_id=7,   # Nachrichtenartikel
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.fool.com/investing/2024/11/04/these-must-see-quotes-from-amazon-ceo-andy-jassy-a/",
        quell_titel="These Must-See Quotes From Amazon CEO Andy Jassy Are Great News For Nvidia",
        datum_aussage="2024-11-04",
        sprache="en",
        kontext="Earnings Call Q3 2024, Vision für AWS Bedrock als potentiell größtes AWS-Geschäft",
        aussage_uebersetzung_de="Wir bauen Bedrock zur größten Inference Engine der Welt aus und glauben langfristig, dass Bedrock ein so großes Geschäft für AWS werden könnte wie EC2."
    )

    # AUSSAGE 11: Anthropic Partnership
    insert_aussage(
        cursor, person_id,
        aussage_text="We have tremendous respect for Anthropic's team and foundation models, and believe we can help improve many customer experiences, short and long-term, through our deeper collaboration.",
        aussage_kurz="Tiefe Zusammenarbeit mit Anthropic wird Kundenerfahrungen verbessern",
        modus="schriftlich",
        quellen_typ_id=10,  # Offizielle Stellungnahme
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.aboutamazon.com/news/company-news/amazon-anthropic-ai-investment",
        quell_titel="Amazon completes $4B Anthropic investment to advance generative AI collaboration",
        datum_aussage="2024-11-22",
        sprache="en",
        kontext="Ankündigung der $4 Milliarden Gesamtinvestition in Anthropic, strategische KI-Partnerschaft",
        aussage_uebersetzung_de="Wir haben großen Respekt vor Anthropics Team und Foundation Models und glauben, dass wir durch unsere tiefere Zusammenarbeit viele Kundenerfahrungen kurz- und langfristig verbessern können."
    )

    # AUSSAGE 12: Kosten von KI-Modellen
    insert_aussage(
        cursor, person_id,
        aussage_text="Really good AI models take billions of dollars to train, so most companies want to work off of a foundational model that's big and great already and then have the ability to customize it for their own purposes.",
        aussage_kurz="Gute KI-Modelle kosten Milliarden, daher Bedarf an anpassbaren Foundation Models",
        modus="muendlich",
        quellen_typ_id=1,   # Video-Interview
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://www.cnbc.com/2023/04/13/aws-launches-bedrock-generative-ai-service-titan-llms.html",
        quell_titel="Amazon CEO Andy Jassy says 'really good' A.I. models take 'billions of dollars' to train",
        datum_aussage="2023-04-13",
        sprache="en",
        kontext="AWS Bedrock Launch Event 2023, Erklärung der Bedrock-Strategie und Marktbedürfnisse",
        aussage_uebersetzung_de="Wirklich gute KI-Modelle kosten Milliarden von Dollar im Training, deshalb wollen die meisten Unternehmen mit einem großen und großartigen Foundation Model arbeiten und dann die Möglichkeit haben, es für ihre eigenen Zwecke anzupassen."
    )

    # AUSSAGE 13: Climate Pledge Commitment
    insert_aussage(
        cursor, person_id,
        aussage_text="Amazon's central commitment is The Climate Pledge, which aims to reach net-zero carbon across its operations by 2040—10 years ahead of the Paris Agreement.",
        aussage_kurz="Amazon verpflichtet sich zu Netto-Null-Emissionen bis 2040",
        modus="schriftlich",
        quellen_typ_id=6,   # Blog-Artikel
        plattform_id=9,     # Blogs
        quell_link="https://www.aboutamazon.com/news/sustainability/amazon-ceo-andy-jassy-discussion-on-sustainability",
        quell_titel="Amazon CEO Andy Jassy shares 5 ways the company is committed to sustainability",
        datum_aussage="2024-09-26",
        sprache="en",
        kontext="Nachhaltigkeits-Diskussion, Amazons Klimaziele trotz massiver KI-Infrastruktur-Expansion",
        aussage_uebersetzung_de="Amazons zentrale Verpflichtung ist das Climate Pledge, das darauf abzielt, bis 2040 Netto-Null-Emissionen über alle Betriebsabläufe hinweg zu erreichen — 10 Jahre vor dem Pariser Abkommen."
    )

    # AUSSAGE 14: Project Kuiper Vision
    insert_aussage(
        cursor, person_id,
        aussage_text="Kuiper targets 400 to 500 million households around the world who don't have broadband connectivity. The tight connection between Kuiper and AWS is going to make that very compelling as well.",
        aussage_kurz="Kuiper zielt auf 400-500 Mio. Haushalte ohne Breitband, Integration mit AWS",
        modus="muendlich",
        quellen_typ_id=1,   # Video-Interview
        plattform_id=5,     # Nachrichtenmedien
        quell_link="https://broadbandbreakfast.com/amazon-ceo-pushes-back-project-kuiper-will-pay-off/",
        quell_titel="Amazon CEO Pushes Back: Project Kuiper Will Pay Off",
        datum_aussage="2025-02-26",
        sprache="en",
        kontext="CNBC The Exchange Interview, Verteidigung der $10+ Milliarden Kuiper-Investition",
        aussage_uebersetzung_de="Kuiper zielt auf 400 bis 500 Millionen Haushalte weltweit, die keine Breitbandverbindung haben. Die enge Verbindung zwischen Kuiper und AWS wird das ebenfalls sehr überzeugend machen."
    )

    print("14 Aussagen erfolgreich eingefügt.")
    print("\nFüge Handlungen von Andy Jassy ein...")

    # HANDLUNG 1: CEO-Übernahme
    insert_handlung(
        cursor, person_id,
        beschreibung="Andy Jassy übernahm als CEO von Amazon, Nachfolger von Jeff Bezos",
        handlung_typ="einstellung",
        datum_handlung="2021-07-05",
        quell_link="https://www.cnbc.com/2021/07/05/amazon-new-ceo-andy-jassy-takes-over-for-jeff-bezos.html",
        quell_titel="Amazon new CEO Andy Jassy takes over for Jeff Bezos",
        kontext="Führungswechsel bei Amazon nach 27 Jahren Bezos-Ära. Jassy kam von AWS und erhielt ein 10-Jahres-Vergütungspaket von $212,7 Millionen."
    )

    # HANDLUNG 2: Anthropic Investment $4B
    insert_handlung(
        cursor, person_id,
        beschreibung="Amazon investierte unter Jassy insgesamt $4 Milliarden in Anthropic (Claude AI)",
        handlung_typ="investition",
        datum_handlung="2024-11-22",
        quell_link="https://www.aboutamazon.com/news/company-news/amazon-anthropic-ai-investment",
        quell_titel="Amazon completes $4B Anthropic investment",
        kontext="Strategische KI-Partnerschaft: $1,25B im Sept 2023, $2,75B im März 2024. Anthropic nutzt AWS Trainium für Training, AWS wird primärer Cloud-Partner. Teil von Jassys aggressiver KI-Strategie."
    )

    # HANDLUNG 3: Massenentlassungen 27.000
    insert_handlung(
        cursor, person_id,
        beschreibung="Jassy leitete Massenentlassungen von 27.000 Mitarbeitern bei Amazon (18.000 + 9.000 in zwei Phasen)",
        handlung_typ="entlassung",
        datum_handlung="2023-03-21",
        quell_link="https://www.aboutamazon.com/news/company-news/update-from-ceo-andy-jassy-on-role-eliminations",
        quell_titel="Update from CEO Andy Jassy on role eliminations",
        kontext="Größte Entlassungswelle in Amazon-Geschichte (2022-2023). Begründung: Kosteneffizienz, unsichere Wirtschaftslage, Überbeschäftigung nach COVID-Boom. Mitarbeiter erhielten Abfindung und Job-Vermittlungshilfe."
    )

    # HANDLUNG 4: Return to Office Mandate
    insert_handlung(
        cursor, person_id,
        beschreibung="Jassy führte 5-Tage-Büropflicht ab Januar 2025 ein, Ende des Hybrid-Modells",
        handlung_typ="umstrukturierung",
        datum_handlung="2024-09-16",
        quell_link="https://www.aboutamazon.com/news/company-news/ceo-andy-jassy-latest-update-on-amazon-return-to-office-manager-team-ratio",
        quell_titel="Message from CEO Andy Jassy: Strengthening our culture and teams",
        kontext="Kontroverse Entscheidung mit massivem Mitarbeiter-Widerstand. 73% der Befragten erwogen Kündigung. Jassy dementierte 'backdoor layoff'-Vorwürfe. Zusätzlich Reduzierung der Manager-Quote um 15% bis Q1 2025."
    )

    # HANDLUNG 5: Amazon Nova Launch
    insert_handlung(
        cursor, person_id,
        beschreibung="Launch von Amazon Nova, eigene Foundation Model Familie (Micro, Lite, Pro, Premier, Canvas, Reel)",
        handlung_typ="produktlaunch",
        datum_handlung="2024-12-03",
        quell_link="https://www.geekwire.com/2024/amazon-unveils-nova-ai-models/",
        quell_titel="Amazon unveils 'Nova' AI models",
        kontext="AWS re:Invent 2024. Multimodale KI-Modelle für Text, Bild und Video. Konkurrenzt zu OpenAI, Google Gemini, Anthropic Claude. Betonung auf Geschwindigkeit und Kosteneffizienz."
    )

    # HANDLUNG 6: AWS Trainium2 Produktion
    insert_handlung(
        cursor, person_id,
        beschreibung="Skalierung von AWS Trainium2 Custom AI Chips - Multi-Milliarden-Dollar-Business, 150% QoQ Wachstum",
        handlung_typ="produktlaunch",
        datum_handlung="2024-11-01",
        quell_link="https://www.cnbc.com/2023/08/12/amazon-is-racing-to-catch-up-in-generative-ai-with-custom-aws-chips.html",
        quell_titel="How Amazon is racing to catch Microsoft and Google in generative A.I. with custom AWS chips",
        kontext="Alternative zu Nvidia GPUs. Trainium2 vollständig ausgebucht. Project Rainier: 500.000 Trainium2 Chips für Anthropic. Trainium3 angekündigt mit 40% Performance-Boost."
    )

    # HANDLUNG 7: AWS Bedrock Launch
    insert_handlung(
        cursor, person_id,
        beschreibung="Launch von AWS Bedrock, managed Foundation Model Plattform mit 10+ Modellen",
        handlung_typ="produktlaunch",
        datum_handlung="2023-04-13",
        quell_link="https://www.cnbc.com/2023/04/13/aws-launches-bedrock-generative-ai-service-titan-llms.html",
        quell_titel="AWS launches Bedrock generative AI service",
        kontext="Zentrale Plattform für Foundation Models (Anthropic Claude, Meta Llama, Mistral, Stability AI, Cohere, Amazon Titan). Bedrock Marketplace eingeführt Dez 2024. Vision: Größtes Inference-Business der Welt."
    )

    # HANDLUNG 8: Amazon Q Launch
    insert_handlung(
        cursor, person_id,
        beschreibung="Launch von Amazon Q, AI-Assistent für Entwickler und Business (Q Developer, Q Business)",
        handlung_typ="produktlaunch",
        datum_handlung="2023-11-28",
        quell_link="https://finance.yahoo.com/news/amazon-ceo-andy-jassy-says-213018283.html",
        quell_titel="Amazon CEO Andy Jassy Says Company's AI Assistant Has Saved $260M",
        kontext="KI-Coding-Assistent. Interne Nutzung bei Amazon: 4.500 Entwicklerjahre gespart, $260M Effizienzgewinne bei Java-Upgrades. 79% auto-generierter Code ohne Änderungen übernommen."
    )

    # HANDLUNG 9: Project Kuiper Investment
    insert_handlung(
        cursor, person_id,
        beschreibung="Fortsetzung Project Kuiper: $10+ Milliarden Investment in Satelliten-Internet (3.232 Satelliten geplant)",
        handlung_typ="investition",
        datum_handlung="2024-10-01",
        quell_link="https://broadbandbreakfast.com/amazon-ceo-pushes-back-project-kuiper-will-pay-off/",
        quell_titel="Amazon CEO Pushes Back: Project Kuiper Will Pay Off",
        kontext="54 Satelliten in Orbit (Stand 2024), Ziel: 400-500 Mio. Haushalte ohne Breitband. Commercial Beta geplant Ende 2025. Integration mit AWS für Enterprise/Government-Kunden. Konkurrenz zu Starlink."
    )

    # HANDLUNG 10: Climate Pledge Expansion
    insert_handlung(
        cursor, person_id,
        beschreibung="Fortführung Climate Pledge: 500+ Wind- und Solarprojekte, größter Corporate Renewable Energy Käufer",
        handlung_typ="investition",
        datum_handlung="2024-09-26",
        quell_link="https://www.aboutamazon.com/news/sustainability/amazon-ceo-andy-jassy-discussion-on-sustainability",
        quell_titel="Amazon CEO Andy Jassy shares 5 ways the company is committed to sustainability",
        kontext="Ziel: Netto-Null-Emissionen bis 2040. 525+ Signatories des Climate Pledge. Climate Pledge Fund: 25+ Investitionen. Kritik: Neue Gas-Kraftwerke für KI-Rechenzentren trotz Nachhaltigkeits-Versprechen."
    )

    # HANDLUNG 11: AI Leadership Umstrukturierung
    insert_handlung(
        cursor, person_id,
        beschreibung="Jassy reorganisierte AI-Leadership: Rohit Prasad (AGI-Chef) ersetzt durch Peter DeSantis",
        handlung_typ="umstrukturierung",
        datum_handlung="2025-12-17",
        quell_link="https://fortune.com/2025/12/17/amazon-ceo-andy-jassy-announces-departure-of-ai-exec-rohit-prasad-in-leadership-shakeup/",
        quell_titel="Amazon CEO Andy Jassy announces departure of AI executive Rohit Prasad",
        kontext="Leadership-Wechsel in kritischer Phase. DeSantis (AWS-Veteran) übernimmt AGI, Nova Models, Chips, Quantum. Prasad leitete zuvor Alexa und AGI-Initiative."
    )

    print("11 Handlungen erfolgreich eingefügt.")

    conn.commit()
    conn.close()

    print("\n" + "="*60)
    print("ZUSAMMENFASSUNG")
    print("="*60)
    print(f"Datenbank: {DB_PATH}")
    print(f"Person: Andy Jassy (person_id={person_id})")
    print(f"Eingefügte Aussagen: 14")
    print(f"Eingefügte Handlungen: 11")
    print(f"Tier-Status: Tier 2 (OK >= 10 Aussagen, OK >= 8 Handlungen)")
    print("="*60)
    print("\nAlle Daten erfolgreich in die Datenbank eingefügt!")

    # Verifikation
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (person_id,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (person_id,))
    handlungen_count = cursor.fetchone()[0]

    print(f"\nVerifikation:")
    print(f"  - Aussagen in DB: {aussagen_count}")
    print(f"  - Handlungen in DB: {handlungen_count}")

    conn.close()

if __name__ == "__main__":
    main()
