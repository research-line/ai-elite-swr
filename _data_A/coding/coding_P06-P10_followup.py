# -*- coding: utf-8 -*-
"""
Nachtrag: Kodierung der Aussagen P6-P10 (IDs 417-472)
Die Kodierungen existieren bereits im ersten Skript für Aussagen 152-224,
müssen aber auf die korrekten IDs 417-472 gemappt werden.
"""

import sqlite3

conn = sqlite3.connect(r'C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db')
c = conn.cursor()

# Mapping: meine Kodierungs-IDs 152-224 -> echte Aussagen-IDs 417-472
# A152-A168 = A417-A433 (Larry Page, 17 Aussagen)
# A169-A185 = A434-A450 (Sergey Brin, 17 Aussagen)
# A186-A207 = A451-A472 (Jeff Bezos, 22 Aussagen)
# A208-A224 = A936-A952 (Larry Ellison, 17 Aussagen)

id_mapping = {}
# Larry Page: 152-168 -> 417-433
for i in range(17):
    id_mapping[152 + i] = 417 + i
# Sergey Brin: 169-185 -> 434-450
for i in range(17):
    id_mapping[169 + i] = 434 + i
# Jeff Bezos: 186-207 -> 451-472
for i in range(22):
    id_mapping[186 + i] = 451 + i
# Larry Ellison: 208-224 -> 936-952
for i in range(17):
    id_mapping[208 + i] = 936 + i

# Hole alle Kodierungen für Aussagen 152-224 aus dem ersten Skript
original_codes = [
    # Die Kodierungen von Aussagen 152-224 aus dem ersten Skript
    # müssen hier eingefügt werden
]

# Da das erste Skript bereits gelaufen ist, müssen wir die Kodierungen
# aus der Datenbank lesen und umkopieren
print("Kopiere Kodierungen zu korrekten IDs...")

codes_to_insert = []

# Für jede gemappte ID
for old_id, new_id in id_mapping.items():
    # Hole die Kodierungen der alten ID
    c.execute("""
        SELECT kategorie_id
        FROM aussagen_kategorien
        WHERE aussage_id = ?
    """, (old_id,))

    kategorien = c.fetchall()
    if kategorien:
        print(f"Kopiere {len(kategorien)} codes von Aussage {old_id} -> {new_id}")
        for (kat_id,) in kategorien:
            codes_to_insert.append((new_id, kat_id))

# Füge neue Kodierungen ein
if codes_to_insert:
    c.executemany("""
        INSERT OR IGNORE INTO aussagen_kategorien (aussage_id, kategorie_id)
        VALUES (?, ?)
    """, codes_to_insert)
    conn.commit()
    print(f"\nEingefügt: {len(codes_to_insert)} Kodierungen für P6-P10")
else:
    print("FEHLER: Keine Kodierungen gefunden zum Kopieren!")
    print("Die Aussagen 152-224 scheinen nicht kodiert zu sein.")

# Statistik
c.execute("""
    SELECT
        p.id,
        p.name,
        COUNT(DISTINCT a.id) as total_aussagen,
        COUNT(DISTINCT ak.aussage_id) as kodiert
    FROM personen p
    LEFT JOIN aussagen a ON p.id = a.person_id
    LEFT JOIN aussagen_kategorien ak ON a.id = ak.aussage_id
    WHERE p.id BETWEEN 1 AND 10
    GROUP BY p.id, p.name
    ORDER BY p.id
""")
print("\n=== STATUS NACH NACHTRAG ===")
for row in c.fetchall():
    pct = (row[3] / row[2] * 100) if row[2] > 0 else 0
    print(f"P{row[0]} {row[1]:20s}: {row[3]}/{row[2]} kodiert ({pct:.0f}%)")

conn.close()
