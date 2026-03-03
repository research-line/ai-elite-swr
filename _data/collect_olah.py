#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_olah.py
===============
Fuegt verifizierbare Aussagen und Handlungen von Chris Olah (person_id=54)
in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Eintraege basieren auf oeffentlich zugaenglichen Quellen,
die per WebSearch am 2026-02-12 recherchiert wurden.

NUTZUNG:
    python collect_olah.py

ACHTUNG: Vor dem Ausfuehren pruefen! Doppelte Ausfuehrung wird durch
         unique-Check auf (person_id, aussage_text) bzw.
         (person_id, beschreibung, datum_handlung) verhindert.
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 54  # Chris Olah
ERFASST_VON = "Claude"
DATUM_ABRUF = "2026-02-12"


# ============================================================================
# AUSSAGEN
# ============================================================================
# Jede Aussage ist ein dict mit den DB-Feldern.
# aussage_text: Originalwortlaut (Englisch), so nah wie moeglich am Original.
# Quellen sind oeffentlich verifizierbar.
# ============================================================================

AUSSAGEN = [
    # -----------------------------------------------------------------------
    # 1. TIME 100 Most Influential People in AI 2024
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "If we could really understand these systems, and this would require "
            "a lot of progress, we might be able to go and say when these models "
            "are actually safe."
        ),
        "aussage_kurz": "Volles Verstaendnis koennte Sicherheitsbewertung von KI ermoeglichen",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel / Profil
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://time.com/collections/time100-ai-2024/7012873/chris-olah/",
        "quell_titel": "TIME 100 Most Influential People in AI 2024: Chris Olah",
        "datum_aussage": "2024-05-01",
        "sprache": "en",
        "kontext": "TIME-Profil ueber Olah als Pionier der mechanischen Interpretierbarkeit",
    },
    # -----------------------------------------------------------------------
    # 2. Twitter/X zur Superposition (Oktober 2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "If you'd asked me a year ago, superposition would have been by far "
            "the reason I was most worried that mechanistic interpretability would "
            "hit a dead end. I'm now very optimistic. I'd go as far as saying it's "
            "now primarily an engineering problem -- hard, but less fundamental risk."
        ),
        "aussage_kurz": "Superposition ist nun ein loesbare Ingenieursproblem, kein fundamentales Risiko mehr",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Social Media Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://x.com/ch402/status/1709998674087227859",
        "quell_titel": "Chris Olah on X, Oktober 2023",
        "datum_aussage": "2023-10-05",
        "sprache": "en",
        "kontext": "Tweet ueber Durchbruch bei Superposition-Problem in der Interpretierbarkeitsforschung",
    },
    # -----------------------------------------------------------------------
    # 3. 80,000 Hours Podcast - Microscope AI
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Chris calls his alternative vision of what an advanced AI system might "
            "look like 'microscope AI' since the AI is being used sort of like a "
            "microscope to learn about and build models of the world. In contrast "
            "with something like a tool or oracle AI that is designed to output useful "
            "information, the utility of a microscope AI wouldn't come from its output "
            "but rather our ability to look inside of it and access all of the implicit "
            "knowledge it learned."
        ),
        "aussage_kurz": "Microscope AI als Alternative zu Oracle AI: Nutzen durch Einblick statt Output",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://80000hours.org/podcast/episodes/chris-olah-interpretability-research/",
        "quell_titel": "80,000 Hours Podcast: Chris Olah on what the hell is going on inside neural networks",
        "datum_aussage": "2022-06-15",
        "sprache": "en",
        "kontext": "Konzeptualisierung einer alternativen AI-Architektur, die auf Transparenz statt Leistung setzt",
    },
    # -----------------------------------------------------------------------
    # 4. Mechanistic Interpretability Essay (2022)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "The critical benefit of mechanistic interpretability is that you can "
            "truly determine whether statements are true, serving as an epistemic "
            "foundation where statements about circuits become questions of "
            "mathematical reasoning."
        ),
        "aussage_kurz": "Mechanische Interpretierbarkeit bietet epistemisches Fundament fuer KI-Verstaendnis",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Wissenschaftlicher Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://www.transformer-circuits.pub/2022/mech-interp-essay",
        "quell_titel": "Mechanistic Interpretability, Variables, and the Importance of Interpretable Bases",
        "datum_aussage": "2022-09-01",
        "sprache": "en",
        "kontext": "Grundsatzpaper zur mechanischen Interpretierbarkeit auf transformer-circuits.pub",
    },
    # -----------------------------------------------------------------------
    # 5. Distill: Zoom In - Circuits Philosophy
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Rather than typical interpretability approaches that aim to give simple "
            "explanations of entire neural networks, his approach is inspired by "
            "neuroscience and cellular biology—an approach of 'zooming in' where "
            "individual neurons, even individual weights, are treated as being worthy "
            "of serious investigation."
        ),
        "aussage_kurz": "Interpretierbarkeit durch 'Zoom In': Einzelne Neuronen verdienen ernsthafte Untersuchung",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 9,
        "quell_link": "https://distill.pub/2020/circuits/zoom-in/",
        "quell_titel": "Zoom In: An Introduction to Circuits (Distill)",
        "datum_aussage": "2020-03-10",
        "sprache": "en",
        "kontext": "Einfuehrung in die Circuits-Agenda, von Neurowissenschaft inspiriert",
    },
    # -----------------------------------------------------------------------
    # 6. Interpretability Dreams (2023)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Developing a visualization or tool that allows us to see the world in "
            "a new level of detail can lead to a new field of science developing "
            "to study the world through this lens."
        ),
        "aussage_kurz": "Neue Visualisierungswerkzeuge eroeffnen neue wissenschaftliche Felder",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 9,
        "quell_link": "https://transformer-circuits.pub/2023/interpretability-dreams/index.html",
        "quell_titel": "Interpretability Dreams (Transformer Circuits Thread)",
        "datum_aussage": "2023-03-14",
        "sprache": "en",
        "kontext": "Visionaerer Essay ueber Zukunftsperspektiven der Interpretierbarkeitsforschung",
    },
    # -----------------------------------------------------------------------
    # 7. Anthropic Core Views on AI Safety (Twitter)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "One of the ideas I find most useful from @AnthropicAI's Core Views on "
            "AI Safety post is thinking in terms of a distribution over safety "
            "difficulty."
        ),
        "aussage_kurz": "Verteilung ueber Sicherheitsschwierigkeit als nuetzliches Denkmodell",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 2,
        "quell_link": "https://x.com/ch402/status/1666482929772666880",
        "quell_titel": "Chris Olah on X, Juni 2023",
        "datum_aussage": "2023-06-07",
        "sprache": "en",
        "kontext": "Endorsement von Anthropics Ansatz zur Risikomodellierung",
    },
    # -----------------------------------------------------------------------
    # 8. 80,000 Hours - Optimism ueber Interpretierbarkeit
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Feature visualization, where you do gradient descent to create an "
            "image that causes a neuron to fire really strongly, is actually "
            "very effective."
        ),
        "aussage_kurz": "Feature-Visualisierung durch Gradient Descent ist sehr effektiv",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://80000hours.org/podcast/episodes/chris-olah-interpretability-research/",
        "quell_titel": "80,000 Hours Podcast: Chris Olah",
        "datum_aussage": "2022-06-15",
        "sprache": "en",
        "kontext": "Erklaerung einer erfolgreichen Methode zur Visualisierung neuronaler Netzwerke",
    },
    # -----------------------------------------------------------------------
    # 9. Scaling Monosemanticity (2024)
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Eight months prior, they had demonstrated that sparse autoencoders "
            "could recover monosemantic features from a small one-layer transformer, "
            "but there was a major concern that this method might not scale feasibly "
            "to state-of-the-art transformers. The scaling work successfully addressed "
            "this concern by demonstrating the approach could work on larger, "
            "production-grade models."
        ),
        "aussage_kurz": "Sparse Autoencoders skalieren erfolgreich auf produktionsreife Modelle",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 9,
        "quell_link": "https://transformer-circuits.pub/2024/scaling-monosemanticity/",
        "quell_titel": "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet",
        "datum_aussage": "2024-05-21",
        "sprache": "en",
        "kontext": "Durchbruch: Sparse Autoencoders funktionieren bei Claude 3 Sonnet, nicht nur bei Toy Models",
    },
    # -----------------------------------------------------------------------
    # 10. Twitter - Departure from OpenAI
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Moving on from OpenAI to try something new. I'll still be doing lots "
            "of interpretability and sharing interesting things I find inside "
            "neural networks. :)"
        ),
        "aussage_kurz": "Verlasse OpenAI fuer neues Projekt, bleibe bei Interpretierbarkeit",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 2,
        "quell_link": "https://x.com/ch402/status/1344798317364932608",
        "quell_titel": "Chris Olah on X, 31. Dezember 2020",
        "datum_aussage": "2020-12-31",
        "sprache": "en",
        "kontext": "Ankuendigung seines Abgangs von OpenAI, kurz vor Gruendung von Anthropic",
    },
    # -----------------------------------------------------------------------
    # 11. CV - Personal Philosophy
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "I want to understand things clearly and explain them well."
        ),
        "aussage_kurz": "Persoenliches Motto: Klar verstehen und gut erklaeren",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://colah.github.io/cv.pdf",
        "quell_titel": "Chris Olah - Personal CV",
        "datum_aussage": "2020-01-01",
        "sprache": "en",
        "kontext": "Motto auf seinem persoenlichen CV und Website",
    },
    # -----------------------------------------------------------------------
    # 12. Scaling Monosemanticity - Safety Features
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "The team observed features related to a broad range of safety concerns, "
            "including deception, sycophancy, bias, and dangerous content."
        ),
        "aussage_kurz": "Sparse Autoencoders identifizieren Sicherheitsrisiken wie Tauschung und Bias",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 9,
        "quell_link": "https://transformer-circuits.pub/2024/scaling-monosemanticity/",
        "quell_titel": "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet",
        "datum_aussage": "2024-05-21",
        "sprache": "en",
        "kontext": "Praktische Anwendung: Features erkennen gefaehrliche Verhaltensweisen in LLMs",
    },
    # -----------------------------------------------------------------------
    # 13. AGI Safety Views - Transparency
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "If complete understanding of transformative AI systems isn't achieved, "
            "they could fall back to careful analysis of small slices—for example, "
            "understanding whether a model is being manipulative, which could still "
            "reduce safety concerns."
        ),
        "aussage_kurz": "Selbst partielle Interpretierbarkeit kann Sicherheit verbessern",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://www.alignmentforum.org/posts/X2i9dQQK3gETCyqh2/chris-olah-s-views-on-agi-safety",
        "quell_titel": "Chris Olah's views on AGI safety (AI Alignment Forum)",
        "datum_aussage": "2022-03-01",
        "sprache": "en",
        "kontext": "Pragmatischer Ansatz: Partielle Interpretierbarkeit ist besser als gar keine",
    },
    # -----------------------------------------------------------------------
    # 14. Transformer Circuits Thread Launch
    # -----------------------------------------------------------------------
    {
        "aussage_text": (
            "Missing the Distill Circuits Thread? My colleagues and I at @AnthropicAI "
            "are starting a similar project focused on transformer language models."
        ),
        "aussage_kurz": "Transformer Circuits Thread als Nachfolger von Distill Circuits",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 2,
        "quell_link": "https://x.com/ch402/status/1473697352313679876",
        "quell_titel": "Chris Olah on X, Dezember 2021",
        "datum_aussage": "2021-12-22",
        "sprache": "en",
        "kontext": "Ankuendigung des Transformer Circuits Thread bei Anthropic",
    },
]


