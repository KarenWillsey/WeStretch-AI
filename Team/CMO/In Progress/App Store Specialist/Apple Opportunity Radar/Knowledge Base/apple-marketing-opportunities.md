# Apple Marketing Opportunities; Knowledge Base

**Status: seeded with a real baseline (2026-08-21, Karen-provided).** This
replaces the earlier empty skeleton. The content below was compiled by
Karen from the developer.apple.com pages cited under each section's
`Source:` line; treat those lines as the last-verified reference for that
section, dated 2026-08-21, until a monthly refresh re-checks them.

**Important for future sessions:** this baseline was hand-provided this one
time, not fetched live by Claude. The standing decision in `../Memory.md`
that the monthly refresh fetches developer.apple.com **live** still
applies going forward; this file is the starting snapshot to diff future
fetches against, not a reason to switch to manual updates.

## Changelog

- **2026-09-01 (monthly refresh)**: Second live monthly-refresh run (first
  run via the actual scheduled task, not a manual test). Fetched all 13
  confirmed source URLs successfully (0 failures). Found real, actionable
  changes in 10 of 16 sections. Updated: App Store Listing, Screenshots and
  Videos, Ratings and Reviews, App Store A/B Testing, Subscriptions and Free
  Trials, Analytics and Measurement, Revenue and Apple Commissions, Privacy
  and Customer Accounts, App Review and Releases, Getting Featured by Apple.
  No changes to: Custom Product Pages, App Store Events, App Store
  A/B Testing baseline mechanics beyond the additions below, Accessibility,
  Health and Fitness Claims, Metadata rejection triggers table. 5 new
  backlog items added; see `../Backlog.md`. WebSearch pass for
  still-unconfirmed candidates found a solid Apple Search Ads canonical page
  (`developer.apple.com/app-store/promote/`), flagged in
  `../Implementation Spec.md` for human sanity-check rather than auto-added.
  Full run detail in `../state/monthly-refresh-log.json`.
- **2026-08-21 (live refresh)**: First live monthly-refresh run (manual
  test, triggered in session rather than by the scheduled task). Fetched
  all 13 confirmed source URLs successfully (0 failures). Found real,
  actionable additions in 8 of 16 sections, expected for a first live
  pull, since the baseline below was Karen's manually-compiled excerpt
  rather than a full page-by-page pull. Updated: Ratings and Reviews,
  Custom Product Pages, App Store Events, Subscriptions and Free Trials,
  Billing Recovery and Subscriber Retention, Revenue and Apple Commissions,
  Accessibility, Privacy and Customer Accounts, Health and Fitness Claims,
  App Review and Releases, Getting Featured by Apple. No changes to: App
  Store Listing, Screenshots and Videos, App Store A/B Testing, Analytics
  and Measurement, Notifications and Engagement. 4 new backlog items added,
see `../Backlog.md`. Full run detail in `../state/monthly-refresh-log.json`.
- **2026-08-21**: Initial baseline imported (Karen-provided research,
  sourced from the developer.apple.com pages listed per section below). No
  prior snapshot existed, so nothing to diff against yet. The next monthly
  refresh (once built) should re-fetch every Source URL below, diff against
  this baseline, and update whichever sections actually changed, not
  rewrite the whole file. Source attributions are preserved exactly as
  provided; not independently re-verified in this session.

---

## App Store Listing

- App name: Maximum 30 characters.
- Subtitle: Maximum 30 characters.
- Promotional text: Maximum 170 characters.
- Promotional text can be updated without releasing a new app version.
- Keyword field: Maximum 100 characters.
- Separate keywords with commas and avoid unnecessary spaces.
- Do not repeat keywords or include unnecessary plurals.
- Do not use competitors' names or irrelevant keywords.
- Target search terms such as back pain, stiffness, mobility, and stretching.
- Lead the app description with the strongest differentiator and customer benefit.
- Do not stuff the description with keywords.
- Avoid specific prices in descriptions because prices vary by region.
- Select accurate primary and secondary App Store categories.
- Localize metadata for English, French, and Spanish.
- Keep screenshots, descriptions, and claims accurate and current.
- Write meaningful "What's New" release notes.
- **[2026-09-01]** In-app purchases and subscriptions can be showcased
  directly on the product page: up to 20 total items across both sections
  combined, with a customizable display order. Each showcased item gets its
  own display name (max 35 characters) and description (max 55 characters).
  Showcased items are also discoverable in App Store search and can be
  featured on the Today/Games/Apps tabs, routing back to the product page.

