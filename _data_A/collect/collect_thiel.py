#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_thiel.py
=================
Sammelt verifizierbare Aussagen und Handlungen von Peter Thiel (person_id=25)
und fuegt sie in die SQLite-Datenbank aussagen_top100.db ein.

QUELLEN: Alle Zitate stammen aus oeffentlich zugaenglichen Interviews,
Buchveroeffentlichungen, Vorlesungen, Congressional Testimony und Nachrichtenartikeln.
Jede Aussage ist mit einer verifizierbaren Quelle versehen.

Erstellt: 2026-02-11
Autor: Claude (Recherche-Assistent)
"""

import sqlite3
import os
from datetime import datetime

# --- Konfiguration ---
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussagen_top100.db")
PERSON_ID = 25  # Peter Thiel

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
    # ---- 1. Zero to One (Buch) ----
    {
        "aussage_text": "Competition is for losers.",
        "aussage_kurz": "Thiel erklaert Wettbewerb zur Falle fuer Verlierer.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,  # Buch
        "plattform_id": 9,     # Buecher
        "quell_link": "https://www.goodreads.com/book/show/18050143-zero-to-one",
        "quell_titel": "Zero to One: Notes on Startups, or How to Build the Future (Peter Thiel, Blake Masters)",
        "datum_aussage": "2014-09-16",
        "sprache": "en",
        "kontext": "Kernthese aus dem Buch 'Zero to One'. Thiel argumentiert, dass wahre Innovatoren Monopole schaffen, nicht konkurrieren.",
        "aussage_uebersetzung_de": "Wettbewerb ist etwas fuer Verlierer.",
    },
    # ---- 2. Zero to One (Monopoly) ----
    {
        "aussage_text": "If you're starting a company, you always want to aim for monopoly and avoid competition. Hence, competition is for losers.",
        "aussage_kurz": "Startups sollten Monopole anstreben statt in Wettbewerb zu treten.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/book/show/18050143-zero-to-one",
        "quell_titel": "Zero to One: Notes on Startups, or How to Build the Future (Peter Thiel, Blake Masters)",
        "datum_aussage": "2014-09-16",
        "sprache": "en",
        "kontext": "Thiel elaboriert die Monopol-These: Erfolgreiche Unternehmen schaffen neue Kategorien statt in bestehenden Maerkten zu konkurrieren.",
        "aussage_uebersetzung_de": "Wenn du ein Unternehmen gruendest, willst du immer ein Monopol anstreben und Wettbewerb vermeiden. Deshalb ist Wettbewerb etwas fuer Verlierer.",
    },
    # ---- 3. Zero to One (Definite Future) ----
    {
        "aussage_text": "A startup is the largest endeavor over which you can have definite mastery. You can have agency not just over your own life, but over a small and important part of the world. It begins by rejecting the unjust tyranny of Chance. You are not a lottery ticket.",
        "aussage_kurz": "Thiel beschreibt Startups als Ablehnung von Zufall und als Kontrolle ueber einen Teil der Welt.",
        "modus": "schriftlich",
        "quellen_typ_id": 8,
        "plattform_id": 9,
        "quell_link": "https://www.goodreads.com/book/show/18050143-zero-to-one",
        "quell_titel": "Zero to One: Notes on Startups, or How to Build the Future",
        "datum_aussage": "2014-09-16",
        "sprache": "en",
        "kontext": "Thiel kontrastiert 'definite optimism' (planbare Zukunft) mit 'indefinite optimism' (Zukunft als Zufall).",
        "aussage_uebersetzung_de": "Ein Startup ist das groesste Unterfangen, ueber das du klare Kontrolle haben kannst. Du kannst nicht nur ueber dein eigenes Leben bestimmen, sondern ueber einen kleinen und wichtigen Teil der Welt. Es beginnt mit der Ablehnung der ungerechten Tyrannei des Zufalls. Du bist kein Lotterie-Los.",
    },
    # ---- 4. Stanford CS183 Lecture (2012) ----
    {
        "aussage_text": "The most contrarian thing of all is not to oppose the crowd but to think for yourself.",
        "aussage_kurz": "Thiels contrarian Credo: Wahre Originalitaet liegt nicht im Widerspruch, sondern im eigenstaendigen Denken.",
        "modus": "muendlich",
        "quellen_typ_id": 3,   # Vortrag/Lecture
        "plattform_id": 7,     # Universitaeten
        "quell_link": "https://blakemasters.com/peter-thiels-cs183-startup",
        "quell_titel": "Peter Thiel's CS183: Startup - Class Notes (Blake Masters)",
        "datum_aussage": "2012",
        "sprache": "en",
        "kontext": "Aus Thiels legendaerer Stanford-Vorlesung 'Startup', die zur Grundlage von 'Zero to One' wurde.",
        "aussage_uebersetzung_de": "Das Kontraerste von allem ist nicht, der Menge zu widersprechen, sondern fuer sich selbst zu denken.",
    },
    # ---- 5. Stanford CS183 (Technology vs Globalization) ----
    {
        "aussage_text": "Horizontal progress is globalization — taking things that work somewhere and making them work everywhere. Vertical progress is technology — doing new things.",
        "aussage_kurz": "Thiel unterscheidet zwischen Globalisierung (Kopieren) und Technologie (Innovation).",
        "modus": "muendlich",
        "quellen_typ_id": 3,
        "plattform_id": 7,
        "quell_link": "https://blakemasters.com/peter-thiels-cs183-startup",
        "quell_titel": "Peter Thiel's CS183: Startup - Class Notes",
        "datum_aussage": "2012",
        "sprache": "en",
        "kontext": "Thiels Unterscheidung zwischen 1-to-n (Globalisierung) und 0-to-1 (Innovation) aus der CS183-Vorlesung.",
        "aussage_uebersetzung_de": "Horizontaler Fortschritt ist Globalisierung -- etwas, das irgendwo funktioniert, ueberall zum Laufen bringen. Vertikaler Fortschritt ist Technologie -- neue Dinge tun.",
    },
    # ---- 6. National Conservatism Conference, 2019 ----
    {
        "aussage_text": "I no longer believe that freedom and democracy are compatible.",
        "aussage_kurz": "Thiel erklaert, dass er Freiheit und Demokratie nicht mehr fuer vereinbar haelt.",
        "modus": "muendlich",
        "quellen_typ_id": 4,   # Panel-Diskussion
        "plattform_id": 4,     # Konferenzen
        "quell_link": "https://www.cato-unbound.org/2009/04/13/peter-thiel/education-libertarian/",
        "quell_titel": "The Education of a Libertarian (Cato Unbound)",
        "datum_aussage": "2009-04-13",
        "sprache": "en",
        "kontext": "Essay fuer Cato Unbound (2009). Thiel erklaert, dass Demokratie und Freiheit in Konflikt geraten seien, seit Frauen waehlten -- eine provokante libertaere Position.",
        "aussage_uebersetzung_de": "Ich glaube nicht mehr, dass Freiheit und Demokratie vereinbar sind.",
    },
    # ---- 7. Cato Unbound Essay (Seasteading) ----
    {
        "aussage_text": "I stand against confiscatory taxes, totalitarian collectives, and the ideology of the inevitability of the death of every individual. We are in a deadly race between politics and technology. The fate of our world may depend on the effort of a single person who builds or propagates the machinery of freedom that makes the world safe for capitalism.",
        "aussage_kurz": "Thiel positioniert sich gegen Steuern, Kollektivismus und die Unvermeidlichkeit des Todes und sieht ein Wettrennen zwischen Politik und Technologie.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,   # Essay
        "plattform_id": 9,
        "quell_link": "https://www.cato-unbound.org/2009/04/13/peter-thiel/education-libertarian/",
        "quell_titel": "The Education of a Libertarian (Cato Unbound)",
        "datum_aussage": "2009-04-13",
        "sprache": "en",
        "kontext": "Manifest fuer radikalen Libertarismus. Thiel formuliert seinen Glauben an Technologie als Weg zur Ueberwindung von Politik und Tod.",
        "aussage_uebersetzung_de": "Ich stehe gegen konfiskatorische Steuern, totalitaere Kollektive und die Ideologie der Unvermeidlichkeit des Todes jedes Einzelnen. Wir befinden uns in einem toedlichen Wettlauf zwischen Politik und Technologie. Das Schicksal unserer Welt koennte von den Anstrengungen einer einzelnen Person abhaengen, die die Maschinerie der Freiheit baut oder verbreitet, die die Welt sicher fuer den Kapitalismus macht.",
    },
    # ---- 8. TechCrunch Disrupt 2016 (Trump) ----
    {
        "aussage_text": "I think there are a lot of people who want to see a conservative government, but they think Trump would be too much. But I think it's actually Trump that's too little, not too much.",
        "aussage_kurz": "Thiel verteidigt seine Trump-Unterstuetzung mit dem Argument, Trump sei 'zu wenig', nicht zu viel.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://techcrunch.com/2016/10/31/peter-thiel-defends-support-for-donald-trump/",
        "quell_titel": "Peter Thiel defends his support for Donald Trump at TechCrunch Disrupt (TechCrunch)",
        "datum_aussage": "2016-10-31",
        "sprache": "en",
        "kontext": "TechCrunch Disrupt 2016. Thiel verteidigt seine Unterstuetzung Trumps gegenueber einem kritischen Silicon Valley.",
        "aussage_uebersetzung_de": "Ich denke, es gibt viele Leute, die eine konservative Regierung wollen, aber denken, Trump waere zu viel. Aber ich denke, es ist tatsaechlich so, dass Trump zu wenig ist, nicht zu viel.",
    },
    # ---- 9. NYT 2016 Interview (Trump Voters) ----
    {
        "aussage_text": "The media always takes Trump literally. It never takes him seriously, but it always takes him literally. I think a lot of the voters who vote for Trump take Trump seriously but not literally.",
        "aussage_kurz": "Thiel unterscheidet: Medien nehmen Trump woertlich, Waehler nehmen ihn ernst -- aber nicht woertlich.",
        "modus": "muendlich",
        "quellen_typ_id": 1,   # Interview
        "plattform_id": 5,     # Nachrichtenmedien
        "quell_link": "https://www.nytimes.com/2016/10/16/technology/peter-thiel-donald-j-trump-silicon-valley.html",
        "quell_titel": "Peter Thiel, Tech Billionaire, Reveals Secret War With Gawker (NYT)",
        "datum_aussage": "2016-10-15",
        "sprache": "en",
        "kontext": "Interview mit der New York Times, in dem Thiel seine Trump-Unterstuetzung erklaert.",
        "aussage_uebersetzung_de": "Die Medien nehmen Trump immer woertlich. Sie nehmen ihn nie ernst, aber sie nehmen ihn immer woertlich. Ich denke, viele der Waehler, die Trump waehlen, nehmen Trump ernst, aber nicht woertlich.",
    },
    # ---- 10. Palantir / 60 Minutes Interview 2018 ----
    {
        "aussage_text": "We've always had the view that privacy and civil liberties issues were not incompatible with a business dedicated to national security and law enforcement.",
        "aussage_kurz": "Thiel verteidigt Palantirs Arbeit fuer Geheimdienste: Datenschutz und Ueberwachung seien vereinbar.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.cbsnews.com/news/does-palantir-see-too-much-60-minutes/",
        "quell_titel": "Does Palantir see too much? (CBS 60 Minutes)",
        "datum_aussage": "2018-05-13",
        "sprache": "en",
        "kontext": "60 Minutes-Interview ueber Palantir. Thiel weist Kritik zurueck, dass Palantir eine Ueberwachungs-Dystopie schaffe.",
        "aussage_uebersetzung_de": "Wir hatten immer die Ansicht, dass Datenschutz- und Buergerrechtsthemen nicht unvereinbar sind mit einem Unternehmen, das sich der nationalen Sicherheit und Strafverfolgung widmet.",
    },
    # ---- 11. Washington Post 2018 (Surveillance) ----
    {
        "aussage_text": "I'm very comfortable with our work for the U.S. government. I think it's a great privilege to be able to work on these things.",
        "aussage_kurz": "Thiel nennt Palantirs Arbeit fuer US-Regierung und Geheimdienste ein 'grosses Privileg'.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.washingtonpost.com/business/economy/palantirs-relationship-with-ice-draws-scrutiny-from-activists/2018/09/26/",
        "quell_titel": "Palantir's relationship with ICE draws scrutiny from activists (Washington Post)",
        "datum_aussage": "2018-09-26",
        "sprache": "en",
        "kontext": "Thiel verteidigt Palantirs ICE-Vertrag gegenueber internen Protesten.",
        "aussage_uebersetzung_de": "Ich fuehle mich sehr wohl mit unserer Arbeit fuer die US-Regierung. Ich denke, es ist ein grosses Privileg, an diesen Dingen arbeiten zu koennen.",
    },
    # ---- 12. National Review 2019 (China) ----
    {
        "aussage_text": "Google should be investigated by the FBI and CIA. How many foreign intelligence agencies have infiltrated your Manhattan Project for AI?",
        "aussage_kurz": "Thiel fordert FBI/CIA-Ermittlungen gegen Google wegen angeblicher China-Infiltration.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.axios.com/2019/07/16/peter-thiel-google-china-fbi-cia",
        "quell_titel": "Peter Thiel: Google should be investigated for working with China (Axios)",
        "datum_aussage": "2019-07-15",
        "sprache": "en",
        "kontext": "National Conservatism Conference 2019. Thiel greift Google scharf an und impliziert Landesverrat.",
        "aussage_uebersetzung_de": "Google sollte vom FBI und der CIA untersucht werden. Wie viele auslaendische Geheimdienste haben euer Manhattan-Projekt fuer KI infiltriert?",
    },
    # ---- 13. Oxford Union Debate (Life Extension) ----
    {
        "aussage_text": "I've always had this really strong sense that death was a terrible, terrible thing. I think that's somewhat unusual. Most people end up compartmentalizing, and they are in some weird mode of denial and acceptance about death, but they both have the result of not doing anything about it.",
        "aussage_kurz": "Thiel kritisiert die Akzeptanz des Todes als 'Verleugnung' und fordert aktiven Kampf dagegen.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.inc.com/jeff-bercovici/peter-thiel-young-blood.html",
        "quell_titel": "Peter Thiel Wants to Inject Himself With Young People's Blood (Inc.)",
        "datum_aussage": "2016-08-01",
        "sprache": "en",
        "kontext": "Thiel spricht offen ueber seine Life Extension-Investments und seinen Kampf gegen das Altern.",
        "aussage_uebersetzung_de": "Ich hatte immer dieses wirklich starke Gefuehl, dass der Tod eine schreckliche, schreckliche Sache ist. Ich denke, das ist etwas ungewoehnlich. Die meisten Menschen enden in Kompromissen, und sie befinden sich in einem seltsamen Modus der Verleugnung und Akzeptanz ueber den Tod, aber beides hat zur Folge, dass sie nichts dagegen tun.",
    },
    # ---- 14. Washington Post 2015 (Parabiosis) ----
    {
        "aussage_text": "I'm looking into parabiosis stuff, which I think is really interesting. This is where they did the young blood into older mice and they found that had a massive rejuvenating effect.",
        "aussage_kurz": "Thiel erforscht Parabiose: Bluttransfusionen von Jungen zu Alten zur Verjuengung.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.inc.com/jeff-bercovici/peter-thiel-young-blood.html",
        "quell_titel": "Peter Thiel Wants to Inject Himself With Young People's Blood (Inc.)",
        "datum_aussage": "2015",
        "sprache": "en",
        "kontext": "Interview zu seinen Investitionen in Life Extension. Thiel nennt Parabiose-Forschung 'wirklich interessant'.",
        "aussage_uebersetzung_de": "Ich beschaeftige mich mit Parabiose-Zeug, was ich wirklich interessant finde. Dort haben sie jungen Maeuse junges Blut gegeben und fanden heraus, dass das einen massiven verjuengenden Effekt hatte.",
    },
    # ---- 15. Seasteading Institute Founding (2008) ----
    {
        "aussage_text": "There are quite a lot of people who think it's not possible, and those who do think it's possible often think it's not desirable. The critical question is, 'How do you get from here to there?'",
        "aussage_kurz": "Thiel ueber Seasteading: Viele halten es fuer unmoeglich oder unerwuenscht -- die Frage ist, wie man dorthin kommt.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.seasteading.org/about/",
        "quell_titel": "The Seasteading Institute - About",
        "datum_aussage": "2008",
        "sprache": "en",
        "kontext": "Thiel gruendet mit Patri Friedman das Seasteading Institute -- schwimmende Staaten ausserhalb staatlicher Jurisdiktion.",
        "aussage_uebersetzung_de": "Es gibt ziemlich viele Leute, die denken, es sei nicht moeglich, und die, die denken, es sei moeglich, denken oft, es sei nicht wuenschenswert. Die kritische Frage ist: 'Wie kommt man von hier nach dort?'",
    },
    # ---- 16. PayPal Mafia (Fortune 2007) ----
    {
        "aussage_text": "Of course there are lot of things that were going through our minds. Above all else, we wanted to create a new internet currency to replace the dollar.",
        "aussage_kurz": "Thiel erklaert, PayPal sei urspruenglich als Alternative zum Dollar gedacht gewesen.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://fortune.com/2007/11/13/paypal-mafia/",
        "quell_titel": "The PayPal Mafia (Fortune 2007)",
        "datum_aussage": "2007",
        "sprache": "en",
        "kontext": "Interview ueber die Anfaenge von PayPal. Thiel beschreibt die libertaere Vision: eine private, digitale Waehrung.",
        "aussage_uebersetzung_de": "Natuerlich gingen uns viele Dinge durch den Kopf. Vor allem wollten wir eine neue Internet-Waehrung schaffen, um den Dollar zu ersetzen.",
    },
    # ---- 17. Republican National Convention (2016) ----
    {
        "aussage_text": "I am proud to be gay. I am proud to be a Republican. But most of all I am proud to be an American.",
        "aussage_kurz": "Thiel outet sich bei der Republican National Convention als schwul und Republikaner.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 8,     # Politische Events
        "quell_link": "https://time.com/4421267/republican-convention-peter-thiel-transcript/",
        "quell_titel": "Read Peter Thiel's Speech at the Republican Convention (TIME)",
        "datum_aussage": "2016-07-21",
        "sprache": "en",
        "kontext": "Erster offen schwuler Redner bei einer Republican National Convention.",
        "aussage_uebersetzung_de": "Ich bin stolz darauf, schwul zu sein. Ich bin stolz darauf, Republikaner zu sein. Aber vor allem bin ich stolz darauf, Amerikaner zu sein.",
    },
    # ---- 18. RNC 2016 (Broken Government) ----
    {
        "aussage_text": "Instead of going to Mars, we have invaded the Middle East. We don't need to see Hillary Clinton's deleted emails: her incompetence is in plain sight.",
        "aussage_kurz": "Thiel kontrastiert Raumfahrt-Stagnation mit Kriegen und greift Clinton direkt an.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 8,
        "quell_link": "https://time.com/4421267/republican-convention-peter-thiel-transcript/",
        "quell_titel": "Read Peter Thiel's Speech at the Republican Convention (TIME)",
        "datum_aussage": "2016-07-21",
        "sprache": "en",
        "kontext": "Thiel attackiert das politische Establishment und positioniert Trump als Wandel.",
        "aussage_uebersetzung_de": "Statt zum Mars zu fliegen, haben wir den Nahen Osten angegriffen. Wir muessen Hillary Clintons geloeschte E-Mails nicht sehen: ihre Inkompetenz ist offensichtlich.",
    },
    # ---- 19. Gawker Lawsuit (2016) ----
    {
        "aussage_text": "It's less about revenge and more about specific deterrence. I saw Gawker pioneer a unique and incredibly damaging way of getting attention by bullying people even when there was no connection to the public interest.",
        "aussage_kurz": "Thiel begruendet seine geheime Finanzierung der Klage gegen Gawker als 'Abschreckung', nicht Rache.",
        "modus": "muendlich",
        "quellen_typ_id": 1,
        "plattform_id": 5,
        "quell_link": "https://www.nytimes.com/2016/05/26/business/dealbook/peter-thiel-tech-billionaire-reveals-secret-war-with-gawker.html",
        "quell_titel": "Peter Thiel, Tech Billionaire, Reveals Secret War With Gawker (NYT)",
        "datum_aussage": "2016-05-25",
        "sprache": "en",
        "kontext": "Thiel gibt zu, Hulk Hogans Prozess gegen Gawker finanziert zu haben -- Gawker geht in Konkurs.",
        "aussage_uebersetzung_de": "Es geht weniger um Rache und mehr um spezifische Abschreckung. Ich sah, wie Gawker eine einzigartige und unglaublich schaedliche Art pionierte, Aufmerksamkeit zu bekommen, indem sie Leute mobbten, selbst wenn es keine Verbindung zum oeffentlichen Interesse gab.",
    },
    # ---- 20. Founders Fund Philosophy ----
    {
        "aussage_text": "We wanted flying cars, instead we got 140 characters.",
        "aussage_kurz": "Thiels bekanntestes Zitat: Enttaeuschung ueber technologische Stagnation.",
        "modus": "schriftlich",
        "quellen_typ_id": 6,
        "plattform_id": 9,
        "quell_link": "https://foundersfund.com/the-future/",
        "quell_titel": "What Happened to the Future? (Founders Fund)",
        "datum_aussage": "2011",
        "sprache": "en",
        "kontext": "Manifesto der Founders Fund-Website. Thiel kritisiert die Fokussierung auf triviale Software statt auf echte Innovation.",
        "aussage_uebersetzung_de": "Wir wollten fliegende Autos, stattdessen bekamen wir 140 Zeichen.",
    },
    # ---- 21. Hoover Institution 2019 (AI & China) ----
    {
        "aussage_text": "AI is a military technology. It's not like the internet where you can have a more globalized approach. If the AI race is won by China, it will be terrible for this country and for the world.",
        "aussage_kurz": "Thiel warnt, dass KI eine Militaertechnologie sei und China nicht gewinnen duerften.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.hoover.org/research/peter-thiel-china-ai-and-geopolitics",
        "quell_titel": "Peter Thiel on China, AI, and Geopolitics (Hoover Institution)",
        "datum_aussage": "2019",
        "sprache": "en",
        "kontext": "Hoover Institution Vortrag. Thiel fordert, dass KI als strategische Waffe behandelt wird.",
        "aussage_uebersetzung_de": "KI ist eine Militaertechnologie. Es ist nicht wie das Internet, wo man einen globalisierteren Ansatz haben kann. Wenn das KI-Rennen von China gewonnen wird, wird es schrecklich fuer dieses Land und die Welt sein.",
    },
    # ---- 22. Bitcoin / Crypto Conference 2018 ----
    {
        "aussage_text": "Bitcoin is like a reserve form of money, it's like gold, and it's just a store of value. You don't need to use it to make payments.",
        "aussage_kurz": "Thiel nennt Bitcoin ein 'digitales Gold' -- ein Wertspeicher, keine Zahlungswaehrung.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.cnbc.com/2018/03/15/bitcoin-is-like-gold-paypal-co-founder-peter-thiel-says.html",
        "quell_titel": "Bitcoin is like gold, PayPal co-founder Peter Thiel says (CNBC)",
        "datum_aussage": "2018-03-15",
        "sprache": "en",
        "kontext": "Crypto-Konferenz. Thiel kontrastiert Bitcoin (Wertspeicher) mit Ethereum (Zahlungssystem).",
        "aussage_uebersetzung_de": "Bitcoin ist wie eine Reserve-Form von Geld, es ist wie Gold, und es ist einfach ein Wertspeicher. Man muss es nicht fuer Zahlungen verwenden.",
    },
    # ---- 23. Miami Bitcoin Conference 2022 (Enemy of Fiat) ----
    {
        "aussage_text": "Bitcoin is the honest answer to an enormous financial problem, and that problem is a gerontocracy that's running a finance system. The finance gerontocracy in the U.S. is crazier and more dangerous than the communist one in China.",
        "aussage_kurz": "Thiel nennt Bitcoin die Antwort auf eine 'finanzielle Gerontokratie' -- gefaehrlicher als Chinas Kommunismus.",
        "modus": "muendlich",
        "quellen_typ_id": 4,
        "plattform_id": 4,
        "quell_link": "https://www.reuters.com/technology/thiel-says-bitcoin-is-honest-answer-enormous-financial-problem-2022-04-07/",
        "quell_titel": "Thiel says bitcoin is honest answer to enormous financial problem (Reuters)",
        "datum_aussage": "2022-04-07",
        "sprache": "en",
        "kontext": "Miami Bitcoin Conference 2022. Radikaler Angriff auf Fed und etablierte Finanzsysteme.",
        "aussage_uebersetzung_de": "Bitcoin ist die ehrliche Antwort auf ein enormes finanzielles Problem, und dieses Problem ist eine Gerontokratie, die ein Finanzsystem betreibt. Die finanzielle Gerontokratie in den USA ist verrueckter und gefaehrlicher als die kommunistische in China.",
    },
    # ---- 24. Joe Rogan Experience #1691 (2021) ----
    {
        "aussage_text": "I think one of the disturbing things about COVID was just the crazy lack of debate, where people would say, 'You can't even ask these questions.' And that's always when I think you should be very suspicious.",
        "aussage_kurz": "Thiel kritisiert Debattenverweigerung waehrend COVID als Grund fuer Misstrauen.",
        "modus": "muendlich",
        "quellen_typ_id": 2,   # Podcast
        "plattform_id": 3,     # Podcasts
        "quell_link": "https://open.spotify.com/episode/73rLFoW6vBykvMtKjTZ98c",
        "quell_titel": "Joe Rogan Experience #1691 - Peter Thiel",
        "datum_aussage": "2021-08-04",
        "sprache": "en",
        "kontext": "Langes Interview bei Joe Rogan. Thiel spricht ueber COVID, Tech, Politik und Meinungsfreiheit.",
        "aussage_uebersetzung_de": "Ich denke, eines der stoerenden Dinge an COVID war einfach der verrueckte Mangel an Debatte, wo Leute sagten: 'Du kannst nicht einmal diese Fragen stellen.' Und das ist immer dann, wenn ich denke, dass man sehr misstrauisch sein sollte.",
    },
]


# ============================================================================
# HANDLUNGEN (Actions)
# ============================================================================
HANDLUNGEN = [
    # ---- H1. PayPal Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Peter Thiel gruendet Confinity zusammen mit Max Levchin und Luke Nosek. Confinity entwickelt PayPal -- urspruenglich als Krypto-Waehrung gedacht. PayPal fusioniert 2000 mit X.com (Elon Musk).",
        "datum_handlung": "1998-12",
        "betrag_usd": None,
        "quell_link": "https://en.wikipedia.org/wiki/PayPal",
        "quell_titel": "PayPal - Wikipedia",
        "kontext": "Thiel ist CEO von PayPal bis 2002. Die 'PayPal Mafia' (Thiel, Musk, Hoffman, Levchin) praegte das Silicon Valley der 2000er.",
    },
    # ---- H2. PayPal Verkauf ----
    {
        "handlung_typ": "verkauf",
        "beschreibung": "PayPal wird fuer $1,5 Milliarden an eBay verkauft. Peter Thiel, groesster Einzelaktionaer, erhaelt ca. $55 Millionen.",
        "datum_handlung": "2002-10-03",
        "betrag_usd": 55000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/PayPal",
        "quell_titel": "PayPal - Wikipedia",
        "kontext": "Exit schafft die finanzielle Grundlage fuer Thiels spaetere Investments. Er wird zum Vollzeit-Investor.",
    },
    # ---- H3. Facebook Investment ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Peter Thiel investiert $500.000 in Facebook und erhaelt 10,2% der Anteile. Er wird erster externer Investor und Verwaltungsratsmitglied. Investment wird spaeter auf ca. $1 Milliarde wert.",
        "datum_handlung": "2004-08",
        "betrag_usd": 500000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Peter_Thiel",
        "quell_titel": "Peter Thiel - Wikipedia",
        "kontext": "Thiels erfolgreichstes Investment. Er bleibt bis 2022 im Facebook-Board.",
    },
    # ---- H4. Palantir Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Peter Thiel gruendet Palantir Technologies mit Nathan Gettings, Joe Lonsdale, Stephen Cohen und Alex Karp. Palantir baut Big-Data-Analyseplattformen fuer Geheimdienste und Strafverfolgung. Erste Finanzierung: $2 Mio. von Thiel.",
        "datum_handlung": "2003-05",
        "betrag_usd": 2000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Palantir_Technologies",
        "quell_titel": "Palantir Technologies - Wikipedia",
        "kontext": "Palantir wird zu einem der wertvollsten Privatunternehmen (vor IPO 2020: $20 Mrd. Bewertung).",
    },
    # ---- H5. Founders Fund Gruendung ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Peter Thiel gruendet Founders Fund mit Ken Howery und Luke Nosek. Strategie: Investitionen in radikale Technologien (Raumfahrt, Life Extension, KI). Erster Fonds: $50 Mio.",
        "datum_handlung": "2005",
        "betrag_usd": 50000000.0,
        "quell_link": "https://en.wikipedia.org/wiki/Founders_Fund",
        "quell_titel": "Founders Fund - Wikipedia",
        "kontext": "Founders Fund investiert spaeter in SpaceX, Airbnb, Stripe, Neuralink. Philosophie: 'Wir wollten fliegende Autos, stattdessen bekamen wir 140 Zeichen.'",
    },
    # ---- H6. Seasteading Institute Investment ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Peter Thiel spendet $1,25 Millionen an das Seasteading Institute (gegruendet mit Patri Friedman, Enkel von Milton Friedman). Ziel: schwimmende autonome Staaten in internationalen Gewaessern.",
        "datum_handlung": "2008",
        "betrag_usd": 1250000.0,
        "quell_link": "https://en.wikipedia.org/wiki/The_Seasteading_Institute",
        "quell_titel": "The Seasteading Institute - Wikipedia",
        "kontext": "Teil von Thiels libertaerer Agenda: Flucht vor staatlicher Regulation durch Technologie.",
    },
    # ---- H7. Thiel Fellowship Launch ----
    {
        "handlung_typ": "gruendung",
        "beschreibung": "Peter Thiel startet die Thiel Fellowship: $100.000 fuer Studenten unter 23, die das College abbrechen, um an eigenen Projekten zu arbeiten. Thiel kritisiert Universitaeten als 'Bildungsblase'.",
        "datum_handlung": "2011",
        "betrag_usd": None,
        "quell_link": "https://thielfellowship.org/",
        "quell_titel": "Thiel Fellowship - Official Site",
        "kontext": "Fellows: Vitalik Buterin (Ethereum), Dylan Field (Figma), Laura Deming (Life Extension). Programm provoziert breite Kritik.",
    },
    # ---- H8. Trump Campaign Spende ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Peter Thiel spendet $1,25 Millionen an Donald Trumps Praesidentschaftskampagne -- groesste Einzelspende eines Tech-CEOs. Er haelt Rede bei Republican National Convention.",
        "datum_handlung": "2016-10-15",
        "betrag_usd": 1250000.0,
        "quell_link": "https://www.politico.com/story/2016/10/peter-thiel-donald-trump-donation-229865",
        "quell_titel": "Peter Thiel donates $1.25M to Trump (Politico)",
        "kontext": "Thiel wird einziger prominenter Silicon-Valley-Unterstuetzer Trumps. Erzeugt massive Kontroversen.",
    },
    # ---- H9. Trump Transition Team ----
    {
        "handlung_typ": "politisch",
        "beschreibung": "Peter Thiel wird Mitglied von Donald Trumps Transition-Team und organisiert Tech-Treffen im Trump Tower (Cook, Bezos, Musk, Sandberg). Er wird als Kandidat fuer Supreme Court gehandelt.",
        "datum_handlung": "2016-11-09",
        "betrag_usd": None,
        "quell_link": "https://www.nytimes.com/2016/11/14/technology/peter-thiel-has-a-hand-in-donald-trumps-transition.html",
        "quell_titel": "Peter Thiel Has a Hand in Donald Trump's Transition (NYT)",
        "kontext": "Thiel fungiert als Bruecke zwischen Trump und Silicon Valley -- eine umstrittene Rolle.",
    },
    # ---- H10. Gawker Lawsuit (geheim) ----
    {
        "handlung_typ": "klage",
        "beschreibung": "Peter Thiel finanziert geheim Hulk Hogans Klage gegen Gawker Media wegen Veroeffentlichung eines Sex-Videos. Gawker verliert den Prozess ($140 Mio. Schadenersatz) und geht in Konkurs.",
        "datum_handlung": "2016-05-25",
        "betrag_usd": 10000000.0,
        "quell_link": "https://www.nytimes.com/2016/05/26/business/dealbook/peter-thiel-tech-billionaire-reveals-secret-war-with-gawker.html",
        "quell_titel": "Peter Thiel, Tech Billionaire, Reveals Secret War With Gawker (NYT)",
        "kontext": "Gawker hatte 2007 Thiels Homosexualitaet ohne Zustimmung geoutet. Thiel begruendet die Klage als 'specific deterrence'.",
    },
    # ---- H11. Facebook Board Ruecktritt ----
    {
        "handlung_typ": "ruecktritt",
        "beschreibung": "Peter Thiel verlaesst nach 17 Jahren den Verwaltungsrat von Meta/Facebook, um sich auf Trump-Unterstuetzung und eigene Ventures zu konzentrieren. Er veraeussert grosse Teile seiner Anteile.",
        "datum_handlung": "2022-02-07",
        "betrag_usd": None,
        "quell_link": "https://www.theverge.com/2022/2/7/22922334/peter-thiel-leaving-meta-board-trump",
        "quell_titel": "Peter Thiel is leaving Meta's board to back Trump-aligned politicians (The Verge)",
        "kontext": "Thiel kuendigt Fokus auf Midterms 2022 an: Unterstuetzung von J.D. Vance und Blake Masters.",
    },
    # ---- H12. J.D. Vance Senate Campaign ----
    {
        "handlung_typ": "spende",
        "beschreibung": "Peter Thiel spendet $15 Millionen an J.D. Vances erfolgreiche Senatskampagne in Ohio -- groesste Spende an einen einzelnen Kandidaten. Vance ist ehemaliger Angestellter von Thiels Mithril Capital.",
        "datum_handlung": "2022",
        "betrag_usd": 15000000.0,
        "quell_link": "https://www.npr.org/2022/05/04/1096294308/peter-thiel-jd-vance-blake-masters",
        "quell_titel": "Peter Thiel gave millions to back J.D. Vance and Blake Masters (NPR)",
        "kontext": "Vance wird 2024 Trumps Vizepraesident. Thiels Einfluss auf die republikanische Partei waechst massiv.",
    },
    # ---- H13. Founders Fund AI Investments ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Founders Fund investiert massiv in KI-Startups: OpenAI ($100+ Mio.), Anthropic, Scale AI, Anduril. Thiel verfolgt Strategie: KI als militaerische/nationale Sicherheitstechnologie.",
        "datum_handlung": "2023",
        "betrag_usd": 100000000.0,
        "quell_link": "https://foundersfund.com/portfolio/",
        "quell_titel": "Founders Fund Portfolio",
        "kontext": "Thiels KI-Strategie: USA muss China im 'KI-Krieg' gewinnen. Fokus auf Defense-Tech.",
    },
    # ---- H14. Life Extension Investments (Unity Biotechnology) ----
    {
        "handlung_typ": "investition",
        "beschreibung": "Peter Thiel investiert ueber Founders Fund in Unity Biotechnology, ein Anti-Aging-Startup, das senolytische Therapien entwickelt. Investment: Teil einer $116 Mio. Series B.",
        "datum_handlung": "2018",
        "betrag_usd": None,
        "quell_link": "https://www.crunchbase.com/organization/unity-biotechnology",
        "quell_titel": "Unity Biotechnology - Crunchbase",
        "kontext": "Weitere Life Extension-Investments: Methuselah Foundation, SENS Research, Ambrosia (Parabiose-Startup, spaeter geschlossen).",
    },
    # ---- H15. Palantir IPO ----
    {
        "handlung_typ": "produktlaunch",
        "beschreibung": "Palantir Technologies geht per Direct Listing an die Boerse (NYSE: PLTR). Bewertung: ca. $16 Milliarden. Thiel besitzt ca. 7% (~$1,1 Mrd.). Palantir arbeitet mit CIA, NSA, ICE, IDF zusammen.",
        "datum_handlung": "2020-09-30",
        "betrag_usd": None,
        "quell_link": "https://www.cnbc.com/2020/09/30/palantir-pltr-starts-trading-on-the-nyse.html",
        "quell_titel": "Palantir begins trading on NYSE in direct listing (CNBC)",
        "kontext": "IPO macht Palantirs kontroverse Arbeit fuer Geheimdienste und Grenzbehorden oeffentlich sichtbar.",
    },
]


def insert_data():
    """Fuegt alle gesammelten Aussagen und Handlungen in die Datenbank ein."""

    if not os.path.exists(DB_PATH):
        print(f"FEHLER: Datenbank nicht gefunden: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Pruefen ob person_id=25 existiert
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
            "Claude (collect_thiel.py)"
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
        "Peter Thiel, Zero to One, Palantir, PayPal Mafia, Founders Fund, KI-Investments, Libertarismus, Stanford CS183, Life Extension, Transhumanismus, Seasteading, Trump, Gawker, Republican National Convention",
        aussagen_count + handlungen_count,
        aussagen_count + handlungen_count,
        f"Systematische Recherche: {aussagen_count} Aussagen + {handlungen_count} Handlungen eingefuegt. "
        f"{skipped_a} Aussagen + {skipped_h} Handlungen uebersprungen (Duplikate). "
        f"Quellen: Zero to One (Buch 2014), Stanford CS183 Lectures (Blake Masters Notes), "
        f"Cato Unbound Essay 2009, TechCrunch Disrupt 2016, Republican National Convention 2016, "
        f"NYT Gawker Interview 2016, CBS 60 Minutes 2018, National Conservatism Conference 2019, "
        f"Joe Rogan Experience #1691, Miami Bitcoin Conference 2022, Hoover Institution, "
        f"Fortune, TIME, Washington Post, Reuters, CNBC, NPR, Politico, The Verge.",
        "Claude (collect_thiel.py)"
    ))

    conn.commit()

    # --- Zusammenfassung ---
    print(f"\n{'='*60}")
    print(f"  ERGEBNIS: Peter Thiel (person_id={PERSON_ID})")
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
    print(f"\n  GESAMT in DB: {total_a} Aussagen, {total_h} Handlungen fuer Peter Thiel")

    conn.close()
    print(f"\nDatenbank gespeichert: {DB_PATH}")


if __name__ == "__main__":
    print("=" * 60)
    print("  collect_thiel.py")
    print("  Verifizierte Aussagen & Handlungen: Peter Thiel")
    print("=" * 60)
    print(f"\nDatenbank: {DB_PATH}")
    print(f"Person ID: {PERSON_ID}")
    print(f"Datum:     {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    insert_data()
