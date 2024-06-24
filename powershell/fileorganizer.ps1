## File Organizer
## Lists files using specific parameters
## 6/19/24
## File  manipulation choices
## 1 - Files larger than 1GB
## 2 - Files less than 1GB
## 3 - Files by certain type
## 4 - Files starting with certain letter
## 5 - Files older than certain date


Write-Host "Welcome to the File organizer program"
Write-Host "This program will allow you to list files in a path you provide and list based on type"




$Directory = Read-Host "Please enter the directory or path that you would like to perform file organization on"
Write-Host "Please select from options listed below what you would like to use."
Write-Host "These are the options for the file|path selected:
1. Files larger than 1GB
2. Files less than 1GB
3. Files by certain type (.docx, .xls, .pdf)
4. Files starting with certain letter.
5. Files by date."
$action = Read-Host "Please check from options listed above"

if ($action = "1") {
    Write-Host "You picked files larger that 1GB"
}
elseif ($action = "2") {
    Write-Host " You picked files less than 1 GB"

}
elseif ($action = "3") {
    Write-Host "You picked files by certain type"

}
elseif ($action = "4") {
    Write-Host "You Picked files that start with a certain letter"

}
elseif ($action = "5") {
    Write-Host "You picked files by date"

}
else {
    Write-Host "Invalid Choice"
}


function FileOrganizer{
    param( 
        $Directory
    )
    Write-Host "You selected", $Directory
 Get-ChildItem $Directory   
}

FileOrganizer($Directory)



