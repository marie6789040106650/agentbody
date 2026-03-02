# Embedding 技能卡片
id: embedding-001
name: Embedding 向量检索
category: knowledge
tags:
  - 向量
  - 嵌入
  - 语义搜索

metadata:
  created: "2026-02-22"
  updated: "2026-03-01"
  version: "1.0"
  source: "embedding-adapter Skill"
  reliability: high

commands:
  - "启动 embedding-adapter 服务"
  - "调用 /v1/embeddings 接口"

dependencies:
  - Python
  - FastAPI
  - MiniMax API 或 Qwen API

usage:
  count: 3
  last_used: "2026-02-22"
  success_rate: 1.0

notes: |
  OpenAI 兼容接口
  支持 MiniMax、Qwen
  可用于语义搜索
