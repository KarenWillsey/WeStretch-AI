---
name: daily-brief-asana
description: Use when running Karen's daily Asana review as part of the daily brief — pulls Recently Assigned and Today's tasks, flags emerging urgency, and clears Asana inbox notifications that were actually reviewed in the report.
---

# Daily Brief — Asana

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md` for the full problem/spec this serves.

Ground rule: only clear an Asana inbox notification if it was actually resolved to a specific task and included in this run's report. If a notification can't be matched to a task, leave it and flag it — never clear something you didn't actually surface to Karen.

## 0. Setup

1. Call the Asana MCP `get_me` (or equivalent) to confirm the Asana user this run operates as.
2. If Asana MCP tools are unreachable, stop and emit only:
   `COULDN'T CHECK: Asana — connector unavailable ([error]).`
   Do not fabricate task data or reuse a previous run's list.

## 1. Today's tasks

Pull tasks in Karen's "My Tasks" that are due today or sit in the "Today" section, via `get_my_tasks` / `search_tasks`. List each with task name, project, due date, and a link.

## 2. Recently Assigned tasks

Pull tasks assigned to Karen within the last 24–48 hours (by assignment date, not creation date — a task created last week but just handed to Karen today still counts). List each with task name, project, who assigned it, and a link.

## 3. Urgency flags (starting heuristic — expect to tune after real use)

Flag a task as trending urgent if any of:
- Due within 24 hours and not yet marked in-progress/complete.
- Still open with no comment/activity in several days despite an approaching due date.
- Explicitly marked high priority (if a priority field exists in the workspace).

List each flagged task with the specific reason it was flagged (not just "urgent") so Karen can sanity-check the heuristic and we can tune false positives/negatives over time.

## 4. Inbox cleanup

1. Pull Karen's Asana inbox notifications.
2. For each notification that maps to a task already surfaced in §1–§3 of this run, mark it read/archived.
3. For any notification that doesn't clearly map to a reviewed task, leave it as-is and list it under a short "Unresolved Asana notifications" note — don't guess at what it's about.

## 5. Verification pass

- The count of tasks pulled from each query must match the count reported (nothing summarized away).
- Every task name/project/date in the output must come from this run's actual API results.

## 6. Failure handling

- Any individual call failure: include a `COULDN'T CHECK: [what]` line with the real error, and don't clear any inbox notifications this run (fail loud, don't half-complete cleanup).

## Output contract (consumed by `daily-brief-compose`)

```
today: [{task, project, due, url}]
recently_assigned: [{task, project, assigned_by, url}]
urgent_flags: [{task, reason}]
inbox_cleared_count: N
unresolved_notifications: [{summary}]
couldnt_check: [string, ...]
```