---
name: reengagement-email-copy
description: Verify and improve WeStretch re-engagement/win-back email funnel copy (the day 7/11/16/23/30 sequences sent after a lapsed stretch, across interchangeable Flows 1-3) against the Voice & Approach rules, graded through Chase, Expert, and Marg every loop. Use whenever writing, auditing, or revising re-engagement or win-back email copy for WeStretch. Depends on the westretch-core skill, load and apply its personas and guardrails first. Output markdown only.
---

# WeStretch Re-Engagement Email Copy

Turns a re-engagement email flow (existing draft or new) into verified, on-voice copy, graded through the WeStretch personas every loop.

## Before you start
1. Load **westretch-core** and apply Marg, Expert, Chase, the Strategic Thesis, the honesty guardrail, and the grading loop (`grading-and-loop.md`). Everything here runs inside those rules.
2. Read `../../WeStretch Re-Engagement Emails - Voice & Approach.md`, the email-specific voice rules and the 3-flow theme table. This is a specialization layer on top of westretch-core: where it is more specific than the general rubric (the five-minute anchor, the no-downside rule, the exact template details), follow it.

## The process (touch all three personas every loop, never just Expert x Marg)
1. **Chase** sets or confirms the influence strategy for the sequence and for each day-slot: the FATE lever (identity anchor: "someone who takes care of how I move"), the Six-Axis read for that day (readiness rises from day 7 to day 30), and whether each email's angle still matches its assigned theme in the flow table. Chase also flags strategic drift, e.g. an email that has quietly wandered from its intended theme into another slot's territory.
2. **Marg** grades every email in the set on the 5-dimension rubric (`grading-and-loop.md`), reacting as the ICP user, and applies the Voice & Approach "Before it goes out" checklist as an extra pass: obviously-true opener, one idea, easier not harder, calm-friend not coach, no guilt/downside/fitness language.
3. **Expert** rewrites only what Marg (or Chase's drift flag) flagged, diagnoses *why* it broke, and repairs it without breaking the honesty guardrail.
4. Repeat (Chase confirms the fix still fits strategy, Marg re-grades) until the set hits the A-average target or a named honest ceiling, per `grading-and-loop.md`.

## Format rules specific to this asset
- Template per email: `Subject:` / `Preview:` / `Hi {{first_name | default:"there"}},` body / `[Start today's routine]` CTA / `The WeStretch Team` sign-off (no dash). Do not vary these mechanics between emails or flows.
- One idea per email, start to finish. No em dashes anywhere (also a westretch-core rule).
- Each flow must give every day-slot a genuinely distinct angle from the same slot in the other flows (see the theme table in the Voice & Approach doc). If two flows converge on the same idea for a slot, that is a real defect (Expert's "kill repetition across a series"), not a style nitpick, even if the piece individually clears the grade bar.
- The CTA is deliberately soft by design (Voice & Approach: "ask for less, not more"). Do not chase an A+ on the Act dimension by pushing the ask harder; a soft-ceiling Act score on a win-back email is a feature, name it as an honest ceiling rather than forcing it.
- Guardrail note specific to this asset: late-sequence emails (day 23, day 30) are the ones most likely to drift into stakes/decline framing ("if you don't keep this up...", aging-as-threat) because they reach for a bigger, longer-term reason to return. Read every long-horizon email specifically against "never exploit anxiety about aging, decline, or dependence" before passing it.

## Output
Markdown only, in the deliverable format from `grading-and-loop.md` (steps-run line, Chase's strategy note, per-loop grade table, final copy, appendix with honest ceilings and any structural findings). Save the deliverable under `../../Output/`. Do not overwrite the source instruction files; they are the canonical input.
