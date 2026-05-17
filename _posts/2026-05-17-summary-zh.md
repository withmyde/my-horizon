---
layout: default
title: "Horizon Summary: 2026-05-17 (ZH)"
date: 2026-05-17
lang: zh
---

> From 23 items, 7 important content pieces were selected

---

1. [sglang v0.5.12 完整支持 DeepSeek V4 推理](#item-1) ⭐️ 9.0/10
2. [Julia Evans 离开 Tailwind CSS](#item-2) ⭐️ 8.0/10
3. [《加速》：2005 年小说精准预测 AI 代理与技术奇点](#item-3) ⭐️ 8.0/10
4. [δ-mem：大语言模型的高效在线记忆机制](#item-4) ⭐️ 8.0/10
5. [Google 将 AI 搜索操纵列入垃圾内容政策](#item-5) ⭐️ 8.0/10
6. [OpenAI 与马耳他合作，向全体公民免费提供 ChatGPT Plus](#item-6) ⭐️ 8.0/10
7. [GitHub Copilot 桌面应用进入技术预览](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [sglang v0.5.12 完整支持 DeepSeek V4 推理](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 9.0/10

Sglang v0.5.12 版本提供了对 DeepSeek V4 的完整推理支持，包括张量并行、专家并行和上下文并行、解耦的预填充-解码过程，以及优化的 DeepGemm 和 FlashMLA 内核。此外，还增加了针对 Blackwell GPU 的 TokenSpeed MLA 注意力后端，并支持 Intern-S2-Preview 和 Gemma 4 等新模型。 此次发布意义重大，因为它通过先进的并行技术和内核优化，实现了对大型 MoE 模型 DeepSeek V4 的高效服务，降低了延迟并提高了吞吐量。这巩固了 sglang 作为生产环境中领先的开源 LLM 推理框架的地位。 关键技术细节包括针对 MegaMoE 的 W4A4 和 W4A8 量化内核、带有 UnifiedRadixTree 的 HiCache KV 缓存卸载功能，以及支持 EAGLE-3 的推测解码 V2 成熟版本。该版本还将 DeepEP 迁移至 CUDA 13，并提供了适用于所有 Nvidia GPU 的统一 Docker 镜像。

github · Fridge003 · May 16, 18:23

**背景**: 像 DeepSeek V4 这样的大型语言模型需要高效的推理服务来处理高流量。张量并行将模型层拆分到多个 GPU 上，专家并行分配 MoE 专家，而解耦的预填充-解码则将提示处理与令牌生成分离，以提高 GPU 利用率。Sglang 是一个开源框架，为此类模型提供优化的内核和服务能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.perplexity.ai/hub/blog/disaggregated-prefill-and-decode">Disaggregated Prefill and Decode</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/disagg_prefill/">Disaggregated Prefilling (experimental) - vLLM</a></li>

</ul>
</details>

**标签**: `#sglang`, `#DeepSeek`, `#LLM inference`, `#GPU optimization`, `#open-source tools`

---

<a id="item-2"></a>
## [Julia Evans 离开 Tailwind CSS](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/) ⭐️ 8.0/10

知名开发者与教育者 Julia Evans 发布博文，详述她放弃 Tailwind CSS 并转向结构化、语义化 CSS 方法的决定，并分享了她的学习历程和转型原因。 该博文引发了关于 CSS 方法论、实用优先与语义化 CSS 以及前端最佳实践的广泛讨论。鉴于 Evans 的影响力，这场讨论可能促使许多开发者重新审视自己的 CSS 方案。 Evans 的博文明确讨论了离开 Tailwind 并学习结构化 CSS 的过程，提及了 BEM 和 CSS Modules 等方法论。该文在 Hacker News 上获得超过 400 分和 284 条评论，社区参与度极高。

hackernews · mpweiher · May 16, 09:14 · [社区讨论](https://news.ycombinator.com/item?id=48158400)

**背景**: Tailwind CSS 是一种实用优先的 CSS 框架，通过小型、单一用途的类直接为元素添加样式，而传统 CSS 的类名通常描述内容的语义角色。BEM（块元素修饰符）等方法提供了命名约定，以可维护的方式组织 CSS。实用优先与语义化 CSS 之间的权衡是 Web 开发中一个长期的争论话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://heydonworks.com/article/what-is-utility-first-css/">What is Utility-First CSS?: HeydonWorks</a></li>
<li><a href="https://getbem.com/">BEM — Block Element Modifier</a></li>
<li><a href="https://dev.to/michi/utility-first-css-you-have-to-try-it-first-3m85">Utility-first CSS - You have to try it first! - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论呈现两极分化：有人认为 Tailwind 颠倒了 HTML 语义的自然顺序，也有人称赞其实用性。部分用户推荐 CSS Modules 作为 Tailwind 的更简单替代方案，还有评论批评 Tailwind 推广者缺乏深入的 CSS 知识。

**标签**: `#CSS`, `#Tailwind CSS`, `#Web Development`, `#Frontend`, `#Semantic HTML`

---

<a id="item-3"></a>
## [《加速》：2005 年小说精准预测 AI 代理与技术奇点](https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html) ⭐️ 8.0/10

Hacker News 上的讨论指出，查理·斯特罗斯 2005 年的小说《加速》准确预测了现代 AI 代理、神经网络和技术奇点，读者认为它与当前发展惊人地相关。 这部小说的先见之明表明科幻作品能够预见真实的技术发展轨迹，而讨论也凸显了公众对 AI 快速进步及其社会影响日益增强的认识。 小说中主角依赖眼镜中运行的 AI 代理执行任务，并包含十亿节点神经网络和递归自我改进等概念，评论者将其与当今的 AI 助手和大语言模型联系起来。

hackernews · eamag · May 16, 11:36 · [社区讨论](https://news.ycombinator.com/item?id=48159241)

**背景**: 技术奇点是一个假设性的未来节点，人工智能超级智能引发失控的技术增长，导致不可预测的变化。《加速》通过一系列相互关联的短篇故事探讨了这一概念，追踪一个家庭穿越奇点的历程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technological_singularity">Technological singularity</a></li>
<li><a href="https://aiworldjournal.substack.com/p/accelerando-the-ai-prophecy-hidden-e8c">Accelerando: The AI Prophecy Hidden in Charles Stross's Sci-Fi Masterpiece</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞小说的预测能力，指出其对 AI 代理和神经网络的描绘与当前技术相吻合。有人觉得它准确得'可怕'，也有人推荐它和《量子窃贼》一起作为最合理的未来怪异景象的典范。

**标签**: `#science-fiction`, `#AI-agents`, `#technology-predictions`, `#singularity`, `#Charlie-Stross`

---

<a id="item-4"></a>
## [δ-mem：大语言模型的高效在线记忆机制](https://arxiv.org/abs/2605.12357) ⭐️ 8.0/10

一篇新论文提出了δ-mem，这是一种利用 delta 规则学习将过往信息压缩为固定大小状态矩阵的记忆机制，为大语言模型实现了高效的在线记忆。 这种方法可以使大语言模型在内存使用不线性增长的情况下，拥有近乎无限的上下文能力，这对于需要跨会话保留历史记录的长期运行的智能体和助手至关重要。 δ-mem 通过一个紧凑的联想记忆状态增强冻结的注意力主干，该状态为注意力计算提供低秩修正，并利用 delta 规则学习在每个新 token 到来时更新该状态。

hackernews · 44za12 · May 16, 09:30 · [社区讨论](https://news.ycombinator.com/item?id=48158506)

**背景**: 大语言模型通常依靠扩展上下文窗口来记住过往信息，但这成本高昂且常因注意力稀释而效果不佳。Delta 规则受 Hebbian 学习启发，通过计算新值与预测值之间的差异来更新隐藏记忆状态，从而将序列数据高效压缩为固定大小的表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.12357">δ-mem: Efficient Online Memory for Large Language Models</a></li>
<li><a href="https://huggingface.co/papers/2605.12357">Paper page - δ-mem: Efficient Online Memory for Large Language ...</a></li>
<li><a href="https://www.alphaxiv.org/audio/2605.12357v1">$δ$-mem: Efficient Online Memory for Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出分歧：一些人认为固定大小的状态是实现智能体无限上下文的一条路径，而另一些人则质疑记忆容量和查询关联的有效性。还有要求透明报告内存需求和吞吐量指标的呼声。

**标签**: `#LLM`, `#memory`, `#efficiency`, `#AI research`, `#online learning`

---

<a id="item-5"></a>
## [Google 将 AI 搜索操纵列入垃圾内容政策](https://www.theverge.com/tech/931416/google-ai-search-spam-policy) ⭐️ 8.0/10

Google 更新了搜索垃圾内容政策，明确禁止操纵生成式 AI 搜索结果（包括 AI Overview 和 AI Mode），针对偏见内容注入和提示注入等技术。 这项政策变化直接打击了旨在操纵 AI 搜索结果的生成式引擎优化（GEO）新兴实践。违规站点可能被降权或从搜索结果中移除，重塑 AI 时代的 SEO 策略。 该政策将 AI 搜索操纵与传统垃圾战术同等对待。常见的 GEO 方法包括批量生成有偏见的“最佳推荐”内容，或嵌入提示注入以欺骗 AI 模型将某站点视为权威来源。

telegram · zaihuapd · May 16, 06:31

**背景**: 生成式引擎优化（GEO）是一种通过结构化内容来提高在 AI 生成搜索回复中可见性的实践，这一概念首次在 2023 年的一篇 arXiv 论文中提出。提示注入是一种安全漏洞，恶意输入可覆盖 AI 指令，被用于操纵 AI 搜索排名。Google 的新政策正式将此类做法视为垃圾内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_engine_optimization">Generative engine optimization - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2311.09735">[2311.09735] GEO: Generative Engine Optimization - arXiv.org GEO: Generative Engine Optimization What’s Generative Engine Optimization (GEO) & How To Do It? The Birth Of GEO: Generative Engine Optimization And What It ... Generative Engine Optimization (GEO): Complete Guide 2025 Top Stories Generative engine optimization - Wikipedia Generative engine optimization (GEO): How to win AI mentions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google`, `#AI search`, `#spam policy`, `#SEO`, `#GEO`

---

<a id="item-6"></a>
## [OpenAI 与马耳他合作，向全体公民免费提供 ChatGPT Plus](https://openai.com/index/malta-chatgpt-plus-partnership/) ⭐️ 8.0/10

OpenAI 与马耳他政府宣布了一项国家级合作，凡是完成马耳他大学开发的 AI 素养课程的公民，均可免费获得一年的 ChatGPT Plus 访问权限。 这是全球首个国家级 AI 普及合作，为政府主导的 AI 素养计划树立了先例，可能加速 AI 在全体国民中的普及。 该计划名为 'AI for All'，将于 5 月启动，由马耳他数字创新局管理，并逐步扩大到海外公民。

telegram · zaihuapd · May 16, 10:40

**背景**: ChatGPT Plus 是 OpenAI 旗下 ChatGPT 聊天机器人的付费订阅版本，提供更快的响应速度、优先访问权以及 GPT-4 等高级功能。此次合作开创了独特模式：国家政府通过补贴 AI 工具，换取公民完成教育模块。

**标签**: `#OpenAI`, `#ChatGPT Plus`, `#马耳他`, `#AI普及`, `#政府合作`

---

<a id="item-7"></a>
## [GitHub Copilot 桌面应用进入技术预览](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) ⭐️ 8.0/10

GitHub 发布了 Copilot 桌面应用的技术预览，开发者可以从 issue、PR、提示词或历史会话启动隔离的开发会话，并通过 Agent Merge 自动处理 PR 审查评论和合并。 这标志着 Copilot 从 IDE 插件扩展为独立的智能开发环境，简化了从 issue 到合并的整个工作流。它直接影响了数百万使用 GitHub 的开发者，减少了手动 PR 管理，实现了无需上下文切换的隔离会话。 预览版现已面向 Copilot Pro 和 Pro+ 订阅者开放，Business 和 Enterprise 用户将在本周内逐步获得访问权限，但需要组织管理员在策略中开启预览和 CLI 权限。该应用支持跨仓库的多个并发智能体会话，每个会话都隔离并实时跟踪。

telegram · zaihuapd · May 16, 15:07

**背景**: GitHub Copilot 是由 GitHub 和 OpenAI 开发的 AI 代码补全和编程助手，最初作为插件集成在 VS Code 和 JetBrains 等 IDE 中。新的桌面应用引入了 GitHub 原生的智能体开发体验，允许用户将智能体分配给 issue 或 PR，并在应用内审查变更。这建立在最近的 Copilot CLI 智能体和统一会话视图等功能之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/">GitHub Copilot app is now available in technical preview - GitHub Changelog</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/2544/github-copilot-app-technical-preview-2026">GitHub Copilot App: Microsoft's Agentic Desktop Client Opens Waitlist...</a></li>
<li><a href="https://github.com/features/preview/github-app">GitHub Copilot app · GitHub</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Copilot`, `#developer tools`, `#AI`, `#preview`

---