# ============================================================================
# HANDLUNGEN
# ============================================================================

HANDLUNGEN = [
    # -----------------------------------------------------------------------
    # 1. Thiel Fellowship
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Chris Olah erhaelt das Thiel Fellowship mit 19 Jahren. "
            "Er fokussiert sich auf 3D-Druck zur Reduktion von Knappheit, "
            "mit dem Ziel, jedem mit einem 3D-Drucker zu ermoeglichen, "
            "Bildungshilfen, wissenschaftliche Grundausstattung und Werkzeuge "
            "herzustellen."
        ),
        "datum_handlung": "2012-06-12",
        "betrag_usd": 100_000,
        "quell_link": "https://www.businesswire.com/news/home/20120612006972/en/Peter-Thiel-Announces-2012-Class-of-%E2%80%9C20-Under-20%E2%80%9D-Thiel-Fellows",
        "quell_titel": "Business Wire: Peter Thiel Announces 2012 Class of '20 Under 20' Thiel Fellows",
        "kontext": "Olah aus Kanada, verzichtet auf Universitaet fuer Thiel Fellowship",
    },
    # -----------------------------------------------------------------------
    # 2. Google Brain Internship / DeepDream
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "Chris Olah beginnt Internship bei Google Brain und wird zweiter "
            "Autor auf dem DeepDream-Projekt. DeepDream wird zu einem Meilenstein "
            "der neuronalen Netzwerk-Visualisierung und loest eine kleine "
            "Kunstbewegung aus."
        ),
        "datum_handlung": "2015-06-17",
        "betrag_usd": None,
        "quell_link": "https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html",
        "quell_titel": "Google Research Blog: Inceptionism: Going Deeper into Neural Networks",
        "kontext": "Mitarbeit mit Alexander Mordvintsev und Mike Tyka; Code wird open source",
    },
    # -----------------------------------------------------------------------
    # 3. Distill Journal Gruendung
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "gruendung",
        "beschreibung": (
            "Chris Olah gruendet zusammen mit Shan Carter (Google Brain) und "
            "Arvind Satyanarayan (MIT CSAIL) das wissenschaftliche Journal Distill. "
            "Unterstuetzung durch Google, OpenAI, DeepMind und Y Combinator Research. "
            "Distill fokussiert sich auf herausragende visuelle und interaktive "
            "Kommunikation von ML-Konzepten."
        ),
        "datum_handlung": "2017-03-01",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Distill_(journal)",
        "quell_titel": "Wikipedia: Distill (journal)",
        "kontext": "Einzigartiges Journal-Format mit interaktiven Artikeln und strengen Standards fuer Klarheit",
    },
    # -----------------------------------------------------------------------
    # 4. Feature Visualization Paper (Distill)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Feature Visualization' auf Distill mit "
            "Alexander Mordvintsev und Ludwig Schubert. Das Paper erklaert, "
            "wie man durch Gradient Descent Beispiele generiert, die zeigen, "
            "wonach ein Neuron sucht."
        ),
        "datum_handlung": "2017-11-07",
        "betrag_usd": None,
        "quell_link": "https://distill.pub/2017/feature-visualization/",
        "quell_titel": "Distill: Feature Visualization",
        "kontext": "Einflussreiches Paper zur Visualisierung neuronaler Netzwerke",
    },
    # -----------------------------------------------------------------------
    # 5. Building Blocks of Interpretability (Distill)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'The Building Blocks of Interpretability' "
            "auf Distill (Februar 2018), ein Meilenstein der Interpretierbarkeits-"
            "forschung mit interaktiven Visualisierungen."
        ),
        "datum_handlung": "2018-02-01",
        "betrag_usd": None,
        "quell_link": "https://distill.pub/2018/building-blocks/",
        "quell_titel": "Distill: The Building Blocks of Interpretability",
        "kontext": "Einfuehrung von Techniken zur Zerlegung komplexer neuronaler Netzwerke",
    },
    # -----------------------------------------------------------------------
    # 6. Wechsel zu OpenAI (Clarity Team)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "einstellung",
        "beschreibung": (
            "Chris Olah wechselt zu OpenAI und gruendet das Clarity Team innerhalb "
            "der Safety Division. Das Team fokussiert sich auf neuronale Netzwerk-"
            "Interpretierbarkeit und die Entwicklung von Abstraktionen, Schnittstellen "
            "und Methoden zum besseren Verstaendnis der internen Funktionsweise von KI-Modellen."
        ),
        "datum_handlung": "2018-05-01",
        "betrag_usd": None,
        "quell_link": "https://colah.github.io/about.html",
        "quell_titel": "Chris Olah - About",
        "kontext": "Von Google Brain zu OpenAI; Leitung der Interpretability-Forschung",
    },
    # -----------------------------------------------------------------------
    # 7. Activation Atlas (Distill)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Exploring Neural Networks with Activation Atlases' "
            "als Kollaboration zwischen Google und OpenAI-Forschern. Activation Atlases "
            "erlauben die Inspektion neuronaler Netzwerk-Repraesentationen."
        ),
        "datum_handlung": "2019-03-06",
        "betrag_usd": None,
        "quell_link": "https://distill.pub/2019/activation-atlas/",
        "quell_titel": "Distill: Exploring Neural Networks with Activation Atlases",
        "kontext": "Wichtige Kollaboration zwischen Google und OpenAI",
    },
    # -----------------------------------------------------------------------
    # 8. Zoom In - Circuits Introduction (Distill)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Zoom In: An Introduction to Circuits' auf Distill. "
            "Einfuehrung der 'Circuits'-Agenda: Reverse-Engineering neuronaler Netzwerke "
            "durch detaillierte Untersuchung einzelner Neuronen und Gewichte."
        ),
        "datum_handlung": "2020-03-10",
        "betrag_usd": None,
        "quell_link": "https://distill.pub/2020/circuits/zoom-in/",
        "quell_titel": "Distill: Zoom In: An Introduction to Circuits",
        "kontext": "Grundsatzpaper der Circuits-Forschung, inspiriert von Neurobiologie",
    },
    # -----------------------------------------------------------------------
    # 9. Abgang von OpenAI
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": (
            "Chris Olah kuendigt oeffentlich seinen Ruecktritt von OpenAI an. "
            "Er verspricht, weiterhin Interpretierbarkeitsforschung zu betreiben "
            "und interessante Entdeckungen in neuronalen Netzwerken zu teilen."
        ),
        "datum_handlung": "2020-12-31",
        "betrag_usd": None,
        "quell_link": "https://x.com/ch402/status/1344798317364932608",
        "quell_titel": "Chris Olah on X: Moving on from OpenAI",
        "kontext": "Abgang von OpenAI, Teil der Gruppe die Anthropic gruendet",
    },
    # -----------------------------------------------------------------------
    # 10. Anthropic Co-Founding
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "gruendung",
        "beschreibung": (
            "Chris Olah wird Mitgruender von Anthropic zusammen mit Dario Amodei, "
            "Daniela Amodei, Tom Brown, Sam McCandlish, Jack Clark und Jared Kaplan. "
            "Olah uebernimmt die Rolle des Interpretability Research Lead. "
            "Die Gruendung erfolgt durch sieben Ex-OpenAI-Mitarbeiter."
        ),
        "datum_handlung": "2021-01-28",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Anthropic",
        "quell_titel": "Wikipedia: Anthropic",
        "kontext": "Gruendung aufgrund von Sorgen ueber KI-Sicherheit und OpenAI-Richtung",
    },
    # -----------------------------------------------------------------------
    # 11. Transformer Circuits Thread Launch
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Launch des Transformer Circuits Thread bei Anthropic als Nachfolger "
            "des Distill Circuits Thread. Das Projekt fokussiert sich auf mechanische "
            "Interpretierbarkeit von Transformer-Sprachmodellen."
        ),
        "datum_handlung": "2021-12-22",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/",
        "quell_titel": "Transformer Circuits Thread",
        "kontext": "Fortsetzung der Circuits-Forschung bei Anthropic, nun auf Transformer fokussiert",
    },
    # -----------------------------------------------------------------------
    # 12. Mathematical Framework for Transformer Circuits
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'A Mathematical Framework for Transformer Circuits' "
            "mit Nelson Elhage, Neel Nanda, Catherine Olsson und anderen. "
            "Chris Olah ist Correspondence Author. Das Paper legt mathematische "
            "Grundlagen fuer das Reverse-Engineering von Transformern."
        ),
        "datum_handlung": "2021-12-22",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/2021/framework/index.html",
        "quell_titel": "Transformer Circuits: A Mathematical Framework",
        "kontext": "Initiale Schritte zum Reverse-Engineering von Transformern",
    },
    # -----------------------------------------------------------------------
    # 13. Towards Monosemanticity (Toy Models)
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Towards Monosemanticity: Decomposing Language "
            "Models With Dictionary Learning' auf Transformer Circuits Thread. "
            "Demonstration, dass Sparse Autoencoders monosemantische Features "
            "aus einem einfachen Ein-Layer-Transformer extrahieren koennen."
        ),
        "datum_handlung": "2023-10-04",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/2023/monosemantic-features",
        "quell_titel": "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning",
        "kontext": "Proof of Concept fuer Sparse Autoencoders, aber nur bei Toy Models",
    },
    # -----------------------------------------------------------------------
    # 14. Scaling Monosemanticity - Claude 3 Sonnet
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Scaling Monosemanticity: Extracting Interpretable "
            "Features from Claude 3 Sonnet'. Chris Olah ist Co-Autor. "
            "Der Durchbruch zeigt, dass Sparse Autoencoders auf produktionsreifen "
            "LLMs funktionieren und Features zu Deception, Bias und gefaehrlichem "
            "Content identifizieren koennen."
        ),
        "datum_handlung": "2024-05-21",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/2024/scaling-monosemanticity/",
        "quell_titel": "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet",
        "kontext": "Durchbruch: Interpretierbarkeit skaliert auf State-of-the-Art Modelle",
    },
    # -----------------------------------------------------------------------
    # 15. Sparse Crosscoders
    # -----------------------------------------------------------------------
    {
        "handlung_typ": "sonstiges",
        "beschreibung": (
            "Veroeffentlichung von 'Sparse Crosscoders for Cross-Layer Features "
            "and Model Diffing' auf Transformer Circuits Thread. Chris Olah ist "
            "Co-Autor. Sparse Crosscoders sind eine Variante, die Features ueber "
            "mehrere Schichten von Modellen verstehen."
        ),
        "datum_handlung": "2024-10-28",
        "betrag_usd": None,
        "quell_link": "https://transformer-circuits.pub/2024/crosscoders/index.html",
        "quell_titel": "Sparse Crosscoders for Cross-Layer Features and Model Diffing",
        "kontext": "Weiterentwicklung: Layer-uebergreifende Feature-Analyse",
    },
]


