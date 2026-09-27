# BOOK: First Screen

Source mockup: `Images/Screenshot 2026-08-19 151826.png` (screen 3)
Applies [[Brand-Voice-Principles]] throughout: personalized/intelligent
framing, Ada advancing the user, ego-forward copy, invested-progress FOMO
toward Pro.

Legend: **(Karen's wording)** = dictated verbatim or near-verbatim.
**(drafted; confirm)** = Claude drafted this copy where Karen asked for
help or left a gap; needs her approval/edit before it's final.

---

## Chapter: routines_completed == 0 (any account_type)
State: `routines_completed == 0`

- Title: "Welcome. Let's get you stretching." **(Karen's wording)**
- Subtitle: none
- Login link (bottom of screen) → {Screen: Sign Up} (existing app login flow, not part of this spec)
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}

## Chapter: routines_completed == 1, account_type == guest
State: `routines_completed == 1 AND account_type == "guest"`

- Title: "Welcome back" **(Karen's wording)**
- Subtitle: "Once an account is created, we can remember your settings." **(Karen's wording)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}

## Chapter: routines_completed == 1, account_type == free
State: `routines_completed == 1 AND account_type == "free"`

- Title: "Welcome back, {first_name}" **(Karen's wording)**
- Subtitle: "Explore all the customizations available to fit your needs today." **(Karen's wording)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}
- Button 3 "Last routine settings" → {Screen: Rating} (uses saved `last_routine_settings`, skips the wizard)

## Chapter: routines_completed == 2, account_type == guest
State: `routines_completed == 2 AND account_type == "guest"`

- Title: "Welcome back to your 3rd routine" **(Karen's wording)**
- Subtitle: "Take notice of the shifts occurring in your body." **(Karen's wording)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}

## Chapter: routines_completed == 2, account_type == free
State: `routines_completed == 2 AND account_type == "free"`

- Title: "Welcome back for your 3rd routine, {first_name}" **(Karen's wording, exact word order TBD; confirm)**
- Subtitle: "Look around and take full advantage of our customizations." **(Karen's wording)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}
- Button 3 "Last routine settings" → {Screen: Rating} **(3-button pattern inferred from Chapter routines_completed==1/free; confirm free users always get this 3rd button from routine 1 onward)**

## Chapter: routines_completed == 3, account_type == guest
State: `routines_completed == 3 AND account_type == "guest"`

- Title: "Welcome back to your 4th routine" **(drafted; confirm, follows the established "to your Nth routine" pattern)**
- Subtitle: "Changing phones or want to use multiple devices? Sign up and your data will be saved." **(drafted from Karen's dictated content; confirm exact wording)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}

## Chapter: routines_completed == 3, account_type == free
State: `routines_completed == 3 AND account_type == "free"`

- Title: "Welcome back to your 4th routine, {first_name}" **(drafted; confirm)**
- Subtitle: "As a free user, you get 11 fully unlocked routines as our gift (after that, go Pro to keep everything unlocked." **(drafted from Karen's dictated content) confirmed 2026-08-20 against the resolved 14-routine trial budget: 14 − 3 = 11, checks out)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}
- Button 3 "Last routine settings" → {Screen: Rating}

## Chapter: routines_completed == 4, account_type == free
State: `routines_completed == 4 AND account_type == "free"`

- Title: "10 routines left, {first_name}" **(drafted; Karen explicitly asked for help with this one, confirm)**
- Subtitle: "Your full-body routine moves every joint, every direction (see how far you've come." **(drafted) intentionally does not mention that customize/style choice is what's locked, per Karen's instruction not to say that explicitly)**
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second} (individual locked routine types inside Second/pain/sport/standing/floor/Base Positions/Body Filter route to `paywall place holder` if tapped by a free user; see [[Routine Type 2]])
- Button 3 "Last routine settings" → {Screen: Rating}

## Chapter: routines_completed >= 4, account_type == guest
State: `routines_completed >= 4 AND account_type == "guest"`

**Fixed 2026-08-21; this chapter was missing.** Karen only dictated
guest copy through `routines_completed == 3`; routines 4+ had no matching
chapter, which is a bug (undefined screen state). Karen separately
confirmed guests keep the same 2-button pattern indefinitely ("the guest
user only has the same 2 buttons as above"), so this chapter repeats that
pattern rather than inventing new copy.

- Title: "Welcome back to your {routines_completed + 1}th routine" **(pattern extrapolated from earlier guest chapters; confirm)**
- Subtitle: none dictated for this range; reuse routines_completed==3's
  subtitle tone or leave blank until Karen provides copy.
- Button 1 "Full Body" → {Screen: Time}
- Button 2 "Customize" → {Screen: Second}
- Once `routines_completed >= 7` (past the 7-routine guest trial pool):
  the Customize path's routine-type selection becomes gated the same way
  `Routine Type 2` gates a budget-exhausted free user (Full Body only,
  other types blurred, tap → paywall); see the note below. This is a
  guest, not a free user, so it does **not** route through `Routine Type 2`
  the way free users do at routine 7; that consolidation was only
  dictated for free users. **Confirm with Karen**: should guest also
  collapse into `Routine Type 2` at routine 7, or does gating apply
  in-place within the existing wizard screens (Second/pain/sport/etc.)?

## Chapter: routines_completed == 5, account_type == free
State: `routines_completed == 5 AND account_type == "free"`

- Title: "9 routines left, {first_name}" **(drafted, following the countdown pattern; confirm)**
- Subtitle: same pattern as routines_completed==4 chapter, or Karen may want variation, **not yet dictated**
- Buttons: same 3 as above

## Chapter: routines_completed >= 6, account_type == free
State: `routines_completed >= 6 AND account_type == "free"`

- Title: "Welcome back for your {routines_completed + 1}th routine" **(Karen's wording, first said for the 7th routine specifically)**
- Subtitle: "All your customizations are now on one screen." **(drafted from Karen's dictated content; confirm)**
- Single button → {Screen: Routine Type 2} directly, replacing the Full Body / Customize / Last routine settings buttons used through routine 6.
- **Karen: confirm this reading**: your dictation said this chapter's welcome-back copy shows, then routes straight to Routine Type 2, but didn't specify whether First Screen still renders with a button first or skips straight through. Drafted as: First Screen shows this chapter once, with one CTA into Routine Type 2, which is where "Let's stretch" → {Screen: Rating} actually lives (see [[Routine Type 2]]).

## Note: guest past the 7-routine trial pool
Not a separate First Screen chapter: Karen confirmed (2026-08-21) that a
guest who passes `trial_routines_remaining` without signing up gets the
same gating as a budget-exhausted free user: access to the "Full Body"
routine style only, no customization; other options are visible but
blurred, and tapping any of them → {Screen: paywall place holder}. This
gating lives on [[Routine Type 2]] (`account_type == 'free'` chapter),
apply it to guests past-budget too rather than duplicating it here.

## Chapter: account_type == pro
**Not yet dictated.** No Pro-tier First Screen copy has been specified,
flagging as an open item rather than inventing it. Pro users presumably
always see the fully-unlocked 3-button variant, but confirm with Karen.

---

```json
{
  "screen": "First Screen",
  "chapters": [
    {
      "condition": "routines_completed == 0",
      "title": "Welcome. Let's get you stretching.",
      "subtitle": null,
      "login_link": "SignUp",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"}
      ]
    },
    {
      "condition": "routines_completed == 1 && account_type == 'guest'",
      "title": "Welcome back",
      "subtitle": "Once an account is created, we can remember your settings.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"}
      ]
    },
    {
      "condition": "routines_completed == 1 && account_type == 'free'",
      "title": "Welcome back, {first_name}",
      "subtitle": "Explore all the customizations available to fit your needs today.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"},
        {"label": "Last routine settings", "target": "Rating"}
      ]
    },
    {
      "condition": "routines_completed == 2 && account_type == 'guest'",
      "title": "Welcome back to your 3rd routine",
      "subtitle": "Take notice of the shifts occurring in your body.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"}
      ]
    },
    {
      "condition": "routines_completed == 2 && account_type == 'free'",
      "title": "Welcome back for your 3rd routine, {first_name}",
      "subtitle": "Look around and take full advantage of our customizations.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"},
        {"label": "Last routine settings", "target": "Rating"}
      ]
    },
    {
      "condition": "routines_completed == 3 && account_type == 'guest'",
      "title": "Welcome back to your 4th routine",
      "subtitle": "Changing phones or want to use multiple devices? Sign up and your data will be saved.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"}
      ]
    },
    {
      "condition": "routines_completed == 3 && account_type == 'free'",
      "title": "Welcome back to your 4th routine, {first_name}",
      "subtitle": "As a free user, you get 11 fully unlocked routines as our gift; after that, go Pro to keep everything unlocked.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"},
        {"label": "Last routine settings", "target": "Rating"}
      ]
    },
    {
      "condition": "routines_completed == 4 && account_type == 'free'",
      "title": "10 routines left, {first_name}",
      "subtitle": "Your full-body routine moves every joint, every direction; see how far you've come.",
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"},
        {"label": "Last routine settings", "target": "Rating"}
      ]
    },
    {
      "condition": "routines_completed >= 4 && account_type == 'guest'",
      "title": "Welcome back to your {routines_completed + 1}th routine",
      "subtitle": null,
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"}
      ]
    },
    {
      "condition": "routines_completed == 5 && account_type == 'free'",
      "title": "9 routines left, {first_name}",
      "subtitle": null,
      "buttons": [
        {"label": "Full Body", "target": "Time"},
        {"label": "Customize", "target": "Second"},
        {"label": "Last routine settings", "target": "Rating"}
      ]
    },
    {
      "condition": "routines_completed >= 6 && account_type == 'free'",
      "title": "Welcome back for your {routines_completed + 1}th routine",
      "subtitle": "All your customizations are now on one screen.",
      "buttons": [
        {"label": "Continue", "target": "Routine Type 2"}
      ]
    }
  ]
}
```
