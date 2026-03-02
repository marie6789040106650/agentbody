# Message 技能卡片
id: message-001
name: 跨平台消息发送
category: communication
tags:
  - 消息
  - Telegram
  - Discord

metadata:
  created: "2026-02-09"
  updated: "2026-03-01"
  version: "1.0"
  source: "OpenClaw 内置"
  reliability: high

commands:
  - "message send --channel telegram --target <id> --message '<内容>'"

dependencies:
  - OpenClaw Gateway
  - Telegram Bot Token

usage:
  count: 50
  last_used: "2026-03-01"
  success_rate: 0.98

channels:
  - Telegram
  - Discord
  - WhatsApp

notes: |
  已配置 Telegram Bot
  安全原则: 只给自己发消息
