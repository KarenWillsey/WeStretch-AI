# Apple Opportunity Radar; Memory

Durable decisions for this project only. See `Implementation Spec.md` for
the reasoning behind each.

## Build session (2026-08-21), fully live

Karen said "go ahead" to build execution. Both skills, both wrapper
scripts, and initial state files were built successfully. Registering the
two Windows Scheduled Tasks (`Register-ScheduledTask`) was blocked twice by
the auto-mode permission classifier, creating unattended system
automation apparently isn't something a blanket "go ahead" clears on its
own in this environment, even after a retry, so Karen ran the
registration herself.

**The nightly task registered fine on the first try** via
`Register-ScheduledTask` + `New-ScheduledTaskTrigger -Daily`.

**The monthly task needed 3 tries:**
1. `New-ScheduledTaskTrigger -Monthly -DaysOfMonth 1 -At ...` → `Register-
   ScheduledTask` failed with "argument is null or empty"; `-Monthly`
   silently returned a null trigger without the `-Months` parameter.
2. Added `-Months <all 12 names>` → `-Monthly` errored as "parameter
   cannot be found"; it wasn't a real parameter set on this machine's
   `New-ScheduledTaskTrigger` at all. Root cause: Karen's shell prompt is
   PowerShell 7 (`.venv`-activated), which loads the built-in
   `ScheduledTasks` module through a Windows-PowerShell compatibility
   proxy that doesn't reliably expose every parameter set (`-Daily`
   survived the proxy, `-Monthly` didn't).
3. Switched to `schtasks.exe /sc monthly /d 1` directly to sidestep the
   module entirely, but PowerShell's own native-argument quoting kept
   mangling the `/tr` value (a string containing embedded spaces *and*
   embedded double quotes, needed because the wrapper script's own path
   has spaces in it) across two more attempts. **What finally worked:**
   writing the exact `schtasks` command into a plain `.cmd` batch file and
   having Karen execute that file directly; this routes the string
   through `cmd.exe`'s parser once, with no PowerShell re-quoting layer in
   between at all.

**Lesson for next time this needs redoing** (e.g. if the task ever needs
re-registering): skip straight to the batch-file approach for any
`schtasks`/native-command call whose arguments contain both spaces and
embedded quotes; don't bother with `Register-ScheduledTask -Monthly` in a
PowerShell-7-via-venv shell, and don't try to hand a quoted string directly
to a native command through PowerShell's argument passing.

**Confirmed live 2026-08-21:** both tasks show `State: Ready`. First real
unattended runs: nightly 2026-08-21 8:00 PM, monthly 2026-09-01 7:00 AM.

## Manual end-to-end test run (2026-08-21), loop confirmed working

Ran both skills manually (in-session, not via the scheduled tasks) to
verify the whole loop before trusting it unattended:

- **Nightly-action:** worked the top backlog item (Small Business Program
  enrollment), correctly recognized it as a verification-shaped item it
  couldn't confirm directly, and produced a checklist instead of falsely
  claiming enrollment status, exactly the intended behavior. Output,
  Backlog.md, last-run.log, and WORK-TRACKER hand-off all updated correctly.
- **Monthly-refresh:** fetched all 13 confirmed source URLs successfully.
  Found real (not cosmetic) changes in 9 of 13 sections, expected, since
  the existing baseline was Karen's manual excerpt, not a full live pull.
  Knowledge Base, Backlog.md (4 new items), monthly-refresh-log.json, and
  WORK-TRACKER were all updated correctly. Also ran the WebSearch pass for
  the "still-unconfirmed candidates" and found solid URLs for TestFlight
  and App Clips, plus the general Apple Developer News feed, correctly
  did NOT auto-add them as tracked sections (per the skill's own caution
  rule), just flagged them in Implementation Spec section 1 for a human
  to sanity-check first.

**Conclusion: both skills work as designed.** Safe to let the unattended
schedule run for real going forward. Nothing to fix.

## The live App Store listing is readable without App Store Connect (2026-09-06)

