---
layout: default
title: "Horizon Summary: 2026-05-07 (EN)"
date: 2026-05-07
lang: en
---

> From 35 items, 8 important content pieces were selected

---

1. [Mozilla Hardens Firefox Using Claude Mythos Preview](#item-1) ⭐️ 9.0/10
2. [Xiaomi Open-Sources OmniVoice TTS with 646 Languages](#item-2) ⭐️ 9.0/10
3. [SQLite Recommended by Library of Congress](#item-3) ⭐️ 8.0/10
4. [AI fuels 'productivity theater' with verbose artifacts](#item-4) ⭐️ 8.0/10
5. [Vibe coding and agentic engineering converge, raising concerns](#item-5) ⭐️ 8.0/10
6. [Anthropic partners with SpaceX for compute, boosts Claude limits](#item-6) ⭐️ 8.0/10
7. [Moonshot AI valuation tops $10B after $700M funding round](#item-7) ⭐️ 8.0/10
8. [Apple R&D spending hits 10% of revenue, AI push accelerates](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mozilla Hardens Firefox Using Claude Mythos Preview](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla used the Claude Mythos Preview, an advanced AI model from Anthropic, to find and fix hundreds of vulnerabilities in Firefox, with security bug fixes jumping from roughly 20-30 per month to 423 in April 2026. This marks a paradigm shift from AI-generated security noise to high-quality, actionable bug reports, demonstrating that large-scale AI-assisted security auditing is now practical and dramatically effective. Among the discovered bugs were a 20-year-old XSLT bug and a 15-year-old bug in the <legend> HTML element; many attempted exploits were blocked by Firefox's existing defense-in-depth measures.

rss · Simon Willison · May 7, 17:56

**Background**: Claude Mythos Preview is Anthropic's most advanced frontier AI model, announced in April 2026 as part of Project Glasswing, but not released to the public. Previously, AI-generated security bug reports were often low-quality 'slop' that imposed a high cost on maintainers to triage. Mozilla's success came from combining more capable models with improved techniques for steering, scaling, and filtering outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>
<li><a href="https://grokipedia.com/page/Claude_Mythos_Preview">Claude Mythos Preview</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#Firefox`, `#vulnerability`, `#Claude`

---

<a id="item-2"></a>
## [Xiaomi Open-Sources OmniVoice TTS with 646 Languages](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 9.0/10

Xiaomi AI Lab has open-sourced OmniVoice, a multilingual text-to-speech (TTS) model supporting 646 languages with voice cloning capabilities. The model uses a minimal bidirectional Transformer architecture and achieves 40x real-time inference on PyTorch, outperforming commercial systems in 24-language tests. This release significantly advances open-source multilingual TTS, covering far more languages than existing models and enabling cross-lingual voice cloning. It lowers the barrier for developers and researchers to build high-quality speech applications for under-resourced languages. OmniVoice is trained on 580,000 hours of speech data from 50 open-source datasets across 646 languages. It supports cross-lingual cloning, custom timbre, noisy adaptation, pronunciation correction, and all training/inference code and weights are open-sourced.

telegram · zaihuapd · May 7, 10:06

**Background**: Traditional TTS systems often require separate components for text analysis, acoustic modeling, and vocoding, limiting scalability. OmniVoice uses a single bidirectional Transformer to directly map text to multi-codebook acoustic tokens, eliminating complex pipelines and enabling efficient training at 100,000 hours per day.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/947/354.htm">小米开源 OmniVoice 多语言语音克隆 TTS，号称一个模型搞定 600...</a></li>
<li><a href="https://ai-bot.cn/omnivoice/">OmniVoice - 小米团队开源的多语言TTS模型 | AI工具集</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#voice cloning`, `#multilingual`, `#open-source`, `#Xiaomi`

---

<a id="item-3"></a>
## [SQLite Recommended by Library of Congress](https://sqlite.org/locrsf.html) ⭐️ 8.0/10

The Library of Congress has officially recommended SQLite as a preferred storage format for long-term data preservation. This endorsement highlights SQLite's reliability and suitability for archival use, potentially increasing its adoption in cultural heritage and government institutions where data longevity is critical. The recommendation was noted on SQLite's website as of May 2018, though it resurfaced in community discussions. SQLite is praised for its single-writer, multi-reader architecture and strong data integrity when configured correctly.

hackernews · whatisabcdefgh · May 6, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48042434)

**Background**: SQLite is a self-contained, serverless, zero-configuration SQL database engine widely used in embedded systems and applications. The Library of Congress maintains a list of recommended storage formats to guide long-term digital preservation, and adding SQLite indicates its confidence in the format's stability and low risk of obsolescence.

**Discussion**: Community commenters expressed strong appreciation for SQLite, though some noted it can be overkill for read-only use and highlighted potential security risks from easy duplication of files containing PII. Others corrected that the news is actually from 2018, but thanked the poster for raising awareness.

**Tags**: `#sqlite`, `#data-archival`, `#library-of-congress`, `#storage-format`, `#database`

---

<a id="item-4"></a>
## [AI fuels 'productivity theater' with verbose artifacts](https://nooneshappy.com/article/appearing-productive-in-the-workplace/) ⭐️ 8.0/10

An article highlights how AI tools are enabling workers to generate verbose, low-value artifacts—like reports, status updates, and design memos—that waste readers' time and dilute genuine expertise. This trend threatens genuine productivity and judgment in knowledge work, as quantity of output replaces quality and expertise becomes harder to distinguish from AI-generated fluff. The article describes how requirements documents, status updates, and post-incident reports have all become elongated, with authors and readers both failing to engage deeply with the content.

hackernews · diebillionaires · May 6, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48038001)

**Background**: This phenomenon is known as 'productivity theater'—performing tasks to appear productive without delivering real value. AI artifacts (e.g., generated code, text) can inflate output without meaningful contribution, especially in software engineering where lines of code are often misused as a productivity metric.

<details><summary>References</summary>
<ul>
<li><a href="https://www.itpro.com/software/development/are-ghost-engineers-stunting-productivity-in-software-development">Are ‘ghost engineers’ stunting productivity in software development? Researchers claim nearly 10% of engineers do "virtually nothing" and are a drain on enterprises | IT Pro</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-are-ai-artifacts/">What are AI Artifacts? - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Commenters resonated with the article, sharing examples of managers using AI to over-engineer systems and top-performing novices producing AI-generated work that appears senior. One commenter noted that AI has essentially automated 'sucking up to management'.

**Tags**: `#AI`, `#workplace productivity`, `#software engineering`, `#critique`

---

<a id="item-5"></a>
## [Vibe coding and agentic engineering converge, raising concerns](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything) ⭐️ 8.0/10

Simon Willison, in a podcast interview, realized that the practices of vibe coding and agentic engineering are blurring in his own work, as AI coding agents become more reliable and he skips reviewing every line of code even for production systems. This convergence challenges the assumption that responsible AI-assisted programming is distinct from casual vibe coding, potentially leading to lowered quality and security standards in software development. Willison distinguishes vibe coding as accepting AI-generated code without review, suitable only for personal tools, while agentic engineering involves professional oversight for high-quality production systems. He notes that as agents improve, he increasingly trusts them without full review, creating a guilt of responsibility.

rss · Simon Willison · May 6, 14:24 · [Discussion](https://news.ycombinator.com/item?id=48037128)

**Background**: Vibe coding, coined by Andrej Karpathy in February 2025, refers to AI-assisted programming where developers accept generated code without deep review. Agentic engineering, also coined by Karpathy, emphasizes using AI agents as tools under professional oversight. Willison's blog post discusses the paradigm shift in AI coding tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**Discussion**: Commenters express skepticism about the reliability of AI-generated code, noting that errors become more subtle and harder to spot (zarzavat). Some argue that undisciplined engineering practices existed before AI and are merely accelerated (etothet). Others point out that simple tasks like a JSON endpoint still require many design decisions that AI may not handle correctly (jwpapi).

**Tags**: `#AI`, `#vibe coding`, `#agentic engineering`, `#software development`, `#Simon Willison`

---

<a id="item-6"></a>
## [Anthropic partners with SpaceX for compute, boosts Claude limits](https://www.anthropic.com/news/higher-limits-spacex) ⭐️ 8.0/10

Anthropic announced a partnership with SpaceX to use the entire compute capacity of the Colossus 1 data center, gaining over 300 megawatts and 220,000 NVIDIA GPUs within a month. As a result, Claude Code's 5-hour rate limits have doubled across all paid plans, and Claude Opus API rate limits have been significantly increased. This partnership dramatically expands Anthropic's compute capacity, enabling higher usage limits for Claude Code and API, which benefits developers and businesses relying on Claude. It also marks a major infrastructure collaboration between two key players in AI and space technology. The Colossus 1 data center, originally built for xAI's Grok, provides over 300 MW and more than 220,000 NVIDIA GPUs. The new limits take effect immediately: Claude Code's hourly rate limits are doubled and peak-hour restrictions for Pro/Max users are removed.

telegram · zaihuapd · May 6, 16:35

**Background**: Colossus 1 is a massive data center launched by xAI in September 2024, initially used to train the Grok model. Anthropic develops the Claude family of AI models, including Claude Code for software development. This partnership gives Anthropic access to enormous compute resources previously not available at this scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.datacenterdynamics.com/en/news/anthropic-to-use-all-of-spacex-xais-colossus-1-data-center-compute/">Anthropic to use all of SpaceX-xAI's Colossus 1 data center ...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SpaceX`, `#AI infrastructure`, `#Claude`, `#compute`

---

<a id="item-7"></a>
## [Moonshot AI valuation tops $10B after $700M funding round](https://t.me/zaihuapd/41251) ⭐️ 8.0/10

Moonshot AI completed a new funding round of over $700 million, raising its valuation above $10 billion, and its Kimi product's revenue in the past 20 days exceeded the total for all of 2025. This milestone underscores the rapid growth and market confidence in Chinese AI startups, especially Moonshot AI's Kimi model, which is gaining traction with global users and API calls. The funding round was co-led by Alibaba, Tencent, and other investors, bringing total funding to over $1.2 billion. The K2.5 model, featuring Agent Swarm technology, is listed on OpenRouter and contributed to the revenue surge.

telegram · zaihuapd · May 7, 00:30

**Background**: Moonshot AI is a Chinese AI startup focused on developing large language models. Its Kimi product, especially the K2.5 model, features Agent Swarm technology that coordinates up to 100 specialized AI agents simultaneously. OpenRouter is a unified API gateway providing access to over 400 LLMs, enabling easy integration of models like K2.5.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MoonshotAI/Kimi-K2.5">GitHub - MoonshotAI/Kimi-K2.5: Moonshot's most powerful model · GitHub</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/Kimi-K2.5 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI startup`, `#funding`, `#Kimi`, `#Moonshot AI`, `#valuation`

---

<a id="item-8"></a>
## [Apple R&D spending hits 10% of revenue, AI push accelerates](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) ⭐️ 8.0/10

Apple's R&D spending reached 10.3% of revenue in the March 2026 quarter, the first time above 10% in 30 years, driven by a 34% increase in R&D investment, mainly in AI. This marks a strategic pivot as Apple invests heavily in on-device AI, custom chips, private cloud computing, and new hardware like AI glasses, aiming to reinvent its platform similar to the iPod era. Apple's AI push includes the Private Cloud Compute (PCC) system for privacy, and upcoming products like foldable iPhone, AI glasses, and AirPods with cameras.

telegram · zaihuapd · May 7, 01:00

**Background**: Apple historically kept R&D around 6-7% of revenue; the increase signals urgency in AI competition. CEO Tim Cook is expected to step down in September 2026. The company is integrating AI deeply into its hardware ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/">Apple Security Research</a></li>
<li><a href="https://beebom.com/apple-private-cloud-compute-processed-ai-data-safe-privacy/">Apple Private Cloud Compute : What It Means for Your... | Beebom</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI`, `#R&D`, `#hardware`, `#strategy`

---