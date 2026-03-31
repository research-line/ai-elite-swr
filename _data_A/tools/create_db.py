#!/usr/bin/env python3
"""
Creates the SQLite database for the statement collection of the Top 100 AI personalities.
Research project: Transhumanism / Silicon Valley Worldviews
Date: 2026-02-11
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")

# If DB already exists, delete and recreate
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA journal_mode=WAL")
conn.execute("PRAGMA foreign_keys=ON")
cur = conn.cursor()

# ============================================================
# TABLES
# ============================================================

cur.executescript("""
-- personen = persons (from Top-100 research)
CREATE TABLE personen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rang INTEGER NOT NULL,
    name TEXT NOT NULL,
    rolle TEXT,
    firmen TEXT,
    sv_verbindung TEXT,
    score_a INTEGER DEFAULT 0,
    score_b INTEGER DEFAULT 0,
    score_c INTEGER DEFAULT 0,
    score_d INTEGER DEFAULT 0,
    score_e INTEGER DEFAULT 0,
    score_f INTEGER DEFAULT 0,
    score_gesamt INTEGER DEFAULT 0,
    notizen TEXT,
    erstellt_am TEXT DEFAULT (datetime('now')),
    aktualisiert_am TEXT DEFAULT (datetime('now'))
);

-- plattformen = platforms (YouTube, Twitter/X, Reddit, etc.)
CREATE TABLE plattformen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    typ TEXT,
    url_template TEXT,
    ergiebigkeit TEXT CHECK(ergiebigkeit IN ('sehr_hoch','hoch','mittel','niedrig')),
    notizen TEXT
);

-- quellen_typen = source types (video, post, interview, book, etc.)
CREATE TABLE quellen_typen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    beschreibung TEXT
);

-- kategorien = categories (WV, SB, MB, ET, GE, RI, FO, MA, AR, TR, RE, SP + secondary)
CREATE TABLE kategorien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    beschreibung TEXT,
    typ TEXT CHECK(typ IN ('primaer','sekundaer')) DEFAULT 'primaer',
    beispiel TEXT
);

-- aussagen = statements (core table)
CREATE TABLE aussagen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER NOT NULL,
    aussage_text TEXT NOT NULL,
    aussage_kurz TEXT,
    modus TEXT CHECK(modus IN ('muendlich','schriftlich','unbekannt')) DEFAULT 'unbekannt',
    quellen_typ_id INTEGER,
    plattform_id INTEGER,
    quell_link TEXT,
    quell_titel TEXT,
    datum_aussage TEXT,
    datum_quelle TEXT,
    datum_abruf TEXT DEFAULT (date('now')),
    sprache TEXT DEFAULT 'en',
    originalitaet INTEGER DEFAULT 1,
    einschluss INTEGER DEFAULT 1,
    grenzfall INTEGER DEFAULT 0,
    kontext TEXT,
    notizen TEXT,
    erfasst_von TEXT DEFAULT 'Claude',
    erstellt_am TEXT DEFAULT (datetime('now')),
    aktualisiert_am TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (person_id) REFERENCES personen(id),
    FOREIGN KEY (quellen_typ_id) REFERENCES quellen_typen(id),
    FOREIGN KEY (plattform_id) REFERENCES plattformen(id)
);

-- aussagen_kategorien = statements <-> categories (n:m)
CREATE TABLE aussagen_kategorien (
    aussage_id INTEGER NOT NULL,
    kategorie_id INTEGER NOT NULL,
    PRIMARY KEY (aussage_id, kategorie_id),
    FOREIGN KEY (aussage_id) REFERENCES aussagen(id) ON DELETE CASCADE,
    FOREIGN KEY (kategorie_id) REFERENCES kategorien(id)
);

