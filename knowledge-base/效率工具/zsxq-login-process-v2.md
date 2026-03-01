# 知识星球登录操作流程（优化版）

> **版本**: v2.0
> **创建时间**: 2026-02-10
> **问题修复**: 针对之前遇到的浏览器窗口管理问题

---

## 🎯 目标

可靠地登录知识星球，并保存状态供后续访问。

---

## ❌ 之前的错误操作

### 错误1: 并行启动多个子代理
```bash
# 错误：同时启动3个不同模型的子代理
sessions_spawn --model MiniMax-M2.1 ...
sessions_spawn --model vision-model ...
sessions_spawn --model coder-model ...
```
**问题**: 每个子代理都尝试打开浏览器，造成窗口冲突

### 错误2: 多次保存状态
```bash
# 错误：不确定哪个窗口有登录状态
npx agent-browser state save zsxq-auth.json (多次)
```
**问题**: 可能保存了无效的空白状态

### 错误3: 状态获取不完整
```bash
# 错误：使用 agent-browser state save
# 但浏览器窗口可能已经关闭
```
**问题**: 窗口关闭后无法获取状态

---

## ✅ 优化后的正确流程

### Step 1: 清理旧窗口

```bash
# 先关闭所有旧的浏览器窗口
npx agent-browser close
pkill -f "visible-browser"  # 关闭脚本启动的窗口
pkill -f "login-zsxq"       # 关闭登录脚本
```

### Step 2: 启动可见浏览器（单一窗口）

**方式A: 使用 Playwright 脚本（推荐）**

```bash
node login-zsxq-visible-v2.js
```

脚本内容：
```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ 
    headless: false,
    args: ['--start-maximized']
  });
  
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.setViewportSize({ width: 1280, height: 800 });
  
  await page.goto('https://wx.zsxq.com/login', { waitUntil: 'networkidle' });
  
  console.log('✅ 浏览器窗口已打开');
  console.log('📍 请扫码登录');
  
  // 等待用户操作，不自动关闭
  await new Promise(() => {}); // 永久等待
})();
```

**方式B: 使用 agent-browser（无头模式转有头）**

```bash
# agent-browser 默认无头模式
# 需要使用 Playwright 脚本才有有头模式
```

### Step 3: 用户扫码登录

1. 在可见浏览器窗口中操作
2. 点击"获取登录二维码"
3. 扫码并确认登录
4. 确认页面显示"知识星球首页"而非登录页

### Step 4: 保存状态（登录成功后立即执行）

**关键：登录成功后立即保存状态**

```javascript
// 在同一个 Playwright 脚本中
(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  await page.goto('https://wx.zsxq.com/login');
  await page.click('button:has-text("获取登录二维码")');
  
  // ... 用户扫码登录 ...
  
  // ✅ 登录成功后立即保存状态
  await context.storageState({ path: 'zsxq-auth.json' });
  console.log('✅ 登录状态已保存到 zsxq-auth.json');
  
  await browser.close();
})();
```

### Step 5: 验证状态

```javascript
// test-zsxq-state.js
(async () => {
  const { chromium } = require('playwright');
  
  const browser = await chromium.launch();
  const context = await browser.newContext({
    storageState: 'zsxq-auth.json'  // 加载保存的状态
  });
  
  const page = await context.newPage();
  await page.goto('https://wx.zsxq.com/', { waitUntil: 'networkidle' });
  
  const title = await page.title();
  console.log('页面标题:', title);
  
  if (!title.includes('登录')) {
    console.log('✅ 登录状态有效！');
  } else {
    console.log('❌ 登录状态无效，仍需重新登录');
  }
  
  await browser.close();
})();
```

---

## 📋 完整脚本清单

| 脚本 | 用途 | 命令 |
|------|------|------|
| `login-zsxq-visible-v2.js` | 启动可见浏览器，等待登录 | `node login-zsxq-visible-v2.js` |
| `save-zsxq-state.js` | 登录成功后保存状态 | 在登录脚本中自动执行 |
| `test-zsxq-state.js` | 验证登录状态 | `node test-zsxq-state.js` |
| `access-zsxq-loggedin.js` | 使用保存的状态访问 | `node access-zsxq-loggedin.js` |

---

## 🚨 常见问题排查

### 问题1: 浏览器窗口一闪而过

**原因**: 脚本执行完毕自动关闭

**解决**: 
- 确保脚本中有等待机制
- 使用 `await new Promise(() => {})` 保持打开

### 问题2: 状态文件不完整

**原因**: 登录成功后没有立即保存

**解决**: 
- 在登录确认后立即执行 `storageState`
- 不要关闭浏览器后再保存

### 问题3: 状态加载后仍显示登录页

**原因**: cookie 可能已过期或不完整

**解决**:
- 检查 `zsxq-auth.json` 中的 cookie 数量
- 确保有 `zsxq_access_token` 等关键 cookie
- 重新登录并保存

---

## 💡 最佳实践

1. **单一窗口原则**: 整个登录流程只使用一个浏览器窗口
2. **立即保存**: 登录成功后立即保存状态
3. **及时验证**: 保存后立即验证状态是否有效
4. **避免并行**: 不要同时启动多个登录相关的子代理

---

## 📁 文件位置

所有脚本保存在: `/Users/bypasser/.openclaw/workspace/`

```
*.js                      # 登录和状态管理脚本
zsxq-auth.json           # 登录状态文件
zsxq-*.png               # 截图文件
```

---

*创建时间: 2026-02-10*
*版本: v2.0*
