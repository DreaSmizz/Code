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

# Intermediate Script - only works on windows