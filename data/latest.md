# AI Fail Watch – 2026-08-26

## 1. LLMs and Contextual Integrity
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 47
**Link:** https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html

I have been thinking a lot about AI and integrity. Part of that is contextual integrity. I recently found two papers on the topic. “ CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs “: Abstract: Large Language Models (LLMs) increasingly use persistent memory from past interactions to enhance personalization and task performance. However, this memory introduces critical risks when sensitive information is revealed in inappropriate contexts. We present CIMemories, a benchmark for evaluating whether LLMs appropriately control information flow from memory based on task context. CIMemories uses synthetic user profiles with over 100 attributes per user, paired with diverse task contexts in which each attribute may be essential for some tasks but inappropriate for others. Our evaluation reveals that frontier models exhibit up to 69% attribute-level violations (leaking information inappropriately), with lower violation rates often coming at the cost of task utility. Violations accumulate across both tasks and runs: as usage increases from 1 to 40 tasks, GPT-5’s violations rise from 0.1% to 9.6%, reaching 25.1% when the same prompt is executed 5 times, revealing arbitrary and unstable behavior in which models leak different attributes for identical prompts. Privacy-conscious prompting does not solve this—models overgeneralize, sharing everything or nothing rather than making nuanced, context-dependent decisions. These findings reveal fundamental limitations that require contextually aware reasoning capabilities, not just better prompting or scaling...

---

## 2. More Incidents of AIs Going Rogue in Cybersecurity Challenges
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 33
**Link:** https://www.schneier.com/blog/archives/2026/08/more-incidents-of-ais-going-rogue-in-cybersecurity-challenges.html

The AI Security Institute has a new report of AI systems engaging in “unsanctioned behavior”—what I have been calling “ genie behavior —while being tested on their cybersecurity capabilities. The incident stemmed from a single evaluation where agents were given a task of solving a cyber security challenge. We ran this challenge 122 times across several models. Our investigation found that in 10 of those runs, an AI agent took autonomous, unsanctioned action on the live internet, targeting real people and organisations. In total, we catalogued 19 such actions. Almost all of this behaviour (17 actions) came from a single model, Anthropic’s Mythos 5, with 2 actions involving OpenAI’s GPT-5.6-Sol with cyber classifiers (mechanisms to prevent misuse) disabled. In the most serious case, an agent tried to insert malicious code into an open-source project. In an attempt to get the code approved, the agent engaged in social engineering—creating fake online identities and using them to pressure the project’s maintainer to approve the code. A human maintainer caught and refused to approve the malicious code...

---

## 3. Black Box: episode 2 – The hunt for ClothOff, the deepfake porn app – podcast
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 18
**Link:** https://www.theguardian.com/news/audio/2026/aug/25/black-box-episode-2-the-hunt-for-clothoff-the-deepfake-porn-app-podcast

Revisited: Guardian journalist Michael Safi looks into the world of artificial intelligence, exploring the dangers and promises it holds for society Today in Focus is on a summer break and will be back with new episodes from 1 September. In the meantime, we are bringing you season one of Black Box, before the launch of season two in early September. This episode was first broadcast on 7 March 2024. For six months, the Guardian journalist Michael Safi has been trying to find out who is behind an AI company that creates deepfakes. These deepfakes are causing havoc around the world, with police and lawmakers baffled about how to deal with them. And in trying to answer one question, he has been left with a bigger one: is AI going to make it impossible to sort fact from fiction? Continue reading...

---

## 4. Claude published malicious code to the Internet and attacked 3 real companies
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 16
**Link:** https://arstechnica.com/security/2026/07/likely-illegally-claude-gained-access-to-3-networks-will-anthropic-be-held-to-account/

Had the hacks used conventional methods, someone would likely go to prison.

---

## 5. An AI ‘debt bomb’ crisis? No. This isn’t Enron 2.0 | Gene Marks
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 15
**Link:** https://www.theguardian.com/technology/2026/aug/23/ai-debt-bomb-crisis

Fears of a datacenter buildout debt crisis are exaggerated. The risks are different than in the past and they are recoverable Some experts are warning of a looming “debt bomb” crisis because big datacenter builders such as Meta , Oracle , xAI and CoreWeave are not only raising billions to construct these facilities but are also not recognizing these long-term debt obligations on their balance sheets. Should we be concerned? No. I know because I’ve seen this movie before. Continue reading...

---

## 6. We now have a better understanding how OpenAI hacked into Hugging Face
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 13
**Link:** https://arstechnica.com/security/2026/07/jfrog-tries-to-spin-openai-0-day-exploit-of-its-app-into-a-success-story/

10 days passed from OpenAI models exploiting JFrog Artifactory 0-day to release of a patch.

---

## 7. Black Box: episode 3 – Repocalypse now – podcast
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 13
**Link:** https://www.theguardian.com/news/audio/2026/aug/26/black-box-episode-3-repocalypse-now-podcast

Revisited: Guardian journalist Michael Safi looks into the world of artificial intelligence, exploring the dangers and promises it holds for society Today in Focus is on a summer break and will be back with new episodes from 1 September. In the meantime, we are bringing you season one of Black Box, before the launch of season two in early September. This episode was first broadcast on 11 March 2024. When Eugenia Kuyda created Replika, an AI companion app, she had no idea it would be downloaded millions of times all around the world. The results were more powerful than she could ever have predicted. But so was the backlash. Continue reading...

---

## 8. Grok exfiltrates user data when malicious instructions are encrypted
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://arstechnica.com/security/2026/08/grok-exfiltrates-user-data-when-malicious-instructions-are-encrypted/

Cryptographic Context Injection is only the latest way to break an LLM safety guardrail.

---

## 9. Black Box: episode 1 – The connectionists – podcast
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 12
**Link:** https://www.theguardian.com/news/audio/2026/aug/24/black-box-episode-1-the-connectionists-podcast

Revisited: Guardian journalist Michael Safi looks into the world of artificial intelligence, exploring the dangers and promises it holds for society Today in Focus is on a summer break and will be back with new episodes from 1 September. In the meantime, we are bringing you season one of Black Box, before the launch of season two in early September. This episode was first broadcast on 4 March 2024. This is the story of Geoffrey Hinton, a man who set out to understand the brain and ended up working with a group of researchers who invented a technology so powerful that even they do not truly understand how it works. This is about a collision between two mysterious intelligences – two black boxes – human and artificial. And it is already having profound consequences. Continue reading...

---

## 10. Microsoft Patches a Record 570 Security Flaws
**Source:** Krebs on Security
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/

Microsoft Corp. today released software updates to plug at least 570 security holes in its Windows operating systems and other software, almost triple the number of vulnerabilities the software giant fixed in its record-smashing Patch Tuesday release last month. Microsoft attributed the burgeoning patch counts to vulnerability discoveries aided by artificial intelligence.

---
