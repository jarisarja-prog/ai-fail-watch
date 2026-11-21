# AI Fail Watch – 2026-11-21

## 1. REA: The Open-Source AI Tool That Can Reverse Engineer Almost Anything (2026 Guide)
**Source:** Crunch Hype
**Category:** Legal
**Language:** EN
**Score:** 63
**Link:** https://techncruncher.blogspot.com/2026/11/rea-open-source-ai-tool-that-can.html

What if you could ask your AI assistant how any app works and get a real answer, backed by evidence, without ever seeing the source code? You use an app, tap a feature, and wonder how it was built. Maybe it is a fast search bar, a clever clipboard trick, or a mechanic in an old game. Until recently, finding out meant months of learning disassemblers and reading assembly code. A new open-source project called REA changes that. It has earned more than 430,000 stars on GitHub, and in this guide I will explain what it does, which problems it solves, and how you can start using it today. In this guide The problem with reverse engineering How REA solves it How REA works What REA can analyze Real examples How to get started REA at a glance Using REA responsibly Frequently asked questions The Problem: Reverse Engineering Is Hard Reverse engineering is the practice of studying finished software to understand how it works. It is powerful, but it has never been beginner-friendly. If you have tried it, or even thought about trying it, you have probably run into these obstacles. 1. A steep learning curve Reading assembly code and pseudocode takes a long time to learn. Many curious developers give up before they get their first useful result. 2. Too many tools and no single workflow An Electron app needs one approach. An Android APK needs another. A .NET assembly, a native binary, and a website each have their own tools, file formats, and tricks. 3. Slow, manual investigation Even experts can spend hours following one function through strings, calls, and references just to understand a single small feature. 4. AI answers you cannot verify If you ask a general chatbot how an app works, it may give a confident answer that is simply invented. Without evidence, you cannot tell what is real. 5. Painful setup Connecting analysis tools to an AI agent usually requires custom scripts and configuration, and it is easy to break. The Solution: REA (Reverse Engineer Anything) REA is a free, MIT-licensed project that connects your AI agent to professional reverse engineering tools through MCP (Model Context Protocol). MCP is a standard way for AI agents to use external tools. In simple terms, REA acts as a bridge between your agent and the software you want to understand. Here is how it answers each problem above. The Problem How REA Solves It Steep learning curve You ask in plain English. Your agent runs the tools and explains the results. Too many tools One MCP server covers native binaries, Electron apps, Android, .NET, websites, and dozens of other formats. Slow and manual The agent traces code, references, and calls for you. Answers you cannot verify Every result includes the evidence and limitations behind it. Painful setup One command registers REA with your agent and backs up your existing configuration. You do not need the app’s source code. You point your agent at the app, ask a question, and REA helps it trace the answer. How REA Works You ask a question. For example, how a feature in a particular app works. The agent calls REA. It uses MCP to inspect the target and trace the relevant code. REA returns findings. These include code, references, and clearly marked unknowns. The agent acts on them. It can explain the behavior, ask follow-up questions, or write and test its own version of the feature. The same workflows are available from the terminal, so you can also script them without an agent. Analysis runs locally on your machine. Your agent receives the tool results, and your AI provider’s own data policy applies to that part. What Can REA Analyze? The range of supported targets is one of REA’s biggest strengths. These are the main groups. Native programs and binaries REA returns pseudocode, assembly, strings, symbols, calls, and references. Deep native analysis uses an engine you already have, such as Hopper, Ghidra, IDA, or Kuna. It also supports GNU objdump and Rizin for offline inspection. JavaScript and Electron apps This is the easiest place to start, because static JavaScript analysis needs no native engine. REA recovers modules, imports, source maps, routes, IPC connections, and native add-on relationships. Android apps and devices REA can inspect APK manifests, classes, decompiled methods, signatures, and resources. Through adb, it can also look at packages, processes, and logs on an emulator or a real phone. Flutter apps and JEB projects are supported too. .NET and managed code For .NET assemblies, REA reads metadata, CIL instructions, and native dependencies without running the program. Websites and network captures REA can inspect page structure, scripts, and network activity using a Chrome-family browser. It can also read saved HAR and Fiddler SAZ files to examine requests, responses, and exposed payloads. Specialist formats The list continues with Go and Rust binaries, GPU code objects, GGUF and safetensors model files, Unity IL2CPP metadata, Godot PCK archives, PE imports and certificates, ELF notes, Linux kernel modules, WebAssembly, EVM bytecode, SQLite databases, firmware images, packet captures, and PyInstaller executables. Most of these use built-in static inspection, so no extra software is required. Real Examples: What Has REA Done? The project publishes several case studies on its website. DX-Ball sound panning. REA followed a sound call into a helper function and turned incomplete pseudocode into C. The reconstruction passed 3,205 test cases against the original x86 code and matched all 63 compiled function bytes. Notion’s clipboard bridge. REA traced how Notion’s Electron app moves clipboard data from the renderer through preload and IPC into the main process, including the rich clipboard format. TH04 bullet patterns. REA recovered the angle calculations of a classic DOS game and compared the rebuilt C++ with the original compiler output. Bonus: build RL environments from a web app REA can record a web app session and turn its API calls into tools an AI agent can use. It then exports a runnable environment for reinforcement learning or for testing how well an agent completes tasks. With a saved HAR file, the command looks like this: rea environment-build ./session.har ./my-env --name my-env --json You then run the result with AgentEnv and Docker, and add your own tasks and reward checks. How to Get Started With REA You need Node.js and npm. The project lists supported Node versions as 22.x (22.23.4 or newer), 24.x (24.22.1 or newer), or 26.12.1 and above. Step 1: Run the setup command npx rea-agents setup Step 2: Choose your agents and approve the changes Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents. It shows you the proposed changes first and keeps backups of your existing configuration. Step 3: Restart your agent The new MCP server is loaded when the agent starts again. Step 4: Ask your first question Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project. Prefer the terminal? You can inspect an extracted Electron app or ASAR file directly: npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json To keep REA installed, run npm install --global rea-agents . REA changes quickly, so use rea update to stay current. Updating is also the first fix to try if you run into a bug. REA at a Glance What makes it special REA combines the reach of dozens of analysis tools with the convenience of an AI agent. It helps you understand software you do not have source code for, and it backs each conclusion with evidence instead of guesses. The range of supported formats, from native binaries to Electron apps to Android devices, is unusually broad for a free tool. Key features Works through MCP with Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents Evidence and limitations attached to every result Local analysis on your own machine A full command-line interface for scripting Support for dozens of file and app types An RL environment builder Guides and case studies on the official website Pricing REA itself: free and open source (MIT license) Commercial engines such as IDA Pro, Hopper, and JEB: you must obtain these legally under their own licenses Ghidra: a free option for native analysis; see the setup guide for details Perfect for Developers, security researchers, students, software preservationists, and anyone who wants to understand how an app works. Using REA Responsibly Use REA only on software you own or are authorized to examine. The project is intended for lawful research, education, interoperability, software preservation, and analysis of software you have permission to study. It does not permit cracked tools, stolen license keys, or bypassing license restrictions. Read the project’s disclaimer before you start. Also be careful where you download it from. The project warns that a similar repository name or a copied README does not make a download official. Use only these sources: GitHub: github.com/morluto/rea Website: rea.tools npm package: rea-agents Frequently Asked Questions Do I need Hopper or Ghidra? Only for deep native binary analysis. JavaScript and .NET inspection work without a native engine, and setup can install Hopper with your approval. Does REA upload my app? No. Analysis runs locally. Your agent sees the results, and its provider has its own data policy. Which AI agents work with REA? Any agent that supports local MCP servers can use it. What should I do if I find a bug? Update first, because a recent release may already include the fix. If the problem continues, open an issue on GitHub with your REA version, the target type, the steps to reproduce, and the error output. Final Thoughts The old problem was simple: understanding software without source code took too much skill, too many tools, and too much time. REA’s answer is just as simple. It gives your AI agent the tools to investigate, and it requires the agent to show its evidence. Whether you want to learn how a favorite feature works, study a classic game, or inspect an Electron app, REA is a strong place to start. Just make sure you use it only on software you are allowed to examine.

