# CIO; Data Governance Review: Multiplayer Stretching

_Skill applied: `Team/CIO/skills/data-governance-review`_

## What data is collected and why

Multiplayer stretching introduces **cross-user visibility** into data that was previously single-user-scoped: routine completion status, streaks, and (indirectly) activity timing/frequency, now visible to other members of a shared "stretch party." This is new: it's the first feature where one user's activity data is shown to another user, not just to WeStretch itself.

## Access control

- A user's completion/streak data should be visible **only** to members of a session they explicitly joined; never broadly visible (e.g., no public leaderboard of all users' activity by default, consistent with [cpo.md](cpo.md)'s decision to cut public matchmaking).
- Leaving or muting a party (per [cxo.md](cxo.md)) should also revoke that user's data visibility to remaining members going forward, a left session shouldn't continue exposing new activity to people no longer sharing it.
- Invite acceptance should be the explicit consent gate; a friend being invited doesn't imply visibility until they accept.

## Compliance exposure

- Sharing activity/health-adjacent data (even something as simple as "did a stretch today") between users is a step up in sensitivity from solo tracking, and app store health-data policies (Apple/Google) generally require clear disclosure when health-related data becomes visible to other users, not just to the app itself. Update in-app disclosure/consent copy at the invite-accept step, not buried in general terms of service.
- No indication this triggers new regional privacy-law obligations beyond what solo tracking already requires, but confirm with counsel if any biometric/wearable data (vs. simple completion status) is ever surfaced to other users.

## Recommendations

1. **Must fix before launch**: explicit, in-flow consent at invite-accept ("X will be able to see when you complete this routine"), not just general ToS coverage.
2. **Must fix before launch**: leaving a session revokes future visibility, enforced at the data-access layer, not just hidden in the UI.
3. **Should improve**: audit logging on who can see whose completion data, so a future incident (accidental over-sharing) is debuggable.
4. **Should improve**: default session visibility to the smallest reasonable group (the invited party only), resist any future pressure to default to broader visibility for engagement's sake.
