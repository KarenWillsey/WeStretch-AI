---
name: app-store-specialist-monthly-refresh
description: Use once a month (or on demand, e.g. "refresh the Apple knowledge base") to check developer.apple.com for anything new or changed against the Apple Opportunity Radar's Knowledge Base. Fetches each tracked source URL live, diffs against the last saved snapshot, updates changed sections, and always reports completion — including "nothing changed" — to state/monthly-refresh-log.json and state/last-run.log.
---

# Apple Opportunity Radar — Monthly Knowledge Refresh

Reference: `Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Implementation Spec.md` section 2 for the full design this implements. Read `Memory.md` in that same folder for standing decisions (scope is broad; refresh must fetch live; Manager must always be notified of completion, even a clean run).

Paths below are relative to `Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/`.

## 0. Setup

- Knowledge Base: `Knowledge Base/apple-marketing-opportunities.md`
- Structured state: `state/monthly-refresh-log.json`
- Shared banner log: `state/last-run.log` (also used by the nightly-action skill — prefix your lines with `[monthly-refresh]` so both run types stay distinguishable in one file)

## 1. Fetch each tracked source URL

Use the confirmed source URL list in `Implementation Spec.md` section 1 ("Confirmed source URLs") — one URL per Knowledge Base section. Fetch each with WebFetch. If a URL 404s or clearly moved, don't guess a replacement — record it as a fetch failure for that section and keep the existing Knowledge Base content for it untouched.

Also check the "still-unconfirmed candidates" list (Apple Search Ads, App Clips, a TestFlight overview page, a general Apple Developer News feed) via WebSearch once per run — if you find a solid canonical URL for one, add it to the "Confirmed source URLs" list in `Implementation Spec.md` and give it a new Knowledge Base section next run (don't invent a full section from a single search result in the same run you found it — flag it as a candidate addition instead, so a human can sanity-check before it becomes tracked "fact").

## 2. Diff against the last snapshot

For each fetched page, compare its substantive content (limits, features, requirements, process steps) against that section's current text in the Knowledge Base. Ignore cosmetic differences (page redesign, wording tweaks that don't change meaning, formatting). Only count it as a real change if something a WeStretch decision-maker would act differently on has changed — a limit changed, a feature added/removed, a new requirement, a process step added.

## 3. Update the Knowledge Base for real changes only

For each section with a real change:
- Update that section's bullet list to reflect the new reality.
- Update its "Source" line's implicit last-verified date by adding a dated changelog entry at the top of the file (don't remove prior changelog entries — this file's changelog is a running history).
- If the change surfaces a new opportunity WeStretch hasn't acted on, add it to `Backlog.md` under "Not started," with a one-line note of why (e.g. "new 2026-09 — In-App Events now allow X").

Sections with no real change: leave untouched, do not touch their Source line or add a changelog entry for them.

## 4. Always write structured state (even a clean run)

Append one entry to `state/monthly-refresh-log.json` (a JSON array — read the existing array, append, write back the whole array; create it as `[]` first if it doesn't exist yet). Entry shape:

```json
{
  "run_at": "2026-09-01T07:00:00-06:00",
  "urls_checked": [{"url": "...", "status": "ok|failed|not_found", "changed": true|false}],
  "changes_found": ["one-line description", "..."],
  "new_backlog_items": ["..."],
  "candidate_urls_found": ["..."]
}
```

`changes_found` and `new_backlog_items` are empty arrays on a clean run — an empty array is the expected, valid "checked, nothing new" result, never a reason to skip writing the entry.

## 5. Always write the banner log

Append to `state/last-run.log`:
`[monthly-refresh] [ISO timestamp] Checked N URLs, M changed, K new backlog items. <one-line summary or "No changes found.">`

This must happen even if step 1 failed entirely for every URL — in that case log `[monthly-refresh] [timestamp] FAILED: could not reach any tracked URL (see monthly-refresh-log.json for per-URL errors).` Never let a failed run produce silence.

## 6. Notify the Manager and CMO

Add a short entry to root `WORK-TRACKER.md` under a "CMO — Apple Opportunity Radar monthly refresh" heading (create it if it doesn't exist) summarizing this run — even a clean run gets a line, dated, so it's visible at the next session start rather than silently sitting only in the JSON log. Once acknowledged in a future session, that WORK-TRACKER line can be removed per the file's own rule 3 (don't let it go stale).

## Failure handling

- A single URL failing doesn't fail the whole run — keep going, record it, move on.
- If every fetch fails (e.g. no network), still complete steps 4–6 with the failure recorded — don't exit early and leave no trace of the attempt.
