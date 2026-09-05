# Set Up Daily Housekeeping; CLAUDE.md

Scope: Karen's daily brief automation; Outlook email triage, Asana review,
Jira review, composed into one skimmable morning email. Read `Memory.md`
alongside this file, and `Implementation Spec.md` for the full design.

## Where things live

- `Implementation Spec.md`: the full spec: reliability bar, scope, and the
  detailed design for each source (Outlook/Asana/Jira) and the composer.
- `Daily brief.txt`: original early draft/notes, superseded by the spec.
- `run-daily-brief.ps1`: the script the Windows Scheduled Task actually runs.
- `state/`: machine-written runtime state (dedup tracking, credentials, last
  run log). This is operational state, not memory; never hand-edit it as if
  it were documentation, and never commit `.jira-credentials.json` (gitignored).
- The actual skills this project runs (`daily-brief`, `daily-brief-email-triage`,
  `daily-brief-asana`, `daily-brief-jira`, `daily-brief-compose`) live under
  `.claude/skills/`, not in this folder; this folder is the project's home
  base, not the skill implementation.

To resume work on this project: say "continue the daily brief," or read
`Implementation Spec.md` directly; it has everything needed.