Source: https://developer.apple.com/app-store/product-page/

## Screenshots and Videos

- Display up to 10 screenshots per product page.
- The first one to three screenshots can appear in search results.
- Put the strongest customer benefit in screenshot one.
- Highlight one clear benefit per screenshot.
- Show actual app functionality.
- Create appropriate screenshots for iPhone and iPad.
- Localize screenshots for each supported language.
- Add up to three app preview videos.
- Each preview video can be up to 30 seconds.
- Make videos effective without sound because previews autoplay muted.
- Show personalized routine creation within the opening seconds.
- Test Ada, lifestyle photography, and mixed visuals.
- **[2026-09-01]** If the app supports Dark Mode, include at least one
  screenshot showing what the experience looks like in Dark Mode.

Source: https://developer.apple.com/app-store/product-page/

## Ratings and Reviews

- Show Apple's native rating pop-up up to three times per user within 365 days.
- Request ratings after positive moments, such as completed routines or streak milestones.
- Do not request ratings during onboarding or frustrating experiences.
- Respond promptly to negative reviews.
- Address technical issues and customer confusion in review responses.
- Tell reviewers when reported problems have been fixed.
- Reviewers are notified of responses and can update their reviews.
- Avoid resetting the overall rating unnecessarily.
- Resetting the displayed summary rating does not remove written reviews.
- Never offer coins, discounts, or rewards in exchange for reviews.
- **[2026-08-21]** A star rating may be used in marketing only if it
  accurately reflects the app's current rating; quoting a customer review
  in marketing materials requires the reviewer's permission first.
- **[2026-08-21]** Report offensive/spam reviews via "Report a Concern" in
  App Store Connect: do not use a public reply for this.
- **[2026-09-01]** Since iOS 18.4/iPadOS 18.4, Apple shows AI-generated
  "review summaries" on product pages, short paragraphs compiling review
  highlights. Users can tap-and-hold a summary to report a concern.
  Currently English-only, US-only, with planned expansion; nothing for
  WeStretch to configure, but worth knowing it's live when reviewing how
  the product page presents.
- **[2026-09-01]** The displayed summary rating is specific to each
  territory and can be reset per-territory when releasing a new version
  (not just globally).
- **[2026-09-01]** App Store Connect can now send an email alert when a user
  edits a review that WeStretch previously replied to.
- **[2026-09-01]** Direct reviewers reporting download errors or billing
  issues to Apple Support rather than trying to resolve those in a public
  reply.

Source: https://developer.apple.com/app-store/ratings-and-reviews/

## Custom Product Pages

- Create up to 70 additional custom product pages.
- Customize screenshots, previews, and promotional text for each page.
- Create dedicated pages for back pain, knee pain, hip mobility, desk workers, golfers, and pickleball players.
- Match each page to the user's search intent.
- Assign relevant keywords to custom pages.
- Use unique URLs for individual pages.
- Link ads, emails, and social campaigns to the most relevant page.
- Connect Apple Ads campaigns to corresponding custom pages.
- Add deep links to relevant destinations inside the app.
- **[2026-08-21]** Deep links require iOS 18 / iPadOS 18 or later; confirm
  WeStretch's minimum deployment target before committing to deep-linked CPPs.
- Localize custom pages by language and market.
- Compare conversion, retention, downloads, and revenue by page.
- Submit custom page changes independently of app updates.
- **[2026-08-21]** Apple's own published conversion stats: custom product
  pages average +2.5 percentage points conversion vs. the default page
  (2.5% vs 1.6% baseline, ~156% relative improvement). Case studies cited:
  CBS Sports +20% conversion; State of Survival +33% conversion and -14%
  cost per install.
- **[2026-08-21]** CPPs are compatible with Apple Search Ads (Search tab
  placements and search-result variations) and with StoreKit-rendered ads
  via the `customProductPageIdentifier` parameter, links this opportunity
  directly to any future Apple Search Ads work.

