# -*- coding: utf-8 -*-
"""
Korrektur: Entferne doppelte Tonalitäten
Jede Aussage bekommt genau 1 Tonalität
"""

import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Manuelle Korrektur: Entscheide für jede Aussage die korrekte Tonalität
# Format: (aussage_id, zu_entfernende_kategorie_ids)
fixes = [
    # A418 Larry Page - "afraid of technology, not adapting" - eher PES
    (153, [13]),  # entferne OPT, behalte PES
    # A423 - "people able should solve" - eher PES (Kritik)
    (158, [13]),  # entferne OPT, behalte PES
    # A424 - "die working" - eher OPT trotz Tod
    (159, [14]),  # entferne PES, behalte OPT
    # A426 - "slavishly work inefficiently" - eher OPT (für Veränderung)
    (161, [14]),  # entferne PES, behalte OPT
    # A427 - "people like working, want time" - eher OPT
    (162, [14]),  # entferne PES, behalte OPT
    # A439 Sergey - "phone emasculating" - AMB ist richtig
    (174, [13, 14]),  # entferne OPT und PES, behalte AMB
    # A441 - "predisposed Parkinson's, opportunity" - eher OPT
    (176, [14]),  # entferne PES, behalte OPT
    # A442 - "make difference, re-evaluating" - AMB
    (177, [14]),  # entferne PES, behalte AMB
    # A444 - "moonshot-style, millions affected" - eher OPT
    (179, [14]),  # entferne PES, behalte OPT
    # A445 - "supporting research" - eher OPT
    (180, [15]),  # entferne AMB, behalte OPT
    # A446 - "coming in, exciting" - eher OPT
    (181, [15]),  # entferne AMB, behalte OPT
    # A448 - "not failure if learn" - eher OPT
    (183, [14]),  # entferne PES, behalte OPT
    # A449 - "lighter-than-air vehicles" - eher OPT
    (184, [14]),  # entferne PES, behalte OPT
    # A451 Bezos - "Day 1" - eher OPT
    (186, [14]),  # entferne PES, behalte OPT
    # A452 - "shareholder value" - eher OPT/AMB, nehme OPT
    (187, [15]),  # entferne AMB, behalte OPT
    # A454 - "obsessive customer focus" - eher OPT
    (189, [14]),  # entferne PES, behalte OPT
    # A456 - "high-quality high-velocity" - eher OPT
    (191, [14]),  # entferne PES, behalte OPT
    # A457 - "conviction despite not perfect" - eher OPT
    (192, [14]),  # entferne PES, behalte OPT
    # A458 - "size of failures grow" - eher OPT
    (193, [14]),  # entferne PES, behalte OPT
    # A459 - "machine learning quiet impact" - eher OPT
    (194, [14]),  # entferne PES, behalte OPT
    # A460 - "Alexa sophisticated AI" - eher OPT
    (195, [14]),  # entferne PES, behalte OPT
    # A461 - "trillion humans" - eher OPT/AMB, nehme OPT
    (196, [15]),  # entferne AMB, behalte OPT
    # A466 - "AI best tool, mostly good" - eher OPT
    (201, [14]),  # entferne PES, behalte OPT
    # A467 - "values do not need changing" - eher OPT
    (202, [14]),  # entferne PES, behalte OPT
    # A469 - "LLMs not lead to AGI" - AMB
    (204, [14]),  # entferne PES, behalte AMB
    # A470 - "AWS own best customer" - eher OPT
    (205, [14]),  # entferne PES, behalte OPT
    # A471 - "create more than consume" - eher OPT
    (206, [14]),  # entferne PES, behalte OPT
    # A936 Ellison - "biggest than industrial revolution" - eher OPT/AMB, nehme OPT
    (208, [15]),  # entferne AMB, behalte OPT
    # A937 - "police supervised" - kontrovers, nehme OPT (seine Sicht)
    (209, [14]),  # entferne PES, behalte OPT (dystopisch für manche, aber er meint es positiv)
    # A938 - "AI help solve, make us better" - eher OPT/AMB, nehme OPT
    (210, [15]),  # entferne AMB, behalte OPT
    # A945 - "wheat 20% more grain" - eher OPT/AMB, nehme OPT
    (217, [15]),  # entferne AMB, behalte OPT
    # A947 - "US can't let China win" - eher PES
    (219, [13]),  # entferne OPT, behalte PES
    # A948 - "environmental sustainability" - eher OPT
    (220, [14]),  # entferne PES, behalte OPT
    # A950 - "smartest engineers" - eher OPT/AMB, nehme OPT
    (222, [15]),  # entferne AMB, behalte OPT
]

# Lösche die doppelten Tonalitäten
for aussage_id, to_remove in fixes:
    for kategorie_id in to_remove:
        c.execute("""
            DELETE FROM aussagen_kategorien
            WHERE aussage_id = ? AND kategorie_id = ?
        """, (aussage_id, kategorie_id))
        print(f"Entfernt: Aussage {aussage_id}, Kategorie {kategorie_id}")

conn.commit()

# Überprüfung
c.execute("""
    SELECT aussage_id, COUNT(*) as cnt
    FROM aussagen_kategorien
    WHERE aussage_id BETWEEN 1 AND 224
      AND kategorie_id IN (13, 14, 15)
    GROUP BY aussage_id
    HAVING cnt != 1
""")
problematic = c.fetchall()

if problematic:
    print(f"\nNoch {len(problematic)} Aussagen mit Problem:")
    for row in problematic:
        print(f"  Aussage {row[0]}: {row[1]} Tonalitäten")
else:
    print("\nOK: Alle Aussagen haben genau 1 Tonalität!")

# Statistik
c.execute("""
    SELECT k.name, COUNT(*) as cnt
    FROM aussagen_kategorien ak
    JOIN kategorien k ON ak.kategorie_id = k.id
    WHERE ak.aussage_id BETWEEN 1 AND 224
      AND ak.kategorie_id IN (13, 14, 15)
    GROUP BY k.name
    ORDER BY cnt DESC
""")
print("\nTonalität-Verteilung nach Korrektur:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.close()
print("\nKorrektur abgeschlossen!")
