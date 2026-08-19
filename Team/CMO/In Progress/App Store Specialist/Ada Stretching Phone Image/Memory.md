# Ada Stretching Phone Image — Memory

Folded in from this project's former `SESSION_NOTES.md` (2026-08-11 session
that Karen called "an epic failure" — kept so the next session doesn't
repeat the same detours).

## What actually got done (kept, not wasted)

- `Team/CMO/skills/ada-stretching-phone-image/SKILL.md` was updated: leg logo
  placement clarified (front of thigh, not hip/glute), leg stripe documented
  as full-length (waistband to ankle), a "Known failure modes" entry logged,
  and the `waiting for approval/` staging-folder convention added.
- Locked reference asset added: `assets/ada-side-profile-leg-stripe-logo-reference.png`
  (documented in `reference-map.md`) — ground truth for leg logo + stripe
  placement.

**None of the generated output from that session should be reused.** Every
candidate was rejected — start image generation completely fresh, using the
skill and reference assets above, not any prior attempt.

## Standing lessons (apply every time)

1. **Confirm the pose reference photo actually matches the intended stretch
   before generating anything.** The 2026-08-11 session burned a full
   generation cycle on the wrong pose (a different stretch than Karen
   wanted) before she supplied a corrective photo.
   - **Why:** wrong-pose generation wastes credits and a full review cycle.
   - **How to apply:** ask Karen to confirm the pose reference before
     starting if there's any doubt.

2. **Neither `nano_banana_pro` nor `gpt_image_2` outputs true alpha
   transparency**, regardless of prompt wording — every generation comes
   back fully opaque (alpha=255) with a flat gray field standing in for
   "transparent." The Read-tool preview renders this as a misleading
   checkerboard.
   - **Fix that worked:** a local post-process (flood-fill the background
     from the image border using a low-saturation/high-brightness mask,
     dilate, then Gaussian-blur the mask edge for antialiasing) reliably
     produces clean true-alpha PNGs at zero extra Higgsfield cost.
   - **How to apply:** always verify by sampling raw alpha at the four
     corners/edges and by compositing over two contrasting solid colors
     (black and magenta) to check the silhouette edge matches on both — not
     by eyeballing the preview.

3. **Model choice matters a lot for logo/text fidelity.** `nano_banana_pro`
   (2 credits/gen) repeatedly mangled the chest and leg logos (wrong
   orientation, mirrored, missing letters, invented dots) even across
   correction passes. `gpt_image_2` (7 credits/gen, `quality: high`) fixed
   logo fidelity dramatically in one pass.
   - **How to apply:** go straight to `gpt_image_2` for anything involving
     the exact wordmark/logo artwork; don't burn cycles on `nano_banana_pro`
     logo corrections.

4. **Multi-reference "edit" prompts can hijack the whole image.** An edit
   prompt with several reference images (base candidate + multiple
   brand/pose refs) asking for a small localized fix once made the model
   discard the base image's pose entirely and regenerate toward whichever
   reference was visually strongest.
   - **Fix that worked:** for small, localized corrections, pass *only* the
     single base candidate as the reference and describe the fix very
     narrowly ("pixel-identical except X"). Save multi-reference prompts for
     full regenerations, not surgical edits.

5. **Defects hide at full-image scale.** A garbled text artifact near the
   leg logo, a mirrored leg logo, and missing dots were all invisible at
   normal viewing size and only showed up under 2-3x cropped zoom.
   - **How to apply:** always crop-and-zoom the hands, both logos, and the
     phone silhouette edges before presenting a candidate — don't just
     glance at the full image.

6. **Check credit budget before starting.** The account was once down to 2
   credits (one generation's worth) mid-task, forcing a top-up mid-session.
   A single logo/pose correction cycle costs roughly 2-16 credits depending
   on model and pass count; six attempts in the 2026-08-11 session used
   about 32 credits total.
   - **How to apply:** check `higgsfield account status` at the start of any
     image-generation task and give Karen a realistic credit estimate before
     generating.

## Suggested prompt for starting a fresh generation

```
Start a fresh Ada figure-4 stretch inside-phone image using the
ada-stretching-phone-image skill. This is a clean start -- do not
reuse, reference, or build on any prior candidate image; all earlier
output was rejected. Before generating anything:

1. Read this Memory.md for what went wrong last time and what to avoid.
2. Confirm the pose reference photo actually matches the intended
   stretch (a figure-4 / IT-band stretch: one leg bent with the knee
   pulled to the chest, the other ankle crossed and resting near that
   knee, both hands wrapped behind the bent thigh) before generating
   anything -- ask Karen to confirm if there's any doubt.
3. Use gpt_image_2 (not nano_banana_pro) for the generation, since
   logo/wordmark fidelity matters and nano_banana_pro repeatedly
   mangled it last time.
4. Feed the skill's reference assets, including
   assets/ada-side-profile-leg-stripe-logo-reference.png for leg logo
   and stripe placement.
5. If a correction pass is needed afterward, pass ONLY the single
   candidate being corrected as the image reference and describe the
   fix narrowly ("pixel-identical except X") -- including other
   brand-reference images in that same edit call caused the model to
   regenerate the whole pose instead of editing it, last time.
6. Check account credits first (`higgsfield account status`) and tell
   Karen the balance before generating.
7. Whatever comes out, verify it by (a) cropping and zooming both
   logos, both hands, and the phone edge before showing it to Karen,
   and (b) checking the raw alpha channel at the corners/edges in
   Python/PIL, not just eyeballing the preview -- neither
   nano_banana_pro nor gpt_image_2 outputs real transparency by
   default, so plan to background-remove locally and re-verify alpha
   before calling anything "transparent."

Goal: a candidate that passes the full quality gate, get Karen's explicit
approval, then canvas-fit to both required output sizes and save into
output/.
```
