# Daily Brief — Implementation Spec (v1)

Status (2026-08-10): **V1 complete and scheduled.** All four skills built (`daily-brief-email-triage`, `daily-brief-asana`, `daily-brief-jira`, `daily-brief-compose`, `daily-brief` orchestrator — all under `.claude/skills/`), one full live end-to-end run completed 2026-08-09, and refined further 2026-08-10 based on that live run's real output. A local Windows Scheduled Task now fires the brief unattended every morning at 5:00am.

- **Email triage:** run live and confirmed working end to end (Unsubscribe + inbox scanned, spam deleted, threads flagged, digest emailed). Kari's rollup expanded 2026-08-09/10 from sent-mail-only to full Outlook activity — sent mail, plus inbox items Karen filed to a subfolder or deleted herself (excluding this automation's own spam cleanup, and excluding pure junk) — because Kari co-runs the family enterprise office and needs knowledge parity, personal and corporate. State file: `state/kari-activity-summary.json`.
- **Asana:** run live and confirmed working end to end; `get_my_tasks` + client-side section filtering verified against Karen's actual app counts (26 Recently Assigned, 17 Today, 2026-08-09). Inbox-notification clearing was dropped from scope entirely 2026-08-10 — the Asana MCP connector has no endpoint for it, and there's no value in carrying a permanent `couldnt_check` stub for something structurally unavailable.
- **Jira:** built 2026-08-09, refined 2026-08-10 after the first live run showed the original design was too broad (22 assigned tickets, mostly stale backlog to 2019). No Jira MCP exists, so this calls the Jira Cloud REST API directly (site `webananas.atlassian.net`). Credentials live in `state/.jira-credentials.json` (gitignored — see `.gitignore` at repo root — never commit this file).
  - "Assigned to Karen" now scopes to tickets assigned to her in whatever sprint(s) are currently active (discovered live via the Agile REST API each run), not the full backlog. Verified live: WEMVP's active sprint has 50+ tickets, zero assigned to Karen — an empty section here is a correct, expected result.
  - "New @mentions" still uses a text-match heuristic (no mentions API exists), now capped to a rolling 7-day window and excluding threads Karen has already commented on, so it can't dump stale backlog or re-surface things she's already replied to.
  - State file: `state/jira-mentions-state.json`.
- **Compose:** includes the Jira section unconditionally, reflects the Asana/Jira scope changes above.
- **Scheduling:** NOT via the cloud `/schedule` skill — that runs in an isolated cloud git clone with no access to the gitignored Jira credentials and no way to persist state-file updates back to this repo, so it would break Jira entirely and silently corrupt dedup tracking. Instead: a Windows Scheduled Task ("WeStretch Daily Brief," registered 2026-08-10) runs `CEO/In Progress/Set up Daily housing/run-daily-brief.ps1` daily at 5:00am, which invokes the Claude Code CLI bundled inside the VS Code extension (path resolved dynamically each run, not hardcoded to a version) with `--print --dangerously-skip-permissions`, logging to `state/last-run.log`. Only fires if Karen's machine is on and she's logged in at 5am.

To resume in a new session: say "continue the daily brief" (or open this file — it has everything needed). No special setup required; the skills are already discoverable by Claude Code in this project. To check whether the scheduled run actually fired, read `state/last-run.log`.

## Core problem

Karen has a reading disability that makes high email/task volume overwhelming. The brief's job is to turn scattered inbox/task/comms noise into a small, high-signal, **skimmable** worklist — meant to be scanned and acted on, not read start to finish like a normal email.

**Who it's for:** Karen only. A personal operational tool — not shared outward, not (yet) a template for other execs.

**Why the old version failed:** `Daily brief.txt` never actually worked — every run got permission-blocked trying to browser-automate Gmail/Google Calendar. That path is being replaced entirely: this repo already has an authenticated Microsoft 365 MCP connector, so calendar/email is pulled via direct structured API calls, not browser automation.

## Reliability bar (non-negotiable, per Karen's answers)

- **Fail loud, never silent.** If a source can't be reached, the report says so in a "COULDN'T CHECK" section — it never just omits that section.
- **No unverified content.** Every fact in the report must trace back to an actual API/MCP call, checked before send. Matches Karen's standing rule (see memory `karen-workflow-preferences`) of never delivering unreviewed output.
- **Deterministic facts.** Counts, subjects, senders, task names, ticket keys come verbatim from source data. The model may triage/summarize, but must not paraphrase facts in a way that could drift from the source.
- **Runs every time.** The schedule must actually fire and complete, not silently stall like the old Codex automation did.

## Scope

### V1 — build now (Outlook + Asana + Jira)

