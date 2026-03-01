# Memory Directory Index

> 最后更新: 2026-02-10

## 📁 目录结构

```
memory/
├── 📄 INDEX.md                    ← 本索引
├── 📁 archives/                   ← 历史归档
│   └── YYYY-MM.md                ← 按月归档
│
├── 📁 PROJECTS/                   ← 项目知识
│   ├── SOLANA.md                 ← Solana 开发
│   ├── ESIM.md                   ← eSIM 业务
│   ├── AI_TOOLS_COVER.md         ← ⭐ 封面制作
│   └── SCYS.md                   ← ⭐ 生财有术航海项目
│
├── 📁 TOOLS/                     ← 工具配置
│   ├── OPENCLAW.md              ← 系统配置
│   ├── BROWSER.md               ← 浏览器自动化
│   └── CLI.md                   ← 命令行速查
│
├── 📁 METHODS/                   ← 方法论
│   ├── LEARNING.md              ← 学习方法论
│   ├── SUBAGENTS.md             ← 子代理模式
│   └── RESEARCH.md              ← 研究协议
│
└── 📁 DAILY/                     ← 每日日志
    └── YYYY-MM-DD.md            ← 每日记录
```

## 📋 文件列表

### PROJECTS - 项目知识

| 文件 | 大小 | 说明 |
|------|------|------|
| [SOLANA.md](./SOLANA.md) | 251 行 | Solana 开发知识库 |
| [ESIM.md](./ESIM.md) | 298 行 | eSIM 业务知识库 |
| [AI_TOOLS_COVER.md](./AI_TOOLS_COVER.md) | ⭐ 新增 | 封面制作专题 |
| [SCYS.md](./SCYS.md) | ⭐ 新增 | 生财有术航海项目 |

### TOOLS - 工具配置

| 文件 | 大小 | 说明 |
|------|------|------|
| [OPENCLAW.md](./OPENCLAW.md) | 410 行 | OpenClaw 系统配置 |
| [BROWSER.md](./BROWSER.md) | 354 行 | 浏览器自动化配置 |
| [CLI.md](./CLI.md) | 450 行 | 命令行工具速查 |

### METHODS - 方法论

| 文件 | 大小 | 说明 |
|------|------|------|
| [LEARNING.md](./LEARNING.md) | 304 行 | 学习方法论与研究 |
| [SUBAGENTS.md](./SUBAGENTS.md) | 397 行 | 子代理创建与配置 |
| [RESEARCH.md](./RESEARCH.md) | 173 行 | 研究协议与机制 |

### DAILY - 每日日志

| 文件 | 日期 | 说明 |
|------|------|------|
| [2026-02-12.md](./2026-02-12.md) | 2026-02-12 | 引入 sancho-skills 仓库（4个Skills） |
| [2026-02-10.md](./2026-02-10.md) | 2026-02-10 | 浏览器配置优化、知识星球登录、OpenClaw Chrome 配置 |
| [2026-02-09.md](./2026-02-09.md) | 2026-02-09 | 知识库搭建、Skills创建 |
| [2026-02-07.md](./2026-02-07.md) | 2026-02-07 | 自动化工作流 |
| [2026-02-06.md](./2026-02-06.md) | 2026-02-06 | 独立文件体系建设 |
| [2026-02-04.md](./2026-02-04.md) | 2026-02-04 | Solana 学习总结 |
| [2026-02-03.md](./2026-02-03.md) | 2026-02-03 | Gateway 配置经验 |
| [2026-02-02.md](./2026-02-02-1018.md) | 2026-02-02 | 浏览器扩展配置 |
| [2026-02-01.md](./2026-02-01.md) | 2026-02-01 | 初始化日志 |

---

## ⭐ 封面制作专题

**新文件**: [AI_TOOLS_COVER.md](./AI_TOOLS_COVER.md)

### 核心内容

| 内容 | 说明 |
|------|------|
| **核心规则** | 禁止文字、尺寸规范、工作流程 |
| **提示词模板** | 渐变拟物玻璃卡片、矢量插画、科技极简 |
| **工具配置** | Replicate API、成本对比 |
| **工作流程** | 批量生成、质量检查 |

### 快速开始

**最佳提示词**:
```
一个高端科技感的公众号封面设计，
渐变拟物玻璃卡片风格，
深色陶瓷白背景配极光渐变（紫色、蓝色、青色），
C4D渲染特写镜头，
磨砂玻璃材质卡片，
...
NO TEXT, NO WORDS, NO CHINESE
```

**生成命令**:
```bash
cd ~/.openclaw/workspace/skills/replicate
node replicate.js call black-forest-labs/flux-schnell "[提示词]" --aspect_ratio="16:9" --num_outputs=4
```

---

## 🔍 快速查找

### 按主题

| 主题 | 文件 |
|------|------|
| 封面制作 | **AI_TOOLS_COVER.md** ⭐ |
| 生财有术航海 | **SCYS.md** ⭐ |
| Solana 开发 | SOLANA.md |
| eSIM 业务 | ESIM.md |
| OpenClaw 配置 | OPENCLAW.md |
| 浏览器自动化 | BROWSER.md |
| 命令行工具 | CLI.md |
| 学习方法 | LEARNING.md |
| 子代理使用 | SUBAGENTS.md |
| 研究协议 | RESEARCH.md |

---

## 📁 相关项目文件

| 项目 | 位置 | 说明 |
|------|------|------|
| AI工具搞钱 | `../ai-money-making/` | 公众号项目主目录 |
| 归藏提示词 | `../guizang-prompts/` | 18个高质量提示词 |
| Skills | `../skills/` | 工具技能目录 |

---

## 📊 统计

| 指标 | 值 |
|------|-----|
| 总文件数 | 20 |
| 独立知识文件 | 12 |
| 专题文件 | 4 (SOLANA, ESIM, AI_TOOLS_COVER, SCYS) |
| 每日日志 | 9 |
| 归档目录 | 1 |

---

## 📖 快速链接

### 核心文件

| 文件 | 说明 |
|------|------|
| [MEMORY.md](../MEMORY.md) | ⭐ 精简版长期记忆（必读） |
| [INDEX.md](./INDEX.md) | 本索引 |
| [AI_TOOLS_COVER.md](./AI_TOOLS_COVER.md) | ⭐ 封面制作专题 |
| [SCYS.md](./SCYS.md) | ⭐ 生财有术航海项目 |

### 项目文件

| 文件 | 说明 |
|------|------|
| [ai-money-making/README.md](../ai-money-making/README.md) | AI工具搞钱项目主文档 |
| [ai-money-making/articles/](../ai-money-making/articles/) | 40篇文章内容 |

---

*此索引自动生成，用于快速定位文档。*
*最后更新: 2026-02-12 10:15*
