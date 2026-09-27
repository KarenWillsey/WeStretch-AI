Add-Type -AssemblyName System.Drawing

$outputDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path

function New-Canvas([int]$size) {
    $bitmap = [System.Drawing.Bitmap]::new($size, $size, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $bitmap.SetResolution(144, 144)
    return $bitmap
}

function Save-Png($bitmap, [string]$name) {
    $path = Join-Path $outputDirectory $name
    $bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $bitmap.Dispose()
}

function Fill-RoundedRectangle($graphics, $brush, [int]$x, [int]$y, [int]$width, [int]$height, [int]$radius) {
    $diameter = $radius * 2
    $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $path.AddArc($x, $y, $diameter, $diameter, 180, 90)
    $path.AddArc($x + $width - $diameter, $y, $diameter, $diameter, 270, 90)
    $path.AddArc($x + $width - $diameter, $y + $height - $diameter, $diameter, $diameter, 0, 90)
    $path.AddArc($x, $y + $height - $diameter, $diameter, $diameter, 90, 90)
    $path.CloseFigure()
    $graphics.FillPath($brush, $path)
    $path.Dispose()
}

function Draw-Ring([string]$name, [int]$outerDiameter, [int]$innerDiameter, [System.Drawing.Color]$color, [System.Drawing.Color]$edgeColor) {
    $size = 512
    $bitmap = New-Canvas $size
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.Clear([System.Drawing.Color]::Transparent)

    if ($edgeColor.A -gt 0) {
        $edgeInset = [int](($size - $outerDiameter) / 2) - 2
        $edgeBrush = [System.Drawing.SolidBrush]::new($edgeColor)
        $graphics.FillEllipse($edgeBrush, $edgeInset, $edgeInset, $outerDiameter + 4, $outerDiameter + 4)
        $edgeBrush.Dispose()
    }

    $outerInset = [int](($size - $outerDiameter) / 2)
    $ringBrush = [System.Drawing.SolidBrush]::new($color)
    $graphics.FillEllipse($ringBrush, $outerInset, $outerInset, $outerDiameter, $outerDiameter)
    $ringBrush.Dispose()

    $innerInset = [int](($size - $innerDiameter) / 2)
    $graphics.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceCopy
    $clearBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::Transparent)
    $graphics.FillEllipse($clearBrush, $innerInset, $innerInset, $innerDiameter, $innerDiameter)
    $clearBrush.Dispose()
    $graphics.Dispose()
    Save-Png $bitmap $name
}

Draw-Ring 'countdown-ring.png' 472 392 ([System.Drawing.Color]::FromArgb(220, 121, 121, 121)) ([System.Drawing.Color]::FromArgb(190, 53, 53, 53))
Draw-Ring 'progress-track-ring.png' 442 386 ([System.Drawing.Color]::FromArgb(205, 165, 165, 165)) ([System.Drawing.Color]::Transparent)
Draw-Ring 'progress-fill-ring.png' 442 386 ([System.Drawing.Color]::FromArgb(255, 252, 72, 80)) ([System.Drawing.Color]::Transparent)

$background = New-Canvas 512
$backgroundGraphics = [System.Drawing.Graphics]::FromImage($background)
$backgroundGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$backgroundGraphics.Clear([System.Drawing.Color]::Transparent)
$backgroundBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(220, 31, 31, 31))
$backgroundGraphics.FillEllipse($backgroundBrush, 60, 60, 392, 392)
$backgroundBrush.Dispose()
$backgroundGraphics.Dispose()
Save-Png $background 'counter-background.png'

$pause = New-Canvas 256
$pauseGraphics = [System.Drawing.Graphics]::FromImage($pause)
$pauseGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$pauseGraphics.Clear([System.Drawing.Color]::Transparent)
$pauseBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
Fill-RoundedRectangle $pauseGraphics $pauseBrush 68 48 38 160 19
Fill-RoundedRectangle $pauseGraphics $pauseBrush 150 48 38 160 19
$pauseBrush.Dispose()
$pauseGraphics.Dispose()
Save-Png $pause 'pause-icon.png'

$play = New-Canvas 256
$playGraphics = [System.Drawing.Graphics]::FromImage($play)
$playGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$playGraphics.Clear([System.Drawing.Color]::Transparent)
$playBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
$playPath = [System.Drawing.Drawing2D.GraphicsPath]::new()
$playPoints = [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(76, 48),
    [System.Drawing.Point]::new(200, 128),
    [System.Drawing.Point]::new(76, 208)
)
$playPath.AddPolygon($playPoints)
$playGraphics.FillPath($playBrush, $playPath)
$playPath.Dispose()
$playBrush.Dispose()
$playGraphics.Dispose()
Save-Png $play 'play-icon.png'

$cap = New-Canvas 64
$capGraphics = [System.Drawing.Graphics]::FromImage($cap)
$capGraphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$capGraphics.Clear([System.Drawing.Color]::Transparent)
$capBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(255, 252, 72, 80))
$capGraphics.FillEllipse($capBrush, 0, 0, 64, 64)
$capBrush.Dispose()
$capGraphics.Dispose()
Save-Png $cap 'progress-round-cap.png'
