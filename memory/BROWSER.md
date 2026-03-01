# Browser Automation Configuration

> 独立记忆文件 | 最后更新: 2026-02-06

---

## 🌐 默认浏览器模式

### 配置决定

| 项目 | 值 | 原因 |
|------|-----|------|
| **默认模式** | 无头模式 (headless=true) | 更快速度，适合后端任务 |
| **Profile** | openclaw | 完全隔离 |

### 启动命令

```bash
# 默认使用无头模式
browser action=start profile=openclaw

# 明确指定无头模式
browser action=start profile=openclaw headless=true

# 需要可视化时
browser action=start profile=openclaw headless=false
```

---

## 📋 浏览器模式选择规则

### 根据任务类型选择

| 任务类型 | 模式 | Profile | 原因 |
|----------|------|---------|------|
| 需要可视化交互 | OpenClaw 托管 | `openclaw` headless=false | 需要查看页面、操作UI |
| 截图/页面验证 | 无头模式 | `openclaw` headless=true | 速度快，支持截图 |
| 后端任务/自动化 | 无头模式 | `openclaw` headless=true | 不需要界面，更快 |
| 调试问题 | OpenClaw 托管 | `openclaw` headless=false | 需要查看实时页面 |

### 决策流程

```
任务需要可视化吗？
├─ 是 → 使用 OpenClaw 托管 (headless=false)
└─ 否 → 使用无头模式 (headless=true)
```

---

## 🔧 无头模式交互能力

### 支持的操作

| 操作 | 命令 | 说明 |
|------|------|------|
| 页面导航 | `browser action=navigate` | 打开 URL |
| 元素定位 | selector | CSS/XPath 选择器 |
| 点击 | `act kind=click` | 点击元素 |
| 输入 | `act kind=type` | 键盘输入 |
| 截图 | `action=screenshot` | 页面截图 |
| DOM 提取 | `action=snapshot` | 获取 DOM 结构 |
| 表单自动化 | act | 填表单、提交 |
| 滚动/拖拽 | act | 页面滚动 |

### 原理

> 无头模式 = 无窗口显示，但 CDP (Chrome DevTools Protocol) 正常工作

所有交互通过命令执行，结果通过返回数据获取。

### 调试方式

```bash
1. 截图确认页面状态
   browser action=screenshot profile=openclaw

2. snapshot 查看 DOM 结构
   browser action=snapshot profile=openclaw

3. act 返回执行结果
   browser action=act profile=openclaw
```

---

## 📦 Browser Profile

### Profile 类型

| Profile | 用途 | CDP 端口 | 隔离性 |
|---------|------|----------|--------|
| `openclaw` | OpenClaw 托管浏览器 | 18800 | ✅ 完全独立 |
| `chrome` | 日常 Chrome | 动态 | ❌ 共享配置 |

### 使用示例

```bash
# 启动 OpenClaw 托管浏览器 (无头模式)
browser action=start profile=openclaw

# 启动 OpenClaw 托管浏览器 (可视化模式)
browser action=start profile=openclaw headless=false

# Chrome 扩展接管 (需要先附加标签页)
browser action=navigate profile=chrome targetUrl="..."

# 截图
browser action=screenshot profile=openclaw

# 无头模式任务
browser action=start profile=openclaw headless=true
```

---

## 🧩 Browser Extensions

### 下载位置

```
~/.openclaw/workspace/extensions/
├── ublock-origin.crx   4.1M  广告拦截
└── json-viewer.crx     310K  JSON查看
```

### 安装方法

```bash
# 1. 启动浏览器
browser action=start profile=openclaw

# 2. 打开扩展页面
chrome://extensions/

# 3. 开启开发者模式

# 4. 拖入 .crx 文件
```

---

## ⚠️ Browser Relay 经验

### 卸载历史

| 项目 | 值 |
|------|-----|
| **状态** | 已卸载 (2026-02-02) |
| **原因** | 与 OpenClaw 托管浏览器冲突 |

### 卸载操作

1. 删除 `~/.openclaw/browser/chrome-extension/` 目录
2. 清理 Preferences 中的扩展引用
3. 创建备份: `Preferences.bak.*`

### 问题症状

```
ERROR: "Chrome extension relay is running, but no tab is connected"
```

### 解决方案

- 使用 OpenClaw 托管浏览器 (`profile=openclaw`)
- 避免同时运行日常 Chrome 和托管浏览器

---

## 🔧 快速命令参考

### 浏览器管理

```bash
# 启动浏览器 (默认无头模式)
browser action=start profile=openclaw

# 启动浏览器 (可视化模式)
browser action=start profile=openclaw headless=false

# 停止浏览器
browser action=stop profile=openclaw

# 查看状态
browser action=status profile=openclaw
```

### 页面操作

```bash
# 打开网页
browser action=navigate targetUrl="https://example.com"

# 截图
browser action=screenshot profile=openclaw

# 获取 DOM
browser action=snapshot profile=openclaw

# 点击元素
browser action=act profile=openclaw kind=click selector="#button"

# 输入文字
browser action=act profile=openclaw kind=type selector="#input" text="hello"
```

---

## 📂 Related Documents

- `memory/OPENCLAW.md` - OpenClaw 系统配置
- `memory/ESIM.md` - eSIM 业务知识
- `memory/SOLANA.md` - Solana 开发知识

---

*此文件独立维护，便于浏览器自动化配置的查阅和更新。*