Source: https://developer.apple.com/app-store/custom-product-pages/

## App Store A/B Testing

- Use Apple's Product Page Optimization.
- Test up to three alternative versions against the original.
- Test screenshots, screenshot order, previews, and icons.
- Compare pain relief, mobility, independence, and personalization messaging.
- Test different first-screenshot headlines.
- Allocate traffic between test versions.
- Monitor results in App Store Connect.
- Apply the winning version to the default product page.
- Continue testing regularly.
- **[2026-09-01]** Only one test can be running at a time.
- **[2026-09-01]** Tests run for up to 90 days (or until manually stopped),
  and results need to reach at least 90% confidence before a treatment
  should be applied.
- **[2026-09-01]** Traffic allocated to a test is split across its
  treatments, not given to each individually, e.g. 40% traffic allocated
  to a 2-treatment test means each treatment gets 20%.
- **[2026-09-01]** If testing alternate app icons, all icon variants must be
  included in the published app's binary ahead of time.
- **[2026-09-01]** Tests that don't include alternate icons can be submitted
  for review independently of a new app version; icon-variant tests cannot.
- **[2026-09-01]** Localized treatments may take longer to reach a
  significant result. The comparison baseline can be changed at any time.

Source: https://developer.apple.com/app-store/product-page-optimization/

## App Store Events

- Publish In-App Events for challenges, competitions, and new experiences.
- Create events such as "7-Day Mobility Challenge" or "Pickleball Mobility Week."
- Events can appear on product pages, in search, and in editorial placements.
- Events can last up to 31 days.
- Promote events up to 14 days before they begin.
- Maintain up to 15 approved events in App Store Connect.
- Publish up to 10 events simultaneously.
- Event name: Maximum 30 characters.
- Short description: Maximum 50 characters.
- Long description: Maximum 120 characters.
- Use the "Challenge" event type for fitness challenges.
- **[2026-08-21]** Full list of event badge types (not just Challenge):
  Challenge, Competition, Live Event, Major Update, New Season, Premiere,
  Special Event: pick whichever actually fits (e.g. a leaderboard-based
  event is Competition, not Challenge).
- Do not submit ordinary daily routines or generic discounts as events.
- **[2026-08-21]** Additional creative restrictions on event metadata: no
  specific prices, no unverifiable claims ("best," "#1"), no text/logos in
  media, no call-to-action as the event name, no all-caps or excessive
  punctuation, no borders/gradients (Apple applies these automatically).
- Promote event links through email, social media, and advertising.
- Submit events independently of app updates.

Source: https://developer.apple.com/app-store/in-app-events/

## Subscriptions and Free Trials

- Clearly explain which features are free and which require a subscription.
- Show subscription price, billing interval, and renewal terms before purchase.
- **[2026-08-21]** The full billed amount must be the *most prominent*
  price shown on the sign-up screen, a monthly-equivalent or other
  breakdown price can be shown too, but only in a visually subordinate
  position. Don't let a "$X/month" figure outshine the actual amount charged.
- Explain when free trials end and billing begins.
- Offer monthly and annual plans when appropriate.
- Use introductory offers for eligible new subscribers.
- Use promotional offers to retain or recover subscribers.
- Use win-back offers for former subscribers.
- Use offer codes for campaigns, partnerships, and customer recovery.
- Track which offers produce paid conversions and long-term retention.
- Provide an obvious in-app subscription management option.
- Make cancellation easy to locate.
- Distinguish Apple subscriptions from website subscriptions.
- Explain that deleting the app does not cancel an Apple subscription.
- Avoid offering existing subscribers the same subscription again.
- Consider Family Sharing when appropriate.
- Family Sharing can include up to five additional family members.
- Enabling Family Sharing for an applicable subscription cannot be undone.
- **[2026-09-01]** Apple now supports monthly subscriptions with a 12-month
  commitment as an additional plan structure, worth evaluating alongside
  WeStretch's existing Monthly/Annual plans.
- **[2026-09-01]** "Streamlined purchasing" lets a customer complete a
  purchase from outside the app (this can be turned off if unwanted), worth
  confirming whether WeStretch wants this on or off.
