param (
    [string]$client_id,
    [string]$client_secret,
    [string]$filePath,
    [string]$testId,
    [string]$testExecId
)
Write-Output "Testplan id: $testId"
Write-Output "Test exec id: $testExecId"
Write-Output "Received client_id: $client_id"
Write-Output "Received client_secret: $client_secret"
Write-Output "Received filePath: $filePath"

# Authentication request
$uri = "https://xray.cloud.getxray.app/api/v1/authenticate"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "client_id" = $client_id
    "client_secret" = $client_secret
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ErrorAction Stop
    

    # API request with token
    Invoke-RestMethod -Uri "https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey=$testId" -Method Post -Headers @{
        "Authorization" = "Bearer $response"
        "Content-Type" = "application/xml"
    } -InFile $filePath

} catch {
    Write-Error $_.Exception.Message
    exit 1
}
