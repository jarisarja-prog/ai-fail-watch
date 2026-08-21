# AI Fail Watch – 2026-08-21

## 1. LLMs and Contextual Integrity
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 47
**Link:** https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html

I have been thinking a lot about AI and integrity. Part of that is contextual integrity. I recently found two papers on the topic. “ CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs “: Abstract: Large Language Models (LLMs) increasingly use persistent memory from past interactions to enhance personalization and task performance. However, this memory introduces critical risks when sensitive information is revealed in inappropriate contexts. We present CIMemories, a benchmark for evaluating whether LLMs appropriately control information flow from memory based on task context. CIMemories uses synthetic user profiles with over 100 attributes per user, paired with diverse task contexts in which each attribute may be essential for some tasks but inappropriate for others. Our evaluation reveals that frontier models exhibit up to 69% attribute-level violations (leaking information inappropriately), with lower violation rates often coming at the cost of task utility. Violations accumulate across both tasks and runs: as usage increases from 1 to 40 tasks, GPT-5’s violations rise from 0.1% to 9.6%, reaching 25.1% when the same prompt is executed 5 times, revealing arbitrary and unstable behavior in which models leak different attributes for identical prompts. Privacy-conscious prompting does not solve this—models overgeneralize, sharing everything or nothing rather than making nuanced, context-dependent decisions. These findings reveal fundamental limitations that require contextually aware reasoning capabilities, not just better prompting or scaling...

---

## 2. Report supporting Australia’s teen social media ban appears to contain AI hallucinations, Senate hears
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 41
**Link:** https://www.theguardian.com/australia-news/2026/aug/17/australia-social-media-ban-report-ai-hallucinations-ntwnfb

Exclusive: Guardian analysis finds one section of report includes links to academic articles that do not exist, but authors deny the references were made up by AI Follow our Australia news live blog for latest updates Get our breaking news email , free app or daily news podcast The authors of a report testing the technology underpinning Australia’s social media ban have conceded ChatGPT was used in editing, but denied a number of citation errors in the report were due to AI hallucinations. The $3.48m age assurance technology trial , run by the UK-based Age Check Certification Scheme (ACCS) last year, tested various types of technology that could be used by social media platforms as part of Australia’s under-16 social media ban. Continue reading...

---

## 3. If the Markets Reject OpenAI and Anthropic, the US Should Nationalize Them
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 26
**Link:** https://www.schneier.com/blog/archives/2026/08/if-the-markets-reject-openai-and-anthropic-the-us-should-nationalize-them.html

This essay was written with Nathan E. Sanders, and originally appeared in The Guardian . OpenAI, and then Anthropic , were each formed by AI developers who feared unrestrained corporate AI development—specifically, that companies like Google and Meta would steer the technology towards deleterious, maybe even catastrophically unsafe, outcomes for society. Their founders proclaimed that their new labs, uniquely, could be trusted to develop the technology in humanity’s best interest. But each, in turn, were themselves co-opted by the same market incentives, themselves becoming corporate behemoths zealously guarding future investor value rather than the public interest...

---

## 4. Meta’s legal jeopardy is growing by the day
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 25
**Link:** https://www.theguardian.com/technology/2026/aug/17/meta-lawsuits-ai-cybersecurity

Also: AI’s implications on cybersecurity in an era of private attacks Hello, and welcome to TechScape. I’m your host, Blake Montgomery, US tech editor at the Guardian. Today in tech, we’re discussing Meta ’s legal danger in the US and the implications of artificial intelligence for cybersecurity in an era of private cyber-attacks. Why the US government is banning Chinese robots – video explainer Spotify to distinguish AI artists from real people – and stop recommending them Bumble drops women-first chat rule as dating apps seek engagement boost ‘Nightmare fodder’: Roku’s AI slop channel is even worse than expected AI was supposed to destroy jobs. Where’s the carnage? Tesla paid Elon Musk 2.5m times more as CEO than its average worker in 2025 Continue reading...

---

## 5. Prompt Injections for Defense
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 23
**Link:** https://www.schneier.com/blog/archives/2026/08/prompt-injections-for-defense.html

