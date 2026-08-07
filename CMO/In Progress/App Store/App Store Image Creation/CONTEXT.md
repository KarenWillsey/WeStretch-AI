# App Store Image Creation Context

Use this file to keep the current work context, decisions, and chat-summary notes for this folder.

## Purpose
- Keep relevant information close to the asset folder.
- Make it easy to re-open work later and know what was decided.
- Preserve the key brief items, brand rules, and next steps.

## What to record
- Current task or objective
- Exact title and subtitle being used
- Human/reference image details
- Activity, setting, clothing, and asset requirements
- Relevant production rules from `Knowledge files/`
- Any open questions or missing inputs
- Chat summary or decisions from the current discussion

## Example
- Task: Finalize App Store screenshot assets for the 50–65 active lifestyle campaign.
- Title: “Move with confidence.”
- Subtitle: “Support your mobility with everyday strength and balance.”
- Human reference: `human reference Leo.png`
- Activity: walking a dog on a neighborhood path
- Open questions:
  1. Should the paddle be visible in the image?
  2. Confirm exact output dimensions before export.
- Notes: Use `02_WeStretch_Logo_Do_Not_Modify.png` and follow `06_WeStretch_App_Store_Production_Standards.txt`.

## Notes
- This is not an automated chat history file, but a hand-maintained local summary.
- Update it whenever the brief changes, a new draft is generated, or a key decision is made.

## Standing decisions (2026-08-06)
- **Clothing is locked to the reference photo** along with face, body type, hair and skin tone. It is no longer a separate free-form job-brief field — only change it if explicitly requested. (`GPT_INSTRUCTIONS.md`, `06_..._Production_Standards.txt` §7/§9 updated.)
- **Root cause of "logo/title/subtitle not identical" testing failures**: the logo mark itself was coming out visibly redrawn between images, which points to Image Generation drawing the logo/text directly instead of Code Interpreter compositing the exact asset. Instructions now require discarding any Image Generation output that contains logo-like marks or text before compositing.
- **3 concepts must be significantly different**, not near-duplicates. Each must now differ from the others in at least two of: action moment, camera angle, body position, composition/crop, background, amount of visible environment. Still 3 concepts × 2 sizes = 6 PNGs per run for now (not the full 10-slot App Store max) — one creative at a time, title/subtitle entered manually.
- **Output structure**: `Output/[Set Name]/Run_[NN]/`. Sets = Custom Product Page / A-B test variants (existing: `CPP Athletic performances`, `CPP for competitors`, `CPP for Pain`, `CPP senior mobility`, `Default A`). Runs within a set are sequentially numbered (`Run_01`, `Run_02`, ...), not timestamped. Next run for `Default A` is `Run_01` (folder currently empty).
- Fixed filename mismatches between `GPT_INSTRUCTIONS.md` and the actual `Knowledge files/` names (03/04/05 need `_TEMPLATE` suffix; logo placement spec renamed to `08_Logo_Placement_Spec_TEMPLATE.txt`).
- Reconciled small numeric drift between `06_..._Production_Standards.txt` and `08_Logo_Placement_Spec_TEMPLATE.txt`/`03_Title_Typography_Spec_TEMPLATE.txt` (logo centre/width/bottom, title top) — `08` and `03` are now the sole numeric source of truth; `06` mirrors them and must be corrected to match if they ever diverge again.

## Current brief (2026-08-07)
- Title: Physio-Informed, Adaptive Intelligence
- Subtitle: Always get the right pose at the right time. (typo "teh" from the 2026-08-06 brief corrected by the user)
- Source photo: `SourceImages/source image one.png` (single photo, three crop/zoom framings per size so the user can pick).
- Output: 6 PNGs delivered to `Output/Default A/` (V1/V2/V3 x iPhone 1320x2868 + iPad 2064x2752) plus `verification_report.txt`.

