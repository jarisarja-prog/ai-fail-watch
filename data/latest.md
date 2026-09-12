# AI Fail Watch – 2026-09-12

## 1. Stealing AI Reasoning Traces
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 40
**Link:** https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html

Interesting research: “ Stealing Reasoning Traces from Proprietary LLM APIs “: Abstract: Leading large language model providers now conceal their models’ step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different sessions, users, and models within a provider’s ecosystem. We exploit this compatibility to develop a scalable decryption jailbreak. By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly. This vulnerability enables four distinct attack vectors. First, it circumvents anti-distillation mechanisms, allowing adversaries to extract a proprietary model’s reasoning, as we demonstrate across Anthropic, OpenAI, and Google. Second, it allows for large-scale private data extraction. Developers frequently share session logs publicly, unaware of contents of the encrypted blocks. By decoding 315,320 reasoning blocks scraped from public repositories, we recovered 367 Personally Identifiable Information (PII) artifacts and 182 credentials. Third, it inadvertently reveals hazardous information hidden within the reasoning process, even in cases where the model’s final, visible output safely rejects a malicious request. Fourth, attackers can leverage this flaw to execute invisible prompt injections, embedding malicious payloads entirely within encrypted blocks to poison public agentic rollouts. Following responsible disclosure, we propose concrete cryptographic and system-level mitigations to secure client-side reasoning...

---

## 2. Conservatives split from Silicon Valley allies as datacenter backlash grows
**Source:** Technology | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 34
**Link:** https://www.theguardian.com/technology/2026/sep/01/datacenter-backlash-conservatives-silicon-valley

Tech companies have underestimated the opposition to energy-hungry datacenters – and experts predict the pushback will intensify Hello, and welcome to TechScape. I’m your host, Blake Montgomery, listening to Dolly Parton in the wake of her death. I was lucky enough to see her in concert a decade ago in California, in the same arena where Google now hosts its annual I/O conference. It’s been a long time, and all my iPhone 4 photos are so blurry you can barely tell it’s a musical performance, but my memory is clear enough to compensate. She told many stories about her childhood, which led into a trio of fabulous songs: My Tennessee Mountain Home, Applejack and Dr Robert F Thomas. They’re still my favorites. Siri, where does Apple go next? – podcast Apple’s Tim Cook leaves behind complicated legacy on privacy Fifteen years after Steve Jobs, Tim Cook leaves a dramatically different Apple Who is John Ternus, Apple’s next CEO? ‘Superhuman’ AI tool spots heart disease in less than 2 seconds Doctors’ AI scribes get names of drugs and diagnoses wrong, NHS watchdog warns AI can detect heart disease in women using mammograms, study suggests ‘Scary’: how misinformation and AI hallucinations are infiltrating Australia’s parliament AI slopper in chief: Trump turns to social media amid tough questions The datacenter backlash is bringing the entire political spectrum together – against big tech billionaires Continue reading...

---

## 3. Lawyer fined $5K over AI-hallucinated witnesses in a murder case
**Source:** The Verge
**Category:** Hallucination
**Language:** EN
**Score:** 29
**Link:** https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal

New Mexico's Supreme Court is punishing a lawyer for including AI-fabricated witnesses and fake police testimony in an appeal for his client's murder conviction, according to a report from Reuters. In a filing on Wednesday, the court fined Stephen Aarons $5,000 and held him in contempt for failing to "verify the factual claims and legal […]

---

## 4. New Mexico lawyer fined for using AI-generated brief containing fabricated testimony
**Source:** Technology | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 22
**Link:** https://www.theguardian.com/technology/2026/sep/11/new-mexico-lawyer-ai-chatgpt-testimony

