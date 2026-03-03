#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data insertion script for Daniel Gross (person_id=71)
Daniel Gross: AI Grant Co-Founder with Nat Friedman, ex-Apple AI Director, Pioneer fund founder
Database: aussagen_top100.db
"""

import sqlite3
import os

# Database path
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_data():
    """Insert statements and actions for Daniel Gross into the database."""

    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (Statements)
    aussagen = [
        # 1
        (71, "We want to democratize AI. We want to level the playing field for startups to ensure that innovation doesn't get locked up in large companies like Google or Facebook.",
         "Democratize AI to prevent big tech monopoly",
         "muendlich", "https://www.thetwentyminutevc.com/danielgross/", "20VC: YC's Daniel Gross on How YC Can Democratise AI",
         "2017-08-01", "en", "Interview on democratizing AI and reducing incumbency advantages"),

        # 2
        (71, "Part of my job at Y combinator is to kind of democratize AI again and to try to take those three properties that I mentioned that are today unique to large companies and kind of give them back to startups.",
         "YC mission to democratize AI infrastructure",
         "muendlich", "https://www.thetwentyminutevc.com/danielgross/", "20VC Interview with Daniel Gross",
         "2017-08-01", "en", "Discussing Y Combinator's role in supporting AI startups"),

        # 3
        (71, "Machine learning software will eat the software that has eaten the world.",
         "ML software will dominate all software",
         "muendlich", "https://www.thetwentyminutevc.com/danielgross/", "20VC Interview",
         "2017-08-01", "en", "Prediction about the future of machine learning in software"),

        # 4
        (71, "Doing monotonous labor with text, extracting things out of PDFs, organizing information—all that stuff, I think, will get accelerated.",
         "AI will accelerate information processing",
         "muendlich", "https://stratechery.com/2023/an-interview-with-daniel-gross-and-nat-friedman-about-the-ai-hype-cycle/", "An Interview about the AI Hype Cycle - Stratechery",
         "2023-03-15", "en", "Discussing practical AI applications"),

        # 5
        (71, "Businesses that have product market fit in AI have gone from no revenue to tens in some cases hundreds of millions of ARR extremely quickly. In fact, so quickly that I always wonder, it's like an unhealthy kind of growth, but there's real thirst for it.",
         "AI businesses achieving unprecedented rapid growth",
         "muendlich", "https://stratechery.com/2023/an-interview-with-daniel-gross-and-nat-friedman-about-the-ai-hype-cycle/", "Interview about AI Hype Cycle - Stratechery",
         "2023-03-15", "en", "Observing the rapid growth of AI companies"),

        # 6
        (71, "We can talk about AI all day, but there are things happening outside of AI that are exciting and big.",
         "Technology innovation extends beyond AI",
         "muendlich", "https://stratechery.com/2023/an-interview-with-daniel-gross-and-nat-friedman-about-the-ai-hype-cycle/", "Stratechery Interview",
         "2023-03-15", "en", "Maintaining perspective on broader tech innovation"),

        # 7
        (71, "I expect miracles to follow.",
         "Expecting miraculous AI breakthroughs",
         "schriftlich", "https://www.calcalistech.com/ctechnews/article/4oj53t7pf", "I expect miracles - Ctech",
         "2025-07-03", "en", "Statement when leaving Safe Superintelligence Inc. to join Meta"),

        # 8
        (71, "Culture is very underrated and we need artists who can understand the direction of technology and craft narratives for the public.",
         "Need artists to communicate technology",
         "schriftlich", "https://twitter.com/danielgross", "Daniel Gross Twitter",
         "2018-06-15", "en", "On the importance of culture and narrative in technology"),

        # 9
        (71, "If you want to have better things in the world, generally speaking, they come from outsiders.",
         "Outsiders drive innovation",
         "muendlich", "https://mothfund.substack.com/p/mm-daniel-gross", "Moth Minds Interview",
         "2022-05-20", "en", "On finding and supporting overlooked talent"),

        # 10
        (71, "Everything in life is in some form of a video game, and all humans, regardless of IQ, are seeking novelty.",
         "Life as gamification seeking novelty",
         "muendlich", "https://mothfund.substack.com/p/mm-daniel-gross", "Moth Minds: Daniel Gross Interview",
         "2022-05-20", "en", "Philosophy on human motivation and gamification"),

        # 11
        (71, "The long-term goal is to create a decentralized AI research lab — think DeepMind but run through Slack and full of engineers that don't cost $300,000 a pop.",
         "Vision for decentralized AI research",
         "muendlich", "https://techcrunch.com/2017/07/25/ai-grant-aims-to-fund-the-unfundable-to-advance-ai-and-solve-hard-problems/", "TechCrunch: AI Grant aims to fund the unfundable",
         "2017-07-25", "en", "Explaining the vision behind AI Grant program"),

        # 12
        (71, "I think there are two possible takes on this. One is that we're just early and that's going to happen. And I think that's fairly true.",
         "Optimistic on independent AI companies emerging",
         "muendlich", "https://www.deciphr.ai/podcast/20vc-ycs-daniel-gross-on-how-yc-can-democratise-ai--reduce-incumbency-advantages-why-ml-enabled-software-will-eat-the-software-that-ate-the-world--whether-ai-will-produce-independent-companies-or-be-technology-within-incumbents", "20VC Interview on AI Companies",
         "2017-08-21", "en", "Discussing whether AI will produce independent companies"),

        # 13
        (71, "Someone who grew up in Jerusalem was able to build a search engine acquired by Apple.",
         "Geographic diversity enables innovation",
         "muendlich", "https://judgmentcallpodcast.com/2021/01/the-judgment-call-episode-12-daniel-gross-how-to-scale-entrepreneurship-and-applied-innovation-and-bring-it-to-the-world/", "The Judgment Call Podcast",
         "2021-01-15", "en", "Using himself as example for finding talent in overlooked populations"),

        # 14
        (71, "Invest in yourself, so that you can invest in others.",
         "Self-investment enables supporting others",
         "schriftlich", "https://mothfund.substack.com/p/mm-daniel-gross", "Moth Minds Interview",
         "2022-05-20", "en", "Core principle on personal development and supporting entrepreneurship"),

        # 15
        (71, "With deep fake video swapping becoming increasingly impressive, people can't trust everything they watch.",
         "Deep fakes threaten media trust",
         "schriftlich", "https://twitter.com/danielgross", "Daniel Gross on Twitter",
         "2018-09-10", "en", "Warning about the implications of deepfake technology"),

        # 16
        (71, "Online reading habits are changing the way people read in general, making it harder to read deeply into novels due to the habit of reading bite-sized posts.",
         "Digital media altering reading cognition",
         "schriftlich", "https://twitter.com/danielgross", "Twitter Statement",
         "2018-11-05", "en", "Observation on how digital media affects cognitive habits"),

        # 17
        (71, "As AI's impact in the business world grows, its proper use becomes more important.",
         "Responsible AI use increasingly critical",
         "schriftlich", "https://twitter.com/danielgross", "Daniel Gross Twitter",
         "2018-05-20", "en", "On the growing importance of ethical AI deployment"),

        # 18
        (71, "When evaluating a company, I consider whether the research idea makes sense as a good product, whether the person will be a good leader and able to recruit top talent, and whether the market structure supports the company in capturing the value it creates.",
         "Investment criteria: product, leadership, market",
         "muendlich", "https://mothfund.substack.com/p/mm-daniel-gross", "Moth Minds: Angel Investor & Entrepreneur",
         "2022-05-20", "en", "Explaining his framework for evaluating startup investments"),
    ]

    # HANDLUNGEN (Actions)
    handlungen = [
        # 1
        (71, "gruendung", "Co-founded Greplin (later renamed Cue), a personal search engine startup that indexed users' online data, at age 19",
         "2010-01-01", "https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)", "Wikipedia: Daniel Gross",
         "Launched Greplin along with Robby Walker as one of the youngest founders in Y Combinator"),

        # 2
        (71, "investition", "Received $4 million Series A investment from Sequoia Capital for Greplin, becoming one of Sequoia's youngest founders at age 19",
         "2011-03-01", "https://digidai.github.io/2025/11/28/daniel-gross-ai-pioneer-fund-jerusalem-to-meta-superintelligence-deep-analysis/", "Daniel Gross: AI Pioneer Fund & Meta",
         "Major validation from top-tier VC firm that had backed Apple, Google, YouTube, and Instagram"),

        # 3
        (71, "investition", "Raised $10 million from Index Ventures for Cue after rebranding from Greplin",
         "2012-11-01", "https://golden.com/wiki/Daniel_Gross_(entrepreneur)-63AKG86", "Golden: Daniel Gross",
         "Series B funding following company rebrand and launch of predictive search features"),

        # 4
        (71, "verkauf", "Sold Cue to Apple for $40-60 million and joined Apple as Director of Machine Learning",
         "2013-10-01", "https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)", "Wikipedia: Daniel Gross",
         "Apple acquired Cue for its AI-driven contextual search technology, integrating it into Siri and Spotlight"),

        # 5
        (71, "einstellung", "Joined Apple as Director leading artificial intelligence and machine learning initiatives across iOS, OS X, and other platforms",
         "2013-10-01", "https://9to5mac.com/2017/01/10/cue-co-founder-leaving-apple-y-combinator/", "9to5Mac: Cue co-founder leaving Apple",
         "Led AI and search projects at Apple from 2013-2017"),

        # 6
        (71, "ruecktritt", "Left Apple after four years to join Y Combinator as a partner",
         "2017-01-10", "https://techcrunch.com/2017/01/10/daniel-gross-of-apple-leaves-to-become-y-combinators-newest-partner/", "TechCrunch: Daniel Gross leaves Apple",
         "Moved from Apple to focus on AI democratization at Y Combinator"),

        # 7
        (71, "gruendung", "Founded AI Grant with Nat Friedman, a non-profit program providing $5,000-$50,000 grants to AI researchers and DIY enthusiasts",
         "2017-07-01", "https://techcrunch.com/2017/07/25/ai-grant-aims-to-fund-the-unfundable-to-advance-ai-and-solve-hard-problems/", "TechCrunch: AI Grant aims to fund the unfundable",
         "Created no-strings-attached grant program to fund unfundable AI research outside of large institutions"),

        # 8
        (71, "gruendung", "Founded Pioneer, an early-stage remote startup accelerator and fund finding talented people globally through online tournaments",
         "2018-08-01", "https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)", "Wikipedia: Daniel Gross",
         "Pioneered a new model of startup acceleration with continuous online tournaments, investing $20,000 for 5% equity plus 1%"),

        # 9
        (71, "investition", "Made early angel investments in Uber, Instacart, Figma, GitHub, Airtable, Rippling, and Coinbase",
         "2011-01-01", "https://en.wikipedia.org/wiki/Daniel_Gross_(businessman)", "Wikipedia: Daniel Gross",
         "Built portfolio of highly successful tech companies across diverse sectors, with over 90 angel investments by 2020"),

        # 10
        (71, "investition", "Participated in CoreWeave's $221 million Series B funding round alongside Nat Friedman and NVIDIA",
         "2023-04-20", "https://x.com/danielgross/status/1649113439917178892", "Daniel Gross Twitter Announcement",
         "Invested in GPU-focused cloud infrastructure company valued at $2 billion for AI workloads"),

        # 11
        (71, "gruendung", "Co-founded NFDG venture capital fund with Nat Friedman, raising $1.1 billion in committed capital focused on AI",
         "2023-01-01", "https://www.saastr.com/the-1-1b-vc-fund-that-4xd-in-two-years-then-got-acquired-by-meta/", "SaaStr: NFDG Fund Story",
         "Launched major AI-focused VC fund that achieved 4x returns in two years"),

        # 12
        (71, "gruendung", "Co-founded Safe Superintelligence Inc. with Ilya Sutskever and Daniel Levy as CEO",
         "2024-06-01", "https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.", "Wikipedia: Safe Superintelligence Inc.",
         "Founded AI safety company focused on safely developing superintelligent AI, headquartered in Palo Alto and Tel Aviv"),

        # 13
        (71, "ruecktritt", "Left Safe Superintelligence Inc. as CEO after 13 months to join Meta Superintelligence Labs",
         "2025-07-03", "https://www.calcalistech.com/ctechnews/article/4oj53t7pf", "Ctech: Gross joins Meta",
         "Departed SSI with statement 'I expect miracles to follow' to work on Meta's most ambitious AI projects"),

        # 14
        (71, "einstellung", "Joined Meta Superintelligence Labs to work on AI products and superintelligence development",
         "2025-07-03", "https://siliconangle.com/2025/07/03/safe-superintelligence-ceo-daniel-gross-joins-metas-new-ai-lab/", "SiliconANGLE: Daniel Gross joins Meta",
         "Meta hired Gross after failed attempt to acquire Safe Superintelligence, to lead AI superintelligence efforts"),

        # 15
        (71, "verkauf", "Meta acquired substantial portion of NFDG's holdings (potentially over $1 billion) while hiring Gross and Friedman",
         "2025-07-03", "https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/", "DCD: Meta acquires NFDG stake",
         "Meta partially acquired NFDG venture fund providing liquidity to LPs without gaining control over portfolio companies"),
    ]

    try:
        # Insert Aussagen
        print("Inserting Aussagen (Statements)...")
        cursor.executemany("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussagen)
        aussagen_count = len(aussagen)
        print(f"  [OK] Inserted {aussagen_count} statements")

        # Insert Handlungen
        print("Inserting Handlungen (Actions)...")
        cursor.executemany("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlungen)
        handlungen_count = len(handlungen)
        print(f"  [OK] Inserted {handlungen_count} actions")

        # Commit changes
        conn.commit()
        print("\n" + "="*60)
        print("SUCCESS: Data insertion completed")
        print("="*60)
        print(f"Total Aussagen inserted:  {aussagen_count}")
        print(f"Total Handlungen inserted: {handlungen_count}")
        print(f"GRAND TOTAL: {aussagen_count + handlungen_count} records")
        print("="*60)

    except sqlite3.Error as e:
        print(f"\nERROR during insertion: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    print("="*60)
    print("Daniel Gross (person_id=71) - Data Insertion Script")
    print("="*60)
    insert_data()
