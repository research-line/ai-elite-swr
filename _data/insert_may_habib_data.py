import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 80  # May Habib

# AUSSAGEN
aussagen = [
    # Equity und Sprache
    {
        "aussage_text": "the language you were born speaking shouldn't impact the kind of life you end up leading",
        "aussage_kurz": "Sprache sollte Lebenschancen nicht beeinflussen",
        "modus": "muendlich",
        "quell_link": "https://writer.com/blog/humans-of-ai-may-habib/",
        "quell_titel": "Embracing risk and equity: May Habib's journey into the world of generative AI",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Statement about AI's potential to create language equity"
    },
    {
        "aussage_text": "AI has potential to be ten, maybe a hundred times more equity-creating or equity-exacerbating, depending on how we shape it",
        "aussage_kurz": "KI kann Gleichheit fördern oder verschärfen",
        "modus": "muendlich",
        "quell_link": "https://writer.com/blog/humans-of-ai-may-habib/",
        "quell_titel": "Embracing risk and equity: May Habib's journey into the world of generative AI",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Discussion on AI's dual potential for society"
    },
    {
        "aussage_text": "We can have a future where AI takes dignity away from a lot of people. Or, we can have a future where AI enables a lot more progress, access, and prosperity. We're working like hell for the latter.",
        "aussage_kurz": "KI kann Würde nehmen oder Fortschritt ermöglichen",
        "modus": "schriftlich",
        "quell_link": "https://chief.com/articles/from-finance-to-tech-how-this-banker-launched-a-multi-million-dollar-ai-startup/",
        "quell_titel": "From Finance to Tech: How This Banker Launched a Multi-Million Dollar AI Startup",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Vision for ethical AI development"
    },
    # Enterprise AI und Transformation
    {
        "aussage_text": "Our customers are taking a big risk in partnering with us because the technology is so exciting and what it enables is so breakthrough",
        "aussage_kurz": "Kunden gehen Risiko mit generativer KI ein",
        "modus": "muendlich",
        "quell_link": "https://www.runtime.news/writers-may-habib-generative-ai-challenges-the-concept-of-done/",
        "quell_titel": "Writer's May Habib: Generative AI challenges the concept of done",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "On enterprise adoption of generative AI"
    },
    {
        "aussage_text": "So much of the last year has been WRITER in risk-taking mode. I can't overemphasize how much risk enterprise generative AI leaders take today",
        "aussage_kurz": "Enterprise-KI-Führung erfordert massives Risiko",
        "modus": "muendlich",
        "quell_link": "https://www.runtime.news/writers-may-habib-generative-ai-challenges-the-concept-of-done/",
        "quell_titel": "Writer's May Habib: Generative AI challenges the concept of done",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Reflecting on building Writer during the generative AI revolution"
    },
    {
        "aussage_text": "everybody really wants to see a transformation happen with generative AI. The promise of more intelligent workplaces is so exciting. Our vision is to transform work and we do want to help companies do that.",
        "aussage_kurz": "Vision: Arbeit mit generativer KI transformieren",
        "modus": "muendlich",
        "quell_link": "https://www.runtime.news/writers-may-habib-generative-ai-challenges-the-concept-of-done/",
        "quell_titel": "Writer's May Habib: Generative AI challenges the concept of done",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Vision for enterprise AI transformation"
    },
    {
        "aussage_text": "The vast majority of enterprises have not gotten meaningful results from generative AI, and it's been two years. There has never before been such a gap between what the tech is capable of and what the enterprise results have been.",
        "aussage_kurz": "Große Kluft zwischen KI-Potenzial und Enterprise-Ergebnissen",
        "modus": "schriftlich",
        "quell_link": "https://writer.com/blog/enterprise-ai-future-fireside/",
        "quell_titel": "The future of enterprise AI: A fireside chat with WRITER CEO, May Habib",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Critique of current enterprise AI adoption"
    },
    # Modelle und technische Vision
    {
        "aussage_text": "We made a contrarian bet to build our own models 18 months before ChatGPT when investors were sceptical",
        "aussage_kurz": "Konträre Wette: Eigene Modelle vor ChatGPT",
        "modus": "muendlich",
        "quell_link": "https://ff.co/profile/may-habib",
        "quell_titel": "May Habib | Founders File",
        "datum_aussage": "2023-01-01",
        "sprache": "en",
        "kontext": "On Writer's strategic decision to build proprietary LLMs"
    },
    {
        "aussage_text": "We called the company Writer because it was very clear even in those early days that AI was going to be better than people at reading and writing and certainly faster",
        "aussage_kurz": "KI wird Menschen beim Lesen/Schreiben übertreffen",
        "modus": "muendlich",
        "quell_link": "https://www.runtime.news/writers-may-habib-generative-ai-challenges-the-concept-of-done/",
        "quell_titel": "Writer's May Habib: Generative AI challenges the concept of done",
        "datum_aussage": "2020-01-01",
        "sprache": "en",
        "kontext": "Explanation for company naming and early AI vision"
    },
    # Future of Work
    {
        "aussage_text": "I envision a future workplace where most jobs involve shaping workflows, rather than the current hands-on, manual input, and inspection processes, with AI handling the repetitive tasks to free people to focus on higher-value, strategic work",
        "aussage_kurz": "Zukunft: Menschen gestalten Workflows, KI erledigt Routinen",
        "modus": "muendlich",
        "quell_link": "https://writer.com/blog/humans-of-ai-may-habib/",
        "quell_titel": "Embracing risk and equity: May Habib's journey into the world of generative AI",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Vision for future of work with AI"
    },
    {
        "aussage_text": "the risk associated with trying out AI tools is just really nonexistent; people expect you to",
        "aussage_kurz": "Kein Risiko beim Ausprobieren von KI-Tools",
        "modus": "muendlich",
        "quell_link": "https://www.runtime.news/writers-may-habib-generative-ai-challenges-the-concept-of-done/",
        "quell_titel": "Writer's May Habib: Generative AI challenges the concept of done",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Encouraging AI adoption in enterprises"
    },
    # AI Agents und agentic AI
    {
        "aussage_text": "AI HQ represents the next era of WRITER's evolution as we bring our foundational technology to the world of agentic AI, tackling the toughest work for our customers with enterprise-grade agents",
        "aussage_kurz": "AI HQ markiert Ära der agentischen KI",
        "modus": "schriftlich",
        "quell_link": "https://writer.com/blog/writer-ai-hq-press-release/",
        "quell_titel": "WRITER Launches AI HQ to Revolutionize Agentic Work in the Enterprise",
        "datum_aussage": "2025-04-10",
        "sprache": "en",
        "kontext": "Announcement of AI HQ platform launch"
    },
    # Leadership und Unternehmenskultur
    {
        "aussage_text": "AI transformation lives or dies in customer success",
        "aussage_kurz": "KI-Transformation steht und fällt mit Kundenerfolg",
        "modus": "schriftlich",
        "quell_link": "https://writer.com/blog/writer-appoints-mina-alaghband-as-first-chief-customer-officer/",
        "quell_titel": "WRITER Appoints Mina Alaghband as First Chief Customer Officer",
        "datum_aussage": "2026-01-14",
        "sprache": "en",
        "kontext": "On appointing first Chief Customer Officer"
    },
    # Palmyra Modell
    {
        "aussage_text": "Unlocking the full potential of generative AI for enterprise customers like Intuit, Uber, L'Oreal, and Accenture requires the ability to execute complex actions and workflows",
        "aussage_kurz": "Enterprise-KI erfordert komplexe Aktionsfähigkeit",
        "modus": "schriftlich",
        "quell_link": "https://www.businesswire.com/news/home/20241009659164/en/Writer-Releases-New-Frontier-Model-Palmyra-X-004-to-Add-Intelligent-Action-to-Enterprise-AI-Applications",
        "quell_titel": "Writer Releases New Frontier Model Palmyra X 004",
        "datum_aussage": "2024-10-09",
        "sprache": "en",
        "kontext": "Announcement of Palmyra X 004 model"
    },
    # Partnerschaft mit Waseem
    {
        "aussage_text": "We're very yin and yang. I focus on broader strategy while Waseem handles technical challenges",
        "aussage_kurz": "Komplementäre Partnerschaft mit Co-Founder Waseem",
        "modus": "muendlich",
        "quell_link": "https://salesforceventures.com/perspectives/welcome-writer/",
        "quell_titel": "Welcome, Writer! | Salesforce Ventures",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Describing partnership with co-founder Waseem AlShikh"
    },
    # Kommunikation und Bias
    {
        "aussage_text": "We can have a future where AI takes dignity away from a lot of people. Or, we can have a future where AI enables a lot more progress, access, and prosperity",
        "aussage_kurz": "KI-Zukunft: Würdeverlust oder Fortschritt",
        "modus": "schriftlich",
        "quell_link": "https://chief.com/articles/from-finance-to-tech-how-this-banker-launched-a-multi-million-dollar-ai-startup/",
        "quell_titel": "From Finance to Tech: How This Banker Launched a Multi-Million Dollar AI Startup",
        "datum_aussage": "2023-01-01",
        "sprache": "en",
        "kontext": "On ethical development of AI"
    },
    # Multimodal AI
    {
        "aussage_text": "Palmyra-Vision was the result of a vision to rethink entire workflows with multimodal AI capabilities",
        "aussage_kurz": "Palmyra-Vision: Workflows mit multimodaler KI neu denken",
        "modus": "schriftlich",
        "quell_link": "https://venturebeat.com/ai/writer-unveils-palmyra-vision-a-multimodal-ai-to-reimagine-enterprise-workflows",
        "quell_titel": "Writer unveils Palmyra-Vision, a multimodal AI to reimagine enterprise workflows",
        "datum_aussage": "2024-02-27",
        "sprache": "en",
        "kontext": "Launch of Palmyra-Vision multimodal model"
    },
    # AI und Produktivität
    {
        "aussage_text": "AI has the potential to be a game-changer in terms of how we work and what we can achieve",
        "aussage_kurz": "KI als Game-Changer für Arbeit",
        "modus": "muendlich",
        "quell_link": "https://chief.com/articles/from-finance-to-tech-how-this-banker-launched-a-multi-million-dollar-ai-startup/",
        "quell_titel": "From Finance to Tech",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "On AI's transformative potential for work"
    },
    # Persönlicher Hintergrund
    {
        "aussage_text": "By daring to be different and embracing the power of taking a different path, we can unlock new possibilities and shape a future where AI is not just a tool but a force for positive change",
        "aussage_kurz": "KI als Kraft für positiven Wandel",
        "modus": "schriftlich",
        "quell_link": "https://writer.com/blog/humans-of-ai-may-habib/",
        "quell_titel": "Embracing risk and equity: May Habib's journey",
        "datum_aussage": "2024-01-01",
        "sprache": "en",
        "kontext": "Reflection on entrepreneurial journey and AI vision"
    }
]

