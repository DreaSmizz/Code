# function Get-time {get-date -Format hh:mm}

# $Name = "Print Spooler"
# $Service = Get-Service -display $Name -ErrorAction silentlycontinue
# If (-Not $Service) {$Name + " is not installed on this computer."}
# Else {$Name + " is installed."
# $Name + ":s status is: " + $Service.status }

# First Basic Script

Get-CimInstance -ClassName Win32_logcialdisk -Filter "DeviceID='C:'"