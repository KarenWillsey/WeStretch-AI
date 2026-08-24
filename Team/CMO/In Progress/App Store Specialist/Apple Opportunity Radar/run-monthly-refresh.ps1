# Runs the app-store-specialist-monthly-refresh skill unattended via the local Claude Code CLI.
# Invoked by a Windows Scheduled Task on the 1st of each month.
$ErrorActionPreference = "Stop"
$repoRoot = "C:\Users\karen\Documents\WeStretch AI\WeStretch-AI"
$logFile = Join-Path $repoRoot "Team\CMO\In Progress\App Store Specialist\Apple Opportunity Radar\state\last-run.log"

# Resolve the currently installed Claude Code VS Code extension's bundled CLI.
# Not hardcoded to a version, since the extension auto-updates and the folder name changes with it.
$extDir = Get-ChildItem -Path "$env:USERPROFILE\.vscode\extensions" -Filter "anthropic.claude-code-*" -Directory -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1

if (-not $extDir) {
    "[monthly-refresh] [$(Get-Date -Format o)] FAILED: Claude Code VS Code extension not found under $env:USERPROFILE\.vscode\extensions" | Out-File -FilePath $logFile -Append -Encoding utf8
    exit 1
}

$claudeExe = Join-Path $extDir.FullName "resources\native-binary\claude.exe"
if (-not (Test-Path $claudeExe)) {
    "[monthly-refresh] [$(Get-Date -Format o)] FAILED: claude.exe not found at $claudeExe" | Out-File -FilePath $logFile -Append -Encoding utf8
    exit 1
}

Set-Location $repoRoot
"[monthly-refresh] [$(Get-Date -Format o)] Starting scheduled monthly-refresh run via $claudeExe" | Out-File -FilePath $logFile -Append -Encoding utf8

& $claudeExe --print --dangerously-skip-permissions "Run the app-store-specialist-monthly-refresh skill now (.claude/skills/app-store-specialist-monthly-refresh/SKILL.md) -- this is the scheduled unattended monthly run." *>> $logFile

"[monthly-refresh] [$(Get-Date -Format o)] Run finished with exit code $LASTEXITCODE" | Out-File -FilePath $logFile -Append -Encoding utf8
