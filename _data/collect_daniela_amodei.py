#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Daniela Amodei (Person ID 17)
Mitgründerin und Präsidentin von Anthropic (Claude)
Fokus: KI-Sicherheit, verantwortungsvolle KI-Entwicklung, Business-Strategie
"""

import sqlite3
from datetime import datetime

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 17

def get_quellen_typ_id(conn, typ_name):
    """Ermittelt die quellen_typ_id basierend auf dem Typ-Namen"""
    mapping = {
        "Interview": 1,  # Video-Interview
        "Vortrag": 3,     # Keynote/Vortrag
        "Stellungnahme": 10,  # Offizielle Stellungnahme
        "Firmendokumentation": 6  # Blog-Artikel (am nächsten)
    }
    return mapping.get(typ_name, 1)  # Default: Video-Interview

def insert_aussagen(conn):
    """Fügt Aussagen von Daniela Amodei in die Datenbank ein"""
    aussagen = [
        {
            "aussage_text": "The number of jobs that AI could do without help from people is vanishingly small. When hiring at Anthropic, I look for people who are great communicators, have excellent emotional intelligence and people skills, and are kind, compassionate, and curious. The things that make us human will become much more important instead of much less important.",
            "datum_aussage": "2026-02-07",
            "quelle_typ": "Interview",
            "kontext": "ABC News Interview über die Bedeutung menschlicher Fähigkeiten im KI-Zeitalter und Einstellungskriterien bei Anthropic",
            "modus": "muendlich"
        },
        {
            "aussage_text": "The exponential continues until it doesn't. We have made do more with less a governing principle for Anthropic's entire strategy. The next phase won't be won by the biggest pre-training runs alone, but by who can deliver the most capability per dollar of compute.",
            "datum_aussage": "2026-01-03",
            "quelle_typ": "Interview",
            "kontext": "CNBC Interview über Anthropics Compute-Effizienz-Strategie und Zweifel an unbegrenztem exponentiellem Wachstum",
            "modus": "muendlich"
        },
        {
            "aussage_text": "Trust is what unlocks deployment at scale. In regulated industries, the question isn't just which model is smartest—it's which model you can actually rely on, and whether the company behind it will be a responsible long-term partner.",
            "datum_aussage": "2025-12-04",
            "quelle_typ": "Interview",
            "kontext": "Fast Company Interview über Anthropics Fokus auf Vertrauen und Enterprise-Kunden in regulierten Branchen",
            "modus": "muendlich"
        },
        {
            "aussage_text": "There's a strong focus at Anthropic on ensuring that AI tools are made available throughout the world. We're thinking very critically about how access to this technology is really available to people.",
            "datum_aussage": "2025-11-08",
            "quelle_typ": "Interview",
            "kontext": "Aussage über Anthropics Bemühungen um globalen Zugang zu KI-Technologie",
            "modus": "muendlich"
        },
        {
            "aussage_text": "No one says, 'We want a less safe product.' We're setting what you can almost think of as minimum safety standards just by what we're putting into the economy.",
            "datum_aussage": "2025-10-21",
            "quelle_typ": "Interview",
            "kontext": "WIRED Big Interview Event - Verteidigung von Anthropics Sicherheitsansatz gegenüber Trump-Administration",
            "modus": "muendlich"
        },
        {
            "aussage_text": "No model available today is 100% safe, but our goal for Claude is helping to improve on each of those three criteria: helpful, honest, and harmless.",
            "datum_aussage": "2024-02-23",
            "quelle_typ": "Vortrag",
            "kontext": "Stanford eCorner Vortrag über Constitutional AI und Anthropics Sicherheitsziele",
            "modus": "muendlich"
        },
        {
            "aussage_text": "There's something about the mission and the values and this desire to be honest about both the good and the bad. We were very vocal from day one that we felt there was this incredible potential for AI. We really want to be able to have the entire world realize the potential, the positive benefits, and the upside that can come from AI, and in order to do that, we have to get the tough things right.",
            "datum_aussage": "2023-09-15",
            "quelle_typ": "Interview",
            "kontext": "Stripe Interview über Anthropics Mission und Balance zwischen KI-Potenzial und Sicherheit",
            "modus": "muendlich"
        },
        {
            "aussage_text": "We hope people use Claude as a partner or collaborator that helps humans do what they want to do and live the lives they want to live, with humans at the center of their process. The name Anthropic means relating to humans, and keeping humans at the center has been important for the company.",
            "datum_aussage": "2023-08-20",
            "quelle_typ": "Interview",
            "kontext": "Stripe Interview über die Namensgebung von Anthropic und die menschenzentrierte Philosophie",
            "modus": "muendlich"
        },
        {
            "aussage_text": "Humans plus AI together actually create more meaningful work, more challenging work, more interesting work, and high-productivity jobs. Studying the humanities is going to be more important than ever, as understanding ourselves, understanding history, and understanding what makes us tick will always be really important.",
            "datum_aussage": "2026-02-07",
            "quelle_typ": "Interview",
            "kontext": "Fortune Interview über die Bedeutung von Geisteswissenschaften im KI-Zeitalter",
            "modus": "muendlich"
        },
        {
            "aussage_text": "We truly believe that AI needed to be defined in accordance with humanity—acting as a copilot, rather than something that could one day supersede society. Trust and safety is something the market wants, and it's both the correct thing to do from a moral perspective and good for business.",
            "datum_aussage": "2023-10-15",
            "quelle_typ": "Interview",
            "kontext": "Aussage über Anthropics Philosophie: KI als Copilot statt Ersatz für die Menschheit",
            "modus": "schriftlich"
        },
        {
            "aussage_text": "We aim to build transformative general AI systems that are safe, reliable, steerable, ethical. We want to build generative AI tools and systems and products that people could use while feeling really, really confident that what we were putting on the market was trustworthy, reliable, and safe.",
            "datum_aussage": "2022-04-15",
            "quelle_typ": "Firmendokumentation",
            "kontext": "Beschreibung von Anthropics Gründungsmission nach der Series B Finanzierungsrunde",
            "modus": "schriftlich"
        },
        {
            "aussage_text": "Dario and I shared a conviction that AI development required a fundamentally different approach—one that placed constitutional safety principles at the foundation rather than bolting them on afterward.",
            "datum_aussage": "2021-05-31",
            "quelle_typ": "Interview",
            "kontext": "Rückblick auf die Gründung von Anthropic und die Unterschiede zum OpenAI-Ansatz",
            "modus": "schriftlich"
        },
        {
            "aussage_text": "Anthropic is projected to bring in $10 billion in 2025 revenue, with profitability expected in 2028—a shorter path to profit than its rivals. We are placing our biggest strategic bets in regulated industries, positioning Claude as core enterprise infrastructure.",
            "datum_aussage": "2025-12-02",
            "quelle_typ": "Interview",
            "kontext": "Fortune Artikel über Anthropics Geschäftsstrategie und Finanzen",
            "modus": "schriftlich"
        },
        {
            "aussage_text": "Anthropic supports a unified federal policy approach to AI regulation. We did support California legislation that aims to set safety standards for leading AI firms. The bill sets a profit threshold that keeps it from stifling startups.",
            "datum_aussage": "2024-08-20",
            "quelle_typ": "Stellungnahme",
            "kontext": "Position zu KI-Regulierung auf Bundes- und Bundesstaatsebene (Kalifornien)",
            "modus": "schriftlich"
        }
    ]

    cursor = conn.cursor()
    for aussage in aussagen:
        quellen_typ_id = get_quellen_typ_id(conn, aussage["quelle_typ"])
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, datum_aussage, quellen_typ_id, kontext, modus, einschluss)
            VALUES (?, ?, ?, ?, ?, ?, 1)
        """, (
            PERSON_ID,
            aussage["aussage_text"],
            aussage["datum_aussage"],
            quellen_typ_id,
            aussage["kontext"],
            aussage["modus"]
        ))

    print(f"[OK] {len(aussagen)} Aussagen eingefuegt")

