import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 69

# AUSSAGEN
aussagen = [
    # Interview-Aussagen (Sayak Paul Medium Interview)
    {
        "aussage_text": "The important components in this paper were doing parallel computation across all the words in the sentence and the ability to learn and capture the relationships between any two words in the sentence, not just neighboring words as in long short-term memory networks and convolutional neural network-based models.",
        "aussage_kurz": "Transformer: Parallel computation and word relationships",
        "modus": "muendlich",
        "quell_link": "https://sayakpaul.medium.com/an-interview-with-niki-parmar-senior-research-scientist-at-google-brain-74a592596cb3",
        "quell_titel": "An interview with Niki Parmar, Senior Research Scientist at Google Brain",
        "datum_aussage": "2020-01-01",
        "sprache": "en",
        "kontext": "Explaining the key innovation of the Transformer architecture in the 'Attention Is All You Need' paper"
    },
    {
        "aussage_text": "I believe one should always start with forming the research question/goal and an initial hypothesis. In collaborative settings, it's useful to brainstorm closely and refine solutions based on incoming results. In our project, we did this every day and discussed at great lengths the new results we got each day and then went on to try new things. Through the course of the project, paying attention to details is important — every detail, every question, every choice seems relevant.",
        "aussage_kurz": "Research approach: Hypothesis, collaboration, attention to details",
        "modus": "muendlich",
        "quell_link": "https://sayakpaul.medium.com/an-interview-with-niki-parmar-senior-research-scientist-at-google-brain-74a592596cb3",
        "quell_titel": "An interview with Niki Parmar, Senior Research Scientist at Google Brain",
        "datum_aussage": "2020-01-01",
        "sprache": "en",
        "kontext": "Describing her research methodology and collaborative approach at Google Brain"
    },
    {
        "aussage_text": "Choosing a problem is one of the hardest parts, which to be honest, I still struggle with sometimes. Being able to get feedback or collaborate with peers really helps in all aspects. The other, which is echoed several times and is extremely important, is to ask a lot of questions — small or big. Useful brainstorming and making interesting connections happen by doing that. I've also found that staying consistent on a problem and not giving up early forces one to look in multiple directions for solutions that can help to find new insights.",
        "aussage_kurz": "Problem selection, persistence, and asking questions",
        "modus": "muendlich",
        "quell_link": "https://sayakpaul.medium.com/an-interview-with-niki-parmar-senior-research-scientist-at-google-brain-74a592596cb3",
        "quell_titel": "An interview with Niki Parmar, Senior Research Scientist at Google Brain",
        "datum_aussage": "2020-01-01",
        "sprache": "en",
        "kontext": "Reflecting on the challenges of research and her approach to problem-solving"
    },
    {
        "aussage_text": "Today is as good a day as any to share that I joined Anthropic last Dec :) Claude 3.7 is a remarkable model at complex tasks, especially coding, and I'm thrilled to have contributed to its development.",
        "aussage_kurz": "Joined Anthropic, contributed to Claude 3.7",
        "modus": "schriftlich",
        "quell_link": "https://x.com/nikiparmar09/status/1894168474886574404",
        "quell_titel": "Niki Parmar on X (Twitter)",
        "datum_aussage": "2025-02-25",
        "sprache": "en",
        "kontext": "Announcement of joining Anthropic and working on Claude 3.7 Sonnet"
    },
    {
        "aussage_text": "Life update: For those who haven't heard, I left Google Brain! I'm grateful for the 6+ years I spent there, the peers and friends that are inspiring and the opportunities to push on some of the most important problems in AI.",
        "aussage_kurz": "Left Google Brain after 6+ years, grateful for opportunities",
        "modus": "schriftlich",
        "quell_link": "https://x.com/nikiparmar09/status/1518714367386169344",
        "quell_titel": "Niki Parmar on X (Twitter)",
        "datum_aussage": "2022-04-25",
        "sprache": "en",
        "kontext": "Announcement of departure from Google Brain in April 2022"
    },
    {
        "aussage_text": "We are in an exciting era of human-computer collaboration evolving the way we will reason with, process and generate information.",
        "aussage_kurz": "Exciting era of human-computer collaboration",
        "modus": "schriftlich",
        "quell_link": "https://www.ayeshakhanna.com/women-in-ai-feature/niki-parmar",
        "quell_titel": "Niki Parmar | AI Researcher & Co-Founder of Adept AI",
        "datum_aussage": "2023-01-01",
        "sprache": "en",
        "kontext": "Statement about her vision for AI and human-computer collaboration"
    },
    {
        "aussage_text": "I developed my first interest in Machine Learning during my undergrad by taking MOOCs by Andrew Ng and Peter Norvig, and when I joined USC, I was part of a computational social science lab led by Prof. Morteza Dehghani, where I explored social science questions using ML and big data.",
        "aussage_kurz": "Developed ML interest through MOOCs and USC lab work",
        "modus": "muendlich",
        "quell_link": "https://viterbischool.usc.edu/news/2023/03/attention-is-all-you-need-usc-alumni-paved-path-for-chatgpt/",
        "quell_titel": "USC Alumni Paved Path for ChatGPT",
        "datum_aussage": "2023-03-01",
        "sprache": "en",
        "kontext": "Describing her educational journey into machine learning"
    },
    {
        "aussage_text": "There's always more to learn. Even after co-authoring the influential Transformer paper, she doesn't believe she's 'made it.' Additionally, she doesn't want to be remembered just for the Transformer model.",
        "aussage_kurz": "Always more to learn, not just remembered for Transformer",
        "modus": "muendlich",
        "quell_link": "https://nationnow.org/2024/10/05/niki-parmar-shares-her-experience-on-moving-to-modern-ai-pioneer/",
        "quell_titel": "Niki Parmar shares her experience on moving to modern AI Pioneer",
        "datum_aussage": "2024-10-05",
        "sprache": "en",
        "kontext": "Reflections on her career and legacy in October 2024"
    }
]

