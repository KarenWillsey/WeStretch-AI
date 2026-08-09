---
name: asana-backlog-triage
description: Use when Karen wants to work through her Asana backlog (My Tasks, all projects) in small batches — presents each task with minimal context, takes a quick keep/delete/complete/reschedule decision, and executes it immediately in Asana.
---

# Asana Backlog Triage

Reference: `daily-brief-asana` for the daily Today/Recently Assigned pull — this is a separate, on-demand cleanup session for the broader backlog, not part of the scheduled daily brief.

Ground rule: batches must be small (default 5, Karen can ask for a different size) and fast. This exists specifically to avoid facing 200+ tasks at once — never dump the whole backlog in one message.

## 0. Setup

1. `get_me` to confirm the Asana account.
2. Read `state/asana-backlog-triage.json` for `confirmed_keep_gids` — tasks Karen already explicitly said "keep, don't ask again" in a prior session. Deleted/completed tasks need no tracking; they're just gone from Asana.
3. If Asana MCP unreachable: `COULDN'T CHECK: Asana backlog triage — connector unavailable.` Stop.

## 1. Pull the next batch

- Pull incomplete tasks assigned to Karen (`get_my_tasks(completed_since="now", opt_fields="name,due_on,assignee_section.name,permalink_url,projects.name")`, paginating as needed) — this is already workspace-wide by assignment, covering every project, not just My Tasks.
- Filter out any gid in `confirmed_keep_gids`.
- Take the next N (default 5) from what remains. Default order: oldest-touched first (the true neglected backlog), unless Karen asks for a different slice (e.g. "just the ones with due dates," "just the emoji routine ones").

## 2. Present the batch

One line per task: **Task name** — project (if any) — due date (if any) — current section (if any). Nothing else unless Karen asks.

## 3. Take decisions

Ask for a plain conversational decision per task — no rigid multi-choice UI, speed matters more than structure here. Accepted shorthand:
- **delete** → `delete_task`. This is hard to undo in Asana — if a task might actually matter, don't delete on a guess; ask instead.
- **complete** → `update_tasks` with `completed: true`.
- **keep** → no change; add its gid to `confirmed_keep_gids` in state so it's not re-asked in future triage sessions. (It'll still appear in the regular daily brief if it's in Today/Recently Assigned — this list only suppresses re-asking here.)
- **due `<date>`** / **today** / **this week** / **later** → `update_tasks` with the given `due_on`, and `assignee_section` if Karen names a target section.
- Anything ambiguous → ask a quick follow-up. Never delete or complete on an unclear instruction.

## 4. Execute immediately

Apply each decision as soon as it's given — don't silently queue all of them and apply at the end. Confirm each action succeeded (or report the failure) so Karen sees real progress as it happens.

## 5. Wrap-up

After the batch: report counts (kept / deleted / completed / rescheduled) and how many remain untriaged. Ask whether to run another batch now or stop — never auto-continue into another batch without asking.

## Failure handling

Any single task's update/delete failing: report it plainly, don't silently skip it, don't retry blindly.

## Output (conversational, no fixed report format — this is a live session, not a compose-and-send artifact)