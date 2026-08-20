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
