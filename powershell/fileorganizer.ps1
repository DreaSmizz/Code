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


# Parameters for the script
param (
    [string]$SourceDirectory = "/Users/andreasmith/PycharmProjects/Code",
    [string]$OrganizeBy = "Type", # Options: Type, Date
    [string]$DateFormat = "yyyy-MM-dd" # Only used if organizing by Date
)

# Check if the source directory exists
if (-Not (Test-Path -Path $SourceDirectory)) {
    Write-Output "The specified source directory does not exist."
    exit
}

# Function to organize files by type
function Organize-ByType {
    param ($SourceDirectory)

    # Get all files in the source directory
    $files = Get-ChildItem -Path $SourceDirectory -File

    foreach ($file in $files) {
        $extension = $file.Extension.TrimStart('.')
        if (-Not $extension) {
            $extension = "NoExtension"
        }
        $destination = Join-Path -Path $SourceDirectory -ChildPath $extension

        # Create the directory if it doesn't exist
        if (-Not (Test-Path -Path $destination)) {
            New-Item -Path $destination -ItemType Directory
        }

        # Move the file to the destination directory
        Move-Item -Path $file.FullName -Destination $destination
    }
}

# Function to organize files by date
function Organize-ByDate {
    param ($SourceDirectory, $DateFormat)

    # Get all files in the source directory
    $files = Get-ChildItem -Path $SourceDirectory -File

    foreach ($file in $files) {
        $date = $file.CreationTime.ToString($DateFormat)
        $destination = Join-Path -Path $SourceDirectory -ChildPath $date

        # Create the directory if it doesn't exist
        if (-Not (Test-Path -Path $destination)) {
            New-Item -Path $destination -ItemType Directory
        }

        # Move the file to the destination directory
        Move-Item -Path $file.FullName -Destination $destination
    }
}

# Main logic
switch ($OrganizeBy) {
    "Type" {
        Organize-ByType -SourceDirectory $SourceDirectory
    }
    "Date" {
        Organize-ByDate -SourceDirectory $SourceDirectory -DateFormat $DateFormat
    }
    default {
        Write-Output "Invalid option for OrganizeBy. Use 'Type' or 'Date'."
    }
}

Write-Output "Files have been organized."



