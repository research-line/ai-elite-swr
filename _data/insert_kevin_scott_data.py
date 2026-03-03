import sqlite3
from datetime import datetime

# Database connection
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 93  # Kevin Scott

# AUSSAGEN - INSERT STATEMENTS
aussagen = [
    # Aussage 1
    (person_id,
     "AI has the potential to create opportunity for everyone and help solve some of our most vexing problems. The sooner that we stop viewing AI as a substitute for human labor and start imagining how it can be a force multiplier for human ingenuity, the better.",
     "AI as force multiplier for human ingenuity",
     "schriftlich",
     "https://news.microsoft.com/reprogramming-the-american-dream/",
     "Reprogramming the American Dream - Microsoft News",
     "2020-04-07",
     "en",
     "Book publication and promotional materials for 'Reprogramming the American Dream'"),

    # Aussage 2
    (person_id,
     "Technology only matters when it expands what people can do. The core question stays constant: Does the work make someone's life or job meaningfully better? Are we doing the best job that we possibly can to build technology in a way where 40 years from now, our children and our grandchildren will look back and say, 'Wow, this was beneficial. This mattered.'",
     "Technology must meaningfully improve lives",
     "schriftlich",
     "https://www.relativity.com/blog/ai-is-not-what-the-world-thinks-it-is-insights-from-microsoft-cto-kevin-scott/",
     "AI Is Not What the World Thinks It Is - Relativity Blog",
     "2023-01-01",
     "en",
     "Discussion about technology's purpose and long-term impact"),

    # Aussage 3
    (person_id,
     "Every time that we have used AI to solve a problem that we thought was some high watermark of human intelligence, we have changed our mind about how important that watermark was.",
     "AI redefines human intelligence benchmarks",
     "schriftlich",
     "https://www.relativity.com/blog/ai-is-not-what-the-world-thinks-it-is-insights-from-microsoft-cto-kevin-scott/",
     "AI Is Not What the World Thinks It Is - Relativity Blog",
     "2023-01-01",
     "en",
     "Reflections on AI capabilities and human perception of intelligence"),

    # Aussage 4
    (person_id,
     "We must democratize access to AI tools so that people in small communities have the same access I do, because I have infinite amounts of faith in their ability to go do amazing things once they have the access, which ultimately ensures fair and inclusive decision-making about AI's trajectory.",
     "Democratize AI access for all communities",
     "schriftlich",
     "https://www.relativity.com/blog/ai-is-not-what-the-world-thinks-it-is-insights-from-microsoft-cto-kevin-scott/",
     "AI Is Not What the World Thinks It Is - Relativity Blog",
     "2023-01-01",
     "en",
     "Discussion on democratization of AI and equal access"),

    # Aussage 5
    (person_id,
     "As I dug in to try to understand where all of the capability gaps were between Google and us for model training, I got very, very worried. The thing that's interesting about what OpenAI and DeepMind and Google Brain are doing is the scale of their ambition.",
     "Very worried about Google's AI lead",
     "schriftlich",
     "https://fortune.com/2024/05/02/microsoft-ai-openai-google-bill-gates-satya-nadella-chatgpt-kevin-scott-email/",
     "2019 email from Microsoft's CTO - Fortune",
     "2019-06-01",
     "en",
     "Internal email to Satya Nadella and Bill Gates expressing concerns about Microsoft's AI capabilities compared to competitors"),

    # Aussage 6
    (person_id,
     "We are multiple years behind the competition in terms of ML scale.",
     "Microsoft years behind in ML scale",
     "schriftlich",
     "https://www.windowscentral.com/microsoft/emails-show-microsoft-was-worried-about-google-ai-development",
     "Microsoft worried about Google AI - Windows Central",
     "2019-06-01",
     "en",
     "Part of the 2019 email to Microsoft leadership about AI competitive position"),

    # Aussage 7
    (person_id,
     "Despite what other people think, we're not at diminishing marginal returns on scale-up. The unfortunate thing is you only get to sample it every couple of years because it just takes a while to build supercomputers and then train models on top of them.",
     "Scaling laws still hold strong",
     "schriftlich",
     "https://sequoiacap.com/podcast/training-data-kevin-scott/",
     "Microsoft CTO on Scaling Laws - Sequoia Capital",
     "2024-07-15",
     "en",
     "Podcast interview discussing AI scaling laws and future of large language models"),

    # Aussage 8
    (person_id,
     "Everything that large language models can do will get better at the next scale point, and they will become more general in capability.",
     "LLMs improve with each scale increase",
     "schriftlich",
     "https://sequoiacap.com/podcast/training-data-kevin-scott/",
     "Microsoft CTO on Scaling Laws - Sequoia Capital",
     "2024-07-15",
     "en",
     "Discussion on the continued benefits of scaling AI models"),

    # Aussage 9
    (person_id,
     "We must ensure equal access to technology, starting with rural broadband. In order for these communities to be able to connect with their digital future, they actually have to be able to connect to the internet. You can't run a modern, technology-heavy business when your business and your employees don't have great broadband connectivity.",
     "Rural broadband is essential infrastructure",
     "schriftlich",
     "https://www.geekwire.com/2020/reprogramming-american-dream-microsofts-cto-returns-rural-roots-find-future-ai/",
     "Reprogramming the American Dream - GeekWire",
     "2020-02-01",
     "en",
     "Discussion on technology infrastructure needs in rural America"),

    # Aussage 10
    (person_id,
     "AI must be developed in accordance with a set of policies that democratize AI. AI must be accessible to all individuals and all businesses so that this immense potential is not missed by those with limited resources.",
     "AI democratization requires policy framework",
     "schriftlich",
     "https://www.vedp.org/news/making-ai-serve-us-all-conversation-kevin-scott",
     "Making AI Serve Us All - Virginia Economic Development",
     "2020-01-01",
     "en",
     "Talk about AI policy and democratization principles"),

    # Aussage 11
    (person_id,
     "Humans and machines have different strengths—machines excel at chess, Go, and repetitive work, while humans are strong in areas like common sense reasoning where machines still have long way to go.",
     "Humans and AI have complementary strengths",
     "schriftlich",
     "https://www.mckinsey.com/featured-insights/future-of-work/forward-thinking-on-artificial-intelligence-with-microsoft-cto-kevin-scott",
     "Forward Thinking on AI - McKinsey",
     "2022-01-01",
     "en",
     "Interview about the relationship between human and machine intelligence"),

    # Aussage 12
    (person_id,
     "We're probably going to have more change over the next 40 years due to technology than in the past 40. We as a society need to realize the potential for AI to relieve us of repetitive cognitive work, and with the democratization of AI should come recognition of our unique abilities as humans.",
     "Next 40 years will see unprecedented tech change",
     "schriftlich",
     "https://exchange.scale.com/public/blogs/kevin-scott-cto-of-microsoft-speaks-on-democratizing-and-accelerating-the-future-of-ai",
     "Kevin Scott's Seven Insights on AI - Scale Events",
     "2023-01-01",
     "en",
     "Speech about future technological transformation and human capabilities"),

    # Aussage 13
    (person_id,
     "The partnership with OpenAI was basically a bet saying this particular team at the time also understood that this was a game of scaling, compute and doing incredible things with it in a very disciplined way. If we work with them, they will push us to build better infrastructure, and we can enable them to do their best work.",
     "OpenAI partnership was strategic bet on scaling",
     "schriftlich",
     "https://www.yahoo.com/tech/microsofts-partnership-openai-basically-bet-095253559.html",
     "Microsoft's partnership with OpenAI was 'basically a bet' - Yahoo",
     "2025-10-06",
     "en",
     "TechCrunch Disrupt 2025 discussion about the strategic rationale behind Microsoft-OpenAI partnership"),

    # Aussage 14
    (person_id,
     "Developers report that Copilot helps them stay in the flow and keeps their minds sharper during what used to be boring and repetitive tasks, and when AI tools help eliminate drudgery from a job, it improves satisfaction.",
     "AI tools eliminate drudgery and improve satisfaction",
     "schriftlich",
     "https://www.microsoft.com/en-us/worklab/kevin-scott-on-5-ways-generative-ai-will-transform-work-in-2023",
     "Kevin Scott on 5 Ways Generative AI Will Transform Work - Microsoft",
     "2023-01-01",
     "en",
     "Analysis of GitHub Copilot impact on developer productivity and satisfaction"),

    # Aussage 15
    (person_id,
     "GitHub Copilot is a large language model-based system that turns natural language prompts into code and has a dramatic positive impact on developer productivity, opening up coding to a much broader group of people.",
     "Copilot democratizes coding capabilities",
     "schriftlich",
     "https://news.microsoft.com/source/features/ai/a-conversation-with-kevin-scott-whats-next-in-ai/",
     "A conversation with Kevin Scott: What's next in AI - Microsoft Source",
     "2023-01-01",
     "en",
     "Discussion on AI's impact on software development"),

    # Aussage 16
    (person_id,
     "Within five years, 95% of new code could be AI-generated, enabling even non-coders like my 16-year-old daughter to build apps effortlessly.",
     "95% of code will be AI-generated in 5 years",
     "muendlich",
     "https://every.to/chain-of-thought/microsoft-s-ai-vision-an-open-internet-made-for-agents",
     "Microsoft's AI Vision - Every.to",
     "2025-05-01",
     "en",
     "Microsoft Build 2025 keynote presentation on future of coding"),

    # Aussage 17
    (person_id,
     "The agentic web is an open internet with agents talking to agents the way browsers talk to servers. By championing the open Model Context Protocol across GitHub, Copilot Studio, Azure AI Foundry, and Windows 11, Microsoft aims to provide HTTP-style interoperability and memory via structured retrieval augmentation.",
     "Vision for an open agentic web",
     "muendlich",
     "https://devblogs.microsoft.com/blog/a-developers-guide-to-build-2025",
     "A Developer's Guide to Build 2025 - Microsoft",
     "2025-05-01",
     "en",
     "Microsoft Build 2025 keynote outlining vision for AI agents"),

    # Aussage 18
    (person_id,
     "Technology really does massively benefit society. You wouldn't go take mechanical engines or books away from society. AI will eventually be indispensable to society, and we must choose what kind of transformation wave we're going to have.",
     "AI will become indispensable to society",
     "schriftlich",
     "https://exchange.scale.com/public/blogs/kevin-scott-cto-of-microsoft-speaks-on-democratizing-and-accelerating-the-future-of-ai",
     "Kevin Scott's Seven Insights on AI - Scale Events",
     "2023-01-01",
     "en",
     "Discussion on AI's inevitable integration into society"),

    # Aussage 19
    (person_id,
     "Massive crunch is probably an understatement. I think we have been in a mode where it's been almost impossible to build capacity fast enough since ChatGPT launched.",
     "Impossible to build capacity fast enough",
     "schriftlich",
     "https://www.capgemini.com/insights/research-library/a-conversation-with-kevin-scott/",
     "Turning scarcity into abundance - Capgemini",
     "2024-01-01",
     "en",
     "Discussion on data center capacity constraints and AI infrastructure challenges"),

    # Aussage 20
    (person_id,
     "I expect constraints to persist for a while. Demand keeps exploding. I do not see demand for inference declining and some of the most ambitious teams using coding agents can face inference costs of roughly $150,000 per year.",
     "AI compute demand will stay constrained",
     "muendlich",
     "https://finance.yahoo.com/news/microsoft-conference-kevin-scott-says-060806311.html",
     "Microsoft Conference: Kevin Scott on AI Outpacing Use Cases - Yahoo Finance",
     "2024-01-01",
     "en",
     "Microsoft conference presentation on AI infrastructure challenges")
]

