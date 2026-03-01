# Solana Development Knowledge Base

> 独立记忆文件 | 最后更新: 2026-02-07 09:15

---

## ⚠️ 重要规则

### Solana 安装原则

| 场景 | 工具 | 命令 |
|------|------|------|
| **macOS Solana 安装/更新** | ✅ **agave-install** | `agave-install init <version>` |
| **Homebrew 安装** | ❌ 避免 | 不完整，只包含 CLI |
| **源码编译** | ⚠️ 仅特殊需求 | 复杂，需要额外配置 |

### agave-install 使用

```bash
# 安装最新版本 (edge)
agave-install init edge

# 更新到最新
agave-install update

# 查看当前安装
agave-install info

# 清理旧版本
agave-install gc
```

### 当前版本 (2026-02-07 更新)

| 组件 | 版本 | 说明 |
|------|------|------|
| **agave-install** | 3.1.8 | macOS 安装工具 |
| **solana-cli** | 4.0.0 | CLI 版本 (Agave) |
| **commit** | eab72338 | 最新稳定版 |

---

## 🔑 GitHub 账号规则

| 场景 | 账号 | 命令 |
|------|------|------|
| **加密货币 / Solana 相关** | `truongvknnlthao-gif` | `gh auth switch -u truongvknnlthao-gif` |
| **独立项目 / 其他** | `marie6789040106650` | `gh auth switch -u marie6789040106650` |

### Solana 仓库

| 仓库 | 用途 | 状态 |
|------|------|------|
| `truongvknnlthao-gif/solana-tasks` | ✅ **主仓库** | 6 Tasks 完成 |
| `truongvknnlthao-gif/solana-dev-skill` | 开发技能 | 维护中 |

---

## 🖥️ 开发服务器

### 连接信息

```bash
# SSH 连接
ssh -i ~/.ssh/Atlas.pem admin@ec2-47-129-231-137.ap-southeast-1.compute.amazonaws.com

# 或使用别名
ssh solana-dev  # 需要在 ~/.ssh/config 中配置
```

### 服务器配置

| 项目 | 配置 |
|------|------|
| **IP** | ec2-47-129-231-137.ap-southeast-1.compute.amazonaws.com |
| **用户** | admin |
| **密钥** | ~/.ssh/Atlas.pem |
| **Region** | Singapore (ap-southeast-1) |
| **OS** | Debian 6.12.48 |

### 磁盘规划

| 目录 | 位置 | 大小 | 用途 |
|------|------|------|------|
| `/home/admin` | 系统盘 | 7.7GB | 用户配置、SSH |
| `/data/.rustup` | 数据盘 | - | Rust 工具链 |
| `/data/.cargo` | 数据盘 | - | Cargo 依赖 |
| `/data/.cache` | 数据盘 | - | Solana 缓存 |
| `/data/workspace` | 数据盘 | - | 项目代码 |

### 项目路径

```
/data/workspace/
└── solana-tasks/           # ✅ 主工作区
    ├── task3-anchor-escrow/
    ├── task4-pinocchio-vault/
    ├── task5-pinocchio-escrow/
    └── task6-pinocchio-amm/
```

---

## 🛠️ 工具链版本

### 环境对比 (2026-02-07 统一)

| 工具 | macOS | 服务器 | 状态 |
|------|-------|--------|------|
| solana-cli | **4.0.0** (Agave) | **4.0.0** (Agave) | ✅ 统一 |
| rustc | 1.95.0-nightly | 1.95.0-nightly | ✅ 统一 |
| anchor | 0.32.1 | 0.32.1 | ✅ 统一 |
| node | v22.22.0 | v22.22.0 | ✅ 统一 |

### macOS Homebrew solana

- **状态**: ❌ 已卸载 (2026-02-07)
- **原因**: 将在 2026-04-27 被 Homebrew 禁用
- **替代方案**: 使用 `agave-install` 安装

### 版本验证命令

```bash
# 服务器
ssh solana-dev 'export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH" && solana --version'

# macOS (zsh)
export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH" && solana --version
```

---

## 📚 学习进度 (Blueshift Challenge)

### ✅ 已完成 (6/6)

