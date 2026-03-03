import sqlite3
from datetime import datetime

# Verbindung zur Datenbank
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 82  # Martin Casado

# AUSSAGEN
aussagen = [
    {
        'aussage_text': "I'm a venture capitalist, so clearly I've got a bias, right? So I should be a voice, but I should not drive the conversation.",
        'aussage_kurz': "VCs sollten nicht die AI-Regulierungsdebatte anführen",
        'modus': 'schriftlich',
        'quell_link': "https://fortune.com/2024/12/10/a16z-martin-casado-dawn-song-ai-regulation-brainstormai/",
        'quell_titel': "a16z partner says he's tired of driving the AI regulation conversation",
        'datum_aussage': "2024-12-10",
        'sprache': 'en',
        'kontext': "After winning crusade to defeat California's AI safety bill SB 1047"
    },
    {
        'aussage_text': "If we got it wrong in social media, you can't fix it by putting it on AI. The AI regulation people, they're like, 'Oh, we got it wrong in like social, therefore we'll get it right in AI,' which is a nonsensical statement.",
        'aussage_kurz': "Social-Media-Fehler können nicht auf AI übertragen werden",
        'modus': 'schriftlich',
        'quell_link': "https://techcrunch.com/2024/11/10/a16z-vc-martin-casado-explains-why-so-many-ai-regulations-are-so-wrong/",
        'quell_titel': "a16z VC Martin Casado explains why so many AI regulations are so wrong",
        'datum_aussage': "2024-11-10",
        'sprache': 'en',
        'kontext': "On misguided AI regulation approaches"
    },
    {
        'aussage_text': "This stuff is magic. The users are real. The demand is real. The GPU usage is real.",
        'aussage_kurz': "AI ist echte Technologie mit realer Nachfrage, kein Hype",
        'modus': 'schriftlich',
        'quell_link': "https://www.dailygazette.com/tribune/andreessen-horowitz-makes-a-3-billion-bet-that-there-s-no-ai-bubble/article_de406f8c-2c6b-5ba3-b51f-0becc5a55921.html",
        'quell_titel': "Andreessen Horowitz makes a $3 billion bet that there's no AI bubble",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "On AI bubble concerns, acknowledging private valuations are crazy but rejecting bubble fears"
    },
    {
        'aussage_text': "changes the precedent for which we've dealt with software policy for 30 years. shifts liability away from applications, and applies it to infrastructure, which we've never done.",
        'aussage_kurz': "SB 1047 verschiebt Haftung auf Infrastruktur statt Anwendungen",
        'modus': 'schriftlich',
        'quell_link': "https://techcrunch.com/2024/09/02/governor-newsom-must-weigh-the-future-of-californias-ai-industry-with-sb-1047/",
        'quell_titel': "Sign or veto: What's next for California's AI disaster bill, SB 1047?",
        'datum_aussage': "2024-09-02",
        'sprache': 'en',
        'kontext': "Arguing against California's SB 1047 AI safety bill at Fight for Open Source event"
    },
    {
        'aussage_text': "If there is one thing that I learned about developing new technology it's that you can't give things away. If it's totally new, you have to sell it. People don't attach value to things that are free. That's why I became an entrepreneur.",
        'aussage_kurz': "Neue Technologie muss verkauft werden, nicht verschenkt",
        'modus': 'schriftlich',
        'quell_link': "https://www.llnl.gov/article/41011/GET",
        'quell_titel': "The accidental entrepreneur",
        'datum_aussage': "2015-01-01",
        'sprache': 'en',
        'kontext': "On lessons learned from developing OpenFlow and founding Nicira"
    },
    {
        'aussage_text': "My goal in creating Nicira was to change networking. It's very difficult to do that alone, and now I'm working with the best company in the world to make it happen.",
        'aussage_kurz': "Ziel von Nicira war es, Networking zu verändern",
        'modus': 'schriftlich',
        'quell_link': "https://www.digitalnewsasia.com/sizzle/fizzle/startup-lessons-from-openflow-creator-martin-casado",
        'quell_titel': "Startup lessons from OpenFlow creator Martin Casado",
        'datum_aussage': "2012-07-23",
        'sprache': 'en',
        'kontext': "On VMware acquisition of Nicira"
    },
    {
        'aussage_text': "China has rapidly surpassed global competitors in robotics, building a complete supply chain and innovation ecosystem that positions it as the emerging superpower in physical AI.",
        'aussage_kurz': "China dominiert Robotik und physische AI",
        'modus': 'schriftlich',
        'quell_link': "https://a16z.com/america-cannot-lose-the-robotics-race/",
        'quell_titel': "America Cannot Lose the Robotics Race",
        'datum_aussage': "2025-01-01",
        'sprache': 'en',
        'kontext': "Co-authored with Anne Neuberger, warning about US losing robotics race"
    },
    {
        'aussage_text': "In a few years, it will be Chinese companies that are making parts that we cannot replicate—not just at low cost, but at any cost.",
        'aussage_kurz': "USA wird bald chinesische Teile nicht replizieren können",
        'modus': 'schriftlich',
        'quell_link': "https://a16z.com/america-cannot-lose-the-robotics-race/",
        'quell_titel': "America Cannot Lose the Robotics Race",
        'datum_aussage': "2025-01-01",
        'sprache': 'en',
        'kontext': "Warning about China's manufacturing advantages in robotics"
    },
    {
        'aussage_text': "Chinese companies now design and fabricate precision parts like harmonic reducers at competitive quality, cheaper prices, and – most importantly – colocated with their customers in manufacturing superclusters. The colocation of so many robot toolmakers, assemblers, and customers in nodes like Shenzhen or Shanghai is how new combinatorial use cases are discovered.",
        'aussage_kurz': "Chinas Co-Location-Vorteil ermöglicht schnellere Innovation",
        'modus': 'schriftlich',
        'quell_link': "https://a16z.com/america-cannot-lose-the-robotics-race/",
        'quell_titel': "America Cannot Lose the Robotics Race",
        'datum_aussage': "2025-01-01",
        'sprache': 'en',
        'kontext': "Explaining China's structural advantages in robotics manufacturing"
    },
    {
        'aussage_text': "without urgent regulatory reform and allied industrial coordination, the United States risks losing its ability to compete in the defining technological and strategic race of the century.",
        'aussage_kurz': "USA braucht dringend Reform für Robotik-Wettbewerb",
        'modus': 'schriftlich',
        'quell_link': "https://a16z.com/america-cannot-lose-the-robotics-race/",
        'quell_titel': "America Cannot Lose the Robotics Race",
        'datum_aussage': "2025-01-01",
        'sprache': 'en',
        'kontext': "Call for US action in robotics competition"
    },
    {
        'aussage_text': "Preemptively regulating innovations in computer science in ways that can hurt open source, innovation, and competition is wrong.",
        'aussage_kurz': "Präemptive Regulierung schadet Open Source und Innovation",
        'modus': 'schriftlich',
        'quell_link': "https://x.com/martin_casado/status/1724506266985431416",
        'quell_titel': "Martin Casado on X about regulation",
        'datum_aussage': "2023-11-14",
        'sprache': 'en',
        'kontext': "Twitter/X statement on AI regulation"
    },
    {
        'aussage_text': "I think it's very important to have open source. I think it's changing the way people buy things. I think building communities like this is a very critical thing to do, but I do think it's more about go-to-market and less about innovation.",
        'aussage_kurz': "Open Source ist mehr Go-to-Market als Innovation",
        'modus': 'schriftlich',
        'quell_link': "https://siliconangle.com/2017/04/14/sdn-balancing-customer-technology-critical-says-vc-guestoftheweek/",
        'quell_titel': "Martin Casado: Here's how software-defined networking took over the industry",
        'datum_aussage': "2017-04-14",
        'sprache': 'en',
        'kontext': "On the strategic role of open source in technology"
    },
    {
        'aussage_text': "The goal is, how do you make networking have the properties of software systems as far as innovation, provisioning speed, and upgrade speed. You want networks to be as flexible and as agile as compute is.",
        'aussage_kurz': "Networking sollte so flexibel wie Software sein",
        'modus': 'schriftlich',
        'quell_link': "https://www.networkworld.com/article/2220587/openflow-inventor--network-provisioning-will-inevitably-be-automated.html",
        'quell_titel': "OpenFlow inventor: Network provisioning will inevitably be automated",
        'datum_aussage': "2012-01-01",
        'sprache': 'en',
        'kontext': "Explaining the vision behind software-defined networking"
    },
    {
        'aussage_text': "AGI debates often obscure more meaningful questions about how technology actually creates value.",
        'aussage_kurz': "AGI-Debatten verschleiern echte Wertschöpfungsfragen",
        'modus': 'schriftlich',
        'quell_link': "https://www.generalist.com/p/this-feels-like-1996-martin-casado",
        'quell_titel': "This feels like 1996: Why a16z's Martin Casado believes the AI boom still has years to run",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "Skeptical of AGI hype, characterizing discussions as lazy thinking"
    },
    {
        'aussage_text': "up to 80% of US AI startups are now using Chinese open-source models instead of those from OpenAI or Anthropic during their fundraising pitches.",
        'aussage_kurz': "80% der US-AI-Startups nutzen chinesische Open-Source-Modelle",
        'modus': 'schriftlich',
        'quell_link': "https://eu.36kr.com/en/p/3440755786126725",
        'quell_titel': "80% of US AI Startups Rely on Chinese Open-Source Models for Survival",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "Revealing Chinese dominance in open-source AI models"
    },
    {
        'aussage_text': "I think there will be less and less open source. If you ask, 'Is open source more dangerous than closed source?' the answer is yes, because China does have an edge in the open-source field.",
        'aussage_kurz': "Open Source wird weniger, China hat Vorteil darin",
        'modus': 'schriftlich',
        'quell_link': "https://www.thetwentyminutevc.com/martin-casado-2",
        'quell_titel': "Martin Casado on Anthropic vs OpenAI: Why Open Source is a National Security Risk with China",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "On security concerns around open-source AI and China"
    },
    {
        'aussage_text': "The right approach for us isn't to close off, but to further promote our own open-source efforts.",
        'aussage_kurz': "USA sollte eigene Open-Source-Bemühungen fördern",
        'modus': 'schriftlich',
        'quell_link': "https://www.interconnects.ai/p/on-chinas-open-source-ai-trajectory",
        'quell_titel': "On China's open source AI trajectory",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "Despite security concerns, advocating for American open-source investment"
    },
    {
        'aussage_text': "In the cloud era, value scaled with the number of users accessing a shared system. However, in the AI era, value shifts to the work the software performs on your behalf, automating tasks such as writing code or resolving support tickets. As a result, the old value metric of 'users' is being replaced by 'output'.",
        'aussage_kurz': "AI verschiebt Wertmetrik von Nutzern zu Output",
        'modus': 'schriftlich',
        'quell_link': "https://a16z.com/podcast/ai-is-upending-saas-pricing/",
        'quell_titel': "AI Is Upending SaaS Pricing",
        'datum_aussage': "2024-01-01",
        'sprache': 'en',
        'kontext': "Discussion with Metronome CEO about AI's impact on SaaS business models"
    }
]