# HANDLUNGEN - INSERT STATEMENTS
handlungen = [
    # Handlung 1
    (person_id,
     "einstellung",
     "Kevin Scott appointed as Microsoft Chief Technology Officer, reporting directly to CEO Satya Nadella",
     "2017-01-24",
     "https://news.microsoft.com/source/2017/01/24/microsoft-appoints-kevin-scott-as-chief-technology-officer/",
     "Microsoft appoints Kevin Scott as CTO - Microsoft Source",
     "Scott joined Microsoft's Senior Leadership Team in a newly created CTO role following LinkedIn acquisition"),

    # Handlung 2
    (person_id,
     "investition",
     "Microsoft invested $1 billion in OpenAI following Kevin Scott's strategic recommendation",
     "2019-07-01",
     "https://fortune.com/2024/05/02/microsoft-ai-openai-google-bill-gates-satya-nadella-chatgpt-kevin-scott-email/",
     "Microsoft's $1B OpenAI Investment - Fortune",
     "Scott's June 2019 email to Nadella and Gates about being 'very worried' about Google's AI led directly to the investment decision"),

    # Handlung 3
    (person_id,
     "produktlaunch",
     "GitHub Copilot launched as AI pair programming tool, co-developed under Scott's leadership",
     "2021-06-29",
     "https://www.linkedin.com/posts/jkevinscott_were-super-excited-to-launch-github-copilot-activity-6815702070205792256-mehZ",
     "GitHub Copilot Launch - Kevin Scott LinkedIn",
     "Scott announced the launch of GitHub Copilot, built in collaboration with OpenAI"),

    # Handlung 4
    (person_id,
     "produktlaunch",
     "Book 'Reprogramming the American Dream: From Rural America to Silicon Valley—Making AI Serve Us All' published",
     "2020-04-07",
     "https://www.amazon.com/Reprogramming-American-Dream-America-Valley_Making/dp/0062879871",
     "Reprogramming the American Dream - Amazon",
     "Kevin Scott published #1 WSJ bestselling book co-authored with Greg Shaw, with foreword by J.D. Vance"),

    # Handlung 5
    (person_id,
     "investition",
     "Microsoft invested additional $10 billion in OpenAI, giving it just shy of 50% stake",
     "2023-01-23",
     "https://www.fastcompany.com/90957311/how-microsoft-cto-kevin-scott-helped-forge-the-companys-deal-with-openai",
     "How Microsoft CTO Kevin Scott helped forge OpenAI deal - Fast Company",
     "Extended partnership following ChatGPT success, with Scott being credited for 75-80% of partnership success by Sam Altman"),

    # Handlung 6
    (person_id,
     "partnerschaft",
     "Microsoft and OpenAI extended partnership announced with supercomputing infrastructure commitment",
     "2023-01-23",
     "https://stratechery.com/2023/new-bing-and-an-interview-with-kevin-scott-and-sam-altman-about-the-microsoft-openai-partnership/",
     "New Bing and Microsoft-OpenAI Partnership - Stratechery",
     "Scott participated in joint interview with Sam Altman about the extended partnership and technology-sharing deal"),

    # Handlung 7
    (person_id,
     "umstrukturierung",
     "Microsoft deployed equivalent of five 561 petaflops supercomputers monthly for AI infrastructure",
     "2024-05-21",
     "https://www.datacenterdynamics.com/en/news/microsoft-deploying-equivalent-of-five-561-petaflops-supercomputers-every-month/",
     "Microsoft deploying five supercomputers monthly - Data Center Dynamics",
     "Scott announced at Microsoft Build 2024 that Microsoft is deploying 72,000 H100 GPU equivalents monthly, totaling 2.8 exaflops of compute"),

    # Handlung 8
    (person_id,
     "produktlaunch",
     "Launched 'Behind the Tech' podcast as host, interviewing technology innovators",
     "2018-01-01",
     "https://www.microsoft.com/en-us/behind-the-tech",
     "Behind the Tech Podcast - Microsoft",
     "Scott created and hosts podcast featuring AI experts, computer scientists, and innovators"),

    # Handlung 9
    (person_id,
     "lobbying",
     "Participated in National Security Commission on AI, representing industry perspective on AI policy",
     "2019-01-01",
     "https://www.techbrew.com/stories/2022/05/31/microsoft-cto-kevin-scott-thinks-ai-should-be-regulated",
     "Microsoft CTO Kevin Scott thinks AI should be regulated - Tech Brew",
     "Scott participated in National Security Council's commission on AI with industry, academia, and government representatives"),

    # Handlung 10
    (person_id,
     "umstrukturierung",
     "Led Microsoft Responsible AI Council as co-chair alongside Brad Smith",
     "2020-01-01",
     "https://www.microsoft.com/insidetrack/blog/responsible-ai-why-it-matters-and-how-were-infusing-it-into-our-internal-ai-projects-at-microsoft/",
     "Responsible AI at Microsoft - Inside Track Blog",
     "Scott provides leadership and strategic guidance for Microsoft's responsible AI initiatives"),

    # Handlung 11
    (person_id,
     "investition",
     "Microsoft invested $19 billion in data center capital expenditures for AI workload capacity",
     "2024-01-01",
     "https://www.ciodive.com/news/microsoft-azure-capacity-constraints-datacenter-buildouts-cloud-ai/722912/",
     "Microsoft spends billions on infrastructure - CIO Dive",
     "Scott oversees massive data center buildout, with over 2GW capacity added in 12 months"),

    # Handlung 12
    (person_id,
     "produktlaunch",
     "Windows AI Foundry and Model Context Protocol (MCP) integration announced at Build 2025",
     "2025-05-01",
     "https://devblogs.microsoft.com/blog/a-developers-guide-to-build-2025",
     "A Developer's Guide to Build 2025 - Microsoft",
     "Scott presented Microsoft's vision for agentic web with MCP integration across Windows 11, GitHub, and Azure"),

    # Handlung 13
    (person_id,
     "partnerschaft",
     "Microsoft and NVIDIA collaboration announced to build AI supercomputer",
     "2023-01-01",
     "https://www.capgemini.com/insights/research-library/a-conversation-with-kevin-scott/",
     "Turning scarcity into abundance - Capgemini",
     "Scott announced supercomputer partnership powered by Azure infrastructure and NVIDIA GPUs"),

    # Handlung 14
    (person_id,
     "produktlaunch",
     "SQL Server 2025 public preview announced with AI-ready enterprise database capabilities",
     "2025-05-01",
     "https://www.outlookbusiness.com/technology/microsoft-build-2025-live-ceo-satya-nadella-to-unveil-copilot-ai-enhancements-and-azure-innovations",
     "Microsoft Build 2025 Announcements - Outlook Business",
     "Scott announced SQL Server 2025 with integrated AI capabilities at Build 2025")
]

# Insert Aussagen
print(f"Inserting {len(aussagen)} Aussagen for Kevin Scott (person_id={person_id})...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)

# Insert Handlungen
print(f"Inserting {len(handlungen)} Handlungen for Kevin Scott (person_id={person_id})...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)

# Commit changes
conn.commit()

# Verify insertions
cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (person_id,))
aussagen_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (person_id,))
handlungen_count = cursor.fetchone()[0]

print(f"\n[OK] Successfully inserted data for Kevin Scott:")
print(f"  - {aussagen_count} Aussagen")
print(f"  - {handlungen_count} Handlungen")
print(f"  - Total: {aussagen_count + handlungen_count} entries")

# Close connection
conn.close()

print(f"\nDatabase updated: {db_path}")
