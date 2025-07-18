@echo off
echo 🤖 Browser Agent - Quick Start
echo ==============================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed
    echo    Please install Python 3.8+ and try again
    pause
    exit /b 1
)

echo ✅ Python found
for /f "tokens=*" %%i in ('python --version') do echo    %%i

REM Check if we're in the right directory
if not exist requirements.txt (
    echo ❌ requirements.txt not found
    echo    Please run this script from the brouser-agent directory
    pause
    exit /b 1
)

echo ✅ In correct directory

REM Run initialization
echo.
echo 🚀 Running initialization...
python init.py

echo.
echo 🎉 Browser Agent setup complete!
echo.
echo Quick commands:
echo   python run_gui.py        # Launch GUI
echo   python init.py           # Re-run setup
echo   start.bat                # This script
echo.
pause