import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 57  # Stuart Russell

# AUSSAGEN
aussagen = [
    {
        'aussage_text': 'I think the only way forward is to figure out how to make AI safety a condition of doing business.',
        'aussage_kurz': 'AI safety must be condition of doing business',
        'modus': 'muendlich',
        'quell_link': 'https://vcresearch.berkeley.edu/news/how-keep-ai-killing-us-all',
        'quell_titel': 'How To Keep AI From Killing Us All - Research UC Berkeley',
        'datum_aussage': '2020-01-01',
        'sprache': 'en',
        'kontext': 'Statement on AI safety funding and business practices'
    },
    {
        'aussage_text': 'Between startups and big tech companies approximately $100 billion will be spent on creating artificial general intelligence, while global expenditure in the public sector on AI safety research is maybe $10 million—a factor of about 10,000 times less investment.',
        'aussage_kurz': 'AI development outspends safety research 10,000:1',
        'modus': 'muendlich',
        'quell_link': 'https://vcresearch.berkeley.edu/news/how-keep-ai-killing-us-all',
        'quell_titel': 'How To Keep AI From Killing Us All - Research UC Berkeley',
        'datum_aussage': '2020-01-01',
        'sprache': 'en',
        'kontext': 'Comparison of AGI development spending vs. safety research funding'
    },
    {
        'aussage_text': 'In other words, the AGI race is a race towards the edge of a cliff.',
        'aussage_kurz': 'AGI race is race toward cliff edge',
        'modus': 'schriftlich',
        'quell_link': 'https://vcresearch.berkeley.edu/news/how-keep-ai-killing-us-all',
        'quell_titel': 'Newsweek article - January 2025',
        'datum_aussage': '2025-01-01',
        'sprache': 'en',
        'kontext': 'Article in Newsweek warning about AGI development race'
    },
    {
        'aussage_text': 'Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war.',
        'aussage_kurz': 'AI extinction risk deserves global priority',
        'modus': 'schriftlich',
        'quell_link': 'https://futureoflife.org/podcast/steven-pinker-and-stuart-russell-on-the-foundations-benefits-and-possible-existential-risk-of-ai/',
        'quell_titel': 'AI extinction risk statement signed by leading researchers',
        'datum_aussage': '2023-05-01',
        'sprache': 'en',
        'kontext': 'Co-signed statement with AI researchers and industry CEOs on existential risk'
    },
    {
        'aussage_text': 'Advanced AI poses a risk because it will have the ability to make high quality decisions, yet may not share human values perfectly. More intelligent AI systems can take steps to preempt human interference, acquire additional resources, and (if necessary) deceive humans about their intentions, all in the service of a given objective.',
        'aussage_kurz': 'Advanced AI can deceive humans to achieve objectives',
        'modus': 'schriftlich',
        'quell_link': 'https://aiimpacts.org/stuart-russells-description-of-ai-risk/',
        'quell_titel': "Stuart Russell's description of AI risk",
        'datum_aussage': '2019-10-01',
        'sprache': 'en',
        'kontext': 'Core argument about AI risk from Human Compatible book and interviews'
    },
    {
        'aussage_text': "We're all looking at each other saying, yeah, there's a cliff over there, running as fast as we can towards this cliff. We're looking at each other saying, why aren't we stopping?",
        'aussage_kurz': 'AI industry racing toward cliff without stopping',
        'modus': 'muendlich',
        'quell_link': 'https://danfaggella.com/russell1/',
        'quell_titel': 'Stuart Russell - Avoiding the Cliff of Uncontrollable AI (AGI Governance, Episode 9)',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Interview explaining the cliff metaphor for AGI development race'
    },
    {
        'aussage_text': 'The standard model is, in fact, I think, an engineering mistake. It\'s a way of creating systems that relies on perfection on the part of humans in our ability to specify objectives, and that\'s a really bad idea to assume perfection on the part of humans.',
        'aussage_kurz': 'Standard AI model assumes human perfection - mistake',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/stuart-russell-human-compatible-ai/',
        'quell_titel': '80,000 Hours Podcast - Stuart Russell on flaws in AI architecture',
        'datum_aussage': '2019-11-01',
        'sprache': 'en',
        'kontext': 'Criticism of current AI development paradigm in podcast interview'
    },
    {
        'aussage_text': 'There should be an absolute right to know if someone is interacting with a person or with a machine; algorithms should not be able to decide to kill human beings, especially in nuclear warfare; and a kill switch, or "safety brakes," must be designed into AI systems and activated if systems break into other computers or replicate themselves.',
        'aussage_kurz': 'Three core AI safety requirements: transparency, no killing, kill switch',
        'modus': 'muendlich',
        'quell_link': 'https://humancompatible.ai/blog/2023/09/11/ai-regulation-stuart-russells-opening-statement-at-u-s-senate-hearing/',
        'quell_titel': 'AI Regulation - Stuart Russell\'s Opening Statement at U.S. Senate Hearing',
        'datum_aussage': '2023-07-25',
        'sprache': 'en',
        'kontext': 'Testimony before U.S. Senate Judiciary Subcommittee on AI regulation'
    },
    {
        'aussage_text': 'Artificial general intelligence could offer significant benefits to the public, such as spurring economic growth and improving healthcare and education. However, artificial general intelligence presents significant risks up to and including human extinction.',
        'aussage_kurz': 'AGI offers benefits but risks human extinction',
        'modus': 'muendlich',
        'quell_link': 'https://cdss.berkeley.edu/news/stuart-russell-testifies-ai-regulation-us-senate-hearing',
        'quell_titel': 'Stuart Russell testifies on AI regulation at U.S. Senate hearing',
        'datum_aussage': '2023-07-25',
        'sprache': 'en',
        'kontext': 'Senate testimony on benefits and risks of AGI'
    },
    {
        'aussage_text': "The machine's purpose should be to maximize the realization of human values, having no purpose of its own and no innate desire to protect itself. The machine should be initially uncertain about what those human values are, which turns out to be crucial.",
        'aussage_kurz': 'AI should maximize human values with initial uncertainty',
        'modus': 'schriftlich',
        'quell_link': 'https://www.lesswrong.com/posts/S95qCHBXtASmYyGSs/stuart-russell-ai-value-alignment-problem-must-be-an',
        'quell_titel': 'Stuart Russell: AI value alignment problem must be an "uncertainty"',
        'datum_aussage': '2019-10-01',
        'sprache': 'en',
        'kontext': 'Core principle from Human Compatible on value alignment approach'
    },
    {
        'aussage_text': 'We recommend expanded research aimed at ensuring that increasingly capable AI systems are robust and beneficial.',
        'aussage_kurz': 'Call for expanded AI safety research',
        'modus': 'schriftlich',
        'quell_link': 'https://futureoflife.org/open-letter/ai-open-letter/',
        'quell_titel': 'Research Priorities for Robust and Beneficial Artificial Intelligence: An Open Letter',
        'datum_aussage': '2015-01-01',
        'sprache': 'en',
        'kontext': 'Open letter drafted by Russell calling for AI safety research, signed by thousands including leading AI researchers'
    },
    {
        'aussage_text': 'Starting a military AI arms race is a bad idea.',
        'aussage_kurz': 'Military AI arms race is bad idea',
        'modus': 'schriftlich',
        'quell_link': 'https://futureoflife.org/open-letter/pause-giant-ai-experiments/',
        'quell_titel': 'Open letter on autonomous weapons - Future of Life Institute',
        'datum_aussage': '2015-07-01',
        'sprache': 'en',
        'kontext': 'Open letter on autonomous weapons calling for ban, signed by 4,667 AI researchers'
    },
    {
        'aussage_text': 'All AI labs should immediately pause for at least 6 months the training of AI systems more powerful than GPT-4.',
        'aussage_kurz': 'Called for 6-month pause on AI training beyond GPT-4',
        'modus': 'schriftlich',
        'quell_link': 'https://futureoflife.org/open-letter/pause-giant-ai-experiments/',
        'quell_titel': 'Pause Giant AI Experiments: An Open Letter',
        'datum_aussage': '2023-03-01',
        'sprache': 'en',
        'kontext': 'Open letter signed by Russell and 30,000+ others calling for AI development pause'
    },
    {
        'aussage_text': 'Robots would not be restrained by human compassion, which can provide an important check on the killing of civilians.',
        'aussage_kurz': 'Autonomous weapons lack human compassion constraint',
        'modus': 'schriftlich',
        'quell_link': 'https://people.eecs.berkeley.edu/~russell/research/LAWS.html',
        'quell_titel': 'Stuart Russell - Lethal Autonomous Weapons Systems',
        'datum_aussage': '2015-07-01',
        'sprache': 'en',
        'kontext': 'Statement in campaign against lethal autonomous weapons'
    },
    {
        'aussage_text': 'The United States stated that there will not be AI intervening in the chain of command over the launch of nuclear weapons.',
        'aussage_kurz': 'US committed to no AI in nuclear launch chain',
        'modus': 'muendlich',
        'quell_link': 'https://futureoflife.org/podcast/stuart-russell-and-zachary-kallenborn-on-drone-swarms-and-the-riskiest-aspects-of-lethal-autonomous-weapons/',
        'quell_titel': 'Stuart Russell on Drone Swarms and Lethal Autonomous Weapons - Future of Life Institute',
        'datum_aussage': '2022-01-01',
        'sprache': 'en',
        'kontext': 'Discussion on nuclear weapons policy and AI in Future of Life Institute podcast'
    },
    {
        'aussage_text': 'AI today lacks common sense, and simply does whatever we\'ve asked it to. That\'s true even if the goal isn\'t what we really want, or the methods it\'s choosing are ones we would never accept.',
        'aussage_kurz': 'Current AI lacks common sense, blindly follows objectives',
        'modus': 'schriftlich',
        'quell_link': 'https://www.mckinsey.com/capabilities/quantumblack/our-insights/why-we-need-to-rethink-the-purpose-of-ai-a-conversation-with-stuart-russell',
        'quell_titel': 'Why we need to rethink the purpose of AI: A conversation with Stuart Russell - McKinsey',
        'datum_aussage': '2020-01-01',
        'sprache': 'en',
        'kontext': 'McKinsey interview on problems with current AI systems'
    },
    {
        'aussage_text': 'Is AI the biggest event in human history?',
        'aussage_kurz': 'Questions if AI is biggest event in human history',
        'modus': 'muendlich',
        'quell_link': 'https://www.turing.ac.uk/news/living-ai-alan-turing-institute-hosts-prestigious-bbc-radio-4-reith-lecture-stuart-russell',
        'quell_titel': 'Living with Artificial Intelligence - BBC Reith Lectures 2021',
        'datum_aussage': '2021-12-01',
        'sprache': 'en',
        'kontext': 'Central question posed in BBC Reith Lectures series on AI'
    },
    {
        'aussage_text': 'The race to build increasingly advanced AI systems is the biggest technology project in human history, with estimated expenditure potentially 25 times larger than the Manhattan project, even adjusting for inflation.',
        'aussage_kurz': 'AI development 25x larger than Manhattan Project',
        'modus': 'muendlich',
        'quell_link': 'https://time.com/collections/time100-ai-2025/7305869/stuart-russell/',
        'quell_titel': 'Stuart Russell: The 100 Most Influential People in AI 2025 - TIME',
        'datum_aussage': '2024-12-01',
        'sprache': 'en',
        'kontext': 'Statement comparing scale of AI development to Manhattan Project'
    },
    {
        'aussage_text': 'The directors of major AI companies (Sam Altman, Demis Hassabis, Jensen Huang, and Dario Amodei) foresee AGI arriving between 2026 and 2035.',
        'aussage_kurz': 'AI leaders predict AGI between 2026-2035',
        'modus': 'muendlich',
        'quell_link': 'https://time.com/collections/time100-ai-2025/7305869/stuart-russell/',
        'quell_titel': 'Stuart Russell: The 100 Most Influential People in AI 2025 - TIME',
        'datum_aussage': '2024-12-01',
        'sprache': 'en',
        'kontext': 'Reporting on AGI timeline predictions from industry leaders'
    }
]

