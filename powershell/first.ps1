# function Get-time {get-date -Format hh:mm}

# $Name = "Print Spooler"
# $Service = Get-Service -display $Name -ErrorAction silentlycontinue
# If (-Not $Service) {$Name + " is not installed on this computer."}
# Else {$Name + " is installed."
# $Name + ":s status is: " + $Service.status }

# First Basic Script

# This works on Windows only, gets output for C drive, space, etc for remote computer

# Below is simple script, one after is custom
# Get-CimInstance -ClassName Win32_logcialdisk - Filter "DeviceID='C'" -ComputerName inhyd-dc01  | Select-Object Pscomputername, FreeSpace
Get-CimInstance -ClassName Win32_logcialdisk -Filter "DeviceID='C:'" -ComputerName inhyd-dc01 | Select-Object @{name="ComputerName";e={$_.Pscomputername}}, 
@{name="FreeSpaceinGB";e={$_.FreeSpace /1gb -as [int]}} 

Get-CimInstance -ComputerName inhyd-dc01 -ClassName Win32_logcialdisk -Filter "Device='C'" |
 Select-Object @{name="ComputerName";e={$_.Pscomputername}} ,
  @{Name="FreeSpaceinGB";E={$_.FreeSpace /1gb -as [int]}}

# Intermediate Script - only works on windows
<#
.SYNOPSIS
This is for my computers disk info
.DESCRIPTION
This can be used for getting disk info on Windows machine
.PARAMETER MachineName
.EXAMPLE 
to connect and give remote Computer Disk Free Space report
Disk-info -MachineName Localhost
#>
param (
$MachineName = 'inhyd-dc01'
)

Get-CimInstance -ComputerName $MachineName -ClassName Win32_logcialdisk -Filter "Device='C'" |
 Select-Object @{name="ComputerName";e={$_.Pscomputername}} ,
  @{Name="FreeSpaceinGB";E={$_.FreeSpace /1gb -as [int]}}


#Get content of computers
$computers = Get-Content "C:\computers.txt"

$session = New-PSSsession -ComputerName $computers

ForEach($line in $computers)
{
  Invoke-Command -ComputerName $line -ScriptBlock{Get-Service -Name bits}  
}