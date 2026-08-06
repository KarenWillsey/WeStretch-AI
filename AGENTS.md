# Repository Guidelines

## Project Structure & Module Organization

This repository is WeStretch's business-planning workspace; it does not contain application source code. Top-level executive folders (`CFO/`, `CTO/`, `CXO/`, and others) contain task-specific skills under `skills/<skill-name>/SKILL.md`. Each skill should address one decision or review rather than define a broad persona.

Cross-functional plans live in `Features/<feature-name>/`. A feature folder normally includes `README.md`, one lowercase role document per function (for example, `cto.md`), and `synthesis.md`. Read the synthesis first for decisions and open questions. Shared voice guidance belongs in `ToneManager/`, while repository-wide context is documented in `README.md`, `CLAUDE.md`, and `CHATTY_REVIEW.md`.

## Development and Validation Commands

There is no build system, runtime, automated test suite, or configured linter. Use lightweight repository checks:

- `rg --files` lists tracked workspace content and helps confirm file placement.
- `rg -n "^(name|description):" -g "SKILL.md"` reviews skill frontmatter fields.
- `git diff --check` detects trailing whitespace and malformed patch spacing.
- `git status --short` confirms the exact files changed before submission.

Do not add placeholder build commands. Update this guide if executable application code or tooling is introduced.

## Coding Style & Naming Conventions

Write concise Markdown with descriptive headings, short paragraphs, and actionable lists. Name role folders with uppercase abbreviations, feature and skill directories in kebab-case, role outputs in lowercase, and skill entry files exactly `SKILL.md`. Skill files require YAML frontmatter with `name` matching the directory and a `description` beginning with `Use when...`. Keep recommendations proportional to a lean fitness-app team and label estimates or assumptions explicitly.

## Testing Guidelines

Validation is currently manual. Preview changed Markdown, verify relative links, and confirm each new feature folder includes its overview, relevant role outputs, and synthesis. For skills, check that the requested output format is specific and that referenced repository paths exist. No coverage threshold applies.

## Commit & Pull Request Guidelines

Git history is sparse and does not establish a strict convention. Use short, imperative commit subjects such as `Add retention planning skill`. Keep commits focused on one role, feature, or documentation concern. Pull requests should summarize the business goal, list affected roles or features, identify assumptions and illustrative figures, and link any related issue. Include before/after images only when visual assets change.
