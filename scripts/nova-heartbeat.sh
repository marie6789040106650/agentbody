#!/bin/bash
# =============================================================================
# Nova Heartbeat Executor - 持续执行任务直到完成
# =============================================================================
# 逻辑:
# 1. 检查是否有未完成的任务 (running)
# 2. 有 → 继续执行
# 3. 无 → 从 pending 获取新任务
# 4. 无新任务 → 检查 HEARTBEAT.md
# =============================================================================

SCRIPT_DIR="$HOME/.openclaw/workspace/scripts"
TASK_CMD="$SCRIPT_DIR/nova-tasks.sh"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# 检查并继续未完成的任务
continue_running_tasks() {
    local continued=0
    
    # 检查 running 任务
    running=$($TASK_CMD next 2>/dev/null)
    
    if [ "$running" = "NO_TASKS" ]; then
        return 0
    fi
    
    if [ -n "$running" ] && [ ! "$running" = "NO_TASKS" ]; then
        log "📌 发现未完成任务，继续执行..."
        
        # 解析命令
        command=$(echo "$running" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('command',''))" 2>/dev/null)
        task_id=$(echo "$running" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id',''))" 2>/dev/null)
        
        if [ -n "$command" ]; then
            log "▶ 执行: $command"
            
            # 执行命令
            eval "$command" 2>&1
            result=$?
            
            if [ $result -eq 0 ]; then
                log "✅ 任务完成"
                $TASK_CMD complete "$task_id" success
                continued=1
            else
                log "❌ 任务失败 (exit: $result)"
                $TASK_CMD complete "$task_id" failed
                continued=1
            fi
        fi
    fi
    
    return $continued
}

# 检查新任务
check_new_tasks() {
    log "📋 检查新任务..."
    
    # 从 HEARTBEAT.md 添加任务
    if [ -f "$HOME/.openclaw/workspace/HEARTBEAT.md" ]; then
        # 检查每日任务
        if grep -q "API 工具健康检查" "$HOME/.openclaw/workspace/HEARTBEAT.md"; then
            $TASK_CMD add "API健康检查" "bash $SCRIPT_DIR/sync-api-tools.sh test" normal
        fi
        
        if grep -q "新能力发现" "$HOME/.openclaw/workspace/HEARTBEAT.md"; then
            $TASK_CMD add "能力发现" "bash $SCRIPT_DIR/discover-api.sh search AI 3" normal
        fi
    fi
    
    # 获取新任务
    task=$($TASK_CMD next 2>/dev/null)
    
    if [ "$task" = "NO_TASKS" ]; then
        log "📭 没有新任务"
        return 1
    fi
    
    if [ -n "$task" ] && [ ! "$task" = "NO_TASKS" ]; then
        log "▶ 发现新任务，执行..."
        
        command=$(echo "$task" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('command',''))" 2>/dev/null)
        task_id=$(echo "$task" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id',''))" 2>/dev/null)
        
        if [ -n "$command" ]; then
            log "▶ 执行: $command"
            
            eval "$command" 2>&1
            result=$?
            
            if [ $result -eq 0 ]; then
                log "✅ 任务完成"
                $TASK_CMD complete "$task_id" success
            else
                log "❌ 任务失败"
                $TASK_CMD complete "$task_id" failed
            fi
        fi
        return 0
    fi
    
    return 1
}

# 主循环 - 持续执行直到队列为空
main() {
    log "🚀 Nova Heartbeat 开始"
    
    # 清理旧任务
    $TASK_CMD cleanup
    
    max_iterations=10
    iterations=0
    
    # 持续执行直到没有任务
    while [ $iterations -lt $max_iterations ]; do
        iterations=$((iterations + 1))
        log "📌 第 $iterations 轮"
        
        # 1. 继续未完成任务
        if continue_running_tasks; then
            continue
        fi
        
        # 2. 检查新任务
        if check_new_tasks; then
            continue
        fi
        
        # 3. 没有任务了
        log "✅ 所有任务完成"
        break
    done
    
    log "🏁 Nova Heartbeat 结束"
}

main
