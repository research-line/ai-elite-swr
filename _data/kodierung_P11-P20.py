import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

codes = [
    # P11 - Demis Hassabis (A152-A175)
    (152, 24), (152, 1), (152, 13),  # AGI before 2030 - Zeitprognose, Weltvision, Optimistisch
    (153, 1), (153, 13), (153, 24),  # AGI most transformative - Weltvision, Optimistisch, Zeitprognose
    (154, 7), (154, 13), (154, 1),   # 10x bigger than Industrial Revolution - Fortschritt, Optimistisch, Weltvision
    (155, 7), (155, 13), (155, 4), (155, 21),  # AI beneficial if safe - Fortschritt, Optimistisch, Ethik, Handlungsbezug
    (156, 2), (156, 13), (156, 25),  # Nobel Prize - Selbstbild, Optimistisch, Biographische Legitimation
    (157, 7), (157, 13), (157, 18),  # AlphaFold2 cracked challenge - Fortschritt, Optimistisch, Empirisch
    (158, 24), (158, 1), (158, 13),  # AGI in 5 years - Zeitprognose, Weltvision, Optimistisch
    (159, 6), (159, 14), (159, 8),   # AI race makes unsafe - Risiko, Pessimistisch, Macht
    (160, 11), (160, 13), (160, 21), (160, 26),  # Smart adaptable regulation - Regulierung, Optimistisch, Handlungsbezug, Strategisch
    (161, 6), (161, 14), (161, 16),  # Extinction risk priority - Risiko, Pessimistisch, Politisch
    (162, 6), (162, 14), (162, 22),  # Bad actors question - Risiko, Pessimistisch, Epistemik
    (163, 3), (163, 17), (163, 22),  # Consciousness definition - Menschenbild, Philosophisch, Epistemik
    (164, 12), (164, 13), (164, 17),  # Waking up universe - Spiritualität/Existenzielles, Optimistisch, Philosophisch
    (165, 2), (165, 12), (165, 17),  # Underlying motivation - Selbstbild, Spiritualität/Existenzielles, Philosophisch
    (166, 3), (166, 18), (166, 13),  # Brain is classical computing - Menschenbild, Empirisch, Optimistisch
    (167, 7), (167, 13), (167, 18),  # AlphaProteo announcement - Fortschritt, Optimistisch, Empirisch
    (168, 1), (168, 13), (168, 24),  # New renaissance - Weltvision, Optimistisch, Zeitprognose
    (169, 7), (169, 13), (169, 17),  # AlphaZero alien play - Fortschritt, Optimistisch, Philosophisch
    (170, 7), (170, 13), (170, 26),  # Energy/intelligence equation - Fortschritt, Optimistisch, Strategisch
    (171, 7), (171, 13), (171, 21),  # Room temp superconductor - Fortschritt, Optimistisch, Handlungsbezug
    (172, 1), (172, 13), (172, 12),  # AGI new explanations - Weltvision, Optimistisch, Spiritualität/Existenzielles
    (173, 7), (173, 18), (173, 13),  # World Models crucial - Fortschritt, Empirisch, Optimistisch
    (174, 12), (174, 13), (174, 17),  # Science enhances beauty - Spiritualität/Existenzielles, Optimistisch, Philosophisch
    (175, 2), (175, 25), (175, 13),  # Chess master at 13 - Selbstbild, Biographische Legitimation, Optimistisch

    # P12 - Ilya Sutskever (A201-A223)
    (201, 2), (201, 14), (201, 19),  # Regret board actions - Selbstbild, Pessimistisch, Anekdotisch
    (202, 22), (202, 14), (202, 19),  # Process was rushed - Epistemik, Pessimistisch, Anekdotisch
    (203, 22), (203, 14), (203, 19),  # Didn't expect strong feelings - Epistemik, Pessimistisch, Anekdotisch
    (204, 2), (204, 14), (204, 19),  # Unhappy about merger - Selbstbild, Pessimistisch, Anekdotisch
    (205, 7), (205, 14), (205, 18),  # Pre-training will end - Fortschritt, Pessimistisch, Empirisch
    (206, 22), (206, 14), (206, 18),  # Data is finite - Epistemik, Pessimistisch, Empirisch
    (207, 1), (207, 13), (207, 24),  # Superintelligent AI coming - Weltvision, Optimistisch, Zeitprognose
    (208, 24), (208, 15), (208, 22),  # 5-20 years - Zeitprognose, Ambivalent, Epistemik
    (209, 7), (209, 14), (209, 22),  # Current approaches will peter out - Fortschritt, Pessimistisch, Epistemik
    (210, 7), (210, 15), (210, 18),  # Generalization is frontier - Fortschritt, Ambivalent, Empirisch
    (211, 1), (211, 13), (211, 17),  # AGI as superintelligent learner - Weltvision, Optimistisch, Philosophisch
    (212, 7), (212, 18), (212, 13),  # Compressors become predictors - Fortschritt, Empirisch, Optimistisch
    (213, 3), (213, 18), (213, 17),  # Consciousness test - Menschenbild, Empirisch, Philosophisch
    (214, 3), (214, 22), (214, 17),  # Psychology language for NNs - Menschenbild, Epistemik, Philosophisch
    (215, 9), (215, 13), (215, 26),  # First product safe superintelligence - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (216, 7), (216, 13), (216, 18),  # RLHF to stop hallucination - Fortschritt, Optimistisch, Empirisch
    (217, 7), (217, 15), (217, 24),  # Age of research/scaling - Fortschritt, Ambivalent, Zeitprognose
    (218, 2), (218, 13), (218, 19),  # Feel the AGI - Selbstbild, Optimistisch, Anekdotisch
    (219, 2), (219, 13), (219, 25),  # Personally meaningful - Selbstbild, Optimistisch, Biographische Legitimation
    (220, 6), (220, 14), (220, 2),   # Before/after, self-interest - Risiko, Pessimistisch, Selbstbild
    (221, 2), (221, 13), (221, 25),  # Big new vision - Selbstbild, Optimistisch, Biographische Legitimation
    (222, 7), (222, 15), (222, 18),  # What we got right/wrong - Fortschritt, Ambivalent, Empirisch
    (223, 7), (223, 18), (223, 17),  # Kolmogorov complexity - Fortschritt, Empirisch, Philosophisch

    # P13 - Yann LeCun (A247-A272)
    (247, 6), (247, 14), (247, 20),  # P(doom) is BS - Risiko, Pessimistisch, Provokant
    (248, 6), (248, 14), (248, 20),  # AI threat is BS - Risiko, Pessimistisch, Provokant
    (249, 7), (249, 14), (249, 18),  # LLMs can't plan - Fortschritt, Pessimistisch, Empirisch
    (250, 7), (250, 14), (250, 18),  # LLMs don't understand physical world - Fortschritt, Pessimistisch, Empirisch
    (251, 5), (251, 13), (251, 16),  # No monopoly on ideas - Gesellschaft, Optimistisch, Politisch
    (252, 3), (252, 15), (252, 17),  # Human intelligence specialized - Menschenbild, Ambivalent, Philosophisch
    (253, 8), (253, 14), (253, 20),  # Doomer's Delusion - Macht, Pessimistisch, Provokant
    (254, 7), (254, 13), (254, 24),  # New paradigm 3-5 years - Fortschritt, Optimistisch, Zeitprognose
    (255, 7), (255, 14), (255, 18),  # Machine learning sucks - Fortschritt, Pessimistisch, Empirisch
    (256, 7), (256, 14), (256, 18),  # Don't understand like housecat - Fortschritt, Pessimistisch, Empirisch
    (257, 8), (257, 14), (257, 20),  # OpenAI premise wrong - Macht, Pessimistisch, Provokant
    (258, 8), (258, 13), (258, 16),  # WE design and build AI - Macht, Optimistisch, Politisch
    (259, 11), (259, 13), (259, 16),  # Regulate products not tech - Regulierung, Optimistisch, Politisch
    (260, 7), (260, 13), (260, 18),  # Deep learning definition - Fortschritt, Optimistisch, Empirisch
    (261, 2), (261, 15), (261, 19),  # Musk agreement/disagreement - Selbstbild, Ambivalent, Anekdotisch
    (262, 2), (262, 13), (262, 21),  # Leaving Meta for world models - Selbstbild, Optimistisch, Handlungsbezug
    (263, 7), (263, 14), (263, 20),  # LLM obsession wrong - Fortschritt, Pessimistisch, Provokant
    (264, 22), (264, 13), (264, 17),  # Advanced Machine Intelligence - Epistemik, Optimistisch, Philosophisch
    (265, 5), (265, 13), (265, 16),  # Secrecy hampers progress - Gesellschaft, Optimistisch, Politisch
    (266, 7), (266, 14), (266, 18),  # LLMs exponentially diverging - Fortschritt, Pessimistisch, Empirisch
    (267, 3), (267, 14), (267, 17),  # Intelligence vs autonomy - Menschenbild, Pessimistisch, Philosophisch
    (268, 22), (268, 14), (268, 20),  # False predictions - Epistemik, Pessimistisch, Provokant
    (269, 6), (269, 13), (269, 18),  # Turbojets made reliable - Risiko, Optimistisch, Empirisch
    (270, 11), (270, 13), (270, 16),  # EU AI Act kudos - Regulierung, Optimistisch, Politisch
    (271, 2), (271, 14), (271, 20),  # Join xAI sarcasm - Selbstbild, Pessimistisch, Provokant

    # P14 - Fei-Fei Li (A296-A319)
    (296, 7), (296, 13), (296, 18),  # Map entire world of objects - Fortschritt, Optimistisch, Empirisch
    (297, 7), (297, 13), (297, 18),  # Training data crucial insight - Fortschritt, Optimistisch, Empirisch
    (298, 5), (298, 13), (298, 16), (298, 21),  # AI too important for technologists alone - Gesellschaft, Optimistisch, Politisch, Handlungsbezug
    (299, 4), (299, 13), (299, 17),  # Human-centered AI - Ethik, Optimistisch, Philosophisch
    (300, 2), (300, 13), (300, 25),  # Arrived with $600 - Selbstbild, Optimistisch, Biographische Legitimation
    (301, 7), (301, 13), (301, 17),  # ImageNet as bet - Fortschritt, Optimistisch, Philosophisch
    (302, 7), (302, 13), (302, 18),  # ImageNet project description - Fortschritt, Optimistisch, Empirisch
    (303, 5), (303, 13), (303, 16),  # Diversity strengthens science - Gesellschaft, Optimistisch, Politisch
    (304, 6), (304, 14), (304, 4),   # Worry about AI without care - Risiko, Pessimistisch, Ethik
    (305, 7), (305, 13), (305, 17),  # Vision most information-rich - Fortschritt, Optimistisch, Philosophisch
    (306, 7), (306, 13), (306, 18),  # Spatial intelligence needed - Fortschritt, Optimistisch, Empirisch
    (307, 7), (307, 13), (307, 18),  # Building 3D world tech - Fortschritt, Optimistisch, Empirisch
    (308, 5), (308, 14), (308, 25),  # Often only woman in room - Gesellschaft, Pessimistisch, Biographische Legitimation
    (309, 5), (309, 13), (309, 4),   # AI4ALL for diversity - Gesellschaft, Optimistisch, Ethik
    (310, 7), (310, 13), (310, 4),   # AI healthcare full context - Fortschritt, Optimistisch, Ethik
    (311, 5), (311, 13), (311, 21),  # Democratize AI - Gesellschaft, Optimistisch, Handlungsbezug
    (312, 4), (312, 13), (312, 17),  # Algorithms embed values - Ethik, Optimistisch, Philosophisch
    (313, 4), (313, 13), (313, 17),  # Science is service - Ethik, Optimistisch, Philosophisch
    (314, 7), (314, 15), (314, 18),  # Datasets contain biases - Fortschritt, Ambivalent, Empirisch
    (315, 11), (315, 13), (315, 16),  # Smart regulation needed - Regulierung, Optimistisch, Politisch
    (316, 5), (316, 13), (316, 25),  # Teaching builds future - Gesellschaft, Optimistisch, Biographische Legitimation
    (317, 7), (317, 15), (317, 4),   # AI for climate but carbon footprint - Fortschritt, Ambivalent, Ethik
    (318, 2), (318, 13), (318, 25),  # Parents in dry cleaning - Selbstbild, Optimistisch, Biographische Legitimation
    (319, 7), (319, 13), (319, 24),  # Spatial intelligence future - Fortschritt, Optimistisch, Zeitprognose

    # P15 - Satya Nadella (A344-A367)
    (344, 2), (344, 4), (344, 13),   # Ideas and empathy - Selbstbild, Ethik, Optimistisch
    (345, 5), (345, 13), (345, 17),  # Learn-it-alls not know-it-alls - Gesellschaft, Optimistisch, Philosophisch
    (346, 4), (346, 13), (346, 26),  # Intelligence augments humans - Ethik, Optimistisch, Strategisch
    (347, 4), (347, 13), (347, 21),  # AI designed responsibly - Ethik, Optimistisch, Handlungsbezug
    (348, 11), (348, 13), (348, 16),  # Transparent accountable AI - Regulierung, Optimistisch, Politisch
    (349, 7), (349, 13), (349, 5),   # Democratize AI - Fortschritt, Optimistisch, Gesellschaft
    (350, 1), (350, 13), (350, 4),   # World needs safe AGI - Weltvision, Optimistisch, Ethik
    (351, 9), (351, 13), (351, 21),  # Copilot for developers - Arbeit/Wirtschaft, Optimistisch, Handlungsbezug
    (352, 7), (352, 13), (352, 21),  # New paradigm for search - Fortschritt, Optimistisch, Handlungsbezug
    (353, 7), (353, 13), (353, 24),  # Copilot is new UI - Fortschritt, Optimistisch, Zeitprognose
    (354, 1), (354, 13), (354, 9),   # Evolution of computing - Weltvision, Optimistisch, Arbeit/Wirtschaft
    (355, 9), (355, 13), (355, 26),  # Not race but real use cases - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (356, 11), (356, 13), (356, 4),  # AI innovation and safety - Regulierung, Optimistisch, Ethik
    (357, 9), (357, 13), (357, 26),  # Have all IP and capability - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (358, 7), (358, 13), (358, 24),  # Era of AI PCs - Fortschritt, Optimistisch, Zeitprognose
    (359, 9), (359, 13), (359, 26),  # Committed to OpenAI partnership - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (360, 9), (360, 13), (360, 11),  # Partnership accelerates innovation - Arbeit/Wirtschaft, Optimistisch, Regulierung
    (361, 11), (361, 15), (361, 16),  # Thoughtful regulation - Regulierung, Ambivalent, Politisch
    (362, 9), (362, 13), (362, 26),  # Every org custom AI - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (363, 1), (363, 13), (363, 24),  # Age of AI is here - Weltvision, Optimistisch, Zeitprognose
    (364, 9), (364, 13), (364, 18),  # Copilot fastest growing - Arbeit/Wirtschaft, Optimistisch, Empirisch
    (365, 11), (365, 13), (365, 16),  # Open to regulation - Regulierung, Optimistisch, Politisch
    (366, 7), (366, 13), (366, 9),   # Sora future of creative work - Fortschritt, Optimistisch, Arbeit/Wirtschaft
    (367, 11), (367, 15), (367, 17),  # AI is a tool - Regulierung, Ambivalent, Philosophisch

    # P16 - Daniela Amodei (A953-A967)
    (953, 9), (953, 13), (953, 4),   # Human skills more important - Arbeit/Wirtschaft, Optimistisch, Ethik
    (954, 7), (954, 15), (954, 26),  # Do more with less - Fortschritt, Ambivalent, Strategisch
    (955, 9), (955, 13), (955, 4),   # Trust unlocks deployment - Arbeit/Wirtschaft, Optimistisch, Ethik
    (956, 5), (956, 13), (956, 4),   # AI available throughout world - Gesellschaft, Optimistisch, Ethik
    (957, 6), (957, 13), (957, 11),  # Setting minimum safety standards - Risiko, Optimistisch, Regulierung
    (958, 6), (958, 15), (958, 4),   # Helpful honest harmless - Risiko, Ambivalent, Ethik
    (959, 4), (959, 15), (959, 21),  # Mission values honesty - Ethik, Ambivalent, Handlungsbezug
    (960, 4), (960, 13), (960, 17),  # Claude as partner - Ethik, Optimistisch, Philosophisch
    (961, 9), (961, 13), (961, 5),   # Humans+AI meaningful work - Arbeit/Wirtschaft, Optimistisch, Gesellschaft
    (962, 4), (962, 13), (962, 9),   # AI as copilot - Ethik, Optimistisch, Arbeit/Wirtschaft
    (963, 4), (963, 13), (963, 11),  # Build safe AI systems - Ethik, Optimistisch, Regulierung
    (964, 2), (964, 13), (964, 4),   # Different approach needed - Selbstbild, Optimistisch, Ethik
    (965, 9), (965, 13), (965, 26),  # Revenue and profit path - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (966, 11), (966, 13), (966, 16),  # Support federal AI policy - Regulierung, Optimistisch, Politisch

    # P17 - Lisa Su (A967-A986)
    (967, 7), (967, 13), (967, 2),   # AI most important tech - Fortschritt, Optimistisch, Selbstbild
    (968, 7), (968, 13), (968, 17),  # AI most powerful ever - Fortschritt, Optimistisch, Philosophisch
    (969, 7), (969, 15), (969, 22),  # AI accelerating - Fortschritt, Ambivalent, Epistemik
    (970, 9), (970, 13), (970, 18),  # Demand incredible - Arbeit/Wirtschaft, Optimistisch, Empirisch
    (971, 24), (971, 7), (971, 13),  # 10 yottaflops by 2030 - Zeitprognose, Fortschritt, Optimistisch
    (972, 9), (972, 13), (972, 21),  # AI not slowing hiring - Arbeit/Wirtschaft, Optimistisch, Handlungsbezug
    (973, 11), (973, 15), (973, 16),  # Balance export controls - Regulierung, Ambivalent, Politisch
    (974, 9), (974, 13), (974, 16),  # China large opportunity - Arbeit/Wirtschaft, Optimistisch, Politisch
    (975, 7), (975, 13), (975, 24),  # Year 2 of 10-year cycle - Fortschritt, Optimistisch, Zeitprognose
    (976, 9), (976, 13), (976, 16),  # Semiconductor manufacturing US - Arbeit/Wirtschaft, Optimistisch, Politisch
    (977, 9), (977, 13), (977, 24),  # Double-digit market share - Arbeit/Wirtschaft, Optimistisch, Zeitprognose
    (978, 9), (978, 13), (978, 18),  # Multiple technologies - Arbeit/Wirtschaft, Optimistisch, Empirisch
    (979, 5), (979, 13), (979, 16),  # Diversity benefits - Gesellschaft, Optimistisch, Politisch
    (980, 5), (980, 13), (980, 21),  # Make STEM fun - Gesellschaft, Optimistisch, Handlungsbezug
    (981, 9), (981, 13), (981, 26),  # Decide what to be - Arbeit/Wirtschaft, Optimistisch, Strategisch
    (982, 7), (982, 13), (982, 24),  # 100x power efficiency - Fortschritt, Optimistisch, Zeitprognose
    (983, 7), (983, 14), (983, 18),  # Supercomputers 500MW - Fortschritt, Pessimistisch, Empirisch
    (984, 5), (984, 13), (984, 17),  # Leaders are trained - Gesellschaft, Optimistisch, Philosophisch
    (985, 9), (985, 13), (985, 26),  # AI not zero-sum - Arbeit/Wirtschaft, Optimistisch, Strategisch

    # P18 - Tim Cook (A986-A1003)
    (986, 7), (986, 13), (986, 9),   # AI profound technology - Fortschritt, Optimistisch, Arbeit/Wirtschaft
    (987, 7), (987, 13), (987, 26),  # Best for customer - Fortschritt, Optimistisch, Strategisch
    (988, 7), (988, 13), (988, 24),  # Transformative opportunities 2024 - Fortschritt, Optimistisch, Zeitprognose
    (989, 7), (989, 13), (989, 4),   # Personal powerful private - Fortschritt, Optimistisch, Ethik
    (990, 4), (990, 14), (990, 16),  # Privacy fundamental right - Ethik, Pessimistisch, Politisch
    (991, 6), (991, 14), (991, 16),  # Data weaponized - Risiko, Pessimistisch, Politisch
    (992, 4), (992, 14), (992, 16),  # Privacy top issue - Ethik, Pessimistisch, Politisch
    (993, 4), (993, 13), (993, 17),  # Technology serve humanity - Ethik, Optimistisch, Philosophisch
    (994, 3), (994, 14), (994, 17),  # Worried about people not AI - Menschenbild, Pessimistisch, Philosophisch
    (995, 5), (995, 13), (995, 4),   # Moral responsibility economy - Gesellschaft, Optimistisch, Ethik
    (996, 11), (996, 13), (996, 16),  # Tech needs regulation - Regulierung, Optimistisch, Politisch
    (997, 4), (997, 14), (997, 16),  # Protect data and privacy - Ethik, Pessimistisch, Politisch
    (998, 5), (998, 13), (998, 4),   # Sustainable future - Gesellschaft, Optimistisch, Ethik
    (999, 9), (999, 13), (999, 16),  # China supply chain critical - Arbeit/Wirtschaft, Optimistisch, Politisch
    (1000, 5), (1000, 14), (1000, 16),  # Distraught immigration policy - Gesellschaft, Pessimistisch, Politisch
    (1001, 2), (1001, 13), (1001, 25),  # Being gay not limitation - Selbstbild, Optimistisch, Biographische Legitimation

    # P19 - Masayoshi Son (A1003-A1020)
    (1003, 2), (1003, 13), (1003, 12),  # Born to realize ASI - Selbstbild, Optimistisch, Spiritualität/Existenzielles
    (1004, 1), (1004, 13), (1004, 24),  # AI 10000x smarter - Weltvision, Optimistisch, Zeitprognose
    (1005, 1), (1005, 13), (1005, 12),  # Singularity inevitable - Weltvision, Optimistisch, Spiritualität/Existenzielles
    (1006, 1), (1006, 13), (1006, 24),  # 10B robots 10B humans - Weltvision, Optimistisch, Zeitprognose
    (1007, 1), (1007, 13), (1007, 24),  # Every industry redefined - Weltvision, Optimistisch, Zeitprognose
    (1008, 7), (1008, 13), (1008, 24),  # AI will solve cancer - Fortschritt, Optimistisch, Zeitprognose
    (1009, 10), (1009, 13), (1009, 17),  # Superintelligence as partner - Transhumanismus, Optimistisch, Philosophisch
    (1010, 2), (1010, 13), (1010, 12),  # 300 years human evolution - Selbstbild, Optimistisch, Spiritualität/Existenzielles
    (1011, 10), (1011, 13), (1011, 24),  # Telepathy with chips - Transhumanismus, Optimistisch, Zeitprognose
    (1012, 1), (1012, 13), (1012, 24),  # Telepathy service provider - Weltvision, Optimistisch, Zeitprognose
    (1013, 7), (1013, 13), (1013, 9),   # ASI needs breakthrough computing - Fortschritt, Optimistisch, Arbeit/Wirtschaft
    (1014, 1), (1014, 13), (1014, 24),  # Singularity by 2047 - Weltvision, Optimistisch, Zeitprognose
    (1015, 2), (1015, 13), (1015, 21),  # 97% time on AI - Selbstbild, Optimistisch, Handlungsbezug
    (1016, 24), (1016, 13), (1016, 1),  # AGI within 10 years - Zeitprognose, Optimistisch, Weltvision
    (1017, 24), (1017, 13), (1017, 1),  # AGI in 2-3 years - Zeitprognose, Optimistisch, Weltvision
    (1018, 2), (1018, 13), (1018, 9),   # Become ASI platform - Selbstbild, Optimistisch, Arbeit/Wirtschaft
    (1019, 4), (1019, 13), (1019, 12),  # Information Revolution happiness - Ethik, Optimistisch, Spiritualität/Existenzielles
    (1020, 2), (1020, 13), (1020, 9),   # 21st century Rothschild - Selbstbild, Optimistisch, Arbeit/Wirtschaft

    # P20 - Jeff Dean (A1062-A1076)
    (1062, 7), (1062, 13), (1062, 24),  # Major difference in 5 years - Fortschritt, Optimistisch, Zeitprognose
    (1063, 6), (1063, 14), (1063, 16),  # Extinction risk priority - Risiko, Pessimistisch, Politisch
    (1064, 5), (1064, 13), (1064, 21),  # Open source TensorFlow - Gesellschaft, Optimistisch, Handlungsbezug
    (1065, 7), (1065, 13), (1065, 19),  # Invented concept of cat - Fortschritt, Optimistisch, Anekdotisch
    (1066, 7), (1066, 13), (1066, 18),  # Medical imaging transformation - Fortschritt, Optimistisch, Empirisch
    (1067, 7), (1067, 13), (1067, 12),  # Moonshot all decisions inform future - Fortschritt, Optimistisch, Spiritualität/Existenzielles
    (1068, 11), (1068, 13), (1068, 16),  # Engage with governments - Regulierung, Optimistisch, Politisch
    (1069, 7), (1069, 13), (1069, 4),   # AI responsibly ethically - Fortschritt, Optimistisch, Ethik
    (1070, 7), (1070, 15), (1070, 18),  # Combine supervised/unsupervised - Fortschritt, Ambivalent, Empirisch
    (1071, 7), (1071, 13), (1071, 18),  # Chip specialization advantage - Fortschritt, Optimistisch, Empirisch
    (1072, 2), (1072, 13), (1072, 19),  # Like twins together - Selbstbild, Optimistisch, Anekdotisch
    (1073, 7), (1073, 13), (1073, 18),  # Sparse networks less energy - Fortschritt, Optimistisch, Empirisch
    (1074, 7), (1074, 13), (1074, 18),  # Gemini energy usage - Fortschritt, Optimistisch, Empirisch
    (1075, 9), (1075, 14), (1075, 18),  # Voice search double capacity - Arbeit/Wirtschaft, Pessimistisch, Empirisch
    (1076, 7), (1076, 13), (1076, 18),  # TPUs better performance - Fortschritt, Optimistisch, Empirisch
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {c.rowcount} Kodierungen fuer P11-P20")
c.execute("SELECT COUNT(*) FROM aussagen_kategorien")
print(f"Gesamt in DB: {c.fetchone()[0]}")
conn.close()
