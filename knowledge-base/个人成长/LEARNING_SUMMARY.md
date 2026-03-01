# 学习成果沉淀

**日期:** 2026-02-02
**主题:** Claude Code Skills 学习方法论

---

## 一、学习方法论

### 核心原则：按类型选择学习方法

| 资源类型 | 判断标准 | 学习方法 |
|----------|----------|----------|
| **完整专业 Skill** | 已有 SKILL.md + 结构完整 | 直接安装使用 |
| **工具类 Skill** | 提供命令/工具使用 | 安装学习命令 |
| **Prompt 库** | 提示词集合，无 SKILL.md | 阅读理解，引用有价值内容 |
| **全新领域** | 没有现成资源 | auto-skill-builder 自动创建 |

### 方法选择流程

```
遇到新资源
    ↓
判断类型
    ↓
├─ 完整 Skill? → 直接安装使用 ✅
├─ 工具? → 安装学习命令 ✅
├─ Prompt 库? → 阅读引用 ⚡
└─ 新领域? → auto-skill-builder 🎯
```

---

## 二、已安装 Skills 清单

| Skill | 类型 | 来源 | 状态 |
|-------|------|------|------|
| `solana-dev` | 完整专业 Skill | Solana Foundation | ✅ 已安装 |
| `ppt-generator-pro` | 完整专业 Skill | op7418 | ✅ 已安装 |
| `skill-seekers` | 工具类 | yusufkaraaslan | ✅ 已安装 |
| `auto-skill-builder` | 工具类 | 自建 | ✅ 已安装 |
| `github-repo-mirror` | 工具类 | 实践创建 | ✅ 已安装 |

---

## 三、技能对比

### 1. skill-creator vs skill-seekers

| 维度 | skill-creator | skill-seekers |
|------|---------------|---------------|
| **定位** | 手动创建模板 | 自动生成工具 |
| **输入** | 手动编写内容 | 文档/仓库/PDF |
| **输出** | Skill 结构模板 | 完整可用 Skill |
| **自动化** | 低 | 高 |
| **AI 增强** | ❌ | ✅ |
| **冲突检测** | ❌ | ✅ |
| **预设模板** | ❌ | ✅ 18+ 个 |

**结论:** skill-seekers 已整合 skill-creator 的功能，无需单独使用 skill-creator。

### 2. Solana 官方版 vs 社区版

| 维度 | solana-foundation | Solana-ZH |
|------|-------------------|------------|
| **所有者** | 官方 | 社区 |
| **内容** | 完全相同 | 完全相同 |
| **programs-pinocchio.md** | 16.8KB | 14.0KB |
| **额外字段** | `user-invocable: true` | 无 |

**结论:** 官方版内容更完整，使用 `solana-foundation/solana-dev-skill`

### 3. Skill vs Prompt 库

| 类型 | 示例 | 处理方式 |
|------|------|----------|
| **完整 Skill** | solana-dev / ppt-generator-pro | 直接安装使用 |
| **Prompt 库** | guizang-s-prompt | 阅读理解，有需要时引用 |

**重要发现:** ppt-generator-pro 中的矢量插画风格已整合 guizang-s-prompt 的内容。

---

## 四、学习方法实践

### 实践案例：Solana Skill

| 步骤 | 做法 |
|------|------|
| 1. 获取 | git clone https://github.com/solana-foundation/solana-dev-skill.git |
| 2. 判断 | 完整专业 Skill ✅ |
| 3. 安装 | cp -r skill/ ~/.openclaw/workspace/skills/solana-dev |
| 4. 记录 | 更新 MEMORY.md |

### 实践案例：Prompt 库

| 步骤 | 做法 |
|------|------|
| 1. 获取 | git clone https://github.com/op7418/guizang-s-prompt.git |
| 2. 判断 | Prompt 库 ⚡ |
| 3. 阅读 | 理解结构，提取有价值内容 |
| 4. 关联 | 发现已整合到 ppt-generator-pro |
| 5. 记录 | 沉淀到本文档 |

---

## 五、Prompt 库有价值内容

### 可引用模式

#### PPT 风格提示词结构

```
结构模板:
├─ 适用模型
├─ 视觉风格
├─ 构图要求
├─ 线条风格
├─ 几何化处理
├─ 空间与透视
├─ 配色方案
└─ 字体排版
```

#### 3D 信息图模式

```
层级结构:
├─ 顶部: 3D 艺术字标题
├─ 中间: 3D 微缩模型
├─ 信息叠加层: 悬浮标签
└─ 底部: 数据矩阵区
```

---

## 六、待整合内容

### 可以添加到现有 Skills 的内容

| 来源 | 内容 | 目标 Skill | 优先级 |
|------|------|------------|--------|
| guizang-s-prompt | 新 PPT 风格灵感 | ppt-generator-pro | 低 |
| - | - | - | - |

---

## 七、经验总结

### 好的实践

1. **诚实回答** - 不懂就说不懂
2. **自主判断** - 根据类型选择学习方法
3. **成果沉淀** - 学习后记录到本地
4. **关联已有** - 发现资源间的联系

### 需要避免的

