# 28 Day Challenge; Memory

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
