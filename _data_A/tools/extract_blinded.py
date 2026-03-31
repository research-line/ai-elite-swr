#!/usr/bin/env python3
"""
extract_blinded.py
==================
Extracts statements (aussagen) and actions (handlungen) for a person from the DB,
removes all identifying information (blinding) and
outputs the blinded data corpus as text.

Usage:
    python extract_blinded.py <person_id>
    python extract_blinded.py --top10
    python extract_blinded.py --top10-collective
"""

import sqlite3
import os
import sys
import re
import json

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")

# Last names that are too common/generic -> only replace full name
COMMON_LAST_NAMES = {
    "Page", "Cook", "Brown", "Chen", "Wang", "Li", "Wu", "Dean",
    "Clark", "Jones", "Dixon", "Scott", "Jordan", "Gross", "Ba",
    "Son", "Tan", "Singh", "Guo", "Su", "Ng", "Rao", "Taylor",
    "Russell", "Manning", "Kaiser", "Foody", "Asif"
}

# All 100 persons with full name + last name (if unambiguous)
PERSON_NAMES = {
    # Full names -- always replace
    "Jensen Huang": "[PERSON]", "Sam Altman": "[PERSON]",
    "Elon Musk": "[PERSON]", "Sundar Pichai": "[PERSON]",
    "Mark Zuckerberg": "[PERSON]", "Larry Page": "[PERSON]",
    "Larry Ellison": "[PERSON]", "Sergey Brin": "[PERSON]",
    "Dario Amodei": "[PERSON]", "Jeff Bezos": "[PERSON]",
    "Demis Hassabis": "[PERSON]", "Ilya Sutskever": "[PERSON]",
    "Satya Nadella": "[PERSON]", "Lisa Su": "[PERSON]",
    "Tim Cook": "[PERSON]", "Masayoshi Son": "[PERSON]",
    "Daniela Amodei": "[PERSON]", "Fei-Fei Li": "[PERSON]",
    "Jeff Dean": "[PERSON]", "Yann LeCun": "[PERSON]",
    "Geoffrey Hinton": "[PERSON]", "Andrew Ng": "[PERSON]",
    "Mustafa Suleyman": "[PERSON]", "Marc Andreessen": "[PERSON]",
    "Peter Thiel": "[PERSON]", "Mira Murati": "[PERSON]",
    "Bret Taylor": "[PERSON]", "Greg Brockman": "[PERSON]",
    "Alexandr Wang": "[PERSON]", "Noam Shazeer": "[PERSON]",
    "Reid Hoffman": "[PERSON]", "Vinod Khosla": "[PERSON]",
    "Ashish Vaswani": "[PERSON]", "Michael Truell": "[PERSON]",
    "Aravind Srinivas": "[PERSON]", "David Sacks": "[PERSON]",
    "Sriram Krishnan": "[PERSON]", "Ali Ghodsi": "[PERSON]",
    "Alex Karp": "[PERSON]", "Aidan Gomez": "[PERSON]",
    "Michael Intrator": "[PERSON]", "Scott Wu": "[PERSON]",
    "Palmer Luckey": "[PERSON]", "Jakub Pachocki": "[PERSON]",
    "Mark Chen": "[PERSON]", "Andy Jassy": "[PERSON]",
    "Craig Federighi": "[PERSON]", "Clement Delangue": "[PERSON]",
    "Ben Horowitz": "[PERSON]", "Chris Dixon": "[PERSON]",
    "Jack Clark": "[PERSON]", "Jared Kaplan": "[PERSON]",
    "Tom Brown": "[PERSON]", "Chris Olah": "[PERSON]",
    "Sam McCandlish": "[PERSON]", "Mike Krieger": "[PERSON]",
    "Stuart Russell": "[PERSON]", "Pieter Abbeel": "[PERSON]",
    "Christopher Manning": "[PERSON]", "Michael I. Jordan": "[PERSON]",
    "Trevor Darrell": "[PERSON]", "Yoshua Bengio": "[PERSON]",
    "Winston Weinberg": "[PERSON]", "Lip-Bu Tan": "[PERSON]",
    "Jakob Uszkoreit": "[PERSON]", "Illia Polosukhin": "[PERSON]",
    "Lukasz Kaiser": "[PERSON]", "Llion Jones": "[PERSON]",
    "Niki Parmar": "[PERSON]", "Nat Friedman": "[PERSON]",
    "Daniel Gross": "[PERSON]", "Naveen Rao": "[PERSON]",
    "Jan Leike": "[PERSON]", "Brendan Foody": "[PERSON]",
    "Adarsh Hiremath": "[PERSON]", "Surya Midha": "[PERSON]",
    "Clay Bavor": "[PERSON]", "Aman Sanger": "[PERSON]",
    "Sualeh Asif": "[PERSON]", "May Habib": "[PERSON]",
    "Adam D'Angelo": "[PERSON]", "Martin Casado": "[PERSON]",
    "Daphne Koller": "[PERSON]", "Rene Haas": "[PERSON]",
    "Brett Adcock": "[PERSON]", "Navrina Singh": "[PERSON]",
    "Sarah Guo": "[PERSON]", "Igor Babuschkin": "[PERSON]",
    "Jimmy Ba": "[PERSON]", "Karol Hausman": "[PERSON]",
    "Barret Zoph": "[PERSON]", "Soumith Chintala": "[PERSON]",
    "Kevin Scott": "[PERSON]", "Steve Huffman": "[PERSON]",
    "Emad Mostaque": "[PERSON]", "Edwin Chen": "[PERSON]",
    "Arvid Lunnemark": "[PERSON]", "Trae Stephens": "[PERSON]",
    "Dorsa Sadigh": "[PERSON]", "Michael Kratsios": "[PERSON]",
    # Unique last names -- also replace individually
    "Huang": "[PERSON]", "Altman": "[PERSON]", "Musk": "[PERSON]",
    "Pichai": "[PERSON]", "Zuckerberg": "[PERSON]", "Ellison": "[PERSON]",
    "Brin": "[PERSON]", "Amodei": "[PERSON]", "Bezos": "[PERSON]",
    "Hassabis": "[PERSON]", "Sutskever": "[PERSON]", "Nadella": "[PERSON]",
    "LeCun": "[PERSON]", "Hinton": "[PERSON]", "Suleyman": "[PERSON]",
    "Andreessen": "[PERSON]", "Thiel": "[PERSON]", "Murati": "[PERSON]",
    "Brockman": "[PERSON]", "Shazeer": "[PERSON]", "Hoffman": "[PERSON]",
    "Khosla": "[PERSON]", "Vaswani": "[PERSON]", "Truell": "[PERSON]",
    "Srinivas": "[PERSON]", "Sacks": "[PERSON]", "Krishnan": "[PERSON]",
    "Ghodsi": "[PERSON]", "Karp": "[PERSON]", "Gomez": "[PERSON]",
    "Intrator": "[PERSON]", "Luckey": "[PERSON]", "Pachocki": "[PERSON]",
    "Jassy": "[PERSON]", "Federighi": "[PERSON]", "Delangue": "[PERSON]",
    "Horowitz": "[PERSON]", "Kaplan": "[PERSON]", "Olah": "[PERSON]",
    "McCandlish": "[PERSON]", "Krieger": "[PERSON]", "Abbeel": "[PERSON]",
    "Darrell": "[PERSON]", "Bengio": "[PERSON]", "Weinberg": "[PERSON]",
    "Uszkoreit": "[PERSON]", "Polosukhin": "[PERSON]",
    "Parmar": "[PERSON]", "Friedman": "[PERSON]",
    "Leike": "[PERSON]", "Hiremath": "[PERSON]", "Midha": "[PERSON]",
    "Bavor": "[PERSON]", "Sanger": "[PERSON]",
    "Habib": "[PERSON]", "D'Angelo": "[PERSON]", "Casado": "[PERSON]",
    "Koller": "[PERSON]", "Haas": "[PERSON]", "Adcock": "[PERSON]",
    "Babuschkin": "[PERSON]", "Hausman": "[PERSON]", "Zoph": "[PERSON]",
    "Chintala": "[PERSON]", "Huffman": "[PERSON]", "Mostaque": "[PERSON]",
    "Lunnemark": "[PERSON]", "Stephens": "[PERSON]", "Sadigh": "[PERSON]",
    "Kratsios": "[PERSON]",
}

