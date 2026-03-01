# Nova 主动成长定时任务

# Nova 主动成长任务 - 每天自动执行

## 每日任务 (每日 6:00 & 18:00 执行)

### 1. API 工具健康检查
```bash
~/.openclaw/workspace/scripts/sync-api-tools.sh test
```

### 2. 新能力发现
```bash
~/.openclaw/workspace/scripts/discover-api.sh search "AI" 3
```

### 3. OpenClaw 状态检查
```bash
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && nvm use default && openclaw status
```

## 每周任务 (每周日 20:00 执行)

### 1. 知识库更新
- 扫描新的 Apify Actors
- 扫描新的 Replicate 模型
- 更新知识库文档

### 2. GitHub 备份
```bash
cd ~/.openclaw/workspace && git add -A && git commit -m "Nova 每周备份" && git push backup master
```

### 3. 安全检查
- 检查 API Keys 状态
- 验证工具可用性

## 每月任务 (每月1日 9:00 执行)

### 1. 参考项目更新
- 检查 MemTensor/MemOS 更新
- 检查 Agent-Reach 更新
- 检查 Raphael-Publish 更新

### 2. 技能评估
- 评估现有技能使用率
- 规划新技能方向

---

## 执行状态

| 任务 | 频率 | 状态 |
|------|------|------|
| API 健康检查 | 每日 | ⏳ 待配置 |
| 能力发现 | 每日 | ⏳ 待配置 |
| OpenClaw 状态 | 每日 | ⏳ 待配置 |
| 每周备份 | 每周 | ⏳ 待配置 |

## 配置说明

要启用定时任务，需要在 openclaw.json 中配置 cron 工具。
