#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Navrina Singh (person_id=86) - Datenbank-Insert Script
Credo AI Founder/CEO, AI Ethics/Governance Expert
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 86

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN - Statements und Zitate von Navrina Singh
    aussagen = [
        # 1. Mission und Vision von Credo AI
        {
            'aussage_text': 'From day one of Credo AI, we\'ve just been very relentlessly focused on our mission, which is how do we become the standard of good AI and defining what that good looks like so that this technology works in service of humanity. So whether it is generative AI or our groundbreaking work in making sure the AI agents and agentic AI future is also governed, we just continue to stay very heads down focused on making sure that we become the infrastructure of trust.',
            'aussage_kurz': 'Credo AI as standard of good AI serving humanity',
            'modus': 'muendlich',
            'quell_link': 'https://www.credo.ai/blog/from-pioneering-partnerships-to-groundbreaking-products-accelerating-enterprise-ai-innovation-with-governance-into-2025',
            'quell_titel': 'From Pioneering Partnerships to Groundbreaking Products - Credo AI Blog',
            'datum_aussage': '2024-12-01',
            'sprache': 'en',
            'kontext': 'Reflection on Credo AI\'s mission and approach to AI governance, including generative AI and agentic AI systems'
        },
        # 2. AI Governance als Wettbewerbsvorteil 2025
        {
            'aussage_text': 'AI governance—encompassing reliability, alignment, safety, compliance, robustness, fairness, and privacy—is needed to break away from the pack for companies to win long-term. 2025 is the year governance becomes the launchpad for AI innovation.',
            'aussage_kurz': 'AI governance as competitive advantage and innovation launchpad',
            'modus': 'schriftlich',
            'quell_link': 'https://www.credo.ai/blog/from-pioneering-partnerships-to-groundbreaking-products-accelerating-enterprise-ai-innovation-with-governance-into-2025',
            'quell_titel': 'From Pioneering Partnerships to Groundbreaking Products - Credo AI Blog',
            'datum_aussage': '2024-12-01',
            'sprache': 'en',
            'kontext': 'Looking ahead to 2025, positioning governance as strategic enabler rather than obstacle'
        },
        # 3. Microsoft Partnership
        {
            'aussage_text': 'When I think about some of the most transformational companies, Microsoft is up there not only as an AI leader, but as a company that has been leading with trust and leading with the right leadership of Satya Nadella at the forefront. And so to partner with an AI first company, the leader AI, and a company that believes in trust as deeply as we do has been just phenomenal.',
            'aussage_kurz': 'Microsoft partnership based on shared trust values',
            'modus': 'muendlich',
            'quell_link': 'https://www.credo.ai/blog/from-pioneering-partnerships-to-groundbreaking-products-accelerating-enterprise-ai-innovation-with-governance-into-2025',
            'quell_titel': 'From Pioneering Partnerships to Groundbreaking Products - Credo AI Blog',
            'datum_aussage': '2024-11-01',
            'sprache': 'en',
            'kontext': 'Discussing the strategic partnership between Credo AI and Microsoft Azure AI'
        },
        # 4. AI-first, Ethics-forward Approach
        {
            'aussage_text': 'Responsible AI is building systems that are not only powerful, but fair, transparent, and aligned with human values—the difference between tech that serves society and tech that risks it.',
            'aussage_kurz': 'Responsible AI: power + fairness + transparency + human values',
            'modus': 'muendlich',
            'quell_link': 'https://www.madrona.com/credo-ai-navrina-singh-responsible-ai-governance/',
            'quell_titel': 'Credo AI Founder Navrina Singh on Responsible AI - Madrona',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Defining responsible AI and AI-first, ethics-forward approach'
        },
        # 5. Vision für Ecosystem
        {
            'aussage_text': 'Success is creating an ecosystem of enterprises, builders, and policymakers all coming together to be equally invested in trustworthy AI and governance from the onset, not when something goes wrong.',
            'aussage_kurz': 'Ecosystem vision: proactive governance from the onset',
            'modus': 'muendlich',
            'quell_link': 'https://www.madrona.com/credo-ai-navrina-singh-responsible-ai-governance/',
            'quell_titel': 'Credo AI Founder Navrina Singh on Responsible AI - Madrona',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Vision for collaborative approach to AI governance across stakeholders'
        },
        # 6. China AI Race Warning
        {
            'aussage_text': 'America will lose the artificial intelligence race with China if the industry doesn\'t implement tougher safety standards. America\'s effort to win out over China would falter if businesses and consumers don\'t trust the U.S.\' safety framework.',
            'aussage_kurz': 'US needs safety standards to win AI race with China',
            'modus': 'muendlich',
            'quell_link': 'https://www.axios.com/2025/09/17/credo-ai-ceo-china-safety-standards',
            'quell_titel': 'Credo AI CEO: U.S. needs safety standards to win AI race with China - Axios',
            'datum_aussage': '2024-09-17',
            'sprache': 'en',
            'kontext': 'Speaking at Axios AI+ DC Summit on US-China AI competition and safety standards'
        },
        # 7. Governance vs. Regulation
        {
            'aussage_text': 'Stronger governance of AI isn\'t the same thing as increased regulation. Governance is about understanding risk and aligning with a company\'s policies and standards.',
            'aussage_kurz': 'Governance is not regulation but risk understanding',
            'modus': 'muendlich',
            'quell_link': 'https://www.axios.com/2025/09/17/credo-ai-ceo-china-safety-standards',
            'quell_titel': 'Credo AI CEO: U.S. needs safety standards to win AI race with China - Axios',
            'datum_aussage': '2024-09-17',
            'sprache': 'en',
            'kontext': 'Clarifying distinction between governance and regulation at AI+ DC Summit'
        },
        # 8. AI can't create value without trust
        {
            'aussage_text': 'AI can\'t create business value without ironclad trust.',
            'aussage_kurz': 'No business value without trust in AI',
            'modus': 'muendlich',
            'quell_link': 'https://www.businesswire.com/news/home/20250812596835/en/Credo-AI-Launches-Advisory-Services-to-Make-Trusted-AI-Governance-Real-Auditable-and-Measurable',
            'quell_titel': 'Credo AI Launches Advisory Services - BusinessWire',
            'datum_aussage': '2024-08-12',
            'sprache': 'en',
            'kontext': 'Launch of Credo AI Advisory Services for trusted AI governance'
        },
        # 9. Operational, measurable governance
        {
            'aussage_text': 'AI trustworthy with governance that is operational, measurable, and embedded into the way AI is built and deployed.',
            'aussage_kurz': 'Governance must be operational, measurable, embedded',
            'modus': 'schriftlich',
            'quell_link': 'https://www.businesswire.com/news/home/20250812596835/en/Credo-AI-Launches-Advisory-Services-to-Make-Trusted-AI-Governance-Real-Auditable-and-Measurable',
            'quell_titel': 'Credo AI Launches Advisory Services - BusinessWire',
            'datum_aussage': '2024-08-12',
            'sprache': 'en',
            'kontext': 'Describing Credo AI\'s approach to making governance practical and actionable'
        },
        # 10. Governance enables scaling
        {
            'aussage_text': 'Managing the risks of generative AI is the only way the tech can be scaled, and it\'s all about oversight, control, and getting to trust very fast.',
            'aussage_kurz': 'Risk management is prerequisite for AI scaling',
            'modus': 'muendlich',
            'quell_link': 'https://www.businesswire.com/news/home/20250828691688/en/TIME-Names-Credo-AI-Founder-and-CEO-Navrina-Singh-One-of-the-100-Most-Influential-People-in-AI',
            'quell_titel': 'TIME Names Navrina Singh One of 100 Most Influential in AI - BusinessWire',
            'datum_aussage': '2024-08-28',
            'sprache': 'en',
            'kontext': 'Explaining why governance is enabler, not obstacle, for AI innovation'
        },
        # 11. Enthusiasm für 2024/2025 AI Fortschritte
        {
            'aussage_text': 'I am exhilarated by AI\'s rapid advancements—from multimodal models to enterprise adoption—and humbled by our shared responsibility to ensure it serves humanity\'s best interests.',
            'aussage_kurz': 'Exhilarated by AI progress, humbled by responsibility',
            'modus': 'schriftlich',
            'quell_link': 'https://www.credo.ai/blog/from-pioneering-partnerships-to-groundbreaking-products-accelerating-enterprise-ai-innovation-with-governance-into-2025',
            'quell_titel': 'From Pioneering Partnerships to Groundbreaking Products - Credo AI Blog',
            'datum_aussage': '2024-12-01',
            'sprache': 'en',
            'kontext': 'Year-end reflection on 2024 AI developments and looking to 2025'
        },
        # 12. Fairness is context-dependent
        {
            'aussage_text': 'An AI system can be considered to be "fair," in the sense of algorithmic fairness, if it does not perpetuate or amplify harmful societal biases in its systems. The concept of fairness is incredibly context-dependent.',
            'aussage_kurz': 'AI fairness is context-dependent, avoiding bias amplification',
            'modus': 'schriftlich',
            'quell_link': 'https://republicans-science.house.gov/_cache/files/1/2/12f7f6fc-4925-47f5-b2aa-a488c9fbaba5/3A99526F6CEAA6850FB5511D506BB73808533BF178BF02AE63906A94E68A4965.2022-09-29-singh-testimony.pdf',
            'quell_titel': 'Prepared Testimony before House Committee on Science, Space and Technology',
            'datum_aussage': '2022-09-29',
            'sprache': 'en',
            'kontext': 'Congressional testimony on Trustworthy AI: Managing the Risks of Artificial Intelligence'
        },
        # 13. Transparency in AI value chain
        {
            'aussage_text': 'To achieve "transparency in AI," it is necessary to inject disclosures throughout the entire AI value chain, including comprehensive AI use case risk reporting, model cards, data set cards, and algorithmic impact assessments (AIAs).',
            'aussage_kurz': 'AI transparency requires disclosures across entire value chain',
            'modus': 'schriftlich',
            'quell_link': 'https://republicans-science.house.gov/_cache/files/1/2/12f7f6fc-4925-47f5-b2aa-a488c9fbaba5/3A99526F6CEAA6850FB5511D506BB73808533BF178BF02AE63906A94E68A4965.2022-09-29-singh-testimony.pdf',
            'quell_titel': 'Prepared Testimony before House Committee on Science, Space and Technology',
            'datum_aussage': '2022-09-29',
            'sprache': 'en',
            'kontext': 'Congressional testimony defining technical requirements for AI transparency'
        },
        # 14. Foundation Model Transparency Index
        {
            'aussage_text': 'Introducing The Foundation Model Transparency Index - this aligns with methodology that Credo AI used for their GenAI Risk profiles.',
            'aussage_kurz': 'Stanford FMTI aligns with Credo AI methodology',
            'modus': 'schriftlich',
            'quell_link': 'https://www.linkedin.com/posts/navrina_introducing-the-foundation-model-transparency-activity-7120528555444166656-zCaa',
            'quell_titel': 'Navrina Singh LinkedIn Post on Foundation Model Transparency Index',
            'datum_aussage': '2023-10-20',
            'sprache': 'en',
            'kontext': 'Commenting on Stanford\'s Foundation Model Transparency Index release'
        },
        # 15. Technology serving humanity
        {
            'aussage_text': 'How do we become the standard of good AI and defining what that good looks like so that this technology works in service of humanity.',
            'aussage_kurz': 'Technology must work in service of humanity',
            'modus': 'muendlich',
            'quell_link': 'https://www.ice.com/insights/conversations/inside-the-ice-house/credo-ai-founder-and-ceo-navrina-singh-on-ai-governance-responsibility-and-accessibility',
            'quell_titel': 'Credo AI Founder & CEO on AI Governance - Inside the ICE House',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'ICE House interview on AI governance and responsibility'
        },
        # 16. RAI Definition
        {
            'aussage_text': 'Responsible AI includes assessment, reporting, and governance to the highest of ethical standards in order to ensure a fair, transparent, compliant, and auditable environment for the development and use of artificial intelligence.',
            'aussage_kurz': 'RAI: assessment, reporting, governance to highest ethical standards',
            'modus': 'schriftlich',
            'quell_link': 'https://oecd.ai/en/community/navrina-singh',
            'quell_titel': 'Navrina Singh - OECD.AI Expert Profile',
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'OECD AI Expert profile defining Responsible AI principles'
        },
        # 17. QWISE Founding Vision
        {
            'aussage_text': 'The simple goal was to energize women engineers and focus on personal and professional development. What started with 17 women grew to 1,800 members strong all over the world, with 12 chapters.',
            'aussage_kurz': 'QWISE grew from 17 to 1,800 women engineers worldwide',
            'modus': 'muendlich',
            'quell_link': 'http://www.sddt.com/Reports/article.cfm?RID=1035&SourceCode=20140306cre',
            'quell_titel': 'Qualcomm exec encourages women to raise their hand - San Diego Source',
            'datum_aussage': '2014-03-06',
            'sprache': 'en',
            'kontext': 'Reflecting on founding and growth of QWISE at Qualcomm'
        },
        # 18. ImpaQt Innovation Philosophy
        {
            'aussage_text': 'The ImpaQt blueprint consists of three phases—Ideation, Review and Prototyping—and the program engages the entire employee population, with those who come up with workable ideas remaining involved in their projects all the way through to fruition, creating and nurturing a culture of innovation and collaboration.',
            'aussage_kurz': 'ImpaQt: employee-driven innovation from ideation to fruition',
            'modus': 'muendlich',
            'quell_link': 'https://www.innovationleader.com/topics/articles-and-content-by-topic/strategy-and-governance/qualcomm-on-building-an-internal-startup-venture-capital-ecosystem/',
            'quell_titel': 'Qualcomm on Building Internal Startup Ecosystem - InnoLead',
            'datum_aussage': '2016-01-01',
            'sprache': 'en',
            'kontext': 'Describing Qualcomm ImpaQt innovation incubator structure'
        },
        # 19. Marketplace for Ethical AI Tools (MERAT)
        {
            'aussage_text': 'The goal was to create an ecosystem for startups and Global 2000s focusing on responsible development of AI through the Marketplace for Ethical and Responsible AI Tools.',
            'aussage_kurz': 'MERAT: ecosystem for responsible AI development',
            'modus': 'muendlich',
            'quell_link': 'https://blog.mozilla.org/en/mozilla/navrina-singh-joins-the-mozilla-foundation-board-of-directors/',
            'quell_titel': 'Navrina Singh Joins Mozilla Foundation Board - Mozilla Blog',
            'datum_aussage': '2021-01-01',
            'sprache': 'en',
            'kontext': 'Describing nonprofit MERAT initiative before founding Credo AI'
        },
        # 20. Speed and Caution in AI Race
        {
            'aussage_text': 'In A.I. Race, Microsoft and Google Choose Speed Over Caution - we need to ensure governance keeps pace with innovation.',
            'aussage_kurz': 'Governance must keep pace with AI innovation speed',
            'modus': 'schriftlich',
            'quell_link': 'https://lt.linkedin.com/posts/navrina_in-ai-race-microsoft-and-google-choose-activity-7050681248318459904-4nnV',
            'quell_titel': 'Navrina Singh LinkedIn Post on AI Race Speed vs Caution',
            'datum_aussage': '2023-04-10',
            'sprache': 'en',
            'kontext': 'Commentary on Microsoft and Google\'s rapid AI deployment'
        }
    ]

    # HANDLUNGEN - Actions and Events
    handlungen = [
        # 1. Gründung Credo AI
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Founded Credo AI with co-founder Eli Chen, an AI governance platform to help organizations build AI aligned with human values and deliver responsible AI at scale',
            'datum_handlung': '2020-03-01',
            'quell_link': 'https://www.madrona.com/credo-ai-navrina-singh-responsible-ai-governance/',
            'quell_titel': 'Credo AI Founder Navrina Singh on Responsible AI - Madrona',
            'kontext': 'Company founding after nearly 20 years at Microsoft and Qualcomm'
        },
        # 2. Series A Funding
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Credo AI raised $12.8 million Series A funding led by Sands Capital, with follow-on investments from Decibel VC and AI Fund',
            'datum_handlung': '2022-05-17',
            'quell_link': 'https://www.prnewswire.com/news-releases/credo-ai-closes-12-8-million-series-a-funding-round-led-by-sands-capital-301548311.html',
            'quell_titel': 'Credo AI Closes $12.8 Million Series A Funding - PR Newswire',
            'kontext': 'Series A led by Sands Capital Partner Scott Frederick, total raised $12.8M'
        },
        # 3. NAIAC Appointment
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Appointed by U.S. Department of Commerce as one of 27 members to the National Artificial Intelligence Advisory Committee (NAIAC) to advise the President and National AI Initiative Office',
            'datum_handlung': '2022-04-01',
            'quell_link': 'https://www.commerce.gov/news/press-releases/2022/04/us-department-commerce-appoints-27-members-national-ai-advisory',
            'quell_titel': 'U.S. Department of Commerce Appoints 27 Members to NAIAC - Commerce.gov',
            'kontext': 'First appointments to committee created by National AI Initiative Act of 2020'
        },
        # 4. Congressional Testimony
        {
            'handlung_typ': 'politisch',
            'beschreibung': 'Testified before House Committee on Science, Space and Technology at hearing "Trustworthy AI: Managing the Risks of Artificial Intelligence" on AI governance and risk management',
            'datum_handlung': '2022-09-29',
            'quell_link': 'https://science.house.gov/2022/9/research-technology-subcommittee-hearing-trustworthy-ai-managing-the-risks-of-artificial-intelligence',
            'quell_titel': 'Research and Technology Subcommittee Hearing - Trustworthy AI - House Science Committee',
            'kontext': 'Congressional testimony on trustworthy AI and managing AI risks'
        },
        # 5. WEF Technology Pioneer Recognition
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Credo AI recognized as 2022 World Economic Forum Technology Pioneer for leadership in AI governance',
            'datum_handlung': '2022-06-01',
            'quell_link': 'https://www.credo.ai/our-ethos',
            'quell_titel': 'Credo AI - Credo-bility - Company Ethos',
            'kontext': 'WEF Technology Pioneer recognition alongside other awards in 2022'
        },
        # 6. Mozilla Foundation Board
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Joined Mozilla Foundation Board of Directors as executive board member to guide trustworthy AI charter and support Mozilla AI initiatives',
            'datum_handlung': '2021-01-01',
            'quell_link': 'https://blog.mozilla.org/en/mozilla/navrina-singh-joins-the-mozilla-foundation-board-of-directors/',
            'quell_titel': 'Navrina Singh Joins Mozilla Foundation Board of Directors - Mozilla Blog',
            'kontext': 'Board role supporting Mozilla\'s trustworthy AI charter, leveraging MERAT experience'
        },
        # 7. Series B Funding 2024
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Credo AI raised $21 million Series B funding led by CrimsoNox Capital, Mozilla Ventures and FPV Ventures, with participation from Sands Capital, Decibel VC, Booz Allen Hamilton and AI Fund, valuing company at $101 million',
            'datum_handlung': '2024-07-30',
            'quell_link': 'https://siliconangle.com/2024/07/30/credo-ai-raises-21m-help-enterprises-deploy-ai-safely-responsibly-compliant-way/',
            'quell_titel': 'Credo AI raises $21M - SiliconANGLE',
            'kontext': 'Series B funding bringing total raised to $41.3 million, $101M valuation'
        },
        # 8. Microsoft Partnership
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Credo AI partnered with Microsoft Azure AI to deliver end-to-end AI governance for Azure AI applications, including GPT-4, GPT-4o, Phi-3 models, and comprehensive oversight of generative AI, multimodal models, and RAG use cases',
            'datum_handlung': '2024-11-01',
            'quell_link': 'https://www.streetinsider.com/Business+Wire/Credo+AI+and+Microsoft+Partner+to+Power+End-to-End+AI+Governance+for+Enterprise+Applications/24003857.html',
            'quell_titel': 'Credo AI and Microsoft Partner to Power AI Governance - StreetInsider',
            'kontext': 'Strategic partnership enabling governance for Microsoft Azure AI enterprise solutions'
        },
        # 9. UN AI Advisory Board
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Appointed as AI Expert for UN Secretary-General\'s High-Level Advisory Body on AI at United Nations to advise on AI governance and policy',
            'datum_handlung': '2024-03-01',
            'quell_link': 'https://engineering.wisc.edu/blog/ece-alum-navrina-singh-named-to-time100-ai/',
            'quell_titel': 'ECE alum Navrina Singh named to Time100 AI - UW-Madison Engineering',
            'kontext': 'UN appointment as AI expert alongside NAIAC, OECD, and WEF roles'
        },
        # 10. TIME100 AI Recognition
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Named by TIME to 2025 TIME100 AI list as one of the 100 most influential people in artificial intelligence for work in AI governance and Credo AI\'s impact',
            'datum_handlung': '2024-08-28',
            'quell_link': 'https://time.com/collections/time100-ai-2025/7305855/navrina-singh/',
            'quell_titel': 'Navrina Singh: The 100 Most Influential People in AI 2025 - TIME',
            'kontext': 'Recognition for quadrupling revenue, doubling customer base, 100% platform retention'
        },
        # 11. Inc. Female Founders 500
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Recognized on Inc.\'s 2025 Female Founders 500 list for introducing Microsoft partnership, quadrupling revenue, and securing $21M Series B funding',
            'datum_handlung': '2024-04-01',
            'quell_link': 'https://www.inc.com/profile/navrina-singh',
            'quell_titel': 'Navrina Singh on Inc. 2025 Female Founders 500 List - Inc.',
            'kontext': 'Recognition for business growth and strategic partnerships in 2024'
        },
        # 12. Credo AI Advisory Services Launch
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launched Credo AI Advisory Services to make trusted AI governance real, auditable, and measurable for enterprise clients',
            'datum_handlung': '2024-08-12',
            'quell_link': 'https://www.businesswire.com/news/home/20250812596835/en/Credo-AI-Launches-Advisory-Services-to-Make-Trusted-AI-Governance-Real-Auditable-and-Measurable',
            'quell_titel': 'Credo AI Launches Advisory Services - BusinessWire',
            'kontext': 'Product expansion beyond platform to include advisory services'
        },
        # 13. QWISE Founding at Qualcomm
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Founded QWISE (Qualcomm Women in Science and Engineering), Qualcomm\'s first women\'s initiative focused on personal and professional development of women in leadership roles, growing from 17 members to 1,800 members with 12 global chapters',
            'datum_handlung': '2005-01-01',
            'quell_link': 'http://www.sddt.com/Reports/article.cfm?RID=1035&SourceCode=20140306cre',
            'quell_titel': 'Qualcomm exec encourages women to raise their hand - San Diego Source',
            'kontext': 'Grassroots initiative at Qualcomm to support women engineers globally'
        },
        # 14. Axios AI+ DC Summit Speaking
        {
            'handlung_typ': 'politisch',
            'beschreibung': 'Spoke at Axios AI+ DC Summit warning that America will lose AI race with China without tougher safety standards, arguing governance is key to competitive advantage',
            'datum_handlung': '2024-09-17',
            'quell_link': 'https://www.axios.com/2025/09/17/credo-ai-ceo-china-safety-standards',
            'quell_titel': 'Credo AI CEO: U.S. needs safety standards to win AI race with China - Axios',
            'kontext': 'High-profile speaking engagement on US-China AI competition and safety'
        },
        # 15. MERAT Non-profit Initiative
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Led non-profit initiative MERAT (Marketplace for Ethical and Responsible AI Tools) focused on building, testing and deploying AI responsibly, creating ecosystem for startups and enterprises',
            'datum_handlung': '2019-01-01',
            'quell_link': 'https://blog.mozilla.org/en/mozilla/navrina-singh-joins-the-mozilla-foundation-board-of-directors/',
            'quell_titel': 'Navrina Singh Joins Mozilla Foundation Board - Mozilla Blog',
            'kontext': 'Non-profit work on responsible AI before founding Credo AI'
        }
    ]

    print(f"Inserting {len(aussagen)} Aussagen for person_id={PERSON_ID}...")
    for aussage in aussagen:
        cursor.execute('''
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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

    print(f"Inserting {len(handlungen)} Handlungen for person_id={PERSON_ID}...")
    for handlung in handlungen:
        cursor.execute('''
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            PERSON_ID,
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))

    conn.commit()

    # Verify inserts
    cursor.execute('SELECT COUNT(*) FROM aussagen WHERE person_id = ?', (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM handlungen WHERE person_id = ?', (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    conn.close()

    print("\n" + "="*70)
    print(f"INSERT COMPLETED for Navrina Singh (person_id={PERSON_ID})")
    print("="*70)
    print(f"Total Aussagen inserted:   {len(aussagen)}")
    print(f"Total Handlungen inserted: {len(handlungen)}")
    print(f"\nVerified in database:")
    print(f"  Aussagen:   {aussagen_count}")
    print(f"  Handlungen: {handlungen_count}")
    print("="*70)

if __name__ == '__main__':
    insert_data()
