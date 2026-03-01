# Apify Agent Skills 完整使用指南

> 更新时间: 2026-03-01
> 来源: 官方文档 + GitHub 源码研究

---

## 1. 什么是 Apify Agent Skills

**Apify Agent Skills** 是 Apify 官方推出的 AI Agent 技能包，为 AI 编程助手（如 Claude Code、Cursor、Codex、Windsurf）提供网页爬取和数据提取能力。

### 核心架构

```
用户请求 → AI Agent → Agent Skill (SKILL.md) → mcpc CLI → Apify MCP Server → Apify Actors
```

### 支持的 AI 工具

| 工具 | 支持情况 |
|------|----------|
| Claude Code | ✅ 官方支持 |
| Cursor | ✅ 官方支持 |
| Windsurf | ✅ 官方支持 |
| Codex | ✅ 参考 agents/AGENTS.md |
| Gemini CLI | ✅ 参考 gemini-extension.json |
| 其他支持 Markdown 的 AI 工具 | ✅ 通用支持 |

---

## 2. 快速开始

### 2.1 前置条件

```bash
# 1. Node.js 20.6+
node --version

# 2. Apify 账号 (apify.com)
# 3. API Token (从 Apify Console 获取)
# 4. mcpc CLI
npm install -g @apify/mcpc
```

### 2.2 配置 API Token

```bash
# 方式1: 添加到 .env 文件
echo "APIFY_TOKEN=your_token_here" >> .env

# 方式2: 环境变量
export APIFY_TOKEN=your_token_here
```

### 2.3 安装 Agent Skills

```bash
# 方式1: npx (推荐)
npx skills add apify/agent-skills

# 方式2: Claude Code 插件
/plugin marketplace add https://github.com/apify/agent-skills
/plugin install apify-ultimate-scraper@apify-agent-skills

# 方式3: 手动克隆
git clone https://github.com/apify/agent-skills.git
cd agent-skills
```

---

## 3. 可用 Skills 清单

| Skill 名称 | 功能描述 | 适用场景 |
|------------|----------|----------|
| `apify-ultimate-scraper` | 通用 AI 爬虫 (55+ Actors) | 任何数据提取任务 |
| `apify-ecommerce` | 电商数据 (Amazon, Walmart, eBay 等) | 定价情报、产品研究 |
| `apify-lead-generation` | B2B/B2C 潜在客户生成 | 销售线索、市场开拓 |
| `apify-influencer-discovery` | 网红发现与评估 | 品牌合作、KOL 营销 |
| `apify-competitor-intelligence` | 竞品策略分析 | 市场分析、竞争情报 |
| `apify-market-research` | 市场调研 | 商业决策、市场验证 |
| `apify-audience-analysis` | 受众分析 | 用户画像、内容策略 |
| `apify-content-analytics` | 内容分析 | ROI 测量、效果追踪 |
| `apify-brand-reputation-monitoring` | 品牌声誉监控 | 口碑管理、危机预警 |
| `apify-trend-analysis` | 趋势分析 | 热点追踪、内容规划 |
| `apify-actor-development` | Actor 开发调试 | 开发者工具 |
| `apify-actorization` | 项目转换为 Actor | 迁移工具 |

---

## 4. mcpc CLI 详解

### 4.1 核心命令

```bash
# 查看可用会话和认证配置
mcpc

# 登录远程 MCP 服务器
mcpc mcp.apify.com login

# 查看服务器信息
mcpc mcp.apify.com

# 列出所有工具
mcpc mcp.apify.com tools-list

# 调用工具 (搜索 Actors)
mcpc mcp.apify.com tools-call search-actors keywords:="instagram" limit:=5

# 创建持久会话
mcpc mcp.apify.com connect @my_session

# 使用会话调用工具
mcpc @my_session tools-call search-actors keywords:="website crawler"
```

### 4.2 JSON 模式 (脚本化)

```bash
# JSON 输出便于脚本处理
mcpc mcp.apify.com tools-list --json

# 配合 jq 使用
mcpc mcp.apify.com tools-call search-actors keywords:="instagram" limit:=5 --json | jq '.content[0].text'
```

### 4.3 工具调用语法

```bash
# 基础参数
mcpc <target> tools-call <tool-name> arg1:=value1 arg2:=value2

# 强制字符串类型
mcpc tools-call id:='\"123\"' flag:='\"true\"'

# JSON 对象
mcpc tools-call config:='{\"key\":\"value\"}'

# 管道输入
echo '{"query": "test"}' | mcpc tools-call
```

---

## 5. 使用示例

### 5.1 爬取 Instagram 帖子

```bash
# 通过 mcpc 调用 Instagram Scraper Actor
mcpc mcp.apify.com tools-call run-actor \
  actorId:='apify/instagram-post-scraper' \
  input:='{"urls": ["https://www.instagram.com/openai/"], "limit": 10}'
```

