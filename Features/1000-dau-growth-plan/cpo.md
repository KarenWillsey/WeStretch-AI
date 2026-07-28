# CPO — Roadmap & Research: Path to 1,000 DAU

_Skills applied: `CPO/skills/user-research-synthesis`, `CPO/skills/roadmap-prioritization`_

## User research synthesis

No user feedback, reviews, support tickets, or interview notes are on file in this repo. **Confidence: none — this section is a gap, not a finding.** Do not let the roadmap below substitute for real user input.

Recommended first action, week 1: pull existing App Store/Play Store reviews (if any exist) and run 5 quick user interviews with recent signups and recent churned users. This is cheap, fast, and should inform — and possibly reprioritize — the roadmap below before week 2 work starts.

## Roadmap prioritization

Candidates scored against the specific goal of **DAU growth in 12 weeks**, not general engagement:

| Initiative | Impact | Effort | Confidence | Notes |
|---|---|---|---|---|
| Referral/invite loop | High | S–M | Medium | Primary growth lever per [cgo.md](cgo.md); needs deep-linking + attribution from [cto.md](cto.md) |
| Onboarding reorder (delay signup, surface value fast) | High | M | Medium | Targets the biggest assumed funnel drop per [cxo.md](cxo.md)/[cgo.md](cgo.md) |
| Re-engagement pushes (streak recovery, day-1/day-3) | Medium | S | Medium | Cheap, but only works once push infra + analytics exist ([cto.md](cto.md)/[cio.md](cio.md)) |
| ASO copy/screenshots | Medium | S | High | No engineering dependency; do in parallel starting week 1 |
| Social/community feature (leaderboard, friend activity) | High (if it works) | L | **Low** | See cut-list rationale below |

### Ranked roadmap

1. **Analytics instrumentation is not a CPO line item but gates everything below it** — see [cio.md](cio.md). Nothing here can be confirmed as working without it.
2. **Referral/invite loop** — highest impact-per-effort given the zero-budget constraint; it's the only channel that doesn't require cash.
3. **Onboarding reorder** — addresses the largest assumed activation drop directly.
4. **Re-engagement pushes** — cheap once infra exists, meaningful lift on retention which compounds DAU.
5. **ASO** — low effort, no dependency, ship in parallel from week 1.

### Cut list

- **Social/community feature (leaderboard, friend graph, live sessions)** — explicitly deprioritized for this 12-week window. A near-identical feature was scoped in [`Features/multiplayer-stretches/`](../multiplayer-stretches/) and the independent review in [`CHATTY_REVIEW.md`](../../CHATTY_REVIEW.md) found the effort estimate for exactly this kind of feature was made without confirming whether a friend/contact graph even exists. That open question is still unresolved. Building this now, under a hard 3-month deadline with no discovery done, repeats a mistake already on record — cut it from this window and revisit only after the referral loop is validated.
- **Any new subscription tier or paywall restructuring** — see the disagreement preserved in [cro.md](cro.md)/[synthesis.md](synthesis.md); this is a distraction from the DAU goal this quarter.

### Dependencies

- Referral loop: blocked on deep-link/attribution infra ([cto.md](cto.md)) and a decision on whether invites target existing users only or non-users too (same open question flagged for the multiplayer effort — resolve it once, for the whole company, not per-feature).
- Re-engagement pushes: blocked on push infra existing at all ([cto.md](cto.md)) and on the DAU/activation events being defined ([cio.md](cio.md)).
- Everything: blocked on a locked, single definition of "DAU" — see [coo.md](coo.md)'s definition-of-done and [cio.md](cio.md).
