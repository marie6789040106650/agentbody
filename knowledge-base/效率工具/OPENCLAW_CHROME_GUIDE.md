# OpenClaw 独有 Chrome 配置使用指南

> **原则**: 不使用 Playwright，不需要插件，不需要连接扩展，使用 OpenClaw 独有的配置文件打开 Chrome

---

## ✅ 已清理的软件（完全卸载）

| 软件 | 状态 | 说明 |
|------|------|------|
| **agent-browser** | ✅ 已卸载 | npm 包（259个依赖包已移除） |
| **Playwright** | ✅ 已卸载 | npm 包（2个包已移除） |
| **Chrome for Testing** | ✅ 已卸载 | Playwright 安装的测试版 Chrome |
| **chromium_headless_shell** | ✅ 已卸载 | Playwright 安装的无头浏览器 |

## ✅ 保留的配置

### 1. 用户 Chrome 配置（完全保留，不受影响）

**目录**: `~/Library/Application Support/Google/Chrome/`

**包含**:
- ✅ Default（默认配置）
- ✅ Profile 1-14（多个用户配置）
- ✅ Guest Profile
- ✅ 扩展程序
- ✅ 书签、历史记录、密码等

**说明**: 您的所有 Chrome 数据、扩展、书签都完整保留。

### 2. OpenClaw 独有 Chrome 配置

**目录**: `/Users/bypasser/.openclaw/browser/openclaw/user-data/Default`

**用途**: OpenClaw 专用，与用户配置隔离

**包含**:
- ✅ Cookies（登录状态）
- ✅ Preferences（浏览器设置）
- ✅ 扩展程序
- ✅ 本地存储

---

## 🎯 使用的 Chrome 浏览器

**Chrome 路径**: `/Users/bypasser/Library/Application Support/Google/Chrome/Google Chrome`

**说明**:
- ✅ 使用系统安装的 Google Chrome（不是测试版）
- ✅ 与用户的 Chrome 完全独立
- ✅ 使用 OpenClaw 独有的配置目录

---

## 🚀 使用方法

### 方法 1: 使用启动脚本（推荐）

```bash
# 打开知识星球登录页
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command start

# 检查配置状态
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command status

# 打开指定 URL
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command start https://wx.zsxq.com/
```

### 方法 2: 手动启动

```bash
# 使用 OpenClaw 独有配置启动 Chrome
open -na "Google Chrome" \
    --args \
    --user-data-dir="/Users/bypasser/.openclaw/browser/openclaw/user-data/Default" \
    --start-maximized \
    --no-first-run \
    --no-default-browser-check \
    "https://wx.zsxq.com/login"
```

### 方法 3: 双击脚本文件

1. 在 Finder 中找到 `openclaw-chrome.command`
2. 双击运行
3. Chrome 将使用 OpenClaw 独有配置启动

---

## 📁 相关文件

| 文件 | 用途 |
|------|------|
| `openclaw-chrome.command` | 启动脚本（推荐使用） |
| `OPENCLAW_CHROME_GUIDE.md` | 本文档 |
| `/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/` | OpenClaw 独有配置 |

---

## 🔧 技术详情

### 目录对比

| 配置 | 路径 | 用途 |
|------|------|------|
| **用户 Chrome** | `~/Library/Application Support/Google/Chrome/` | 用户的日常 Chrome 使用 |
| **OpenClaw 独有** | `/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/` | OpenClaw 专用 |

### 浏览器路径

| 浏览器 | 路径 | 说明 |
|--------|------|------|
| **Google Chrome** | `/Users/bypasser/Library/Application Support/Google/Chrome/Google Chrome` | 系统安装的正式版 Chrome |
| Chrome for Testing | （已卸载） | Playwright 安装的测试版 |

---

## ✅ 优势

1. **完全隔离** - OpenClaw 配置与用户配置完全独立
2. **不依赖外部工具** - 不使用 Playwright、agent-browser
3. **无需插件** - 不需要任何浏览器扩展
4. **无需连接** - 不需要 Chrome 扩展连接
5. **保留用户数据** - 用户的 Chrome 配置完全不受影响

---

## 🚨 注意事项

1. **配置独立** - OpenClaw 的配置与用户配置分开存储
2. **登录状态** - 在 OpenClaw Chrome 中登录后，状态保存到 OpenClaw 配置目录
3. **数据隔离** - 两个配置完全独立，互不影响

---

## 🔄 后续操作

1. **启动 Chrome**: 运行 `openclaw-chrome.command start`
2. **在 Chrome 中登录**: 访问需要的网站并登录
3. **状态自动保存**: 登录状态会保存到 OpenClaw 配置目录
4. **下次直接使用**: 关闭后重新打开，保持登录状态

---

*创建时间: 2026-02-10*
*版本: v2.0*
