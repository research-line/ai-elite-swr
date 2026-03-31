#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clay Bavor (person_id=77) - Datensammlung für Forschungsdatenbank
Weltbilder von KI/Silicon-Valley-Persönlichkeiten
"""

import sqlite3
from datetime import datetime

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person ID
PERSON_ID = 77

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # AUSSAGEN (20 Stück)
    aussagen = [
        # 1
        (PERSON_ID,
         "Over the past several decades, every time people made computers work more like we do—every time we removed a layer of abstraction between us and them—computers became more broadly accessible, useful, and valuable to us, and in turn, we became more capable and productive.",
         "Removing abstraction layers makes computing more accessible and valuable",
         "schriftlich",
         "https://medium.com/@claybavor/virtual-and-augmented-realities-asking-the-right-questions-and-traveling-the-path-ahead-2428b9d13c01",
         "Virtual and Augmented Realities: Asking the right questions",
         "2017-05-01",
         "en",
         "Medium essay on VR/AR and computing interfaces"),

        # 2
        (PERSON_ID,
         "Immersive computing will remove more of the abstractions between us and our computers. You'll have access to information in context, with computing woven seamlessly into your environment. It's the inevitable next step in the arc of computing interfaces.",
         "Immersive computing is the inevitable next step in interface evolution",
         "schriftlich",
         "https://medium.com/@claybavor/virtual-and-augmented-realities-asking-the-right-questions-and-traveling-the-path-ahead-2428b9d13c01",
         "Virtual and Augmented Realities: Asking the right questions",
         "2017-05-01",
         "en",
         "Medium essay on VR/AR future"),

        # 3
        (PERSON_ID,
         "I am an emphatic believer in the long term promise of VR, AR and all things as I call them 'Immersive Computing.' It is very clearly to me and to us more broadly at Google part of the next phase of computing — computing that makes use of our environment, that vastly increases the richness of input and output — that's going to be important.",
         "VR/AR as 'Immersive Computing' is next phase of computing",
         "muendlich",
         "https://www.uploadvr.com/google-clay-bavor-vr-ar-long-term/",
         "Google VR/AR Boss Confirms Commitment",
         "2017-06-01",
         "en",
         "Interview on Google's VR/AR strategy"),

        # 4
        (PERSON_ID,
         "In time, these points on the spectrum will blur: we'll have AR headsets that can augment your whole field of view, and VR headsets which can pull in photo-realistic digital representations of your environment, and devices in between which do a bit of both. Once the technology progresses to this point, the distinction between VR and AR will be far less relevant than it is today.",
         "VR and AR will converge into unified immersive computing spectrum",
         "schriftlich",
         "https://medium.com/@claybavor/virtual-and-augmented-realities-asking-the-right-questions-and-traveling-the-path-ahead-2428b9d13c01",
         "Virtual and Augmented Realities: Asking the right questions",
         "2017-05-01",
         "en",
         "Medium essay on VR/AR convergence"),

        # 5
        (PERSON_ID,
         "AI is first and foremost about creating exceptional customer experiences.",
         "AI is primarily about exceptional customer experiences",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "Sequoia Capital podcast on AI agents"),

        # 6
        (PERSON_ID,
         "Technology magnifies whatever it touches. Bad processes get worse; great ones become exceptional.",
         "Technology amplifies existing processes for better or worse",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "On technology's amplifying effect"),

        # 7
        (PERSON_ID,
         "The number one predictor of a high customer satisfaction interaction in service is low effort. People talk about delight and surprise, sure, but in Maslow's hierarchy of experiential needs: could you please just solve my problem quickly and fully, without me having to spell my last name for the fifth time?",
         "Low effort is the primary predictor of customer satisfaction",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "Sequoia podcast on customer experience design"),

        # 8
        (PERSON_ID,
         "If in 1995 you needed a web site, in 2025 you'll need an AI agent.",
         "AI agents will be as essential as websites",
         "muendlich",
         "https://www.acquired.fm/episodes/how-is-ai-different-than-other-technology-waves-with-bret-taylor-and-clay-bavor",
         "How is AI Different Than Other Technology Waves?",
         "2024-10-01",
         "en",
         "Acquired podcast with Bret Taylor"),

        # 9
        (PERSON_ID,
         "In the future, your AI agent will be more important than your website and more important than your app. It will be the main way you interact with your customers.",
         "AI agents will surpass websites and apps in importance",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "On strategic importance of AI agents"),

        # 10
        (PERSON_ID,
         "With new technologies, people overestimate impact in the short run and underestimate impact in the long run.",
         "People misjudge technology impact timelines",
         "muendlich",
         "https://www.acquired.fm/episodes/how-is-ai-different-than-other-technology-waves-with-bret-taylor-and-clay-bavor",
         "How is AI Different Than Other Technology Waves?",
         "2024-10-01",
         "en",
         "Acquired podcast on technology adoption"),

        # 11
        (PERSON_ID,
         "We're at the cusp of something that we will, in five years, have a very different market on the internet.",
         "The internet market will transform dramatically within five years",
         "muendlich",
         "https://www.acquired.fm/episodes/how-is-ai-different-than-other-technology-waves-with-bret-taylor-and-clay-bavor",
         "How is AI Different Than Other Technology Waves?",
         "2024-10-01",
         "en",
         "Acquired podcast on AI's market impact"),

        # 12
        (PERSON_ID,
         "Recent advances in AI represent a sea change in technology that we think will enable some fundamentally new and better experiences.",
         "AI represents a fundamental technological sea change",
         "schriftlich",
         "https://fortune.com/2024/02/13/bret-taylor-clay-bavor-ai-startup-sierra-110-million-funding-sequoia-benchmark/",
         "Ex-Salesforce Co-CEO Bret Taylor launches AI startup Sierra",
         "2024-02-13",
         "en",
         "Sierra launch announcement"),

        # 13
        (PERSON_ID,
         "The AI version of your company...may dwarf all of those [website, mobile app platforms] in terms of their importance to your brand.",
         "AI representation will eclipse traditional digital presences",
         "muendlich",
         "https://www.acquired.fm/episodes/how-is-ai-different-than-other-technology-waves-with-bret-taylor-and-clay-bavor",
         "How is AI Different Than Other Technology Waves?",
         "2024-10-01",
         "en",
         "Acquired podcast on brand representation"),

        # 14
        (PERSON_ID,
         "Putting AI in front of customers is first and foremost, a product design and an experience design problem.",
         "AI deployment is primarily a design challenge",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "Sequoia podcast on AI design"),

        # 15
        (PERSON_ID,
         "It's possible to build a couch by going to Home Depot and buying lumber and cushions and fabric and putting it together yourself.",
         "Building AI agents yourself is inefficient compared to full-service solutions",
         "muendlich",
         "https://fortune.com/2024/02/13/bret-taylor-clay-bavor-ai-startup-sierra-110-million-funding-sequoia-benchmark/",
         "Ex-Salesforce Co-CEO Bret Taylor launches AI startup Sierra",
         "2024-02-13",
         "en",
         "Metaphor explaining Sierra's business model"),

        # 16
        (PERSON_ID,
         "In the age of conversational AI, the best customer experience is not installing an app or clicking a link, but simply having a conversation.",
         "Conversation is the ultimate customer experience interface",
         "schriftlich",
         "https://siliconangle.com/2024/02/13/sierra-announces-launch-conversational-ai-platform-customer-service/",
         "Sierra announces launch of conversational AI platform",
         "2024-02-13",
         "en",
         "Sierra launch announcement"),

        # 17
        (PERSON_ID,
         "I like to call it immersive computing to sidestep some of the jargon and acronym debate — VR, AR, MR — just everything.",
         "Immersive computing transcends VR/AR/MR categorization",
         "muendlich",
         "http://voicesofvr.com/584-googles-clay-bavor-on-ambient-computing-conversational-interfaces-ar-vr-strategy/",
         "Google's Clay Bavor on Ambient Computing",
         "2017-08-01",
         "en",
         "Voices of VR podcast"),

        # 18
        (PERSON_ID,
         "Technology creates possibility, creativity creates value.",
         "Creativity transforms technological possibilities into value",
         "schriftlich",
         "https://blog.google/perspectives/clay-bavor/virtual-and-augmented-realities-asking-right-questions-and-traveling-path-ahead/",
         "Virtual and augmented realities",
         "2017-05-01",
         "en",
         "Quoting Sir John Hegarty in Google blog post"),

        # 19
        (PERSON_ID,
         "Companies need to capture their brand voice, values and internal processes to create AI agents that truly represent the business.",
         "AI agents must embody company brand and values",
         "muendlich",
         "https://sequoiacap.com/podcast/training-data-clay-bavor/",
         "Sierra's Clay Bavor on Delightful Customer-Facing AI Agents",
         "2024-11-01",
         "en",
         "Sequoia podcast on AI agent authenticity"),

        # 20
        (PERSON_ID,
         "Zero percent of the world knows about VR.",
         "VR awareness is practically non-existent globally",
         "muendlich",
         "https://www.trustedreviews.com/news/google-s-clay-bavor-zero-percent-of-the-world-know-about-vr-2938143",
         "Google's Clay Bavor: 'Zero percent of the world' knows about VR",
         "2016-11-01",
         "en",
         "Interview on VR adoption challenges"),
    ]

    # HANDLUNGEN (15 Stück)
    handlungen = [
        # 1
        (PERSON_ID,
         "gruendung",
         "Co-founded Sierra, a conversational AI platform for businesses, with Bret Taylor after 18 years at Google",
         "2023-03-01",
         "https://www.cnbc.com/2023/02/08/google-s-clay-bavor-for-ai-startup-with-ex-salesforce-ceo-bret-taylor.html",
         "Google's Clay Bavor for AI startup with ex-Salesforce CEO Bret Taylor",
         "Left Google Labs VP role to start AI company focused on customer-facing AI agents"),

        # 2
        (PERSON_ID,
         "ruecktritt",
         "Announced departure from Google after 18 years, leaving VP of Labs position in March 2023",
         "2023-02-08",
         "https://9to5google.com/2023/02/08/google-ar-head-clay-bavor-leaving-the-company-after-18-years/",
         "Google AR head Clay Bavor leaving the company after 18 years",
         "Left to co-found Sierra with Bret Taylor; no replacement planned for Labs role"),

        # 3
        (PERSON_ID,
         "investition",
         "Raised $110 million Series A funding for Sierra from Sequoia Capital and Benchmark at ~$1 billion valuation",
         "2024-02-13",
         "https://fortune.com/2024/02/13/bret-taylor-clay-bavor-ai-startup-sierra-110-million-funding-sequoia-benchmark/",
         "Ex-Salesforce Co-CEO Bret Taylor launches AI startup Sierra",
         "Initial funding round with Ravi Gupta (Sequoia) and Peter Fenton (Benchmark) joining board"),

        # 4
        (PERSON_ID,
         "produktlaunch",
         "Launched Sierra conversational AI platform publicly with early customers including WeightWatchers, SiriusXM, Sonos, OluKai",
         "2024-02-13",
         "https://siliconangle.com/2024/02/13/sierra-announces-launch-conversational-ai-platform-customer-service/",
         "Sierra announces launch of conversational AI platform",
         "Platform enables companies to build customer-facing AI agents for service and recommendations"),

        # 5
        (PERSON_ID,
         "investition",
         "Raised $175 million Series B funding led by Greenoaks Capital at $4.5 billion valuation",
         "2024-10-28",
         "https://www.cnbc.com/2024/10/28/bret-taylors-ai-startup-sierra-valued-at-4point5-billion-in-funding.html",
         "Bret Taylor's AI startup Sierra valued at $4.5 billion",
         "Round included Thrive Capital and Iconiq; reached $20M+ ARR"),

        # 6
        (PERSON_ID,
         "investition",
         "Raised $350 million Series C funding led by Greenoaks at $10 billion valuation",
         "2025-09-04",
         "https://techcrunch.com/2025/09/04/bret-taylors-sierra-raises-350m-at-10b-valuation/",
         "Bret Taylor's Sierra raises $350M at a $10B valuation",
         "Reached $100M ARR milestone in 7 quarters, one of fastest-growing enterprise companies"),

        # 7
        (PERSON_ID,
         "produktlaunch",
         "Launched Google Daydream VR platform and Daydream View headset at Google I/O 2016",
         "2016-05-18",
         "https://blog.google/products-and-platforms/products/google-ar-vr/daydream-bringing-high-quality-vr-everyone/",
         "Daydream: Bringing high-quality VR to everyone",
         "Mobile VR platform for Android with $79 headset and motion controller"),

        # 8
        (PERSON_ID,
         "umstrukturierung",
         "Led creation of new Google Labs division consolidating AR/VR, Project Starline, and Area 120 incubator",
         "2021-11-11",
         "https://techcrunch.com/2021/11/11/google-reorg-moves-ar-vr-starline-and-area-120-into-new-labs-team-reporting-directly-to-sundar-pichai/",
         "Google reorg moves AR, VR, Starline and Area 120 into new 'Labs' team",
         "Appointed VP of Labs reporting directly to CEO Sundar Pichai, focusing on long-term high-potential projects"),

        # 9
        (PERSON_ID,
         "partnerschaft",
         "Established Sierra partnerships with WeightWatchers, achieving 70% automated resolution rate with 4.6/5 customer satisfaction",
         "2024-02-13",
         "https://fortune.com/2024/02/13/bret-taylor-clay-bavor-ai-startup-sierra-110-million-funding-sequoia-benchmark/",
         "Ex-Salesforce Co-CEO Bret Taylor launches AI startup Sierra",
         "WeightWatchers AI agent assists with meal choices, weight loss, and membership management"),

        # 10
        (PERSON_ID,
         "partnerschaft",
         "Launched Sierra AI agents for Sonos, SiriusXM, OluKai as design partners for conversational AI platform",
         "2024-02-13",
         "https://siliconangle.com/2024/02/13/sierra-announces-launch-conversational-ai-platform-customer-service/",
         "Sierra announces launch of conversational AI platform",
         "Early partnerships demonstrating enterprise AI agent capabilities"),

        # 11
        (PERSON_ID,
         "produktlaunch",
         "Led development and launch of Project Starline, Google's holographic videoconferencing technology",
         "2021-05-01",
         "https://www.roadtovr.com/google-labs-ar-vr-starline-area-120/",
         "Google's New 'Labs' Team Brings AR/VR, Project Starline",
         "Ultra-high-resolution 3D video chat booth under Google Labs"),

        # 12
        (PERSON_ID,
         "produktlaunch",
         "Oversaw development and launch of Google Lens visual search technology",
         "2017-05-01",
         "https://9to5google.com/2023/02/08/google-ar-head-clay-bavor-leaving-the-company-after-18-years/",
         "Google AR head Clay Bavor leaving",
         "Led Google Lens as part of AR/VR efforts before Labs reorganization"),

        # 13
        (PERSON_ID,
         "umstrukturierung",
         "Led product management and design for Gmail, Google Drive, Google Docs, and Google Apps for Enterprise (Workspace)",
         "2013-01-01",
         "https://www.claybavor.com/about",
         "About — Clay Bavor",
         "VP of Product Management overseeing tools used by billions before moving to VR/AR"),

        # 14
        (PERSON_ID,
         "partnerschaft",
         "Announced partnership with IMAX to develop cinema-grade 360-degree VR camera at Google I/O 2016",
         "2016-05-18",
         "https://singjupost.com/google-io-2016-keynote-full-transcript/",
         "Google I/O 2016 Keynote Full Transcript",
         "Upgraded Jump camera rig for high-quality cinema VR content production"),

        # 15
        (PERSON_ID,
         "gruendung",
         "Started first business in second grade selling Japanese candies, and website design company at age 13",
         "1995-01-01",
         "https://www.linkedin.com/posts/claybavor_i-started-my-first-business-in-second-grade-activity-7029166849497989120-YHsI",
         "Clay Bavor LinkedIn post",
         "Early entrepreneurial ventures before Princeton and Google career"),
    ]

    # Insert Aussagen
    print(f"Inserting {len(aussagen)} Aussagen for Clay Bavor (person_id={PERSON_ID})...")
    cursor.executemany("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussagen)

    # Insert Handlungen
    print(f"Inserting {len(handlungen)} Handlungen for Clay Bavor (person_id={PERSON_ID})...")
    cursor.executemany("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlungen)

    conn.commit()
    conn.close()

    print(f"\nSuccessfully inserted:")
    print(f"  - {len(aussagen)} Aussagen")
    print(f"  - {len(handlungen)} Handlungen")
    print(f"  - Total: {len(aussagen) + len(handlungen)} entries for Clay Bavor (person_id={PERSON_ID})")

if __name__ == "__main__":
    insert_data()
