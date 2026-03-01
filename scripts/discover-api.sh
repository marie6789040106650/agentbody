#!/bin/bash
# =============================================================================
# API Tools Discovery - 自动发现新平台/模型
# =============================================================================
# 功能: 
#   - 发现 Apify 新增的 Actors/平台
#   - 发现 Replicate 新增的模型
#   - 自动更新文档
# =============================================================================

SCRIPT_DIR="$HOME/.openclaw/workspace/scripts"
KEY_MANAGER="$SCRIPT_DIR/key_manager.sh"
KNOWLEDGE_DIR="$HOME/.openclaw/workspace/knowledge-base"

# Apify 平台列表 (已知的)
PLATFORMS=("instagram" "facebook" "tiktok" "youtube" "google" "amazon" "twitter" "linkedin" "pinterest" "snapchat")

# 发现新的 Apify Actors
discover_apify() {
    echo "🔍 扫描 Apify 新平台 Actors..."
    
    for platform in "${PLATFORMS[@]}"; do
        echo -n "  检查 $platform... "
        RESULT=$($SCRIPT_DIR/apify-mcpc tools-call search-actors "keywords:=$platform" limit:=1 2>/dev/null | grep -c "Actor" || echo "0")
        if [ "$RESULT" -gt 0 ]; then
            echo "✅ 发现 Actors"
        else
            echo "❌ 无"
        fi
    done
}

# 发现 Replicate 新模型
discover_replicate() {
    echo ""
    echo "🔍 扫描 Replicate 新模型..."
    
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm use default >/dev/null 2>&1
    source ~/.openclaw/workspace/.env 2>/dev/null
    cd ~/.openclaw/workspace/skills/replicate
    
    # 获取所有模型
    node replicate.js models 2>/dev/null | grep -E "^\[" | sed 's/\[32m//g' | sed 's/\[0m//g'
}

# 搜索特定类型
search_type() {
    local type="$1"
    echo ""
    echo "🔍 搜索 $type 相关 Actors..."
    $SCRIPT_DIR/apify-mcpc tools-call search-actors "keywords:=$type" limit:=5 2>&1 | grep -E "Actor|URL" | head -20
}

# 更新知识库
update_knowledge() {
    local tool="$1"
    local content="$2"
    local file="$KNOWLEDGE_DIR/${tool}/discovered.md"
    
    mkdir -p "$(dirname "$file")"
    echo "# $tool 发现的新功能" > "$file"
    echo "" >> "$file"
    echo "更新时间: $(date)" >> "$file"
    echo "" >> "$file"
    echo "$content" >> "$file"
    
    echo "✅ 已更新 $file"
}

# 主命令
case "${1:-discover}" in
    apify)
        discover_apify
        ;;
    replicate)
        discover_replicate
        ;;
    search)
        search_type "${2:-video}"
        ;;
    all)
        discover_apify
        discover_replicate
        ;;
    *)
        echo "用法: $0 <command> [args]"
        echo ""
        echo "Commands:"
        echo "  apify    - 发现 Apify 新平台"
        echo "  replicate - 发现 Replicate 新模型"
        echo "  search <类型> - 搜索特定类型 Actors"
        echo "  all      - 完整扫描"
        ;;
esac
