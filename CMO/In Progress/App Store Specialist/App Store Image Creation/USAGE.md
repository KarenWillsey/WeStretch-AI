# App Store Image Creation Script Usage

This folder now includes a deterministic compositing script for WeStretch App Store image production.

## Script
- `build_app_store_images.py`

## Requirements
- Python 3.14 or compatible
- Pillow
- Three source lifestyle photos in a local folder
- `02_WeStretch_Logo_Do_Not_Modify.png` from `Knowledge files/`
- Optional exact Inter font files: `Inter-ExtraBold.ttf` and `Inter-SemiBold.ttf`

## Example workflow
1. Create a source folder and add your 3 base photographs:
   - `CMO/In Progress/App Store/App Store Image Creation/SourceImages/`
   - Use three distinct concepts that preserve the reference model and activity.

2. Run the script from the App Store Image Creation folder:

```powershell
cd "c:\Users\karen\Documents\WeStretch AI\WeStretch-AI\CMO\In Progress\App Store\App Store Image Creation"
C:/Python314/python.exe build_app_store_images.py \
  --source-dir "SourceImages" \
  --output-dir "Output/Default A/Run_01" \
  --logo-path "Knowledge files/02_WeStretch_Logo_Do_Not_Modify.png"
```

3. If you have the Inter font files, add:

```powershell
  --title-font "path\to\Inter-ExtraBold.ttf" \
  --subtitle-font "path\to\Inter-SemiBold.ttf"
```

## Expected output
- `V1_1320x2868.png`
- `V1_2064x2752.png`
- `V2_1320x2868.png`
- `V2_2064x2752.png`
- `V3_1320x2868.png`
- `V3_2064x2752.png`
- `WeStretch_App_Store_Images_Run_01.zip`
- `logo_verification.txt`

## Notes
- The script crops and resizes the source images to the required sizes.
- It also generates `logo_verification.txt` with the logo top, centre, width, and height percentages for every output image.
- It applies the black fade, places the approved logo, and renders the exact title and subtitle.
- The source images must be text-free and should not include any generated logo or typography.
