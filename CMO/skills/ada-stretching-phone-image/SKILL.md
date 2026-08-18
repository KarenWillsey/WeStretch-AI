---
name: ada-stretching-phone-image
description: Create WeStretch marketing images of Ada performing a user-supplied human stretch pose, either fully contained inside an iPhone screen or using a trompe-l'oeil effect where Ada extends out of the phone. Output is a transparent PNG cutout by default, delivered in both required App Store sizes (iPhone 6.9-inch and iPad 13-inch) into the output folder. Preserve Ada's identity, proportions, skin tone, anatomy, the WeStretch studio, and branding (chest + leg logos, exact art and placement) exactly, and match the human pose reference exactly. Prefer Higgsfield MCP for generation/editing. Ends with a mandatory pre-delivery review gate — never auto-finalize.
---

# Ada Stretching Phone Image

Use this skill whenever the user wants a WeStretch image that places **Ada** into a stretch pose shown by a human reference photo and presents her in or emerging from an iPhone.

**Assets, examples, and delivered output live outside this skill folder, for human browsability:**
`CMO/In Progress/App Store/Ada Stretching Phone Image/`
- `assets/` — locked reference images (see `reference-map.md` in that folder)
- `output/` — delivered PNGs, flat, no subfolders
- `reference-map.md` — the asset table

This `SKILL.md` is the only file that lives in `CMO/skills/ada-stretching-phone-image/`. Every path below is relative to `CMO/In Progress/App Store/Ada Stretching Phone Image/` unless stated otherwise.

## Core rule

Treat Ada (face, proportions, anatomy, skin tone), her outfit, the WeStretch studio, and the WeStretch logos (chest and leg, exact art **and** exact placement) as **locked brand assets**. The requested stretch pose, camera angle, phone presentation, crop, and output dimensions may change; nothing else may drift — not even a little, not even by accident across a chain of edits.

## Known failure modes (observed 2026-08-11 — read this before generating)

A real generation run ("knee tuck leg raise") failed on exactly the things this skill is supposed to lock down. Both defects were caught by Karen, not by the checklist, which is why the checklist and this section now call them out explicitly:

- **Chest logo was re-lettered, not traced.** The model produced a stacked/wrapped "WE / STRETCH" treatment curved around the ribcage instead of `westretch-logo-reference.png`'s flat, single-line horizontal wordmark. It invented a layout instead of projecting the real artwork onto the fabric.
- **Leg logo was invented and mislocated.** The model drew a thick, differently-styled "W" shape near the knee instead of `westretch-logo-secondary-leg-reference.png`'s slim rounded "WE" mark placed on the upper-outer front thigh, just below the waistband.

If a candidate does either of these, it is not a minor touch-up — treat it as a failed logo generation and run the dedicated logo-correction edit pass described in § Logo before showing anything to the user.

A second run (also 2026-08-11, a reclined stretch pose) re-failed the leg logo in a new way even after the chest logo was corrected: **the leg logo landed on the hip/glute/side of the leg instead of the front of the thigh**, and was mirrored/upside-down with its dots on the wrong side. This is why `ada-side-profile-leg-stripe-logo-reference.png` (see Logo below) now exists as an explicit, unambiguous placement reference — when the leg logo is in frame, check it against that image specifically, not just the written description.

## Known gaps (read before starting)

1. **No approved exemplar yet** — there is no single "this is the target output" image to match against. Once the user approves a generated image, save it into `assets/approved-exemplars/` with a short filename describing the pose/mode, so future runs have a real north star instead of only prose rules.

## Required inputs per image

Ask only for missing information that cannot be inferred from the request:

1. **Pose reference** — one or more photos of a human performing the desired stretch.
2. **Presentation mode** — one of:
   - `inside-phone`: Ada remains completely inside the iPhone screen as a believable app screenshot.
   - `trompe-loeil`: Ada remains visually connected to the phone/studio but selected limbs or body parts extend beyond the phone bezel into the surrounding composition.
