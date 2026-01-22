@echo off
title OnlySniper - Professional Discord Vanity Sniper
echo ==========================================
echo    ONLYSNIPER - PROFESSIONAL EDITION
echo ==========================================
echo.
echo [1/2] Checking/Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [!] Failed to install dependencies. 
    echo [!] Please make sure Python and Pip are installed and added to PATH.
    pause
    exit /b
)
echo.
echo [2/2] Starting OnlySniper...
echo.
python onlysniper.py
pause
