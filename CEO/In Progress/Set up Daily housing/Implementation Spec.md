# Daily Brief — Implementation Spec (v1)

Status (2026-08-09): All four V1 skills built and wired together (`daily-brief-email-triage`, `daily-brief-asana`, `daily-brief-jira`, `daily-brief-compose`, `daily-brief` orchestrator — all under `.claude/skills/`).

- Email triage: run live and confirmed working end to end (Unsubscribe + inbox scanned, spam deleted, one reply draft created, Kari's sent-rollup sent, digest emailed). State file: `state/kari-sent-summary.json`.
- Asana: run live and confirmed working end to end; `get_my_tasks` + client-side section filtering verified against Karen's actual app counts (26 Recently Assigned, 17 Today, 2026-08-09). No inbox-notifications tool exists in the connector, so that step is skipped and reported as `couldnt_check` until one does.
- Jira: built 2026-08-09. No Jira MCP exists, so this calls the Jira Cloud REST API directly (site `webananas.atlassian.net`, project `WEMVP`). Credentials live in `state/.jira-credentials.json` (gitignored — see `.gitignore` at repo root — never commit this file). "Assigned to Karen" is a verified live query (22 open tickets on first check). "New @mentions" uses a text-match + updated-since heuristic (documented as a caveat in the skill and surfaced in every report) because the API has no dedicated mentions endpoint; state file `state/jira-mentions-state.json` tracks the delta. Not yet run end-to-end through the full orchestrator.
- Compose: updated to include the Jira section unconditionally (previously gated on Jira not existing yet).

**Next step:** run one full live end-to-end test of `daily-brief` (all three sources → compose → send), then wire up the 5:00am America/Edmonton daily schedule via the `schedule` skill. Confirm with Karen before the first unattended scheduled run per the orchestrator's "First run caution."

To resume in a new session: say "continue the daily brief" (or open this file — it has everything needed). No special setup required; the skills are already discoverable by Claude Code in this project.

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
- Clear Asana inbox notifications once reviewed in the report.

**3. Jira**
- Tickets assigned to Karen + new @mentions.
- No MCP exists yet for this — small custom integration (Jira REST API + API token) is part of the V1 build, not a prerequisite blocking it.

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

**Recommendation:** a small state file in this repo, e.g. `CEO/In Progress/Set up Daily housing/state/kari-sent-summary.json`, storing the timestamp/message-IDs of the last sent-mail rollup reported to Kari.

**Why a repo file instead of querying Outlook for "since last run":** it's git-versioned, so there's an inspectable history of exactly what was reported and when — which matters given the "no unverified content" bar. It also avoids writing tracking flags back onto live mailbox items.

## Architecture

Build as real Claude Code **project skills** under `.claude/skills/daily-brief-*/` — not the `ROLE/skills/` convention-only pattern used elsewhere in this repo, because this needs to be actually invocable and schedulable, not just read by reference.

Proposed skill breakdown (one focused skill per source, matching this repo's "one skill = one task" convention):

- `daily-brief-email-triage` — Outlook classification, draft generation, spam move, sent-rollup delta.
- `daily-brief-asana` — Asana pull, urgency flagging, inbox clear.
- `daily-brief-jira` — Jira pull (once the integration exists).
- `daily-brief-compose` — merges outputs from the above into the final scannable report, runs the verification/fail-loud pass, sends the email.

A top-level orchestration runs all of the above in sequence, then composes. Scheduling via the `schedule` skill (cron-backed), replacing the old Codex automation entirely — this is what actually satisfies "runs every time."

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
2. ✅ `daily-brief-jira` — built 2026-08-09, `myself`/assigned-tickets queries verified live; not yet run through the full orchestrator.
3. Wire up scheduling — next.
4. V2: Mattermost, Cozi, Gmail.