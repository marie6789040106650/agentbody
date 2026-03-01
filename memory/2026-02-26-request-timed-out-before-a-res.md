# Session: 2026-02-26 19:01:23 UTC

- **Session Key**: agent:main:telegram:group:-1003782534970:topic:2877
- **Session ID**: 7a4f7683-fbf3-4db3-b493-a1dce1df94f6
- **Source**: telegram

## Conversation Summary

user: [media attached: /Users/bypasser/.openclaw/media/inbound/file_22---4f371442-996d-4227-9257-ca7ee1f20acd.md (text/markdown) | /Users/bypasser/.openclaw/media/inbound/file_22---4f371442-996d-4227-9257-ca7ee1f20acd.md]
To send an image back, prefer the message tool (media/path/filePath). If you must inline, use MEDIA:https://example.com/image.jpg (spaces ok, quote if needed) or a safe relative path like MEDIA:./image.jpg. Avoid absolute paths (MEDIA:/...) and ~ paths — they are blocked for security. Keep caption in the text body.
System: [2026-02-26 13:48:13 EST] Reasoning ON — include <think>.

Conversation info (untrusted metadata):
```json
{
  "message_id": "2883",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:2877",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "BY",
  "name": "BY",
  "username": "HeyWhiteBY"
}
```

[Telegram BY & Inkblock id:-1003782534970 topic:2877 +1m Thu 2026-02-26 13:49 EST] BY (7015703628): 验证内容，并找到《The Complete Guide to Building Skills for Claude》 <file name="file_22---4f371442-996d-4227-9257-ca7ee1f20acd.md" mime="text/markdown"> ![Anthropic 发布《Claude Skill 构建完整指南》：AI Agent 开发的新范式](https://mmbiz.qpic.cn/mmbiz_jpg/3OakhjY0T9iax9MuIUbDKEeJZYlgMvEibdz0Tb7smqWTSswGvzsMa058JxzDFR2AAU0ibXd7S5ZpNW6uWVcvvyPsNeHQWyf6tpDNm258le5ojw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0) 33 页技术指南，从提示词工程到结构化系统，渐进式披露设计理念，三种主要应用模式。附 PDF 下载链接。 ⸻ ## 一份改变游戏规则的 33 页指南 2026 年 1 月 29 日，Anthropic 正式发布了《The Complete Guide to Building Skills for Claude》，这份长达 33 页的技术指南，标志着 AI Agent 开发进入了一个新的阶段。 虽然 Claude 的 Skill 功能早在 2025 年 10 月就随 Agent 功能一同推出，但这份完整版的技术指南才刚刚发布，它系统地阐述了如何构建高效、可复用的 AI 技能系统。 **📥 PDF 下载：** The Complete Guide to Building Skills for Claude ## 为什么这份指南如此重要？ ### 从提示词工程到结构化系统 以前，我们和大模型打交道，主要靠各种提示词工程（Prompt Engineering）。每次对话都要重新解释任务逻辑，效率低下，结果不稳定。 现在，Anthropic 推动的是以"技能（Skills）"为核心的结构化系统设计。通过渐进式披露和标准化工作流，这套体系把 AI 聊天从海量的临时对话，升级成一套可扩展的基础设施。 ### Skill 不再是简单的指令 一个"技能（Skill）"不再只是对话中的一小段指令，而是一个完整的系统： •**SKILL.md 文件** - 核心定义和工作流 •**相关脚本** - 可执行的代码 •**参考资料** - 领域知识和文档 •**配套资产** - 模板、图片等资源 开发者通过这种方式定义一次工作流，Claude 就能在不同场景下反复调用，而不用每次对话都重新解释任务逻辑。 **最佳实践被固化到执行层里了，API 调用和任务处理会更加稳定，一致性也更好。** ## 核心设计理念：渐进式披露 指南详细解释了"渐进式披露（Progressive Disclosure）"的设计理念，这是用来解决 AI Agent 常见的上下文窗口过载问题。 ### 三级加载系统 1. **元数据（Metadata）** - 始终在上下文中（~100 词） •name 和 description 字段 •用于判断何时触发 Skill 2. **SKILL.md 主体** - 当 Skill 触发时加载（<5k 词） •核心工作流和指令 •保持简洁，避免冗余 3. **捆绑资源** - 按需加载（无限制） •scripts/ - 可执行脚本 •references/ - 参考文档 •assets/ - 输出资源 ### 按需加载机制 系统通过轻量级的 YAML 前置数据（Frontmatter）来引导 Claude 判断何时调用特定技能。只有在任务真正需要时，才会加载完整的详细指令和额外文件。 这种按需加载机制： •**显著减少 Token 消耗** •**提升 AI 在处理复杂任务时的精确度** •**避免上下文窗口过载** ## 三种主要应用模式 Anthropic 在指南中给出了三种主要的 Skill 应用模式： ### 1\. 文档与资产创作 使用 Skill 来生成标准化的文档、报告、代码模板等。 **示例：** •生成 API 文档 •创建项目模板 •生成测试报告 ### 2\. 工作流自动化 将复杂的多步骤流程封装成 Skill，实现自动化执行。 **示例：** •代码审查流程 •数据处理管道 •部署工作流 ### 3\. 模型上下文协议（MCP）增强 通过 Skill 增强 MCP 的能力，实现更复杂的交互。 **示例：** •数据库查询 •API 调用 •外部工具集成 ## 实际应用案例 ### 案例 1：墨问 OpenAPI Skill 有开发者基于墨问的 OpenAPI，创建了两个 Skill： 1. **笔记创建 Skill** - 自动创建和发布笔记 2. **用户状态查询 Skill** - 查询用户的创作状态 •近期写了多少 •点赞评论阅读数 •自动分类 这两个 Skill，Claude Code 能用，OpenClaw 也能用，每次用自然语言激活即可。 ### 案例 2：跨平台兼容 Anthropic 推出的 MCP 和 Skills 都成了行业标准。 我们构建的 Skill，稍作迁移即可适配各大公司的产品： •Claude Code •OpenClaw •Cursor（未来可能支持） •其他 AI 编程工具 **学会构建自己的 Skills 本身就是一个非常重要的技能。** ## 社区反响 ### Reddit 讨论热度 在 Reddit 的 r/ClaudeAI 社区，这份指南的讨论帖获得了： •**1.5K+ 点赞** •**112+ 条评论** 社区成员评价： \> "Great read for anyone new to skills, or struggling to wrap their heads around skills and where/how they fit in the ecosystem. Heck you could extract the info in here and turn it into a more detailed skill-creator skill than the official one from Anthropic." ### 行业影响 这份指南的发布，标志着： 1. **AI Agent 开发进入标准化阶段** •不再是各自为战 •有了统一的设计范式 2. **提示词工程的终结** •从临时对话到结构化系统 •从一次性指令到可复用技能 3. **AI 能力的模块化** •技能可以打包、分享、复用 •形成技能生态系统 ## 关键要点总结 ### 1\. Skill 是完整的系统 不是简单的提示词，而是包含代码、文档、资源的完整系统。 ### 2\. 渐进式披露是核心 通过三级加载系统，避免上下文窗口过载，提升效率。 ### 3\. 标准化带来可移植性 遵循标准的 Skill 可以在不同平台间迁移使用。 ### 4\. 最佳实践被固化 将经验和知识固化到 Skill 中，确保一致性和稳定性。 ### 5\. 生态系统正在形成 Skills 可以被分享、复用，形成一个技能市场。 ## 如何开始构建 Skill？ ### 第一步：阅读指南 下载并仔细阅读这份 33 页的指南： **📥 The Complete Guide to Building Skills for Claude** ### 第二步：理解核心概念 •SKILL.md 的结构 •YAML Frontmatter 的作用 •渐进式披露的原理 •资源组织的最佳实践 ### 第三步：从简单开始 不要一开始就构建复杂的 Skill，从简单的开始： 1. **单一功能 Skill** - 只做一件事 2. **无外部依赖** - 不依赖复杂的环境 3. **清晰的输入输出** - 明确的接口定义 ### 第四步：迭代优化 根据实际使用情况，不断优化： •简化 SKILL.md •提取公共资源到 references/ •添加更多示例到 assets/ •优化脚本性能 ## 未来展望 ### Skill 市场的兴起 随着 Skills 标准的普及，我们可能会看到： •**Skill 市场** - 类似 App Store 的技能商店 •**Skill 评级** - 社区评价和推荐 •**Skill 组合** - 多个 Skill 协同工作 ### AI Agent 的专业化 通过 Skills，AI Agent 可以： •**快速专业化** - 加载特定领域的 Skill •**能力可扩展** - 随时添加新的 Skill •**知识可积累** - Skill 承载领域知识 ### 开发者的新角色 开发者的角色将从"写代码"转变为： •**Skill 设计师** - 设计高效的技能系统 •**工作流架构师** - 组织多个 Skill 协同 •**知识工程师** - 将领域知识固化到 Skill ## 结语 Anthropic 发布的这份《Claude Skill 构建完整指南》，不仅仅是一份技术文档，更是 AI Agent 开发范式转变的宣言。 从提示词工程到结构化系统，从临时对话到可复用技能，这是 AI 应用开发的一次重大升级。 MCP 和 Skills 都成了行业标准，学会构建自己的 Skills，将成为 AI 时代开发者的核心竞争力。 ⸻ **📥 下载指南：** The Complete Guide to Building Skills for Claude **🔗 相关资源：** •Anthropic 官方文档 •Claude Skills Hub ⸻ ✨ 更多 AI 最新资讯和实践指南 cc.guapihub.net 关注公众号，获取最新信息 🚀 </file>
assistant: 我来验证这篇文章的内容，并找到原始指南。

assistant: 找到了！让我获取更多细节并下载原始 PDF。

assistant: 让我用 PDF 工具提取内容：

assistant: ## 验证结果 ✅

**内容真实性：已验证**

| 项目 | 文章描述 | 实际情况 |
|------|----------|----------|
| **发布日期** | 2026年1月29日 | ✅ 确认 |
| **页数** | 33页 | 32页（接近） |
| **渐进式披露** | 三级加载系统 | ✅ 确认（frontmatter → SKILL.md → 捆绑资源） |
| **三种应用模式** | 文档创作/工作流自动化/MCP增强 | ✅ 确认 |
| **PDF下载** | 有链接 | ✅ 官方链接有效 |

---

## 原始指南

**📥 官方 PDF:**
https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

**🔗 GitHub 转换版（Markdown）:**
https://gist.github.com/liskl/269ae33835ab4bfdd6140f0beb909873

**📚 官方 Skills 示例库:**
https://github.com/anthropics/skills

---

文章内容与原始指南基本一致，主要核心点都涵盖了：
- 渐进式披露设计理念
- YAML Frontmatter 结构
- Skill 文件夹结构（SKILL.md + scripts/ + references/ + assets/）
- 三种应用模式
- 测试和分发指南
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2891",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:2877",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "BY",
  "name": "BY",
  "username": "HeyWhiteBY"
}
```

《The Complete Guide to Building Skills for Claude》 官方有提供便于你阅读的版本吗？比如md格式
assistant: 找到了！让我下载到 workspace 方便阅读：

assistant: 已下载到 workspace：

| 项目 | 值 |
|------|-----|
| **文件** | `anthropic-claude-skills-guide.md` |
| **路径** | `~/.openclaw/workspace/anthropic-claude-skills-guide.md` |
| **格式** | Markdown |
| **来源** | GitHub Gist (社区转换版) |

---

**目录结构：**
- Introduction
- Chapter 1: Fundamentals
- Chapter 2: Planning and Design
- Chapter 3: Testing and Iteration
- Chapter 4: Distribution and Sharing
- Chapter 5: Patterns and Troubleshooting
- Chapter 6: Resources and References
- Reference A: Quick Checklist
- Reference B: YAML Frontmatter
- Reference C: Complete Skill Examples

---

**注意：** 这是社区转换的非官方版本。Anthropic 官方只提供 PDF 版本，没有直接提供 Markdown。但这个 Gist 版本内容完整且格式良好，适合阅读。

你可以直接让我读取特定章节，或者在 workspace 中查看完整文件。
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2895",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:2877",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "BY",
  "name": "BY",
  "username": "HeyWhiteBY"
}
```

