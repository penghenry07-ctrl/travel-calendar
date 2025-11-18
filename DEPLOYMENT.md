# 📖 详细部署指南

## 方案选择

我为你提供了几种部署方案，推荐程度从高到低：

### 🥇 方案一：Render（最推荐）
- ✅ 完全免费
- ✅ 部署简单
- ✅ 自动HTTPS
- ✅ 支持自定义域名
- ⚠️ 国内访问可能较慢
- ⚠️ 15分钟不访问会休眠

### 🥈 方案二：Vercel
- ✅ 国内访问速度快
- ✅ 完全免费
- ✅ 自动HTTPS
- ⚠️ 需要改造成Serverless架构（稍复杂）

### 🥉 方案三：Railway
- ✅ 部署简单
- ✅ 性能好
- ⚠️ 免费额度有限（每月5美元额度）

---

## 🎯 方案一：Render 详细步骤

### 步骤1：准备 Git 和 GitHub

#### 1.1 安装 Git

**Windows:**
1. 下载 https://git-scm.com/download/win
2. 双击安装，全部使用默认选项

**Mac:**
```bash
# 打开终端，输入：
git --version
# 如果没有安装会提示安装
```

#### 1.2 配置 Git
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

#### 1.3 创建 GitHub 账号
1. 访问 https://github.com
2. 点击 "Sign up" 注册
3. 验证邮箱

### 步骤2：上传项目到 GitHub

#### 2.1 创建仓库
1. 登录 GitHub
2. 点击右上角 "+" → "New repository"
3. 填写信息：
   - Repository name: `travel-calendar`
   - Description: 旅行日历应用
   - Public 或 Private 都可以
   - **不要**勾选任何初始化选项
4. 点击 "Create repository"

#### 2.2 上传代码

**方法A：使用命令行（推荐）**

1. 打开终端/命令提示符
2. 进入项目文件夹：
   ```bash
   cd /path/to/travel-calendar-project
   ```
3. 执行命令：
   ```bash
   git init
   git add .
   git commit -m "首次提交"
   git branch -M main
   git remote add origin https://github.com/你的用户名/travel-calendar.git
   git push -u origin main
   ```

**方法B：使用 GitHub Desktop（图形界面）**

1. 下载 https://desktop.github.com/
2. 登录 GitHub 账号
3. File → Add Local Repository
4. 选择项目文件夹
5. 点击 "Publish repository"

### 步骤3：部署到 Render

#### 3.1 注册 Render
1. 访问 https://render.com
2. 点击 "Get Started for Free"
3. 选择 "Sign in with GitHub"（用GitHub登录最方便）
4. 授权 Render 访问你的 GitHub

#### 3.2 创建 Web Service
1. 登录后，点击 "New +" 按钮
2. 选择 "Web Service"
3. 点击 "Connect a repository"
4. 如果看不到仓库，点击 "Configure account" 授权访问
5. 找到 `travel-calendar` 仓库，点击 "Connect"

#### 3.3 配置服务
填写以下信息：

| 配置项 | 填写内容 |
|--------|----------|
| Name | `travel-calendar` 或任意名称 |
| Region | Singapore（离中国最近）|
| Branch | `main` |
| Runtime | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Instance Type | `Free` |

#### 3.4 等待部署
1. 点击 "Create Web Service"
2. 等待1-2分钟，查看日志
3. 看到 "Your service is live" 表示成功！
4. 复制网址，例如：`https://travel-calendar-abcd.onrender.com`

### 步骤4：测试访问

1. 在浏览器打开你的网址
2. 尝试添加一个旅行计划
3. 刷新页面，确认数据保存成功
4. 在手机上访问同一个网址测试

---

## 📱 手机端设置

### iPhone (Safari)
1. 打开网址
2. 点击底部分享按钮（方框+向上箭头）
3. 向下滚动，点击"添加到主屏幕"
4. 自定义名称（如"旅行日历"）
5. 点击"添加"

### Android (Chrome)
1. 打开网址  
2. 点击右上角三个点
3. 选择"添加到主屏幕"
4. 自定义名称
5. 点击"添加"

---

## 🔧 常见问题

### Q1: 部署失败怎么办？
**A:** 检查以下几点：
1. 确认所有文件都上传到 GitHub
2. 查看 Render 的 Logs 标签页，看具体错误
3. 确认 requirements.txt 文件存在
4. 确认 app.py 文件存在

### Q2: 网站打开很慢？
**A:** Render 免费版会在15分钟无访问后休眠，首次访问需要约30秒启动。
解决方法：
1. 使用 UptimeRobot 等服务定期访问保持唤醒
2. 升级到付费版（7美元/月）
3. 考虑使用其他平台（如 Vercel）

### Q3: 数据会丢失吗？
**A:** 不会！数据保存在服务器的 `trips_data.json` 文件中，即使服务休眠也不会丢失。

### Q4: 如何备份数据？
**A:** 
1. 点击"导出HTML"按钮下载备份
2. 或者在 Render 的 Shell 中下载 `trips_data.json` 文件

### Q5: 如何更新代码？
**A:** 
```bash
# 修改代码后
git add .
git commit -m "更新说明"
git push
```
Render 会自动检测并重新部署！

### Q6: 国内访问太慢怎么办？
**A:** 考虑以下方案：
1. 使用国内云服务（阿里云、腾讯云）
2. 使用 Vercel（国内访问较快）
3. 使用 Cloudflare Workers
4. 购买VPS自己部署

---

## 🎁 高级功能

### 绑定自定义域名
1. 在 Render 的 Settings → Custom Domain
2. 添加你的域名
3. 在域名DNS设置中添加 CNAME 记录

### 定期唤醒服务
使用 UptimeRobot (https://uptimerobot.com/)：
1. 注册账号
2. 添加监控，URL 填你的网址
3. 检查间隔设为 5 分钟

---

## 📞 需要帮助？

如果遇到问题：
1. 查看 Render 的日志（Logs 标签页）
2. 检查 GitHub 仓库文件是否完整
3. 在 GitHub 仓库创建 Issue 提问

祝你部署顺利！🎉
