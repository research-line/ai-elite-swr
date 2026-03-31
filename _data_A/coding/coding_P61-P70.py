import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierungen für P61-P70
codes = [
    # P61: Yoshua Bengio (A392-A416)
    (392, 7), (392, 22), (392, 13),  # Deep learning Fortschritt, AGI-Reise, epistemisch, optimistisch
    (393, 6), (393, 11), (393, 14),  # Safety-Forschung, Regulierung, pessimistisch
    (394, 8), (394, 6), (394, 14), (394, 16),  # Macht/Kontrolle, Risiko, pessimistisch, politisch
    (395, 6), (395, 5), (395, 14), (395, 22),  # Risiko für Gesellschaft, epistemisch, pessimistisch
    (396, 6), (396, 22), (396, 14), (396, 26),  # Zeitliche Nähe des Risikos, epistemisch, pessimistisch, Dringlichkeit
    (397, 11), (397, 6), (397, 14),  # Regulierung (Guardrails/Pause), Risiko, pessimistisch
    (398, 6), (398, 12), (398, 14), (398, 26),  # Existenzielles Risiko, Spirituell/existenziell, pessimistisch, Dringlichkeit
    (399, 6), (399, 5), (399, 14), (399, 16),  # Globale Priorität, Gesellschaft, pessimistisch, politisch
    (400, 11), (400, 5), (400, 13),  # Internationale Koordination, Gesellschaft, ambivalent
    (401, 6), (401, 7), (401, 14), (401, 21),  # Metapher Cliff, Fortschritt zu schnell, pessimistisch, Haltung
    (402, 22), (402, 6), (402, 14),  # Epistemische Unsicherheit (AGI-Zeitrahmen), Risiko, pessimistisch
    (403, 6), (403, 5), (403, 14),  # Katastrophale Schäden, Gesellschaft, pessimistisch
    (404, 22), (404, 11), (404, 13),  # Neue Forschungsagenda (Verstehen), epistemisch, Regulierung, ambivalent
    (405, 11), (405, 5), (405, 14), (405, 26),  # Globale Governance, Gesellschaft, pessimistisch, Dringlichkeit
    (406, 6), (406, 8), (406, 14), (406, 16),  # Multiple Risiken, Macht, pessimistisch, politisch
    (407, 4), (407, 5), (407, 13), (407, 17),  # Ethische Prinzipien, Gesellschaft, optimistisch, philosophisch
    (408, 22), (408, 18), (408, 13),  # GFlowNets (technische Methode), epistemisch, empirisch, optimistisch
    (409, 6), (409, 7), (409, 14), (409, 26),  # Wettlauf Capabilities vs Safety, Fortschritt, pessimistisch, Dringlichkeit
    (410, 3), (410, 10), (410, 13), (410, 17),  # Menschenbild (bessere Versionen), Transhumanismus, optimistisch, philosophisch
    (411, 11), (411, 9), (411, 14), (411, 16),  # Regulierung (Safety), Wirtschaft, pessimistisch, politisch
    (412, 6), (412, 12), (412, 14), (412, 22),  # Extinktionsrisiko 10-20%, existenziell, pessimistisch, epistemisch
    (413, 11), (413, 6), (413, 14), (413, 16),  # Licensing/Compute Governance, Risiko, pessimistisch, politisch
    (414, 7), (414, 6), (414, 14), (414, 2),  # Zu schneller Fortschritt, Risiko, pessimistisch, Selbstbild (Überraschung)
    (415, 6), (415, 11), (415, 2), (415, 14),  # Safety-Priorisierung bei MILA, Regulierung, Selbstbild, pessimistisch
    (416, 2), (416, 4), (416, 15), (416, 12),  # Selbstzweifel (Reue möglich), Ethik, ambivalent, existenziell

    # P62: Winston Weinberg (A1192-A1211)
    (1192, 2), (1192, 9), (1192, 13), (1192, 21),  # Selbstbild (Stress), Arbeit, optimistisch, Haltung
    (1193, 2), (1193, 9), (1193, 15), (1193, 21),  # Selbstbild (Reinvention), Arbeit, ambivalent, Haltung
    (1194, 9), (1194, 13), (1194, 21),  # Wirtschaft (Valuation), optimistisch, Haltung
    (1195, 9), (1195, 7), (1195, 13),  # Wirtschaft (Marktpotenzial), Fortschritt, optimistisch
    (1196, 9), (1196, 5), (1196, 13),  # Arbeit/Profession, Gesellschaft, optimistisch
    (1197, 5), (1197, 13), (1197, 19),  # Gesellschaft (Feedback), optimistisch, Anekdote
    (1198, 9), (1198, 2), (1198, 13),  # Arbeit (Hiring), Selbstbild (Methode), optimistisch
    (1199, 2), (1199, 9), (1199, 13), (1199, 21),  # Selbstbild (Führungsphilosophie), Arbeit, optimistisch, Haltung
    (1200, 9), (1200, 5), (1200, 13), (1200, 18),  # Arbeit (Task vs Job Displacement), Gesellschaft, optimistisch, empirisch
    (1201, 9), (1201, 5), (1201, 13),  # Arbeit (Junior Associates), Gesellschaft, optimistisch
    (1202, 9), (1202, 7), (1202, 13),  # Arbeit (Leverage Pyramid), Fortschritt, optimistisch
    (1203, 9), (1203, 7), (1203, 13),  # Arbeit (Multiplayer Future), Fortschritt, optimistisch
    (1204, 9), (1204, 7), (1204, 13),  # Arbeit (Complex Work), Fortschritt, optimistisch
    (1205, 9), (1205, 13),  # Wirtschaft (Marktdiversität), optimistisch
    (1206, 9), (1206, 13),  # Wirtschaft (Partnership), optimistisch
    (1207, 22), (1207, 9), (1207, 13),  # Epistemisch (UX vs Performance), Arbeit, optimistisch
    (1208, 5), (1208, 11), (1208, 13), (1208, 16),  # Gesellschaft (Gerechtigkeit), Regulierung (PPP), optimistisch, politisch
    (1209, 9), (1209, 7), (1209, 13),  # Arbeit (Innovation), Fortschritt, optimistisch
    (1210, 9), (1210, 11), (1210, 15),  # Wirtschaft (Sicherheit), Regulierung, ambivalent
    (1211, 22), (1211, 9), (1211, 13),  # Epistemisch (Human-in-loop), Arbeit, optimistisch

    # P63: Lip-Bu Tan (A1246-A1263)
    (1246, 2), (1246, 9), (1246, 14), (1246, 16),  # Selbstbild (Intel Kritik), Arbeit, pessimistisch, politisch
    (1247, 2), (1247, 4), (1247, 13),  # Selbstbild (Loyalität), Ethik, optimistisch
    (1248, 2), (1248, 9), (1248, 14), (1248, 16),  # Selbstbild (Feedback), Arbeit, pessimistisch, politisch
    (1249, 9), (1249, 11), (1249, 13),  # Arbeit (Restrukturierung), Regulierung, optimistisch
    (1250, 9), (1250, 13), (1250, 21),  # Wirtschaft (Investment), optimistisch, Haltung
    (1251, 9), (1251, 14), (1251, 21),  # Wirtschaft (Cashflow), pessimistisch, Haltung
    (1252, 9), (1252, 7), (1252, 13),  # Wirtschaft (Best Products), Fortschritt, optimistisch
    (1253, 9), (1253, 14),  # Wirtschaft (Overinvestment), pessimistisch
    (1254, 9), (1254, 13), (1254, 21),  # Wirtschaft (Capex Discipline), optimistisch, Haltung
    (1255, 9), (1255, 5), (1255, 13),  # Arbeit (Foundry), Gesellschaft (Trust), optimistisch
    (1256, 9), (1256, 7), (1256, 13),  # Wirtschaft (Tech Success), Fortschritt, optimistisch
    (1257, 9), (1257, 7), (1257, 13),  # Arbeit (GPU Investment), Fortschritt, optimistisch
    (1258, 7), (1258, 22), (1258, 13),  # Fortschritt (Moore's Law), epistemisch, optimistisch
    (1259, 7), (1259, 9), (1259, 13),  # Fortschritt (ML Processors), Arbeit, optimistisch
    (1260, 9), (1260, 7), (1260, 13),  # Wirtschaft (AI Startups), Fortschritt, optimistisch
    (1261, 2), (1261, 4), (1261, 13), (1261, 17),  # Selbstbild (Contrarian), Ethik, optimistisch, philosophisch
    (1262, 9), (1262, 11), (1262, 13),  # Arbeit (Restrukturierung), Regulierung, optimistisch
    (1263, 9), (1263, 13),  # Wirtschaft (Focus), optimistisch

    # P64: Jakob Uszkoreit (A1282-A1300)
    (1282, 2), (1282, 7), (1282, 13), (1282, 25),  # Selbstbild (Transformer Beitrag), Fortschritt, optimistisch, biografisch
    (1283, 2), (1283, 15), (1283, 19), (1283, 25),  # Selbstbild (Skepsis), ambivalent, Anekdote, biografisch
    (1284, 2), (1284, 7), (1284, 13), (1284, 25),  # Selbstbild (Pivot zu Bio), Fortschritt, optimistisch, biografisch
    (1285, 22), (1285, 3), (1285, 14), (1285, 17),  # Epistemisch (LLM-Grenzen), Menschenbild, pessimistisch, philosophisch
    (1286, 9), (1286, 15), (1286, 16),  # Wirtschaft (Google vs OpenAI), ambivalent, politisch
    (1287, 7), (1287, 5), (1287, 13),  # Fortschritt (Positive Potenziale), Gesellschaft, optimistisch
    (1288, 6), (1288, 11), (1288, 13), (1288, 17),  # Risiko, Regulierung (Responsible Development), optimistisch, philosophisch
    (1289, 7), (1289, 22), (1289, 15), (1289, 17),  # Fortschritt (Evolution vs Revolution), epistemisch, ambivalent, philosophisch
    (1290, 10), (1290, 7), (1290, 13), (1290, 17),  # Transhumanismus (Molecular Programming), Fortschritt, optimistisch, philosophisch
    (1291, 10), (1291, 7), (1291, 13), (1291, 19),  # Transhumanismus (mRNA++), Fortschritt, optimistisch, Anekdote
    (1292, 22), (1292, 7), (1292, 13), (1292, 17),  # Epistemisch (AI vs Theory), Fortschritt, optimistisch, philosophisch
    (1293, 7), (1293, 22), (1293, 13),  # Fortschritt (Architecture Simplification), epistemisch, optimistisch
    (1294, 7), (1294, 9), (1294, 13),  # Fortschritt (Drug Discovery), Arbeit, optimistisch
    (1295, 10), (1295, 13), (1295, 21),  # Transhumanismus (Cell Programming), optimistisch, Haltung
    (1296, 1), (1296, 10), (1296, 13), (1296, 17),  # Weltvision (Synthetic Biology), Transhumanismus, optimistisch, philosophisch
    (1297, 2), (1297, 15), (1297, 25),  # Selbstbild (Career Pivot), ambivalent, biografisch
    (1298, 19), (1298, 25),  # Anekdote (Name), biografisch
    (1299, 22), (1299, 3), (1299, 15), (1299, 17),  # Epistemisch (Cognition Limits), Menschenbild, ambivalent, philosophisch

    # P65: Trevor Darrell (A1300-A1318)
    (1300, 5), (1300, 9), (1300, 13), (1300, 17),  # Gesellschaft (Collaboration), Arbeit, optimistisch, philosophisch
    (1301, 9), (1301, 5), (1301, 13),  # Arbeit (Automation), Gesellschaft, optimistisch
    (1302, 7), (1302, 9), (1302, 13),  # Fortschritt (Small Teams), Arbeit, optimistisch
    (1303, 5), (1303, 7), (1303, 13), (1303, 16),  # Gesellschaft (Climate), Fortschritt, optimistisch, politisch
    (1304, 6), (1304, 7), (1304, 13),  # Risiko/Sicherheit (Autonomous Vehicles), Fortschritt, optimistisch
    (1305, 5), (1305, 9), (1305, 13), (1305, 17),  # Gesellschaft (Academia-Industry), Arbeit, optimistisch, philosophisch
    (1306, 7), (1306, 22), (1306, 13),  # Fortschritt (Efficiency), epistemisch, optimistisch
    (1307, 22), (1307, 13),  # Epistemisch (Interpretability), optimistisch
    (1308, 5), (1308, 11), (1308, 13), (1308, 16),  # Gesellschaft (Open Research), Regulierung, optimistisch, politisch
    (1309, 7), (1309, 13),  # Fortschritt (Multimodal AI), optimistisch
    (1310, 7), (1310, 22), (1310, 13),  # Fortschritt (Control/Perception), epistemisch, optimistisch
    (1311, 22), (1311, 7), (1311, 13),  # Epistemisch (CV Techniques), Fortschritt, optimistisch
    (1312, 22), (1312, 13), (1312, 18),  # Epistemisch (BDD100K Dataset), optimistisch, empirisch
    (1313, 5), (1313, 9), (1313, 13), (1313, 16),  # Gesellschaft (ORC), Arbeit, optimistisch, politisch
    (1314, 22), (1314, 7), (1314, 13),  # Epistemisch (R-CNN), Fortschritt, optimistisch
    (1315, 22), (1315, 7), (1315, 13),  # Epistemisch (Caffe Framework), Fortschritt, optimistisch
    (1316, 7), (1316, 13),  # Fortschritt (VLMs), optimistisch
    (1317, 22), (1317, 7), (1317, 13),  # Epistemisch (ADDA), Fortschritt, optimistisch

    # P66: Illia Polosukhin (A1318-A1338)
    (1318, 8), (1318, 5), (1318, 14), (1318, 16),  # Macht/Kontrolle (Bias), Gesellschaft, pessimistisch, politisch
    (1319, 4), (1319, 5), (1319, 13), (1319, 16),  # Ethik (User Sovereignty), Gesellschaft, optimistisch, politisch
    (1320, 7), (1320, 6), (1320, 15), (1320, 18),  # Fortschritt (Electricity Constraint), Risiko, ambivalent, empirisch
    (1321, 5), (1321, 9), (1321, 13), (1321, 17),  # Gesellschaft (Web3 Philosophy), Arbeit, optimistisch, philosophisch
    (1322, 5), (1322, 4), (1322, 13), (1322, 16),  # Gesellschaft (Open Web), Ethik, optimistisch, politisch
    (1323, 5), (1323, 9), (1323, 13), (1323, 19),  # Gesellschaft (Ukraine Crypto), Arbeit, optimistisch, Anekdote
    (1324, 5), (1324, 9), (1324, 13),  # Gesellschaft (NGO Speed), Arbeit, optimistisch
    (1325, 8), (1325, 5), (1325, 14), (1325, 16),  # Macht (FTX Kritik), Gesellschaft, pessimistisch, politisch
    (1326, 22), (1326, 15), (1326, 18),  # Epistemisch (AI Alchemy), ambivalent, empirisch
    (1327, 6), (1327, 5), (1327, 14),  # Risiko (Data Fear), Gesellschaft, pessimistisch
    (1328, 8), (1328, 6), (1328, 14), (1328, 16),  # Macht (Manipulation), Risiko, pessimistisch, politisch
    (1329, 5), (1329, 3), (1329, 13), (1329, 17),  # Gesellschaft (Future Meaning), Menschenbild, optimistisch, philosophisch
    (1330, 9), (1330, 5), (1330, 13),  # Arbeit (AI Agents), Gesellschaft, optimistisch
    (1331, 3), (1331, 4), (1331, 13), (1331, 17),  # Menschenbild (Human-AI Growth), Ethik, optimistisch, philosophisch
    (1332, 5), (1332, 11), (1332, 13), (1332, 16),  # Gesellschaft (Governance), Regulierung, optimistisch, politisch
    (1333, 22), (1333, 5), (1333, 13),  # Epistemisch (UX Abstraction), Gesellschaft, optimistisch
    (1334, 5), (1334, 6), (1334, 13), (1334, 16),  # Gesellschaft (Sustainability), Risiko, optimistisch, politisch
    (1335, 4), (1335, 8), (1335, 14), (1335, 16),  # Ethik (User-Owned AI), Macht, pessimistisch, politisch
    (1336, 1), (1336, 7), (1336, 13),  # Weltvision (Software Change), Fortschritt, optimistisch
    (1337, 4), (1337, 5), (1337, 13), (1337, 16),  # Ethik (Open AI), Gesellschaft, optimistisch, politisch

    # P67: Niki Parmar (A1338-A1345)
    (1338, 22), (1338, 7), (1338, 13), (1338, 18),  # Epistemisch (Transformer Mechanism), Fortschritt, optimistisch, empirisch
    (1339, 22), (1339, 2), (1339, 13), (1339, 17),  # Epistemisch (Research Method), Selbstbild, optimistisch, philosophisch
    (1340, 2), (1340, 22), (1340, 13), (1340, 17),  # Selbstbild (Research Struggle), epistemisch, optimistisch, philosophisch
    (1341, 2), (1341, 7), (1341, 13), (1341, 25),  # Selbstbild (Anthropic), Fortschritt, optimistisch, biografisch
    (1342, 2), (1342, 15), (1342, 25),  # Selbstbild (Google Exit), ambivalent, biografisch
    (1343, 7), (1343, 5), (1343, 13),  # Fortschritt (Human-Computer Collaboration), Gesellschaft, optimistisch
    (1344, 2), (1344, 25),  # Selbstbild (Background), biografisch
    (1345, 2), (1345, 22), (1345, 15), (1345, 17),  # Selbstbild (Humility), epistemisch, ambivalent, philosophisch

    # P68: Lukasz Kaiser (A1438-A1455)
    (1438, 22), (1438, 18), (1438, 15),  # Epistemisch (NN Limitations), empirisch, ambivalent
    (1439, 4), (1439, 8), (1439, 14), (1439, 17),  # Ethik (Dual Use), Macht, pessimistisch, philosophisch
    (1440, 2), (1440, 8), (1440, 15),  # Selbstbild (OpenAI Size), Macht, ambivalent
    (1441, 2), (1441, 9), (1441, 15), (1441, 19),  # Selbstbild (Career Comparison), Arbeit, ambivalent, Anekdote
    (1442, 2), (1442, 9), (1442, 15),  # Selbstbild (Reinvention), Arbeit, ambivalent
    (1443, 22), (1443, 7), (1443, 14), (1443, 18),  # Epistemisch (RNN Limits), Fortschritt, pessimistisch, empirisch
    (1444, 1), (1444, 10), (1444, 13), (1444, 17),  # Weltvision (One Model), Transhumanismus, optimistisch, philosophisch
    (1445, 2), (1445, 9), (1445, 13), (1445, 16),  # Selbstbild (OpenAI Crisis), Arbeit, optimistisch, politisch
    (1446, 22), (1446, 7), (1446, 15), (1446, 26),  # Epistemisch (Paradigm Shift), Fortschritt, ambivalent, Dringlichkeit
    (1447, 22), (1447, 7), (1447, 14), (1447, 18),  # Epistemisch (Scaling Limits), Fortschritt, pessimistisch, empirisch
    (1448, 22), (1448, 7), (1448, 15),  # Epistemisch (Data Scarcity), Fortschritt, ambivalent
    (1449, 7), (1449, 22), (1449, 13), (1449, 18),  # Fortschritt (o1 Paradigm), epistemisch, optimistisch, empirisch
    (1450, 22), (1450, 7), (1450, 13),  # Epistemisch (Reasoning), Fortschritt, optimistisch
    (1451, 1), (1451, 10), (1451, 13), (1451, 17),  # Weltvision (Researchers), Transhumanismus, optimistisch, philosophisch
    (1452, 1), (1452, 7), (1452, 13), (1452, 17),  # Weltvision (Models Doing Science), Fortschritt, optimistisch, philosophisch
    (1453, 22), (1453, 7), (1453, 13),  # Epistemisch (Internal Thinking), Fortschritt, optimistisch
    (1454, 22), (1454, 7), (1454, 13), (1454, 18),  # Epistemisch (Generalization), Fortschritt, optimistisch, empirisch
    (1455, 22), (1455, 7), (1455, 14), (1455, 18),  # Epistemisch (RNN Sequential Nature), Fortschritt, pessimistisch, empirisch

    # P69: Nat Friedman (A1489-A1508)
    (1489, 1), (1489, 4), (1489, 13), (1489, 17),  # Weltvision (Reshape Universe), Ethik, optimistisch, philosophisch
    (1490, 4), (1490, 7), (1490, 13), (1490, 21),  # Ethik (Ceiling vs Floor), Fortschritt, optimistisch, Haltung
    (1491, 7), (1491, 22), (1491, 13), (1491, 21),  # Fortschritt (Speed), epistemisch, optimistisch, Haltung
    (1492, 7), (1492, 13), (1492, 21),  # Fortschritt (Fast Focus), optimistisch, Haltung
    (1493, 7), (1493, 13), (1493, 17),  # Fortschritt (Energy), optimistisch, philosophisch
    (1494, 10), (1494, 3), (1494, 13),  # Transhumanismus (AI > Humans), Menschenbild, optimistisch
    (1495, 22), (1495, 15), (1495, 18),  # Epistemisch (Black Box), ambivalent, empirisch
    (1496, 7), (1496, 9), (1496, 13), (1496, 19),  # Fortschritt (Copilot), Arbeit, optimistisch, Anekdote
    (1497, 9), (1497, 13),  # Wirtschaft (Prices Dropping), optimistisch
    (1498, 2), (1498, 9), (1498, 13), (1498, 19),  # Selbstbild (GitHub Culture), Arbeit, optimistisch, Anekdote
    (1499, 2), (1499, 5), (1499, 13), (1499, 16),  # Selbstbild (Developer Focus), Gesellschaft, optimistisch, politisch
    (1500, 9), (1500, 18), (1500, 15),  # Wirtschaft (Immaterial Revenue), empirisch, ambivalent
    (1501, 2), (1501, 9), (1501, 15), (1501, 25),  # Selbstbild (Exit), Arbeit, ambivalent, biografisch
    (1502, 4), (1502, 5), (1502, 13), (1502, 21),  # Ethik (Developer First), Gesellschaft, optimistisch, Haltung
    (1503, 1), (1503, 4), (1503, 13), (1503, 17),  # Weltvision (Reshape Universe), Ethik, optimistisch, philosophisch
    (1504, 7), (1504, 22), (1504, 13),  # Fortschritt (Agency), epistemisch, optimistisch
    (1505, 11), (1505, 6), (1505, 13), (1505, 16),  # Regulierung (Insurance Model), Risiko, optimistisch, politisch
    (1506, 2), (1506, 9), (1506, 13), (1506, 19),  # Selbstbild (First Day), Arbeit, optimistisch, Anekdote
    (1507, 2), (1507, 4), (1507, 13), (1507, 17),  # Selbstbild (Vision), Ethik, optimistisch, philosophisch
    (1508, 2), (1508, 7), (1508, 13), (1508, 25),  # Selbstbild (Linux Discovery), Fortschritt, optimistisch, biografisch

    # P70: Llion Jones (A1745-A1763)
    (1745, 2), (1745, 22), (1745, 14), (1745, 21),  # Selbstbild (Sick of Transformers), epistemisch, pessimistisch, Haltung
    (1746, 7), (1746, 22), (1746, 14), (1746, 17),  # Fortschritt (Narrowing Research), epistemisch, pessimistisch, philosophisch
    (1747, 2), (1747, 7), (1747, 13),  # Selbstbild (Next Big Thing), Fortschritt, optimistisch
    (1748, 7), (1748, 22), (1748, 15), (1748, 17),  # Fortschritt (Tech Too Good), epistemisch, ambivalent, philosophisch
    (1749, 2), (1749, 22), (1749, 13), (1749, 17),  # Selbstbild (Research Philosophy), epistemisch, optimistisch, philosophisch
    (1750, 22), (1750, 3), (1750, 13), (1750, 17),  # Epistemisch (Reverse Engineering Mind), Menschenbild, optimistisch, philosophisch
    (1751, 9), (1751, 7), (1751, 14), (1751, 16),  # Arbeit (Investor Pressure), Fortschritt, pessimistisch, politisch
    (1752, 7), (1752, 22), (1752, 15), (1752, 26),  # Fortschritt (Paradigm Obsolescence), epistemisch, ambivalent, Dringlichkeit
    (1753, 2), (1753, 9), (1753, 14), (1753, 25),  # Selbstbild (Google Bureaucracy), Arbeit, pessimistisch, biografisch
    (1754, 5), (1754, 22), (1754, 13),  # Gesellschaft (Japanese Context), epistemisch, optimistisch
    (1755, 7), (1755, 22), (1755, 13), (1755, 21),  # Fortschritt (Curiosity), epistemisch, optimistisch, Haltung
    (1756, 7), (1756, 22), (1756, 13), (1756, 17),  # Fortschritt (Swarm Intelligence), epistemisch, optimistisch, philosophisch
    (1757, 2), (1757, 9), (1757, 15), (1757, 25),  # Selbstbild (Google Exit), Arbeit, ambivalent, biografisch
    (1758, 7), (1758, 9), (1758, 14), (1758, 16),  # Fortschritt (Corporate Stifling), Arbeit, pessimistisch, politisch
    (1759, 7), (1759, 22), (1759, 15), (1759, 17),  # Fortschritt (Local Optimization), epistemisch, ambivalent, philosophisch
    (1760, 2), (1760, 25),  # Selbstbild (Transformer Contribution), biografisch
    (1761, 7), (1761, 22), (1761, 13),  # Fortschritt (Distributed Models), epistemisch, optimistisch
    (1762, 5), (1762, 9), (1762, 13),  # Gesellschaft (Tokyo Infrastructure), Arbeit, optimistisch
    (1763, 2), (1763, 9), (1763, 13), (1763, 25),  # Selbstbild (Google Entry), Arbeit, optimistisch, biografisch
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {len(codes)} Kodierungen fuer P61-P70")
conn.close()
