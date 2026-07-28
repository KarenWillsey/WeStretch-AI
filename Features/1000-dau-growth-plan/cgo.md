# CGO — Growth & Retention: Path to 1,000 DAU

_Skills applied: `CGO/skills/retention-funnel-analysis`, `CGO/skills/growth-experiment-design`_

## Retention funnel analysis

### Funnel read

No analytics stack is confirmed in this repo (see [cio.md](cio.md) — this is a real gap, not a formality). Absent real data, the funnel below is a **category-typical assumption for a fitness app**, not a WeStretch-specific read:

- Biggest drop: **install → first completed workout** (many users never reach the product's core value moment).
- Second-biggest drop: **day 1 → day 7** (novelty wears off before a habit forms).
- Smaller, steadier drop from day 7 → month 2 (motivation dips, plateaus, life interruptions).

Confidence: **low** until [cio.md](cio.md)'s instrumentation gap is closed. Treat everything below as the plan to run once real numbers exist, not a diagnosis of what's actually wrong today.

### Likely drivers

- Onboarding shows the app before it shows the payoff — no "aha" moment inside the first session (product/UX cause).
- No re-entry hook after session 1 — nothing brings a user back on day 2 (product cause, fixable without new infra).
- No social proof or accountability loop — solo habit formation is fragile by default (this is the underlying value-prop gap the multiplayer/social work in [cpo.md](cpo.md) targets).

### Interventions

1. Streak-recovery nudge (a missed day doesn't feel like failure, re-engages same-day).
2. Day-1 and day-3 re-engagement push tied to a concrete next action, not a generic reminder.
3. A share-a-win moment immediately after the first completed workout — this doubles as the seed of the referral loop below.

### Prioritized next step

Given zero marketing budget, the highest-leverage single move is **not** a retention nudge — it's turning existing users into the acquisition channel, since there's no other channel funded. See the experiment below.

## Growth experiment design

### Hypothesis

Adding a one-tap "invite a friend" prompt immediately after a user's first completed workout increases installs-per-existing-user (K-factor) enough that organic referral, not paid acquisition, can plausibly carry WeStretch from ~200 to 1,000 DAU inside the 3-month window.

### Design

- **Variant**: after first workout completion, show a one-tap share/invite prompt with a specific, concrete hook (not "check out this app").
- **Control**: existing completion screen, no prompt.
- Randomize at the user level, not the session level.
- Requires a working invite link with attribution — this is a dependency on [cto.md](cto.md), not something CGO can ship alone.

### Success metric and threshold

- **Primary metric**: K-factor (installs attributed to invites ÷ inviting users) measured over a rolling 2-week window.
- **Threshold**: pre-register **K ≥ 0.15** as the bar for "this loop can plausibly get us to 1,000 DAU without paid spend" — this is a judgment call being set now, before results, precisely to avoid rationalizing a weak number later. If the actual figure differs meaningfully once real usage data exists, revisit the threshold explicitly rather than quietly moving the goalposts.
- If K comes back below threshold, that's the signal to escalate to [cfo.md](cfo.md)/CEO on whether to inject a small paid budget or extend the timeline — not to keep iterating on the same organic loop indefinitely.

### Risks

- **Sample size**: at a ~200 DAU base, the invited cohort will be small for the first 2-4 weeks — reading K-factor too early will be noisy. Don't call the experiment before a large-enough invited cohort exists.
- **Confound with other launches**: don't run this alongside a pricing change ([cro.md](cro.md)) or a paywall change in the same window — either would contaminate the retention/K-factor read.
- **Ceiling risk**: a strong K-factor compounds slowly at a small base — even K = 0.2 takes several cycles to meaningfully move 200 → 1,000 DAU inside 12 weeks. This experiment de-risks the *channel*, it does not guarantee the *timeline*. Flagged again in [synthesis.md](synthesis.md).
