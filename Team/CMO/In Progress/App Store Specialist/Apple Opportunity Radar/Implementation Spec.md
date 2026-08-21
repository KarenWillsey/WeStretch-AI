# Apple Opportunity Radar — Implementation Spec (v1, planning stage)

Status (2026-08-21): **Planning spec only — not built, not scheduled.**
This document is the full design so a later session can build it in one
pass. See `Memory.md` for the standing decisions this spec is built on.

## Core problem

Apple gives developers a growing set of levers to get an app seen —
product page metadata, Custom Product Pages, In-App Events, Search Ads,
TestFlight, App Clips, editorial "Nominate an app" pitches, feature-adoption
bonuses, seasonal placement — and those levers change over time as Apple
ships new App Store Connect capabilities. WeStretch currently uses a
narrow slice (screenshots + description copy, via the other App Store
Specialist sub-projects) and has no standing process to notice new
opportunities or work through the backlog of ones already known.

**Who it's for:** CMO's App Store presence work. Nightly output goes to the
Manager for review before anything ships; the Manager is also the one
expected to notice if a scheduled run didn't fire.

## Reliability bar (matches the daily-brief precedent)

- **Fail loud, never silent.** Every scheduled run — nightly or monthly —
  writes to `state/` whether it succeeded, found nothing, or failed. No run
  is allowed to simply not report.
- **Manager checks the schedule, not just the output.** At the start of any
  session that touches this project (or, at minimum, any CMO session), the
  Manager reads `state/last-run.log` and `state/monthly-refresh-log.json`
  timestamps. If the nightly run is more than ~36 hours stale, or the
  monthly refresh is more than ~35 days stale, the Manager flags it to
  Karen immediately and offers to trigger a manual re-run in that session.
- **No unverified content.** Knowledge Base updates must trace back to an
  actual fetched Apple page (URL + fetch date recorded), not the model's
  general knowledge of Apple's platform.

## Scope

### 1. Knowledge Base — what gets tracked

`Knowledge Base/apple-marketing-opportunities.md`, one section per lever
below. Each section: current rules/specs (summarized, not copy-pasted),
source URL(s), last-verified date, and an "opportunity seeds" subsection —
concrete things WeStretch hasn't done yet in that category.

**Seeded 2026-08-21** with a real baseline Karen compiled from
developer.apple.com directly (App Store Listing, Screenshots and Videos,
Ratings and Reviews, Custom Product Pages, App Store A/B Testing, App Store
Events, Subscriptions and Free Trials, Billing Recovery and Subscriber
Retention, Revenue and Apple Commissions, Analytics and Measurement,
Notifications and Engagement, Accessibility, Privacy and Customer Accounts,
Health and Fitness Claims, App Review and Releases, Getting Featured by
Apple — 16 sections, each with its own Source line). That file's actual
section headers are now the authoritative list; the 12-item outline below
is this spec's original planning list and is superseded by it, kept here
only for the "why these categories matter" framing. The monthly refresh,
once built, diffs against this 2026-08-21 baseline rather than starting
from nothing — see the Knowledge Base file's own Changelog section.

1. **Product page metadata** — name/subtitle/keywords/description/promo
   text/what's-new limits and indexing rules. (Baseline already exists in
   `.agents/skills/aso/references/apple-specs.md`, March 2026 snapshot —
   first refresh run should import and then supersede it.)
2. **Screenshots & App Previews** — device/size requirements, video specs.
3. **Custom Product Pages (CPPs)** — up to 70 pages, organic search
   inclusion since July 2025, per-CPP keyword uniqueness.
4. **Product Page Optimization** — A/B testing icons/screenshots/previews.
5. **In-App Events** — challenge/competition/season badges, editorial
   placement, pre-event promotion window.
6. **Apple Search Ads** — placements, keyword bidding (flag as a paid
   channel needing budget sign-off, not something the nightly run spends
   money on unilaterally).
7. **TestFlight** — public links, beta distribution as an acquisition/hype
   channel.