---

## 2. AI Doesn’t Have to Go Rogue to Break the World
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://www.schneier.com/blog/archives/2026/11/ai-doesnt-have-to-go-rogue-to-break-the-world.html

This essay is adapted from a keynote speech delivered at the DEF CON 34 conference in Las Vegas on August 7, 2026. The essay originally appeared in CyberScoop . I want to talk about AI hacking. There are three aspects: people hacking AI systems, people using AI to hack other systems, and AIs hacking systems on their own, not even maliciously. The last two matter more than the first. The third is the weirdest and potentially the most destabilizing. I started writing about this in 2021 and in my 2022 book, A Hacker’s Mind . Back then I said it was mostly still science fiction, but not stupid science fiction. We’re seeing it more and more, especially in the past year. The trends I’m describing don’t require a major breakthrough in AI. They’re starting to happen now, and they’ll happen more often as AIs get better at autonomous problem-solving. And it will involve far more than computer code...

---

## 3. ‘Little room for error’: what a debt-laden cloud computing company says about the AI boom
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 16
**Link:** https://www.theguardian.com/business/2026/nov/21/debt-laden-cloud-computing-company-coreweave-ai-boom

‘Poster child of AI bubble’ CoreWeave symbolises increasingly risky business model of datacentre buildout The Egyptians had pyramids. The Roman empire had roads. The early 21st-century tech bros have massive buildings full of expensive glass and metal blocks providing the substratum for a powerful inhuman intelligence. Building all those datacentres is taking a while, locals everywhere are angry about them and it is unclear whether the inhuman intelligence inside them is actually going to make their backers rich. Continue reading...

