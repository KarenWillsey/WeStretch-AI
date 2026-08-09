---
name: app-store-copy
description: Generate WeStretch Apple App Store product-page copy (the text for the screens and app-preview video, not the graphics) for a given goal or Custom Product Page (CPP) theme like pain relief, seniors, free, or a competitor-driven CPP. Produces Part 1, the opening app-preview VIDEO topics, a 6–8 screen, ~30-second title-card sequence graded per card via Chase then Expert then Marg with a card bank for A/B testing. And Part 2, the still-screen titles and optional subtitles for the remaining Apple screenshots. Use whenever writing or iterating App Store screenshot titles, app-preview video hook copy, screen subtitles, or a CPP for WeStretch, for any theme. Depends on the westretch-core skill, load and apply its personas and guardrails first. Output markdown by default; produce a .docx only if the user asks for a shareable document.
---

# WeStretch App Store Copy

Turns a **goal** (a CPP theme) into App Store copy, the text for the screens and the app-preview video, not the graphics (a separate design job handles those), in two parts, graded through the WeStretch personas.

## Before you start
1. Load **westretch-core** and apply Marg, Expert, Chase, the Strategic Thesis, the honesty guardrail, and the grading loop (`grading-and-loop.md`). Everything here runs inside those rules.
2. Read `references/store-rules-apple.md`, the Apple limits and banned claims. Copy must comply.
3. Read `references/output-format.md`, the exact markdown structure to return.

## The process (do all three, in order, every time. Never skip a step.)
1. **Chase** sets the influence strategy for the whole CPP: the FATE lever, the identity it builds, and the Six-Axis read for this theme and audience. Do this even when the copy seems obvious.
2. **Expert** writes and rewrites the copy to that strategy.
3. **Marg** grades every card and screen, and runs the loop to target.

Show each persona's work in the output, and open with the one-line confirmation that no step was skipped (see `references/output-format.md`).

## The input
A goal / CPP theme, e.g. "pain relief," "seniors," "free," or a competitor-driven CPP. If the goal isn't given, ask for it. The theme shapes the angle; the personas, thesis, and store rules never change.

## Part 1, the opening video topics
The first App Store asset is an app-preview video (~30 s). Treat it as a **6–8 screen title-card sequence** (each card held a few seconds).
1. **Chase** designs the hook strategy for the theme (identity / belonging / stakes-as-hope / authority / cost, pick what fits the theme, and consider offering variants for A/B).
2. **Expert** writes the card sequence.
3. **Marg** grades it **per card** (see per-card grading in `grading-and-loop.md`), the loop runs to target, and you produce a **card bank** (every card graded, with role tags) so cards can be A/B tested individually.
4. Note the honest ceiling and the strongest opener / closer / transplant cards.

**Format constraint:** each card is a **single title line, no subtitle**, **maximum 60 characters** (spaces and punctuation included). If a card cannot carry the idea honestly within 60 characters, cut the idea down rather than padding or running past the limit; flag it in the loop log instead of exceeding it.

Reminder: the Apple video must be **real in-app footage with the titles as caption overlays**, not a slideshow of text cards. State this so the design team builds it compliantly.

## Part 2, the still screens
The remaining Apple screenshots (up to 9 more, for 10 total incl. the video). For each screen: a **title** (**maximum 42 characters**) and an **optional subtitle** (**maximum 65 characters**), used only when the title needs the extra room. Run the Expert × Marg loop across the set, executing the Chase strategy set above; grade each screen; keep them distinct (no three screens making the same point); comply with the store rules. If a title or subtitle cannot carry the idea honestly within its limit, cut the idea down rather than padding or running past the limit; flag it in the loop log instead of exceeding it.

## Competitor-driven CPP goals
Competitor names may be used as **hidden ASO keywords / in ads**, never in visible on-screen title or subtitle text. For a competitor-driven CPP, focus the on-screen copy entirely on WeStretch's differentiators.

## Output
Markdown by default, in the structure from `references/output-format.md`. Produce a `.docx` only if the user asks for a shareable document; in that case use the standard **docx** skill to render the same content, and do not build a bespoke document script.

Never use em dashes in the copy or the document (this rule also comes from westretch-core). Use commas, periods, colons, or parentheses.
