# Set Up Daily Housekeeping; CLAUDE.md

Scope: Karen's daily brief automation; Outlook email triage, Asana review,
Jira review, composed into one skimmable morning email. Read `Memory.md`
alongside this file, and `Implementation Spec.md` for the full design.

## Where things live

- `Implementation Spec.md`: the full spec: reliability bar, scope, and the
  detailed design for each source (Outlook/Asana/Jira) and the composer.
- `Daily brief.txt`: original early draft/notes, superseded by the spec.
- `run-daily-brief.ps1`: the script the Windows Scheduled Task actually runs.
- `make-brief-audio.ps1`: renders the spoken version of the brief to a WAV with
  the Windows built-in voice (no API, no key, no cost) and drops it in
  `OneDrive\Daily Brief\` so it syncs to Karen's phone, plus a Desktop copy.
  Called by `daily-brief-compose`; can also be run by hand on any script file.
- `send-brief-email.ps1`: sends the brief through the local Outlook desktop
  client over COM, which is the only way to get the audio in as a real
  attachment; the MCP connector cannot attach files. Confirms Sent Items
  delivery and attachment count before exiting 0. The MCP send is the fallback.
- `state/`: machine-written runtime state (dedup tracking, credentials, last
  run log). This is operational state, not memory; never hand-edit it as if
  it were documentation, and never commit `.jira-credentials.json` (gitignored).
- The actual skills this project runs (`daily-brief`, `daily-brief-email-triage`,
  `daily-brief-asana`, `daily-brief-jira`, `daily-brief-compose`,
  `daily-brief-walkthrough`) live under `.claude/skills/`, not in this folder;
  this folder is the project's home base, not the skill implementation.
- `daily-brief-walkthrough` is the interactive half added in V2: Karen says
  "brief" in a chat and works the day one item at a time, replying, sending,
  deleting and filing without opening Outlook. It reads `state/today-queue.json`,
  which `daily-brief-compose` writes each morning.

To resume work on this project: say "continue the daily brief," or read
`Implementation Spec.md` directly; it has everything needed.
