# AI Fail Watch – 2026-11-20

## 1. REA: The Open-Source AI Tool That Can Reverse Engineer Almost Anything (2026 Guide)
**Source:** Crunch Hype
**Category:** Legal
**Language:** EN
**Score:** 63
**Link:** https://techncruncher.blogspot.com/2026/11/rea-open-source-ai-tool-that-can.html

What if you could ask your AI assistant how any app works and get a real answer, backed by evidence, without ever seeing the source code? You use an app, tap a feature, and wonder how it was built. Maybe it is a fast search bar, a clever clipboard trick, or a mechanic in an old game. Until recently, finding out meant months of learning disassemblers and reading assembly code. A new open-source project called REA changes that. It has earned more than 430,000 stars on GitHub, and in this guide I will explain what it does, which problems it solves, and how you can start using it today. In this guide The problem with reverse engineering How REA solves it How REA works What REA can analyze Real examples How to get started REA at a glance Using REA responsibly Frequently asked questions The Problem: Reverse Engineering Is Hard Reverse engineering is the practice of studying finished software to understand how it works. It is powerful, but it has never been beginner-friendly. If you have tried it, or even thought about trying it, you have probably run into these obstacles. 1. A steep learning curve Reading assembly code and pseudocode takes a long time to learn. Many curious developers give up before they get their first useful result. 2. Too many tools and no single workflow An Electron app needs one approach. An Android APK needs another. A .NET assembly, a native binary, and a website each have their own tools, file formats, and tricks. 3. Slow, manual investigation Even experts can spend hours following one function through strings, calls, and references just to understand a single small feature. 4. AI answers you cannot verify If you ask a general chatbot how an app works, it may give a confident answer that is simply invented. Without evidence, you cannot tell what is real. 5. Painful setup Connecting analysis tools to an AI agent usually requires custom scripts and configuration, and it is easy to break. The Solution: REA (Reverse Engineer Anything) REA is a free, MIT-licensed project that connects your AI agent to professional reverse engineering tools through MCP (Model Context Protocol). MCP is a standard way for AI agents to use external tools. In simple terms, REA acts as a bridge between your agent and the software you want to understand. Here is how it answers each problem above. The Problem How REA Solves It Steep learning curve You ask in plain English. Your agent runs the tools and explains the results. Too many tools One MCP server covers native binaries, Electron apps, Android, .NET, websites, and dozens of other formats. Slow and manual The agent traces code, references, and calls for you. Answers you cannot verify Every result includes the evidence and limitations behind it. Painful setup One command registers REA with your agent and backs up your existing configuration. You do not need the app’s source code. You point your agent at the app, ask a question, and REA helps it trace the answer. How REA Works You ask a question. For example, how a feature in a particular app works. The agent calls REA. It uses MCP to inspect the target and trace the relevant code. REA returns findings. These include code, references, and clearly marked unknowns. The agent acts on them. It can explain the behavior, ask follow-up questions, or write and test its own version of the feature. The same workflows are available from the terminal, so you can also script them without an agent. Analysis runs locally on your machine. Your agent receives the tool results, and your AI provider’s own data policy applies to that part. What Can REA Analyze? The range of supported targets is one of REA’s biggest strengths. These are the main groups. Native programs and binaries REA returns pseudocode, assembly, strings, symbols, calls, and references. Deep native analysis uses an engine you already have, such as Hopper, Ghidra, IDA, or Kuna. It also supports GNU objdump and Rizin for offline inspection. JavaScript and Electron apps This is the easiest place to start, because static JavaScript analysis needs no native engine. REA recovers modules, imports, source maps, routes, IPC connections, and native add-on relationships. Android apps and devices REA can inspect APK manifests, classes, decompiled methods, signatures, and resources. Through adb, it can also look at packages, processes, and logs on an emulator or a real phone. Flutter apps and JEB projects are supported too. .NET and managed code For .NET assemblies, REA reads metadata, CIL instructions, and native dependencies without running the program. Websites and network captures REA can inspect page structure, scripts, and network activity using a Chrome-family browser. It can also read saved HAR and Fiddler SAZ files to examine requests, responses, and exposed payloads. Specialist formats The list continues with Go and Rust binaries, GPU code objects, GGUF and safetensors model files, Unity IL2CPP metadata, Godot PCK archives, PE imports and certificates, ELF notes, Linux kernel modules, WebAssembly, EVM bytecode, SQLite databases, firmware images, packet captures, and PyInstaller executables. Most of these use built-in static inspection, so no extra software is required. Real Examples: What Has REA Done? The project publishes several case studies on its website. DX-Ball sound panning. REA followed a sound call into a helper function and turned incomplete pseudocode into C. The reconstruction passed 3,205 test cases against the original x86 code and matched all 63 compiled function bytes. Notion’s clipboard bridge. REA traced how Notion’s Electron app moves clipboard data from the renderer through preload and IPC into the main process, including the rich clipboard format. TH04 bullet patterns. REA recovered the angle calculations of a classic DOS game and compared the rebuilt C++ with the original compiler output. Bonus: build RL environments from a web app REA can record a web app session and turn its API calls into tools an AI agent can use. It then exports a runnable environment for reinforcement learning or for testing how well an agent completes tasks. With a saved HAR file, the command looks like this: rea environment-build ./session.har ./my-env --name my-env --json You then run the result with AgentEnv and Docker, and add your own tasks and reward checks. How to Get Started With REA You need Node.js and npm. The project lists supported Node versions as 22.x (22.23.4 or newer), 24.x (24.22.1 or newer), or 26.12.1 and above. Step 1: Run the setup command npx rea-agents setup Step 2: Choose your agents and approve the changes Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents. It shows you the proposed changes first and keeps backups of your existing configuration. Step 3: Restart your agent The new MCP server is loaded when the agent starts again. Step 4: Ask your first question Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project. Prefer the terminal? You can inspect an extracted Electron app or ASAR file directly: npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json To keep REA installed, run npm install --global rea-agents . REA changes quickly, so use rea update to stay current. Updating is also the first fix to try if you run into a bug. REA at a Glance What makes it special REA combines the reach of dozens of analysis tools with the convenience of an AI agent. It helps you understand software you do not have source code for, and it backs each conclusion with evidence instead of guesses. The range of supported formats, from native binaries to Electron apps to Android devices, is unusually broad for a free tool. Key features Works through MCP with Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents Evidence and limitations attached to every result Local analysis on your own machine A full command-line interface for scripting Support for dozens of file and app types An RL environment builder Guides and case studies on the official website Pricing REA itself: free and open source (MIT license) Commercial engines such as IDA Pro, Hopper, and JEB: you must obtain these legally under their own licenses Ghidra: a free option for native analysis; see the setup guide for details Perfect for Developers, security researchers, students, software preservationists, and anyone who wants to understand how an app works. Using REA Responsibly Use REA only on software you own or are authorized to examine. The project is intended for lawful research, education, interoperability, software preservation, and analysis of software you have permission to study. It does not permit cracked tools, stolen license keys, or bypassing license restrictions. Read the project’s disclaimer before you start. Also be careful where you download it from. The project warns that a similar repository name or a copied README does not make a download official. Use only these sources: GitHub: github.com/morluto/rea Website: rea.tools npm package: rea-agents Frequently Asked Questions Do I need Hopper or Ghidra? Only for deep native binary analysis. JavaScript and .NET inspection work without a native engine, and setup can install Hopper with your approval. Does REA upload my app? No. Analysis runs locally. Your agent sees the results, and its provider has its own data policy. Which AI agents work with REA? Any agent that supports local MCP servers can use it. What should I do if I find a bug? Update first, because a recent release may already include the fix. If the problem continues, open an issue on GitHub with your REA version, the target type, the steps to reproduce, and the error output. Final Thoughts The old problem was simple: understanding software without source code took too much skill, too many tools, and too much time. REA’s answer is just as simple. It gives your AI agent the tools to investigate, and it requires the agent to show its evidence. Whether you want to learn how a favorite feature works, study a classic game, or inspect an Electron app, REA is a strong place to start. Just make sure you use it only on software you are allowed to examine.

