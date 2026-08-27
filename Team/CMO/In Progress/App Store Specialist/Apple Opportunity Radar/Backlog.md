# Apple Opportunity Radar — Backlog

The nightly run takes the top not-done item, executes it, writes output to
`Output/`, and marks it done here with a date + link. See
`Implementation Spec.md` section 3 for the workflow and section 4 for how
this list gets seeded/grown.

## Not started

Seeded 2026-08-21 from `Knowledge Base/apple-marketing-opportunities.md`
"Highest-Priority Actions for WeStretch" (Karen-provided, sourced list —
supersedes the earlier generic seed list). Order preserved from that list;
re-prioritize here if the order needs to change.

- [ ] Wire up native rating prompts after positive moments (completed routines, streak milestones) — respecting the 3-prompts/365-day cap.
- [ ] Launch an App Store In-App Event fitness challenge (e.g. "7-Day Mobility Challenge").
- [ ] Configure introductory, promotional, and win-back subscription offers.
- [ ] Verify accessibility, account deletion, privacy disclosures, and subscription-clarity requirements are met.
- [ ] Draft an Apple Featuring Nomination for a meaningful upcoming update or seasonal campaign.

Added 2026-08-21 by the first live monthly-refresh run (found via a real
developer.apple.com fetch, not invented — see Knowledge Base changelog):

- [ ] Get reviewer permission before quoting any App Store review in marketing materials — Apple requires explicit reviewer consent for this.
- [ ] Confirm WeStretch's minimum iOS/iPadOS deployment target supports iOS 18+ before committing to deep-linked Custom Product Pages.
- [ ] Audit current ad/analytics SDKs against Apple's device-fingerprinting prohibition (Developer Program License Agreement) — flag any SDK deriving identifiers from browser/device/location/network properties.
- [ ] Evaluate whether Apple's EU alternative business terms (10% commission) change WeStretch's economics, if EU is a meaningful subscriber market.

Added 2026-08-26 by the nightly-action run (found the App Store metadata
gap while working the localization item below):

- [ ] Draft English App Store product page metadata (name ≤30 chars, subtitle ≤30 chars, keyword field ≤100 chars, promotional text ≤170 chars, long-form description) — prerequisite for localizing product page metadata into French and Spanish.

## Done

- [x] Confirm enrollment in Apple's Small Business Program (15% commission rate). — 2026-08-21 (manual test run) — checklist: [Output/2026-08-21-small-business-program-checklist.md](Output/2026-08-21-small-business-program-checklist.md)
- [x] Enable Billing Grace Period and subscription-status notifications (App Store Server Notifications). — 2026-08-21 (first scheduled run) — checklist: [Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md](Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md)
- [x] Optimize the first three screenshots and set up a Product Page Optimization (A/B) test. — 2026-08-22 (scheduled run) — plan: [Output/2026-08-22-ppo-test-first-3-screenshots.md](Output/2026-08-22-ppo-test-first-3-screenshots.md)
- [x] Create Custom Product Pages for back pain, stiffness, mobility, golf, and pickleball. — 2026-08-23 (scheduled run) — plan: [Output/2026-08-23-cpp-plan-5-pages.md](Output/2026-08-23-cpp-plan-5-pages.md)
- [x] Localize App Store assets for English, French, and Spanish. — 2026-08-26 (scheduled run) — scoped to existing screenshot/video copy only (product page metadata doesn't exist in English yet — see new backlog item above): [Output/2026-08-26-localize-app-store-assets-fr-es.md](Output/2026-08-26-localize-app-store-assets-fr-es.md)