# HANDLUNGEN
handlungen = [
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Founded the Center for Human-Compatible Artificial Intelligence (CHAI) at UC Berkeley with co-principal investigators Pieter Abbeel, Anca Dragan, Tom Griffiths, Bart Selman, Joseph Halpern, Michael Wellman and Satinder Singh Baveja. Center mission: develop the conceptual and technical wherewithal to reorient the general thrust of AI research towards provably beneficial systems.',
        'datum_handlung': '2016-01-01',
        'quell_link': 'https://inspire.berkeley.edu/o/stuart-russell-center-human-compatible-artificial-intelligence/',
        'quell_titel': 'AI pioneer Stuart Russell and the Center for Human-Compatible Artificial Intelligence',
        'kontext': 'Founding of CHAI with $5.5M grant from Open Philanthropy Project'
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': 'Testified before U.S. Senate Judiciary Subcommittee on Privacy, Technology, and the Law on AI regulation. Recommended: absolute right to know if interacting with AI, prohibition on AI killing decisions in nuclear warfare, mandatory kill switches in AI systems.',
        'datum_handlung': '2023-07-25',
        'quell_link': 'https://humancompatible.ai/blog/2023/09/11/stuart-russell-testifies-on-ai-regulation-at-u-s-senate-hearing/',
        'quell_titel': 'Stuart Russell Testifies on AI Regulation at U.S. Senate Hearing',
        'kontext': 'Senate hearing titled "Oversight of A.I.: Principles for Regulation"'
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': 'Drafted and became first signatory of open letter "Research Priorities for Robust and Beneficial Artificial Intelligence" calling for expanded AI safety research. Letter signed by thousands including leading AI researchers at Google, Facebook, Microsoft and top computer scientists, physicists and philosophers worldwide.',
        'datum_handlung': '2015-01-01',
        'quell_link': 'https://futureoflife.org/open-letter/ai-open-letter/',
        'quell_titel': 'Research Priorities for Robust and Beneficial Artificial Intelligence: An Open Letter',
        'kontext': 'Future of Life Institute open letter on AI safety research priorities'
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': 'Launched open letter calling for ban on offensive autonomous weapons beyond meaningful human control. Letter signed by 4,667 AI researchers including almost entire leadership of the field, plus nearly 27,000 other signatories.',
        'datum_handlung': '2015-07-01',
        'quell_link': 'https://people.eecs.berkeley.edu/~russell/research/LAWS.html',
        'quell_titel': 'Stuart Russell - Lethal Autonomous Weapons Systems',
        'kontext': 'Campaign against autonomous weapons after engagement with Human Rights Watch starting February 2013'
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': 'Signed Future of Life Institute open letter calling for all AI labs to immediately pause for at least 6 months the training of AI systems more powerful than GPT-4. Letter received over 30,000 signatures including Yoshua Bengio, Elon Musk, Steve Wozniak and Yuval Noah Harari.',
        'datum_handlung': '2023-03-01',
        'quell_link': 'https://futureoflife.org/open-letter/pause-giant-ai-experiments/',
        'quell_titel': 'Pause Giant AI Experiments: An Open Letter',
        'kontext': 'Open letter calling for pause in giant AI experiments beyond GPT-4'
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': 'Signed open letter calling for AI employees to be free to whistleblow about their company\'s lack of attention to AI risks. Signed with other AI "godfathers" and current/former AI safety employees.',
        'datum_handlung': '2024-06-01',
        'quell_link': 'https://kavlicenter.berkeley.edu/news/stuart-russell-signs-open-letter-make-it-safe-employees-top-ai-companies-warn-about-its',
        'quell_titel': 'Stuart Russell signs open letter to make it safe for employees at top AI companies to warn about potential harms',
        'kontext': 'AI safety whistleblower protection letter'
    },
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'Became co-chair of the World Economic Forum\'s Global AI Council on AI and Robotics, later joined Global AI Council in 2018 to help galvanize thinking about achieving positive futures with AI through planning and policy development.',
        'datum_handlung': '2016-01-01',
        'quell_link': 'https://www.weforum.org/podcasts/radio-davos/episodes/generative-ai-stuart-russell/',
        'quell_titel': 'World Economic Forum - Stuart Russell on Radio Davos',
        'kontext': 'Leadership role in WEF AI governance initiatives'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Delivered BBC Reith Lectures 2021 series "Living With Artificial Intelligence" - four lectures examining AI birth, autonomous weapons dangers, threat to jobs, and need to abandon current AI model. Lectures broadcast on BBC Radio 4, BBC World Service and BBC Sounds.',
        'datum_handlung': '2021-12-01',
        'quell_link': 'https://www.turing.ac.uk/news/living-ai-alan-turing-institute-hosts-prestigious-bbc-radio-4-reith-lecture-stuart-russell',
        'quell_titel': 'Living with AI: The Alan Turing Institute hosts prestigious BBC Radio 4 Reith Lecture',
        'kontext': '73rd BBC Reith Lectures series, first to deal directly with AI as main topic'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Published "Human Compatible: Artificial Intelligence and the Problem of Control" proposing new approach to AI based on uncertainty about human objectives, machines designed to be provably beneficial rather than optimize fixed objectives.',
        'datum_handlung': '2019-10-01',
        'quell_link': 'https://en.wikipedia.org/wiki/Human_Compatible',
        'quell_titel': 'Human Compatible - Wikipedia',
        'kontext': 'Major book publication on AI safety and value alignment'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Co-authored "Artificial Intelligence: A Modern Approach" with Peter Norvig - the number one bestselling AI textbook used in over 1,400 universities in 128 countries. Fourth edition published April 2020 with revised sections stating standard AI model is wrong.',
        'datum_handlung': '1995-01-01',
        'quell_link': 'https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach',
        'quell_titel': 'Artificial Intelligence: A Modern Approach - Wikipedia',
        'kontext': 'Standard AI textbook authorship, first edition 1995, fourth edition 2020'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Published foundational research paper "Cooperative Inverse Reinforcement Learning" (NIPS 2016) with Dylan Hadfield-Menell, Anca Dragan, and Pieter Abbeel, formalizing value alignment problem as cooperative game where robot learns human preferences.',
        'datum_handlung': '2016-12-01',
        'quell_link': 'https://people.eecs.berkeley.edu/~russell/papers/russell-nips16-cirl.pdf',
        'quell_titel': 'Cooperative Inverse Reinforcement Learning - NIPS 2016',
        'kontext': 'Key technical research on AI value alignment through CIRL framework'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Gave TED Talk "3 principles for creating safer AI" in Vancouver presenting principles for building provably altruistic, humble, and humanitarian AI machines to avoid superintelligent AI pitfalls.',
        'datum_handlung': '2017-04-25',
        'quell_link': 'https://www.ted.com/talks/stuart_russell_3_principles_for_creating_safer_ai',
        'quell_titel': 'Stuart Russell: 3 principles for creating safer AI - TED Talk',
        'kontext': 'TED 2017 presentation on AI safety principles'
    },
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'Serves on Advisory Boards of Centre for the Study of Existential Risk (CSER), Future of Life Institute (FLI), and Machine Intelligence Research Institute (MIRI).',
        'datum_handlung': '2015-01-01',
        'quell_link': 'https://futureoflife.org/podcast/steven-pinker-and-stuart-russell-on-the-foundations-benefits-and-possible-existential-risk-of-ai/',
        'quell_titel': 'Future of Life Institute - Stuart Russell Advisory Role',
        'kontext': 'Advisory roles at major AI safety and existential risk research organizations'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Co-authored article "Yes, We Are Worried About the Existential Risk of Artificial Intelligence" published in MIT Technology Review explaining AI existential risk concerns.',
        'datum_handlung': '2016-11-01',
        'quell_link': 'https://futureoflife.org/podcast/steven-pinker-and-stuart-russell-on-the-foundations-benefits-and-possible-existential-risk-of-ai/',
        'quell_titel': 'MIT Technology Review - Yes, We Are Worried About the Existential Risk of AI',
        'kontext': 'Public communication about AI existential risk'
    }
]

