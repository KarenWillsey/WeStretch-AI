Add-Type -AssemblyName System.Drawing

$roundDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourcePath = Join-Path (Split-Path -Parent $roundDirectory) 'Round 03/07-calm-routine-no-upper-gradient.png'

function New-MockupCanvas {
    $source = [System.Drawing.Image]::FromFile($sourcePath)
    $bitmap = [System.Drawing.Bitmap]::new($source.Width, $source.Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.DrawImageUnscaled($source, 0, 0)
    $source.Dispose()
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

    # Cover only the original counter text. Preserve the grey ring and red progress arc.
    $background = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(255, 54, 49, 44))
    $graphics.FillEllipse($background, 66, 93, 102, 102)
    $background.Dispose()

    return @($bitmap, $graphics)
}

function Draw-CentredText($graphics, [string]$text, $font, $brush, [float]$centreX, [float]$topY) {
    $format = [System.Drawing.StringFormat]::new()
    $format.Alignment = [System.Drawing.StringAlignment]::Center
    $format.LineAlignment = [System.Drawing.StringAlignment]::Near
    $format.FormatFlags = [System.Drawing.StringFormatFlags]::NoWrap
    $graphics.DrawString($text, $font, $brush, $centreX, $topY, $format)
    $format.Dispose()
}

$white = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
$softWhite = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(235, 255, 255, 255))
$dividerPen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(225, 255, 255, 255), 3)
$dividerPen.StartCap = [System.Drawing.Drawing2D.LineCap]::Round
$dividerPen.EndCap = [System.Drawing.Drawing2D.LineCap]::Round
$largeFont = [System.Drawing.Font]::new('Segoe UI Semibold', 34, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
$mediumFont = [System.Drawing.Font]::new('Segoe UI Semibold', 31, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)

# Option 1: diagonal fraction, closest to the handwritten reference.
$canvas = New-MockupCanvas
$bitmap = $canvas[0]
$graphics = $canvas[1]
Draw-CentredText $graphics '12' $largeFont $white 95 101
Draw-CentredText $graphics '66' $largeFont $white 139 150
$graphics.DrawLine($dividerPen, 86, 160, 149, 121)
$graphics.Dispose()
$bitmap.Save((Join-Path $roundDirectory '01-diagonal-fraction.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$bitmap.Dispose()

# Option 2: centred fraction with a short horizontal divider.
$canvas = New-MockupCanvas
$bitmap = $canvas[0]
$graphics = $canvas[1]
Draw-CentredText $graphics '12' $largeFont $white 117 96
Draw-CentredText $graphics '66' $largeFont $white 117 149
$graphics.DrawLine($dividerPen, 87, 144, 147, 144)
$graphics.Dispose()
$bitmap.Save((Join-Path $roundDirectory '02-horizontal-divider.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$bitmap.Dispose()

# Option 3: offset stack, separated by space rather than a line.
$canvas = New-MockupCanvas
$bitmap = $canvas[0]
$graphics = $canvas[1]
Draw-CentredText $graphics '12' $largeFont $white 99 101
Draw-CentredText $graphics '66' $mediumFont $softWhite 136 151
$graphics.Dispose()
$bitmap.Save((Join-Path $roundDirectory '03-offset-no-divider.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$bitmap.Dispose()

$largeFont.Dispose()
$mediumFont.Dispose()
$dividerPen.Dispose()
$white.Dispose()
$softWhite.Dispose()
