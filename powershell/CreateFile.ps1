# #CreateFile.ps1
# Param (
#     $Path
# )
# If (-Not $Path  -eq '') {
# New-Item $Path # Creates a new file at $Path.
# Write-Host "File created at path $Path"
# } Else {
#     Write-Error "Path cannont be empty"
# }

# Better way and requires less typing
Param (
    [Parameter(Mandatory, HelpMessage = "Please provide a valid path")]
    $Path
)
New-Item $Path
Write-Host "File created at path $Path"