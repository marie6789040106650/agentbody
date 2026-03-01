# OpenClaw Workspace

**个人 AI 助手配置** | Nova 🦉

## 📦 项目结构

```
~/.openclaw/workspace/
├── AGENTS.md          # Agent 运行时配置
├── SOUL.md            # 人格定义
├── MEMORY.md          # 长期记忆
├── TOOLS.md           # 工具配置
├── USER.md            # 用户信息
├── IDENTITY.md        # 身份定义
├── README.md          # 项目说明
├── skills/            # Skills 集合
├── memory/            # 每日记录
└── *.md               # 研究文档、项目文档
```

## 🎯 核心功能

| 功能 | 说明 |
|------|------|
| **AI 助手** | Nova (MiniMax-M2.1) |
| **通信平台** | Telegram (Bot: @InkBlockbot) |
| **邮件管理** | Zoho Mail |
| **浏览器自动化** | OpenClaw Browser (无头模式) |
| **版本控制** | GitHub (私有仓库) |

## 🛠️ Skills 列表

| Skill | 功能 | 状态 |
|-------|------|------|
| `openclaw-gen` | 模板生成器 | ✅ 已安装 |
| `solana-dev` | Solana 开发 | ✅ 已安装 |
| `auto-skill-builder` | 自动构建 Skills | ✅ 已安装 |
| `github-repo-mirror` | Git 仓库镜像 | ✅ 已安装 |
| `zoho-mail-assistant` | Zoho 邮件管理 | ✅ 已安装 |
| `duckduckgo-search` | 搜索工具 | ✅ 已安装 |

详细列表: [skills/README.md](skills/README.md)

## 📚 文档索引

| 类型 | 文件 | 说明 |
|------|------|------|
| **记忆** | MEMORY.md | 长期记忆和规则 |
| **每日** | memory/YYYY-MM-DD.md | 每日记录 |
| **Solana** | memory/SOLANA.md | Solana 开发知识 |
| **eSIM** | memory/ESIM.md | eSIM 业务知识 |
| **OpenClaw** | memory/OPENCLAW.md | 系统配置 |
| **浏览器** | memory/BROWSER.md | 浏览器自动化 |

## 🚀 常用命令

```bash
# 启动 OpenClaw
openclaw gateway start

# 启动浏览器
browser action=start profile=openclaw

# 查看状态
openclaw status

# 备份配置
cd ~/.openclaw/workspace && git add -A && git commit -m "update"
```

## 📖 参考资源

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub](https://clawhub.com)
- [GitHub 仓库](https://github.com/marie6789040106650/openclaw-user-config)

---

**最后更新**: 2026-02-09
**维护者**: Nova 🦉
