#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_cook.py
===============
Sammelt verifizierbare Aussagen und Handlungen von Tim Cook (person_id=15)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Keynotes, Congressional Testimony, Shareholder Meetings und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-12
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 15  # Tim Cook

# ============================================================================
# AUSSAGEN (Statements)
# ============================================================================

AUSSAGEN = [
    # ---- 1. AI as profound technology (2025) ----
    {
        "aussage_text": "We see AI as one of the most profound technologies of our lifetime. We are embedding it across our devices and platforms and across the company. We are also significantly growing our investments.",
        "aussage_kurz": "Cook bezeichnet KI als eine der bedeutendsten Technologien unserer Zeit.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Interview
        "plattform_id": 1,    # Mainstream-Medien
        "quell_link": "https://www.barchart.com/story/news/34183355/apple-ceo-tim-cook-says-the-technology-theyre-developing-will-be-one-of-the-most-profound-technologies-of-our-lifetime",
        "quell_titel": "Apple fiscal Q3 2025 earnings call",
        "datum_aussage": "2025-08-01",
        "sprache": "en",
        "kontext": "Tim Cook in Apple's fiscal Q3 2025 earnings call ueber die Bedeutung von KI fuer Apple.",
        "aussage_uebersetzung_de": "Wir sehen KI als eine der bedeutendsten Technologien unserer Zeit. Wir integrieren sie in unsere Geraete und Plattformen und im gesamten Unternehmen. Wir erhoehen auch unsere Investitionen erheblich.",
    },
    # ---- 2. Not first, but best (2024) ----
    {
        "aussage_text": "We weren't the first to do intelligence. But we've done it in a way that we think is the best for the customer.",
        "aussage_kurz": "Cook betont, dass Apple nicht als Erstes, aber am besten KI umsetze.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://gizmodo.com/tim-cook-knows-apple-isnt-first-in-ai-but-says-its-about-being-the-best-2000514347",
        "quell_titel": "Tim Cook Interview with The Wall Street Journal",
        "datum_aussage": "2024-10-21",
        "sprache": "en",
        "kontext": "Tim Cook im Wall Street Journal-Interview ueber Apples KI-Strategie und den spaeteren Einstieg in KI.",
        "aussage_uebersetzung_de": "Wir waren nicht die Ersten, die Intelligenz entwickelt haben. Aber wir haben es auf eine Weise gemacht, die unserer Meinung nach die beste fuer den Kunden ist.",
    },
    # ---- 3. Break new ground in AI (2024) ----
    {
        "aussage_text": "We believe it will unlock transformative opportunities for our users. We will break new ground in generative AI in 2024.",
        "aussage_kurz": "Cook kuendigt bahnbrechende Fortschritte in generativer KI fuer 2024 an.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Shareholder Meeting
        "plattform_id": 1,
        "quell_link": "https://www.macrumors.com/2024/02/28/tim-cook-apple-generative-ai-break-new-ground/",
        "quell_titel": "Apple Annual Shareholders Meeting February 2024",
        "datum_aussage": "2024-02-28",
        "sprache": "en",
        "kontext": "Tim Cook bei der jaehrlichen Hauptversammlung von Apple im Februar 2024 ueber KI-Plaene.",
        "aussage_uebersetzung_de": "Wir glauben, dass es transformative Moeglichkeiten fuer unsere Nutzer erschliessen wird. Wir werden 2024 neue Wege in generativer KI beschreiten.",
    },
    # ---- 4. Apple Intelligence announcement (2024) ----
    {
        "aussage_text": "It's personal, powerful, and private—and it's integrated into the apps you rely on every day. Introducing Apple Intelligence—our next chapter in AI.",
        "aussage_kurz": "Cook stellt Apple Intelligence als persoenliches, maechtig und privates KI-System vor.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,  # Social Media
        "plattform_id": 5,    # Twitter/X
        "quell_link": "https://x.com/tim_cook/status/1800251049472839872",
        "quell_titel": "Tim Cook Twitter/X announcement of Apple Intelligence",
        "datum_aussage": "2024-06-10",
        "sprache": "en",
        "kontext": "Tim Cook kuendigt Apple Intelligence bei der WWDC 2024 an, betont Privacy-First-Ansatz.",
        "aussage_uebersetzung_de": "Es ist persoenlich, maechtig und privat – und es ist in die Apps integriert, auf die Sie jeden Tag angewiesen sind. Wir praesentieren Apple Intelligence – unser naechstes Kapitel in KI.",
    },
    # ---- 5. Privacy as fundamental human right (2015) ----
    {
        "aussage_text": "Privacy is a fundamental human right. At Apple, respect for privacy — and a healthy suspicion of authority — have always been in our bloodstream.",
        "aussage_kurz": "Cook bezeichnet Datenschutz als fundamentales Menschenrecht.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://www.npr.org/sections/alltechconsidered/2015/10/01/445026470/apple-ceo-tim-cook-privacy-is-a-fundamental-human-right",
        "quell_titel": "NPR Interview with Tim Cook",
        "datum_aussage": "2015-10-01",
        "sprache": "en",
        "kontext": "Tim Cook im NPR-Interview ueber Apples Datenschutz-Philosophie.",
        "aussage_uebersetzung_de": "Datenschutz ist ein fundamentales Menschenrecht. Bei Apple waren Respekt fuer Datenschutz – und ein gesundes Misstrauen gegenueber Autoritaeten – schon immer in unserer DNA.",
    },
    # ---- 6. Data collection weaponized (2018) ----
    {
        "aussage_text": "Personal data collection is being weaponized against us with military efficiency. We shouldn't sugarcoat the consequences. This is surveillance.",
        "aussage_kurz": "Cook warnt, dass persoenliche Datensammlung als Waffe gegen uns eingesetzt wird.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://www.cnbc.com/2018/10/24/apples-tim-cook-warns-silicon-valley-it-would-be-destructive-to-block-strong-privacy-laws.html",
        "quell_titel": "Tim Cook speech at Brussels privacy conference",
        "datum_aussage": "2018-10-24",
        "sprache": "en",
        "kontext": "Tim Cook bei einer Datenschutz-Konferenz in Bruessel, kritisiert Datensammlung der Tech-Industrie.",
        "aussage_uebersetzung_de": "Die Sammlung persoenlicher Daten wird mit militaerischer Effizienz gegen uns bewaffnet. Wir sollten die Konsequenzen nicht beschoenigen. Das ist Ueberwachung.",
    },
    # ---- 7. Privacy is top issue of the century (2021) ----
    {
        "aussage_text": "Privacy is one of the top issues of the century.",
        "aussage_kurz": "Cook bezeichnet Datenschutz als eines der wichtigsten Themen des Jahrhunderts.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://www.macrumors.com/2021/01/28/tim-cook-privacy-interview/",
        "quell_titel": "Tim Cook Interview on Privacy",
        "datum_aussage": "2021-01-28",
        "sprache": "en",
        "kontext": "Tim Cook betont in einem Interview die zentrale Bedeutung von Datenschutz im 21. Jahrhundert.",
        "aussage_uebersetzung_de": "Datenschutz ist eines der wichtigsten Themen des Jahrhunderts.",
    },
    # ---- 8. Technology serve humanity (2017) ----
    {
        "aussage_text": "Technology should serve humanity, not the other way around. Whatever we do at Apple, we must infuse it with the humanity that each of us is born with.",
        "aussage_kurz": "Cook betont, dass Technologie der Menschheit dienen soll, nicht umgekehrt.",
        "modus": "muendlich",
        "quellen_typ_id": 3,  # Keynote/Konferenz
        "plattform_id": 1,
        "quell_link": "https://www.technologyreview.com/2017/06/09/151322/tim-cook-technology-should-serve-humanity-not-the-other-way-around/",
        "quell_titel": "MIT Commencement Address 2017",
        "datum_aussage": "2017-06-09",
        "sprache": "en",
        "kontext": "Tim Cook in seiner Grundsatzrede an der MIT-Abschlussfeier 2017 ueber Technologie und Menschlichkeit.",
        "aussage_uebersetzung_de": "Technologie sollte der Menschheit dienen, nicht umgekehrt. Was auch immer wir bei Apple tun, muessen wir es mit der Menschlichkeit durchdringen, mit der jeder von uns geboren wurde.",
    },
    # ---- 9. AI concerns: people thinking like computers (2017) ----
    {
        "aussage_text": "I'm not worried about artificial intelligence giving computers the ability to think like humans. I'm more concerned about people thinking like computers without values or compassion, without concern for consequences.",
        "aussage_kurz": "Cook sorgt sich mehr um Menschen, die wie Computer denken, als um KI.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 1,
        "quell_link": "https://www.technologyreview.com/2017/06/09/151322/tim-cook-technology-should-serve-humanity-not-the-other-way-around/",
        "quell_titel": "MIT Commencement Address 2017",
        "datum_aussage": "2017-06-09",
        "sprache": "en",
        "kontext": "Tim Cook bei der MIT-Abschlussrede ueber seine Sorgen bezueglich KI und menschlicher Werte.",
        "aussage_uebersetzung_de": "Ich mache mir keine Sorgen, dass kuenstliche Intelligenz Computern die Faehigkeit gibt, wie Menschen zu denken. Ich bin mehr besorgt darueber, dass Menschen wie Computer denken, ohne Werte oder Mitgefuehl, ohne Ruecksicht auf Konsequenzen.",
    },
    # ---- 10. Moral responsibility (2017) ----
    {
        "aussage_text": "We have a moral responsibility to help grow the economy, to help grow jobs, to contribute to this country and to contribute to the other countries that we do business in.",
        "aussage_kurz": "Cook betont moralische Verantwortung von Unternehmen fuer Wirtschaft und Gesellschaft.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://fortune.com/2017/08/29/apple-tim-cook-moral-responsibility/",
        "quell_titel": "Tim Cook Fortune Interview on Corporate Responsibility",
        "datum_aussage": "2017-08-29",
        "sprache": "en",
        "kontext": "Tim Cook im Fortune-Interview ueber die gesellschaftliche Verantwortung von Apple.",
        "aussage_uebersetzung_de": "Wir haben eine moralische Verantwortung, die Wirtschaft zu foerdern, Arbeitsplaetze zu schaffen, zu diesem Land beizutragen und zu den anderen Laendern, in denen wir Geschaefte machen.",
    },
    # ---- 11. Technology needs regulation (2019) ----
    {
        "aussage_text": "We all have to be intellectually honest, and we have to admit that what we're doing isn't working. Technology needs to be regulated.",
        "aussage_kurz": "Cook fordert Regulierung von Technologie und gesteht ein, dass der Status Quo nicht funktioniert.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://time.com/5574143/technology-regulated-apple-tim-cook/",
        "quell_titel": "Tim Cook at TIME 100 Summit 2019",
        "datum_aussage": "2019-04-23",
        "sprache": "en",
        "kontext": "Tim Cook beim TIME 100 Summit, fordert Regulierung der Technologieindustrie.",
        "aussage_uebersetzung_de": "Wir alle muessen intellektuell ehrlich sein und zugeben, dass das, was wir tun, nicht funktioniert. Technologie muss reguliert werden.",
    },
    # ---- 12. FBI encryption case (2016) ----
    {
        "aussage_text": "We need to decide as a nation how much power the government should have over our data and over our privacy. We have a responsibility to protect your data and your privacy. We will not shrink from this responsibility.",
        "aussage_kurz": "Cook lehnt FBI-Forderung zur Entschluesselung ab, verteidigt Datenschutz.",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 1,
        "quell_link": "https://www.cnbc.com/2016/02/17/apple-order-to-hack-iphone-for-fbi-in-san-bernardino-case-chilling-tim-cook.html",
        "quell_titel": "Tim Cook Press Conference on FBI Case",
        "datum_aussage": "2016-03-21",
        "sprache": "en",
        "kontext": "Tim Cook zur FBI-Aufforderung, das iPhone des San Bernardino-Attentaeters zu entschluesseln.",
        "aussage_uebersetzung_de": "Wir muessen als Nation entscheiden, wie viel Macht die Regierung ueber unsere Daten und unsere Privatsphaere haben soll. Wir haben die Verantwortung, Ihre Daten und Ihre Privatsphaere zu schuetzen. Wir werden uns dieser Verantwortung nicht entziehen.",
    },
    # ---- 13. Climate action opportunity (2020) ----
    {
        "aussage_text": "Businesses have a profound opportunity to help build a more sustainable future, one born of our common concern for the planet we share. With our commitment to carbon neutrality, we hope to be a ripple in the pond that creates a much larger change.",
        "aussage_kurz": "Cook sieht Unternehmen in der Pflicht, zur Nachhaltigkeit beizutragen.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,  # Pressemitteilung
        "plattform_id": 1,
        "quell_link": "https://www.apple.com/newsroom/2020/07/apple-commits-to-be-100-percent-carbon-neutral-for-its-supply-chain-and-products-by-2030/",
        "quell_titel": "Apple Commits to Be 100 Percent Carbon Neutral by 2030",
        "datum_aussage": "2020-07-21",
        "sprache": "en",
        "kontext": "Apple kuendigt an, bis 2030 vollstaendig klimaneutral zu werden.",
        "aussage_uebersetzung_de": "Unternehmen haben eine grosse Chance, eine nachhaltigere Zukunft aufzubauen, eine, die aus unserer gemeinsamen Sorge um den Planeten entsteht. Mit unserem Bekenntnis zur Klimaneutralitaet hoffen wir, eine Welle zu sein, die eine viel groessere Veraenderung schafft.",
    },
    # ---- 14. China supply chain critical (2024) ----
    {
        "aussage_text": "There's no supply chain in the world that's more critical to us than China.",
        "aussage_kurz": "Cook betont die kritische Bedeutung Chinas fuer Apples Lieferkette.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://www.chinadaily.com.cn/a/202403/20/WS65fa936fa31082fc043bdbf3.html",
        "quell_titel": "Tim Cook China Visit Interview",
        "datum_aussage": "2024-03-20",
        "sprache": "en",
        "kontext": "Tim Cook bei einem Besuch in China, betont die Bedeutung der chinesischen Lieferkette fuer Apple.",
        "aussage_uebersetzung_de": "Es gibt keine Lieferkette auf der Welt, die fuer uns wichtiger ist als China.",
    },
    # ---- 15. Immigration advocacy (2026) ----
    {
        "aussage_text": "I'm deeply distraught with U.S. immigration policy. We have team members across the US on some form of Visa. I will personally advocate for you and will continue to lobby lawmakers on this issue.",
        "aussage_kurz": "Cook verspricht persoenlichen Einsatz fuer Einwanderungspolitik und DACA.",
        "modus": "schriftlich",
        "quellen_typ_id": 11,  # Internes Memo
        "plattform_id": 1,
        "quell_link": "https://www.tuaw.com/2026/02/07/tim-cook-pledges-immigration-advocacy-after-staff-concerns",
        "quell_titel": "Tim Cook Internal Memo to Apple Staff on Immigration",
        "datum_aussage": "2026-02-07",
        "sprache": "en",
        "kontext": "Tim Cook in einem internen Memo an Apple-Mitarbeiter bezueglich US-Einwanderungspolitik.",
        "aussage_uebersetzung_de": "Ich bin zutiefst beunruhigt ueber die US-Einwanderungspolitik. Wir haben Teammitglieder in den USA mit verschiedenen Visa-Status. Ich werde mich persoenlich fuer Sie einsetzen und weiterhin bei Gesetzgebern Lobbyarbeit zu diesem Thema leisten.",
    },
    # ---- 16. LGBTQ rights (2019) ----
    {
        "aussage_text": "Gay is not a limitation. Being gay has given me a deeper understanding of what it means to be in the minority and provided a window into the challenges that people in other minority groups deal with every day.",
        "aussage_kurz": "Cook betont, dass Homosexualitaet keine Einschraenkung ist und ihm Perspektive gibt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 1,
        "quell_link": "https://www.advocate.com/business/2019/10/25/tim-cook-people-en-espanol-gay-not-limitation",
        "quell_titel": "Tim Cook People en Español Interview",
        "datum_aussage": "2019-10-25",
        "sprache": "en",
        "kontext": "Tim Cook im Interview ueber seine Erfahrungen als schwuler CEO und LGBTQ-Rechte.",
        "aussage_uebersetzung_de": "Schwul zu sein ist keine Einschraenkung. Schwul zu sein hat mir ein tieferes Verstaendnis dafuer gegeben, was es bedeutet, in der Minderheit zu sein, und mir einen Einblick in die Herausforderungen gegeben, mit denen Menschen in anderen Minderheitengruppen jeden Tag zu tun haben.",
    },
]

# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================

HANDLUNGEN = [
    # ---- 1. Appointed CEO (2011) ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Tim Cook wird zum CEO von Apple ernannt, Nachfolger von Steve Jobs",
        "datum_handlung": "2011-08-24",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Tim_Cook",
        "kontext": "Tim Cook wird offiziell zum CEO von Apple ernannt, sechs Wochen vor Steve Jobs' Tod.",
    },
    # ---- 2. Stock buyback and dividend restart (2012) ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Apple kuendigt erste Dividende seit 1995 und 10-Mrd.-Dollar-Aktienrueckkauf an",
        "datum_handlung": "2012-03-19",
        "betrag_usd": 10000000000,
        "quell_link": "https://www.cnbc.com/2022/01/03/apples-3-trillion-market-cap-shows-value-of-share-buybacks-dividend.html",
        "kontext": "Cook leitet ein historisches Aktienrueckkaufprogramm ein, das bis 2024 ueber 750 Mrd. Dollar an Aktionaere zurueckgeben wird.",
    },
    # ---- 3. Apple Watch launch (2015) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launch der Apple Watch, erste neue Produktkategorie unter Cook",
        "datum_handlung": "2015-04-24",
        "betrag_usd": None,
        "quell_link": "https://www.cnn.com/2021/08/24/tech/tim-cook-apple-ceo-ten-years",
        "kontext": "Apple Watch wird lanciert, erste komplett neue Produktkategorie unter Tim Cooks Fuehrung.",
    },
    # ---- 4. Beats acquisition (2014) ----
    {
        "handlung_typ": "kauf",
        "beschreibung": "Apple kauft Beats Electronics und Beats Music fuer 3 Milliarden Dollar",
        "datum_handlung": "2014-05-28",
        "betrag_usd": 3000000000,
        "quell_link": "https://en.wikipedia.org/wiki/List_of_mergers_and_acquisitions_by_Apple",
        "kontext": "Groesste Uebernahme in Apples Geschichte, Grundlage fuer Apple Music.",
    },
    # ---- 5. FBI encryption lawsuit (2016) ----
    {
        "handlung_typ": "klage",
        "beschreibung": "Apple widersetzt sich FBI-Anordnung zur Entschluesselung von iPhone im San Bernardino-Fall",
        "datum_handlung": "2016-02-17",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Apple%E2%80%93FBI_encryption_dispute",
        "kontext": "Apple lehnt FBI-Forderung ab, Backdoor in iOS zu erstellen, verteidigt Verschluesselung.",
    },
    # ---- 6. Charitable donation (2019) ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Tim Cook spendet Apple-Aktien im Wert von 4,87 Millionen Dollar an wohltatige Organisationen",
        "datum_handlung": "2019-08-26",
        "betrag_usd": 4870000,
        "quell_link": "https://www.cnbc.com/2019/08/26/tim-cook-donates-nearly-5-million-of-apple-shares-to-charity.html",
        "kontext": "Cook spendet regelmaessig an wohltatige Zwecke, plant gesamtes Vermoegen zu spenden.",
    },
    # ---- 7. Carbon neutrality commitment (2020) ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Apple verpflichtet sich, bis 2030 vollstaendig klimaneutral zu werden",
        "datum_handlung": "2020-07-21",
        "betrag_usd": None,
        "quell_link": "https://www.apple.com/newsroom/2020/07/apple-commits-to-be-100-percent-carbon-neutral-for-its-supply-chain-and-products-by-2030/",
        "kontext": "Apple kuendigt an, alle Produkte und Lieferketten bis 2030 klimaneutral zu machen.",
    },
    # ---- 8. Vision Pro launch (2024) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Launch des Apple Vision Pro Mixed-Reality-Headsets",
        "datum_handlung": "2024-02-02",
        "betrag_usd": None,
        "quell_link": "https://www.macrumors.com/2024/02/02/tim-cook-on-vision-pro-moment/",
        "kontext": "Apple Vision Pro wird eingefuehrt, neue Produktkategorie fuer Mixed Reality.",
    },
    # ---- 9. Apple Intelligence launch (2024) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Ankuendigung von Apple Intelligence, Apples KI-System bei WWDC 2024",
        "datum_handlung": "2024-06-10",
        "betrag_usd": None,
        "quell_link": "https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/",
        "kontext": "Apple kuendigt Apple Intelligence an, Integration von KI in iOS 18, iPadOS 18 und macOS Sequoia.",
    },
    # ---- 10. OpenAI partnership (2024) ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Apple kuendigt Partnerschaft mit OpenAI fuer ChatGPT-Integration in Apple Intelligence an",
        "datum_handlung": "2024-06-10",
        "betrag_usd": None,
        "quell_link": "https://www.cbsnews.com/news/apple-wwdc-2024-ios-18-tim-cook-keynote/",
        "kontext": "Apple geht Partnerschaft mit OpenAI ein, um ChatGPT in Siri und Apple Intelligence zu integrieren.",
    },
    # ---- 11. Record stock buyback (2024) ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Apple kuendigt groessten Aktienrueckkauf der Geschichte an: 110 Milliarden Dollar",
        "datum_handlung": "2024-05-02",
        "betrag_usd": 110000000000,
        "quell_link": "https://www.cnbc.com/amp/2024/05/02/apple-aapl-earnings-report-q2-2024.html",
        "kontext": "Apple kuendigt den groessten Aktienrueckkauf in der Unternehmensgeschichte an.",
    },
    # ---- 12. Trump inauguration donation (2025) ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Tim Cook spendet persoenlich 1 Million Dollar an Donald Trumps Amtseinfuehrungs-Komitee",
        "datum_handlung": "2025-01-03",
        "betrag_usd": 1000000,
        "quell_link": "https://www.axios.com/2025/01/03/tim-cook-apple-donate-1-million-trump-inauguration",
        "kontext": "Cook spendet persoenlich 1 Million Dollar an Trumps Amtseinfuehrung 2025.",
    },
    # ---- 13. Apple lobbying spending (2017) ----
    {
        "handlung_typ": "lobbying",
        "beschreibung": "Apple gibt Rekordbetrag von 7,15 Millionen Dollar fuer Lobbying aus",
        "datum_handlung": "2017-12-31",
        "betrag_usd": 7150000,
        "quell_link": "https://press.farm/tim-cooks-political-views-and-public-advocacy/",
        "kontext": "Apple gibt 2017 mehr fuer Lobbying aus als je zuvor, fokussiert auf Immigration, Privacy und Steuerpolitik.",
    },
]

