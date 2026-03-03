#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nat Friedman (person_id=70) - Aussagen und Handlungen
Ex-GitHub CEO, AI investor, AI Grant co-founder
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 70

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (20 Stück)
    aussagen = [
        # Technologie & Fortschritt
        (PERSON_ID,
         "As human beings it is our right (maybe our moral duty) to reshape the universe to our preferences. Technology, which is really knowledge, enables this.",
         "Recht/Pflicht, Universum nach Präferenzen zu formen",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "Friedman's philosophical statement about technology and human agency"),

        (PERSON_ID,
         "You should probably work on raising the ceiling, not the floor.",
         "Fokus auf Ceiling-Raising statt Floor-Raising",
         "schriftlich",
         "https://www.azquotes.com/author/45430-Nat_Friedman",
         "TOP 11 QUOTES BY NAT FRIEDMAN",
         None,
         "en",
         "Philosophy on innovation and ambition"),

        (PERSON_ID,
         "It's important to do things fast. You learn more per unit time because you make contact with reality more frequently.",
         "Schnelligkeit = mehr Realitätskontakt = mehr Lernen",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "On speed and iteration in product development"),

        (PERSON_ID,
         "Going fast makes you focus on what's important; there's no time for bullshit.",
         "Schnelligkeit zwingt zu Fokus auf Wichtiges",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "On speed as a forcing function for prioritization"),

        (PERSON_ID,
         "Energy is a necessary input for progress.",
         "Energie als notwendiger Input für Fortschritt",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "On the relationship between energy and progress"),

        # AI & Zukunft
        (PERSON_ID,
         "AI is clearly more capable than humans now. We know this is going to get better.",
         "KI bereits fähiger als Menschen, wird sich weiter verbessern",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "Statement on current and future AI capabilities"),

        (PERSON_ID,
         "We don't really quite understand mechanically what's happening inside them [AI models]... they're not engineered and designed, they're kind of grown.",
         "KI-Modelle werden 'gewachsen', nicht designt - mechanisch unverstanden",
         "schriftlich",
         "https://www.antoinebuteau.com/lessons-from-nat-friedman/",
         "Lessons from Nat Friedman",
         None,
         "en",
         "On the nature of AI models and lack of mechanistic understanding"),

        (PERSON_ID,
         "We spent the last year working closely with OpenAI to build GitHub Copilot. We've been using it internally for months, and can't wait for you to try it out; it's like a piece of the future teleported back to 2021.",
         "GitHub Copilot wie 'Stück Zukunft in 2021 teleportiert'",
         "schriftlich",
         "https://x.com/natfriedman/status/1409883713786241032",
         "Nat Friedman on X (Twitter)",
         "2021-06-29",
         "en",
         "Announcement of GitHub Copilot launch"),

        (PERSON_ID,
         "if you're on the side of application building, generally this is great news because prices are going to keep dropping 90% per year, capabilities are going to keep improving.",
         "KI-Preise sinken 90% p.a., Fähigkeiten steigen - gut für App-Builder",
         "muendlich",
         "https://stratechery.com/topic/events/interview/nat-friedman-and-daniel-gross/",
         "Stratechery Interviews with Nat Friedman and Daniel Gross",
         None,
         "en",
         "On competition among AI labs and impact on application developers"),

        # GitHub & Microsoft
        (PERSON_ID,
         "Github was a company that had a little bit of stage fright about shipping, so when we broke that static friction it felt great.",
         "GitHub hatte 'Lampenfieber beim Shipping' - statische Reibung überwunden",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "On transforming GitHub's culture as CEO"),

        (PERSON_ID,
         "We needed to show the world we cared about developers, not that we care about Microsoft.",
         "Wir mussten zeigen: Wir kümmern uns um Entwickler, nicht um Microsoft",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "On GitHub's positioning after Microsoft acquisition"),

        (PERSON_ID,
         "The revenue from the purchase is less than $200,000 and not financially material for our company.",
         "ICE-Vertrag unter $200k, finanziell nicht material",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         "2019",
         "en",
         "Statement on controversial ICE contract during GitHub tenure"),

        (PERSON_ID,
         "With all that we've accomplished in mind, and more than five great years at Microsoft under my belt, I've decided it's time for me to go back to my startup roots.",
         "Nach 5 Jahren Microsoft zurück zu Startup-Wurzeln",
         "schriftlich",
         "https://www.theregister.com/2021/11/03/github_ceo_quits/",
         "Nat Friedman quits as CEO of GitHub - The Register",
         "2021-11-03",
         "en",
         "Statement on stepping down from GitHub CEO role"),

        # Open Source & Philosophie
        (PERSON_ID,
         "Listen to developers, encourage innovation, and maintain the open source spirit.",
         "Entwicklern zuhören, Innovation fördern, Open-Source-Geist bewahren",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "Core leadership philosophy"),

        (PERSON_ID,
         "As human beings it is our right (maybe our moral duty) to reshape the universe to our preferences.",
         "Menschen haben Recht/Pflicht, Universum nach Präferenzen zu formen",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "Philosophical worldview on human agency and technology"),

        # AI Safety & Regulation
        (PERSON_ID,
         "Next time someone tells you we don't know how to put agency into current AI systems, show them this! It may be primitive, but it sure feels like agency.",
         "KI-Systeme zeigen primitive, aber echte Agency",
         "schriftlich",
         "https://x.com/natfriedman/status/1642600823674011648",
         "Nat Friedman on X (Twitter)",
         "2023-04-02",
         "en",
         "Comment on AI agency capabilities"),

        # Investments & AI Infrastructure
        (PERSON_ID,
         "The market, not just government, can drive responsible development, as leaving it all to companies like OpenAI, Anthropic and Google doesn't work either—voluntary safety commitments are already being walked back. Insurance creates a third way to align incentives and evolves with the technology.",
         "Markt (via Insurance) als dritter Weg neben Staat & freiwilligen Commitments",
         "schriftlich",
         "https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/",
         "AIUC emerges from stealth with $15M seed - Fortune",
         "2025-07-23",
         "en",
         "Via investment in AIUC - view on AI safety governance through market mechanisms"),

        # GitHub First Day
        (PERSON_ID,
         "On Nat Friedman's first day as CEO of Github, at 9am, he had meeting with his leadership team over Zoom. They were probably expecting a long term strategy, but instead he shared his screen and pulled up a GitHub repo where users could submit and vote on product feedback.",
         "Erster Tag als GitHub-CEO: User-Feedback-Repo statt Langzeitstrategie",
         "schriftlich",
         "https://x.com/danhockenmaier/status/1836783428143853644",
         "Dan Hockenmaier on X about Nat Friedman",
         "2018-10-29",
         "en",
         "Anecdote about Friedman's leadership approach - prioritizing user feedback"),

        # Vision & Impact
        (PERSON_ID,
         "He has always believed that the best technology is the one that helps humanity the most, and his journey spans from MIT to Microsoft, then to GitHub and the world of AI—not just about code, but about how vision and humanity can drive innovation.",
         "Beste Technologie hilft Menschheit am meisten - Vision & Humanität treiben Innovation",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "Summary of Friedman's philosophical approach to technology"),

        # Open Source Early Days
        (PERSON_ID,
         "I discovered Linux, and was impressed to find a free operating system with development tools and source code available—an incredible opportunity for me as a teenager in a small town in Virginia to learn from the best developers in the world.",
         "Linux als Teenager: Chance, von besten Entwicklern weltweit zu lernen",
         "schriftlich",
         "https://www.bittime.com/en/blog/nat-friedman-revolusi-ai-dan-open-source",
         "Nat Friedman: The Visionary Behind GitHub",
         None,
         "en",
         "On discovering open source and its democratizing effect on learning"),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen
            (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # HANDLUNGEN (15 Stück)
    handlungen = [
        # Gründungen
        (PERSON_ID,
         "gruendung",
         "Co-founded Ximian (originally International Gnome Support/Helix Code) with Miguel de Icaza to work on GNOME and Linux desktop environment",
         "1999-10-19",
         "https://en.wikipedia.org/wiki/Nat_Friedman",
         "Nat Friedman - Wikipedia",
         "Founded October 19, 1999; served as CEO 1999-2001, then VP Product Management until Novell acquisition"),

        (PERSON_ID,
         "gruendung",
         "Co-founded Xamarin with Miguel de Icaza to continue Mono project development after Novell layoffs",
         "2011-05-16",
         "https://techcrunch.com/2016/03/31/xamarin-ceo-nat-friedman-on-getting-acquired-by-microsoft/",
         "Xamarin CEO Nat Friedman on getting acquired by Microsoft - TechCrunch",
         "Founded May 16, 2011; Friedman served as CEO through Microsoft acquisition in 2016"),

        (PERSON_ID,
         "gruendung",
         "Co-founded AI Grant with Daniel Gross - non-profit program providing $250k funding + $250k Azure credits to AI startups",
         "2017",
         "https://aigrant.org/",
         "AI Grant",
         "Established 2017; notable alumni include Perplexity AI"),

        (PERSON_ID,
         "gruendung",
         "Co-founded California YIMBY with Zack Rosen and Brian Hanlon to address California's housing shortage through pro-housing advocacy",
         "2017",
         "https://www.housingisahumanright.org/selling-off-california-exposes-corporate-yimbys-ties-to-big-tech-and-big-real-estate/",
         "California YIMBY - Housing Is A Human Right",
         "Founded 2017; Friedman served as chairman; organization grew to 80,000+ members"),

        (PERSON_ID,
         "gruendung",
         "Co-founded NFDG venture capital fund with Daniel Gross, raising $1.1 billion debut fund focused on AI investments",
         "2023",
         "https://www.saastr.com/the-1-1b-vc-fund-that-4xd-in-two-years-then-got-acquired-by-meta/",
         "NFDG: The $1.1B VC Fund - SaaStr",
         "Fund launched 2023; invested $1M-$100M per round; portfolio included SSI, Perplexity, Character.ai"),

        # Verkäufe/Acquisitions
        (PERSON_ID,
         "verkauf",
         "Ximian acquired by Novell for improving Linux enterprise offerings",
         "2003-08-04",
         "https://www.deseret.com/2003/8/5/19739706/novell-buys-linux-company-ximian/",
         "Novell buys Linux company Ximian - Deseret News",
         "Acquired August 4, 2003; Friedman became Chief Technology and Strategy Officer for Open Source at Novell until Jan 2010"),

        (PERSON_ID,
         "verkauf",
         "Xamarin acquired by Microsoft for approximately $400-500 million",
         "2016-02",
         "https://techcrunch.com/2016/03/31/xamarin-ceo-nat-friedman-on-getting-acquired-by-microsoft/",
         "Xamarin CEO Nat Friedman on getting acquired by Microsoft - TechCrunch",
         "Acquisition discussions started mid-November 2015; term sheet signed January 1, 2016; announced February 2016; Friedman signed early morning Jan 1"),

        (PERSON_ID,
         "verkauf",
         "NFDG partially acquired by Meta as part of deal to hire Friedman and Gross for Meta Superintelligence Labs",
         "2025-06",
         "https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/",
         "Meta in talks to partially acquire VC fund NFDG - DCD",
         "Meta acquired minority stake in NFDG valued at over $1 billion; fund had 4X'd in two years"),

        # Einstellungen/Rollen
        (PERSON_ID,
         "einstellung",
         "Appointed CEO of GitHub following Microsoft's $7.5 billion acquisition, replacing Chris Wanstrath",
         "2018-10-29",
         "https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/",
         "Microsoft to acquire GitHub for $7.5 billion - Microsoft",
         "Assumed CEO role October 29, 2018; previously Microsoft corporate VP; acquisition completed same day"),

        (PERSON_ID,
         "einstellung",
         "Joined Meta Platforms as VP of Product at Meta Superintelligence Labs alongside Alexandr Wang",
         "2025-06",
         "https://time.com/collections/time100-ai-2025/7305854/alexandr-wang-and-nat-friedman/",
         "Alexandr Wang and Nat Friedman: TIME100 AI 2025",
         "Joined June 2025 to co-lead Meta Superintelligence Labs; oversees AI-driven products and applied research"),

        # Rücktritte
        (PERSON_ID,
         "ruecktritt",
         "Stepped down as CEO of GitHub to return to startup/entrepreneurial roots",
         "2021-11-03",
         "https://www.theregister.com/2021/11/03/github_ceo_quits/",
         "Nat Friedman quits as CEO of GitHub - The Register",
         "Announced November 3, 2021; effective November 15, 2021; replaced by Thomas Dohmke; served 3+ years as CEO"),

        # Investitionen
        (PERSON_ID,
         "investition",
         "Led $50 million funding round in Weights & Biases (with Daniel Gross) at $1.25B valuation",
         "2023-08-09",
         "https://www.prnewswire.com/news-releases/weights--biases-raises-50-million-round-led-by-daniel-gross-and-nat-friedman-announces-wb-prompts-301896349.html",
         "Weights & Biases Raises $50M - PR Newswire",
         "Led August 9, 2023 round; W&B serves OpenAI, Meta, Microsoft; total raised $250M"),

        (PERSON_ID,
         "investition",
         "Co-led seed financing of ElevenLabs (AI voice generation) with Andreessen Horowitz at ~$100M post-money valuation",
         "2023",
         "https://elevenlabs.io/blog/elevenlabs-launches-new-generative-voice-ai-products-and-announces-19m-series-a-round-led-by-nat-friedman-daniel-gross-and-andreessen-horowitz",
         "ElevenLabs Announces $19M Series A - ElevenLabs",
         "Co-led with a16z in 2023; later co-led $80M Series B; company became unicorn"),

        (PERSON_ID,
         "investition",
         "Led $15 million seed round in AIUC (Artificial Intelligence Underwriting Company) for AI agent insurance",
         "2025-07-23",
         "https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/",
         "AIUC emerges from stealth with $15M seed - Fortune",
         "Led seed round July 23, 2025; AIUC creates insurance and safety standards for AI agents"),

        # Produktlaunches
        (PERSON_ID,
         "produktlaunch",
         "Launched GitHub Copilot, AI pair programming tool built with OpenAI, as GitHub CEO",
         "2021-06-29",
         "https://x.com/natfriedman/status/1409883713786241032",
         "Nat Friedman on X announcing Copilot",
         "Announced June 29, 2021; one of earliest successful AI coding assistants; developed over 1 year with OpenAI"),

        # Sonstiges (Andromeda Cluster)
        (PERSON_ID,
         "sonstiges",
         "Built Andromeda Cluster supercomputer for NFDG portfolio ($100M cost): 3,200 H100 GPUs on 400 nodes with 3.2Tbps InfiniBand",
         "2023",
         "https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/",
         "Meta in talks to acquire NFDG - DCD",
         "Built during GPU shortage at ~$100M total cost; provides compute infrastructure for AI startups at $2.40-3.00/GPU/hour"),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen
            (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    conn.commit()

    # Zähle Einträge
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    conn.close()

    print(f"[OK] Erfolgreich eingefuegt fuer Nat Friedman (person_id={PERSON_ID}):")
    print(f"  - {aussagen_count} Aussagen")
    print(f"  - {handlungen_count} Handlungen")
    print(f"  - GESAMT: {aussagen_count + handlungen_count} Eintraege")

    return aussagen_count, handlungen_count

if __name__ == "__main__":
    insert_data()
