# Agent-Reach 技能卡片
id: agent-reach-001
name: Agent-Reach 互联网能力工具箱
category: data-collection
tags:
  - 爬虫
  - 数据采集
  - 社交媒体

metadata:
  created: "2026-03-01"
  updated: "2026-03-01"
  version: "1.2.0"
  source: "https://github.com/Panniantong/Agent-Reach"
  reliability: medium

commands:
  - "agent-reach doctor 检查状态"
  - "agent-reach install 安装"
  - "curl https://r.jina.ai/<URL> 读取网页"

dependencies:
  - Python 3.10+
  - Node.js
  - mcporter (可选)

usage:
  count: 1
  last_used: "2026-03-01"
  success_rate: 1.0

status:
  total: 12
  available: 5
  not_available: 7

available_channels:
  - GitHub (完整)
  - YouTube (字幕 - 暂不可用: Python 3.13 SSL问题)
  - RSS (订阅)
  - Web (任意网页)
  - B站 (本地)

unavailable_channels:
  - Twitter/X (需 xreach)
  - 小红书 (需 mcporter + docker)
  - 抖音 (需 mcporter + docker)
  - LinkedIn (需额外配置)
  - Boss直聘 (需额外配置)

notes: |
  安装: python3 -m pip install agent-reach --user --break-system-packages
  状态: ~/Library/Python/3.13/bin/agent-reach doctor

### 已知问题
- YouTube: Python 3.13 SSL 兼容性问题，暂时不可用

