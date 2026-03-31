import sqlite3
from datetime import datetime

# Database connection
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 74  # Brendan Foody

# AUSSAGEN
aussagen = [
    {
        'aussage_text': "We work a lot, I've worked every day for the last three years.",
        'aussage_kurz': "Worked every day for three years",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/29/self-made-billionaire-artifical-intelligence-brendan-foody-mercor-silcion-valley-startup-founders-technology/",
        'quell_titel': "Fortune - The world's youngest self-made billionaire hasn't taken a day off in 3 years",
        'datum_aussage': "2025-11-29",
        'sprache': "en",
        'kontext': "On work ethic and habits that brought him to billionaire status at age 22"
    },
    {
        'aussage_text': "People generally burn out, not just from working hard, but from working hard on something that they don't feel as fulfilling and compounding.",
        'aussage_kurz': "Burnout comes from unfulfilling work",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/29/self-made-billionaire-artifical-intelligence-brendan-foody-mercor-silcion-valley-startup-founders-technology/",
        'quell_titel': "Fortune - The world's youngest self-made billionaire hasn't taken a day off in 3 years",
        'datum_aussage': "2025-11-29",
        'sprache': "en",
        'kontext': "Explaining his perspective on burnout and work-life balance"
    },
    {
        'aussage_text': "I can't really take a day off, because I just have this impulsive drive to go back to it. So I think that people finding the thing that they're obsessed with and can really pour their lives into, is one of the most important things.",
        'aussage_kurz': "Find work you're obsessed with",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/29/self-made-billionaire-artifical-intelligence-brendan-foody-mercor-silcion-valley-startup-founders-technology/",
        'quell_titel': "Fortune - The world's youngest self-made billionaire hasn't taken a day off in 3 years",
        'datum_aussage': "2025-11-29",
        'sprache': "en",
        'kontext': "On finding meaningful work and obsession as driver for success"
    },
    {
        'aussage_text': "We'll automate maybe two-thirds of knowledge work. And that'll be incredible, because it lets us do things like cure cancer and go to Mars.",
        'aussage_kurz': "Two-thirds of knowledge work will be automated",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "On the future of AI automation and its impact on knowledge work"
    },
    {
        'aussage_text': "In the next five years, AI could automate 50 percent of the tasks that people do today. That will be extremely exciting to see play out.",
        'aussage_kurz': "50% of tasks automated in 5 years",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "Predicting the pace of AI-driven automation"
    },
    {
        'aussage_text': "Everyone's been focused on what models can do. But the real opportunity is teaching them what only humans know—judgment, nuance, and taste.",
        'aussage_kurz': "AI needs to learn human judgment and nuance",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "On the core value proposition of Mercor - teaching AI human qualities"
    },
    {
        'aussage_text': "The challenge now is to be thoughtful about what comes next: the higher, better things humans will spend time on, and how quickly we can help make that future real.",
        'aussage_kurz': "Humans will move to higher value work",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "On the future of human work in an AI-automated economy"
    },
    {
        'aussage_text': "Millions of people will spend the next decade teaching machines the judgment, nuance, and taste that only humans possess.",
        'aussage_kurz': "Millions will teach AI human qualities",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "On the emerging labor market for AI training and evaluation"
    },
    {
        'aussage_text': "I knew I wanted to drop out before finals my sophomore year. I just didn't go to finals.",
        'aussage_kurz': "Dropped out without taking finals",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "On his decision to drop out of Georgetown University"
    },
    {
        'aussage_text': "It's like we have this bottleneck of only so much human labor in the economy. That shape is going to change radically over the next decade.",
        'aussage_kurz': "Human labor bottleneck will change radically",
        'modus': "muendlich",
        'quell_link': "https://sfstandard.com/2025/11/07/san-francisco-s-youngest-billionaires-betting-new-kind-job-boom/",
        'quell_titel': "San Francisco Standard - San Francisco's youngest billionaires are betting on a new kind of job boom",
        'datum_aussage': "2025-11-07",
        'sprache': "en",
        'kontext': "On the transformation of labor markets through AI"
    },
    {
        'aussage_text': "I think always making sure that I see the impact of what I do, the ROI of putting in a huge amount of time is most important.",
        'aussage_kurz': "Focus on seeing impact and ROI of work",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/29/self-made-billionaire-artifical-intelligence-brendan-foody-mercor-silcion-valley-startup-founders-technology/",
        'quell_titel': "Fortune - The world's youngest self-made billionaire hasn't taken a day off in 3 years",
        'datum_aussage': "2025-11-29",
        'sprache': "en",
        'kontext': "On what keeps him motivated and prevents burnout"
    },
    {
        'aussage_text': "Find the problem you can't stop thinking about—obsession beats discipline when building for the long haul.",
        'aussage_kurz': "Obsession beats discipline",
        'modus': "muendlich",
        'quell_link': "https://www.notion.com/blog/first-block-with-brendan-foody",
        'quell_titel': "Notion First Block Interview with Brendan Foody",
        'datum_aussage': "2025-01-01",
        'sprache': "en",
        'kontext': "Advice to entrepreneurs from Notion First Block interview"
    },
    {
        'aussage_text': "Hire with the highest possible bar for your first 10 people. Those early hires will shape your next hundred employees and are the most important decisions you'll make while scaling.",
        'aussage_kurz': "First 10 hires are most critical",
        'modus': "muendlich",
        'quell_link': "https://www.notion.com/blog/first-block-with-brendan-foody",
        'quell_titel': "Notion First Block Interview with Brendan Foody",
        'datum_aussage': "2025-01-01",
        'sprache': "en",
        'kontext': "Advice on hiring and scaling companies"
    },
    {
        'aussage_text': "Now is the most exciting time in history to build a company. The gap between what's possible with AI and what's been actualized in the economy is enormous—if there's ever a time to bet on yourself, it's now.",
        'aussage_kurz': "Now is best time to build AI company",
        'modus': "muendlich",
        'quell_link': "https://www.notion.com/blog/first-block-with-brendan-foody",
        'quell_titel': "Notion First Block Interview with Brendan Foody",
        'datum_aussage': "2025-01-01",
        'sprache': "en",
        'kontext': "On the current opportunity in AI entrepreneurship"
    },
    {
        'aussage_text': "When I was in college, work was something I had to be disciplined to do.",
        'aussage_kurz': "College work required discipline, not passion",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'datum_aussage': "2025-11-12",
        'sprache': "en",
        'kontext': "Contrasting college work with entrepreneurial passion"
    },
    {
        'aussage_text': "Mercor is training models that predict how well someone will perform on a job better than a human can.",
        'aussage_kurz': "AI predicts job performance better than humans",
        'modus': "muendlich",
        'quell_link': "https://conversationswithtyler.com/episodes/brendan-foody/",
        'quell_titel': "Conversations with Tyler - Episode 267 with Brendan Foody",
        'datum_aussage': "2025-10-16",
        'sprache': "en",
        'kontext': "On Mercor's AI capabilities in talent assessment"
    },
    {
        'aussage_text': "As software automates repetitive white-collar tasks, humans will move up the value chain, teaching machines how to reason, decide, and create.",
        'aussage_kurz': "Humans will teach machines higher-order skills",
        'modus': "muendlich",
        'quell_link': "https://conversationswithtyler.com/episodes/brendan-foody/",
        'quell_titel': "Conversations with Tyler - Episode 267 with Brendan Foody",
        'datum_aussage': "2025-10-16",
        'sprache': "en",
        'kontext': "On the evolving relationship between human labor and AI"
    },
    {
        'aussage_text': "Versus when I started Mercor, it really became this feeling of obsession that I can't stop thinking about, even if I'm getting dinner with my parents or whatever, it's going through the back of my head.",
        'aussage_kurz': "Mercor became an obsession",
        'modus': "muendlich",
        'quell_link': "https://fortune.com/2025/11/29/self-made-billionaire-artifical-intelligence-brendan-foody-mercor-silcion-valley-startup-founders-technology/",
        'quell_titel': "Fortune - The world's youngest self-made billionaire hasn't taken a day off in 3 years",
        'datum_aussage': "2025-11-29",
        'sprache': "en",
        'kontext': "Describing his passion and obsession with building Mercor"
    }
]

