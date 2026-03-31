import sqlite3

# Kodierungen für P81-P90 (Aussagen 1509-1921)
# Format: (aussage_id, kategorie_id)

codes = [
    # P81: Martin Casado (1509-1526)
    (1509, 2), (1509, 8), (1509, 14),  # Selbstbild (VC-bias), Macht, Pessimistisch
    (1510, 11), (1510, 22), (1510, 14),  # Regulierung (skeptisch), Epistemik, Pessimistisch
    (1511, 7), (1511, 22), (1511, 13), (1511, 18),  # Fortschritt, Epistemik (real), Optimistisch, Empirisch
    (1512, 11), (1512, 8), (1512, 14),  # Regulierung (Präzedenzfall), Macht, Pessimistisch
    (1513, 9), (1513, 3), (1513, 13), (1513, 19),  # Arbeit/Wirtschaft, Menschenbild (Wert), Optimistisch, Anekdotisch
    (1514, 2), (1514, 7), (1514, 13),  # Selbstbild (Ziel), Fortschritt, Optimistisch
    (1515, 5), (1515, 7), (1515, 8), (1515, 14), (1515, 16),  # Gesellschaft (China), Fortschritt, Macht, Pessimistisch, Politisch
    (1516, 5), (1516, 8), (1516, 14), (1516, 16),  # Gesellschaft, Macht, Pessimistisch, Politisch
    (1517, 9), (1517, 7), (1517, 14), (1517, 18),  # Arbeit/Wirtschaft, Fortschritt, Pessimistisch, Empirisch
    (1518, 11), (1518, 5), (1518, 8), (1518, 14), (1518, 16),  # Regulierung, Gesellschaft, Macht, Pessimistisch, Politisch
    (1519, 11), (1519, 7), (1519, 13), (1519, 16),  # Regulierung (gegen), Fortschritt, Optimistisch, Politisch
    (1520, 7), (1520, 9), (1520, 15),  # Fortschritt (Open Source), Arbeit, Ambivalent
    (1521, 7), (1521, 9), (1521, 13),  # Fortschritt, Arbeit, Optimistisch
    (1522, 1), (1522, 22), (1522, 15), (1522, 17),  # Weltvision (AGI-Debatte), Epistemik, Ambivalent, Philosophisch
    (1523, 5), (1523, 9), (1523, 14), (1523, 18),  # Gesellschaft (China), Arbeit, Pessimistisch, Empirisch
    (1524, 7), (1524, 6), (1524, 14), (1524, 16),  # Fortschritt, Risiko, Pessimistisch, Politisch
    (1525, 7), (1525, 11), (1525, 13), (1525, 16),  # Fortschritt, Regulierung, Optimistisch, Politisch
    (1526, 9), (1526, 1), (1526, 13), (1526, 18),  # Arbeit (Wert-Shift), Weltvision, Optimistisch, Empirisch

    # P82: Daphne Koller (1594-1611)
    (1594, 7), (1594, 3), (1594, 13),  # Fortschritt (AI löst Probleme), Menschenbild, Optimistisch
    (1595, 6), (1595, 4), (1595, 15), (1595, 18),  # Risiko (Sicherheit), Ethik, Ambivalent, Empirisch
    (1596, 3), (1596, 10), (1596, 13), (1596, 17),  # Menschenbild, Transhumanismus (Partnership), Optimistisch, Philosophisch
    (1597, 7), (1597, 3), (1597, 13), (1597, 17),  # Fortschritt, Menschenbild, Optimistisch, Philosophisch
    (1598, 7), (1598, 1), (1598, 13),  # Fortschritt, Weltvision, Optimistisch
    (1599, 11), (1599, 7), (1599, 15),  # Regulierung, Fortschritt, Ambivalent
    (1600, 5), (1600, 4), (1600, 13),  # Gesellschaft (Bildung), Ethik, Optimistisch
    (1601, 3), (1601, 10), (1601, 13), (1601, 17),  # Menschenbild, Transhumanismus (amplify), Optimistisch, Philosophisch
    (1602, 4), (1602, 5), (1602, 13), (1602, 16),  # Ethik (Bildung), Gesellschaft, Optimistisch, Politisch
    (1603, 5), (1603, 4), (1603, 13),  # Gesellschaft (Bildung), Ethik, Optimistisch
    (1604, 3), (1604, 4), (1604, 13), (1604, 17),  # Menschenbild (Geist), Ethik, Optimistisch, Philosophisch
    (1605, 5), (1605, 4), (1605, 13), (1605, 16),  # Gesellschaft, Ethik, Optimistisch, Politisch
    (1606, 5), (1606, 4), (1606, 13),  # Gesellschaft (Bildung), Ethik, Optimistisch
    (1607, 22), (1607, 7), (1607, 13), (1607, 18),  # Epistemik (ML sieht mehr), Fortschritt, Optimistisch, Empirisch
    (1608, 22), (1608, 18), (1608, 15),  # Epistemik (Krankheit), Empirisch, Ambivalent
    (1609, 22), (1609, 3), (1609, 13), (1609, 18),  # Epistemik (ML>Mensch), Menschenbild, Optimistisch, Empirisch
    (1610, 22), (1610, 7), (1610, 13), (1610, 18),  # Epistemik (Daten), Fortschritt, Optimistisch, Empirisch
    (1611, 7), (1611, 9), (1611, 13),  # Fortschritt, Arbeit (Partnership), Optimistisch

    # P83: Adam D'Angelo (1612-1630)
    (1612, 1), (1612, 7), (1612, 13), (1612, 12),  # Weltvision (AGI), Fortschritt, Optimistisch, Existenziell
    (1613, 1), (1613, 7), (1613, 13),  # Weltvision (AGI), Fortschritt, Optimistisch
    (1614, 7), (1614, 13), (1614, 16),  # Fortschritt, Optimistisch, Politisch (Klima)
    (1615, 6), (1615, 8), (1615, 13),  # Risiko (Verteidigung), Macht, Optimistisch
    (1616, 22), (1616, 3), (1616, 13),  # Epistemik (Wissen), Menschenbild, Optimistisch
    (1617, 22), (1617, 3), (1617, 13), (1617, 17),  # Epistemik, Menschenbild, Optimistisch, Philosophisch
    (1618, 22), (1618, 5), (1618, 14),  # Epistemik (Wissen-Zugang), Gesellschaft, Pessimistisch
    (1619, 2), (1619, 7), (1619, 15), (1619, 19),  # Selbstbild, Fortschritt, Ambivalent, Anekdotisch
    (1620, 22), (1620, 4), (1620, 13),  # Epistemik (Quelle), Ethik, Optimistisch
    (1621, 7), (1621, 13),  # Fortschritt (exponential), Optimistisch
    (1622, 2), (1622, 7), (1622, 13),  # Selbstbild, Fortschritt (AGI), Optimistisch
    (1623, 2), (1623, 8), (1623, 15),  # Selbstbild (Grenzen), Macht, Ambivalent
    (1624, 7), (1624, 9), (1624, 13),  # Fortschritt (Ökosystem), Arbeit, Optimistisch
    (1625, 9), (1625, 7), (1625, 13),  # Arbeit (Monetarisierung), Fortschritt, Optimistisch
    (1626, 7), (1626, 3), (1626, 13), (1626, 17),  # Fortschritt, Menschenbild (Vernetzung), Optimistisch, Philosophisch
    (1627, 7), (1627, 9), (1627, 13), (1627, 18),  # Fortschritt, Arbeit, Optimistisch, Empirisch
    (1628, 8), (1628, 3), (1628, 13),  # Macht (Kontrolle aufgeben), Menschenbild, Optimistisch
    (1629, 22), (1629, 5), (1629, 13),  # Epistemik (Wissenszugang), Gesellschaft, Optimistisch
    (1630, 2), (1630, 13),  # Selbstbild (Langfristigkeit), Optimistisch

    # P84: Brett Adcock (1631-1648)
    (1631, 1), (1631, 10), (1631, 13), (1631, 12),  # Weltvision (neue Spezies), Transhumanismus, Optimistisch, Existenziell
    (1632, 1), (1632, 7), (1632, 13),  # Weltvision, Fortschritt (Roboter+AGI), Optimistisch
    (1633, 9), (1633, 3), (1633, 13),  # Arbeit (optional), Menschenbild, Optimistisch
    (1634, 1), (1634, 7), (1634, 13),  # Weltvision (Goldilocks), Fortschritt, Optimistisch
    (1635, 1), (1635, 10), (1635, 13), (1635, 12),  # Weltvision (Space), Transhumanismus (von Neumann), Optimistisch, Existenziell
    (1636, 9), (1636, 22), (1636, 14), (1636, 18),  # Arbeit (Teleoperation), Epistemik, Pessimistisch, Empirisch
    (1637, 2), (1637, 7), (1637, 13),  # Selbstbild (Durchbruch), Fortschritt, Optimistisch
    (1638, 7), (1638, 22), (1638, 13), (1638, 18),  # Fortschritt (vertikale Integration), Epistemik, Optimistisch, Empirisch
    (1639, 2), (1639, 8), (1639, 13),  # Selbstbild (Unabhängigkeit), Macht, Optimistisch
    (1640, 1), (1640, 7), (1640, 13),  # Weltvision (Milliarden Roboter), Fortschritt, Optimistisch
    (1641, 9), (1641, 5), (1641, 13),  # Arbeit (Arbeitskrise), Gesellschaft, Optimistisch
    (1642, 1), (1642, 7), (1642, 13),  # Weltvision (AGI), Fortschritt, Optimistisch
    (1643, 1), (1643, 7), (1643, 13),  # Weltvision (Revolution), Fortschritt, Optimistisch
    (1644, 7), (1644, 22), (1644, 13),  # Fortschritt (Autonomie), Epistemik, Optimistisch
    (1645, 3), (1645, 10), (1645, 13),  # Menschenbild (Companion), Transhumanismus, Optimistisch
    (1646, 9), (1646, 1), (1646, 13),  # Arbeit (50% Roboter), Weltvision, Optimistisch
    (1647, 4), (1647, 10), (1647, 13),  # Ethik (care), Transhumanismus, Optimistisch
    (1648, 1), (1648, 10), (1648, 13), (1648, 12),  # Weltvision (Galaxie), Transhumanismus, Optimistisch, Existenziell

    # P85: Navrina Singh (1707-1726)
    (1707, 2), (1707, 4), (1707, 11), (1707, 13),  # Selbstbild (Mission), Ethik, Regulierung (Governance), Optimistisch
    (1708, 11), (1708, 4), (1708, 13),  # Regulierung (Governance), Ethik, Optimistisch
    (1709, 2), (1709, 4), (1709, 13),  # Selbstbild, Ethik (Trust), Optimistisch
    (1710, 4), (1710, 11), (1710, 13), (1710, 17),  # Ethik, Regulierung, Optimistisch, Philosophisch
    (1711, 5), (1711, 11), (1711, 4), (1711, 13),  # Gesellschaft (Ökosystem), Regulierung, Ethik, Optimistisch
    (1712, 5), (1712, 6), (1712, 11), (1712, 14), (1712, 16),  # Gesellschaft (USA-China), Risiko, Regulierung, Pessimistisch, Politisch
    (1713, 11), (1713, 4), (1713, 13),  # Regulierung (Governance≠Regulation), Ethik, Optimistisch
    (1714, 9), (1714, 4), (1714, 13),  # Arbeit (Trust), Ethik, Optimistisch
    (1715, 11), (1715, 4), (1715, 13),  # Regulierung (Governance), Ethik, Optimistisch
    (1716, 6), (1716, 11), (1716, 13),  # Risiko, Regulierung, Optimistisch
    (1717, 7), (1717, 4), (1717, 15),  # Fortschritt (exhilarated), Ethik (Verantwortung), Ambivalent
    (1718, 4), (1718, 11), (1718, 13),  # Ethik (Fairness), Regulierung, Optimistisch
    (1719, 4), (1719, 11), (1719, 13),  # Ethik (Transparenz), Regulierung, Optimistisch
    (1720, 11), (1720, 22), (1720, 13),  # Regulierung (Index), Epistemik, Optimistisch
    (1721, 2), (1721, 4), (1721, 13),  # Selbstbild (Mission), Ethik, Optimistisch
    (1722, 4), (1722, 11), (1722, 13),  # Ethik (Responsible AI), Regulierung, Optimistisch
    (1723, 5), (1723, 2), (1723, 13),  # Gesellschaft (Frauen), Selbstbild, Optimistisch
    (1724, 5), (1724, 9), (1724, 13),  # Gesellschaft (Innovation), Arbeit, Optimistisch
    (1725, 5), (1725, 4), (1725, 13),  # Gesellschaft (Ökosystem), Ethik, Optimistisch
    (1726, 7), (1726, 11), (1726, 14), (1726, 16),  # Fortschritt, Regulierung (Governance pace), Pessimistisch, Politisch

    # P86: Rene Haas (1727-1744)
    (1727, 7), (1727, 13),  # Fortschritt (profound), Optimistisch
    (1728, 7), (1728, 13), (1728, 18),  # Fortschritt (Tipping point), Optimistisch, Empirisch
    (1729, 4), (1729, 5), (1729, 15),  # Ethik, Gesellschaft, Ambivalent
    (1730, 7), (1730, 22), (1730, 13),  # Fortschritt (nicht overhyped), Epistemik, Optimistisch
    (1731, 7), (1731, 13),  # Fortschritt (AI agents lokal), Optimistisch
    (1732, 7), (1732, 13),  # Fortschritt (schnell), Optimistisch
    (1733, 7), (1733, 5), (1733, 13),  # Fortschritt (Nachhaltigkeit), Gesellschaft, Optimistisch
    (1734, 7), (1734, 9), (1734, 13),  # Fortschritt (Effizienz), Arbeit, Optimistisch
    (1735, 7), (1735, 13),  # Fortschritt (Energie), Optimistisch
    (1736, 7), (1736, 13),  # Fortschritt (Edge AI), Optimistisch
    (1737, 6), (1737, 5), (1737, 14), (1737, 18),  # Risiko (Energie), Gesellschaft, Pessimistisch, Empirisch
    (1738, 1), (1738, 7), (1738, 13),  # Weltvision (exceed century), Fortschritt, Optimistisch
    (1739, 4), (1739, 3), (1739, 13),  # Ethik (Fehler akzeptieren), Menschenbild, Optimistisch
    (1740, 3), (1740, 2), (1740, 13),  # Menschenbild (Neugierde), Selbstbild, Optimistisch
    (1741, 7), (1741, 9), (1741, 13),  # Fortschritt (Arm), Arbeit, Optimistisch
    (1742, 9), (1742, 13),  # Arbeit (fab), Optimistisch
    (1743, 7), (1743, 13),  # Fortschritt (Effizienz), Optimistisch
    (1744, 9), (1744, 2), (1744, 13), (1744, 19),  # Arbeit (IPO), Selbstbild, Optimistisch, Anekdotisch

    # P87: Jimmy Ba (1764-1773)
    (1764, 1), (1764, 10), (1764, 13),  # Weltvision (humanlike), Transhumanismus, Optimistisch
    (1765, 4), (1765, 11), (1765, 15),  # Ethik, Regulierung, Ambivalent
    (1766, 7), (1766, 9), (1766, 13),  # Fortschritt (100x), Arbeit, Optimistisch
    (1767, 10), (1767, 7), (1767, 13), (1767, 12),  # Transhumanismus (recursive), Fortschritt, Optimistisch, Existenziell
    (1768, 1), (1768, 7), (1768, 13), (1768, 12),  # Weltvision (most consequential), Fortschritt, Optimistisch, Existenziell
    (1769, 2), (1769, 15),  # Selbstbild (Recalibrate), Ambivalent
    (1770, 10), (1770, 3), (1770, 13), (1770, 17),  # Transhumanismus (Maschinen), Menschenbild, Optimistisch, Philosophisch
    (1771, 2), (1771, 13), (1771, 19),  # Selbstbild (xAI), Optimistisch, Anekdotisch
    (1772, 2), (1772, 13), (1772, 19),  # Selbstbild (cofounder), Optimistisch, Anekdotisch
    (1773, 22), (1773, 7), (1773, 15), (1773, 18),  # Epistemik (LLM Limits), Fortschritt, Ambivalent, Empirisch

    # P88: Sarah Guo (1774-1791)
    (1774, 1), (1774, 9), (1774, 13),  # Weltvision (value creation), Arbeit, Optimistisch
    (1775, 7), (1775, 1), (1775, 13), (1775, 17),  # Fortschritt (Software 3.0), Weltvision, Optimistisch, Philosophisch
    (1776, 9), (1776, 7), (1776, 13),  # Arbeit (Execution), Fortschritt, Optimistisch
    (1777, 7), (1777, 9), (1777, 13),  # Fortschritt (Code), Arbeit, Optimistisch
    (1778, 11), (1778, 5), (1778, 13), (1778, 16),  # Regulierung (gegen), Gesellschaft, Optimistisch, Politisch
    (1779, 22), (1779, 9), (1779, 14),  # Epistemik (skeptisch), Arbeit, Pessimistisch
    (1780, 9), (1780, 7), (1780, 13),  # Arbeit (Wert), Fortschritt, Optimistisch
    (1781, 3), (1781, 9), (1781, 13),  # Menschenbild (Produktivität), Arbeit, Optimistisch
    (1782, 7), (1782, 1), (1782, 13), (1782, 18),  # Fortschritt, Weltvision (special moment), Optimistisch, Empirisch
    (1783, 9), (1783, 10), (1783, 13), (1783, 17),  # Arbeit (hire it), Transhumanismus, Optimistisch, Philosophisch
    (1784, 7), (1784, 11), (1784, 13),  # Fortschritt (Open Source), Regulierung, Optimistisch
    (1785, 22), (1785, 3), (1785, 13), (1785, 17),  # Epistemik (Wahrheit), Menschenbild, Optimistisch, Philosophisch
    (1786, 4), (1786, 5), (1786, 9), (1786, 13), (1786, 16),  # Ethik, Gesellschaft, Arbeit, Optimistisch, Politisch
    (1787, 7), (1787, 9), (1787, 13), (1787, 18),  # Fortschritt, Arbeit, Optimistisch, Empirisch
    (1788, 7), (1788, 9), (1788, 13), (1788, 18),  # Fortschritt (Agentic), Arbeit, Optimistisch, Empirisch
    (1789, 7), (1789, 9), (1789, 13),  # Fortschritt (StackBlitz), Arbeit, Optimistisch
    (1790, 5), (1790, 8), (1790, 14), (1790, 16),  # Gesellschaft (China), Macht, Pessimistisch, Politisch
    (1791, 2), (1791, 7), (1791, 13),  # Selbstbild (Bet), Fortschritt, Optimistisch

    # P89: Igor Babuschkin (1847-1864)
    (1847, 10), (1847, 7), (1847, 13),  # Transhumanismus (beyond humans), Fortschritt, Optimistisch
    (1848, 1), (1848, 12), (1848, 13), (1848, 17),  # Weltvision (mind), Existenziell, Optimistisch, Philosophisch
    (1849, 2), (1849, 4), (1849, 13), (1849, 12),  # Selbstbild (dream), Ethik, Optimistisch, Existenziell
    (1850, 4), (1850, 10), (1850, 13), (1850, 17),  # Ethik (elevate), Transhumanismus, Optimistisch, Philosophisch
    (1851, 2), (1851, 4), (1851, 13), (1851, 19),  # Selbstbild (Elon), Ethik, Optimistisch, Anekdotisch
    (1852, 1), (1852, 10), (1852, 13), (1852, 12),  # Weltvision (Singularity), Transhumanismus, Optimistisch, Existenziell
    (1853, 6), (1853, 11), (1853, 13),  # Risiko (Safety), Regulierung, Optimistisch
    (1854, 7), (1854, 2), (1854, 13), (1854, 19),  # Fortschritt (ludicrous speed), Selbstbild, Optimistisch, Anekdotisch
    (1855, 2), (1855, 8), (1855, 13), (1855, 19),  # Selbstbild (Lessons), Macht, Optimistisch, Anekdotisch
    (1856, 2), (1856, 19), (1856, 13),  # Selbstbild, Anekdotisch, Optimistisch
    (1857, 6), (1857, 4), (1857, 13), (1857, 19),  # Risiko (Safety), Ethik, Optimistisch, Anekdotisch
    (1858, 7), (1858, 13), (1858, 18),  # Fortschritt (Colossus), Optimistisch, Empirisch
    (1859, 3), (1859, 13), (1859, 21),  # Menschenbild (Freunde), Optimistisch, Humor
    (1860, 2), (1860, 6), (1860, 4), (1860, 13),  # Selbstbild (Ventures), Risiko (Safety), Ethik, Optimistisch
    (1861, 7), (1861, 13), (1861, 18),  # Fortschritt (H100 cluster), Optimistisch, Empirisch
    (1862, 2), (1862, 7), (1862, 13),  # Selbstbild (dream), Fortschritt, Optimistisch
    (1863, 7), (1863, 18), (1863, 13), (1863, 25),  # Fortschritt (WaveNet), Empirisch, Optimistisch, Biografie
    (1864, 7), (1864, 18), (1864, 13), (1864, 25),  # Fortschritt (Agentic), Empirisch, Optimistisch, Biografie

    # P90: Karol Hausman (1903-1921)
    (1903, 10), (1903, 7), (1903, 13),  # Transhumanismus (generalist brain), Fortschritt, Optimistisch
    (1904, 7), (1904, 22), (1904, 13), (1904, 18),  # Fortschritt (bottleneck), Epistemik, Optimistisch, Empirisch
    (1905, 10), (1905, 22), (1905, 13), (1905, 18),  # Transhumanismus (brain), Epistemik, Optimistisch, Empirisch
    (1906, 7), (1906, 22), (1906, 13), (1906, 18),  # Fortschritt (mind-blowing), Epistemik, Optimistisch, Empirisch
    (1907, 22), (1907, 18), (1907, 14),  # Epistemik (no data), Empirisch, Pessimistisch
    (1908, 3), (1908, 10), (1908, 13), (1908, 17),  # Menschenbild (Lernen), Transhumanismus, Optimistisch, Philosophisch
    (1909, 6), (1909, 11), (1909, 15),  # Risiko (Privacy), Regulierung, Ambivalent
    (1910, 7), (1910, 9), (1910, 13), (1910, 18),  # Fortschritt (VLM+LLM), Arbeit, Optimistisch, Empirisch
    (1911, 4), (1911, 11), (1911, 13), (1911, 21),  # Ethik (Asimov), Regulierung, Optimistisch, Humor
    (1912, 1), (1912, 7), (1912, 13),  # Weltvision (year of robotics), Fortschritt, Optimistisch
    (1913, 7), (1913, 18), (1913, 13),  # Fortschritt (laundry), Empirisch, Optimistisch
    (1914, 10), (1914, 22), (1914, 13), (1914, 18),  # Transhumanismus (inner monologue), Epistemik, Optimistisch, Empirisch
    (1915, 7), (1915, 18), (1915, 13),  # Fortschritt (closed-loop), Empirisch, Optimistisch
    (1916, 7), (1916, 22), (1916, 13), (1916, 18),  # Fortschritt (RT-2), Epistemik, Optimistisch, Empirisch
    (1917, 7), (1917, 18), (1917, 13),  # Fortschritt (task generalization), Empirisch, Optimistisch
    (1918, 7), (1918, 22), (1918, 13), (1918, 18),  # Fortschritt (AutoRT), Epistemik, Optimistisch, Empirisch
    (1919, 10), (1919, 7), (1919, 13), (1919, 18),  # Transhumanismus (π0), Fortschritt, Optimistisch, Empirisch
    (1920, 7), (1920, 22), (1920, 13), (1920, 18),  # Fortschritt (AutoRT data), Epistemik, Optimistisch, Empirisch
    (1921, 22), (1921, 18), (1921, 13),  # Epistemik (not scripted), Empirisch, Optimistisch
]

# Verbindung zur Datenbank
conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Einfügen der Kodierungen
c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()

print(f"Eingefuegt: {c.rowcount} Kodierungen fuer P81-P90")
print(f"Gesamtzahl der Kodierungen: {len(codes)}")

# Statistik der Kodierungen pro Person
c.execute("""
SELECT p.name, COUNT(DISTINCT ak.aussage_id) as anzahl_aussagen, COUNT(ak.kategorie_id) as anzahl_codes
FROM personen p
JOIN aussagen a ON p.id = a.person_id
JOIN aussagen_kategorien ak ON a.id = ak.aussage_id
WHERE p.id BETWEEN 81 AND 90
GROUP BY p.id
ORDER BY p.id
""")

print("\nStatistik pro Person:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]} Aussagen, {row[2]} Codes")

conn.close()
