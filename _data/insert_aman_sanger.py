import sqlite3
from datetime import datetime

# Verbindung zur Datenbank
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 78  # Aman Sanger

# AUSSAGEN (20 Stück)
aussagen = [
    (person_id, "We're not trying to build a feature or a product. We're trying to build the way people will program for the next 20 years.", "Cursor baut die Zukunft der Programmierung für 20 Jahre", "schriftlich", "https://www.startuparchive.org/p/aman-sanger-on-scaling-cursor-to-100m-in-revenue-in-12-months-c8297f175d3a52be", "Peak XV Partners Interview", "2025-02-01", "en", "Interview bei Peak XV Partners über die Vision von Cursor"),

    (person_id, "Paranoia is daily life at Cursor. You need to reinvent the product every few months, every year.", "Paranoia ist Alltag bei Cursor", "schriftlich", "https://www.businesstoday.in/latest/trends/story/paranoia-is-daily-life-cursor-cofounder-aman-sanger-on-scaling-silicon-valleys-hottest-ai-coding-startup-503512-2025-11-24", "BusinessToday Interview", "2025-11-24", "en", "Über die Unternehmenskultur bei Cursor und die Notwendigkeit konstanter Innovation"),

    (person_id, "A lot of the work of Cursor has been just experimenting with what is possible. For everything you see in the product, there's like 10 failed experiments that didn't work.", "Für jedes Feature gibt es 10 gescheiterte Experimente", "schriftlich", "https://www.startuparchive.org/p/aman-sanger-on-scaling-cursor-to-100m-in-revenue-in-12-months-c8297f175d3a52be", "Startup Archive Interview", "2025-02-01", "en", "Über den Entwicklungsprozess und die experimentelle Natur von Cursor"),

    (person_id, "We released these half-finished things, which a lot of our competitors refused to do. The first version of Copilot++ and Cursor Tab sucked.", "Wir veröffentlichten halbfertige Features", "schriftlich", "https://www.startuparchive.org/p/aman-sanger-on-scaling-cursor-to-100m-in-revenue-in-12-months-c8297f175d3a52be", "Startup Archive Interview", "2025-02-01", "en", "Über die Produktstrategie, früh und unfertig zu launchen"),

    (person_id, "The entirety of that summer was just incredibly slow growth, and that was somewhat demoralizing. The big question in our minds was, 'Are we being too ambitious?'", "Der Sommer war demoralisierend langsames Wachstum", "schriftlich", "https://www.startuparchive.org/p/aman-sanger-on-scaling-cursor-to-100m-in-revenue-in-12-months-c8297f175d3a52be", "Startup Archive Interview", "2025-02-01", "en", "Über die schwierige Anfangsphase von Cursor im Sommer 2023"),

    (person_id, "Programming will soon feel like reviewing the work of a number of interns as engineers spend more time auditing AI-generated code than writing it.", "Programmieren wird wie Praktikanten-Review", "schriftlich", "https://startuppedia.in/trending/trending/were-still-paranoid-25-yo-cursor-founder-says-paranoia-made-the-29b-startup-one-of-fastest-growing-ai-firms-10802232", "Startuppedia Interview", "2025-11-01", "en", "Über die Zukunft der Programmierung mit KI"),

    (person_id, "Software engineering bandwidth and genius ideas are the bottlenecks to rapid AI progress, and Cursor represents our attempt at solving the former, allowing more talent, effort, and resources to be devoted to the latter.", "Engineering-Kapazität ist Flaschenhals für KI-Fortschritt", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über die Mission von Cursor im Kontext des KI-Fortschritts"),

    (person_id, "Programmers should stay in the driver's seat, using AI to amplify human creativity rather than replace it.", "Programmierer bleiben am Steuer", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über die Rolle von Menschen vs. KI in der Programmierung"),

    (person_id, "We want to be a sustainable, independent company. That goal will require constant reinvention, even amid Silicon Valley's admiration.", "Wir wollen nachhaltig und unabhängig bleiben", "schriftlich", "https://startupnews.fyi/2025/11/21/reinvention-will-keep-cursor-on-the-map-says-cofounder-aman-sanger-2/", "StartupNews Interview", "2025-11-21", "en", "Über die langfristige Vision für Cursor trotz enormen Erfolgs"),

    (person_id, "We hired very slowly early on because it was a team of four technical co-founders who could build most of the early product and reach product-market fit without needing to hire anyone.", "Wir stellten am Anfang sehr langsam ein", "schriftlich", "https://www.aol.com/inside-cursors-hiring-strategy-no-052015324.html", "AOL Interview", "2025-08-01", "en", "Über die Hiring-Strategie in der Anfangsphase"),

    (person_id, "We need a brand new AI-powered IDE to get there to reach 90+% code generation adoption.", "Wir brauchen eine völlig neue IDE für 90% Code-Generierung", "schriftlich", "https://www.latent.space/p/cursor", "Latent Space Podcast", "2023-08-01", "en", "Im Latent Space Podcast über die Notwendigkeit einer neuen IDE-Architektur"),

    (person_id, "Most AI product companies are not going to be mostly training their own models, but will instead use these APIs out of the box.", "Die meisten KI-Produkt-Firmen trainieren keine eigenen Modelle", "schriftlich", "https://www.latent.space/p/cursor", "Latent Space Podcast", "2023-08-01", "en", "Über seine veränderte Meinung zur Frage, ob KI-Produktfirmen eigene Modelle trainieren sollten"),

    (person_id, "As language models become capable of producing 90-95% of code, you cannot maintain the old form factor—instead, you need to redesign the entire UX of writing software.", "Bei 90% KI-Code muss die UX neu gedacht werden", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über die Notwendigkeit, die User Experience komplett neu zu gestalten"),

    (person_id, "It's possible to achieve AGI superhuman-level systems through memory mechanisms, but the more elegant approach involves models that can continuously learn through recurrent-based systems with state.", "AGI ist möglich durch kontinuierliches Lernen", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über mögliche Wege zu AGI und kontinuierliches Lernen"),

    (person_id, "Our laser focus is on solving one problem exceptionally well: developer productivity, obsessing over sub-second response times, accurate code predictions, seamless VS Code integration, and real-time collaboration between human and AI.", "Fokus auf Developer Productivity", "schriftlich", "https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/", "WeAreFounders Article", "2024-08-01", "en", "Über die Produktstrategie und den Fokus auf ein Problem"),

    (person_id, "The decision to offer a generous free tier, price at $20-40/month rather than $50-100, and invest zero dollars in marketing reflected confidence that superior product quality would drive growth more effectively than traditional go-to-market motions.", "Produktqualität statt Marketing", "schriftlich", "https://www.wearefounders.uk/how-cursor-ai-hit-100m-arr-in-12-months-the-freemium-fueled-rocket-ship-taking-on-github-copilot/", "WeAreFounders Analysis", "2024-11-01", "en", "Über die Pricing- und Go-to-Market-Strategie"),

    (person_id, "Cursor's competitive strategy against GitHub Copilot targeted specific weaknesses: slow feature velocity, limited context awareness, and being locked-in to a single model.", "Wir zielen auf Copilots Schwächen", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über die Wettbewerbsstrategie gegen GitHub Copilot"),

    (person_id, "We had a thesis that you needed to own the interface, you need to own the IDE, and that gave us an edge compared to well-funded startups and GitHub Copilot.", "Man muss die IDE besitzen, nicht nur ein Plugin bauen", "schriftlich", "https://digidai.github.io/2025/11/21/aman-sanger-cursor-anysphere-fastest-growing-saas-deep-analysis/", "DigiDAI Analysis", "2025-11-21", "en", "Über die strategische Entscheidung, eine eigene IDE zu bauen"),

    (person_id, "The accelerating pace of AI creates more pressure, not less.", "KI-Beschleunigung erhöht den Druck", "schriftlich", "https://www.businesstoday.in/latest/trends/story/paranoia-is-daily-life-cursor-cofounder-aman-sanger-on-scaling-silicon-valleys-hottest-ai-coding-startup-503512-2025-11-24", "BusinessToday Interview", "2025-11-24", "en", "Über die Auswirkungen des schnellen KI-Fortschritts auf das Unternehmen"),

    (person_id, "We empowered programmers to implement ideas more rapidly while maintaining human control and decision-making, with AI handling tasks like generating boilerplate code and migrating codebases.", "KI für Boilerplate, Mensch für Entscheidungen", "schriftlich", "https://wistovibes.co.uk/aman-sanger-innovator-cursor-and-anysphere", "Wisto Vibes Profile", "2025-11-01", "en", "Über die Arbeitsteilung zwischen KI und Menschen")
]

# HANDLUNGEN (15 Stück)
handlungen = [
    (person_id, "gruendung", "Co-founded Anysphere with Michael Truell, Sualeh Asif, and Arvid Lunnemark while at MIT to build Cursor AI code editor", "2022-01-01", "https://en.wikipedia.org/wiki/Anysphere", "Wikipedia: Anysphere", "Gründung von Anysphere durch vier MIT-Studenten"),

    (person_id, "produktlaunch", "Official launch of Cursor IDE to the public, introducing AI-driven code generation, intelligent autocompletion, and codebase querying", "2023-03-01", "https://www.taskade.com/blog/anysphere-cursor-history", "Taskade: Anysphere Cursor History", "Öffentlicher Launch von Cursor als VS Code-kompatiblem AI Editor"),

    (person_id, "investition", "Raised $8 million seed round led by OpenAI Startup Fund, with angels including former GitHub CEO Nat Friedman and Dropbox co-founder Arash Ferdowsi", "2023-10-01", "https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/", "TechCrunch: Anysphere raises $8M from OpenAI", "Seed-Finanzierung mit OpenAI als Lead-Investor"),

    (person_id, "investition", "Raised $60 million Series A led by Andreessen Horowitz (a16z) at $400 million valuation", "2024-08-01", "https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/", "TechCrunch: Exclusive Series A announcement", "Series A Finanzierungsrunde mit a16z als Lead"),

    (person_id, "investition", "Raised $105 million Series B led by Thrive Capital and Andreessen Horowitz at $2.5 billion valuation", "2025-01-01", "https://sacra.com/c/cursor/", "Sacra: Cursor revenue and funding", "Series B Finanzierung mit massiver Bewertungssteigerung"),

    (person_id, "investition", "Raised $900 million Series C led by Thrive Capital with participation from Andreessen Horowitz, Accel, and DST Global at $9.9 billion valuation", "2025-06-05", "https://www.caproasia.com/2025/05/09/united-states-ai-coding-app-cursor-creator-anysphere-raised-900-million-at-9-billion-valuation-founded-in-2022-by-mit-graduates-sualeh-asif-arvid-lunnemark-aman-sanger-michael-truell-investors/", "Caproasia: Series C announcement", "Series C Mega-Runde mit fast $1 Milliarde Kapital"),

    (person_id, "investition", "Raised $2.3 billion Series D at $29.3 billion valuation from OpenAI Startup Fund, Andreessen Horowitz, Thrive Capital, Accel, DST, Coatue, NVIDIA and Google", "2025-11-01", "https://www.caproasia.com/2025/11/15/united-states-ai-coding-app-cursor-creator-anysphere-raised-2-3-billion-in-series-d-funding-at-29-3-billion-valuation-founded-in-2022-by-mit-graduates-sualeh-asif-arvid-lunnemark-aman-sanger-mi/", "Caproasia: Series D mega-round", "Historische Finanzierungsrunde mit NVIDIA und Google als neue Investoren"),

    (person_id, "einstellung", "Scaled team from 4 co-founders to approximately 40-60 employees while reaching $500M ARR, demonstrating extreme capital efficiency", "2024-12-01", "https://www.aol.com/inside-cursors-hiring-strategy-no-052015324.html", "AOL: Inside Cursor's hiring strategy", "Langsames, selektives Team-Wachstum trotz Hyper-Growth"),

    (person_id, "einstellung", "Expanded team to approximately 150 employees as company scaled past $1 billion ARR", "2025-08-01", "https://en.wikipedia.org/wiki/Anysphere", "Wikipedia: Anysphere", "Team-Expansion auf 150 Mitarbeiter"),

    (person_id, "partnerschaft", "Integrated multiple AI models including OpenAI GPT-4, Anthropic Claude, Google Gemini, xAI Grok, and DeepSeek into Cursor platform", "2024-06-01", "https://www.trendingtopics.eu/cursor-launches-in-house-coding-model-to-become-independent-from-openai-anthropic/", "TrendingTopics: Cursor multi-model strategy", "Multi-Modell-Strategie mit allen großen KI-Providern"),

    (person_id, "produktlaunch", "Launched in-house coding model to reduce dependency on OpenAI, Anthropic and other external providers", "2025-10-01", "https://www.trendingtopics.eu/cursor-launches-in-house-coding-model-to-become-independent-from-openai-anthropic/", "TrendingTopics: Cursor launches in-house model", "Strategischer Schritt zur Unabhängigkeit durch eigenes Modell"),

    (person_id, "partnerschaft", "Collaboration with Anthropic featuring joint webinar on pioneering coding frontiers with Claude Opus 4", "2025-03-01", "https://www.anthropic.com/webinars/how-cursor-pioneering-coding-frontiers-claude-opus-4", "Anthropic Webinar", "Strategische Partnerschaft mit Anthropic für Claude Integration"),

    (person_id, "sonstiges", "Achieved billionaire status at age 25 with estimated net worth of $1.3 billion based on 4.5% stake in Anysphere", "2025-11-15", "https://www.dnaindia.com/business/report-who-is-aman-sanger-youngest-billionaire-cofounder-who-started-ai-coding-revolution-his-net-worth-is-know-all-about-his-journey-3190300", "DNA India: Youngest billionaire cofounder", "Wurde mit 25 Jahren zum Milliardär durch Cursor-Bewertung"),

    (person_id, "sonstiges", "Selected for Forbes 30 Under 30 list 2025 in Artificial Intelligence category", "2025-01-15", "https://www.commonwealthunion.com/8-indian-origin-innovators-make-forbes-30-under-30-list/", "Commonwealth Union: Forbes 30 Under 30", "Aufnahme in die Forbes 30 Under 30 Liste"),

    (person_id, "sonstiges", "Appeared on Lex Fridman Podcast #447 with all four Cursor co-founders to discuss Future of Programming with AI", "2024-10-06", "https://lexfridman.com/cursor-team-transcript/", "Lex Fridman Podcast Transcript", "Prominentes Interview im Lex Fridman Podcast")
]

# Aussagen einfügen
print("Füge Aussagen ein...")
for aussage in aussagen:
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage)

# Handlungen einfügen
print("Füge Handlungen ein...")
for handlung in handlungen:
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung)

# Commit und Schließen
conn.commit()
conn.close()

print(f"\n=== ERFOLGREICH ABGESCHLOSSEN ===")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Einträge")
