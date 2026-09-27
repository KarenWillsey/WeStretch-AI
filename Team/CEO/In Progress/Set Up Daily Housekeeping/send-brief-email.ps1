<#
  send-brief-email.ps1
  Sends the daily brief through the local Outlook desktop client via COM, so
  the audio WAV can ride along as a real attachment.

  Why this exists: the Microsoft 365 MCP connector cannot attach files at all
  (outlook_send_mail has no attachment parameter, and outlook_send_draft
  explicitly rejects drafts that have attachments). Karen listens to the brief
  on her phone, and a OneDrive path in the footer is not the same as an audio
  file she can tap in Mail. Outlook COM is the only path on this machine that
  puts a real attachment in a real message.

  Exit codes:
    0   sent, and confirmed present in Sent Items
    2   Outlook COM unavailable (not installed, not signed in, blocked)
    3   send attempted but could not be confirmed in Sent Items
    1   anything else

  A non-zero exit is a fail-loud signal to the caller: fall back to the MCP
  send (no attachment) and say in the brief that the audio is a path only.

  Usage:
    powershell -ExecutionPolicy Bypass -File send-brief-email.ps1 `
      -Subject "6 to decide, 1 to reply - Sat Sep 12" `
      -BodyHtmlFile "state\2026-09-12-body.html" `
      -AttachmentPath "C:\Users\karen\OneDrive\Daily Brief\2026-09-12-brief.wav" `
      -To "karen@kasa.ca"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)] [string]$Subject,

    # File holding the HTML body. Passed as a file, never as a string argument:
    # a long body on the command line hits the same space-splitting and quoting
    # traps that broke run-daily-brief.ps1 on 2026-09-12.
    [Parameter(Mandatory = $true)] [string]$BodyHtmlFile,

    [string]$AttachmentPath,

    [string]$To = 'karen@kasa.ca',

    # Seconds to wait for the message to appear in Sent Items before giving up.
    [int]$ConfirmTimeoutSeconds = 60
)

$ErrorActionPreference = 'Stop'
$olMailItem   = 0
$olFolderSent = 5

function Fail($code, $message) {
    # Write straight to stderr rather than Write-Error: with
    # $ErrorActionPreference = 'Stop', Write-Error throws, which a surrounding
    # catch would swallow and turn every specific exit code back into 1.
    [Console]::Error.WriteLine("send-brief-email.ps1: $message")
    exit $code
}

if (-not (Test-Path -LiteralPath $BodyHtmlFile)) {
    Fail 1 "Body file not found: $BodyHtmlFile"
}
$body = Get-Content -LiteralPath $BodyHtmlFile -Raw
if ([string]::IsNullOrWhiteSpace($body)) {
    Fail 1 "Body file is empty: $BodyHtmlFile"
}

if ($AttachmentPath) {
    if (-not (Test-Path -LiteralPath $AttachmentPath)) {
        Fail 1 "Attachment not found: $AttachmentPath"
    }
    # Outlook.Attachments.Add needs a full path; a relative one silently
    # resolves against Outlook's working directory, not ours.
    $AttachmentPath = (Resolve-Path -LiteralPath $AttachmentPath).Path

    $mb = (Get-Item -LiteralPath $AttachmentPath).Length / 1MB
    if ($mb -gt 20) {
        Fail 1 ("Attachment is {0:N1} MB, over the 20 MB ceiling." -f $mb)
    }
}

try {
    $outlook = New-Object -ComObject Outlook.Application
}
catch {
    Fail 2 "Could not create the Outlook COM object: $($_.Exception.Message)"
}

try {
    $ns = $outlook.GetNamespace('MAPI')

    $mail = $outlook.CreateItem($olMailItem)
    $mail.To       = $To
    $mail.Subject  = $Subject
    # HTMLBody takes raw markup. Do not HTML-escape the body before writing the
    # file; the same escaped-tags bug that hit the MCP path applies here.
    $mail.HTMLBody = $body

    if ($AttachmentPath) {
        $null = $mail.Attachments.Add($AttachmentPath)
    }

    $mail.Send()
}
catch {
    Fail 1 "Send failed: $($_.Exception.Message)"
}

# Confirm it actually left, rather than trusting Send() returning quietly.
# Outlook queues the message, so poll Sent Items rather than checking once.
try {
    $sent = $ns.GetDefaultFolder($olFolderSent)
    $deadline = (Get-Date).AddSeconds($ConfirmTimeoutSeconds)
    $found = $null

    while ((Get-Date) -lt $deadline -and -not $found) {
        $items = $sent.Items
        $items.Sort('[SentOn]', $true)
        # Take the newest few rather than filtering: subjects contain commas and
        # dashes that Outlook's Restrict syntax handles badly.
        for ($i = 1; $i -le [Math]::Min(10, $items.Count); $i++) {
            if ($items.Item($i).Subject -eq $Subject) { $found = $items.Item($i); break }
        }
        if (-not $found) { Start-Sleep -Seconds 3 }
    }

    if (-not $found) {
        Fail 3 "Sent, but did not appear in Sent Items within $ConfirmTimeoutSeconds seconds. Check Outlook's Outbox."
    }

    $attachCount = $found.Attachments.Count
    if ($AttachmentPath -and $attachCount -lt 1) {
        Fail 3 'Message is in Sent Items but carries no attachment.'
    }

    Write-Output "SENT: $Subject"
    Write-Output "ATTACHMENTS: $attachCount"
    exit 0
}
catch {
    Fail 3 "Sent, but confirmation failed: $($_.Exception.Message)"
}
