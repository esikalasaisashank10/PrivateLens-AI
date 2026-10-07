@echo off
title PrivateLens AI - Build
python -m pip install -r requirements.txt
python -m PyInstaller --noconfirm --clean --onefile --windowed --name PrivateLensAI PrivateLensAI.py
echo.
echo Build complete: dist\PrivateLensAI.exe
pause