| Task | 框架 | 状态 | 提交记录 |
|------|------|------|----------|
| 1 | TypeScript + Web3.js | ✅ 通过 | Mint Token |
| 2 | Anchor | ✅ 通过 | Vault |
| 3 | Anchor | ✅ 通过 | Escrow |
| 4 | Pinocchio | ✅ 通过 | Vault |
| 5 | Pinocchio | ✅ 通过 | Escrow |
| 6 | Pinocchio | ✅ 通过 | AMM |

### 仓库提交历史

```
cbc3361 Task 6: Native AMM with Pinocchio + constant-product-curve
43080e4 Organize all tasks: Task3-6 with source code and .so files
```

---

## 🔧 开发命令速查

### Anchor 项目

```bash
# 创建新项目
anchor init <project-name>

# 构建
anchor build

# 部署到 devnet
anchor deploy

# 运行测试
anchor test
```

### Pinocchio 项目

```bash
# 添加依赖
cargo add pinocchio pinocchio-system pinocchio-token pinocchio-associated-token-account
cargo add --git="https://github.com/deanmlittle/constant-product-curve" constant-product-curve

# 构建 SBF (Solana Berkeley Packet Filter)
cargo build-sbf

# 清理构建缓存
rm -rf target
```

### Solana CLI

```bash
# 配置 devnet
solana config set --url devnet

# 检查余额
solana balance

# 空投 SOL (devnet)
solana airdrop 2
```

---

## 🍎 本地 macOS 开发环境

### 安装信息

| 项目 | 值 |
|------|-----|
| **安装时间** | 2026-02-06 |
| **安装方式** | Homebrew + cargo |
| **安装时长** | ~8 分钟 |

### 工具链版本

```
rustc 1.86.0 (默认)
rustc 1.95.0-nightly (已激活)
llvm-config 21.1.8
solana-cli 1.18.20
anchor-cli 0.32.1
```

### 环境变量配置

```bash
# ~/.zshrc 已添加
export PATH="$HOME/.cargo/bin:$PATH"
export LLVM_PATH="/usr/local/opt/llvm"
export PATH="/usr/local/opt/llvm/bin:$PATH"
```

### 工作目录版本覆盖

**注意:** 在 workspace 目录下，Rust 版本会显示为 1.75.0-dev（因为 sbf 工具链配置），实际版本是 1.86.0。

```bash
# 验证真实版本 (在 workspace 外)
cd ~ && rustc --version
```

### Rust 工具链列表

| 工具链 | 用途 |
|--------|------|
| stable (1.86.0) | 默认工具链 |
| nightly-x86_64-apple-darwin | Solana SBF 编译 |
| sbf | Solana 专用工具链 |
| solana | Solana 专用工具链 |

### 安装来源

| 组件 | 来源 | 镜像 |
|------|------|------|
| Rust | rustup | rust-lang.org (官方) |
| LLVM | Homebrew | brew |
| Solana | Homebrew | brew |
| Anchor | cargo | crates.io |

### Rust nightly 镜像

#### 中国镜像 (网络慢时使用)

```bash
# 临时设置
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static

# 永久设置
echo 'export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static' >> ~/.zshrc
echo 'export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static' >> ~/.zshrc
```

#### 推荐镜像列表

| 优先级 | 镜像 | 地址 | 速度 |
|--------|------|------|------|
| 🥇 | 中科大 | `mirrors.ustc.edu.cn` | 最快 |
| 🥈 | 清华 | `mirrors.tuna.tsinghua.edu.cn` | 快 |
| 🥉 | 上海交大 | `mirrors.sjtug.sjtu.edu.cn` | 快 |
| - | 官方 | rust-lang.org | 正常 |

### 常见问题

#### 1. 版本显示异常

**问题:** 在 workspace 内显示 1.75.0-dev，实际是 1.86.0

**解决:**
```bash
cd ~ && rustc --version  # 在 workspace 外验证
```

#### 2. nightly 安装失败

**原因:** 网络问题 (TLS 握手失败)

**解决:**
```bash
# 使用中国镜像
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
rustup install nightly
rustup default nightly
```

#### 3. SBF 工具链问题

**解决:**
```bash
# 检查 sbf 工具链
rustup show sbf

# 如需重新安装
rustup toolchain install sbf
```

