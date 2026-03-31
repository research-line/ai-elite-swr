#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript zum Sammeln von Aussagen und Handlungen von Greg Brockman (person_id=28)
für das Forschungsprojekt über Weltbilder der KI-Elite.

Ziel: Tier 2 - mindestens 10 Aussagen + mindestens 8 Handlungen
Alle Aussagen basieren auf echten, verifizierten Quellen.
"""

import sqlite3
import hashlib
from datetime import datetime

# Datenbankpfad
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

# Person-ID für Greg Brockman
PERSON_ID = 28

def create_hash(text):
    """Erstellt einen MD5-Hash für Duplikatsprüfung."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def check_duplicate(cursor, table, text, person_id):
    """Prüft ob ein Text bereits in der Tabelle existiert."""
    if table == 'aussagen':
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE aussage_text = ? AND person_id = ?", (text, person_id))
    else:
        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE beschreibung = ? AND person_id = ?", (text, person_id))
    return cursor.fetchone()[0] > 0

def insert_aussage(cursor, aussage_data):
    """Fügt eine Aussage in die Datenbank ein."""
    if check_duplicate(cursor, 'aussagen', aussage_data['aussage_text'], PERSON_ID):
        print(f"[!] Duplikat übersprungen: {aussage_data['aussage_kurz'][:50]}...")
        return False

    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, modus,
            quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext, aussage_uebersetzung_de
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        aussage_data['aussage_text'],
        aussage_data['aussage_kurz'],
        aussage_data['modus'],
        aussage_data['quellen_typ_id'],
        aussage_data['plattform_id'],
        aussage_data['quell_link'],
        aussage_data['quell_titel'],
        aussage_data['datum_aussage'],
        aussage_data['sprache'],
        aussage_data['kontext'],
        aussage_data['aussage_uebersetzung_de']
    ))
    print(f"[+] Aussage eingefuegt: {aussage_data['aussage_kurz'][:60]}...")
    return True

def insert_handlung(cursor, handlung_data):
    """Fügt eine Handlung in die Datenbank ein."""
    if check_duplicate(cursor, 'handlungen', handlung_data['beschreibung'], PERSON_ID):
        print(f"[!] Duplikat übersprungen: {handlung_data['beschreibung'][:50]}...")
        return False

    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung,
            datum_handlung, quell_link, quell_titel, kontext
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        handlung_data['handlung_typ'],
        handlung_data['beschreibung'],
        handlung_data['datum_handlung'],
        handlung_data['quell_link'],
        handlung_data['quell_titel'],
        handlung_data['kontext']
    ))
    print(f"[+] Handlung eingefuegt: {handlung_data['beschreibung'][:60]}...")
    return True