3. **Output format** — PNG with true alpha transparency is the **default** for every deliverable from this skill (these are marketing cutouts meant to be composited elsewhere). Only skip transparency if the user explicitly asks for a background scene instead.

If the user omits the camera angle, choose the angle that best communicates the pose while preserving studio continuity.

## Output sizes (required)

Every delivered image must be produced in **both** of these sizes — matching the App Store output spec in `CMO/In Progress/App Store/App Store Image Creation/Knowledge files/05_Output_Size_Requirements_TEMPLATE.txt`:

| Size label | Device | Width | Height | Orientation | Format |
|---|---|---|---|---|---|
| `iphone-6.9` | iPhone 6.9-inch | 1320px | 2868px | Portrait | PNG |
| `ipad-13` | iPad 13-inch | 2064px | 2752px | Portrait | PNG |

Both sizes are required per approved pose/mode, not a pick-one. Generate at the correct portrait orientation and framing, then canvas-fit/resize to hit these exact pixel dimensions as a finishing step — don't stretch or distort Ada, the phone, or the studio to force-fit; pad or adjust crop instead. Save both as separate files (see Output folder below); do not skip a size because it looks close enough.

## Output folder

Save every delivered PNG directly into `CMO/In Progress/App Store/Ada Stretching Phone Image/output/` — flat, no subfolders, no scratch/working files. Filename pattern: `<pose-slug>-<mode>-<size-label>.png`, e.g. `forward-fold-inside-phone-iphone-6.9.png` and `forward-fold-inside-phone-ipad-13.png`. Keep intermediate crops, comparison renders, or rejected candidates out of this folder entirely — use your own scratch space for those, never `output/`. See `output/README.md`.

## Review staging folder (pre-approval candidates)

While a candidate is awaiting the mandatory Pre-delivery review gate below, save it as a real file into `CMO/In Progress/App Store/Ada Stretching Phone Image/waiting for approval/` (flat, no subfolders) — not just described or embedded in chat — so Karen can open it directly as a file for review. Use a filename that identifies the attempt, e.g. `<pose-slug>-<mode>-candidate-<n>.png`. This folder is working space, not delivery space:
- Once a candidate is approved, canvas-fit it to both required sizes and save those into `output/` per the naming pattern above; the working candidate can stay in `waiting for approval/` or be removed at that point — it is never itself a delivered size.
- Rejected/superseded candidates should be cleared out of this folder once a review cycle ends, so it always reflects what's currently awaiting a decision, not a growing archive.

## Locked reference assets

All paths below are inside `CMO/In Progress/App Store/Ada Stretching Phone Image/assets/` (see `reference-map.md` in that same folder for the full table and caveats).

### Ada identity and wardrobe
- `ada-front.png` — primary face, front identity, hair, proportions, outfit, **and the only full-body reference that shows both logos in their correct locations at once.** Treat it as the placement ground truth for both the chest and leg logo.
- `ada-back.png` — rear identity and wardrobe. No leg or chest logo is visible from behind — don't add one to a rear-facing pose.
- `ada-expression-wave.png`, `ada-expression-present.png`, `ada-expression-thumbsup.png` — additional facial/expression/gesture references, already true alpha-transparent cutouts. Treat their crop/edge quality as the transparency bar every deliverable must hit.

### Studio
- `studio-canonical.png` — **the** WeStretch studio. Ada must always be visually located in this studio. Camera angle may change; architecture, materials, palette, lighting family, and recognizable studio details (backlit wordmark sign, stone accent wall, wood beams, arched windows, wood shelving) must not change.
- `ada-fullbody-alt-studio-cobra-1.png` / `-2.png` render in a *different, uncontrolled* environment (different lamp, different wall art, no vaulted ceiling). **Do not use these for studio-background guidance.** They're only valid for full-body proportion/wardrobe/shoe reference.

### Phone / composition examples
- `example-inside-phone-appstore-headline.png` — inside-phone with marketing headline overlay (opt-in format only).
- `example-inside-phone-neck-stretch.png` — inside-phone, no overlay UI. Default-mode reference.
- `example-trompe-loeil-knee-to-chest.png`, `example-trompe-loeil-childs-pose.png`, `example-trompe-loeil-lunge.webp` — trompe-l'oeil / screen-breaking references. Use `example-trompe-loeil-lunge.webp` as the primary reference for a clean bezel edge transition.

