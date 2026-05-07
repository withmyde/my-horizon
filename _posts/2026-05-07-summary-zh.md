---
layout: default
title: "Horizon Summary: 2026-05-07 (ZH)"
date: 2026-05-07
lang: zh
---

> From 28 items, 10 important content pieces were selected

---

1. [Firefox 借助 Claude Mythos 发现数百个漏洞](#item-1) ⭐️ 9.0/10
2. [Anthropic 与 SpaceX 合作提升 Claude 算力上限](#item-2) ⭐️ 9.0/10
3. [Chrome 移除设备端 AI 隐私声明](#item-3) ⭐️ 8.0/10
4. [SQLite 被美国国会图书馆推荐为存储格式](#item-4) ⭐️ 8.0/10
5. [AI 芯片需求挤压供应，主板销量暴跌 25%](#item-5) ⭐️ 8.0/10
6. [月之暗面估值超 100 亿美元，完成超 7 亿美元融资](#item-6) ⭐️ 8.0/10
7. [苹果研发支出占比突破 10%，加速 AI 布局](#item-7) ⭐️ 8.0/10
8. [腾讯 Hy3 预览版两周调用量超 Hy2 十倍](#item-8) ⭐️ 8.0/10
9. [Google Cloud 将 reCAPTCHA 升级为 Fraud Defense，加入二维码验证](#item-9) ⭐️ 8.0/10
10. [小米开源 OmniVoice：极简架构实现 646 语种语音克隆 TTS](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox 借助 Claude Mythos 发现数百个漏洞](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla 利用 Claude Mythos 预览版配合改进的提示技术，在 2026 年 4 月发现并修复了 Firefox 中的 423 个安全漏洞，而此前每月通常仅修复 20-30 个。 这标志着 AI 生成的安全报告从被视作“垃圾”到大规模发现真实漏洞的范式转变，显著提升了开源软件的安全性。 AI 程序多次被 Firefox 的纵深防御机制阻止，但仍发现了包括 20 年历史的 XSLT 漏洞和 15 年历史的 <legend> 元素漏洞在内的古老缺陷。修复数量从 2025 年的每月 20-30 个跃升至 2026 年 4 月的 423 个。

rss · Simon Willison · May 7, 17:56

**背景**: Claude Mythos Preview 是 Anthropic 于 2026 年 4 月作为 Project Glasswing 一部分发布的最先进的前沿大语言模型。它通过 Claude Code 在隔离容器中以代理方式寻找安全漏洞。此前，AI 生成的安全报告常常错误百出，给维护者带来高昂成本，而近期模型能力和提示技术的改进改变了这一局面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Firefox`, `#vulnerability detection`, `#LLM`

---

<a id="item-2"></a>
## [Anthropic 与 SpaceX 合作提升 Claude 算力上限](https://t.me/zaihuapd/41259) ⭐️ 9.0/10

Anthropic 宣布与 SpaceX（xAI）达成合作，将使用 Colossus 1 数据中心的全部算力，包括超过 22 万块 NVIDIA GPU 和 300 兆瓦新增容量。因此，Claude Code 的速率限制翻倍，Pro 和 Max 用户的高峰期限制被取消，同时 Claude Opus API 的限额也大幅提升。 此次合作为 Anthropic 提供了巨大的算力资源，使其能够扩展 Claude 服务并满足开发者和企业日益增长的需求。这也凸显了大规模 GPU 集群作为 AI 竞争关键基础设施的重要性。 该协议使 Anthropic 独家使用 Colossus 1 数据中心，该中心最初由 xAI 为训练 Grok 而建。新增容量来自 Colossus 1 以及近期与亚马逊和谷歌达成的其他协议。

telegram · zaihuapd · May 7, 08:19

**背景**: Colossus 是 xAI 于 2024 年 9 月推出的超级计算机，位于田纳西州孟菲斯，最初拥有 10 万块 NVIDIA H100 GPU，被认为是世界上最大的 AI 超级计算机。Anthropic 开发 Claude 系列 AI 模型，与 OpenAI 的 GPT 和 Google 的 Gemini 竞争。算力是 AI 公司的关键约束，因为训练和运行大型模型需要大量 GPU 和高能耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/news/anthropic-to-rent-all-ai-capacity-at-spacexs-colossus-data-center-180327774.html">Anthropic to rent all AI capacity at SpaceX's Colossus data center</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#算力`, `#合作`, `#NVIDIA`, `#Claude`

---

<a id="item-3"></a>
## [Chrome 移除设备端 AI 隐私声明](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/) ⭐️ 8.0/10

谷歌 Chrome 从其文档中删除了一句声明，该声明称设备端 AI 功能不会向谷歌服务器发送数据，此举引发了新的隐私担忧。 此次删除暗示数据现在可能会被发送到服务器，与先前的隐私保证相矛盾，从而削弱了用户信任。它影响了数百万依赖内置 AI 功能的 Chrome 用户。 这一删除是在 Chrome 关于设备端 AI 功能（如 Gemini Nano）的文档中被注意到的，而该功能最近被发现在未经明确同意的情况下悄然向用户设备下载了 4GB 的模型。

hackernews · newsoftheday · May 7, 15:56 · [社区讨论](https://news.ycombinator.com/item?id=48050964)

**背景**: 设备端 AI 在用户设备本地运行机器学习模型，以提供写作辅助和诈骗检测等功能，而无需将数据发送到云端。Chrome 的 Gemini Nano 是谷歌用于设备端任务的轻量级 AI 模型，但其静默下载以及现在被删除的隐私声明引发了关于数据收集实践的争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.google.com/chrome/ai-innovations/">Gemini in Chrome | The next generation of AI in Chrome | Chrome</a></li>
<li><a href="https://developer.chrome.com/docs/ai/get-started">Get started with built-in AI | AI on Chrome | Chrome for Developers</a></li>
<li><a href="https://www.tomsguide.com/ai/check-your-storage-chrome-may-be-downloading-a-4gb-ai-model-heres-what-we-know">'No clear consent flow for this download': Google Chrome is silently stashing a 4GB AI model on your device — and Google just responded | Tom's Guide</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了广泛的不信任，用户指出将 AI 添加到桌面应用是在用户不知情的情况下收集数据的有效方式。有人质疑谷歌是否真的禁用了数据发送，而另一些人则建议改用 Brave 等替代品。

**标签**: `#privacy`, `#chrome`, `#google`, `#ai`, `#data-collection`

---

<a id="item-4"></a>
## [SQLite 被美国国会图书馆推荐为存储格式](https://sqlite.org/locrsf.html) ⭐️ 8.0/10

美国国会图书馆正式将 SQLite 列为长期数字保存的推荐存储格式。这一认可在 2026 年推荐格式声明中被强调。 这一来自重要保存机构的认可验证了 SQLite 的可靠性和归档适用性，将影响图书馆、机构和开发者的保存实践。它可能鼓励 SQLite 在数据密集型应用中的更广泛采用，并增强对其长期可行性的信任。 SQLite 是美国国会图书馆为数据集存储推荐的四种格式之一，属于其数字保存的“推荐格式声明”。该推荐针对数据集，而非通用文件格式。

hackernews · whatisabcdefgh · May 6, 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48042434)

**背景**: 美国国会图书馆维护一份推荐格式列表，以确保数字内容长期可访问。SQLite 是一个自包含、无服务器的数据库引擎，以其简单、可靠和零配置而广泛应用于各类应用。被推荐意味着它符合开放性、稳定性、广泛采用和无专有限制等标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQLite">SQLite - Wikipedia</a></li>
<li><a href="https://thecodersblog.com/sqlite-as-recommended-storage-format-2026/">SQLite: Library of Congress Recommended for Digital Preservation</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了不同观点：有人赞赏 SQLite 的简洁性，但担心便携文件中可能包含个人身份信息；而另一些人承认从最初认为它是玩具到如今广泛使用的转变。一位用户指出该公告来自 2018 年，但这一认可仍然具有现实意义。

**标签**: `#sqlite`, `#digital preservation`, `#databases`, `#data storage`

---

<a id="item-5"></a>
## [AI 芯片需求挤压供应，主板销量暴跌 25%](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers) ⭐️ 8.0/10

由于芯片制造商优先生产 AI 芯片而非消费级 PC 组件，主板销量暴跌超过 25%，预计华硕在 2025 年将少售 500 万块主板，技嘉、微星和华擎等其他主要厂商也预期销量下降。 这一转变标志着 PC 硬件行业的根本性调整——AI 需求不仅推高了组件价格，还减少了消费级硬件的供应和创新，可能迫使发烧友离开 PC 平台。 短缺不仅限于主板，还波及机箱、风扇、消费级 SSD 等 PC 配件，芯片制造商将晶圆厂产能转向利润率更高的 AI 芯片，供应紧张预计将持续到 2027 年。

hackernews · speckx · May 7, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48050540)

**背景**: 主板连接所有 PC 组件，是组装台式机的核心。近年来，新一代 CPU/GPU 的性能提升递减，削弱了升级动力。与此同时，AI 热潮挤占了芯片制造产能，导致消费级 PC 使用的常规内存和逻辑芯片短缺并涨价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sourceability.com/post/ai-chip-shortages-deepen-amid-tariff-risks">AI demand sparks memory supply chain strain | Sourceability</a></li>
<li><a href="https://wccftech.com/amd-warns-pc-gaming-demand-will-decline-in-h2-as-memory-prices-surge/">AMD Warns PC & Gaming Demand Will Decline In H2 As Memory...</a></li>

</ul>
</details>

**社区讨论**: 评论者感叹 PC 硬件价格飙升——主板从 100-200 美元涨至 300 美元以上，且性能提升递减使升级缺乏动力。有人指出一个悖论：AI 既导致短缺，又减少了人们对强大 PC 的需求，因为任务转移到了云端。

**标签**: `#AI`, `#PC Hardware`, `#Supply Chain`, `#Market Trends`, `#Consumer Electronics`

---

<a id="item-6"></a>
## [月之暗面估值超 100 亿美元，完成超 7 亿美元融资](https://t.me/zaihuapd/41251) ⭐️ 8.0/10

月之暗面完成新一轮超 7 亿美元融资，估值突破 100 亿美元，仅用两年多时间成为“十角兽”；其 AI 助手 Kimi 近 20 天累计收入已超过 2025 年全年总额。 这一里程碑显示了中国 AI 初创公司强大的投资者信心，以及大语言模型快速商业化的能力；Kimi 海外收入已超过国内，表明其全球竞争力。 本轮融资由阿里、腾讯、五源资本和九安医疗联合领投，累计融资超 12 亿美元；Kimi 的 K2.5 模型支持多达 100 个专业智能体协同的 Agent Swarm 技术，已在 OpenRouter 上线，推动了收入增长。

telegram · zaihuapd · May 7, 00:30

**背景**: 月之暗面是中国 AI 初创公司，以 Kimi 助手和 K2.5 大语言模型闻名。“十角兽”指估值超过 100 亿美元的初创企业。OpenRouter 是一个提供多模型统一 API 访问的平台，包括 K2.5。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MoonshotAI/Kimi-K2.5">GitHub - MoonshotAI/Kimi-K2.5: Moonshot's most powerful model · GitHub</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.5">moonshotai/Kimi-K2.5 · Hugging Face</a></li>
<li><a href="https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model">Kimi K2.5: Complete Guide to Moonshot's AI Model | Codecademy</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI startup`, `#funding`, `#Moonshot AI`, `#Kimi`, `#valuation`

---

<a id="item-7"></a>
## [苹果研发支出占比突破 10%，加速 AI 布局](https://www.cnbc.com/2026/05/06/apples-rd-spending-climbs-to-10percent-of-revenue-on-ai-investments.html) ⭐️ 8.0/10

苹果 2026 年 3 月财季研发支出占营收比例升至 10.3%，为 30 年来首次突破 10%，同比增长 34%，主要投入 AI 领域。 这一里程碑标志着苹果战略转向以 AI 为核心平台重塑硬件生态，类似于 iPod 时代，将影响其端侧 AI、自研芯片和私有云计算等关键方向。 苹果正大力投入端侧 AI、自研芯片（如用于私有云计算的 M5 芯片），以及 AI 眼镜和带摄像头的 AirPods 等新产品，此外还有首款折叠屏 iPhone 和 Siri 升级。

telegram · zaihuapd · May 7, 01:00

**背景**: 端侧 AI 是指在本地设备上直接运行人工智能算法，相比云端 AI 能降低延迟并提升隐私性。苹果的私有云计算（PCC）使用搭载自研芯片的专用服务器，在处理敏感 AI 任务时保护用户隐私。这些技术是苹果将 AI 深度整合进硬件生态的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.com.cn/stock/t/2025-12-10/doc-inhaicsz1972147.shtml">概念研究所-什么是AI端侧？|AI_新浪财经_新浪网</a></li>
<li><a href="https://semiconductor.samsung.cn/technologies/processor/on-device-ai/">端侧AI | 技术 | 三星半导体官网</a></li>
<li><a href="https://stock.10jqka.com.cn/usstock/20260218/c674837048.shtml">消息称 苹 果 AI 私 有 云 端 算 力大跃进：跳过 M3 和 M4，直接部署 M5 芯片</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#研发`, `#硬件生态`

---

<a id="item-8"></a>
## [腾讯 Hy3 预览版两周调用量超 Hy2 十倍](https://finance.sina.com.cn/tech/shenji/2026-05-07/doc-inhwzrtp8521239.shtml) ⭐️ 8.0/10

腾讯混元 Hy3 preview 模型（295B 参数 MoE 架构）上线两周后，Token 调用量达到上一代 Hy2 的十倍，并在 OpenRouter 周榜中排名第一。 这一快速采用表明腾讯最新 AI 模型在编程和智能体工作流等领域具有强大的产品-市场契合度，也凸显了高效 MoE 模型在生产部署中日益增长的重要性。 Hy3 preview 是一个 295B 参数的 MoE 模型，但仅有 21B 活跃参数和 3.8B MTP 层，支持高效推理。它提供可配置的推理级别（关闭、低、高），并在 OpenRouter 上临时免费以收集真实场景反馈。

telegram · zaihuapd · May 7, 05:34

**背景**: 混合专家（MoE）模型每次只激活部分参数，在模型容量与计算成本间取得平衡。腾讯 Hy3 preview 是公司重建训练基础设施后的首个模型。OpenRouter 是一个统一 API 平台，汇集了来自不同提供商的数百个大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy3-preview">tencent / Hy 3 - preview · Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy3-preview:free">Hy 3 preview (free) - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://docs.clore.ai/guides/language-models/hy3-preview">Hy 3 Preview ( Tencent Hunyuan 3, 295B MoE) | Guides | Clore.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#Tencent`, `#model deployment`, `#OpenRouter`

---

<a id="item-9"></a>
## [Google Cloud 将 reCAPTCHA 升级为 Fraud Defense，加入二维码验证](https://support.google.com/recaptcha/answer/16609652?hl=en) ⭐️ 8.0/10

Google Cloud 宣布推出 Fraud Defense，作为 reCAPTCHA 的下一代演进，新增二维码挑战，用于验证网站和应用中的人类存在。 这一升级将广泛使用的机器人检测工具提升为抵御 AI 驱动欺诈的能力，采用新颖且用户友好的验证方法，影响整个网络的安全。 二维码验证要求用户用手机扫描二维码；兼容 Android Google Play Services 25.41.30+、iOS/iPadOS 15.0+，且“点击验证”按钮有特定版本要求。

telegram · zaihuapd · May 7, 09:18

**背景**: reCAPTCHA 是 Google 的 CAPTCHA 系统，用于区分人类和机器人。Fraud Defense 将其扩展为面向智能体网络的全面信任平台，提供风险评分和取证理由以自动化安全策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/security/products/fraud-defense">Google Cloud Fraud Defense - The evolution of reCAPTCHA.</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha">Introducing Google Cloud Fraud Defense , the... | Google Cloud Blog</a></li>

</ul>
</details>

**标签**: `#security`, `#reCAPTCHA`, `#fraud prevention`, `#Google Cloud`, `#QR code`

---

<a id="item-10"></a>
## [小米开源 OmniVoice：极简架构实现 646 语种语音克隆 TTS](https://mp.weixin.qq.com/s/TCS_Sd10g_rvf1cszw673A) ⭐️ 8.0/10

小米开源了 OmniVoice 多语言文本转语音（TTS）模型，采用极简双向 Transformer 架构，支持 646 种语言，训练速度达每天 10 万小时，PyTorch 推理速度达 40 倍实时，合成质量优于同类主流模型。 此次开源使得高质量多语言 TTS 技术普及化，开发者和研究者无需大量专有数据即可构建覆盖众多语言的语音应用。同时，它填补了开源社区在高扩展性、高效率且具有竞争力的多语言 TTS 系统方面的空白。 该模型采用全码本随机掩蔽技术，并利用预训练大语言模型参数提升训练效率和可懂度。它在 50 个开源数据集的 58 万小时数据上训练，在 24 种语言上超越商用系统，在 102 种语言上接近真实语音。

telegram · zaihuapd · May 7, 10:06

**背景**: 文本转语音（TTS）技术将文字转化为语音。多语言 TTS 模型由于数据稀缺和语音多样性而面临挑战。OmniVoice 采用简洁的 Transformer 设计，结合大语言模型技术，实现了广泛的语言覆盖和高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/full-codebook-random-masking">Full - Codebook Random Masking</a></li>
<li><a href="https://github.com/soobinseo/Transformer-TTS/blob/master/module.py">Transformer - TTS /module.py at master · soobinseo/ Transformer - TTS</a></li>

</ul>
</details>

**标签**: `#TTS`, `#multilingual`, `#open source`, `#speech synthesis`, `#Xiaomi`

---