import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 89  # Jimmy Ba

# AUSSAGEN (Englische Originalzitate)
aussagen = [
    # Weltbild & AI Future
    (person_id, "One day there will be humanlike learning machines capable of understanding our cultural norms and the nuances in our human values.",
     "Humanlike learning machines understanding cultural norms", "schriftlich",
     "https://tech.yahoo.com/ai/articles/jimmy-ba-founding-member-elon-090002716.html",
     "Jimmy Ba, founding member of Elon Musk's xAI", None, "en",
     "Vision for future AI systems"),

    (person_id, "The technology available needs to consider the complexity of ethics, privacy, fairness, and good versus evil.",
     "AI must consider ethics, privacy, fairness", "muendlich",
     "https://www.ted.com/talks/jimmy_ba_the_need_for_humanity_in_ai",
     "TEDx Talk: The need for humanity in AI", "2020-12-01", "en",
     "2020 TEDx Talk on ethical AI development"),

    (person_id, "We are heading to an age of 100x productivity with the right tools.",
     "Age of 100x productivity with right tools", "schriftlich",
     "https://officechai.com/ai/xai-co-founder-jimmy-ba-quits-6-of-12-co-founders-have-now-left/",
     "xAI Co-founder Jimmy Ba Quits", "2026-02-11", "en",
     "Statement upon xAI departure about AI productivity"),

    (person_id, "Recursive self improvement loops likely go live in the next 12mo.",
     "Recursive self-improvement loops in next 12 months", "schriftlich",
     "https://officechai.com/ai/xai-co-founder-jimmy-ba-quits-6-of-12-co-founders-have-now-left/",
     "xAI Co-founder Jimmy Ba Quits", "2026-02-11", "en",
     "Prediction about AI recursive self-improvement upon leaving xAI"),

    (person_id, "2026 is gonna be insane and likely the busiest (and most consequential) year for the future of our species.",
     "2026 most consequential year for species", "schriftlich",
     "https://www.cnbc.com/2026/02/10/musks-xai-loses-second-co-founder-in-two-days-as-jimmy-ba-departs.html",
     "Musk's xAI loses second co-founder as Jimmy Ba departs", "2026-02-11", "en",
     "Departure statement from xAI"),

    (person_id, "It's time to recalibrate my gradient on the big picture.",
     "Time to recalibrate gradient on big picture", "schriftlich",
     "https://www.cnbc.com/2026/02/10/musks-xai-loses-second-co-founder-in-two-days-as-jimmy-ba-departs.html",
     "Musk's xAI loses second co-founder as Jimmy Ba departs", "2026-02-11", "en",
     "Metaphorical statement about leaving xAI to reassess priorities"),

    # Research Goals
    (person_id, "How can we build general problem-solving machines with human-like efficiency and adaptability?",
     "Build problem-solving machines with human-like efficiency", "schriftlich",
     "https://globalexcellenceinitiative.ca/winner/jimmy-ba/",
     "Jimmy Ba - Global Excellence Initiative", None, "en",
     "Long-term research goal statement"),

    # xAI Departure
    (person_id, "Enormous thanks to @elonmusk for bringing us together on this incredible journey. So proud of what the xAI team has done and will continue to stay close as a friend of the team.",
     "Thanks to Musk for xAI journey", "schriftlich",
     "https://www.tipranks.com/news/xai-co-founders-tony-wu-jimmy-ba-depart-amid-mass-exodus",
     "xAI Co-Founders Tony Wu, Jimmy Ba Depart", "2026-02-10", "en",
     "Departure message from xAI"),

    (person_id, "Grateful to have helped cofound at the start.",
     "Grateful to have helped cofound xAI", "schriftlich",
     "https://www.cnbc.com/2026/02/10/musks-xai-loses-second-co-founder-in-two-days-as-jimmy-ba-departs.html",
     "Musk's xAI loses second co-founder as Jimmy Ba departs", "2026-02-10", "en",
     "Statement about role as xAI co-founder"),

    # Technical Contributions (implied statements through work)
    (person_id, "Large Language Models (LLMs) based on the Transformer architecture have achieved remarkable success, yet their core processing mechanisms remain largely static after training. This static nature limits their ability to dynamically adapt their processing strategy based on nuanced contextual cues, task demands, or desired operational modes.",
     "LLMs lack dynamic adaptability after training", "schriftlich",
     "https://research.com/u/jimmy-ba",
     "2026 Jimmy Ba: Computer Science Researcher", "2025-01-01", "en",
     "From 2025 NCNs paper on LLM limitations"),
]

