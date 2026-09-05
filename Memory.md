# Project Memory (global / cross-role)

This file holds only facts that are truly cross-role: general Karen workflow
preferences and org-wide decisions that don't belong to one officer's work.
Role-specific and project-specific memory now lives closer to the work: see
`Team/ROLE/Memory.md` for each C-suite role, and `Team/ROLE/.../ProjectName/Memory.md`
for individual initiatives. See `CLAUDE.md` under "Memory" for the full model.

## Karen's workflow preferences (feedback)

Two standing rules from Karen (established 2026-08-07, App Store image work,
originated in CMO but apply to any deliverable-producing work across roles):

1. **Never place unreviewed generated assets into an Output folder she collects from.** Inspect and verify first, deliver only what passes.
   - **Why:** A prior run delivered visibly broken images (overlapping text, wrong fonts) straight into her pickup folder.
   - **How to apply:** Render to scratch, visually inspect and measure, then copy only passing files to the delivery folder.

2. **If supplied title/subtitle copy looks misspelled or ungrammatical (e.g. "teh"), ask her to confirm exact wording before production.** Never silently correct, never render it as-is without asking.
   - **Why:** The template rules said "render exactly as given," which shipped a typo; she wants a confirmation gate instead.
   - **How to apply:** This gate is written into the App Store image pipeline's own docs (see `Team/CMO/In Progress/App Store/App Store Image Creation/Memory.md`) and should be applied by analogy anywhere else copy is rendered verbatim into a deliverable.

3. **Be token-efficient in every task, always.** Short responses, no fluff/analogies, use the most direct tool for the job, avoid redundant work.
   - **Why:** Karen said (2026-08-21) that "don't worry about the credit limit" on a specific task is never permission to be verbose generally. Token efficiency is a constant default, not situational.
   - **How to apply:** Applies to chat responses (short, plain, no filler) and to how work gets done (pick the right tool/skill first time, don't re-read files already in context, don't over-dispatch agents). Not worrying about a budget for one task means "don't stall the work," not "spend freely."

4. **"git commit and push all" means stage and commit everything currently unstaged, without stopping to ask which parts to include.**
   - **Why:** Karen clarified (2026-08-24) after being asked to scope down a commit that included unrelated pending work. She wants "all" taken literally going forward, not treated as a prompt to filter or confirm scope.
   - **How to apply:** When Karen says "commit and push all" (or equivalent), stage every unstaged/untracked change across the repo (including submodules: commit and push inside each dirty submodule first, then bump its pointer in the parent) and commit/push without an `AskUserQuestion` scoping check first. Still apply the normal safety checks (no secrets, review `git status` after a broad `git add`); this rule removes the scope-confirmation step, not the safety review. If something looks genuinely broken (e.g. a bug producing phantom untracked files), it's fine to fix and mention it, but don't hold the commit for a scoping decision.

5. **No em dashes anywhere in any company output, full stop. This is absolute. Check every single response, every time, with no exceptions for drafts or casual chat text.**
   - **Why:** Company-wide style rule set by Karen at the Manager level (2026-08-20), applies to every role and every deliverable, not just one project. **Violated 2026-08-29**: this rule was already documented right here in this file, yet a copywriting draft (30 title/subtitle pairs for WeStretch-UX, delivered as plain chat text, not a committed file) used em dashes throughout. Karen was explicit that "draft, not yet shipped" is not an exemption. The rule applies to the response itself, not just to what eventually lands in a file. She warned that a repeat costs token credit back to her. **Violated again the same day**: the fix for this very rule (this entry, plus a new item 6) itself contained em dashes, and they went unnoticed until a full-file sweep found em dashes scattered through nearly every other entry in this file too, most predating the rule. Checking only newly-written sentences is not enough. Any time this file (or any file) is touched, scan the whole file, not just the new lines.
   - **Reinforced 2026-09-05:** Karen: "clean up all em dashes never just log them, fix them." Finding em dashes in existing files and writing a tracker item about them is not acceptable; the fix happens in the same session. A repo-wide sweep followed (2,586 across 170 tracked files, every file WeStretch owns).
   - **Two places are permanently out of scope, decided by Karen 2026-09-05: leave their em dashes alone.** (a) Vendored third-party packages under `.agents/` (the skill packages and the tool/integration docs beside them, plus their `.claude/skills/` junctions). They get overwritten on the next package update and they are not WeStretch's words. (b) Scraped third-party source material held as raw data, the standing example being the Bend Google Play reviews in the `website-repo` submodule (`competitors/bend/bend-google-play-reviews.md`). These are other people's words kept verbatim as evidence, not company output. Do not sweep either, do not raise either as a to-do again. The rule still applies in full the moment any of that text gets quoted into something WeStretch publishes: strip the em dash in the quote, not in the source file.
   - **How to apply:** Never write an em dash in any generated copy, doc, code comment, or chat response across this repo/project, full stop, no exceptions for drafts, brainstorms, or "just talking it through." Before sending ANY response containing generated prose (not just file writes), scan it for the em dash character and replace with a period, comma, colon, semicolon, parentheses, or a restructured sentence. When editing a file that already exists, scan the entire file for stray em dashes while you're in there, not just the lines you're changing. Applies even inside text supplied by someone else (a draft from Kari or a teammate): strip or replace any em dash found in source material before it ships or before it's shown back to Karen at all.