《The Complete Guide to Building Skills for Claude》 对我们有哪些帮助
assistant: 结合你的 OpenClaw 现状，这本指南能帮助你的几个方面：

---

## 1. 优化现有 Skills

你已经安装了 20+ Skills，但可能存在结构不统一的问题。指南会告诉你：

- **YAML Frontmatter 最佳实践** — 让 Skill 触发更精准
- **渐进式披露** — 减少 token 消耗，提升响应速度
- **文件夹结构** — scripts/ references/ assets/ 正确使用

```
你的 skills 目录        指南标准结构
├── skill-creator/     → 已有但可优化
├── xiaohongshu/      → 缺 YAML frontmatter？
├── n8n-automator/     → 可添加 references/
└── ...
```

---

## 2. 构建更强大的自定义 Skill

你有一些很强的工具能力，但缺少"知识层"：

| 现有能力 | 指南告诉你的 |
|----------|-------------|
| browser 控制 | 如何封装"小红书竞品分析"Skill |
| MCP (Tavily) | 如何创建"搜索→分析→报告"工作流 |
| 文件读写 | 如何创建"批量处理"Skill |

---

## 3. 复用社区 Skills

指南提到了官方 Skills 示例库：https://github.com/anthropics/skills

你可以：
- 直接使用其中的 skill-creator、frontend-design 等
- 学习他们的 YAML 写法
- 提交你的 Skills 到社区

