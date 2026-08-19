# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository contains no application source code, build system, test suite, or lint config. Per the README:

> WeStretch is a fitness app. This project will be used as the global overview from a business view.

This repo models WeStretch's business/org structure as Claude Code skills rather than as application code. When application code is eventually added, update this file with the actual build/lint/test commands and architecture notes at that point — do not invent them ahead of time.

## The Manager (this level) and the Team (`Team/`)

This root — the repo top level, this `CLAUDE.md` — is **the Manager**: the orchestrator/delegator. It doesn't do officer-specific work itself. When Karen says "tell the Manager to do X," the job is to read the request, figure out which officer(s) under `Team/` have the relevant skills/mandate, and delegate to their `CLAUDE.md` + `skills/` (routing to multiple officers and synthesizing their output when a request is genuinely cross-functional — see "Cross-functional feature planning" below).

All 11 C-suite officer folders — WeStretch's org chart (WeStretch → CEO → 10 direct reports) — live under `Team/`, one top-level folder per officer, isolated so each officer's responsibilities, memory, and conventions don't bleed into another's:

| Role | Mandate | Details |
|---|---|---|
| `Team/CEO/` | Karen's own operational hub — daily brief, personal ideas/initiatives | [Team/CEO/CLAUDE.md](Team/CEO/CLAUDE.md) |
| `Team/CTO/` | Technical architecture review, engineering roadmap | [Team/CTO/CLAUDE.md](Team/CTO/CLAUDE.md) |
| `Team/CXO/` | Customer journey audit, UX design review | [Team/CXO/CLAUDE.md](Team/CXO/CLAUDE.md) |
| `Team/CRO/` | Revenue pipeline review, pricing strategy | [Team/CRO/CLAUDE.md](Team/CRO/CLAUDE.md) |
| `Team/COO/` | Ops process audit, cross-team execution planning | [Team/COO/CLAUDE.md](Team/COO/CLAUDE.md) |
| `Team/CIO/` | Data systems audit, data governance review | [Team/CIO/CLAUDE.md](Team/CIO/CLAUDE.md) |
| `Team/CHRO/` | Hiring plan, org/culture review | [Team/CHRO/CLAUDE.md](Team/CHRO/CLAUDE.md) |
| `Team/CFO/` | Financial model review, budget planning | [Team/CFO/CLAUDE.md](Team/CFO/CLAUDE.md) |
| `Team/CMO/` | Brand, marketing, App Store assets and copy | [Team/CMO/CLAUDE.md](Team/CMO/CLAUDE.md) |
| `Team/CPO/` | Roadmap prioritization, user research synthesis | [Team/CPO/CLAUDE.md](Team/CPO/CLAUDE.md) |
| `Team/CGO/` | Growth experiment design, retention funnel analysis | [Team/CGO/CLAUDE.md](Team/CGO/CLAUDE.md) |

### Per-role structure (consistent across all 11 folders under `Team/`)

```
Team/ROLE/
  CLAUDE.md         # this role's scope + conventions — read at the start of any work in this folder
  Memory.md         # this role's persistent memory (facts/feedback/context specific to this role)
  skills/           # Claude Code Skills (SKILL.md files) scoped to this role's tasks
  Ideas/            # early-stage concepts, not yet started
  In Progress/      # active initiatives — each gets its own subfolder
  Ready/            # finished/decided initiatives, kept for reference
```

Each real project inside `Ideas/`, `In Progress/`, or `Ready/` (e.g. `Team/CMO/In Progress/App Store/App Store Image Creation/`) gets its own `CLAUDE.md` (what this project is, how to work on it) + `Memory.md` (durable decisions, calibrated values, standing rules for that project only) pair, the same way roles do. Claude Code auto-loads nested `CLAUDE.md` files as you work within a subtree, so these are picked up automatically — no manual pointer needed. Empty `Ideas/In Progress/Ready` folders just hold a `README.md` explaining their purpose until a real project starts there.

Each skill is scoped to a single decision or review task for that function (e.g. `Team/CFO/skills/budget-planning`), not a general-purpose "be the CFO" persona — invoke the specific skill that matches the task at hand. When adding a new skill, follow the existing `SKILL.md` frontmatter pattern (`name`, `description` starting with "Use when...") and keep the body to a short, structured output format rather than open-ended prose.

**Known issue:** Claude Code only auto-discovers project *skills* under `.claude/skills/<skill>/SKILL.md`. `Team/ROLE/skills/...` files live outside that path, so they are not automatically invokable as slash-command skills — they're read and applied by convention/reference (e.g. by an agent explicitly told to read a given `SKILL.md`). This does **not** apply to `CLAUDE.md` files: those nest and auto-load normally, which is why the per-role/per-project `CLAUDE.md` structure above works without extra plumbing.

**Third-party skill packages (e.g. Higgsfield, `coreyhaines31/marketingskills`):** installed skills live in `.agents/skills/<skill-name>/` — the cross-agent standard location (`.agents/`) referenced by the Agent Skills spec, used because it's the canonical home both Claude Code and other agent tools (Codex, Cursor, etc.) can share. `.claude/skills/<skill-name>` is a Windows NTFS directory **junction** (`mklink /J`, no admin required) pointing at the real folder under `.agents/skills/`, so Claude Code's auto-discovery sees the files without duplicating them. Junctions are local filesystem state, not git objects — git only tracks the real content under `.agents/skills/`, so a fresh clone needs the junctions recreated (`mklink /J .claude\skills\<name> .agents\skills\<name>` per skill) before those skills are invokable as slash commands on that machine.

## Cross-functional feature planning: `Team/CPO/Ideas/Features/`

`Team/CPO/Ideas/Features/<feature-name>/` holds multi-role planning docs for a proposed product feature, e.g. `multiplayer-stretches/` and `1000-dau-growth-plan/`. It lives under CPO because a not-yet-started feature is a roadmap idea — CPO's mandate — even though building it out means pulling in other roles. Pattern per feature folder:

- `README.md` — what the feature is, why it matters, and a table mapping each role doc to the skill used to produce it.
- One doc per role (`cto.md`, `cmo.md`, `cfo.md`, ...) — that role's output from applying its skill(s) to the feature.
- `synthesis.md` — cross-role summary: where roles agree, open questions, and the recommended next step. Read this first; it's the entry point into the folder.

When asked to plan a new feature across the org, follow this same structure rather than inventing a new one. Once a feature moves from concept to active build, move its folder into `Team/CPO/In Progress/` (or the most relevant owning role), same as any other project.

## Memory

Memory is distributed to match the folder it's about — read the file(s) relevant to what you're working on, not just this one:

- **`Memory.md`** (repo root, this level) — only facts that are truly cross-role: general Karen workflow preferences, org-wide decisions, anything not specific to one officer's work. Always read this at the start of any work in the repo.
- **`Team/ROLE/Memory.md`** — facts, feedback, and context specific to that one role. Read it whenever working inside that role's folder.
- **`Team/ROLE/.../ProjectName/Memory.md`** — facts specific to that one project only (calibrated values, standing decisions, session learnings). Read it whenever working inside that project's folder.

Write new durable facts into the most specific file that's still true after this session ends — a project-specific decision goes in that project's `Memory.md`, not the role's or root's. Do not use the external per-user auto-memory store for this project; everything relevant lives in these checked-in files so it travels with the repo and is visible to anyone working in it.
