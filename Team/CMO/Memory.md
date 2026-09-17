# CMO Memory

Persistent memory for the CMO role only: facts, feedback, and context that
apply across CMO's work but aren't specific to a single project (those live in
that project's own `Memory.md` under `Ideas/`, `In Progress/`, or `Ready/`).

## Review ToDo → Image Catalogue approval flow (set 2026-08-28, Karen)

Source-image generation skills (`female-actor-01-image-generator`,
`male-actor-01-image-generator`, `male-actor-02-image-generator`,
`westretch-ada-image-gen`) save every
reviewed candidate to `Team/CMO/Review ToDo/` by default, unchanged. What's
new: once Karen approves a candidate there, move the file into
`Team/CMO/Image Catalogue/`: a standing source-image archive, not a
delivery folder.

**Why:** Karen wants a single place holding only approved source images, so
future generations/compositing can pull from a trusted set instead of
searching `Review ToDo/` (which mixes approved and rejected candidates over
time).

**How to apply:** Applies only to the three general-purpose source-image
skills above. `ada-stretching-phone-image` and `app-store-image-creation`
keep their own project-specific staging (`waiting for approval/`, `output/`,
`assets/approved-exemplars/`); those pipelines produce finished, sized App
Store deliverables, not reusable source images, and Karen confirmed
(2026-08-28) not to fold them into this shared flow.

## Actor facial expression calibration (set 2026-09-10, Karen)

In generated actor images the face should read **pleasant but not overly
excited**. Target: soft eyes, smooth unfurrowed brow, relaxed jaw, and either
a faint natural half-smile or a warm neutral mouth. Two failure modes, both
rejected: a strained/frowning/stern face that reads as upset or angry (the
first `female-actor-03` render), and an overcorrected broad toothy grin,
which reads as staged stock photography.

**Why:** Karen's words, "she looks a little upset or angry", and separately
that over-excitement "is not natural". Effort in the body must never show as
strain in the face.

**How to apply:** Encoded in
`Team/CMO/skills/female-actor-03-image-generator/` (prompt template
photography section, negative prompt, and the review gate). The same rule
applies to `female-actor-03-image-generator` and, since 2026-09-10,
`male-actor-02-image-generator`, which was built after the calibration was
set and carries it from the start. Karen decided 2026-09-10 to leave
`female-actor-01-image-generator`, `female-actor-02-image-generator` and
`male-actor-01-image-generator` on their older "calm, focused expression"
line. Do not change those three. **Any new actor skill from here on gets the
calibration.**

## website-repo deploy command

Karen keeps this rule in `Team/CMO/Ready/website-repo/CLAUDE.md`'s
Commands section (the checked-in file, since it travels with that repo),
not here: see that file for the required `./build-deploy-hosting.sh`
deploy command.
