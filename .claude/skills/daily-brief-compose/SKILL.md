---
name: daily-brief-compose
description: Use when merging daily-brief-email-triage, daily-brief-asana, and daily-brief-jira output into Karen's final morning brief email — runs the fail-loud verification pass, formats for scanning not reading, and sends the report to Karen's own inbox.
---

# Daily Brief — Compose

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md`.

This skill does not pull any data itself — it only merges structured output already produced by the source skills (`daily-brief-email-triage`, `daily-brief-asana`, and `daily-brief-jira`), plus the `data_gathering_tokens` figure the orchestrator captured from those calls (see §4a), and sends the final report.

## Format requirement — this is the whole point of the brief

Karen has a reading disability; the brief must be **scanned, not read**. Every section:

- Short lines. No dense paragraphs, ever.
- Clear, bolded section headers.
- Bolded subject/task/ticket names so the eye catches them first.
- Each item carries its reference (email thread ID, Asana task URL, Jira ticket key) so a follow-up chat session can act on it directly without re-searching.
- **Deleted** section specifically: one item per line, **sender/company name bolded** first, then a summary under one sentence — e.g. `**Halara** — clothing sale promo.` Karen asked for this exact shape so the list is fast to scan.
- **Other Inbox Mail** is the one deliberate exception to "no dense paragraphs": render each `other_inbox` entry as `email-triage` produced it — a bold subject/thread header, then its `detail_bullets` as-is, one fact per line. Do not compress a multi-bullet item back down to a single line, and do not merge a thread's bullets into prose — Karen explicitly asked (2026-08-09) for zero detail loss here, in exchange for accepting more lines than other sections.
- If a section has nothing to report, say so in one line ("Nothing needs your attention here today") rather than omitting the header — an omitted section reads as "not checked," which violates the fail-loud rule.

## 1. Verification pass (do this before composing anything)

- Confirm every source skill that ran actually returned output — if `daily-brief-email-triage`, `daily-brief-asana`, or `daily-brief-jira` didn't run or errored entirely, the top of the report must say so explicitly, not just skip that section.
- Carry forward every `couldnt_check` entry from each source verbatim into a single **Couldn't Check Today** section near the top of the report — this is the most important section for the fail-loud reliability bar and must never be buried.
- Do not paraphrase or summarize facts (subjects, counts, task names) beyond what the source skill already produced — compose only reorganizes and formats, it doesn't reinterpret.

## 2. Report structure

```
Subject: Daily Brief — [date] — [token cost suffix, see §4a]

[Couldn't Check Today]        <- only if non-empty, but check first, show first

Needs My Attention             <- Unsubscribe-folder items that might have value (recurs daily until Karen clears them)
Threads Waiting On You         <- inbox items needing a reply or a reply from someone else
Other Inbox Mail                <- no action needed, but full detail per item/thread (see below), not a one-liner
Deleted                        <- few-word summaries of what got moved to Deleted, and why

Asana — Today
Asana — Recently Assigned
Asana — Urgent flags

Jira — Assigned to Karen (active sprint only — name the sprint(s) checked from `active_sprints`, even when the list is empty; an empty sprint-assignment list is a normal, correct result, not a gap)
Jira — New mentions (include the `mentions_caveat` string from the source output right under this header — it's a heuristic, say so every time; if `mentions_excluded_replied_count` > 0, note it inline, e.g. "3 mentions found, 2 already replied to — 1 below")

Today's Priorities            <- synthesis, not a new data source (see §3)
```

## 3. Today's Priorities synthesis

After all housekeeping sections are composed, write a short "what actually matters today" section by looking across everything above — not a separate data pull. Keep it to a handful of bullets, most important first. This is the one place light judgment/synthesis is appropriate; everything else in the report must stay factual and traceable to source data.

## 4. Send

- Recipient: Karen's own mailbox (the same address confirmed via `get_me` in `daily-brief-email-triage`).
- Send via the Microsoft 365 MCP mail-send tool.
- The Kari activity rollup is **not** sent from here — `daily-brief-email-triage` already sends that separately to kari@kasa.ca in its own step.

## 4a. Token cost in the subject line (2026-08-10)

The orchestrator (`daily-brief`) passes either `data_gathering_tokens` (a number) or `data_gathering_tokens_partial: true` (one of the three source calls didn't report a figure) alongside the source output contracts. This number covers steps 1–3 (email-triage, Asana, Jira) only — it never includes this compose step's own token cost, which can't be known before compose finishes running.

- `data_gathering_tokens` present → subject suffix: `~{N} tokens (excl. compose)`.
- `data_gathering_tokens_partial: true` instead → subject suffix: `tokens: partial (some steps unreported)`. Never guess a number to fill the gap.
- Neither passed (e.g. an older orchestrator run predating this feature) → omit the suffix entirely rather than inventing one.

## 5. Failure handling

- If composing/sending itself fails, do not silently drop the report — surface the failure directly in the conversation so Karen (or whoever's running this) knows the morning brief did not go out.