6. **Never describe WeStretch's personalization as the app "learning," "watching," or "getting to know" the user's body over time.**
   - **Why:** Factually wrong. Karen corrected this explicitly (2026-08-29) after a WeStretch-UX copywriting draft used that framing. Elevated from that project's `Memory.md` to here since any role writing about the app's personalization (marketing copy, product docs, in-app copy) needs to get this right, not just one project.
   - **How to apply:** The real mechanism is that the algorithm determines the next important stretches based on physiotherapist recommendations (a prescriptive, expert-backed selection, not observational/adaptive learning), and methodically increases pose hold time and difficulty over time on a schedule. Use language like "physio-backed picks," "physiotherapist-recommended progressions," "your holds and difficulty step up on schedule." Never "learning your body," "getting to know you," "taking notes on what feels good for you," or similar adaptive/observational phrasing, anywhere in the repo.

7. **In app/marketing copy, when a comma could go either way (optional vocative commas, e.g. around an inserted name), leave it out.**
   - **Why:** Karen said (2026-08-29, `guest-welcome-onboarding-copy.csv`) that commas I added around `{first_name}` insertions ("Sign in, {first_name}, and...") were "overkill." Casual/punchy in-app copy reads better without them, even where formal grammar would normally call for one.
   - **How to apply:** Default to no comma around a name or short inserted token unless dropping it genuinely creates a misread (e.g. two adjacent tokens running together, like `{routines_completed}` directly followed by `{first_name}`). Applies to any title/subtitle/push-notification-style copy across roles, not just this file.

8. **Never leave working/scratch copies committed or lying around in the repo. Any automation or session that generates temporary data must clean up after itself before finishing.**
   - **Why:** Karen found three raw Jira API dump files (`assigned_tickets_data.json`, `jira_brief_output.json`, `mentions_data.json`) sitting untracked at the repo root, left behind by a `daily-brief-jira` run (2026-08-31). They were intermediate working data for building the daily brief, not a deliverable, and should have been deleted once the brief was produced.
   - **How to apply:** If a task needs a scratch/intermediate file at all, write it to the session's actual scratchpad directory (never the repo), and if it must briefly touch the repo for some tool-specific reason, delete it before the task ends. Before finishing any task, run `git status` and treat any unexpected untracked file as a cleanup item, not something to leave for later or silently commit. This applies to every role and every automation (scheduled or interactive), not just Jira. See `.claude/skills/daily-brief-jira/SKILL.md` for the specific fix applied to the skill that caused this.

## Repo restructure (project)

On 2026-08-17, the repo moved from one root `CLAUDE.md`/`Memory.md` to a
distributed model: every role folder (including `CEO/`) got its own
`CLAUDE.md` + `Memory.md`, and every active project inside a role's
`Ideas/In Progress/Ready` folders got the same pair. Root files were trimmed
to only cross-role content as part of that move.

- **Why:** Karen wanted each officer's responsibilities isolated (their own
  scope + memory, not mixed into one shared file), with consistent naming
  across all 11 roles, so the structure scales as more roles accumulate
  active project folders the way CMO and CEO already had.
- **How to apply:** When creating a new role skill or starting a new
  initiative, follow the structure documented in the root `CLAUDE.md` rather
  than adding content back into this file or inventing a new pattern.

## Manager/Team restructure (project)

On 2026-08-19, all 11 officer folders (`CEO/` through `CXO/`) moved under a
new `Team/` folder (e.g. `CEO/` → `Team/CEO/`). The repo root (this
`CLAUDE.md`/`Memory.md`) is now framed as **the Manager**: the
orchestrator/delegator Karen addresses directly ("tell the Manager to do
this"), which routes work to the officer(s) under `Team/` with the relevant
skills/mandate.

- **Why:** Karen wanted the root level to read as a clean delegation point
  rather than a peer sibling of 11 officer folders. As she put it: "the
  directory to the orchestrator, the delegator of work."
- **How to apply:** All path references to officer folders take a `Team/`
  prefix (`Team/CMO/...`, `Team/CEO/In Progress/...`, etc.). The Windows
  Scheduled Task and `run-daily-brief.ps1` that drive the daily brief
  automation were repointed at `Team/CEO/In Progress/Set up Daily
  housing/run-daily-brief.ps1` as part of this move. If daily brief state
  files ever seem stale, check the scheduled task's action path first.

## Root-folder cleanup (project)

On 2026-08-19: `Features/` moved to `Team/CPO/Ideas/Features/` (a not-yet-started
feature is a CPO roadmap idea, even if cross-role). `CHATTY_REVIEW.md` moved
into `Team/CPO/Ideas/Features/Multiplayer Stretches/` (the feature it critiques;
its P1 findings on that feature's experiment design are still unaddressed).
`ToneManager/` (empty file, no content) and `tmp/` (empty, untracked) were
deleted. `Globial Knowledge Content/` renamed to `Knowledge Base/` (typo fix +
standard term).
