#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datenimport für Brett Adcock (person_id=85)
Figure AI Founder/CEO, ex-Archer Aviation, ex-Vettery
"""

import sqlite3
from datetime import datetime

# Datenbankverbindung
DB_PATH = r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db'

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    person_id = 85

    # ============================================================================
    # AUSSAGEN
    # ============================================================================

    aussagen = [
        {
            'aussage_text': "We're building a new species here. A future where robots could reproduce and share knowledge with one another could be close at hand.",
            'aussage_kurz': "Building a new robotic species",
            'modus': 'muendlich',
            'quell_link': 'https://www.aol.com/articles/figure-ai-ceo-brett-adcock-040201319.html',
            'quell_titel': "Figure AI CEO Brett Adcock says the robotics company is building 'a new species'",
            'datum_aussage': '2025-10-01',
            'sprache': 'en',
            'kontext': 'Interview at Salesforce Dreamforce conference, October 2025'
        },
        {
            'aussage_text': "The home is like single-digit years away from being a place where humanoid robots can do useful work. In time, the humanoid robot will be the ultimate deployment vector for AGI.",
            'aussage_kurz': "Humanoid robots in homes within single-digit years",
            'modus': 'muendlich',
            'quell_link': 'https://time.com/7012726/brett-adcock/',
            'quell_titel': "Brett Adcock: The 100 Most Influential People in AI 2024 | TIME",
            'datum_aussage': '2024-06-01',
            'sprache': 'en',
            'kontext': 'Around the Prompt podcast, discussing timeline for home robotics'
        },
        {
            'aussage_text': "Eventually, physical labor will be optional. You'll choose to do it, or you'll ask your Figure robot to do it. The world was built for humans. So if we can create a robot that interacts with it in the same way, we can automate a huge range of tasks.",
            'aussage_kurz': "Physical labor will become optional",
            'modus': 'muendlich',
            'quell_link': 'https://time.com/7012726/brett-adcock/',
            'quell_titel': "Brett Adcock: The 100 Most Influential People in AI 2024 | TIME",
            'datum_aussage': '2024-06-01',
            'sprache': 'en',
            'kontext': 'TIME Magazine profile on most influential AI people 2024'
        },
        {
            'aussage_text': "We're in a Goldilocks scenario for AI. This is the first time in human history when this is all possible.",
            'aussage_kurz': "Goldilocks moment for AI",
            'modus': 'muendlich',
            'quell_link': 'https://time.com/7012726/brett-adcock/',
            'quell_titel': "Brett Adcock: The 100 Most Influential People in AI 2024 | TIME",
            'datum_aussage': '2024-06-01',
            'sprache': 'en',
            'kontext': 'On current opportunities in AI development'
        },
        {
            'aussage_text': "One of the things I'm excited about is self-replicating von Neumann probes in space. I think it will happen in our lifetime.",
            'aussage_kurz': "Self-replicating space probes in our lifetime",
            'modus': 'muendlich',
            'quell_link': 'https://www.aol.com/articles/figure-ai-ceo-brett-adcock-040201319.html',
            'quell_titel': "Figure AI CEO Brett Adcock says the robotics company is building 'a new species'",
            'datum_aussage': '2025-10-01',
            'sprache': 'en',
            'kontext': 'Interview at Salesforce Dreamforce conference, discussing space colonization'
        },
        {
            'aussage_text': "Most major competitors are putting out most of their content and updates tele-opt from a human.",
            'aussage_kurz': "Competitors use teleoperation",
            'modus': 'muendlich',
            'quell_link': 'https://mikekalil.com/blog/brett-adcock-vs-everyone/',
            'quell_titel': "Brett Adcock vs. Everyone: Figure CEO Targets Rivals",
            'datum_aussage': '2025-11-01',
            'sprache': 'en',
            'kontext': 'Nikhil Kamath\'s WTF podcast, November 2025, criticizing competitors'
        },
        {
            'aussage_text': "Today, I made the decision to leave our Collaboration Agreement with OpenAI. Figure made a major breakthrough on fully end-to-end robot AI, built entirely in-house. We're excited to show you in the next 30 days something no one has ever seen on a humanoid.",
            'aussage_kurz': "Leaving OpenAI partnership due to in-house breakthrough",
            'modus': 'schriftlich',
            'quell_link': 'https://x.com/adcock_brett/status/1886860098980733197',
            'quell_titel': "Brett Adcock on X announcing OpenAI partnership exit",
            'datum_aussage': '2025-02-04',
            'sprache': 'en',
            'kontext': 'X/Twitter announcement of ending OpenAI collaboration'
        },
        {
            'aussage_text': "We found that to solve embodied AI at scale in the real world, you have to vertically integrate robot AI. LLMs are getting smarter yet more commoditized. For us, LLMs have quickly become the smallest piece of the puzzle.",
            'aussage_kurz': "LLMs are smallest piece of embodied AI puzzle",
            'modus': 'schriftlich',
            'quell_link': 'https://decrypt.co/305074/figure-ai-dumps-openai-major-breakthrough-robotics',
            'quell_titel': "Figure AI Dumps OpenAI Deal After 'Major Breakthrough' in Robot Intelligence",
            'datum_aussage': '2025-02-04',
            'sprache': 'en',
            'kontext': 'Explanation for ending OpenAI partnership, emphasizing vertical integration'
        },
        {
            'aussage_text': "Figure's AI models are built entirely in-house, making external AI partnerships not just cumbersome but ultimately irrelevant to our success.",
            'aussage_kurz': "External AI partnerships irrelevant",
            'modus': 'schriftlich',
            'quell_link': 'https://www.maginative.com/article/figure-ai-ends-openai-partnership-to-focus-on-in-house-robot-intelligence/',
            'quell_titel': "Figure AI Ends OpenAI Partnership to Focus on In-House Robot Intelligence",
            'datum_aussage': '2025-02-04',
            'sprache': 'en',
            'kontext': 'Company statement on independent AI development strategy'
        },
        {
            'aussage_text': "We will see billions of humanoids on the planet in our lifetime. There could be up to 10 billion humanoids on Earth in the coming decades.",
            'aussage_kurz': "10 billion humanoids by 2040",
            'modus': 'muendlich',
            'quell_link': 'https://www.freepressjournal.in/tech/we-will-see-billions-of-humanoids-on-the-planet-in-our-lifetime-figure-ai-founder-brett-adcock-foresees-robot-revolution',
            'quell_titel': "Figure AI Founder Brett Adcock Foresees Robot Revolution",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Prediction of 10 billion humanoid robots by 2040'
        },
        {
            'aussage_text': "Rather than viewing robotics as primarily a job displacement threat, there's a huge labor crisis that's going on that's really not well reported. I want to help solve that through robots that fill gaps in the workforce rather than replacing it.",
            'aussage_kurz': "Robots solve labor crisis, not replace workers",
            'modus': 'muendlich',
            'quell_link': 'https://theaiinsider.tech/2024/04/17/brett-adcocks-figure-revolutionizes-robotics-industry-with-humanoid-machines-seeks-to-transform-workforce-dynamics/',
            'quell_titel': "Brett Adcock's Figure Revolutionizes Robotics Industry",
            'datum_aussage': '2024-04-17',
            'sprache': 'en',
            'kontext': 'Discussion on labor shortages and robotics role'
        },
        {
            'aussage_text': "I think we might see the advent of AGI [artificial general intelligence], and I think that's going to be really, really important for abundance and affordability.",
            'aussage_kurz': "AGI will bring abundance and affordability",
            'modus': 'muendlich',
            'quell_link': 'https://newatlas.com/robotics/interview-brett-adcock-humanoid/',
            'quell_titel': "Getting philosophical with future robot overlord Brett Adcock",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Philosophical discussion on AGI and future society'
        },
        {
            'aussage_text': "Humanoid robotics is the next major technological revolution, a paradigm shift as profound as the advent of the internet itself.",
            'aussage_kurz': "Humanoid robotics as revolutionary as internet",
            'modus': 'schriftlich',
            'quell_link': 'https://onlinequeso.com/de/blogs/trending-today/the-future-of-humanoid-robots-an-insight-into-brett-adcocks-vision',
            'quell_titel': "The Future of Humanoid Robots: An Insight into Brett Adcock's Vision",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Comparing humanoid robotics revolution to internet revolution'
        },
        {
            'aussage_text': "Figure will not teleoperate robots in the market. Products will only launch at scale when they are fully autonomous.",
            'aussage_kurz': "No teleoperation, only full autonomy",
            'modus': 'schriftlich',
            'quell_link': 'https://onlinequeso.com/de/blogs/trending-today/the-future-of-humanoid-robots-an-insight-into-brett-adcocks-vision',
            'quell_titel': "The Future of Humanoid Robots: An Insight into Brett Adcock's Vision",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Company policy against teleoperation, commitment to autonomy'
        },
        {
            'aussage_text': "I envision robots becoming companions with infinite context window for memory, capable of understanding emotional states from voice tone alone.",
            'aussage_kurz': "Robots as emotionally intelligent companions",
            'modus': 'muendlich',
            'quell_link': 'https://onlinequeso.com/de/blogs/trending-today/the-future-of-humanoid-robots-an-insight-into-brett-adcocks-vision',
            'quell_titel': "The Future of Humanoid Robots: An Insight into Brett Adock's Vision",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Vision of home robotics with emotional AI capabilities'
        },
        {
            'aussage_text': "I envision a world where humanoids handle 50% of global labor—repairing infrastructure, building homes, even wiping toddlers' noses.",
            'aussage_kurz': "Humanoids handling 50% of global labor",
            'modus': 'muendlich',
            'quell_link': 'https://newatlas.com/robotics/interview-brett-adcock-humanoid/',
            'quell_titel': "Getting philosophical with future robot overlord Brett Adcock",
            'datum_aussage': '2024-01-01',
            'sprache': 'en',
            'kontext': 'Vision of extensive robot integration in daily life'
        },
        {
            'aussage_text': "We're building human-centric AI that can think proactively, recursively improve, and care deeply about people.",
            'aussage_kurz': "Human-centric AI that cares",
            'modus': 'schriftlich',
            'quell_link': 'https://www.theinformation.com/briefings/exclusive-figure-ceo-brett-adcock-launches-new-ai-lab-100-million-funding',
            'quell_titel': "Figure CEO Brett Adcock Launches New AI Lab With $100 Million",
            'datum_aussage': '2025-12-01',
            'sprache': 'en',
            'kontext': 'Announcement of Hark AI lab mission statement'
        },
        {
            'aussage_text': "Robots where they can build themselves, mine methane on different planets, and create more of themselves to colonize the galaxy. I believe this will happen in our lifetime.",
            'aussage_kurz': "Self-replicating robots colonizing galaxy in our lifetime",
            'modus': 'muendlich',
            'quell_link': 'https://www.aol.com/articles/figure-ai-ceo-brett-adcock-040201319.html',
            'quell_titel': "Figure AI CEO Brett Adcock says the robotics company is building 'a new species'",
            'datum_aussage': '2025-10-01',
            'sprache': 'en',
            'kontext': 'Discussing space colonization through self-replicating robots'
        }
    ]

    # ============================================================================
    # HANDLUNGEN
    # ============================================================================

    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-founded Vettery, a talent marketplace matching job seekers with employers needing technical expertise',
            'datum_handlung': '2013-01-01',
            'quell_link': 'https://foundingjourney.com/p/tfj-brett-adcock',
            'quell_titel': "Brett Adcock's Journey: Acquisition to IPO",
            'kontext': 'First major startup, scaled to 300 employees and 20,000 customers'
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Sold Vettery to Adecco Group for $100 million',
            'datum_handlung': '2018-02-20',
            'quell_link': 'https://techcrunch.com/2018/02/20/adecco-acquires-vettery/',
            'quell_titel': "Adecco Group acquires recruiting startup Vettery for $100M",
            'kontext': 'Exit from first major company after scaling to significant revenue'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-founded Archer Aviation, an eVTOL (electric vertical takeoff and landing) aircraft company',
            'datum_handlung': '2018-10-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Brett_Adcock',
            'quell_titel': "Brett Adcock - Wikipedia",
            'kontext': 'Founded with Adam Goldstein, emerged from stealth in 2020'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Secured $1 billion investment from United Airlines for Archer Aviation urban air mobility services',
            'datum_handlung': '2021-02-01',
            'quell_link': 'https://foundingjourney.com/p/tfj-brett-adcock',
            'quell_titel': "Brett Adcock's Journey: Acquisition to IPO",
            'kontext': 'United Airlines committed to urban airport service using Archer aircraft'
        },
        {
            'handlung_typ': 'ruecktritt',
            'beschreibung': 'Stepped down from co-CEO role at Archer Aviation, leaving Adam Goldstein as sole CEO',
            'datum_handlung': '2021-04-01',
            'quell_link': 'https://verticalmag.com/news/archer-brett-adcock-steps-down-co-ceo/',
            'quell_titel': "Archer's Brett Adcock steps down as co-CEO",
            'kontext': 'Transitioned away from Archer to pursue new ventures'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Took Archer Aviation public on NYSE with $2.7 billion valuation and $860 million cash proceeds',
            'datum_handlung': '2021-09-01',
            'quell_link': 'https://foundingjourney.com/p/tfj-brett-adcock',
            'quell_titel': "Brett Adcock's Journey: Acquisition to IPO",
            'kontext': 'Successfully completed SPAC merger and public listing'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Founded Figure AI, artificial intelligence startup developing general-purpose humanoid robots',
            'datum_handlung': '2022-05-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Brett_Adcock',
            'quell_titel': "Brett Adcock - Wikipedia",
            'kontext': 'Based in Sunnyvale, focused on humanoid robotics for labor markets'
        },
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Assembled Figure AI team from Boston Dynamics, Tesla, Google DeepMind and Apple engineers',
            'datum_handlung': '2022-06-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Figure_AI',
            'quell_titel': "Figure AI - Wikipedia",
            'kontext': 'Built world-class robotics and AI engineering team'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Secured $70 million Series A funding led by Parkway Venture Capital at $500 million valuation',
            'datum_handlung': '2023-05-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Figure_AI',
            'quell_titel': "Figure AI - Wikipedia",
            'kontext': 'First major funding round for Figure AI'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Figure 01 robot took first walking steps, achieving milestone in less than one year from company inception',
            'datum_handlung': '2023-05-01',
            'quell_link': 'https://www.linkedin.com/posts/brettadcock_excited-to-share-that-figure-01-robot-took-activity-7086695375130030081-v3Qs',
            'quell_titel': "Brett Adcock on LinkedIn: Figure 01 first steps",
            'kontext': 'Major technical milestone demonstrating rapid development'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Announced commercial agreement with BMW Manufacturing to deploy humanoid robots in automotive production',
            'datum_handlung': '2024-01-01',
            'quell_link': 'https://www.prnewswire.com/news-releases/figure-announces-commercial-agreement-with-bmw-manufacturing-to-bring-general-purpose-robots-into-automotive-production-302036263.html',
            'quell_titel': "Figure announces commercial agreement with BMW Manufacturing",
            'kontext': 'First major commercial deployment at BMW Spartanburg facility'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Raised $675 million Series B funding at $2.6 billion valuation from Microsoft, OpenAI, NVIDIA, Amazon, Intel Capital, Jeff Bezos',
            'datum_handlung': '2024-02-01',
            'quell_link': 'https://www.linkedin.com/posts/brettadcock_excited-to-share-figure-raises-675m-at-activity-7168968916403208192-CqAw',
            'quell_titel': "Brett Adcock on LinkedIn: Figure raises $675M",
            'kontext': 'Major funding round with top tech investors and OpenAI partnership'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Unveiled Figure 02, second-generation robot with upgraded hardware, 16-joint hands, enhanced sensors',
            'datum_handlung': '2024-08-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Figure_AI',
            'quell_titel': "Figure AI - Wikipedia",
            'kontext': 'Second generation humanoid with improved dexterity and computing'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Delivered first robots to commercial client, transitioning from research to deployment',
            'datum_handlung': '2024-12-01',
            'quell_link': 'https://www.humanoidsdaily.com/feed/figure-ai-at-three-a-look-back-at-the-humanoid-startups-rapid-ascent',
            'quell_titel': "Figure AI at Three: A Look Back at the Humanoid Startup's Rapid Ascent",
            'kontext': 'Important milestone marking commercial deployment phase'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Terminated collaboration agreement with OpenAI, citing in-house breakthrough in end-to-end robot AI',
            'datum_handlung': '2025-02-04',
            'quell_link': 'https://x.com/adcock_brett/status/1886860098980733197',
            'quell_titel': "Brett Adcock on X: OpenAI partnership exit",
            'kontext': 'Strategic pivot to fully vertically integrated AI development'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Closed Series C funding exceeding $1 billion at $39 billion post-money valuation (15x increase in 18 months)',
            'datum_handlung': '2025-09-01',
            'quell_link': 'https://www.humanoidsdaily.com/feed/figure-ai-at-three-a-look-back-at-the-humanoid-startups-rapid-ascent',
            'quell_titel': "Figure AI at Three: A Look Back at the Humanoid Startup's Rapid Ascent",
            'kontext': 'Massive valuation increase reflecting rapid progress and market interest'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Unveiled Figure 03, third-generation humanoid robot redesigned for mass manufacturing and home environments',
            'datum_handlung': '2025-10-09',
            'quell_link': 'https://www.humanoidsdaily.com/feed/figure-ai-at-three-a-look-back-at-the-humanoid-startups-rapid-ascent',
            'quell_titel': "Figure AI at Three: A Look Back at the Humanoid Startup's Rapid Ascent",
            'kontext': 'Named TIME Magazine best invention 2025, optimized for affordability'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Launched Hark AI lab with $100 million personal funding to build human-centric AI, hired 30+ engineers from Apple, Meta, Amazon',
            'datum_handlung': '2025-12-01',
            'quell_link': 'https://www.theinformation.com/briefings/exclusive-figure-ceo-brett-adcock-launches-new-ai-lab-100-million-funding',
            'quell_titel': "Exclusive: Figure CEO Brett Adcock Launches New AI Lab With $100 Million",
            'kontext': 'Self-funded new venture while remaining CEO of Figure AI'
        }
    ]

    # ============================================================================
    # DATEN EINFÜGEN
    # ============================================================================

    print(f"Füge {len(aussagen)} Aussagen für Brett Adcock (person_id={person_id}) ein...")

    for aussage in aussagen:
        cursor.execute('''
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
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

    print(f"Füge {len(handlungen)} Handlungen für Brett Adcock (person_id={person_id}) ein...")

    for handlung in handlungen:
        cursor.execute('''
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            person_id,
            handlung['handlung_typ'],
            handlung['beschreibung'],
            handlung['datum_handlung'],
            handlung['quell_link'],
            handlung['quell_titel'],
            handlung['kontext']
        ))

    # Änderungen speichern
    conn.commit()

    # Überprüfung
    cursor.execute('SELECT COUNT(*) FROM aussagen WHERE person_id = ?', (person_id,))
    aussagen_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM handlungen WHERE person_id = ?', (person_id,))
    handlungen_count = cursor.fetchone()[0]

    print(f"\nErfolgreich eingefuegt:")
    print(f"  - {aussagen_count} Aussagen")
    print(f"  - {handlungen_count} Handlungen")
    print(f"  - Gesamt: {aussagen_count + handlungen_count} Datensaetze")

    conn.close()

if __name__ == '__main__':
    insert_data()
