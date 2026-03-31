import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierungen für P91 (Soumith Chintala) - P100 (Dorsa Sadigh)
codes = [
    # A1792: PyTorch Erfolg, Demokratisierung - Fortschritt, Gesellschaft, optimistisch
    (1792, 7), (1792, 5), (1792, 13),

    # A1793: Will nicht ewig an PyTorch arbeiten - Selbstbild, ambivalent
    (1793, 2), (1793, 15),

    # A1794: Bedürfnis etwas Neues zu probieren - Selbstbild, ambivalent
    (1794, 2), (1794, 15),

    # A1795: Schwer zu verlassen, leveraged Position - Macht, Selbstbild, ambivalent
    (1795, 8), (1795, 2), (1795, 15),

    # A1796: Suche nach Neuem, Unbekanntem - Selbstbild, optimistisch
    (1796, 2), (1796, 13),

    # A1797: Skalierungshypothese, Unsicherheit über Sättigung - Epistemik, ambivalent, empirisch
    (1797, 22), (1797, 15), (1797, 18),

    # A1798: Open Source demokratisiert - Gesellschaft, optimistisch
    (1798, 5), (1798, 13),

    # A1799: Rechte in Frage gestellt durch KI - Ethik, Gesellschaft, ambivalent, philosophisch
    (1799, 4), (1799, 5), (1799, 15), (1799, 17),

    # A1800: Wir bauen gehorsame Studenten, keine Revolutionäre - Menschenbild, Macht, pessimistisch
    (1800, 3), (1800, 8), (1800, 14),

    # A1801: Open Source AI = vertrauenswürdige AI - Ethik, Regulierung, optimistisch
    (1801, 4), (1801, 11), (1801, 13),

    # A1802: Liebe zu Open Source aus Gründen der Chancengleichheit - Selbstbild, Gesellschaft, optimistisch
    (1802, 2), (1802, 5), (1802, 13),

    # A1803: Open Source verteilt Chancen - Gesellschaft, optimistisch
    (1803, 5), (1803, 13),

    # A1804: PyTorch Foundation - Regulierung, neutral announcement
    (1804, 11), (1804, 15),

    # A1805: Empfehlung für offene Forschung - Ethik, Gesellschaft, optimistisch
    (1805, 4), (1805, 5), (1805, 13),

    # A1806: PyTorch Design Origins - technisch, neutral
    (1806, 7), (1806, 15),

    # A1807: PyTorch Nutzungsstatistiken - Fortschritt, optimistisch, empirisch
    (1807, 7), (1807, 13), (1807, 18),

    # A1808: AI lässt uns alles überdenken - Weltvision, ambivalent
    (1808, 1), (1808, 15),

    # A1809: Transparente Business-Entscheidungen - Ethik, Regulierung, optimistisch
    (1809, 4), (1809, 11), (1809, 13),

    # A1828: Kein künstliche ohne echte Intelligenz - Menschenbild, philosophisch, ambivalent
    (1828, 3), (1828, 17), (1828, 15),

    # A1829: Maschineninhalt erhöht Wert menschlichen Inhalts - Menschenbild, Gesellschaft, optimistisch
    (1829, 3), (1829, 5), (1829, 13),

    # A1830: Reddit = menschlichster Ort im Internet - Gesellschaft, optimistisch
    (1830, 5), (1830, 13),

    # A1831: Weltende-Vorbereitung (Kontaktlinsen) - Risiko, Sicherheit, pessimistisch, anekdotisch
    (1831, 6), (1831, 14), (1831, 19),

    # A1832: Gesellschaft basiert auf Glauben - Weltvision, Gesellschaft, ambivalent, philosophisch
    (1832, 1), (1832, 5), (1832, 15), (1832, 17),

    # A1833: Motorrad für Katastrophenfall - Risiko, pessimistisch, anekdotisch
    (1833, 6), (1833, 14), (1833, 19),

    # A1834: Reddit nicht als free speech Bastion - Ethik, ambivalent
    (1834, 4), (1834, 15),

    # A1835: Reddit für authentische Gespräche - Menschenbild, Gesellschaft, optimistisch
    (1835, 3), (1835, 5), (1835, 13),

    # A1836: Nicht Gedankenpolizei aber Verhalten wichtig - Ethik, Regulierung, ambivalent
    (1836, 4), (1836, 11), (1836, 15),

    # A1837: Vererbte Moderatorenpositionen nicht demokratisch - Gesellschaft, Macht, pessimistisch
    (1837, 5), (1837, 8), (1837, 14),

    # A1838: Mehr Demokratie als Lösung - Gesellschaft, optimistisch
    (1838, 5), (1838, 13),

    # A1839: Reddit nicht für third-party apps designed - technisch, ambivalent
    (1839, 9), (1839, 15),

    # A1840: WallStreetBets hebt wichtige Fragen auf - Gesellschaft, Arbeit/Wirtschaft, optimistisch
    (1840, 5), (1840, 9), (1840, 13),

    # A1841: WallStreetBets ist echte Community - Gesellschaft, optimistisch
    (1841, 5), (1841, 13),

    # A1842: Liebe zu WallStreetBets - Selbstbild, optimistisch, anekdotisch
    (1842, 2), (1842, 13), (1842, 19),

    # A1843: Wenn ich es mag, mögen es Millionen - Selbstbild, Epistemik, optimistisch
    (1843, 2), (1843, 22), (1843, 13),

    # A1844: CEO sollte nicht solche Spiele spielen - Selbstbild, Ethik, ambivalent
    (1844, 2), (1844, 4), (1844, 15),

    # A1845: Wünschte Reddit noch zu besitzen - Selbstbild, ambivalent, anekdotisch
    (1845, 2), (1845, 15), (1845, 19),

    # A1846: Helfen ohne zu fordern - Ethik, Selbstbild, optimistisch
    (1846, 4), (1846, 2), (1846, 13),

    # A1865: 2024 Jahr der Aktion - Fortschritt, optimistisch, prognose
    (1865, 7), (1865, 13), (1865, 20),

    # A1866: Geschwindigkeit ist erschreckend - Risiko, pessimistisch
    (1866, 6), (1866, 14),

    # A1867: Zentrale AI nicht mit zentraler AI schlagen - Macht, Gesellschaft, ambivalent
    (1867, 8), (1867, 5), (1867, 15),

    # A1868: AI Ambivalenz - schlechtes/gutes Szenario - Weltvision, Risiko, ambivalent
    (1868, 1), (1868, 6), (1868, 15),

    # A1869: Empathie durch AI, universal basic AI - Menschenbild, Gesellschaft, optimistisch, philosophisch
    (1869, 3), (1869, 5), (1869, 13), (1869, 17),

    # A1870: Keine Programmierer in 5 Jahren - Arbeit, pessimistisch, prognose
    (1870, 9), (1870, 14), (1870, 20),

    # A1871: 41% Code AI-generiert - Arbeit, Fortschritt, ambivalent, empirisch
    (1871, 9), (1871, 7), (1871, 15), (1871, 18),

    # A1872: Größte Blase aller Zeiten - Wirtschaft, pessimistisch
    (1872, 9), (1872, 14),

    # A1873: Hat noch nicht begonnen - Fortschritt, ambivalent
    (1873, 7), (1873, 15),

    # A1874: Zentrale AI nicht mit zentraler AI schlagen (Wiederholung) - Macht, ambivalent
    (1874, 8), (1874, 15),

    # A1875: OpenAI blockiert Ukrainer - Ethik, Gesellschaft, pessimistisch
    (1875, 4), (1875, 5), (1875, 14),

    # A1876: Blockierung von Technologie fundamental falsch - Ethik, pessimistisch
    (1876, 4), (1876, 14),

    # A1877: Tipping point in 1000 Tagen - Fortschritt, Arbeit, ambivalent, prognose
    (1877, 7), (1877, 9), (1877, 15), (1877, 20),

    # A1878: Terminal point der Wirtschaftsstruktur - Weltvision, Wirtschaft, pessimistisch, philosophisch
    (1878, 1), (1878, 9), (1878, 14), (1878, 17),

    # A1879: Krebs ist gut für GDP - Wirtschaft, Ethik, pessimistisch, provokant
    (1879, 9), (1879, 4), (1879, 14), (1879, 21),

    # A1880: UBI würde mehr kosten als Steuerbasis - Wirtschaft, pessimistisch, empirisch
    (1880, 9), (1880, 14), (1880, 18),

    # A1881: Jeder Schüler AI-Tutor in 10 Jahren - Gesellschaft, Fortschritt, optimistisch, prognose
    (1881, 5), (1881, 7), (1881, 13), (1881, 20),

    # A1882: Beste Diagnostiker/Chirurgen werden AIs - Fortschritt, Gesellschaft, optimistisch, prognose
    (1882, 7), (1882, 5), (1882, 13), (1882, 20),

    # A1883: Superintelligenz als kollektive Intelligenz - Weltvision, Transhumanismus, optimistisch, philosophisch
    (1883, 1), (1883, 10), (1883, 13), (1883, 17),

    # A1884: Motivation durch autistischen Sohn - Selbstbild, optimistisch, biografisch
    (1884, 2), (1884, 13), (1884, 25),

    # A1885: Neuronale Netze schwer zu designen - Epistemik, ambivalent, empirisch
    (1885, 22), (1885, 15), (1885, 18),

    # A1886: Algorithmus kann neuartige Architekturen designen - Fortschritt, optimistisch, empirisch
    (1886, 7), (1886, 13), (1886, 18),

    # A1887: Verlassen von OpenAI - Selbstbild, ambivalent, biografisch
    (1887, 2), (1887, 15), (1887, 25),

    # A1888: Natürlicher Punkt neue Chancen zu erkunden - Selbstbild, optimistisch
    (1888, 2), (1888, 13),

    # A1889: Trennung von Barret Zoph - neutral
    (1889, 2), (1889, 15),

    # A1890: Konnte menschliche Performance matchen - Fortschritt, optimistisch, empirisch
    (1890, 7), (1890, 13), (1890, 18),

    # A1891: ChatGPT als low-key research preview geplant - ambivalent, anekdotisch
    (1891, 15), (1891, 19),

    # A1892: Post-training macht Modell zum Assistant - Fortschritt, optimistisch, empirisch
    (1892, 7), (1892, 13), (1892, 18),

    # A1893: Key contribution: transferability - Fortschritt, optimistisch, empirisch
    (1893, 7), (1893, 13), (1893, 18),

    # A1894: Transfer von kleinem zu großem Dataset - Fortschritt, optimistisch, empirisch
    (1894, 7), (1894, 13), (1894, 18),

    # A1895: Zusammenarbeit seit Sept 2022 für aligned chatbot - Ethik, optimistisch, biografisch
    (1895, 4), (1895, 13), (1895, 25),

    # A1896: Methode 5x effizienter - Fortschritt, optimistisch, empirisch
    (1896, 7), (1896, 13), (1896, 18),

    # A1897: Transfer learning verbessert BLEU - Fortschritt, optimistisch, empirisch
    (1897, 7), (1897, 13), (1897, 18),

    # A1898: Multi-source translation model - Fortschritt, optimistisch, empirisch
    (1898, 7), (1898, 13), (1898, 18),

    # A1899: AutoAugment für data augmentation - Fortschritt, optimistisch, empirisch
    (1899, 7), (1899, 13), (1899, 18),

    # A1900: Sparse model auf 269B Parameter skaliert - Fortschritt, optimistisch, empirisch
    (1900, 7), (1900, 13), (1900, 18),

    # A1901: State-of-the-art über diverse Tasks - Fortschritt, optimistisch, empirisch
    (1901, 7), (1901, 13), (1901, 18),

    # A1902: GPT-4 safety reward signal - Ethik, Regulierung, optimistisch, empirisch
    (1902, 4), (1902, 11), (1902, 13), (1902, 18),

    # A1962: AI als force multiplier - Menschenbild, Fortschritt, optimistisch
    (1962, 3), (1962, 7), (1962, 13),

    # A1963: Technologie muss Leben verbessern - Ethik, Weltvision, optimistisch, philosophisch
    (1963, 4), (1963, 1), (1963, 13), (1963, 17),

    # A1964: AI ändert Bewertung menschlicher Intelligenz - Epistemik, Menschenbild, ambivalent, philosophisch
    (1964, 22), (1964, 3), (1964, 15), (1964, 17),

    # A1965: Demokratisierung von AI-Tools - Gesellschaft, Ethik, optimistisch
    (1965, 5), (1965, 4), (1965, 13),

    # A1966: Sehr besorgt über capability gaps zu Google - Risiko, Macht, pessimistisch, empirisch
    (1966, 6), (1966, 8), (1966, 14), (1966, 18),

    # A1967: Jahre hinter Konkurrenz - Risiko, Macht, pessimistisch, empirisch
    (1967, 6), (1967, 8), (1967, 14), (1967, 18),

    # A1968: Nicht bei diminishing returns bei scale-up - Epistemik, Fortschritt, optimistisch, empirisch
    (1968, 22), (1968, 7), (1968, 13), (1968, 18),

    # A1969: LLMs werden besser und genereller - Fortschritt, optimistisch, prognose
    (1969, 7), (1969, 13), (1969, 20),

    # A1970: Gleichberechtigter Technologiezugang, Breitband - Gesellschaft, optimistisch
    (1970, 5), (1970, 13),

    # A1971: AI muss demokratisiert werden - Gesellschaft, Ethik, optimistisch
    (1971, 5), (1971, 4), (1971, 13),

    # A1972: Menschen/Maschinen unterschiedliche Stärken - Menschenbild, ambivalent, empirisch
    (1972, 3), (1972, 15), (1972, 18),

    # A1973: Mehr Wandel in nächsten 40 Jahren - Weltvision, Fortschritt, optimistisch, prognose
    (1973, 1), (1973, 7), (1973, 13), (1973, 20),

    # A1974: Partnership mit OpenAI als Wette - Macht, ambivalent, biografisch
    (1974, 8), (1974, 15), (1974, 25),

    # A1975: Copilot eliminiert Langeweile - Arbeit, optimistisch, empirisch
    (1975, 9), (1975, 13), (1975, 18),

    # A1976: Copilot dramatisch positiver Einfluss - Arbeit, Fortschritt, optimistisch, empirisch
    (1976, 9), (1976, 7), (1976, 13), (1976, 18),

    # A1977: 95% neuer Code AI-generiert in 5 Jahren - Arbeit, Fortschritt, optimistisch, prognose
    (1977, 9), (1977, 7), (1977, 13), (1977, 20),

    # A1978: Agentic web, offenes Internet - Weltvision, Gesellschaft, optimistisch
    (1978, 1), (1978, 5), (1978, 13),

    # A1979: Technologie nutzt massiv der Gesellschaft - Weltvision, Gesellschaft, optimistisch, philosophisch
    (1979, 1), (1979, 5), (1979, 13), (1979, 17),

    # A1980: Massive crunch bei Kapazität - Risiko, ambivalent, empirisch
    (1980, 6), (1980, 15), (1980, 18),

    # A1981: Constraints bleiben, explodierende Nachfrage - Risiko, Wirtschaft, ambivalent, empirisch
    (1981, 6), (1981, 9), (1981, 15), (1981, 18),

    # A1982: Action Plan beendet AI doomerism - Regulierung, Fortschritt, optimistisch, politisch
    (1982, 11), (1982, 7), (1982, 13), (1982, 16),

    # A1983: Biden Admin von Angst geleitet - Regulierung, pessimistisch, politisch
    (1983, 11), (1983, 14), (1983, 16),

    # A1984: Freier Markt für Innovation - Weltvision, Wirtschaft, optimistisch, politisch
    (1984, 1), (1984, 9), (1984, 13), (1984, 16),

    # A1985: Vier Säulen nationaler Strategie - Regulierung, ambivalent, politisch
    (1985, 11), (1985, 15), (1985, 16),

    # A1986: CCP nutzt Tech für autoritäre Ziele - Macht, Gesellschaft, pessimistisch, politisch
    (1986, 8), (1986, 5), (1986, 14), (1986, 16),

    # A1987: Aufhören China zu subventionieren - Macht, Wirtschaft, pessimistisch, politisch
    (1987, 8), (1987, 9), (1987, 14), (1987, 16),

    # A1988: Export controls, America-first - Regulierung, Macht, ambivalent, politisch
    (1988, 11), (1988, 8), (1988, 15), (1988, 16),

    # A1989: EU enttäuschend - Regulierung, pessimistisch, politisch
    (1989, 11), (1989, 14), (1989, 16),

    # A1990: One-size-fits-all Regulierung = Fehler - Regulierung, pessimistisch
    (1990, 11), (1990, 14),

    # A1991: US zeigt Alternative zu EU - Regulierung, optimistisch, politisch
    (1991, 11), (1991, 13), (1991, 16),

    # A1992: Flickenteppich von Regulierungen anti-innovation - Regulierung, Macht, pessimistisch
    (1992, 11), (1992, 8), (1992, 14),

    # A1993: Technologie manipuliert Zeit/Raum - Fortschritt, optimistisch, philosophisch
    (1993, 7), (1993, 13), (1993, 17),

    # A1994: Regulierung Barriere für Transport - Regulierung, Fortschritt, pessimistisch
    (1994, 11), (1994, 7), (1994, 14),

    # A1995: Schlechte Regulierung abwerfen - Regulierung, Fortschritt, optimistisch, politisch
    (1995, 11), (1995, 7), (1995, 13), (1995, 16),

    # A1996: National AI Initiative Office - Regulierung, optimistisch
    (1996, 11), (1996, 13),

    # A1997: Data center companies arbeiten daran - technisch, ambivalent
    (1997, 15),

    # A1998: Bundesressourcen für AI-Infrastruktur - Regulierung, Fortschritt, optimistisch, politisch
    (1998, 11), (1998, 7), (1998, 13), (1998, 16),

    # A1999: Internationaler Konsens bei OECD - Regulierung, Gesellschaft, optimistisch, politisch
    (1999, 11), (1999, 5), (1999, 13), (1999, 16),

    # A2000: Promote and protect Strategie - Regulierung, Macht, ambivalent, politisch
    (2000, 11), (2000, 8), (2000, 15), (2000, 16),

    # A2001: High-end Chips export control - Regulierung, Macht, ambivalent, politisch
    (2001, 11), (2001, 8), (2001, 15), (2001, 16),

    # A2002: AI trainiert auf menschlicher Expertise/Werten - Menschenbild, Ethik, optimistisch
    (2002, 3), (2002, 4), (2002, 13),

    # A2003: Hasse Begriff data labeling - Selbstbild, Menschenbild, ambivalent, philosophisch
    (2003, 2), (2003, 3), (2003, 15), (2003, 17),

    # A2004: Hemingway vs 10-jährige beim Gedicht - Menschenbild, Epistemik, optimistisch, anekdotisch
    (2004, 3), (2004, 22), (2004, 13), (2004, 19),

    # A2005: AI so gut wie Daten - Epistemik, ambivalent, empirisch
    (2005, 22), (2005, 15), (2005, 18),

    # A2006: Datenqualität #1 constraint - Epistemik, ambivalent, empirisch
    (2006, 22), (2006, 15), (2006, 18),

    # A2007: Wenige gut-gelabelte Beispiele besser - Epistemik, optimistisch, empirisch
    (2007, 22), (2007, 13), (2007, 18),

    # A2008: AI soll warm und kreativ sein - Menschenbild, Ethik, optimistisch
    (2008, 3), (2008, 4), (2008, 13),

    # A2009: Dekade bis AGI - Fortschritt, ambivalent, prognose
    (2009, 7), (2009, 15), (2009, 20),

    # A2010: AGI mit unbeabsichtigten Konsequenzen - Risiko, Weltvision, pessimistisch, prognose
    (2010, 6), (2010, 1), (2010, 14), (2010, 20),

    # A2011: Skeptisch dass AI ohne Menschen auskommt - Menschenbild, Epistemik, optimistisch
    (2011, 3), (2011, 22), (2011, 13),

    # A2012: Menschen als Quality Control für synthetische Daten - Menschenbild, Arbeit, optimistisch
    (2012, 3), (2012, 9), (2012, 13),

    # A2013: Hasse VC Silicon Valley Status quo - Selbstbild, Wirtschaft, pessimistisch
    (2013, 2), (2013, 9), (2013, 14),

    # A2014: Langsam, Politik, Bürokratie - Wirtschaft, pessimistisch
    (2014, 9), (2014, 14),

    # A2015: Froh nicht Silicon Valley Denken zu haben - Selbstbild, optimistisch
    (2015, 2), (2015, 13),

    # A2016: Industrie in falsche Richtung - Wirtschaft, pessimistisch
    (2016, 9), (2016, 14),

    # A2017: Sales optimiert für Deals nicht Probleme - Wirtschaft, Ethik, pessimistisch
    (2017, 9), (2017, 4), (2017, 14),

    # A2018: So gut sein dass Kunden nicht ohne können - Selbstbild, Wirtschaft, optimistisch
    (2018, 2), (2018, 9), (2018, 13),

    # A2019: AI safety nicht Zukunftssorge - Ethik, Risiko, pessimistisch
    (2019, 4), (2019, 6), (2019, 14),

    # A2020: Gesehen wie Produkte Schaden anrichten - Ethik, Risiko, pessimistisch, empirisch
    (2020, 4), (2020, 6), (2020, 14), (2020, 18),

    # A2021: Vielseitige Ingenieure bevorzugt - Selbstbild, Arbeit, optimistisch
    (2021, 2), (2021, 9), (2021, 13),

    # A2022: Gemischte Gefühle beim Verlassen - Selbstbild, ambivalent, biografisch
    (2022, 2), (2022, 15), (2022, 25),

    # A2023: Programmierer im driver's seat - Menschenbild, Arbeit, optimistisch
    (2023, 3), (2023, 9), (2023, 13),

    # A2024: AI soll Programmieren bereichern - Menschenbild, Arbeit, optimistisch
    (2024, 3), (2024, 9), (2024, 13),

    # A2025: AI als Assistant - Menschenbild, Arbeit, optimistisch
    (2025, 3), (2025, 9), (2025, 13),

    # A2026: Technologie schnell, akkurat, menschlich kontrolliert - Ethik, Macht, optimistisch
    (2026, 4), (2026, 8), (2026, 13),

    # A2027: Developer productivity lösen - Arbeit, optimistisch
    (2027, 9), (2027, 13),

    # A2028: Systeme für sicherere AI entwickeln - Ethik, Risiko, optimistisch
    (2028, 4), (2028, 6), (2028, 13),

    # A2029: Mensch-plus-AI Developer Era - Menschenbild, Arbeit, optimistisch
    (2029, 3), (2029, 9), (2029, 13),

    # A2030: Obsession über Details - Selbstbild, optimistisch
    (2030, 2), (2030, 13),

    # A2031: AI verstärkt menschliche Kreativität - Menschenbild, optimistisch
    (2031, 3), (2031, 13),

    # A2032: Robuste Systeme für sichere AI - Ethik, Risiko, optimistisch
    (2032, 4), (2032, 6), (2032, 13),

    # A2033: Schnellster Weg zu $100M ARR - Wirtschaft, optimistisch, empirisch
    (2033, 9), (2033, 13), (2033, 18),

    # A2034: AI erweitert Fähigkeiten statt zu ersetzen - Menschenbild, Arbeit, optimistisch, biografisch
    (2034, 3), (2034, 9), (2034, 13), (2034, 25),

    # A2035: Von competitive programming zu Firma - Selbstbild, biografisch
    (2035, 2), (2035, 25),

    # A2036: Open-source Ethos - Selbstbild, Ethik, optimistisch, biografisch
    (2036, 2), (2036, 4), (2036, 13), (2036, 25),

    # A2037: Technologieführer setzen ethische Normen - Ethik, Macht, optimistisch, philosophisch
    (2037, 4), (2037, 8), (2037, 13), (2037, 17),

    # A2038: Liberale Demokratie, moralischer High Ground - Weltvision, Ethik, optimistisch, philosophisch, politisch
    (2038, 1), (2038, 4), (2038, 13), (2038, 17), (2038, 16),

    # A2039: Defense Tech wurde populär - Gesellschaft, ambivalent, biografisch
    (2039, 5), (2039, 15), (2039, 25),

    # A2040: Prinzipiell und moralisch überzeugt sein - Selbstbild, Ethik, optimistisch, philosophisch
    (2040, 2), (2040, 4), (2040, 13), (2040, 17),

    # A2041: Bedrohung wie Cold War - Risiko, Macht, pessimistisch, politisch
    (2041, 6), (2041, 8), (2041, 14), (2041, 16),

    # A2042: Munition in einer Woche aufgebraucht - Risiko, pessimistisch, empirisch, politisch
    (2042, 6), (2042, 14), (2042, 18), (2042, 16),

    # A2043: Könnte nicht schaden Schrotflinten zu haben - Risiko, pessimistisch, anekdotisch
    (2043, 6), (2043, 14), (2043, 19),

    # A2044: Gott original innovator, Menschen sollen bauen - Weltvision, Menschenbild, optimistisch, spirituell/philosophisch
    (2044, 1), (2044, 3), (2044, 13), (2044, 12), (2044, 17),

    # A2045: Wissenschaft unzureichend für Ethik - Epistemik, Ethik, ambivalent, spirituell/philosophisch
    (2045, 22), (2045, 4), (2045, 15), (2045, 12), (2045, 17),

    # A2046: Easy button für Regierung - Gesellschaft, Regulierung, optimistisch
    (2046, 5), (2046, 11), (2046, 13),

    # A2047: Tech für Gutes und Schlechtes - Ethik, ambivalent
    (2047, 4), (2047, 15),

    # A2048: Just War Prinzipien, präzise Angriffe - Ethik, Risiko, optimistisch, philosophisch
    (2048, 4), (2048, 6), (2048, 13), (2048, 17),

    # A2049: Technologie macht Krieg ethischer - Ethik, Fortschritt, optimistisch, philosophisch
    (2049, 4), (2049, 7), (2049, 13), (2049, 17),

    # A2050: Demokratien sollen führen - Ethik, Macht, optimistisch, politisch
    (2050, 4), (2050, 8), (2050, 13), (2050, 16),

    # A2051: 9/11 inspirierte national security - Selbstbild, biografisch
    (2051, 2), (2051, 25),

    # A2052: Vergebung nützlich in Silicon Valley - Ethik, Selbstbild, optimistisch, spirituell
    (2052, 4), (2052, 2), (2052, 13), (2052, 12),

    # A2053: Ethische Sorge: gute Quests verfolgen - Ethik, Selbstbild, optimistisch, philosophisch
    (2053, 4), (2053, 2), (2053, 13), (2053, 17),

    # A2054: ACTS 17 für Glauben bei Intellektuellen - Spiritualität, Gesellschaft, optimistisch
    (2054, 12), (2054, 5), (2054, 13),

    # A2055: AI/LLMs beeinflussen Robotik durch Hardware - Fortschritt, optimistisch, empirisch
    (2055, 7), (2055, 13), (2055, 18),

    # A2056: Roboter-Foundation Models brauchen mehr Daten - Epistemik, Fortschritt, ambivalent, empirisch
    (2056, 22), (2056, 7), (2056, 15), (2056, 18),

    # A2057: Autonome Autos beeinflussen menschliches Fahrverhalten - Menschenbild, Gesellschaft, optimistisch, empirisch
    (2057, 3), (2057, 5), (2057, 13), (2057, 18),

    # A2058: Shared autonomy, Roboter gewinnt Vertrauen - Menschenbild, Macht, optimistisch, empirisch
    (2058, 3), (2058, 8), (2058, 13), (2058, 18),

    # A2059: Algorithmen für Mensch-Roboter Kollaboration - Menschenbild, Fortschritt, optimistisch, empirisch
    (2059, 3), (2059, 7), (2059, 13), (2059, 18),

    # A2060: Zukunft mit geteilten Straßen - Weltvision, Gesellschaft, optimistisch
    (2060, 1), (2060, 5), (2060, 13),

    # A2061: Safety zentrale Sorge - Risiko, Ethik, ambivalent, empirisch
    (2061, 6), (2061, 4), (2061, 15), (2061, 18),

    # A2062: Generalist robot policies transformativ - Fortschritt, optimistisch, empirisch
    (2062, 7), (2062, 13), (2062, 18),

    # A2063: Von Präferenzen lernen statt Demonstrationen - Epistemik, Fortschritt, optimistisch, empirisch
    (2063, 22), (2063, 7), (2063, 13), (2063, 18),

    # A2064: Konventionen kritisch für Mensch-AI Kollaboration - Menschenbild, Gesellschaft, optimistisch, empirisch
    (2064, 3), (2064, 5), (2064, 13), (2064, 18),

    # A2065: Grounded representations für embodied AI - Epistemik, Fortschritt, optimistisch, empirisch
    (2065, 22), (2065, 7), (2065, 13), (2065, 18),

    # A2066: Generalist policies wie Garten kultivieren - Selbstbild, Fortschritt, optimistisch, Metapher
    (2066, 2), (2066, 7), (2066, 13),

    # A2067: Autonome Fahrzeuge nudgen Fahrer - Menschenbild, Macht, optimistisch, empirisch
    (2067, 3), (2067, 8), (2067, 13), (2067, 18),

    # A2068: Algorithmic HRI für Sicherheit/Effizienz - Ethik, Fortschritt, optimistisch, empirisch
    (2068, 4), (2068, 7), (2068, 13), (2068, 18),

    # A2069: RoboCrowd crowdsourcing für Daten - Fortschritt, Gesellschaft, optimistisch, empirisch
    (2069, 7), (2069, 5), (2069, 13), (2069, 18),

    # A2070: StarGen Taxonomie für Generalisierung - Epistemik, Fortschritt, optimistisch, empirisch
    (2070, 22), (2070, 7), (2070, 13), (2070, 18),

    # A2071: Modell für menschliches Fahrverhalten - Menschenbild, Epistemik, optimistisch, empirisch
    (2071, 3), (2071, 22), (2071, 13), (2071, 18),

    # A2072: Interaktion als underactuated dynamical system - Epistemik, Fortschritt, optimistisch, empirisch
    (2072, 22), (2072, 7), (2072, 13), (2072, 18),

    # A2073: Roboter verstehen Menschen/Menschen Roboter-Skills - Menschenbild, Fortschritt, optimistisch, empirisch
    (2073, 3), (2073, 7), (2073, 13), (2073, 18),
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {len(codes)} Kodierungen fuer P91-P100")
conn.close()
