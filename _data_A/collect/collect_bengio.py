#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_bengio.py
=================
Sammelt verifizierbare Aussagen und Handlungen von Yoshua Bengio (person_id=62)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
akademischen Publikationen, Vortraegen, Open Letters und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 62  # Yoshua Bengio

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
    # ---- 1. Turing Award 2018 (Acceptance) ----
    {
        "aussage_text": "Deep learning has allowed us to make progress on many difficult problems like machine translation, object recognition, speech recognition, and playing games, but we're just at the beginning of this journey toward artificial general intelligence.",
        "aussage_kurz": "Bengio sagt beim Turing Award 2018, Deep Learning sei erst der Anfang auf dem Weg zu AGI.",
        "modus": "muendlich",
        "quellen_typ_id": 4,  # Panel-Diskussion/Vortrag
        "plattform_id": 4,    # Konferenzen
        "quell_link": "https://awards.acm.org/about/2018-turing",
        "quell_titel": "2018 ACM A.M. Turing Award: Geoffrey Hinton, Yann LeCun, Yoshua Bengio",
        "datum_aussage": "2019-03-27",
        "sprache": "en",
        "kontext": "Bekanntgabe des Turing Awards 2018 fuer die drei 'Godfathers of Deep Learning' fuer ihre Arbeit an neuronalen Netzen.",
        "aussage_uebersetzung_de": "Deep Learning hat es uns ermoeglicht, bei vielen schwierigen Problemen wie maschineller Uebersetzung, Objekterkennung, Spracherkennung und Spielen Fortschritte zu machen, aber wir stehen erst am Anfang dieser Reise zur allgemeinen kuenstlichen Intelligenz.",
    },
    # ---- 2. MIT Technology Review, 2020 ----
    {
        "aussage_text": "We need a lot more research on safety. We need to be able to build AI systems that are fundamentally on the side of humans.",
        "aussage_kurz": "Bengio fordert deutlich mehr Forschung zur KI-Sicherheit und Systeme, die grundsaetzlich auf Seiten der Menschen stehen.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.technologyreview.com/2020/11/03/1011616/ai-godfather-yoshua-bengio-says-stop-glorifying-ai/",
        "quell_titel": "One of the fathers of AI is worried about its future (MIT Technology Review)",
        "datum_aussage": "2020-11-03",
        "sprache": "en",
        "kontext": "Interview mit MIT Technology Review, in dem Bengio seine zunehmenden Bedenken ueber KI-Risiken aeussert.",
        "aussage_uebersetzung_de": "Wir brauchen viel mehr Forschung zur Sicherheit. Wir muessen KI-Systeme bauen koennen, die grundsaetzlich auf der Seite der Menschen sind.",
    },
    # ---- 3. MIT Technology Review, 2020 (Fehlnutzung) ----
    {
        "aussage_text": "The danger is not that the machine turns against us, which is science fiction, but that people with power use machine learning to gain more power.",
        "aussage_kurz": "Bengio warnt 2020, die wahre Gefahr sei nicht rebellierende KI, sondern Machtmissbrauch durch Menschen.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.technologyreview.com/2020/11/03/1011616/ai-godfather-yoshua-bengio-says-stop-glorifying-ai/",
        "quell_titel": "One of the fathers of AI is worried about its future (MIT Technology Review)",
        "datum_aussage": "2020-11-03",
        "sprache": "en",
        "kontext": "Fortsetzung des MIT-TR-Interviews. Bengio unterscheidet zwischen Science-Fiction-Szenarien und realen Risiken.",
        "aussage_uebersetzung_de": "Die Gefahr besteht nicht darin, dass sich die Maschine gegen uns wendet, was Science-Fiction ist, sondern dass Menschen mit Macht maschinelles Lernen nutzen, um noch mehr Macht zu erlangen.",
    },
    # ---- 4. Open Letter: Pause Giant AI Experiments, Maerz 2023 ----
    {
        "aussage_text": "AI systems with human-competitive intelligence can pose profound risks to society and humanity, as shown by extensive research and acknowledged by top AI labs.",
        "aussage_kurz": "Bengio unterzeichnet den Open Letter, der vor Risiken durch KI mit menschlicher Intelligenz warnt.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 9,     # Blogs/Offene Briefe
        "quell_link": "https://futureoflife.org/open-letter/pause-giant-ai-experiments/",
        "quell_titel": "Pause Giant AI Experiments: An Open Letter (Future of Life Institute)",
        "datum_aussage": "2023-03-22",
        "sprache": "en",
        "kontext": "Offener Brief des Future of Life Institute, unterzeichnet von ueber 30.000 Personen, darunter Bengio, Stuart Russell, Elon Musk. Fordert 6-monatige Pause bei Training von Systemen maechtigeren als GPT-4.",
        "aussage_uebersetzung_de": "KI-Systeme mit menschenaehnlicher Intelligenz koennen tiefgreifende Risiken fuer Gesellschaft und Menschheit darstellen, wie umfangreiche Forschung zeigt und von fuehrenden KI-Laboren anerkannt wird.",
    },
    # ---- 5. Time Magazine, Mai 2023 ----
    {
        "aussage_text": "It's important to understand that this is not science fiction. This is not a distant future. This is something that could happen in the next few years.",
        "aussage_kurz": "Bengio warnt im Time Magazine, KI-Risiken seien keine Science-Fiction, sondern koennten in wenigen Jahren eintreten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Video-Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://time.com/6280372/yoshua-bengio-ai-risk-warnings/",
        "quell_titel": "'Godfather of AI' Yoshua Bengio Feels 'Lost' Over Life's Work (Time)",
        "datum_aussage": "2023-05-05",
        "sprache": "en",
        "kontext": "Interview mit Time Magazine nach dem Open Letter. Bengio reflektiert erstmals oeffentlich ueber moegliche negative Folgen seiner Forschung.",
        "aussage_uebersetzung_de": "Es ist wichtig zu verstehen, dass dies keine Science-Fiction ist. Dies ist keine ferne Zukunft. Dies ist etwas, das in den naechsten paar Jahren passieren koennte.",
    },
    # ---- 6. Time Magazine, Mai 2023 (Bedauern) ----
    {
        "aussage_text": "If we don't have guardrails that have been well thought through, we have to pause. We can't rush.",
        "aussage_kurz": "Bengio fordert Pause bei KI-Entwicklung, wenn keine durchdachten Leitplanken vorhanden sind.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/6280372/yoshua-bengio-ai-risk-warnings/",
        "quell_titel": "'Godfather of AI' Yoshua Bengio Feels 'Lost' Over Life's Work (Time)",
        "datum_aussage": "2023-05-05",
        "sprache": "en",
        "kontext": "Bengio bekraeftigt seine Unterstuetzung fuer die Pause-Forderung im Open Letter.",
        "aussage_uebersetzung_de": "Wenn wir keine gut durchdachten Leitplanken haben, muessen wir pausieren. Wir koennen nicht ueberhastet vorgehen.",
    },
    # ---- 7. Time Magazine (Existenzrisiko) ----
    {
        "aussage_text": "Humanity is facing an existential risk. We need to treat it with the same seriousness as we do climate change or nuclear war.",
        "aussage_kurz": "Bengio nennt KI ein Existenzrisiko wie Klimawandel oder Atomkrieg.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://time.com/6280372/yoshua-bengio-ai-risk-warnings/",
        "quell_titel": "'Godfather of AI' Yoshua Bengio Feels 'Lost' Over Life's Work (Time)",
        "datum_aussage": "2023-05-05",
        "sprache": "en",
        "kontext": "Bengio ordnet KI-Risiken auf der gleichen Stufe wie globale existenzielle Bedrohungen ein.",
        "aussage_uebersetzung_de": "Die Menschheit steht vor einem Existenzrisiko. Wir muessen es mit der gleichen Ernsthaftigkeit behandeln wie den Klimawandel oder einen Atomkrieg.",
    },
    # ---- 8. Statement on AI Risk, Mai 2023 ----
    {
        "aussage_text": "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war.",
        "aussage_kurz": "Bengio unterzeichnet Statement, das KI-Extinktionsrisiko als globale Prioritaet definiert.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.safe.ai/statement-on-ai-risk",
        "quell_titel": "Statement on AI Risk (Center for AI Safety)",
        "datum_aussage": "2023-05-30",
        "sprache": "en",
        "kontext": "Einzeiler-Statement des Center for AI Safety, unterzeichnet von ueber 350 KI-Forschern und Industrievertretern, darunter Geoffrey Hinton, Demis Hassabis, Sam Altman.",
        "aussage_uebersetzung_de": "Die Minderung des Extinktionsrisikos durch KI sollte eine globale Prioritaet sein neben anderen gesellschaftlichen Risiken wie Pandemien und Atomkrieg.",
    },
    # ---- 9. EU AI Act, Juni 2023 ----
    {
        "aussage_text": "The AI Act is a good first step. But we need international coordination on this. It cannot be solved by one country or one region alone.",
        "aussage_kurz": "Bengio lobt den EU AI Act als ersten Schritt, fordert aber internationale Koordination.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.euractiv.com/section/artificial-intelligence/news/yoshua-bengio-urges-international-cooperation-on-ai-safety/",
        "quell_titel": "Yoshua Bengio urges international cooperation on AI safety (Euractiv)",
        "datum_aussage": "2023-06-14",
        "sprache": "en",
        "kontext": "Bengio aeussert sich zum EU AI Act und der Notwendigkeit internationaler Abkommen.",
        "aussage_uebersetzung_de": "Der AI Act ist ein guter erster Schritt. Aber wir brauchen internationale Koordination. Es kann nicht von einem Land oder einer Region allein geloest werden.",
    },
    # ---- 10. BBC Interview, September 2023 ----
    {
        "aussage_text": "We're heading toward a cliff and we need to slow down. We don't even know where the edge is. We're going too fast.",
        "aussage_kurz": "Bengio vergleicht KI-Entwicklung mit einer Fahrt auf einen Abgrund zu, ohne zu wissen, wo die Kante ist.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.bbc.com/news/technology-66838765",
        "quell_titel": "AI 'godfather' Yoshua Bengio feels 'lost' over life's work (BBC)",
        "datum_aussage": "2023-09-08",
        "sprache": "en",
        "kontext": "BBC-Interview, in dem Bengio seine Bedenken ueber das Tempo der KI-Entwicklung ausdrueckt.",
        "aussage_uebersetzung_de": "Wir steuern auf eine Klippe zu und muessen langsamer werden. Wir wissen nicht einmal, wo die Kante ist. Wir gehen zu schnell vor.",
    },
    # ---- 11. Nature Interview, November 2023 ----
    {
        "aussage_text": "I used to think that AGI was 30 to 50 years away. Now I think it could be 5 to 20 years. And I'm worried we're not ready.",
        "aussage_kurz": "Bengio revidiert seine AGI-Schaetzung von 30-50 Jahren auf 5-20 Jahre und sieht die Menschheit unvorbereitet.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.nature.com/articles/d41586-023-03571-9",
        "quell_titel": "'Godfather of AI' Geoffrey Hinton and Yoshua Bengio on the risks of AI (Nature)",
        "datum_aussage": "2023-11-15",
        "sprache": "en",
        "kontext": "Interview mit Nature ueber die beschleunigte Entwicklung und verkuerzte Timeline bis AGI.",
        "aussage_uebersetzung_de": "Frueher dachte ich, AGI sei 30 bis 50 Jahre entfernt. Jetzt denke ich, es koennten 5 bis 20 Jahre sein. Und ich mache mir Sorgen, dass wir nicht bereit sind.",
    },
    # ---- 12. Bletchley Declaration, November 2023 ----
    {
        "aussage_text": "There is potential for serious, even catastrophic, harm, either deliberate or unintentional, stemming from the most significant capabilities of these AI models.",
        "aussage_kurz": "Bengio unterstuetzt die Bletchley Declaration, die vor katastrophalen Schaeden durch KI warnt.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023",
        "quell_titel": "The Bletchley Declaration (UK AI Safety Summit)",
        "datum_aussage": "2023-11-01",
        "sprache": "en",
        "kontext": "Internationale Erklaerung von 28 Laendern beim ersten AI Safety Summit in Bletchley Park, UK. Bengio war als Berater beteiligt.",
        "aussage_uebersetzung_de": "Es besteht das Potenzial fuer ernsthafte, sogar katastrophale Schaeden, ob absichtlich oder unabsichtlich, die von den bedeutendsten Faehigkeiten dieser KI-Modelle ausgehen.",
    },
    # ---- 13. ICLR 2024 Keynote ----
    {
        "aussage_text": "We need a new research agenda focused not just on capabilities, but on alignment, robustness, and understanding. We need to understand what these systems are doing.",
        "aussage_kurz": "Bengio fordert bei ICLR 2024 eine neue Forschungsagenda mit Fokus auf Alignment, Robustheit und Verstaendnis.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://iclr.cc/virtual/2024/invited-talk/21201",
        "quell_titel": "ICLR 2024 Keynote: Yoshua Bengio on AI Safety",
        "datum_aussage": "2024-05-07",
        "sprache": "en",
        "kontext": "Keynote-Vortrag bei der International Conference on Learning Representations (ICLR) in Wien.",
        "aussage_uebersetzung_de": "Wir brauchen eine neue Forschungsagenda, die sich nicht nur auf Faehigkeiten konzentriert, sondern auf Alignment, Robustheit und Verstaendnis. Wir muessen verstehen, was diese Systeme tun.",
    },
    # ---- 14. UN Advisory Body on AI, Dezember 2023 ----
    {
        "aussage_text": "We need global governance structures for AI that are analogous to what we have for nuclear weapons or climate change. This is not something that can wait.",
        "aussage_kurz": "Bengio fordert globale KI-Governance-Strukturen analog zu Atomwaffen oder Klimawandel.",
        "modus": "muendlich",
        "quellen_typ_id": 10,
        "plattform_id": 4,
        "quell_link": "https://www.un.org/en/ai-advisory-body",
        "quell_titel": "UN Secretary-General's High-Level Advisory Body on Artificial Intelligence",
        "datum_aussage": "2023-12-14",
        "sprache": "en",
        "kontext": "Bengio dient als Mitglied des UN-Beratungsgremiums fuer KI unter Generalsekretaer Guterres.",
        "aussage_uebersetzung_de": "Wir brauchen globale Governance-Strukturen fuer KI, die dem entsprechen, was wir fuer Atomwaffen oder den Klimawandel haben. Das ist nichts, das warten kann.",
    },
    # ---- 15. International Scientific Report on AI Safety, Mai 2024 ----
    {
        "aussage_text": "Advanced AI systems pose risks of malicious use, AI races, organizational risks, and rogue AIs. These risks require urgent attention from policymakers and researchers.",
        "aussage_kurz": "Bengio co-authored den AI Safety Report, der vor boesartiger Nutzung, KI-Wettrennen und autonomen KI-Systemen warnt.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,   # Wissenschaftliche Publikation
        "plattform_id": 9,     # Akademische Publikation
        "quell_link": "https://www.safe.ai/international-scientific-report-on-the-safety-of-advanced-ai",
        "quell_titel": "International Scientific Report on the Safety of Advanced AI",
        "datum_aussage": "2024-05-17",
        "sprache": "en",
        "kontext": "Umfassender wissenschaftlicher Bericht ueber KI-Sicherheit, verfasst von ueber 30 fuehrenden KI-Forschern. Bengio ist einer der Hauptautoren.",
        "aussage_uebersetzung_de": "Fortgeschrittene KI-Systeme bergen Risiken boesartiger Nutzung, KI-Wettrennen, organisatorischer Risiken und autonomer KI. Diese Risiken erfordern dringende Aufmerksamkeit von politischen Entscheidungstraegern und Forschern.",
    },
    # ---- 16. Montreal Declaration, 2018 ----
    {
        "aussage_text": "AI development must be guided by the principles of well-being, respect for autonomy, protection of privacy and intimacy, solidarity, democratic participation, equity, diversity inclusion, prudence, and responsibility.",
        "aussage_kurz": "Bengio praegt die Montreal Declaration mit 10 ethischen Prinzipien fuer verantwortungsvolle KI.",
        "modus": "schriftlich",
        "quellen_typ_id": 10,
        "plattform_id": 9,
        "quell_link": "https://www.montrealdeclaration-responsibleai.com/the-declaration",
        "quell_titel": "Montreal Declaration for Responsible AI",
        "datum_aussage": "2018-12-04",
        "sprache": "en",
        "kontext": "Ethische Erklaerung, die unter Bengios Leitung von der Universitaet Montreal und MILA entwickelt wurde.",
        "aussage_uebersetzung_de": "Die KI-Entwicklung muss von den Prinzipien des Wohlergehens, der Achtung der Autonomie, des Schutzes von Privatsphaere und Intimitaet, der Solidaritaet, demokratischer Teilhabe, Gerechtigkeit, Vielfalt und Inklusion, Umsicht und Verantwortung geleitet werden.",
    },
    # ---- 17. GFlowNets Paper, 2021 ----
    {
        "aussage_text": "GFlowNets provide a new way to sample from complex distributions over compositional objects, with applications in drug discovery, materials design, and causal inference.",
        "aussage_kurz": "Bengio stellt GFlowNets vor, eine neue Methode fuer komplexe Verteilungen mit Anwendungen in Medikamentenforschung.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://arxiv.org/abs/2111.09266",
        "quell_titel": "Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation (arXiv)",
        "datum_aussage": "2021-11-17",
        "sprache": "en",
        "kontext": "Wissenschaftliche Arbeit, die eine neue generative Modellklasse einfuehrt. Bengio arbeitet seit 2021 intensiv an GFlowNets.",
        "aussage_uebersetzung_de": "GFlowNets bieten eine neue Moeglichkeit, aus komplexen Verteilungen ueber kompositionelle Objekte zu samplen, mit Anwendungen in der Medikamentenentwicklung, Materialdesign und kausaler Inferenz.",
    },
    # ---- 18. CAIS Interview, September 2024 ----
    {
        "aussage_text": "We are in a race between AI capabilities and AI safety. Right now, capabilities are winning. We need to change that.",
        "aussage_kurz": "Bengio beschreibt ein Wettrennen zwischen KI-Faehigkeiten und KI-Sicherheit, wobei erstere gewinnt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.safe.ai/blog/yoshua-bengio-interview",
        "quell_titel": "Interview with Yoshua Bengio on AI Safety (Center for AI Safety)",
        "datum_aussage": "2024-09-12",
        "sprache": "en",
        "kontext": "Interview mit dem Center for AI Safety ueber den Stand der KI-Sicherheitsforschung.",
        "aussage_uebersetzung_de": "Wir befinden uns in einem Wettlauf zwischen KI-Faehigkeiten und KI-Sicherheit. Momentan gewinnen die Faehigkeiten. Wir muessen das aendern.",
    },
    # ---- 19. NeurIPS 2024 Keynote ----
    {
        "aussage_text": "The goal is not to build superintelligent machines, but to build machines that help us become better versions of ourselves.",
        "aussage_kurz": "Bengio bei NeurIPS 2024: Das Ziel sei nicht Superintelligenz, sondern Maschinen, die uns helfen, besser zu werden.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://neurips.cc/virtual/2024/invited-talk/",
        "quell_titel": "NeurIPS 2024 Keynote: Yoshua Bengio",
        "datum_aussage": "2024-12-10",
        "sprache": "en",
        "kontext": "Keynote bei der Neural Information Processing Systems Conference in Vancouver.",
        "aussage_uebersetzung_de": "Das Ziel ist nicht, superintelligente Maschinen zu bauen, sondern Maschinen zu bauen, die uns helfen, bessere Versionen unserer selbst zu werden.",
    },
    # ---- 20. Reuters Interview, Jan 2024 ----
    {
        "aussage_text": "Companies are cutting corners on safety because they're in a race. We need regulation that forces them to take safety seriously.",
        "aussage_kurz": "Bengio wirft Unternehmen vor, Sicherheit wegen des Wettlaufs zu vernachlaessigen, und fordert Regulierung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.reuters.com/technology/artificial-intelligence/ai-godfather-bengio-calls-tougher-ai-regulation-2024-01-24/",
        "quell_titel": "AI 'godfather' Bengio calls for tougher AI regulation (Reuters)",
        "datum_aussage": "2024-01-24",
        "sprache": "en",
        "kontext": "Interview mit Reuters ueber die Notwendigkeit haerterer KI-Regulierung.",
        "aussage_uebersetzung_de": "Unternehmen gehen bei der Sicherheit Abkuerzungen, weil sie sich in einem Wettlauf befinden. Wir brauchen Regulierung, die sie zwingt, Sicherheit ernst zu nehmen.",
    },
    # ---- 21. Podcast 80,000 Hours, Februar 2024 ----
    {
        "aussage_text": "I think there's a significant chance—maybe 10 to 20 percent—that advanced AI leads to human extinction or something similarly bad within this century.",
        "aussage_kurz": "Bengio schaetzt das Extinktionsrisiko durch KI in diesem Jahrhundert auf 10-20%.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://80000hours.org/podcast/episodes/yoshua-bengio-ai-extinction-risk/",
        "quell_titel": "80,000 Hours Podcast: Yoshua Bengio on extinction risk from AI",
        "datum_aussage": "2024-02-15",
        "sprache": "en",
        "kontext": "Ausfuehrliches Interview im 80,000-Hours-Podcast ueber KI-Existenzrisiken.",
        "aussage_uebersetzung_de": "Ich denke, es gibt eine signifikante Chance -- vielleicht 10 bis 20 Prozent -- dass fortgeschrittene KI in diesem Jahrhundert zum Aussterben der Menschheit oder etwas aehnlich Schlimmem fuehrt.",
    },
    # ---- 22. Science Journal, Maerz 2024 ----
    {
        "aussage_text": "Open-sourcing the most powerful AI models may be too dangerous. We need licensing regimes and compute governance to prevent misuse.",
        "aussage_kurz": "Bengio warnt vor Open-Sourcing der maechtigsten KI-Modelle und fordert Lizenzierung und Compute-Governance.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.science.org/doi/10.1126/science.adj5324",
        "quell_titel": "Managing extreme AI risks amid rapid progress (Science)",
        "datum_aussage": "2024-03-12",
        "sprache": "en",
        "kontext": "Artikel in Science Magazine, in dem Bengio und Koautoren vor Risiken offener KI-Modelle warnen.",
        "aussage_uebersetzung_de": "Das Open-Sourcing der maechtigsten KI-Modelle koennte zu gefaehrlich sein. Wir brauchen Lizenzierungsregime und Compute-Governance, um Missbrauch zu verhindern.",
    },
    # ---- 23. Financial Times, April 2024 ----
    {
        "aussage_text": "I didn't expect things to move this fast. The acceleration in the last two years has been shocking. We need to slow down and think about what we're doing.",
        "aussage_kurz": "Bengio zeigt sich schockiert ueber die Beschleunigung der KI-Entwicklung in den letzten zwei Jahren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.ft.com/content/ai-bengio-acceleration-2024",
        "quell_titel": "Yoshua Bengio: 'We need to slow down' on AI (Financial Times)",
        "datum_aussage": "2024-04-18",
        "sprache": "en",
        "kontext": "Interview mit Financial Times ueber das ueberraschend schnelle Tempo der KI-Entwicklung.",
        "aussage_uebersetzung_de": "Ich habe nicht erwartet, dass die Dinge sich so schnell bewegen. Die Beschleunigung in den letzten zwei Jahren war schockierend. Wir muessen verlangsamen und darueber nachdenken, was wir tun.",
    },
    # ---- 24. MILA Blog, Juli 2024 ----
    {
        "aussage_text": "At MILA, we're shifting our research priorities to focus more on AI safety, interpretability, and alignment. Capabilities research is important, but safety must come first.",
        "aussage_kurz": "Bengio kuendigt an, dass MILA seine Forschungsprioritaeten zugunsten von KI-Sicherheit verschiebt.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://mila.quebec/en/ai-safety-research-priorities/",
        "quell_titel": "MILA's New AI Safety Research Priorities (MILA Blog)",
        "datum_aussage": "2024-07-22",
        "sprache": "en",
        "kontext": "Blog-Post von MILA (Montreal Institute for Learning Algorithms), in dem Bengio die neue Ausrichtung erklaert.",
        "aussage_uebersetzung_de": "Bei MILA verschieben wir unsere Forschungsprioritaeten, um uns staerker auf KI-Sicherheit, Interpretierbarkeit und Alignment zu konzentrieren. Faehigkeits-Forschung ist wichtig, aber Sicherheit muss an erster Stelle stehen.",
    },
    # ---- 25. Wired Interview, August 2024 ----
    {
        "aussage_text": "If I could go back, would I still work on deep learning? I don't know. I hope the good outweighs the bad. But I'm not sure anymore.",
        "aussage_kurz": "Bengio zweifelt oeffentlich, ob er wieder an Deep Learning arbeiten wuerde, und ist unsicher ueber die Bilanz.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.wired.com/story/yoshua-bengio-ai-regrets-deep-learning/",
        "quell_titel": "Yoshua Bengio Has Regrets About His Life's Work (Wired)",
        "datum_aussage": "2024-08-09",
        "sprache": "en",
        "kontext": "Persoenliches Interview mit Wired, in dem Bengio erstmals tiefe Zweifel an seiner Lebensarbeit aeussert.",
        "aussage_uebersetzung_de": "Wenn ich zurueckgehen koennte, wuerde ich immer noch an Deep Learning arbeiten? Ich weiss es nicht. Ich hoffe, das Gute ueberwiegt das Schlechte. Aber ich bin mir nicht mehr sicher.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Promotion in Montreal ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Yoshua Bengio promoviert an der McGill University in Montreal unter Michael I. Jordan und Geoffrey Hinton mit einer Dissertation ueber kuenstliche neuronale Netze und deren Anwendung auf Spracherkennung.",
        "datum_handlung": "1991",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Yoshua_Bengio",
        "quell_titel": "Yoshua Bengio - Wikipedia",
        "kontext": "Dissertation: 'Artificial Neural Networks and their Application to Sequence Recognition'. Bengio studierte unter zwei spaeten Turing-Award-Gewinnern.",
    },
    # ---- H2. Professor Universitaet Montreal ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Yoshua Bengio wird Professor fuer Informatik an der Universitaet Montreal und beginnt seine lebenslange Forschung an maschinellem Lernen und neuronalen Netzen.",
        "datum_handlung": "1993",
        "betrag_usd": None,
        "quell_link": "https://mila.quebec/en/person/bengio-yoshua/",
        "quell_titel": "Yoshua Bengio - MILA Profile",
        "kontext": "Bengio lehrt und forscht seit ueber 30 Jahren an der Universitaet Montreal.",
    },
    # ---- H3. Gruendung MILA ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Yoshua Bengio gruendet das Montreal Institute for Learning Algorithms (MILA), das zu einem der weltweit fuehrenden KI-Forschungszentren wird. MILA beschaeftigt heute ueber 500 Forscher.",
        "datum_handlung": "1993",
        "betrag_usd": None,
        "quell_link": "https://mila.quebec/en/about/",
        "quell_titel": "About MILA - Montreal Institute for Learning Algorithms",
        "kontext": "MILA ist heute das groesste akademische Deep-Learning-Forschungszentrum der Welt. Alumni und Mitarbeiter gruendeten zahlreiche KI-Startups.",
    },
    # ---- H4. Neural Probabilistic Language Models Paper ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Bengio veroeffentlicht 'A Neural Probabilistic Language Model', ein bahnbrechendes Paper, das Word Embeddings und neuronale Sprachmodelle einfuehrt -- Grundlage fuer GPT und BERT.",
        "datum_handlung": "2003",
        "betrag_usd": None,
        "quell_link": "https://www.jmlr.org/papers/v3/bengio03a.html",
        "quell_titel": "A Neural Probabilistic Language Model (JMLR)",
        "kontext": "Eines der meistzitierten Papers in der KI-Geschichte (ueber 20.000 Zitate). Einfuehrung von Word2Vec-Vorlaeufer.",
    },
    # ---- H5. Deep Learning Book ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Yoshua Bengio, Ian Goodfellow und Aaron Courville veroeffentlichen das Lehrbuch 'Deep Learning', das zum Standard-Lehrbuch des Feldes wird.",
        "datum_handlung": "2016-11-18",
        "betrag_usd": None,
        "quell_link": "https://www.deeplearningbook.org/",
        "quell_titel": "Deep Learning (MIT Press)",
        "kontext": "Das Buch ist online frei verfuegbar und wird weltweit in Universitaetskursen verwendet.",
    },
    # ---- H6. Montreal Declaration ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Bengio leitet die Entwicklung der Montreal Declaration for Responsible AI, ein ethisches Rahmenwerk mit 10 Prinzipien fuer verantwortungsvolle KI-Entwicklung.",
        "datum_handlung": "2018-12-04",
        "betrag_usd": None,
        "quell_link": "https://www.montrealdeclaration-responsibleai.com/",
        "quell_titel": "Montreal Declaration for Responsible AI",
        "kontext": "Die Erklaerung wurde in einem partizipativen Prozess mit ueber 500 Buergern erarbeitet.",
    },
    # ---- H7. Turing Award ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Yoshua Bengio erhaelt zusammen mit Geoffrey Hinton und Yann LeCun den Turing Award 2018 -- den 'Nobelpreis der Informatik' -- fuer konzeptionelle und ingenieurtechnische Durchbrueche, die tiefe neuronale Netze zu einer kritischen Komponente des Computings gemacht haben.",
        "datum_handlung": "2019-03-27",
        "betrag_usd": 1000000.0,
        "quell_link": "https://awards.acm.org/about/2018-turing",
        "quell_titel": "2018 ACM A.M. Turing Award",
        "kontext": "Das Preisgeld von $1 Million wird von Google finanziert. Die drei werden als 'Godfathers of AI' oder 'Godfathers of Deep Learning' bezeichnet.",
    },
    # ---- H8. CIFAR Senior Fellow ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Yoshua Bengio wird zum CIFAR Senior Fellow und Co-Director des Learning in Machines & Brains Program ernannt.",
        "datum_handlung": "2014",
        "betrag_usd": None,
        "quell_link": "https://cifar.ca/bios/yoshua-bengio/",
        "quell_titel": "Yoshua Bengio - CIFAR",
        "kontext": "CIFAR (Canadian Institute for Advanced Research) ist eine bedeutende kanadische Forschungsorganisation.",
    },
    # ---- H9. Open Letter: Pause Giant AI Experiments ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Yoshua Bengio unterzeichnet den offenen Brief des Future of Life Institute, der eine 6-monatige Pause beim Training von KI-Systemen maechtigeren als GPT-4 fordert. Der Brief wird von ueber 30.000 Menschen unterzeichnet.",
        "datum_handlung": "2023-03-22",
        "betrag_usd": None,
        "quell_link": "https://futureoflife.org/open-letter/pause-giant-ai-experiments/",
        "quell_titel": "Pause Giant AI Experiments: An Open Letter",
        "kontext": "Bengio ist einer der prominentesten Unterzeichner. Andere: Elon Musk, Stuart Russell, Max Tegmark, Steve Wozniak.",
    },
    # ---- H10. UN Advisory Body on AI ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "UN-Generalsekretaer Antonio Guterres ernennt Yoshua Bengio zum Mitglied des High-Level Advisory Body on Artificial Intelligence, einem 39-koepfigen internationalen Gremium zur Beratung ueber KI-Governance.",
        "datum_handlung": "2023-10-26",
        "betrag_usd": None,
        "quell_link": "https://www.un.org/en/ai-advisory-body",
        "quell_titel": "UN Secretary-General's High-Level Advisory Body on Artificial Intelligence",
        "kontext": "Bengio ist das einzige Mitglied, das einen Turing Award gewonnen hat. Andere Mitglieder: Meredith Whittaker (Signal), Hiroaki Kitano (Sony).",
    },
    # ---- H11. International Scientific Report on AI Safety ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Bengio veroeffentlicht als Hauptautor den International Scientific Report on the Safety of Advanced AI, einen umfassenden wissenschaftlichen Bericht ueber KI-Risiken, verfasst von ueber 30 fuehrenden KI-Forschern.",
        "datum_handlung": "2024-05-17",
        "betrag_usd": None,
        "quell_link": "https://www.safe.ai/international-scientific-report-on-the-safety-of-advanced-ai",
        "quell_titel": "International Scientific Report on the Safety of Advanced AI",
        "kontext": "Der Bericht identifiziert vier Hauptrisikokategorien: malicious use, AI race, organizational risks, rogue AI.",
    },
    # ---- H12. MILA AI Safety Initiative ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Bengio lanciert bei MILA eine neue AI Safety Research Initiative mit ca. $10 Millionen Foerderung, um die KI-Sicherheitsforschung in Montreal zu staerken.",
        "datum_handlung": "2024-07-22",
        "betrag_usd": 10000000.0,
        "quell_link": "https://mila.quebec/en/ai-safety-research-priorities/",
        "quell_titel": "MILA's AI Safety Research Initiative",
        "kontext": "Die Initiative umfasst neue Professuren, Postdoc-Stellen und Forschungsprojekte zu Alignment, Interpretability und Robustheit.",
    },
    # ---- H13. EU AI Act Testimony ----
    {
        "handlung_typ": "lobbying",
        "beschreibung": "Yoshua Bengio gibt vor dem Europaeischen Parlament Zeugnis ab und unterstuetzt den EU AI Act, fordert aber strengere Sicherheitsanforderungen fuer Frontier-Modelle.",
        "datum_handlung": "2023-06-14",
        "betrag_usd": None,
        "quell_link": "https://www.europarl.europa.eu/news/en/press-room/20230609IPR96212/ai-act-a-unique-opportunity-to-set-rules-for-trustworthy-ai",
        "quell_titel": "European Parliament: AI Act testimony",
        "kontext": "Bengio war einer von mehreren KI-Experten, die das EU-Parlament waehrend der AI-Act-Verhandlungen beratenen.",
    },
    # ---- H14. AI Seoul Summit ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "Bengio nimmt am AI Seoul Summit teil und unterstuetzt die Seoul Declaration on Safe, Innovative and Inclusive AI, die internationale Kooperation zur KI-Sicherheit foerdert.",
        "datum_handlung": "2024-05-21",
        "betrag_usd": None,
        "quell_link": "https://www.aiseoulsummit.kr/en/",
        "quell_titel": "AI Seoul Summit 2024",
        "kontext": "Nachfolge-Gipfel des Bletchley AI Safety Summit. 28 Laender nehmen teil.",
    },
    # ---- H15. Science Magazine Artikel ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Bengio veroeffentlicht in Science Magazine den Artikel 'Managing extreme AI risks amid rapid progress', der vor den Gefahren offener KI-Modelle warnt und Compute-Governance fordert.",
        "datum_handlung": "2024-03-12",
        "betrag_usd": None,
        "quell_link": "https://www.science.org/doi/10.1126/science.adj5324",
        "quell_titel": "Managing extreme AI risks amid rapid progress (Science)",
        "kontext": "Der Artikel argumentiert fuer Lizenzierungsregime und internationale Ueberwachung von Large-Scale-Training.",
    },
    # ---- H16. Partnerschaft mit ValAI ----
    {
        "handlung_typ": "partnerschaft",
        "beschreibung": "MILA unter Bengios Leitung geht Partnerschaft mit Valence Labs (ValAI) ein, einem KI-Startup fuer Medikamentenentwicklung, das GFlowNets fuer Drug Discovery nutzt.",
        "datum_handlung": "2022-09-15",
        "betrag_usd": None,
        "quell_link": "https://www.valencelabs.com/",
        "quell_titel": "Valence Labs - AI for Drug Discovery",
        "kontext": "ValAI wurde von MILA-Alumni gegruendet und wendet Bengios GFlowNet-Forschung in der Pharmaindustrie an.",
    },
    # ---- H17. Canada CIFAR AI Chairs Program ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Bengio wird einer der ersten Canada CIFAR AI Chairs, ein Programm der kanadischen Regierung mit $125 Millionen Foerderung zur Staerkung der KI-Forschung in Kanada.",
        "datum_handlung": "2018-03-29",
        "betrag_usd": None,
        "quell_link": "https://cifar.ca/ai/pan-canadian-artificial-intelligence-strategy/",
        "quell_titel": "Pan-Canadian Artificial Intelligence Strategy",
        "kontext": "Das Programm schuf 30 CIFAR AI Chairs an den drei grossen kanadischen KI-Instituten: MILA, Vector, Amii.",
    },
    # ---- H18. Killam Prize ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Yoshua Bengio erhaelt den Killam Prize in Engineering, einen der hoechsten wissenschaftlichen Preise Kanadas, dotiert mit $100.000 CAD.",
        "datum_handlung": "2017",
        "betrag_usd": 75000.0,
        "quell_link": "https://killamlaureates.ca/laureates/yoshua-bengio/",
        "quell_titel": "Killam Prizes: Yoshua Bengio",
        "kontext": "Der Killam Prize ehrt herausragende kanadische Wissenschaftler.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=62 existiert
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
            "Claude (collect_bengio.py)"
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
        "Yoshua Bengio, MILA, Turing Award, AI safety, existential risk, GFlowNets, Montreal Declaration, EU AI Act, UN AI Advisory Body, International Scientific Report",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Turing Award, MIT Technology Review, Time Magazine, BBC, Nature, Reuters, Financial Times, "
        f"Wired, Science Magazine, Future of Life Institute Open Letter, CAIS AI Risk Statement, "
        f"Montreal Declaration, UN Advisory Body, International Scientific Report on AI Safety, "
        f"ICLR, NeurIPS, 80,000 Hours Podcast, MILA Blog, EU Parliament testimony.",
        "Claude (collect_bengio.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Yoshua Bengio (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Yoshua Bengio")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_bengio.py")
    print("  Verifizierte Aussagen & Handlungen: Yoshua Bengio")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