Found during the 2026-09-06 nightly run, which had been told (by an
earlier run's own note) that no English product page metadata existed.
It did. It was live on the App Store the whole time; only the repo had no
record of it. **Check the live listing before ever concluding an App
Store asset "does not exist."**

Two public, unauthenticated sources cover most fields, and both were
verified working:

- `https://itunes.apple.com/lookup?id=1458915362&country=us` returns
  JSON with the app name, the full description, version, release date,
  seller, categories, price, **minimum iOS version**, average rating,
  rating count, and the current release notes.
- The storefront HTML (`https://apps.apple.com/us/app/id1458915362`,
  fetched with a browser user agent) contains the **subtitle**, which the
  lookup API does not return. Grep the HTML for `"subtitle":"`. The same
  trick reads competitors' subtitles from the "You Might Also Like" rail,
  which is free keyword research.

**Two fields stay invisible from outside and always need App Store
Connect:** the keyword field and promotional text. Never guess at their
current values; propose, and say plainly that it is a proposal.

WeStretch's App Store app ID is **1458915362**. The storefront URL slug
(`westretch-the-stretching-app`) is stale and does not match the current
app name, which is normal; the slug does not update when the name does.

## The live IAP list is readable too, and WeStretch does sell via Apple IAP (2026-09-07)

Extends the 2026-09-06 note below. The storefront HTML also carries the
in-app purchase list, which the `itunes.apple.com/lookup` API does not
return. In the page's embedded JSON, look for an `Annotation` block with
`"title":"In-App Purchases"`; its `textPairs` are `[name, price]`.

**This settles a question that had blocked the 2026-08-30 subscription
offers item: WeStretch transacts through Apple IAP, not only Stripe.**

Live US SKUs as of 2026-09-07 (Apple caps this public list at 10 and orders
it itself, so there may be more): Premium Monthly $9.99, Premium Yearly
$59.99, Premium Quarterly $20.99, 999 Coins $6.99, 200 Coins $1.99, 50
Coins $0.99, Streak Saver (1) $1.99, Streak Saver (7) $11.99, Streak Saver
(3) $4.99, Pro Quarterly $69.99. The Premium Monthly/Yearly prices match
the website's Stripe links exactly, so the channels are at price parity.

**Unresolved naming split, don't write copy around it until Karen rules:**
the App Store sells "**Premium**" Monthly/Yearly/Quarterly, but the app's
own onboarding/paywall spec (`Team/CXO/In Progress/Onboarding UX Flow
Spec/`) calls the paid tier "**Pro**" everywhere. There is *also* a
separate "Pro Quarterly" at $69.99 alongside "Premium Quarterly" at $20.99,
and nothing in this repo explains what the difference is.

## WeStretch is a dark-themed app, and the whole product page is dark (2026-09-08)

Found during the 2026-09-08 nightly run, working a backlog item that assumed
the opposite. **All 10 live iPhone screenshots and all 10 iPad screenshots
show a dark app UI on a dark caption band.** There is no light screen
anywhere on the product page. Do not accept a future "add a Dark Mode
screenshot" item at face value; it is already satisfied.

This is deliberate, not accidental. The approved brand palette in
`App Store Image Creation/Memory.md` is Fire Red #FC4850 / White #FFFFFF /
Midnight Grey #1F1F1F, with a charcoal RGB(12,13,14)->RGB(30,30,31) caption
band. The CXO redesign prototype
(`Team/CXO/In Progress/Westretch-UX/public/screens/westretch/`) is dark too;
11 of 12 sampled screens. **So the current screenshots will not go stale when
the redesign ships**, a risk worth not re-checking.

**How to inspect the live screenshots without App Store Connect:** the
`itunes.apple.com/lookup` call already in this file returns `screenshotUrls`
and `ipadScreenshotUrls` at thumbnail size. Swap the trailing
`/320x480bb.jpg` for `/600x0w.png` to get a readable version. Measure mean
luminance to triage, but **always look at a few**: WeStretch's brighter
screenshots (mean luma ~112) are sunlit lifestyle photography with a
near-black app UI composited on top, so the number alone is misleading.

**Still unanswered, and it needs the iOS project:** whether the app is
*adaptive* (honours the system Light/Dark setting) or *hard-locked* to dark.
The `UIUserInterfaceStyle` key in the app target's Info.plist decides it.
If adaptive, the product page needs a *Light* Mode screenshot, the reverse
of what the backlog item asked for. If fixed dark, there is nothing to do.
Record the answer here when someone checks, so a monthly refresh does not
raise this a third time.

## The App Privacy label and Accessibility labels are readable too (2026-09-09)

Third finding in the same series as the 2026-09-06 / 2026-09-07 / 2026-09-08
notes above: the storefront HTML also carries the **App Privacy** panel and the
**Accessibility** panel. Search the HTML for `privacyTypes` and read the plain
text that follows; `privacyHeader` and `privacyFooter` bracket the section.

**WeStretch's declared privacy label, as of 2026-09-09:**

- Data Used to Track You: **nothing declared**
- Data Linked to You: **nothing declared**
- Data Not Linked to You: Usage Data -> "Other Usage Data"

That is near the floor of what an app can declare, and it is a genuinely useful
audit yardstick: any SDK in the shipping build that tracks, or collects a data
type not on that list, makes the *public label* wrong, which is a removal risk
in its own right regardless of the SDK rules. Use it as the pass/fail anchor for
anything privacy-shaped rather than reasoning about SDKs in the abstract.

**Accessibility Nutrition Labels are entirely undeclared.** The live page says
"The developer has not yet indicated which accessibility features this app
supports." Nine categories are declarable (see the Knowledge Base 2026-08-21
entry) and WeStretch currently appears in **none** of the App Store's
accessibility filters. Given the older-adult positioning this is a real
discovery miss, not a formality. The 2026-08-31 accessibility checklist did not
catch it because that item checked whether the app *meets* the requirements, not
whether the declaration was ever filled in. Flagged to the Manager 2026-09-09;
not yet a backlog item.

