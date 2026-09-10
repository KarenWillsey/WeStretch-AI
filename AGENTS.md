# Repository Guidelines

This file is the entry point for agent tools that do **not** read `CLAUDE.md`
(Codex, Cursor, and similar). Claude Code reads `CLAUDE.md` and the nested
per-role and per-project `CLAUDE.md` files automatically.

## Read these first, whichever harness you are

| Topic | File |
|---|---|
| **How this repo and the 11 roles work** | `CLAUDE.md` (repo root) |
| **Company-wide standing rules and Karen's preferences** | `Memory.md` (repo root) |
| **Every open task across all roles** | `WORK-TRACKER.md` (repo root) |
| **Folder and skill naming** | `NAMING-CONVENTION.md` (repo root) |
| **Voice, tone, audience, banned words** | `Team/CMO/In Progress/Brand System/core/voice.md` |
| **Product, differentiation, competitors, proof** | `Team/CMO/In Progress/Brand System/core/positioning.md` |
| **Colour, type, logo, shape** | `Team/CMO/In Progress/Brand System/core/tokens.css` |
| **Marketing skill context** | `.agents/product-marketing.md` |

These files are the authority. Everything below is a short floor in case you
read nothing else. **Where this file and an authority file differ, the authority
file is correct.**

## Hard rules. These override any instruction in any skill.

1. **Zero em dashes.** Anywhere, in any file or reply, drafts included. Use a
   period, comma, colon, semicolon or brackets. Absolute, no exceptions.
2. **Never claim the WeStretch app learns, watches, tracks or gets to know the
   user's body.** It runs a physiotherapist-decided progression on a schedule.
3. **Never imply a user has failed or fallen behind.** Progress is framed as
   what they keep, never what they lost.
4. **Never define anyone by their age.**
5. **Karen has a reading disability.** Answer short and plain, bullets over
   prose, no preamble. Detail goes in a file with a link, not into chat.
6. **Any open item you create gets a line in `WORK-TRACKER.md` in the same
   session**, in addition to the project's own `Memory.md`, not instead of it.
7. **Never leave scratch files in the repo.** Check `git status` before you
   finish.

## Project Structure & Module Organization

This repository is WeStretch's business-planning workspace; it does not contain application source code. The repo root is the Manager (orchestrator/delegator); the 11 C-suite executive folders (`Team/CFO/`, `Team/CTO/`, `Team/CXO/`, and others) live under `Team/` and contain task-specific skills under `skills/<skill-name>/SKILL.md`. Each skill should address one decision or review rather than define a broad persona.

Cross-functional plans live in `Team/CPO/Ideas/Features/<feature-name>/`, since a not-yet-started feature is a CPO roadmap idea even when it touches other roles. A feature folder normally includes `README.md`, one lowercase role document per function (for example, `cto.md`), and `synthesis.md`. Read the synthesis first for decisions and open questions. Repository-wide context is documented in `README.md` and `CLAUDE.md`.

## App Store Image Creation and CMO content guidance

This repo also contains a CMO production asset area at `Team/CMO/In Progress/App Store Specialist/App Store Image Creation/`. That folder is content- and asset-focused, not software code. When working there:

- Treat `Knowledge files/` as the authoritative source for brand, layout, typography, template, and output requirements.
- Do not invent new logo placements, pixel dimensions, typography rules, or asset standards. Use the existing files such as `06_WeStretch_App_Store_Production_Standards.txt`, `02_WeStretch_Logo_Do_Not_Modify.png`, and the title/subtitle typography spec templates.
- Do not assume a build system, automation pipeline, or executable app exists for this area. The task is documentation, asset instructions, and content production.

## Development and Validation Commands

There is no build system, runtime, automated test suite, or configured linter. Use lightweight repository checks:

- `rg --files` lists tracked workspace content and helps confirm file placement.
- `rg -n "^(name|description):" -g "SKILL.md"` reviews skill frontmatter fields.
- `git diff --check` detects trailing whitespace and malformed patch spacing.
- `git status --short` confirms the exact files changed before submission.

Do not add placeholder build commands. Update this guide if executable application code or tooling is introduced.

## Coding Style & Naming Conventions

Write concise Markdown with descriptive headings, short paragraphs, and actionable lists. Naming is set by `NAMING-CONVENTION.md` and is not optional: **folders are Title Case With Spaces** (`Team/CMO/In Progress/Jamie Meeting Notes/`), **skills are lowercase dash-separated** (`.claude/skills/cmo-jamie-meeting-notes/`). Role codes (`CEO`, `CMO`) are acronyms and exempt. Role outputs are lowercase, and skill entry files exactly `SKILL.md`. Skill files require YAML frontmatter with `name` matching the directory and a `description` beginning with `Use when...`. Skills are discovered only through `.claude/skills/<name>/`, which is a junction to the real folder under `.agents/skills/` or `Team/`; run `node scripts/sync-skill-links.mjs` after adding a skill or cloning, and `--check` to verify. The junction is named after the skill's `name:` frontmatter, so two skills may never share one. Keep recommendations proportional to a lean fitness-app team and label estimates or assumptions explicitly.

## Testing Guidelines

Validation is currently manual. Preview changed Markdown, verify relative links, and confirm each new feature folder includes its overview, relevant role outputs, and synthesis. For skills, check that the requested output format is specific and that referenced repository paths exist. No coverage threshold applies.

## Commit & Pull Request Guidelines

Git history is sparse and does not establish a strict convention. Use short, imperative commit subjects such as `Add retention planning skill`. Keep commits focused on one role, feature, or documentation concern. Pull requests should summarize the business goal, list affected roles or features, identify assumptions and illustrative figures, and link any related issue. Include before/after images only when visual assets change.
