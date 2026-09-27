# CIO; Data Systems & Governance: Path to 1,000 DAU

_Skills applied: `Team/CIO/skills/data-systems-audit`, `Team/CIO/skills/data-governance-review`_

## Data systems audit

### System inventory

**Not documented anywhere in this repo.** This is the single biggest blind spot in the entire plan: if there is no reliable, single source of truth for DAU today, the company cannot know whether 1,000 DAU has actually been reached, nor which of [cgo.md](cgo.md)'s, [cxo.md](cxo.md)'s, or [cmo.md](cmo.md)'s levers moved it. This gap should be closed before any other workstream, not in parallel with equal priority.

### Gaps and redundancy

- No confirmed analytics tool, meaning no confirmed definition of "DAU" itself; does it mean app-opened, session-started, or workout-completed? These produce different numbers. **Lock one definition in week 1** and use it everywhere in this initiative, including in [coo.md](coo.md)'s definition-of-done.
- No confirmed attribution system, meaning [cgo.md](cgo.md)'s K-factor experiment has no way to credit installs to invites without one being built.

### Risk flags

Every system referenced above has an unclear or unconfirmed owner. Recommend a named DRI for "growth analytics" specifically, distinct from general product analytics if one already exists, so this doesn't fall through org cracks during a fast-moving quarter.

### Recommendations, ranked

1. Instrument DAU/activation/retention events and lock the DAU definition, blocks everything else.
2. Wire up referral/install attribution: blocks [cgo.md](cgo.md)'s experiment from producing a trustworthy read.
3. Everything downstream (dashboards, weekly reporting cadence) is secondary to the above two.

## Data governance review

### What data is collected and why

Unknown: no data inventory exists in this repo. Treat WeStretch's fitness/activity data as sensitive by default per standard practice for this category, until an actual inventory says otherwise.

### Access control

Cannot be assessed without a system inventory (see above). Flagged as unknown, not assumed adequate.

### Compliance exposure

The referral/invite flow and any push-notification targeting introduce new handling of user contact data; if the app connects to wearables or health platforms at all, note that **Android restricts socially sharing data obtained through health permissions without informed consent** (same point raised in [`CHATTY_REVIEW.md`](../Multiplayer Stretches/CHATTY_REVIEW.md) for the prior multiplayer effort); this applies here too if the invite/share flow touches any workout data sourced from a health permission. Confirm data sourcing before shipping the share/invite feature, don't assume it's clear.

### Recommendations

- **Must fix before shipping the referral loop**: confirm what data (if any) an invite/share action exposes about the inviting user, and get explicit consent if it includes anything health-permission-sourced.
- **Should improve**: a basic data inventory doc, even a lightweight one, before this quarter's growth push scales usage significantly.
