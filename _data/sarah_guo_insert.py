#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data insertion script for Sarah Guo (person_id=87)
Research database on worldviews of AI/Silicon Valley personalities
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (Statements)
    aussagen = [
        # Statement 1 - AI value creation
        (87, "AI is the biggest value creation opportunity in our lifetimes.",
         "AI biggest value creation opportunity",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Interview about founding Conviction and AI investment thesis"),

        # Statement 2 - Software 3.0 definition
        (87, "If Software 1.0 was about human-written code, and Software 2.0 is about dataset labeling, Software 3.0 will be about manipulating foundation models.",
         "Software 3.0 definition",
         "schriftlich",
         "https://sarahguo.com/blog/foundationmodels",
         "The Age of Open Foundation Models - Sarah Guo",
         "2022-09-01", "en",
         "Blog post defining Software 3.0 and foundation models"),

        # Statement 3 - Execution is the moat
        (87, "Execution is the moat. In an environment where foundational AI capabilities are becoming increasingly accessible, the true differentiator is the ability to rapidly and effectively build, iterate, and integrate these capabilities into solutions that solve real-world problems.",
         "Execution is the moat",
         "schriftlich",
         "https://www.startuphub.ai/ai-news/ai-video/2025/execution-is-the-moat-sarah-guos-state-of-ai-startups/",
         "Execution is the Moat: Sarah Guo's State of AI Startups",
         "2025-01-15", "en",
         "State of AI Startups presentation"),

        # Statement 4 - Code as first killer AI app
        (87, "Code is the first killer AI app because it is structured text allowing for deterministic validation, is seen as crucial to Artificial General Intelligence (AGI), and developers intimately understood their users' workflows.",
         "Code is first killer AI app",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Discussion of AI applications and their potential"),

        # Statement 5 - Anti-regulation stance
        (87, "I am strongly on the reduce regulation, encourage innovation side. From an industrial policy and national security perspective, if the US wants to be winning in AI in a durable way, the paths are clear—people need compute, and it must be made a priority in the United States.",
         "Anti-AI regulation stance",
         "schriftlich",
         "https://sarahguo.com/blog/listenerqa23-04",
         "No Priors: Elad & Sarah on AI Investment Hype, Foundation Models, Regulation (TRANSCRIPT)",
         "2023-04-01", "en",
         "No Priors podcast episode on AI regulation and policy"),

        # Statement 6 - AI marketing skepticism
        (87, "I have a really strong allergic reaction to aggressive AI marketing, citing five-plus years of snake oil salesmanship around AI as a solution to all customer problems.",
         "Skeptical of AI marketing hype",
         "schriftlich",
         "https://www.startuphub.ai/ai-news/ai-video/2025/execution-is-the-moat-sarah-guos-state-of-ai-startups/",
         "Execution is the Moat: Sarah Guo's State of AI Startups",
         "2025-01-15", "en",
         "Commentary on AI industry marketing practices"),

        # Statement 7 - Gap between theory and practice
        (87, "I actually think that's like half the opportunity for startups... if you don't get it all the way to end user value... it doesn't matter what the technology was.",
         "End user value matters most",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Discussion of startup opportunities in AI"),

        # Statement 8 - Human-AI coexistence
        (87, "People who know how to leverage these models and use these models as tools will, like, I think that type of human productivity is going to be relevant for a while.",
         "Human productivity with AI tools",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Views on future of human-AI collaboration"),

        # Statement 9 - Innovation momentum
        (87, "Innovation happens inexorably, but at uneven speeds. After years of nothing foundationally new happening (outside of crypto) we are at a special moment in technology history.",
         "Special moment in tech history",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Reflection on technology innovation cycles"),

        # Statement 10 - AGI litmus test
        (87, "Can you hire it? This perspective emphasizes functional capability—whether AI systems can autonomously handle complex, multi-step work—rather than philosophical definitions of general intelligence.",
         "Hire it test for AGI",
         "schriftlich",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "2022-10-14", "en",
         "Practical test for artificial general intelligence"),

        # Statement 11 - Open source models
        (87, "Open source models can be fine-tuned for different use cases that are commercially viable. There is now healthy competition amongst foundation models across multiple dimensions, including control (oss / fine tuning / policy).",
         "Open source AI models viability",
         "schriftlich",
         "https://sarahguo.com/blog/foundationmodels",
         "The Age of Open Foundation Models - Sarah Guo",
         "2022-09-01", "en",
         "Blog post on open source foundation models"),

        # Statement 12 - Transparency philosophy
        (87, "You are much more likely to find the truth if you are curious and willing to be wrong.",
         "Truth through curiosity",
         "schriftlich",
         "https://fortune.com/2025/04/14/conviction-ai-venture-sarah-guo-greylock-investor/",
         "Sarah Guo's path to becoming a top AI investor | Fortune",
         "2025-04-14", "en",
         "On publishing LP letters and intellectual transparency"),

        # Statement 13 - Entrepreneurship and progress
        (87, "People who oppose economic and technical progress are confused about where prosperity comes from. Entrepreneurship and competition are the only engines we have found that reliably produce progress.",
         "Entrepreneurship drives progress",
         "schriftlich",
         "http://sarahguo.com/",
         "Sarah Guo - Personal Website",
         "2024-01-01", "en",
         "Personal website statement on economic progress"),

        # Statement 14 - AI Leapfrog Effect
        (87, "Traditionally conservative, low-tech industries are adopting AI at the fastest rates, with examples like Sierra resolving 70% of customer service tickets and Harvey achieving over $70M ARR in the legal sector.",
         "Low-tech industries leapfrogging with AI",
         "schriftlich",
         "https://www.startuphub.ai/ai-news/ai-video/2025/execution-is-the-moat-sarah-guos-state-of-ai-startups/",
         "Execution is the Moat: Sarah Guo's State of AI Startups",
         "2025-01-15", "en",
         "Observation on AI adoption patterns across industries"),

        # Statement 15 - Agentic AI growth
        (87, "There is a remarkable 50% increase in agentic startups over the past year, many demonstrating real-world utility.",
         "50% growth in agentic AI startups",
         "schriftlich",
         "https://www.startuphub.ai/ai-news/ai-video/2025/execution-is-the-moat-sarah-guos-state-of-ai-startups/",
         "Execution is the Moat: Sarah Guo's State of AI Startups",
         "2025-01-15", "en",
         "Analysis of agentic AI startup landscape"),

        # Statement 16 - StackBlitz vision
        (87, "StackBlitz is finally bringing production-grade, full-stack web development to the web, with a magical experience that's much better than local: faster, more secure, inherently collaborative.",
         "StackBlitz revolutionizes web development",
         "schriftlich",
         "https://sarahguo.com/blog/stackblitz",
         "Instant, Collaborative Developer Environments - Sarah Guo",
         "2022-04-01", "en",
         "Blog post announcing Greylock investment in StackBlitz"),

        # Statement 17 - China AI competition
        (87, "AI labs from China are releasing models that can outperform those from the United States, sparking concern and panic in Silicon Valley.",
         "Concern about China AI advances",
         "schriftlich",
         "https://www.ainvest.com/news/sarah-guo-invests-heavily-ai-sees-50-growth-potential-2504/",
         "Sarah Guo Invests Heavily in AI, Sees 50% Growth Potential",
         "2025-04-01", "en",
         "Commentary on US-China AI competition"),

        # Statement 18 - Baseten investment rationale
        (87, "This was my first bet that AI would be the most important technological shift of their lifetime, and has invested in every round of the company.",
         "Baseten as first AI bet",
         "schriftlich",
         "https://theaiinsider.tech/2025/02/21/baseten-lands-75m-from-ivp-and-spark-to-solve-ais-biggest-bottleneck-to-ubiquitous-adoption-inference/",
         "Baseten Lands $75M from IVP and Spark",
         "2025-02-21", "en",
         "Explaining Baseten investment on Day Zero"),
    ]

    # HANDLUNGEN (Actions)
    handlungen = [
        # Action 1 - Greylock join
        (87, "einstellung", "Joined Greylock Partners as venture capitalist, later becoming youngest General Partner",
         "2013-01-01",
         "https://en.wikipedia.org/wiki/Sarah_Guo",
         "Sarah Guo - Wikipedia",
         "Joined leading Silicon Valley VC firm at age 24"),

        # Action 2 - Greylock General Partner promotion
        (87, "einstellung", "Promoted to General Partner at Greylock Partners, becoming firm's youngest and first female GP in 53-year history",
         "2018-05-15",
         "https://techcrunch.com/2018/05/15/sarah-guo-breaks-through-at-greylock-becoming-the-first-female-general-partner-in-the-firms-53-year-history/",
         "Sarah Guo breaks through at Greylock | TechCrunch",
         "Historic appointment as youngest and first female GP at Greylock"),

        # Action 3 - Figma investment
        (87, "investition", "Led Greylock's seed investment in Figma when it was a seed-stage startup",
         "2013-06-01",
         "https://sarahguo.com/investments",
         "Investments - Sarah Guo",
         "Early investment in design tool that later reached $10B+ valuation"),

        # Action 4 - StackBlitz investment
        (87, "investition", "Led $7.9M seed round in StackBlitz with Greylock, joining board",
         "2022-04-01",
         "https://sarahguo.com/blog/stackblitz",
         "Instant, Collaborative Developer Environments - Sarah Guo",
         "Investment in WebContainer technology for browser-based development"),

        # Action 5 - Left Greylock
        (87, "ruecktritt", "Left Greylock Partners after 9 years to found own venture firm",
         "2022-07-01",
         "https://en.wikipedia.org/wiki/Sarah_Guo",
         "Sarah Guo - Wikipedia",
         "Departed Greylock to launch AI-focused investment firm"),

        # Action 6 - Founded Conviction
        (87, "gruendung", "Founded Conviction, early-stage venture capital firm focused on AI and Software 3.0",
         "2022-10-01",
         "https://techcrunch.com/2022/10/14/carving-out-conviction-around-the-future-of-ai-with-sarah-guo/",
         "Carving out conviction around the future of AI with Sarah Guo | TechCrunch",
         "Launched $101M fund targeting AI-native companies"),

        # Action 7 - Harvey investment
        (87, "investition", "Conviction invested in Harvey AI seed round ($5M led by OpenAI Startup Fund)",
         "2022-11-01",
         "https://en.wikipedia.org/wiki/Harvey_(software)",
         "Harvey (software) - Wikipedia",
         "Early investment in legal AI startup, now valued at $8B"),

        # Action 8 - HeyGen investment and board seat
        (87, "investition", "Conviction invested in HeyGen ($5.6M round), Sarah joined board replacing Sequoia China seat",
         "2023-11-01",
         "https://www.maginative.com/article/heygen-launches-avatar-2-0-and-announces-5-6-million-in-new-funding/",
         "HeyGen Launches Avatar 2.0 and Announces $5.6 Million in New Funding",
         "Investment and board appointment at AI video generation company"),

        # Action 9 - Mistral investment
        (87, "investition", "Conviction invested in Mistral AI, French open-source AI startup",
         "2023-12-01",
         "https://finance.yahoo.com/news/35-old-investor-backed-hottest-125740650.html",
         "35-year-old investor has backed the hottest companies in AI | Yahoo Finance",
         "Investment in European AI challenger, now valued at $6B"),

        # Action 10 - Sierra investment
        (87, "investition", "Conviction invested in Sierra, Bret Taylor's conversational AI platform",
         "2024-01-01",
         "https://fortune.com/2025/04/14/conviction-ai-venture-sarah-guo-greylock-investor/",
         "Conviction founder Sarah Guo invests in AI | Fortune",
         "Backed ex-Salesforce co-CEO's customer service AI startup, now valued at $10B"),

        # Action 11 - Cognition/Devin investment
        (87, "investition", "Conviction invested in Cognition AI, creator of Devin AI software engineer",
         "2024-03-01",
         "https://en.wikipedia.org/wiki/Sarah_Guo",
         "Sarah Guo - Wikipedia",
         "Early investment in autonomous coding assistant startup"),

        # Action 12 - Common Room board seat
        (87, "investition", "Led Series B funding round for Common Room and joined board with Greylock",
         "2021-06-01",
         "https://sarahguo.com/blog/networked-users-common-room",
         "Networked Users: Our Investment in Common Room - Sarah Guo",
         "Investment and board role at community-led growth platform"),

        # Action 13 - Baseten multiple rounds
        (87, "investition", "Conviction invested in every Baseten funding round from Day Zero through Series D",
         "2022-11-01",
         "https://theaiinsider.tech/2025/02/21/baseten-lands-75m-from-ivp-and-spark-to-solve-ais-biggest-bottleneck-to-ubiquitous-adoption-inference/",
         "Baseten Lands $75M from IVP and Spark",
         "Continued investment in AI inference platform, now valued at $5B"),

        # Action 14 - Mike Vernal partnership
        (87, "partnerschaft", "Added Mike Vernal (ex-Sequoia, ex-Facebook) as General Partner at Conviction",
         "2025-01-31",
         "https://techcrunch.com/2025/01/31/guos-conviction-partners-adds-mike-vernal-as-gp-raises-230m-fund/",
         "Guo's Conviction Partners adds Mike Vernal as GP | TechCrunch",
         "Strategic hire of veteran investor to scale Conviction"),

        # Action 15 - Conviction Fund II
        (87, "gruendung", "Raised $230M for Conviction's second fund, more than doubling debut fund size",
         "2025-01-31",
         "https://techcrunch.com/2025/01/31/guos-conviction-partners-adds-mike-vernal-as-gp-raises-230m-fund/",
         "Guo's Conviction Partners adds Mike Vernal as GP, raises $230M fund | TechCrunch",
         "Fund II totaling $230M vs $101M Fund I, focused on AI infrastructure and applications"),
    ]

    # Insert statements
    print("Inserting statements...")
    cursor.executemany("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussagen)

    # Insert actions
    print("Inserting actions...")
    cursor.executemany("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlungen)

    conn.commit()

    # Verify counts
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = 87")
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = 87")
    handlungen_count = cursor.fetchone()[0]

    print(f"\n=== INSERTION COMPLETE ===")
    print(f"Total Aussagen (Statements) inserted: {aussagen_count}")
    print(f"Total Handlungen (Actions) inserted: {handlungen_count}")
    print(f"Total records for Sarah Guo (person_id=87): {aussagen_count + handlungen_count}")

    conn.close()

if __name__ == "__main__":
    insert_data()
