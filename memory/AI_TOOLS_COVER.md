# 封面制作专题

> **创建时间**: 2026-02-10
> **最后更新**: 2026-02-10
> **版本**: v1.0

---

## 目录

- [核心规则](#核心规则)
- [提示词模板](#提示词模板)
- [工具配置](#工具配置)
- [工作流程](#工作流程)
- [相关文件](#相关文件)

---

## 核心规则

### 封面制作规则（必须遵守）

#### 1. 禁止生成文字

AI模型无法正确渲染中文字符，必须在提示词中添加：

```
NO TEXT, NO WORDS, NO CHINESE, NO LETTERS, NO NUMBERS
```

#### 2. 尺寸规范

| 项目 | 规格 |
|------|------|
| **尺寸** | 900×383像素 |
| **比例** | 2.35:1 |
| **格式** | JPG |
| **文件大小** | ≤500KB |

#### 3. 工作流程

```
AI生成底图（不加文字） → Canva添加中文标题 → 完成
```

#### 4. 提示词结构

遵循归藏提示词结构：

```
[场景描述] + [材质细节] + [风格要求] + [技术参数] + [禁止项]
```

---

## 提示词模板

### 最佳模板：渐变拟物玻璃卡片风格

```
一个高端科技感的公众号封面设计，
渐变拟物玻璃卡片风格，
深色陶瓷白背景配极光渐变（紫色、蓝色、青色），
C4D渲染特写镜头，
磨砂玻璃材质卡片，
带有模糊效果的圆角矩形容器，
精致白色边缘、柔和投影，
巨大的内部留白，
现代极简主义UI设计风格，
干净深色背景，
光线追踪反射，
Dribbble风格，
8k分辨率，
NO TEXT, NO WORDS, NO CHINESE
```

### 其他风格模板

#### 矢量插画风格

```
扁平化矢量插画风格的公众号封面，
统一粗细的黑色单线描边（Monoline），
所有物体有封闭的黑色轮廓，
线条末端圆润，
几何化处理的简单形状，
复古柔和色调（珊瑚红、薄荷绿、芥末黄），
米色奶油色纸张纹理背景，
2.5D视角，
图层前后遮挡表现纵深，
装饰性几何元素，
Dribbble风格，
扁平化设计，
NO TEXT, NO WORDS, NO CHINESE
```

#### 科技极简风格

```
专业的科技风格公众号封面设计，
深蓝色渐变背景（#007AFF → #0055D4），
极简主义UI设计，
干净现代的排版，
抽象几何图形装饰，
柔和的光线追踪反射，
科技感线条和元素，
高端SaaS产品设计风格，
苹果 Keynote 极简主义，
巨大的留白空间，
Dribbble热门趋势，
NO TEXT, NO WORDS, NO CHINESE
```

---

## 工具配置

### Replicate API

#### 配置状态

| 项目 | 值 |
|------|-----|
| **Token** | `r8_cvLFh6uMQchrJTRpeIgNjUB0KV87zor2TYHRa` |
| **CLI位置** | `~/.openclaw/workspace/skills/replicate/` |
| **模型** | black-forest-labs/flux-schnell |

#### 使用命令

```bash
cd ~/.openclaw/workspace/skills/replicate

# 生成封面
export REPLICATE_API_TOKEN="r8_cvLFh6uMQchrJTRpeIgNjUB0KV87zor2TYHRa"

node replicate.js call black-forest-labs/flux-schnell \
  "[提示词]" \
  --aspect_ratio="16:9" \
  --num_outputs=4 \
  --output_quality=90 \
  --output_format="jpg"
```

#### 成本对比

| 方案 | 36张成本 | 速度 | 推荐度 |
|------|----------|------|--------|
| **Replicate FLUX** | **$0.11** | 2秒 | ⭐⭐⭐⭐⭐ |
| Bannerbear | $0.72 | 3-5分钟 | ⭐⭐⭐⭐ |
| DALL-E 3 | $1.44 | 10-15秒 | ⭐⭐⭐⭐ |
| Canva手动 | 免费 | 2-3小时 | ⭐⭐⭐ |

#### 结论

**Replicate是最优方案**
- 成本最低（$0.003/张）
- 速度最快（2秒/张）
- 质量优秀
- 无需额外配置

---

## 工作流程

### 批量生成流程

```
Step 1: 选择风格
├─ 渐变拟物玻璃卡片 → 科技感、现代UI
├─ 矢量插画 → 可爱、玩具模型风格
└─ 科技极简 → 简洁、专业

Step 2: 复制提示词模板
├─ 从本文档选择对应模板
├─ 替换内容占位符
└─ 添加禁止文字规则

Step 3: 生成测试
├─ 使用Replicate FLUX生成
├─ 检查4个变体
└─ 选择最佳

Step 4: 后期处理
├─ 裁剪为900x383
├─ 用Canva添加中文标题
└─ 导出发布
```

### 质量检查清单

生成封面后检查：

- [ ] **无文字**：图片中没有文字、字母、数字
- [ ] **尺寸正确**：900×383像素
- [ ] **风格统一**：符合公众号整体定位
- [ ] **色彩协调**：符合类型配色方案
- [ ] **美观度**：看起来专业、现代
- [ ] **可编辑性**：底图适合添加中文标题

---

## 相关文件

### 提示词库

| 文件 | 位置 | 说明 |
|------|------|------|
| 归藏提示词库 | `~/.openclaw/workspace/guizang-prompts/` | 18个高质量提示词 |
| 综合研究文档 | `ai-money-making/articles/guizang-prompt-research.md` | 归藏提示词详细分析 |
| 36个模板 | `ai-money-making/articles/scys-cover-prompts.md` | 36篇文章专用提示词 |

### 工具文档

| 文档 | 位置 | 说明 |
|------|------|------|
| Replicate Skill | `skills/replicate/SKILL.md` | CLI使用文档 |
| Canva Skill | `skills/canva-cover-maker/` | Canva操作指南 |

### 每日记录

| 文件 | 位置 | 说明 |
|------|------|------|
| 今日工作 | `memory/2026-02-10.md` | 2026-02-10工作记录 |

---

## 最佳实践

### 封面制作成功要点

1. **禁止文字** - 必须添加 `NO TEXT, NO WORDS, NO CHINESE`
2. **详细提示词** - 参考归藏提示词结构
3. **统一风格** - 所有封面保持一致
4. **后期处理** - Canva添加中文标题

### 常见问题

#### Q1: AI生成的图片出现乱码文字

**原因**: AI模型无法正确渲染中文字符

**解决方案**:
```
✅ 添加明确禁止词：
- NO TEXT
- NO WORDS
- NO CHINESE
- NO LETTERS
- NO NUMBERS
- completely text-free design
```

#### Q2: 生成的图片不够美观

**原因**: 提示词不够详细具体

**解决方案**:
```markdown
✅ 优化提示词结构：
1. 明确指定风格（technology, minimalist, modern）
2. 详细描述配色（使用颜色代码）
3. 添加技术参数（8k quality, high resolution）
4. 添加氛围词（soft lighting, ambient glow）
```

#### Q3: 图片比例不对

**原因**: AI默认生成方形图片

**解决方案**:
```markdown
✅ 使用比例参数：
- FLUX: --aspect_ratio="16:9" (接近2.35:1)
- 后期裁剪：1024x576 → 900x383
```

---

## 参考资源

### 外部链接

| 资源 | 链接 |
|------|------|
| 归藏GitHub | https://github.com/op7418/guizang-s-prompt |
| Replicate | https://replicate.com |
| FLUX Schnell | https://replicate.com/black-forest-labs/flux-schnell |
| Canva | https://www.canva.com |

### 内部文档

| 文档 | 位置 |
|------|------|
| MEMORY.md | `~/.openclaw/workspace/MEMORY.md` |
| INDEX.md | `~/.openclaw/workspace/memory/INDEX.md` |
| 今日记录 | `~/.openclaw/workspace/memory/2026-02-10.md` |

---

*最后更新: 2026-02-10*
*版本: v1.0*
