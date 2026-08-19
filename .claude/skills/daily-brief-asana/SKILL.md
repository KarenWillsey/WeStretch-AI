---
name: daily-brief-asana
description: Use when running Karen's daily Asana review as part of the daily brief — pulls Recently Assigned and Today's tasks and flags emerging urgency.
---

# Daily Brief — Asana

Reference: `Team/CEO/In Progress/Set up Daily housing/Implementation Spec.md` for the full problem/spec this serves.

**Note (2026-08-09):** Asana inbox-notification clearing was in scope for V1 but the Asana MCP connector available in this project has no inbox/notifications endpoint — there's no tool to list or clear them. That feature has been dropped from this skill entirely rather than left as a permanent `couldnt_check` stub; if a notifications tool becomes available later, it can be re-added as a new step.

## 0. Setup

1. Call the Asana MCP `get_me` (or equivalent) to confirm the Asana user this run operates as.
2. If Asana MCP tools are unreachable, stop and emit only:
   `COULDN'T CHECK: Asana — connector unavailable ([error]).`
   Do not fabricate task data or reuse a previous run's list.

## 1. Today's tasks + 2. Recently Assigned tasks

Both pull from the same real Asana My Tasks sections Karen actually uses day to day — this is the literal "Today" and "Recently Assigned" section she sees in the Asana app, not a due-date heuristic.

**Correct method (fixed 2026-08-09, live-verified):** call
`get_my_tasks(completed_since="now", opt_fields="name,due_on,assignee_section.name,permalink_url", limit=100)`,
paginate via the returned `next_page.offset` as needed, and filter client-side for `assignee_section.name == "Today"` and `== "Recently Assigned"`. This has been verified to exactly match Karen's own Asana app counts (26 Recently Assigned, 17 Today). Section membership is not clustered in the default sort order, so keep paginating until both sections' tasks have all been found — don't stop after page 1 assuming the rest live elsewhere. In practice both sections combined have been under 50 tasks, well within 1-2 pages.

**Do not use these fields for this purpose — both were tried and are wrong:**
- `assignee_status` — a legacy 4-value enum (today/upcoming/later/new) that cannot see Karen's custom sections ("Track It or FAIL," "Daily 20 minute chunks," "Waiting On ~ Review Daily") and returned the same generic value for every task regardless of its real section.
- `task.memberships` — only reflects section membership within real *projects*; tasks living only in My Tasks (no other project) return an empty array.

List each task with task name, due date (if any), and a link (`permalink_url`). For "Recently Assigned," note who assigned it if that's derivable; most of Karen's tasks are self-assigned, so this will often just be Karen herself — don't guess otherwise.

Report the total open-task count in Karen's My Tasks (across all sections) as a headline stat too — as of 2026-08-09 it was 200+, most with no due date or wildly inconsistent ones (years in the future, months overdue). This is useful backlog-size context distinct from Today/Recently Assigned.

## 3. Urgency flags (starting heuristic — expect to tune after real use)

Flag a task as trending urgent if any of:
- Due within 24 hours and not yet marked in-progress/complete.
- Still open with no comment/activity in several days despite an approaching due date.
- Explicitly marked high priority (if a priority field exists in the workspace).

List each flagged task with the specific reason it was flagged (not just "urgent") so Karen can sanity-check the heuristic and we can tune false positives/negatives over time.

## 4. Verification pass

- The count of tasks pulled from each query must match the count reported (nothing summarized away).
- Every task name/project/date in the output must come from this run's actual API results.

## 5. Failure handling

- Any individual call failure: include a `COULDN'T CHECK: [what]` line with the real error.

## Output contract (consumed by `daily-brief-compose`)

```
today: [{task, project, due, url}]
recently_assigned: [{task, project, assigned_by, url}]
urgent_flags: [{task, reason}]
couldnt_check: [string, ...]
```