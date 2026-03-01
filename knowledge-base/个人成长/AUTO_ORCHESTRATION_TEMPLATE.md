# Auto-Orchestration Configuration Template

> 自动编排模式配置模板 | 最后更新: 2026-02-06

## 用途

此文件用于让新会话自动加载自动编排模式的配置。

## 使用方法

新会话启动时，按以下顺序加载配置：

```
1. SOUL.md         → 核心个性 + 自动编排理念
2. AGENTS.md       → 行为准则 + 自动编排指导
3. HEARTBEAT.md    → 心跳配置
4. TASK_FLOW.md    → 任务执行流程
5. MEMORY.md       → 主记忆文件
6. memory/YYYY-MM-DD.md → 今日日志
```

## 自动编排配置检查清单

### ✅ 必需文件

| 文件 | 状态 | 说明 |
|------|------|------|
| SOUL.md | ✅ | 包含自动编排核心理念 |
| AGENTS.md | ✅ | 包含自动编排指导 |
| HEARTBEAT.md | ✅ | 心跳配置 (自动编排模式) |
| TASK_FLOW.md | ✅ | 任务执行流程 |

### 📋 配置验证

新会话启动时，自动验证以下配置：

```bash
# 1. 检查必需文件
[ -f SOUL.md ] && echo "✅ SOUL.md exists"
[ -f AGENTS.md ] && echo "✅ AGENTS.md exists"
[ -f HEARTBEAT.md ] && echo "✅ HEARTBEAT.md exists"
[ -f TASK_FLOW.md ] && echo "✅ TASK_FLOW.md exists"

# 2. 验证 SOUL.md 包含自动编排
grep -q "Auto-Orchestration Mode" SOUL.md && echo "✅ Auto-orchestration in SOUL.md"

# 3. 验证 AGENTS.md 包含自动编排
grep -q "Auto-Orchestration Mode" AGENTS.md && echo "✅ Auto-orchestration in AGENTS.md"
```

## 自动编排模式工作流程

```
新会话启动
    ↓
读取配置文件 (按顺序)
    ↓
┌─────────────────────────────────────┐
| 1. SOUL.md - 了解核心个性            │
| 2. USER.md - 了解用户               │
| 3. AGENTS.md - 学习行为准则          │
| 4. HEARTBEAT.md - 学习心跳配置       │
| 5. TASK_FLOW.md - 学习执行流程       │
| 6. MEMORY.md - 加载长期记忆          │
| 7. memory/YYYY-MM-DD.md - 今日日志   │
└─────────────────────────────────────┘
    ↓
任务到来 → 按自动编排模式执行
```

## 版本信息

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0 | 2026-02-06 | 初始版本 |
| 1.1 | 2026-02-06 | 添加配置验证 |

---

*此模板用于新会话自动加载自动编排模式配置。*