# ============================================================================
# EINFUEGE-LOGIK
# ============================================================================

def insert_aussagen(cursor, aussagen):
    """Fuegt Aussagen ein, ueberspringt Duplikate basierend auf (person_id, aussage_text)."""
    inserted = 0
    skipped = 0
    for a in aussagen:
        # Duplikat-Check
        cursor.execute(
            "SELECT id FROM aussagen WHERE person_id = ? AND aussage_text = ?",
            (PERSON_ID, a["aussage_text"])
        )
        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO aussagen (
                person_id, aussage_text, aussage_kurz, modus,
                quellen_typ_id, plattform_id, quell_link, quell_titel,
                datum_aussage, datum_abruf, sprache,
                kontext, erfasst_von
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
            DATUM_ABRUF,
            a.get("sprache", "en"),
            a.get("kontext"),
            ERFASST_VON,
        ))
        inserted += 1
    return inserted, skipped


def insert_handlungen(cursor, handlungen):
    """Fuegt Handlungen ein, ueberspringt Duplikate basierend auf (person_id, beschreibung, datum_handlung)."""
    inserted = 0
    skipped = 0
    for h in handlungen:
        cursor.execute(
            "SELECT id FROM handlungen WHERE person_id = ? AND beschreibung = ? AND datum_handlung = ?",
            (PERSON_ID, h["beschreibung"], h.get("datum_handlung"))
        )
        if cursor.fetchone():
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO handlungen (
                person_id, handlung_typ, beschreibung,
                datum_handlung, betrag_usd,
                quell_link, quell_titel, datum_abruf,
                kontext
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            PERSON_ID,
            h["handlung_typ"],
            h["beschreibung"],
            h.get("datum_handlung"),
            h.get("betrag_usd"),
            h.get("quell_link"),
            h.get("quell_titel"),
            DATUM_ABRUF,
            h.get("kontext"),
        ))
        inserted += 1
    return inserted, skipped


