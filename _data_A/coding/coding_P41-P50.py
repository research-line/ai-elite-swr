import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Kodierung für P41-P50
codes = [
    # A702 - Scott Wu - Programmieren lernen, Ideen realisieren
    (702, 2), (702, 13),  # SB, OPT

    # A703 - Scott Wu - Zukunft Software Engineering, Devin als async Agent
    (703, 7), (703, 9), (703, 13), (703, 18),  # FO, AR, OPT, EMP

    # A704 - Scott Wu - Devin als Junior Engineer
    (704, 9), (704, 13), (704, 18),  # AR, OPT, EMP

    # A705 - Scott Wu - Evolution von High School Student zu Junior Engineer
    (705, 7), (705, 9), (705, 13),  # FO, AR, OPT

    # A706 - Scott Wu - Bricklayer zu Architect, Mensch in Kontrolle
    (706, 3), (706, 8), (706, 9), (706, 13),  # MB, MA, AR, OPT

    # A707 - Scott Wu - Zukunft: Computer baut was man sagt
    (707, 7), (707, 9), (707, 13),  # FO, AR, OPT

    # A708 - Scott Wu - Mensch+AI, 10x Gains
    (708, 3), (708, 9), (708, 13),  # MB, AR, OPT

    # A709 - Scott Wu - AI übertrifft beste Programmierer, Demokratisierung
    (709, 7), (709, 9), (709, 13),  # FO, AR, OPT

    # A710 - Scott Wu - Devin merged 30-40% Pull Requests
    (710, 9), (710, 13), (710, 18),  # AR, OPT, EMP

    # A711 - Scott Wu - Windsurf Akquisition
    (711, 9), (711, 13),  # AR, OPT

    # A712 - Scott Wu - AI schafft mehr Jobs (Jevons Paradox)
    (712, 9), (712, 13), (712, 17),  # AR, OPT, PHI

    # A713 - Scott Wu - Engineers: Bricklayers zu Architects
    (713, 9), (713, 13),  # AR, OPT

    # A714 - Michael Intrator - Unermüdliche Nachfrage großer Tech-Firmen
    (714, 9), (714, 13), (714, 18),  # AR, OPT, EMP

    # A715 - Michael Intrator - Divergenz Kapitalmarkt vs. Realität
    (715, 9), (715, 13), (715, 22),  # AR, OPT, EP

    # A716 - Michael Intrator - IPO als Mittel zum Zweck
    (716, 9), (716, 15),  # AR, AMB

    # A717 - Michael Intrator - CoreWeave: erste AI-native Cloud
    (717, 9), (717, 13), (717, 18),  # AR, OPT, EMP

    # A718 - Michael Intrator - Physische Engpässe: Policy, Infrastruktur, Energie
    (718, 9), (718, 11), (718, 14), (718, 18),  # AR, RE, PES, EMP

    # A719 - Michael Intrator - Nicht zirkulär, logistische Notwendigkeit
    (719, 9), (719, 22), (719, 15),  # AR, EP, AMB

    # A720 - Michael Intrator - Diversifikation von Microsoft-Abhängigkeit
    (720, 9), (720, 13), (720, 18),  # AR, OPT, EMP

    # A721 - Michael Intrator - AI in allem in 10 Jahren
    (721, 7), (721, 13),  # FO, OPT

    # A722 - Michael Intrator - AI: 15% Wirtschaftswachstum, kurzfristig schwierig
    (722, 9), (722, 5), (722, 15), (722, 18),  # AR, GE, AMB, EMP

    # A723 - Michael Intrator - OpenAI-Partnerschaft
    (723, 9), (723, 13),  # AR, OPT

    # A724 - Michael Intrator - AI Energiehunger, Effizienz vs. Nachfrage
    (724, 9), (724, 6), (724, 15), (724, 18),  # AR, RI, AMB, EMP

    # A725 - Michael Intrator - AI: von Tech zu Systemen, Nutzbarkeit
    (725, 7), (725, 5), (725, 13),  # FO, GE, OPT

    # A738 - Jakub Pachocki - Modelle entdecken neue Erkenntnisse
    (738, 22), (738, 7), (738, 13),  # EP, FO, OPT

    # A739 - Jakub Pachocki - Form von Reasoning, aber anders als Menschen
    (739, 3), (739, 22), (739, 15),  # MB, EP, AMB

    # A740 - Jakub Pachocki - Ziel: Automatisierung wissenschaftlicher Forschung
    (740, 7), (740, 22), (740, 13),  # FO, EP, OPT

    # A741 - Jakub Pachocki - Deep Learning ist Black Box
    (741, 22), (741, 15), (741, 18),  # EP, AMB, EMP

    # A742 - Jakub Pachocki - KI als Naturwissenschaft, nicht nur Mathematik
    (742, 22), (742, 17), (742, 15),  # EP, PHI, AMB

    # A743 - Jakub Pachocki - Reasoning-Modelle werden persistente Entitäten
    (743, 7), (743, 10), (743, 13),  # FO, TR, OPT

    # A744 - Jakub Pachocki - Von Sci-Fi zu Realität
    (744, 7), (744, 13),  # FO, OPT

    # A745 - Jakub Pachocki - Je mehr Verständnis, desto faszinierender
    (745, 22), (745, 13), (745, 17),  # EP, OPT, PHI

    # A746 - Jakub Pachocki - Ilya als Mentor und Visionär
    (746, 2), (746, 13),  # SB, OPT

    # A747 - Jakub Pachocki - Chain-of-thought Faithfulness & Interpretability
    (747, 22), (747, 6), (747, 13),  # EP, RI, OPT

    # A748 - Jakub Pachocki - ICPC: 12/12 Probleme gelöst, Platz 1
    (748, 7), (748, 13), (748, 18),  # FO, OPT, EMP

    # A749 - Jakub Pachocki - "Hackers and Painters" mit 15
    (749, 2), (749, 15),  # SB, AMB

    # A750 - Palmer Luckey - $50 Milliarden Firma bauen
    (750, 2), (750, 9), (750, 13),  # SB, AR, OPT

    # A751 - Palmer Luckey - Leben/Tod-Entscheidungen: beste Technologie nötig
    (751, 4), (751, 6), (751, 15), (751, 16),  # ET, RI, AMB, POL

    # A752 - Palmer Luckey - Kein moralischer Vorteil für dumme Waffen
    (752, 4), (752, 6), (752, 15), (752, 16),  # ET, RI, AMB, POL

    # A753 - Palmer Luckey - Mehr wie China: Fokus auf Technologie
    (753, 8), (753, 16), (753, 15),  # MA, POL, AMB

    # A754 - Palmer Luckey - Facebook-Entlassung wegen Trump-Spende
    (754, 2), (754, 8), (754, 14), (754, 16),  # SB, MA, PES, POL

    # A755 - Palmer Luckey - Widerspruch zu offizieller Story
    (755, 2), (755, 8), (755, 14), (755, 16),  # SB, MA, PES, POL

    # A756 - Palmer Luckey - VR/AR als Zukunft des Militärs
    (756, 7), (756, 8), (756, 13), (756, 16),  # FO, MA, OPT, POL

    # A757 - Palmer Luckey - Börsengang geplant
    (757, 9), (757, 13),  # AR, OPT

    # A758 - Palmer Luckey - Trump-Unterstützung
    (758, 2), (758, 16),  # SB, POL

    # A759 - Palmer Luckey - DeepSeek beeindruckend, aber Hysterie übertrieben
    (759, 22), (759, 9), (759, 15), (759, 16),  # EP, AR, AMB, POL

    # A760 - Palmer Luckey - Tesla/Roomba haben bessere KI als Pentagon
    (760, 8), (760, 16), (760, 14),  # MA, POL, PES

    # A761 - Palmer Luckey - Gut, Menschen manchmal zu erschrecken
    (761, 4), (761, 8), (761, 15), (761, 21),  # ET, MA, AMB, HA

    # A786 - Mark Chen - GPT 4.5 als Beweis für Skalierung
    (786, 7), (786, 13), (786, 18),  # FO, OPT, EMP

    # A787 - Mark Chen - Skalierung und Reasoning komplementär
    (787, 7), (787, 22), (787, 13),  # FO, EP, OPT

    # A788 - Mark Chen - Von AGI-Skeptiker zu Überzeugtem
    (788, 2), (788, 7), (788, 13),  # SB, FO, OPT

    # A789 - Mark Chen - Finanzwelt schwierig für Impact
    (789, 2), (789, 4), (789, 15),  # SB, ET, AMB

    # A790 - Mark Chen - Abgänge tough, aber OpenAI ist bester Ort
    (790, 2), (790, 13),  # SB, OPT

    # A791 - Mark Chen - Feld entwickelt sich inkonsistent zu früherer Forschung
    (791, 7), (791, 22), (791, 15),  # FO, EP, AMB

    # A792 - Mark Chen - ICPC volle Punktzahl, weitere Erfolge
    (792, 7), (792, 13), (792, 18),  # FO, OPT, EMP

    # A793 - Mark Chen - Glückwunsch DeepSeek für o1-Level Reasoning
    (793, 22), (793, 13),  # EP, OPT

    # A794 - Mark Chen - Sicheres AI-Modell tut was User will
    (794, 6), (794, 11), (794, 13),  # RI, RE, OPT

    # A795 - Mark Chen - o3/o4-mini mit Tools mächtiger
    (795, 7), (795, 13), (795, 18),  # FO, OPT, EMP

    # A796 - Mark Chen - GPT-5 Pro entwickelt neue Mathematik
    (796, 7), (796, 22), (796, 13),  # FO, EP, OPT

    # A797 - Mark Chen - Deep Research für Pro-User
    (797, 9), (797, 13),  # AR, OPT

    # A798 - Craig Federighi - Privacy als Grundlage für Personal Intelligence
    (798, 4), (798, 6), (798, 13), (798, 17),  # ET, RI, OPT, PHI

    # A799 - Craig Federighi - Privacy Bubble auf Server
    (799, 6), (799, 11), (799, 13), (799, 18),  # RI, RE, OPT, EMP

    # A800 - Craig Federighi - AI soll User empowern, nicht ersetzen
    (800, 3), (800, 4), (800, 13), (800, 17),  # MB, ET, OPT, PHI

    # A801 - Craig Federighi - Jahrzehnte-langer Arc, verantwortungsvoll
    (801, 7), (801, 4), (801, 15),  # FO, ET, AMB

    # A802 - Craig Federighi - Lieber richtig machen als schnell rausbringen
    (802, 4), (802, 6), (802, 13),  # ET, RI, OPT

    # A803 - Craig Federighi - On-Device AI, Daten unter Kontrolle
    (803, 6), (803, 11), (803, 13), (803, 18),  # RI, RE, OPT, EMP

    # A804 - Craig Federighi - Niemand hat Zugang zu Daten
    (804, 6), (804, 4), (804, 13),  # RI, ET, OPT

    # A805 - Craig Federighi - Aware ohne zu sammeln
    (805, 6), (805, 11), (805, 13),  # RI, RE, OPT

    # A806 - Craig Federighi - Nicht Chatbot, sondern tief integriert
    (806, 7), (806, 13),  # FO, OPT

    # A807 - Craig Federighi - Apple Silicon im Data Center
    (807, 9), (807, 13), (807, 18),  # AR, OPT, EMP

    # A808 - Craig Federighi - Moment an dem lange gearbeitet wurde
    (808, 7), (808, 2), (808, 13),  # FO, SB, OPT

    # A809 - Craig Federighi - E2E Encryption nicht möglich, neue Lösung
    (809, 6), (809, 11), (809, 15), (809, 18),  # RI, RE, AMB, EMP

    # A858 - Chris Dixon - Web3: internet owned by builders/users
    (858, 1), (858, 5), (858, 8), (858, 13),  # WV, GE, MA, OPT

    # A859 - Chris Dixon - Blockchains als einziger Pfad zu offenem Internet
    (859, 1), (859, 5), (859, 8), (859, 13), (859, 17),  # WV, GE, MA, OPT, PHI

    # A860 - Chris Dixon - Gambling lenkt ab von wahrem Potenzial
    (860, 4), (860, 9), (860, 14),  # ET, AR, PES

    # A861 - Chris Dixon - Next big thing sieht aus wie Spielzeug
    (861, 7), (861, 13), (861, 17),  # FO, OPT, PHI

    # A862 - Chris Dixon - Smarteste Leute: Wochenende → Woche in 10 Jahren
    (862, 7), (862, 5), (862, 13), (862, 17),  # FO, GE, OPT, PHI

    # A863 - Chris Dixon - Hobbies ohne finanzielle Zwänge
    (863, 7), (863, 2), (863, 13),  # FO, SB, OPT

    # A864 - Chris Dixon - Firma besitzt Netzwerk, nicht Community
    (864, 8), (864, 9), (864, 14), (864, 16),  # MA, AR, PES, POL

    # A865 - Chris Dixon - Read-write-own era durch Tokens
    (865, 1), (865, 8), (865, 13),  # WV, MA, OPT

    # A866 - Chris Dixon - Blockchains: User als Owner statt Services
    (866, 1), (866, 8), (866, 5), (866, 13), (866, 17),  # WV, MA, GE, OPT, PHI

    # A867 - Chris Dixon - Blockchain für Authentizität gegen Deepfakes
    (867, 6), (867, 11), (867, 13),  # RI, RE, OPT

    # A868 - Chris Dixon - UK Büro, konstruktiver Dialog
    (868, 9), (868, 11), (868, 13), (868, 16),  # AR, RE, OPT, POL

    # A869 - Chris Dixon - Yuga Labs als Gegengewicht zu Meta
    (869, 8), (869, 5), (869, 13), (869, 16),  # MA, GE, OPT, POL

    # A870 - Ben Horowitz - AI wie Dampfmaschine oder Elektrizität
    (870, 1), (870, 7), (870, 13), (870, 17),  # WV, FO, OPT, PHI

    # A871 - Ben Horowitz - Nicht vorhersagbar
    (871, 22), (871, 15),  # EP, AMB

    # A872 - Ben Horowitz - AI-Regulierung nicht verlangsamen, Europa warnt
    (872, 11), (872, 9), (872, 14), (872, 16),  # RE, AR, PES, POL

    # A873 - Ben Horowitz - Beste der Welt in einer Sache
    (873, 9), (873, 13),  # AR, OPT

    # A874 - Ben Horowitz - Was du tust, nicht glaubst, definiert dich
    (874, 4), (874, 2), (874, 17),  # ET, SB, PHI

    # A875 - Ben Horowitz - Harte Entscheidungen → mutige Firma
    (875, 4), (875, 8), (875, 13), (875, 17),  # ET, MA, OPT, PHI

    # A876 - Ben Horowitz - Gut für Tech, Zukunft steht auf dem Spiel
    (876, 9), (876, 7), (876, 13), (876, 16),  # AR, FO, OPT, POL

    # A877 - Ben Horowitz - Biden-Administration destruktiv für Tech
    (877, 11), (877, 9), (877, 14), (877, 16),  # RE, AR, PES, POL

    # A878 - Ben Horowitz - Rap über Leadership, nicht nur Geld
    (878, 4), (878, 2), (878, 15),  # ET, SB, AMB

    # A879 - Ben Horowitz - Unmöglich, alle zukünftigen Jobs vorauszusehen
    (879, 9), (879, 7), (879, 13),  # AR, FO, OPT

    # A880 - Ben Horowitz - Hard things in Leadership
    (880, 8), (880, 9), (880, 15),  # MA, AR, AMB

    # A881 - Ben Horowitz - Crypto als fehlende Schicht für AI
    (881, 7), (881, 9), (881, 13),  # FO, AR, OPT

    # A882 - Ben Horowitz - Crypto-Gründer können jetzt bauen
    (882, 9), (882, 11), (882, 13), (882, 16),  # AR, RE, OPT, POL

    # A883 - Andy Jassy - AI transformativste Technologie unserer Zeit
    (883, 1), (883, 7), (883, 13),  # WV, FO, OPT

    # A884 - Andy Jassy - AI: Once-in-a-lifetime, aggressiv investieren
    (884, 7), (884, 9), (884, 13),  # FO, AR, OPT

    # A885 - Andy Jassy - Drei Schritte in Marathon
    (885, 7), (885, 15),  # FO, AMB

    # A886 - Andy Jassy - Weniger Menschen bei automatisierten Jobs
    (886, 9), (886, 14), (886, 18),  # AR, PES, EMP

    # A887 - Andy Jassy - Zurück ins Büro wie vor COVID
    (887, 9), (887, 15), (887, 16),  # AR, AMB, POL

    # A888 - Andy Jassy - Nicht Kostenspiel, kein Backdoor Layoff
    (888, 9), (888, 15), (888, 16),  # AR, AMB, POL

    # A889 - Andy Jassy - Amazon Q: Game Changer für Effizienz
    (889, 9), (889, 13), (889, 18),  # AR, OPT, EMP

    # A890 - Andy Jassy - Practical AI für Kundenprobleme
    (890, 7), (890, 9), (890, 13),  # FO, AR, OPT

    # A891 - Andy Jassy - Menschen haben verschiedene Expertise
    (891, 3), (891, 15), (891, 17),  # MB, AMB, PHI

    # A892 - Andy Jassy - Bedrock als größte Inference Engine
    (892, 9), (892, 13),  # AR, OPT

    # A893 - Andy Jassy - Respekt für Anthropic, tiefere Kooperation
    (893, 9), (893, 13),  # AR, OPT

    # A894 - Andy Jassy - Gute AI-Modelle kosten Milliarden
    (894, 9), (894, 15), (894, 18),  # AR, AMB, EMP

    # A895 - Andy Jassy - Climate Pledge: net-zero 2040
    (895, 4), (895, 6), (895, 13),  # ET, RI, OPT

    # A896 - Andy Jassy - Kuiper für 400-500M Haushalte ohne Breitband
    (896, 5), (896, 9), (896, 13),  # GE, AR, OPT

    # A897 - Clement Delangue - Open source verteilt ökonomische Gewinne
    (897, 5), (897, 9), (897, 13), (897, 17),  # GE, AR, OPT, PHI

    # A898 - Clement Delangue - Ethische Offenheit für Zivilgesellschaft
    (898, 4), (898, 8), (898, 13), (898, 17),  # ET, MA, OPT, PHI

    # A899 - Clement Delangue - Transparenz, Offenheit, Machtverteilung
    (899, 4), (899, 8), (899, 5), (899, 13),  # ET, MA, GE, OPT

    # A900 - Clement Delangue - Open source schafft 1000x mehr Wert
    (900, 9), (900, 5), (900, 13), (900, 17),  # AR, GE, OPT, PHI

    # A901 - Clement Delangue - Open source aligned mit amerikanischen Werten
    (901, 4), (901, 16), (901, 13),  # ET, POL, OPT

    # A902 - Clement Delangue - AI "denkt" nicht, es "verarbeitet"
    (902, 3), (902, 22), (902, 14), (902, 17),  # MB, EP, PES, PHI

    # A903 - Clement Delangue - Open source hinkt hinterher wegen Ethik
    (903, 4), (903, 22), (903, 15),  # ET, EP, AMB

    # A904 - Clement Delangue - Wort "AI" aufgeben für spezifische Begriffe?
    (904, 22), (904, 5), (904, 15), (904, 17),  # EP, GE, AMB, PHI

    # A905 - Clement Delangue - Zukunft der AI: offen und zugänglich
    (905, 1), (905, 5), (905, 8), (905, 13),  # WV, GE, MA, OPT

    # A906 - Clement Delangue - Open source verhindert Black Box
    (906, 4), (906, 22), (906, 13),  # ET, EP, OPT

    # A907 - Clement Delangue - Existenzrisiko als Argument gegen Offenheit
    (907, 6), (907, 8), (907, 14), (907, 16),  # RI, MA, PES, POL

    # A908 - Clement Delangue - Offenheit ermöglicht externe Kontrolle
    (908, 4), (908, 11), (908, 13),  # ET, RE, OPT
]

c.executemany("INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id) VALUES (?, ?)", codes)
conn.commit()
print(f"Eingefuegt: {len(codes)} Kodierungen fuer P41-P50 ({len(set([x[0] for x in codes]))} Aussagen)")
conn.close()
