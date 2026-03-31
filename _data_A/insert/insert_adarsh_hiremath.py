import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 75  # Adarsh Hiremath

# WICHTIGER HINWEIS: Adarsh Hiremath ist Co-Founder und CTO von MERCOR, NICHT Perplexity AI
# Perplexity AI wurde von Aravind Srinivas gegründet

# AUSSAGEN
aussagen = [
    {
        "aussage_text": "I wouldn't say there was some specific logical thing that gave me the confidence to pursue Mercor. It was more so just an emotional pull, right, that feeling that you want to be working on the problem, you want to be working with the people that you're working with, and it just feels right in terms of an opportunity to spend a bunch of time working on and dedicating your whole life to.",
        "aussage_kurz": "Emotional pull, not logical reasoning, drove decision to pursue Mercor",
        "modus": "muendlich",
        "quell_link": "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        "quell_titel": "Meet the world's youngest self-made billionaire - Fortune",
        "datum_aussage": "2025-11-12",
        "sprache": "en",
        "kontext": "Discussing decision to drop out of Harvard and pursue Mercor full-time"
    },
    {
        "aussage_text": "Scaling culture is harder than scaling software.",
        "aussage_kurz": "Scaling culture harder than scaling software",
        "modus": "muendlich",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "datum_aussage": "2025-02-20",
        "sprache": "en",
        "kontext": "Discussing challenges of building Mercor's intense work culture"
    },
    {
        "aussage_text": "You can teach people a lot of things, but the one thing you can't quite teach people is to care.",
        "aussage_kurz": "Cannot teach people to care - core hiring principle",
        "modus": "muendlich",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "datum_aussage": "2025-02-20",
        "sprache": "en",
        "kontext": "Explaining Mercor's hiring philosophy and culture"
    },
    {
        "aussage_text": "I'll be sticking with Mercor forever... I think the main way that I've wrapped my head around it is that Mercor is just such an incredible and exciting opportunity, and I want to spend 100 percent of my time focusing on that.",
        "aussage_kurz": "Long-term commitment to Mercor - wants to focus 100% on it",
        "modus": "muendlich",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Global Indian Times - Mercor Interview",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Discussing future plans and commitment to Mercor"
    },
    {
        "aussage_text": "The future of programming will involve orchestrating AI tools rather than traditional coding.",
        "aussage_kurz": "Programming future: orchestrating AI tools, not traditional coding",
        "modus": "muendlich",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Global Indian Times - Mercor Interview",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Vision of how AI will transform software development"
    },
    {
        "aussage_text": "As AI tools become more sophisticated, the role of programmers will evolve to managing these tools rather than writing code from scratch.",
        "aussage_kurz": "Programmers will manage AI tools rather than write code",
        "modus": "muendlich",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Global Indian Times - Mercor Interview",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Explaining evolution of programming profession with AI advancement"
    },
    {
        "aussage_text": "We grew north of 40 percent month over month, all of 2024, and that growth is actually only accelerating into 2025.",
        "aussage_kurz": "40%+ monthly growth throughout 2024, accelerating in 2025",
        "modus": "muendlich",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "datum_aussage": "2025-02-20",
        "sprache": "en",
        "kontext": "Discussing Mercor's rapid growth trajectory"
    },
    {
        "aussage_text": "We don't have a sales team. There isn't a single person who works on sales at Mercor outside of the founders.",
        "aussage_kurz": "No sales team at Mercor - only founders do sales",
        "modus": "muendlich",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Global Indian Times - Mercor Interview",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Explaining Mercor's unconventional business model"
    },
    {
        "aussage_text": "And very, very quickly, we realized that the magic was actually in the really, really exceptional people that we're finding.",
        "aussage_kurz": "Magic is in finding exceptional people",
        "modus": "muendlich",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Global Indian Times - Mercor Interview",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Describing Mercor's core value proposition - talent discovery"
    },
    {
        "aussage_text": "I aim to be part of transformative projects that improve quality of life and address global issues.",
        "aussage_kurz": "Aims to improve quality of life and address global issues",
        "modus": "muendlich",
        "quell_link": "https://nri.today/adarsh-hiremath/",
        "quell_titel": "NRI Today - Adarsh Hiremath Profile",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Discussing long-term vision and goals"
    },
    {
        "aussage_text": "The vision that we have is just incredibly large and will take a lot of time and blood, sweat and tears to execute on.",
        "aussage_kurz": "Vision is incredibly large, requires blood, sweat and tears",
        "modus": "muendlich",
        "quell_link": "https://nri.today/adarsh-hiremath/",
        "quell_titel": "NRI Today - Adarsh Hiremath Profile",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Discussing the ambitious scope of Mercor's mission"
    },
    {
        "aussage_text": "My piece of advice would be to not choose the deferred life path and instead jump into things.",
        "aussage_kurz": "Advice: don't defer life, jump into things immediately",
        "modus": "muendlich",
        "quell_link": "https://nri.today/adarsh-hiremath/",
        "quell_titel": "NRI Today - Adarsh Hiremath Profile",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Advice to young entrepreneurs about taking risks"
    },
    {
        "aussage_text": "If you want to hire anyone for any job, you come to Mercor because it's the best place to do that.",
        "aussage_kurz": "Vision: Mercor as universal hiring platform",
        "modus": "muendlich",
        "quell_link": "https://nri.today/adarsh-hiremath/",
        "quell_titel": "NRI Today - Adarsh Hiremath Profile",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Describing vision of building a unified global labor marketplace"
    },
    {
        "aussage_text": "The only reason we actually just floated those numbers out is because we didn't want our team working on Sundays.",
        "aussage_kurz": "996 work culture to prevent Sunday work, not enforce it",
        "modus": "muendlich",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "datum_aussage": "2025-02-20",
        "sprache": "en",
        "kontext": "Explaining Mercor's 9-9-6 work culture (9am-9pm, 6 days per week)"
    },
    {
        "aussage_text": "Everyone's been focused on what models can do. But the real opportunity is teaching them what only humans know—judgment, nuance, and taste.",
        "aussage_kurz": "Real AI opportunity: teaching models human judgment, nuance, taste",
        "modus": "muendlich",
        "quell_link": "https://fortune.com/2026/01/13/will-ai-take-my-job-or-human-skills-protect-me-mercor-training-self-made-billionaires/",
        "quell_titel": "Fortune - Will AI Take My Job",
        "datum_aussage": "2026-01-13",
        "sprache": "en",
        "kontext": "Describing Mercor's mission to bridge machine learning and human nuance"
    },
    {
        "aussage_text": "AI isn't eliminating labor: it's reallocating it. As software automates repetitive white-collar tasks, humans will move up the value chain, teaching machines how to reason, decide, and create.",
        "aussage_kurz": "AI reallocates labor, not eliminates it - humans teach machines",
        "modus": "muendlich",
        "quell_link": "https://fortune.com/2026/01/13/will-ai-take-my-job-or-human-skills-protect-me-mercor-training-self-made-billionaires/",
        "quell_titel": "Fortune - Will AI Take My Job",
        "datum_aussage": "2026-01-13",
        "sprache": "en",
        "kontext": "Worldview on AI's impact on future of work and employment"
    },
    {
        "aussage_text": "Labor aggregation was the greatest opportunity of the 21st century.",
        "aussage_kurz": "Labor aggregation is greatest 21st century opportunity",
        "modus": "muendlich",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "datum_aussage": "2025-02-20",
        "sprache": "en",
        "kontext": "Explaining core belief that motivated founding Mercor"
    }
]