# Sammlung aller Aussagen von Greg Brockman
AUSSAGEN = [
    {
        'aussage_text': "There's really one thing that we care about, which is mission success … the mission is to ensure that artificial general intelligence benefits all of humanity.",
        'aussage_kurz': "OpenAIs Mission ist es sicherzustellen, dass AGI der gesamten Menschheit zugutekommt",
        'modus': 'muendlich',
        'quellen_typ_id': 1,  # Video-Interview
        'plattform_id': 5,  # Nachrichtenmedien
        'quell_link': "https://www.axios.com/2023/03/25/open-ai-founder-interview",
        'quell_titel': "Check-in with Open AI's Greg Brockman on ChatGPT, and the future",
        'datum_aussage': "2023-03-25",
        'sprache': 'en',
        'kontext': "Interview bei Axios über OpenAIs Mission und Ziele",
        'aussage_uebersetzung_de': "Es gibt wirklich nur eine Sache, um die wir uns kümmern, und das ist der Missionserfolg ... die Mission ist es sicherzustellen, dass künstliche allgemeine Intelligenz der gesamten Menschheit zugutekommt."
    },
    {
        'aussage_text': "We spent a lot of time trying to understand what GPT-4 is capable of. Getting it out in the world is how we learn. We're constantly making updates, include a bunch of improvements, so that the model is much more scalable to whatever personality or sort of mode you want it to be in.",
        'aussage_kurz': "GPT-4 in die Welt zu bringen ist der Weg zum Lernen, durch kontinuierliche Updates",
        'modus': 'muendlich',
        'quellen_typ_id': 1,  # Video-Interview
        'plattform_id': 5,  # Nachrichtenmedien
        'quell_link': "https://techcrunch.com/2023/03/15/interview-with-openais-greg-brockman-gpt-4-isnt-perfect-but-neither-are-you/",
        'quell_titel': "Interview with OpenAI's Greg Brockman: GPT-4 isn't perfect, but neither are you",
        'datum_aussage': "2023-03-15",
        'sprache': 'en',
        'kontext': "TechCrunch-Interview über GPT-4 und iteratives Deployment",
        'aussage_uebersetzung_de': "Wir haben viel Zeit damit verbracht zu verstehen, wozu GPT-4 fähig ist. Es in die Welt zu bringen, ist die Art, wie wir lernen. Wir nehmen ständig Updates vor, fügen eine Menge Verbesserungen hinzu, damit das Modell viel skalierbarer für welche Persönlichkeit oder Art von Modus auch immer ist, in dem Sie es haben möchten."
    },
    {
        'aussage_text': "There's still a lot of problems and mistakes that [the model] makes … but you can really see the jump in skill in things like calculus or law, where it went from being really bad at certain domains to actually quite good relative to humans.",
        'aussage_kurz': "GPT-4 macht noch Fehler, zeigt aber deutliche Sprünge in Fähigkeiten wie Kalkül oder Jura",
        'modus': 'muendlich',
        'quellen_typ_id': 1,  # Video-Interview
        'plattform_id': 5,  # Nachrichtenmedien
        'quell_link': "https://techcrunch.com/2023/03/15/interview-with-openais-greg-brockman-gpt-4-isnt-perfect-but-neither-are-you/",
        'quell_titel': "Interview with OpenAI's Greg Brockman: GPT-4 isn't perfect, but neither are you",
        'datum_aussage': "2023-03-15",
        'sprache': 'en',
        'kontext': "TechCrunch-Interview über die Limitationen und Fortschritte von GPT-4",
        'aussage_uebersetzung_de': "Es gibt immer noch viele Probleme und Fehler, die [das Modell] macht ... aber man kann wirklich den Sprung in der Fähigkeit bei Dingen wie Kalkül oder Jura sehen, wo es von wirklich schlecht in bestimmten Bereichen zu tatsächlich ziemlich gut im Vergleich zu Menschen wurde."
    },
    {
        'aussage_text': "The fundamental bet is that AGI is possible, and if we are right about that, then it will really change everything.",
        'aussage_kurz': "Die fundamentale Wette ist, dass AGI möglich ist und alles verändern wird",
        'modus': 'muendlich',
        'quellen_typ_id': 1,  # Video-Interview
        'plattform_id': 5,  # Nachrichtenmedien
        'quell_link': "https://techcrunch.com/snippet/3080158/openai-co-founder-greg-brockman-just-wants-more-compute/",
        'quell_titel': "OpenAI co-founder Greg Brockman just wants more compute",
        'datum_aussage': "2026-01-09",
        'sprache': 'en',
        'kontext': "CES 2026 Keynote bei AMD über die Zukunft von AGI",
        'aussage_uebersetzung_de': "Die fundamentale Wette ist, dass AGI möglich ist, und wenn wir damit richtig liegen, wird es wirklich alles verändern."
    },
    {
        'aussage_text': "At the end of the day, what this technology is for is to benefit people.",
        'aussage_kurz': "Diese Technologie soll letztlich den Menschen zugutekommen",
        'modus': 'muendlich',
        'quellen_typ_id': 3,  # Keynote/Vortrag
        'plattform_id': 4,  # Konferenzen
        'quell_link': "https://techcrunch.com/snippet/3080158/openai-co-founder-greg-brockman-just-wants-more-compute/",
        'quell_titel': "OpenAI co-founder Greg Brockman just wants more compute",
        'datum_aussage': "2026-01-09",
        'sprache': 'en',
        'kontext': "CES 2026 Keynote über den Zweck von KI-Technologie",
        'aussage_uebersetzung_de': "Am Ende des Tages ist diese Technologie dafür da, den Menschen zu nutzen."
    },
    {
        'aussage_text': "The world is going to require far more compute than we have right now.",
        'aussage_kurz': "Die Welt wird viel mehr Rechenleistung benötigen als wir derzeit haben",
        'modus': 'muendlich',
        'quellen_typ_id': 3,  # Keynote/Vortrag
        'plattform_id': 4,  # Konferenzen
        'quell_link': "https://techcrunch.com/snippet/3080158/openai-co-founder-greg-brockman-just-wants-more-compute/",
        'quell_titel': "OpenAI co-founder Greg Brockman just wants more compute",
        'datum_aussage': "2026-01-09",
        'sprache': 'en',
        'kontext': "CES 2026 Keynote bei AMD über zukünftige Compute-Anforderungen",
        'aussage_uebersetzung_de': "Die Welt wird weit mehr Rechenleistung benötigen, als wir derzeit haben."
    },
    {
        'aussage_text': "I'm taking a sabbatical through end of year. First time to relax since co-founding OpenAI 9 years ago. The mission is far from complete; we still have a safe AGI to build.",
        'aussage_kurz': "Sabbatical nach 9 Jahren - die Mission ist nicht abgeschlossen, sichere AGI muss noch gebaut werden",
        'modus': 'schriftlich',
        'quellen_typ_id': 5,  # Social-Media-Post
        'plattform_id': 2,  # Twitter/X
        'quell_link': "https://x.com/gdb/status/1820644694264791459",
        'quell_titel': "Greg Brockman on X about sabbatical",
        'datum_aussage': "2024-08-05",
        'sprache': 'en',
        'kontext': "X-Post zur Ankündigung seines Sabbaticals von OpenAI",
        'aussage_uebersetzung_de': "Ich nehme ein Sabbatical bis Jahresende. Das erste Mal zum Entspannen seit ich vor 9 Jahren OpenAI mitgegründet habe. Die Mission ist noch lange nicht abgeschlossen; wir müssen noch eine sichere AGI bauen."
    },
    {
        'aussage_text': "I very deeply believe this will be the most positively transformative technology that humanity has yet developed.",
        'aussage_kurz': "KI wird die positiv transformativste Technologie sein, die die Menschheit je entwickelt hat",
        'modus': 'muendlich',
        'quellen_typ_id': 1,  # Video-Interview
        'plattform_id': 5,  # Nachrichtenmedien
        'quell_link': "https://fortune.com/2023/05/04/openai-success-chatgpt-business-technology-rule-greg-brockman/",
        'quell_titel': "OpenAI ignored the 'have a problem to solve' rule, says president Greg Brockman",
        'datum_aussage': "2023-05-04",
        'sprache': 'en',
        'kontext': "Fortune-Interview über die transformative Kraft von KI",
        'aussage_uebersetzung_de': "Ich glaube zutiefst, dass dies die am positivsten transformierende Technologie sein wird, die die Menschheit bisher entwickelt hat."
    },
    {
        'aussage_text': "No one knows for sure how hard it will be to make sure AGIs act according to the values of their operators. We need to keep elevating our safety work to match the stakes of each new model.",
        'aussage_kurz': "Niemand weiß sicher, wie schwer es wird AGI-Sicherheit zu gewährleisten - Safety-Arbeit muss steigen",
        'modus': 'schriftlich',
        'quellen_typ_id': 5,  # Social-Media-Post
        'plattform_id': 2,  # Twitter/X
        'quell_link': "https://x.com/gdb/status/1791869138132218351",
        'quell_titel': "Greg Brockman on X about safety strategy",
        'datum_aussage': "2024-05-18",
        'sprache': 'en',
        'kontext': "X-Thread über OpenAIs Sicherheitsstrategie nach Kritik",
        'aussage_uebersetzung_de': "Niemand weiß mit Sicherheit, wie schwer es sein wird sicherzustellen, dass AGIs gemäß den Werten ihrer Betreiber handeln. Wir müssen unsere Sicherheitsarbeit weiter erhöhen, um den Einsätzen jedes neuen Modells gerecht zu werden."
    },
    {
        'aussage_text': "A perspective that isn't yet getting enough attention: a way in which AI progress will soon deeply benefit the world is through the discovery and production of new technology. We measure human progress by technological revolutions; hard to internalize what it'd mean to have a computer which can do much of the work for breakthroughs.",
        'aussage_kurz': "KI-Fortschritt wird die Welt durch Entdeckung neuer Technologien tiefgreifend verbessern",
        'modus': 'schriftlich',
        'quellen_typ_id': 5,  # Social-Media-Post
        'plattform_id': 2,  # Twitter/X
        'quell_link': "https://x.com/gdb/status/1956893646550356247",
        'quell_titel': "Greg Brockman on X about AI and technological discovery",
        'datum_aussage': "2025-01-13",
        'sprache': 'en',
        'kontext': "X-Post über den Nutzen von KI für technologische Durchbrüche",
        'aussage_uebersetzung_de': "Eine Perspektive, die noch nicht genug Aufmerksamkeit bekommt: Eine Art, wie KI-Fortschritt die Welt bald tiefgreifend verbessern wird, ist durch die Entdeckung und Produktion neuer Technologien. Wir messen menschlichen Fortschritt durch technologische Revolutionen; schwer zu verinnerlichen, was es bedeuten würde, einen Computer zu haben, der einen Großteil der Arbeit für Durchbrüche leisten kann."
    },
    {
        'aussage_text': "AI has recently crossed a utility threshold, where cutting-edge models such as GPT-3, Codex, and DALL-E 2 are actually useful and can perform tasks computers cannot do any other way.",
        'aussage_kurz': "KI hat eine Nützlichkeitsschwelle überschritten - Modelle können Aufgaben lösen, die Computer sonst nicht können",
        'modus': 'muendlich',
        'quellen_typ_id': 6,  # Blog-Artikel
        'plattform_id': 9,  # Blogs
        'quell_link': "https://blog.gregbrockman.com/",
        'quell_titel': "Greg Brockman on Svbtle",
        'datum_aussage': "2022-06-15",
        'sprache': 'en',
        'kontext': "Blog-Post über den Durchbruch von KI-Modellen zur praktischen Nutzbarkeit",
        'aussage_uebersetzung_de': "KI hat kürzlich eine Nützlichkeitsschwelle überschritten, bei der hochmoderne Modelle wie GPT-3, Codex und DALL-E 2 tatsächlich nützlich sind und Aufgaben ausführen können, die Computer auf keine andere Weise tun können."
    },
    {
        'aussage_text': "We have called for international governance of AGI before such calls were popular. We need a very tight feedback loop, rigorous testing, careful consideration at every step, world-class security, and harmony of safety and capabilities.",
        'aussage_kurz': "OpenAI forderte internationale AGI-Governance früh - braucht enge Feedbackschleifen und Sicherheit",
        'modus': 'schriftlich',
        'quellen_typ_id': 5,  # Social-Media-Post
        'plattform_id': 2,  # Twitter/X
        'quell_link': "https://x.com/gdb/status/1791869138132218351",
        'quell_titel': "Greg Brockman on X about OpenAI safety approach",
        'datum_aussage': "2024-05-18",
        'sprache': 'en',
        'kontext': "X-Thread als Antwort auf Kritik an OpenAIs Sicherheitsansatz",
        'aussage_uebersetzung_de': "Wir haben internationale Governance für AGI gefordert, bevor solche Aufrufe populär waren. Wir brauchen eine sehr enge Feedbackschleife, rigorose Tests, sorgfältige Überlegung bei jedem Schritt, erstklassige Sicherheit und Harmonie von Sicherheit und Fähigkeiten."
    }
]

