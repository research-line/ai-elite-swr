# -*- coding: utf-8 -*-
"""
collect_intrator.py
Sammelt Aussagen und Handlungen von Michael Intrator (person_id=41)
Tier 2: mindestens 10 Aussagen + mindestens 8 Handlungen
"""

import sqlite3

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 41  # Michael Intrator

def insert_aussagen(conn):
    """Fuegt mindestens 10 verifizierte Aussagen von Michael Intrator ein"""

    aussagen = [
        # Aussage 1: Relentless Demand
        {
            'aussage_text': 'The demand from the most knowledgeable, most sophisticated, largest tech companies in the world is relentless.',
            'aussage_kurz': 'Unerbittliche Nachfrage von fuehrenden Tech-Unternehmen nach GPU-Kapazitaeten',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://fortune.com/2025/12/26/coreweave-ceo-michael-intrator-circular-economy-ai-bubble-violent-change-supply/',
            'quell_titel': 'CoreWeave\'s CEO sees a \'violent change\' rattling the supply chain',
            'datum_aussage': '2025-12-26',
            'sprache': 'en',
            'kontext': 'Fortune Brainstorm AI Konferenz in San Francisco, Diskussion ueber AI-Nachfrage trotz Marktskepsis',
            'aussage_uebersetzung_de': 'Die Nachfrage von den sachkundigsten, fortschrittlichsten, groessten Technologieunternehmen der Welt ist unerbittlich.'
        },

        # Aussage 2: Capital Markets vs Reality
        {
            'aussage_text': 'There\'s a divergence between what the capital markets and what the media is thinking, and what I am feeling down in the trenches. What I am feeling is relentless demand.',
            'aussage_kurz': 'Divergenz zwischen Kapitalmaerkten/Medien und realer AI-Nachfrage in der Praxis',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://fortune.com/2025/03/31/coreweave-ceo-michael-intrator-on-capital-markets-vs-the-media/',
            'quell_titel': 'CoreWeave CEO Michael Intrator on capital markets vs the media',
            'datum_aussage': '2025-03-31',
            'sprache': 'en',
            'kontext': 'Interview kurz nach CoreWeave IPO ueber Diskrepanz zwischen Marktsentiment und Geschaeftsrealitaet',
            'aussage_uebersetzung_de': 'Es gibt eine Divergenz zwischen dem, was die Kapitalmaerkte und die Medien denken, und dem, was ich in den Schutzengraeben fuehle. Was ich fuehle, ist unerbittliche Nachfrage.'
        },

        # Aussage 3: IPO as Means to End
        {
            'aussage_text': 'Going public is really a means to an end. It puts us on the path towards what we need to accomplish as a business.',
            'aussage_kurz': 'Boersengang als Mittel zum Zweck fuer weiteres Geschaeftswachstum',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://www.cnbc.com/video/2025/03/28/coreweave-ceo-mike-intrator-going-public-positions-us-for-the-next-stage-of-growth.html',
            'quell_titel': 'CoreWeave CEO: Going public \'positions us for the next stage of growth\'',
            'datum_aussage': '2025-03-28',
            'sprache': 'en',
            'kontext': 'CNBC Interview am Tag des CoreWeave IPO, Erklaerung der strategischen Bedeutung',
            'aussage_uebersetzung_de': 'An die Boerse zu gehen ist wirklich ein Mittel zum Zweck. Es bringt uns auf den Weg zu dem, was wir als Unternehmen erreichen muessen.'
        },

        # Aussage 4: AI Native Cloud
        {
            'aussage_text': 'CoreWeave is the first AI-native cloud, designed from the ground up for AI workloads rather than retrofitted from CPU-based systems.',
            'aussage_kurz': 'CoreWeave als erste von Grund auf fuer AI konzipierte Cloud-Infrastruktur',
            'modus': 'muendlich',
            'quellen_typ_id': 3,
            'plattform_id': 4,
            'quell_link': 'https://business.columbia.edu/insights/digital-future/ai-coreweave-cloud-sustainability',
            'quell_titel': 'Powering AI: CoreWeave CEO Michael Intrator on the Future of Cloud and Sustainability',
            'datum_aussage': '2025-11-15',
            'sprache': 'en',
            'kontext': 'Columbia Business School Diskussion ueber CoreWeave\'s einzigartige Architektur',
            'aussage_uebersetzung_de': 'CoreWeave ist die erste AI-native Cloud, von Grund auf fuer AI-Workloads konzipiert und nicht von CPU-basierten Systemen umgeruested.'
        },

        # Aussage 5: Violent Supply Chain Change
        {
            'aussage_text': 'The primary constraint facing the AI sector is a physical bottleneck associated with getting the most performant compute into the hands of the most cutting-edge players. The reasons that you have challenges in delivering that compute is because of policy, because of physical infrastructure, because of energy.',
            'aussage_kurz': 'Physische Engpaesse bei Compute-Delivery durch Politik, Infrastruktur und Energie',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://fortune.com/2025/12/26/coreweave-ceo-michael-intrator-circular-economy-ai-bubble-violent-change-supply/',
            'quell_titel': 'CoreWeave\'s CEO sees a \'violent change\' rattling the supply chain',
            'datum_aussage': '2025-12-26',
            'sprache': 'en',
            'kontext': 'Erklaerung der systemischen Herausforderungen in der AI-Infrastruktur Lieferkette',
            'aussage_uebersetzung_de': 'Die primaere Beschraenkung fuer den AI-Sektor ist ein physischer Engpass beim Zugang zu leistungsstaerkster Rechenleistung fuer fuehrende Unternehmen. Die Gruende fuer diese Herausforderungen liegen in Politik, physischer Infrastruktur und Energie.'
        },

        # Aussage 6: Circular Economy Rejection
        {
            'aussage_text': 'Circular is the incorrect way of looking at it. This is not financial engineering, but logistical necessity.',
            'aussage_kurz': 'Ablehnung der Circular Economy Narrative als falsche Perspektive',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://fortune.com/2025/12/26/coreweave-ceo-michael-intrator-circular-economy-ai-bubble-violent-change-supply/',
            'quell_titel': 'CoreWeave\'s CEO sees a \'violent change\' rattling the supply chain',
            'datum_aussage': '2025-12-26',
            'sprache': 'en',
            'kontext': 'Verteidigung gegen Kritik an NVIDIA-CoreWeave Partnerschaftsmodell',
            'aussage_uebersetzung_de': 'Zirkular ist die falsche Betrachtungsweise. Das ist keine Finanzmanipulation, sondern logistische Notwendigkeit.'
        },

        # Aussage 7: Customer Diversification
        {
            'aussage_text': 'While we were previously reliant on Microsoft for 85% of our revenue, aggressive diversification efforts mean that no single customer now represents more than 30% of the company\'s backlog.',
            'aussage_kurz': 'Erfolgreiche Diversifizierung von 85% Microsoft-Abhaengigkeit auf max. 30% pro Kunde',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://fortune.com/2025/03/31/coreweave-ceo-michael-intrator-on-capital-markets-vs-the-media/',
            'quell_titel': 'CoreWeave CEO Michael Intrator on capital markets vs the media',
            'datum_aussage': '2025-03-31',
            'sprache': 'en',
            'kontext': 'Diskussion ueber Risikominderung und Kundenportfolio-Strategie',
            'aussage_uebersetzung_de': 'Waehrend wir zuvor zu 85% von Microsoft abhaengig waren, bedeuten aggressive Diversifizierungsbemuehungen, dass nun kein einzelner Kunde mehr als 30% des Auftragsbestands ausmacht.'
        },

        # Aussage 8: AI Embedded Everywhere
        {
            'aussage_text': 'AI will be embedded into everything we do within the next decade.',
            'aussage_kurz': 'AI wird innerhalb eines Jahrzehnts in alle Lebensbereiche eingebettet sein',
            'modus': 'muendlich',
            'quellen_typ_id': 1,
            'plattform_id': 5,
            'quell_link': 'https://www.cnbc.com/video/2025/09/22/watch-cnbcs-full-interview-with-coreweave-ceo-michael-intrator.html',
            'quell_titel': 'Watch CNBC\'s full interview with CoreWeave CEO Michael Intrator',
            'datum_aussage': '2025-09-22',
            'sprache': 'en',
            'kontext': 'CNBC Interview ueber die Zukunft der AI-Integration in Gesellschaft und Wirtschaft',
            'aussage_uebersetzung_de': 'KI wird innerhalb des naechsten Jahrzehnts in alles eingebettet sein, was wir tun.'
        },

        # Aussage 9: Productivity Growth Potential
        {
            'aussage_text': 'AI has the potential to accelerate the economy by 15 percent through sustained productivity growth, which could expand employment and raise standards of living, even if the short-term adjustment is difficult.',
            'aussage_kurz': 'AI koennte Wirtschaft um 15% beschleunigen durch Produktivitaetswachstum trotz kurzfristiger Anpassungen',
            'modus': 'muendlich',
            'quellen_typ_id': 3,
            'plattform_id': 4,
            'quell_link': 'https://business.columbia.edu/insights/digital-future/ai-coreweave-cloud-sustainability',
            'quell_titel': 'Powering AI: CoreWeave CEO Michael Intrator on the Future of Cloud and Sustainability',
            'datum_aussage': '2025-11-15',
            'sprache': 'en',
            'kontext': 'Columbia Business School Diskussion ueber makrooekonomische AI-Auswirkungen',
            'aussage_uebersetzung_de': 'KI hat das Potenzial, die Wirtschaft durch anhaltendes Produktivitaetswachstum um 15 Prozent zu beschleunigen, was Beschaeftigung ausweiten und Lebensstandards erhoehen koennte, auch wenn die kurzfristige Anpassung schwierig ist.'
        },

        # Aussage 10: OpenAI Expansion
        {
            'aussage_text': 'We are proud to expand our relationship with OpenAI, a company consistently at the forefront of advancing artificial intelligence. This expansion affirms the trust that world-leading innovators have in CoreWeave\'s ability to power the most demanding inference and training workloads at an unmatched pace.',
            'aussage_kurz': 'Stolz auf erweiterte OpenAI-Partnerschaft als Bestaetigung der Fuehrungsrolle',
            'modus': 'schriftlich',
            'quellen_typ_id': 10,
            'plattform_id': 17,
            'quell_link': 'https://www.coreweave.com/news/coreweave-expands-agreement-with-openai-by-up-to-6-5b',
            'quell_titel': 'CoreWeave Expands Agreement with OpenAI by up to $6.5B',
            'datum_aussage': '2025-09-25',
            'sprache': 'en',
            'kontext': 'Offizielle Stellungnahme zur 6,5 Milliarden Dollar OpenAI-Vertragserweiterung',
            'aussage_uebersetzung_de': 'Wir sind stolz darauf, unsere Beziehung zu OpenAI auszuweiten, einem Unternehmen, das konsequent an der Spitze der KI-Entwicklung steht. Diese Erweiterung bestaetigt das Vertrauen, das weltweit fuehrende Innovatoren in CoreWeaves Faehigkeit haben, die anspruchsvollsten Inferenz- und Trainings-Workloads in unuebertroffenem Tempo zu betreiben.'
        },

        # Aussage 11: Energy and Sustainability Challenge
        {
            'aussage_text': 'AI\'s appetite for energy is immense. While advances like liquid cooling have reduced data center energy consumption by as much as 60 percent, overall demand continues to rise faster than efficiency gains can offset.',
            'aussage_kurz': 'AI-Energiebedarf waechst schneller als Effizienzgewinne durch Kuehltechnologie',
            'modus': 'muendlich',
            'quellen_typ_id': 3,
            'plattform_id': 4,
            'quell_link': 'https://business.columbia.edu/insights/digital-future/ai-coreweave-cloud-sustainability',
            'quell_titel': 'Powering AI: CoreWeave CEO Michael Intrator on the Future of Cloud and Sustainability',
            'datum_aussage': '2025-11-15',
            'sprache': 'en',
            'kontext': 'Diskussion ueber Nachhaltigkeit und Energie-Herausforderungen der AI-Infrastruktur',
            'aussage_uebersetzung_de': 'Der Energiebedarf von KI ist immens. Waehrend Fortschritte wie Fluessigkuehlung den Energieverbrauch von Rechenzentren um bis zu 60 Prozent gesenkt haben, steigt die Gesamtnachfrage weiterhin schneller als Effizienzgewinne ausgleichen koennen.'
        },

        # Aussage 12: Technology Shift Phase
        {
            'aussage_text': 'Every major technology shift eventually stops being about the technology and starts being about the systems around it. AI has begun to cross that threshold, with foundational capabilities firmly in place. This next phase is about making AI usable and productive across entire industries.',
            'aussage_kurz': 'AI bewegt sich von Technologie-Phase zu System-Integration ueber ganze Industrien',
            'modus': 'schriftlich',
            'quellen_typ_id': 6,
            'plattform_id': 9,
            'quell_link': 'https://www.coreweave.com/blog/mike-intrator-ceo-blog-the-year-ai-gets-to-work',
            'quell_titel': 'The Year AI Gets to Work - CoreWeave CEO Blog',
            'datum_aussage': '2026-01-10',
            'sprache': 'en',
            'kontext': 'CEO Blog-Post ueber die naechste Phase der AI-Entwicklung und Industrialisierung',
            'aussage_uebersetzung_de': 'Jeder grosse Technologiewandel hoert irgendwann auf, sich um die Technologie zu drehen, und beginnt sich um die Systeme drum herum zu drehen. KI hat begonnen, diese Schwelle zu ueberschreiten, mit fest verankerten grundlegenden Faehigkeiten. Diese naechste Phase geht darum, KI ueber ganze Industrien hinweg nutzbar und produktiv zu machen.'
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
    """Fuegt mindestens 8 verifizierte Handlungen von Michael Intrator ein"""

    handlungen = [
        # Handlung 1: CoreWeave Gründung
        {
            'handlung_typ': 'gruendung',
            'beschreibung': 'Michael Intrator co-gruendete CoreWeave (urspruenglich Atlantic Crypto) zusammen mit Brian Venturo, Brannin McBee und Peter Salanki. Das Unternehmen startete als Ethereum-Mining-Operation in einer Garage in New Jersey. Intrator brachte seine Erfahrung aus dem Rohstoffhandel und Climate Finance mit.',
            'datum_handlung': '2017-09-01',
            'quell_link': 'https://en.wikipedia.org/wiki/CoreWeave',
            'quell_titel': 'CoreWeave - Wikipedia',
            'kontext': 'Pivot von Commodities Trading zu Krypto-Mining mit vier Gruendern'
        },

        # Handlung 2: Pivot zu GPU Cloud
        {
            'handlung_typ': 'umstrukturierung',
            'beschreibung': 'Nach dem Krypto-Crash 2018 leitete Intrator die strategische Neuausrichtung von CoreWeave vom Ethereum-Mining zur GPU-Cloud-Computing-Plattform. Diese visionaere Entscheidung verwandelte potenziell wertlose GPU-Bestaende in die Grundlage eines Milliarden-Dollar-Unternehmens, genau rechtzeitig fuer die AI-Revolution.',
            'datum_handlung': '2019-03-01',
            'quell_link': 'https://introl.com/blog/coreweave-gpu-cloud-ai-infrastructure-deep-dive-2025',
            'quell_titel': 'CoreWeave Deep Dive: How a Former Crypto Miner Became AI\'s Essential Cloud',
            'kontext': 'Ethereum-Crash machte Mining unprofitabel, rechtzeitiger Pivot vor ChatGPT-Launch'
        },

        # Handlung 3: Rebranding zu CoreWeave
        {
            'handlung_typ': 'umstrukturierung',
            'beschreibung': 'Intrator fuehrte das Rebranding von Atlantic Crypto zu CoreWeave durch, um die neue Mission als Anbieter von Kern-Rechenleistung und vernetzten Netzwerkressourcen fuer AI-Workloads zu reflektieren. Dies signalisierte den definitiven Bruch mit der Krypto-Mining-Vergangenheit.',
            'datum_handlung': '2021-10-01',
            'quell_link': 'https://pestel-analysis.com/blogs/brief-history/coreweave',
            'quell_titel': 'What is Brief History of CoreWeave Company?',
            'kontext': 'Strategische Neupositionierung als AI-Cloud-Anbieter vor Ethereum Proof-of-Stake Transition'
        },

        # Handlung 4: NVIDIA Partnerschaft und Investment
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Intrator sicherte eine strategische Partnerschaft mit NVIDIA, bei der NVIDIA 100 Millionen Dollar in CoreWeave investierte und sich verpflichtete, Milliarden Dollar an CoreWeave Cloud-Kapazitaet bis 2032 zu kaufen. Diese Partnerschaft etablierte CoreWeave als primaere GPU-Infrastruktur fuer NVIDIA.',
            'datum_handlung': '2023-04-01',
            'betrag_usd': 100000000.0,
            'quell_link': 'https://www.cnbc.com/2026/01/26/3coreweave-nvidia-stock-ai-data-centers.html',
            'quell_titel': 'Nvidia invests $2 billion in CoreWeave to boost data center build-out',
            'kontext': 'NVIDIA sicherte sich exklusive Kapazitaeten und wurde strategischer Partner'
        },

        # Handlung 5: Microsoft Deal
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Unter Intrators Fuehrung schloss CoreWeave einen massiven Deal mit Microsoft ab, der 2024 zu 62% bzw. 85% der Gesamteinnahmen fuehrte. Microsoft nutzte CoreWeave\'s GPU-Infrastruktur fuer Azure AI-Services und OpenAI-Support.',
            'datum_handlung': '2023-08-01',
            'quell_link': 'https://introl.com/blog/coreweave-gpu-cloud-ai-infrastructure-deep-dive-2025',
            'quell_titel': 'CoreWeave Deep Dive: How a Former Crypto Miner Became AI\'s Essential Cloud',
            'kontext': '77% der 2024 Einnahmen von Top-2-Kunden, Microsoft allein 62%'
        },

        # Handlung 6: Funding Round $1.1B
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Intrator fuehrte CoreWeave durch eine 1,1 Milliarden Dollar Finanzierungsrunde unter Fuehrung von Coatue Management, die das Unternehmen mit 19 Milliarden Dollar bewertete. Weitere Investoren umfassten Magnetar Capital, Fidelity, Jane Street und andere fuehrende Institutionen.',
            'datum_handlung': '2024-05-01',
            'betrag_usd': 1100000000.0,
            'quell_link': 'https://www.crunchbase.com/organization/coreweave',
            'quell_titel': 'CoreWeave - Crunchbase Company Profile & Funding',
            'kontext': 'Series C funding bei $19B Bewertung, Wachstum von Startup zu Unicorn'
        },

        # Handlung 7: OpenAI Partnership Expansion
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Intrator erweiterte die CoreWeave-OpenAI Partnerschaft massiv: Maerz 2025 initiale 11,9 Milliarden Dollar, Mai 2025 weitere 4 Milliarden, September 2025 zusaetzliche 6,5 Milliarden Dollar. Gesamtwert der OpenAI-Zusammenarbeit erreichte 22,4 Milliarden Dollar. OpenAI investierte zudem 350 Millionen in CoreWeave-Aktien.',
            'datum_handlung': '2025-09-25',
            'betrag_usd': 22400000000.0,
            'quell_link': 'https://www.coreweave.com/news/coreweave-expands-agreement-with-openai-by-up-to-6-5b',
            'quell_titel': 'CoreWeave Expands Agreement with OpenAI by up to $6.5B',
            'kontext': 'Groesste AI-Infrastruktur-Partnerschaft, OpenAI wurde auch Investor'
        },

        # Handlung 8: CoreWeave IPO
        {
            'handlung_typ': 'sonstiges',
            'beschreibung': 'Michael Intrator fuehrte CoreWeave am 28. Maerz 2025 an die Boerse (Nasdaq: CRWV). Der IPO brachte 1,5 Milliarden Dollar ein und war das groesste AI-bezogene Listing nach eingeworbener Summe. Intrator behielt 11% Eigentumsanteil, was seine persoenliche Ausrichtung mit dem langfristigen Erfolg signalisiert.',
            'datum_handlung': '2025-03-28',
            'betrag_usd': 1500000000.0,
            'quell_link': 'https://en.wikipedia.org/wiki/CoreWeave',
            'quell_titel': 'CoreWeave - Wikipedia',
            'kontext': 'Groesstes AI-IPO 2025, reduziert von $2.7B auf $1.5B wegen Marktbedingungen'
        },

        # Handlung 9: Meta Partnership
        {
            'handlung_typ': 'partnerschaft',
            'beschreibung': 'Intrator sicherte einen 14,2 Milliarden Dollar Deal mit Meta fuer AI-Infrastruktur. Dies war Teil der strategischen Diversifizierung weg von der Microsoft-Abhaengigkeit und positionierte CoreWeave als kritischer Infrastrukturanbieter fuer mehrere AI-Giganten.',
            'datum_handlung': '2025-06-15',
            'betrag_usd': 14200000000.0,
            'quell_link': 'https://www.pymnts.com/news/artificial-intelligence/2025/ai-hyperscaler-coreweave-signs-14-billion-dollar-deal-with-meta',
            'quell_titel': 'AI Hyperscaler CoreWeave Signs $14.2 Billion Deal With Meta',
            'kontext': 'Teil der Diversifizierungsstrategie, kein Kunde mehr als 30% des Backlogs'
        },

        # Handlung 10: NVIDIA $2B Investment Round 2
        {
            'handlung_typ': 'investition',
            'beschreibung': 'NVIDIA investierte weitere 2 Milliarden Dollar in CoreWeave im Januar 2026, verdoppelte seinen Anteil und wurde zweitgroesster Aktionaer. Die Aktien wurden mit 87,20 Dollar bewertet. Dies vertiefte die strategische Partnerschaft fuer 5 Gigawatt Rechenzentrumskapazitaet bis 2030.',
            'datum_handlung': '2026-01-26',
            'betrag_usd': 2000000000.0,
            'quell_link': 'https://www.cnbc.com/2026/01/26/3coreweave-nvidia-stock-ai-data-centers.html',
            'quell_titel': 'CoreWeave stock jumps 6% as Nvidia invests $2 billion to expand AI data center capacity',
            'kontext': 'NVIDIA verdoppelte Stake von 6.3% auf ~13%, commitment zu 5GW bis 2030'
        },

        # Handlung 11: Scotland Renewable Data Center
        {
            'handlung_typ': 'investition',
            'beschreibung': 'Intrator kuendigte eine 2 Milliarden Dollar Investition in schottische Rechenzentren an, die vollstaendig mit erneuerbarer Energie betrieben werden. Dies reflektiert seinen Hintergrund in Climate Finance und adressiert Nachhaltigkeitsbedenken bzgl. AI-Energieverbrauch.',
            'datum_handlung': '2025-05-10',
            'betrag_usd': 2000000000.0,
            'quell_link': 'https://business.columbia.edu/insights/digital-future/ai-coreweave-cloud-sustainability',
            'quell_titel': 'Powering AI: CoreWeave CEO Michael Intrator on the Future of Cloud and Sustainability',
            'kontext': 'Nachhaltigkeit-Initiative, Nutzung von Intrators Climate Finance Expertise'
        },

        # Handlung 12: Plano Texas Supercomputer
        {
            'handlung_typ': 'produktlaunch',
            'beschreibung': 'CoreWeave eroeffnete ein 1,6 Milliarden Dollar Supercomputer-Rechenzentrum in Plano, Texas, fuer NVIDIA. NVIDIA bezeichnete es als schnellsten AI-Supercomputer der Welt. Dies demonstrierte CoreWeave\'s Faehigkeit, cutting-edge Infrastruktur in Rekordzeit zu liefern.',
            'datum_handlung': '2025-08-20',
            'betrag_usd': 1600000000.0,
            'quell_link': 'https://www.datacenterknowledge.com/investing/nvidia-invests-2b-more-in-coreweave-for-5-gw-data-center-push',
            'quell_titel': 'Nvidia Commits $2B to CoreWeave for 5 GW Data Center Expansion',
            'kontext': 'Schnellster AI-Supercomputer weltweit laut NVIDIA, zeigt Ausfuehrungsgeschwindigkeit'
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
    print("DATENSAMMLUNG: MICHAEL INTRATOR (person_id=41)")
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
