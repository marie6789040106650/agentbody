#!/bin/bash
# Nova 技能可靠性评估 (修复版)

ASSESS_DIR="$HOME/.openclaw/workspace/memory/skills/cards"

assess_skill() {
    local skill=$1
    local card_file="$ASSESS_DIR/${skill}.md"
    
    if [ ! -f "$card_file" ]; then
        echo "技能 $skill 不存在"
        return 1
    fi
    
    # 读取当前成功率
    local success_rate=$(grep "success_rate:" "$card_file" 2>/dev/null | head -1 | awk -F': ' '{print $2}')
    
    if [ -z "$success_rate" ]; then
        success_rate=1.0
    fi
    
    # 使用 python 计算可靠性
    local reliability=$(python3 -c "
success = float('$success_rate')
if success >= 0.9:
    print('high')
elif success >= 0.7:
    print('medium')
else:
    print('low')
")
    
    echo "=== $skill ==="
    echo "成功率: $success_rate → 可靠性: $reliability"
    
    # 更新卡片
    sed -i '' "s/^  reliability:.*/  reliability: $reliability/" "$card_file"
}

case "$1" in
    assess)
        assess_skill "$2"
        ;;
    all)
        for card in "$ASSESS_DIR"/*.md; do
            skill=$(basename "$card" .md)
            if [ "$skill" != "INDEX" ] && [ "$skill" != "README" ]; then
                assess_skill "$skill"
            fi
        done
        ;;
    *)
        echo "用法: $0 <assess|all> [技能名]"
        ;;
esac