- **[2026-09-01]** Win-back offer discovery now spans more surfaces: the App
  Store product page, editorial/recommendation placements (Today/Games/Apps
  tabs), an automatic in-app offer sheet, the customer's Apple Account
  Subscriptions settings, and direct links, with a priority ranking when
  more than one offer is eligible.

Source: https://developer.apple.com/app-store/subscriptions/

## Billing Recovery and Subscriber Retention

- Enable Billing Grace Period.
- Choose a grace period of 3, 16, or 28 days.
- Apple attempts to recover failed renewals for up to 60 days.
- Use App Store Server Notifications to detect renewals, cancellations, failed payments, refunds, and offer redemptions.
- Identify subscribers who turn off auto-renewal.
- Show relevant retention messaging before subscriptions expire.
- Help customers resolve payment problems.
- Track voluntary cancellations separately from failed payments.
- Measure free-trial conversion.
- Compare monthly and annual subscriber retention.
- Track cancellation reasons.
- Run win-back campaigns for former subscribers.
- For qualifying service problems, renewal dates can be extended twice per calendar year.
- Each renewal-date extension can be up to 90 days.
- **[2026-08-21]** Neither a grace-period recovery window nor a renewal-date
  extension counts against the subscriber's continuous one-year tenure that
  determines the standard 85% subscriber-proceeds rate (see Revenue and
  Apple Commissions below): so using these tools to save a subscriber
  doesn't cost WeStretch anything on that front.

Source: https://developer.apple.com/app-store/subscriptions/

## Revenue and Apple Commissions

- Confirm eligibility for Apple's Small Business Program.
- Eligible developers receive a reduced 15% commission rate.
- Eligibility generally requires no more than US$1 million in proceeds across associated developer accounts.
- Enroll proactively rather than assuming the reduced commission applies automatically.
- Monitor proceeds, taxes, refunds, territories, and offer costs.
- **[2026-08-21]** The $1M threshold is checked twice: prior-year proceeds
  to *qualify*, and current-year proceeds (must also stay under $1M) to
  *stay* eligible, exceeding it mid-year reverts future sales to the
  standard rate; falling back under it lets WeStretch re-qualify the
  following year.
- **[2026-08-21]** Enrollment steps: must be the Account Holder in the
  Apple Developer Program → review and accept the Paid Apps Agreement
  Schedule 2 in App Store Connect → list all Associated Developer Accounts.
  The reduced rate takes effect **15 days after the end of the fiscal
  calendar month in which enrollment is approved**, not immediately and
  not retroactively.
- **[2026-08-21]** ~~EU-specific: developers on Apple's EU alternative
  business terms get a 10% commission rate, and *any* subscription (not
  just Small Business Program apps) drops to 10% after its first
  continuous year (vs. the general 85%-proceeds/15%-commission rule
  elsewhere), worth checking if this changes WeStretch's actual EU
  economics, if EU is a meaningful market.~~
  **SUPERSEDED [2026-09-05]:** the EU Alternative Terms Addendum this
  described is discontinued. Apple announced 2026-08-18 that all EU
  developers move to a single set of **unified EU business terms effective
  2026-10-01**. Under those: Apple IAP on the App Store is **26%**, or
  **15%** for Small Business Program participants and for auto-renewable
  subscriptions after their first year; alternative in-app payment
  processing is 20% / 10%; out-of-app link-out offers are 15% / 10% with a
  7-day conversion window; and a 5% Core Technology Commission applies only
  to apps distributed *outside* the App Store (it replaces the per-install
  Core Technology Fee). Net effect for WeStretch: **if enrolled in the
  Small Business Program, the EU rate is 15%, same as everywhere else; no
  EU-specific economics to chase.** Full analysis and the pre-2026-10-01
  Account Holder action:
  `Output/2026-09-05-eu-business-terms-economics-evaluation.md`.
  Sources: https://developer.apple.com/support/apps-in-the-eu/ and
  https://developer.apple.com/support/dma-and-apps-in-the-eu/
  (Flagged for the next monthly refresh: these two URLs are not yet in the
  tracked source list; the Small Business Program page alone will not
  surface EU-terms changes.)
