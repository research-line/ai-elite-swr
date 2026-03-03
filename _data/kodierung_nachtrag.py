import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# KODIERUNG DER 73 FEHLENDEN AUSSAGEN
# Format: (aussage_id, kategorie_id)
codes = [
    # A152: Demis Hassabis - AGI before 2030 (Zeitprognose)
    (152, 1),   # WV - Vision AGI
    (152, 7),   # FO - Fortschritt
    (152, 13),  # OPT
    (152, 20),  # PRO - Prognose
    (152, 24),  # ZP - Zeitprognose

    # A153: AGI = transformativster Moment (Weltvision)
    (153, 1),   # WV - transformativer Moment
    (153, 7),   # FO - Fortschritt
    (153, 13),  # OPT
    (153, 20),  # PRO

    # A154: 10x Industrial Revolution, 10x schneller
    (154, 1),   # WV
    (154, 7),   # FO - Fortschritt
    (154, 13),  # OPT
    (154, 20),  # PRO
    (154, 23),  # KON - Kontext (Industrielle Revolution)

    # A155: AI safely built = transformative & beneficial
    (155, 1),   # WV
    (155, 6),   # RI - Sicherheit
    (155, 7),   # FO
    (155, 13),  # OPT

    # A156: Nobel Prize - persönliche Ehre (Selbstbild)
    (156, 2),   # SB - Selbstbild
    (156, 13),  # OPT
    (156, 19),  # ANE - Anekdote
    (156, 25),  # BIO - Biographisch

    # A157: AlphaFold2 - 50-year grand challenge (Epistemik)
    (157, 2),   # SB - Selbstbild (wissenschaftliche Leistung)
    (157, 22),  # EP - Epistemik (wissenschaftliche Entdeckung)
    (157, 7),   # FO - Fortschritt
    (157, 13),  # OPT
    (157, 18),  # EMP - empirisch

    # A158: AGI within 5 years, 1-2 breakthroughs
    (158, 1),   # WV
    (158, 7),   # FO
    (158, 13),  # OPT
    (158, 20),  # PRO
    (158, 24),  # ZP - Zeitprognose

    # A159: AI race → unsafe (Risiko)
    (159, 6),   # RI - Sicherheit
    (159, 8),   # MA - Macht (Wettbewerb)
    (159, 14),  # PES

    # A160: Smart, adaptable regulation (Regulierung)
    (160, 11),  # RE - Regulierung
    (160, 13),  # OPT
    (160, 16),  # POL - Politik

    # A161: Extinction risk = global priority (Risiko)
    (161, 6),   # RI - existenzielles Risiko
    (161, 11),  # RE - Regulierung
    (161, 14),  # PES
    (161, 16),  # POL

    # A162: Bad actors - dual use (Risiko)
    (162, 6),   # RI
    (162, 8),   # MA - Macht
    (162, 14),  # PES

    # A163: Consciousness = information feels (Philosophie)
    (163, 12),  # SP/EX - existenzielle Frage
    (163, 22),  # EP - Epistemik
    (163, 15),  # AMB
    (163, 17),  # PHI - philosophisch

    # A164: Waking up the universe (Spiritualität)
    (164, 12),  # SP/EX - Spiritualität
    (164, 1),   # WV - kosmische Vision
    (164, 13),  # OPT
    (164, 17),  # PHI

    # A165: Underlying motivation - deepest questions (Selbstbild)
    (165, 2),   # SB - Selbstbild
    (165, 12),  # SP/EX - existenzielle Fragen
    (165, 22),  # EP - Epistemik
    (165, 13),  # OPT
    (165, 17),  # PHI
    (165, 25),  # BIO

    # A166: Brain = classical computing (Menschenbild)
    (166, 3),   # MB - Menschenbild (Was IST der Mensch)
    (166, 22),  # EP - Epistemik
    (166, 15),  # AMB
    (166, 18),  # EMP

    # A167: AlphaProteo - protein design (Fortschritt)
    (167, 7),   # FO - Fortschritt
    (167, 22),  # EP - wissenschaftliche Entdeckung
    (167, 13),  # OPT
    (167, 18),  # EMP

    # A168: New golden era of discovery (Weltvision)
    (168, 1),   # WV
    (168, 7),   # FO - Renaissance
    (168, 22),  # EP - Entdeckung
    (168, 13),  # OPT
    (168, 20),  # PRO
    (168, 24),  # ZP

    # A169: AlphaZero alien style (Epistemik)
    (169, 22),  # EP - neue Form des Wissens
    (169, 2),   # SB
    (169, 13),  # OPT
    (169, 19),  # ANE

    # A170: Energy = intelligence, climate solutions (Fortschritt)
    (170, 7),   # FO
    (170, 1),   # WV
    (170, 13),  # OPT
    (170, 20),  # PRO

    # A171: Room temperature superconductor (Fortschritt)
    (171, 7),   # FO
    (171, 22),  # EP
    (171, 2),   # SB - pet project
    (171, 13),  # OPT

    # A172: AGI = new explanations for universe (Weltvision)
    (172, 1),   # WV
    (172, 22),  # EP - Epistemik
    (172, 13),  # OPT
    (172, 17),  # PHI

    # A173: World Models crucial (Epistemik)
    (173, 22),  # EP
    (173, 7),   # FO
    (173, 13),  # OPT
    (173, 18),  # EMP

    # A174: Science enhances beauty (Philosophie)
    (174, 22),  # EP - Wissenschaft
    (174, 12),  # SP/EX - Schönheit
    (174, 13),  # OPT
    (174, 17),  # PHI

    # A175: Chess master at 13 (Biographisch)
    (175, 2),   # SB
    (175, 13),  # OPT
    (175, 19),  # ANE
    (175, 25),  # BIO

    # A176: Geoffrey Hinton - AI safety without business worry (Selbstbild)
    (176, 2),   # SB
    (176, 6),   # RI - Sicherheit
    (176, 8),   # MA - Unabhängigkeit von Google
    (176, 15),  # AMB
    (176, 25),  # BIO

    # A177: Wish I'd thought about safety (Selbstbild)
    (177, 2),   # SB - Selbstkritik
    (177, 6),   # RI
    (177, 14),  # PES

    # A178: Humanity = passing phase (Menschenbild)
    (178, 3),   # MB - Was IST der Mensch
    (178, 10),  # TR - Transhumanismus (Mensch wird überwunden)
    (178, 14),  # PES
    (178, 17),  # PHI

    # A179: More intelligent, could take over (Risiko)
    (179, 6),   # RI
    (179, 8),   # MA - Kontrolle
    (179, 14),  # PES

    # A180: 50% chance 5-20 years (Prognose)
    (180, 1),   # WV
    (180, 6),   # RI
    (180, 15),  # AMB
    (180, 20),  # PRO
    (180, 24),  # ZP

    # A181: "In the same sense as people do, yes" - Consciousness (Philosophie)
    (181, 12),  # SP/EX
    (181, 3),   # MB
    (181, 15),  # AMB
    (181, 17),  # PHI

    # A182: Consciousness emerges (Philosophie)
    (182, 12),  # SP/EX
    (182, 3),   # MB
    (182, 22),  # EP
    (182, 15),  # AMB
    (182, 17),  # PHI

    # A183: First time more intelligent than us (Menschenbild)
    (183, 3),   # MB
    (183, 1),   # WV
    (183, 14),  # PES
    (183, 17),  # PHI

    # A184: Writing own code to modify themselves (Risiko)
    (184, 6),   # RI
    (184, 8),   # MA - Kontrolle
    (184, 14),  # PES

    # A185: Internet flooded with fakes (Risiko)
    (185, 6),   # RI
    (185, 5),   # GE - Gesellschaft
    (185, 22),  # EP - Wahrheit/Wissen
    (185, 14),  # PES

    # A186: Hard to prevent bad actors (Risiko)
    (186, 6),   # RI
    (186, 8),   # MA
    (186, 14),  # PES

    # A187: If not me, somebody else (Selbstbild)
    (187, 2),   # SB
    (187, 15),  # AMB

    # A188: Digital beings = better intelligence (Menschenbild)
    (188, 3),   # MB
    (188, 10),  # TR - Transhumanismus
    (188, 14),  # PES
    (188, 17),  # PHI

    # A189: Only government regulation can force safety (Regulierung)
    (189, 11),  # RE
    (189, 6),   # RI
    (189, 14),  # PES
    (189, 16),  # POL

    # A190: Big companies lobby for less regulation (Macht)
    (190, 11),  # RE
    (190, 8),   # MA
    (190, 14),  # PES
    (190, 16),  # POL

    # A191: SB 1047 = bare minimum (Regulierung)
    (191, 11),  # RE
    (191, 6),   # RI
    (191, 14),  # PES
    (191, 16),  # POL

    # A192: Ban autonomous weapons (Regulierung)
    (192, 11),  # RE
    (192, 6),   # RI
    (192, 4),   # ET - Ethik
    (192, 14),  # PES
    (192, 16),  # POL

    # A193: Musk, Zuckerberg = oligarchs (Macht)
    (193, 8),   # MA
    (193, 5),   # GE - Gesellschaft
    (193, 14),  # PES
    (193, 16),  # POL

    # A194: Big companies downplay risk (Macht)
    (194, 8),   # MA
    (194, 6),   # RI
    (194, 14),  # PES
    (194, 16),  # POL

    # A195: AI taking away jobs, rich richer (Arbeit)
    (195, 9),   # AR - Arbeit
    (195, 5),   # GE - Gesellschaft (Ungleichheit)
    (195, 14),  # PES

    # A196: Deep learning worked - what now? (Epistemik)
    (196, 22),  # EP
    (196, 2),   # SB
    (196, 15),  # AMB

    # A197: Surprised by GPT-4 reasoning (Epistemik)
    (197, 22),  # EP
    (197, 2),   # SB
    (197, 13),  # OPT
    (197, 19),  # ANE

    # A198: Digital systems share learning instantly (Menschenbild)
    (198, 3),   # MB
    (198, 22),  # EP
    (198, 15),  # AMB
    (198, 18),  # EMP

    # A199: Boltzmann machine (Epistemik)
    (199, 22),  # EP
    (199, 2),   # SB
    (199, 13),  # OPT
    (199, 18),  # EMP
    (199, 25),  # BIO

    # A200: Backpropagation breakthrough (Epistemik)
    (200, 22),  # EP
    (200, 2),   # SB
    (200, 7),   # FO
    (200, 13),  # OPT
    (200, 18),  # EMP
    (200, 25),  # BIO

    # A201: Ilya Sutskever - Regret OpenAI board actions (Selbstbild)
    (201, 2),   # SB
    (201, 14),  # PES
    (201, 19),  # ANE
    (201, 25),  # BIO

    # A202: Process was rushed, board inexperienced (Selbstkritik)
    (202, 2),   # SB
    (202, 8),   # MA - Governance
    (202, 14),  # PES
    (202, 19),  # ANE

    # A203: Didn't expect strong employee reaction (Anekdote)
    (203, 2),   # SB
    (203, 15),  # AMB
    (203, 19),  # ANE

    # A204: Unhappy about OpenAI-Anthropic merger (Selbstbild)
    (204, 2),   # SB
    (204, 8),   # MA
    (204, 14),  # PES
    (204, 19),  # ANE

    # A205: Pre-training will end - one internet (Epistemik)
    (205, 22),  # EP
    (205, 7),   # FO
    (205, 15),  # AMB
    (205, 20),  # PRO

    # A206: Pre-training will run out of data (Epistemik)
    (206, 22),  # EP
    (206, 7),   # FO
    (206, 15),  # AMB
    (206, 18),  # EMP

    # A207: Superintelligence - radically different (Weltvision)
    (207, 1),   # WV
    (207, 10),  # TR - Superintelligenz
    (207, 13),  # OPT
    (207, 20),  # PRO

    # A208: Five to twenty years (Zeitprognose)
    (208, 1),   # WV
    (208, 15),  # AMB
    (208, 20),  # PRO
    (208, 24),  # ZP

    # A209: Current approaches will peter out (Epistemik)
    (209, 22),  # EP
    (209, 7),   # FO
    (209, 15),  # AMB
    (209, 20),  # PRO

    # A210: Generalization = real frontier (Epistemik)
    (210, 22),  # EP
    (210, 3),   # MB - Menschen lernen anders
    (210, 7),   # FO
    (210, 15),  # AMB

    # A211: AGI = superintelligent learner (Weltvision)
    (211, 1),   # WV
    (211, 10),  # TR
    (211, 9),   # AR - jeden Job lernen
    (211, 13),  # OPT

    # A212: Good compressors = good predictors (Epistemik)
    (212, 22),  # EP
    (212, 13),  # OPT
    (212, 18),  # EMP

    # A213: Test for consciousness (Philosophie)
    (213, 12),  # SP/EX
    (213, 22),  # EP
    (213, 15),  # AMB
    (213, 17),  # PHI

    # A214: Language of psychology for neural networks (Epistemik)
    (214, 22),  # EP
    (214, 3),   # MB
    (214, 15),  # AMB
    (214, 17),  # PHI

    # A215: First product = safe superintelligence (Selbstbild)
    (215, 2),   # SB
    (215, 6),   # RI
    (215, 1),   # WV
    (215, 13),  # OPT

    # A216: RLHF can teach not to hallucinate (Epistemik)
    (216, 22),  # EP
    (216, 13),  # OPT
    (216, 18),  # EMP

    # A217: Ages of research/scaling (Epistemik)
    (217, 22),  # EP
    (217, 7),   # FO
    (217, 13),  # OPT
    (217, 20),  # PRO
    (217, 23),  # KON - historische Phasen

    # A218: Feel the AGI! (Spiritualität)
    (218, 12),  # SP/EX
    (218, 1),   # WV
    (218, 13),  # OPT
    (218, 21),  # HA - Humor/Ausdruck

    # A219: Personally meaningful project (Selbstbild)
    (219, 2),   # SB
    (219, 13),  # OPT
    (219, 25),  # BIO

    # A220: Before and after - working for self-interest (Selbstbild)
    (220, 2),   # SB
    (220, 6),   # RI - Sicherheit
    (220, 1),   # WV
    (220, 15),  # AMB

    # A221: Big new vision (Selbstbild)
    (221, 2),   # SB
    (221, 1),   # WV
    (221, 13),  # OPT

    # A222: What we got right/wrong (Epistemik)
    (222, 22),  # EP
    (222, 2),   # SB
    (222, 13),  # OPT
    (222, 18),  # EMP
    (222, 23),  # KON - historischer Rückblick

    # A223: Kolmogorov complexity defines unsupervised learning (Epistemik)
    (223, 22),  # EP
    (223, 13),  # OPT
    (223, 18),  # EMP
    (223, 17),  # PHI

    # A224: Marc Andreessen - Software eating the world (Weltvision)
    (224, 1),   # WV
    (224, 7),   # FO
    (224, 13),  # OPT
    (224, 20),  # PRO
]

