#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung: Vinod Khosla (person_id=32)
Tier 2: Mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 32  # Vinod Khosla

def insert_aussagen(cursor):
    """Fügt Aussagen von Vinod Khosla in die Datenbank ein."""

    aussagen = [
        {
            'aussage_text': 'Within the next five years, any economically valuable job humans can do, AI will be able to do 80% of it…80% of all jobs can be done by an AI.',
            'aussage_kurz': '80% aller Jobs können in 5 Jahren von KI erledigt werden',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://fortune.com/2025/07/01/silicon-valley-investor-vinod-khosla-ai-job-prediction-interview/',
            'quell_titel': 'Silicon Valley investor Vinod Khosla predicts AI will replace 80% of jobs by 2030',
            'datum_aussage': '2025-06-01',
            'sprache': 'en',
            'kontext': 'Interview über die Zukunft der Arbeit und KI-Automatisierung',
            'aussage_uebersetzung_de': 'Innerhalb der nächsten fünf Jahre wird KI in der Lage sein, 80% jeder wirtschaftlich wertvollen Arbeit zu erledigen, die Menschen tun können... 80% aller Jobs können von einer KI erledigt werden.'
        },
        {
            'aussage_text': 'The people who don\'t know how to use AI will be obsoleted by people who know how to use AI first.',
            'aussage_kurz': 'Menschen ohne KI-Kenntnisse werden obsolet',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,  # Nachrichtenartikel
            'plattform_id': 5,  # Nachrichtenmedien
            'quell_link': 'https://fortune.com/2025/07/01/silicon-valley-investor-vinod-khosla-ai-job-prediction-interview/',
            'quell_titel': 'Silicon Valley investor Vinod Khosla predicts AI will replace 80% of jobs by 2030',
            'datum_aussage': '2025-06-01',
            'sprache': 'en',
            'kontext': 'Warnung über die Notwendigkeit, KI zu lernen',
            'aussage_uebersetzung_de': 'Die Menschen, die nicht wissen, wie man KI benutzt, werden von denen obsolet gemacht, die wissen, wie man KI benutzt.'
        },
        {
            'aussage_text': 'Technology will replace 80 percent of what doctors do.',
            'aussage_kurz': 'KI wird 80% der ärztlichen Tätigkeit ersetzen',
            'modus': 'schriftlich',
            'quellen_typ_id': 6,  # Blog-Artikel
            'plattform_id': 9,  # Blogs
            'quell_link': 'https://www.khoslaventures.com/fortune-technology-will-replace-80-of-what-doctors-do/',
            'quell_titel': 'Fortune | Technology Will Replace 80-Percent of What Doctors Do',
            'datum_aussage': '2016-01-01',
            'sprache': 'en',
            'kontext': 'Khoslas berühmtes Paper "20 Percent Doctor Included" über die Zukunft der Medizin',
            'aussage_uebersetzung_de': 'Technologie wird 80 Prozent dessen ersetzen, was Ärzte tun.'
        },
        {
            'aussage_text': 'Within 5 to 6 years, the FDA will approve a primary care app qualified to practice medicine like a primary care physician.',
            'aussage_kurz': 'FDA wird in 5-6 Jahren KI-Hausarzt-App genehmigen',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.statnews.com/2023/05/03/artificial-intelligence-doctor-vinod-khosla-ventures/',
            'quell_titel': 'Vinod Khosla predicts AI doctors could be here sooner than you think',
            'datum_aussage': '2023-05-03',
            'sprache': 'en',
            'kontext': 'Interview über KI in der Gesundheitsversorgung',
            'aussage_uebersetzung_de': 'Innerhalb von 5 bis 6 Jahren wird die FDA eine Hausarzt-App genehmigen, die qualifiziert ist, Medizin wie ein Hausarzt zu praktizieren.'
        },
        {
            'aussage_text': 'Almost all expertise will be free — where AI democratizes medical knowledge so completely that barriers to expert care dissolve.',
            'aussage_kurz': 'Nahezu alle Expertise wird kostenlos durch KI',
            'modus': 'schriftlich',
            'quellen_typ_id': 6,  # Blog-Artikel
            'plattform_id': 9,  # Blogs
            'quell_link': 'https://www.khoslaventures.com/posts/a-roadmap-to-ai-utopia',
            'quell_titel': 'A Roadmap to AI Utopia',
            'datum_aussage': '2024-03-15',
            'sprache': 'en',
            'kontext': 'Blog-Post über seine Vision einer KI-Utopie',
            'aussage_uebersetzung_de': 'Nahezu alle Expertise wird kostenlos sein — wo KI medizinisches Wissen so vollständig demokratisiert, dass Barrieren zur Expertenversorgung sich auflösen.'
        },
        {
            'aussage_text': 'Within 15 years, almost all expertise on the planet will be free, including medical, legal, scientific and educational services.',
            'aussage_kurz': 'In 15 Jahren wird alle Expertise kostenlos sein',
            'modus': 'schriftlich',
            'quellen_typ_id': 6,  # Blog-Artikel
            'plattform_id': 9,  # Blogs
            'quell_link': 'https://www.productgeeks.com/p/the-age-of-free-expertise-vinod-khosla',
            'quell_titel': 'The Age of Free Expertise: Vinod Khosla on AI\'s impact',
            'datum_aussage': '2024-06-01',
            'sprache': 'en',
            'kontext': 'Artikel über Khoslas Vision des "Age of Free Expertise"',
            'aussage_uebersetzung_de': 'Innerhalb von 15 Jahren wird nahezu alle Expertise auf dem Planeten kostenlos sein, einschließlich medizinischer, rechtlicher, wissenschaftlicher und Bildungsdienstleistungen.'
        },
        {
            'aussage_text': 'By 2040, the need to work will go away.',
            'aussage_kurz': 'Bis 2040 wird die Notwendigkeit zu arbeiten wegfallen',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://fortune.com/2024/09/24/silicon-valley-billionaire-vinod-khosla-universal-basic-income-ai-80-jobs/',
            'quell_titel': 'Silicon Valley billionaire Vinod Khosla says AI will handle 80% of work in 80% of jobs',
            'datum_aussage': '2024-09-24',
            'sprache': 'en',
            'kontext': 'Interview über die Zukunft der Arbeit',
            'aussage_uebersetzung_de': 'Bis 2040 wird die Notwendigkeit zu arbeiten wegfallen.'
        },
        {
            'aussage_text': 'We could be at a 3 day workweek in 10-20 years, providing the 20% of work we may need or want.',
            'aussage_kurz': '3-Tage-Woche in 10-20 Jahren durch KI möglich',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://fortune.com/2024/09/24/silicon-valley-billionaire-vinod-khosla-universal-basic-income-ai-80-jobs/',
            'quell_titel': 'Silicon Valley billionaire Vinod Khosla says AI will handle 80% of work in 80% of jobs',
            'datum_aussage': '2024-09-24',
            'sprache': 'en',
            'kontext': 'Vision einer stark reduzierten Arbeitswoche durch KI-Automatisierung',
            'aussage_uebersetzung_de': 'Wir könnten in 10-20 Jahren bei einer 3-Tage-Woche sein und die 20% der Arbeit leisten, die wir brauchen oder wollen.'
        },
        {
            'aussage_text': 'Hard for me to support someone with no values, lies, cheats, rapes, demeans women, hates immigrants like me. He may cut my taxes or reduce some regulation but that is no reason to accept depravity in his personal values.',
            'aussage_kurz': 'Kritik an Trump: Keine Unterstützung trotz möglicher Steuersenkungen',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://x.com/vkhosla/status/1815096257867923740',
            'quell_titel': 'Vinod Khosla on X about Trump',
            'datum_aussage': '2024-07-22',
            'sprache': 'en',
            'kontext': 'X-Post nach Bidens Rückzug aus dem Wahlkampf, Kritik an Trump',
            'aussage_uebersetzung_de': 'Es fällt mir schwer, jemanden zu unterstützen, der keine Werte hat, lügt, betrügt, vergewaltigt, Frauen erniedrigt, Immigranten wie mich hasst. Er mag meine Steuern senken oder einige Regulierungen reduzieren, aber das ist kein Grund, die Verkommenheit seiner persönlichen Werte zu akzeptieren.'
        },
        {
            'aussage_text': 'Our democracy is definitely on the line.',
            'aussage_kurz': 'Unsere Demokratie steht auf dem Spiel',
            'modus': 'muendlich',
            'quellen_typ_id': 4,  # Panel-Diskussion
            'plattform_id': 4,  # Konferenzen
            'quell_link': 'https://techcrunch.com/2024/10/28/vinod-khosla-calls-out-trumps-depraved-values-and-musks-role-in-spreading-misinformation/',
            'quell_titel': 'Vinod Khosla calls out Trump\'s \'depraved values\' and Musk\'s role in spreading misinformation',
            'datum_aussage': '2024-10-28',
            'sprache': 'en',
            'kontext': 'Rede auf der TechCrunch Disrupt 2024 Konferenz',
            'aussage_uebersetzung_de': 'Unsere Demokratie steht definitiv auf dem Spiel.'
        },
        {
            'aussage_text': 'Would we open source the Manhattan Project so innovation could happen faster?',
            'aussage_kurz': 'KI-Open-Source ist wie Manhattan Project zu veröffentlichen',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://www.webpronews.com/americas-ai-reckoning-countering-chinas-open-source-onslaught/',
            'quell_titel': 'America\'s AI Reckoning: Countering China\'s Open-Source Onslaught',
            'datum_aussage': '2024-11-02',
            'sprache': 'en',
            'kontext': 'X-Post über die Gefahren von Open-Source-KI im Kontext des KI-Wettlaufs mit China',
            'aussage_uebersetzung_de': 'Würden wir das Manhattan-Projekt als Open Source veröffentlichen, damit Innovation schneller passieren kann?'
        },
        {
            'aussage_text': 'It\'s a national-security hazard to open source AI.',
            'aussage_kurz': 'Open-Source-KI ist ein nationales Sicherheitsrisiko',
            'modus': 'muendlich',
            'quellen_typ_id': 2,  # Podcast-Interview
            'plattform_id': 3,  # Podcasts
            'quell_link': 'https://www.khoslaventures.com/posts/ai-dystopia-or-utopia',
            'quell_titel': 'AI: Dystopia or Utopia?',
            'datum_aussage': '2024-08-15',
            'sprache': 'en',
            'kontext': 'Diskussion über KI-Sicherheit und geopolitische Risiken',
            'aussage_uebersetzung_de': 'Es ist ein nationales Sicherheitsrisiko, KI als Open Source zu veröffentlichen.'
        },
        {
            'aussage_text': 'This is a war for political philosophy: Western values and political philosophy versus Chinese political philosophy.',
            'aussage_kurz': 'KI-Wettlauf ist ein Krieg der politischen Philosophien',
            'modus': 'muendlich',
            'quellen_typ_id': 4,  # Panel-Diskussion
            'plattform_id': 4,  # Konferenzen
            'quell_link': 'https://aparc.fsi.stanford.edu/news/vinod-khosla-shares-insights-future-sino-american-tech-competition',
            'quell_titel': 'Vinod Khosla Shares Insights Into Future of Sino-American Tech Competition',
            'datum_aussage': '2023-05-15',
            'sprache': 'en',
            'kontext': 'Stanford-Vortrag über den technologischen Wettbewerb zwischen USA und China',
            'aussage_uebersetzung_de': 'Dies ist ein Krieg um politische Philosophie: Westliche Werte und politische Philosophie gegen chinesische politische Philosophie.'
        },
        {
            'aussage_text': 'DeepSeek makes the same mistakes O1 makes, a strong indication the technology was ripped off.',
            'aussage_kurz': 'DeepSeek hat OpenAI-Technologie gestohlen (Behauptung)',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,  # Social-Media-Post
            'plattform_id': 2,  # Twitter/X
            'quell_link': 'https://www.cnbc.com/2025/01/30/chinas-deepseek-has-some-big-ai-claims-not-all-experts-are-convinced-.html',
            'quell_titel': 'DeepSeek\'s AI claims have shaken the world — but not everyone\'s convinced',
            'datum_aussage': '2025-01-27',
            'sprache': 'en',
            'kontext': 'X-Post als Reaktion auf die Veröffentlichung des chinesischen DeepSeek R1 KI-Modells',
            'aussage_uebersetzung_de': 'DeepSeek macht die gleichen Fehler wie O1, ein starker Hinweis darauf, dass die Technologie gestohlen wurde.'
        },
        {
            'aussage_text': 'Every economically valuable job will be doable by AI by 2030. AI will free humans to be human.',
            'aussage_kurz': 'Bis 2030 kann KI jeden wirtschaftlich wertvollen Job erledigen',
            'modus': 'muendlich',
            'quellen_typ_id': 3,  # Keynote/Vortrag
            'plattform_id': 16,  # TED
            'quell_link': 'https://www.ted.com/talks/vinod_khosla_12_predictions_for_the_future_of_technology',
            'quell_titel': 'Vinod Khosla: 12 predictions for the future of technology | TED Talk',
            'datum_aussage': '2024-04-15',
            'sprache': 'en',
            'kontext': 'TED Talk 2024 mit 12 Vorhersagen über die Zukunft der Technologie',
            'aussage_uebersetzung_de': 'Jeder wirtschaftlich wertvolle Job wird bis 2030 von KI erledigt werden können. KI wird Menschen befreien, menschlich zu sein.'
        }
    ]

    for aussage in aussagen:
        aussage['person_id'] = PERSON_ID
        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus, quellen_typ_id,
                plattform_id, quell_link, quell_titel, datum_aussage, sprache,
                kontext, aussage_uebersetzung_de
            ) VALUES (
                :person_id, :aussage_text, :aussage_kurz, :modus, :quellen_typ_id,
                :plattform_id, :quell_link, :quell_titel, :datum_aussage, :sprache,
                :kontext, :aussage_uebersetzung_de
            )
        """, aussage)

    print(f"[OK] {len(aussagen)} Aussagen eingefuegt")


def insert_handlungen(cursor):
    """Fügt Handlungen von Vinod Khosla in die Datenbank ein."""

    handlungen = [
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Mitgründung von Sun Microsystems als Chairman und CEO',
            'datum_handlung': '1982-02-24',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Vinod_Khosla',
            'quell_titel': 'Vinod Khosla - Wikipedia',
            'kontext': 'Khosla gründete zusammen mit Scott McNealy, Andy Bechtolsheim und Bill Joy Sun Microsystems, das zu einem führenden Workstation- und Server-Hersteller wurde.'
        },
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Gründung von Khosla Ventures',
            'datum_handlung': '2004-01-01',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Khosla_Ventures',
            'quell_titel': 'Khosla Ventures - Wikipedia',
            'kontext': 'Nach seiner Zeit bei Kleiner Perkins gründete Khosla seine eigene Venture-Capital-Firma mit Fokus auf transformative Technologien und Klimatech.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Erste VC-Investition in OpenAI (5% Anteil)',
            'datum_handlung': '2019-01-01',
            'betrag_usd': 50000000.0,
            'quell_link': 'https://fortune.com/2023/12/04/khosla-ventures-openai-sam-altman/',
            'quell_titel': 'Vinod Khosla details how much his venture firm had on the line during OpenAI\'s Sam Altman drama',
            'kontext': 'Khosla Ventures war der erste VC-Investor in OpenAI. Khosla bezeichnete dies als "die größte Wette um den Faktor zwei meiner ersten Investition, die ich in 40 Jahren gemacht habe".'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Zusätzliche Investition in OpenAI über Special Purpose Vehicle',
            'datum_handlung': '2024-10-01',
            'betrag_usd': 405000000.0,
            'quell_link': 'https://techcrunch.com/2024/10/11/khosla-ventures-just-backed-openai-with-405m-more-but-not-necessarily-with-its-own-capital/',
            'quell_titel': 'Khosla Ventures just backed OpenAI with $405M more',
            'kontext': 'Khosla Ventures sammelte ein Special Purpose Vehicle von 405 Millionen Dollar, um zusätzlich in OpenAI zu investieren.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Investition in Impossible Foods (pflanzliches Fleisch)',
            'datum_handlung': '2015-01-01',
            'betrag_usd': None,
            'quell_link': 'https://www.khoslaventures.com/portfolio',
            'quell_titel': 'Khosla Ventures Portfolio',
            'kontext': 'Frühe Investition in Impossible Foods, Hersteller von pflanzlichem Fleischersatz, als Teil von Khoslas Klimatech-Portfolio.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Investition in Square (Fintech)',
            'datum_handlung': '2009-01-01',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Khosla_Ventures',
            'quell_titel': 'Khosla Ventures - Wikipedia',
            'kontext': 'Frühe Investition in Square (jetzt Block Inc.), das mobile Zahlungsunternehmen von Jack Dorsey, die zu großen Returns führte.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Investition in Instacart (Online-Lebensmittellieferung)',
            'datum_handlung': '2013-01-01',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Khosla_Ventures',
            'quell_titel': 'Khosla Ventures - Wikipedia',
            'kontext': 'Frühe Investition in Instacart, das zu einem der führenden Online-Lebensmittel-Lieferdienste wurde.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Investition in DoorDash (Essenslieferung)',
            'datum_handlung': '2014-01-01',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Khosla_Ventures',
            'quell_titel': 'Khosla Ventures - Wikipedia',
            'kontext': 'Frühe Investition in DoorDash, das zum größten Essenslieferdienst in den USA wurde.'
        },
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Investition in Affirm (Fintech Buy-Now-Pay-Later)',
            'datum_handlung': '2014-01-01',
            'betrag_usd': None,
            'quell_link': 'https://en.wikipedia.org/wiki/Khosla_Ventures',
            'quell_titel': 'Khosla Ventures - Wikipedia',
            'kontext': 'Investition in Affirm, das von PayPal-Mitgründer Max Levchin gegründete Buy-Now-Pay-Later Fintech-Unternehmen.'
        },
        {
            'handlung_typ': 'politisch',
            'beschreibung': 'Öffentliche Kritik an Elon Musk und Trump auf TechCrunch Disrupt',
            'datum_handlung': '2024-10-28',
            'betrag_usd': None,
            'quell_link': 'https://techcrunch.com/2024/10/28/vinod-khosla-calls-out-trumps-depraved-values-and-musks-role-in-spreading-misinformation/',
            'quell_titel': 'Vinod Khosla calls out Trump\'s \'depraved values\' and Musk\'s role in spreading misinformation',
            'kontext': 'Khosla kritisierte öffentlich Trump als "convicted felon, charged rapist" und beschuldigte Musk, Fehlinformationen auf X zu verbreiten.'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Teilnahme am $60 Milliarden VC-Koalition für Climate Tech',
            'datum_handlung': '2023-01-01',
            'betrag_usd': None,
            'quell_link': 'https://www.esgtoday.com/60-billion-venture-capital-coalition-launches-new-fund-to-scale-climate-tech-startups/',
            'quell_titel': '$60 Billion Venture Capital Coalition Launches New Fund to Scale Climate Tech Startups',
            'kontext': 'Khosla Ventures schloss sich einer Koalition von VCs an, um einen neuen Fonds zur Skalierung von Climate-Tech-Startups zu gründen.'
        },
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Vortrag bei Stanford über sino-amerikanischen Tech-Wettbewerb',
            'datum_handlung': '2023-05-15',
            'betrag_usd': None,
            'quell_link': 'https://aparc.fsi.stanford.edu/news/vinod-khosla-shares-insights-future-sino-american-tech-competition',
            'quell_titel': 'Vinod Khosla Shares Insights Into Future of Sino-American Tech Competition',
            'kontext': 'Vortrag an der Stanford University über den "20-Year Tech War" zwischen USA und China und die Rolle von KI.'
        }
    ]

    for handlung in handlungen:
        handlung['person_id'] = PERSON_ID
        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung, datum_handlung,
                betrag_usd, quell_link, quell_titel, kontext
            ) VALUES (
                :person_id, :handlung_typ, :beschreibung, :datum_handlung,
                :betrag_usd, :quell_link, :quell_titel, :kontext
            )
        """, handlung)

    print(f"[OK] {len(handlungen)} Handlungen eingefuegt")


