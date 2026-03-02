# Nova 技能卡片系统
# 基于 MemOS MemCube 概念

技能卡片 = 技能内容 + 元数据

## 卡片结构

```yaml
skill_card:
  id: "apify-001"
  name: "Apify 网页爬虫"
  category: "data-collection"
  tags: ["爬虫", "数据", "API"]
  
  # 元数据
  metadata:
    created: "2026-03-01"
    updated: "2026-03-01"
    version: "1.0"
    source: "自主探索"
    reliability: "high"  # high/medium/low
    
  # 技能内容
  commands:
    - "apify-quick search <关键词>"
    - "apify-quick profile <用户名>"
    
  # 使用记录
  usage:
    count: 5
    last_used: "2026-03-01T18:00"
    success_rate: 1.0
    
  # 依赖
  dependencies:
    - "mcpc CLI"
    - "APIFY_TOKEN"
```

## 技能分类

| 分类 | 说明 | 示例 |
|------|------|------|
| **data-collection** | 数据采集 | Apify, Tavily |
| **content-creation** | 内容创作 | Replicate, Raphael |
| **automation** | 自动化 | cron, workflows |
| **knowledge** | 知识管理 | memory, knowledge-base |
| **communication** | 通讯 | Telegram, message |

## 管理命令

```bash
# 查看所有技能
ls ~/.openclaw/workspace/skills/cards/

# 创建新技能卡片
new-skill-card <name>

# 更新使用记录
update-usage <skill-id>
```
