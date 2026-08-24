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
| 13 | Routine Type 2 | 151851 | ☐ | full customize-routine summary sheet (length, type, body filter, base positions) — button relabeled "Let's Go" pre-routine-7 / "Let's stretch" once it becomes the standard entry point at routine 7+. Free users: only Full Body routine type is tappable, other type cards shown blurred/greyed and route to paywall if tapped; add an info banner "Fully unlock every customization" |
| 14 | Rating | 151851 | ☐ | pre-routine "while your routine is being built" check-in |
| 15 | Do routine | 151851 | ☐ | placeholder — the actual routine-playback screen |
| 16 | Post Rating | 151851 | ☐ | "Congratulations! Let's check in on how you feel" — pain/stiffness/speed sliders |
| 17 | Badges | 151851 | ☐ | placeholder |
| 18 | Streak Progress | 151851 | ☐ | placeholder |
| 19 | Collect coins | 151900 | ☐ | placeholder |
| 20 | Goal Reached | 151900 | ☐ | placeholder, conditional on `daily_goal_reached` |
| 21 | Rate us | 151900 | ☐ | placeholder |
| 22 | Leader board | 151900 | — | **Not the real leaderboard.** Karen confirmed 2026-08-20 she did not upload the actual live leaderboard and doesn't know what this placeholder was meant to represent — purpose unclear even to her. Do not treat as a design target; the flow's actual leaderboard destination is row #28. Candidate to drop from this spec entirely — confirm with Karen. |
| 23 | paywall place holder | 151900 | ☐ | placeholder — now has real copy detail, see Storyline.md paywall steps |
| 24 | Home | *(not uploaded)* | ☑ partial | Drafted 2026-08-21 (`Screens/Home.md`) with everything Karen specified (guest banner, history calendar widget, Turn Pro banner, partial bottom nav); summary-card content and full nav list still unspecified — needs a real design pass. **Needed for Goal 1.** |
| 25 | Set Your Goal | *(not uploaded)* | ☑ partial | Drafted 2026-08-21 (`Screens/Set Your Goal.md`) — first-visit copy, routine-length field, Everyday/Weekday toggle. Save target and Weekday-Stretcher behavior still unspecified. |
| 26 | Streak Saver Offer | *(not uploaded)* | ☑ stub | Drafted 2026-08-21 (`Screens/Streak Saver Offer.md`) — trigger condition only, no real copy yet. |
| 27 | Sign Up | *(existing app screen)* | — | not part of this spec — Karen confirmed this is the existing login/signup structure already live in the app; every book's "Login"/"Sign up" button target just links out to it |
| 28 | Leaderboard (real) | *(existing app screen, no image)* | — | The actual live leaderboard, already built and shipping. **Confirmed 2026-08-20: out of scope — Karen will not be altering it, no image exists to work from.** `Storyline.md` step S2's "Take me to the leaderboard" button targets this screen as a link-out only, same treatment as `Sign Up` (#27) — nothing about its design is part of this spec. |
| 29 | Routine Recap | *(not uploaded)* | ☑ | Drip step S1 — fully dictated, drafted 2026-08-21 as `Screens/Routine Recap.md`. |
| 30 | Leaderboard Explainer | *(not uploaded)* | ☑ | Drip step S2 — fully dictated, drafted 2026-08-21 as `Screens/Leaderboard Explainer.md`. |

**Drip/education sheets** (~28 distinct topics Karen dictated, most not
wireframed) are cataloged in `Storyline.md` rather than duplicated here as
individual rows, per the project's format decision that the drip layer
owns its own sequence separate from the core screen inventory.

## Status as of 2026-08-21: dictation pass closed

Karen has finished dictating for this project — she is **not** producing
individual chapter/JSON books for the remaining un-drafted rows above
(Second, pain, sport, standing, floor, Base Positions, Body Filter,
Minutes, Badges, Streak Progress, Collect coins, Goal Reached, Rate us).
Their status going forward:

- Rows with a source image (everything above except #24–26) — **mockup
  only, no book.** The uploaded screenshot is the reference; nothing in
  this project should invent chapter text/JSON for them.
- Rows without any source image (**#24 Home, #25 Set Your Goal, #26
  Streak Saver Offer, #29 Routine Recap, #30 Leaderboard Explainer**) have
  no visual mockup, but where Karen had dictated real content it's now
  drafted as its own book (2026-08-21 pass, using her existing credits to
  close gaps rather than wait for more dictation) — see each row's notes
  for exactly what's still missing (mostly: visual design, a couple of
  unspecified nav targets).

11 books are now drafted: `First Screen`, `Time`, `Rating`, `Do Routine`,
`Post Rating`, `Routine Type 2`, `Routine Recap`, `Leaderboard Explainer`,
`Home` (partial), `Set Your Goal` (partial), `Streak Saver Offer` (stub) —
plus `Storyline.md` (now including a proposed drip sequence),
`Global-Goals.md`, `Brand-Voice-Principles.md`, and `State-Variables.md`.

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
