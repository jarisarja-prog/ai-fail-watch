# AI Fail Watch – 2026-11-26

## 1. REA: The Open-Source AI Tool That Can Reverse Engineer Almost Anything (2026 Guide)
**Source:** Crunch Hype
**Category:** Legal
**Language:** EN
**Score:** 63
**Link:** https://techncruncher.blogspot.com/2026/11/rea-open-source-ai-tool-that-can.html

What if you could ask your AI assistant how any app works and get a real answer, backed by evidence, without ever seeing the source code? You use an app, tap a feature, and wonder how it was built. Maybe it is a fast search bar, a clever clipboard trick, or a mechanic in an old game. Until recently, finding out meant months of learning disassemblers and reading assembly code. A new open-source project called REA changes that. It has earned more than 430,000 stars on GitHub, and in this guide I will explain what it does, which problems it solves, and how you can start using it today. In this guide The problem with reverse engineering How REA solves it How REA works What REA can analyze Real examples How to get started REA at a glance Using REA responsibly Frequently asked questions The Problem: Reverse Engineering Is Hard Reverse engineering is the practice of studying finished software to understand how it works. It is powerful, but it has never been beginner-friendly. If you have tried it, or even thought about trying it, you have probably run into these obstacles. 1. A steep learning curve Reading assembly code and pseudocode takes a long time to learn. Many curious developers give up before they get their first useful result. 2. Too many tools and no single workflow An Electron app needs one approach. An Android APK needs another. A .NET assembly, a native binary, and a website each have their own tools, file formats, and tricks. 3. Slow, manual investigation Even experts can spend hours following one function through strings, calls, and references just to understand a single small feature. 4. AI answers you cannot verify If you ask a general chatbot how an app works, it may give a confident answer that is simply invented. Without evidence, you cannot tell what is real. 5. Painful setup Connecting analysis tools to an AI agent usually requires custom scripts and configuration, and it is easy to break. The Solution: REA (Reverse Engineer Anything) REA is a free, MIT-licensed project that connects your AI agent to professional reverse engineering tools through MCP (Model Context Protocol). MCP is a standard way for AI agents to use external tools. In simple terms, REA acts as a bridge between your agent and the software you want to understand. Here is how it answers each problem above. The Problem How REA Solves It Steep learning curve You ask in plain English. Your agent runs the tools and explains the results. Too many tools One MCP server covers native binaries, Electron apps, Android, .NET, websites, and dozens of other formats. Slow and manual The agent traces code, references, and calls for you. Answers you cannot verify Every result includes the evidence and limitations behind it. Painful setup One command registers REA with your agent and backs up your existing configuration. You do not need the app’s source code. You point your agent at the app, ask a question, and REA helps it trace the answer. How REA Works You ask a question. For example, how a feature in a particular app works. The agent calls REA. It uses MCP to inspect the target and trace the relevant code. REA returns findings. These include code, references, and clearly marked unknowns. The agent acts on them. It can explain the behavior, ask follow-up questions, or write and test its own version of the feature. The same workflows are available from the terminal, so you can also script them without an agent. Analysis runs locally on your machine. Your agent receives the tool results, and your AI provider’s own data policy applies to that part. What Can REA Analyze? The range of supported targets is one of REA’s biggest strengths. These are the main groups. Native programs and binaries REA returns pseudocode, assembly, strings, symbols, calls, and references. Deep native analysis uses an engine you already have, such as Hopper, Ghidra, IDA, or Kuna. It also supports GNU objdump and Rizin for offline inspection. JavaScript and Electron apps This is the easiest place to start, because static JavaScript analysis needs no native engine. REA recovers modules, imports, source maps, routes, IPC connections, and native add-on relationships. Android apps and devices REA can inspect APK manifests, classes, decompiled methods, signatures, and resources. Through adb, it can also look at packages, processes, and logs on an emulator or a real phone. Flutter apps and JEB projects are supported too. .NET and managed code For .NET assemblies, REA reads metadata, CIL instructions, and native dependencies without running the program. Websites and network captures REA can inspect page structure, scripts, and network activity using a Chrome-family browser. It can also read saved HAR and Fiddler SAZ files to examine requests, responses, and exposed payloads. Specialist formats The list continues with Go and Rust binaries, GPU code objects, GGUF and safetensors model files, Unity IL2CPP metadata, Godot PCK archives, PE imports and certificates, ELF notes, Linux kernel modules, WebAssembly, EVM bytecode, SQLite databases, firmware images, packet captures, and PyInstaller executables. Most of these use built-in static inspection, so no extra software is required. Real Examples: What Has REA Done? The project publishes several case studies on its website. DX-Ball sound panning. REA followed a sound call into a helper function and turned incomplete pseudocode into C. The reconstruction passed 3,205 test cases against the original x86 code and matched all 63 compiled function bytes. Notion’s clipboard bridge. REA traced how Notion’s Electron app moves clipboard data from the renderer through preload and IPC into the main process, including the rich clipboard format. TH04 bullet patterns. REA recovered the angle calculations of a classic DOS game and compared the rebuilt C++ with the original compiler output. Bonus: build RL environments from a web app REA can record a web app session and turn its API calls into tools an AI agent can use. It then exports a runnable environment for reinforcement learning or for testing how well an agent completes tasks. With a saved HAR file, the command looks like this: rea environment-build ./session.har ./my-env --name my-env --json You then run the result with AgentEnv and Docker, and add your own tasks and reward checks. How to Get Started With REA You need Node.js and npm. The project lists supported Node versions as 22.x (22.23.4 or newer), 24.x (24.22.1 or newer), or 26.12.1 and above. Step 1: Run the setup command npx rea-agents setup Step 2: Choose your agents and approve the changes Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents. It shows you the proposed changes first and keeps backups of your existing configuration. Step 3: Restart your agent The new MCP server is loaded when the agent starts again. Step 4: Ask your first question Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project. Prefer the terminal? You can inspect an extracted Electron app or ASAR file directly: npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json To keep REA installed, run npm install --global rea-agents . REA changes quickly, so use rea update to stay current. Updating is also the first fix to try if you run into a bug. REA at a Glance What makes it special REA combines the reach of dozens of analysis tools with the convenience of an AI agent. It helps you understand software you do not have source code for, and it backs each conclusion with evidence instead of guesses. The range of supported formats, from native binaries to Electron apps to Android devices, is unusually broad for a free tool. Key features Works through MCP with Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents Evidence and limitations attached to every result Local analysis on your own machine A full command-line interface for scripting Support for dozens of file and app types An RL environment builder Guides and case studies on the official website Pricing REA itself: free and open source (MIT license) Commercial engines such as IDA Pro, Hopper, and JEB: you must obtain these legally under their own licenses Ghidra: a free option for native analysis; see the setup guide for details Perfect for Developers, security researchers, students, software preservationists, and anyone who wants to understand how an app works. Using REA Responsibly Use REA only on software you own or are authorized to examine. The project is intended for lawful research, education, interoperability, software preservation, and analysis of software you have permission to study. It does not permit cracked tools, stolen license keys, or bypassing license restrictions. Read the project’s disclaimer before you start. Also be careful where you download it from. The project warns that a similar repository name or a copied README does not make a download official. Use only these sources: GitHub: github.com/morluto/rea Website: rea.tools npm package: rea-agents Frequently Asked Questions Do I need Hopper or Ghidra? Only for deep native binary analysis. JavaScript and .NET inspection work without a native engine, and setup can install Hopper with your approval. Does REA upload my app? No. Analysis runs locally. Your agent sees the results, and its provider has its own data policy. Which AI agents work with REA? Any agent that supports local MCP servers can use it. What should I do if I find a bug? Update first, because a recent release may already include the fix. If the problem continues, open an issue on GitHub with your REA version, the target type, the steps to reproduce, and the error output. Final Thoughts The old problem was simple: understanding software without source code took too much skill, too many tools, and too much time. REA’s answer is just as simple. It gives your AI agent the tools to investigate, and it requires the agent to show its evidence. Whether you want to learn how a favorite feature works, study a classic game, or inspect an Electron app, REA is a strong place to start. Just make sure you use it only on software you are allowed to examine.

