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

## V2 redesign: the format that actually works (2026-09-12)

Karen stopped reviewing the V1 brief. Her words: "the output is completely
useless for me and has made me slower." V1 was complete and correct and she
could not use it. **Treat "she isn't reading it" as a design failure of the
brief, never as something for her to push through.**

**The unit that works is the Deleted line.** `**Halara**, clothing sale promo.`
Bold name, then a handful of words, one item per line. She identified this
herself: she reads that section fast, always has, and asked for the whole brief
to look like it. V2 applies that shape to every section. Her rule, verbatim:
"the more compact the lines are in a section the better."

- **Why it matters:** the problem was never how much the brief covered, it was
  words per item. A bulleted block costs her a paragraph of reading before she
  can decide anything; a bold name plus six words costs her a glance.
- **How to apply:** one line per item, everywhere, no exceptions, no
  sub-bullets. If an item will not fit on a line, the detail goes in the queue
  entry for the walkthrough, and the line still gets written short.

**Coverage did not shrink, and must not.** Karen: "I can't neglect anything, I
need to answer all important and urgent... the goal is always to get inbox and
unsubscribe to zero but each item does need its appropriate attention." Never
solve a length complaint by dropping items. Compress the line, move the detail
to `state/today-queue.json` and `state/YYYY-MM-DD-full.md`, keep the item.

**Mail lands in Unsubscribe that belongs in the Inbox**, and she must see those
for certain. That is why UNFILED, SHOULD BE INBOX survives as its own section
and recurs daily until cleared.

**This supersedes the 2026-08-09 "zero detail loss in Other Inbox Mail" rule.**
That rule required every `detail_bullets` entry rendered inline, and it is the
single biggest reason the email became unreadable. The bullets are still kept
verbatim, in the queue file and the full-detail file. Do not reinstate the
inline rendering; the fix for "I need that detail" is the walkthrough, where she
meets one item at a time.

## Audio and the walkthrough (2026-09-12)

Two deliverables were added alongside the email.

