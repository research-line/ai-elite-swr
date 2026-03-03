# -*- coding: utf-8 -*-
"""
Insert data for Edwin Chen (person_id=96) into aussagen_top100.db
Data collected from web research on 2026-02-12
"""

import sqlite3
from datetime import datetime

# Database path
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Inserting data for Edwin Chen (person_id=96)...")

# ============================================================================
# AUSSAGEN (STATEMENTS)
# ============================================================================

aussagen = [
    # 1 - AI capabilities and data quality
    (96, "AI is capable of Nobel Prize-winning poetry, solving the Riemann hypothesis, and discovering the secrets of the universe—but only if it's trained on data that captures human expertise, creativity, and values.",
     "AI capable of Nobel-level work with quality data", "schriftlich",
     "https://time.com/collections/time100-ai-2025/7305876/edwin-chen/",
     "Edwin Chen: The 100 Most Influential People in AI 2025 | TIME",
     None, "en", "TIME 100 AI 2025 profile"),

    # 2 - Data labeling philosophy
    (96, "I've always hated the word data labeling because it just paints this very simplistic picture when I think what we're doing is completely different. You don't just feed a child information. You're teaching them values, and creativity, and what's beautiful, and these infinite subtle things about what makes somebody a good person.",
     "Data labeling is like raising a child", "schriftlich",
     "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "2025-12-07", "en", "Lenny's Podcast interview"),

    # 3 - Human vs machine analogy
    (96, "You could ask a 10-year-old and you could ask Hemingway to draw a bounding box around a car... But if you were saying like, write me a poem of a moon that makes me cry, like I would expect Hemingway to be better than a 10-year-old.",
     "Complex tasks require expertise like Hemingway", "schriftlich",
     "https://datainnovation.org/2022/09/5-qs-for-edwin-chen-ceo-of-surge-ai/",
     "5 Q's for Edwin Chen, CEO of Surge AI – Center for Data Innovation",
     "2022-09", "en", "Interview on data labeling quality"),

    # 4 - AI models and data quality
    (96, "AI models are only as good as the data that you feed them. If you feed your models poor data, then they'll mimic the bad data and give inaccurate predictions.",
     "AI models mirror their training data quality", "schriftlich",
     "https://polygonhealthanalytics.com/edwin-chen-and-surge-ai/",
     "Powerful AI Starts with High-Quality Data",
     None, "en", "Discussion on data quality fundamentals"),

    # 5 - Data quality as top constraint
    (96, "Without clean, contextual, high-quality training data, even the best models underperform. Data quality is the #1 constraint in AI today.",
     "Data quality is #1 AI constraint", "schriftlich",
     "https://www.todayin-ai.com/p/surgeai",
     "Surge AI: The $24B Data Engine Teaching AGI Real Human Taste",
     None, "en", "Analysis of Surge AI's approach"),

    # 6 - Quality vs quantity
    (96, "In many cases, a few thousand well-labeled human examples outperform millions of synthetic ones.",
     "Quality beats quantity in data labeling", "schriftlich",
     "https://westoperators.com/blog/surge-ai-case-study",
     "Surge AI built a $25B company on philosophy while competitors sold features | West Operators",
     None, "en", "Case study on business philosophy"),

    # 7 - Vision for AI warmth
    (96, "I don't want AI to be this cold robotic thing that solves a bunch of math questions. I want it to feel rich and warm and creative, capable of interacting in an inherently human way.",
     "AI should be warm and creative, not cold", "schriftlich",
     "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "2025-12-07", "en", "Lenny's Podcast interview on AI vision"),

    # 8 - AGI timeline
    (96, "We're still a decade away from AGI.",
     "AGI is a decade away", "schriftlich",
     "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "2025-12-07", "en", "Lenny's Podcast interview"),

    # 9 - AGI concerns
    (96, "If AGI is realized, it will be significantly more powerful than today's algorithmic platforms while infiltrating every part of society, with almost an infinite potential for unintended consequences.",
     "AGI has infinite potential for unintended consequences", "schriftlich",
     "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "2025-12-07", "en", "Discussion on AGI risks"),

    # 10 - Human feedback permanence
    (96, "I'm skeptical that AI will reach a point where human feedback is no longer needed. Annotation becomes more difficult as models improve.",
     "AI will always need human feedback", "schriftlich",
     "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "2025-12-07", "en", "On future of human involvement in AI"),

    # 11 - Synthetic data philosophy
    (96, "We're not competing with synthetic data. We are the quality control layer that makes synthetic data usable. As AI generates more training data, Surge's humans verify quality in a recursive loop of human-AI collaboration.",
     "Humans are quality control for synthetic data", "schriftlich",
     "https://getlatka.com/blog/surgeai-revenue-valuation/",
     "How Edwin Chen Bootstrapped Surge AI to $1.2 Billion Revenue",
     None, "en", "On relationship between human and synthetic data"),

    # 12 - Silicon Valley criticism
    (96, "One of the reasons we self-financed is that I've always hated the status quo in Silicon Valley. I hate the idea of raising a large amount of money and then having to spend it. Typical VC-backed Silicon Valley startups are get-rich-quick schemes.",
     "VC-backed startups are get-rich-quick schemes", "schriftlich",
     "https://eu.36kr.com/en/p/3502837065586825",
     "37-Year-Old Genius Chinese-American Becomes the 'Youngest Billionaire'",
     None, "en", "Criticism of venture capital culture"),

    # 13 - VC bureaucracy
    (96, "You move slow. You have a lot of politics. You have a lot of bureaucracy.",
     "VC money creates politics and bureaucracy", "schriftlich",
     "https://www.antoinebuteau.com/lessons-from-edwin-chen-of-surge-ai/",
     "Lessons from Edwin Chen of Surge AI",
     None, "en", "On why he avoided venture capital"),

    # 14 - Escaping Silicon Valley groupthink
    (96, "I'm glad I'm not surrounded by the default ways of Silicon Valley thinking.",
     "Glad to escape Silicon Valley default thinking", "schriftlich",
     "https://www.antoinebuteau.com/lessons-from-edwin-chen-of-surge-ai/",
     "Lessons from Edwin Chen of Surge AI",
     None, "en", "On independent thinking"),

    # 15 - Industry direction criticism
    (96, "The industry is moving in the wrong direction due to a broader pattern of style over substance.",
     "AI industry prioritizes style over substance", "schriftlich",
     "https://westoperators.com/blog/surge-ai-case-study",
     "Surge AI built a $25B company on philosophy while competitors sold features | West Operators",
     None, "en", "Criticism of industry trends"),

    # 16 - Product quality over sales
    (96, "Sales teams optimize for closing deals, not solving problems.",
     "Sales teams don't solve problems", "schriftlich",
     "https://ainativegtm.substack.com/p/1b-arr-zero-vc-funding-no-sales-team",
     "$1B ARR, Zero VC Funding, No Sales Team, 110 Employees: The Surge AI story",
     None, "en", "On why Surge has no sales team"),

    # 17 - Organic growth philosophy
    (96, "Be so good that customers can't function without you. We'll get calls from new customers saying, 'We hired someone from [major AI lab] and they said we need to get Surge AI here or we're not doing anything.' That's exactly the kind of organic growth we want—driven by people who've seen firsthand what a difference quality data makes.",
     "Be so good customers can't function without you", "schriftlich",
     "https://henrythe9th.substack.com/p/how-edwin-chen-built-a-1b-arr-ai-fde",
     "How Edwin Chen Built a $1B+ ARR AI Company in 5 years without any Investors",
     None, "en", "On organic growth strategy"),

    # 18 - AI safety current concern
    (96, "AI safety is not a future concern. Misaligned objectives—like optimizing for engagement over truth—are already causing harm.",
     "AI misalignment already causes harm today", "schriftlich",
     "https://polygonhealthanalytics.com/edwin-chen-and-surge-ai/",
     "Powerful AI Starts with High-Quality Data",
     None, "en", "On current AI safety issues"),

    # 19 - Previous platforms harm
    (96, "I've seen firsthand how products designed to optimize for clicks can cause harm.",
     "Click-optimization products cause harm", "schriftlich",
     "https://time.com/collections/time100-ai-2025/7305876/edwin-chen/",
     "Edwin Chen: The 100 Most Influential People in AI 2025 | TIME",
     None, "en", "Reflecting on experience at Facebook and Twitter"),

    # 20 - Engineer-first approach
    (96, "I advocate for versatile engineers to maintain agility and focus on building. I'm skeptical about hiring too many specialized PMs or non-engineering roles early on, preferring tight product feedback loops driven by engineers.",
     "Engineers first, not specialized PMs early", "schriftlich",
     "https://www.webpronews.com/surge-ai-ceo-skip-early-pms-hire-versatile-engineers-for-growth/",
     "Surge AI CEO: Skip Early PMs, Hire Versatile Engineers for Growth",
     None, "en", "On team building philosophy"),
]

# Insert aussagen
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)

print(f"Inserted {len(aussagen)} aussagen")

# ============================================================================
# HANDLUNGEN (ACTIONS)
# ============================================================================

handlungen = [
    # 1 - Founded Surge AI
    (96, "gruendung", "Founded Surge AI with $300,000 from personal savings, bootstrapping the company without any venture capital. Started from San Francisco apartment.",
     "2020-05", "https://en.wikipedia.org/wiki/Surge_AI", "Surge AI - Wikipedia",
     "Left Facebook to found data labeling company focused on quality over quantity"),

    # 2 - Quit seven-figure job
    (96, "ruecktritt", "Quit seven-figure salary job to found Surge AI, turning down lucrative Big Tech compensation.",
     "2020-05", "https://wshreport.com/edwin-chen-surge-ai/",
     "Chinese-American Entrepreneur Edwin Chen Joins Forbes Billionaires List with $18 Billion Fortune",
     "Made bold move to leave stable, high-paying position"),

    # 3 - Reached $1B revenue
    (96, "sonstiges", "Surge AI surpassed $1 billion in annual revenue with under 100 employees, completely bootstrapped—the fastest company in history to reach this milestone.",
     "2024", "https://time.com/collections/time100-ai-2025/7305876/edwin-chen/",
     "Edwin Chen: The 100 Most Influential People in AI 2025 | TIME",
     "Unprecedented growth rate without external funding"),

    # 4 - Partnership with OpenAI
    (96, "partnerschaft", "Established partnership with OpenAI as major client for data labeling and RLHF services.",
     "2020", "https://en.wikipedia.org/wiki/Surge_AI", "Surge AI - Wikipedia",
     "Became key data provider for leading AI lab"),

    # 5 - Partnership with Anthropic
    (96, "partnerschaft", "Established partnership with Anthropic as major client, contributing to Claude's training and evaluation.",
     "2020", "https://www.lennysnewsletter.com/p/surge-ai-edwin-chen",
     "The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI)",
     "Became secret weapon for Anthropic's AI development"),

    # 6 - Partnership with Google
    (96, "partnerschaft", "Established partnership with Google as major client for AI training data.",
     "2020", "https://wshreport.com/edwin-chen-surge-ai/",
     "Chinese-American Entrepreneur Edwin Chen Joins Forbes Billionaires List with $18 Billion Fortune",
     "Won contract with former employer"),

    # 7 - Partnership with Meta
    (96, "partnerschaft", "Established partnership with Meta (Facebook) as major client for AI training data.",
     "2020", "https://wshreport.com/edwin-chen-surge-ai/",
     "Chinese-American Entrepreneur Edwin Chen Joins Forbes Billionaires List with $18 Billion Fortune",
     "Won contract with former employer"),

    # 8 - Partnership with Microsoft
    (96, "partnerschaft", "Established partnership with Microsoft as major client for AI training data.",
     "2020", "https://wshreport.com/edwin-chen-surge-ai/",
     "Chinese-American Entrepreneur Edwin Chen Joins Forbes Billionaires List with $18 Billion Fortune",
     "Expanded client base to major tech companies"),

    # 9 - Built contractor network
    (96, "sonstiges", "Built network of over 1 million contractors across 50+ countries, including professors from Stanford, Princeton, and Harvard, medical doctors, lawyers, and PhD researchers.",
     "2020-2024", "https://time.com/collections/time100-ai-2025/7305876/edwin-chen/",
     "Edwin Chen: The 100 Most Influential People in AI 2025 | TIME",
     "Created global expert network for high-quality data annotation"),

    # 10 - Rejected venture capital
    (96, "sonstiges", "Explicitly rejected venture capital offers, maintaining 100% bootstrapped status despite achieving $1B+ revenue.",
     "2020-2025", "https://ainativegtm.substack.com/p/1b-arr-zero-vc-funding-no-sales-team",
     "$1B ARR, Zero VC Funding, No Sales Team, 110 Employees: The Surge AI story",
     "Maintained independence and control by avoiding VC funding"),

    # 11 - TIME 100 AI recognition
    (96, "sonstiges", "Named to TIME 100 Most Influential People in AI 2025 list.",
     "2025", "https://time.com/collections/time100-ai-2025/7305876/edwin-chen/",
     "Edwin Chen: The 100 Most Influential People in AI 2025 | TIME",
     "Recognition as influential AI industry figure"),

    # 12 - Forbes 400 youngest member
    (96, "sonstiges", "Became youngest person on Forbes 400 list of richest Americans at age 37 with $18 billion net worth.",
     "2025", "https://e.vnexpress.net/news/tech/personalities/meet-edwin-chen-mit-graduate-and-youngest-billionaire-on-forbes-400-richest-americans-list-4938703.html",
     "Meet Edwin Chen, MIT graduate and youngest billionaire on Forbes' 400 richest Americans list",
     "Achieved youngest billionaire status through bootstrapped company"),

    # 13 - Preparation for Series A
    (96, "sonstiges", "Reportedly preparing $1 billion Series A funding round at $24-25 billion valuation after years of bootstrapping.",
     "2025-07", "https://theaiinsider.tech/2025/07/03/surge-ai-prepares-1b-capital-raise-as-demand-for-premium-ai-training-data-surges/",
     "Surge AI Prepares $1B Capital Raise as Demand for Premium AI Training Data Surges",
     "First external funding after proving business model"),

    # 14 - Capitalized on Scale AI-Meta deal
    (96, "sonstiges", "Gained significant market share after Meta's $14.3B investment in competitor Scale AI, as clients worried about data sharing with competitors. Gained more revenue in one week than previous six months.",
     "2025-06", "https://henrythe9th.substack.com/p/how-edwin-chen-built-a-1b-arr-ai-fde",
     "How Edwin Chen Built a $1B+ ARR AI Company in 5 years without any Investors",
     "Competitor's deal became Surge's growth catalyst"),

    # 15 - No sales/marketing structure
    (96, "umstrukturierung", "Built company to $1B revenue with zero sales team, zero marketing team, relying entirely on word-of-mouth and product quality.",
     "2020-2024", "https://ainativegtm.substack.com/p/1b-arr-zero-vc-funding-no-sales-team",
     "$1B ARR, Zero VC Funding, No Sales Team, 110 Employees: The Surge AI story",
     "Unconventional go-to-market strategy"),
]

# Insert handlungen
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)

print(f"Inserted {len(handlungen)} handlungen")

# Commit and close
conn.commit()
conn.close()

print("\n" + "="*60)
print(f"SUMMARY FOR EDWIN CHEN (person_id=96)")
print("="*60)
print(f"Total Aussagen inserted: {len(aussagen)}")
print(f"Total Handlungen inserted: {len(handlungen)}")
print(f"Total records: {len(aussagen) + len(handlungen)}")
print("="*60)
print("Data insertion completed successfully!")
