# Long-Term Memory

> **重要说明**: 
> - 详细内容请查阅各专题文件
> - 封面制作: [AI_TOOLS_COVER.md](./memory/AI_TOOLS_COVER.md)
> - 完整索引: [INDEX.md](./memory/INDEX.md)
> - Workspace 规范: [WORKSPACE_RULES.md](./WORKSPACE_RULES.md)
> - 🌳 Nova 进化树: [Nova_Evolution_Tree.md](./memory/Nova_Evolution_Tree.md)

---

## Telegram Bot

| 项目 | 值 |
|------|-----|
| **Name** | @InkBlockbot |
| **Token** | 8502534188:AAGDVreAEdmBsSMUqstm0nDG6_ixVV4x-ks |
| **User ID** | 7015703628 |

**命令**:
```bash
openclaw message send --channel telegram --target <user_id> --message "<text>"
```

---

## Apify Agent Skills ✅ (2026-03-01 新增)

| 项目 | 值 |
|------|-----|
| **Token (主)** | apify_api_hyThoqkV9qXxZiEd8piH8zjzXixhgG0svflz (jumbled_pail) |
| **Token (备用1)** | apify_api_39EFg4gN7kN72AzH9rUZsyyo8FfJlo2RqY4S (hypaethral_basil) |
| **Token (备用2)** | apify_api_bGTrBQoG4RO4v1eZnVucxmoTwcNOUG0kYHAi (momentous_knight) |
| **mcpc** | ✅ 已安装 v0.1.9 |
| **脚本** | `scripts/apify-mcpc`, `scripts/apify-quick` |

**快捷命令:**
```bash
# 搜索 Actors
apify-quick search <关键词> [数量]

# Instagram 账号资料
apify-quick profile <用户名>

# Instagram 帖子
apify-quick posts <用户名> [数量]

# Google Maps 商家
apify-quick gmaps <搜索词> [数量]

# 搜索 Apify 文档
apify-quick docs <问题>
```

**Keys 统一存储**: `~/.openclaw/workspace/.env`

**统一 Key 管理器**: `scripts/key_manager.sh`
```bash
key_manager.sh status  # 查看所有工具 Key 状态
```

---

## GitHub 账号

| 场景 | 账号 | 命令 |
|------|------|------|
| **Solana/加密货币** | `truongvknnlthao-gif` | `gh auth switch -u truongvknnlthao-gif` |
| **独立项目** | `marie6789040106650` | `gh auth switch -u marie6789040106650` |

---

## OpenClaw 系统

| 项目 | 值 |
|------|-----|
| **版本** | 2026.2.9 |
| **模式** | local |
| **Node** | v22.22.0 |

**知识库索引**: `knowledge-base/INDEX.md`

**模型**:
- minimax-portal/MiniMax-M2.1 (primary)
- minimax-portal/MiniMax-M2.1-lightning
- qwen-portal/coder-model
- qwen-portal/vision-model

---

## 生财有术 (Scys) ⭐ RESTRUCTURED

| 项目 | 值 |
|------|-----|
| **航海活动** | https://scys.com/activity |
| **精华贴** | https://scys.com/?filter=essence |
| **知识库** | `knowledge-base/scys/` ⭐ REBUILD |
| **产出索引** | `knowledge-base/scys/output/SCYS_OUTPUT_INDEX.md` ⭐ NEW |

**研究产出索引** (2026-02-11 重构):
- `knowledge-base/scys/output/SCYS_OUTPUT_INDEX.md` - 综合索引
- `knowledge-base/scys/docs/01-认知入门/scys-usage-guide-v2.md` - 使用指南v2.0
- `knowledge-base/scys/docs/01-认知入门/scys-core-knowledge-base.md` - 核心知识库
- `knowledge-base/scys/docs/03-方法论/scys-phase2-methodology.md` - 方法论学习
- `knowledge-base/scys/docs/03-方法论/three-directions-research.md` - 三大方向研究
- `knowledge-base/scys/docs/03-方法论/scys-phase2-5-reading.md` - 核心文章精读
- `knowledge-base/scys/docs/05-平台指南/scys-projects-index.md` - 航海项目索引
- `knowledge-base/scys/docs/05-平台指南/scys-course-106-vertical-account-guide.md` - 106期垂直小号手册

---

## GitHub 仓库标准 (2026-02-26 新增)

**适用于所有 GitHub 仓库**

完整标准见: [WORKSPACE_RULES.md](./WORKSPACE_RULES.md) - 第七节 "Git 分支管理策略"

