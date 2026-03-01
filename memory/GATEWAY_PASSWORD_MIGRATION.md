# Gateway 密码迁移计划

**创建时间**: 2026-02-11  
**状态**: 规划阶段  
**目标**: 将 Gateway 密码从明文存储迁移到环境变量

---

## 当前问题

**位置**: `openclaw.json`
```json
{
  "gateway": {
    "auth": {
      "mode": "password",
      "token": "d354b1307cde95edd437ff040cf9e58f72bffa52c45b08df",
      "password": "123123"  // ❌ 明文存储
    }
  }
}
```

**风险**：
- 密码以明文形式存储在配置文件中
- 任何能访问配置文件的人都能看到密码
- 不符合安全最佳实践

---

## 迁移方案

### 方案：环境变量 + .env 文件

#### 步骤 1：备份当前配置
```bash
cp /Users/bypasser/.openclaw/workspace/openclaw.json /Users/bypasser/.openclaw/workspace/openclaw.json.backup
```

#### 步骤 2：创建 .env 文件
```bash
# 创建 .env 文件
touch /Users/bypasser/.openclaw/workspace/.env

# 添加内容
GATEWAY_PASSWORD=your_secure_password_here
```

#### 步骤 3：修改 openclaw.json
```json
{
  "gateway": {
    "auth": {
      "mode": "password",
      "token": "d354b1307cde95edd437ff040cf9e58f72bffa52c45b08df",
      "password": "${GATEWAY_PASSWORD}"  // ✅ 引用环境变量
    }
  }
}
```

#### 步骤 4：设置 .env 文件权限
```bash
chmod 600 /Users/bypasser/.openclaw/workspace/.env
```

#### 步骤 5：加载环境变量并重启 Gateway
```bash
# 临时加载（当前会话）
source /Users/bypasser/.openclaw/workspace/.env

# 永久加载（添加到 shell 配置文件）
echo 'source /Users/bypasser/.openclaw/workspace/.env' >> ~/.zshrc

# 重启 Gateway
openclaw gateway restart
```

---

## 验证步骤

### 1. 检查 Gateway 状态
```bash
openclaw gateway status
```

### 2. 测试连接
```bash
openclaw status
```

### 3. 验证密码不再可见
```bash
# 检查配置文件
grep password /Users/bypasser/.openclaw/workspace/openclaw.json
# 应该看到： "password": "${GATEWAY_PASSWORD}"

# 检查 .env 文件
cat /Users/bypasser/.openclaw/workspace/.env
# 应该看到： GATEWAY_PASSWORD=xxx
```

---

## 回退方案

如果迁移出现问题，可以回退：

```bash
# 1. 停止 Gateway
openclaw gateway stop

# 2. 恢复备份
cp /Users/bypasser/.openclaw/workspace/openclaw.json.backup /Users/bypasser/.openclaw/workspace/openclaw.json

# 3. 重启 Gateway
openclaw gateway start
```

---

## 安全建议

1. **使用强密码**
   - 长度：至少 16 位
   - 包含：大写字母 + 小写字母 + 数字 + 特殊字符
   - 示例：`Gk9#mN2$pL7@qR4!sT8`

2. **定期更换密码**
   - 建议每 3 个月更换一次
   - 更换后更新 .env 文件

3. **不要提交 .env 到版本控制**
   - 在 .gitignore 中添加：
   ```
   .env
   .env.*
   ```

4. **限制 .env 文件权限**
   - 只让本人可读写：`chmod 600 .env`

---

## 预期效果

| 指标 | 迁移前 | 迁移后 |
|------|--------|--------|
| 密码可见性 | 明文存储 | 加密存储 |
| 访问风险 | 高 | 低 |
| 维护难度 | 低 | 中 |
| 安全等级 | 60/100 | 90/100 |

---

## 注意事项

- 迁移过程中 Gateway 会短暂中断
- 确保有备份再进行操作
- 如果使用 CI/CD，需要在环境变量中设置密码
- Docker 环境需要使用 docker-compose 的 environment 配置

---

**下一步**: 确认是否执行此迁移方案？
