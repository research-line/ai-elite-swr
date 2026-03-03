#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data insertion script for Michael Kratsios (person_id=100)
Research database on worldviews of AI/Silicon Valley personalities
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 100

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (Statements)
    aussagen = [
        # 1. AI Regulation & Biden criticism
        (PERSON_ID,
         "The Action Plan very definitively turned the page on AI doomerism and hostility towards AI innovation that had been the hallmark of the Biden administration.",
         "AI doomerism ended under Trump",
         "muendlich",
         "https://www.nbcnews.com/tech/tech-news/kratsios-heads-davos-sell-trumps-light-touch-ai-approach-rcna254497",
         "Kratsios heads to Davos to sell Trump's light-touch AI approach",
         "2025-01-01",
         "en",
         "Statement about Trump AI Action Plan vs Biden approach"
        ),

        # 2. Biden fear-based approach
        (PERSON_ID,
         "To the degree it even tried to accomplish this, the Biden administration failed on its own terms, led by a spirit of fear rather than promise.",
         "Biden led with fear not promise",
         "schriftlich",
         "https://fortune.com/2025/04/15/trump-tech-science-policy-chief-michael-kratsios-talk-austin-innovation-deregulation/",
         "Trump's tech and science policy chief says Biden led with 'spirit of fear'",
         "2025-04-15",
         "en",
         "Endless Frontiers Retreat in Austin, Texas"
        ),

        # 3. Free market approach
        (PERSON_ID,
         "The only way to do so will be to double down on what has made our history of innovation so great, the uniquely American free market approach to scientific discovery, which harnesses the combined strength of government, industry and academia.",
         "Free market approach to innovation",
         "schriftlich",
         "https://www.science.org/content/article/tech-executive-michael-kratsios-confirmed-lead-white-house-science-office-bipartisan",
         "Tech executive confirmed to lead White House science office",
         "2025-03-01",
         "en",
         "Confirmation hearing for OSTP director role"
        ),

        # 4. Four pillars strategy
        (PERSON_ID,
         "Whenever I think about how you structure a national strategy around emerging tech, it typically falls on four pillars – one is R&D [research and development], one is on regulations, one is on international, and the fourth pillar is always workforce.",
         "Four pillars tech strategy framework",
         "schriftlich",
         "https://www.science.org/content/article/tech-executive-michael-kratsios-confirmed-lead-white-house-science-office-bipartisan",
         "Tech executive confirmed to lead White House science office",
         "2025-03-01",
         "en",
         "Outlining strategic framework for emerging technologies"
        ),

        # 5. China competition - dangerous technologies
        (PERSON_ID,
         "The CCP has made it very clear that they will use these technologies for their authoritarian objectives.",
         "CCP uses tech for authoritarianism",
         "schriftlich",
         "https://www.nbcnews.com/tech/tech-news/kratsios-heads-davos-sell-trumps-light-touch-ai-approach-rcna254497",
         "Kratsios heads to Davos to sell Trump's light-touch AI approach",
         "2025-01-01",
         "en",
         "Discussion on emerging technologies and strategic competition"
        ),

        # 6. China - 30 years of subsidizing
        (PERSON_ID,
         "After 30 years of subsidizing Chinese growth, it is time for us to stop helping a rival catch up with us in that race.",
         "Stop helping China catch up",
         "schriftlich",
         "https://www.whitehouse.gov/articles/2025/04/remarks-by-director-kratsios-at-the-endless-frontiers-retreat/",
         "Remarks by Director Kratsios at the Endless Frontiers Retreat",
         "2025-04-15",
         "en",
         "Speech at Endless Frontiers Retreat in Austin"
        ),

        # 7. Export controls strategy
        (PERSON_ID,
         "Strict and simple export controls and know your customer rules, with an unapologetic America-first attitude about enforcing them, are central to stopping China from continuing to build itself up at our expense.",
         "Strict export controls vs China",
         "schriftlich",
         "https://www.washingtontimes.com/news/2025/apr/16/michael-kratsios-wh-tech-director-outlines-new-strategy-winning/",
         "Michael Kratsios outlines new strategy for winning global tech competition",
         "2025-04-16",
         "en",
         "Technology competition strategy"
        ),

        # 8. EU AI Act criticism
        (PERSON_ID,
         "The EU stuff is particularly disappointing. American companies, like, over the barrel of a gun.",
         "EU AI Act disaster for US companies",
         "schriftlich",
         "https://www.nbcnews.com/tech/tech-news/kratsios-heads-davos-sell-trumps-light-touch-ai-approach-rcna254497",
         "White House tech chief slams EU AI Act",
         "2025-01-01",
         "en",
         "Criticism of EU AI regulation at Davos"
        ),

        # 9. EU AI Act - one size fits all
        (PERSON_ID,
         "A terrific example of a mistake that can be made where you try to create a one-size-fits-all regulatory regime, and ultimately you end up with less innovation.",
         "One-size-fits-all regulation kills innovation",
         "schriftlich",
         "https://www.meritalk.com/articles/u-s-cto-michael-kratsios-on-eu-u-s-ai-strategies/",
         "U.S. CTO Michael Kratsios on EU, U.S. AI Strategies",
         "2020-09-01",
         "en",
         "Contrasting US and EU AI regulatory approaches"
        ),

        # 10. Alternative to EU precautionary principle
        (PERSON_ID,
         "The United States is being able to show that there is an alternative to that sort of precautionary principle-driven mode of AI regulation.",
         "US shows alternative to EU precaution",
         "schriftlich",
         "https://venturebeat.com/ai/ai-weekly-u-s-and-european-governments-strike-contrasting-tones-on-ai/",
         "U.S. and EU strike contrasting tones on AI regulatory policy",
         "2025-09-01",
         "en",
         "US vs EU AI regulation philosophy"
        ),

        # 11. State regulations anti-innovation
        (PERSON_ID,
         "A patchwork of state regulations is anti-innovation. It actually presents and gives more power to large technology companies that have armies of lawyers.",
         "State AI laws favor big tech",
         "schriftlich",
         "https://www.scientificamerican.com/article/kratsios-calls-patchwork-state-ai-laws-anti-innovation-at-house-science-ai/",
         "Kratsios Calls Patchwork State AI Laws 'Anti-Innovation'",
         "2025-09-01",
         "en",
         "House Science Committee AI hearing"
        ),

        # 12. Manipulate time and space
        (PERSON_ID,
         "Our technologies permit us to manipulate time and space. They leave distance annihilated, cause things to grow, and improve productivity.",
         "Technologies manipulate time and space",
         "schriftlich",
         "https://www.whitehouse.gov/articles/2025/04/remarks-by-director-kratsios-at-the-endless-frontiers-retreat/",
         "Remarks by Director Kratsios at the Endless Frontiers Retreat",
         "2025-04-15",
         "en",
         "Speech on American technological capabilities"
        ),

        # 13. Regulatory barriers to supersonic
        (PERSON_ID,
         "The chief barrier to pushing the envelope again in transportation, whether supersonic aircraft or high-speed rail and flying cars, has been a regulatory regime opposed to innovation and development.",
         "Regulations block supersonic innovation",
         "schriftlich",
         "https://www.whitehouse.gov/articles/2025/04/remarks-by-director-kratsios-at-the-endless-frontiers-retreat/",
         "Remarks by Director Kratsios at the Endless Frontiers Retreat",
         "2025-04-15",
         "en",
         "On regulatory barriers to transportation innovation"
        ),

        # 14. Bad regulations burden
        (PERSON_ID,
         "Throw off the burden of bad regulations that weigh down our innovators, and use federal resources to test, to deploy, and to mature emerging technologies.",
         "Remove bad regulations weighing innovators",
         "schriftlich",
         "https://www.whitehouse.gov/articles/2025/04/remarks-by-director-kratsios-at-the-endless-frontiers-retreat/",
         "Remarks by Director Kratsios at the Endless Frontiers Retreat",
         "2025-04-15",
         "en",
         "Call for deregulation and federal support"
        ),

        # 15. National AI Initiative Office
        (PERSON_ID,
         "The National Artificial Intelligence Initiative Office will be integral to the Federal government's AI efforts for many years to come, serving as a central hub for national AI research and policy for the entire US innovation ecosystem.",
         "AI Initiative Office central hub",
         "schriftlich",
         "https://govciomedia.com/kratsios-brings-ai-5g-future-tech-to-ostp-forefront/",
         "Kratsios Brings AI, 5G, Future Tech to OSTP Forefront",
         "2020-01-01",
         "en",
         "Announcement of National AI Initiative Office establishment"
        ),

        # 16. Data center energy strategy
        (PERSON_ID,
         "That's something that we're pushing a lot of the folks in the big data center companies to work on.",
         "Push data centers to build own energy",
         "schriftlich",
         "https://meridian.org/project/conversation-with-ostp-director-michael-kratsios/",
         "Conversation with OSTP Director Michael Kratsios",
         "2025-11-01",
         "en",
         "Encouraging data center companies to build own energy supplies"
        ),

        # 17. Federal resources for AI future
        (PERSON_ID,
         "The Trump Administration will unleash Federal resources to build out the data resources needed for an AI-powered future.",
         "Unleash federal resources for AI",
         "schriftlich",
         "https://www.energy.gov/articles/doe-identifies-16-federal-sites-across-country-data-center-and-ai-infrastructure",
         "DOE Identifies 16 Federal Sites for Data Center Development",
         "2025-04-01",
         "en",
         "On federal infrastructure for AI development"
        ),

        # 18. OECD AI Principles historic
        (PERSON_ID,
         "The Trump Administration made history by joining together with democracies in the world that share our common values when we signed an international consensus document on AI Principles at the OECD in Paris.",
         "OECD AI Principles historic achievement",
         "schriftlich",
         "https://datainnovation.org/2019/09/remarks-by-michael-kratsios-u-s-cto-at-center-for-data-innovation-forum-on-ai/",
         "Remarks By Michael Kratsios at Center for Data Innovation Forum on AI",
         "2019-09-01",
         "en",
         "Discussion of first international AI policy guidelines"
        ),

        # 19. Promote and protect strategy
        (PERSON_ID,
         "President Trump's 'promote and protect' strategy for artificial intelligence is based on expanding the use of export controls while reforming them to better allow friends and allies to acquire U.S. technologies.",
         "Promote and protect AI strategy",
         "schriftlich",
         "https://insidetrade.com/trade/white-house-science-chief-promote-and-protect-strategy-must-advance-ai-exports",
         "White House science chief: 'Promote and protect' strategy must advance AI exports",
         "2025-07-01",
         "en",
         "Dual approach to AI export policy"
        ),

        # 20. Highest end semiconductors export control
        (PERSON_ID,
         "The highest end of semiconductors need to continue to be export controlled, not allowed into China, and that's important for our ability to maintain our leadership in this race.",
         "Block high-end chips to China",
         "schriftlich",
         "https://www.kharon.com/brief/trump-ai-policy-michael-kratsios-csis",
         "White House's AI Policy Chief: Expect Sharper Controls",
         "2025-08-01",
         "en",
         "On semiconductor export controls to China"
        ),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # HANDLUNGEN (Actions)
    handlungen = [
        # 1. Thiel Capital employment
        (PERSON_ID,
         "einstellung",
         "Joined Thiel Capital as principal and served as chief of staff to Peter Thiel before entering Trump administration",
         "2010-01-01",
         "https://www.michaelkratsios.com/bio",
         "Michael Kratsios Bio",
         "Early career at venture capital firm of billionaire Peter Thiel"
        ),

        # 2. White House CTO appointment
        (PERSON_ID,
         "einstellung",
         "Appointed as Deputy Assistant to the President for Technology Policy, later became 4th US Chief Technology Officer",
         "2017-01-20",
         "https://trumpwhitehouse.archives.gov/people/michael-kratsios/",
         "Michael Kratsios – The White House",
         "First Trump administration appointment"
        ),

        # 3. American AI Initiative creation
        (PERSON_ID,
         "produktlaunch",
         "Architected the American AI Initiative, the nation's first comprehensive AI strategy",
         "2019-02-11",
         "https://www.michaelkratsios.com/bio",
         "Michael Kratsios Bio",
         "Executive order establishing national AI strategy"
        ),

        # 4. OECD AI Principles negotiation
        (PERSON_ID,
         "politisch",
         "Led U.S. efforts to develop world's first intergovernmental AI policy guidelines at OECD in Paris",
         "2019-05-22",
         "https://www.technologyreview.com/2019/05/22/135238/america-and-its-economic-allies-announce-a-democratic-vision-for-ai/",
         "America and its economic allies announce democratic vision for AI",
         "First international consensus on AI principles"
        ),

        # 5. Senate confirmation as CTO
        (PERSON_ID,
         "politisch",
         "Unanimously confirmed by U.S. Senate as Chief Technology Officer of the United States",
         "2019-08-01",
         "https://en.wikipedia.org/wiki/Michael_Kratsios",
         "Michael Kratsios - Wikipedia",
         "Became 4th US CTO with bipartisan support"
        ),

        # 6. National AI Initiative Office establishment
        (PERSON_ID,
         "gruendung",
         "Established the National AI Initiative Office at the White House as central hub for AI research and policy",
         "2020-01-01",
         "https://govciomedia.com/kratsios-brings-ai-5g-future-tech-to-ostp-forefront/",
         "Kratsios Brings AI, 5G, Future Tech to OSTP Forefront",
         "Implementation of bipartisan National AI Initiative Act"
        ),

        # 7. Pentagon Acting Under Secretary appointment
        (PERSON_ID,
         "einstellung",
         "Appointed Acting Under Secretary of Defense for Research and Engineering, 3rd highest Pentagon official",
         "2020-07-10",
         "https://www.war.gov/News/Releases/Release/Article/2271633/dod-names-acting-under-secretary-of-defense-for-research-and-engineering/",
         "DOD Names Acting Under Secretary of Defense for Research and Engineering",
         "Oversaw $100+ billion DOD R&D portfolio at age 33"
        ),

        # 8. Quantum research institutes funding
        (PERSON_ID,
         "investition",
         "Spearheaded $1 billion program creating network of AI and quantum research institutes across US",
         "2020-08-01",
         "https://www.energy.gov/articles/white-house-office-technology-policy-national-science-foundation-and-department-energy",
         "White House announces $1B for AI, quantum research hubs",
         "Established multiple National Quantum Initiative research centers"
        ),

        # 9. Scale AI appointment
        (PERSON_ID,
         "einstellung",
         "Joined Scale AI as Managing Director and Head of Strategy after leaving Pentagon",
         "2021-03-01",
         "https://www.linkedin.com/posts/michaelkratsios_scale-ai-hires-former-us-cto-michael-kratsios-activity-6803838565659762690-Mvo_",
         "Scale AI Hires Former U.S. CTO Michael Kratsios",
         "Moved to AI data infrastructure company after government service"
        ),

        # 10. Foundation for American Innovation board
        (PERSON_ID,
         "einstellung",
         "Joined Foundation for American Innovation board as new member",
         "2023-05-01",
         "https://www.thefai.org/posts/quarterly-activities-update-2023-Q2",
         "Quarterly Activities Update Q2 2023 - Foundation for American Innovation",
         "Joined tech policy advocacy organization board"
        ),

        # 11. Trump 2024 transition team
        (PERSON_ID,
         "einstellung",
         "Named to Trump White House transition team while at Scale AI",
         "2024-11-01",
         "https://www.inc.com/sam-blum/scale-ai-exec-michael-kratsios-to-rejoin-trump-white-house-as-part-of-transition-team/91017910",
         "Scale AI Exec Michael Kratsios to Rejoin Trump White House",
         "Rejoined Trump administration planning efforts"
        ),

        # 12. OSTP Director nomination
        (PERSON_ID,
         "politisch",
         "Nominated by President-elect Trump as Director of Office of Science and Technology Policy",
         "2024-12-22",
         "https://www.techpolicy.press/michael-kratsios-nomination-to-direct-ostp-sent-to-us-senate/",
         "Michael Kratsios Nomination to Direct OSTP Sent to US Senate",
         "Nominated as 13th OSTP Director and Science Advisor to President"
        ),

        # 13. OSTP Director confirmation
        (PERSON_ID,
         "politisch",
         "Confirmed by U.S. Senate as OSTP Director in 74-25 vote, youngest person ever in role",
         "2025-03-25",
         "https://www.nextgov.com/people/2025/03/senate-confirms-michael-kratsios-lead-white-house-tech-office/404059/",
         "Senate confirms Michael Kratsios to lead White House tech office",
         "First millennial to serve as OSTP Director"
        ),

        # 14. Federal data center sites announcement
        (PERSON_ID,
         "politisch",
         "Led DOE identification of 16 federal sites for rapid AI data center construction",
         "2025-04-09",
         "https://www.energy.gov/articles/doe-identifies-16-federal-sites-across-country-data-center-and-ai-infrastructure",
         "DOE Identifies 16 Federal Sites for Data Center Development",
         "Infrastructure push for AI-powered future"
        ),

        # 15. Davos AI policy promotion
        (PERSON_ID,
         "lobbying",
         "Promoted Trump's light-touch AI approach and criticized EU AI Act at World Economic Forum Davos",
         "2025-01-20",
         "https://www.nbcnews.com/tech/tech-news/kratsios-heads-davos-sell-trumps-light-touch-ai-approach-rcna254497",
         "Kratsios heads to Davos to sell Trump's light-touch AI approach",
         "International advocacy for US AI regulatory model"
        ),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    conn.commit()

    # Count inserted records
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    handlungen_count = cursor.fetchone()[0]

    conn.close()

    return aussagen_count, handlungen_count

if __name__ == "__main__":
    print("Starting data insertion for Michael Kratsios (person_id=100)...")
    print(f"Database: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print("-" * 80)

    aussagen_count, handlungen_count = insert_data()

    print(f"\n{'='*80}")
    print(f"DATA INSERTION COMPLETED SUCCESSFULLY")
    print(f"{'='*80}")
    print(f"Total Aussagen (Statements) inserted: {aussagen_count}")
    print(f"Total Handlungen (Actions) inserted:  {handlungen_count}")
    print(f"{'='*80}")
    print(f"\nAll data for Michael Kratsios has been successfully added to the database.")
