@echo off
chcp 65001 >nul
echo 🧪 开始测试旅行日历应用...
echo.

REM 检查Python
echo 1️⃣ 检查 Python...
where python >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :python_found
)

where python3 >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    goto :python_found
)

echo ❌ 未找到 Python，请先安装 Python 3
pause
exit /b 1

:python_found
for /f "tokens=*" %%i in ('%PYTHON_CMD% --version') do set PYTHON_VERSION=%%i
echo ✅ Python 已安装: %PYTHON_VERSION%
echo.

REM 检查pip
echo 2️⃣ 检查 pip...
%PYTHON_CMD% -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ 未找到 pip
    pause
    exit /b 1
)
echo ✅ pip 已安装
echo.

REM 安装依赖
echo 3️⃣ 安装依赖...
%PYTHON_CMD% -m pip install -r requirements.txt
echo ✅ 依赖安装完成
echo.

REM 检查必要文件
echo 4️⃣ 检查必要文件...
set MISSING_FILES=0

if not exist "app.py" (
    echo ❌ 缺少文件: app.py
    set MISSING_FILES=1
) else (
    echo ✅ app.py
)

if not exist "index.html" (
    echo ❌ 缺少文件: index.html
    set MISSING_FILES=1
) else (
    echo ✅ index.html
)

if not exist "requirements.txt" (
    echo ❌ 缺少文件: requirements.txt
    set MISSING_FILES=1
) else (
    echo ✅ requirements.txt
)

if not exist "trips_data.json" (
    echo ❌ 缺少文件: trips_data.json
    set MISSING_FILES=1
) else (
    echo ✅ trips_data.json
)

if %MISSING_FILES% equ 1 (
    echo.
    echo ❌ 存在缺失文件，请检查
    pause
    exit /b 1
)
echo.

REM 启动服务
echo 5️⃣ 启动服务...
echo 🌐 服务运行在: http://localhost:5000
echo 📱 请在浏览器中打开上面的地址
echo 🛑 按 Ctrl+C 停止服务
echo.

%PYTHON_CMD% app.py
pause
