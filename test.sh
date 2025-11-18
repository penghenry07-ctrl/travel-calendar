#!/bin/bash

echo "🧪 开始测试旅行日历应用..."
echo ""

# 检查Python
echo "1️⃣ 检查 Python..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ 未找到 Python，请先安装 Python 3"
    exit 1
fi

echo "✅ Python 已安装: $($PYTHON_CMD --version)"
echo ""

# 检查pip
echo "2️⃣ 检查 pip..."
if command -v pip3 &> /dev/null; then
    PIP_CMD=pip3
elif command -v pip &> /dev/null; then
    PIP_CMD=pip
else
    echo "❌ 未找到 pip"
    exit 1
fi

echo "✅ pip 已安装"
echo ""

# 安装依赖
echo "3️⃣ 安装依赖..."
$PIP_CMD install -r requirements.txt --break-system-packages 2>/dev/null || $PIP_CMD install -r requirements.txt
echo "✅ 依赖安装完成"
echo ""

# 检查必要文件
echo "4️⃣ 检查必要文件..."
files=("app.py" "index.html" "requirements.txt" "trips_data.json")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ 缺少文件: $file"
        exit 1
    fi
done
echo ""

# 启动服务
echo "5️⃣ 启动服务..."
echo "🌐 服务运行在: http://localhost:5000"
echo "📱 请在浏览器中打开上面的地址"
echo "🛑 按 Ctrl+C 停止服务"
echo ""

$PYTHON_CMD app.py
