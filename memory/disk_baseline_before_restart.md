# 磁盘空间分析报告 (树形结构)
> 分析时间: 2026-02-22 05:03 EST - 重启前基准

---

## 📊 磁盘整体

```
/ (根目录)
├── [466G] 总容量
│   ├── [11G] 已用
│   └── [22G] 可用 (35%)
```

---

## 🌳 用户目录树形结构 (~)

```
~/ (用户主目录)
├── 📁 Pictures/          [~57G]  照片库
├── 📁 Downloads/         [~20G]  下载
├── 📁 Documents/         [~6G]   文档
├── 📁 Desktop/           [173M]  桌面
├── 📁 Movies/            [12G]   视频
├── 📁 Music/             [较小]  音乐
├── 📁 Library/           [较大]  系统库
│
├── 📁 .rustup/           [18G]   ⚠️ Rust工具链
├── 📁 .colima/           [5.8G]  ⚠️ Docker虚拟机
├── 📁 .cache/            [4.7G]  缓存
├── 📁 .openclaw/         [2G]    OpenClaw
├── 📁 .cargo/            [1.7G]  Rust包
├── 📁 .nvm/              [1.5G]  Node版本
├── 📁 .local/            [1.1G]  本地数据
├── 📁 .npm-global/       [996M]  npm全局包
├── 📁 .antigravity/      [782M]  
├── 📁 .vscode/           [494M]  VS Code
├── 📁 .stacher/          [335M]  
├── 📁 .pnpm-cache/       [102M]  pnpm缓存
│
├── 📁 d/                 [42G]   项目资料
│   ├── 📁 出海/          [25G]   
│   ├── 📁 Movies/        [12G]   
│   ├── 📁 天涯神帖210+/  [4.5G]  
│   └── 📁 ...
│
├── 📁 Code/              [较小]  代码
├── 📁 openclaw/          [较小]  OpenClaw工作区
├── 📁 node_modules/      [较小]  npm包
├── 📁 solana-src/        [较小]  Solana源码
│
└── 📄 .DS_Store, .zsh_history, 等 [小文件]
```

---

## 🌳 ~/Library 树形结构

```
~/Library/
├── 📁 Application Support/    [较大]
│   ├── 📁 Google/            [25G]  ⚠️ Chrome
│   │   └── Chrome/
│   │       ├── 📁 Profile 11/        [9.7G]  ⚠️
│   │       ├── 📁 Profile 14/        [5.2G]  ⚠️
│   │       ├── 📁 OptGuideOnDeviceModel/  [4.0G]  AI模型
│   │       ├── 📁 Profile 4/          [3.1G]
│   │       ├── 📁 Profile 2/          [1.7G]
│   │       └── 📁 Default/             [173M]
│   │
│   ├── 📁 Comet/             [2.5G]  代理
│   ├── 📁 Caches/            [1.3G]
│   ├── 📁 Binance/           [1.0G]  币安
│   ├── 📁 Quark/             [947M]  夸克
│   ├── 📁 v2rayN/            [364M]
│   ├── 📁 quark-cloud-drive/ [341M]
│   ├── 📁 Discord/           [322M]
│   ├── 📁 Adobe/             [313M]
│   ├── 📁 com.tencent.imamac/[311M]  微信
│   ├── 📁 aDrive/            [254M]  阿里云盘
│   ├── 📁 zoom.us/           [222M]
│   ├── 📁 cloud-code/        [119M]
│   ├── 📁 Antigravity/       [108M]
│   └── 📁 ...
│
├── 📁 Caches/               [较大]
│   ├── 📁 Google/            [189M]  Chrome缓存
│   ├── 📁 Comet/             [143M]
│   ├── 📁 ms-playwright-go/  [120M]
│   ├── 📁 Homebrew/          [51M]
│   ├── 📁 GeoServices/       [49M]
│   └── 📁 pnpm/              [26M]
│
└── 📁 ...
```

---

## 📊 按大小排序 (树形展示)

```
🏆 最大占用 Top 20
│
├── [57G]  Pictures/              照片库
├── [25G]  Google Chrome          浏览器
│   ├── [9.7G]  Profile 11
│   ├── [5.2G]  Profile 14
│   ├── [4.0G]  OptGuideOnDeviceModel
│   ├── [3.1G]  Profile 4
│   └── [1.7G]  Profile 2
│
├── [20G]  Downloads/             下载
├── [18G]  .rustup/              ⚠️ Rust工具链
├── [12G]  Movies/               视频
├── [6G]   Documents/            文档
├── [5.8G] .colima/              ⚠️ Docker虚拟机
├── [4.7G] .cache/               缓存
├── [4.5G] d/天涯神帖210+/       论坛存档
├── [2.5G] Comet/                代理工具
├── [2G]   .openclaw/            OpenClaw
├── [1.7G] .cargo/               Rust包
├── [1.5G] .nvm/                 Node版本
├── [1.1G] .local/               本地数据
├── [1.0G] Binance/              币安
├── [996M] .npm-global/          npm全局
├── [947M] Quark/                夸克网盘
├── [782M] .antigravity/
├── [494M] .vscode/
└── [364M] v2rayN/
```

---

## ⚠️ 重点关注 (可清理)

```
建议清理项:
│
├── 🗑️ Chrome Profile 11     [9.7G]  不使用的Chrome账号
├── 🗑️ Chrome Profile 14     [5.2G]  不使用的Chrome账号
├── 🗑️ OptGuideOnDeviceModel [4.0G]  Chrome AI模型(可重新下载)
├── 🗑️ .rustup               [18G]   Rust文档(可删除)
├── 🗑️ .colima               [5.8G]  Docker虚拟机
└── 🗑️ Chrome/Caches        [189M]  浏览器缓存
```

---

## 📝 重启后对比

重启后请运行相同命令对比：
```bash
df -h /
du -sh ~/Library/Application\ Support/Google
du -sh ~/.rustup
du -sh ~/.colima
```
