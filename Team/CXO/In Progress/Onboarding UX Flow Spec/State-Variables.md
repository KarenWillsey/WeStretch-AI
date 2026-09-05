# State variables

Master list of variables any screen's chapter condition or `Storyline.md`
gate is allowed to reference. Check here before inventing a new condition
variable in a screen book; add it here first so naming stays consistent
across the whole spec. Built incrementally as Karen dictates, not
finalized.

| Variable | Type | Meaning | Notes |
|---|---|---|---|
| `routines_completed` | integer | count of stretching routines the user has finished | drives "0 routines done" / "1 routine done" chapters |
| `account_type` | enum: `guest`, `free`, `pro` | which of WeStretch's three user tiers | confirm exact tier names/values with Karen |
| `routine_path` | enum: `full_body`, `customize` | which top-level choice the user made on First Screen | |
| `sport_id` | identifier | which specific routine the user was given/chose | **Renamed from `routine_id` to `sport_id` 2026-08-21 per Karen.** Live app already identifies completed routines by this ID; mechanism still unconfirmed; see Open items. |
| `standing_poses_selected` | set, up to 8 | which of the 8 standing poses (Standing, Arms Up, T-Pose, Straddle T, Arms Behind, Toe Touch, Lunge (R), Lunge (L)) are toggled on | from `standing` / `Base Positions` screens |
| `floor_poses_selected` | set, up to 8 | which of the 8 floor poses (Plank, Cat, Knee Sit, Diamond Sit, Splits, L Sit, Cobra, Lay Down) are toggled on | from `floor` / `Base Positions` screens |
| `body_filter` | 12 booleans | on/off per body part | from `Body Filter` screen. **2026-08-21**: Karen's team owns the exact 12-part list/defaults, not tracked as an open question in this file anymore. |
| `routine_length_minutes` | integer, 3–60 | length of routine, either a preset (5/10 min) or custom | from `time` / `Minutes` / `Routine Length` fields |
| `stiffness_rating` | integer 0–10 | "how stiff are you" | asked pre-routine (`Rating`) and post-routine (`Post Rating`) |
| `feeling_rating` | integer 0–10 | "how are you feeling today" | asked pre-routine (`Rating`) and post-routine (`Post Rating`) |
| `pain_rating` | integer 0–10 | pain level | **Confirmed 2026-08-21**: separate from `stiffness_rating` and `speed_rating`, not a combined metric, asked on `Post Rating` |
| `speed_rating` | integer 0–10 | pace/speed feedback | **Confirmed 2026-08-21**: Karen's term is "speed," not "pace" (drop "pace" everywhere. Separate variable, not combined with pain/stiffness) asked on `Post Rating` |
| `badges_earned` | set | which badges unlocked this session | drives `Badges` screen |
| `streak_count` | integer | consecutive days/sessions streak | drives `Streak Progress` screen |
| `coins_earned_today` | integer | coins collected this session | drives `Collect coins` screen |
| `daily_goal_reached` | boolean | whether the user hit the goal they set | gates whether `Goal Reached` screen shows at all |

## Added 2026-08-20 (from full flow dictation)

