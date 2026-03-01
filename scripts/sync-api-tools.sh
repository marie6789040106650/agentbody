#!/bin/bash
# =============================================================================
# API Tools Sync - 自动同步工具更新
# =============================================================================
# 功能: 检查 Apify/Tavily/Replicate 官方更新，同步到本地
# 建议: 每周运行一次 `sync-api-tools`
# =============================================================================

SCRIPT_DIR="$HOME/.openclaw/workspace/scripts"
KEY_MANAGER="$SCRIPT_DIR/key_manager.sh"

echo "=== API Tools Sync $(date) ==="
echo ""

# 1. 检查 Tavily 官方
check_tavily() {
    echo "📡 检查 Tavily 官方..."
    TAVILY_DOCS=$(curl -s "https://api.tavily.com" 2>/dev/null | head -c 100)
    if [ -n "$TAVILY_DOCS" ]; then
        echo "  ✅ Tavily API 在线"
    else
        echo "  ⚠️ Tavily API 不可达"
    fi
}

# 2. 检查 Apify 官方
check_apify() {
    echo "📡 检查 Apify 官方..."
    APIFY_STATUS=$(curl -s "https://api.apify.com/v2/health" 2>/dev/null | head -c 50)
    if [ -n "$APIFY_STATUS" ]; then
        echo "  ✅ Apify API 在线"
        
        # 检查新增 Actors
        echo "  📊 检查新 Actors..."
        # TODO: 可以扩展为自动发现新 Actor
    else
        echo "  ⚠️ Apify API 不可达"
    fi
}

# 3. 检查 Replicate 官方
check_replicate() {
    echo "📡 检查 Replicate 官方..."
    REPLICATE_STATUS=$(curl -s "https://api.replicate.com/health" 2>/dev/null | head -c 50)
    if [ -n "$REPLICATE_STATUS" ]; then
        echo "  ✅ Replicate API 在线"
    else
        echo "  ⚠️ Replicate API 不可达"
    fi
}

# 4. 显示当前 Key 状态
show_status() {
    echo ""
    echo "📊 当前 Key 状态:"
    $KEY_MANAGER status
}

# 5. 测试所有工具
test_tools() {
    echo ""
    echo "🧪 测试工具功能..."
    
    # Test Tavily
    if ~/.openclaw/workspace/skills/tavily-search/tavily_cli.sh "test" 1 >/dev/null 2>&1; then
        echo "  ✅ Tavily 正常"
    else
        echo "  ❌ Tavily 失败"
    fi
    
    # Test Apify
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    nvm use default >/dev/null 2>&1
    source ~/.openclaw/workspace/.env 2>/dev/null
    
    if $SCRIPT_DIR/apify-mcpc tools-list >/dev/null 2>&1; then
        echo "  ✅ Apify 正常"
    else
        echo "  ❌ Apify 失败"
    fi
    
    # Test Replicate
    if source ~/.openclaw/workspace/.env 2>/dev/null && \
       cd ~/.openclaw/workspace/skills/replicate && \
       node replicate.js models >/dev/null 2>&1; then
        echo "  ✅ Replicate 正常"
    else
        echo "  ❌ Replicate 失败"
    fi
}

# 主命令
case "${1:-all}" in
    check)
        check_tavily
        check_apify
        check_replicate
        ;;
    status)
        show_status
        ;;
    test)
        test_tools
        ;;
    all)
        check_tavily
        check_apify
        check_replicate
        show_status
        test_tools
        ;;
    *)
        echo "用法: $0 <command>"
        echo ""
        echo "Commands:"
        echo "  check   - 检查各平台 API 状态"
        echo "  status  - 显示 Key 状态"
        echo "  test    - 测试所有工具"
        echo "  all     - 完整检查 (默认)"
        ;;
esac
