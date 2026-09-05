# Naming Convention

One consistent naming rule for the whole repo, so folder names stop being
decided case-by-case. Set 2026-08-21 (Karen). The Manager (root `CLAUDE.md`)
enforces this for any new folder/skill it creates or renames going forward.

## The rule

- **Folders (everything under `Team/`, and this repo's own top level):
  Title Case With Spaces.** Every word capitalized, spaces between words,
  no dashes/underscores. Example: `Team/CMO/In Progress/Jamie Meeting Notes/`.
- **Skills (`skills/<skill-name>/`, both `Team/ROLE/skills/` and
  `.claude/skills/`): all-lowercase, dash-separated.** Example:
  `Team/CMO/skills/westretch-core/`, `.claude/skills/cmo-jamie-meeting-notes/`.
  This already matched almost everywhere before this cleanup; it's the
  Claude Agent Skills spec convention, not a new rule.

## What's exempt (not covered by the folder rule)

- **Role codes** (`CEO`, `CFO`, `CMO`, ...), acronyms, not word-folders.
- **The four bucket folders** (`Ideas`, `In Progress`, `Ready`,
  `Review ToDo`), already Title Case, listed here for completeness.
- **Tool/working subfolders inside an active project**: `Output/`,
  `references/`, `assets/`, `agents/`, `state/`, `examples/`,
  `SourceImages/`, `Fonts/`, `__pycache__/`, numbered run folders
  (`Run_01/`), and similar. These are read/written by scripts and skills at
  exact relative paths, follow their own tool conventions (Python's
  `__pycache__` can't be renamed at all; a skill's `references/` folder is
  the Agent Skills spec name), and renaming them risks silently breaking
  automation for no visible benefit. Leave as-is.
- **Vendored/third-party skill packages** under `.agents/skills/` (and the
  `.claude/skills/` junctions pointing at them), not ours to rename, per
  the existing note in root `CLAUDE.md`.
- **File names** (`CLAUDE.md`, `README.md`, `Memory.md`, `WORK-TRACKER.md`)
, out of scope for this rule; it governs folders only. (One stray
  casing bug, `Team/COO/Readme.md`, got fixed to `README.md` as a drive-by
  since every other role already used that exact casing.)

## Done 2026-08-21

| Old | New | Why |
|---|---|---|
| `Team/CMO/Review/` | `Team/CMO/Review ToDo/` | Karen's explicit rename request |
| `Team/CMO/skills/WeStretch-Core/` (plus a malformed nested `westretch-core/` copy and a stray `.skill` zip left over from a package extraction) | `Team/CMO/skills/westretch-core/` | Skill name must be dash-case; also flattened the extraction artifact |
| `Team/CMO/In Progress/Jamie meeting notes/` | `Team/CMO/In Progress/Jamie Meeting Notes/` | Title Case rule |
| `Team/CFO/New folder/` | *(deleted, empty)* | Stray OS-default folder name, no content |
| `Team/COO/Readme.md` | `Team/COO/README.md` | File casing, drive-by fix |
| `Team/CEO/In Progress/Set up Daily housing/` | `Team/CEO/In Progress/Set Up Daily Housekeeping/` | Title Case rule + word fix; Karen confirmed "Housekeeping" fits the daily-brief-prep purpose better than "Housing" |
| `Team/CPO/Ideas/Features/multiplayer-stretches/` | `Team/CPO/Ideas/Features/Multiplayer Stretches/` | Karen confirmed: convert to Title Case like every other project folder (no more slug-style exemption) |
| `Team/CPO/Ideas/Features/1000-dau-growth-plan/` | `Team/CPO/Ideas/Features/1000 DAU Growth Plan/` | Same; DAU kept uppercase as an acronym, matching CPP/UX elsewhere in the repo |
| `Team/CEO/Ideas/Build an Advisotry Board/` | `Team/CEO/Ideas/Build An Advisory Board/` | Title Case + typo fix (Karen confirmed "Advisory") |
| `Team/CEO/Ideas/Nich Dashboard/` (+ `Nich Dashboard.txt` inside it) | `Team/CEO/Ideas/Niche Dashboard/` (+ `Niche Dashboard.txt`) | Typo fix (Karen confirmed "Niche"), content already said "Create a Niche Dashboard," so the folder name was the only place it was wrong |
| `Team/CMO/Ideas/App Stores/App Sore Keyword Creation/` | `Team/CMO/Ideas/App Stores/App Store Keyword Creation/` | Typo fix (Karen confirmed "Store") |

Every cross-reference to these paths (`CLAUDE.md`, `Memory.md`, `SKILL.md`,
`WORK-TRACKER.md` files, and the internal cross-links inside the two CPO
Features folders) was updated in the same pass. The `Set Up Daily
Housekeeping` rename also required updating the live Windows Scheduled Task
("WeStretch Daily Brief") to the new script path, confirmed via
`Get-ScheduledTask` after the change.

Renames used a two-hop `git mv` (temp name, then final name) for anything
where old and new names differ only by casing/spacing, a direct
case-adjacent `git mv`/`Move-Item` on Windows can silently collide with the
existing folder (NTFS is case-insensitive) and delete data; this happened
once during this cleanup (recovered from git before anything was lost). If
old and new names differ by more than casing/spacing (e.g. a real word
swap or typo fix), a direct rename is safe, no collision risk.

## Going forward

When creating a new project folder or skill, use the rule above; don't
default to whatever casing feels natural in the moment. If a new folder's
name doesn't fit cleanly (compound punctuation, a slug-style name like the
CPO Features case above), flag it here rather than guessing.
