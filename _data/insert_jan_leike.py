#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data insertion script for Jan Leike (person_id=73)
Research on worldviews of AI/Silicon Valley personalities
"""

import sqlite3
from datetime import datetime

DB_PATH = r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db'
PERSON_ID = 73

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Counter
aussagen_count = 0
handlungen_count = 0

print(f"Starting data insertion for Jan Leike (person_id={PERSON_ID})")
print("="*80)

# ============================================================================
# AUSSAGEN (STATEMENTS)
# ============================================================================

aussagen = [
    # Statement 1 - OpenAI Safety Culture Criticism
    {
        'aussage_text': 'Over the past years, safety culture and processes have taken a backseat to shiny products',
        'aussage_kurz': 'Safety culture took backseat to products at OpenAI',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/janleike/status/1791498174659715494',
        'quell_titel': 'Jan Leike on X: Yesterday was my last day at OpenAI',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Twitter/X thread announcing resignation from OpenAI as head of alignment and Superalignment lead, criticizing company priorities'
    },

    # Statement 2 - Trust in Leadership Lost
    {
        'aussage_text': 'I have been disagreeing with OpenAI leadership about the company\'s core priorities for quite some time, until we finally reached a breaking point',
        'aussage_kurz': 'Disagreement with OpenAI leadership on core priorities',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/janleike/status/1791498178346549382',
        'quell_titel': 'Jan Leike on X: I joined because I thought OpenAI would be the best place',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Resignation announcement explaining reasons for leaving OpenAI'
    },

    # Statement 3 - Resource Struggles
    {
        'aussage_text': 'Sometimes we were struggling for compute and it was getting harder and harder to get this crucial research done',
        'aussage_kurz': 'Superalignment team struggled for compute resources',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/janleike/status/1791498174659715494',
        'quell_titel': 'Jan Leike resignation statement on X',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Describing resource constraints faced by Superalignment team despite 20% compute commitment'
    },

    # Statement 4 - AGI Preparation Priority
    {
        'aussage_text': 'We are long overdue in getting incredibly serious about the implications of AGI. We must prioritize preparing for them as best as we can',
        'aussage_kurz': 'Must get serious about AGI implications',
        'modus': 'schriftlich',
        'quell_link': 'https://venturebeat.com/ai/openais-former-superalignment-leader-blasts-company-safety-culture-and-processes-have-taken-a-backseat',
        'quell_titel': 'OpenAI\'s former superalignment leader blasts company - VentureBeat',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Part of resignation statement emphasizing urgency of AGI safety preparation'
    },

    # Statement 5 - Bandwidth Allocation
    {
        'aussage_text': 'I believe much more of our bandwidth should be spent getting ready for the next generations of models, on security, monitoring, preparedness, safety, adversarial robustness, (super)alignment, confidentiality, societal impact, and related topics',
        'aussage_kurz': 'More bandwidth needed for safety and preparedness',
        'modus': 'schriftlich',
        'quell_link': 'https://www.ccn.com/news/technology/jan-leike-resignation-damning-of-openai-core-safety-priorities/',
        'quell_titel': 'Jan Leike\'s Resignation Damning of OpenAI\'s Core Priorities - CCN.com',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Resignation statement outlining priorities OpenAI should focus on'
    },

    # Statement 6 - Alignment Tractability
    {
        'aussage_text': 'I think alignment is tractable. I think we can actually make a lot of progress if we focus on it and we put an effort into it',
        'aussage_kurz': 'Alignment is tractable with focused effort',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Interview discussing Superalignment project and optimism about solving alignment'
    },

    # Statement 7 - Angle of Attack
    {
        'aussage_text': 'It really feels like we have a real angle of attack on the problem that we can actually iterate on, we can actually build towards. And I think it\'s pretty likely going to work, actually',
        'aussage_kurz': 'We have a real angle of attack on alignment',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Expressing optimism about technical approach to alignment problem during Superalignment announcement period'
    },

    # Statement 8 - Human Supervision Limitation
    {
        'aussage_text': 'Future superhuman models will behave in complex ways too difficult for humans to reliably evaluate; humans will only be able to weakly supervise superhuman models',
        'aussage_kurz': 'Humans can only weakly supervise superhuman AI',
        'modus': 'schriftlich',
        'quell_link': 'https://openai.com/index/weak-to-strong-generalization/',
        'quell_titel': 'Weak-to-strong generalization - OpenAI',
        'datum_aussage': '2023-12',
        'sprache': 'en',
        'kontext': 'Research publication introducing weak-to-strong generalization paradigm for superhuman AI alignment'
    },

    # Statement 9 - RLHF Current Method
    {
        'aussage_text': 'Reinforcement learning from human feedback is kind of the popular method today. It works well because humans can look at what the system is doing and tell whether it\'s good or not',
        'aussage_kurz': 'RLHF works by human evaluation of system behavior',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Explaining current alignment methodology and its limitations for future systems'
    },

    # Statement 10 - Anthropic Mission Continuation
    {
        'aussage_text': 'I\'m excited to join @AnthropicAI to continue the superalignment mission! My new team will work on scalable oversight, weak-to-strong generalization, and automated alignment research',
        'aussage_kurz': 'Joining Anthropic to continue superalignment work',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/janleike/status/1795497960509448617',
        'quell_titel': 'Jan Leike on X: I\'m excited to join @AnthropicAI',
        'datum_aussage': '2024-05-28',
        'sprache': 'en',
        'kontext': 'Announcement of joining Anthropic with research agenda'
    },

    # Statement 11 - AGI Timeline Uncertainty
    {
        'aussage_text': 'I have a lot of uncertainty about how the future will go, and nobody really knows when AGI will arrive specifically',
        'aussage_kurz': 'High uncertainty about AGI timeline',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Discussing uncertainty around AGI development timeline in podcast interview'
    },

    # Statement 12 - Alignment Next Generation
    {
        'aussage_text': 'Maybe this problem isn\'t even solvable by humans who live today. But there\'s this easier problem, which is how do you align the system that is the next generation? How do you align GPT-N+1? And that is a substantially easier problem',
        'aussage_kurz': 'Focus on aligning next generation, not final superintelligence',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Explaining iterative approach to alignment - solve for next model generation rather than final superintelligence'
    },

    # Statement 13 - DeepMind Portfolio Approach
    {
        'aussage_text': 'DeepMind\'s approach to safety is like a portfolio because they don\'t know what will end up working, so they pursue different approaches in parallel',
        'aussage_kurz': 'Portfolio approach to AI safety at DeepMind',
        'modus': 'muendlich',
        'quell_link': 'https://futureoflife.org/podcast/ai-alignment-podcast-on-deepmind-ai-safety-and-recursive-reward-modeling-with-jan-leike/',
        'quell_titel': 'AI Alignment Podcast: On DeepMind, AI Safety, and Recursive Reward Modeling - Future of Life Institute',
        'datum_aussage': '2022-08',
        'sprache': 'en',
        'kontext': 'Describing DeepMind\'s multi-track approach to AI safety research during his time there'
    },

    # Statement 14 - Automated Alignment Researcher Goal
    {
        'aussage_text': 'Our goal is to build the first automated alignment researcher with human-level capabilities',
        'aussage_kurz': 'Goal: Build human-level automated alignment researcher',
        'modus': 'schriftlich',
        'quell_link': 'https://openai.com/index/introducing-superalignment/',
        'quell_titel': 'Introducing Superalignment - OpenAI',
        'datum_aussage': '2023-07-05',
        'sprache': 'en',
        'kontext': 'Superalignment project announcement describing core objective'
    },

    # Statement 15 - Weak-to-Strong Results
    {
        'aussage_text': 'We showed that we can use a GPT-2-level model to elicit most of GPT-4\'s capabilities—close to GPT-3.5-level performance—generalizing correctly even to hard problems where the small model failed',
        'aussage_kurz': 'Weak models can elicit strong model capabilities',
        'modus': 'schriftlich',
        'quell_link': 'https://openai.com/index/weak-to-strong-generalization/',
        'quell_titel': 'Weak-to-strong generalization - OpenAI',
        'datum_aussage': '2023-12',
        'sprache': 'en',
        'kontext': 'Research results on weak-to-strong generalization showing surprising capability elicitation'
    },

    # Statement 16 - Scalable Oversight Definition
    {
        'aussage_text': 'Scalable oversight is generally a portfolio of ideas and techniques that allow leveraging AI to assist human evaluation on difficult tasks',
        'aussage_kurz': 'Scalable oversight: AI-assisted human evaluation',
        'modus': 'muendlich',
        'quell_link': 'https://axrp.net/episode/2023/07/27/episode-24-superalignment-jan-leike.html',
        'quell_titel': 'AXRP Episode 24 - Superalignment with Jan Leike',
        'datum_aussage': '2023-07',
        'sprache': 'en',
        'kontext': 'Technical podcast explaining key concepts in superalignment research agenda'
    },

    # Statement 17 - Best Place for Research
    {
        'aussage_text': 'I joined because I thought OpenAI would be the best place in the world to do this research',
        'aussage_kurz': 'OpenAI initially seemed best place for alignment research',
        'modus': 'schriftlich',
        'quell_link': 'https://x.com/janleike/status/1791498178346549382',
        'quell_titel': 'Jan Leike on X: I joined because I thought OpenAI would be the best place',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Resignation statement reflecting on initial motivations for joining OpenAI'
    },

    # Statement 18 - Sailing Against the Wind
    {
        'aussage_text': 'Over the past few months my team had been sailing against the wind',
        'aussage_kurz': 'Team faced headwinds at OpenAI',
        'modus': 'schriftlich',
        'quell_link': 'https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html',
        'quell_titel': 'OpenAI dissolves Superalignment AI safety team - CNBC',
        'datum_aussage': '2024-05-17',
        'sprache': 'en',
        'kontext': 'Describing organizational resistance and difficulties faced by Superalignment team'
    },

    # Statement 19 - Four Year Timeline
    {
        'aussage_text': 'Systems could get a lot smarter or more capable over the next few years, and OpenAI would love to have solved the alignment problem in advance of actually having to solve it, ideally far in advance',
        'aussage_kurz': 'Need to solve alignment before systems become much smarter',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Explaining rationale for four-year Superalignment timeline relative to expected capability increases'
    },

    # Statement 20 - Research Progress Dedication
    {
        'aussage_text': 'I think there\'s a lot of research progress to be made that we can actually make with a small dedicated team over the course of a year, or four',
        'aussage_kurz': 'Small dedicated teams can make significant progress',
        'modus': 'muendlich',
        'quell_link': 'https://80000hours.org/podcast/episodes/jan-leike-superalignment/',
        'quell_titel': 'Jan Leike on OpenAI\'s massive push to make superintelligence safe - 80,000 Hours Podcast',
        'datum_aussage': '2023-08',
        'sprache': 'en',
        'kontext': 'Optimistic view on what focused research teams can accomplish in alignment'
    }
]

# Insert statements
for aussage in aussagen:
    cursor.execute('''
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quell_link,
            quell_titel, datum_aussage, sprache, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
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
    aussagen_count += 1
    print(f"[OK] Statement {aussagen_count}: {aussage['aussage_kurz']}")

print(f"\n{aussagen_count} statements inserted successfully!")
print("="*80)

# ============================================================================
# HANDLUNGEN (ACTIONS)
# ============================================================================

handlungen = [
    # Action 1 - PhD Completion
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Completed PhD in reinforcement learning theory at Australian National University under supervision of Marcus Hutter. Thesis: "Nonparametric General Reinforcement Learning"',
        'datum_handlung': '2016-01-01',
        'quell_link': 'https://jan.leike.name/',
        'quell_titel': 'Jan Leike - Personal Website',
        'kontext': 'Academic foundation in theoretical reinforcement learning before transitioning to empirical AI safety'
    },

    # Action 2 - FHI Postdoc
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Six-month postdoctoral fellowship at Future of Humanity Institute, Oxford, focusing on theoretical alignment research',
        'datum_handlung': '2016-06-01',
        'quell_link': 'https://www.fhi.ox.ac.uk/team/jan-leike/',
        'quell_titel': 'Jan Leike - Future of Humanity Institute',
        'kontext': 'Brief transition period at FHI before deciding to pursue empirical AI safety research at DeepMind'
    },

    # Action 3 - Joining DeepMind
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Joined DeepMind as alignment researcher to focus on empirical AI safety research, prototyped reinforcement learning from human feedback (RLHF)',
        'datum_handlung': '2017-01-01',
        'quell_link': 'https://en.wikipedia.org/wiki/Jan_Leike',
        'quell_titel': 'Jan Leike - Wikipedia',
        'kontext': 'Career pivot from theoretical to empirical work; developed foundational RLHF techniques that would later underpin major language models'
    },

    # Action 4 - Deep RL from Human Preferences Paper
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Co-authored seminal paper "Deep Reinforcement Learning from Human Preferences" with Paul Christiano, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei at NIPS 2017',
        'datum_handlung': '2017-06-01',
        'quell_link': 'https://arxiv.org/abs/1706.03741',
        'quell_titel': 'Deep reinforcement learning from human preferences - arXiv',
        'kontext': 'Foundational paper establishing RLHF methodology, showing human preferences could effectively train RL agents without reward function access'
    },

    # Action 5 - Recursive Reward Modeling Paper
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Published "Scalable agent alignment via reward modeling: a research direction" with co-authors David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane Legg, introducing recursive reward modeling',
        'datum_handlung': '2018-11-01',
        'quell_link': 'https://arxiv.org/abs/1811.07871',
        'quell_titel': 'Scalable agent alignment via reward modeling - arXiv',
        'kontext': 'Key theoretical contribution to alignment proposing recursive approach to reward modeling for more capable agents'
    },

    # Action 6 - Joining OpenAI
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Joined OpenAI as alignment researcher, later became Head of Alignment',
        'datum_handlung': '2021-01-01',
        'quell_link': 'https://en.wikipedia.org/wiki/Jan_Leike',
        'quell_titel': 'Jan Leike - Wikipedia',
        'kontext': 'Move from DeepMind to OpenAI to continue alignment research with more capable models'
    },

    # Action 7 - InstructGPT Development
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Co-authored "Training language models to follow instructions with human feedback" (InstructGPT paper), developing first RLHF language model at NIPS 2022',
        'datum_handlung': '2022-03-01',
        'quell_link': 'https://arxiv.org/abs/2203.02155',
        'quell_titel': 'Training language models to follow instructions with human feedback - arXiv',
        'kontext': 'Applied RLHF to language models at scale, laying groundwork for ChatGPT. Led data collection and training process'
    },

    # Action 8 - ChatGPT Alignment Work
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Led alignment efforts for ChatGPT including RLHF training and red-teaming, using similar approach as InstructGPT',
        'datum_handlung': '2022-11-01',
        'quell_link': 'https://www.technologyreview.com/2023/03/03/1069311/inside-story-oral-history-how-chatgpt-built-openai/',
        'quell_titel': 'The inside story of how ChatGPT was built - MIT Technology Review',
        'kontext': 'Key role in safety and alignment work for ChatGPT launch, coordinating human feedback and adversarial testing'
    },

    # Action 9 - Superalignment Team Co-founding
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded and co-led Superalignment team with Ilya Sutskever, with 20% of OpenAI compute allocated. Goal: solve core technical challenges of superintelligence alignment in 4 years',
        'datum_handlung': '2023-07-05',
        'quell_link': 'https://openai.com/index/introducing-superalignment/',
        'quell_titel': 'Introducing Superalignment - OpenAI',
        'kontext': 'Major organizational initiative at OpenAI to develop automated alignment researcher and prepare for superintelligent systems'
    },

    # Action 10 - TIME 100 AI 2023
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Named to TIME 100 Most Influential People in AI 2023 list for co-leading OpenAI Superalignment team',
        'datum_handlung': '2023-09-01',
        'quell_link': 'https://time.com/collection/time100-ai/6310616/jan-leike/',
        'quell_titel': 'Jan Leike: The 100 Most Influential People in AI 2023 - TIME',
        'kontext': 'Recognition for leadership in AI safety and alignment research community'
    },

    # Action 11 - Weak-to-Strong Paper
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Published weak-to-strong generalization research showing GPT-2-level models can elicit most GPT-4 capabilities, addressing superhuman AI supervision challenge',
        'datum_handlung': '2023-12-01',
        'quell_link': 'https://openai.com/index/weak-to-strong-generalization/',
        'quell_titel': 'Weak-to-strong generalization - OpenAI',
        'kontext': 'Novel approach to alignment problem: how weaker supervisors can align stronger models, key for superhuman AI'
    },

    # Action 12 - Resignation from OpenAI
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': 'Resigned as Head of Alignment, Superalignment lead, and executive at OpenAI citing disagreement with leadership priorities and insufficient safety focus',
        'datum_handlung': '2024-05-17',
        'quell_link': 'https://x.com/janleike/status/1791498174659715494',
        'quell_titel': 'Jan Leike on X: Yesterday was my last day at OpenAI',
        'kontext': 'High-profile departure following Ilya Sutskever exit; criticized safety culture and compute resource allocation. OpenAI subsequently dissolved Superalignment team'
    },

    # Action 13 - Joining Anthropic
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Joined Anthropic to lead new superalignment team working on scalable oversight, weak-to-strong generalization, and automated alignment research. Reports to Jared Kaplan (Chief Science Officer)',
        'datum_handlung': '2024-05-28',
        'quell_link': 'https://techcrunch.com/2024/05/28/anthropic-hires-former-openai-safety-lead-to-head-up-new-team/',
        'quell_titel': 'Anthropic hires former OpenAI safety lead to head up new team - TechCrunch',
        'kontext': 'Continued superalignment mission at rival AI safety-focused company founded by former OpenAI researchers Dario and Daniela Amodei'
    },

    # Action 14 - TIME 100 AI 2024
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Named to TIME 100 Most Influential People in AI 2024 list for second consecutive year, recognized for dramatic exit from OpenAI and continued alignment work at Anthropic',
        'datum_handlung': '2024-09-01',
        'quell_link': 'https://time.com/collections/time100-ai-2024/7012867/jan-leike/',
        'quell_titel': 'Jan Leike: The 100 Most Influential People in AI 2024 - TIME',
        'kontext': 'Continued recognition as influential voice in AI safety despite organizational transition'
    }
]

# Insert actions
for handlung in handlungen:
    cursor.execute('''
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        PERSON_ID,
        handlung['handlung_typ'],
        handlung['beschreibung'],
        handlung['datum_handlung'],
        handlung['quell_link'],
        handlung['quell_titel'],
        handlung['kontext']
    ))
    handlungen_count += 1
    print(f"[OK] Action {handlungen_count}: {handlung['beschreibung'][:80]}...")

print(f"\n{handlungen_count} actions inserted successfully!")
print("="*80)

# Commit and close
conn.commit()
conn.close()

print(f"\n{'='*80}")
print(f"DATA INSERTION COMPLETED SUCCESSFULLY")
print(f"{'='*80}")
print(f"Total Statements (Aussagen): {aussagen_count}")
print(f"Total Actions (Handlungen):  {handlungen_count}")
print(f"Total Records:               {aussagen_count + handlungen_count}")
print(f"Person ID:                   {PERSON_ID} (Jan Leike)")
print(f"Database:                    {DB_PATH}")
print(f"{'='*80}")
