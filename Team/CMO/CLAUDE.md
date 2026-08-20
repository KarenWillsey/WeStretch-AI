# Team/CMO/CLAUDE.md

Scope: this folder is the CMO's isolated workspace — brand, marketing, and
App Store asset/copy work. Read this file (and `Team/CMO/Memory.md`) whenever
working here; cross-role conventions live in the repo root `CLAUDE.md`.

## Mandate

Brand, marketing, and App Store presence for WeStretch — screenshot/asset
creation, App Store copywriting, and campaign work (email funnels, radio,
website copy).

## Skills

- `Team/CMO/skills/WeStretch-Core/` — shared brand personas, strategic thesis, and
  guardrails other CMO skills depend on; load this first.
- `Team/CMO/skills/ada-stretching-phone-image/` — Ada (brand character) stretching
  phone-image generation.
- `Team/CMO/skills/app-store-image-creation/` — App Store screenshot pipeline.
- `Team/CMO/skills/create-4k-crop-master/` — source-image crop mastering.
- `.claude/skills/cmo-app-store-image-creation/` — CMO-persona review/guidance
  companion to the app-store-image-creation pipeline; discoverable as a slash
  command (see the root `CLAUDE.md` "Known issue" note on why this lives under
  `.claude/skills/` instead of `Team/CMO/skills/`).
- `.claude/skills/cmo-jamie-meeting-notes/` — updates the running WeStretch
  team action-item list from Karen/Jamie Zoom transcripts; writes dated
  output to `Team/CMO/In Progress/Jamie meeting notes/Output/`.

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
  - `Radio Specialist/5 x 30 second radio copy/` — generates a fresh batch
    of 5 new 30-second radio scripts on distinct angles; has `CLAUDE.md` +
    `Memory.md`.
  - `Radio Specialist/Single Radio Ad Revision/` — revises/polishes one
    existing radio ad script for natural read-aloud delivery; has
    `CLAUDE.md` + `Memory.md`.
- `Ready/` — finished/decided initiatives, kept for reference. Empty for now.

## Memory

`Team/CMO/Memory.md` holds durable facts specific to CMO as a whole (brand source
of truth, cross-project standing rules). Project-level memory (calibrated
pixel values, session learnings, per-run decisions) lives in that project's
own `Memory.md`. See the root `CLAUDE.md` "Memory" section for the full model.
