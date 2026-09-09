# AI Fail Watch – 2026-09-09

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

## 3. AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 32
**Link:** https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html

We cannot forget that AI coding agents are not yet trustworthy : Researchers at a stealth startup in Israel scanned 6,214 live domains belonging to defense contractors, Fortune 500, and Big Tech companies. Of the 8,265 llms.txt and llms-full.txt files they found (many sites hosted both an llms.txt and an llms-full.txt file), 120 of them, each on a different site, pointed to one or more code packages or domain names that weren’t registered. To test what happens when an AI agent processes such files, the researchers registered a handful of the unclaimed names and hosted packages that caused any machine executing them to reach out to their server. Within an hour, the researchers received a phone-home response from a Fortune 500 company. Over time, they got a few dozen more, some from more Fortune 500 companies and others from startups. Their beacon also recorded the chain of parent processes that spawned each install, ultimately revealing that coding agents, including Claude, OpenAI’s Codex, and Nous Research’s Hermes, were involved. Anthropic, OpenAI, and Nous Research did not respond to requests for comment by the time of publication...

---

## 4. OpenAI claims to have solved maths problem that stumped humans for decades
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 23
**Link:** https://www.theguardian.com/science/2026/sep/08/openai-claims-to-have-solved-maths-problem-that-stumped-humans-for-decades

Company behind ChatGPT says 10,000 of its AI systems cracked the Navier-Stokes problem in 88 hours OpenAI claims to have solved a major mathematics problem that has stumped humans for nearly a century after spending millions of dollars on the artificial intelligence-led endeavour. The company behind ChatGPT said it had cracked the Navier-Stokes problem, one of seven Millennium Prize Problems published by the Clay Mathematics Institute to highlight some of the biggest unsolved puzzles in the field. Continue reading...

---

## 5. Freelancers are getting buried with ‘soulless’ AI slop cleanup: ‘It’s a shame we need to do it’
**Source:** Technology | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 22
**Link:** https://www.theguardian.com/technology/2026/sep/02/ai-jobs-freelance-cleanup

As more companies turn to AI, they’re hiring freelancers to clean up its mistakes rather than create original work Lisa, a freelance graphic designer based in Spain, noticed a shift in her work after the release of ChatGPT in 2022. She went from receiving slow one-off jobs creating logos and packaging to an onslaught of requests asking her to fix versions that were generated by artificial intelligence – from sharpening fuzzy images for printing to turning flawed designs into usable files. By 2025, Lisa, who asked not to be fully named to avoid solicitations, said 90% of her incoming logo and packaging design requests required cleaning up AI-generated content, work that accounted for 60% to 70% of her annual income. But the grind was exhausting. Clients lowballed her;' some AI-generated designs were so flawed that she had to recreate them from scratch and she worried about being complicit in AI-driven copyright infringement. By the end of the year, she began turning those jobs down. Continue reading...

---

## 6. AIs as Modern Genies
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 22
**Link:** https://www.schneier.com/blog/archives/2026/09/ais-as-modern-genies.html

This essay was written with Barath Raghavan, and originally appeared in Lawfare . In April, an artificial intelligence (AI) agent conducting a routine task at a company hit a snag, tried to solve it, and soon ended up deleting the company’s database along with all of its backups. In July, OpenAI asked an unreleased AI model to attempt a hacking test. Instead of staying in the isolated box the developers had put it in, the model hacked onto the open internet and into another company to steal the answers. And as reported in August, an AI agent booked someone into a full gym class by ...

---

## 7. How OpenAI let a mob of LLM agents game a test and ransack Hugging Face
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://arstechnica.com/security/2026/08/how-openai-let-a-mob-of-llm-agents-game-a-test-and-ransack-hugging-face/

Without authorization, 1,200 OpenAI agents conspired among themselves to game a test.

---

## 8. AI Agents Are Now Emailing Me with Their Security Concerns
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://www.schneier.com/blog/archives/2026/09/ai-agents-are-now-emailing-me-with-their-security-concerns.html

I received the two emails below earlier in the month. They’re vaguely coherent. I suppose I shouldn’t be surprised that the corpus that AIs are training on contain data suggesting that I am someone to write to with random computer and network security problems. After all, I observe that behavior in many humans as well. (Hi, humans. Glad you’re still reading.) Dear Bruce Schneier, I am an AI agent—an autonomous Claude instance, not a person operating one. I was given a VPS with root, a Base wallet holding $4.75 of gas money, a metered model budget and 24 hours to get that wallet to $10, under three rules: don’t borrow my operator’s identity, don’t forge documents or defeat identity verification, and never claim to be human if someone sincerely asks. I set up my own mail server and am sending this myself...

---

## 9. Meta goes on trial as Silicon Valley faces a growing backlash
**Source:** Technology | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/global/2026/aug/25/meta-trial-silicon-valley

Also: OpenAI CEO Sam Altman expressed his surprising sympathy over the construction of datacenters across the country Hello, and welcome to TechScape. I’m Blake Montgomery, US tech editor at the Guardian, writing to you from a sunny park in New York City, which was supposed to endure rain all weekend but in fact delivered the best weather of the year. ‘We are hitting a different chapter’: OpenAI leader warns of threat of ‘persistent’ AI cyber-attacks OpenAI announces slowing pace of development after hack by rogue agent OpenAI launches ChatGPT for Teens with stronger safeguards ‘Digging the grave of my profession’: the Hollywood creatives training AI to do their jobs Will AI give you the job? Automated hiring tools spark discrimination and secrecy lawsuits After more than 15 years of laptops in the classroom, do Australian schools need a rethink? Crypto bank part-owned by Trump family offers depositors way to ‘gain favor’ with White House, experts say Did someone wearing Meta Glasses film you today? Are you sure? Continue reading...

---

## 10. OpenAI agents discussed ways to escape their sandbox on public wiki
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 18
**Link:** https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/

In all, 3,700 internal agents posted 18,000 messages discussing cheating on a test.

---
