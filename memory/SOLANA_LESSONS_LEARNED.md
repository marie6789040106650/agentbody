# Solana 开发经验教训

> **创建时间:** 2026-02-06
> **来源:** solana-tasks 仓库分析
> **主题:** 从实践中总结的经验教训

---

## 🚀 开发效率

### ✅ 应该做的

1. **使用 Solana Playground 进行快速原型开发**
   ```bash
   # 优点:
   # - 无需本地环境配置
   # - 即时部署到 devnet
   # - 内置测试框架
   # - 团队协作功能
   
   # 使用方法:
   # 1. 访问 https://playground.solana.com
   # 2. 创建新项目
   # 3. 粘贴代码
   # 4. Build → Deploy
   ```

2. **利用 Anchor 的自动 IDL 生成**
   ```rust
   // Anchor 自动生成:
   // - TypeScript 类型定义
   // - 账户结构序列化
   // - 指令编码器
   
   // 在 tests/ 中直接使用:
   import { Program } from '@coral-xyz/anchor';
   import { getProgram } from './getProgram';
   
   const program = getProgram();
   await program.methods.make(seed, receive, amount).accounts(...).rpc();
   ```

3. **使用 `anchor test` 进行快速测试**
   ```bash
   anchor test --skip-build  # 跳过构建，只运行测试
   anchor test --skip-local-validator  # 使用远程 validator
   anchor test -e mainnet-beta  # 在 mainnet 测试
   ```

4. **建立模板项目**
   ```
   ~/.anchor/
   ├── templates/
   │   ├── basic/          # 基础模板
   │   ├── token/          # Token 模板
   │   └── escrow/         # Escrow 模板
   ```

5. **记录每个 Task 的完成步骤**
   ```markdown
   ## Task X: 完成日期
   1. 步骤 1
   2. 步骤 2
   3. 步骤 3
   
   ### 遇到的问题
   - 问题 1: 解决方案
   
   ### 验证结果
   - 状态: ✅ 通过
   ```

### ❌ 不应该做的

1. **不要跳过代码审查**
   ```rust
   // 错误: 直接复制粘贴代码
   let seeds = [b"vault", user.key().as_ref()];
   
   // 正确: 理解每行代码
   // 1. "vault" 是 PDA 种子前缀
   // 2. user.key() 确保每个用户有独立的 vault
   ```

2. **不要硬编码 Program ID**
   ```rust
   // 错误
   const ID = new PublicKey("11111111111111111111111111111111");
   
   // 正确: 从配置文件读取
   declare_id!("11111111111111111111111111111111");
   ```

3. **不要忽略日志**
   ```rust
   // 错误: 没有调试信息
   pub fn process(ctx: Context<MyInstruction>) -> Result<()> {
       // ...
   }
   
   // 正确: 添加日志
   pub fn process(ctx: Context<MyInstruction>) -> Result<()> {
       msg!("Processing instruction for user: {}", ctx.accounts.user.key());
       // ...
   }
   ```

---

## 🔧 技术实践

### ✅ 应该做的

1. **使用 `require!` 系列宏进行参数验证**
   ```rust
   require!(amount > 0, MyError::InvalidAmount);
   require_keys_eq!(ctx.accounts.mint_a.key(), expected_mint, MyError::WrongMint);
   require!(ctx.accounts.vault.amount > 0, MyError::EmptyVault);
   ```

2. **使用 `try_from` 而不是直接转换**
   ```rust
   // 正确: 安全转换
   let amount = u64::try_from(data).map_err(|_| MyError::InvalidData)?;
   
   // 避免: 可能 panic
   let amount = u64::from_le_bytes(data.try_into().unwrap());
   ```

3. **使用 `checked_*` 算术运算**
   ```rust
   // 正确: 防止溢出
   let total = amount.checked_add(fee).ok_or(MyError::Overflow)?;
   let result = a.checked_mul(b).ok_or(MyError::Overflow)?;
   ```

4. **显式标记可变性**
   ```rust
   // 正确
   let mut escrow = &mut ctx.accounts.escrow;
   escrow.amount = new_amount;
   
   // 避免: 过度使用 mut
   let escrow = &ctx.accounts.escrow;  // 只读
   ```

5. **使用 `?` 而不是 `unwrap()`**
   ```rust
   // 正确: 传播错误
   let result = maybe_value.ok_or(MyError::NotFound)?;
   
   // 避免: 可能 panic
   let result = maybe_value.unwrap();
   ```

### ❌ 不应该做的

1. **不要在验证前使用账户数据**
   ```rust
   // 错误: 顺序错误
   let balance = account.amount;  // 未验证!
   require!(account.is_signer()); // 验证在后
   
   // 正确: 先验证
   require!(account.is_signer());
   let balance = account.amount;
   ```

2. **不要忽略账户所有权**
   ```rust
   // 错误: 未验证 owner
   let data = account.data.borrow();
   
   // 正确: 验证 owner
   require!(account.owner() == &program_id, MyError::WrongOwner);
   let data = account.data.borrow();
   ```

