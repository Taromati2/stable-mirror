[CmdletBinding()]
param (
	[Parameter(ValueFromRemainingArguments)]
	[string[]]$theargs
)
[system.collections.arraylist]$theargs = @($theargs)
$theargs.AddRange(@('-gp', "$PSScriptRoot/../..", '--disable-text', 'all')) | Out-Null
$exe = "$PSScriptRoot/../../ghost/master/saori/ghost_terminal.exe"
$theargs = $theargs | ForEach-Object { """$_""" }
Start-Process -FilePath $exe -ArgumentList $theargs -NoNewWindow -Wait
