---
name: daily-brief
description: Use when running Karen's full daily brief (V1 — Outlook + Asana + Jira) end to end, whether triggered on schedule or manually — runs each source skill in sequence and hands their output to compose for the final email.
---

# Daily Brief — Orchestrator (V1)

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md`.

V1 covers Outlook + Asana + Jira.

## Sequence

1. Run `daily-brief-email-triage` on the default model: launch it via the Agent tool (general-purpose, no `model` override), instructing the subagent to read and follow `.claude/skills/daily-brief-email-triage/SKILL.md` in full and return its output contract verbatim. §3 of that skill drafts replies in Karen's voice, which needs full judgment quality — do not route it to a cheaper model. Capture its output contract, and separately note the `subagent_tokens` figure the Agent tool result reports for this call.
2. Run `daily-brief-asana` on the cheapest capable model: launch it via the Agent tool (general-purpose, `model: haiku`), instructing the subagent to read and follow `.claude/skills/daily-brief-asana/SKILL.md` in full and return its output contract verbatim. This step is pure API extraction plus a fixed rule-based urgency heuristic — no free-form judgment — so Haiku is sufficient. Capture its output contract and `subagent_tokens` figure.
3. Run `daily-brief-jira` the same way — Agent tool, `model: haiku`, instructed to follow `.claude/skills/daily-brief-jira/SKILL.md` in full. Same reasoning: fixed REST calls/JQL, list formatting, no judgment calls. Capture its output contract and `subagent_tokens` figure.
4. Sum the `subagent_tokens` figures from steps 1–3 into `data_gathering_tokens`. If any of the three didn't report a figure, don't substitute zero — pass `data_gathering_tokens_partial: true` instead so compose can label it honestly rather than understate it. Invoke `daily-brief-compose` (default model — §3 "Today's Priorities" is the one real synthesis/judgment step in the whole pipeline), passing all captured output contracts from steps 1–3 plus `data_gathering_tokens` (or the partial flag). This produces and sends the final report.

Run steps 1–3 independently — a failure in one must not block or corrupt the others. All three still hand off to compose even if one reported nothing but `couldnt_check` entries; compose is responsible for surfacing that clearly (see `daily-brief-compose` §1).

### Why Haiku for Asana/Jira only (2026-08-10)

Considered a "caveman"-style terse-output skill for token savings instead — rejected because it only cuts output tokens (single-digit % savings on real tool-orchestration runs, by that technique's own published benchmarks) and this pipeline's cost is dominated by input tokens (mailbox/task/ticket contents), which such a skill doesn't touch. Routing the two purely-mechanical steps to Haiku addresses the actual cost driver instead. Email-triage and compose stay on the default model because each has one real judgment step (voice-matched reply drafting; priority synthesis) where output quality matters more than token cost.

### Token count in the subject line (2026-08-10)

Karen wants the run's token cost visible in the subject line. What's actually obtainable: each Agent-tool subagent call (steps 1–3, now that email-triage also runs this way) reports its own `subagent_tokens` automatically in the tool result — no extra API calls, effectively free to capture. Compose's own token cost can't be known in time to appear in its own subject line, since compose hasn't finished running yet when it writes that line. So the figure handed to compose is **data-gathering cost only (steps 1–3), never the true full-run total** — see `daily-brief-compose` §4a for the exact label this must use so the number isn't presented as more complete than it actually is.

## Manual vs scheduled use

- **Scheduled**: invoked automatically each morning by a local Windows Scheduled Task ("WeStretch Daily Brief," 5:00am, running `CEO/In Progress/Set up Daily housing/run-daily-brief.ps1`) — not the cloud `/schedule` skill, which can't reach the gitignored Jira credentials or persist state-file updates back to this repo (see Implementation Spec → Architecture). Runs unattended end to end, including the M365/Asana actions each source skill performs (drafts, moves to Deleted, Kari rollup).
- **Manual / live session**: Karen can invoke this directly and then work through the resulting report interactively in the same session — the report's reference IDs (thread refs, task URLs) exist specifically to support that follow-up work without re-searching.

## First run caution

The first time this runs against Karen's real mailbox and Asana account, it will act on live data: creating reply drafts, moving inbox/unsubscribe spam to Deleted, and sending a rollup email to kari@kasa.ca. Confirm with Karen before the first live run — after that, scheduled runs proceed unattended per the reliability bar in the spec.