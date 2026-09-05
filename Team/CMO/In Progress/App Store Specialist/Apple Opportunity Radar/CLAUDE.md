# Apple Opportunity Radar; CLAUDE.md

Scope: a standing capability that (1) keeps a living knowledge base of every
marketing/growth lever Apple exposes to App Store developers, (2) checks
developer.apple.com monthly for anything new or changed and tells the
Manager and CMO about it, and (3) works through a backlog of resulting
opportunities one item per night, handing results to the Manager for
review. Read `Memory.md` alongside this file, and `Implementation Spec.md`
for the full design.

**Status: fully live (2026-08-21).** Both skills exist
(`.claude/skills/app-store-specialist-monthly-refresh/`,
`.claude/skills/app-store-specialist-nightly-action/`), both wrapper
scripts exist (`run-nightly-action.ps1`, `run-monthly-refresh.ps1`),
`Knowledge Base/apple-marketing-opportunities.md` / `Backlog.md` are seeded
with a real baseline (Karen-provided, see `Memory.md`), and both Windows
Scheduled Tasks are registered and `Ready`:
- **"WeStretch App Store Specialist - Nightly"**: daily, 8:00 PM.
- **"WeStretch App Store Specialist - Monthly Refresh"**: 1st of month, 7:00 AM.

Registration had to be done by Karen herself (`Register-ScheduledTask` was
blocked by the auto-mode permission classifier), and the monthly task
needed a `schtasks.exe`-via-batch-file workaround since `New-
ScheduledTaskTrigger -Monthly` wasn't available as a parameter set in her
shell (see `Memory.md` "Build session" for the full story, useful if this
ever needs re-registering). Neither task has fired yet as of this writing;
first real runs are 2026-08-21 8:00 PM (nightly) and 2026-09-01 7:00 AM
(monthly). Recommend a manual test run of each skill before then; see
Implementation Spec "Recommended next step."

## Where things live

- `Implementation Spec.md`: the full spec: scope, the monthly-refresh
  design, the nightly-action design, automation mechanism, and the
  Manager's fail-loud staleness check. Read this first to resume the project.
- `.claude/skills/app-store-specialist-monthly-refresh/SKILL.md` and
  `.claude/skills/app-store-specialist-nightly-action/SKILL.md`: the two
  built skills (live under `.claude/skills/`, not here, since they need to
  be actually invocable/schedulable; see root `CLAUDE.md`'s "Known issue"
  note on why).
- `run-nightly-action.ps1` / `run-monthly-refresh.ps1`, the Windows
  Scheduled Task wrapper scripts, same pattern as the daily brief's
  `run-daily-brief.ps1`.
- `Knowledge Base/apple-marketing-opportunities.md`: the living reference
  file, one section per Apple marketing lever. Seeded 2026-08-21 with a
  real, sourced baseline (Karen-provided); the monthly refresh, once built,
  updates it from developer.apple.com rather than starting from empty.
- `Backlog.md`: the queue of opportunity action items the nightly run
  works through, one per night, in priority order. Seeded 2026-08-21 from
  the Knowledge Base's "Highest-Priority Actions" list (10 items); not
  exhaustive, grows over time.
- `Output/`: dated result files from completed nightly runs, for the
  Manager to review. Empty until the first run.
- `state/`: machine-written runtime state once this is live (last-run
  timestamps, refresh logs). Not created yet; see `Implementation Spec.md`
  "State tracking."

To resume work on this project: say "continue the Apple Opportunity Radar,"
or read `Implementation Spec.md` directly.
