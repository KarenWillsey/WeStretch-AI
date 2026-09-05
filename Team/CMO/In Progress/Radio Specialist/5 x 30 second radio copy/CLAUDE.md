# Radio Specialist (5 x 30 Second Radio Copy) CLAUDE.md

Scope: generates a fresh batch of 5 announcer-ready WeStretch 30-second
radio ad scripts, each on a distinct angle. For revising or polishing a
single existing radio ad script, see the sibling project
`Team/CMO/In Progress/Radio Specialist/Single Radio Ad Revision/` instead.
Read `Memory.md` alongside this file before running the skill.

## Where things live

- `SKILL.md`: the `westretch-radio-ads` skill: depends on `westretch-core`
  (`Team/CMO/skills/westretch-core/`, load first for personas/Strategic
  Thesis/honesty guardrail). Scans this project's `Output/` for angles
  already covered, then runs Chase (strategy) → Expert (copy) → Marg
  (grading) to produce 5 new scripts before saving.
- `Output/`: dated batch files only (`WeStretch-Radio-Ads-30sec-
  [YYYY-MM-DD].md`). All skill output lands here; never OneDrive or any
  other location (this was misconfigured until 2026-08-20; see `Memory.md`).
