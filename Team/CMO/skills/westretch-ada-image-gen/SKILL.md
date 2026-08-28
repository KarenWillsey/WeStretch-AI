---
name: westretch-ada-image-gen
description: Generate or edit images of the WeStretch Ada fitness avatar when the user asks for Ada in a pose, stretch, exercise, or workout image, such as "Create an image of Ada in Pose XYZ."
metadata:
  short-description: Generate Ada pose images
---

# WeStretch Ada Image Generation

Use this skill when the user asks to create, edit, or prompt an image of Ada, especially phrasing like "Create an image of Ada in Pose XYZ", "Ada doing a hamstring stretch", or "make Ada in this exercise pose."

## Reference Assets

Use the bundled references to preserve Ada's character identity and image style:

- `assets/Ada_StraddleSide_R.png`: seated side straddle stretch, three-quarter side view.
- `assets/Ada_DeepLungeShldrStretch_frontViiew.png`: front-facing kneeling lunge with cross-body shoulder stretch.
- `assets/Ada_CrossLegs_NeckSideStretch.png`: cross-legged seated neck side stretch, closer upper-body framing.
- `assets/Ada_BirdDog.png`: bird-dog pose, side/top three-quarter view.

When an image-generation tool accepts reference images, include all four assets by default for character consistency unless the user explicitly asks to use only one reference. Use the requested pose or exercise as the pose target, not as permission to change Ada's design.

## Ada Character Guide

Ada is a stylized 3D fitness avatar for WeStretch:

- young adult woman with fair skin, soft friendly face, green eyes, and a short light-brown bob haircut with subtle highlights.
- athletic but approachable build, realistic stretch anatomy, calm expression, and gentle wellness-coach energy.
- navy sleeveless crop athletic top with coral-red trim and subtle WeStretch wordmark styling.
- navy high-waisted leggings with coral-red waistband and coral side accents.
- barefoot, no shoes, no extra jewelry, no props unless requested.
- polished 3D render look with smooth skin shading, clean studio lighting, rounded forms, and a premium app-avatar finish.

## Image Defaults

Unless the user specifies otherwise, generate Ada as a full-body or mostly full-body isolated character render on a transparent or plain black background, matching the reference images. Keep the pose readable and anatomically plausible for a fitness/stretching app. When the user asks for transparency, require true alpha transparency: no checkerboard, grid, white/gray stand-in, black fill, or fake transparency pattern.

Prefer these defaults in prompts:

- square canvas.
- single Ada character only.
- clean, centered composition with enough margin around extended limbs.
- no text, labels, watermarks, logos, UI, furniture, yoga mats, transparency grids, checkerboards, or environment.
- no photoreal human, anime redesign, mascot redesign, childlike proportions, exaggerated body shape, or altered outfit colors.

## Prompt Pattern

For a new pose, adapt this structure:

```text
Create a polished stylized 3D render of Ada, the WeStretch fitness avatar, performing [requested pose]. Preserve her reference identity: short light-brown bob haircut with highlights, fair skin, green eyes, friendly calm expression, navy athletic crop top with coral trim, navy leggings with coral waistband and side accents, barefoot. Full-body isolated character render, centered square composition, clean studio lighting, transparent or plain black background, no text, no props, no environment. If transparent output is requested, use true alpha transparency with no checkerboard/grid/fake transparency pattern, and preserve only a soft semi-transparent contact shadow where Ada touches the ground. Make the pose anatomically plausible and clearly readable for a stretching/workout app.
```

If the user asks for a named pose that could be ambiguous, infer the common fitness/stretch version and generate it. Ask a concise clarification only when the body position, facing direction, or output use would materially change the result.

## Output location

- Save every generated candidate to `Team/CMO/Review ToDo/` by default. Use a different folder only when the user explicitly specifies one.
- Present it there for Karen's review before treating the task as done.
- Once Karen approves the image, move it from `Team/CMO/Review ToDo/` into `Team/CMO/Image Catalogue/` (skip this step if the user saved to a different destination). Leave rejected or superseded candidates in `Review ToDo/`, or delete them — they never move to `Image Catalogue/`.
- Use a descriptive lowercase kebab-case filename based on the pose (e.g. `ada-standing-quad-stretch.png`). Never overwrite an existing file unless explicitly asked — add `-v2`, `-v3`, etc. instead.