# HANDLUNGEN
handlungen = [
    {
        'handlung_typ': 'gruendung',
        'beschreibung': "Co-founded Nicira Networks with Nick McKeown and Scott Shenker, developing software-defined networking technology based on OpenFlow protocol from Stanford research",
        'datum_handlung': "2007-01-01",
        'quell_link': "https://en.wikipedia.org/wiki/Nicira",
        'quell_titel': "Nicira - Wikipedia",
        'kontext': "Founded in Palo Alto after PhD work at Stanford on OpenFlow"
    },
    {
        'handlung_typ': 'verkauf',
        'beschreibung': "Nicira acquired by VMware for $1.26 billion ($1.05 billion in cash and $210 million in assumed unvested equity awards), becoming one of the largest acquisitions in networking history",
        'datum_handlung': "2012-07-23",
        'quell_link': "https://venturebeat.com/business/vmware-buys-nicira-virtualize-networking/",
        'quell_titel': "VMware buys Nicira for $1.26B, making a bid for virtualized networking",
        'kontext': "VMware acquisition to enter software-defined networking market"
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': "Joined VMware as Fellow and CTO for Networking and Security, General Manager of Networking and Security Business Unit after Nicira acquisition",
        'datum_handlung': "2012-08-01",
        'quell_link': "https://en.wikipedia.org/wiki/Martin_Casado",
        'quell_titel': "Martin Casado - Wikipedia",
        'kontext': "Leadership role at VMware following Nicira acquisition"
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': "Built VMware NSX network virtualization product to $600 million annual revenue run-rate, tripling revenue and growing to 1,200 paying customers",
        'datum_handlung': "2015-12-31",
        'quell_link': "https://www.networkworld.com/article/948636/vmware-sdn-cloud-issues-did-not-push-casado-out.html",
        'quell_titel': "VMware SDN, cloud issues did not push Casado out",
        'kontext': "Major business growth achievement at VMware before leaving"
    },
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': "Left VMware as EVP and General Manager of Networking and Security Business, stating he waited until NSX established solid footing after contemplating departure for two years",
        'datum_handlung': "2016-02-25",
        'quell_link': "https://www.theregister.com/2016/02/25/martin_cassado_leaves_vmware/",
        'quell_titel': "NSX Daddy Martin Casado leaves VMware to become a VC",
        'kontext': "Departure during turbulent period as VMware was being acquired by Dell/EMC"
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': "Joined Andreessen Horowitz as ninth General Partner to lead infrastructure investments, announced by Marc Andreessen who first met Casado in 2009",
        'datum_handlung': "2016-02-01",
        'quell_link': "https://en.wikipedia.org/wiki/Martin_Casado",
        'quell_titel': "Martin Casado - Wikipedia",
        'kontext': "Transition from operating executive to venture capital"
    },
    {
        'handlung_typ': 'lobbying',
        'beschreibung': "Led opposition against California's SB 1047 AI safety bill at Fight for Open Source event, arguing bill shifts liability to infrastructure and threatens startups, alongside a16z, Nancy Pelosi, OpenAI, and Big Tech",
        'datum_handlung': "2024-08-01",
        'quell_link': "https://techcrunch.com/2024/09/02/governor-newsom-must-weigh-the-future-of-californias-ai-industry-with-sb-1047/",
        'quell_titel': "Sign or veto: What's next for California's AI disaster bill, SB 1047?",
        'kontext': "Successful lobbying campaign; Governor Newsom vetoed bill in September 2024"
    },
    {
        'handlung_typ': 'umstrukturierung',
        'beschreibung': "Led a16z infrastructure practice with $1.25 billion dedicated fund for AI infrastructure investments, later expanded with additional $1.7 billion commitment",
        'datum_handlung': "2024-04-19",
        'quell_link': "https://techcrunch.com/2024/04/19/andreessen-horowitz-jennifer-li-125-billion-dollar-infrastructure-fund/",
        'quell_titel': "a16z promotes Jennifer Li to help lead the new $1.25B Infrastructure fund",
        'kontext': "Major infrastructure fund expansion at a16z"
    },
    {
        'handlung_typ': 'investition',
        'beschreibung': "Led a16z investment in Ideogram's $80 million Series A funding round for AI image generation technology, joining board of directors",
        'datum_handlung': "2024-02-28",
        'quell_link': "https://venturebeat.com/ai/midjourney-rival-ideogram-gets-80m-in-series-a-led-by-andreessen-horowitz",
        'quell_titel': "Midjourney rival Ideogram gets $80M in Series A led by Andreessen Horowitz",
        'kontext': "Board position and lead investor in AI image generation startup"
    },
    {
        'handlung_typ': 'investition',
        'beschreibung': "Invested in World Labs (founded by Fei-Fei Li), taking part-time residence in World Labs offices to learn from AI/graphics team and help balance research and product",
        'datum_handlung': "2024-01-01",
        'quell_link': "https://a16z.com/announcement/investing-in-world-labs/",
        'quell_titel': "What's In a World? Investing in World Labs",
        'kontext': "Hands-on involvement with World Labs, leveraging 20-year relationship with Fei-Fei Li"
    },
    {
        'handlung_typ': 'investition',
        'beschreibung': "Invested in Cursor (AI-assisted programming tool, fork of VS Code) and joined board, with a16z infrastructure team's use of Cursor instrumental in identifying investment",
        'datum_handlung': "2024-01-01",
        'quell_link': "https://www.generalist.com/p/this-feels-like-1996-martin-casado",
        'quell_titel': "This feels like 1996",
        'kontext': "Board position at Cursor, noted as potentially fastest-growing startup in history"
    },
    {
        'handlung_typ': 'investition',
        'beschreibung': "Serves on boards of 17+ portfolio companies including Ambient.ai, Astranis, Braintrust, Coactive, Convex, Distributional, Fivetran, Imply, Kong, Material Security, Netlify, Pindrop Security, Preset, Truffle Security",
        'datum_handlung': "2024-01-01",
        'quell_link': "https://a16z.com/martin-casado/",
        'quell_titel': "Martin Casado | Andreessen Horowitz",
        'kontext': "Current board portfolio as of 2024"
    },
    {
        'handlung_typ': 'investition',
        'beschreibung': "Led investments in dbt Labs (acquired by Fivetran in 2025), previously serving on board of both companies before merger",
        'datum_handlung': "2023-01-01",
        'quell_link': "https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement",
        'quell_titel': "dbt Labs + Fivetran: Open data Infrastructure for analytics and AI",
        'kontext': "Board position at both companies before they merged"
    },
    {
        'handlung_typ': 'politisch',
        'beschreibung': "Spoke with Senator Todd Young (R-IN) at a16z American Dynamism Summit about importance of open innovation and American leadership in AI, supporting AI research from classroom to war room",
        'datum_handlung': "2024-01-01",
        'quell_link': "https://a16z.com/podcast/why-america-must-lead-in-ai-investment-with-senator-young-r-in/",
        'quell_titel': "Why America Must Lead in AI Investment with Senator Young (R-IN)",
        'kontext': "Policy advocacy for American AI competitiveness"
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': "Received ACM Grace Murray Hopper Award (shared with Dina Katabi) for inventing software-defined networking (SDN), including OpenFlow API, OpenVswitch, and NOX/ONIX controllers",
        'datum_handlung': "2012-01-01",
        'quell_link': "https://awards.acm.org/award_winners/casado_9032793",
        'quell_titel': "Martin Casado - ACM Grace Murray Hopper Award",
        'kontext': "Recognition for creating SDN paradigm that changed networking field"
    }
]

# Aussagen einfügen
print(f"Füge {len(aussagen)} Aussagen für Martin Casado (person_id={person_id}) ein...")
for aussage in aussagen:
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

# Handlungen einfügen
print(f"Füge {len(handlungen)} Handlungen für Martin Casado (person_id={person_id}) ein...")
for handlung in handlungen:
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

# Commit und Schließen
conn.commit()
conn.close()

print(f"\nErfolgreich abgeschlossen!")
print(f"  - {len(aussagen)} Aussagen eingefuegt")
print(f"  - {len(handlungen)} Handlungen eingefuegt")
print(f"  - Gesamt: {len(aussagen) + len(handlungen)} Datensaetze")