### Logo

- `westretch-logo-reference.png` — **exact chest-logo artwork.** A flat, single horizontal line: red "WE" + white "STRETCH" + red dots. Preview on a dark canvas; the "STRETCH" lettering is white and disappears on light backgrounds.
- `westretch-logo-secondary-leg-reference.png` — **exact leg-logo artwork.** The "WE" mark alone (no "STRETCH"), slim rounded strokes, same red as the chest mark, with four dots beneath it.
- `ada-side-profile-leg-stripe-logo-reference.png` — **exact leg-logo and leg-stripe placement, side-on.** Feed this alongside the two artwork files above whenever the leg is in frame; it removes any ambiguity the written description below leaves room for.

**Placement (verified against `ada-front.png` and `ada-side-profile-leg-stripe-logo-reference.png`):**
- **Chest logo** — centered on the front of the tank top, below the neckline/collar seam, roughly mid-chest. It sits on stretch fabric over a curved, moving 3D surface, so it *must* deform with the garment: it can bend gently around the chest curvature and pick up fabric folds/highlights/shadows like a real screen-print. What it must **not** do is change layout — it stays one horizontal line, "WE" then "STRETCH" left to right, not stacked, not wrapped vertically, not re-kerned into a new shape. If the surface curvature is too extreme (e.g. a very foreshortened or side-on torso) for the full wordmark to read cleanly, it's fine for it to look partially foreshortened by perspective — it is not fine for it to be re-lettered into a different arrangement to "fit."
- **Leg logo** — on the **front** of Ada's **left thigh** (her left, screen-right when she's facing camera), upper area, just below the waistband edge, sitting beside where the red side stripe begins. It is small — don't enlarge it into a hero element. It belongs on the flat front plane of the thigh, **not** on the hip, the side of the leg, or the glute — see `ada-side-profile-leg-stripe-logo-reference.png` for exactly where "front of thigh" means on this body. **Only include it if that specific zone of the leg is actually in frame and roughly facing the camera** in the generated pose/angle/crop. If the pose, angle, or crop doesn't show that zone, no leg logo appears anywhere in the image — do not relocate it to the knee, calf, hip, glute, or the other leg to force it into view.
- **Leg stripe** — the coral/red stripe on the leggings runs the **full length of the leg**, from the waistband all the way down to the ankle/shoe — it is not a short accent confined to the upper thigh. See `ada-side-profile-leg-stripe-logo-reference.png`.

Both logos must trace back to their reference file exactly — do not invent, abbreviate, restyle, re-letter, change stroke weight, or approximate either mark, and do not substitute one mark for the other. Preserve letterforms, spacing, dot placement, and brand red.

**After every generation, before running the rest of the quality gate:** zoom into the chest and (if present) the leg logo and compare each against its reference file side by side. If either fails the layout/placement check above, run a focused edit pass — feed the exact logo reference as the primary input, constrain the edit to that logo's region only, and re-check. Do not present a candidate with an invented logo to the user "to see what they think" — fix it first.

## Identity lock

Ada must keep, in every generation:

- **Face and expression range** — same face shape, same green almond eyes, same eyebrows, nose, and mouth. Default expression is warm/friendly (soft smile), matching the reference set; don't flatten it to neutral or exaggerate it into a different personality.
- **Hair** — same bob haircut, same length and shape, same multi-tone warm brunette/rose-gold coloring and part.
- **Skin tone** — same warm light-medium skin tone shown across `ada-front.png`, `ada-back.png`, and the expression cutouts. Do not let generation drift it lighter, darker, tanner, paler, or shift its undertone (warm vs. cool) across edits or between pose variants.
- **Body proportions** — same stylized 3D-character proportions (torso-to-leg ratio, shoulder width, waist, limb thickness) across every pose and camera angle. Do not "correct" her toward generic photoreal human proportions, and don't let proportions drift across a chain of iterative edits.
- **Wardrobe** — the same charcoal athletic top and leggings with coral/red trim, same shoe styling, unless the user explicitly requests a wardrobe change.

