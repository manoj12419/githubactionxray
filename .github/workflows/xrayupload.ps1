param (
    [string]$client_id,
    [string]$client_secret,
    [string]$filePath
)

# Authentication request
$uri = "https://xray.cloud.getxray.app/api/v1/authenticate"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "client_id" = $client_id
    "client_secret" = $client_secret
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body

# Extract the token from the response
$token = $response.token

# API request with token
Invoke-RestMethod -Uri "https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey=YAK-4" -Method Post -Headers @{
    "Authorization" = "Bearer $token"
    "Content-Type" = "application/xml"
} -InFile $filePath