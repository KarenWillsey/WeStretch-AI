# Apple Opportunity Radar; Backlog

The nightly run takes the top not-done item, executes it, writes output to
`Output/`, and marks it done here with a date + link. See
`Implementation Spec.md` section 3 for the workflow and section 4 for how
this list gets seeded/grown.

## Not started

Seeded 2026-08-21 from `Knowledge Base/apple-marketing-opportunities.md`
"Highest-Priority Actions for WeStretch" (Karen-provided, sourced list,
supersedes the earlier generic seed list). Order preserved from that list;
re-prioritize here if the order needs to change.

Added 2026-08-21 by the first live monthly-refresh run (found via a real
developer.apple.com fetch, not invented; see Knowledge Base changelog):

(all items from this batch are now done; see the Done section below)

Added 2026-08-26 by the nightly-action run (found the App Store metadata
gap while working the localization item below):

- [ ] Draft English App Store product page metadata (name ≤30 chars, subtitle ≤30 chars, keyword field ≤100 chars, promotional text ≤170 chars, long-form description), prerequisite for localizing product page metadata into French and Spanish.

Added 2026-09-01 by the monthly-refresh run (found via real
developer.apple.com fetches; see Knowledge Base changelog):

- [ ] Configure the in-app purchase/subscription showcase on the product page (up to 20 items across IAPs + subscriptions, custom order, 35-char name / 55-char description each), new Apple feature, not yet used.
- [ ] Confirm whether WeStretch's app supports Dark Mode, and if so add at least one Dark-Mode screenshot to the product page.
- [ ] Fold privacy-manifest and SDK-signature verification into the existing ad/analytics SDK audit item; Apple is expanding software-supply-chain integrity requirements for third-party SDKs.
- [ ] Submit the drafted "7-Day Mobility Challenge" In-App Event (see Output/2026-08-29-in-app-event-7-day-mobility-challenge.md) for an Apple Featuring Nomination; In-App Events are now an explicitly nominate-able, featurable content type.
- [ ] Evaluate offering a monthly subscription with a 12-month commitment as an additional plan tier alongside the existing Monthly/Annual options, and confirm whether "streamlined purchasing" (completing a purchase from outside the app) should stay on or be turned off.

## Done

- [x] Confirm enrollment in Apple's Small Business Program (15% commission rate). (2026-08-21 (manual test run)) checklist: [Output/2026-08-21-small-business-program-checklist.md](Output/2026-08-21-small-business-program-checklist.md)
- [x] Enable Billing Grace Period and subscription-status notifications (App Store Server Notifications). (2026-08-21 (first scheduled run)) checklist: [Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md](Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md)
- [x] Optimize the first three screenshots and set up a Product Page Optimization (A/B) test. (2026-08-22 (scheduled run)) plan: [Output/2026-08-22-ppo-test-first-3-screenshots.md](Output/2026-08-22-ppo-test-first-3-screenshots.md)
- [x] Create Custom Product Pages for back pain, stiffness, mobility, golf, and pickleball. (2026-08-23 (scheduled run)) plan: [Output/2026-08-23-cpp-plan-5-pages.md](Output/2026-08-23-cpp-plan-5-pages.md)
- [x] Localize App Store assets for English, French, and Spanish. 2026-08-26 (scheduled run): scoped to existing screenshot/video copy only (product page metadata doesn't exist in English yet (see new backlog item above): [Output/2026-08-26-localize-app-store-assets-fr-es.md](Output/2026-08-26-localize-app-store-assets-fr-es.md)
- [x] Wire up native rating prompts after positive moments (completed routines, streak milestones), respecting the 3-prompts/365-day cap. (2026-08-28 (scheduled run)) implementation plan: [Output/2026-08-28-native-rating-prompts-plan.md](Output/2026-08-28-native-rating-prompts-plan.md)
- [x] Launch an App Store In-App Event fitness challenge (e.g. "7-Day Mobility Challenge"). (2026-08-29 (scheduled run)) draft: [Output/2026-08-29-in-app-event-7-day-mobility-challenge.md](Output/2026-08-29-in-app-event-7-day-mobility-challenge.md)
- [x] Configure introductory, promotional, and win-back subscription offers. (2026-08-30 (scheduled run)) checklist: [Output/2026-08-30-subscription-offers-config-checklist.md](Output/2026-08-30-subscription-offers-config-checklist.md)
- [x] Verify accessibility, account deletion, privacy disclosures, and subscription-clarity requirements are met. (2026-08-31 (scheduled run)) checklist: [Output/2026-08-31-accessibility-privacy-subscription-clarity-checklist.md](Output/2026-08-31-accessibility-privacy-subscription-clarity-checklist.md)
- [x] Draft an Apple Featuring Nomination for a meaningful upcoming update or seasonal campaign. (2026-09-01 (scheduled run)) pitch copy for the "7-Day Mobility Challenge" In-App Event: [Output/2026-09-01-featuring-nomination-draft.md](Output/2026-09-01-featuring-nomination-draft.md)
- [x] Confirm WeStretch's minimum iOS/iPadOS deployment target supports iOS 18+ before committing to deep-linked Custom Product Pages. (2026-09-03 (scheduled run)) this skill has no access to the native app's build config, so it produced a checklist for whoever does have that access, rather than a confirmed answer: [Output/2026-09-03-ios-18-deployment-target-checklist.md](Output/2026-09-03-ios-18-deployment-target-checklist.md)
- [x] Get reviewer permission before quoting any App Store review in marketing materials; Apple requires explicit reviewer consent for this. (2026-09-02 (scheduled run)) standing process: [Output/2026-09-02-reviewer-permission-process-for-quoting-reviews.md](Output/2026-09-02-reviewer-permission-process-for-quoting-reviews.md) (this Done line was missing until the 2026-09-05 run added it; the item had been dropped from "Not started" without being recorded here)
- [x] Audit current ad/analytics SDKs against Apple's device-fingerprinting prohibition (Developer Program License Agreement), flag any SDK deriving identifiers from browser/device/location/network properties. (2026-09-04 (scheduled run)) this skill has no access to the production app's dependency manifest, so it produced a checklist for whoever does have that access: [Output/2026-09-04-ad-analytics-sdk-fingerprinting-audit-checklist.md](Output/2026-09-04-ad-analytics-sdk-fingerprinting-audit-checklist.md)
- [x] Evaluate whether Apple's EU alternative business terms (10% commission) change WeStretch's economics, if EU is a meaningful subscriber market. (2026-09-05 (scheduled run)) answered: **no**, and the premise is obsolete; the EU Alternative Terms Addendum is discontinued and unified EU terms take effect 2026-10-01, under which a Small Business Program member pays 15% via Apple IAP in the EU, same as everywhere else. Carry-forward: an Account Holder needs to check for a pending updated Developer Program License Agreement before 2026-10-01. [Output/2026-09-05-eu-business-terms-economics-evaluation.md](Output/2026-09-05-eu-business-terms-economics-evaluation.md)