- **[2026-09-01]** New Small Business Program member benefit: developers
  with fewer than 2 million first-time App Store downloads can use Apple
  Foundation Models on Private Cloud Compute at no cloud API cost (subject
  to obtaining the PCC entitlement). CTO-adjacent, relevant only if
  WeStretch is using or planning on-device/PCC AI features, not something
  this project builds itself.

Source: https://developer.apple.com/app-store/small-business-program/

## Analytics and Measurement

- Monitor App Store impressions.
- Monitor product page views.
- Monitor downloads and redownloads.
- Track product page conversion rates.
- Compare performance by acquisition source.
- Compare performance by territory and language.
- Compare custom product page performance.
- Compare customer retention by campaign.
- Identify keywords and pages that attract paying subscribers.
- Track trial starts and trial-to-paid conversion.
- Track renewals, cancellations, and reactivations.
- Monitor monthly recurring revenue.
- Measure average proceeds per paying user.
- Evaluate introductory, promotional, and win-back offers.
- Compare subscriber retention by cohort.
- Separate new users, returning users, current subscribers, and former subscribers.
- Review results after screenshot updates, pricing changes, and major releases.
- **[2026-09-01]** App Store Connect now has a dedicated Offers dashboard
  (introductory/promotional/win-back offers and offer codes performance)
  and a Subscription Retention view (percentage renewed for consecutive
  periods, filterable by acquisition source). Trackable subscription events
  now explicitly include activations, conversions to standard price,
  reactivations, and renewals. Results can also be filtered/grouped by
  proceeds rate (85% vs. 70%) to see which subscriber cohort each metric
  belongs to.

Source: https://developer.apple.com/app-store/subscriptions/

## Notifications and Engagement

- Request notification permission when users understand the benefit.
- Let users choose reminder timing.
- Send useful reminders for stretching goals, streaks, and routines.
- Keep notifications timely and personalized.
- Avoid excessive notification frequency.
- Obtain explicit consent before sending marketing push notifications.
- Provide an easy marketing-notification opt-out.
- Do not include sensitive health information in notifications.
- Avoid interrupting routines with review prompts or paywalls.
- Consider Apple Watch integration and useful widgets.

Source: https://developer.apple.com/app-store/subscriptions/

## Accessibility

- Support larger text and Dynamic Type.
- Prevent enlarged text from being truncated or overlapping controls.
- Ensure sufficient color contrast.
- Support VoiceOver with meaningful button and control labels.
- Support Voice Control for important actions.
- Avoid relying on color alone to communicate important information.
- Support reduced-motion preferences when appropriate.
- Provide captions for spoken instructions and relevant video content.
- Make controls easy for older adults to read and operate.
- Verify accessibility on both iPhone and iPad.
- Declare supported accessibility features in App Store Connect.
- Treat accessibility as a competitive advantage for older users.
- **[2026-08-21]** This declaration mechanism has a name; **Accessibility
  Nutrition Labels**, with 9 specific declarable categories: VoiceOver,
  Voice Control, Sufficient Contrast, Dark Interface, Larger Text,
  Differentiate Without Color Alone, Reduce Motion, Captions, Audio
  Descriptions. Declaring more of these (truthfully) makes WeStretch more
  discoverable to users filtering by accessibility need, directly
  relevant given WeStretch's older-adult audience positioning.
- **[2026-08-21]** Dynamic Type requirement for Nutrition Label
  qualification: support scaling to at least 200%, test up to 310% with
  larger accessibility sizes enabled.

Source: https://developer.apple.com/videos/play/tech-talks/111433/

## Privacy and Customer Accounts

- Maintain an accurate, publicly accessible privacy policy.
- Explain what personal and health-related information is collected.
- Explain why information is collected and how it is used.
- Identify third-party services that receive customer information.
- Explain data retention and deletion practices.
- Keep App Store privacy disclosures accurate and current.
- Include data collected by third-party analytics and advertising software.
- Request only permissions necessary for actual functionality.
- Explain why Apple Health access is requested.
- Obtain App Tracking Transparency permission before applicable tracking.
- Do not track users who deny permission.
- Do not require tracking permission for ordinary app functionality.
- Audit advertising and analytics SDKs.
- **[2026-08-21]** Device fingerprinting is prohibited under the Apple
  Developer Program License Agreement: cannot derive an identifier from
  browser properties, device configuration, location, or network
  connection to uniquely identify a device, and cannot use hashed
  email/phone numbers as a tracking identifier without ATT permission. Any
  ad/analytics SDK doing this risks rejection, worth including explicitly
  in the SDK audit above.
