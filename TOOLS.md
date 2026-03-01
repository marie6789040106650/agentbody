# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### 本地开发环境 (macOS)

**环境配置（2026-02-12 同步）**:
| 组件 | 版本/路径 | 说明 |
|------|----------|------|
| Python | 3.13.11 | /usr/local/bin/python3 |
| Node.js | v22.22.0 | NVM 管理 |
| **PATH 配置** | Solana 已在 Zsh PATH 中 |
| **SBF_SDK_PATH** | `$HOME/.local/share/solana/install/active_release/bin` |

**注意事项**:
- ✅ Python 3.13.11 已验证（Zsh 强制 alias）
- ✅ Node 22 已验证（NVM 懒加载）
- ✅ Solana CLI 4.0.0 (Agave) 已验证（PATH 已配置）
- 🚫 Claude/Gemini CLI 已卸载，禁止调用

**执行规则**:
```bash
# PATH 已由 ~/.zshrc 配置，无需手动添加
# Solana 命令已可直接使用：solana --version
```

**Python 虚拟环境**:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Solana 开发服务器 (远程 Docker)

**保留远程开发能力**（可选使用）:
- **solana-dev** → ec2-47-129-231-137.ap-southeast-1.compute.amazonaws.com
  - SSH: `ssh solana-dev`
  - Docker 容器: Solana Agave 3.0.13 + Anchor 0.32.1

---

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without sharing your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
