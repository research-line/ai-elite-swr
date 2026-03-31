#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trae Stephens (person_id=98) - Datensammlung
Founders Fund Partner, Anduril Co-Founder, ex-Palantir
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 98

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (18 Stück)
    aussagen = [
        # Ethics & Defense Technology
        (PERSON_ID,
         "History has shown that those who lead in new technologies of defense will set the ethical norms and standards that govern those technologies. Those who lead from behind will be subject to those norms.",
         "Tech leaders set ethical norms",
         "schriftlich",
         "https://medium.com/@traestephens/the-ethics-of-defense-technology-development-an-investors-perspective-45c71bf6e6af",
         "The Ethics of Defense Technology Development: An Investor's Perspective",
         None,
         "en",
         "Medium article on defense ethics"),

        (PERSON_ID,
         "I believe deeply in liberal democratic governance and the values that form its foundation. In the national security sector, it is critical for the United States and her allies to set ethical norms and assert a moral high ground, and in order to do that, we must first hold the technological high ground.",
         "US must hold technological high ground",
         "schriftlich",
         "https://medium.com/@traestephens/the-ethics-of-defense-technology-development-an-investors-perspective-45c71bf6e6af",
         "The Ethics of Defense Technology Development",
         None,
         "en",
         "On democratic values and tech leadership"),

        # Anduril & Defense Tech Evolution
        (PERSON_ID,
         "When we started Anduril in 2017, there was a lot of bad press. It was not popular. There was a lot of being dragged through the mud on things that either weren't true or were a misunderstanding of what it is that we were doing. But in 2024, I mean, it's a meme category. Like everybody wants to work in defense tech, which is amazing.",
         "Defense tech went from taboo to popular",
         "muendlich",
         "https://aletteraday.substack.com/p/letter-199-trae-stephens-2024",
         "Letter #199: Trae Stephens (2024)",
         "2024-01-01",
         "en",
         "Kevin Gee interview 2024"),

        (PERSON_ID,
         "The important thing is to be principled, to have conviction, moral conviction, around the thing that it is you're doing. And get smart on why you have that moral conviction. And as long as you have that conviction, and you're not on an island, like you have people around you that are willing to dive into this exploration with you, stay firm.",
         "Stay firm with moral conviction",
         "muendlich",
         "https://aletteraday.substack.com/p/letter-199-trae-stephens-2024",
         "Letter #199: Trae Stephens (2024)",
         "2024-01-01",
         "en",
         "On principled entrepreneurship"),

        (PERSON_ID,
         "The threat that we're facing globally is very different than it was in 2000 through 2020. It looks now more like a Cold War conflict against near-peer adversaries.",
         "We face Cold War-like near-peer threat",
         "muendlich",
         "https://techcrunch.com/2024/03/02/vc-trae-stephens-says-he-has-a-bunker-and-much-more-in-talk-about-founders-fund-and-anduril/",
         "TechCrunch StrictlyVC Interview",
         "2024-03-02",
         "en",
         "On geopolitical threat environment"),

        # Ukraine & Munitions
        (PERSON_ID,
         "If the U.S. got into a hot conflict with a great power, we would run out of munitions in a week. You see situations like Ukraine where we deplete not only available inventory, we also deplete our own inventory.",
         "US would run out of munitions in a week",
         "muendlich",
         "https://www.zerohedge.com/military/anduril-co-founder-warns-us-munitions-stockpile-would-last-one-week-hot-conflict",
         "Anduril Co-Founder Warns: U.S. Munitions Stockpile",
         "2025-04-01",
         "en",
         "Warning about defense preparedness"),

        # Bunker & Preparedness
        (PERSON_ID,
         "It might not hurt to have some shotguns.",
         "Good to have shotguns in survival kit",
         "muendlich",
         "https://techcrunch.com/2024/03/02/vc-trae-stephens-says-he-has-a-bunker-and-much-more-in-talk-about-founders-fund-and-anduril/",
         "VC Trae Stephens says he has a bunker",
         "2024-03-02",
         "en",
         "On bunker preparations and survival kit"),

        # Faith & Technology
        (PERSON_ID,
         "God is the original innovator and humans, made in God's image, are meant to build things, and that it is excessive pride, not building, that God punishes.",
         "God made humans to build things",
         "schriftlich",
         "https://www.aaronrenn.com/p/christianity-and-tech",
         "Is Christianity the New Religion of Silicon Valley?",
         None,
         "en",
         "Moral Code series on faith and tech"),

        (PERSON_ID,
         "Science alone is insufficient to provide a framework for ethical living, and the values held by secular humanists were developed within and shaped by the Judeo-Christian tradition.",
         "Science insufficient for ethics framework",
         "schriftlich",
         "https://digidai.github.io/2025/11/27/trae-stephens-founders-fund-anduril-defense-tech-billionaire-deep-analysis/",
         "Trae Stephens and Founders Fund Analysis",
         None,
         "en",
         "On ethics and religious foundations"),

        # Government & Technology Philosophy
        (PERSON_ID,
         "Building the easy button for the government - creating products that genuinely make government operations more effective rather than forcing government agencies to adapt to commercial paradigms.",
         "Build easy button for government",
         "schriftlich",
         "https://digidai.github.io/2025/11/27/trae-stephens-founders-fund-anduril-defense-tech-billionaire-deep-analysis/",
         "Trae Stephens Philosophy Analysis",
         None,
         "en",
         "Core philosophy on gov tech from Palantir experience"),

        # Tech & Harm
        (PERSON_ID,
         "Tech can be used for both good and bad. It's cliche because it's true.",
         "Tech for both good and bad",
         "muendlich",
         "https://faithdriveninvestor.org/bios/trae-stephens/",
         "Faith Driven Investor Bio",
         None,
         "en",
         "On technology and moral responsibility"),

        # Just War & Precision
        (PERSON_ID,
         "Where use of force is necessary, Just War principles require it be deployed ethically and consistently with principles of discrimination and proportionality. Technology has the potential to lead to significant reduction in innocent life loss through highly precise and targeted attacks, reducing the need for massive indiscriminate strikes.",
         "Tech enables more ethical warfare",
         "schriftlich",
         "https://medium.com/@traestephens/the-ethics-of-defense-technology-development-an-investors-perspective-45c71bf6e6af",
         "Ethics of Defense Technology Development",
         None,
         "en",
         "On Just War theory and technology"),

        (PERSON_ID,
         "Modern technology, if developed properly, can make warfare more proportional, precise, and less indiscriminate than ever before, representing ethical goods that result in better and more peaceful outcomes globally.",
         "Modern tech makes warfare more ethical",
         "schriftlich",
         "https://medium.com/@traestephens/the-ethics-of-defense-technology-development-an-investors-perspective-45c71bf6e6af",
         "Ethics of Defense Technology Development",
         None,
         "en",
         "On technology improving warfare ethics"),

        # Democratically-Elected Governments
        (PERSON_ID,
         "It is critical that democratically-elected governments with a firm respect for Just War frameworks be the leaders in the development of these technologies.",
         "Democratic governments must lead tech",
         "schriftlich",
         "https://medium.com/@traestephens/the-ethics-of-defense-technology-development-an-investors-perspective-45c71bf6e6af",
         "Ethics of Defense Technology Development",
         None,
         "en",
         "On who should develop defense AI"),

        # 9/11 Inspiration
        (PERSON_ID,
         "I was a senior in high school on 9/11 and was inspired to pursue a career in national security.",
         "9/11 inspired national security career",
         "schriftlich",
         "https://mostlyhuman.com/why-9-11-inspired-trae-stephens-to-work-on-the-future-of-defense-tech/",
         "Why 9/11 Inspired Trae Stephens",
         None,
         "en",
         "Career motivation origin"),

        # Forgiveness & Silicon Valley
        (PERSON_ID,
         "Forgiveness is a surprisingly useful concept in Silicon Valley, where relationships matter and holding grudges limits opportunities.",
         "Forgiveness useful in Silicon Valley",
         "schriftlich",
         "https://medium.com/@traestephens/forgiveness-and-silicon-valley-the-surprising-utility-of-forgiveness-1007a941c335",
         "Forgiveness and Silicon Valley: The Surprising Utility of Forgiveness",
         None,
         "en",
         "Medium article on Christian ethics in tech"),

        # Good Quests
        (PERSON_ID,
         "My primary ethical concern about tech is not innovation itself, but whether people are pursuing good quests - asking if they're actually making the world a better place or pursuing selfish ambition.",
         "Pursue good quests not selfish ambition",
         "muendlich",
         "https://faithdriveninvestor.org/bios/trae-stephens/",
         "Faith Driven Investor Profile",
         None,
         "en",
         "On ethical framework for tech work"),

        # ACTS 17 Goal
        (PERSON_ID,
         "Our goal with ACTS 17 Collective is not necessarily conversion, but rather encouraging the high intellectuals of our time to consider incorporating faith into their lives.",
         "Encourage tech elites to consider faith",
         "muendlich",
         "https://www.denisonforum.org/daily-article/the-acts-17-collective-is-introducing-tech-leaders-to-jesus/",
         "The ACTS 17 Collective is introducing tech leaders to Jesus",
         None,
         "en",
         "On ministry to Silicon Valley elites"),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # HANDLUNGEN (13 Stück)
    handlungen = [
        # Gründungen
        (PERSON_ID,
         "gruendung",
         "Co-founded Anduril Industries with Palmer Luckey, Matt Grimm, Joe Chen, and Brian Schimpf, focusing on autonomous defense systems and AI-powered surveillance",
         "2017-06-01",
         "https://en.wikipedia.org/wiki/Anduril_Industries",
         "Anduril Industries Wikipedia",
         "Incorporated June 2017, seeded by Founders Fund"),

        (PERSON_ID,
         "gruendung",
         "Co-founded Sol (Sindarin Inc.) with Ben Chelf, developing next-generation wearable e-reader device incubated by Founders Fund",
         "2021-01-01",
         "https://en.wikipedia.org/wiki/Trae_Stephens",
         "Trae Stephens Wikipedia",
         "Consumer tech venture, $350 wearable e-reader"),

        (PERSON_ID,
         "gruendung",
         "Co-founded Valinor Enterprises with Julie Bush (CEO), Paul Kwan, and Grant Verstandig as defense-tech company incubator",
         "2024-01-01",
         "https://www.axios.com/2025/10/15/valinor-harbor-bush-stephens-kwan",
         "Valinor wants to build defense-tech picks and shovels",
         "Launched 10 product companies in first year"),

        (PERSON_ID,
         "gruendung",
         "Co-founded Pursuit Properties, offering turnkey co-ownership and management of recreational ranches and legacy-building properties",
         None,
         "https://pursuit-properties.com/team",
         "Pursuit Properties Team",
         "Small ownership groups (10 or fewer) for world-class ranches"),

        (PERSON_ID,
         "gruendung",
         "Co-founded ACTS 17 Collective with wife Michelle Stephens to minister to Silicon Valley elites and tech industry leaders",
         None,
         "https://www.denisonforum.org/daily-article/the-acts-17-collective-is-introducing-tech-leaders-to-jesus/",
         "ACTS 17 Collective introducing tech leaders to Jesus",
         "Christian nonprofit engaging tech elite"),

        # Investitionen & Karriere
        (PERSON_ID,
         "einstellung",
         "Became Partner at Founders Fund, focusing on startups in government and defense technology sectors",
         "2014-01-01",
         "https://foundersfund.com/team/trae-stephens/",
         "Founders Fund - Trae Stephens",
         "Previously joined FF in 2013, promoted to Partner 2014"),

        (PERSON_ID,
         "einstellung",
         "Joined Palantir Technologies as early employee, led teams for defense/intelligence expansion, international growth, and product development",
         "2008-01-01",
         "https://en.wikipedia.org/wiki/Trae_Stephens",
         "Trae Stephens Wikipedia",
         "One of early employees, designed analytical software"),

        (PERSON_ID,
         "investition",
         "Founders Fund led Anduril Series G funding round with $1 billion investment at $30.5 billion valuation, doubling prior valuation",
         "2025-06-05",
         "https://www.cnbc.com/2025/06/05/anduril-valuation-founders-fund.html",
         "Anduril raises funding at $30.5 billion valuation",
         "Largest check Founders Fund ever written, 8x oversubscribed"),

        (PERSON_ID,
         "investition",
         "Led $8 million seed round for Hydra Host through Founders Fund with Joe Lonsdale participating",
         None,
         "https://www.newcomer.co/p/the-investor-who-called-defense-techs",
         "The Investor Who Called Defense Tech's Big Moment",
         "Defense infrastructure investment"),

        # Politische Handlungen
        (PERSON_ID,
         "politisch",
         "Led Department of Defense transition team for President-elect Donald Trump, screening staff and shaping policies",
         "2016-11-23",
         "https://executivegov.com/2016/11/donald-trumps-defense-transition-team-taps-trae-stephens/",
         "Donald Trump's Defense Transition Team Taps Trae Stephens",
         "Did not take position in administration, policy role only"),

        (PERSON_ID,
         "politisch",
         "Consulted with President-elect Trump on revamping US military, considered for Deputy Secretary of Defense position",
         "2024-11-15",
         "https://fortune.com/2024/11/16/anduril-chairman-trae-stephens-donald-trump-us-military-reform-defense-spending/",
         "Anduril's chair consulted with Trump on revamping US military",
         "Trump transition 2024, highlighting Thiel influence"),

        # Verträge & Geschäft
        (PERSON_ID,
         "verkauf",
         "Anduril awarded $6+ billion in Trump border security legislation for virtual wall surveillance tower expansion",
         "2025-07-04",
         "https://theintercept.com/2025/07/09/trump-big-beautiful-bill-anduril/",
         "Trump's Big Beautiful Gift to Anduril",
         "Legislation signed July 4, massive border surveillance expansion"),

        (PERSON_ID,
         "produktlaunch",
         "Anduril announced Arsenal Projects, hyperscale computing facilities for manufacturing autonomous weapons faster than near-peer rivals",
         "2025-01-01",
         "https://en.wikipedia.org/wiki/Trae_Stephens",
         "Trae Stephens Wikipedia",
         "Strategic manufacturing initiative for autonomous systems"),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    conn.commit()
    conn.close()

    print(f"Erfolgreich eingefügt:")
    print(f"  - {len(aussagen)} Aussagen")
    print(f"  - {len(handlungen)} Handlungen")
    print(f"  - Gesamt: {len(aussagen) + len(handlungen)} Einträge")
    print(f"\nPerson ID: {PERSON_ID} (Trae Stephens)")

if __name__ == "__main__":
    insert_data()
