#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datenbank-Inserts für Rene Haas (person_id=84)
Arm Holdings CEO - Aussagen und Handlungen
Recherche-Datum: 2026-02-12
"""

import sqlite3
import os

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID
PERSON_ID = 84

def insert_data():
    """Fügt Aussagen und Handlungen für Rene Haas in die Datenbank ein."""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (10-20 Statements)
    aussagen = [
        # AI & Technology Worldview
        (PERSON_ID,
         "we are going to see some very, very profound advancements around AI going forward",
         "profound AI advancements ahead",
         "muendlich",
         "https://stratechery.com/2024/an-interview-with-arm-ceo-rene-haas/",
         "An Interview with Arm CEO Rene Haas - Stratechery",
         "2024-01-01",
         "en",
         "Interview discussing AI's future impact and Arm's role in the AI revolution"),

        (PERSON_ID,
         "the ChatGPT moment...was a tipping point relative to what the capability of these large language models could do",
         "ChatGPT was a tipping point",
         "muendlich",
         "https://stratechery.com/2024/an-interview-with-arm-ceo-rene-haas/",
         "An Interview with Arm CEO Rene Haas - Stratechery",
         "2024-01-01",
         "en",
         "Reflecting on the transformative impact of ChatGPT on public understanding of AI capabilities"),

        (PERSON_ID,
         "there are a lot of social and ethical type of things to consider, which I think as a society, we have to figure out",
         "society must address AI ethics",
         "muendlich",
         "https://stratechery.com/2024/an-interview-with-arm-ceo-rene-haas/",
         "An Interview with Arm CEO Rene Haas - Stratechery",
         "2024-01-01",
         "en",
         "Acknowledging ethical challenges posed by advancing AI technology"),

        (PERSON_ID,
         "I just don't ascribe to the idea that AI is overhyped",
         "AI is not overhyped",
         "muendlich",
         "https://theaiinsider.tech/2024/10/23/arm-ceo-rene-haas-sees-ai-as-a-turning-point-not-a-bubble/",
         "Arm CEO Rene Haas Sees AI as a Turning Point, Not a Bubble",
         "2024-10-23",
         "en",
         "Defending AI's significance against criticism of industry hype"),

        (PERSON_ID,
         "AI agents will run locally on your glasses, your wearable, your phone",
         "AI will run on all devices",
         "muendlich",
         "https://www.cnbc.com/video/2026/01/20/arm-ceo-rene-haas-ai-models-will-become-very-domain-specific-in-the-future.html",
         "Arm CEO: AI models will become 'very domain-specific' in the future - CNBC",
         "2026-01-20",
         "en",
         "Predicting the future of distributed AI computing across personal devices"),

        (PERSON_ID,
         "AI is moving so quickly… it's going to require a level of innovation that we haven't yet seen",
         "AI requires unprecedented innovation",
         "muendlich",
         "https://www.weforum.org/stories/2026/01/ai-energy-demand-challenge/",
         "65 global leaders share how to scale AI responsibly to 2035 - World Economic Forum",
         "2026-01-01",
         "en",
         "Speaking at Davos 2026 World Economic Forum Annual Meeting about AI's pace of development"),

        # Energy & Sustainability
        (PERSON_ID,
         "Research done by universities in this space around sustainability and energy efficiency is a huge, huge opportunity",
         "sustainability is huge opportunity",
         "muendlich",
         "https://www.cmu.edu/news/stories/archives/2025/august/arm-ceo-rene-haas-talks-ai-at-presidents-lecture-series",
         "Arm CEO Rene Haas Talks AI at President's Lecture Series - Carnegie Mellon University",
         "2025-08-01",
         "en",
         "Carnegie Mellon University President's Lecture Series on AI and energy efficiency"),

        (PERSON_ID,
         "Arm is the world's most power-efficient CPU because our DNA was to build processors that run on batteries",
         "Arm built for power efficiency",
         "muendlich",
         "https://www.cnbc.com/2025/10/15/arm-holdings-ceo-move-ai-workloads-from-cloud-reduce-power-consumption-energy-.html",
         "Arm CEO says moving some AI workloads from the cloud will make it more sustainable - CNBC",
         "2025-10-15",
         "en",
         "Explaining Arm's competitive advantage in energy-efficient computing"),

        (PERSON_ID,
         "Everyone is looking to maintain the same level of energy for far more compute",
         "need more compute with same energy",
         "muendlich",
         "https://time.com/collections/davos-2025/7204668/rene-haas-arm-chips-ai/",
         "Rene Haas on What Makes Arm's Chips Indispensable - TIME",
         "2025-01-01",
         "en",
         "TIME interview at Davos 2025 discussing industry-wide energy efficiency challenges"),

        (PERSON_ID,
         "moving those AI workloads away from the cloud to local applications",
         "move AI from cloud to edge",
         "muendlich",
         "https://www.cnbc.com/2025/10/15/arm-holdings-ceo-move-ai-workloads-from-cloud-reduce-power-consumption-energy-.html",
         "Arm CEO says moving some AI workloads from the cloud will make it more sustainable - CNBC",
         "2025-10-15",
         "en",
         "Advocating for edge computing to reduce energy consumption from massive data centers"),

        (PERSON_ID,
         "if efficiency is not improved, the electricity consumption of artificial intelligence data centers may be as high as 20% to 25% of the US electricity demand by 2030",
         "AI could consume 25% US electricity by 2030",
         "muendlich",
         "https://news.futunn.com/en/post/40634257/will-ai-eat-1-4-of-america-s-electricity-after",
         "Will AI eat 1/4 of America's electricity after six years? Arm CEO warns",
         "2025-10-15",
         "en",
         "Warning about unsustainable energy consumption trajectory of AI data centers"),

        (PERSON_ID,
         "AI has the potential to exceed all the transformative innovations created in the past century. The benefits to society around healthcare, productivity, education and many other areas will be beyond our imagination",
         "AI exceeds century of innovation",
         "schriftlich",
         "https://newsroom.arm.com/blog/driving-ai-datacenter-compute-efficiency",
         "Arm's Mission to Help Tackle AI's Insatiable Energy Needs - Arm Newsroom",
         "2025-01-01",
         "en",
         "Expressing optimistic vision for AI's transformative potential across sectors"),

        # Leadership & Innovation Philosophy
        (PERSON_ID,
         "experiment often and be really comfortable with failing. Mistakes are made...be happy with failure, because that will give you the advancement that you really deserve and want",
         "embrace failure for advancement",
         "muendlich",
         "https://www.thetwentyminutevc.com/rene-haas",
         "20VC: Arm CEO Rene Haas on Leadership and Decision Making",
         "2024-01-01",
         "en",
         "Leadership philosophy on innovation, experimentation, and learning from failure"),

        (PERSON_ID,
         "curiosity is that pilot light that keeps you going, and if you've got a natural curiosity for doing things, you're going to go pretty far",
         "curiosity drives success",
         "muendlich",
         "https://www.thetwentyminutevc.com/rene-haas",
         "20VC: Arm CEO Rene Haas on Leadership",
         "2024-01-01",
         "en",
         "Personal philosophy on the importance of curiosity in professional development"),

        # Business Model & Strategy
        (PERSON_ID,
         "the world runs on Arm, it's hard to find an end device that doesn't run on Arm",
         "world runs on Arm",
         "muendlich",
         "https://stratechery.com/2024/an-interview-with-arm-ceo-rene-haas/",
         "An Interview with Arm CEO Rene Haas - Stratechery",
         "2024-01-01",
         "en",
         "Asserting Arm's ubiquity and dominance in the computing ecosystem"),

        (PERSON_ID,
         "our products can be built at any fab by any chip company",
         "open fab-agnostic model",
         "muendlich",
         "https://stratechery.com/2024/an-interview-with-arm-ceo-rene-haas/",
         "An Interview with Arm CEO Rene Haas - Stratechery",
         "2024-01-01",
         "en",
         "Describing Arm's competitive advantage through open licensing model"),

        (PERSON_ID,
         "AI's next era will be defined by delivering efficiency at scale",
         "AI's future is efficiency at scale",
         "muendlich",
         "https://techcrunch.com/2025/10/15/arm-partners-with-meta-to-scale-ai-efforts/",
         "Meta partners up with Arm to scale AI efforts - TechCrunch",
         "2025-10-15",
         "en",
         "Statement accompanying Meta partnership announcement on AI infrastructure"),

        (PERSON_ID,
         "It's a great day for the company…Our bankers say if you can price at the high end of the range and go out of that number, it's a good thing",
         "successful IPO pricing",
         "muendlich",
         "https://www.cnn.com/videos/business/2023/09/14/exp-arm-public-listing-rene-haas-live-091403pseg1-cnni-business.cnn",
         "Arm CEO speaks about company's $54 billion stock market listing - CNN Business",
         "2023-09-14",
         "en",
         "Reacting to Arm's successful $54.5 billion IPO, the largest of 2023"),
    ]

    # HANDLUNGEN (8-15 Actions)
    handlungen = [
        # CEO Appointment
        (PERSON_ID,
         "einstellung",
         "Appointed as Chief Executive Officer of Arm Holdings, succeeding Simon Segars after 30 years with the company. Appointment coincided with collapse of Nvidia acquisition deal.",
         "2022-02-08",
         "https://newsroom.arm.com/news/arm-appoints-rene-haas-as-ceo",
         "Arm Appoints Rene Haas as Chief Executive Officer - Arm Newsroom",
         "Leadership transition during critical period following failed Nvidia merger, with responsibility for preparing company for IPO"),

        # Workforce Restructuring
        (PERSON_ID,
         "umstrukturierung",
         "Reformed executive leadership team within weeks of appointment, letting three executives go and reshaping organizational structure",
         "2022-02-28",
         "https://fortune.com/2022/02/08/new-arm-ceo-rene-haas-challenges-collapse-nvidia-deal-fired-china-head-softbank/",
         "New Arm CEO faces challenges after Nvidia deal collapse - Fortune",
         "Early leadership restructuring to align team with new strategic vision post-Nvidia deal failure"),

        (PERSON_ID,
         "entlassung",
         "Announced layoffs of 12-15% of global workforce (up to 1,000 employees out of 6,400), with UK hit hardest at 20% reduction. Most cuts avoided engineering roles to preserve product roadmap.",
         "2022-03-14",
         "https://www.bloomberg.com/news/articles/2022-03-14/softbank-s-arm-to-cut-up-to-15-of-workforce-as-it-prepares-ipo",
         "SoftBank's Arm to Cut Up to 15% as It Prepares IPO - Bloomberg",
         "Cost-cutting measures to improve financial performance ahead of planned IPO after Nvidia acquisition collapsed"),

        # IPO Execution
        (PERSON_ID,
         "produktlaunch",
         "Led Arm Holdings' initial public offering on Nasdaq, pricing at $51/share and raising $4.87 billion in the largest IPO of 2023. Company valued at $54.5 billion. Stock opened at $56.10 and closed first day at $63.59 (+24%).",
         "2023-09-14",
         "https://newsroom.arm.com/news/arm-announces-pricing-of-initial-public-offering",
         "Arm Announces Pricing of Initial Public Offering - Arm Newsroom",
         "Successfully returned Arm to public markets seven years after SoftBank's $32 billion acquisition in 2016"),

        # Strategic Partnerships
        (PERSON_ID,
         "partnerschaft",
         "Established partnerships with Alibaba, Ampere, AWS, Bosch, Denso, Mobileye and Telechips as new entrants to Arm ecosystem through IPG investments in vertical market solutions",
         "2022-01-01",
         "https://newsroom.arm.com/news/arm-appoints-rene-haas-as-ceo",
         "Arm Appoints Rene Haas as Chief Executive Officer - Arm Newsroom",
         "Expanded Arm ecosystem during tenure as president of IP Products Group (2017-2022), diversifying into automotive, cloud infrastructure, and IoT markets"),

        (PERSON_ID,
         "partnerschaft",
         "Announced expanded multi-year partnership with Meta Platforms for AI infrastructure, moving Meta's ranking and recommendation systems to Arm's Neoverse platform optimized for cloud AI",
         "2025-10-15",
         "https://techcrunch.com/2025/10/15/arm-partners-with-meta-to-scale-ai-efforts/",
         "Meta partners up with Arm to scale AI efforts - TechCrunch",
         "Partnership focused on delivering efficiency at scale for AI workloads, without equity stakes or infrastructure exchanges"),

        (PERSON_ID,
         "partnerschaft",
         "Strengthened partnerships with OpenAI and SoftBank to drive AI productivity across global technology sector",
         "2025-02-03",
         "https://group.softbank/en/news/press/20250203_0",
         "OpenAI and SoftBank Group Partner with Arm support - SoftBank Group",
         "Strategic collaboration ensuring Arm remains primary compute platform for AI workloads globally"),

        # Legal Actions
        (PERSON_ID,
         "klage",
         "Filed lawsuit against Qualcomm and Nuvia for breach of license agreements and trademark infringement following Qualcomm's 2021 acquisition of Nuvia",
         "2022-08-31",
         "https://newsroom.arm.com/news/arm-files-lawsuit-against-qualcomm-and-nuvia-for-breach-of-license-agreements-and-trademark-infringement",
         "Arm Files Lawsuit Against Qualcomm and Nuvia - Arm Newsroom",
         "Legal action over disputed license transfers and chip designs developed using Arm technology"),

        (PERSON_ID,
         "klage",
         "Issued 60-day notice to terminate Qualcomm's architectural license agreement, escalating legal dispute over chip design licensing",
         "2024-10-23",
         "https://www.bnnbloomberg.ca/business/company-news/2024/10/23/arm-to-cancel-qualcomm-chip-design-license-in-escalation-of-feud/",
         "Arm to Cancel Qualcomm Chip Design License in Escalation of Feud - Bloomberg",
         "Aggressive legal strategy reflecting shift in business model toward offering more complete chip designs and seeking greater compensation for engineering work"),

        (PERSON_ID,
         "klage",
         "Ended legal efforts to terminate Qualcomm's license after jury concluded Qualcomm had not violated license terms and chips using Nuvia technology were properly licensed",
         "2025-02-06",
         "https://www.theregister.com/2025/02/06/arm_qualcomm_nuvia/",
         "Arm ends legal efforts to terminate Qualcomm's license - The Register",
         "Legal defeat in major licensing dispute, forced to abandon termination strategy"),

        # Board Appointments
        (PERSON_ID,
         "einstellung",
         "Appointed as Non-Executive Director to AstraZeneca PLC board, bringing deep technology expertise in data science, computing and AI to pharmaceutical company",
         "2025-01-01",
         "https://www.marketscreener.com/quote/stock/ASTRAZENECA-PLC-4000930/news/AstraZeneca-PLC-Appoints-Rene-Haas-and-Birgit-Conix-as-Non-Executive-Directors-Effective-January-1-48597443/",
         "AstraZeneca Appoints Rene Haas as Non-Executive Director - MarketScreener",
         "Cross-industry board role leveraging semiconductor and AI expertise in healthcare/pharmaceutical sector"),

        # Product Strategy
        (PERSON_ID,
         "produktlaunch",
         "Introduced automotive-enhanced Armv9 CPU profiles specifically designed for autonomous driving and self-driving cars",
         "2024-05-09",
         "https://www.benzinga.com/news/earnings/24/05/38721328/arm-ceo-rene-haas-bets-big-on-automotive-with-armv9-autonomous-driving-solutions-this-is-very-very-",
         "ARM CEO Rene Haas Bets Big On Automotive With ARMv9 - Benzinga",
         "Strategic expansion into autonomous vehicle market with specialized chip architecture. Haas stated 'This is very, very significant' regarding automotive opportunity"),

        # Government/Policy Partnerships
        (PERSON_ID,
         "partnerschaft",
         "Secured agreement with Malaysian government for $250 million over ten years for AI chip design blueprints, including IP access, training 10,000 local engineers, and establishing Kuala Lumpur office",
         "2025-03-01",
         "https://time.com/collections/time100-ai-2025/7305840/rene-haas/",
         "Rene Haas: The 100 Most Influential People in AI 2025 - TIME",
         "Major government partnership demonstrating Arm's strategic expansion into national AI infrastructure development and technology transfer"),

        (PERSON_ID,
         "politisch",
         "Participated in US-Japan announcement of university-corporate AI partnerships worth $110 million with support from Arm",
         "2025-01-01",
         "https://newsroom.arm.com/news/ai-partnerships-support-from-arm",
         "Rene Haas' Comments on US-Japan AI Partnerships - Arm Newsroom",
         "International cooperation on AI research and development, supporting academic-industry collaboration"),
    ]

    # Aussagen einfügen
    print(f"Füge {len(aussagen)} Aussagen ein...")
    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen
            (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # Handlungen einfügen
    print(f"Füge {len(handlungen)} Handlungen ein...")
    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen
            (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    # Änderungen speichern
    conn.commit()

    # Bestätigung
    print(f"\n=== ERFOLGREICH EINGEFÜGT ===")
    print(f"Person ID: {PERSON_ID} (Rene Haas)")
    print(f"Aussagen: {len(aussagen)}")
    print(f"Handlungen: {len(handlungen)}")
    print(f"Gesamt: {len(aussagen) + len(handlungen)} Datensätze")

    # Verifikation
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    print(f"\n=== VERIFIKATION ===")
    print(f"Aussagen in DB für person_id {PERSON_ID}: {aussagen_count}")
    print(f"Handlungen in DB für person_id {PERSON_ID}: {handlungen_count}")

    conn.close()
    print(f"\nDatenbank geschlossen: {DB_PATH}")

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        exit(1)

    insert_data()
