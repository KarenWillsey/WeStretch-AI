# BOOK: Do routine

Source mockup: `Images/Screenshot 2026-08-19 151851.png` (screen 3, "Do routine", currently placeholder text only)
Applies [[Brand-Voice-Principles]] (Ada advancing the user's difficulty/hold
times over time; this is the screen where that shows up live).

This screen isn't chapter/condition-driven like the others; it's one
continuous interactive screen. Documented as UI elements + behaviors
instead of forcing the chapter format.

## UI elements

- **Top-left**: "X out of Y" pose counter (`pose_index` / `pose_total`),
  wrapped in a circular ring showing % of the routine completed.
- **Top-right**: countdown in seconds for the current pose (`pose_countdown_seconds`).
- **X (exit) button**: quits the routine.
- **Pause button**: toggles `pause_state` between `playing` and `paused`;
  icon swaps to a play/continue icon while paused.
- **"Too fast" button**: sets `speed_adjustment` to 25% slower. **Confirm
  with Karen:** does a second tap stack another 25%, or is it capped at
  one adjustment per routine?
- **"Next" button** (bottom), advances to the next pose immediately.

## Completion behavior

- A routine reaches `routine_finish_status = completed` once the user
  reaches **≥75%** through it, even if they stop before 100%.
- Whether the user completes it, stops it, or pauses and later exits, once
  the routine is finished (per the 75% rule) the app **auto-routes to
  {Screen: Post Rating}**; no explicit "done" button push is required.
- If the user exits (X) before hitting 75%, `routine_finish_status =
  abandoned` and `routines_completed` should NOT increment. **Confirm this
  assumption with Karen**, not explicitly stated, inferred from the 75%
  rule's purpose.

---

```json
{
  "screen": "Do routine",
  "elements": {
    "pose_counter": {"position": "top_left", "shows": "pose_index/pose_total", "style": "circular_progress_ring"},
    "countdown": {"position": "top_right", "shows": "pose_countdown_seconds"},
    "exit_button": {"action": "quit_routine"},
    "pause_button": {"toggles": "pause_state", "values": ["playing", "paused"]},
    "too_fast_button": {"action": "set_speed_adjustment", "value": "-25%"},
    "next_button": {"position": "bottom", "action": "advance_pose"}
  },
  "completion_rule": {"finished_threshold_pct": 75, "on_finished_target": "Post Rating"}
}
```