- **[2026-08-21]** Exception: the ID for Vendors (IDFV) can be used without
  ATT permission for analytics *across WeStretch's own apps only*; it
  cannot be combined with other data to track across third-party apps or
  websites.
- **[2026-09-01]** "Tracking" is defined broadly enough to catch unintentional
  cases: using a third-party SDK that combines WeStretch's data with other
  companies' data for ad targeting/measurement counts as tracking requiring
  ATT permission *even if WeStretch itself doesn't use it that way*, the
  SDK's behavior is what matters. Tracking inside an in-app webview requires
  the same ATT prompt as native tracking would.
- **[2026-09-01]** Apple is expanding software-supply-chain integrity
  requirements: third-party SDKs increasingly need signatures and privacy
  manifests. Worth folding into the existing ad/analytics SDK audit backlog
  item (device-fingerprinting) since it's the same audit surface.
- **[2026-09-01]** Developers can offer a separate consent control for local
  privacy-law compliance (e.g. GDPR, ePrivacy) distinct from the ATT prompt.
- Provide in-app account deletion if users can create accounts.
- Allow account deletion regardless of the customer's location.
- Explain that account deletion does not automatically cancel an Apple subscription.
- Direct users to subscription management before account deletion when appropriate.
- **[2026-09-01]** Account deletion can also offer a "deferred" option (schedule deletion to align with subscription expiration) as long as an
  immediate-deletion option is also available.

Sources:
- https://developer.apple.com/app-store/user-privacy-and-data-use/
- https://developer.apple.com/support/offering-account-deletion-in-your-app/

## Health and Fitness Claims

- Describe WeStretch accurately as a stretching, mobility, and wellness app.
- Avoid guaranteed medical outcome claims.
- Avoid unsupported diagnosis, treatment, or injury-prevention claims.
- **[2026-08-21] Hard redline (App Review Guideline 1.4.1):** apps claiming
  to measure x-rays, blood pressure, body temperature, blood glucose, or
  blood oxygen using only device sensors are **not permitted, full stop**,
  never let marketing copy or a feature description drift toward this,
  even implicitly (e.g. no "detects your pain level" framed as a sensor
  measurement).
- Substantiate claims such as "physiotherapist-approved."
- Make safety guidance easy to understand.
- Encourage users to avoid painful movements.
- Explain how users can skip poses or avoid specific joints.
- Handle Apple Health and sensitive information according to Apple's requirements.
- Avoid using sensitive health information for advertising or unrelated purposes.

Source: https://developer.apple.com/app-store/review/guidelines/

## App Review and Releases

- Test releases thoroughly before submission.
- Eliminate crashes, broken links, and unfinished screens.
- Provide Apple reviewers with working login credentials when necessary.
- Explain unusual features and subscription behavior in review notes.
- Keep backend services available during review.
- Provide working support and privacy-policy links.
- Ensure screenshots match actual functionality.
- Clearly distinguish free and paid features.
- Test subscriptions, trials, purchase restoration, and expired access.
- Use TestFlight for beta testing.
- Monitor complaints and crash reports after release.
- Write specific, understandable release notes.
- Prioritize recurring issues mentioned in reviews and support tickets.
- **[2026-08-21]** On average, 90% of submissions are reviewed in under 24
  hours, useful for planning launch timing around In-App Events, seasonal
  campaigns, etc.
- **[2026-08-21]** Expedited review can be requested for critical bug fixes
  or event-related apps, worth using when a time-sensitive In-App Event
  or seasonal campaign is at risk from normal review timing.
- **[2026-08-21]** An appeal can be submitted if WeStretch believes a
  rejection was made in error or unfairly.
- **[2026-09-01]** If additional issues turn up while a bug-fix update is
  under review, and none involve legal/safety concerns, Apple now lets the
  developer opt to resolve them in the next submission instead of blocking
  the current one, reply to the offer message in App Store Connect to
  accept.
