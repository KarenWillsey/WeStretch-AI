# Set Up Daily Housekeeping; Memory

## Status (project)

V1 complete and scheduled as of 2026-08-10. All four source skills built plus
the `daily-brief` orchestrator, one full live end-to-end run completed
2026-08-09, refined 2026-08-10 based on that run's real output. A Windows
Scheduled Task ("WeStretch Daily Brief") fires it unattended every morning at
5:00am via `run-daily-brief.ps1`.

- **Why it matters:** this is the authoritative status; don't re-derive
  "is this built yet" from first principles; check here and
  `state/last-run.log` first.
- **How to apply:** treat this as a maintenance/refinement project, not a
  greenfield build, unless Karen says otherwise.

## Reliability bar (project, non-negotiable)

- **Fail loud, never silent**: a source that can't be reached gets a
  "COULDN'T CHECK" section, never a silent omission.
- **No unverified content**: every fact in the report traces back to an
  actual API/MCP call checked before send; matches Karen's general
  never-deliver-unreviewed-output rule (see root `Memory.md`).
- **Deterministic facts**: counts, subjects, senders, task names, ticket
  keys come verbatim from source data; the model may triage/summarize but
  must not paraphrase facts in a way that could drift from source.
- **Runs every time**: the schedule must actually fire and complete.

## Scheduling mechanism (project)

Runs via a local Windows Scheduled Task, **not** the cloud `/schedule` skill.

- **Why:** the cloud scheduler runs in an isolated cloud git clone with no
  access to the gitignored Jira credentials and no way to persist
  state-file updates back to this repo; using it would silently break Jira
  and corrupt dedup tracking.
- **How to apply:** any future change to how this runs must keep local
  execution with access to `state/` and `state/.jira-credentials.json`; don't
  suggest moving this to the cloud scheduler.

## Karen (user)

Karen has a reading disability that makes high email/task volume
overwhelming; the brief's entire purpose is turning scattered noise into a
small, skimmable, high-signal worklist, not a start-to-finish read. This is
a personal tool for Karen only, not (yet) a template for other execs.

## Known failure modes (added 2026-09-06)

- **Expired auth kills the run silently. Alerting added 2026-09-11.** On
  2026-09-05 the scheduled task exited 1 with "Failed to authenticate: OAuth
  session expired and could not be refreshed." Sep 2, Sep 3 and Sep 4 started
  but logged no completion line. Nothing alerted Karen; the only evidence was
  a missing brief. **Fixed 2026-09-11** in `run-daily-brief.ps1`: it now
  detects a previous "Starting" line with no matching finish line, enforces a
  60 minute timeout (killed runs log exit 124), alerts on any non-zero exit,
  and drops a `DAILY-BRIEF-FAILED.txt` marker on Karen's Desktop plus
  `state/RUN-FAILED.txt`, clearing both on the next clean run. Marker files
  rather than an alert email on purpose: expired auth is the main failure mode
  and email is precisely what stops working then.
  **How to apply:** when a brief is missing, check the Desktop marker and
  `state/last-run.log` before assuming the schedule didn't fire, and treat
  "started, no finish line" as a failure, not an unknown. The alert path has
  been parse-checked but not yet exercised by a real failure, so the first
  genuine failure is also its first live test.

- **The brief has no memory of yesterday, and that loses dated commitments.**
  The 2026-09-10 brief flagged a Sheer Illusions install on Mon Sep 14 with
  $567.61 due on install. By 2026-09-11 that email was out of the Inbox, so
  the source skill could not see it and the item would have vanished. The
  compose step carried it forward by hand from `state/last-run.log` and
  labelled it as unverified. **How to apply:** until this is built into
  `daily-brief-compose`, check the previous run's log for dated commitments
  whose date has not yet passed, and carry them forward explicitly marked as
  "carried from the [date] brief, not confirmed in today's scan." Never
  present a carried item as if it came from today's data.
- **The Kari rollup timestamp used to be written at end of run, not at send
  time.** A run that sent the rollup and then died left
  `last_report_sent_at` stale, and the next successful run re-sent content
  Kari already had. **Fixed 2026-09-07**: `daily-brief-email-triage` step 6
  now writes the state file only after a confirmed successful send, and the
  2026-09-07 run did exactly that. Do not reopen this one; if a stale
  timestamp shows up again, the cause is something new.

- **Oversized email bodies can be recovered from the saved tool-result file.**
  The Aug 12 Taylor Estates email (166,815 chars) was reported unreadable on
  every run from Aug 21 through Sep 7, because it exceeds the read tool's
  limit. On 2026-09-08 its full text was recovered by reading the saved
  tool-result file instead of re-reading the message, and it turned out to
  hold a live 27-day-old decision waiting on Karen (choose Concept A or B for
  the Taylor Estates website). **How to apply:** an over-limit body is not a
  permanent gap. Fall back to the saved tool-result file before writing it
  off as a COULDN'T CHECK; a message big enough to break the reader is
  exactly the kind likely to be hiding something that matters.
  **Written into the skill 2026-09-10** as its own "Oversized message bodies"
  section, so it no longer depends on the caller remembering.
- **Outlook reissues a message id on every folder move.** This is why the
  Kari inbox-activity delta can never re-read items that left the Inbox
  (confirmed again 2026-09-06 by batch-delete returning a different newId
  per message). Not a bug to fix in the skill; report those items as
  "left the inbox, folder untraceable" and move on.

## Resolved (kept so it is not re-investigated)

- **Escaped-HTML email bodies: fixed at the source 2026-09-10.** The bug shipped
  unreadable mail three runs running (Kari's rollup 2026-09-06, the Park Employee
  Email draft 2026-09-07, Kari's rollup again 2026-09-08), then ran clean
  2026-09-09 and 2026-09-10. It stayed open through both clean runs because
  prevention lived in whatever was calling the skill, not in the skill. On
  2026-09-10 the rule was written into `daily-brief-email-triage` (its own "HTML
  bodies: pass raw tags, then read back" section, covering every draft and every
  send) and into `daily-brief-compose` §4 for Karen's own brief. Both now require
  raw unescaped tags AND the HTML body type AND a read-back before moving on.
  Do not reopen on the strength of the old history; a new occurrence would be a
  new failure.
- **Karen's own brief landing in the Unsubscribe folder: closed 2026-09-10.**
  Intercepted 2026-09-06 and 2026-09-07, then two clean mornings (2026-09-09 and
  2026-09-10). The 2026-09-10 run pulled all 37 Unsubscribe items and found no
  brief among them, with the 15 briefs from Aug 21 through Sep 9 sitting in the
  Inbox where they belong. Reopen only on a fresh interception.
- **Asana project names: fixed 2026-09-10.** `projects.name` added to the
  `get_my_tasks` opt_fields list, and the skill now prints the real project name
  or "no project", never "My Tasks" or a numeric id. Verified live the same run.

- **Asana My Tasks pagination is fine.** An invalid pagination token on
  2026-09-07 made the task count unconfirmable and looked like a broken API.
  Two clean runs since: 2026-09-08 paged through 225 open tasks and 2026-09-09
  paged through 224, both across three pages with no gap. Treat that one day as
  transient. Tracker item deleted 2026-09-09; do not reopen without a new
  failure.
- **The Asana project-name gap was real, not a pagination side effect.** `daily-brief-asana` requests only
  `name,due_on,assignee_section.name,permalink_url`, so every task in the brief
  reads as "My Tasks" or a bare numeric project id. Confirmed again 2026-09-09. Fixed 2026-09-10 by adding `projects.name` to the opt_fields list; see the
  entry above.

