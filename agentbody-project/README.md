# AgentBody AI 自动化指南

## 概述

AgentBody 是一个本地运行的 AI 浏览器自动化工具，让 AI 能够：
1. 控制浏览器 - 打开网页、点击、填表
2. 任务隔离 - 每个任务独立标签页，自动清理
3. 智能复用 - 同域名导航复用标签页
4. OAuth 登录 - 检测新窗口，处理授权

## API 地址

```
http://127.0.0.1:9229
```

## 快速开始

### 1. 检查状态
```bash
curl http://127.0.0.1:9229/health
```

### 2. 启动浏览器
```bash
curl -X POST http://127.0.0.1:9229/start -H "Content-Type: application/json" -d '{"headless": false}'
```

### 3. 打开网页
```bash
# 智能打开（推荐）- 自动标签页复用
curl -X POST http://127.0.0.1:9229/smart_open -d '{"url": "https://vercel.com"}'

# 强制新建
curl -X POST http://127.0.0.1:9229/open -d '{"url": "https://github.com"}'
```

### 4. 截图让 AI 看图
```bash
curl -X POST http://127.0.0.1:9229/screenshot -d '"/tmp/screenshot.png"'
```

### 5. 点击/填写
```bash
curl -X POST http://127.0.0.1:9229/click -d '{"selector": "#login"}'
curl -X POST http://127.0.0.1:9229/fill -d '{"selector": "#email", "text": "test@test.com"}'
```

### 6. 任务结束（清理）
```bash
curl -X POST http://127.0.0.1:9229/task/end -d '{"cleanup": true}'
```

## AI 工作流程

### 完整示例：用 GitHub 登录 Vercel

```
1. /start - 启动浏览器

2. /smart_open?url=vercel.com/login - 打开登录页

3. /screenshot - 截图，AI 看图

4. /click?selector=button - 点击 GitHub 登录按钮

5. 检查返回的 new_tabs - 检测新窗口

6. /smart_open?url=github.com/oauth/authorize - 在新窗口继续

7. /fill - 填写账号密码

8. /task/end?cleanup=true - 清理
```

## 智能标签页管理

| 操作 | 行为 |
|------|------|
| smart_open(vercel.com) | 新建标签页 |
| smart_open(vercel.com/login) | 导航到同一标签页（同域名复用） |
| open(github.com) | 强制新建标签页 + 新任务 |
| task/end | 清理该任务所有标签页 |

## 选择器技巧

AI 看图后，使用正确的 CSS 选择器：

| 场景 | 选择器 |
|------|--------|
| ID | `#login` |
| Class | `.btn-primary` |
| 属性 | `button[aria-label*="GitHub"]` |
| 文本 | 不支持，用属性选择器 |

## 错误处理

| 错误 | 解决 |
|------|------|
| Browser not started | 先调用 /start |
| Element not found | 用 /screenshot 看图确认 |
| Timeout | 页面加载慢，增加等待 |

## 常用命令速查

```bash
# 启动
curl -X POST http://127.0.0.1:9229/start -d '{"headless": false}'

# 打开
curl -X POST http://127.0.0.1:9229/smart_open -d '{"url": "https://example.com"}'

# 点击
curl -X POST http://127.0.0.1:9229/click -d '{"selector": "button"}'

# 填写
curl -X POST http://127.0.0.1:9229/fill -d '{"selector": "input", "text": "hello"}'

# 截图
curl -X POST http://127.0.0.1:9229/screenshot -d '"/tmp/s.png"'

# 任务
curl http://127.0.0.1:9229/task/info
curl -X POST http://127.0.0.1:9229/task/end -d '{"cleanup": true}'

# 停止
curl -X POST http://127.0.0.1:9229/stop
```
