# Featuring Nomination Submission Runbook: "7-Day Mobility Challenge"

Addresses backlog item: "Submit the drafted '7-Day Mobility Challenge'
In-App Event (see Output/2026-08-29-in-app-event-7-day-mobility-challenge.md)
for an Apple Featuring Nomination; In-App Events are now an explicitly
nominate-able, featurable content type."
Date: 2026-09-10 (scheduled nightly-action run)

Status: **runbook for whoever holds App Store Connect. Nothing submitted.**
This skill has no App Store Connect access and never takes a live action
against Apple. The backlog item asked for a live submission, so what follows
is the submission sequence, the date math, and the readiness gate that has to
clear first.

---

## 1. What I verified live tonight (no App Store Connect needed)

Read off Apple's public iTunes Lookup API and the US storefront HTML for app
ID 1458915362, the same method recorded in `Memory.md`:

| Check | Result |
|---|---|
| Any In-App Event live or upcoming on the product page | **None.** The storefront page carries no event payload at all, only the empty `appEvents` module slot in the layout template. The 7-Day Mobility Challenge has not been created in App Store Connect. |
| Current version | **8.1.33, released today, 2026-09-10** ("small and quick update" to routine types plus Full Body poses, per the release notes) |
| Ratings | **4.45 stars from 53 ratings**, US storefront |
| Minimum iOS | 15.2 |
| Editors' Choice badge | Not present |

**The 53-rating count is the finding that matters here.** Apple's published
evaluation criteria for a Featuring Nomination include product page quality,
and ratings are part of that. 53 ratings is thin for a nomination in a
category as crowded as Health and Fitness. The already-drafted native rating
prompt plan (`Output/2026-08-28-native-rating-prompts-plan.md`) is the lever
that fixes this, and it is still unimplemented. Shipping it before nominating
is worth more to the nomination than any wording change to the pitch.

## 2. The sequencing problem, and the answer

**You cannot nominate an In-App Event that does not exist yet.** Apple's
nomination flow asks you to select the event you are nominating, so the event
has to be created and approved in App Store Connect first. That reorders the
work from what the backlog item implies.

Apple's two timing rules pull in opposite directions:

- **Nomination:** at least 2 weeks' notice, accepted up to 3 months in advance.
- **Event promotion window:** an approved event can only go *live* on the
  product page up to 14 days before its start date.

These reconcile because App Store Connect lets you hold up to 15 **approved**
events and publish up to 10 at a time. So an event can be created, submitted,
and approved months early, then published inside the 14-day window. Approved
but unpublished is the state you want while the nomination is under review.

**Correct order:**

1. Confirm the "Day N unlocks a themed session" mechanic is buildable and pick a start date.
2. Build the event card artwork (clean art, no text or logo, no border or gradient).
3. Create the event in App Store Connect and submit it for review. Get it approved.
4. Submit the Featuring Nomination, selecting the now-approved event.
5. Publish the event inside its 14-day promotion window.

## 3. Date math, and why the January slot is not bookable today

Today is 2026-09-10, a Thursday. Working backwards from a Monday start date
(a Monday keeps the "Day 1 of 7" framing on a calendar week, per the event draft):

| Start date | Nomination window opens (start minus 90 days) | Nomination deadline (start minus 14 days) | Publish event by |
|---|---|---|---|
| Mon 2026-10-05 | already open | 2026-09-21 | 2026-09-21 |
| Mon 2026-11-02 | already open | 2026-10-19 | 2026-10-19 |
| Mon 2027-01-04 | **2026-10-06** | 2026-12-21 | 2026-12-21 |

**The New Year fitness surge slot cannot be nominated yet.** 2027-01-04 is 116
days out, past Apple's 3-month window. The earliest you can nominate it is
**2026-10-06**. Apple's window today reaches only to 2026-12-09.

**Recommendation: aim at Mon 2027-01-04 and nominate on 2026-10-06.** The
January resolution surge is the single strongest fitness moment of the year and
is named as a target in this project's own standing decisions. It also buys
almost four months to close the readiness gaps in section 4, which a
2026-10-05 start does not. If Karen wants something live sooner, 2026-11-02 is
the realistic fallback, and the nomination for it is due 2026-10-19.

## 4. Readiness gate: close these before nominating, not after

The pitch copy is already written and still stands
(`Output/2026-09-01-featuring-nomination-draft.md`). These are the substantive
gaps that would weaken the nomination itself.

- [ ] **Accessibility Nutrition Labels are entirely undeclared.** Found
      2026-09-09; the live page says the developer has not indicated which
      accessibility features the app supports, so WeStretch appears in none of
      the App Store's accessibility filters. **Accessibility is one of Apple's
      seven named evaluation criteria**, and the pitch leans on older-adult
      usability. Nominating while the declaration is blank asks an Apple editor
      to take accessibility on trust when the app's own listing says nothing.
      This is the highest-value fix on the list and it needs no code, only the
      declaration filled in.
- [ ] **Ratings volume.** 53 ratings at 4.45 stars. Ship the native rating
      prompts (2026-08-28 plan) and let them accumulate before nominating. The
      January timing gives roughly three months of runway for this.
- [ ] **Localization claim.** The pitch cites French and Spanish. Screenshot and
      preview copy is translated; product page metadata is English-only. The
      2026-09-01 draft already hedges this correctly. Either close the metadata
      localization first or keep the hedge.
- [ ] **Event mechanic confirmed buildable.** Open since 2026-08-29. Do not
      nominate a feature that does not exist yet.
- [ ] **Long description A or B chosen.** Open since 2026-08-29. Recommendation
      stands at Option B: "Seven days, one guided stretch a day. Physio-informed,
      step-by-step, paced to your body." (88 characters.)
- [ ] **Event card artwork built.** Route to `App Store Image Creation/` per the
      event draft's section 4. Apple may ask for promotional artwork during
      nomination review, so have it ready before submitting rather than
      scrambling afterwards.

## 5. Compliance re-check at submission time

Re-run these against the pitch copy on the day it is submitted, since the
underlying facts move:

- [ ] No pricing anywhere in the event metadata or the pitch.
- [ ] No superlatives or unverifiable claims.
- [ ] No competitor names.
- [ ] Event name is not a call to action, no all-caps, no excessive punctuation.
- [ ] Event artwork carries no text or logo, no pre-applied border or gradient.
- [ ] Any star-rating or review quote used is re-checked against the live
      current rating that day (per the 2026-09-02 reviewer-permission process).
- [ ] Accessibility framed as design intent unless the declaration is filled in
      by then, in which case it can be stated as fact.

Guideline 2.3.13 covers inaccurate In-App Event metadata or timing, so a start
date that slips after approval is a real rejection risk, not a formality.

## 6. Decisions needed from Karen

1. Start date: Mon 2027-01-04 (recommended, nominate 2026-10-06) or Mon 2026-11-02 (nominate by 2026-10-19).
2. Is the "Day N unlocks a themed session" mechanic buildable with current app logic?
3. Long description, Option A or B.
4. Who holds App Store Connect and will actually run steps 3 to 5 in section 2.
5. Should the Accessibility Nutrition Labels declaration become its own backlog item? It was flagged 2026-09-09 and is now blocking this nomination too.

## 7. What this skill could not do

- Could not create the event, submit it, or file the nomination. No App Store
  Connect access, and live submission is out of scope for this skill regardless.
- Could not confirm the exact field structure of Apple's current nomination
  form; it is not documented in the Knowledge Base and is not publicly readable.
  Map the 2026-09-01 pitch content onto whatever fields the live form shows.
- Could not verify the event mechanic is buildable; that needs the product and
  engineering side, not this repo.
