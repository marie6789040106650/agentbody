# Nova 主动成长定时任务

> HEARTBEAT.md - OpenClaw 自动执行 (5分钟间隔)

## 持续执行机制 ✅

Nova 现在会持续执行任务直到完成：
- 每 5 分钟检查一次
- 如果有未完成任务 → 继续执行
- 如果有新任务 → 开始执行
- 任务完成后才结束

## 配置

| 项目 | 值 |
|------|-----|
| Heartbeat 间隔 | 5 分钟 |
| Active Hours | 全天 |
| 最大迭代 | 10 轮/次 |

## 管理命令

```bash
# 查看任务状态
~/.openclaw/workspace/scripts/nova-tasks.sh status

# 添加任务
~/.openclaw/workspace/scripts/nova-tasks.sh add "任务名" "命令" [优先级]

# 手动执行
~/.openclaw/workspace/scripts/nova-heartbeat.sh
```
