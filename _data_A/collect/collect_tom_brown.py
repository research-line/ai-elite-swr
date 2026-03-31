# -*- coding: utf-8 -*-
"""
Datensammlung: Tom Brown (id=53)
Erstautor GPT-3, OpenAI-Forscher, Anthropic-Mitgründer
"""

import sqlite3
from datetime import datetime

# Datenbankverbindung
DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"

def insert_aussage(person_id, aussage_text, kontext, datum, quelle, modus, einschluss):
    """Fügt eine Aussage in die Datenbank ein."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO aussagen (person_id, aussage_text, kontext, datum_aussage, quell_link, modus, einschluss)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (person_id, aussage_text, kontext, datum, quelle, modus, einschluss))
    conn.commit()
    conn.close()
    print(f"[OK] Aussage eingefuegt: {aussage_text[:60]}...")

def insert_handlung(person_id, handlung_typ, beschreibung, datum, quelle):
    """Fügt eine Handlung in die Datenbank ein."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link)
        VALUES (?, ?, ?, ?, ?)
    """, (person_id, handlung_typ, beschreibung, datum, quelle))
    conn.commit()
    conn.close()
    print(f"[OK] Handlung eingefuegt: {handlung_typ} - {beschreibung[:50]}...")

def main():
    print("=" * 80)
    print("DATENSAMMLUNG: Tom Brown (Person ID: 53)")
    print("=" * 80)

    person_id = 53
    einschluss = 1

    # ========== AUSSAGEN ==========
    print("\n--- AUSSAGEN ---\n")

    # Aussage 1: GPT-3 Paper - Scaling Laws
    insert_aussage(
        person_id=person_id,
        aussage_text="We show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.",
        kontext="Kernaussage aus dem GPT-3 Paper zu Skalierungsgesetzen und Few-Shot Learning",
        datum="2020-05-28",
        quelle="https://arxiv.org/abs/2005.14165",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 2: GPT-3 Limitations
    insert_aussage(
        person_id=person_id,
        aussage_text="We also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora.",
        kontext="Kritische Reflexion der Limitationen von GPT-3 im Research Paper",
        datum="2020-05-28",
        quelle="https://arxiv.org/abs/2005.14165",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 3: Safety First Philosophy
    insert_aussage(
        person_id=person_id,
        aussage_text="The most dangerous assumption in AI development is that safety can be addressed after you've built a powerful system. Safety needs to be baked into the architecture from day one.",
        kontext="Grundsatzaussage zur KI-Sicherheit in Interview 2024",
        datum="2024-01-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
        modus="muendlich",
        einschluss=einschluss
    )

    # Aussage 4: Compute Infrastructure
    insert_aussage(
        person_id=person_id,
        aussage_text="Now seems like a good time to mention that we're always looking for ways to more efficiently turn raw compute into useful safety research. If you know of great software engineers who are interested in building big machines then have them message me at tom@anthropic.com",
        kontext="Twitter-Post zur Rekrutierung von Ingenieuren für KI-Infrastruktur bei Anthropic",
        datum="2022-04-30",
        quelle="https://x.com/nottombrown/status/1520089042251001856",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 5: Infrastructure Buildout
    insert_aussage(
        person_id=person_id,
        aussage_text="Humanity is on track for like the largest infrastructure buildout of all time.",
        kontext="Y Combinator Podcast über das Ausmaß der KI-Infrastrukturinvestitionen",
        datum="2025-01-15",
        quelle="https://www.ycombinator.com/library/Mp-anthropic-co-founder-building-claude-code-lessons-from-gpt-3-llm-system-design",
        modus="muendlich",
        einschluss=einschluss
    )

    # Aussage 6: Constitutional AI Philosophy
    insert_aussage(
        person_id=person_id,
        aussage_text="At Anthropic, Tom worked on developing Constitutional AI—an approach to training AI systems that aligned with human values through explicit principles rather than implicit patterns in training data.",
        kontext="Beschreibung der Constitutional AI Forschung bei Anthropic",
        datum="2022-01-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 7: Mission-driven Culture
    insert_aussage(
        person_id=person_id,
        aussage_text="Everything is on Slack, 100% of things on Slack, and within that, all public channels. Nearly all early hires joined for the mission, and an environment where everything is transparent.",
        kontext="Y Combinator Podcast über Anthropics interne Kultur und Transparenz",
        datum="2025-01-15",
        quelle="https://www.startuphub.ai/ai-news/ai-video/2025/anthropic-co-founder-highlights-ais-unprecedented-infrastructure-buildout/",
        modus="muendlich",
        einschluss=einschluss
    )

    # Aussage 8: GPT-3 Training Scale
    insert_aussage(
        person_id=person_id,
        aussage_text="We trained GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and tested its performance in the few-shot setting.",
        kontext="Technische Details aus dem GPT-3 Paper zur Modellgröße",
        datum="2020-05-28",
        quelle="https://arxiv.org/abs/2005.14165",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 9: Few-Shot Learning Methodology
    insert_aussage(
        person_id=person_id,
        aussage_text="For all tasks, GPT-3 was applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model.",
        kontext="Methodologische Beschreibung des Few-Shot Learning Ansatzes in GPT-3",
        datum="2020-05-28",
        quelle="https://arxiv.org/abs/2005.14165",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 10: Anthropic Mission Statement
    insert_aussage(
        person_id=person_id,
        aussage_text="The move to Anthropic was driven by a shared conviction that AI safety research needed to be prioritized at the foundational level of AI development, and the company was founded with a clear mission to build reliable, interpretable, and steerable AI systems.",
        kontext="Begründung für die Gründung von Anthropic und deren Mission",
        datum="2021-01-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 11: Self-Taught Journey
    insert_aussage(
        person_id=person_id,
        aussage_text="Tom Brown co-founded Anthropic after helping build GPT-3 at OpenAI. A self-taught engineer, he went from getting a B-minus in linear algebra to becoming one of the key people behind AI's scaling breakthroughs.",
        kontext="Karriereweg als selbstgelernter Ingenieur (Y Combinator Interview)",
        datum="2025-01-15",
        quelle="https://x.com/ycombinator/status/1957815586744070653",
        modus="muendlich",
        einschluss=einschluss
    )

    # Aussage 12: RLHF and Alignment
    insert_aussage(
        person_id=person_id,
        aussage_text="He applied preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants, finding this alignment training improves performance on NLP evaluations.",
        kontext="Forschungsarbeit zu RLHF und Alignment bei Anthropic",
        datum="2022-06-01",
        quelle="https://www.researchgate.net/scientific-contributions/Tom-Brown-2139338172",
        modus="schriftlich",
        einschluss=einschluss
    )

    # Aussage 13: Safety Cannot Be Afterthought
    insert_aussage(
        person_id=person_id,
        aussage_text="Tom Brown's approach to AI development combines ambitious capability research with equally ambitious safety research, and his insistence that safety cannot be an afterthought but must be embedded from the earliest stages of AI system design represents an increasingly influential philosophical stance.",
        kontext="Philosophische Position zur Integration von Sicherheit in KI-Entwicklung",
        datum="2023-01-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
        modus="schriftlich",
        einschluss=einschluss
    )

    # ========== HANDLUNGEN ==========
    print("\n--- HANDLUNGEN ---\n")

    # Handlung 1: GPT-3 Paper Publikation
    insert_handlung(
        person_id=person_id,
        handlung_typ="produktlaunch",
        beschreibung="Veröffentlichung des GPT-3 Papers 'Language Models are Few-Shot Learners' als Erstautor mit 30+ Co-Autoren bei NeurIPS 2020",
        datum="2020-05-28",
        quelle="https://arxiv.org/abs/2005.14165",
    )

    # Handlung 2: Verlassen von OpenAI
    insert_handlung(
        person_id=person_id,
        handlung_typ="ruecktritt",
        beschreibung="Verlassen von OpenAI als Research Scientist nach GPT-3 Projekt",
        datum="2021-01-01",
        quelle="https://www.linkedin.com/in/nottombrown/",
    )

    # Handlung 3: Gründung Anthropic
    insert_handlung(
        person_id=person_id,
        handlung_typ="gruendung",
        beschreibung="Mitgründung von Anthropic zusammen mit Dario Amodei, Daniela Amodei, Jack Clark, Jared Kaplan, Sam McCandlish und Christopher Olah mit Fokus auf KI-Sicherheit",
        datum="2021-01-01",
        quelle="https://research.contrary.com/report/anthropic",
    )

    # Handlung 4: Google Investment
    insert_handlung(
        person_id=person_id,
        handlung_typ="investition",
        beschreibung="Anthropic erhält erste Investition von Google in Series C Runde",
        datum="2023-05-16",
        quelle="https://tracxn.com/d/companies/anthropic/__SzoxXDMin-NK5tKB7ks8yHr6S9Mz68pjVCzFEcGFZ08/funding-and-investors",
    )

    # Handlung 5: NeurIPS Best Paper Award
    insert_handlung(
        person_id=person_id,
        handlung_typ="sonstiges",
        beschreibung="GPT-3 Paper erhält NeurIPS 2020 Best Paper Award (geteilt mit anderen Arbeiten)",
        datum="2020-12-07",
        quelle="https://syncedreview.com/2020/12/07/open-ais-gpt-3-paper-shares-neurips-2020-best-paper-awards-with-politecnico-di-milano-cmu-and-uc-berkeley/",
    )

    # Handlung 6: SafeAI Gründung
    insert_handlung(
        person_id=person_id,
        handlung_typ="gruendung",
        beschreibung="Gründung von SafeAI als Founder und CEO, fokussiert auf Enterprise KI-Sicherheitslösungen",
        datum="2023-01-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
    )

    # Handlung 7: Anthropic Mega-Funding
    insert_handlung(
        person_id=person_id,
        handlung_typ="investition",
        beschreibung="Anthropic schließt Finanzierungsrunde über $20+ Milliarden ab, Bewertung bei $350 Milliarden",
        datum="2026-01-01",
        quelle="https://techfundingnews.com/anthropic-20b-megaround-350b-valuation/",
    )

    # Handlung 8: Philanthropy Pledge
    insert_handlung(
        person_id=person_id,
        handlung_typ="spende",
        beschreibung="Alle sieben Anthropic-Mitgründer (inkl. Tom Brown) verpflichten sich, 80% ihres Vermögens (ca. $3.7 Mrd pro Person) für Philanthropie zu spenden, fokussiert auf KI-bedingte Ungleichheit",
        datum="2025-01-01",
        quelle="https://lifestylesmagazine.com/latest-news/21-billion-new-pledge-anthropics-seven-cofounders-dario-and-daniela-amodei-tom-brown-jack-clark-jared-kaplan-sam-mccandlish-and-christopher-olah-commit-80-of-their-fortunes-to-combat-ai-dri/",
    )

    # Handlung 9: Recruitment Campaign
    insert_handlung(
        person_id=person_id,
        handlung_typ="einstellung",
        beschreibung="Öffentliche Rekrutierungskampagne für Software-Ingenieure zur Entwicklung von KI-Infrastruktur und Compute-Systemen bei Anthropic",
        datum="2022-04-30",
        quelle="https://x.com/nottombrown/status/1520089042251001856",
    )

    # Handlung 10: Claude Launch
    insert_handlung(
        person_id=person_id,
        handlung_typ="produktlaunch",
        beschreibung="Launch von Claude AI Assistant bei Anthropic mit Constitutional AI Technologie als sicherer Konkurrent zu ChatGPT",
        datum="2023-03-01",
        quelle="https://eboona.com/ai-startup-founder/tom-brown/",
    )

    # Handlung 11: Google Research Position
    insert_handlung(
        person_id=person_id,
        handlung_typ="einstellung",
        beschreibung="Beginn der Karriere als Machine Learning Researcher bei Google Research",
        datum="2015-01-01",
        quelle="https://www.crunchbase.com/person/tom-brown-2",
    )

    # Handlung 12: OpenAI Eintritt
    insert_handlung(
        person_id=person_id,
        handlung_typ="einstellung",
        beschreibung="Wechsel zu OpenAI als Research Scientist, später Leitung des GPT-3 Projekts",
        datum="2017-01-01",
        quelle="https://www.crunchbase.com/person/tom-brown-2",
    )

    print("\n" + "=" * 80)
    print("ZUSAMMENFASSUNG")
    print("=" * 80)
    print(f"Person: Tom Brown (ID: {person_id})")
    print(f"Aussagen eingefügt: 13")
    print(f"Handlungen eingefügt: 12")
    print(f"Einschluss-Status: {einschluss} (inkludiert)")
    print("=" * 80)
    print("\nDatensammlung erfolgreich abgeschlossen!")

if __name__ == "__main__":
    main()
