import sqlite3
from datetime import datetime

# Verbindung zur Datenbank herstellen
db_path = r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 66  # Illia Polosukhin

print("Beginne Einfügen der Daten für Illia Polosukhin (person_id=66)...")

# ==================== AUSSAGEN ====================

aussagen = [
    # 1
    {
        'aussage_text': 'AI is a really powerful force, but what we don\'t want is it to be controlled and biased by a single company. Whoever controls these models controls the biases, what gets shown or hidden, and the decisions suggested to millions of people.',
        'aussage_kurz': 'AI should not be controlled by a single company',
        'modus': 'muendlich',
        'quell_link': 'https://www.eweek.com/news/illia-polosukhin-ai-neuron-podcast-interview/',
        'quell_titel': 'AI Is Broken, Says the Creator of the Tech Behind ChatGPT',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Interview on The Neuron podcast about AI centralization concerns'
    },
    # 2
    {
        'aussage_text': 'User-owned AI optimizes for the privacy and sovereignty of users. The system\'s objective function is designed to prioritize the user\'s well-being rather than advertising metrics or revenue.',
        'aussage_kurz': 'User-owned AI prioritizes user well-being over profits',
        'modus': 'schriftlich',
        'quell_link': 'https://medium.com/nearprotocol/user-owned-ai-is-near-97d28e8002ab',
        'quell_titel': 'User-Owned AI is NEAR',
        'datum_aussage': '2024-05-22',
        'sprache': 'en',
        'kontext': 'Blog post announcing NEAR\'s vision for user-owned AI'
    },
    # 3
    {
        'aussage_text': 'The constraint is no longer just GPUs — it\'s electricity. Training and testing large-scale models requires thousands of GPUs running for days, placing major pressure on electric grids and data center infrastructure worldwide.',
        'aussage_kurz': 'Electricity is the main bottleneck for AI, not GPUs',
        'modus': 'muendlich',
        'quell_link': 'https://www.novaims.unl.pt/en/here-now/news/from-google-to-near-illia-polosukhin-argues-at-nova-that-ai-should-belong-to-its-users/',
        'quell_titel': 'From Google to Near: Illia Polosukhin argues at NOVA that AI should belong to its users',
        'datum_aussage': '2024-11-17',
        'sprache': 'en',
        'kontext': 'Confluence Conference at NOVA IMS, discussing AI infrastructure challenges'
    },
    # 4
    {
        'aussage_text': 'For me, web3 is not about decentralization. I think decentralization is just a tool. What it is about is low switching costs.',
        'aussage_kurz': 'Web3 is about low switching costs, not decentralization per se',
        'modus': 'muendlich',
        'quell_link': 'https://www.danielscrivner.com/notes/near-protocol-illia-polosukhin-spotlight-transcript',
        'quell_titel': 'NEAR Protocol – Building a High Speed, Climate Neutral, Low Fee Blockchain with Illia Polosukhin',
        'datum_aussage': '2022-01-01',
        'sprache': 'en',
        'kontext': 'Podcast interview with Daniel Scrivner explaining his philosophy on Web3'
    },
    # 5
    {
        'aussage_text': 'The open web is an internet where all people control their own assets, data, and power of governance.',
        'aussage_kurz': 'Open web means user control over assets, data, and governance',
        'modus': 'muendlich',
        'quell_link': 'https://pages.near.org/blog/ai-is-near-illia-polosukhin-on-ai-and-the-open-web-at-nearcon-23/',
        'quell_titel': 'AI is NEAR: Illia Polosukhin on AI and the Open Web at NEARCON \'23',
        'datum_aussage': '2023-11-07',
        'sprache': 'en',
        'kontext': 'NEARCON 2023 keynote in Lisbon on Day One'
    },
    # 6
    {
        'aussage_text': 'Crypto became the largest driver for humanitarian help as well as some of military help for Ukraine. It\'s resilient, it\'s fast, it delivers help directly to people.',
        'aussage_kurz': 'Crypto is the largest driver for humanitarian help to Ukraine',
        'modus': 'muendlich',
        'quell_link': 'https://decrypt.co/111242/near-protocol-founder-ukraine-has-shown-how-crypto-delivers-help-directly-to-people',
        'quell_titel': 'Near Protocol Founder: Ukraine Shows How Crypto \'Delivers Help Directly to People\'',
        'datum_aussage': '2022-11-04',
        'sprache': 'en',
        'kontext': 'Interview about crypto\'s role in Ukraine war relief efforts'
    },
    # 7
    {
        'aussage_text': 'You can create a full system, an NGO system in days. Instead of [the] months it would take to create a new nonprofit, set up banks accounts, get all the legal structure, make sure that people can wire money to it without problems.',
        'aussage_kurz': 'Crypto enables creation of NGO systems in days instead of months',
        'modus': 'muendlich',
        'quell_link': 'https://decrypt.co/111242/near-protocol-founder-ukraine-has-shown-how-crypto-delivers-help-directly-to-people',
        'quell_titel': 'Near Protocol Founder: Ukraine Shows How Crypto \'Delivers Help Directly to People\'',
        'datum_aussage': '2022-11-04',
        'sprache': 'en',
        'kontext': 'Explaining the speed advantage of crypto for humanitarian organizations'
    },
    # 8
    {
        'aussage_text': 'There was nothing decentralized or transparent about Sam Bankman-Fried\'s FTX empire. FTX\'s failure was a result of centralized mismanagement rather than an indictment of decentralized technology.',
        'aussage_kurz': 'FTX failure was due to centralization, not blockchain flaws',
        'modus': 'muendlich',
        'quell_link': 'https://www.hulkapps.com/blogs/ecommerce-hub/who-is-illia-polosukhin',
        'quell_titel': 'Who is Illia Polosukhin?',
        'datum_aussage': '2023-01-01',
        'sprache': 'en',
        'kontext': 'Commentary on FTX collapse and centralization risks'
    },
    # 9
    {
        'aussage_text': 'AI training is still "alchemy," with most AI research remaining guesswork and "change stuff until it works".',
        'aussage_kurz': 'AI training is still alchemy and guesswork',
        'modus': 'muendlich',
        'quell_link': 'https://www.eweek.com/news/illia-polosukhin-ai-neuron-podcast-interview/',
        'quell_titel': 'AI Is Broken, Says the Creator of the Tech Behind ChatGPT',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'The Neuron podcast discussing current state of AI development'
    },
    # 10
    {
        'aussage_text': 'Both sides of the market are scared — users fear giving AI access to their data, while companies fear the liability of handling that data, especially with HIPAA, IP rights, and compliance nightmares.',
        'aussage_kurz': 'Users and companies both fear AI data handling',
        'modus': 'muendlich',
        'quell_link': 'https://www.eweek.com/news/illia-polosukhin-ai-neuron-podcast-interview/',
        'quell_titel': 'AI Is Broken, Says the Creator of the Tech Behind ChatGPT',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Discussing privacy and liability concerns in AI systems'
    },
    # 11
    {
        'aussage_text': 'Your AI could be secretly programmed to convince you of opinions. As language models gain the ability to interact directly with society, they hold the potential to manipulate information on a broad scale.',
        'aussage_kurz': 'AI could manipulate users through secret programming',
        'modus': 'muendlich',
        'quell_link': 'https://www.eweek.com/news/illia-polosukhin-ai-neuron-podcast-interview/',
        'quell_titel': 'AI Is Broken, Says the Creator of the Tech Behind ChatGPT',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Warning about dystopian AI manipulation scenarios'
    },
    # 12
    {
        'aussage_text': 'People will find meaning and compete for status in small communities focused on niche interests and activities such as athletics, video games, collection & creation of unique artifacts, and who knows what else.',
        'aussage_kurz': 'In AI future, people will find meaning in niche communities',
        'modus': 'muendlich',
        'quell_link': 'https://www.cognitiverevolution.ai/a-positive-vision-for-the-future-part-2-with-illia-polosukhin-of-near/',
        'quell_titel': 'A Positive Vision for the Future: Part 2 with Illia Polosukhin of NEAR',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Cognitive Revolution podcast on future society with AI'
    },
    # 13
    {
        'aussage_text': 'Advertising and middlemen will become less relevant as AI agents allow buyers and sellers to connect directly at unprecedented scale.',
        'aussage_kurz': 'AI agents will enable direct markets, reducing middlemen',
        'modus': 'muendlich',
        'quell_link': 'https://www.cognitiverevolution.ai/a-positive-vision-for-the-future-part-2-with-illia-polosukhin-of-near/',
        'quell_titel': 'A Positive Vision for the Future: Part 2 with Illia Polosukhin of NEAR',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Discussing economic implications of AI agents'
    },
    # 14
    {
        'aussage_text': 'Humans and AIs effectively grow up together. AIs should pursue the interests of their individual humans, even if that means being less than fully transparent when negotiating with other AIs on their humans\' behalf.',
        'aussage_kurz': 'AIs should grow with humans and advocate for them',
        'modus': 'muendlich',
        'quell_link': 'https://www.cognitiverevolution.ai/a-positive-vision-for-the-future-part-2-with-illia-polosukhin-of-near/',
        'quell_titel': 'A Positive Vision for the Future: Part 2 with Illia Polosukhin of NEAR',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Vision of symbiotic human-AI relationships'
    },
    # 15
    {
        'aussage_text': 'We need is some form of community coordination and governance and incentives to continue building this in the open and de-bias it over time.',
        'aussage_kurz': 'AI needs community governance to reduce bias',
        'modus': 'muendlich',
        'quell_link': 'https://www.cognitiverevolution.ai/a-positive-vision-for-the-future-part-2-with-illia-polosukhin-of-near/',
        'quell_titel': 'A Positive Vision for the Future: Part 2 with Illia Polosukhin of NEAR',
        'datum_aussage': '2024-01-01',
        'sprache': 'en',
        'kontext': 'Discussing governance models for open AI development'
    },
    # 16
    {
        'aussage_text': 'The idea is that blockchains must be abstracted away from the user so they are not barriers to entry or participation.',
        'aussage_kurz': 'Blockchains should be invisible to users',
        'modus': 'muendlich',
        'quell_link': 'https://www.coindesk.com/opinion/2023/12/20/the-rise-of-chain-abstraction-and-end-of-blockchain-factionalism',
        'quell_titel': 'The Rise of Chain Abstraction and End of Blockchain Factionalism',
        'datum_aussage': '2023-12-20',
        'sprache': 'en',
        'kontext': 'CoinDesk article on NEAR\'s chain abstraction vision'
    },
    # 17
    {
        'aussage_text': 'As a PoS chain, NEAR is that much more energy efficient. The NEAR chain\'s energy consumption as a whole contributed to less than 1% of the entire NEAR collective\'s carbon footprint.',
        'aussage_kurz': 'NEAR blockchain uses less than 1% of team\'s carbon footprint',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/nearprotocol/sustainable-crypto-is-near-illia-polosukhin-at-the-open-web-forum-by-cogx-9afff2ce20f6',
        'quell_titel': 'Sustainable Crypto is NEAR: Illia Polosukhin at the Open Web Forum by CogX',
        'datum_aussage': '2021-11-01',
        'sprache': 'en',
        'kontext': 'CogX Open Web Forum discussion on NEAR\'s climate neutrality'
    },
    # 18
    {
        'aussage_text': 'Today\'s centralized AI ecosystem is broken. User-Owned AI is the path forward—making systems private, verifiable, and aligned with users rather than corporations.',
        'aussage_kurz': 'Centralized AI is broken, user-owned AI is the solution',
        'modus': 'schriftlich',
        'quell_link': 'https://www.cnbc.com/2024/06/27/illiapolosukhinai240624tarasovsf.html',
        'quell_titel': 'AI pioneer Illia Polosukhin, one of Google\'s \'Transformer 8,\' wants to democratize artificial intelligence',
        'datum_aussage': '2024-06-27',
        'sprache': 'en',
        'kontext': 'CNBC interview on democratizing AI'
    },
    # 19
    {
        'aussage_text': 'I firmly believed that the software would make significant progress and that software will change the entire world. The most direct way is to teach machines to write code and make programming accessible to everyone.',
        'aussage_kurz': 'Machines writing code will make programming accessible to all',
        'modus': 'muendlich',
        'quell_link': 'https://www.cnbc.com/2024/06/27/illiapolosukhinai240624tarasovsf.html',
        'quell_titel': 'AI pioneer Illia Polosukhin on inventing the tech behind generative AI at Google',
        'datum_aussage': '2024-06-27',
        'sprache': 'en',
        'kontext': 'Explaining why he left Google after publishing Transformer paper'
    },
    # 20
    {
        'aussage_text': 'AI must be open for all to participate and profit while preserving ownership and privacy of data. Blockchain technology provides a means to accomplish this, with NEAR being the only platform purpose-built to power AI at scale while preserving privacy and user ownership.',
        'aussage_kurz': 'Blockchain enables open AI with privacy and user ownership',
        'modus': 'muendlich',
        'quell_link': 'https://medium.com/nearprotocol/near-protocol-co-founder-illia-polosukhin-delivers-keynote-at-2024-hong-kong-web3-festival-on-why-4b8b8241a96a',
        'quell_titel': 'NEAR Protocol Co-Founder Illia Polosukhin Delivers Keynote at 2024 Hong Kong Web3 Festival',
        'datum_aussage': '2024-04-08',
        'sprache': 'en',
        'kontext': 'Hong Kong Web3 Festival 2024 keynote on AI and Web3 integration'
    }
]

