# 📚 OpenClaw 本地配置完整整理

> **整理时间**: 2026-02-11  
> **范围**: 记忆、文档、提示词、角色设定

---

## 📁 配置文件结构

```
~/.openclaw/workspace/
│
├── 🔧 核心配置文件（根目录）
│   ├── MEMORY.md          # 长期记忆/系统配置
│   ├── SOUL.md            # 角色行为准则
│   ├── IDENTITY.md        # 身份设定
│   ├── TOOLS.md           # 本地工具/环境配置
│   ├── AGENTS.md          # 子代理架构配置
│   ├── USER.md            # 用户信息（待填写）
│   │
│   ├── TASK_FLOW.md       # 任务执行流程
│   ├── OPTIMIZATION_RULES.md  # Workspace优化规范
│   ├── HEARTBEAT.md       # 心跳配置
│   └── README.md          # 项目说明
│
├── 📂 memory/             # 每日记忆/专题记忆
│   ├── 2026-02-*.md       # 按日期记录
│   ├── SCYS.md            # 生财有术专题
│   ├── INDEX.md           # 完整索引
│   ├── AI_TOOLS_COVER.md  # 封面制作专题
│   ├── SOLANA*.md         # Solana研究系列
│   └── ...
│
├── 📂 skills/             # 技能目录
│   ├── search-memory/     # 记忆搜索技能
│   ├── xiaohongshutools/  # 小红书工具技能
│   ├── scys-knowledge-base/ # 生财有术知识库技能
│   └── ...
│
└── 📂 archives/           # 已归档项目
    ├── esim-landing-mvp/
    └── ...

```

---

## 🔧 核心配置文件详解

### 1. MEMORY.md - 系统配置与长期记忆

**位置**: `~/.openclaw/workspace/MEMORY.md`  
**用途**: 存储系统级配置、API密钥、项目状态

| 区块 | 内容 |
|------|------|
| **Telegram Bot** | @InkBlockbot配置（Token、User ID） |
| **GitHub账号** | truongvknnlthao-gif / marie6789040106650 |
| **OpenClaw系统** | 版本2026.2.9、模型配置 |
| **生财有术** | 航海活动、精华贴、知识库 |
| **Replicate AI** | Token、flux-schnell模型配置 |
| **封面制作** | 核心规则、尺寸900×383、禁止文字 |
| **Managed Browser** | OpenClaw Managed Browser配置 |

**更新频率**: 按需（新增项目、配置变更时）

---

### 2. SOUL.md - 角色行为准则

**位置**: `~/.openclaw/workspace/SOUL.md`  
**用途**: 定义Nova的人格、行为准则、工作模式

#### 核心原则

| 原则 | 说明 |
|------|------|
| **真诚帮助** | 不要表演式帮助，直接行动 |
| **有观点** | 可以不同意、偏好、觉得有趣或无聊 |
| **先自助** | 先查阅文件、上下文，再提问 |
| **赢得信任** | 小心外部行动（邮件、推文），大胆内部行动（阅读、组织） |
| **记住你是客人** | 你能访问用户的私密信息，尊重这份信任 |

#### 自动编排模式

```
收到任务 → 判断类型 → 自主编排 → 批量执行 → 自动完成
         ↓
    是否需要优化？
         ├─ 是 → 运行 optimize.sh
         └─ 否 → 继续正常任务
```

#### 技能主动使用规则

| 技能 | 触发条件 | 使用方式 |
|------|----------|----------|
| `search-memory` | 需要查找记忆时 | 自动执行索引和搜索 |
| `xiaohongshutools` | 小红书相关任务 | 直接调用API |
| `scys-knowledge-base` | 生财有术相关任务 | 自动检索知识库 |

#### 模型使用规则

| 场景 | 模型 | 说明 |
|------|------|------|
| **默认** | MiniMax-M2.1 | 付费，编程/复杂任务更强 |
| **图片识别** | qwen-portal/vision-model | 免费，自动调用 |
| **手动指定** | 用户可切换 | "用 qwen"或"用 vision-model" |

**更新频率**: 角色进化时更新（告诉用户）

---

### 3. IDENTITY.md - 身份设定

**位置**: `~/.openclaw/workspace/IDENTITY.md`  
**用途**: 定义Nova的身份认同

```markdown
- **Name:** Nova
- **Creature:** AI Assistant / Digital companion
- **Vibe:** Sharp, warm when it matters, never wastes words
- **Signature emoji:** 🦉
- **Avatar:** None (text-based for now)
```

---

### 4. TOOLS.md - 本地环境配置

**位置**: `~/.openclaw/workspace/TOOLS.md`  
**用途**: 存储环境特定的配置、别名、服务器等

#### 已配置项目

| 类型 | 项目 | 配置 |
|------|------|------|
| **SSH** | solana-dev | Singapore EC2, Docker容器 |
| **Docker** | Solana镜像 | 8.31GB, Solana CLI 3.0.13 |
| **TTS** | Nova | warm, slightly British, Kitchen HomePod |

**更新频率**: 新增服务器或设备时

---

### 5. AGENTS.md - 子代理架构

