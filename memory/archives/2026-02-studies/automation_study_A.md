# OpenClaw 自动化能力研究报告

**生成日期**: 2026-02-04
**作者**: OpenClaw 研究助手
**版本**: 1.0

---

## 摘要

OpenClaw 提供了一套完整的自动化框架，包括 **Cron 调度系统**、**工作流自动化 (Lobster)**、**节点管理自动化** 和 **条件执行机制**。本报告深入分析了每个自动化组件的配置方法、使用场景和最佳实践，为用户提供全面的自动化配置指南。

---

## 目录

1. [Cron 调度系统](#1-cron-调度系统)
2. [工作流自动化 (Lobster)](#2-工作流自动化-lobster)
3. [节点管理自动化](#3-节点管理自动化)
4. [条件执行机制](#4-条件执行机制)
5. [配置示例集合](#5-配置示例集合)
6. [最佳实践](#6-最佳实践)
7. [故障排除](#7-故障排除)

---

## 1. Cron 调度系统

### 1.1 概述

OpenClaw 的 Cron 系统是 Gateway 内置的调度器，具备以下核心特性：

- **持久化存储**: 任务存储在 `~/.openclaw/cron/jobs.json`，重启后不丢失
- **双模式执行**: Main Session 和 Isolated Session
- **精确时间控制**: 支持 cron 表达式、一次性定时和固定间隔
- **灵活的交付机制**: 可配置消息交付目标和通道

### 1.2 核心概念

#### 任务 (Jobs)

Cron 任务由以下组件构成：

| 组件 | 说明 |
|------|------|
| schedule | 调度时间 (at/every/cron) |
| payload | 执行内容 (systemEvent/agentTurn) |
| delivery | 交付模式 (announce/none) |
| agentId | 绑定的 Agent ID |

#### 调度类型

```json
// 1. 一次性定时 (at)
{
  "schedule": { "kind": "at", "at": "2026-02-01T16:00:00Z" }
}

// 2. 固定间隔 (every)
{
  "schedule": { "kind": "every", "everyMs": 3600000 }
}

// 3. Cron 表达式 (cron)
{
  "schedule": { "kind": "cron", "expr": "0 7 * * *", "tz": "America/New_York" }
}
```

### 1.3 执行模式

#### Main Session 模式

```bash
# 创建一次性提醒任务
openclaw cron add \
  --name "Reminder" \
  --at "2026-02-01T16:00:00Z" \
  --session main \
  --system-event "Reminder: check the cron docs draft" \
  --wake now \
  --delete-after-run
```

**特点**:
- 使用 `systemEvent` payload
- 通过 heartbeat 运行，共享主会话上下文
- `wakeMode` 控制是否立即触发

#### Isolated Session 模式

```bash
# 创建每日早晨简报
openclaw cron add \
  --name "Morning brief" \
  --cron "0 7 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --message "Summarize overnight updates." \
  --announce \
  --channel slack \
  --to "channel:C1234567890"
```

**特点**:
- 使用 `agentTurn` payload
- 独立会话，不污染主会话历史
- 默认交付模式为 announce
- 支持模型和 thinking 覆盖

### 1.4 交付配置

```json
{
  "delivery": {
    "mode": "announce",
    "channel": "whatsapp",
    "to": "+15551234567",
    "bestEffort": true
  }
}
```

| 字段 | 可选值 | 说明 |
|------|--------|------|
| mode | announce / none | 交付模式 |
| channel | whatsapp/telegram/discord/slack/last | 消息通道 |
| to | 通道特定标识 | 收件人标识 |
| bestEffort | true/false | 失败时是否继续 |

### 1.5 配置文件

```json
{
  "cron": {
    "enabled": true,
    "store": "~/.openclaw/cron/jobs.json",
    "maxConcurrentRuns": 1
  }
}
```

禁用 Cron:
- 配置: `cron.enabled: false`
- 环境变量: `OPENCLAW_SKIP_CRON=1`

---

## 2. 工作流自动化 (Lobster)

### 2.1 概述

Lobster 是 OpenClaw 的工作流运行时，专为多步骤工具管道设计，具备：

- **确定性执行**: 管道式执行，结果可预测
- **审批门控**: 副作用操作需要明确审批
- **可恢复性**: 暂停的工作流可通过 token 恢复
- **安全隔离**: 作为本地子进程运行，无网络访问

### 2.2 为什么需要 Lobster

| 传统方式 | Lobster 方式 |
|---------|-------------|
| 多次往返调用 | 单次调用返回结构化结果 |
| LLM 编排每一步 | 运行时编排，LLM 只做决策 |
| 无法暂停恢复 | 内置审批和恢复机制 |
| 难以审计 | 管道即数据，易于日志和回放 |

### 2.3 核心概念

#### 管道 (Pipeline)

```json
{
  "action": "run",
  "pipeline": "exec --json --shell 'inbox list --json' | exec --stdin json --shell 'inbox categorize --json' | exec --stdin json --shell 'inbox apply --json' | approve --preview-from-stdin --limit 5 --prompt 'Apply changes?'",
  "timeoutMs": 30000
}
```

#### 工作流文件 (.lobster)

```yaml
name: inbox-triage
args:
  tag:
    default: "family"
steps:
  - id: collect
    command: inbox list --json
  - id: categorize
    command: inbox categorize --json
    stdin: $collect.stdout
  - id: approve
    command: inbox apply --approve
    stdin: $categorize.stdout
    approval: required
  - id: execute
    command: inbox apply --execute
    stdin: $categorize.stdout
    condition: $approve.approved
```

### 2.4 启用 Lobster

```json
{
  "tools": {
    "alsoAllow": ["lobster"]
  }
}
```

### 2.5 使用示例

#### 邮箱分类工作流

```json
{
  "action": "run",
  "pipeline": "email.triage --limit 20",
  "timeoutMs": 30000
}
```

#### 审批恢复

```json
{
  "action": "resume",
  "token": "<resumeToken>",
  "approve": true
}
```

### 2.6 LLM 任务集成

```json
{
  "plugins": {
    "entries": {
      "llm-task": { "enabled": true }
    }
  },
  "agents": {
    "list": [
      {
        "id": "main",
        "tools": { "allow": ["llm-task"] }
      }
    ]
  }
}
```

在管道中使用:

```json
{
  "action": "run",
  "pipeline": "openclaw.invoke --tool llm-task --action json --args-json '{
    \"prompt\": \"Given the input email, return intent and draft.\",
    \"input\": { \"subject\": \"Hello\", \"body\": \"Can you help?\" },
    \"schema\": {
      \"type\": \"object\",
      \"properties\": {
        \"intent\": { \"type\": \"string\" },
        \"draft\": { \"type\": \"string\" }
      },
      \"required\": [\"intent\", \"draft\"],
      \"additionalProperties\": false
    }
  }'"
}
```

---

## 3. 节点管理自动化

### 3.1 概述

节点 (Nodes) 是连接到 Gateway 的companion设备，提供：

- **Canvas 控制**: 远程截图、页面控制
- **相机功能**: 拍照、录像
- **屏幕录制**: 屏幕捕获
- **位置服务**: GPS 定位
- **系统命令**: 远程执行 shell 命令
- **通知推送**: 发送系统通知

### 3.2 节点类型

| 类型 | 平台 | 功能 |
|------|------|------|
| macOS 节点 | macOS | 完整功能集 |
| iOS 节点 | iOS | Canvas、相机、语音唤醒 |
| Android 节点 | Android | Canvas、相机、屏幕录制、SMS |
| Headless 节点 | 任意 | 系统命令执行 |

### 3.3 节点配对

```bash
# 列出待处理请求
openclaw nodes pending

# 批准节点
openclaw nodes approve <requestId>

# 列出已配对节点
openclaw nodes list

# 查看节点状态
openclaw nodes status

# 节点重命名
openclaw nodes rename --node <id> --name "Build Node"
```

### 3.4 远程节点主机配置

#### 启动节点主机 (前台)

```bash
openclaw node run --host <gateway-host> --port 18789 --display-name "Build Node"
```

#### 启动节点主机 (服务)

```bash
openclaw node install --host <gateway-host> --port 18789 --display-name "Build Node"
openclaw node restart
```

#### SSH 隧道模式

```bash
# 网关主机端
ssh -N -L 18790:127.0.0.1:18789 user@gateway-host

# 节点主机端
export OPENCLAW_GATEWAY_TOKEN="<gateway-token>"
openclaw node run --host 127.0.0.1 --port 18790 --display-name "Build Node"
```

### 3.5 命令执行

#### Canvas 控制

```bash
# 截图
openclaw nodes canvas snapshot --node <id> --format png

# 打开 URL
openclaw nodes canvas present --node <id> --target https://example.com

# 执行 JavaScript
openclaw nodes canvas eval --node <id> --js "document.title"
```

#### 相机操作

```bash
# 拍照
openclaw nodes camera snap --node <id>
openclaw nodes camera snap --node <id> --facing front

# 录像
openclaw nodes camera clip --node <id> --duration 10s
```

#### 屏幕录制

```bash
openclaw nodes screen record --node <id> --duration 10s --fps 10
```

#### 位置获取

```bash
openclaw nodes location get --node <id>
openclaw nodes location get --node <id> --accuracy precise --max-age 15000
```

#### 系统命令

```bash
# 远程执行命令
openclaw nodes run --node <id> -- echo "Hello from mac node"

# 发送通知
openclaw nodes notify --node <id> --title "Ping" --body "Gateway ready"
```

### 3.6 命令白名单

```bash
# 添加白名单命令
openclaw approvals allowlist add --node <id> "/usr/bin/uname"
openclaw approvals allowlist add --node <id> "/usr/bin/sw_vers"
```

### 3.7 Exec 节点绑定

```bash
# 全局默认
openclaw config set tools.exec.host node
openclaw config set tools.exec.security allowlist
openclaw config set tools.exec.node "<id-or-name>"

# 覆盖执行节点
/exec host=node security=allowlist node=<id-or-name>
```

---

## 4. 条件执行机制

### 4.1 Heartbeat 机制

Heartbeat 是 OpenClaw 的周期性检查机制，与 Cron 互补。

#### 配置

```json
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "activeHours": {
          "start": "08:00",
          "end": "22:00"
        },
        "includeReasoning": true,
        "prompt": "Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.",
        "ackMaxChars": 300
      }
    }
  }
}
```

#### HEARTBEAT.md 示例

```markdown
# Heartbeat checklist

- Quick scan: anything urgent in inboxes?
- If it's daytime, do a lightweight check-in if nothing else is pending.
- If a task is blocked, write down what is missing and ask for help next time.
```

### 4.2 Cron vs Heartbeat 选择指南

| 场景 | 推荐 | 原因 |
|------|------|------|
| 每 30 分钟检查收件箱 | Heartbeat | 可与其他检查批量处理 |
| 每天 9 点精确发送报告 | Cron (isolated) | 需要精确时间 |
| 监控日历事件 | Heartbeat | 自然适合周期性感知 |
| 每周深度分析 | Cron (isolated) | 独立任务，可使用不同模型 |
| 20 分钟后提醒 | Cron (main, --at) | 一次性精确计时 |
| 后台项目健康检查 | Heartbeat | 依附现有周期 |
| 多步骤工作流 | Lobster | 需要审批和恢复 |

### 4.3 Webhooks 触发

#### 启用 Webhooks

```json
{
  "hooks": {
    "enabled": true,
    "token": "shared-secret",
    "path": "/hooks"
  }
}
```

#### Wake 端点

```bash
curl -X POST http://127.0.0.1:18789/hooks/wake \
  -H 'Authorization: Bearer SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"text":"New email received","mode":"now"}'
```

#### Agent 端点

```bash
curl -X POST http://127.0.0.1:18789/hooks/agent \
  -H 'x-openclaw-token: SECRET' \
  -H 'Content-Type: application/json' \
  -d '{
    "message": "Summarize inbox",
    "name": "Email",
    "wakeMode": "next-heartbeat",
    "deliver": true,
    "channel": "last"
  }'
```

### 4.4 Gmail Pub/Sub 集成

```json
{
  "hooks": {
    "enabled": true,
    "token": "OPENCLAW_HOOK_TOKEN",
    "presets": ["gmail"],
    "mappings": [
      {
        "match": { "path": "gmail" },
        "action": "agent",
        "wakeMode": "now",
        "name": "Gmail",
        "messageTemplate": "New email from {{messages[0].from}}\nSubject: {{messages[0].subject}}\n{{messages[0].snippet}}",
        "deliver": true,
        "channel": "last"
      }
    ]
  }
}
```

### 4.5 Lobster 条件执行

在 .lobster 文件中使用条件:

```yaml
steps:
  - id: execute
    command: inbox apply --execute
    stdin: $categorize.stdout
    condition: $approve.approved
```

### 4.6 消息队列控制

```json
{
  "messages": {
    "queue": {
      "mode": "collect",
      "debounceMs": 1000,
      "cap": 20,
      "drop": "summarize",
      "byChannel": {
        "whatsapp": "collect",
        "telegram": "collect"
      }
    },
    "inbound": {
      "debounceMs": 2000,
      "byChannel": {
        "whatsapp": 5000,
        "slack": 1500
      }
    }
  }
}
```

---

## 5. 配置示例集合

### 5.1 完整自动化配置

```json
{
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "activeHours": {
          "start": "08:00",
          "end": "22:00"
        }
      }
    }
  },
  "cron": {
    "enabled": true,
    "maxConcurrentRuns": 1
  },
  "hooks": {
    "enabled": true,
    "token": "${OPENCLAW_HOOK_TOKEN}",
    "presets": ["gmail"]
  },
  "tools": {
    "alsoAllow": ["lobster"]
  }
}
```

### 5.2 多代理自动化路由

```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "default": true,
        "heartbeat": {
          "every": "30m",
          "target": "whatsapp",
          "to": "+15551234567"
        }
      },
      {
        "id": "ops",
        "heartbeat": {
          "every": "1h",
          "target": "slack",
          "to": "channel:C1234567890"
        }
      }
    ]
  },
  "bindings": [
    { "agentId": "main", "match": { "channel": "whatsapp", "accountId": "personal" } },
    { "agentId": "ops", "match": { "channel": "slack", "accountId": "alerts" } }
  ]
}
```

### 5.3 远程节点配置

```json
{
  "tools": {
    "exec": {
      "host": "node",
      "security": "allowlist",
      "node": "build-node"
    }
  }
}
```

节点端白名单 (`~/.openclaw/exec-approvals.json`):

```json
{
  "approvals": [
    {
      "command": "/usr/bin/git",
      "allowed": true
    },
    {
      "command": "/usr/bin/npm",
      "allowed": true
    }
  ]
}
```

### 5.4 邮箱自动化工作流

```yaml
# email-triage.lobster
name: email-triage
args:
  limit:
    default: 20
steps:
  - id: search
    command: gog.gmail.search --query 'newer_than:1d' --limit $args.limit --json
  - id: triage
    command: email.triage --stdin $search.stdout --json
    approval: required
  - id: draft
    command: email.draft --stdin $triage.stdout --json
    condition: $triage.needs_reply
  - id: send
    command: email.send --stdin $draft.stdout
    condition: $draft.ready
```

---

## 6. 最佳实践

### 6.1 Cron 任务设计

1. **选择正确的执行模式**
   - 需要上下文 → Main Session
   - 需要隔离 → Isolated Session

2. **合理设置交付目标**
   - 使用 `channel:last` 简化配置
   - 明确指定 `to` 避免歧义

3. **注意时区配置**
   - 使用 `--tz` 明确时区
   - 默认为本地时区

### 6.2 Lobster 工作流

1. **保持管道简单**
   - 每个步骤做一件事
   - 使用有意义的命令名称

2. **合理使用审批**
   - 副作用操作必须审批
   - 避免过度审批降低效率

3. **设置合理的超时**
   - 根据步骤复杂度调整 `timeoutMs`
   - 避免无限等待

### 6.3 Heartbeat 优化

1. **保持 HEARTBEAT.md 简洁**
   - 只包含必要检查项
   - 避免过长的提示词

2. **合理设置间隔**
   - 30 分钟是合理的默认
   - 根据需求调整

3. **使用 activeHours**
   - 避免夜间打扰
   - 节省 API 调用成本

### 6.4 节点管理

1. **安全第一**
   - 严格限制命令白名单
   - 定期审查白名单

2. **合理使用节点**
   - 根据任务选择合适的节点
   - 避免不必要的远程调用

3. **监控节点状态**
   - 定期检查节点可用性
   - 及时处理离线节点

### 6.5 成本控制

| 机制 | 成本特点 | 优化建议 |
|------|----------|----------|
| Heartbeat | 每次运行完整 agent turn | 保持 HEARTBEAT.md 简洁 |
| Cron (main) | 仅添加事件到队列 | 用于不需要独立运行的场景 |
| Cron (isolated) | 完整 agent turn | 使用便宜模型 |
| Lobster | 单次调用 | 复杂流程使用 |

---

## 7. 故障排除

### 7.1 Cron 任务不执行

```bash
# 检查 Cron 是否启用
openclaw config get cron.enabled

# 检查任务列表
openclaw cron list

# 手动运行测试
openclaw cron run <jobId> --force

# 检查日志
openclaw logs --tail
```

常见原因:
- `cron.enabled: false`
- Gateway 未持续运行
- 时区配置错误

### 7.2 Webhook 无法触发

```bash
# 验证 hooks 配置
openclaw config get hooks

# 测试连接
curl -v -X POST http://127.0.0.1:18789/hooks/wake \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"text":"test"}'
```

检查项:
- Token 是否正确
- 网络是否可达
- 防火墙设置

### 7.3 Lobster 管道失败

```bash
# 检查超时设置
# 增加 timeoutMs

# 检查输出大小
# 调整 maxStdoutBytes

# 手动运行命令测试
exec --json --shell 'your-command'
```

### 7.4 节点连接问题

```bash
# 列出节点状态
openclaw nodes status

# 检查节点描述
openclaw nodes describe --node <id>

# 验证 SSH 隧道
ssh user@gateway-host "ps aux | grep openclaw"
```

### 7.5 消息不交付

```bash
# 检查目标配置
openclaw config get channels.whatsapp

# 验证 last route
openclaw sessions --json | grep lastRoute

# 检查消息队列
openclaw gateway call messages.queues
```

---

## 附录

### A. CLI 命令速查

#### Cron 命令

```bash
# 任务管理
openclaw cron add --name "Name" --cron "0 7 * * *" --session isolated --message "..."
openclaw cron list
openclaw cron edit <jobId> --message "..."
openclaw cron remove <jobId>

# 执行控制
openclaw cron run <jobId> --force
openclaw cron runs --id <jobId> --limit 50
```

#### 节点命令

```bash
# 节点管理
openclaw nodes list
openclaw nodes status
openclaw nodes describe --node <id>
openclaw nodes rename --node <id> --name "Name"

# 节点审批
openclaw nodes pending
openclaw nodes approve <requestId>

# 节点命令
openclaw nodes run --node <id> --command
openclaw nodes notify --node <id> --title "Title" --body "Body"
openclaw nodes canvas snapshot --node <id>
openclaw nodes camera snap --node <id>
openclaw nodes location get --node <id>
```

#### 系统命令

```bash
# 心跳控制
openclaw system event --text "..." --mode now
```

### B. 参考文档

- [Cron Jobs 文档](https://docs.openclaw.ai/automation/cron-jobs)
- [Heartbeat 文档](https://docs.openclaw.ai/gateway/heartbeat)
- [Cron vs Heartbeat](https://docs.openclaw.ai/automation/cron-vs-heartbeat)
- [Webhooks 文档](https://docs.openclaw.ai/automation/webhook)
- [Lobster 文档](https://docs.openclaw.ai/tools/lobster)
- [Nodes 文档](https://docs.openclaw.ai/nodes)
- [配置参考](https://docs.openclaw.ai/gateway/configuration)

---

## 结论

OpenClaw 提供了一套强大且灵活的自动化框架：

1. **Cron 系统** 提供了精确的时间调度能力，支持多种执行模式和交付选项
2. **Lobster 工作流** 实现了复杂流程的确定性执行和审批管理
3. **节点管理** 实现了跨设备的命令执行和资源访问
4. **条件执行机制** 通过 Heartbeat、Webhooks 等实现了事件驱动的自动化

通过合理组合这些机制，用户可以构建复杂的自动化流程，实现高效的助手管理。

---

*报告结束*