---

## 4. 与 MCP 协同

这是最关键的 — 你的 OpenClaw 有强大 MCP 能力，但缺少" recipes"（食谱）：

| MCP（厨房） | Skill（食谱）|
|-------------|--------------|
| 给你工具 | 教你怎么用 |
| 连接外部服务 | 封装最佳实践 |
| 提供数据 | 整合工作流 |

**比如**：你有 Tavily MCP，但每次搜索都要解释"怎么搜索才精准"。有了 Skill 后，一次定义，多次复用。

---

## 下一步建议

要我帮你：

1. **分析现有 Skills** — 检查哪些缺 frontmatter 或结构问题
2. **创建一个示例 Skill** — 按指南标准封装一个简单功能
3. **从官方库导入** — 看看有哪些可以直接用

你选哪个？
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2897",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:2877",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true,
  "is_group_chat": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "BY",
  "name": "BY",
  "username": "HeyWhiteBY"
}
```

思考《The Complete Guide to Building Skills for Claude》 对我们有哪些帮助，我们以后用这个标准来制作skills 这个标准本身能否作为一个skills
assistant: 好问题！让我深入思考一下 👇

---

## 这本身就是一个 Skill

**完全可以，而且非常有价值。**

指南的核心就是教你"如何构建 Skill"，把它封装成 Skill 非常合理 — 这就是**元技能（Meta-Skill）**。

```
指南本体 (PDF/MD)
        ↓ 封装
