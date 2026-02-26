# MBTI 性格测试网站

一个基于 Astro 的轻量型前端项目，用于展示并运行 MBTI 性格测试。该仓库包含前端页面、布局与资源，适合快速在本地预览或部署到静态站点托管服务（例如 Netlify）。

**线上演示**: https://cnmbti.netlify.app/ （这是作者的线上演示站点）

**主要功能**

- **双题库支持**：保留原始 93 题选择测试，同时新增 100 题评分型随机测评。
- **首页亮点**：动态趣味事实、功能卡片介绍双模式，增强互动与吸引力。
- **会员系统提示**：结果页面会提示“会员专享更多分析”以引导付费升级。
- **丰富的 AI 分析**：100题版本结束后会生成深入的个性、职业、事业、爱情等评估模板。
- **简洁的问卷页面**：轻量化 UI，适配移动与桌面。
- **结果展示**：根据分值给出 MBTI 类型及简短解析。
- **基于 Astro 构建**：静态站点生成，构建产物位于 `dist/`。

**项目结构（简要）**

- `public/`：静态资源
- `src/assets/`：图片与静态资源
- `src/components/`：可复用组件
- `src/layouts/`：页面布局
- `src/pages/`：各页面入口（如 `index.astro`, `result.astro` 等）

**快速开始（本地开发）**

- **安装依赖**: `npm install`
- **启动开发服务器**: `npm run dev` （默认在 `localhost:4321`）
- **构建生产包**: `npm run build`（产物输出到 `dist/`）
- **本地预览构建**: `npm run preview`

**部署到 Netlify（推荐）**

1. 在 GitHub/GitLab/Bitbucket 上创建仓库并推送本项目代码。
2. 登录 Netlify，选择 "New site from Git"，连接你的代码仓库。
3. 在部署设置中填写：
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
4. 保存并触发部署，部署完成后即可访问生成的站点（可设置自定义域名）。

或者使用 Netlify CLI（适合手动部署）：

```sh
npm install -g netlify-cli
npm run build
netlify deploy --prod --dir=./dist
```

（首次使用 `netlify deploy` 可能需先通过 `netlify login` 或 `netlify init` 关联站点）

**其他部署选项**

- Vercel：将仓库导入 Vercel，构建命令同样使用 `npm run build`，输出目录 `dist`。
- 静态托管（如 GitHub Pages）：需要把 `dist/` 的内容发布到 Pages 或通过 CI/CD 上传到你的静态托管服务。

**自定义与扩展**

- 如果需要更改测试题与解析逻辑，请编辑 `src/pages` 与 `src/components` 下的相关文件。
- 想加入后端统计或持久化，可将表单结果 POST 到你的 API，然后在前端调用。

**贡献**

- 欢迎提交 Issue 与 Pull Request。

**许可证**

- 未特别声明前，请根据项目需要添加合适的 LICENSE 文件。

---
