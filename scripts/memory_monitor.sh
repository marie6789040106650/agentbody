#!/bin/bash
# 内存监控脚本 - 监控内存和Swap使用情况
# 每30秒检查一次，记录异常

LOG_FILE="$HOME/.memory_monitor.log"
ALERT_THRESHOLD_MB=1000  # Swap超过1GB时告警

echo "=== 内存监控开始 ===" >> "$LOG_FILE"
echo "时间: $(date)" >> "$LOG_FILE"

while true; do
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    
    # 获取内存信息
    MEM_INFO=$(top -l 1 -n 10 -s 0 2>/dev/null | grep "PhysMem" | head -1)
    
    # 获取Swap使用量
    SWAP_TOTAL=$(sysctl vm.swapfile 2>/dev/null | awk '{print $2}')
    if [ -n "$SWAP_TOTAL" ]; then
        SWAP_MB=$((SWAP_TOTAL / 1024 / 1024))
    else
        SWAP_MB=0
    fi
    
    # 获取内存使用最高的进程
    TOP_PROCS=$(ps aux --sort=-%mem 2>/dev/null | head -11 | tail -10 | awk '{printf "%s %s%%\n", $11, $4}')
    
    # 记录
    echo "=== $TIMESTAMP ===" >> "$LOG_FILE"
    echo "Swap: ${SWAP_MB}MB" >> "$LOG_FILE"
    echo "Memory: $MEM_INFO" >> "$LOG_FILE"
    echo "Top Processes:" >> "$LOG_FILE"
    echo "$TOP_PROCS" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    
    # 告警
    if [ $SWAP_MB -gt $ALERT_THRESHOLD_MB ]; then
        echo "🚨 ALERT: Swap使用 ${SWAP_MB}MB 超过阈值!" >> "$LOG_FILE"
    fi
    
    sleep 30
done
