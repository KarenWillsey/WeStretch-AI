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
# The prompt MUST be passed as one quoted argument. Start-Process joins the
# ArgumentList with spaces and quotes nothing, so an unquoted prompt is split on
# every space and claude.exe receives only the first word. That is what broke
# the 2026-09-12 run: the agent got the bare word "Run" and asked what to run
# instead of running the brief. The prompt also must not contain "--", which
# terminates option parsing.
$prompt = "Run the daily-brief skill end to end now, following .claude/skills/daily-brief/SKILL.md in full. This is the scheduled unattended morning run and you are that run, so do not check whether a brief is already running and do not ask any clarifying questions; there is nobody awake to answer them."
$quotedPrompt = '"' + $prompt.Replace('"', '\"') + '"'

$proc = Start-Process -FilePath $claudeExe `
    -ArgumentList @("--print", "--dangerously-skip-permissions", $quotedPrompt) `
    -WorkingDirectory $repoRoot `
    -RedirectStandardOutput $tempOut `
    -RedirectStandardError $tempErr `
    -NoNewWindow -PassThru

# Touch .Handle immediately. Without this, .NET drops the process handle when the
# child exits and .ExitCode comes back EMPTY even on a clean run. That is why the
# 2026-09-12 alert read "exited with code ." with no number. Verified 2026-09-12:
# same launch without this line returns [], with it returns [0].
try { $null = $proc.Handle } catch { }

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

# Refresh first: without it ExitCode can come back empty on an already-exited
# process, which produced the useless "exited with code ." alert on 2026-09-12.
# Treat an unreadable exit code as a failure (125), never as success.
if (-not $timedOut) { try { $proc.Refresh() } catch { } }
$exitCode = if ($timedOut) {
    124
} elseif ($null -eq $proc.ExitCode -or "$($proc.ExitCode)" -eq "") {
    Write-Log "Exit code could not be read from the process; treating as a failure."
    125
} else {
    $proc.ExitCode
}
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
