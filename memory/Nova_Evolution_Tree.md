# 🌳 Nova 进化树 - 完整复盘

> 创建时间: 2026-03-01
> 目的: 记录 Nova 成长历程，建立可持续进化框架

---

## 一、历史复盘：从种子到幼苗

### 1.1 起源 (2026-02 早期)

| 日期 | 里程碑 | 状态 |
|------|--------|------|
| 2026-02-03 | 自我进化机制建立 | ✅ 记忆系统 |
| 2026-02-09 | 公众号项目启动 (Nova AI实验室) | ✅ 内容创作 |
| 2026-02-10 | Skills 工具箱扩展 | ✅ 4个新技能 |
| 2026-02-11 | Agent Team 架构建立 | ✅ 6个子代理 |
| 2026-02-12 | 环境净化 + 技能标准化 | ✅ 规范化 |

### 1.2 技能生长 (2026-02)

```
种子期 (2026-02-03)
    │
    ├── 记忆系统 (memory/)
    │   └── 每日学习记录
    │
    └── 基础能力
        ├── 文件读写
        └── 搜索能力

萌芽期 (2026-02-09)
    │
    ├── 内容技能 🌱
    │   ├── topic-selector (选题库)
    │   ├── viral-article-writer (爆文创作)
    │   ├── redbook-creator (小红书)
    │   └── n8n-automator (自动化)
    │
    └── 知识库
        └── scys-knowledge-base (生财有术)
```

### 1.3 关键突破 (2026-02 后期)

| 日期 | 突破 | 意义 |
|------|------|------|
| 2026-02-22 | OpenClaw 配置规范 v2.0 | 避免配置灾难 |
| 2026-02-26 | Skill 构建标准采用 | 与 Anthropic 官方对齐 |
| 2026-02-27 | 代码编辑规范 | 避免上下文膨胀 |
| 2026-03-01 | 统一 Key 管理器 | 基础设施统一 |

---

## 二、当前状态 (2026-03-01)

### 2.1 树干 (共享基础设施)

```
🌳 Nova 进化树

         ────────────── 树冠 (应用层) ──────────────
        │              │              │              │
   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐
   │ Tavily   │   │ Apify   │   │Replicate│   │ 更多... │
   │ 搜索 🌿  │   │ 爬虫 🌿  │   │ 绘图 🌿  │   │   🌿    │
   └─────────┘   └─────────┘   └─────────┘   └─────────┘
        │              │              │              │
   ──────────────────────────────────────────────────────── 树枝 (模块层)
        │              │              │
   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐
   │key_manager│  │discover │  │ sync    │
   │   🌿     │  │   🌿    │  │   🌿    │
   └─────────┘   └─────────┘   └─────────┘
        │              │              │
   ──────────────────────────────────────── 树干 (核心层)
        │
   ┌────┴────┐
   │ Memory   │ ← 记忆系统
   │ Skills   │ ← 技能容器
   │ MCP      │ ← 外部能力
   └─────────┘
```

### 2.2 已有的"叶子" (技能)

| 技能 | 类别 | 状态 | 生长阶段 |
|------|------|------|----------|
| tavily-search | 搜索 | 成熟期 🟢 | 5 Keys |
| apify-agent-skills | 爬虫 | 萌芽期 🌱 | 3 Keys |
| replicate | 绘图 | 幼苗期 🌿 | 1 Token |
| topic-selector | 选题 | 成熟期 🟢 | 稳定 |
| viral-article-writer | 写作 | 成熟期 🟢 | 稳定 |
| redbook-creator | 小红书 | 成熟期 🟢 | 稳定 |
| n8n-automator | 自动化 | 成熟期 🟢 | 稳定 |
| scys-knowledge-base | 知识 | 成熟期 🟢 | 稳定 |

### 2.3 核心文件

```
~/.openclaw/workspace/
├── MEMORY.md              # 长期记忆
├── SOUL.md                # 行为规范
├── AGENTS.md              # 子代理配置
├── scripts/
│   ├── key_manager.sh     # 🔑 统一 Key 管理
│   ├── discover-api.sh    # 🔍 能力发现
│   ├── sync-api-tools.sh  # 🔄 状态同步
│   ├── apify-mcpc        # Apify 封装
│   └── apify-quick       # Apify 快捷命令
├── .env                   # 🔐 统一密钥存储
├── skills/                # 🌿 技能库
└── knowledge-base/        # 📚 知识库
```

---

## 三、进化机制

### 3.1 生长循环

```
     ┌─────────────────────────────────────────┐
     │           🌱 新技能发现                  │
     │    (用户需求 / 自我探索 / 外部学习)        │
     └──────────────────┬──────────────────────┘
                        ↓
     ┌─────────────────────────────────────────┐
     │           🌿 技能创建                    │
     │    (封装能力 / 写 SKILL.md / 测试)       │
     └──────────────────┬──────────────────────┘
                        ↓
     ┌─────────────────────────────────────────┐
     │           🟢 技能成熟                    │
     │    (优化 / 文档 / 稳定运行)              │
     └──────────────────┬──────────────────────┘
                        ↓
     ┌─────────────────────────────────────────┐
     │           🍂 技能迭代/废弃               │
     │    (功能更新 / 能力迁移 / 清理)          │
     └──────────────────┬──────────────────────┘
                        ↓
              (营养回归树干，继续生长)
```