def insert_handlungen(conn):
    """Fügt Handlungen von Daniela Amodei in die Datenbank ein"""
    handlungen = [
        {
            "handlung_typ": "gruendung",
            "beschreibung": "Mitgründung von Anthropic zusammen mit Dario Amodei und 5 weiteren ehemaligen OpenAI-Mitarbeitern. Verlassen von OpenAI wegen unterschiedlicher Auffassungen über Richtung und Sicherheitsprioritäten.",
            "datum_handlung": "2021-01-15",
            "betrag_usd": None
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Anthropic Series A Finanzierungsrunde unter Führung von Jaan Tallinn zur Unterstützung der KI-Sicherheitsforschung. Daniela Amodei als Co-Founder und President.",
            "datum_handlung": "2021-05-31",
            "betrag_usd": 124000000
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Anthropic Series B Finanzierungsrunde unter Führung von Sam Bankman-Fried zur Expansion von Rechenressourcen und Team-Wachstum.",
            "datum_handlung": "2022-04-15",
            "betrag_usd": 580000000
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Anthropic Series C Finanzierungsrunde unter Führung von Spark Capital mit Beteiligung von Google, Salesforce Ventures und anderen.",
            "datum_handlung": "2023-05-20",
            "betrag_usd": 450000000
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Amazon kündigt Partnerschaft mit Anthropic an und investiert initial 1,25 Milliarden USD mit Planung von insgesamt 4 Milliarden USD. Amazon wird primärer Cloud-Provider.",
            "datum_handlung": "2023-09-25",
            "betrag_usd": 1250000000
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Google investiert 500 Millionen USD in Anthropic und verpflichtet sich zu weiteren 1,5 Milliarden USD über Zeit.",
            "datum_handlung": "2023-10-15",
            "betrag_usd": 500000000
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Öffentlicher Launch von Claude 2 nach früheren eingeschränkten Versionen (Claude, Claude Instant). Erster breiter öffentlicher Zugang zu Anthropics LLM.",
            "datum_handlung": "2023-07-11",
            "betrag_usd": None
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Amazon komplettiert zusätzliche 2,75 Milliarden USD Investition in Anthropic (Teil der ursprünglich angekündigten 4 Milliarden USD).",
            "datum_handlung": "2024-03-27",
            "betrag_usd": 2750000000
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Launch der Claude 3 Familie: Claude 3 Opus, Claude 3 Sonnet und Claude 3 Haiku. Signifikanter Leistungssprung in Benchmarks.",
            "datum_handlung": "2024-03-04",
            "betrag_usd": None
        },
        {
            "handlung_typ": "lobbying",
            "beschreibung": "Anthropic unterstützt öffentlich kalifornisches KI-Sicherheitsgesetz (SB 1047) trotz Widerstands anderer Tech-Firmen. Position für föderale KI-Regulierung.",
            "datum_handlung": "2024-08-20",
            "betrag_usd": None
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Anthropic Series E Finanzierungsrunde unter Führung von Lightspeed Venture Partners. Post-Money Bewertung: 61,5 Milliarden USD.",
            "datum_handlung": "2025-03-15",
            "betrag_usd": 3500000000
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Google investiert weitere 1 Milliarde USD in Anthropic zusätzlich zu früheren Commitments.",
            "datum_handlung": "2025-03-20",
            "betrag_usd": 1000000000
        },
        {
            "handlung_typ": "partnerschaft",
            "beschreibung": "Launch von Claude for Education mit Partnerschaften an Northeastern University, London School of Economics und Champlain College.",
            "datum_handlung": "2025-04-02",
            "betrag_usd": None
        },
        {
            "handlung_typ": "produktlaunch",
            "beschreibung": "Ankündigung von Claude 4 mit Claude Opus 4 und Claude Sonnet 4. Verbesserte Coding-Fähigkeiten und neue Features.",
            "datum_handlung": "2025-05-15",
            "betrag_usd": None
        },
        {
            "handlung_typ": "investition",
            "beschreibung": "Anthropic Series F Finanzierungsrunde co-geführt von Iconiq Capital, Fidelity und Lightspeed. Post-Money Bewertung: 183 Milliarden USD.",
            "datum_handlung": "2025-09-10",
            "betrag_usd": 13000000000
        }
    ]

    cursor = conn.cursor()
    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, betrag_usd)
            VALUES (?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            handlung["handlung_typ"],
            handlung["beschreibung"],
            handlung["datum_handlung"],
            handlung["betrag_usd"]
        ))

    print(f"[OK] {len(handlungen)} Handlungen eingefügt")