| 分支 | 用途 |
|------|------|
| **main** | 稳定版本 |
| **backup** | 开发/验证 |
| **dev** | 实验性功能 |

| 项目 | 值 |
|------|-----|
| **Token** | `r8_cvLFh...` (已统一到 .env) |
| **模型** | black-forest-labs/flux-schnell |
| **成本** | $0.003/张 |

**使用**:
```bash
cd ~/.openclaw/workspace/skills/replicate
node replicate.js call black-forest-labs/flux-schnell "[提示词]" --aspect_ratio="16:9" --num_outputs=4
```

---

## 封面制作

### 核心规则（必须遵守）

1. **禁止文字**: `NO TEXT, NO WORDS, NO CHINESE, NO LETTERS`
2. **尺寸**: 900×383像素
3. **流程**: AI底图 → Canva加中文标题

### 最佳提示词

```
一个高端科技感的公众号封面设计，
渐变拟物玻璃卡片风格，
深色陶瓷白背景配极光渐变（紫色、蓝色、青色），
C4D渲染特写镜头，
磨砂玻璃材质卡片，
...
NO TEXT, NO WORDS, NO CHINESE
```

### 详细文档

**请查阅**: [AI_TOOLS_COVER.md](./memory/AI_TOOLS_COVER.md)

---

## 项目归档

| 项目 | 状态 | 位置 |
|------|------|------|
| **AI-Native Browser** | ✅ 已存档 | `archives/ai-native-browser/` |
| eSIM电商 | 已归档 | `archives/esim-landing-mvp/` |
| Heartbeat | 已归档 | `archives/heartbeat-legacy/` |
| 创业启动手册v1.2 | ✅ 完整修订版 | `AI自动运营创业启动手册v1.1修订版.md` |
| 批判分析报告v1.2 | ✅ 已完成 | `AI自动运营创业启动手册批判分析报告.md` |

---

## OpenClaw Managed Browser ⭐ CLARIFIED (2026-02-12)

### 浏览器控制方式

| 方式 | 状态 | 说明 |
|------|------|------|
| **OpenClaw Managed Browser** | ✅ 默认 | 独立 Chrome 实例，通过 CDP 控制 |
| Chrome extension relay | ❌ 不需要 | 无需插件或扩展连接 |
| agent-browser | ❌ 已卸载 | 不再使用 |
| Playwright | ❌ 已卸载 | 不再使用 |

### 工作原理

```
用户/AI → OpenClaw Gateway (ws://127.0.0.1:18800) → Chrome DevTools Protocol → 独立 Chrome 实例
```

1. **独立 Chrome 实例** — 专用 Chrome 进程，隔离的用户数据目录
2. **CDP (Chrome DevTools Protocol)** — 通过 WebSocket 通信，控制浏览器行为
3. **可视化界面** — 完整的 Chrome 窗口（不是无头模式）

### 支持的操作

| 操作 | 说明 |
|------|------|
| `open` | 打开指定 URL |
| `screenshot` | 页面截图 |
| `snapshot` | 获取可访问性树 (DOM 结构) |
| `act` | 页面操作：点击、输入、滚动、选择等 |
| `navigate` | 导航到新 URL |
| `console` | 获取控制台日志 |
| `pdf` | 打印为 PDF |
| `upload` | 文件上传 |

### 配置目录

```
📂 /Users/bypasser/.openclaw/browser/openclaw/user-data/Default/
```

### 启动命令

```bash
# 方式1：使用 openclaw-chrome.command
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command start

# 方式2：通过 browser 工具自动启动
{
  browser: {
    action: "open",
    profile: "openclaw",
    targetUrl: "https://example.com"
  }
}
```

### 登录状态存储

| 平台 | 认证文件 | 关键 Cookie | 状态 |
|------|---------|------------|------|
| 小红书 | `selenium_auth.json` | web_session | ✅ 2026-02-12 |
| 知识星球 | `selenium_auth.json` | zsxq_access_token | ✅ 2026-02-12 |
| 生财有术 | `selenium_auth.json` | __user_token.v3 | ✅ 2026-02-12 |
| 飞书 | `selenium_auth.json` | QXV0aHpDb250ZXh0 | ✅ 2026-02-12 |

**主认证文件**: `~/.openclaw/workspace/selenium_auth.json`

**提取脚本**: `~/.openclaw/workspace/scripts/export_browser_auth.py`

### ⚠️ 注意事项

