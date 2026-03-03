#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sammle Aussagen und Handlungen von Noam Shazeer (person_id=30)
für die Datenbank aussagen_top100.db

Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime
import hashlib

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 30  # Noam Shazeer

# Suchprotokoll
search_log = []

def log_search(query, source):
    """Protokolliere durchgeführte Suchen"""
    search_log.append({
        'timestamp': datetime.now().isoformat(),
        'query': query,
        'source': source
    })

def create_hash(text):
    """Erstelle Hash für Duplikatsprüfung"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def check_duplicate_aussage(cursor, aussage_text):
    """Prüfe ob Aussage bereits existiert"""
    cursor.execute("""
        SELECT id FROM aussagen
        WHERE person_id = ? AND aussage_text = ?
    """, (PERSON_ID, aussage_text))
    return cursor.fetchone() is not None

def check_duplicate_handlung(cursor, beschreibung):
    """Prüfe ob Handlung bereits existiert"""
    cursor.execute("""
        SELECT id FROM handlungen
        WHERE person_id = ? AND beschreibung = ?
    """, (PERSON_ID, beschreibung))
    return cursor.fetchone() is not None

def insert_aussage(cursor, aussage_data):
    """Füge Aussage ein wenn nicht bereits vorhanden"""
    if check_duplicate_aussage(cursor, aussage_data['aussage_text']):
        print(f"  [SKIP] Aussage bereits vorhanden: {aussage_data['aussage_kurz'][:50]}...")
        return False

    aussage_data['person_id'] = PERSON_ID

    cursor.execute("""
        INSERT INTO aussagen (
            person_id, aussage_text, aussage_kurz, aussage_uebersetzung_de,
            modus, quellen_typ_id, plattform_id, quell_link, quell_titel,
            datum_aussage, sprache, kontext
        ) VALUES (
            :person_id, :aussage_text, :aussage_kurz, :aussage_uebersetzung_de,
            :modus, :quellen_typ_id, :plattform_id, :quell_link, :quell_titel,
            :datum_aussage, :sprache, :kontext
        )
    """, aussage_data)
    print(f"  [OK] Aussage eingefügt: {aussage_data['aussage_kurz'][:60]}...")
    return True

def insert_handlung(cursor, handlung_data):
    """Füge Handlung ein wenn nicht bereits vorhanden"""
    if check_duplicate_handlung(cursor, handlung_data['beschreibung']):
        print(f"  [SKIP] Handlung bereits vorhanden: {handlung_data['beschreibung'][:50]}...")
        return False

    handlung_data['person_id'] = PERSON_ID

    cursor.execute("""
        INSERT INTO handlungen (
            person_id, handlung_typ, beschreibung, datum_handlung,
            quell_link, quell_titel, kontext
        ) VALUES (
            :person_id, :handlung_typ, :beschreibung, :datum_handlung,
            :quell_link, :quell_titel, :kontext
        )
    """, handlung_data)
    print(f"  [OK] Handlung eingefügt: {handlung_data['beschreibung'][:60]}...")
    return True

def main():
    print("="*80)
    print("NOAM SHAZEER - Datensammlung für aussagen_top100.db")
    print("="*80)
    print(f"Person ID: {PERSON_ID}")
    print(f"Ziel: Tier 2 (min. 10 Aussagen + min. 8 Handlungen)")
    print()

    # Protokolliere Suchquellen
    log_search("Noam Shazeer quotes interviews statements 2024 2023", "WebSearch")
    log_search("Noam Shazeer Character.AI Google DeepMind return deal", "WebSearch")
    log_search("Noam Shazeer Attention Is All You Need transformer paper interview", "WebSearch")
    log_search("Noam Shazeer Meena chatbot 2020 Google controversy", "WebSearch")
    log_search("Noam Shazeer AI ethics responsibility statements", "WebSearch")
    log_search("Noam Shazeer future AI predictions scaling laws", "WebSearch")
    log_search("Noam Shazeer GTC 2024 NVIDIA Jensen Huang transformer panel", "WebSearch")
    log_search("Noam Shazeer CNBC interview technology paradigm shift", "WebSearch")
    log_search("Noam Shazeer Dwarkesh podcast Jeff Dean AGI interview 2025", "WebSearch")

    # Aussagen basierend auf recherchierten Quellen
    aussagen = [
        {
            'aussage_text': "No. Not yet. [...] We're going to work on it as the technology improves",
            'aussage_kurz': "Keine Angst vor AGI-Risiko (noch nicht), will daran arbeiten",
            'aussage_uebersetzung_de': "Nein. Noch nicht. [...] Wir werden daran arbeiten, während sich die Technologie verbessert",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.cnbc.com/video/2023/09/07/character-ai-ceo-on-scaling-business-future-of-ai-and-monetization.html',
            'quell_titel': 'Character.AI CEO Noam Shazeer on future of AI',
            'datum_aussage': '2023-09-07',
            'sprache': 'en',
            'kontext': 'Antwort auf die Frage, ob er Angst habe, dass AGI die Welt zerstören wird'
        },
        {
            'aussage_text': "My best guess is divine benevolence [...] Nobody really understands what's going on.",
            'aussage_kurz': "LLMs funktionieren durch 'göttliche Güte', niemand versteht es wirklich",
            'aussage_uebersetzung_de': "Meine beste Vermutung ist göttliche Güte [...] Niemand versteht wirklich, was vor sich geht.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.cnbc.com/video/2023/09/07/character-ai-ceo-on-scaling-business-future-of-ai-and-monetization.html',
            'quell_titel': 'Character.AI CEO on future of AI',
            'datum_aussage': '2023-09-07',
            'sprache': 'en',
            'kontext': 'Erklärung, warum Large Language Models so gut funktionieren'
        },
        {
            'aussage_text': "This is a very experimental science [...] It's more like alchemy or whatever chemistry was in the Middle Ages.",
            'aussage_kurz': "KI-Forschung ist experimentelle Wissenschaft wie Alchemie",
            'aussage_uebersetzung_de': "Dies ist eine sehr experimentelle Wissenschaft [...] Es ist eher wie Alchemie oder was auch immer Chemie im Mittelalter war.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.cnbc.com/video/2023/09/07/character-ai-ceo-on-scaling-business-future-of-ai-and-monetization.html',
            'quell_titel': 'Character.AI CEO on future of AI',
            'datum_aussage': '2023-09-07',
            'sprache': 'en',
            'kontext': 'Charakterisierung des aktuellen Stands der KI-Forschung'
        },
        {
            'aussage_text': "The next step for me was doing my best to get that technology out there to billions of users. That's why I decided to leave Google for a startup, which can move faster.",
            'aussage_kurz': "Verließ Google um Technologie schneller zu Milliarden Nutzern zu bringen",
            'aussage_uebersetzung_de': "Der nächste Schritt für mich war, mein Bestes zu tun, um diese Technologie zu Milliarden von Nutzern zu bringen. Deshalb habe ich mich entschieden, Google für ein Startup zu verlassen, das sich schneller bewegen kann.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://time.com/collection/time100-ai/6310599/noam-shazeer/',
            'quell_titel': 'Noam Shazeer: The 100 Most Influential People in AI 2023 | TIME',
            'datum_aussage': '2023-09-01',
            'sprache': 'en',
            'kontext': 'Begründung für das Verlassen von Google und Gründung von Character.AI'
        },
        {
            'aussage_text': "If users are looking for porn, they need to do it somewhere else.",
            'aussage_kurz': "Pornografische Inhalte nicht auf Character.AI erlaubt",
            'aussage_uebersetzung_de': "Wenn Nutzer nach Pornografie suchen, müssen sie das woanders tun.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://time.com/collection/time100-ai/6310599/noam-shazeer/',
            'quell_titel': 'Noam Shazeer: The 100 Most Influential People in AI 2023',
            'datum_aussage': '2023-09-01',
            'sprache': 'en',
            'kontext': 'Statement zu Content-Moderation und unangemessenen sexuellen Inhalten auf Character.AI'
        },
        {
            'aussage_text': "It is important for users to follow our terms of service, and we will take action when appropriate when users violate our policies and standards.",
            'aussage_kurz': "Nutzer müssen Nutzungsbedingungen folgen, Verstöße werden geahndet",
            'aussage_uebersetzung_de': "Es ist wichtig, dass Nutzer unseren Nutzungsbedingungen folgen, und wir werden angemessen handeln, wenn Nutzer gegen unsere Richtlinien und Standards verstoßen.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://time.com/collection/time100-ai/6310599/noam-shazeer/',
            'quell_titel': 'TIME100 AI 2023',
            'datum_aussage': '2023-09-01',
            'sprache': 'en',
            'kontext': 'Statement zu Nutzerverantwortung und Plattform-Governance'
        },
        {
            'aussage_text': "According to the papers OpenAI has been publishing, they haven't seen any signs that the quality improvements plateau as they make the models bigger. So I don't see any end in sight.",
            'aussage_kurz': "Keine Anzeichen für Plateau bei größeren Modellen, kein Ende in Sicht",
            'aussage_uebersetzung_de': "Laut den Papers, die OpenAI veröffentlicht hat, haben sie keine Anzeichen dafür gesehen, dass die Qualitätsverbesserungen sich abflachen, wenn sie die Modelle größer machen. Also sehe ich kein Ende in Sicht.",
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 1,  # YouTube
            'quell_link': 'https://www.deeplearning.ai/the-batch/ai-transformed/',
            'quell_titel': 'Noam Shazeer Explains How He Co-Created the AI Transformer',
            'datum_aussage': '2023-05-01',
            'sprache': 'en',
            'kontext': 'Perspektive auf zukünftige Skalierung von Sprachmodellen'
        },
        {
            'aussage_text': "Transformer is a better tool for understanding language. That's very exciting, and it's going to affect a lot of applications at Google like translation, search, and accessibility.",
            'aussage_kurz': "Transformer ist besseres Werkzeug für Sprachverständnis, wird viele Anwendungen beeinflussen",
            'aussage_uebersetzung_de': "Transformer ist ein besseres Werkzeug zum Verstehen von Sprache. Das ist sehr aufregend und wird viele Anwendungen bei Google beeinflussen, wie Übersetzung, Suche und Barrierefreiheit.",
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 1,  # YouTube
            'quell_link': 'https://www.deeplearning.ai/the-batch/ai-transformed/',
            'quell_titel': 'Noam Shazeer Explains How He Co-Created the AI Transformer',
            'datum_aussage': '2023-05-01',
            'sprache': 'en',
            'kontext': 'Diskussion über die Auswirkungen des Transformers'
        },
        {
            'aussage_text': "We could have done the industrial revolution on the steam engine, but it would just have been a pain.",
            'aussage_kurz': "RNNs sind wie Dampfmaschinen, Transformer wie Verbrennungsmotoren",
            'aussage_uebersetzung_de': "Wir hätten die industrielle Revolution mit der Dampfmaschine machen können, aber es wäre einfach mühsam gewesen.",
            'modus': 'muendlich',
            'quellen_typ_id': 4,  # Panel-Diskussion
            'plattform_id': 4,  # Konferenzen
            'quell_link': 'https://blogs.nvidia.com/blog/gtc-2024-transformer-ai-research-panel-jensen/',
            'quell_titel': 'NVIDIA GTC 2024 - Transformer AI Research Panel',
            'datum_aussage': '2024-03-20',
            'sprache': 'en',
            'kontext': 'Vergleich von RNNs zu Transformers bei der GTC 2024 Panel-Diskussion mit Jensen Huang'
        },
        {
            'aussage_text': "Some of the big unlocks we're working on are to just train a bigger, smarter model. The scaling laws are going to take us a pretty long way.",
            'aussage_kurz': "Skalierungsgesetze werden uns noch weit bringen",
            'aussage_uebersetzung_de': "Einige der großen Durchbrüche, an denen wir arbeiten, bestehen darin, einfach ein größeres, intelligenteres Modell zu trainieren. Die Skalierungsgesetze werden uns noch ziemlich weit bringen.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://a16z.com/universally-accessible-intelligence/',
            'quell_titel': 'Universally Accessible Intelligence | Andreessen Horowitz',
            'datum_aussage': '2023-06-15',
            'sprache': 'en',
            'kontext': 'Diskussion über zukünftige KI-Entwicklungen und Skalierung'
        },
        {
            'aussage_text': "There is capacity there to scale these things up by orders of magnitude.",
            'aussage_kurz': "Kapazität für Skalierung um Größenordnungen vorhanden",
            'aussage_uebersetzung_de': "Es gibt die Kapazität, diese Dinge um Größenordnungen zu skalieren.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://a16z.com/universally-accessible-intelligence/',
            'quell_titel': 'Universally Accessible Intelligence | a16z',
            'datum_aussage': '2023-06-15',
            'sprache': 'en',
            'kontext': 'Über die Kosten und Skalierbarkeit von KI-Modellen'
        },
        {
            'aussage_text': "One of the big areas of improvement in the near future is inference time compute, applying more compute at inference time.",
            'aussage_kurz': "Inference-Time-Compute ist wichtiger Verbesserungsbereich",
            'aussage_uebersetzung_de': "Einer der großen Verbesserungsbereiche in naher Zukunft ist Inferenz-Zeit-Compute, also mehr Rechenleistung zur Inferenzzeit anzuwenden.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.dwarkesh.com/p/jeff-dean-and-noam-shazeer',
            'quell_titel': 'Jeff Dean & Noam Shazeer — 25 years at Google: from PageRank to AGI',
            'datum_aussage': '2025-01-15',
            'sprache': 'en',
            'kontext': 'Dwarkesh Podcast über zukünftige KI-Entwicklungen'
        },
        {
            'aussage_text': "The biggest thing is just scale.",
            'aussage_kurz': "Das Wichtigste ist einfach Skalierung",
            'aussage_uebersetzung_de': "Das Wichtigste ist einfach die Skalierung.",
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://a16z.com/universally-accessible-intelligence/',
            'quell_titel': 'Universally Accessible Intelligence',
            'datum_aussage': '2023-06-15',
            'sprache': 'en',
            'kontext': 'Diskussion über die wichtigsten Faktoren für KI-Fortschritt'
        },
    ]

    # Handlungen basierend auf recherchierten Ereignissen
    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-Gründung von Character.AI zusammen mit Daniel De Freitas nach Verlassen von Google',
            'datum_handlung': '2021-12-01',
            'quell_link': 'https://www.cnbc.com/2024/08/02/ex-google-engineers-from-characterai-re-join-company-with-ai-partnership-.html',
            'quell_titel': 'Ex-Google engineers who founded Character.AI rejoin company',
            'kontext': 'Shazeer und De Freitas verließen Google nachdem das Unternehmen sich weigerte, ihren Chatbot Meena zu veröffentlichen'
        },
        {
            'handlung_typ': 'ruecktritt',
            'beschreibung': 'Verlassen von Google nach 20 Jahren aufgrund von Frustration über nicht veröffentlichten Meena-Chatbot',
            'datum_handlung': '2021-10-01',
            'quell_link': 'https://gulfnews.com/special-reports/noam-shazeer-after-20-years-at-google-he-walked-away-then-came-back-for-27-billion-1.1734670875849',
            'quell_titel': 'Noam Shazeer: After 20 years at Google, he walked away',
            'kontext': 'Google-Führungskräfte lehnten 2020 die Veröffentlichung von Meena ab aus Sicherheits- und Fairness-Bedenken'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Character.AI erhält $150M Series A Funding von Andreessen Horowitz bei $1 Milliarde Bewertung',
            'datum_handlung': '2023-03-23',
            'quell_link': 'https://www.businesswire.com/news/home/20230323005299/en/Personalized-Superintelligence-Platform-Character.AI-Secures-$150M-in-Series-A-Funding-Led-by-Andreessen-Horowitz',
            'quell_titel': 'Character.AI Secures $150M in Series A Funding Led by Andreessen Horowitz',
            'kontext': 'Weitere Investoren: Nat Friedman (ehem. GitHub CEO), Elad Gil, SV Angel und A Capital'
        },
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Google lizenziert Character.AI Technologie für $2.7 Milliarden, Shazeer erhält hunderte Millionen Dollar',
            'datum_handlung': '2024-08-02',
            'quell_link': 'https://techcrunch.com/2024/08/02/character-ai-ceo-noam-shazeer-returns-to-google/',
            'quell_titel': 'Character.AI CEO Noam Shazeer returns to Google',
            'kontext': 'Lizenzvereinbarung statt vollständiger Übernahme, um regulatorische Hürden zu umgehen'
        },
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'Rückkehr zu Google DeepMind als Technical Co-Lead von Gemini für geschätzt $2.7 Milliarden Deal',
            'datum_handlung': '2024-08-02',
            'quell_link': 'https://www.cnbc.com/2024/08/02/ex-google-engineers-from-characterai-re-join-company-with-ai-partnership-.html',
            'quell_titel': 'Ex-Google engineers from Character.AI re-join company',
            'kontext': 'Zusammen mit Jeff Dean und Oriol Vinyals als Gemini Co-Lead; bezeichnet als einer der teuersten Tech-Talente aller Zeiten'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Co-Autor des wissenschaftlichen Papers "Attention Is All You Need" über Transformer-Architektur',
            'datum_handlung': '2017-06-12',
            'quell_link': 'https://arxiv.org/abs/1706.03762',
            'quell_titel': 'Attention Is All You Need',
            'kontext': 'Bahnbrechendes Paper mit über 100.000 Zitationen; entwickelte scaled dot-product attention und multi-head attention'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Entwicklung und interne Tests von Meena Chatbot bei Google (nicht öffentlich veröffentlicht)',
            'datum_handlung': '2020-02-01',
            'quell_link': 'https://www.business-standard.com/world-news/google-hesitated-on-his-chatbot-now-spends-2-7-bn-to-rehire-ai-pioneer-124100100527_1.html',
            'quell_titel': 'Google hesitated on his chatbot, now spends $2.7 bn to rehire AI pioneer',
            'kontext': 'Meena war ein hochentwickelter Chatbot, Google lehnte öffentliche Demo ab; OpenAI veröffentlichte ChatGPT ein Jahr später'
        },
        {
            'handlung_typ': 'lobbying',
            'beschreibung': 'Untersuchung durch US-Justizministerium ob Google-Character.AI Deal Kartellrecht umging',
            'datum_handlung': '2024-09-01',
            'quell_link': 'https://www.calcalistech.com/ctechnews/article/sy06wllflg',
            'quell_titel': "Google's $2.7B AI deal with Noam Shazeer's Character.AI draws DOJ attention",
            'kontext': 'DOJ prüft ob die Lizenzstruktur regulatorische Aufsicht umgehen sollte und Kartellgesetze verletzt'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Teilnahme am NVIDIA GTC 2024 Panel mit allen 8 Autoren des Transformer-Papers',
            'datum_handlung': '2024-03-20',
            'quell_link': 'https://blogs.nvidia.com/blog/gtc-2024-transformer-ai-research-panel-jensen/',
            'quell_titel': 'NVIDIA GTC 2024 - Transformer AI Research Panel with Jensen Huang',
            'kontext': 'Panel mit Jensen Huang über die Zukunft von Generativer KI und Transformer-Entwicklung'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Auszeichnung als einer der 100 einflussreichsten Menschen in KI 2023 durch TIME Magazine',
            'datum_handlung': '2023-09-07',
            'quell_link': 'https://time.com/collection/time100-ai/6310599/noam-shazeer/',
            'quell_titel': 'Noam Shazeer: The 100 Most Influential People in AI 2023 | TIME',
            'kontext': 'Anerkennung für Beiträge zur Transformer-Architektur und Character.AI'
        },
    ]

    # Datenbankverbindung
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Aussagen einfügen
        print("\n" + "="*80)
        print("AUSSAGEN EINFÜGEN")
        print("="*80)
        aussagen_count = 0
        for aussage in aussagen:
            if insert_aussage(cursor, aussage):
                aussagen_count += 1

        # Handlungen einfügen
        print("\n" + "="*80)
        print("HANDLUNGEN EINFÜGEN")
        print("="*80)
        handlungen_count = 0
        for handlung in handlungen:
            if insert_handlung(cursor, handlung):
                handlungen_count += 1

        # Commit
        conn.commit()

        # Zusammenfassung
        print("\n" + "="*80)
        print("ZUSAMMENFASSUNG")
        print("="*80)
        print(f"Aussagen eingefügt: {aussagen_count} von {len(aussagen)}")
        print(f"Handlungen eingefügt: {handlungen_count} von {len(handlungen)}")
        print()

        # Tier-Prüfung
        tier_reached = "UNBEKANNT"
        if aussagen_count >= 10 and handlungen_count >= 8:
            tier_reached = "TIER 2 [OK]"
        elif aussagen_count >= 5 and handlungen_count >= 3:
            tier_reached = "TIER 3 (nicht ausreichend)"
        else:
            tier_reached = "TIER 4 (nicht ausreichend)"

        print(f"Status: {tier_reached}")
        print()

        # Suchprotokoll ausgeben
        print("="*80)
        print("SUCHPROTOKOLL")
        print("="*80)
        for entry in search_log:
            print(f"{entry['timestamp']}: {entry['source']}")
            print(f"  Query: {entry['query']}")
        print()

    except Exception as e:
        print(f"\nFEHLER: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

    print("="*80)
    print("FERTIG")
    print("="*80)

if __name__ == "__main__":
    main()
