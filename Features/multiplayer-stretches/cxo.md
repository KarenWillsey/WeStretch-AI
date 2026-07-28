# CXO — UX Design Review: Multiplayer Stretching

_Skill applied: `CXO/skills/ux-design-review`_

Reviewing the proposed async "stretch party" flow: invite friends → shared routine within a 24h window → shared completion/streak view.

## Clarity

- **Invite step** must make the ask unmistakable in one glance: who's inviting, to what (which routine), by when. Avoid burying it in a generic notification — a first-time recipient who has never used WeStretch's social feature needs zero prior context to understand and act.
- **Completion view** should answer "did my friends do it?" instantly — a simple checked/unchecked or avatar-with-status list, not a stat dashboard. This is a glanceable social proof moment, not an analytics screen.

## Consistency

- Reuse WeStretch's existing routine-card and streak visual language rather than inventing a new "social" visual system — multiplayer should feel like an extension of the app users already know, not a bolted-on separate feature.
- Invite/notification copy should match the brand voice already established for solo streak nudges (see [cmo.md](cmo.md) for messaging alignment).

## Accessibility

- Session/invite screens must be usable one-handed and glanceable mid-workout — no small tap targets for "join" or "invite," consistent with the rest of the app's in-workout UI.
- If avatars/status indicators are added, don't rely on color alone to distinguish "done" vs "not done" — pair with an icon or label for contrast/colorblind accessibility.

## Emotional tone

- This is the highest-risk part of the feature: a visible "your friend didn't stretch today" or an empty completion list can read as social pressure or shame rather than motivation. Default framing should be encouraging ("cheer them on") not evaluative ("they're behind").
- Give users an easy, low-friction way to leave or mute a stretch party without it feeling like a visible "failure" or a pointed notification to the group — social features that trap users in obligation tend to get turned off entirely, which kills the retention benefit this feature exists for.

## Recommendation

Ship the invite and completion-view screens with an explicit "encouragement, not accountability-shaming" tone as a design constraint, and user-test the empty/incomplete state specifically — it's the state most likely to produce negative sentiment.