3. **不要使用浮点数**
   ```rust
   // 错误: 精度问题
   let price = 1.5;  // ❌ 不支持
   
   // 正确: 使用整数
   let price = 1500000;  // 1.5 * 10^6
   ```

4. **不要忘记租金**
   ```rust
   // 错误: 未计算 rent
   let lamports = 1000000;
   
   // 正确: 使用 Rent sysvar
   let rent = Rent::get()?;
   let lamports = rent.minimum_balance(space);
   ```

---

## 🛡️ 安全性

### ✅ 应该做的

1. **验证所有签名者**
   ```rust
   // 正确: 显式验证
   require!(ctx.accounts.user.is_signer(), MyError::NotSigned);
   ```

2. **验证账户所有者**
   ```rust
   // 正确: 验证 owner
   require!(account.owner() == &token::ID, MyError::WrongOwner);
   require!(account.owner() == &system_program::ID, MyError::WrongOwner);
   ```

3. **使用约束条件**
   ```rust
   #[account(
       has_one = mint_a,
       has_one = mint_b,
       has_one = maker,
       seeds = [b"escrow", maker.key().as_ref(), seed.to_le_bytes().as_ref()],
       bump = escrow.bump,
   )]
   pub escrow: Account<'info, Escrow>,
   ```

4. **检查权限边界**
   ```rust
   // 正确: 只允许特定角色操作
   require!(ctx.accounts.authority.key() == self.authority, MyError::Unauthorized);
   ```

5. **防止重入攻击**
   ```rust
   // 使用状态机模式
   let previous_state = escrow.state;
   escrow.state = State::Processing;
   
   // ... 执行操作 ...
   
   require!(previous_state == State::Idle, MyError::InvalidState);
   ```

### ❌ 不应该做的

1. **不要信任客户端数据**
   ```rust
   // 错误: 直接使用客户端数据
   let amount = ctx.accounts.amount;
   
   // 正确: 从指令数据获取
   #[instruction(amount: u64)]
   pub fn process(ctx: Context<...>, amount: u64) -> Result<()> {
       // amount 来自指令数据，可信
   }
   ```

2. **不要跳过账户验证**
   ```rust
   // 错误: 跳过验证
   ctx.accounts.vault.amount;
   
   // 正确: 完整验证
   require!(ctx.accounts.vault.amount > 0, MyError::ZeroAmount);
   ```

3. **不要使用过大的权限**
   ```rust
   // 错误: 过度授权
   #[account(
       init,
       payer = user,
       space = 10000,  // ❌ 过大
   )]
   
   // 正确: 精确计算
   #[derive(InitSpace)]
   #[account]
   pub struct MyStruct {
       pub field1: u64,
       pub field2: Pubkey,
   }
   // space = 8 + 32 + 8 (Discriminator) = 48
   ```

4. **不要硬编码常量**
   ```rust
   // 错误
   let fee = 0.03;
   
   // 正确: 可配置
   #[account]
   pub struct Config {
       pub fee: u16,  // 存为 basis points
   }
   ```

---

## 📐 架构设计

### ✅ 应该做的

1. **模块化代码结构**
   ```
   src/
   ├── lib.rs              # 主入口
   ├── error.rs            # 错误定义
   ├── state.rs            # 状态结构
   └── instructions/       # 指令模块
       ├── mod.rs
       ├── initialize.rs
       ├── deposit.rs
       └── withdraw.rs
   ```

2. **使用清晰的命名约定**
   ```rust
   // 账户命名
   pub vault: Account<'info, TokenAccount>,
   pub user_ata: Account<'info, TokenAccount>,
   
   // 指令命名
   pub fn initialize_config(...),
   pub fn deposit(...),
   pub fn withdraw(...),
   ```

3. **保持函数短小**
   ```rust
   // 正确: 单一职责
   pub fn make(ctx: Context<Make>, ...) -> Result<()> {
       ctx.accounts.escrow.set_inner(...);
       token::transfer(...)
   }
   
   // 避免: 过长函数
   pub fn make(...) -> Result<()> {
       // 50+ 行代码
   }
   ```

4. **使用常量**
   ```rust
   pub const SEED_PREFIX: &[u8] = b"escrow";
   pub const MAX_FEE_BASIS_POINTS: u16 = 1000;
   ```

5. **添加文档注释**
   ```rust
   /// Creates a new escrow for token exchange.
   ///
   /// # Arguments
   ///
   /// * `seed` - Unique identifier for the escrow
   /// * `receive` - Amount of token B requested
   /// * `amount` - Amount of token A offered
   ///
   /// # Errors
   ///
   /// Returns `InvalidAmount` if amount is zero.
   #[instruction(seed, receive, amount)]
   pub fn make(...) -> Result<()> {
       // ...
   }
   ```

### ❌ 不应该做的

1. **不要重复代码**
   ```rust
   // 错误: 重复的验证逻辑
   if !account.is_signer() { return Err(...) }
   if !account.is_signer() { return Err(...) }
   
   // 正确: 提取到函数
   fn assert_signer(account: &AccountInfo) -> Result<()> {
       require!(account.is_signer(), ErrorCode::NotSigner);
       Ok(())
   }
   ```

