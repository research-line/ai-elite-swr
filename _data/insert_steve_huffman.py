#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dateneinfügung für Steve Huffman (person_id=94)
Reddit CEO/Co-Founder
Weltbilder zu KI, Silicon Valley, Technologie
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN
    aussagen = [
        # AI & Technology Worldview
        (94, "You can't have artificial intelligence without actual intelligence.",
         "AI braucht menschliche Intelligenz", "muendlich",
         "https://www.benzinga.com/markets/tech/25/08/46783436/reddit-ceo-steve-huffman-says-ai-learns-from-us-doesnt-invent-knowledge-cant-have-artificial-intelligence-without-actual-intelligence",
         "Reddit CEO Steve Huffman Says AI Learns From Us", "2025-08-01", "en",
         "Q2 earnings call 2025, discussing AI's dependence on human knowledge"),

        (94, "The paradox I see is that, as more content on the internet is written by machines, there's an increasing premium on content that comes from real people.",
         "Menschliche Inhalte werden wertvoller", "schriftlich",
         "https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php",
         "Reddit Is Winning the AI Game", "2024-03-01", "en",
         "Company earnings call discussing AI data licensing strategy"),

        (94, "Reddit is the most human place on the internet.",
         "Reddit ist der menschlichste Ort im Internet", "schriftlich",
         "https://www.webpronews.com/reddits-billion-dollar-bet-why-steve-huffman-thinks-being-the-most-human-place-on-the-internet-is-the-ultimate-competitive-advantage-in-the-age-of-ai-slop/",
         "Reddit's Billion-Dollar Bet", "2025-01-01", "en",
         "Positioning Reddit against AI-generated content ('AI slop')"),

        # Prepper/Survival Worldview
        (94, "If the world ends — and not even if the world ends, but if we have trouble — getting contacts or glasses is going to be a huge pain in the ass.",
         "Laser-OP für Apokalypse-Vorbereitung", "schriftlich",
         "https://www.cnbc.com/2017/01/25/the-super-rich-are-preparing-for-the-end-of-the-world.html",
         "The super rich are preparing for the end of the world", "2017-01-25", "en",
         "Explaining why he got laser eye surgery as apocalypse preparation"),

        (94, "I think, to some degree, we all collectively take it on faith that our country works, that our currency is valuable, the peaceful transfer of power—that all of these things that we hold dear work because we believe they work. While I do believe they're quite resilient, and we've been through a lot, certainly we're going to go through a lot more.",
         "Gesellschaft basiert auf fragilem Konsens", "schriftlich",
         "https://www.cnbc.com/2017/01/25/the-super-rich-are-preparing-for-the-end-of-the-world.html",
         "The super rich are preparing for the end of the world", "2017-01-25", "en",
         "Discussing concerns about American political stability"),

        (94, "I need to own a motorcycle because everybody else is screwed.",
         "Motorrad für Katastrophenfall", "schriftlich",
         "https://www.inc.com/bartie-scott/how-silicon-valley-super-rich-are-preparing-for-doomsda.html",
         "How Silicon Valley's Super Rich Are Getting Ready for 'Doomsday'", "2017-01-01", "en",
         "Inspired by 'Deep Impact' scene of escaping through stalled traffic"),

        # Free Speech & Moderation
        (94, "Neither Alexis nor I created Reddit to be a bastion of free speech, but rather as a place where open and honest discussion can happen.",
         "Reddit nicht für absolute Redefreiheit geschaffen", "schriftlich",
         "https://officialbespoke.co/reddit-steve-huffman/",
         "We Asked Steve Huffman if it's Possible to Save the Platform", "2018-01-01", "en",
         "Clarifying Reddit's purpose regarding free speech"),

        (94, "Reddit is a place for open and honest conversations—'open and honest' meaning authentic, meaning messy, meaning the best and worst and realest and weirdest parts of humanity.",
         "Reddit für authentische Gespräche", "schriftlich",
         "https://officialbespoke.co/reddit-steve-huffman/",
         "We Asked Steve Huffman if it's Possible to Save the Platform", "2018-01-01", "en",
         "2018 statement on Reddit's commitment to free expression"),

        (94, "We are not the thought police … but we do care about how you behave.",
         "Keine Gedankenpolizei, aber Verhaltensregeln", "schriftlich",
         "https://www.marketplace.org/story/2018/07/02/ceo-reddit-we-are-not-thought-police-we-don-t-want-control-what-you-believe-we",
         "The CEO of Reddit: 'We are not the thought police'", "2018-07-02", "en",
         "Interview on content moderation philosophy"),

        # Democracy & Governance
        (94, "The people who get there first get to stay there and pass it down to their descendants, and that is not democratic.",
         "Moderatoren wie 'landed gentry'", "schriftlich",
         "https://gizmodo.com/reddit-ceo-steve-huffman-moderators-landed-gentry-1850546737",
         "Reddit CEO Flames Protesting Moderators", "2023-06-15", "en",
         "Criticizing moderator system during API protest, calling it undemocratic"),

        (94, "What I'm suggesting as a pathway out is actually more democracy. We've got some old, legacy decisions on how communities are run that we need to kind of work our way out of.",
         "Mehr Demokratie für Reddit-Communities", "schriftlich",
         "https://www.nbcnews.com/tech/tech-news/reddit-protest-blackout-ceo-steve-huffman-moderators-rcna89544",
         "Reddit CEO slams protesters", "2023-06-01", "en",
         "Discussing changes to moderator governance during 2023 protests"),

        # API Controversy
        (94, "Reddit was never designed to support third-party apps.",
         "Reddit nicht für Drittanbieter-Apps designed", "schriftlich",
         "https://tech.slashdot.org/story/23/06/15/2252235/reddit-ceo-steve-huffman-reddit-was-never-designed-to-support-third-party-apps",
         "Reddit CEO Steve Huffman on Third-Party Apps", "2023-06-15", "en",
         "Defending API pricing changes that killed third-party apps"),

        # WallStreetBets & Meme Stocks
        (94, "WallStreetBets may look sophomoric or chaotic from the outside, but the fact that we are here today means they've managed to raise important issues about fairness and opportunity in our financial system.",
         "WallStreetBets zeigt Fairness-Probleme", "schriftlich",
         "https://www.cnbc.com/2021/02/18/reddit-ceo-steve-huffman-defends-platforms-role-in-gamestop-surge.html",
         "Reddit CEO defends platform's role in GameStop surge", "2021-02-18", "en",
         "Testimony before House Financial Services Committee"),

        (94, "WallStreetBets is first and foremost a real community. The self-deprecating jokes, the memes, the crass-at-times language, all reflect this.",
         "WallStreetBets ist echte Community", "schriftlich",
         "https://www.shacknews.com/article/122839/wallstreetbets-was-well-within-normal-parameters-says-reddit-ceo-steve-huffman",
         "WallStreetBets was well within normal parameters", "2021-02-18", "en",
         "Defending WallStreetBets during GameStop congressional hearing"),

        (94, "First of all, I love wallstreetbets. I'm a user, I've seen their comments over the last couple of weeks so I just send them my regards.",
         "Ich liebe WallStreetBets", "schriftlich",
         "https://fortune.com/2024/03/22/reddit-ipo-share-price-steve-huffman-wallstreetbets/",
         "Reddit CEO says he loves 'meme stock'", "2024-03-21", "en",
         "On Reddit IPO day, revealing his membership in WallStreetBets"),

        # Product Philosophy
        (94, "If I like it, there are millions of people just like me so they'll also like it.",
         "Produktphilosophie: Was ich mag, mögen Millionen", "schriftlich",
         "https://www.fastcompany.com/90997770/reddit-steve-huffman-interview-ai-ipo-2024",
         "CEO Steve Huffman on Reddit's essential humanity", "2024-01-01", "en",
         "Explaining his product development philosophy"),

        # Comment Edit Controversy
        (94, "As the CEO, I shouldn't play such games, and it's all fixed now.",
         "CEO sollte solche Spiele nicht spielen", "schriftlich",
         "https://www.cnbc.com/2016/11/24/reddits-ceo-edited-comments-that-criticized-him.html",
         "Reddit's CEO edited comments that criticized him", "2016-11-24", "en",
         "Apologizing for secretly editing user comments criticizing him"),

        # 2014 Regret about Selling
        (94, "I wish I still owned Reddit now.",
         "Verkauf war ein Fehler", "schriftlich",
         "https://mixergy.com/interviews/steve-huffman-reddit-interview/",
         "Reddit Founder: 'I Wish I Still Owned Reddit Now'", "2014-01-01", "en",
         "Regretting 2006 sale to Condé Nast, site exceeded expectations"),

        # Burning Man Influence
        (94, "Happy to help others, but not wanting to require others.",
         "Burning Man 'radical self-reliance'", "schriftlich",
         "https://www.cnbc.com/2017/01/25/the-super-rich-are-preparing-for-the-end-of-the-world.html",
         "The super rich are preparing for the end of the world", "2017-01-25", "en",
         "Describing his interpretation of 'radical self-reliance' from Burning Man"),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)

    # HANDLUNGEN
    handlungen = [
        # Founding & Early History
        (94, "gruendung", "Co-founded Reddit with Alexis Ohanian after Y Combinator acceptance, programmed entire site in Lisp in 20 days",
         "2005-06-01", "https://en.wikipedia.org/wiki/Steve_Huffman",
         "Steve Huffman - Wikipedia",
         "Y Combinator's first class, $12,000 grant, launched in June 2005"),

        (94, "verkauf", "Sold Reddit to Condé Nast for reported $10-20 million at age 23",
         "2006-10-31", "https://techcrunch.com/2006/10/31/breaking-news-conde-nastwired-acquires-reddit/",
         "Breaking News: Condé Nast/Wired Acquires Reddit",
         "Acquisition completed October 31, 2006, later regretted the sale"),

        (94, "ruecktritt", "Left Reddit as acting CEO after Condé Nast acquisition",
         "2009-01-01", "https://en.wikipedia.org/wiki/Steve_Huffman",
         "Steve Huffman - Wikipedia",
         "Departed in 2009 to pursue other ventures"),

        (94, "gruendung", "Co-founded Hipmunk travel search startup with Adam Goldstein as CTO",
         "2010-08-01", "https://www.ycombinator.com/companies/hipmunk",
         "Hipmunk: Y Combinator",
         "Y Combinator-funded startup launched August 2010, focused on 'agony reduction' in flight search"),

        (94, "einstellung", "Returned to Reddit as CEO, replacing Ellen Pao after moderator revolt",
         "2015-07-10", "https://time.com/3953655/reddit-ellen-pao/",
         "Reddit CEO Ellen Pao Is Leaving, Steve Huffman Replacing Her",
         "Returned after Ellen Pao's controversial tenure and Victoria Taylor firing protests"),

        (94, "sonstiges", "Secretly edited user comments criticizing him (u/spez) on r/The_Donald, replacing his username with moderator names",
         "2016-11-23", "https://techcrunch.com/2016/11/23/reddit-huffman-trump/",
         "Reddit CEO admits he secretly edited comments from Donald Trump supporters",
         "Controversial use of admin powers during Pizzagate controversy, later apologized"),

        (94, "sonstiges", "Testified before House Financial Services Committee defending WallStreetBets during GameStop meme stock surge",
         "2021-02-18", "https://www.cnbc.com/2021/02/18/reddit-ceo-steve-huffman-defends-platforms-role-in-gamestop-surge.html",
         "Reddit CEO defends platform's role in GameStop surge",
         "Called WallStreetBets activity 'culture war of Wall Street versus everybody else'"),

        (94, "umstrukturierung", "Announced major API pricing changes requiring third-party apps to pay for access",
         "2023-04-01", "https://en.wikipedia.org/wiki/2023_Reddit_API_controversy",
         "Reddit API controversy - Wikipedia",
         "Pricing forced closure of Apollo, Sync, BaconReader, RIF; led to 8,500+ subreddit blackout protest"),

        (94, "sonstiges", "Implemented API changes despite massive protest, killing major third-party apps",
         "2023-06-30", "https://en.wikipedia.org/wiki/2023_Reddit_API_controversy",
         "Reddit API controversy - Wikipedia",
         "Changes went into effect June 30, 2023, shutting down Apollo and other popular apps"),

        (94, "partnerschaft", "Signed data licensing deal with Google worth $60 million per year for AI training",
         "2024-02-01", "https://www.universityherald.com/articles/79929/20251031/reddit-ceo-speaks-out-protecting-user-data-reveals-60m-google-deal.htm",
         "Reddit CEO reveals $60M Google Deal",
         "Gave Google access to real-time Reddit content for AI model training"),

        (94, "produktlaunch", "Led Reddit's Initial Public Offering (IPO) at $34 per share",
         "2024-03-21", "https://finance.yahoo.com/news/reddit-ipo-the-company-is-ready-for-more-ai-and-advertising-says-ceo-165515262.html",
         "Reddit IPO: ready for more AI and advertising",
         "Stock opened at $34, reached intra-day high of $55.39 (63% increase), RDDT ticker"),

        (94, "verkauf", "Sold 500,000 Reddit shares during IPO process for estimated $17 million",
         "2024-03-01", "https://fortune.com/2024/03/20/ipos-reddit-openai-sam-altman-sequoia-capital-fmr-vogue-tencent/",
         "Who's getting rich on the Reddit IPO?",
         "CEO and top executives sold stock as part of IPO"),

        (94, "partnerschaft", "Signed data licensing partnership with OpenAI worth estimated $70 million per year",
         "2024-05-16", "https://techcrunch.com/2024/05/16/openai-inks-deal-to-train-ai-on-reddit-data/",
         "OpenAI inks deal to train AI on Reddit data",
         "Provided OpenAI access to real-time, structured Reddit content for AI training"),

        (94, "sonstiges", "Achieved billionaire status as Reddit stock soared after earnings report",
         "2025-11-01", "https://fortune.com/2025/11/03/reddit-ceo-steve-huffman-became-billionaire-20-years-after-founding-company-12-thousand-dollar-investment/",
         "Reddit's CEO just become a billionaire",
         "Net worth reached $1.2 billion, fifth consecutive quarter of profitability since IPO"),

        (94, "produktlaunch", "Announced plans to launch paid subreddits and contributor monetization features",
         "2025-02-14", "https://www.latesthappenings.com/tech/reddits-paywall-era-begins-ceo-steve-huffman-confirms-paid-subreddits-for-2025",
         "Reddit's Paywall Era Begins",
         "Confirmed paid subreddits coming in 2025, allowing community monetization"),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)

    conn.commit()

    # Zählung
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = 94")
    anzahl_aussagen = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = 94")
    anzahl_handlungen = cursor.fetchone()[0]

    conn.close()

    return anzahl_aussagen, anzahl_handlungen

if __name__ == "__main__":
    try:
        aussagen_count, handlungen_count = insert_data()
        print(f"Erfolgreich eingefuegt fuer Steve Huffman (person_id=94):")
        print(f"  - {aussagen_count} Aussagen")
        print(f"  - {handlungen_count} Handlungen")
        print(f"  - GESAMT: {aussagen_count + handlungen_count} Eintraege")
    except Exception as e:
        print(f"Fehler: {e}")
