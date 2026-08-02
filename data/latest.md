# AI Fail Watch – 2026-08-02

## 1. Measuring LLMs’ Ability to Perform Cryptanalysis
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 28
**Link:** https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html

There’s new benchmark measuring AI’s ability to perform mathematical cryptanalysis. Anthropic’s frontier model actually found new attacks. The benchmark: “ CryptanalysisBench: Can LLMs do Cryptanalysis? ” The idea is to benchmark the ability of LLMs to discover new mathematical cryptanalytic attacks against a series of historical algorithms. Abstract: Cryptanalysis—the task of finding attacks against cryptographic schemes—its at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest. Cryptanalysis represents both a clean testbed for frontier reasoning (as practical attacks can be automatically verified) and a domain with unusually high stakes, since the primitives under study underpin our digital security. In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes. We introduce CryptanalysisBench, 191 tasks across six families of cryptographic primitives (block ciphers, hash functions, etc.) drawn primarily from four NIST standardization competitions. Our benchmark consists of three tiers: (i) primitives with known practical breaks; (ii) primitives with no known practical break, evaluated both at full strength and as scaled-down variants; and (iii) a challenge set of production primitives at the frontier of cryptanalysis. Five frontier models (Claude Opus 4.8, Sonnet 5, Mythos 5, GPT-5.5, and the open-weights GLM-5.2) break 65%­86% of Tier 1 schemes, 6­12 Tier-2 schemes at full strength, and 24­61 across all scaled-down variants. Beyond deriving known results, models produce novel cryptanalysis, such as a key-recovery attack that exploits a design flaw in the SpoC AEAD and an error in KINDI’s published CCA-security proof, both to the best of our knowledge not previously known...

---

## 2. FTSE 100 on track for best month since first US attacks on Iran five months ago – as it happened
**Source:** Technology | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 21
**Link:** https://www.theguardian.com/business/live/2026/jul/31/bp-sell-north-sea-ai-record-korea-kospi-stock-market-latest-news-updates

Live, rolling coverage as London’s biggest companies defy Middle East disruption and UK petrol prices rise to around £1.60 per litre, the highest since Donald Trump ordered renewed strikes The story piquing the interest of the financial press this morning is that of Leopold Aschenbrenner , the AI Wunderkind (he’s German-born) who has been forced to sell off his fund in a fire sale after the AI boom ran out of steam. The 24-year-old had persuaded a lot of people to give him a lot of money for a hedge fund, after previously working for OpenAI and the FTX Future Fund, a charitable arm of the fraudulent crypto empire of Sam Bankman-Fried, who is now in prison . Aschenbrenner ploughed that money into debt-fuelled bets on artificial intelligence companies, earning huge returns until he found out that stocks can also fall. The trader dubbed the “Nostradamus of AI” would have been hard-pressed to foresee how quickly his high-flying hedge fund would run into trouble. The firm’s rapid downward spiral is a familiar tale, as Silicon Valley and Wall Street once again threw their weight behind a bright-eyed but untested investor who promised this time would be different. “Everybody always wants to find the next golden child,” said one longtime hedge fund executive. “It just keeps happening.” In less than 24 hours — which included a conversation between Griffin and Aschenbrenner — Griffin’s Citadel hedge fund reached out to Situational Awareness and snapped up the investments at a discount, according to a person familiar with the matter who asked not to be identified citing private information. It was a startling reversal for Aschenbrenner, a former researcher at OpenAI who – before starting his hedge fund roughly two years ago — had no previous investment experience. His fledging firm has watched its assets plunge from $45bn at the start of July to about $10bn. Continue reading...

---

## 3. Flock surveillance cameras can pose a crash risk for drivers, US experts say
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/us-news/2026/jul/30/controversial-flock-ai-surveillance-camera-risk

Roadside safety advocates say some automated license plate readers may not meet highway safety standards Flock Safety cameras have been pilloried for facilitating the AI -powered surveillance of private citizens and for targeting immigrants for years. But now safety advocates are also claiming that their physical location can pose potential roadside hazards. At the bottom of a tree-lined hill on a narrow, two lane rural road in Greene county, Ohio, stands a black metal rod with a camera and solar panel attached at the top. Continue reading...

---

## 4. Hackers can use 9 of the most popular AI tools to assemble massive botnets
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 18
**Link:** https://arstechnica.com/security/2026/07/hackers-can-use-9-of-the-most-popular-ai-tools-to-assemble-massive-botnets/

