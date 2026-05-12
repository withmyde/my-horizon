---
layout: default
title: "Horizon Summary: 2026-05-12 (EN)"
date: 2026-05-12
lang: en
---

> From 31 items, 8 important content pieces were selected

---

1. [TanStack npm supply-chain attack with dead-man's switch](#item-1) ⭐️ 9.0/10
2. [UCLA discovers first drug to repair brain damage after stroke](#item-2) ⭐️ 9.0/10
3. [Nvidia releases CUDA-oxide, official Rust-to-CUDA compiler](#item-3) ⭐️ 9.0/10
4. [Ratty: A GPU-accelerated terminal with inline 3D graphics](#item-4) ⭐️ 8.0/10
5. [AI may shorten software engineering careers, but debate rages](#item-5) ⭐️ 8.0/10
6. [AI Coding Agents Must Slash Maintenance Costs Proportionally](#item-6) ⭐️ 8.0/10
7. [Fake OpenAI Privacy Filter on Hugging Face Hits #1 Trend](#item-7) ⭐️ 8.0/10
8. [Study: AI models reject Black users at higher rates](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TanStack npm supply-chain attack with dead-man's switch](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 9.0/10

TanStack's npm packages were compromised in a supply-chain worm that installed a dead-man's switch, which would execute `rm -rf ~/` if the stolen GitHub token was revoked. This attack demonstrates a sophisticated supply-chain compromise on a widely used library, with a destructive dead-man's switch that punishes defenders. It underscores critical weaknesses in npm's security model and token management. The dead-man's switch was implemented as a systemd user service on Linux or a LaunchAgent on macOS, polling GitHub API every 60 seconds with the stolen token. If the token is revoked (HTTP 40x), it triggers `rm -rf ~/`. npm's 'no unpublish if dependents exist' policy delayed mitigation.

hackernews · varunsharma07 · May 11, 21:08 · [Discussion](https://news.ycombinator.com/item?id=48100706)

**Background**: Supply-chain attacks occur when attackers compromise a legitimate package to distribute malware to its users. A dead-man's switch is a mechanism that triggers a destructive action when a specific condition (like token revocation) is met. The TanStack incident is part of a broader wave of npm attacks involving the Shai-Hulud malware strain.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberpress.org/dead-mans-switch-widespread-npm-supply-chain-attack-driving-malware-attacks/">Dead Man’s Switch: Widespread npm Supply Chain Attack Driving ...</a></li>
<li><a href="https://www.trendmicro.com/en_us/research/25/i/npm-supply-chain-attack.html">What We Know About the NPM Supply Chain Attack | Trend Micro (US)</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem | CISA</a></li>

</ul>
</details>

**Discussion**: Community members warned about the danger of revoking tokens without first removing the dead-man's switch, and highlighted that the mistralai package was also compromised. Some argued that npm's unpublish policy and GitHub's allowance of malicious commits from forks exacerbated the attack, while others noted that postinstall scripts remain a major risk.

**Tags**: `#security`, `#npm`, `#supply-chain`, `#malware`, `#postmortem`

---

<a id="item-2"></a>
## [UCLA discovers first drug to repair brain damage after stroke](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

UCLA researchers have identified the first drug that can repair brain damage after a stroke by targeting the disconnection in surviving neural networks, rather than dead tissue. The compound, referenced in community comments as linked to a 2024 PubMed study, aims to restore lost rhythmic communication between distant brain regions. This breakthrough could transform stroke rehabilitation by offering the first pharmacological option to promote functional recovery, potentially benefiting millions of stroke survivors worldwide. It shifts the focus from cell death to network disconnection, opening new avenues for brain repair therapies. The drug targets 'disconnection syndromes'—disrupted neural networks in surviving brain tissue—rather than the infarct core where cells have died. The specific compound was mentioned in a comment linking to a 2024 PubMed study (PMID: 39106304), though UCLA's official publication may provide further details.

hackernews · bookofjoe · May 11, 17:53 · [Discussion](https://news.ycombinator.com/item?id=48098261)

**Background**: Strokes cause brain damage through cell death and disruption of neural networks, leading to lasting impairments. Traditional rehabilitation focuses on compensating for lost function, but the brain has limited ability to repair itself. UCLA's approach targets the 'disconnection' in surviving networks, aiming to restore communication and rhythm between brain regions, which is a novel strategy in stroke therapy.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12651463/">Reconnecting Brain Networks After Stroke: A Scoping Review of ...</a></li>
<li><a href="https://www.frontiersin.org/journals/stroke/articles/10.3389/fstro.2025.1643570/full">Disconnection syndromes and injury to neural systems after ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the distinction between cell death and network disconnection, with users noting that recovery from 'bruised' cells is possible. Some discuss parallels with psychedelics that reopen critical periods for neuroplasticity, while others reference Neuralink or express surprise inspired by Ted Chiang's story 'Understand'. A user linked a specific 2024 PubMed study as the compound in question.

**Tags**: `#stroke`, `#rehabilitation`, `#brain repair`, `#UCLA`, `#drug discovery`

---

<a id="item-3"></a>
## [Nvidia releases CUDA-oxide, official Rust-to-CUDA compiler](https://nvlabs.github.io/cuda-oxide/index.html) ⭐️ 9.0/10

Nvidia Labs has released CUDA-oxide 0.1, an experimental compiler that translates standard Rust code directly to PTX, enabling GPU programming without DSLs or foreign language bindings. CUDA-oxide allows Rust developers to write GPU kernels using familiar Rust syntax and safety guarantees, potentially improving productivity and code reliability in GPU computing. This could also influence the broader GPU programming ecosystem by offering a modern alternative to CUDA C++. The compiler targets PTX (Parallel Thread Execution), NVIDIA's low-level GPU instruction set, avoiding the need for nvcc or CMake during compilation. It is labeled as experimental and focuses on safe-ish programming, meaning it supports unsafe code where necessary.

hackernews · adamnemecek · May 11, 15:55 · [Discussion](https://news.ycombinator.com/item?id=48096692)

**Background**: GPU programming traditionally relies on CUDA C++ or domain-specific languages (DSLs) like Slang, which require learning new syntax and toolchains. Rust offers memory safety and modern language features but lacked official GPU support. CUDA-oxide bridges this gap by allowing Rust to compile directly to PTX, leveraging Rust's type system and safety guarantees while maintaining high performance for GPU kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVlabs/cuda-oxide">GitHub - NVlabs/cuda-oxide: cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.</a></li>
<li><a href="https://nvlabs.github.io/cuda-oxide/index.html">The cuda-oxide Book — cuda-oxide</a></li>
<li><a href="https://www.phoronix.com/news/NVIDIA-CUDA-Oxide-0.1">NVIDIA Releases CUDA-Oxide 0.1 For Experimental Rust-To-CUDA Compiler - Phoronix</a></li>

</ul>
</details>

**Discussion**: The community expressed excitement about the potential for Rust in GPU programming, with users curious about build times compared to traditional CUDA toolchains and how the Rust memory model maps to CUDA semantics. Some wondered about the implications for other GPU languages like Slang, while others questioned the choice of targeting PTX directly instead of using NVIDIA's MLIR or Tile IR.

**Tags**: `#rust`, `#cuda`, `#gpu-programming`, `#nvidia`, `#compiler`

---

<a id="item-4"></a>
## [Ratty: A GPU-accelerated terminal with inline 3D graphics](https://ratty-term.org/) ⭐️ 8.0/10

Ratty is a newly released GPU-rendered terminal emulator that supports inline 3D graphics, allowing users to embed 3D objects directly within the terminal using its own protocol, the Ratty Graphics Protocol (RGP). This innovation pushes the boundaries of traditional text-only terminals, potentially enabling richer development environments and data visualization directly in the terminal, and has sparked significant community interest as a step towards modernizing the terminal experience. Ratty is built with Rust and Ratatui, and its RGP supports registering .obj and .glb assets, placing them at terminal cell anchors, and controlling animation, scale, color, and depth. It is inspired by TempleOS and features a spinning rat cursor.

hackernews · orhunp_ · May 11, 10:13 · [Discussion](https://news.ycombinator.com/item?id=48093100)

**Background**: Traditional terminal emulators display text and simple graphics via escape sequences, but 3D graphics have been limited. Ratty leverages GPU acceleration to render 3D objects inline, building on protocols like Kitty's graphics protocol. Its approach echoes earlier systems like Xerox workstations and Lisp machines that had inline graphics in REPL environments.

<details><summary>References</summary>
<ul>
<li><a href="https://ratty-term.org/">Ratty — A GPU-rendered terminal emulator with inline 3 D graphics</a></li>
<li><a href="https://github.com/orhun/ratty">GitHub - orhun/ratty: A GPU-rendered terminal emulator with inline ...</a></li>
<li><a href="https://blog.orhun.dev/introducing-ratty/">Ratty : A terminal emulator with inline 3D graphics - Orhun's Blog</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive, with commendation for innovation and comparisons to historical systems like Xerox workstations and Lisp machines. Some users raised questions about the limitations of 2D rendering via this approach, performance over SSH, and whether this signals the terminal evolving into a full web browser.

**Tags**: `#terminal emulator`, `#3D graphics`, `#innovation`, `#REPL`, `#Hacker News`

---

<a id="item-5"></a>
## [AI may shorten software engineering careers, but debate rages](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/) ⭐️ 8.0/10

A blog post argues that AI, particularly LLMs, may reduce the longevity of software engineering careers, sparking a heated discussion on whether coding ability defines engineering. This debate reflects deep uncertainty in the software industry about AI's impact on jobs, affecting career planning, hiring practices, and the definition of engineering competence. Commenters distinguish between 'writing code' (2-5% of work) and broader engineering activities like understanding systems and formulating solutions. Critics warn that over-reliance on AI may cause technical skill atrophy.

hackernews · movis · May 11, 14:34 · [Discussion](https://news.ycombinator.com/item?id=48095550)

**Background**: Software engineering involves far more than coding, including requirements analysis, system design, debugging, and collaboration. AI tools like LLMs can generate code, but they lack understanding of business logic and system context, leading to debates about their true impact on the profession.

**Discussion**: Commenters overwhelmingly agree that coding is only a small part of software engineering, with one noting coding takes 2-5% of their time. Many express concern that AI reliance could erode problem-solving skills, while others argue experienced engineers using AI become more productive. The sentiment is cautiously optimistic but warns against conflating coding with engineering.

**Tags**: `#AI`, `#software engineering`, `#career`, `#LLM`, `#future of work`

---

<a id="item-6"></a>
## [AI Coding Agents Must Slash Maintenance Costs Proportionally](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 8.0/10

James Shore argues that AI coding agents must reduce maintenance costs by the same factor they boost code output, or teams will face unsustainable debt. He provides a mathematical model showing that doubling code output without halving maintenance costs quadruples total maintenance burden. This insight highlights a critical hidden cost of AI-assisted development: if teams only focus on speed gains, they may inadvertently accumulate crippling long-term maintenance debt. It reframes the productivity conversation from pure output to sustainable total cost of ownership. In Shore's example, each month of coding generates 10 days of maintenance in the first year and 5 days yearly thereafter. Doubling code output without reducing maintenance costs per unit could multiply total maintenance costs by four, based on his formula.

rss · Simon Willison · May 11, 19:48

**Background**: Software maintenance costs—including bug fixes, updates, and refactoring—often exceed initial development costs over a project's lifetime. AI coding agents dramatically accelerate code generation but rarely produce code that is inherently easier to maintain, potentially increasing the maintenance burden if not carefully managed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs">James Shore: You Need AI That Reduces Maintenance Costs</a></li>
<li><a href="https://simonwillison.net/2026/May/11/james-shore/">A quote from James Shore - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#software maintenance`, `#productivity`, `#software engineering economics`

---

<a id="item-7"></a>
## [Fake OpenAI Privacy Filter on Hugging Face Hits #1 Trend](https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html) ⭐️ 8.0/10

A malicious Hugging Face repository named 'Open-OSS/privacy-filter' impersonated an OpenAI privacy filter and delivered a Rust-based infostealer, peaking at the #1 trending spot with approximately 244,000 downloads before being taken down. This supply-chain attack on Hugging Face highlights the risk of malicious models in AI/ML repositories, potentially affecting thousands of users, and the link to the Silver Fox hacker group indicates a broader, well-funded campaign targeting AI developers. HiddenLayer discovered six additional similar malicious repositories, and the same infrastructure previously distributed ValleyRAT remote access trojan; the repository's download count and likes may have been artificially inflated.

telegram · zaihuapd · May 11, 12:51

**Background**: Hugging Face is a popular platform for hosting and sharing machine learning models, and supply-chain attacks on such platforms involve uploading malicious models that execute harmful code when loaded. The Silver Fox group is a China-based cybercrime group known for deploying trojans like ValleyRAT.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zscaler.com/blogs/security-research/technical-analysis-latest-variant-valleyrat">New Updates to ValleyRAT | ThreatLabz - Zscaler</a></li>
<li><a href="https://www.trustwave.com/en-us/resources/blogs/trustwave-blog/inside-silver-foxs-den-trustwave-spiderlabs-unmasks-a-global-threat-actor/">Inside Silver Fox’s Den: Trustwave SpiderLabs Unmasks a Global Threat Actor</a></li>
<li><a href="https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html">Silver Fox Deploys ABCDoor Malware via Tax-Themed Phishing in India and Russia</a></li>

</ul>
</details>

**Tags**: `#security`, `#malware`, `#Hugging Face`, `#supply chain attack`, `#OpenAI`

---

<a id="item-8"></a>
## [Study: AI models reject Black users at higher rates](https://cybernews.com/ai-news/ai-chatbots-refuse-black-users/) ⭐️ 8.0/10

A study by the University of Washington found that models like Google's Gemma-3-12B and Alibaba's Qwen-3-VL-8B are four times more likely to refuse prompts from users who explicitly identify as Black, compared to white users. When users wrote in African American English without mentioning race, the refusal rate dropped nearly to zero. This research exposes a critical fairness flaw in AI safety systems, showing that explicit racial keywords trigger disproportionate refusals while failing to recognize African American English. It highlights the need for more inclusive training data and bias mitigation in large language models. The study focused on two models: Google's Gemma-3-12B, a multimodal model with 12 billion parameters and 128k context window, and Alibaba's Qwen-3-VL-8B, a vision-language model. It found that the refusal rate for Black-identifying users was about 7.5 percentage points higher, and that African American English constitutes only 0.007% of training data.

telegram · zaihuapd · May 12, 01:00

**Background**: Large language models (LLMs) are often trained predominantly on Standard American English (SAE), leading to underrepresentation of dialects like African American English (AAE). Bias in NLP systems can cause misclassification of AAE as toxic or offensive, which may contribute to higher refusal rates for Black users. The study highlights that safety systems are overly sensitive to explicit racial keywords while not recognizing the linguistic patterns of AAE, creating an 'identity penalty'.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/models/google/gemma-3-12b">google/ gemma - 3 - 12 b • LM Studio</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct">Qwen/Qwen3-VL-8B-Instruct · Hugging Face</a></li>
<li><a href="https://scholar.smu.edu/datasciencereview/vol9/iss3/9/">"NLP Bias and African American English" by Kenya Roy and ...</a></li>

</ul>
</details>

**Tags**: `#AI bias`, `#fairness`, `#language models`, `#safety systems`

---