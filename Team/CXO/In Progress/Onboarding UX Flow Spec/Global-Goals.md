# Global Goals

The checklist this whole spec gets held against once `Screens/` +
`Storyline.md` are drafted: for each goal below, we should be able to point
to which book/chapter/gate accomplishes it. Karen asked to be interviewed
on this before drafting goes too far, so this file starts as a working
draft from what's already been said — not finalized.

## Context: current live app post-routine flow (as described by Karen)

Routine finished →
1. Post-routine talk (animated character)
2. Badges earned (if any)
3. Streak progress
4. Collect coins earned that day
5. Goal-reached celebration sheet (conditional on hitting the day's set goal)
6. *(drip-feed education screen, on some cadence — exact trigger pattern
   not yet defined, see open item below)*
7. Leaderboard
8. User explores leaderboard (their stats, competitors' stats)

**Known problem:** step 8 is usually the last screen the user stops on.
Home screen (bottom-nav tab, holds the summary cards / full picture of the
user's progress) is not reached unless the user manually navigates there.

## Global Goals (confirmed 2026-08-19, numeric targets still TBD)

1. **Close the leaderboard dead-end.** After exploring the leaderboard,
   the flow should actively route the user to Home (not just leave it
   reachable via bottom nav) so they land on the full summary-card
   picture, not on leaderboard/competitor stats.
2. **Guest → account conversion.** This flow should meaningfully increase
   how many guest users create an account, not just tolerate guests
   passing through.
3. **Free → Pro (paywall) conversion.** The `paywall place holder` screen
   is a real conversion moment in this flow, not incidental — treat its
   placement/trigger as a deliberate design decision.
4. **Drip-feed education engagement.** The gated multi-session education
   sequence (see `Storyline.md`) should be designed to actually get seen/
   completed, not just be technically possible to gate.

Numeric targets (conversion %, retention lift, etc.) are intentionally
TBD for now — qualitative goals are locked so drafting can proceed;
revisit with real targets once the spec is further along.

Every screen book and every `Storyline.md` step should be checkable
against this list once done — if a goal has no book/chapter/gate serving
it, that's a gap to flag, not something to quietly drop.

## Resolved from this session

- `Post Rating` **is** the "post-routine talk" screen — the animated
  character's check-in copy belongs in that book, not a separate screen.
- The drip-feed step in the flow above is the `Rate us` screen (#21 in
  `Screen-Inventory.md`). Its exact cadence/trigger is deferred to
  `Storyline.md` drafting time, not needed before individual screen books
  start.

## Open items from this session

- Home screen (with summary cards) isn't among the uploaded wireframes —
  needs its own mockup/book since Goal 1 depends on it.
