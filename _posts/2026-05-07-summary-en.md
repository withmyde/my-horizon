---
layout: default
title: "Horizon Summary: 2026-05-07 (EN)"
date: 2026-05-07
lang: en
---

> From 28 items, 10 important content pieces were selected

---

1. [Firefox Hardened with Claude Mythos Finds Hundreds of Bugs](#item-1) ⭐️ 9.0/10
2. [Anthropic Partners with SpaceX to Boost Claude Compute Limits](#item-2) ⭐️ 9.0/10
3. [Chrome removes on-device AI privacy claim](#item-3) ⭐️ 8.0/10
4. [SQLite Endorsed by Library of Congress as Storage Format](#item-4) ⭐️ 8.0/10
5. [Motherboard sales collapse 25% as AI chip demand diverts supply](#item-5) ⭐️ 8.0/10
6. [Moonshot AI valuation tops $10B with new $700M+ funding](#item-6) ⭐️ 8.0/10
7. [Apple R&D Spending Hits 10% of Revenue, Accelerates AI Push](#item-7) ⭐️ 8.0/10
8. [Tencent Hy3 Preview Surpasses Hy2 by 10x in Two Weeks](#item-8) ⭐️ 8.0/10
9. [Google Cloud turns reCAPTCHA into Fraud Defense with QR code verification](#item-9) ⭐️ 8.0/10
10. [Xiaomi Open-Sources OmniVoice: 646-Language TTS with Minimalist Architecture](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Hardened with Claude Mythos Finds Hundreds of Bugs](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla used the Claude Mythos preview, combined with improved prompting techniques, to locate and fix 423 security bugs in Firefox in April 2026 — a dramatic increase from the typical 20-30 per month. This marks a paradigm shift from AI-generated security reports being dismissed as 'unwanted slop' to actually discovering hundreds of real vulnerabilities at scale, significantly improving open-source software security. The AI harness was often blocked by Firefox's defense-in-depth measures, yet it still uncovered ancient bugs including a 20-year-old XSLT bug and a 15-year-old <legend> element bug. The fix count jumped from 20-30 per month in 2025 to 423 in April 2026.

rss · Simon Willison · May 7, 17:56

**Background**: Claude Mythos Preview is Anthropic's most advanced frontier large language model, released in April 2026 as part of Project Glasswing. It is used via Claude Code in isolated containers to agentically find security vulnerabilities. Previously, AI-generated security reports were often incorrect and imposed high costs on maintainers, but recent improvements in model capability and prompting techniques have changed this dynamic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#Firefox`, `#vulnerability detection`, `#LLM`

---

<a id="item-2"></a>
## [Anthropic Partners with SpaceX to Boost Claude Compute Limits](https://t.me/zaihuapd/41259) ⭐️ 9.0/10

Anthropic has announced a partnership with SpaceX to use the entire compute capacity of the Colossus 1 data center, providing over 220,000 NVIDIA GPUs and more than 300 megawatts of additional capacity. As a result, Claude Code's rate limits have been doubled and Pro/Max peak restrictions removed, while Claude Opus API limits have also been significantly increased. This deal secures a massive compute resource for Anthropic, enabling it to scale Claude services and meet growing demand from developers and enterprises. It also highlights the increasing importance of large-scale GPU clusters as critical infrastructure for AI competition. The agreement grants Anthropic exclusive access to the Colossus 1 data center, which was originally built by xAI for training Grok. The capacity addition comes from both Colossus 1 and other recent agreements with Amazon and Google.

telegram · zaihuapd · May 7, 08:19

**Background**: Colossus is a supercomputer launched by xAI in September 2024, located in Memphis, Tennessee, and is considered the world's largest AI supercomputer with 100,000 NVIDIA H100 GPUs initially. Anthropic develops the Claude family of AI models, competing with OpenAI's GPT and Google's Gemini. Compute power is a critical constraint for AI companies, as training and running large models require vast numbers of GPUs and high energy consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/news/anthropic-to-rent-all-ai-capacity-at-spacexs-colossus-data-center-180327774.html">Anthropic to rent all AI capacity at SpaceX's Colossus data center</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#算力`, `#合作`, `#NVIDIA`, `#Claude`

---

<a id="item-3"></a>
## [Chrome removes on-device AI privacy claim](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/) ⭐️ 8.0/10

Google Chrome deleted a statement from its documentation that claimed on-device AI features do not send data to Google servers, raising new privacy concerns. This removal erodes user trust by implying that data may now be sent to servers, contradicting the earlier privacy assurance. It affects millions of Chrome users who rely on built-in AI features. The removal was noticed in Chrome's documentation for on-device AI features like Gemini Nano, which was recently found to be silently downloading a 4GB model to user devices without clear consent.

hackernews · newsoftheday · May 7, 15:56 · [Discussion](https://news.ycombinator.com/item?id=48050964)

**Background**: On-device AI runs machine learning models locally on the user's device to provide features like writing assistance and scam detection without sending data to the cloud. Chrome's Gemini Nano is Google's lightweight AI model for on-device tasks, but its silent download and now removed privacy claim have sparked controversy over data collection practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.google.com/chrome/ai-innovations/">Gemini in Chrome | The next generation of AI in Chrome | Chrome</a></li>
<li><a href="https://developer.chrome.com/docs/ai/get-started">Get started with built-in AI | AI on Chrome | Chrome for Developers</a></li>
<li><a href="https://www.tomsguide.com/ai/check-your-storage-chrome-may-be-downloading-a-4gb-ai-model-heres-what-we-know">'No clear consent flow for this download': Google Chrome is silently stashing a 4GB AI model on your device — and Google just responded | Tom's Guide</a></li>

</ul>
</details>

**Discussion**: Community comments expressed widespread distrust, with users noting that adding AI to desktop apps is an effective way to collect data without user awareness. Some questioned whether Google ever truly disabled data sending, while others recommended switching to alternatives like Brave.

**Tags**: `#privacy`, `#chrome`, `#google`, `#ai`, `#data-collection`

---

<a id="item-4"></a>
## [SQLite Endorsed by Library of Congress as Storage Format](https://sqlite.org/locrsf.html) ⭐️ 8.0/10

The Library of Congress has officially listed SQLite as a recommended storage format for long-term digital preservation of datasets. This recognition was highlighted in the 2026 Recommended Formats Statement. This endorsement from a major preservation authority validates SQLite's reliability and suitability for archiving, influencing preservation practices across libraries, institutions, and developers. It may encourage broader adoption of SQLite in data-intensive applications and reinforce trust in its long-term viability. SQLite is one of four formats recommended by the Library of Congress for dataset storage, as part of its 'Recommended Formats Statement' for digital preservation. The recommendation applies to datasets, not general-purpose file formats.

hackernews · whatisabcdefgh · May 6, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48042434)

**Background**: The Library of Congress maintains a list of recommended formats for long-term preservation to ensure digital content remains accessible over time. SQLite is a self-contained, serverless database engine widely used in applications for its simplicity, reliability, and zero configuration. Being recommended means it meets criteria like openness, stability, widespread adoption, and absence of proprietary restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQLite">SQLite - Wikipedia</a></li>
<li><a href="https://thecodersblog.com/sqlite-as-recommended-storage-format-2026/">SQLite: Library of Congress Recommended for Digital Preservation</a></li>

</ul>
</details>

**Discussion**: Community comments reveal mixed perspectives: some praise SQLite's simplicity but raise concerns about PII in portable files, while others admit shifting from viewing it as a toy to using it extensively. One user notes the announcement is from 2018, but the recognition remains relevant.

**Tags**: `#sqlite`, `#digital preservation`, `#databases`, `#data storage`

---

<a id="item-5"></a>
## [Motherboard sales collapse 25% as AI chip demand diverts supply](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers) ⭐️ 8.0/10

Motherboard sales have dropped over 25% as chipmakers prioritize AI chip production over consumer PC components, with ASUS projected to sell 5 million fewer boards in 2025 and other major vendors like Gigabyte, MSI, and ASRock also expecting reduced sales. This shift signals a fundamental realignment of the PC hardware industry, where AI demand is not only raising component prices but also reducing availability and innovation in consumer hardware, potentially pushing enthusiasts away from the PC platform. The shortage extends beyond motherboards to cases, fans, consumer SSDs, and other PC accessories, and is exacerbated by chipmakers reallocating fab capacity toward higher-margin AI chips, leading to supply constraints expected to persist through 2027.

hackernews · speckx · May 7, 15:23 · [Discussion](https://news.ycombinator.com/item?id=48050540)

**Background**: Motherboards connect all PC components and are essential for custom-built desktops. Recent years have seen diminishing performance gains from new CPU/GPU generations, reducing upgrade incentives. Meanwhile, AI boom has diverted chip manufacturing capacity, causing shortages and price hikes for conventional memory and logic chips used in consumer PCs.

<details><summary>References</summary>
<ul>
<li><a href="https://sourceability.com/post/ai-chip-shortages-deepen-amid-tariff-risks">AI demand sparks memory supply chain strain | Sourceability</a></li>
<li><a href="https://wccftech.com/amd-warns-pc-gaming-demand-will-decline-in-h2-as-memory-prices-surge/">AMD Warns PC & Gaming Demand Will Decline In H2 As Memory...</a></li>

</ul>
</details>

**Discussion**: Commenters lament that PC hardware prices have surged—motherboards once cost $100–200 now command $300+, and diminishing returns on performance make upgrades less compelling. Some see a paradox: AI is both causing shortages and reducing the need for powerful PCs, as tasks shift to the cloud.

**Tags**: `#AI`, `#PC Hardware`, `#Supply Chain`, `#Market Trends`, `#Consumer Electronics`

---

<a id="item-6"></a>
## [Moonshot AI valuation tops $10B with new $700M+ funding](https://t.me/zaihuapd/41251) ⭐️ 8.0/10

Moonshot AI completed a new funding round of over $700 million, pushing its valuation past $10 billion in just over two years, and its Kimi assistant generated more revenue in the last 20 days than its entire 2025 annual total. This milestone highlights strong investor confidence in Chinese AI startups and the rapid monetization of large language models, with Kimi's overseas revenue surpassing domestic, signaling global competitiveness. The round was co-led by Alibaba, Tencent, 5Y Capital, and Jiuan, bringing total funding to over $1.2 billion; Kimi's K2.5 model, which supports agent swarms of up to 100 specialized agents, is available on OpenRouter and has driven revenue growth.

telegram · zaihuapd · May 7, 00:30

**Background**: Moonshot AI is a Chinese startup known for its Kimi assistant and the K2.5 large language model. A 'decacorn' is a startup valued at over $10 billion. OpenRouter is a platform that provides unified API access to multiple AI models, including K2.5.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MoonshotAI/Kimi-K2.5">GitHub - MoonshotAI/Kimi-K2.5: Moonshot's most powerful model · GitHub</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/Kimi-K2.5 · Hugging Face</a></li>
<li><a href="https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model">Kimi K2.5: Complete Guide to Moonshot's AI Model | Codecademy</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI startup`, `#funding`, `#Moonshot AI`, `#Kimi`, `#valuation`

---

<a id="item-7"></a>
## [Apple R&D Spending Hits 10% of Revenue, Accelerates AI Push](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) ⭐️ 8.0/10

Apple's R&D spending rose to 10.3% of revenue in its March 2026 fiscal quarter, the first time above 10% in 30 years, driven by a 34% year-over-year increase in investment focused on AI. This milestone signals Apple's strategic pivot to AI as a core platform enabler, similar to the iPod era, and will reshape its hardware ecosystem with on-device AI, custom chips, and private cloud computing. Apple is investing heavily in on-device AI, custom chips (including M5 for Private Cloud Compute), and new products such as AI glasses and camera-equipped AirPods, alongside the first foldable iPhone and Siri upgrades.

telegram · zaihuapd · May 7, 01:00

**Background**: On-device AI runs artificial intelligence algorithms locally on devices, reducing latency and improving privacy compared to cloud-based AI. Apple's Private Cloud Compute (PCC) uses dedicated servers with custom chips to process sensitive AI tasks while maintaining user privacy. These technologies are key to Apple's strategy of integrating AI deeply into its hardware ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.sina.com.cn/stock/t/2025-12-10/doc-inhaicsz1972147.shtml">概念研究所-什么是AI端侧？|AI_新浪财经_新浪网</a></li>
<li><a href="https://semiconductor.samsung.cn/technologies/processor/on-device-ai/">端侧AI | 技术 | 三星半导体官网</a></li>
<li><a href="https://stock.10jqka.com.cn/usstock/20260218/c674837048.shtml">消息称 苹 果 AI 私 有 云 端 算 力大跃进：跳过 M3 和 M4，直接部署 M5 芯片</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI`, `#研发`, `#硬件生态`

---

<a id="item-8"></a>
## [Tencent Hy3 Preview Surpasses Hy2 by 10x in Two Weeks](https://finance.sina.com.cn/tech/shenji/2026-05-07/doc-inhwzrtp8521239.shtml) ⭐️ 8.0/10

Tencent's Hy3 preview model, a 295B-parameter Mixture-of-Experts (MoE) model, achieved 10 times the token usage of its predecessor Hy2 within two weeks of launch and ranked first on OpenRouter's weekly leaderboard. This rapid adoption signals strong product-market fit for Tencent's latest AI model, especially in coding and agentic workflows, and demonstrates the growing importance of efficient MoE models for production deployment. Hy3 preview is a 295B-parameter MoE model with only 21B active parameters and a 3.8B MTP layer, enabling efficient inference. It supports configurable reasoning levels (disabled, low, high) and was made temporarily free on OpenRouter to gather real-world feedback.

telegram · zaihuapd · May 7, 05:34

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, offering a balance between model capacity and computational cost. Tencent's Hy3 preview is the first model from the company's rebuilt training infrastructure. OpenRouter is a unified API platform that aggregates hundreds of LLMs from different providers.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy3-preview">tencent / Hy 3 - preview · Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy3-preview:free">Hy 3 preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://docs.clore.ai/guides/language-models/hy3-preview">Hy 3 Preview ( Tencent Hunyuan 3, 295B MoE) | Guides | Clore.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#Tencent`, `#model deployment`, `#OpenRouter`

---

<a id="item-9"></a>
## [Google Cloud turns reCAPTCHA into Fraud Defense with QR code verification](https://support.google.com/recaptcha/answer/16609652?hl=en) ⭐️ 8.0/10

Google Cloud announced Fraud Defense, the next evolution of reCAPTCHA, which introduces a QR code challenge to verify human presence on websites and apps. This move upgrades a widely-used bot detection tool to combat AI-driven fraud with a novel, user-friendly verification method, impacting security across the web. The QR code verification requires users to scan a code with their phone; it is compatible with Android Google Play Services 25.41.30+, iOS/iPadOS 15.0+, and has specific version requirements for the 'Click to Verify' button.

telegram · zaihuapd · May 7, 09:18

**Background**: reCAPTCHA is a CAPTCHA system from Google that distinguishes humans from bots. Fraud Defense extends this into a comprehensive trust platform for the agentic web, providing risk scores and forensic reasons to automate security policies.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/security/products/fraud-defense">Google Cloud Fraud Defense - The evolution of reCAPTCHA.</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha">Introducing Google Cloud Fraud Defense , the... | Google Cloud Blog</a></li>

</ul>
</details>

**Tags**: `#security`, `#reCAPTCHA`, `#fraud prevention`, `#Google Cloud`, `#QR code`

---

<a id="item-10"></a>
## [Xiaomi Open-Sources OmniVoice: 646-Language TTS with Minimalist Architecture](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 8.0/10

Xiaomi has open-sourced OmniVoice, a multilingual text-to-speech (TTS) model that supports 646 languages with a minimalist bidirectional Transformer architecture. It achieves 100,000 hours of training per day and 40x real-time inference on PyTorch, with quality surpassing comparable mainstream models. This open-source release democratizes high-quality multilingual TTS, enabling developers and researchers to build voice applications across a vast number of languages without needing massive proprietary data. It also fills a gap in the open-source community for a scalable, efficient, and competitive multilingual TTS system. The model uses full-codebook random masking and leverages pretrained large language model parameters to enhance training efficiency and intelligibility. It was trained on 580,000 hours of data from 50 open datasets, outperforming commercial systems in 24 languages and approaching real speech in 102 languages.

telegram · zaihuapd · May 7, 10:06

**Background**: Text-to-speech (TTS) converts text into spoken audio. Multilingual TTS models that handle many languages are challenging due to data scarcity and phonetic diversity. OmniVoice's approach combines a simple Transformer design with techniques from large language models to achieve broad language coverage and high efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/full-codebook-random-masking">Full - Codebook Random Masking</a></li>
<li><a href="https://github.com/soobinseo/Transformer-TTS/blob/master/module.py">Transformer - TTS /module.py at master · soobinseo/ Transformer - TTS</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#multilingual`, `#open source`, `#speech synthesis`, `#Xiaomi`

---