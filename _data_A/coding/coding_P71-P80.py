import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierungen für P71-P80 (Adarsh Hiremath, Naveen Rao, Brendan Foody, Jan Leike, Sualeh Asif, Daniel Gross, Surya Midha, May Habib, Aman Sanger, Clay Bavor)

codes = [
    # A1346 - Adarsh Hiremath: Emotionale Entscheidung, Selbstbild
    (1346, 2), (1346, 4), (1346, 15),

    # A1347 - Adarsh Hiremath: Kultur schwieriger als Software - Gesellschaft/Arbeit
    (1347, 5), (1347, 9), (1347, 14), (1347, 17),

    # A1348 - Adarsh Hiremath: Man kann Care nicht lehren - Menschenbild
    (1348, 3), (1348, 14), (1348, 17),

    # A1349 - Adarsh Hiremath: Bei Mercor bleiben - Selbstbild
    (1349, 2), (1349, 13), (1349, 18),

    # A1350 - Adarsh Hiremath: Zukunft der Programmierung - Fortschritt/Arbeit
    (1350, 7), (1350, 9), (1350, 13), (1350, 20),

    # A1351 - Adarsh Hiremath: Rolle der Programmierer entwickelt sich - Arbeit/Fortschritt
    (1351, 7), (1351, 9), (1351, 13), (1351, 20),

    # A1352 - Adarsh Hiremath: Wachstumszahlen - Arbeit
    (1352, 9), (1352, 13), (1352, 18),

    # A1353 - Adarsh Hiremath: Kein Vertriebsteam - Arbeit
    (1353, 9), (1353, 13), (1353, 18),

    # A1354 - Adarsh Hiremath: Außergewöhnliche Leute sind die Magie - Menschenbild/Arbeit
    (1354, 3), (1354, 9), (1354, 13), (1354, 18),

    # A1355 - Adarsh Hiremath: Teil transformativer Projekte sein - Selbstbild/Gesellschaft
    (1355, 2), (1355, 5), (1355, 13),

    # A1356 - Adarsh Hiremath: Vision ist groß - Weltvision
    (1356, 1), (1356, 13), (1356, 17),

    # A1357 - Adarsh Hiremath: Nicht aufgeschobenes Leben - Ethik/Werte
    (1357, 4), (1357, 13), (1357, 21),

    # A1358 - Adarsh Hiremath: Mercor als beste Stelle - Arbeit
    (1358, 9), (1358, 13), (1358, 20),

    # A1359 - Adarsh Hiremath: Keine Arbeit am Sonntag - Ethik/Arbeit
    (1359, 4), (1359, 9), (1359, 13), (1359, 19),

    # A1360 - Adarsh Hiremath: Menschliches Urteil lehren - Menschenbild/Fortschritt
    (1360, 3), (1360, 7), (1360, 13), (1360, 17),

    # A1361 - Adarsh Hiremath: AI reallokiert Arbeit - Arbeit/Gesellschaft
    (1361, 9), (1361, 5), (1361, 13), (1361, 17),

    # A1362 - Adarsh Hiremath: Arbeitsaggregation größte Chance - Arbeit
    (1362, 9), (1362, 13), (1362, 17),

    # A1363 - Naveen Rao: AGI-Begriff schadet - Epistemik/Menschenbild
    (1363, 22), (1363, 3), (1363, 14), (1363, 17),

    # A1364 - Naveen Rao: AI als Evolution der Menschheit - Transhumanismus/Weltvision
    (1364, 10), (1364, 1), (1364, 13), (1364, 17),

    # A1365 - Naveen Rao: Zu früh regulieren - Regulierung
    (1365, 11), (1365, 15), (1365, 17), (1365, 19),

    # A1366 - Naveen Rao: Intelligenz nicht rein reduktionistisch - Epistemik/Menschenbild
    (1366, 22), (1366, 3), (1366, 14), (1366, 17),

    # A1367 - Naveen Rao: Natürliche Lernsysteme nutzen Physik - Epistemik
    (1367, 22), (1367, 15), (1367, 17), (1367, 18),

    # A1368 - Naveen Rao: Napster-Moment für generative AI - Gesellschaft/Regulierung
    (1368, 5), (1368, 11), (1368, 15), (1368, 19),

    # A1369 - Naveen Rao: Energieproblem begrenzt Skalierung - Risiko/Fortschritt
    (1369, 6), (1369, 7), (1369, 14), (1369, 18),

    # A1370 - Naveen Rao: Analog vs Digital - Epistemik
    (1370, 22), (1370, 15), (1370, 17), (1370, 18),

    # A1371 - Naveen Rao: AI fehlt echte Reasoning - Epistemik
    (1371, 22), (1371, 14), (1371, 17), (1371, 18),

    # A1372 - Naveen Rao: AGI braucht Dynamik und Kausalität - Epistemik/Transhumanismus
    (1372, 22), (1372, 10), (1372, 15), (1372, 17),

    # A1373 - Naveen Rao: AGI Wahrscheinlichkeiten - Epistemik/Fortschritt
    (1373, 22), (1373, 7), (1373, 15), (1373, 18),

    # A1374 - Naveen Rao: Echte Gefahr in Überstürzung - Risiko/Regulierung
    (1374, 6), (1374, 11), (1374, 14), (1374, 17),

    # A1375 - Naveen Rao: LLMs mit eigenen Daten - Arbeit
    (1375, 9), (1375, 13), (1375, 18),

    # A1376 - Naveen Rao: Intelligenz auf jedem Substrat - Menschenbild/Epistemik
    (1376, 3), (1376, 22), (1376, 15), (1376, 17),

    # A1377 - Naveen Rao: Open Source überholt Closed - Fortschritt
    (1377, 7), (1377, 13), (1377, 20),

    # A1378 - Naveen Rao: Software-Interface zur Physik - Epistemik
    (1378, 22), (1378, 13), (1378, 17), (1378, 18),

    # A1379 - Naveen Rao: Computer so effizient wie Biologie - Transhumanismus/Fortschritt
    (1379, 10), (1379, 7), (1379, 13), (1379, 17),

    # A1380 - Naveen Rao: AI fehlt Kausalverständnis - Epistemik
    (1380, 22), (1380, 14), (1380, 17), (1380, 18),

    # A1381 - Naveen Rao: Energieangebot begrenzt Wachstum - Risiko/Arbeit
    (1381, 6), (1381, 9), (1381, 14), (1381, 18),

    # A1382 - Brendan Foody: Jeden Tag gearbeitet - Selbstbild/Arbeit
    (1382, 2), (1382, 9), (1382, 15), (1382, 18),

    # A1383 - Brendan Foody: Burnout durch Mangel an Sinn - Menschenbild/Arbeit
    (1383, 3), (1383, 9), (1383, 14), (1383, 17),

    # A1384 - Brendan Foody: Impulsiver Antrieb zur Obsession - Selbstbild
    (1384, 2), (1384, 13), (1384, 17), (1384, 18),

    # A1385 - Brendan Foody: 2/3 Wissensarbeit automatisieren - Arbeit/Fortschritt
    (1385, 9), (1385, 7), (1385, 13), (1385, 20),

    # A1386 - Brendan Foody: 50% Aufgaben in 5 Jahren - Arbeit/Fortschritt
    (1386, 9), (1386, 7), (1386, 13), (1386, 20),

    # A1387 - Brendan Foody: Menschliches Urteil lehren - Menschenbild/Fortschritt
    (1387, 3), (1387, 7), (1387, 13), (1387, 17),

    # A1388 - Brendan Foody: Höhere menschliche Dinge - Menschenbild/Gesellschaft
    (1388, 3), (1388, 5), (1388, 13), (1388, 17),

    # A1389 - Brendan Foody: Menschen lehren Maschinen - Arbeit/Menschenbild
    (1389, 9), (1389, 3), (1389, 13), (1389, 20),

    # A1390 - Brendan Foody: Nicht zu Prüfungen gegangen - Selbstbild
    (1390, 2), (1390, 15), (1390, 19),

    # A1391 - Brendan Foody: Flaschenhals menschlicher Arbeit - Arbeit/Gesellschaft
    (1391, 9), (1391, 5), (1391, 13), (1391, 17),

    # A1392 - Brendan Foody: Impact und ROI wichtig - Selbstbild/Werte
    (1392, 2), (1392, 4), (1392, 13), (1392, 18),

    # A1393 - Brendan Foody: Problem finden das man nicht loslassen kann - Ethik/Selbstbild
    (1393, 4), (1393, 2), (1393, 13), (1393, 21),

    # A1394 - Brendan Foody: Hohe Einstellungsstandards - Arbeit
    (1394, 9), (1394, 13), (1394, 21),

    # A1395 - Brendan Foody: Beste Zeit für Unternehmensgründung - Arbeit/Fortschritt
    (1395, 9), (1395, 7), (1395, 13), (1395, 21),

    # A1396 - Brendan Foody: Arbeit brauchte Disziplin im College - Selbstbild
    (1396, 2), (1396, 15), (1396, 18),

    # A1397 - Brendan Foody: Modelle zur Leistungsvorhersage - Arbeit/Fortschritt
    (1397, 9), (1397, 7), (1397, 13), (1397, 18),

    # A1398 - Brendan Foody: Menschen steigen in Wertschöpfung auf - Arbeit/Menschenbild
    (1398, 9), (1398, 3), (1398, 13), (1398, 17),

    # A1399 - Brendan Foody: Obsession statt Disziplin - Selbstbild
    (1399, 2), (1399, 13), (1399, 18),

    # A1418 - Jan Leike: Safety-Kultur zurückgestellt - Risiko/Ethik
    (1418, 6), (1418, 4), (1418, 14), (1418, 16),

    # A1419 - Jan Leike: Uneinigkeit über Prioritäten - Selbstbild/Ethik
    (1419, 2), (1419, 4), (1419, 14), (1419, 16),

    # A1420 - Jan Leike: Kampf um Rechenleistung - Arbeit/Macht
    (1420, 9), (1420, 8), (1420, 14), (1420, 18),

    # A1421 - Jan Leike: AGI-Vorbereitung überfällig - Risiko/Transhumanismus
    (1421, 6), (1421, 10), (1421, 14), (1421, 16),

    # A1422 - Jan Leike: Mehr Fokus auf Safety nötig - Risiko/Ethik
    (1422, 6), (1422, 4), (1422, 14), (1422, 16),

    # A1423 - Jan Leike: Alignment ist lösbar - Epistemik/Risiko
    (1423, 22), (1423, 6), (1423, 13), (1423, 17),

    # A1424 - Jan Leike: Realer Angriffswinkel auf Problem - Epistemik
    (1424, 22), (1424, 13), (1424, 17), (1424, 18),

    # A1425 - Jan Leike: Schwache Supervision für übermenschliche Modelle - Epistemik/Transhumanismus
    (1425, 22), (1425, 10), (1425, 14), (1425, 17),

    # A1426 - Jan Leike: RLHF funktioniert - Epistemik
    (1426, 22), (1426, 13), (1426, 18), (1426, 17),

    # A1427 - Jan Leike: Wechsel zu Anthropic - Selbstbild
    (1427, 2), (1427, 13), (1427, 18),

    # A1428 - Jan Leike: Unsicherheit über AGI-Zeitpunkt - Epistemik
    (1428, 22), (1428, 15), (1428, 17), (1428, 18),

    # A1429 - Jan Leike: Nächste Generation ausrichten ist einfacher - Epistemik/Strategie
    (1429, 22), (1429, 13), (1429, 17), (1429, 26),

    # A1430 - Jan Leike: DeepMind Portfolio-Ansatz - Epistemik/Strategie
    (1430, 22), (1430, 15), (1430, 18), (1430, 26),

    # A1431 - Jan Leike: Automatisierter Alignment-Forscher - Fortschritt/Risiko
    (1431, 7), (1431, 6), (1431, 13), (1431, 17),

    # A1432 - Jan Leike: Weak-to-strong Generalisierung - Epistemik
    (1432, 22), (1432, 13), (1432, 18), (1432, 17),

    # A1433 - Jan Leike: Scalable Oversight Portfolio - Epistemik/Strategie
    (1433, 22), (1433, 13), (1433, 17), (1433, 26),

    # A1434 - Jan Leike: OpenAI als beste Stelle - Selbstbild
    (1434, 2), (1434, 14), (1434, 18),

    # A1435 - Jan Leike: Gegen den Wind segeln - Selbstbild
    (1435, 2), (1435, 14), (1435, 19),

    # A1436 - Jan Leike: Alignment im Voraus lösen - Risiko/Strategie
    (1436, 6), (1436, 13), (1436, 17), (1436, 26),

    # A1437 - Jan Leike: Viel Forschungsfortschritt möglich - Epistemik
    (1437, 22), (1437, 13), (1437, 17), (1437, 18),

    # A1456 - Sualeh Asif: Tool das alle Software baut - Weltvision/Fortschritt
    (1456, 1), (1456, 7), (1456, 13), (1456, 17),

    # A1457 - Sualeh Asif: In 10 Jahren noch nutzen - Fortschritt
    (1457, 7), (1457, 13), (1457, 17),

    # A1458 - Sualeh Asif: Entwickler in Kontrolle - Menschenbild/Arbeit
    (1458, 3), (1458, 9), (1458, 13), (1458, 17),

    # A1459 - Sualeh Asif: Produktivität steigern, nicht ersetzen - Arbeit
    (1459, 9), (1459, 13), (1459, 17),

    # A1460 - Sualeh Asif: Entwickler ausrüsten nicht ersetzen - Arbeit/Menschenbild
    (1460, 9), (1460, 3), (1460, 13), (1460, 17),

    # A1461 - Sualeh Asif: Copilot erstes AI-Produkt - Fortschritt
    (1461, 7), (1461, 13), (1461, 18),

    # A1462 - Sualeh Asif: Skalierung berechenbar besser - Fortschritt
    (1462, 7), (1462, 13), (1462, 18),

    # A1463 - Sualeh Asif: AI verstärkt, ersetzt nicht - Arbeit/Menschenbild
    (1463, 9), (1463, 3), (1463, 13), (1463, 17),

    # A1464 - Sualeh Asif: Schneller Kollege - Arbeit
    (1464, 9), (1464, 13), (1464, 17),

    # A1465 - Sualeh Asif: Hunderte Millionen Anfragen skalieren - Arbeit/Fortschritt
    (1465, 9), (1465, 7), (1465, 13), (1465, 18),

    # A1466 - Sualeh Asif: Vertrauen durch Produktqualität - Arbeit/Ethik
    (1466, 9), (1466, 4), (1466, 13), (1466, 18),

    # A1467 - Sualeh Asif: Menschen für Kreativität nötig - Menschenbild
    (1467, 3), (1467, 13), (1467, 17),

    # A1468 - Sualeh Asif: Menschen mit AI zusammenarbeiten - Arbeit/Menschenbild
    (1468, 9), (1468, 3), (1468, 13), (1468, 17),

    # A1469 - Sualeh Asif: Frustration inspirierte Cursor - Selbstbild/Arbeit
    (1469, 2), (1469, 9), (1469, 13), (1469, 18),

    # A1470 - Sualeh Asif: Automatisierung mit Kontrolle - Arbeit/Menschenbild
    (1470, 9), (1470, 3), (1470, 13), (1470, 17),

    # A1471 - Daniel Gross: AI demokratisieren - Gesellschaft/Macht
    (1471, 5), (1471, 8), (1471, 13), (1471, 16),

    # A1472 - Daniel Gross: AI demokratisieren bei YC - Gesellschaft/Macht
    (1472, 5), (1472, 8), (1472, 13), (1472, 16),

    # A1473 - Daniel Gross: ML frisst Software - Fortschritt
    (1473, 7), (1473, 13), (1473, 17),

    # A1474 - Daniel Gross: Monotone Textarbeit beschleunigt - Arbeit/Fortschritt
    (1474, 9), (1474, 7), (1474, 13), (1474, 20),

    # A1475 - Daniel Gross: Extremes Wachstum, fast ungesund - Arbeit
    (1475, 9), (1475, 15), (1475, 18),

    # A1476 - Daniel Gross: Nicht nur AI ist spannend - Fortschritt
    (1476, 7), (1476, 15), (1476, 17),

    # A1477 - Daniel Gross: Erwarte Wunder - Weltvision
    (1477, 1), (1477, 13), (1477, 17),

    # A1478 - Daniel Gross: Kultur und Künstler für Tech - Gesellschaft/Ethik
    (1478, 5), (1478, 4), (1478, 13), (1478, 17),

    # A1479 - Daniel Gross: Bessere Dinge von Außenseitern - Gesellschaft
    (1479, 5), (1479, 13), (1479, 17),

    # A1480 - Daniel Gross: Leben ist Videospiel, Suche nach Neuheit - Menschenbild
    (1480, 3), (1480, 15), (1480, 17),

    # A1481 - Daniel Gross: Dezentrales AI-Labor - Gesellschaft/Arbeit
    (1481, 5), (1481, 9), (1481, 13), (1481, 17),

    # A1482 - Daniel Gross: Wir sind früh dran - Fortschritt
    (1482, 7), (1482, 13), (1482, 18),

    # A1483 - Daniel Gross: Jerusalem zu Apple - Gesellschaft
    (1483, 5), (1483, 13), (1483, 19),

    # A1484 - Daniel Gross: In sich investieren - Ethik/Selbstbild
    (1484, 4), (1484, 2), (1484, 13), (1484, 21),

    # A1485 - Daniel Gross: Deep Fakes bedrohen Vertrauen - Risiko/Gesellschaft
    (1485, 6), (1485, 5), (1485, 14), (1485, 17),

    # A1486 - Daniel Gross: Online-Lesen verändert Lesefähigkeit - Gesellschaft/Risiko
    (1486, 5), (1486, 6), (1486, 14), (1486, 17),

    # A1487 - Daniel Gross: Richtiger Einsatz von AI wichtiger - Ethik/Arbeit
    (1487, 4), (1487, 9), (1487, 13), (1487, 17),

    # A1488 - Daniel Gross: Evaluation von Unternehmen - Arbeit
    (1488, 9), (1488, 15), (1488, 18),

    # A1527 - Surya Midha: 50 Jahre übersprungen - Selbstbild
    (1527, 2), (1527, 15), (1527, 17), (1527, 19),

    # A1528 - Surya Midha: Wechsel zu Chairman - Selbstbild/Arbeit
    (1528, 2), (1528, 9), (1528, 13), (1528, 18),

    # A1529 - Surya Midha: Series A Finanzierung - Arbeit
    (1529, 9), (1529, 13), (1529, 18),

    # A1530 - Surya Midha: Tiefgreifender gesellschaftlicher Wandel - Gesellschaft/Arbeit
    (1530, 5), (1530, 9), (1530, 13), (1530, 17),

    # A1531 - Surya Midha: Milliarde Menschen einstellen - Weltvision/Arbeit
    (1531, 1), (1531, 9), (1531, 13), (1531, 17),

    # A1532 - Surya Midha: Moralisches Gewicht der Arbeit - Ethik/Arbeit
    (1532, 4), (1532, 9), (1532, 13), (1532, 17),

    # A1533 - Surya Midha: Messianische Intensität - Selbstbild/Spiritualität
    (1533, 2), (1533, 12), (1533, 15), (1533, 17),

    # A1534 - Surya Midha: Von drei zu 100 Leuten - Arbeit
    (1534, 9), (1534, 13), (1534, 18),

    # A1535 - Surya Midha: Highschool Debatte - Selbstbild
    (1535, 2), (1535, 13), (1535, 25),

    # A1536 - Surya Midha: Georgetown Studium - Selbstbild
    (1536, 2), (1536, 13), (1536, 25),

    # A1575 - May Habib: Sprache und Lebensmöglichkeiten - Gesellschaft/Ethik
    (1575, 5), (1575, 4), (1575, 13), (1575, 17),

    # A1576 - May Habib: AI kann Gleichheit schaffen oder verstärken - Gesellschaft/Risiko
    (1576, 5), (1576, 6), (1576, 15), (1576, 17),

    # A1577 - May Habib: Zukunft mit Würde oder ohne - Gesellschaft/Ethik
    (1577, 5), (1577, 4), (1577, 15), (1577, 17),

    # A1578 - May Habib: Kunden gehen Risiko ein - Arbeit/Risiko
    (1578, 9), (1578, 6), (1578, 13), (1578, 18),

    # A1579 - May Habib: Writer im Risiko-Modus - Arbeit/Risiko
    (1579, 9), (1579, 6), (1579, 15), (1579, 18),

    # A1580 - May Habib: Intelligente Arbeitsplätze - Arbeit/Gesellschaft
    (1580, 9), (1580, 5), (1580, 13), (1580, 17),

    # A1581 - May Habib: Lücke zwischen Fähigkeit und Ergebnis - Arbeit/Fortschritt
    (1581, 9), (1581, 7), (1581, 14), (1581, 18),

    # A1582 - May Habib: Konträrer Einsatz eigene Modelle - Arbeit/Strategie
    (1582, 9), (1582, 13), (1582, 18), (1582, 26),

    # A1583 - May Habib: AI besser/schneller als Menschen - Fortschritt/Menschenbild
    (1583, 7), (1583, 3), (1583, 13), (1583, 17),

    # A1584 - May Habib: Zukunft Workflows statt Handarbeit - Arbeit/Fortschritt
    (1584, 9), (1584, 7), (1584, 13), (1584, 17),

    # A1585 - May Habib: Risiko von AI-Tools nicht existent - Risiko/Arbeit
    (1585, 6), (1585, 9), (1585, 13), (1585, 18),

    # A1586 - May Habib: AI HQ für agentische AI - Arbeit/Fortschritt
    (1586, 9), (1586, 7), (1586, 13), (1586, 18),

    # A1587 - May Habib: Transformation durch Customer Success - Arbeit
    (1587, 9), (1587, 13), (1587, 17),

    # A1588 - May Habib: Komplexe Aktionen und Workflows - Arbeit/Fortschritt
    (1588, 9), (1588, 7), (1588, 13), (1588, 18),

    # A1589 - May Habib: Yin und Yang Partnerschaft - Selbstbild
    (1589, 2), (1589, 13), (1589, 18),

    # A1590 - May Habib: Zukunft mit Würde oder ohne - Gesellschaft/Ethik
    (1590, 5), (1590, 4), (1590, 15), (1590, 17),

    # A1591 - May Habib: Multimodale AI-Fähigkeiten - Fortschritt
    (1591, 7), (1591, 13), (1591, 18),

    # A1592 - May Habib: AI als Game-Changer - Arbeit/Fortschritt
    (1592, 9), (1592, 7), (1592, 13), (1592, 17),

    # A1593 - May Habib: Anderer Weg für positive Veränderung - Ethik/Fortschritt
    (1593, 4), (1593, 7), (1593, 13), (1593, 17),

    # A1649 - Aman Sanger: Bauen wie man 20 Jahre programmiert - Weltvision/Fortschritt
    (1649, 1), (1649, 7), (1649, 13), (1649, 17),

    # A1650 - Aman Sanger: Paranoia ist täglich - Selbstbild/Risiko
    (1650, 2), (1650, 6), (1650, 14), (1650, 17),

    # A1651 - Aman Sanger: Viel Experimentieren - Arbeit/Epistemik
    (1651, 9), (1651, 22), (1651, 13), (1651, 18),

    # A1652 - Aman Sanger: Halbfertige Dinge veröffentlicht - Arbeit/Strategie
    (1652, 9), (1652, 13), (1652, 18), (1652, 26),

    # A1653 - Aman Sanger: Langsames Wachstum demoralisierend - Selbstbild/Arbeit
    (1653, 2), (1653, 9), (1653, 14), (1653, 18),

    # A1654 - Aman Sanger: Programmieren wird Code-Audit - Arbeit/Fortschritt
    (1654, 9), (1654, 7), (1654, 13), (1654, 20),

    # A1655 - Aman Sanger: Cursor löst Engineering-Flaschenhals - Arbeit/Fortschritt
    (1655, 9), (1655, 7), (1655, 13), (1655, 17),

    # A1656 - Aman Sanger: Entwickler im Fahrersitz - Menschenbild/Arbeit
    (1656, 3), (1656, 9), (1656, 13), (1656, 17),

    # A1657 - Aman Sanger: Nachhaltig und unabhängig - Selbstbild/Arbeit
    (1657, 2), (1657, 9), (1657, 13), (1657, 17),

    # A1658 - Aman Sanger: Langsam eingestellt - Arbeit/Strategie
    (1658, 9), (1658, 13), (1658, 18), (1658, 26),

    # A1659 - Aman Sanger: Neue AI-IDE nötig - Fortschritt/Arbeit
    (1659, 7), (1659, 9), (1659, 13), (1659, 17),

    # A1660 - Aman Sanger: Nicht eigene Modelle trainieren - Arbeit/Strategie
    (1660, 9), (1660, 13), (1660, 18), (1660, 26),

    # A1661 - Aman Sanger: UX komplett neu designen - Arbeit/Fortschritt
    (1661, 9), (1661, 7), (1661, 13), (1661, 17),

    # A1662 - Aman Sanger: AGI durch Rekurrenz möglich - Transhumanismus/Epistemik
    (1662, 10), (1662, 22), (1662, 13), (1662, 17),

    # A1663 - Aman Sanger: Laserfokus auf Developer Productivity - Arbeit
    (1663, 9), (1663, 13), (1663, 17),

    # A1664 - Aman Sanger: Preismodell durch Produktqualität - Arbeit/Strategie
    (1664, 9), (1664, 13), (1664, 18), (1664, 26),

    # A1665 - Aman Sanger: Strategie gegen Copilot - Arbeit/Strategie
    (1665, 9), (1665, 13), (1665, 18), (1665, 26),

    # A1666 - Aman Sanger: IDE besitzen gibt Vorteil - Arbeit/Strategie
    (1666, 9), (1666, 13), (1666, 17), (1666, 26),

    # A1667 - Aman Sanger: AI schafft mehr Druck - Risiko/Fortschritt
    (1667, 6), (1667, 7), (1667, 14), (1667, 17),

    # A1668 - Aman Sanger: Programmierer ermächtigt mit Kontrolle - Arbeit/Menschenbild
    (1668, 9), (1668, 3), (1668, 13), (1668, 17),

    # A1687 - Clay Bavor: Computer wie wir machen uns fähiger - Fortschritt/Menschenbild
    (1687, 7), (1687, 3), (1687, 13), (1687, 17),

    # A1688 - Clay Bavor: Immersive Computing als nächster Schritt - Fortschritt
    (1688, 7), (1688, 13), (1688, 17),

    # A1689 - Clay Bavor: VR/AR Teil der nächsten Computing-Phase - Fortschritt
    (1689, 7), (1689, 13), (1689, 17),

    # A1690 - Clay Bavor: VR/AR werden verschwimmen - Fortschritt
    (1690, 7), (1690, 13), (1690, 17),

    # A1691 - Clay Bavor: AI für außergewöhnliche Kundenerfahrungen - Arbeit
    (1691, 9), (1691, 13), (1691, 17),

    # A1692 - Clay Bavor: Technologie vergrößert alles - Fortschritt/Risiko
    (1692, 7), (1692, 6), (1692, 15), (1692, 17),

    # A1693 - Clay Bavor: Geringer Aufwand wichtigster Prädiktor - Menschenbild/Arbeit
    (1693, 3), (1693, 9), (1693, 13), (1693, 17),

    # A1694 - Clay Bavor: 2025 braucht man AI-Agenten - Fortschritt/Arbeit
    (1694, 7), (1694, 9), (1694, 13), (1694, 20),

    # A1695 - Clay Bavor: AI-Agent wichtiger als Website - Fortschritt/Arbeit
    (1695, 7), (1695, 9), (1695, 13), (1695, 17),

    # A1696 - Clay Bavor: Über-/Unterschätzung neuer Technologie - Fortschritt
    (1696, 7), (1696, 15), (1696, 17),

    # A1697 - Clay Bavor: In 5 Jahren anderer Markt - Fortschritt/Gesellschaft
    (1697, 7), (1697, 5), (1697, 13), (1697, 20),

    # A1698 - Clay Bavor: AI ist Paradigmenwechsel - Fortschritt
    (1698, 7), (1698, 13), (1698, 17),

    # A1699 - Clay Bavor: AI-Version des Unternehmens übertrifft alles - Arbeit/Fortschritt
    (1699, 9), (1699, 7), (1699, 13), (1699, 17),

    # A1700 - Clay Bavor: AI vor Kunden ist Designproblem - Arbeit
    (1700, 9), (1700, 13), (1700, 17),

    # A1701 - Clay Bavor: Couch selbst bauen vs kaufen - Arbeit
    (1701, 9), (1701, 15), (1701, 19),

    # A1702 - Clay Bavor: Beste Erfahrung ist Konversation - Gesellschaft/Arbeit
    (1702, 5), (1702, 9), (1702, 13), (1702, 17),

    # A1703 - Clay Bavor: Immersive Computing - Fortschritt
    (1703, 7), (1703, 13), (1703, 17),

    # A1704 - Clay Bavor: Technologie schafft Möglichkeit, Kreativität Wert - Ethik/Fortschritt
    (1704, 4), (1704, 7), (1704, 13), (1704, 17),

    # A1705 - Clay Bavor: Markenstimme und Werte einfangen - Arbeit/Ethik
    (1705, 9), (1705, 4), (1705, 13), (1705, 17),

    # A1706 - Clay Bavor: Null Prozent kennen VR - Fortschritt/Gesellschaft
    (1706, 7), (1706, 5), (1706, 14), (1706, 18)
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {len(codes)} Kodierungen fuer P71-P80 (Aussagen A1346-A1706)")
conn.close()
