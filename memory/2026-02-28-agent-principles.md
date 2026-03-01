# Session: 2026-02-28 09:57:32 UTC

- **Session Key**: agent:main:telegram:group:-1003782534970:topic:1612
- **Session ID**: 59d671fa-f9fb-4130-af89-90a648e1e622
- **Source**: telegram

## Conversation Summary

assistant: 已添加到 SOUL.md 并推送 ✅

新增内容：
- 上下文无状态化
- 原子化任务粒度
- 带状态调试
- 原生视觉走查
- Git 存档回滚
- 成本意识

这些原则会让我更可靠 👍
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2372",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

SOUL.md 使用中文和英文，哪种语言，对你效果更好？
assistant: 对我效果来说，**中文为主 + 英文术语** 混合最好：

| 内容 | 语言 | 原因 |
|------|------|------|
| 规则描述 | 中文 | 我理解更自然 |
| 配置项/术语 | 英文 | 如 `memorySearch`、`provider` |
| 命令/代码 | 英文 | 保持原样 |

当前 SOUL.md 就是这种混合方式，我觉得**不需要改**。

重要的是**一致性** — 只要整篇用同一种语言/格式，别中英文混排导致解析混乱就行。

你觉得当前混合方式可以吗？
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2374",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

我看到你加入了6条核心原则对吗？没有加入的哪些是为什么
assistant: 对，我加入了 6 条：

| 加入的 | 没加入的 |
|--------|----------|
| 上下文无状态化 | 文件权限隔离 |
| 原子化任务粒度 | |
| 带状态调试 | |
| 原生视觉走查 | |
| Git 存档回滚 | |
| 成本意识 | |

**没加入的原因**：

- **文件权限隔离** — 你之前说"暂时不需要"，因为我们现在没有多个子代理分别管理不同目录的场景

要不要把第7条也加上？或者等以后有需要再加？
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2376",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

可以先加上，以后我们会升级为多个子代理
assistant: 已添加 ✅ 现在共7条：

1. 上下文无状态化
2. 原子化任务粒度
3. 带状态调试
4. 原生视觉走查
5. Git 存档回滚
6. 文件权限隔离
7. 成本意识

推送完成 👍
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2379",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

再次思考 ，长期对我们有用的 7*24小时全栈开发的Agent Team 避坑指南 💡 首先是，搭配食用的7 条避坑指南，可以直接扔给 AI 形成记忆： 1. 拒绝“假通”测试：严禁仅用 curl 测试 API。必须通过 MCP 或 browser-use 调用真实浏览器进行端到端点击测试，防止后端数据通了但前端样式丢失或交互失效。 2. 原生视觉走查：截图后禁止让 AI 写 Python 脚本读图。直接调用AI的原生视觉能力“看”截图，让它像真实用户一样判断 UI 布局错位或渲染失败。 3. 带状态调试：放弃 Playwright 默认的无痕沙盒模式。使用 browser-use --browser real --profile "Default" 挂载本地真实 Chrome 配置（含 Cookie/Session），解决因验证码或登录态丢失导致 AI 无法进入业务页面的死结。 4. Git 存档回滚：将 Git Commit 设为“游戏存档点”。在自动化脚本中集成错误检测，一旦 AI 陷入死循环或测试连续失败，自动执行 git reset --hard 回滚至上一个稳定版本，切断错误累积。 5. 原子化任务粒度：task.json 的拆解必须极细。拒绝“完成支付功能”这种模糊指令，必须拆解为“定义数据库表”、“写后端接口”、“写前端组件”、“联调”四个独立任务。 6. 上下文“无状态”化：不要依赖长对话记忆。每次循环强制重置 Context，迫使 AI 必须通过读取 progress.txt 和文件系统来获取状态，这是保持模型长时间运行不“降智”的关键。 7. 文件权限隔离：在 Agent Team 中实施严格的目录级权限控制。Backend Agent 只能写 /api，Frontend Agent 只能写 /src，防止 AI 幻觉导致跨层级乱改代码引发灾难。 🚀 接下来的3 个升级方向，让Agent越来越好用： 1. RAG 动态知识库：为 Agent 挂载向量数据库，索引 Next.js 15、Supabase 等最新官方文档。防止模型因训练数据滞后而写出过时语法（幻觉），实现“边查文档边写代码”。 2. 成本熔断机制：在循环脚本中集成 Token 计费监控。设定阈值（如单任务耗资 >$2 或重试 >5 次），触发时自动 Kill 进程并推送到手机，防止逻辑死循环导致 API 账单爆炸。 3. Human-in-the-Loop 网关：在 task.json 引入 requires_approval 字段。对于数据库 Schema 变更、生产环境部署等高危操作，Agent 必须挂起并发送通知，等待人类回复“Approve”后方可执行。
assistant: 重新分析了这7+3条：

| 类别 | 内容 | 现状 |
|------|------|------|
| ✅ 已加入 | 原生视觉走查 | 第4条 |
| ✅ 已加入 | 带状态调试 | 第3条 |
| ✅ 已加入 | Git 存档回滚 | 第5条 |
| ✅ 已加入 | 原子化任务粒度 | 第2条 |
| ✅ 已加入 | 上下文无状态化 | 第1条 |
| ✅ 已加入 | 文件权限隔离 | 第6条 |
| ✅ 已加入 | 成本意识 | 第7条 |
| ⚠️ 遗漏 | 拒绝"假通"测试 | 可合并到"带状态调试" |
| 🚀 可升级 | RAG 动态知识库 | 暂时不需要 |
| 🚀 可升级 | Human-in-the-Loop | 暂时不需要 |

**分析**：
- 7条核心原则都已覆盖
- "拒绝假通测试"本质也是用真实浏览器测试，已被"带状态调试"涵盖
- 3个升级方向暂时用不到

**结论**：当前7条已经够用，不需要大改。

要不要微调一下表述，让"拒绝假通测试"更明确？
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2381",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

给出你的理由
assistant: 理由：

### 1. "拒绝假通测试" → 已覆盖

| 原句 | 对应现有原则 |
|------|-------------|
| 必须通过 MCP 或 browser-use 调用真实浏览器 | "带状态调试"：使用真实浏览器配置 |

本质一样：不用 curl/命令行模拟，要用真实浏览器操作。

### 2. 3个升级方向 → 暂时不需要

| 方向 | 理由 |
|------|------|
| RAG 动态知识库 | 我们有 memorySearch + 本地文档，够用 |
| Human-in-the-Loop | 暂时没有高危操作需要审批 |
| 成本熔断 | 当前任务规模还没大到需要 |

### 3. 保持简洁

原则太多会稀释重点。7条刚好覆盖核心风险。

---

**如果要加强**，可以把"拒绝假通测试"明确写进"带状态调试"里：

```
3. **带状态调试**：使用真实浏览器测试，拒绝 curl/命令行模拟...
```

要加吗？
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2383",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

同意
assistant: 已更新 ✅

"拒绝假通测试"已整合进"带状态调试"原则。

现在7条原则都到位了 👍
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "2385",
  "sender_id": "7015703628",
  "conversation_label": "BY & Inkblock id:-1003782534970 topic:1612",
  "sender": "7015703628",
  "group_subject": "BY & Inkblock",
  "is_forum": true
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

更新到GitHub仓库
assistant: 已经推送了 ✅

```
1f57b2a chore: 强化带状态调试原则，加入拒绝假通测试
e1db343 chore: 添加文件权限隔离原则（共7条）
929e2f1 chore: 添加 Agent Team 可靠原则到 SOUL.md
```

SOUL.md 最新版本已在 GitHub 上。

还有其他要处理的吗？
