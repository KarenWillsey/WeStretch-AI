# Reference Map

Assets and delivered output for the `ada-stretching-phone-image` skill (instructions live at `Team/CMO/skills/ada-stretching-phone-image/SKILL.md`), kept here, alongside the rest of the App Store image work, for human browsability.

| File | Purpose | Notes |
|---|---|---|
| `ada-front.png` | Primary Ada identity reference, face, hair, proportions, full front wardrobe. | **Also the placement ground truth for both logos:** chest logo centered below the neckline; leg logo on the front upper-outer left thigh, just below the waistband, above the red side stripe. Use for face/hair/outfit/proportion lock too. |
| `ada-back.png` | Rear identity reference (hairstyle from behind, outfit back detail, red leg stripe. | Cropped 2026-08-11: the original capture had a live news-notification banner and a dev-build debug console baked into it (unrelated content, not brand-safe). Crop keeps only Ada and the shelf background. No logo is visible from behind) don't add one to a rear-facing pose. |
| `ada-expression-wave.png` | Torso-up cutout, waving/presenting gesture. | True alpha transparency; confirms the transparent-cutout quality bar this skill must hit. |
| `ada-expression-present.png` | Torso-up cutout, open-hand presenting gesture. | True alpha transparency. |
| `ada-expression-thumbsup.png` | Torso-up cutout, thumbs-up, big smile. | True alpha transparency. |
| `studio-canonical.png` | **The** canonical WeStretch studio: vaulted wood-beam ceiling, stone accent wall with backlit wordmark sign, arched windows, wood shelving, foam blocks/mats. | This is the only studio background to treat as locked. See caution on the two `ada-fullbody-alt-studio-*` files below. |
| `example-inside-phone-appstore-headline.png` | Full App Store screenshot template (marketing headline + checkmarks overlaid, human pose reference beside a phone with Ada fully inside (inside-phone mode). | Shows the overlay-UI marketing format. Overlay text/headline copy is **opt-in only**) don't treat this as the default look. |
| `example-inside-phone-neck-stretch.png` | inside-phone mode, no overlay text. Human doing a seated neck stretch; phone shows Ada fully contained, mirroring the pose. | Good default-mode reference (no UI chrome). |
| `example-trompe-loeil-knee-to-chest.png` | trompe-l'oeil; Ada's shoe/foot breaks the bottom bezel onto the real mat. | |
| `example-trompe-loeil-childs-pose.png` | trompe-l'oeil; Ada's forearms/hands break the bezel onto the real rug. | |
| `example-trompe-loeil-lunge.webp` | trompe-l'oeil; Ada's front foot breaks the bezel onto the real mat. | Cleanest edge-transition example; use as the primary trompe-l'oeil reference. |
| `ada-fullbody-alt-studio-cobra-1.png` | Full-body Ada, cobra-pose stretch. No phone, no human reference. | **Caution:** the lamp, wall art, and ceiling here do not match `studio-canonical.png`; this was rendered in a different environment. Use only for full-body proportions/wardrobe/shoe reference, never as studio-background guidance. |
| `ada-fullbody-alt-studio-cobra-2.png` | Same pose, alternate angle. | Same caution as above. |
| `westretch-logo-reference.png` | Exact **chest**-logo artwork: red "WE" + white "STRETCH" wordmark with red dots, transparent background. | Preview this on a dark canvas; the white lettering is invisible against white/light UI chrome, which can make the file look broken when it isn't. |
| `westretch-logo-secondary-leg-reference.png` | Exact **leg**-logo artwork: the "WE" mark alone (no "STRETCH"), transparent background, matches the small mark visible near the hem in `ada-back.png` / `ada-expression-wave.png`. | Supplied by Karen 2026-08-11. This is a *different, smaller* mark from the chest wordmark; don't substitute one for the other. |
| `ada-side-profile-leg-stripe-logo-reference.png` | Full-body side-profile of Ada mid-stretch (standing quad stretch against a wall). **The definitive reference for two wardrobe details a generation can otherwise get wrong:** (1) the red side stripe on the leggings runs the **full length of the leg**, waistband to ankle, not just the upper thigh; (2) the leg logo sits on the **front of the thigh**, small, near where the stripe begins, not on the hip, side, or glute. | Supplied by Karen 2026-08-11 to correct a generation that drifted the leg logo onto the hip/glute. Use alongside `ada-front.png` as placement ground truth. |