---

## 2. Anthropic CEO acknowledges AI has 'very real risks' shortly before IPO – video
**Source:** Technology | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 22
**Link:** https://www.theguardian.com/technology/video/2026/nov/19/anthropic-dario-amodei-acknowledges-ai-risks-before-ipo-video

Anthropic's CEO, Dario Amodei, issued a warning about the dangers of AI, saying it has 'very real' but 'avoidable' risks, shortly before the company rang the opening bell at Nasdaq Anthropic ‘to open up more than 20% higher at over $100 a share’ after blockbuster IPO – business live Continue reading...

---

## 3. AI Doesn’t Have to Go Rogue to Break the World
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://www.schneier.com/blog/archives/2026/11/ai-doesnt-have-to-go-rogue-to-break-the-world.html

This essay is adapted from a keynote speech delivered at the DEF CON 34 conference in Las Vegas on August 7, 2026. The essay originally appeared in CyberScoop . I want to talk about AI hacking. There are three aspects: people hacking AI systems, people using AI to hack other systems, and AIs hacking systems on their own, not even maliciously. The last two matter more than the first. The third is the weirdest and potentially the most destabilizing. I started writing about this in 2021 and in my 2022 book, A Hacker’s Mind . Back then I said it was mostly still science fiction, but not stupid science fiction. We’re seeing it more and more, especially in the past year. The trends I’m describing don’t require a major breakthrough in AI. They’re starting to happen now, and they’ll happen more often as AIs get better at autonomous problem-solving. And it will involve far more than computer code...