# HANDLUNGEN
handlungen = [
    # Gründungen
    (person_id, "gruendung", "Co-founded xAI with Elon Musk and 11 other researchers to compete against OpenAI and Google",
     "2023-07-01", "https://www.britannica.com/money/xAI",
     "XAI - Britannica Money", "Musk launched xAI in 2023 to understand the true nature of the universe"),

    # Rücktritte
    (person_id, "ruecktritt", "Resigned as co-founder from xAI after leading research, safety, and enterprise efforts",
     "2026-02-10", "https://www.cnbc.com/2026/02/10/musks-xai-loses-second-co-founder-in-two-days-as-jimmy-ba-departs.html",
     "Musk's xAI loses second co-founder as Jimmy Ba departs",
     "Left xAI following tensions over AI model performance demands; became 6th of 12 co-founders to depart"),

    # Einstellungen/Beförderungen
    (person_id, "einstellung", "Joined University of Toronto Computer Science Department as Assistant Professor",
     "2018-07-01", "https://jimmylba.github.io/",
     "Jimmy Ba | home page", "Appointed Assistant Professor after completing PhD under Geoffrey Hinton"),

    (person_id, "einstellung", "Became CIFAR AI Chair at Vector Institute",
     "2018-07-01", "https://medium.com/@1528371521zx/jimmy-lei-ba-3855139f2857",
     "Jimmy Lei Ba - Medium", "Appointed as Canada CIFAR AI Chair"),

    (person_id, "einstellung", "Promoted to Associate Professor with tenure at University of Toronto",
     "2024-07-01", "https://web.cs.toronto.edu/news-events/news/tag/Jimmy+Ba",
     "Jimmy Ba News - UofT CS", "Promotion effective July 1, 2024"),

    # Produktlaunches/Research
    (person_id, "produktlaunch", "Co-authored Adam optimizer algorithm with Diederik Kingma",
     "2014-12-01", "https://arxiv.org/abs/1412.6980",
     "Adam: A Method for Stochastic Optimization",
     "Published at ICLR 2015; became standard optimization algorithm training virtually every LLM"),

    (person_id, "produktlaunch", "Published Layer Normalization paper with Geoffrey Hinton and Jamie Ryan Kiros",
     "2016-07-01", "https://arxiv.org/abs/1607.06450",
     "Layer Normalization", "Published at NIPS 2016; became core building block in transformer architectures"),

    (person_id, "produktlaunch", "Co-authored Lookahead Optimizer paper improving SGD and Adam performance",
     "2019-07-01", "https://arxiv.org/abs/1907.08610",
     "Lookahead Optimizer: k steps forward, 1 step back",
     "Published at NeurIPS 2019; improved generalization and stability of fast optimizers"),

    (person_id, "produktlaunch", "Published research on Neuromodulatory Control Networks (NCNs) for dynamic LLM processing",
     "2025-01-01", "https://github.com/Mmorgan-ML/Neuromodulatory-Control-Networks",
     "Neuromodulatory Control Networks - GitHub",
     "Biologically-inspired architecture for LLMs to dynamically adapt processing strategies"),

    (person_id, "produktlaunch", "Contributed critical research to xAI's Grok version 4 AI models",
     "2024-01-01", "https://www.businesstoday.in/technology/news/story/elon-musks-xai-sees-co-founder-exit-jimmy-ba-bids-farewell-515605-2026-02-11",
     "Elon Musk's xAI sees co founder exit", "Led research efforts at xAI influencing Grok 4 development"),

    # Auszeichnungen (als sonstige Handlung)
    (person_id, "sonstiges", "Received Facebook PhD Fellowship in Machine Learning",
     "2016-01-01", "https://jimmylba.github.io/",
     "Jimmy Ba | home page", "Facebook Graduate Fellowship 2016; first Canadian student recipient"),

    (person_id, "sonstiges", "Awarded Sloan Research Fellowship",
     "2023-02-01", "https://web.cs.toronto.edu/news-events/news/sloan-research-fellowships-awarded-to-jimmy-ba-and-sushant-sachdeva",
     "Sloan Research Fellowships awarded to Jimmy Ba",
     "Prestigious fellowship for early-career researchers showing exceptional creativity and innovation"),

    (person_id, "sonstiges", "Received Amazon Research Award",
     "2020-01-01", "https://www.amazon.science/research-awards/recipients/jimmy-ba",
     "Jimmy Ba - Amazon Science", "Amazon worldwide Research Award for deep learning research"),

    # Akademische Tätigkeiten
    (person_id, "sonstiges", "Completed PhD under supervision of Geoffrey Hinton at University of Toronto",
     "2017-01-01", "https://jimmylba.github.io/cv/cv.pdf",
     "Jimmy Ba CV", "PhD completed 2017 after starting in 2011"),

    (person_id, "sonstiges", "Submitted work to ICLR 2025 conference",
     "2025-01-01", "https://openreview.net/profile?id=~Jimmy_Ba1",
     "Jimmy Ba - OpenReview", "Active research submissions to major ML conferences"),
]

# Aussagen einfügen
print(f"Füge {len(aussagen)} Aussagen ein...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)

# Handlungen einfügen
print(f"Füge {len(handlungen)} Handlungen ein...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)

# Änderungen speichern
conn.commit()

# Statistik ausgeben
cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (person_id,))
anzahl_aussagen = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (person_id,))
anzahl_handlungen = cursor.fetchone()[0]

print(f"\n=== ERFOLGREICH EINGEFÜGT ===")
print(f"Person ID: {person_id} (Jimmy Ba)")
print(f"Aussagen: {anzahl_aussagen}")
print(f"Handlungen: {anzahl_handlungen}")
print(f"Gesamt: {anzahl_aussagen + anzahl_handlungen}")

conn.close()
