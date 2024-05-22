$PI = 3.14
Write-Host "The value of `$PI is $PI"
Write-Host "Here is `$PI and its value is $PI"
Write-Host "An expression $($PI + 1)"
Write-Host "The value of `$PI is now $PI, inside the script."

$test = 'hi'
Write-Host $test

# Sets Parameters - Param()
$Value = 3
If ($Value -le 0)
{
    Write-Host "Is negative"
} Else {
    Write-Host "Is positive"
}