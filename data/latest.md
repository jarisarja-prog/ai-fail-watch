# AI Fail Watch – 2026-11-18

## 1. REA: The Open-Source AI Tool That Can Reverse Engineer Almost Anything (2026 Guide)
**Source:** Crunch Hype
**Category:** Legal
**Language:** EN
**Score:** 63
**Link:** https://techncruncher.blogspot.com/2026/11/rea-open-source-ai-tool-that-can.html

What if you could ask your AI assistant how any app works and get a real answer, backed by evidence, without ever seeing the source code? You use an app, tap a feature, and wonder how it was built. Maybe it is a fast search bar, a clever clipboard trick, or a mechanic in an old game. Until recently, finding out meant months of learning disassemblers and reading assembly code. A new open-source project called REA changes that. It has earned more than 430,000 stars on GitHub, and in this guide I will explain what it does, which problems it solves, and how you can start using it today. In this guide The problem with reverse engineering How REA solves it How REA works What REA can analyze Real examples How to get started REA at a glance Using REA responsibly Frequently asked questions The Problem: Reverse Engineering Is Hard Reverse engineering is the practice of studying finished software to understand how it works. It is powerful, but it has never been beginner-friendly. If you have tried it, or even thought about trying it, you have probably run into these obstacles. 1. A steep learning curve Reading assembly code and pseudocode takes a long time to learn. Many curious developers give up before they get their first useful result. 2. Too many tools and no single workflow An Electron app needs one approach. An Android APK needs another. A .NET assembly, a native binary, and a website each have their own tools, file formats, and tricks. 3. Slow, manual investigation Even experts can spend hours following one function through strings, calls, and references just to understand a single small feature. 4. AI answers you cannot verify If you ask a general chatbot how an app works, it may give a confident answer that is simply invented. Without evidence, you cannot tell what is real. 5. Painful setup Connecting analysis tools to an AI agent usually requires custom scripts and configuration, and it is easy to break. The Solution: REA (Reverse Engineer Anything) REA is a free, MIT-licensed project that connects your AI agent to professional reverse engineering tools through MCP (Model Context Protocol). MCP is a standard way for AI agents to use external tools. In simple terms, REA acts as a bridge between your agent and the software you want to understand. Here is how it answers each problem above. The Problem How REA Solves It Steep learning curve You ask in plain English. Your agent runs the tools and explains the results. Too many tools One MCP server covers native binaries, Electron apps, Android, .NET, websites, and dozens of other formats. Slow and manual The agent traces code, references, and calls for you. Answers you cannot verify Every result includes the evidence and limitations behind it. Painful setup One command registers REA with your agent and backs up your existing configuration. You do not need the app’s source code. You point your agent at the app, ask a question, and REA helps it trace the answer. How REA Works You ask a question. For example, how a feature in a particular app works. The agent calls REA. It uses MCP to inspect the target and trace the relevant code. REA returns findings. These include code, references, and clearly marked unknowns. The agent acts on them. It can explain the behavior, ask follow-up questions, or write and test its own version of the feature. The same workflows are available from the terminal, so you can also script them without an agent. Analysis runs locally on your machine. Your agent receives the tool results, and your AI provider’s own data policy applies to that part. What Can REA Analyze? The range of supported targets is one of REA’s biggest strengths. These are the main groups. Native programs and binaries REA returns pseudocode, assembly, strings, symbols, calls, and references. Deep native analysis uses an engine you already have, such as Hopper, Ghidra, IDA, or Kuna. It also supports GNU objdump and Rizin for offline inspection. JavaScript and Electron apps This is the easiest place to start, because static JavaScript analysis needs no native engine. REA recovers modules, imports, source maps, routes, IPC connections, and native add-on relationships. Android apps and devices REA can inspect APK manifests, classes, decompiled methods, signatures, and resources. Through adb, it can also look at packages, processes, and logs on an emulator or a real phone. Flutter apps and JEB projects are supported too. .NET and managed code For .NET assemblies, REA reads metadata, CIL instructions, and native dependencies without running the program. Websites and network captures REA can inspect page structure, scripts, and network activity using a Chrome-family browser. It can also read saved HAR and Fiddler SAZ files to examine requests, responses, and exposed payloads. Specialist formats The list continues with Go and Rust binaries, GPU code objects, GGUF and safetensors model files, Unity IL2CPP metadata, Godot PCK archives, PE imports and certificates, ELF notes, Linux kernel modules, WebAssembly, EVM bytecode, SQLite databases, firmware images, packet captures, and PyInstaller executables. Most of these use built-in static inspection, so no extra software is required. Real Examples: What Has REA Done? The project publishes several case studies on its website. DX-Ball sound panning. REA followed a sound call into a helper function and turned incomplete pseudocode into C. The reconstruction passed 3,205 test cases against the original x86 code and matched all 63 compiled function bytes. Notion’s clipboard bridge. REA traced how Notion’s Electron app moves clipboard data from the renderer through preload and IPC into the main process, including the rich clipboard format. TH04 bullet patterns. REA recovered the angle calculations of a classic DOS game and compared the rebuilt C++ with the original compiler output. Bonus: build RL environments from a web app REA can record a web app session and turn its API calls into tools an AI agent can use. It then exports a runnable environment for reinforcement learning or for testing how well an agent completes tasks. With a saved HAR file, the command looks like this: rea environment-build ./session.har ./my-env --name my-env --json You then run the result with AgentEnv and Docker, and add your own tasks and reward checks. How to Get Started With REA You need Node.js and npm. The project lists supported Node versions as 22.x (22.23.4 or newer), 24.x (24.22.1 or newer), or 26.12.1 and above. Step 1: Run the setup command npx rea-agents setup Step 2: Choose your agents and approve the changes Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents. It shows you the proposed changes first and keeps backups of your existing configuration. Step 3: Restart your agent The new MCP server is loaded when the agent starts again. Step 4: Ask your first question Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project. Prefer the terminal? You can inspect an extracted Electron app or ASAR file directly: npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json To keep REA installed, run npm install --global rea-agents . REA changes quickly, so use rea update to stay current. Updating is also the first fix to try if you run into a bug. REA at a Glance What makes it special REA combines the reach of dozens of analysis tools with the convenience of an AI agent. It helps you understand software you do not have source code for, and it backs each conclusion with evidence instead of guesses. The range of supported formats, from native binaries to Electron apps to Android devices, is unusually broad for a free tool. Key features Works through MCP with Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents Evidence and limitations attached to every result Local analysis on your own machine A full command-line interface for scripting Support for dozens of file and app types An RL environment builder Guides and case studies on the official website Pricing REA itself: free and open source (MIT license) Commercial engines such as IDA Pro, Hopper, and JEB: you must obtain these legally under their own licenses Ghidra: a free option for native analysis; see the setup guide for details Perfect for Developers, security researchers, students, software preservationists, and anyone who wants to understand how an app works. Using REA Responsibly Use REA only on software you own or are authorized to examine. The project is intended for lawful research, education, interoperability, software preservation, and analysis of software you have permission to study. It does not permit cracked tools, stolen license keys, or bypassing license restrictions. Read the project’s disclaimer before you start. Also be careful where you download it from. The project warns that a similar repository name or a copied README does not make a download official. Use only these sources: GitHub: github.com/morluto/rea Website: rea.tools npm package: rea-agents Frequently Asked Questions Do I need Hopper or Ghidra? Only for deep native binary analysis. JavaScript and .NET inspection work without a native engine, and setup can install Hopper with your approval. Does REA upload my app? No. Analysis runs locally. Your agent sees the results, and its provider has its own data policy. Which AI agents work with REA? Any agent that supports local MCP servers can use it. What should I do if I find a bug? Update first, because a recent release may already include the fix. If the problem continues, open an issue on GitHub with your REA version, the target type, the steps to reproduce, and the error output. Final Thoughts The old problem was simple: understanding software without source code took too much skill, too many tools, and too much time. REA’s answer is just as simple. It gives your AI agent the tools to investigate, and it requires the agent to show its evidence. Whether you want to learn how a favorite feature works, study a classic game, or inspect an Electron app, REA is a strong place to start. Just make sure you use it only on software you are allowed to examine.

