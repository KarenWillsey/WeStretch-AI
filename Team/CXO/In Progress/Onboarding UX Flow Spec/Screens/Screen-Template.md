<!--
Template for one "book" (= one screen). Copy this file to
`Screens/<Screen Name>.md`, using the exact screen name from the top-left
corner of Karen's wireframe image as both the filename and the `screen`
field below; that name is the ID every other screen's button targets
will reference.

Delete this comment block once filled in.
-->

# BOOK: [Screen Name]

Source mockup: `Images/[Screen Name].png`

## Chapter: [condition in plain English, e.g. "0 routines done"]
State: `[condition as it should appear in State-Variables.md, e.g. routines_completed == 0]`

- Title: "..."
- Subtitle: "..." (or "none")
- Button 1 "[label]" → {Screen: [target screen name]}
- Button 2 "[label]" → {Screen: [target screen name]}
- Button 3 "[label]" → {Screen: [target screen name]} (omit if this chapter has no third button)

## Chapter: [next condition]
State: `[condition]`

- Title: "..."
- ...

---

```json
{
  "screen": "[Screen Name]",
  "chapters": [
    {
      "condition": "[condition]",
      "title": "...",
      "subtitle": null,
      "buttons": [
        {"label": "...", "target": "..."}
      ]
    }
  ]
}
```
