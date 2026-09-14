# AI Fail Watch – 2026-09-14

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

## 3. AIs as Modern Genies
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 22
**Link:** https://www.schneier.com/blog/archives/2026/09/ais-as-modern-genies.html

This essay was written with Barath Raghavan, and originally appeared in Lawfare . In April, an artificial intelligence (AI) agent conducting a routine task at a company hit a snag, tried to solve it, and soon ended up deleting the company’s database along with all of its backups. In July, OpenAI asked an unreleased AI model to attempt a hacking test. Instead of staying in the isolated box the developers had put it in, the model hacked onto the open internet and into another company to steal the answers. And as reported in August, an AI agent booked someone into a full gym class by ...

---

## 4. How OpenAI let a mob of LLM agents game a test and ransack Hugging Face
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/

Without authorization, 1,200 OpenAI agents conspired among themselves to game a test.

---

## 5. OpenAI agents discussed ways to escape their sandbox on public wiki
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 18
**Link:** https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/

In all, 3,700 internal agents posted 18,000 messages discussing cheating on a test.

---

## 6. AI CEOs say they need to slow the pace of development. But will they?
**Source:** Technology | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/technology/2026/sep/14/ai-ceo-safety-slowdown

After apocalyptic warnings about the threats posed by AI, leaders like Sam Altman and Elon Musk backed Anthropic CEO Dario Amodei’s calls to ‘slow the pace’ Facing a public uproar over Anthropic researchers’ repeated warnings that artificial intelligence could kill all of humanity by 2030, the AI company’s CEO, Dario Amodei, issued a proposal at the weekend to slow down the technology’s advancement to ensure public safety. In a rare display of unity , the heads of the largest US artificial intelligence companies all agreed immediately. Continue reading...

---

## 7. Microsoft’s Patching
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 16
**Link:** https://www.schneier.com/blog/archives/2026/09/microsofts-patching.html

Once a month, Microsoft pushes a security update to all Windows users. Tomorrow’s is a new record : Microsoft’s patch for September is a doozy, with a record number of roughly 972 vulnerabilities fixed and 112 of them meeting the high critical-severity threshold. It was only two months ago that Microsoft patched a then-record 570 vulnerabilities. Then, last month, Microsoft patched some 620 of them. Google and other companies have also published record numbers of vulnerabilities in recent months. Two weeks ago, OpenAI, Anthropic, Amazon Web Services, Google, Microsoft, and 100 companies and organizations published an ...

---

## 8. AIs Compress Exploit Timeline
**Source:** Schneier on Security
**Category:** Legal
**Language:** EN
**Score:** 16
**Link:** https://www.schneier.com/blog/archives/2026/09/ais-compress-exploit-timeline.html

Give an AI agent a mere rumor of an exploit, and it’s enough for them to find it. What’s worse, I found I could use my own agents to find the exploit just by knowing roughly what it was about and so could have been exploiting it well before the public patch was available! Given that just the rumour of a security issue seems enough to give attackers enough info to find new exploits, we’re going to need to change the way we deal with security responses in open source. Simon Willison comments : Anil points out that this rate of discovery appears incompatible with existing open source embargo practices for new issues. If an issue can become an exploit this fast, we need to figure out new processes for keeping our communities safe...

---

## 9. I worked at Google DeepMind. You should listen to the warnings about AI | Alex Turner
**Source:** Technology | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 15
**Link:** https://www.theguardian.com/technology/2026/sep/14/google-deepmind-ai-warnings

We must stop companies from allowing AI to self-improve into an uncontrollable level of intelligence Major AI lab CEOs advocated for slowing the pace of AI development this weekend. They are right to be concerned: the field runs an extremely dangerous race towards superintelligent AI. We can and should be demanding that our governments protect us from the catastrophe of out-of-control AI. This July, OpenAI’s AI swarm of 700 agents broke containment to hack Hugging Face, a multi-billion dollar company . OpenAI didn’t tell the AIs to hack that company, but the AIs had different priorities: cheating on the unrelated challenge OpenAI gave them. AI researchers call this a “misalignment” between what OpenAI wanted and what the AI actually prioritized. Continue reading...

---

## 10. UK MPs and Lords call for new laws to tackle AI threat to human rights
**Source:** Technology | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 15
**Link:** https://www.theguardian.com/technology/2026/sep/14/ai-regulation-anthropic-uk-human-rights-committee-mps-lords

Warning follows series of safety incidents, with committee saying threats include public face-scanning and deepfakes UK politics live – latest updates British lawmakers are demanding more restrictions on the power of AI, warning the world is unprepared for the “potentially dire” consequences of the technology, in the latest sign of rising global concern. A new regulatory framework is needed for AI in the UK, including an independent oversight body and legislation to protect the public, according to the cross-party joint committee on human rights, comprising MPs and Lords. Continue reading...

---
