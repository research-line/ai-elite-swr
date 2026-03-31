import sqlite3
from datetime import datetime

# Connect to database
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 63  # Winston Weinberg

# AUSSAGEN
aussagen = [
    # 1. Stress and Growth Philosophy
    (person_id,
     "You should be constantly stressed and do things that make you stressed every day. I think the times that I've stagnated, or the company has stagnated, is every day I don't have something that's really stressful.",
     "Founders should be constantly stressed to grow",
     "muendlich",
     "https://www.entrepreneur.com/business-news/the-ceo-of-an-8-billion-startup-says-you-should-be-constantly-stressed-to-do-your-best-work",
     "The CEO of an $8 Billion Startup Says You Should Be 'Constantly Stressed'",
     "2025-11-01",
     "en",
     "Interview about work philosophy and personal growth"),

    # 2. Reinvent yourself every 4 months
    (person_id,
     "Every four months he experiences a mental block where there are too many things going wrong at the company and he can't address all of them. He needs to reinvent himself as a founder every, like, four months or so, otherwise he is not going to be able to fix all of the things that are going wrong at the company.",
     "Reinvent yourself as founder every 4 months",
     "muendlich",
     "https://sequoiacap.com/podcast/harvey-ceo-winston-weinberg-why-you-should-reinvent-yourself-every-4-months/",
     "Harvey CEO Winston Weinberg: Why You Should Reinvent Yourself Every 4 Months",
     "2025-06-01",
     "en",
     "Sequoia Capital podcast about leadership"),

    # 3. Earning valuation
    (person_id,
     "We need to earn that valuation everyday.",
     "We need to earn $8B valuation everyday",
     "schriftlich",
     "https://www.lawnext.com/2025/12/harvey-cofounders-answer-tough-questions-in-reddit-ama-valuation-competition-and-the-future-of-legal-ai.html",
     "Harvey Cofounders Answer Tough Questions in Reddit AMA",
     "2025-12-01",
     "en",
     "Reddit AMA about company valuation"),

    # 4. Market opportunity
    (person_id,
     "The simplest answer here is that the tech penetration into the legal market is going to change massively. If we build a great product we hopefully capture some of that very large upside.",
     "Tech penetration in legal market will change massively",
     "schriftlich",
     "https://www.lawnext.com/2025/12/harvey-cofounders-answer-tough-questions-in-reddit-ama-valuation-competition-and-the-future-of-legal-ai.html",
     "Harvey Cofounders Answer Tough Questions in Reddit AMA",
     "2025-12-01",
     "en",
     "Reddit AMA about market opportunity"),

    # 5. AI and legal hiring
    (person_id,
     "There's a world in which, actually, this is super good for the profession and very good for recruiting into the profession.",
     "AI could be super good for legal profession and recruiting",
     "muendlich",
     "https://www.lawnext.com/2025/12/harvey-cofounders-answer-tough-questions-in-reddit-ama-valuation-competition-and-the-future-of-legal-ai.html",
     "Harvey Cofounders Answer Tough Questions in Reddit AMA",
     "2025-12-01",
     "en",
     "Reddit AMA about AI's impact on legal profession"),

    # 6. Demo strategy - holding up mirror
    (person_id,
     "It was like holding up a mirror. Many lawyers appreciated the unvarnished feedback, which mirrored the scrutiny they faced in courtrooms.",
     "Demo strategy was like holding up mirror to lawyers",
     "muendlich",
     "https://dnyuz.com/2026/01/19/harveys-ceo-explains-his-early-tactic-to-get-customers-telling-lawyers-how-bad-their-arguments-were/",
     "Harvey's CEO explains his early tactic to get customers",
     "2026-01-19",
     "en",
     "Interview about early customer acquisition strategy"),

    # 7. Google Docs interview
    (person_id,
     "This is the best way to separate good interviewers from good operators. There are folks that are really good at talking and terrible at doing.",
     "Google Docs interviews separate good talkers from good operators",
     "muendlich",
     "https://dnyuz.com/2025/11/21/harvey-ceo-explains-why-he-interviews-candidates-in-google-docs-there-are-folks-that-are-really-good-at-talking/",
     "Harvey CEO explains why he interviews candidates in Google Docs",
     "2025-11-21",
     "en",
     "Interview about hiring process"),

    # 8. Decision making philosophy
    (person_id,
     "I think people feel like you can't make mistakes. And that is actually the opposite of how I feel. I would much rather people just try and make a decision and then it's wrong, and a week later they adjust and change, than they spend, like, three months not making a decision.",
     "Better to make wrong decisions quickly than delay for months",
     "muendlich",
     "https://sequoiacap.com/podcast/harvey-ceo-winston-weinberg-why-you-should-reinvent-yourself-every-4-months/",
     "Harvey CEO Winston Weinberg: Why You Should Reinvent Yourself Every 4 Months",
     "2025-06-01",
     "en",
     "Sequoia Capital podcast about decision-making"),

    # 9. Task automation not job automation
    (person_id,
     "It is not job displacement, it is task displacement. And I think that's a super important distinction because getting rid of those tasks does not mean the legal industry falls apart.",
     "AI is task automation, not job automation",
     "muendlich",
     "https://www.webpronews.com/harvey-ceo-envisions-ai-transforming-law-less-burnout-more-strategy/",
     "Harvey CEO Envisions AI Transforming Law: Less Burnout, More Strategy",
     "2025-11-01",
     "en",
     "Interview about AI's impact on legal profession"),

    # 10. Junior lawyers benefit
    (person_id,
     "The junior folks are incredibly happy about this. Most junior associates spend the first part of their careers on rote tasks such as reviewing documents in discovery or in data rooms, and you end up not being able to do the strategic level things until like 10 years into your career, if you're lucky, five.",
     "Junior lawyers happy about AI automating rote tasks",
     "muendlich",
     "https://b17news.com/the-founder-of-harvey-says-a-massive-shift-is-coming-to-the-legal-profession-the-junior-folks-are-incredibly-happy-about-this/",
     "The founder of Harvey says a massive shift is coming to the legal profession",
     "2025-11-01",
     "en",
     "Interview about AI's impact on junior lawyers"),

    # 11. AI agents and leverage pyramid
    (person_id,
     "Agents will rewire the leverage pyramid, moving junior lawyers past rote work while strengthening partner profitability.",
     "AI agents will rewire law firm leverage pyramid",
     "muendlich",
     "https://ccbjournal.com/blog/in-the-ai-agent-war-harvey-ai-puts-law-firms-on-the-front-line",
     "In the AI Agent War, Harvey AI Puts Law Firms on the Front Line",
     "2025-11-01",
     "en",
     "Interview about AI agents in legal work"),

    # 12. Multiplayer legal services
    (person_id,
     "The future of legal services is becoming 'multiplayer' - a future of collaborative systems that allow lawyers and their clients to work alongside AI in a shared environment.",
     "Future of legal services is collaborative multiplayer systems",
     "muendlich",
     "https://www.artificiallawyer.com/2025/11/03/the-future-of-legal-ai-is-collaboration-harvey/",
     "The Future of Legal AI Is Collaboration - Harvey",
     "2025-11-03",
     "en",
     "Interview about future vision for legal AI"),

    # 13. Complex work automation
    (person_id,
     "The biggest gains will come from enabling lawyers to better handle the most complex work—not NDA review but transactions on the scale of mega-mergers, with AI eventually automating the first 10% of such deals.",
     "AI will enable lawyers to handle most complex work, not just NDAs",
     "muendlich",
     "https://www.artificiallawyer.com/2025/11/03/the-future-of-legal-ai-is-collaboration-harvey/",
     "The Future of Legal AI Is Collaboration - Harvey",
     "2025-11-03",
     "en",
     "Interview about AI's role in complex legal work"),

    # 14. Multiple competitors in space
    (person_id,
     "I don't think a single player is going to capture all of the pretty enormous amount of value that will be created in the next 10 years in this space.",
     "Room for multiple competitors in legal AI space",
     "schriftlich",
     "https://www.lawnext.com/2025/12/harvey-cofounders-answer-tough-questions-in-reddit-ama-valuation-competition-and-the-future-of-legal-ai.html",
     "Harvey Cofounders Answer Tough Questions in Reddit AMA",
     "2025-12-01",
     "en",
     "Reddit AMA about competition"),

    # 15. LexisNexis partnership value
    (person_id,
     "LexisNexis is an insanely trusted data source. The partnership has enabled Harvey to build specialized workflows like drafting motions for summary judgment and motions to dismiss that combine Lexis data with Harvey's drafting capabilities.",
     "LexisNexis trusted data source enables specialized workflows",
     "schriftlich",
     "https://www.lawnext.com/2025/12/harvey-cofounders-answer-tough-questions-in-reddit-ama-valuation-competition-and-the-future-of-legal-ai.html",
     "Harvey Cofounders Answer Tough Questions in Reddit AMA",
     "2025-12-01",
     "en",
     "Reddit AMA about LexisNexis partnership"),

    # 16. Model performance vs UX
    (person_id,
     "The biggest problem with ChatGPT and similar tools is they're focusing so much on performance from the model side and not on how to make the experience easier for the user.",
     "AI tools focus too much on model performance, not UX",
     "muendlich",
     "https://www.thetwentyminutevc.com/winston-weinberg",
     "Harvey's CEO on How Model Performance is Plateauing",
     "2025-09-01",
     "en",
     "Podcast about AI development priorities"),

    # 17. Access to justice
    (person_id,
     "It's an honour to partner with the Singapore Judiciary, a recognised leader in judicial innovation, on this pivotal project. This initiative is a perfect example of how public-private partnerships can leverage cutting-edge technology to create a more efficient and equitable justice system for the public.",
     "Public-private partnerships can create more equitable justice system",
     "muendlich",
     "https://www.judiciary.gov.sg/news-and-resources/news/news-details/media-release--new-generative-ai-powered-case-summarisation-tool-to-help-small-claims-tribunals-users",
     "Singapore Judiciary AI-powered Case Summarisation Tool",
     "2025-05-01",
     "en",
     "Media release about Singapore judiciary partnership"),

    # 18. Firm differentiation
    (person_id,
     "Firms are asking 'how do I differentiate myself as a firm?' There is a gap between firms that have significant internal expertise and innovation teams, and those that don't. Harvey is giving firms the tools to innovate on top of Harvey.",
     "Harvey enables law firms to differentiate through innovation",
     "muendlich",
     "https://legaltechnology.com/2025/06/24/harvey-launches-workflow-builder-we-speak-with-winston-weinberg-and-ashurst-about-the-tool-that-helps-legal-teams-leverage-their-own-ip/",
     "Harvey launches Workflow Builder",
     "2025-06-24",
     "en",
     "Interview about Workflow Builder product launch"),

    # 19. Multi-model strategy
    (person_id,
     "Harvey didn't avoid other models out of loyalty to OpenAI, but necessity. Until recently, most major law firms would only approve AI tools that ran through Microsoft Azure, which meant models like Claude and Gemini couldn't clear security reviews.",
     "Adopted multi-model strategy due to security requirements, not loyalty",
     "muendlich",
     "https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/",
     "Anthropic, Google score win by nabbing OpenAI-backed Harvey as a user",
     "2025-05-13",
     "en",
     "TechCrunch article about Harvey's multi-model strategy"),

    # 20. Cold email to Sam Altman
    (person_id,
     "We figured we had to email a lawyer because otherwise the person wouldn't know if the outputs were right.",
     "Emailed OpenAI lawyer because they could verify AI outputs",
     "muendlich",
     "https://techcrunch.com/2025/11/14/inside-harvey-how-a-first-year-legal-associate-built-one-of-silicon-valleys-hottest-startups/",
     "Inside Harvey: How a first-year legal associate built one of Silicon Valley's hottest startups",
     "2025-11-14",
     "en",
     "TechCrunch interview about founding story")
]

