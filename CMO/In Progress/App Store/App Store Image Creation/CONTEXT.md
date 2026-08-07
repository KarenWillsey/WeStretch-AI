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

## Current brief (2026-08-06)
- Title: Physio-Informed, Adaptive Intelligence
- Subtitle: Always get teh right pose at the right time.
- Human reference: uploaded model in green outfit, matching the stretch pose of the woman in the pink shirt.
- Activity: stretch/mobility pose in a clean minimalist home living room.
- Output: 3 unique iPhone images and 3 unique iPad images.
- Set: Default A / Run_01.
- Note: workspace does not contain an image generation/compositing pipeline, so the final PNG assets must be produced externally or via a new script.