# HANDLUNGEN
handlungen = [
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Mercor in dorm room at Harvard with Brendan Foody and Surya Midha - AI recruitment platform",
        "datum_handlung": "2023-01-01",
        "quell_link": "https://www.thecrimson.com/article/2025/3/14/mercor-valuation-2-bil/",
        "quell_titel": "Harvard Crimson - Mercor Valuation",
        "kontext": "Founded Mercor during sophomore year at Harvard, initially focused on connecting freelance programmers in India with global tech companies"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Dropped out of Harvard University during sophomore year to pursue Mercor full-time",
        "datum_handlung": "2023-05-01",
        "quell_link": "https://www.thecrimson.com/article/2024/3/27/thiel-fellowship-startups-2024/",
        "quell_titel": "Harvard Crimson - Thiel Fellowship",
        "kontext": "Left Harvard after receiving Thiel Fellowship to focus 100% on building Mercor"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Awarded $100,000 Thiel Fellowship grant with co-founders - required dropping out of Harvard",
        "datum_handlung": "2024-03-27",
        "quell_link": "https://www.thecrimson.com/article/2024/3/27/thiel-fellowship-startups-2024/",
        "quell_titel": "Harvard Crimson - Five Harvard Students Win Thiel Fellowship",
        "kontext": "Received prestigious Peter Thiel Fellowship along with four other Harvard students, committing to pursue startup instead of completing degree"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Mercor raised $3.6 million seed round led by General Catalyst",
        "datum_handlung": "2023-06-01",
        "quell_link": "https://www.clay.com/dossier/mercor-funding",
        "quell_titel": "Clay - Mercor Funding Overview",
        "kontext": "First institutional funding round for Mercor with participation from Soma Capital, Link Ventures, and 2|Twelve"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Mercor raised $32 million Series A led by Benchmark",
        "datum_handlung": "2024-09-01",
        "quell_link": "https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/",
        "quell_titel": "TechCrunch - Mercor Series B",
        "kontext": "Series A funding round at $250M valuation, participation from General Catalyst and other early investors"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Mercor raised $100 million Series B at $2 billion valuation led by Felicis, with participation from Benchmark, General Catalyst, DST Global",
        "datum_handlung": "2025-02-20",
        "quell_link": "https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/",
        "quell_titel": "TechCrunch - Mercor Raises $100M at $2B Valuation",
        "kontext": "Major funding round representing 8x step-up from Series A valuation, included investment from Peter Thiel and Jack Dorsey"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Mercor raised $350 million Series C at $10 billion valuation led by Felicis, with Robinhood Ventures joining as new investor",
        "datum_handlung": "2025-10-27",
        "quell_link": "https://www.cnbc.com/2025/10/27/ai-hiring-startup-mercor-funding.html",
        "quell_titel": "CNBC - Mercor $10 Billion Valuation",
        "kontext": "Quintupled valuation from Series B, making founders the world's youngest self-made billionaires at age 22"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Mercor partnered with OpenAI and other top 5 AI labs to provide domain experts for training AI models",
        "datum_handlung": "2024-06-01",
        "quell_link": "https://www.clay.com/dossier/mercor-funding",
        "quell_titel": "Clay - Mercor Funding Overview",
        "kontext": "Strategic partnerships with leading AI labs including OpenAI and Meta to supply talent for AI model training and refinement"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launched AI interviewer that conducts interviews tailored to each candidate's individual background",
        "datum_handlung": "2024-03-01",
        "quell_link": "https://www.businesswire.com/news/home/20240320742346/en/Thiel-Foundation-Announces-Next-Thiel-Fellow-Class",
        "quell_titel": "Business Wire - Thiel Fellowship Class 2024",
        "kontext": "Key product development: AI vetting infrastructure to understand exact tasks people excel at"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Built team with intense 9-9-6 culture (9am-9pm, 6 days per week) without traditional sales department",
        "datum_handlung": "2024-01-01",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast - Most Intense Culture in Silicon Valley",
        "kontext": "Established unique hiring culture focused on finding people who genuinely care, with founders handling all sales"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Achieved $70 million ARR within 24 months of founding",
        "datum_handlung": "2025-01-01",
        "quell_link": "https://www.thetwentyminutevc.com/adarsh-hiremath",
        "quell_titel": "20VC Podcast with Adarsh Hiremath",
        "kontext": "Rapid revenue growth milestone announced during Series B fundraising"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Mercor hit $500 million in annualized revenue, up from $35 million at end of 2024",
        "datum_handlung": "2025-08-01",
        "quell_link": "https://www.clay.com/dossier/mercor-funding",
        "quell_titel": "Clay - Mercor Funding Overview",
        "kontext": "Explosive revenue growth of over 14x within 8 months, demonstrating rapid scaling"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Became world's youngest self-made billionaire at age 22 (along with co-founders) after $10B valuation",
        "datum_handlung": "2025-10-27",
        "quell_link": "https://fortune.com/2025/11/12/brendan-foody-mercor-interview-ai-adarsh-hiremath-surya-midha-youngest-self-made-billionaires/",
        "quell_titel": "Fortune - World's Youngest Self-Made Billionaire",
        "kontext": "Surpassed Mark Zuckerberg's record as youngest self-made billionaire after Series C funding round"
    },
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Pivoted Mercor from freelance programmer marketplace to AI model training talent platform",
        "datum_handlung": "2024-01-01",
        "quell_link": "https://fortune.com/2026/01/13/will-ai-take-my-job-or-human-skills-protect-me-mercor-training-self-made-billionaires/",
        "quell_titel": "Fortune - Will AI Take My Job",
        "kontext": "Strategic business model shift from connecting freelance programmers to providing domain experts for AI training"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Won national policy debate championships - first team to win all three major tournaments in single year at Bellarmine",
        "datum_handlung": "2020-06-01",
        "quell_link": "https://www.ktvu.com/news/from-bay-area-high-school-friends-worlds-youngest-self-made-billionaires-company-valued-10b",
        "quell_titel": "KTVU - Bay Area High School Friends",
        "kontext": "With partner Surya Midha, achieved historic debate championship sweep while in high school, ranked 5th nationally"
    }
]

