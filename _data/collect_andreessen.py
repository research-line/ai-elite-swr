#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_andreessen.py
=====================
Sammelt verifizierbare Aussagen und Handlungen von Marc Andreessen (person_id=24)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Essays,
Podcasts, Interviews und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 24  # Marc Andreessen

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
    # ---- 1. "Software is Eating the World" WSJ 2011 ----
    {
        "aussage_text": "In short, software is eating the world.",
        "aussage_kurz": "Andreessen praegte den Begriff 'Software is Eating the World' zur Beschreibung der Digitalisierung aller Industrien.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,   # Nachrichtenartikel
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://a16z.com/why-software-is-eating-the-world/",
        "quell_titel": "Why Software Is Eating the World (Wall Street Journal, republished a16z)",
        "datum_aussage": "2011-08-20",
        "sprache": "en",
        "kontext": "Wegweisender Essay im Wall Street Journal, der die These aufstellt, dass Software alle Industrien transformieren wird.",
        "aussage_uebersetzung_de": "Kurz gesagt: Software frisst die Welt.",
    },
    # ---- 2. "Software is Eating the World" - Technology readiness ----
    {
        "aussage_text": "Six decades into the computer revolution, four decades since the invention of the microprocessor, and two decades into the rise of the modern Internet, all of the technology required to transform industries through software finally works and can be widely delivered at global scale.",
        "aussage_kurz": "Andreessen erklaert, dass 2011 erstmals alle noetigen Technologien zur globalen Software-Transformation verfuegbar waren.",
        "modus": "schriftlich",
        "quellen_typ_id": 7,
        "plattform_id": 5,
        "quell_link": "https://a16z.com/why-software-is-eating-the-world/",
        "quell_titel": "Why Software Is Eating the World (Wall Street Journal)",
        "datum_aussage": "2011-08-20",
        "sprache": "en",
        "kontext": "Erklaerung des historischen Moments, in dem Software-Skalierung moeglich wurde.",
        "aussage_uebersetzung_de": "Sechs Jahrzehnte nach der Computer-Revolution, vier Jahrzehnte nach der Erfindung des Mikroprozessors und zwei Jahrzehnte nach dem Aufstieg des modernen Internets funktioniert endlich die gesamte Technologie, die erforderlich ist, um Industrien durch Software zu transformieren, und kann im globalen Massstab verbreitet werden.",
    },
    # ---- 3. Why AI Will Save the World - June 2023 ----
    {
        "aussage_text": "AI will not destroy the world, and in fact may save it.",
        "aussage_kurz": "Andreessen widerspricht KI-Risiko-Warnungen und behauptet, KI werde die Welt nicht zerstoeren, sondern retten.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Blog-Artikel
        "plattform_id": 9,     # Blogs
        "quell_link": "https://a16z.com/ai-will-save-the-world/",
        "quell_titel": "Why AI Will Save the World (a16z)",
        "datum_aussage": "2023-06-06",
        "sprache": "en",
        "kontext": "Kernthese seines einflussreichen Essays gegen AI Doomerism, veroeffentlicht auf a16z.",
        "aussage_uebersetzung_de": "KI wird die Welt nicht zerstoeren und koennte sie in der Tat retten.",
    },
    # ---- 4. Why AI Will Save the World - AI is not alive ----
    {
        "aussage_text": "AI doesn't want, it doesn't have goals, it doesn't want to kill you, because it's not alive. And AI is a machine – is not going to come alive any more than your toaster will.",
        "aussage_kurz": "Andreessen argumentiert, KI sei nicht lebendig und werde nicht lebendig werden, daher habe sie keine eigenen Ziele.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/ai-will-save-the-world/",
        "quell_titel": "Why AI Will Save the World (a16z)",
        "datum_aussage": "2023-06-06",
        "sprache": "en",
        "kontext": "Argumentation gegen die Idee, dass KI eine existenzielle Bedrohung darstellt, weil sie Bewusstsein erlangen koennte.",
        "aussage_uebersetzung_de": "KI will nichts, sie hat keine Ziele, sie will dich nicht toeten, weil sie nicht lebendig ist. Und KI ist eine Maschine – sie wird nicht lebendig werden, genauso wenig wie dein Toaster.",
    },
    # ---- 5. Why AI Will Save the World - Augmentation ----
    {
        "aussage_text": "What AI offers us is the opportunity to profoundly augment human intelligence to make all of these outcomes of intelligence – and many others, from the creation of new medicines to ways to solve climate change to technologies to reach the stars – much, much better from here.",
        "aussage_kurz": "Andreessen sieht KI als Werkzeug zur massiven Verstaerkung menschlicher Intelligenz fuer alle grossen Herausforderungen.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/ai-will-save-the-world/",
        "quell_titel": "Why AI Will Save the World (a16z)",
        "datum_aussage": "2023-06-06",
        "sprache": "en",
        "kontext": "Optimistische Vision der KI-Zukunft als Verstaerkung menschlicher Faehigkeiten.",
        "aussage_uebersetzung_de": "Was KI uns bietet, ist die Gelegenheit, menschliche Intelligenz tiefgreifend zu erweitern, um all diese Ergebnisse von Intelligenz – und viele andere, von der Entwicklung neuer Medikamente bis hin zu Loesungen fuer den Klimawandel bis hin zu Technologien, um die Sterne zu erreichen – von hier an viel, viel besser zu machen.",
    },
    # ---- 6. Techno-Optimist Manifesto - Technology ----
    {
        "aussage_text": "Technology is the glory of human ambition and achievement, the spearhead of progress, and the realization of our potential.",
        "aussage_kurz": "Im 'Techno-Optimist Manifesto' beschreibt Andreessen Technologie als Hoehepunkt menschlichen Ehrgeizes und Fortschritts.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/the-techno-optimist-manifesto/",
        "quell_titel": "The Techno-Optimist Manifesto (a16z)",
        "datum_aussage": "2023-10-16",
        "sprache": "en",
        "kontext": "Zentraler Satz aus dem umstrittenen 5.200-Woerter-Essay ueber Techno-Optimismus.",
        "aussage_uebersetzung_de": "Technologie ist der Ruhm menschlichen Ehrgeizes und menschlicher Leistung, die Speerspitze des Fortschritts und die Verwirklichung unseres Potenzials.",
    },
    # ---- 7. Techno-Optimist Manifesto - Growth ----
    {
        "aussage_text": "Techno-Optimists believe that societies, like sharks, grow or die. We believe growth is progress – leading to vitality, expansion of life, increasing knowledge, higher well being.",
        "aussage_kurz": "Andreessen vergleicht Gesellschaften mit Haien: Sie muessen wachsen oder sterben.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/the-techno-optimist-manifesto/",
        "quell_titel": "The Techno-Optimist Manifesto (a16z)",
        "datum_aussage": "2023-10-16",
        "sprache": "en",
        "kontext": "Kernaussage ueber die Notwendigkeit staendigen Wachstums im Techno-Optimist Manifesto.",
        "aussage_uebersetzung_de": "Techno-Optimisten glauben, dass Gesellschaften wie Haie wachsen oder sterben. Wir glauben, dass Wachstum Fortschritt ist – fuehrend zu Vitalitaet, Ausdehnung des Lebens, zunehmendem Wissen, hoeherem Wohlbefinden.",
    },
    # ---- 8. Techno-Optimist Manifesto - Masters of technology ----
    {
        "aussage_text": "We believe that we are, have been, and will always be the masters of technology, not mastered by technology. We are not victims, we are conquerors.",
        "aussage_kurz": "Andreessen besteht darauf, dass Menschen Herrscher ueber Technologie sind und bleiben werden, nicht Opfer.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/the-techno-optimist-manifesto/",
        "quell_titel": "The Techno-Optimist Manifesto (a16z)",
        "datum_aussage": "2023-10-16",
        "sprache": "en",
        "kontext": "Aussage ueber menschliche Kontrolle und Selbstbestimmung im technologischen Fortschritt.",
        "aussage_uebersetzung_de": "Wir glauben, dass wir die Herren der Technologie sind, waren und immer sein werden, nicht von Technologie beherrscht. Wir sind keine Opfer, wir sind Eroberer.",
    },
    # ---- 9. Techno-Optimist Manifesto - Techno-Capital Machine ----
    {
        "aussage_text": "We believe the techno-capital machine of markets and innovation never ends, but instead spirals continuously upward.",
        "aussage_kurz": "Andreessen beschreibt einen sich ewig nach oben drehenden Kreislauf aus Maerkten, Innovation und Kapital.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/the-techno-optimist-manifesto/",
        "quell_titel": "The Techno-Optimist Manifesto (a16z)",
        "datum_aussage": "2023-10-16",
        "sprache": "en",
        "kontext": "Zentrale Metapher fuer den sich selbst verstaerkenden Zyklus von Kapitalismus und technologischem Fortschritt.",
        "aussage_uebersetzung_de": "Wir glauben, dass die techno-kapitalistische Maschine aus Maerkten und Innovation niemals endet, sondern sich stattdessen kontinuierlich nach oben dreht.",
    },
    # ---- 10. Joe Rogan Podcast - Morning in America ----
    {
        "aussage_text": "Very happy. It's morning in America.",
        "aussage_kurz": "Nach Trumps Wahlsieg 2024 erklaert Andreessen, es sei 'Morgen in Amerika' – eine Reagan-Anspielung.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast-Interview
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://podcastnotes.org/joe-rogan-experience/marc-andreessen-on-everything-joe-rogan-experience-2234/",
        "quell_titel": "Joe Rogan Experience #2234 with Marc Andreessen",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Antwort auf Joe Rogans Frage nach seiner Reaktion auf die Wahl 2024. Spielt auf Ronald Reagans Wahlkampf-Slogan an.",
        "aussage_uebersetzung_de": "Sehr gluecklich. Es ist Morgen in Amerika.",
    },
    # ---- 11. Joe Rogan Podcast - Political Realignment ----
    {
        "aussage_text": "We're going through the first profound political realignment probably since the 1960s.",
        "aussage_kurz": "Andreessen sieht 2024 die erste tiefgreifende politische Neuausrichtung seit den 1960er Jahren.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://sfstandard.com/2024/11/27/marc-andreessen-joe-rogan-trump-maga-silicon-valley/",
        "quell_titel": "Tech billionaire Marc Andreessen goes full MAGA on Joe Rogan podcast (SF Standard)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Analyse der politischen Verschiebungen im Joe-Rogan-Interview nach Trumps Sieg.",
        "aussage_uebersetzung_de": "Wir durchleben die erste tiefgreifende politische Neuausrichtung wahrscheinlich seit den 1960er Jahren.",
    },
    # ---- 12. Joe Rogan Podcast - Trump Assassination Attempt ----
    {
        "aussage_text": "That other timeline is out there somewhere, and I don't wanna visit it. The most conspicuous display of physical bravery I've ever seen.",
        "aussage_kurz": "Andreessen nennt Trumps Reaktion auf das Attentat im Juli 2024 die eindrucksvollste Demonstration physischer Tapferkeit, die er je gesehen hat.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://sfstandard.com/2024/11/27/marc-andreessen-joe-rogan-trump-maga-silicon-valley/",
        "quell_titel": "Tech billionaire Marc Andreessen goes full MAGA on Joe Rogan podcast (SF Standard)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Kommentar zum Attentatsversuch auf Trump in Pennsylvania im Juli 2024.",
        "aussage_uebersetzung_de": "Diese andere Zeitlinie ist irgendwo da draussen, und ich will sie nicht besuchen. Die eindrucksvollste Demonstration physischer Tapferkeit, die ich je gesehen habe.",
    },
    # ---- 13. Joe Rogan Podcast - Operation Chokepoint 2.0 ----
    {
        "aussage_text": "Over 30 tech founders had been debanked in the last four years. There's no due process. None of this is written down. There's no rules. There's no court. There's no decision process. There's no appeal.",
        "aussage_kurz": "Andreessen behauptet, ueber 30 Tech-Gruender seien ohne rechtlichen Prozess vom Bankensystem ausgeschlossen worden.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.axios.com/2024/12/01/debanked-crypto-andreessen-joe-rogan",
        "quell_titel": "What 'debanking' is and why tech execs say they were debanked (Axios)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Kritik an der angeblichen 'Operation Chokepoint 2.0' gegen Krypto-Unternehmen unter Biden.",
        "aussage_uebersetzung_de": "Ueber 30 Tech-Gruender wurden in den letzten vier Jahren vom Bankensystem ausgeschlossen. Es gibt kein ordentliches Verfahren. Nichts davon ist schriftlich festgehalten. Es gibt keine Regeln. Es gibt kein Gericht. Es gibt keinen Entscheidungsprozess. Es gibt keine Berufungsmoeglichkeit.",
    },
    # ---- 14. Joe Rogan Podcast - Debanking as motive ----
    {
        "aussage_text": "This is why we ended up supporting Trump. We can't live in a world where somebody starts a company that's completely legal, and then gets sanctioned and embargoed by the US government, through a completely unaccountable, no-due process.",
        "aussage_kurz": "Andreessen nennt 'Debanking' als Hauptgrund fuer seine Trump-Unterstuetzung 2024.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://decrypt.co/293947/operation-chokepoint-2-0-crypto-founders-silenced-by-secret-debanking",
        "quell_titel": "Operation Choke Point 2.0: Crypto Founders Silenced by 'Secret' Debanking? (Decrypt)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Erklaerung seiner politischen Wende von Demokrat zu Trump-Unterstuetzer.",
        "aussage_uebersetzung_de": "Deswegen haben wir am Ende Trump unterstuetzt. Wir koennen nicht in einer Welt leben, in der jemand ein voellig legales Unternehmen gruendet und dann von der US-Regierung sanktioniert und mit einem Embargo belegt wird, durch einen voellig unkontrollierbaren Prozess ohne ordentliches Verfahren.",
    },
    # ---- 15. Lex Fridman Podcast - AI Regulation ----
    {
        "aussage_text": "I think we're going to cause extraordinary damage. The moment you say AI is going to kill all of us, therefore we should ban it, or we should regulate it, all that kind of stuff, that's when it starts getting serious.",
        "aussage_kurz": "Andreessen warnt, dass KI-Regulierung ausserordentlichen Schaden anrichten werde.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://lexfridman.com/marc-andreessen-2-transcript/",
        "quell_titel": "Lex Fridman Podcast #458: Marc Andreessen on Trump, Power, Tech, AI",
        "datum_aussage": "2025-01-26",
        "sprache": "en",
        "kontext": "Kritik an regulatorischen Ansaetzen zur KI-Sicherheit im Lex-Fridman-Interview 2025.",
        "aussage_uebersetzung_de": "Ich denke, wir werden ausserordentlichen Schaden anrichten. In dem Moment, in dem man sagt, KI wird uns alle toeten, daher sollten wir sie verbieten oder regulieren, all das Zeug, da wird es ernst.",
    },
    # ---- 16. AI Censorship - Comparison to social media ----
    {
        "aussage_text": "My concern is that the censorship and political control of AI is a thousand times more dangerous than censorship and political control of social media — maybe a million times more dangerous.",
        "aussage_kurz": "Andreessen haelt Zensur von KI fuer tausend- bis millionenfach gefaehrlicher als Social-Media-Zensur.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,   # Social-Media-Post
        "plattform_id": 2,     # Twitter/X
        "quell_link": "https://www.shortform.com/podcast/episode/lex-fridman-podcast-2025-01-26-episode-summary-458-marc-andreessen-trump-power-tech-ai-immigration-future-of-america",
        "quell_titel": "Marc Andreessen on AI Censorship (via Lex Fridman Podcast Summary)",
        "datum_aussage": "2025-01-26",
        "sprache": "en",
        "kontext": "Warnung vor staatlicher Kontrolle von KI-Systemen.",
        "aussage_uebersetzung_de": "Meine Sorge ist, dass die Zensur und politische Kontrolle von KI tausendmal gefaehrlicher ist als Zensur und politische Kontrolle von Social Media – vielleicht millionenfach gefaehrlicher.",
    },
    # ---- 17. Government censorship critique ----
    {
        "aussage_text": "The government... decided that the First Amendment didn't apply to them... they can just arbitrarily pressure companies to censor.",
        "aussage_kurz": "Andreessen wirft der US-Regierung vor, das First Amendment zu umgehen, indem sie Unternehmen zur Zensur draengt.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.deciphr.ai/podcast/marc-andreessen-trump-power-tech-ai-immigration--future-of-america--lex-fridman-podcast-458",
        "quell_titel": "Lex Fridman Podcast #458: Marc Andreessen",
        "datum_aussage": "2025-01-26",
        "sprache": "en",
        "kontext": "Kritik an vermeintlicher staatlicher Einflussnahme auf Content-Moderation.",
        "aussage_uebersetzung_de": "Die Regierung... hat entschieden, dass das First Amendment fuer sie nicht gilt... sie koennen Unternehmen einfach willkuerlich unter Druck setzen zu zensieren.",
    },
    # ---- 18. E/acc - Deceleration as murder ----
    {
        "aussage_text": "Any deceleration of AI will cost lives. It's a form of murder.",
        "aussage_kurz": "Andreessen bezeichnet Verlangsamung der KI-Entwicklung als 'Form von Mord', weil sie Leben koste.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://www.nasdaq.com/articles/marc-andreessen-says-pumping-the-brakes-on-ai-development-is-a-form-of-murder",
        "quell_titel": "Marc Andreessen Says Pumping The Brakes On AI Development Is 'A Form Of Murder' (Nasdaq)",
        "datum_aussage": "2023",
        "sprache": "en",
        "kontext": "Radikale Position im Decel-vs-Accel-Streit ueber KI-Entwicklungsgeschwindigkeit.",
        "aussage_uebersetzung_de": "Jede Verlangsamung von KI wird Leben kosten. Es ist eine Form von Mord.",
    },
    # ---- 19. Libertarianism critique ----
    {
        "aussage_text": "I'm fond of libertarianism, but it's more like an absence of philosophy than its presence.",
        "aussage_kurz": "Andreessen distanziert sich teilweise vom Libertarismus: mehr Abwesenheit als Anwesenheit einer Philosophie.",
        "modus": "schriftlich",
        "quellen_typ_id": 5,
        "plattform_id": 2,
        "quell_link": "https://x.com/pmarca/status/1635482944084254720",
        "quell_titel": "Marc Andreessen on X (@pmarca)",
        "datum_aussage": "2023-03-14",
        "sprache": "en",
        "kontext": "Tweet, der seine nuancierte Haltung zum Libertarismus verdeutlicht.",
        "aussage_uebersetzung_de": "Ich mag den Libertarismus, aber er ist eher wie die Abwesenheit einer Philosophie als ihre Anwesenheit.",
    },
    # ---- 20. Woke vs traditional religion ----
    {
        "aussage_text": "The big difference between Woke and traditional religions is that Woke has no concept of redemption or forgiveness.",
        "aussage_kurz": "Andreessen kritisiert 'Woke'-Ideologie fuer fehlende Konzepte von Vergebung und Erloesung.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://podcastnotes.org/joe-rogan-experience/marc-andreessen-on-everything-joe-rogan-experience-2234/",
        "quell_titel": "Joe Rogan Experience #2234 with Marc Andreessen (Podcast Notes)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Kulturkritik im Joe-Rogan-Podcast ueber den Unterschied zwischen 'Woke'-Kultur und traditioneller Religion.",
        "aussage_uebersetzung_de": "Der grosse Unterschied zwischen Woke und traditionellen Religionen ist, dass Woke kein Konzept von Erloesung oder Vergebung hat.",
    },
    # ---- 21. Markets generate wealth ----
    {
        "aussage_text": "Markets are the way to generate societal wealth for everything else we want to pay for, including basic research, social welfare programs, and national defense.",
        "aussage_kurz": "Andreessen sieht Maerkte als Grundlage allen gesellschaftlichen Wohlstands, der soziale Programme erst ermoeglicht.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://a16z.com/the-techno-optimist-manifesto/",
        "quell_titel": "The Techno-Optimist Manifesto (a16z)",
        "datum_aussage": "2023-10-16",
        "sprache": "en",
        "kontext": "Oekonomische Grundposition im Techno-Optimist Manifesto.",
        "aussage_uebersetzung_de": "Maerkte sind der Weg, um gesellschaftlichen Wohlstand fuer alles andere zu erzeugen, was wir bezahlen wollen, einschliesslich Grundlagenforschung, Sozialprogrammen und nationaler Verteidigung.",
    },
    # ---- 22. Golden Age potential ----
    {
        "aussage_text": "I'm incredibly optimistic, and I was optimistic already with flashes of pessimism, but I'm really optimistic especially now. We have the real potential here for a Golden Age.",
        "aussage_kurz": "Andreessen sieht das Potenzial fuer ein 'Goldenes Zeitalter' durch technologischen Fortschritt.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://podcastnotes.org/joe-rogan-experience/marc-andreessen-on-everything-joe-rogan-experience-2234/",
        "quell_titel": "Joe Rogan Experience #2234 with Marc Andreessen",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Ausdruck seines gesteigerten Optimismus nach der Wahl 2024.",
        "aussage_uebersetzung_de": "Ich bin unglaublich optimistisch, und ich war schon vorher optimistisch mit Anflügen von Pessimismus, aber ich bin jetzt wirklich besonders optimistisch. Wir haben hier das echte Potenzial fuer ein Goldenes Zeitalter.",
    },
    # ---- 23. Silicon Valley division ----
    {
        "aussage_text": "There's now two kinds of dinner parties. They've fractured cleanly in half.",
        "aussage_kurz": "Andreessen beschreibt Silicon Valley als politisch gespalten in zwei unterschiedliche Lager.",
        "modus": "muendlich",
        "quellen_typ_id": 2,
        "plattform_id": 3,
        "quell_link": "https://fortune.com/2024/11/27/marc-andreessen-joe-rogan-silicon-valley-split-trump-democrats-republicans/",
        "quell_titel": "Marc Andreessen tells Joe Rogan that Silicon Valley is split (Fortune)",
        "datum_aussage": "2024-11-26",
        "sprache": "en",
        "kontext": "Beobachtung zur politischen Fragmentierung von Silicon Valley nach der Wahl 2024.",
        "aussage_uebersetzung_de": "Es gibt jetzt zwei Arten von Dinnerpartys. Sie sind klar in zwei Haelften zerbrochen.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. NCSA Mosaic Entwicklung ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Marc Andreessen entwickelt gemeinsam mit Eric Bina am National Center for Supercomputing Applications (NCSA) den Mosaic-Webbrowser, den ersten weitverbreiteten grafischen Browser. Mosaic wird im Januar 1993 veroeffentlicht und revolutioniert den Zugang zum World Wide Web.",
        "datum_handlung": "1993-01-23",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Marc_Andreessen",
        "quell_titel": "Marc Andreessen - Wikipedia",
        "kontext": "Andreessen war zu diesem Zeitpunkt Student an der University of Illinois. Mosaic wurde zur Grundlage fuer Netscape Navigator.",
    },
    # ---- H2. Netscape Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Jim Clark (Gruender von Silicon Graphics) und Marc Andreessen gruenden Mosaic Communications Corporation, spaeter umbenannt in Netscape Communications. Das Unternehmen entwickelt den Netscape Navigator Browser.",
        "datum_handlung": "1994-04-04",
        "betrag_usd": None,
        "quell_link": "https://www.internethistorypodcast.com/2014/04/on-the-20th-anniversary-an-oral-history-of-netscapes-founding/",
        "quell_titel": "On The 20th Anniversary – An Oral History of Netscape's Founding",
        "kontext": "Andreessen war 22 Jahre alt. Die Gruendung markiert den Beginn des kommerziellen Web-Zeitalters.",
    },
    # ---- H3. Netscape Navigator Launch ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Netscape veroeffentlicht Mosaic Netscape 0.9, den Vorlaefer von Netscape Navigator. Innerhalb von vier Monaten erobert der Browser drei Viertel des Browsermarkts.",
        "datum_handlung": "1994-10-13",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Marc_Andreessen",
        "quell_titel": "Marc Andreessen - Wikipedia",
        "kontext": "Der Browser wurde kostenlos verfuegbar gemacht und dominierte schnell den Markt vor dem Aufstieg von Microsoft Internet Explorer.",
    },
    # ---- H4. Netscape IPO ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Netscape geht mit dem drittgroessten Boersengang der Geschichte an die Boerse. Der Aktienkurs wurde last-minute von $14 auf $28 verdoppelt, stieg am ersten Tag auf $75 und schloss bei $58,25. Boersenwert: $2,9 Milliarden. Andreessen wird ueber Nacht 50 Millionen Dollar reicher.",
        "datum_handlung": "1995-08-09",
        "betrag_usd": 2900000000.0,
        "quell_link": "https://www.internethistorypodcast.com/2015/08/20-years-on-why-netscapes-ipo-was-the-big-bang-of-the-internet-era/",
        "quell_titel": "20 Years On: Why Netscape's IPO Was the 'Big Bang' of the Internet Era",
        "kontext": "Der Netscape-IPO gilt als Startpunkt der Dotcom-Boom-Aera und machte Andreessen zum oeffentlich bekannten Tech-Visionaer.",
    },
    # ---- H5. AOL uebernimmt Netscape ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "America Online (AOL) uebernimmt Netscape Communications fuer $4,3 Milliarden, nachdem Netscape den Browser-Krieg gegen Microsoft Internet Explorer verloren hat.",
        "datum_handlung": "1999-03-17",
        "betrag_usd": 4300000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Marc_Andreessen",
        "quell_titel": "Marc Andreessen - Wikipedia",
        "kontext": "Die Uebernahme markiert das Ende von Netscape als unabhaengiges Unternehmen. Andreessen verlaesst das Unternehmen.",
    },
    # ---- H6. Loudcloud Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Marc Andreessen, Ben Horowitz, Tim Howes und In Sik Rhee gruenden Loudcloud am 9. September 1999 (9/9/99) als Managed-Services-Provider fuer Cloud-Computing und Hosting.",
        "datum_handlung": "1999-09-09",
        "betrag_usd": None,
        "quell_link": "https://www.fundinguniverse.com/company-histories/opsware-inc-history/",
        "quell_titel": "History of Opsware Inc. - FundingUniverse",
        "kontext": "Loudcloud war einer der fruehen Cloud-Computing-Anbieter, gegruendet auf dem Hoehepunkt der Dotcom-Blase.",
    },
    # ---- H7. Loudcloud IPO ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Loudcloud geht an die Boerse, nur sechs Monate vor dem Platzen der Dotcom-Blase. Der IPO ist einer der letzten grossen Tech-Boersengaenge vor dem Crash.",
        "datum_handlung": "2001-03-09",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Opsware",
        "quell_titel": "Opsware - Wikipedia",
        "kontext": "Der Boersengang erfolgt zu einem schwierigen Zeitpunkt, kurz vor dem massiven Tech-Crash 2001-2002.",
    },
    # ---- H8. Loudcloud → Opsware Umstrukturierung ----
    {
        "handlung_typ": "umstrukturierung",
        "beschreibung": "Loudcloud verkauft sein Hosting- und Managed-Services-Geschaeft fuer $63,5 Millionen an EDS und benennt sich in Opsware um, um sich auf Software-Produkte zu konzentrieren.",
        "datum_handlung": "2002-06-30",
        "betrag_usd": 63500000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Opsware",
        "quell_titel": "Opsware - Wikipedia",
        "kontext": "Die Umstrukturierung rettet das Unternehmen nach dem Dotcom-Crash und fokussiert auf profitablere Software-Loesungen.",
    },
    # ---- H9. HP uebernimmt Opsware ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "Hewlett-Packard (HP) kauft Opsware fuer $1,65 Milliarden in bar. Dies ist Andreessens zweiter erfolgreicher Exit.",
        "datum_handlung": "2007-07-23",
        "betrag_usd": 1650000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Opsware",
        "quell_titel": "Opsware - Wikipedia",
        "kontext": "Der Verkauf beendet Andreessens operative Rolle als CEO und ebnet den Weg fuer seinen Einstieg ins Venture Capital.",
    },
    # ---- H10. a16z Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Marc Andreessen und Ben Horowitz gruenden die Venture-Capital-Firma Andreessen Horowitz (a16z) mit einem Anfangskapital von $300 Millionen. Die Gruendung erfolgt waehrend der Finanzkrise 2008-2009.",
        "datum_handlung": "2009-07-06",
        "betrag_usd": 300000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Andreessen_Horowitz",
        "quell_titel": "Andreessen Horowitz - Wikipedia",
        "kontext": "Nur zwei Venture-Fonds wurden 2009 aufgelegt – a16z war einer davon. Dies war ein mutiger Schritt inmitten der schlimmsten Finanzkrise seit den 1930er Jahren.",
    },
    # ---- H11. Facebook Board-Mitgliedschaft ----
    {
        "handlung_typ": "einstellung",
        "beschreibung": "Marc Andreessen tritt dem Board of Directors von Facebook bei. Er bleibt bis 2019 im Board und spielt eine wichtige beratende Rolle waehrend Facebooks Wachstumsphase.",
        "datum_handlung": "2008-06-24",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/Marc_Andreessen",
        "quell_titel": "Marc Andreessen - Wikipedia",
        "kontext": "Andreessen wurde von Mark Zuckerberg rekrutiert und beriet Facebook in kritischen strategischen Entscheidungen, einschliesslich der Ablehnung eines $1 Mrd. Kaufangebots von Yahoo.",
    },
    # ---- H12. Trump Super PAC Spende ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Marc Andreessen und Ben Horowitz spenden insgesamt $5 Millionen an den pro-Trump Super PAC 'Right For America', der sich auf Swing States konzentriert. Andreessen spendet persoenlich $2,5 Millionen.",
        "datum_handlung": "2024-10-16",
        "betrag_usd": 2500000.0,
        "quell_link": "https://www.bloomberg.com/news/articles/2024-10-16/silicon-valley-s-andreessen-horowitz-give-millions-to-trump-pac",
        "quell_titel": "Trump Super PAC Gets $5M From Silicon Valley's Andreessen, Horowitz (Bloomberg)",
        "kontext": "Die Spende markiert Andreessens politischen Wechsel von lebenslangem Demokraten zu Trump-Unterstuetzer, motiviert durch Crypto-Regulierung und Biden's Kapitalertragssteuer-Plaene.",
    },
    # ---- H13. a16z $15 Milliarden Fundraise ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Andreessen Horowitz schliesst Fundraising-Runden im Wert von ueber $15 Milliarden ab, die groesste Kapitalbeschaffung in der Firmengeschichte. Die Fonds zielen auf KI-Infrastruktur ($1,7 Mrd.), Wachstumskapital ($6,75 Mrd.), American Dynamism und weitere Bereiche.",
        "datum_handlung": "2026-01-09",
        "betrag_usd": 15000000000.0,
        "quell_link": "https://techcrunch.com/2026/01/09/the-venture-firm-that-ate-silicon-valley/",
        "quell_titel": "The venture firm that ate Silicon Valley just raised another $15 billion (TechCrunch)",
        "kontext": "Mit dieser Runde wird a16z zu einer der groessten VC-Firmen weltweit mit ueber $90 Milliarden Assets under Management.",
    },
    # ---- H14. xAI Investment ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Andreessen Horowitz investiert in Elon Musks KI-Firma xAI. xAI uebernimmt im April 2025 Twitter fuer $45 Milliarden inklusive Schulden.",
        "datum_handlung": "2025-04-15",
        "betrag_usd": None,
        "quell_link": "https://finance.yahoo.com/news/andreessen-horowitz-raises-15-billion-130217803.html",
        "quell_titel": "Andreessen Horowitz raises $15 billion, doubling down on AI and defense startups (Yahoo Finance)",
        "kontext": "Die Investition in xAI unterstreicht a16z's aggressive KI-Strategie und Andreessens Naehe zu Elon Musk.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=24 existiert
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
            "Claude (collect_andreessen.py)"
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
        "Marc Andreessen, Techno-Optimist Manifesto, Why AI Will Save the World, Software is Eating the World, a16z, Netscape, Joe Rogan, Lex Fridman, Trump support, debanking, e/acc",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: The Techno-Optimist Manifesto (a16z.com, Oct 2023), Why AI Will Save the World (a16z.com, Jun 2023), "
        f"Why Software is Eating the World (WSJ 2011), Joe Rogan Experience #2234 (Nov 2024), "
        f"Lex Fridman Podcast #458 (Jan 2025), Bloomberg, TechCrunch, Fortune, Axios, Wikipedia, Decrypt.",
        "Claude (collect_andreessen.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Marc Andreessen (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Marc Andreessen")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_andreessen.py")
    print("  Verifizierte Aussagen & Handlungen: Marc Andreessen")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
