# 28 Day Challenge; Memory

## 2026-10-05: everyday-frustration Meta static plan

- Karen requested a plan using the supplied Meta expert's three concepts and `westretch-core`, then an explicit pause before production.
- Plan: `meta-static-ad-plan.md`. Recommended first batch is three concepts in three sizes, nine images. Two follow-up challengers are conditional on results, not part of the initial build.
- Core strategy/copy review completed with one revision cycle and two grading passes. Proposed wording remains unapproved. No images, renderer, campaign or paid generation created.
- Resolved on Karen's subsequent "please proceed": plan/copy and photo directions approved for production, with all new photography required to use CMO female-actor or male-actor skills. Nine PNGs are now in `Static Ads/Output/`; see `Static Ads/README.md`. R02 was inspected, Work Sans Bold obtained and verified, and R03 generated with Male Actor 02's canonical reference and skill.
- Open before launch: Meta expert to supply budget, target CPA, conversion event and audience; campaign owner to confirm dates, year, terms and destination. Existing landing-page approval, checkout and confirmation work remains open. Detailed Meta safe-zone/policy pages were login/rate-limit blocked, so verify in Ads Manager before launch.
- Production is complete. Karen's review of the finished ads and new R03 source remains open. Launch dependencies above remain open and are also recorded in `WORK-TRACKER.md`. No campaign launched.

No durable decisions recorded yet. The review in this folder is a first pass;
once Karen signs off on which rewritten sections to keep, log standing
decisions here (e.g. if the physio-informed FAQ addition or the How It Works
rewrite gets approved as final, or if any of it gets rejected and why).

## 2026-09-23: landing page built, pending sign-off

Built `/28-day-reset/` in the website-repo using the Final Copy in this
folder (not the slightly earlier draft copy that circulated separately),
so the added safety FAQ and the physio-informed clauses in "What if"/How It
Works/pricing subhead are already live in the built page, not just this
review doc. If Karen rejects any of those specific rewrites on review, both
this folder's Final Copy and the live `.astro` file need updating together,
they're no longer two independent things once the page exists.

No campaign-specific Stripe Payment Link was ever supplied for the 28-Day
Reset. The pricing strip reuses the site's real, existing Annual/Monthly
links (`src/data/site.ts` `pricingPlans`), same ones used on `/30-day.astro`
and the homepage. Flag if Karen wants challenge-specific checkout links
instead.

Confirmation Page copy in this folder's Final Copy was not built into a real
page this pass; treated as out of scope for the landing-page build task. See
`WORK-TRACKER.md` and this folder's `CLAUDE.md` for the open item.
