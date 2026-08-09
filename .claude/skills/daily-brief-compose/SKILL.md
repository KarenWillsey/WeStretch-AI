---
name: daily-brief-compose
description: Use when merging daily-brief-email-triage, daily-brief-asana, and (once built) daily-brief-jira output into Karen's final morning brief email — runs the fail-loud verification pass, formats for scanning not reading, and sends the report to Karen's own inbox.
---

# Daily Brief — Compose

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md`.

This skill does not pull any data itself — it only merges structured output already produced by the source skills (`daily-brief-email-triage`, `daily-brief-asana`, and `daily-brief-jira` once it exists) and sends the final report.

## Format requirement — this is the whole point of the brief

Karen has a reading disability; the brief must be **scanned, not read**. Every section:

- Short lines. No dense paragraphs, ever.
- Clear, bolded section headers.
- Bolded subject/task/ticket names so the eye catches them first.
- Each item carries its reference (email thread ID, Asana task URL, Jira ticket key) so a follow-up chat session can act on it directly without re-searching.
- **Deleted** section specifically: one item per line, **sender/company name bolded** first, then a summary under one sentence — e.g. `**Halara** — clothing sale promo.` Karen asked for this exact shape so the list is fast to scan.
- If a section has nothing to report, say so in one line ("Nothing needs your attention here today") rather than omitting the header — an omitted section reads as "not checked," which violates the fail-loud rule.

## 1. Verification pass (do this before composing anything)

- Confirm every source skill that ran actually returned output — if `daily-brief-email-triage` or `daily-brief-asana` didn't run or errored entirely, the top of the report must say so explicitly, not just skip that section.
- Carry forward every `couldnt_check` entry from each source verbatim into a single **Couldn't Check Today** section near the top of the report — this is the most important section for the fail-loud reliability bar and must never be buried.
- Do not paraphrase or summarize facts (subjects, counts, task names) beyond what the source skill already produced — compose only reorganizes and formats, it doesn't reinterpret.

## 2. Report structure

```
Subject: Daily Brief — [date]

[Couldn't Check Today]        <- only if non-empty, but check first, show first

Needs My Attention             <- Unsubscribe-folder items that might have value (recurs daily until Karen clears them)
Threads Waiting On You         <- inbox items needing a reply or a reply from someone else
Other Inbox Mail                <- everything else currently in the inbox, one line each
Deleted                        <- few-word summaries of what got moved to Deleted, and why

Asana — Today
Asana — Recently Assigned
Asana — Urgent flags
Asana — Unresolved notifications (if any)

Jira — Assigned & Mentions    <- only once daily-brief-jira exists; omit section entirely (not "no data") until then

Today's Priorities            <- synthesis, not a new data source (see §3)
```

## 3. Today's Priorities synthesis

After all housekeeping sections are composed, write a short "what actually matters today" section by looking across everything above — not a separate data pull. Keep it to a handful of bullets, most important first. This is the one place light judgment/synthesis is appropriate; everything else in the report must stay factual and traceable to source data.

## 4. Send

- Recipient: Karen's own mailbox (the same address confirmed via `get_me` in `daily-brief-email-triage`).
- Send via the Microsoft 365 MCP mail-send tool.
- The Kari sent-mail rollup is **not** sent from here — `daily-brief-email-triage` already sends that separately to kari@kasa.ca in its own step.

## 5. Failure handling

- If composing/sending itself fails, do not silently drop the report — surface the failure directly in the conversation so Karen (or whoever's running this) knows the morning brief did not go out.