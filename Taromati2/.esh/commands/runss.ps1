[CmdletBinding()]
param (
	[Parameter(ValueFromRemainingArguments)]
	[string]$command
)
ghost-terminal -s $command
