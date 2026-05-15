---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 31 items, 13 important content pieces were selected

---

1. [Bun Merges Rewrite from Zig to Rust](#item-1) ⭐️ 10.0/10
2. [vLLM v0.21.0 Released: Breaking Changes and New Features](#item-2) ⭐️ 9.0/10
3. [First Public macOS Kernel Exploit on Apple M5](#item-3) ⭐️ 9.0/10
4. [Critical NGINX RCE Vulnerability Discovered After 18 Years](#item-4) ⭐️ 9.0/10
5. [DeepSeek Session Isolation Flaw via Unclosed <think String](#item-5) ⭐️ 9.0/10
6. [Removing Modem and GPS from 2024 Toyota RAV4 Hybrid](#item-6) ⭐️ 8.0/10
7. [antirez Unveils DwarfStar4 for Local DeepSeek 4 Inference](#item-7) ⭐️ 8.0/10
8. [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM](#item-8) ⭐️ 8.0/10
9. [Codex integrated into ChatGPT mobile app for free](#item-9) ⭐️ 8.0/10
10. [arXiv bans hallucinated references with 1-year submission ban](#item-10) ⭐️ 8.0/10
11. [US approves Nvidia H200 sales to Chinese firms, Nvidia seeks breakthrough](#item-11) ⭐️ 8.0/10
12. [Global obesity trends diverge by income level](#item-12) ⭐️ 8.0/10
13. [JD.com lists sanctioned NVIDIA AI GPUs](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun Merges Rewrite from Zig to Rust](https://github.com/oven-sh/bun/pull/30412) ⭐️ 10.0/10

Bun, the JavaScript runtime, has merged a pull request that rewrites its core from Zig to Rust, adding over 1 million lines of Rust code. This shift from Zig to Rust is a major architectural change for a widely-used runtime, potentially improving memory safety and reducing bugs like use-after-free. According to the merge commit, the new Rust codebase includes over 1 million lines, with 10,428 uses of `unsafe` across 736 files, as noted in a community analysis.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Background**: Bun is a JavaScript runtime and toolkit designed for speed, originally written in the Zig language. Zig is a system programming language that competes with C, offering compile-time features and manual memory management. Rewriting in Rust, which provides stronger safety guarantees, is a significant codebase migration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://grokipedia.com/page/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>

</ul>
</details>

**Discussion**: Community responses highlight the precise preparation with mapping files and smart pointer types (sesm), and concerns about complexity as Bun approaches the size of the Rust compiler (vitaminCPP). Jarred noted that Rust will catch many memory bugs but not all, especially those crossing the JS boundary.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-2"></a>
## [vLLM v0.21.0 Released: Breaking Changes and New Features](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 introduces breaking changes including deprecation of Transformers v4 and a new C++20 build requirement, along with major new features such as KV offloading with hybrid memory allocator, speculative decoding with thinking budgets, and a TOKENSPEED_MLA backend for Blackwell GPUs. This release significantly impacts the vLLM community as users must migrate to Transformers v5 and upgrade their build tools, while gaining substantial performance and memory efficiency improvements that enable larger model deployments and faster inference on modern hardware. The release includes 367 commits from 202 contributors, with new model architectures supported (e.g., MiMo-V2.5, Moondream3, Cohere MoE) and enhancements to speculative decoding, KV offloading, and engine core stability.

github · khluu · May 14, 23:15

**Background**: KV cache offloading is a technique to reduce GPU memory usage by moving key-value cache data to CPU or NVMe storage, allowing larger context lengths or batch sizes. vLLM's hybrid memory allocator manages heterogeneous memory pools efficiently. Speculative decoding uses a smaller draft model to accelerate generation, and thinking budgets constrain reasoning steps for improved efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bentoml.com/llm/inference-optimization/kv-cache-offloading">KV cache offloading | LLM Inference Handbook</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm -project/ vllm</a></li>
<li><a href="https://lmstudio.ai/docs/app/advanced/speculative-decoding">Speculative Decoding | LM Studio</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#release`, `#LLM inference`, `#breaking change`, `#AI/ML`

---

<a id="item-3"></a>
## [First Public macOS Kernel Exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

A security research team publicly disclosed the first kernel memory corruption exploit targeting Apple's M5 chip, bypassing hardware memory protections like MTE (Memory Tagging Extension). This marks a significant security milestone as it demonstrates that even Apple's latest M5 chip with advanced memory protections is vulnerable to kernel-level attacks, potentially impacting macOS security posture and bug bounty valuations. The exploit reportedly bypasses MTE, and a detailed 55-page report is available. Some community members noted that the exploit could be valued at $100,000 to $1.5 million on Apple's bug bounty program depending on how it is packaged.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: Apple M5 is the latest ARM-based system-on-a-chip in Apple's silicon family, featuring unified memory and hardware security features like Memory Tagging Extension (MTE) to detect memory corruption. Kernel memory corruption is a critical vulnerability class that allows attackers to gain full control of the operating system. Previously, public exploits for Apple M-series chips were rare, making this disclosure notable.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5 - Calif</a></li>
<li><a href="https://news.ycombinator.com/item?id=48139219">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community expressed mixed reactions: some praised the technical achievement and called it a significant security milestone, while others noted a lack of details and questioned how the exploit bypassed MTE. There was also discussion about potential bug bounty valuations, with estimates ranging from $100,000 to $1.5 million. A few users expressed skepticism, suggesting the exploit might be overhyped.

**Tags**: `#security`, `#macOS`, `#kernel exploit`, `#Apple M5`, `#vulnerability`

---

<a id="item-4"></a>
## [Critical NGINX RCE Vulnerability Discovered After 18 Years](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability) ⭐️ 9.0/10

Security researchers disclosed CVE-2026-42945, a critical heap buffer overflow in NGINX's rewrite module affecting all versions from 0.6.27 to 1.30.0, allowing unauthenticated remote code execution. This vulnerability, with a CVSS v4.0 score of 9.2, impacts billions of servers globally, including NGINX Open Source, NGINX Plus, and many enterprise products, posing a massive security risk. The vulnerability originates from a two-pass execution inconsistency in the script engine: the first pass calculates buffer length without considering character escaping, while the second pass expands special characters (e.g., '?' to %3F), causing heap overflow.

telegram · zaihuapd · May 14, 02:41

**Background**: NGINX is a widely used web server and reverse proxy, often deployed as an ingress controller in Kubernetes environments. The ngx_http_rewrite_module uses a two-pass script engine to process rewrite directives. A heap buffer overflow occurs when the length calculation pass underestimates the final buffer size due to URI encoding expansion.

<details><summary>References</summary>
<ul>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via an 18-Year-Old ...</a></li>
<li><a href="https://github.com/nginx/nginx/blob/master/src/http/modules/ngx_http_rewrite_module.c">nginx/src/http/modules/ngx_http_rewrite_module.c at master · nginx/nginx</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that while the published PoC assumes ASLR is disabled, the researchers claim there is a reliable way to bypass ASLR. Some users note that the exploit requires specific rewrite configurations (unnamed capture groups with a question mark in the replacement string). Others discuss the difficulty of finding memory-safe alternatives to Apache and NGINX.

**Tags**: `#nginx`, `#security`, `#vulnerability`, `#rce`, `#cve`

---

<a id="item-5"></a>
## [DeepSeek Session Isolation Flaw via Unclosed <think String](https://github.com/deepseek-ai/DeepSeek-R1/issues/840) ⭐️ 9.0/10

A session isolation vulnerability was discovered in DeepSeek's dialogue system where sending an unclosed '<think' string in a new empty conversation can cause the model to return fragments of other users' conversations, potentially leaking sensitive data. The vulnerability was responsibly disclosed by user cancat2024 on May 11, 2026. This vulnerability poses a critical security risk as it can expose private conversation data including code, keys, and personal information of other users. It highlights significant weaknesses in session isolation mechanisms in AI chatbots, which is particularly concerning for enterprise and consumer deployments. The attack works by simply inputting an unclosed '<think' token in a fresh conversation, triggering the model to hallucinate and output content from other sessions. The issue has been confirmed to affect both DeepSeek Web and API, and reportedly also appears in third-party deployments, suggesting it may be an inherent hallucination behavior.

telegram · zaihuapd · May 14, 13:15

**Background**: Session isolation is a fundamental security requirement for multi-user AI chatbots, ensuring each user's conversation context remains separate. Special tokens like '<think>' are used by some models to indicate reasoning steps, but when left unclosed, the model may misinterpret the prompt and leak cross-session data. This vulnerability is a form of prompt injection that exploits the model's tendency to complete patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://successquarterly.com/deepseek-data-breach-highlights-ai-industrys-security-vulnerabilities/">DeepSeek Data Breach Highlights AI Industry's Security Vulnerabilities</a></li>
<li><a href="https://injectiqa.com/blog/prompt-inject-enterprise-deepseek">Prompt Injection in the Enterprise: Dissecting the DeepSeek ...</a></li>

</ul>
</details>

**Discussion**: The community discussion notes that the same issue appears in third-party deployments, indicating it is a hallucination phenomenon rather than a server-side data mix-up. The reporter acted responsibly by disclosing without exploiting the vulnerability for data collection.

**Tags**: `#security`, `#vulnerability`, `#DeepSeek`, `#data-leakage`, `#AI`

---

<a id="item-6"></a>
## [Removing Modem and GPS from 2024 Toyota RAV4 Hybrid](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

A detailed technical guide has been published showing how to physically remove the telematics control module and GPS antenna from a 2024 Toyota RAV4 hybrid to stop vehicle data collection. This guide addresses growing privacy concerns over car telemetry data being shared with insurance companies and third parties, and empowers owners to regain control of their data without software hacks. The removal process involves disconnecting the telematics control unit behind the glove box and removing the GPS antenna from the dashboard, which does not trigger any dashboard warning lights.

hackernews · arkadiyt · May 14, 17:08 · [Discussion](https://news.ycombinator.com/item?id=48138136)

**Background**: Modern connected vehicles collect and transmit data such as location, speed, and driving behavior through built-in cellular modems. This data is often shared with third parties without explicit consent, raising significant privacy issues. The guide provides a hardware-based solution for those opposed to telemetry.

<details><summary>References</summary>
<ul>
<li><a href="https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid</a></li>
<li><a href="https://news.ycombinator.com/item?id=48138136">Removing the modem and GPS from my 2024 RAV4 hybrid - Hacker News</a></li>
<li><a href="https://www.reddit.com/r/cars/comments/1td7mi2/removing_the_modem_and_gps_from_my_2024_rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid : r/cars - Reddit</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects a divide: some users appreciate the privacy focus and technical detail, while others argue that disabling connectivity negates the benefits of modern features like over-the-air updates. A few commenters share alternative solutions, such as removing a specific fuse on other car models.

**Tags**: `#privacy`, `#telematics`, `#car hacking`, `#DIY`, `#Toyota`

---

<a id="item-7"></a>
## [antirez Unveils DwarfStar4 for Local DeepSeek 4 Inference](https://antirez.com/news/165) ⭐️ 8.0/10

antirez, creator of Redis, announced DwarfStar4 (DS4), a small LLM inference runtime that can run DeepSeek 4 locally on hardware with 96GB VRAM, achieving performance close to Claude. This marks significant progress in local model deployment, enabling powerful open-source models like DeepSeek 4 to run on consumer-grade hardware, potentially reducing reliance on cloud APIs and improving privacy. DwarfStar4 currently requires 96GB of VRAM, targets Metal (macOS) as primary backend, with NVIDIA CUDA and AMD ROCm support (ROCm maintained separately by community). It builds upon llama.cpp and GGML.

hackernews · caust1c · May 14, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48142108)

**Background**: LLM inference runtimes are software stacks that allow large language models to be executed efficiently on hardware. DeepSeek 4 is a powerful open-source LLM. Local inference enables offline use and data privacy, but typically requires high-end GPUs due to model size. DwarfStar4 is a lightweight runtime optimized for this purpose.

**Discussion**: Commenters noted that DS4 feels shockingly close to Claude in quality, though slower, and observed self-awareness in the model (e.g., recognizing its own server process). They also discussed the potential for local models to approach or match cloud capabilities within a few years.

**Tags**: `#LLM`, `#inference`, `#local models`, `#DeepSeek`, `#AI runtime`

---

<a id="item-8"></a>
## [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

The author successfully connected an NVIDIA RTX 5090 via a Thunderbolt eGPU enclosure to an M4 MacBook Air, enabling Windows gaming through GPU passthrough and achieving substantial speedups in LLM prompt processing. This demonstrates that eGPUs remain viable on Apple Silicon for specific workloads, offering a bridge for Mac users who need high-end graphics for gaming or AI inference without switching to a PC. The setup overcomes macOS's poor OpenGL support and lack of native GPU passthrough, but requires significant effort; LLM benchmarks show prompt processing speed more than doubles with the RTX 5090 compared to the M4's built-in GPU.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: An eGPU (external GPU) connects a desktop graphics card to a laptop via Thunderbolt, boosting graphical performance. LLM inference involves running large language models; prompt processing (prefill) is a memory-bandwidth-intensive step that is often slow on Macs due to unified memory bandwidth limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://biztechmagazine.com/article/2022/08/what-external-graphics-processing-unit-perfcon">What Is an External Graphics Processing Unit (eGPU) and How Does it Boost Performance?</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/external-gpu/">What is an external graphics processing unit (GPU)?</a></li>
<li><a href="https://www.computerhope.com/jargon/e/egpu.htm">What Is an eGPU (External Graphics Processing Unit)?</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article's technical depth, with one highlighting that the LLM performance improvement is the most practical takeaway. Another noted the irony that Doom (2016) requires this setup on Mac, while others discussed GPU passthrough challenges and AI model limitations.

**Tags**: `#eGPU`, `#MacBook Air`, `#RTX 5090`, `#gaming`, `#LLM`

---

<a id="item-9"></a>
## [Codex integrated into ChatGPT mobile app for free](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 8.0/10

OpenAI has integrated its Codex AI coding assistant into the ChatGPT mobile app, making it available to free-tier users. This enables developers to write and edit code directly from their smartphones using natural language prompts. This integration lowers the barrier to AI-powered coding, allowing developers to work on code from anywhere without requiring a desktop or paid subscription. It could accelerate mobile-first development workflows and make coding assistance more ubiquitous. Codex is available in the ChatGPT mobile app's sidebar as a dedicated feature, and users sign in with their ChatGPT account. Free-tier interactions may be used for model training, as noted by the community.

hackernews · mikeevans · May 14, 20:06 · [Discussion](https://news.ycombinator.com/item?id=48140529)

**Background**: OpenAI Codex is a series of large language models fine-tuned on source code to translate natural language into code. Originally launched in 2021, it has evolved into both a language model and an AI agent product. The integration into the ChatGPT mobile app extends its accessibility beyond desktop and CLI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://developers.openai.com/codex/models">Models – Codex | OpenAI Developers</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about Codex being free, with some calling it a long-desired feature. However, concerns are raised about mobile UX limitations, such as smaller screens causing less effective direction of the agent, and requests for remote CLI support on Linux machines.

**Tags**: `#Codex`, `#ChatGPT mobile`, `#OpenAI`, `#AI coding assistant`, `#developer tools`

---

<a id="item-10"></a>
## [arXiv bans hallucinated references with 1-year submission ban](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv has introduced a new policy that imposes a 1-year ban on authors who submit papers containing hallucinated references, and subsequently requires that their future submissions be accepted at a reputable peer-reviewed venue before being posted on arXiv. This policy directly addresses the growing misuse of LLMs in academic publishing, where fabricated citations undermine research integrity and waste reviewers' time. It sets a strong precedent for other preprint servers and publishers to follow. The ban applies to submissions with hallucinated references, and after the ban, authors must have their work accepted by a reputable peer-reviewed venue before resubmitting to arXiv. The policy is not yet fully detailed on arXiv's website but has been announced.

hackernews · gjuggler · May 14, 20:39 · [Discussion](https://news.ycombinator.com/item?id=48140922)

**Background**: Hallucinated references are fake citations generated by large language models (LLMs) that appear plausible but do not exist. These have become a growing problem in academic papers, as LLMs like ChatGPT can fabricate references that pass AI detection tools and mislead readers. arXiv is a widely used preprint repository that allows researchers to share early versions of papers before formal peer review.

<details><summary>References</summary>
<ul>
<li><a href="https://ref-check.org/">ref-check.org — Academic Reference Verification Tool</a></li>
<li><a href="https://arxiv.org/pdf/2604.16407">26-19 How unique are hallucinated citations 2026-03-31</a></li>
<li><a href="https://writemask.com/blog/aigenerated-detect-or-detection-or-detector-or-text-or-literature-or-references-or-manuscript-or-academic-or-hallucination-or-paper-or-article">AI Hallucinations in Academic Papers : 7 Problems No... — WriteMask</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with users like rgmerk applauding the move as necessary for quality control. Some commenters caution about careful vetting before imposing bans, while others note that LLM enthusiasts are angry about the restrictions, highlighting a divide in attitudes towards AI-generated content.

**Tags**: `#arXiv`, `#academic publishing`, `#LLM misuse`, `#policy`, `#research integrity`

---

<a id="item-11"></a>
## [US approves Nvidia H200 sales to Chinese firms, Nvidia seeks breakthrough](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) ⭐️ 8.0/10

The US Commerce Department has approved the sale of Nvidia's H200 chips to about 10 Chinese companies, including Alibaba, Tencent, ByteDance, and JD.com, with distributors like Lenovo and Foxconn also receiving licenses, though no deliveries have been completed yet. This development signals a potential shift in US-China tech tensions, as it allows high-end AI chips to flow to Chinese firms, impacting the global AI hardware supply chain and China's ability to advance AI models. The H200 GPU features 141 GB of HBM3e memory with 4.8 TB/s bandwidth, nearly double the capacity of the H100, and is designed for large language models and long-context workloads; each customer can purchase up to 75,000 units.

telegram · zaihuapd · May 14, 08:57

**Background**: The US has imposed export controls on advanced AI chips to China, citing national security concerns. The H200 is based on Nvidia's Hopper architecture and is among the most powerful AI accelerators available. Chinese firms have been seeking alternatives amid restrictions, but domestic chips lag behind.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/h200/">H200 GPU | NVIDIA</a></li>
<li><a href="https://www.runpod.io/articles/guides/nvidia-h200-gpu">Nvidia H200 GPU: Specs, VRAM, Price, and AI Performance</a></li>
<li><a href="https://lenovopress.lenovo.com/lp1944-nvidia-h200-141gb-gpu">ThinkSystem NVIDIA H200 141GB GPUs Product Guide > Lenovo Press</a></li>

</ul>
</details>

**Tags**: `#chips`, `#AI hardware`, `#US-China`, `#Nvidia`, `#trade policy`

---

<a id="item-12"></a>
## [Global obesity trends diverge by income level](https://www.nature.com/articles/s41586-026-10383-0) ⭐️ 8.0/10

A study covering 200 countries and 232 million people reveals that obesity rates have stabilized in high-income countries since the 2000s, while continuing to rise in middle- and low-income countries, with some low-income countries now surpassing high-income nations in prevalence. This shift in obesity trends indicates that public health interventions in high-income countries may be effective, but underscores the urgent need for policy action in developing nations to address the growing obesity epidemic. The study analyzed data from 1980 to 2024, noting that in high-income countries, child and adolescent obesity rates began to slow in the 1990s, with some countries like Italy, Portugal, and France even seeing slight declines.

telegram · zaihuapd · May 14, 09:45

**Background**: Obesity is a major global health issue linked to chronic diseases such as diabetes and cardiovascular disease. This large-scale epidemiological study provides the most comprehensive picture of obesity trends across 200 countries over four decades, highlighting how economic development influences nutritional transitions.

**Tags**: `#public health`, `#obesity`, `#epidemiology`, `#global health`, `#nutrition`

---

<a id="item-13"></a>
## [JD.com lists sanctioned NVIDIA AI GPUs](https://u.jd.com/HaDkFMa) ⭐️ 8.0/10

JD.com launched an 'AI Hardware JD Self-Operated Store' that lists previously sanctioned NVIDIA GPUs including the RTX 5090 32GB Turbo Edition, RTX PRO 6000 Blackwell server edition, and H100. This move could signal a potential circumvention of U.S. export controls, significantly impacting AI hardware procurement in China and the global GPU supply chain. The RTX 5090 Turbo Edition is listed as a global un-crippled version, while the H100 was previously suspended for export to China due to sanctions.

telegram · zaihuapd · May 14, 15:15

**Background**: Since 2022, the U.S. government has imposed license requirements on exporting advanced NVIDIA GPUs like the H100 and A100 to China and Russia. The Blackwell architecture, featured in the RTX PRO 6000, is NVIDIA's latest GPU architecture designed for AI and data center workloads. JD.com's self-operated store directly sells hardware, contrasting with third-party listings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.3dstor.com/product-item-202.html">RTX 5090 Blower/Turbo,3DSTOR Technology Co. Ltd</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/AMD_Stock/comments/x2pedp/us_to_restrict_nvidia_from_exporting_its_a100_and/">r/AMD_Stock on Reddit: U.S. to restrict Nvidia from exporting its A100 and H100 server chips to China and Russia</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#NVIDIA`, `#sanctions`, `#JD.com`, `#GPU`

---