- **[2026-09-01]** 30-minute Webex appointments with App Review are
  available to discuss guidelines/best practices directly, worth using
  ahead of a first Featuring Nomination or a submission with unusual
  subscription/health-claim framing.
- **[2026-08-21]** Metadata rejection triggers worth keeping front-of-mind
  when drafting App Store copy/screenshots/events (App Review Guideline
  §2.3, consolidated from the Health and Fitness Claims source below):

  | Guideline | Rejection trigger |
  | --- | --- |
  | 2.3.1(a) | Hidden features, misleading marketing, false claims/pricing |
  | 2.3.2 | Not disclosing IAPs in description/screenshots |
  | 2.3.3 | Screenshots that don't show the app in actual use (splash/login only) |
  | 2.3.4 | Preview videos using non-app content |
  | 2.3.5 | Wrong category selected |
  | 2.3.6 | Dishonest age rating |
  | 2.3.7 | Keyword stuffing: trademarks, competitor names, pricing, irrelevant terms |
  | 2.3.8 | Metadata (icons/screenshots/previews) not appropriate for a 4+ rating |
  | 2.3.9 | Using materials without rights, or real person data instead of fictional |
  | 2.3.10 | Other platform names/imagery in metadata |
  | 2.3.11 | Pre-order app materially different from what was advertised |
  | 2.3.12 | Generic "What's New" for a significant change |
  | 2.3.13 | Inaccurate In-App Event metadata or timing |

Sources:
- https://developer.apple.com/distribute/app-review/
- https://developer.apple.com/app-store/review/guidelines/

## Getting Featured by Apple

- Submit significant updates and campaigns through Featuring Nominations.
- Give Apple at least two weeks' notice.
- Submit up to three months in advance for broader consideration.
- Nominate major updates, seasonal campaigns, and fitness challenges.
- Highlight WeStretch's animated personalization.
- Highlight the physiotherapist-informed stretch library.
- Emphasize accessibility, older adults, and multilingual availability.
- Explain how WeStretch helps people remain active and mobile.
- Ensure screenshots, ratings, onboarding, and app quality are polished.
- Prepare promotional artwork in case Apple requests it.
- **[2026-08-21]** Apple's own stated evaluation criteria (strengthen these
  specifically before nominating): user experience, UI design, innovation,
  uniqueness vs. competitors, accessibility, localization quality, and
  App Store product page quality (screenshots/previews/description/ratings).
- **[2026-09-01]** In-App Events are now explicitly one of the nominate-able
  content types (alongside new apps, significant updates, and "great
  stories") and can themselves be featured on Today/Games/Apps tabs, in
  search results, and on product pages, directly relevant now that
  WeStretch has a drafted In-App Event ("7-Day Mobility Challenge," see
  `../Output/2026-08-29-in-app-event-7-day-mobility-challenge.md`).
- **[2026-09-01]** Other featuring mechanisms worth knowing about beyond a
  Featuring Nomination: App/Game of the Day (Apple's own daily pick),
  themed Lists on the Today tab, Personalized recommendations (algorithmic,
  not nominated), and the Editors' Choice badge (a distinct curated award
  with its own badge shown on the product page).
- **[2026-09-01]** Eligibility isn't restricted by app category, no need to
  read prior guidance as fitness-specific.

Source: https://developer.apple.com/app-store/getting-featured/

## Highest-Priority Actions for WeStretch

1. Confirm enrollment in Apple's 15% Small Business Program.
2. Enable Billing Grace Period and subscription-status notifications.
3. Optimize the first three screenshots and run App Store A/B tests.
4. Create custom product pages for back pain, stiffness, mobility, golf, and pickleball.
5. Localize App Store assets for English, French, and Spanish.
6. Trigger native review prompts after successful routines or meaningful milestones.
7. Launch App Store fitness challenges as In-App Events.
8. Configure introductory, promotional, and win-back subscription offers.
9. Verify accessibility, account deletion, privacy disclosures, and subscription clarity.
10. Nominate meaningful updates and campaigns for Apple editorial featuring.

This priority list is the source for `../Backlog.md`'s seed items; see
that file for status/dates as each one gets worked.
