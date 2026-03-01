#!/bin/bash

# ========================================
# OpenClaw 清理脚本
# 使用方法: bash scripts/cleanup.sh
# ========================================

echo "🔍 OpenClaw 清理脚本"
echo "===================="
echo ""

# 1. 清理 .DS_Store
echo "🧹 清理 .DS_Store..."
find . -name ".DS_Store" -delete
echo "✅ .DS_Store 清理完成"
echo ""

# 2. 清理临时文件
echo "🧹 清理临时文件..."
find . -name "*.tmp" -delete 2>/dev/null
find . -name "*.bak" -delete 2>/dev/null
find . -name "*.deleted" -delete 2>/dev/null
echo "✅ 临时文件清理完成"
echo ""

# 3. 统计状态
echo "📊 清理后状态:"
echo "  - 根目录文件: $(ls *.md 2>/dev/null | wc -l) 个"
echo "  - 知识库文档: $(ls knowledge-base/*/*.md 2>/dev/null | wc -l) 个"
echo "  - Sessions: $(du -sh ~/.openclaw/agents/main/sessions/ | cut -f1)"
echo ""

echo "✅ 清理完成！"