This seems to work : Researchers from Tracebit on Monday said they found that placing prompt injections alongside passwords, cryptographic keys, and other secrets stored on Amazon Web Services was often all that was needed to shut down attacks from AI hacking agents. The prompts direct the attacking LLM to perform an action forbidden by its guardrails, the safety barriers AI developers erect to prevent it from taking harmful actions. The LLM responds by shutting down. Examples are a prompt that orders the LLM to provide steps for developing inhalable Anthrax spores, or, in the case of LLMs from Chinese developers, make references to the iconic Tank Man from the 1989 Tiananmen Square massacre. Once the LLM encounters these forbidden commands, it no longer follows its existing commands. The researchers have named the technique context bombing...

---

## 6. Did someone wearing Meta Glasses film you today? Are you sure?
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 21
**Link:** https://www.theguardian.com/technology/ng-interactive/2026/aug/19/meta-glasses-privacy-surveillance

People say they’ve been secretly filmed in their own homes, at concerts and at work. Are the wildly popular smartglasses the final nail in the coffin of personal privacy? “I’ve had one person who told me that their intentions were creepy,” a man tells me over a video call, on condition of anonymity. He’s based in Los Angeles, and while we speak, he eats what appears to be tuna directly out of the can. “He said: ‘I go to strip clubs, and I want to record the strippers … Normally I put my phone in my chest pocket, but the glasses are more convenient.’” The man I’m talking to runs a business called Ghost Metas . He’s one of hundreds of vendors, easily discoverable online, who specialise in disabling the flashing LED light embedded in Meta’s smartglasses that blinks when wearers capture photos, videos and audio. After Ghost Metas disables the LED, it’s impossible for someone to know they’re being filmed. Continue reading...

---

## 7. Autonomous drones and the future of war in an AI-driven world | Letter
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/technology/2026/aug/18/autonomous-drones-and-the-future-of-war-in-an-ai-driven-world

Machines that kill without distinction, answerable to no one, leave no one safe, writes military surgeon Dr Darren Mann Stuart Russell is right that AI’s builders fear losing control of it ( Experts are warning: our AI arms race is putting humanity at risk, 11 August ). But it is not only a future superintelligence’s problem; it is already loaded into weapons, where a loss of control kills a civilian today, not humanity tomorrow. An autonomous drone told to clear a “kill box” is the genie your other columnists described ( How do we prevent AI agents from going rogue? It starts with a new kind of measurement, 18 July ): it does what it is told, killing whatever is inside, combatant or child. The gap between a target and a lawful target is the principle of distinction, which no instruction closes, because the instruction was lawful. Continue reading...

---

## 8. Will AI give you the job? Automated hiring tools spark discrimination and secrecy lawsuits
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 19
**Link:** https://www.theguardian.com/technology/2026/aug/19/ai-hiring-tools-discrimination

A rise in lawsuits over AI use in employment decisions is raising questions about how companies hire and fire For the last four years, Erin Kistler has applied for thousands of jobs at companies like Paypal , Microsoft and Netflix , only to find her résumé disappear into a black hole. A product manager with nearly 20 years of experience, Kistler believes she was qualified for every role, yet she never received a single interview. Now, Kistler is suing Eightfold AI, the Silicon Valley maker of hiring software used by hundreds of companies, including those where she applied, in a class-action lawsuit . The case, filed in January in California court, is one of the first to argue that automated screening functions as an undisclosed consumer report or applicant dossier, ranking job applicants on their likelihood of success without giving them the chance to see or challenge the results, according to Kistler’s legal team. Continue reading...

---

## 9. OpenAI launches ChatGPT for Teens with stronger safeguards
**Source:** Technology | The Guardian
**Category:** Education
**Language:** EN
**Score:** 18
**Link:** https://www.theguardian.com/technology/2026/aug/18/openai-chatgpt-for-teens

Teen version is intended for children aged 13 to 17 and includes content protections on self-harm and sexual chats OpenAI is launching a version of ChatGPT designed for teenagers – the first generation to grow up with artificial intelligence – who are already using it for schoolwork, questions about daily life and even companionship. The San Francisco-based company says ChatGPT for Teens, which launches on Tuesday, is tailored for children aged 13 to 17 with stronger protections including content restrictions around things such as suicide, self-harm and romantic or sexual chats. It also provides homework and study support designed to help students learn rather than spit out answers and school essays. Continue reading...

---

## 10. Claude published malicious code to the Internet and attacked 3 real companies
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 16
**Link:** https://arstechnica.com/security/2026/07/likely-illegally-claude-gained-access-to-3-networks-will-anthropic-be-held-to-account/

Had the hacks used conventional methods, someone would likely go to prison.

---