8. **App Clips** — lightweight instant-experience acquisition lever.
9. **Editorial pitches** — App Store Connect's "Nominate an app" /
   promotional request process for Today tab / category features.
10. **Feature-adoption bonuses** — Apple's tendency to editorially feature
    apps that adopt new OS capabilities early (widgets, Live Activities,
    StandBy, Apple Intelligence integration, etc.) — flag as CTO-adjacent
    opportunities, not something this project builds itself.
11. **Ratings & reviews** — SKStoreReviewController prompt-frequency limits
    (compliance boundary, but affects social-proof strategy).
12. **Seasonal moments** — recurring known windows, e.g. Apple's "New Year,
    New You" fitness-category push each January — directly relevant to a
    stretching app; should generate recurring backlog items with enough
    lead time to act (build starting well before the window, not in it).

**Confirmed source URLs** (from the 2026-08-21 baseline, one per Knowledge
Base section — these are the fetch list the monthly refresh should use):
`developer.apple.com/app-store/product-page/`,
`.../app-store/ratings-and-reviews/`, `.../app-store/custom-product-pages/`,
`.../app-store/product-page-optimization/`, `.../app-store/in-app-events/`,
`.../app-store/subscriptions/`, `.../app-store/small-business-program/`,
`developer.apple.com/videos/play/tech-talks/111433/` (Accessibility),
`.../app-store/user-privacy-and-data-use/`,
`developer.apple.com/support/offering-account-deletion-in-your-app/`,
`.../app-store/review/guidelines/`, `developer.apple.com/distribute/app-review/`,
`.../app-store/getting-featured/`.

**Still-unconfirmed candidates** (levers worth tracking but no source URL
pinned down yet — confirm at build time): Apple Search Ads, App Clips, a
dedicated TestFlight overview page, and a general Apple Developer News feed
for cross-cutting announcements.

### 2. Monthly refresh workflow

Runs once a month (proposed: 1st of month, morning).

1. Read the Knowledge Base's stored per-section snapshot + last-verified date.
2. Fetch each tracked URL live.
3. Diff meaningfully against the last snapshot (ignore cosmetic/formatting
   noise; care about limits, new features, new sections, removed features).
4. For each real change: update that Knowledge Base section, and append a
   dated entry to a changelog block at the top of the file.
5. **Always** write a run summary to `state/monthly-refresh-log.json`
   (timestamp, per-URL fetch success/failure, list of changes found — even
   an empty list). This is what makes "ran, found nothing new" a valid,
   visible outcome instead of silence.
6. Notify the Manager and CMO: if changes were found, summarize what's new
   and which opportunity seeds it implies; if nothing changed, still report
   that the check ran and came back clean. (Delivery mechanism: written
   into `state/monthly-refresh-log.json` plus a short note the Manager
   surfaces at the next session start — no separate email channel unless
   Karen wants one added later.)
7. If a new opportunity category or seed emerges, add it to `Backlog.md`.

### 3. Nightly action workflow

Runs once an evening (proposed: ~8:00pm).

1. Read `Backlog.md`, take the top not-yet-done item in priority order.
2. Execute it — routing to whichever existing pipeline fits (e.g. the
   `App Store Image Text Copywriting` or `App Store Image Creation`
   sub-projects for asset-shaped items) or doing direct research/drafting
   for process-shaped items (e.g. drafting the actual editorial-pitch
   submission text, or a CPP test plan).
3. Write one dated output file to `Output/` (e.g.
   `Output/2026-09-15-cpp-ab-test-plan.md`) — this is the result the
   Manager reviews. Never auto-publish/auto-submit anything to Apple; every
   nightly item produces a draft/plan for review, not a live action.
4. Mark the item done in `Backlog.md` (date + link to its output file).
5. **Always** write to `state/last-run.log`, including the no-op case
   ("backlog empty, nothing to run — needs new seeds") — this must never
   fail silently.
6. Add a line for the new output under a "CMO — App Store Specialist
   pending Manager review" section in root `WORK-TRACKER.md`, mirroring
   the existing `Team/CMO/Review ToDo/` convention — removed once Karen/Manager
   has reviewed it.