# Aussagen einfügen
print("Füge Aussagen ein...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        aussage.get("aussage_text"),
        aussage.get("aussage_kurz"),
        aussage.get("modus"),
        aussage.get("quell_link"),
        aussage.get("quell_titel"),
        aussage.get("datum_aussage"),
        aussage.get("sprache"),
        aussage.get("kontext")
    ))

# Handlungen einfügen
print("Füge Handlungen ein...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        handlung.get("handlung_typ"),
        handlung.get("beschreibung"),
        handlung.get("datum_handlung"),
        handlung.get("quell_link"),
        handlung.get("quell_titel"),
        handlung.get("kontext")
    ))

# Änderungen speichern
conn.commit()

# Anzahl der eingefügten Datensätze
print(f"\n{'='*60}")
print(f"ERFOLGREICH EINGEFÜGT FÜR ADARSH HIREMATH (person_id={person_id})")
print(f"{'='*60}")
print(f"Aussagen: {len(aussagen)}")
print(f"Handlungen: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)}")
print(f"{'='*60}\n")

# Verbindung schließen
conn.close()

print("Datenbankverbindung geschlossen.")
print("\nWICHTIGER HINWEIS: Adarsh Hiremath ist Co-Founder und CTO von MERCOR, nicht Perplexity AI!")
print("Perplexity AI wurde von Aravind Srinivas, Denis Yarats, Johnny Ho und Andy Konwinski gegründet.")