-- suchprotokolle = search logs (documentation of each search)
CREATE TABLE suchprotokolle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    plattform_id INTEGER,
    suchbegriffe TEXT NOT NULL,
    ergebnis_anzahl INTEGER DEFAULT 0,
    relevante_treffer INTEGER DEFAULT 0,
    datum_suche TEXT DEFAULT (datetime('now')),
    notizen TEXT,
    durchgefuehrt_von TEXT DEFAULT 'Claude',
    FOREIGN KEY (person_id) REFERENCES personen(id),
    FOREIGN KEY (plattform_id) REFERENCES plattformen(id)
);
""")

# ============================================================
# INDEXES
# ============================================================

cur.executescript("""
CREATE INDEX idx_aussagen_person ON aussagen(person_id);
CREATE INDEX idx_aussagen_einschluss ON aussagen(einschluss);
CREATE INDEX idx_aussagen_datum ON aussagen(datum_aussage);
CREATE INDEX idx_aussagen_plattform ON aussagen(plattform_id);
CREATE INDEX idx_aussagen_kat_aussage ON aussagen_kategorien(aussage_id);
CREATE INDEX idx_aussagen_kat_kategorie ON aussagen_kategorien(kategorie_id);
CREATE INDEX idx_suchprotokolle_person ON suchprotokolle(person_id);
""")

# ============================================================
# VIEWS
# ============================================================

cur.executescript("""
-- Full view of a statement with person, platform, source type
CREATE VIEW v_aussagen_komplett AS
SELECT
    a.id AS aussage_id,
    p.rang,
    p.name AS person,
    a.aussage_text,
    a.aussage_kurz,
    a.modus,
    qt.name AS quellen_typ,
    pl.name AS plattform,
    a.quell_link,
    a.quell_titel,
    a.datum_aussage,
    a.datum_quelle,
    a.datum_abruf,
    a.sprache,
    a.originalitaet,
    a.einschluss,
    a.grenzfall,
    a.kontext,
    a.notizen
FROM aussagen a
JOIN personen p ON a.person_id = p.id
LEFT JOIN quellen_typen qt ON a.quellen_typ_id = qt.id
LEFT JOIN plattformen pl ON a.plattform_id = pl.id;

-- Statements with assigned categories (one row per category assignment)
CREATE VIEW v_aussagen_mit_kategorien AS
SELECT
    a.id AS aussage_id,
    p.name AS person,
    a.aussage_kurz,
    k.code AS kategorie_code,
    k.name AS kategorie_name,
    k.typ AS kategorie_typ,
    a.einschluss
FROM aussagen a
JOIN personen p ON a.person_id = p.id
JOIN aussagen_kategorien ak ON a.id = ak.aussage_id
JOIN kategorien k ON ak.kategorie_id = k.id;

-- Statistics per person
CREATE VIEW v_statistik_personen AS
SELECT
    p.rang,
    p.name,
    p.score_gesamt,
    COUNT(a.id) AS anzahl_aussagen,
    SUM(CASE WHEN a.einschluss = 1 THEN 1 ELSE 0 END) AS eingeschlossen,
    SUM(CASE WHEN a.einschluss = 0 THEN 1 ELSE 0 END) AS ausgeschlossen,
    SUM(CASE WHEN a.grenzfall = 1 THEN 1 ELSE 0 END) AS grenzfaelle
FROM personen p
LEFT JOIN aussagen a ON p.id = a.person_id
GROUP BY p.id
ORDER BY p.rang;

-- Statistics per category
CREATE VIEW v_statistik_kategorien AS
SELECT
    k.code,
    k.name,
    k.typ,
    COUNT(ak.aussage_id) AS anzahl_zuordnungen,
    COUNT(DISTINCT a.person_id) AS anzahl_personen
