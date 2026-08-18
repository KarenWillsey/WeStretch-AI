---
name: create-4k-crop-master
description: Create or edit a portrait photograph into a flexible 4K crop master for App Store and marketing layouts. Use when the user asks for a "4K master for cropping," extra padding or crop room around people, one image suitable for both iPad and iPhone crops, a larger uncropped source, safer framing around a human, or improved subject lighting while preserving identity. Produce a clean 3:4 PNG master at 3072 × 4096 pixels unless the user specifies another master format.
---

# Create a 4K Crop Master

Turn the selected source photograph into one flexible, text-free master that a designer can crop for multiple portrait layouts.

## Required output

- Deliver a portrait PNG at exactly **3072 × 4096 pixels** (3:4).
- Treat this as the master for the **2064 × 2752 iPad** crop and the narrower **1320 × 2868 iPhone** crop.
- Preserve real photographic detail while outpainting. If the image tool returns a smaller 3:4 image, resize the approved result to exactly 3072 × 4096 with high-quality Lanczos resampling.
- Save non-destructively with a descriptive filename ending in `-4k-crop-master.png`.

## Composition

- Expand the scene on **all four sides**; do not merely upscale the existing crop.
- Make the complete human action comfortably smaller within the frame. Include the person plus anything functionally attached to the action, such as a paddle, ball, equipment, shoes, extended limbs, and cast shadow.
- Add generous, believable padding above, below, left, and right so both 3:4 and narrow phone crops remain possible.
- Keep critical action near the shared center-safe region. Do not place indispensable details near either side edge.
- Extend the existing environment with coherent perspective, depth of field, textures, court or floor markings, foliage, sky, and shadows.

## Identity and content preservation

- Use the exact user-selected image as the edit target.
- Preserve the subject as closely as possible: face, expression, age, hair, skin tone, body, pose, anatomy, clothing, equipment, and action moment.
- Do not beautify, redesign, replace, or materially reposition the person unless the user requests it.
- Preserve the original location and visual style unless the user requests a background change.
- Remove text, logos, branding, watermarks, frames, and graphic overlays by default. Reconstruct the photograph behind them naturally.
- Do not add people or unrelated objects.

## Lighting

- Inspect the subject for deep facial or body shade.
- When needed, add broad, soft, natural frontal fill light, as from a large reflector near the camera.
- Open shadows across the eyes, face, neck, clothing, arms, and legs while retaining believable outdoor directionality and dimensional modeling.
- Preserve natural skin texture. Avoid flat lighting, clipped highlights, artificial studio light, excessive HDR, or mismatched shadows.

## Workflow

1. Load and inspect the exact selected source image.
2. Use the built-in image editing tool with the source as the edit target.
3. Explicitly request identity preservation, four-sided outpainting, crop-safe composition, text removal, and any needed lighting correction.
4. Inspect the result for identity drift, missing anatomy or equipment, edge crowding, unwanted text, inconsistent perspective, and lighting artifacts.
5. Iterate with one targeted correction if a critical requirement fails.
6. Verify the final pixel dimensions. Resize only after the visual edit is approved.
7. Return the finished PNG with a clickable file link and briefly state its dimensions and crop purpose.

## Prompt core

Use language equivalent to:

> Create a clean 3:4 portrait master for delivery at 3072 × 4096. Outpaint on all four sides and make the complete subject action smaller within the canvas, with generous safe padding for both 2064 × 2752 iPad and 1320 × 2868 iPhone crops. Preserve the person's identity, face, body, pose, clothing, equipment, and action. Add soft natural frontal fill light where needed to open deep shadows. Keep the scene photorealistic. No text, logos, branding, watermarks, borders, new people, or cropped action details.

Honor any user instruction that overrides these defaults.
