# Replicate 技能卡片
id: replicate-001
name: Replicate AI 图片生成
category: content-creation
tags:
  - AI绘图
  - 图片生成
  - Flux

metadata:
  created: "2026-02-10"
  updated: "2026-03-01"
  version: "1.0"
  source: "官方文档"
  reliability: high

commands:
  - "cd ~/.openclaw/workspace/skills/replicate && node replicate.js call <模型> <提示词>"

dependencies:
  - REPLICATE_API_TOKEN
  - Node.js

usage:
  count: 5
  last_used: "2026-03-01T13:42"
  success_rate: 1.0

models:
  - black-forest-labs/flux-schnell
  - black-forest-labs/flux-pro

cost: "$0.003/张"

notes: |
  支持 Flux DALL-E Leonardo AI 等模型
  可用于公众号封面、海报等
