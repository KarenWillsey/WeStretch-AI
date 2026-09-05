# BOOK: Routine Recap

No source mockup: not among the uploaded wireframes. Content fully
dictated by Karen; formalized as its own book here (was previously only
captured inline in `Storyline.md` step S1). Applies [[Brand-Voice-Principles]].

First sheet of the drip funnel, shown right after `Collect coins` on the
**first routine completion**. **Confirm with Karen:** does this repeat
every session, or only the first time? Dictation implies first-time-only
but wasn't stated outright.

## Chapter: default
State: (none, first routine completion only, per the open question above)

- Title: "Your routine was {routine_length_minutes} minutes long, {routine_path == 'full_body' ? 'full body' : chosen customize style}."
- Subtitle: "Keep up your mobility."
- Body: explains the app builds the next routine off the user's history,
  so routines evolve with them; recommends logging in to save history,
  use the account across multiple devices, and protect against losing
  everything on a new phone.
- Button 1 "Sure, I'll log in" → {Screen: Sign Up} (existing app login
  flow), on success, `account_type` becomes `free`, then → {Screen: Leaderboard Explainer}
- Button 2 "Continue as guest" → {Screen: Leaderboard Explainer} (`account_type` stays `guest`)

---

```json
{
  "screen": "Routine Recap",
  "chapters": [
    {
      "condition": "first routine completion",
      "title": "Your routine was {routine_length_minutes} minutes long, {routine_style}.",
      "subtitle": "Keep up your mobility.",
      "buttons": [
        {"label": "Sure, I'll log in", "target": "Sign Up", "then_target": "Leaderboard Explainer", "sets": {"account_type": "free"}},
        {"label": "Continue as guest", "target": "Leaderboard Explainer"}
      ]
    }
  ]
}
```
