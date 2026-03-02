# 安装避坑指南

## Python 包安装

### 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `Python 3.9.6 not in '>=3.10'` | pip3 使用 Python 3.9 | 用 `python3 -m pip` |
| `externally-managed-environment` | macOS 系统保护 | 加 `--break-system-packages` |
| `not on PATH` | 安装到非标准路径 | 使用完整路径或添加 PATH |

### 正确安装姿势

```bash
# 1. 确认 Python 版本
python3 --version

# 2. 使用正确的 pip
python3 -m pip install <包名> --user --break-system-packages

# 3. 检查安装位置
which <包名>
# 或
python3 -c "import <包名>; print(<包名>.__file__)"
```

### PATH 问题

```bash
# 方案1: 添加到 PATH
export PATH="$HOME/Library/Python/3.13/bin:$PATH"

# 方案2: 使用完整路径
~/Library/Python/3.13/bin/<命令>
```

## 检查清单

安装前检查：
- [ ] Python 版本: `python3 --version`
- [ ] pip 对应版本: `python3 -m pip --version`
- [ ] 是否有虚拟环境
