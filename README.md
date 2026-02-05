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

1. 打开仓库，点击顶部的 **Settings**（若看不到，点仓库名旁的 **▼** 再选 Settings）。
2. 在**左侧边栏**找到 **“Code and automation”**，点击 **Pages**。
3. 在 **Build and deployment** 里，**Source** 一定要选 **Deploy from a branch**（不要选 “GitHub Actions”）。
4. **Branch** 选 **main**（不要选 gh-pages）。
5. **Folder**：若页面上有第二个下拉框，选 **/ (root)**；若没有单独的 Folder 选项，只要 Branch 选的是 main，一般就是用仓库根目录，直接点 **Save** 即可。
6. 等 2–3 分钟，再访问 `https://jiashenhzju.github.io`。

**Save 点不了（灰色）时**：GitHub 有时在“没检测到改动”时会禁用 Save。可以这样试：
- **Branch** 下拉框先选 **None**，点一次 **Save**（会先取消发布）；
- 再在 **Branch** 里选 **main**，再点 **Save**。
若仍不行，换浏览器或无痕窗口试一次，或确认仓库里已有 **main** 分支且你有权限。

> 若左侧没有 Pages：在 **“Code and automation”** 区域找。参考：[GitHub 官方说明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

---

**关于 404 和 gh-pages 分支**

- **404**：多半是 Pages 当前从 **gh-pages** 分支发布，而那个分支是空的或没有你的 `index.html`。  
  **处理**：在 Settings → Pages 里把 **Source** 设为 **Deploy from a branch**，**Branch** 选 **main**（不要选 gh-pages），再保存。等几分钟后再打开 `https://jiashenhzju.github.io`。
- **gh-pages 分支**：是以前用 “GitHub Actions” 或模板时常见的一个分支，用来存发布出来的静态文件。  
  你现在网站内容在 **main** 上，所以不用管 gh-pages：在 Pages 里选 **main** 即可。若以后确定不用，可以在仓库 **Code** 页切到分支列表里删除 **gh-pages** 分支（可选）。

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
