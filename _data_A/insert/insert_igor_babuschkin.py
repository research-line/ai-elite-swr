#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert statements and actions for Igor Babuschkin (person_id=88) into aussagen_top100.db
Data collected from web research on 2026-02-12
"""

import sqlite3
import os

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Check if database exists
if not os.path.exists(DB_PATH):
    print(f"ERROR: Database not found at {DB_PATH}")
    exit(1)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

person_id = 88  # Igor Babuschkin

# ============================================================================
# AUSSAGEN (Statements)
# ============================================================================

aussagen = [
    # 1
    {
        'person_id': person_id,
        'aussage_text': 'Very soon AI could reason beyond the level of humans.',
        'aussage_kurz': 'AI will soon reason beyond human level',
        'modus': 'schriftlich',
        'quell_link': 'https://siliconangle.com/2025/08/13/xai-co-founder-igor-babuschkin-leaving-company-focus-ai-safety/',
        'quell_titel': 'Igor Babuschkin, co-founder of Elon Musk\'s xAI, is leaving the company to focus on AI safety - SiliconANGLE',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Statement about AI capabilities when announcing departure from xAI to focus on AI safety'
    },
    # 2
    {
        'person_id': person_id,
        'aussage_text': 'The same curiosity that asks "what is matter?" must ultimately ask "what is mind?" I\'ve spent my career chasing that question—and I believe we\'re closer than ever to understanding it.',
        'aussage_kurz': 'Physics curiosity leads to understanding mind through AI',
        'modus': 'schriftlich',
        'quell_link': 'https://babuschk.in/about.html',
        'quell_titel': 'About - Igor Babuschkin',
        'datum_aussage': '2025-08-01',
        'sprache': 'en',
        'kontext': 'Personal statement on website about connecting physics background to AI research'
    },
    # 3
    {
        'person_id': person_id,
        'aussage_text': 'Building AI that advances humanity has been my lifelong dream.',
        'aussage_kurz': 'Building AI to advance humanity is lifelong dream',
        'modus': 'schriftlich',
        'quell_link': 'https://babuschk.in/about.html',
        'quell_titel': 'About - Igor Babuschkin',
        'datum_aussage': '2025-08-01',
        'sprache': 'en',
        'kontext': 'Statement of personal mission on personal website'
    },
    # 4
    {
        'person_id': person_id,
        'aussage_text': 'I believe in building tools that let us do more than we ever could alone—technology that elevates rather than replaces. The question isn\'t whether AI will transform humanity—it\'s how.',
        'aussage_kurz': 'Technology should elevate not replace humans',
        'modus': 'schriftlich',
        'quell_link': 'https://babuschk.in/about.html',
        'quell_titel': 'About - Igor Babuschkin',
        'datum_aussage': '2025-08-01',
        'sprache': 'en',
        'kontext': 'Statement on technology philosophy regarding AI and human augmentation'
    },
    # 5
    {
        'person_id': person_id,
        'aussage_text': 'I still remember the day I first met Elon, we talked for hours about AI and what the future might hold. We both felt that a new AI company with a different kind of mission was needed.',
        'aussage_kurz': 'Meeting with Musk led to founding xAI with different mission',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/ibab/status/1955741698690322585',
        'quell_titel': 'Igor Babuschkin on X - Last day at xAI announcement',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Recalling first meeting with Elon Musk when announcing departure from xAI'
    },
    # 6
    {
        'person_id': person_id,
        'aussage_text': 'The singularity is near, but humanity\'s future is bright.',
        'aussage_kurz': 'Singularity is near but humanity\'s future is bright',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/ibab/status/1955741698690322585',
        'quell_titel': 'Igor Babuschkin on X - Last day at xAI announcement',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Statement in departure announcement from xAI, expressing optimism about AI future'
    },
    # 7
    {
        'person_id': person_id,
        'aussage_text': 'As frontier models become more agentic over longer horizons and a wider range of tasks, they will take on more and more powerful capabilities, which will make it critical to study and advance AI safety.',
        'aussage_kurz': 'Agentic AI over longer horizons requires critical safety research',
        'modus': 'schriftlich',
        'quell_link': 'https://winbuzzer.com/2025/08/14/xai-co-founder-igor-babuschkin-departs-to-launch-ai-safety-venture-xcxwbn/',
        'quell_titel': 'xAI Co-Founder Igor Babuschkin Departs to Launch AI Safety Venture - WinBuzzer',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Explaining rationale for launching AI safety venture when leaving xAI'
    },
    # 8
    {
        'person_id': person_id,
        'aussage_text': 'xAI executes at ludicrous speed. Industry veterans told us that building the Memphis supercluster in 120 days would be impossible, but we believed we could do the impossible.',
        'aussage_kurz': 'xAI executes at ludicrous speed doing the impossible',
        'modus': 'schriftlich',
        'quell_link': 'https://www.entrepreneur.com/business-news/xai-cofounder-says-he-learned-2-major-lessons-from-elon-musk/495933',
        'quell_titel': 'xAI Cofounder Says He Learned 2 Major Lessons From Elon Musk - Entrepreneur',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Describing working culture at xAI and Memphis supercomputer project'
    },
    # 9
    {
        'person_id': person_id,
        'aussage_text': 'I learned two priceless lessons from Elon: #1 be fearless in rolling up your sleeves to personally dig into technical problems, #2 have a maniacal sense of urgency.',
        'aussage_kurz': 'Learned fearless hands-on approach and urgency from Musk',
        'modus': 'schriftlich',
        'quell_link': 'https://www.entrepreneur.com/business-news/xai-cofounder-says-he-learned-2-major-lessons-from-elon-musk/495933',
        'quell_titel': 'xAI Cofounder Says He Learned 2 Major Lessons From Elon Musk - Entrepreneur',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Reflecting on lessons learned from Elon Musk at xAI'
    },
    # 10
    {
        'person_id': person_id,
        'aussage_text': 'Towards the end of our 120 day deadline, we were riddled with mysterious issues with communicating over RDMA between the machines, so Elon decided to fly to the datacenter. The infra team landed in Memphis in the middle of the night and got straight to work, and after pouring through tens of thousands of lines of lspci output they finally identified a wrong BIOS setting.',
        'aussage_kurz': 'Musk flew to Memphis datacenter at night to debug RDMA issues',
        'modus': 'schriftlich',
        'quell_link': 'https://www.entrepreneur.com/business-news/xai-cofounder-says-he-learned-2-major-lessons-from-elon-musk/495933',
        'quell_titel': 'xAI Cofounder Says He Learned 2 Major Lessons From Elon Musk - Entrepreneur',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Recounting hands-on example of Musk\'s involvement in Memphis supercomputer crisis'
    },
    # 11
    {
        'person_id': person_id,
        'aussage_text': 'I recently had dinner with Max Tegmark, founder of the Future of Life Institute. Over dinner Max showed me a photo of his two young sons and asked "how can we build AI safely to ensure that our children can flourish?" I was deeply moved by his question.',
        'aussage_kurz': 'Tegmark\'s question about children\'s future deeply moved me',
        'modus': 'schriftlich',
        'quell_link': 'https://the-decoder.com/a-conversation-with-max-tegmark-inspired-ai-co-founder-igor-babuschkin-shift-to-safer-ai/',
        'quell_titel': 'A conversation with Max Tegmark inspired AI co-founder Igor Babuschkin shift to safer AI',
        'datum_aussage': '2025-08-01',
        'sprache': 'en',
        'kontext': 'Explaining conversation with Max Tegmark that influenced decision to focus on AI safety'
    },
    # 12
    {
        'person_id': person_id,
        'aussage_text': 'In 122 days, xAI transformed an abandoned Electrolux factory in Memphis into "Colossus," with 100,000 Nvidia H100 GPUs, then doubled it to 200,000 in another 92 days.',
        'aussage_kurz': 'Built Colossus supercomputer with 100k H100s in 122 days',
        'modus': 'schriftlich',
        'quell_link': 'https://www.rdworldonline.com/how-xai-turned-a-factory-shell-into-an-ai-colossus-to-power-grok-3-and-beyond/',
        'quell_titel': 'How xAI turned a factory shell into an AI Colossus for Grok 3',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Describing the rapid construction of xAI\'s Memphis supercomputer facility'
    },
    # 13
    {
        'person_id': person_id,
        'aussage_text': 'Maybe the real ASI was the friends we made along the way.',
        'aussage_kurz': 'Maybe real ASI was the friends we made along the way',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/ibab',
        'quell_titel': 'Igor Babuschkin (@ibab) on X',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Playful statement referencing artificial superintelligence (ASI) and team relationships'
    },
    # 14
    {
        'person_id': person_id,
        'aussage_text': 'I\'m announcing the launch of Babuschkin Ventures, which supports AI safety research and backs startups in AI and agentic systems that advance humanity and unlock the mysteries of our universe.',
        'aussage_kurz': 'Launching Babuschkin Ventures for AI safety and agentic systems',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/ibab/status/1955741698690322585',
        'quell_titel': 'Igor Babuschkin on X - Babuschkin Ventures announcement',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Announcing new venture fund focused on AI safety when leaving xAI'
    },
    # 15
    {
        'person_id': person_id,
        'aussage_text': 'Igor Babuschkin calls it "the biggest, fully connected H100 cluster of its kind."',
        'aussage_kurz': 'Colossus is biggest fully connected H100 cluster',
        'modus': 'schriftlich',
        'quell_link': 'https://www.rdworldonline.com/how-xai-turned-a-factory-shell-into-an-ai-colossus-to-power-grok-3-and-beyond/',
        'quell_titel': 'How xAI turned a factory shell into an AI Colossus for Grok 3',
        'datum_aussage': '2024-12-01',
        'sprache': 'en',
        'kontext': 'Describing technical achievement of Memphis Colossus supercomputer'
    },
    # 16
    {
        'person_id': person_id,
        'aussage_text': 'Building AI that advances humanity has been my lifelong dream. At xAI, I had the chance to push the frontiers of what\'s possible.',
        'aussage_kurz': 'At xAI pushed frontiers of AI possibilities',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/ibab/status/1955741698690322585',
        'quell_titel': 'Igor Babuschkin on X - Last day at xAI',
        'datum_aussage': '2025-08-13',
        'sprache': 'en',
        'kontext': 'Reflecting on time at xAI in departure announcement'
    },
    # 17
    {
        'person_id': person_id,
        'aussage_text': 'On GitHub he contributed a core TensorFlow implementation of DeepMind\'s WaveNet—adding dilated convolutions, mu-law encoding/decoding, CLI, logging and other production features—showing attention to both model design and engineering.',
        'aussage_kurz': 'Contributed production-ready TensorFlow WaveNet implementation',
        'modus': 'schriftlich',
        'quell_link': 'https://github.com/ibab',
        'quell_titel': 'ibab (Igor Babuschkin) on GitHub',
        'datum_aussage': '2016-06-01',
        'sprache': 'en',
        'kontext': 'Description of open source contributions to deep learning community'
    },
    # 18
    {
        'person_id': person_id,
        'aussage_text': 'The work advanced agentic systems by employing population-based training across diverse agents in a league format, enabling robust policies that handle imperfect information and long-term planning, surpassing 99.8% of human players.',
        'aussage_kurz': 'AlphaStar surpassed 99.8% of human StarCraft players',
        'modus': 'schriftlich',
        'quell_link': 'https://deepmind.google/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/',
        'quell_titel': 'AlphaStar: Grandmaster level in StarCraft II - DeepMind',
        'datum_aussage': '2019-10-30',
        'sprache': 'en',
        'kontext': 'Describing technical achievement of AlphaStar project at DeepMind'
    }
]

# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================

handlungen = [
    # 1
    {
        'person_id': person_id,
        'handlung_typ': 'einstellung',
        'beschreibung': 'Joined Google DeepMind as research engineer, worked on AlphaStar project',
        'datum_handlung': '2017-01-01',
        'quell_link': 'https://grokipedia.com/page/igor-babuschkin',
        'quell_titel': 'Igor Babuschkin - Grokipedia',
        'kontext': 'Career move from physics research to AI at DeepMind'
    },
    # 2
    {
        'person_id': person_id,
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Led AlphaStar project at DeepMind, achieving grandmaster-level performance in StarCraft II, surpassing 99.8% of human players',
        'datum_handlung': '2019-10-30',
        'quell_link': 'https://deepmind.google/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/',
        'quell_titel': 'AlphaStar: Grandmaster level in StarCraft II - DeepMind',
        'kontext': 'Major breakthrough in multi-agent reinforcement learning and agentic AI systems'
    },
    # 3
    {
        'person_id': person_id,
        'handlung_typ': 'einstellung',
        'beschreibung': 'Joined OpenAI as senior R&D engineer, participated in core technologies behind ChatGPT including GPT-4',
        'datum_handlung': '2021-06-01',
        'quell_link': 'https://eu.36kr.com/en/p/3423457623362947',
        'quell_titel': 'Musk Loses Top Talent at xAI - 36kr',
        'kontext': 'Career transition from DeepMind to OpenAI during critical GPT development period'
    },
    # 4
    {
        'person_id': person_id,
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded xAI with Elon Musk and 11 other team members from OpenAI, DeepMind, Google, and Microsoft',
        'datum_handlung': '2023-07-12',
        'quell_link': 'https://en.wikipedia.org/wiki/XAI_(company)',
        'quell_titel': 'xAI (company) - Wikipedia',
        'kontext': 'Left OpenAI to co-found xAI with mission to "understand the true nature of the universe"'
    },
    # 5
    {
        'person_id': person_id,
        'handlung_typ': 'einstellung',
        'beschreibung': 'Served as Chief Engineer at xAI, leading engineering teams for scalable AI infrastructure',
        'datum_handlung': '2023-07-12',
        'quell_link': 'https://grokipedia.com/page/igor-babuschkin',
        'quell_titel': 'Igor Babuschkin - Grokipedia',
        'kontext': 'Technical leadership role at newly founded xAI'
    },
    # 6
    {
        'person_id': person_id,
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Helped develop and launch Grok chatbot at xAI in late 2023',
        'datum_handlung': '2023-11-04',
        'quell_link': 'https://en.wikipedia.org/wiki/Grok_(chatbot)',
        'quell_titel': 'Grok (chatbot) - Wikipedia',
        'kontext': 'First major product launch at xAI, competing with ChatGPT and other AI assistants'
    },
    # 7
    {
        'person_id': person_id,
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Oversaw construction of Memphis Colossus supercomputer with 100,000 Nvidia H100 GPUs in 122 days, transforming abandoned Electrolux factory',
        'datum_handlung': '2024-07-01',
        'quell_link': 'https://finance.yahoo.com/news/elon-musks-xai-co-founder-140107302.html',
        'quell_titel': 'Elon Musk\'s xAI Co-Founder Igor Babuschkin Resigns - Yahoo Finance',
        'kontext': 'Rapid deployment of world\'s largest fully connected H100 GPU cluster'
    },
    # 8
    {
        'person_id': person_id,
        'handlung_typ': 'umstrukturierung',
        'beschreibung': 'Expanded Memphis Colossus supercomputer from 100,000 to 200,000 Nvidia H100 GPUs in additional 92 days',
        'datum_handlung': '2024-10-01',
        'quell_link': 'https://www.rdworldonline.com/how-xai-turned-a-factory-shell-into-an-ai-colossus-to-power-grok-3-and-beyond/',
        'quell_titel': 'How xAI turned a factory shell into an AI Colossus',
        'kontext': 'Doubling of compute capacity for Grok model training'
    },
    # 9
    {
        'person_id': person_id,
        'handlung_typ': 'ruecktritt',
        'beschreibung': 'Resigned as co-founder and Chief Engineer from xAI after 2 years',
        'datum_handlung': '2025-08-13',
        'quell_link': 'https://www.cnbc.com/2025/08/13/elon-musks-xai-loses-co-founder-igor-babuschkin-for-venture-firm.html',
        'quell_titel': 'Elon Musk\'s xAI loses co-founder Igor Babuschkin - CNBC',
        'kontext': 'Departure to focus on AI safety, part of broader executive exodus from xAI'
    },
    # 10
    {
        'person_id': person_id,
        'handlung_typ': 'gruendung',
        'beschreibung': 'Founded Babuschkin Ventures, investment firm focused on AI safety research and agentic systems startups',
        'datum_handlung': '2025-08-13',
        'quell_link': 'https://www.technology.org/2025/08/14/xai-co-founder-igor-babuschkin-leaves-to-start-ai-safety-fund/',
        'quell_titel': 'xAI Co-Founder Igor Babuschkin Leaves to Start AI Safety Fund - Technology.org',
        'kontext': 'Pivoting from building frontier AI to investing in AI safety after conversation with Max Tegmark'
    },
    # 11
    {
        'person_id': person_id,
        'handlung_typ': 'investition',
        'beschreibung': 'Personally invested $50 million as first-closing capital for general partner of Babuschkin Ventures',
        'datum_handlung': '2025-08-13',
        'quell_link': 'https://eu.36kr.com/en/p/3433402509184643',
        'quell_titel': 'Musk "Bets On" the Man Behind Him with $200 Million - 36kr',
        'kontext': 'Personal capital commitment to launch AI safety venture fund'
    },
    # 12
    {
        'person_id': person_id,
        'handlung_typ': 'investition',
        'beschreibung': 'Secured $200 million investment commitment from Elon Musk as limited partner for Babuschkin Ventures',
        'datum_handlung': '2025-08-13',
        'quell_link': 'https://eu.36kr.com/en/p/3433402509184643',
        'quell_titel': 'Musk "Bets On" the Man Behind Him with $200 Million - 36kr',
        'kontext': 'Musk backing former co-founder\'s AI safety fund with significant capital'
    },
    # 13
    {
        'person_id': person_id,
        'handlung_typ': 'investition',
        'beschreibung': 'Secured commitments from Teacher Retirement System of Texas ($500 million) and Musk Family Office ($200 million additional) for Babuschkin Ventures, targeting $1 billion total fund size',
        'datum_handlung': '2025-08-13',
        'quell_link': 'https://eu.36kr.com/en/p/3433402509184643',
        'quell_titel': 'Musk "Bets On" the Man Behind Him with $200 Million - 36kr',
        'kontext': 'Major institutional backing for AI safety venture fund with 10+2 year term'
    },
    # 14
    {
        'person_id': person_id,
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Published open-source TensorFlow implementation of DeepMind WaveNet with production features on GitHub',
        'datum_handlung': '2016-09-01',
        'quell_link': 'https://github.com/ibab',
        'quell_titel': 'ibab (Igor Babuschkin) on GitHub',
        'kontext': 'Contributing to open source AI research community during early deep learning era'
    },
    # 15
    {
        'person_id': person_id,
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Conducted research at CERN LHCb experiment while studying physics at TU Dortmund',
        'datum_handlung': '2013-06-01',
        'quell_link': 'https://www.getprog.ai/profile/890531',
        'quell_titel': 'Igor Babuschkin - GetProg',
        'kontext': 'Early physics research before transitioning to AI/ML field'
    }
]

# ============================================================================
# INSERT INTO DATABASE
# ============================================================================

try:
    # Insert Aussagen
    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            aussage['person_id'],
            aussage['aussage_text'],
            aussage['aussage_kurz'],
            aussage['modus'],
            aussage['quell_link'],
            aussage['quell_titel'],
            aussage['datum_aussage'],
            aussage['sprache'],
            aussage['kontext']
        ))

    print(f"OK Inserted {len(aussagen)} statements (aussagen)")

    # Insert Handlungen
    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            handlung['person_id'],
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))

    print(f"OK Inserted {len(handlungen)} actions (handlungen)")

    # Commit changes
    conn.commit()
    print(f"\n=== SUCCESS ===")
    print(f"Total: {len(aussagen)} statements + {len(handlungen)} actions = {len(aussagen) + len(handlungen)} records inserted for Igor Babuschkin (person_id={person_id})")

except sqlite3.Error as e:
    print(f"X Database error: {e}")
    conn.rollback()

finally:
    conn.close()