COMPANY_NAMES = {
    # Major tech companies
    "NVIDIA": "[FIRMA]", "Nvidia": "[FIRMA]",
    "OpenAI": "[FIRMA]", "Google DeepMind": "[FIRMA]",
    "DeepMind": "[FIRMA]", "Google": "[FIRMA]", "Alphabet": "[FIRMA]",
    "Meta Platforms": "[FIRMA]", "Meta": "[FIRMA]", "Facebook": "[FIRMA]",
    "Anthropic": "[FIRMA]", "Amazon": "[FIRMA]", "AWS": "[FIRMA]",
    "Microsoft": "[FIRMA]", "Apple": "[FIRMA]",
    "Tesla": "[FIRMA]", "SpaceX": "[FIRMA]",
    "Neuralink": "[FIRMA]", "xAI": "[FIRMA]",
    "Blue Origin": "[FIRMA]", "Oracle": "[FIRMA]",
    "SoftBank": "[FIRMA]", "AMD": "[FIRMA]",
    # AI startups
    "Cohere": "[FIRMA]", "Perplexity": "[FIRMA]",
    "Inflection AI": "[FIRMA]", "Inflection": "[FIRMA]",
    "Scale AI": "[FIRMA]", "Databricks": "[FIRMA]",
    "Anduril": "[FIRMA]", "Figure AI": "[FIRMA]",
    "Cursor": "[FIRMA]", "Anysphere": "[FIRMA]",
    "Stability AI": "[FIRMA]", "Hugging Face": "[FIRMA]",
    "a16z": "[FIRMA]", "Andreessen Horowitz": "[FIRMA]",
    "Founders Fund": "[FIRMA]", "Greylock": "[FIRMA]",
    "Sequoia": "[FIRMA]", "Y Combinator": "[FIRMA]",
    "Palantir": "[FIRMA]", "Reddit": "[FIRMA]",
    "Quora": "[FIRMA]", "Writer": "[FIRMA]",
    "Coursera": "[FIRMA]", "insitro": "[FIRMA]",
    "Arm": "[FIRMA]", "Arm Holdings": "[FIRMA]",
    "Sierra": "[FIRMA]", "CoreWeave": "[FIRMA]",
    "SSI": "[FIRMA]", "Safe Superintelligence": "[FIRMA]",
    "Sakana AI": "[FIRMA]", "NEAR Protocol": "[FIRMA]",
    "Physical Intelligence": "[FIRMA]",
    "Thinking Machines Lab": "[FIRMA]",
    "Surge AI": "[FIRMA]", "Credo AI": "[FIRMA]",
    "Conviction": "[FIRMA]",
    # Platforms
    "Instagram": "[FIRMA]", "WhatsApp": "[FIRMA]",
    "YouTube": "[FIRMA]", "LinkedIn": "[FIRMA]",
    "PayPal": "[FIRMA]", "Twitter": "[PLATTFORM]",
    "X (formerly Twitter)": "[PLATTFORM]",
    # Universities
    "Stanford": "[UNI]", "MIT": "[UNI]", "Berkeley": "[UNI]",
    "Carnegie Mellon": "[UNI]", "Toronto": "[UNI]",
    "Montreal": "[UNI]", "Oxford": "[UNI]", "Cambridge": "[UNI]",
}

