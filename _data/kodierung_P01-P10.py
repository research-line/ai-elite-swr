# -*- coding: utf-8 -*-
"""
Kodierung der Aussagen P1-P10 nach dem 26-Kategorien-Schema
Erstellt: 2026-02-12
"""

import sqlite3

# Verbindung zur Datenbank
conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Format: (aussage_id, kategorie_id) Paare
# Jede Aussage bekommt: 1-2 primäre Kategorien + 1 Tonalität + 0-n Modus/Struktur
codes = [
    # A1: Sam Altman - "lights out for all of us"
    (1, 6),   # RI - Risiko/Gefahren
    (1, 1),   # WV - Weltvision (worst case)
    (1, 14),  # PES - Pessimistisch
    (1, 20),  # PRO - Provokant

    # A2: Sam Altman - "happy that we are scared"
    (2, 6),   # RI - Risiko
    (2, 2),   # SB - Selbstbild (wir bei OpenAI)
    (2, 15),  # AMB - Ambivalent
    (2, 22),  # EP - Epistemik (Unsicherheit)

    # A3: Sam Altman - "should not trust me"
    (3, 2),   # SB - Selbstbild/Rolle
    (3, 6),   # RI - Risiko
    (3, 14),  # PES - Pessimistisch
    (3, 4),   # ET - Ethik (Verantwortung)

    # A4: Sam Altman - "worst fears, significant harm"
    (4, 6),   # RI - Risiko
    (4, 14),  # PES - Pessimistisch
    (4, 22),  # EP - Epistemik

    # A5: Sam Altman - "regulatory intervention critical"
    (5, 11),  # RE - Regulierung
    (5, 6),   # RI - Risiko (Begründung für Regulierung)
    (5, 15),  # AMB - Ambivalent
    (5, 21),  # HA - Handlungsbezug
    (5, 16),  # POL - Politisch

    # A6: Sam Altman - "impact on jobs, government action"
    (6, 9),   # AR - Arbeit/Wirtschaft
    (6, 11),  # RE - Regulierung (government action)
    (6, 14),  # PES - Pessimistisch
    (6, 16),  # POL - Politisch
    (6, 21),  # HA - Handlungsbezug

    # A7: Sam Altman - "programs that can think, companions"
    (7, 7),   # FO - Fortschritt (Tech-Entwicklung)
    (7, 9),   # AR - Arbeit (assembly-line work)
    (7, 13),  # OPT - Optimistisch
    (7, 24),  # ZP - Zeitprognose
    (7, 18),  # EMP - Empirisch

    # A8: Sam Altman - "taxing capital, distribute wealth"
    (8, 11),  # RE - Regulierung (konkrete Governance)
    (8, 5),   # GE - Gesellschaft (Ungleichheit)
    (8, 13),  # OPT - Optimistisch
    (8, 16),  # POL - Politisch
    (8, 21),  # HA - Handlungsbezug

    # A9: Sam Altman - "elevate humanity, abundance"
    (9, 1),   # WV - Weltvision
    (9, 7),   # FO - Fortschritt
    (9, 13),  # OPT - Optimistisch
    (9, 17),  # PHI - Philosophisch

    # A10: Sam Altman - "misaligned superintelligent AGI, autocratic regime"
    (10, 6),  # RI - Risiko
    (10, 8),  # MA - Macht
    (10, 14), # PES - Pessimistisch
    (10, 16), # POL - Politisch

    # A11: Sam Altman - "not unqualified utopia, maximize good"
    (11, 1),  # WV - Weltvision
    (11, 4),  # ET - Ethik
    (11, 15), # AMB - Ambivalent
    (11, 17), # PHI - Philosophisch

    # A12: Sam Altman - "no one person in control"
    (12, 8),  # MA - Macht
    (12, 11), # RE - Regulierung/Governance
    (12, 13), # OPT - Optimistisch
    (12, 16), # POL - Politisch

    # A13: Sam Altman - "things go wrong, get shot"
    (13, 6),  # RI - Risiko
    (13, 2),  # SB - Selbstbild (persönliche Gefahr)
    (13, 14), # PES - Pessimistisch
    (13, 20), # PRO - Provokant
    (13, 19), # ANE - Anekdotisch

    # A14: Sam Altman - "sleight of hand, values I approve"
    (14, 4),  # ET - Ethik (Werte)
    (14, 8),  # MA - Macht (wessen Werte?)
    (14, 15), # AMB - Ambivalent
    (14, 17), # PHI - Philosophisch
    (14, 22), # EP - Epistemik (kritische Reflexion)

    # A15: Sam Altman - "stochastic parrot"
    (15, 3),  # MB - Menschenbild
    (15, 15), # AMB - Ambivalent
    (15, 17), # PHI - Philosophisch
    (15, 20), # PRO - Provokant

    # A16: Sam Altman - "superintelligence in few thousand days"
    (16, 7),  # FO - Fortschritt
    (16, 13), # OPT - Optimistisch
    (16, 24), # ZP - Zeitprognose
    (16, 22), # EP - Epistemik (confidence)

    # A17: Sam Altman - "future so bright, massive prosperity"
    (17, 1),  # WV - Weltvision
    (17, 13), # OPT - Optimistisch
    (17, 17), # PHI - Philosophisch
    (17, 24), # ZP - Zeitprognose

    # A18: Sam Altman - "deep learning worked, learn any distribution"
    (18, 7),  # FO - Fortschritt
    (18, 13), # OPT - Optimistisch
    (18, 18), # EMP - Empirisch
    (18, 17), # PHI - Philosophisch

    # A19: Sam Altman - "confident how to build AGI, AI agents join workforce"
    (19, 7),  # FO - Fortschritt
    (19, 9),  # AR - Arbeit/Wirtschaft
    (19, 13), # OPT - Optimistisch
    (19, 22), # EP - Epistemik (confidence)
    (19, 24), # ZP - Zeitprognose

    # A20: Sam Altman - "big failure of governance"
    (20, 11), # RE - Regulierung/Governance
    (20, 2),  # SB - Selbstbild (myself included)
    (20, 14), # PES - Pessimistisch
    (20, 25), # BIO - Biographische Legitimation

    # A21: Sam Altman - "sometimes wrong, don't want that driving car"
    (21, 6),  # RI - Risiko
    (21, 22), # EP - Epistemik (Grenzen des Wissens)
    (21, 14), # PES - Pessimistisch
    (21, 18), # EMP - Empirisch

    # A22: Sam Altman - "universal basic compute"
    (22, 5),  # GE - Gesellschaft (Verteilung)
    (22, 11), # RE - Regulierung (konkreter Vorschlag)
    (22, 13), # OPT - Optimistisch
    (22, 17), # PHI - Philosophisch
    (22, 26), # STR - Strategisch

    # A23: Sam Altman - "cost falls 10x every 12 months"
    (23, 7),  # FO - Fortschritt
    (23, 9),  # AR - Arbeit/Wirtschaft (economic impact)
    (23, 13), # OPT - Optimistisch
    (23, 18), # EMP - Empirisch

    # A24: Sam Altman - "marshall intellectual capacity, unlimited genius"
    (24, 1),  # WV - Weltvision
    (24, 5),  # GE - Gesellschaft (Demokratisierung)
    (24, 13), # OPT - Optimistisch
    (24, 24), # ZP - Zeitprognose

    # A25: Sam Altman - "wouldn't do this without you, Mr. President"
    (25, 8),  # MA - Macht (politische Allianz)
    (25, 16), # POL - Politisch
    (25, 13), # OPT - Optimistisch
    (25, 26), # STR - Strategisch

    # A26: Sam Altman - "not a super useful term"
    (26, 22), # EP - Epistemik (Begriffskritik)
    (26, 15), # AMB - Ambivalent

    # A27: Sam Altman - "end of world, but great companies"
    (27, 1),  # WV - Weltvision
    (27, 9),  # AR - Arbeit/Wirtschaft
    (27, 15), # AMB - Ambivalent
    (27, 20), # PRO - Provokant
    (27, 23), # KON - Kongruenz/Widerspruch

    # A28: Dario Amodei - "risks vs positive future"
    (28, 6),  # RI - Risiko
    (28, 1),  # WV - Weltvision (positive future)
    (28, 15), # AMB - Ambivalent
    (28, 2),  # SB - Selbstbild (my main reasons)

    # A29: Dario Amodei - "underestimating upside and risks"
    (29, 22), # EP - Epistemik (Menschen unterschätzen)
    (29, 6),  # RI - Risiko
    (29, 15), # AMB - Ambivalent
    (29, 17), # PHI - Philosophisch

    # A30: Dario Amodei - "compressed 21st century"
    (30, 1),  # WV - Weltvision
    (30, 7),  # FO - Fortschritt (Medizin/Biologie)
    (30, 13), # OPT - Optimistisch
    (30, 24), # ZP - Zeitprognose
    (30, 17), # PHI - Philosophisch

    # A31: Dario Amodei - "inspiring vision, hope not just fear"
    (31, 1),  # WV - Weltvision
    (31, 4),  # ET - Ethik
    (31, 13), # OPT - Optimistisch
    (31, 17), # PHI - Philosophisch
    (31, 21), # HA - Handlungsbezug

    # A32: Dario Amodei - "most important: how fast it is moving"
    (32, 7),  # FO - Fortschritt
    (32, 22), # EP - Epistemik (Verständnis)
    (32, 15), # AMB - Ambivalent
    (32, 18), # EMP - Empirisch

    # A33: Dario Amodei - "bioweapons, empower actors"
    (33, 6),  # RI - Risiko
    (33, 8),  # MA - Macht (larger set of actors)
    (33, 14), # PES - Pessimistisch
    (33, 18), # EMP - Empirisch
    (33, 24), # ZP - Zeitprognose

    # A34: Dario Amodei - "catastrophically wrong on scale of civilization"
    (34, 6),  # RI - Risiko
    (34, 1),  # WV - Weltvision
    (34, 14), # PES - Pessimistisch
    (34, 22), # EP - Epistemik (entirely possible)

    # A35: Dario Amodei - "rite of passage, test who we are"
    (35, 1),  # WV - Weltvision
    (35, 3),  # MB - Menschenbild (test as species)
    (35, 15), # AMB - Ambivalent
    (35, 17), # PHI - Philosophisch
    (35, 12), # SP/EX - Spiritualität/Existenzielles

    # A36: Dario Amodei - "country of geniuses in datacenter"
    (36, 7),  # FO - Fortschritt
    (36, 13), # OPT - Optimistisch
    (36, 17), # PHI - Philosophisch

    # A37: Dario Amodei - "least sensible voices, sensationalistic"
    (37, 22), # EP - Epistemik (Kritik an Diskurs)
    (37, 11), # RE - Regulierung (Diskurs darüber)
    (37, 14), # PES - Pessimistisch
    (37, 16), # POL - Politisch

    # A38: Dario Amodei - "realistic pragmatic manner, sober fact-based"
    (38, 22), # EP - Epistemik (Wissensanspruch)
    (38, 11), # RE - Regulierung (wie diskutieren)
    (38, 13), # OPT - Optimistisch
    (38, 21), # HA - Handlungsbezug

    # A39: Dario Amodei - "do not understand how AI works"
    (39, 22), # EP - Epistemik (lack of understanding)
    (39, 6),  # RI - Risiko (unprecedented)
    (39, 14), # PES - Pessimistisch
    (39, 18), # EMP - Empirisch

    # A40: Dario Amodei - "race between interpretability and intelligence"
    (40, 6),  # RI - Risiko
    (40, 7),  # FO - Fortschritt
    (40, 14), # PES - Pessimistisch
    (40, 17), # PHI - Philosophisch

    # A41: Dario Amodei - "can't stop bus, but can steer it"
    (41, 8),  # MA - Macht (Steuerung)
    (41, 11), # RE - Regulierung (wie gestalten)
    (41, 13), # OPT - Optimistisch
    (41, 17), # PHI - Philosophisch
    (41, 21), # HA - Handlungsbezug

    # A42: Dario Amodei - "uncomfortable with decisions by few companies"
    (42, 8),  # MA - Macht
    (42, 4),  # ET - Ethik (demokratische Legitimation)
    (42, 14), # PES - Pessimistisch
    (42, 2),  # SB - Selbstbild
    (42, 16), # POL - Politisch

    # A43: Dario Amodei - "head-spinningly fast, all bets off"
    (43, 7),  # FO - Fortschritt
    (43, 1),  # WV - Weltvision
    (43, 15), # AMB - Ambivalent
    (43, 24), # ZP - Zeitprognose
    (43, 22), # EP - Epistemik (all bets are off)

    # A44: Dario Amodei - "better than humans at intellectual tasks"
    (44, 7),  # FO - Fortschritt
    (44, 3),  # MB - Menschenbild (Vergleich mit Menschen)
    (44, 15), # AMB - Ambivalent
    (44, 5),  # GE - Gesellschaft (grapple with it)

    # A45: Dario Amodei - "wealth to AI companies, less to people"
    (45, 9),  # AR - Arbeit/Wirtschaft
    (45, 5),  # GE - Gesellschaft (Ungleichheit)
    (45, 14), # PES - Pessimistisch
    (45, 16), # POL - Politisch

    # A46: Dario Amodei - "public and politicians not aware"
    (46, 22), # EP - Epistemik (Unwissenheit)
    (46, 16), # POL - Politisch
    (46, 14), # PES - Pessimistisch
    (46, 5),  # GE - Gesellschaft

    # A47: Dario Amodei - "25% chance things go really badly"
    (47, 6),  # RI - Risiko
    (47, 14), # PES - Pessimistisch
    (47, 22), # EP - Epistemik (probabilistische Aussage)
    (47, 18), # EMP - Empirisch

    # A48: Dario Amodei - "democratic societies lead, not authoritarian"
    (48, 8),  # MA - Macht
    (48, 16), # POL - Politisch
    (48, 6),  # RI - Risiko (military dominance)
    (48, 13), # OPT - Optimistisch
    (48, 21), # HA - Handlungsbezug

    # A49: Dario Amodei - "excited about benefits, worried about risks"
    (49, 15), # AMB - Ambivalent
    (49, 6),  # RI - Risiko
    (49, 2),  # SB - Selbstbild

    # A50: Dario Amodei - "unproductive to argue, make your vision happen"
    (50, 2),  # SB - Selbstbild (leaving)
    (50, 8),  # MA - Macht (eigene Vision)
    (50, 13), # OPT - Optimistisch
    (50, 25), # BIO - Biographische Legitimation
    (50, 21), # HA - Handlungsbezug

    # A51: Dario Amodei - "better than humans at almost all tasks in 2-3 years"
    (51, 7),  # FO - Fortschritt
    (51, 3),  # MB - Menschenbild
    (51, 15), # AMB - Ambivalent
    (51, 24), # ZP - Zeitprognose

    # A52: Dario Amodei - "some players taking unwise risk"
    (52, 6),  # RI - Risiko
    (52, 8),  # MA - Macht (andere Player)
    (52, 14), # PES - Pessimistisch
    (52, 9),  # AR - Arbeit/Wirtschaft (economic value uncertain)

    # A53: Dario Amodei - "very little idea what we're talking about"
    (53, 22), # EP - Epistemik
    (53, 14), # PES - Pessimistisch
    (53, 20), # PRO - Provokant

    # A54: Dario Amodei - "half of entry-level jobs vanish in 1-5 years"
    (54, 9),  # AR - Arbeit/Wirtschaft
    (54, 14), # PES - Pessimistisch
    (54, 24), # ZP - Zeitprognose
    (54, 18), # EMP - Empirisch

    # A55: Jensen Huang - "AGI within 5 years"
    (55, 7),  # FO - Fortschritt
    (55, 13), # OPT - Optimistisch
    (55, 24), # ZP - Zeitprognose
    (55, 22), # EP - Epistemik (I believe)

    # A56: Jensen Huang - "superintelligent AI for various tasks"
    (56, 7),  # FO - Fortschritt
    (56, 9),  # AR - Arbeit/Wirtschaft
    (56, 13), # OPT - Optimistisch

    # A57: Jensen Huang - "AI's iPhone moment"
    (57, 7),  # FO - Fortschritt
    (57, 13), # OPT - Optimistisch
    (57, 18), # EMP - Empirisch

    # A58: Jensen Huang - "codifies culture, society's intelligence"
    (58, 5),  # GE - Gesellschaft (Kultur)
    (58, 8),  # MA - Macht (own your data)
    (58, 13), # OPT - Optimistisch
    (58, 16), # POL - Politisch

    # A59: Jensen Huang - "Nobody needs atomic bombs, everyone needs AI"
    (59, 7),  # FO - Fortschritt
    (59, 13), # OPT - Optimistisch
    (59, 20), # PRO - Provokant
    (59, 16), # POL - Politisch

    # A60: Jensen Huang - "AI is infrastructure, largest buildout"
    (60, 7),  # FO - Fortschritt
    (60, 9),  # AR - Arbeit/Wirtschaft (infrastructure)
    (60, 13), # OPT - Optimistisch
    (60, 18), # EMP - Empirisch

    # A61: Jensen Huang - "India should not export flour to import bread"
    (61, 8),  # MA - Macht (data sovereignty)
    (61, 5),  # GE - Gesellschaft (societal values)
    (61, 13), # OPT - Optimistisch
    (61, 16), # POL - Politisch
    (61, 26), # STR - Strategisch

    # A62: Jensen Huang - "TSMC pride of Taiwan, pride of world"
    (62, 2),  # SB - Selbstbild (Beziehung zu TSMC)
    (62, 9),  # AR - Arbeit/Wirtschaft
    (62, 13), # OPT - Optimistisch

    # A63: Jensen Huang - "TSMC is my family"
    (63, 2),  # SB - Selbstbild
    (63, 13), # OPT - Optimistisch
    (63, 19), # ANE - Anekdotisch

    # A64: Jensen Huang - "Elon singular in understanding engineering"
    (64, 2),  # SB - Selbstbild (Bewunderung)
    (64, 7),  # FO - Fortschritt
    (64, 13), # OPT - Optimistisch
    (64, 18), # EMP - Empirisch

    # A65: Jensen Huang - "humanity discovered algorithm"
    (65, 7),  # FO - Fortschritt
    (65, 3),  # MB - Menschenbild (humanity discovered)
    (65, 13), # OPT - Optimistisch
    (65, 17), # PHI - Philosophisch

    # A66: Jensen Huang - "$1 trillion computers upgraded"
    (66, 7),  # FO - Fortschritt
    (66, 9),  # AR - Arbeit/Wirtschaft
    (66, 13), # OPT - Optimistisch
    (66, 24), # ZP - Zeitprognose

    # A67: Jensen Huang - "perception AI to physical AI"
    (67, 7),  # FO - Fortschritt
    (67, 13), # OPT - Optimistisch
    (67, 18), # EMP - Empirisch

    # A68: Jensen Huang - "every layer transformed in 12 years"
    (68, 7),  # FO - Fortschritt
    (68, 13), # OPT - Optimistisch
    (68, 18), # EMP - Empirisch

    # A69: Jensen Huang - "get yourself AI tutor"
    (69, 5),  # GE - Gesellschaft (Bildung)
    (69, 13), # OPT - Optimistisch
    (69, 21), # HA - Handlungsbezug
    (69, 19), # ANE - Anekdotisch

    # A70: Jensen Huang - "TSMC dance with 400 partners vs Intel alone"
    (70, 9),  # AR - Arbeit/Wirtschaft (business strategy)
    (70, 13), # OPT - Optimistisch
    (70, 26), # STR - Strategisch

    # A71: Jensen Huang - "Blackwell engine for industrial revolution"
    (71, 7),  # FO - Fortschritt
    (71, 9),  # AR - Arbeit/Wirtschaft
    (71, 13), # OPT - Optimistisch
    (71, 2),  # SB - Selbstbild (Nvidia)

    # A72: Jensen Huang - "Meta Llama open source greatest thing"
    (72, 8),  # MA - Macht (open source)
    (72, 13), # OPT - Optimistisch
    (72, 5),  # GE - Gesellschaft (community)

    # A73: Jensen Huang - "every company will have AI"
    (73, 9),  # AR - Arbeit/Wirtschaft
    (73, 13), # OPT - Optimistisch
    (73, 24), # ZP - Zeitprognose

    # A74: Jensen Huang - "codify language, culture into LLM"
    (74, 5),  # GE - Gesellschaft (Kultur)
    (74, 8),  # MA - Macht (own LLM)
    (74, 13), # OPT - Optimistisch
    (74, 21), # HA - Handlungsbezug
    (74, 16), # POL - Politisch

    # A75: Jensen Huang - "half trillion infrastructure capacity"
    (75, 9),  # AR - Arbeit/Wirtschaft (Investitionen)
    (75, 13), # OPT - Optimistisch
    (75, 18), # EMP - Empirisch

    # A76: Jensen Huang - "business very strong, need capacity"
    (76, 9),  # AR - Arbeit/Wirtschaft
    (76, 13), # OPT - Optimistisch
    (76, 2),  # SB - Selbstbild (Nvidia)

    # A77: Sundar Pichai - "AI helpful for everyone"
    (77, 5),  # GE - Gesellschaft (for everyone)
    (77, 4),  # ET - Ethik (mission)
    (77, 13), # OPT - Optimistisch
    (77, 2),  # SB - Selbstbild (our mission)

    # A78: Sundar Pichai - "investing two decades, improve lives"
    (78, 7),  # FO - Fortschritt
    (78, 2),  # SB - Selbstbild (our mission)
    (78, 13), # OPT - Optimistisch
    (78, 25), # BIO - Biographische Legitimation

    # A79: Sundar Pichai - "most profound shift, democratize access"
    (79, 1),  # WV - Weltvision
    (79, 5),  # GE - Gesellschaft (Demokratisierung)
    (79, 13), # OPT - Optimistisch
    (79, 17), # PHI - Philosophisch

    # A80: Sundar Pichai - "most profound technology, societal disruption"
    (80, 7),  # FO - Fortschritt
    (80, 5),  # GE - Gesellschaft (disruption)
    (80, 15), # AMB - Ambivalent
    (80, 17), # PHI - Philosophisch

    # A81: Sundar Pichai - "technology enabler, equalizer"
    (81, 7),  # FO - Fortschritt
    (81, 5),  # GE - Gesellschaft (Gleichheit)
    (81, 13), # OPT - Optimistisch
    (81, 4),  # ET - Ethik

    # A82: Sundar Pichai - "most profound transition in our lifetimes"
    (82, 7),  # FO - Fortschritt
    (82, 1),  # WV - Weltvision
    (82, 13), # OPT - Optimistisch
    (82, 22), # EP - Epistemik (I believe)

    # A83: Sundar Pichai - "biggest upgrade to Bard, new era"
    (83, 7),  # FO - Fortschritt
    (83, 13), # OPT - Optimistisch
    (83, 2),  # SB - Selbstbild (Google)

    # A84: Sundar Pichai - "fully in Gemini era, investing decade"
    (84, 7),  # FO - Fortschritt
    (84, 2),  # SB - Selbstbild (Google)
    (84, 13), # OPT - Optimistisch
    (84, 25), # BIO - Biographische Legitimation

    # A85: Sundar Pichai - "AI Mode total reimagining of Search"
    (85, 7),  # FO - Fortschritt
    (85, 13), # OPT - Optimistisch
    (85, 2),  # SB - Selbstbild (Google Search)

    # A86: Sundar Pichai - "bold and responsible development"
    (86, 11), # RE - Regulierung
    (86, 4),  # ET - Ethik (responsible)
    (86, 13), # OPT - Optimistisch
    (86, 21), # HA - Handlungsbezug

    # A87: Sundar Pichai - "US must get balance right, national level"
    (87, 11), # RE - Regulierung
    (87, 16), # POL - Politisch
    (87, 8),  # MA - Macht (US vs China)
    (87, 15), # AMB - Ambivalent
    (87, 26), # STR - Strategisch

    # A88: Sundar Pichai - "countries work together, international frameworks"
    (88, 11), # RE - Regulierung
    (88, 16), # POL - Politisch
    (88, 6),  # RI - Risiko (weaponize)
    (88, 13), # OPT - Optimistisch
    (88, 21), # HA - Handlungsbezug

    # A89: Sundar Pichai - "people need to adapt, impact jobs, conversations"
    (89, 9),  # AR - Arbeit/Wirtschaft
    (89, 5),  # GE - Gesellschaft
    (89, 15), # AMB - Ambivalent
    (89, 21), # HA - Handlungsbezug

    # A90: Sundar Pichai - "people who adapt to AI will do better"
    (90, 9),  # AR - Arbeit/Wirtschaft
    (90, 5),  # GE - Gesellschaft (Ungleichheit)
    (90, 15), # AMB - Ambivalent
    (90, 21), # HA - Handlungsbezug

    # A91: Sundar Pichai - "democratize access, not AI divide"
    (91, 5),  # GE - Gesellschaft (AI divide)
    (91, 4),  # ET - Ethik
    (91, 13), # OPT - Optimistisch
    (91, 21), # HA - Handlungsbezug

    # A92: Sundar Pichai - "not replacing humans, augmenting capabilities"
    (92, 3),  # MB - Menschenbild
    (92, 7),  # FO - Fortschritt
    (92, 13), # OPT - Optimistisch
    (92, 17), # PHI - Philosophisch

    # A93: Sundar Pichai - "technology foundational enabler of progress"
    (93, 7),  # FO - Fortschritt
    (93, 1),  # WV - Weltvision
    (93, 13), # OPT - Optimistisch
    (93, 17), # PHI - Philosophisch

    # A94: Sundar Pichai - "don't blindly trust AI, people adapt"
    (94, 22), # EP - Epistemik (Grenzen des Vertrauens)
    (94, 6),  # RI - Risiko
    (94, 14), # PES - Pessimistisch
    (94, 21), # HA - Handlungsbezug

    # A95: Sundar Pichai - "Willow quantum chip breakthrough"
    (95, 7),  # FO - Fortschritt
    (95, 13), # OPT - Optimistisch
    (95, 18), # EMP - Empirisch
    (95, 2),  # SB - Selbstbild (Google)

    # A96: Sundar Pichai - "quantum for drug discovery, fusion energy"
    (96, 7),  # FO - Fortschritt
    (96, 13), # OPT - Optimistisch
    (96, 24), # ZP - Zeitprognose (journey)

    # A97: Sundar Pichai - "more profound than electricity or fire"
    (97, 7),  # FO - Fortschritt
    (97, 1),  # WV - Weltvision
    (97, 13), # OPT - Optimistisch
    (97, 17), # PHI - Philosophisch
    (97, 20), # PRO - Provokant

    # A98: Sundar Pichai - "2 billion products use Gemini, fastest adoption"
    (98, 7),  # FO - Fortschritt
    (98, 13), # OPT - Optimistisch
    (98, 2),  # SB - Selbstbild (Google)
    (98, 18), # EMP - Empirisch

    # A99: Sundar Pichai - "warned against AI divide"
    (99, 5),  # GE - Gesellschaft (AI divide)
    (99, 6),  # RI - Risiko
    (99, 14), # PES - Pessimistisch
    (99, 16), # POL - Politisch

    # A100: Sundar Pichai - "investing two decades, responsibility"
    (100, 7),  # FO - Fortschritt
    (100, 4),  # ET - Ethik (responsibility)
    (100, 13), # OPT - Optimistisch
    (100, 25), # BIO - Biographische Legitimation

    # A101: Elon Musk - "fundamental existential risk"
    (101, 6),  # RI - Risiko
    (101, 1),  # WV - Weltvision
    (101, 14), # PES - Pessimistisch
    (101, 20), # PRO - Provokant
    (101, 22), # EP - Epistemik (people don't appreciate)

    # A102: Elon Musk - "more dangerous than nukes, insane"
    (102, 6),  # RI - Risiko
    (102, 11), # RE - Regulierung (no oversight)
    (102, 14), # PES - Pessimistisch
    (102, 20), # PRO - Provokant
    (102, 16), # POL - Politisch

    # A103: Elon Musk - "games indistinguishable, most likely simulation"
    (103, 1),  # WV - Weltvision
    (103, 12), # SP/EX - Spiritualität/Existenzielles
    (103, 15), # AMB - Ambivalent
    (103, 17), # PHI - Philosophisch

    # A104: Elon Musk - "biological boot-loader for AI"
    (104, 3),  # MB - Menschenbild
    (104, 1),  # WV - Weltvision
    (104, 14), # PES - Pessimistisch
    (104, 17), # PHI - Philosophisch

    # A105: Elon Musk - "multi-planet civilization, long-term survival"
    (105, 1),  # WV - Weltvision
    (105, 6),  # RI - Risiko (survival)
    (105, 13), # OPT - Optimistisch
    (105, 21), # HA - Handlungsbezug
    (105, 17), # PHI - Philosophisch

    # A106: Elon Musk - "tempting to use AI as weapon, humans against each other"
    (106, 6),  # RI - Risiko
    (106, 8),  # MA - Macht (weapon)
    (106, 14), # PES - Pessimistisch
    (106, 16), # POL - Politisch

    # A107: Elon Musk - "neural lace matters for symbiosis"
    (107, 10), # TR - Transhumanismus
    (107, 13), # OPT - Optimistisch
    (107, 17), # PHI - Philosophisch
    (107, 21), # HA - Handlungsbezug

    # A108: Elon Musk - "achieve symbiosis with AI, can choose"
    (108, 10), # TR - Transhumanismus
    (108, 13), # OPT - Optimistisch
    (108, 17), # PHI - Philosophisch
    (108, 4),  # ET - Ethik (choice)

    # A109: Elon Musk - "in one of these demos, I will"
    (109, 2),  # SB - Selbstbild
    (109, 10), # TR - Transhumanismus (Neuralink)
    (109, 13), # OPT - Optimistisch
    (109, 19), # ANE - Anekdotisch

    # A110: Elon Musk - "Stephen Hawking communicate faster"
    (110, 10), # TR - Transhumanismus
    (110, 13), # OPT - Optimistisch
    (110, 21), # HA - Handlungsbezug (goal)

    # A111: Elon Musk - "TruthGPT, maximum truth-seeking AI"
    (111, 4),  # ET - Ethik (truth)
    (111, 7),  # FO - Fortschritt
    (111, 13), # OPT - Optimistisch
    (111, 17), # PHI - Philosophisch
    (111, 2),  # SB - Selbstbild (I'm going to start)

    # A112: Elon Musk - "AI understanding universe unlikely to annihilate"
    (112, 6),  # RI - Risiko (Umkehrung)
    (112, 13), # OPT - Optimistisch
    (112, 17), # PHI - Philosophisch
    (112, 12), # SP/EX - Spiritualität/Existenzielles

    # A113: Elon Musk - "safety regulated, AI power good and evil"
    (113, 11), # RE - Regulierung
    (113, 6),  # RI - Risiko
    (113, 15), # AMB - Ambivalent
    (113, 16), # POL - Politisch

    # A114: Elon Musk - "important to have referee"
    (114, 11), # RE - Regulierung
    (114, 13), # OPT - Optimistisch
    (114, 16), # POL - Politisch

    # A115: Elon Musk - "some chance AI will kill us all"
    (115, 6),  # RI - Risiko
    (115, 14), # PES - Pessimistisch
    (115, 22), # EP - Epistemik (probabilistisch)

    # A116: Elon Musk - "important for future of civilization"
    (116, 1),  # WV - Weltvision
    (116, 13), # OPT - Optimistisch
    (116, 17), # PHI - Philosophisch

    # A117: Elon Musk - "AI smarter than all humans combined by 2029"
    (117, 7),  # FO - Fortschritt
    (117, 3),  # MB - Menschenbild (Vergleich)
    (117, 15), # AMB - Ambivalent
    (117, 24), # ZP - Zeitprognose

    # A118: Elon Musk - "What is consciousness?"
    (118, 12), # SP/EX - Spiritualität/Existenzielles
    (118, 3),  # MB - Menschenbild
    (118, 15), # AMB - Ambivalent
    (118, 17), # PHI - Philosophisch

    # A119: Elon Musk - "We have entered the Singularity"
    (119, 1),  # WV - Weltvision
    (119, 7),  # FO - Fortschritt
    (119, 15), # AMB - Ambivalent
    (119, 20), # PRO - Provokant
    (119, 24), # ZP - Zeitprognose

    # A120: Elon Musk - "most economically compelling place for AI is space"
    (120, 9),  # AR - Arbeit/Wirtschaft
    (120, 1),  # WV - Weltvision (space)
    (120, 13), # OPT - Optimistisch
    (120, 24), # ZP - Zeitprognose

    # A121: Elon Musk - "even if bad, I want to be there to see it"
    (121, 2),  # SB - Selbstbild
    (121, 15), # AMB - Ambivalent
    (121, 20), # PRO - Provokant
    (121, 12), # SP/EX - Spiritualität/Existenzielles

    # A122: Elon Musk - "Grok 4 better than PhD level every subject"
    (122, 7),  # FO - Fortschritt
    (122, 13), # OPT - Optimistisch
    (122, 2),  # SB - Selbstbild (eigenes Produkt)
    (122, 20), # PRO - Provokant

    # A123: Elon Musk - "notion of human economy will seem quaint"
    (123, 1),  # WV - Weltvision
    (123, 9),  # AR - Arbeit/Wirtschaft
    (123, 15), # AMB - Ambivalent
    (123, 24), # ZP - Zeitprognose
    (123, 17), # PHI - Philosophisch

    # A124: Elon Musk - "10-20% chance it goes bad"
    (124, 6),  # RI - Risiko
    (124, 14), # PES - Pessimistisch
    (124, 22), # EP - Epistemik (probabilistisch)

    # A125: Elon Musk - "multi-planet species"
    (125, 1),  # WV - Weltvision
    (125, 6),  # RI - Risiko (survival)
    (125, 13), # OPT - Optimistisch
    (125, 21), # HA - Handlungsbezug

    # A126: Elon Musk - "I was assiduously manipulated and deceived"
    (126, 2),  # SB - Selbstbild
    (126, 8),  # MA - Macht (Opfer von Manipulation)
    (126, 14), # PES - Pessimistisch
    (126, 25), # BIO - Biographische Legitimation

    # A127: Elon Musk - "spinal cord injury, walk out couple days later"
    (127, 10), # TR - Transhumanismus
    (127, 13), # OPT - Optimistisch
    (127, 24), # ZP - Zeitprognose

    # A128: Mark Zuckerberg - "open source AI safer, more scrutiny"
    (128, 8),  # MA - Macht (open source)
    (128, 6),  # RI - Risiko (safer)
    (128, 13), # OPT - Optimistisch
    (128, 11), # RE - Regulierung (Governance-Modell)

    # A129: Mark Zuckerberg - "future so bright, massive prosperity"
    (129, 1),  # WV - Weltvision
    (129, 13), # OPT - Optimistisch
    (129, 17), # PHI - Philosophisch

    # A130: Mark Zuckerberg - "very good in one dimension, trade-offs"
    (130, 22), # EP - Epistemik (Reflexion)
    (130, 8),  # MA - Macht (open source vs proprietary)
    (130, 15), # AMB - Ambivalent
    (130, 26), # STR - Strategisch

    # A131: Mark Zuckerberg - "don't have crystal ball, hard to predict"
    (131, 22), # EP - Epistemik (Unsicherheit)
    (131, 7),  # FO - Fortschritt
    (131, 15), # AMB - Ambivalent
    (131, 24), # ZP - Zeitprognose

    # A132: Mark Zuckerberg - "AI help reason, code, be creative"
    (132, 7),  # FO - Fortschritt
    (132, 13), # OPT - Optimistisch
    (132, 24), # ZP - Zeitprognose

    # A133: Mark Zuckerberg - "too eager to please government, more outspoken"
    (133, 11), # RE - Regulierung
    (133, 8),  # MA - Macht (Verhältnis zu Regierung)
    (133, 14), # PES - Pessimistisch
    (133, 25), # BIO - Biographische Legitimation
    (133, 16), # POL - Politisch

    # A134: Mark Zuckerberg - "I'm sorry for everything you've been through"
    (134, 2),  # SB - Selbstbild
    (134, 4),  # ET - Ethik (Entschuldigung)
    (134, 14), # PES - Pessimistisch
    (134, 19), # ANE - Anekdotisch

    # A135: Mark Zuckerberg - "$5 billion safety and security"
    (135, 6),  # RI - Risiko (safety)
    (135, 9),  # AR - Arbeit/Wirtschaft (Investitionen)
    (135, 13), # OPT - Optimistisch
    (135, 2),  # SB - Selbstbild (Meta)

    # A136: Mark Zuckerberg - "make Meta better, financial performance"
    (136, 9),  # AR - Arbeit/Wirtschaft
    (136, 2),  # SB - Selbstbild (Meta)
    (136, 13), # OPT - Optimistisch
    (136, 26), # STR - Strategisch

    # A137: Mark Zuckerberg - "flatten organization, strong leaders"
    (137, 9),  # AR - Arbeit/Wirtschaft (Organisationsstruktur)
    (137, 2),  # SB - Selbstbild
    (137, 13), # OPT - Optimistisch
    (137, 26), # STR - Strategisch

    # A138: Mark Zuckerberg - "embodied internet, metaverse"
    (138, 1),  # WV - Weltvision
    (138, 7),  # FO - Fortschritt
    (138, 13), # OPT - Optimistisch
    (138, 17), # PHI - Philosophisch

    # A139: Mark Zuckerberg - "feeling of presence, right there with another"
    (139, 1),  # WV - Weltvision
    (139, 3),  # MB - Menschenbild (soziale Präsenz)
    (139, 13), # OPT - Optimistisch
    (139, 17), # PHI - Philosophisch

    # A140: Mark Zuckerberg - "first frontier-level open source AI model"
    (140, 8),  # MA - Macht (open source)
    (140, 7),  # FO - Fortschritt
    (140, 13), # OPT - Optimistisch
    (140, 2),  # SB - Selbstbild (Meta)

    # A141: Mark Zuckerberg - "600 million monthly actives, most widely-used"
    (141, 9),  # AR - Arbeit/Wirtschaft
    (141, 13), # OPT - Optimistisch
    (141, 2),  # SB - Selbstbild (Meta AI)
    (141, 24), # ZP - Zeitprognose

    # A142: Mark Zuckerberg - "superintelligence in sight"
    (142, 7),  # FO - Fortschritt
    (142, 13), # OPT - Optimistisch
    (142, 2),  # SB - Selbstbild (Meta)
    (142, 24), # ZP - Zeitprognose

    # A143: Mark Zuckerberg - "smart glasses primary computing devices"
    (143, 7),  # FO - Fortschritt
    (143, 1),  # WV - Weltvision
    (143, 13), # OPT - Optimistisch
    (143, 24), # ZP - Zeitprognose

    # A144: Mark Zuckerberg - "Meta Compute infrastructure for superintelligence"
    (144, 9),  # AR - Arbeit/Wirtschaft (Infrastruktur)
    (144, 13), # OPT - Optimistisch
    (144, 2),  # SB - Selbstbild (Meta)
    (144, 26), # STR - Strategisch

    # A145: Mark Zuckerberg - "$60 billion into AI, datacenter size of Manhattan"
    (145, 9),  # AR - Arbeit/Wirtschaft (Investitionen)
    (145, 13), # OPT - Optimistisch
    (145, 2),  # SB - Selbstbild
    (145, 18), # EMP - Empirisch

    # A146: Mark Zuckerberg - "public conversations app 1 billion+"
    (146, 9),  # AR - Arbeit/Wirtschaft (business strategy)
    (146, 5),  # GE - Gesellschaft (public conversations)
    (146, 13), # OPT - Optimistisch
    (146, 26), # STR - Strategisch

    # A147: Mark Zuckerberg - "cure, prevent, manage all diseases by end of century"
    (147, 1),  # WV - Weltvision
    (147, 13), # OPT - Optimistisch
    (147, 24), # ZP - Zeitprognose
    (147, 2),  # SB - Selbstbild (CZI mission)
    (147, 21), # HA - Handlungsbezug

    # A148: Mark Zuckerberg - "CZI into AI-powered biomedical research"
    (148, 7),  # FO - Fortschritt (Medizin)
    (148, 13), # OPT - Optimistisch
    (148, 2),  # SB - Selbstbild (CZI)
    (148, 26), # STR - Strategisch

    # A149: Mark Zuckerberg - "Llama 1 billion downloads, open source winning"
    (149, 8),  # MA - Macht (open source)
    (149, 13), # OPT - Optimistisch
    (149, 2),  # SB - Selbstbild (Meta)
    (149, 18), # EMP - Empirisch

    # A150: Mark Zuckerberg - "likely won't open source all, too powerful"
    (150, 8),  # MA - Macht (open source Grenzen)
    (150, 6),  # RI - Risiko (too powerful)
    (150, 15), # AMB - Ambivalent
    (150, 22), # EP - Epistemik (Reflexion)
    (150, 23), # KON - Kongruenz/Widerspruch

    # A151: Mark Zuckerberg - "personal superintelligence for everyone"
    (151, 1),  # WV - Weltvision
    (151, 5),  # GE - Gesellschaft (for everyone)
    (151, 13), # OPT - Optimistisch
    (151, 4),  # ET - Ethik (power in people's hands)
    (151, 2),  # SB - Selbstbild (Meta's vision)

    # A417: Larry Page - "toothbrush test"
    (152, 9),  # AR - Arbeit/Wirtschaft (Produktstrategie)
    (152, 13), # OPT - Optimistisch
    (152, 26), # STR - Strategisch
    (152, 2),  # SB - Selbstbild (Google)

    # A418: Larry Page - "people afraid of new technology, not adapting fast"
    (153, 22), # EP - Epistemik (Menschen verstehen nicht)
    (153, 7),  # FO - Fortschritt (pace of change)
    (153, 14), # PES - Pessimistisch
    (153, 5),  # GE - Gesellschaft
    (153, 21), # HA - Handlungsbezug

    # A419: Larry Page - "ultimate version of Google, AI understand everything"
    (154, 7),  # FO - Fortschritt
    (154, 1),  # WV - Weltvision
    (154, 13), # OPT - Optimistisch
    (154, 2),  # SB - Selbstbild (Google)

    # A420: Larry Page - "build better search engine"
    (155, 7),  # FO - Fortschritt
    (155, 13), # OPT - Optimistisch
    (155, 2),  # SB - Selbstbild (Google)
    (155, 25), # BIO - Biographische Legitimation

    # A421: Larry Page - "negativity is not realism, amazing positive people"
    (156, 22), # EP - Epistemik (Weltwahrnehmung)
    (156, 3),  # MB - Menschenbild (Menschen tun Gutes)
    (156, 13), # OPT - Optimistisch
    (156, 17), # PHI - Philosophisch

    # A422: Larry Page - "aim for radical, transformative, powerful"
    (157, 7),  # FO - Fortschritt
    (157, 13), # OPT - Optimistisch
    (157, 21), # HA - Handlungsbezug
    (157, 17), # PHI - Philosophisch

    # A423: Larry Page - "people able should solve biggest problems"
    (158, 5),  # GE - Gesellschaft (Verantwortung der Fähigen)
    (158, 4),  # ET - Ethik
    (158, 14), # PES - Pessimistisch
    (158, 17), # PHI - Philosophisch

    # A424: Larry Page - "would like to die working"
    (159, 2),  # SB - Selbstbild
    (159, 13), # OPT - Optimistisch
    (159, 19), # ANE - Anekdotisch
    (159, 17), # PHI - Philosophisch

    # A425: Larry Page - "give money to Elon not charity, entrepreneurs solve problems"
    (160, 4),  # ET - Ethik (Philanthrophie)
    (160, 9),  # AR - Arbeit/Wirtschaft (Unternehmer)
    (160, 13), # OPT - Optimistisch
    (160, 20), # PRO - Provokant
    (160, 17), # PHI - Philosophisch

    # A426: Larry Page - "slavishly work inefficiently doesn't make sense"
    (161, 9),  # AR - Arbeit/Wirtschaft
    (161, 5),  # GE - Gesellschaft (Arbeitsorganisation)
    (161, 13), # OPT - Optimistisch
    (161, 17), # PHI - Philosophisch

    # A427: Larry Page - "people like working, but also want time with family"
    (162, 9),  # AR - Arbeit/Wirtschaft
    (162, 3),  # MB - Menschenbild
    (162, 13), # OPT - Optimistisch
    (162, 21), # HA - Handlungsbezug

    # A428: Larry Page - "changing world, excited to get up"
    (163, 7),  # FO - Fortschritt
    (163, 2),  # SB - Selbstbild
    (163, 13), # OPT - Optimistisch
    (163, 17), # PHI - Philosophisch

    # A429: Larry Page - "tremendous trust, protecting data and privacy"
    (164, 4),  # ET - Ethik (privacy)
    (164, 8),  # MA - Macht (Datenkontrolle)
    (164, 13), # OPT - Optimistisch
    (164, 2),  # SB - Selbstbild (Google)

    # A430: Larry Page - "regulation doesn't work, pace too rapid"
    (165, 11), # RE - Regulierung (kritisch)
    (165, 7),  # FO - Fortschritt (pace of change)
    (165, 14), # PES - Pessimistisch
    (165, 16), # POL - Politisch

    # A431: Larry Page - "we need revolution, not evolution"
    (166, 7),  # FO - Fortschritt
    (166, 13), # OPT - Optimistisch
    (166, 20), # PRO - Provokant
    (166, 17), # PHI - Philosophisch

    # A432: Larry Page - "automate cars, save lives, people dying daily"
    (167, 7),  # FO - Fortschritt
    (167, 6),  # RI - Risiko (Unfälle)
    (167, 13), # OPT - Optimistisch
    (167, 21), # HA - Handlungsbezug

    # A433: Larry Page - "if not doing crazy things, doing wrong things"
    (168, 7),  # FO - Fortschritt
    (168, 13), # OPT - Optimistisch
    (168, 17), # PHI - Philosophisch
    (168, 20), # PRO - Provokant

    # A434: Sergey Brin - "solve search, solve world's problems, fundamental right"
    (169, 7),  # FO - Fortschritt
    (169, 5),  # GE - Gesellschaft (fundamental right)
    (169, 13), # OPT - Optimistisch
    (169, 4),  # ET - Ethik (human right)
    (169, 17), # PHI - Philosophisch

    # A435: Sergey Brin - "technology inherent democratizer"
    (170, 7),  # FO - Fortschritt
    (170, 5),  # GE - Gesellschaft (Demokratisierung)
    (170, 13), # OPT - Optimistisch
    (170, 8),  # MA - Macht (Umverteilung von Macht)
    (170, 17), # PHI - Philosophisch

    # A436: Sergey Brin - "technology everybody loves, use twice a day"
    (171, 7),  # FO - Fortschritt
    (171, 13), # OPT - Optimistisch
    (171, 2),  # SB - Selbstbild (Google)
    (171, 26), # STR - Strategisch

    # A437: Sergey Brin - "Don't be evil, stay on right side"
    (172, 4),  # ET - Ethik
    (172, 2),  # SB - Selbstbild (Google)
    (172, 13), # OPT - Optimistisch
    (172, 17), # PHI - Philosophisch

    # A438: Sergey Brin - "information universally accessible, come to me"
    (173, 5),  # GE - Gesellschaft (universal access)
    (173, 7),  # FO - Fortschritt
    (173, 13), # OPT - Optimistisch
    (173, 1),  # WV - Weltvision

    # A439: Sergey Brin - "phone emasculating, socially isolating"
    (174, 3),  # MB - Menschenbild
    (174, 5),  # GE - Gesellschaft (soziale Isolation)
    (174, 14), # PES - Pessimistisch
    (174, 17), # PHI - Philosophisch
    (174, 15), # AMB - Ambivalent (glass half full/empty)

    # A440: Sergey Brin - "save million lives with self-driving cars"
    (175, 7),  # FO - Fortschritt
    (175, 6),  # RI - Risiko (Unfälle)
    (175, 13), # OPT - Optimistisch
    (175, 18), # EMP - Empirisch
    (175, 21), # HA - Handlungsbezug

    # A441: Sergey Brin - "predisposed to Parkinson's, opportunity to adjust"
    (176, 2),  # SB - Selbstbild
    (176, 13), # OPT - Optimistisch
    (176, 25), # BIO - Biographische Legitimation
    (176, 21), # HA - Handlungsbezug

    # A442: Sergey Brin - "able to make difference, but constantly re-evaluating"
    (177, 8),  # MA - Macht (Einfluss in China)
    (177, 4),  # ET - Ethik
    (177, 15), # AMB - Ambivalent
    (177, 16), # POL - Politisch
    (177, 22), # EP - Epistemik (re-evaluating)

    # A443: Sergey Brin - "troubled by China, Soviet Union childhood"
    (178, 8),  # MA - Macht (Totalitarismus)
    (178, 16), # POL - Politisch
    (178, 14), # PES - Pessimistisch
    (178, 2),  # SB - Selbstbild
    (178, 25), # BIO - Biographische Legitimation

    # A444: Sergey Brin - "moonshot-style, millions affected"
    (179, 7),  # FO - Fortschritt
    (179, 13), # OPT - Optimistisch
    (179, 5),  # GE - Gesellschaft (millions affected)
    (179, 26), # STR - Strategisch

    # A445: Sergey Brin - "supporting medical research, Parkinson's, poverty, education"
    (180, 5),  # GE - Gesellschaft (Bildung, Armut)
    (180, 13), # OPT - Optimistisch
    (180, 2),  # SB - Selbstbild
    (180, 21), # HA - Handlungsbezug
    (180, 25), # BIO - Biographische Legitimation

    # A446: Sergey Brin - "coming in most days, exciting progress"
    (181, 2),  # SB - Selbstbild
    (181, 7),  # FO - Fortschritt
    (181, 13), # OPT - Optimistisch
    (181, 19), # ANE - Anekdotisch

    # A447: Sergey Brin - "organize world's information, PageRank"
    (182, 7),  # FO - Fortschritt
    (182, 5),  # GE - Gesellschaft (universal access)
    (182, 13), # OPT - Optimistisch
    (182, 2),  # SB - Selbstbild (Google)
    (182, 25), # BIO - Biographische Legitimation

    # A448: Sergey Brin - "not failure if you learn something"
    (183, 22), # EP - Epistemik (Lernen)
    (183, 13), # OPT - Optimistisch
    (183, 17), # PHI - Philosophisch

    # A449: Sergey Brin - "lighter-than-air vehicles, solving real-world problems"
    (184, 7),  # FO - Fortschritt
    (184, 13), # OPT - Optimistisch
    (184, 21), # HA - Handlungsbezug

    # A450: Sergey Brin - "more worried, threat to freedom of Internet"
    (185, 8),  # MA - Macht (Bedrohung)
    (185, 5),  # GE - Gesellschaft (open Internet)
    (185, 14), # PES - Pessimistisch
    (185, 16), # POL - Politisch
    (185, 6),  # RI - Risiko

    # A451: Jeff Bezos - "Day 1 for Internet, personalization accelerate discovery"
    (186, 9),  # AR - Arbeit/Wirtschaft (Amazon)
    (186, 7),  # FO - Fortschritt
    (186, 13), # OPT - Optimistisch
    (186, 25), # BIO - Biographische Legitimation
    (186, 2),  # SB - Selbstbild

    # A452: Jeff Bezos - "shareholder value long term"
    (187, 9),  # AR - Arbeit/Wirtschaft
    (187, 13), # OPT - Optimistisch
    (187, 26), # STR - Strategisch

    # A453: Jeff Bezos - "Day 2 is death, always Day 1"
    (188, 9),  # AR - Arbeit/Wirtschaft (business philosophy)
    (188, 14), # PES - Pessimistisch (Day 2)
    (188, 17), # PHI - Philosophisch
    (188, 2),  # SB - Selbstbild

    # A454: Jeff Bezos - "obsessive customer focus most protective"
    (189, 9),  # AR - Arbeit/Wirtschaft
    (189, 13), # OPT - Optimistisch
    (189, 26), # STR - Strategisch
    (189, 17), # PHI - Philosophisch

    # A455: Jeff Bezos - "tendency to manage to proxies, dangerous"
    (190, 9),  # AR - Arbeit/Wirtschaft
    (190, 14), # PES - Pessimistisch
    (190, 22), # EP - Epistemik (Kritik)
    (190, 17), # PHI - Philosophisch

    # A456: Jeff Bezos - "high-quality high-velocity decisions"
    (191, 9),  # AR - Arbeit/Wirtschaft
    (191, 13), # OPT - Optimistisch
    (191, 26), # STR - Strategisch

    # A457: Jeff Bezos - "conviction despite not perfect information"
    (192, 22), # EP - Epistemik (Unsicherheit)
    (192, 9),  # AR - Arbeit/Wirtschaft
    (192, 13), # OPT - Optimistisch
    (192, 26), # STR - Strategisch

    # A458: Jeff Bezos - "size of failures must grow"
    (193, 9),  # AR - Arbeit/Wirtschaft
    (193, 13), # OPT - Optimistisch
    (193, 17), # PHI - Philosophisch
    (193, 26), # STR - Strategisch

    # A459: Jeff Bezos - "machine learning quiet but pervasive impact"
    (194, 7),  # FO - Fortschritt
    (194, 9),  # AR - Arbeit/Wirtschaft (Amazon)
    (194, 13), # OPT - Optimistisch
    (194, 18), # EMP - Empirisch

    # A460: Jeff Bezos - "Alexa sophisticated AI, have conversation"
    (195, 7),  # FO - Fortschritt
    (195, 13), # OPT - Optimistisch
    (195, 2),  # SB - Selbstbild (Amazon)

    # A461: Jeff Bezos - "solar system support trillion humans"
    (196, 1),  # WV - Weltvision
    (196, 13), # OPT - Optimistisch
    (196, 17), # PHI - Philosophisch
    (196, 24), # ZP - Zeitprognose

    # A462: Jeff Bezos - "zone Earth residential, heavy industry to space"
    (197, 1),  # WV - Weltvision
    (197, 13), # OPT - Optimistisch
    (197, 6),  # RI - Risiko (Umwelt)
    (197, 21), # HA - Handlungsbezug

    # A463: Jeff Bezos - "go to space to save Earth, not escape"
    (198, 1),  # WV - Weltvision
    (198, 4),  # ET - Ethik (purpose)
    (198, 13), # OPT - Optimistisch
    (198, 2),  # SB - Selbstbild (Blue Origin)
    (198, 17), # PHI - Philosophisch

    # A464: Jeff Bezos - "minimize regrets, not regret trying Internet"
    (199, 2),  # SB - Selbstbild
    (199, 13), # OPT - Optimistisch
    (199, 25), # BIO - Biographische Legitimation
    (199, 17), # PHI - Philosophisch

    # A465: Jeff Bezos - "two-pizza team rule"
    (200, 9),  # AR - Arbeit/Wirtschaft
    (200, 13), # OPT - Optimistisch
    (200, 26), # STR - Strategisch

    # A466: Jeff Bezos - "AI best tool, mostly for good, not Terminator"
    (201, 7),  # FO - Fortschritt
    (201, 13), # OPT - Optimistisch
    (201, 6),  # RI - Risiko (Terminator negiert)
    (201, 17), # PHI - Philosophisch

    # A467: Jeff Bezos - "values do not need changing, duty to readers"
    (202, 4),  # ET - Ethik
    (202, 13), # OPT - Optimistisch
    (202, 2),  # SB - Selbstbild (Washington Post)

    # A468: Jeff Bezos - "climate change biggest threat"
    (203, 6),  # RI - Risiko
    (203, 1),  # WV - Weltvision
    (203, 14), # PES - Pessimistisch
    (203, 21), # HA - Handlungsbezug

    # A469: Jeff Bezos - "LLMs powerful but not lead to AGI"
    (204, 7),  # FO - Fortschritt
    (204, 22), # EP - Epistemik (Skepsis)
    (204, 15), # AMB - Ambivalent

    # A470: Jeff Bezos - "AWS started as own best customer"
    (205, 9),  # AR - Arbeit/Wirtschaft
    (205, 13), # OPT - Optimistisch
    (205, 25), # BIO - Biographische Legitimation
    (205, 2),  # SB - Selbstbild (Amazon)

    # A471: Jeff Bezos - "create more than consume"
    (206, 4),  # ET - Ethik
    (206, 13), # OPT - Optimistisch
    (206, 17), # PHI - Philosophisch
    (206, 9),  # AR - Arbeit/Wirtschaft

    # A472: Jeff Bezos - "willing to be misunderstood, long-term oriented"
    (207, 9),  # AR - Arbeit/Wirtschaft
    (207, 13), # OPT - Optimistisch
    (207, 26), # STR - Strategisch
    (207, 2),  # SB - Selbstbild

    # A936: Larry Ellison - "AI changes everything, bigger than industrial revolution"
    (208, 1),  # WV - Weltvision
    (208, 7),  # FO - Fortschritt
    (208, 13), # OPT - Optimistisch
    (208, 20), # PRO - Provokant
    (208, 18), # EMP - Empirisch

    # A937: Larry Ellison - "police supervised, citizens best behavior, recording everything"
    (209, 8),  # MA - Macht (Überwachung)
    (209, 6),  # RI - Risiko (Freiheit)
    (209, 13), # OPT - Optimistisch (aus seiner Sicht)
    (209, 16), # POL - Politisch
    (209, 20), # PRO - Provokant

    # A938: Larry Ellison - "AI help solve problems, make us better, not replace"
    (210, 7),  # FO - Fortschritt
    (210, 3),  # MB - Menschenbild
    (210, 13), # OPT - Optimistisch
    (210, 9),  # AR - Arbeit/Wirtschaft

    # A939: Larry Ellison - "begging Jensen for GPUs, take our money"
    (211, 9),  # AR - Arbeit/Wirtschaft
    (211, 13), # OPT - Optimistisch
    (211, 19), # ANE - Anekdotisch
    (211, 2),  # SB - Selbstbild
    (211, 20), # PRO - Provokant

    # A940: Larry Ellison - "AI design cancer vaccine in 48 hours"
    (212, 7),  # FO - Fortschritt
    (212, 13), # OPT - Optimistisch
    (212, 18), # EMP - Empirisch
    (212, 24), # ZP - Zeitprognose

    # A941: Larry Ellison - "single blood test, AI early cancer detection"
    (213, 7),  # FO - Fortschritt
    (213, 13), # OPT - Optimistisch
    (213, 18), # EMP - Empirisch

    # A942: Larry Ellison - "reasoning on private corporate data bigger market"
    (214, 9),  # AR - Arbeit/Wirtschaft
    (214, 13), # OPT - Optimistisch
    (214, 26), # STR - Strategisch
    (214, 2),  # SB - Selbstbild (Oracle)

    # A943: Larry Ellison - "Oracle gigawatt-scale datacenters faster cost-efficient"
    (215, 9),  # AR - Arbeit/Wirtschaft
    (215, 13), # OPT - Optimistisch
    (215, 2),  # SB - Selbstbild (Oracle)
    (215, 18), # EMP - Empirisch

    # A944: Larry Ellison - "trained with public data, future in private enterprise data"
    (216, 9),  # AR - Arbeit/Wirtschaft
    (216, 13), # OPT - Optimistisch
    (216, 26), # STR - Strategisch

    # A945: Larry Ellison - "Oxford modify wheat, 20% more grain, AI photosynthesis"
    (217, 7),  # FO - Fortschritt
    (217, 13), # OPT - Optimistisch
    (217, 18), # EMP - Empirisch
    (217, 5),  # GE - Gesellschaft (Ernährung)

    # A946: Larry Ellison - "trillion-dollar capital cycle, bigger than railroads"
    (218, 9),  # AR - Arbeit/Wirtschaft
    (218, 13), # OPT - Optimistisch
    (218, 18), # EMP - Empirisch
    (218, 20), # PRO - Provokant

    # A947: Larry Ellison - "US can't let China win competition"
    (219, 8),  # MA - Macht (geopolitisch)
    (219, 16), # POL - Politisch
    (219, 14), # PES - Pessimistisch
    (219, 26), # STR - Strategisch

    # A948: Larry Ellison - "Lanai environmental sustainability, $500 million"
    (220, 6),  # RI - Risiko (Umwelt)
    (220, 13), # OPT - Optimistisch
    (220, 2),  # SB - Selbstbild
    (220, 21), # HA - Handlungsbezug

    # A949: Larry Ellison - "Oracle solving multistep reasoning on private data"
    (221, 9),  # AR - Arbeit/Wirtschaft
    (221, 7),  # FO - Fortschritt
    (221, 13), # OPT - Optimistisch
    (221, 2),  # SB - Selbstbild (Oracle)
    (221, 26), # STR - Strategisch

    # A950: Larry Ellison - "Elon, Mark, Sam smartest engineers in AI"
    (222, 2),  # SB - Selbstbild (Bewunderung)
    (222, 7),  # FO - Fortschritt
    (222, 13), # OPT - Optimistisch

    # A951: Larry Ellison - "US and countries need to unify national data for AI"
    (223, 8),  # MA - Macht (Datenzentralisierung)
    (223, 16), # POL - Politisch
    (223, 13), # OPT - Optimistisch
    (223, 21), # HA - Handlungsbezug
    (223, 20), # PRO - Provokant

    # A952: Larry Ellison - "Stargate expand to 20 datacenters, largest AI infrastructure"
    (224, 9),  # AR - Arbeit/Wirtschaft
    (224, 13), # OPT - Optimistisch
    (224, 18), # EMP - Empirisch
    (224, 2),  # SB - Selbstbild
]

# Einfügen in Datenbank
c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()

print(f"Eingefuegt: {len(codes)} Kodierungen fuer Aussagen P1-P10")

# Statistik
c.execute("SELECT COUNT(*) FROM aussagen_kategorien")
print(f"Gesamt in DB: {c.fetchone()[0]}")

# Überprüfung: Wie viele Aussagen haben Kodierungen?
c.execute("""
SELECT COUNT(DISTINCT aussage_id)
FROM aussagen_kategorien
WHERE aussage_id BETWEEN 1 AND 224
""")
print(f"Anzahl kodierter Aussagen (P1-P10): {c.fetchone()[0]} von 224")

# Durchschnittliche Anzahl Kategorien pro Aussage
c.execute("""
SELECT AVG(cnt) FROM (
    SELECT COUNT(*) as cnt
    FROM aussagen_kategorien
    WHERE aussage_id BETWEEN 1 AND 224
    GROUP BY aussage_id
)
""")
print(f"Durchschnittliche Kategorien pro Aussage: {c.fetchone()[0]:.2f}")

conn.close()
print("\nKodierung abgeschlossen!")