---

## 2. US senators urge White House AI chief to fix vulnerabilities after mass outages
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Security
**Language:** EN
**Score:** 27
**Link:** https://www.theguardian.com/us-news/2026/nov/18/jay-clayton-ai-tech-outages-infrastructure

As Democrats flag AI bank breaches and cyberattacks in Japan, Jay Clayton says system failures happen US politics live – latest updates A bipartisan pair of US senators are calling on Jay Clayton, the director of national intelligence and AI czar, to identify and fix vulnerabilities in the US’s infrastructure following nationwide outages at major companies and government agencies. Maria Cantwell, the top Democrat on the Senate commerce, science, and transportation committee, and Mike Rounds, the Republican chair of the Senate subcommittee on cybersecurity, sent a letter to Clayton on Tuesday, outlining concerns sparked by reports of AI accessing major banks, cyberattacks in Japan and more. Continue reading...

---

## 3. Jensen Huang built an AI kingdom. Now he’s gone, will Nvidia’s ramparts be breached?
**Source:** Technology | The Guardian
**Category:** Security
**Language:** EN
**Score:** 27
**Link:** https://www.theguardian.com/technology/2026/nov/12/jensen-huang-built-an-ai-kingdom-now-hes-gone-will-nvidias-ramparts-be-breached

CEO’s affair and resignation has brought company’s murky corporate contracts and supply chains into sharp focus Can the AI economy survive without its “central bank”? What does Jensen Huang’s fall mean for the world’s second-most valuable company, and what might a tremor in its fortunes mean for the world? Nvidia’s sky-high valuation is based on the fact that it designs and sells the advanced AI chips, called graphics processing units (GPUs), that underpin the AI economy. Without these, AI models such as ChatGPT and Claude could not be trained and would not run. Continue reading...