Same fetch also re-confirms: seller We Bananas Software Inc., 418.9 MB, Health &
Fitness, iOS/iPadOS 15.2 minimum, **visionOS 1.0**, English/French/Spanish, 9+.

## A Featuring Nomination needs the event to exist first, and the 3-month cap is real (2026-09-10)

Two rules that reorder the whole In-App Event plan, settled during the
2026-09-10 nightly run:

1. **You cannot nominate an In-App Event that has not been created.** Apple's
   nomination flow asks you to select the event, so the order is: build the
   mechanic, create the event in App Store Connect, get it *approved*, then
   nominate, then publish inside the 14-day promotion window. App Store Connect
   holds up to 15 approved events and publishes up to 10, so "approved but not
   published" is a legitimate holding state and is exactly what you want while
   a nomination is under review. The backlog item implied the reverse order.
2. **Nominations are accepted a maximum of 3 months ahead**, minimum 2 weeks.
   That makes the January fitness-resolution surge un-bookable until autumn:
   a Mon 2027-01-04 start is 116 days out, so its nomination window opens
   **2026-10-06**. Recommended plan is to aim at 2027-01-04 and nominate the
   day the window opens; fallback start Mon 2026-11-02, nomination due
   2026-10-19.

**Also readable from the storefront: whether any event is live or upcoming.**
Fetch the storefront HTML as in the 2026-09-06 note and search for event data.
An app with no events has only the empty `appEvents` slot in the page's module
ordering list and no event payload. Confirmed 2026-09-10: **WeStretch has no
In-App Event live or scheduled.** Do not assume the 7-Day Mobility Challenge
was ever created.

