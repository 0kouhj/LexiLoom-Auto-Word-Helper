:: build_old.bat
@echo off
pyinstaller -D -w ^
--name "LexiLoom" ^
--add-data "app/gui/main_window.ui;app/gui" ^
--add-data "bin;bin" ^
--collect-all easyocr ^
run_old.py
pause