## Standing decisions (2026-08-07)
- **Calibrated template numbers** (pixel-measured from the authorized `Output/Default A/Screen 2.png`, 853x1844): title Inter ExtraBold 3.85%H (NOT the old 4.60%), advance 4.93%H, visible ink top 11.88%H; subtitle Inter SemiBold 2.22%H (NOT 2.75%), advance 2.87%H, ink top 23.16%H; logo visible height 2.33%H, top 4.93%H, centre 49.53%W; fade = charcoal gradient RGB(12,13,14)->RGB(30,30,31) opaque to 28%H, smoothstep to transparent by 42%H (not pure black). Specs 03/04/06/08 updated to match.
- **Text-box width rules are % of canvas HEIGHT** (title min(90%W, 41%H); subtitle min(90%W, 30%H)) — the Run_01 failure came from applying them to width. Specs now include worked pixel examples.
- **Title line limit**: 2 lines when a subtitle is present (3-line titles collide with the fixed subtitle position); 3 only with no subtitle.
- **Inter static fonts live in `Fonts/`** (Inter-ExtraBold.ttf, Inter-SemiBold.ttf, from the official Inter 4.1 release). Rendering with a fallback font is forbidden — the build script hard-fails if they're missing.
- **`build_app_store_images.py` rewritten**: implements the calibrated template, supports `--source-image` (3 crop/zoom variants from one photo; pan variants for phone, zoom variants for tablet since the tablet canvas has no horizontal slack) and `--source-dir` (3 photos), and self-verifies every export against the authorized targets into `verification_report.txt`; any FAIL blocks delivery.
- **Spelling/grammar gate**: if a supplied title/subtitle looks misspelled or ungrammatical, ask the user to confirm exact wording BEFORE production (added to `GPT_INSTRUCTIONS.md` and `06` §6).
- **Review before delivery**: outputs must be visually inspected and measured before being saved into an Output folder — never deliver unreviewed images (added to `GPT_INSTRUCTIONS.md` quality check and `06` §17).
- ~~Logo asset SHA-256: F63C9C9F...094E~~ superseded same day, see below.

## Standing decisions (2026-08-07, afternoon — brand colors & crop rules)
- **Brand colors source of truth** = `Globial Knowledge Content/Brand Guildeline.pdf`: Fire Red #FC4850, WHITE #FFFFFF, Midnight Grey #1F1F1F (+ Dark Grey #4C4C4C; secondary Light Grey #E4E4E4, Sunshine Gold #FBBC05, Lavender Blue #667FD4, Medium Grey #ADACAC). That PDF is never edited unless Karen explicitly instructs; branding changes flow FROM it. Assets that disagree get flagged, not silently used.
- **Logo asset corrected to brand red**: the "WE" was off-brand #F05556; recolored to #FC4850 (white was already #FFFFFF). Old file kept as `Knowledge files/Retired_02_WeStretch_Logo_OffBrand_Red_F05556.png` (Retired = never authoritative). New SHA-256 in spec 08: 8B8C89D92516C072B1259AD307B4D49D65B0E0B6E7F20476DD840AB7048CD7FF.
- **Fade bottom tone snapped to brand Midnight Grey #1F1F1F** (was measured 30,30,31 — imperceptible 1/255 change).
- **Crop rules (hard limits)**: at most half a foot may be cropped; no other body part; head + ALL hair always fully visible. Exceptions need explicit per-job permission recorded in run notes. If a source can't comply for an output size, stop and ask (added to GPT_INSTRUCTIONS.md and 06 §8).
- **Recorded permission for this run**: Karen permitted cropping the raised leg on the iPhone crops of `source image one.png` (lying pose spans 76.5% of source width; iPhone window is 57.5%, so head/hair + half-foot cannot both fit). iPad crops comply without exception.
- Final delivery re-rendered with brand-red logo and compliant crops → `Output/Default A/` (2026-08-07 afternoon files).
