import sqlite3
from datetime import datetime

# Datenbankverbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 83  # Daphne Koller

# AUSSAGEN - 18 Aussagen
aussagen = [
    # AI und Technologie
    (person_id, "AI can solve really hard, aspirational problems, that people maybe are not capable of solving such as health, agriculture and climate change.",
     "AI can solve problems humans cannot", "muendlich", "https://www.weforum.org/stories/2024/01/artificial-intelligence-ai-innovation-technology-davos-2024/",
     "AI at Davos 2024", "2024-01-01", "en", "Davos 2024 discussion on AI potential"),

    (person_id, "What we're doing is really hard—intervening in human biology in a way that is both safe and efficacious. So it's important to not make extravagant promises that are just not the right ones for this space.",
     "Avoid extravagant AI promises in biotech", "schriftlich", "https://sfbn.org/san-francisco-biotech-news/2024/04/01/insitro-ceo-daphne-koller-on-potentially-destructive-ai-hype-nvidia-chips-and-biotechs-data-problem/",
     "Insitro CEO on AI hype", "2024-04-01", "en", "Warning about potentially destructive AI hype in biotech"),

    (person_id, "the future is in a partnership between the human and the machine",
     "Future is human-machine partnership", "schriftlich", "https://fortune.com/2025/07/09/leadership-next-daphne-koller-insitro-coursera/",
     "Leadership Next - Fortune", "2025-07-09", "en", "Vision for future of AI and human collaboration"),

    (person_id, "AI is a fundamental technology that enables us to use computers to solve problems that are so hard that we don't know how to solve ourselves.",
     "AI enables solving unknowable problems", "schriftlich", "https://www.technovation.org/blogs/machine-learning-and-medicine-an-interview-with-daphne-koller/",
     "Machine Learning and Medicine Interview", None, "en", "Definition of AI's fundamental purpose"),

    (person_id, "machine learning technology will have significant impact and is not a niche technology. It will be used in every place, with value limited primarily by imagination of where it can be deployed.",
     "ML will be used everywhere", "schriftlich", "https://www.mckinsey.com/industries/life-sciences/our-insights/it-will-be-a-paradigm-shift-daphne-koller-on-machine-learning-in-drug-discovery",
     "McKinsey: Paradigm shift in drug discovery", None, "en", "On ubiquity of machine learning technology"),

    (person_id, "While you cannot stop the advance of technology, restricting problematic use cases of technology and regulating it is something that deserves more thought to prevent harmful applications.",
     "Cannot stop tech but must regulate it", "schriftlich", "https://schneppat.com/daphne-koller.html",
     "Daphne Koller & AI", None, "en", "On AI regulation and ethics"),

    (person_id, "It is critical that we as a society teach our kids the right set of skills that they can leverage technology in the right way.",
     "Must teach kids right tech skills", "schriftlich", "https://quotlr.com/author/daphne-koller",
     "Daphne Koller Quotes", None, "en", "On education and technology literacy"),

    (person_id, "AI's power lies in amplifying human potential, not replacing it.",
     "AI amplifies, not replaces humans", "schriftlich", "https://www.brainyquote.com/authors/daphne-koller-quotes",
     "Daphne Koller Quotes", None, "en", "Core philosophy on AI and human potential"),

    # Bildung und Wissen
    (person_id, "I would like to make it so that education was a right, and not a privilege.",
     "Education as right not privilege", "schriftlich", "https://quotlr.com/author/daphne-koller",
     "Daphne Koller Quotes", None, "en", "Vision for democratizing education"),

    (person_id, "We should spend less time at universities filling our students' minds with content by lecturing at them, and more time igniting their creativity ... by actually talking with them.",
     "Ignite creativity not fill minds", "schriftlich", "https://quotlr.com/author/daphne-koller",
     "Daphne Koller Quotes", None, "en", "Educational philosophy on active learning"),

    (person_id, "The mind is not a vessel that needs filling, but wood that needs igniting.",
     "Mind needs igniting not filling", "schriftlich", "https://mindbursts.com/2013/02/17/daphne-koller-what-were-learning-about-learning-online/",
     "What we're learning about learning online", "2013-02-17", "en", "Quoting Plutarch on learning philosophy"),

    (person_id, "As a society, we can and should invest more money in education.",
     "Society should invest more in education", "schriftlich", "https://www.brainyquote.com/authors/daphne-koller-quotes",
     "Daphne Koller Quotes", None, "en", "Call for societal investment in education"),

    (person_id, "There are so many people around the world in need of high-quality education and really starving for education.",
     "People starving for education worldwide", "schriftlich", "https://www.educationandcareernews.com/online-education/coursera-co-founder-daphne-koller-talks-about-why-online-education-is-so-important/",
     "Why Online Education Is So Important", None, "en", "On global education inequality"),

    # Drug Discovery und Biologie
    (person_id, "machine learning, trained on massive, carefully generated biological datasets, can uncover patterns in disease biology that humans simply cannot see – and in doing so, dramatically increase the odds of finding drugs that actually work.",
     "ML finds patterns humans cannot see", "schriftlich", "https://biz.bio/innovation/daphne-koller-turns-ai-into-a-drug-discovery-engine/",
     "Daphne Koller Turns AI into Drug Discovery Engine", None, "en", "Core premise of insitro's approach"),

    (person_id, "Disease is often defined by coarse-grained symptomatic manifestations, some of which use classifications that date back 50 years or more, resulting in a mishmash that really doesn't speak to the underlying biological causes of the disease.",
     "Disease classifications outdated", "schriftlich", "https://www.mckinsey.com/industries/life-sciences/our-insights/it-will-be-a-paradigm-shift-daphne-koller-on-machine-learning-in-drug-discovery",
     "McKinsey: Paradigm shift in drug discovery", None, "en", "Critique of traditional disease classification"),

    (person_id, "Human pathologists couldn't see those patterns because they don't even know what to look for. Machine learning was able to identify disease-causing and disease-modifying associations that humans just can't see.",
     "ML sees what humans cannot", "schriftlich", "https://www.mckinsey.com/industries/life-sciences/our-insights/it-will-be-a-paradigm-shift-daphne-koller-on-machine-learning-in-drug-discovery",
     "McKinsey: Paradigm shift in drug discovery", None, "en", "Example from fatty liver disease research"),

    (person_id, "when I was at Stanford, a large data set was 200 samples, but now there's an unbelievable ability to both access and generate data fit for purpose for machine learning.",
     "Data availability dramatically increased", "schriftlich", "https://www.technovation.org/blogs/machine-learning-and-medicine-an-interview-with-daphne-koller/",
     "Machine Learning and Medicine Interview", None, "en", "On transformation in available biological data"),

    (person_id, "We are innovating not only in our biology discovery, but also how we partner with industry leaders like Lilly to accelerate our therapeutic programs toward the clinic",
     "Innovation in partnerships too", "schriftlich", "https://www.businesswire.com/news/home/20241009485564/en/insitro-and-Lilly-Enter-Strategic-Agreements-to-Advance-Novel-Treatments-for-Metabolic-Diseases",
     "insitro-Lilly Partnership Announcement", "2024-10-09", "en", "On novel partnership structures with pharma"),
]

