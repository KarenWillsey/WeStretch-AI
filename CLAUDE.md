# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository contains no application source code, build system, test suite, or lint config. Per the README:

> WeStretch is a fitness app. This project will be used as the global overview from a business view.

This repo models WeStretch's business/org structure as Claude Code skills rather than as application code. When application code is eventually added, update this file with the actual build/lint/test commands and architecture notes at that point — do not invent them ahead of time.

## Structure: C-suite role skills

The repo is organized around WeStretch's C-suite org chart (WeStretch → CEO → 10 direct reports). Each role has its own top-level folder containing a `skills/` directory of Claude Code Skills (`SKILL.md` files) that let Claude act as that executive when invoked:

- `CTO/skills/` — technical architecture review, engineering roadmap
- `CXO/skills/` — customer journey audit, UX design review
- `CRO/skills/` — revenue pipeline review, pricing strategy
- `COO/skills/` — ops process audit, cross-team execution planning
- `CIO/skills/` — data systems audit, data governance review
- `CHRO/skills/` — hiring plan, org/culture review
- `CFO/skills/` — financial model review, budget planning
- `CMO/skills/` — currently empty (brand-messaging-review, campaign-planning, and jokes SKILL.md were deleted from the working tree; see `CMO/In Progress/` for the App Store image-creation work that replaced them). Restore or rewrite these before invoking CMO skills.
- `CPO/skills/` — roadmap prioritization, user research synthesis
- `CGO/skills/` — growth experiment design, retention funnel analysis

Every role except CMO also has a `skills/jokes/SKILL.md` — a role-flavored humor skill (e.g. CTO jokes about tech debt and Friday deploys), not a generic joke generator.

Each skill is scoped to a single decision or review task for that function (e.g. `CFO/skills/budget-planning`), not a general-purpose "be the CFO" persona — invoke the specific skill that matches the task at hand. When adding a new skill, follow the existing `SKILL.md` frontmatter pattern (`name`, `description` starting with "Use when...") and keep the body to a short, structured output format rather than open-ended prose.

**Known issue (see `CHATTY_REVIEW.md`):** Claude Code only auto-discovers project skills under `.claude/skills/<skill>/SKILL.md`. These `ROLE/skills/...` files live outside that path, so they are not automatically invokable as slash-command skills — they're read and applied by convention/reference (e.g. by an agent explicitly told to read a given `SKILL.md`). Treat that review as the current authoritative critique of this repo's structure; don't re-derive the same findings from scratch.

## Cross-functional feature planning: `Features/`

`Features/<feature-name>/` holds multi-role planning docs for a proposed product feature, e.g. `Features/multiplayer-stretches/` and `Features/1000-dau-growth-plan/`. Pattern per feature folder:

- `README.md` — what the feature is, why it matters, and a table mapping each role doc to the skill used to produce it.
- One doc per role (`cto.md`, `cmo.md`, `cfo.md`, ...) — that role's output from applying its skill(s) to the feature.
- `synthesis.md` — cross-role summary: where roles agree, open questions, and the recommended next step. Read this first; it's the entry point into the folder.

When asked to plan a new feature across the org, follow this same structure rather than inventing a new one.

## Tone

When multiple roles are "talking" together (e.g. in a synthesis doc or a multi-role conversation), tone must follow `ToneManager/Karen.md`. That file is currently empty — check it before relying on it, and flag to the user if it still has no content to follow.