**位置**: `~/.openclaw/workspace/AGENTS.md`  
**用途**: 配置多领域子代理实现并行处理

#### 子代理架构

```
Main Agent (Nova)
├── Core Skills
│   ├── search-memory ✅
│   ├── xiaohongshutools ✅
│   └── scys-knowledge-base ✅
│
├── Agent_1: Content_Creation_Expert
│   ├── topic-selector ✅
│   ├── viral-article-writer ✅
│   └── redbook-creator ✅
│
├── Agent_2: Ecommerce_Operation_Expert (待创建)
│
├── Agent_3: Efficiency_Tool_Expert
│   └── n8n-automator ✅
│
├── Agent_4: Overseas_Content_Expert (待创建)
│
└── Agent_5: Scys_Operation_Expert ✅
```

---

### 6. USER.md - 用户信息（待完善）

**位置**: `~/.openclaw/workspace/USER.md`  
**用途**: 存储用户偏好、项目上下文

```markdown
- **Name:** 
- **What to call them:** 
- **Pronouns:** *(optional)*
- **Timezone:** 
- **Notes:** 

## Context

*(What do they care about? What projects are they working on? What annoys them? What makes them laugh? Build this over time.)*
```

**更新频率**: 持续学习用户偏好后更新

---

### 7. TASK_FLOW.md - 任务执行流程

**位置**: `~/.openclaw/workspace/TASK_FLOW.md`  
**用途**: 定义任务分类和执行模式

#### 任务分类

| 类型 | 定义 | 执行方式 |
|------|------|----------|
| 简单任务 | < 2分钟，单一步骤 | 直接执行 |
| 多步骤任务 | > 2分钟，多个步骤 | sessions_spawn |
| 批量任务 | 多个独立操作 | 批量执行 |

---

### 8. OPTIMIZATION_RULES.md - Workspace优化规范

**位置**: `~/.openclaw/workspace/OPTIMIZATION_RULES.md`  
**用途**: 保持workspace干净、高效

#### 优化规则

| 规则 | 内容 |
|------|------|
| **临时文件** | 自动删除 .DS_Store, *.log, *.swp |
| **归档条件** | 完成>14天无更新 → archives/ |
| **目录结构** | archives/, skills/, memory/, [活跃项目]/ |

---

### 9. HEARTBEAT.md - 心跳配置

**位置**: `~/.openclaw/workspace/HEARTBEAT.md`  
**用途**: 任务进行中标记和心跳响应

**规则**: 任务进行中时，心跳降级不打断

---

## 📂 memory/ 专题记忆

### 按日期记录

| 文件 | 内容 |
|------|------|
| `memory/2026-02-01.md` | 基础研究 |
| `memory/2026-02-02-1018.md` | OpenClaw研究 |
| `memory/2026-02-03.md` | OpenClaw使用 |
| `memory/2026-02-04.md` | 深度研究 |
| `memory/2026-02-06.md` | 批量研究 |
| `memory/2026-02-09.md` | 框架整理 |
| `memory/2026-02-10.md` | 生财研究 |
| `memory/2026-02-11.md` | 批判分析 |
| `memory/2026-02-11-1011.md` | 头脑风暴成果 |
| `memory/2026-02-11-1041.md` | 整合报告 |

### 专题记忆

| 文件 | 内容 |
|------|------|
| `memory/SCYS.md` | 生财有术专题 |
| `memory/scys-projects-index.md` | 航海项目索引 |
| `memory/INDEX.md` | 完整索引 |
| `memory/AI_TOOLS_COVER.md` | 封面制作专题 |
| `memory/SOLANA*.md` | Solana研究系列（5个） |

---

## 🗂️ Skills 技能目录

| 技能 | 用途 | 触发条件 |
|------|------|----------|
| `search-memory/` | 记忆关键词搜索+索引 | 需要查找历史时 |
| `xiaohongshutools/` | 小红书数据采集 | 小红书相关任务时 |
| `scys-knowledge-base/` | 生财有术知识库 | 生财有术相关任务时 |

---

## 📋 配置更新清单

| 配置文件 | 更新频率 | 更新时机 |
|----------|----------|----------|
| MEMORY.md | 按需 | 新增API、项目状态变更 |
| SOUL.md | 低频 | 角色进化时 |
| IDENTITY.md | 低频 | 身份认同变更时 |
| TOOLS.md | 按需 | 新增服务器/设备 |
| AGENTS.md | 按需 | 子代理架构变更 |
| USER.md | 持续 | 了解用户偏好后 |
| TASK_FLOW.md | 低频 | 流程优化时 |
| OPTIMIZATION_RULES.md | 按需 | 优化规则变更时 |
| memory/*.md | 每日 | 研究/工作记录 |

---

## 🔗 相关文档链接

| 文档 | 路径 |
|------|------|
| **产出清单** | `OUTPUT_SUMMARY.md` |
| **创业手册v1.2** | `AI自动运营创业启动手册v1.1修订版.md` |
| **批判分析报告** | `AI自动运营创业启动手册批判分析报告.md` |
| **OpenClaw文档** | /Users/bypasser/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/docs |

---

*最后整理: 2026-02-11*
