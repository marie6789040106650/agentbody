#!/bin/bash
# =============================================================================
# Nova 任务管理系统 - 持续执行机制 (修复版)
# =============================================================================

TASK_DIR="$HOME/.openclaw/workspace/.tasks"

init_tasks() {
    mkdir -p "$TASK_DIR"
    [ ! -f "$TASK_DIR/pending.json" ] && echo "[]" > "$TASK_DIR/pending.json"
    [ ! -f "$TASK_DIR/running.json" ] && echo "[]" > "$TASK_DIR/running.json"
    [ ! -f "$TASK_DIR/completed.json" ] && echo "[]" > "$TASK_DIR/completed.json"
}

add_task() {
    local name="$1"
    local command="$2"
    local priority="${3:-normal}"
    
    init_tasks
    
    local task_id=$(date +%s)
    
    # 使用 python 添加任务
    python3 -c "
import json

task = {
    'id': '$task_id',
    'name': '$name',
    'command': '''$command''',
    'priority': '$priority',
    'created': '$(date -Iseconds)',
    'status': 'pending',
    'attempts': 0,
    'max_attempts': 10
}

with open('$TASK_DIR/pending.json', 'r') as f:
    try:
        tasks = json.load(f)
    except:
        tasks = []

tasks.append(task)

with open('$TASK_DIR/pending.json', 'w') as f:
    json.dump(tasks, f, indent=2)
"
    
    echo "✅ 任务已添加: $name"
}

get_next_task() {
    init_tasks
    
    python3 -c "
import json

try:
    with open('$TASK_DIR/pending.json', 'r') as f:
        pending = json.load(f)
except:
    pending = []

if not pending:
    print('NO_TASKS')
    exit(0)

# 按优先级排序
priority_order = {'high': 0, 'normal': 1, 'low': 2}
pending.sort(key=lambda x: (priority_order.get(x.get('priority', 'normal'), 1), x.get('created', '')))

task = pending[0]
pending = pending[1:]

# 保存剩余的 pending
with open('$TASK_DIR/pending.json', 'w') as f:
    json.dump(pending, f, indent=2)

# 移动到 running
task['status'] = 'running'
task['started'] = '$(date -Iseconds)'
task['attempts'] = task.get('attempts', 0) + 1

try:
    with open('$TASK_DIR/running.json', 'r') as f:
        running = json.load(f)
except:
    running = []

running.append(task)

with open('$TASK_DIR/running.json', 'w') as f:
    json.dump(running, f, indent=2)

print(json.dumps(task))
"
}

complete_task() {
    local task_id="$1"
    local status="$2"
    
    python3 -c "
import json

try:
    with open('$TASK_DIR/running.json', 'r') as f:
        running = json.load(f)
except:
    running = []

task = None
for t in running:
    if str(t.get('id')) == '$task_id':
        task = t
        running.remove(t)
        break

if task:
    task['status'] = '$status'
    task['completed'] = '$(date -Iseconds)'
    
    with open('$TASK_DIR/running.json', 'w') as f:
        json.dump(running, f, indent=2)
    
    try:
        with open('$TASK_DIR/completed.json', 'r') as f:
            completed = json.load(f)
    except:
        completed = []
    
    completed.append(task)
    
    with open('$TASK_DIR/completed.json', 'w') as f:
        json.dump(completed, f, indent=2)
    
    print(f'✅ Task $task_id completed: $status')
else:
    print(f'⚠️ Task $task_id not found')
"
}

status() {
    init_tasks
    echo "=== Nova 任务状态 ==="
    
    for state in pending running completed; do
        count=$(python3 -c "
import json
try:
    with open('$TASK_DIR/${state}.json', 'r') as f:
        print(len(json.load(f)))
except:
    print(0)
" 2>/dev/null)
        echo "$state: $count"
    done
    
    echo ""
    echo "=== Pending 任务 ==="
    cat "$TASK_DIR/pending.json" 2>/dev/null | python3 -m json.tool 2>/dev/null || echo "无"
    
    echo ""
    echo "=== Running 任务 ==="
    cat "$TASK_DIR/running.json" 2>/dev/null | python3 -m json.tool 2>/dev/null || echo "无"
}

cleanup() {
    python3 -c "
import json
from datetime import datetime, timedelta

for state in ['completed', 'running']:
    try:
        with open(f'$TASK_DIR/{state}.json', 'r') as f:
            tasks = json.load(f)
        
        cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
        tasks = [t for t in tasks if t.get('completed', t.get('started', '')) > cutoff]
        
        with open(f'$TASK_DIR/{state}.json', 'w') as f:
            json.dump(tasks, f, indent=2)
    except:
        pass
print('✅ 清理完成')
"
}

case "$1" in
    add)
        add_task "$2" "$3" "$4"
        ;;
    next)
        get_next_task
        ;;
    complete)
        complete_task "$2" "$3"
        ;;
    status)
        status
        ;;
    cleanup)
        cleanup
        ;;
    *)
        echo "用法: $0 <command> [args]"
        echo ""
        echo "Commands:"
        echo "  add <名称> <命令> [优先级]"
        echo "  next              获取下一个任务"
        echo "  complete <id> <success|failed> 完成任务"
        echo "  status            查看状态"
        echo "  cleanup           清理旧任务"
        ;;
esac
