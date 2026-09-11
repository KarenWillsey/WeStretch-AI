# Runs the daily-brief skill unattended via the local Claude Code CLI.
# Invoked by a Windows Scheduled Task at 5:00 AM daily (America/Edmonton).
#
# Fails loud. A run that dies, hangs, or exits non-zero must not leave Karen with
# a silently missing brief, which is what happened Sep 2 to Sep 5 2026 when the
# OAuth session expired. On any failure this writes a marker file to her Desktop
# and to state/, and clears them again on the next clean run.
$ErrorActionPreference = "Stop"
$repoRoot = "C:\Users\karen\Documents\WeStretch AI\WeStretch-AI"
$stateDir = Join-Path $repoRoot "Team\CEO\In Progress\Set Up Daily Housekeeping\state"
$logFile = Join-Path $stateDir "last-run.log"
$failFlag = Join-Path $stateDir "RUN-FAILED.txt"
$desktopFlag = Join-Path ([Environment]::GetFolderPath("Desktop")) "DAILY-BRIEF-FAILED.txt"

# Kill the run if it hangs. Today's healthy runs land around 10 to 15 minutes.
$timeoutMinutes = 60

function Write-Log($message) {
    "[$(Get-Date -Format o)] $message" | Out-File -FilePath $logFile -Append -Encoding utf8
}

function Raise-Alert($reason) {
    Write-Log "ALERT: $reason"
    $text = @"
The WeStretch daily brief did NOT complete.

When:   $(Get-Date -Format 'yyyy-MM-dd HH:mm')
Reason: $reason

There is no brief in your inbox for this morning.
Full detail: $logFile

This file deletes itself the next time the brief runs clean.
"@
    foreach ($path in @($failFlag, $desktopFlag)) {
        try { $text | Out-File -FilePath $path -Encoding utf8 } catch { }
    }
    # Best effort desktop notification. Silently skipped when the task runs
    # without an interactive session, which is why the marker files exist.
    try {
        Add-Type -AssemblyName System.Windows.Forms
        $n = New-Object System.Windows.Forms.NotifyIcon
        $n.Icon = [System.Drawing.SystemIcons]::Warning
        $n.Visible = $true
        $n.ShowBalloonTip(20000, "Daily brief failed", $reason, [System.Windows.Forms.ToolTipIcon]::Error)
        Start-Sleep -Seconds 12
        $n.Dispose()
    } catch { }
}

function Clear-Alert {
    foreach ($path in @($failFlag, $desktopFlag)) {
        if (Test-Path $path) { Remove-Item $path -Force -ErrorAction SilentlyContinue }
    }
}

# A previous run that logged "Starting" but never logged a finish line died
# without saying so. Surface it now rather than letting it stay invisible.
if (Test-Path $logFile) {
    $lines = Get-Content $logFile -ErrorAction SilentlyContinue
    $lastStart = ($lines | Select-String -SimpleMatch "Starting scheduled daily-brief run" | Select-Object -Last 1)
    $lastFinish = ($lines | Select-String -SimpleMatch "Run finished with exit code" | Select-Object -Last 1)
    if ($lastStart -and (-not $lastFinish -or $lastFinish.LineNumber -lt $lastStart.LineNumber)) {
        Raise-Alert "The previous run started but never logged a finish line, so it died or was killed mid-run."
    }
}

# Resolve the currently installed Claude Code VS Code extension's bundled CLI.
# Not hardcoded to a version, since the extension auto-updates and the folder name changes with it.
$extDir = Get-ChildItem -Path "$env:USERPROFILE\.vscode\extensions" -Filter "anthropic.claude-code-*" -Directory -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1

if (-not $extDir) {
    Write-Log "FAILED: Claude Code VS Code extension not found under $env:USERPROFILE\.vscode\extensions"
    Raise-Alert "Claude Code VS Code extension not found, so the brief could not be launched."
    exit 1
}

$claudeExe = Join-Path $extDir.FullName "resources\native-binary\claude.exe"
if (-not (Test-Path $claudeExe)) {
    Write-Log "FAILED: claude.exe not found at $claudeExe"
    Raise-Alert "claude.exe not found at the expected path, so the brief could not be launched."
    exit 1
}

Set-Location $repoRoot
Write-Log "Starting scheduled daily-brief run via $claudeExe"

# Run detached so the timeout can be enforced. Start-Process cannot append, so
# capture to a temp file outside the repo and fold it into the log afterwards.
$tempOut = Join-Path $env:TEMP "daily-brief-stdout-$([guid]::NewGuid()).txt"
$tempErr = Join-Path $env:TEMP "daily-brief-stderr-$([guid]::NewGuid()).txt"
$prompt = "Run the daily-brief skill end to end now (.claude/skills/daily-brief/SKILL.md) -- this is the scheduled unattended morning run."

$proc = Start-Process -FilePath $claudeExe `
    -ArgumentList @("--print", "--dangerously-skip-permissions", $prompt) `
    -WorkingDirectory $repoRoot `
    -RedirectStandardOutput $tempOut `
    -RedirectStandardError $tempErr `
    -NoNewWindow -PassThru

$timedOut = $false
if (-not $proc.WaitForExit($timeoutMinutes * 60 * 1000)) {
    $timedOut = $true
    try { $proc.Kill() } catch { }
    try { $proc.WaitForExit(30000) | Out-Null } catch { }
}

foreach ($f in @($tempOut, $tempErr)) {
    if (Test-Path $f) {
        Get-Content $f -Raw -ErrorAction SilentlyContinue | Out-File -FilePath $logFile -Append -Encoding utf8
        Remove-Item $f -Force -ErrorAction SilentlyContinue
    }
}

$exitCode = if ($timedOut) { 124 } else { $proc.ExitCode }
Write-Log "Run finished with exit code $exitCode"

if ($timedOut) {
    Raise-Alert "The run passed $timeoutMinutes minutes and was killed. No brief was sent."
    exit 124
}
if ($exitCode -ne 0) {
    Raise-Alert "The run exited with code $exitCode. Check the log for an auth or connector failure."
    exit $exitCode
}

Clear-Alert
exit 0
