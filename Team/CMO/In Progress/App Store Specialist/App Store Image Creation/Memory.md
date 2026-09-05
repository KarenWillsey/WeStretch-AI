# App Store Image Creation; Memory

Folded in from this project's former `CONTEXT.md` (hand-maintained decision
log, 2026-08-06 through 2026-08-12). Calibrated by pixel-measuring the
authorized reference `Output/Default A/Screen 2.png` (853x1844).

## Calibrated template numbers (source of truth)

Pixel-measured from the authorized reference:

- **Title**: Inter ExtraBold 3.85%H (not the old 4.60%), advance 4.93%H,
  visible ink top 11.88%H.
- **Subtitle**: Inter SemiBold 2.22%H (not 2.75%), advance 2.87%H, ink top
  23.16%H.
- **Logo**: visible height 2.33%H, top 4.93%H, centre 49.53%W.
- **Fade**: charcoal gradient RGB(12,13,14)->RGB(30,30,31) (not pure black) 
  opaque to 28%H, smoothstep to transparent by 42%H. Bottom tone later
  snapped to brand Midnight Grey #1F1F1F (imperceptible 1/255 change).
- **Text-box width rules are % of canvas HEIGHT, not width**: title
  min(90%W, 41%H), subtitle min(90%W, 30%H). The Run_01 failure came from
  applying these to width; specs now include worked pixel examples.
- **Title line limit**: 2 lines when a subtitle is present (3-line titles
  collide with the fixed subtitle position); 3 only with no subtitle.
- Specs `03`/`04`/`06`/`08` in `Knowledge files/` are updated to match all of
  the above. `08` and `03` are the sole numeric source of truth for
  logo/title placement; `06` mirrors them and must be corrected to match if
  they ever diverge again.

## Standing gates (non-negotiable)

- **Clothing/face/body/hair/skin tone locked to the reference photo**: not a
  free-form job-brief field; change only if explicitly requested
  (`GPT_INSTRUCTIONS.md`, `06_..._Production_Standards.txt` §7/§9).
- **Spelling/grammar gate**: if a supplied title/subtitle looks misspelled or
  ungrammatical, ask Karen to confirm exact wording BEFORE production; never
  silently correct, never render as-is (`GPT_INSTRUCTIONS.md`, `06` §6; see
  also the general version of this rule in root `Memory.md`).
- **Review before delivery**: outputs must be visually inspected and measured
  before being saved into an `Output/` folder; never deliver unreviewed
  images (`GPT_INSTRUCTIONS.md` quality check, `06` §17; see also root
  `Memory.md`).
- **Crop rules (hard limits)**: at most half a foot may be cropped, no other
  body part, head + ALL hair always fully visible. Exceptions need explicit
  per-job permission recorded in run notes; if a source can't comply for an
  output size, stop and ask (`GPT_INSTRUCTIONS.md`, `06` §8).
- **3 concepts per run must be significantly different**, not near-duplicates,
each must differ from the others in at least two of: action moment,
  camera angle, body position, composition/crop, background, amount of
  visible environment. 3 concepts × 2 sizes = 6 PNGs per default run (not the
  full 10-slot App Store max); one creative at a time, title/subtitle entered
  manually.
- **Output structure**: `Output/[Set Name]/Run_[NN]/`. Sets = Custom Product
  Page / A-B test variants (e.g. `CPP Athletic performances`, `CPP for
  competitors`, `CPP for Pain`, `CPP senior mobility`, `Default A`). Runs
  within a set are sequentially numbered (`Run_01`, `Run_02`, ...), not
  timestamped.
- **Fonts**: Inter static fonts live in `Fonts/`; rendering with a fallback
  font is forbidden, the build script hard-fails if they're missing.
- **`build_app_store_images.py`** implements the calibrated template,
  supports `--source-image` (3 crop/zoom variants from one photo, pan
  variants for phone, zoom variants for tablet since the tablet canvas has no
  horizontal slack) and `--source-dir` (3 photos), and self-verifies every
  export against the authorized targets into `verification_report.txt`; any
  FAIL blocks delivery.

## Brand source of truth

- **Brand colors** come from `Knowledge Base/Brand Guildeline.pdf`:
Fire Red #FC4850, White #FFFFFF, Midnight Grey #1F1F1F (+ Dark Grey
  #4C4C4C; secondary Light Grey #E4E4E4, Sunshine Gold #FBBC05, Lavender Blue
  #667FD4, Medium Grey #ADACAC). That PDF is never edited without Karen's
  explicit instruction; branding changes flow FROM it. Assets that disagree
  get flagged, not silently used.
- **Logo asset corrected to brand red 2026-08-07**: the "WE" was off-brand
  #F05556, recolored to #FC4850. Old file kept as
  `Knowledge files/Retired_02_WeStretch_Logo_OffBrand_Red_F05556.png`
  (Retired = never authoritative). Current logo SHA-256:
  `8B8C89D92516C072B1259AD307B4D49D65B0E0B6E7F20476DD840AB7048CD7FF`.

## Root-cause fixes worth remembering

- **"Logo/title/subtitle not identical" testing failures** traced to Image
  Generation drawing the logo/text directly instead of Code Interpreter
  compositing the exact asset. Instructions now require discarding any Image
  Generation output containing logo-like marks or text before compositing.

## Notable past runs (chronological)

- **2026-08-12; Default A / Run_02, "Physio-Informed Stretches"**: two-person
  clinical stretch photo (patient + physiotherapist), Karen explicitly
  approved keeping both people despite the usual "avoid unnecessary secondary
  people" rule (§10). Output override: 1 iPhone + 1 iPad PNG from a single
  supplied photo (not the default 3-concept/6-PNG output). Revised same day:
  lowered/zoomed the crop (phone zoom 1.3, tablet zoom 1.6) so the
  physiotherapist's head cleared the fade/title band, on this source photo,
  clearing her head and keeping both feet in frame couldn't both be
  satisfied, so both feet were cropped out entirely; Karen explicitly
  permitted this tradeoff.
- **2026-08-12 note**: the phone-compositing "Ada inside phone" job that had
  been sketched for this folder's `Run_02` moved to its own dedicated project,
  `Ada Stretching Phone Image/` (see that project's own `CLAUDE.md`/`Memory.md`
  and `Team/CMO/skills/ada-stretching-phone-image/SKILL.md`). It no longer occupies
  a slot in this pipeline.
- **2026-08-07; Default A, "Physio-Informed, Adaptive Intelligence"**:
  established the calibrated template numbers above; delivered with
  brand-red logo and compliant crops (Karen permitted cropping the raised leg
  on the iPhone crops of `source image one.png`, the lying pose exceeds the
  iPhone window's width, so head/hair + half-foot couldn't both fit; iPad
  crops complied without exception).