**The blank Accessibility Nutrition Labels are not just a discovery miss, they
block this nomination.** Accessibility is one of Apple's seven stated
evaluation criteria and WeStretch's pitch leans on older-adult usability, so
nominating while the declaration is empty asks an Apple editor to take
accessibility on trust when the listing itself says nothing. Fixing it needs no
code. Same for ratings volume, one of the product-page-quality signals: **53
ratings at 4.45 stars as of 2026-09-10**, which the still-unimplemented
2026-08-28 native rating prompt plan is the lever for.

Current live version as of 2026-09-10 is **8.1.33**, shipped that same day.

## Two Apple subscription levers, settled (2026-09-11)

**The monthly-with-12-month-commitment plan is not available in the United
States or Singapore.** Available in the other 173 storefronts. So it is an
international-only lever, never a general "third tier." Three more rules that
shape any future discussion of it:

- It is a billing option layered on the **existing 1-year subscription**, not a
  new product. Upfront Billing availability has to be set up first; monthly
  billing is only offered where upfront billing is.
- **The 12-payment total must be between 1.0x and 1.5x the annual upfront
  price.** Because WeStretch's annual is priced well under 12x monthly, the
  1.5x ceiling always lands *below* the standalone monthly price. The plan
  cannot avoid looking like a discount while paying about 47% more than annual.
- Cancelling mid-commitment does not stop the payments (except in certain
  regions), and completing 12 payments rolls into **another** 12-month
  commitment. Heavier lock-in than the annual plan.
- Needs device OS 26.4+ and an app built with SDK 26.5+. Not a blocker (iOS
  26.6.2 was current in early Sept 2026, iOS 27 shipped 2026-09-14) but
  WeStretch's iOS 15.2 floor means older-device users never see it.

**Streamlined purchasing only covers Win-back Offers and Contingent Pricing.**
It is on by default and it is much narrower than its name suggests: it does
*not* cover offer codes or promo codes. WeStretch has neither win-back offers
nor contingent pricing configured, so **the setting is currently attached to
nothing**. Do not treat a future "should we turn this off" question as urgent
until win-back offers actually go live.

**It also cannot be turned off today.** Apple requires the latest approved
binary to implement the `PurchaseIntent` StoreKit API before the toggle is
available. Recommendation recorded in the output: leave it ON, ship
`PurchaseIntent` so an App-Store-side purchase reconciles to a WeStretch
account, and only flip it off if that reconciliation proves impossible.

## International pricing is real, differentiated, and roughly 40% cheaper in the UK and Germany (2026-09-11)

Extends the 2026-09-07 IAP note. The same storefront-HTML `textPairs` trick
works on **any** country code, so per-territory pricing is readable without App
Store Connect. Read 2026-09-11:

| | US | UK | Germany | Canada | Australia |
|---|---|---|---|---|---|
| Premium Monthly | $9.99 | £4.99 | €4.99 | C$9.99 | A$9.99 |
| Premium Yearly | $59.99 | £34.99 | €34.99 | C$59.99 | A$69.99 |
| Premium Quarterly | $20.99 | £11.99 | (not in top 10) | C$20.99 | A$22.99 |

£4.99 is about US$6.30 and €4.99 about US$5.40. **Never assume US prices apply
elsewhere** when doing any pricing or LTV math for this project.

**Two SKUs exist that have never shown in the US list:** "Missed Day Token"
(C$2.99 / A$2.99) and **"Pro Monthly" at €34.99** in Germany, next to Premium
Monthly at €4.99. Apple caps the public list at 10 and orders it itself, so
this may be display ordering rather than availability. But it is a second data
point on the unresolved Premium-vs-Pro split from 2026-09-07, and it is a
seven-fold price gap nothing in this repo explains.

App confirmed unchanged from 2026-09-10: version 8.1.33, 53 ratings, 4.45
stars, US IAP list identical.

## The backlog ran dry on 2026-09-11

The 2026-09-11 run took the last item in "Not started." Unless new items are
seeded, the next nightly run is a legitimate no-op. Seeds come from the monthly
refresh (next 2026-10-01) or from Karen/the Manager. Two candidates are already
surfaced and waiting on a decision: the blank Accessibility Nutrition Labels
(raised 2026-09-09) and shipping `PurchaseIntent` (raised 2026-09-11). Per the
skill's own rule, a nightly run does not invent its own backlog items.

