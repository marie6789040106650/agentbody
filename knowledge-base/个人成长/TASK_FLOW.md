# Task Execution Flow (自动编排模式)

> 基于 OpenClaw 官方文档优化 | 最后更新: 2026-02-06

---

## 🎯 核心理念

### 任务分类

| 任务类型 | 定义 | 执行方式 |
|----------|------|----------|
| **简单任务** | < 2分钟，单一步骤 | 直接执行 |
| **多步骤任务** | > 2分钟，多个步骤 | `sessions_spawn` (isolated) |
| **批量任务** | 多个独立操作 | 批量执行，不等待 |

---

## 📋 任务执行流程

### 收到任务

```
任务到来
    ↓
┌─────────────────────────────────────┐
| 1. 判断任务类型                     │
|    ├─ 简单任务? → 直接执行         │
|    ├─ 多步骤任务? → sessions_spawn │
|    └─ 批量任务? → 批量执行         │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
| 2. 规划执行步骤                     │
|    - 确定工具调用顺序               │
|    - 决定是否需要子代理             │
|    - 预估时间和资源                 │
└─────────────────────────────────────┘
    ↓
3. 执行
```

---

## 🚀 执行模式

### 模式 1：直接执行 (简单任务)

```
read → write → edit → 完成
```

**适用场景**：
- 单一步骤操作
- 预计 < 2 分钟
- 无需并行处理

### 模式 2：sessions_spawn (多步骤任务)

```bash
sessions_spawn \
  task="执行 P4 全部步骤..." \
  cleanup=delete \
  label="p4-execution"
```

**适用场景**：
- 多步骤操作
- 预计 > 2 分钟
- 需要独立上下文
- 可后台运行

### 模式 3：批量执行 (批量任务)

```
read(批量) → write(批量) → edit(批量) → 通知完成
```

**适用场景**：
- 多个独立操作
- 可以并行处理
- 无需等待确认

---

## 🔄 心跳集成

### 任务进行中标记

```
任务开始前:
任务进行中 = false

任务开始时:
任务进行中 = true

任务完成时:
任务进行中 = false
```

### 心跳响应

```bash
# 心跳触发时

if [ 任务进行中 == true ]; then
    # 任务进行中，跳过详细检查
    MiniMaxi 检查 (必要)
    回复 HEARTBEAT_OK
else
    # 正常心跳流程
    执行完整检查
fi
```

---

## 📝 任务执行清单

### 执行前

- [ ] 判断任务类型
- [ ] 规划执行步骤
- [ ] 确定执行模式

### 执行中

- [ ] 标记任务进行中
- [ ] 批量操作，不中断
- [ ] 使用子代理处理多步骤任务

### 执行后

- [ ] 补做心跳检查
- [ ] 更新相关文档
- [ ] 发送完成通知

---

## 🔧 常用命令

### 子代理管理

```bash
# 创建子代理 (短期任务，结束后删除)
sessions_spawn \
  task="<task description>" \
  cleanup=delete \
  label="<label>"

# 创建子代理 (长期任务，保留)
sessions_spawn \
  task="<task description>" \
  cleanup=keep \
  label="<label>"

# 查看子代理历史
sessions_history sessionKey="<key>"

# 列出会话
sessions_list
```

### 批量操作

```bash
# 批量读取
read file1.md
read file2.md
read file3.md

# 批量写入
write content=... file_path=file1.md
write content=... file_path=file2.md

# 批量编辑
edit path=file1.md oldText=... newText=...
edit path=file2.md oldText=... newText=...
```

---

## 💡 最佳实践

### 1. 任务规划

- 收到任务后，先判断类型
- 复杂任务使用子代理
- 批量任务并行处理

### 2. 执行效率

- 减少不必要的等待
- 使用批量操作
- 心跳期间继续执行

### 3. 完成收尾

- 补做心跳检查
- 更新 MEMORY.md
- 发送完成通知

---

## 📖 相关文档

- [HEARTBEAT.md](./HEARTBEAT.md) - 心跳配置
- [memory/SUBAGENTS.md](./memory/SUBAGENTS.md) - 子代理模式
- [memory/RESEARCH.md](./memory/RESEARCH.md) - 研究协议

---

*基于 OpenClaw 官方文档优化 | cron-vs-heartbeat.md*