FROM kategorien k
LEFT JOIN aussagen_kategorien ak ON k.id = ak.kategorie_id
LEFT JOIN aussagen a ON ak.aussage_id = a.id AND a.einschluss = 1
GROUP BY k.id
ORDER BY k.typ, anzahl_zuordnungen DESC;
""")

# ============================================================
# MASTER DATA: Platforms
# ============================================================

plattformen = [
    ("YouTube", "Video-Plattform", "https://youtube.com/results?search_query={query}", "sehr_hoch"),
    ("Twitter/X", "Mikroblogging", "https://x.com/search?q={query}", "hoch"),
    ("Podcasts", "Audio-Langform", None, "sehr_hoch"),
    ("Konferenzen", "Vortraege/Panels", None, "hoch"),
    ("Nachrichtenmedien", "Interviews/Profile", None, "hoch"),
    ("LinkedIn", "Berufliches Netzwerk", "https://linkedin.com/search/results/content/?keywords={query}", "mittel"),
    ("Reddit", "Diskussionsforum", "https://reddit.com/search/?q={query}", "mittel"),
    ("Buecher", "Monographien/Aufsaetze", None, "mittel"),
    ("Blogs", "Persoenliche/Firmenblogs", None, "mittel"),
    ("Congressional Testimony", "Offizielle Anhoerungen", None, "niedrig"),
    ("Wikiquote", "Zitatesammlung", "https://en.wikiquote.org/wiki/{query}", "niedrig"),
    ("Goodreads", "Buchzitate", None, "niedrig"),
    ("BrainyQuote", "Allgemeine Zitate", "https://brainyquote.com/search_results?q={query}", "niedrig"),
    ("Substack", "Newsletter", "https://substack.com/search/{query}", "mittel"),
    ("Google Scholar", "Akademische Artikel", "https://scholar.google.com/scholar?q={query}", "mittel"),
    ("TED", "TED Talks", "https://ted.com/search?q={query}", "hoch"),
    ("Sonstige", "Andere Quellen", None, "niedrig"),
]

cur.executemany(
    "INSERT INTO plattformen (name, typ, url_template, ergiebigkeit) VALUES (?, ?, ?, ?)",
    plattformen
)

# ============================================================
# MASTER DATA: Source types
# ============================================================

quellen_typen = [
    ("Video-Interview", "Aufgezeichnetes Interview (YouTube, TV, Konferenz)"),
    ("Podcast-Interview", "Audio-Interview in Podcast-Format"),
    ("Keynote/Vortrag", "Oeffentlicher Vortrag oder Keynote"),
    ("Panel-Diskussion", "Gespraeche mit mehreren Teilnehmern"),
    ("Social-Media-Post", "Twitter/X, LinkedIn, etc."),
    ("Blog-Artikel", "Persoenlicher oder Firmenblog"),
    ("Nachrichtenartikel", "Zeitungsinterview, Profil-Artikel"),
    ("Buch", "Monographie oder Buchkapitel"),
    ("Wissenschaftlicher Artikel", "Paper, Preprint, Aufsatz"),
    ("Offizielle Stellungnahme", "Testimony, offizielle Erklaerung"),
    ("AMA/Q&A", "Ask Me Anything, oeffentliche Fragerunde"),
]

cur.executemany(
    "INSERT INTO quellen_typen (name, beschreibung) VALUES (?, ?)",
    quellen_typen
)

# ============================================================
# MASTER DATA: Categories
# ============================================================

kategorien = [
    # Primary categories
    ("WV", "Weltvision", "Aussagen ueber die Zukunft der Welt/Menschheit", "primaer",
     "AI will be the most transformative technology in human history"),
    ("SB", "Selbstbild", "Aussagen ueber die eigene Rolle, Mission, Motivation", "primaer",
     "I feel a deep responsibility to get this right"),
    ("MB", "Menschenbild", "Aussagen ueber das Wesen des Menschen, Bewusstsein", "primaer",
     "What makes us human is our ability to..."),
    ("ET", "Ethik/Werte", "Aussagen ueber Moral, Verantwortung, richtig/falsch", "primaer",
     "We have an obligation to ensure AI benefits everyone"),
    ("GE", "Gesellschaft", "Aussagen ueber Gesellschaftsstruktur, Ungleichheit, Politik", "primaer",
     "The wealth created by AI must be distributed more broadly"),
    ("RI", "Risiko/Sicherheit", "Aussagen ueber KI-Risiken, existenzielle Bedrohung", "primaer",
     "The probability of doom is..."),
    ("FO", "Fortschritt/Beschleunigung", "Aussagen ueber Tempo, Disruption, Acceleration", "primaer",
     "We are moving faster than anyone expected"),
    ("MA", "Macht/Kontrolle", "Aussagen ueber Machtkonzentration, Zugang, Kontrolle", "primaer",
     "Open source ensures no single entity controls AI"),
    ("AR", "Arbeit/Wirtschaft", "Aussagen ueber Arbeitsmarkt, UBI, Automatisierung", "primaer",
     "Most jobs will be transformed within a decade"),
    ("TR", "Transhumanismus", "Aussagen ueber Verschmelzung Mensch-Maschine, Post-Humanity", "primaer",
     "Brain-computer interfaces will extend human cognition"),
    ("RE", "Regulierung", "Aussagen ueber Gesetze, Governance, internationale Kooperation", "primaer",
     "We need global AI governance frameworks"),
    ("SP", "Spiritualitaet/Sinn", "Aussagen ueber Sinn, Zweck, Spiritualitaet, Transzendenz", "primaer",
     "AI raises profound questions about consciousness"),
    # Secondary codes
    ("OPT", "Optimistisch", "Optimistischer Tenor der Aussage", "sekundaer", None),
    ("PES", "Pessimistisch", "Pessimistischer Tenor der Aussage", "sekundaer", None),
    ("AMB", "Ambivalent", "Ambivalenter Tenor der Aussage", "sekundaer", None),
    ("POL", "Politisch", "Politisch konnotierte Aussage", "sekundaer", None),
    ("PHI", "Philosophisch", "Philosophisch reflektierte Aussage", "sekundaer", None),
    ("EMP", "Empirisch", "Empirisch gestuetzte Aussage", "sekundaer", None),
    ("ANE", "Anekdotisch", "Anekdotische Aussage", "sekundaer", None),
    ("PRO", "Provokant", "Provokante/kontroverse Aussage", "sekundaer", None),
]

cur.executemany(
    "INSERT INTO kategorien (code, name, beschreibung, typ, beispiel) VALUES (?, ?, ?, ?, ?)",
    kategorien
)

# ============================================================
# MASTER DATA: Top 100 persons (personen)
# ============================================================

personen = [
    (1, "Jensen Huang", "CEO & Mitgruender", "NVIDIA", "HQ, WO", 9, 6, 3, 4, 1, 5, 28),
    (2, "Sam Altman", "CEO", "OpenAI", "HQ, WO, INV", 9, 4, 0, 4, 3, 5, 25),
    (3, "Elon Musk", "CEO & Gruender", "xAI, Tesla, SpaceX", "HQ, WO, INV", 9, 6, 0, 4, 1, 5, 25),
    (4, "Sundar Pichai", "CEO", "Alphabet/Google", "HQ, WO, UNI", 9, 6, 0, 4, 1, 5, 25),
    (5, "Mark Zuckerberg", "CEO & Gruender", "Meta", "HQ, WO", 9, 6, 0, 4, 0, 5, 24),
    (6, "Larry Page", "Mitgruender, Board", "Alphabet/Google", "HQ, WO, UNI", 6, 6, 0, 3, 0, 5, 20),
    (7, "Larry Ellison", "Gruender & CTO", "Oracle", "HQ, WO", 5, 6, 0, 3, 1, 5, 20),
    (8, "Sergey Brin", "Mitgruender", "Alphabet/Google", "HQ, WO, UNI", 6, 6, 0, 3, 0, 5, 20),
    (9, "Dario Amodei", "CEO & Mitgruender", "Anthropic", "HQ, WO, AG", 9, 4, 3, 4, 0, 5, 25),
    (10, "Jeff Bezos", "Gruender", "Amazon", "AG, INV", 6, 6, 0, 3, 0, 5, 20),
    (11, "Demis Hassabis", "CEO", "Google DeepMind", "AG, UNI", 9, 4, 5, 4, 1, 5, 28),
    (12, "Ilya Sutskever", "CEO & Mitgruender", "Safe Superintelligence", "HQ, AG", 9, 4, 4, 3, 0, 5, 25),
    (13, "Satya Nadella", "CEO", "Microsoft", "INV, AG", 5, 6, 0, 3, 1, 4, 19),
    (14, "Lisa Su", "CEO", "AMD", "HQ", 5, 5, 0, 4, 0, 4, 18),
    (15, "Tim Cook", "CEO", "Apple", "HQ, WO", 5, 6, 0, 3, 1, 3, 18),
    (16, "Masayoshi Son", "CEO & Gruender", "SoftBank / Stargate", "INV", 6, 6, 0, 3, 1, 3, 19),
    (17, "Daniela Amodei", "President & Mitgruenderin", "Anthropic", "HQ, AG", 7, 4, 0, 3, 0, 4, 18),
    (18, "Fei-Fei Li", "Professorin & Gruenderin", "Stanford / World Labs", "UNI, HQ", 4, 3, 5, 4, 1, 5, 22),
    (19, "Jeff Dean", "Chief Scientist", "Google", "HQ, WO", 5, 4, 4, 3, 0, 4, 20),
    (20, "Yann LeCun", "Gruender", "AMI Labs (ex-Meta FAIR)", "AG", 6, 4, 5, 3, 1, 5, 24),
    (21, "Geoffrey Hinton", "Prof. emeritus", "U of Toronto (ex-Google)", "AG", 2, 3, 5, 4, 2, 5, 21),
    (22, "Andrew Ng", "Gruender & Professor", "AI Fund, Landing AI, Stanford", "UNI, HQ, WO", 6, 3, 4, 3, 1, 4, 21),
    (23, "Mustafa Suleyman", "CEO Microsoft AI", "Microsoft AI", "AG, HQ", 7, 4, 2, 3, 0, 4, 20),
    (24, "Marc Andreessen", "Mitgruender", "Andreessen Horowitz", "HQ, WO, INV", 4, 5, 0, 3, 2, 4, 18),
    (25, "Peter Thiel", "Mitgruender & Investor", "Founders Fund, Palantir", "HQ, WO, INV", 4, 5, 0, 3, 2, 4, 18),
    (26, "Mira Murati", "CEO & Gruenderin", "Thinking Machines Lab", "HQ, AG", 7, 4, 2, 3, 0, 4, 20),
    (27, "Bret Taylor", "Chairman & Mitgruender", "OpenAI Board, Sierra AI", "HQ, WO, AG", 7, 4, 0, 3, 0, 4, 18),
    (28, "Greg Brockman", "President & Mitgruender", "OpenAI", "HQ, WO", 7, 3, 0, 3, 0, 4, 17),
    (29, "Alexandr Wang", "Chief AI Officer", "Meta (ex-Scale AI)", "HQ, AG", 7, 4, 0, 4, 1, 4, 20),
    (30, "Noam Shazeer", "VP Engineering", "Google DeepMind", "HQ, AG", 5, 4, 4, 2, 0, 3, 18),
    (31, "Reid Hoffman", "Partner & Mitgruender", "Greylock, Manas AI", "HQ, WO, INV", 4, 4, 0, 3, 1, 3, 15),
    (32, "Vinod Khosla", "Gruender", "Khosla Ventures", "HQ, WO, INV", 2, 5, 0, 3, 1, 3, 14),
    (33, "Ashish Vaswani", "CEO & Mitgruender", "Essential AI", "HQ, AG", 6, 3, 4, 2, 0, 3, 18),
    (34, "Michael Truell", "CEO & Mitgruender", "Anysphere/Cursor", "HQ", 6, 4, 0, 2, 0, 3, 15),
    (35, "Aravind Srinivas", "CEO & Mitgruender", "Perplexity AI", "HQ, UNI, AG", 6, 4, 2, 3, 0, 3, 18),
    (36, "David Sacks", "AI/Crypto Czar", "White House", "HQ, WO, INV", 2, 4, 0, 3, 3, 4, 16),
    (37, "Sriram Krishnan", "Senior AI Policy Advisor", "White House", "AG, HQ", 2, 2, 0, 2, 3, 3, 12),
    (38, "Ali Ghodsi", "CEO & Mitgruender", "Databricks", "HQ, UNI", 6, 4, 2, 3, 0, 3, 18),
    (39, "Alex Karp", "CEO", "Palantir", "HQ, UNI", 5, 5, 0, 3, 1, 3, 17),
    (40, "Aidan Gomez", "CEO & Mitgruender", "Cohere", "AG", 6, 4, 4, 2, 0, 3, 19),
    (41, "Michael Intrator", "CEO & Mitgruender", "CoreWeave", "INV, AG", 6, 5, 0, 2, 0, 3, 16),
    (42, "Scott Wu", "CEO & Mitgruender", "Cognition AI", "HQ", 6, 4, 0, 2, 0, 3, 15),
    (43, "Palmer Luckey", "Gruender", "Anduril Industries", "HQ, WO", 6, 4, 0, 3, 1, 3, 17),
    (44, "Jakub Pachocki", "Chief Scientist", "OpenAI", "HQ, AG", 5, 3, 3, 2, 0, 3, 16),
    (45, "Mark Chen", "SVP Research", "OpenAI", "HQ, AG", 5, 3, 2, 2, 0, 3, 15),
    (46, "Andy Jassy", "CEO", "Amazon (AWS AI)", "INV, AG", 5, 6, 0, 3, 0, 3, 17),
    (47, "Craig Federighi", "SVP Software Engineering", "Apple", "HQ, WO", 5, 4, 0, 2, 0, 2, 13),
    (48, "Clement Delangue", "CEO & Mitgruender", "Hugging Face", "HQ, UNI", 6, 3, 0, 3, 0, 3, 15),
    (49, "Ben Horowitz", "Mitgruender", "Andreessen Horowitz", "HQ, WO, INV", 4, 5, 0, 2, 1, 3, 15),
    (50, "Chris Dixon", "General Partner", "Andreessen Horowitz", "HQ, INV", 3, 4, 0, 2, 0, 2, 11),
    (51, "Jack Clark", "Mitgruender", "Anthropic", "HQ", 4, 3, 1, 2, 1, 3, 14),
    (52, "Jared Kaplan", "Chief Science Officer", "Anthropic", "HQ, UNI", 5, 3, 3, 1, 0, 3, 15),
    (53, "Tom Brown", "Mitgruender", "Anthropic", "HQ, AG", 4, 3, 3, 1, 0, 3, 14),
    (54, "Chris Olah", "Mitgruender, Interpretability Lead", "Anthropic", "HQ, AG", 4, 3, 3, 1, 0, 3, 14),
    (55, "Sam McCandlish", "Chief Architect, Mitgruender", "Anthropic", "HQ", 5, 3, 2, 1, 0, 3, 14),
    (56, "Mike Krieger", "Head of Product", "Anthropic", "HQ, AG", 5, 3, 0, 2, 0, 2, 12),
    (57, "Stuart Russell", "Professor, Mitgruender", "UC Berkeley, CHAI", "UNI, HQ", 2, 0, 5, 3, 2, 3, 15),
    (58, "Pieter Abbeel", "Professor & Mitgruender", "UC Berkeley, Covariant", "UNI, AG", 4, 3, 4, 2, 0, 3, 16),
    (59, "Christopher Manning", "Professor", "Stanford NLP", "UNI", 2, 0, 4, 2, 0, 2, 10),
    (60, "Michael I. Jordan", "Professor", "UC Berkeley", "UNI", 2, 0, 5, 2, 0, 2, 11),
    (61, "Trevor Darrell", "Professor, Co-Director BAIR", "UC Berkeley", "UNI", 2, 0, 4, 2, 0, 2, 10),
    (62, "Yoshua Bengio", "Chair/Gruender", "LawZero, MILA", "AG", 4, 2, 5, 3, 2, 4, 20),
    (63, "Winston Weinberg", "CEO & Mitgruender", "Harvey AI", "HQ", 6, 3, 0, 2, 0, 2, 13),
    (64, "Lip-Bu Tan", "CEO", "Intel", "HQ", 5, 4, 0, 2, 0, 2, 13),
    (65, "Jakob Uszkoreit", "CEO & Mitgruender", "Inceptive", "AG, HQ", 4, 3, 4, 1, 0, 2, 14),
    (66, "Illia Polosukhin", "Mitgruender", "NEAR Protocol", "AG", 4, 3, 4, 1, 0, 2, 14),
    (67, "Lukasz Kaiser", "Researcher", "OpenAI", "HQ, AG", 3, 2, 4, 1, 0, 2, 12),
    (68, "Llion Jones", "Mitgruender", "Sakana AI", "AG", 4, 3, 4, 1, 0, 2, 14),
    (69, "Niki Parmar", "Mitgruenderin", "(ex-Google Brain)", "AG", 2, 2, 4, 1, 0, 1, 10),
    (70, "Nat Friedman", "VP Product", "Meta", "HQ, AG", 5, 4, 0, 3, 0, 3, 15),
    (71, "Daniel Gross", "Superintendent AI", "Meta", "HQ, AG", 5, 4, 0, 2, 0, 3, 14),
    (72, "Naveen Rao", "Gruender & CEO", "Unconventional AI", "HQ, AG", 4, 3, 1, 1, 0, 2, 11),
    (73, "Jan Leike", "Head of Safety", "Anthropic", "HQ, AG", 3, 2, 3, 1, 1, 2, 12),
    (74, "Brendan Foody", "Mitgruender", "Mercor", "HQ", 4, 4, 0, 1, 0, 2, 11),
    (75, "Adarsh Hiremath", "Mitgruender", "Mercor", "HQ", 4, 4, 0, 1, 0, 2, 11),
    (76, "Surya Midha", "Mitgruender", "Mercor", "HQ", 4, 4, 0, 1, 0, 2, 11),
    (77, "Clay Bavor", "Mitgruender", "Sierra AI", "HQ, AG", 4, 4, 0, 1, 0, 2, 11),
    (78, "Aman Sanger", "COO & Mitgruender", "Anysphere/Cursor", "HQ", 5, 4, 0, 1, 0, 2, 12),
    (79, "Sualeh Asif", "CPO & Mitgruender", "Anysphere/Cursor", "HQ", 5, 4, 0, 1, 0, 2, 12),
    (80, "May Habib", "CEO & Mitgruenderin", "Writer", "HQ", 4, 3, 0, 2, 0, 2, 11),
    (81, "Adam D'Angelo", "Board Member, CEO", "OpenAI Board, Quora", "HQ, AG", 4, 3, 0, 2, 0, 3, 12),
    (82, "Martin Casado", "General Partner", "Andreessen Horowitz", "HQ, INV", 3, 3, 1, 2, 0, 2, 11),
    (83, "Daphne Koller", "CEO & Mitgruenderin", "insitro", "HQ, UNI", 4, 3, 4, 2, 0, 2, 15),
    (84, "Rene Haas", "CEO", "Arm", "AG, HQ", 5, 4, 0, 2, 0, 2, 13),
    (85, "Brett Adcock", "CEO & Gruender", "Figure AI", "HQ", 6, 3, 0, 2, 0, 2, 13),
    (86, "Navrina Singh", "CEO & Gruenderin", "Credo AI", "HQ", 4, 2, 0, 3, 1, 2, 12),
    (87, "Sarah Guo", "Gruenderin", "Conviction", "HQ, INV", 3, 3, 0, 2, 0, 2, 10),
    (88, "Igor Babuschkin", "Mitgruender", "xAI", "HQ", 4, 2, 2, 1, 0, 2, 11),
    (89, "Jimmy Ba", "Mitgruender", "xAI", "HQ, AG", 4, 2, 3, 1, 0, 2, 12),
    (90, "Karol Hausman", "Mitgruender", "Physical Intelligence", "HQ, UNI, AG", 4, 3, 3, 1, 0, 2, 13),
    (91, "Barret Zoph", "VP Research", "OpenAI", "HQ, AG", 4, 2, 2, 1, 0, 2, 11),
    (92, "Soumith Chintala", "CTO", "Thinking Machines Lab", "HQ, AG", 4, 2, 3, 1, 0, 2, 12),
    (93, "Kevin Scott", "CTO", "Microsoft", "AG, HQ", 5, 4, 0, 2, 0, 2, 13),
    (94, "Steve Huffman", "CEO", "Reddit", "HQ", 4, 3, 0, 2, 0, 2, 11),
    (95, "Emad Mostaque", "Gruender", "Stability AI", "AG, HQ", 4, 3, 0, 2, 0, 2, 11),
    (96, "Edwin Chen", "CEO", "Surge AI", "HQ", 4, 5, 0, 1, 0, 1, 11),
    (97, "Arvid Lunnemark", "Mitgruender", "Integrous Research", "HQ", 4, 4, 0, 1, 0, 1, 10),
    (98, "Trae Stephens", "Mitgruender", "Anduril, Founders Fund", "HQ, INV", 4, 3, 0, 2, 1, 2, 12),
    (99, "Dorsa Sadigh", "Professorin", "Stanford", "UNI", 2, 0, 3, 2, 0, 1, 8),
    (100, "Michael Kratsios", "Direktor OSTP", "White House", "AG, HQ", 2, 2, 0, 2, 3, 2, 11),
]

cur.executemany(
    """INSERT INTO personen (rang, name, rolle, firmen, sv_verbindung,
       score_a, score_b, score_c, score_d, score_e, score_f, score_gesamt)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
    personen
)

