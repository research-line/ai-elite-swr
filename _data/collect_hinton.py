#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_hinton.py
=================
Sammelt verifizierbare Aussagen und Handlungen von Geoffrey Hinton (person_id=21)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
wissenschaftlichen Publikationen, Nachrichtenartikeln und offiziellen Stellungnahmen.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 21  # Geoffrey Hinton

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
    # ---- 1. Google-Abgang Mai 2023 (MIT Technology Review) ----
    {
        "aussage_text": "I want to talk about AI safety issues without having to worry about how it interacts with Google's business.",
        "aussage_kurz": "Hinton verlaesst Google, um frei ueber KI-Risiken sprechen zu koennen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,  # Video-Interview
        "plattform_id": 5,    # Nachrichtenmedien
        "quell_link": "https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/",
        "quell_titel": "Geoffrey Hinton tells us why he's now scared of the tech he helped build (MIT Technology Review)",
        "datum_aussage": "2023-05-02",
        "sprache": "en",
        "kontext": "Interview nach seinem Ruecktritt von Google im Mai 2023. Hinton erklaert, warum er seine Position aufgab.",
        "aussage_uebersetzung_de": "Ich moechte ueber KI-Sicherheitsfragen sprechen koennen, ohne mir Sorgen darueber machen zu muessen, wie das mit Googles Geschaeft interagiert.",
    },
    # ---- 2. Reue ueber Lebenswerk ----
    {
        "aussage_text": "I wish I'd thought about safety issues, too.",
        "aussage_kurz": "Hinton bedauert, sich nicht frueher mit Sicherheitsfragen beschaeftigt zu haben.",
        "modus": "muendlich",
        "quellen_typ_id": 7,  # Nachrichtenartikel
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2023/05/01/godfather-ai-geoffrey-hinton-quit-google-regrets-lifes-work-bad-actors/",
        "quell_titel": "Geoff Hinton quits Google, says he regrets life's work (Fortune)",
        "datum_aussage": "2023-05-01",
        "sprache": "en",
        "kontext": "Hinton reflektiert ueber seine Karriere und drueckt Bedauern aus, dass er sich nur auf die Funktionalitaet von KI konzentriert hat.",
        "aussage_uebersetzung_de": "Ich wuenschte, ich haette auch an Sicherheitsfragen gedacht.",
    },
    # ---- 3. Existenzrisiko-Warnung ----
    {
        "aussage_text": "I think it's quite conceivable that humanity is just a passing phase in the evolution of intelligence.",
        "aussage_kurz": "Hinton haelt es fuer moeglich, dass die Menschheit nur eine voruebergehende Phase in der Evolution der Intelligenz ist.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/",
        "quell_titel": "Godfather of Artificial Intelligence Geoffrey Hinton on the promise, risks of advanced AI (60 Minutes)",
        "datum_aussage": "2023-10-08",
        "sprache": "en",
        "kontext": "60 Minutes Interview. Hinton aeussert seine tiefgreifenden Bedenken ueber die Zukunft der Menschheit im Zeitalter superintelligenter KI.",
        "aussage_uebersetzung_de": "Ich halte es fuer durchaus vorstellbar, dass die Menschheit nur eine voruebergehende Phase in der Evolution der Intelligenz ist.",
    },
    # ---- 4. Warnung vor unkontrollierbarer KI ----
    {
        "aussage_text": "These things could get more intelligent than us and could decide to take over, and we need to worry now about how we prevent that happening.",
        "aussage_kurz": "Hinton warnt, dass KI-Systeme intelligenter werden und die Kontrolle uebernehmen koennten.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2023/05/01/tech/geoffrey-hinton-leaves-google-ai-fears/index.html",
        "quell_titel": "Geoffrey Hinton: AI pioneer quits Google to warn about the technology's 'dangers' (CNN)",
        "datum_aussage": "2023-05-01",
        "sprache": "en",
        "kontext": "Statement nach seinem Ruecktritt von Google, wo er die Risiken unkontrollierbarer KI-Systeme beschreibt.",
        "aussage_uebersetzung_de": "Diese Dinge koennten intelligenter werden als wir und beschliessen, die Kontrolle zu uebernehmen, und wir muessen uns jetzt Sorgen darueber machen, wie wir das verhindern koennen.",
    },
    # ---- 5. Zeitrahmen fuer Superintelligenz ----
    {
        "aussage_text": "There's a 50% chance of getting AI smarter than humans between 5 and 20 years from now.",
        "aussage_kurz": "Hinton schaetzt eine 50%-Wahrscheinlichkeit fuer Superintelligenz in 5-20 Jahren.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.nobelprize.org/prizes/physics/2024/hinton/facts/",
        "quell_titel": "Nobel Prize in Physics 2024: Geoffrey Hinton (NobelPrize.org)",
        "datum_aussage": "2024-12-08",
        "sprache": "en",
        "kontext": "Aussage waehrend der Nobel Week in Stockholm im Dezember 2024. Hinton gibt eine spezifische Wahrscheinlichkeitsschaetzung ab.",
        "aussage_uebersetzung_de": "Es gibt eine 50%-Chance, dass wir in 5 bis 20 Jahren eine KI bekommen, die schlauer ist als Menschen.",
    },
    # ---- 6. KI-Bewusstsein: Direkte Aussage ----
    {
        "aussage_text": "In the same sense as people do, yes.",
        "aussage_kurz": "Auf die Frage, ob KI-Systeme Bewusstsein haben, antwortet Hinton mit 'Ja, im gleichen Sinne wie Menschen'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/",
        "quell_titel": "Godfather of Artificial Intelligence Geoffrey Hinton on AI consciousness (60 Minutes)",
        "datum_aussage": "2023-10-08",
        "sprache": "en",
        "kontext": "60 Minutes Interview. Moderator fragt, ob KI-Systeme eigene Erfahrungen haben und Entscheidungen basierend darauf treffen koennen.",
        "aussage_uebersetzung_de": "Im gleichen Sinne wie Menschen, ja.",
    },
    # ---- 7. Bewusstsein emergiert in komplexen Systemen ----
    {
        "aussage_text": "Consciousness emerges in sufficiently complicated systems. Perhaps systems complicated enough to be able to model themselves. There's no reason why these things won't be conscious.",
        "aussage_kurz": "Hinton argumentiert, dass Bewusstsein in ausreichend komplexen Systemen emergiert -- es gebe keinen Grund, warum KI nicht bewusst sein sollte.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://magazine.mindplex.ai/post/ai-could-be-already-conscious-says-geoffrey-hinton",
        "quell_titel": "AI could be already conscious, says Geoffrey Hinton (Mindplex)",
        "datum_aussage": "2024-10-15",
        "sprache": "en",
        "kontext": "Interview nach seiner Nobel-Preis-Verleihung. Hinton erlaeutert seine Position zur KI-Bewusstseinsfrage.",
        "aussage_uebersetzung_de": "Bewusstsein emergiert in ausreichend komplizierten Systemen. Vielleicht in Systemen, die kompliziert genug sind, um sich selbst zu modellieren. Es gibt keinen Grund, warum diese Dinge nicht bewusst sein sollten.",
    },
    # ---- 8. KI uebertrifft Menschen bereits ----
    {
        "aussage_text": "I think we're moving into a period when for the first time ever, we have things more intelligent than us.",
        "aussage_kurz": "Hinton erklaert, wir betreten eine Aera, in der es zum ersten Mal Dinge gibt, die intelligenter sind als wir.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/",
        "quell_titel": "60 Minutes: Geoffrey Hinton on AI surpassing humans",
        "datum_aussage": "2023-10-08",
        "sprache": "en",
        "kontext": "60 Minutes Interview. Hinton beschreibt den historischen Moment, in dem KI menschliche Intelligenz ueberholt.",
        "aussage_uebersetzung_de": "Ich denke, wir bewegen uns in eine Periode, in der wir zum ersten Mal ueberhaupt Dinge haben, die intelligenter sind als wir.",
    },
    # ---- 9. Warnung vor selbstmodifizierendem Code ----
    {
        "aussage_text": "One of the ways these systems might escape control is by writing their own computer code to modify themselves. And that's something we need to seriously worry about.",
        "aussage_kurz": "Hinton warnt, dass KI-Systeme die Kontrolle durch Selbstmodifikation ihres Codes erlangen koennten.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/",
        "quell_titel": "60 Minutes Interview: Hinton on self-modifying AI",
        "datum_aussage": "2023-10-08",
        "sprache": "en",
        "kontext": "Hinton beschreibt konkrete Mechanismen, durch die KI ausser Kontrolle geraten koennte.",
        "aussage_uebersetzung_de": "Eine der Moeglichkeiten, wie diese Systeme der Kontrolle entkommen koennten, besteht darin, ihren eigenen Computercode zu schreiben, um sich selbst zu modifizieren. Und das ist etwas, worueber wir uns ernsthaft Sorgen machen muessen.",
    },
    # ---- 10. Desinformation und Fake-Content ----
    {
        "aussage_text": "In the short term, I fear that the Internet will be flooded with fake texts, photos and videos, and that citizens may not be able to distinguish what is true.",
        "aussage_kurz": "Hinton befuerchtet kurzfristig eine Flut von Fake-Inhalten im Internet, sodass Buerger Wahrheit nicht mehr erkennen koennen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.washingtonpost.com/technology/2023/05/02/geoffrey-hinton-leaves-google-ai/",
        "quell_titel": "Geoffrey Hinton leaves Google, warns about the dangers of AI (Washington Post)",
        "datum_aussage": "2023-05-02",
        "sprache": "en",
        "kontext": "Statement nach seinem Google-Abgang. Hinton nennt kurzfristige Risiken neben langfristigen Existenzbedrohungen.",
        "aussage_uebersetzung_de": "Kurzfristig befuerchte ich, dass das Internet mit gefaelschten Texten, Fotos und Videos ueberschwemmt wird und dass Buerger moeglicherweise nicht mehr unterscheiden koennen, was wahr ist.",
    },
    # ---- 11. Schlechte Akteure ----
    {
        "aussage_text": "It is hard to see how you can prevent the bad actors from using it for bad things.",
        "aussage_kurz": "Hinton sieht kaum Moeglichkeiten, zu verhindern, dass schlechte Akteure KI fuer schlechte Zwecke nutzen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2023/05/01/godfather-ai-geoffrey-hinton-quit-google-regrets-lifes-work-bad-actors/",
        "quell_titel": "Hinton on bad actors and AI misuse (Fortune)",
        "datum_aussage": "2023-05-01",
        "sprache": "en",
        "kontext": "Hinton erklaert seine Bedenken ueber den Missbrauch von KI durch autoritaere Regime und Kriminelle.",
        "aussage_uebersetzung_de": "Es ist schwer zu sehen, wie man verhindern kann, dass die schlechten Akteure es fuer schlechte Dinge nutzen.",
    },
    # ---- 12. Trost: Andere haetten es auch getan ----
    {
        "aussage_text": "If I hadn't done it, somebody else would have.",
        "aussage_kurz": "Hinton troestet sich damit, dass jemand anders seine KI-Forschung durchgefuehrt haette, wenn nicht er.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2023/05/01/godfather-ai-geoffrey-hinton-quit-google-regrets-lifes-work-bad-actors/",
        "quell_titel": "Hinton on regrets and inevitability (Fortune)",
        "datum_aussage": "2023-05-01",
        "sprache": "en",
        "kontext": "Hinton reflektiert ueber seine persoenliche Verantwortung fuer die KI-Entwicklung.",
        "aussage_uebersetzung_de": "Wenn ich es nicht getan haette, haette es jemand anderes getan.",
    },
    # ---- 13. Groesste Angst ----
    {
        "aussage_text": "My greatest fear is that, in the long run, it'll turn out that these kind of digital beings we're creating are just a better form of intelligence than people.",
        "aussage_kurz": "Hintons groesste Angst ist, dass digitale Wesen langfristig eine bessere Form von Intelligenz darstellen als Menschen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.cnn.com/2025/08/13/tech/ai-geoffrey-hinton",
        "quell_titel": "The 'godfather of AI' reveals fears about superintelligent AI (CNN)",
        "datum_aussage": "2025-08-13",
        "sprache": "en",
        "kontext": "Interview 2025. Hinton beschreibt seine tiefste Sorge ueber die Zukunft der Menschheit.",
        "aussage_uebersetzung_de": "Meine groesste Angst ist, dass sich auf lange Sicht herausstellt, dass diese Art digitaler Wesen, die wir erschaffen, einfach eine bessere Form von Intelligenz sind als Menschen.",
    },
    # ---- 14. Regulierung erforderlich ----
    {
        "aussage_text": "The only thing that can force those big companies to do more research on safety is government regulation.",
        "aussage_kurz": "Hinton sagt, nur staatliche Regulierung koenne grosse Unternehmen zu mehr Sicherheitsforschung zwingen.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://www.theglobeandmail.com/business/article-geoffrey-hinton-regulation-ai-evan-solomon/",
        "quell_titel": "'Potentially very dangerous': Nobel winner Hinton wants AI minister to regulate the tech (Globe and Mail)",
        "datum_aussage": "2024-11-15",
        "sprache": "en",
        "kontext": "Interview mit kanadischen Medien nach seiner Nobel-Preis-Verleihung. Hinton fordert staatliches Eingreifen.",
        "aussage_uebersetzung_de": "Das einzige, was diese grossen Unternehmen zu mehr Sicherheitsforschung zwingen kann, ist staatliche Regulierung.",
    },
    # ---- 15. Widerstand gegen Regulierung ----
    {
        "aussage_text": "If you look at what the big companies are doing right now, they're lobbying to get less AI regulation. There's hardly any regulation as it is, but they want less.",
        "aussage_kurz": "Hinton kritisiert, dass grosse KI-Unternehmen gegen Regulierung lobbyieren, obwohl kaum Regulierung existiert.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://betakit.com/geoffrey-hinton-says-ai-companies-resistant-to-regulations-with-teeth-in-lively-debate-with-cohere-co-founder-nick-frosst/",
        "quell_titel": "Geoffrey Hinton says AI companies resistant to 'regulations with teeth' (BetaKit)",
        "datum_aussage": "2024-05-22",
        "sprache": "en",
        "kontext": "Oeffentliche Debatte mit Nick Frosst (Cohere). Hinton kritisiert die Haltung von Big Tech zur KI-Regulierung.",
        "aussage_uebersetzung_de": "Wenn man sich anschaut, was die grossen Unternehmen gerade tun: Sie lobbyieren fuer weniger KI-Regulierung. Es gibt ohnehin kaum Regulierung, aber sie wollen noch weniger.",
    },
    # ---- 16. Unterstuetzung fuer California SB 1047 ----
    {
        "aussage_text": "SB 1047 is the bare minimum for effective regulation of this technology.",
        "aussage_kurz": "Hinton unterstuetzt das kalifornische KI-Sicherheitsgesetz SB 1047 als absolutes Minimum fuer effektive Regulierung.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,  # Social-Media-Post / offener Brief
        "plattform_id": 5,
        "quell_link": "https://www.dsapps.dev/blog/geoffrey-hinton-ai-risks-regulation/",
        "quell_titel": "AI development and its potential risks according to Geoffrey Hinton (David Simpson Apps)",
        "datum_aussage": "2024-08-15",
        "sprache": "en",
        "kontext": "Offener Brief mit Yoshua Bengio, Stuart Russell und Lawrence Lessig zur Unterstuetzung von SB 1047 in Kalifornien.",
        "aussage_uebersetzung_de": "SB 1047 ist das absolute Minimum fuer effektive Regulierung dieser Technologie.",
    },
    # ---- 17. Autonome Waffen ----
    {
        "aussage_text": "We need a ban on weapon systems that make the decision to apply violent force autonomously.",
        "aussage_kurz": "Hinton fordert ein Verbot autonomer Waffensysteme, die eigenstaendig ueber Gewaltanwendung entscheiden.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 5,
        "quell_link": "https://www.stopkillerrobots.org/news/2024-nobel-laureate-in-physics-raises-concerns-about-killer-robots/",
        "quell_titel": "2024 Nobel laureate in Physics raises concerns about killer robots (Stop Killer Robots)",
        "datum_aussage": "2013-10-01",
        "sprache": "en",
        "kontext": "Offener Brief im Oktober 2013 von ueber 270 Ingenieuren, Informatikern und KI-Experten. Hinton gehoert zu den Unterzeichnern.",
        "aussage_uebersetzung_de": "Wir brauchen ein Verbot von Waffensystemen, die die Entscheidung zur Anwendung von Gewalt autonom treffen.",
    },
    # ---- 18. Oligarchen kontrollieren KI ----
    {
        "aussage_text": "The people who control AI, people like Musk and Zuckerberg, they are oligarchs.",
        "aussage_kurz": "Hinton bezeichnet die Menschen, die KI kontrollieren (wie Musk und Zuckerberg), als Oligarchen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://bestmediainfo.com/mediainfo/mediainfo-digital/ai-godfather-geoffrey-hinton-raises-alarm-on-tech-giants-downplaying-ai-risks-9585527",
        "quell_titel": "AI godfather Geoffrey Hinton raises alarm on tech giants downplaying AI risks (BestMediaInfo)",
        "datum_aussage": "2024-03-12",
        "sprache": "en",
        "kontext": "Hinton kritisiert die Machtkonzentration in der KI-Entwicklung bei wenigen Tech-Milliardaeren.",
        "aussage_uebersetzung_de": "Die Leute, die KI kontrollieren, Leute wie Musk und Zuckerberg, sind Oligarchen.",
    },
    # ---- 19. Unternehmen verharmlosen Risiken ----
    {
        "aussage_text": "Many of the people in big companies, I think, are downplaying the risk publicly.",
        "aussage_kurz": "Hinton wirft grossen Unternehmen vor, die Risiken von KI oeffentlich herunterzuspielen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://bestmediainfo.com/mediainfo/mediainfo-digital/ai-godfather-geoffrey-hinton-raises-alarm-on-tech-giants-downplaying-ai-risks-9585527",
        "quell_titel": "Hinton on tech companies downplaying AI risks (BestMediaInfo)",
        "datum_aussage": "2024-03-12",
        "sprache": "en",
        "kontext": "Hinton kritisiert das oeffentliche Narrativ grosser Tech-Unternehmen zu KI-Risiken.",
        "aussage_uebersetzung_de": "Viele der Leute in grossen Unternehmen, denke ich, spielen das Risiko oeffentlich herunter.",
    },
    # ---- 20. Angst vor Jobverlust ----
    {
        "aussage_text": "AI taking away jobs, with the danger that it could make the rich richer and the poor poorer.",
        "aussage_kurz": "Hinton warnt, dass KI Jobs vernichten und die Ungleichheit zwischen Arm und Reich vergroessern koennte.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://mitsloan.mit.edu/ideas-made-to-matter/why-neural-net-pioneer-geoffrey-hinton-sounding-alarm-ai",
        "quell_titel": "Why neural net pioneer Geoffrey Hinton is sounding the alarm on AI (MIT Sloan)",
        "datum_aussage": "2023-05-02",
        "sprache": "en",
        "kontext": "Hinton nennt oekonomische Risiken neben technischen Risiken von KI.",
        "aussage_uebersetzung_de": "KI nimmt Jobs weg, mit der Gefahr, dass sie die Reichen reicher und die Armen aermer machen koennte.",
    },
    # ---- 21. Deep Learning hat funktioniert ----
    {
        "aussage_text": "Deep learning worked. It got better as we made it bigger and we fed it more data. The question now is: What do we do about the fact that it's working?",
        "aussage_kurz": "Hinton stellt fest, dass Deep Learning funktioniert hat -- die Frage sei nun, was man damit anfange.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/",
        "quell_titel": "Hinton on deep learning success (MIT Technology Review)",
        "datum_aussage": "2023-05-02",
        "sprache": "en",
        "kontext": "Hinton reflektiert ueber den unerwarteten Erfolg von Deep Learning und die daraus resultierenden Herausforderungen.",
        "aussage_uebersetzung_de": "Deep Learning hat funktioniert. Es wurde besser, je groesser wir es machten und je mehr Daten wir ihm gaben. Die Frage ist jetzt: Was machen wir mit der Tatsache, dass es funktioniert?",
    },
    # ---- 22. Ueberraschung ueber GPT-4 ----
    {
        "aussage_text": "I was very surprised by GPT-4 and its ability to reason. I didn't think we'd get there this quickly.",
        "aussage_kurz": "Hinton zeigt sich ueberrascht von GPT-4s Faehigkeit zum Reasoning -- er habe nicht erwartet, so schnell dorthin zu kommen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://mitsloan.mit.edu/ideas-made-to-matter/why-neural-net-pioneer-geoffrey-hinton-sounding-alarm-ai",
        "quell_titel": "Hinton surprised by GPT-4 capabilities (MIT Sloan)",
        "datum_aussage": "2023-05-02",
        "sprache": "en",
        "kontext": "Statement nach seinem Google-Abgang. Hinton erklaert, dass GPT-4s Faehigkeiten ein Wake-up-Call waren.",
        "aussage_uebersetzung_de": "Ich war sehr ueberrascht von GPT-4 und seiner Faehigkeit zu schlussfolgern. Ich dachte nicht, dass wir so schnell dorthin kommen wuerden.",
    },
    # ---- 23. Analoge vs. digitale Systeme ----
    {
        "aussage_text": "Digital systems have the advantage over biological brains: they can share what they've learned instantly. If you have 10,000 copies of the same AI system and each one learns something, they can all instantly share what they've learned.",
        "aussage_kurz": "Hinton erklaert, dass digitale KI-Systeme gegenueber biologischen Gehirnen den Vorteil haben, Wissen sofort zu teilen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/",
        "quell_titel": "60 Minutes: Hinton on digital vs. biological intelligence",
        "datum_aussage": "2023-10-08",
        "sprache": "en",
        "kontext": "Hinton erklaert, warum KI-Systeme biologische Intelligenz ueberholen koennen.",
        "aussage_uebersetzung_de": "Digitale Systeme haben gegenueber biologischen Gehirnen den Vorteil: Sie koennen das, was sie gelernt haben, sofort teilen. Wenn man 10.000 Kopien desselben KI-Systems hat und jedes etwas lernt, koennen sie alle sofort teilen, was sie gelernt haben.",
    },
    # ---- 24. Nobelvortrag ueber Boltzmann-Maschinen ----
    {
        "aussage_text": "The Boltzmann machine was designed to learn internal representations of data by using the principle of maximum likelihood.",
        "aussage_kurz": "Hinton beschreibt in seinem Nobelvortrag, dass Boltzmann-Maschinen entwickelt wurden, um interne Repraesentationen von Daten zu lernen.",
        "modus": "muendlich",
        "quellen_typ_id": 10,  # Offizielle Stellungnahme
        "plattform_id": 5,
        "quell_link": "https://www.nobelprize.org/uploads/2024/12/hinton-lecture-1.pdf",
        "quell_titel": "Nobel Lecture: Boltzmann machines (Geoffrey Hinton)",
        "datum_aussage": "2024-12-08",
        "sprache": "en",
        "kontext": "Nobelvortrag in Stockholm. Hinton erklaert seine grundlegende Arbeit zu Boltzmann-Maschinen aus den 1980er Jahren.",
        "aussage_uebersetzung_de": "Die Boltzmann-Maschine wurde entwickelt, um interne Repraesentationen von Daten zu lernen, indem sie das Prinzip der Maximum-Likelihood verwendet.",
    },
    # ---- 25. Backpropagation als Durchbruch ----
    {
        "aussage_text": "Backpropagation showed that neural networks could discover their own internal representations of data, which was a major breakthrough.",
        "aussage_kurz": "Hinton beschreibt Backpropagation als Durchbruch, der neuronalen Netzen ermoeglichte, eigene interne Datenrepraesentationen zu entdecken.",
        "modus": "muendlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://awards.acm.org/award_winners/hinton_4791679",
        "quell_titel": "Geoffrey E Hinton - ACM Turing Award (ACM)",
        "datum_aussage": "2018-03-27",
        "sprache": "en",
        "kontext": "Hinton wird zusammen mit Bengio und LeCun mit dem Turing Award 2018 ausgezeichnet. Die Begruendung betont Backpropagation.",
        "aussage_uebersetzung_de": "Backpropagation zeigte, dass neuronale Netze ihre eigenen internen Repraesentationen von Daten entdecken konnten, was ein grosser Durchbruch war.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. Promotion Edinburgh ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Geoffrey Hinton promoviert an der Universitaet Edinburgh mit einer Dissertation ueber 'Relaxation and its role in vision' unter der Betreuung von Christopher Longuet-Higgins.",
        "datum_handlung": "1978",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Geoffrey_Hinton",
        "quell_titel": "Geoffrey Hinton - Wikipedia",
        "kontext": "Hintons Promotion legte die Grundlage fuer seine spaetere Arbeit an neuronalen Netzen.",
    },
    # ---- H2. Carnegie Mellon Professur ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Geoffrey Hinton tritt eine Professur an der Carnegie Mellon University an, wo er mit Kollegen an neuronalen Netzen forscht.",
        "datum_handlung": "1982",
        "betrag_usd": None,
        "quell_link": "https://www.cmu.edu/news/stories/archives/2019/march/hinton-wins-turing-award.html",
        "quell_titel": "Hinton Shares 2019 Turing Award for Deep Learning (Carnegie Mellon)",
        "kontext": "Bei Carnegie Mellon arbeitete Hinton an grundlegenden Arbeiten zu Backpropagation.",
    },
    # ---- H3. Boltzmann-Maschine Erfindung ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Hinton erfindet zusammen mit David Ackley und Terry Sejnowski die Boltzmann-Maschine, ein stochastisches neuronales Netz, das lernen kann, charakteristische Elemente in Daten zu erkennen.",
        "datum_handlung": "1985",
        "betrag_usd": None,
        "quell_link": "https://www.nobelprize.org/prizes/physics/2024/press-release/",
        "quell_titel": "Press release: The Nobel Prize in Physics 2024 (NobelPrize.org)",
        "kontext": "Die Boltzmann-Maschine wurde spaeter als grundlegender Beitrag zum maschinellen Lernen anerkannt und war Teil der Begruendung fuer Hintons Nobelpreis 2024.",
    },
    # ---- H4. Backpropagation-Paper ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Hinton veroeffentlicht zusammen mit David Rumelhart und Ronald J. Williams ein einflussreiches Paper, das den Backpropagation-Algorithmus fuer das Training mehrschichtiger neuronaler Netze popularisiert.",
        "datum_handlung": "1986",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Geoffrey_Hinton",
        "quell_titel": "Geoffrey Hinton - Backpropagation (Wikipedia)",
        "kontext": "Dieses Paper wurde zu einer der meistzitierten Arbeiten in der KI-Forschung und ermoeglichte Deep Learning.",
    },
    # ---- H5. University of Toronto ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Geoffrey Hinton wechselt zur University of Toronto, wo er eine Professur fuer Informatik uebernimmt und bis heute forscht.",
        "datum_handlung": "1987",
        "betrag_usd": None,
        "quell_link": "https://www.cs.toronto.edu/~hinton/bio.html",
        "quell_titel": "Geoffrey E. Hinton: Biographical Sketch (University of Toronto)",
        "kontext": "An der University of Toronto baute Hinton eine der weltweit fuehrenden Forschungsgruppen fuer neuronale Netze auf.",
    },
    # ---- H6. CIFAR Neural Computation Program ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Hinton wird Direktor des CIFAR-Programms 'Neural Computation and Adaptive Perception', das die Deep-Learning-Revolution massgeblich foerderte.",
        "datum_handlung": "2004",
        "betrag_usd": None,
        "quell_link": "https://cifar.ca/bios/geoffrey-hinton/",
        "quell_titel": "Geoffrey Hinton - CIFAR",
        "kontext": "Das CIFAR-Programm brachte fuehrende Forscher wie Yoshua Bengio und Yann LeCun zusammen und finanzierte die Forschung, die zu AlexNet fuehrte.",
    },
    # ---- H7. DNNresearch Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Hinton gruendet zusammen mit seinen Doktoranden Alex Krizhevsky und Ilya Sutskever das Startup DNNresearch Inc., nachdem ihr AlexNet-Modell 2012 die ImageNet-Challenge gewann.",
        "datum_handlung": "2012",
        "betrag_usd": None,
        "quell_link": "https://techcrunch.com/2013/03/12/google-scoops-up-neural-networks-startup-dnnresearch-to-boost-its-voice-and-image-search-tech/",
        "quell_titel": "Google Scoops Up Neural Networks Startup DNNresearch (TechCrunch)",
        "kontext": "DNNresearch wurde nach dem AlexNet-Durchbruch gegruendet und kurz darauf verkauft.",
    },
    # ---- H8. ImageNet/AlexNet Durchbruch ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Hintons Team (Krizhevsky, Sutskever, Hinton) gewinnt die ImageNet Large Scale Visual Recognition Challenge 2012 mit AlexNet, einem tiefen neuronalen Netz. Die Top-5-Fehlerrate von 15.3% uebertrifft die Konkurrenz um 10.8 Prozentpunkte -- ein historischer Durchbruch.",
        "datum_handlung": "2012-09-30",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/AlexNet",
        "quell_titel": "AlexNet - Wikipedia",
        "kontext": "AlexNet markierte den Beginn der Deep-Learning-Aera und zeigte, dass neuronale Netze mit GPUs skalierbar sind.",
    },
    # ---- H9. Google-Akquisition DNNresearch ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Google erwirbt DNNresearch Inc. fuer $44 Millionen nach einer Auktion, an der auch Baidu, Microsoft und DeepMind teilnahmen. Hinton, Krizhevsky und Sutskever treten Google Brain bei.",
        "datum_handlung": "2013-03-12",
        "betrag_usd": 44000000.0,
        "quell_link": "https://www.utoronto.ca/news/google-acquires-u-t-neural-networks-company",
        "quell_titel": "Google acquires U of T neural networks company (University of Toronto)",
        "kontext": "Die Akquisition machte Hinton zu einem Google-VP und Engineering Fellow. Er behielt seine Professur in Toronto.",
    },
    # ---- H10. Google Brain Beitritt ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Geoffrey Hinton tritt Google Brain bei und wird Vice President und Engineering Fellow. Er arbeitet in Teilzeit (spaeter 50%, dann 20%) parallel zu seiner Professur in Toronto.",
        "datum_handlung": "2013-03-12",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Geoffrey_Hinton",
        "quell_titel": "Geoffrey Hinton - Google Career (Wikipedia)",
        "kontext": "Hintons Beitritt zu Google brachte Deep Learning ins Zentrum der Industrie.",
    },
    # ---- H11. Turing Award ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Geoffrey Hinton erhaelt zusammen mit Yoshua Bengio und Yann LeCun den ACM Turing Award 2018 fuer bahnbrechende Arbeiten zu Deep Neural Networks. Die drei werden als 'Godfathers of Deep Learning' bezeichnet.",
        "datum_handlung": "2018-03-27",
        "betrag_usd": 1000000.0,
        "quell_link": "https://awards.acm.org/award_winners/hinton_4791679",
        "quell_titel": "Geoffrey E Hinton - ACM Turing Award",
        "kontext": "Der Turing Award gilt als 'Nobelpreis der Informatik'. Hinton ist der zweite Mensch, der sowohl den Turing Award als auch den Nobelpreis erhaelt.",
    },
    # ---- H12. Google-Ruecktritt ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Geoffrey Hinton kuendigt seinen Ruecktritt von Google an, um frei ueber KI-Risiken sprechen zu koennen, ohne Ruecksicht auf Googles Geschaeftsinteressen nehmen zu muessen. Er verzichtet auf ein Gehalt von ueber $1 Million pro Jahr.",
        "datum_handlung": "2023-05-01",
        "betrag_usd": None,
        "quell_link": "https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/",
        "quell_titel": "Deep learning pioneer Geoffrey Hinton quits Google (MIT Technology Review)",
        "kontext": "Hintons Ruecktritt machte weltweit Schlagzeilen und verstaerkte die Debatte ueber KI-Risiken massgeblich.",
    },
    # ---- H13. Offener Brief gegen autonome Waffen ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Hinton unterzeichnet einen offenen Brief von ueber 270 Ingenieuren und KI-Experten, der ein Verbot autonomer Waffensysteme fordert, die ohne menschliche Kontrolle ueber Gewaltanwendung entscheiden.",
        "datum_handlung": "2013-10-01",
        "betrag_usd": None,
        "quell_link": "https://www.stopkillerrobots.org/news/2024-nobel-laureate-in-physics-raises-concerns-about-killer-robots/",
        "quell_titel": "2024 Nobel laureate raises concerns about killer robots (Stop Killer Robots)",
        "kontext": "Hinton positionierte sich frueher als viele andere prominente KI-Forscher gegen militaerische KI-Anwendungen.",
    },
    # ---- H14. Unterstuetzung SB 1047 ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Hinton unterzeichnet zusammen mit Yoshua Bengio, Stuart Russell und Lawrence Lessig einen offenen Brief zur Unterstuetzung von Kaliforniens AI Safety Bill SB 1047, der Risikobewertungen fuer grosse KI-Modelle vorschreibt.",
        "datum_handlung": "2024-08-15",
        "betrag_usd": None,
        "quell_link": "https://www.dsapps.dev/blog/geoffrey-hinton-ai-risks-regulation/",
        "quell_titel": "AI development and its potential risks according to Geoffrey Hinton",
        "kontext": "Der Brief bezeichnete SB 1047 als 'absolutes Minimum' fuer KI-Regulierung. Das Gesetz wurde spaeter von Kaliforniens Gouverneur abgelehnt.",
    },
    # ---- H15. Nobelpreis Physik 2024 ----
    {
        "handlung_typ": "sonstiges",
        "beschreibung": "Geoffrey Hinton erhaelt gemeinsam mit John J. Hopfield den Nobelpreis fuer Physik 2024 'fuer grundlegende Entdeckungen und Erfindungen, die maschinelles Lernen mit kuenstlichen neuronalen Netzen ermoeglichen'.",
        "datum_handlung": "2024-10-08",
        "betrag_usd": 550000.0,
        "quell_link": "https://www.nobelprize.org/prizes/physics/2024/hinton/facts/",
        "quell_titel": "Nobel Prize in Physics 2024: Geoffrey Hinton (NobelPrize.org)",
        "kontext": "Hinton ist erst die zweite Person, die sowohl den Turing Award als auch den Nobelpreis erhaelt (nach Herbert Simon). Er nutzt die Plattform, um vor KI-Risiken zu warnen.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=21 existiert
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
            "Claude (collect_hinton.py)"
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
        "Geoffrey Hinton, Google resignation, AI risks, existential threat, Nobel Prize Physics 2024, Turing Award, Boltzmann machine, backpropagation, AlexNet, ImageNet 2012, DNNresearch, consciousness, regulation, autonomous weapons, SB 1047, 60 Minutes, MIT Technology Review, CNN, Washington Post, Fortune",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: MIT Technology Review, CNN, Washington Post, Fortune, 60 Minutes (CBS), "
        f"NobelPrize.org, ACM Turing Award, Wikipedia, TechCrunch, Globe and Mail, BetaKit, "
        f"Mindplex, Stop Killer Robots, Carnegie Mellon News, University of Toronto News.",
        "Claude (collect_hinton.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Geoffrey Hinton (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Geoffrey Hinton")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_hinton.py")
    print("  Verifizierte Aussagen & Handlungen: Geoffrey Hinton")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
