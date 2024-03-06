[CmdletBinding()]
param (
	[Parameter(ValueFromRemainingArguments)]
	[string]$command
)
ghost-terminal -c $command
