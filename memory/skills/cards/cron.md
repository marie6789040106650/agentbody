# Automation 技能卡片
id: cron-001
name: 定时任务系统
category: automation
tags:
  - 定时
  - 自动化
  - cron

metadata:
  created: "2026-03-01"
  updated: "2026-03-01"
  version: "1.0"
  source: "OpenClaw"
  reliability: high

commands:
  - "cron 任务配置在 openclaw.json"

dependencies:
  - OpenClaw cron 工具

tasks:
  - nova-daily: "每日 6:00 & 18:00 API 测试"
  - nova-weekly: "每周日 20:00 GitHub 备份"

usage:
  count: 3
  last_used: "2026-03-01"
  success_rate: 1.0

notes: |
  已配置每日和每周定时任务
  等待 cron 触发
