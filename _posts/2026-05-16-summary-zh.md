---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 33 items, 10 important content pieces were selected

---

1. [首个公开 Apple M5 内核内存破坏利用 5 天完成](#item-1) ⭐️ 10.0/10
2. [Pixel 10 零点击利用链披露](#item-2) ⭐️ 9.0/10
3. [arXiv 对未核查 LLM 内容禁投 1 年](#item-3) ⭐️ 9.0/10
4. [Mitchell Hashimoto 警告企业陷入“AI 精神病”](#item-4) ⭐️ 8.0/10
5. [Zulip 过渡到独立非营利基金会](#item-5) ⭐️ 8.0/10
6. [加州法案要求停服游戏提供补丁或退款](#item-6) ⭐️ 8.0/10
7. [美国司法部要求苹果和谷歌披露 10 万汽车改装应用用户](#item-7) ⭐️ 8.0/10
8. [O(x)Caml 太空应用：通过栈注解实现亚 10 纳秒包分发](#item-8) ⭐️ 8.0/10
9. [ABC 新闻移除所有 FiveThirtyEight 文章](#item-9) ⭐️ 8.0/10
10. [苹果与 OpenAI 合作关系紧张，可能面临法律诉讼](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [首个公开 Apple M5 内核内存破坏利用 5 天完成](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 10.0/10

Calif 与 AI 系统 Mythos Preview 合作，在 5 天内（2026 年 4 月 25 日至 5 月 1 日）构建了首个公开的针对 Apple M5 硬件的 macOS 内核内存破坏漏洞利用，实现了从非特权用户到 root shell 的本地提权。 这证明 AI 辅助的安全研究能在数天内攻破 Apple 的硬件级内存完整性保护（MIE），而 Apple 曾声称这是消费级操作系统史上最重要的内存安全升级。 该漏洞利用是纯数据型内核本地提权链，针对 M5 上的 macOS 26.4.1，仅使用正常系统调用并完全绕过 MIE。完整的 55 页技术报告将在 Apple 发布修复后公开。

telegram · zaihuapd · May 15, 02:15

**背景**: Apple M5 和 A19 芯片引入了内存完整性保护（MIE），这是一种软硬件协同设计，旨在阻止内存破坏漏洞利用，Apple 称这是消费级操作系统史上最重要的内存安全升级。Mythos Preview 是 Anthropic（Claude Mythos Preview）推出的一款有限访问 AI 模型，专为高级网络安全任务设计，包括漏洞发现和利用开发。Calif 是一个安全研究团队，与 Mythos Preview 合作实现了这一突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://cybernews.com/ai-news/mythos-ai-apple-m5-mac-security-expliot/">Mythos AI helps engineers crack Apple security| Cybernews</a></li>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory ...</a></li>

</ul>
</details>

**标签**: `#安全研究`, `#漏洞利用`, `#Apple M5`, `#AI辅助`, `#内核漏洞`

---

<a id="item-2"></a>
## [Pixel 10 零点击利用链披露](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero 披露了针对 Pixel 10 的完整零点击利用链，利用远程杜比音频解码漏洞（CVE-2025-54957）实现内核控制。 这展示了 AI 驱动的功能（如预读用户消息）所引入的额外攻击面，并强调了整个 Android 生态系统及时打补丁的紧迫性。 该利用链无需用户交互，且在 90 天内得到修复，这对于 Android 驱动漏洞来说相当迅速。该杜比漏洞在 2026 年 1 月修复前影响所有 Android 设备。

hackernews · happyhardcore · May 15, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48148460)

**背景**: Google Project Zero 是一个旨在发现零日漏洞的安全分析团队。零点击漏洞利用允许攻击者在无需用户交互的情况下入侵设备，通常通过发送恶意消息实现。像许多现代手机一样，Pixel 10 包含自动解码媒体（如音频）的 AI 功能以增强搜索和理解能力，这无意中增加了攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0-click exploit chain for the Pixel 10: When a Door Closes ...</a></li>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Project_Zero">Google Project Zero</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AI 功能增加攻击面表示担忧，并注意到这次 Android 漏洞的修复速度相对较快。一些用户将响应时间与苹果进行比较，并质疑披露漏洞的频率是否因 AI 炒作而增加。

**标签**: `#security`, `#exploit`, `#zero-click`, `#Android`, `#vulnerability`

---

<a id="item-3"></a>
## [arXiv 对未核查 LLM 内容禁投 1 年](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 9.0/10

arXiv 宣布新政策：含有未核查的 LLM 生成内容（如幻觉引用、元注释、占位数据）的投稿将被禁投 1 年，且禁投结束后需先经同行评审的 venue 接收才能重新提交。 该政策对涉及 AI 的学术不端行为建立了明确的震慑，为预印本平台树立了先例，可能重塑研究人员在论文准备中使用 LLM 的方式。 禁投适用于显示作者未核查的内容，如幻觉引用、LLM 留下的元注释（例如“作为一个 AI 语言模型”）、以及“表格数据仅为示例”等占位内容。禁投后，作者需先将论文被可信的同行评审 venue 接收，才能再次提交 arXiv。

telegram · zaihuapd · May 15, 04:30

**背景**: arXiv 是广泛使用的预印本库，研究人员在正式同行评审前分享论文。LLM 可能生成令人信服但错误的引用（幻觉）并留下意外的元注释，损害科学可信度。该政策针对这些失当行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific ... - Nature</a></li>
<li><a href="https://arxiv.org/abs/2605.07723">[2605.07723] LLM hallucinations in the wild: Large-scale ...</a></li>

</ul>
</details>

**标签**: `#arXiv`, `#LLM`, `#学术出版`, `#科研诚信`, `#AI伦理`

---

<a id="item-4"></a>
## [Mitchell Hashimoto 警告企业陷入“AI 精神病”](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

HashiCorp 联合创始人 Mitchell Hashimoto 发布警告，称许多公司正陷入“AI 精神病”状态，盲目信任 AI 进行决策和编码，缺乏关键性监督。 这一警告意义重大，因为过度依赖 AI 可能导致系统不稳定且难以维护，尤其是在企业规模扩大时；它也可能引发关于在软件工程中负责任地整合 AI 的必要讨论。 Hashimoto 的批评针对那些将思考外包给 AI 的公司，它们以 AI 代理能更快修复为借口发布有缺陷的代码，从而形成危险的反馈循环。

hackernews · reasonableklout · May 15, 20:26 · [社区讨论](https://news.ycombinator.com/item?id=48153379)

**背景**: Mitchell Hashimoto 是 DevOps 和基础设施领域的知名人物，共同创造了 Vagrant、Packer 和 Terraform 等工具。“AI 精神病”指的是不加人工验证就非理性地过度依赖 AI 输出，类似于群体思维。这种担忧在于，这种做法会损害代码质量和系统的长期健康。

**社区讨论**: 评论普遍赞同 Hashimoto 的观点，指出纯 AI 编写的系统规模扩大后会变得难以理解且不稳定。一些人认为，只要人类保持控制，使用 AI 编码是可以的，这与鲁莽迁移的故事形成对比。其他人预测，修复此类系统的“AI 救援咨询”将会兴起。

**标签**: `#AI`, `#software engineering`, `#risk`, `#technology criticism`

---

<a id="item-5"></a>
## [Zulip 过渡到独立非营利基金会](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

Zulip 宣布将过渡到一个独立的非营利基金会，核心团队成员退出全职领导岗位加入 Anthropic，以确保该平台的长期治理服务于公共利益。 此举回应了团队聊天中对供应商锁定和数据隐私日益增长的担忧，为开源可持续性树立了先例。可能会增强对商业聊天平台持怀疑态度的用户和社区的信任。 该基金会将是独立且非营利的，而四位高级团队成员离职加入 Anthropic 引发了关于持续性的疑问。公告于周五下午发布，一些观察者认为这是试图减少关注度的做法。

hackernews · boramalper · May 15, 18:37 · [社区讨论](https://news.ycombinator.com/item?id=48152168)

**背景**: Zulip 是一个开源团队聊天平台，以其独特的基于话题的线程功能而闻名，支持实时和异步对话。它与 Slack、Microsoft Teams 和 Discord 竞争。过渡到基金会的方式遵循了其他开源项目的模式，例如最近的 Bun/Rust 收购新闻，其中社区治理优先于商业控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zulip.com/">Zulip — organized team chat</a></li>
<li><a href="https://github.com/zulip/zulip">GitHub - zulip/zulip: Zulip server and web application. Open ... Zulip Chat: Open Source Alternative to Slack and Teams (2026 ... Zulip: The Open Source Alternative to Slack & Teams Zulip — organized team chat Self-host Zulip Zulip - GitHub</a></li>
<li><a href="https://www.almtoolbox.com/blog/zulip-chat-overview/">Zulip Chat: Open Source Alternative to Slack and Teams (2026 ...</a></li>

</ul>
</details>

**社区讨论**: 评论显示出混合的反应：一些用户对基金会感到兴奋并称赞 Zulip 的界面，而另一些则对时机持怀疑态度，并将其与 Bun 收购相提并论。一位评论者指出，在周五下午发布公告通常是不受欢迎消息的做法，但 Zulip 创始人澄清此举不可相提并论。

**标签**: `#zulip`, `#open-source`, `#foundation`, `#nonprofit`, `#chat`

---

<a id="item-6"></a>
## [加州法案要求停服游戏提供补丁或退款](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

加利福尼亚州议会法案 AB 1234 已通过关键委员会投票，要求游戏发行商在关闭在线游戏服务时，要么发布补丁使游戏可离线游玩，要么提供退款。 该法案可能为消费者权益和游戏保存开创先例，影响数百万玩家，迫使发行商在停止在线游戏服务时考虑长期支持或财务责任。 该法案仅通过订阅模式提供的游戏可获得豁免，且仅适用于在加利福尼亚销售的游戏。发行商必须在关闭前 60 天发出通知，并在 90 天内合规。

hackernews · Lihh27 · May 15, 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48152994)

**背景**: 许多在线游戏在服务器关闭后无法游玩，消费者无法追索。该法案由“停止杀死游戏”活动支持，旨在保留游戏功能并保护消费者。其他州和国家也提出了类似立法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/">Bill to block publishers from killing online games advances ...</a></li>
<li><a href="https://www.msn.com/en-us/gaming/general/california-bill-pushes-for-refunds-offline-versions-of-video-games/ar-AA22xyH0">California bill pushes for refunds, offline versions of video ...</a></li>
<li><a href="https://www.rockpapershotgun.com/california-bill-pushing-to-keep-games-playable-after-server-shutdowns-passes-key-hurdle-paving-way-for-full-assembly-vote">California bill pushing to keep games playable after server ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了不同观点：一些建议开源服务器代码作为公平解决方案，而另一些则担心独立开发者面临更大风险。一位正在关闭游戏的开发者提到运营成本高昂，另一位则质疑此类立法的可执行性。

**标签**: `#gaming`, `#consumer protection`, `#software preservation`, `#legislation`

---

<a id="item-7"></a>
## [美国司法部要求苹果和谷歌披露 10 万汽车改装应用用户](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

美国司法部已向苹果和谷歌发出传票，要求其披露超过 10 万名下载了一款可禁用排放控制装置的汽车改装应用的用户身份，作为排放打击行动的一部分。 这一行动引发了重大的隐私担忧，并为政府访问应用商店用户数据开创了潜在先例，影响到不仅限于排放相关应用的各种定制工具的数百万用户。 该应用据称用于 ECU 调校以修改车辆性能，包括禁用排放控制装置，这违反了《清洁空气法》。司法部声称需要用户信息来识别调查中的证人。

hackernews · tencentshill · May 15, 17:28 · [社区讨论](https://news.ycombinator.com/item?id=48151383)

**背景**: ECU 调校涉及修改车辆电子控制单元软件以改变性能参数，常被爱好者使用。但若用于禁用排放控制装置，则根据《清洁空气法》属于非法，类似于绕过排放测试的‘失效装置’。EPA 已将阻止售后失效装置列为优先事项，以减少空气污染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ECU_tuning">ECU tuning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Defeat_device">Defeat device - Wikipedia</a></li>
<li><a href="https://www.epa.gov/enforcement/national-enforcement-and-compliance-initiative-stopping-aftermarket-defeat-devices">National Enforcement and Compliance Initiative: Stopping Aftermarket Defeat Devices for Vehicles and Engines | US EPA</a></li>

</ul>
</details>

**社区讨论**: 评论反映出多种担忧：有人质疑政府为何在未掌握证据的情况下要求提供数据，也有人批评应用用户禁用排放控制装置。还有人担心这为其他形式的车辆改装（如禁用 GPS 追踪）开创先例，并担忧应用分发的集中化问题。

**标签**: `#privacy`, `#government surveillance`, `#app distribution`, `#digital rights`, `#emissions regulations`

---

<a id="item-8"></a>
## [O(x)Caml 太空应用：通过栈注解实现亚 10 纳秒包分发](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

一篇博客文章揭示，使用 OCaml 并配合 exclave_ 栈注解，可将数据包分发的 p99.9 延迟从 29 纳秒降至 9 纳秒，并在处理 2500 万个数据包时完全消除 GC 压力。 这表明像 OCaml 这样的垃圾收集语言可以实现对太空应用至关重要的实时性能，可能扩大其在嵌入式和高性能系统中的采用。 这一改进通过添加类型注解来减少堆分配，使得在 2500 万个数据包上的次要 GC 次数从 394 次降为零，同时吞吐量保持不变。该工作基于 OCaml 最近的局部/栈分配特性。

hackernews · yminsky · May 15, 10:55 · [社区讨论](https://news.ycombinator.com/item?id=48147058)

**背景**: OCaml 是一种使用垃圾收集的函数式语言，传统上依赖堆分配。栈注解允许某些值在调用栈上分配，从而减少 GC 开销并改善延迟。太空软件通常要求确定性性能和低延迟，而这正是 GC 语言历来面临的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cs3110.github.io/textbook/ocaml_programming.pdf">OCaml Programming: Correct + Efficient + Beautiful</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，早在 2016 年，OCaml 就已在 GHGSat-D 上用于太空，并对 GC 改进表示赞赏。关于内存安全与栈注解的优劣存在讨论，并与其他 GC 语言（如 Java）在高频交易场景中的应用进行了比较。

**标签**: `#OCaml`, `#space`, `#performance`, `#GC`, `#embedded systems`

---

<a id="item-9"></a>
## [ABC 新闻移除所有 FiveThirtyEight 文章](https://twitter.com/baseballot/status/2055309076209492208) ⭐️ 8.0/10

ABC 新闻已将 FiveThirtyEight 的所有文章下线，实际上删除了这个数据驱动新闻网站的全部存档。 这标志着一个著名数据新闻品牌的终结，移除了被研究人员和公众广泛引用的关于民调、体育和数据可视化的宝贵资源。 移除的内容包括备受赞誉的互动可视化作品，如枪击死亡可视化和 p-hacking 文章。在迪士尼几轮成本削减后，ABC 新闻此前已裁减了 FiveThirtyEight 的大部分员工。

hackernews · cmsparks · May 15, 19:07 · [社区讨论](https://news.ycombinator.com/item?id=48152553)

**背景**: FiveThirtyEight 由 Nate Silver 于 2008 年创立，以对政治和体育的统计分析而闻名。它于 2013 年被 ESPN（迪士尼）收购，随后并入 ABC 新闻。该网站的数据驱动方法和独特的可视化使其成为选举报道和解释性新闻的重要平台。

**社区讨论**: 评论者表达了对 ABC 品牌管理不善的不满，指出 FiveThirtyEight 在专业人士中是一个知名品牌，其移除浪费了宝贵的内容。还有人提到 Nate Silver 曾试图回购知识产权但被拒绝，并敦促在 GitHub 仓库也被删除前进行备份。

**标签**: `#journalism`, `#data visualization`, `#media`, `#brand management`, `#technology`

---

<a id="item-10"></a>
## [苹果与 OpenAI 合作关系紧张，可能面临法律诉讼](https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight) ⭐️ 8.0/10

苹果与 OpenAI 的合作关系恶化，OpenAI 因订阅目标未达成和战略分歧正考虑采取法律行动。 这可能重塑消费产品中的 AI 集成格局，因为苹果计划向 Claude、Gemini 等其他 AI 模型开放 Siri，削弱 OpenAI 的独家地位。 OpenAI 声称 ChatGPT 在苹果生态系统中的集成入口隐蔽且功能受限，导致订阅转化率远低于预期；苹果也对 OpenAI 的隐私标准和挖角工程师感到不满。

telegram · zaihuapd · May 15, 12:59

**背景**: 苹果曾与 OpenAI 合作将 ChatGPT 集成到 Siri 中，期望获得可观的订阅收入。然而，集成面临采用问题。另外，苹果计划在 iOS 27 中让 Siri 使用其他 AI 模型，如 Anthropic 的 Claude 和谷歌的 Gemini。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Apple`, `#AI partnership`, `#legal action`, `#ChatGPT`

---