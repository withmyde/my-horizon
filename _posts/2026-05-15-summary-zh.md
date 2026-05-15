---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 31 items, 13 important content pieces were selected

---

1. [Bun 将 Zig 重写为 Rust 的代码已合并](#item-1) ⭐️ 10.0/10
2. [vLLM v0.21.0 发布：重大变更与新功能](#item-2) ⭐️ 9.0/10
3. [Apple M5 首个公开 macOS 内核漏洞](#item-3) ⭐️ 9.0/10
4. [NGINX 曝出潜伏 18 年的严重远程代码执行漏洞](#item-4) ⭐️ 9.0/10
5. [DeepSeek 会话隔离漏洞：未闭合<think 字符串泄露对话](#item-5) ⭐️ 9.0/10
6. [从 2024 款丰田 RAV4 混动车中移除调制解调器和 GPS](#item-6) ⭐️ 8.0/10
7. [antirez 发布 DwarfStar4，可在本地运行 DeepSeek 4](#item-7) ⭐️ 8.0/10
8. [RTX 5090 eGPU 搭配 M4 MacBook Air：游戏与 LLM](#item-8) ⭐️ 8.0/10
9. [Codex 免费集成到 ChatGPT 移动应用](#item-9) ⭐️ 8.0/10
10. [arXiv 禁止虚构参考文献，违规者面临一年提交禁令](#item-10) ⭐️ 8.0/10
11. [美国批准英伟达 H200 对华销售，英伟达寻求突破](#item-11) ⭐️ 8.0/10
12. [全球肥胖趋势因收入水平而分化](#item-12) ⭐️ 8.0/10
13. [京东上架受制裁的 NVIDIA AI GPU](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun 将 Zig 重写为 Rust 的代码已合并](https://github.com/oven-sh/bun/pull/30412) ⭐️ 10.0/10

作为 JavaScript 运行时的 Bun 已合并一个拉取请求，将其核心从 Zig 重写为 Rust，新增了超过 100 万行 Rust 代码。 从 Zig 转向 Rust 是一项重大的架构变更，对于广泛使用的运行时而言，有可能提高内存安全性并减少像使用后释放这样的 bug。 根据合并提交，新的 Rust 代码库包含超过 100 万行代码，社区分析指出有 10,428 次 `unsafe` 使用，分布在 736 个文件中。

hackernews · Chaoses · May 14, 08:15 · [社区讨论](https://news.ycombinator.com/item?id=48132488)

**背景**: Bun 是一个以速度见长的 JavaScript 运行时和工具包，最初用 Zig 语言编写。Zig 是一种系统编程语言，与 C 竞争，提供编译时特性和手动内存管理。改用 Rust（具有更强的安全性保证）是一次重大的代码库迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://grokipedia.com/page/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区回应强调了明确的准备，包括映射文件和智能指针类型（sesm），并担忧 Bun 的代码量已接近 Rust 编译器，复杂度管理成疑（vitaminCPP）。Jarred 指出 Rust 能捕获许多内存 bug，但并非全部，尤其是跨越 JavaScript 边界的那些。

**标签**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-2"></a>
## [vLLM v0.21.0 发布：重大变更与新功能](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 引入了重大变更，包括弃用 Transformers v4 和新的 C++20 构建要求，同时推出了多项新功能，如基于混合内存分配器的 KV 卸载、支持思考预算的推测解码，以及针对 Blackwell GPU 的 TOKENSPEED_MLA 后端。 此次发布对 vLLM 社区影响重大，用户必须迁移到 Transformers v5 并升级构建工具，同时获得显著的性能和内存效率提升，从而能够部署更大的模型并在现代硬件上实现更快的推理。 该版本包含来自 202 位贡献者的 367 次提交，支持新的模型架构（如 MiMo-V2.5、Moondream3、Cohere MoE），并增强了推测解码、KV 卸载和引擎核心的稳定性。

github · khluu · May 14, 23:15

**背景**: KV 缓存卸载是一种通过将键值缓存数据移至 CPU 或 NVMe 存储来减少 GPU 内存使用的技术，从而支持更长的上下文或更大的批处理。vLLM 的混合内存分配器高效管理异构内存池。推测解码利用较小的草稿模型加速生成，而思考预算则限制推理步骤以提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bentoml.com/llm/inference-optimization/kv-cache-offloading">KV cache offloading | LLM Inference Handbook</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm -project/ vllm</a></li>
<li><a href="https://lmstudio.ai/docs/app/advanced/speculative-decoding">Speculative Decoding | LM Studio</a></li>

</ul>
</details>

**标签**: `#vllm`, `#release`, `#LLM inference`, `#breaking change`, `#AI/ML`

---

<a id="item-3"></a>
## [Apple M5 首个公开 macOS 内核漏洞](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

一个安全研究团队公开披露了首个针对 Apple M5 芯片的内核内存破坏漏洞，绕过了 MTE（内存标记扩展）等硬件内存保护机制。 这标志着重要的安全里程碑，表明即使是配备先进内存保护的 Apple M5 芯片也容易受到内核级攻击，可能影响 macOS 安全态势和漏洞赏金估值。 该漏洞据报道绕过了 MTE，并提供了一份详细的 55 页报告。一些社区成员指出，根据打包方式，该漏洞在 Apple 的漏洞赏金计划中可能价值 10 万至 150 万美元。

hackernews · quadrige · May 14, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48139219)

**背景**: Apple M5 是 Apple 硅系列中最新基于 ARM 的片上系统，具备统一内存和内存标记扩展 (MTE) 等硬件安全特性，用于检测内存破坏。内核内存破坏是一种关键漏洞类别，允许攻击者完全控制操作系统。此前，针对 Apple M 系列芯片的公开漏洞非常罕见，因此这次披露引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5 - Calif</a></li>
<li><a href="https://news.ycombinator.com/item?id=48139219">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人称赞这一技术成就，称其为重要的安全里程碑，而另一些人则指出缺乏细节，并质疑漏洞如何绕过 MTE。还有关于潜在漏洞赏金估值的讨论，估计在 10 万至 150 万美元之间。少数用户表示怀疑，认为该漏洞可能被过度炒作。

**标签**: `#security`, `#macOS`, `#kernel exploit`, `#Apple M5`, `#vulnerability`

---

<a id="item-4"></a>
## [NGINX 曝出潜伏 18 年的严重远程代码执行漏洞](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability) ⭐️ 9.0/10

安全研究人员披露了 CVE-2026-42945，这是一个存在于 NGINX rewrite 模块中的严重堆缓冲区溢出漏洞，影响从 0.6.27 到 1.30.0 的所有版本，可导致未经身份验证的远程代码执行。 该漏洞的 CVSS v4.0 评分为 9.2，影响全球数十亿台服务器，包括 NGINX Open Source、NGINX Plus 以及多个企业级产品，带来了巨大的安全风险。 该漏洞源于脚本引擎两遍执行流程中的不一致：第一遍计算缓冲区长度时未考虑字符转义，第二遍复制数据时扩展特殊字符（如 '?' 变为 %3F），导致堆溢出。

telegram · zaihuapd · May 14, 02:41

**背景**: NGINX 是一种广泛使用的 Web 服务器和反向代理，常部署在 Kubernetes 环境中的入口控制器。ngx_http_rewrite_module 使用两遍执行的脚本引擎处理 rewrite 指令。当长度计算遍由于 URI 编码扩展而低估最终缓冲区大小时，就会发生堆缓冲区溢出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via an 18-Year-Old ...</a></li>
<li><a href="https://github.com/nginx/nginx/blob/master/src/http/modules/ngx_http_rewrite_module.c">nginx/src/http/modules/ngx_http_rewrite_module.c at master · nginx/nginx</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，虽然已发布的 PoC 假设 ASLR 已禁用，但研究人员声称有可靠的方法绕过 ASLR。一些用户注意到该漏洞利用需要特定的 rewrite 配置（替换字符串中带问号的未命名捕获组）。还有人讨论了寻找 Apache 和 NGINX 的内存安全替代方案的困难。

**标签**: `#nginx`, `#security`, `#vulnerability`, `#rce`, `#cve`

---

<a id="item-5"></a>
## [DeepSeek 会话隔离漏洞：未闭合<think 字符串泄露对话](https://github.com/deepseek-ai/DeepSeek-R1/issues/840) ⭐️ 9.0/10

DeepSeek 对话系统中发现了一个会话隔离漏洞：在新空白对话中发送未闭合的“<think”字符串，可能导致模型返回其他用户的对话片段，从而泄露敏感数据。该漏洞由用户 cancat2024 于 2026 年 5 月 11 日负责任地披露。 该漏洞构成了严重的安全风险，可能暴露其他用户的私有对话数据，包括代码、密钥和个人信息。它突显了 AI 聊天机器人在会话隔离机制上的重大缺陷，对企业和消费者的部署尤为令人担忧。 攻击方式是在新对话中仅输入未闭合的“<think”标记，触发模型产生幻觉并输出其他会话的内容。该问题已确认影响 DeepSeek Web 和 API，并且据报告也在第三方部署中出现，表明这可能是一种固有的幻觉行为。

telegram · zaihuapd · May 14, 13:15

**背景**: 会话隔离是多用户 AI 聊天机器人的基本安全要求，确保每个用户的对话上下文保持独立。像“<think>”这样的特殊标记被一些模型用来指示推理步骤，但当未闭合时，模型可能会误解提示并泄露跨会话数据。该漏洞是一种利用模型模式完成倾向的提示注入形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://successquarterly.com/deepseek-data-breach-highlights-ai-industrys-security-vulnerabilities/">DeepSeek Data Breach Highlights AI Industry's Security Vulnerabilities</a></li>
<li><a href="https://injectiqa.com/blog/prompt-inject-enterprise-deepseek">Prompt Injection in the Enterprise: Dissecting the DeepSeek ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，同样的漏洞也在第三方部署中出现，表明这是一种幻觉现象而非服务器端数据混淆。报告者以负责任态度披露，未利用该漏洞收集数据。

**标签**: `#security`, `#vulnerability`, `#DeepSeek`, `#data-leakage`, `#AI`

---

<a id="item-6"></a>
## [从 2024 款丰田 RAV4 混动车中移除调制解调器和 GPS](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

一份详细的技术指南已经发布，展示了如何从 2024 款丰田 RAV4 混动车中物理移除远程信息处理控制模块和 GPS 天线，以阻止车辆数据收集。 该指南回应了日益增长的关于汽车遥测数据与保险公司及第三方共享的隐私担忧，并赋予车主无需软件破解即可重新掌控数据的能力。 移除过程包括断开手套箱后的远程信息处理控制单元以及拆下仪表盘内的 GPS 天线，且不会触发任何仪表盘警告灯。

hackernews · arkadiyt · May 14, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=48138136)

**背景**: 现代网联汽车通过内置蜂窝调制解调器收集并传输位置、速度和驾驶行为等数据。这些数据常常在未获得明确同意的情况下与第三方共享，引发了严重的隐私问题。该指南为反对遥测的人提供了一种基于硬件的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid</a></li>
<li><a href="https://news.ycombinator.com/item?id=48138136">Removing the modem and GPS from my 2024 RAV4 hybrid - Hacker News</a></li>
<li><a href="https://www.reddit.com/r/cars/comments/1td7mi2/removing_the_modem_and_gps_from_my_2024_rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid : r/cars - Reddit</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了分歧：一些用户赞赏隐私关注和技术细节，而另一些用户则认为禁用连接会抵消 OTA 更新等现代功能的好处。少数评论者分享了其他车型上移除特定保险丝等替代方案。

**标签**: `#privacy`, `#telematics`, `#car hacking`, `#DIY`, `#Toyota`

---

<a id="item-7"></a>
## [antirez 发布 DwarfStar4，可在本地运行 DeepSeek 4](https://antirez.com/news/165) ⭐️ 8.0/10

Redis 创始人 antirez 宣布了 DwarfStar4（DS4），这是一个小型 LLM 推理运行时，能够在拥有 96GB VRAM 的硬件上本地运行 DeepSeek 4，性能接近 Claude。 这标志着本地模型部署的重大进展，使得像 DeepSeek 4 这样强大的开源模型能够在消费级硬件上运行，可能减少对云端 API 的依赖并提升隐私性。 DwarfStar4 目前需要 96GB VRAM，主要后端为 Metal（macOS），同时支持 NVIDIA CUDA 和 AMD ROCm（ROCm 由社区单独维护）。该项目基于 llama.cpp 和 GGML。

hackernews · caust1c · May 14, 22:29 · [社区讨论](https://news.ycombinator.com/item?id=48142108)

**背景**: LLM 推理运行时是允许大型语言模型在硬件上高效执行的软件栈。DeepSeek 4 是一个强大的开源大语言模型。本地推理可以实现离线使用和数据隐私，但由于模型规模较大，通常需要高端 GPU。DwarfStar4 是一个为此优化的轻量级运行时。

**社区讨论**: 评论者指出，DS4 在质量上非常接近 Claude，虽然速度较慢，并且观察到模型具有自我意识（例如识别自己的服务器进程）。他们还讨论了本地模型在几年内接近或匹敌云端能力的潜力。

**标签**: `#LLM`, `#inference`, `#local models`, `#DeepSeek`, `#AI runtime`

---

<a id="item-8"></a>
## [RTX 5090 eGPU 搭配 M4 MacBook Air：游戏与 LLM](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

作者成功通过 Thunderbolt eGPU 扩展坞将 NVIDIA RTX 5090 连接到 M4 MacBook Air，利用 GPU 直通实现了 Windows 游戏，并显著提升了 LLM 的提示处理速度。 这表明 eGPU 在 Apple Silicon 上对特定工作负载仍然可行，为需要高端图形性能进行游戏或 AI 推理的 Mac 用户提供了一座桥梁，无需转而使用 PC。 这一设置克服了 macOS 对 OpenGL 支持不佳以及缺乏原生 GPU 直通的问题，但需要付出大量努力；LLM 基准测试显示，与 M4 内置 GPU 相比，RTX 5090 的提示处理速度提高了一倍以上。

hackernews · allenleee · May 14, 15:47 · [社区讨论](https://news.ycombinator.com/item?id=48137145)

**背景**: eGPU（外部 GPU）通过 Thunderbolt 将台式机显卡连接到笔记本电脑，以提升图形性能。LLM 推理涉及运行大型语言模型；提示处理（预填充）是一个内存带宽密集型步骤，在 Mac 上由于统一内存带宽限制通常较慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biztechmagazine.com/article/2022/08/what-external-graphics-processing-unit-perfcon">What Is an External Graphics Processing Unit (eGPU) and How Does it Boost Performance?</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/external-gpu/">What is an external graphics processing unit (GPU)?</a></li>
<li><a href="https://www.computerhope.com/jargon/e/egpu.htm">What Is an eGPU (External Graphics Processing Unit)?</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章的技术深度，其中一人指出 LLM 性能提升是最实用的收获。另一人提到讽刺的是，《毁灭战士》（2016）在 Mac 上需要这种设置才能运行，其他人则讨论了 GPU 直通挑战和 AI 模型的局限性。

**标签**: `#eGPU`, `#MacBook Air`, `#RTX 5090`, `#gaming`, `#LLM`

---

<a id="item-9"></a>
## [Codex 免费集成到 ChatGPT 移动应用](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 8.0/10

OpenAI 已将 Codex AI 编程助手集成到 ChatGPT 移动应用中，并向免费用户开放。开发人员可以直接通过智能手机使用自然语言提示编写和编辑代码。 这一集成降低了 AI 辅助编程的门槛，开发者无需台式机或付费订阅即可随时随地编写代码。它可能加速移动优先的开发工作流程，使编程辅助更加普及。 Codex 作为专用功能位于 ChatGPT 移动应用的侧边栏中，用户使用 ChatGPT 账户登录即可使用。社区指出，免费层的交互可能用于模型训练。

hackernews · mikeevans · May 14, 20:06 · [社区讨论](https://news.ycombinator.com/item?id=48140529)

**背景**: OpenAI Codex 是一系列针对源代码微调的大型语言模型，旨在将自然语言转换为代码。它最初于 2021 年推出，现已发展出语言模型和 AI 代理产品。将其集成到 ChatGPT 移动应用扩展了其可访问性，不再局限于桌面和命令行界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://developers.openai.com/codex/models">Models – Codex | OpenAI Developers</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Codex 免费开放感到兴奋，部分用户称其为期待已久的功能。但也有人担心移动端用户体验的限制，例如屏幕太小导致对代理的引导效果不佳，并希望支持远程 Linux 机器的 CLI。

**标签**: `#Codex`, `#ChatGPT mobile`, `#OpenAI`, `#AI coding assistant`, `#developer tools`

---

<a id="item-10"></a>
## [arXiv 禁止虚构参考文献，违规者面临一年提交禁令](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 推出了一项新政策，对提交含有虚构参考文献的论文的作者实行一年禁令，并要求其后续提交必须先经过知名同行评审机构的接收才能发布在 arXiv 上。 该政策直接回应了学术界日益严重的 LLM 滥用问题，虚构引用损害了研究的完整性并浪费审稿人的时间。它为其他预印本服务器和出版商树立了强有力的榜样。 该禁令适用于含有虚构参考文献的提交，禁令结束后，作者必须将论文被知名同行评审机构接收后才能重新提交到 arXiv。该政策尚未在 arXiv 网站上详细公布，但已宣布。

hackernews · gjuggler · May 14, 20:39 · [社区讨论](https://news.ycombinator.com/item?id=48140922)

**背景**: 虚构参考文献是由大型语言模型（LLM）生成的虚假引用，看似合理但实际上并不存在。这一问题在学术论文中日益严重，因为像 ChatGPT 这样的 LLM 可以编造出能够通过 AI 检测工具并误导读者的参考文献。arXiv 是一个广泛使用的预印本存储库，允许研究人员在正式同行评审之前分享论文的早期版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ref-check.org/">ref-check.org — Academic Reference Verification Tool</a></li>
<li><a href="https://arxiv.org/pdf/2604.16407">26-19 How unique are hallucinated citations 2026-03-31</a></li>
<li><a href="https://writemask.com/blog/aigenerated-detect-or-detection-or-detector-or-text-or-literature-or-references-or-manuscript-or-academic-or-hallucination-or-paper-or-article">AI Hallucinations in Academic Papers : 7 Problems No... — WriteMask</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体上是正面的，如用户 rgmerk 称赞此举对于质量控制是必要的。一些评论者提醒在实施禁令前需要仔细审查，而另一些人则指出 LLM 爱好者对此限制感到愤怒，凸显了对于 AI 生成内容态度的分歧。

**标签**: `#arXiv`, `#academic publishing`, `#LLM misuse`, `#policy`, `#research integrity`

---

<a id="item-11"></a>
## [美国批准英伟达 H200 对华销售，英伟达寻求突破](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) ⭐️ 8.0/10

美国商务部已批准约 10 家中国企业购买英伟达 H200 芯片，买家包括阿里巴巴、腾讯、字节跳动和京东等，联想和富士康等分销商也获得许可，但截至目前尚未有交付完成。 这一进展标志着美中科技紧张局势可能出现转变，允许高端 AI 芯片流入中国企业，影响全球 AI 硬件供应链以及中国推进 AI 模型的能力。 H200 GPU 配备 141 GB 的 HBM3e 内存，带宽达 4.8 TB/s，容量几乎是 H100 的两倍，专为大型语言模型和长上下文工作负载设计；单一客户最多可购买 7.5 万颗。

telegram · zaihuapd · May 14, 08:57

**背景**: 美国以国家安全为由对向中国出口先进 AI 芯片实施了管制。H200 基于英伟达 Hopper 架构，是目前最强大的 AI 加速器之一。在限制下，中国企业一直在寻求替代方案，但国产芯片仍落后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/h200/">H200 GPU | NVIDIA</a></li>
<li><a href="https://www.runpod.io/articles/guides/nvidia-h200-gpu">Nvidia H200 GPU: Specs, VRAM, Price, and AI Performance</a></li>
<li><a href="https://lenovopress.lenovo.com/lp1944-nvidia-h200-141gb-gpu">ThinkSystem NVIDIA H200 141GB GPUs Product Guide > Lenovo Press</a></li>

</ul>
</details>

**标签**: `#chips`, `#AI hardware`, `#US-China`, `#Nvidia`, `#trade policy`

---

<a id="item-12"></a>
## [全球肥胖趋势因收入水平而分化](https://www.nature.com/articles/s41586-026-10383-0) ⭐️ 8.0/10

一项覆盖 200 个国家、2.32 亿人的研究发现，高收入国家的肥胖率自 2000 年代起趋于稳定，而中低收入国家的肥胖率仍在持续上升，部分低收入国家的肥胖率甚至已超过高收入国家。 这一肥胖趋势的转变表明，高收入国家的公共卫生干预措施可能有效，但也凸显了发展中国家迫切需要采取政策行动来应对日益严重的肥胖流行。 该研究分析了 1980 年至 2024 年的数据，指出高收入国家的儿童青少年肥胖率自 1990 年代起增速放缓，意大利、葡萄牙和法国等国家甚至出现了小幅下降。

telegram · zaihuapd · May 14, 09:45

**背景**: 肥胖是一个主要的全球健康问题，与糖尿病和心血管疾病等慢性病相关。这项大规模流行病学研究提供了四十年间 200 个国家肥胖趋势的最全面图景，突显了经济发展如何影响营养转型。

**标签**: `#public health`, `#obesity`, `#epidemiology`, `#global health`, `#nutrition`

---

<a id="item-13"></a>
## [京东上架受制裁的 NVIDIA AI GPU](https://u.jd.com/HaDkFMa) ⭐️ 8.0/10

京东开设了“AI 硬件京东自营专区”，上架了此前受制裁的 NVIDIA GPU，包括 RTX 5090 32G 涡轮版、RTX PRO 6000 Blackwell 服务器版和 H100。 此举可能标志着对美国出口管制的潜在规避，将显著影响中国的 AI 硬件采购及全球 GPU 供应链。 RTX 5090 涡轮版被列为无阉割的全球统一规格版本，而 H100 此前因制裁暂停对华出口。

telegram · zaihuapd · May 14, 15:15

**背景**: 自 2022 年起，美国政府要求对向中国和俄罗斯出口先进 NVIDIA GPU（如 H100 和 A100）需获得许可证。RTX PRO 6000 采用的 Blackwell 架构是 NVIDIA 专为 AI 和数据中心工作负载设计的最新 GPU 架构。京东自营专区直接销售硬件，与第三方商家列表不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.3dstor.com/product-item-202.html">RTX 5090 Blower/Turbo,3DSTOR Technology Co. Ltd</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/AMD_Stock/comments/x2pedp/us_to_restrict_nvidia_from_exporting_its_a100_and/">r/AMD_Stock on Reddit: U.S. to restrict Nvidia from exporting its A100 and H100 server chips to China and Russia</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#NVIDIA`, `#sanctions`, `#JD.com`, `#GPU`

---