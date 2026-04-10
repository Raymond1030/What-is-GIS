# GIS 百科全书 v2 扩充设计方案

**日期**：2026-04-11
**项目**：https://github.com/Raymond1030/What-is-GIS
**目标**：把 GIS 百科升级为面向入门者和研究者的完整学习资源

## 问题陈述

当前 v1 版本存在以下问题：
1. 主页到子页面的部分链接指向不存在的文件（coordinate-systems.html、gis-software.html）
2. 主页没链接到已存在的 `3d-gis.html`
3. 核心概念（矢量/栅格/GIS 用途）缺少直观的图片和视频解释
4. ArcGIS 等软件只有一句话介绍，没有独立详情页和截图
5. 学习资源是一个列表，没有路径指引
6. 缺少研究前沿/论文索引，研究者无法找到深入方向

## 目标用户

1. **入门者**（高中生/非专业人士）：想了解 GIS 是什么、能做什么
2. **学习者**（本科生/自学者）：想系统学习 GIS 技术
3. **研究者**（研究生/从业者）：想找最新论文、研究方向

## 修复的 bug

- 修复 `chapters/vector-data.html` 中指向 `coordinate-systems.html` 的 prev 链接
- 修复 `chapters/remote-sensing.html` 中指向 `gis-software.html` 的 next 链接
- 主页 `index.html` 添加 `3d-gis.html` 的详细阅读按钮

## 新建子页面（7 个）

### 1. `chapters/what-is-gis.html` — GIS 是什么（入门）
- 5 分钟快速理解 GIS
- 3 个生动案例开场：外卖派单/共享单车热力图/疫情传播地图
- 用 SVG 动画展示"一张图"叠加概念
- 嵌入 Esri 官方 3 分钟介绍视频（YouTube 链接卡片）
- 配 Bilibili 中文 GIS 入门视频

### 2. `chapters/history.html` — GIS 发展简史
- 故事化叙述：Snow 霍乱地图 → Tomlinson CGIS → Jack Dangermond 创立 Esri → 中国 GIS 发展 → 现代 GeoAI
- 时间轴可视化（扩展主页已有的）
- 关键人物卡片（含照片 Wikimedia 公共版权）
- 历史地图文物（Snow 地图、CGIS 早期截图、Landsat-1 首图）

### 3. `chapters/coordinate-systems.html` — 坐标系统详解
- 从地球形状开始讲起：为什么不能用经纬度直接算面积
- 大地水准面 vs 椭球体（带 SVG 示意图）
- 常见投影动画：墨卡托/UTM/高斯克吕格 的视觉对比
- 中国坐标系深入：WGS84/CGCS2000/GCJ-02/BD-09 的故事和加密原理
- 实操：如何在 ArcGIS/QGIS/Python 中做坐标转换（代码示例）

### 4. `chapters/gis-software.html` — GIS 软件生态（扩充版）
- 每个软件独立小节，含：
  - 公司/项目介绍 + logo
  - 主要功能截图（使用 Wikimedia 或官方公开图）
  - 定价模式
  - 学习曲线与社区
  - Bilibili 入门教程嵌入
  - 下载链接
- 覆盖：ArcGIS Pro、QGIS、SuperMap、MapGIS、Google Earth Engine、GRASS GIS、PostGIS、Mapbox、Cesium
- 决策树：我该选哪个软件（决策流程图 SVG）

### 5. `chapters/applications.html` — 应用领域（图文并茂）
- 每个应用领域一个大卡片，包含：
  - 真实案例描述
  - 图片/示意图
  - 视频嵌入（Bilibili 中文为主）
- 覆盖 12+ 领域：
  - 城市规划、应急管理、精准农业、公共卫生（COVID-19 地图案例）、
    物流配送、生态环保、智慧交通、不动产、考古、国防、
    商业选址、零售选址、新能源规划
- 每个案例链接到相关的深入子页面

### 6. `chapters/learning-resources.html` — 学习资源 + 路径图
- SVG 可视化学习路径图：
  - 三条路径：**WebGIS 开发** / **遥感算法研究** / **应用分析师**
  - 每条路径 5-8 个阶段
