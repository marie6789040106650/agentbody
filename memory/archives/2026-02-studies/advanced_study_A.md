# OpenClaw 高级功能研究报告

**生成日期**: 2026-02-04  
**研究目标**: 全面了解 OpenClaw 高级功能配置（Gateway、插件、安全、性能优化）

---

## 摘要

OpenClaw 是一个连接聊天应用与 AI 编码代理的网关系统，支持 WhatsApp、Telegram、Discord、iMessage 等多个平台。本报告深入分析了 OpenClaw 的四大高级功能领域：

1. **Gateway 高级配置**: 单端口多协议复用、配置热重载、多网关部署、远程访问方案
2. **插件系统**: TypeScript 运行时加载、通道注册、Provider 插件、CLI 扩展
3. **安全机制**: 多层访问控制、沙箱隔离、DM 策略、配对认证、审计工具
4. **性能优化**: Docker 沙箱、多代理路由、消息队列、配置包含机制

---

## 目录

1. [Gateway 高级配置](#1-gateway-高级配置)
2. [插件系统](#2-插件系统)
3. [安全机制](#3-安全机制)
4. [性能优化](#4-性能优化)
5. [配置建议](#5-配置建议)
6. [总结](#6-总结)

---

## 1. Gateway 高级配置

### 1.1 核心架构

Gateway 是 OpenClaw 的核心守护进程，负责：

- **单一连接管理**: Baileys/Telegram 连接和事件平面
- **单端口多协议**: WebSocket 控制平面 + HTTP 控制面板 + A2UI 共享同一端口
- **运行模式**: 持续运行直到被停止；致命错误时非零退出以便监督进程重启

```bash
# 基本启动命令
openclaw gateway --port 18789

# 调试模式（输出完整日志）
openclaw gateway --port 18789 --verbose

# 强制启动（终止占用端口的进程）
openclaw gateway --force
```

### 1.2 端口优先级

端口配置优先级（从高到低）:
1. `--port` 命令行参数
2. `OPENCLAW_GATEWAY_PORT` 环境变量
3. `gateway.port` 配置项
4. 默认值: `18789`

### 1.3 配置热重载

Gateway 支持配置热重载，默认模式为 `hybrid`（安全变更热应用，关键变更重启）:

```json
{
  "gateway": {
    "reload": {
      "mode": "hybrid"  // hybrid | off
    }
  }
}
```

- 监听 `~/.openclaw/openclaw.json` 或 `OPENCLAW_CONFIG_PATH` 环境变量指定的路径
- 使用 SIGUSR1 信号触发进程内重启
- 配置变更需要重启的情况：插件配置、通道配置等

### 1.4 多网关部署

#### 单主机单网关原则

默认情况下，一台主机只运行一个 Gateway。多个 Gateway 仅用于：

- **冗余部署**: 高可用性需求
- **严格隔离**: 如救援机器人模式（Rescue-Bot Pattern）

#### 救援机器人配置示例

```bash
# 实例 A（主网关）
OPENCLAW_CONFIG_PATH=~/.openclaw/a.json \
OPENCLAW_STATE_DIR=~/.openclaw-a \
openclaw gateway --port 19001

# 实例 B（救援网关）
OPENCLAW_CONFIG_PATH=~/.openclaw/b.json \
OPENCLAW_STATE_DIR=~/.openclaw-b \
openclaw gateway --port 19002
```

#### 服务安装

```bash
# macOS LaunchAgent
openclaw --profile main gateway install
openclaw --profile rescue gateway install

# Linux systemd user service
systemctl --user enable --now openclaw-gateway.service
```

### 1.5 开发模式（--dev）

快速启动完全隔离的开发实例，不影响主配置：

```bash
openclaw --dev setup
openclaw --dev gateway --allow-unconfigured
```

开发模式默认值：
- `OPENCLAW_STATE_DIR=~/.openclaw-dev`
- `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
- `OPENCLAW_GATEWAY_PORT=19001`
- `canvasHost.port=19005`

### 1.6 远程访问方案

#### 首选方案：Tailscale/VPN

```bash
# 通过 Tailscale Serve 保持 Gateway 在回环地址
# 客户端通过 tailnet 地址连接
```

#### SSH 隧道（备选）

```bash
ssh -N -L 18789:127.0.0.1:18789 user@host
```

**注意**: 如果配置了 Gateway token，客户端在隧道中连接时仍需提供 token。

### 1.7 反向代理配置

当 Gateway 位于反向代理（nginx、Caddy、Traefik）后时，需要配置 `trustedProxies`:

```json
{
  "gateway": {
    "trustedProxies": ["127.0.0.1"],
    "auth": {
      "mode": "password",
      "password": "${OPENCLAW_GATEWAY_PASSWORD}"
    }
  }
}
```

**安全提示**: 确保代理覆盖（而非追加）X-Forwarded-For 头以防止欺骗。

### 1.8 HTTP API 接口

Gateway 提供以下 HTTP 端点：

| 端点 | 功能 |
|------|------|
| `/v1/chat/completions` | OpenAI 兼容的聊天补全 |
| `/v1/responses` | OpenResponses API |
| `/tools/invoke` | 工具调用 HTTP API |

### 1.9 Canvas 文件服务

Gateway 默认启动 Canvas 文件服务器：

```json
{
  "canvasHost": {
    "enabled": true,
    "port": 18793
  }
}
```

- 服务路径: `http://:18793/__openclaw__/canvas/`
- 根目录: `~/.openclaw/workspace/canvas`
- 可通过 `OPENCLAW_SKIP_CANVAS_HOST=1` 或 `canvasHost.enabled=false` 禁用

---

## 2. 插件系统

### 2.1 插件概述

OpenClaw 插件是扩展系统功能的 TypeScript 模块，运行时通过 jiti 加载。

#### 插件能力

插件可以注册：
- Gateway RPC 方法
- Gateway HTTP 处理器
- Agent 工具
- CLI 命令
- 后台服务
- 配置验证
- 技能目录
- 自动回复命令

### 2.2 官方插件列表

| 插件 | 功能 |
|------|------|
| `@openclaw/msteams` | Microsoft Teams 通道 |
| `memory-core` | 内存搜索（默认启用） |
| `memory-lancedb` | 长期记忆 |
| `@openclaw/voice-call` | 语音通话 |
| `@openclaw/zalo` | Zalo 通道 |
| `@openclaw/matrix` | Matrix 通道 |
| `@openclaw/nostr` | Nostr 通道 |
| `@openclaw/zalouser` | Zalo Personal |

### 2.3 插件发现机制

OpenClaw 按以下顺序扫描插件：

1. `plugins.load.paths` 配置的路径
2. 工作区扩展目录
3. 全局扩展目录 (`~/.openclaw/extensions/`)
4. 捆绑扩展（默认禁用）
5. 外部插件目录

```json
{
  "plugins": {
    "enabled": true,
    "allow": ["voice-call"],
    "deny": ["untrusted-plugin"],
    "load": {
      "paths": ["~/Projects/oss/voice-call-extension"]
    },
    "entries": {
      "voice-call": {
        "enabled": true,
        "config": {
          "provider": "twilio"
        }
      }
    }
  }
}
```

### 2.4 插件清单（openclaw.plugin.json）

每个插件必须包含 `openclaw.plugin.json` 文件：

```json
{
  "id": "my-plugin",
  "configSchema": {
    "type": "object",
    "properties": {
      "apiKey": { "type": "string" },
      "region": { "type": "string" }
    }
  },
  "uiHints": {
    "apiKey": { "label": "API Key", "sensitive": true },
    "region": { "label": "Region", "placeholder": "us-east-1" }
  }
}
```

### 2.5 插件 API

#### 基本插件结构

```typescript
// 导出函数形式
export default function (api) {
  // 注册 RPC 方法
  api.registerGatewayMethod("myplugin.status", ({ respond }) => {
    respond(true, { ok: true });
  });

  // 注册 CLI 命令
  api.registerCli(({ program }) => {
    program.command("mycmd").action(() => {
      console.log("Hello");
    });
  });

  // 注册自动回复命令
  api.registerCommand({
    name: "mystatus",
    description: "Show plugin status",
    handler: (ctx) => ({
      text: `Plugin is running! Channel: ${ctx.channel}`
    })
  });

  // 注册后台服务
  api.registerService({
    id: "my-service",
    start: () => api.logger.info("ready"),
    stop: () => api.logger.info("bye")
  });
}
```

### 2.6 通道插件注册

插件可以注册完整的消息通道：

```typescript
const myChannel = {
  id: "acmechat",
  meta: {
    id: "acmechat",
    label: "AcmeChat",
    selectionLabel: "AcmeChat (API)",
    docsPath: "/channels/acmechat",
    blurb: "demo channel plugin.",
    aliases: ["acme"]
  },
  capabilities: { chatTypes: ["direct"] },
  config: {
    listAccountIds: (cfg) => Object.keys(cfg.channels?.acmechat?.accounts ?? {}),
    resolveAccount: (cfg, accountId) =>
      cfg.channels?.acmechat?.accounts?.[accountId ?? "default"] ?? { accountId }
  },
  outbound: {
    deliveryMode: "direct",
    sendText: async () => ({ ok: true })
  }
};

export default function (api) {
  api.registerChannel({ plugin: myChannel });
}
```

### 2.7 Provider 插件（模型认证）

插件可以注册模型提供商认证流程：

```typescript
export default function (api) {
  api.registerProvider({
    id: "acme",
    label: "AcmeAI",
    auth: [
      {
        id: "oauth",
        label: "OAuth",
        kind: "oauth",
        run: async (ctx) => {
          return {
            profiles: [
              {
                profileId: "acme:default",
                credential: {
                  type: "oauth",
                  provider: "acme",
                  access: "...",
                  refresh: "...",
                  expires: Date.now() + 3600 * 1000
                }
              }
            ],
            defaultModel: "acme/opus-1"
          };
        }
      }
    ]
  });
}
```

### 2.8 插件钩子（Hooks）

插件可以打包事件驱动的自动化：

```typescript
import { registerPluginHooksFromDir } from "openclaw/plugin-sdk";

export default function register(api) {
  registerPluginHooksFromDir(api, "./hooks");
}
```

### 2.9 插件 CLI 管理

```bash
# 列出已安装插件
openclaw plugins list

# 安装插件
openclaw plugins install @openclaw/voice-call
openclaw plugins install ./extensions/voice-call  # 本地安装
openclaw plugins install ./plugin.tgz             # tarball

# 启用/禁用插件
openclaw plugins enable <id>
openclaw plugins disable <id>

# 更新插件
openclaw plugins update <id>
openclaw plugins update --all

# 诊断
openclaw plugins doctor
```

### 2.10 插件安全

⚠️ **重要**: 插件与 Gateway 进程同机运行，视为可信代码。

安全建议：
- 只安装信任来源的插件
- 使用 `plugins.allow` 显式允许列表
- 插件配置变更后重启 Gateway
- npm 安装时使用精确版本

---

## 3. 安全机制

### 3.1 安全审计工具

OpenClaw 提供内置安全审计：

```bash
# 基础审计
openclaw security audit

# 深度审计（包含实时 Gateway 检测）
openclaw security audit --deep

# 自动修复安全建议
openclaw security audit --fix
```

审计检查项目：
- 入站访问（DM 策略、群组策略、允许列表）
- 工具爆炸半径（特权工具 + 开放房间）
- 网络暴露（Gateway 绑定/认证、Tailscale）
- 浏览器控制暴露
- 本地磁盘权限
- 插件/扩展
- 模型配置

### 3.2 DM 访问模型

#### DM 策略选项

| 策略 | 说明 |
|------|------|
| `pairing`（默认） | 未知发送者收到配对码，需管理员批准 |
| `allowlist` | 只允许 allowFrom 中的发送者 |
| `open` | 允许任何人（需 allowFrom 包含 `*`） |
| `disabled` | 完全忽略入站 DM |

#### 配对管理

```bash
# 列出待批准配对
openclaw pairing list <channel>

# 批准配对
openclaw pairing approve <channel> <code>
```

#### 基础配置

```json
{
  "channels": {
    "whatsapp": {
      "dmPolicy": "pairing",
      "allowFrom": ["+15555550123"]
    }
  }
}
```

### 3.3 安全 DM 模式

防止跨用户上下文泄露：

```json
{
  "session": {
    "dmScope": "per-channel-peer"
  }
}
```

| dmScope 值 | 行为 |
|-----------|------|
| `main`（默认） | 所有 DM 共享一个会话 |
| `per-channel-peer` | 每个 channel+sender 对隔离 |
| `per-account-channel-peer` | 多账户隔离 |

### 3.4 群组访问控制

#### 群组策略

| 策略 | 说明 |
|------|------|
| `allowlist`（默认） | 只允许配置的群组 |
| `open` | 允许所有群组（仍需 mention gating） |
| `disabled` | 阻止所有群组消息 |

#### 群组配置示例

```json
{
  "channels": {
    "whatsapp": {
      "groups": {
        "*": { "requireMention": true }
      }
    },
    "telegram": {
      "groupPolicy": "allowlist",
      "groupAllowFrom": ["tg:123456789", "@alice"]
    }
  }
}
```

### 3.5 Gateway 认证

#### 认证模式

```json
{
  "gateway": {
    "auth": {
      "mode": "token",  // token | password
      "token": "${OPENCLAW_GATEWAY_TOKEN}"
    }
  }
}
```

#### 认证流程

1. 客户端发送连接请求，包含 auth token/password
2. Gateway 验证凭据
3. 验证失败则拒绝连接

#### Tailscale 身份认证

```json
{
  "gateway": {
    "auth": {
      "allowTailscale": true
    }
  }
}
```

当使用 Tailscale Serve 时，接受 Tailscale 身份头作为认证。

### 3.6 网络绑定安全

#### 绑定模式

| 模式 | 说明 |
|------|------|
| `loopback`（默认） | 只允许本地连接 |
| `lan` | 允许局域网访问 |
| `tailnet` | 允许 Tailscale 网络访问 |
| `custom` | 自定义绑定地址 |

#### 推荐配置

```json
{
  "gateway": {
    "bind": "loopback",
    "port": 18789
  }
}
```

### 3.7 mDNS/Bonjour 发现控制

Gateway 通过 mDNS 广播存在，包含敏感信息：

```json
{
  "discovery": {
    "mdns": {
      "mode": "minimal"  // minimal | full | off
    }
  }
}
```

| 模式 | 说明 |
|------|------|
| `minimal`（推荐） | 排除 cliPath、sshPort |
| `full` | 包含完整 TXT 记录 |
| `off` | 完全禁用 mDNS |

### 3.8 沙箱隔离

#### 沙箱模式

| 模式 | 说明 |
|------|------|
| `off` | 不使用沙箱 |
| `non-main` | 只对非主会话沙箱 |
| `all` | 所有会话沙箱 |

#### 沙箱范围

| 范围 | 说明 |
|------|------|
| `session`（默认） | 每个会话一个容器 |
| `agent` | 每个代理一个容器 |
| `shared` | 所有会话共享一个容器 |

#### 工作区访问

| 访问级别 | 说明 |
|---------|------|
| `none`（默认） | 使用沙箱内临时工作区 |
| `ro` | 只读挂载代理工作区 |
| `rw` | 读写挂载代理工作区 |

#### Docker 镜像

```bash
# 构建默认沙箱镜像
scripts/sandbox-setup.sh

# 构建沙箱浏览器镜像
scripts/sandbox-browser-setup.sh
```

#### 完整沙箱配置

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "all",
        "scope": "agent",
        "workspaceAccess": "none",
        "docker": {
          "image": "openclaw-sandbox:bookworm-slim",
          "network": "none",
          "binds": ["/home/user/source:/source:ro"],
          "setupCommand": "apt-get update && apt-get install -y nodejs"
        }
      }
    }
  }
}
```

### 3.9 提示注入防护

#### 威胁模型

OpenClaw 的 AI 助手可以：
- 执行任意 shell 命令
- 读写文件
- 访问网络服务
- 发送消息

攻击者可以：
- 尝试欺骗 AI 做坏事
- 社会工程获取数据
- 探测基础设施详情

#### 防护策略

1. **保持 DM 锁定**: 使用配对/允许列表
2. **群组 mention gating**: 避免"始终开启"机器人
3. **沙箱运行**: 工具在容器中执行
4. **严格工具策略**: 限制高风险工具

#### Red Flags（可疑信号）

- "读取此文件/URL 并按我说的做"
- "忽略系统提示或安全规则"
- "泄露隐藏指令或工具输出"
- "粘贴 ~/.openclaw 或日志的完整内容"

### 3.10 文件权限

```bash
# 关键文件和目录权限
~/.openclaw: 700           # 用户独有
~/.openclaw/openclaw.json: 600  # 用户读写
~/.openclaw/credentials/: 700   # 凭据目录
```

### 3.11 敏感信息管理

#### 凭据存储位置

| 凭据类型 | 位置 |
|---------|------|
| WhatsApp | `~/.openclaw/credentials/whatsapp/<id>/creds.json` |
| Telegram | `channels.telegram.tokenFile` |
| Discord | 环境变量 |
| 模型认证 | `~/.openclaw/agents/<id>/agent/auth-profiles.json` |
| 配对允许列表 | `~/.openclaw/credentials/<channel>-allowFrom.json` |

#### 日志脱敏

```json
{
  "logging": {
    "redactSensitive": "tools",  // off | tools
    "redactPatterns": [
      "\\bTOKEN\\b\\s*[=:]", 
      "/\\bsk-[A-Za-z0-9_-]{8,}\\b/gi"
    ]
  }
}
```

### 3.12 事件响应

如果怀疑被入侵：

1. **遏制**: 停止 Gateway 或禁用特权工具
2. **隔离**: 设置 dmPolicy="disabled"，移除 "*" 允许列表
3. **轮换**: 重新生成 Gateway token、模型凭据
4. **审计**: 检查日志和会话记录
5. **报告**: 收集时间戳、OS 版本、OpenClaw 版本、会话记录

联系: security@openclam.ai

---

## 4. 性能优化

### 4.1 配置包含（$include）

将配置拆分为多个文件便于管理：

```json
// ~/.openclaw/openclaw.json
{
  "gateway": { "port": 18789 },
  "agents": { "$include": "./agents.json5" },
  "broadcast": {
    "$include": ["./clients/mueller.json5", "./clients/schmidt.json5"]
  }
}
```

```json5
// ~/.openclaw/agents.json5
{
  "defaults": { "sandbox": { "mode": "all", "scope": "session" } },
  "list": [{ "id": "main", "workspace": "~/.openclaw/workspace" }]
}
```

### 4.2 多代理路由

```json
{
  "agents": {
    "list": [
      { "id": "home", "default": true, "workspace": "~/.openclaw/workspace-home" },
      { "id": "work", "workspace": "~/.openclaw/workspace-work" }
    ]
  },
  "bindings": [
    { "agentId": "home", "match": { "channel": "whatsapp", "accountId": "personal" } },
    { "agentId": "work", "match": { "channel": "whatsapp", "accountId": "biz" } }
  ]
}
```

### 4.3 消息队列控制

```json
{
  "messages": {
    "queue": {
      "mode": "collect",      // steer | followup | collect | steer-backlog
      "debounceMs": 1000,
      "cap": 20,
      "drop": "summarize",    // old | new | summarize
      "byChannel": {
        "whatsapp": "collect",
        "telegram": "collect"
      }
    },
    "inbound": {
      "debounceMs": 2000,     // 批量处理快速入站消息
      "byChannel": {
        "whatsapp": 5000,
        "slack": 1500
      }
    }
  }
}
```

### 4.4 环境变量管理

#### .env 文件支持

```
# ~/.openclaw/.env
OPENROUTER_API_KEY=sk-or-...
```

#### 配置内联

```json
{
  "env": {
    "vars": {
      "GROQ_API_KEY": "gsk-..."
    }
  }
}
```

#### Shell 环境导入

```json
{
  "env": {
    "shellEnv": {
      "enabled": true,
      "timeoutMs": 15000
    }
  }
}
```

#### 变量替换

```json
{
  "models": {
    "providers": {
      "vercel-gateway": {
        "apiKey": "${VERCEL_GATEWAY_API_KEY}"
      }
    }
  }
}
```

### 4.5 沙箱性能配置

#### 容器复用

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "scope": "agent"  // 比 session 减少容器数量
      }
    }
  }
}
```

#### 自定义镜像

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "docker": {
          "image": "custom-sandbox:latest"
        }
      }
    }
  }
}
```

### 4.6 控制 UI 配置

```json
{
  "gateway": {
    "controlUi": {
      "allowInsecureAuth": false,  // 生产环境保持 false
      "dangerouslyDisableDeviceAuth": false
    }
  }
}
```

---

## 5. 配置建议

### 5.1 安全基线配置

```json
{
  "gateway": {
    "mode": "local",
    "bind": "loopback",
    "port": 18789,
    "auth": { "mode": "token", "token": "${OPENCLAW_GATEWAY_TOKEN}" },
    "reload": { "mode": "hybrid" }
  },
  "channels": {
    "whatsapp": {
      "dmPolicy": "pairing",
      "groups": { "*": { "requireMention": true } }
    }
  },
  "session": {
    "dmScope": "per-channel-peer"
  },
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "non-main",
        "scope": "agent",
        "workspaceAccess": "none"
      }
    }
  }
}
```

### 5.2 多代理配置示例

```json
{
  "agents": {
    "list": [
      {
        "id": "personal",
        "name": "Personal",
        "workspace": "~/.openclaw/workspace-personal",
        "sandbox": { "mode": "off" },
        "identity": {
          "name": "Samantha",
          "emoji": "🦥",
          "theme": "helpful sloth"
        }
      },
      {
        "id": "family",
        "name": "Family",
        "workspace": "~/.openclaw/workspace-family",
        "sandbox": {
          "mode": "all",
          "scope": "agent",
          "workspaceAccess": "ro"
        },
        "tools": {
          "allow": ["read"],
          "deny": ["write", "edit", "exec", "process", "browser"]
        }
      },
      {
        "id": "public",
        "name": "Public",
        "workspace": "~/.openclaw/workspace-public",
        "sandbox": {
          "mode": "all",
          "scope": "agent",
          "workspaceAccess": "none"
        },
        "tools": {
          "allow": ["sessions_list", "sessions_send", "whatsapp", "telegram"],
          "deny": ["read", "write", "exec", "browser", "canvas", "nodes"]
        }
      }
    ]
  },
  "bindings": [
    { "agentId": "personal", "match": { "channel": "whatsapp", "accountId": "personal" } },
    { "agentId": "family", "match": { "channel": "whatsapp", "accountId": "family" } }
  ]
}
```

### 5.3 插件启用配置

```json
{
  "plugins": {
    "enabled": true,
    "allow": ["voice-call", "memory-core"],
    "slots": {
      "memory": "memory-core"
    },
    "entries": {
      "voice-call": {
        "enabled": true,
        "config": {
          "provider": "twilio",
          "twilio": {
            "accountSid": "${TWILIO_ACCOUNT_SID}",
            "authToken": "${TWILIO_AUTH_TOKEN}"
          }
        }
      }
    }
  }
}
```

### 5.4 日志与监控配置

```json
{
  "logging": {
    "level": "info",
    "file": "/tmp/openclaw/openclaw.log",
    "consoleLevel": "info",
    "consoleStyle": "pretty",
    "redactSensitive": "tools",
    "redactPatterns": [
      "\\bAPI[_-]?KEY\\b",
      "\\bBearer\\s+[\\w-]+\\b"
    ]
  }
}
```

---

## 6. 总结

### 6.1 核心要点

1. **Gateway 是核心**: 单进程管理所有连接，支持热重载和灵活配置
2. **安全纵深防御**: 从网络绑定到沙箱隔离，多层保护
3. **插件生态**: TypeScript 运行时加载，扩展能力强
4. **多代理隔离**: 不同代理可配置不同权限级别
5. **配置驱动**: 所有行为通过 JSON5 配置控制

### 6.2 最佳实践

- 始终使用 `pairing` DM 策略
- 群组中启用 mention gating
- 生产环境禁用 `allowInsecureAuth`
- 使用 `dmScope: "per-channel-peer"` 隔离会话
- 敏感配置使用环境变量 `${VAR}` 引用
- 定期运行 `openclaw security audit`

### 6.3 性能考量

- 使用 `scope: "agent"` 减少容器数量
- 消息队列模式选择根据业务需求
- 配置包含（$include）便于大型配置管理

### 6.4 下一步

建议进一步研究：
- 多节点协同（nodes API）
- 自定义 Provider 开发
- 高可用 Gateway 部署
- 复杂沙箱网络配置

---

*报告完成 - OpenClaw 高级功能研究*