## Anatomy lock

Ada must always read as anatomically plausible, even in a stylized pose:

- **Five fingers per hand**, correctly jointed — no fused, missing, extra, or malformed digits. Check hands closely in trompe-l'oeil compositions where a hand crosses the bezel; that seam is the most common place for AI hand errors to hide.
- **Five toes per foot** if bare feet are ever shown (Ada normally wears shoes in every reference — bare feet are an exception, not the default; if shoes are on, this doesn't apply).
- **Joints bend only in anatomically correct directions** — knees, elbows, wrists, ankles must not hyperextend or bend backward.
- **The pose must be within real human range of motion.** The human reference photo defines the target pose; if literal translation to Ada's proportions would require an anatomically impossible joint angle, adapt the pose enough to keep it human-plausible rather than forcing an exact copy.
- **Limb continuity** — no extra limbs, no limbs that vanish behind an implausible occlusion, no duplicated body parts (a second-most-common AI generation failure alongside hands).

## Studio and color/lighting lock

The generated image must stay in the same tone family as `studio-canonical.png` and the Ada references:

- warm-neutral studio light;
- natural pale-beige walls;
- warm wood floor and beams;
- neutral gray mat and stone/brick surfaces;
- Ada's original skin and hair tones (see Identity lock above);
- charcoal clothing with the original coral/red accents;
- no orange wash, hyper-saturation, cool-blue cast, crushed blacks, or cinematic recoloring unless explicitly requested.

Background outside the phone (or outside phone + studio, if a non-transparent scene is explicitly requested) must be **100% true to `studio-canonical.png`** — camera angle may change, but materials, architecture, and recognizable details may not, unless the user explicitly asks for a different setting.

When editing an existing approved image, preserve its geometry and composition and adjust only the requested items.

## Pose matching

The human reference defines biomechanics, not identity — but it defines them **exactly**, not approximately. "A similar-looking stretch" is not a pass. Match:

- front/back leg selection;
- knee bend angle and foot placement;
- torso rotation and lean;
- shoulder orientation;
- arm path;
- elbow and wrist positions;
- hand direction and grip/contact;
- head orientation when relevant;
- overall camera framing/angle relative to the pose, unless the user asked for a different angle.

Adapt a joint's exact angle only when literal translation would break the Anatomy lock (an impossible human joint angle) — and even then, adapt as little as possible and note the specific adaptation in the pre-delivery review note (see Pre-delivery review gate). "Adaptation for anatomical plausibility" is not a license to loosely reinterpret the pose; it's a narrow exception for genuinely impossible geometry.

Before presenting a candidate, do an explicit side-by-side check against the human reference photo, landmark by landmark using the list above — not a general glance for "does this look like a stretch." Note any landmark that doesn't match and fix it or justify it before moving to the quality gate.

## Phone rules

### inside-phone
- Keep Ada, mat, and studio fully inside the display boundary.
- The iPhone must read as a real device frame.
- Default: **no overlay UI** unless the user explicitly asks for UI (see `example-inside-phone-appstore-headline.png` for what opt-in overlay looks like).
- No notification banners, debug console, fake status elements, captions, timers, progress bars, menu icons, or generated text. (`ada-back.png` was cropped for exactly this kind of contamination before being kept as a reference.)

### trompe-loeil
- Maintain a clear visual relationship between the phone screen and the studio image.
- Ada must appear to originate from the screen, not stand independently in front of it.
- Let only compositionally useful limbs/body areas break the bezel.
- Preserve realistic overlap, occlusion, scale, depth, and edge transitions.
- Default: **no overlay UI** unless explicitly requested.

## Transparency

Transparent PNG is the default output for this skill (see Required inputs above):
- output PNG with a real alpha channel;
- `inside-phone`: every pixel outside the outer phone silhouette must be transparent;
- `trompe-loeil`: every pixel outside the combined silhouette of phone + protruding Ada must be transparent;
- do not leave a black, gray, beige, white, checkerboard, vignette, glow, or shadow field around the cutout;
- verify corners and fine edges (hair strands, fingers crossing the bezel) are truly transparent, not merely visually dark or anti-aliased against a matching backdrop.

### How to actually verify transparency (don't just eyeball it)

A visual check against a white canvas can hide a translucent or off-color halo. Before delivery, composite the candidate PNG over two different solid colors (e.g. pure black and pure magenta) and confirm the silhouette edge looks identical against both — any visible fringe or shift means the alpha isn't clean. If you have file/shell access to the output, a quick pixel-level check works too: sample the four corners and a strip along the phone/Ada silhouette edge and confirm alpha == 0 outside the silhouette and alpha == 255 (or a clean, intentional anti-aliased gradient only right at the edge) elsewhere. Don't ship on "looks fine on a white background."

## Higgsfield MCP workflow

Prefer Higgsfield MCP for generation and iterative edits.

1. Use Higgsfield image generation directly with `nano_banana_pro` for general image/reference work unless another Higgsfield image model is specifically required.
2. Feed the human pose reference plus the locked Ada/studio/logo references — including both `westretch-logo-reference.png` and `westretch-logo-secondary-leg-reference.png` as explicit inputs, not just described in text, so the model has the actual art to trace.
3. Use reference images to preserve character, environment, and branding; do not train or invent a new Ada.
4. Generate one presentation mode at a time when precision matters.
5. If the user requests both modes, create two outputs:
   - inside-phone PNG;
   - trompe-l'oeil PNG.
   Each of those then needs both required sizes (see Output sizes) — up to four files per pose when both modes are requested.
6. Run targeted edits rather than regenerating the full composition when the user says "keep everything identical except…".
7. For exact-logo fixes, make the relevant logo reference (chest or leg) explicit and constrain the edit to that logo's region only — this is mandatory whenever § Logo's side-by-side check fails, not an optional nice-to-have.
8. For tone fixes, use the original Ada/studio references as the color anchor and constrain edits to color/lighting only.
9. Explicitly request true alpha transparency in the generation/edit prompt and run the verification steps above before delivery.
10. Canvas-fit each approved candidate to both required output sizes and save into `output/` using the filename pattern in Output folder.

## Prompt template — inside phone

Use this as a starting point, replacing bracketed fields:

> Create a polished WeStretch promotional PNG. Use the human pose reference to place Ada in **exactly** that stretch — same leg selection, same knee bend angle, same torso rotation, same arm path, same wrist and hand position, same head orientation — adapted only where literally required to stay anatomically correct on Ada's proportions. Preserve Ada exactly from the Ada reference assets: same face, same green eyes, same bob haircut, same skin tone, same stylized body proportions, and preserve her original charcoal/coral wardrobe. Ada must be inside the canonical WeStretch studio from studio-canonical.png. Present the result fully inside a realistic iPhone screen; no part of Ada may cross the bezel. Reproduce the chest logo exactly from the westretch-logo-reference.png file — one horizontal line, "WE" then "STRETCH", warped naturally to the fabric's curve but never re-lettered or restacked. If the upper-outer front of her left thigh, just below the waistband, is in frame, reproduce the leg logo exactly from westretch-logo-secondary-leg-reference.png in that exact spot; if that area isn't in frame, add no leg logo at all. Preserve the original studio/Ada color tone: warm neutral, natural wood and beige, no color cast. No app overlay UI, no extra text, no notification, no debug content. Make every pixel outside the phone fully transparent — true alpha channel, no halo or matte fringe. Output PNG, portrait orientation, then canvas-fit to [1320×2868 / 2064×2752].

## Prompt template — trompe-l'oeil

> Create a polished WeStretch trompe-l'oeil promotional PNG. Use the human pose reference to place Ada in **exactly** that stretch — same leg selection, same knee bend angle, same torso rotation, same arm path, same wrist and hand position, same head orientation — adapted only where literally required to stay anatomically correct on Ada's proportions. Preserve Ada exactly from the Ada reference assets: same face, same green eyes, same bob haircut, same skin tone, same stylized body proportions, and preserve her original charcoal/coral wardrobe. Ada must originate inside the canonical WeStretch studio shown in studio-canonical.png and remain visually connected to the phone screen, while selected limbs/body areas extend naturally beyond the iPhone bezel to create a convincing screen-breaking effect. Reproduce the chest logo exactly from the westretch-logo-reference.png file — one horizontal line, "WE" then "STRETCH", warped naturally to the fabric's curve but never re-lettered or restacked. If the upper-outer front of her left thigh, just below the waistband, is in frame, reproduce the leg logo exactly from westretch-logo-secondary-leg-reference.png in that exact spot; if that area isn't in frame, add no leg logo at all. Preserve the original studio/Ada color tone: warm neutral, natural wood and beige, no color cast. No app overlay UI, no extra text, no notification, no debug content. Make every pixel outside the combined phone + Ada silhouette fully transparent — true alpha channel, no halo or matte fringe. Output PNG, portrait orientation, then canvas-fit to [1320×2868 / 2064×2752].

## Revision discipline

When the user approves an image and requests a small change:
- use the approved image as the direct edit target;
- list the requested changes internally;
- explicitly say "change only these items" in the edit prompt;
- preserve pose, crop, phone geometry, studio geometry, character identity, facial expression, and all unmentioned elements.

Never silently redesign an approved image.

## Quality gate before delivery

Confirm visually, in this order:

1. **Pose fidelity** — ran the landmark-by-landmark side-by-side comparison against the human reference (see Pose matching); every landmark matches or a specific, necessary anatomical adaptation is noted.
2. **Identity** — Ada is recognizably the same character: same face, eyes, hair, skin tone, body proportions.
3. **Anatomy** — five fingers per hand, five toes if barefoot, joints bend correctly, no extra/missing/fused body parts, especially at any bezel-crossing seam.
4. **Studio** — is `studio-canonical.png`'s studio, tone matches originals, camera angle only has changed.
5. **Chest logo** — traced from `westretch-logo-reference.png`, single horizontal line, correct chest location, only warped by fabric curvature — not re-lettered or restacked.
6. **Leg logo** — if the upper-outer front-left-thigh zone is in frame, it's traced from `westretch-logo-secondary-leg-reference.png` in that exact spot; if that zone isn't in frame, confirm no leg logo was added anywhere else.
7. **UI** — no overlay UI unless requested; no accidental text/artifacts.
8. **Geometry** — phone edges clean, realistic device frame.
9. **Transparency** — if transparent, alpha is verified clean per the method above, around the entire silhouette, including hair strands and any limb crossing the bezel.
10. **Format and size** — output is PNG, delivered in both required sizes (see Output sizes), saved into `output/` with no distortion introduced by the resize/canvas-fit step.

If any of these fail, revise before presenting the result. A failed chest/leg logo check (see Known failure modes) is not a "note it and move on" item — fix it via the dedicated logo edit pass before continuing.

## Pre-delivery review gate (mandatory)

Passing the checklist above is necessary but not sufficient — it's a self-check, and there's no approved exemplar yet to catch what the checklist misses (see Known gaps). Before calling the task done:

1. Run through the Quality gate checklist explicitly, point by point.
2. Save the candidate (a single size is enough at this stage) into `waiting for approval/` (see Review staging folder above) and present it to the user with a short note on what to look at first (anything you were less confident about — a bezel-crossing hand, a tight crop on the leg-logo area, an unusual pose adaptation and why it was necessary).
3. Treat the task as **not complete** until the user confirms. Don't mark it delivered, don't move on to a next variant, and don't clean up/discard intermediate candidates until you have that confirmation.
4. On approval, canvas-fit to both required sizes (see Output sizes) and save both into `output/` following the naming pattern in Output folder.
5. Ask whether this should also be saved to `assets/approved-exemplars/` as a new reference point (see Known gaps) — this is how the skill accumulates the "perfect expected output" it doesn't have yet.
