#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datensammlung für Emad Mostaque (person_id=95)
Datenbank: aussagen_top100.db
Erstellt: 2026-02-12
"""

import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\User\OneDrive\Desktop\Forschung\Sozialwissenschaft\Transhumanismus\_data\aussagen_top100.db"
PERSON_ID = 95

def insert_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    aussagen_count = 0
    handlungen_count = 0

    # ==================== AUSSAGEN ====================

    aussagen = [
        # AI Impact & Future
        (PERSON_ID,
         "2024 is going to be the year of action and we will see exponential adoption. It's not a case of if, but when and the UK can lead the charge.",
         "2024 year of AI action and exponential adoption",
         "muendlich",
         "https://openuk.uk/thought-leadership/fireside-chat-emad-mostaque-2024-phase-one/",
         "Emad Mostaque, Founder, Stability AI from State of Open: The UK in 2024 Phase One - OpenUK",
         "2024-01-01",
         "en",
         "Statement about AI adoption in 2024"),

        (PERSON_ID,
         "I'm not sure that any of us can cope with the speed. You know, frankly it's terrifying.",
         "AI disruption speed is terrifying",
         "muendlich",
         "https://www.goldmansachs.com/insights/articles/stability-ai-ceo-says-ai-will-prove-more-disruptive-than-the-pandemic",
         "Stability AI CEO says AI will prove more disruptive than the pandemic | Goldman Sachs",
         "2023-01-01",
         "en",
         "Statement about AI's disruption potential"),

        (PERSON_ID,
         "You're not going to beat centralized AI with more centralized AI.",
         "Can't beat centralized AI with centralization",
         "muendlich",
         "https://techcrunch.com/2024/03/22/stability-ai-ceo-resigns-because-youre-not-going-to-beat-centralized-ai-with-more-centralized-ai/",
         "Stability AI CEO resigns because you can't beat centralized AI with more centralized AI | TechCrunch",
         "2024-03-22",
         "en",
         "Resignation statement emphasizing commitment to decentralized AI"),

        (PERSON_ID,
         "We're at this point whereby if we don't have AI to help us, I think we're in a very bad scenario. With AI, if we don't build it right, we're also in a bad scenario. If AI is built right and is aligned and works with us, then we're in a very good scenario.",
         "AI alignment critical for humanity's future",
         "muendlich",
         "https://medium.com/@vardhanam.daga/10-brilliant-ai-insights-from-stability-ais-founder-emad-mostaque-182905c11a60",
         "10 Brilliant AI Insights from Stability AI's Founder Emad Mostaque | by Vardhanam Daga | Medium",
         "2023-01-01",
         "en",
         "Statement on AI's critical importance and alignment"),

        (PERSON_ID,
         "The world becomes a better place, ironically, through empathy from AI, and that's infrastructure that should be available to everyone. This is a concept we call universal basic AI.",
         "Universal basic AI creates empathy infrastructure",
         "muendlich",
         "https://www.cognitiverevolution.ai/emad-mostaque-on-the-intelligent-internet-and-universal-basic-ai/",
         "Emad Mostaque on the Intelligent Internet and Universal Basic AI",
         "2023-01-01",
         "en",
         "Introducing concept of universal basic AI"),

        # Programmers & Job Replacement
        (PERSON_ID,
         "There will be no programmers in five years.",
         "No human programmers in 5 years",
         "muendlich",
         "https://decrypt.co/147191/no-human-programmers-five-years-ai-stability-ceo",
         "Stability AI CEO: There Will Be No (Human) Programmers in Five Years - Decrypt",
         "2023-06-01",
         "en",
         "Prediction about AI replacing programmers"),

        (PERSON_ID,
         "41% of all code right now is AI generated.",
         "41% of code is AI-generated",
         "muendlich",
         "https://decrypt.co/147191/no-human-programmers-five-years-ai-stability-ceo",
         "Stability AI CEO: There Will Be No (Human) Programmers in Five Years - Decrypt",
         "2023-06-01",
         "en",
         "Evidence for programmer replacement prediction"),

        # AI Bubble
        (PERSON_ID,
         "I think this will be the biggest bubble of all time.",
         "AI will be biggest bubble of all time",
         "muendlich",
         "https://www.cnbc.com/2023/07/17/ai-will-be-the-biggest-bubble-of-all-time-stability-ai-ceo.html",
         "AI will be the 'biggest bubble of all time': Stability AI CEO",
         "2023-07-17",
         "en",
         "Statement to UBS analysts about AI bubble"),

        (PERSON_ID,
         "It hasn't even started yet.",
         "AI bubble hasn't started yet",
         "muendlich",
         "https://www.cnbc.com/2023/07/17/ai-will-be-the-biggest-bubble-of-all-time-stability-ai-ceo.html",
         "AI will be the 'biggest bubble of all time': Stability AI CEO",
         "2023-07-17",
         "en",
         "Continuation of AI bubble statement"),

        # Open Source & Democratization
        (PERSON_ID,
         "You're not going to beat centralized AI with more centralized AI. You're not going to beat centralized AI with more centralized AI.",
         "Decentralization necessary to counter centralized AI",
         "muendlich",
         "https://sifted.eu/articles/stable-diffusion-ai-emad-mostaque",
         "Stability AI's Emad Mostaque says OpenAI 'fundamentally wrong' to block Ukrainians| Sifted",
         "2023-01-01",
         "en",
         "Core philosophy on AI development"),

        (PERSON_ID,
         "OpenAI decided not to allow any Ukrainian content or Ukrainians to use it.",
         "OpenAI blocks Ukrainians from ChatGPT",
         "muendlich",
         "https://sifted.eu/articles/stable-diffusion-ai-emad-mostaque",
         "Stability AI's Emad Mostaque says OpenAI 'fundamentally wrong' to block Ukrainians| Sifted",
         "2023-01-01",
         "en",
         "Criticism of OpenAI's access restrictions"),

        (PERSON_ID,
         "Blocking people from using technology — as OpenAI has done with its ChatGPT service in Ukraine, China and Russia — is fundamentally wrong.",
         "Blocking technology access is fundamentally wrong",
         "muendlich",
         "https://sifted.eu/articles/stable-diffusion-ai-emad-mostaque",
         "Stability AI's Emad Mostaque says OpenAI 'fundamentally wrong' to block Ukrainians| Sifted",
         "2023-01-01",
         "en",
         "Moral stance against technology blocking"),

        # Economic Transformation
        (PERSON_ID,
         "Within 1,000 days, we'll reach a tipping point where AI systems begin replacing large portions of cognitive work as the cost of intelligence approaches that of electricity.",
         "AI will replace cognitive work in 1000 days",
         "muendlich",
         "https://danielmiessler.com/blog/emad-mostaque-on-the-end-of-capitalism",
         "Emad Mostaque on the End of Capitalism | Daniel Miessler",
         "2024-01-01",
         "en",
         "Prediction about AI's economic impact timeline"),

        (PERSON_ID,
         "We're at the terminal point of our current economic structure and questions fundamental concepts like the nature of money and value in a world of infinite abundance with billions of robots and trillions of agents.",
         "Current economic structure at terminal point",
         "muendlich",
         "https://singjupost.com/transcript-emad-mostaque-why-gdp-capitalism-is-obsolete-in-an-ai-world-impact-theory/",
         "Transcript: Emad Mostaque - Why GDP & Capitalism Is Obsolete in an AI World - Impact Theory",
         "2024-01-01",
         "en",
         "View on capitalism becoming obsolete"),

        (PERSON_ID,
         "Cancer is good for GDP and it makes it go up.",
         "GDP measures wrong things like cancer",
         "muendlich",
         "https://singjupost.com/transcript-emad-mostaque-why-gdp-capitalism-is-obsolete-in-an-ai-world-impact-theory/",
         "Transcript: Emad Mostaque - Why GDP & Capitalism Is Obsolete in an AI World - Impact Theory",
         "2024-01-01",
         "en",
         "Criticism of GDP as economic metric"),

        # UBI Alternative
        (PERSON_ID,
         "Universal Basic Income at poverty level would cost more than entire US tax base.",
         "Traditional UBI not scalable economically",
         "muendlich",
         "https://blog.biocomm.ai/2025/02/07/when-capital-no-longer-needs-labor-how-does-labor-gain-capital-by-emad-mostaque-jan-08-2025/",
         "When Capital No Longer Needs Labor, How Does Labor Gain Capital? By Emad Mostaque",
         "2025-01-08",
         "en",
         "Critique of traditional UBI approach"),

        # Education
        (PERSON_ID,
         "In 10 years, every single student in the world will have an AI tutor that helps them.",
         "Every student will have AI tutor in 10 years",
         "muendlich",
         "https://www.diamandis.com/blog/ai-education-healthcare-hollywood",
         "AI's Impact on Education, Healthcare & Hollywood",
         "2023-01-01",
         "en",
         "Prediction about AI in education"),

        # Healthcare
        (PERSON_ID,
         "In the not-too-distant future, the best diagnosticians in the world will be AIs, and the best surgeons will be robots driven by AIs. This is how we create an abundance of health globally.",
         "AI will become best diagnosticians and surgeons",
         "muendlich",
         "https://www.diamandis.com/blog/ai-education-healthcare-hollywood",
         "AI's Impact on Education, Healthcare & Hollywood",
         "2023-01-01",
         "en",
         "Vision for AI in healthcare"),

        # Superintelligence
        (PERSON_ID,
         "Superintelligence should be a collective intelligence made up of amplified human intelligence, versus an AGI that is top-down and designed to control us.",
         "Superintelligence should amplify humans not control them",
         "muendlich",
         "https://www.diamandis.com/blog/ai-education-healthcare-hollywood",
         "AI's Impact on Education, Healthcare & Hollywood",
         "2023-01-01",
         "en",
         "Philosophy on superintelligence development"),

        # Personal Motivation
        (PERSON_ID,
         "His motivation stems from his son being diagnosed with autism, with Emad wanting to see how AI could help review existing research.",
         "Son's autism diagnosis motivated AI healthcare work",
         "muendlich",
         "https://medium.com/@vardhanam.daga/10-brilliant-ai-insights-from-stability-ais-founder-emad-mostaque-182905c11a60",
         "10 Brilliant AI Insights from Stability AI's Founder Emad Mostaque | by Vardhanam Daga | Medium",
         "2020-01-01",
         "en",
         "Personal motivation for AI work in healthcare"),
    ]

    for aussage in aussagen:
        cursor.execute("""
            INSERT INTO aussagen (person_id, aussage_text, aussage_kurz, modus, quell_link, quell_titel, datum_aussage, sprache, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, aussage)
        aussagen_count += 1

    # ==================== HANDLUNGEN ====================

    handlungen = [
        # Company Founding
        (PERSON_ID,
         "gruendung",
         "Co-founded Stability AI with Cyrus Hodes, creating company behind Stable Diffusion AI image generator",
         "2020-12-01",
         "https://en.wikipedia.org/wiki/Stability_AI",
         "Stability AI - Wikipedia",
         "Late 2020 founding of Stability AI"),

        # Stable Diffusion Launch
        (PERSON_ID,
         "produktlaunch",
         "Launched Stable Diffusion as open-source AI image generation model, competing with DALL-E and Midjourney",
         "2022-08-01",
         "https://en.wikipedia.org/wiki/Emad_Mostaque",
         "Emad Mostaque - Wikipedia",
         "August 2022 public release of Stable Diffusion"),

        # Major Funding Round
        (PERSON_ID,
         "investition",
         "Secured $101 million investment led by Coatue and Lightspeed Venture Partners, reaching unicorn status at $1 billion valuation",
         "2022-10-01",
         "https://fortune.com/2024/03/27/inside-stability-ai-emad-mostaque-bad-breakup-vc-investors-coatue-lightspeed/",
         "Inside the $1 billion love affair between Stability AI's 'complicated' founder and tech investors | Fortune",
         "Funding round less than two years after founding"),

        # AWS Partnership
        (PERSON_ID,
         "partnerschaft",
         "Selected AWS as Stability AI's preferred cloud provider, using Amazon SageMaker for AI model development",
         "2022-11-30",
         "https://press.aboutamazon.com/2022/11/stability-ai-selects-aws-as-its-preferred-cloud-provider-to-build-artificial-intelligence-for-the-future",
         "Stability AI Selects AWS as Its Preferred Cloud Provider | AWS Press Center",
         "Partnership announcement for cloud infrastructure"),

        # Intel Investment
        (PERSON_ID,
         "investition",
         "Received $50 million investment from Intel (partial disbursement of planned $95 million), with $20 million initially disbursed",
         "2023-12-01",
         "https://www.theregister.com/2024/04/03/stability_ai_bills/",
         "Stability AI reportedly ran out of cash to pay its AWS bills | The Register",
         "Intel investment for Gaudi2 accelerator supercomputer"),

        # Co-founder Lawsuit
        (PERSON_ID,
         "klage",
         "Co-founder Cyrus Hodes filed lawsuit alleging fraud, claiming Mostaque deceived him into selling 15% stake for $100",
         "2023-07-01",
         "https://www.linkedin.com/posts/forbes-magazine_stability-ai-cofounder-says-emad-mostaque-activity-7085324033038135296-WtRl",
         "Forbes: Stability AI Cofounder Says Emad Mostaque Tricked Him Into Selling Stake",
         "Lawsuit alleging misrepresentation about company value before $1B valuation"),

        # Investor Pressure
        (PERSON_ID,
         "sonstiges",
         "Lightspeed Venture Partners sent letter to board stating Mostaque's mismanagement 'severely undermined' confidence, urged sale",
         "2023-10-01",
         "https://fortune.com/2024/03/27/inside-stability-ai-emad-mostaque-bad-breakup-vc-investors-coatue-lightspeed/",
         "Inside the $1 billion love affair between Stability AI | Fortune",
         "October 2023 investor letter criticizing CEO management"),

        # Mass Exodus
        (PERSON_ID,
         "sonstiges",
         "Core Stable Diffusion researchers Rombach, Blattmann and Lorenz resigned amid financial struggles and executive exodus",
         "2024-03-01",
         "https://petapixel.com/2024/03/25/stability-ai-ceo-emad-mostaque-resigns-amid-chaos-at-the-ai-image-generator-company/",
         "Stability AI CEO Emad Mostaque Resigns Amid Chaos | PetaPixel",
         "Mass resignation of key technical staff"),

        # CEO Resignation
        (PERSON_ID,
         "ruecktritt",
         "Resigned as CEO and board member of Stability AI to pursue decentralized AI initiatives after investor pressure",
         "2024-03-23",
         "https://www.bloomberg.com/news/articles/2024-03-23/startup-stability-ai-ceo-emad-mostaque-steps-down",
         "Startup Stability AI CEO Emad Mostaque Steps Down - Bloomberg",
         "Departure following months of investor pressure despite $5.4M monthly revenue"),

        # Leadership Transition
        (PERSON_ID,
         "umstrukturierung",
         "Stability AI appointed Shan Shan Wong (COO) and Christian Laforte (CTO) as interim co-CEOs after Mostaque's departure",
         "2024-03-24",
         "https://stability.ai/news/stabilityai-announcement",
         "Stability AI Announcement — Stability AI",
         "Leadership restructuring following CEO resignation"),

        # Schelling AI Foundation
        (PERSON_ID,
         "gruendung",
         "Founded Schelling AI to build open source AI code, models and datasets powered by 'AI money' and tokenized economics",
         "2024-06-07",
         "https://x.com/EMostaque/status/1799044420282826856",
         "Emad on X: Happy to announce @SchellingAI",
         "New venture focused on decentralized, culturally-aware AI systems"),

        # New Leadership at Stability
        (PERSON_ID,
         "sonstiges",
         "Prem Akkaraju announced as new Stability AI CEO, Sean Parker joined board as Executive Chairman with new funding round",
         "2024-06-25",
         "https://tracxn.com/d/companies/stability-ai/__j9m4iz5g2IAe2paU-Sre7UIBk1ByQZ0ippRUslXvqwc",
         "Stability AI - 2026 Company Profile | Tracxn",
         "Company transition to new leadership with fresh investment"),

        # WPP Investment
        (PERSON_ID,
         "investition",
         "Stability AI secured fresh funds from UK advertising group WPP as lead investor, shifting toward enterprise solutions",
         "2025-03-01",
         "https://tracxn.com/d/companies/stability-ai/__j9m4iz5g2IAe2paU-Sre7UIBk1ByQZ0ippRUslXvqwc",
         "Stability AI - 2026 Company Profile | Tracxn",
         "Investment marking shift to membership-based revenue model"),

        # Forbes Controversy
        (PERSON_ID,
         "sonstiges",
         "Forbes investigation alleged misrepresentations about Oxford degrees, AWS partnership, and role in Stable Diffusion creation",
         "2023-06-01",
         "https://petapixel.com/2023/06/05/so-many-things-dont-add-up-stability-ai-founder-accused-of-exaggerations/",
         "So Many Things Don't Add Up: Stability AI Founder Accused of Exaggerations | PetaPixel",
         "Controversial report citing 30+ sources alleging false claims"),

        # Financial Crisis
        (PERSON_ID,
         "sonstiges",
         "Stability AI reportedly defaulted on AWS and Google Cloud payments, with $99M annual infrastructure costs and shrinking cash",
         "2024-04-01",
         "https://www.theregister.com/2024/04/03/stability_ai_bills/",
         "Stability AI reportedly ran out of cash to pay its AWS bills | The Register",
         "Financial difficulties following CEO departure"),
    ]

    for handlung in handlungen:
        cursor.execute("""
            INSERT INTO handlungen (person_id, handlung_typ, beschreibung, datum_handlung, quell_link, quell_titel, kontext)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, handlung)
        handlungen_count += 1

    conn.commit()
    conn.close()

    return aussagen_count, handlungen_count

if __name__ == "__main__":
    print(f"Starte Datenimport für Emad Mostaque (person_id={PERSON_ID})...")
    print(f"Datenbank: {DB_PATH}")
    print()

    try:
        aussagen_count, handlungen_count = insert_data()
        print("=" * 60)
        print("IMPORT ERFOLGREICH ABGESCHLOSSEN")
        print("=" * 60)
        print(f"Eingefügte Aussagen:   {aussagen_count}")
        print(f"Eingefügte Handlungen: {handlungen_count}")
        print(f"Gesamt:                {aussagen_count + handlungen_count}")
        print("=" * 60)

    except Exception as e:
        print(f"FEHLER beim Import: {e}")
        import traceback
        traceback.print_exc()
