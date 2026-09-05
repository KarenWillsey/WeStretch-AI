# Team/CMO/CLAUDE.md

Scope: this folder is the CMO's isolated workspace, brand, marketing, and
App Store asset/copy work. Read this file (and `Team/CMO/Memory.md`) whenever
working here; cross-role conventions live in the repo root `CLAUDE.md`.

## Mandate

Brand, marketing, and App Store presence for WeStretch, screenshot/asset
creation, App Store copywriting, and campaign work (email funnels, radio,
website copy).

## Skills

- `Team/CMO/skills/westretch-core/`: shared brand personas, strategic thesis, and
  guardrails other CMO skills depend on; load this first.
- `Team/CMO/skills/ada-stretching-phone-image/`: Ada (brand character) stretching
  phone-image generation.
- `Team/CMO/skills/westretch-ada-image-gen/`: general-purpose Ada pose image
  generation (any pose/exercise, isolated character render), reference-locked
  to the four bundled Ada pose assets. For App Store phone-composited images
  specifically, use `ada-stretching-phone-image` instead.
- `Team/CMO/skills/app-store-image-creation/`: App Store screenshot pipeline.
- `Team/CMO/skills/create-4k-crop-master/`: source-image crop mastering.
- `Team/CMO/skills/female-actor-01-image-generator/` - reference-locked lifestyle
  image generation for Female Actor 01 in a user-supplied pose.
- `Team/CMO/skills/female-actor-02-image-generator/` - reference-locked lifestyle
  image generation for Female Actor 02 (outdoor patio/lawn reference) in a
  user-supplied pose.
- `Team/CMO/skills/male-actor-01-image-generator/` - reference-locked lifestyle
  image generation for Male Actor 01 (outdoor pickleball-court reference) in a
  user-supplied pose.
- `.claude/skills/cmo-app-store-image-creation/`: CMO-persona review/guidance
  companion to the app-store-image-creation pipeline; discoverable as a slash
  command (see the root `CLAUDE.md` "Known issue" note on why this lives under
  `.claude/skills/` instead of `Team/CMO/skills/`).
- `.claude/skills/cmo-jamie-meeting-notes/`: updates the running WeStretch
  team action-item list from Karen/Jamie Zoom transcripts; writes dated
  output to `Team/CMO/In Progress/Jamie Meeting Notes/Output/`.

The original `brand-messaging-review`, `campaign-planning`, and `jokes`
SKILL.md files were removed from this folder; the App Store image-creation
work above replaced them as CMO's active output. Restore or rewrite those if
that generic review/planning function is needed again.

## Website changes

When Karen asks to make changes to the website, the code lives in
`Team/CMO/Ready/website-repo` (git submodule, Astro app; see its own
`CLAUDE.md` for that codebase's conventions). Before editing:

1. `cd` into `Team/CMO/Ready/website-repo`.
2. Start the local dev server so the site can be viewed while working:
   `npm run dev` (Astro dev server). Check for an already-running dev
   server/port first; if one's already up, reuse it instead of starting
   a second one.
3. Make the change, then verify it in the browser against the running
   dev server (and check responsive breakpoints per that repo's
   `CLAUDE.md`: every styling/markup change must work on mobile,
   tablet, and desktop, not just the window it was eyeballed at).

If `Ready/website-repo/` is empty, run `git submodule update --init
--recursive` from the repo root first.

## Project pipeline

- `Review ToDo/` - shared staging area for reviewed CMO image assets awaiting
  Karen's approval. `female-actor-01-image-generator`,
  `female-actor-02-image-generator`, `male-actor-01-image-generator`, and
  `westretch-ada-image-gen` all save here by default. Mixed approved/rejected over time; once Karen approves a
  candidate, move it to `Image Catalogue/` (see below); don't leave approved
  images sitting in this folder.
- `Image Catalogue/` - standing archive of **approved** source images only,
  moved here from `Review ToDo/` once Karen signs off. Not a delivery
  folder, finished, sized App Store exports still go through their own
  project `output/` folders. See `Team/CMO/Memory.md` for the full rule and
  which skills it applies to.
- `Ideas/App Stores/App Store Keyword Creation/`: not yet started (empty).
- `In Progress/`: active initiatives, each with its own `CLAUDE.md` + `Memory.md`:
  - `App Store Specialist/`: has its own `CLAUDE.md` orienting across its
    sub-projects (grouping folder, not a project itself):
    - `App Store Specialist/Ada Stretching Phone Image/`
    - `App Store Specialist/App Store Image Creation/`
    - `App Store Specialist/App Store Image Text Copywriting/`
    - `App Store Specialist/Apple Opportunity Radar/`: **planning spec
      only, not built** (2026-08-21): a standing capability to track every
      Apple App Store marketing lever, refresh monthly from
      developer.apple.com, and work a nightly opportunity backlog. See its
      `Implementation Spec.md` before building/scheduling anything.
    - `App Store Specialist/App Store Description Copywriting/`: stub, no content yet.
  - `Email Funnels Specialist/`
  - `Website/`: stub folder, no content yet.
  - `Jamie Meeting Notes/Output/`: dated running action-item lists produced
    by the `cmo-jamie-meeting-notes` skill (`.claude/skills/`); this folder
    holds output only, not a skill definition; not given a memory pair.
  - `Radio Specialist/5 x 30 second radio copy/`: generates a fresh batch
    of 5 new 30-second radio scripts on distinct angles; has `CLAUDE.md` +
    `Memory.md`.
  - `Radio Specialist/Single Radio Ad Revision/`: revises/polishes one
    existing radio ad script for natural read-aloud delivery; has
    `CLAUDE.md` + `Memory.md`.
- `Ready/website-repo/`: git submodule tracking the live WeStretch marketing
  site codebase (`git@github.com:WeBananas/westretch-website-astro.git`, an
  Astro app). This is real application code, not a planning doc, so it has
  no `CLAUDE.md`/`Memory.md` pair here, defer to whatever guidance file
  ships inside the submodule itself. Relates to `In Progress/Website/`
  (currently an empty stub): that folder is where website *copy/planning*
  work happens; this submodule is the deployed implementation. If
  `Ready/website-repo/` appears empty after a fresh clone, run
  `git submodule update --init --recursive` from the repo root.

## Memory

`Team/CMO/Memory.md` holds durable facts specific to CMO as a whole (brand source
of truth, cross-project standing rules). Project-level memory (calibrated
pixel values, session learnings, per-run decisions) lives in that project's
own `Memory.md`. See the root `CLAUDE.md` "Memory" section for the full model.