### 5.2 搜索特定 Actor

```bash
mcpc mcp.apify.com tools-call search-actors keywords:="google maps" limit:=10
```

### 5.3 在 Claude Code 中使用

安装 Agent Skill 后，只需用自然语言描述需求：

```
"帮我爬取 @openai 的最新 10 条 Instagram 帖子，分析 AI 趋势"
```

Agent Skill 会自动：
1. 选择合适的 Actor
2. 获取 Actor schema
3. 询问输出格式偏好
4. 执行爬取
5. 返回结构化结果

---

## 6. 输出格式

| 格式 | 说明 | 使用场景 |
|------|------|----------|
| **Quick Answer** | 聊天中显示前 5 条结果 | 快速预览 |
| **CSV** | 完整导出，所有字段 | 数据分析 |
| **JSON** | 完整数据导出 | 程序处理 |

---

## 7. 定价

- **Actors**: 按结果付费 (pay-per-result)
- **免费额度**: 免费版可用，基本功能
- **付费版**: $99-$999/月 (根据用量)
- **具体价格**: 每个 Actor 不同，需在 Apify Store 查看

---

## 8. 安全风险 (重要)

### 8.1 Prompt Injection

| 风险 | 描述 |
|------|------|
| **攻击向量** | 如果 Agent 有"读取网页"技能，攻击者可在页面中嵌入隐藏指令 |
| **后果** | 可执行恶意代码、删除文件、窃取数据 |
| **场景** | 大规模系统处理不受信任的互联网数据时风险高 |

### 8.2 其他风险

| 风险 | 描述 |
|------|------|
| **碎片化管理** | 技能分散在不同文件夹，难以大规模治理 |
| **运行时不一致** | 本地运行正常，云 API 环境可能失败 |
| **Confused Deputy** | 技能描述重叠时可能触发错误技能 |
| **数据合规** | 爬取数据可能违反平台 ToS |

### 8.3 建议

- ✅ 仅用于本地、个人/团队小规模使用
- ✅ 处理可信数据源
- ❌ 不要用于大规模企业级关键任务
- ❌ 不要处理不受信任的互联网数据

---

## 9. 官方资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/apify/agent-skills |
| 官方文档 | https://docs.apify.com |
| Apify Academy | https://docs.apify.com/academy/ai/ai-agents |
| mcpc CLI | https://github.com/apify/mcp-cli |
| Discord 社区 | https://discord.gg/jyEM2PRvMU |
| 技能规范 | https://agentskills.io/specification |

---

## 10. 本地配置状态

| 项目 | 状态 |
|------|------|
| APIFY_TOKEN | ✅ 已配置 |
| mcpc CLI | ✅ 已安装 v0.1.9 |
| 脚本 | ✅ apify-mcpc, apify-quick |

---

## 11. 安装方式对比

### 官方推荐方式

| 工具 | 安装命令 |
|------|----------|
| **通用** | `npx skills add apify/agent-skills` |
| **Claude Code** | `/plugin marketplace add` + `/plugin install` |
| **Cursor/Windsurf** | `.cursor/settings.json` 配置 |
| **Codex/Gemini CLI** | 参考 `agents/AGENTS.md` |

### 我的实现方式 (直接使用 mcpc CLI)

```bash
# 安装 mcpc
npm install -g @apify/mcpc

# 直接调用 (无需安装 Skill)
~/.openclaw/workspace/scripts/apify-mcpc tools-call call-actor actor:='apify/instagram-profile-scraper' input:='{"usernames": ["openai"]}'

# 快捷脚本
~/.openclaw/workspace/scripts/apify-quick profile openai
```

### 对比分析

| 维度 | 官方 Skill 方式 | mcpc CLI 方式 |
|------|-----------------|---------------|
| **集成度** | 高 (内置到 AI Agent) | 中 (需调用脚本) |
| **使用门槛** | 低 (自然语言) | 中 (需记命令) |
| **灵活性** | 中 (依赖 Agent 能力) | 高 (直接控制) |
| **调试** | 难 (黑盒) | 易 (直接看输出) |
| **适合场景** | Claude Code/Cursor 内 | 自动化脚本、OpenClaw |

### 结论

- **用官方 Skill**: 在 Claude Code/Cursor/Windsurf 中使用更自然
- **用 mcpc CLI**: OpenClaw/自动化脚本/需要精确控制时更好

当前 OpenClaw 采用 **mcpc CLI 方式**，因为：
1. 不依赖特定 AI 工具
2. 可精确控制参数
3. 便于调试和日志追踪

---

*文档基于 Apify 官方文档和 GitHub 源码研究*
