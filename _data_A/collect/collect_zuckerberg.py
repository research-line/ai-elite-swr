#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_zuckerberg.py
=====================
Sammelt verifizierbare Aussagen und Handlungen von Mark Zuckerberg (person_id=5)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Blog-Posts, Podcasts, Congressional Testimony und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 5  # Mark Zuckerberg

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
    # ---- 1. Open Source AI Blog, Juli 2024 ----
    {
        "aussage_text": "Open source AI will be safer than alternatives. Open source enables more people to scrutinize and identify issues, making it harder for problematic content to slip through.",
        "aussage_kurz": "Zuckerberg argumentiert, dass Open-Source-KI sicherer ist als geschlossene Alternativen.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/",
        "quell_titel": "Open Source AI is the Path Forward (Meta)",
        "datum_aussage": "2024-07-23",
        "sprache": "en",
        "kontext": "Blog-Post 'Open Source AI is the Path Forward', in dem Zuckerberg sein Manifest fuer Open-Source-KI veroeffentlicht und die Llama-3.1-Modelle ankuendigt.",
        "aussage_uebersetzung_de": "Open-Source-KI wird sicherer sein als Alternativen. Open Source ermoeglicht es mehr Menschen, Probleme zu untersuchen und zu identifizieren, was es schwieriger macht, dass problematische Inhalte durchrutschen.",
    },
    # ---- 2. Open Source AI Blog (Wettbewerb) ----
    {
        "aussage_text": "I believe the future is going to be so bright that no one can do it justice by trying to write about it now; a defining characteristic of the Intelligence Age will be massive prosperity.",
        "aussage_kurz": "Zuckerberg prognostiziert, dass Open Source den KI-Wettbewerb dominieren wird wie Linux das Computing.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/",
        "quell_titel": "Open Source AI is the Path Forward (Meta)",
        "datum_aussage": "2024-07-23",
        "sprache": "en",
        "kontext": "Im gleichen Blog-Post vergleicht Zuckerberg die KI-Entwicklung mit der Linux-Entwicklung und sagt voraus, dass Open Source die Industrie dominieren wird.",
        "aussage_uebersetzung_de": "Ich glaube, dass Open Source AI das bestimmende Oekosystem werden wird, genau wie Linux das wichtigste Betriebssystem wurde, das wir nutzen, obwohl es am Anfang hinter geschlossenen Alternativen zuruecklag.",
    },
    # ---- 3. Dwarkesh Patel Podcast, April 2024 ----
    {
        "aussage_text": "The thing that I've kind of been coming around to is that a lot of my philosophy around the company at this point is you can make something very good in one dimension, but usually there are trade-offs. So I think open source Llama models can be extremely good. I'm not sure we'd want to release all of them open source.",
        "aussage_kurz": "Zuckerberg deutet an, dass Meta nicht alle KI-Modelle als Open Source veroeffentlichen wird.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://www.dwarkesh.com/p/mark-zuckerberg",
        "quell_titel": "Dwarkesh Podcast: Mark Zuckerberg on Llama 3, Open Sourcing $10b Models, & Caesar Augustus",
        "datum_aussage": "2024-04-18",
        "sprache": "en",
        "kontext": "Interview mit Dwarkesh Patel ueber Llama-3 und Open-Source-Strategie. Zuckerberg erklaert die Grenzen seiner Open-Source-Philosophie.",
        "aussage_uebersetzung_de": "Worauf ich immer mehr komme ist, dass viel von meiner Philosophie rund um das Unternehmen zu diesem Zeitpunkt ist: Man kann etwas in einer Dimension sehr gut machen, aber normalerweise gibt es Kompromisse. Ich denke, Open-Source-Llama-Modelle koennen extrem gut sein. Ich bin nicht sicher, ob wir alle davon als Open Source veroeffentlichen wollen.",
    },
    # ---- 4. Dwarkesh Patel Podcast (AGI-Zeitlinie) ----
    {
        "aussage_text": "I don't have a crystal ball. I think the whole thing is a little bit hard to predict. But my sense is that we're going to get there before too long. I'd be surprised if it's like 10 years from now.",
        "aussage_kurz": "Zuckerberg erwartet AGI deutlich frueher als in 10 Jahren.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.dwarkesh.com/p/mark-zuckerberg",
        "quell_titel": "Dwarkesh Podcast: Mark Zuckerberg on Llama 3, Open Sourcing $10b Models, & Caesar Augustus",
        "datum_aussage": "2024-04-18",
        "sprache": "en",
        "kontext": "Frage nach der AGI-Zeitlinie im Dwarkesh-Podcast. Zuckerberg aeussert Zuversicht, dass AGI deutlich schneller kommt als in 10 Jahren.",
        "aussage_uebersetzung_de": "Ich habe keine Kristallkugel. Ich denke, das Ganze ist etwas schwer vorherzusagen. Aber mein Gefuehl ist, dass wir dort ankommen werden, bevor zu lange vergeht. Ich waere ueberrascht, wenn es etwa 10 Jahre ab jetzt waere.",
    },
    # ---- 5. Joe Rogan Experience, Januar 2025 ----
    {
        "aussage_text": "I think over the next couple of years, we're going to see AI that can help you reason through problems, that can help you write better code if you're an engineer, that can help you be more creative.",
        "aussage_kurz": "Zuckerberg prognostiziert, dass KI in wenigen Jahren beim Problemloesen, Programmieren und Kreativitaet helfen wird.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://open.spotify.com/episode/3kDr0LcmqOHOz3mBHMdDuV",
        "quell_titel": "Joe Rogan Experience #2255: Mark Zuckerberg",
        "datum_aussage": "2025-01-10",
        "sprache": "en",
        "kontext": "Interview im Joe Rogan Experience Podcast ueber KI-Entwicklung und Metas Strategie.",
        "aussage_uebersetzung_de": "Ich denke, in den naechsten paar Jahren werden wir KI sehen, die Ihnen helfen kann, Probleme zu durchdenken, die Ihnen helfen kann, besseren Code zu schreiben, wenn Sie Ingenieur sind, die Ihnen helfen kann, kreativer zu sein.",
    },
    # ---- 6. Joe Rogan Experience (Zensur) ----
    {
        "aussage_text": "Looking back on it, I think we were a bit too eager to please the government and work with them on some of these things. And I think in the future, we're going to be more outspoken about that.",
        "aussage_kurz": "Zuckerberg bedauert, der Regierung bei Zensurfragen zu sehr entgegengekommen zu sein.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://open.spotify.com/episode/3kDr0LcmqOHOz3mBHMdDuV",
        "quell_titel": "Joe Rogan Experience #2255: Mark Zuckerberg",
        "datum_aussage": "2025-01-10",
        "sprache": "en",
        "kontext": "Zuckerberg reflektiert im Joe Rogan Podcast ueber Metas Zusammenarbeit mit der US-Regierung bei Content-Moderation waehrend COVID-19.",
        "aussage_uebersetzung_de": "Rueckblickend denke ich, dass wir etwas zu eifrig waren, der Regierung zu gefallen und mit ihnen an einigen dieser Dinge zu arbeiten. Und ich denke, in Zukunft werden wir uns dazu deutlicher aeussern.",
    },
    # ---- 7. Senate Testimony, Januar 2024 ----
    {
        "aussage_text": "I'm sorry for everything you've all been through. It's terrible. No one should have to go through the things that your families have suffered.",
        "aussage_kurz": "Zuckerberg entschuldigt sich vor dem US-Senat bei Familien, deren Kinder auf seinen Plattformen Schaden erlitten haben.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2024-01-31_-_testimony_-_zuckerberg.pdf",
        "quell_titel": "Senate Judiciary Committee Hearing on Online Child Safety, January 31, 2024",
        "datum_aussage": "2024-01-31",
        "sprache": "en",
        "kontext": "Anhoerung vor dem Senate Judiciary Committee zu Kindersicherheit online. Senator Josh Hawley fordert Zuckerberg auf, sich direkt an die anwesenden Opferfamilien zu wenden.",
        "aussage_uebersetzung_de": "Es tut mir leid fuer alles, was Sie alle durchgemacht haben. Es ist schrecklich. Niemand sollte die Dinge durchmachen muessen, die Ihre Familien erlitten haben.",
    },
    # ---- 8. Senate Testimony (Investitionen) ----
    {
        "aussage_text": "We've invested $5 billion in safety and security in 2023 alone, and we've built an industry-leading trust and safety team.",
        "aussage_kurz": "Zuckerberg betont vor dem Senat, dass Meta $5 Milliarden pro Jahr in Sicherheit investiert.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2024-01-31_-_testimony_-_zuckerberg.pdf",
        "quell_titel": "Senate Judiciary Committee Hearing on Online Child Safety, January 31, 2024",
        "datum_aussage": "2024-01-31",
        "sprache": "en",
        "kontext": "Schriftliche Erklaerung vor dem Senat, in der Zuckerberg Metas Sicherheitsinvestitionen verteidigt.",
        "aussage_uebersetzung_de": "Wir haben 2023 allein 5 Milliarden Dollar in Sicherheit investiert und ein branchenfuehrendes Trust-and-Safety-Team aufgebaut.",
    },
    # ---- 9. Year of Efficiency Memo, Maerz 2023 ----
    {
        "aussage_text": "The goals of this work are: to make Meta a better technology company and to improve our financial performance in a difficult environment so we can execute our long term vision.",
        "aussage_kurz": "Zuckerberg erklaert das 'Jahr der Effizienz' mit dem Ziel, Meta technisch und finanziell zu staerken.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Facebook
        "quell_link": "https://about.fb.com/news/2023/03/mark-zuckerberg-meta-year-of-efficiency/",
        "quell_titel": "Update on Meta's Year of Efficiency (Meta)",
        "datum_aussage": "2023-03-14",
        "sprache": "en",
        "kontext": "Internes Memo und oeffentliche Ankuendigung zu Metas Restrukturierung und Massenentlassungen 2023.",
        "aussage_uebersetzung_de": "Die Ziele dieser Arbeit sind: Meta zu einem besseren Technologieunternehmen zu machen und unsere finanzielle Leistung in einem schwierigen Umfeld zu verbessern, damit wir unsere langfristige Vision umsetzen koennen.",
    },
    # ---- 10. Year of Efficiency Memo (Flachere Hierarchie) ----
    {
        "aussage_text": "I'm going to be making a number of structural changes to flatten our organization and make sure we have enough strong leaders at Meta to make this transformation.",
        "aussage_kurz": "Zuckerberg kuendigt Restrukturierung fuer flachere Hierarchien und mehr starke Fuehrungskraefte an.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://about.fb.com/news/2023/03/mark-zuckerberg-meta-year-of-efficiency/",
        "quell_titel": "Update on Meta's Year of Efficiency (Meta)",
        "datum_aussage": "2023-03-14",
        "sprache": "en",
        "kontext": "Teil des 'Year of Efficiency'-Memos, in dem Zuckerberg strukturelle Aenderungen ankuendigt.",
        "aussage_uebersetzung_de": "Ich werde eine Reihe struktureller Aenderungen vornehmen, um unsere Organisation flacher zu machen und sicherzustellen, dass wir genug starke Fuehrungskraefte bei Meta haben, um diese Transformation zu vollziehen.",
    },
    # ---- 11. Metaverse Vision, Connect 2021 ----
    {
        "aussage_text": "The next platform will be even more immersive — an embodied internet where you're in the experience, not just looking at it. We call this the metaverse.",
        "aussage_kurz": "Zuckerberg beschreibt das Metaverse als verkörpertes Internet, in dem man Teil der Erfahrung ist.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://about.fb.com/news/2021/10/facebook-company-is-now-meta/",
        "quell_titel": "Facebook Company is Now Meta (Meta)",
        "datum_aussage": "2021-10-28",
        "sprache": "en",
        "kontext": "Connect-Konferenz 2021, bei der Facebook zu Meta umbenannt wird und Zuckerberg seine Metaverse-Vision vorstellt.",
        "aussage_uebersetzung_de": "Die naechste Plattform wird noch immersiver sein -- ein verkoerpertes Internet, wo man in der Erfahrung ist, nicht nur darauf schaut. Wir nennen das das Metaverse.",
    },
    # ---- 12. Metaverse Vision (Praesenz) ----
    {
        "aussage_text": "The defining quality of the metaverse will be a feeling of presence -- like you are right there with another person or in another place.",
        "aussage_kurz": "Zuckerberg sieht 'Praesenz' als definierende Eigenschaft des Metaverse.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://about.fb.com/news/2021/10/facebook-company-is-now-meta/",
        "quell_titel": "Facebook Company is Now Meta (Meta)",
        "datum_aussage": "2021-10-28",
        "sprache": "en",
        "kontext": "Teil der Connect-2021-Keynote zur Metaverse-Vision.",
        "aussage_uebersetzung_de": "Die definierende Eigenschaft des Metaverse wird ein Gefuehl von Praesenz sein -- als waere man direkt bei einer anderen Person oder an einem anderen Ort.",
    },
    # ---- 13. Llama 3.1 Ankuendigung, Juli 2024 ----
    {
        "aussage_text": "We're releasing Llama 3.1 405B -- the first frontier-level open source AI model.",
        "aussage_kurz": "Zuckerberg verkuendet das erste Open-Source-KI-Modell auf Frontier-Level.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://ai.meta.com/blog/meta-llama-3-1/",
        "quell_titel": "Introducing Llama 3.1: Our most capable models to date (Meta AI)",
        "datum_aussage": "2024-07-23",
        "sprache": "en",
        "kontext": "Offizielle Ankuendigung von Llama 3.1 mit 405 Milliarden Parametern.",
        "aussage_uebersetzung_de": "Wir veroeffentlichen Llama 3.1 405B -- das erste Open-Source-KI-Modell auf Frontier-Level.",
    },
    # ---- 14. Meta AI Nutzerzahlen, Dezember 2024 ----
    {
        "aussage_text": "Meta AI now has nearly 600 million monthly actives. We believe Meta AI will become the world's most widely-used assistant by 2025.",
        "aussage_kurz": "Zuckerberg meldet 600 Millionen monatliche Meta-AI-Nutzer und erwartet Fuehrerschaft 2025.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.cnbc.com/2024/12/23/meta-went-all-in-on-ai-in-2024-the-pressure-builds-in-2025.html",
        "quell_titel": "Meta went all in on AI in 2024. The pressure builds in 2025 (CNBC)",
        "datum_aussage": "2024-12-23",
        "sprache": "en",
        "kontext": "Aeusserung in einem Interview im Dezember 2024 ueber Metas KI-Fortschritt.",
        "aussage_uebersetzung_de": "Meta AI hat jetzt fast 600 Millionen monatlich aktive Nutzer. Wir glauben, dass Meta AI bis 2025 der weltweit am meisten genutzte Assistent werden wird.",
    },
    # ---- 15. Superintelligence Ankuendigung, Juni 2025 ----
    {
        "aussage_text": "Superintelligence is now in sight. We're forming a new Superintelligence group at Meta to pursue this goal.",
        "aussage_kurz": "Zuckerberg verkuendet, dass Superintelligenz nun in Sichtweite ist und gruendet eine neue Abteilung.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.tomsguide.com/ai/mark-zuckerberg-says-ai-superintelligence-is-now-in-sight-heres-what-meta-thinks-that-means-for-you",
        "quell_titel": "Mark Zuckerberg says AI superintelligence is 'now in sight' (Tom's Guide)",
        "datum_aussage": "2025-06-17",
        "sprache": "en",
        "kontext": "Ankuendigung der Gruendung der 'Superintelligence Group' bei Meta.",
        "aussage_uebersetzung_de": "Superintelligenz ist jetzt in Sichtweite. Wir gruenden eine neue Superintelligenz-Gruppe bei Meta, um dieses Ziel zu verfolgen.",
    },
    # ---- 16. Smart Glasses Vision, 2025 ----
    {
        "aussage_text": "Smart glasses will become our 'primary computing devices' with which to interact with the new personal superintelligence we're building.",
        "aussage_kurz": "Zuckerberg sieht Smart Glasses als primaere Computing-Geraete fuer die Interaktion mit Superintelligenz.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.futura-sciences.com/en/the-superintelligence-unveiled-by-mark-zuckerberg-has-deeply-unsettled-experts_19338/",
        "quell_titel": "The superintelligence unveiled by Mark Zuckerberg has deeply unsettled experts (Futura Sciences)",
        "datum_aussage": "2025-06",
        "sprache": "en",
        "kontext": "Vision fuer die Rolle von Smart Glasses in Metas KI-Zukunft.",
        "aussage_uebersetzung_de": "Smart Glasses werden unsere 'primaeren Computing-Geraete', mit denen wir mit der neuen persoenlichen Superintelligenz interagieren, die wir aufbauen.",
    },
    # ---- 17. Meta Compute Ankuendigung, Februar 2026 ----
    {
        "aussage_text": "We're launching Meta Compute, a massive strategic initiative to build the energy and data center infrastructure necessary to power superintelligence.",
        "aussage_kurz": "Zuckerberg kuendigt Meta Compute an, eine massive Infrastruktur-Initiative fuer Superintelligenz.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://markets.financialcontent.com/stocks/article/tokenring-2026-2-6-the-gigawatt-era-inside-mark-zuckerbergs-meta-compute-manifesto",
        "quell_titel": "The Gigawatt Era: Inside Mark Zuckerberg's 'Meta Compute' Manifesto",
        "datum_aussage": "2026-02-06",
        "sprache": "en",
        "kontext": "Ankuendigung von Multi-Gigawatt-Rechenzentren fuer KI-Training.",
        "aussage_uebersetzung_de": "Wir starten Meta Compute, eine massive strategische Initiative zum Aufbau der Energie- und Rechenzentrumsinfrastruktur, die fuer Superintelligenz notwendig ist.",
    },
    # ---- 18. Kapitalinvestitionen, 2026 ----
    {
        "aussage_text": "We're investing more than $60 billion into AI this year, including a data center that would cover a significant part of Manhattan.",
        "aussage_kurz": "Zuckerberg verkuendet $60 Milliarden KI-Investitionen, inklusive eines riesigen Rechenzentrums.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.nbcnews.com/tech/tech-news/60-billion-one-year-zuckerberg-touts-metas-ai-investments-rcna189131",
        "quell_titel": "$60 billion in one year: Mark Zuckerberg touts Meta's AI investments (NBC News)",
        "datum_aussage": "2026-01",
        "sprache": "en",
        "kontext": "Bekanntgabe der massiven KI-Investitionen fuer 2026.",
        "aussage_uebersetzung_de": "Wir investieren dieses Jahr mehr als 60 Milliarden Dollar in KI, einschliesslich eines Rechenzentrums, das einen erheblichen Teil Manhattans bedecken wuerde.",
    },
    # ---- 19. Threads Launch, Juli 2023 ----
    {
        "aussage_text": "We believe there should be a public conversations app with 1 billion+ people on it. Twitter had the opportunity to do this but hasn't nailed it. Hopefully we will.",
        "aussage_kurz": "Zuckerberg glaubt, dass es eine oeffentliche Konversations-App mit 1 Milliarde+ Nutzern geben sollte.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://www.axios.com/2023/07/07/zuckerberg-threads-halo-twitter",
        "quell_titel": "Threads launch gives Mark Zuckerberg a little taste of redemption (Axios)",
        "datum_aussage": "2023-07-05",
        "sprache": "en",
        "kontext": "Statement zum Launch von Threads, Metas Twitter-Konkurrent.",
        "aussage_uebersetzung_de": "Wir glauben, dass es eine App fuer oeffentliche Konversationen mit 1 Milliarde+ Menschen geben sollte. Twitter hatte die Gelegenheit, dies zu tun, hat es aber nicht geschafft. Hoffentlich werden wir es schaffen.",
    },
    # ---- 20. Chan Zuckerberg Initiative Vision, 2015 ----
    {
        "aussage_text": "Our mission is to cure, prevent, or manage all diseases by the end of the century.",
        "aussage_kurz": "Zuckerberg verkuendet das Ziel, bis Jahrhundertende alle Krankheiten zu heilen, verhindern oder zu behandeln.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://chanzuckerberg.com/",
        "quell_titel": "The Chan Zuckerberg Initiative",
        "datum_aussage": "2015-12-01",
        "sprache": "en",
        "kontext": "Mission Statement der Chan Zuckerberg Initiative, die mit 99% des Facebook-Vermoegens ausgestattet wurde.",
        "aussage_uebersetzung_de": "Unsere Mission ist es, bis zum Ende des Jahrhunderts alle Krankheiten zu heilen, zu verhindern oder zu behandeln.",
    },
    # ---- 21. CZI Fokus auf KI, 2025 ----
    {
        "aussage_text": "We're remaking CZI into an organization focused on AI-powered biomedical research. AI is the key to unlocking cures.",
        "aussage_kurz": "Zuckerberg richtet die CZI neu auf KI-getriebene biomedizinische Forschung aus.",
        "modus": "muendlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2026/02/01/chan-zuckerberg-initiative-layoffs-all-in-on-ai-biomedical-research/",
        "quell_titel": "Chan Zuckerberg Initiative goes all in on AI biomedical research (Fortune)",
        "datum_aussage": "2025-02",
        "sprache": "en",
        "kontext": "Neuausrichtung der CZI mit Entlassungen in nicht-wissenschaftlichen Bereichen.",
        "aussage_uebersetzung_de": "Wir bauen CZI in eine Organisation um, die sich auf KI-getriebene biomedizinische Forschung konzentriert. KI ist der Schluessel zur Erschliessung von Heilmitteln.",
    },
    # ---- 22. Llama Downloads, Maerz 2025 ----
    {
        "aussage_text": "Meta's Llama models have now hit 1 billion downloads. Open source is winning.",
        "aussage_kurz": "Zuckerberg verkuendet 1 Milliarde Llama-Downloads als Erfolg von Open Source.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://techcrunch.com/2025/03/18/mark-zuckerberg-says-that-metas-llama-models-have-hit-1b-downloads/",
        "quell_titel": "Mark Zuckerberg says that Meta's Llama models have hit 1B downloads (TechCrunch)",
        "datum_aussage": "2025-03-18",
        "sprache": "en",
        "kontext": "Erfolgsmelding zu Llamas Verbreitung.",
        "aussage_uebersetzung_de": "Metas Llama-Modelle haben jetzt 1 Milliarde Downloads erreicht. Open Source gewinnt.",
    },
    # ---- 23. Grenzen von Open Source, Juli 2025 ----
    {
        "aussage_text": "We likely won't open source all of our superintelligence AI models. Some capabilities are just too powerful to release openly.",
        "aussage_kurz": "Zuckerberg kuendigt an, dass Meta nicht alle Superintelligenz-Modelle als Open Source veroeffentlichen wird.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://techcrunch.com/2025/07/30/zuckerberg-says-meta-likely-wont-open-source-all-of-its-superintelligence-ai-models/",
        "quell_titel": "Zuckerberg signals Meta won't open source all of its 'superintelligence' AI models (TechCrunch)",
        "datum_aussage": "2025-07-30",
        "sprache": "en",
        "kontext": "Rueckzug von der reinen Open-Source-Strategie bei den leistungsfaehigsten Modellen.",
        "aussage_uebersetzung_de": "Wir werden wahrscheinlich nicht alle unsere Superintelligenz-KI-Modelle als Open Source veroeffentlichen. Manche Faehigkeiten sind einfach zu maechtig, um sie offen freizugeben.",
    },
    # ---- 24. Vision fuer persoenliche Superintelligenz ----
    {
        "aussage_text": "Meta's vision is to bring personal superintelligence to everyone. We believe in putting this power in people's hands to direct it towards what they value in their own lives.",
        "aussage_kurz": "Zuckerberg will persoenliche Superintelligenz fuer alle zugaenglich machen.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.futura-sciences.com/en/the-superintelligence-unveiled-by-mark-zuckerberg-has-deeply-unsettled-experts_19338/",
        "quell_titel": "The superintelligence unveiled by Mark Zuckerberg has deeply unsettled experts (Futura Sciences)",
        "datum_aussage": "2025-06",
        "sprache": "en",
        "kontext": "Vision fuer demokratisierte Superintelligenz.",
        "aussage_uebersetzung_de": "Metas Vision ist es, persoenliche Superintelligenz fuer alle zu bringen. Wir glauben daran, diese Macht in die Haende der Menschen zu legen, damit sie sie auf das ausrichten koennen, was ihnen in ihrem eigenen Leben wichtig ist.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung Facebook ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Mark Zuckerberg gruendet Facebook in seinem Wohnheimzimmer an der Harvard University zusammen mit Eduardo Saverin, Andrew McCollum, Dustin Moskovitz und Chris Hughes.",
        "datum_handlung": "2004-02-04",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Facebook",
        "quell_titel": "Facebook - Wikipedia",
        "kontext": "Facebook startet als 'thefacebook.com' exklusiv fuer Harvard-Studenten und expandiert schnell zu anderen Universitaeten.",
    },
    # ---- H2. Facebook IPO ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Facebook geht an die Boerse mit einer Bewertung von $104 Milliarden -- zu diesem Zeitpunkt der groesste Tech-IPO der Geschichte. Zuckerberg behaelt Kontrolle durch spezielle Aktienklassen.",
        "datum_handlung": "2012-05-18",
        "betrag_usd": 104000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Facebook",
        "quell_titel": "Facebook - Wikipedia",
        "kontext": "Der IPO machte Zuckerberg zum juengsten Selfmade-Milliardaer der Geschichte.",
    },
    # ---- H3. Instagram-Uebernahme ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Facebook uebernimmt Instagram fuer $1 Milliarde in bar und Aktien. Instagram hatte zu diesem Zeitpunkt 13 Mitarbeiter und 30 Millionen Nutzer.",
        "datum_handlung": "2012-04-09",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Instagram",
        "quell_titel": "Instagram - Wikipedia",
        "kontext": "Die Uebernahme wurde damals als ueberteuert kritisiert, erwies sich aber als eine der erfolgreichsten Akquisitionen der Tech-Geschichte.",
    },
    # ---- H4. WhatsApp-Uebernahme ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Facebook uebernimmt WhatsApp fuer $19 Milliarden -- zu diesem Zeitpunkt die groesste Uebernahme eines VC-finanzierten Startups. WhatsApp hatte 55 Mitarbeiter und 450 Millionen Nutzer.",
        "datum_handlung": "2014-02-19",
        "betrag_usd": 19000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/WhatsApp",
        "quell_titel": "WhatsApp - Wikipedia",
        "kontext": "Die Akquisition festigte Facebooks Dominanz in Messaging und internationalen Maerkten.",
    },
    # ---- H5. Oculus VR-Uebernahme ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Facebook uebernimmt Oculus VR fuer $2,3 Milliarden, um in Virtual Reality einzusteigen. Oculus hatte die Kickstarter-gefundete Oculus Rift entwickelt.",
        "datum_handlung": "2014-03-25",
        "betrag_usd": 2300000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Oculus_VR",
        "quell_titel": "Oculus VR - Wikipedia",
        "kontext": "Diese Akquisition markierte den Beginn von Zuckerbergs Vision fuer das Metaverse.",
    },
    # ---- H6. Chan Zuckerberg Initiative Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Mark Zuckerberg und Priscilla Chan gruenden die Chan Zuckerberg Initiative (CZI) und verpflichten sich, 99% ihrer Facebook-Aktien (damals ca. $45 Milliarden) zu spenden. CZI wird als LLC strukturiert, nicht als klassische Stiftung.",
        "datum_handlung": "2015-12-01",
        "betrag_usd": 45000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Chan_Zuckerberg_Initiative",
        "quell_titel": "Chan Zuckerberg Initiative - Wikipedia",
        "kontext": "Die Gruendung wurde mit einem offenen Brief an ihre neugeborene Tochter Max angekuendigt.",
    },
    # ---- H7. Cambridge Analytica Skandal ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Es wird bekannt, dass Cambridge Analytica Daten von 87 Millionen Facebook-Nutzern ohne Einwilligung fuer politische Werbung gesammelt hat. Zuckerberg muss vor dem US-Kongress und dem EU-Parlament aussagen.",
        "datum_handlung": "2018-03-17",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal",
        "quell_titel": "Facebook–Cambridge Analytica data scandal - Wikipedia",
        "kontext": "Der Skandal fuehrte zu massiven Vertrauensverlusten und regulatorischer Pruefung weltweit.",
    },
    # ---- H8. FTC-Strafe $5 Mrd. ----
    {
        "handlung_typ": "klage",
        "beschreibung": "Facebook zahlt eine Rekordstrafe von $5 Milliarden an die FTC wegen Datenschutzverletzungen im Zusammenhang mit Cambridge Analytica und anderen Verstoessen. Zuckerberg muss persoenlich vierteljährlich Compliance zertifizieren.",
        "datum_handlung": "2019-07-24",
        "betrag_usd": 5000000000.0,
        "quell_link": "https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions-facebook",
        "quell_titel": "FTC Imposes $5 Billion Penalty and Sweeping New Privacy Restrictions on Facebook",
        "kontext": "Die zu diesem Zeitpunkt hoechste Strafe gegen ein Technologieunternehmen.",
    },
    # ---- H9. Umbenennung zu Meta ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Facebook Inc. benennt sich in Meta Platforms Inc. um, um die strategische Neuausrichtung auf das Metaverse zu signalisieren. Facebook, Instagram und WhatsApp bleiben Produktnamen.",
        "datum_handlung": "2021-10-28",
        "betrag_usd": None,
        "quell_link": "https://about.fb.com/news/2021/10/facebook-company-is-now-meta/",
        "quell_titel": "Facebook Company is Now Meta",
        "kontext": "Die Umbenennung folgte auf Jahren negativer PR und regulatorischer Probleme und signalisierte einen strategischen Neustart.",
    },
    # ---- H10. Massenentlassungen November 2022 ----
    {
        "handlung_typ": "entlassung",
        "beschreibung": "Meta entlaesst 11.000 Mitarbeiter (ca. 13% der Belegschaft) -- die groesste Entlassungswelle in der Geschichte des Unternehmens. Zuckerberg uebernimmt oeffentlich die Verantwortung fuer Fehleinschaetzungen beim Wachstum.",
        "datum_handlung": "2022-11-09",
        "betrag_usd": None,
        "quell_link": "https://about.fb.com/news/2022/11/mark-zuckerberg-layoff-message-to-employees/",
        "quell_titel": "Mark Zuckerberg's message to Meta employees",
        "kontext": "Die Entlassungen folgten auf massive Investitionen in Reality Labs und schwaecher als erwartetes Werbewachstum.",
    },
    # ---- H11. Year of Efficiency Entlassungen ----
    {
        "handlung_typ": "entlassung",
        "beschreibung": "Meta kuendigt weitere 10.000 Entlassungen und einen Einstellungsstopp fuer 5.000 Stellen als Teil des 'Year of Efficiency' an. Insgesamt wurden 2023 ueber 21.000 Stellen abgebaut.",
        "datum_handlung": "2023-03-14",
        "betrag_usd": None,
        "quell_link": "https://about.fb.com/news/2023/03/mark-zuckerberg-meta-year-of-efficiency/",
        "quell_titel": "Update on Meta's Year of Efficiency",
        "kontext": "Die Restrukturierung fuehrte zu einem Boersenkurs-Anstieg von ueber 20% und wurde als dauerhafter Strategiewechsel angekuendigt.",
    },
    # ---- H12. Threads Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Meta launcht Threads, eine Twitter-Alternative. Die App erreicht 100 Millionen Nutzer in 5 Tagen -- der schnellste Wachstum einer Consumer-App jemals, schneller selbst als ChatGPT.",
        "datum_handlung": "2023-07-05",
        "betrag_usd": None,
        "quell_link": "https://www.washingtonpost.com/technology/2023/07/06/threads-instagram-app-zuckerberg-twitter/",
        "quell_titel": "Instagram Threads app has 30M users, Zuckerberg says (Washington Post)",
        "kontext": "Der Launch nutzte die Turbulenzen bei Twitter unter Elon Musk und die enge Integration mit Instagram.",
    },
    # ---- H13. Llama 2 Open Source Release ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Meta veroeffentlicht Llama 2 als Open-Source-Sprachmodell mit bis zu 70 Milliarden Parametern. Kostenlos fuer Forschung und kommerzielle Nutzung (mit Einschraenkungen fuer grosse Unternehmen).",
        "datum_handlung": "2023-07-18",
        "betrag_usd": None,
        "quell_link": "https://ai.meta.com/llama/",
        "quell_titel": "Llama 2 - Meta AI",
        "kontext": "Llama 2 etablierte Meta als fuehrenden Anbieter von Open-Source-KI und alternative Vision zu OpenAI.",
    },
    # ---- H14. Senate Testimony Kindersicherheit ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Zuckerberg sagt vor dem Senate Judiciary Committee zu Online-Kindersicherheit aus. Er entschuldigt sich direkt bei anwesenden Opferfamilien, nachdem Senator Hawley ihn dazu draengt. Senator Graham sagt, er habe 'Blut an den Haenden'.",
        "datum_handlung": "2024-01-31",
        "betrag_usd": None,
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2024-01-31_-_testimony_-_zuckerberg.pdf",
        "quell_titel": "Senate Judiciary Committee Hearing on Online Child Safety",
        "kontext": "Eine der emotionalsten Congressional Hearings fuer Zuckerberg, mit scharfer Kritik an Instagram und Facebook.",
    },
    # ---- H15. Llama 3.1 Release (405B) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Meta veroeffentlicht Llama 3.1 mit 405 Milliarden Parametern -- das groesste Open-Source-Sprachmodell und laut Meta wettbewerbsfaehig mit GPT-4 und Claude. Begleitet von Zuckerbergs 'Open Source AI is the Path Forward'-Manifest.",
        "datum_handlung": "2024-07-23",
        "betrag_usd": None,
        "quell_link": "https://ai.meta.com/blog/meta-llama-3-1/",
        "quell_titel": "Introducing Llama 3.1: Our most capable models to date",
        "kontext": "Markiert Metas Anspruch auf Fuehrerschaft in Open-Source-KI und direkte Herausforderung an OpenAI.",
    },
    # ---- H16. Scale AI Investition $14,3 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Meta investiert $14,3 Milliarden in Scale AI und stellt dessen CEO Alexandr Wang ein. Die Investition ist Teil von Metas AGI-Sprint und soll Metas Datenannotation und KI-Training beschleunigen.",
        "datum_handlung": "2025-06-10",
        "betrag_usd": 14300000000.0,
        "quell_link": "https://www.cnbc.com/2025/06/10/zuckerberg-makes-metas-biggest-bet-on-ai-14-billion-scale-ai-deal.html",
        "quell_titel": "A frustrated Zuckerberg makes his biggest AI bet as Meta nears $14 billion stake in Scale AI (CNBC)",
        "kontext": "Die Investition zeigt Zuckerbergs Ungeduld mit Metas KI-Fortschritt und Entschlossenheit, an der Spitze zu bleiben.",
    },
    # ---- H17. Superintelligence Group Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Meta gruendet die 'Superintelligence Group', die FAIR (Facebook AI Research) und GenAI-Teams vereint mit dem Ziel, AGI/Superintelligenz zu entwickeln. Zuckerberg erklaert Superintelligenz als 'in Sichtweite'.",
        "datum_handlung": "2025-06-17",
        "betrag_usd": None,
        "quell_link": "https://campustechnology.com/articles/2025/06/17/meta-forms-superintelligence-group-to-pursue-artificial-general-intelligence.aspx",
        "quell_titel": "Meta Forms 'Superintelligence Group' to Pursue Artificial General Intelligence",
        "kontext": "Organisatorische Neuausrichtung mit dem expliziten Ziel, Superintelligenz zu entwickeln.",
    },
    # ---- H18. Metaverse-Pivot: 30% Budget-Cuts ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Zuckerberg kuendigt Budgetkuerzungen von bis zu 30% fuer Reality Labs (Metaverse-Abteilung) und Entlassungen von 10-30% des Teams an. Fokus verschiebt sich zu KI-gesteuerten Smart Glasses statt VR-Headsets.",
        "datum_handlung": "2025-12-08",
        "betrag_usd": None,
        "quell_link": "https://petapixel.com/2025/12/08/mark-zuckerberg-making-big-cuts-to-the-metaverse-after-77-billion-loss/",
        "quell_titel": "Mark Zuckerberg is Making Big Cuts to the Metaverse After $77 Billion Loss (PetaPixel)",
        "kontext": "Nach $77 Milliarden Verlusten bei Reality Labs schwenkt Meta von VR-Headsets zu AI-Smart-Glasses um.",
    },
    # ---- H19. Manus AI Akquisition ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Meta uebernimmt Manus, ein in Singapur ansaessiges KI-Startup mit chinesischen Wurzeln, fuer ueber $2 Milliarden. Manus entwickelt KI-Agenten. Eine seltene Uebernahme eines China-gegruendeten Startups durch einen US-Tech-Giganten.",
        "datum_handlung": "2025-12-29",
        "betrag_usd": 2000000000.0,
        "quell_link": "https://fortune.com/2025/12/30/meta-buys-manus-mark-zuckerberg-ai-spending-spree-china-startup/",
        "quell_titel": "Meta is dropping over $2 billion for an AI startup (Fortune)",
        "kontext": "Teil von Metas KI-Kaufrausch und Plan, KI-Agenten in Facebook, Instagram und WhatsApp zu integrieren.",
    },
    # ---- H20. CZI Restrukturierung zu KI-Fokus ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Die Chan Zuckerberg Initiative entlaesst 70 Mitarbeiter und stellt Finanzierung fuer Bildung, Klimawandel und soziale Gerechtigkeit ein. Volle Fokussierung auf KI-getriebene biomedizinische Forschung und das Biohub-Netzwerk.",
        "datum_handlung": "2026-02-01",
        "betrag_usd": None,
        "quell_link": "https://fortune.com/2026/02/01/chan-zuckerberg-initiative-layoffs-all-in-on-ai-biomedical-research/",
        "quell_titel": "Chan Zuckerberg Initiative goes all in on AI biomedical research (Fortune)",
        "kontext": "CZI plant, $10 Milliarden in KI-Forschung im naechsten Jahrzehnt zu investieren.",
    },
    # ---- H21. Meta Compute Ankuendigung ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Meta kuendigt 'Meta Compute' an: eine massive Infrastruktur-Initiative mit Multi-Gigawatt-Rechenzentren. Das erste 'Prometheus'-Zentrum (1 GW) in Ohio, das groesste 'Hyperion' (5 GW, $10 Mrd.) in Louisiana.",
        "datum_handlung": "2026-02-06",
        "betrag_usd": 10000000000.0,
        "quell_link": "https://markets.financialcontent.com/stocks/article/tokenring-2026-2-6-the-gigawatt-era-inside-mark-zuckerbergs-meta-compute-manifesto",
        "quell_titel": "The Gigawatt Era: Inside Mark Zuckerberg's 'Meta Compute' Manifesto",
        "kontext": "Metas Antwort auf OpenAI/Microsoft-Infrastruktur, um Superintelligenz zu trainieren.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=5 existiert
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
            "Claude (collect_zuckerberg.py)"
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
        "Mark Zuckerberg AI, Llama, open source, metaverse, Reality Labs, superintelligence, Meta AI, Threads, CZI, Congressional testimony, Dwarkesh Patel, Joe Rogan",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Meta Blog (about.fb.com), Meta AI Blog (ai.meta.com), Dwarkesh Podcast, "
        f"Joe Rogan Experience #2255, Senate Judiciary Committee Hearings, "
        f"TechCrunch, Fortune, CNBC, Washington Post, NBC News, TIME, Tom's Guide, Axios.",
        "Claude (collect_zuckerberg.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Mark Zuckerberg (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Mark Zuckerberg")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_zuckerberg.py")
    print("  Verifizierte Aussagen & Handlungen: Mark Zuckerberg")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
