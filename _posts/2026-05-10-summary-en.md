---
layout: default
title: "Horizon Summary: 2026-05-10 (EN)"
date: 2026-05-10
lang: en
---

> From 22 items, 8 important content pieces were selected

---

1. [Bun's experimental Rust rewrite hits 99.8% test compatibility](#item-1) ⭐️ 8.0/10
2. [Internet Archive Switzerland Expands as Independent Entity](#item-2) ⭐️ 8.0/10
3. [LLMs Corrupt Documents via 'Semantic Ablation' in Agent Loops](#item-3) ⭐️ 8.0/10
4. [Mathematician's Hands-On Review of ChatGPT 5.5 Pro](#item-4) ⭐️ 8.0/10
5. [EU Report: VPNs Are a Loophole for Age Verification](#item-5) ⭐️ 8.0/10
6. [HTML vs Markdown for LLM Output](#item-6) ⭐️ 8.0/10
7. [Baidu Launches ERNIE 5.1 with 94% Cost Reduction](#item-7) ⭐️ 8.0/10
8. [Chinese gray market sells Claude API at 90% off via proxy networks](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun's experimental Rust rewrite hits 99.8% test compatibility](https://twitter.com/jarredsumner/status/2053047748191232310) ⭐️ 8.0/10

Bun, the JavaScript runtime originally written in Zig, has an experimental Rust rewrite branch that now passes 99.8% of the test suite on Linux x64 glibc, achieved over six days of work. This milestone sparks community debate about Bun's direction and the viability of rewriting performance-critical systems from Zig to Rust, potentially influencing JavaScript runtime development. The rewrite is experimental and not yet committed to production; the developer noted that all this code might be thrown out. The high pass rate was enabled by LLM-assisted code generation using a tool called Mythos.

hackernews · heldrida · May 9, 10:12 · [Discussion](https://news.ycombinator.com/item?id=48073680)

**Background**: Bun is a fast all-in-one JavaScript runtime written in Zig, built as a drop-in replacement for Node.js. Zig is a systems programming language emphasizing performance and safety, while Rust is another systems language known for memory safety without a garbage collector. The project's move to Rust has generated both excitement and skepticism.

<details><summary>References</summary>
<ul>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime ... Bun Guide: Install, Configure & Deploy the Fast JS Runtime ... Top Stories How to Install Bun - commandlinux.com What Is Bun JS? Ultra-Fast JavaScript Runtime Explained (2025 ... Bun 2026: How the Anthropic Acquisition Reshapes the ...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: a Bun developer cautions that the rewrite is experimental and may be discarded, while others praise the speed but worry about reliance on LLM-generated code and the project's shifting direction. Some see the Rust port as a potential fix for Zig-related crashes.

**Tags**: `#javascript-runtime`, `#rust`, `#zig`, `#software-engineering`, `#bun`

---

<a id="item-2"></a>
## [Internet Archive Switzerland Expands as Independent Entity](https://blog.archive.org/2026/05/06/internet-archive-switzerland-expanding-a-global-mission-to-preserve-knowledge/) ⭐️ 8.0/10

Internet Archive Switzerland has been launched as an independent Swiss non-profit foundation based in Sankt Gallen, aiming to preserve endangered archives and collect content from the generative AI wave. This expansion strengthens the global decentralized resilience of digital preservation against legal threats, such as those faced by the US-based Internet Archive, and underscores the growing need for a distributed approach to knowledge access. The new entity operates independently within its national context, joining a network of mission-aligned organizations including Internet Archive Canada and Internet Archive Europe, though early reports note that its website currently contains placeholder text.

hackernews · hggh · May 9, 12:00 · [Discussion](https://news.ycombinator.com/item?id=48074265)

**Background**: The Internet Archive, founded in 1996, is a digital library that provides free access to archived web pages, books, audio, and video. It has faced multiple legal challenges, including copyright lawsuits, that threaten its operations. The creation of independent, distributed entities aims to ensure the survival of digital knowledge by spreading content across jurisdictions and legal systems.

<details><summary>References</summary>
<ul>
<li><a href="https://internetarchive.ch/">Internet Archive Switzerland</a></li>
<li><a href="https://blog.archive.org/2026/05/06/internet-archive-switzerland-expanding-a-global-mission-to-preserve-knowledge/">Internet Archive Switzerland: Expanding a Global Mission to ...</a></li>
<li><a href="https://www.heise.de/en/news/Humanity-s-Memory-Internet-Archive-Takes-Root-in-Switzerland-11288180.html">Humanity's Memory: Internet Archive Takes Root in Switzerland</a></li>

</ul>
</details>

**Discussion**: Community comments express strong support for a decentralized model similar to Usenet to resist DMCA takedowns, while also questioning the actual independence of the new entity due to shared board members (e.g., Brewster Kahle) and potential operational ties. Some users noted placeholder text on the Swiss site, suggesting it is still early in development.

**Tags**: `#Internet Archive`, `#digital preservation`, `#decentralized infrastructure`, `#censorship resistance`, `#copyright`

---

<a id="item-3"></a>
## [LLMs Corrupt Documents via 'Semantic Ablation' in Agent Loops](https://arxiv.org/abs/2604.15597) ⭐️ 8.0/10

A new study reveals that large language models (LLMs) progressively degrade documents when used in successive processing tasks, a phenomenon termed 'semantic ablation'. The paper demonstrates that even with tool use, the semantic content and precision of documents erode over multiple passes. This finding highlights a critical limitation of LLMs in autonomous agent loops, where repeated LLM calls can corrupt data. It challenges the assumption that LLMs can be safely used for iterative document refinement without oversight, impacting applications in automated report generation, data analysis, and content curation. The researchers implemented a basic agentic harness with file reading, writing, and code execution tools, and found that even with tool use, corruption occurred. The paper introduces the term 'semantic ablation' to describe the loss of high-entropy, precise information replaced by generic token sequences.

hackernews · rbanffy · May 9, 08:44 · [Discussion](https://news.ycombinator.com/item?id=48073246)

**Background**: LLMs generate text by predicting the most probable next token, which tends to produce generic outputs. In agent loops, an LLM repeatedly processes its own output, leading to a drift toward statistical averages, eroding original intent. This is analogous to repeated JPEG compression causing image degradation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/">Semantic ablation: Why AI writing is boring and dangerous • The Register</a></li>
<li><a href="https://completeaitraining.com/news/semantic-ablation-how-ai-polishing-guts-meaning-and/">Semantic Ablation: How AI Polishing Guts Meaning and Originality</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree with the findings, with some noting it's an expected behavior (e.g., 'least shocking thing'). SimonW questioned why tool use didn't help, suggesting the agent implementation may not be optimal. Others advocate using LLMs only as a thin translation layer, with minimal round trips, to avoid corruption.

**Tags**: `#LLM`, `#document corruption`, `#agent loops`, `#semantic ablation`, `#AI limitations`

---

<a id="item-4"></a>
## [Mathematician's Hands-On Review of ChatGPT 5.5 Pro](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/) ⭐️ 8.0/10

Timothy Gowers, a prominent mathematician, published a detailed account of using ChatGPT 5.5 Pro for research-level mathematical problems, sharing both successes and failures. This review provides rare insight from a leading researcher into the capabilities and limitations of advanced LLMs in scientific discovery, influencing expectations for AI-assisted research. Gowers noted that ChatGPT 5.5 Pro is the first LLM that can be guided to solve tedious but straightforward problems correctly, though it still makes many mistakes and requires rigid guidance.

hackernews · _alternator_ · May 9, 02:41 · [Discussion](https://news.ycombinator.com/item?id=48071262)

**Background**: Large language models (LLMs) like ChatGPT have been increasingly used for coding and text generation, but their application to advanced mathematical research remains controversial. Gowers' experience highlights both the promise and pitfalls of using AI for original research.

**Discussion**: Commenters like Jweb_Guru echoed Gowers' experience, noting the model's ability to trace reasoning and self-correct. Others debated the philosophical impact on research, with Baez questioning the value of ideas when automation reduces scarcity. A physics professor shared that Gemini helped find a missing imaginary unit but made conceptual errors.

**Tags**: `#AI`, `#LLM`, `#ChatGPT`, `#research methodology`, `#education`

---

<a id="item-5"></a>
## [EU Report: VPNs Are a Loophole for Age Verification](https://cyberinsider.com/eu-calls-vpns-a-loophole-that-needs-closing-in-age-verification-push/) ⭐️ 8.0/10

The European Parliamentary Research Service (EPRS) published a report describing VPNs as a loophole in age verification legislation, suggesting they enable bypassing age checks for adult content. Some policymakers have proposed requiring age verification for VPNs. This could lead to stricter VPN regulation in the EU, impacting privacy and internet freedom. It reflects a broader global push for online age verification, raising concerns about increased surveillance and potential censorship. The report notes that VPN downloads surged after mandatory age verification was introduced in the UK. The Children's Commissioner for England has suggested limiting VPN access to adults. Additionally, an EU-developed age verification app was found to have security flaws.

hackernews · muse900 · May 9, 05:52 · [Discussion](https://news.ycombinator.com/item?id=48072190)

**Background**: Age verification systems are technical methods used to confirm a user's age online, often required for accessing age-restricted content like pornography or gambling. VPNs (Virtual Private Networks) encrypt internet traffic and mask IP addresses, allowing users to bypass geographic restrictions and age gates. The debate centers on balancing child protection with privacy and anonymity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Age_verification_system">Age verification - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/soaring-age-verification-tech-market-why-online-safety-fueling-cp6fe">The Soaring Age - Verification Tech Market: Why Online Safety is...</a></li>

</ul>
</details>

**Discussion**: Comments express skepticism, drawing parallels to China's internet licensing under the guise of protecting children, and argue that the real motive is commercial, such as preventing VPN use for streaming. Some note that the report merely highlights a debate, not a definitive policy. Others criticize the focus on VPNs instead of tax loopholes.

**Tags**: `#VPN`, `#privacy`, `#EU regulation`, `#internet freedom`, `#age verification`

---

<a id="item-6"></a>
## [HTML vs Markdown for LLM Output](https://twitter.com/trq212/status/2052809885763747935) ⭐️ 8.0/10

A discussion on Hacker News argues that using HTML instead of Markdown for LLM-generated content offers superior rendering and interactivity, exemplified by a demo page and a blog post by Simon Willison. This highlights a practical trade-off for developers and content creators using LLMs: HTML enables richer, interactive documents but sacrifices human editability and token efficiency, potentially influencing how AI-generated content is shared and maintained. HTML is significantly less token-efficient than Markdown, and it is harder for humans to co-edit HTML documents without using an LLM, as noted in community comments. The irony of arguing for HTML on Twitter—a platform with minimal semantics—was also pointed out.

hackernews · pretext · May 9, 04:53 · [Discussion](https://news.ycombinator.com/item?id=48071940)

**Background**: Large language models (LLMs) like Claude and GPT often generate text in Markdown, a lightweight markup language for formatting. HTML (HyperText Markup Language) is the standard language for creating web pages, offering richer presentation and interactivity but with more verbose syntax.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/">Using Claude Code: The Unreasonable Effectiveness of HTML</a></li>
<li><a href="https://news.ycombinator.com/item?id=48071940">Using Claude Code: The unreasonable effectiveness of HTML | Hacker News</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: Comments express mixed sentiment: some value HTML's rendered output for LLM interactions while others worry about losing the ability to manually edit documents and note increased token costs. The irony of promoting HTML via a tweet was also highlighted.

**Tags**: `#AI`, `#LLM`, `#HTML`, `#software engineering`, `#content generation`

---

<a id="item-7"></a>
## [Baidu Launches ERNIE 5.1 with 94% Cost Reduction](https://mp.weixin.qq.com/s/_I9ziafHheXiJpA-QY2F7A) ⭐️ 8.0/10

Baidu has released ERNIE 5.1 (文心大模型5.1), utilizing a 'multi-dimensional elastic pre-training' technique that achieves leading foundation model performance at only about 6% of the pre-training cost of comparable models. The model is now available on Baidu's Qianfan model plaza and ERNIE Bot website for enterprise users and developers. ERNIE 5.1's dramatic cost reduction in pre-training could lower barriers for large model deployment, making advanced AI more accessible. Its strong performance on the LMArena leaderboard demonstrates that Chinese models can compete globally in search and other capabilities. According to Baidu, the model's total parameters are compressed to about one-third of the original, while inheriting knowledge from ERNIE 5.0. ERNIE 5.1 scored 1223 points on the LMArena search leaderboard, ranking first domestically and fourth globally.

telegram · zaihuapd · May 9, 07:45

**Background**: ERNIE 5.1 is the latest iteration of Baidu's large language model series. The 'multi-dimensional elastic pre-training' technique refers to a method that dynamically adjusts model architecture and training strategy to reduce computational cost while maintaining or improving performance. LMArena (formerly Chatbot Arena) is an open evaluation platform created by LMSYS for ranking AI models through human preference and benchmark tests.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stnn.cc/c/2026-05-09/4077413.shtml">stnn.cc/c/2026-05-09/4077413.shtml</a></li>
<li><a href="https://finance.sina.com.cn/tech/digi/2026-05-09/doc-inhxhcxm1651084.shtml">finance.sina.com.cn/tech/digi/2026-05-09/doc-inhxhcxm1651084.shtml</a></li>
<li><a href="https://www.ghxi.com/ai202605092.html">国产模型再突破！ 文心5.1登顶 LMArena ... | 果核剥壳</a></li>

</ul>
</details>

**Tags**: `#AI`, `#大模型`, `#百度`, `#文心`, `#预训练`

---

<a id="item-8"></a>
## [Chinese gray market sells Claude API at 90% off via proxy networks](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data) ⭐️ 8.0/10

A report reveals that Chinese gray market 'transit stations' resell Anthropic's Claude API access at a 90% discount, often by stealing credit cards, using fake accounts, and swapping models. This practice puts user data and proprietary code at risk of theft and model distillation, threatening intellectual property and security for AI developers and enterprises. The services engage in model fraud, claiming to provide Claude Opus but returning results from cheaper models, and they harvest prompts and outputs for resale and distillation.

telegram · zaihuapd · May 10, 01:48

**Background**: API transit stations are third-party proxy services that forward requests to official AI APIs. They can reduce latency and costs but also introduce security risks like data interception and model swapping. Model distillation is a technique where a small model learns from a large model's outputs; the stolen data can be used to train competing models.

<details><summary>References</summary>
<ul>
<li><a href="https://post.smzdm.com/p/agolgm9m/">一分钟搞懂大 模 型 蒸 馏 _服务软件_ 什 么 值得买</a></li>
<li><a href="https://juejin.cn/post/7616765969831411718">API 中转站安全性完全指南：5 个维度评估你的中转服务是否可信（2026...</a></li>
<li><a href="https://xz.aliyun.com/news/91721">黑心中转站的安全风险---上下文膨胀、模型造假与提示词投毒</a></li>

</ul>
</details>

**Tags**: `#Claude API`, `#AI安全`, `#数据窃取`, `#灰色市场`, `#模型掉包`

---