def main():
    """Hauptfunktion zum Einfügen aller Daten"""
    print(f"\n{'='*70}")
    print(f"Datensammlung: Daniela Amodei (Person ID {PERSON_ID})")
    print(f"{'='*70}\n")

    try:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect(DB_PATH)
        print(f"[OK] Verbindung zur Datenbank hergestellt: {DB_PATH}\n")

        # Aussagen einfügen
        print("Füge Aussagen ein...")
        insert_aussagen(conn)

        # Handlungen einfügen
        print("\nFüge Handlungen ein...")
        insert_handlungen(conn)

        # Änderungen speichern
        conn.commit()
        print("\n[OK] Alle Änderungen wurden gespeichert")

        # Statistik ausgeben
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
        anzahl_aussagen = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
        anzahl_handlungen = cursor.fetchone()[0]

        print(f"\n{'='*70}")
        print(f"ZUSAMMENFASSUNG")
        print(f"{'='*70}")
        print(f"Gesamtanzahl Aussagen für Daniela Amodei: {anzahl_aussagen}")
        print(f"Gesamtanzahl Handlungen für Daniela Amodei: {anzahl_handlungen}")
        print(f"{'='*70}\n")

    except sqlite3.Error as e:
        print(f"\n[FEHLER] Datenbankfehler: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            print("[OK] Datenbankverbindung geschlossen")

if __name__ == "__main__":
    main()
