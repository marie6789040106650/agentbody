# OpenClaw Managed Browser 使用指南

> **状态**: ✅ 默认浏览器控制方式
> **最后更新**: 2026-02-10

---

## 📊 配置总结

### 当前使用的浏览器控制方式

| 方式 | 状态 | 说明 |
|------|------|------|
| **OpenClaw Managed Browser** | ✅ 默认 | 独立的 Chrome 实例，橙色 UI |
| agent-browser | ❌ 已卸载 | 不再使用 |
| Playwright | ❌ 已卸载 | 不再使用 |
| Chrome extension relay | ❌ 已移除 | 不再需要 |

### 配置文件

**主配置**: `~/.openclaw/openclaw.json`

```json5
{
  "browser": {
    "enabled": true,
    "defaultProfile": "openclaw",
    "headless": false,
    "noSandbox": false,
    "color": "#FF4500",
    "profiles": {
      "openclaw": {
        "cdpPort": 18800,
        "color": "#FF4500"
      }
    }
  }
}
```

---

## 🚀 快速开始

### 方法 1: 使用 CLI 命令

```bash
# 启动 managed Chrome
openclaw browser --browser-profile openclaw start

# 打开知识星球
openclaw browser --browser-profile openclaw open https://wx.zsxq.com/

# 查看当前标签页
openclaw browser --browser-profile openclaw tabs

# 截图
openclaw browser --browser-profile openclaw screenshot

# 快照（获取页面元素）
openclaw browser --browser-profile openclaw snapshot

# 关闭
openclaw browser --browser-profile openclaw stop
```

### 方法 2: 使用 OpenClaw Chrome 命令（简单版）

```bash
# 打开知识星球
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command start

# 检查状态
/Users/bypasser/.openclaw/workspace/openclaw-chrome.command status
```

### 方法 3: 使用 Agent 工具

在代码中：

```javascript
{
  browser: {
    action: "open",
    profile: "openclaw",
    targetUrl: "https://wx.zsxq.com/"
  }
}
```

---

## 📁 登录状态管理

### 登录状态文件

| 文件 | 用途 | 包含内容 |
|------|------|----------|
| `zsxq-auth.json` | 知识星球登录状态 | zsxq_access_token, user_id, member_number |
| `scys-auth.json` | SCYS 登录状态 | 登录令牌 |

**位置**: `/Users/bypasser/.openclaw/workspace/`

### 加载登录状态

在 Managed Chrome 中登录后，状态会自动保存到配置目录。

**配置目录**:
```
/Users/bypasser/.openclaw/browser/openclaw/user-data/Default/
```

---

## 🎯 核心原则

✅ **使用 OpenClaw Managed Browser**
- 独立的 Chrome 实例
- 橙色 UI 标识
- 完整的浏览器控制功能

✅ **不使用外部工具**
- 不使用 Playwright
- 不使用 agent-browser
- 不使用 Chrome extension relay

✅ **独立配置**
- 使用 OpenClaw 独有的 Chrome 配置目录
- 与用户 Chrome 完全隔离
- 安全的自动化环境

---

## 🔧 配置详情

### Managed Browser 特点

1. **独立进程**: 独立的 Chrome 进程，不会干扰用户 Chrome
2. **橙色 UI**: 默认使用橙色主题，便于识别
3. **CDP 控制**: 通过 Chrome DevTools Protocol 控制
4. **完整功能**: 支持点击、输入、截图、快照等所有操作

### 端口配置

| 端口 | 用途 |
|------|------|
| 18800 | Managed Chrome CDP 端口 |
| 18789 | OpenClaw Gateway 端口 |

---

## 📋 常用命令速查

| 操作 | 命令 |
|------|------|
| 启动浏览器 | `openclaw browser --profile openclaw start` |
| 打开网页 | `openclaw browser --profile openclaw open <url>` |
| 关闭浏览器 | `openclaw browser --profile openclaw stop` |
| 查看标签页 | `openclaw browser --profile openclaw tabs` |
| 截图 | `openclaw browser --profile openclaw screenshot` |
| 页面快照 | `openclaw browser --profile openclaw snapshot` |
| 点击元素 | `openclaw browser --profile openclaw click <ref>` |
| 输入文本 | `openclaw browser --profile openclaw type <ref> "text"` |

---

## 💡 最佳实践

### 1. 登录流程

```bash
# 1. 启动浏览器
openclaw browser --profile openclaw start

# 2. 打开登录页面
openclaw browser --profile openclaw open https://wx.zsxq.com/login

# 3. 手动登录（扫码或输入密码）
# 登录后状态会自动保存

# 4. 验证登录状态
openclaw browser --profile openclaw open https://wx.zsxq.com/
```

### 2. 自动化操作

```bash
# 打开页面
openclaw browser --profile openclaw open https://wx.zsxq.com/

# 获取页面快照
openclaw browser --profile openclaw snapshot

# 点击元素（需要 ref）
openclaw browser --profile openclaw click e2

# 截图
openclaw browser --profile openclaw screenshot
```

### 3. 多步骤工作流

```bash
# 打开页面
openclaw browser --profile openclaw open https://wx.zsxq.com/

# 等待页面加载
openclaw browser --profile openclaw wait --load networkidle

# 执行操作
openclaw browser --profile openclaw click e2
openclaw browser --profile openclaw type e3 "text"

# 截图记录
openclaw browser --profile openclaw screenshot
```

---

## 🛠️ 故障排除

### 问题 1: 浏览器无法启动

**错误**: `Browser disabled`

**解决**:
1. 检查配置: `openclaw browser status`
2. 启用浏览器: 在 `openclaw.json` 中设置 `"browser.enabled": true`
3. 重启 Gateway

### 问题 2: CDP 连接失败

**错误**: `Cannot connect to browser`

**解决**:
1. 检查端口: 默认 18800
2. 确认浏览器已启动
3. 检查防火墙设置

### 问题 3: 登录状态丢失

**解决**:
1. 确认在正确的配置目录中登录
2. 检查配置目录权限
3. 重新登录并验证状态文件

---

## 📖 相关文档

| 文档 | 说明 |
|------|------|
| [OpenClaw Browser 文档](docs/tools/browser.md) | 官方浏览器控制文档 |
| [Browser Login 文档](docs/tools/browser-login.md) | 登录相关说明 |
| [OPENCLAW_CHROME_GUIDE.md](OPENCLAW_CHROME_GUIDE.md) | OpenClaw Chrome 配置说明 |

---

## 🎉 优势总结

| 优势 | 说明 |
|------|------|
| **简单** | 不需要安装额外工具 |
| **安全** | 独立的 Chrome 配置 |
| **可靠** | 官方支持，与 OpenClaw 深度集成 |
| **功能完整** | 支持所有浏览器操作 |

---

*创建时间: 2026-02-10*
*版本: v1.0*