1. ❌ 不盲目重新创建已有资源
2. ❌ 不把所有东西都安装为 Skill
3. ❌ 学习后不记录

---

## 八、参考资料

- Skill Creator 最佳实践: `/Users/bypasser/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw/skills/skill-creator/SKILL.md`
- Auto Skill Builder: `/Users/bypasser/.openclaw/workspace/skills/auto-skill-builder/SKILL.md`
- MEMORY.md: `/Users/bypasser/.openclaw/workspace/MEMORY.md`

---

**最后更新:** 2026-02-03
**下次回顾:** 遇到新技能时

---

## 附录：Solana OpenBuild BootCamp 资源

**日期:** 2026-02-03
**来源:** https://www.notion.so/openbuildxyz/Solana-OpenBuild-BootCamp-2f1f8dcc31908022932cdf746ac9b692
**类型:** 官方课程资源库

### 内容概览

| 分类 | 说明 |
|------|------|
| 所有课程回放 | 视频教程 |
| Task 指南 | 实践任务说明 |
| 黑客松资源 | 比赛相关资源 |

### 用途

- Solana 开发入门到进阶
- 配合 `solana-dev` skill 和 `solana-pinocchio-amm-workshop` 实践项目
- 完成 BootCamp 任务和黑客松

---

**笔记创建:** 2026-02-03
**关联资源:**
- solana-dev (Skill)
- solana-pinocchio-amm-workshop (GitHub)

---

# 附录：Solana Pinocchio AMM Workshop 学习笔记

**日期:** 2026-02-03
**来源:** https://github.com/qiaopengjun5162/solana-pinocchio-amm-workshop
**类型:** 代码教程 + 实践项目

---

## 一、项目概述

这是一个展示 **Pinocchio 框架** 在 Solana 上构建高性能 AMM 的实战教程。

### 核心特性

| 特性 | 说明 |
|------|------|
| **零拷贝** | 直接操作账户内存快照，放弃 Borsh 序列化 |
| **CU 优化** | Initialize 和 Swap 指令的 CU 消耗远低于 Anchor |
| **双版本演进** | v0.9.x (AccountInfo) → v0.10.x+ (AccountView) |

---

## 二、项目结构

```bash
pinocchio_amm/
├── src/
│   ├── lib.rs              # 程序入口，指令分发
│   ├── state.rs            # 核心状态定义：Config + 数据布局
│   ├── instructions/
│   │   ├── mod.rs          # 模块化导出
│   │   ├── initialize.rs   # 初始化 AMM
│   │   ├── deposit.rs      # 注入流动性
│   │   ├── withdraw.rs     # 提取流动性
│   │   └── swap.rs         # 代币交换
│   └── curve.rs            # 数学公式（恒定乘积）
```

---

## 三、核心知识点

### 1. 零拷贝与内存管理

```rust
// 直接读取账户内存，跳过序列化
let auth = unsafe { core::ptr::addr_of!(self.authority).read_unaligned() };
```

**关键点：**
- `unsafe` = 手动验证的安全，非"危险"
- 使用 `read_unaligned` 处理非对齐内存
- 适合 BPF 环境下的性能优化

### 2. v0.9.x vs v0.10.x 对比

| 特性 | 旧版本 (v0.9.x) | 新版本 (v0.10.x+) |
|------|-----------------|------------------|
| **核心抽象** | `AccountInfo` | `AccountView` |
| **错误处理** | `minimum_balance` | `try_minimum_balance` |
| **数据访问** | `borrow_unchecked` | `Ref` 封装 |
| **性能** | 极高性能 | 巅峰性能 |

### 3. AMM 指令实现

#### Initialize
1. 创建 `Config` 账户 (PDA)
2. 创建 `Mint LP` 代币账户
3. 锁定铸币权给 `Config` 账户

#### Swap
1. 验证交易对账户
2. 计算金额（恒定乘积公式 x * y = k）
3. 执行转移 + 更新状态

---

## 四、与其他资源的关联

| 关联资源 | 关系 |
|----------|------|
| `solana-dev` skill | 补充 Pinocchio 框架的实践案例 |
| `programs-pinocchio.md` | 框架理论 ↔ 实战项目 |
| `solana-foundation/solana-dev-skill` | 官方理论 ↔ 社区实践 |

---

## 五、实践价值

### 可复用的模式

1. **Pinocchio 最佳实践** - AccountView + Zero-copy
2. **高性能指令设计** - 最小化 CU 消耗
3. **内存布局技巧** - unsafe Rust 在链上的应用
4. **AMM 核心逻辑** - Initialize/Deposit/Withdraw/Swap

### 建议的后续实践

| 难度 | 项目 | 说明 |
|------|------|------|
| ⭐ | 克隆并编译项目 | `cargo build-sbf` |
| ⭐⭐ | 添加新指令 | 例如 `collect_fees` |
| ⭐⭐⭐ | 迁移到最新框架 | 从 v0.9.x → v0.10.x |
| ⭐⭐⭐⭐ | 从零实现类似项目 | 用学到的模式构建新 AMM |

---

## 六、参考资料

