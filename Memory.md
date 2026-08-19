# Project Memory (global / cross-role)

This file holds only facts that are truly cross-role — general Karen workflow
preferences and org-wide decisions that don't belong to one officer's work.
Role-specific and project-specific memory now lives closer to the work: see
`Team/ROLE/Memory.md` for each C-suite role, and `Team/ROLE/.../ProjectName/Memory.md`
for individual initiatives. See `CLAUDE.md` under "Memory" for the full model.

## Karen's workflow preferences (feedback)

Two standing rules from Karen (established 2026-08-07, App Store image work —
originated in CMO but apply to any deliverable-producing work across roles):

1. **Never place unreviewed generated assets into an Output folder she collects from** — inspect and verify first, deliver only what passes.
   - **Why:** A prior run delivered visibly broken images (overlapping text, wrong fonts) straight into her pickup folder.
   - **How to apply:** Render to scratch, visually inspect and measure, then copy only passing files to the delivery folder.

2. **If supplied title/subtitle copy looks misspelled or ungrammatical (e.g. "teh"), ask her to confirm exact wording before production** — never silently correct, never render it as-is without asking.
   - **Why:** The template rules said "render exactly as given," which shipped a typo; she wants a confirmation gate instead.
   - **How to apply:** This gate is written into the App Store image pipeline's own docs (see `Team/CMO/In Progress/App Store/App Store Image Creation/Memory.md`) and should be applied by analogy anywhere else copy is rendered verbatim into a deliverable.

## Repo restructure (project)

On 2026-08-17, the repo moved from one root `CLAUDE.md`/`Memory.md` to a
distributed model: every role folder (including `CEO/`) got its own
`CLAUDE.md` + `Memory.md`, and every active project inside a role's
`Ideas/In Progress/Ready` folders got the same pair. Root files were trimmed
to only cross-role content as part of that move.

- **Why:** Karen wanted each officer's responsibilities isolated (their own
  scope + memory, not mixed into one shared file), with consistent naming
  across all 11 roles, so the structure scales as more roles accumulate
  active project folders the way CMO and CEO already had.
- **How to apply:** When creating a new role skill or starting a new
  initiative, follow the structure documented in the root `CLAUDE.md` rather
  than adding content back into this file or inventing a new pattern.

## Manager/Team restructure (project)

On 2026-08-19, all 11 officer folders (`CEO/` through `CXO/`) moved under a
new `Team/` folder (e.g. `CEO/` → `Team/CEO/`). The repo root — this
`CLAUDE.md`/`Memory.md` — is now framed as **the Manager**: the
orchestrator/delegator Karen addresses directly ("tell the Manager to do
this"), which routes work to the officer(s) under `Team/` with the relevant
skills/mandate.

- **Why:** Karen wanted the root level to read as a clean delegation point
  rather than a peer sibling of 11 officer folders — "the directory to the
  orchestrator, the delegator of work."
- **How to apply:** All path references to officer folders take a `Team/`
  prefix (`Team/CMO/...`, `Team/CEO/In Progress/...`, etc.). The Windows
  Scheduled Task and `run-daily-brief.ps1` that drive the daily brief
  automation were repointed at `Team/CEO/In Progress/Set up Daily
  housing/run-daily-brief.ps1` as part of this move — if daily brief state
  files ever seem stale, check the scheduled task's action path first.