| Variable | Type | Meaning | Notes |
|---|---|---|---|
| `speed_adjustment` | percentage | how much slower Ada paces the routine after "Too fast" is tapped on `Do routine` | Karen said "25% slower" per tap; confirm if this stacks on repeat taps or caps at one adjustment |
| `routine_finish_status` | enum: `completed`, `abandoned` | whether the routine counts as finished | a routine reaching **≥75%** counts as finished even if not 100%; this threshold gates `routines_completed` increments |
| `pause_state` | enum: `playing`, `paused` | drives whether `Do routine`'s pause button shows pause or play/continue icon | |
| `pose_index` / `pose_total` | integers | "X out of Y" poses done, shown top-left on `Do routine` with a circular countdown ring | |
| `pose_countdown_seconds` | integer | per-pose countdown shown top-right on `Do routine` | |
| `drip_progress` | set of completed sheet IDs | which `Storyline.md` drip sheets the user has fully completed | must persist across sessions; if the user quits (hits X) mid-drip, resume from the correct next sheet, don't restart or skip |
| `first_name` | string | user's first name, once known | used in free-user "Welcome back, [Name]" copy on `First Screen` |
| `last_routine_settings` | object | the user's most recent routine configuration | powers the "Last routine settings" button (free users only) that skips straight to `Rating` |
| `trial_routines_remaining` | integer | pool of Pro-level completed routines remaining. **Confirmed 2026-08-20**: measured in *completed routines*, not calendar days, earlier "day 8"/"day 14" language actually meant the 8th/14th completed routine. Guest starts at 7; signing up (guest→free) adds +7 *on top of* whatever's currently left (not reset to a flat total) | typical path (signs up before using any guest routines) yields a 14-routine total budget, which is why "11 routines left" at `routines_completed==3` and "10 routines left" at `routines_completed==4` both check out (14 − 3 = 11, 14 − 4 = 10) |
| `trial_paywall_checkpoint` | enum: `soft` (after routine 8), `hard` (after routine 14) | fixed messaging checkpoints keyed to total `routines_completed`, independent of the exact remaining-pool math | `soft` = first paywall/upsell appearance; `hard` = "that was your last fully unlocked routine." **Resolved 2026-08-21**: a guest who passes the 7-routine pool without signing up gets the same gating as a budget-exhausted free user; Full Body only, other routine types visible but blurred, tap → paywall. |
| `library_tier` | enum: `guest_curated` (50 stretches), `free_full` (6700+ stretches) | which stretch library the user can draw from | guest library is device-local only, doesn't transfer on device change; free is account-synced |
| `device_bound` | boolean | true for guest users; history/settings don't transfer to a new phone or another device | core reason the drip funnel pushes sign-up |
| `notification_prefs` | object: channel (`push`/`email`/`vibrate_only`), optional `anchor_text` | how/when the user wants stretch reminders; "anchor" ties the reminder to an existing habit (e.g. "after brewing coffee") | opting in triggers the native OS notification-permission prompt |
| `instructor_selected` | enum: `ada`, `bruce` | which animated instructor character is active | adjustable in Settings |
| `background_selected` | enum: `plain_white`, `gym` | Ada's/the instructor's background scene | adjustable in Settings |
| `captioning_font_size` | enum/scale | closed-captioning text size | Settings |
| `sound_mode` | enum: `instructions_and_ding`, `no_ding`, `silent` | audio cue preference | Settings |
| `profile_customization` | object | user's leaderboard avatar/personality customization | |
| `family_share_active` | boolean | whether the account is part of a family-share Pro subscription | family members can have their own routine groupings, e.g. pregnancy routines |
| `daily_goal_type` | enum: `everyday_stretcher`, `weekday_stretcher` | set on the goal-setting screen; `everyday_stretcher` is the one tied to streaks | |
| `default_routine_length` | integer (minutes) | user's set default, editable periodically ("every few weeks, add a minute or two") | set on the goal-setting screen |
| `stiffness_before` / `stiffness_after` | integer 0–10 each | stiffness rating at routine start (`Rating`) vs. end (`Post Rating`) | compared roughly every 8 routines in a progress-over-time drip sheet; mood tracking flagged as a possible future variable, not live yet |
| `referral_state` | object | gifting: gifter gives a friend 30 days Pro, gifter receives 30 more days once the friend completes 2 routines | separate from the day-5 one-time-offer share mechanic, which gives coins to the sharer and 60 days for $2 to the friend; confirm these are two distinct sharing mechanics, not the same one described twice |

## Open items
- Confirm exact mechanism of `sport_id` (renamed from `routine_id`
  2026-08-21); does this map to a fixed catalog of named routines, or is
  it generated per custom build? Still needs engineering confirmation.
- ~~Confirm exact list/count for `body_filter`~~, **dropped 2026-08-21
  per Karen**: her team owns this detail; no longer tracked as an open
  question here.
- ~~Confirm whether "pain," "stiffness," and "pace/speed" on the `Post
  Rating` screen are three separate tracked variables or one combined
  metric~~; **Resolved 2026-08-21**: three separate variables
  (`pain_rating`, `stiffness_rating`, `speed_rating`); "pace" dropped in
  favor of "speed."
- ~~`trial_days_remaining` vs. `trial_routines_remaining` vs. day-8/day-14
  paywall milestones~~; **Resolved 2026-08-20**: single routine-count
  based model, see `trial_routines_remaining` / `trial_paywall_checkpoint`
  above.
- ~~Confirm whether the day-5 "60 days for $2" one-time offer and the
  routine-type-2 "share to friend, 60 days for $2" offer are the same
  promotion~~; **Resolved 2026-08-20**: same offer (60 days for $2 +
  bonus coins + bonus streak tokens). Karen added a nuance: the
  *share-with-a-friend* version of this offer should be introduced later
  in the drip sequence, not bundled with the offer's first appearance,
  see `Storyline.md`.