## `state/last-run.log` is locked during every scheduled run; write the banner to stdout (2026-09-09)

Recurring, wastes time every night until it is written down, so: the wrapper
`run-nightly-action.ps1` pipes the CLI's entire output into `last-run.log` with
`*>> $logFile`, and PowerShell holds that handle open for the whole run. **The
skill's step 5 "append to state/last-run.log" therefore always fails** with
"Device or resource busy" / "being used by another process", from Bash and from
`Add-Content` alike. It is not a permissions problem and retrying will not help.

**What works, and what earlier runs settled on:** print the banner line as part
of the final response. The wrapper's redirect carries it into the log anyway.
This is why several banner lines in the log start with a stray backtick or bold
markers; they arrived through the transcript, not through a file append.

**The underlying defect is worth fixing properly:** point the wrapper's `*>>`
redirect at a separate transcript file (e.g. `state/nightly-transcript.log`) and
leave `last-run.log` free for the skills to append to. Not done unprompted,
since it means editing a live Scheduled Task's wrapper script.

**Related, still open:** 7 of the scheduled runs so far (2026-08-22, 08-24,
08-25, 08-27, 09-02, 09-03, 09-04) have a "Starting" line and no banner at all.
08-24 and 08-25 are already tracked in `WORK-TRACKER.md` as a reliability gap;
the others did produce `Output/` files, so those are banner-only misses.

## Knowledge Base baseline (2026-08-21)

Karen provided a full, sourced Apple Developer checklist for WeStretch
(16 sections, each with its own developer.apple.com Source line, plus a
10-item "Highest-Priority Actions" list). This is now the real content of
`Knowledge Base/apple-marketing-opportunities.md`, replacing the earlier
empty skeleton, and `Backlog.md`'s seed list was replaced with the 10
priority actions from it. This was a manual one-time seed, not a reversal
of the "monthly refresh fetches live" decision below, future refreshes
still fetch developer.apple.com live and diff against this baseline.

## Standing decisions (2026-08-21, Karen's answers during planning)

- **Scope is broad, not just metadata/screenshots.** Cover every Apple
  marketing lever: product page metadata, screenshots/previews, Custom
  Product Pages, Product Page Optimization (A/B testing), In-App Events,
  Apple Search Ads, TestFlight, App Clips, editorial/"Nominate an app"
  pitches, feature-adoption bonuses, seasonal moments (e.g. January
  fitness-resolution surge). Do not narrow this back to just what
  `.agents/skills/aso/references/apple-specs.md` already covers.
- **Monthly refresh fetches developer.apple.com live** (WebFetch/WebSearch
  against a tracked URL list), diffs against the last saved snapshot in
  `Knowledge Base/`. Not a manual "Karen pastes a file" process.
- **The Manager must be notified every time the monthly refresh completes**,
  even if nothing changed ("checked, no changes" is itself a required
  output; silence is not acceptable). This is the same "fail loud, never
  silent" bar the daily-brief project (`Team/CEO/In Progress/Set up Daily
  housing/`) uses.
- **Automation is a local Windows Scheduled Task**, same pattern as the
  daily brief, not the cloud `/schedule` skill, for the same reason the
  daily brief rejected it (isolated cloud clone can't reliably read/write
  this repo's state and output files).
- **The Manager is expected to police the schedule.** At the start of any
  session, the Manager should check whether the nightly and monthly runs
  actually fired on schedule (via `state/` timestamps once built). If a run
  is missing/stale, flag it to Karen immediately and offer to trigger a
  manual re-run right then; don't wait for Karen to notice. Mirrors the
  daily brief's "runs every time" reliability bar, applied here as an
  explicit Manager-side check since this automation, like the daily brief,
  only fires if Karen's machine is on and she's logged in at that hour.
