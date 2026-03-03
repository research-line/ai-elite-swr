#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_altman.py
=================
Sammelt verifizierbare Aussagen und Handlungen von Sam Altman (person_id=2)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Blog-Posts, Congressional Testimony und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 2  # Sam Altman

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
    # ---- 1. StrictlyVC Interview, Jan 2023 ----
    {
        "aussage_text": "The bad case — and I think this is important to say — is, like, lights out for all of us.",
        "aussage_kurz": "Altman warnt, dass der schlimmste Fall von KI das Ende fuer alle bedeuten koennte.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 1,    # YouTube
        "quell_link": "https://techcrunch.com/2023/01/16/a-peek-into-future-as-sam-altman-sees-it/",
        "quell_titel": "StrictlyVC in conversation with Sam Altman, part one (TechCrunch)",
        "datum_aussage": "2023-01-17",
        "sprache": "en",
        "kontext": "Interview mit Connie Loizos (StrictlyVC/TechCrunch) im Januar 2023 ueber KI-Risiken und die Zukunft von OpenAI.",
        "aussage_uebersetzung_de": "Der schlimmste Fall -- und ich denke, es ist wichtig, das zu sagen -- ist so etwas wie: Licht aus fuer uns alle.",
    },
    # ---- 2. ABC News Interview, Maerz 2023 ----
    {
        "aussage_text": "I think people should be happy that we are a little bit scared of this.",
        "aussage_kurz": "Altman sagt, es sei gut, dass die Entwickler selbst etwas Angst vor KI haben.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://abcnews.go.com/Technology/openai-ceo-sam-altman-ai-reshape-society-acknowledges/story?id=97897122",
        "quell_titel": "OpenAI CEO Sam Altman says AI will reshape society, acknowledges risks (ABC News)",
        "datum_aussage": "2023-03-16",
        "sprache": "en",
        "kontext": "Interview mit ABC News (Rebecca Jarvis) kurz nach dem Launch von GPT-4. Altman aeussert sich offen zu Risiken.",
        "aussage_uebersetzung_de": "Ich denke, die Leute sollten froh sein, dass wir selbst ein bisschen Angst davor haben.",
    },
    # ---- 3. ABC News Interview, Maerz 2023 (Ergaenzung) ----
    {
        "aussage_text": "I think if I said I were not [scared], you should either not trust me or be very unhappy I'm in this job.",
        "aussage_kurz": "Altman sagt, man solle ihm nicht vertrauen, wenn er keine Angst vor KI haette.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://abcnews.go.com/Technology/openai-ceo-sam-altman-ai-reshape-society-acknowledges/story?id=97897122",
        "quell_titel": "OpenAI CEO Sam Altman says AI will reshape society, acknowledges risks (ABC News)",
        "datum_aussage": "2023-03-16",
        "sprache": "en",
        "kontext": "Fortsetzung des ABC-News-Interviews. Auf die Nachfrage, ob er persoenlich Angst habe.",
        "aussage_uebersetzung_de": "Wenn ich sagen wuerde, dass ich keine Angst haette, sollte man mir entweder nicht vertrauen oder sehr unzufrieden sein, dass ich diesen Job mache.",
    },
    # ---- 4. US Senate Testimony, Mai 2023 ----
    {
        "aussage_text": "My worst fears are that we cause significant harm to the world. I think if this technology goes wrong, it can go quite wrong.",
        "aussage_kurz": "Vor dem US-Senat warnt Altman, dass KI-Technologie gravierend schiefgehen koennte.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony
        "quell_link": "https://www.judiciary.senate.gov/committee-activity/hearings/oversight-of-ai-rules-for-artificial-intelligence",
        "quell_titel": "Oversight of A.I.: Rules for Artificial Intelligence, US Senate Judiciary Subcommittee",
        "datum_aussage": "2023-05-16",
        "sprache": "en",
        "kontext": "Anhoerung vor dem Senate Judiciary Subcommittee on Privacy, Technology, and the Law. Erste Kongressanhoerung eines KI-CEOs.",
        "aussage_uebersetzung_de": "Meine groesste Angst ist, dass wir der Welt erheblichen Schaden zufuegen. Wenn diese Technologie schiefgeht, kann sie ziemlich schiefgehen.",
    },
    # ---- 5. US Senate Testimony, Mai 2023 (Regulierung) ----
    {
        "aussage_text": "We think that regulatory intervention by governments will be critical to mitigate the risks of increasingly powerful models.",
        "aussage_kurz": "Altman fordert vor dem US-Senat staatliche Regulierung fuer KI-Modelle.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.judiciary.senate.gov/imo/media/doc/2023-05-16%20-%20Bio%20&%20Testimony%20-%20Altman.pdf",
        "quell_titel": "Written Testimony of Sam Altman, CEO OpenAI, before US Senate",
        "datum_aussage": "2023-05-16",
        "sprache": "en",
        "kontext": "Eroeffnungserklaerung bei der Senatsanhoerung. Altman fordert aktiv staatliche KI-Regulierung.",
        "aussage_uebersetzung_de": "Wir glauben, dass regulatorisches Eingreifen der Regierungen entscheidend sein wird, um die Risiken immer leistungsfaehigerer Modelle zu mindern.",
    },
    # ---- 6. US Senate Testimony, Mai 2023 (Arbeitsmarkt) ----
    {
        "aussage_text": "There will be an impact on jobs. We try to be very clear about that, and I think it'll require partnership between industry and government, but mostly action by government, to figure out how we want to mitigate that.",
        "aussage_kurz": "Altman raeumt vor dem Senat Auswirkungen von KI auf Arbeitsplaetze ein und fordert staatliches Handeln.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 10,
        "quell_link": "https://www.techpolicy.press/transcript-senate-judiciary-subcommittee-hearing-on-oversight-of-ai/",
        "quell_titel": "Transcript: Senate Judiciary Subcommittee Hearing on Oversight of AI (TechPolicy.Press)",
        "datum_aussage": "2023-05-16",
        "sprache": "en",
        "kontext": "Antwort auf Fragen zu den Auswirkungen von KI auf den Arbeitsmarkt waehrend der Senatsanhoerung.",
        "aussage_uebersetzung_de": "Es wird Auswirkungen auf Arbeitsplaetze geben. Wir versuchen, das sehr klar zu sagen, und ich denke, es wird eine Partnerschaft zwischen Industrie und Regierung erfordern, aber vor allem Handeln der Regierung, um herauszufinden, wie wir das abmildern wollen.",
    },
    # ---- 7. "Moore's Law for Everything" Blog, Maerz 2021 ----
    {
        "aussage_text": "In the next five years, computer programs that can think will read legal documents and give medical advice. In the next decade, they will do assembly-line work and maybe even become companions.",
        "aussage_kurz": "Altman prognostiziert, dass KI in 5-10 Jahren juristische und medizinische Aufgaben uebernimmt.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://moores.samaltman.com/",
        "quell_titel": "Moore's Law for Everything (Sam Altman Blog)",
        "datum_aussage": "2021-03-16",
        "sprache": "en",
        "kontext": "Blog-Post 'Moore's Law for Everything', in dem Altman eine umfassende Vision fuer KI-getriebene Wirtschaftsumwaelzung und neue Steuerpolitik skizziert.",
        "aussage_uebersetzung_de": "In den naechsten fuenf Jahren werden Computerprogramme, die denken koennen, juristische Dokumente lesen und medizinische Ratschlaege geben. Im naechsten Jahrzehnt werden sie Fliessband-Arbeit erledigen und vielleicht sogar zu Begleitern werden.",
    },
    # ---- 8. "Moore's Law for Everything" Blog (Steuerpolitik) ----
    {
        "aussage_text": "We should therefore focus on taxing capital rather than labor, and we should use these taxes as an opportunity to directly distribute ownership and wealth to citizens.",
        "aussage_kurz": "Altman fordert die Besteuerung von Kapital statt Arbeit und direkte Vermoegensuebertragung an Buerger.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://moores.samaltman.com/",
        "quell_titel": "Moore's Law for Everything (Sam Altman Blog)",
        "datum_aussage": "2021-03-16",
        "sprache": "en",
        "kontext": "Zentraler Policy-Vorschlag im Blog-Post. Altman schlaegt vor, AI-generierte Wertschoepfung ueber Kapitalbesteuerung umzuverteilen.",
        "aussage_uebersetzung_de": "Wir sollten uns daher darauf konzentrieren, Kapital statt Arbeit zu besteuern, und wir sollten diese Steuern als Gelegenheit nutzen, Eigentum und Wohlstand direkt an die Buerger zu verteilen.",
    },
    # ---- 9. "Planning for AGI and beyond" Blog, Feb 2023 ----
    {
        "aussage_text": "If AGI is successfully created, this technology could help us elevate humanity by increasing abundance, turbocharging the global economy, and aiding in the discovery of new scientific knowledge that changes the limits of possibility.",
        "aussage_kurz": "Altman beschreibt AGI als Technologie, die die Menschheit durch Ueberfluss und neue Entdeckungen erheben koennte.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://openai.com/index/planning-for-agi-and-beyond/",
        "quell_titel": "Planning for AGI and beyond (OpenAI Blog)",
        "datum_aussage": "2023-02-24",
        "sprache": "en",
        "kontext": "Offizieller OpenAI Blog-Post, in dem Altman die AGI-Strategie und Sicherheitsueberlegungen von OpenAI darlegt.",
        "aussage_uebersetzung_de": "Wenn AGI erfolgreich erschaffen wird, koennte diese Technologie uns helfen, die Menschheit zu erheben, indem sie Ueberfluss schafft, die Weltwirtschaft beschleunigt und bei der Entdeckung neuen wissenschaftlichen Wissens hilft, das die Grenzen des Moeglichen verschiebt.",
    },
    # ---- 10. "Planning for AGI and beyond" (Fehlausrichtung) ----
    {
        "aussage_text": "A misaligned superintelligent AGI could cause grievous harm to the world; an autocratic regime with a decisive superintelligence lead could do that too.",
        "aussage_kurz": "Altman warnt vor den Gefahren einer fehlausgerichteten Superintelligenz und autoritaerer Regime mit KI-Vorsprung.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://openai.com/index/planning-for-agi-and-beyond/",
        "quell_titel": "Planning for AGI and beyond (OpenAI Blog)",
        "datum_aussage": "2023-02-24",
        "sprache": "en",
        "kontext": "Im gleichen Blog-Post benennt Altman die zwei grossen Risiken: technische Fehlausrichtung und autoritaeren Missbrauch.",
        "aussage_uebersetzung_de": "Eine fehlausgerichtete superintelligente AGI koennte der Welt schweren Schaden zufuegen; ein autokratisches Regime mit einem entscheidenden Superintelligenz-Vorsprung koennte das ebenfalls.",
    },
    # ---- 11. "Planning for AGI and beyond" (Governance) ----
    {
        "aussage_text": "We don't expect the future to be an unqualified utopia, but we want to maximize the good and minimize the bad, and for AGI to be an amplifier of humanity.",
        "aussage_kurz": "Altman will keine Utopie versprechen, sondern AGI als Verstaerker der Menschheit gestalten.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://openai.com/index/planning-for-agi-and-beyond/",
        "quell_titel": "Planning for AGI and beyond (OpenAI Blog)",
        "datum_aussage": "2023-02-24",
        "sprache": "en",
        "kontext": "Vision fuer eine ausgewogene AGI-Entwicklung im offiziellen OpenAI-Strategiedokument.",
        "aussage_uebersetzung_de": "Wir erwarten nicht, dass die Zukunft eine uneingeschraenkte Utopie sein wird, aber wir wollen das Gute maximieren und das Schlechte minimieren, und dass AGI ein Verstaerker der Menschheit ist.",
    },
    # ---- 12. Lex Fridman Podcast #367, Maerz 2023 ----
    {
        "aussage_text": "I don't think any one person should be in control of an AGI, and I don't think any one person will.",
        "aussage_kurz": "Altman lehnt die Kontrolle ueber AGI durch eine einzelne Person ab.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://lexfridman.com/sam-altman-2-transcript/",
        "quell_titel": "Lex Fridman Podcast #367: Sam Altman on GPT-4, ChatGPT, and the Future of AI",
        "datum_aussage": "2023-03-25",
        "sprache": "en",
        "kontext": "Interview mit Lex Fridman ueber AGI-Governance, Macht und Kontrolle. Altman betont dezentrale Kontrolle.",
        "aussage_uebersetzung_de": "Ich glaube nicht, dass eine einzelne Person die Kontrolle ueber eine AGI haben sollte, und ich glaube auch nicht, dass eine einzelne Person sie haben wird.",
    },
    # ---- 13. Lex Fridman Podcast #419, Maerz 2024 ----
    {
        "aussage_text": "I think some things are going to go theatrically wrong with AI. I don't know what the percent chance is that I eventually get shot, but it's not zero.",
        "aussage_kurz": "Altman rechnet mit dramatischen KI-Fehlschlaegen und sieht persoenliche Bedrohungen als reales Risiko.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/sam-altman-2-transcript/",
        "quell_titel": "Lex Fridman Podcast #419: Sam Altman on OpenAI, GPT-5, Sora, Board Saga, Elon Musk, Ilya, Power & AGI",
        "datum_aussage": "2024-03-18",
        "sprache": "en",
        "kontext": "Zweites langes Interview mit Lex Fridman nach der Board-Krise. Altman spricht ueberraschend offen ueber persoenliche Risiken.",
        "aussage_uebersetzung_de": "Ich denke, einige Dinge werden bei KI dramatisch schiefgehen. Ich weiss nicht, wie hoch die Wahrscheinlichkeit ist, dass ich irgendwann erschossen werde, aber sie ist nicht null.",
    },
    # ---- 14. Lex Fridman Podcast (Alignment-Kritik) ----
    {
        "aussage_text": "I think there's a bit of sleight of hand when people talk about aligning an AI to human preferences and values. There's a hidden asterisk: it's the values and preferences I approve of.",
        "aussage_kurz": "Altman kritisiert, dass 'Alignment an menschliche Werte' oft bedeutet: an die Werte, die ich billige.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/sam-altman-2-transcript/",
        "quell_titel": "Lex Fridman Podcast #419: Sam Altman on OpenAI, GPT-5, Sora, Board Saga, Elon Musk, Ilya, Power & AGI",
        "datum_aussage": "2024-03-18",
        "sprache": "en",
        "kontext": "Altman reflektiert ueber die Schwierigkeit, KI an 'menschliche Werte' auszurichten, wenn unklar ist, wessen Werte gemeint sind.",
        "aussage_uebersetzung_de": "Ich denke, es gibt eine Art Taschenspielertrick, wenn Leute davon sprechen, eine KI an menschliche Praeferenzen und Werte anzupassen. Da ist ein verstecktes Sternchen: Es sind die Werte und Praeferenzen, die ich billige.",
    },
    # ---- 15. Twitter/X, Dez 2022 ----
    {
        "aussage_text": "i am a stochastic parrot, and so r u",
        "aussage_kurz": "Altman bezeichnet sich und alle Menschen als 'stochastische Papageien' -- wie LLMs.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/sama/status/1599471830255177728",
        "quell_titel": "Sam Altman on X (@sama)",
        "datum_aussage": "2022-12-04",
        "sprache": "en",
        "kontext": "Tweet vier Tage nach dem Launch von ChatGPT. Spielt auf die Kritik an LLMs als 'stochastic parrots' an und wendet den Begriff auf den Menschen an.",
        "aussage_uebersetzung_de": "Ich bin ein stochastischer Papagei, und du auch.",
    },
    # ---- 16. "The Intelligence Age" Blog, Sep 2024 ----
    {
        "aussage_text": "It is possible that we will have superintelligence in a few thousand days (!); it may take longer, but I'm confident we'll get there.",
        "aussage_kurz": "Altman haelt Superintelligenz in wenigen tausend Tagen fuer moeglich.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://ia.samaltman.com/",
        "quell_titel": "The Intelligence Age (Sam Altman Blog)",
        "datum_aussage": "2024-09-23",
        "sprache": "en",
        "kontext": "Persoenlicher Blog-Post mit dem Titel 'The Intelligence Age'. Altman skizziert seine Vision einer neuen Aera, angetrieben durch KI.",
        "aussage_uebersetzung_de": "Es ist moeglich, dass wir in ein paar tausend Tagen Superintelligenz haben (!); es kann laenger dauern, aber ich bin zuversichtlich, dass wir dorthin gelangen werden.",
    },
    # ---- 17. "The Intelligence Age" Blog (Wohlstand) ----
    {
        "aussage_text": "I believe the future is going to be so bright that no one can do it justice by trying to write about it now; a defining characteristic of the Intelligence Age will be massive prosperity.",
        "aussage_kurz": "Altman prognostiziert massiven Wohlstand als Merkmal des 'Zeitalters der Intelligenz'.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://ia.samaltman.com/",
        "quell_titel": "The Intelligence Age (Sam Altman Blog)",
        "datum_aussage": "2024-09-23",
        "sprache": "en",
        "kontext": "Optimistische Kernaussage des Blog-Posts ueber die positiven Auswirkungen fortschreitender KI.",
        "aussage_uebersetzung_de": "Ich glaube, die Zukunft wird so hell sein, dass ihr niemand gerecht werden kann, wenn er jetzt darueber zu schreiben versucht; ein praegendes Merkmal des Zeitalters der Intelligenz wird massiver Wohlstand sein.",
    },
    # ---- 18. "The Intelligence Age" Blog (Deep Learning) ----
    {
        "aussage_text": "Deep learning worked, got predictably better with scale, and we dedicated increasing resources to it. That's really it; humanity discovered an algorithm that could really, truly learn any distribution of data.",
        "aussage_kurz": "Altman erklaert den Durchbruch der KI damit, dass die Menschheit einen universellen Lernalgorithmus entdeckt hat.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://ia.samaltman.com/",
        "quell_titel": "The Intelligence Age (Sam Altman Blog)",
        "datum_aussage": "2024-09-23",
        "sprache": "en",
        "kontext": "Altman fasst den Kern des KI-Fortschritts in einem Satz zusammen: Deep Learning funktioniert und skaliert vorhersagbar.",
        "aussage_uebersetzung_de": "Deep Learning hat funktioniert, wurde vorhersagbar besser mit Skalierung, und wir widmeten ihm zunehmende Ressourcen. Das ist im Grunde alles; die Menschheit hat einen Algorithmus entdeckt, der wirklich jede Datenverteilung erlernen kann.",
    },
    # ---- 19. "Reflections" Blog, Jan 2025 ----
    {
        "aussage_text": "We are now confident we know how to build AGI as we have traditionally understood it. We believe that, in 2025, we may see the first AI agents 'join the workforce' and materially change the output of companies.",
        "aussage_kurz": "Altman erklaert Anfang 2025, OpenAI wisse nun, wie man AGI baut, und kuendigt KI-Agenten in der Arbeitswelt an.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blog.samaltman.com/reflections",
        "quell_titel": "Reflections (Sam Altman Blog)",
        "datum_aussage": "2025-01-06",
        "sprache": "en",
        "kontext": "Jahresrueckblick-Blog-Post, in dem Altman die kuenftige AGI-Entwicklung und den Eintritt von KI-Agenten in die Arbeitswelt ankuendigt.",
        "aussage_uebersetzung_de": "Wir sind jetzt zuversichtlich, dass wir wissen, wie man AGI baut, so wie wir sie traditionell verstanden haben. Wir glauben, dass wir 2025 die ersten KI-Agenten sehen koennten, die 'der Belegschaft beitreten' und die Leistung von Unternehmen wesentlich veraendern.",
    },
    # ---- 20. "Reflections" Blog (Governance-Fehler) ----
    {
        "aussage_text": "The whole event was, in my opinion, a big failure of governance by well-meaning people, myself included.",
        "aussage_kurz": "Altman bezeichnet seine eigene Entlassung 2023 als 'grosses Governance-Versagen' -- einschliesslich seiner eigenen Rolle.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blog.samaltman.com/reflections",
        "quell_titel": "Reflections (Sam Altman Blog)",
        "datum_aussage": "2025-01-06",
        "sprache": "en",
        "kontext": "Altman reflektiert ueber die Board-Krise vom November 2023 und uebernimmt Mitverantwortung.",
        "aussage_uebersetzung_de": "Das gesamte Ereignis war meiner Meinung nach ein grosses Governance-Versagen von wohlmeinenden Menschen, mich eingeschlossen.",
    },
    # ---- 21. Davos/WEF, Jan 2024 ----
    {
        "aussage_text": "AI is good at some things but not good at a life-and-death situation. It's a system that is sometimes right, sometimes creative, often totally wrong — you actually don't want that to drive your car.",
        "aussage_kurz": "In Davos warnt Altman, dass KI fuer Lebensentscheidungen ungeeignet ist, weil sie oft voellig falsch liegt.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.cnn.com/2024/01/18/tech/davos-sam-altman-ai/index.html",
        "quell_titel": "Davos: AI shouldn't make life-or-death decisions, says OpenAI's Sam Altman (CNN)",
        "datum_aussage": "2024-01-18",
        "sprache": "en",
        "kontext": "World Economic Forum in Davos 2024. Altman aeussert sich ueber die Grenzen aktueller KI-Systeme.",
        "aussage_uebersetzung_de": "KI ist in manchen Dingen gut, aber nicht gut in Lebenssituationen. Es ist ein System, das manchmal richtig liegt, manchmal kreativ ist, oft voellig falsch -- man will nicht, dass es das eigene Auto faehrt.",
    },
    # ---- 22. All-In Podcast, Mai 2024 (Universal Basic Compute) ----
    {
        "aussage_text": "I wonder if the future looks something more like universal basic compute than universal basic income and everybody gets a slice of GPT-7's compute and they can use it, they can resell it, they can donate it to somebody to use for cancer research.",
        "aussage_kurz": "Altman schlaegt 'Universal Basic Compute' statt UBI vor: Jeder erhaelt einen Anteil an GPT-7-Rechenleistung.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.techspot.com/news/102975-sam-altman-envisions-future-where-universal-basic-income.html",
        "quell_titel": "Sam Altman envisions a future where universal basic income is a 'slice of GPT' (TechSpot / All-In Podcast)",
        "datum_aussage": "2024-05-12",
        "sprache": "en",
        "kontext": "Interview im All-In Podcast. Altman formuliert erstmals sein Konzept von 'Universal Basic Compute' als Alternative zu UBI.",
        "aussage_uebersetzung_de": "Ich frage mich, ob die Zukunft eher wie universelle Grundrechenleistung aussieht als wie ein universelles Grundeinkommen, und jeder ein Stueck von GPT-7s Rechenleistung bekommt, das er nutzen, weiterverkaufen oder an jemanden spenden kann, der es fuer Krebsforschung verwendet.",
    },
    # ---- 23. "Three Observations" Blog, Feb 2025 ----
    {
        "aussage_text": "The cost to use a given level of AI falls about 10x every 12 months, and lower prices lead to much more use. Moore's law changed the world at 2x every 18 months; this is unbelievably stronger.",
        "aussage_kurz": "Altman beschreibt ein 'Mooresches Gesetz fuer KI': 10-fache Kostenreduktion pro Jahr, staerker als Moores Gesetz.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blog.samaltman.com/three-observations",
        "quell_titel": "Three Observations (Sam Altman Blog)",
        "datum_aussage": "2025-02-09",
        "sprache": "en",
        "kontext": "Blog-Post 'Three Observations' ueber die oekonomischen Grundgesetze der KI-Entwicklung.",
        "aussage_uebersetzung_de": "Die Kosten fuer die Nutzung einer bestimmten KI-Stufe sinken etwa um das 10-fache alle 12 Monate, und niedrigere Preise fuehren zu viel mehr Nutzung. Moores Gesetz veraenderte die Welt mit 2x alle 18 Monate; dies ist unglaublich staerker.",
    },
    # ---- 24. "Three Observations" Blog (Zugang) ----
    {
        "aussage_text": "Anyone in 2035 should be able to marshall the intellectual capacity equivalent to everyone in 2025; everyone should have access to unlimited genius to direct however they can imagine.",
        "aussage_kurz": "Bis 2035 soll jeder Einzelne ueber die intellektuelle Kapazitaet aller Menschen von 2025 verfuegen koennen.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://blog.samaltman.com/three-observations",
        "quell_titel": "Three Observations (Sam Altman Blog)",
        "datum_aussage": "2025-02-09",
        "sprache": "en",
        "kontext": "Altmans Vision fuer demokratisierten Zugang zu KI-Intelligenz in den naechsten 10 Jahren.",
        "aussage_uebersetzung_de": "Jeder sollte 2035 in der Lage sein, die intellektuelle Kapazitaet zu buendeln, die der aller Menschen von 2025 entspricht; jeder sollte Zugang zu unbegrenztem Genie haben, das er nach Belieben einsetzen kann.",
    },
    # ---- 25. Stargate-Ankuendigung, Weisses Haus, Jan 2025 ----
    {
        "aussage_text": "For AGI to get built here, to create hundreds of thousands of jobs, to create a new industry centered here, we wouldn't be able to do this without you, Mr. President.",
        "aussage_kurz": "Bei der Stargate-Ankuendigung im Weissen Haus dankt Altman Trump fuer die Unterstuetzung beim Aufbau von AGI in den USA.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment",
        "quell_titel": "Stargate: Trump announces a $500 billion AI infrastructure investment in the US (CNN)",
        "datum_aussage": "2025-01-21",
        "sprache": "en",
        "kontext": "Pressekonferenz im Weissen Haus zur Ankuendigung des Stargate-Projekts mit Trump, SoftBank-CEO Son und Oracle-CEO Ellison.",
        "aussage_uebersetzung_de": "Damit AGI hier gebaut werden kann, um Hunderttausende von Arbeitsplaetzen zu schaffen, um eine neue Industrie hier zu zentrieren -- das waere ohne Sie nicht moeglich gewesen, Herr Praesident.",
    },
    # ---- 26. CNBC Squawk Box, August 2025 (AGI-Begriff) ----
    {
        "aussage_text": "I think it's not a super useful term.",
        "aussage_kurz": "Altman erklaert den Begriff 'AGI' fuer nicht besonders nuetzlich -- ein Kurswechsel gegenueber frueheren Aussagen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cnbc.com/2025/08/11/sam-altman-says-agi-is-a-pointless-term-experts-agree.html",
        "quell_titel": "Sam Altman now says AGI, or human-level AI, is 'not a super useful term' (CNBC)",
        "datum_aussage": "2025-08-08",
        "sprache": "en",
        "kontext": "CNBC Squawk Box Interview. Bemerkenswerte Kehrtwende: Anfang 2025 sprach Altman noch davon, AGI bauen zu koennen.",
        "aussage_uebersetzung_de": "Ich denke, es ist kein besonders nuetzlicher Begriff.",
    },
    # ---- 27. 2015 informelle Aeusserung (Y Combinator Aera) ----
    {
        "aussage_text": "AI will probably most likely lead to the end of the world, but in the meantime, there'll be great companies.",
        "aussage_kurz": "Altman sagt 2015, KI werde wohl das Ende der Welt bringen -- aber es werde tolle Firmen geben.",
        "modus": "muendlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://www.tomsguide.com/ai/i-think-ai-will-probably-most-likely-lead-to-the-end-of-the-world-everyone-is-sharing-sam-altmans-doomsday-quote-but-almost-no-one-notices-the-date",
        "quell_titel": "Sam Altman's viral quote is missing key context (Tom's Guide)",
        "datum_aussage": "2015",
        "sprache": "en",
        "kontext": "Informelle Aeusserung waehrend der Y-Combinator-Zeit, ca. 2015. Wird oft ohne Kontext oder Datum geteilt.",
        "aussage_uebersetzung_de": "KI wird hoechstwahrscheinlich zum Ende der Welt fuehren, aber in der Zwischenzeit wird es grossartige Unternehmen geben.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung Loopt ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sam Altman gruendet im Alter von 19 Jahren die standortbasierte Social-Networking-App Loopt als Teil des ersten Y-Combinator-Batches. Er sammelt ueber $30 Mio. Risikokapital ein.",
        "datum_handlung": "2005",
        "betrag_usd": 30000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Sam_Altman",
        "quell_titel": "Sam Altman - Wikipedia",
        "kontext": "Loopt war eine der ersten acht Firmen in Y Combinator. 2012 wurde Loopt von Green Dot fuer $43 Mio. uebernommen.",
    },
    # ---- H2. Y Combinator Praesident ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Sam Altman wird Praesident von Y Combinator und loest Paul Graham ab. Unter seiner Fuehrung foerdert YC ca. 1.900 Startups, darunter Airbnb, DoorDash, Reddit und Twitch.",
        "datum_handlung": "2014-02-21",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2014/02/21/sam-altman-taking-over-as-president-of-y-combinator-replacing-paul-graham-at-the-helm/",
        "quell_titel": "Sam Altman Taking Over As President Of Y Combinator (TechCrunch)",
        "kontext": "Paul Graham und Jessica Livingston waehlen Altman als Nachfolger. Er bleibt bis 2019.",
    },
    # ---- H3. Gruendung OpenAI ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sam Altman, Elon Musk, Ilya Sutskever, Greg Brockman und weitere gruenden OpenAI als Non-Profit-Forschungslabor. Eine Gruppe von Unterstuetzern (u.a. Peter Thiel, Reid Hoffman) sagen $1 Mrd. Foerderung zu. Altman und Musk sind Co-Vorsitzende.",
        "datum_handlung": "2015-12-11",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://www.cnbc.com/2025/12/11/openai-began-decade-ago-as-nonprofit-lab-musk-and-altman-now-rivals.html",
        "quell_titel": "Altman and Musk launched OpenAI as a nonprofit 10 years ago (CNBC)",
        "kontext": "OpenAI wird als gemeinnuetzige Organisation gegruendet mit dem Ziel, KI zum Nutzen der gesamten Menschheit zu entwickeln. Tatsaechlich werden nur ca. $130 Mio. der zugesagten $1 Mrd. eingezahlt.",
    },
    # ---- H4. OpenAI CEO ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Sam Altman wird CEO von OpenAI und verlaesst seine Position als Praesident von Y Combinator, um sich voll auf OpenAI zu konzentrieren.",
        "datum_handlung": "2019-03-08",
        "betrag_usd": None,
        "quell_link": "https://www.axios.com/2019/03/08/sam-altman-y-combinator",
        "quell_titel": "Sam Altman steps down as president of Y Combinator (Axios)",
        "kontext": "Der Wechsel markiert Altmans volle Fokussierung auf KI-Entwicklung. OpenAI wechselt im gleichen Zeitraum zum 'capped-profit'-Modell.",
    },
    # ---- H5. Microsoft-Investition $1 Mrd. ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Microsoft investiert $1 Milliarde in OpenAI und wird exklusiver Cloud-Partner. OpenAI fuehrt eine gewinnbegrenzte Gesellschaftsform (capped-profit) ein.",
        "datum_handlung": "2019-07-22",
        "betrag_usd": 1000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/OpenAI",
        "quell_titel": "OpenAI - Wikipedia",
        "kontext": "Erste grosse Investitionsrunde. Microsoft wird strategischer Partner und exklusiver Cloud-Anbieter fuer OpenAI.",
    },
    # ---- H6. GPT-3 Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI veroeffentlicht GPT-3 mit 175 Milliarden Parametern -- das zu diesem Zeitpunkt groesste Sprachmodell der Welt. Zunaechst Zugang nur per API.",
        "datum_handlung": "2020-06-11",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/OpenAI",
        "quell_titel": "OpenAI - Wikipedia",
        "kontext": "GPT-3 demonstriert beeindruckende Sprachfaehigkeiten und loest grosse oeffentliche Diskussionen ueber KI aus.",
    },
    # ---- H7. ChatGPT Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI veroeffentlicht ChatGPT als kostenlose Forschungsvorschau. Der Chatbot erreicht 1 Million Nutzer in 5 Tagen und 100 Millionen in 2 Monaten -- die am schnellsten wachsende Verbraucheranwendung der Geschichte.",
        "datum_handlung": "2022-11-30",
        "betrag_usd": None,
        "quell_link": "https://x.com/sama/status/1598038815599661056",
        "quell_titel": "Sam Altman on X: 'today we launched ChatGPT'",
        "kontext": "Der Launch von ChatGPT wird weithin als Beginn des generativen KI-Booms betrachtet und veraendert die Wahrnehmung von KI in der Oeffentlichkeit grundlegend.",
    },
    # ---- H8. Microsoft $10 Mrd. Investition ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Microsoft investiert weitere ca. $10 Milliarden in OpenAI (kumulativ nun ca. $13 Mrd.). OpenAI wird auf ca. $86 Milliarden bewertet.",
        "datum_handlung": "2023-01-23",
        "betrag_usd": 10000000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/OpenAI",
        "quell_titel": "OpenAI - Wikipedia",
        "kontext": "Die Investition erfolgt wenige Monate nach dem ChatGPT-Launch und ist zu diesem Zeitpunkt eine der groessten KI-Investitionen der Geschichte.",
    },
    # ---- H9. GPT-4 Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI veroeffentlicht GPT-4, ein multimodales grosses Sprachmodell mit deutlich verbessertem Reasoning. OpenAI wird fuer mangelnde Transparenz kritisiert, da kaum technische Details veroeffentlicht werden.",
        "datum_handlung": "2023-03-14",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/OpenAI",
        "quell_titel": "OpenAI - Wikipedia",
        "kontext": "GPT-4 markiert den Uebergang zu multimodalen Modellen und den zunehmenden Widerspruch zwischen dem Namen 'OpenAI' und der tatsaechlichen Offenheit des Unternehmens.",
    },
    # ---- H10. Worldcoin/World Launch ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Sam Altman launcht Worldcoin (spaeter 'World') mit Tools for Humanity. Das Projekt nutzt Iris-Scanner ('Orb') um eine globale digitale Identitaet (World ID) und Kryptowaehrung bereitzustellen. Ueber 2 Millionen Nutzer verifizieren sich bis zum Launch. $250 Mio. Venture-Capital eingesammelt.",
        "datum_handlung": "2023-07-24",
        "betrag_usd": 250000000.0,
        "quell_link": "https://techcrunch.com/2023/07/24/worldcoin-launch-sam-altman/",
        "quell_titel": "Sam Altman's Worldcoin eyeball-scanning crypto project launches (TechCrunch)",
        "kontext": "Altman verknuepft das Projekt mit seiner KI-Vision: World ID soll in einer Welt mit fortschrittlicher KI Menschen von Bots unterscheidbar machen und UBI ermoeglichen. Das Projekt stoeesst in mehreren Laendern auf Datenschutz-Bedenken.",
    },
    # ---- H11. Entlassung durch den Board ----
    {
        "handlung_typ": "entlassung",
        "beschreibung": "Der OpenAI-Vorstand entlaesst Sam Altman als CEO mit der Begruendung, er sei 'nicht durchgaengig aufrichtig' in seiner Kommunikation mit dem Board gewesen. Greg Brockman kuendigt ebenfalls. Microsoft wird erst eine Minute vor der Oeffentlichkeit informiert.",
        "datum_handlung": "2023-11-17",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI",
        "quell_titel": "Removal of Sam Altman from OpenAI - Wikipedia",
        "kontext": "Die ueberraschende Entlassung loest eine der dramatischsten Krisen in der Tech-Geschichte aus. Ilya Sutskever und weitere Board-Mitglieder stehen hinter der Entscheidung.",
    },
    # ---- H12. Rueckkehr als CEO ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Nach 4 Tagen intensiver Verhandlungen kehrt Sam Altman als CEO zurueck. Ueber 700 von 770 OpenAI-Mitarbeitern hatten mit Kuendigung gedroht. Ilya Sutskever bedauert seine Rolle oeffentlich. Ein neuer Board unter Bret Taylor wird installiert. Microsoft erhaelt einen Beobachtersitz.",
        "datum_handlung": "2023-11-21",
        "betrag_usd": None,
        "quell_link": "https://www.axios.com/2023/11/22/openai-microsoft-sam-altman-ceo-chaos-timeline",
        "quell_titel": "OpenAI chaos: A timeline of Sam Altman's firing and return (Axios)",
        "kontext": "Die Rueckkehr wird als Sieg Altmans und der Investoren ueber den Non-Profit-Board gewertet. Das Kraeftegleichgewicht verschiebt sich zugunsten kommerzieller Interessen.",
    },
    # ---- H13. GPT-4o Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI stellt GPT-4o vor, ein schnelleres und guenstigeres Modell als GPT-4 mit verbesserten multimodalen Faehigkeiten (Text, Audio, Bild). Kostenlos verfuegbar fuer alle Nutzer.",
        "datum_handlung": "2024-05-13",
        "betrag_usd": None,
        "quell_link": "https://fortune.com/2024/05/13/openai-ai-model-gpt-4o-sam-altman/",
        "quell_titel": "OpenAI debuts a speedier model for powering ChatGPT (Fortune)",
        "kontext": "GPT-4o senkt die Token-Kosten drastisch und macht fortschrittliche KI fuer Millionen mehr Nutzer zugaenglich.",
    },
    # ---- H14. OpenAI o1 Launch (Reasoning) ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "OpenAI veroeffentlicht o1 (intern 'Strawberry'), ein Reasoning-Modell, das vor der Antwort plant und mehrere Loesungswege durchgeht. Bei der Internationalen Mathematik-Olympiade loest es 83% der Aufgaben (GPT-4o: 13%).",
        "datum_handlung": "2024-09-12",
        "betrag_usd": None,
        "quell_link": "https://openai.com/index/introducing-openai-o1-preview/",
        "quell_titel": "Introducing OpenAI o1 (OpenAI)",
        "kontext": "Altman bezeichnet o1 als Paradigmenwechsel: von reiner Sprachgenerierung zu echtem Reasoning. Er vergleicht die aktuelle Phase mit der GPT-2-Aera.",
    },
    # ---- H15. $6,6 Mrd. Funding-Runde ----
    {
        "handlung_typ": "investition",
        "beschreibung": "OpenAI schliesst eine $6,6 Milliarden Finanzierungsrunde ab (gefuehrt von Thrive Capital mit $1,3 Mrd.). Bewertung: $157 Milliarden. Investoren: Microsoft ($750 Mio.), SoftBank ($500 Mio.), Nvidia ($100 Mio.) u.a. Bedingung: For-Profit-Umbau innerhalb von 2 Jahren.",
        "datum_handlung": "2024-10-02",
        "betrag_usd": 6600000000.0,
        "quell_link": "https://www.washingtonpost.com/technology/2024/10/02/openai-funding-157-billion/",
        "quell_titel": "OpenAI gets $6.6 billion in new funding, valuing company at $157 billion (Washington Post)",
        "kontext": "Eine der groessten Startup-Finanzierungen aller Zeiten. OpenAI rangiert hinter ByteDance ($225 Mrd.) und SpaceX ($200 Mrd.).",
    },
    # ---- H16. Politische Spende: Trump Inauguration ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Sam Altman spendet persoenlich $1 Million an Trumps Inaugurations-Fonds. Zuvor hatte er 2023 $200.000 an Biden gespendet und Trump 2016 mit Hitler verglichen.",
        "datum_handlung": "2024-12-13",
        "betrag_usd": 1000000.0,
        "quell_link": "https://www.npr.org/2024/12/13/nx-s1-5227874/trump-bezos-zuckerberg-amazon-facebook-open-ai-meta-inauguration-fund",
        "quell_titel": "Tech moguls Altman, Bezos and Zuckerberg donate to Trump's inauguration fund (NPR)",
        "kontext": "Die Spende markiert eine bemerkenswerte politische Kehrtwende und wird im Kontext der Stargate-Partnerschaft mit der Trump-Regierung gesehen.",
    },
    # ---- H17. Stargate-Projekt ----
    {
        "handlung_typ": "investition",
        "beschreibung": "OpenAI, SoftBank, Oracle und MGX kuendigen gemeinsam mit Praesident Trump das Stargate-Projekt an: bis zu $500 Milliarden Investition in KI-Infrastruktur (Rechenzentren) in den USA. OpenAI hat operative Verantwortung, SoftBank die finanzielle. Geplant: 100.000 neue Jobs.",
        "datum_handlung": "2025-01-21",
        "betrag_usd": 500000000000.0,
        "quell_link": "https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment",
        "quell_titel": "Stargate: Trump announces a $500 billion AI infrastructure investment (CNN)",
        "kontext": "Die Ankuendigung findet am zweiten Tag der Trump-Praesidentschaft im Weissen Haus statt. Elon Musk kritisiert das Projekt oeffentlich und bezweifelt, dass die Mittel tatsaechlich vorhanden sind.",
    },
    # ---- H18. $40 Mrd. SoftBank-Runde ----
    {
        "handlung_typ": "investition",
        "beschreibung": "OpenAI schliesst eine $40 Milliarden Finanzierungsrunde ab, die groesste private Tech-Finanzierung aller Zeiten. SoftBank fuehrt mit $30 Mrd. Bewertung: $300 Milliarden. Weitere Investoren: Microsoft, Coatue, Altimeter, Thrive.",
        "datum_handlung": "2025-03-31",
        "betrag_usd": 40000000000.0,
        "quell_link": "https://www.cnbc.com/2025/03/31/openai-closes-40-billion-in-funding-the-largest-private-fundraise-in-history-softbank-chatgpt.html",
        "quell_titel": "OpenAI closes $40 billion funding round, largest private tech deal on record (CNBC)",
        "kontext": "Die Runde ist an die Bedingung geknuepft, dass OpenAI in eine For-Profit-Struktur umgewandelt wird. SoftBank erhaelt ca. 11% Anteil.",
    },
    # ---- H19. OpenAI For-Profit-Umwandlung (PBC) ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Nach fast einem Jahr Verhandlungen schliesst OpenAI den Umbau zu einer Public Benefit Corporation (PBC) ab. Die gemeinnuetzige OpenAI Foundation erhaelt 26% ($130 Mrd. Anteil), Microsoft 27%, Mitarbeiter/andere Investoren 47%. Gewinndeckelungen entfallen.",
        "datum_handlung": "2025-10-29",
        "betrag_usd": None,
        "quell_link": "https://www.bloomberg.com/news/articles/2025-10-29/openai-restructure-paves-way-for-ipo-and-ai-spending-spree",
        "quell_titel": "OpenAI Restructure Paves Way for IPO and AI Spending Spree (Bloomberg)",
        "kontext": "Urspruenglich sollte OpenAI komplett for-profit werden. Der Kompromiss bewahrt die Foundation, entfernt aber die Gewinndeckelung. Der Generalstaatsanwalt von Kalifornien sichert Sicherheitsauflagen und ein Veto-Recht der Foundation bei neuen Modellen.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=2 existiert
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
            "Claude (collect_altman.py)"
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
        "Sam Altman quotes, interviews, Congressional testimony, blog posts, Twitter, Lex Fridman, Davos, Stargate, Worldcoin, OpenAI",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Blog-Posts (moores.samaltman.com, ia.samaltman.com, blog.samaltman.com), "
        f"Lex Fridman Podcasts #367 und #419, ABC News Interview, US Senate Testimony May 2023, "
        f"StrictlyVC/TechCrunch Interview, Davos/WEF 2024, All-In Podcast, CNBC Squawk Box, "
        f"Twitter/X (@sama), CNN, CNBC, Washington Post, Bloomberg, NPR, TechCrunch, Fortune, Axios.",
        "Claude (collect_altman.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Sam Altman (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Sam Altman")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_altman.py")
    print("  Verifizierte Aussagen & Handlungen: Sam Altman")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
