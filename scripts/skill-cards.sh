#!/bin/bash
# Nova 技能卡片管理

CARDS_DIR="$HOME/.openclaw/workspace/memory/skills/cards"

case "$1" in
  list)
    echo "=== Nova 技能卡片 ==="
    ls -1 "$CARDS_DIR"/*.md 2>/dev/null | xargs -I {} basename {} .md
    ;;
  info)
    if [ -f "$CARDS_DIR/$2.md" ]; then
      cat "$CARDS_DIR/$2.md"
    else
      echo "技能 $2 不存在"
    fi
    ;;
  stats)
    echo "=== 技能统计 ==="
    echo "总技能数: $(ls -1 "$CARDS_DIR"/*.md 2>/dev/null | wc -l)"
    echo ""
    echo "按分类:"
    grep -h "^category:" "$CARDS_DIR"/*.md 2>/dev/null | sort | uniq -c
    ;;
  *)
    echo "用法: $0 <command> [args]"
    echo ""
    echo "Commands:"
    echo "  list           列出所有技能"
    echo "  info <名称>    查看技能详情"
    echo "  stats          技能统计"
    ;;
esac
