---
layout: default
title: "Horizon Summary: 2026-05-07 (EN)"
date: 2026-05-07
lang: en
---

> From 37 items, 14 important content pieces were selected

---

1. [Mozilla Hardens Firefox with Claude Mythos AI](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.11: CUDA 13, Torch 2.11, Spec Decode V2 Default](#item-2) ⭐️ 8.0/10
3. [AlphaEvolve: Gemini-powered coding agent scales impact across fields](#item-3) ⭐️ 8.0/10
4. [Chrome removes on-device AI privacy claim](#item-4) ⭐️ 8.0/10
5. [Library of Congress Recommends SQLite for Digital Preservation](#item-5) ⭐️ 8.0/10
6. [AI Tools Inflate Workplace Productivity Artifacts](#item-6) ⭐️ 8.0/10
7. [Valve Releases Steam Controller CAD Files Under Creative Commons](#item-7) ⭐️ 8.0/10
8. [Vibe coding and agentic engineering converge](#item-8) ⭐️ 8.0/10
9. [Anthropic and SpaceX Partner for Massive GPU Compute Boost](#item-9) ⭐️ 8.0/10
10. [Moonshot AI raises $7B+ at $10B valuation, Kimi revenue surges](#item-10) ⭐️ 8.0/10
11. [Apple's R&D Spending Hits 10.3% of Revenue, Fueling AI Push](#item-11) ⭐️ 8.0/10
12. [Tencent Hy3 preview achieves 10x token calls over Hy2, tops OpenRouter weekly charts](#item-12) ⭐️ 8.0/10
13. [Xiaomi Open-Sources OmniVoice: TTS for 646 Languages](#item-13) ⭐️ 8.0/10
14. [UK FCA Investigates PayPal, Mastercard, Visa Over Digital Wallet Contracts](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mozilla Hardens Firefox with Claude Mythos AI](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla used the Claude Mythos preview AI model to discover and fix hundreds of security vulnerabilities in Firefox, dramatically increasing the monthly bug-fix rate from about 20-30 to 423 in April 2026. This breakthrough demonstrates that advanced LLMs can now significantly enhance software security hardening, shifting from generating low-quality bug reports to producing high-value vulnerability discoveries that pass maintainer scrutiny. The AI harness combined improved model capabilities with better techniques for steering, scaling, and stacking models to generate signal and filter noise. Many attempts were blocked by Firefox's defense-in-depth measures, showing the model's findings were genuine and precise.

rss · Simon Willison · May 7, 17:56

**Background**: Claude Mythos is Anthropic's newest and most powerful language model, released in 2026, with exceptional performance on computer security tasks. Traditional AI-generated bug reports were often dismissed as 'slop' due to high false-positive rates, but Mythos's high accuracy has changed that dynamic.

<details><summary>References</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#Firefox`, `#vulnerability detection`, `#Claude Mythos`

---

<a id="item-2"></a>
## [SGLang v0.5.11: CUDA 13, Torch 2.11, Spec Decode V2 Default](https://github.com/sgl-project/sglang/releases/tag/v0.5.11) ⭐️ 8.0/10

SGLang v0.5.11 upgrades to CUDA 13.0 and PyTorch 2.11, sets speculative decoding V2 with overlap scheduling as the default, and adds a decode radix cache for prefill-decode disaggregation. It also introduces support for many new models including Gemma 4, Qwen3.6, and Kimi-K2.6. These updates significantly improve performance and compatibility for LLM inference, making SGLang more competitive for production deployments. The default speculative decoding V2 reduces CPU overhead, while the decode radix cache addresses a key limitation in disaggregated deployments, boosting throughput and reducing time-to-first-token. Speculative decoding V2 uses an overlap scheduler to hide CPU overhead, and is now the default for EAGLE, MTP, and DFLASH paths. The decode radix cache recovers radix-cache hit rates under prefill-decode disaggregation, enabling TTFT savings for long shared prefixes.

github · Kangyan-Zhou · May 5, 21:28

**Background**: SGLang is an open-source LLM inference framework that optimizes serving performance through techniques like prefix caching (RadixAttention) and speculative decoding. Prefill-decode (PD) disaggregation separates the prefill and decode phases into different processes to better utilize GPU resources, but previously it broke prefix caching; the new decode radix cache fixes this.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill-decode disaggregation | LLM Inference Handbook</a></li>
<li><a href="https://www.lmsys.org/blog/2024-12-04-sglang-v0-4/">SGLang v0.4: Zero-Overhead Batch Scheduler, Cache-Aware Load Balancer, Faster Structured Outputs - LMSYS Blog | LMSYS Org</a></li>

</ul>
</details>

**Tags**: `#sglang`, `#LLM inference`, `#CUDA 13`, `#speculative decoding`, `#release`

---

<a id="item-3"></a>
## [AlphaEvolve: Gemini-powered coding agent scales impact across fields](https://deepmind.google/blog/alphaevolve-impact/) ⭐️ 8.0/10

DeepMind has unveiled AlphaEvolve, a coding agent powered by the Gemini large language model that can design advanced algorithms and solve high-level optimization problems across mathematics, computer science, and other fields. AlphaEvolve demonstrates the potential for AI to improve itself by optimizing the algorithms it runs on, which could accelerate progress in scientific discovery and software development. It also sparks discussion on how foundation models excel at well-defined, high-level optimization tasks. AlphaEvolve combines an evolutionary search approach with Gemini to generate and refine algorithms, and it was benchmarked on a curated set of around 50 mathematical problems spanning geometry, combinatorics, and number theory. The system focuses on high-level, well-defined problem spaces rather than low-level coding.

hackernews · berlianta · May 7, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48050278)

**Background**: Coding agents are AI assistants designed to help developers write, debug, and optimize code by automating routine tasks. AlphaEvolve extends this concept by using an LLM like Gemini to explore solution spaces evolutionarily, effectively evolving new algorithms. DeepMind previously developed AlphaDev for sorting algorithms, and AlphaEvolve represents a broader application to mathematical and scientific problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaEvolve">AlphaEvolve - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/deepmind-unveils-alphaevolve-precision-ai-tool-solving-avinash-dubey-qblbc">DeepMind Unveils AlphaEvolve : A Precision AI Tool for Solving Math...</a></li>
<li><a href="https://github.com/resources/articles/what-are-ai-agents">What are AI agents ? · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed reactions: some highlighted the potential for AI self-improvement and rapid progress, while others grew tired of hearing about the same math problems (like Erdős problems) being solved repeatedly. There was also curiosity about whether Google engineers themselves prefer Gemini over alternatives like Claude Code or Codex.

**Tags**: `#AI`, `#coding agent`, `#DeepMind`, `#Gemini`, `#optimization`

---

<a id="item-4"></a>
## [Chrome removes on-device AI privacy claim](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/) ⭐️ 8.0/10

Google has removed from Chrome's documentation the claim that the on-device AI model Gemini Nano does not send data to Google servers, raising new privacy concerns. This change undermines user trust in Chrome's privacy promises, especially given that Gemini Nano is being actively deployed on users' devices via Chrome updates. It signals a potential shift in Google's data handling practices for on-device AI. The removed claim was part of documentation for Chrome's built-in AI APIs, which use Gemini Nano to perform tasks like translation and summarization locally. Users have previously raised concerns about a 4GB 'weights.bin' file downloaded without explicit permission.

hackernews · newsoftheday · May 7, 15:56 · [Discussion](https://news.ycombinator.com/item?id=48050964)

**Background**: Chrome's on-device AI feature relies on Gemini Nano, a lightweight AI model designed to run locally on users' devices to improve privacy by avoiding cloud processing. Google had previously committed that this on-device model does not send user data to its servers. The removal of that commitment casts doubt on the privacy guarantees of Chrome's AI features.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/google-chrome-weights-bin-ai-model-download-explained-3664043/">The truth behind Chrome 's 4GB 'weights.bin' Gemini Nano file</a></li>
<li><a href="https://developer.chrome.com/docs/ai/get-started">Get started with built-in AI | AI on Chrome | Chrome for Developers</a></li>
<li><a href="https://indianexpress.com/article/technology/tech-news-technology/google-chrome-downloads-4gb-gemini-ai-model-onto-your-devices-without-permission-report-10677956/">Google Chrome downloads 4GB Gemini AI model onto your devices ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed distrust in Google, with some recommending alternative browsers like Brave that prioritize privacy. Others questioned the impact on Chromium-based browsers, noting that Brave's own AI 'Leo' also has privacy implications. The sentiment was largely skeptical, with one user stating 'we can not trust Google.'

**Tags**: `#privacy`, `#google chrome`, `#on-device AI`, `#data collection`, `#trust`

---

<a id="item-5"></a>
## [Library of Congress Recommends SQLite for Digital Preservation](https://sqlite.org/locrsf.html) ⭐️ 8.0/10

The Library of Congress has officially listed SQLite as a preferred storage format for digital preservation as part of its 2026 recommended formats. This endorsement from a major cultural institution validates SQLite's reliability and longevity, encouraging wider adoption in archival and data preservation contexts. The recommendation appears on the Library of Congress's 2026 recommended storage formats page, listing preferred formats for various data types.

hackernews · whatisabcdefgh · May 6, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48042434)

**Background**: SQLite is a self-contained, serverless, zero-configuration SQL database engine widely used in embedded systems and applications. It stores the entire database as a single cross-platform file, making it easy to archive and preserve.

**Discussion**: Commenters expressed appreciation for SQLite's simplicity and reliability, though some noted potential misuse in enterprise environments where database files can be carelessly copied with sensitive data. One commenter pointed out that the Library of Congress recommendation dates back to 2018, making this news less recent than it appears.

**Tags**: `#SQLite`, `#data storage`, `#digital preservation`, `#open source`, `#database`

---

<a id="item-6"></a>
## [AI Tools Inflate Workplace Productivity Artifacts](https://nooneshappy.com/article/appearing-productive-in-the-workplace/) ⭐️ 8.0/10

The article critiques how AI tools lead to inflated, superficial productivity artifacts in the workplace, diluting expert judgment and creating a culture of verbosity. This undermines authenticity in workplace communication and can erode genuine expertise, especially in fields like software engineering where clear, concise communication is valued. The article notes that requirements documents, status updates, and other artifacts are becoming unnecessarily verbose, and even experts produce work that seems out of character due to AI reliance.

hackernews · diebillionaires · May 6, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48038001)

**Discussion**: Commenters strongly resonated with the notion of artifact elongation and the dilution of expertise. One comment shared an experience where an architect used AI to over-engineer systems, while another noted that LLMs have automated the act of sucking up to management.

**Tags**: `#AI`, `#workplace culture`, `#productivity`, `#software engineering`

---

<a id="item-7"></a>
## [Valve Releases Steam Controller CAD Files Under Creative Commons](https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license) ⭐️ 8.0/10

Valve has released the CAD files for the Steam Controller's external shell and the Steam Controller Puck under a Creative Commons license, enabling users to 3D print, modify, and create custom accessories. This open hardware move empowers modding, accessibility adaptations (e.g., for disabled gamers), and third-party accessories, reducing dependency on proprietary parts and fostering community innovation. The released files include STP, STL models, and engineering drawings with critical features and keep-out zones. The controller itself was recently re-released but quickly sold out, with scalpers reselling units at inflated prices.

hackernews · haunter · May 6, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48037555)

**Background**: Steam Controller is a game controller designed by Valve with unique trackpads and customizable inputs. CAD (Computer-Aided Design) files allow precise 3D printing modifications. Creative Commons licenses enable free sharing and adaptation with attribution.

**Discussion**: Comments praised the friendly readme and highlighted benefits for disabled gamers needing custom controllers. Concerns were raised about scalping during the recent sale, and one user criticized the controller's exclusive reliance on Steam as a step towards a walled garden.

**Tags**: `#open hardware`, `#3d printing`, `#steam controller`, `#creative commons`, `#accessibility`

---

<a id="item-8"></a>
## [Vibe coding and agentic engineering converge](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything) ⭐️ 8.0/10

Simon Willison, a prominent software developer, describes in a podcast how his previously clear distinction between vibe coding and agentic engineering has started to blur, as he increasingly relies on AI coding agents without reviewing every line of code even for production systems. This convergence challenges the responsible use of AI in software development, especially for production software serving others, where unchecked AI-generated code could introduce security vulnerabilities and bugs. Willison notes that for simple, repetitive tasks like building a JSON API endpoint with a SQL query, agents such as Claude Code produce correct code reliably, leading him to skip review and feel guilty about it.

rss · Simon Willison · May 6, 14:24 · [Discussion](https://news.ycombinator.com/item?id=48037128)

**Background**: Vibe coding, coined by Andrej Karpathy in February 2025, is an AI-assisted practice where developers accept AI-generated code without thorough review. Agentic engineering, a term popularized by Willison, involves professional software engineers using AI agents to enhance code quality and productivity while maintaining oversight. The blurring of these practices raises questions about the boundaries of responsible AI use in production environments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://medium.com/@telumai/there-was-prompt-engineering-then-vibe-coding-now-agentic-engineering-7da779d1cb63">There Was Prompt Engineering Then Vibe Coding Now Agentic ...</a></li>

</ul>
</details>

**Discussion**: Commenters note that AI abilities follow a jagged frontier, making it effective for some tasks but not others. They argue that vibe coding and LLMs have not created undisciplined practices but merely exposed and accelerated existing loose standards. Others caution that AI errors become more subtle and harder to spot as reliability improves.

**Tags**: `#AI coding tools`, `#vibe coding`, `#agentic engineering`, `#software engineering practices`, `#LLM`

---

<a id="item-9"></a>
## [Anthropic and SpaceX Partner for Massive GPU Compute Boost](https://www.anthropic.com/news/higher-limits-spacex) ⭐️ 8.0/10

Anthropic announced a partnership with SpaceX to access the full compute capacity of the Colossus 1 datacenter, adding over 300 megawatts and 220,000 NVIDIA GPUs within a month. Immediately, Claude Code's rate limits for all paid plans are doubled, peak restrictions for Pro/Max users are removed, and Claude Opus API rate limits are significantly increased. This partnership dramatically increases Anthropic's compute capacity, accelerating model training and inference, and directly improves user experience with higher usage limits. It underscores the critical role of massive infrastructure partnerships in the competitive AI landscape. Colossus 1 is an xAI data center in Memphis, Tennessee, designed for AI workloads. The deal provides over 300 MW and 220,000 GPUs, with Claude Code's 5-hour rate limit doubled and peak restrictions eliminated for Pro/Max users.

telegram · zaihuapd · May 6, 16:35

**Background**: Colossus 1 is a large-scale AI data center built by Elon Musk's xAI, equipped with hundreds of thousands of NVIDIA GPUs. Anthropic develops the Claude family of large language models, which require enormous computational resources for training and inference. This partnership helps Anthropic secure the necessary compute power to scale its services.

<details><summary>References</summary>
<ul>
<li><a href="https://www.democracynow.org/2026/4/22/memphis_xai_data_center_pollution_keshaun">“ Colossus Failure”: Elon Musk’s Data Centers ... | Democracy Now!</a></li>
<li><a href="https://www.datacenterfrontier.com/machine-learning/article/55244139/the-colossus-ai-supercomputer-elon-musks-drive-toward-data-center-ai-technology-domination">datacenterfrontier.com/machine-learning/article/55244139/the...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SpaceX`, `#Claude`, `#GPU`, `#compute partnership`

---

<a id="item-10"></a>
## [Moonshot AI raises $7B+ at $10B valuation, Kimi revenue surges](https://t.me/zaihuapd/41251) ⭐️ 8.0/10

Chinese AI startup Moonshot AI completed a new funding round of over $7 billion on February 23, led by Alibaba, Tencent, and others, bringing its valuation to $10 billion. Its Kimi model's cumulative revenue in the last 20 days has surpassed the total for the entire year of 2025, with overseas revenue now exceeding domestic revenue. This funding round and revenue milestone underscore the rapid growth and global traction of Chinese AI startups in the competitive LLM landscape, potentially reshaping market dynamics and attracting further investment. Moonshot AI has raised over $12 billion in total funding to date, becoming a 'decacorn' in just over two years—the fastest in China. The K2.5 model on OpenRouter has driven significant API usage and paid user growth.

telegram · zaihuapd · May 7, 00:30

**Background**: Moonshot AI is a prominent Chinese startup focused on large language models (LLMs), known for its Kimi series. The company competes with other domestic players like Baidu and Alibaba in the rapidly evolving AI space. 'Decacorn' refers to a startup valued over $10 billion.

**Tags**: `#AI startup`, `#fundraising`, `#LLM`, `#Chinese tech`, `#valuation`

---

<a id="item-11"></a>
## [Apple's R&D Spending Hits 10.3% of Revenue, Fueling AI Push](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) ⭐️ 8.0/10

Apple's R&D spending reached 10.3% of revenue in its March 2026 fiscal quarter, the first time above 10% in 30 years, driven by accelerated AI investments. This historic R&D spending increase signals Apple's urgent shift toward AI, which could redefine its hardware ecosystem and competitive position in the post-iPhone era. While revenue grew 17%, R&D spending surged 34%, with focus on on-device AI, custom chips, and private cloud computing, along with products like AI glasses and camera-equipped AirPods.

telegram · zaihuapd · May 7, 01:00

**Background**: R&D spending as a percentage of revenue is a key indicator of a company's investment in future innovation. Apple has historically kept this ratio below 10%, but with the AI race intensifying, the company is making a strategic pivot to integrate AI deeply into its hardware.

**Tags**: `#Apple`, `#AI`, `#R&D`, `#Hardware`, `#Strategy`

---

<a id="item-12"></a>
## [Tencent Hy3 preview achieves 10x token calls over Hy2, tops OpenRouter weekly charts](https://finance.sina.com.cn/tech/shenji/2026-05-07/doc-inhwzrtp8521239.shtml) ⭐️ 8.0/10

Tencent's Hy3 preview model has reached token call volumes over 10 times that of its predecessor Hy2 in just two weeks of launch, and it has claimed the top spot on OpenRouter's weekly leaderboard for both overall usage and market share. This rapid adoption signals Hy3 preview's strong performance and efficiency, validated by the open community on OpenRouter, and positions Tencent as a competitive force in the large language model landscape, especially for agentic and coding workflows. Hy3 preview is a 295B-parameter Mixture-of-Experts (MoE) model with only 21B active parameters and supports up to 256K context length, making it highly efficient for production use. Its token processing in coding and agent scenarios increased over 16.5 times in Tencent's own applications like WorkBuddy and Codebuddy.

telegram · zaihuapd · May 7, 05:34

**Background**: The Hy3 preview is the first model trained on Tencent's rebuilt infrastructure, designed for agentic workflows and long-horizon reasoning. OpenRouter is a unified API platform that provides developers access to over 300 AI models through a single interface, and its weekly rankings reflect real-world usage patterns from thousands of applications. Mixture-of-Experts (MoE) is a neural network architecture that activates only a subset of parameters per token, enabling high performance with lower computational cost.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy3-preview">tencent / Hy 3 - preview · Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy3-preview:free">Hy 3 preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tencent`, `#large language model`, `#model performance`, `#technology`

---

<a id="item-13"></a>
## [Xiaomi Open-Sources OmniVoice: TTS for 646 Languages](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 8.0/10

Xiaomi has open-sourced OmniVoice, a massively multilingual voice cloning TTS model that supports 646 languages with a simple bidirectional Transformer architecture. This release democratizes high-quality multilingual TTS and voice cloning, outperforming commercial systems in 24-language tests and offering strong zero-shot capabilities for cross-lingual cloning. OmniVoice is trained on 580k hours of data from 50 open-source datasets, achieves 40x real-time inference in PyTorch, and its weights, training, and inference code are all open-sourced.

telegram · zaihuapd · May 7, 10:06

**Background**: TTS (Text-to-Speech) systems convert text into spoken audio. Voice cloning TTS can mimic a specific speaker's voice with only a few seconds of reference audio. OmniVoice's extreme multilingualism (646 languages) and zero-shot cloning make it notable.

<details><summary>References</summary>
<ul>
<li><a href="https://omnivoice.app/">OmniVoice : Free AI Voice Generator & Voice Cloning</a></li>
<li><a href="https://huggingface.co/k2-fsa/OmniVoice">k2-fsa/ OmniVoice · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#voice cloning`, `#open source`, `#multilingual`, `#xiaomi`

---

<a id="item-14"></a>
## [UK FCA Investigates PayPal, Mastercard, Visa Over Digital Wallet Contracts](https://www.fca.org.uk/news/press-releases/competition-act-1998-investigations) ⭐️ 8.0/10

The UK Financial Conduct Authority has launched competition investigations into PayPal, Mastercard, and Visa, focusing on contractual terms related to PayPal's digital wallet. The FCA has not yet concluded whether competition law has been breached. This investigation could reshape the UK digital wallet market, which saw its transaction share jump from 8% to 29% in the past year. It may affect competition, innovation, and market access for new entrants. The investigation specifically targets contract clauses that may restrict competition. All three companies have stated they will cooperate with the FCA.

telegram · zaihuapd · May 7, 14:46

**Background**: Digital wallets allow users to store payment card information on mobile devices and make contactless payments. The UK digital wallet market has grown rapidly, with its transaction share rising from 8% in 2023 to 29% currently. The FCA is examining whether certain contract terms hinder competition among digital wallet providers.

**Tags**: `#反垄断`, `#数字钱包`, `#支付监管`, `#金融科技`, `#英国FCA`

---