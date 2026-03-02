# Browser 技能卡片
id: browser-001
name: OpenClaw 浏览器控制
category: automation
tags:
  - 浏览器
  - 自动化
  - CDP

metadata:
  created: "2026-02-12"
  updated: "2026-03-01"
  version: "1.0"
  source: "OpenClaw 内置"
  reliability: high

commands:
  - "browser open <URL>"
  - "browser snapshot"
  - "browser act <action>"

dependencies:
  - OpenClaw Gateway
  - Chrome CDP

usage:
  count: 15
  last_used: "2026-03-01"
  success_rate: 0.95

notes: |
  通过 Chrome DevTools Protocol 控制浏览器
  支持截图、点击、填表等操作
