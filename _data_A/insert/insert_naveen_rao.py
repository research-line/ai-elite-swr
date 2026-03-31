import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 72  # Naveen Rao

# AUSSAGEN
aussagen = [
    {
        "aussage_text": "The term 'AGI' might have done more damage to the AI field than anything else. Human (or any animal intelligence) is NOT general; it's very specifically constrained. Generality would require too many observations to fit to; constrained intelligence learns the right stuff to.",
        "aussage_kurz": "AGI-Begriff schadet AI-Feld, menschliche Intelligenz ist nicht generell",
        "modus": "muendlich",
        "quell_link": "https://x.com/NaveenGRao/status/1846029025069629717",
        "quell_titel": "Naveen Rao on X/Twitter about AGI",
        "datum_aussage": "2024-10-14",
        "sprache": "en",
        "kontext": "Twitter/X statement criticizing the concept of Artificial General Intelligence"
    },
    {
        "aussage_text": "AI is the next evolution of humanity if we reinvent the computer itself. AI lets us collaborate, understand each other, and understand the world in much deeper ways.",
        "aussage_kurz": "KI ist nächste Evolution der Menschheit bei Hardware-Neuerfindung",
        "modus": "muendlich",
        "quell_link": "https://x.com/a16z/status/1998875475767406685",
        "quell_titel": "a16z on X featuring Naveen Rao",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Statement about Unconventional AI's mission and vision"
    },
    {
        "aussage_text": "You can't make rules and laws before you understand the problem. Regulating generative AI is like setting traffic laws in 1850 without knowing what cars, accidents, or liability look like.",
        "aussage_kurz": "Keine Regulierung vor Problemverständnis",
        "modus": "muendlich",
        "quell_link": "https://ashugarg.substack.com/p/how-to-shape-the-future-of-ai-naveen",
        "quell_titel": "How to Shape the Future of AI (Naveen Rao, VP of Generative AI at Databricks)",
        "datum_aussage": "2024-01-10",
        "sprache": "en",
        "kontext": "Discussion on AI regulation and governance"
    },
    {
        "aussage_text": "It's literally impossible to understand intelligence in a purely reductionist format because the complexity is too high and the amount of effort required would be many orders of magnitude more complicated than what you're trying to understand.",
        "aussage_kurz": "Intelligenz nicht rein reduktionistisch verstehbar",
        "modus": "muendlich",
        "quell_link": "https://voicesinai.com/episode/episode-79-a-conversation-with-naveen-rao/",
        "quell_titel": "Episode 79: A Conversation with Naveen Rao – Voices in AI",
        "datum_aussage": "2018-06-15",
        "sprache": "en",
        "kontext": "Discussion on philosophy of intelligence and AI"
    },
    {
        "aussage_text": "Natural learning systems never used numerics. They didn't simulate the dynamics of learning. They use the intrinsic physics of whatever substrate they're on to build a learning system.",
        "aussage_kurz": "Natürliche Lernsysteme nutzen Physik des Substrats, nicht Simulation",
        "modus": "muendlich",
        "quell_link": "https://www.theregister.com/2025/12/08/unconventional_ai/",
        "quell_titel": "Bezos-backed Unconventional AI addresses datacenter power",
        "datum_aussage": "2025-12-08",
        "sprache": "en",
        "kontext": "Explaining Unconventional AI's analog computing approach"
    },
    {
        "aussage_text": "We are currently having a 'Napster moment' for generative AI. Napster clearly demonstrated demand for streaming music, but it did get shut down until someone figured out the incentives, how to go back and remunerate the creators the right way.",
        "aussage_kurz": "KI hat 'Napster-Moment' wegen Copyright-Fragen",
        "modus": "muendlich",
        "quell_link": "https://finance.yahoo.com/news/generative-ai-needs-tools-avoid-090002361.html",
        "quell_titel": "Generative AI needs tools to avoid copyright infringement, Databricks' Naveen Rao says",
        "datum_aussage": "2023-10-15",
        "sprache": "en",
        "kontext": "Warning about copyright challenges in AI training data"
    },
    {
        "aussage_text": "AI is intrinsically linked to hardware and hardware is intrinsically linked to power. We can't scale beyond a certain number of inferences per unit time because of the energy problem. We can't produce that much more energy in the next 10 years.",
        "aussage_kurz": "Energie-Problem limitiert KI-Skalierung fundamental",
        "modus": "muendlich",
        "quell_link": "https://lsvp.com/stories/investing-in-unconventional-ai-biology-scale-efficiency-for-the-ai-era/",
        "quell_titel": "Investing In Unconventional AI: Biology-Scale Efficiency For The AI Era",
        "datum_aussage": "2025-12-10",
        "sprache": "en",
        "kontext": "Explaining energy constraints for AI development"
    },
    {
        "aussage_text": "These are nonlinear dynamics of circuits. That's inherently an analog thing. All devices are analog, even 'digital' devices. We just engineer those circuits to behave digitally, but we're largely erasing the richness of what those circuits can do by making them one and zero.",
        "aussage_kurz": "Digitale Beschränkung löscht Reichtum analoger Schaltkreise",
        "modus": "muendlich",
        "quell_link": "https://www.hpcwire.com/bigdatawire/2025/12/11/unconventional-ai-wants-to-solve-ai-scaling-crunch-with-analog-chips-will-it-work/",
        "quell_titel": "Unconventional AI Wants to Solve AI Scaling Crunch with Analog Chips",
        "datum_aussage": "2025-12-11",
        "sprache": "en",
        "kontext": "Technical explanation of analog vs digital computing approach"
    },
    {
        "aussage_text": "Current AI systems excel at pattern matching and probability estimation but fall short of true reasoning capabilities, lacking the ability to break down human intention into meaningful sub-goals or simulate potential outcomes before acting.",
        "aussage_kurz": "Aktuelle KI-Systeme fehlt echte Reasoning-Fähigkeit",
        "modus": "muendlich",
        "quell_link": "https://www.oreateai.com/blog/naveen-rao-redefining-ai-through-unconventional-computing/a7856a23cd78c212a41dc4ece1d37401",
        "quell_titel": "Naveen Rao: Redefining AI Through Unconventional Computing",
        "datum_aussage": "2025-01-20",
        "sprache": "en",
        "kontext": "Critique of current AI capabilities"
    },
    {
        "aussage_text": "If we want true advancements in AI—especially towards achieving Artificial General Intelligence—we must explore models based on dynamics and causality rather than sticking rigidly with existing frameworks like Transformers or GPUs alone.",
        "aussage_kurz": "AGI erfordert Kausalitäts-Modelle statt nur Transformer",
        "modus": "muendlich",
        "quell_link": "https://www.oreateai.com/blog/naveen-rao-redefining-ai-through-unconventional-computing/a7856a23cd78c212a41dc4ece1d37401",
        "quell_titel": "Naveen Rao: Redefining AI Through Unconventional Computing",
        "datum_aussage": "2025-01-20",
        "sprache": "en",
        "kontext": "Vision for future AI development beyond current paradigms"
    },
    {
        "aussage_text": "I place the probability of achieving AGI in the next three years as virtually zero, estimating maybe a 50% or 30% chance in 10 years, and by 30 years, a 90% chance range.",
        "aussage_kurz": "AGI-Wahrscheinlichkeit: 3 Jahre ~0%, 10 Jahre 30-50%, 30 Jahre 90%",
        "modus": "muendlich",
        "quell_link": "https://ashugarg.substack.com/p/how-to-shape-the-future-of-ai-naveen",
        "quell_titel": "How to Shape the Future of AI (Naveen Rao, VP of Generative AI at Databricks)",
        "datum_aussage": "2024-01-10",
        "sprache": "en",
        "kontext": "Timeline predictions for achieving AGI"
    },
    {
        "aussage_text": "The real danger lies not in rogue AI, but in hastily constraining a technology that we don't yet understand.",
        "aussage_kurz": "Gefahr ist vorschnelle Regulierung, nicht Schurken-KI",
        "modus": "muendlich",
        "quell_link": "https://ashugarg.substack.com/p/how-to-shape-the-future-of-ai-naveen",
        "quell_titel": "How to Shape the Future of AI (Naveen Rao, VP of Generative AI at Databricks)",
        "datum_aussage": "2024-01-10",
        "sprache": "en",
        "kontext": "Warning against premature AI regulation"
    },
    {
        "aussage_text": "Together with Databricks, we will empower enterprise customers to more securely and cost-effectively build LLMs and generative AI with their own data.",
        "aussage_kurz": "Demokratisierung von LLMs für Unternehmen mit eigenen Daten",
        "modus": "schriftlich",
        "quell_link": "https://www.databricks.com/company/newsroom/press-releases/databricks-signs-definitive-agreement-acquire-mosaicml-leading-generative-ai-platform",
        "quell_titel": "Databricks Signs Definitive Agreement to Acquire MosaicML",
        "datum_aussage": "2023-06-26",
        "sprache": "en",
        "kontext": "Announcement of MosaicML acquisition by Databricks"
    },
    {
        "aussage_text": "I consider artificial intelligence to be 'artificial' simply because we built it, and believe intelligence can be implemented on any kind of substrate, not just biological.",
        "aussage_kurz": "Intelligenz kann auf jedem Substrat implementiert werden",
        "modus": "muendlich",
        "quell_link": "https://voicesinai.com/episode/episode-79-a-conversation-with-naveen-rao/",
        "quell_titel": "Episode 79: A Conversation with Naveen Rao – Voices in AI",
        "datum_aussage": "2018-06-15",
        "sprache": "en",
        "kontext": "Philosophy on substrate-independence of intelligence"
    },
    {
        "aussage_text": "Open-source models will eventually overtake closed models, just as Linux did with Solaris.",
        "aussage_kurz": "Open-Source-KI wird proprietäre Modelle überholen",
        "modus": "muendlich",
        "quell_link": "https://venturebeat.com/ai/mosaicml-ceo-naveen-rao-on-how-to-democratize-generative-ai-and-why-he-sold-to-databricks-for-1-3b",
        "quell_titel": "MosaicML CEO Naveen Rao on how to democratize generative AI",
        "datum_aussage": "2023-07-19",
        "sprache": "en",
        "kontext": "Prediction about the future of open-source AI"
    },
    {
        "aussage_text": "Can we provide a software interface to the inherent physics of the silicon? In essence, we will run the neural network on the physics directly rather than simulating some physical system.",
        "aussage_kurz": "Neuronale Netze direkt auf Physik laufen lassen statt simulieren",
        "modus": "muendlich",
        "quell_link": "https://www.theregister.com/2025/12/08/unconventional_ai/",
        "quell_titel": "Bezos-backed Unconventional AI addresses datacenter power",
        "datum_aussage": "2025-12-08",
        "sprache": "en",
        "kontext": "Technical vision for Unconventional AI's computing approach"
    },
    {
        "aussage_text": "My goal is to create a computer that is as efficient as biology.",
        "aussage_kurz": "Ziel: Computer so effizient wie Biologie",
        "modus": "schriftlich",
        "quell_link": "https://techfundingnews.com/former-databricks-ai-chiefs-unconventional-ai-raises-475m-at-4-5b-valuation-to-redesign-computing/",
        "quell_titel": "Unconventional AI raises $475M at $4.5B valuation",
        "datum_aussage": "2025-10-15",
        "sprache": "en",
        "kontext": "Statement on X/Twitter about Unconventional AI mission"
    },
    {
        "aussage_text": "Current AI, while powerful, falls short of genuine intelligence, often making stupid errors because it lacks a true understanding of causality. The ability to inherently understand and model causality, rather than merely simulate it, is a critical step towards AGI.",
        "aussage_kurz": "Echte KI braucht Kausalitätsverständnis, nicht nur Simulation",
        "modus": "muendlich",
        "quell_link": "https://www.startuphub.ai/ai-news/ai-video/2025/rethinking-ais-foundations-the-analog-path-to-agi/",
        "quell_titel": "Rethinking AI's Foundations: The Analog Path to AGI",
        "datum_aussage": "2025-01-25",
        "sprache": "en",
        "kontext": "Critique of current AI and path to AGI"
    },
    {
        "aussage_text": "The funding is a first installment toward the goal of up to $1 billion for the round. Within the next three to four years, this growth will be constrained by the global energy supply.",
        "aussage_kurz": "Globale Energieversorgung wird KI-Wachstum in 3-4 Jahren limitieren",
        "modus": "muendlich",
        "quell_link": "https://www.bloomberg.com/news/articles/2025-12-08/ai-computer-startup-hits-4-5-billion-valuation-in-seed-round",
        "quell_titel": "AI Computer Startup Hits $4.5 Billion Valuation in Seed Round - Bloomberg",
        "datum_aussage": "2025-12-08",
        "sprache": "en",
        "kontext": "Discussion of Unconventional AI funding and energy constraints"
    }
]

