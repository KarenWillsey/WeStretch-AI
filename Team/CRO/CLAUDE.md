# Team/CRO/CLAUDE.md

Scope: this folder is the CRO's isolated workspace, responsibilities, skills, and
memory specific to this role only. Read this file (and Team/CRO/Memory.md) whenever
working here; cross-role conventions live in the repo root `CLAUDE.md`.

## Mandate

Revenue pipeline review, pricing strategy.

## Skills

- `Team/CRO/skills/jokes/`
- `Team/CRO/skills/pricing-strategy/`
- `Team/CRO/skills/revenue-pipeline-review/`
Each skill is scoped to a single decision or review task, not a general "be the
CRO" persona; invoke the specific skill that matches the task. New skills follow
the existing `SKILL.md` frontmatter pattern (`name`, `description` starting
with "Use when...") and a short structured output format. Note the repo-wide
skill-discovery caveat in the root `CLAUDE.md`; these
`skills/` files are read by convention/reference, not auto-invoked as slash
commands.

## Project pipeline

- `Ideas/`: early-stage CRO concepts, not yet started.
- `In Progress/`: active CRO initiatives. Each gets its own subfolder with its
  own `CLAUDE.md` + `Memory.md` pair once real work begins.
- `Ready/`: finished/decided CRO initiatives, kept for reference.

## Memory

Team/CRO/Memory.md holds durable facts, feedback, and context specific to this role.
Project-specific memory lives one level deeper, inside that project's own
`Memory.md`. See the root `CLAUDE.md` "Memory" section for the full model.
