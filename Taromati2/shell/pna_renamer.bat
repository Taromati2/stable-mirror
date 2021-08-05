chcp 65001
@echo off
for /r %%a in (*.pna) do ren "%%a" "%%~na.jpg"
@echo on
