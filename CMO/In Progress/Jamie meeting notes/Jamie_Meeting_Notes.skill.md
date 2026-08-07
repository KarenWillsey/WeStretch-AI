---
name: Jamie Meeting notes
description: Update WeStretch running meeting action items from a new Zoom transcript. Use when Karen provides the previous meeting-notes Markdown and a current transcript or SRT file. Preserve only work that remains open, add newly assigned actions, remove completed or superseded actions, and return a concise downloadable Markdown file.
---

# Jamie Meeting notes

Update the WeStretch team's running action-item Markdown using the newest meeting transcript.

## Inputs

1. The previous running action-item Markdown.
2. The newest Zoom transcript, preferably SRT, VTT, TXT, or Markdown.

## Required process

1. Read the complete previous action-item file and the complete transcript.
2. Treat the previous Markdown as the baseline, not as unquestioned truth.
3. Identify explicit task updates, assignments, completions, cancellations, dependencies, deadlines, and changed priorities in the transcript.
4. Remove completed, cancelled, duplicated, obsolete, or superseded items.
5. Keep existing tasks that are clearly still open.
6. Add new tasks only when the transcript supports a concrete next action.
7. Assign each task to the person explicitly responsible. Put cross-functional actions under `Shared / Team` only when no single owner is responsible.
8. Preserve important dependencies, such as waiting for onboarding, brand approval, localization approval, legal compliance, or another team member.
9. Do not add speculative tasks, meeting discussion, background information, opinions, travel notes, or ideas that were not accepted as current work.
10. Resolve obvious transcript-name variations consistently: Josee/Josie/Jose → Josee; Jacques/Jack/Jock only when the context clearly identifies the same person. Do not merge people when uncertain.

## Output rules

- Output one concise Markdown file.
- Title format: `# WeStretch Team Zoom – Remaining Action Items`
- Use these sections when applicable:
  - `## Karen`
  - `## Josee`
  - `## Jamie`
  - `## Shared / Team`
- Include only unchecked tasks using `- [ ]`.
- Start each item with a clear action verb.
- Keep one action or closely linked deliverable per checkbox.
- Include a deadline in the task only when it was explicitly stated.
- Do not include completed checkboxes, commentary, explanations, or a meeting summary unless requested.
- Prefer concise wording while preserving enough context for the team to act without reopening the transcript.

## Quality check

Before finalizing, verify that:

- Every retained task is still open.
- Every added task is supported by the transcript.
- Completed or superseded work is absent.
- Owners and dependencies are accurate.
- The file is valid, clean Markdown ready to replace the previous running list.
