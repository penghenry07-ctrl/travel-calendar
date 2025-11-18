# 🌍 旅行日历 - Travel Calendar

一个美观实用的旅行日历应用，支持添加、编辑、删除旅行计划，数据保存在服务器端，可在任何设备上访问。

## ✨ 功能特点

- 📅 2025-2026年完整日历视图
- ✈️ 添加、编辑、删除旅行计划
- 🎨 多种预设颜色标记
- 💾 服务器端数据持久化
- 📱 移动端友好设计
- 🖨️ 支持打印和导出

## 🚀 快速部署到 Render（免费）

### 前置要求
- GitHub 账号
- Render 账号（可以用GitHub登录）

### 部署步骤

#### 1️⃣ 上传到 GitHub

1. 在 GitHub 创建新仓库（Repository）
   - 进入 https://github.com/new
   - 仓库名：`travel-calendar`（或任意名称）
   - 选择 **Public** 或 **Private**
   - **不要**勾选 "Add a README file"
   - 点击 "Create repository"

2. 在本地电脑打开终端/命令行，进入项目文件夹

3. 执行以下命令（替换 `YOUR_USERNAME` 为你的GitHub用户名）：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/travel-calendar.git
git push -u origin main
```

#### 2️⃣ 部署到 Render

1. 访问 https://render.com/ 并登录（可以用GitHub登录）

2. 点击 "New +" → 选择 "Web Service"

3. 连接你的 GitHub 仓库
   - 如果第一次使用，需要授权 Render 访问 GitHub
   - 找到 `travel-calendar` 仓库，点击 "Connect"

4. 配置部署设置：
   - **Name**: `travel-calendar`（或任意名称）
   - **Region**: 选择离你最近的区域（如 Singapore）
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: 选择 `Free`

5. 点击 "Create Web Service"

6. 等待部署完成（约1-2分钟），你会看到一个类似这样的网址：
   ```
   https://travel-calendar-xxxx.onrender.com
   ```

7. 点击这个网址，你的旅行日历就可以使用了！🎉

### 📱 手机访问

直接在手机浏览器输入你的 Render 网址即可访问！

建议：
- **iPhone**: 在Safari中打开后，点击分享按钮 → "添加到主屏幕"
- **Android**: 在Chrome中打开后，点击菜单 → "添加到主屏幕"

这样就可以像App一样快速打开了！

## 📝 使用说明

1. **添加旅行**：
   - 在日历上点击开始日期
   - 再点击结束日期
   - 在弹窗中输入目的地
   - 选择颜色（可选）
   - 点击"确认"

2. **修改旅行**：
   - 在旅行列表中点击"修改"按钮
   - 更新信息后点击"更新"

3. **删除旅行**：
   - 在旅行列表中点击"删除"按钮
   - 确认删除

## 🔧 本地开发

如果你想在本地测试：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行应用
python app.py

# 访问 http://localhost:5000
```

## 💾 数据保存

- 所有旅行数据保存在服务器的 `trips_data.json` 文件中
- Render 免费版会在15分钟无访问后休眠，但数据不会丢失
- 首次访问休眠的服务需要等待约30秒唤醒

## ⚠️ 注意事项

1. **Render 免费版限制**：
   - 每月 750 小时免费时长（足够个人使用）
   - 15分钟无访问会自动休眠
   - 休眠后首次访问需要约30秒启动时间

2. **数据备份**：
   - 建议定期使用"导出HTML"功能备份数据
   - 或者定期访问保持服务活跃

## 🎯 更新代码

当你修改代码后，执行：

```bash
git add .
git commit -m "更新说明"
git push
```

Render 会自动检测到更新并重新部署！

## 📧 问题反馈

如有问题，请在 GitHub 仓库创建 Issue。

---

享受你的旅行规划吧！✈️🌏
