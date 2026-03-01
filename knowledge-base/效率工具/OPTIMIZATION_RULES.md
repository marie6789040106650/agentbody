# OpenClaw Workspace 优化规范

> 最后更新: 2026-02-08

## 🎯 优化目标

保持 workspace 干净、高效，只保留活跃项目。

---

## 📋 优化规则

### 1️⃣ 临时文件清理规则

| 类型 | 处理方式 | 示例 |
|------|----------|------|
| `.DS_Store` | ✅ 自动删除 | macOS 元数据 |
| `temp-*` | ⚠️ 先检查后删除 | 临时备份目录 |
| `*.log` | ✅ 自动删除 | 日志文件 |
| `*.bak` | ⚠️ 先检查后删除 | 备份文件 |
| `*~`, `*.swp` | ✅ 自动删除 | 编辑器临时文件 |
| `node_modules/` | ❌ 不清理 | 项目依赖 |

### 2️⃣ 项目归档规则

**归档条件（满足任一）**:
- ✅ 项目标记为"已完成"或"已存档"（见 MEMORY.md）
- ✅ 超过 14 天无更新且无活跃开发
- ✅ 有独立的 `archives/` 备份

**归档位置**:
```
archives/
├── esim-landing-mvp/
├── solana-project/
└── [项目名]/
```

**归档流程**:
1. 检查 MEMORY.md 中项目状态
2. 确认无活跃开发
3. 移动到 `archives/`
4. 更新 MEMORY.md 归档信息

### 3️⃣ Git 管理规则

**定期执行**:
```bash
# 每周清理一次
git add .
git commit -m "chore: 周度清理 $(date +%Y-%m-%d)"
```

**.gitignore 建议**:
```
.DS_Store
*.log
temp-*
*.tmp
node_modules/
```

### 4️⃣ 目录结构规范

```
~/.openclaw/workspace/
├── 📁 archives/          # 已完成项目
├── 📁 skills/            # 技能
├── 📁 tools/            # 工具脚本
├── 📁 memory/           # 每日记忆
├── 📁 [活跃项目]/        # 进行中项目
└── 📄 MEMORY.md         # 长期记忆
```

### 5️⃣ 优化触发方式

| 触发方式 | 命令 |
|----------|------|
| **WhatsApp** | "运行优化检查" |
| **终端** | `./tools/optimize.sh` |
| **手动** | `cron action=run jobId=3c883ca2` |

---

## 🔄 优化检查清单

每次优化执行以下检查：

- [ ] MiniMaxi 用量状态
- [ ] Git 未跟踪文件数量
- [ ] 临时文件识别
- [ ] 待归档项目检查
- [ ] MEMORY.md 待办更新

---

## 📊 历史记录

| 日期 | 清理内容 | 状态 |
|------|----------|------|
| 2026-02-08 | 归档研究类文件 (5个 → 2个) | ✅ 完成 |
| 2026-02-08 | 归档 esim-landing-mvp, esim-project | ✅ 完成 |
| 2026-02-08 | 删除 .DS_Store, 清理 temp-openclaw-backup | ✅ 完成 |
| 2026-02-08 | 归档研究文件 (efficiency_*, openclaw_research_*) | ✅ 完成 |

### 研究文件归档详情

| 原文件 | 归档位置 |
|--------|----------|
| efficiency_study_A.md | archives/research/openclaw_efficiency_study_2026-02.md |
| efficiency_study_B.md | (删除 - 重复) |
| openclaw_research_A.md | archives/research/openclaw_advanced_features_2026-02.md |
| openclaw_research_B.md | (删除 - 重复) |
| openclaw_research_summary.md | (删除 - 空文件) |