# Product names -- reveal the company/person
PRODUCT_NAMES = {
    # OpenAI products
    "ChatGPT": "[PRODUKT]", "GPT-4o": "[PRODUKT]", "GPT-4": "[PRODUKT]",
    "GPT-3.5": "[PRODUKT]", "GPT-3": "[PRODUKT]", "GPT-2": "[PRODUKT]",
    "GPT-1": "[PRODUKT]", "DALL-E 3": "[PRODUKT]", "DALL-E 2": "[PRODUKT]",
    "DALL-E": "[PRODUKT]", "Codex": "[PRODUKT]", "Whisper": "[PRODUKT]",
    "Sora": "[PRODUKT]", "o1": "[PRODUKT-REASONING]", "o3": "[PRODUKT-REASONING]",
    # Anthropic products
    "Claude 3.5 Sonnet": "[PRODUKT]", "Claude 3 Opus": "[PRODUKT]",
    "Claude 3": "[PRODUKT]", "Claude 2": "[PRODUKT]",
    "Claude": "[PRODUKT]",
    # Google products
    "Gemini Ultra": "[PRODUKT]", "Gemini Pro": "[PRODUKT]",
    "Gemini": "[PRODUKT]", "Bard": "[PRODUKT]",
    "AlphaFold": "[PRODUKT]", "AlphaGo": "[PRODUKT]",
    "AlphaZero": "[PRODUKT]", "LaMDA": "[PRODUKT]",
    "PaLM 2": "[PRODUKT]", "PaLM": "[PRODUKT]",
    # Meta products
    "Llama 3": "[PRODUKT]", "Llama 2": "[PRODUKT]", "Llama": "[PRODUKT]",
    # xAI products
    "Grok-2": "[PRODUKT]", "Grok-1": "[PRODUKT]", "Grok": "[PRODUKT]",
    # Microsoft products
    "Copilot": "[PRODUKT]", "GitHub Copilot": "[PRODUKT]",
    "Bing Chat": "[PRODUKT]",
    # Other AI products
    "Midjourney": "[PRODUKT]", "Stable Diffusion": "[PRODUKT]",
    "Pepper": "[PRODUKT-ROBOTER]",
    # Projects
    "Stargate": "[PROJEKT]", "Project Stargate": "[PROJEKT]",
    "Project Izanagi": "[PROJEKT]",
    "Worldcoin": "[PROJEKT]", "World ID": "[PROJEKT]",
    # Generic GPT catch-all (AFTER specific GPT variants)
    "GPT": "[PRODUKT-FAMILIE]",
}

