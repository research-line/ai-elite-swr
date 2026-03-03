#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Aravind Srinivas (person_id=35)
Gründer und CEO von Perplexity AI

Tier 2 Anforderung:
- Mindestens 10 Aussagen
- Mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 35

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, aussage_data)

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein."""
    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, handlung_data)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Sammle Daten fuer Aravind Srinivas (person_id={PERSON_ID})...")

    # ========== AUSSAGEN ==========

    aussagen = [
        # 1. Lex Fridman Podcast - über Citations
        (PERSON_ID,
         "When I wrote my first paper, the senior people who were working with me on the paper told me this one profound thing, which is that every sentence you write in a paper should be backed with a citation, with a citation from another peer reviewed paper, or an experimental result in your own paper.",
         "Jeder Satz in wissenschaftlichen Arbeiten muss durch Zitationen belegt sein",
         "muendlich",
         2, 3,  # Podcast-Interview, Podcasts
         "https://lexfridman.com/aravind-srinivas-transcript/",
         "Aravind Srinivas: Perplexity CEO on Future of AI, Search & the Internet | Lex Fridman Podcast #434",
         "2024-06-19",
         "en",
         "Diskussion über akademische Strenge und wie diese Philosophie Perplexitys Ansatz mit Quellenangaben beeinflusst hat",
         "Als ich meine erste wissenschaftliche Arbeit schrieb, sagten mir die erfahrenen Kollegen etwas Bedeutsames: Jeder Satz in einer wissenschaftlichen Arbeit sollte durch eine Zitation aus einem peer-reviewed Paper oder einem experimentellen Ergebnis der eigenen Arbeit belegt sein."),

        # 2. Lex Fridman - über Curiosity und Perplexitys Mission
        (PERSON_ID,
         "I think this curiosity makes humans special, and we want to cater to that. That's the mission of the company. And we harness the power of AI in all these frontier models to serve that.",
         "Neugierde macht Menschen besonders - das ist die Mission von Perplexity",
         "muendlich",
         2, 3,
         "https://lexfridman.com/aravind-srinivas-transcript/",
         "Aravind Srinivas: Perplexity CEO on Future of AI, Search & the Internet | Lex Fridman Podcast #434",
         "2024-06-19",
         "en",
         "Erklärung der grundlegenden Mission von Perplexity AI",
         "Ich glaube, diese Neugierde macht Menschen besonders, und genau darauf wollen wir eingehen. Das ist die Mission des Unternehmens. Und wir nutzen die Kraft der KI in all diesen Frontier-Modellen, um diesem Zweck zu dienen."),

        # 3. Lex Fridman - Definition von Perplexity
        (PERSON_ID,
         "Perplexity is best described as an answer engine. So you ask it a question, you get an answer. Except the difference is all the answers are backed by sources.",
         "Perplexity ist eine Answer Engine - alle Antworten sind quellenbasiert",
         "muendlich",
         2, 3,
         "https://lexfridman.com/aravind-srinivas-transcript/",
         "Aravind Srinivas: Perplexity CEO on Future of AI, Search & the Internet | Lex Fridman Podcast #434",
         "2024-06-19",
         "en",
         "Kernunterscheidung zwischen Perplexity und anderen KI-Chatbots",
         "Perplexity wird am besten als Answer Engine beschrieben. Man stellt eine Frage und erhält eine Antwort. Der Unterschied ist nur, dass alle Antworten durch Quellen belegt sind."),

        # 4. über AI Accuracy
        (PERSON_ID,
         "I only have one: accuracy. Everything else breaks without it.",
         "Nur eines begeistert mich an KI: Genauigkeit - ohne sie funktioniert nichts",
         "muendlich",
         7, 5,  # Nachrichtenartikel, Nachrichtenmedien
         "https://polsky.uchicago.edu/2025/11/07/fireside-chat-with-perplexity-ais-aravind-srinivas-offers-look-into-the-future-of-ai/",
         "Fireside Chat with Perplexity AI's Aravind Srinivas Offers Look into the Future of AI",
         "2025-11-07",
         "en",
         "Antwort auf die Frage, was ihn an der Zukunft der KI am meisten begeistert",
         "Ich habe nur eine Antwort: Genauigkeit. Ohne sie bricht alles zusammen."),

        # 5. über Reliability
        (PERSON_ID,
         "To make that real, you need reliability. That comes from fixing the thousand bugs no one wants to fix.",
         "Zuverlässigkeit erreicht man durch Behebung tausender Bugs",
         "muendlich",
         7, 5,
         "https://polsky.uchicago.edu/2025/11/07/fireside-chat-with-perplexity-ais-aravind-srinivas-offers-look-into-the-future-of-ai/",
         "Fireside Chat with Perplexity AI's Aravind Srinivas Offers Look into the Future of AI",
         "2025-11-07",
         "en",
         "Über die Entwicklung eines zuverlässigen KI-Assistenten",
         "Um das zu verwirklichen, braucht man Zuverlässigkeit. Diese kommt davon, dass man tausende Bugs behebt, die niemand beheben will."),

        # 6. Stanford GSB - über Knowledge
        (PERSON_ID,
         "The best thing you can do for another human being is to help them learn and know more. It's almost like a moral duty for all of us to seek wisdom and become perpetual learning machines because nothing else can help us keep upgrading ourselves.",
         "Anderen beim Lernen zu helfen ist fast eine moralische Pflicht",
         "muendlich",
         3, 4,  # Keynote/Vortrag, Konferenzen
         "https://www.gsb.stanford.edu/insights/perplexitys-aravind-srinivas-infinite-value-knowledge",
         "Perplexity's Aravind Srinivas on the Infinite Value of Knowledge | Stanford GSB",
         "2024-05-15",
         "en",
         "Zitiert Charlie Munger und erläutert Perplexitys philosophische Grundlage",
         "Das Beste, was man für einen anderen Menschen tun kann, ist ihm zu helfen, mehr zu lernen und zu wissen. Es ist fast eine moralische Pflicht für uns alle, Weisheit zu suchen und zu perpetuellen Lernmaschinen zu werden, denn nichts anderes kann uns helfen, uns kontinuierlich weiterzuentwickeln."),

        # 7. über Curiosity
        (PERSON_ID,
         "Curiosity is unbounded in this world. Every person in the world is curious, but not all of them are blessed to translate that curiosity into a well-articulated question.",
         "Neugierde ist grenzenlos, aber nicht jeder kann sie in gute Fragen übersetzen",
         "muendlich",
         7, 5,
         "https://annjose.com/post/perplexity-ai-ceo-insights/",
         "Perplexity AI: Insights from the CEO Aravind Srinivas",
         "2024-08-20",
         "en",
         "Über die Rolle von Perplexity bei der Demokratisierung von Wissen",
         "Neugierde ist grenzenlos in dieser Welt. Jeder Mensch ist neugierig, aber nicht alle haben das Privileg, diese Neugierde in eine gut formulierte Frage zu übersetzen."),

        # 8. über Search vs Ads
        (PERSON_ID,
         "Search should return answers, not ads. Traditional search is fundamentally a marketing function.",
         "Suche sollte Antworten liefern, nicht Werbung - traditionelle Suche ist Marketing",
         "muendlich",
         7, 5,
         "https://www.gsb.stanford.edu/insights/perplexitys-aravind-srinivas-infinite-value-knowledge",
         "Perplexity's Aravind Srinivas on the Infinite Value of Knowledge | Stanford GSB",
         "2024-05-15",
         "en",
         "Kritik an Googles Geschäftsmodell und Vision für Perplexity",
         "Suche sollte Antworten zurückgeben, nicht Werbeanzeigen. Traditionelle Suche ist im Kern eine Marketingfunktion."),

        # 9. über Google's AI Features
        (PERSON_ID,
         "Every year it's the same feature announced in the IO. Like I think in 2023 they called it Search Generative Experience. In 2024 they called it AI Overview. This year they called it AI Mode. Next year they'll call it another name. But at the end of the day, the feature never gets shipped to the user.",
         "Google kündigt jedes Jahr das gleiche KI-Feature unter neuem Namen an, liefert es aber nie aus",
         "muendlich",
         7, 5,
         "https://www.gsb.stanford.edu/insights/perplexitys-aravind-srinivas-infinite-value-knowledge",
         "Perplexity's Aravind Srinivas on the Infinite Value of Knowledge | Stanford GSB",
         "2024-05-15",
         "en",
         "Kritik an Googles langsamer Innovation und Produktauslieferung",
         "Jedes Jahr wird auf der IO das gleiche Feature angekündigt. 2023 nannten sie es Search Generative Experience. 2024 hieß es AI Overview. Dieses Jahr nennen sie es AI Mode. Nächstes Jahr werden sie es wieder anders nennen. Aber am Ende wird das Feature nie an die Nutzer ausgeliefert."),

        # 10. über Hallucinations
        (PERSON_ID,
         "Hallucinations are always going to be a problem. Hallucinations should always be a bug for a product that aims to give you accurate answers or do stuff for you. You don't want an agent that makes mistakes 20% of the time.",
         "Halluzinationen sind immer ein Problem - ein Agent darf nicht 20% Fehlerquote haben",
         "muendlich",
         7, 5,
         "https://newsroom.haas.berkeley.edu/deans-speaker-series-perplexity-ai-ceo-aravind-srinivas-phd-21-on-why-he-ditched-pitch-decks/",
         "Perplexity AI CEO Aravind Srinivas, PhD 21, on why he ditched pitch decks | UC Berkeley Haas",
         "2024-10-15",
         "en",
         "Über die Herausforderungen bei der Entwicklung zuverlässiger KI-Systeme",
         "Halluzinationen werden immer ein Problem sein. Halluzinationen sollten immer als Bug betrachtet werden für ein Produkt, das genaue Antworten liefern oder Aufgaben für dich erledigen soll. Man will keinen Agenten, der 20% der Zeit Fehler macht."),

        # 11. über Resilience
        (PERSON_ID,
         "Resilience means redefining failure and never giving up. Too many people avoid risks because they worry about losing or how others might perceive them, when in reality, most potential critics aren't paying attention.",
         "Resilienz bedeutet, Scheitern neu zu definieren und niemals aufzugeben",
         "muendlich",
         3, 4,
         "https://www.gsb.stanford.edu/insights/perplexitys-aravind-srinivas-infinite-value-knowledge",
         "Perplexity's Aravind Srinivas on the Infinite Value of Knowledge | Stanford GSB",
         "2024-05-15",
         "en",
         "Leadership-Ratschlag für Entrepreneure",
         "Resilienz bedeutet, Scheitern neu zu definieren und niemals aufzugeben. Zu viele Menschen vermeiden Risiken, weil sie sich Sorgen um Verluste machen oder darum, wie andere sie wahrnehmen könnten, während in Wirklichkeit die meisten potenziellen Kritiker gar nicht aufmerksam sind."),

        # 12. über Knowledge Discovery
        (PERSON_ID,
         "I think of Perplexity as a knowledge discovery engine. The journey doesn't end once you get an answer. In my opinion, the journey begins after you get an answer.",
         "Perplexity ist eine Knowledge Discovery Engine - die Reise beginnt nach der Antwort",
         "muendlich",
         7, 5,
         "https://annjose.com/post/perplexity-ai-ceo-insights/",
         "Perplexity AI: Insights from the CEO Aravind Srinivas",
         "2024-08-20",
         "en",
         "Unterscheidung zwischen reiner Antwortmaschine und Wissens-Explorationstool",
         "Ich sehe Perplexity als Knowledge Discovery Engine. Die Reise endet nicht, sobald man eine Antwort erhält. Meiner Meinung nach beginnt die Reise erst, nachdem man eine Antwort erhalten hat."),
    ]

    for aussage in aussagen:
        insert_aussage(cursor, aussage)

    print(f"  [OK] {len(aussagen)} Aussagen eingefuegt")

    # ========== HANDLUNGEN ==========

    handlungen = [
        # 1. Gründung von Perplexity
        (PERSON_ID,
         "gruendung",
         "Gründung von Perplexity AI als KI-gestützte Answer Engine mit Quellenangaben. Co-Gründer und CEO.",
         "2022-08-01",
         "https://en.wikipedia.org/wiki/Perplexity_AI",
         "Perplexity AI - Wikipedia",
         "Srinivas verließ OpenAI im August 2022 und gründete sofort Perplexity AI zusammen mit Co-Gründern."),

        # 2. Series B Funding - Januar 2024
        (PERSON_ID,
         "investition",
         "Series B Finanzierungsrunde: 73,6 Millionen USD bei 520 Millionen USD Bewertung. Lead: IVP, mit Beteiligung von Nvidia, Jeff Bezos (Bezos Expeditions), und weiteren Investoren.",
         "2024-01-04",
         "https://www.perplexity.ai/hub/blog/perplexity-raises-series-b-funding-round",
         "Perplexity raises Series B funding round",
         "Wichtiger Meilenstein für Wachstum und Produktentwicklung. Bezos' Beteiligung signalisiert starkes Vertrauen in die Vision."),

        # 3. Unicorn Status - März 2024
        (PERSON_ID,
         "investition",
         "Weitere Finanzierung von 63 Millionen USD, Erreichen des Unicorn-Status mit 1,04 Milliarden USD Bewertung. Lead: Daniel Gross (ehemals Y Combinator AI Lead), mit Jeff Bezos, Nvidia, Stan Druckenmiller, Tobi Lutke, Garry Tan.",
         "2024-03-10",
         "https://fortune.com/2024/03/10/jeff-bezos-perplexity-ai-tech-investment/",
         "Jeff Bezos's investment in Perplexity AI has nearly doubled in value | Fortune",
         "Perplexity erreichte Unicorn-Status nur 1,5 Jahre nach Gründung - bemerkenswert schnelles Wachstum."),

        # 4. Publishers Program Launch
        (PERSON_ID,
         "partnerschaft",
         "Launch des Publishers Program: Revenue-Sharing-Modell mit Medienunternehmen als Reaktion auf Plagiatsvorwürfe. Erste Partner: Fortune, Time, Entrepreneur, The Texas Tribune, Der Spiegel, WordPress.com.",
         "2024-07-30",
         "https://www.cnbc.com/2024/07/30/perplexity-ai-to-share-revenue-with-publishers-after-plagiarism-accusations.html",
         "Perplexity AI will share revenue with publishers after plagiarism accusations | CNBC",
         "Strategische Antwort auf Kritik von Forbes, Wired und Condé Nast bezüglich Web Scraping und Plagiat."),

        # 5. Advertising Launch
        (PERSON_ID,
         "produktlaunch",
         "Launch des Werbegeschäfts: Sponsored Follow-up Questions und Video Ads. Erste Partner: Indeed, Whole Foods, Universal McCann, PMG. CPM über 50 USD.",
         "2024-11-12",
         "https://techcrunch.com/2024/11/12/perplexity-brings-ads-to-its-platform/",
         "Perplexity brings ads to its platform | TechCrunch",
         "Perplexity wird erste große KI-Suchmaschine mit Werbung. Zielgruppe: hochgebildete, einkommensstarke Nutzer (80%+ Bachelor-Abschluss)."),

        # 6. Shopping Hub Launch
        (PERSON_ID,
         "produktlaunch",
         "Launch des Shopping Hub für Pro-Nutzer in den USA: Visual Product Cards, Snap to Shop (Foto-basierte Produktsuche), One-Click Checkout mit kostenlosem Versand für Pro-Abonnenten. Integration mit Shopify.",
         "2024-11-18",
         "https://techcrunch.com/2024/11/18/perplexity-introduces-a-shopping-feature-for-pro-users/",
         "Perplexity introduces a shopping feature for Pro users | TechCrunch",
         "Direkte Konkurrenz zu Google Shopping und Amazon. Unterstützt durch Investment von Jeff Bezos und Nvidia."),

        # 7. Series D Funding
        (PERSON_ID,
         "investition",
         "Series D Finanzierungsrunde: 500 Millionen USD bei 9 Milliarden USD Bewertung - Verdreifachung des Werts innerhalb weniger Monate. Vierte Finanzierungsrunde in 2024.",
         "2024-12-18",
         "https://www.benzinga.com/tech/24/12/42570376/jeff-bezos-backed-perplexity-raises-500-million-tripling-its-valuation-to-9-billion-as-competition-with-google-and-openai-heats-up",
         "Jeff Bezos-Backed Perplexity Raises $500 Million, Tripling Its Valuation To $9 Billion | Benzinga",
         "Massive Wachstumsdynamik: von 520M USD (Januar) auf 9 Mrd. USD (Dezember) - Faktor 17 in einem Jahr."),

        # 8. Meeting mit PM Modi
        (PERSON_ID,
         "politisch",
         "Treffen mit dem indischen Premierminister Narendra Modi in Neu-Delhi. Diskussion über KI-Adoption in Indien und weltweit. Srinivas bot an, Perplexity Pro für indische Studenten, Forscher und Fakultät zugänglich zu machen.",
         "2024-12-28",
         "https://startupnews.fyi/2024/12/28/pm-modi-meets-perplexity-ai-ceo-aravind-srinivas/",
         "PM Modi Meets Perplexity AI CEO Aravind Srinivas | Startup News",
         "Hochrangige politische Engagement zeigt Srinivas' Rolle als KI-Vordenker und indischer Tech-Botschafter."),

        # 9. Investment in Finance AI Startup
        (PERSON_ID,
         "investition",
         "Persönliche Beteiligung an 9 Millionen USD Finanzierungsrunde für ein KI-Startup im Finanzbereich, das Finance-Routinearbeit um 40% reduziert und Monatsabschlüsse halbiert.",
         "2024-11-15",
         "https://finance.yahoo.com/news/perplexity-ceo-aravind-srinivas-backs-143108581.html",
         "Perplexity CEO Aravind Srinivas Backs $9M AI Startup | Yahoo Finance",
         "Zeigt Srinivas' Rolle als Angel Investor und Unterstützer des breiteren KI-Ökosystems."),

        # 10. Stanford GSB View From The Top Talk
        (PERSON_ID,
         "sonstiges",
         "Keynote beim Stanford GSB View From The Top - dem führenden Leadership Speaker Series seit 1978. Themen: Entrepreneurship, Building Teams, Bias for Action, Ethische KI.",
         "2024-05-15",
         "https://www.gsb.stanford.edu/events/view-top-aravind-srinivas",
         "View From The Top: Aravind Srinivas | Stanford GSB",
         "Anerkennung als führende Stimme im KI- und Entrepreneurship-Bereich. Stanford GSB ist eine der weltweit führenden Business Schools."),
    ]

    for handlung in handlungen:
        insert_handlung(cursor, handlung)

    print(f"  [OK] {len(handlungen)} Handlungen eingefuegt")

    # Commit und Close
    conn.commit()
    conn.close()

    print(f"\n[ERFOLG] Erfolgreich abgeschlossen!")
    print(f"  Total: {len(aussagen)} Aussagen + {len(handlungen)} Handlungen")
    print(f"  Tier 2 erfuellt: [OK] (mindestens 10 Aussagen + 8 Handlungen)")

if __name__ == "__main__":
    main()