**Audio.** `make-brief-audio.ps1` renders the spoken brief with the Windows
built-in voice (Zira), writes it to `OneDrive\Daily Brief\` so it syncs to her
phone, and copies it to the Desktop. Karen chose the free built-in voice over a
paid natural one to start, so the habit gets tested before anything is paid for.

- **The audio must be a real attachment, not a path.** Karen asked for this
  directly on 2026-09-12 after seeing the OneDrive-path version: she listens on
  her phone and wants to tap it in Mail. The MCP connector genuinely cannot do
  it (`outlook_send_mail` has no attachment parameter, `outlook_send_draft`
  rejects drafts that have attachments), so **the brief now sends through the
  local Outlook desktop client over COM** via `send-brief-email.ps1`, which
  confirms both Sent Items delivery and attachment count before exiting 0.
  Verified live 2026-09-12. **How to apply:** treat "the tool cannot do it" as
  the start of the search, not the end. The MCP send is now only the fallback,
  and a fallback must always say in the brief that the audio is missing.
- **Outlook COM needs an interactive desktop session.** If the 5am task ever
  fires while Karen is logged off, `send-brief-email.ps1` exits 2 and the MCP
  fallback carries the morning without the attachment. Expected and handled;
  do not treat exit 2 as a bug on its own.
- **Pass the HTML body as a file, never as a command-line argument.** Same
  space-splitting and quoting trap that broke `run-daily-brief.ps1`.
- **2.5 MB is the normal size** for an 80-second 16 kHz mono WAV, well inside
  mail limits. There is no ffmpeg on this machine, so do not plan on MP3; the
  fix for a long brief is fewer spoken items, not a smaller codec.
- **How to apply:** only DECIDE, DATED and REPLY get read aloud, 60 to 90
  seconds. Deleted, FYI and Tasks are scanning material, not listening material.
- **Karen listens at 1.8x and the speed is rendered into the file**, not left to
  a player: a plain WAV gives her no speed control on a phone. `-Speed 1.8` is
  the script default. She asked for 1.6 first, heard it, and asked for faster
  the same day; if she asks again the table goes to 2.18x. SAPI's `Rate` is not a speed multiple and is not linear,
  so the script carries a table measured on this machine 2026-09-12 (rate 0 =
  1.00x, 1 = 1.15x, 2 = 1.28x, 3 = 1.44x, 4 = 1.61x, 5 = 1.79x) and picks the
  nearest rate. The mapping is voice-specific; re-measure if the voice changes.
- The Desktop copy must resolve the Desktop via
  `[Environment]::GetFolderPath('Desktop')`. Karen's Desktop is redirected into
  OneDrive, so a hardcoded `$env:USERPROFILE\Desktop` path does not exist.

**Walkthrough.** `daily-brief-walkthrough` lets her say "brief" in a chat and
work the day one item at a time: it drafts in her voice and sends, deletes or
files straight from the conversation so she never opens Outlook. She asked for
this directly. Two standing rules: never send without her explicit "send," and
batch the Deleted and FYI sections rather than walking them, because the list
format already works for her and walking it would waste the session.

## The approved brief email (2026-09-12)

`reference-brief-email.html` in this folder is the exact HTML of the 2026-09-12
brief, pulled back out of Sent Items. Karen approved it unprompted: "That email
copy was great." It is the gold standard for section order, line shape, density
and footer, and `daily-brief-compose` §0 requires reading it before composing.

- **Why it matters:** the V2 rules were written before anything shipped. This
  file is the first output Karen has actually endorsed, so where a rule and
  this file disagree, the file is what she said yes to.
- **How to apply:** do not overwrite it with a later brief unless she approves
  a new one. Its whole value is that she signed off on this specific one.
- Shape for reference: 84 visible lines covering 72 items, sections
  COULDN'T CHECK 2, DECIDE 6 (5 shown plus "+1 more"), REPLY 1, DATED 2,
  DELETED 3, TASKS 7, FYI 51, then the "Checked, nothing" line and a 4-line
  footer. Note FYI at 51 one-liners did not bother her; density was never the
  problem, words per line was.

**Exactly one email reaches Karen per run.** She asked for this after 2026-09-12
produced two (the brief, then a separate audio message). The audio is an
attachment on the brief, never its own email. Fold anything else into the next
morning's brief.

## Runner bugs found and fixed 2026-09-12

Both were in `run-daily-brief.ps1` and both were invisible until they bit.

- **The prompt was passed unquoted and got split on spaces.** `Start-Process`
  joins `-ArgumentList` with spaces and quotes nothing, so `claude.exe` received
  only the first word, `Run`. The 2026-09-12 05:00 run answered "'Run' on its
  own isn't clear enough to act on" and no brief was sent. Fixed by wrapping the
  prompt in real quotes, and by removing the `--` from the prompt text, which
  terminates option parsing. Verified live: the full prompt now arrives intact.
  **How to apply:** any future change to that argument list must keep the prompt
  as one quoted argument. This will look like it works when you eyeball it.
- **`$proc.ExitCode` came back empty even on success.** That produced the
  useless "exited with code ." alert. Cause is the standard .NET one: the
  process handle is released when the child exits unless something touched
  `.Handle` first. Fixed by `$null = $proc.Handle` immediately after launch,
  plus a 125 fallback if the code still cannot be read. Verified live 2026-09-12:
  the same launch returns `[]` without the Handle line and `[0]` with it.

The 2026-09-11 alerting work got its first real test on 2026-09-12 and did fire:
`state/RUN-FAILED.txt` was written. The alert path works; what it reported was
garbled, and that is what got fixed.

## V2's first live run: 2026-09-12

V2 shipped and ran end to end the same day it was built. The 05:00 scheduled run
died on the prompt-splitting bug, the runner relaunched at 09:53, and that
catch-up run produced the first real V2 brief. It worked: one line per item in
every section, counts in the headers, 72 items in `state/today-queue.json`, a
1:20 WAV in `OneDrive\Daily Brief\` plus the Desktop copy, and HTML confirmed by
read-back from Sent Items. Both runner bugs fixed earlier that day are now
verified by a real run, not just parse-checked.

- **Coverage was checked against the live mailbox, not just the source contract,
  and that is worth repeating every run.** The triage contract said 52 items in
  Other Inbox Mail but produced 51 entries. The difference was not a dropped
  item: the two-message SR-20707 thread is one entry. Confirmed by paging all
  60 remaining Inbox messages and mapping each to a brief line. **How to apply:**
  when a source's own count and its entry count disagree, page the source and
  reconcile before sending. Do not assume a dropped item, and do not assume the
  count is right either.
- **The Inbox arithmetic that reconciles a run:** messages pulled, minus those
  moved to Deleted, equals what a fresh search returns. 63 minus 3 was 60 here.

## The queue's `ref` field is only as good as the triage contract (2026-09-12)

`daily-brief-compose` §5 says `ref` must be the live Outlook messageId, but
`daily-brief-email-triage` hands over `thread_ref`, a date or conversation id.
Compose cannot satisfy its own spec from the contract it is given. The
2026-09-12 run re-searched the Inbox and filled in real messageIds for the 26
items that matter most (all of DECIDE, REPLY and DATED, plus recent FYI), and
left a date string on roughly 25 older FYI entries.

- **Why it matters:** the walkthrough's `delete` and `file` actions act on a real
  mailbox. Several FYI subjects repeat exactly ("Note to self", "Daily Brief"),
  so resolving one by subject could act on the wrong message.
- **How to apply:** until the messageId is added to the triage output contract,
  compose should keep back-filling ids for at least DECIDE, REPLY and DATED, and
  the walkthrough must confirm a match before acting on any item whose `ref` is
  not a messageId. The real fix is at the source; see `WORK-TRACKER.md`.

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

