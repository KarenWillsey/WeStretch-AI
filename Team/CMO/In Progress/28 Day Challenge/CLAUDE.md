# 28 Day Challenge; CLAUDE.md

Scope: copy review for the WeStretch 28-Day Reset Challenge landing page,
subscription screen, and confirmation page. Read `Memory.md` alongside this
file before revising this copy further.

## Where things live

- `WeStretch Challenge Landing Page (Original).pdf`: the source draft as
  handed to CMO, unedited. Kept for comparison, don't overwrite it.
- `28-Day Reset Challenge Landing Page Review.md`: the Marg x Chase x Expert
  review of that draft (`westretch-core` skill), plus a CRO/copywriting pass
  (`cro` and `copywriting` skills). Contains the grading loop, the honest
  ceilings, and the specific rewritten sections (Reveal, How It Works, a new
  safety FAQ, the subscription subhead, the benefits checklist).
- `28-Day Reset Challenge Landing Page (Final Copy).md`: the complete page,
  read top to bottom, with every approved change folded into place. This is
  the one to hand off or read straight through; the review file above is the
  reasoning/grading behind it, not something you need to assemble yourself.

## Status

Review complete (2026-09-21), landed at an A- average (3.75), up from 3.50 on
the original draft. The final copy file has the full assembled page.

Built into a real page 2026-09-23: `Team/CMO/Ready/website-repo/src/pages/28-day-reset.astro`
(route `/28-day-reset/`), implementing the Final Copy above (including its
added safety FAQ). No sitewide header on this page, footer stays, every CTA
anchors to this page's own `#pricing` strip (reuses the homepage's dark
two-card Annual/Monthly layout). Three new actor images generated for it
(hero + morning-stiffness + payoff) live in `public/images/` on the site and
as reviewed copies in `Team/CMO/Review ToDo/`, pending Karen's sign-off.
Lighthouse (scoped): performance 99, accessibility 100, best-practices 100,
seo 100. Not yet deployed or committed, that's Karen's call. The PDF's
"Confirmation Page" copy above was not built this pass; the existing
`ThankYouContent.astro` / `thank-you-yearly.astro` covers download/login
generically but has no Reset-specific wording, flagged as an open item in
`WORK-TRACKER.md`.
