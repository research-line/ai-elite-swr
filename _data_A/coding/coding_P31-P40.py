import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierungen für P31-P40 (Aravind Srinivas, Vinod Khosla, Michael Truell, Ashish Vaswani, Reid Hoffman, Aidan Gomez, Ali Ghodsi, Sriram Krishnan, Alex Karp, David Sacks)

codes = [
    # A537: Aravind Srinivas - Epistemik/Wissenschaftsmethode
    (537, 22), (537, 18), (537, 13),

    # A538: Aravind Srinivas - Menschenbild/Curiosity
    (538, 3), (538, 13),

    # A539: Aravind Srinivas - Epistemik/Quellen
    (539, 22), (539, 18), (539, 13),

    # A540: Aravind Srinivas - Epistemik/Werte
    (540, 22), (540, 4), (540, 13),

    # A541: Aravind Srinivas - Arbeit/Qualität
    (541, 9), (541, 13),

    # A542: Aravind Srinivas - Ethik/Lernen als Pflicht
    (542, 4), (542, 10), (542, 13), (542, 17),

    # A543: Aravind Srinivas - Menschenbild/Curiosity
    (543, 3), (543, 13),

    # A544: Aravind Srinivas - Wirtschaft/Kritik
    (544, 9), (544, 4), (544, 14), (544, 16),

    # A545: Aravind Srinivas - Kritik an Google
    (545, 9), (545, 14), (545, 21),

    # A546: Aravind Srinivas - Epistemik/Halluzinationen
    (546, 22), (546, 6), (546, 13), (546, 18),

    # A547: Aravind Srinivas - Selbstbild/Resilience
    (547, 2), (547, 6), (547, 13),

    # A548: Aravind Srinivas - Epistemik/Lernprozess
    (548, 22), (548, 7), (548, 13),

    # A573: Vinod Khosla - Arbeit/KI ersetzt Jobs
    (573, 9), (573, 10), (573, 14), (573, 20),

    # A574: Vinod Khosla - Arbeit/Anpassung
    (574, 9), (574, 6), (574, 14),

    # A575: Vinod Khosla - Arbeit/Medizin
    (575, 9), (575, 10), (575, 14),

    # A576: Vinod Khosla - Regulierung/Medizin
    (576, 11), (576, 9), (576, 13), (576, 20),

    # A577: Vinod Khosla - Gesellschaft/Demokratisierung
    (577, 5), (577, 9), (577, 13),

    # A578: Vinod Khosla - Gesellschaft/Demokratisierung
    (578, 5), (578, 9), (578, 13), (578, 20),

    # A579: Vinod Khosla - Arbeit/Ende der Arbeit
    (579, 9), (579, 7), (579, 13), (579, 20),

    # A580: Vinod Khosla - Arbeit/Workweek
    (580, 9), (580, 7), (580, 13), (580, 20),

    # A581: Vinod Khosla - Ethik/Politik
    (581, 4), (581, 16), (581, 14),

    # A582: Vinod Khosla - Gesellschaft/Demokratie
    (582, 5), (582, 6), (582, 14), (582, 16),

    # A583: Vinod Khosla - Regulierung/Open Source
    (583, 11), (583, 6), (583, 14), (583, 19),

    # A584: Vinod Khosla - Regulierung/Sicherheit
    (584, 11), (584, 6), (584, 14),

    # A585: Vinod Khosla - Geopolitik/Werte
    (585, 5), (585, 4), (585, 8), (585, 14), (585, 16),

    # A586: Vinod Khosla - Kritik/DeepSeek
    (586, 22), (586, 8), (586, 14), (586, 16),

    # A587: Vinod Khosla - Arbeit/Menschenbild
    (587, 9), (587, 3), (587, 13), (587, 20),

    # A588: Michael Truell - Risiko/Technische Schuld
    (588, 6), (588, 9), (588, 14), (588, 19),

    # A589: Michael Truell - Weltvision/Neudenken
    (589, 1), (589, 7), (589, 13),

    # A590: Michael Truell - Arbeit/Coding ersetzen
    (590, 9), (590, 7), (590, 13),

    # A591: Michael Truell - Fortschritt/Demokratisierung
    (591, 7), (591, 5), (591, 13),

    # A592: Michael Truell - Strategie/Kontrolle
    (592, 8), (592, 9), (592, 13),

    # A593: Michael Truell - Arbeit/Automatisierung
    (593, 9), (593, 7), (593, 15),

    # A594: Michael Truell - Fortschritt/Browser-Projekt
    (594, 7), (594, 9), (594, 13), (594, 18),

    # A595: Michael Truell - Weltvision/KI als Fundament
    (595, 1), (595, 7), (595, 13),

    # A596: Michael Truell - Selbstbild/Fokus
    (596, 2), (596, 4), (596, 13),

    # A597: Michael Truell - Weltvision/Epochal
    (597, 1), (597, 7), (597, 13),

    # A598: Michael Truell - Arbeit/Hiring
    (598, 9), (598, 15), (598, 18),

    # A599: Michael Truell - Selbstbild/Mission
    (599, 2), (599, 13),

    # A600: Michael Truell - Arbeit/Produktivität
    (600, 9), (600, 7), (600, 13), (600, 20),

    # A601: Ashish Vaswani - Epistemik/Transformer
    (601, 22), (601, 18), (601, 13),

    # A602: Ashish Vaswani - Epistemik/Daten
    (602, 22), (602, 15),

    # A603: Ashish Vaswani - Fortschritt/Mathematik
    (603, 7), (603, 22), (603, 13),

    # A604: Ashish Vaswani - Ethik/Open Science
    (604, 4), (604, 22), (604, 13),

    # A605: Ashish Vaswani - Selbstbild/Produktankündigung
    (605, 2), (605, 13), (605, 16),

    # A606: Ashish Vaswani - Kritik/Big Tech
    (606, 8), (606, 7), (606, 14), (606, 16),

    # A607: Ashish Vaswani - Ethik/Menschheit
    (607, 4), (607, 5), (607, 13),

    # A608: Ashish Vaswani - Menschenbild/Kooperation
    (608, 3), (608, 7), (608, 13),

    # A609: Ashish Vaswani - Selbstbild/Entdeckung
    (609, 2), (609, 22), (609, 15),

    # A610: Ashish Vaswani - Strategie/Technisch
    (610, 22), (610, 9), (610, 13),

    # A611: Ashish Vaswani - Selbstbild/Mission
    (611, 2), (611, 13),

    # A612: Ashish Vaswani - Epistemik/Reflection
    (612, 22), (612, 18), (612, 13),

    # A613: Reid Hoffman - Weltvision/Transformation
    (613, 1), (613, 7), (613, 13),

    # A614: Reid Hoffman - Menschenbild/Partner
    (614, 3), (614, 4), (614, 13),

    # A615: Reid Hoffman - Selbstbild/Optimismus
    (615, 2), (615, 4), (615, 13),

    # A616: Reid Hoffman - Gesellschaft/Geschwindigkeit
    (616, 5), (616, 7), (616, 15),

    # A617: Reid Hoffman - Gesellschaft/Angst
    (617, 5), (617, 6), (617, 14),

    # A618: Reid Hoffman - Menschenbild/Beziehungen
    (618, 3), (618, 4), (618, 13), (618, 19),

    # A619: Reid Hoffman - Arbeit/Agenten
    (619, 9), (619, 7), (619, 13),

    # A620: Reid Hoffman - Fortschritt/Medizin
    (620, 7), (620, 4), (620, 13),

    # A621: Reid Hoffman - Regulierung/Selbstverwaltung
    (621, 11), (621, 6), (621, 13),

    # A622: Reid Hoffman - Regulierung/Light-touch
    (622, 11), (622, 7), (622, 13), (622, 16),

    # A623: Reid Hoffman - Menschenbild/Innovation
    (623, 3), (623, 4), (623, 13), (623, 17),

    # A624: Reid Hoffman - Fortschritt/Biologie
    (624, 7), (624, 22), (624, 13),

    # A625: Aidan Gomez - Arbeit/Adoption
    (625, 9), (625, 13),

    # A626: Aidan Gomez - Risiko/Privacy
    (626, 6), (626, 9), (626, 14),

    # A627: Aidan Gomez - Fortschritt/Überraschung
    (627, 7), (627, 2), (627, 15), (627, 18),

    # A628: Aidan Gomez - Macht/Souveränität
    (628, 8), (628, 6), (628, 14), (628, 16),

    # A629: Aidan Gomez - Wirtschaft/Investoren
    (629, 9), (629, 13),

    # A630: Aidan Gomez - Wirtschaft/Geschäftsmodell
    (630, 9), (630, 13),

    # A631: Aidan Gomez - Selbstbild/Bescheidenheit
    (631, 2), (631, 22), (631, 15),

    # A632: Aidan Gomez - Fortschritt/Lernen
    (632, 7), (632, 22), (632, 13),

    # A633: Aidan Gomez - Fortschritt/Selbstverbesserung
    (633, 7), (633, 10), (633, 13),

    # A634: Aidan Gomez - Arbeit/Produktivität
    (634, 9), (634, 6), (634, 13),

    # A635: Aidan Gomez - Arbeit/Augmentierung
    (635, 9), (635, 3), (635, 13),

    # A636: Aidan Gomez - Selbstbild/Familie
    (636, 2), (636, 4), (636, 13), (636, 25),

    # A637: Ali Ghodsi - Fortschritt/Genug
    (637, 7), (637, 15),

    # A638: Ali Ghodsi - Wirtschaft/Bubble
    (638, 9), (638, 6), (638, 14),

    # A639: Ali Ghodsi - Arbeit/Agenten
    (639, 9), (639, 7), (639, 13), (639, 18),

    # A640: Ali Ghodsi - Risiko/Governance
    (640, 6), (640, 11), (640, 14),

    # A641: Ali Ghodsi - Wirtschaft/Disruption
    (641, 9), (641, 6), (641, 14), (641, 20),

    # A642: Ali Ghodsi - Gesellschaft/Demokratisierung
    (642, 5), (642, 8), (642, 13),

    # A643: Ali Ghodsi - Wirtschaft/Adoption
    (643, 9), (643, 13),

    # A644: Ali Ghodsi - Wirtschaft/IPO
    (644, 9), (644, 15),

    # A645: Ali Ghodsi - Selbstbild/Standard
    (645, 2), (645, 13),

    # A646: Ali Ghodsi - Arbeit/Dateninfrastruktur
    (646, 9), (646, 18), (646, 13),

    # A647: Ali Ghodsi - Wirtschaft/Wachstum
    (647, 9), (647, 13),

    # A648: Ali Ghodsi - Wirtschaft/Differenzierung
    (648, 9), (648, 8), (648, 13),

    # A649: Sriram Krishnan - Geopolitik/Existenziell
    (649, 8), (649, 6), (649, 14), (649, 16),

    # A650: Sriram Krishnan - Geopolitik/Wettbewerb
    (650, 8), (650, 9), (650, 14), (650, 16),

    # A651: Sriram Krishnan - Regulierung/Privatsektor
    (651, 11), (651, 9), (651, 13), (651, 16),

    # A652: Sriram Krishnan - Geopolitik/Tech-Stack
    (652, 8), (652, 9), (652, 14), (652, 16),

    # A653: Sriram Krishnan - Regulierung/Light-touch
    (653, 11), (653, 7), (653, 13), (653, 16),

    # A654: Sriram Krishnan - Regulierung/Föderalismus
    (654, 11), (654, 6), (654, 14), (654, 16),

    # A655: Sriram Krishnan - Macht/Deep State
    (655, 8), (655, 11), (655, 14), (655, 16),

    # A656: Sriram Krishnan - Wirtschaft/Web3
    (656, 9), (656, 5), (656, 13),

    # A657: Sriram Krishnan - Macht/Governance
    (657, 8), (657, 5), (657, 13),

    # A658: Sriram Krishnan - Gesellschaft/Dezentralisierung
    (658, 5), (658, 7), (658, 13), (658, 20),

    # A659: Sriram Krishnan - Regulierung/Transparenz
    (659, 11), (659, 4), (659, 13),

    # A660: Sriram Krishnan - Gesellschaft/Immigration
    (660, 5), (660, 4), (660, 13), (660, 16),

    # A661: Sriram Krishnan - Geopolitik/AI-Plan
    (661, 8), (661, 7), (661, 13), (661, 16),

    # A662: Sriram Krishnan - Selbstbild/Lernen
    (662, 2), (662, 13), (662, 25),

    # A677: Alex Karp - Gesellschaft/Silicon Valley
    (677, 5), (677, 4), (677, 14), (677, 16),

    # A678: Alex Karp - Selbstbild/Abgrenzung
    (678, 2), (678, 4), (678, 14),

    # A679: Alex Karp - Ethik/Oppenheimer
    (679, 4), (679, 8), (679, 15), (679, 16), (679, 19),

    # A680: Alex Karp - Selbstbild/Kampf
    (680, 2), (680, 21), (680, 13),

    # A681: Alex Karp - Weltvision/Geopolitik
    (681, 1), (681, 8), (681, 14), (681, 16),

    # A682: Alex Karp - Geopolitik/Amerika
    (682, 8), (682, 6), (682, 13), (682, 16),

    # A683: Alex Karp - Persönliches/Colorado
    (683, 2), (683, 13), (683, 19),

    # A684: Alex Karp - Geopolitik/ICE
    (684, 8), (684, 16), (684, 14), (684, 21),

    # A685: Alex Karp - Selbstbild/Israel
    (685, 2), (685, 4), (685, 13), (685, 16),

    # A686: Alex Karp - Selbstbild/Westen
    (686, 2), (686, 4), (686, 13), (686, 16),

    # A687: Alex Karp - Geopolitik/Ukraine
    (687, 8), (687, 6), (687, 13), (687, 16),

    # A688: Alex Karp - Selbstbild/Dyslexie
    (688, 2), (688, 13), (688, 25),

    # A689: David Sacks - Regulierung/One Rulebook
    (689, 11), (689, 8), (689, 13), (689, 16),

    # A690: David Sacks - Regulierung/Föderalismus
    (690, 11), (690, 6), (690, 14), (690, 16),

    # A691: David Sacks - Fortschritt/Exponentiell
    (691, 7), (691, 13), (691, 18),

    # A692: David Sacks - Regulierung/Open Source
    (692, 11), (692, 8), (692, 13), (692, 16),

    # A693: David Sacks - Ethik/Free Speech
    (693, 4), (693, 5), (693, 14), (693, 16),

    # A694: David Sacks - Wirtschaft/Wettbewerb
    (694, 9), (694, 8), (694, 13), (694, 16),

    # A695: David Sacks - Regulierung/Crypto
    (695, 11), (695, 9), (695, 13), (695, 16),

    # A696: David Sacks - Regulierung/Bitcoin Reserve
    (696, 11), (696, 9), (696, 13), (696, 16),

    # A697: David Sacks - Regulierung/Orwell
    (697, 11), (697, 6), (697, 14), (697, 16),

    # A698: David Sacks - Regulierung/Crypto
    (698, 11), (698, 9), (698, 13), (698, 16),

    # A699: David Sacks - Wirtschaft/Open Source
    (699, 9), (699, 13),

    # A700: David Sacks - Regulierung/Föderalismus
    (700, 11), (700, 6), (700, 14), (700, 16),

    # A701: David Sacks - Geopolitik/Open Source
    (701, 8), (701, 11), (701, 13), (701, 16),
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {len(codes)} Kodierungen fuer P31-P40")
conn.close()