---

## 2. New York bans AI toys, including those using internet to talk to children
**Source:** Technology | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 34
**Link:** https://www.theguardian.com/us-news/2026/nov/25/new-york-bans-ai-toys

The state attorney general says she would ‘not hesitate to enforce’ the five-year ban signed by Governor Kathy Hochul The New York governor, Kathy Hochul , signed legislation on Wednesday that places a five-year ban on the manufacture and sale of toys powered by AI chatbots, including talking stuffed animals, dolls and robots that use the internet to hold conversations with children. The recently re-elected governor, who has also placed a one-year moratorium AI datacenter construction in the state , said that parents shopping for children’s toys “should not have to worry that dangerous chatbots disguised as toys could expose their children to inappropriate conversations, manipulate their feelings or put their privacy at risk”. Continue reading...

---

## 3. Dozens of court cases in England and Wales affected by undisclosed AI use in 2026
**Source:** Technology | The Guardian
**Category:** Hallucination
**Language:** EN
**Score:** 26
**Link:** https://www.theguardian.com/technology/2026/nov/26/dozens-of-court-cases-in-england-and-wales-affected-by-undisclosed-ai-use-in-2026

Exclusive: Investigation finds at least 25 cases affected by AI-generated witness statements, fictitious case law and nonexistent statutes Undisclosed AI use has affected more than two dozen court cases this year, prompting judges to complain about AI-generated witness statements, fictitious case law and nonexistent statutes, an investigation has revealed. Proceedings where judges have been forced to deal with lawyers, police officers and claimants misusing the technology in 2026 include a high court dispute between tax lawyers marred by what the judge called “unacceptable” use of “generative AI hallucinations” and references to nonexistent cases. Continue reading...

