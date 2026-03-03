import sqlite3
from datetime import datetime
import sys
import io

# Set UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 90  # Karol Hausman

# AUSSAGEN
aussagen = [
    {
        'aussage_text': "What we're doing is not just a brain for any particular robot, it's a single generalist brain that can control any robot.",
        'aussage_kurz': "Single generalist brain for any robot",
        'modus': 'muendlich',
        'quell_link': 'https://www.maginative.com/article/physical-intelligence-unveils-p0-a-foundation-model-for-general-robot-control/',
        'quell_titel': 'Physical Intelligence Unveils π₀, A Foundation Model for General Robot Control',
        'datum_aussage': '2024-10-31',
        'sprache': 'en',
        'kontext': 'Statement about Physical Intelligence mission and π0 foundation model'
    },
    {
        'aussage_text': "If you look at the history of robotics, it's very, very clear to me… that we've always been bottlenecked on intelligence.",
        'aussage_kurz': "Robotics bottlenecked by intelligence, not hardware",
        'modus': 'muendlich',
        'quell_link': 'https://sequoiacap.com/podcast/training-general-robots-for-any-task-physical-intelligences-karol-hausman-and-tobi-springenberg/',
        'quell_titel': 'Training General Robots for Any Task - Sequoia Capital Podcast',
        'datum_aussage': '2026-01-06',
        'sprache': 'en',
        'kontext': 'Discussion about the fundamental bottleneck in robotics development'
    },
    {
        'aussage_text': "You build this loosely brain-inspired thing that has a very general purpose learning algorithm. You feed the data, and it somehow gets it and gets it way better than anything we've ever had before.",
        'aussage_kurz': "Foundation models surpass previous approaches dramatically",
        'modus': 'muendlich',
        'quell_link': 'https://sequoiacap.com/podcast/training-general-robots-for-any-task-physical-intelligences-karol-hausman-and-tobi-springenberg/',
        'quell_titel': 'Training General Robots for Any Task - Sequoia Capital Podcast',
        'datum_aussage': '2026-01-06',
        'sprache': 'en',
        'kontext': 'Expressing wonder at foundation model capabilities applying to robots, vision, language, and sound'
    },
    {
        'aussage_text': "It's just like the whole thing works, it's kind of mind-blowing.",
        'aussage_kurz': "Foundation models for robotics are mind-blowing",
        'modus': 'muendlich',
        'quell_link': 'https://eutechfuture.com/artificial-intelligence/physical-intelligence-building-foundation-models-for-robots-to-interact-with-the-real-world/',
        'quell_titel': 'Physical Intelligence: Building Foundation Models for Robots',
        'datum_aussage': '2024-11-04',
        'sprache': 'en',
        'kontext': 'Expressing excitement about foundation models unlocking general-purpose robotics'
    },
    {
        'aussage_text': "There is no data of robots actually operating in the real world.",
        'aussage_kurz': "Lack of real-world robot operation data",
        'modus': 'muendlich',
        'quell_link': 'https://sequoiacap.com/podcast/training-general-robots-for-any-task-physical-intelligences-karol-hausman-and-tobi-springenberg/',
        'quell_titel': 'Training General Robots for Any Task - Sequoia Capital Podcast',
        'datum_aussage': '2026-01-06',
        'sprache': 'en',
        'kontext': 'Discussing challenges in robotics data collection compared to internet data for LLMs'
    },
    {
        'aussage_text': "They have these childhood periods, the adolescence period, where they're not very smart to begin with, but they have to learn from their own experience. And it doesn't come pre-baked. You kind of have to earn it on your own.",
        'aussage_kurz': "Intelligence requires learning from experience, not pre-programming",
        'modus': 'muendlich',
        'quell_link': 'https://sequoiacap.com/podcast/training-general-robots-for-any-task-physical-intelligences-karol-hausman-and-tobi-springenberg/',
        'quell_titel': 'Training General Robots for Any Task - Sequoia Capital Podcast',
        'datum_aussage': '2026-01-06',
        'sprache': 'en',
        'kontext': 'Drawing analogy from biological learning in intelligent species like humans and crows to robot learning'
    },
    {
        'aussage_text': "Some tasks requiring a ton of generalization, like deploying in homes with privacy or safety concerns, may not be the best places to deploy just yet, but the aperture is growing as models improve.",
        'aussage_kurz': "Cautious about home deployment due to privacy/safety",
        'modus': 'muendlich',
        'quell_link': 'https://sequoiacap.com/podcast/training-general-robots-for-any-task-physical-intelligences-karol-hausman-and-tobi-springenberg/',
        'quell_titel': 'Training General Robots for Any Task - Sequoia Capital Podcast',
        'datum_aussage': '2026-01-06',
        'sprache': 'en',
        'kontext': 'Discussing deployment considerations and safety concerns for general-purpose robots'
    },
    {
        'aussage_text': "Foundation models 🤝 robots at scale. We show how to use VLMs and LLMs to orchestrate a fleet of robots and allow 1:5 human:robot ratio.",
        'aussage_kurz': "Foundation models enable 1:5 human-to-robot supervision ratio",
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/hausman_k/status/1742935894120968353',
        'quell_titel': 'Karol Hausman on X about AutoRT',
        'datum_aussage': '2024-01-04',
        'sprache': 'en',
        'kontext': 'Announcing AutoRT research showing large-scale robot orchestration using foundation models'
    },
    {
        'aussage_text': "Fun fact: you can now literally write Asimov's laws into the [robot constitution].",
        'aussage_kurz': "Can implement Asimov-like laws in robot systems",
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/hausman_k/status/1742935894120968353',
        'quell_titel': 'Karol Hausman on X about AutoRT',
        'datum_aussage': '2024-01-04',
        'sprache': 'en',
        'kontext': 'Discussing AutoRT Robot Constitution feature allowing operational guideposts for safety'
    },
    {
        'aussage_text': "This is to 2024 being the year of robotics.",
        'aussage_kurz': "2024 as the year of robotics",
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/hausman_k/status/1740405696074850667',
        'quell_titel': 'Karol Hausman on X',
        'datum_aussage': '2023-12-28',
        'sprache': 'en',
        'kontext': 'Celebrating remarkable progress in robotics research over 2024'
    },
    {
        'aussage_text': "There are many reasons [for using laundry folding]: everyone understands if it's done well, it's easy to reset, it can be arbitrarily long, and it's easy to generate diverse data.",
        'aussage_kurz': "Laundry folding ideal benchmark for robot evaluation",
        'modus': 'muendlich',
        'quell_link': 'https://www.infoq.com/news/2024/12/pi-zero-robot/',
        'quell_titel': 'Physical Intelligence Unveils Robotics Foundation Model Pi-Zero',
        'datum_aussage': '2024-10-31',
        'sprache': 'en',
        'kontext': 'Explaining choice of laundry folding as evaluation task for π0 model'
    },
    {
        'aussage_text': "By leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in robotic control scenarios.",
        'aussage_kurz': "LLMs can use feedback for embodied reasoning",
        'modus': 'schriftlich',
        'quell_link': 'https://arxiv.org/abs/2207.05608',
        'quell_titel': 'Inner Monologue: Embodied Reasoning through Planning with Language Models',
        'datum_aussage': '2022-07-12',
        'sprache': 'en',
        'kontext': 'Core concept from Inner Monologue paper on using language models for robot planning'
    },
    {
        'aussage_text': "Closed-loop language feedback significantly improves high-level instruction completion on three domains, including simulated and real tabletop rearrangement tasks and long-horizon mobile manipulation tasks.",
        'aussage_kurz': "Language feedback improves robot task completion",
        'modus': 'schriftlich',
        'quell_link': 'https://arxiv.org/abs/2207.05608',
        'quell_titel': 'Inner Monologue: Embodied Reasoning through Planning with Language Models',
        'datum_aussage': '2022-07-12',
        'sprache': 'en',
        'kontext': 'Research findings from Inner Monologue paper'
    },
    {
        'aussage_text': "RT-2 shows improved generalization capabilities and semantic and visual understanding beyond the robotic data it was exposed to, including interpreting new commands and responding to user commands by performing rudimentary reasoning.",
        'aussage_kurz': "RT-2 generalizes beyond training data",
        'modus': 'schriftlich',
        'quell_link': 'https://robotics-transformer2.github.io/',
        'quell_titel': 'RT-2: Vision-Language-Action Models',
        'datum_aussage': '2023-07-28',
        'sprache': 'en',
        'kontext': 'Describing capabilities of RT-2 vision-language-action model'
    },
    {
        'aussage_text': "Task generalization becomes feasible when representing tasks through rough trajectory sketches.",
        'aussage_kurz': "Trajectory sketches enable task generalization",
        'modus': 'schriftlich',
        'quell_link': 'https://rt-trajectory.github.io/',
        'quell_titel': 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches',
        'datum_aussage': '2024-01-16',
        'sprache': 'en',
        'kontext': 'Key insight from RT-Trajectory ICLR 2024 paper'
    },
    {
        'aussage_text': "AutoRT leverages vision-language models (VLMs) for scene understanding and grounding, and further uses large language models (LLMs) for proposing diverse and novel instructions to be performed by a fleet of robots.",
        'aussage_kurz': "AutoRT uses VLMs and LLMs for robot orchestration",
        'modus': 'schriftlich',
        'quell_link': 'https://arxiv.org/abs/2401.12963',
        'quell_titel': 'AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents',
        'datum_aussage': '2024-01-23',
        'sprache': 'en',
        'kontext': 'Description of AutoRT system architecture'
    },
    {
        'aussage_text': "π0 is a general-purpose robot foundation model trained on broad and diverse data that can follow various text instructions, spanning images, text, and actions, and acquires physical intelligence by training on embodied experience from robots.",
        'aussage_kurz': "π0 learns physical intelligence from embodied experience",
        'modus': 'schriftlich',
        'quell_link': 'https://arxiv.org/abs/2410.24164',
        'quell_titel': 'π₀: A Vision-Language-Action Flow Model for General Robot Control',
        'datum_aussage': '2024-10-31',
        'sprache': 'en',
        'kontext': 'Description of Physical Intelligence π0 foundation model'
    },
    {
        'aussage_text': "The data collected by AutoRT is significantly more diverse, and AutoRT's use of LLMs allows for instruction following data collection robots that are aligned with human preferences.",
        'aussage_kurz': "AutoRT enables diverse, human-aligned data collection",
        'modus': 'schriftlich',
        'quell_link': 'https://arxiv.org/abs/2401.12963',
        'quell_titel': 'AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents',
        'datum_aussage': '2024-01-23',
        'sprache': 'en',
        'kontext': 'Benefits of AutoRT for robotic data collection'
    },
    {
        'aussage_text': "Our demo video was not scripted or teleoperated.",
        'aussage_kurz': "π0 demos are autonomous, not teleoperated",
        'modus': 'muendlich',
        'quell_link': 'https://www.infoq.com/news/2024/12/pi-zero-robot/',
        'quell_titel': 'Physical Intelligence Unveils Robotics Foundation Model Pi-Zero',
        'datum_aussage': '2024-10-31',
        'sprache': 'en',
        'kontext': 'Confirming authenticity of π0 demonstration videos'
    }
]

