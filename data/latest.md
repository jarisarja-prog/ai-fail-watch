# AI Fail Watch – 2026-11-23

## 1. REA: The Open-Source AI Tool That Can Reverse Engineer Almost Anything (2026 Guide)
**Source:** Crunch Hype
**Category:** Legal
**Language:** EN
**Score:** 63
**Link:** https://techncruncher.blogspot.com/2026/11/rea-open-source-ai-tool-that-can.html

What if you could ask your AI assistant how any app works and get a real answer, backed by evidence, without ever seeing the source code? You use an app, tap a feature, and wonder how it was built. Maybe it is a fast search bar, a clever clipboard trick, or a mechanic in an old game. Until recently, finding out meant months of learning disassemblers and reading assembly code. A new open-source project called REA changes that. It has earned more than 430,000 stars on GitHub, and in this guide I will explain what it does, which problems it solves, and how you can start using it today. In this guide The problem with reverse engineering How REA solves it How REA works What REA can analyze Real examples How to get started REA at a glance Using REA responsibly Frequently asked questions The Problem: Reverse Engineering Is Hard Reverse engineering is the practice of studying finished software to understand how it works. It is powerful, but it has never been beginner-friendly. If you have tried it, or even thought about trying it, you have probably run into these obstacles. 1. A steep learning curve Reading assembly code and pseudocode takes a long time to learn. Many curious developers give up before they get their first useful result. 2. Too many tools and no single workflow An Electron app needs one approach. An Android APK needs another. A .NET assembly, a native binary, and a website each have their own tools, file formats, and tricks. 3. Slow, manual investigation Even experts can spend hours following one function through strings, calls, and references just to understand a single small feature. 4. AI answers you cannot verify If you ask a general chatbot how an app works, it may give a confident answer that is simply invented. Without evidence, you cannot tell what is real. 5. Painful setup Connecting analysis tools to an AI agent usually requires custom scripts and configuration, and it is easy to break. The Solution: REA (Reverse Engineer Anything) REA is a free, MIT-licensed project that connects your AI agent to professional reverse engineering tools through MCP (Model Context Protocol). MCP is a standard way for AI agents to use external tools. In simple terms, REA acts as a bridge between your agent and the software you want to understand. Here is how it answers each problem above. The Problem How REA Solves It Steep learning curve You ask in plain English. Your agent runs the tools and explains the results. Too many tools One MCP server covers native binaries, Electron apps, Android, .NET, websites, and dozens of other formats. Slow and manual The agent traces code, references, and calls for you. Answers you cannot verify Every result includes the evidence and limitations behind it. Painful setup One command registers REA with your agent and backs up your existing configuration. You do not need the app’s source code. You point your agent at the app, ask a question, and REA helps it trace the answer. How REA Works You ask a question. For example, how a feature in a particular app works. The agent calls REA. It uses MCP to inspect the target and trace the relevant code. REA returns findings. These include code, references, and clearly marked unknowns. The agent acts on them. It can explain the behavior, ask follow-up questions, or write and test its own version of the feature. The same workflows are available from the terminal, so you can also script them without an agent. Analysis runs locally on your machine. Your agent receives the tool results, and your AI provider’s own data policy applies to that part. What Can REA Analyze? The range of supported targets is one of REA’s biggest strengths. These are the main groups. Native programs and binaries REA returns pseudocode, assembly, strings, symbols, calls, and references. Deep native analysis uses an engine you already have, such as Hopper, Ghidra, IDA, or Kuna. It also supports GNU objdump and Rizin for offline inspection. JavaScript and Electron apps This is the easiest place to start, because static JavaScript analysis needs no native engine. REA recovers modules, imports, source maps, routes, IPC connections, and native add-on relationships. Android apps and devices REA can inspect APK manifests, classes, decompiled methods, signatures, and resources. Through adb, it can also look at packages, processes, and logs on an emulator or a real phone. Flutter apps and JEB projects are supported too. .NET and managed code For .NET assemblies, REA reads metadata, CIL instructions, and native dependencies without running the program. Websites and network captures REA can inspect page structure, scripts, and network activity using a Chrome-family browser. It can also read saved HAR and Fiddler SAZ files to examine requests, responses, and exposed payloads. Specialist formats The list continues with Go and Rust binaries, GPU code objects, GGUF and safetensors model files, Unity IL2CPP metadata, Godot PCK archives, PE imports and certificates, ELF notes, Linux kernel modules, WebAssembly, EVM bytecode, SQLite databases, firmware images, packet captures, and PyInstaller executables. Most of these use built-in static inspection, so no extra software is required. Real Examples: What Has REA Done? The project publishes several case studies on its website. DX-Ball sound panning. REA followed a sound call into a helper function and turned incomplete pseudocode into C. The reconstruction passed 3,205 test cases against the original x86 code and matched all 63 compiled function bytes. Notion’s clipboard bridge. REA traced how Notion’s Electron app moves clipboard data from the renderer through preload and IPC into the main process, including the rich clipboard format. TH04 bullet patterns. REA recovered the angle calculations of a classic DOS game and compared the rebuilt C++ with the original compiler output. Bonus: build RL environments from a web app REA can record a web app session and turn its API calls into tools an AI agent can use. It then exports a runnable environment for reinforcement learning or for testing how well an agent completes tasks. With a saved HAR file, the command looks like this: rea environment-build ./session.har ./my-env --name my-env --json You then run the result with AgentEnv and Docker, and add your own tasks and reward checks. How to Get Started With REA You need Node.js and npm. The project lists supported Node versions as 22.x (22.23.4 or newer), 24.x (24.22.1 or newer), or 26.12.1 and above. Step 1: Run the setup command npx rea-agents setup Step 2: Choose your agents and approve the changes Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents. It shows you the proposed changes first and keeps backups of your existing configuration. Step 3: Restart your agent The new MCP server is loaded when the agent starts again. Step 4: Ask your first question Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project. Prefer the terminal? You can inspect an extracted Electron app or ASAR file directly: npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json To keep REA installed, run npm install --global rea-agents . REA changes quickly, so use rea update to stay current. Updating is also the first fix to try if you run into a bug. REA at a Glance What makes it special REA combines the reach of dozens of analysis tools with the convenience of an AI agent. It helps you understand software you do not have source code for, and it backs each conclusion with evidence instead of guesses. The range of supported formats, from native binaries to Electron apps to Android devices, is unusually broad for a free tool. Key features Works through MCP with Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other agents Evidence and limitations attached to every result Local analysis on your own machine A full command-line interface for scripting Support for dozens of file and app types An RL environment builder Guides and case studies on the official website Pricing REA itself: free and open source (MIT license) Commercial engines such as IDA Pro, Hopper, and JEB: you must obtain these legally under their own licenses Ghidra: a free option for native analysis; see the setup guide for details Perfect for Developers, security researchers, students, software preservationists, and anyone who wants to understand how an app works. Using REA Responsibly Use REA only on software you own or are authorized to examine. The project is intended for lawful research, education, interoperability, software preservation, and analysis of software you have permission to study. It does not permit cracked tools, stolen license keys, or bypassing license restrictions. Read the project’s disclaimer before you start. Also be careful where you download it from. The project warns that a similar repository name or a copied README does not make a download official. Use only these sources: GitHub: github.com/morluto/rea Website: rea.tools npm package: rea-agents Frequently Asked Questions Do I need Hopper or Ghidra? Only for deep native binary analysis. JavaScript and .NET inspection work without a native engine, and setup can install Hopper with your approval. Does REA upload my app? No. Analysis runs locally. Your agent sees the results, and its provider has its own data policy. Which AI agents work with REA? Any agent that supports local MCP servers can use it. What should I do if I find a bug? Update first, because a recent release may already include the fix. If the problem continues, open an issue on GitHub with your REA version, the target type, the steps to reproduce, and the error output. Final Thoughts The old problem was simple: understanding software without source code took too much skill, too many tools, and too much time. REA’s answer is just as simple. It gives your AI agent the tools to investigate, and it requires the agent to show its evidence. Whether you want to learn how a favorite feature works, study a classic game, or inspect an Electron app, REA is a strong place to start. Just make sure you use it only on software you are allowed to examine.