# Sammlung aller Handlungen von Greg Brockman
HANDLUNGEN = [
    {
        'handlung_typ': 'gruendung',
        'beschreibung': "Mitgründung von OpenAI zusammen mit Sam Altman, Ilya Sutskever, Elon Musk und anderen",
        'datum_handlung': "2015-12-11",
        'quell_link': "https://en.wikipedia.org/wiki/Greg_Brockman",
        'quell_titel': "Greg Brockman - Wikipedia",
        'kontext': "Gründung von OpenAI als Non-Profit-Organisation zur Entwicklung sicherer AGI. OpenAI startete zunächst in Brockmans Wohnzimmer."
    },
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': "Rücktritt als CTO von Stripe, um sich OpenAI zu widmen",
        'datum_handlung': "2015-05-01",
        'quell_link': "https://en.wikipedia.org/wiki/Greg_Brockman",
        'quell_titel': "Greg Brockman - Wikipedia",
        'kontext': "Brockman war seit 2013 der erste CTO von Stripe (bei nur 5 Mitarbeitern gestartet, bis auf 205 angewachsen) und verließ das Unternehmen, um OpenAI mitzugründen."
    },
    {
        'handlung_typ': 'politisch',
        'beschreibung': "Aussage vor dem US-Kongress zur KI-Regulierung und -Sicherheit",
        'datum_handlung': "2018-06-26",
        'quell_link': "https://www.congress.gov/115/meeting/house/108474/witnesses/HHRG-115-SY15-Wstate-BrockmanG-20180626.pdf",
        'quell_titel': "Testimony of Mr. Greg Brockman - Congress.gov",
        'kontext': "Brockman empfahl dem Kongress: 1) Kooperation bei offener Grundlagenforschung, 2) Öffentliche Messungen und Wettbewerbe, 3) Verstärkte Koordination zwischen Industrie und Regierung zu Sicherheit und Ethik."
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': "Öffentliche Präsentation von GPT-4 in einem Live-Video-Demo",
        'datum_handlung': "2023-03-14",
        'quell_link': "https://en.wikipedia.org/wiki/Greg_Brockman",
        'quell_titel': "Greg Brockman - Wikipedia",
        'kontext': "Brockman stellte GPT-4 der Öffentlichkeit vor und demonstrierte die Fähigkeiten des Modells live."
    },
    {
        'handlung_typ': 'produktlaunch',
        'beschreibung': "Live-Demo von unreleased ChatGPT-Plugins bei TED2023",
        'datum_handlung': "2023-04-17",
        'quell_link': "https://blog.ted.com/openai-cofounder-greg-brockman-demos-unreleased-chatgpt-plug-ins-live-at-ted2023/",
        'quell_titel': "OpenAI cofounder Greg Brockman demos new ChatGPT plug-ins – live at TED2023",
        'kontext': "Brockman demonstrierte live bei TED2023, wie ChatGPT mit Plugins Rezepte erstellen, Bilder generieren, Tweets verfassen und Einkaufslisten in Instacart erstellen kann."
    },
    {
        'handlung_typ': 'ruecktritt',
        'beschreibung': "Rücktritt als President von OpenAI nach Sam Altmans Entlassung durch das Board",
        'datum_handlung': "2023-11-17",
        'quell_link': "https://techcrunch.com/2023/11/17/greg-brockman-quits-openai-after-abrupt-firing-of-sam-altman/",
        'quell_titel': "Greg Brockman quits OpenAI after abrupt firing of Sam Altman",
        'kontext': "Brockman trat zurück, nachdem das Board Sam Altman entlassen und ihn selbst vom Board entfernt hatte. Er schrieb: 'Sam and I are shocked and saddened by what the board did today.'"
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': "Rückkehr zu OpenAI als President nach der Neubildung des Boards und Altmans Rückkehr",
        'datum_handlung': "2023-11-21",
        'quell_link': "https://openai.com/index/review-completed-altman-brockman-to-continue-to-lead-openai/",
        'quell_titel': "Review completed & Altman, Brockman to continue to lead OpenAI",
        'kontext': "Nach intensiven Verhandlungen kehrten sowohl Altman als CEO als auch Brockman als President zu OpenAI zurück, mit einem neu zusammengesetzten Board."
    },
    {
        'handlung_typ': 'sonstiges',
        'beschreibung': "Beginn eines dreimonatigen Sabbaticals von OpenAI - erstes Mal Entspannung nach 9 Jahren",
        'datum_handlung': "2024-08-05",
        'quell_link': "https://x.com/gdb/status/1820644694264791459",
        'quell_titel': "Greg Brockman on X announcing sabbatical",
        'kontext': "Brockman kündigte auf X an, dass er ein Sabbatical bis Jahresende nimmt. Dies fiel zeitlich mit dem Weggang mehrerer OpenAI-Führungskräfte zusammen."
    },
    {
        'handlung_typ': 'einstellung',
        'beschreibung': "Rückkehr zu OpenAI nach dreimonatigem Sabbatical",
        'datum_handlung': "2024-11-12",
        'quell_link': "https://www.cnbc.com/2024/11/12/openai-co-founder-greg-brockman-returns-after-three-months-of-leave.html",
        'quell_titel': "OpenAI co-founder Greg Brockman returns after three months of leave",
        'kontext': "Brockman kündigte auf X an: 'My longest vacation ever. Back to building OpenAI.' Er arbeitet nun mit Sam Altman an einer neuen Rolle, die ihm erlaubt, sich auf wichtige technische Herausforderungen zu konzentrieren."
    },
    {
        'handlung_typ': 'umstrukturierung',
        'beschreibung': "Ankündigung der neuen Rechtsstruktur OpenAI LP zur besseren Verfolgung der AGI-Mission",
        'datum_handlung': "2019-03-11",
        'quell_link': "https://blog.gregbrockman.com/the-openai-mission",
        'quell_titel': "The OpenAI Mission - Greg Brockman",
        'kontext': "Brockman und Sutskever kündigten die neue 'capped-profit' Struktur OpenAI LP an, um mehr Kapital für die sichere Entwicklung von AGI aufnehmen zu können."
    },
    {
        'handlung_typ': 'partnerschaft',
        'beschreibung': "Öffentliches Auftreten bei AMD CEO Lisa Sus Keynote auf der CES 2026",
        'datum_handlung': "2026-01-09",
        'quell_link': "https://techcrunch.com/snippet/3080158/openai-co-founder-greg-brockman-just-wants-more-compute/",
        'quell_titel': "OpenAI co-founder Greg Brockman just wants more compute",
        'kontext': "Brockman sprach bei AMDs CES-Keynote über ChatGPT und die Notwendigkeit von mehr Rechenleistung, was eine enge Zusammenarbeit zwischen OpenAI und AMD signalisiert."
    }
]