2. **不要混合关注点**
   ```rust
   // 错误: 一个函数做太多
   pub fn complex_instruction(...) -> Result<()> {
       // 验证
       // 计算
       // 转账
       // 更新状态
       // 发日志
   }
   
   // 正确: 分解
   pub fn make(...) -> Result<()> {
       validate()?;
       calculate()?;
       transfer()?;
       update()?;
   }
   ```

3. **不要忽略错误类型**
   ```rust
   // 错误: 所有错误都用同一个
   Err(MyError::Failed)?;
   
   // 正确: 精确的错误类型
   Err(MyError::InsufficientFunds)?;
   Err(MyError::InvalidAccount)?;
   Err(MyError::Unauthorized)?;
   ```

---

## 🧪 测试

### ✅ 应该做的

1. **编写完整的测试用例**
   ```typescript
   describe('Escrow', () => {
     it('should create escrow', async () => {
       const tx = await program.methods
         .make(seed, receiveAmount, offerAmount)
         .accounts({...})
         .rpc();
       
       assert.ok(tx);
     });
     
     it('should fail with zero amount', async () => {
       await expect(program.methods
         .make(seed, 0, 0)
         .accounts({...})
         .rpc()).rejects.toThrow();
     });
   });
   ```

2. **测试边界条件**
   ```typescript
   it('should handle max amount', async () => {
     const max = new BN(2).pow(new BN(64)).subn(1);
     const tx = await program.methods
       .make(seed, max, max)
       .accounts({...})
       .rpc();
     assert.ok(tx);
   });
   ```

3. **使用真实的测试网**
   ```bash
   anchor test -e devnet  # devnet
   anchor test -e testnet  # testnet
   ```

### ❌ 不应该做的

1. **不要只测试 happy path**
   ```typescript
   // 错误: 只测试成功
   it('works', () => { expect(success).true });
   
   // 正确: 测试各种情况
   it('handles edge cases', () => {
     expect(success).true;
     expect(invalidAmount).throw();
     expect(unauthorized).throw();
     expect(overflow).throw();
   });
   ```

2. **不要忽略测试覆盖**
   ```bash
   # 运行覆盖报告
   anchor test --coverage
   ```

---

## 🔄 版本控制

### ✅ 应该做的

1. **使用语义化 commit**
   ```
   feat: add take instruction to escrow
   fix: resolve PDA validation issue
   docs: update README
   refactor: extract common validation logic
   test: add edge case tests
   ```

2. **使用分支开发**
   ```bash
   git checkout -b feature/escrow-take
   git checkout -b fix/pda-validation
   ```

3. **保存中间状态**
   ```bash
   git stash save "WIP: escrow with partial take"
   ```

---

## 📈 性能优化

### ✅ 应该做的

1. **使用 `#[inline(always)]`**
   ```rust
   #[inline(always)]
   pub fn get_amount(&self) -> u64 {
       self.amount
   }
   ```

2. **批量操作**
   ```rust
   // 正确: 减少 CPI 调用
   for i in 0..10 {
       token::transfer(...)?;  // ❌ 10 次 CPI
   }
   
   // 更好: 批量处理
   transfer_batch(accounts, amounts)?;
   ```

3. **使用合适的账户大小**
   ```rust
   // 正确: 精确计算
   #[derive(InitSpace)]
   #[account]
   pub struct Config {
       pub authority: Pubkey,    // 32
       pub fee: u16,            // 2
       pub bump: u8,             // 1
   }
   // 总空间: 8 + 32 + 2 + 1 = ~50
   ```

### ❌ 不应该做的

1. **不要太早优化**
   ```
   规则:
   1. 先让代码工作 (80% 性能)
   2. 识别瓶颈 (profiler)
   3. 只优化热点路径 (10x 收益)
   ```

2. **不要忽略 gas 成本**
   ```rust
   // 注意: Solana 有计算预算限制
   // 200,000 计算单元 / 交易
   ```

---

## 🎯 实践经验

### 1. 学习建议

**从简单到复杂:**
1. Mint Token (TypeScript) - 1 天
2. Anchor Vault - 2-3 天
3. Anchor Escrow - 1 周
4. Pinocchio Vault - 1 周
5. Pinocchio AMM - 2-3 周

**遇到问题时:**
1. 查看官方文档
2. 搜索 GitHub Issues
3. 阅读示例代码
4. 询问社区

### 2. 常见问题解决

| 问题 | 解决方案 |
|------|----------|
| 构建失败 | `cargo clean && anchor build` |
| 测试超时 | 增加 timeout |
| 部署失败 | 检查余额 |
| CPI 失败 | 验证 signer seeds |
| 账户验证失败 | 检查约束条件 |

### 3. 资源推荐

**文档:**
- Solana Docs: https://docs.solana.com/
- Anchor Docs: https://www.anchor-lang.com/
- Rust Book: https://doc.rust-lang.org/book/

**示例:**
- Solana Program Examples
- OpenZeppelin Contracts
- Blueshift Challenges

**社区:**
- Solana Discord
- Anchor Discord
- Stack Overflow

---

*文档由 OpenClaw 自动生成*
*最后更新: 2026-02-06*
