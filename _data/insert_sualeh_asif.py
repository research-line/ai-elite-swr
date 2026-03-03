import sqlite3
from datetime import datetime

# Datenbank-Verbindung
db_path = r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 79  # Sualeh Asif

# AUSSAGEN
aussagen = [
    # Vision und Philosophie
    {
        'aussage_text': 'Plan: build the tool that builds all the worlds software. We will continue to focus all of our energy on hardcore engineering and research.',
        'aussage_kurz': 'Build tool for all world software, focus on engineering',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/sualehasif996',
        'quell_titel': 'Sualeh Asif on X',
        'datum_aussage': '2024-08-01',
        'sprache': 'en',
        'kontext': 'Statement about Cursor vision and company focus'
    },
    {
        'aussage_text': 'that people would still want to use in 10 years',
        'aussage_kurz': 'Building tools for 10-year longevity',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary Rethinking How We Build Software in the Age of AI',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Philosophy on long-term product vision vs quick exits'
    },
    {
        'aussage_text': 'In a world where AI is creating code, the real innovation is creating environments where human developers remain in control — amplified, not sidelined. That\'s what Asif is building: a world where AI is a co-pilot, not a crutch.',
        'aussage_kurz': 'AI as co-pilot, not crutch for developers',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Philosophy on human-AI collaboration in software development'
    },
    {
        'aussage_text': 'increase productivity and learning, not replace the coder',
        'aussage_kurz': 'Increase productivity, not replace coders',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Statement on purpose of AI coding tools'
    },
    {
        'aussage_text': 'not out to replace developers — he\'s out to equip them',
        'aussage_kurz': 'Equip developers, not replace them',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Core philosophy on developer empowerment'
    },

    # Copilot und Scaling
    {
        'aussage_text': 'Copilot was the first real AI product, the first language model consumer product',
        'aussage_kurz': 'Copilot first real AI language model product',
        'modus': 'muendlich',
        'quell_link': 'https://lexfridman.com/cursor-team-transcript/',
        'quell_titel': 'Cursor Team: Future of Programming with AI | Lex Fridman Podcast #447',
        'datum_aussage': '2024-10-01',
        'sprache': 'en',
        'kontext': 'Recognition of GitHub Copilot as pioneering AI product'
    },
    {
        'aussage_text': 'scaling is bigger and better, but predictably better',
        'aussage_kurz': 'Scaling is predictably better',
        'modus': 'muendlich',
        'quell_link': 'https://lexfridman.com/cursor-team-transcript/',
        'quell_titel': 'Cursor Team: Future of Programming with AI | Lex Fridman Podcast #447',
        'datum_aussage': '2024-10-01',
        'sprache': 'en',
        'kontext': 'Statement on AI model scaling laws'
    },

    # Product Philosophy
    {
        'aussage_text': 'AI should enhance, not replace, developers. Cursor is a collaborative intelligence — an assistant that lightens cognitive load, speeds up development, and naturally instils best practices.',
        'aussage_kurz': 'AI as collaborative intelligence to enhance developers',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Anysphere company philosophy on AI and developers'
    },
    {
        'aussage_text': 'a fast colleague that removes repetitive, predictable work so the human operator steers creative effort',
        'aussage_kurz': 'Fast colleague removing repetitive work',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/@imharshsavaliya/sualeh-asif-the-mit-bred-visionary-rethinking-how-we-build-software-in-the-age-of-ai-f674c30f9921',
        'quell_titel': 'Sualeh Asif: The MIT-Bred Visionary',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Description of Cursor as AI assistant'
    },

    # Gradient Dissent Podcast
    {
        'aussage_text': 'scaling AI inference to support hundreds of millions of requests per day',
        'aussage_kurz': 'Scaling to hundreds of millions of requests daily',
        'modus': 'muendlich',
        'quell_link': 'https://wandb.ai/site/resources/podcast/episodes/inside-cursor-the-future-of-ai-coding-with-co-founder-sualeh-asif/',
        'quell_titel': 'Inside Cursor: The future of AI coding with Co-founder Sualeh Asif - Gradient Dissent',
        'datum_aussage': '2024-11-01',
        'sprache': 'en',
        'kontext': 'Discussion of Cursor infrastructure challenges'
    },
    {
        'aussage_text': 'building trust through product quality',
        'aussage_kurz': 'Build trust through product quality',
        'modus': 'muendlich',
        'quell_link': 'https://wandb.ai/site/resources/podcast/episodes/inside-cursor-the-future-of-ai-coding-with-co-founder-sualeh-asif/',
        'quell_titel': 'Inside Cursor: The future of AI coding - Gradient Dissent',
        'datum_aussage': '2024-11-01',
        'sprache': 'en',
        'kontext': 'Discussion on building user trust in AI tools'
    },

    # Community and Future Vision
    {
        'aussage_text': 'AI isn\'t here to replace engineers. We need humans for their ability to exercise creativity and think critically',
        'aussage_kurz': 'AI needs human creativity and critical thinking',
        'modus': 'muendlich',
        'quell_link': 'https://tribune.com.pk/story/2554852/cursor-wows-islamabad-tech-crowd-1',
        'quell_titel': 'Cursor wows Islamabad tech crowd | The Express Tribune',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Statement from Cursor team at Pakistan meetup in Islamabad'
    },
    {
        'aussage_text': 'Cursor is not about eliminating the work humans do. It\'s about what can be achieved when humans work alongside the power of AI.',
        'aussage_kurz': 'Cursor about human-AI collaboration',
        'modus': 'muendlich',
        'quell_link': 'https://tribune.com.pk/story/2554852/cursor-wows-islamabad-tech-crowd-1',
        'quell_titel': 'Cursor wows Islamabad tech crowd',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Statement at Pakistan developer meetup'
    },

    # Background and Motivation
    {
        'aussage_text': 'their frustration with coding\'s repetitive and fragmented nature inspired them to create a more intelligent, intuitive coding assistant',
        'aussage_kurz': 'Frustration with repetitive coding inspired Cursor',
        'modus': 'muendlich',
        'quell_link': 'https://techfundingnews.com/meet-cursor-how-anyspheres-mit-born-ai-startup-hit-a-9-9b-valuation-in-3-years/',
        'quell_titel': 'Meet Cursor: How Anysphere\'s MIT-born AI startup hit a $9.9B valuation',
        'datum_aussage': '2022-01-01',
        'sprache': 'en',
        'kontext': 'Origin story from MIT late-night hackathons'
    },

    # Technical Vision
    {
        'aussage_text': 'predict programmer actions and streamline code writing, with the aim of significantly automating software engineering tasks while keeping programmers in control',
        'aussage_kurz': 'Predict actions, automate tasks, keep programmers in control',
        'modus': 'muendlich',
        'quell_link': 'https://app.daily.dev/posts/cursor-building-the-human-ai-hybrid-engineer-michael-truell-and-sualeh-asif-vhhpfstgd',
        'quell_titel': 'Cursor: Building the Human-AI Hybrid Engineer',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Vision for predictive AI coding assistant'
    }
]

