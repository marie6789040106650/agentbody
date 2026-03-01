# 磁盘空间分析报告 (mo tool)
> 分析时间: 2026-02-22

## 当前状态
| 指标 | 值 |
|------|-----|
| 总容量 | 466 GB |
| 已用 | 11 GB |
| 可用 | **22 GB** |
| 使用率 | 35% |

---

## 🔍 mo clean --dry-run 分析结果

### 用户缓存 (User Caches)
| 项目 | 大小 |
|------|------|
| User app cache | 467.4 MB |
| User app logs | 953 KB |
| Trash | 5 items |

### 浏览器缓存
| 项目 | 大小 |
|------|------|
| Chrome cache | 188.9 MB |
| Chrome GPU cache | 1.5 MB |
| Chrome component CRX cache | 684 KB |
| GoogleUpdater CRX cache | 9.6 MB |
| Comet cache | 142.8 MB |

### 开发者工具
| 项目 | 状态 |
|------|------|
| npm cache | 可清理 |
| pnpm cache | 可清理 |

---

## 📊 空间变化历史

| 时间 | 可用空间 | 备注 |
|------|----------|------|
| 2026-02-21 16:45 | 62 GB | 基准 |
| 2026-02-21 18:00 | 60 GB | -2 GB |
| 2026-02-21 ~20:00 | 20 GB | **-40 GB** |
| 2026-02-22 04:30 | 22 GB | 当前 |

---

## ⚠️ 发现

1. **Swap 使用率高** (之前观察到 86%)
2. **Rust 文档占用大** (~10GB+ in ~/.rustup)
3. **Chrome 多 Profile** (Profile 11: 9.7GB, Profile 14: 5.2GB)

---

## 🛠️ 建议清理

```bash
# 使用 mo 清理缓存
mo clean

# 或手动清理
rm -rf ~/Library/Caches/*
```
