<h1 align="center">植物大战僵尸 AI 魔改版</h1>
<p align="center">
  <a href="https://opensource.org/license/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT许可证"></a>
  <a href="#"><img src="https://img.shields.io/badge/version-2.0.0-green.svg" alt="版本"></a>
  <a href="#"><img src="https://img.shields.io/badge/platform-Web-orange.svg" alt="平台"></a>
  <a href="#"><img src="https://img.shields.io/badge/AI-Powered-purple.svg" alt="AI驱动"></a>
</p>

<hr/>

## 📖 项目简介

这是一个由 AI 驱动的网页版植物大战僵尸游戏，不仅基于 AI 辅助开发，更支持玩家们通过 AI 进行魔改。游戏不仅复刻了经典植物大战僵尸的核心玩法，还允许每个玩家成为"法师"，用自己的"咒语集"（prompt 集）来创造独特的游戏体验。

本项目展示了如何将 AI 与游戏开发结合，让每个参与者都能贡献自己的创意，打造属于自己的植物大战僵尸版本。

![首页点击开始](https://cdn.canghecode.com/blog/20250508232428.png)

![游戏界面](https://cdn.canghecode.com/blog/20250508232626.png)

AI创作教程：[我用谷歌新发布的AI做了一个植物大战僵尸游戏，全程不写一行代码，好酷！](https://mp.weixin.qq.com/s/-0pbpXIBu2T1-FmVFsUPYg)

## ✨ 游戏特点

- **纯网页实现**：无需安装，在任何现代浏览器中即可运行
- **响应式设计**：支持各种设备和屏幕尺寸
- **经典元素重现**：
  - 向日葵产生阳光资源
  - 豌豆射手防御僵尸
  - 波次进攻系统
  - 阳光经济系统
- **简单直观的操作**：点击放置植物，轻松上手
- **逐步增强的难度**：随着游戏进行，僵尸数量和种类会增加

## 🎮 游戏演示

![游戏演示](https://i.imgur.com/example.gif)

## 🚀 如何开始

### 在线体验

访问 [游戏演示链接](#) 即可在线体验游戏

### 本地运行

1. 克隆本仓库到本地
```bash
git clone https://github.com/yourusername/plants-vs-zombies-ai.git
```

2. 使用浏览器打开 `index.html` 文件
```bash
cd plants-vs-zombies-ai
# 使用浏览器打开index.html
# 在macOS上：
open index.html
# 在Linux上：
xdg-open index.html
# 在Windows上：
start index.html
```

也可以使用任意HTTP服务器托管文件：
```bash
# 使用Python的简易HTTP服务器
python -m http.server
# 然后访问 http://localhost:8000
```

## 🎯 游戏规则

1. 游戏开始时，你有150点阳光资源
2. 向日葵每隔一段时间会产生阳光
3. 使用阳光资源来种植植物：
   - 向日葵：50阳光
   - 豌豆射手：100阳光
4. 僵尸会从右侧进入，你需要种植植物来阻止它们到达左侧
5. 如果任何僵尸到达最左侧，游戏结束
6. 随着游戏进行，僵尸会越来越多，难度会逐渐增加

## 💻 技术实现

- **HTML5 Canvas**：用于绘制游戏界面和动画
- **JavaScript ES6+**：实现游戏逻辑和交互
- **CSS3**：提供响应式设计和视觉效果
- **Tailwind CSS**：优化UI展示效果
- **Web Font**：使用Google Fonts提升视觉体验

## 🧠 AI 魔改系统

本项目采用了创新的 AI 魔改系统，让每个参与者都能成为游戏设计师：

### 🎭 法师系统
- **成为法师**：每个参与者都是一位游戏魔改大师
- **咒语集**：通过编写专属的 prompt 集来创造独特玩法
- **魔改效果**：可以改变游戏规则、添加新植物、设计新僵尸等

### 🔮 咒语集功能
- **自定义玩法**：创造专属的游戏机制
- **植物设计**：设计新的植物类型和能力
- **僵尸创新**：创造独特的僵尸种类
- **场景魔改**：定制游戏场景和关卡

### 💫 AI 辅助开发
- **架构设计**：AI 辅助游戏架构规划
- **代码生成**：自动生成游戏逻辑代码
- **创意激发**：AI 提供创新玩法建议
- **优化建议**：性能和游戏体验优化

## 📝 待实现功能

- [ ] 添加更多种类的植物
- [ ] 添加更多种类的僵尸
- [ ] 实现夜间场景
- [ ] 添加游戏音效
- [ ] 存档功能
- [ ] 更丰富的关卡设计

## 🤝 贡献指南

欢迎提交问题和贡献代码！请遵循以下步骤：

1. Fork本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m '添加一些很棒的功能'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个Pull Request

## 🎨 成为魔改法师

### 🚀 快速开始
1. 克隆魔法工坊：
   ```bash
   git clone <项目地址>
   cd plants-vs-zombies-ai
   ```

2. 启动魔法工坊：
   ```bash
   python -m http.server
   # 访问 http://localhost:8000 开始你的魔法之旅
   ```

### 📚 创建咒语集
1. 打开 Web 界面，点击"咒语集管理"
2. 输入你的法师名称和咒语内容
3. 点击"上传咒语"保存你的创作

### 🛠 高级魔法师
如果你精通魔法（代码），还可以：
1. 直接编辑 `prompts/` 目录下的咒语集文件
2. 使用 `scripts/manage_prompts.py` 管理咒语
3. 通过 Pull Request 分享你的魔法

## 📁 魔法工坊结构
```
plants-vs-zombies-ai/
├── index.html         # 魔法主界面
├── prompts/           # 咒语集存储
│   └── README.md      # 咒语编写指南
└── scripts/           # 魔法工具箱
    └── manage_prompts.py  # 咒语管理工具
```

## 📜 版权说明

本项目仅用于学习和研究目的，不得用于商业用途。

原版"植物大战僵尸"游戏版权归**EA/PopCap**所有。

## 👍 公众号

微信搜 **苍何** 或扫描下方二维码关注苍何的原创公众号，回复 **AI** 即可加入AI交流群和5000+AI极客一同学习交流。

![苍何微信公众号](https://cdn.tobebetterjavaer.com/stutymore/%E6%89%AB%E7%A0%81_%E6%90%9C%E7%B4%A2%E8%81%94%E5%90%88%E4%BC%A0%E6%92%AD%E6%A0%B7%E5%BC%8F-%E6%A0%87%E5%87%86%E8%89%B2%E7%89%88.png)

## ⭐ star 趋势图

[![Star History Chart](https://api.star-history.com/svg?repos=freestylefly/plants-vs-zombies-ai&type=Date)](https://star-history.com/#freestylefly/plants-vs-zombies-ai&Date)



## 📄 许可证

[MIT License (MIT)](https://opensource.org/licenses/MIT)<hr/>
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Copyright (c) 2025-2025 PmHub（苍何）





