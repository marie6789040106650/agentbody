# PARL Optimization Knowledge Base
# PARL 优化知识库

> ⚠️ **此文件已合并到主文件**
> 
> - 提示词规则 → **`AGENTS.md`** (PARL-Style Task Decomposition 章节)
> - 记忆记录 → **`MEMORY.md`** (PARL Optimization 章节)
> 
> 本文件保留为**历史参考**。

---

## Core Concepts

### 1. Critical Steps

```
CriticalSteps = Σ (S_main + max S_sub)

Explanation:
- S_main: Coordinator overhead
- max S_sub: Slowest subtask execution time
- Critical path = Minimum wall-clock time
```

### 2. Spurious Parallelism

- **Phenomenon**: Spawn many subagents but no meaningful task decomposition
- **Harm**: Consumes resources but no actual speedup
- **Avoid**: Verify subtasks are truly independent

### 3. Serial Collapse

- **Phenomenon**: Has parallel capability but defaults to sequential execution
- **Cause**: Parallel signals sparse, hard to optimize
- **Avoid**: Encourage parallelism through reward mechanisms

---

## Theoretical Framework

### PARL Three-Layer Mechanism

| Mechanism | Function | OpenClaw Equivalent |
|-----------|----------|-------------------|
| Reward Shaping | Encourage parallel behavior | Prompt rules |
| Critical Steps Metric | Evaluate parallel effect | Performance recording |
| Frozen Subagents | Stable execution layer | sessions_spawn |

### OpenClaw Adaptation

```
PARL Goal: Learn optimal parallel strategies
OpenClaw Current: Manually specify concurrency
Gap: Need data-driven optimization
```

---

## Practical Techniques

### Task Decomposition

1. **Identify Dependencies**
   - A needs B's result → Must be sequential
   - A and B completely independent → Can parallelize

2. **Estimate Overhead**
   - Coordinator overhead: ~1 step
   - Subagent startup: ~N seconds
   - Result aggregation: ~M seconds

3. **Calculate Benefits**
   ```
   Sequential time: T_seq = T1 + T2 + ... + Tn
   Parallel time: T_par = T_overhead + max(T1, T2, ..., Tn) + T_agg
   Benefit: T_seq - T_par > 0 ?
   ```

### Concurrency Selection

```
Few subtasks (1-2): Sequential execution
Moderate subtasks (3-5): Partial parallel
Many subtasks (5+): Batch parallel
```

---

## References

1. PARL Original Paper (Kimi AI Research Team, 2026)
2. The Swarm Corporation PARL Implementation
3. Medium: "An Evaluation of PARL Design Philosophy"

---

*文件状态: 已合并，保留参考*
*更新日期: 2026-02-07*