# HANDLUNGEN - 15 Handlungen
handlungen = [
    # Gründungen
    (person_id, "gruendung", "Co-founded Coursera with Andrew Ng, online education platform that reached over 100 million learners worldwide",
     "2012-01-01", "https://www.coursera.org/about", "About Coursera", "Both were Computer Science professors at Stanford"),

    (person_id, "gruendung", "Founded insitro, machine learning-driven drug discovery and development company",
     "2018-03-01", "https://www.insitro.com/leadership/daphne-koller/", "insitro Leadership", "Left Calico to start insitro"),

    (person_id, "gruendung", "Co-founded Engageli, digital learning platform with video conferencing tool for higher education",
     "2020-08-01", "https://tytonpartners.com/founders-five-daphne-koller-coursera-and-engageli/", "Founder's Five: Engageli", "Founded with Dan Avida and Serge Plotkin"),

    # Rücktritte/Wechsel
    (person_id, "ruecktritt", "Stepped down as President of Coursera to join Calico as Chief Computing Officer",
     "2016-08-01", "https://www.edsurge.com/news/2016-08-18-daphne-koller-bids-farewell-to-coursera-hello-to-calico",
     "Daphne Koller Bids Farewell to Coursera", "Remained as co-chair of Coursera Board"),

    (person_id, "ruecktritt", "Resigned from Calico as Chief Computing Officer after 18 months",
     "2018-03-01", "https://www.fiercebiotech.com/biotech/calico-loses-its-second-exec-4-months-as-daphne-koller-quits",
     "Calico loses executive as Daphne Koller quits", "To pursue other professional opportunities (insitro)"),

    # Partnerschaften
    (person_id, "partnerschaft", "Announced partnership between insitro and Gilead Sciences for NASH drug discovery worth up to $1.05 billion",
     "2019-04-16", "https://www.gilead.com/news/news-details/2019/gilead-and-insitro-announce-strategic-collaboration-to-discover-and-develop-novel-therapies-for-nonalcoholic-steatohepatitis",
     "Gilead-insitro NASH Collaboration", "First major pharma partnership for insitro, 3-year collaboration with $15M upfront + up to $200M per target for 5 targets"),

    (person_id, "partnerschaft", "Announced 5-year discovery collaboration with Bristol Myers Squibb for ALS and frontotemporal dementia treatments",
     "2020-10-28", "https://www.businesswire.com/news/home/20201028005276/en/insitro-Announces-Five-Year-Discovery-Collaboration-with-Bristol-Myers-Squibb-to-Discover-and-Develop-Novel-Treatments-for-Amyotrophic-Lateral-Sclerosis-and-Frontotemporal-Dementia",
     "insitro-BMS ALS/FTD Collaboration", "$50M upfront, eligible for $20M operational milestones + up to $2B in total milestones + royalties"),

    (person_id, "partnerschaft", "Announced three strategic agreements with Eli Lilly for metabolic diseases including MASLD",
     "2024-10-09", "https://www.businesswire.com/news/home/20241009485564/en/insitro-and-Lilly-Enter-Strategic-Agreements-to-Advance-Novel-Treatments-for-Metabolic-Diseases",
     "insitro-Lilly Metabolic Diseases Partnership", "Novel partnership structure with reversed asset flow, insitro to in-license Lilly's GalNAc delivery technology"),

    # Investitionen/Fundraising
    (person_id, "investition", "Raised $100 million Series A for insitro",
     "2019-07-22", "https://www.businesswire.com/news/home/20200526005212/en/insitro-Announces-143-Million-Raised-in-Series-B-Financing",
     "insitro Series A", "Led by ARCH Venture Partners, Foresite Capital, a16z, GV, Third Rock Ventures"),

    (person_id, "investition", "Raised $143 million Series B for insitro",
     "2020-05-26", "https://www.businesswire.com/news/home/20200526005212/en/insitro-Announces-143-Million-Raised-in-Series-B-Financing",
     "insitro Series B Financing", "Led by Andreessen Horowitz, joined by CPP Investments, T. Rowe Price, BlackRock, Casdin Capital, HOF Capital, WuXi AppTec"),

    (person_id, "investition", "Raised $400 million Series C for insitro",
     "2021-03-15", "https://www.businesswire.com/news/home/20210315005214/en/insitro-Raises-%24400-Million-in-Series-C-Financing",
     "insitro Series C Financing", "Led by CPP Investments, joined by Andreessen Horowitz, T. Rowe Price, BlackRock, Temasek, SoftBank Investment Advisors. Total raised: $743M"),

    (person_id, "investition", "Raised $14.5 million seed funding for Engageli",
     "2020-10-14", "https://www.globenewswire.com/news-release/2020/10/14/2108251/0/en/Engageli-Raises-14-5-Million-to-Build-Inclusive-Digital-Learning-Platform.html",
     "Engageli Raises $14.5M", "To build inclusive digital learning platform as Zoom alternative"),

    # Ehrungen
    (person_id, "sonstiges", "Received MacArthur Foundation Fellowship (Genius Grant)",
     "2004-01-01", "https://www.macfound.org/fellows/class-of-2004/daphne-koller",
     "MacArthur Fellows Class of 2004", "For developing computational methods for representing knowledge and reasoning with uncertainty"),

    (person_id, "sonstiges", "Received ACM-Infosys Foundation Award in Computing Sciences ($150,000)",
     "2008-04-01", "https://www.acm.org/media-center/2008/april/acm-infosys-foundation-announce-winner-of-new-award-honoring-contemporary-contributions-in-computer-science",
     "ACM-Infosys Award 2008", "First recipient of this award, for innovative approach to AI allowing computers to reason from real-world data"),

    (person_id, "sonstiges", "Elected to National Academy of Engineering",
     "2011-01-01", "https://handwiki.org/wiki/Biography:Daphne_Koller",
     "National Academy of Engineering", "For contributions to representation, inference, and learning in probabilistic models with applications to robotics, vision, and biology"),
]

# Aussagen einfügen
print(f"Füge {len(aussagen)} Aussagen ein...")
cursor.executemany("""
    INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", aussagen)

# Handlungen einfügen
print(f"Füge {len(handlungen)} Handlungen ein...")
cursor.executemany("""
    INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", handlungen)

# Änderungen speichern
conn.commit()
print(f"\nErfolgreich eingefügt:")
print(f"- {len(aussagen)} Aussagen")
print(f"- {len(handlungen)} Handlungen")
print(f"- Gesamt: {len(aussagen) + len(handlungen)} Einträge")

# Verbindung schließen
conn.close()
print("\nDatenbank-Update abgeschlossen!")
