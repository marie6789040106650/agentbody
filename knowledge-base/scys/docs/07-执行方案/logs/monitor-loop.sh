#!/bin/bash
# 5分钟监控循环
# 使用方法: ./monitor-loop.sh &

MONITOR_INTERVAL=300  # 5分钟
MAX_FAILURES=2  # 连续2次失败重试
SUBAGENTS=("R1-竞品调研" "R2-AI工具搭建")
FAIL_COUNT=()

# 初始化失败计数
for i in "${!SUBAGENTS[@]}"; do
    FAIL_COUNT[$i]=0
done

run_check() {
    echo "=== $(date '+%Y-%m-%d %H:%M:%S') ==="
    
    for i in "${!SUBAGENTS[@]}"; do
        subagent="${SUBAGENTS[$i]}"
        
        # 检查子代理是否存在
        status=$(openclaw sessions list --format json 2>/dev/null | grep -c "$subagent" || echo "0")
        
        if [ "$status" -gt 0 ]; then
            echo "🟢 $subagent: 运行中"
            FAIL_COUNT[$i]=0  # 重置失败计数
        else
            echo "🔴 $subagent: 未运行"
            FAIL_COUNT[$i]=$((FAIL_COUNT[$i] + 1))
            
            if [ "${FAIL_COUNT[$i]}" -ge "$MAX_FAILURES" ]; then
                echo "⚠️ 连续${MAX_FAILURES}次失败，启动重试..."
                # 启动重试子代理
                openclaw sessions spawn --label "R$((FAIL_COUNT[$i]+1))-$subagent" --task "重试任务: $subagent" --timeout 600
                FAIL_COUNT[$i]=0  # 重置计数
            fi
        fi
    done
    echo ""
}

# 主循环
while true; do
    run_check
    sleep $MONITOR_INTERVAL
done
