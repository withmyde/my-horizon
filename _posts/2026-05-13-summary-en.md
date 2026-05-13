---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 35 items, 11 important content pieces were selected

---

1. [CERT Releases Six CVEs for Serious dnsmasq Vulnerabilities](#item-1) ⭐️ 9.0/10
2. [Unitree Unveils First Mass-Produced Manned Transforming Mech](#item-2) ⭐️ 9.0/10
3. [Needle: 26M Parameter Tool-Calling Model Runs on Consumer Devices](#item-3) ⭐️ 8.0/10
4. [DuckDB Unveils Quack Protocol for Client-Server Setup](#item-4) ⭐️ 8.0/10
5. [Rendering Realistic Skies and Planets with Atmospheric Scattering](#item-5) ⭐️ 8.0/10
6. [Bambu Lab Accused of Abusing Open Source Social Contract](#item-6) ⭐️ 8.0/10
7. [Canada's Bill C-22: Repackaged Surveillance Threat](#item-7) ⭐️ 8.0/10
8. [Hashimoto: Technical decision makers avoid risk, follow trends](#item-8) ⭐️ 8.0/10
9. [Anthropic Denies Chinese Think Tank Access to Latest AI Model](#item-9) ⭐️ 8.0/10
10. [US Commerce Dept. Deletes AI Safety Test Agreement Details](#item-10) ⭐️ 8.0/10
11. [Samsung union protests slash chip output, threaten global supply](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [CERT Releases Six CVEs for Serious dnsmasq Vulnerabilities](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT has disclosed six Common Vulnerabilities and Exposures (CVEs) for serious security vulnerabilities in the dnsmasq DNS/DHCP server, a widely used lightweight network service. dnsmasq is embedded in numerous routers, IoT devices, and Linux distributions; these vulnerabilities could allow remote code execution or denial of service, affecting millions of devices. This highlights the ongoing risks of memory-unsafe languages in critical network infrastructure. The specific CVEs have not been published yet, but based on community discussion, the vulnerabilities are likely memory-safety issues such as buffer overflows. The disclosure is pending further details from the dnsmasq maintainers.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: dnsmasq is a lightweight DNS forwarder and DHCP server designed for resource-constrained environments like routers and firewalls. It is part of many open-source projects including OpenWrt and Pi-hole. CERT (Computer Emergency Response Team) coordinates vulnerability disclosures and provides guidance on mitigation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">dnsmasq - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/Dnsmasq">dnsmasq - ArchWiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_emergency_response_team">Computer emergency response team - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed urgency to replace C-based software with memory-safe languages like Rust or Go, citing these CVEs as a breaking point. Some criticized Debian's slow update policy and backporting practices, while others defended dnsmasq's importance and noted that not all users will abandon it despite the vulnerabilities.

**Tags**: `#security`, `#dnsmasq`, `#CVE`, `#memory-safety`, `#networking`

---

<a id="item-2"></a>
## [Unitree Unveils First Mass-Produced Manned Transforming Mech](https://m.mydrivers.com/newsview/1121657.html) ⭐️ 9.0/10

Unitree Technology has unveiled the GD01, the world's first mass-produced manned transforming mech, with a starting price of 3.9 million yuan (approx. $540,000). This marks a milestone in commercializing advanced robotics for civilian use, combining walking, transforming, and manned capabilities in a mass-produced vehicle. It could pave the way for new applications in tourism, special operations, and high-end personal transportation. The GD01 weighs approximately 500 kg, uses high-strength alloys and precision servo drives, and can walk upright while carrying passengers or transform into a quadruped state. Demo videos show it can punch through a brick wall with one fist.

telegram · zaihuapd · May 12, 05:25

**Background**: Unitree is a Chinese robotics company best known for its quadruped robots like the Go1 and B2. Transforming mechs combine humanoid and animal-like locomotion, offering flexibility for complex terrains. The GD01 uses precision servo drives for smooth motion and is powered by aerospace-grade batteries for high energy density.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sohu.com/a/993362742_121124371">Triamec 100kHz 超精密伺服驱动器：重新定义运动控制</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#transforming mech`, `#Unitree`, `#manned vehicle`, `#civilian transport`

---

<a id="item-3"></a>
## [Needle: 26M Parameter Tool-Calling Model Runs on Consumer Devices](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus released Needle, an open-source 26M parameter model distilled from Gemini for efficient tool calling, achieving 6000 tok/s prefill and 1200 tok/s decode on consumer devices. This demonstrates that tiny models can handle tool calling effectively, potentially enabling on-device AI agents on phones, watches, and glasses without relying on cloud APIs. The model uses a Simple Attention Network architecture without MLPs, trained on 200B tokens pre-training and 2B tokens of synthesized function-calling data. It beats several larger models on single-shot function calling but has limitations in conversational settings.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Tool calling (function calling) allows AI models to interact with external APIs and services by outputting structured JSON. Traditional large language models dedicate substantial parameters to factual knowledge, but for tool use, the model primarily needs to match input to tool names and extract arguments—a retrieval task. The 'Simple Attention Network' removes feed-forward layers entirely, relying on attention and gating, which proves sufficient when external knowledge is provided in the input.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md">needle/docs/ simple _ attention _ networks .md at main...</a></li>

</ul>
</details>

**Discussion**: Community members expressed interest in testing the model's discriminatory power, suggested using it for command-line argument parsing, and requested a live demo playground. Others praised the push for tiny models and noted that the '26M' versus '0.026B' notation can be confusing.

**Tags**: `#machine-learning`, `#tool-calling`, `#tiny-models`, `#open-source`, `#efficiency`

---

<a id="item-4"></a>
## [DuckDB Unveils Quack Protocol for Client-Server Setup](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB announced Quack, a remote protocol that enables DuckDB instances to communicate, allowing client-server deployments with multiple concurrent writers. Quack transforms DuckDB from a single-user embedded database into a multi-user system capable of horizontal scaling, opening up new use cases like shared analytics and concurrent read/write workloads. The Quack protocol is simple to set up and builds on proven technologies, supporting multiple concurrent writers within a client-server architecture.

hackernews · aduffy · May 12, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48111765)

**Background**: DuckDB is a high-performance embedded analytics database traditionally used as a single-user, in-process library. Without a client-server protocol, each process accessed the database individually, preventing concurrent writes and remote access. Quack addresses these limitations by enabling DuckDB instances to communicate over a network.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack: The DuckDB Client - Server Protocol – DuckDB</a></li>
<li><a href="https://news.ycombinator.com/item?id=48111765">Quack: The DuckDB Client-Server Protocol | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community reacted positively, with users sharing practical use cases such as piping sensor data into DuckDB and scaling internal apps. Some expressed uncertainty about DuckDB's evolving identity, while others praised the simplicity and timeliness of Quack.

**Tags**: `#DuckDB`, `#database`, `#client-server`, `#protocol`, `#scalability`

---

<a id="item-5"></a>
## [Rendering Realistic Skies and Planets with Atmospheric Scattering](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

Maxime Heckel published a detailed blog post exploring real-time rendering of skies, sunsets, and planets using shaders and atmospheric scattering techniques like Rayleigh and Mie scattering. This deep dive provides valuable technical insights for graphics programmers and game developers, advancing accessible real-time rendering of atmospheric effects in web browsers. The article covers techniques from simple sky domes to entire planets, using raymarching, Rayleigh and Mie scattering, and ozone absorption.

hackernews · ibobev · May 12, 13:26 · [Discussion](https://news.ycombinator.com/item?id=48107997)

**Background**: Atmospheric scattering, including Rayleigh scattering (causing blue sky) and Mie scattering (causing haze), determines sky colors. Real-time rendering of these effects requires approximations for performance, often using precomputed data or simplified physics models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Atmospheric_scattering">Atmospheric scattering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rayleigh_scattering">Rayleigh scattering - Wikipedia</a></li>
<li><a href="https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/">On Rendering the Sky, Sunsets, and Planets - The Blog of Maxime Heckel</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the article, with references to Sebastian Lague's video on atmospheres and an observation about the sunset model lacking twilight. Others shared links to related work and noted the capability of modern mobile browsers.

**Tags**: `#graphics programming`, `#atmospheric scattering`, `#real-time rendering`, `#computer graphics`, `#game development`

---

<a id="item-6"></a>
## [Bambu Lab Accused of Abusing Open Source Social Contract](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/) ⭐️ 8.0/10

Bambu Lab faces backlash for implementing restrictive measures on its 3D printers, such as blocking third-party clients via user-agent checks, under the guise of security, which critics argue violates the open source social contract. This controversy highlights the tension between corporate control and open source ethics in the 3D printing ecosystem, potentially affecting user trust and the broader movement toward open hardware and software. Bambu Lab's changes reportedly include blocking non-official clients by checking user-agent strings, and requiring all print data to pass through their servers, citing outage risks from unauthorized traffic.

hackernews · rubenbe · May 12, 14:54 · [Discussion](https://news.ycombinator.com/item?id=48109224)

**Background**: The open source social contract refers to the unwritten agreement that users of open source software have the freedom to use, modify, and share it. Bambu Lab initially used open source components like OrcaSlicer but later imposed restrictions, leading to accusations of abusing this trust. The 3D printing community values openness, and such actions are seen as a betrayal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/">Bambu Lab is abusing the open source social contract - Jeff Geerling</a></li>

</ul>
</details>

**Discussion**: Community commenters express strong disapproval, with some noting Bambu Lab's history of backtracking under pressure (e.g., LAN mode). Others criticize the security argument as weak, pointing out that user-agent checks are not authentication. There is speculation about data privacy concerns due to Chinese government ties.

**Tags**: `#open source`, `#3d printing`, `#controversy`, `#community backlash`, `#corporate behavior`

---

<a id="item-7"></a>
## [Canada's Bill C-22: Repackaged Surveillance Threat](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare) ⭐️ 8.0/10

Canada's Bill C-22 proposes mandatory data retention and encryption backdoors, threatening encrypted messaging services. This repackaged legislation revives last year's surveillance proposal with similar requirements. If passed, encrypted services like Signal and WhatsApp may be forced to block Canadian users or break end-to-end encryption, undermining privacy for millions. This sets a dangerous precedent for other countries considering similar surveillance laws. The bill requires tech companies to store user metadata for one year and create encryption backdoors for law enforcement access. Major companies like Apple and Meta have warned they may withdraw services rather than comply.

hackernews · Brajeshwar · May 12, 17:35 · [Discussion](https://news.ycombinator.com/item?id=48111531)

**Background**: An encryption backdoor is a deliberate vulnerability that allows third parties (e.g., law enforcement) to access encrypted communications. Mandatory data retention forces companies to keep user metadata for extended periods. Both measures are widely criticized by privacy advocates for weakening security and enabling mass surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.internetsociety.org/blog/2025/05/what-is-an-encryption-backdoor/">What Is an Encryption Backdoor? - Internet Society</a></li>
<li><a href="https://cambridgeanalytica.org/surveillance-privacy/canada-bill-c-22-encryption-backdoor-apple-meta-50971/">Apple and Meta just warned Canada 's Bill C - 22 would force them to...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed alarm and frustration, with many calling for public opposition. Some argued that such legislation drives innovation in censorship-resistant tools, while others noted a concerning trend of multiple anti-privacy bills appearing simultaneously.

**Tags**: `#privacy`, `#encryption`, `#surveillance`, `#Canada`, `#digital rights`

---

<a id="item-8"></a>
## [Hashimoto: Technical decision makers avoid risk, follow trends](https://simonwillison.net/2026/May/12/mitchell-hashimoto/#atom-everything) ⭐️ 8.0/10

Mitchell Hashimoto criticized technical decision makers as primarily motivated by not getting fired, following analyst trends like AI strategy instead of genuine innovation. This insight highlights a widespread risk-averse culture in technical leadership that stifles innovation and drives purchasing decisions based on hype rather than value. Hashimoto noted 90% of Technical Decision Makers (TDMs) work 9-to-5 and never think about work outside hours, relying on analyst reports like Gartner and McKinsey to justify purchases such as 'Context Engine for AI Apps.'

rss · Simon Willison · May 12, 22:21

**Background**: Mitchell Hashimoto is a prominent software engineer and co-founder of HashiCorp, known for tools like Vagrant and Terraform. His comment was made on Lobsters, a tech-focused social news site, in response to a discussion about the Redis homepage design. Technical Decision Makers (TDMs) are individuals in organizations who influence or decide on technology purchases, often prioritizing job security over bold choices.

**Tags**: `#software-engineering`, `#decision-making`, `#management`, `#risk-aversion`, `#industry-trends`

---

<a id="item-9"></a>
## [Anthropic Denies Chinese Think Tank Access to Latest AI Model](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html) ⭐️ 8.0/10

Anthropic rejected a request from a Chinese think tank to access its latest AI model during a conference in Singapore, prompting concern from the US National Security Council. This incident highlights the escalating US-China tech competition and the increasing national security scrutiny on AI model access by foreign entities. The request was made by a representative of a Chinese think tank at a conference organized by the Carnegie Endowment for International Peace, and while not an official Chinese government request, it alarmed the White House.

telegram · zaihuapd · May 12, 12:57

**Background**: US AI companies like Anthropic and OpenAI have been at the forefront of developing advanced AI models. The US government has increasingly viewed the transfer of such technology to China as a national security risk, given the potential military and surveillance applications.

**Tags**: `#AI`, `#geopolitics`, `#Anthropic`, `#China`, `#national security`

---

<a id="item-10"></a>
## [US Commerce Dept. Deletes AI Safety Test Agreement Details](https://www.reuters.com/legal/litigation/microsoft-google-xai-security-test-details-deleted-us-government-website-2026-05-11/) ⭐️ 8.0/10

The US Commerce Department quietly removed web pages detailing agreements with Google, xAI, and Microsoft for pre-release safety testing of AI models. The deleted pages originally described the terms for government scientists to evaluate new AI models before public deployment. This deletion raises concerns about transparency and potential shifts in AI regulation policy. It undermines public trust in the government's oversight of frontier AI safety and affects how companies and stakeholders perceive the commitment to open AI governance. The removed pages concerned agreements with the Center for AI Standards and Innovation (CAISI). The original links now redirect to CAISI's website, but no official explanation was provided for the deletion.

telegram · zaihuapd · May 12, 13:38

**Background**: The US AI Safety Institute was renamed to the Center for AI Standards and Innovation (CAISI) in June 2025 under the Commerce Department. CAISI's role includes conducting safety testing of frontier AI models before public release. These agreements were part of a broader government effort to evaluate AI risks. The deletion of these details occurs amid ongoing debates about AI regulation transparency and government accountability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-before-release.html">US government agency to safety test frontier AI models before ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Center_for_AI_Standards_and_Innovation">Center for AI Standards and Innovation</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#government policy`, `#tech regulation`, `#transparency`

---

<a id="item-11"></a>
## [Samsung union protests slash chip output, threaten global supply](https://t.me/zaihuapd/41355) ⭐️ 8.0/10

Samsung Electronics' largest union reported that chip production at its South Korean facilities dropped sharply during the Thursday night shift due to mass walkouts for a wage protest. Foundry and memory chip output fell by 58% and 18%, respectively. This disruption from Samsung, a dominant player in global semiconductor manufacturing, could exacerbate supply chain tightness for memory and foundry chips. If a full strike occurs on May 21, it may severely impact industries relying on these components, from electronics to automotive. The walkout targeted the 10 p.m. to 6 a.m. shift, with union leadership threatening an 18-day total strike starting May 21 unless demands for higher base pay and removal of bonus caps are met.

telegram · zaihuapd · May 13, 01:11

**Background**: Samsung Electronics is the world's largest memory chip maker and a major foundry contractor. Labor disputes have been escalating over pay and bonuses. A prolonged strike at Samsung would be unprecedented and could ripple through global electronics supply chains, given the company's central role in producing DRAM, NAND flash, and logic chips.

**Tags**: `#Samsung`, `#semiconductor`, `#supply chain`, `#labor dispute`, `#chip production`

---