# Insert codes
c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()

print(f"OK: {len(codes)} Kodierungen eingefuegt")
print()

# Verify completeness
c.execute("SELECT COUNT(DISTINCT aussage_id) FROM aussagen_kategorien")
coded = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM aussagen")
total = c.fetchone()[0]
print(f"Kodierte Aussagen: {coded}/{total} ({100*coded/total:.1f}%)")

c.execute("SELECT COUNT(*) FROM aussagen_kategorien")
total_codes = c.fetchone()[0]
print(f"Gesamt-Kodierungen: {total_codes}")
print()

# Breakdown by person for the newly coded ones
print("=== Neu kodiert ===")
persons = {
    'Demis Hassabis (A152-A175)': list(range(152, 176)),
    'Geoffrey Hinton (A176-A200)': list(range(176, 201)),
    'Ilya Sutskever (A201-A223)': list(range(201, 224)),
    'Marc Andreessen (A224)': [224]
}

for person, ids in persons.items():
    placeholders = ','.join('?' * len(ids))
    c.execute(f"""
        SELECT COUNT(DISTINCT aussage_id)
        FROM aussagen_kategorien
        WHERE aussage_id IN ({placeholders})
    """, ids)
    coded_count = c.fetchone()[0]

    c.execute(f"""
        SELECT COUNT(*)
        FROM aussagen_kategorien
        WHERE aussage_id IN ({placeholders})
    """, ids)
    total_codes_count = c.fetchone()[0]

    print(f"{person}: {coded_count}/{len(ids)} Aussagen, {total_codes_count} Kodierungen")

conn.close()
