---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 33 items, 10 important content pieces were selected

---

1. [First public Apple M5 kernel memory corruption exploit in 5 days](#item-1) ⭐️ 10.0/10
2. [0-Click Exploit Chain for Pixel 10 Disclosed](#item-2) ⭐️ 9.0/10
3. [arXiv bans unchecked LLM content for 1 year](#item-3) ⭐️ 9.0/10
4. [Mitchell Hashimoto warns of 'AI psychosis' in companies](#item-4) ⭐️ 8.0/10
5. [Zulip Transitions to Independent Nonprofit Foundation](#item-5) ⭐️ 8.0/10
6. [California bill mandates patches or refunds for dead online games](#item-6) ⭐️ 8.0/10
7. [DOJ demands Apple and Google unmask 100k car-tinkering app users](#item-7) ⭐️ 8.0/10
8. [O(x)Caml in Space: Sub-10ns Packet Dispatch via Stack Annotations](#item-8) ⭐️ 8.0/10
9. [ABC News Removes All FiveThirtyEight Articles](#item-9) ⭐️ 8.0/10
10. [Apple-OpenAI Partnership Frays, Legal Action Looms](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First public Apple M5 kernel memory corruption exploit in 5 days](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 10.0/10

Calif, in collaboration with AI system Mythos Preview, built the first public macOS kernel memory corruption exploit targeting Apple M5 hardware, achieving local privilege escalation from an unprivileged user to root shell in five days (April 25 to May 1, 2026). This demonstrates that AI-assisted security research can defeat Apple's hardware-level Memory Integrity Enforcement (MIE) protection, which Apple claimed was the most significant memory safety upgrade in consumer OS history, in just days. The exploit is a data-only kernel local privilege escalation chain targeting macOS 26.4.1 on M5, using only normal system calls and bypassing MIE entirely. A full 55-page technical report will be released after Apple issues a fix.

telegram · zaihuapd · May 15, 02:15

**Background**: Apple's M5 and A19 chips introduced Memory Integrity Enforcement (MIE), a hardware-software co-design to prevent memory corruption exploits, which Apple described as the most significant memory safety upgrade in consumer OS history. Mythos Preview is a limited-access AI model from Anthropic (Claude Mythos Preview) designed for advanced cybersecurity tasks, including vulnerability discovery and exploit development. Calif is a security research team that collaborated with Mythos Preview to achieve this breakthrough.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://cybernews.com/ai-news/mythos-ai-apple-m5-mac-security-expliot/">Mythos AI helps engineers crack Apple security| Cybernews</a></li>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory ...</a></li>

</ul>
</details>

**Tags**: `#安全研究`, `#漏洞利用`, `#Apple M5`, `#AI辅助`, `#内核漏洞`

---

<a id="item-2"></a>
## [0-Click Exploit Chain for Pixel 10 Disclosed](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a full zero-click exploit chain for the Pixel 10, leveraging a remote Dolby audio decoding vulnerability (CVE-2025-54957) to achieve kernel control. This demonstrates the increased attack surface introduced by AI-powered features that pre-process user messages, and highlights the critical need for timely patching across the Android ecosystem. The exploit chain requires no user interaction and was patched within 90 days, which is notably fast for an Android driver bug. The Dolby vulnerability affected all Android devices until patched in January 2026.

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: Google Project Zero is a team of security analysts tasked with finding zero-day vulnerabilities. A zero-click exploit allows an attacker to compromise a device without any user interaction, often by sending a malicious message. The Pixel 10, like many modern phones, includes AI features that automatically decode media (e.g., audio) to enhance search and understanding, which inadvertently increases the attack surface.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0-click exploit chain for the Pixel 10: When a Door Closes ...</a></li>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Project_Zero">Google Project Zero</a></li>

</ul>
</details>

**Discussion**: Community comments express concern over AI features increasing attack surface, and note the relatively fast patching time for this Android bug. Some users compare response times with Apple and wonder if the frequency of disclosed exploits is increasing due to AI hype.

**Tags**: `#security`, `#exploit`, `#zero-click`, `#Android`, `#vulnerability`

---

<a id="item-3"></a>
## [arXiv bans unchecked LLM content for 1 year](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 9.0/10

arXiv announced a new policy: submissions containing unchecked LLM-generated content (e.g., hallucinated references, meta-comments, placeholder data) will result in a 1-year ban, and subsequent submissions must first be accepted by a peer-reviewed venue. This policy establishes a clear deterrent against academic integrity violations involving AI, setting a precedent for preprint platforms and potentially reshaping how researchers use LLMs in paper preparation. The ban applies to content showing lack of author verification, such as hallucinated citations, LLM meta-annotations like 'as an AI language model', and placeholder data. After the ban, authors must have their paper accepted at a trusted peer-reviewed venue before resubmitting to arXiv.

telegram · zaihuapd · May 15, 04:30

**Background**: arXiv is a widely-used preprint repository where researchers share papers before formal peer review. LLMs can generate convincing but false references (hallucinations) and leave unintended meta-comments, undermining scientific credibility. This policy targets those failures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific ... - Nature</a></li>
<li><a href="https://arxiv.org/abs/2605.07723">[2605.07723] LLM hallucinations in the wild: Large-scale ...</a></li>

</ul>
</details>

**Tags**: `#arXiv`, `#LLM`, `#学术出版`, `#科研诚信`, `#AI伦理`

---

<a id="item-4"></a>
## [Mitchell Hashimoto warns of 'AI psychosis' in companies](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto, co-founder of HashiCorp, posted a warning that many companies are in a state of 'AI psychosis,' blindly trusting AI for decision-making and coding without critical oversight. This warning is significant because AI over-reliance could lead to unstable, unmaintainable systems, especially as companies scale; it may also spark needed debate on responsible AI integration in software engineering. Hashimoto's criticism targets companies that outsource thinking to AI, shipping buggy code with the excuse that AI agents will fix it faster, creating a dangerous feedback loop.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: Mitchell Hashimoto is a well-known figure in DevOps and infrastructure, co-creator of tools like Vagrant, Packer, and Terraform. 'AI psychosis' refers to an irrational over-reliance on AI outputs without human verification, akin to groupthink. The concern is that such practices undermine code quality and long-term system health.

**Discussion**: Comments broadly agree with Hashimoto, noting that pure AI-written systems become incomprehensible and unstable at scale. Some argue that using AI for coding is fine as long as humans remain in control, contrasting with stories of reckless migrations. Others predict a rise in 'AI rescue consulting' to fix such systems.

**Tags**: `#AI`, `#software engineering`, `#risk`, `#technology criticism`

---

<a id="item-5"></a>
## [Zulip Transitions to Independent Nonprofit Foundation](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

Zulip announced it is transitioning to an independent nonprofit foundation, with core team members stepping back from full-time leadership to join Anthropic, ensuring the platform's long-term governance for public good. This move addresses growing concerns about vendor lock-in and data privacy in team chat, setting a precedent for open-source sustainability. It is likely to boost trust among users and communities skeptical of commercial chat platforms. The foundation will be independent and nonprofit, while the departure of four senior team members to Anthropic raises questions about continuity. The announcement was made on a Friday afternoon, which some observers interpret as an attempt to minimize attention.

hackernews · boramalper · May 15, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48152168)

**Background**: Zulip is an open-source team chat platform known for its unique topic-based threading that enables both live and asynchronous conversations. It competes with Slack, Microsoft Teams, and Discord. The transition to a foundation follows a pattern seen in other open-source projects, such as the recent Bun/Rust acquisition news, where community governance is prioritized over commercial control.

<details><summary>References</summary>
<ul>
<li><a href="https://zulip.com/">Zulip — organized team chat</a></li>
<li><a href="https://github.com/zulip/zulip">GitHub - zulip/zulip: Zulip server and web application. Open ... Zulip Chat: Open Source Alternative to Slack and Teams (2026 ... Zulip: The Open Source Alternative to Slack & Teams Zulip — organized team chat Self-host Zulip Zulip - GitHub</a></li>
<li><a href="https://www.almtoolbox.com/blog/zulip-chat-overview/">Zulip Chat: Open Source Alternative to Slack and Teams (2026 ...</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some users express excitement about the foundation and praise Zulip's interface, while others are skeptical about the timing and draw parallels to the Bun acquisition. One commenter noted that announcing on a Friday afternoon is typical for unwelcome news, but the Zulip founder clarified the move is not comparable.

**Tags**: `#zulip`, `#open-source`, `#foundation`, `#nonprofit`, `#chat`

---

<a id="item-6"></a>
## [California bill mandates patches or refunds for dead online games](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

California's Assembly Bill (AB) 1234 has passed a key committee vote, requiring game publishers to either release a patch enabling offline play or provide refunds when they shut down online game services. This bill could set a precedent for consumer rights and game preservation, affecting millions of players and forcing publishers to consider long-term support or financial liability for discontinued online games. The bill exempts games offered solely through a subscription model and applies only to games sold in California. Publishers must provide 60 days' notice before shutdown and comply within 90 days.

hackernews · Lihh27 · May 15, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48152994)

**Background**: Many online games become unplayable when servers shut down, leaving consumers with no recourse. This bill, backed by the Stop Killing Games campaign, aims to preserve game functionality and protect consumers. Similar legislation has been proposed in other states and countries.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/">Bill to block publishers from killing online games advances ...</a></li>
<li><a href="https://www.msn.com/en-us/gaming/general/california-bill-pushes-for-refunds-offline-versions-of-video-games/ar-AA22xyH0">California bill pushes for refunds, offline versions of video ...</a></li>
<li><a href="https://www.rockpapershotgun.com/california-bill-pushing-to-keep-games-playable-after-server-shutdowns-passes-key-hurdle-paving-way-for-full-assembly-vote">California bill pushing to keep games playable after server ...</a></li>

</ul>
</details>

**Discussion**: Community comments express varied views: some suggest open-sourcing server code as a fair solution, while others worry about increased risks for indie developers. A developer shutting down a game mentions high operating costs, and another doubts the enforceability of such legislation.

**Tags**: `#gaming`, `#consumer protection`, `#software preservation`, `#legislation`

---

<a id="item-7"></a>
## [DOJ demands Apple and Google unmask 100k car-tinkering app users](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice has subpoenaed Apple and Google to reveal the identities of over 100,000 users who downloaded a car-tinkering app that can disable emissions controls, as part of an emissions crackdown. This action raises significant privacy concerns and sets a potential precedent for government access to app store user data, affecting millions of users of various customization tools beyond just emissions-related apps. The app is reportedly used for ECU tuning to modify vehicle performance, including disabling emissions controls, which violates the Clean Air Act. The DOJ claims it needs the user information to identify witnesses for the investigation.

hackernews · tencentshill · May 15, 17:28 · [Discussion](https://news.ycombinator.com/item?id=48151383)

**Background**: ECU tuning involves modifying a vehicle's electronic control unit software to change performance parameters, often used by enthusiasts. However, when used to disable emissions controls, it becomes illegal under the Clean Air Act, similar to 'defeat devices' that bypass emissions testing. The EPA has prioritized stopping aftermarket defeat devices to reduce air pollution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ECU_tuning">ECU tuning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Defeat_device">Defeat device - Wikipedia</a></li>
<li><a href="https://www.epa.gov/enforcement/national-enforcement-and-compliance-initiative-stopping-aftermarket-defeat-devices">National Enforcement and Compliance Initiative: Stopping Aftermarket Defeat Devices for Vehicles and Engines | US EPA</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of concerns: some question why the government doesn't already have evidence before demanding data, while others criticize app users for disabling emissions controls. There is also worry about this setting a precedent for other forms of vehicle modification, like disabling GPS tracking, and about the centralization of app distribution.

**Tags**: `#privacy`, `#government surveillance`, `#app distribution`, `#digital rights`, `#emissions regulations`

---

<a id="item-8"></a>
## [O(x)Caml in Space: Sub-10ns Packet Dispatch via Stack Annotations](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

A blog post reveals that using OCaml with exclave_ stack annotations reduces p99.9 packet dispatch latency from 29 ns to 9 ns and eliminates GC pressure entirely over 25 million packets. This demonstrates that garbage-collected languages like OCaml can achieve real-time performance critical for space applications, potentially broadening their adoption in embedded and high-performance systems. The improvement comes from adding type annotations to reduce heap allocations, dropping minor GCs from 394 to zero over 25 million packets, with comparable throughput. The work builds on OCaml's recent local/stack allocation features.

hackernews · yminsky · May 15, 10:55 · [Discussion](https://news.ycombinator.com/item?id=48147058)

**Background**: OCaml is a garbage-collected functional language that traditionally relies on heap allocation. Stack annotations allow certain values to be allocated on the call stack instead, reducing GC overhead and improving latency. Space software often demands deterministic performance and low latency, areas where GC languages have historically struggled.

<details><summary>References</summary>
<ul>
<li><a href="https://cs3110.github.io/textbook/ocaml_programming.pdf">OCaml Programming: Correct + Efficient + Beautiful</a></li>

</ul>
</details>

**Discussion**: Commenters pointed out that OCaml was used in space as early as 2016 on GHGSat-D, and praised the GC improvements. There was debate about memory safety versus stack annotations, and comparisons to other GC languages like Java in high-frequency trading contexts.

**Tags**: `#OCaml`, `#space`, `#performance`, `#GC`, `#embedded systems`

---

<a id="item-9"></a>
## [ABC News Removes All FiveThirtyEight Articles](https://twitter.com/baseballot/status/2055309076209492208) ⭐️ 8.0/10

ABC News has taken all FiveThirtyEight articles offline, effectively deleting the entire archive of the data-driven journalism site. This marks the end of a prominent data journalism brand, removing valuable resources on polling, sports, and data visualization that were widely referenced by researchers and the public. The removal includes acclaimed interactive visualizations like the gun deaths visualization and the p-hacking piece. ABC News had previously laid off most of the FiveThirtyEight staff after Disney's cost-cutting rounds.

hackernews · cmsparks · May 15, 19:07 · [Discussion](https://news.ycombinator.com/item?id=48152553)

**Background**: FiveThirtyEight was founded by Nate Silver in 2008, known for its statistical analysis of politics and sports. It was acquired by ESPN (Disney) in 2013 and later folded into ABC News. The site's data-driven approach and unique visualizations made it a staple for election coverage and explanatory journalism.

**Discussion**: Commenters express frustration at ABC's brand mismanagement, noting that FiveThirtyEight was a recognizable brand among professionals and that its removal wastes valuable content. Some also suggest Nate Silver attempted to buy back the IP but was rebuffed, and urge preservation of the GitHub repositories before they are also taken down.

**Tags**: `#journalism`, `#data visualization`, `#media`, `#brand management`, `#technology`

---

<a id="item-10"></a>
## [Apple-OpenAI Partnership Frays, Legal Action Looms](https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight) ⭐️ 8.0/10

The partnership between Apple and OpenAI has deteriorated, with OpenAI considering legal action over unmet subscription goals and strategic differences. This could reshape AI integration in consumer products, as Apple plans to open Siri to other AI models like Claude and Gemini, reducing OpenAI's exclusivity. OpenAI claims that ChatGPT integration in Apple's ecosystem is hidden and feature-limited, leading to far lower subscription conversions than expected; Apple is also unhappy with OpenAI's privacy standards and engineer poaching.

telegram · zaihuapd · May 15, 12:59

**Background**: Apple partnered with OpenAI to integrate ChatGPT into Siri, expecting significant subscription revenue. However, the integration faced adoption issues. Separately, Apple plans to allow Siri to use other AI models like Anthropic's Claude and Google's Gemini in iOS 27.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Apple`, `#AI partnership`, `#legal action`, `#ChatGPT`

---