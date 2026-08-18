# CXO/CLAUDE.md

Scope: this folder is the CXO's isolated workspace — responsibilities, skills, and
memory specific to this role only. Read this file (and CXO/Memory.md) whenever
working here; cross-role conventions live in the repo root `CLAUDE.md`.

## Mandate

Customer journey audit, UX design review.

## Skills

- `CXO/skills/customer-journey-audit/`
- `CXO/skills/jokes/`
- `CXO/skills/ux-design-review/`
Each skill is scoped to a single decision or review task, not a general "be the
CXO" persona — invoke the specific skill that matches the task. New skills follow
the existing `SKILL.md` frontmatter pattern (`name`, `description` starting
with "Use when...") and a short structured output format. Note the repo-wide
skill-discovery caveat in the root `CLAUDE.md` / `CHATTY_REVIEW.md` — these
`skills/` files are read by convention/reference, not auto-invoked as slash
commands.

## Project pipeline

- `Ideas/` — early-stage CXO concepts, not yet started.
- `In Progress/` — active CXO initiatives. Each gets its own subfolder with its
  own `CLAUDE.md` + `Memory.md` pair once real work begins.
- `Ready/` — finished/decided CXO initiatives, kept for reference.

## Memory

CXO/Memory.md holds durable facts, feedback, and context specific to this role.
Project-specific memory lives one level deeper, inside that project's own
`Memory.md`. See the root `CLAUDE.md` "Memory" section for the full model.