"HalluSquatting" weaponizes LLMs' inability to say "I don't know."

---

## 5. Measuring the Tendency of AI Agents to Go Rogue
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 18
**Link:** https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html

This essay was written with Barath Raghavan, and originally appeared in The Guardian . In July, Hugging Face, a company that hosts much of the world’s AI software and open-source AI models, was hacked. A malicious dataset had been used to run code on one of its servers. Whoever was behind it captured internal security credentials and moved through systems over a weekend, running thousands of actions from a swarm of temporary server environments. It looked like the work of a sophisticated criminal group. It was not. It was one of OpenAI’s new, still unreleased GPT models...

---

## 6. Elon Musk’s xAI sues Minnesota over law banning ‘nudification’ technology
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/technology/2026/jul/29/xai-sues-minnesota-nudification-technology

First-in-nation law sets up test on states’ power to regulate use of AI as it tries to outlaw fake nude images of real people Elon Musk’s company xAI has sued Minnesota over the state’s first-in-the-nation law banning “nudification” technology on websites and apps, potentially providing a test for how far states can go in constitutionally regulating the use of artificial intelligence. Musk’s company sued on Monday in federal court, days before the law is set to take effect on Saturday and make Minnesota the first state to try to outlaw the increasingly proliferating technology that lets people use AI to create fake nude images of real people. The law was signed in May. Continue reading...

---

## 7. Anthropic’s Opus 5 Is Better at Resisting Prompt Injection
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 17
**Link:** https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html

The chart is interesting. On the IPI benchmark, Opus 5 improved over Opus 4.8, reducing the probability of an attacker succeeding within 15 attempts from 5.5% to 2.0%, and from 0.5% to 0.2% on 1 attempt. It also improved on Sonnet 5 (5.9% at k=15) and Mythos 5 (2.6%), making it the most robust model evaluated. Opus 5 also outperformed all non-Claude models on this benchmark. The most robust non-Claude model was Muse Spark at 16.5% within 15 attempts—more than eight times Opus 5’s rate. The most capable GPT 5.6 variant, Sol, was comparable to its predecessor GPT 5.5 (20.0% versus 20.8% within 15 attempts), and was 10 times as likely to be successfully attacked as Claude Opus 5 at 2.0%. The other GPT 5.6 variants are less robust, at 30.4% (Terra) and 43.9% (Luna). A single attempt against GPT 5.6 Sol succeeded 3.1% of the time, higher than the 2.0% an attacker achieved against Opus 5 after fifteen attempts...

---

## 8. Claude published malicious code to the Internet and attacked 3 real companies
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 16
**Link:** https://arstechnica.com/security/2026/07/likely-illegally-claude-gained-access-to-3-networks-will-anthropic-be-held-to-account/

Had the hacks used conventional methods, someone would likely go to prison.

---

## 9. $2m crime novel deal collapses amid questions over AI use
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 14
**Link:** https://www.theguardian.com/books/2026/jul/31/crime-novel-deal-collapses-questions-ai-jerry-falade-call-me-ill-hide-the-body

Agents withdraw Jerry Falade’s hotly anticipated debut after saying they can no longer authenticate ‘how the manuscript evolved’ A high-profile publishing deal for a debut crime novel has collapsed after doubts emerged over whether artificial intelligence played a role in writing it. The hotly anticipated manuscript Call Me, I’ll Hide the Body, by Jerry Falade, was withdrawn from sale by its agent despite reportedly receiving an offer for more than $2m (£1.5m) from Minotaur, owned by Macmillan US, as part of a 14-way auction. The plan was to publish it in 2028. Continue reading...

---

## 10. AI labels to be compulsory on authentic-looking content under EU rules
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 14
**Link:** https://www.theguardian.com/technology/2026/jul/31/ai-labels-to-be-compulsory-on-authentic-looking-content-under-eu-rules

Companies must ensure people know when they are interacting with artificially generated images, audio and text designed to look real From apparently conspiring to steal elections to abusing staff or performing embarrassing dance moves, the last few years have seen plenty of fake content made about politicians intended to malign its targets and mislead the public. Now EU rules aim to stem the flood of this deceptive content: starting from Sunday, artificially generated images, audio and text designed to look authentic must be labelled. Continue reading...

---
