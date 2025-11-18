# 🚀 快速开始指南

## 📦 你已经下载的文件

你的项目包含以下文件：

```
travel-calendar-project/
├── app.py                 # 后端服务器代码
├── index.html            # 前端页面
├── requirements.txt      # Python依赖
├── trips_data.json       # 数据存储文件
├── test.sh              # Mac/Linux 测试脚本
├── test.bat             # Windows 测试脚本
├── README.md            # 项目说明
├── DEPLOYMENT.md        # 详细部署指南
└── .gitignore           # Git忽略文件
```

## ⚡ 三步部署到云端

### 第一步：本地测试（可选但推荐）

**Windows 用户：**
双击运行 `test.bat`

**Mac/Linux 用户：**
```bash
chmod +x test.sh
./test.sh
```

如果一切正常，浏览器会打开 http://localhost:5000

### 第二步：上传到 GitHub

1. 在 https://github.com/new 创建新仓库
   - 仓库名：`travel-calendar`
   - 选择 Public
   - **不要**勾选任何初始化选项

2. 在项目文件夹打开终端，执行：

```bash
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/你的用户名/travel-calendar.git
git push -u origin main
```

### 第三步：部署到 Render

1. 访问 https://render.com （用 GitHub 登录）
2. 点击 "New +" → "Web Service"
3. 选择你的 `travel-calendar` 仓库
4. 填写配置：
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: `Free`
5. 点击 "Create Web Service"
6. 等待2分钟，完成！

你会得到一个网址，例如：
```
https://travel-calendar-xxxx.onrender.com
```

## 📱 在手机上使用

直接访问你的网址，然后"添加到主屏幕"，就像使用App一样！

## ❓ 遇到问题？

- 查看 `DEPLOYMENT.md` 了解详细步骤
- 查看 `README.md` 了解功能说明

## 🎯 接下来做什么？

- ✅ 在日历上添加你的第一个旅行计划
- ✅ 在手机上访问测试
- ✅ 分享给朋友一起使用
- ✅ 定期使用"导出HTML"功能备份数据

祝你使用愉快！🎉
