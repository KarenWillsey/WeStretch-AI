# CMO Memory

Persistent memory for the CMO role only: facts, feedback, and context that
apply across CMO's work but aren't specific to a single project (those live in
that project's own `Memory.md` under `Ideas/`, `In Progress/`, or `Ready/`).

## Review ToDo → Image Catalogue approval flow (set 2026-08-28, Karen)

Source-image generation skills (`female-actor-01-image-generator`,
`male-actor-01-image-generator`, `westretch-ada-image-gen`) save every
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

## website-repo deploy command (set 2026-09-01, Karen)

When Karen says "deploy to Firebase" / "push to Firebase" for
`Team/CMO/Ready/website-repo` (the Astro site, submodule
`westretch-website-astro`), run from inside that folder:

```
npm run build
firebase deploy --only hosting:website-dev --project westretch-prod
```

or equivalently `./build-deploy-hosting.sh`. This publishes to the dev
site at https://westretch-website-dev.firebaseapp.com/ (also reachable at
https://westretch-website-dev.web.app). Firebase CLI is already installed
and logged in as karen.westretch@gmail.com on Karen's machine, no login
step needed there. `.firebaserc` targets Firebase project `westretch-prod`,
hosting target `website-dev` → site `westretch-website-dev`.

**Why:** Karen doesn't know the Firebase workflow herself and wants this
run automatically on request rather than re-explained each time.

**How to apply:** Any request like "deploy/push the website/site to
Firebase" with no other target named should be read as this command
against `website-repo`. If a different Firebase target or site is ever
meant, confirm before running; this default is specific to
`website-dev`/`westretch-prod`.
