#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Ben Horowitz (person_id=49)
Tier 2: Mindestens 10 Aussagen + 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 49  # Ben Horowitz

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage_data)
    return cursor.lastrowid

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung,
            datum_handlung, quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)
    return cursor.lastrowid

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Beginne Datensammlung für Ben Horowitz (person_id={PERSON_ID})...")

    # ============================================================================
    # AUSSAGEN (Mindestens 10 für Tier 2)
    # ============================================================================

    aussagen = [
        # Aussage 1: AI als transformative Kraft
        (PERSON_ID,
         "This is on the order of the steam engine or electricity. AI is so powerful it will push society into 'a different world'.",
         "AI wird die Gesellschaft in eine völlig neue Welt transformieren - vergleichbar mit Dampfmaschine oder Elektrizität",
         "muendlich",  # modus
         1,  # quellen_typ_id: Video-Interview
         5,  # plattform_id: Nachrichtenmedien
         "https://finance.yahoo.com/news/ben-horowitz-says-fears-ai-125243493.html",
         "Ben Horowitz says fears of an AI-fueled job apocalypse are based on a flawed assumption",
         "2024-01-01",  # datum_aussage
         "en",
         "Interview über die transformative Kraft von KI und ihre gesellschaftlichen Auswirkungen",
         "Dies ist von der Größenordnung der Dampfmaschine oder der Elektrizität. KI ist so mächtig, dass sie die Gesellschaft in 'eine andere Welt' stoßen wird."),

        # Aussage 2: Unpredictability of AI impact
        (PERSON_ID,
         "I think people are acting as though it's very predictable when it's not at all predictable. I don't think it's nearly as predictable as people are saying.",
         "Die Auswirkungen von KI sind viel weniger vorhersehbar als viele behaupten",
         "muendlich",
         2,  # quellen_typ_id: Podcast-Interview
         3,  # plattform_id: Podcasts
         "https://a16z.com/podcast/when-will-ai-hit-the-enterprise-ben-horowitz-and-ali-ghodsi-discuss/",
         "When Will AI Hit the Enterprise? Ben Horowitz and Ali Ghodsi Discuss",
         "2023-10-01",
         "en",
         "Podcast-Diskussion über KI-Auswirkungen auf den Enterprise-Bereich",
         "Ich denke, die Leute handeln so, als wäre es sehr vorhersehbar, wenn es überhaupt nicht vorhersehbar ist. Ich glaube nicht, dass es auch nur annähernd so vorhersehbar ist, wie die Leute sagen."),

        # Aussage 3: AI regulation concern
        (PERSON_ID,
         "We have to make sure AI regulation doesn't slow down the tech industry. We've seen that in Europe, where they basically eliminated almost all innovation through this idea of the precautionary principle.",
         "KI-Regulierung nach europäischem Vorbild würde Innovation eliminieren - USA darf diesen Fehler nicht wiederholen",
         "muendlich",
         1,  # Video-Interview
         5,  # Nachrichtenmedien
         "https://www.cnbc.com/video/2024/01/30/ben-horowitz-we-have-to-make-sure-ai-regulation-doesnt-slow-down-the-tech-industry.html",
         "Ben Horowitz: We have to make sure AI regulation doesn't slow down the tech industry",
         "2024-01-30",
         "en",
         "CNBC-Interview über KI-Regulierung und Innovation",
         "Wir müssen sicherstellen, dass die KI-Regulierung die Tech-Industrie nicht verlangsamt. Wir haben das in Europa gesehen, wo sie durch die Idee des Vorsorgeprinzips fast alle Innovationen eliminiert haben."),

        # Aussage 4: Investment strategy on AI
        (PERSON_ID,
         "Investors should look for companies literally the best in the world at a thing, as opposed to those that are pretty good at a lot of things.",
         "Investoren sollten nach Unternehmen suchen, die weltbeste in einer Sache sind - nicht solche, die in vielem gut sind",
         "muendlich",
         1,  # Video-Interview
         5,  # Nachrichtenmedien
         "https://www.bloomberg.com/news/features/2026-01-19/andreessen-horowitz-makes-a-3-billion-bet-against-the-ai-bubble",
         "Andreessen Horowitz Makes a $3 Billion Bet Against the AI Bubble",
         "2026-01-19",
         "en",
         "Bloomberg-Feature über a16z's KI-Investmentstrategie",
         "Investoren sollten nach Unternehmen suchen, die buchstäblich die besten der Welt in einer Sache sind, im Gegensatz zu solchen, die in vielen Dingen ziemlich gut sind."),

        # Aussage 5: Culture is action
        (PERSON_ID,
         "Culturally, what you believe means nearly nothing. What you do is what you are.",
         "Unternehmenskultur wird durch Handlungen definiert, nicht durch Überzeugungen",
         "schriftlich",
         8,  # quellen_typ_id: Buch
         8,  # plattform_id: Bücher
         "https://fortune.com/2019/10/25/ben-horowitz-culture-book/",
         "Q&A: Ben Horowitz on His New Book, 'What You Do Is What You Are'",
         "2019-10-25",
         "en",
         "Zitat aus dem Buch 'What You Do Is What You Are' über Unternehmenskultur",
         "Kulturell gesehen bedeutet das, was Sie glauben, fast nichts. Was Sie tun, ist das, was Sie sind."),

        # Aussage 6: Leadership courage
        (PERSON_ID,
         "Every time you make the hard, correct decision you become a bit more courageous, and every time you make the easy, wrong decision you become a bit more cowardly. If you are CEO, these choices will lead to a courageous or cowardly company.",
         "CEOs schaffen durch ihre Entscheidungen mutige oder feige Unternehmen",
         "schriftlich",
         8,  # Buch
         8,  # Bücher
         "https://www.goodreads.com/author/quotes/7155094.Ben_Horowitz",
         "Ben Horowitz Quotes - The Hard Thing About Hard Things",
         "2014-03-04",
         "en",
         "Zitat aus 'The Hard Thing About Hard Things' über Führungsqualitäten",
         "Jedes Mal, wenn Sie die harte, richtige Entscheidung treffen, werden Sie ein bisschen mutiger, und jedes Mal, wenn Sie die einfache, falsche Entscheidung treffen, werden Sie ein bisschen feiger. Wenn Sie CEO sind, werden diese Entscheidungen zu einem mutigen oder feigen Unternehmen führen."),

        # Aussage 7: Trump election celebration
        (PERSON_ID,
         "Hallelujah! This is really good for tech. The future of our business, the future of new technology and the future of America is literally at stake.",
         "Trump-Sieg ist 'Halleluja' für Tech-Industrie - Zukunft des Business stand auf dem Spiel",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://hoodline.com/2024/11/hallelujah-really-good-for-tech-andreessen-horowitz-founders-openly-celebrate-trump-win-criticize-tech-regulation/",
         "Hallelujah ... Really Good for Tech: Andreessen Horowitz Founders Celebrate Trump Win",
         "2024-11-06",
         "en",
         "Podcast nach Trump-Wahlsieg über die Zukunft der Tech-Industrie",
         "Halleluja! Das ist wirklich gut für Tech. Die Zukunft unseres Geschäfts, die Zukunft neuer Technologie und die Zukunft Amerikas stand buchstäblich auf dem Spiel."),

        # Aussage 8: Crypto under Biden
        (PERSON_ID,
         "The Biden Administration has been exceptionally destructive on tech policy across the industry, but especially as it relates to Crypto/Blockchain and AI.",
         "Biden-Administration war außergewöhnlich destruktiv für Tech-Politik, besonders für Crypto und KI",
         "schriftlich",
         5,  # Social-Media-Post
         2,  # Twitter/X
         "https://x.com/bhorowitz/status/1842344079163822239",
         "Ben Horowitz on X about Biden Administration tech policy",
         "2024-10-04",
         "en",
         "Twitter/X-Post über Tech-Politik der Biden-Administration",
         "Die Biden-Administration war außergewöhnlich destruktiv in der Tech-Politik in der gesamten Industrie, aber besonders in Bezug auf Crypto/Blockchain und KI."),

        # Aussage 9: Hip-hop and business
        (PERSON_ID,
         "People think of rap lyrics as being only about money, women, status and cocaine, but more pervasive themes are leadership, collaboration and the vulnerability beneath the swagger — all relevant in business.",
         "Hip-Hop-Texte handeln von Leadership, Kollaboration und Verletzlichkeit - alles relevant für Business",
         "muendlich",
         7,  # Nachrichtenartikel
         5,  # Nachrichtenmedien
         "https://www.seattletimes.com/business/from-hip-hop-hopeful-to-tech-management-expert/",
         "From hip-hop hopeful to tech management expert",
         "2014-03-01",
         "en",
         "Artikel über Horowitz' Verbindung zwischen Hip-Hop-Kultur und Business-Leadership",
         "Die Leute denken, dass Rap-Texte nur von Geld, Frauen, Status und Kokain handeln, aber durchdringendere Themen sind Führung, Zusammenarbeit und die Verletzlichkeit unter der Prahlerei - alles relevant im Geschäft."),

        # Aussage 10: AI job creation
        (PERSON_ID,
         "The idea that we could imagine all the jobs that are going to come, sitting here now, that AI is going to enable, I think is low.",
         "Wir können uns heute noch nicht alle Jobs vorstellen, die KI ermöglichen wird",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://finance.yahoo.com/news/ben-horowitz-says-fears-ai-125243493.html",
         "Ben Horowitz says fears of an AI-fueled job apocalypse are based on a flawed assumption",
         "2024-01-15",
         "en",
         "Podcast-Diskussion über KI und Jobmarkt-Transformation",
         "Die Idee, dass wir uns alle Jobs vorstellen könnten, die kommen werden, wenn wir jetzt hier sitzen, die KI ermöglichen wird, halte ich für unwahrscheinlich."),

        # Aussage 11: The Hard Thing quote
        (PERSON_ID,
         "The hard thing isn't setting a big, hairy, audacious goal. The hard thing is laying people off when you miss the big goal. The hard thing isn't hiring great people. The hard thing is when those 'great people' develop a sense of entitlement.",
         "Das Schwierige ist nicht die große Vision, sondern die harten operativen Entscheidungen danach",
         "schriftlich",
         8,  # Buch
         8,  # Bücher
         "https://www.goodreads.com/work/quotes/25548865-the-hard-thing-about-hard-things",
         "The Hard Thing About Hard Things Quotes by Ben Horowitz",
         "2014-03-04",
         "en",
         "Kernaussage aus 'The Hard Thing About Hard Things' über die wahren Herausforderungen im Management",
         "Das Schwierige ist nicht, ein großes, haariges, kühnes Ziel zu setzen. Das Schwierige ist, Leute zu entlassen, wenn man das große Ziel verfehlt. Das Schwierige ist nicht, großartige Leute einzustellen. Das Schwierige ist, wenn diese 'großartigen Leute' ein Anspruchsdenken entwickeln."),

        # Aussage 12: AI and crypto synergy
        (PERSON_ID,
         "Crypto is the missing layer for AI, giving AI money, identity, provenance against deepfakes, and a decentralized registry of truth.",
         "Crypto ist die fehlende Schicht für KI - gibt ihr Geld, Identität und Schutz gegen Deepfakes",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://blockonomi.com/ai-has-machines-crypto-brings-the-network-says-ben-horowitz",
         "AI Has Machines, Crypto Brings the Network, Says Ben Horowitz",
         "2024-08-15",
         "en",
         "Podcast über die Synergie zwischen KI und Blockchain-Technologie",
         "Crypto ist die fehlende Ebene für KI und gibt der KI Geld, Identität, Herkunft gegen Deepfakes und ein dezentrales Register der Wahrheit."),

        # Aussage 13: Renewed crypto optimism post-election
        (PERSON_ID,
         "I've talked to so many crypto founders who are just like, 'We can build these products now.'",
         "Nach Trump-Sieg: Crypto-Gründer sagen 'wir können diese Produkte jetzt bauen'",
         "muendlich",
         2,  # Podcast-Interview
         3,  # Podcasts
         "https://fortune.com/2025/10/12/ben-horowitz-raghu-raghuram-interview-ai-politics/",
         "Ben Horowitz and Raghu Raghuram on AI, politics, and the questions they don't have easy answers to",
         "2024-11-15",
         "en",
         "Interview über erneuten Optimismus in der Crypto-Szene nach Politikwechsel",
         "Ich habe mit so vielen Crypto-Gründern gesprochen, die einfach sagten: 'Wir können diese Produkte jetzt bauen.'"),
    ]

    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for i, aussage in enumerate(aussagen, 1):
        aussage_id = insert_aussage(cursor, aussage)
        print(f"  [{i}/{len(aussagen)}] Aussage eingefügt (ID: {aussage_id})")

    # ============================================================================
    # HANDLUNGEN (Mindestens 8 für Tier 2)
    # ============================================================================

    handlungen = [
        # Handlung 1: Opsware Gründung
        (PERSON_ID,
         "gruendung",
         "Co-Gründung von Loudcloud (später Opsware) mit Marc Andreessen, Tim Howes und In Sik Rhee - eines der ersten SaaS-Unternehmen mit Infrastructure-as-a-Service-Modell",
         "1999-09-09",
         "https://en.wikipedia.org/wiki/Opsware",
         "Opsware - Wikipedia",
         "Gründung von Loudcloud/Opsware als Pionier im Cloud-Computing-Bereich"),

        # Handlung 2: Opsware Verkauf an HP
        (PERSON_ID,
         "verkauf",
         "Verkauf von Opsware an Hewlett-Packard für 1,6 Milliarden Dollar in bar - HPs drittgrößte Akquisition nach Compaq und Mercury Interactive",
         "2007-07-01",
         "https://en.wikipedia.org/wiki/Ben_Horowitz",
         "Ben Horowitz - Wikipedia",
         "Erfolgreicher Exit von Opsware nach dramatischer Transformation von Loudcloud zu einem Softwareunternehmen"),

        # Handlung 3: Andreessen Horowitz Gründung
        (PERSON_ID,
         "gruendung",
         "Co-Gründung der Venture-Capital-Firma Andreessen Horowitz (a16z) mit Marc Andreessen - heute eine der einflussreichsten VC-Firmen im Silicon Valley",
         "2009-07-01",
         "https://en.wikipedia.org/wiki/Andreessen_Horowitz",
         "Andreessen Horowitz - Wikipedia",
         "Gründung von a16z, das zu einem der größten und einflussreichsten VC-Firmen werden sollte"),

        # Handlung 4: a16z Crypto Fund Launch
        (PERSON_ID,
         "gruendung",
         "Launch des a16z crypto Fund mit 300 Millionen Dollar - dedizierter Fonds für Investments in Crypto-Unternehmen und Blockchain-Protokolle",
         "2018-06-25",
         "https://www.cryptoninjas.net/2018/06/25/a16z-sets-up-300-million-venture-fund-to-invest-in-crypto-companies/",
         "a16z sets up $300 million venture fund to invest in crypto companies",
         "Etablierung von a16z als Major Player im Crypto/Blockchain-Bereich"),

        # Handlung 5: Mistral AI Investment
        (PERSON_ID,
         "investition",
         "a16z führt Series-A-Investment in Mistral AI durch - französisches KI-Startup für Open-Source Large Language Models, Bewertung nähert sich 2 Milliarden Dollar",
         "2023-12-11",
         "https://www.pymnts.com/news/artificial-intelligence/2023/mistral-ai-raises-487-million-in-round-led-by-andreessen-horowitz/",
         "Mistral AI Raises $487 Million in Round Led by Andreessen Horowitz",
         "Strategisches Investment in europäischen OpenAI-Konkurrenten mit Open-Source-Fokus"),

        # Handlung 6: Character.AI Investment
        (PERSON_ID,
         "investition",
         "a16z investiert 100 Millionen Dollar in Character.AI - Plattform für KI-Chatbots und virtuelle Charaktere",
         "2023-03-01",
         "https://techcrunch.com/2026/01/09/the-venture-firm-that-ate-silicon-valley/",
         "The venture firm that ate Silicon Valley just raised another $15 billion",
         "Investment in Consumer-facing AI-Anwendungen und Chatbot-Technologie"),

        # Handlung 7: Trump Campaign Donation
        (PERSON_ID,
         "spende",
         "Spende von 2,5 Millionen Dollar an pro-Trump Super-PAC - öffentliche Unterstützung von Donald Trump im Präsidentschaftswahlkampf 2024",
         "2024-07-16",
         "https://www.bloomberg.com/news/articles/2024-10-16/silicon-valley-s-andreessen-horowitz-give-millions-to-trump-pac",
         "Silicon Valley's Andreessen, Horowitz Give Millions to Trump",
         "Politische Positionierung zugunsten Trump wegen Sorgen über Tech-Regulierung unter Biden"),

        # Handlung 8: Harris Campaign Donation (Flip-Flop)
        (PERSON_ID,
         "spende",
         "Ben und Felicia Horowitz kündigen 'signifikante Spende' an Kamala Harris' Kampagne an - nur 3 Monate nach Trump-Unterstützung",
         "2024-10-04",
         "https://fortune.com/2024/10/05/ben-horowitz-donattion-kamala-harris-campaign-donald-trump-marc-andreessn/",
         "Ben Horowitz will donate to Harris campaign after Trump support",
         "Kontroverse politische Kehrtwende, die Kritik sowohl von Demokraten als auch Republikanern hervorrief"),

        # Handlung 9: $7.2 Billion Fund Raise
        (PERSON_ID,
         "investition",
         "a16z sammelt 7,2 Milliarden Dollar für Tech-Investments mit Fokus auf AI und Gaming - einer der größten VC-Fonds aller Zeiten",
         "2024-04-17",
         "https://www.cryptotimes.io/2024/04/17/a16z-raises-7-2-billion-for-tech-investments-in-gaming-ai/",
         "a16z Raises $7.2 Billion for Tech Investments in Gaming & AI",
         "Massive Kapitalaufnahme unterstreicht a16z's Dominanz und Fokus auf KI-Investments"),

        # Handlung 10: Leading the Future Super PAC
        (PERSON_ID,
         "gruendung",
         "Horowitz und Andreessen gründen 'Leading the Future' Super-PAC mit 100 Millionen Dollar - Ziel: sicherstellen, dass USA bei KI-Innovation, Entwicklung und Governance führend bleibt",
         "2024-08-01",
         "https://www.rollingstone.com/politics/politics-features/ai-industry-cryptocurrency-model-influence-2026-midterms-1235475232/",
         "Crypto Won Big in 2024. AI Is Angling to Do the Same in 2026",
         "Direktes Lobbying und politische Einflussnahme für KI-freundliche Regulierung"),

        # Handlung 11: Buch-Publikation "The Hard Thing About Hard Things"
        (PERSON_ID,
         "produktlaunch",
         "Publikation des Management-Buches 'The Hard Thing About Hard Things: Building a Business When There Are No Easy Answers' - wurde zum Bestseller und Standardwerk für Startup-Gründer",
         "2014-03-04",
         "https://www.amazon.com/Hard-Thing-About-Things-Building/dp/0062273205",
         "The Hard Thing About Hard Things - Amazon",
         "Einflussreiches Buch über die harten Realitäten des Unternehmertums mit Hip-Hop-Zitaten"),

        # Handlung 12: Buch-Publikation "What You Do Is What You Are"
        (PERSON_ID,
         "produktlaunch",
         "Publikation von 'What You Do Is What You Are: How to Create Your Business Culture' - Buch über Unternehmenskultur basierend auf historischen Beispielen",
         "2019-10-25",
         "https://fortune.com/2019/10/25/ben-horowitz-culture-book/",
         "Q&A: Ben Horowitz on His New Book, 'What You Do Is What You Are'",
         "Zweites einflussreiches Management-Buch mit Fokus auf Kultur-Bildung in Unternehmen"),
    ]

    print(f"\nFüge {len(handlungen)} Handlungen ein...")
    for i, handlung in enumerate(handlungen, 1):
        handlung_id = insert_handlung(cursor, handlung)
        print(f"  [{i}/{len(handlungen)}] Handlung eingefügt (ID: {handlung_id})")

    # Änderungen speichern
    conn.commit()

    # Statistik ausgeben
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    anzahl_aussagen = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    anzahl_handlungen = cursor.fetchone()[0]

    print("\n" + "="*70)
    print("ZUSAMMENFASSUNG")
    print("="*70)
    print(f"Person: Ben Horowitz (ID: {PERSON_ID})")
    print(f"Aussagen eingefuegt: {anzahl_aussagen}")
    print(f"Handlungen eingefuegt: {anzahl_handlungen}")
    tier_status = "OK - Tier 2 erfuellt" if anzahl_aussagen >= 10 and anzahl_handlungen >= 8 else "FEHLER - Tier 2 nicht erfuellt"
    print(f"Tier-Status: {tier_status}")
    print("="*70)

    conn.close()
    print("\nDatensammlung erfolgreich abgeschlossen!")

if __name__ == "__main__":
    main()