---

## 📖 核心概念对比

### Anchor vs Pinocchio

| 特性 | Anchor | Pinocchio |
|------|--------|-----------|
| **代码量** | 少 (自动生成样板) | 多 (手动控制) |
| **性能** | 良好 | 极致优化 |
| **安全** | 自动验证 | 手动验证 |
| **学习曲线** | 简单 | 陡峭 |
| **适用场景** | 快速开发 | 高性能场景 |

### 关键组件

| 组件 | Anchor | Pinocchio |
|------|--------|-----------|
| 入口点 | `entrypoint!` 宏 | `entrypoint!` 函数 |
| 账户类型 | `#[account]` | `AccountView` |
| CPI 调用 | `CpiContext` | `invoke_signed` |
| PDA 签名 | 自动生成 | 手动构造 seeds |
| 指令路由 | `#[instruction]` | discriminator |

---

## 🐛 常见问题

### Rust 版本兼容

**问题**: `blake3 1.8.3` 需要 nightly edition2024，但 Solana SBF 使用 Rust 1.84.0

**解决**:
```bash
cargo update -p blake3 --precise 1.5.5
```

### 编译错误

**问题**: `feature 'edition2024' is required`

**解决**:
```bash
# 使用 Rust nightly
rustup default nightly

# 或降级依赖
cargo update -p blake3 --precise 1.5.5
```

---

## 📂 参考资源

### GitHub 仓库

