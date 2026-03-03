#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sammlung von Aussagen und Handlungen von Clement Delangue (person_id=48)
CEO und Co-Gründer von Hugging Face
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

# Datenbank-Pfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_aussage(cursor, person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
                   plattform_id, quell_link, quell_titel, datum_aussage, sprache,
                   kontext, aussage_uebersetzung_de):
    """Fügt eine Aussage in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
            plattform_id, quell_link, quell_titel, datum_aussage, sprache,
            kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
          plattform_id, quell_link, quell_titel, datum_aussage, sprache,
          kontext, aussage_uebersetzung_de))

def insert_handlung(cursor, person_id, handlung_typ, beschreibung,
                    datum_handlung, quell_link, quell_titel):
    """Fügt eine Handlung in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung,
            datum_handlung, quell_link, quell_titel
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (person_id, handlung_typ, beschreibung,
          datum_handlung, quell_link, quell_titel))

def main():
    print("Starte Datensammlung für Clement Delangue (person_id=48)...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    person_id = 48  # Clement Delangue

    # ============================================================================
    # AUSSAGEN (mindestens 10 für Tier 2)
    # ============================================================================

    aussagen = [
        {
            "aussage_text": "Open science and open source AI distribute economic gains by enabling hundreds of thousands of small companies and startups to build with AI. It fosters innovation, and fair competition between all.",
            "aussage_kurz": "Open Source AI verteilt wirtschaftliche Gewinne und fördert Innovation durch Zugänglichkeit für Startups",
            "modus": "muendlich",
            "quellen_typ_id": 10,  # Offizielle Stellungnahme
            "plattform_id": 10,  # Congressional Testimony
            "quell_link": "https://x.com/ClementDelangue/status/1673348676478025730",
            "quell_titel": "Testimony before US Congress on AI",
            "datum_aussage": "2023-06-22",
            "sprache": "EN",
            "kontext": "Congressional testimony before House Science Committee on AI regulation and innovation",
            "aussage_uebersetzung_de": "Open Science und Open Source KI verteilen wirtschaftliche Gewinne, indem sie Hunderttausenden kleiner Unternehmen und Startups ermöglichen, mit KI zu bauen. Dies fördert Innovation und fairen Wettbewerb zwischen allen."
        },
        {
            "aussage_text": "Thanks to ethical openness, [they create] a safer path for development of the technology by giving civil society, nonprofits, academia and policymakers the capabilities they need to counterbalance the power of big private companies.",
            "aussage_kurz": "Ethische Offenheit schafft sichereren KI-Entwicklungsweg durch Ermächtigung der Zivilgesellschaft",
            "modus": "muendlich",
            "quellen_typ_id": 10,  # Offizielle Stellungnahme
            "plattform_id": 10,  # Congressional Testimony
            "quell_link": "https://venturebeat.com/ai/hugging-face-ceo-tells-us-house-open-source-ai-is-extremely-aligned-with-american-interests",
            "quell_titel": "Hugging Face CEO tells US House open-source AI is 'extremely aligned' with American interests",
            "datum_aussage": "2023-06-22",
            "sprache": "EN",
            "kontext": "Congressional testimony explaining why open source AI creates safer development paths",
            "aussage_uebersetzung_de": "Dank ethischer Offenheit schaffen wir einen sichereren Weg für die Entwicklung der Technologie, indem wir der Zivilgesellschaft, gemeinnützigen Organisationen, der Wissenschaft und politischen Entscheidungsträgern die Fähigkeiten geben, die sie brauchen, um die Macht großer privater Unternehmen auszugleichen."
        },
        {
            "aussage_text": "We are a big proponent of more transparency, more openness, more distribution of power in terms of AI capabilities. That's what we're trying to push, while at the same time respecting the different approaches that companies take.",
            "aussage_kurz": "Befürworter von Transparenz, Offenheit und Machtverteilung bei KI-Fähigkeiten",
            "modus": "muendlich",
            "quellen_typ_id": 1,  # Video-Interview
            "plattform_id": 3,  # Podcasts
            "quell_link": "https://www.acquired.fm/episodes/building-the-open-source-ai-revolution-with-hugging-face-ceo-clem-delangue",
            "quell_titel": "Building the Open Source AI Revolution - Acquired Podcast",
            "datum_aussage": "2023-08-15",
            "sprache": "EN",
            "kontext": "Interview discussing Hugging Face's philosophy and approach to AI development",
            "aussage_uebersetzung_de": "Wir sind ein großer Befürworter von mehr Transparenz, mehr Offenheit, mehr Verteilung von Macht in Bezug auf KI-Fähigkeiten. Das ist es, was wir vorantreiben wollen, während wir gleichzeitig die verschiedenen Ansätze respektieren, die Unternehmen verfolgen."
        },
        {
            "aussage_text": "I think through the open source model, you can do things a bit differently ... you can, as a startup, empower the community in a way, and create a thousand times more value than you would by building a proprietary tool.",
            "aussage_kurz": "Open Source ermöglicht Startups tausendfach mehr Wert zu schaffen als proprietäre Tools",
            "modus": "muendlich",
            "quellen_typ_id": 2,  # Podcast-Interview
            "plattform_id": 3,  # Podcasts
            "quell_link": "https://www.acquired.fm/episodes/building-the-open-source-ai-revolution-with-hugging-face-ceo-clem-delangue",
            "quell_titel": "Building the Open Source AI Revolution - Acquired Podcast",
            "datum_aussage": "2023-08-15",
            "sprache": "EN",
            "kontext": "Explaining the business value and community empowerment potential of open source AI models",
            "aussage_uebersetzung_de": "Ich denke, durch das Open-Source-Modell kann man Dinge etwas anders machen ... man kann als Startup die Community auf eine Weise befähigen und tausendmal mehr Wert schaffen, als man es durch den Bau eines proprietären Tools würde."
        },
        {
            "aussage_text": "Open science and open source AI are extremely aligned with the American values and interests.",
            "aussage_kurz": "Open Source KI entspricht amerikanischen Werten und Interessen",
            "modus": "muendlich",
            "quellen_typ_id": 10,  # Offizielle Stellungnahme
            "plattform_id": 10,  # Congressional Testimony
            "quell_link": "https://venturebeat.com/ai/hugging-face-ceo-tells-us-house-open-source-ai-is-extremely-aligned-with-american-interests",
            "quell_titel": "Hugging Face CEO tells US House open-source AI is 'extremely aligned' with American interests",
            "datum_aussage": "2023-06-22",
            "sprache": "EN",
            "kontext": "Congressional testimony positioning open source AI as aligned with US national interests",
            "aussage_uebersetzung_de": "Open Science und Open Source KI sind extrem im Einklang mit den amerikanischen Werten und Interessen."
        },
        {
            "aussage_text": "Once again, an AI system is not 'thinking', it's 'processing', 'running predictions',... just like Google or computers do. Giving the false impression that technology systems are human is just cheap snake oil and marketing to fool you into thinking it's more clever than it is.",
            "aussage_kurz": "KI-Systeme 'denken' nicht - anthropomorphe Sprache ist Marketing-Täuschung",
            "modus": "schriftlich",
            "quellen_typ_id": 5,  # Social-Media-Post
            "plattform_id": 2,  # Twitter/X
            "quell_link": "https://x.com/ClementDelangue/status/1834283206474191320",
            "quell_titel": "Tweet on AI anthropomorphization",
            "datum_aussage": "2024-09-12",
            "sprache": "EN",
            "kontext": "Critique of anthropomorphizing AI systems and misleading marketing language",
            "aussage_uebersetzung_de": "Noch einmal: Ein KI-System 'denkt' nicht, es 'verarbeitet', 'führt Vorhersagen aus'... genau wie Google oder Computer es tun. Den falschen Eindruck zu erwecken, dass Technologiesysteme menschlich sind, ist nur billiges Schlangenöl und Marketing, um Sie glauben zu machen, dass es cleverer ist, als es tatsächlich ist."
        },
        {
            "aussage_text": "What few understand is that the main reason why open-source is lagging behind closed-source in some AI domains (ex: video or LLMs) is because you can't hide with open-source and it forces you to take more ethical decisions that can sometimes be detrimental to performance.",
            "aussage_kurz": "Open Source hinkt hinterher, weil ethische Transparenz Performance-Nachteile bringen kann",
            "modus": "schriftlich",
            "quellen_typ_id": 5,  # Social-Media-Post
            "plattform_id": 2,  # Twitter/X
            "quell_link": "https://x.com/ClementDelangue/status/1820790760419053696",
            "quell_titel": "Tweet on open-source AI ethics vs performance",
            "datum_aussage": "2024-08-06",
            "sprache": "EN",
            "kontext": "Discussion of trade-offs between open source transparency/ethics and performance in AI development",
            "aussage_uebersetzung_de": "Was wenige verstehen ist, dass der Hauptgrund, warum Open Source in einigen KI-Bereichen (z.B. Video oder LLMs) hinter Closed Source zurückbleibt, darin liegt, dass man sich mit Open Source nicht verstecken kann und es einen zwingt, ethischere Entscheidungen zu treffen, die manchmal für die Performance nachteilig sein können."
        },
        {
            "aussage_text": "Is it time we stop using the word AI for everything and instead use words like 'chatbots', 'video generation', 'recommendation engines', 'cell prediction',...? Feels like as a society, we could have healthier debates like that.",
            "aussage_kurz": "Präzisere Begriffe statt 'KI' würden zu gesünderen gesellschaftlichen Debatten führen",
            "modus": "schriftlich",
            "quellen_typ_id": 5,  # Social-Media-Post
            "plattform_id": 2,  # Twitter/X
            "quell_link": "https://x.com/ClementDelangue/status/1973864684387516478",
            "quell_titel": "Tweet on AI terminology",
            "datum_aussage": "2025-10-28",
            "sprache": "EN",
            "kontext": "Proposal to use more specific terminology instead of the catch-all term 'AI' for better public discourse",
            "aussage_uebersetzung_de": "Ist es an der Zeit, dass wir aufhören, das Wort KI für alles zu verwenden und stattdessen Wörter wie 'Chatbots', 'Videogenerierung', 'Empfehlungsalgorithmen', 'Zellvorhersage' verwenden...? Es fühlt sich so an, als könnten wir als Gesellschaft auf diese Weise gesündere Debatten führen."
        },
        {
            "aussage_text": "The future of AI is here, but it's not evenly distributed. We're on a journey to advance and democratize artificial intelligence through open source and open science. It's time to make AI open and accessible to all.",
            "aussage_kurz": "KI-Zukunft ist da, aber ungleich verteilt - Zeit für Demokratisierung durch Open Source",
            "modus": "muendlich",
            "quellen_typ_id": 10,  # Offizielle Stellungnahme
            "plattform_id": 5,  # Nachrichtenmedien
            "quell_link": "https://www.artificialintelligence-news.com/news/aws-and-hugging-face-expand-partnership-to-make-ai-more-accessible/",
            "quell_titel": "AWS and Hugging Face expand partnership to make AI more accessible",
            "datum_aussage": "2023-02-21",
            "sprache": "EN",
            "kontext": "Statement at announcement of AWS partnership expansion to democratize AI access",
            "aussage_uebersetzung_de": "Die Zukunft der KI ist hier, aber sie ist nicht gleichmäßig verteilt. Wir sind auf einer Reise, künstliche Intelligenz durch Open Source und Open Science voranzubringen und zu demokratisieren. Es ist Zeit, KI offen und für alle zugänglich zu machen."
        },
        {
            "aussage_text": "Open-science and open-source prevent black box systems, make companies more accountable and help solving today's challenges like mitigating biases, reducing misinformation, promoting copyrights, and rewarding all stakeholders.",
            "aussage_kurz": "Open Source verhindert Black-Box-Systeme und schafft Rechenschaftspflicht",
            "modus": "muendlich",
            "quellen_typ_id": 7,  # Nachrichtenartikel
            "plattform_id": 5,  # Nachrichtenmedien
            "quell_link": "https://aibusiness.com/responsible-ai/hugging-face-ceo-advocates-for-safe-ai-innovation-in-u-s-congress",
            "quell_titel": "Hugging Face CEO: Balance Openness, Accountability in AI Models",
            "datum_aussage": "2023-06-22",
            "sprache": "EN",
            "kontext": "Congressional testimony on benefits of open source for AI accountability and addressing societal challenges",
            "aussage_uebersetzung_de": "Open Science und Open Source verhindern Black-Box-Systeme, machen Unternehmen rechenschaftspflichtiger und helfen bei der Lösung heutiger Herausforderungen wie der Minderung von Voreingenommenheit, der Reduzierung von Fehlinformationen, der Förderung von Urheberrechten und der Belohnung aller Beteiligten."
        },
        {
            "aussage_text": "There are a lot of people emphasizing the existential risk of AI to justify the fact that it shouldn't be as open as it is, saying that it's better not to share research because it's dangerous.",
            "aussage_kurz": "Existenzielle KI-Risiko-Argumente werden genutzt, um Offenheit zu verhindern",
            "modus": "schriftlich",
            "quellen_typ_id": 7,  # Nachrichtenartikel
            "plattform_id": 5,  # Nachrichtenmedien
            "quell_link": "https://qz.com/hugging-face-clement-delangue-ai-democracy-1851058839",
            "quell_titel": "Hugging Face CEO Clément Delangue wants an AI democracy",
            "datum_aussage": "2023-11-15",
            "sprache": "EN",
            "kontext": "Critique of using existential risk arguments to justify closed AI development",
            "aussage_uebersetzung_de": "Es gibt viele Leute, die das existenzielle Risiko von KI betonen, um zu rechtfertigen, dass sie nicht so offen sein sollte, wie sie ist, und sagen, dass es besser ist, Forschung nicht zu teilen, weil es gefährlich ist."
        },
        {
            "aussage_text": "Openness bolsters transparency and enables external scrutiny.",
            "aussage_kurz": "Offenheit stärkt Transparenz und ermöglicht externe Kontrolle",
            "modus": "muendlich",
            "quellen_typ_id": 7,  # Nachrichtenartikel
            "plattform_id": 5,  # Nachrichtenmedien
            "quell_link": "https://aibusiness.com/responsible-ai/hugging-face-ceo-advocates-for-safe-ai-innovation-in-u-s-congress",
            "quell_titel": "Hugging Face CEO: Balance Openness, Accountability in AI Models",
            "datum_aussage": "2023-06-22",
            "sprache": "EN",
            "kontext": "Congressional testimony on benefits of openness for AI safety and accountability",
            "aussage_uebersetzung_de": "Offenheit stärkt Transparenz und ermöglicht externe Kontrolle."
        }
    ]

    print(f"\nFüge {len(aussagen)} Aussagen ein...")
    for aussage in aussagen:
        insert_aussage(cursor, person_id, **aussage)

    # ============================================================================
    # HANDLUNGEN (mindestens 8 für Tier 2)
    # ============================================================================

    handlungen = [
        {
            "handlung_typ": "gruendung",
            "beschreibung": "Co-Gründung von Hugging Face zusammen mit Julien Chaumond und Thomas Wolf in New York. Ursprünglich als Chatbot-App für Teenager gestartet, später zur Open-Source-KI-Plattform pivotiert.",
            "datum_handlung": "2016-03-01",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Series D Funding Round von $235 Millionen unter Führung von Salesforce, mit Beteiligung von Google, Amazon, Nvidia, Intel, AMD, Qualcomm und IBM. Unternehmensbewertung erreicht $4.5 Milliarden.",
            "datum_handlung": "2023-08-24",
            "quell_link": "https://techcrunch.com/2023/08/24/hugging-face-raises-235m-from-investors-including-salesforce-and-nvidia/",
            "quell_titel": "Hugging Face raises $235M from investors, including Salesforce and Nvidia - TechCrunch"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Strategische Partnerschaft mit Amazon Web Services (AWS) zur Integration von Hugging Face Produkten in AWS-Infrastruktur. Hugging Face nutzt AWS als bevorzugten Cloud-Provider für Training und Deployment von KI-Modellen.",
            "datum_handlung": "2023-02-21",
            "quell_link": "https://www.artificialintelligence-news.com/news/aws-and-hugging-face-expand-partnership-to-make-ai-more-accessible/",
            "quell_titel": "AWS and Hugging Face expand partnership to make AI more accessible"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Erweiterung der Partnerschaft mit Microsoft Azure, begonnen 2022, um Entwicklern breitere Infrastruktur und Tools für Copilot AI-Modelle bereitzustellen.",
            "datum_handlung": "2024-05-01",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch von HuggingChat als Open-Source-Alternative zu ChatGPT, basierend auf Meta's LLaMa-Modell. Ziel war zu demonstrieren, dass Open-Source-Alternativen zu proprietären Chatbots möglich sind.",
            "datum_handlung": "2023-04-25",
            "quell_link": "https://techcrunch.com/2023/04/25/hugging-face-releases-its-own-version-of-chatgpt/",
            "quell_titel": "Hugging Face releases its own version of ChatGPT - TechCrunch"
        },
        {
            "handlung_typ": "lobbying",
            "beschreibung": "Aussage vor dem US House Committee on Science, Space and Technology über die Bedeutung von Open-Source-KI für amerikanische Interessen, Innovation und faire Wettbewerbsbedingungen. Advocacy für erhöhte NIST-Finanzierung.",
            "datum_handlung": "2023-06-22",
            "quell_link": "https://venturebeat.com/ai/hugging-face-ceo-tells-us-house-open-source-ai-is-extremely-aligned-with-american-interests",
            "quell_titel": "Hugging Face CEO tells US House open-source AI is 'extremely aligned' with American interests"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Partnerschaft mit Dell Technologies zur Vereinfachung der On-Premises-Implementierung von Open-Source-Generative-AI-Modellen für Unternehmen. Erstellung eines Dell-Portals auf der Hugging Face Plattform.",
            "datum_handlung": "2023-11-14",
            "quell_link": "https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2023~11~20231114-dell-technologies-and-hugging-face-to-simplify-generative-ai-with-on-premises-it.htm",
            "quell_titel": "Dell Technologies and Hugging Face to Simplify Generative AI with On-Premises IT"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Zusammenarbeit mit Google Cloud zur Kombination von Hugging Face Open-Source-Modellen mit Google-Infrastruktur. Einführung des Hallucinations Leaderboard zur Bekämpfung von KI-Halluzinationen.",
            "datum_handlung": "2024-01-15",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch von HUGS (Hugging Face for Generative AI Services) als kostenpflichtiges Angebot zur Unterstützung von Unternehmen bei der Bereitstellung von KI-Modellen. Markiert Wandel zu kommerziellen Diensten.",
            "datum_handlung": "2024-10-01",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Zusammenarbeit mit Nvidia zur Integration von Nvidia-beschleunigten Inferenz-Services in die Hugging Face Open-Source-Plattform für verbesserte KI-Model-Performance.",
            "datum_handlung": "2024-07-01",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Start eines KI-Accelerator-Programms für europäische Startups zusammen mit Meta und Scaleway, um Startups bei der Integration offener Foundation-Modelle in ihre Produkte zu unterstützen.",
            "datum_handlung": "2024-06-01",
            "quell_link": "https://en.wikipedia.org/wiki/Hugging_Face",
            "quell_titel": "Hugging Face - Wikipedia"
        }
    ]

    print(f"Füge {len(handlungen)} Handlungen ein...")
    for handlung in handlungen:
        insert_handlung(cursor, person_id, **handlung)

    # Änderungen speichern
    conn.commit()

    # Statistik ausgeben
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (person_id,))
    anzahl_aussagen = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (person_id,))
    anzahl_handlungen = cursor.fetchone()[0]

    print("\n" + "="*70)
    print("ERFOLGREICH ABGESCHLOSSEN")
    print("="*70)
    print(f"Person: Clement Delangue (ID: {person_id})")
    print(f"Aussagen eingefügt: {anzahl_aussagen}")
    print(f"Handlungen eingefügt: {anzahl_handlungen}")
    tier2_status = "ERFUELLT" if anzahl_aussagen >= 10 and anzahl_handlungen >= 8 else "NICHT ERFUELLT"
    print(f"Tier 2 Status: {tier2_status}")
    print("="*70)

    conn.close()

if __name__ == "__main__":
    main()
