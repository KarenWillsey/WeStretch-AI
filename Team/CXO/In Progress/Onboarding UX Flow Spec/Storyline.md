# Storyline: post-workout drip-feed education sequence

Tracks gating logic that spans multiple screens and multiple sessions —
kept separate from individual `Screens/*.md` books per the format decision
in `Memory.md`. Each step names the screen(s) it shows and the condition
that must be true before it's allowed to show.

Not yet populated — draft this after the individual screen books for the
first-routine and second-routine education screens exist, so it can
reference them by their confirmed screen names.

## Template for one step

```
## Step [N]: [short name]
Unlocks when: [prerequisite, e.g. "routine_count >= 2 AND all screens in Step 1 were completed"]
Screens shown, in order: [Screen A] → [Screen B] → [Screen C]
```
