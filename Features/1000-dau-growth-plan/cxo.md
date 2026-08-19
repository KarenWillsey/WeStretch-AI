# CXO — Customer Journey & Activation: Path to 1,000 DAU

_Skills applied: `Team/CXO/skills/customer-journey-audit`, `Team/CXO/skills/ux-design-review`_

## Customer journey audit

### Journey map

Discovery (App Store listing) → download → signup/onboarding → first workout attempt → day 2–7 → week 2+. No screenshots, flows, or actual onboarding copy are available in this repo, so the audit below is **structural** (what to check), not a review of confirmed current screens.

### Friction points, ranked by probable impact

1. **Signup before value** — if account creation happens before the user sees or does anything, that's a probable top-of-funnel leak; this is the most common activation killer in fitness apps and should be checked first.
2. **No concrete "next action" after install** — if the first screen doesn't get a user into a workout within ~60 seconds, motivation decays fast.
3. **Push-permission ask with no context** — a generic OS permission prompt with no stated benefit gets declined reflexively; this quietly kills the re-engagement channel [cgo.md](cgo.md) is counting on.
4. **No moment to invite a friend** — the flip side of [cgo.md](cgo.md)'s referral experiment: if there's no natural point in the journey to share a win, the growth loop has nowhere to attach.

### Quick wins vs. structural fixes

- **Quick (days, no new infra)**: defer account creation until after a first-workout preview; add a specific, benefit-framed push-permission prompt; add a share moment right after first completion.
- **Structural (needs product/eng investment)**: a full onboarding redesign with a proper activation-event funnel — this depends on [cio.md](cio.md)'s instrumentation existing first, otherwise "did the redesign work" is unanswerable.

### Success metric

Activation rate — % of installs completing a first workout within 24 hours — and D1 retention. Both require [cio.md](cio.md)'s event instrumentation to measure; until then this is a design change made on faith, not a measured one, and should be labeled as such internally.

## UX design review (applied to the onboarding/activation flow generally, no specific screens provided)

- **Clarity**: a first-time user should be able to reach their first workout without creating an account first — if the current flow requires signup up front, that's the single highest-priority UX fix in this plan.
- **Consistency**: no existing brand/visual language is documented (same gap [cmo.md](cmo.md) flags) — cannot verify consistency against a standard that doesn't exist on paper yet.
- **Accessibility**: tap targets and one-handed use matter more here than in a typical app, since users are often mid-stretch/mid-workout when interacting — flag this as a review criterion for whatever onboarding screens get built, not a finding against current screens (none were provided).
- **Emotional tone**: a missed-day nudge should read as re-invitation, not guilt — this matters directly for the streak-recovery intervention in [cgo.md](cgo.md); a shaming tone would actively work against the retention goal it's meant to serve.
