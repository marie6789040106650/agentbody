#!/bin/bash
# 子代理监控脚本
# 用法: ./subagent-monitor.sh

CHECK_TIME=$(date "+%Y-%m-%d %H:%M")
MONITOR_LOG="/Users/bypasser/.openclaw/workspace/knowledge-base/scys/docs/07-执行方案/logs/subagent-monitor-log.md"
SUBAGENTS=("Day1-竞品调研" "Day1-AI工具搭建")

echo "=== 子代理状态检查 - $CHECK_TIME ==="

for subagent in "${SUBAGENTS[@]}"; do
    status=$(openclaw sessions list --format json 2>/dev/null | grep -c "$subagent" || echo "0")
    if [ "$status" -gt 0 ]; then
        echo "🟢 $subagent: 运行中"
    else
        echo "🔴 $subagent: 未运行"
    fi
done
