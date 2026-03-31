#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Einfügen von Aussagen und Handlungen für Pieter Abbeel (person_id=58)
in die Forschungsdatenbank aussagen_top100.db
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 58

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN - Pieter Abbeel
    aussagen = [
        # 1. On Intelligence as a moving target
        (PERSON_ID,
         "I feel like traditionally we think of intelligence as the things that computers can't do yet. And then all of a sudden when we manage to do it, we understand how it works and we don't think of it as that intelligent anymore. It used to be okay, if we can make a computer play checkers that would make it intelligent, and then later we're like, 'Wait, that's not enough to be intelligent,' and we keep moving the bar.",
         "Intelligence is what computers can't do yet - we keep moving the bar",
         "muendlich",
         "https://voicesinai.com/episode/episode-93-a-conversation-with-pieter-abbeel/",
         "Voices in AI - Episode 93: A Conversation with Pieter Abbeel",
         None,
         "en",
         "Interview discussion about defining intelligence and AI capabilities"),

        # 2. On defining intelligence
        (PERSON_ID,
         "Intelligence should be understood as having the ability to adapt to new environments and achieve something meaningful in new environments that the system has never been in.",
         "Intelligence is the ability to adapt to new environments",
         "muendlich",
         "https://voicesinai.com/episode/episode-93-a-conversation-with-pieter-abbeel/",
         "Voices in AI - Episode 93: A Conversation with Pieter Abbeel",
         None,
         "en",
         "Proposing a functional definition of intelligence"),

        # 3. On AI and robotics impact
        (PERSON_ID,
         "What's possible in AI and robotics today is so different from what was possible even five years ago. It's a space where things are changing very fast and in ways that are going to impact people's lives.",
         "AI and robotics are changing very fast and will impact lives",
         "muendlich",
         "https://engineering.berkeley.edu/news/2022/03/robots-ai-and-podcasting-a-qa-with-pieter-abbeel/",
         "Robots, AI and podcasting: a Q&A with Pieter Abbeel - Berkeley Engineering",
         "2022-03-01",
         "en",
         "Interview about the pace of AI development"),

        # 4. On robot learning needs
        (PERSON_ID,
         "Robots need to be smarter than they are. They need to learn how to react to situations not just perform the same action again and again. They need to adapt to live in their environment.",
         "Robots need to learn to adapt, not just repeat actions",
         "muendlich",
         "https://engineering.berkeley.edu/news/2022/03/robots-ai-and-podcasting-a-qa-with-pieter-abbeel/",
         "Robots, AI and podcasting: a Q&A with Pieter Abbeel - Berkeley Engineering",
         "2022-03-01",
         "en",
         "Discussing the need for adaptive robotics"),

        # 5. On autonomous vehicles and safety
        (PERSON_ID,
         "I view the notion that people get into car accidents as something that can be made a thing of the past through good self-driving cars as very powerful.",
         "Self-driving cars can eliminate human car accidents",
         "muendlich",
         "https://vcresearch.berkeley.edu/faculty/pieter-abbeel",
         "Pieter Abbeel | Research UC Berkeley",
         None,
         "en",
         "Discussing the safety potential of autonomous vehicles"),

        # 6. On AI empowering science
        (PERSON_ID,
         "I am excited about the direction of empowering other scientific disciplines with AI and believe there is a whole area where AI can help other scientific disciplines.",
         "AI can empower and help other scientific disciplines",
         "muendlich",
         "https://vcresearch.berkeley.edu/faculty/pieter-abbeel",
         "Pieter Abbeel | Research UC Berkeley",
         None,
         "en",
         "On broader applications of AI beyond robotics"),

        # 7. On jobs and automation
        (PERSON_ID,
         "Humans will continue to work alongside robots in warehouses, but the job market would surely change as machine learning improves.",
         "Humans will work with robots but job market will change",
         "muendlich",
         "https://stories.kuleuven.be/en/stories/inside-the-human-intelligence-of-pieter-abbeel",
         "Adapt to impact: inside the human intelligence of Pieter Abbeel",
         None,
         "en",
         "Discussion on the future of work and automation"),

        # 8. On robotics as positive force
        (PERSON_ID,
         "A future with smarter robots could be a real benefit to humanity. At Covariant, we firmly believe that robotics represents an overwhelmingly positive force for our society and the human race.",
         "Robotics represents overwhelmingly positive force for humanity",
         "muendlich",
         "https://stories.kuleuven.be/en/stories/inside-the-human-intelligence-of-pieter-abbeel",
         "Adapt to impact: inside the human intelligence of Pieter Abbeel",
         None,
         "en",
         "Expressing optimistic view on robotics impact"),

        # 9. On thinking about AI impact
        (PERSON_ID,
         "Whatever a human does a robot can do it is not the right way to think about it, and instead one should carefully consider what AI systems can do in the next couple of years where they can have the most impact.",
         "Don't think robots replace humans - focus on where AI has most impact",
         "muendlich",
         "https://stories.kuleuven.be/en/stories/inside-the-human-intelligence-of-pieter-abbeel",
         "Adapt to impact: inside the human intelligence of Pieter Abbeel",
         None,
         "en",
         "Nuanced perspective on AI deployment strategy"),

        # 10. On deep learning limitations
        (PERSON_ID,
         "There is a level of generality 'under the hood' that's doing the training of these neural nets even if the resulting neural net often ends up being a little specialized.",
         "Neural nets have generality in training but specialize in results",
         "muendlich",
         "https://www.nexxworks.com/blog/what-you-need-to-know-about-ai-according-to-pieter-abbeel",
         "What you need to know about AI according to Pieter Abbeel",
         None,
         "en",
         "Explaining limitations of current deep learning"),

        # 11. On AI breakthroughs
        (PERSON_ID,
         "The breakthroughs in AI of the past 5 years are only the icebreaker, making way for bigger ships to thrive in their wake.",
         "Recent AI breakthroughs are just the beginning",
         "muendlich",
         "https://www.nexxworks.com/blog/what-you-need-to-know-about-ai-according-to-pieter-abbeel",
         "What you need to know about AI according to Pieter Abbeel",
         None,
         "en",
         "Predicting future AI developments"),

        # 12. On future AI capabilities
        (PERSON_ID,
         "It's clear we're making a lot of progress, but it's just not clear what the gap is. It's also not clear to which extent the gap is a conceptual breakthrough sequence of things that we need to go through to get there.",
         "We're making progress but gaps to AGI remain unclear",
         "muendlich",
         "https://www.nexxworks.com/blog/what-you-need-to-know-about-ai-according-to-pieter-abbeel",
         "What you need to know about AI according to Pieter Abbeel",
         None,
         "en",
         "Discussing the path to more advanced AI"),

        # 13. On transfer learning expectations
        (PERSON_ID,
         "Once robots learn a task like putting a cap on a bottle, you'd expect it to transfer that knowledge to other, similar processes, such as for instance letting a hammer tap in a nail.",
         "Robots should transfer knowledge between similar tasks",
         "muendlich",
         "https://www.nexxworks.com/blog/what-you-need-to-know-about-ai-according-to-pieter-abbeel",
         "What you need to know about AI according to Pieter Abbeel",
         None,
         "en",
         "On the importance of transfer learning in robotics"),

        # 14. On multidisciplinary skills for AI
        (PERSON_ID,
         "It is very important for people who want to work in AI and robotics to have skills in more than one field. You should have a strong background in math (calculus, probability, linear algebra, and optimization), physics for modeling real-world problems, and programming skills in Python and deep learning frameworks like PyTorch or TensorFlow.",
         "AI researchers need math, physics, and programming skills",
         "muendlich",
         "https://odsc.medium.com/a-recap-of-our-interview-with-pieter-abbeel-on-deep-reinforcement-learning-95a5ccf2bca2",
         "A Recap of Our Interview with Pieter Abbeel on Deep Reinforcement Learning - ODSC",
         "2022-01-01",
         "en",
         "Interview discussing skill requirements for AI research"),

        # 15. On the Robot Brains podcast goal
        (PERSON_ID,
         "My goal is that if people listen to the podcast, they'll get an understanding of what AI can do, where it is in our lives and what it will become.",
         "Podcast aims to help people understand AI's current and future role",
         "muendlich",
         "https://engineering.berkeley.edu/news/2022/03/robots-ai-and-podcasting-a-qa-with-pieter-abbeel/",
         "Robots, AI and podcasting: a Q&A with Pieter Abbeel - Berkeley Engineering",
         "2022-03-01",
         "en",
         "Explaining the purpose of his Robot Brains podcast"),

        # 16. On ethical AI deployment
        (PERSON_ID,
         "I stress the ethical implications of AI, advocating for responsible deployment of robotics to ensure safety, job enhancement, and societal benefit.",
         "Advocate for responsible AI deployment ensuring safety and societal benefit",
         "schriftlich",
         "https://aiworld.eu/people/pieter-abbeel",
         "Pieter Abbeel - AI World",
         None,
         "en",
         "Statement on ethical considerations in AI development"),

        # 17. On Covariant's mission
        (PERSON_ID,
         "People will benefit immensely as the Covariant Brain gets more experience in customer environments and learns more general skills, eventually powering ever more robots in industrial-scale settings like manufacturing, agriculture, hospitality, commercial kitchens and homes.",
         "Covariant Brain will benefit people across many industries",
         "muendlich",
         "https://medium.com/covariant-ai/q-a-with-the-founders-dbd41dfcb208",
         "Q&A with the Founders - Covariant Blog",
         "2019-01-01",
         "en",
         "Interview at Covariant launch discussing future vision"),

        # 18. On RFM-1 capabilities
        (PERSON_ID,
         "RFM-1 provides robots the human-like ability to reason, representing the first time Generative AI has successfully given commercial robots a deeper understanding of language and the physical world.",
         "RFM-1 gives robots human-like reasoning and language understanding",
         "schriftlich",
         "https://covariant.ai/covariant-introduces-rfm-1-to-give-robots-the-human-like-ability-to-reason/",
         "Covariant introduces RFM-1 to give robots the human-like ability to reason",
         "2024-03-11",
         "en",
         "Announcement of RFM-1 robotics foundation model"),
    ]

    # HANDLUNGEN - Pieter Abbeel
    handlungen = [
        # 1. Co-founding Covariant
        (PERSON_ID,
         "gruendung",
         "Co-founded Covariant (originally Embodied Intelligence) with Peter Chen, Rocky Duan, and Tianhao Zhang to build AI foundation models for robotics in warehouses and factories",
         "2017-10-01",
         "https://en.wikipedia.org/wiki/Covariant_(company)",
         "Covariant (company) - Wikipedia",
         "Covariant focuses on building universal AI for robots"),

        # 2. Co-founding Gradescope
        (PERSON_ID,
         "gruendung",
         "Co-founded Gradescope with Arjun Singh, Sergey Karayev, and Ibrahim Awwal to use AI for streamlined grading in education",
         "2014-01-01",
         "https://www.crunchbase.com/organization/gradescope",
         "Gradescope - Crunchbase",
         "Platform for AI-assisted grading now used by hundreds of universities"),

        # 3. Gradescope acquisition by Turnitin
        (PERSON_ID,
         "verkauf",
         "Gradescope acquired by Turnitin, expanding educational technology tools for STEM assessment",
         "2018-10-01",
         "https://eecs.berkeley.edu/news/turnitin-acquires-gradescope/",
         "Turnitin Acquires Gradescope - EECS at Berkeley",
         "Acquisition allowed Gradescope to expand reach in educational institutions"),

        # 4. Covariant Series A funding
        (PERSON_ID,
         "investition",
         "Covariant raised $20 million Series A funding led by Amplify Partners",
         "2019-01-01",
         "https://www.crunchbase.com/organization/covariant",
         "Covariant - Crunchbase",
         "Early stage funding for robotics foundation models"),

        # 5. Covariant launch from stealth
        (PERSON_ID,
         "produktlaunch",
         "Covariant officially launched from stealth mode to bring universal AI to robots",
         "2020-01-01",
         "https://www.prnewswire.com/news-releases/covariant-launches-from-stealth-to-bring-universal-ai-to-robots-300995185.html",
         "Covariant launches from stealth to bring universal AI to robots",
         "Public announcement of Covariant Brain for warehouse robotics"),

        # 6. Covariant Series B funding
        (PERSON_ID,
         "investition",
         "Covariant raised $40 million Series B funding led by Index Ventures with participation from Radical Ventures and Amplify Partners",
         "2020-05-06",
         "https://techcrunch.com/2020/05/06/industrial-ai-startup-covariant-raises-a-40m-series-b/",
         "Industrial AI startup Covariant raises a $40M Series B - TechCrunch",
         "Funding to expand AI robotics to new industries"),

        # 7. Covariant Series C funding (first round)
        (PERSON_ID,
         "investition",
         "Covariant raised $80 million Series C funding led by Index Ventures with participation from Temasek and CPP Investments",
         "2021-07-27",
         "https://techcrunch.com/2021/07/27/robotic-ai-firm-covariant-raises-another-80-million/",
         "Robotic AI firm Covariant raises another $80 million - TechCrunch",
         "Total capitalization reached $147M within two years of public launch"),

        # 8. Launched The Robot Brains Podcast
        (PERSON_ID,
         "produktlaunch",
         "Launched 'The Robot Brains Podcast' featuring conversations with top AI and robotics experts and entrepreneurs",
         "2021-03-01",
         "https://shows.acast.com/the-robot-brains",
         "The Robot Brains Podcast - Hosted by Pieter Abbeel",
         "Podcast to educate public about AI and robotics developments"),

        # 9. Joined AIX Ventures as Investment Partner
        (PERSON_ID,
         "einstellung",
         "Joined AIX Ventures as Investment Partner, a venture capital fund investing in AI startups",
         "2021-01-01",
         "https://signal.nfx.com/investors/pieter-abbeel",
         "Pieter Abbeel's Investing Profile - AIX Ventures Partner",
         "Active angel investor with 18+ investments"),

        # 10. ACM Prize in Computing
        (PERSON_ID,
         "sonstiges",
         "Received ACM Prize in Computing for contributions to robot learning, including learning from demonstrations and deep reinforcement learning. Prize carries $250,000.",
         "2022-04-01",
         "https://awards.acm.org/about/2021-acm-prize",
         "UC Berkeley's Pieter Abbeel receives 2021 ACM Prize in Computing",
         "Recognition for pioneering apprenticeship learning and reinforcement learning for robotics"),

        # 11. Covariant Series C funding (second round)
        (PERSON_ID,
         "investition",
         "Covariant raised additional $75 million in Series C funding led by Index Ventures and Radical Ventures, bringing total funding to $222M",
         "2023-04-04",
         "https://www.indexventures.com/perspectives/congratulations-to-covariant-on-their-75m-series-c/",
         "Covariant Adds $75M in Series C Funds - Index Ventures",
         "Continued growth funding for robotics foundation models"),

        # 12. RFM-1 launch
        (PERSON_ID,
         "produktlaunch",
         "Covariant launched RFM-1, the first Robotics Foundation Model giving robots human-like reasoning capabilities with 8 billion parameters",
         "2024-03-11",
         "https://covariant.ai/covariant-introduces-rfm-1-to-give-robots-the-human-like-ability-to-reason/",
         "Covariant introduces RFM-1 to give robots the human-like ability to reason",
         "Multimodal model trained on text, images, video, robot actions and physics"),

        # 13. Amazon partnership and hiring
        (PERSON_ID,
         "partnerschaft",
         "Amazon entered non-exclusive licensing agreement with Covariant and hired 25% of workforce including founders Abbeel, Chen, and Duan",
         "2024-08-30",
         "https://finance.yahoo.com/news/amazon-hires-founders-ai-robotics-161000695.html",
         "Amazon hires the founders of AI robotics startup Covariant",
         "Major partnership bringing Covariant technology to Amazon fulfillment"),

        # 14. Amazon Distinguished Scientist appointment
        (PERSON_ID,
         "einstellung",
         "Joined Amazon as Distinguished Scientist and VP/Scholar focusing on advancing AI and robotics",
         "2024-08-01",
         "https://www.amazon.science/author/pieter-abbeel",
         "Pieter Abbeel - Amazon Science",
         "Joined Amazon Fulfillment Technologies & Robotics Team"),

        # 15. Amazon AGI leadership appointment
        (PERSON_ID,
         "einstellung",
         "Appointed head of Amazon's frontier model research team (LLM base models) in AGI organization while continuing robotics work",
         "2025-12-17",
         "https://www.ciodive.com/news/amazon-ai-chief-exits-leadership-shakeup/808189/",
         "Amazon AI chief exits, triggering leadership shakeup - CIO Dive",
         "Major leadership role overseeing Amazon's large language model development"),
    ]

    # Insert Aussagen
    print(f"Inserting {len(aussagen)} Aussagen for Pieter Abbeel (person_id={PERSON_ID})...")
    cursor.executemany("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussagen)

    # Insert Handlungen
    print(f"Inserting {len(handlungen)} Handlungen for Pieter Abbeel (person_id={PERSON_ID})...")
    cursor.executemany("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlungen)

    conn.commit()

    # Verify inserts
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    print(f"\n=== ERFOLG ===")
    print(f"Total Aussagen für Pieter Abbeel: {aussagen_count}")
    print(f"Total Handlungen für Pieter Abbeel: {handlungen_count}")
    print(f"Gesamtzahl: {aussagen_count + handlungen_count}")

    conn.close()

if __name__ == "__main__":
    insert_data()
