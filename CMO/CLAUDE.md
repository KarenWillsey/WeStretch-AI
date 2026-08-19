# CMO/CLAUDE.md

Scope: this folder is the CMO's isolated workspace — brand, marketing, and
App Store asset/copy work. Read this file (and `CMO/Memory.md`) whenever
working here; cross-role conventions live in the repo root `CLAUDE.md`.

## Mandate

Brand, marketing, and App Store presence for WeStretch — screenshot/asset
creation, App Store copywriting, and campaign work (email funnels, radio,
website copy).

## Skills

- `CMO/skills/WeStretch-Core/` — shared brand personas, strategic thesis, and
  guardrails other CMO skills depend on; load this first.
- `CMO/skills/ada-stretching-phone-image/` — Ada (brand character) stretching
  phone-image generation.
- `CMO/skills/app-store-image-creation/` — App Store screenshot pipeline.
- `CMO/skills/create-4k-crop-master/` — source-image crop mastering.
- `.claude/skills/cmo-app-store-image-creation/` — CMO-persona review/guidance
  companion to the app-store-image-creation pipeline; discoverable as a slash
  command (see `CHATTY_REVIEW.md` on why this lives under `.claude/skills/`
  instead of `CMO/skills/`).
- `.claude/skills/cmo-jamie-meeting-notes/` — updates the running WeStretch
  team action-item list from Karen/Jamie Zoom transcripts; writes dated
  output to `CMO/In Progress/Jamie meeting notes/Output/`.

The original `brand-messaging-review`, `campaign-planning`, and `jokes`
SKILL.md files were removed from this folder; the App Store image-creation
work above replaced them as CMO's active output. Restore or rewrite those if
that generic review/planning function is needed again.

## Project pipeline

- `Ideas/App Stores/App Sore Keyword Creation/` — not yet started (empty).
- `In Progress/` — active initiatives, each with its own `CLAUDE.md` + `Memory.md`:
  - `App Store Specialist/Ada Stretching Phone Image/`
  - `App Store Specialist/App Store Image Creation/`
  - `App Store Specialist/App Store Image Text Copywriting/`
  - `Email Funnels Specialist/`
  - `App Store Specialist/App Store Description Copywriting/`, `Website/` — stub folders, no content yet.
  - `Jamie meeting notes/Output/` — dated running action-item lists produced
    by the `cmo-jamie-meeting-notes` skill (`.claude/skills/`); this folder
    holds output only, not a skill definition; not given a memory pair.
  - `Radio Specialist/5 x 30 second radio copy/` — contains a skill
    definition, not project notes; not given a memory pair.
- `Ready/` — finished/decided initiatives, kept for reference. Empty for now.

## Memory

`CMO/Memory.md` holds durable facts specific to CMO as a whole (brand source
of truth, cross-project standing rules). Project-level memory (calibrated
pixel values, session learnings, per-run decisions) lives in that project's
own `Memory.md`. See the root `CLAUDE.md` "Memory" section for the full model.