Skill: skill-builder (教你怎么创建 Skill)
        ↓ 使用
你创建的新 Skill
```

---

## 这个 Skill 应该包含什么？

| 模块 | 内容 |
|------|------|
| **YAML Frontmatter 模板** | 标准化的 name + description |
| **文件夹结构模板** | SKILL.md + scripts/ + references/ + assets/ |
| **创建流程** | Step 1: 明确用例 → Step 2: 定义触发词 → Step 3: 写指令 → Step 4: 测试 |
| **检查清单** | Reference A 的 checklist |
| **示例** | Reference C 的完整示例 |

---

## 触发场景

用户说：
- "帮我创建一个 Skill"
- "我想封装个工作流"
- "怎么做一个小红书分析的 Skill"
- "教我构建技能"

→ 自动激活这个 Skill，然后引导用户完成创建流程。

---

## 实际上...

Anthropic 官方已经做了一个：**skill-creator**

位置：https://github.com/anthropics/skills/tree/main/skills/skill-creator

我们可以：
1. **直接使用官方的** — 已存在，直接导入
2. **本地化定制** — 基于官方 + 你的习惯，创建一个增强版

---

## 我的建议

创建一个 `openclaw-skill-builder` Skill：

- 基于官方 skill-creator
- 加入你的 OpenClaw 特定内容（browser、你的 MCPs、workspace 规范）
- 用中文引导（更适合你）

要我现在创建这个 Skill 吗？预计结构：

```
openclaw-skill-builder/
├── SKILL.md              # 主文件
├── templates/
│   ├── frontmatter.yaml  # YAML 模板
│   └── skill-folder.md   # 文件夹结构模板
└── examples/
    └── xiaohongshu-analysis.md  # 示例
```
