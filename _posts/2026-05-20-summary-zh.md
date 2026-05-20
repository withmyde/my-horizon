---
layout: default
title: "Horizon Summary: 2026-05-20 (ZH)"
date: 2026-05-20
lang: zh
---

> From 38 items, 12 important content pieces were selected

---

1. [谷歌发布 Gemini 3.5 Flash AI 模型](#item-1) ⭐️ 9.0/10
2. [Google 用 Gemini AI 全面改造搜索](#item-2) ⭐️ 9.0/10
3. [Andrej Karpathy 加入 Anthropic 预训练团队](#item-3) ⭐️ 9.0/10
4. [CISA 承包商在 GitHub 泄露 AWS GovCloud 凭证](#item-4) ⭐️ 9.0/10
5. [Google Cloud 未通知即封锁 Railway 基础设施](#item-5) ⭐️ 8.0/10
6. [虚拟博物馆展出几乎所有操作系统](#item-6) ⭐️ 8.0/10
7. [OpenAI 采用谷歌 SynthID 水印保护 AI 图像](#item-7) ⭐️ 8.0/10
8. [Forge 护栏将 8B 模型在智能体任务上的准确率从 53%提升至 99%](#item-8) ⭐️ 8.0/10
9. [苹果推出融入代理型 AI 的无障碍功能](#item-9) ⭐️ 8.0/10
10. [DeepSeek 会话隔离漏洞：'<think' 导致用户对话泄露](#item-10) ⭐️ 8.0/10
11. [伊朗要求美科技巨头为霍尔木兹海峡海底电缆付费](#item-11) ⭐️ 8.0/10
12. [Gemini Omni 支持对话式视频编辑](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 3.5 Flash AI 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) ⭐️ 9.0/10

谷歌发布了 Gemini 3.5 Flash，这是一个原生多模态推理模型，支持可调思考层级，定价为每百万输入标记 1.50 美元，每百万输出标记 9.00 美元。 相比之前的 Flash 模型，价格提高了 3 倍，这标志着谷歌定价策略的重大转变，可能会影响开发者的采用，但该模型在速度与智能之间取得了良好平衡，使其在代理应用中具有竞争力。 该模型在 TPU 8i 上运行，社区分析者根据硬件限制推断出参数数量。它提供思考层级（中等、高）以平衡质量、成本和延迟，并支持多模态输入。

hackernews · spectraldrift · May 19, 17:43 · [社区讨论](https://news.ycombinator.com/item?id=48196570)

**背景**: Gemini 3.5 Flash 是谷歌 Gemini 3 系列原生多模态推理模型的一部分，该系列结合了文本、图像、音频和视频理解能力。'Flash' 变体旨在实现更快、更高效的推理，但这个新版本在维持强大推理性能的同时引入了更高的定价。模型卡将其描述为 Gemini 3 系列的下一个迭代，通过思考层级来控制质量、成本和延迟的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-5-flash/">Gemini 3.5 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/google/2026/05/google-announces-agent-optimized-gemini-3-5-flash-and-a-do-anything-model-called-omni/">Gemini 3.5 Flash might be fast enough for gen AI to make sense</a></li>
<li><a href="https://artificialanalysis.ai/articles/gemini-3-5-flash-everything-you-need-to-know">Gemini 3.5 Flash: The new leader in intelligence versus speed</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人注意到比 Gemini 2.5 Flash 贵了 3 倍，令人担忧；另一些人则提供了技术分析，根据 TPU 规格推断参数数量。一位评论者报告说，在一个代理 SQL 基准测试中表现平庸（19/25），比 Gemini 3.1 Flash Lite Preview（22/25）更慢。

**标签**: `#AI`, `#Gemini`, `#Google`, `#model release`, `#pricing`

---

<a id="item-2"></a>
## [Google 用 Gemini AI 全面改造搜索](https://blog.google/products-and-platforms/products/search/search-io-2026/) ⭐️ 9.0/10

在 2026 年 Google I/O 大会上，Google 宣布对其搜索引擎进行重大 AI 改造，将 Gemini AI 助手深度集成到搜索框中。这根本性地改变了搜索结果的呈现方式，AI 生成的摘要和对话式回答取代了传统的链接列表。 这标志着全球最常用搜索引擎的范式转变，可能会减少对网站的有机流量，因为用户可以直接从 Google 获得答案。这引发了关于网络出版、内容发现以及 AI 生成信息可靠性的紧迫问题。 这种集成超越了早期的 AI 摘要；Gemini 现在驱动整个搜索体验，包括复杂查询、产品比较和本地推荐。Google 声称该系统是‘对话式’的，可以跟进问题，但早期报告表明它仍然存在幻觉和来源归因问题。

hackernews · berkeleyjunk · May 19, 18:34 · [社区讨论](https://news.ycombinator.com/item?id=48197370)

**背景**: 过去二十多年，Google 通过排名列表将用户链接到其他网站，主导了网络搜索。在 2026 年开发者大会（I/O）上，该公司揭示了一个根本性转变：Gemini AI 模型现在直接在搜索框中生成答案，通常无需用户点击访问外部网站。这一举措与 AI 助手取代传统搜索的行业趋势一致，但 Google 的规模使其成为开放网络的关键时刻。

**社区讨论**: 社区评论表达了重大担忧。用户担心 AI 可靠性、缺乏原始来源以及‘Google 归零’的可能性——即 Google 停止向外部网站发送流量的时刻。有人怀念原始搜索框的简洁，也有人质疑 LLM 生成答案的事实准确性。

**标签**: `#google`, `#search`, `#ai`, `#gemini`, `#io2026`

---

<a id="item-3"></a>
## [Andrej Karpathy 加入 Anthropic 预训练团队](https://twitter.com/karpathy/status/2056753169888334312) ⭐️ 9.0/10

OpenAI 联合创始人、前特斯拉 AI 总监 Andrej Karpathy 在推特上宣布加入 Anthropic，负责 Claude 的预训练工作。他将加入预训练团队，该团队负责执行大规模训练任务，赋予 Claude 核心知识与能力。 Karpathy 是极具影响力的 AI 研究者和教育家，他加入 Anthropic 标志着该公司在前沿 AI 竞赛中影响力日益增强。这也凸显了预训练在开发像 Claude 这样最先进的大语言模型中的关键作用。 据 Anthropic 证实，Karpathy 将立即开始在 Anthropic 的预训练团队工作。他此前在 2025 年 2 月首创了“vibe coding”这一术语，并于 2024 年创办了 AI 教育公司 Eureka Labs。

hackernews · dmarcos · May 19, 15:07 · [社区讨论](https://news.ycombinator.com/item?id=48194352)

**背景**: 预训练是构建大语言模型的初始阶段，系统从大量未标注数据中学习，捕获通用模式和知识。这一阶段计算密集，是模型能力的基础。Karpathy 在 AI 领域阅历丰富，包括作为 OpenAI 创始成员、领导特斯拉 Autopilot 视觉系统，以及创建 nanoGPT 等广受欢迎的教育项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nebius.com/blog/posts/understanding-pre-trained-ai-models">Understanding pre-trained AI models and their applications</a></li>
<li><a href="https://www.ibm.com/think/topics/pretrained-model">What Is A Pretrained Model? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区反应喜忧参半。许多人称赞 Karpathy 作为教育者的贡献，而一些人则担心 Anthropic 日益增长的主导地位以及保密协议可能限制他的教学。还有人提及他此前暗示过加入前沿实验室的言论。

**标签**: `#AI`, `#Anthropic`, `#Karpathy`, `#deep learning`, `#pre-training`

---

<a id="item-4"></a>
## [CISA 承包商在 GitHub 泄露 AWS GovCloud 凭证](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 9.0/10

一名 CISA 承包商在公共 GitHub 仓库中泄露了 AWS GovCloud 访问密钥和内部系统的明文密码，暴露了高度敏感的政府云基础设施凭证。 此次泄密动摇了人们对政府云安全的信任，并凸显了凭证管理方面的系统性失败，可能使对手能够访问敏感的美国政府数据和系统。 泄露的文件包括 AWS Workspace Firefox 密码以及数十个 CISA 内部系统的明文用户名和密码，且承包商未对研究人员的初始通知做出回应。

hackernews · LelouBil · May 19, 07:45 · [社区讨论](https://news.ycombinator.com/item?id=48190454)

**背景**: AWS GovCloud（美国）是一个合规的云环境，专为美国政府机构托管敏感和受控非机密信息（CUI）而设计。在公共仓库中存储此类凭证且未进行自动扫描，违反了基本安全实践和联邦指南。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/whatis.html">What Is AWS GovCloud (US)? - AWS GovCloud (US)</a></li>

</ul>
</details>

**社区讨论**: 评论者表示震惊和难以置信，指出网络安全机构出现此类泄露是不可原谅的；一些人怀疑这可能是蜜罐，另一些人则担心 LLM 可能通过环境文件无意中暴露秘密。

**标签**: `#security`, `#cloud`, `#CISA`, `#leak`, `#GitHub`

---

<a id="item-5"></a>
## [Google Cloud 未通知即封锁 Railway 基础设施](https://status.railway.com/?date=20260519) ⭐️ 8.0/10

Google Cloud 在未事先联系人工的情况下封锁了 Railway 的全部基础设施，导致严重宕机。Railway 公开记录了此次事件，引发了对 GCP 自动化滥用预防系统的广泛批评。 此事件凸显了依赖缺乏人工审核的自动化云滥用系统的风险，尤其对初创公司而言。它强化了对 GCP 支持质量与 AWS 或 Azure 相比的担忧，可能影响云服务商的选择。 Railway 是一个 PaaS（平台即服务）提供商，为开发者抽象云复杂性。封锁发生在 Google Cloud 没有任何事先邮件或电话联系的情况下，从识别问题到 GCP 支持介入耗时超过一小时。

hackernews · aarondf · May 20, 00:23 · [社区讨论](https://news.ycombinator.com/item?id=48201484)

**背景**: Railway 是一个现代化的部署平台，类似于 Heroku 或 Vercel，提供按用量计费和自动扩展。Google Cloud 拥有自动化的滥用事件日志系统，可以标记并阻止可疑工作负载，但它依赖于可能无法及时送达人工的通知。此类事件此前已发生过，削弱了对 GCP 运营实践的信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://railway.com/">Railway | The all-in-one intelligent cloud provider</a></li>
<li><a href="https://docs.cloud.google.com/docs/security/respond-to-abuse-misuse">Respond to abuse notifications and warnings in Google Cloud</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/introducing-abuse-event-logging-for-automated-incident-remediation">Introducing Google Cloud Abuse Event Logging to enable automated ...</a></li>

</ul>
</details>

**社区讨论**: 评论对 GCP 批评激烈，质疑为何如此大规模的封锁能够在无人联系的情况下发生（binarycleric, UrbanNorminal）。有用户指出 Railway 的 IP 产生大量垃圾流量，暗示其滥用防护不力（BitWiseVibe）。另一用户表示这是 GCP 的反复问题，而 AWS 或 Azure 则不然（dangoodmanUT）。

**标签**: `#Google Cloud Platform`, `#incident management`, `#cloud computing`, `#startup infrastructure`, `#DevOps`

---

<a id="item-6"></a>
## [虚拟博物馆展出几乎所有操作系统](https://virtualosmuseum.org/) ⭐️ 8.0/10

一个名为‘Virtual OS Museum’的虚拟博物馆已上线，展示了从历史到现代的几乎所有操作系统，并提供模拟演示。 该博物馆保存了计算历史，让用户体验稀有和被遗忘的操作系统，引发了关于操作系统演变和遗漏的有价值社区讨论。 该博物馆包含了许多版本，但一些评论者指出了如 Pick 和 TempleOS 等重要遗漏，并批评某些条目展示了‘最后、最伟大’的版本，可能并非最有趣的。

hackernews · andreww591 · May 19, 15:53 · [社区讨论](https://news.ycombinator.com/item?id=48195009)

**背景**: 操作系统是管理计算机硬件并为应用程序提供服务的基础软件。几十年来，从早期的命令行系统到现代图形界面，许多操作系统被开发出来，其中一些变得鲜为人知。虚拟博物馆使用模拟技术在网络浏览器中运行这些老系统，让人们可以交互式地探索计算历史。

**社区讨论**: 评论者赞扬了策展工作，但指出了遗漏（如 Pick、TempleOS），并就展示‘最后’版本的准确性进行了辩论。一位评论者分享了 Apollo DomainOS 的独特功能，如提前输入编辑，而另一位询问了特定的 Windows 3.1 版本。

**标签**: `#operating systems`, `#curation`, `#history`, `#computing`, `#museum`

---

<a id="item-7"></a>
## [OpenAI 采用谷歌 SynthID 水印保护 AI 图像](https://openai.com/index/advancing-content-provenance/) ⭐️ 8.0/10

OpenAI 已将谷歌 DeepMind 的 SynthID 不可见水印集成到其图像生成模型中，并发布了一种新的验证工具来检测 AI 生成的图像。 这一采用标志着行业在内容来源标准上的重大合作，可能使 AI 生成的图像更可追溯，减少欺骗性合成媒体的传播。 SynthID 嵌入了一种不可察觉的数字水印，即使在裁剪或压缩等转换后仍可检测；然而，部分社区成员声称可以通过像素操作将其去除。

hackernews · smooke · May 19, 19:34 · [社区讨论](https://news.ycombinator.com/item?id=48198291)

**背景**: SynthID 是谷歌 DeepMind 开发的一种技术，可为 AI 生成的内容添加不可见水印。它设计为在常见修改后依然保留，并可通过检测工具验证。内容来源指的是追踪数字内容起源和历史的能力，随着 AI 生成媒体的普及变得越来越重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/responsible/docs/safeguards/synthid">SynthID: Tools for watermarking and detecting LLM-generated Text | Responsible Generative AI Toolkit | Google AI for Developers</a></li>
<li><a href="https://blog.google/innovation-and-ai/products/google-synthid-ai-content-detector/">SynthID Detector: Identify content made with Google’s AI tools</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点不一：部分用户展示了去除水印的技术方法，而另一些人则为其有效性辩护，指出尚无可重复的去除实例。还有人担心水印类似于数字版权管理（DRM）。

**标签**: `#AI images`, `#watermarking`, `#content provenance`, `#OpenAI`, `#SynthID`

---

<a id="item-8"></a>
## [Forge 护栏将 8B 模型在智能体任务上的准确率从 53%提升至 99%](https://github.com/antoinezambelli/forge) ⭐️ 8.0/10

Forge 是一个开源可靠性层，为在消费级硬件上运行的本地大语言模型添加护栏，在不修改模型本身的情况下，将多步骤智能体工作流的准确率从约 53%提升至约 99%。它通过五个可独立开关的护栏层实现，包括重试提示、错误恢复和步骤强制。 这项工作表明，当与强大的护栏系统配合时，小型本地模型在复杂智能体任务上可以媲美前沿 API，可能减少对昂贵云服务的依赖。它解决了累积误差问题，即每一步的高准确率在多步骤工作流中仍会导致频繁失败。 Forge 的护栏包括重试提示、错误恢复、步骤强制、救援解析和上下文压缩；消融研究表明，禁用重试提示会导致准确率下降 24-49 个百分点。该项目还引入了 ToolResolutionError，用于区分工具执行成功但无结果与工具失败，解决了当前大语言模型工具调用中的一个盲点。

hackernews · zambelli · May 19, 12:23 · [社区讨论](https://news.ycombinator.com/item?id=48192383)

**背景**: 智能体任务涉及大语言模型通过多步骤与工具或环境交互以实现目标，例如编写代码或搜索数据库。每一步都有成功概率，在步骤链中，即使每一步的准确率达到 90%，经过 5 步后也可能导致 40%的失败率，这被称为累积误差问题。护栏是外部机制，在输入和输出时进行拦截，以强制执行安全性和可靠性约束，而无需修改底层模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://labs.adaline.ai/p/what-are-agentic-llms-a-comprehensive">What Are Agentic LLMs? Use Cases, Risks, and How They Work</a></li>
<li><a href="https://grokipedia.com/page/LLM_Guardrails">LLM Guardrails</a></li>
<li><a href="https://arxiv.org/abs/2511.07568">Procedural Knowledge Improves Agentic LLM Workflows</a></li>

</ul>
</details>

**社区讨论**: 评论者认识到护栏对小型本地模型的价值，有人指出，具有重试机制的合适框架可以使小型模型表现出惊人的效果。另一位评论者强调，工具调用歧义问题（例如 grep 无匹配结果被解释为工具失败）即使在前沿模型中也普遍存在，并赞赏将重试提示层作为解决方案。

**标签**: `#llm`, `#agentic-ai`, `#guardrails`, `#local-models`, `#reliability`

---

<a id="item-9"></a>
## [苹果推出融入代理型 AI 的无障碍功能](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) ⭐️ 8.0/10

苹果宣布了新的无障碍功能，这些功能据信集成了代理型人工智能，能够为残障用户提供更自主的辅助。 此举可能为如何利用人工智能赋能残障人士树立新标准，有望推动整个行业在无障碍工具中采用代理型 AI。 这些功能据称利用了代理型 AI，它能够在设定约束内自主设定目标、使用工具并采取行动。社区评论还指出了苹果语音转文字转录方面持续存在的问题，暗示了改进方向。

hackernews · interpol_p · May 19, 12:04 · [社区讨论](https://news.ycombinator.com/item?id=48192224)

**背景**: 代理型 AI 指能够在人类设定的约束下自主追求目标并采取行动的智能体。苹果有通过无障碍功能引入新技术的传统，社区成员指出这是一种隐蔽测试手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>

</ul>
</details>

**社区讨论**: JeremyHerrman 指出苹果通过无障碍功能秘密测试技术的模式，并举例 Touch Bar。Brightbeige 分享了使用 Be My Eyes 的积极经历，而 postalcoder 批评苹果的语音转文字功能落后。Mohsen1 提到视频语速过快，nechuchelo 则称赞 LLM 在此类辅助中的实际应用。

**标签**: `#accessibility`, `#Apple`, `#AI`, `#agentic AI`, `#technology`

---

<a id="item-10"></a>
## [DeepSeek 会话隔离漏洞：'<think' 导致用户对话泄露](https://t.me/zaihuapd/41461) ⭐️ 8.0/10

新披露的 DeepSeek Web 和 API 对话模型漏洞允许在全新的空对话中输入未闭合的 '<think' 字符串，模型即返回其他用户的对话片段，可能泄露包括代码、密钥、隐私等敏感信息。 此漏洞造成严重的数据隐私风险，攻击者可轻易未经认证提取其他用户的机密信息，影响任何使用 DeepSeek 托管对话服务的组织或个人。 该漏洞由用户 'cancat2024' 于 2026 年 5 月 11 日负责任地披露，并已公开传播，增加了修复的紧迫性。据报道，DeepSeek 的第三方部署也受影响。

telegram · zaihuapd · May 19, 11:33

**背景**: DeepSeek 的对话模型使用像 '<think>' 这样的特殊标签来内部界定思维链推理。会话隔离是一种安全措施，防止一个对话会话的数据泄露到另一个会话；如果应用层未正确实现，上下文可能跨越用户扩散。该漏洞利用了对 '<think>' 标签缺乏输入过滤的缺陷，触发跨会话数据泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendmicro.com/en_us/research/25/c/exploiting-deepseek-r1.html">Exploiting DeepSeek-R1: Breaking Down Chain of Thought Security | Trend Micro (US)</a></li>
<li><a href="https://www.linkedin.com/posts/shannon-torcato_i-tested-an-ai-chatbot-on-a-website-last-activity-7426978937877991424-nBb2">AI Chatbot Security Flaw: Session Isolation and Data Exposure | Shannon Torcato posted on the topic | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 在 Telegram 群组中，有群友指出第三方部署也存在此现象，认为这是模型幻觉而非逻辑缺陷，但披露者视其为真实的会话隔离漏洞。

**标签**: `#security`, `#vulnerability`, `#deepseek`, `#AI`, `#data privacy`

---

<a id="item-11"></a>
## [伊朗要求美科技巨头为霍尔木兹海峡海底电缆付费](https://arstechnica.com/tech-policy/2026/05/iran-demands-big-tech-pay-fees-for-undersea-internet-cables-in-strait-of-hormuz/) ⭐️ 8.0/10

伊朗宣布将对通过霍尔木兹海峡的海底互联网电缆收费，目标直指 Meta、Google 等美国科技巨头，并声称拥有独家维修权。 此举威胁到全球互联网的关键咽喉——约 30%的数据流经这些电缆——可能中断连接，并加剧围绕数字基础设施的地缘政治紧张局势。 伊朗半官方媒体塔斯尼姆引用《联合国海洋法公约》第 34 条为收费提供法律依据。霍尔木兹海峡下方至少铺设了七条主要海底电缆，承载全球 30%的互联网流量。

telegram · zaihuapd · May 19, 16:40

**背景**: 霍尔木兹海峡是一条狭窄水道，承担着全球 20%的石油和 25%的液化天然气运输，同时也通过海底电缆承载约 30%的全球互联网流量。海底电缆是互联网的骨干，维修需要进入专属经济区的权利。伊朗的威胁正值地区冲突已导致部分电缆项目和维修停工之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/world/2026/may/18/iran-threat-internet-cables-strait-hormuz">How realistic is threat of Iran charging to use internet cables under...</a></li>
<li><a href="https://www.businesstoday.in/technology/story/why-the-strait-of-hormuz-matters-for-indias-internet-523294-2026-03-31">Why the Strait of Hormuz matters for India's internet - BusinessToday</a></li>

</ul>
</details>

**标签**: `#地缘政治`, `#互联网基础设施`, `#海底电缆`, `#伊朗`, `#网络安全`

---

<a id="item-12"></a>
## [Gemini Omni 支持对话式视频编辑](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/) ⭐️ 8.0/10

谷歌发布了多模态模型 Gemini Omni，用户可以通过自然语言对话来编辑视频。首个型号 Gemini Omni Flash 已通过 Gemini 应用向 Google AI Plus、Pro 和 Ultra 订阅用户开放，并同步登陆 Google Flow、YouTube Shorts 和 YouTube Create App。 这一进展通过让非专业人士能使用日常语言进行复杂编辑，从而普及了视频编辑，可能改变像 YouTube 这样的平台上的内容创作。它代表了多模态 AI 的重要一步，将现实世界物理理解与生成能力相结合。 该模型具备对重力、流体力学等物理规律的直观理解，并能确保在多次编辑中保持角色的一致性。所有生成的视频都嵌入了 SynthID 数字水印以确保透明度，谷歌计划在未来几周向开发者开放 API。

telegram · zaihuapd · May 19, 18:23

**背景**: Gemini Omni 是谷歌推出的新型多模态模型，接受图像、音频、视频和文本的混合输入来生成视频。它建立在谷歌现有的 Gemini 系列和 DeepMind 研究之上。SynthID 是谷歌的数字水印工具，它将一种不可见的签名直接嵌入 AI 生成的内容中，以帮助识别其为人工内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/">Introducing Gemini Omni</a></li>
<li><a href="https://deepmind.google/models/gemini-omni/">Gemini Omni — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#多模态AI`, `#视频编辑`, `#谷歌Gemini`, `#生成式AI`, `#自然语言处理`

---