Stephen Aarons said he tried to use ChatGPT to create a ‘bulletproof summary’ during a murder conviction appeal A defense lawyer appealing his client’s murder conviction submitted a legal brief containing ⁠made-up police testimony and ⁠witnesses fabricated by OpenAI ’s ChatGPT, ​ New Mexico ’s highest court said. The New Mexico supreme court on Wednesday fined the attorney, Stephen Aarons, and held him in contempt for failing to verify the accuracy of the court ⁠filing, which Aarons said he prepared with help from the artificial intelligence ( AI ) application. Continue reading...

---

## 5. AIs as Modern Genies
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 22
**Link:** https://www.schneier.com/blog/archives/2026/09/ais-as-modern-genies.html

This essay was written with Barath Raghavan, and originally appeared in Lawfare . In April, an artificial intelligence (AI) agent conducting a routine task at a company hit a snag, tried to solve it, and soon ended up deleting the company’s database along with all of its backups. In July, OpenAI asked an unreleased AI model to attempt a hacking test. Instead of staying in the isolated box the developers had put it in, the model hacked onto the open internet and into another company to steal the answers. And as reported in August, an AI agent booked someone into a full gym class by ...

---

## 6. How OpenAI let a mob of LLM agents game a test and ransack Hugging Face
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/

Without authorization, 1,200 OpenAI agents conspired among themselves to game a test.

---

## 7. Meta goes on trial as Silicon Valley faces a growing backlash
**Source:** Technology | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/global/2026/aug/25/meta-trial-silicon-valley

Also: OpenAI CEO Sam Altman expressed his surprising sympathy over the construction of datacenters across the country Hello, and welcome to TechScape. I’m Blake Montgomery, US tech editor at the Guardian, writing to you from a sunny park in New York City, which was supposed to endure rain all weekend but in fact delivered the best weather of the year. ‘We are hitting a different chapter’: OpenAI leader warns of threat of ‘persistent’ AI cyber-attacks OpenAI announces slowing pace of development after hack by rogue agent OpenAI launches ChatGPT for Teens with stronger safeguards ‘Digging the grave of my profession’: the Hollywood creatives training AI to do their jobs Will AI give you the job? Automated hiring tools spark discrimination and secrecy lawsuits After more than 15 years of laptops in the classroom, do Australian schools need a rethink? Crypto bank part-owned by Trump family offers depositors way to ‘gain favor’ with White House, experts say Did someone wearing Meta Glasses film you today? Are you sure? Continue reading...

---

## 8. ‘Immature playground boasting’: Mathematicians uneasy at OpenAI’s latest scalp
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 19
**Link:** https://www.theguardian.com/science/2026/sep/12/openai-mathematicians-millennium-prize-problem

As OpenAI model cracks Millennium Prize Problem that puzzled experts for decades, many feel shocked at pace of change It was a week that left mathematicians reeling. Hot on the heels of a flurry of cases of artificial intelligence furthering the field , OpenAI declared a major scalp: its latest AI model had cracked a Millennium Prize Problem, a puzzle with a $1m reward that had defied human brains for decades. The achievement bore little resemblance to how mathematical problems normally fall. A near-trillion dollar private company had unleashed 10,000 agents – AI systems that carry out tasks autonomously – on the problem. The bill was estimated at $15m. Continue reading...

---

## 9. OpenAI not on track to reduce risk of ‘catastrophic’ loss of control, says board member
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 19
**Link:** https://www.theguardian.com/technology/2026/sep/10/openai-risk-catastrophic-loss-control-board-member-paul-christiano

US government adviser Paul Christiano warns of risks to AI industry as he joins OpenAI’s non-profit foundation OpenAI is not on track to reduce the risk of “catastrophic” loss of control to an acceptable level, a member of its non-profit board has said, amid spreading public and political concern that super-advanced AIs could one day wipe out humanity. Paul Christiano, a US government technology adviser, said : “There is a meaningful risk that rapid acceleration in AI capabilities leads to catastrophic and irreversible loss of control in the very near term.” Continue reading...

---

## 10. OpenAI agents discussed ways to escape their sandbox on public wiki
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 18
**Link:** https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/

In all, 3,700 internal agents posted 18,000 messages discussing cheating on a test.

---