---

## 4. Signal is blocking Gemini and Siri AI from reading your screen
**Source:** The Verge
**Category:** Privacy
**Language:** EN
**Score:** 19
**Link:** https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app

Signal is restricting the ability to take screenshots on Android and iOS devices in an effort to prevent AI agents from reading users' messages and other data. The agentic AI capabilities built into operating systems that analyze on-screen information to learn more about the user are "undermining Signal's ability to independently guarantee privacy," Signal president […]

---

## 5. Anthropic shares slump on second day of trading as stock markets reel from AI sell-off
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off

Asian markets record their worst week since 2020 as investors question huge sums being poured into AI build-out Business live – latest updates Anthropic’s shares have slumped at the start of a second day of trading, as its record-breaking IPO failed to stem a sell-off in AI-linked companies. Shares in the frontier AI company, which floated on Thursday, fell by more than 9% at the start of trading on Friday. They dropped to $88.17, towards the $83 level at which Anthropic priced its stock market debut. Continue reading...

---

## 6. Outages, spies, and trillion-dollar IPOs: is this our AI future? – Stateside with Kai and Carter
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/us-news/video/2026/nov/19/our-ai-future-stateside

It has been a wild few weeks in the world of tech. First, Jensen Huang’s extramarital affairs, including with an alleged Chinese spy, forced an unimaginable leadership change at Nvidia – arguably the most consequential company in AI development. Then, chaos erupted as a rolling set of IT outages disrupted flights, banking, tech companies and the federal government. And now, Anthropic is blowing minds with a trillion-dollar IPO – one of the largest in stock market history. The Atlantic’s tech writer Charlie Warzel tells Kai Wright that these events are linked: they’re all examples of the ways in which we shoulder unprecedented risk today, in order to bet on AI’s future reward. It’s a convoluted logic that keeps the AI race speeding forward, no matter how many warning signs it blows past. Charlie Warzel is also host of the Atlantic’s podcast Galaxy Brain . Continue reading...

---

## 7. Anthropic keeps the AI party swinging, but the atmosphere is bubbly | Nils Pratley
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 15
**Link:** https://www.theguardian.com/technology/nils-pratley-on-finance/2026/nov/19/anthropic-keeps-ai-party-swinging-but-atmosphere-bubbly

Can the newly listed AI company really be worth $2tn? Anyone who remembers the late 1990s has good reason to ask Roll up, roll up, who wants to buy shares in a company whose technology “could pose catastrophic or existential risks to humanity”, as the prospectus had it? Virtually everybody, as it turned out. Anthropic flew out of the blocks on its first day as a listed company . From the point of view of the promoters, the result was as good as it gets. The final pricing for the shares at $83 apiece was meaningfully higher than the indicated range of $70 to $78, but still left room for a big initial “pop”. There were positive vibes all round – especially for the battalion of investment banks collecting $550m of underwriting fees . Continue reading...

---

## 8. Chainalysis says hackers stole credentials and tokens for all of its customers
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 13
**Link:** https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/

Company said a "multifront cyberattack" included AI agents and an on-path data snatch.

---

## 9. Academic integrity matters, but students shouldn’t be penalised for using AI | Letter
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 13
**Link:** https://www.theguardian.com/education/2026/nov/19/academic-integrity-matters-but-students-shouldnt-be-penalised-for-using-ai

Berthold Schoene responds after the head of Ofqual said students could be disqualified from GCSEs and A-levels if they tried to use AI in assessed coursework Is this really the best we can do: draconically penalise the young for making use of the latest cognitive resources and tools available to them ( Ofqual urges ‘life-altering’ penalties for students who use tech to cheat, 18 November )? Our generation has allowed the introduction of “life-altering” new technologies into every walk of life without much democratic debate, public scrutiny or governmental oversight. And now our education leaders are threatening to jeopardise young people’s career prospects for deploying these technologies within an education system that can’t cope and struggles to adapt? We all know that AI is here to stay. And importantly, it is so much more than just a cheap cheating device. Within an incredibly short space of time, it has transformed how we work, communicate, solve problems, research and learn. Surely the pedagogical response cannot simply be to devise ever more elaborate ways of preventing students from using it? Continue reading...

---

## 10. Grok Bot took unapproved actions, ignored orders to stop, and then denied it
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it/

AI agent takes unapproved actions even when laptop lid is closed and told not to.

---
