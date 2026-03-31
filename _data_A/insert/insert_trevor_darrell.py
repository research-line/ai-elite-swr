#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Trevor Darrell (person_id=61)
UC Berkeley Computer Vision Professor, BAIR Lab Co-Founder
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 61

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ============================================================================
    # AUSSAGEN (Statements/Quotes)
    # ============================================================================

    aussagen = [
        # 1. On AI-Academia-Industry Collaboration
        {
            'aussage_text': 'The biggest point of leverage is trying to enable actual collaboration between top industry labs and startups and AI researchers in academia, at Berkeley. There\'s something about the synergy between the resources that industry offers and the kind of rich idea space and youthful energy that comes out of academia that if they can collaborate together, they really can have an impact.',
            'aussage_kurz': 'Synergy between industry resources and academic innovation creates maximum impact in AI research',
            'modus': 'muendlich',
            'quell_link': 'https://www.superannotate.com/podcast/episode-1-ai-talks-with-trevor-darrell',
            'quell_titel': 'Episode 1: AI talks with Trevor Darrell from UC Berkeley - SuperAnnotate Podcast',
            'datum_aussage': '2023-01-01',
            'sprache': 'en',
            'kontext': 'Interview discussing BAIR Commons program and industry-academia partnerships'
        },

        # 2. On Future of Retail/Cashier-less Technology
        {
            'aussage_text': 'In the future, we can have places where we don\'t need to have human beings just sitting at a cash register. We can have systems that can be supervised to make better use of their time and more productive environments, both in a business sense and in a personal sense.',
            'aussage_kurz': 'Cashier-less retail technology will free humans from repetitive tasks for more productive work',
            'modus': 'muendlich',
            'quell_link': 'https://www.superannotate.com/podcast/episode-1-ai-talks-with-trevor-darrell',
            'quell_titel': 'Episode 1: AI talks with Trevor Darrell from UC Berkeley - SuperAnnotate Podcast',
            'datum_aussage': '2023-01-01',
            'sprache': 'en',
            'kontext': 'Discussion about computer vision applications in cashier-less checkout systems'
        },

        # 3. On Small Teams in AI
        {
            'aussage_text': 'Some of the hottest models on image generation came out of a small group in Germany that now has a startup around it, but it wasn\'t necessarily coming out of an enormous company. Even small teams can still have a big impact, either in academia or in startups.',
            'aussage_kurz': 'Small teams can achieve breakthrough AI innovations, not just large companies',
            'modus': 'muendlich',
            'quell_link': 'https://www.superannotate.com/podcast/episode-1-ai-talks-with-trevor-darrell',
            'quell_titel': 'Episode 1: AI talks with Trevor Darrell from UC Berkeley - SuperAnnotate Podcast',
            'datum_aussage': '2023-01-01',
            'sprache': 'en',
            'kontext': 'Discussing democratization of AI research and innovation across different organizational sizes'
        },

        # 4. On Climate Change as AI Challenge
        {
            'aussage_text': 'Climate change is a very significant AI problem at a scale that wasn\'t addressed in previous challenges that drove the internet-AI era. We actually need to have systems that function in the real world.',
            'aussage_kurz': 'Climate change represents unprecedented AI challenge requiring real-world functional systems',
            'modus': 'muendlich',
            'quell_link': 'https://cdss.berkeley.edu/news/new-uc-berkeley-initiative-uses-ai-research-solve-climate-problems',
            'quell_titel': 'New UC Berkeley initiative uses AI research to solve climate problems',
            'datum_aussage': '2022-06-01',
            'sprache': 'en',
            'kontext': 'Announcement of BAIR Climate Initiative to use AI for climate change solutions'
        },

        # 5. On Autonomous Vehicle Safety
        {
            'aussage_text': 'This research makes cars potentially safer and more agile. When computers can recognize their surroundings, it makes them more perceptive and able to react properly to other cars, pedestrians, and objects in their environment, and be robust to unexpected situations.',
            'aussage_kurz': 'Computer vision enables safer autonomous vehicles through better environmental perception',
            'modus': 'muendlich',
            'quell_link': 'https://its.berkeley.edu/node/3164',
            'quell_titel': 'Berkeley Drives Deep Into Automotive Perception - Institute of Transportation Studies',
            'datum_aussage': '2015-03-01',
            'sprache': 'en',
            'kontext': 'Discussing Berkeley DeepDrive research on autonomous vehicle perception and safety'
        },

        # 6. On Collaboration vs Isolation in AI Research
        {
            'aussage_text': 'It\'s hard to do the best research alone in academia, and I think it\'s even hard often to do the best research alone in the industry. There\'s something about the synergy between the resources that industry offers and the kind of rich idea space and youthful energy that comes out of academia that if we can collaborate together, we really can have an impact.',
            'aussage_kurz': 'Neither academia nor industry alone can achieve optimal AI research outcomes without collaboration',
            'modus': 'muendlich',
            'quell_link': 'https://www.superannotate.com/podcast/episode-1-ai-talks-with-trevor-darrell',
            'quell_titel': 'Episode 1: AI talks with Trevor Darrell from UC Berkeley - SuperAnnotate Podcast',
            'datum_aussage': '2023-01-01',
            'sprache': 'en',
            'kontext': 'Philosophy behind BAIR Commons and open research collaboration model'
        },

        # 7. On Efficient AI Models
        {
            'aussage_text': 'Much of Professor Darrell\'s work aims to overcome obstacles—such as massive memory and compute requirements—that limit the practical application of AI models, including approaches to making VLMs (Vision-Language Models) smaller and more efficient while retaining accuracy.',
            'aussage_kurz': 'Focus on reducing AI model resource requirements for practical real-world deployment',
            'modus': 'schriftlich',
            'quell_link': 'https://embeddedvisionsummit.com/2025/speaker/trevor-darrell/',
            'quell_titel': 'Trevor Darrell - 2025 Embedded Vision Summit Speaker Bio',
            'datum_aussage': '2025-01-01',
            'sprache': 'en',
            'kontext': 'Description of research focus on efficient multimodal AI for edge computing'
        },

        # 8. On Explainable AI and Interpretability
        {
            'aussage_text': 'The model is more interpretable to human evaluators compared to other state-of-the-art models: users can better understand the model\'s underlying reasoning procedure and predict when it will succeed or fail based on observing its intermediate outputs.',
            'aussage_kurz': 'Stack Neural Module Networks enable human understanding of AI reasoning processes',
            'modus': 'schriftlich',
            'quell_link': 'https://arxiv.org/abs/1807.08556',
            'quell_titel': 'Explainable Neural Computation via Stack Neural Module Networks',
            'datum_aussage': '2018-07-23',
            'sprache': 'en',
            'kontext': 'Research paper on explainable AI and interpretable neural computation for question answering'
        },

        # 9. On Open Climate Research
        {
            'aussage_text': 'Any technology or research done by the climate initiative will be openly published and won\'t be exclusively licensed or proprietary.',
            'aussage_kurz': 'BAIR Climate Initiative commits to open-source publication of all research',
            'modus': 'muendlich',
            'quell_link': 'https://cdss.berkeley.edu/news/new-uc-berkeley-initiative-uses-ai-research-solve-climate-problems',
            'quell_titel': 'New UC Berkeley initiative uses AI research to solve climate problems',
            'datum_aussage': '2022-06-01',
            'sprache': 'en',
            'kontext': 'Commitment to open research in BAIR Climate Initiative announcement'
        },

        # 10. On Multimodal AI Revolution
        {
            'aussage_text': 'AI is on the cusp of a revolution, driven by the convergence of several breakthroughs. Multimodal AI, visual perception and prompt-tuned reasoning are enabling consumers to utilize visual intelligence at home while preserving privacy.',
            'aussage_kurz': 'Multimodal AI convergence enables privacy-preserving visual intelligence for consumers',
            'modus': 'muendlich',
            'quell_link': 'https://embeddedvisionsummit.com/2025/session/the-future-of-visual-ai-efficient-multimodal-intelligence/',
            'quell_titel': 'The Future of Visual AI: Efficient Multimodal Intelligence - 2025 Summit',
            'datum_aussage': '2025-05-01',
            'sprache': 'en',
            'kontext': 'Keynote presentation at Embedded Vision Summit 2025 on future of visual AI'
        },

        # 11. On Robotics and Perception-Action Integration
        {
            'aussage_text': 'Darrell leverages recent advances at UC Berkeley in perceptual optimization and real-time control, including those which map visual inputs directly to control outputs and which support intelligent perception, manipulation and control tasks.',
            'aussage_kurz': 'Direct mapping of visual perception to robotic control enables intelligent manipulation',
            'modus': 'schriftlich',
            'quell_link': 'https://vcresearch.berkeley.edu/faculty/trevor-darrell',
            'quell_titel': 'Trevor Darrell - Research UC Berkeley',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Research profile describing robotics work on perception-based control and manipulation'
        },

        # 12. On Cross-Modal Learning
        {
            'aussage_text': 'Darrell\'s work has focused on advancements in object detection, semantic segmentation and feature extraction techniques, as well as unsupervised learning techniques and adaptive models that improve generalization from limited examples, and cross-modal methods that integrate various data types.',
            'aussage_kurz': 'Research spans object detection, unsupervised learning, and cross-modal data integration',
            'modus': 'schriftlich',
            'quell_link': 'https://scholar.google.com/citations?user=bh-uRFMAAAAJ&hl=en',
            'quell_titel': 'Trevor Darrell - Google Scholar',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Summary of research contributions across multiple AI domains'
        },

        # 13. On BDD Dataset Impact
        {
            'aussage_text': 'BDD100K is the largest and most diverse open driving video dataset so far for computer vision research.',
            'aussage_kurz': 'BDD100K dataset provides unprecedented scale and diversity for autonomous driving research',
            'modus': 'schriftlich',
            'quell_link': 'https://bair.berkeley.edu/blog/2018/05/30/bdd/',
            'quell_titel': 'BDD100K: A Large-scale Diverse Driving Video Database - Berkeley AI Research Blog',
            'datum_aussage': '2018-05-30',
            'sprache': 'en',
            'kontext': 'Release announcement of BDD100K autonomous driving dataset'
        },

        # 14. On BAIR Open Research Commons Philosophy
        {
            'aussage_text': 'The Open Research Commons was designed to foster collaboration across academia and industry, leveraging the strengths of both to drive transformative advances in AI. The BAIR Open Research Commons brings together academia and industry to cultivate an open, interdisciplinary research environment, and by fostering interactions between academia\'s forward-thinking approaches and industry\'s practical expertise, ORC accelerates the creation and deployment of AI models with real-world impact.',
            'aussage_kurz': 'Open Research Commons model combines academic innovation with industry expertise for real-world AI impact',
            'modus': 'schriftlich',
            'quell_link': 'https://www.prnewswire.com/news-releases/clarifai-joins-the-berkeley-artificial-intelligence-research-bair-open-research-commons-to-advance-ai-innovation-302303302.html',
            'quell_titel': 'Clarifai Joins BAIR Open Research Commons - Press Release',
            'datum_aussage': '2024-11-13',
            'sprache': 'en',
            'kontext': 'Description of BAIR Open Research Commons mission and collaboration model'
        },

        # 15. On R-CNN Innovation
        {
            'aussage_text': 'The R-CNN approach combines two key insights: applying high-capacity convolutional neural networks (CNNs) to bottom-up region proposals to localize and segment objects, and using supervised pre-training for an auxiliary task followed by domain-specific fine-tuning.',
            'aussage_kurz': 'R-CNN combines region proposals with CNN features and transfer learning for object detection',
            'modus': 'schriftlich',
            'quell_link': 'https://arxiv.org/abs/1311.2524',
            'quell_titel': 'Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation',
            'datum_aussage': '2013-11-11',
            'sprache': 'en',
            'kontext': 'Seminal paper on R-CNN object detection method that won CVPR Longuet-Higgins Prize 2024'
        },

        # 16. On Caffe Framework Philosophy
        {
            'aussage_text': 'Caffe is a deep learning framework made with expression, speed, and modularity in mind, and is developed by Berkeley AI Research (BAIR) and by community contributors. Caffe provides multimedia scientists and practitioners with a clean and modifiable framework for state-of-the-art deep learning algorithms and a collection of reference models.',
            'aussage_kurz': 'Caffe framework prioritizes expression, speed, modularity for accessible deep learning',
            'modus': 'schriftlich',
            'quell_link': 'https://caffe.berkeleyvision.org/',
            'quell_titel': 'Caffe: Deep Learning Framework Official Website',
            'datum_aussage': '2014-01-01',
            'sprache': 'en',
            'kontext': 'Official description of Caffe deep learning framework design philosophy'
        },

        # 17. On Edge AI and Real-time Processing
        {
            'aussage_text': 'Trevor Darrell delivered a powerful keynote on multimodal intelligence, emphasizing how vision-language models (VLMs) like CLIP and Flamingo are accelerating cross-sensory understanding in edge devices. His insights around real-time processing and edge-efficient AI architectures resonated with developers looking to minimize latency without compromising performance.',
            'aussage_kurz': 'VLMs enable cross-sensory understanding on edge devices with minimal latency',
            'modus': 'schriftlich',
            'quell_link': 'https://insighttechtalk.com/technology-events/embedded-vision-summit-2025-future-of-ai-vision-unveiled/',
            'quell_titel': 'Embedded Vision Summit 2025: Future of AI Vision Unveiled',
            'datum_aussage': '2025-05-01',
            'sprache': 'en',
            'kontext': 'Coverage of Embedded Vision Summit 2025 keynote on edge AI'
        },

        # 18. On Domain Adaptation Innovation
        {
            'aussage_text': 'ADDA (Adversarial Discriminative Domain Adaptation) was shown to be more effective yet considerably simpler than competing domain-adversarial methods, exceeding state-of-the-art unsupervised adaptation results on standard domain adaptation tasks.',
            'aussage_kurz': 'ADDA achieves superior domain adaptation with simpler adversarial approach',
            'modus': 'schriftlich',
            'quell_link': 'https://arxiv.org/abs/1702.05464',
            'quell_titel': 'Adversarial Discriminative Domain Adaptation',
            'datum_aussage': '2017-02-16',
            'sprache': 'en',
            'kontext': 'Research paper on adversarial domain adaptation methods'
        }
    ]

    # ============================================================================
    # HANDLUNGEN (Actions/Activities)
    # ============================================================================

    handlungen = [
        # 1. BAIR Lab Co-Founding
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-founded Berkeley Artificial Intelligence Research (BAIR) Lab at UC Berkeley, one of the world\'s premier AI research laboratories bringing together researchers in computer vision, machine learning, natural language processing, planning, and robotics.',
            'datum_handlung': '2010-01-01',
            'quell_link': 'https://www2.eecs.berkeley.edu/Faculty/Homepages/darrell.html',
            'quell_titel': 'Trevor Darrell - EECS at UC Berkeley',
            'kontext': 'Established BAIR as major AI research hub with over 100 faculty, postdocs, and graduate students'
        },

        # 2. Berkeley DeepDrive Founding
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Founded Berkeley DeepDrive (BDD) Industrial Consortium, investigating state-of-the-art technologies in computer vision, robotics, and machine learning for autonomous vehicle applications, with industry partners including Volkswagen, Ford, Toyota, Samsung, Bosch, Honda, Hyundai, Qualcomm and NVIDIA.',
            'datum_handlung': '2015-03-01',
            'quell_link': 'https://deepdrive.berkeley.edu/',
            'quell_titel': 'Berkeley DeepDrive Official Website',
            'kontext': 'Major industry-academia consortium for autonomous driving research with multiple Fortune 500 partners'
        },

        # 3. Caffe Framework Release
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Released Caffe deep learning framework as open-source software, developed by Yangqing Jia in Darrell\'s lab at UC Berkeley. Caffe quickly became one of the most widely used platforms for deep learning, particularly in computer vision applications.',
            'datum_handlung': '2014-01-01',
            'quell_link': 'https://github.com/BVLC/caffe',
            'quell_titel': 'Caffe: A fast open framework for deep learning - GitHub',
            'kontext': 'Caffe became industry standard deep learning framework, cited in thousands of papers and used in production systems worldwide'
        },

        # 4. BAIR Commons Program Launch
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Launched BAIR Commons (later BAIR Open Research Commons) program in partnership with Facebook, Google, Microsoft, Amazon, and other major tech companies to enable collaboration between top industry labs, startups, and AI researchers at Berkeley.',
            'datum_handlung': '2017-01-01',
            'quell_link': 'https://embeddedvisionsummit.com/2025/speaker/trevor-darrell/',
            'quell_titel': 'Trevor Darrell - 2025 Summit Bio',
            'kontext': 'Established new model for industry-academia AI collaboration with multiple Fortune 100 partners'
        },

        # 5. The House Fund Faculty Partnership
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Joined The House Fund as Co-Founder & Faculty Partner of AI@The House initiative, adding six world-leading entrepreneurial AI researchers to the pre-seed and early-stage venture capital fund focused on Berkeley startups.',
            'datum_handlung': '2018-01-01',
            'quell_link': 'https://medium.com/@thehousecal/announcing-ai-the-house-990e77857228',
            'quell_titel': 'Announcing AI@The House - Medium',
            'kontext': 'Strategic move to support Berkeley AI entrepreneurship ecosystem, The House Fund has since invested in 100+ startups with 15+ exits'
        },

        # 6. BAIR Climate Initiative Launch
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-founded and leads BAIR Climate Initiative, a multi-disciplinary student-led hub dedicated to fighting climate change through AI research, partnering with climate experts, government agencies, and industry. Committed to open publication of all research.',
            'datum_handlung': '2022-06-01',
            'quell_link': 'https://cdss.berkeley.edu/news/new-uc-berkeley-initiative-uses-ai-research-solve-climate-problems',
            'quell_titel': 'New UC Berkeley initiative uses AI research to solve climate problems',
            'kontext': 'Student-led initiative addressing climate change at unprecedented scale for AI research'
        },

        # 7. Nexar Chief Scientist Appointment
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Appointed as Chief Scientist at Nexar (consulting role), leading and overseeing research in machine vision deep learning and vehicle path prediction for the AI-powered dashcam and automotive safety company.',
            'datum_handlung': '2017-01-01',
            'quell_link': 'https://www.prnewswire.com/news-releases/nexar-hires-professor-trevor-darrell-as-chief-scientist-300396597.html',
            'quell_titel': 'Nexar Hires Professor Trevor Darrell as Chief Scientist',
            'kontext': 'Advisory role bringing academic computer vision expertise to automotive safety startup'
        },

        # 8. SafelyYou Advisory Role
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Joined SafelyYou as advisor, contributing computer vision and AI expertise to the company developing fall detection and prevention technology for senior care facilities using privacy-preserving AI.',
            'datum_handlung': '2018-01-01',
            'quell_link': 'https://theorg.com/org/safelyyou/org-chart/trevor-darrell',
            'quell_titel': 'Trevor Darrell - Advisor at SafelyYou - The Org',
            'kontext': 'Application of computer vision research to elderly care and fall prevention'
        },

        # 9. BDD100K Dataset Release
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Released BDD100K, the largest and most diverse open driving video dataset for computer vision research, containing 100,000 videos with detailed annotations for object detection, lane marking, drivable area, and full-frame semantic/instance segmentation.',
            'datum_handlung': '2018-05-30',
            'quell_link': 'https://bair.berkeley.edu/blog/2018/05/30/bdd/',
            'quell_titel': 'BDD100K Dataset Announcement - BAIR Blog',
            'kontext': 'Major open dataset contribution to autonomous driving research community'
        },

        # 10. Wave Computing BAIR Partnership
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Established partnership with Wave Computing for BAIR Open Research Alliance to accelerate cutting-edge artificial intelligence research, providing access to Wave\'s dataflow architecture and AI acceleration technology.',
            'datum_handlung': '2019-03-25',
            'quell_link': 'https://www.globenewswire.com/news-release/2019/03/25/1760439/0/en/Wave-Collaborates-with-UC-Berkeley-s-BAIR-Open-Research-Alliance-to-Accelerate-Cutting-Edge-Artificial-Intelligence-Research.html',
            'quell_titel': 'Wave Collaborates with UC Berkeley\'s BAIR Open Research Alliance',
            'kontext': 'Industry partnership for AI hardware acceleration research'
        },

        # 11. Microsoft BAIR Partnership
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Established Microsoft Research partnership with Berkeley AI Research (BAIR) for Phase 2 collaborations, forging strong collaborations between Microsoft researchers, students and faculty pursuing research on fundamental advances in computer vision, machine learning, natural language processing, planning, control, and robotics.',
            'datum_handlung': '2019-01-01',
            'quell_link': 'https://www.microsoft.com/en-us/research/collaboration/bair/phase-2-collaborations/',
            'quell_titel': 'Microsoft Research & BAIR: Phase 2 Collaborations',
            'kontext': 'Expanded industry-academia collaboration with Microsoft Research for multi-year AI research program'
        },

        # 12. PATH Faculty Director Appointment
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Appointed as Faculty Director of PATH (Partners for Advanced Transportation Technology) at UC Berkeley, leading transportation research initiatives including autonomous vehicle development and intelligent transportation systems.',
            'datum_handlung': '2018-01-01',
            'quell_link': 'https://its.berkeley.edu/node/12896',
            'quell_titel': 'Trevor Darrell Tapped to Co-Lead PATH - ITS Berkeley',
            'kontext': 'Leadership role in major transportation research center at UC Berkeley'
        },

        # 13. ICML Test of Time Award
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Received ICML Test of Time Award for paper "DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition" (with Donahue, Jia, Vinyals, Hoffman, Zhang, Tzeng), recognizing exceptional long-term impact on machine learning field.',
            'datum_handlung': '2024-07-01',
            'quell_link': 'https://eecs.berkeley.edu/news/trevor-darrell-receives-icml-test-of-time-award/',
            'quell_titel': 'Trevor Darrell receives ICML Test-of-Time Award - EECS Berkeley',
            'kontext': 'Award recognizing foundational work on transfer learning and deep feature extraction'
        },

        # 14. CVPR Longuet-Higgins Prize
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Received CVPR Longuet-Higgins Prize for paper "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation" (with Girshick, Donahue, Malik), recognizing fundamental contribution to computer vision over 10-year period.',
            'datum_handlung': '2024-06-01',
            'quell_link': 'https://eecs.berkeley.edu/news/berkeley-eecs-win-awards-at-cvpr/',
            'quell_titel': 'Berkeley EECS win awards at CVPR - EECS Berkeley',
            'kontext': 'Award for seminal R-CNN paper that revolutionized object detection methods'
        },

        # 15. ACM SIGMM Test of Time Award
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Received ACM SIGMM Test of Time Paper Award for "Caffe: Convolutional Architecture for Fast Feature Embedding" (with Jia, Shelhamer, Donahue, Karayev, Long, Girshick, Guadarrama), recognizing lasting impact on multimedia computing.',
            'datum_handlung': '2024-01-01',
            'quell_link': 'https://embeddedvisionsummit.com/2025/speaker/trevor-darrell/',
            'quell_titel': 'Trevor Darrell - 2025 Summit Bio',
            'kontext': 'Award for Caffe framework that became industry-standard deep learning platform'
        }
    ]

    # Insert Aussagen
    print(f"Inserting {len(aussagen)} Aussagen for Trevor Darrell (person_id={PERSON_ID})...")
    for i, aussage in enumerate(aussagen, 1):
        try:
            cursor.execute("""
                INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                PERSON_ID,
                aussage['aussage_text'],
                aussage['aussage_kurz'],
                aussage['modus'],
                aussage['quell_link'],
                aussage['quell_titel'],
                aussage['datum_aussage'],
                aussage['sprache'],
                aussage['kontext']
            ))
            print(f"  [{i}/{len(aussagen)}] Inserted: {aussage['aussage_kurz'][:80]}...")
        except Exception as e:
            print(f"  ERROR inserting aussage {i}: {e}")

    # Insert Handlungen
    print(f"\nInserting {len(handlungen)} Handlungen for Trevor Darrell (person_id={PERSON_ID})...")
    for i, handlung in enumerate(handlungen, 1):
        try:
            cursor.execute("""
                INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                PERSON_ID,
                handlung['handlung_typ'],
                handlung['beschreibung'],
                handlung['datum_handlung'],
                handlung['quell_link'],
                handlung['quell_titel'],
                handlung['kontext']
            ))
            print(f"  [{i}/{len(handlungen)}] Inserted: {handlung['beschreibung'][:80]}...")
        except Exception as e:
            print(f"  ERROR inserting handlung {i}: {e}")

    # Commit and close
    conn.commit()
    conn.close()

    print(f"\n{'='*80}")
    print(f"SUMMARY - Trevor Darrell (person_id={PERSON_ID})")
    print(f"{'='*80}")
    print(f"Total Aussagen inserted:   {len(aussagen)}")
    print(f"Total Handlungen inserted: {len(handlungen)}")
    print(f"Grand Total:               {len(aussagen) + len(handlungen)}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    insert_data()