# HANDLUNGEN
handlungen = [
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded Physical Intelligence with Sergey Levine, Chelsea Finn, Brian Ichter, Adnan Esmail, and Lachy Groom to build foundation models for general-purpose robotics',
        'datum_handlung': '2024-01-01',
        'quell_link': 'https://eutechfuture.com/artificial-intelligence/physical-intelligence-building-foundation-models-for-robots-to-interact-with-the-real-world/',
        'quell_titel': 'Physical Intelligence: Building Foundation Models for Robots',
        'kontext': 'Founded by former Google DeepMind researchers and Stanford/Berkeley academics'
    },
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': 'Left position as Staff Research Scientist at Google DeepMind to co-found Physical Intelligence',
        'datum_handlung': '2024-01-01',
        'quell_link': 'https://yalibnan.com/2024/03/13/google-scientists-leave-to-build-robot-brain/',
        'quell_titel': 'Google scientists leave to build robot brain',
        'kontext': 'Departure from Google DeepMind where he led robot manipulation research'
    },
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': 'Left adjunct professorship at Stanford University where he co-taught CS 224R on deep reinforcement learning',
        'datum_handlung': '2024-01-01',
        'quell_link': 'https://karolhausman.github.io/',
        'quell_titel': 'Karol Hausman Personal Website',
        'kontext': 'Left Stanford teaching position to focus on Physical Intelligence full-time'
    },
    {
        'handlung_typ': 'spende',
        'beschreibung': 'Physical Intelligence raised $70M seed funding from Thrive Capital (lead), Khosla Ventures, Lux Capital, OpenAI, and Sequoia Capital',
        'datum_handlung': '2024-03-01',
        'quell_link': 'https://www.maginative.com/article/physical-intelligence-raises-70m-to-build-ai-powered-robots-for-any-application/',
        'quell_titel': 'Physical Intelligence Raises $70M to Build AI-Powered Robots',
        'kontext': 'Initial seed funding for Physical Intelligence startup'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Published AutoRT paper demonstrating large-scale robot fleet orchestration with 1:5 human-to-robot supervision ratio across 50+ robots collecting 77k episodes',
        'datum_handlung': '2024-01-23',
        'quell_link': 'https://arxiv.org/abs/2401.12963',
        'quell_titel': 'AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents',
        'kontext': 'Research published while at Google DeepMind showing foundation models enabling scaled robot deployment'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Published RT-Trajectory paper at ICLR 2024 introducing hindsight trajectory sketches for robotic task generalization',
        'datum_handlung': '2024-01-16',
        'quell_link': 'https://rt-trajectory.github.io/',
        'quell_titel': 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches',
        'kontext': 'Spotlight paper at ICLR 2024 on novel conditioning method for robot policies'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Launched π0 (pi-zero), Physical Intelligence first generalist robot foundation model capable of controlling any robot for diverse tasks including laundry folding',
        'datum_handlung': '2024-10-31',
        'quell_link': 'https://physicalintelligence.company/blog/pi0',
        'quell_titel': 'Our First Generalist Policy - Physical Intelligence',
        'kontext': 'First major product release from Physical Intelligence, trained on 7 robots across 68 tasks'
    },
    {
        'handlung_typ': 'spende',
        'beschreibung': 'Physical Intelligence raised $400M Series A at $2.4B valuation from Jeff Bezos, OpenAI, Thrive Capital, Lux Capital, Bond Capital, Khosla Ventures, and Sequoia Capital',
        'datum_handlung': '2024-11-04',
        'quell_link': 'https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html',
        'quell_titel': 'Jeff Bezos and OpenAI invest in robot startup Physical Intelligence at $2.4 billion valuation',
        'kontext': 'Major Series A funding round shortly after π0 launch'
    },
    {
        'handlung_typ': 'spende',
        'beschreibung': 'Physical Intelligence raised $600M Series B at $5.6B valuation led by CapitalG (Alphabet growth fund) with Lux Capital, Bond, Redpoint, Sequoia, T. Rowe Price, and NVIDIA',
        'datum_handlung': '2025-11-20',
        'quell_link': 'https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding',
        'quell_titel': 'Robotics Startup Physical Intelligence Valued at $5.6 Billion in New Funding',
        'kontext': 'Series B round bringing total funding to $1.1B, valuation more than doubled from Series A'
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Became CEO of Physical Intelligence, leading company mission to bring general-purpose AI into the physical world',
        'datum_handlung': '2024-01-01',
        'quell_link': 'https://www.linkedin.com/in/karolhausman/',
        'quell_titel': 'Karol Hausman LinkedIn Profile',
        'kontext': 'Took CEO role at Physical Intelligence founding'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Co-authored RT-2 (Robotic Transformer 2) at Google DeepMind, first vision-language-action model translating vision and language into robotic actions',
        'datum_handlung': '2023-07-28',
        'quell_link': 'https://robotics-transformer2.github.io/',
        'quell_titel': 'RT-2: Vision-Language-Action Models',
        'kontext': 'Groundbreaking VLA model described by NYT as "a quiet revolution" in robotics'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Co-authored SayCan paper "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances" combining LLMs with robot affordances',
        'datum_handlung': '2022-04-04',
        'quell_link': 'https://arxiv.org/abs/2204.01691',
        'quell_titel': 'Do As I Can, Not As I Say: Grounding Language in Robotic Affordances',
        'kontext': 'CoRL 2022 paper on grounding language models in real-world robot capabilities'
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Co-authored Inner Monologue paper on embodied reasoning through planning with language models for robotic control',
        'datum_handlung': '2022-07-12',
        'quell_link': 'https://arxiv.org/abs/2207.05608',
        'quell_titel': 'Inner Monologue: Embodied Reasoning through Planning with Language Models',
        'kontext': 'CoRL 2022 paper showing LLMs can reason over feedback for robot planning'
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Appointed adjunct professor at Stanford University, co-teaching CS 224R Deep Reinforcement Learning with Chelsea Finn',
        'datum_handlung': '2023-01-01',
        'quell_link': 'https://cs224r.stanford.edu/',
        'quell_titel': 'CS 224R Deep Reinforcement Learning - Stanford',
        'kontext': 'Teaching role at Stanford while working at Google DeepMind'
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Completed PhD in Computer Science at USC focused on interactive perception, reinforcement learning, and probabilistic state estimation for robotics',
        'datum_handlung': '2018-05-01',
        'quell_link': 'https://robotics.usc.edu/resl/people/57/',
        'quell_titel': 'Karol Hausman - USC Robotic Embedded Systems Laboratory',
        'kontext': 'Doctoral research under Prof. Gaurav Sukhatme at USC RESL, collaborating with Stefan Schaal group'
    }
]

# Aussagen einfügen
print("Füge Aussagen ein...")
for i, aussage in enumerate(aussagen, 1):
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        aussage['aussage_text'],
        aussage['aussage_kurz'],
        aussage['modus'],
        aussage['quell_link'],
        aussage['quell_titel'],
        aussage['datum_aussage'],
        aussage['sprache'],
        aussage['kontext']
    ))
    print(f"  {i}. {aussage['aussage_kurz']}")

# Handlungen einfügen
print("\nFüge Handlungen ein...")
for i, handlung in enumerate(handlungen, 1):
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        person_id,
        handlung['handlung_typ'],
        handlung['beschreibung'],
        handlung['datum_handlung'],
        handlung['quell_link'],
        handlung['quell_titel'],
        handlung['kontext']
    ))
    print(f"  {i}. [{handlung['handlung_typ']}] {handlung['beschreibung'][:80]}...")

# Commit und schließen
conn.commit()
conn.close()

print(f"\n{'='*80}")
print(f"ABGESCHLOSSEN")
print(f"{'='*80}")
print(f"Person ID: {person_id} (Karol Hausman)")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Datensätze")
print(f"{'='*80}")