- Pinocchio 框架: https://github.com/litesvm/pinocchio
- 旧版参考: `blueshift_native_amm/` 目录
- 恒定乘积曲线: 参考 `curve.rs`

---

**笔记创建:** 2026-02-03
**关联 Skill:** solana-dev

---

## 附录：Solana OpenBuild BootCamp 完整清单

**日期:** 2026-02-03 (更新)
**来源:** Notion 页面 (通过 OpenClaw 托管浏览器访问)
**文件:** `~/workspace/solana-bootcamp-curriculum.md`

### 课程列表 (8节)

| 日期 | 主题 |
|------|------|
| 2026-1-6 | 区块链 + Solana 基础全攻略 |
| 2026-1-8 | Trading Bot + 代币与NFT |
| 2026-1-13 | 资本市场与链上存储 |
| 2026-1-15 | Solana 程序开发入门 |
| 2026-1-20 | AI Vibe Coding Anchor |
| 2026-1-22 | Anchor Basics - SPL & Token 2022 |
| 2026-1-27 | 黑客松参赛指导 + Pinocchio |
| 2026-1-29 | 链上套利与测试工具 |

### Task 清单 (6个)

| Task | 框架 | GitHub 仓库 |
|------|------|-------------|
| 铸造 SPL Token | Anchor | Tools-touch/Task- |
| Anchor 金库 | Anchor | daog1/blueshift_anchor_vault |
| Anchor 托管 | Anchor | Tools-touch/Task- |
| Pinocchio 金库 | Pinocchio | qiaopengjun5162/pinocchio_vault |
| Pinocchio 托管 | Pinocchio | Likeben-boy/blueshift_escrow_study |
| Pinocchio AMA | Pinocchio | qiaopengjun5162/solana-pinocchio-amm-workshop |

### Blueshift 学习路径

| 路径 | 课程数 | 时长 | 特点 |
|------|--------|------|------|
| Solana Developer Foundations | 3 | 8 hrs | 区块链基础 |
| TypeScript Client Developer | 5 | 15 hrs | 客户端开发 |
| **Anchor Mastery** | 4 + 3 挑战 | 20 hrs | ⭐ **重点** |
| Payments & Commerce | 3 | 6 hrs | 支付方案 |
| Security Specialist | 4 | 12 hrs | 安全最佳实践 |
| Testing & Tooling | 4 | 10 hrs | 测试框架 |
| Token Developer | 6 | 18 hrs | 代币开发 |
| **Native Rust Developer** | 4 + 3 挑战 | 30 hrs | ⭐ **Pinocchio** |
| Advanced Low-Level | 3 + 3 挑战 | 25 hrs | 底层优化 |

---

## 今日深度学习 (2026-02-03)

### ✅ 框架深入学习

| 时间 | 内容 | 状态 |
|------|------|------|
| 上午 | solana-dev skill 复习 | ✅ 完成 |
| 上午 | Anchor 框架详解 | ✅ programs-anchor.md 完全阅读 |
| 上午 | Pinocchio 框架详解 | ✅ programs-pinocchio.md 完全阅读 |

### 📖 核心概念总结

#### Anchor 框架

| 特性 | 说明 |
|------|------|
| Reduced Boilerplate | 自动账户管理、序列化、错误处理 |
| Built-in Security | 自动账户所有权验证 |
| IDL Generation | 自动生成客户端代码 |
| 关键宏 | `declare_id!`, `#[program]`, `#[derive(Accounts)]` |
| 账户类型 | `Signer`, `SystemAccount`, `Program`, `Account` |

#### Pinocchio 框架

| 特性 | 说明 |
|------|------|
| Zero-Copy | 零拷贝技术 |
| Minimal Dependencies | 仅 Solana SDK 类型 |
| CU Optimization | 相比 Anchor 节省 84% CU |
| Manual Validation | 手动账户验证 |
| 性能 | 高性能、低二进制大小 |

#### Vault vs Escrow

| 概念 | 用途 |
|------|------|
| Vault | 金库 - 存储和管理资金 |
| Escrow | 托管 - 条件释放资金 |

---

## 今日 GitHub 仓库克隆

```bash
~/.openclaw/workspace/
├── Task-/                      # Task 模板
├── blueshift_anchor_vault/    # Anchor Vault 参考
├── pinocchio_vault/           # Pinocchio Vault 参考
└── blueshift_escrow_study/    # Escrow 学习
```

---

## 明天计划：Task 实践

### Task 执行顺序

```
1. 铸造 SPL Token  (基础概念)
   └── 参考: Tools-touch/Task-
2. Anchor Vault    (账户模型)
   └── 参考: daog1/blueshift_anchor_vault
3. Anchor Escrow  (程序交互)
   └── 参考: blueshift_escrow_study
4. Pinocchio Vault (高性能)
   └── 参考: qiaopengjun5162/pinocchio_vault
5. Pinocchio Escrow
6. Pinocchio AMA
```

---

*最后更新: 2026-02-03 13:40*
*明天: 开始实践 Task*

**笔记创建:** 2026-02-03
**关联文档:**
- solana-bootcamp-curriculum.md (完整清单)
- solana-dev (Skill)
- solana-pinocchio-amm-workshop (GitHub)
