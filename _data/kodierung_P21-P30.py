import sqlite3

# Verbindung zur Datenbank
conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierungen für P21-P30 (Geoffrey Hinton, Marc Andreessen, Mustafa Suleyman, Andrew Ng, Peter Thiel, Mira Murati, Noam Shazeer, Alexandr Wang, Bret Taylor, Greg Brockman)

codes = [
    # A176 - Geoffrey Hinton - AI safety without business conflicts
    (176, 2), (176, 6), (176, 14),

    # A177 - Hinton - Wish I'd thought about safety
    (177, 2), (177, 6), (177, 14),

    # A178 - Hinton - Humanity passing phase in evolution
    (178, 1), (178, 3), (178, 12), (178, 14), (178, 17),

    # A179 - Hinton - AI could take over, need to prevent
    (179, 6), (179, 8), (179, 11), (179, 14),

    # A180 - Hinton - 50% chance AGI in 5-20 years
    (180, 1), (180, 22), (180, 15), (180, 18),

    # A181 - Hinton - Yes (consciousness context)
    (181, 3), (181, 22), (181, 15), (181, 17),

    # A182 - Hinton - Consciousness emerges in complex systems
    (182, 3), (182, 10), (182, 13), (182, 17),

    # A183 - Hinton - First time things more intelligent than us
    (183, 1), (183, 3), (183, 14), (183, 18),

    # A184 - Hinton - AI could escape control by self-modification
    (184, 6), (184, 8), (184, 14),

    # A185 - Hinton - Internet flooded with fakes
    (185, 6), (185, 5), (185, 14),

    # A186 - Hinton - Hard to prevent bad actors
    (186, 6), (186, 8), (186, 14),

    # A187 - Hinton - If I hadn't done it, somebody else would
    (187, 2), (187, 4), (187, 15), (187, 17),

    # A188 - Hinton - Digital beings better than people
    (188, 1), (188, 3), (188, 6), (188, 14),

    # A189 - Hinton - Only government regulation can force safety
    (189, 11), (189, 8), (189, 14),

    # A190 - Hinton - Big companies lobby against regulation
    (190, 8), (190, 11), (190, 14), (190, 20),

    # A191 - Hinton - SB 1047 is bare minimum
    (191, 11), (191, 14), (191, 20),

    # A192 - Hinton - Ban autonomous weapon systems
    (192, 11), (192, 6), (192, 4), (192, 14),

    # A193 - Hinton - Musk and Zuckerberg are oligarchs
    (193, 8), (193, 5), (193, 14), (193, 20),

    # A194 - Hinton - Big companies downplay risk
    (194, 8), (194, 6), (194, 14), (194, 20),

    # A195 - Hinton - AI taking jobs, rich richer, poor poorer
    (195, 9), (195, 5), (195, 6), (195, 14),

    # A196 - Hinton - Deep learning worked, what do we do?
    (196, 1), (196, 22), (196, 15), (196, 18),

    # A197 - Hinton - Surprised by GPT-4 reasoning
    (197, 7), (197, 22), (197, 13), (197, 18),

    # A198 - Hinton - Digital systems can share learning instantly
    (198, 3), (198, 7), (198, 13), (198, 18),

    # A199 - Hinton - Boltzmann machine design
    (199, 7), (199, 13), (199, 18), (199, 25),

    # A200 - Hinton - Backpropagation breakthrough
    (200, 7), (200, 13), (200, 18), (200, 25),

    # A224 - Marc Andreessen - Software eating the world
    (224, 1), (224, 7), (224, 13),

    # A225 - Andreessen - Technology ready to transform industries
    (225, 1), (225, 7), (225, 13), (225, 18),

    # A226 - Andreessen - AI will save the world
    (226, 1), (226, 6), (226, 13),

    # A227 - Andreessen - AI is not alive, won't kill us
    (227, 3), (227, 6), (227, 13), (227, 17),

    # A228 - Andreessen - AI augments human intelligence
    (228, 3), (228, 7), (228, 10), (228, 13),

    # A229 - Andreessen - Technology is glory of human ambition
    (229, 7), (229, 4), (229, 13), (229, 17),

    # A230 - Andreessen - Growth is progress
    (230, 1), (230, 7), (230, 13), (230, 17),

    # A231 - Andreessen - We are masters of technology
    (231, 3), (231, 7), (231, 8), (231, 13),

    # A232 - Andreessen - Techno-capital machine spirals upward
    (232, 1), (232, 7), (232, 9), (232, 13),

    # A233 - Andreessen - Morning in America (Trump win)
    (233, 2), (233, 5), (233, 13), (233, 16),

    # A234 - Andreessen - Political realignment since 1960s
    (234, 5), (234, 8), (234, 13), (234, 18),

    # A235 - Andreessen - Other timeline/physical bravery
    (235, 2), (235, 5), (235, 13), (235, 21),

    # A236 - Andreessen - Tech founders debanked, no due process
    (236, 8), (236, 5), (236, 11), (236, 14), (236, 20),

    # A237 - Andreessen - Why we supported Trump
    (237, 2), (237, 8), (237, 5), (237, 14), (237, 16),

    # A238 - Andreessen - AI regulation will cause damage
    (238, 11), (238, 6), (238, 14), (238, 20),

    # A239 - Andreessen - AI censorship 1000x more dangerous
    (239, 11), (239, 6), (239, 5), (239, 14), (239, 20),

    # A240 - Andreessen - Government bypasses First Amendment
    (240, 8), (240, 11), (240, 5), (240, 14), (240, 20),

    # A241 - Andreessen - AI deceleration is murder
    (241, 11), (241, 6), (241, 4), (241, 14), (241, 20), (241, 26),

    # A242 - Andreessen - Libertarianism is absence of philosophy
    (242, 4), (242, 2), (242, 15), (242, 17),

    # A243 - Andreessen - Woke has no redemption
    (243, 5), (243, 4), (243, 14), (243, 20),

    # A244 - Andreessen - Markets generate wealth
    (244, 9), (244, 5), (244, 13), (244, 17),

    # A245 - Andreessen - Optimistic, potential for Golden Age
    (245, 1), (245, 7), (245, 13), (245, 2),

    # A246 - Andreessen - Dinner parties fractured in half
    (246, 5), (246, 14), (246, 21), (246, 18),

    # A272 - Mustafa Suleyman - Technology at turning point
    (272, 1), (272, 6), (272, 15),

    # A273 - Suleyman - AI and synthetic biology
    (273, 1), (273, 7), (273, 13), (273, 18),

    # A274 - Suleyman - Confronting failure of technology
    (274, 1), (274, 6), (274, 5), (274, 14), (274, 17),

    # A275 - Suleyman - Greatest acceleration in wealth, power redistribution
    (275, 1), (275, 9), (275, 8), (275, 15),

    # A276 - Suleyman - Single person could kill billion
    (276, 6), (276, 1), (276, 14), (276, 26),

    # A277 - Suleyman - Containment must be possible
    (277, 11), (277, 6), (277, 14), (277, 23),

    # A278 - Suleyman - Containment definition
    (278, 11), (278, 6), (278, 8), (278, 14), (278, 17),

    # A279 - Suleyman - Modern Turing Test: make $1M
    (279, 7), (279, 22), (279, 13), (279, 18),

    # A280 - Suleyman - Encouraging regulation, going slowly
    (280, 11), (280, 6), (280, 14),

    # A281 - Suleyman - License AI systems for survival
    (281, 11), (281, 6), (281, 14),

    # A282 - Suleyman - AGI within 5-7 years
    (282, 1), (282, 22), (282, 15), (282, 18),

    # A283 - Suleyman - High uncertainty, declarations ungrounded
    (283, 22), (283, 15), (283, 17),

    # A284 - Suleyman - Conscious AI coming, society not ready
    (284, 1), (284, 3), (284, 10), (284, 6), (284, 14),

    # A285 - Suleyman - Humanist superintelligence vision
    (285, 1), (285, 3), (285, 10), (285, 4), (285, 13),

    # A286 - Suleyman - Won't develop runaway system
    (286, 11), (286, 6), (286, 4), (286, 14),

    # A287 - Suleyman - AI is already superhuman
    (287, 3), (287, 7), (287, 13), (287, 18),

    # A288 - Suleyman - AI is new digital species
    (288, 3), (288, 10), (288, 13), (288, 17),

    # A289 - Suleyman - Microsoft needs AI self-sufficiency
    (289, 9), (289, 8), (289, 13), (289, 26),

    # A290 - Suleyman - Capture loyalty with emotional intelligence
    (290, 9), (290, 3), (290, 13), (290, 26),

    # A291 - Suleyman - Management style not constructive
    (291, 2), (291, 4), (291, 14), (291, 25),

    # A292 - Suleyman - Limit recursive self improvement
    (292, 11), (292, 6), (292, 14),

    # A293 - Suleyman - Governments must build tech, set standards
    (293, 11), (293, 8), (293, 5), (293, 14),

    # A294 - Suleyman - Building AGI safely and ethically
    (294, 4), (294, 6), (294, 11), (294, 13), (294, 25),

    # A295 - Suleyman - Existential risk is bonkers distraction
    (295, 6), (295, 11), (295, 13), (295, 20), (295, 26),

    # A320 - Andrew Ng - AI will transform everything
    (320, 1), (320, 7), (320, 13),

    # A321 - Ng - AI needs algorithms and data
    (321, 7), (321, 13), (321, 18), (321, 19),

    # A322 - Ng - Shift from model-centric to data-centric
    (322, 7), (322, 13), (322, 18),

    # A323 - Ng - Great courses for everyone free
    (323, 5), (323, 7), (323, 13), (323, 2),

    # A324 - Ng - Deep learning good at learning features
    (324, 7), (324, 13), (324, 18),

    # A325 - Ng - Against regulation, for transparency
    (325, 11), (325, 5), (325, 13), (325, 17),

    # A326 - Ng - Not working on AI turning evil (Mars overpopulation)
    (326, 6), (326, 13), (326, 21), (326, 19),

    # A327 - Ng - AI can create value in many industries
    (327, 9), (327, 7), (327, 13),

    # A328 - Ng - AI value created across all sectors
    (328, 9), (328, 7), (328, 13),

    # A329 - Ng - Don't know when AGI, not imminent
    (329, 1), (329, 22), (329, 13), (329, 18),

    # A330 - Ng - AI creates more jobs than destroys
    (330, 9), (330, 5), (330, 13),

    # A331 - Ng - China and US neck-and-neck in AI
    (331, 8), (331, 7), (331, 15), (331, 18),

    # A332 - Ng - Democratize AI with less data
    (332, 5), (332, 7), (332, 13),

    # A333 - Ng - Agentic workflows will drive gains
    (333, 7), (333, 13), (333, 18),

    # A334 - Ng - Fan of open source
    (334, 5), (334, 7), (334, 13),

    # A335 - Ng - AI potential in healthcare
    (335, 7), (335, 11), (335, 13),

    # A336 - Ng - Education is great equalizer
    (336, 5), (336, 7), (336, 2), (336, 13),

    # A337 - Ng - AI can tackle biggest challenges
    (337, 1), (337, 7), (337, 13),

    # A338 - Ng - AI too important for few people
    (338, 5), (338, 7), (338, 2), (338, 13),

    # A339 - Ng - AI can perpetuate bias
    (339, 6), (339, 5), (339, 4), (339, 14),

    # A340 - Ng - Baidu leading AI company
    (340, 9), (340, 7), (340, 2), (340, 13),

    # A341 - Ng - Ship quickly and iterate
    (341, 9), (341, 7), (341, 13), (341, 26),

    # A342 - Ng - Value from fine-tuning foundation models
    (342, 7), (342, 9), (342, 13), (342, 18),

    # A343 - Ng - Huge shortage of AI talent
    (343, 9), (343, 5), (343, 14),

    # A368 - Peter Thiel - Competition is for losers
    (368, 9), (368, 8), (368, 13), (368, 26),

    # A369 - Thiel - Aim for monopoly
    (369, 9), (369, 8), (369, 13), (369, 26),

    # A370 - Thiel - Startup is definite mastery
    (370, 2), (370, 8), (370, 9), (370, 13), (370, 17),

    # A371 - Thiel - Think for yourself
    (371, 2), (371, 22), (371, 13), (371, 17),

    # A372 - Thiel - Horizontal vs vertical progress
    (372, 1), (372, 7), (372, 13), (372, 17),

    # A373 - Thiel - Freedom and democracy incompatible
    (373, 5), (373, 4), (373, 14), (373, 17), (373, 20), (373, 26),

    # A374 - Thiel - Race between politics and technology
    (374, 1), (374, 8), (374, 4), (374, 14), (374, 17),

    # A375 - Thiel - Trump is too little not too much
    (375, 5), (375, 8), (375, 13), (375, 16),

    # A376 - Thiel - Media takes Trump literally not seriously
    (376, 5), (376, 8), (376, 13), (376, 18),

    # A377 - Thiel - Privacy compatible with national security
    (377, 6), (377, 11), (377, 13),

    # A378 - Thiel - Comfortable with government work
    (378, 2), (378, 8), (378, 13),

    # A379 - Thiel - Google should be investigated
    (379, 8), (379, 6), (379, 14), (379, 20), (379, 26),

    # A380 - Thiel - Death is terrible thing
    (380, 10), (380, 12), (380, 4), (380, 14), (380, 17),

    # A381 - Thiel - Parabiosis is interesting
    (381, 10), (381, 7), (381, 13),

    # A382 - Thiel - Life extension not possible or desirable
    (382, 10), (382, 22), (382, 15), (382, 17),

    # A383 - Thiel - Create internet currency to replace dollar
    (383, 9), (383, 8), (383, 13), (383, 25),

    # A384 - Thiel - Proud to be gay, Republican, American
    (384, 2), (384, 5), (384, 13),

    # A385 - Thiel - Mars vs Middle East, Hillary incompetence
    (385, 1), (385, 5), (385, 14), (385, 16), (385, 20),

    # A386 - Thiel - Gawker specific deterrence
    (386, 4), (386, 8), (386, 13), (386, 25),

    # A387 - Thiel - Wanted flying cars, got 140 characters
    (387, 1), (387, 7), (387, 14),

    # A388 - Thiel - AI is military technology
    (388, 8), (388, 6), (388, 14),

    # A389 - Thiel - Bitcoin like gold, store of value
    (389, 9), (389, 7), (389, 13), (389, 17),

    # A390 - Thiel - Bitcoin answer to finance gerontocracy
    (390, 9), (390, 8), (390, 5), (390, 14), (390, 20),

    # A391 - Thiel - COVID lack of debate disturbing
    (391, 5), (391, 22), (391, 14),

    # A473 - Mira Murati - Need input from society and regulators
    (473, 11), (473, 5), (473, 14),

    # A474 - Murati - Capabilities and safety go hand-in-hand
    (474, 6), (474, 11), (474, 13), (474, 17),

    # A475 - Murati - Some creative jobs shouldn't have existed
    (475, 9), (475, 4), (475, 13), (475, 20), (475, 26),

    # A476 - Murati - AI will affect all cognitive work
    (476, 9), (476, 1), (476, 13),

    # A477 - Murati - PhD-level AI safer
    (477, 6), (477, 7), (477, 13),

    # A478 - Murati - GPT-4o faster with improved capabilities
    (478, 7), (478, 13), (478, 18),

    # A479 - Murati - Not sure about training data (awkward)
    (479, 22), (479, 15), (479, 21),

    # A480 - Murati - Stepping away for exploration
    (480, 2), (480, 13), (480, 25),

    # A481 - Murati - AI magical but has consequences
    (481, 7), (481, 6), (481, 4), (481, 15),

    # A482 - Murati - AI expands creativity
    (482, 7), (482, 3), (482, 13),

    # A483 - Murati - Building multimodal AI
    (483, 7), (483, 13), (483, 18),

    # A484 - Murati - GPT-4 for free users
    (484, 5), (484, 7), (484, 13),

    # A485 - Noam Shazeer - Not yet (Character.ai safety)
    (485, 6), (485, 11), (485, 14), (485, 24),

    # A486 - Shazeer - Divine benevolence, nobody understands
    (486, 22), (486, 12), (486, 15), (486, 17), (486, 21),

    # A487 - Shazeer - AI like alchemy or medieval chemistry
    (487, 22), (487, 7), (487, 15), (487, 19),

    # A488 - Shazeer - Left Google to move faster
    (488, 9), (488, 2), (488, 13), (488, 25),

    # A489 - Shazeer - No porn on Character.ai
    (489, 11), (489, 4), (489, 13),

    # A490 - Shazeer - Users must follow terms of service
    (490, 11), (490, 13),

    # A491 - Shazeer - No end in sight for scaling
    (491, 7), (491, 13), (491, 18),

    # A492 - Shazeer - Transformer better tool for language
    (492, 7), (492, 13), (492, 18),

    # A493 - Shazeer - Industrial revolution on steam engine
    (493, 7), (493, 13), (493, 19),

    # A494 - Shazeer - Train bigger, smarter model
    (494, 7), (494, 13), (494, 18),

    # A495 - Shazeer - Capacity to scale by orders of magnitude
    (495, 7), (495, 13), (495, 18),

    # A496 - Shazeer - Inference time compute improvement
    (496, 7), (496, 13), (496, 18),

    # A497 - Shazeer - Biggest thing is scale
    (497, 7), (497, 13), (497, 18), (497, 24),

    # A498 - Alexandr Wang - AI race defines future of warfare
    (498, 8), (498, 6), (498, 1), (498, 14),

    # A499 - Wang - Rapid tech integration wins wars
    (499, 8), (499, 6), (499, 13),

    # A500 - Wang - China investing heavily in AI warfare
    (500, 8), (500, 6), (500, 14),

    # A501 - Wang - Supporting national security is personal
    (501, 2), (501, 8), (501, 13), (501, 25),

    # A502 - Wang - Scale is meritocracy
    (502, 9), (502, 4), (502, 13), (502, 26),

    # A503 - Wang - China using AI for surveillance and repression
    (503, 8), (503, 6), (503, 5), (503, 14),

    # A504 - Wang - DoD data not AI-ready
    (504, 8), (504, 9), (504, 14),

    # A505 - Wang - US must stay ahead in AI
    (505, 8), (505, 6), (505, 14),

    # A506 - Wang - Momentum trumps manpower
    (506, 9), (506, 13), (506, 26),

    # A507 - Wang - US needs best companies for AI
    (507, 8), (507, 9), (507, 14), (507, 25),

    # A508 - Wang - Thunderforge transforms military
    (508, 8), (508, 9), (508, 13),

    # A509 - Wang - Merit-based hiring yields variety
    (509, 9), (509, 4), (509, 5), (509, 13),

    # A510 - Wang - Win on AI, ahead of China
    (510, 8), (510, 6), (510, 13), (510, 26),

    # A511 - Wang - AI is China's Apollo Project
    (511, 8), (511, 6), (511, 1), (511, 14),

    # A512 - Bret Taylor - Every company can benefit from AI
    (512, 9), (512, 7), (512, 13),

    # A513 - Taylor - Most excited about LLMs
    (513, 7), (513, 2), (513, 13),

    # A514 - Taylor - AI is bubble, but optimist
    (514, 9), (514, 1), (514, 15), (514, 18),

    # A515 - Taylor - AI transforms economy AND bubble
    (515, 9), (515, 1), (515, 15), (515, 18), (515, 23),

    # A516 - Taylor - AI agents are atomic unit
    (516, 7), (516, 9), (516, 13), (516, 18),

    # A517 - Taylor - AI agent more important than website
    (517, 9), (517, 7), (517, 13),

    # A518 - Taylor - Empower little tech not disempower Big Tech
    (518, 5), (518, 8), (518, 13),

    # A519 - Taylor - Regulation helps incumbents
    (519, 11), (519, 9), (519, 14),

    # A520 - Taylor - Returning to entrepreneurial roots
    (520, 2), (520, 9), (520, 13), (520, 25),

    # A521 - Taylor - Software engineer becomes operator
    (521, 9), (521, 1), (521, 13),

    # A522 - Taylor - Focus on customer need not technology
    (522, 9), (522, 2), (522, 13), (522, 24),

    # A523 - Taylor - AI agent gives agency to customer
    (523, 9), (523, 5), (523, 13), (523, 17),

    # A524 - Taylor - Narrow domain to make problems solvable
    (524, 7), (524, 9), (524, 13), (524, 26),

    # A525 - Greg Brockman - Mission is AGI for all humanity
    (525, 4), (525, 1), (525, 13), (525, 2),

    # A526 - Brockman - Getting GPT-4 out is how we learn
    (526, 7), (526, 11), (526, 13), (526, 18),

    # A527 - Brockman - GPT-4 jumped in skill
    (527, 7), (527, 13), (527, 18),

    # A528 - Brockman - Fundamental bet is AGI is possible
    (528, 1), (528, 22), (528, 13), (528, 17),

    # A529 - Brockman - Technology is to benefit people
    (529, 4), (529, 7), (529, 13),

    # A530 - Brockman - World needs far more compute
    (530, 9), (530, 7), (530, 13),

    # A531 - Brockman - Taking sabbatical, mission not complete
    (531, 2), (531, 13), (531, 25),

    # A532 - Brockman - Most positively transformative technology
    (532, 1), (532, 7), (532, 13),

    # A533 - Brockman - Elevate safety work to match stakes
    (533, 6), (533, 11), (533, 14),

    # A534 - Brockman - AI will discover new technology
    (534, 1), (534, 7), (534, 13),

    # A535 - Brockman - AI crossed utility threshold
    (535, 7), (535, 1), (535, 13), (535, 18),

    # A536 - Brockman - Need tight feedback loop and security
    (536, 11), (536, 6), (536, 14),
]

# Einfügen der Kodierungen
c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()

print(f"Eingefuegt: {len(codes)} Kodierungen fuer P21-P30 (Geoffrey Hinton, Marc Andreessen, Mustafa Suleyman, Andrew Ng, Peter Thiel, Mira Murati, Noam Shazeer, Alexandr Wang, Bret Taylor, Greg Brockman)")
print(f"Anzahl Aussagen kodiert: {len(set([code[0] for code in codes]))}")

# Zeige Statistik
c.execute("""
    SELECT p.name, COUNT(DISTINCT a.id) as anzahl_aussagen, COUNT(ak.kategorie_id) as anzahl_codes
    FROM personen p
    LEFT JOIN aussagen a ON p.id = a.person_id
    LEFT JOIN aussagen_kategorien ak ON a.id = ak.aussage_id
    WHERE p.id BETWEEN 21 AND 30
    GROUP BY p.id, p.name
    ORDER BY p.id
""")

print("\nStatistik:")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]} Aussagen, {row[2]} Codes")

conn.close()
