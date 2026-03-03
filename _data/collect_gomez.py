#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sammle Aussagen und Handlungen von Aidan Gomez (person_id=40)
für die Datenbank aussagen_top100.db

Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime
import hashlib

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 40  # Aidan Gomez

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
    print("AIDAN GOMEZ - Datensammlung für aussagen_top100.db")
    print("="*80)
    print(f"Person ID: {PERSON_ID}")
    print(f"Ziel: Tier 2 (min. 10 Aussagen + min. 8 Handlungen)")
    print()

    # Protokolliere Suchquellen
    log_search("Aidan Gomez Cohere CEO quotes interviews 2024 2025", "WebSearch")
    log_search("Aidan Gomez Attention Is All You Need transformer paper interview statements", "WebSearch")
    log_search("Aidan Gomez AI safety ethics responsibility statements", "WebSearch")
    log_search("Aidan Gomez Cohere enterprise AI RAG retrieval augmented generation", "WebSearch")
    log_search("Aidan Gomez Geoffrey Hinton University of Toronto", "WebSearch")
    log_search("Aidan Gomez Cohere funding Series A B C investors valuation history", "WebSearch")
    log_search("Aidan Gomez Canada AI sovereignty privacy data security", "WebSearch")
    log_search("Aidan Gomez future of AI predictions AGI timeline", "WebSearch")
    log_search("Aidan Gomez interview podcast TED talk video 2023 2024", "WebSearch")
    log_search("Cohere Command R model launch product announcement", "WebSearch")
    log_search("Aidan Gomez Radical Ventures Geoffrey Hinton investment Cohere", "WebSearch")
    log_search("Aidan Gomez Oracle Salesforce Nvidia partnership Cohere", "WebSearch")
    log_search("Aidan Gomez Cohere Canada government deal contract AI", "WebSearch")
    log_search("Aidan Gomez Bell Canada partnership sovereign AI", "WebSearch")

    # Aussagen basierend auf recherchierten Quellen
    aussagen = [
        {
            'aussage_text': "At some point you need to commit and start adopting.",
            'aussage_kurz': "Firmen müssen aufhören PoCs zu testen und KI adoptieren",
            'aussage_uebersetzung_de': "Irgendwann muss man sich verpflichten und mit der Einführung beginnen.",
            'modus': 'muendlich',
            'quellen_typ_id': 4,  # Panel-Diskussion
            'plattform_id': 4,  # Konferenzen
            'quell_link': 'https://thelogic.co/news/cohere-aidan-gomez-collision-2024/',
            'quell_titel': "Cohere's Aidan Gomez says it's time for businesses to commit and start adopting generative AI",
            'datum_aussage': '2024-06-18',
            'sprache': 'en',
            'kontext': 'Statement zu Unternehmen, die in einem "PoC death cycle" (Proof-of-Concept-Tests ohne Implementierung) feststecken'
        },
        {
            'aussage_text': "Privacy is the most important, underrated and under-appreciated bottleneck to AI adoption.",
            'aussage_kurz': "Datenschutz ist der wichtigste, unterschätzte Flaschenhals für KI-Adoption",
            'aussage_uebersetzung_de': "Datenschutz ist der wichtigste, unterschätzte und zu wenig gewürdigte Engpass für die KI-Einführung.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2024/07/06/cohere-ceo-and-ex-google-researcher-aidan-gomez-on-how-ai-makes-money.html',
            'quell_titel': 'Cohere CEO and ex-Google researcher Aidan Gomez on how AI makes money',
            'datum_aussage': '2024-07-06',
            'sprache': 'en',
            'kontext': 'Interview zu Hindernissen bei der Enterprise-KI-Adoption'
        },
        {
            'aussage_text': "There's no one in the field who was around back then working who could have foreseen where we are in terms of technological capability. The models are doing stuff that I personally thought maybe I'd see at the end of my career, maybe in like 40 years.",
            'aussage_kurz': "KI-Entwicklung übertrifft alle Vorhersagen, dachte es würde 40 Jahre dauern",
            'aussage_uebersetzung_de': "Es gibt niemanden in diesem Bereich, der damals gearbeitet hat und vorhersehen konnte, wo wir heute in Bezug auf technologische Fähigkeiten sind. Die Modelle machen Sachen, von denen ich persönlich dachte, ich würde sie vielleicht am Ende meiner Karriere sehen, vielleicht in 40 Jahren.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.cnbc.com/2024/07/06/cohere-ceo-and-ex-google-researcher-aidan-gomez-on-how-ai-makes-money.html',
            'quell_titel': 'Cohere CEO and ex-Google researcher Aidan Gomez on how AI makes money',
            'datum_aussage': '2024-07-06',
            'sprache': 'en',
            'kontext': 'Reflexion über die schnellere als erwartete KI-Entwicklung seit dem Transformer-Paper 2017'
        },
        {
            'aussage_text': "Ensuring there is no third party that can switch you off, there is no foreign entity that can just shut down the operation of your economy or government — we're starting to actually see that happening. It's actually happening and needs to be protected against.",
            'aussage_kurz': "Digitale Souveränität ist kritisch, ausländische Akteure können Wirtschaft/Regierung abschalten",
            'aussage_uebersetzung_de': "Sicherstellen, dass es keine dritte Partei gibt, die Sie abschalten kann, dass es keine ausländische Entität gibt, die einfach den Betrieb Ihrer Wirtschaft oder Regierung lahmlegen kann — wir sehen, dass das tatsächlich passiert. Es passiert wirklich und muss dagegen geschützt werden.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://betakit.com/aidan-gomez-says-cohere-could-ipo-soon-as-company-holds-secondary-sale/',
            'quell_titel': 'Aidan Gomez says Cohere could IPO "soon" as company holds secondary sale',
            'datum_aussage': '2025-10-15',
            'sprache': 'en',
            'kontext': 'Statement zu geopolitischen Risiken und Notwendigkeit von AI-Souveränität für Nationen'
        },
        {
            'aussage_text': "I think public market investors would be excited to have a pure-play AI investment opportunity, as opposed to investing by proxy through hyperscalers.",
            'aussage_kurz': "Öffentliche Märkte wollen direkte KI-Investments statt über Cloud-Provider",
            'aussage_uebersetzung_de': "Ich denke, Investoren am öffentlichen Markt wären begeistert, eine reine KI-Investitionsmöglichkeit zu haben, anstatt indirekt über Hyperscaler zu investieren.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://betakit.com/aidan-gomez-says-cohere-could-ipo-soon-as-company-holds-secondary-sale/',
            'quell_titel': 'Aidan Gomez says Cohere could IPO "soon" as company holds secondary sale',
            'datum_aussage': '2025-10-15',
            'sprache': 'en',
            'kontext': 'Aussage zu möglichem baldigen Cohere-IPO'
        },
        {
            'aussage_text': "We have a differentiated deployment model, we have very high margins similar to a traditional [software-as-a-service] business.",
            'aussage_kurz': "Cohere hat hohe SaaS-ähnliche Margen durch differenziertes Deployment-Modell",
            'aussage_uebersetzung_de': "Wir haben ein differenziertes Bereitstellungsmodell, wir haben sehr hohe Margen ähnlich einem traditionellen [Software-as-a-Service] Geschäft.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://betakit.com/aidan-gomez-says-cohere-could-ipo-soon-as-company-holds-secondary-sale/',
            'quell_titel': 'Aidan Gomez says Cohere could IPO "soon"',
            'datum_aussage': '2025-10-15',
            'sprache': 'en',
            'kontext': 'Erklärung des Geschäftsmodells und Vorhersage, dass Cohere vor 2029 profitabel wird'
        },
        {
            'aussage_text': "I was just trying to understand how attention mechanisms worked. We didn't know it would become the architecture for everything.",
            'aussage_kurz': "Wussten nicht, dass Transformer die Architektur für alles werden würde",
            'aussage_uebersetzung_de': "Ich habe nur versucht zu verstehen, wie Aufmerksamkeitsmechanismen funktionieren. Wir wussten nicht, dass es die Architektur für alles werden würde.",
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 1,  # YouTube
            'quell_link': 'https://digidai.github.io/2025/11/11/aidan-gomez-cohere-ceo-deep-analysis/',
            'quell_titel': 'Aidan Gomez: Cohere CEO & Transformer Co-Author',
            'datum_aussage': '2023-05-01',
            'sprache': 'en',
            'kontext': 'Reflexion über die Arbeit am "Attention Is All You Need" Paper als 20-jähriger Google Brain Intern'
        },
        {
            'aussage_text': "AI models will no longer be stateless, but will be actively learning from experience.",
            'aussage_kurz': "KI-Modelle werden aktiv aus Erfahrung lernen statt statisch zu sein",
            'aussage_uebersetzung_de': "KI-Modelle werden nicht länger zustandslos sein, sondern werden aktiv aus Erfahrung lernen.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.golan.ai/ai-news/the-future-of-ai-in-2026-major-predictions-from-top-ceos-RfA2Ug4FuaY',
            'quell_titel': 'The Future of AI in 2026: Major Predictions from Top CEOs',
            'datum_aussage': '2025-12-15',
            'sprache': 'en',
            'kontext': 'Vorhersage für 2026: Durchbrüche bei Continual Learning, wo KI-Modelle aus Interaktionen und Fehlern lernen können'
        },
        {
            'aussage_text': "When a model fails at a task, it will be able to learn from that failure and remember the correct way to perform the task, continuously improving over time.",
            'aussage_kurz': "Zukünftige Modelle lernen aus Fehlern und verbessern sich kontinuierlich",
            'aussage_uebersetzung_de': "Wenn ein Modell bei einer Aufgabe scheitert, wird es in der Lage sein, aus diesem Fehler zu lernen und sich an den richtigen Weg zu erinnern, die Aufgabe zu erledigen, und sich kontinuierlich im Laufe der Zeit zu verbessern.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.golan.ai/ai-news/the-future-of-ai-in-2026-major-predictions-from-top-ceos-RfA2Ug4FuaY',
            'quell_titel': 'The Future of AI in 2026: Major Predictions from Top CEOs',
            'datum_aussage': '2025-12-15',
            'sprache': 'en',
            'kontext': 'Vision für kontinuierliches Lernen in KI-Systemen'
        },
        {
            'aussage_text': "We have the potential to be truly transformative for organizations looking to massively increase their productivity and efficiency without any compromise on data security and privacy.",
            'aussage_kurz': "KI kann Produktivität massiv steigern ohne Kompromisse bei Sicherheit/Datenschutz",
            'aussage_uebersetzung_de': "Wir haben das Potenzial, wirklich transformativ zu sein für Organisationen, die ihre Produktivität und Effizienz massiv steigern wollen, ohne Kompromisse bei Datensicherheit und Datenschutz einzugehen.",
            'modus': 'muendlich',
            'quellen_typ_id': 10,  # Offizielle Stellungnahme
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://www.newswire.ca/news-releases/bell-canada-and-cohere-forge-strategic-partnership-to-deliver-sovereign-ai-powered-solutions-for-government-and-business-888382855.html',
            'quell_titel': 'Bell Canada and Cohere forge strategic partnership to deliver sovereign AI-powered solutions',
            'datum_aussage': '2025-07-28',
            'sprache': 'en',
            'kontext': 'Statement zur Bell-Cohere Partnerschaft für souveräne KI-Lösungen in Kanada'
        },
        {
            'aussage_text': "A.I. will make people more effective not displace them.",
            'aussage_kurz': "KI macht Menschen effektiver, verdrängt sie nicht",
            'aussage_uebersetzung_de': "KI wird Menschen effektiver machen, sie nicht verdrängen.",
            'modus': 'muendlich',
            'quellen_typ_id': 1,  # Video-Interview
            'plattform_id': 1,  # YouTube
            'quell_link': 'https://www.cnbc.com/video/2023/05/09/a-i-will-make-people-more-effective-not-displace-them-says-cohere-ceo-aidan-gomez.html',
            'quell_titel': 'A.I. will make people more effective not displace them, says Cohere CEO Aidan Gomez',
            'datum_aussage': '2023-05-09',
            'sprache': 'en',
            'kontext': 'CNBC Interview über die Auswirkungen von KI auf Arbeitsplätze'
        },
        {
            'aussage_text': "My dad would bring home math problems from his classes, and we'd work through them at dinner. My mom taught me to think about systems aesthetically, not just functionally. Good design is elegant design.",
            'aussage_kurz': "Familiäre Prägung: Mathe-Probleme mit Vater, ästhetisches Systemdenken von Mutter",
            'aussage_uebersetzung_de': "Mein Vater brachte Mathe-Aufgaben aus seinen Kursen mit nach Hause, und wir haben sie beim Abendessen durchgearbeitet. Meine Mutter lehrte mich, über Systeme ästhetisch nachzudenken, nicht nur funktional. Gutes Design ist elegantes Design.",
            'modus': 'muendlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://digidai.github.io/2025/11/11/aidan-gomez-cohere-ceo-deep-analysis/',
            'quell_titel': 'Aidan Gomez: Cohere CEO & Transformer Co-Author',
            'datum_aussage': '2023-08-01',
            'sprache': 'en',
            'kontext': 'Über seinen familiären Hintergrund und frühe Prägung'
        },
    ]

    # Handlungen basierend auf recherchierten Ereignissen
    handlungen = [
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Co-Autor des wissenschaftlichen Papers "Attention Is All You Need" über Transformer-Architektur als 20-jähriger Google Brain Intern',
            'datum_handlung': '2017-06-12',
            'quell_link': 'https://arxiv.org/abs/1706.03762',
            'quell_titel': 'Attention Is All You Need',
            'kontext': 'Bahnbrechendes Paper als jüngster von 8 Autoren; arbeitete unter Geoffrey Hinton während Studium an University of Toronto'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Co-Gründung von Cohere zusammen mit Nick Frosst (ebenfalls Hinton-Student) und Ivan Zhang',
            'datum_handlung': '2019-11-01',
            'quell_link': 'https://en.wikipedia.org/wiki/Cohere',
            'quell_titel': 'Cohere - Wikipedia',
            'kontext': 'Gründung der Enterprise-KI-Plattform mit Fokus auf Retrieval Augmented Generation (RAG) und Datenschutz'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Cohere erhält $40M Series A Funding von Radical Ventures (Geoffrey Hinton) und Index Ventures',
            'datum_handlung': '2020-11-01',
            'quell_link': 'https://radical.vc/radical-reads-cohere-raises/',
            'quell_titel': 'Cohere raises $40 million Series A financing to make NLP safe and accessible',
            'kontext': 'Radical Ventures war bereits 2019 erster Seed-Investor; Geoffrey Hintons Beteiligung verleiht jungem CEO instant Credibility'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Cohere erhält $125M Series B Funding von Tiger Global',
            'datum_handlung': '2022-02-01',
            'quell_link': 'https://tracxn.com/d/companies/cohere/__o4xfwmr3XwgsGEyH41XvwBm6Xd-SjsMlSld3d4ci6G0/funding-and-investors',
            'quell_titel': 'Cohere Funding Rounds & Investors',
            'kontext': 'Signifikante Expansion der Finanzierung während AI-Boom'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Cohere erhält $270M Series C Funding bei $2.2B Bewertung von Nvidia, Oracle, Salesforce Ventures und Inovia Capital',
            'datum_handlung': '2023-06-01',
            'quell_link': 'https://betakit.com/cohere-announces-270-million-series-c-from-inovia-nvidia-oracle-salesforce/',
            'quell_titel': 'Cohere announces $270-million USD Series C from Inovia, Nvidia, Oracle, Salesforce',
            'kontext': 'Strategische Investoren aus Tech-Industrie; Oracle und Salesforce integrieren Cohere-Technologie in ihre Produkte'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Oracle integriert Cohere-Technologie in Oracle Fusion Cloud, Oracle NetSuite und branchenspezifische Oracle-Anwendungen',
            'datum_handlung': '2023-06-15',
            'quell_link': 'https://erp.today/oracle-salesforce-ventures-and-nvidia-invest-in-cohere/',
            'quell_titel': 'Oracle, Salesforce Ventures and NVIDIA invest in Cohere',
            'kontext': 'Strategische Enterprise-Partnerschaft für generative KI-Services'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Command-R: RAG-optimiertes LLM für Enterprise mit 128k Token Kontext und 10 Sprachen',
            'datum_handlung': '2024-03-01',
            'quell_link': 'https://venturebeat.com/ai/cohere-releases-powerful-command-r-language-model-for-enterprise-use',
            'quell_titel': 'Cohere releases powerful Command-R language model for enterprise use',
            'kontext': 'Während $1B Fundraising-Runde; Modell speziell für Retrieval Augmented Generation optimiert'
        },
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'Launch von Command R+: Advanced Enterprise LLM mit best-in-class RAG mit Zitationen und Tool Use API',
            'datum_handlung': '2024-04-04',
            'quell_link': 'https://venturebeat.com/ai/cohere-launches-command-r-a-powerful-llm-optimized-for-enterprise-ai',
            'quell_titel': 'Cohere launches Command R+, a powerful enterprise LLM that beats GPT-4 Turbo',
            'kontext': 'Command R+ zeigt 30% weniger Compute-Bedarf als vergleichbare OpenAI/Anthropic-Modelle bei RAG-Tasks'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Cohere erhält $500M Series D Funding bei $6.8B Bewertung von Radical Ventures, AMD, Nvidia, Salesforce',
            'datum_handlung': '2025-08-14',
            'quell_link': 'https://techcrunch.com/2025/08/14/cohere-hits-a-6-8b-valuation-as-investors-amd-nvidia-and-salesforce-double-down/',
            'quell_titel': 'Cohere hits a $6.8B valuation as investors AMD, Nvidia, and Salesforce double down',
            'kontext': 'Gesamtkapital erreicht $1.6B; Vorbereitung auf IPO mit potenzieller >$10B Bewertung'
        },
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Bell Canada und Cohere formen strategische Partnerschaft für souveräne Full-Stack-KI-Lösungen in Kanada',
            'datum_handlung': '2025-07-28',
            'quell_link': 'https://www.newswire.ca/news-releases/bell-canada-and-cohere-forge-strategic-partnership-to-deliver-sovereign-ai-powered-solutions-for-government-and-business-888382855.html',
            'quell_titel': 'Bell Canada and Cohere forge strategic partnership to deliver sovereign AI-powered solutions',
            'kontext': 'Cohere-Modelle via Bell AI Fabric mit strikter Datensouveränität; Bell wird preferred Canadian AI infrastructure provider'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Kanadische Regierung unterzeichnet Memorandum of Understanding (MoU) mit Cohere für KI-Einsatz im öffentlichen Dienst',
            'datum_handlung': '2025-08-15',
            'quell_link': 'https://www.canada.ca/en/innovation-science-economic-development/news/2025/08/canada-partners-with-cohere-to-accelerate-world-leading-artificial-intelligence.html',
            'quell_titel': 'Canada partners with Cohere to accelerate world-leading artificial intelligence',
            'kontext': 'Nicht-bindende Vereinbarung als Roadmap für zukünftige Zusammenarbeit; keine Verträge über MoU hinaus vergeben'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Kanadische Regierung finalisiert $240M Investment in Coheres $725M Projekt für kanadische Compute-Kapazität',
            'datum_handlung': '2025-03-01',
            'quell_link': 'https://www.canada.ca/en/innovation-science-economic-development/news/2025/03/government-of-canada-finalizes-investment-to-support-canadian-born-ai-leader-cohere.html',
            'quell_titel': 'Government of Canada finalizes investment to support Canadian-Born AI leader, Cohere',
            'kontext': 'Teil von Kanadas $2B sovereign AI compute Strategie; Cohere partnert mit CoreWeave für Data Center in Cambridge, Ontario'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Cohere verkauft Services an Communications Security Establishment (CSE), Kanadas Cyber-Geheimdienst',
            'datum_handlung': '2024-10-01',
            'quell_link': 'https://thelogic.co/news/exclusive/cohere-communications-security-establishment-government/',
            'quell_titel': 'Cohere had contract with Canadian cyber intelligence agency, documents reveal',
            'kontext': 'Memo für PM Trudeau vor Meeting mit Aidan Gomez vorbereitet; zeigt frühe Regierungsnutzung vor öffentlichem MoU'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Cohere schließt zweite Tranche der Finanzierungsrunde mit zusätzlichen $100M ab, Bewertung steigt auf $7B',
            'datum_handlung': '2025-09-24',
            'quell_link': 'https://techcrunch.com/2025/09/24/cohere-hits-7b-valuation-a-month-after-its-last-raise-partners-with-amd/',
            'quell_titel': 'Cohere hits $7B valuation a month after its last raise, partners with AMD',
            'kontext': 'Neue Investoren: BDC (Business Development Bank of Canada) und Nexxus Capital Management'
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
