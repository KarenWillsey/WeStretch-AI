# Apple Opportunity Radar; Memory

Durable decisions for this project only. See `Implementation Spec.md` for
the reasoning behind each.

## Build session (2026-08-21), fully live

Karen said "go ahead" to build execution. Both skills, both wrapper
scripts, and initial state files were built successfully. Registering the
two Windows Scheduled Tasks (`Register-ScheduledTask`) was blocked twice by
the auto-mode permission classifier, creating unattended system
automation apparently isn't something a blanket "go ahead" clears on its
own in this environment, even after a retry, so Karen ran the
registration herself.

**The nightly task registered fine on the first try** via
`Register-ScheduledTask` + `New-ScheduledTaskTrigger -Daily`.

**The monthly task needed 3 tries:**
1. `New-ScheduledTaskTrigger -Monthly -DaysOfMonth 1 -At ...` → `Register-
   ScheduledTask` failed with "argument is null or empty"; `-Monthly`
   silently returned a null trigger without the `-Months` parameter.
2. Added `-Months <all 12 names>` → `-Monthly` errored as "parameter
   cannot be found"; it wasn't a real parameter set on this machine's
   `New-ScheduledTaskTrigger` at all. Root cause: Karen's shell prompt is
   PowerShell 7 (`.venv`-activated), which loads the built-in
   `ScheduledTasks` module through a Windows-PowerShell compatibility
   proxy that doesn't reliably expose every parameter set (`-Daily`
   survived the proxy, `-Monthly` didn't).
3. Switched to `schtasks.exe /sc monthly /d 1` directly to sidestep the
   module entirely, but PowerShell's own native-argument quoting kept
   mangling the `/tr` value (a string containing embedded spaces *and*
   embedded double quotes, needed because the wrapper script's own path
   has spaces in it) across two more attempts. **What finally worked:**
   writing the exact `schtasks` command into a plain `.cmd` batch file and
   having Karen execute that file directly; this routes the string
   through `cmd.exe`'s parser once, with no PowerShell re-quoting layer in
   between at all.

**Lesson for next time this needs redoing** (e.g. if the task ever needs
re-registering): skip straight to the batch-file approach for any
`schtasks`/native-command call whose arguments contain both spaces and
embedded quotes; don't bother with `Register-ScheduledTask -Monthly` in a
PowerShell-7-via-venv shell, and don't try to hand a quoted string directly
to a native command through PowerShell's argument passing.

**Confirmed live 2026-08-21:** both tasks show `State: Ready`. First real
unattended runs: nightly 2026-08-21 8:00 PM, monthly 2026-09-01 7:00 AM.

## Manual end-to-end test run (2026-08-21), loop confirmed working

Ran both skills manually (in-session, not via the scheduled tasks) to
verify the whole loop before trusting it unattended:

- **Nightly-action:** worked the top backlog item (Small Business Program
  enrollment), correctly recognized it as a verification-shaped item it
  couldn't confirm directly, and produced a checklist instead of falsely
  claiming enrollment status, exactly the intended behavior. Output,
  Backlog.md, last-run.log, and WORK-TRACKER hand-off all updated correctly.
- **Monthly-refresh:** fetched all 13 confirmed source URLs successfully.
  Found real (not cosmetic) changes in 9 of 13 sections, expected, since
  the existing baseline was Karen's manual excerpt, not a full live pull.
  Knowledge Base, Backlog.md (4 new items), monthly-refresh-log.json, and
  WORK-TRACKER were all updated correctly. Also ran the WebSearch pass for
  the "still-unconfirmed candidates" and found solid URLs for TestFlight
  and App Clips, plus the general Apple Developer News feed, correctly
  did NOT auto-add them as tracked sections (per the skill's own caution
  rule), just flagged them in Implementation Spec section 1 for a human
  to sanity-check first.

**Conclusion: both skills work as designed.** Safe to let the unattended
schedule run for real going forward. Nothing to fix.

## Knowledge Base baseline (2026-08-21)

Karen provided a full, sourced Apple Developer checklist for WeStretch
(16 sections, each with its own developer.apple.com Source line, plus a
10-item "Highest-Priority Actions" list). This is now the real content of
`Knowledge Base/apple-marketing-opportunities.md`, replacing the earlier
empty skeleton, and `Backlog.md`'s seed list was replaced with the 10
priority actions from it. This was a manual one-time seed, not a reversal
of the "monthly refresh fetches live" decision below, future refreshes
still fetch developer.apple.com live and diff against this baseline.

## Standing decisions (2026-08-21, Karen's answers during planning)

- **Scope is broad, not just metadata/screenshots.** Cover every Apple
  marketing lever: product page metadata, screenshots/previews, Custom
  Product Pages, Product Page Optimization (A/B testing), In-App Events,
  Apple Search Ads, TestFlight, App Clips, editorial/"Nominate an app"
  pitches, feature-adoption bonuses, seasonal moments (e.g. January
  fitness-resolution surge). Do not narrow this back to just what
  `.agents/skills/aso/references/apple-specs.md` already covers.
- **Monthly refresh fetches developer.apple.com live** (WebFetch/WebSearch
  against a tracked URL list), diffs against the last saved snapshot in
  `Knowledge Base/`. Not a manual "Karen pastes a file" process.
- **The Manager must be notified every time the monthly refresh completes**,
  even if nothing changed ("checked, no changes" is itself a required
  output; silence is not acceptable). This is the same "fail loud, never
  silent" bar the daily-brief project (`Team/CEO/In Progress/Set up Daily
  housing/`) uses.
- **Automation is a local Windows Scheduled Task**, same pattern as the
  daily brief, not the cloud `/schedule` skill, for the same reason the
  daily brief rejected it (isolated cloud clone can't reliably read/write
  this repo's state and output files).
- **The Manager is expected to police the schedule.** At the start of any
  session, the Manager should check whether the nightly and monthly runs
  actually fired on schedule (via `state/` timestamps once built). If a run
  is missing/stale, flag it to Karen immediately and offer to trigger a
  manual re-run right then; don't wait for Karen to notice. Mirrors the
  daily brief's "runs every time" reliability bar, applied here as an
  explicit Manager-side check since this automation, like the daily brief,
  only fires if Karen's machine is on and she's logged in at that hour.
