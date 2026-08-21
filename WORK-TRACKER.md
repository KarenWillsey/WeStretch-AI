# Work Tracker

One place to see every open task across the whole repo — so nothing gets
lost across chats, roles, or people. The Manager (root `CLAUDE.md`) owns
this file.

## Rules
1. Any open item (decision needed, unfinished work, gap, blocked task)
   gets a line here **in the same session it's found** — same time it's
   noted in that project's own `Memory.md`.
2. Check this file at the start of any session before starting work.
3. Delete or check off a line the moment it's resolved. Don't let this
   file go stale — it's only useful if it's current.
4. Format: `- [ ] item — path/to/project — flagged YYYY-MM-DD`
5. **`Ideas/` folders are excluded — never add items from there.** Not
   active work yet; the Manager surfaces those separately, on request,
   when looking for new work to start.
6. Items in a role's `Review ToDo/` folder go here too. Once Karen approves
   one, move it wherever it actually belongs (not always `Ready/`) and
   remove its line here.
7. Check every role's `Review ToDo/` folder at the start of any session
   (not just the ones already listed below) — a file sitting there with no
   line here means this tracker has gone stale and rule 3 was missed.
8. **Scheduled-automation staleness check.** At the start of any session,
   check whether registered scheduled automations actually fired on
   schedule. Currently tracked: the daily brief (`state/last-run.log` under
   `Team/CEO/In Progress/Set Up Daily Housekeeping/`, expected every
   morning) and the Apple Opportunity Radar (`state/last-run.log` and
   `state/monthly-refresh-log.json` under `Team/CMO/In Progress/App Store
   Specialist/Apple Opportunity Radar/`, expected nightly + monthly once
   its scheduled tasks are registered — see that project's `CLAUDE.md` for
   whether that's confirmed yet). If a run is stale beyond its expected
   cadence, flag it to Karen immediately and offer to trigger a manual
   re-run in that session — don't wait for her to notice.

## CMO — website-repo
Sits in `Ready/` but has 5 open items in its own tracker — folder location
may need revisiting (Ready usually means done, this isn't). Full detail:
`Team/CMO/Ready/website-repo/USER_TODO.md`.
- [ ] Meta Conversions API access token needs a secure home (not this repo)
  — no backend exists yet to hold it; **recommend rotating it**, since
  Karen shared it in chat rather than a secrets vault — flagged 2026-08-21
- [ ] Image self-hosting — flagged priority, hurts Lighthouse score
- [ ] DNS/domain cutover plan + access — Karen confirmed 2026-08-21 this is
  easy and ready whenever needed; window still TBD
- [ ] Remove dev-site noindex block before going live — intentionally
  deferred to launch, not blocked
- [ ] Final content review pass vs. live site

Resolved 2026-08-21 (contact form → keep mailto:, future: swap to a
WeStretch webhook API once Karen builds it; analytics/GA4/Meta Pixel IDs
provided and wired; Stripe links confirmed live; `/signup/` now redirects
home; Sign In URL confirmed correct; social links confirmed; no video
needed) — see `USER_TODO.md` for detail, removed from this list per rule 3.

## CMO — Apple Opportunity Radar (fully live 2026-08-21)
- [ ] Recommended: trigger one manual run of each skill in a live session
  to confirm the Output/WORK-TRACKER/state-file loop works end to end
  before the unattended schedule fires for real (nightly first fires
  2026-08-21 8:00 PM, monthly first fires 2026-09-01 7:00 AM) — see that
  project's Implementation Spec "Recommended next step" — flagged 2026-08-21

Resolved 2026-08-21: both skills built, wrapper scripts built, state files
initialized, Knowledge Base seeded with Karen's baseline, both Windows
Scheduled Tasks registered and `Ready` (monthly one needed a `.cmd`-batch-
file workaround for PowerShell quoting — see project `Memory.md` if it
ever needs redoing), Manager staleness-check rule wired into this file's
rule 8.

## CMO — Review ToDo/ (awaiting Karen's approval)
Nothing currently pending. `female-actor-01-pigeon-pose-park.webp` and
`female-actor-01-pigeon-pose-park reversed.jpg` were exploratory variants
tried for the homepage hero and superseded — never separately approved,
no action needed on them.

Resolved 2026-08-21: homepage hero image locked in — three variants tried
(`female-actor-01-cobra-studio-hero.webp`, then the pigeon-pose park
photo, then `female-actor-01-pigeon-pose-warm-readable-hero.webp`), Karen
confirmed the warm-readable one is best. Deployed to
`public/images/hero-home.webp` in website-repo: cropped for tight
headroom, full width/full height kept (no bottom crop, per Karen's
instruction), resized ~7% to cover wide desktop viewports without a seam.
Text-shadow added to the overlaid hero text (`src/pages/index.astro`) for
legibility. Source files left in place in `Review ToDo/` as the CMO asset
archive copies.

## CXO — Onboarding UX Flow Spec
- [ ] Karen to review proposed drip sequence (Claude's draft) — `Team/CXO/In Progress/Onboarding UX Flow Spec/Storyline.md` — 2026-08-21
- [ ] No visual design for Home, Set Your Goal, Streak Saver Offer — `Team/CXO/In Progress/Onboarding UX Flow Spec/Screen-Inventory.md` — 2026-08-21
- [ ] Goal 1 fix (leaderboard dead-end) not decided — `Team/CXO/In Progress/Onboarding UX Flow Spec/Screens/Home.md` — 2026-08-21
- [ ] ~15 more small open questions (body_filter list, "too fast" stacking, etc.) — see `Team/CXO/In Progress/Onboarding UX Flow Spec/Global-Goals.md` and `State-Variables.md`
