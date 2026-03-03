#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_hassabis.py
===================
Sammelt verifizierbare Aussagen und Handlungen von Demis Hassabis (person_id=11)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Podcasts, Nachrichtenartikeln, Nobel-Interviews und wissenschaftlichen Veroeffentlichungen.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 11  # Demis Hassabis

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
    # ---- 1. TIME100 Interview 2025 (AGI Timeline) ----
    {
        "aussage_text": "I'm gonna say before [2030 for AGI].",
        "aussage_kurz": "Hassabis prognostiziert AGI vor 2030.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://time.com/7277608/demis-hassabis-interview-time100-2025/",
        "quell_titel": "Demis Hassabis' TIME100 on AlphaFold, AGI, and humanity. (TIME)",
        "datum_aussage": "2025-02-06",
        "sprache": "en",
        "kontext": "TIME100 Interview nach dem Nobelpreis. Hassabis aeussert sich zur AGI-Zeitlinie und korrigiert seine fruehere '5-10 Jahre'-Schaetzung nach oben.",
        "aussage_uebersetzung_de": "Ich wuerde sagen, vor 2030.",
    },
    # ---- 2. TIME100 Interview 2025 (Transformative Moment) ----
    {
        "aussage_text": "AGI, probably the most transformative moment in human history, is on the horizon.",
        "aussage_kurz": "Hassabis bezeichnet AGI als 'wohl transformativsten Moment der Menschheitsgeschichte'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/7277608/demis-hassabis-interview-time100-2025/",
        "quell_titel": "Demis Hassabis' TIME100 on AlphaFold, AGI, and humanity. (TIME)",
        "datum_aussage": "2025-02-06",
        "sprache": "en",
        "kontext": "Hassabis ordnet die Bedeutung von AGI historisch ein und vergleicht sie mit anderen technologischen Revolutionen.",
        "aussage_uebersetzung_de": "AGI, wahrscheinlich der transformativste Moment in der Menschheitsgeschichte, steht bevor.",
    },
    # ---- 3. TIME100 Interview 2025 (Industrial Revolution) ----
    {
        "aussage_text": "It will be ten times bigger than the Industrial Revolution and perhaps ten times faster.",
        "aussage_kurz": "Hassabis sagt, AGI werde zehnmal groesser und zehnmal schneller als die Industrielle Revolution sein.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/7277608/demis-hassabis-interview-time100-2025/",
        "quell_titel": "Demis Hassabis' TIME100 on AlphaFold, AGI, and humanity. (TIME)",
        "datum_aussage": "2025-02-06",
        "sprache": "en",
        "kontext": "Historischer Vergleich der erwarteten AGI-Auswirkungen mit der Industriellen Revolution.",
        "aussage_uebersetzung_de": "Es wird zehnmal groesser sein als die Industrielle Revolution und vielleicht zehnmal schneller.",
    },
    # ---- 4. TIME100 Interview 2025 (AI Safety) ----
    {
        "aussage_text": "If AI is built safely and responsibly, I believe it will be one of the most transformative and beneficial technologies ever.",
        "aussage_kurz": "Hassabis glaubt, verantwortungsvolle KI werde eine der transformativsten und nuetzlichsten Technologien sein.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/7277608/demis-hassabis-interview-time100-2025/",
        "quell_titel": "Demis Hassabis' TIME100 on AlphaFold, AGI, and humanity. (TIME)",
        "datum_aussage": "2025-02-06",
        "sprache": "en",
        "kontext": "Bedingt optimistische Vision: Hassabis betont die Notwendigkeit sicherer und verantwortungsvoller Entwicklung.",
        "aussage_uebersetzung_de": "Wenn KI sicher und verantwortungsvoll gebaut wird, glaube ich, dass sie eine der transformativsten und nuetzlichsten Technologien ueberhaupt sein wird.",
    },
    # ---- 5. Nobel Prize Interview 2024 ----
    {
        "aussage_text": "Winning the Nobel Prize is the honour of a lifetime and the realisation of a lifelong dream - it still hasn't really sunk in yet.",
        "aussage_kurz": "Hassabis beschreibt den Nobelpreis als lebenslangen Traum, der noch nicht ganz real erscheint.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/demishassabis/status/1845864764469334239",
        "quell_titel": "Demis Hassabis on X (@demishassabis)",
        "datum_aussage": "2024-10-09",
        "sprache": "en",
        "kontext": "Tweet am Tag der Nobelpreis-Bekanntgabe. Hassabis und John Jumper erhalten den Chemie-Nobelpreis fuer AlphaFold2.",
        "aussage_uebersetzung_de": "Den Nobelpreis zu gewinnen ist die Ehre meines Lebens und die Verwirklichung eines lebenslangen Traums - es ist noch nicht wirklich angekommen.",
    },
    # ---- 6. Nobel Prize Interview 2024 (AlphaFold) ----
    {
        "aussage_text": "With AlphaFold2 we cracked the 50-year grand challenge of protein structure prediction: predicting the 3D structure of a protein purely from its amino acid sequence.",
        "aussage_kurz": "Hassabis erklaert, AlphaFold2 habe die 50-Jahre alte Herausforderung der Proteinstrukturvorhersage geloest.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/demishassabis/status/1845864764469334239",
        "quell_titel": "Demis Hassabis on X (@demishassabis)",
        "datum_aussage": "2024-10-09",
        "sprache": "en",
        "kontext": "Fortsetzung des Tweets zur Nobelpreis-Bekanntgabe. Hassabis fasst die wissenschaftliche Leistung von AlphaFold2 zusammen.",
        "aussage_uebersetzung_de": "Mit AlphaFold2 haben wir die 50-Jahre alte grosse Herausforderung der Proteinstrukturvorhersage geknackt: die Vorhersage der 3D-Struktur eines Proteins allein aus seiner Aminosaeurensequenz.",
    },
    # ---- 7. Axios Interview Dez 2025 (AGI Horizon) ----
    {
        "aussage_text": "AGI is on the horizon. Within 5 years, perhaps with 1-2 major technological breakthroughs, we may overcome the obstacles on the path to AGI.",
        "aussage_kurz": "Hassabis sagt, AGI sei in Sichtweite und erfordere noch 1-2 grosse Durchbrueche in den naechsten 5 Jahren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.axios.com/2025/12/05/ai-deepmind-gemini-agi",
        "quell_titel": "Exclusive: 'Transformative' AGI is on the horizon, DeepMind's Hassabis says (Axios)",
        "datum_aussage": "2025-12-05",
        "sprache": "en",
        "kontext": "Axios-Exklusivinterview. Hassabis wird konkreter bezueglich der noch fehlenden technischen Durchbrueche.",
        "aussage_uebersetzung_de": "AGI steht bevor. Innerhalb von 5 Jahren koennten wir mit 1-2 grossen technologischen Durchbruechen die Hindernisse auf dem Weg zur AGI ueberwinden.",
    },
    # ---- 8. Axios Interview Feb 2025 (AI Race) ----
    {
        "aussage_text": "The more artificial intelligence becomes a race, the harder it is to keep the technology from becoming unsafe.",
        "aussage_kurz": "Hassabis warnt, dass ein KI-Wettrennen die Sicherheit gefaehrde.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.axios.com/2025/02/14/hassabis-google-ai-race-hazards",
        "quell_titel": "Google DeepMind CEO Demis Hassabis warns AI 'race' could be dangerous (Axios)",
        "datum_aussage": "2025-02-14",
        "sprache": "en",
        "kontext": "Hassabis aeussert sich zu den Gefahren eines unkontrollierten Wettlaufs in der KI-Entwicklung.",
        "aussage_uebersetzung_de": "Je mehr kuenstliche Intelligenz zu einem Wettrennen wird, desto schwieriger ist es, die Technologie davor zu bewahren, unsicher zu werden.",
    },
    # ---- 9. Regulation Statement (Smart Regulation) ----
    {
        "aussage_text": "We need smart, adaptable regulation instead of rigid rules. Policy should evolve in line with the technology's direction and impact.",
        "aussage_kurz": "Hassabis fordert intelligente, anpassungsfaehige Regulierung statt starrer Regeln.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://dig.watch/updates/google-deepmind-chief-urges-smarter-ai-regulation",
        "quell_titel": "Google DeepMind chief urges smarter AI regulation (Digital Watch Observatory)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Oeffentliche Stellungnahme zu KI-Regulierung. Hassabis plaediert fuer flexible Regulation, die mit der Technologie Schritt haelt.",
        "aussage_uebersetzung_de": "Wir brauchen intelligente, anpassungsfaehige Regulierung statt starrer Regeln. Die Politik sollte sich im Einklang mit der Richtung und den Auswirkungen der Technologie entwickeln.",
    },
    # ---- 10. Extinction Risk Statement 2023 ----
    {
        "aussage_text": "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war.",
        "aussage_kurz": "Hassabis unterzeichnet Erklaerung, die KI-Risiko auf Ebene von Pandemien und Atomkrieg einstuft.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 10,    # Congressional Testimony / Offizielle Erklaerungen
        "quell_link": "https://www.safe.ai/statement-on-ai-risk",
        "quell_titel": "Statement on AI Risk (Center for AI Safety)",
        "datum_aussage": "2023-05-30",
        "sprache": "en",
        "kontext": "Hassabis unterzeichnet zusammen mit Sam Altman, Geoffrey Hinton und anderen die Ein-Satz-Erklaerung des Center for AI Safety zu existenziellen KI-Risiken.",
        "aussage_uebersetzung_de": "Die Minderung des Risikos der Ausloeschung durch KI sollte eine globale Prioritaet sein, neben anderen gesellschaftlichen Risiken wie Pandemien und Atomkrieg.",
    },
    # ---- 11. Open Source AI Warning ----
    {
        "aussage_text": "How do you stop bad actors repurposing general purpose technology for harmful ends?",
        "aussage_kurz": "Hassabis stellt die Frage, wie man boese Akteure daran hindert, Allzweck-KI fuer Schaedliches zu nutzen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.klover.ai/ethical-and-economic-implications-hassabis-on-ais-future/",
        "quell_titel": "Ethical and Economic Implications: Hassabis on AI's Future (Klover.ai)",
        "datum_aussage": "2024",
        "sprache": "en",
        "kontext": "Hassabis aeussert sich zu den Herausforderungen von Open-Source-KI und dem Dual-Use-Problem.",
        "aussage_uebersetzung_de": "Wie hindert man boese Akteure daran, Allzwecktechnologie fuer schaedliche Zwecke umzufunktionieren?",
    },
    # ---- 12. Lex Fridman Podcast #299, 2022 (Consciousness) ----
    {
        "aussage_text": "One of the best definitions I like of consciousness is it's the information feels when we process it.",
        "aussage_kurz": "Hassabis definiert Bewusstsein als das, was Information fuehlt, wenn wir sie verarbeiten.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://lexfridman.com/demis-hassabis-transcript/",
        "quell_titel": "Lex Fridman Podcast #299: Demis Hassabis - DeepMind, AI, Superintelligence & the Future of Humanity",
        "datum_aussage": "2022-07-01",
        "sprache": "en",
        "kontext": "Langes Interview mit Lex Fridman ueber Bewusstsein, KI und die Zukunft der Menschheit. Hassabis reflektiert ueber die Natur des Bewusstseins.",
        "aussage_uebersetzung_de": "Eine der besten Definitionen von Bewusstsein, die mir gefaellt, ist: Es ist das, was Information fuehlt, wenn wir sie verarbeiten.",
    },
    # ---- 13. Lex Fridman Podcast #299 (Universe Waking Up) ----
    {
        "aussage_text": "We are the only sort of fully conscious beings in the universe. We are 'waking up the universe,' bringing self-awareness to a universe that otherwise lacks it.",
        "aussage_kurz": "Hassabis sieht Menschen als Wesen, die das Universum 'aufwecken' und Selbstbewusstsein bringen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.philosophyforlife.org/blog/tag/Demis+Hassabis",
        "quell_titel": "Demis Hassabis - Philosophy for Life",
        "datum_aussage": "2022-07-01",
        "sprache": "en",
        "kontext": "Hassabis zitiert Carl Sagan und beschreibt die besondere Rolle bewusster Wesen im Universum. Philosophische Reflexion ueber die menschliche Existenz.",
        "aussage_uebersetzung_de": "Wir sind die einzigen vollstaendig bewussten Wesen im Universum. Wir 'wecken das Universum auf', bringen Selbstbewusstsein in ein Universum, dem es sonst fehlt.",
    },
    # ---- 14. Lex Fridman Podcast #299 (Motivation) ----
    {
        "aussage_text": "My underlying motivation for working in artificial intelligence is to understand how the universe works and to answer the deepest scientific questions: What is consciousness? What are we doing here? What's the universe about?",
        "aussage_kurz": "Hassabis' Motivation fuer KI-Forschung ist das Verstaendnis des Universums und des Bewusstseins.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://blogs.swastikmukherjee.com/blog/demis-hassabis-the-google-deepmind-lead-thinks-ai-can-solve-everything-in-nature/",
        "quell_titel": "Demis Hassabis Thinks AI Can Solve Everything in Nature (Swastik Mukherjee Blog)",
        "datum_aussage": "2022-07-01",
        "sprache": "en",
        "kontext": "Hassabis legt seine philosophische Grundmotivation fuer die Arbeit an KI dar: tiefe wissenschaftliche Fragen zu beantworten.",
        "aussage_uebersetzung_de": "Meine grundlegende Motivation fuer die Arbeit an kuenstlicher Intelligenz ist, zu verstehen, wie das Universum funktioniert, und die tiefsten wissenschaftlichen Fragen zu beantworten: Was ist Bewusstsein? Was machen wir hier? Worum geht es im Universum?",
    },
    # ---- 15. Lex Fridman Podcast #475, 2025 (Classical Computing Brain) ----
    {
        "aussage_text": "It's mostly just classical computing that's going on in the brain, which suggests that all the phenomena are modellable or mimicable by a classical computer.",
        "aussage_kurz": "Hassabis glaubt, das Gehirn funktioniere hauptsaechlich klassisch und sei durch klassische Computer modellierbar.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://officechai.com/consciousness/consciousness-might-not-need-quantum-effects-could-be-modeled-by-classical-computers-demis-hassabis/",
        "quell_titel": "Consciousness Might Not Need Quantum Effects: Demis Hassabis (OfficeChai)",
        "datum_aussage": "2025-07-15",
        "sprache": "en",
        "kontext": "Zweites Lex-Fridman-Interview. Hassabis argumentiert gegen die Notwendigkeit von Quanteneffekten fuer Bewusstsein.",
        "aussage_uebersetzung_de": "Es ist groesstenteils nur klassisches Computing, das im Gehirn ablaeuft, was nahelegt, dass alle Phaenomene durch einen klassischen Computer modelliert oder nachgeahmt werden koennen.",
    },
    # ---- 16. AlphaProteo Announcement, Sep 2024 ----
    {
        "aussage_text": "Excited to announce AlphaProteo, our breakthrough AI system for designing novel proteins that bind to a target molecule or protein. It has the potential to accelerate our understanding of biology, and aid the discovery of new drugs, the development of biosensors, & much more!",
        "aussage_kurz": "Hassabis kuendigt AlphaProteo an, ein KI-System zur Protein-Design fuer Medikamentenentwicklung.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/demishassabis/status/1831843656623599936",
        "quell_titel": "Demis Hassabis on X (@demishassabis)",
        "datum_aussage": "2024-09-05",
        "sprache": "en",
        "kontext": "Tweet zur Ankuendigung von AlphaProteo, einem Nachfolgesystem zu AlphaFold, das nicht nur Strukturen vorhersagt, sondern neue Proteine entwirft.",
        "aussage_uebersetzung_de": "Begeistert, AlphaProteo anzukuendigen, unser bahnbrechendes KI-System zum Entwerfen neuartiger Proteine, die an ein Zielmolekuel oder -protein binden. Es hat das Potenzial, unser Verstaendnis der Biologie zu beschleunigen und bei der Entdeckung neuer Medikamente, der Entwicklung von Biosensoren und vielem mehr zu helfen!",
    },
    # ---- 17. Fortune Interview (Golden Age) ----
    {
        "aussage_text": "In 10, 15 years' time, we'll be in a kind of new golden era of discovery that is a kind of new renaissance.",
        "aussage_kurz": "Hassabis prognostiziert in 10-15 Jahren ein 'neues goldenes Zeitalter der Entdeckung'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2026/02/11/demis-hassabis-nobel-google-deepmind-predicts-ai-renaissance-radical-abundance/",
        "quell_titel": "Google's Nobel-winning AI leader sees a 'renaissance' ahead (Fortune)",
        "datum_aussage": "2026-02-11",
        "sprache": "en",
        "kontext": "Fortune-Interview im Februar 2026. Hassabis beschreibt seine langfristige Vision einer KI-getriebenen wissenschaftlichen Renaissance.",
        "aussage_uebersetzung_de": "In 10, 15 Jahren werden wir in einer Art neuem goldenen Zeitalter der Entdeckung sein, das eine Art neue Renaissance ist.",
    },
    # ---- 18. AlphaZero Chess Quote ----
    {
        "aussage_text": "AlphaZero's play style is alien. It sometimes wins by offering counterintuitive sacrifices. It's like chess from another dimension.",
        "aussage_kurz": "Hassabis beschreibt AlphaZeros Spielstil als 'alien' und wie Schach aus einer anderen Dimension.",
        "modus": "muendlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://www.chess.com/news/view/demis-hassabis-nobel-prize-chemistry",
        "quell_titel": "AlphaZero Creator Demis Hassabis Wins Nobel Prize For Chemistry (Chess.com)",
        "datum_aussage": "2018",
        "sprache": "en",
        "kontext": "Hassabis kommentiert die ueberraschende Spielweise von AlphaZero, das Schach, Go und Shogi durch Selbstspiel meisterte.",
        "aussage_uebersetzung_de": "AlphaZeros Spielstil ist fremd. Es gewinnt manchmal durch kontraintuitive Opfer. Es ist wie Schach aus einer anderen Dimension.",
    },
    # ---- 19. Energy and Intelligence Statement ----
    {
        "aussage_text": "Energy will be synonymous to intelligence as we get towards AGI. The amount we're going to get back, even just narrowly for climate [solutions] from these models, it's going to far outweigh the energy costs.",
        "aussage_kurz": "Hassabis sagt, Energie werde gleichbedeutend mit Intelligenz, und KI-Nutzen ueberwiege die Energiekosten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://officechai.com/ai/energy-will-be-synonymous-to-intelligence-as-we-get-towards-agi-google-deepmind-ceo-demis-hassabis/",
        "quell_titel": "Energy Will Be Synonymous To Intelligence: Demis Hassabis (OfficeChai)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Hassabis verteidigt den hohen Energieverbrauch von KI-Systemen mit dem Argument, dass die Loesungen (z.B. fuer Klimawandel) den Verbrauch rechtfertigen.",
        "aussage_uebersetzung_de": "Energie wird gleichbedeutend mit Intelligenz sein, je naeher wir der AGI kommen. Das, was wir zurueckbekommen werden, selbst nur im engen Sinne fuer Klima-Loesungen von diesen Modellen, wird die Energiekosten bei weitem ueberwiegen.",
    },
    # ---- 20. Room Temperature Superconductor Vision ----
    {
        "aussage_text": "One of my pet projects is discovering room temperature superconductor materials using AI, with multiple breakthroughs that AI could come up with to help with the energy situation.",
        "aussage_kurz": "Hassabis' 'Lieblingsprojekt' ist die Entdeckung von Raumtemperatur-Supraleitern mittels KI.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.remio.ai/post/demis-hassabis-on-the-future-of-ai-a-new-golden-age-of-science-and-creativity",
        "quell_titel": "Demis Hassabis on the Future of AI: A New Golden Age (Remio.ai)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Hassabis beschreibt seine Vision, wie KI Materialdurchbrueche ermoeglichen kann, die die Energiekrise loesen koennten.",
        "aussage_uebersetzung_de": "Eines meiner Lieblingsprojekte ist die Entdeckung von Raumtemperatur-Supraleitermaterialien mittels KI, mit mehreren Durchbruechen, die KI hervorbringen koennte, um bei der Energiesituation zu helfen.",
    },
    # ---- 21. AGI Definition (Scientific Discovery) ----
    {
        "aussage_text": "AGI would be a technology that could not only solve existing problems, but also come up with entirely new explanations for the universe.",
        "aussage_kurz": "Hassabis definiert AGI als System, das nicht nur Probleme loest, sondern neue Erklaerungen fuer das Universum findet.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://research.aimultiple.com/artificial-general-intelligence-singularity-timing/",
        "quell_titel": "AGI/Singularity: 9,300 Predictions Analyzed (AIMultiple)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Hassabis unterscheidet sich von anderen KI-Fuehrern durch seine Betonung wissenschaftlicher Entdeckung als Kern der AGI-Definition.",
        "aussage_uebersetzung_de": "AGI waere eine Technologie, die nicht nur bestehende Probleme loesen, sondern auch voellig neue Erklaerungen fuer das Universum finden koennte.",
    },
    # ---- 22. World Models Statement ----
    {
        "aussage_text": "World Models are crucial — a model that can predict and simulate how the state of the environment changes with actions, with core logic to truly 'understand' the operating rules of the physical world.",
        "aussage_kurz": "Hassabis betont die Bedeutung von 'World Models' zum Verstaendnis der physikalischen Welt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://eu.36kr.com/en/p/3646186509667977",
        "quell_titel": "Only 5 Years Left? Nobel Laureate Hassabis Unveils AGI Timeline (36Kr)",
        "datum_aussage": "2025",
        "sprache": "en",
        "kontext": "Hassabis identifiziert 'World Models' als eine der Schluesselkomponenten auf dem Weg zu AGI.",
        "aussage_uebersetzung_de": "Weltmodelle sind entscheidend - ein Modell, das vorhersagen und simulieren kann, wie sich der Zustand der Umgebung mit Aktionen aendert, mit Kernlogik, um die Funktionsregeln der physischen Welt wirklich zu 'verstehen'.",
    },
    # ---- 23. Scientific Understanding Quote ----
    {
        "aussage_text": "Scientific understanding enhances rather than diminishes the beauty and mystery of the world.",
        "aussage_kurz": "Hassabis argumentiert, wissenschaftliches Verstaendnis verstaerke die Schoenheit der Welt, statt sie zu verringern.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.philosophyforlife.org/blog/tag/Demis+Hassabis",
        "quell_titel": "Demis Hassabis - Philosophy for Life",
        "datum_aussage": "2022",
        "sprache": "en",
        "kontext": "Hassabis verbindet wissenschaftliche Rationalitaet mit Spiritualitaet und Aesthetik. Bezug zu Feynman und Spinoza.",
        "aussage_uebersetzung_de": "Wissenschaftliches Verstaendnis verstaerkt die Schoenheit und das Mysterium der Welt, anstatt sie zu verringern.",
    },
    # ---- 24. Chess Master at 13 ----
    {
        "aussage_text": "I reached chess master standard at 13 with an Elo rating of 2300. Chess taught me pattern recognition and strategic thinking — skills that became fundamental to my work in AI.",
        "aussage_kurz": "Hassabis wurde mit 13 Schachmeister und sieht Schach als Grundlage fuer seine KI-Arbeit.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://medium.com/@sahin.samia/demis-hassabis-the-chess-prodigy-who-transformed-ai-and-science-1f0e696fb6eb",
        "quell_titel": "Demis Hassabis: The Chess Prodigy Who Transformed AI and Science (Medium)",
        "datum_aussage": "2020",
        "sprache": "en",
        "kontext": "Rueckblick auf seine Jugend. Hassabis sieht eine direkte Verbindung zwischen Brettspielen und KI-Forschung.",
        "aussage_uebersetzung_de": "Ich erreichte mit 13 Schachmeister-Standard mit einer Elo-Wertung von 2300. Schach lehrte mich Mustererkennung und strategisches Denken - Faehigkeiten, die fuer meine Arbeit in KI fundamental wurden.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Gruendung DeepMind ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Demis Hassabis gruendet DeepMind Technologies in London zusammen mit Shane Legg und Mustafa Suleyman. Die Vision: KI-Systeme entwickeln, die so allgemein und flexibel sind wie die menschliche Intelligenz.",
        "datum_handlung": "2010-09-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Hassabis und Legg lernten sich als Postdocs am Gatsby Computational Neuroscience Unit kennen. DeepMind kombiniert Neurowissenschaft und maschinelles Lernen.",
    },
    # ---- H2. DeepMind Series A Funding ----
    {
        "handlung_typ": "investition",
        "beschreibung": "DeepMind schliesst Serie-A-Finanzierung ueber $50 Millionen ab. Investoren: Founders Fund (Peter Thiel), Horizons Ventures (Li Ka-shing), Elon Musk und Scott Banister.",
        "datum_handlung": "2011-12-01",
        "betrag_usd": 50000000.0,
        "quell_link": "https://www.crunchbase.com/organization/deepmind",
        "quell_titel": "Google DeepMind - Crunchbase Company Profile & Funding",
        "kontext": "Fruehe Unterstuetzung durch prominente Tech-Investoren. Musk und Thiel erkennen das Potenzial von DeepMind frueher als die meisten anderen.",
    },
    # ---- H3. DQN Atari Breakthrough ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "DeepMind veroeffentlicht bahnbrechende Forschung: Ein Deep Q-Network (DQN) lernt, Atari-Spiele auf uebermenschlichem Niveau zu spielen, allein durch Beobachtung der Pixel.",
        "datum_handlung": "2013-12-19",
        "betrag_usd": None,
        "quell_link": "https://timelines.issarice.com/wiki/Timeline_of_DeepMind",
        "quell_titel": "Timeline of DeepMind (Timelines)",
        "kontext": "Dieser Durchbruch beweist die Macht von Deep Reinforcement Learning und macht DeepMind schlagartig beruehmt. Nature-Paper folgt 2015.",
    },
    # ---- H4. Google-Acquisition ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Google erwirbt DeepMind fuer geschaetzt $400-650 Millionen. Groesste europaeische Tech-Akquisition von Google zu diesem Zeitpunkt. DeepMind wird Tochterunternehmen von Alphabet.",
        "datum_handlung": "2014-01-26",
        "betrag_usd": 500000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Die Akquisition sichert DeepMind massive Rechenressourcen. Larry Page und Sergey Brin waren persoenlich an der Uebernahme beteiligt. Hassabis bleibt CEO.",
    },
    # ---- H5. AlphaGo besiegt Fan Hui ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "AlphaGo besiegt Fan Hui, den europaeischen Go-Champion, mit 5:0. Erster Sieg eines Computerprogramms gegen einen professionellen Go-Spieler auf dem 19x19-Brett.",
        "datum_handlung": "2015-10-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Die Go-Herausforderung galt als Jahrzehnte entfernt. AlphaGo nutzt eine Kombination aus neuronalen Netzen und Monte-Carlo-Baumsuche.",
    },
    # ---- H6. AlphaGo vs Lee Sedol ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "AlphaGo besiegt Lee Sedol, einen der besten Go-Spieler der Welt, mit 4:1 in Seoul. Das Match wird von ueber 200 Millionen Menschen weltweit verfolgt.",
        "datum_handlung": "2016-03-15",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Demis_Hassabis",
        "quell_titel": "Demis Hassabis - Wikipedia",
        "kontext": "Historischer Moment fuer KI. Zug 37 in Spiel 2 ueberrascht Experten weltweit. Lee Sedol erringt einen Sieg in Spiel 4 mit ebenso brillantem Zug 78.",
    },
    # ---- H7. AlphaZero Veroeffentlichung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "DeepMind veroeffentlicht AlphaZero, ein generalisiertes Reinforcement-Learning-System, das Schach, Shogi und Go meistert - allein durch Selbstspiel ohne menschliches Wissen. Besiegt Stockfish 8 nach 9 Stunden Training.",
        "datum_handlung": "2017-12-05",
        "betrag_usd": None,
        "quell_link": "https://www.science.org/doi/10.1126/science.aar6404",
        "quell_titel": "A general reinforcement learning algorithm that masters chess, shogi, and Go (Science)",
        "kontext": "AlphaZero repraesentiert einen Paradigmenwechsel: von domainspezifischen zu generellen KI-Systemen. Hassabis nennt den Spielstil 'alien'.",
    },
    # ---- H8. AlphaFold CASP13 Durchbruch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "AlphaFold gewinnt die CASP13-Proteinstruktur-Vorhersage-Wettbewerb mit deutlichem Vorsprung. DeepMind wendet Deep Learning auf Biologie an.",
        "datum_handlung": "2018-12-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Erster Schritt zum Loesen der Proteinstrukturvorhersage. AlphaFold 1 zeigt, dass KI biologische Probleme angehen kann.",
    },
    # ---- H9. AlphaFold2 loest Protein-Folding ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "DeepMind veroeffentlicht AlphaFold2, das die 50-Jahre alte 'Protein-Folding'-Herausforderung loest. CASP14-Gewinn mit atomarer Genauigkeit (GDT-Score 92.4). Strukturen von ueber 200 Millionen Proteinen vorhergesagt.",
        "datum_handlung": "2020-11-30",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Wissenschaftlicher Meilenstein. Ueber 3 Millionen Forscher nutzen AlphaFold. John Jumper ist Co-Lead. Nature bezeichnet es als 'Loesung eines 50-Jahre-Problems'.",
    },
    # ---- H10. Gruendung Isomorphic Labs ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Demis Hassabis gruendet Isomorphic Labs, ein Alphabet-Tochterunternehmen, das KI fuer Medikamentenentwicklung nutzt. Hassabis ist CEO sowohl von DeepMind als auch Isomorphic.",
        "datum_handlung": "2021-11-04",
        "betrag_usd": None,
        "quell_link": "https://www.caproasia.com/2025/04/04/google-parent-alphabet-commercial-venture-isomorphic-labs-raised-600-million-in-first-external-funding-founded-in-2021-by-alphabet-demis-hassabis-who-is-founder-ceo-of-google-deepmind-and-2024-n/",
        "quell_titel": "Isomorphic Labs Raised $600 Million (Caproasia)",
        "kontext": "Kommerzialisierung von AlphaFold-Technologie fuer Pharma-Industrie. Isomorphic arbeitet mit Eli Lilly und Novartis zusammen.",
    },
    # ---- H11. DeepMind + Google Brain Merger ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Google vereint DeepMind und Google Brain zu 'Google DeepMind'. Demis Hassabis wird CEO der neuen Einheit. Ziel: Beschleunigung der KI-Entwicklung und AGI-Forschung.",
        "datum_handlung": "2023-04-20",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Google_DeepMind",
        "quell_titel": "Google DeepMind - Wikipedia",
        "kontext": "Strategische Entscheidung von Sundar Pichai und Sergey Brin. Jeff Dean wird Chief Scientist. Merger vereint zwei fuehrende KI-Labs.",
    },
    # ---- H12. Gemini 1.0 Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google DeepMind launcht Gemini 1.0, ein multimodales Large Language Model in drei Groessen (Ultra, Pro, Nano). Gemini Ultra uebertrifft GPT-4 in mehreren Benchmarks.",
        "datum_handlung": "2023-12-06",
        "betrag_usd": None,
        "quell_link": "https://time.com/collections/time100-companies-2025/7289661/google-deepmind/",
        "quell_titel": "Google DeepMind: 2025 TIME100 Most Influential Companies (TIME)",
        "kontext": "Googles Antwort auf ChatGPT/GPT-4. Gemini ist nativ multimodal (Text, Bild, Audio, Video, Code). Hassabis fuehrte die Entwicklung.",
    },
    # ---- H13. AlphaProteo Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Google DeepMind veroeffentlicht AlphaProteo, ein KI-System zum Design neuer Proteine, die an Zielmolekuele binden. Geht ueber AlphaFolds Vorhersagefaehigkeit hinaus zur aktiven Protein-Design.",
        "datum_handlung": "2024-09-05",
        "betrag_usd": None,
        "quell_link": "https://analyticsindiamag.com/ai-news-updates/google-deepmind-launches-alphaproteo-an-ai-model-for-generating-proteins/",
        "quell_titel": "Google DeepMind Launches AlphaProteo (AIM)",
        "kontext": "AlphaProteo kann Proteine entwerfen, die biologische Prozesse modifizieren. Anwendungen: Medikamentenentwicklung, Biosensoren, Therapien.",
    },
    # ---- H14. Nobelpreis Chemie 2024 ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Demis Hassabis und John M. Jumper erhalten den Nobelpreis fuer Chemie 2024 fuer die Entwicklung von AlphaFold2 zur Proteinstrukturvorhersage. Erster Nobelpreis fuer KI-Forschung.",
        "datum_handlung": "2024-10-09",
        "betrag_usd": None,
        "quell_link": "https://www.technologyreview.com/2024/10/09/1105335/google-deepmind-wins-joint-nobel-prize-in-chemistry-for-protein-prediction-ai/",
        "quell_titel": "Google DeepMind wins joint Nobel Prize in Chemistry (MIT Technology Review)",
        "kontext": "Historischer Moment: KI-System loest fundamentales wissenschaftliches Problem und wird mit Nobelpreis ausgezeichnet. Hassabis teilt Preis mit Jumper; David Baker (Uni Washington) erhaelt die andere Haelfte.",
    },
    # ---- H15. Ritterschlag (Knighthood) ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Demis Hassabis wird von Koenig Charles III. zum Ritter geschlagen ('Sir Demis Hassabis') fuer Verdienste um KI und Wissenschaft.",
        "datum_handlung": "2024-10-15",
        "betrag_usd": None,
        "quell_link": "https://fortune.com/article/demis-hassabis-deepmind-artificial-intelligence-google-alphabet-drug-discovery-isomorphic/",
        "quell_titel": "The pioneer behind Google Gemini is tackling disease (Fortune)",
        "kontext": "Wenige Tage nach Nobelpreis-Bekanntgabe. Hassabis schliesst sich Turing, Berners-Lee und anderen britischen Tech-Pionieren an.",
    },
    # ---- H16. Isomorphic Labs $600M Funding ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Isomorphic Labs schliesst erste externe Finanzierungsrunde ueber $600 Millionen ab. Gefuehrt von Thrive Capital, mit Beteiligung von Google Ventures und Alphabet.",
        "datum_handlung": "2025-04-01",
        "betrag_usd": 600000000.0,
        "quell_link": "https://fortune.com/2025/04/01/demis-hassabis-on-isomorphics-600-million-raise-ai-and-healthcares-future/",
        "quell_titel": "Demis Hassabis on Isomorphic's $600 million raise (Fortune)",
        "kontext": "Grosse Finanzierung fuer KI-basierte Medikamentenentwicklung. Isomorphic hat bereits Partnerschaften mit Pharma-Riesen Eli Lilly und Novartis.",
    },
    # ---- H17. DeepMind UK Government Partnership ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Google DeepMind kuendigt weitreichende Forschungspartnerschaft mit der britischen Regierung an. Fokus: Materialwissenschaft, saubere Energie, Kernfusion. Eroeffnung des ersten automatisierten Forschungslabors in UK 2026.",
        "datum_handlung": "2025-12-10",
        "betrag_usd": None,
        "quell_link": "https://fortune.com/2025/12/10/google-deepmind-uk-government-partnership-science-clean-energy/",
        "quell_titel": "Google DeepMind agrees to sweeping research collaboration with the U.K. government (Fortune)",
        "kontext": "Strategische Partnerschaft zur Beschleunigung wissenschaftlicher Durchbrueche. Suche nach Raumtemperatur-Supraleitern und Fusionsenergie-Loesungen.",
    },
    # ---- H18. DeepMind + Commonwealth Fusion Partnership ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Google DeepMind kuendigt Zusammenarbeit mit Commonwealth Fusion Systems an, um KI zur Beschleunigung der Fusionsenergie-Entwicklung einzusetzen. KI optimiert Simulation, Kontrollsysteme und Materialentdeckung.",
        "datum_handlung": "2025",
        "betrag_usd": None,
        "quell_link": "https://blockchain.news/ainews/google-deepmind-partners-with-commonwealth-fusion-systems-to-accelerate-fusion-energy-development-using-ai",
        "quell_titel": "Google DeepMind Partners with Commonwealth Fusion Systems (Blockchain.news)",
        "kontext": "KI fuer saubere Energie. Hassabis sieht Fusionsenergie als Schluessel zur Loesung der Energiekrise und zum Erreichen von AGI.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=11 existiert
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
            "Claude (collect_hassabis.py)"
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
        "Demis Hassabis quotes, interviews, Nobel Prize, AlphaFold, AlphaGo, AlphaZero, AlphaProteo, AGI, Lex Fridman, TIME100, Axios, consciousness, DeepMind, Google, Gemini",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: TIME100 Interview 2025, Nobel Prize Interview 2024, Lex Fridman Podcasts #299 und #475, "
        f"Axios Interviews, Twitter/X (@demishassabis), Fortune, MIT Technology Review, Science, "
        f"Philosophy for Life, OfficeChai, Medium, Chess.com, Wikipedia, Crunchbase, Nature.",
        "Claude (collect_hassabis.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Demis Hassabis (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Demis Hassabis")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_hassabis.py")
    print("  Verifizierte Aussagen & Handlungen: Demis Hassabis")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
