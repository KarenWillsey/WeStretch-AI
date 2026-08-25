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

3. **Be token-efficient in every task, always** — short responses, no fluff/analogies, use the most direct tool for the job, avoid redundant work.
   - **Why:** Karen said (2026-08-21) that "don't worry about the credit limit" on a specific task is never permission to be verbose generally — token efficiency is a constant default, not situational.
   - **How to apply:** Applies to chat responses (short, plain, no filler) and to how work gets done (pick the right tool/skill first time, don't re-read files already in context, don't over-dispatch agents). Not worrying about a budget for one task means "don't stall the work," not "spend freely."

4. **"git commit and push all" means stage and commit everything currently unstaged, without stopping to ask which parts to include.**
   - **Why:** Karen clarified (2026-08-24) after being asked to scope down a commit that included unrelated pending work — she wants "all" taken literally going forward, not treated as a prompt to filter or confirm scope.
   - **How to apply:** When Karen says "commit and push all" (or equivalent), stage every unstaged/untracked change across the repo (including submodules — commit and push inside each dirty submodule first, then bump its pointer in the parent) and commit/push without an `AskUserQuestion` scoping check first. Still apply the normal safety checks (no secrets, review `git status` after a broad `git add`) — this rule removes the scope-confirmation step, not the safety review. If something looks genuinely broken (e.g. a bug producing phantom untracked files), it's fine to fix and mention it, but don't hold the commit for a scoping decision.

5. **No em dashes anywhere in any company output, full stop.**
   - **Why:** Company-wide style rule set by Karen at the Manager level (2026-08-20) — applies to every role and every deliverable, not just one project.
   - **How to apply:** Never write an em dash (—) in any generated copy, doc, or code comment across this repo. Use a period, comma, or restructure the sentence instead. Applies even inside text supplied by someone else (e.g. a draft from Kari or another teammate) — strip or replace any em dash found in source material before it ships.

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

## Root-folder cleanup (project)

On 2026-08-19: `Features/` moved to `Team/CPO/Ideas/Features/` (a not-yet-started
feature is a CPO roadmap idea, even if cross-role). `CHATTY_REVIEW.md` moved
into `Team/CPO/Ideas/Features/Multiplayer Stretches/` (the feature it critiques
— its P1 findings on that feature's experiment design are still unaddressed).
`ToneManager/` (empty file, no content) and `tmp/` (empty, untracked) were
deleted. `Globial Knowledge Content/` renamed to `Knowledge Base/` (typo fix +
standard term).
