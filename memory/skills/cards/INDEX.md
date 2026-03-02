# Nova 技能卡片索引

> 基于 MemOS MemCube 概念 - 技能作为结构化记忆单元

## 总览

| 分类 | 数量 | 技能 |
|------|------|------|
| data-collection | 2 | apify, tavily |
| content-creation | 1 | replicate |
| automation | 2 | browser, cron |
| knowledge | 1 | knowledge-base |
| communication | 0 | - |
| **总计** | **6** | |

## 技能详情

### data-collection (数据采集)
- [apify.md](apify.md) - Apify 网页爬虫 (55+ Actors)
- [tavily.md](tavily.md) - Tavily 网络搜索

### content-creation (内容创作)
- [replicate.md](replicate.md) - Replicate AI 图片生成

### automation (自动化)
- [browser.md](browser.md) - OpenClaw 浏览器控制
- [cron.md](cron.md) - 定时任务系统

### knowledge (知识管理)
- [knowledge-base.md](knowledge-base.md) - 生财有术知识库

## 使用指南

```bash
# 列出所有技能
skill-cards.sh list

# 查看技能详情
skill-cards.sh info <名称>

# 查看统计
skill-cards.sh stats

# 追踪使用
track-usage.sh log <技能名> <success|fail>
```

## MemOS 借鉴

这些技能卡片借鉴了 MemOS 的 MemCube 概念：
- 技能 = 内容 + 元数据
- 支持版本追踪
- 支持使用统计
- 支持可靠性评估
