# Radio Specialist — Single Radio Ad Revision — CLAUDE.md

Scope: revising, tightening, or polishing a single existing WeStretch
30-second radio ad script for natural read-aloud delivery — not generating
a fresh batch (see the sibling project `5 x 30 second radio copy/` for
that). Read `Memory.md` alongside this file before revising any script; it
holds the read-aloud house-style rules learned from real revision rounds.

## Where things live

- `SKILL.md` — the `radio-ad-revise` skill: depends on `westretch-core`
  (`Team/CMO/skills/westretch-core/`, load first for guardrail compliance).
  Applies the read-aloud checklist in `Memory.md` to a supplied draft and
  fits it to a target spot length (default 30 sec).
- `Output/` — all revision output lands here, dated/versioned, with a short
  changelog of what changed and why per round.
