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

## CMO — Apple Opportunity Radar (new, planning stage)
- [ ] Karen to greenlight execution (build the 2 skills, register 2
  scheduled tasks) — spec is done, nothing built yet — `Team/CMO/In
  Progress/App Store Specialist/Apple Opportunity Radar/Implementation
  Spec.md` — flagged 2026-08-21
- [ ] Once live: add the Manager's nightly/monthly staleness check to this
  file's session-start rules (see that project's Implementation Spec,
  "Reliability bar") — not wired in yet — flagged 2026-08-21

## CMO — Review ToDo/ (awaiting Karen's approval)
- [ ] `female-actor-01-cobra-studio-hero.webp` — `Team/CMO/Review ToDo/` — 2026-08-21
- [ ] `female-actor-01-pigeon-pose-park.webp` — `Team/CMO/Review ToDo/` — 2026-08-21

## CXO — Onboarding UX Flow Spec
- [ ] Karen to review proposed drip sequence (Claude's draft) — `Team/CXO/In Progress/Onboarding UX Flow Spec/Storyline.md` — 2026-08-21
- [ ] No visual design for Home, Set Your Goal, Streak Saver Offer — `Team/CXO/In Progress/Onboarding UX Flow Spec/Screen-Inventory.md` — 2026-08-21
- [ ] Goal 1 fix (leaderboard dead-end) not decided — `Team/CXO/In Progress/Onboarding UX Flow Spec/Screens/Home.md` — 2026-08-21
- [ ] ~15 more small open questions (body_filter list, "too fast" stacking, etc.) — see `Team/CXO/In Progress/Onboarding UX Flow Spec/Global-Goals.md` and `State-Variables.md`
