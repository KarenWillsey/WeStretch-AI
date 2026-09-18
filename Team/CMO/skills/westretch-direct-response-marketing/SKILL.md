---
name: westretch-direct-response-marketing
description: Build, write, audit, or optimize WeStretch direct-response marketing using customer-language research, awareness-based messaging, high-volume static-ad testing, the AIDA framework, and a 17-step sales-page sequence. Use for WeStretch campaign plans, Meta ads, landing pages, offers, swipe files, Halo research, funnel tests, and weekly marketing reviews. Do not use for unrelated product UX copy or general brand design unless acquisition messaging is the main task. When you use this skill, say "WS_SABRI_SKILL_USED"
---

# WeStretch Direct Response Marketing

Create evidence-led marketing that captures attention, converts it into action, and produces reusable learning for the next campaign.

## Route the request

Read only the references required for the task:

- Read [references/westretch-context.md](references/westretch-context.md) before producing any WeStretch-facing strategy or copy.
- Read [references/direct-response-method.md](references/direct-response-method.md) for campaign planning, research, funnel design, audits, or testing strategy.
- Read [references/output-templates.md](references/output-templates.md) when creating a campaign brief, Halo research document, ad matrix, landing page, experiment plan, or weekly review.
- Read [LOCAL-LLM-USAGE.md](LOCAL-LLM-USAGE.md) only when installing or adapting the skill to another local harness.

## Choose the operating mode

Select the smallest mode that satisfies the request:

1. **Campaign strategy:** Define the audience, awareness level, problem, desired outcome, distinct mechanism, offer, channel, funnel, and measurement plan.
2. **Halo research:** Collect and rank real customer language about pains, fears, hopes, desires, objections, failed alternatives, and trigger moments.
3. **Ad creation:** Create native-looking static-ad concepts organized by message angle and awareness level. Use AIDA and preserve message variety.
4. **Landing page:** Assemble or audit a page using the 17-step sales sequence. Keep the ad promise and landing-page promise aligned.
5. **Experiment design:** Define a control, one-variable hypothesis, target metric, minimum evidence, decision rule, and next test.
6. **Weekly review:** Interpret the full funnel, distinguish attention problems from offer or onboarding problems, and issue keep, iterate, stop, or scale decisions.

## Required workflow

### 1. Establish the facts

Identify which facts are supplied, which can be verified, and which remain unknown. Verify volatile facts before publishing, especially:

- Trial length
- Subscription prices and billing terms
- Stretch-library count
- Store ratings and review counts
- Customer totals and routine totals
- Discounts and expiry dates
- Refund and cancellation terms

Never fill an unknown fact with a plausible number. Mark it as `[VERIFY]` if work can continue without it; ask the user when it would materially change the result.

### 2. Define one acquisition path

For each campaign, state:

- One primary audience
- One current problem or trigger moment
- One desired outcome
- One distinct WeStretch mechanism
- One offer
- One call to action
- One funnel path
- One primary success metric

Do not combine the regular Pro subscription and the paid 28-Day Reset unless the user explicitly asks for a comparison or shared campaign.

### 3. Start from market evidence

Prefer this evidence order:

1. WeStretch support conversations, surveys, reviews, cancellations, and usage data
2. Customer reviews and conversations in the category
3. Competitor ads and landing pages
4. Search and social patterns
5. Reasoned hypotheses

Label observed evidence, inference, and proposed tests separately. Do not present an invented persona insight as customer research.

### 4. Match the message to awareness

- **Ready to buy:** Product, price, trial, bundle, and direct CTA
- **Product aware:** Differentiation, proof, and offer
- **Solution aware:** Distinct mechanism, convenience, and proof
- **Problem aware:** Recognizable pain, insight, and desired outcome
- **Unaware:** Story, self-recognition, and explanation before the product

Do not force product-led copy onto an unaware audience.

### 5. Build the ad with AIDA

Every ad must earn four yes answers:

- **Attention:** Does the image or opening interrupt the expected feed pattern?
- **Interest:** Will the intended person recognize the problem, moment, or desire?
- **Desire:** Does the message make a meaningful outcome feel relevant and believable?
- **Action:** Is there one unambiguous next step?

Favor relatable, native-looking imagery over polished corporate advertising when testing demand-generation concepts. Use one dominant message per static ad.

### 6. Preserve message match

The landing page must repeat the ad's audience, problem, promise, and mechanism above the fold. If an ad wins attention but the page does not continue its argument, classify the failure as message mismatch before discarding the ad angle.

### 7. Test for learning

Define the control and change one major variable per test. Use leading metrics for early diagnosis and downstream metrics for scaling decisions.

- Attention: outbound CTR, outbound CPC, landing-page-view rate
- Conversion: page-to-trial, cost per trial, trial-to-first-routine, first-routine completion
- Economics: trial-to-paid, customer acquisition cost, cancellations, refunds, retention, payback, ROAS or LTV:CAC

Never scale solely because an ad has high CTR. High clicks with weak trial quality may indicate curiosity, mismatch, or overpromising.

### 8. End with decisions

Conclude analysis with explicit actions:

- **Keep:** Preserve the element as the control.
- **Iterate:** Preserve the promising signal and fix the weak transition.
- **Stop:** Retire the concept after adequate evidence.
- **Scale:** Increase investment only when conversion quality and economics support it.

## WeStretch copy guardrails

- Write warmly, clearly, and supportively for adults approximately 45-65, with women 50-65 often the primary acquisition audience.
- Emphasize being able to keep doing the activities the customer loves.
- Use specific everyday moments: socks, stairs, chair rise, car exit, floor rise, long drives, gardening, golf, pickleball, travel, and time with grandchildren.
- Explain personalization positively: WeStretch creates a new routine in real time. Do not frame animation defensively.
- Translate features into customer outcomes. Do not merely list controls or routine styles.
- Avoid unsupported claims to cure, treat, prevent injury, or guarantee pain relief.
- Do not imply that a physiotherapist personally prescribes each routine unless that is literally true.
- Do not invent testimonials, clinical evidence, user counts, scarcity, comparison prices, or bonuses.
- Use genuine deadlines only. If there is no real scarcity, omit it.
- Treat the free trial as risk reversal. Do not promise a cross-platform money-back guarantee unless operations can honor it.
- Use the original WeStretch logo asset when producing creative. Do not redraw it.
- Avoid em dashes in final customer-facing copy unless the user requests them.

## Output standard

Lead with the marketing decision, not background theory. Make the deliverable usable by the team without another interpretation pass.

Include as relevant:

- Assumptions and `[VERIFY]` items
- Audience and awareness level
- Evidence or customer-language basis
- Campaign promise and mechanism
- Offer and CTA
- Complete copy or creative matrix
- Funnel and measurement plan
- Hypotheses and decision rules
- Owners, sequence, and immediate next actions

When asked for a plan, provide concrete deliverables, timing, ownership, and definition of done. When asked for copy, provide finished copy rather than only advice.