# HANDLUNGEN
handlungen = [
    # 1. Company founding
    (person_id,
     "gruendung",
     "Co-founded Harvey AI with Gabriel Pereyra after leaving O'Melveny & Myers law firm after just one year. Cold-emailed Sam Altman and OpenAI's general counsel on July 4, 2022, leading to a pitch call with OpenAI's C-suite.",
     "2022-07-31",
     "https://techcrunch.com/2025/11/14/inside-harvey-how-a-first-year-legal-associate-built-one-of-silicon-valleys-hottest-startups/",
     "Inside Harvey: How a first-year legal associate built Silicon Valley's hottest startup",
     "Former first-year legal associate co-founded legal AI startup"),

    # 2. Seed round
    (person_id,
     "investition",
     "Raised $5 million seed round led by OpenAI Startup Fund, with investors including Jeff Dean (Google AI head), Elad Gil (Mixer Labs founder), and Sarah Guo (Conviction founder).",
     "2022-11-23",
     "https://techcrunch.com/2022/11/23/harvey-which-uses-ai-to-answer-legal-questions-lands-cash-from-openai/",
     "Harvey lands cash from OpenAI",
     "OpenAI Startup Fund's first legal AI investment"),

    # 3. Series A
    (person_id,
     "investition",
     "Raised $23 million Series A round led by Sequoia Capital.",
     "2023-04-01",
     "https://en.wikipedia.org/wiki/Harvey_(software)",
     "Harvey (software) - Wikipedia",
     "Sequoia Capital led Series A"),

    # 4. Series B
    (person_id,
     "investition",
     "Raised $80 million Series B round led by Elad Gil and Kleiner Perkins, valuing company at $715 million.",
     "2023-12-01",
     "https://en.wikipedia.org/wiki/Harvey_(software)",
     "Harvey (software) - Wikipedia",
     "Kleiner Perkins led round, $715M valuation"),

    # 5. Series C
    (person_id,
     "investition",
     "Raised $100 million Series C round, valuing company at $1.5 billion.",
     "2024-07-01",
     "https://en.wikipedia.org/wiki/Harvey_(software)",
     "Harvey (software) - Wikipedia",
     "Reached $1.5B valuation"),

    # 6. Series D
    (person_id,
     "investition",
     "Raised $300 million Series D round led by Sequoia Capital at $3 billion valuation, with CEO stating target of $100 million annual recurring revenue.",
     "2025-02-12",
     "https://fortune.com/2025/02/12/legal-ai-startup-harvey-300-million-series-d-funding-3-billion-valuation-sequoia/",
     "Legal AI startup Harvey lands fresh $300 million in Sequoia-led round",
     "Series D at $3B valuation, $100M ARR target"),

    # 7. Series E
    (person_id,
     "investition",
     "Raised $300 million Series E round at $5 billion valuation.",
     "2025-06-01",
     "https://techcrunch.com/2025/11/14/inside-harvey-how-a-first-year-legal-associate-built-one-of-silicon-valleys-hottest-startups/",
     "Inside Harvey TechCrunch article",
     "Series E at $5B valuation"),

    # 8. Partnership with PwC
    (person_id,
     "partnerschaft",
     "Announced strategic alliance with PwC Legal Business Solutions. Harvey and PwC jointly developing custom AI models for tax, legal and HR, with 4,000 PwC professionals in 100 countries using Harvey.",
     "2023-08-01",
     "https://www.pwc.com/gx/en/news-room/press-releases/2023/pwc-announces-strategic-alliance-with-harvey-positioning-pwcs-legal-business-solutions-at-the-forefront-of-legal-generative-ai.html",
     "PwC announces strategic alliance with Harvey",
     "PwC partnership for 4,000 professionals across 100 countries"),

    # 9. Allen & Overy partnership
    (person_id,
     "partnerschaft",
     "Allen & Overy law firm rolled out Harvey to 3,500 staff members, with lawyers using it for around 40,000 queries during trial period.",
     "2023-10-01",
     "https://en.wikipedia.org/wiki/Harvey_(software)",
     "Harvey (software) - Wikipedia",
     "Allen & Overy deployed Harvey to 3,500 lawyers"),

    # 10. LexisNexis partnership
    (person_id,
     "partnerschaft",
     "Announced strategic alliance with LexisNexis Legal & Professional to integrate LexisNexis' AI technology, primary law content, and Shepard's Citations within Harvey platform. Co-developed workflows for motion to dismiss and summary judgment.",
     "2025-06-18",
     "https://legaltechnology.com/2025/06/18/lexisnexis-and-harvey-announce-strategic-alliance-in-major-genai-turning-point/",
     "LexisNexis and Harvey announce strategic alliance",
     "Major partnership integrating LexisNexis legal content"),

    # 11. Workflow Builder launch
    (person_id,
     "produktlaunch",
     "Launched Workflow Builder product, enabling law firms to design custom repeatable workflows embedding firm expertise. Paul, Weiss became first firm to launch custom workflows. Early adopters included Ashurst, Ropes & Gray, dentsu, King & Wood Mallesons, and Setterwalls.",
     "2025-06-11",
     "https://legaltechnology.com/2025/06/24/harvey-launches-workflow-builder-we-speak-with-winston-weinberg-and-ashurst-about-the-tool-that-helps-legal-teams-leverage-their-own-ip/",
     "Harvey launches Workflow Builder",
     "Product launch enabling firms to create custom AI workflows"),

    # 12. Multi-model strategy adoption
    (person_id,
     "umstrukturierung",
     "Announced Harvey will use foundation models from Anthropic (Claude) and Google (Gemini), moving beyond exclusively using OpenAI models. Users can route tasks to best-performing model or select manually.",
     "2025-05-13",
     "https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/",
     "Anthropic, Google score win by nabbing OpenAI-backed Harvey",
     "Strategic shift to multi-model AI approach"),

    # 13. Singapore judiciary partnership
    (person_id,
     "partnerschaft",
     "Partnered with Singapore Judiciary to develop generative AI tool that summarizes case documents for Tribunal Magistrates and individuals in Small Claims Tribunals. Part of Harvey's access to justice program.",
     "2025-05-01",
     "https://www.judiciary.gov.sg/news-and-resources/news/news-details/media-release--new-generative-ai-powered-case-summarisation-tool-to-help-small-claims-tribunals-users",
     "Singapore Judiciary AI tool media release",
     "Government partnership for access to justice initiative"),

    # 14. Series F funding round
    (person_id,
     "investition",
     "Raised $160 million round led by Andreessen Horowitz, valuing company at $8 billion. Surpassed $100 million annual recurring revenue in August with 700 clients across 63 countries including majority of top 10 US law firms.",
     "2025-12-04",
     "https://techcrunch.com/2025/12/04/legal-ai-startup-harvey-confirms-8b-valuation/",
     "Legal AI startup Harvey confirms $8B valuation",
     "Series F at $8B valuation, $100M+ ARR achieved"),

    # 15. Fundraising for $11B valuation
    (person_id,
     "investition",
     "Reportedly raising new round at $11 billion valuation just months after hitting $8 billion valuation, with $190 million annual revenue.",
     "2026-02-09",
     "https://techcrunch.com/2026/02/09/harvey-reportedly-raising-at-11b-valuation-just-months-after-it-hit-8b/",
     "Harvey reportedly raising at $11B valuation",
     "New funding round targeting $11B valuation")
]

# Insert aussagen
print("Inserting aussagen...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)
    print(f"  Inserted: {aussage[2]}")

# Insert handlungen
print("\nInserting handlungen...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)
    print(f"  Inserted: {handlung[1]} - {handlung[2][:60]}...")

# Commit and close
conn.commit()
conn.close()

print(f"\n=== SUMMARY ===")
print(f"Total aussagen inserted: {len(aussagen)}")
print(f"Total handlungen inserted: {len(handlungen)}")
print(f"Total records inserted: {len(aussagen) + len(handlungen)}")
print(f"\nAll data successfully inserted for Winston Weinberg (person_id={person_id})")
