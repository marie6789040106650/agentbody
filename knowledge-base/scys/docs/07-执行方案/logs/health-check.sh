#!/bin/bash
# 子代理健康检查脚本
# 每5分钟自动执行

LOG_FILE="/Users/bypasser/.openclaw/workspace/knowledge-base/scys/docs/07-执行方案/logs/health-check.log"
SUBAGENTS=("Day1-竞品调研" "Day1-AI工具搭建" "R1-竞品调研")

echo "=== $(date '+%Y-%m-%d %H:%M:%S') 健康检查 ===" >> "$LOG_FILE"

for subagent in "${SUBAGENTS[@]}"; do
    status=$(openclaw sessions list --format json 2>/dev/null | grep -c "$subagent" || echo "0")
    if [ "$status" -gt 0 ]; then
        echo "🟢 $subagent: 正常" >> "$LOG_FILE"
    else
        echo "🔴 $subagent: 未运行，需要重试" >> "$LOG_FILE"
    fi
done

echo "---" >> "$LOG_FILE"
