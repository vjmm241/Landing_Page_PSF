# Deploy Edge Functions
Write-Host "Deploying Supabase Edge Functions..." -ForegroundColor Cyan

# Check if user is logged in
$status = npx supabase status
if ($LASTEXITCODE -ne 0) {
    Write-Host "Please login to Supabase first using 'npx supabase login'" -ForegroundColor Yellow
}

# 1. Deploy Process PDF
Write-Host "Deploying process_pdf..." -ForegroundColor Green
npx supabase functions deploy process_pdf --no-verify-jwt

# 2. Deploy Chat
Write-Host "Deploying chat..." -ForegroundColor Green
npx supabase functions deploy chat --no-verify-jwt

Write-Host "Deployment Complete!" -ForegroundColor Cyan
Write-Host "Make sure to set your Secrets in the Dashboard or via 'npx supabase secrets set'!" -ForegroundColor Yellow
