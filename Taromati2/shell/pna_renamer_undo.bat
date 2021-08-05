chcp 65001
@echo off
for /r %%a in (*.jpg) do ren "%%a" "%%~na.pna"
@echo on