---

## 2. How freaked out should we be? After mass outages, experts tell us how close we are to ‘doomsday’
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Security
**Language:** EN
**Score:** 22
**Link:** https://www.theguardian.com/technology/2026/nov/23/tech-outages-security-experts

As tech, travel and banking failures sweep the US, analysts and cyber-security directors discuss AI, underfunding and what keeps them up at night Grounded flights. Bank websites crashing. Microsoft Outlook outages grinding business operations to a halt. Zoom, Ikea, and PokerStars websites hacked. In the past weeks, there’s been a distinct sense that the complex systems that undergird our daily life might be on the verge of total collapse. Or, at the very least, they seem pretty wobbly. Even those who aren’t prone to conspiracy theories have been wondering out loud if these recent disruptions are somehow connected. Speculation runs wild about targeted cyber-attacks by Iranian hackers, or AI agents autonomously hacking critical (air traffic, banking) and not-so-critical (the Ikea website) infrastructure. Continue reading...

---

## 3. Two groups verify mathematician’s claim that Claude helped prove mathematics problem
**Source:** Technology | The Guardian
**Category:** General
**Language:** EN
**Score:** 21
**Link:** https://www.theguardian.com/technology/2026/nov/21/anthropic-riemann-hypothesis-solved-claude-ai

Anthropic’s Levent Alpöge says it took six weeks for him using the AI tool to solve 19th-century Riemann hypothesis A mathematician at Anthropic has said that the San Francisco -based artificial intelligence (AI) company’s software has helped crack one of the most important unsolved problems in mathematics – and experts say the claim checks out. Levent Alpöge, a Turkish American mathematician, on Friday posted a note on his personal website saying that Claude, the AI software, had helped prove the Riemann hypothesis. He says that Claude helped develop a solution to the problem during the course of about six weeks. Continue reading...