# Combined dictionary
BLIND_REPLACEMENTS = {**PERSON_NAMES, **COMPANY_NAMES, **PRODUCT_NAMES}

def blind_text(text):
    """Removes all identifying information from a text."""
    if not text:
        return text
    result = text
    # Replace longer strings first (to avoid partial match issues)
    for original, replacement in sorted(BLIND_REPLACEMENTS.items(), key=lambda x: -len(x[0])):
        result = result.replace(original, replacement)
    return result

def extract_person(conn, person_id):
    """Extracts and blinds all data for a person."""
    c = conn.cursor()

    # Person info (internal use only)
    c.execute("SELECT name, rang FROM personen WHERE id=?", (person_id,))
    person = c.fetchone()
    if not person:
        return None, None, None

    # Statements (aussagen)
    c.execute("""
        SELECT aussage_text, datum_aussage, kontext, modus
        FROM aussagen
        WHERE person_id=? AND einschluss=1
        ORDER BY datum_aussage
    """, (person_id,))
    aussagen = c.fetchall()

    # Actions (handlungen)
    c.execute("""
        SELECT handlung_typ, beschreibung, datum_handlung, betrag_usd
        FROM handlungen
        WHERE person_id=?
        ORDER BY datum_handlung
    """, (person_id,))
    handlungen = c.fetchall()

    return person, aussagen, handlungen

def format_blinded_corpus(aussagen, handlungen, label=""):
    """Formats a blinded data corpus as text."""
    lines = []
    if label:
        lines.append(f"=== DATENKORPUS {label} ===\n")

    lines.append(f"--- AUSSAGEN ({len(aussagen)} Stueck) ---\n")
    for i, (text, datum, kontext, modus) in enumerate(aussagen, 1):
        bt = blind_text(text)
        bk = blind_text(kontext) if kontext else ""
        datum_str = datum if datum else "unbekannt"
        lines.append(f"[A{i:03d}] ({datum_str}, {modus})")
        lines.append(f"  \"{bt}\"")
        if bk:
            lines.append(f"  Kontext: {bk}")
        lines.append("")

    lines.append(f"\n--- HANDLUNGEN ({len(handlungen)} Stueck) ---\n")
    for i, (typ, beschr, datum, betrag) in enumerate(handlungen, 1):
        bb = blind_text(beschr)
        datum_str = datum if datum else "unbekannt"
        betrag_str = f" (${betrag:,.0f})" if betrag else ""
        lines.append(f"[H{i:03d}] ({datum_str}) [{typ}]{betrag_str}")
        lines.append(f"  {bb}")
        lines.append("")

    return "\n".join(lines)

