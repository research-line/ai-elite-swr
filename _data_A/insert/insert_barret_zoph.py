import sqlite3
from datetime import datetime

# Verbindung zur Datenbank
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 91  # Barret Zoph

# AUSSAGEN - Statements und Zitate
aussagen = [
    {
        "aussage_text": "Despite their success, neural networks are still hard to design.",
        "aussage_kurz": "Neural networks hard to design",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1611.01578",
        "quell_titel": "Neural Architecture Search with Reinforcement Learning",
        "datum_aussage": "2016-11-01",
        "sprache": "en",
        "kontext": "From the abstract of Zoph & Le's foundational NAS paper, describing motivation for automating neural architecture design"
    },
    {
        "aussage_text": "On the CIFAR-10 dataset, our algorithm can design a novel network architecture that rivals the best human-invented architecture in terms of test set accuracy.",
        "aussage_kurz": "NAS rivals human-invented architectures",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1611.01578",
        "quell_titel": "Neural Architecture Search with Reinforcement Learning",
        "datum_aussage": "2016-11-01",
        "sprache": "en",
        "kontext": "Describing results from Neural Architecture Search using reinforcement learning, demonstrating that automated design can match human experts"
    },
    {
        "aussage_text": "I posted this note to OpenAI. Hey everybody, I have decided to leave OpenAI. This was a very difficult decision as I have has such an incredible time at OpenAI. I got to join right before ChatGPT and helped build the post-training team from scratch with John Schulman and others.",
        "aussage_kurz": "Leaving OpenAI - built post-training team",
        "modus": "schriftlich",
        "quell_link": "https://x.com/barret_zoph/status/1839095143397515452",
        "quell_titel": "Barret Zoph on X - OpenAI departure announcement",
        "datum_aussage": "2024-09-25",
        "sprache": "en",
        "kontext": "Announcement of departure from OpenAI, highlighting his role in building the post-training team that developed ChatGPT"
    },
    {
        "aussage_text": "It felt like a natural point for me to explore new opportunities outside of OpenAI.",
        "aussage_kurz": "Natural point to explore new opportunities",
        "modus": "schriftlich",
        "quell_link": "https://techcrunch.com/2024/09/25/openais-chief-research-officer-has-left/",
        "quell_titel": "OpenAI's chief research officer has left following CTO Mira Murati's exit",
        "datum_aussage": "2024-09-25",
        "sprache": "en",
        "kontext": "Describing his decision to leave OpenAI as personal decision based on how he wanted to evolve the next phase of his career"
    },
    {
        "aussage_text": "We have parted ways with Barret Zoph.",
        "aussage_kurz": "Parted ways with Barret Zoph",
        "modus": "schriftlich",
        "quell_link": "https://www.benzinga.com/markets/tech/26/01/49925838/barret-zoph-reportedly-fired-from-thinking-machines-by-mira-murati-for-unethical-conduct-immediately-returns-to-openai",
        "quell_titel": "Barret Zoph Reportedly Fired From Thinking Machines By Mira Murati",
        "datum_aussage": "2026-01-14",
        "sprache": "en",
        "kontext": "Mira Murati's announcement at Thinking Machines all-hands meeting about Zoph's termination for alleged unethical conduct"
    },
    {
        "aussage_text": "Zoph was so skilled that he was actually able to match human performance.",
        "aussage_kurz": "Zoph matched human performance in AutoML",
        "modus": "schriftlich",
        "quell_link": "https://medium.com/syncedreview/a-conversation-with-quoc-le-the-ai-expert-behind-google-automl-73a7d0c9fe38",
        "quell_titel": "A Conversation With Quoc Le: The AI Expert Behind Google AutoML",
        "datum_aussage": "2018-06-15",
        "sprache": "en",
        "kontext": "Quoc Le describing Barret Zoph's exceptional abilities as a resident at Google Brain, exceeding expectations on the AutoML project"
    },
    {
        "aussage_text": "ChatGPT was initially meant to be a low key research preview.",
        "aussage_kurz": "ChatGPT started as low-key research preview",
        "modus": "muendlich",
        "quell_link": "https://hai.stanford.edu/events/john-schulman-and-barret-zoph-chatgpt-and-art-post-training",
        "quell_titel": "ChatGPT and the Art of Post-Training - Stanford HAI",
        "datum_aussage": "2024-11-15",
        "sprache": "en",
        "kontext": "From Zoph & Schulman's Stanford HAI talk about the development process of ChatGPT and post-training methods"
    },
    {
        "aussage_text": "Post-training makes the model behave like an assistant and follow the right format, and it's the final stage of getting the model ready for production.",
        "aussage_kurz": "Post-training prepares models for production",
        "modus": "muendlich",
        "quell_link": "https://hai.stanford.edu/events/john-schulman-and-barret-zoph-chatgpt-and-art-post-training",
        "quell_titel": "ChatGPT and the Art of Post-Training - Stanford HAI",
        "datum_aussage": "2024-11-15",
        "sprache": "en",
        "kontext": "Explaining the role of post-training in AI model development at Stanford HAI seminar"
    },
    {
        "aussage_text": "The key contribution was the design of a new search space (the 'NASNet search space') which enables transferability.",
        "aussage_kurz": "NASNet search space enables transferability",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1707.07012",
        "quell_titel": "Learning Transferable Architectures for Scalable Image Recognition",
        "datum_aussage": "2017-07-21",
        "sprache": "en",
        "kontext": "Describing innovation in NASNet that allowed architectures designed on small datasets to transfer to larger ones like ImageNet"
    },
    {
        "aussage_text": "We search for an architectural building block on a small dataset and then transfer the block to a larger dataset.",
        "aussage_kurz": "Search on small, transfer to large datasets",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1707.07012",
        "quell_titel": "Learning Transferable Architectures for Scalable Image Recognition",
        "datum_aussage": "2017-07-21",
        "sprache": "en",
        "kontext": "Explaining the NASNet methodology for efficient architecture search with transfer learning"
    },
    {
        "aussage_text": "They started working together in September 2022 with a big push on making an aligned chatbot that they could safely deploy.",
        "aussage_kurz": "Big push on aligned chatbot deployment",
        "modus": "muendlich",
        "quell_link": "https://hai.stanford.edu/events/john-schulman-and-barret-zoph-chatgpt-and-art-post-training",
        "quell_titel": "ChatGPT and the Art of Post-Training - Stanford HAI",
        "datum_aussage": "2024-11-15",
        "sprache": "en",
        "kontext": "Describing the beginning of the ChatGPT project with focus on alignment and safe deployment"
    },
    {
        "aussage_text": "Our method is up to 5 times more efficient than the RL method of Zoph et al. (2018) in terms of number of models evaluated.",
        "aussage_kurz": "PNAS 5x more efficient than original NAS",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1712.00559",
        "quell_titel": "Progressive Neural Architecture Search",
        "datum_aussage": "2017-12-01",
        "sprache": "en",
        "kontext": "Progressive NAS paper comparing efficiency improvements over Zoph's original reinforcement learning based NAS approach"
    },
    {
        "aussage_text": "Transfer learning significantly improves BLEU scores across a range of low-resource languages by an average of 5.6 BLEU.",
        "aussage_kurz": "Transfer learning improves low-resource translation",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1604.02201",
        "quell_titel": "Transfer Learning for Low-Resource Neural Machine Translation",
        "datum_aussage": "2016-04-07",
        "sprache": "en",
        "kontext": "Presenting results on using transfer learning to improve neural machine translation for languages with limited training data"
    },
    {
        "aussage_text": "We build a multi-source machine translation model trained to maximize the probability of a target English string given French and German sources.",
        "aussage_kurz": "Multi-source translation from multiple languages",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1601.00710",
        "quell_titel": "Multi-Source Neural Translation",
        "datum_aussage": "2016-01-04",
        "sprache": "en",
        "kontext": "Describing approach to neural machine translation using multiple source languages simultaneously"
    },
    {
        "aussage_text": "AutoAugment is a simple procedure to automatically search for improved data augmentation policies.",
        "aussage_kurz": "AutoAugment automates data augmentation",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/1805.09501",
        "quell_titel": "AutoAugment: Learning Augmentation Policies from Data",
        "datum_aussage": "2018-05-24",
        "sprache": "en",
        "kontext": "Introducing automated approach to finding optimal data augmentation strategies, applying NAS principles to data preprocessing"
    },
    {
        "aussage_text": "We scaled a sparse model to 269B parameters with computational cost comparable to a 32B dense encoder-decoder Transformer.",
        "aussage_kurz": "ST-MoE scales to 269B parameters efficiently",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/2202.08906",
        "quell_titel": "ST-MoE: Designing Stable and Transferable Sparse Expert Models",
        "datum_aussage": "2022-02-17",
        "sprache": "en",
        "kontext": "Describing breakthrough in Mixture of Experts models achieving massive scale with manageable compute requirements"
    },
    {
        "aussage_text": "For the first time achieved state-of-the-art performance in transfer learning across diverse tasks including reasoning, summarization, closed book question answering.",
        "aussage_kurz": "ST-MoE achieves SOTA on diverse tasks",
        "modus": "schriftlich",
        "quell_link": "https://arxiv.org/abs/2202.08906",
        "quell_titel": "ST-MoE: Designing Stable and Transferable Sparse Expert Models",
        "datum_aussage": "2022-02-17",
        "sprache": "en",
        "kontext": "Highlighting the broad capabilities achieved by sparse expert models across multiple NLP benchmarks"
    },
    {
        "aussage_text": "GPT-4 incorporates an additional safety reward signal during RLHF training to reduce harmful outputs by training the model to refuse requests for such content.",
        "aussage_kurz": "GPT-4 uses safety reward in RLHF",
        "modus": "schriftlich",
        "quell_link": "https://cdn.openai.com/papers/gpt-4.pdf",
        "quell_titel": "GPT-4 Technical Report",
        "datum_aussage": "2023-03-15",
        "sprache": "en",
        "kontext": "From GPT-4 technical report describing safety measures in post-training, area led by Zoph's team"
    }
]

