---
layout: default
title: "Horizon Summary: 2026-05-07 (ZH)"
date: 2026-05-07
lang: zh
---

> From 37 items, 14 important content pieces were selected

---

1. [Mozilla 借助 Claude Mythos 强化 Firefox 安全性](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.11：升级 CUDA 13 和 Torch 2.11，默认启用推测解码 V2](#item-2) ⭐️ 8.0/10
3. [AlphaEvolve：Gemini 驱动的编码代理跨领域扩大影响](#item-3) ⭐️ 8.0/10
4. [Chrome 移除本地 AI 隐私声明](#item-4) ⭐️ 8.0/10
5. [美国国会图书馆推荐 SQLite 用于数字保存](#item-5) ⭐️ 8.0/10
6. [AI 工具导致职场产出膨胀](#item-6) ⭐️ 8.0/10
7. [Valve 以 Creative Commons 许可发布 Steam 控制器 CAD 文件](#item-7) ⭐️ 8.0/10
8. [氛围编码与代理工程趋于融合](#item-8) ⭐️ 8.0/10
9. [Anthropic 与 SpaceX 合作获得海量 GPU 算力](#item-9) ⭐️ 8.0/10
10. [月之暗面融资超 70 亿美元，估值破 1000 亿，Kimi 收入激增](#item-10) ⭐️ 8.0/10
11. [苹果研发支出占比突破 10%，AI 投入加速硬件平台重塑](#item-11) ⭐️ 8.0/10
12. [腾讯 Hy3 preview 调用量超 Hy2 十倍，OpenRouter 周榜居首](#item-12) ⭐️ 8.0/10
13. [小米开源 OmniVoice：支持 646 语种的语音克隆 TTS](#item-13) ⭐️ 8.0/10
14. [英国 FCA 调查 PayPal、万事达、Visa 数字钱包合约](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mozilla 借助 Claude Mythos 强化 Firefox 安全性](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla 利用 Claude Mythos 预览版 AI 模型发现并修复了 Firefox 中的数百个安全漏洞，月度修复数量从 2025 年的约 20-30 个飙升至 2026 年 4 月的 423 个。 这一突破表明，先进的 LLM 现能显著增强软件安全加固能力，从生成低质量漏洞报告转变为发现高价值漏洞并通过维护者审查，可能改变 AI 辅助漏洞检测的格局。 该 AI 系统结合了更强的模型能力和改进的引导、扩展及堆叠技术，以产生有效信号并过滤噪声。许多尝试被 Firefox 的纵深防御措施拦截，表明模型的发现真实且精确。

rss · Simon Willison · May 7, 17:56

**背景**: Claude Mythos 是 Anthropic 于 2026 年发布的最新、最强大的语言模型，在计算机安全任务中表现卓越。传统 AI 生成的漏洞报告常因误报率高而被视为“垃圾”，但 Mythos 的高准确性改变了这一局面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Firefox`, `#vulnerability detection`, `#Claude Mythos`

---

<a id="item-2"></a>
## [SGLang v0.5.11：升级 CUDA 13 和 Torch 2.11，默认启用推测解码 V2](https://github.com/sgl-project/sglang/releases/tag/v0.5.11) ⭐️ 8.0/10

SGLang v0.5.11 升级至 CUDA 13.0 和 PyTorch 2.11，默认启用带重叠调度的推测解码 V2，并为预填充-解码分离新增了解码前缀缓存。同时新增了对 Gemma 4、Qwen3.6、Kimi-K2.6 等多个新模型的支持。 这些更新显著提升了 LLM 推理的性能和兼容性，使 SGLang 在生产部署中更具竞争力。默认的推测解码 V2 降低了 CPU 开销，而解码前缀缓存解决了分离部署中的一个关键限制，提升了吞吐量并减少了首 token 延迟。 推测解码 V2 使用重叠调度器来隐藏 CPU 开销，现已成为 EAGLE、MTP 和 DFLASH 路径的默认配置。解码前缀缓存恢复了预填充-解码分离下的前缀缓存命中率，从而为长共享前缀节省了首 token 时间。

github · Kangyan-Zhou · May 5, 21:28

**背景**: SGLang 是一个开源 LLM 推理框架，通过前缀缓存（RadixAttention）和推测解码等技术优化推理性能。预填充-解码分离将预填充和解码阶段分到不同进程，以更好地利用 GPU 资源，但此前会破坏前缀缓存；新的解码前缀缓存修复了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.sglang.io/docs/advanced_features/speculative_decoding">Speculative Decoding - SGLang Documentation</a></li>
<li><a href="https://bentoml.com/llm/inference-optimization/prefill-decode-disaggregation">Prefill-decode disaggregation | LLM Inference Handbook</a></li>
<li><a href="https://www.lmsys.org/blog/2024-12-04-sglang-v0-4/">SGLang v0.4: Zero-Overhead Batch Scheduler, Cache-Aware Load Balancer, Faster Structured Outputs - LMSYS Blog | LMSYS Org</a></li>

</ul>
</details>

**标签**: `#sglang`, `#LLM inference`, `#CUDA 13`, `#speculative decoding`, `#release`

---

<a id="item-3"></a>
## [AlphaEvolve：Gemini 驱动的编码代理跨领域扩大影响](https://deepmind.google/blog/alphaevolve-impact/) ⭐️ 8.0/10

DeepMind 发布了 AlphaEvolve，这是一个由 Gemini 大语言模型驱动的编码代理，能够设计先进算法并解决数学、计算机科学及其他领域的高级优化问题。 AlphaEvolve 展示了 AI 通过优化其运行的算法来自我改进的潜力，这可能加速科学发现和软件开发领域的进步。它也引发了关于基础模型如何在定义明确的高级优化任务中表现出色的讨论。 AlphaEvolve 将进化搜索方法与 Gemini 相结合，用于生成和改进算法，并在涵盖几何学、组合数学和数论的约 50 个精选数学问题上进行了基准测试。该系统侧重于高层次、定义明确的问题空间，而非低级编码。

hackernews · berlianta · May 7, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48050278)

**背景**: 编码代理是旨在通过自动化常规任务来帮助开发者编写、调试和优化代码的 AI 助手。AlphaEvolve 扩展了这一概念，利用像 Gemini 这样的 LLM 以进化方式探索解决方案空间，从而有效地进化出新算法。DeepMind 此前曾开发用于排序算法的 AlphaDev，而 AlphaEvolve 则代表了更广泛地应用于数学和科学问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaEvolve">AlphaEvolve - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/deepmind-unveils-alphaevolve-precision-ai-tool-solving-avinash-dubey-qblbc">DeepMind Unveils AlphaEvolve : A Precision AI Tool for Solving Math...</a></li>
<li><a href="https://github.com/resources/articles/what-are-ai-agents">What are AI agents ? · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者们反应不一：一些人强调了 AI 自我改进和快速进步的潜力，而另一些人则厌倦了反复听到相同的数学问题（如 Erdős 问题）被解决。还有人好奇谷歌工程师自己是否更喜欢 Gemini 而非 Claude Code 或 Codex 等替代品。

**标签**: `#AI`, `#coding agent`, `#DeepMind`, `#Gemini`, `#optimization`

---

<a id="item-4"></a>
## [Chrome 移除本地 AI 隐私声明](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/) ⭐️ 8.0/10

Google 从 Chrome 文档中移除了关于本地 AI 模型 Gemini Nano 不会向 Google 服务器发送数据的声明，引发了新的隐私担忧。 这一变化削弱了用户对 Chrome 隐私承诺的信任，尤其是考虑到 Gemini Nano 正通过 Chrome 更新积极部署到用户设备上。这可能意味着 Google 在本地 AI 数据处理方式上的转变。 被移除的声明是 Chrome 内置 AI API 文档的一部分，这些 API 使用 Gemini Nano 在本地执行翻译、摘要等任务。此前用户曾对未经明确许可下载的 4GB 'weights.bin' 文件表示担忧。

hackernews · newsoftheday · May 7, 15:56 · [社区讨论](https://news.ycombinator.com/item?id=48050964)

**背景**: Chrome 的本地 AI 功能依赖于 Gemini Nano，这是一个轻量级 AI 模型，旨在用户设备上本地运行，通过避免云端处理来提升隐私。Google 此前承诺该本地模型不会向服务器发送用户数据。移除这一承诺动摇了 Chrome AI 功能的隐私保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/google-chrome-weights-bin-ai-model-download-explained-3664043/">The truth behind Chrome 's 4GB 'weights.bin' Gemini Nano file</a></li>
<li><a href="https://developer.chrome.com/docs/ai/get-started">Get started with built-in AI | AI on Chrome | Chrome for Developers</a></li>
<li><a href="https://indianexpress.com/article/technology/tech-news-technology/google-chrome-downloads-4gb-gemini-ai-model-onto-your-devices-without-permission-report-10677956/">Google Chrome downloads 4GB Gemini AI model onto your devices ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 Google 的不信任，有人推荐 Brave 等更注重隐私的替代浏览器。其他人则质疑这对基于 Chromium 的浏览器的影响，指出 Brave 自家的 AI 'Leo' 也存在隐私问题。总体情绪充满怀疑，有用户表示‘我们不能信任 Google’。

**标签**: `#privacy`, `#google chrome`, `#on-device AI`, `#data collection`, `#trust`

---

<a id="item-5"></a>
## [美国国会图书馆推荐 SQLite 用于数字保存](https://sqlite.org/locrsf.html) ⭐️ 8.0/10

美国国会图书馆将 SQLite 正式列为数字保存的优选存储格式，作为其 2026 年推荐格式的一部分。 来自重要文化机构的认可验证了 SQLite 的可靠性和持久性，鼓励在档案和数据保存领域更广泛地采用。 该推荐出现在美国国会图书馆的 2026 年推荐存储格式页面上，列出了各种数据类型的优选格式。

hackernews · whatisabcdefgh · May 6, 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48042434)

**背景**: SQLite 是一个自包含、无服务器、零配置的 SQL 数据库引擎，广泛应用于嵌入式系统和应用程序。它将整个数据库存储为单一的跨平台文件，便于存档和保存。

**社区讨论**: 评论者对 SQLite 的简洁性和可靠性表示赞赏，但有些人指出在企业环境中存在潜在误用，即数据库文件可能被随意复制并包含敏感数据。一位评论者指出，国会图书馆的推荐可以追溯到 2018 年，因此这条新闻并不像看起来那么新。

**标签**: `#SQLite`, `#data storage`, `#digital preservation`, `#open source`, `#database`

---

<a id="item-6"></a>
## [AI 工具导致职场产出膨胀](https://nooneshappy.com/article/appearing-productive-in-the-workplace/) ⭐️ 8.0/10

这篇文章批评了 AI 工具如何导致职场中出现膨胀且肤浅的生产力产出，稀释了专家判断，并造成了一种冗长文化。 这削弱了职场沟通的真实性，并可能侵蚀真正的专业知识，尤其是在软件工程等领域，清晰简洁的沟通本应受到重视。 文章指出需求文档、状态更新等工作产出变得不必要的冗长，甚至专家也因依赖 AI 而产出看似反常的工作。

hackernews · diebillionaires · May 6, 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48038001)

**社区讨论**: 评论者强烈认同产出膨胀和专业知识稀释的观点。有评论分享了一位架构师使用 AI 过度设计系统的经历，另一评论指出 LLM 已自动化了讨好管理层的行为。

**标签**: `#AI`, `#workplace culture`, `#productivity`, `#software engineering`

---

<a id="item-7"></a>
## [Valve 以 Creative Commons 许可发布 Steam 控制器 CAD 文件](https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license) ⭐️ 8.0/10

Valve 已以 Creative Commons 许可发布了 Steam 控制器外壳和 Steam Controller Puck 的 CAD 文件，允许用户 3D 打印、修改和制作自定义配件。 这一开放硬件举措推动了改造、无障碍适配（例如针对残障玩家）和第三方配件的发展，减少了对专有部件的依赖，并促进了社区创新。 发布的文件包括 STP、STL 模型以及带有关键特征和禁止区域的工程图纸。该控制器近期重新发售但迅速售罄，黄牛以高价转卖。

hackernews · haunter · May 6, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48037555)

**背景**: Steam 控制器是 Valve 设计的游戏控制器，具有独特的触摸板和可自定义输入。CAD（计算机辅助设计）文件允许精确的 3D 打印修改。Creative Commons 许可允许在注明出处的情况下自由分享和改编。

**社区讨论**: 评论称赞了友好的 README 文件，并强调了该文件对需要自定义控制器的残障玩家的好处。有人对近期销售中的黄牛现象表示担忧，还有用户批评该控制器仅支持 Steam 的做法是走向封闭生态的一步。

**标签**: `#open hardware`, `#3d printing`, `#steam controller`, `#creative commons`, `#accessibility`

---

<a id="item-8"></a>
## [氛围编码与代理工程趋于融合](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything) ⭐️ 8.0/10

著名软件开发者 Simon Willison 在播客中描述，他此前对“氛围编码”与“代理工程”的清晰区分已开始模糊，因为他越来越依赖 AI 编码代理，甚至在生产系统中也不再逐行审阅代码。 这种融合挑战了 AI 在软件开发中的负责任使用，尤其是在服务他人的生产软件中，未经检查的 AI 生成代码可能引入安全漏洞和错误。 Willison 指出，对于像构建带 SQL 查询的 JSON API 端点这类简单重复任务，Claude Code 等代理能可靠地生成正确代码，导致他跳过审查并感到内疚。

rss · Simon Willison · May 6, 14:24 · [社区讨论](https://news.ycombinator.com/item?id=48037128)

**背景**: “氛围编码”由 Andrej Karpathy 于 2025 年 2 月提出，是一种 AI 辅助实践，开发者不经仔细审查就接受 AI 生成的代码。“代理工程”由 Willison 推广，指专业软件工程师使用 AI 代理提升代码质量和生产力，同时保持监督。这两种实践的模糊化引发了对生产环境中负责任使用 AI 边界的思考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://medium.com/@telumai/there-was-prompt-engineering-then-vibe-coding-now-agentic-engineering-7da779d1cb63">There Was Prompt Engineering Then Vibe Coding Now Agentic ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，AI 能力呈锯齿形前沿，对某些任务有效但对其他任务无效。他们认为氛围编码和 LLM 并非创造了不规范的实践，而是暴露并加速了已有的松散标准。还有评论警告，随着 AI 可靠性提高，其错误变得更细微且更难发现。

**标签**: `#AI coding tools`, `#vibe coding`, `#agentic engineering`, `#software engineering practices`, `#LLM`

---

<a id="item-9"></a>
## [Anthropic 与 SpaceX 合作获得海量 GPU 算力](https://www.anthropic.com/news/higher-limits-spacex) ⭐️ 8.0/10

Anthropic 宣布与 SpaceX 合作，使用 Colossus 1 数据中心的全部算力，一个月内可新增超过 300 兆瓦容量和 22 万块 NVIDIA GPU。即日起，Claude Code 所有付费方案的速率限制翻倍，Pro/Max 用户的高峰期限制取消，Claude Opus 的 API 速率限制也大幅提高。 此次合作大幅提升了 Anthropic 的算力，加速模型训练和推理，并通过更高的使用限制直接改善用户体验。它突显了大规模基础设施合作在竞争激烈的 AI 领域中的关键作用。 Colossus 1 是 xAI 位于田纳西州孟菲斯的数据中心，专为 AI 工作负载设计。该合作提供超过 300 兆瓦和 22 万块 GPU，Claude Code 的 5 小时速率限制翻倍，Pro/Max 用户的高峰期限制取消。

telegram · zaihuapd · May 6, 16:35

**背景**: Colossus 1 是 Elon Musk 旗下 xAI 公司建造的大型 AI 数据中心，配备了数十万块 NVIDIA GPU。Anthropic 开发 Claude 系列大语言模型，训练和推理需要海量计算资源。此次合作帮助 Anthropic 获得所需的算力以扩展服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.democracynow.org/2026/4/22/memphis_xai_data_center_pollution_keshaun">“ Colossus Failure”: Elon Musk’s Data Centers ... | Democracy Now!</a></li>
<li><a href="https://www.datacenterfrontier.com/machine-learning/article/55244139/the-colossus-ai-supercomputer-elon-musks-drive-toward-data-center-ai-technology-domination">datacenterfrontier.com/machine-learning/article/55244139/the...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SpaceX`, `#Claude`, `#GPU`, `#compute partnership`

---

<a id="item-10"></a>
## [月之暗面融资超 70 亿美元，估值破 1000 亿，Kimi 收入激增](https://t.me/zaihuapd/41251) ⭐️ 8.0/10

2 月 23 日，中国 AI 初创公司月之暗面完成新一轮超 7 亿美元融资，由阿里、腾讯等联合领投，估值突破 100 亿美元。其 Kimi 模型近 20 天累计收入已超 2025 年全年总额，且海外收入已超过国内。 这轮融资和收入里程碑凸显了中国 AI 初创公司在竞争激烈的大模型领域的快速成长和全球吸引力，可能重塑市场格局并吸引更多投资。 月之暗面累计融资额已超 12 亿美元，仅用两年多时间便成为国内晋级最快的“十角兽”企业。K2.5 模型在 OpenRouter 上推动了 API 调用量和付费用户的显著增长。

telegram · zaihuapd · May 7, 00:30

**背景**: 月之暗面是一家专注于大语言模型（LLM）的知名中国初创公司，以其 Kimi 系列闻名。该公司在快速发展的 AI 领域与百度、阿里巴巴等国内玩家竞争。“十角兽”指估值超过 100 亿美元的初创企业。

**标签**: `#AI startup`, `#fundraising`, `#LLM`, `#Chinese tech`, `#valuation`

---

<a id="item-11"></a>
## [苹果研发支出占比突破 10%，AI 投入加速硬件平台重塑](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) ⭐️ 8.0/10

苹果 2026 年 3 月财季研发支出占营收比例升至 10.3%，为 30 年来首超 10%，主要由加速的 AI 投资驱动。 这一历史性的研发支出增长标志着苹果向 AI 的迫切转型，可能重塑其硬件生态和后 iPhone 时代的竞争地位。 尽管营收增长 17%，但研发投入飙升 34%，重点集中在端侧 AI、自研芯片和私有云计算，以及 AI 眼镜和带摄像头的 AirPods 等产品。

telegram · zaihuapd · May 7, 01:00

**背景**: 研发支出占营收的比例是衡量公司未来创新投入的关键指标。苹果历史上一直将这一比例保持在 10%以下，但随着 AI 竞赛加剧，公司正进行战略转向，将 AI 深度整合进硬件中。

**标签**: `#Apple`, `#AI`, `#R&D`, `#Hardware`, `#Strategy`

---

<a id="item-12"></a>
## [腾讯 Hy3 preview 调用量超 Hy2 十倍，OpenRouter 周榜居首](https://finance.sina.com.cn/tech/shenji/2026-05-07/doc-inhwzrtp8521239.shtml) ⭐️ 8.0/10

腾讯 Hy3 preview 模型上线仅两周，Token 调用量已达上一代 Hy2 模型的 10 倍以上，并在 OpenRouter 周榜的总榜和市场占有率上双双登顶。 这一快速普及表明 Hy3 preview 在性能和效率上的强劲表现，得到了 OpenRouter 开放社区的验证，并使腾讯在大语言模型领域成为一股有竞争力的力量，特别是在智能体与编程场景中。 Hy3 preview 是一个 295B 参数的混合专家（MoE）模型，仅有 21B 活跃参数，支持最高 256K 上下文长度，使其在生产使用中非常高效。在腾讯内部的 WorkBuddy、Codebuddy 等应用中，代码与智能体场景的 Token 处理量增长超过 16.5 倍。

telegram · zaihuapd · May 7, 05:34

**背景**: Hy3 preview 是腾讯在重建的基础设施上训练的首个模型，专为智能体工作流和长程推理设计。OpenRouter 是一个统一的 API 平台，通过单一接口为开发者提供 300 多种 AI 模型的访问，其周榜反映了来自数千个应用的真实使用模式。混合专家（MoE）是一种神经网络架构，每个 Token 仅激活部分参数，从而以较低的算力成本实现高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy3-preview">tencent / Hy 3 - preview · Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy3-preview:free">Hy 3 preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tencent`, `#large language model`, `#model performance`, `#technology`

---

<a id="item-13"></a>
## [小米开源 OmniVoice：支持 646 语种的语音克隆 TTS](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 8.0/10

小米开源了 OmniVoice，一个大规模多语言语音克隆 TTS 模型，采用极简双向 Transformer 架构，支持 646 种语言。 这一开源发布使高质量多语言 TTS 和语音克隆技术更加普及，在 24 语种测试中超越商用系统，并具备强大的零样本跨语言克隆能力。 OmniVoice 基于 50 个开源数据集构建了 58 万小时的训练数据，在 PyTorch 上推理速度可达 40 倍实时，其权重、训练和推理代码均已开源。

telegram · zaihuapd · May 7, 10:06

**背景**: TTS（文本转语音）系统将文本转换为语音音频。语音克隆 TTS 能够仅凭几秒参考音频模仿特定说话人的声音。OmniVoice 极致的多语言能力（646 种语言）和零样本克隆使其备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://omnivoice.app/">OmniVoice : Free AI Voice Generator & Voice Cloning</a></li>
<li><a href="https://huggingface.co/k2-fsa/OmniVoice">k2-fsa/ OmniVoice · Hugging Face</a></li>

</ul>
</details>

**标签**: `#TTS`, `#voice cloning`, `#open source`, `#multilingual`, `#xiaomi`

---

<a id="item-14"></a>
## [英国 FCA 调查 PayPal、万事达、Visa 数字钱包合约](https://www.fca.org.uk/news/press-releases/competition-act-1998-investigations) ⭐️ 8.0/10

英国金融行为监管局（FCA）对 PayPal、万事达和 Visa 启动反竞争调查，重点关注 PayPal 数字钱包相关的合同条款。FCA 尚未就是否违反竞争法得出结论。 这项调查可能重塑英国数字钱包市场格局，该市场交易占比在过去一年从 8%跃升至 29%。它可能影响竞争、创新和新进入者的市场准入。 调查特别针对可能限制竞争的合同条款。三家公司均表示将配合 FCA 的调查。

telegram · zaihuapd · May 7, 14:46

**背景**: 数字钱包允许用户在移动设备上存储支付卡信息并进行非接触式支付。英国数字钱包市场增长迅速，其交易占比从 2023 年的 8%跃升至当前的 29%。FCA 正在调查某些合同条款是否阻碍了数字钱包提供商之间的竞争。

**标签**: `#反垄断`, `#数字钱包`, `#支付监管`, `#金融科技`, `#英国FCA`

---