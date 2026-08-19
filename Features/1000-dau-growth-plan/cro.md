# CRO — Pricing & Revenue: Path to 1,000 DAU

_Skills applied: `Team/CRO/skills/pricing-strategy`, `Team/CRO/skills/revenue-pipeline-review`_

## Pricing strategy

### Current state

**Unconfirmed.** No pricing tiers, conversion, ARPU, or churn-by-tier data exist in this repo. The prior planning pass on multiplayer stretching ([`Features/multiplayer-stretches/cro.md`](../multiplayer-stretches/cro.md)) assumed a free/paid split existed without confirming it — [`CHATTY_REVIEW.md`](../../CHATTY_REVIEW.md) flagged that as unverified. Same flag applies here: **confirm actual pricing structure before acting on anything below.**

### Proposal

If a paywall or usage gate exists in front of core daily-use features (workout logging, streaks, the invite flow), recommend **not** introducing new friction there during this 3-month window, and consider loosening existing gates on exactly those surfaces. The DAU goal and a revenue-maximizing paywall are in direct tension: every gate placed in front of daily use is, by construction, a DAU suppressant.

### Impact estimate

Loosening any existing paywall would plausibly cost near-term conversion/revenue to buy DAU. This is a real trade-off, not a free win, and CRO should not be expected to absorb it silently.

### Rollout plan

If any change is made: grandfather existing paying users unconditionally, communicate the change plainly, and treat it as a **time-boxed experiment for this quarter**, not a permanent pricing decision — revisit once the DAU push concludes.

## Revenue pipeline review

### Funnel snapshot

Unknown without real data — flagged as an estimate gap, not filled with invented numbers.

### Forecast vs. target

No revenue target was given for this planning pass (the stated goal is DAU, not revenue) — noting that explicitly so this doc isn't read as silently substituting a revenue goal for the DAU one.

### Levers (deferred, not abandoned)

Once the DAU push concludes, the highest-leverage revenue lever is likely the very cohort this plan produces: users acquired via referral are typically higher-intent than paid-acquired users and convert better. Recommend picking up a pricing/conversion pass in the quarter *after* this one, using data this plan will generate — not concurrently with it.

### Risks

Running a pricing test simultaneously with [cgo.md](cgo.md)'s referral experiment would confound both reads. This is called out again in [cgo.md](cgo.md)'s risk section — don't schedule them in the same window.

## Disagreement, preserved rather than resolved

CRO's normal mandate is revenue performance. This plan asks CRO to explicitly **not** optimize for revenue this quarter, and possibly to loosen monetization surfaces that would otherwise help conversion. That is a real conflict with CRO's usual KPIs, not a minor implementation detail — it should be decided explicitly by the CEO (does this quarter's revenue target get formally reduced/waived?), not quietly assumed by consensus. See [synthesis.md](synthesis.md).