def main():
    """Hauptfunktion: Verbindung zur DB und Einfügen der Daten."""

    print(f"\n{'='*60}")
    print(f"Datensammlung: Vinod Khosla (person_id={PERSON_ID})")
    print(f"{'='*60}\n")

    try:
        # Verbindung zur Datenbank
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Prüfe ob Person existiert
        cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
        result = cursor.fetchone()
        if not result:
            print(f"[FEHLER] Person mit ID {PERSON_ID} existiert nicht in der Datenbank!")
            return

        print(f"Person gefunden: {result[0]}\n")

        # Daten einfügen
        insert_aussagen(cursor)
        insert_handlungen(cursor)

        # Änderungen speichern
        conn.commit()

        # Statistik
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
        aussagen_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
        handlungen_count = cursor.fetchone()[0]

        print(f"\n{'='*60}")
        print(f"ERFOLG!")
        print(f"{'='*60}")
        print(f"Aussagen gesamt:    {aussagen_count}")
        print(f"Handlungen gesamt:  {handlungen_count}")

        # Tier-Prüfung
        if aussagen_count >= 10 and handlungen_count >= 8:
            print(f"\n[OK] Tier 2 erreicht! (>=10 Aussagen + >=8 Handlungen)")
        else:
            print(f"\n[WARNUNG] Tier 2 noch nicht erreicht!")
            print(f"  Benoetigt: >=10 Aussagen + >=8 Handlungen")
            print(f"  Aktuell:  {aussagen_count} Aussagen + {handlungen_count} Handlungen")

        print(f"{'='*60}\n")

    except sqlite3.Error as e:
        print(f"[FEHLER] Datenbankfehler: {e}")
        conn.rollback()

    finally:
        conn.close()


if __name__ == "__main__":
    main()