### 4. Backlog seeding

`Backlog.md` is seeded (as of 2026-08-21) directly from the Knowledge
Base's "Highest-Priority Actions for WeStretch" list — 10 concrete,
sourced items (Small Business Program enrollment, Billing Grace Period,
screenshot A/B test, CPPs by use-case, localization, review-prompt timing,
an In-App Event challenge, subscription offers, accessibility/privacy
compliance sweep, and an Apple Featuring Nomination). This replaces the
earlier generic 6-item placeholder list this spec originally proposed.

Not exhaustive — the monthly refresh and ad hoc Manager/CMO input both feed
new items in over time.

## Architecture

Two Claude Code project skills, matching this repo's "one skill = one task"
convention, living under `.claude/skills/` (not `Team/ROLE/skills/`) because
both need to be actually invocable/schedulable:

- `app-store-specialist-monthly-refresh` — implements the workflow in
  section 2.
- `app-store-specialist-nightly-action` — implements the workflow in
  section 3.

## Scheduling

Two Windows Scheduled Tasks, same pattern as
`Team/CEO/In Progress/Set Up Daily Housekeeping/run-daily-brief.ps1`:

- **"WeStretch App Store Specialist — Nightly"** — fires each evening,
  invokes Claude Code CLI (`--print --dangerously-skip-permissions`)
  against the nightly-action skill, logs to `state/last-run.log`.
- **"WeStretch App Store Specialist — Monthly Refresh"** — fires monthly,
  same invocation pattern against the monthly-refresh skill, logs to
  `state/monthly-refresh-log.json`.

Both only fire if Karen's machine is on and she's logged in at that hour —
same caveat as the daily brief. This is exactly why the Manager-side
staleness check in the "Reliability bar" section above matters: a missed
evening needs to be caught and offered as a re-run, not silently dropped.

## State tracking

Not created yet — will live under `state/` once built:

- `state/last-run.log` — nightly run history (timestamp, item worked,
  success/no-op/failure).
- `state/monthly-refresh-log.json` — monthly refresh history (timestamp,
  per-URL fetch status, changes found).

Git-versioned like the daily brief's state files, for the same reason: an
inspectable history of what was actually checked and when.

## Open items — flag if wrong

- **Exact nightly/monthly fire times** — proposed 8:00pm and 1st-of-month
  morning; not yet confirmed with Karen.
- **Source URL list** — candidates listed above need verifying at build
  time; some may 404 or have moved.
- **Notification channel** — currently proposed as "Manager surfaces it at
  next session start" (reusing the WORK-TRACKER/session-start check
  pattern already used elsewhere in this repo). If Karen wants an actual
  push notification or email for monthly-refresh findings, that's an
  additional build step, not assumed here.
- **Apple Search Ads and paid spend** — this project should surface the
  opportunity and a plan, but should not be assumed to have authority to
  spend budget; likely needs CRO/CFO sign-off before executing.

## Explicitly out of scope for now

- Actually building the two skills.
- Registering the two Windows Scheduled Tasks.
- ~~Populating the Knowledge Base~~ — done 2026-08-21 (Karen-provided
  baseline); what's still not built is the *automated* monthly refresh that
  keeps it current going forward.
- Any live submission to Apple (editorial pitch, CPP publish, Search Ads
  campaign) — nightly output is always a draft for Manager/Karen review.

## Build order (once Karen greenlights execution)

1. Verify/finalize the source URL list.
2. Build `app-store-specialist-monthly-refresh`, run it once manually to
   populate `Knowledge Base/apple-marketing-opportunities.md` for real.
3. Build `app-store-specialist-nightly-action`, run it once manually
   against a seeded backlog item to confirm the Output/WORK-TRACKER loop works.
4. Register both Windows Scheduled Tasks.
5. Add the Manager-side staleness check to root `WORK-TRACKER.md`'s
   session-start routine (currently just documented here, not yet wired
   into that file's rules).
