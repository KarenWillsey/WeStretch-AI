---
name: male-actor-02-image-generator
description: Use when the user says "create image of male actor 02 in pose ...", asks to generate Male Actor 02 in a dynamic or specified pose, or requests another image of Male Actor 02. Generate a photorealistic 3:4 lifestyle image using the bundled identity reference while preserving the actor and, by default, the wardrobe, right-knee brace, bright classic living room, lighting, and clean App Store source-photo composition. Apply an explicitly requested scene or wardrobe change narrowly. Save reviewed outputs to Team/CMO/Review ToDo/ unless the user specifies another destination.
---

# Male Actor 02 Image Generator

Generate the requested image directly. Do not return only a suggested prompt.
Treat the user's pose description as the required dynamic input. Keep every
other property locked by default, but honor an explicit user-requested change
such as `outdoors` by overriding only the conflicting lock.

## Canonical resources

- Identity image: `assets/male-actor-02-reference.png`
- Supporting outdoor reference: `assets/male-actor-02-reference-outdoor-walk.png`
- Prompt: `references/prompt-template.md`
- Identity image SHA-256:
  `39D3E05E38867260FC64B8F1D13905CD4FF15C7235ACE5C5F07B1B0BE94C6AF5`
- Outdoor reference SHA-256:
  `29C8322F7638D56903FC74014DC9C7FE12933D7C89FEB0EA0409A7A21EFC4731`

Read the prompt reference fully before generating. Always attach the bundled
identity image to the image-generation or image-editing request. Never attempt
to reproduce this actor from text alone and never substitute another man.

## Reference assets

`assets/male-actor-02-reference.png` is the single identity anchor for this
actor: the solo seated-in-an-armchair-with-phone source photograph in the
bright classic living room. If that file is missing, stop and ask for it
rather than generating from the text description alone; the text locks below
describe the reference, they do not replace it.

`assets/male-actor-02-reference-outdoor-walk.png` is a supporting reference
only. It shows the same man walking a tree-lined path with a woman and a small
child. Attach it in addition to the identity anchor when the user asks for an
outdoor or walking scene, or when a second angle of his face, hair, wardrobe,
or knee brace helps. Never attach it alone, and never carry the woman or the
child into a generated image unless the user explicitly asks for them.

## Extract the pose

Interpret the wording after phrases such as `in pose`, `doing`, `performing`,
or `in a` as `{{POSE}}`.

Example:

```text
Create image of Male Actor 02 in pose seated hamstring stretch on the edge of a chair.
```

Use this pose value:

```text
Seated on the front edge of a chair with one leg extended, heel on the floor,
hinging forward from the hips into a hamstring stretch.
```

If the pose is clear, proceed without asking questions. If no pose is given,
ask for one concise pose description and stop.

## Generate

1. Inspect `assets/male-actor-02-reference.png` before the first generation.
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

Inspect the generated candidate and compare it with the canonical reference.
Regenerate or make a targeted correction before showing it if any check fails:

- The face reads as a different man.
- Apparent age, facial proportions, short silver-grey side-parted hair,
  clean-shaven jaw, complexion, body type, navy quarter-zip long-sleeve
  pullover, light grey shorts, or blue-and-grey running shoes drift from the
  reference.
- The black hinged brace is missing from his right knee, has moved to the left
  knee, has changed colour or style, or has drifted into a bandage, wrap,
  sleeve, or medical cast.
- His expression reads as strained, frowning, scowling, stern, pained, tense,
  upset, or angry. Effort in the body must never show as strain in the face.
- His expression overcorrects into a broad grin, a toothy laugh, or
  exaggerated delight. The target is warm and relaxed: soft eyes, smooth
  brow, an easy natural smile or warm neutral mouth.
- The requested pose is inaccurate or biomechanically implausible.
- Hands, fingers, feet, joints, limb count, balance, or weight-bearing are
  malformed.
- The head or hair is cropped, or the framing prevents the full pose from
  being understood.
- Unless explicitly overridden, the bright classic living room, the cream
  armchair, the round cream rug on warm hardwood, the white fireplace and
  built-in shelving, the soft daylight from the camera-left window, the 3:4
  style, or the upper negative space changes materially.
- Text, logos, watermarks, extra people, device frames, or UI appear. A phone
  in his hand is allowed only when the requested pose calls for one, and it
  must stay screen-blank with no visible interface.

## Output location

- Save every reviewed image to `Team/CMO/Review ToDo/` by default.
- Use a different folder only when the user explicitly specifies one.
- Create the destination folder when it does not exist.
- Honor the user's requested file format. If none is specified, use PNG.
- Use a descriptive lowercase kebab-case filename based on the pose, setting,
  and orientation when relevant.
- Never overwrite an existing file by default. Add `-v2`, `-v3`, and so on
  when a filename already exists.
- Treat `Team/CMO/Image Catalogue/` as append-only. Never overwrite or replace
  a catalogue image, even when a revision is requested. If a destination name
  already exists there, preserve it and use the next available version suffix.
- Do not leave a project-bound final only in the image tool's generated-images
  directory.

After the candidate passes review, save it to the destination and present it
for user approval. Never place an unreviewed generation in an App Store
`Output/` folder.

Once Karen approves the image, move it from `Team/CMO/Review ToDo/` into
`Team/CMO/Image Catalogue/` (skip this step if the user saved to a different
destination). Leave rejected or superseded candidates in `Review ToDo/`, or
delete them; they never move to `Image Catalogue/`.

## Revisions

Use the previously approved candidate as the edit target. Change only the
newly requested pose detail and preserve every unmentioned element. Save the
revision outside `Image Catalogue/`, re-run the same review, and present it for
approval. Once approved, add it to the catalogue as a new image with a unique
filename; never replace the original catalogue file.
