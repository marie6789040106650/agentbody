#!/bin/bash
# Nova 技能使用追踪

USAGE_FILE="$HOME/.openclaw/workspace/memory/skills/usage.json"

log_usage() {
    local skill="$1"
    local status="$2"  # success/fail
    
    mkdir -p "$(dirname "$USAGE_FILE")"
    
    # 读取现有数据
    if [ -f "$USAGE_FILE" ]; then
        data=$(cat "$USAGE_FILE")
    else
        data="{}"
    fi
    
    # 使用 jq 更新 (如果可用)
    if command -v jq &> /dev/null; then
        echo "$data" | jq --arg skill "$skill" --arg status "$status" \
            '.[$skill].count += 1 | .[$skill].last_used = now | .[$skill].success_rate = (if $status == "success" then (.[$skill].success_rate * (.[$skill].count - 1) + 1) / .[$skill].count else (.[$skill].success_rate * (.[$skill].count - 1)) / .[$skill].count end)' > "$USAGE_FILE.tmp"
        mv "$USAGE_FILE.tmp" "$USAGE_FILE"
    else
        echo "Warning: jq not available, skipping usage log"
    fi
}

show_usage() {
    if [ -f "$USAGE_FILE" ]; then
        cat "$USAGE_FILE" | python3 -m json.tool 2>/dev/null || cat "$USAGE_FILE"
    else
        echo "No usage data yet"
    fi
}

case "$1" in
    log)
        log_usage "$2" "$3"
        ;;
    show)
        show_usage
        ;;
    *)
        show_usage
        ;;
esac
