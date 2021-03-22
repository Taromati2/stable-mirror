chcp 65001
@echo off
for /r %%a in (*.pna) do mklink /h "%%~dpa/profile/%%~nxa.png" "%%a"
@echo on
