# Storyline: post-workout drip-feed education sequence

Tracks gating/sequencing logic that spans multiple screens and multiple
sessions — kept separate from individual `Screens/*.md` books per the
format decision in `Memory.md`. Captured wholesale from Karen's 2026-08-20
dictation; she explicitly flagged the ordering below as unresolved and
asked for help organizing it — **this file is a first-pass catalog, not a
locked sequence.** Nothing here should be treated as final until she
confirms.

Applies [[Brand-Voice-Principles]] to every sheet's copy.

---

## Fixed sequence — every user, first routine completion

These happen in this order right after `Post Rating` → `Badges` (if any)
→ `Streak Progress` → `Collect coins`, before the user reaches the real
leaderboard. **Confirm with Karen: do S1/S2 repeat every session, or only
the first time?** (Dictation implies first-time-only, but wasn't stated
outright.)

### S1: Routine recap + login prompt
Screen/sheet, not yet in `Screen-Inventory.md` as its own book — add as
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
Screen/sheet, not yet in `Screen-Inventory.md` — add as `Leaderboard Explainer`.
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

## Trial & paywall structure (needs reconciliation — see open items)

- Guest: 7 days of Pro-level access unlocked from the start.
- Guest → Free (signs up): +7 *more* days on top of whatever's left.
- Free tier messaging also references **11 fully-unlocked routines as a
  gift** (stated at routines_completed==3) and **14 routines/14 days**
  (stated as a rough duration for the countdown pattern) and a first real
  **paywall around day 8**, with a harder paywall on **day 14** ("that was
  your last fully unlocked routine").
- **These day-based and routine-based framings don't obviously reconcile
  into one model — flagged in State-Variables.md and Global-Goals.md as an
  open item for Karen to resolve before this section can be finalized.**
- Free users should keep getting recurring Pro-upsell prompts on a regular
  cadence, not just at the milestones above (persistent "Turn Pro" banner
  on Home, the Routine Type 2 lock banner, etc.)

---

## Topical drip sheets — tentative grouping, sequence TBD

Karen dictated ~25 distinct education topics without a fixed order and
asked for help breaking them out. Grouped below by the rough timing signal
she gave (or "unspecified" where none was given) — **treat the grouping,
not the exact order within a group, as the useful part; confirm real
sequence with Karen.**

### Very early (routines 2–3)
- **Coins explainer** — "opening the app every day is the hardest part";
  finishing a routine earns coins; coins can buy a streak saver.

### Early (within first ~14 days of Pro / early routines, exact routine # TBD)
- **Streak explainer** — what a streak is; positioned as optional
  motivation, not guilt: "if that's not what you're here for, keep going."
  Strategy: don't surface any missed-day messaging until the user has a
  5-day streak.
- **Notification reminders setup** — Karen said this should occur earlier
  than the 10th-routine mark (see below), exact routine # TBD. Lists
  channels: push, email, vibrate-only alarm. Introduces "anchoring" a
  stretch to an existing habit (e.g. right after brewing coffee, right
  after brushing teeth) and referencing that anchor in the push copy.
  Opting in via checkbox triggers the native OS notification-permission
  prompt.
- **Body Filter / Position Filter explainer** — what the body filter and
  position filter customizations do.
- **Closed captioning / font size** — Settings.
- **Sound options** — instructions + ding / no ding / silent — Settings.
- **Profile setup** — "Let's adjust your profile" — leaderboard avatar
  reflects personality, enables further stretch customization.
- **Meet Ada** — formal introduction of the instructor character; mentions
  a second instructor, Bruce, selectable in Settings.
- **Gym setting** — choose plain white background vs. Ada's gym setting —
  Settings.
- **Sport type explainer** — Warm Up (activation: reach full range and
  back out) vs. Cool Down (longer hold, reduces post-sport lactic
  acid/stiffness) vs. Sport Improvement & Splits (progressively increases
  hold up to 30s, repeated multiple times — most aggressive flexibility
  gain).
- **Pre-Routine-Type-2 transition explainer** — shown the session *before*
  the user is switched to the consolidated `Routine Type 2` screen (i.e.
  before routine 7). Explains where the summary/filters now live, possibly
  as a quick animated toggle-through.

### Mid (~routine 8–10)
- **Stiffness progress stats** — roughly every 8 routines, compares
  `stiffness_before`/`stiffness_after` across sessions to show improvement.
  Karen flagged mood tracking as a possible future addition here, not live
  yet.
- **Increase routine time nudge** — around the 10th routine, encourages
  bumping up `default_routine_length`.
- **Ada speed control** — teaches the user they can slow down/speed up
  Ada; setting saved in the menu. Also mentions stretch history is
  viewable by tapping the Home screen's top widget → opens a calendar.
- **Badges explainer** — how to find badges, encourages browsing for a
  challenge to earn one.

### Later / pre-paywall
- **Family Share** — explains family-share Pro subscription; Settings has
  a pregnancy-routines grouping for expecting family members. Positioned
  "maybe before the paywall."
- **Sharing** — share WeStretch with a friend via Settings; gifts the
  friend 30 days of Pro; gifter receives 30 more days once the friend
  completes 2 routines.
- **Alberta tour** — Settings toggle, shows content about Alberta (the
  province WeStretch was made in) for variety.
- **Feedback ask** — invites suggestions/comments/feedback, especially
  positive ones; email contact via Settings.
- **Time-off reassurance** — if a user takes a few weeks off, the app
  rolls back some old times/intensity to keep routines safe and prevent
  injury on return.

### Recurring / conditional (not part of the linear sequence)
- **Streak Saver Offer** — triggered specifically when a user with a
  5-day streak misses a day and returns (Karen's example: misses day 6,
  returns day 7) — "do you want to use your streak freeze?"
- **Guest sign-up nudge** — shown every 3 days for guest users. Framed
  around what they're missing: guest library is a curated 50 stretches,
  device-only (doesn't transfer to a new phone/device); free unlocks the
  full 6700+ stretch library, synced to the account.
- **Random reactivation gift** — for users whose Pro trial/subscription
  has lapsed and are back to stretching free: on a genuinely random
  schedule, offer "the next 24 hours" of Pro as a gift.
- **Turn Pro banner** — persistent, not a one-off sheet: sits on the Home
  screen for free users, tapping it → {Screen: paywall place holder}.

### One-time offers / paywall milestones
- **Day-5 one-time offer** — "best offer" framing: 60 days of Pro for $2,
  then regular price after; includes bonus coins and bonus streak savers.
  **Confirm vs. the Routine Type 2 share-to-friend offer — same promotion
  or a second one?** (see State-Variables.md open items)
- **Paywall, ~day 8** — first real paywall appearance for free users.
- **Paywall, day 14** — "that was your last fully unlocked routine";
  offers coins-for-Pro-for-a-day, or a yearly-billed-monthly subscription
  option; gives reduced coins/streak-savers as a softer consolation tier.

---

## Template for one step (once sequence is confirmed)

```
## Step [N]: [short name]
Unlocks when: [prerequisite, e.g. "routine_count >= 2 AND all screens in Step 1 were completed"]
Screens shown, in order: [Screen A] → [Screen B] → [Screen C]
Serves Global Goal: [1/2/3/4 from Global-Goals.md, or "none — flag as gap"]
```

## Open items
- Full sequence/timing for the ~25 topical sheets above is unresolved —
  Karen asked for help organizing these; needs a follow-up working session
  once the goal-per-sheet mapping (see Global-Goals.md) is done, so
  sequencing decisions can be justified against the 4 confirmed goals
  rather than picked arbitrarily.
- Trial/paywall day-vs-routine-count conflict (see "Trial & paywall
  structure" above) blocks finalizing the one-time-offer and paywall
  milestone steps.
- `drip_progress` (State-Variables.md) needs to track completion at the
  granularity of these individual sheets so a user who quits mid-drip
  resumes correctly — exact resume behavior not yet specified.
