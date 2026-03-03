#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dateneinfügung für Llion Jones (person_id=68)
Transformer Co-Author, Sakana AI Co-Founder
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 68

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # =============================================================================
    # AUSSAGEN (Statements)
    # =============================================================================

    aussagen = [
        # 1 - Transformers criticism
        (PERSON_ID,
         "It may sound a little controversial to hear one of the Transformers authors stand on stage and tell you that he's absolutely sick of them, but it's kind of fair enough, right?",
         "Absolutely sick of transformers",
         "muendlich",
         "https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers",
         "VentureBeat - Sakana AI's CTO says he's 'absolutely sick' of transformers",
         "2025-10-01",
         "en",
         "TED AI conference San Francisco 2025"),

        # 2 - Narrowing of research
        (PERSON_ID,
         "Despite the fact that there's never been so much interest and resources and money and talent, this has somehow caused the narrowing of the research that we're doing.",
         "Resources causing narrowing of research",
         "muendlich",
         "https://www.ted.com/talks/llion_jones_how_competition_is_stifling_ai_breakthroughs",
         "TED Talk - How competition is stifling AI breakthroughs",
         "2025-10-01",
         "en",
         "TED AI San Francisco 2025"),

        # 3 - Decision to reduce transformer work
        (PERSON_ID,
         "I personally made a decision in the beginning of this year that I'm going to drastically reduce the amount of time that I spend on transformers. I'm explicitly now exploring and looking for the next big thing.",
         "Reducing time on transformers to find next big thing",
         "schriftlich",
         "https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers",
         "VentureBeat - Sakana AI's CTO on transformers",
         "2025-01-01",
         "en",
         "Statement about 2025 research direction"),

        # 4 - Problem with transformer success
        (PERSON_ID,
         "The fact that the current technology is so powerful and flexible... stopped us from looking for better. It makes sense that if the current technology was worse, more people would be looking for better.",
         "Transformer success as obstacle to innovation",
         "muendlich",
         "https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers",
         "VentureBeat - Sakana AI's CTO on transformers",
         "2025-10-01",
         "en",
         "TED AI conference"),

        # 5 - Research philosophy at Sakana
        (PERSON_ID,
         "You should only do the research that wouldn't happen if you weren't doing it.",
         "Research mantra at Sakana AI",
         "schriftlich",
         "https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers",
         "VentureBeat - Sakana AI's CTO on transformers",
         "2024-08-01",
         "en",
         "Sakana AI research philosophy"),

        # 6 - Reverse engineering the mind
        (PERSON_ID,
         "Artificial Intelligence is just fascinating, from a scientific, philosophical and ethical view. I'm at the forefront of an effort to reverse engineer literally the most complex thing in the known universe: the human mind.",
         "AI as reverse engineering the human mind",
         "schriftlich",
         "https://www.hulkapps.com/blogs/ecommerce-hub/llion-jones-a-pioneer-in-ai-and-transformer-architecture",
         "HulkApps - Llion Jones: A Pioneer in AI and Transformer Architecture",
         "2019-01-01",
         "en",
         "Personal philosophy on AI research"),

        # 7 - Corporate pressure stifling innovation
        (PERSON_ID,
         "The immense amount of pressure from investors demanding returns and researchers scrambling to stand out in an overcrowded field.",
         "Investor pressure killing innovation",
         "muendlich",
         "https://www.ted.com/talks/llion_jones_how_competition_is_stifling_ai_breakthroughs",
         "TED Talk - How competition is stifling AI breakthroughs",
         "2025-10-01",
         "en",
         "Criticism of current AI industry dynamics"),

        # 8 - Fine-tuning may be wasted effort
        (PERSON_ID,
         "If I am right, then all those who are burying their heads in improving Transformer variants are wasting their time, and all mixture-of-experts models, all architecture fine-tunings, all attention mechanism variants—may become obsolete instantly when a new paradigm emerges.",
         "Fine-tuning transformers may be waste of time",
         "schriftlich",
         "https://eu.36kr.com/en/p/3643193251516297",
         "36Kr - Transformer's 'Father' Blasts: Current AI Reaches Dead End",
         "2025-10-01",
         "en",
         "Warning about current research direction"),

        # 9 - Google bureaucracy limitations
        (PERSON_ID,
         "Every day I would be spending my time trying to get access to resources, trying to get access to data. The bureaucracy had built to the point where I just felt like I couldn't get anything done.",
         "Google bureaucracy preventing productivity",
         "schriftlich",
         "https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html",
         "CNBC - Transformer co-author Llion Jones leaves Google for startup Sakana AI",
         "2023-08-17",
         "en",
         "Reasons for leaving Google"),

        # 10 - Japanese context understanding
        (PERSON_ID,
         "We want to build AI models that actually understand Japanese context.",
         "Building AI for Japanese context",
         "schriftlich",
         "https://www.hulkapps.com/blogs/ecommerce-hub/llion-jones-a-pioneer-in-ai-and-transformer-architecture",
         "Interview about Sakana AI vision",
         "2024-01-01",
         "en",
         "Sakana AI mission for Japan"),

        # 11 - Less KPIs, more curiosity
        (PERSON_ID,
         "Less KPIs, more curiosity; less following the trend, more natural inspiration.",
         "Research philosophy: curiosity over KPIs",
         "schriftlich",
         "https://eu.36kr.com/en/p/3526680165981315",
         "36Kr - Transformer's Father's Breakup Letter",
         "2025-10-01",
         "en",
         "Sakana AI research culture"),

        # 12 - Nature-inspired AI vision
        (PERSON_ID,
         "The idea behind it is applying swarm intelligence—where individual fish might not be very smart, but a school of fish can have emergent behavior—to AI research.",
         "Swarm intelligence approach to AI",
         "schriftlich",
         "https://geodesiccap.com/insight/introducing-sakana-the-future-of-foundation-models-inspired-by-adaptive-systems/",
         "Geodesic - Introducing Sakana: The Future of Foundation Models",
         "2023-08-01",
         "en",
         "Explanation of Sakana AI's biological inspiration"),

        # 13 - Company size limiting innovation
        (PERSON_ID,
         "While I have no ill will toward Google, I realized that the company's size was keeping me from doing the kind of work I wanted to pursue.",
         "Company size limiting research freedom",
         "schriftlich",
         "https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html",
         "CNBC - Transformer co-author Llion Jones leaves Google",
         "2023-08-17",
         "en",
         "Reflections on leaving Google"),

        # 14 - Corporate arms race killing innovation
        (PERSON_ID,
         "The industry that grew out of this breakthrough is stifling the next one. The current corporate arms race is killing true innovation.",
         "Corporate arms race stifling breakthroughs",
         "muendlich",
         "https://www.ted.com/talks/llion_jones_how_competition_is_stifling_ai_breakthroughs",
         "TED Talk - How competition is stifling AI breakthroughs",
         "2025-10-01",
         "en",
         "TED AI San Francisco 2025"),

        # 15 - AGI may need new architecture
        (PERSON_ID,
         "Countless current fine-tuning studies may only be local optimizations, and the real AGI breakthrough may lie in a brand-new biologically inspired architecture.",
         "AGI needs biologically inspired architecture",
         "schriftlich",
         "https://eu.36kr.com/en/p/3643193251516297",
         "36Kr - Transformer's 'Father' Blasts",
         "2025-10-01",
         "en",
         "Vision for AGI development"),

        # 16 - Transformer role in implementation
        (PERSON_ID,
         "I was responsible for the initial codebase, and handled efficient inference and visualizations.",
         "Initial transformer codebase responsibility",
         "schriftlich",
         "https://arxiv.org/abs/1706.03762",
         "Attention Is All You Need - ArXiv",
         "2017-06-12",
         "en",
         "Contribution to Attention Is All You Need paper"),

        # 17 - Nature-inspired models vision
        (PERSON_ID,
         "Rather than building one massive AI model, our goal is to have a large number of smaller models communicate and work together rather than creating one giant model.",
         "Many small models over one giant model",
         "schriftlich",
         "https://www.maginative.com/article/new-startup-sakana-ai-wants-to-build-nature-inspired-artificial-intelligence/",
         "Maginative - New Startup Sakana AI Wants To Build Nature-Inspired AI",
         "2023-08-17",
         "en",
         "Sakana AI architecture philosophy"),

        # 18 - Tokyo location choice
        (PERSON_ID,
         "We chose the city for Sakana AI due to the ready availability of researchers and technical infrastructure.",
         "Tokyo chosen for researchers and infrastructure",
         "schriftlich",
         "https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html",
         "CNBC - Transformer co-author leaves Google",
         "2023-08-17",
         "en",
         "Explanation for Tokyo headquarters"),

        # 19 - Educational background importance
        (PERSON_ID,
         "I credit my good Computer Science school background on my CV as a key reason I was able to get into Google without having a referral.",
         "CS education key to Google entry",
         "schriftlich",
         "https://www.birmingham.ac.uk/study/student-experience/meet-our-students/llion-jones",
         "University of Birmingham - Alumni Llion Jones",
         "2018-01-01",
         "en",
         "Reflection on career path"),
    ]

    # =============================================================================
    # HANDLUNGEN (Actions)
    # =============================================================================

    handlungen = [
        # 1 - Co-founding Sakana AI
        (PERSON_ID,
         "gruendung",
         "Co-founded Sakana AI in Tokyo with David Ha and Ren Ito, a nature-inspired AI research company focused on evolutionary and collective intelligence approaches",
         "2023-08-01",
         "https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html",
         "CNBC - Transformer co-author Llion Jones leaves Google for startup Sakana AI",
         "Left Google after almost 12 years to co-found startup in Tokyo"),

        # 2 - Leaving Google
        (PERSON_ID,
         "ruecktritt",
         "Left Google after almost 12 years as senior software engineer and researcher at Google Brain",
         "2023-08-01",
         "https://www.cnbc.com/2023/08/17/transformer-co-author-llion-jones-leaves-google-for-startup-sakana-ai.html",
         "CNBC - Transformer co-author leaves Google",
         "Cited bureaucracy and resource access limitations as reasons"),

        # 3 - Seed funding round
        (PERSON_ID,
         "investition",
         "Sakana AI raised $30M seed funding from Lux Capital and Khosla Ventures",
         "2024-03-01",
         "https://sakana.ai/seed-round/",
         "Sakana AI - We raised $30M to develop nature-inspired AI in Japan",
         "Initial seed round to develop nature-inspired AI"),

        # 4 - Series A funding
        (PERSON_ID,
         "investition",
         "Sakana AI raised approximately $200M Series A at $1.5B valuation from Mitsubishi UFJ, SMBC, Mizuho, Itochu, KDDI, Nomura and Nvidia",
         "2024-09-01",
         "https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/",
         "TechCrunch - Sakana AI raises Series B",
         "Major Series A round with Japanese financial institutions and Nvidia"),

        # 5 - Series B funding
        (PERSON_ID,
         "investition",
         "Sakana AI raised $135M Series B at $2.65B post-money valuation from MUFG, Khosla Ventures, Macquarie Capital, NEA, Lux Capital, and In-Q-Tel",
         "2025-11-17",
         "https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/",
         "TechCrunch - Sakana AI raises $135M Series B at $2.65B valuation",
         "Series B funding making Sakana AI most valuable Japanese AI unicorn"),

        # 6 - Evolutionary Model Merge launch
        (PERSON_ID,
         "produktlaunch",
         "Launched 'Evolutionary Model Merge' - a general method using evolutionary techniques to combine different open-source models",
         "2024-03-21",
         "https://sakana.ai/evolutionary-model-merge/",
         "Sakana AI - Evolving New Foundation Models",
         "First major research product demonstrating nature-inspired AI approach"),

        # 7 - AI Scientist launch
        (PERSON_ID,
         "produktlaunch",
         "Launched 'The AI Scientist' - first comprehensive system for fully automatic scientific discovery, automating entire research lifecycle at ~$15 per paper",
         "2024-08-13",
         "https://sakana.ai/ai-scientist/",
         "Sakana AI - The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery",
         "Collaboration with University of Oxford and University of British Columbia"),

        # 8 - Nature Machine Intelligence publication
        (PERSON_ID,
         "produktlaunch",
         "Paper 'Evolutionary Optimization of Model Merging Recipes' accepted to Nature Machine Intelligence",
         "2025-01-27",
         "https://www.nature.com/articles/s42256-024-00975-8",
         "Nature Machine Intelligence - Evolutionary optimization of model merging recipes",
         "Major academic publication validating Sakana AI's approach"),

        # 9 - Partnership with Oxford
        (PERSON_ID,
         "partnerschaft",
         "Established research collaboration with Foerster Lab for AI Research at University of Oxford for AI Scientist development",
         "2024-08-01",
         "https://sakana.ai/ai-scientist/",
         "Sakana AI - The AI Scientist announcement",
         "Academic partnership for automated scientific discovery research"),

        # 10 - Partnership with UBC
        (PERSON_ID,
         "partnerschaft",
         "Established research collaboration with Jeff Clune and Cong Lu at University of British Columbia for AI Scientist development",
         "2024-08-01",
         "https://sakana.ai/ai-scientist/",
         "Sakana AI - The AI Scientist announcement",
         "Academic partnership for automated research system"),

        # 11 - TED Talk presentation
        (PERSON_ID,
         "sonstiges",
         "Delivered TED Talk 'How competition is stifling AI breakthroughs' at TED AI San Francisco 2025",
         "2025-10-23",
         "https://www.ted.com/talks/llion_jones_how_competition_is_stifling_ai_breakthroughs",
         "TED - Llion Jones: How competition is stifling AI breakthroughs",
         "Public presentation criticizing current AI research dynamics"),

        # 12 - Joining YouTube/Google
        (PERSON_ID,
         "einstellung",
         "Joined YouTube as software engineer",
         "2012-02-01",
         "https://www.hulkapps.com/blogs/ecommerce-hub/llion-jones-a-pioneer-in-ai-and-transformer-architecture",
         "HulkApps - Llion Jones career history",
         "Initial entry into Google ecosystem"),

        # 13 - Transfer to Google Research
        (PERSON_ID,
         "umstrukturierung",
         "Transferred from YouTube to Google Research/Google Brain as senior software engineer",
         "2015-06-01",
         "https://www.hulkapps.com/blogs/ecommerce-hub/llion-jones-a-pioneer-in-ai-and-transformer-architecture",
         "HulkApps - Llion Jones career history",
         "Career shift from software engineering to AI research"),

        # 14 - Attention Is All You Need publication
        (PERSON_ID,
         "produktlaunch",
         "Co-authored seminal paper 'Attention Is All You Need' introducing the Transformer architecture with 7 other equal contributors",
         "2017-06-12",
         "https://arxiv.org/abs/1706.03762",
         "ArXiv - Attention Is All You Need",
         "Groundbreaking paper that became foundation of modern AI"),

        # 15 - AI Scientist v2 launch
        (PERSON_ID,
         "produktlaunch",
         "Launched AI Scientist-v2 producing first entirely AI-generated peer-review-accepted workshop paper",
         "2025-04-01",
         "https://github.com/SakanaAI/AI-Scientist-v2",
         "GitHub - SakanaAI/AI-Scientist-v2",
         "Enhanced version achieving workshop-level automated scientific discovery"),
    ]

    # Insert aussagen
    aussagen_count = 0
    for aussage in aussagen:
        try:
            cursor.execute("""
                INSERT INTO aussagen
                (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, aussage)
            aussagen_count += 1
        except Exception as e:
            print(f"Fehler bei Aussage: {e}")
            print(f"Aussage: {aussage[1][:50]}...")

    # Insert handlungen
    handlungen_count = 0
    for handlung in handlungen:
        try:
            cursor.execute("""
                INSERT INTO handlungen
                (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, handlung)
            handlungen_count += 1
        except Exception as e:
            print(f"Fehler bei Handlung: {e}")
            print(f"Handlung: {handlung[2][:50]}...")

    conn.commit()
    conn.close()

    print(f"\n{'='*70}")
    print(f"DATENEINFÜGUNG ABGESCHLOSSEN - Llion Jones (person_id={PERSON_ID})")
    print(f"{'='*70}")
    print(f"Aussagen eingefügt:   {aussagen_count}")
    print(f"Handlungen eingefügt: {handlungen_count}")
    print(f"Gesamt eingefügt:     {aussagen_count + handlungen_count}")
    print(f"{'='*70}\n")

    return aussagen_count, handlungen_count

if __name__ == "__main__":
    insert_data()
