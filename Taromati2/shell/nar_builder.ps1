if(Test-Path ".vscode/.nar_icon"){
	Move-Item ".vscode/.nar_icon" ".nar_icon"
}
Get-ChildItem . -Directory | ForEach-Object {
	if (Test-Path "$($_.FullName)\install.txt"){
		# 将$($_.FullName)\profile文件夹移动到.\profile文件夹
		if(Test-Path ".\profile"){
			Remove-Item ".\profile" -Recurse -Force
		}
		if(Test-Path "$($_.FullName)\profile"){
			Move-Item "$($_.FullName)\profile" ".\profile"
		}
		7z a -tzip "$($_.BaseName).nar" -mx=9 -mmt -mm=LZMA -md=1536m -mfb=273 -mtc=off "$($_.FullName)" ".nar_icon"
		# 将.\profile文件夹移动到$($_.FullName)\profile文件夹
		if(Test-Path "$($_.FullName)\profile"){
			Move-Item ".\profile" "$($_.FullName)\profile"
		}
	}
}
if(Test-Path ".nar_icon"){
	Move-Item ".nar_icon" ".vscode/.nar_icon"
}
