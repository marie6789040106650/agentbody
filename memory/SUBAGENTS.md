# Sub-Agents Pattern & Configuration

> 独立记忆文件 | 最后更新: 2026-02-06

---

## 🎯 核心理念

### 闭环思维

每任务必须有产出、有记录、有验收

| 环节 | 说明 | 产出 |
|------|------|------|
| 规划 | 明确任务目标 | TODO.md |
| 执行 | 子代理执行 | 具体产出 |
| 验收 | 主代理验收 | 确认通过 |
| 记录 | 更新文档 | MEMORY.md |

### 主代理与子代理分工

| 角色 | 职责 | 示例 |
|------|------|------|
| **主代理** | 规划、验收、驱动 | 我 |
| **子代理** | 并行执行具体任务 | monitoring-agent, build-agent |

---

## 🤖 子代理执行模式

```
主代理 (我)
    │
    ├── 规划任务 → 写入 TODO.md
    ├── 验收结果 → 确认产出
    └── 驱动子代理 → 启动/监控
         │
         ├── monitoring-agent → 监控下载
         ├── build-agent → 构建程序
         ├── deploy-agent → 部署程序
         └── test-agent → 运行测试
```

---

## 📋 子代理创建规则

### 判断标准

| 任务特征 | 创建子代理 | 说明 |
|----------|------------|------|
| 耗时 > 5 分钟 | ✅ | 后台执行，不阻塞主流程 |
| 需要持续监控 | ✅ | 如 LLVM 下载 |
| 独立可执行 | ✅ | 无需人工干预 |
| 并行任务 | ✅ | 多任务同时进行 |
| 简单任务 (< 5分钟) | ❌ | 直接执行 |
| 需要交互 | ❌ | 主代理处理 |
| 决策类 | ❌ | 主代理处理 |

### 自主创建流程

```
任务到来
    ↓
判断复杂度
    ↓
┌─────────────────────────────────────┐
│ 复杂任务 (>5分钟/需监控/并行)?       │
│ ├─ 是 → 创建子代理                  │
│ └─ 否 → 直接执行                   │
└─────────────────────────────────────┘
    ↓
    ↓ 创建子代理
    ├── 规划任务目标
    ├── 定义验收标准
    └── 记录到 SUB_AGENTS_PLAN.md
```

### 决策示例

| 任务 | 复杂度 | 决策 | 原因 |
|------|--------|------|------|
| LLVM 下载监控 | 高 | ✅ 子代理 | 需持续监控数小时 |
| .so 构建 | 高 | ✅ 子代理 | 耗时 30 分钟 |
| 部署程序 | 中 | ✅ 子代理 | 可独立执行 |
| 整理文档 | 低 | ❌ 直接执行 | 只需 5 分钟 |
| 规划任务 | 低 | ❌ 直接执行 | 决策类 |

---

## 📊 验收标准模板

```markdown
**验收标准**:
- [ ] 产出文件/结果
- [ ] 验证命令
- [ ] 主代理确认
```

### 实际验收标准

| 阶段 | 验收标准 |
|------|----------|
| LLVM | `llvm-config --version` 返回 21.1.8 |
| 构建 | `.so` 文件生成在 `target/deploy/` |
| 部署 | 程序 ID 生成，`solana program show <ID>` 成功 |
| 测试 | `anchor test` 通过 |

---

## 🔀 模型动态选择

### 两种模型对比

| 特征 | MiniMax | Qwen |
|------|---------|------|
| **模型 ID** | minimax-portal/MiniMax-M2.1 | qwen-portal/coder-model |
| **特点** | 推理能力强，适合复杂任务 | 快速/便宜，适合简单任务 |
| **成本** | 较高 | 较低 |
| **速度** | 较慢 | 较快 |

### 模型选择策略

| 任务类型 | 推荐模型 | 原因 |
|----------|----------|------|
| 复杂代码/调试 | **MiniMax** | 推理能力强 |
| 简单任务/查询 | **Qwen** | 快速/便宜 |
| 学习笔记整理 | **Qwen** | 简单任务 |
| 调试构建错误 | **MiniMax** | 需要强推理 |
| 长时间监控 | **Qwen** | 成本敏感 |
| 架构研究 | **MiniMax** | 需要深度分析 |

### 实际应用示例

| 子代理 | 任务 | 模型 | 原因 |
|--------|------|------|------|
| monitoring-agent | LLVM 监控 | **Qwen** | 简单检查 |
| build-agent | .so 构建 | **MiniMax** | 可能遇到复杂错误 |
| test-agent | 测试调试 | **MiniMax** | 需要分析错误 |
| deploy-agent | 部署 | **Qwen** | 简单命令 |

---

## 🧪 双模型并行研究实验

### 实验概述

**目的**: 利用等待 LLVM 下载时间，让两个不同 AI 模型的子代理并行研究 OpenClaw 优化方案

**配置**:
- 子代理 A: MiniMax 模型 (推理能力强，适合复杂研究)
- 子代理 B: Qwen 模型 (快速/便宜，适合简单调研)

### 研究成果对比

| 子代理 | 模型 | 研究方向 | 产出大小 |
|--------|------|----------|----------|
| A | MiniMax | 高级功能与协作优化 | 15KB |
| B | Qwen | 效率提升与生产力 | 4KB |

### 关键发现

| 模型 | 优势 | 适合场景 |
|------|------|----------|
| **MiniMax** | 深度分析、架构研究、复杂配置建议 | 复杂问题、架构设计 |
| **Qwen** | 快速调研、最佳实践、实用技巧 | 简单任务、快速调研 |

### 实验结论

**并行研究优势**:
- ✅ 不同模型发挥各自特长
- ✅ 并行执行节省时间 (2x 效率)
- ✅ 结果互补，质量更高

---

## 🔧 子代理管理命令

### 创建子代理

```bash
# 使用 MiniMax 模型
sessions_spawn agentId='main' model='minimax-portal/MiniMax-M2.1' task='...' label='<label>'

# 使用 Qwen 模型
sessions_spawn agentId='main' model='qwen-portal/coder-model' task='...' label='<label>'

# 带超时设置
sessions_spawn agentId='main' task='...' timeoutSeconds=3600
```

### 管理子代理

```bash
# 发送消息到子代理
sessions_send sessionKey="<key>" message="<message>"

# 查看子代理历史
sessions_history sessionKey="<key>"

# 列出会话
sessions_list

# 查看状态
session_status sessionKey="<key>"
```

---

## 📁 相关文件

| 文件 | 位置 | 说明 |
|------|------|------|
| SUB_AGENTS_PLAN.md | ~/.openclaw/workspace/ | 子代理规划 |
| TODO.md | ~/.openclaw/workspace/ | 任务列表 |
| openclaw_research_A.md | ~/.openclaw/workspace/ | MiniMax 研究成果 |
| openclaw_research_B.md | ~/.openclaw/workspace/ | Qwen 研究成果 |

---

## 📂 Related Documents

- `memory/LEARNING.md` - 学习方法论与研究机制
- `memory/OPENCLAW.md` - OpenClaw 系统配置
- `memory/SOLANA.md` - Solana 开发知识

---

*此文件独立维护，便于子代理模式的查阅和配置。*
