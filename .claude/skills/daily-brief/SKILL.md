---
name: daily-brief
description: Use when running Karen's full daily brief (V1 — Outlook + Asana + Jira) end to end, whether triggered on schedule or manually — runs each source skill in sequence and hands their output to compose for the final email.
---

# Daily Brief — Orchestrator (V1)

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md`.

V1 covers Outlook + Asana + Jira.

## Sequence

1. Invoke `daily-brief-email-triage`. Capture its full output contract.
2. Invoke `daily-brief-asana`. Capture its full output contract.
3. Invoke `daily-brief-jira`. Capture its output contract.
4. Invoke `daily-brief-compose`, passing all captured output. This produces and sends the final report.

Run steps 1–3 independently — a failure in one must not block or corrupt the others. All three still hand off to compose even if one reported nothing but `couldnt_check` entries; compose is responsible for surfacing that clearly (see `daily-brief-compose` §1).

## Manual vs scheduled use

- **Scheduled**: invoked automatically each morning per the `schedule` skill's cron config (see Implementation Spec → Architecture). Runs unattended end to end, including the M365/Asana actions each source skill performs (drafts, moves to Deleted, notification clearing, Kari rollup).
- **Manual / live session**: Karen can invoke this directly and then work through the resulting report interactively in the same session — the report's reference IDs (thread refs, task URLs) exist specifically to support that follow-up work without re-searching.

## First run caution

The first time this runs against Karen's real mailbox and Asana account, it will act on live data: creating reply drafts, moving inbox/unsubscribe spam to Deleted, clearing Asana inbox notifications, and sending a rollup email to kari@kasa.ca. Confirm with Karen before the first live run — after that, scheduled runs proceed unattended per the reliability bar in the spec.