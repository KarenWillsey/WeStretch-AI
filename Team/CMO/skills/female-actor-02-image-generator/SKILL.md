---
name: female-actor-02-image-generator
description: Use when the user says "create image of female actor 02 in pose ...", asks to generate Female Actor 02 in a dynamic or specified pose, or requests another image of Female Actor 02. Generate a photorealistic 3:4 lifestyle image using the bundled identity reference while preserving the actor and, by default, the wardrobe, outdoor patio/lawn setting, lighting, and clean App Store source-photo composition. Apply an explicitly requested scene or wardrobe change narrowly. Save reviewed outputs to Team/CMO/Review ToDo/ unless the user specifies another destination.
---

# Female Actor 02 Image Generator

Generate the requested image directly. Do not return only a suggested prompt.
Treat the user's pose description as the required dynamic input. Keep every
other property locked by default, but honor an explicit user-requested change
such as `indoors` by overriding only the conflicting lock.

## Canonical resources

- Identity image: `assets/female-actor-02-reference.png`
- Supplementary face reference (close-up, for identity confirmation only —
  not a scene or wardrobe reference): `assets/female-actor-02-headshot-a.png`
  and `assets/female-actor-02-headshot-b.png`
- Prompt: `references/prompt-template.md`
- Identity image SHA-256:
  `50EA292184500CEFD743985FBB03AFE9308EA8B9A8CB759378560D05E48D6129`

Read the prompt reference fully before generating. Always attach
`assets/female-actor-02-reference.png` to the image-generation or
image-editing request as the identity anchor. Use the two headshot images
only as an extra facial-identity check when reviewing a candidate. Never
attempt to reproduce this actor from text alone and never substitute another
woman.

## Extract the pose

Interpret the wording after phrases such as `in pose`, `doing`, `performing`,
or `in a` as `{{POSE}}`.

Example:

```text
Create image of Female Actor 02 in pose kneeling low lunge stretch, looking up.
```

Use this pose value:

```text
Kneeling low lunge stretch, chest lifted, looking up.
```

If the pose is clear, proceed without asking questions. If no pose is given,
ask for one concise pose description and stop.

## Generate

1. Inspect `assets/female-actor-02-reference.png` before the first generation.
2. Replace `{{POSE}}` in `references/prompt-template.md` with the user's pose.
   Keep every identity, wardrobe, setting, lighting, composition, and output
   constraint unchanged unless the user explicitly overrides one. In that
   case, modify only the conflicting prompt lock and preserve all others.
3. Use the image tool in reference-image or edit mode with the canonical asset
   as the identity anchor. Set identity/reference preservation high when the
   tool exposes that control.
4. Generate one clean, photorealistic, vertical 3:4 source photograph. Request
   3072 by 4096 pixels when the tool supports exact dimensions. Otherwise use
   its highest-quality 3:4 output and report the actual size.
5. Do not add the WeStretch logo, typography, fade, captions, UI, or other
   branding. Those belong to the deterministic App Store compositing stage.

## Review before presenting

Inspect the generated candidate and compare it with the canonical reference
(and, for facial detail, the two headshot images). Regenerate or make a
targeted correction before showing it if any check fails:

- The face reads as a different woman.
- Apparent age, facial proportions, short choppy dark-brown layered hair with
  lift at the crown, complexion, body type, black crew-neck short-sleeve top,
  dark floral-patterned leggings, or bare feet drift from the reference.
- The gold multi-circle-link necklace, drop earrings, black fitness-tracker
  watch, or thin wrist bangle is missing or changed.
- The requested pose is inaccurate or biomechanically implausible.
- Hands, fingers, feet, joints, limb count, balance, or weight-bearing are
  malformed.
- The head or hair is cropped, or the framing prevents the full pose from
  being understood.
- Unless explicitly overridden, the stone-paver patio, teal blue yoga mat,
  bordering grassy lawn, tree line, hazy overcast daylight, 3:4 style, or
  upper negative space changes materially.
- Text, logos, watermarks, extra people, device frames, or UI appear.

## Output location

- Save every reviewed image to `Team/CMO/Review ToDo/` by default.
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

Once Karen approves the image, move it from `Team/CMO/Review ToDo/` into
`Team/CMO/Image Catalogue/` (skip this step if the user saved to a different
destination). Leave rejected or superseded candidates in `Review ToDo/`, or
delete them — they never move to `Image Catalogue/`.

## Revisions

Use the previously approved candidate as the edit target. Change only the
newly requested pose detail and preserve every unmentioned element. Re-run the
same review before presenting the revision.