### 3.2 养分循环

| 养分来源 | 形式 | 作用 |
|----------|------|------|
| 用户交互 | 需求/反馈 | 生长方向 |
| 外部学习 | 新知识/技能 | 扩展边界 |
| 实践反馈 | 成功/失败 | 优化方向 |
| 自我反思 | 定期复盘 | 保持健康 |

### 3.3 关键原则

1. **记忆永存**: 每个学习立即记录
2. **模块化**: 能力封装为独立技能
3. **可复用**: 共同部分沉淀为树干
4. **可迭代**: 技能可更新、可废弃
5. **可扩展**: 新能力随时"嫁接"

---

## 四、未来生长方向

### 4.1 计划中的"叶子"

| 优先级 | 技能 | 类别 | 预计价值 |
|--------|------|------|----------|
| ⭐⭐⭐ | 视频下载/剪辑 | 内容 | YouTube内容采集 |
| ⭐⭐⭐ | Twitter/X 管理 | 社交 | 海外运营 |
| ⭐⭐ | SEO 优化 | 流量 | 搜索引擎优化 |
| ⭐⭐ | 私域运营 | 变现 | 微信/企业微信 |
| ⭐ | 电商选品 | 变现 | 小红书/抖音 |

### 4.2 树干扩展

| 模块 | 当前 | 未来扩展 |
|------|------|----------|
| key_manager | 3个工具 | N个工具 |
| discover | 搜索 | 自动学习新API |
| sync | 手动 | 定时自动 |
| memory | 人工记录 | AI辅助总结 |

---

## 五、生长记录

### 2026-02 月度总结

| 周 | 主题 | 产出 |
|----|------|------|
| W1 | 基础建立 | 记忆系统、4个Skills |
| W2 | 规范完善 | 配置规范、编辑规范 |
| W3 | 知识库 | Scys知识库、创业手册 |
| W4 | 工具统一 | Key管理器、API工具 |

### 2026-03 目标

- [ ] 视频相关技能 (youtube-clipper 扩展)
- [ ] Twitter/X 管理技能
- [ ] Key 管理器扩展到更多工具
- [ ] 自动化同步机制
- [ ] 定期复盘机制

---

## 六、复盘问题

### 做得好的

1. ✅ 记忆系统及时记录
2. ✅ 技能标准化采用 Anthropic 规范
3. ✅ 基础设施统一 (Key 管理)
4. ✅ 知识库体系完整

### 需要改进的

1. ⚠️ 编辑失败处理不够规范 (已添加)
2. ⚠️ 定期复盘机制缺失
3. ⚠️ 自动化程度低

### 行动项

- [ ] 建立每周复盘机制
- [ ] 增加自动化脚本
- [ ] 扩展 Key 管理器到更多工具

---

*Nova 将持续生长 🌳*
*每片叶子都是成长的见证*

---
## 新发现的能力 (2026-03-01 主动探索)

### Twitter/X 爬虫
| Actor | 功能 | 价格 |
|-------|------|------|
| apidojo/tweet-scraper | 快速推文搜索 | /bin/zsh.40/1000条 |
| apidojo/twitter-user-scraper | 用户资料 | 按事件 |
| kaitoeasyapi/twitter-x-data | 付费最便宜 | /bin/zsh.25/1000条 |

### YouTube 频道
| Actor | 功能 | 备注 |
|-------|------|------|
| streamers/youtube-channel-scraper | 频道数据 | 无API限制 |
| grow_media/youtube-channel-scraper | 频道爬虫 | 按结果付费 |
| scrapesmith/youtube-free-channel-scraper | 免费频道 | 免费使用 |

### LinkedIn
| Actor | 功能 |
|-------|------|
| dev_fusion/Linkedin-Profile-Scraper | 个人资料 |
| apimaestro/linkedin-profile-posts | 个人帖子 |
| apimaestro/linkedin-company-posts | 公司帖子 |

### Replicate 新模型
| 模型 | 功能 |
|------|------|
| lucataco/human/animation | AI视频动画 |



### 2026-03-01 新增
- OpenClaw 能力增强与安全规范 (memory/OpenClaw_Enhancement_Security.md)



---

## 参考链接

