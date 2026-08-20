# Screen inventory

Master ordered list of every "book" (screen) found in the uploaded
wireframes, in upload/timestamp order (oldest first) as Karen specified.
This is the checklist for `Screens/` — each row becomes one file. Not yet
drafted into books; this is just the confirmed inventory so nothing gets
lost or drafted out of order.

Source images: `Images/Screenshot 2026-08-19 151826.png` (oldest) through
`Images/Screenshot 2026-08-19 151900.png` (newest).

| # | Screen name (as labeled) | Source image | Drafted? | Notes |
|---|---|---|---|---|
| 1 | Westretch | 151826 | ☐ | splash/loading screen, version footer |
| 2 | splash screen | 151826 | ☐ | intro video/demo screen |
| 3 | First Screen | 151826 | ☐ | "Welcome, Lets get you stretching" — Full Body / Customize |
| 4 | Second | 151826 | ☐ | "What can I help you with?" — Reduce Pain & Stiffness / Sports Related / Improve Mobility |
| 5 | pain | 151826 | ☐ | 9-option pain-focus grid, follows "Reduce Pain & Stiffness" |
| 6 | sport | 151826 | ☐ | Warm Up / Cool Down / Sport Improvement / Splits, follows "Sports Related" |
| 7 | standing | 151837 | ☐ | 8 standing poses toggle grid |
| 8 | floor | 151837 | ☐ | 8 floor poses toggle grid |
| 9 | Base Positions | 151837 | ☐ | combined standing+floor summary/edit sheet — name confirmed by Karen |
| 10 | Body Filter | 151837 | ☐ | 12-part body diagram on/off — name confirmed by Karen |
| 11 | time | 151837 | ☐ | "How long would you like your routine to be?" 5 / 10 / Custom Length |
| 12 | Minutes | 151837 | ☐ | "Minutes Per Day" dial, Daily Stretch Goal |
| 13 | Routine Type 2 | 151851 | ☐ | full customize-routine summary sheet (length, type, body filter, base positions) — "Let's Go" |
| 14 | Rating | 151851 | ☐ | pre-routine "while your routine is being built" check-in |
| 15 | Do routine | 151851 | ☐ | placeholder — the actual routine-playback screen |
| 16 | Post Rating | 151851 | ☐ | "Congratulations! Let's check in on how you feel" — pain/stiffness/pace sliders |
| 17 | Badges | 151851 | ☐ | placeholder |
| 18 | Streak Progress | 151851 | ☐ | placeholder |
| 19 | Collect coins | 151900 | ☐ | placeholder |
| 20 | Goal Reached | 151900 | ☐ | placeholder, conditional on `daily_goal_reached` |
| 21 | Rate us | 151900 | ☐ | placeholder |
| 22 | Leader board | 151900 | ☐ | placeholder — flagged as a current dead-end (see Global-Goals.md) |
| 23 | paywall place holder | 151900 | ☐ | placeholder |

## Known gaps vs. Karen's dictated live-app flow

Karen's description of the current live post-routine flow is: post-routine
talk (animated character) → badges → streak progress → collect coins →
goal-reached celebration (conditional) → [drip-feed step] → leaderboard →
explore leaderboard → **(gap: currently often ends here)** → should route
to Home screen via bottom nav.

- Resolved: "post-routine talk" is the same screen as `Post Rating` — the
  animated character's check-in copy is drafted as part of that book, not
  a separate undrawn screen.
- Resolved: `Rate us` (#21) is the drip-feed step referenced above — its
  exact cadence/trigger is deferred to when `Storyline.md` is drafted, not
  needed to start on individual screen books.
- Still open: Home screen itself (with summary cards) is not among the 23
  uploaded screens — needed as a book since fixing the leaderboard
  dead-end is a confirmed Global Goal (see `Global-Goals.md`).
