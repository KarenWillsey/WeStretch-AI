# Storyline: post-workout drip-feed education sequence

Tracks gating/sequencing logic that spans multiple screens and multiple
sessions, kept separate from individual `Screens/*.md` books per the
format decision in `Memory.md`. Captured wholesale from Karen's 2026-08-20
dictation; she explicitly flagged the ordering below as unresolved and
asked for help organizing it; **this file is a first-pass catalog, not a
locked sequence.** Nothing here should be treated as final until she
confirms.

Applies [[Brand-Voice-Principles]] to every sheet's copy.

---

## Fixed sequence, every user, first routine completion

These happen in this order right after `Post Rating` → `Badges` (if any)
→ `Streak Progress` → `Collect coins`, before the user reaches the real
leaderboard. **Confirm with Karen: do S1/S2 repeat every session, or only
the first time?** (Dictation implies first-time-only, but wasn't stated
outright.)

### S1: Routine recap + login prompt
Screen/sheet, not yet in `Screen-Inventory.md` as its own book; add as
`Routine Recap` if confirmed.
- Title: "Your routine was {routine_length_minutes} minutes long, {routine_path == 'full_body' ? 'full body' : the chosen customize style}."
- Subtitle: "Keep up your mobility."
- Body: explains the app builds the next routine off the user's history,
  so routines evolve with them; to save history and use the account
  across multiple devices, and to protect against losing everything on a
  new phone, recommends logging in.
- Button 1: "Sure, I'll log in" → existing login/signup flow ({Screen: Sign Up}) → on success, `account_type` becomes `free` → continue to S2
- Button 2: "Continue as guest" → continue to S2 (guest path, `account_type` stays `guest`)

### S2: Leaderboard explainer
Screen/sheet, not yet in `Screen-Inventory.md`; add as `Leaderboard Explainer`.
- Title: "Leaderboards are to help you motivate and show up every day."
- Body: "It's based on how many minutes you stretch in a day. Set a little
  personal goal to move up, or stay in the top league."
- Button: "Take me to the leaderboard" → {Screen: Leaderboard (real)}

Then: user explores the leaderboard → **(Goal 1 gap)** → should route to
{Screen: Home}, which shows a guest banner ("You are a guest user. Sign up
anytime to save your history" → tap → Sign Up) and bottom nav (at least
Leaderboard, Notifications, Settings). This is where the drip funnel ends
for that day.

---

## Trial & paywall structure, confirmed 2026-08-20

- Measured in **completed routines, not calendar days** (earlier "day 8"/
  "day 14" language was actually the 8th/14th completed routine).
- Guest: pool of 7 Pro-level completed routines (`trial_routines_remaining`).
- Guest → Free (signs up): +7 more added *on top of* whatever's currently
  left in the pool (not reset to a flat number).
- Typical path (signs up before using any guest routines) yields a
  14-routine total budget; this is why "11 routines left" at
  `routines_completed==3` and "10 routines left" at `routines_completed==4`
  both check out (14 − 3 = 11, 14 − 4 = 10).
- Fixed messaging checkpoints, keyed to total `routines_completed`: a
  **soft paywall/upsell after the 8th completed routine**, a **hard
  paywall after the 14th** ("that was your last fully unlocked routine",
  offers coins-for-Pro-for-a-day or the yearly-billed-monthly option, with
  reduced coins/streak-savers as a softer consolation tier).
- **Resolved 2026-08-21**: a guest who passes their 7-routine pool without
  signing up gets the same gating as a free user past budget, access to
  the single "Full Body" routine style only, no customization; locked
  features are visible but blurred, and tapping any of them → {Screen:
  paywall place holder}. Same behavior as `Routine Type 2`'s
  `account_type == 'free'` chapter, applies to guests past-budget too.