# HANDLUNGEN
handlungen = [
    # Company Founding
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded Anysphere Inc. at MIT with Michael Truell, Arvid Lunnemark, and Aman Sanger to develop AI-powered coding tools',
        'datum_handlung': '2022-04-01',
        'quell_link': 'https://en.wikipedia.org/wiki/Anysphere',
        'quell_titel': 'Anysphere - Wikipedia',
        'kontext': 'Company founded by four MIT students'
    },

    # Product Launch
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Launched Cursor AI code editor, an AI-native IDE built on VS Code fork',
        'datum_handlung': '2023-03-01',
        'quell_link': 'https://research.contrary.com/company/anysphere',
        'quell_titel': 'Report: Anysphere Business Breakdown & Founding Story',
        'kontext': 'First version of Cursor released to public'
    },

    # OpenAI Accelerator
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'Completed OpenAI Startup Fund accelerator program',
        'datum_handlung': '2023-06-01',
        'quell_link': 'https://research.contrary.com/company/anysphere',
        'quell_titel': 'Report: Anysphere Business Breakdown & Founding Story',
        'kontext': 'Graduated from OpenAI accelerator before seed funding'
    },

    # Seed Funding
    {
        'handlung_typ': 'investition',
        'beschreibung': 'Raised $8 million seed round led by OpenAI Startup Fund, with participation from Nat Friedman (former GitHub CEO) and Arash Ferdowsi (Dropbox co-founder)',
        'datum_handlung': '2023-10-01',
        'quell_link': 'https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/',
        'quell_titel': 'Anysphere raises $8M from OpenAI to build an AI-powered IDE | TechCrunch',
        'kontext': 'Seed round following OpenAI accelerator completion'
    },

    # Series A Funding
    {
        'handlung_typ': 'investition',
        'beschreibung': 'Raised $60+ million Series A at $400 million valuation, co-led by Andreessen Horowitz (a16z) and Thrive Capital, with participation from Patrick Collison (Stripe CEO)',
        'datum_handlung': '2024-08-01',
        'quell_link': 'https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/',
        'quell_titel': 'Anysphere raised $60M Series A at $400M valuation from a16z, Thrive | TechCrunch',
        'kontext': 'Major funding round with top-tier VCs'
    },

    # Supermaven Acquisition
    {
        'handlung_typ': 'kauf',
        'beschreibung': 'Acquired Supermaven AI coding assistant founded by Jacob Jackson (Tabnine co-founder) to enhance Tab AI model with faster, context-aware code completion',
        'datum_handlung': '2024-11-12',
        'quell_link': 'https://techcrunch.com/2024/11/12/anysphere-acquires-supermaven-to-beef-up-cursor/',
        'quell_titel': 'Anysphere acquires Supermaven to beef up Cursor | TechCrunch',
        'kontext': 'Strategic acquisition to improve AI model capabilities'
    },

    # Series B Funding
    {
        'handlung_typ': 'investition',
        'beschreibung': 'Raised $105 million Series B at $2.5 billion valuation led by Thrive Capital',
        'datum_handlung': '2024-12-01',
        'quell_link': 'https://techcrunch.com/2024/12/19/in-just-4-months-ai-coding-assistant-cursor-raised-another-100m-at-a-2-5b-valuation-led-by-thrive-sources-say/',
        'quell_titel': 'Cursor raised $100M at $2.6B valuation led by Thrive | TechCrunch',
        'kontext': 'Second major funding round in 2024, 4 months after Series A'
    },

    # Partnership with xAI
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'Announced multi-year partnership with xAI to integrate Grok models, becoming select launch partner for grok-code-fast-1',
        'datum_handlung': '2024-12-01',
        'quell_link': 'https://x.ai/news/grok-code-fast-1',
        'quell_titel': 'Grok Code Fast 1 | xAI',
        'kontext': 'Strategic partnership to offer free xAI models in Cursor'
    },

    # Partnership with Anthropic
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'Announced multi-year partnership with Anthropic to integrate Claude models with expectation of long-term collaboration',
        'datum_handlung': '2024-12-01',
        'quell_link': 'https://www.anthropic.com/webinars/how-cursor-pioneering-coding-frontiers-claude-opus-4',
        'quell_titel': 'How Cursor is pioneering new coding frontiers with Claude Opus 4 | Anthropic',
        'kontext': 'Partnership with Anthropic for Claude integration'
    },

    # ARR Milestone $100M
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Cursor reached $100 million in annual recurring revenue (ARR) in 20 months, becoming fastest-growing SaaS to this milestone',
        'datum_handlung': '2025-01-01',
        'quell_link': 'https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/',
        'quell_titel': 'Cursor Hit $1B ARR in 24 Months: The Fastest Scaling SaaS Ever? | SaaStr',
        'kontext': 'Record-breaking growth milestone without marketing spend'
    },

    # ARR Milestone $200M
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Cursor reached $200 million in annual recurring revenue',
        'datum_handlung': '2025-03-01',
        'quell_link': 'https://getlatka.com/companies/cursor.com',
        'quell_titel': 'How Cursor by Anysphere hit $1B revenue and 50K customers in 2025',
        'kontext': 'Continued rapid revenue growth trajectory'
    },

    # Graphite Acquisition
    {
        'handlung_typ': 'kauf',
        'beschreibung': 'Signed definitive agreement to acquire Graphite, AI code review startup serving 500+ companies including Shopify, Snowflake, Figma, for "way over" $290M last valuation with mix of cash and equity',
        'datum_handlung': '2025-12-19',
        'quell_link': 'https://fortune.com/2025/12/19/cursor-ai-coding-startup-graphite-competition-heats-up/',
        'quell_titel': 'Cursor acquires code review startup Graphite | Fortune',
        'kontext': 'Second major acquisition to address code review bottleneck'
    },

    # Product Features
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Launched in-house AI models that generate more code than almost any other LLMs in the world',
        'datum_handlung': '2024-11-01',
        'quell_link': 'https://www.trendingtopics.eu/cursor-launches-in-house-coding-model-to-become-independent-from-openai-anthropic/',
        'quell_titel': 'Cursor launches in-house coding model | Trending Topics',
        'kontext': 'Developed proprietary models alongside third-party integrations'
    },

    # Community Engagement
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Cursor team held first Pakistan meetup in Islamabad with 100+ builders, tech enthusiasts and students, featuring live demo and Q&A',
        'datum_handlung': '2024-01-01',
        'quell_link': 'https://tribune.com.pk/story/2554852/cursor-wows-islamabad-tech-crowd-1',
        'quell_titel': 'Cursor wows Islamabad tech crowd | The Express Tribune',
        'kontext': 'Community engagement event in Pakistan'
    }
]

# Insert Aussagen
print("Inserting Aussagen...")
for i, aussage in enumerate(aussagen, 1):
    try:
        cursor.execute('''
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
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
        print(f"  {i}. Aussage inserted: {aussage['aussage_kurz'][:50]}...")
    except Exception as e:
        print(f"  ERROR on aussage {i}: {e}")

# Insert Handlungen
print("\nInserting Handlungen...")
for i, handlung in enumerate(handlungen, 1):
    try:
        cursor.execute('''
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            person_id,
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))
        print(f"  {i}. Handlung inserted: {handlung['handlung_typ']} - {handlung['beschreibung'][:60]}...")
    except Exception as e:
        print(f"  ERROR on handlung {i}: {e}")

# Commit and close
conn.commit()
conn.close()

print("\n" + "="*80)
print("ZUSAMMENFASSUNG")
print("="*80)
print(f"Person ID: {person_id} (Sualeh Asif)")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"GESAMT: {len(aussagen) + len(handlungen)} Einträge")
print("="*80)
