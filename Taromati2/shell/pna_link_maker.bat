chcp 65001
@echo off
for /r %%a in (*.pna) do mklink /h "%%a.png" "%%a"
@echo on
