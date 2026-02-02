# 个人主页 · jiashenhzju.github.io

基于 [Wwstarry/Wwstarry.github.io](https://github.com/Wwstarry/Wwstarry.github.io) 风格的个人学术/个人主页模板，部署在 **GitHub Pages**。

- 仓库：<https://github.com/jiashenhzju/jiashenhzju.github.io>
- 访问：<https://jiashenhzju.github.io>

## 📌 致谢

本模板参考了以下仓库的设计与结构：

- [Wwstarry/Wwstarry.github.io](https://github.com/Wwstarry/Wwstarry.github.io)
- [song-chen1/song-chen1.github.io](https://github.com/song-chen1/song-chen1.github.io)
- [Purshow/Purshow.github.io](https://github.com/Purshow/Purshow.github.io)
- [SuperFCR/SuperFCR.github.io](https://github.com/SuperFCR/SuperFCR.github.io)

## 🚀 在 GitHub 上部署

### 1. 创建仓库

1. 登录 [GitHub](https://github.com)，点击 **New repository**。
2. 仓库名必须为：**`你的用户名.github.io`**（例如：`jiashenhzju.github.io`）。
3. 选择 **Public**，可不勾选 README（本地已有），创建仓库。

### 2. 推送本地项目

在项目根目录执行：

```bash
git init
git add .
git commit -m "Initial commit: personal homepage"
git branch -M main
git remote add origin https://github.com/jiashenhzju/jiashenhzju.github.io.git
git push -u origin main
```

### 3. 开启 GitHub Pages

1. 打开仓库 → **Settings** → 左侧 **Pages**。
2. 在 **Source** 中选择 **Deploy from a branch**。
3. **Branch** 选 `main`，**Folder** 选 `/ (root)`。
4. 保存后等待 1–2 分钟。

访问 **https://jiashenhzju.github.io** 即可看到你的个人主页。

## 🖥️ 本地运行与调试

本项目为静态 HTML/CSS/JS，无需构建，可直接用本地服务器预览和调试。

### 方式一：npm 脚本（推荐，支持保存后自动刷新）

```bash
# 安装依赖（首次）
npm install

# 启动开发服务器（默认 http://localhost:3000，修改文件后自动刷新）
npm run dev
```

### 方式二：不安装依赖，直接运行

```bash
# 使用 live-server（自动刷新）
npx live-server --port=3000 --open=/

# 或使用 serve（仅静态服务）
npx serve -l 3000
```

### 方式三：Python 自带 HTTP 服务

```bash
# Python 3
python3 -m http.server 3000

# 浏览器访问 http://localhost:3000
```

### 方式四：VS Code

安装 [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) 插件，在 `index.html` 上右键选择 **“Open with Live Server”** 即可本地预览并自动刷新。

---

调试时直接修改 `index.html` 或 `profile.css`，保存后刷新（或使用上述带自动刷新的方式）即可看到效果。

## ✏️ 如何修改内容

- **个人信息**：编辑 `index.html` 中的姓名、邮箱、学校、简介、教育、论文、奖项等。
- **头像**：将头像图片命名为 `avatar.jpg`，放入 `assets/` 目录；无图片时会显示占位符。
- **News 打字机**：在 `index.html` 底部 `<script>` 中的 `newsMessages` 数组里修改要轮播的新闻文案。
- **样式**：修改 `profile.css` 调整颜色、字体、间距等。

## 📁 项目结构

```
jiashenhzju.github.io/
├── index.html      # 主页面
├── profile.css     # 样式表
├── package.json    # 本地开发脚本（npm run dev）
├── assets/         # 图片等资源（如 avatar.jpg、论文配图）
├── README.md
└── .gitignore
```

## 📄 许可证

本项目采用 [CC0-1.0](LICENSE) 许可证。