| 仓库 | 说明 |
|------|------|
| [qiaopengjun5162/solana-pinocchio-amm-workshop](https://github.com/qiaopengjun5162/solana-pinocchio-amm-workshop) | AMM 参考实现 |
| [deanmlittle/constant-product-curve](https://github.com/deanmlittle/constant-product-curve) | AMM 数学库 |

### 在线资源

| 资源 | 链接 |
|------|------|
| Blueshift Challenge | https://learn.blueshift.gg |
| Solana Playground | https://beta.solpg.io |

---

## 📝 笔记索引

### 本地笔记

| 文件 | 说明 |
|------|------|
| `/Users/bypasser/.openclaw/workspace/solana-tasks/` | 完整项目代码 |
| `/Users/bypasser/.openclaw/workspace/solana-dev-test/` | 学习笔记和总结 |

### 重要文件

| 文件 | 位置 | 说明 |
|------|------|------|
| TOOLS.md | ~/.openclaw/workspace/ | 服务器连接配置 |
| solana-tasks/ | ~/.openclaw/workspace/ | GitHub 仓库 |

---

## 📂 相关文件

| 文件 | 说明 |
|------|------|
| `memory/SOLANA_EXPERIENCE.md` | 完整开发经验总结 (42KB) |
| `memory/SOLANA_KEY_DISCOVERIES.md` | 关键发现和对比 |
| `memory/SOLANA_LESSONS_LEARNED.md` | 开发经验教训 |
| `macos_solana_impact_analysis.md` | 安装影响分析 |

---

## 🎯 后续任务

- [ ] 完成 Blueshift 毕业问卷
- [ ] 探索其他 DeFi 协议

---

### 📝 任务状态同步 (2026-02-07 更新)

| 任务 | 之前状态 | 现在状态 | 说明 |
|------|----------|----------|------|
| macOS 本地编译 Task 4-6 | 待测试 | ✅ 完成 | 全部编译成功 |
| Pinocchio API v2 兼容 | 待修复 | ✅ 已解决 | 启用 curve25519 feature |
| Task 3 Anchor 多模块 | 待解决 | ⚠️ 记录中 | 等待 Anchor 官方修复 |
| Blueshift 毕业问卷 | 待完成 | ⏳ 待完成 | 仍未进行 |
| Blueshift 毕业设计项目 | 未记录 | ⏳ 待开始 | 发现 subagent: solana-final-project |

---

## 🍎 macOS 本地编译 Task 4-6

### 编译结果 (2026-02-06)

| Task | 项目 | 大小 | 状态 |
|------|------|------|------|
| Task 4 | pinocchio_vault | 11KB | ✅ 成功 |
| Task 5 | pinocchio_escrow | 42KB | ✅ 成功 |
| Task 6 | pinocchio_amm | 40KB | ✅ 成功 |

### 问题背景

**现象:**
- Server: pinocchio 0.10.2 + Cargo.lock → 编译成功 ✅
- macOS: pinocchio 0.10.2 + crates.io 最新 → 编译失败 ❌

**错误信息:**
```
error[E0599]: no method named `find_program_address` found for struct `Address` in the current scope
```

**根因分析:**
- crates.io pinocchio 0.10.2 API 变更
- `find_program_address` 方法需要 `curve25519` feature
- Server 使用旧版本 (Cargo.lock 锁定)
- macOS 使用新版本 (cargo update 下载最新)

### 解决方案

#### Cargo.toml 更新

```toml
[dependencies]
pinocchio = "0.10.2"
pinocchio-system = "0.5.0"
solana-address = { version = "2.1", features = ["curve25519"] }
```

#### 代码更新

```rust
// 旧 API (已废弃)
// pinocchio::Address::find_program_address()

// 新 API
use solana_address::Address;

let (pda, bump) = Address::find_program_address(seeds, program_id);
```

### macOS 编译环境配置

```bash
# 设置 SBF SDK 路径
export SBF_SDK_PATH=/Users/bypasser/.cache/solana/v1.41/platform-tools/rust

# 编译命令
cd solana-tasks/task4-pinocchio-vault
cargo build-sbf

# 产物位置
target/sbpf-solana-solana/release/*.so
```

### 关键命令

```bash
# 检查 solana-address API
grep -rn "pub fn find_program_address" ~/.cargo/registry/src/index.crates.io-*/solana-address-2.1.0/src/

# 修复后的 import
use solana_address::Address;
```

### 经验教训

| 问题 | 教训 |
|------|------|
| crates.io 版本差异 | Cargo.lock 锁定版本的重要性 |
| API 变更检测 | 依赖版本更新可能导致编译失败 |
| Feature 配置 | solana-address 需要正确配置 features |

### 相关文档

| 文件 | 说明 |
|------|------|
| `memory/SOLANA.md` | ✅ 已更新 (macOS 编译经验) |
| `memory/2026-02-06.md` | ✅ 每日进度记录 |

---

## 🎯 macOS Solana 环境最终验证结果

### 验证方法

使用迭代循环方式验证环境：
1. 尝试不同 Rust 版本 (stable/nightly)
2. 降级依赖 (blake3 1.8.3 → 1.5.5)
3. 最小化测试
4. 完整项目测试

### 验证结果

| 项目 | 结果 | 说明 |
|------|------|------|
| **Pinocchio Tasks (4-6)** | ✅ 成功 | API 问题已解决 |
| **Anchor 最小测试** | ✅ 成功 | 228KB .so 生成 |
| **Anchor Task 3** | ❌ 失败 | 多模块代码问题 |

### macOS Solana 环境评估

| 组件 | 状态 | 说明 |
|------|------|------|
| Rust nightly 1.95.0 | ✅ 正常 | SBF 编译工具链 |
| platform-tools v1.41 | ✅ 正常 | SBF SDK |
| cargo build-sbf | ✅ 正常 | 编译命令 |
| Anchor 0.32.1 | ✅ 正常 | 宏展开正常 |
| Pinocchio 0.10.2 | ✅ 正常 | API 已适配 |

### Task 3 Anchor 问题分析

**问题现象：**
```
error[E0432]: unresolved import `crate`
error: cannot find derive macro `Accounts`
error: cannot find macro `require`
```

**根因：**
- Task 3 使用多模块组织 (`lib.rs` + `instructions/*.rs`)
- 这种组织方式在 macOS 上触发 Anchor 宏展开问题
- 单文件 Anchor 测试成功证明环境正常

**临时方案：**
```bash
# 使用服务器编译的 .so 文件
scp admin@server:/data/workspace/solana-tasks/task3-anchor-escrow/*.so ./
```

### macOS Solana 开发环境结论

| 结论 | 说明 |
|------|------|
| ✅ 环境基本正常 | Pinocchio + Anchor 最小测试成功 |
| ⚠️ 多模块限制 | Task 3 多模块代码不兼容 |
| 📝 已记录问题 | 等待 Anchor 官方修复 |

### 后续行动

1. **短期：** 使用服务器 .so 文件提交测试
2. **中期：** 关注 Anchor 版本更新
3. **长期：** 使用单文件组织 Anchor 代码

---

## 🖥️ macOS 与服务器环境配置对比

### 服务器 (Debian) 环境配置

| 组件 | 版本 | 安装方式 |
|------|------|----------|
| Rust | 1.86.0 + nightly | rustup |
| Solana CLI | 3.0.15 | 源码编译 |
| Anchor | 0.32.1 | cargo |
| platform-tools | v1.51 | Solana SDK |

### macOS 环境配置

| 组件 | 版本 | 安装方式 |
|------|------|----------|
| Rust | 1.95.0-nightly | rustup |
| **Solana CLI** | **3.0.14** | **agave-install** |
| Anchor | 0.32.1 | cargo |
| platform-tools | v1.51 | agave-install |

### macOS 环境变量 (~/.zshrc)

```bash
# Cargo & Rust
export PATH="$HOME/.cargo/bin:$PATH"

# LLVM
export LLVM_PATH="/usr/local/opt/llvm"
export PATH="/usr/local/opt/llvm/bin:$PATH"

# Solana CLI (agave-install)
export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"

# SBF SDK (可选，用于 cargo build-sbf)
export SBF_SDK_PATH="$HOME/.local/share/solana/install/active_release/bin"
```

### 服务器环境变量 (~/.bashrc)

```bash
# Solana CLI & Cargo
export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"

### 编译命令对比

| 操作 | macOS | 服务器 |
|------|-------|---------|
| **设置 SDK** | `export SBF_SDK_PATH=...` | 默认已配置 |
| **Pinocchio 编译** | `cargo build-sbf` | `cargo build-sbf` |
| **Anchor 编译** | `anchor build` | `anchor build` |
| **检查 Rust** | `rustc --version` | `rustc --version` |
| **检查 Solana** | `solana --version` | `solana --version` |

### 依赖版本同步

| 依赖 | 服务器 | macOS | 备注 |
|------|--------|-------|------|
| anchor-lang | 0.32.1 | 0.32.1 | ✅ 同步 |
| anchor-spl | 0.32.1 | 0.32.1 | ✅ 同步 |
| pinocchio | 0.10.2 | 0.10.2 | ✅ 同步 |
| solana-address | 2.1.0 | 2.1.0 | ✅ 同步 |
| blake3 | 1.5.5 | 1.5.5 | ✅ 需降级 |

### 常见问题处理

| 问题 | macOS 解决方案 | 服务器解决方案 |
|------|---------------|----------------|
| **blake3 edition2024** | `cargo update -p blake3 --precise 1.5.5` | 同 macOS |
| **Anchor 宏展开失败** | 同步服务器 Cargo.toml | - |
| **platform-tools 缺失** | `agave-install init` | 自动配置 |

---

## 📝 Solana 代码规范

### Anchor 项目结构

```
project/
├── Anchor.toml          # Anchor 配置
├── Cargo.toml           # Workspace 配置
├── programs/
│   └── project-name/
│       ├── Cargo.toml   # 程序依赖
│       └── src/
│           ├── lib.rs   # 程序入口 + 指令
│           ├── errors.rs # 错误定义
│           ├── state.rs # 状态结构
│           └── instructions/  # 可选：指令模块
│               ├── mod.rs
│               ├── make.rs
│               ├── take.rs
│               └── refund.rs
└── tests/               # 测试文件
```

### Cargo.toml 规范

#### Anchor 程序

```toml
[package]
name = "your_program"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib", "lib"]

[features]
default = []
cpi = ["no-entrypoint"]
no-entrypoint = []
no-idl = []
no-log-ix-name = []
idl-build = ["anchor-lang/idl-build", "anchor-spl/idl-build"]
anchor-debug = []
custom-heap = []
custom-panic = []

[dependencies]
anchor-lang = { version = "0.32.1", features = ["init-if-needed"] }
anchor-spl = "0.32.1"

[lints.rust]
unexpected_cgs = { level = "warn", check-cfg = ['cfg(target_os, values("solana"))'] }
```

#### Pinocchio 程序

```toml
[package]
name = "your_program"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["lib", "cdylib"]

[dependencies]
pinocchio = "0.10.2"
pinocchio-system = "0.5.0"
pinocchio-token = "0.5.0"
pinocchio-associated-token-account = "0.3.0"
solana-address = { version = "2.1", features = ["curve25519"] }
```

### 代码风格规范

#### 1. 程序入口

```rust
// ✅ 正确：使用 handler 函数模式
#[program]
pub mod your_program {
    use super::*;

    #[instruction(discriminator = 0)]
    pub fn initialize(ctx: Context<Initialize>, seed: u64) -> Result<()> {
        instructions::initialize::handler(ctx, seed)
    }
}

// ❌ 错误：直接实现逻辑
#[program]
pub mod your_program {
    pub fn initialize(ctx: Context<Initialize>, seed: u64) -> Result<()> {
        // 直接写逻辑...
    }
}
```

#### 2. 账户定义

```rust
// ✅ 正确：使用 derive macro
#[derive(Accounts)]
#[instruction(seed: u64)]
pub struct Initialize<'info> {
    #[account(mut)]
    pub signer: Signer<'info>,
    #[account(
        init,
        payer = signer,
        space = 8 + 32 + 8,
        seeds = [b"account", signer.key().as_ref(), seed.to_le_bytes().as_ref()],
        bump
    )]
    pub your_account: Account<'info, YourData>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct YourData {
    pub data: u64,
    pub authority: Pubkey,
}
```

#### 3. 错误定义

```rust
// ✅ 正确：使用 error_code macro
#[error_code]
pub enum YourError {
    #[msg("Invalid amount")]
    InvalidAmount = 0,
    #[msg("Unauthorized")]
    Unauthorized = 1,
    #[msg("Already initialized")]
    AlreadyInitialized = 2,
}
```

#### 4. CPI 调用

```rust
// ✅ 正确：使用 helper 函数
use anchor_spl::token::{transfer, Transfer};