def main():
    """Hauptfunktion zum Einfügen der Daten."""
    print("=" * 80)
    print("GREG BROCKMAN - Datensammlung für Aussagen und Handlungen")
    print("=" * 80)
    print(f"\nPerson ID: {PERSON_ID}")
    print(f"Datenbankpfad: {DB_PATH}")
    print(f"\nZiel: Tier 2 (mind. 10 Aussagen + mind. 8 Handlungen)")
    print(f"Geplant: {len(AUSSAGEN)} Aussagen, {len(HANDLUNGEN)} Handlungen")
    print("=" * 80)

    # Suchprotokoll
    print("\nSUCHPROTOKOLL:")
    print("-" * 80)
    search_queries = [
        "Greg Brockman OpenAI quotes interviews 2023 2024",
        "Greg Brockman artificial intelligence safety AGI statements",
        "Greg Brockman Twitter OpenAI resignation departure 2024",
        "Greg Brockman keynote speech conference AI development",
        "Greg Brockman OpenAI founding 2015 investment Stripe CTO",
        "Greg Brockman ChatGPT launch GPT-4 development role",
        "Greg Brockman Congress testimony AI regulation 2018",
        "Greg Brockman Sam Altman firing board November 2023",
        "Greg Brockman exact quotes TED talk 2023",
        "Greg Brockman X Twitter posts 2024 sabbatical mission AGI",
        "Greg Brockman blog post OpenAI mission statement"
    ]

    for i, query in enumerate(search_queries, 1):
        print(f"{i:2d}. {query}")

    print("\nHAUPTQUELLEN:")
    print("-" * 80)
    sources = [
        "TechCrunch - Interview with OpenAI's Greg Brockman (March 2023)",
        "Axios - Check-in with Open AI's Greg Brockman (March 2023)",
        "TED2023 - The inside story of ChatGPT's astonishing potential",
        "X/Twitter - @gdb (Greg Brockmans offizieller Account)",
        "Fortune - OpenAI master builder interviews (2023-2025)",
        "Congress.gov - Testimony of Mr. Greg Brockman (June 2018)",
        "Greg Brockman's Blog - blog.gregbrockman.com",
        "Wikipedia - Greg Brockman & OpenAI entries",
        "CNBC - OpenAI leadership coverage"
    ]

    for source in sources:
        print(f"  • {source}")

    print("\n" + "=" * 80)
    print("Starte Datenbankoperationen...")
    print("=" * 80 + "\n")

    # Datenbankverbindung
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    aussagen_count = 0
    handlungen_count = 0

    try:
        # Aussagen einfügen
        print("AUSSAGEN EINFUEGEN:")
        print("-" * 80)
        for aussage in AUSSAGEN:
            if insert_aussage(cursor, aussage):
                aussagen_count += 1

        print("\n" + "=" * 80)
        print("\nHANDLUNGEN EINFUEGEN:")
        print("-" * 80)
        for handlung in HANDLUNGEN:
            if insert_handlung(cursor, handlung):
                handlungen_count += 1

        # Commit
        conn.commit()

        # Abschlussbericht
        print("\n" + "=" * 80)
        print("ERFOLGREICH ABGESCHLOSSEN!")
        print("=" * 80)
        print(f"\nSTATISTIK:")
        print(f"  - Aussagen eingefuegt: {aussagen_count} von {len(AUSSAGEN)} geplant")
        print(f"  - Handlungen eingefuegt: {handlungen_count} von {len(HANDLUNGEN)} geplant")
        print(f"\nTIER-STATUS:")

        if aussagen_count >= 10 and handlungen_count >= 8:
            print(f"  [OK] Tier 2 erreicht! ({aussagen_count} Aussagen >= 10, {handlungen_count} Handlungen >= 8)")
        else:
            print(f"  [!] Tier 2 noch nicht erreicht!")
            if aussagen_count < 10:
                print(f"     Fehlende Aussagen: {10 - aussagen_count}")
            if handlungen_count < 8:
                print(f"     Fehlende Handlungen: {8 - handlungen_count}")

        print("\n" + "=" * 80)
        print(f"Zeitstempel: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)

    except Exception as e:
        print(f"\n[ERROR] FEHLER: {e}")
        conn.rollback()
        raise

    finally:
        conn.close()

if __name__ == "__main__":
    main()