# Aussagen einfügen
for aussage in aussagen:
    cursor.execute('''
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (person_id, aussage['aussage_text'], aussage['aussage_kurz'], aussage['modus'],
          aussage['quell_link'], aussage['quell_titel'], aussage['datum_aussage'],
          aussage['sprache'], aussage['kontext']))

print(f"{len(aussagen)} Aussagen eingefügt.")

# ==================== HANDLUNGEN ====================

handlungen = [
    # 1
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded NEAR Protocol (originally named Near.ai) with Alexander Skidanov. Initially focused on AI development and program synthesis, later evolved to provide blockchain services.',
        'datum_handlung': '2017-06-01',
        'quell_link': 'https://www.crunchbase.com/person/illia-polosukhin',
        'quell_titel': 'Illia Polosukhin - Co-founder @ NEAR - Crunchbase',
        'kontext': 'Left Google shortly after publishing Transformer paper to start NEAR'
    },
    # 2
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Launched NEAR Protocol mainnet on April 22, 2020. Genesis occurred at 18:00:00 UTC, enabling developers to deploy production apps. Network became completely community-operated in September 2020.',
        'datum_handlung': '2020-04-22',
        'quell_link': 'https://www.businesswire.com/news/home/20200504005546/en/',
        'quell_titel': 'NEAR Protocol Project Launches MainNet to Bring Open Web Business Models to Founders',
        'kontext': 'Major milestone transitioning from development to production blockchain'
    },
    # 3
    {
        'handlung_typ': 'investition',
        'beschreibung': 'NEAR Protocol raised $21.6 million in token sale led by Andreessen Horowitz (a16z), with participation from Pantera Capital, Electric Capital, Blockchange, Libertus Capital and Distributed Global.',
        'datum_handlung': '2020-05-04',
        'quell_link': 'https://www.coindesk.com/tech/2020/05/04/near-protocol-launches-following-21m-token-sale-led-by-andreessen-horowitz',
        'quell_titel': 'NEAR Protocol Launches Following $21M Token Sale Led by Andreessen Horowitz',
        'kontext': 'Major Series A funding round at mainnet launch'
    },
    # 4
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded SID Venture Partners, a Ukrainian VC fund with $15M fund size, focused on Web3/Blockchain, AI, and enterprise applications. Became General Partner with investment range $100K-$5M.',
        'datum_handlung': '2021-12-01',
        'quell_link': 'https://techukraine.org/2021/12/08/ukrainian-it-experts-established-vc-sid-venture-partners-fund-for-it-geeks/',
        'quell_titel': 'Ukrainian IT experts established VC SID Venture Partners fund',
        'kontext': 'Expanding role as investor to support blockchain and AI startups'
    },
    # 5
    {
        'handlung_typ': 'investition',
        'beschreibung': 'NEAR Protocol raised $150 million in funding round. This came less than three months before the larger Tiger Global round.',
        'datum_handlung': '2022-01-15',
        'quell_link': 'https://www.coindesk.com/business/2022/04/06/near-protocol-raises-350m',
        'quell_titel': 'Near Protocol Raises $350M',
        'kontext': 'Major funding round during crypto bull market'
    },
    # 6
    {
        'handlung_typ': 'gruendung',
        'beschreibung': 'Co-founded Unchain Fund immediately after Russian invasion of Ukraine on February 24. Created with other Ukrainian crypto entrepreneurs, raised nearly $7-10 million in crypto donations for humanitarian and military aid.',
        'datum_handlung': '2022-02-26',
        'quell_link': 'https://decrypt.co/111242/near-protocol-founder-ukraine-has-shown-how-crypto-delivers-help-directly-to-people',
        'quell_titel': 'Near Protocol Founder: Ukraine Shows How Crypto Delivers Help Directly to People',
        'kontext': 'Emergency humanitarian response using cryptocurrency infrastructure'
    },
    # 7
    {
        'handlung_typ': 'investition',
        'beschreibung': 'NEAR Protocol raised $350 million in funding round led by Tiger Global, with participation from Republic Capital, Hashed, FTX Ventures, Dragonfly Capital and others. Aimed to accelerate decentralization of NEAR ecosystem.',
        'datum_handlung': '2022-04-06',
        'quell_link': 'https://www.theblock.co/post/140751/near-protocol-raises-350-million-in-new-funding-round-led-by-tiger-global',
        'quell_titel': 'NEAR Protocol raises $350 million in new funding round led by Tiger Global',
        'kontext': 'Largest funding round for NEAR, total funding exceeded $550M'
    },
    # 8
    {
        'handlung_typ': 'einstellung',
        'beschreibung': 'Appointed CEO of NEAR Foundation on November 7, 2023. Took over leadership to oversee growth of NEAR Open Web Ecosystem and guide constellation of teams building on NEAR. Predecessor Chris Donovan became COO.',
        'datum_handlung': '2023-11-07',
        'quell_link': 'https://liberlandpress.com/2023/11/11/illia-polosukhin-co-founder-of-near-protocol-announced-as-ceo-of-near-foundation/',
        'quell_titel': 'Illia Polosukhin announced as CEO of NEAR Foundation',
        'kontext': 'Leadership transition after Marieke Flament\'s resignation in September 2023'
    },
    # 9
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'Announced User-Owned AI initiative for NEAR Protocol. Building infrastructure for decentralized AI that optimizes for privacy and user sovereignty, including DCML (Decentralized Confidential Machine Learning) technology.',
        'datum_handlung': '2024-05-22',
        'quell_link': 'https://medium.com/nearprotocol/user-owned-ai-is-near-97d28e8002ab',
        'quell_titel': 'User-Owned AI is NEAR',
        'kontext': 'Major strategic pivot combining blockchain and AI expertise'
    },
    # 10
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': 'NEAR launched Chain Signatures on mainnet, enabling multichain, non-custodial accounts. Allows users with NEAR account to sign transactions on other blockchains without cross-chain bridges.',
        'datum_handlung': '2024-08-08',
        'quell_link': 'https://www.coindesk.com/tech/2024/08/08/near-pushes-signatures-on-mainnet-in-growing-trend-of-chain-abstraction',
        'quell_titel': 'NEAR Pushes Signatures on Mainnet, in Growing Trend of Chain Abstraction',
        'kontext': 'Implementation of chain abstraction vision for cross-chain interoperability'
    },
    # 11
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': 'NEAR and Flowcarbon announced partnership to launch carbon-market ecosystem on NEAR network. Enables trading of carbon credits, advancing NEAR\'s vision of becoming carbon-negative blockchain.',
        'datum_handlung': '2022-05-01',
        'quell_link': 'https://medium.com/nearprotocol/sustainable-crypto-is-near-illia-polosukhin-at-the-open-web-forum-by-cogx-9afff2ce20f6',
        'quell_titel': 'Sustainable Crypto is NEAR',
        'kontext': 'Environmental sustainability initiative beyond Proof-of-Stake efficiency'
    },
    # 12
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Presented new AI research from NEAR AI at NVIDIA GTC 2025 in San Jose. Showcased technology to enable confidential, decentralized AI computation, providing technical basis for user-owned AI economy.',
        'datum_handlung': '2025-03-18',
        'quell_link': 'https://pages.near.org/blog/nvidia-gtc-2025/',
        'quell_titel': 'NEAR Co-Founder Illia Polosukhin Presents New AI Research at NVIDIA GTC 2025',
        'kontext': 'Major industry conference presentation on decentralized AI computing'
    },
    # 13
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Delivered keynote at Hong Kong Web3 Festival 2024 on "Why AI needs Web3". Presented choice between closed AI world controlled by few entities versus open, decentralized future powered by Web3 principles.',
        'datum_handlung': '2024-04-08',
        'quell_link': 'https://medium.com/nearprotocol/near-protocol-co-founder-illia-polosukhin-delivers-keynote-at-2024-hong-kong-web3-festival-on-why-4b8b8241a96a',
        'quell_titel': 'NEAR Protocol Co-Founder Illia Polosukhin Delivers Keynote at 2024 Hong Kong Web3 Festival',
        'kontext': 'Major Asia blockchain conference on AI-Web3 convergence'
    },
    # 14
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Delivered TED talk titled "AI should optimize your life — not companies\' profits". Described dangers of AI controlled by few tech companies and outlined how blockchain can empower individuals.',
        'datum_handlung': '2024-10-01',
        'quell_link': 'https://www.ted.com/talks/illia_polosukhin_ai_should_optimize_your_life_not_companies_profits',
        'quell_titel': 'Illia Polosukhin: AI should optimize your life — not companies\' profits | TED Talk',
        'kontext': 'TEDAI San Francisco presentation on user-owned AI vision'
    },
    # 15
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': 'Keynote at NEARCON 2023 in Lisbon on "AI and the Open Web". Discussed AI-Web3 convergence, how blockchains can help AI develop positively, and future of governance and work with AI.',
        'datum_handlung': '2023-11-07',
        'quell_link': 'https://pages.near.org/blog/ai-is-near-illia-polosukhin-on-ai-and-the-open-web-at-nearcon-23/',
        'quell_titel': 'AI is NEAR: Illia Polosukhin on AI and the Open Web at NEARCON 23',
        'kontext': 'NEAR Protocol annual conference, led special AI track'
    }
]

# Handlungen einfügen
for handlung in handlungen:
    cursor.execute('''
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (person_id, handlung['handlung_typ'], handlung['beschreibung'],
          handlung['datum_handlung'], handlung['quell_link'],
          handlung['quell_titel'], handlung['kontext']))

print(f"{len(handlungen)} Handlungen eingefügt.")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("\n" + "="*60)
print("ZUSAMMENFASSUNG")
print("="*60)
print(f"Person: Illia Polosukhin (person_id={person_id})")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Einträge")
print("="*60)
print("\nDaten erfolgreich in die Datenbank eingefügt!")