- Free users should keep getting recurring Pro-upsell prompts on a regular
  cadence too, not just at the two checkpoints above (persistent "Turn
  Pro" banner on Home, the Routine Type 2 lock banner, etc.)

---

## Topical drip sheets, tentative grouping, sequence TBD

Karen dictated ~25 distinct education topics without a fixed order and
asked for help breaking them out. Grouped below by the rough timing signal
she gave (or "unspecified" where none was given); **treat the grouping,
not the exact order within a group, as the useful part; confirm real
sequence with Karen.**

### Very early (routines 2–3)
- **Coins explainer**: "opening the app every day is the hardest part";
  finishing a routine earns coins; coins can buy a streak saver.

### Early (within first ~14 days of Pro / early routines, exact routine # TBD)
- **Streak explainer**: what a streak is; positioned as optional
  motivation, not guilt: "if that's not what you're here for, keep going."
  Strategy: don't surface any missed-day messaging until the user has a
  5-day streak.
- **Notification reminders setup**: Karen said this should occur earlier
  than the 10th-routine mark (see below), exact routine # TBD. Lists
  channels: push, email, vibrate-only alarm. Introduces "anchoring" a
  stretch to an existing habit (e.g. right after brewing coffee, right
  after brushing teeth) and referencing that anchor in the push copy.
  Opting in via checkbox triggers the native OS notification-permission
  prompt.
- **Body Filter / Position Filter explainer**: what the body filter and
  position filter customizations do.
- **Closed captioning / font size**: Settings.
- **Sound options** (instructions + ding / no ding / silent) Settings.
- **Profile setup** ("Let's adjust your profile") leaderboard avatar
  reflects personality, enables further stretch customization.
- **Meet Ada**: formal introduction of the instructor character; mentions
  a second instructor, Bruce, selectable in Settings.
- **Gym setting** (choose plain white background vs. Ada's gym setting) 
  Settings.
- **Sport type explainer**: Warm Up (activation: reach full range and
  back out) vs. Cool Down (longer hold, reduces post-sport lactic
  acid/stiffness) vs. Sport Improvement & Splits (progressively increases
  hold up to 30s, repeated multiple times, most aggressive flexibility
  gain).
- **Pre-Routine-Type-2 transition explainer**: shown the session *before*
  the user is switched to the consolidated `Routine Type 2` screen (i.e.
  before routine 7). Explains where the summary/filters now live, possibly
  as a quick animated toggle-through.

### Mid (~routine 8–10)
- **Stiffness progress stats**: roughly every 8 routines, compares
  `stiffness_before`/`stiffness_after` across sessions to show improvement.
  Karen flagged mood tracking as a possible future addition here, not live
  yet.
- **Increase routine time nudge**: around the 10th routine, encourages
  bumping up `default_routine_length`.
- **Ada speed control**: teaches the user they can slow down/speed up
  Ada; setting saved in the menu. Also mentions stretch history is
  viewable by tapping the Home screen's top widget → opens a calendar.
- **Badges explainer**: how to find badges, encourages browsing for a
  challenge to earn one.

### Later / pre-paywall
- **Family Share**: explains family-share Pro subscription; Settings has
  a pregnancy-routines grouping for expecting family members. Positioned
  "maybe before the paywall."
- **Sharing**: share WeStretch with a friend via Settings; gifts the
  friend 30 days of Pro; gifter receives 30 more days once the friend
  completes 2 routines.
- **Alberta tour**: Settings toggle, shows content about Alberta (the
  province WeStretch was made in) for variety.
- **Feedback ask**: invites suggestions/comments/feedback, especially
  positive ones; email contact via Settings.
- **Time-off reassurance**: if a user takes a few weeks off, the app
  rolls back some old times/intensity to keep routines safe and prevent
  injury on return.

### Recurring / conditional (not part of the linear sequence)
- **Streak Saver Offer**: triggered specifically when a user with a
  5-day streak misses a day and returns (Karen's example: misses day 6,
  returns day 7); "do you want to use your streak freeze?"
- **Guest sign-up nudge**: shown every 3 days for guest users. Framed
  around what they're missing: guest library is a curated 50 stretches,
  device-only (doesn't transfer to a new phone/device); free unlocks the
  full 6700+ stretch library, synced to the account.
- **Random reactivation gift**: for users whose Pro trial/subscription
  has lapsed and are back to stretching free: on a genuinely random
  schedule, offer "the next 24 hours" of Pro as a gift.
- **Turn Pro banner**: persistent, not a one-off sheet: sits on the Home
  screen for free users, tapping it → {Screen: paywall place holder}.

### One-time offers / paywall milestones
- **Day-5 (≈routine 5) one-time offer**: "best offer" framing: 60 days of
  Pro for $2, then regular price after; includes bonus coins and bonus
  streak savers. **Confirmed 2026-08-20: same offer as the Routine Type 2
  lock banner's share-to-friend offer**, shown first in its plain
  (non-share) form; the share-with-a-friend variant of this same offer is
  introduced later in the sequence, deliberately not bundled with its
  first appearance. Exact later timing still TBD.
- **Soft paywall, after the 8th completed routine**: first real paywall
  appearance for free users.
- **Hard paywall, after the 14th completed routine**: "that was your last
  fully unlocked routine"; offers coins-for-Pro-for-a-day, or a
  yearly-billed-monthly subscription option; gives reduced coins/streak-
  savers as a softer consolation tier.

---

## Proposed sequence (Claude's draft, 2026-08-21, pending Karen's confirmation)

Karen asked for help organizing the ~25 topical sheets. This slots each
one against `routines_completed`, anchored to the timing signals she gave
explicitly, with everything else placed to keep pace roughly even and to
front-load sheets that serve a Global Goal. **Nothing below is locked,
it's a starting point to react to, not a decision.**

| Routine # | Sheet | Anchor | Serves goal |
|---|---|---|---|
| 1 | *(fixed: Routine Recap → Leaderboard Explainer → Leaderboard → Home)* | dictated, fixed | Goal 2 |
| 2 | Coins explainer | Karen: "routine 2 or 3" | Goal 4 |
| 3 | Streak explainer | Karen: "early" | Goal 4 |
| 4 | Body Filter / Position Filter explainer | Karen: "early on, within 14 days of Pro" | Goal 4 |
| 5 | Day-5 one-time offer (60 days for $2 + bonuses, plain, no share) | Karen: explicit "day 5" | Goal 3 |
| 6 | Pre–Routine Type 2 transition explainer | Karen: "the session before" routine 7 | Goal 4 |
| 7 | *(structural: routes into Routine Type 2, no drip sheet)* | dictated, fixed |, |
| 8 | Soft paywall | Karen: explicit | Goal 3 |
| 9 | Notification reminders | Karen: "earlier than the 10th" | Goal 4 |
| 10 | Increase routine time nudge | Karen: explicit "~10th routine" | Goal 4 |
| 11 | Ada speed control | unanchored, placed here | Goal 4 |
| 12 | Badges explainer | unanchored, placed here | Goal 4 |
| 13 | Family Share | Karen: "maybe before the paywall" (i.e. before 14) | Goal 3 |
| 14 | Hard paywall | Karen: explicit | Goal 3 |

**Unanchored, no timing signal given**: proposed as a flexible pool, one
per session from routine 15 onward (post-decision period), order not
meaningful: Closed captioning/font size, Sound options, Profile setup,
Meet Ada (+ Bruce), Gym setting, Sport type explainer, Sharing (30-day
gift), Alberta tour, Feedback ask, Time-off reassurance, share-variant of
the day-5 offer (per Karen: introduced later, not bundled with routine 5).

**Recurring/conditional, not slotted into the table** (unchanged from the
earlier grouping): Stiffness progress stats (~every 8 routines, first
one lands on routine 8, same session as the soft paywall; flag as a
possible crowding issue), Streak Saver Offer (conditional trigger),
Guest sign-up nudge (every 3 days, calendar-based), Random reactivation
gift (random schedule), Turn Pro banner (persistent UI, not a sheet).

**Judgment calls made without explicit direction from Karen** (flag before
treating as final): sheets 11–12 (Ada speed control, Badges explainer)
placed by even pacing, not a stated reason; the 10 unanchored sheets
pushed to routine 15+ rather than interspersed earlier, on the assumption
that priority sheets (goal-serving, explicitly anchored) should come
first; Karen may want some of these earlier for other reasons (e.g.
Profile setup or Meet Ada feel like early-app-orientation content, not
routine-15 content).

## Template for one step (once sequence is confirmed)

```
## Step [N]: [short name]
Unlocks when: [prerequisite, e.g. "routine_count >= 2 AND all screens in Step 1 were completed"]
Screens shown, in order: [Screen A] → [Screen B] → [Screen C]
Serves Global Goal: [1/2/3/4 from Global-Goals.md, or "none; flag as gap"]
```

## Open items
- ~~Full sequence/timing for the ~25 topical sheets~~, **draft proposed
  2026-08-21**, see "Proposed sequence" above. Still needs Karen's
  confirmation, especially the judgment calls flagged in that section.
- Trial/paywall day-vs-routine-count conflict (see "Trial & paywall
  structure" above) blocks finalizing the one-time-offer and paywall
  milestone steps.
- `drip_progress` (State-Variables.md) needs to track completion at the
  granularity of these individual sheets so a user who quits mid-drip
  resumes correctly, exact resume behavior not yet specified.