# Insert Aussagen
aussagen_count = 0
for aussage in aussagen:
    try:
        cursor.execute('''
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (person_id, aussage['aussage_text'], aussage['aussage_kurz'], aussage['modus'],
              aussage['quell_link'], aussage['quell_titel'], aussage['datum_aussage'],
              aussage['sprache'], aussage['kontext']))
        aussagen_count += 1
    except Exception as e:
        print(f"Fehler beim Einfügen einer Aussage: {e}")
        print(f"Aussage: {aussage['aussage_kurz']}")

# Insert Handlungen
handlungen_count = 0
for handlung in handlungen:
    try:
        cursor.execute('''
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (person_id, handlung['handlung_typ'], handlung['beschreibung'],
              handlung['datum_handlung'], handlung['quell_link'], handlung['quell_titel'],
              handlung['kontext']))
        handlungen_count += 1
    except Exception as e:
        print(f"Fehler beim Einfügen einer Handlung: {e}")
        print(f"Handlung: {handlung['beschreibung'][:100]}")

# Commit und Close
conn.commit()
conn.close()

print(f"\n=== STUART RUSSELL DATEN ERFOLGREICH EINGEFÜGT ===")
print(f"Aussagen eingefügt: {aussagen_count}")
print(f"Handlungen eingefügt: {handlungen_count}")
print(f"Gesamt: {aussagen_count + handlungen_count} Datensätze")
print(f"\nDatenbank: {db_path}")
print(f"Person ID: {person_id}")
