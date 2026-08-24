---
name: app-store-specialist-nightly-action
description: Use each evening (or on demand, e.g. "work the next App Store opportunity") to take the top item off the Apple Opportunity Radar's backlog, produce a draft/plan for it, and hand it to the Manager for review. Never publishes or submits anything live to Apple — every run produces a reviewable draft file.
---

# Apple Opportunity Radar — Nightly Action

Reference: `Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Implementation Spec.md` section 3 for the full design this implements.

Paths below are relative to `Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/`.

## 0. Setup

- Backlog: `Backlog.md`
- Output folder: `Output/`
- Knowledge Base (context for whatever item you're working): `Knowledge Base/apple-marketing-opportunities.md`
- Shared banner/summary log: `state/last-run.log` (also used by the monthly-refresh skill — prefix your lines with `[nightly-action]`)

## 1. Pick the item

Read `Backlog.md`. Take the first unchecked item under "Not started," top to bottom (the file's order is the priority order). If the list is empty, skip to step 5 (no-op case) — do not invent a new item yourself; that's the monthly refresh's job (or Karen's/the Manager's, ad hoc).

## 2. Execute it

What "execute" means depends on the item's shape — be honest about what you can and can't verify:

- **Drafting-shaped items** (write copy, draft a nomination pitch, draft an event description, draft an A/B test plan) — produce the actual draft content, ready for review. Pull relevant specifics from `Knowledge Base/apple-marketing-opportunities.md` (character limits, required fields, etc.) so the draft is usable as-is.
- **Asset-shaped items** (screenshots, images) — route to the relevant existing sub-project instead of improvising: see `Team/CMO/In Progress/App Store Specialist/App Store Image Creation/` and `.../App Store Image Text Copywriting/`. Produce a plan/brief for that pipeline to execute, don't try to generate final assets from inside this skill.
- **Verification/compliance-shaped items** (confirm Small Business Program enrollment, confirm accessibility/privacy compliance, confirm rating-prompt cadence) — you do not have App Store Connect or production-app access. Do not claim something is confirmed/done. Instead produce a checklist: exactly what to check, where in App Store Connect or the codebase to check it, and what "pass" looks like — addressed to whoever does have that access.
- **Research-shaped items** (investigate a channel, e.g. TestFlight public-link distribution) — produce a short brief: what it is, why it's relevant to WeStretch specifically, and a concrete recommended next step.

Never take a live action against Apple (no submitting an event, nominating an app, publishing a CPP, starting an A/B test) — everything this skill produces is a draft or plan for a human (or a later, explicitly-approved step) to act on.

## 3. Write the output

One dated file in `Output/`, named `YYYY-MM-DD-<short-slug>.md` (e.g. `2026-09-15-cpp-plan-back-pain.md`). Include at the top: which backlog item this addresses, and today's date.

## 4. Update the backlog

Move the item from "Not started" to "Done" in `Backlog.md`, with the date and a relative link to its output file.

## 5. Always write the banner log (including the no-op case)

Append to `state/last-run.log`:
- Normal case: `[nightly-action] [ISO timestamp] Worked "<item>" -> Output/<file>.md`
- No-op case: `[nightly-action] [ISO timestamp] No-op: backlog is empty, nothing to run. Needs new seeds (next monthly refresh, or Karen/Manager ad hoc).`

This must happen every run, success or no-op — never let a run finish silently.

## 6. Hand off to the Manager for review

Add a line under a "CMO — App Store Specialist pending Manager review" heading in root `WORK-TRACKER.md` (create it if it doesn't exist), pointing at the new `Output/` file, dated — mirrors the existing `Team/CMO/Review ToDo/` convention. Remove that line once Karen/Manager has reviewed the output (per `WORK-TRACKER.md`'s own rule 3).

## Failure handling

- If execution genuinely can't produce anything useful (e.g. the item depends on information nobody has provided), still write an `Output/` file explaining exactly what's blocking it and what's needed to unblock it — leave the backlog item in "Not started" (don't mark it done), and say so plainly in the `last-run.log` line and the WORK-TRACKER entry.
