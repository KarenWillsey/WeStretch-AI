---
name: Ada-Stretching-Phone-Image
description: Create WeStretch marketing images of Ada performing a user-supplied human stretch pose, either fully contained inside an iPhone screen or using a trompe-l'oeil effect where Ada extends out of the phone. Preserve Ada, the WeStretch studio, branding, logo, color tone, and transparent PNG output requirements. Prefer Higgsfield MCP for generation/editing.
---

# Ada Stretching Phone Image

Use this skill whenever the user wants a WeStretch image that places **Ada** into a stretch pose shown by a human reference photo and presents her in or emerging from an iPhone.

## Core rule

Treat Ada, her outfit, the WeStretch studio, and the WeStretch logo as **locked brand assets**. The requested stretch pose, camera angle, phone presentation, crop, and output dimensions may change; the character identity and brand system must not drift.

## Required inputs per image

Ask only for missing information that cannot be inferred from the request:

1. **Pose reference** — one or more photos of a human performing the desired stretch.
2. **Presentation mode** — one of:
   - `inside-phone`: Ada remains completely inside the iPhone screen as a believable app screenshot.
   - `trompe-loeil`: Ada remains visually connected to the phone/studio but selected limbs or body parts extend beyond the phone bezel into the surrounding composition.
3. **Output format / aspect ratio** — default to PNG. If the user asks for a cutout, use true alpha transparency around the phone (or around phone + protruding Ada in trompe-l'oeil mode).

If the user omits the camera angle, choose the angle that best communicates the pose while preserving studio continuity.

## Locked reference assets

Use the files in `assets/` as follows:

### Ada identity and wardrobe
- `Ada_front.png` — primary face, front identity, hair, proportions, outfit.
- `Ada_back.png` — rear identity and wardrobe.
- `Ada_1.png`, `Ada_2.png`, `Ada_3.png` — additional facial/expression and body references.

Ada must keep:
- the same stylized 3D character identity;
- the same bob haircut and hair tone;
- the same face and proportions;
- the same charcoal athletic top and leggings with coral/red trim;
- the same shoe styling unless the user explicitly requests a wardrobe change.

### Studio
- `P.png` — canonical WeStretch studio. Ada must always be visually located in this studio.
- Camera angle may change, but architecture, materials, palette, lighting family, and recognizable studio details should remain consistent.

### Phone / composition examples
- `A(1).png` — primary example of Ada contained inside a phone.
- `B(1).png`, `C.webp`, `K.png`, `L.png` — trompe-l'oeil / screen-breaking references.
- `M.png`, `N.png` — human + phone relationship / promotional composition references.

### Logo
- `WeStretch_logo_reference.png` — **exact logo artwork reference**.

The logo on Ada's top must match this reference explicitly. Do not invent, abbreviate, restyle, substitute, or approximate the mark. Preserve letterforms, spacing, dot placement, and brand red. If the first generation distorts the mark, run a focused edit using the exact logo asset as the primary reference while changing nothing else.

## Color and lighting lock

The generated image must stay in the same tone family as the original Ada/studio references:
- warm-neutral studio light;
- natural pale-beige walls;
- warm wood floor and beams;
- neutral gray mat and stone/brick surfaces;
- Ada's original skin and hair tones;
- charcoal clothing with the original coral/red accents;
- no orange wash, hyper-saturation, cool-blue cast, crushed blacks, or cinematic recoloring unless explicitly requested.

When editing an existing approved image, preserve its geometry and composition and adjust only the requested items.

## Pose matching

The human reference defines biomechanics, not identity.

Match:
- front/back leg selection;
- knee bend and foot placement;
- torso rotation and lean;
- shoulder orientation;
- arm path;
- elbow and wrist positions;
- hand direction and grip/contact;
- head orientation when relevant.

Adapt only enough to make the pose anatomically clean on Ada's stylized proportions. Do not replace the pose with a generic stretch.

## Phone rules

### inside-phone
- Keep Ada, mat, and studio fully inside the display boundary.
- The iPhone must read as a real device frame.
- Default: **no overlay UI** unless the user explicitly asks for UI.
- No notification banners, debug console, fake status elements, captions, timers, progress bars, menu icons, or generated text.

### trompe-loeil
- Maintain a clear visual relationship between the phone screen and the studio image.
- Ada must appear to originate from the screen, not stand independently in front of it.
- Let only compositionally useful limbs/body areas break the bezel.
- Preserve realistic overlap, occlusion, scale, depth, and edge transitions.
- Default: **no overlay UI** unless explicitly requested.

## Transparency

When the user requests transparency:
- output PNG with a real alpha channel;
- `inside-phone`: every pixel outside the outer phone silhouette must be transparent;
- `trompe-loeil`: every pixel outside the combined silhouette of phone + protruding Ada must be transparent;
- do not leave a black, gray, beige, white, checkerboard, vignette, glow, or shadow field around the cutout;
- verify corners and fine edges are truly transparent, not merely visually dark.

## Higgsfield MCP workflow

Prefer Higgsfield MCP for generation and iterative edits.

1. Use Higgsfield image generation directly with `nano_banana_pro` for general image/reference work unless another Higgsfield image model is specifically required.
2. Feed the human pose reference plus the locked Ada/studio/logo references.
3. Use reference images to preserve character, environment, and branding; do not train or invent a new Ada.
4. Generate one presentation mode at a time when precision matters.
5. If the user requests both modes, create two outputs:
   - inside-phone PNG;
   - trompe-l'oeil PNG.
6. Run targeted edits rather than regenerating the full composition when the user says “keep everything identical except…”.
7. For exact-logo fixes, make the logo reference explicit and constrain the edit to the chest logo only.
8. For tone fixes, use the original Ada/studio references as the color anchor and constrain edits to color/lighting only.
9. If transparency is required, explicitly request true alpha transparency and inspect the result before delivery.

## Prompt template — inside phone

Use this as a starting point, replacing bracketed fields:

> Create a polished WeStretch promotional PNG. Use the human pose reference to place Ada in the same stretch, matching leg position, torso rotation, arms, wrists, hands, and head orientation. Preserve Ada exactly from the Ada reference assets and preserve her original charcoal/coral wardrobe. Ada must be inside the canonical WeStretch studio from P.png. Present the result fully inside a realistic iPhone screen; no part of Ada may cross the bezel. Use the exact WeStretch logo reference on Ada's top. Preserve the original studio/Ada color tone: warm neutral, natural wood and beige, no color cast. No app overlay UI, no extra text, no notification, no debug content. [If requested: make every pixel outside the phone fully transparent.] Output PNG, [aspect ratio].

## Prompt template — trompe-l'oeil

> Create a polished WeStretch trompe-l'oeil promotional PNG. Use the human pose reference to place Ada in the same stretch, matching leg position, torso rotation, arms, wrists, hands, and head orientation. Preserve Ada exactly from the Ada reference assets and preserve her original charcoal/coral wardrobe. Ada must originate inside the canonical WeStretch studio shown in P.png and remain visually connected to the phone screen, while selected limbs/body areas extend naturally beyond the iPhone bezel to create a convincing screen-breaking effect. Use the exact WeStretch logo reference on Ada's top. Preserve the original studio/Ada color tone: warm neutral, natural wood and beige, no color cast. No app overlay UI, no extra text, no notification, no debug content. [If requested: make every pixel outside the combined phone + Ada silhouette fully transparent.] Output PNG, [aspect ratio].

## Revision discipline

When the user approves an image and requests a small change:
- use the approved image as the direct edit target;
- list the requested changes internally;
- explicitly say “change only these items” in the edit prompt;
- preserve pose, crop, phone geometry, studio geometry, character identity, facial expression, and all unmentioned elements.

Never silently redesign an approved image.

## Quality gate before delivery

Confirm visually:
- Ada is recognizably the same character;
- the pose matches the human reference rather than a generic approximation;
- studio is the WeStretch studio and tone matches originals;
- chest logo follows the exact provided mark;
- no overlay UI unless requested;
- no accidental text/artifacts;
- phone edges and anatomy are clean;
- if transparent, alpha is real and clean around the entire silhouette;
- output is PNG.

If any of these fail, revise before presenting the result.