conn.commit()

# ============================================================
# VALIDATION
# ============================================================

print("=" * 60)
print("DATABASE CREATED:", DB_PATH)
print("=" * 60)

for table in ["personen", "plattformen", "quellen_typen", "kategorien",
              "aussagen", "aussagen_kategorien", "suchprotokolle"]:
    count = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"  {table:25s} -> {count:4d} entries")

print("-" * 60)
print("Views:")
for view in ["v_aussagen_komplett", "v_aussagen_mit_kategorien",
             "v_statistik_personen", "v_statistik_kategorien"]:
    try:
        cur.execute(f"SELECT * FROM {view} LIMIT 1")
        print(f"  {view:35s} -> OK")
    except Exception as e:
        print(f"  {view:35s} -> ERROR: {e}")

print("-" * 60)
print("Indexes:")
indexes = cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%'").fetchall()
for idx in indexes:
    print(f"  {idx[0]}")

print("-" * 60)
print("Sample persons (Top 5):")
for row in cur.execute("SELECT rang, name, score_gesamt FROM personen ORDER BY rang LIMIT 5"):
    print(f"  Rank {row[0]:3d}: {row[1]:20s} (Score: {row[2]})")

print("-" * 60)
print("Sample categories:")
for row in cur.execute("SELECT code, name, typ FROM kategorien ORDER BY typ, code"):
    print(f"  [{row[0]:3s}] {row[1]:25s} ({row[2]})")

print("=" * 60)
print("DONE. Database ready for statement collection.")
print("=" * 60)

conn.close()
