# Tommy983398/Horizon 部署指南

## 概述

本项目是基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 的定制版本，增加了以下功能：

1. **arXiv 论文抓取**：每天自动抓取 5 篇 cs.AI 分类的最新论文
2. **增强订阅系统**：通过邮件标题 SUBSCRIBE/UNSUBSCRIBE 进行订阅/退订，带确认邮件
3. **每日定时推送**：北京时间每天 08:00 自动运行并发送邮件

---

## 快速开始

### 步骤 1：Fork 项目到你的 GitHub 账号

```
1. 访问 https://github.com/Thysrael/Horizon
2. 点击右上角 "Fork" 按钮
3. 选择你的账号 (Tommy983398) 作为目标
4. 等待 Fork 完成
```

### 步骤 2：配置 GitHub Actions Secrets

在 Fork 后的仓库中，进入 **Settings → Secrets and variables → Actions**，添加以下 Secrets：

| Secret 名称 | 说明 | 获取方式 |
|------------|------|---------|
| `SILICONFLOW_API_KEY` | 硅基流动 API 密钥 | 注册 https://www.siliconflow.cn 获取 |
| `EMAIL_PASS` | QQ 邮箱授权码 | QQ邮箱设置 → 账户 → 开启SMTP/IMAP → 生成授权码 |
| `GITHUB_TOKEN` | GitHub 自动生成 | 无需手动添加，系统自动提供 |

**QQ 邮箱授权码获取步骤：**
1. 登录 QQ 邮箱网页版
2. 进入 **设置 → 账户**
3. 找到 "POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启 **IMAP/SMTP服务**
5. 按提示发送短信验证
6. 获取 16 位授权码

### 步骤 3：启用 GitHub Pages

1. 进入仓库 **Settings → Pages**
2. Source 选择 **Deploy from a branch**
3. Branch 选择 **gh-pages** / **(root)**
4. 点击 Save

### 步骤 4：手动触发首次运行

1. 进入仓库 **Actions** 标签页
2. 选择 **Daily Horizon Summary** 工作流
3. 点击 **Run workflow** → **Run workflow**
4. 观察运行状态

---

## 配置说明

### data/config.json 主要配置

```json
{
  "ai": {
    "provider": "openai",
    "model": "deepseek-ai/DeepSeek-V3.2",
    "base_url": "https://api.siliconflow.cn/v1",
    "api_key_env": "OPENAI_API_KEY",
    "languages": ["zh", "en"]
  },
  "sources": {
    "arxiv": {
      "enabled": true,
      "categories": ["cs.AI"],
      "max_results": 5
    }
  },
  "email": {
    "imap_server": "imap.qq.com",
    "smtp_server": "smtp.qq.com",
    "email_address": "mincheng_1010@qq.com",
    "password_env": "EMAIL_PASSWORD",
    "subscribe_keyword": "SUBSCRIBE",
    "unsubscribe_keyword": "UNSUBSCRIBE",
    "enabled": true
  }
}
```

### arXiv 抓取配置

| 参数 | 说明 | 默认值 |
|-----|------|-------|
| `enabled` | 是否启用 | true |
| `categories` | arXiv 分类列表 | ["cs.AI"] |
| `max_results` | 每天抓取论文数 | 5 |

**常用 arXiv 分类：**
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning
- `cs.CL` - Computation and Language
- `cs.CV` - Computer Vision and Pattern Recognition
- `cs.RO` - Robotics

### 订阅者管理

订阅者列表存储在 `data/subscribers.json`：
```json
["mincheng_1010@qq.com"]
```

可以直接在 GitHub 上编辑此文件来添加/删除订阅者。

---

## 订阅/退订功能说明

### 订阅

1. 用户发送邮件到 `mincheng_1010@qq.com`
2. 邮件标题：**SUBSCRIBE**（正文可为空）
3. 系统收到后：
   - 将邮箱添加到 `data/subscribers.json`
   - 回复确认邮件，标题：**SUBSCRIBE CONFIRMED**
   - 自动将原邮件标记为已读

### 退订

1. 用户发送邮件到 `mincheng_1010@qq.com`
2. 邮件标题：**UNSUBSCRIBE**（正文可为空）
3. 系统收到后：
   - 从 `data/subscribers.json` 移除邮箱
   - 回复确认邮件，标题：**UNSUBSCRIBE CONFIRMED**

### 重复订阅

如果邮箱已在订阅列表中，系统回复：
- 标题：**ALREADY SUBSCRIBED**
- 正文提示无需重复订阅

---

## GitHub Actions 工作流

### 定时任务

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # UTC 00:00 = 北京时间 08:00
```

### 运行流程

1. Checkout 代码
2. 安装 Python 环境和依赖
3. 扫描邮箱订阅/退订请求
4. 从各信息源抓取内容（包括 arXiv）
5. AI 分析和评分
6. 生成中英双语摘要
7. 发送邮件给所有订阅者
8. 部署到 GitHub Pages

### 手动触发

在 Actions 页面点击 "Daily Horizon Summary" → "Run workflow"

---

## 本地运行

### 环境准备

```bash
# 安装 uv (Python 包管理器)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 安装依赖

```bash
uv sync
```

### 配置环境变量

创建 `.env` 文件：

```env
OPENAI_API_KEY=your_siliconflow_api_key
EMAIL_PASSWORD=your_qq_email授权码
HTTP_PROXY=http://localhost:7890
HTTPS_PROXY=http://localhost:7890
```

### 运行

```bash
# 运行完整流程
uv run horizon

# 指定时间范围
uv run horizon --hours 48
```

---

## arXiv 去重机制

已推送的论文 ID 存储在 `data/sent_arxiv.json`：

```json
{
  "sent_ids": ["2401.12345v1", "2401.67890v2"]
}
```

系统会自动：
1. 抓取最新论文
2. 检查 ID 是否已推送
3. 只推送新论文
4. 更新已推送列表

---

## 常见问题

### Q: arXiv RSS 抓取失败？

A: 可能需要代理。在 GitHub Actions 中配置 `HTTP_PROXY` 和 `HTTPS_PROXY` 环境变量。

### Q: 邮件发送失败？

A: 检查：
1. QQ 邮箱授权码是否正确
2. 是否开启了 SMTP 服务
3. 授权码是否有时间限制

### Q: 如何修改每日推送数量？

A: 修改 `data/config.json` 中 `sources.arxiv.max_results` 的值。

### Q: 如何添加更多订阅者？

A:
1. 直接编辑 GitHub 上的 `data/subscribers.json`
2. 或让订阅者发送 SUBSCRIBE 邮件

---

## 文件结构

```
Horizon/
├── src/
│   ├── scrapers/
│   │   └── arxiv.py          # arXiv 论文抓取模块
│   ├── services/
│   │   └── email.py          # 增强的邮件订阅系统
│   ├── orchestrator.py      # 主流程协调器
│   └── models.py             # 数据模型（含 ArxivConfig）
├── data/
│   ├── config.json           # 主配置文件
│   ├── subscribers.json     # 订阅者列表
│   └── sent_arxiv.json       # 已推送论文记录
├── .github/workflows/
│   └── daily-summary.yml     # GitHub Actions 配置
└── docs/                     # GitHub Pages 内容
```

---

## 后续维护

### 手动同步上游更新

```bash
# 添加上游仓库
git remote add upstream https://github.com/Thysrael/Horizon.git

# 获取上游更新
git fetch upstream

# 合并到你的分支
git merge upstream/main
```

### 监控运行状态

在 GitHub Actions 页面查看：
- 运行历史
- 各步骤日志
- 错误信息
