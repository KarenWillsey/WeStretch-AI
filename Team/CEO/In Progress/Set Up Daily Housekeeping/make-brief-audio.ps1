<#
  make-brief-audio.ps1
  Renders the daily brief audio script to a WAV using the Windows built-in
  voice (System.Speech / SAPI). No API key, no network, no cost.

  Called by the daily-brief-compose skill. Writes the file into the local
  OneDrive folder so it syncs to Karen's phone on its own; the Outlook MCP
  tool cannot attach files to an email, which is why delivery is a synced
  file rather than an attachment.

  Usage:
    powershell -ExecutionPolicy Bypass -File make-brief-audio.ps1 `
      -ScriptFile "state\2026-09-12-audio-script.txt"

  Exits 0 on success and prints the full output path as the last line.
  Exits 1 on any failure; the caller must treat that as a fail-loud gap,
  not a silent skip.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ScriptFile,

    # Override the output path. Default: OneDrive\Daily Brief\<date>-brief.wav
    [string]$OutFile,

    # Zira (female) or "Microsoft David Desktop" (male). Both ship with Windows.
    [string]$VoiceName = 'Microsoft Zira Desktop',

    # Playback speed as a multiple of normal speaking pace. Karen listens at
    # 1.8x, which is why that is the default. Started at 1.6 on 2026-09-12 and
    # she asked for faster the same day. Mapped to a SAPI rate below.
    [double]$Speed = 1.8,

    # Raw SAPI rate (-10 slowest .. 10 fastest). Overrides -Speed when given.
    # Prefer -Speed; this exists for fine tuning outside the calibrated table.
    [Nullable[int]]$Rate = $null
)

$ErrorActionPreference = 'Stop'

try {
    if (-not (Test-Path -LiteralPath $ScriptFile)) {
        throw "Audio script file not found: $ScriptFile"
    }

    $text = Get-Content -LiteralPath $ScriptFile -Raw
    if ([string]::IsNullOrWhiteSpace($text)) {
        throw "Audio script file is empty: $ScriptFile"
    }

    if (-not $OutFile) {
        $OutFile = Join-Path (Join-Path $env:USERPROFILE 'OneDrive\Daily Brief') `
                             ((Get-Date -Format 'yyyy-MM-dd') + '-brief.wav')
    }

    # Create the parent directory for whatever path we ended up with. This must
    # run for a caller-supplied -OutFile too, not just the default: SAPI's
    # SetOutputToWaveFile does not create directories and throws a bare
    # "Could not find a part of the path" that reads like a missing input file.
    $outDir = Split-Path -Parent $OutFile
    if ($outDir -and -not (Test-Path -LiteralPath $outDir)) {
        New-Item -ItemType Directory -Path $outDir -Force | Out-Null
    }

    Add-Type -AssemblyName System.Speech

    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

    # Fall back to whatever voice exists rather than failing the whole brief
    # over a voice name. A robotic brief beats no brief.
    $installed = $synth.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo.Name }
    if ($installed -notcontains $VoiceName) {
        if ($installed.Count -eq 0) { throw 'No SAPI voices are installed on this machine.' }
        Write-Warning "Voice '$VoiceName' not installed; using '$($installed[0])'."
        $VoiceName = $installed[0]
    }
    $synth.SelectVoice($VoiceName)

    # SAPI's Rate is not a speed multiple and is not linear, so guessing a
    # number gets the pace wrong. This table was measured on this machine on
    # 2026-09-12: same script, Zira, rendered at each rate, duration taken from
    # the WAV byte count. Re-measure if the voice changes; the mapping is
    # voice-specific. Re-confirmed the same day against the real 2026-09-12
    # brief script, a longer text: rate 4 gave 80.3s and rate 5 gave 72.0s, a
    # 1.12x step that matches the table below.
    #   Rate 0 = 1.00x   Rate 1 = 1.15x   Rate 2 = 1.28x   Rate 3 = 1.44x
    #   Rate 4 = 1.61x   Rate 5 = 1.79x   Rate 6 = 1.98x   Rate 7 = 2.18x
    $speedTable = [ordered]@{
        0 = 1.00; 1 = 1.15; 2 = 1.28; 3 = 1.44
        4 = 1.61; 5 = 1.79; 6 = 1.98; 7 = 2.18
    }

    if ($null -ne $Rate) {
        $effectiveRate = $Rate
    }
    else {
        # Nearest calibrated rate to the requested speed.
        $effectiveRate = ($speedTable.Keys | Sort-Object { [math]::Abs($speedTable[$_] - $Speed) })[0]
        Write-Verbose ("Speed {0}x -> SAPI rate {1} ({2}x measured)" -f $Speed, $effectiveRate, $speedTable[$effectiveRate])
    }
    $synth.Rate = $effectiveRate

    # 16 kHz mono keeps a ~90 second brief near 2 MB so OneDrive syncs it fast.
    $fmt = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(
        16000,
        [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen,
        [System.Speech.AudioFormat.AudioChannel]::Mono)

    $synth.SetOutputToWaveFile($OutFile, $fmt)
    $synth.Speak($text)
    $synth.SetOutputToNull()
    $synth.Dispose()

    if (-not (Test-Path -LiteralPath $OutFile)) {
        throw "Synthesis reported success but no file exists at $OutFile"
    }
    $size = (Get-Item -LiteralPath $OutFile).Length
    if ($size -lt 10000) {
        throw "Output file is only $size bytes; synthesis probably produced silence."
    }

    # Second copy on the Desktop for one-click play at the laptop. Resolve the
    # real Desktop via the shell folder: Karen's is redirected into OneDrive, so
    # a hardcoded $env:USERPROFILE\Desktop path does not exist. Never let this
    # convenience copy fail the run; the OneDrive file is the real delivery.
    try {
        $desktopDir = [Environment]::GetFolderPath('Desktop')
        if ($desktopDir -and (Test-Path -LiteralPath $desktopDir)) {
            Copy-Item -LiteralPath $OutFile `
                      -Destination (Join-Path $desktopDir 'Daily Brief.wav') -Force
        }
    } catch {
        Write-Warning "Desktop copy skipped: $($_.Exception.Message)"
    }

    Write-Output $OutFile
    exit 0
}
catch {
    Write-Error "make-brief-audio.ps1 failed: $($_.Exception.Message)"
    exit 1
}
