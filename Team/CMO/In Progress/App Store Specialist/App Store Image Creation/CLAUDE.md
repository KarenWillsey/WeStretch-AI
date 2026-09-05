# App Store Image Creation; CLAUDE.md

Scope: the App Store screenshot compositing pipeline, turns a title,
subtitle, and source lifestyle photo into brand-compliant App Store
screenshots (iPhone + iPad), pixel-verified against an authorized reference.
Read `Memory.md` alongside this file before running anything.

## Where things live

- `GPT_INSTRUCTIONS.md`: the production instructions/process.
- `USAGE.md`: how to run `build_app_store_images.py` (the deterministic
  compositing script; requires Python 3.14+, Pillow).
- `README_SOURCE_IMAGES.md`: source-image requirements.
- `Knowledge files/`: numbered spec files (typography, output sizes,
  production standards, logo placement) plus locked reference images. The
  numbered specs (`03`/`04`/`05`/`06`/`08`) are the numeric source of truth;
  see `Memory.md` for which one wins if they ever drift again.
- `Fonts/`: exact Inter static font files the script requires; it hard-fails
  rather than substitute a fallback font.
- `SourceImages/`: input photos for a run.
- `Output/[Set Name]/Run_[NN]/`: delivered output only. **Never place
  unreviewed images here** (see root `Memory.md`); every export is
  self-verified against the authorized targets into `verification_report.txt`
  and any FAIL blocks delivery.

## Before starting a run

Read `Memory.md` in full; it holds the calibrated pixel/color values this
pipeline was built against, the hard-limit crop rules, and the standing
gates (spelling/grammar confirmation, pre-delivery review). These were
derived by hand from the authorized reference image and from real delivery
failures; don't re-derive or loosen them without checking this file first.
