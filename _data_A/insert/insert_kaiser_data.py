import sqlite3
import os

# Datenbankpfad
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Person ID für Lukasz Kaiser
person_id = 67

# AUSSAGEN - 18 Stück
aussagen = [
    # 1
    (person_id,
     "When neural networks first came out, it's built for image recognition to process inputs with the same dimension of pixels. Sentences are not the same as images.",
     "Neural networks built for image recognition, not sentences",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5: Hear 'First-Principles Thinking About Large Models' by Lukasz, an OpenAI Scientist",
     None,
     "en",
     "Discussion on the limitations of early neural networks for NLP tasks"),

    # 2
    (person_id,
     "Any research you research will be used in different ways, and you cannot control how it will be used. Whether you personally like it or not, and AI is a very capable method and we need to come to terms with the fact that it will be used in ways that we do not want it to be used.",
     "AI research will be used in unintended ways",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     None,
     "en",
     "Statement on AI safety and dual-use concerns"),

    # 3
    (person_id,
     "OpenAI is still a small company, if a lot of employees feel that [we have a certain power].",
     "OpenAI is still a small company",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     None,
     "en",
     "Comment on OpenAI's size and influence"),

    # 4
    (person_id,
     "It's much easier to be a theoretical computer scientist because you can do the same thing for 20 years. You may prove different theorems, but in the big picture, it's the same thing",
     "Theoretical CS easier, same thing for 20 years",
     "muendlich",
     "https://www.emergentbehavior.co/p/2025-10-29-some-confirmations-from-openai",
     "Lukasz Kaiser: No AI Winter Coming",
     None,
     "en",
     "Comparing theoretical computer science to deep learning research"),

    # 5
    (person_id,
     "Every two years, you have to do something completely different.",
     "Deep learning changes completely every two years",
     "muendlich",
     "https://www.emergentbehavior.co/p/2025-10-29-some-confirmations-from-openai",
     "Lukasz Kaiser: No AI Winter Coming",
     None,
     "en",
     "On the rapid pace of change in deep learning"),

    # 6
    (person_id,
     "RNNs are very slow. They can only process one sentence at a time, very sequentially. This doesn't match well with the GPUs and TPUs being built at that time.",
     "RNNs too slow, don't match GPU/TPU architecture",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     None,
     "en",
     "Technical critique that motivated Transformer architecture"),

    # 7
    (person_id,
     "The dream is that at some point, there will be one model, and the one model will have learned to be a good programmer, to be a good conversational agent, to do vision, and to do language.",
     "Dream: one universal model for all tasks",
     "muendlich",
     "https://medium.com/aifrontiers/one-model-to-solve-all-problems-the-story-of-lukasz-kaiser-c015bf696a30",
     "One Model To Solve All Problems: The Story of Lukasz Kaiser",
     None,
     "en",
     "Vision for universal AI systems"),

    # 8
    (person_id,
     "OpenAI is nothing without its people.",
     "OpenAI is nothing without its people",
     "schriftlich",
     "https://iq.wiki/wiki/ukasz-kaiser",
     "Lukasz Kaiser - People in crypto | IQ.wiki",
     "2023-11-20",
     "en",
     "Public statement during OpenAI leadership crisis in November 2023"),

    # 9
    (person_id,
     "The predict the next token using transformers trained on the entire Internet paradigm is dead. Yes, there will be some uplift from scaling, but the real path forward is reasoning.",
     "Next-token prediction paradigm is dead, reasoning is the future",
     "muendlich",
     "https://www.emergentbehavior.co/p/2025-10-29-some-confirmations-from-openai",
     "Lukasz Kaiser: No AI Winter Coming",
     None,
     "en",
     "Prediction about the future direction of AI development"),

    # 10
    (person_id,
     "In 'Training Verifiers to Solve Math Word Problems' (Oct 27 2021), OpenAI had shown naive scaling would mean thousands of trillions of parameters would be required to solve a high school level math dataset.",
     "Naive scaling requires thousands of trillions of parameters",
     "muendlich",
     "https://www.emergentbehavior.co/p/2025-10-29-some-confirmations-from-openai",
     "Lukasz Kaiser: No AI Winter Coming",
     None,
     "en",
     "Explanation of why pure scaling is not viable"),

    # 11
    (person_id,
     "While more data and compute lead to better results, there is an impending data scarcity, and in the future, training with fewer, high-quality retrieved data points will be key to enhancing LLM performance.",
     "Impending data scarcity, quality over quantity",
     "muendlich",
     "https://pathway.com/news/pathway-meetup-2024/",
     "The Future of Large Language Models by Lukasz Kaiser and Jan Chorowski | Pathway",
     "2024-04",
     "en",
     "At Pathway Meetup in San Francisco, April 2024"),

    # 12
    (person_id,
     "The o1 model series is a 'new paradigm' in AI. These models are designed to use 'hidden CoTs' (Chain of Thoughts), an internal reasoning process that allows them to spend more computational effort to think before providing a response.",
     "O1 models use hidden chain-of-thought reasoning",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     "2024-09",
     "en",
     "Description of o1 reasoning models upon launch in September 2024"),

    # 13
    (person_id,
     "This approach enables the models to learn from less data, generalize better, and engage in a form of approximate reasoning compared to previous architectures.",
     "Reasoning models learn from less data, generalize better",
     "muendlich",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     "2024-09",
     "en",
     "Benefits of reasoning model approach"),

    # 14
    (person_id,
     "After RNNs and Transformers, the next evolution will be 'Researchers' – AI systems that can generate new scientific insights with less data. This progression represents not just bigger models, but smarter ones — systems capable of creativity and critical thinking.",
     "Next evolution: AI 'Researchers' with creativity and critical thinking",
     "muendlich",
     "https://tedai-vienna.ted.com/speakers-2025/lukasz-kaiser",
     "Lukasz Kaiser - TEDAI 2026",
     "2025",
     "en",
     "At TEDAI Vienna 2025 on the future of AI"),

    # 15
    (person_id,
     "The concept of 'models doing science' — algorithms that can iterate, simulate, and reason in the same way human researchers do, but at unprecedented speed.",
     "Models doing science at unprecedented speed",
     "muendlich",
     "https://tedai-vienna.ted.com/speakers-2025/lukasz-kaiser",
     "Lukasz Kaiser - TEDAI 2026",
     "2025",
     "en",
     "Vision for AI scientific research capabilities"),

    # 16
    (person_id,
     "Models that don't just spit out the most likely next word but internally 'think,' calculate and use tools.",
     "Models that internally think and use tools",
     "muendlich",
     "https://www.ted.com/talks/lukasz_kaiser_what_if_ai_stops_guessing_and_starts_reasoning",
     "Lukasz Kaiser: What if AI stops guessing and starts reasoning? | TED Talk",
     None,
     "en",
     "TED Talk on reasoning AI"),

    # 17
    (person_id,
     "Neural networks can be trained on short instances of an algorithmic task and successfully generalize to long instances.",
     "Neural networks generalize from short to long instances",
     "schriftlich",
     "https://medium.com/aifrontiers/one-model-to-solve-all-problems-the-story-of-lukasz-kaiser-c015bf696a30",
     "One Model To Solve All Problems",
     None,
     "en",
     "Insight on algorithmic learning capabilities"),

    # 18
    (person_id,
     "The inherently sequential nature of RNNs precludes parallelization within training examples, which becomes critical at longer sequence lengths.",
     "RNN sequential nature precludes parallelization",
     "schriftlich",
     "https://arxiv.org/abs/1706.03762",
     "Attention Is All You Need",
     "2017-06-12",
     "en",
     "From the Transformer paper, motivation for new architecture"),
]

