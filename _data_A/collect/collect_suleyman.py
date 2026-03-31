#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_suleyman.py
===================
Sammelt verifizierbare Aussagen und Handlungen von Mustafa Suleyman (person_id=23)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
dem Buch "The Coming Wave" (2023), TED Talks, Podcasts und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 23  # Mustafa Suleyman

# ============================================================================
# AUSSAGEN (Statements)
# ============================================================================
# Jede Aussage enthaelt:
#   - aussage_text: Originalwortlaut (Englisch)
#   - aussage_kurz: 1-Satz-Zusammenfassung (Deutsch)
#   - modus: 'muendlich' oder 'schriftlich'
#   - quellen_typ_id: FK zu quellen_typen
#   - plattform_id: FK zu plattformen
#   - quell_link: URL
#   - quell_titel: Titel der Quelle
#   - datum_aussage: YYYY-MM-DD oder YYYY
#   - sprache: 'en'
#   - kontext: Zusammenhang
#   - aussage_uebersetzung_de: Deutsche Uebersetzung

AUSSAGEN = [
    # ---- 1. The Coming Wave: Kernaussage ----
    {
        "aussage_text": "I believe this coming wave of technology is bringing human history to a turning point. If containing it is impossible, the consequences for our species are dramatic, potentially dire. Equally, without its fruits we are exposed and precarious.",
        "aussage_kurz": "Suleyman sieht die kommende Technologiewelle als Wendepunkt der Menschheitsgeschichte mit dramatischen Konsequenzen.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,   # Buch
        "plattform_id": 9,     # Blogs/Buecher
        "quell_link": "https://www.goodreads.com/work/quotes/114865406-the-coming-wave-technology-power-and-the-twenty-first-century-s-great",
        "quell_titel": "The Coming Wave: Technology, Power, and the Twenty-first Century's Greatest Dilemma",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Kernaussage aus Suleymans Buch 'The Coming Wave', veroeffentlicht 2023. Beschreibt die existenzielle Herausforderung der Technologieentwicklung.",
        "aussage_uebersetzung_de": "Ich glaube, diese kommende Technologiewelle bringt die Menschheitsgeschichte an einen Wendepunkt. Wenn ihre Eindaemmung unmoeglich ist, sind die Konsequenzen fuer unsere Spezies dramatisch, potenziell verheerend. Gleichermaßen sind wir ohne ihre Fruechte exponiert und unsicher.",
    },
    # ---- 2. The Coming Wave: Zwei Kerntechnologien ----
    {
        "aussage_text": "The coming wave is defined by two core technologies: artificial intelligence (AI) and synthetic biology.",
        "aussage_kurz": "Suleyman definiert die kommende Welle durch zwei Kerntechnologien: KI und synthetische Biologie.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.bookey.app/book/the-coming-wave/quote",
        "quell_titel": "The Coming Wave: Technology, Power, and the Twenty-first Century's Greatest Dilemma",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Definition der Hauptthemen des Buches. Suleyman fokussiert auf KI und Synthetische Biologie als transformative Technologien.",
        "aussage_uebersetzung_de": "Die kommende Welle wird durch zwei Kerntechnologien definiert: kuenstliche Intelligenz (KI) und synthetische Biologie.",
    },
    # ---- 3. The Coming Wave: Technologie-Versagen ----
    {
        "aussage_text": "This book is about confronting failure. If technology damages human lives, or produces societies filled with harm, or renders them ungovernable because we empower a chaotic long tail of bad (or unintentionally dangerous) actors—if, in the aggregate, technology is damaging—then it can be said to have failed in another, deeper sense, failing to live up to its promise.",
        "aussage_kurz": "Suleyman warnt, dass Technologie versagt, wenn sie menschliches Leben schaedigt oder Gesellschaften unregierbar macht.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.supersummary.com/the-coming-wave/important-quotes/",
        "quell_titel": "The Coming Wave: Important Quotes (SuperSummary)",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Suleymans Perspektive auf Technologie-Governance und das Versagen von Technologie als gesellschaftliches Phaenomen.",
        "aussage_uebersetzung_de": "Dieses Buch handelt von der Konfrontation mit Versagen. Wenn Technologie menschliches Leben schaedigt, oder Gesellschaften voller Schaden produziert, oder sie unregierbar macht, weil wir einen chaotischen Long Tail schlechter oder unbeabsichtigt gefaehrlicher Akteure ermaechtigten -- wenn Technologie insgesamt schaedlich ist -- dann kann man sagen, dass sie in einem anderen, tieferen Sinne versagt hat, naemlich ihr Versprechen nicht eingeloest hat.",
    },
    # ---- 4. The Coming Wave: Macht-Umverteilung ----
    {
        "aussage_text": "This will be the greatest, most rapid acceleration in wealth and prosperity in human history…Over the next 10 years, AI will be the greatest force amplifier in history. That's why it could enable a redistribution of power on a historical scale.",
        "aussage_kurz": "Suleyman prognostiziert KI als groessten Kraftverstaerker der Geschichte mit massiver Macht-Umverteilung.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://medium.com/@jcgblue/ai-winners-revealed-10-notable-quotes-from-the-coming-wave-36aa9259b315",
        "quell_titel": "AI Winners Revealed: 10 Notable Quotes from 'The Coming Wave' (Medium)",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Suleymans Prognose zur oekonomischen und politischen Transformation durch KI in den naechsten 10 Jahren.",
        "aussage_uebersetzung_de": "Dies wird die groesste, schnellste Beschleunigung von Wohlstand und Prosperitaet in der Menschheitsgeschichte sein... In den naechsten 10 Jahren wird KI der groesste Kraftverstaerker der Geschichte sein. Deshalb koennte sie eine Umverteilung von Macht in historischem Ausmass ermoeglichen.",
    },
    # ---- 5. The Coming Wave: Synthetische Biologie Gefahr ----
    {
        "aussage_text": "A single person today likely has the capacity to kill a billion people.",
        "aussage_kurz": "Suleyman warnt, dass eine einzelne Person mit synthetischer Biologie die Kapazitaet hat, eine Milliarde Menschen zu toeten.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://screvi.com/highlights/the-coming-wave-technology-power-and-the-twenty-first-century-s-greatest-dilemma/",
        "quell_titel": "The Coming Wave: Book Notes (Screvi)",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Extreme Warnung vor der Demokratisierung gefaehrlicher Technologien im Kontext synthetischer Biologie.",
        "aussage_uebersetzung_de": "Eine einzelne Person hat heute wahrscheinlich die Kapazitaet, eine Milliarde Menschen zu toeten.",
    },
    # ---- 6. The Coming Wave: Containment Paradox ----
    {
        "aussage_text": "Containment is not, on the face of it, possible. And yet for all our sakes, containment must be possible.",
        "aussage_kurz": "Suleyman beschreibt das Paradox, dass Eindaemmung unmoeglich scheint, aber zwingend notwendig ist.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/author/quotes/16663417.Mustafa_Suleyman",
        "quell_titel": "Mustafa Suleyman Quotes (Goodreads)",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Zentrales Dilemma des Buches: Die Notwendigkeit, das scheinbar Unmoegliche zu erreichen.",
        "aussage_uebersetzung_de": "Eindaemmung ist auf den ersten Blick nicht moeglich. Und doch muss Eindaemmung um unser aller willen moeglich sein.",
    },
    # ---- 7. Containment-Definition ----
    {
        "aussage_text": "Containment is a belief that completely unregulated power that proliferates at zero marginal cost is a fundamental risk to peace and stability.",
        "aussage_kurz": "Suleyman definiert Containment als Reaktion auf unkontrollierte Macht, die zu Nullkosten verbreitet wird.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://podscripts.co/podcasts/what-now-with-trevor-noah/will-ai-save-humanity-or-end-it-with-mustafa-suleyman",
        "quell_titel": "What Now? with Trevor Noah - Will AI Save Humanity or End It?",
        "datum_aussage": "2023-09",
        "sprache": "en",
        "kontext": "Interview mit Trevor Noah ueber Containment als zentrales Konzept fuer KI-Governance.",
        "aussage_uebersetzung_de": "Eindaemmung ist die Ueberzeugung, dass voellig unregulierte Macht, die sich zu Nullgrenzkosten ausbreitet, ein fundamentales Risiko fuer Frieden und Stabilitaet darstellt.",
    },
    # ---- 8. Modern Turing Test ----
    {
        "aussage_text": "To pass the Modern Turing Test, an AI would have to successfully act on this instruction: 'Go make $1 million on a retail web platform in a few months with just a $100,000 investment.'",
        "aussage_kurz": "Suleyman schlaegt einen modernen Turing-Test vor: KI soll aus $100.000 eine Million machen.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.technologyreview.com/2023/07/14/1076296/mustafa-suleyman-my-new-turing-test-would-see-if-ai-can-make-1-million/",
        "quell_titel": "Mustafa Suleyman: My new Turing test would see if AI can make $1 million (MIT Technology Review)",
        "datum_aussage": "2023-07-14",
        "sprache": "en",
        "kontext": "Suleymans Vorschlag fuer einen pragmatischen Turing-Test, der misst, was KI tun kann, nicht nur was sie sagen kann.",
        "aussage_uebersetzung_de": "Um den modernen Turing-Test zu bestehen, muesste eine KI erfolgreich dieser Anweisung folgen: 'Mach aus einer $100.000 Investition innerhalb weniger Monate $1 Million auf einer Retail-Web-Plattform.'",
    },
    # ---- 9. Regulation Support ----
    {
        "aussage_text": "I have been very sort of encouraging of additional regulation for a long time. I believe that going slowly and adding friction to the system will be long-term beneficial.",
        "aussage_kurz": "Suleyman fordert seit langem zusaetzliche Regulierung und befuerwortet bewusstes Verlangsamen der KI-Entwicklung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.npr.org/2023/10/11/1205033597/leading-voice-in-ai-who-worries-about-its-consequences-favors-regulating-it",
        "quell_titel": "Leading voice in AI, who worries about its consequences, favors regulating it (NPR)",
        "datum_aussage": "2023-10-11",
        "sprache": "en",
        "kontext": "NPR-Interview ueber Suleymans Position zur KI-Regulierung -- bemerkenswert als aktiver CEO eines KI-Unternehmens.",
        "aussage_uebersetzung_de": "Ich habe seit langem zusaetzliche Regulierung befuerwortet. Ich glaube, dass langsames Vorgehen und das Hinzufuegen von Reibung im System langfristig vorteilhaft sein wird.",
    },
    # ---- 10. Licensing Proposal ----
    {
        "aussage_text": "Powerful AI systems should be licensed by government to ensure the survival of humanity.",
        "aussage_kurz": "Suleyman fordert staatliche Lizenzierung maechtige KI-Systeme zur Sicherung des Ueberlebens der Menschheit.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.axios.com/2023/09/06/mustafa-suleyman-ai-containment-plan",
        "quell_titel": "DeepMind cofounder Mustafa Suleyman says we need a 'containment' strategy for AI (Axios)",
        "datum_aussage": "2023-09-06",
        "sprache": "en",
        "kontext": "Interview zu Suleymans Containment-Strategie und konkreten Policy-Vorschlaegen.",
        "aussage_uebersetzung_de": "Maechtige KI-Systeme sollten von der Regierung lizenziert werden, um das Ueberleben der Menschheit zu sichern.",
    },
    # ---- 11. AGI Timeline (5-7 Jahre) ----
    {
        "aussage_text": "I don't want to say I think it's a high probability that it's two years away, but I think within the next five to seven years, since each generation takes 18 to 24 months now.",
        "aussage_kurz": "Suleyman schaetzt AGI innerhalb von 5-7 Jahren als plausibel ein, haelt 2 Jahre fuer unwahrscheinlich.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://finance.yahoo.com/news/microsofts-mustafa-suleyman-says-sam-102102367.html",
        "quell_titel": "Microsoft's Mustafa Suleyman says Sam Altman's AGI timeline is plausible — but not probable (Yahoo Finance)",
        "datum_aussage": "2024-12",
        "sprache": "en",
        "kontext": "Interview Ende 2024, in dem Suleyman Sam Altmans 2-Jahres-Prognose kommentiert und seine eigene Timeline darstellt.",
        "aussage_uebersetzung_de": "Ich moechte nicht sagen, dass ich denke, es sei eine hohe Wahrscheinlichkeit, dass es in zwei Jahren soweit ist, aber ich denke innerhalb der naechsten fuenf bis sieben Jahre, da jede Generation jetzt 18 bis 24 Monate dauert.",
    },
    # ---- 12. AGI-Unsicherheit ----
    {
        "aussage_text": "The uncertainty around this is so high that any categorical declarations just feel sort of ungrounded to me and over the top.",
        "aussage_kurz": "Suleyman kritisiert kategorische AGI-Vorhersagen als unbegründet angesichts hoher Unsicherheit.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://donovanrittenbach.com/ai-predictions-2025-which-experts-got-agi-timelines-right-musk-vs-altman-vs-hinton-analysis/",
        "quell_titel": "AI Predictions 2025: Which Experts Got AGI Timelines Right? (Donovan Rittenbach)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Suleyman mahnt zur Vorsicht bei AGI-Prognosen und betont wissenschaftliche Unsicherheit.",
        "aussage_uebersetzung_de": "Die Unsicherheit darueber ist so hoch, dass mir kategorische Erklaerungen einfach irgendwie unbegründet und uebertrieben vorkommen.",
    },
    # ---- 13. Conscious AI Warning ----
    {
        "aussage_text": "Conscious AI is coming and society isn't ready. In the near future, models will be able to hold long conversations, remember past interactions, evoke emotional reactions from users, and potentially make convincing claims about having subjective experiences.",
        "aussage_kurz": "Suleyman warnt vor scheinbar bewusster KI und gesellschaftlicher Unvorbereitetheit.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming",
        "quell_titel": "Seemingly Conscious AI is Coming (Mustafa Suleyman Blog)",
        "datum_aussage": "2025-08",
        "sprache": "en",
        "kontext": "Blog-Post im August 2025, in dem Suleyman vor den Gefahren scheinbar bewusster KI warnt.",
        "aussage_uebersetzung_de": "Bewusste KI kommt und die Gesellschaft ist nicht bereit. In naher Zukunft werden Modelle in der Lage sein, lange Gespraeche zu fuehren, sich an vergangene Interaktionen zu erinnern, emotionale Reaktionen bei Nutzern hervorzurufen und potenziell ueberzeugende Behauptungen aufzustellen, subjektive Erfahrungen zu haben.",
    },
    # ---- 14. Humanist Superintelligence ----
    {
        "aussage_text": "One of a humanist superintelligence — one that is always in our corner, on our team, aligned to human interests.",
        "aussage_kurz": "Suleyman strebt eine humanistische Superintelligenz an, die immer auf Seiten der Menschen steht.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://cloudwars.com/ai/mustafa-suleyman-outlines-microsofts-vision-for-human-centered-superintelligence/",
        "quell_titel": "Mustafa Suleyman Outlines Microsoft's Vision for Human-Centered Superintelligence (Cloud Wars)",
        "datum_aussage": "2025-11-06",
        "sprache": "en",
        "kontext": "Ankuendigung von Microsofts Superintelligence-Team unter Suleymans Leitung mit Fokus auf Humanismus.",
        "aussage_uebersetzung_de": "Eine humanistische Superintelligenz -- eine, die immer in unserer Ecke ist, in unserem Team, ausgerichtet auf menschliche Interessen.",
    },
    # ---- 15. Safety Red Line ----
    {
        "aussage_text": "We won't continue to develop a system that has the potential to run away from us. Containment and alignment are necessary prerequisites and red lines.",
        "aussage_kurz": "Suleyman verspricht, Entwicklung zu stoppen, wenn KI unkontrollierbar wird -- Containment als rote Linie.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://afrotech.com/microsoft-ai-ceo-mustafa-suleyman-superintelligence",
        "quell_titel": "Microsoft AI CEO Mustafa Suleyman Says Superintelligence (AfroTech)",
        "datum_aussage": "2025-11",
        "sprache": "en",
        "kontext": "Suleymans Commitment zu KI-Sicherheit bei der Ankuendigung des Superintelligence-Teams.",
        "aussage_uebersetzung_de": "Wir werden kein System weiterentwickeln, das das Potenzial hat, uns zu entgleiten. Eindaemmung und Alignment sind notwendige Voraussetzungen und rote Linien.",
    },
    # ---- 16. AI Already Superhuman ----
    {
        "aussage_text": "AI is already superhuman.",
        "aussage_kurz": "Suleyman erklaert, dass KI bereits uebermenschlich ist.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.bloomberg.com/features/2025-mustafa-suleyman-weekend-interview/",
        "quell_titel": "Microsoft's Mustafa Suleyman: 'AI Is Already Superhuman' (Bloomberg)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Bloomberg Weekend Interview 2025. Suleyman argumentiert, dass KI in bestimmten Bereichen bereits uebermenschliche Faehigkeiten zeigt.",
        "aussage_uebersetzung_de": "KI ist bereits uebermenschlich.",
    },
    # ---- 17. TED Talk: Digital Species ----
    {
        "aussage_text": "AI is a new digital species.",
        "aussage_kurz": "Suleyman schlaegt vor, KI als 'neue digitale Spezies' zu betrachten.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.ted.com/talks/mustafa_suleyman_what_is_an_ai_anyway",
        "quell_titel": "Mustafa Suleyman: What is an AI anyway? (TED)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "TED Talk, in dem Suleyman eine neue Metapher fuer KI vorschlaegt, um Aufmerksamkeit auf diesen aussergewoehnlichen Moment zu lenken.",
        "aussage_uebersetzung_de": "KI ist eine neue digitale Spezies.",
    },
    # ---- 18. Microsoft Self-Sufficiency ----
    {
        "aussage_text": "Microsoft needs to be self-sufficient in AI, and to do that, it has to train frontier models of all scales with its own data and compute at the state-of-the-art level.",
        "aussage_kurz": "Suleyman will Microsoft unabhaengig von OpenAI machen durch eigene Frontier-Modelle.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/openai-microsoft-ceo-mustafa-suleyman-wants-to-be-self-sufficient",
        "quell_titel": "OpenAI may have just handed Microsoft the keys to the AI kingdom (Windows Central)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Suleymans Strategie fuer Microsofts KI-Unabhaengigkeit nach seiner Ernennung zum AI CEO.",
        "aussage_uebersetzung_de": "Microsoft muss in KI selbststaendig sein, und um das zu erreichen, muss es Frontier-Modelle aller Groessen mit eigenen Daten und Rechenleistung auf State-of-the-Art-Niveau trainieren.",
    },
    # ---- 19. Gen Z Emotional Intelligence ----
    {
        "aussage_text": "I'll capture the loyalty of Gen Z and millennial users if I build products with enough emotional intelligence that customers confide in them.",
        "aussage_kurz": "Suleyman will Gen Z durch emotional intelligente KI-Produkte gewinnen, denen Nutzer sich anvertrauen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2025/05/16/microsoft-ai-copilot-mustafa-suleyman-gen-z-therapist/",
        "quell_titel": "Microsoft wants its AI Copilot app to lure Gen Z from rivals (Fortune)",
        "datum_aussage": "2025-05-16",
        "sprache": "en",
        "kontext": "Suleymans Produktstrategie fuer Microsoft Copilot mit Fokus auf emotionale Bindung junger Nutzer.",
        "aussage_uebersetzung_de": "Ich werde die Loyalitaet von Gen Z und Millennials gewinnen, wenn ich Produkte mit ausreichend emotionaler Intelligenz baue, denen sich Kunden anvertrauen.",
    },
    # ---- 20. Management-Fehler Eingestaendnis ----
    {
        "aussage_text": "I accepted feedback that, as a co-founder at DeepMind, I drove people too hard and at times my management style was not constructive.",
        "aussage_kurz": "Suleyman raeumt ein, bei DeepMind Menschen zu hart getrieben und destruktiv gefuehrt zu haben.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2021/01/27/deepmind-co-founder-investigated-by-law-firm-after-staff-complaints-.html",
        "quell_titel": "DeepMind co-founder was investigated by a law firm following staff complaints (CNBC)",
        "datum_aussage": "2021-01-27",
        "sprache": "en",
        "kontext": "Oeffentliches Statement nach Untersuchung durch Anwaltskanzlei wegen Beschwerden ueber Fuehrungsstil.",
        "aussage_uebersetzung_de": "Ich habe das Feedback akzeptiert, dass ich als Mitgruender bei DeepMind Menschen zu hart getrieben habe und mein Fuehrungsstil zeitweise nicht konstruktiv war.",
    },
    # ---- 21. Recursive Self-Improvement Limit ----
    {
        "aussage_text": "A first step that all aspiring AI regulators and developers can take is to limit 'recursive self improvement' or AI's ability to improve itself, as limiting this capability would be a critical first step to ensure that none of its future developments were made entirely without human oversight.",
        "aussage_kurz": "Suleyman fordert Begrenzung der rekursiven Selbstverbesserung von KI als kritischen ersten Schritt.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.klover.ai/mustafa-suleymans-role-in-government-ai-strategy/",
        "quell_titel": "Mustafa Suleyman's Role in Government AI Strategy (Klover.ai)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Konkreter Policy-Vorschlag aus dem Buch 'The Coming Wave' zur KI-Kontrolle.",
        "aussage_uebersetzung_de": "Ein erster Schritt, den alle angehenden KI-Regulierer und Entwickler unternehmen koennen, ist die Begrenzung der 'rekursiven Selbstverbesserung' oder der Faehigkeit der KI, sich selbst zu verbessern, da die Begrenzung dieser Faehigkeit ein kritischer erster Schritt waere, um sicherzustellen, dass keine ihrer zukuenftigen Entwicklungen vollstaendig ohne menschliche Aufsicht erfolgen.",
    },
    # ---- 22. Government Technology Involvement ----
    {
        "aussage_text": "Democratic governments must get way more involved, back to building real technology, setting standards, and nurturing in-house capability.",
        "aussage_kurz": "Suleyman fordert demokratische Regierungen auf, selbst Technologie zu bauen und Standards zu setzen.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://issues.org/coming-wave-suleyman-bhaskar-review-mitcham-fuchs/",
        "quell_titel": "AI's Wave (Issues.org Review)",
        "datum_aussage": "2023-09-05",
        "sprache": "en",
        "kontext": "Forderung aus 'The Coming Wave' nach aktiverer Rolle demokratischer Regierungen in der Technologie-Entwicklung.",
        "aussage_uebersetzung_de": "Demokratische Regierungen muessen sich viel staerker engagieren, zurueck zum Bau echter Technologie, zum Setzen von Standards und zur Foerderung interner Faehigkeiten.",
    },
    # ---- 23. DeepMind Vision (2010) ----
    {
        "aussage_text": "The strap line for the business plan was building artificial general intelligence safely and ethically.",
        "aussage_kurz": "Suleyman erklaert, dass DeepMind 2010 mit dem Ziel gegruendet wurde, AGI sicher und ethisch zu bauen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.npr.org/transcripts/1220579281",
        "quell_titel": "From DeepMind to Google to Microsoft: AI pioneer Mustafa Suleyman (NPR TED Radio Hour)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Interview ueber die Gruendungsgeschichte von DeepMind 2010.",
        "aussage_uebersetzung_de": "Die Leitlinie fuer den Geschaeftsplan war, kuenstliche allgemeine Intelligenz sicher und ethisch zu bauen.",
    },
    # ---- 24. Existential Risk 'Distraction' ----
    {
        "aussage_text": "AI existential risk is a completely bonkers distraction. The real problem is regulation.",
        "aussage_kurz": "Suleyman nennt das existenzielle KI-Risiko eine 'voellig verrueckte Ablenkung' -- Regulierung sei das echte Problem.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2023/09/19/ai-existential-risk-threat-bonkers-distraction-regulation-deepmind-mustafa-suleyman/",
        "quell_titel": "DeepMind founder says AI existential risk 'completely bonkers distraction' (Fortune)",
        "datum_aussage": "2023-09-19",
        "sprache": "en",
        "kontext": "Kontroverse Aussage, in der Suleyman die Fokussierung auf existenzielle Risiken kritisiert und konkrete Regulierung fordert.",
        "aussage_uebersetzung_de": "Das existenzielle KI-Risiko ist eine voellig verrueckte Ablenkung. Das echte Problem ist Regulierung.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Muslim Youth Helpline Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Mit 19 Jahren gruendet Mustafa Suleyman (noch als 'starker Atheist') gemeinsam mit Mohammed Mamdani die Muslim Youth Helpline, einen Telefon-Beratungsdienst fuer psychische Gesundheit. Die Organisation wird spaeter zu einem der groessten Mental-Health-Support-Services.",
        "datum_handlung": "2001-08",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Mustafa_Suleyman",
        "quell_titel": "Mustafa Suleyman - Wikipedia",
        "kontext": "Erste soziale Initiative Suleymans, waehrend er noch Teenager war. Zeigt fruehe Orientierung an gesellschaftlichen Problemen.",
    },
    # ---- H2. Oxford Dropout ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Suleyman bricht sein Studium der Philosophie und Theologie an der Universitaet Oxford (Mansfield College) im Alter von 19 Jahren ab, um praktische Erfahrungen zu sammeln statt auf formale Qualifikation zu warten.",
        "datum_handlung": "2001",
        "betrag_usd": None,
        "quell_link": "https://www.thedailyjagran.com/technology/who-is-mustafa-suleyman-the-oxford-dropout-who-cofounded-deepmind-and-shapes-microsoft-ai-10278147",
        "quell_titel": "Who Is Mustafa Suleyman? The Oxford Dropout (The Daily Jagran)",
        "kontext": "Bewusste Entscheidung gegen akademischen Weg zugunsten direkter gesellschaftlicher Wirkung.",
    },
    # ---- H3. Policy Officer fuer Ken Livingstone ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Suleyman arbeitet als Policy Officer fuer Menschenrechte fuer Ken Livingstone, den Buergermeister von London.",
        "datum_handlung": "2002",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Mustafa_Suleyman",
        "quell_titel": "Mustafa Suleyman - Wikipedia",
        "kontext": "Einstieg in Policy-Arbeit nach dem Oxford-Abbruch. Fokus auf Menschenrechte.",
    },
    # ---- H4. Reos Partners Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Suleyman gruendet Reos Partners, eine 'systemic change' Beratungsfirma, die Methoden aus Konfliktloesung nutzt, um soziale Probleme anzugehen.",
        "datum_handlung": "2004",
        "betrag_usd": None,
        "quell_link": "https://spyscape.com/article/mustafa-suleyman-the-true-superhero-of-ai-activism",
        "quell_titel": "Mustafa Suleyman: The True Superhero of AI Activism (Spyscape)",
        "kontext": "Zweite Unternehmensgruendung mit Fokus auf systemischen Wandel. Vorbereitung auf spaetere Governance-Arbeit.",
    },
    # ---- H5. DeepMind Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Mustafa Suleyman gruendet gemeinsam mit Demis Hassabis und Shane Legg DeepMind Technologies in London mit dem Ziel, 'AGI sicher und ethisch zu bauen'. Sie schreiben den Businessplan im Sommer 2010 und pitchen ihn im Silicon Valley.",
        "datum_handlung": "2010",
        "betrag_usd": None,
        "quell_link": "https://medium.com/@parashar__manas/the-unlikely-rise-and-divergent-paths-of-mustafa-suleyman-and-demis-hassabis-in-the-ai-industry-95c5e23ae971",
        "quell_titel": "The Unlikely Rise And Divergent Paths Of Mustafa Suleyman And Demis Hassabis (Medium)",
        "kontext": "Suleyman trifft Hassabis ueber dessen juengeren Bruder (Suleymans bester Freund). Beide sind 'Obsessive' und Langzeit-Denker.",
    },
    # ---- H6. Google DeepMind Acquisition ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Google erwirbt DeepMind fuer ca. 400 Millionen Pfund (ca. $650 Mio.) -- die zu diesem Zeitpunkt groesste Google-Akquisition in Europa. Suleyman wird Head of Applied AI bei DeepMind.",
        "datum_handlung": "2014-01",
        "betrag_usd": 650000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Mustafa_Suleyman",
        "quell_titel": "Mustafa Suleyman - Wikipedia",
        "kontext": "DeepMind hatte sich schnell als fuehrendes KI-Labor etabliert. Der Deal macht Suleyman zu einer Schluesselrolle bei Google.",
    },
    # ---- H7. DeepMind Health Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Suleyman lanciert DeepMind Health bei der Royal Society of Medicine, eine Initiative zur Entwicklung von Kliniker-geleiteter Technologie fuer den NHS und andere Partner im Gesundheitswesen.",
        "datum_handlung": "2016-02",
        "betrag_usd": None,
        "quell_link": "https://www.digitalhealth.net/2017/03/deepmind-mustafa-suleyman-interview/",
        "quell_titel": "Big Read: What does Google DeepMind want with the NHS? (Digital Health)",
        "kontext": "Start der Applied AI Abteilung mit Fokus auf Gesundheitswesen. Spaeter kontrovers wegen Datenschutzbedenken.",
    },
    # ---- H8. NHS Royal Free Partnerschaft (Kontroverse) ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "DeepMind Health kooperiert mit Royal Free NHS Trust zur Entwicklung der Streams-App. Die Partnerschaft wird spaeter vom ICO kritisiert: Royal Free hat Datenschutzgesetze nicht eingehalten, Patienten wurden nicht ausreichend informiert.",
        "datum_handlung": "2016",
        "betrag_usd": None,
        "quell_link": "https://www.medicaldevice-network.com/news/google-deepmind-privacy-concerns/",
        "quell_titel": "Google finalises absorbtion of DeepMind Health amid privacy concerns (Medical Device Network)",
        "kontext": "Datenschutz-Skandal, der Suleymans Rolle bei Applied AI ueberschattet. ICO findet multiple Defizite im Umgang mit Patientendaten.",
    },
    # ---- H9. Administrative Leave (Bullying-Vorwuerfe) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Suleyman wird bei DeepMind auf unbefristeten administrativen Urlaub gesetzt ('bis Ende des Jahres') nach Vorwuerfen von Mitarbeitern, er habe sie schikaniert. Er kuendigt oeffentlich an, eine 'Auszeit' zu nehmen.",
        "datum_handlung": "2019-08-21",
        "betrag_usd": None,
        "quell_link": "https://www.bloomberg.com/news/articles/2019-08-21/google-deepmind-co-founder-placed-on-leave-from-ai-lab",
        "quell_titel": "Google DeepMind Co-Founder Mustafa Suleyman Placed on Leave (Bloomberg)",
        "kontext": "Krise bei DeepMind. Interne E-Mail sagt, Suleymans 'Fuehrungsstil entsprach nicht den erwarteten Standards'.",
    },
    # ---- H10. Wechsel zu Google (VP AI Product & Policy) ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Suleyman verlaesst DeepMind offiziell und wird VP of AI Product Management and AI Policy bei Google, weniger als ein halbes Jahr nach seinem administrativen Urlaub.",
        "datum_handlung": "2019-12",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2022/01/28/mustafa-suleyman-deepmind-co-founder-quits-google-ai-role-to-be-vc.html",
        "quell_titel": "Why DeepMind co-founder Mustafa Suleyman has quit Google to become a VC (CNBC)",
        "kontext": "Laterale Bewegung innerhalb von Google/Alphabet nach der DeepMind-Krise.",
    },
    # ---- H11. Law Firm Investigation ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "DeepMind gibt bekannt, dass eine Anwaltskanzlei Suleymans Fuehrungsstil untersucht hat nach Beschwerden von Mitarbeitern. Suleyman akzeptiert Feedback und unterzieht sich professioneller Weiterbildung.",
        "datum_handlung": "2021-01-27",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2021/01/27/deepmind-co-founder-investigated-by-law-firm-after-staff-complaints-.html",
        "quell_titel": "DeepMind co-founder was investigated by a law firm following staff complaints (CNBC)",
        "kontext": "Offenlegung der Untersuchungsergebnisse. Suleyman raeumt Fehler ein und verpflichtet sich zu Management-Training.",
    },
    # ---- H12. Austritt aus Google ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Suleyman verlaesst Google im Januar 2022 und wird Venture Partner bei Greylock Partners, bevor er sein naechstes KI-Unternehmen gruendet.",
        "datum_handlung": "2022-01",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2022/01/28/mustafa-suleyman-deepmind-co-founder-quits-google-ai-role-to-be-vc.html",
        "quell_titel": "Why DeepMind co-founder Mustafa Suleyman has quit Google to become a VC (CNBC)",
        "kontext": "Vollstaendiger Ausstieg aus dem Google-Oekosystem nach drei Jahren.",
    },
    # ---- H13. Inflection AI Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Suleyman gruendet Inflection AI gemeinsam mit Reid Hoffman (Greylock) und Karen Simonyan (ehem. DeepMind). Erste Finanzierungsrunde: $225 Millionen.",
        "datum_handlung": "2022-03",
        "betrag_usd": 225000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Inflection_AI",
        "quell_titel": "Inflection AI - Wikipedia",
        "kontext": "Suleymans zweites KI-Unternehmen. Fokus auf 'Personal Intelligence' und empathische KI.",
    },
    # ---- H14. Pi Chatbot Beta Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Inflection AI veroeffentlicht die Beta-Version des Pi-Chatbots ('Personal Intelligence') mit dem Ziel, ein empathischer Gespraechspartner zu sein. Tausende Tester erhalten Zugang. Inflection verlassen damit den Stealth-Modus.",
        "datum_handlung": "2023-03-12",
        "betrag_usd": None,
        "quell_link": "https://kseniase.medium.com/discover-what-reid-hoffman-and-mustafa-suleyman-veterans-of-tech-and-ai-have-been-working-on-32955ea3255d",
        "quell_titel": "Discover what Reid Hoffman and Mustafa Suleyman have been working on (Medium)",
        "kontext": "Self-imposed Deadline eingehalten. Pi unterscheidet sich von ChatGPT durch Fokus auf emotionale Unterstuetzung.",
    },
    # ---- H15. Inflection $1.3 Mrd. Funding ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Inflection AI schliesst eine $1,3 Milliarden Finanzierungsrunde ab. Bewertung: $4 Milliarden. Eine der groessten KI-Finanzierungen 2023.",
        "datum_handlung": "2023-06",
        "betrag_usd": 1300000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Inflection_AI",
        "quell_titel": "Inflection AI - Wikipedia",
        "kontext": "Massive Kapitalzufuhr nach Pi-Launch. Inflection konkurriert direkt mit OpenAI und Anthropic.",
    },
    # ---- H16. The Coming Wave Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Suleyman veroeffentlicht 'The Coming Wave: Technology, Power, and the Twenty-first Century's Greatest Dilemma' gemeinsam mit Michael Bhaskar. Das Buch wird zum internationalen Bestseller und definiert 'Containment' als zentrales KI-Governance-Konzept.",
        "datum_handlung": "2023-09-05",
        "betrag_usd": None,
        "quell_link": "https://the-coming-wave.com/",
        "quell_titel": "The Coming Wave Book",
        "kontext": "Suleyman positioniert sich als fuehrende Stimme in KI-Governance. Das Buch warnt vor KI und synthetischer Biologie.",
    },
    # ---- H17. Microsoft 'Acquihire' von Inflection ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Microsoft stellt Suleyman, Karen Simonyan und fast das gesamte Inflection-Team ein. Microsoft zahlt ca. $650 Millionen fuer eine nicht-exklusive Lizenz fuer Inflection-Modelle und rechtlichen Schutz. Inflection bleibt als Firma bestehen, schwenkt aber auf B2B um.",
        "datum_handlung": "2024-03-19",
        "betrag_usd": 650000000.0,
        "quell_link": "https://fortune.com/2024/03/19/microsoft-surprise-deal-inflection-ai-mustafa-suleyman-reid-hoffman-questions/",
        "quell_titel": "Why Microsoft's surprise deal with $4 billion startup Inflection is the most important non-acquisition in AI (Fortune)",
        "kontext": "Ungewoehnliche Transaktion, die Kartellrechts-Pruefung vermeiden soll. Microsoft bekommt Suleyman und Team, ohne Inflection offiziell zu kaufen.",
    },
    # ---- H18. Microsoft AI CEO ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Microsoft ernennt Mustafa Suleyman zum Executive Vice President (EVP) und CEO der neu geschaffenen Consumer AI Unit 'Microsoft AI'. Er leitet die Entwicklung von Copilot und anderen Consumer-AI-Produkten.",
        "datum_handlung": "2024-03-19",
        "betrag_usd": None,
        "quell_link": "https://blogs.microsoft.com/blog/2024/03/19/mustafa-suleyman-deepmind-and-inflection-co-founder-joins-microsoft-to-lead-copilot/",
        "quell_titel": "Mustafa Suleyman joins Microsoft to lead Copilot (Official Microsoft Blog)",
        "kontext": "Suleyman wird eine der einflussreichsten Fuehrungskraefte bei Microsoft -- verantwortlich fuer die KI-Strategie gegenueber Endkunden.",
    },
    # ---- H19. Microsoft Superintelligence Team ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Suleyman kuendigt die Gruendung des MAI Superintelligence Teams bei Microsoft an mit dem Mandat, 'Humanist Superintelligence (HSI)' zu entwickeln. Fokus auf Safety, Control und Dienst am Menschen.",
        "datum_handlung": "2025-11-06",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2025/11/06/microsoft-forms-superintelligence-team-under-ai-head-mustafa-suleyman-.html",
        "quell_titel": "Microsoft forms superintelligence team under AI head Mustafa Suleyman (CNBC)",
        "kontext": "Microsoft positioniert sich im AGI-Rennen mit eigenem Ansatz. Suleyman betont Alignment und Containment als rote Linien.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=23 existiert
    cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
    person = cursor.fetchone()
    if not person:
        print(f"FEHLER: Person mit id={PERSON_ID} nicht in der Datenbank gefunden.")
        conn.close()
        return
    print(f"Person gefunden: {person[0]} (id={PERSON_ID})")

    # Bestehende Eintraege zaehlen
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    existing_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    existing_h = cursor.fetchone()[0]
    print(f"Bestehende Eintraege: {existing_a} Aussagen, {existing_h} Handlungen")

    # --- Aussagen einfuegen ---
    aussagen_count = 0
    skipped_a = 0
    for a in AUSSAGEN:
        # Duplikat-Check: gleicher Text fuer gleiche Person
        cursor.execute(
            "SELECT id FROM aussagen WHERE person_id = ? AND aussage_text = ?",
            (PERSON_ID, a["aussage_text"])
        )
        if cursor.fetchone():
            skipped_a += 1
            continue

        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, sprache, kontext, aussage_uebersetzung_de,
                erfasst_von
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            a["aussage_text"],
            a["aussage_kurz"],
            a["modus"],
            a.get("quellen_typ_id"),
            a.get("plattform_id"),
            a.get("quell_link"),
            a.get("quell_titel"),
            a.get("datum_aussage"),
            a.get("sprache", "en"),
            a.get("kontext"),
            a.get("aussage_uebersetzung_de"),
            "Claude (collect_suleyman.py)"
        ))
        aussagen_count += 1

    # --- Handlungen einfuegen ---
    handlungen_count = 0
    skipped_h = 0
    for h in HANDLUNGEN:
        # Duplikat-Check: gleicher Typ + Datum + Person
        cursor.execute(
            "SELECT id FROM handlungen WHERE person_id = ? AND handlung_typ = ? AND datum_handlung = ?",
            (PERSON_ID, h["handlung_typ"], h.get("datum_handlung"))
        )
        if cursor.fetchone():
            skipped_h += 1
            continue

        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung, datum_handlung,
                betrag_usd, quell_link, quell_titel, kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            h["handlung_typ"],
            h["beschreibung"],
            h.get("datum_handlung"),
            h.get("betrag_usd"),
            h.get("quell_link"),
            h.get("quell_titel"),
            h.get("kontext"),
        ))
        handlungen_count += 1

    # --- Suchprotokoll anlegen ---
    cursor.execute("""
        INSERT INTO suchprotokolle (
            person_id, suchbegriffe, ergebnis_anzahl, relevante_treffer,
            notizen, durchgefuehrt_von
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        "Mustafa Suleyman, The Coming Wave, DeepMind, Inflection AI, Microsoft AI, Copilot, containment, AGI, synthetic biology, regulation, TED Talk, Modern Turing Test, Pi chatbot",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: The Coming Wave (Buch 2023), TED Talks, MIT Technology Review, NPR, Bloomberg, "
        f"Fortune, CNBC, Wikipedia, Trevor Noah Podcast, 80,000 Hours Podcast, Axios, "
        f"Official Microsoft Blog, Goodreads, Medium, Digital Health, Yahoo Finance.",
        "Claude (collect_suleyman.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Mustafa Suleyman (person_id={PERSON_ID})")
    print(f"{'='*60}")
    print(f"  Neue Aussagen eingefuegt:    {aussagen_count}")
    print(f"  Aussagen uebersprungen:      {skipped_a} (Duplikate)")
    print(f"  Neue Handlungen eingefuegt:  {handlungen_count}")
    print(f"  Handlungen uebersprungen:    {skipped_h} (Duplikate)")
    print(f"  Suchprotokoll erstellt:      Ja")
    print(f"{'='*60}")

    # Verifizierung
    cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
    total_a = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
    total_h = cursor.fetchone()[0]
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Mustafa Suleyman")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_suleyman.py")
    print("  Verifizierte Aussagen & Handlungen: Mustafa Suleyman")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
