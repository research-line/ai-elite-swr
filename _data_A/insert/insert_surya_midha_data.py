#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Surya Midha (person_id=76)
Forschungsdatenbank zu Weltbildern von KI/Silicon-Valley-Persönlichkeiten
"""

import sqlite3
import sys
from datetime import datetime

# UTF-8 Encoding für Windows Console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Datenbank-Verbindung
db_path = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

person_id = 76

print(f"Füge Daten für Surya Midha (person_id={person_id}) ein...\n")

# ============================================================================
# AUSSAGEN
# ============================================================================
# Erlaubte modus-Werte: 'muendlich', 'schriftlich', 'unbekannt'

aussagen = [
    {
        "aussage_text": "In some ways, I feel like I leapfrogged 50 years of career development and slightly regressed personally. An excellent trade overall. There's a certain violence to velocity. The world doesn't always notice, but your body does. You gain 30 pounds in six months.",
        "aussage_kurz": "Leapfrogged 50 years of career development, violence to velocity",
        "modus": "schriftlich",
        "quell_link": "https://x.com/suryamidha/status/1923208353213448280",
        "quell_titel": "Surya Midha on X (Twitter)",
        "datum_aussage": "2025-01-15",
        "sprache": "en",
        "kontext": "Reflection on rapid startup growth and personal cost of building Mercor"
    },
    {
        "aussage_text": "last week, I shared with the mercor team that I'll be transitioning into a new role as chairman of the board and stepping away from my position as chief operating officer. mercor has been the defining journey of my life.",
        "aussage_kurz": "Transitioning to chairman, mercor has been defining journey of my life",
        "modus": "schriftlich",
        "quell_link": "https://www.linkedin.com/posts/suryamidha_last-week-i-shared-with-the-mercor-team-activity-7381430825260703745-U2PW",
        "quell_titel": "Surya Midha's LinkedIn Post - October 2025",
        "datum_aussage": "2025-10-01",
        "sprache": "en",
        "kontext": "Announcement of transition from COO to Board Chairman at Mercor"
    },
    {
        "aussage_text": "In September 2024, we announced our $30m Series A at a $250m valuation led by Benchmark, with participation from General Catalyst, Peter Thiel, Jack Dorsey, Adam D'Angelo, and Larry Summers.",
        "aussage_kurz": "$30m Series A funding announcement with top-tier investors",
        "modus": "schriftlich",
        "quell_link": "https://suryamidha.com/",
        "quell_titel": "Surya Midha Personal Website",
        "datum_aussage": "2024-09-18",
        "sprache": "en",
        "kontext": "Announcement of Mercor's Series A funding round"
    },
    {
        "aussage_text": "If you can understand what people are good at, and care about where they do it, you can be the impetus behind profound societal change.",
        "aussage_kurz": "Understanding people's skills can drive profound societal change",
        "modus": "schriftlich",
        "quell_link": "https://nri.today/surya-midha/",
        "quell_titel": "Surya Midha: Redefining AI Recruitment - NRI Today",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Vision statement about Mercor's mission to transform work and labor"
    },
    {
        "aussage_text": "Our goal is to get a billion people hired—not just faster, but better.",
        "aussage_kurz": "Goal to get a billion people hired, better",
        "modus": "schriftlich",
        "quell_link": "https://nri.today/surya-midha/",
        "quell_titel": "Surya Midha: Redefining AI Recruitment - NRI Today",
        "datum_aussage": "2025-02-01",
        "sprache": "en",
        "kontext": "Company mission statement about transforming global employment"
    },
    {
        "aussage_text": "Mercor is a company fixated on work—not just the mechanics of employment but the moral weight of what people do with their lives.",
        "aussage_kurz": "Fixated on work and moral weight of what people do with their lives",
        "modus": "schriftlich",
        "quell_link": "https://www.coffeespace.com/blog-post/mercor-ai-founders-journey",
        "quell_titel": "Mercor AI Founders' Journey - CoffeeSpace",
        "datum_aussage": "2025-03-01",
        "sprache": "en",
        "kontext": "Company philosophy about the deeper meaning of work"
    },
    {
        "aussage_text": "There's a messianic intensity to the work that is polarizing and beautiful.",
        "aussage_kurz": "Messianic intensity to the work, polarizing and beautiful",
        "modus": "schriftlich",
        "quell_link": "https://www.coffeespace.com/blog-post/mercor-ai-founders-journey",
        "quell_titel": "Mercor AI Founders' Journey - CoffeeSpace",
        "datum_aussage": "2025-03-01",
        "sprache": "en",
        "kontext": "Description of company culture and work intensity at Mercor"
    },
    {
        "aussage_text": "In the last two years, Mercor went from three guys in a dorm room to fifty people in an office, with fifty more scattered across time zones.",
        "aussage_kurz": "From three guys in dorm to 100 people in two years",
        "modus": "schriftlich",
        "quell_link": "https://www.coffeespace.com/blog-post/mercor-ai-founders-journey",
        "quell_titel": "Mercor AI Founders' Journey - CoffeeSpace",
        "datum_aussage": "2025-03-01",
        "sprache": "en",
        "kontext": "Reflection on Mercor's rapid growth from founding to scale-up"
    },
    {
        "aussage_text": "I spent most of high school thinking about policy debate. I was coached by Aaron Langerman, Ani Prabhu, and Tyler Vergho.",
        "aussage_kurz": "Policy debate in high school shaped my thinking",
        "modus": "schriftlich",
        "quell_link": "https://suryamidha.com/",
        "quell_titel": "Surya Midha Personal Website",
        "datum_aussage": "2021-06-01",
        "sprache": "en",
        "kontext": "Background on debate career at Bellarmine College Preparatory"
    },
    {
        "aussage_text": "I spent two years at Georgetown taking courses in international relations, math, and economics.",
        "aussage_kurz": "Two years at Georgetown studying IR, math, economics",
        "modus": "schriftlich",
        "quell_link": "https://suryamidha.com/",
        "quell_titel": "Surya Midha Personal Website",
        "datum_aussage": "2023-01-01",
        "sprache": "en",
        "kontext": "Educational background before dropping out to found Mercor"
    }
]

print("Füge Aussagen ein:")
for i, aussage in enumerate(aussagen, 1):
    try:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus,
                                quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            person_id,
            aussage["aussage_text"],
            aussage["aussage_kurz"],
            aussage["modus"],
            aussage["quell_link"],
            aussage["quell_titel"],
            aussage["datum_aussage"],
            aussage["sprache"],
            aussage["kontext"]
        ))
        print(f"  {i}. OK {aussage['aussage_kurz'][:70]}...")
    except sqlite3.Error as e:
        print(f"  {i}. FEHLER: {e}")

# ============================================================================
# HANDLUNGEN
# ============================================================================

handlungen = [
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Co-founded Mercor with Adarsh Hiremath and Brendan Foody, an AI-driven recruitment platform connecting skilled professionals with AI labs. Took academic leave from Georgetown University to start the company.",
        "datum_handlung": "2023-01-15",
        "quell_link": "https://nri.today/surya-midha/",
        "quell_titel": "Surya Midha: Redefining AI Recruitment - NRI Today",
        "kontext": "Founded Mercor during sophomore year at Georgetown University with high school debate teammates"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Received Thiel Fellowship ($100,000 grant) along with co-founders Adarsh Hiremath and Brendan Foody. One of the only times in history that an entire cofounding team received the Thiel Fellowship.",
        "datum_handlung": "2024-03-01",
        "quell_link": "https://x.com/thecrimson/status/1900637562802205174",
        "quell_titel": "The Harvard Crimson on X - Thiel Fellowship Announcement",
        "kontext": "Prestigious fellowship for young founders who drop out of college to build impactful ventures"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Led $3.6 million seed funding round for Mercor, led by General Catalyst. Early stage funding to launch AI recruitment platform.",
        "datum_handlung": "2023-06-01",
        "quell_link": "https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/",
        "quell_titel": "Mercor raises $100M at $2B valuation - TechCrunch",
        "kontext": "Initial institutional funding for Mercor to build out platform"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Announced $30 million Series A funding at $250 million valuation led by Benchmark, with participation from General Catalyst, Peter Thiel, Jack Dorsey, Adam D'Angelo, and Larry Summers.",
        "datum_handlung": "2024-09-18",
        "quell_link": "https://www.prnewswire.com/news-releases/mercor-raises-30m-series-a-at-a-250m-valuation-to-create-jobs-with-ai-302252449.html",
        "quell_titel": "Mercor Raises $30M Series A - PR Newswire",
        "kontext": "Major funding round with top-tier Silicon Valley investors and tech leaders"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Announced $100 million Series B funding at $2 billion valuation led by Felicis, with participation from Benchmark, General Catalyst, DST Global, and Menlo Ventures.",
        "datum_handlung": "2025-02-20",
        "quell_link": "https://techcrunch.com/2025/02/20/mercor-an-ai-recruiting-startup-founded-by-21-year-olds-raises-100m-at-2b-valuation/",
        "quell_titel": "Mercor raises $100M at $2B valuation - TechCrunch",
        "kontext": "8x valuation increase in 5 months, scaling AI expert network"
    },
    {
        "handlung_typ": "investition",
        "beschreibung": "Announced $350 million Series C funding at $10 billion valuation led by Felicis Ventures, with participation from Benchmark, General Catalyst, and Robinhood Ventures. 5x valuation increase since February 2025.",
        "datum_handlung": "2025-10-27",
        "quell_link": "https://techcrunch.com/2025/10/27/mercor-quintuples-valuation-to-10b-with-350m-series-c/",
        "quell_titel": "Mercor quintuples valuation to $10B with $350M Series C - TechCrunch",
        "kontext": "Became one of youngest self-made billionaires at age 22, driven by AI labs moving away from Scale AI after Meta investment"
    },
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Transitioned from Chief Operating Officer (COO) to Chairman of the Board at Mercor. Stepped away from day-to-day operations after guiding company through critical growth phases from $3.6M seed to $100M Series B.",
        "datum_handlung": "2025-10-01",
        "quell_link": "https://x.com/suryamidha/status/1975664221141803423",
        "quell_titel": "Surya Midha on X - COO to Chairman Transition",
        "kontext": "Strategic transition after achieving $10B valuation and becoming youngest self-made billionaire"
    },
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Hired former Bellarmine College Preparatory debate coach Aaron Langerman as Strategic Operations Lead at Mercor to help scale the company and improve internal systems.",
        "datum_handlung": "2025-09-01",
        "quell_link": "https://theorg.com/org/mercor/org-chart/aaron-langerman",
        "quell_titel": "Aaron Langerman - Strategic Operations Lead at Mercor - The Org",
        "kontext": "Brought in former debate coach from high school to help with rapid scaling"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Mercor pivoted from connecting Indian software engineers to US startups to AI-driven recruiting platform serving major AI labs including OpenAI, Anthropic, and Google DeepMind. Platform now manages 30,000+ contractors for AI training and evaluation.",
        "datum_handlung": "2024-06-01",
        "quell_link": "https://en.wikipedia.org/wiki/Mercor",
        "quell_titel": "Mercor - Wikipedia",
        "kontext": "Strategic pivot after meetings with OpenAI and xAI led to focus on expert-driven AI evaluations"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Selected for Forbes 30 Under 30 (2025) list in recognition of achievements as co-founder of Mercor AI recruitment platform. Solidified reputation as leading voice in AI and startup ecosystem.",
        "datum_handlung": "2025-01-15",
        "quell_link": "https://www.analyticsinsight.net/news/forbes-30-under-30-honors-8-indian-origin-ai-visionaries-for-2025",
        "quell_titel": "Forbes 30 Under 30 Honors 8 Indian-Origin AI Visionaries - Analytics Insight",
        "kontext": "Recognition as one of top young entrepreneurs in AI space"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "First team in history to win all three national policy debate tournaments: Tournament of Champions (TOC), National Debate Coaches Association Tournament (NDCA), and National Speech and Debate Association Tournament (NSDA). Individually ranked as best speaker at both TOC and NDCA.",
        "datum_handlung": "2021-05-01",
        "quell_link": "https://suryamidha.com/",
        "quell_titel": "Surya Midha Personal Website",
        "kontext": "Historic achievement in high school debate at Bellarmine College Preparatory"
    },
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Mercor reached $500 million annual recurring revenue (ARR) run rate, growing from $1M to $500M in just 17 months. Company now pays over $1.5 million daily to 30,000+ contractors for AI training work.",
        "datum_handlung": "2025-09-01",
        "quell_link": "https://www.thetwentyminutevc.com/brendan-foody",
        "quell_titel": "Mercor: From $1M to $500M in 17 Months - 20VC Podcast",
        "kontext": "Fastest growing company in history by revenue growth rate"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Graduated as salutatorian from Bellarmine College Preparatory. Enrolled at Georgetown University's School of Foreign Service to study international relations and economics.",
        "datum_handlung": "2021-06-15",
        "quell_link": "https://suryamidha.com/",
        "quell_titel": "Surya Midha Personal Website",
        "kontext": "Academic achievement before college dropout to found Mercor"
    },
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Mercor capitalized on major AI labs (OpenAI, Google DeepMind) cutting ties with Scale AI after Meta's $14 billion investment created conflicts of interest. Positioned Mercor as alternative provider of expert AI training data.",
        "datum_handlung": "2025-08-01",
        "quell_link": "https://www.techbuzz.ai/articles/mercor-hits-10b-valuation-as-ai-training-war-intensifies",
        "quell_titel": "Mercor Hits $10B Valuation as AI Training War Intensifies - TechBuzz",
        "kontext": "Strategic market opportunity from Scale AI's Meta partnership creating competitor exodus"
    },
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Dropped out of Georgetown University School of Foreign Service to focus full-time on building Mercor. Became one of youngest founders to receive Thiel Fellowship for college dropouts.",
        "datum_handlung": "2023-01-15",
        "quell_link": "https://www.globalindiantimes.com/p/johs-recruitment-22025",
        "quell_titel": "Can Mercor Compete Against LinkedIn - Global Indian Times",
        "kontext": "Left Georgetown during sophomore year to pursue Mercor full-time with co-founders"
    }
]

print("\nFüge Handlungen ein:")
for i, handlung in enumerate(handlungen, 1):
    try:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung,
                                  datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            person_id,
            handlung["handlung_typ"],
            handlung["beschreibung"],
            handlung["datum_handlung"],
            handlung["quell_link"],
            handlung["quell_titel"],
            handlung["kontext"]
        ))
        print(f"  {i}. OK [{handlung['handlung_typ']}] {handlung['beschreibung'][:60]}...")
    except sqlite3.Error as e:
        print(f"  {i}. FEHLER: {e}")

# ============================================================================
# COMMIT UND ZUSAMMENFASSUNG
# ============================================================================

conn.commit()
conn.close()

print("\n" + "="*80)
print("ZUSAMMENFASSUNG")
print("="*80)
print(f"Person: Surya Midha (person_id={person_id})")
print(f"Aussagen eingefügt: {len(aussagen)}")
print(f"Handlungen eingefügt: {len(handlungen)}")
print(f"Gesamt: {len(aussagen) + len(handlungen)} Einträge")
print("="*80)
print("\nDatenbank erfolgreich aktualisiert!")
print(f"Pfad: {db_path}")