- 按阶段推荐资源：
  - 入门教材（中/英）
  - MOOC 课程
  - 开源数据集
  - 实践平台（GEE、Colab）
  - 社区论坛
- 推荐学习顺序

### 7. `chapters/research-frontier.html` — 研究前沿（核心新增页）
- 结构：先一段经典理论综述，后大量最前沿论文
- 四大研究方向，每个方向列 15-25 篇**最前沿 2024-2026 年论文**：
  - **GeoAI 与基础大模型**：Prithvi-EO、SatMAE、SatCLIP、AgriFM、Clay、DOFA、SpectralGPT 等
  - **GIS 空间分析**：时空图神经网络、城市计算、轨迹预测
  - **GIS + LLM（大语言模型）**：GeoGPT、轩辕、GeoLLM、UrbanGPT、时空大模型
  - **遥感解译算法**：Segment Anything Model 遥感应用、SAMRS、RingMo、GeoChat、SkySense 等
- 每篇论文条目包含：
  - 标题（中英）
  - 作者和机构
  - 会议/期刊/年份
  - arXiv 链接（仅链接，不复制内容）
  - 一句话要点
  - 可选：项目主页链接
- 开头有该方向的**顶会和期刊列表**（CVPR/ICCV/ICLR/NeurIPS/IJGIS/ISPRS/RSE/TGRS）

## 增强现有页面

- 给 `vector-data.html` 添加 SVG 动画解释点/线/面绘制
- 给 `raster-data.html` 添加网格化动画和 DEM 可视化
- 给 `spatial-analysis.html` 添加缓冲区/叠加的动态演示
- 给 `remote-sensing.html` 添加 NDVI 计算动画
- 给 `3d-gis.html` 添加 NeRF/3DGS 技术对比视频

## 视觉策略

### 自制 SVG / CSS 动画（优先级最高）
- 核心概念的原理动画（永远可用，加载快）

### Bilibili 嵌入（中文友好）
- 国产软件教程
- 中文 GIS 案例
- 大约 6-10 个

### YouTube 链接卡片（避免直接嵌入以防加载问题）
- 用视频封面 + 标题 + 描述做卡片
- 点击新窗口打开
- 大约 8-12 个

### 图片来源
- 已有：16 张 Nano Banana + 9 张 Wikimedia + 2 张 NASA
- 新增：Nano Banana 生成 8-10 张应用场景图、Wikimedia 找 10-15 张教育图、软件官方公开截图

## 实施计划

分 4 批并行执行，每批使用后台 agent：

**批次 1**：修复 bug + 更新主页
- 修复断链
- 主页添加所有新的详细阅读按钮
- 更新导航

**批次 2**（并行 4 个 agent）：入门类页面
- what-is-gis.html
- history.html
- coordinate-systems.html
- gis-software.html

**批次 3**（并行 3 个 agent）：核心内容页面
- applications.html
- learning-resources.html
- research-frontier.html

**批次 4**（并行执行）：
- 生成补充图片（Nano Banana）
- 增强现有页面的视觉元素

## 成功标准

1. 所有主页"详细阅读"按钮都能点进去
2. 所有子页面的 prev/next 都指向存在的文件
3. 每个新页面都有至少 3 张图片（SVG/Nano Banana/Wikimedia）
4. 每个新页面都有至少 1 个视频（嵌入或链接卡片）
5. 研究前沿页有 50+ 篇 2024-2026 年的最前沿论文链接
6. 学习路径图能清晰指引入门到前沿的学习顺序
7. 整站可从 GitHub Pages 正常访问

## 技术约束

- 保持现有的深色主题和 Syne + Noto Sans SC 字体
- 复用现有 CSS 变量和组件样式
- 视频嵌入注意国内访问问题
- **禁止复制任何受版权保护的内容**（歌词、书籍段落、论文正文等），论文只引用元数据和链接
- 图片仅使用公共领域、CC 授权或 AI 生成

## 预期产出

- 8 个新增 HTML 文件（约 400-500KB 总计）
- 10 个增强的现有文件
- 8-12 张新增图片
- 完整更新的 index.html
- 部署到 GitHub Pages