fn handler(ctx: Context<TransferCtx>, amount: u64) -> Result<()> {
    transfer(
        CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.from.to_account_info(),
                to: ctx.accounts.to.to_account_info(),
            },
        ),
        amount,
    )?;
    Ok(())
}
```

### 命名规范

| 项目 | 规范 | 示例 |
|------|------|------|
| **程序名** | snake_case | `blueshift_anchor_escrow` |
| **指令名** | snake_case | `initialize`, `deposit`, `withdraw` |
| **账户名** | PascalCase | `UserAccount`, `EscrowState` |
| **错误名** | PascalCase | `InvalidAmount`, `Unauthorized` |
| **字段名** | snake_case | `total_amount`, `user_authority` |
| **Seed** | kebab-case | `b"vault"`, `b"escrow"` |

### PDA 规范

```rust
// ✅ 正确：使用常量定义 seed
const VAULT_SEED: &[u8] = b"vault";
const ESCROW_SEED: &[u8] = b"escrow";

// ✅ 正确：使用 bump
#[account(
    seeds = [ESCROW_SEED, maker.key().as_ref()],
    bump
)]
pub escrow: Account<'info, Escrow>,
```

### 测试规范

```rust
// ✅ 正确：完整的集成测试
#[tokio::test]
async fn test_initialize() {
    let program = ProgramTest::new("your_program", id(), None).start().await;
    let (mut banks_client, payer, blockhash) = program.clone().start().await;
    
    // 测试逻辑...
}
```

---

## 🔧 快速参考

### 开发流程

```bash
# 1. 创建新项目
anchor init project-name

# 2. 添加依赖
cargo add anchor-lang anchor-spl

# 3. 开发代码
# - 编辑 src/lib.rs
# - 定义 Accounts 结构
# - 实现指令逻辑

# 4. 构建
anchor build
# 或
cargo build-sbf

# 5. 测试
anchor test
```

### 调试技巧

| 场景 | 方法 |
|------|------|
| **打印调试** | `msg!("Value: {}", value)` |
| **Panic 信息** | `anchor-lang` 自动处理 |
| **账户验证** | `require!()` 宏 |
| **错误处理** | `?` 操作符传播错误 |

---

*此文件独立维护，便于 Solana 相关知识的查阅和更新。*
*最后更新: 2026-02-07 00:55*