---

## 4. Anthropic keeps the AI party swinging, but the atmosphere is bubbly | Nils Pratley
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 15
**Link:** https://www.theguardian.com/technology/nils-pratley-on-finance/2026/nov/19/anthropic-keeps-ai-party-swinging-but-atmosphere-bubbly

Can the newly listed AI company really be worth $2tn? Anyone who remembers the late 1990s has good reason to ask Roll up, roll up, who wants to buy shares in a company whose technology “could pose catastrophic or existential risks to humanity”, as the prospectus had it? Virtually everybody, as it turned out. Anthropic flew out of the blocks on its first day as a listed company . From the point of view of the promoters, the result was as good as it gets. The final pricing for the shares at $83 apiece was meaningfully higher than the indicated range of $70 to $78, but still left room for a big initial “pop”. There were positive vibes all round – especially for the battalion of investment banks collecting $550m of underwriting fees . Continue reading...

---

## 5. Ännu ett historiskt matteproblem kan ha lösts – med AI
**Source:** DN.se - Dagens Nyheter
**Category:** General
**Language:** EN
**Score:** 14
**Link:** https://www.dn.se/varlden/annu-ett-historiskt-matteproblem-kan-ha-losts-med-ai/

Det kan ha hänt igen. En anställd på Anthropic hävdar att han med hjälp av AI lyckats lösa ett matteproblem som gäckat forskare i över 150 år. Lösningen sträcker sig över 250 000 sidor, enligt matematikern.

---

## 6. Chainalysis says hackers stole credentials and tokens for all of its customers
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 13
**Link:** https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/

Company said a "multifront cyberattack" included AI agents and an on-path data snatch.

---

## 7. Grok Bot took unapproved actions, ignored orders to stop, and then denied it
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it/

AI agent takes unapproved actions even when laptop lid is closed and told not to.

---

## 8. Anthropic VS code extension on Cursor backdoored for nearly 12 hours
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 12
**Link:** https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/

It's still unknown how attackers got access to Anthropic's verified Cursor account.

---

## 9. Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day of trading
**Source:** Technology | The Guardian
**Category:** Research integrity
**Language:** EN
**Score:** 12
**Link:** https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off

The Nasdaq lost trillions in value, with the AI startup’s IPO failing to buoy it as investors question huge sums being poured into AI buildout Who are Anthropic’s seven co-founders, now worth $180bn? As Anthropic’s stock dropped during its second day of trading, the wider stock market dipped with it. On Friday, the Nasdaq Composite erased all its gains for 2026 and closed down 5% from its value on 1 January. The Dow Jones Industrial Average and S&P 500 closed in correction territory. Anthropic’s record-breaking IPO failed to stem a global sell-off in AI-linked companies, and the tech-heavy Nasdaq erased some $4tn in market value this week, according to the Wall Street Journal. Continue reading...

---

## 10. NextDC vows to keep future datacentres away from homes after community backlash in Melbourne
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 12
**Link:** https://www.theguardian.com/australia-news/2026/nov/20/nextdc-vows-to-keep-future-datacentres-away-from-homes-after-community-backlash-in-melbourne

Public expectations around datacentres have changed in the age of AI, chief executive Craig Scroggie says Get our breaking news email , free app or daily news podcast Community backlash to a datacentre expansion in inner Melbourne that resulted in NextDC’s share price dropping 40% will change the way the company engages with communities – and it says it will no longer pursue new developments near homes. The company held its first annual general meeting since it was forced to delay the controversial expansion of its M3 site in West Footscray after power provider Jemena paused construction of new 22-metre power poles amid community protest . Continue reading...

---