---

## 4. AI Doesn’t Have to Go Rogue to Break the World
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 21
**Link:** https://www.schneier.com/blog/archives/2026/11/ai-doesnt-have-to-go-rogue-to-break-the-world.html

This essay is adapted from a keynote speech delivered at the DEF CON 34 conference in Las Vegas on August 7, 2026. The essay originally appeared in CyberScoop . I want to talk about AI hacking. There are three aspects: people hacking AI systems, people using AI to hack other systems, and AIs hacking systems on their own, not even maliciously. The last two matter more than the first. The third is the weirdest and potentially the most destabilizing. I started writing about this in 2021 and in my 2022 book, A Hacker’s Mind . Back then I said it was mostly still science fiction, but not stupid science fiction. We’re seeing it more and more, especially in the past year. The trends I’m describing don’t require a major breakthrough in AI. They’re starting to happen now, and they’ll happen more often as AIs get better at autonomous problem-solving. And it will involve far more than computer code...

---

## 5. Jensen Huang’s reported affair was ‘most expensive sex since Helen of Troy’, US senator says
**Source:** Technology | The Guardian
**Category:** Security
**Language:** EN
**Score:** 20
**Link:** https://www.theguardian.com/us-news/2026/nov/22/jensen-huang-nvidia-john-kennedy

John Kennedy looks to Trump leaders as he asks how China evidently bypassed export controls for Nvidia’s top AI chips Invoking Greek mythology, the US senator John Kennedy has characterized former Nvidia chief executive officer Jensen Huang ’s reported affair with a suspected Chinese spy as “the most expensive sex since Helen of Troy”. The Louisiana Republican’s allusion to the legendary figure whose desirability was such that it caused the mythic Trojan war came during an interview on NBC’s Meet the Press on Sunday. Host Kristen Welker asked Kennedy, known for his colloquialisms, if US national security was put at risk by Huang’s affair, given the position his company’s chips have occupied at the forefront of the artificial intelligence boom. Continue reading...