---

## 4. Meta launches Muse in UK – the AI agent that can do your Christmas shopping
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 19
**Link:** https://www.theguardian.com/technology/2026/nov/24/meta-launches-muse-uk-ai-agent-do-christmas-shopping

Users can give agents tasks such as booking travel or buying presents, but glitches have been reported Have you downloaded Meta’s AI assistant Muse or do you plan to? Want to avoid the Christmas shopping hordes? Then let your AI agent do the shopping for you. Mark Zuckerberg’s Meta is launching its Muse AI assistant in the UK and is encouraging users to let it loose on your apps – and the high street. Muse has been a hit in the US and is ranked first and second respectively on Google and Apple’s free app stores, having been downloaded millions of times. However, UK regulators have said they are keeping a close eye on the launch over privacy and consumer protection requirements. Continue reading...

---

## 5. Aidan didn’t expect a spoken-word component in his thesis - but universities hope it will help tackle AI
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/australia-news/2026/nov/25/australian-universities-tackle-ai-plagiarism-oral-assessment-honours-masters-phd

Honours students are increasingly being asked to sit oral assessments – but at the University of Sydney it’s become a requirement for all Get our breaking news email , free app or daily news podcast When Aidan Elwig Pollock signed up for an honours program at the University of Sydney, he did not expect his 20,000-word thesis to be accompanied by a spoken component. But, as AI increasingly makes written research an unreliable form of assessment, the university has demanded all students taking the one-year program defend their arguments in conversation with professors. Continue reading...

---

## 6. Humans Have Rights. Machines Do Not.
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 17
**Link:** https://www.schneier.com/blog/archives/2026/11/humans-have-rights-machines-do-not.html

This essay originally appeared in Tech Policy Press . Last year, Character.AI asked a federal court in Florida to dismiss a wrongful-death suit, brought by the mother of a fourteen-year-old boy who had killed himself after months of conversation with its chatbot. The company made two arguments. One, that the chatbot’s words were speech that its users had a First Amendment right to receive. And two, that Character.AI was a service rather than a product—so product-liability law could not touch it. In May 2025, Judge Anne Conway accepted neither...

---

## 7. Tracking Incidents of Hacking Using AI Tools
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 15
**Link:** https://www.schneier.com/blog/archives/2026/11/tracking-incidents-of-hacking-using-ai-tools.html

Daniel Meissler is tracking incidents of AI-enhanced hacking, and the offensive harnesses the hackers are using.

---

## 8. Amazon says hackers' AI agents found and exploited 0-day with little human input
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 14
**Link:** https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/

The Cairn AI framework is proving to be a boon for defenders and attackers.

---

## 9. Chainalysis says hackers stole credentials and tokens for all of its customers
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 13
**Link:** https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/

Company said a "multifront cyberattack" included AI agents and an on-path data snatch.

---

## 10. Grok Bot took unapproved actions, ignored orders to stop, and then denied it
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it/

AI agent takes unapproved actions even when laptop lid is closed and told not to.

---