# ============================================================================
# Datenbankfunktionen
# ============================================================================

def connect_db():
    """Verbindet zur SQLite-Datenbank."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Datenbank nicht gefunden: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

def insert_aussagen(conn, aussagen, person_id):
    """Fuegt Aussagen in die Datenbank ein."""
    cursor = conn.cursor()
    inserted = 0

    for aussage in aussagen:
        try:
            cursor.execute("""
                INSERT INTO aussagen (
                    person_id, aussage_text, aussage_kurz, modus,
                    quellen_typ_id, plattform_id, quell_link, quell_titel,
                    datum_aussage, sprache, kontext, aussage_uebersetzung_de,
                    einschluss
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                person_id,
                aussage.get("aussage_text"),
                aussage.get("aussage_kurz"),
                aussage.get("modus"),
                aussage.get("quellen_typ_id"),
                aussage.get("plattform_id"),
                aussage.get("quell_link"),
                aussage.get("quell_titel"),
                aussage.get("datum_aussage"),
                aussage.get("sprache"),
                aussage.get("kontext"),
                aussage.get("aussage_uebersetzung_de")
            ))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"[WARNUNG] Aussage bereits vorhanden oder Fehler: {e}")
            print(f"  Text: {aussage.get('aussage_text')[:60]}...")

    conn.commit()
    return inserted

