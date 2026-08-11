[CmdletBinding()]
param(
    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$RootPath,

    [Parameter()]
    [ValidateRange(72, 1200)]
    [int]$Dpi = 300
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$sourceFolderNames = @('logo', 'Regulatory', 'seal', 'Thankyou')
$millimetrePattern = '^\s*(\d+(?:\.\d+)?)\s*mm\s*$'

if ([string]::IsNullOrWhiteSpace($RootPath)) {
    if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) {
        $RootPath = $PSScriptRoot
    }
    elseif (-not [string]::IsNullOrWhiteSpace($MyInvocation.MyCommand.Path)) {
        $RootPath = Split-Path -Parent $MyInvocation.MyCommand.Path
    }
    else {
        $RootPath = (Get-Location).Path
    }
}

function Get-ImageMagickPath {
    $command = Get-Command magick -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1

    if (-not $command) {
        throw "ImageMagick 7 was not found. Install it and ensure 'magick.exe' is available in PATH."
    }

    return $command.Source
}

function Get-ExpectedPixelSize {
    param(
        [Parameter(Mandatory)]
        [string]$SvgPath,

        [Parameter(Mandatory)]
        [int]$RenderDpi
    )

    [xml]$document = Get-Content -LiteralPath $SvgPath -Raw
    $root = $document.DocumentElement
    $width = $root.GetAttribute('width')
    $height = $root.GetAttribute('height')

    if ($width -notmatch $millimetrePattern -or $height -notmatch $millimetrePattern) {
        throw "SVG width and height must be declared in millimetres: $SvgPath"
    }

    $widthMm = [double]::Parse(
        ([regex]::Match($width, $millimetrePattern)).Groups[1].Value,
        [Globalization.CultureInfo]::InvariantCulture
    )
    $heightMm = [double]::Parse(
        ([regex]::Match($height, $millimetrePattern)).Groups[1].Value,
        [Globalization.CultureInfo]::InvariantCulture
    )

    return [pscustomobject]@{
        Width = [Math]::Round($widthMm / 25.4 * $RenderDpi)
        Height = [Math]::Round($heightMm / 25.4 * $RenderDpi)
    }
}

function Get-PngProperties {
    param(
        [Parameter(Mandatory)]
        [string]$ImageMagickPath,

        [Parameter(Mandatory)]
        [string]$PngPath
    )

    $result = & $ImageMagickPath identify -quiet -format '%w|%h|%x|%y|%[units]' $PngPath
    $parts = $result -split '\|'
    if ($LASTEXITCODE -ne 0 -or $parts.Count -ne 5) {
        throw "ImageMagick could not validate: $PngPath"
    }

    $culture = [Globalization.CultureInfo]::InvariantCulture
    $resolutionX = [double]::Parse($parts[2], $culture)
    $resolutionY = [double]::Parse($parts[3], $culture)
    switch ($parts[4]) {
        'PixelsPerInch' {
            $dpiX = $resolutionX
            $dpiY = $resolutionY
        }
        'PixelsPerCentimeter' {
            $dpiX = $resolutionX * 2.54
            $dpiY = $resolutionY * 2.54
        }
        default {
            throw "PNG resolution units are missing or unsupported for: $PngPath"
        }
    }

    return [pscustomobject]@{
        Width = [int]$parts[0]
        Height = [int]$parts[1]
        DpiX = $dpiX
        DpiY = $dpiY
    }
}

$root = (Resolve-Path -LiteralPath $RootPath).Path
$magick = Get-ImageMagickPath

Write-Host "ImageMagick: $magick"
Write-Host "Source root: $root"
Write-Host "Resolution: $Dpi DPI"

$missingFolders = @(
    foreach ($folderName in $sourceFolderNames) {
        $sourceFolder = Join-Path $root $folderName
        if (-not (Test-Path -LiteralPath $sourceFolder -PathType Container)) {
            $folderName
        }
    }
)

if ($missingFolders.Count -gt 0) {
    throw "Missing source folder(s) beside the script: $($missingFolders -join ', ')"
}

$converted = 0

foreach ($folderName in $sourceFolderNames) {
    $sourceFolder = (Resolve-Path -LiteralPath (Join-Path $root $folderName)).Path
    $outputFolder = Join-Path $root "$folderName-png"
    $svgFiles = @(Get-ChildItem -LiteralPath $sourceFolder -Filter '*.svg' -File -Recurse | Sort-Object FullName)

    if ($svgFiles.Count -eq 0) {
        Write-Warning "No SVG files found in: $sourceFolder"
        continue
    }

    foreach ($svg in $svgFiles) {
        $relativePath = $svg.FullName.Substring($sourceFolder.Length).TrimStart('\', '/')
        $relativeDirectory = Split-Path -Parent $relativePath
        $relativePngPath = [IO.Path]::ChangeExtension($relativePath, '.png')
        $destinationFolder = if ([string]::IsNullOrWhiteSpace($relativeDirectory)) {
            $outputFolder
        }
        else {
            Join-Path $outputFolder $relativeDirectory
        }
        $destination = Join-Path $destinationFolder ([IO.Path]::GetFileName($relativePngPath))
        $temporary = Join-Path $destinationFolder "$($svg.BaseName).rendering.png"

        New-Item -ItemType Directory -Path $destinationFolder -Force | Out-Null
        Remove-Item -LiteralPath $temporary -Force -ErrorAction SilentlyContinue

        $expected = Get-ExpectedPixelSize -SvgPath $svg.FullName -RenderDpi $Dpi

        try {
            Push-Location -LiteralPath $svg.DirectoryName
            try {
                & $magick `
                    -density $Dpi `
                    -background none `
                    $svg.Name `
                    -units PixelsPerInch `
                    -density $Dpi `
                    -define 'png:exclude-chunks=date,time' `
                    $temporary
            }
            finally {
                Pop-Location
            }

            if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $temporary -PathType Leaf)) {
                throw "ImageMagick failed to render: $($svg.FullName)"
            }

            $actual = Get-PngProperties -ImageMagickPath $magick -PngPath $temporary
            if ($actual.Width -ne $expected.Width -or $actual.Height -ne $expected.Height) {
                throw "Unexpected dimensions for $($svg.Name): expected $($expected.Width)x$($expected.Height), got $($actual.Width)x$($actual.Height)"
            }
            if ([Math]::Abs($actual.DpiX - $Dpi) -gt 0.5 -or [Math]::Abs($actual.DpiY - $Dpi) -gt 0.5) {
                throw "Unexpected resolution for $($svg.Name): expected $Dpi DPI, got $([Math]::Round($actual.DpiX, 2)) x $([Math]::Round($actual.DpiY, 2)) DPI"
            }

            Move-Item -LiteralPath $temporary -Destination $destination -Force
            $converted++
            Write-Host "[$folderName] $relativePath -> $relativePngPath ($($actual.Width)x$($actual.Height), $Dpi DPI)"
        }
        finally {
            Remove-Item -LiteralPath $temporary -Force -ErrorAction SilentlyContinue
        }
    }
}

if ($converted -eq 0) {
    throw 'No PNG files were generated.'
}

Write-Host "Completed: generated $converted PNG file(s) at $Dpi DPI."