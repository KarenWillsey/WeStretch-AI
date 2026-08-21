# State variables

Master list of variables any screen's chapter condition or `Storyline.md`
gate is allowed to reference. Check here before inventing a new condition
variable in a screen book — add it here first so naming stays consistent
across the whole spec. Built incrementally as Karen dictates — not
finalized.

| Variable | Type | Meaning | Notes |
|---|---|---|---|
| `routines_completed` | integer | count of stretching routines the user has finished | drives "0 routines done" / "1 routine done" chapters |
| `account_type` | enum: `guest`, `free`, `pro` | which of WeStretch's three user tiers | confirm exact tier names/values with Karen |
| `routine_path` | enum: `full_body`, `customize` | which top-level choice the user made on First Screen | |
| `routine_id` | identifier ("sport ID number") | which specific routine the user was given/chose | live app already identifies completed routines by this ID; confirm exact field name/format with engineering rather than inventing a new one |
| `standing_poses_selected` | set, up to 8 | which of the 8 standing poses (Standing, Arms Up, T-Pose, Straddle T, Arms Behind, Toe Touch, Lunge (R), Lunge (L)) are toggled on | from `standing` / `Base Positions` screens |
| `floor_poses_selected` | set, up to 8 | which of the 8 floor poses (Plank, Cat, Knee Sit, Diamond Sit, Splits, L Sit, Cobra, Lay Down) are toggled on | from `floor` / `Base Positions` screens |
| `body_filter` | 12 booleans | on/off per body part (Upper: Neck, Shoulder, Elbows, Wrist, Spine, Hip; Lower: Knee, Ankle + others per the L/R diagram) | from `Body Filter` screen; confirm the full 12-part list with Karen — image shows some parts excluded (X'd out) by default |
| `routine_length_minutes` | integer, 3–60 | length of routine, either a preset (5/10 min) or custom | from `time` / `Minutes` / `Routine Length` fields |
| `stiffness_rating` | integer 0–10 | "how stiff are you" | asked pre-routine (`Rating`) and post-routine (`Post Rating`) |
| `feeling_rating` | integer 0–10 | "how are you feeling today" | asked pre-routine (`Rating`) and post-routine (`Post Rating`, also captures a pain 0-10 and a pace/speed 0-10 slider — confirm if these are 3 separate variables: `pain_rating`, `stiffness_rating`, `pace_rating`) |
| `badges_earned` | set | which badges unlocked this session | drives `Badges` screen |
| `streak_count` | integer | consecutive days/sessions streak | drives `Streak Progress` screen |
| `coins_earned_today` | integer | coins collected this session | drives `Collect coins` screen |
| `daily_goal_reached` | boolean | whether the user hit the goal they set | gates whether `Goal Reached` screen shows at all |

## Added 2026-08-20 (from full flow dictation)

| Variable | Type | Meaning | Notes |
|---|---|---|---|
| `speed_adjustment` | percentage | how much slower Ada paces the routine after "Too fast" is tapped on `Do routine` | Karen said "25% slower" per tap — confirm if this stacks on repeat taps or caps at one adjustment |
| `routine_finish_status` | enum: `completed`, `abandoned` | whether the routine counts as finished | a routine reaching **≥75%** counts as finished even if not 100% — this threshold gates `routines_completed` increments |
| `pause_state` | enum: `playing`, `paused` | drives whether `Do routine`'s pause button shows pause or play/continue icon | |
| `pose_index` / `pose_total` | integers | "X out of Y" poses done, shown top-left on `Do routine` with a circular countdown ring | |
| `pose_countdown_seconds` | integer | per-pose countdown shown top-right on `Do routine` | |
| `drip_progress` | set of completed sheet IDs | which `Storyline.md` drip sheets the user has fully completed | must persist across sessions — if the user quits (hits X) mid-drip, resume from the correct next sheet, don't restart or skip |
| `first_name` | string | user's first name, once known | used in free-user "Welcome back, [Name]" copy on `First Screen` |
| `last_routine_settings` | object | the user's most recent routine configuration | powers the "Last routine settings" button (free users only) that skips straight to `Rating` |
| `trial_days_remaining` | integer | guest gets 7 days of Pro-level access unlocked at signup; signing up (guest→free) grants 7 *more* days on top of whatever's left | **conflicts with `trial_routines_remaining` below — see Global-Goals.md open items, needs Karen's reconciliation** |
| `trial_routines_remaining` | integer | free-user framing of the same trial concept, counted in routines instead of days (Karen used "11 routines," "14 routines," and "14 days" at different points) | **same conflict as above** |
| `library_tier` | enum: `guest_curated` (50 stretches), `free_full` (6700+ stretches) | which stretch library the user can draw from | guest library is device-local only, doesn't transfer on device change; free is account-synced |
| `device_bound` | boolean | true for guest users — history/settings don't transfer to a new phone or another device | core reason the drip funnel pushes sign-up |
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
| `referral_state` | object | gifting: gifter gives a friend 30 days Pro, gifter receives 30 more days once the friend completes 2 routines | separate from the day-5 one-time-offer share mechanic, which gives coins to the sharer and 60 days for $2 to the friend — confirm these are two distinct sharing mechanics, not the same one described twice |

## Open items
- Confirm exact list/count for `body_filter` (image shows 12 total: 6
  upper + 6 lower, but only some are checked on by default — need the full
  canonical list of 12 part names).
- Confirm whether "pain," "stiffness," and "pace/speed" on the `Post
  Rating` screen are three separate tracked variables or one combined
  metric.
- Confirm exact meaning/mechanism of `routine_id` ("sport ID number") —
  does this map to a fixed catalog of named routines, or is it generated
  per custom build?
- **`trial_days_remaining` vs. `trial_routines_remaining` vs. day-8/day-14
  paywall milestones**: Karen's dictation used day counts, routine counts,
  and calendar-day paywall triggers somewhat interchangeably and flagged
  it herself as unresolved. This needs one canonical trial/paywall model
  before `Storyline.md`'s paywall steps can be finalized — see
  `Global-Goals.md` open items.
- Confirm whether the day-5 "60 days for $2" one-time offer and the
  routine-type-2 "share to friend, 60 days for $2" offer are the same
  promotion referenced twice, or two separate offers.