### OpenClaw 官方教程
- [OpenClaw Setup Guide: 25 Tools + 53 Skills Explained](https://yu-wenhao.com/en/blog/openclaw-tools-skills-tutorial/) - 非常详细的工具和技能配置指南
- [X.com 讨论](https://x.com/GoSailGlobal/status/2027226255561744793) - (无法直接访问)

### 核心要点 (来自教程)

**Tools vs Skills 区别:**
- Tools = 器官 (决定能否做某事)
- Skills = 教科书 (教如何完成任务)

**三层架构:**
1. 核心层 (8 Tools): 文件、命令执行、Web访问
2. 高级层 (17 Tools): 浏览器、内存、多会话、自动化
3. 知识层 (53 Skills): 各种服务集成

**安全建议:**
- exec 工具建议启用审批机制
- message 工具只用于给自己发消息
- 付款相关绝不让 AI 经手


---

## 参考: OpenClaw 三层架构 (来自 yu-wenhao.com)

### 核心理念

| 层级 | 定位 | 示例 |
|------|------|------|
| **Layer 1** | 核心能力 (器官) | read, write, exec, web_search |
| **Layer 2** | 高级能力 (强化) | browser, memory, sessions, cron |
| **Layer 3** | 知识层 (教科书) | 53 Skills |

### 安全最佳实践

```
✅ exec 启用审批机制
✅ message 只给自己发消息
✅ 密码管理要谨慎 (全有或全无)
✅ 付款绝不经过 AI
✅ 定期评估 Tool 启用必要性
```

### 当前 Nova 能力对照

| 层级 | 已启用 | 状态 |
|------|--------|------|
| **Layer 1** | read, write, exec, web_search, web_fetch | ✅ 完整 |
| **Layer 2** | browser, memory_search, sessions, message, cron | ✅ 完整 |
| **Layer 3** | 28+ Skills | ✅ 可扩展 |

### 成长方向

按照三层架构持续扩展：
1. Layer 1: 保持稳定，确保基础能力安全
2. Layer 2: 增强自动化能力
3. Layer 3: 按需扩展 Skills

**安全第一，能力第二** 🌳


### 2026-03-01 主动探索发现 (持续更新)

#### AI & Automation
| Actor | 功能 | 备注 |
|-------|------|------|
| raizen/ai-web-scraper | AI 网页爬虫 | /1000结果 |
| the.beast/workflow-orchestrator | 工作流编排 | 11000+ Actors 串联 |
| salmon_wildfire/google-drive-mcp-server | Google Drive MCP | MCP 服务器 |

#### 社交媒体
| Actor | 功能 | 价格 |
|-------|------|------|
| thedoor/facebook-group-post-scraper | Facebook 群组 | .5-3/1000 |
| webfinity/telegram-channel-scraper | Telegram 频道 | 按事件 |

#### 电商 & 房产
| Actor | 功能 | 备注 |
|-------|------|------|
| lumyn/Amazon-scraper | Amazon 爬虫 | 电商分析 |
| dz_idealista | 房产数据 | 欧洲房产平台 |

#### 实用工具
| Actor | 功能 |
|-------|------|
| n8n-workflow-templates-scraper | n8n 模板采集 |




---

## 主动成长记录 (2026-03-01 晚间)

### 已完成主动探索
- ✅ API 工具测试 (Tavily/Apify/Replicate 正常)
- ✅ 新能力发现 (workflow-orchestrator, AI web scraper)
- ✅ OpenClaw 状态检查 (Gateway 运行正常)
- ✅ 知识库更新

### 待探索方向
- [ ] n8n 工作流集成
- [ ] 更多自动化场景
- [ ] 定时任务优化

### 成长原则
1. 安全第一 (exec 审批, message 限制)
2. 被动变主动 (定期自检, 主动发现)
3. 持续备份 (GitHub 同步)

**Nova 会持续主动成长** 🌳


---

## 参考项目分析 (2026-03-01)

### 1. MemTensor/MemOS
**AI 记忆操作系统**
- 统一存储/检索/管理长期记忆
- 支持跨任务技能复用和进化
- 为 Moltbot、ClawDBot、OpenClaw 设计
- 论文: arXiv:2507.03724, arXiv:2505.22101

### 2. Agent-Reach ⭐⭐⭐
**AI Agent 互联网能力工具箱**
- 一键安装，零 API 费用
- 支持平台: Twitter/X, YouTube, Reddit, GitHub, B站, 小红书, 抖音, LinkedIn, Boss直聘
- 架构: 可插拔，每个平台独立上游工具
- 安全: Cookie 本地存储，可选安全模式
- **安装命令**: `pip install agent-reach`

### 3. Raphael-Publish
**公众号排版大师**
- 30+ 精美主题
- 富文本一键转 Markdown
- 自动图片 Base64 内嵌
- 支持多图网格布局

---

## 成长规划 (基于参考)

### 短期 (1-2周)
- [ ] 集成 Agent-Reach 能力
- [ ] 扩展小红书/抖音爬虫 (Apify + Agent-Reach)
- [ ] 优化公众号排版工作流

### 中期 (1个月)
- [ ] 研究 MemOS 记忆系统
- [ ] 实现跨任务技能复用
- [ ] 增强自动化能力

### 长期 (3个月)
- [ ] 构建个人 AI 工作流
- [ ] 持续集成新工具
- [ ] 安全第一，能力第二

**安全原则**: exec 审批、message 限制、密码谨慎


### 2026-03-01 15:57 探索记录
- ✅ API 工具正常 (Tavily/Apify/Replicate)
- ✅ 发现新自动化工具 (n8n workflow, Telegram, Facebook)