---

## 6. ‘Pervert glasses’ named word of the year by Macquarie dictionary, ahead of ‘nudify’ and ‘AI;DR’
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Privacy
**Language:** EN
**Score:** 19
**Link:** https://www.theguardian.com/science/2026/nov/23/pervert-glasses-meta-word-of-the-year-macquarie-dictionary-nudify-aidr

Australian dictionary’s committee of word experts says winning term is ‘a succinct reflection of the state of the world in 2026’ Get our breaking news email , free app or daily news podcast The backlash to “pervert glasses” has been swift and severe. Smartglasses such as Meta’s Ray-Bans, which have built-in cameras, microphones, and AI assistants have been banned at some Australian swimming pools and playgrounds, and condemned as a possible invasion of privacy. Continue reading...

---

## 7. Child safety groups urge Amazon and eBay to stop selling AI toys until proved safe
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Legal
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/technology/2026/nov/23/child-safety-groups-urge-amazon-ebay-stop-selling-ai-toys-until-proved-safe

Advocates from across the world voice concern over privacy issues and inappropriate communication to children More than 150 child safety groups and experts across six continents have urged Amazon and eBay to stop selling AI toys this Christmas until they are proved to be safe. In a letter sent to Amazon’s president, Andy Jassy, and eBay’s president, Jamie Iannone, the coalition called for the online retailers to stop the sale of AI toys and offer refunds to customers who have already bought one. Continue reading...

---

## 8. South Korean minister quits after AI cheating scandal engulfs university exams
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Education
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/world/2026/nov/22/south-korea-education-minister-resigns-after-ai-cheating-scandal-engulfs-university-exams

Choi Kyo-jin says he ‘failed to prepare adequately’ for entrance exams following last-minute scramble to tighten measures South Korea’s education minister has resigned after an AI-assisted cheating scandal that erupted in the lead-up to key university entrance exams last week. The country has been gripped by fears of AI-assisted exam cheating since last Sunday, when the top scorer in a national tax accountancy exam confessed to using a miniature camera and smartphone to achieve a near-perfect score, just four days before the crucial university entrance exam, known as the suneung . Continue reading...

---

## 9. ‘Serious error of judgment’: outrage over military AI event at Berlin arts complex
**Source:** AI (artificial intelligence) | The Guardian
**Category:** Security
**Language:** EN
**Score:** 17
**Link:** https://www.theguardian.com/world/2026/nov/22/military-ai-event-berlin-kraftwerk-arts-complex

Kraftwerk Berlin, part of same development as techno club Tresor, transformed into ‘war room’ for arms firm event With their cavernous post-industrial venues, teeth-grinding four-by-four beats and bouncers that look like Blade Runner extras, Berlin’s nightclubs trade on a reputation for bleakness. A recent event at one of the city’s most legendary clubland institutions, however, has proven too dystopian even for seasoned techno-heads. On 11 November, the Kraftwerk Berlin arts complex had its central hall transformed into what visitors described as something resembling a war room, with maps and aerial footage projected on to concrete walls, drones hanging from the ceiling, and guards in flak jackets patrolling the premises with sniffer dogs. Continue reading...

---

## 10. Humans Have Rights. Machines Do Not.
**Source:** Schneier on Security
**Category:** Security
**Language:** EN
**Score:** 17
**Link:** https://www.schneier.com/blog/archives/2026/11/humans-have-rights-machines-do-not.html

This essay originally appeared in Tech Policy Press . Last year, Character.AI asked a federal court in Florida to dismiss a wrongful-death suit, brought by the mother of a fourteen-year-old boy who had killed himself after months of conversation with its chatbot. The company made two arguments. One, that the chatbot’s words were speech that its users had a First Amendment right to receive. And two, that Character.AI was a service rather than a product—so product-liability law could not touch it. In May 2025, Judge Anne Conway accepted neither...

---
