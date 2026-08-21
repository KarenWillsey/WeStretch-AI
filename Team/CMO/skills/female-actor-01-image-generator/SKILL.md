---
name: female-actor-01-image-generator
description: Use when the user says "create image of female actor 01 in pose ...", asks to generate Female Actor 01 in a dynamic or specified pose, or requests another image of Female Actor 01. Generate a photorealistic 3:4 lifestyle image using the bundled identity reference while changing only the requested pose and preserving the actor, wardrobe, room, lighting, and clean App Store source-photo composition. Save reviewed outputs to Team/CMO/Review unless the user specifies another destination.
---

# Female Actor 01 Image Generator

Generate the requested image directly. Do not return only a suggested prompt.
Treat the user's pose description as the single dynamic input.

## Canonical resources

- Identity image: `assets/female-actor-01-reference.png`
- Prompt: `references/prompt-template.md`
- Identity image SHA-256:
  `B5563E679E06FDCD111E288EEDF2FF6C4E2B8261A8BD8F6A1F214F965D5B3B68`

Read the prompt reference fully before generating. Always attach the bundled
identity image to the image-generation or image-editing request. Never attempt
to reproduce this actor from text alone and never substitute another woman.

## Extract the pose

Interpret the wording after phrases such as `in pose`, `doing`, `performing`,
or `in a` as `{{POSE}}`.

Example:

```text
Create image of Female Actor 01 in pose standing calf stretch against a wall.
```

Use this pose value:

```text
Standing in a calf stretch against a wall.
```

If the pose is clear, proceed without asking questions. If no pose is given,
ask for one concise pose description and stop.

## Generate

1. Inspect `assets/female-actor-01-reference.png` before the first generation.
2. Replace only `{{POSE}}` in `references/prompt-template.md` with the user's
   pose. Keep every identity, wardrobe, setting, lighting, composition, and
   output constraint unchanged.
3. Use the image tool in reference-image or edit mode with the canonical asset
   as the identity anchor. Set identity/reference preservation high when the
   tool exposes that control.
4. Generate one clean, photorealistic, vertical 3:4 source photograph. Request
   3072 by 4096 pixels when the tool supports exact dimensions. Otherwise use
   its highest-quality 3:4 output and report the actual size.
5. Do not add the WeStretch logo, typography, fade, captions, UI, or other
   branding. Those belong to the deterministic App Store compositing stage.

## Review before presenting

Inspect the generated candidate and compare it with the canonical reference.
Regenerate or make a targeted correction before showing it if any check fails:

- The face reads as a different woman.
- Apparent age, facial proportions, salt-and-pepper bob, complexion, body type,
  sage-green shirt, charcoal-grey pants, or bare feet drift from the reference.
- The requested pose is inaccurate or biomechanically implausible.
- Hands, fingers, feet, joints, limb count, balance, or weight-bearing are
  malformed.
- The head or hair is cropped, or the framing prevents the full pose from
  being understood.
- The living room, warm camera-left daylight, 3:4 style, or upper negative
  space changes materially.
- Text, logos, watermarks, extra people, device frames, or UI appear.

## Output location

- Save every reviewed image to `Team/CMO/Review/` by default.
- Use a different folder only when the user explicitly specifies one.
- Create the destination folder when it does not exist.
- Honor the user's requested file format. If none is specified, use PNG.
- Use a descriptive lowercase kebab-case filename based on the pose, setting,
  and orientation when relevant.
- Never overwrite an existing file unless the user explicitly requests it.
  Add `-v2`, `-v3`, and so on when a filename already exists.
- Do not leave a project-bound final only in the image tool's generated-images
  directory.

After the candidate passes review, save it to the destination and present it
for user approval. Never place an unreviewed generation in an App Store
`Output/` folder.

## Revisions

Use the previously approved candidate as the edit target. Change only the
newly requested pose detail and preserve every unmentioned element. Re-run the
same review before presenting the revision.