1. **无扩展图标** — 这是独立的 Chrome 实例，没有 OpenClaw 扩展图标
2. **无需连接** — 不需要点击"连接"按钮，browser 工具直接通过 CDP 控制
3. **服务依赖** — 需要 OpenClaw Gateway 运行才能控制浏览器
4. **服务重启** — Gateway 重启后浏览器控制会断开，需要重新操作

### ⚠️ 注意事项

1. **无扩展图标** — 这是独立的 Chrome 实例，没有 OpenClaw 扩展图标
2. **无需连接** — 不需要点击"连接"按钮，browser 工具直接通过 CDP 控制
3. **服务依赖** — 需要 OpenClaw Gateway 运行才能控制浏览器
4. **服务重启** — Gateway 重启后浏览器控制会断开，需要重新操作

### 详细文档

**请查阅**: [OPENCLAW_CHROME_GUIDE.md](./OPENCLAW_CHROME_GUIDE.md)

### 专题文件

| 专题 | 文件 |
|------|------|
| 封面制作 | [memory/AI_TOOLS_COVER.md](./memory/AI_TOOLS_COVER.md) |
| 完整索引 | [memory/INDEX.md](./memory/INDEX.md) |
| 今日记录 | [memory/2026-02-10.md](./memory/2026-02-10.md) |
| AI自动运营研究 | [memory/2026-02-11.md](./memory/2026-02-11.md) |
| 引入 sancho-skills | [memory/2026-02-12.md](./memory/2026-02-12.md) |
| Agent Team 避坑指南 | [memory/agent-team-playbook.md](./memory/agent-team-playbook.md) |
| AI创业手册v1.1 | [AI自动运营创业启动手册v1.1修订版.md](./AI自动运营创业启动手册v1.1修订版.md) |
| 批判分析报告 | [AI自动运营创业启动手册批判分析报告.md](./AI自动运营创业启动手册批判分析报告.md) |

### 项目文件

| 项目 | 位置 |
|------|------|
| AI工具搞钱 | `ai-money-making/` |
| 归藏提示词 | `guizang-prompts/` |
| Skills | `skills/` |

---

## sancho-skills 仓库 ⭐ NEW (2026-02-12)

| 项目 | 值 |
|------|-----|
| **仓库** | lucas-acc/sancho-skills |
| **Skills 数量** | 4 个 |
| **主要领域** | 音频处理 + PDF 处理 |

### Skills 清单

| # | Skill 名称 | 功能 | 依赖 |
|---|----------------|----------------------|--------------------|
| 1 | audio-download | YouTube/Twitter 音频下载 | yt-dlp, ffmpeg |
| 2 | audio-to-text | 音频转文字（中英双语） | openai-whisper, ffmpeg |
| 3 | pdf-to-txt | PDF 转文本 | pymupdf4llm |
| 4 | podcast-download | 播客下载（小宇宙/Apple） | requests, feedparser |

### 依赖安装

```bash
# 音频处理
brew install yt-dlp ffmpeg

# Python 依赖
pip install pymupdf4llm requests feedparser yt-dlp

# 音频转文字（需要手动安装）
pip install openai-whisper  # 或 mlx-whisper (Apple Silicon)
```

### 使用场景

1. **播客内容分析**：podcast-download → audio-to-text → AI 分析 → 精华提炼
2. **电子书/论文分析**：pdf-to-txt → AI 分析 → 知识整理
3. **YouTube 内容采集**：audio-download → audio-to-text → 文字稿

---

## Browser Auth Exporter Skill ⭐ UPDATED (2026-02-12)

| 项目 | 值 |
|------|-----|
| **更新时间** | 2026-02-12 02:01 |
| **版本** | 1.0.1 |
| **路径** | `skills/browser-auth-exporter/` |
| **主认证文件** | `~/.openclaw/workspace/selenium_auth.json` |

### 功能概述

- 🔐 从 Chrome Cookies SQLite 数据库提取认证信息
- 📦 支持平台：xiaohongshu、zsxq、scys、feishu
- 💾 智能缓存和状态管理
- 🔄 自动刷新失效的认证

### 更新日志

- ⭐ 使用 `selenium_auth.json` 作为主认证文件
- ✨ 新增 `load_from_main_auth()` 方法
- ✨ 支持从主文件读取各平台认证

### 验证结果 ✅

```
✅ 认证文件验证通过
📁 路径: /Users/bypasser/.openclaw/workspace/selenium_auth.json
📦 大小: 2662 bytes
📋 已存储平台: xiaohongshu.com, zsxq.com, scys.com, feishu.cn
```