**1. Outlook email triage** (Microsoft 365 MCP)
- **Unsubscribe folder** (already auto-filed there by Karen's existing rule) is actively scanned each run, not just counted:
  - Items that might have real value → few-word summary, listed under a new **"Needs My Attention"** report section, and left in place in the unsubscribe folder (not moved).
  - Everything else (genuine spam) → few-word summary, listed under "Deleted", then moved to the account's default Trash/Deleted folder (recoverable, not gone).
- Classify the remaining (main) inbox into:
  - **Needs reply** → draft a reply in Karen's voice (derived from Sent-folder patterns) as an Outlook draft. Never auto-sent. Stays in inbox. Listed in report.
  - **Spam / low value** → few-word summary, listed under "Deleted", then moved to the Deleted folder (recoverable, not gone).
  - **Follow-ups** → cross-check items previously flagged as "handed off" and report whether they've moved.
- **Sent-mail rollup** → headline-only summary of what Karen sent, delivered separately to kari@kasa.ca. Delta-only since the last report (see State tracking below) — never repeats what she's already seen.

**2. Asana** (Asana MCP)
- Recently Assigned tasks + Today's tasks.
- Flag anything trending urgent (starting heuristic: due-date proximity / staleness — tuned after real use).
- Inbox-notification clearing was in the original scope but dropped 2026-08-10 — no endpoint exists in the connector.

**3. Jira**
- Tickets assigned to Karen **in the currently active sprint(s)** (narrowed 2026-08-10 from "all assigned unresolved tickets," which was mostly years-old backlog noise) + recent @mentions (7-day window, excludes threads already replied to).
- No MCP exists for this — a small custom integration (Jira REST API + API token) is part of the V1 build.

**4. Priorities pass**
- After the housekeeping sections: a short "what actually matters today" synthesis across everything above. Not a separate data source.

### V2 — explicit fast-follow, does not block V1

- **Mattermost** — summarize unread without marking read, catch anything unreplied in the last 3 days. No MCP exists; custom build required.
- **Cozi family calendar** — today's view, one column per family member. No confirmed API; needs investigation (likely an ICS feed subscription if Cozi exposes one, or another access path).
- **Gmail** (via Apify or similar) for the accounts Karen's staff monitor — Karen explicitly deferred this as a bigger setup lift.

## Delivery model

- Every morning, a scheduled run produces one email report to Karen's own inbox.
- Separately, Karen can open a chat session and hand the agent the report to work through flagged items live (draft review, reply decisions, etc.).
- **Design requirement this creates:** the report must carry enough reference detail (email/thread IDs, Asana task IDs, Jira ticket keys) that a follow-up session can act on each item directly, without re-searching for it.
- **Format requirement:** optimized for scanning, not reading — short lines, clear section headers, bolded subjects/senders, no dense paragraphs. This directly serves the core problem.

## State tracking

**Recommendation:** a small state file in this repo, e.g. `CEO/In Progress/Set up Daily housing/state/kari-activity-summary.json`, storing the timestamp/message-IDs/inbox-snapshot of the last activity rollup reported to Kari (sent mail plus inbox items Karen filed away or deleted herself).

**Why a repo file instead of querying Outlook for "since last run":** it's git-versioned, so there's an inspectable history of exactly what was reported and when — which matters given the "no unverified content" bar. It also avoids writing tracking flags back onto live mailbox items.

## Architecture

Build as real Claude Code **project skills** under `.claude/skills/daily-brief-*/` — not the `ROLE/skills/` convention-only pattern used elsewhere in this repo, because this needs to be actually invocable and schedulable, not just read by reference.

Proposed skill breakdown (one focused skill per source, matching this repo's "one skill = one task" convention):

- `daily-brief-email-triage` — Outlook classification, draft generation, spam move, Kari activity-rollup delta.
- `daily-brief-asana` — Asana pull, urgency flagging.
- `daily-brief-jira` — Jira pull via direct REST API (no MCP connector exists).
- `daily-brief-compose` — merges outputs from the above into the final scannable report, runs the verification/fail-loud pass, sends the email.

A top-level orchestration runs all of the above in sequence, then composes. Scheduling is a local Windows Scheduled Task (see Status above) — the cloud `/schedule` skill was evaluated and rejected because it can't reach the gitignored Jira credentials or persist state-file updates back to this repo. This replaces the old Codex automation entirely, which is what actually satisfies "runs every time."

## Open items — assumed defaults, flag if wrong

- **Send time:** assuming early morning (e.g. 5:00am) 
- **Destination address:** assuming Karen's primary Outlook mailbox (same one the M365 MCP is authenticated against).
- **"Urgent" heuristic:** starts simple, tuned once real false positives/negatives show up.

## Explicitly out of scope for now

- Gmail/Apify (v2)
- Mattermost, Cozi (v2)
- Auto-sending any email reply — never, per Karen's answer
- Building this as a shared/team-facing tool

## Build order

1. ✅ `daily-brief-email-triage` + `daily-brief-asana` — built, both run live and confirmed.
2. ✅ `daily-brief-jira` — built 2026-08-09, refined 2026-08-10 (active-sprint scope, capped mentions) after live feedback.
3. ✅ Full orchestrator live end-to-end run — completed 2026-08-09.
4. ✅ Scheduling — local Windows Scheduled Task registered 2026-08-10, next fire 2026-08-11 5:00am.
5. V2 (not started): Mattermost, Cozi, Gmail.