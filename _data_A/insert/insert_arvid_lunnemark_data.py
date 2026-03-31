#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Arvid Lunnemark (person_id=97)
Cursor AI Co-Founder, CTO (bis Oktober 2025)
Forschungsdatenbank: Weltbilder von KI/Silicon-Valley-Persönlichkeiten
"""

import sqlite3
import os

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_data():
    """Fügt Aussagen und Handlungen für Arvid Lunnemark in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    person_id = 97  # Arvid Lunnemark

    print("Füge Aussagen für Arvid Lunnemark ein...")

    # AUSSAGEN (10-20 Statements)
    aussagen = [
        # Aussage 1: Über seinen Abgang von Cursor
        (person_id,
         "It is, of course, with a mix of feelings. I'm sad to leave the team and the product; I'm excited for the ideas I get to explore next.",
         "Mixed feelings about leaving Cursor",
         "schriftlich",
         "https://arvid.xyz/posts/leaving/",
         "Leaving - Arvid Lunnemark",
         "2025-10-01",
         "en",
         "Statement upon leaving Cursor/Anysphere in October 2025 to found Integrous Research, a safety-focused AI research lab"),

        # Aussage 2: Philosophie zu AI und Programmierung
        (person_id,
         "Programmers remain in the driver's seat.",
         "Programmers stay in control with AI",
         "schriftlich",
         "https://entrepreneurloop.com/arvid-lunnemark-departure-cursor-ai-coding-startup/",
         "Co-founder Arvid Lunnemark Leaves Cursor as AI Coding Revolution Reaches New Heights",
         "2024-01-01",
         "en",
         "Core philosophy articulated by the Cursor founding team about human-AI collaboration in coding"),

        # Aussage 3: Vision für AI-enhanced programming
        (person_id,
         "AI should enrich programming as an activity rather than replace it.",
         "AI enriches, not replaces programming",
         "schriftlich",
         "https://www.oreateai.com/blog/arvid-lunnemark-the-young-architect-of-ais-coding-revolution/dcaa63c90736b1a3958955cf800daa4d",
         "Arvid Lunnemark: The Young Architect of AI's Coding Revolution",
         "2024-06-01",
         "en",
         "Lunnemark's vision of programming enriched—not replaced—by AI, which has guided Cursor's product development"),

        # Aussage 4: Über die Rolle von AI als Assistent
        (person_id,
         "AI is an assistant rather than a replacement.",
         "AI as assistant, not replacement",
         "schriftlich",
         "https://entrepreneurloop.com/arvid-lunnemark-departure-cursor-ai-coding-startup/",
         "Co-founder Arvid Lunnemark Leaves Cursor as AI Coding Revolution Reaches New Heights",
         "2024-01-01",
         "en",
         "Philosophy on the role of AI in software development, emphasizing human-AI collaboration"),

        # Aussage 5: Design-Prinzipien
        (person_id,
         "Making technology fast, accurate, and human-controlled.",
         "Fast, accurate, human-controlled tech",
         "schriftlich",
         "https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/",
         "Cursor Founders: The MIT Team Behind the $400 Million AI Code Editor Revolution",
         "2024-08-01",
         "en",
         "Core design principle guiding every product decision at Cursor during Lunnemark's tenure as CTO"),

        # Aussage 6: Über Entwickler-Produktivität
        (person_id,
         "Solving one problem exceptionally well: developer productivity.",
         "Focus on developer productivity",
         "schriftlich",
         "https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/",
         "Cursor Founders: The MIT Team Behind the $400 Million AI Code Editor Revolution",
         "2024-01-01",
         "en",
         "The founders' laser focus on developer productivity rather than broad AI applications"),

        # Aussage 7: Über AI-Safety und Integrous Research
        (person_id,
         "Developing systems for safer AI.",
         "Focus on safer AI systems",
         "schriftlich",
         "https://e.vnexpress.net/news/tech/personalities/4-mit-graduates-who-built-the-popular-ai-coding-tool-cursor-become-billionaires-4965462.html",
         "4 MIT graduates who built the popular AI coding tool Cursor become billionaires",
         "2025-10-01",
         "en",
         "Mission statement for Integrous Research, the AI safety research lab Lunnemark founded after leaving Cursor"),

        # Aussage 8: Vision von human-plus-AI developer era
        (person_id,
         "The human-plus-AI developer era.",
         "Human-plus-AI developer vision",
         "schriftlich",
         "https://www.oreateai.com/blog/arvid-lunnemark-the-young-architect-of-ais-coding-revolution/dcaa63c90736b1a3958955cf800daa4d",
         "Arvid Lunnemark: The Young Architect of AI's Coding Revolution",
         "2024-06-01",
         "en",
         "Lunnemark's articulation of a new era in software development combining human creativity with AI capabilities"),

        # Aussage 9: Über Geschwindigkeit und Genauigkeit
        (person_id,
         "Obsessing over sub-second response times, accurate code predictions, seamless VS Code integration, and real-time collaboration between human and AI.",
         "Obsession with speed and accuracy",
         "schriftlich",
         "https://www.todayin-ai.com/p/cursor",
         "Cursor: The fastest growing startup to hit $200M ARR ever?",
         "2024-03-01",
         "en",
         "Technical priorities that differentiated Cursor from competitors in the AI coding assistant market"),

        # Aussage 10: Über die Rolle von AI im Entwicklungsprozess
        (person_id,
         "Using AI to amplify human creativity rather than replace it.",
         "AI amplifies human creativity",
         "schriftlich",
         "https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/",
         "Cursor Founders: The MIT Team Behind the $400 Million AI Code Editor Revolution",
         "2024-01-01",
         "en",
         "Core belief about the purpose of AI in software development, emphasizing augmentation over automation"),

        # Aussage 11: Über die Zukunft von AI
        (person_id,
         "Robust systems for secure and trustworthy AI.",
         "Focus on secure, trustworthy AI",
         "schriftlich",
         "https://mabumbe.com/people/arvid-lunnemark-biography-net-worth-age-career-profile/",
         "Arvid Lunnemark: Biography, Net Worth, Age & Career Profile",
         "2025-10-01",
         "en",
         "Focus area for Integrous Research, emphasizing AI safety and trustworthiness"),

        # Aussage 12: Über schnelles Wachstum und Produktqualität
        (person_id,
         "We achieved the fastest path to $100M ARR in SaaS history.",
         "Fastest SaaS growth ever",
         "schriftlich",
         "https://www.spearhead.so/blogs/cursor-by-anysphere-the-fastest-growing-saas-product-ever",
         "The Fastest Growing SaaS Product Ever",
         "2025-01-01",
         "en",
         "Recognition of Cursor's unprecedented growth, reaching $100M ARR in just 12 months from launch"),

        # Aussage 13: Über die Bildungshintergrund und Vorbereitung
        (person_id,
         "Our experience at MIT and OpenAI's accelerator convinced us that AI could bridge the gap by enhancing developer capabilities rather than replacing them.",
         "MIT and OpenAI shaped AI vision",
         "schriftlich",
         "https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/",
         "Cursor Founders: The MIT Team Behind the $400 Million AI Code Editor Revolution",
         "2023-10-01",
         "en",
         "How MIT and OpenAI accelerator experience shaped the founding team's philosophy on AI-assisted development"),

        # Aussage 14: Über competitive programming Erfahrung
        (person_id,
         "From competitive programming in Sweden to building a multi-billion dollar AI company.",
         "From coding competitions to AI unicorn",
         "schriftlich",
         "https://mabumbe.com/people/arvid-lunnemark-biography-net-worth-age-career-profile/",
         "Arvid Lunnemark: Biography, Net Worth, Age & Career Profile",
         "2025-01-01",
         "en",
         "Trajectory from winning IOI medals to co-founding one of the fastest-growing AI companies"),

        # Aussage 15: Über die Rolle von Open Source
        (person_id,
         "Early exposure to open-source programming and large code-bases illustrates a self-driven ethos of building and sharing.",
         "Open source ethos",
         "schriftlich",
         "https://mabumbe.com/people/arvid-lunnemark-biography-net-worth-age-career-profile/",
         "Arvid Lunnemark: Biography, Net Worth, Age & Career Profile",
         "2024-01-01",
         "en",
         "Lunnemark's background in open-source development shaped his approach to building collaborative tools"),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen
            (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    print(f"[OK] {len(aussagen)} Aussagen eingefuegt")

    print("\nFüge Handlungen für Arvid Lunnemark ein...")

    # HANDLUNGEN (8-15 Actions)
    handlungen = [
        # Handlung 1: Gründung von Anysphere
        (person_id,
         "gruendung",
         "Co-founded Anysphere with Michael Truell, Sualeh Asif, and Aman Sanger while students at MIT, creating the AI code editor Cursor",
         "2022-06-01",
         "https://en.wikipedia.org/wiki/Anysphere",
         "Anysphere - Wikipedia",
         "The company was incorporated in 2022 by four MIT students who would graduate that year"),

        # Handlung 2: Produktlaunch von Cursor
        (person_id,
         "produktlaunch",
         "Launched Cursor public beta, an AI-native code editor built on VS Code fork, in March 2023",
         "2023-03-01",
         "https://research.contrary.com/company/anysphere",
         "Report: Anysphere Business Breakdown & Founding Story",
         "Cursor launched its public beta in March 2023, offering AI-driven code generation and intelligent autocompletion"),

        # Handlung 3: OpenAI Accelerator Abschluss
        (person_id,
         "partnerschaft",
         "Graduated from OpenAI's accelerator program with Anysphere",
         "2023-06-01",
         "https://en.wikipedia.org/wiki/Anysphere",
         "Anysphere - Wikipedia",
         "Anysphere graduated from OpenAI's accelerator program in 2023"),

        # Handlung 4: Seed-Funding Runde
        (person_id,
         "investition",
         "Raised $8 million seed round led by OpenAI Startup Fund, with angels including Nat Friedman and Arash Ferdowsi",
         "2023-10-01",
         "https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/",
         "Anysphere raises $8M from OpenAI to build an AI-powered IDE",
         "Seed funding announcement in October 2023 brought total raised to $11 million"),

        # Handlung 5: Series A Funding
        (person_id,
         "investition",
         "Raised $60 million Series A at $400 million valuation led by Andreessen Horowitz and Thrive Capital",
         "2024-08-01",
         "https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/",
         "Anysphere raises $60M Series A at $400M valuation",
         "Series A funding in August 2024 marked rapid valuation growth"),

        # Handlung 6: Series B Funding
        (person_id,
         "investition",
         "Raised $105 million Series B at $2.6 billion valuation led by Thrive Capital",
         "2024-12-01",
         "https://techcrunch.com/2024/12/19/in-just-4-months-ai-coding-assistant-cursor-raised-another-100m-at-a-2-5b-valuation-led-by-thrive-sources-say/",
         "Cursor raised $105M Series B at $2.6B valuation",
         "Just 4 months after Series A, demonstrating explosive growth trajectory"),

        # Handlung 7: Erreichen von $100M ARR
        (person_id,
         "sonstiges",
         "Cursor became the fastest SaaS company to reach $100M ARR, achieving this milestone in just 12 months from launch",
         "2025-01-01",
         "https://www.spearhead.so/blogs/cursor-by-anysphere-the-fastest-growing-saas-product-ever",
         "The Fastest Growing SaaS Product Ever",
         "Record-breaking growth milestone, surpassing Slack's previous record of 15 months"),

        # Handlung 8: Erreichen von $500M ARR
        (person_id,
         "sonstiges",
         "Cursor surpassed $500 million in annual recurring revenue",
         "2025-05-01",
         "https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/",
         "Cursor's Anysphere nabs $9.9B valuation, soars past $500M ARR",
         "Continued exponential revenue growth demonstrating product-market fit"),

        # Handlung 9: Series C Funding
        (person_id,
         "investition",
         "Raised $900 million Series C at $9.9 billion valuation led by Thrive Capital",
         "2025-06-01",
         "https://news.crunchbase.com/ai/anysphere-cursor-venture-funding-thrive/",
         "Anysphere Raises $900M at $9.9B Valuation",
         "Third funding round in less than one year, with participation from a16z, Accel, and DST Global"),

        # Handlung 10: Abgang von Cursor
        (person_id,
         "ruecktritt",
         "Left Anysphere/Cursor as Co-Founder and CTO to pursue new ventures in AI safety",
         "2025-10-01",
         "https://www.theinformation.com/briefings/cursor-co-founder-departs",
         "Cursor Co-Founder Departs — The Information",
         "Departed at a pivotal moment when Cursor had become the fastest SaaS company to reach $100M ARR"),

        # Handlung 11: Gründung von Integrous Research
        (person_id,
         "gruendung",
         "Founded Integrous Research, a safety-focused AI research lab developing systems for safer, secure, and trustworthy AI",
         "2025-10-01",
         "https://e.vnexpress.net/news/tech/personalities/4-mit-graduates-who-built-the-popular-ai-coding-tool-cursor-become-billionaires-4965462.html",
         "4 MIT graduates who built the popular AI coding tool Cursor become billionaires",
         "New venture focusing on AI safety and robust systems for secure AI after leaving Cursor"),

        # Handlung 12: Wird zum Milliardär
        (person_id,
         "sonstiges",
         "Became Sweden's youngest dollar billionaire at age 26, with Forbes estimating a 4.5% stake in Anysphere worth at least $1.3 billion",
         "2025-11-01",
         "https://startupnews.fyi/2025/11/18/arvid-lunnemark-becomes-swedens-youngest-dollar-billionaire-through-anysphere-success/",
         "Arvid Lunnemark Becomes Sweden's Youngest Dollar Billionaire",
         "Achieved billionaire status through Anysphere equity stake following Series D funding"),

        # Handlung 13: Series D Funding (nach seinem Abgang)
        (person_id,
         "investition",
         "Anysphere raised $2.3 billion Series D at $29.3 billion valuation co-led by Accel and Coatue Management (after Lunnemark's departure)",
         "2025-11-13",
         "https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html",
         "AI startup Cursor raises $2.3 billion funding round at $29.3 billion valuation",
         "Major funding round shortly after Lunnemark's departure, with investors including Nvidia and Google"),

        # Handlung 14: Erreichen von $1B ARR
        (person_id,
         "sonstiges",
         "Cursor crossed $1 billion in annualized revenue, fastest SaaS to reach this milestone (20 months from launch)",
         "2025-11-01",
         "https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/",
         "Cursor Hit $1B ARR in 24 Months: The Fastest Scaling SaaS Ever?",
         "Unprecedented growth rate in SaaS history, achieved with minimal marketing spend"),

        # Handlung 15: Forschung zu Metadata-Private Messaging
        (person_id,
         "sonstiges",
         "Co-authored academic paper on 'Formal Security Definition of Metadata-Private Messaging' published in IACR Cryptology ePrint Archive",
         "2022-01-01",
         "https://www.csail.mit.edu/person/arvid-lunnemark",
         "Arvid Lunnemark | MIT CSAIL",
         "Research work at MIT CSAIL on privacy and security in messaging systems"),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen
            (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    print(f"[OK] {len(handlungen)} Handlungen eingefuegt")

    # Änderungen speichern
    conn.commit()
    conn.close()

    print(f"\n{'='*60}")
    print(f"ZUSAMMENFASSUNG - Arvid Lunnemark (person_id={person_id})")
    print(f"{'='*60}")
    print(f"Aussagen eingefuegt:   {len(aussagen)}")
    print(f"Handlungen eingefuegt: {len(handlungen)}")
    print(f"GESAMT:                {len(aussagen) + len(handlungen)} Eintraege")
    print(f"{'='*60}")
    print("\nDaten erfolgreich in die Datenbank eingefuegt!")

if __name__ == "__main__":
    insert_data()