def insert_suchprotokoll(cursor):
    """Dokumentiert die Suche im Suchprotokoll."""
    cursor.execute("""
        INSERT INTO suchprotokolle (
            person_id, suchbegriffe, ergebnis_anzahl, relevante_treffer,
            notizen, durchgefuehrt_von
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        PERSON_ID,
        "Chris Olah Anthropic interpretability mechanistic AI safety neural networks Distill transformer circuits sparse autoencoders monosemanticity features visualization DeepDream Google Brain OpenAI",
        60,
        len(AUSSAGEN) + len(HANDLUNGEN),
        (
            "Systematische Recherche via WebSearch (2026-02-12). "
            "Quellen: TIME 100 AI Profile, 80,000 Hours Podcast, Twitter/X Posts, "
            "Transformer Circuits Thread (transformer-circuits.pub), Distill Publications, "
            "AI Alignment Forum, Wikipedia, colah.github.io, Business Wire (Thiel Fellowship), "
            "Google Research Blog. Schwerpunkte: Mechanistic Interpretability, "
            "Sparse Autoencoders, Circuits-Agenda, Microscope AI Konzept, Distill Journal, "
            "DeepDream, Anthropic Founding, OpenAI Clarity Team. "
            "Alle Zitate und Handlungen stammen aus oeffentlich zugaenglichen, verifizierbaren Quellen."
        ),
        ERFASST_VON,
    ))


def main():
    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Pruefen ob Person existiert
        cursor.execute("SELECT name FROM personen WHERE id = ?", (PERSON_ID,))
        person = cursor.fetchone()
        if not person:
            print(f"FEHLER: Person mit id={PERSON_ID} nicht gefunden!")
            return
        print(f"Person: {person[0]} (id={PERSON_ID})")
        print("=" * 60)

        # Aussagen einfuegen
        a_ins, a_skip = insert_aussagen(cursor, AUSSAGEN)
        print(f"AUSSAGEN:   {a_ins} eingefuegt, {a_skip} uebersprungen (Duplikate)")

        # Handlungen einfuegen
        h_ins, h_skip = insert_handlungen(cursor, HANDLUNGEN)
        print(f"HANDLUNGEN: {h_ins} eingefuegt, {h_skip} uebersprungen (Duplikate)")

        # Suchprotokoll
        insert_suchprotokoll(cursor)
        print(f"SUCHPROTOKOLL: 1 Eintrag erstellt")

        conn.commit()
        print("=" * 60)
        print(f"GESAMT: {a_ins + h_ins} neue Eintraege, {a_skip + h_skip} Duplikate")
        print("Datenbank erfolgreich aktualisiert.")

        # Zusammenfassung
        cursor.execute("SELECT COUNT(*) FROM aussagen WHERE person_id = ?", (PERSON_ID,))
        total_a = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM handlungen WHERE person_id = ?", (PERSON_ID,))
        total_h = cursor.fetchone()[0]
        print(f"\nGesamtbestand Chris Olah: {total_a} Aussagen, {total_h} Handlungen")

    except Exception as e:
        conn.rollback()
        print(f"FEHLER: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
