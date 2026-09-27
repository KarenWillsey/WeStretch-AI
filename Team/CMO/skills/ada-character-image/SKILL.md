---
name: ada-character-image
description: Use when generating or editing images of Ada, WeStretch's established female 3D animated coach, from a human pose photo or verbal instructions. Preserve her recognizable face and body proportions, locked charcoal and red outfit, exact WESTRETCH chest artwork and WE leg mark. Supports lifestyle composites, studio scenes, and true transparent PNG cutouts.
---

# Ada character image

Create images in which Ada looks like the **same animated character in another frame**, even when she appears beside a real person. A human pose reference supplies biomechanics only. It never supplies Ada's face, physique, age, style, or wardrobe.

## Canonical assets

Inspect `assets/ada-references/` before every generation. This folder is intentionally restricted to four identity anchors:

| Need | Primary reference |
| --- | --- |
| Face, green eyes, bob, expression, tank details | `Ada_1.png` |
| Alternate face and upper-body angle | `Ada_2.png` |
| Full-body scale, outfit, shoes, leg mark | `Ada_front.png` |
| Rear silhouette and outfit | `Ada_back.png` |

Use `assets/pose-library/` only when its pose closely matches the request. A pose image controls joint placement, camera angle, and contact points only; it never controls Ada's face, body shape, clothing, branding, rendering style, or proportions. Use no more than two identity anchors plus one pose reference in a generation request. Never use files from `Team/CMO/Archive/Ada Source Images/` as generation inputs.

`assets/branding/WeStretch_logo_reference.png` is the **complete transparent red-and-white WESTRETCH chest wordmark**. Preview it on charcoal, not white. Preserve its original pixels and alpha. `assets/branding/WeStretch_leg_logo_reference.png` is the canonical small red `WE` and dots used on Ada's upper leg. Use the two original assets for their specific placements; do not swap or redraw them.

The source folders to consolidate are recorded in `references/source-catalog.md`. Additional images showing other clothing are pose or camera references only. Never treat Bruce, a human actor, a costume variant, an iPhone mockup, or a generated near-match as the primary Ada identity anchor.

## Non-negotiable visual lock

- Keep Ada clearly **stylized 3D animation**, with the same light-brown side-parted bob, large green eyes, simplified smooth features, and recognizable face. Do not make her a photoreal woman, age her, or substitute a generic animated model.
- Match the closest canonical full-body view for head-to-height, shoulder-to-hip, waist-to-hip, torso-to-leg, limb thickness, hand size, and shoe scale. Pose and perspective change projected lengths; underlying anatomy cannot change.
- Use the charcoal-grey sleeveless tank with red neckline and arm trim and red underbust band; charcoal-grey full-length leggings with broad red waistband and thin red side accents; grey/red shoes. Keep skin and hair tones from the canonical images. No alternate colors, sleeves, shorts, or costume.
- Put the exact chest wordmark on the upper tank and the small `WE` with dots on the upper leg at reference scale and position. Reject missing, misspelled, mirrored, garbled, or substitute branding.

## Intake

Take the user's pose photo or verbal pose description, output use, dimensions, camera view, and background. Ask for a background only when it affects the result and the prompt gives no usable context; otherwise choose a clean neutral setting. A requested transparent background always means PNG pixels with a real alpha channel, never a checkerboard image.

For a pose photo, map left/right limbs, foot stance, joint bends, hand contact, torso lean and rotation, and gaze. Preserve Ada's anatomy rather than stretching or shrinking her body to fit a human reference. For an edit, list the exact change region and preserve all unmentioned people, scene objects, framing, text, and lighting. The user's background choice overrides the original WeStretch gym.

## Output location

Save every generated or edited Ada candidate to `Team/CMO/Review ToDo/` before reporting completion. Use a descriptive filename such as `YYYY-MM-DD_ada-short-description_v01.png`. Never save generated candidates inside this skill's `assets/` folders; those contain canonical references only. Do not place a candidate in `Team/CMO/Image Catalogue/` until Karen approves it. Report the exact saved path with the preview.

## Production workflow

1. **Select references.** Use `Ada_front.png` plus the single closest face or rear identity anchor. Add at most one image from `assets/pose-library/` only when needed for biomechanics. Include the chest artwork when supported. State each image's role. Never browse or use the archive.
2. **Generate or edit.** Use an image generation tool for the bitmap. Prompt for one Ada, the precise pose and background, her 3D identity, outfit, proportions, and exact branding. Use the prompt pattern below. For an accepted composition, use it as the edit target and change only the specified region.
3. **Inspect at two scales.** At full frame check pose, perspective, integration and relative scale. At close crop check face, hands, shoes, fabric trim, chest letters, leg `WE` and dots. Compare to the closest original view. If Ada looks human or has a different face, revise using `Ada_1.png` and `Ada_front.png`.
4. **Fix branding.** Generators can invent letters. Prefer placing the original transparent chest and leg artwork over the garment with a localized edit or deterministic compositing, transforming scale and perspective to follow the fabric. Do not redraw lettering. Visually verify every element and never claim a generated mark is exact without inspection.
5. **Verify output.** Run `python scripts/check_png.py OUTPUT.png --transparent` for a cutout. It checks actual alpha, transparent corners, and border leakage. For nontransparent PNG, run it without the flag. Inspect edges visually too. Verify dimensions against the request.
6. **Review and stage.** Revise material identity, proportion, outfit, pose, branding, or transparency failure. Save the reviewed candidate in `Team/CMO/Review ToDo/` and report its exact path. Keep the staged output as the direct target for small follow-up edits. When exact fidelity remains uncertain, describe the specific issue rather than reporting 100% compliance.

## Prompt pattern

> **Target:** [new image or edit target; exact change region]. **Ada identity:** Use `Ada_1.png` for the exact animated face and `Ada_front.png` for body ratios, outfit and shoes; [other view] for angle. Keep her distinctly stylized 3D, not photoreal. **Pose:** [limbs, stance, torso, gaze]; the human reference controls pose only. **Scene:** [background, camera, crop, lighting]. **Wardrobe and marks:** locked charcoal/red tank and leggings, original red/white WESTRETCH chest artwork, small red WE-and-dots upper-leg mark at canonical placement. **Preserve:** [unmentioned contents of edit target]. **Output:** [dimensions, PNG, actual alpha when requested]. Avoid extra logos, fake text, extra people, and distorted anatomy.

## Final gate

Check: same animated face and hair; same underlying body shape and scale; anatomically faithful pose; locked clothing and colors; leg and chest marks correct; clean hands, feet, and floor contact; scene invariants preserved; genuine alpha if requested. A visual review can identify drift but cannot mathematically certify a generated identity as “100% identical.” If a reference angle is missing, ask for it when that prevents a reliable result.