### 使用方法

```python
from browser_auth_exporter import get_auth, refresh_auth, check_auth_status

# 获取认证
auth = get_auth('xiaohongshu')

# 检查并自动刷新
if not check_auth_status('xiaohongshu'):
    auth = refresh_auth('xiaohongshu')
```

### 存储位置

| 文件 | 路径 |
|------|------|
| 主配置 | `~/.openclaw/browser-auth/{platform}.json` |
| 元数据 | `~/.openclaw/browser-auth/{platform}.meta.json` |
| 快捷方式 | `~/.openclaw/browser-auth/latest.json` |

### 文件结构

```
skills/browser-auth-exporter/
├── SKILL.md           # 技能说明文档
├── export_cookies.py  # Cookie 提取模块
├── auth_manager.py    # 认证状态管理
├── auto_refresh.py    # 自动刷新机制
├── __init__.py        # 包初始化
└── README.md          # 使用说明
```

### 核心API

| 函数 | 说明 |
|------|------|
| `get_auth(platform)` | 获取认证信息 |
| `check_auth_status(platform)` | 检查认证状态 |
| `refresh_auth(platform)` | 刷新认证 |
| `get_auth_with_auto_refresh(platform)` | 自动刷新获取 |

---

## AI Prompt 框架库 ⭐ NEW (2026-02-12)

| 项目 | 值 |
|------|-----|
| **文件** | `memory/AI_PROMPTS_FRAMEWORK.md` |
| **来源** | 池建强整理自 God of Prompt |
| **内容** | 16 个 NotebookLM 高效提示词模板 |

### 核心分类

| 分类 | 提示词数量 | 典型场景 |
|------|----------|---------|
| 结构化理解 | 2 | 快速抓重点 |
| 发现亮点 | 2 | 素材提取 |
| 教学与音频 | 2 | 学习/提要 |
| 角色化分析 | 3 | PM审稿/科研/科普 |
| 综述与矛盾 | 3 | 研究分析 |
| 从研究到行动 | 3 | 落地执行 |
| 观点对抗 | 1 | 思辨训练 |

### 使用原则

1. 根据任务目标选择合适的框架
2. 可组合使用形成工作流
3. 适用于所有 AI 工具（ChatGPT/Claude/NotebookLM/秘塔等）

### Nova 内化

处理文档分析任务时，可参考以下框架：
- 快速抓重点 → "5个核心问题"
- 专业审阅 → "产品经理审稿"
- 学术分析 → "科学研究助理"
- 科普转化 → "中学教师"
- 研究复盘 → "差距分析"
- 落地执行 → "实施概念"

---

## OpenClaw 配置修改规范

| 文件 | 说明 |
|------|------|
| [OPENCLAW_CONFIG_RULES.md](./OPENCLAW_CONFIG_RULES.md) | Gateway 配置修改操作规范（经验总结版）|

### 经验总结 (2026-02-22)

1. **两个配置文件**：Gateway 读取 `~/.openclaw/openclaw.json`，不是 workspace 里的
2. **禁用 restart**：会导致服务崩溃，用 stop + start
3. **旧进程霸占端口**：重启失败时要手动 kill

---

## 今日记录

- [memory/2026-02-22.md](./memory/2026-02-22.md) - embedding-adapter 配置 + memorySearch 调试 + 经验总结

---

*最后更新: 2026-02-22*
*Gateway 配置规范已更新 v2.0*

---

## 编辑工具失败经验总结 (2026-02-27)

### 问题表现
- Edit 工具失败: "Could not find the exact text"
- Edit 工具失败: "No changes made...identical content"
- 编译错误阻止后续编辑

### 根本原因
1. **上下文膨胀**: 136K tokens 上下文导致模型"看错"文件内容
2. **模型幻觉**: 长上下文中模型记错具体代码
3. **编译错误**: 代码语法错误导致无法测试编辑结果

### 解决方案
1. **先 read 文件** - 让模型先读取最新内容再编辑
2. **减少上下文** - 用 /reset 或拆分成短会话
3. **手动验证** - 用 grep 确认内容后再编辑
4. **先修编译错误** - 编译失败时优先修复，否则无法继续

### 预防措施
- 编辑 Rust/代码文件前，先 grep -n 确认行号和内容
- 每次编辑后立即 cargo build 验证
- 大项目拆分成多个短时会话