# HANDLUNGEN - Career moves and actions
handlungen = [
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Thinking Machines Lab with Mira Murati and John Schulman as CTO, AI startup focused on innovative AI research",
        "datum_handlung": "2025-02-01",
        "quell_link": "https://en.wikipedia.org/wiki/Thinking_Machines_Lab",
        "quell_titel": "Thinking Machines Lab - Wikipedia",
        "kontext": "Founded AI startup after leaving OpenAI, joining former colleagues Mira Murati and John Schulman"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Left OpenAI as VP of Research (Post-Training) after helping build ChatGPT and the post-training team from scratch",
        "datum_handlung": "2024-09-25",
        "quell_link": "https://x.com/barret_zoph/status/1839095143397515452",
        "quell_titel": "Barret Zoph departure announcement on X",
        "kontext": "Departed OpenAI along with CTO Mira Murati and Chief Research Officer Bob McGrew in coordinated executive exodus"
    },
    {
        "handlung_typ": "entlassung",
        "beschreibung": "Terminated as CTO of Thinking Machines Lab by Mira Murati for alleged unethical conduct involving sharing confidential information and undisclosed workplace relationship",
        "datum_handlung": "2026-01-14",
        "quell_link": "https://www.benzinga.com/markets/tech/26/01/49925838/barret-zoph-reportedly-fired-from-thinking-machines-by-mira-murati-for-unethical-conduct-immediately-returns-to-openai",
        "quell_titel": "Barret Zoph Reportedly Fired From Thinking Machines",
        "kontext": "Controversial firing after only months at startup, with conflicting accounts about reasons including performance concerns and workplace relationship"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Rejoined OpenAI and appointed to lead enterprise AI sales efforts, heading push into corporate market",
        "datum_handlung": "2026-01-22",
        "quell_link": "https://techcrunch.com/2026/01/22/openai-is-coming-for-those-sweet-enterprise-dollars-in-2026/",
        "quell_titel": "OpenAI is coming for those sweet enterprise dollars in 2026",
        "kontext": "Returned to OpenAI immediately after Thinking Machines departure to lead new enterprise strategy as market share declined"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Joined OpenAI as VP of Research (Post-Training), building post-training team with John Schulman right before ChatGPT launch",
        "datum_handlung": "2022-09-01",
        "quell_link": "https://x.com/barret_zoph/status/1839095143397515452",
        "quell_titel": "Barret Zoph on X - career history",
        "kontext": "Joined OpenAI from Google Brain to lead critical post-training research, instrumental in ChatGPT development"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Started as Research Scientist at Google Brain, working on Neural Architecture Search and AutoML",
        "datum_handlung": "2016-01-01",
        "quell_link": "https://www.linkedin.com/in/barret-zoph-65990543/",
        "quell_titel": "Barret Zoph LinkedIn",
        "kontext": "Began career at Google Brain as resident/postdoc, collaborating with Quoc Le on foundational NAS research"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Published Neural Architecture Search with Reinforcement Learning, foundational paper establishing automated neural network design as viable field",
        "datum_handlung": "2016-11-01",
        "quell_link": "https://arxiv.org/abs/1611.01578",
        "quell_titel": "Neural Architecture Search with Reinforcement Learning",
        "kontext": "Breakthrough paper with Quoc Le that initiated AutoML revolution, showing RL could design networks matching human experts"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Published NASNet paper demonstrating transferable architecture search from CIFAR-10 to ImageNet with state-of-the-art results",
        "datum_handlung": "2017-07-21",
        "quell_link": "https://arxiv.org/abs/1707.07012",
        "quell_titel": "Learning Transferable Architectures for Scalable Image Recognition",
        "kontext": "Major advancement showing architectures designed on small datasets could transfer to large-scale problems, achieving 82.7% top-1 ImageNet accuracy"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Published AutoAugment paper introducing automated data augmentation policy search, achieving state-of-the-art on CIFAR-10 (1.48% error)",
        "datum_handlung": "2018-05-24",
        "quell_link": "https://arxiv.org/abs/1805.09501",
        "quell_titel": "AutoAugment: Learning Augmentation Policies from Data",
        "kontext": "Extended NAS principles to data preprocessing, automatically discovering augmentation strategies better than hand-designed approaches"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Published ST-MoE paper on stable sparse expert models, scaling to 269B parameters with efficiency of 32B dense model",
        "datum_handlung": "2022-02-17",
        "quell_link": "https://arxiv.org/abs/2202.08906",
        "quell_titel": "ST-MoE: Designing Stable and Transferable Sparse Expert Models",
        "kontext": "Major contribution to efficient large language models using Mixture of Experts, achieving SOTA on diverse NLP tasks"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Led post-training team that developed and launched ChatGPT, implementing RLHF and alignment techniques for safe deployment",
        "datum_handlung": "2022-11-30",
        "quell_link": "https://hai.stanford.edu/events/john-schulman-and-barret-zoph-chatgpt-and-art-post-training",
        "quell_titel": "ChatGPT and the Art of Post-Training",
        "kontext": "As VP of Post-Training at OpenAI, led team that made ChatGPT safe and useful through reinforcement learning from human feedback"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Contributed to GPT-4 post-training and alignment using RLHF with safety reward signals",
        "datum_handlung": "2023-03-14",
        "quell_link": "https://cdn.openai.com/papers/gpt-4.pdf",
        "quell_titel": "GPT-4 Technical Report",
        "kontext": "Post-training team led by Zoph implemented advanced alignment techniques resulting in OpenAI's best-ever results on factuality and safety"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Became Angel Investor focusing on AI companies",
        "datum_handlung": "2022-01-01",
        "quell_link": "https://www.linkedin.com/in/barret-zoph-65990543/",
        "quell_titel": "Barret Zoph LinkedIn",
        "kontext": "Started angel investing in AI startups while at OpenAI, leveraging expertise in ML/AI research"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Gave Stanford HAI talk with John Schulman on ChatGPT and the Art of Post-Training, sharing insights on alignment and RLHF",
        "datum_handlung": "2024-11-15",
        "quell_link": "https://hai.stanford.edu/events/john-schulman-and-barret-zoph-chatgpt-and-art-post-training",
        "quell_titel": "John Schulman and Barret Zoph | ChatGPT and the Art of Post-Training",
        "kontext": "Public presentation at Stanford discussing technical details of post-training methods, challenges, and experience building ChatGPT"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Thinking Machines Lab raised $2 billion seed round led by Andreessen Horowitz with valuation of $12 billion from Nvidia, AMD, Cisco, Jane Street",
        "datum_handlung": "2025-07-01",
        "quell_link": "https://en.wikipedia.org/wiki/Thinking_Machines_Lab",
        "quell_titel": "Thinking Machines Lab - Wikipedia",
        "kontext": "Historic seed funding round for Zoph's AI startup, one of largest venture rounds ever despite no product or revenue"
    }
]

# Insert Aussagen
print(f"Füge {len(aussagen)} Aussagen ein...")
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

# Insert Handlungen
print(f"Füge {len(handlungen)} Handlungen ein...")
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

# Commit und schließen
conn.commit()
conn.close()

print(f"\nErfolgreich abgeschlossen:")
print(f"- {len(aussagen)} Aussagen eingefügt")
print(f"- {len(handlungen)} Handlungen eingefügt")
print(f"- Gesamt: {len(aussagen) + len(handlungen)} Einträge für Barret Zoph (person_id={person_id})")
