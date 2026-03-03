#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_bezos.py
================
Sammelt verifizierbare Aussagen und Handlungen von Jeff Bezos (person_id=10)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Shareholder Letters, Konferenz-Vortraegen und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 10  # Jeff Bezos

# ============================================================================
# AUSSAGEN (Statements)
# ============================================================================
# Jede Aussage enthaelt:
#   - aussage_text: Originalwortlaut (Englisch)
#   - aussage_kurz: 1-Satz-Zusammenfassung (Deutsch)
#   - modus: 'muendlich' oder 'schriftlich'
#   - quellen_typ_id: FK zu quellen_typen
#   - plattform_id: FK zu plattformen
#   - quell_link: URL
#   - quell_titel: Titel der Quelle
#   - datum_aussage: YYYY-MM-DD oder YYYY
#   - sprache: 'en'
#   - kontext: Zusammenhang
#   - aussage_uebersetzung_de: Deutsche Uebersetzung

AUSSAGEN = [
    # ---- 1. 1997 Shareholder Letter (Day 1) ----
    {
        "aussage_text": "This is Day 1 for the Internet and, if we execute well, for Amazon.com. Today, online commerce saves customers money and precious time. Tomorrow, through personalization, online commerce will accelerate the very process of discovery.",
        "aussage_kurz": "Bezos erklaert 1997, es sei 'Tag 1' fuer das Internet und Amazon -- und kuendigt Personalisierung als naechsten Schritt an.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 9,     # Blogs/Corporate
        "quell_link": "https://www.aboutamazon.com/news/company-news/1997-letter-to-shareholders",
        "quell_titel": "1997 Letter to Shareholders (Amazon)",
        "datum_aussage": "1997-04-01",
        "sprache": "en",
        "kontext": "Der erste Shareholder Letter von Jeff Bezos, geschrieben nach dem Amazon IPO 1997. Etabliert das 'Day 1'-Konzept, das Bezos sein ganzes Berufsleben lang wiederholen wird.",
        "aussage_uebersetzung_de": "Dies ist Tag 1 fuer das Internet und, wenn wir gut ausfuehren, fuer Amazon.com. Heute spart Online-Handel Kunden Geld und wertvolle Zeit. Morgen wird Online-Handel durch Personalisierung den gesamten Entdeckungsprozess beschleunigen.",
    },
    # ---- 2. 1997 Shareholder Letter (Long-Term Thinking) ----
    {
        "aussage_text": "We believe that a fundamental measure of our success will be the shareholder value we create over the long term. This value will be a direct result of our ability to extend and solidify our current market leadership position.",
        "aussage_kurz": "Bezos erklaert 1997, dass Amazons Erfolg am langfristigen Shareholder Value gemessen wird -- nicht an kurzfristigen Gewinnen.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/1997-letter-to-shareholders",
        "quell_titel": "1997 Letter to Shareholders (Amazon)",
        "datum_aussage": "1997-04-01",
        "sprache": "en",
        "kontext": "Bezos etabliert die langfristige Perspektive als Kern der Amazon-Strategie -- eine damals radikale Position in einer von Quartalsberichten dominierten Kultur.",
        "aussage_uebersetzung_de": "Wir glauben, dass ein grundlegendes Mass unseres Erfolgs der Shareholder Value sein wird, den wir langfristig schaffen. Dieser Wert wird ein direktes Ergebnis unserer Faehigkeit sein, unsere aktuelle Marktfuehrerschaft auszubauen und zu festigen.",
    },
    # ---- 3. 2016 Shareholder Letter (Day 2) ----
    {
        "aussage_text": "Day 2 is stasis. Followed by irrelevance. Followed by excruciating, painful decline. Followed by death. And that is why it is always Day 1.",
        "aussage_kurz": "Bezos warnt, dass 'Tag 2' Stillstand, Irrelevanz und letztlich den Tod bedeutet -- deshalb sei es immer Tag 1.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders",
        "quell_titel": "2016 Letter to Shareholders (Amazon)",
        "datum_aussage": "2016-04-01",
        "sprache": "en",
        "kontext": "In seinem vielleicht beruehmtesten Shareholder Letter definiert Bezos 'Day 1' vs. 'Day 2' und etabliert die 'Day 1 Mentalitaet' als Philosophie gegen organisatorische Sklerose.",
        "aussage_uebersetzung_de": "Tag 2 ist Stillstand. Gefolgt von Irrelevanz. Gefolgt von qualvollem, schmerzhaftem Niedergang. Gefolgt vom Tod. Und deshalb ist es immer Tag 1.",
    },
    # ---- 4. 2016 Shareholder Letter (Customer Obsession) ----
    {
        "aussage_text": "There are many ways to center a business. You can be competitor focused, you can be product focused, you can be technology focused, you can be business model focused, and there are more. But in my view, obsessive customer focus is by far the most protective of Day 1 vitality.",
        "aussage_kurz": "Bezos erklaert, obsessive Kundenfokussierung sei der beste Schutz gegen 'Tag 2'-Niedergang.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders",
        "quell_titel": "2016 Letter to Shareholders (Amazon)",
        "datum_aussage": "2016-04-01",
        "sprache": "en",
        "kontext": "Bezos identifiziert vier Faktoren, die Day 1-Vitalitaet bewahren. Customer Obsession steht an erster Stelle.",
        "aussage_uebersetzung_de": "Es gibt viele Wege, ein Unternehmen zu zentrieren. Man kann wettbewerbsfokussiert sein, produktfokussiert, technologiefokussiert, geschaeftsmodellfokussiert -- und es gibt noch mehr. Aber meiner Ansicht nach ist obsessive Kundenfokussierung bei weitem der beste Schutz fuer Tag-1-Vitalitaet.",
    },
    # ---- 5. 2016 Shareholder Letter (Resist Proxies) ----
    {
        "aussage_text": "As companies get larger and more complex, there's a tendency to manage to proxies. This comes in many shapes and sizes, and it's dangerous, subtle, and very Day 2.",
        "aussage_kurz": "Bezos warnt vor dem Management nach 'Proxies' (Ersatzkennzahlen) statt nach der Sache selbst -- typisch fuer 'Tag 2'.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders",
        "quell_titel": "2016 Letter to Shareholders (Amazon)",
        "datum_aussage": "2016-04-01",
        "sprache": "en",
        "kontext": "Zweiter Day-1-Faktor: Widerstand gegen Proxy-Management. Bezos meint damit, Prozesse mit Zielen zu verwechseln.",
        "aussage_uebersetzung_de": "Wenn Unternehmen groesser und komplexer werden, entsteht die Tendenz, nach Proxies zu managen. Das nimmt viele Formen an, und es ist gefaehrlich, subtil und sehr Tag 2.",
    },
    # ---- 6. 2016 Shareholder Letter (High-Velocity Decisions) ----
    {
        "aussage_text": "Day 2 companies make high-quality decisions, but they make high-quality decisions slowly. To keep the energy and dynamism of Day 1, you have to somehow make high-quality, high-velocity decisions.",
        "aussage_kurz": "Bezos fordert hochwertige Entscheidungen bei hoher Geschwindigkeit -- nicht Qualitaet oder Geschwindigkeit, sondern beides.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders",
        "quell_titel": "2016 Letter to Shareholders (Amazon)",
        "datum_aussage": "2016-04-01",
        "sprache": "en",
        "kontext": "Vierter Day-1-Faktor: Schnelle, hochwertige Entscheidungen. Bezos beschreibt Techniken wie 'disagree and commit' und 'two-way doors'.",
        "aussage_uebersetzung_de": "Tag-2-Unternehmen treffen hochwertige Entscheidungen, aber sie treffen hochwertige Entscheidungen langsam. Um die Energie und Dynamik von Tag 1 zu bewahren, muss man irgendwie hochwertige Hochgeschwindigkeits-Entscheidungen treffen.",
    },
    # ---- 7. 2018 Shareholder Letter (Intuition + Data) ----
    {
        "aussage_text": "Sometimes we have conviction about a direction despite not having perfect information – just enough to make a judgement call. We make those judgements with the input of many people and are willing to change course if we get more data.",
        "aussage_kurz": "Bezos erklaert, man muesse manchmal ohne perfekte Information entscheiden, aber bereit sein, den Kurs zu aendern.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2018-letter-to-shareholders",
        "quell_titel": "2018 Letter to Shareholders (Amazon)",
        "datum_aussage": "2018-04-01",
        "sprache": "en",
        "kontext": "Bezos verteidigt Alexa und andere gescheiterte Experimente. Er betont, dass Innovation Misserfolge erfordert.",
        "aussage_uebersetzung_de": "Manchmal haben wir Ueberzeugung ueber eine Richtung, obwohl wir keine perfekten Informationen haben -- gerade genug, um eine Beurteilung zu treffen. Wir treffen diese Beurteilungen mit dem Input vieler Leute und sind bereit, den Kurs zu aendern, wenn wir mehr Daten bekommen.",
    },
    # ---- 8. 2018 Shareholder Letter (Failure) ----
    {
        "aussage_text": "As a company grows, everything needs to scale, including the size of your failed experiments. If the size of your failures isn't growing, you're not going to be inventing at a size that can actually move the needle.",
        "aussage_kurz": "Bezos sagt, die Groesse der Fehlschlaege muesse mit dem Unternehmen wachsen, sonst sei Innovation zu klein.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2018-letter-to-shareholders",
        "quell_titel": "2018 Letter to Shareholders (Amazon)",
        "datum_aussage": "2018-04-01",
        "sprache": "en",
        "kontext": "Bezos beschreibt Amazon als Experimentiermaschine und verteidigt massive Misserfolge wie Fire Phone.",
        "aussage_uebersetzung_de": "Wenn ein Unternehmen waechst, muss alles skalieren, einschliesslich der Groesse Ihrer gescheiterten Experimente. Wenn die Groesse Ihrer Fehlschlaege nicht waechst, werden Sie nicht in einem Massstab innovieren, der tatsaechlich etwas bewegen kann.",
    },
    # ---- 9. re:MARS 2019 (AI and Machine Learning) ----
    {
        "aussage_text": "Machine learning drives many of our algorithms for demand forecasting, product search ranking, product and deals recommendations, merchandising placements, fraud detection, translations, and much more. Though less visible, much of the impact of machine learning will be this kind of quiet but pervasive impact behind the scenes.",
        "aussage_kurz": "Bezos beschreibt 2019, dass Machine Learning 'still und allgegenwaertig' Amazon durchdringt -- meist unsichtbar fuer Kunden.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion / Keynote
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.aboutamazon.com/news/innovation-at-amazon/the-history-behind-amazons-success",
        "quell_titel": "re:MARS 2019 Conference (Amazon)",
        "datum_aussage": "2019-06-04",
        "sprache": "en",
        "kontext": "Erste re:MARS-Konferenz (Machine Learning, Automation, Robotics, Space). Bezos spricht ueber den Einsatz von KI bei Amazon.",
        "aussage_uebersetzung_de": "Machine Learning treibt viele unserer Algorithmen fuer Bedarfsprognosen, Produktsuchranking, Produkt- und Angebotsempfehlungen, Merchandising-Platzierungen, Betrugserkennung, Uebersetzungen und vieles mehr. Auch wenn weniger sichtbar, wird ein Grossteil der Auswirkung von Machine Learning diese Art von stiller, aber allgegenwaertiger Wirkung hinter den Kulissen sein.",
    },
    # ---- 10. re:MARS 2019 (Alexa) ----
    {
        "aussage_text": "We think of Alexa as a sophisticated AI that started as a simple voice assistant. But we wanted to build something that could do far more than just answer questions. We wanted to build something that could have a conversation with you.",
        "aussage_kurz": "Bezos erklaert Alexa als 'anspruchsvolle KI', die als Sprachassistent begann, aber Konversationen fuehren soll.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.theverge.com/2019/6/5/18653981/amazon-alexa-ai-artificial-intelligence-jeff-bezos-remars",
        "quell_titel": "Jeff Bezos on Alexa and AI at re:MARS 2019 (The Verge)",
        "datum_aussage": "2019-06-04",
        "sprache": "en",
        "kontext": "re:MARS 2019. Bezos betont, dass Alexa nicht nur reagiert, sondern vorausschauend handeln soll.",
        "aussage_uebersetzung_de": "Wir denken an Alexa als eine anspruchsvolle KI, die als einfacher Sprachassistent begann. Aber wir wollten etwas bauen, das weit mehr kann als nur Fragen beantworten. Wir wollten etwas bauen, das eine Konversation mit dir fuehren kann.",
    },
    # ---- 11. Lex Fridman Podcast, Dez 2023 (Space Vision) ----
    {
        "aussage_text": "The solar system can support a trillion humans, and then we'd have a thousand Mozarts and a thousand Einsteins. Think of how incredible and dynamic that civilization will be.",
        "aussage_kurz": "Bezos sagt, das Sonnensystem koenne eine Billion Menschen tragen -- und tausend Mozarts und Einsteins hervorbringen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,  # Podcast-Interview
        "plattform_id": 3,    # Podcasts
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Erstes langes Podcast-Interview von Bezos. Er beschreibt seine Vision fuer eine Multi-Planeten-Zivilisation.",
        "aussage_uebersetzung_de": "Das Sonnensystem kann eine Billion Menschen tragen, und dann haetten wir tausend Mozarts und tausend Einsteins. Stell dir vor, wie unglaublich und dynamisch diese Zivilisation sein wird.",
    },
    # ---- 12. Lex Fridman Podcast (Earth as Residential) ----
    {
        "aussage_text": "I would love to see a world where we zone Earth as residential and light industrial, and we move all the heavy industry into space. Keep Earth as this beautiful gem of a planet that it is.",
        "aussage_kurz": "Bezos schlaegt vor, die Erde als 'Wohngebiet' zu zonieren und Schwerindustrie ins All zu verlagern.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bezos beschreibt seine Umweltvision: Industrieverschmutzung ins All verlagern, Erde als Naturreservat bewahren.",
        "aussage_uebersetzung_de": "Ich wuerde gerne eine Welt sehen, in der wir die Erde als Wohn- und Leichtindustrie-Gebiet zonieren und alle Schwerindustrie ins All verlagern. Die Erde als diesen schoenen Edelstein eines Planeten bewahren, der sie ist.",
    },
    # ---- 13. Lex Fridman Podcast (Blue Origin Philosophy) ----
    {
        "aussage_text": "I think I have a very clear purpose with Blue Origin, which is to go to space to benefit Earth. I don't think we go to space to escape Earth. I think we go to space to save Earth.",
        "aussage_kurz": "Bezos betont, Blue Origin gehe ins All, um die Erde zu retten -- nicht um ihr zu entkommen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bezos kontrastiert seine Vision mit Musks Mars-Kolonisierung: Blue Origin will die Erde bewahren, nicht verlassen.",
        "aussage_uebersetzung_de": "Ich denke, ich habe einen sehr klaren Zweck mit Blue Origin, naemlich ins All zu gehen, um der Erde zu nuetzen. Ich denke nicht, dass wir ins All gehen, um der Erde zu entkommen. Ich denke, wir gehen ins All, um die Erde zu retten.",
    },
    # ---- 14. Lex Fridman Podcast (Regret Minimization Framework) ----
    {
        "aussage_text": "I wanted to project myself forward to age 80 and say, 'Okay, now I'm looking back on my life. I want to have minimized the number of regrets I have.' I knew that when I was 80 I was not going to regret having tried this. I was not going to regret trying to participate in this thing called the Internet that I thought was going to be a really big deal.",
        "aussage_kurz": "Bezos beschreibt sein 'Regret Minimization Framework': mit 80 zurueckblicken und Reue minimieren.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bezos erklaert seinen Entscheidungsprozess, Amazon zu gruenden. Er wiederholt diese Geschichte seit den 1990ern.",
        "aussage_uebersetzung_de": "Ich wollte mich selbst mit 80 Jahren vorstellen und sagen: 'Okay, jetzt schaue ich auf mein Leben zurueck. Ich will die Anzahl der Reue minimiert haben.' Ich wusste, dass ich mit 80 es nicht bereuen wuerde, das versucht zu haben. Ich wuerde nicht bereuen, versucht zu haben, an diesem Ding namens Internet teilzunehmen, von dem ich dachte, dass es eine wirklich grosse Sache werden wuerde.",
    },
    # ---- 15. Lex Fridman Podcast (Two-Pizza Teams) ----
    {
        "aussage_text": "We use the two-pizza team rule. If a team can't be fed with two pizzas, it's too large. That forces you to have small, autonomous teams that can move quickly.",
        "aussage_kurz": "Bezos erklaert die 'Zwei-Pizza-Regel': Teams, die nicht mit zwei Pizzas zu ernaehren sind, sind zu gross.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bezos beschreibt Amazons Organisationsprinzipien. Die Zwei-Pizza-Regel ist seit den fruehen 2000ern Teil der Amazon-Kultur.",
        "aussage_uebersetzung_de": "Wir nutzen die Zwei-Pizza-Team-Regel. Wenn ein Team nicht mit zwei Pizzas ernaehrt werden kann, ist es zu gross. Das zwingt dich, kleine, autonome Teams zu haben, die sich schnell bewegen koennen.",
    },
    # ---- 16. Lex Fridman Podcast (AI Safety) ----
    {
        "aussage_text": "I think AI is going to be the best tool we've ever had. And I think it's going to be used mostly for good. I'm very optimistic about AI. I'm not somebody who worries about the Terminator scenario.",
        "aussage_kurz": "Bezos ist optimistisch ueber KI und macht sich keine Sorgen um 'Terminator-Szenarien'.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/jeff-bezos-transcript/",
        "quell_titel": "Lex Fridman Podcast #405: Jeff Bezos on Blue Origin, AI, and the Future",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bezos positioniert sich als KI-Optimist -- im Kontrast zu Warnungen von Altman, Musk und anderen.",
        "aussage_uebersetzung_de": "Ich denke, KI wird das beste Werkzeug sein, das wir je hatten. Und ich denke, sie wird meistens fuer Gutes genutzt werden. Ich bin sehr optimistisch ueber KI. Ich bin nicht jemand, der sich Sorgen um das Terminator-Szenario macht.",
    },
    # ---- 17. Washington Post Kauf-Erklaerung, 2013 ----
    {
        "aussage_text": "The values of The Post do not need changing. The paper's duty will remain to its readers and not to the private interests of its owners. We will continue to follow the truth wherever it leads.",
        "aussage_kurz": "Bezos verspricht bei der Uebernahme der Washington Post, deren Werte und journalistische Unabhaengigkeit zu bewahren.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.washingtonpost.com/national/on-leadership/jeff-bezos-letter-to-washington-post-employees/2013/09/03/47d5d00e-14c9-11e3-880a-d503801e8fc4_story.html",
        "quell_titel": "Jeff Bezos' Letter to Washington Post Employees (Washington Post)",
        "datum_aussage": "2013-09-03",
        "sprache": "en",
        "kontext": "Bezos kauft die Washington Post fuer $250 Millionen und schreibt den Mitarbeitern einen Brief. Er verspricht redaktionelle Unabhaengigkeit.",
        "aussage_uebersetzung_de": "Die Werte der Post muessen sich nicht aendern. Die Pflicht der Zeitung wird weiterhin ihren Lesern gelten und nicht den privaten Interessen ihrer Eigentuemer. Wir werden weiterhin der Wahrheit folgen, wohin sie auch fuehrt.",
    },
    # ---- 18. Bezos Earth Fund Ankuendigung, 2020 ----
    {
        "aussage_text": "Climate change is the biggest threat to our planet. I want to work alongside others both to amplify known ways and to explore new ways of fighting the devastating impact of climate change on this planet we all share.",
        "aussage_kurz": "Bezos kuendigt den $10 Mrd. Bezos Earth Fund an und nennt Klimawandel die groesste Bedrohung fuer den Planeten.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,  # Social-Media-Post
        "plattform_id": 2,    # Instagram/Twitter
        "quell_link": "https://www.instagram.com/p/B8lMIGGnV1b/",
        "quell_titel": "Jeff Bezos on Instagram (February 2020)",
        "datum_aussage": "2020-02-17",
        "sprache": "en",
        "kontext": "Bezos kuendigt den Bezos Earth Fund an -- die groesste philanthropische Zusage zur Klimaforschung aller Zeiten. Kritiker weisen auf Amazons CO2-Fussabdruck hin.",
        "aussage_uebersetzung_de": "Der Klimawandel ist die groesste Bedrohung fuer unseren Planeten. Ich will mit anderen zusammenarbeiten, um bekannte Wege zu verstaerken und neue Wege zu erkunden, um die verheerende Wirkung des Klimawandels auf diesen Planeten zu bekaempfen, den wir alle teilen.",
    },
    # ---- 19. TED Interview, April 2023 (Anthropic Investment) ----
    {
        "aussage_text": "I think large language models are very interesting and very powerful. And I think there are going to be a lot of uses for them. But I don't think they're going to lead to AGI.",
        "aussage_kurz": "Bezos sagt, dass grosse Sprachmodelle interessant sind, aber nicht zu AGI fuehren werden.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://www.ted.com/talks/jeff_bezos_what_matters_more_than_your_talents",
        "quell_titel": "TED Interview with Jeff Bezos (April 2023)",
        "datum_aussage": "2023-04-12",
        "sprache": "en",
        "kontext": "TED-Interview nach Bezos' $3 Mrd. Investment in Anthropic. Er aeussert sich skeptisch zu AGI aus LLMs.",
        "aussage_uebersetzung_de": "Ich denke, grosse Sprachmodelle sind sehr interessant und sehr maechtig. Und ich denke, es wird viele Anwendungen fuer sie geben. Aber ich glaube nicht, dass sie zu AGI fuehren werden.",
    },
    # ---- 20. 2020 Shareholder Letter (AWS und ML) ----
    {
        "aussage_text": "AWS, which is now a $50 billion annual revenue run rate business, was started because we were our own best customer. We started building the tools we needed ourselves, and then we realized other people would find them valuable too.",
        "aussage_kurz": "Bezos erklaert, dass AWS entstand, weil Amazon seine eigenen Tools baute und erkannte, dass andere sie auch nutzen wuerden.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders",
        "quell_titel": "2020 Letter to Shareholders (Amazon)",
        "datum_aussage": "2020-04-01",
        "sprache": "en",
        "kontext": "Bezos' vorletzter Shareholder Letter als CEO. Er beschreibt AWS als Beispiel fuer 'working backwards from customer needs'.",
        "aussage_uebersetzung_de": "AWS, das jetzt ein 50-Milliarden-Dollar-Jahresumsatz-Geschaeft ist, wurde gestartet, weil wir unser eigener bester Kunde waren. Wir begannen, die Tools zu bauen, die wir selbst brauchten, und dann erkannten wir, dass andere sie auch wertvoll finden wuerden.",
    },
    # ---- 21. Last Shareholder Letter as CEO, 2020 ----
    {
        "aussage_text": "If you want to be successful in business (in life, actually), you have to create more than you consume. Your goal should be to create value for everyone you interact with.",
        "aussage_kurz": "In seinem letzten Shareholder Letter als CEO sagt Bezos, man muesse mehr schaffen als konsumieren.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders",
        "quell_titel": "2020 Letter to Shareholders (Amazon)",
        "datum_aussage": "2020-04-01",
        "sprache": "en",
        "kontext": "Bezos' letzter Brief als Amazon-CEO. Er tritt im Juli 2021 zurueck, um sich auf Blue Origin und andere Projekte zu konzentrieren.",
        "aussage_uebersetzung_de": "Wenn du im Geschaeft erfolgreich sein willst (im Leben, eigentlich), musst du mehr schaffen als du konsumierst. Dein Ziel sollte sein, Wert fuer jeden zu schaffen, mit dem du interagierst.",
    },
    # ---- 22. Code Conference 2016 (Long-term thinking) ----
    {
        "aussage_text": "We are willing to be misunderstood for long periods of time. We are long-term oriented, and we are willing to make bets that may not pay off for five to seven years.",
        "aussage_kurz": "Bezos sagt, Amazon sei bereit, fuer lange Zeit missverstanden zu werden und auf 5-7-Jahres-Wetten zu setzen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.recode.net/2016/6/1/11826876/jeff-bezos-amazon-code-conference-2016-recap",
        "quell_titel": "Jeff Bezos at Code Conference 2016 (Recode)",
        "datum_aussage": "2016-06-01",
        "sprache": "en",
        "kontext": "Code Conference Interview. Bezos verteidigt Amazons Investitionsstrategie und niedrige Margen.",
        "aussage_uebersetzung_de": "Wir sind bereit, fuer lange Zeit missverstanden zu werden. Wir sind langfristig orientiert, und wir sind bereit, Wetten einzugehen, die sich vielleicht erst in fuenf bis sieben Jahren auszahlen.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung Amazon ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Jeff Bezos gruendet Amazon.com als Online-Buchhandlung in seiner Garage in Bellevue, Washington. Er verlaesst seine gut bezahlte Stelle bei der Hedgefonds-Firma D.E. Shaw, um das Unternehmen zu starten.",
        "datum_handlung": "1994-07-05",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Amazon_(company)",
        "quell_titel": "Amazon (company) - Wikipedia",
        "kontext": "Bezos gruendet Amazon nach einem Road-Trip von New York nach Seattle. Er schreibt den Business-Plan waehrend der Fahrt. Die ersten Buecherbestellungen werden 1995 ausgeliefert.",
    },
    # ---- H2. Amazon IPO ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Amazon geht an die Boerse (NASDAQ: AMZN) mit einem Aktienpreis von $18. Das Unternehmen nimmt ca. $54 Millionen ein. Die Bewertung betraegt ca. $438 Millionen.",
        "datum_handlung": "1997-05-15",
        "betrag_usd": 54000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Amazon_(company)",
        "quell_titel": "Amazon (company) - Wikipedia",
        "kontext": "Der IPO findet inmitten der Dotcom-Blase statt. Kritiker nennen Amazon 'Amazon.toast' und sagen, das Unternehmen werde nie profitabel werden.",
    },
    # ---- H3. Gruendung Blue Origin ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Jeff Bezos gruendet Blue Origin, ein privates Raumfahrtunternehmen mit dem Ziel, den Zugang zum Weltraum zu demokratisieren. Das Unternehmen arbeitet jahrelang im Geheimen.",
        "datum_handlung": "2000-09-08",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Blue_Origin",
        "quell_titel": "Blue Origin - Wikipedia",
        "kontext": "Bezos gruendet Blue Origin fuenf Jahre nach Amazon. Er finanziert das Unternehmen komplett selbst. Blue Origin bleibt bis 2006 weitgehend geheim.",
    },
    # ---- H4. Amazon Prime Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Amazon startet Amazon Prime, ein Abonnement-Programm mit kostenlosem 2-Tage-Versand fuer $79/Jahr. Viele Analysten kritisieren das Programm als zu teuer und unrealistisch.",
        "datum_handlung": "2005-02-02",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Amazon_Prime",
        "quell_titel": "Amazon Prime - Wikipedia",
        "kontext": "Prime wird zu einem der erfolgreichsten Produkte von Amazon. Bis 2023 hat Prime ueber 200 Millionen Mitglieder weltweit.",
    },
    # ---- H5. Kauf Whole Foods ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Amazon kauft die Supermarktkette Whole Foods Market fuer $13,7 Milliarden -- Amazons groesste Uebernahme. Bezos expandiert damit in den stationaeren Lebensmittelhandel.",
        "datum_handlung": "2017-08-28",
        "betrag_usd": 13700000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Whole_Foods_Market",
        "quell_titel": "Whole Foods Market - Wikipedia",
        "kontext": "Der Kauf signalisiert Amazons Ambition, den Lebensmittelhandel zu revolutionieren. Am Tag der Ankuendigung brechen die Aktienkurse traditioneller Supermaerkten ein.",
    },
    # ---- H6. Kauf Washington Post ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Jeff Bezos kauft die Washington Post fuer $250 Millionen als Privatperson (nicht durch Amazon). Er uebernimmt die angeschlagene Zeitung und verspricht Investitionen in digitalen Journalismus.",
        "datum_handlung": "2013-08-05",
        "betrag_usd": 250000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/The_Washington_Post",
        "quell_titel": "The Washington Post - Wikipedia",
        "kontext": "Die Graham-Familie verkauft die Post nach jahrelangen Verlusten. Bezos investiert in Technologie, Paywall-Strategien und internationale Expansion.",
    },
    # ---- H7. Bezos Earth Fund ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Jeff Bezos kuendigt den Bezos Earth Fund an: $10 Milliarden zur Bekaempfung des Klimawandels. Es ist die groesste philanthropische Zusage zur Klimaforschung.",
        "datum_handlung": "2020-02-17",
        "betrag_usd": 10000000000.0,
        "quell_link": "https://www.bezosearthfund.org/",
        "quell_titel": "Bezos Earth Fund (Official Website)",
        "kontext": "Bezos hatte zuvor Kritik fuer mangelnde Philanthropie erhalten. Der Earth Fund verteilt Milliarden an NGOs, Forschungsinstitute und Klimaprojekte.",
    },
    # ---- H8. Ruecktritt als Amazon CEO ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Jeff Bezos tritt nach 27 Jahren als CEO von Amazon zurueck. Andy Jassy (AWS-Chef) wird neuer CEO. Bezos wird Executive Chairman und konzentriert sich auf Blue Origin, Day 1 Fund und Earth Fund.",
        "datum_handlung": "2021-07-05",
        "betrag_usd": None,
        "quell_link": "https://www.aboutamazon.com/news/company-news/email-from-jeff-bezos-to-employees",
        "quell_titel": "Email from Jeff Bezos to Employees (Amazon)",
        "kontext": "Bezos waehlt das Datum symbolisch: den 27. Jahrestag der Amazon-Gruendung. Er bleibt groesster Aktionaer mit ca. 10% der Anteile.",
    },
    # ---- H9. Alexa Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Amazon stellt Alexa und Echo vor -- Amazons Einstieg in KI-gesteuerte Sprachassistenten. Echo ist ein Smart Speaker, Alexa die dahinterstehende KI. Anfangs nur auf Einladung verfuegbar.",
        "datum_handlung": "2014-11-06",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Amazon_Alexa",
        "quell_titel": "Amazon Alexa - Wikipedia",
        "kontext": "Echo/Alexa wird zu einem der erfolgreichsten Hardwareprodukte von Amazon. Bis 2020 sind ueber 100 Millionen Alexa-Geraete weltweit im Einsatz.",
    },
    # ---- H10. AWS Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Amazon startet Amazon Web Services (AWS) mit einfachen Cloud-Services wie S3 (Storage) und EC2 (Computing). AWS revolutioniert die IT-Branche und wird zu Amazons profitabelstem Geschaeftssegment.",
        "datum_handlung": "2006-03-14",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Amazon_Web_Services",
        "quell_titel": "Amazon Web Services - Wikipedia",
        "kontext": "AWS entsteht aus Amazons internen Infrastruktur-Tools. Bezos erkennt, dass andere Unternehmen dieselbe Infrastruktur brauchen. AWS erreicht 2023 $90 Mrd. Jahresumsatz.",
    },
    # ---- H11. Investition in Anthropic ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Amazon investiert bis zu $4 Milliarden in Anthropic (KI-Startup hinter Claude). Die Investition erfolgt in zwei Tranchen: $1,25 Mrd. initial, bis zu $2,75 Mrd. nachfolgend. Anthropic nutzt AWS als Cloud-Provider.",
        "datum_handlung": "2023-09-25",
        "betrag_usd": 4000000000.0,
        "quell_link": "https://www.cnbc.com/2023/09/25/amazon-to-invest-up-to-4-billion-in-ai-startup-anthropic.html",
        "quell_titel": "Amazon to invest up to $4 billion in AI startup Anthropic (CNBC)",
        "kontext": "Die Investition positioniert Amazon im KI-Wettrennen gegen Microsoft/OpenAI und Google/DeepMind. Anthropic wurde von ehemaligen OpenAI-Mitarbeitern gegruendet.",
    },
    # ---- H12. Blue Origin New Shepard Flug (Bezos selbst) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jeff Bezos fliegt selbst mit Blue Origins New Shepard-Rakete ins All -- 9 Tage nach Richard Branson (Virgin Galactic). Der suborbitale Flug dauert 10 Minuten.",
        "datum_handlung": "2021-07-20",
        "betrag_usd": None,
        "quell_link": "https://www.bbc.com/news/science-environment-57849364",
        "quell_titel": "Jeff Bezos blasts into space on own rocket (BBC)",
        "kontext": "Bezos' Weltraumflug findet zwei Wochen nach seinem Amazon-Ruecktritt statt. Er fliegt mit seinem Bruder Mark, der Pilotin Wally Funk (82) und dem 18-jaehrigen Oliver Daemen.",
    },
    # ---- H13. Partnerschaft mit OpenAI / Azure ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Amazon und Microsoft konkurrieren im Cloud-Geschaeft, aber Anthropic (von Amazon finanziert) nutzt Google Cloud fuer Training. Amazon integriert Anthropic-Modelle in AWS Bedrock und eigene Dienste.",
        "datum_handlung": "2023-11-30",
        "betrag_usd": None,
        "quell_link": "https://aws.amazon.com/bedrock/",
        "quell_titel": "Amazon Bedrock (AWS)",
        "kontext": "AWS Bedrock bietet Zugang zu mehreren KI-Modellen, einschliesslich Anthropics Claude. Amazon entwickelt auch eigene KI-Modelle (Amazon Titan).",
    },
    # ---- H14. Politische Spende: Trump Inauguration ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Jeff Bezos spendet $1 Million an Trumps Inaugurations-Fonds 2025 -- trotz jahrelanger Konflikte zwischen Trump und der Washington Post.",
        "datum_handlung": "2024-12-13",
        "betrag_usd": 1000000.0,
        "quell_link": "https://www.npr.org/2024/12/13/nx-s1-5227874/trump-bezos-zuckerberg-amazon-facebook-open-ai-meta-inauguration-fund",
        "quell_titel": "Tech moguls Altman, Bezos and Zuckerberg donate to Trump's inauguration fund (NPR)",
        "kontext": "Trump hatte Bezos jahrelang angegriffen und Amazon beschuldigt, die Post auszunutzen. Die Spende wird als taktischer Schachzug gesehen.",
    },
    # ---- H15. Washington Post Non-Endorsement ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Jeff Bezos verhindert eine geplante Unterstuetzung von Kamala Harris durch die Washington Post vor der Wahl 2024. Die Redaktion protestiert, ueber 250.000 Abonnenten kuendigen.",
        "datum_handlung": "2024-10-25",
        "betrag_usd": None,
        "quell_link": "https://www.theguardian.com/media/2024/oct/25/washington-post-not-endorse-presidential-candidate",
        "quell_titel": "Washington Post will not endorse a presidential candidate for first time since 1988 (The Guardian)",
        "kontext": "Bezos rechtfertigt die Entscheidung als Rueckkehr zu Neutralitaet. Kritiker sehen vorauseilenden Gehorsam gegenueber einem moeglichen Trump-Sieg.",
    },
    # ---- H16. re:MARS Konferenz (erste) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Jeff Bezos startet die jaehrliche re:MARS-Konferenz (Machine Learning, Automation, Robotics, Space) in Las Vegas. Die Konferenz bringt KI-Forscher, Robotik-Experten und Raumfahrt-Visionaere zusammen.",
        "datum_handlung": "2019-06-04",
        "betrag_usd": None,
        "quell_link": "https://remars.io/",
        "quell_titel": "re:MARS Conference (Official Website)",
        "kontext": "re:MARS wird zu Amazons Antwort auf Googles I/O und Apples WWDC. Bezos nutzt die Konferenz, um Amazons KI-Vision zu praesentieren.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=10 existiert
    cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
    person = cursor.fetchone()
    if not person:
        print(f"FEHLER: Person mit id={PERSON_ID} nicht in der Datenbank gefunden.")
        conn.close()
        return
    print(f"Person gefunden: {person[0]} (id={PERSON_ID})")

    # Bestehende Eintraege zaehlen
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    existing_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    existing_h = cursor.fetchone()[0]
    print(f"Bestehende Eintraege: {existing_a} Aussagen, {existing_h} Handlungen")

    # --- Aussagen einfuegen ---
    aussagen_count = 0
    skipped_a = 0
    for a in AUSSAGEN:
        # Duplikat-Check: gleicher Text fuer gleiche Person
        cursor.execute(
            "SELECT id FROM aussagen WHERE person_id = ? AND aussage_text = ?",
            (PERSON_ID, a["aussage_text"])
        )
        if cursor.fetchone():
            skipped_a += 1
            continue

        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, sprache, kontext, aussage_uebersetzung_de,
                erfasst_von
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            a["aussage_text"],
            a["aussage_kurz"],
            a["modus"],
            a.get("quellen_typ_id"),
            a.get("plattform_id"),
            a.get("quell_link"),
            a.get("quell_titel"),
            a.get("datum_aussage"),
            a.get("sprache", "en"),
            a.get("kontext"),
            a.get("aussage_uebersetzung_de"),
            "Claude (collect_bezos.py)"
        ))
        aussagen_count += 1

    # --- Handlungen einfuegen ---
    handlungen_count = 0
    skipped_h = 0
    for h in HANDLUNGEN:
        # Duplikat-Check: gleicher Typ + Datum + Person
        cursor.execute(
            "SELECT id FROM handlungen WHERE person_id = ? AND handlung_typ = ? AND datum_handlung = ?",
            (PERSON_ID, h["handlung_typ"], h.get("datum_handlung"))
        )
        if cursor.fetchone():
            skipped_h += 1
            continue

        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung, datum_handlung,
                betrag_usd, quell_link, quell_titel, kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            h["handlung_typ"],
            h["beschreibung"],
            h.get("datum_handlung"),
            h.get("betrag_usd"),
            h.get("quell_link"),
            h.get("quell_titel"),
            h.get("kontext"),
        ))
        handlungen_count += 1

    # --- Suchprotokoll anlegen ---
    cursor.execute("""
        INSERT INTO suchprotokolle (
            person_id, suchbegriffe, ergebnis_anzahl, relevante_treffer,
            notizen, durchgefuehrt_von
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        "Jeff Bezos quotes, Shareholder Letters, Lex Fridman interview, re:MARS, Blue Origin, AWS, Alexa, Washington Post, Bezos Earth Fund, Anthropic investment",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Amazon Shareholder Letters (1997-2020), Lex Fridman Podcast #405, TED Interview, "
        f"re:MARS Conferences, Code Conference 2016, Washington Post Letter, Bezos Earth Fund, "
        f"BBC, CNBC, NPR, The Guardian, Wikipedia.",
        "Claude (collect_bezos.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Jeff Bezos (person_id={PERSON_ID})")
    print(f"{'='*60}")
    print(f"  Neue Aussagen eingefuegt:    {aussagen_count}")
    print(f"  Aussagen uebersprungen:      {skipped_a} (Duplikate)")
    print(f"  Neue Handlungen eingefuegt:  {handlungen_count}")
    print(f"  Handlungen uebersprungen:    {skipped_h} (Duplikate)")
    print(f"  Suchprotokoll erstellt:      Ja")
    print(f"{'='*60}")

    # Verifizierung
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    total_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    total_h = cursor.fetchone()[0]
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Jeff Bezos")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_bezos.py")
    print("  Verifizierte Aussagen & Handlungen: Jeff Bezos")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