def insert_handlungen(conn, handlungen, person_id):
    """Fuegt Handlungen in die Datenbank ein."""
    cursor = conn.cursor()
    inserted = 0

    for handlung in handlungen:
        try:
            cursor.execute("""
                INSERT INTO handlungen (
                    person_id, handlung_typ, beschreibung,
                    datum_handlung, betrag_usd, quell_link, kontext
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                person_id,
                handlung.get("handlung_typ"),
                handlung.get("beschreibung"),
                handlung.get("datum_handlung"),
                handlung.get("betrag_usd"),
                handlung.get("quell_link"),
                handlung.get("kontext")
            ))
            inserted += 1
        except sqlite3.IntegrityError as e:
            print(f"[WARNUNG] Handlung bereits vorhanden oder Fehler: {e}")
            print(f"  Beschreibung: {handlung.get('beschreibung')[:60]}...")

    conn.commit()
    return inserted

def main():
    """Hauptfunktion: Verbindet zur DB und fuegt Daten ein."""
    print("=" * 70)
    print("DATENSAMMLUNG: Tim Cook (person_id=15)")
    print("=" * 70)

    try:
        conn = connect_db()
        print(f"[OK] Verbunden mit Datenbank: {DB_PATH}\n")

        # Aussagen einfuegen
        print(f"Fuege {len(AUSSAGEN)} Aussagen ein...")
        inserted_aussagen = insert_aussagen(conn, AUSSAGEN, PERSON_ID)
        print(f"[OK] {inserted_aussagen} Aussagen erfolgreich eingefuegt.\n")

        # Handlungen einfuegen
        print(f"Fuege {len(HANDLUNGEN)} Handlungen ein...")
        inserted_handlungen = insert_handlungen(conn, HANDLUNGEN, PERSON_ID)
        print(f"[OK] {inserted_handlungen} Handlungen erfolgreich eingefuegt.\n")

        conn.close()

        print("=" * 70)
        print("ZUSAMMENFASSUNG")
        print("=" * 70)
        print(f"Aussagen eingefuegt:   {inserted_aussagen}/{len(AUSSAGEN)}")
        print(f"Handlungen eingefuegt: {inserted_handlungen}/{len(HANDLUNGEN)}")
        print("=" * 70)
        print("[OK] Datensammlung abgeschlossen!")

    except Exception as e:
        print(f"[FEHLER] {e}")
        raise

if __name__ == "__main__":
    main()
