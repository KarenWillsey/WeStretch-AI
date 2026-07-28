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
- `CMO/skills/` — campaign planning, brand messaging review
- `CPO/skills/` — roadmap prioritization, user research synthesis
- `CGO/skills/` — growth experiment design, retention funnel analysis

Each skill is scoped to a single decision or review task for that function (e.g. `CFO/skills/budget-planning`), not a general-purpose "be the CFO" persona — invoke the specific skill that matches the task at hand. When adding a new skill, follow the existing `SKILL.md` frontmatter pattern (`name`, `description` starting with "Use when...") and keep the body to a short, structured output format rather than open-ended prose.

When all the roles are "talking" they must use `ToneManager/Karen.md`