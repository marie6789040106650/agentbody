# System Profiles & Accounts

> 独立记忆文件 | 最后更新: 2026-02-06

---

## 🐙 GitHub Accounts

### 账号配置

| 场景 | 账号 | 命令 |
|------|------|------|
| **加密货币 / Solana 相关** | `truongvknnlthao-gif` | `gh auth switch -u truongvknnlthao-gif` |
| **独立项目 / 其他** | `marie6789040106650` | `gh auth switch -u marie6789040106650` |

### 当前状态

- ✅ 两个账号都已登录 (keyring)
- ✅ 协议: HTTPS

### 快速切换命令

```bash
# 切换到加密货币/Solana 账号
gh auth switch -u truongvknnlthao-gif

# 切换到独立项目账号
gh auth switch -u marie6789040106650

# 查看当前账号
gh auth status
```

---

## 🤖 OpenClaw Migration

### 问题状态

| 项目 | 值 |
|------|-----|
| **状态** | Migration in progress |
| **问题** | minimax-portal-auth extension references deprecated clawdbot/plugin-sdk |

### 临时解决方案

- 修改文件: `/Users/bypasser/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/extensions/minimax-portal-auth/index.ts`
- 解决方案: Replaced deprecated import with direct TypeBox imports
- 状态: Working workaround, needs monitoring for official fix

---

## 💻 System Information

### Hardware

| 项目 | 值 |
|------|-----|
| **Host** | MacBook Pro (192.168.182.1) |
| **OS** | Darwin 25.2.0 (x64) |
| **Node** | v22.22.0 |

### OpenClaw

| 项目 | 值 |
|------|-----|
| **Version** | 2026.1.30 (8469) |
| **Mode** | local |

### 可用模型

- `minimax-portal/MiniMax-M2.1` (primary)
- `minimax-portal/MiniMax-M2.1-lightning`
- `qwen-portal/coder-model`
- `qwen-portal/vision-model`

---

## 🔐 Credentials Management

### 存储方式

| 类型 | 存储位置 |
|------|----------|
| GitHub | keyring |
| API Keys | 环境变量 |
| 密码 | 系统 Keychain |

### 重要凭证

| 服务 | 备注 |
|------|------|
| MiniMaxi API | Cookie 已存储在脚本中 |
| Zoho Mail | 已在浏览器配置中 |
| Telegram Bot | 已配置在 OpenClaw 中 |

---

## 📂 Related Documents

- `memory/OPENCLAW.md` - OpenClaw 系统配置
- `memory/CLI.md` - 命令行工具
- `memory/SOLANA.md` - Solana 开发知识

---

*此文件独立维护，便于系统账号和配置的查阅。*
