#!/bin/bash
# =============================================================================
# Unified Key Manager - 多工具 API Key 自动轮换管理
# =============================================================================
# 支持: Tavily, Apify 等多种工具的 API Key 管理
# 逻辑: 优先使用上次成功的 Key → 失败自动切换 → 成功后保存状态
# =============================================================================

# 配置目录
KEY_MANAGER_DIR="$HOME/.openclaw/workspace/.keys"
STATE_DIR="$KEY_MANAGER_DIR/state"

# 初始化目录
init_dirs() {
    mkdir -p "$KEY_MANAGER_DIR"
    mkdir -p "$STATE_DIR"
}

# 获取指定工具的 Key 列表
# 参数: $1=工具名 (如 tavily, apify)
# 返回: 空格分隔的 Key 列表
get_keys() {
    local tool="$1"
    source "$HOME/.openclaw/workspace/.env" 2>/dev/null
    
    case "$tool" in
        tavily)
            echo "$TVLY_KEY_1 $TVLY_KEY_2 $TVLY_KEY_3 $TVLY_KEY_4 $TVLY_KEY_5"
            ;;
        apify)
            echo "$APIFY_TOKEN $APIFY_TOKEN_2 $APIFY_TOKEN_3"
            ;;
        replicate)
            echo "$REPLICATE_API_TOKEN"
            ;;
        *)
            echo ""
            ;;
    esac
}

# 获取状态文件路径
get_state_file() {
    local tool="$1"
    echo "$STATE_DIR/${tool}.state"
}

# 加载上次成功的 Key 索引
load_last_working() {
    local tool="$1"
    local state_file=$(get_state_file "$tool")
    
    if [ -f "$state_file" ]; then
        cat "$state_file"
    else
        echo "0"
    fi
}

# 保存成功的 Key 索引
save_last_working() {
    local tool="$1"
    local index="$2"
    local state_file=$(get_state_file "$tool")
    echo "$index" > "$state_file"
}

# 获取下一个可用 Key
# 参数: $1=工具名
# 返回: index:key 格式
get_next_key() {
    local tool="$1"
    local keys=($(get_keys "$tool"))
    local last_index=$(load_last_working "$tool")
    local total=${#keys[@]}
    
    if [ $total -eq 0 ]; then
        echo "ERROR: No keys found for $tool"
        return 1
    fi
    
    # 从上次成功的 Key 开始尝试
    for i in $(seq 0 $((total - 1))); do
        local idx=$(( (last_index + i) % total ))
        local key="${keys[$idx]}"
        if [ -n "$key" ]; then
            echo "$idx:$key"
            return 0
        fi
    done
    
    echo "ERROR: No valid keys found"
    return 1
}

# 标记 Key 成功
mark_success() {
    local tool="$1"
    local index="$2"
    save_last_working "$tool" "$index"
}

# 标记 Key 失败 (切换到下一个)
mark_failure() {
    local tool="$1"
    local current_index="$2"
    local keys=($(get_keys "$tool"))
    local total=${#keys[@]}
    local next_index=$(( (current_index + 1) % total ))
    save_last_working "$tool" "$next_index"
}

# 列出所有已配置的工具
list_tools() {
    echo "tavily apify replicate"
}

# 显示工具的 Key 状态
status() {
    local tool="$1"
    local keys=($(get_keys "$tool"))
    local last_index=$(load_last_working "$tool")
    
    echo "=== $tool Key Status ==="
    echo "Total Keys: ${#keys[@]}"
    echo "Last Working: ${last_index}"
    echo ""
    
    for i in "${!keys[@]}"; do
        local label="  "
        if [ $i -eq $last_index ]; then
            label="▶ "
        fi
        local masked="${keys[$i]:0:8}...${keys[$i]: -4}"
        echo "${label}Key $((i+1)): $masked"
    done
}

# 初始化
init_dirs

# 命令行接口
case "${1:-status}" in
    get)
        get_next_key "$2"
        ;;
    success)
        mark_success "$2" "$3"
        ;;
    failure)
        mark_failure "$2" "$3"
        ;;
    list)
        list_tools
        ;;
    status)
        if [ -n "$2" ]; then
            status "$2"
        else
            for tool in $(list_tools); do
                status "$tool"
                echo ""
            done
        fi
        ;;
    *)
        echo "Usage: $0 <command> [args]"
        echo ""
        echo "Commands:"
        echo "  get <tool>              获取下一个可用 Key (返回 index:key)"
        echo "  success <tool> <index>  标记 Key 成功"
        echo "  failure <tool> <index> 标记 Key 失败并切换"
        echo "  list                    列出所有已配置的工具"
        echo "  status [tool]          显示 Key 状态"
        echo ""
        echo "Examples:"
        echo "  $0 get apify           # 获取 apify 的下一个可用 Key"
        echo "  $0 success apify 0     # 标记 index 0 成功"
        echo "  $0 failure apify 0    # 标记 index 0 失败，切换到下一个"
        echo "  $0 status              # 显示所有工具状态"
        ;;
esac
