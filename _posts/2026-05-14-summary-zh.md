---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 27 items, 3 important content pieces were selected

---

1. [AI 让个人软件定制化如 Emacs 般自由](#item-1) ⭐️ 8.0/10
2. [小米发布一步式潜空间推理框架 OneVL，用于自动驾驶](#item-2) ⭐️ 8.0/10
3. [Anthropic 与 SpaceX 合作获得大规模 AI 算力提升](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 让个人软件定制化如 Emacs 般自由](https://sockpuppet.org/blog/2026/05/12/emacsification/) ⭐️ 8.0/10

一篇博文指出，借助 AI，构建个人软件如今比使用现有应用更简单，从而催生出每个人都能拥有专属定制工具的软件生态，就像 Emacs 用户个性化编辑器一样。 这种转变可能使软件创作民主化，让个人无需依赖专业开发者就能构建所需工具，并可能改变我们与技术互动的方式，使软件更加个性化和适应性强。 评论者如 tptacek 列出了特定应用类别（播客应用、笔记应用等），AI 生成的解决方案在这些领域可以匹敌甚至超越商业产品。Dang 总结道，软件生产现已如此简单，以致于一切都变成了个人的 .emacs 文件。

hackernews · rdslw · May 13, 07:06 · [社区讨论](https://news.ycombinator.com/item?id=48118727)

**背景**: Emacs 是一个高度可扩展的文本编辑器，用户通常通过维护 .emacs 配置文件来定制行为、快捷键和功能。这里的“Emacs 化”是一个隐喻，描述了 AI 使构建定制软件变得像编辑 .emacs 文件一样普遍和个性化。

**社区讨论**: 讨论大体积极，评论者分享了他们使用 LLM 构建个人软件的经验。一些人指出了脆弱性和跨平台挑战，但总体情绪是这种趋势是真实而令人兴奋的，呼应了家庭计算的原始愿景。

**标签**: `#AI`, `#software development`, `#personal software`, `#LLMs`, `#Hacker News`

---

<a id="item-2"></a>
## [小米发布一步式潜空间推理框架 OneVL，用于自动驾驶](https://mp.weixin.qq.com/s/7po3r6YtmuXm8Xny1bw61Q) ⭐️ 8.0/10

小米推出了 Xiaomi OneVL，这是一个用于自动驾驶的一步式潜空间推理框架，首次将视觉-语言-动作（VLA）模型与世界模型统一。该框架已全面开源，包括模型权重、训练和推理代码。 OneVL 在多个基准测试中达到最优性能，首次在潜空间推理中超越显式思维链（CoT）方法。这一突破通过将场景理解与未来预测整合在一个高效框架中，可能大幅推动自动驾驶技术的发展。 OneVL 使用视觉潜 token 编码物理因果结构，语言潜 token 编码驾驶意图，推理时移除双辅助解码器实现一步并行生成。在 NAVSIM 上，PDM-score 达到 88.84，超过显式 CoT 的 88.29，采用 MLP 回归变体时延迟降至 0.24 秒，仅为自回归 VLA 推理的 5.4%。

telegram · zaihuapd · May 13, 10:33

**背景**: 传统上，自动驾驶系统将 VLA 模型（专注于场景理解和动作输出）与世界模型（专注于未来场景预测）分开。潜空间推理在压缩的潜空间中进行思维链推理，而非显式的 token 空间，可能提供更高效率。OneVL 融合了这些方法，使得同时推理当前动作和未来结果成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.mydrivers.com/1/1122/1122061.htm">小米自动驾驶模型Xiaomi OneVL开源：业内率先统一VLA、世界模型路线</a></li>
<li><a href="https://www.ithome.com/0/949/956.htm">小米开源 Xiaomi OneVL 自动驾驶模型，业内率先实现 VLA、世界模型等...</a></li>
<li><a href="https://hub.baai.ac.cn/view/47370">首篇潜空间推理综述！模型思考不必依赖Token，带宽暴增2700+倍 - 智源...</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#vision-language`, `#latent reasoning`, `#open source`, `#AI framework`

---

<a id="item-3"></a>
## [Anthropic 与 SpaceX 合作获得大规模 AI 算力提升](https://t.me/zaihuapd/41371) ⭐️ 8.0/10

Anthropic 宣布与 SpaceX 合作，获得 Colossus 1 数据中心的全部算力，立即将 Claude Code 付费方案的速率限制提升一倍，并取消了 Pro 和 Max 用户的高峰期限制。 此次合作为 Anthropic 带来了巨大的 GPU 算力增长——一个月内新增超过 22 万块 NVIDIA GPU 和 300 兆瓦容量——可大幅加速模型训练和推理，用户也直接受益于更高的 API 使用限额。 Colossus 1 数据中心最初为 xAI 建造，拥有超过 22 万块 GPU 的超级计算机；Anthropic 将租用其全部算力。速率限制调整立即生效，适用于 Claude Code 和 Claude Opus API。

telegram · zaihuapd · May 14, 00:57

**背景**: AI 公司需要巨大的计算资源来训练和运行大型语言模型。Colossus 1 是全球最大的 AI 超级计算机之一，位于田纳西州孟菲斯，由 SpaceX/xAI 运营。此次合作使 Anthropic 在全球 GPU 短缺的情况下获得了专属计算容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.datacenterdynamics.com/en/news/anthropic-to-use-all-of-spacex-xais-colossus-1-data-center-compute/">Anthropic to use all of SpaceX-xAI's Colossus 1 data center compute - DCD</a></li>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Claude`, `#Anthropic`, `#SpaceX`, `#GPU`

---