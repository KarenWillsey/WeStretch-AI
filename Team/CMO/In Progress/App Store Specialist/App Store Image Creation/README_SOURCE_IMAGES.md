# Source Images for App Store Export

Place the source lifestyle photographs here before running `build_app_store_images.py`.

## Required files
- Three source images in the same pose / activity style
- Each image should be text-free and logo-free
- Each image should show the subject clearly in a clean minimalist home-like environment
- File formats supported: PNG, JPG, JPEG, WEBP

## Example path
- `Team/CMO/In Progress/App Store/App Store Image Creation/SourceImages/source1.png`
- `Team/CMO/In Progress/App Store/App Store Image Creation/SourceImages/source2.png`
- `Team/CMO/In Progress/App Store/App Store Image Creation/SourceImages/source3.png`

## How to run
```powershell
cd "c:\Users\karen\Documents\WeStretch AI\WeStretch-AI\CMO\In Progress\App Store\App Store Image Creation"
C:/Python314/python.exe build_app_store_images.py \
  --source-dir "SourceImages" \
  --output-dir "Output/Default A/Run_01" \
  --logo-path "Knowledge files/02_WeStretch_Logo_Do_Not_Modify.png"
```

If you have the exact font files, add:
```powershell
  --title-font "path\to\Inter-ExtraBold.ttf" \
  --subtitle-font "path\to\Inter-SemiBold.ttf"
```
