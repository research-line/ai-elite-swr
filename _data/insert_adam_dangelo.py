#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data insertion script for Adam D'Angelo (person_id=81)
Research database: Weltbilder von KI/Silicon-Valley-Persönlichkeiten
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 81

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN
    aussagen = [
        # AGI & Future of AI
        (PERSON_ID,
         "It's so incredible that we are going to live through the creation of AGI. It will probably be the most important event in the history of the world and it will happen in our lifetimes.",
         "AGI most important event in history, will happen in our lifetimes",
         "schriftlich",
         "https://x.com/adamdangelo/status/1816644081554194871",
         "Adam D'Angelo on X (Twitter)",
         "2023-08-01",
         "en",
         "Statement on social media about AGI timeline and significance"),

        (PERSON_ID,
         "Artificial general intelligence is likely to happen within five to 15 years. The advent of AGI will be a very, very important change in the world when we get there.",
         "AGI timeline: 5-15 years, very important change",
         "muendlich",
         "https://www.pymnts.com/artificial-intelligence-2/2024/openai-board-member-agi-is-five-to-15-years-away/",
         "OpenAI Board Member: AGI is 5 to 15 Years Away - PYMNTS",
         "2024-07-01",
         "en",
         "Statement at event in July 2024 on AGI timeline prediction"),

        (PERSON_ID,
         "Right now there's a little bit of a climate of, like, if you say something that's too positive, people need to cut you down and remind you of all the bad things that happened in the past. But when you look at what's been enabled by this technology so far, it's very positive.",
         "AI progress has been very positive so far",
         "schriftlich",
         "https://a16z.com/adam-dangelo-ai-masses/",
         "Bringing AI to the Masses with Adam D'Angelo of Quora - a16z",
         "2023-04-01",
         "en",
         "Interview with a16z on AI development and societal impact"),

        (PERSON_ID,
         "At the point at which there is this super powerful AI, there will also be super powerful AI that is available to everyone else to defend themselves or rein it in or enforce the laws.",
         "Super powerful AI will be available to everyone for defense",
         "schriftlich",
         "https://medium.com/@micro-pc-tech-inc/quora-ceo-adam-dangelo-has-spoken-about-ai-fc4306acb065",
         "Quora CEO Adam D'Angelo has spoken about AI - Medium",
         "2023-01-01",
         "en",
         "Discussion on AI safety and democratization of powerful AI"),

        # Knowledge & Human Intelligence
        (PERSON_ID,
         "Quora has always been founded on the idea that humans have a lot of knowledge they have access to in their heads that's not on the internet anywhere. And AI will not have access to any of that knowledge.",
         "Humans have knowledge AI cannot access",
         "muendlich",
         "https://www.econtalk.org/adam-dangelo-on-knowledge-experimentation-and-quora/",
         "Adam D'Angelo on Knowledge, Experimentation, and Quora - EconTalk",
         "2023-01-01",
         "en",
         "Podcast interview on human knowledge vs. AI capabilities"),

        (PERSON_ID,
         "Being intellectual means more than just being able to search through knowledge—it means that you really like knowledge.",
         "Being intellectual means liking knowledge, not just searching it",
         "schriftlich",
         "https://globisinsights.com/leadership/startups/quora-knowledge-sharing/",
         "The Future of Knowledge Sharing with Quora CEO - GLOBIS Insights",
         "2023-01-01",
         "en",
         "Discussion on intellectual curiosity and knowledge-sharing philosophy"),

        (PERSON_ID,
         "More than a billion people use the Internet, yet only a tiny fraction contribute their knowledge to it.",
         "Only tiny fraction of internet users contribute knowledge",
         "schriftlich",
         "https://www.brainyquote.com/authors/adam-dangelo-quotes",
         "Adam D'Angelo Quotes - BrainyQuote",
         "2015-01-01",
         "en",
         "Quote on knowledge-sharing participation gap"),

        # AI Development & LLMs
        (PERSON_ID,
         "I was excited about AI early in my career and tried building AI products in college, but found the technology was too difficult and not ready for consumers at that time.",
         "Tried building AI products in college, technology wasn't ready",
         "schriftlich",
         "https://medium.com/@micro-pc-tech-inc/quora-ceo-adam-dangelo-has-spoken-about-ai-fc4306acb065",
         "Quora CEO Adam D'Angelo has spoken about AI - Medium",
         "2023-01-01",
         "en",
         "Reflection on early AI development attempts"),

        (PERSON_ID,
         "There will be significant value in knowing the source of information and having LLMs quote exact experts rather than synthesizing information in unverifiable ways.",
         "LLMs should quote exact experts, not synthesize unverifiably",
         "schriftlich",
         "https://a16z.com/adam-dangelo-ai-masses/",
         "Bringing AI to the Masses with Adam D'Angelo - a16z",
         "2024-01-01",
         "en",
         "Discussion on AI hallucination problems and information verification"),

        (PERSON_ID,
         "I expect exponential progress to continue for many years due to the concentration of talented and determined people focused on AI problems, despite potential roadblocks ahead.",
         "Exponential AI progress will continue for years",
         "schriftlich",
         "https://a16z.com/adam-dangelo-ai-masses/",
         "Bringing AI to the Masses with Adam D'Angelo - a16z",
         "2024-01-01",
         "en",
         "Prediction on AI development trajectory"),

        # OpenAI & Competition
        (PERSON_ID,
         "OpenAI is working towards this big mission to build AGI. And at Quora, we are looking to make AI products available to the world — including OpenAI's products.",
         "Quora makes AI products available, including OpenAI's",
         "schriftlich",
         "https://techcrunch.com/2024/05/06/adam-dangelo-quora-poe-open-ai/",
         "Quora CEO Adam D'Angelo talks about AI - TechCrunch",
         "2024-05-06",
         "en",
         "Interview on relationship between Quora/Poe and OpenAI"),

        (PERSON_ID,
         "I just can't talk about any of this stuff. I'm not here to represent OpenAI. I can just represent Quora.",
         "Can't discuss OpenAI board matters publicly",
         "schriftlich",
         "https://techcrunch.com/2024/05/06/adam-dangelo-quora-poe-open-ai/",
         "Quora CEO Adam D'Angelo talks about AI - TechCrunch",
         "2024-05-06",
         "en",
         "Response when asked about OpenAI board drama in May 2024"),

        # Poe Platform & Ecosystem
        (PERSON_ID,
         "We're coming into this market, we're lowering the barrier to entry, we're gonna enable this huge ecosystem of AI products to flourish.",
         "Poe enables huge ecosystem of AI products",
         "schriftlich",
         "https://venturebeat.com/ai/poe-wants-to-be-the-app-store-of-conversational-ai-will-pay-chatbot-creators",
         "Poe wants to be the App Store of conversational AI - VentureBeat",
         "2023-10-31",
         "en",
         "Statement on Poe's mission and marketplace strategy"),

        (PERSON_ID,
         "Today we are launching creator monetization for Poe! This program lets any bot creator on Poe generate revenue. This is a major step forward for the platform and is the first program of its kind, so we are very excited to see what it lets everyone create.",
         "Launching creator monetization on Poe",
         "schriftlich",
         "https://x.com/adamdangelo/status/1717237512077561869",
         "Adam D'Angelo on X (Twitter)",
         "2023-10-25",
         "en",
         "Announcement of Poe creator monetization program"),

        # Technology & Social Networks
        (PERSON_ID,
         "I view social networking technology as an alternative to AI, where instead of trying to get computers to do everything, you can connect people with other people over the internet who could do those things.",
         "Social networks as alternative to AI for tasks",
         "schriftlich",
         "https://medium.com/@micro-pc-tech-inc/quora-ceo-adam-dangelo-has-spoken-about-ai-fc4306acb065",
         "Quora CEO Adam D'Angelo has spoken about AI - Medium",
         "2023-01-01",
         "en",
         "Philosophy on social networks vs. AI for problem-solving"),

        (PERSON_ID,
         "The best consumer companies are built in tandem with shifts in technology—like how YouTube wasn't possible until broadband adoption and Flash integration, or how mobile phones made Instagram and Uber possible.",
         "Best companies built with technology shifts",
         "schriftlich",
         "https://a16z.com/adam-dangelo-ai-masses/",
         "Bringing AI to the Masses with Adam D'Angelo - a16z",
         "2024-01-01",
         "en",
         "Discussion on technology enablement of consumer products"),

        # Leadership & Mission
        (PERSON_ID,
         "You have to get comfortable giving up control, and you find people who do things better than you do.",
         "Leadership means giving up control to better people",
         "schriftlich",
         "https://www.brainyquote.com/authors/adam-dangelo-quotes",
         "Adam D'Angelo Quotes - BrainyQuote",
         "2015-01-01",
         "en",
         "Leadership philosophy on delegation and hiring"),

        (PERSON_ID,
         "There's a very positive impact on society when there's more access to knowledge. A lot of knowledge is inside people's heads and not accessible, and while the internet is vast, it's still not where we can access that knowledge easily. My goal is to make it easy.",
         "Goal: make knowledge in people's heads easily accessible",
         "schriftlich",
         "https://globisinsights.com/leadership/startups/quora-knowledge-sharing/",
         "The Future of Knowledge Sharing with Quora CEO - GLOBIS Insights",
         "2023-01-01",
         "en",
         "Statement on Quora's mission and societal impact"),

        (PERSON_ID,
         "We're playing a long-term game.",
         "Quora playing long-term game",
         "schriftlich",
         "https://allthingsd.com/20130520/quora-ceo-adam-dangelo-were-playing-a-long-term-game/",
         "Quora CEO Adam D'Angelo: We're Playing a Long-Term Game - AllThingsD",
         "2013-05-20",
         "en",
         "Statement on Quora's business strategy and patience"),
    ]

    # HANDLUNGEN
    handlungen = [
        # Gründungen
        (PERSON_ID,
         "gruendung",
         "Created BuddyZoo, a website allowing users to upload their AIM buddy list to compare with others and generate network graphs",
         "2004-01-01",
         "https://en.wikipedia.org/wiki/Adam_D'Angelo",
         "Adam D'Angelo - Wikipedia",
         "Early social networking project while attending Caltech"),

        (PERSON_ID,
         "gruendung",
         "Co-founded Quora with Charlie Cheever, a question-and-answer platform to share and grow world's knowledge",
         "2009-06-01",
         "https://en.wikipedia.org/wiki/Adam_D'Angelo",
         "Adam D'Angelo - Wikipedia",
         "Left Facebook CTO position in 2008 to start Quora in June 2009"),

        (PERSON_ID,
         "produktlaunch",
         "Launched Poe (Platform for Open Exploration), AI chatbot aggregation platform",
         "2023-02-01",
         "https://techcrunch.com/2024/05/06/adam-dangelo-quora-poe-open-ai/",
         "Quora CEO Adam D'Angelo talks about AI - TechCrunch",
         "Platform allowing users to interact with various AI chatbots"),

        (PERSON_ID,
         "produktlaunch",
         "Launched creator monetization program on Poe, first program of its kind",
         "2023-10-25",
         "https://x.com/adamdangelo/status/1717237512077561869",
         "Adam D'Angelo on X (Twitter)",
         "Allows bot creators to generate revenue up to $20 per subscriber"),

        (PERSON_ID,
         "produktlaunch",
         "Introduced price-per-message revenue model for AI bot creators on Poe",
         "2024-04-09",
         "https://techcrunch.com/2024/04/09/poe-introduces-a-price-per-message-revenue-model-for-ai-bot-creators/",
         "Poe introduces price-per-message revenue model - TechCrunch",
         "Additional monetization option allowing creators to charge per message"),

        # Einstellungen & Karriere
        (PERSON_ID,
         "einstellung",
         "Joined Facebook shortly after launch in 2004 as early engineer",
         "2004-01-01",
         "https://en.wikipedia.org/wiki/Adam_D'Angelo",
         "Adam D'Angelo - Wikipedia",
         "Met Mark Zuckerberg at Phillips Exeter Academy"),

        (PERSON_ID,
         "einstellung",
         "Appointed Chief Technology Officer (CTO) of Facebook",
         "2006-01-01",
         "https://en.wikipedia.org/wiki/Adam_D'Angelo",
         "Adam D'Angelo - Wikipedia",
         "Became first CTO of Facebook at age 22"),

        (PERSON_ID,
         "ruecktritt",
         "Left position as Facebook CTO and VP of Engineering",
         "2008-01-01",
         "https://venturebeat.com/business/facebook-cto-adam-dangelo-to-leave-or-at-least-take-an-extended-vacation/",
         "Facebook CTO Adam D'Angelo to leave - VentureBeat",
         "Left due to burnout and misalignment of responsibilities with interests"),

        (PERSON_ID,
         "einstellung",
         "Joined OpenAI board of directors",
         "2018-04-01",
         "https://en.wikipedia.org/wiki/Adam_D'Angelo",
         "Adam D'Angelo - Wikipedia",
         "Appointed as independent board member"),

        # Investitionen & Fundraising
        (PERSON_ID,
         "investition",
         "Personally invested $20 million in Quora as part of Series B funding",
         "2012-05-01",
         "https://techcrunch.com/2012/05/14/quora-raises-50-at-400m-from-peter-thiel-dangelo-puts-20m-of-his-own-money/",
         "Quora Raises $50M At $400M From Peter Thiel - TechCrunch",
         "Part of $50M Series B round led by Peter Thiel, valuing Quora at $400M"),

        (PERSON_ID,
         "investition",
         "Became investor in NFDG fund, AI-focused VC fund led by Nat Friedman and Daniel Gross",
         "2023-01-01",
         "https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/",
         "Meta in talks to acquire VC fund NFDG - DCD",
         "NFDG raised $1.1B fund with stakes in SSI, Perplexity, Character.ai"),

        (PERSON_ID,
         "investition",
         "Raised $75 million from Andreessen Horowitz (a16z) for Poe development",
         "2024-01-09",
         "https://techcrunch.com/2024/01/09/quora-75m-funding-a16z-poe-ai-chat/",
         "Quora raised $75M from a16z - TechCrunch",
         "Series I funding round valuing Quora at $425M to support Poe growth"),

        # Board-Actions & Governance
        (PERSON_ID,
         "politisch",
         "Voted to remove Sam Altman as OpenAI CEO alongside three other board members",
         "2023-11-17",
         "https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI",
         "Removal of Sam Altman from OpenAI - Wikipedia",
         "Board cited Altman not being 'consistently candid in communications'"),

        (PERSON_ID,
         "sonstiges",
         "Remained on OpenAI board after Sam Altman's reinstatement, only original member retained",
         "2023-11-21",
         "https://variety.com/2023/digital/news/openai-deal-sam-altman-return-ceo-new-board-1235805171/",
         "OpenAI Reaches Deal With Sam Altman - Variety",
         "New board formed with Bret Taylor (chair), Larry Summers, and D'Angelo"),

        (PERSON_ID,
         "einstellung",
         "Appointed to OpenAI's independent Safety and Security Committee as board oversight",
         "2024-09-16",
         "https://www.cnbc.com/2024/09/16/openai-announces-new-independent-board-oversight-committee-for-safety.html",
         "OpenAI announces independent board oversight committee - CNBC",
         "Committee chaired by Zico Kolter with Paul Nakasone and Nicole Seligman"),
    ]

    # Insert aussagen
    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen
            (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # Insert handlungen
    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen
            (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    conn.commit()

    # Count results
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    conn.close()

    return aussagen_count, handlungen_count

if __name__ == "__main__":
    print(f"Inserting data for Adam D'Angelo (person_id={PERSON_ID})...")
    aussagen_count, handlungen_count = insert_data()
    print(f"\n=== INSERTION COMPLETE ===")
    print(f"Aussagen eingefügt: {aussagen_count}")
    print(f"Handlungen eingefügt: {handlungen_count}")
    print(f"Gesamt: {aussagen_count + handlungen_count}")
