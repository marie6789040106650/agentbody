# CLI Commands Quick Reference

> 独立记忆文件 | 最后更新: 2026-02-06

---

## 🤖 OpenClaw CLI

### Gateway 管理

```bash
# 查看状态
openclaw gateway status

# 启动 Gateway
openclaw gateway start

# 停止 Gateway
openclaw gateway stop

# 重启 Gateway
openclaw gateway restart

# 查看帮助
openclaw gateway --help
```

### 消息发送

```bash
# Telegram
openclaw message send --channel telegram --target <user_id> --message "<text>"

# WhatsApp
openclaw message send --channel whatsapp --target <phone> --message "<text>"
```

### 浏览器控制

```bash
# 启动浏览器
browser action=start profile=openclaw

# 启动浏览器 (可视化)
browser action=start profile=openclaw headless=false

# 停止浏览器
browser action=stop profile=openclaw

# 截图
browser action=screenshot profile=openclaw

# 打开网页
browser action=navigate targetUrl="https://example.com"

# 获取 DOM
browser action=snapshot profile=openclaw
```

### 子代理管理

```bash
# 创建子代理
sessions_spawn task="<task>" agentId="<agent>" label="<label>"

# 发送消息
sessions_send sessionKey="<key>" message="<message>"

# 查看历史
sessions_history sessionKey="<key>"

# 列出会话
sessions_list
```

---

## 🐙 GitHub CLI

### 账号管理

```bash
# 查看当前账号
gh auth status

# 切换账号
gh auth switch -u <username>

# 登录
gh auth login

# 退出登录
gh auth logout
```

### 仓库操作

```bash
# 克隆仓库
gh repo clone <owner>/<repo>

# 创建仓库
gh repo create <name> --public

# 查看仓库
gh repo view <owner>/<repo>

# 列表仓库
gh repo list <owner>
```

### Pull Request

```bash
# 创建 PR
gh pr create --title "<title>" --body "<body>"

# 查看 PR
gh pr view <pr-number>

# 列表 PR
gh pr list

# 合并 PR
gh pr merge <pr-number> --squash
```

### Issues

```bash
# 创建 Issue
gh issue create --title "<title>" --body "<body>"

# 查看 Issue
gh issue view <issue-number>

# 列表 Issue
gh issue list
```

### API 调用

```bash
# 简单 API
gh api repos/<owner>/<repo>

# 带参数
gh api repos/<owner>/<repo>/issues --paginate
```

---

## 🛠️ Solana CLI

### 环境配置

```bash
# 查看配置
solana config get

# 配置 devnet
solana config set --url devnet

# 配置 mainnet-beta
solana config set --url mainnet-beta

# 配置本地
solana config set --url localhost
```

### 账户操作

```bash
# 检查余额
solana balance <address>

# 空投 SOL (devnet)
solana airdrop 2

# 生成密钥对
solana-keygen new --outfile <path>

# 显示地址
solana address
```

### 部署程序

```bash
# 部署程序
solana program deploy <program-file.so>

# 显示已部署程序
solana program show --programs

# 关闭程序
solana program close <program-address>
```

### 代币操作

```bash
# 创建代币
spl-token create-token

# 创建代币账户
spl-token create-account <token-address>

# 铸造代币
spl-token mint <token-address> <amount>

# 转账代币
spl-token transfer <token-address> <amount> <recipient-address>
```

---

## 🦀 Rust / Cargo

### 版本管理

```bash
# 查看版本
rustc --version

# 安装 nightly
rustup install nightly

# 设置默认工具链
rustup default <toolchain>

# 查看已安装工具链
rustup toolchain list

# 更新工具链
rustup update
```

### Cargo 命令

```bash
# 创建新项目
cargo new <project-name>

# 构建项目
cargo build

# 构建 SBF (Solana)
cargo build-sbf

# 清理构建缓存
cargo clean

# 添加依赖
cargo add <package>

# 更新依赖
cargo update

# 降级特定依赖
cargo update -p <package> --precise <version>
```

---

## ⚓ Anchor CLI

### 项目管理

```bash
# 创建新项目
anchor init <project-name>

# 构建项目
anchor build

# 部署到 devnet
anchor deploy

# 部署到 mainnet
anchor deploy --provider.cluster mainnet

# 运行测试
anchor test

# 验证程序
anchor verify
```

### 账户操作

```bash
# 迁移
anchor migrate

# 同步程序 ID
anchor sync-program-id <program-id>

# 展开 (expand)
anchor expand
```

---

## 🔧 自定义脚本

### MiniMaxi 用量监控

```bash
# 用户友好输出
/minimaxi_usage.sh

# JSON 原始输出
/minimaxi_usage.sh --json

# Cron 模式 (静默)
/minimaxi_usage.sh --cron

# OpenClaw 工具脚本
/tools/minimaxi_check.sh
```

### Git 操作

```bash
# 提交所有更改
git add .
git commit -m "<message>"
git push

# 查看状态
git status

# 查看差异
git diff

# 回退
git reset --hard <commit>
```

### 系统命令

```bash
# 检查磁盘空间
df -h

# 查看内存使用
free -h

# 查看进程
htop

# 检查端口占用
lsof -i :<port>
```

---

## 📋 常用组合命令

### Solana 开发环境检查

```bash
source ~/.bashrc && rustc --version && solana --version && anchor --version
```

### 构建并部署 Pinocchio 程序

```bash
cd /data/workspace/<project>
cargo build-sbf
solana program deploy target/deploy/<program>.so
```

### 快速提交代码

```bash
cd /data/workspace/solana-tasks
git add .
git commit -m "$(date +%Y-%m-%d): Update"
git push
```

### Gateway 快速恢复

```bash
openclaw gateway stop
killall -9 openclaw-gateway 2>/dev/null
openclaw gateway start
openclaw gateway status
```

---

## 📂 Related Documents

- `memory/SOLANA.md` - Solana 开发知识
- `memory/OPENCLAW.md` - OpenClaw 系统配置
- `memory/BROWSER.md` - 浏览器自动化配置

---

*此文件独立维护，便于命令行工具的快速查阅。*
