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

- **Expired auth kills the run silently.** On 2026-09-05 the scheduled task
  exited 1 with "Failed to authenticate: OAuth session expired and could not
  be refreshed." Sep 2, Sep 3 and Sep 4 started but logged no completion
  line. Nothing alerted Karen; the only evidence was a missing brief.
  **How to apply:** when a brief is missing, read `state/last-run.log` first
  before assuming the schedule didn't fire, and treat "started, no finish
  line" as a failure, not an unknown.
- **The Kari rollup timestamp used to be written at end of run, not at send
  time.** A run that sent the rollup and then died left
  `last_report_sent_at` stale, and the next successful run re-sent content
  Kari already had. **Fixed 2026-09-07**: `daily-brief-email-triage` step 6
  now writes the state file only after a confirmed successful send, and the
  2026-09-07 run did exactly that. Do not reopen this one; if a stale
  timestamp shows up again, the cause is something new.

- **HTML bodies going out as literal escaped tags is the live recurring bug.**
  Three runs in a row: Kari's rollup 2026-09-06 (first send unreadable,
  corrected copy followed, so Kari got two emails), the Park Employee Email
  reply draft 2026-09-07 (caught mid-run, nothing shipped), and Kari's rollup
  again 2026-09-08 (two emails again, second one telling her to ignore the
  first). **Root cause, confirmed 2026-09-08:** the body was passed to the
  send tool *pre-escaped* rather than as raw HTML tags. Setting `bodyType:
  html` is not enough on its own if the body string itself already contains
  `&lt;p&gt;` instead of `<p>`. **How to apply:** pass raw, unescaped HTML
  tags AND set the HTML body type, on every draft and every send, not just
  the Kari rollup; then read the item back before moving on. Read-back has
  caught this every single time, so detection is working and only prevention
  is missing.
  **First clean run 2026-09-09**: the Kari rollup and Karen's own brief both
  rendered as real HTML on the first send, verified by read-back from Sent
  Items, one send each, no correction email. The streak broke because the
  orchestrator explicitly told the triage agent to pass raw unescaped tags and
  read the item back. That instruction still lives in the caller, not in
  `daily-brief-email-triage` itself, so a run invoked without it can still
  regress. Do not treat this as fixed until the rule is in the skill.

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
- **Outlook reissues a message id on every folder move.** This is why the
  Kari inbox-activity delta can never re-read items that left the Inbox
  (confirmed again 2026-09-06 by batch-delete returning a different newId
  per message). Not a bug to fix in the skill; report those items as
  "left the inbox, folder untraceable" and move on.

## Resolved (kept so it is not re-investigated)

- **Asana My Tasks pagination is fine.** An invalid pagination token on
  2026-09-07 made the task count unconfirmable and looked like a broken API.
  Two clean runs since: 2026-09-08 paged through 225 open tasks and 2026-09-09
  paged through 224, both across three pages with no gap. Treat that one day as
  transient. Tracker item deleted 2026-09-09; do not reopen without a new
  failure.
- **Asana project names are still missing and this is a real gap, not a
  pagination side effect.** `daily-brief-asana` requests only
  `name,due_on,assignee_section.name,permalink_url`, so every task in the brief
  reads as "My Tasks" or a bare numeric project id. Confirmed again 2026-09-09.
  The fix is adding `projects.name` to the opt_fields list.