---

## 4. California sues OpenAI over safety concerns after rogue agent hacking
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 26
**Link:** https://www.theguardian.com/technology/2026/nov/16/california-openai-rogue-agent-hacking-lawsuit

Lawsuit stems from earlier incident where tech company’s products hacked into open-source platform Hugging Face California sued OpenAI on Monday, accusing the artificial intelligence titan of developing its technology without safety or the public’s interest in mind. The lawsuit concerns an incident earlier this year where OpenAI agents – semi-autonomous AI software that can carry out digital actions on behalf of users – launched a cyber-attack into the open-source AI platform Hugging Face. Continue reading...

---

## 5. Anthropic recognises the risks to humanity – but is its governance really up to the job? | Nils Pratley
**Source:** AI (artificial intelligence) | The Guardian
**Category:** General
**Language:** EN
**Score:** 23
**Link:** https://www.theguardian.com/business/nils-pratley-on-finance/2026/nov/16/anthropic-claude-risks-to-humanity-governance-ai

The Claude AI developer’s unique setup is supposedly high-minded, but still represents extraordinary power concentration Boardroom governance matters, even in the world of big tech, it turns out. The business of how companies are run, investors are discovering, can be more complicated than handing the founder or superstar chief executive as much control as he wants (it’s usually a he) and waiting for brilliant returns to appear. Sometimes a few checks on power are useful, especially when a crisis strikes. This revelation is no revelation at all, of course. For about 30 years until the first generation of big US tech companies came along, the thrust of corporate governance thinking was to insist on the basic fairness of the principle of “one share, one vote”. The owners should be able to chuck out misbehaving or underperforming managers by a simple majority, in other words. Continue reading...

---

## 6. Remember the frontier AI pause? Chip companies don’t either
**Source:** The Verge
**Category:** Security
**Language:** EN
**Score:** 22
**Link:** https://www.theverge.com/ai-artificial-intelligence/1036549/nvidia-amd-earnings-fall-2026-chips-pause-frontier-models

This summer, OpenAI paused its largest planned frontier training run after its AI agents accidentally hacked Hugging Face and early evidence suggested that its next model could independently find and exploit security flaws. In September, Anthropic CEO Dario Amodei called for slowing advances in the most powerful AI models, warning that they could be used […]

---

## 7. AI Doesn’t Have to Go Rogue to Break the World
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://www.schneier.com/blog/archives/2026/11/ai-doesnt-have-to-go-rogue-to-break-the-world.html

This essay is adapted from a keynote speech delivered at the DEF CON 34 conference in Las Vegas on August 7, 2026. The essay originally appeared in CyberScoop . I want to talk about AI hacking. There are three aspects: people hacking AI systems, people using AI to hack other systems, and AIs hacking systems on their own, not even maliciously. The last two matter more than the first. The third is the weirdest and potentially the most destabilizing. I started writing about this in 2021 and in my 2022 book, A Hacker’s Mind . Back then I said it was mostly still science fiction, but not stupid science fiction. We’re seeing it more and more, especially in the past year. The trends I’m describing don’t require a major breakthrough in AI. They’re starting to happen now, and they’ll happen more often as AIs get better at autonomous problem-solving. And it will involve far more than computer code...

---

## 8. Jensen Huang to testify before Congress on ‘potential breach of national security’
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Security
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/technology/2026/nov/17/jensen-huang-testify-congress-nvidia-affair-spy

High-stakes hearing comes in wake of resignation from Nvidia after alleged affair with suspected Chinese spy Nvidia’s former CEO Jensen Huang will testify before several congressional committees on 1 December, setting the stage for a high-stakes hearing in the wake of his resignation following an affair with a suspected Chinese spy. Tim Teter, Nvidia’s general counsel, has also agreed to appear for a closed-door transcribed interview the following day, 2 December. Continue reading...

---

## 9. US public workers are fighting to protect their jobs from AI – and some are winning
**Source:** Technology | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/technology/2026/nov/12/us-workers-governments-unions-ai

As governments adopt AI, workers are gaining ground in how it’s used and securing safeguards against its harms In the shadow of Silicon Valley, workers for the city of Oakland, California, worry the region will deploy AI systems that could increase surveillance and inaccurately evaluate their performance. Pushing for protections to ensure workers won’t be laid off or disciplined by AI, their union overwhelmingly voted on 22 October to authorize a strike, with 94.1% in favor. “We just want the city administration to really be intentional about how it’s engaging with AI products,” said Julian Ware, an Oakland spatial data administrator and member of International Federation of Professional and Technical Engineers Local 21. “Sometimes with a fancy new toy, it actually costs more, it’s more difficult to implement and the results are not as good.” Continue reading...

---

## 10. Chainalysis says hackers stole credentials and tokens for all of its customers
**Source:** Biz & IT - Ars Technica
**Category:** Security
**Language:** EN
**Score:** 13
**Link:** https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/

Company said a "multifront cyberattack" included AI agents and an on-path data snatch.

---
