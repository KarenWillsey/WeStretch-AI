# Hero Photo Corrections

- 2026-09-17: Generated desktop, tablet and mobile edits separately using built-in imagegen. Original source images remain unchanged.
- Requested changes: black crew-neck t-shirt, knee-length black shorts and naturally fuller legs. Preserve identity, expression, pose, phone, towel, AirPod, room and framing.
- The full identity reference failed tool decoding. Used an 800 x 800 inspection copy of the same reference.
- A second edit extended the shorts to the knees. Generated images were resized to the original source dimensions for WebP delivery. Desktop is upscaled from the generated image.
- 2026-09-17: Karen approved and applied. All three edits copied into `Team/CMO/Ready/website-repo/public/images/` as `actors-hero-desktop.webp`, `actors-hero-tablet.webp`, `actors-hero-mobile.webp` (overwritten in place, same dimensions as before). `src/pages/review.astro` `#hero` cache-busting query bumped `?v=2` → `?v=3`. See `Team/CMO/Ready/website-repo/review-actor-images.md` for the deploy-side log entry.

## Prompt set

First pass for each original crop: Edit image 1 using image 2 as canonical MALE ACTOR 01 identity reference only. Replace the tank top with a plain black crew-neck short-sleeve t-shirt covering shoulders and upper arms. Replace short shorts with knee-length black athletic shorts. Give naturally fit mature-toned fuller calves and thighs, realistic for a 60-year-old, neither bony nor bodybuilder. Preserve face, curly salt-and-pepper hair, light stubble, smile, expression, seated pose, elbow on raised knee, phone, yellow towel, AirPod, grey mat, room, lighting, camera angle and framing. No other changes, text, logos, watermarks or extra people. Preserve original aspect ratio and resolution.

Second pass for each generated crop: Extend both black shorts legs to the knees, covering the exposed thighs with loose natural fabric. Keep all other details unchanged.