# HANDLUNGEN
handlungen = [
    # Gründungen
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Qordoba with Waseem AlShikh, an AI-powered platform for content localization",
        "datum_handlung": "2015-03-01",
        "quell_link": "https://ff.co/profile/may-habib",
        "quell_titel": "May Habib | Founders File",
        "kontext": "First AI company focused on natural language processing and translation"
    },
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Writer with Waseem AlShikh, incorporating in August 2020 to apply transformer technology for enterprise content",
        "datum_handlung": "2020-08-01",
        "quell_link": "https://ff.co/profile/may-habib",
        "quell_titel": "May Habib | Founders File",
        "kontext": "Founded Writer as full-stack generative AI platform for enterprises"
    },
    # Investments/Funding
    {
        "handlung_typ": "investition",
        "beschreibung": "Raised $5 million seed funding for Writer",
        "datum_handlung": "2020-09-01",
        "quell_link": "https://www.insightpartners.com/ideas/may-habib-is-challenging-a-13-billion-incumbent-with-writer/",
        "quell_titel": "May Habib is challenging a $13 billion incumbent",
        "kontext": "Initial seed round for Writer"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Led Series A funding round of $21 million led by Insight Partners",
        "datum_handlung": "2021-11-01",
        "quell_link": "https://www.insightpartners.com/ideas/may-habib-is-challenging-a-13-billion-incumbent-with-writer/",
        "quell_titel": "May Habib is challenging a $13 billion incumbent",
        "kontext": "Series A to scale Writer platform"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Raised $100 million Series B funding led by ICONIQ Growth, with participation from Accenture and Vanguard as strategic investors, valuing company at over $500 million",
        "datum_handlung": "2023-09-18",
        "quell_link": "https://writer.com/blog/series-b-funding-writer/",
        "quell_titel": "WRITER raises $100 million in Series B",
        "kontext": "Major funding round with strategic enterprise customer participation"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Raised $200 million Series C at $1.9 billion valuation, co-led by Premji Invest, Radical Ventures, and ICONIQ Growth, with participation from Salesforce Ventures, Adobe Ventures, IBM Ventures, and Workday Ventures",
        "datum_handlung": "2024-11-12",
        "quell_link": "https://writer.com/blog/series-c-funding-writer-press-release/",
        "quell_titel": "WRITER raises $200M Series C at $1.9B valuation",
        "kontext": "Series C to fuel leadership in agentic enterprise AI, total raised $326M"
    },
    # Product Launches
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launched Palmyra LLM family (Small 128M, Base 5B, Large 20B parameters) trained on business writing data",
        "datum_handlung": "2023-02-01",
        "quell_link": "https://venturebeat.com/ai/why-writers-palmyra-llm-is-the-little-ai-model-that-could-for-enterprises",
        "quell_titel": "Why Writer's Palmyra LLM is the little AI model that could",
        "kontext": "First proprietary LLM models for enterprise use cases"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launched Palmyra-Vision multimodal LLM with vision capabilities, outperforming GPT-4V and Gemini Ultra on VQAv2 benchmark (84.4% vs 77.2% and 77.8%)",
        "datum_handlung": "2024-02-27",
        "quell_link": "https://venturebeat.com/ai/writer-unveils-palmyra-vision-a-multimodal-ai-to-reimagine-enterprise-workflows",
        "quell_titel": "Writer unveils Palmyra-Vision",
        "kontext": "First multimodal model for enterprise workflows with images, charts, graphs"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Released Palmyra X 004 frontier model, ranking #1 on Berkeley Tool Calling Leaderboard, developed for $700,000 using synthetic data",
        "datum_handlung": "2024-10-09",
        "quell_link": "https://www.businesswire.com/news/home/20241009659164/en/Writer-Releases-New-Frontier-Model-Palmyra-X-004-to-Add-Intelligent-Action-to-Enterprise-AI-Applications",
        "quell_titel": "Writer Releases New Frontier Model Palmyra X 004",
        "kontext": "Advanced model for tool calling and intelligent actions in enterprise AI"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launched AI HQ platform with Agent Builder, observability tools, and library of 100 ready-to-use agents for agentic enterprise work",
        "datum_handlung": "2025-04-10",
        "quell_link": "https://writer.com/blog/writer-ai-hq-press-release/",
        "quell_titel": "WRITER Launches AI HQ to Revolutionize Agentic Work",
        "kontext": "Platform for building, activating, and supervising AI agents across enterprises"
    },
    # Partnerships
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Secured Accenture as both strategic investor and customer in Series B round",
        "datum_handlung": "2023-09-18",
        "quell_link": "https://newsroom.accenture.com/news/2023/accenture-invests-in-writer-to-accelerate-enterprise-use-of-generative-ai",
        "quell_titel": "Accenture Invests in Writer",
        "kontext": "Strategic partnership with global consulting leader"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Announced strategic partnership with Perficient to revolutionize enterprise AI adoption",
        "datum_handlung": "2025-01-01",
        "quell_link": "https://www.perficient.com/news-room/news-releases/2025/perficient-and-writer-announce-strategic-partnership-to-revolutionize-enterprise-ai-adoption",
        "quell_titel": "Perficient and WRITER Announce Strategic Partnership",
        "kontext": "Partnership to accelerate enterprise AI transformation"
    },
    # Leadership Hiring
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Appointed Mina Alaghband as first Chief Customer Officer to accelerate enterprise transformation with agentic AI",
        "datum_handlung": "2026-01-14",
        "quell_link": "https://writer.com/blog/writer-appoints-mina-alaghband-as-first-chief-customer-officer/",
        "quell_titel": "WRITER Appoints Mina Alaghband as First Chief Customer Officer",
        "kontext": "Former McKinsey Partner joins to strengthen customer success and AI transformation"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Announced new C-Suite executives to support accelerating growth trajectory",
        "datum_handlung": "2024-06-20",
        "quell_link": "https://www.businesswire.com/news/home/20240620768956/en/Enterprise-AI-Platform-Writer-Announces-New-C-Suite-Executives-to-Support-Accelerating-Growth-Trajectory",
        "quell_titel": "Enterprise AI Platform Writer Announces New C-Suite Executives",
        "kontext": "C-level expansion to support hypergrowth phase"
    },
    # Recognition
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Selected as World Economic Forum Young Global Leader Class of 2024",
        "datum_handlung": "2024-04-08",
        "quell_link": "https://www.businesswire.com/news/home/20240408625210/en/Writer-CEO-May-Habib-Joins-World-Economic-Forums-Young-Global-Leaders-Class-of-2024",
        "quell_titel": "Writer CEO May Habib Joins World Economic Forum's Young Global Leaders",
        "kontext": "Recognition for impact in generative AI and enterprise technology"
    }
]

# Einfügen der Aussagen
print("Füge Aussagen ein...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        aussage["aussage_text"],
        aussage["aussage_kurz"],
        aussage["modus"],
        aussage["quell_link"],
        aussage["quell_titel"],
        aussage["datum_aussage"],
        aussage["sprache"],
        aussage["kontext"]
    ))

print(f"{len(aussagen)} Aussagen eingefügt.")

# Einfügen der Handlungen
print("Füge Handlungen ein...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        handlung["handlung_typ"],
        handlung["beschreibung"],
        handlung["datum_handlung"],
        handlung["quell_link"],
        handlung["quell_titel"],
        handlung["kontext"]
    ))

print(f"{len(handlungen)} Handlungen eingefügt.")

# Commit und Schließen
conn.commit()
conn.close()

print("\n" + "="*60)
print("ZUSAMMENFASSUNG")
print("="*60)
print(f"Person ID: {person_id} (May Habib)")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Einträge")
print("="*60)