def main():
    conn = sqlite3.connect(DB_PATH)

    if len(sys.argv) < 2:
        print("Usage: python extract_blinded.py <person_id>")
        print("       python extract_blinded.py --top10")
        print("       python extract_blinded.py --top10-collective")
        print("       python extract_blinded.py --all")
        print("       python extract_blinded.py --all-collective")
        sys.exit(1)

    if sys.argv[1] == "--all":
        # Individual corpora for ALL 100 persons
        c = conn.cursor()
        c.execute("SELECT id, name FROM personen ORDER BY id")
        persons = c.fetchall()
        total_a, total_h = 0, 0
        for pid, name in persons:
            person, aussagen, handlungen = extract_person(conn, pid)
            if person and (len(aussagen) > 0 or len(handlungen) > 0):
                corpus = format_blinded_corpus(aussagen, handlungen, f"PERSON-{pid}")
                outpath = os.path.join(os.path.dirname(DB_PATH),
                    f"../_results/synthesen/individual/corpus_person_{pid}.txt")
                os.makedirs(os.path.dirname(outpath), exist_ok=True)
                with open(outpath, "w", encoding="utf-8") as f:
                    f.write(corpus)
                total_a += len(aussagen)
                total_h += len(handlungen)
                print(f"  {pid:3d} {name:25s}: {len(aussagen):2d}A + {len(handlungen):2d}H -> corpus_person_{pid}.txt")
            else:
                print(f"  {pid:3d} {name:25s}: NO DATA")
        print(f"\nTotal: {total_a}A + {total_h}H for {len(persons)} persons")

    elif sys.argv[1] == "--all-collective":
        # Collective corpus of all 100 persons
        c = conn.cursor()
        c.execute("SELECT id FROM personen ORDER BY id")
        all_aussagen = []
        all_handlungen = []
        for (pid,) in c.fetchall():
            _, aussagen, handlungen = extract_person(conn, pid)
            all_aussagen.extend(aussagen)
            all_handlungen.extend(handlungen)
        corpus = format_blinded_corpus(all_aussagen, all_handlungen, "ALLE-100-KOLLEKTIV")
        outpath = os.path.join(os.path.dirname(DB_PATH),
            "../_results/synthesen/corpus_all100_collective.txt")
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(corpus)
        print(f"Alle-100-Kollektiv: {len(all_aussagen)}A + {len(all_handlungen)}H")

    elif sys.argv[1] == "--top10":
        # Individual Top-10 corpora
        top10_ids = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
        for pid in top10_ids:
            person, aussagen, handlungen = extract_person(conn, pid)
            if person:
                corpus = format_blinded_corpus(aussagen, handlungen, f"PERSON-{pid}")
                outpath = os.path.join(os.path.dirname(DB_PATH),
                    f"../_results/synthesen/individual/corpus_person_{pid}.txt")
                os.makedirs(os.path.dirname(outpath), exist_ok=True)
                with open(outpath, "w", encoding="utf-8") as f:
                    f.write(corpus)
                print(f"  {person[0]:25s}: {len(aussagen)}A + {len(handlungen)}H -> corpus_person_{pid}.txt")

    elif sys.argv[1] == "--top10-collective":
        # Collective Top-10 corpus
        top10_ids = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
        all_aussagen = []
        all_handlungen = []
        for pid in top10_ids:
            _, aussagen, handlungen = extract_person(conn, pid)
            all_aussagen.extend(aussagen)
            all_handlungen.extend(handlungen)
        corpus = format_blinded_corpus(all_aussagen, all_handlungen, "TOP-10-KOLLEKTIV")
        outpath = os.path.join(os.path.dirname(DB_PATH),
            "../_results/synthesen/corpus_top10_collective.txt")
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(corpus)
        print(f"Top-10-Kollektiv: {len(all_aussagen)}A + {len(all_handlungen)}H")

    else:
        person_id = int(sys.argv[1])
        person, aussagen, handlungen = extract_person(conn, person_id)
        if person:
            corpus = format_blinded_corpus(aussagen, handlungen)
            print(corpus)
        else:
            print(f"Person {person_id} not found.")

    conn.close()

if __name__ == "__main__":
    main()