# HANDLUNGEN - 14 Stück
handlungen = [
    # 1
    (person_id,
     "einstellung",
     "Joined Google Brain as Senior Software Engineer",
     "2013-10",
     "https://www.linkedin.com/in/lukaszkaiser/",
     "Lukasz Kaiser - OpenAI | LinkedIn",
     "Left tenured position at CNRS/Paris Diderot University to join Google Brain"),

    # 2
    (person_id,
     "produktlaunch",
     "Co-authored publication 'Attention Is All You Need', introducing the Transformer architecture",
     "2017-06-12",
     "https://arxiv.org/abs/1706.03762",
     "Attention Is All You Need",
     "Paper submitted to arXiv, later published at NIPS 2017. One of eight co-authors (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Kaiser, Gomez, Polosukhin)"),

    # 3
    (person_id,
     "produktlaunch",
     "Co-authored 'One Model To Learn Them All', presenting MultiModel architecture",
     "2017-06-16",
     "https://arxiv.org/abs/1706.05137",
     "One Model To Learn Them All",
     "Paper with Gomez, Shazeer, Vaswani, Parmar, Jones, Uszkoreit demonstrating single model across multiple domains (vision, language, audio)"),

    # 4
    (person_id,
     "produktlaunch",
     "Announced Tensor2Tensor (T2T) library for deep learning in TensorFlow",
     "2017-06",
     "https://research.google/blog/accelerating-deep-learning-research-with-the-tensor2tensor-library/",
     "Accelerating Deep Learning Research with the Tensor2Tensor Library",
     "Open-source system for training deep learning models, co-created with Google Brain team"),

    # 5
    (person_id,
     "einstellung",
     "Joined OpenAI as Member of Technical Staff/Researcher",
     "2021-06",
     "https://www.linkedin.com/in/lukaszkaiser/",
     "Lukasz Kaiser - OpenAI | LinkedIn",
     "Left Google Brain after 8 years to join OpenAI"),

    # 6
    (person_id,
     "produktlaunch",
     "Core contributor to GPT-4 development, focusing on pretraining data and long context capabilities",
     "2023-03",
     "https://www.hulkapps.com/blogs/ecommerce-hub/a-comprehensive-insight-into-the-contributions-of-lukasz-kaiser-in-ai-and-machine-learning",
     "Comprehensive Insight into Lukasz Kaiser",
     "Worked on pretraining data for GPT-4 and extended long context to handle over 25,000 words of text"),

    # 7
    (person_id,
     "politisch",
     "Posted public statement supporting OpenAI employees during leadership crisis",
     "2023-11-20",
     "https://iq.wiki/wiki/ukasz-kaiser",
     "Lukasz Kaiser - IQ.wiki",
     "Tweeted 'OpenAI is nothing without its people' during November 2023 Sam Altman board crisis"),

    # 8
    (person_id,
     "produktlaunch",
     "Research lead for o1 reasoning model series at OpenAI",
     "2024-09",
     "https://eu.36kr.com/en/p/3477639604803976",
     "From Transformer to GPT-5",
     "Co-invented o1 model using 'hidden Chain of Thoughts' reasoning approach"),

    # 9
    (person_id,
     "sonstiges",
     "Speaker at Pathway Meetup San Francisco on 'Deep Learning Past and Future: What Comes After GPT?'",
     "2024-04",
     "https://pathway.com/news/pathway-meetup-2024/",
     "The Future of Large Language Models by Lukasz Kaiser",
     "Talk on future of LLMs, data scarcity, and knowledge graphs"),

    # 10
    (person_id,
     "produktlaunch",
     "Co-inventor of o3 reasoning model at OpenAI",
     "2024",
     "https://ml-summit.org/speaker/626?uid=c1047&lang=en",
     "Lukasz Kaiser | 2025 Machine Learning Summit",
     "Advanced reasoning model following o1"),

    # 11
    (person_id,
     "sonstiges",
     "Speaker at TEDAI Vienna 2025 on AI reasoning and 'models doing science'",
     "2025",
     "https://tedai-vienna.ted.com/speakers-2025/lukasz-kaiser",
     "Lukasz Kaiser - TEDAI 2026",
     "Discussed future direction where AI systems become 'Researchers' capable of scientific discovery"),

    # 12
    (person_id,
     "produktlaunch",
     "Co-author on research paper 'Competitive Programming with Large Reasoning Models'",
     "2025-02",
     "https://arxiv.org/abs/2502.06807",
     "Competitive Programming with Large Reasoning Models",
     "Recent research on reasoning models at OpenAI"),

    # 13
    (person_id,
     "sonstiges",
     "TED Talk: 'What if AI stops guessing and starts reasoning?'",
     None,
     "https://www.ted.com/talks/lukasz_kaiser_what_if_ai_stops_guessing_and_starts_reasoning",
     "Lukasz Kaiser TED Talk",
     "Public talk on the shift from next-token prediction to reasoning in AI"),

    # 14
    (person_id,
     "sonstiges",
     "Received E.W. Beth Dissertation Prize for outstanding dissertation in logic",
     "2009",
     "https://folli.info/?page_id=74",
     "E.W. Beth Dissertation Prize",
     "Awarded for PhD thesis 'Logic and Games on Automatic Structures' from RWTH Aachen"),
]

# Aussagen einfügen
print("Fuege Aussagen ein...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)
    print(f"  + Aussage eingefuegt: {aussage[2][:60]}...")

# Handlungen einfügen
print("\nFuege Handlungen ein...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)
    print(f"  + Handlung eingefuegt: {handlung[2][:60]}...")

# Änderungen speichern
conn.commit()

# Statistik ausgeben
print("\n" + "="*70)
print("ZUSAMMENFASSUNG")
print("="*70)
print(f"Person ID: {person_id} (Lukasz Kaiser)")
print(f"Eingefügte Aussagen: {len(aussagen)}")
print(f"Eingefügte Handlungen: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Einträge")
print("="*70)

# Verbindung schließen
conn.close()

print("\nDatenbank erfolgreich aktualisiert!")
