# 小红书技能卡片
id: xiaohongshu-001
name: 小红书数据采集
category: data-collection
tags:
  - 小红书
  - 社交媒体
  - 数据采集

metadata:
  created: "2026-02-12"
  updated: "2026-03-01"
  version: "1.0"
  source: "xiaohongshutools"
  reliability: medium

commands:
  - "xiaohongshu search <关键词>"
  - "xiaohongshu user <用户名>"

dependencies:
  - xiaohongshutools Skill
  - Selenium Auth

usage:
  count: 10
  last_used: "2026-02-28"
  success_rate: 0.8

platforms:
  - 小红书 web

notes: |
  基于 Selenium 认证
  需要维护 Cookie 有效期