# HANDLUNGEN
handlungen = [
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Nervana Systems, a deep learning chip startup focused on AI accelerators for data centers",
        "datum_handlung": "2014-02-01",
        "quell_link": "https://www.ark-invest.com/podcast/ep84-naveen-rao-nervana-systems",
        "quell_titel": "The First AI Chip Startup with Naveen Rao, Nervana Systems",
        "kontext": "Founded after leaving Qualcomm neuromorphic research position, served as CEO"
    },
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Intel acquired Nervana Systems for approximately $408 million; Rao became VP and GM of Intel's AI Products Group",
        "datum_handlung": "2016-08-09",
        "quell_link": "https://techcrunch.com/2016/08/09/intel-buys-deep-learning-startup-nervana-systems-for-a-reported-350-million/",
        "quell_titel": "Intel buys deep learning startup Nervana Systems",
        "kontext": "Intel's strategic move into AI chip market, acquisition valued at $350-408 million"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Appointed to Square's Board of Directors as AI expert while serving as Intel VP of AI Products",
        "datum_handlung": "2017-09-21",
        "quell_link": "https://squareup.com/us/en/press/square-names-naveen-rao-leader-in-artificial-intelligence-to-board-of-directors",
        "quell_titel": "Square Names Naveen Rao, Leader in Artificial Intelligence, to Board of Directors",
        "kontext": "Board appointment during tenure at Intel to provide AI expertise"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Departed Intel after company chose Habana Labs chips over Nervana technology; last day March 10, 2020",
        "datum_handlung": "2020-02-26",
        "quell_link": "https://medium.com/syncedreview/intel-ai-gm-naveen-rao-leaves-after-habana-chosen-over-nervana-4ff526793b6c",
        "quell_titel": "Intel AI GM Naveen Rao Leaves After Habana Chosen Over Nervana",
        "kontext": "Intel discontinued Nervana NNP-T chip in favor of $2B Habana acquisition"
    },
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded MosaicML with Hanlin Tang, focused on democratizing generative AI model training",
        "datum_handlung": "2021-01-15",
        "quell_link": "https://www.hpcwire.com/2021/10/15/mosaicml-led-by-naveen-rao-comes-out-of-stealth-aiming-to-ease-ml-training/",
        "quell_titel": "MosaicML, Led by Naveen Rao, Comes Out of Stealth",
        "kontext": "Founded after leaving Intel, served as CEO, company launched publicly in October 2021"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Released MPT-7B open-source language model with 7 billion parameters and 64,000 token context window",
        "datum_handlung": "2023-05-05",
        "quell_link": "https://www.bigdatawire.com/2023/07/06/what-is-mosaicml-and-why-is-databricks-buying-it-for-1-3b/",
        "quell_titel": "What Is MosaicML, and Why Is Databricks Buying It For $1.3B?",
        "kontext": "Open-source LLM achieved over 3.3 million downloads, commercially licensed"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Released MPT-30B model, significantly more powerful than MPT-7B, outperforming original GPT-3",
        "datum_handlung": "2023-06-01",
        "quell_link": "https://www.bigdatawire.com/2023/07/06/what-is-mosaicml-and-why-is-databricks-buying-it-for-1-3b/",
        "quell_titel": "What Is MosaicML, and Why Is Databricks Buying It For $1.3B?",
        "kontext": "Expanded MosaicML's open-source model offerings with larger parameter model"
    },
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Databricks acquired MosaicML for $1.3 billion including retention packages; Rao became VP of Generative AI at Databricks",
        "datum_handlung": "2023-06-26",
        "quell_link": "https://fortune.com/2023/07/19/databricks-mosaicml-ai-acquisition/",
        "quell_titel": "Behind the scenes of Databricks' $1.3 billion MosaicML deal",
        "kontext": "One of largest AI acquisitions of 2023; Rao and Databricks CEO met at March 30 conference"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launched open-source DBRX language model at Databricks, continuing democratization mission",
        "datum_handlung": "2024-03-15",
        "quell_link": "https://venturebeat.com/ai/mosaicml-ceo-naveen-rao-on-how-to-democratize-generative-ai-and-why-he-sold-to-databricks-for-1-3b",
        "quell_titel": "MosaicML CEO Naveen Rao on how to democratize generative AI",
        "kontext": "Continued open-source AI development at Databricks after MosaicML acquisition"
    },
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Departed Databricks as VP of AI to focus on founding new hardware startup; continues as advisor",
        "datum_handlung": "2025-09-12",
        "quell_link": "https://www.infoworld.com/article/4056636/databricks-at-a-crossroads-can-its-ai-strategy-prevail-without-naveen-rao.html",
        "quell_titel": "Databricks at a crossroads: Can its AI strategy prevail without Naveen Rao?",
        "kontext": "Left to launch Unconventional AI focused on energy-efficient computing"
    },
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Founded Unconventional AI, neuromorphic computing startup focused on analog AI chips for biology-scale efficiency",
        "datum_handlung": "2025-10-01",
        "quell_link": "https://techcrunch.com/2025/10/03/sources-naveen-raos-new-ai-hardware-startup-targets-5b-valuation-with-backing-from-a16z/",
        "quell_titel": "Naveen Rao's new AI hardware startup targets $5B valuation",
        "kontext": "Stealth hardware startup aiming to solve AI energy crisis with brain-inspired computing"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Invested $10 million of personal funds into Unconventional AI seed round",
        "datum_handlung": "2025-12-08",
        "quell_link": "https://techcrunch.com/2025/12/09/unconventional-ai-confirms-its-massive-475m-seed-round/",
        "quell_titel": "Unconventional AI confirms its massive $475M seed round",
        "kontext": "Personal investment alongside institutional funding round"
    },
    {
        "handlung_typ": "kauf",
        "beschreibung": "Raised $475 million seed round at $4.5 billion valuation for Unconventional AI, led by Andreessen Horowitz and Lightspeed",
        "datum_handlung": "2025-12-09",
        "quell_link": "https://techcrunch.com/2025/12/09/unconventional-ai-confirms-its-massive-475m-seed-round/",
        "quell_titel": "Unconventional AI confirms its massive $475M seed round",
        "kontext": "One of largest seed rounds in history; includes Jeff Bezos, a16z, Lightspeed, Lux Capital, DCVC; targets $1B total"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Databricks invested in Unconventional AI as strategic partner alongside venture capital firms",
        "datum_handlung": "2025-12-09",
        "quell_link": "https://analyticsindiamag.com/ai-news-updates/databricks-invests-in-naveen-raos-new-ai-hardware-startup/",
        "quell_titel": "Databricks Invests in Naveen Rao's New AI Hardware Startup",
        "kontext": "Former employer becomes investor and strategic partner in new venture"
    }
]

# Aussagen einfügen
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen
        (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
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

# Handlungen einfügen
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen
        (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
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

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print(f"\nGESAMT: {len(aussagen)} Aussagen + {len(handlungen)} Handlungen = {len(aussagen) + len(handlungen)} Einträge für Naveen Rao (person_id={person_id})")
