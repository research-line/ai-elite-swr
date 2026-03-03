#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert statements and actions for Michael I. Jordan (person_id=60)
UC Berkeley ML Professor, critic of AI hype
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (Statements)
    aussagen = [
        # AGI/AI Hype Criticism - February 2025
        (60,
         'This super AGI thing that can answer any question, it knows everything... this is nonsense.',
         'AGI claims are nonsense',
         'muendlich',
         'https://techxplore.com/news/2025-02-blasts-nonsense-superhuman-ai.html',
         'Top researcher blasts \'nonsense\' of superhuman AI - TechXplore',
         '2025-02-06',
         'en',
         'Speaking to scientists in Paris, criticizing claims from OpenAI chief Sam Altman and Anthropic\'s Dario Amodei that AGI is only years away'),

        (60,
         'This whole development of this wonderful engineering field is really being held back by this whole AI aspiration, building a super robot that takes over and helps you for all your tasks at home and all these other things. I don\'t think there\'s ever been an era in human history where a new field of technology has arisen where there was so much hype and hysteria.',
         'AI hype holding back engineering field',
         'muendlich',
         'https://techxplore.com/news/2025-02-blasts-nonsense-superhuman-ai.html',
         'Top researcher blasts \'nonsense\' of superhuman AI - TechXplore',
         '2025-02-06',
         'en',
         'Commenting on unprecedented hype in AI field'),

        (60,
         'Companies are spending billions and trillions to achieve what is for now an illusory goal.',
         'Billions spent on illusory AGI goal',
         'muendlich',
         'https://techxplore.com/news/2025-02-blasts-nonsense-superhuman-ai.html',
         'Top researcher blasts \'nonsense\' of superhuman AI - TechXplore',
         '2025-02-06',
         'en',
         'Criticizing massive spending on AGI development'),

        (60,
         'AI does not and cannot know everything. Information in people\'s minds cannot be detected by AI. Large language models are tiny experts who reply to certain questions but cannot be deemed intelligent entities.',
         'LLMs are tiny experts, not intelligent',
         'muendlich',
         'https://www.digitalinformationworld.com/2025/02/uc-berkeley-researcher-criticizes.html',
         'UC Berkeley Researcher Criticizes Billion-Dollar AGI Race - Digital Information World',
         '2025-02-01',
         'en',
         'Explaining limitations of current AI systems'),

        # Big Data Winter Prediction - 2014
        (60,
         'After a bubble, when people invested and a lot of companies overpromised without providing serious analysis, it will bust. I am predicting that within a two- to five-year span, people will say the big-data thing came and went and died.',
         'Predicting big-data winter',
         'muendlich',
         'https://spectrum.ieee.org/machinelearning-maestro-michael-jordan-on-the-delusions-of-big-data-and-other-huge-engineering-efforts',
         'Machine-Learning Maestro Michael Jordan on the Delusions of Big Data - IEEE Spectrum',
         '2014-10-03',
         'en',
         'IEEE Spectrum interview, predicting bubble burst due to overpromising without analysis'),

        (60,
         'Cycles of excessive hype—assertions not based on understanding real problems or acknowledging that solving them would take decades—will be followed by a period when it would be very hard to get resources for data analysis.',
         'Hype cycles damage field funding',
         'muendlich',
         'https://spectrum.ieee.org/machinelearning-maestro-michael-jordan-on-the-delusions-of-big-data-and-other-huge-engineering-efforts',
         'Machine-Learning Maestro Michael Jordan on the Delusions of Big Data - IEEE Spectrum',
         '2014-10-03',
         'en',
         'Warning about consequences of unrealistic promises'),

        # AI Revolution Article - 2019
        (60,
         'People are getting confused about the meaning of AI in discussions of technology trends – that there is some kind of intelligent thought in computers that is responsible for the progress and which is competing with humans.',
         'People confused about AI meaning',
         'schriftlich',
         'https://spectrum.ieee.org/stop-calling-everything-ai-machinelearning-pioneer-says',
         'Stop Calling Everything AI, Machine-Learning Pioneer Says - IEEE Spectrum',
         '2021-03-01',
         'en',
         'IEEE Spectrum article explaining misconceptions about AI'),

        (60,
         'AI systems are showing human-level competence in low-level pattern recognition skills, but at the cognitive level they are merely imitating human intelligence, not engaging deeply and creatively.',
         'AI imitates, not thinks deeply',
         'schriftlich',
         'https://spectrum.ieee.org/stop-calling-everything-ai-machinelearning-pioneer-says',
         'Stop Calling Everything AI, Machine-Learning Pioneer Says - IEEE Spectrum',
         '2021-03-01',
         'en',
         'Distinguishing between pattern recognition and cognitive intelligence'),

        (60,
         'I don\'t like the term AI because it prevents you from thinking through the real impact of the technology and the effect on collectives of people instead of on single individuals.',
         'AI term prevents clear thinking',
         'muendlich',
         'https://cdss.berkeley.edu/news/data-scientist-michael-jordan-calls-more-economics-aware-approach-ai',
         'Data Scientist Michael Jordan Calls for a More Economics-Aware Approach to AI - CDSS Berkeley',
         '2023-05-11',
         'en',
         'Explaining problems with AI terminology'),

        # Economics and Employment Focus
        (60,
         'From an economic point of view, the goal of exceeding human performance raises the specter of massive unemployment. As an alternative goal for AI, machine learning should discover and support new kinds of interactions among humans that increase job possibilities.',
         'ML should increase job possibilities',
         'schriftlich',
         'https://hdsr.mitpress.mit.edu/pub/wot7mkc1',
         'Artificial Intelligence—The Revolution Hasn\'t Happened Yet - Harvard Data Science Review',
         '2019-04-01',
         'en',
         'Harvard Data Science Review article proposing alternative vision for ML'),

        (60,
         'The lack of attention to collectivity, uncertainty, and incentive mechanisms is what is missing in the current discussions on artificial intelligence. For AI to be applied in industries, it needs to introduce the economic perspective of incentives.',
         'AI needs economics perspective',
         'muendlich',
         'https://test-news.aibase.com/news/11562',
         'Machine Learning Master Michael Jordan: The Development of AI Must Not Overlook Collectivity - AI Base',
         '2024-09-01',
         'en',
         'Speaking at the 2024 Inclusion·Bund Conference'),

        # Intelligent Infrastructure Vision
        (60,
         'Distributed, social intelligence is better suited to meeting human needs than the type of autonomous general intelligence we associate with the Terminator movies or Marvel\'s Ultron.',
         'Distributed intelligence better than AGI',
         'schriftlich',
         'https://hdsr.mitpress.mit.edu/pub/wot7mkc1',
         'Artificial Intelligence—The Revolution Hasn\'t Happened Yet - Harvard Data Science Review',
         '2019-04-01',
         'en',
         'Proposing alternative to human-imitative AI'),

        (60,
         'I conceived of a discipline of Intelligent Infrastructure (II), whereby a web of computation, data, and physical entities exists that makes human environments more supportive, interesting, and safe, with such infrastructure beginning to appear in domains such as transportation, medicine, commerce, and finance.',
         'Intelligent Infrastructure concept',
         'schriftlich',
         'https://hdsr.mitpress.mit.edu/pub/wot7mkc1',
         'Artificial Intelligence—The Revolution Hasn\'t Happened Yet - Harvard Data Science Review',
         '2019-04-01',
         'en',
         'Defining new engineering discipline'),

        (60,
         'Machine learning is the first engineering field that is humancentric, focused on the interface between people and technology.',
         'ML is humancentric engineering',
         'muendlich',
         'https://www.hec.edu/en/school/news/machine-learning-pioneer-questions-ai-and-forges-new-engineering-path',
         'Machine Learning Pioneer Questions A.I. and Forges New Engineering Path - HEC Paris',
         '2023-11-28',
         'en',
         'Describing unique character of machine learning field'),

        (60,
         'Intelligent Infrastructure systems must bring economic ideas such as incentives and pricing into the realm of the statistical and computational infrastructures that link humans to each other and to valued goods, and can be viewed as not merely providing a service, but as creating markets.',
         'II creates markets, not just services',
         'schriftlich',
         'https://cdss.berkeley.edu/news/data-scientist-michael-jordan-calls-more-economics-aware-approach-ai',
         'Data Scientist Michael Jordan Calls for a More Economics-Aware Approach to AI - CDSS Berkeley',
         '2023-05-11',
         'en',
         'Explaining economic dimension of intelligent systems'),

        # Additional Perspectives
        (60,
         'Since 2018, I declared that the AI revolution has yet to take place, and I do not use the AI terminology, instead calling it machine learning, control theory, engineering or statistics.',
         'AI revolution hasn\'t happened yet',
         'muendlich',
         'https://www.amazon.science/blog/icassp-michael-i-jordans-alternative-view-on-ai',
         'ICASSP: Michael I. Jordan\'s alternative view on AI - Amazon Science',
         '2024-04-14',
         'en',
         'Keynote at ICASSP conference'),

        (60,
         'The optimal goal of machine learning should not be artificial imitation of human thinking, but instead AI should be focused on helping humanity solve the problems that it has created.',
         'ML should solve human problems',
         'muendlich',
         'https://www.hec.edu/en/school/news/machine-learning-pioneer-questions-ai-and-forges-new-engineering-path',
         'Machine Learning Pioneer Questions A.I. and Forges New Engineering Path - HEC Paris',
         '2023-11-28',
         'en',
         'Explaining alternative goals for AI research'),
    ]

    # HANDLUNGEN (Actions)
    handlungen = [
        # AMPLab Co-Founding
        (60,
         'gruendung',
         'Co-directed AMPLab (Algorithms, Machines and People Lab) at UC Berkeley with Michael Franklin and Ion Stoica. The lab was officially launched in 2011 and awarded NSF CISE Expeditions in Computing grant in 2012. AMPLab created Apache Spark, Apache Mesos, and Alluxio, influential big data technologies.',
         '2011-01-01',
         'https://amplab.cs.berkeley.edu/about/',
         'About AMPLab - UC Berkeley',
         'Major research lab that became known for developing foundational big data analytics stack (BDAS)'),

        # RISELab Founding
        (60,
         'gruendung',
         'Affiliated faculty member and leader in RISELab (Real-time Intelligent Secure Execution), the successor to AMPLab. RISELab focuses on enabling computers to make intelligent real-time decisions.',
         '2017-01-01',
         'https://rise.cs.berkeley.edu/',
         'Berkeley RISE Lab - UC Berkeley',
         'Five-year intensive research lab continuing AMPLab\'s work with focus on real-time intelligent systems'),

        # Inria France Research Chair
        (60,
         'partnerschaft',
         'Launched five-year "Markets and Machine Learning" research chair at Inria Foundation in Paris, in collaboration with CNRS and École Normale Supérieure-Université PSL. Chair backed by Air Liquide, BNP Paribas Asset Management Europe, EDF, Orange and SNCF.',
         '2023-01-01',
         'https://www.inria.fr/en/new-research-chair-bringing-together-economics-and-artificial-intelligence',
         'A new research chair bringing together economics and artificial intelligence - Inria',
         'Chair focuses on algorithms for learning and decision-making in industrial and business contexts'),

        # Machine Learning Journal Resignation
        (60,
         'politisch',
         'Resigned from editorial board of journal Machine Learning along with other editors, issuing public letter arguing for less restrictive access and pledging support for new open access journal, the Journal of Machine Learning Research.',
         '2001-01-01',
         'https://en.wikipedia.org/wiki/Michael_I._Jordan',
         'Michael I. Jordan - Wikipedia',
         'Early advocacy for open access in academic publishing'),

        # Data Science Undergraduate Course
        (60,
         'produktlaunch',
         'Developed and taught freshman-level undergraduate Data Science course at Berkeley (Fall 2015) that blends computer science and statistics, teaching Python programming for data analysis with resampling-based inferential procedures.',
         '2015-09-01',
         'https://www.causeweb.org/cause/ecots/ecots16/keynotes/jordan',
         'Computational Thinking and Inferential Thinking: Foundations of Data Science - CAUSEweb',
         'Pioneering undergraduate data science education with connector courses in various disciplines'),

        # National Academy of Engineering Election
        (60,
         'sonstiges',
         'Elected member of National Academy of Engineering for contributions to the foundations and applications of machine learning.',
         '2010-01-01',
         'https://en.wikipedia.org/wiki/Michael_I._Jordan',
         'Michael I. Jordan - Wikipedia',
         'Major recognition of contributions to machine learning field'),

        # Royal Society Election
        (60,
         'sonstiges',
         'Named Foreign Member of the Royal Society.',
         '2021-05-01',
         'https://engineering.berkeley.edu/news/2021/05/eecs-professor-michael-jordan-named-to-royal-society/',
         'EECS professor Michael Jordan named to Royal Society - Berkeley Engineering',
         'International recognition from UK national academy of sciences'),

        # Ulf Grenander Prize
        (60,
         'sonstiges',
         'Awarded 2021 American Mathematical Society (AMS) Ulf Grenander Prize in Stochastic Theory and Modeling.',
         '2021-01-01',
         'https://eecs.berkeley.edu/news/michael-jordan-wins-2021-ams-ulf-grenander-prize/',
         'Michael Jordan wins 2021 AMS Ulf Grenander Prize - EECS Berkeley',
         'Recognition for contributions to stochastic modeling'),

        # World Laureates Association Prize
        (60,
         'sonstiges',
         'Awarded inaugural World Laureates Association Prize for fundamental contributions to the foundations of machine learning and its application.',
         '2022-01-01',
         'https://www.thewlaprize.org/Laureates/2022/Michael_I._Jordan/',
         'Michael I. JORDAN - 2022 - World Laureates Association',
         'First recipient of new international prize'),

        # BBVA Frontiers of Knowledge Award
        (60,
         'sonstiges',
         'Awarded BBVA Foundation Frontiers of Knowledge Award in Information and Communication Technologies (jointly with Anil Jain) for core contributions to machine learning enabling AI applications including ChatGPT, recommender systems, and business decision tools.',
         '2025-01-01',
         'https://www.frontiersofknowledgeawards-fbbva.es/galardonados/michael-i-jordan-2/',
         'Michael I. Jordan, 17th Frontiers of Knowledge Award - BBVA Foundation',
         'Recognition for mathematical foundations of generative AI and recommendation systems'),

        # Harvard Data Science Review Editorial Role
        (60,
         'einstellung',
         'Served as co-editor for Harvard Data Science Review, contributing to inaugural issue and helping establish the publication.',
         '2018-01-01',
         'https://hdsr.mitpress.mit.edu/pub/ujg4bxwa/release/2',
         'Michael Jordan - Harvard Data Science Review',
         'Co-editor role from 2018-2021, shaping emerging field of data science'),

        # Vannevar Bush Fellowship
        (60,
         'sonstiges',
         'Awarded Vannevar Bush Faculty Fellowship for 2021-2026.',
         '2021-01-01',
         'https://people.eecs.berkeley.edu/~jordan/jordan-cv.pdf',
         'Vitae Michael I. Jordan - UC Berkeley',
         'Prestigious DOD-funded fellowship supporting basic research'),

        # Public Criticism of AI Industry Leaders
        (60,
         'politisch',
         'Publicly criticized OpenAI CEO Sam Altman and Anthropic CEO Dario Amodei for making unrealistic AGI timeline claims, calling their "super AGI" vision "nonsense" at scientific conference in Paris.',
         '2025-02-06',
         'https://techxplore.com/news/2025-02-blasts-nonsense-superhuman-ai.html',
         'Top researcher blasts \'nonsense\' of superhuman AI - TechXplore',
         'Direct public challenge to industry hype from leading academic researcher'),
    ]

    # Insert aussagen
    cursor.executemany('''
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', aussagen)

    # Insert handlungen
    cursor.executemany('''
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', handlungen)

    conn.commit()

    aussagen_count = len(aussagen)
    handlungen_count = len(handlungen)
    total_count = aussagen_count + handlungen_count

    print(f"Successfully inserted {aussagen_count} aussagen (statements)")
    print(f"Successfully inserted {handlungen_count} handlungen (actions)")
    print(f"Total entries: {total_count}")
    print(f"\nData for Michael I. Jordan (person_id=60) has been added to the database.")

    conn.close()
    return aussagen_count, handlungen_count

if __name__ == "__main__":
    insert_data()
