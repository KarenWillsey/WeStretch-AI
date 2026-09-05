# App Store Specialist; CLAUDE.md

Scope: everything about getting WeStretch in front of people via the Apple
App Store: screenshots, copy, and (new) proactively hunting down every
marketing lever Apple makes available and working through them
systematically. This folder groups several sub-projects; read the specific
sub-project's own `CLAUDE.md` + `Memory.md` before working in it.

## Sub-projects

- `Ada Stretching Phone Image/`: Ada (brand character) stretching phone-image
  generation for App Store screenshots.
- `App Store Image Creation/`: the screenshot build pipeline (fonts, source
  images, output batches).
- `App Store Image Text Copywriting/`: headline/subtitle copy for
  screenshots.
- `App Store Description Copywriting/`: stub, no content yet.
- `Apple Opportunity Radar/`: **new, planning stage only as of 2026-08-21.**
  A standing capability (not a one-off asset job) that keeps a living
  knowledge base of every Apple App Store marketing lever, monitors
  developer.apple.com monthly for changes, and works through a backlog of
  opportunities one per night. See that folder's `Implementation Spec.md`
  for the full design; nothing here is built or scheduled yet.

## Relationship to the `aso` skill

`.agents/skills/aso/references/apple-specs.md` is a third-party skill
package's reference file (product page metadata + screenshot specs only,
snapshotted March 2026). `Apple Opportunity Radar/Knowledge Base/` is
WeStretch's own, broader, actively-maintained equivalent; it supersedes
that file in scope (adds Search Ads, In-App Events, CPPs, TestFlight,
App Clips, editorial pitches, feature-adoption bonuses, seasonal moments)
and is meant to stay current via its own monthly refresh rather than being
a static snapshot. Once built, treat `Apple Opportunity Radar/Knowledge
Base/` as the authoritative source for Apple opportunity work; the `aso`
skill's file can stay as-is for general ASO audit tasks unrelated to this
project.
