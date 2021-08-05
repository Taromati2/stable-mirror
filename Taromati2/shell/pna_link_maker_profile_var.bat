chcp 65001
@echo off
for /r %%a in (*.pna) do mkdir "%%~dpa/profile/" & mklink /h "%%~dpa/profile/%%~nxa.png" "%%a"
@echo on