# HANDLUNGEN
handlungen = [
    {
        'handlung_typ': "gruendung",
        'beschreibung': "Co-founded Mercor with Adarsh Hiremath and Surya Midha, an AI-powered recruiting platform that evolved into an AI training marketplace",
        'datum_handlung': "2023-01-01",
        'quell_link': "https://www.mercor.com/blog/1/",
        'quell_titel': "Mercor Blog - Introducing Mercor",
        'kontext': "Founded in January 2023 by three college dropouts from Georgetown and Harvard"
    },
    {
        'handlung_typ': "ruecktritt",
        'beschreibung': "Dropped out of Georgetown University during sophomore year to focus on Mercor, skipping final exams",
        'datum_handlung': "2023-05-01",
        'quell_link': "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        'quell_titel': "Fortune - Meet the world's youngest self-made billionaire",
        'kontext': "Received Thiel Fellowship and dropped out during sophomore year in 2023"
    },
    {
        'handlung_typ': "spende",
        'beschreibung': "Received $100,000 Thiel Fellowship grant after being selected as Thiel Fellow",
        'datum_handlung': "2024-03-01",
        'quell_link': "https://www.thecrimson.com/article/2024/3/27/thiel-fellowship-startups-2024/",
        'quell_titel': "Harvard Crimson - Five Harvard Students Just Won $100,000 From Peter Thiel",
        'kontext': "Awarded Thiel Fellowship in March 2024, requiring college dropout commitment"
    },
    {
        'handlung_typ': "investition",
        'beschreibung': "Raised $3.6 million seed funding led by General Catalyst",
        'datum_handlung': "2023-09-01",
        'quell_link': "https://pulse2.com/mercor-3-6-million-in-funding-raised-to-launch-fully-automated-platform/",
        'quell_titel': "Pulse 2.0 - Mercor: $3.6 Million In Funding Raised",
        'kontext': "Seed round to launch fully automated hiring platform"
    },
    {
        'handlung_typ': "investition",
        'beschreibung': "Raised $30-32 million Series A funding led by Benchmark (Victor Lazarte and Bill Gurley) at $250 million valuation, with participation from Peter Thiel, Jack Dorsey, Larry Summers, Adam D'Angelo, and Chris Re",
        'datum_handlung': "2024-09-01",
        'quell_link': "https://techstartups.com/2024/09/18/ai-powered-hiring-platform-startup-mercor-raises-30m-in-series-a-funding-led-by-benchmark/",
        'quell_titel': "Tech Startups - Mercor raises $30M in Series A funding led by Benchmark",
        'kontext': "Series A round with high-profile Silicon Valley investors"
    },
    {
        'handlung_typ': "investition",
        'beschreibung': "Raised $100 million Series B funding led by Felicis at $2 billion valuation",
        'datum_handlung': "2025-02-20",
        'quell_link': "https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/",
        'quell_titel': "TechCrunch - Mercor raises $100M at $2B valuation",
        'kontext': "Series B round quintupling valuation from Series A"
    },
    {
        'handlung_typ': "investition",
        'beschreibung': "Raised $350 million Series C funding led by Felicis Ventures with participation from Benchmark, General Catalyst, and Robinhood Ventures at $10 billion valuation",
        'datum_handlung': "2025-10-27",
        'quell_link': "https://www.cnbc.com/2025/10/27/ai-hiring-startup-mercor-funding.html",
        'quell_titel': "CNBC - AI startup Mercor now valued at $10 billion",
        'kontext': "Series C round making founders youngest self-made billionaires at age 22"
    },
    {
        'handlung_typ': "umstrukturierung",
        'beschreibung': "Pivoted Mercor's business model from AI-powered recruiting to AI training marketplace, focusing on connecting domain experts with frontier AI labs",
        'datum_handlung': "2024-06-01",
        'quell_link': "https://techfundingnews.com/mercor-ai-human-in-the-loop-10-billion-funding/",
        'quell_titel': "Tech Funding News - How Mercor's human-in-the-loop AI platform went from college dropouts to $10B startup",
        'kontext': "Strategic pivot to serve AI labs including OpenAI, Anthropic, and Meta with expert human feedback for model training"
    },
    {
        'handlung_typ': "partnerschaft",
        'beschreibung': "Established partnerships with OpenAI, Anthropic, Meta, and Google DeepMind as customers for AI training services",
        'datum_handlung': "2024-08-01",
        'quell_link': "https://techcrunch.com/2025/10/29/how-ai-labs-use-mercor-to-get-the-data-companies-wont-share/",
        'quell_titel': "TechCrunch - How AI labs use Mercor to get the data companies won't share",
        'kontext': "Major AI labs became customers for domain expert services to train frontier models"
    },
    {
        'handlung_typ': "produktlaunch",
        'beschreibung': "Launched AI-powered interview system that has vetted over 300,000 job candidates",
        'datum_handlung': "2024-02-01",
        'quell_link': "https://www.linkedin.com/posts/brendan-foody-2995ab10b_were-doing-thousands-of-ai-interviews-every-activity-7160713978522783744-IPM0",
        'quell_titel': "LinkedIn - Brendan Foody post on AI interviews",
        'kontext': "Mercor's AI interviewer conducting thousands of interviews daily"
    },
    {
        'handlung_typ': "politisch",
        'beschreibung': "Spoke at TechCrunch Disrupt 2025 on AI's impact on hiring and the future of work",
        'datum_handlung': "2025-10-28",
        'quell_link': "https://techcrunch.com/2025/09/23/techcrunch-disrupt-2025-what-ai-means-for-who-gets-hired-next/",
        'quell_titel': "TechCrunch - Mercor CEO explains how AI affects who gets hired next",
        'kontext': "Panel discussion on AI reshaping hiring practices and talent access"
    },
    {
        'handlung_typ': "einstellung",
        'beschreibung': "Scaled Mercor's contractor network to over 30,000 expert workers, paying them collectively $1.5 million per day to train AI models",
        'datum_handlung': "2025-10-01",
        'quell_link': "https://finance.yahoo.com/news/mercor-pays-over-1-5-065444594.html",
        'quell_titel': "Yahoo Finance - Mercor pays over $1.5 million a day to humans training AI",
        'kontext': "Massive scaling of expert contractor network for AI training, with workers earning $85+ per hour on average"
    },
    {
        'handlung_typ': "gruendung",
        'beschreibung': "Founded Stealth, a cloud consulting business optimizing AWS promotions",
        'datum_handlung': "2020-01-01",
        'quell_link': "https://n24.com.tr/en/mercors-brendan-foody-23-year-old-dropout-builds-10b-ai-firm",
        'quell_titel': "N24 - Mercor's Brendan Foody: 23-Year-Old Dropout Builds $10B AI Firm",
        'kontext': "Early entrepreneurial venture before Mercor, founded in 2020"
    },
    {
        'handlung_typ': "gruendung",
        'beschreibung': "Founded Seros, a project aimed at improving global access to cloud computing",
        'datum_handlung': "2021-01-01",
        'quell_link': "https://n24.com.tr/en/mercors-brendan-foody-23-year-old-dropout-builds-10b-ai-firm",
        'quell_titel': "N24 - Mercor's Brendan Foody: 23-Year-Old Dropout Builds $10B AI Firm",
        'kontext': "Second entrepreneurial venture before Mercor, focused on cloud computing accessibility"
    }
]

# Insert aussagen
print(f"Inserting {len(aussagen)} aussagen for person_id {person_id}...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        aussage['aussage_text'],
        aussage['aussage_kurz'],
        aussage['modus'],
        aussage['quell_link'],
        aussage['quell_titel'],
        aussage['datum_aussage'],
        aussage['sprache'],
        aussage['kontext']
    ))

# Insert handlungen
print(f"Inserting {len(handlungen)} handlungen for person_id {person_id}...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        handlung['handlung_typ'],
        handlung['beschreibung'],
        handlung['datum_handlung'],
        handlung['quell_link'],
        handlung['quell_titel'],
        handlung['kontext']
    ))

# Commit and close
conn.commit()
conn.close()

print(f"\nSuccessfully inserted {len(aussagen)} aussagen and {len(handlungen)} handlungen for Brendan Foody (person_id={person_id})")
print(f"Total: {len(aussagen) + len(handlungen)} records")