# HANDLUNGEN
handlungen = [
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Joined Google Research as software engineer, focusing on end-to-end deep learning systems for NLP",
        "datum_handlung": "2015-06-01",
        "quell_link": "https://www.linkedin.com/in/nikiparmar/",
        "quell_titel": "Niki Parmar - LinkedIn",
        "kontext": "First position after completing Master's at USC"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Transitioned to Google Brain as Research Software Engineer, contributing to research on self-attention and deep learning",
        "datum_handlung": "2017-10-01",
        "quell_link": "https://www.linkedin.com/in/nikiparmar/",
        "quell_titel": "Niki Parmar - LinkedIn",
        "kontext": "Moved from Google Research to Google Brain research team"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Co-authored landmark paper 'Attention Is All You Need' introducing Transformer architecture at NeurIPS 2017, which became foundation for modern LLMs",
        "datum_handlung": "2017-06-12",
        "quell_link": "https://arxiv.org/abs/1706.03762",
        "quell_titel": "Attention Is All You Need - arXiv",
        "kontext": "Paper submitted June 2017, presented at NeurIPS 2017. Has over 254,000+ citations and revolutionized NLP and AI"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Co-authored 'Image Transformer' paper extending Transformer architecture to image generation, achieving state-of-the-art results on ImageNet",
        "datum_handlung": "2018-02-15",
        "quell_link": "https://arxiv.org/abs/1802.05751",
        "quell_titel": "Image Transformer - arXiv",
        "kontext": "Published at ICML 2018, extended self-attention to computer vision tasks"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Contributed to Tensor2Tensor library release at Google Brain, an open-source library for deep learning models and datasets",
        "datum_handlung": "2018-03-01",
        "quell_link": "https://github.com/tensorflow/tensor2tensor",
        "quell_titel": "Tensor2Tensor - GitHub",
        "kontext": "Part of core team developing open-source ML research infrastructure"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Left Google Brain after 6+ years at Google (including Google Research and Google Brain)",
        "datum_handlung": "2021-11-01",
        "quell_link": "https://x.com/nikiparmar09/status/1518714367386169344",
        "quell_titel": "Niki Parmar on X (Twitter)",
        "kontext": "Departed to pursue entrepreneurial ventures in AI"
    },
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Adept AI Labs with David Luan (CEO) and Ashish Vaswani (Chief Scientist), serving as CTO",
        "datum_handlung": "2022-04-26",
        "quell_link": "https://techcrunch.com/2022/04/26/2304039/",
        "quell_titel": "Adept aims to build AI that can automate any software process - TechCrunch",
        "kontext": "Company emerged from stealth to build useful general intelligence for automating software processes"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Adept AI raised $65 million Series A funding led by Greylock and Root Ventures, with participation from Reid Hoffman, Scott Belsky, Andrej Karpathy, and others",
        "datum_handlung": "2022-04-26",
        "quell_link": "https://www.businesswire.com/news/home/20220426005963/en/AI-Transformer-Inventors-Launch-Adept-with-%2465M-to-Lend-a-Hand-to-Knowledge-Workers",
        "quell_titel": "AI Transformer Inventors Launch Adept with $65M - BusinessWire",
        "kontext": "Series A funding announcement when company emerged from stealth"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Left Adept AI as co-founder and CTO after approximately 6 months",
        "datum_handlung": "2022-11-01",
        "quell_link": "https://www.theinformation.com/briefings/two-co-founders-of-adept-an-openai-rival-suddenly-left-to-start-another-company",
        "quell_titel": "Two Co-Founders of Adept, an OpenAI Rival, Suddenly Left to Start Another Company - The Information",
        "kontext": "Left with Ashish Vaswani to start Essential AI, reasons not publicly disclosed"
    },
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Essential AI with Ashish Vaswani to build 'Enterprise Brain' for LLM-powered business workflow automation",
        "datum_handlung": "2023-01-01",
        "quell_link": "https://www.crunchbase.com/person/niki-parmar",
        "quell_titel": "Niki Parmar - Crunchbase",
        "kontext": "Second startup venture after departing Adept AI"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Essential AI raised $56.5 million Series A funding led by March Capital, with backing from Google, NVIDIA, AMD, and Thrive Capital",
        "datum_handlung": "2023-12-11",
        "quell_link": "https://www.businesswire.com/news/home/20231211867788/en/Essential-AI-Raises-$56.5M-Series-A-to-Build-the-Enterprise-Brain",
        "quell_titel": "Essential AI Raises $56.5M Series A to Build the Enterprise Brain - BusinessWire",
        "kontext": "Company emerged from stealth with significant backing from major tech companies"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Joined Anthropic as Member of Technical Staff, contributing to Claude 3.7 Sonnet development",
        "datum_handlung": "2024-12-01",
        "quell_link": "https://analyticsindiamag.com/ai-news-updates/transformer-co-author-niki-parmar-joins-anthropic-after-founding-two-ai-startups/",
        "quell_titel": "Transformer Co-Author Niki Parmar Joins Anthropic After Founding Two AI Startups - AIM",
        "kontext": "Joined Anthropic after founding and co-founding two AI startups (Adept AI and Essential AI)"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Contributed to development and launch of Claude 3.7 Sonnet model at Anthropic, described as remarkable at complex tasks especially coding",
        "datum_handlung": "2025-02-25",
        "quell_link": "https://x.com/nikiparmar09/status/1894168474886574404",
        "quell_titel": "Niki Parmar on X (Twitter)",
        "kontext": "Announcement of her contribution to Claude 3.7 Sonnet model at Anthropic"
    }
]

# Aussagen einfügen
print("Inserting Aussagen...")
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

print(f"OK: {len(aussagen)} Aussagen eingefuegt")

# Handlungen einfügen
print("Inserting Handlungen...")
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

print(f"OK: {len(handlungen)} Handlungen eingefuegt")

# Commit und schließen
conn.commit()
conn.close()

print("\n" + "="*50)
print("ZUSAMMENFASSUNG")
print("="*50)
print(f"Person ID: {person_id} (Niki Parmar)")
print(f"Aussagen: {len(aussagen)}")
print(f"Handlungen: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Datensätze")
print("="*50)
