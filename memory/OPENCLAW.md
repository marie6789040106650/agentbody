# OpenClaw System Configuration

> 独立记忆文件 | 最后更新: 2026-02-06

---

## 🤖 Telegram Bot

### Bot Details

| 项目 | 值 |
|------|-----|
| **Name** | @InkBlockbot |
| **Token** | 8502534188:AAGDVreAEdmBsSMUqstm0nDG6_ixVV4x-ks |
| **User ID** | 7015703628 |
| **迁移时间** | 2026-02-01 (VPS → local) |

### Configuration

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "8502534188:AAGDVreAEdmBsSMUqstm0nDG6_ixVV4x-ks",
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist",
      "allowFrom": ["*"]
    }
  }
}
```

### Key Points

- Bot runs via Bot API (no need for Telegram desktop app)
- Session history does not persist across different OpenClaw instances
- Gateway manages bot connection with polling mode
- Messages sent via: `openclaw message send --channel telegram --target <user_id> --message "<text>"`

---

## 📧 Zoho Mail Automation

### Credentials

| 项目 | 值 |
|------|-----|
| **Email** | atlas@inkblocklab.com |
| **Password** | mU8cmua# |

### Browser Profile

- **Location:** `~/.openclaw/browser/openclaw/user-data/Default/`
- **Session persistence:** Cookies, Login Data, Sessions, Session Storage

### Search URL Format

```
https://mail.zoho.com/zm/#mail/search/0/inbox/any/0/0/subject/KEYWORD
```

### Skills Created

- `/Users/bypasser/.openclaw/workspace/skills/zoho-mail-assistant/`
  - SKILL.md
  - OPENCLAW_BROWSER_GUIDE.md
  - QUICK_REFERENCE.md
  - zoho-mail.js

---

## 💓 Heartbeat Configuration

### Basic Settings

| 项目 | 值 |
|------|-----|
| **频率** | 每 30 分钟 |
| **Cron Job ID** | 9b2e0cd6-7614-40bd-b00e-cb0094b93049 |

### Check Order

1. **MiniMaxi 用量监控** (优先检查)
2. Zoho Mail 待处理邮件

### Removed (2026-02-07)

- ~~Telegram/WhatsApp 未回复消息~~ - 插件不支持 read
- ~~Things 3 未完成任务~~ - 已移除

### MiniMaxi Monitoring

#### Script Locations

| 脚本 | 用途 |
|------|------|
| `/Users/bypasser/.openclaw/workspace/minimaxi_usage.sh` | 用户友好输出 |
| `/Users/bypasser/.openclaw/workspace/tools/minimaxi_check.sh` | 供 OpenClaw 调用 |

#### Usage

```bash
# 用户友好输出
./minimaxi_usage.sh

# JSON 原始输出
./minimaxi_usage.sh --json

# Cron 模式 (静默)
./minimaxi_usage.sh --cron

# OpenClaw 工具脚本
./tools/minimaxi_check.sh
```

#### Output Format (Cron)

```
USAGE_RATE=43.0000
USED_REQUESTS=258
TOTAL=600
REMAINING_REQUESTS=342
REMAINING_MS=6771666
ACTION=CONTINUE
```

#### API Endpoint

- **URL:** `https://www.minimaxi.com/v1/api/openplatform/coding_plan/remains`
- **参数:** `GroupId=2017939093240942908`
- **Cookie:** 已存储在脚本中

---

## 🔧 Gateway Management

### Quick Recovery Commands

```bash
# 1. 停止 Gateway
openclaw gateway stop

# 2. 确保无残留
killall -9 openclaw-gateway 2>/dev/null

# 3. 重新启动
openclaw gateway start

# 4. 确认状态
openclaw gateway status

# 5. 启动浏览器
browser action=start profile=openclaw
```

### ❌ Wrong Way

- 直接 `kill` Gateway 进程然后手动 `nohup ... &` 启动
- 不确认状态就重复启动
- 暴力杀进程 (`killall -9`)

### ✅ Correct Way

1. **先查看状态**: `openclaw gateway status`
2. **用官方命令停止**: `openclaw gateway stop`
3. **用官方命令启动**: `openclaw gateway start`
4. **避免混合使用**:
   - launchd 管理的 Gateway (通过 `launchctl`)
   - 手动启动的 Gateway (`nohup ... &`)
   - OpenClaw.app menubar 控制

### Best Practices

| 规则 | 说明 |
|------|------|
| Gateway 管理 | 始终使用 `openclaw gateway` 子命令 |
| 杀进程 | 只在确认无官方管理时使用 `killall -9` |
| 杀 Chrome | 日常 Chrome 和托管浏览器必须互斥运行 |
| 检查端口 | `lsof -i :18800` (浏览器) / `lsof -i :18789` (Gateway) |

---

## 🌐 Browser Profile Configuration

### Profile Types

| Profile | 用途 | CDP 端口 |
|---------|------|----------|
| `openclaw` | OpenClaw 托管浏览器 | 18800 |
| `chrome` | 日常 Chrome (扩展接管) | 动态分配 |

### Quick Commands

```bash
# 启动 OpenClaw 托管浏览器 (无头模式)
browser action=start profile=openclaw

# Chrome 扩展接管
browser action=navigate profile=chrome targetUrl="..."

# 截图
browser action=screenshot profile=openclaw
```

---

## 🔐 GitHub Accounts

| 场景 | 账号 | 命令 |
|------|------|------|
| **加密货币 / Solana** | `truongvknnlthao-gif` | `gh auth switch -u truongvknnlthao-gif` |
| **独立项目** | `marie6789040106650` | `gh auth switch -u marie6789040106650` |

---

## 📂 Related Documents

- `memory/SOLANA.md` - Solana 开发知识
- `memory/ESIM.md` - eSIM 业务知识
- `memory/BROWSER.md` - 浏览器自动化配置

---

*此文件独立维护，便于 OpenClaw 系统的查阅和更新。*
