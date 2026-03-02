# Tavily 技能卡片
id: tavily-001
name: Tavily 网络搜索
category: data-collection
tags:
  - 搜索
  - 新闻
  - 研究

metadata:
  created: "2026-02-12"
  updated: "2026-03-01"
  version: "1.0"
  source: "官方文档"
  reliability: high

commands:
  - "tavily-cli.sh <搜索词> [结果数] [深度]"

dependencies:
  - TVLY_KEY (5个)

usage:
  count: 50
  last_used: "2026-03-01T18:41"
  success_rate: 0.98

notes: |
  统一 Key 管理，支持自动轮换
  搜索结果包含来源、摘要、深度研究模式
