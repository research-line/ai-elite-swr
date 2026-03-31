# -*- coding: utf-8 -*-
"""
collect_sacks.py
Sammelt Aussagen und Handlungen von David Sacks (person_id=36)
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 36  # David Sacks

def insert_aussagen(conn):
    """Fuegt mindestens 10 verifizierte Aussagen von David Sacks ein"""

    aussagen = [
        # Aussage 1: AI Regulation - One Rulebook
        {
            'aussage_text': 'There must be only One Rulebook if we are going to continue to lead in AI.',
            'aussage_kurz': 'Ein einheitliches Regelwerk fuer KI-Regulierung in den USA notwendig',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,
            'plattform_id': 2,
            'quell_link': 'https://x.com/DavidSacks/status/1998125180753944985',
            'quell_titel': 'David Sacks on X: ONE RULEBOOK FOR AI',
            'datum_aussage': '2025-06-03',
            'sprache': 'en',
            'kontext': 'Diskussion ueber fragmentierte KI-Regulierung in 50 US-Bundesstaaten mit ueber 1000 Gesetzesinitiativen',
            'aussage_uebersetzung_de': 'Es muss nur ein Regelwerk geben, wenn wir weiterhin fuehrend in der KI sein wollen.'
        },

        # Aussage 2: AI Race Warning
        {
            'aussage_text': 'If we have 1,200 different AI laws in the states, you know, clamping down on innovation, I worry that we could lose the AI race.',
            'aussage_kurz': 'Warnung vor Verlust des KI-Wettlaufs durch uebermaessige staatliche Regulierung',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://www.cnbc.com/video/2025/12/15/white-house-ai-czar-david-sacks-talk-pres-trumps-order-limiting-state-regulation-on-ai.html',
            'quell_titel': 'White House AI Czar David Sacks talk Pres. Trump\'s order limiting state regulation on AI',
            'datum_aussage': '2025-12-15',
            'sprache': 'en',
            'kontext': 'Interview zu Trumps Executive Order zur Begrenzung staatlicher KI-Regulierung',
            'aussage_uebersetzung_de': 'Wenn wir 1.200 verschiedene KI-Gesetze in den Bundesstaaten haben, die Innovation einschraenken, befuerchte ich, dass wir das KI-Rennen verlieren koennten.'
        },

        # Aussage 3: AI Progress Rate
        {
            'aussage_text': 'I would say the rate of progress is exponential right now on at least three key dimensions. The algorithms, the chips, and the datacenters are all improving or scaling at a rate of 3-4x a year. That\'s 10x every two years.',
            'aussage_kurz': 'KI-Fortschritt erfolgt exponentiell in drei Dimensionen mit 3-4x pro Jahr',
            'modus': 'muendlich',
            'quellen_typ_id': 2,
            'plattform_id': 3,
            'quell_link': 'https://x.com/theallinpod/status/1918715889530130838',
            'quell_titel': 'David Sacks Explains How AI Will Go 1,000,000x in Four Years - All-In Podcast',
            'datum_aussage': '2024-10-31',
            'sprache': 'en',
            'kontext': 'All-In Podcast Diskussion ueber exponentielles KI-Wachstum',
            'aussage_uebersetzung_de': 'Ich wuerde sagen, dass die Fortschrittsrate derzeit in mindestens drei Schluesseldimensionen exponentiell ist. Die Algorithmen, die Chips und die Rechenzentren verbessern oder skalieren sich alle mit einer Rate von 3-4x pro Jahr. Das sind 10x alle zwei Jahre.'
        },

        # Aussage 4: Open Source AI
        {
            'aussage_text': 'It\'s great to see more American open source AI models. A meaningful segment of the global market will prefer the cost, customizability, and control that open source offers. We want the U.S. to win this category too.',
            'aussage_kurz': 'USA muss auch bei Open-Source-KI fuehrend sein fuer globalen Wettbewerb',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,
            'plattform_id': 2,
            'quell_link': 'https://x.com/DavidSacks/status/1976311543026602424',
            'quell_titel': 'David Sacks on X: American open source AI models',
            'datum_aussage': '2025-04-06',
            'sprache': 'en',
            'kontext': 'Reaktion auf amerikanische Open-Source-KI-Modelle im Wettbewerb mit China',
            'aussage_uebersetzung_de': 'Es ist grossartig, mehr amerikanische Open-Source-KI-Modelle zu sehen. Ein bedeutender Teil des globalen Marktes wird die Kosten, Anpassbarkeit und Kontrolle bevorzugen, die Open Source bietet. Wir wollen, dass die USA auch in dieser Kategorie gewinnen.'
        },

        # Aussage 5: Free Speech Fight
        {
            'aussage_text': 'The fight of our times is over free speech. The bad guys are always the ones trying to restrict it.',
            'aussage_kurz': 'Meinungsfreiheit ist der zentrale Kampf unserer Zeit',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,
            'plattform_id': 2,
            'quell_link': 'https://www.newsbusters.org/blogs/free-speech/catherine-salgado/2024/12/10/trumps-ai-czar-pick-draws-praise-guess-his-blunt',
            'quell_titel': 'Trump\'s AI Czar Pick Draws Praise—Guess His Blunt Views on Censorship',
            'datum_aussage': '2024-09-01',
            'sprache': 'en',
            'kontext': 'Statement zur Bedeutung der Meinungsfreiheit im Tech-Kontext',
            'aussage_uebersetzung_de': 'Der Kampf unserer Zeit dreht sich um freie Meinungsaeusserung. Die Boesen sind immer diejenigen, die versuchen, sie einzuschraenken.'
        },

        # Aussage 6: AI Competition
        {
            'aussage_text': 'We have 5 major American companies vigorously competing on frontier models. This brings out the best in everyone and helps America win the AI race.',
            'aussage_kurz': 'Wettbewerb zwischen 5 US-Firmen bei KI-Modellen staerkt amerikanische Fuehrung',
            'modus': 'muendlich',
            'quellen_typ_id': 2,
            'plattform_id': 3,
            'quell_link': 'https://www.vktr.com/ai-news/trumps-ai-czar-david-sacks-is-reshaping-us-tech-for-better-or-worse/',
            'quell_titel': 'Trump\'s AI Czar David Sacks Is Reshaping US Tech',
            'datum_aussage': '2025-01-15',
            'sprache': 'en',
            'kontext': 'Diskussion ueber Wettbewerb zwischen OpenAI, Google, Meta, Anthropic und anderen',
            'aussage_uebersetzung_de': 'Wir haben 5 grosse amerikanische Unternehmen, die energisch bei Frontier-Modellen konkurrieren. Das bringt das Beste in jedem hervor und hilft Amerika, das KI-Rennen zu gewinnen.'
        },

        # Aussage 7: Stablecoin Priority
        {
            'aussage_text': 'Our first priority is stablecoin legislation. We can get this done in the next six months.',
            'aussage_kurz': 'Stablecoin-Gesetzgebung als oberste Prioritaet in den naechsten 6 Monaten',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://www.cnbc.com/2025/02/04/trump-crypto-czar-david-sacks-says-priority-is-stablecoin-legislation.html',
            'quell_titel': 'White House crypto czar David Sacks says first priority is stablecoin legislation',
            'datum_aussage': '2025-02-04',
            'sprache': 'en',
            'kontext': 'Erste Pressekonferenz als White House AI & Crypto Czar',
            'aussage_uebersetzung_de': 'Unsere erste Prioritaet ist die Stablecoin-Gesetzgebung. Wir koennen das in den naechsten sechs Monaten schaffen.'
        },

        # Aussage 8: Strategic Bitcoin Reserve
        {
            'aussage_text': 'Just a few minutes ago, President Trump signed an Executive Order to establish a Strategic Bitcoin Reserve. The Reserve will be capitalized with Bitcoin owned by the federal government that was forfeited as part of criminal or civil asset forfeiture proceedings. This means it will not cost taxpayers a dime.',
            'aussage_kurz': 'Strategische Bitcoin-Reserve aus beschlagnahmten Assets ohne Steuerkosten',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,
            'plattform_id': 2,
            'quell_link': 'https://x.com/davidsacks47/status/1897802280738734236',
            'quell_titel': 'David Sacks on X: Strategic Bitcoin Reserve Executive Order',
            'datum_aussage': '2025-03-06',
            'sprache': 'en',
            'kontext': 'Ankuendigung der strategischen Bitcoin-Reserve durch Trump Executive Order',
            'aussage_uebersetzung_de': 'Vor wenigen Minuten hat Praesident Trump eine Exekutivanordnung unterzeichnet, um eine strategische Bitcoin-Reserve zu schaffen. Die Reserve wird mit Bitcoin kapitalisiert, die der Bundesregierung gehoeren und als Teil von strafrechtlichen oder zivilrechtlichen Vermoegenseinziehungsverfahren eingezogen wurden. Das bedeutet, dass es die Steuerzahler keinen Cent kostet.'
        },

        # Aussage 9: Orwellian AI Warning
        {
            'aussage_text': 'Excessive regulation leads to Orwellian AI, a future where algorithms are imbued with ideological biases, capable of censoring information, distorting reality, and even rewriting history in real-time.',
            'aussage_kurz': 'Warnung vor uebermaessiger Regulierung die zu ideologisch verzerrter KI fuehrt',
            'modus': 'schriftlich',
            'quellen_typ_id': 7,
            'plattform_id': 5,
            'quell_link': 'https://www.startuphub.ai/ai-news/startup-news/2025/white-house-ai-czar-david-sacks-on-navigating-the-ai-frontier-regulation-race-and-jobs/',
            'quell_titel': 'White House AI Czar David Sacks on Navigating the AI Frontier',
            'datum_aussage': '2025-01-25',
            'sprache': 'en',
            'kontext': 'Warnung vor den Gefahren uebermaessiger KI-Regulierung',
            'aussage_uebersetzung_de': 'Uebermaessige Regulierung fuehrt zu orwellscher KI, einer Zukunft, in der Algorithmen mit ideologischen Vorurteilen durchdrungen sind, Informationen zensieren, die Realitaet verzerren und sogar die Geschichte in Echtzeit umschreiben koennen.'
        },

        # Aussage 10: Crypto War Over
        {
            'aussage_text': 'The war on crypto is over.',
            'aussage_kurz': 'Erklaerung dass der Krieg gegen Kryptowaehrungen beendet ist',
            'modus': 'muendlich',
            'quellen_typ_id': 10,
            'plattform_id': 17,
            'quell_link': 'https://www.coindesk.com/policy/2025/02/04/trump-s-crypto-czar-sacks-says',
            'quell_titel': 'Trump\'s Crypto Czar Sacks Says \'Golden Age\' Coming',
            'datum_aussage': '2025-01-20',
            'sprache': 'en',
            'kontext': 'Crypto Ball nach Trumps Amtseinfuehrung',
            'aussage_uebersetzung_de': 'Der Krieg gegen Krypto ist vorbei.'
        },

        # Aussage 11: Open Source AI Models Cost-Benefit
        {
            'aussage_text': 'There is likely to be a major role for open source. These models excel at providing 80-90% of the capability at 10-20% of the cost.',
            'aussage_kurz': 'Open-Source-KI bietet 80-90% Leistung bei 10-20% der Kosten',
            'modus': 'muendlich',
            'quellen_typ_id': 2,
            'plattform_id': 3,
            'quell_link': 'https://www.axios.com/2025/08/10/david-sacks-ai-goldilocks-scenario',
            'quell_titel': 'David Sacks\' "Goldilocks" scenario',
            'datum_aussage': '2025-08-10',
            'sprache': 'en',
            'kontext': 'Diskussion ueber das Goldilocks-Szenario fuer KI-Wettbewerb',
            'aussage_uebersetzung_de': 'Open Source wird wahrscheinlich eine wichtige Rolle spielen. Diese Modelle zeichnen sich dadurch aus, dass sie 80-90% der Leistung zu 10-20% der Kosten bieten.'
        },

        # Aussage 12: State AI Regulation Statistics
        {
            'aussage_text': 'All 50 states have introduced AI bills in 2025. There\'s been over 1,000 bills in state legislatures. 118 AI laws have already been passed across the 50 states.',
            'aussage_kurz': 'Ueber 1000 KI-Gesetzentwuerfe in US-Bundesstaaten als regulatorische Herausforderung',
            'modus': 'muendlich',
            'quellen_typ_id': 2,
            'plattform_id': 3,
            'quell_link': 'https://x.com/theallinpod/status/1975957261009711613',
            'quell_titel': 'David Sacks: The AI Regulatory Frenzy at the State Level is "Very Concerning"',
            'datum_aussage': '2025-04-10',
            'sprache': 'en',
            'kontext': 'All-In Podcast ueber die regulatorische Fragmentierung auf Bundesstaatsebene',
            'aussage_uebersetzung_de': 'Alle 50 Bundesstaaten haben 2025 KI-Gesetze eingebracht. Es gab ueber 1.000 Gesetzentwuerfe in den Parlamenten der Bundesstaaten. 118 KI-Gesetze wurden bereits in den 50 Bundesstaaten verabschiedet.'
        },

        # Aussage 13: Llama 4 Open Source Leadership
        {
            'aussage_text': 'For the U.S. to win the AI race, we have to win in open source too and Llama 4 puts us back in the lead.',
            'aussage_kurz': 'USA muss bei Open-Source-KI gewinnen, Llama 4 bringt Fuehrung zurueck',
            'modus': 'schriftlich',
            'quellen_typ_id': 5,
            'plattform_id': 2,
            'quell_link': 'https://www.tronweekly.com/meta-releases-llama-4-models-as-us-doubles/',
            'quell_titel': 'Meta Releases Llama 4 Models as US Doubles Down on Open Source Strategy',
            'datum_aussage': '2025-07-23',
            'sprache': 'en',
            'kontext': 'Reaktion auf Meta\'s Llama 4 Veroeffentlichung im Kontext US-China KI-Wettbewerb',
            'aussage_uebersetzung_de': 'Damit die USA das KI-Rennen gewinnen, muessen wir auch bei Open Source gewinnen, und Llama 4 bringt uns wieder in Fuehrung.'
        }
    ]

    cursor = conn.cursor()
    inserted_count = 0

    for aussage in aussagen:
        try:
            cursor.execute('''
                INSERT INTO aussagen (
                    person_id, aussage_text, aussage_kurz, modus,
                    quellen_typ_id, plattform_id, quell_link, quell_titel,
                    datum_aussage, sprache, kontext, aussage_uebersetzung_de
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                PERSON_ID,
                aussage['aussage_text'],
                aussage['aussage_kurz'],
                aussage['modus'],
                aussage['quellen_typ_id'],
                aussage['plattform_id'],
                aussage['quell_link'],
                aussage['quell_titel'],
                aussage['datum_aussage'],
                aussage['sprache'],
                aussage['kontext'],
                aussage['aussage_uebersetzung_de']
            ))
            inserted_count += 1
            print(f"OK Aussage eingefuegt: {aussage['aussage_kurz'][:60]}...")
        except sqlite3.Error as e:
            print(f"XX Fehler bei Aussage: {aussage['aussage_kurz'][:60]}... - {e}")

    conn.commit()
    print(f"\n{inserted_count} Aussagen erfolgreich eingefuegt.")
    return inserted_count


def insert_handlungen(conn):
    """Fuegt mindestens 8 verifizierte Handlungen von David Sacks ein"""

    handlungen = [
        # Handlung 1: PayPal COO
        {
            'handlung_typ': 'einstellung',
            'beschreibung': 'David Sacks wurde Chief Operating Officer bei PayPal und baute viele der Schluesselteams des Unternehmens auf. Er war verantwortlich fuer Produktmanagement und Design, Vertrieb und Marketing, Geschaeftsentwicklung, International, Kundenservice, Betrugsbekaempfung und Personalwesen. Er war Teil der "PayPal Mafia" - der Gruppe von Gruendern und fruehen Mitarbeitern, die spaeter weitere erfolgreiche Tech-Unternehmen gruendeten.',
            'datum_handlung': '1999-06-01',
            'quell_link': 'https://en.wikipedia.org/wiki/David_Sacks',
            'quell_titel': 'David Sacks - Wikipedia',
            'kontext': 'Verliess McKinsey & Company um zu Confinity (spaeter PayPal) zu wechseln'
        },

        # Handlung 2: Yammer Gründung
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'David Sacks gruendete Yammer, ein Enterprise-Social-Network-Tool fuer Unternehmenskommunikation. Als Founder und CEO wuchs er das Unternehmen auf etwa 60 Millionen Dollar Umsatz und 500 Mitarbeiter an, bevor es 2012 an Microsoft verkauft wurde.',
            'datum_handlung': '2008-09-01',
            'quell_link': 'https://techcrunch.com/2012/09/12/david-sacks-on-selling-yammer-we-never-really-shopped-the-company/',
            'quell_titel': 'David Sacks On Selling Yammer: We Never Really Shopped The Company',
            'kontext': 'Nach dem PayPal Exit gruendete Sacks sein eigenes SaaS-Unternehmen'
        },

        # Handlung 3: Yammer Verkauf an Microsoft
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'Microsoft akquirierte Yammer fuer 1,2 Milliarden Dollar in bar. Dies war einer der schnellsten Unicorn-Exits im SaaS-Bereich und etablierte Sacks als erfolgreichen Serial Entrepreneur.',
            'datum_handlung': '2012-06-25',
            'betrag_usd': 1200000000.0,
            'quell_link': 'https://techcrunch.com/2012/06/25/its-official-microsoft-confirms-it-has-acquired-yammer-for-1-2-billion-in-cash/',
            'quell_titel': 'Microsoft Confirms It Has Acquired Yammer For $1.2 Billion In Cash',
            'kontext': 'Exit nach nur 4 Jahren, Microsoft integrierte Yammer in Office 365'
        },

        # Handlung 4: Craft Ventures Gründung
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'David Sacks gruendete Ende 2017 Craft Ventures als Co-Founder und General Partner. Der Early-Stage-Venture-Capital-Fonds konzentriert sich auf B2B-Software-Startups. Der erste Fonds hatte ein Volumen von 350 Millionen Dollar.',
            'datum_handlung': '2017-11-01',
            'betrag_usd': 350000000.0,
            'quell_link': 'https://www.craftventures.com/team/david-sacks',
            'quell_titel': 'David Sacks - Craft Ventures',
            'kontext': 'Nach erfolgreichen Angel-Investments in Uber, SpaceX, Facebook, etc.'
        },

        # Handlung 5: Trump Fundraiser
        {
            'handlung_typ': 'spende',
            'beschreibung': 'David Sacks co-hostete einen Fundraiser fuer Donald Trump in seinem San Francisco Anwesen. Tickets kosteten 50.000 Dollar pro Person, mit einem 300.000 Dollar Tier das Foto-Moeglichkeiten mit Trump beinhaltete. Das Event brachte erwartete 12 Millionen Dollar ein.',
            'datum_handlung': '2024-06-06',
            'betrag_usd': 12000000.0,
            'quell_link': 'https://www.cnbc.com/2024/06/06/trump-hits-tech-fundraiser-in-san-francisco-some-guests-pay-300000.html',
            'quell_titel': 'Trump heads to tech fundraiser in San Francisco, with some guests paying $300,000',
            'kontext': 'Nach offizieller Unterstuetzung von Trump als Praesidentschaftskandidat'
        },

        # Handlung 6: Appointment als AI & Crypto Czar
        {
            'handlung_typ': 'politisch',
            'beschreibung': 'Praesident-elect Donald Trump ernannte David O. Sacks zum "White House A.I. & Crypto Czar". In dieser Rolle wird Sacks die Politik fuer KI und Kryptowaehrungen leiten, zwei fuer die amerikanische Wettbewerbsfaehigkeit kritische Bereiche. Er leitet auch den Presidential Council of Advisors for Science and Technology.',
            'datum_handlung': '2024-12-05',
            'quell_link': 'https://www.presidency.ucsb.edu/documents/statement-president-elect-donald-j-trump-announcing-the-appointment-david-o-sacks-white',
            'quell_titel': 'Statement by President-elect Donald J. Trump Announcing the Appointment of David O. Sacks',
            'kontext': 'Teilzeit-Rolle, Sacks behaelt Position bei Craft Ventures'
        },

        # Handlung 7: Verkauf aller Krypto-Holdings
        {
            'handlung_typ': 'verkauf',
            'beschreibung': 'David Sacks und Craft Ventures verkauften ueber 200 Millionen Dollar an Krypto-bezogenen Holdings, davon mindestens 85 Millionen direkt Sacks zurechenbar. Dies umfasste alle liquiden Kryptowaehrungen (Bitcoin, Ethereum, Solana) sowie Anteile an Krypto-Fonds wie Multicoin Capital und Blockchain Capital, um Interessenskonflikte in seiner White House Rolle zu vermeiden.',
            'datum_handlung': '2025-01-15',
            'betrag_usd': 200000000.0,
            'quell_link': 'https://www.cnbc.com/2025/03/14/david-sacks-sold-200-million-in-crypto-holdings-before-taking-wh-job.html',
            'quell_titel': 'David Sacks sold $200 million in crypto-related holdings before taking White House job',
            'kontext': 'Ethik-Memo vor Amtsantritt, Reaktion auf Kritik von Senator Warren'
        },

        # Handlung 8: Strategic Bitcoin Reserve Executive Order
        {
            'handlung_typ': 'politisch',
            'beschreibung': 'Als White House AI & Crypto Czar leitete Sacks die Arbeitsgruppe zur Einrichtung der Strategic Bitcoin Reserve durch Executive Order von Praesident Trump. Die Reserve wird mit beschlagnahmten Bitcoin aus Strafverfahren kapitalisiert (ca. 200.000 BTC), ohne Kosten fuer Steuerzahler.',
            'datum_handlung': '2025-03-06',
            'quell_link': 'https://www.cnbc.com/2025/03/06/trump-signs-executive-order-for-us-strategic-bitcoin-reserve.html',
            'quell_titel': 'Trump signs executive order establishing U.S. strategic bitcoin reserve',
            'kontext': 'Teil der Trump-Administration Strategie, USA als "Crypto Capital of the World" zu etablieren'
        },

        # Handlung 9: Stablecoin Legislation Push
        {
            'handlung_typ': 'lobbying',
            'beschreibung': 'Sacks arbeitete mit dem Kongress zusammen um Stablecoin-Gesetzgebung als oberste Prioritaet voranzutreiben. Er koordinierte mit dem bicameral crypto committee (Senate Banking, Senate Agriculture, House Agriculture, House Financial Services) um innerhalb von 6 Monaten einen regulatorischen Rahmen zu schaffen.',
            'datum_handlung': '2025-02-04',
            'quell_link': 'https://www.cnbc.com/2025/02/04/trump-crypto-czar-david-sacks-says-priority-is-stablecoin-legislation.html',
            'quell_titel': 'White House crypto czar David Sacks says first priority is stablecoin legislation',
            'kontext': 'Erste Pressekonferenz als Crypto Czar, Ziel: Dollar-Dominanz durch digitale Finanzen staerken'
        },

        # Handlung 10: AI Preemption Executive Order
        {
            'handlung_typ': 'lobbying',
            'beschreibung': 'Sacks entwickelte und verteidigte Trumps Executive Order zur Preemption staatlicher KI-Gesetze. Die Order zielt darauf ab, ein einheitliches bundesweites Regelwerk zu schaffen statt fragmentierter Regulierung durch 50 Bundesstaaten mit ueber 1000 verschiedenen Gesetzentwuerfen.',
            'datum_handlung': '2025-12-11',
            'quell_link': 'https://www.npr.org/2025/12/11/nx-s1-5638562/trump-ai-david-sacks-executive-order',
            'quell_titel': 'Trump is trying to preempt state AI laws via an executive order',
            'kontext': 'Kontroverse um Legalitaet und Interessenskonflikte bei Sacks\' 449 AI-Investments'
        },

        # Handlung 11: Craft Ventures Fund Raises
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Unter Sacks\' Fuehrung wuchs Craft Ventures von 350 Millionen Dollar (2017) auf 3,3 Milliarden Dollar AUM durch mehrere Fondsrunden: 500 Millionen (2019), 1,3 Milliarden in zwei Fonds (2021), und 1,3 Milliarden in Ventures IV und Growth II (2023). Der Fokus liegt auf B2B-Software im Zeitalter generativer KI.',
            'datum_handlung': '2023-06-01',
            'betrag_usd': 3300000000.0,
            'quell_link': 'https://en.wikipedia.org/wiki/David_Sacks',
            'quell_titel': 'David Sacks - Wikipedia',
            'kontext': 'Erfolgreiche Investments in ueber 20 Unicorns inkl. Affirm, SpaceX, Uber'
        },

        # Handlung 12: All-In Podcast Co-Host
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'David Sacks ist Co-Host des All-In Podcasts zusammen mit Chamath Palihapitiya, Jason Calacanis und David Friedberg. Der Podcast wurde zu einer der einflussreichsten Tech-Stimmen mit Millionen Hoerern und regelmaessigen Diskussionen ueber KI, Krypto, Politik und Wirtschaft.',
            'datum_handlung': '2020-03-16',
            'quell_link': 'https://podcasts.apple.com/us/podcast/all-in-with-chamath-jason-sacks-friedberg/id1502871393',
            'quell_titel': 'All-In with Chamath, Jason, Sacks & Friedberg - Podcast',
            'kontext': 'Gestartet waehrend COVID-19 Pandemie, wurde zu bedeutender Plattform fuer Tech-Elite'
        }
    ]

    cursor = conn.cursor()
    inserted_count = 0

    for handlung in handlungen:
        try:
            cursor.execute('''
                INSERT INTO handlungen (
                    person_id, handlung_typ, beschreibung,
                    datum_handlung, betrag_usd, quell_link, quell_titel, kontext
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                PERSON_ID,
                handlung['handlung_typ'],
                handlung['beschreibung'],
                handlung['datum_handlung'],
                handlung.get('betrag_usd'),
                handlung['quell_link'],
                handlung['quell_titel'],
                handlung['kontext']
            ))
            inserted_count += 1
            print(f"OK Handlung eingefuegt: {handlung['beschreibung'][:60]}...")
        except sqlite3.Error as e:
            print(f"XX Fehler bei Handlung: {handlung['beschreibung'][:60]}... - {e}")

    conn.commit()
    print(f"\n{inserted_count} Handlungen erfolgreich eingefuegt.")
    return inserted_count


def main():
    """Hauptfunktion"""
    print("=" * 80)
    print("DATENSAMMLUNG: DAVID SACKS (person_id=36)")
    print("=" * 80)
    print(f"Datenbank: {DB_PATH}")
    print(f"Ziel: Tier 2 (>=10 Aussagen + >=8 Handlungen)\n")

    try:
        # Verbindung zur Datenbank
        conn = sqlite3.connect(DB_PATH)
        print("OK Datenbankverbindung hergestellt\n")

        # Aussagen einfügen
        print("-" * 80)
        print("AUSSAGEN EINFUEGEN")
        print("-" * 80)
        aussagen_count = insert_aussagen(conn)

        # Handlungen einfügen
        print("\n" + "-" * 80)
        print("HANDLUNGEN EINFUEGEN")
        print("-" * 80)
        handlungen_count = insert_handlungen(conn)

        # Zusammenfassung
        print("\n" + "=" * 80)
        print("ZUSAMMENFASSUNG")
        print("=" * 80)
        print(f"Aussagen eingefuegt:    {aussagen_count}")
        print(f"Handlungen eingefuegt:  {handlungen_count}")
        print(f"\nTier 2 Status:")
        print(f"  OK Aussagen:   {aussagen_count} >= 10 -> {'ERFUELLT' if aussagen_count >= 10 else 'NICHT ERFUELLT'}")
        print(f"  OK Handlungen: {handlungen_count} >= 8 -> {'ERFUELLT' if handlungen_count >= 8 else 'NICHT ERFUELLT'}")

        if aussagen_count >= 10 and handlungen_count >= 8:
            print("\n*** TIER 2 ERFOLGREICH ERREICHT ***")

        conn.close()
        print("\nOK Datenbankverbindung geschlossen")

    except sqlite3.Error as e:
        print(f"\nXX DATENBANKFEHLER: {e}")
        return 1
    except Exception as e:
        print(f"\nXX FEHLER: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
