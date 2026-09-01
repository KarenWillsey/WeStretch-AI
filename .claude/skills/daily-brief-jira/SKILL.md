---
name: daily-brief-jira
description: Use when running Karen's daily Jira review as part of the daily brief — pulls her tickets in any currently active sprint and recent unreplied @mentions via direct Jira Cloud REST API calls (no Jira MCP connector exists).
---

# Daily Brief — Jira

Reference: `Team/CEO/In Progress/Set Up Daily Housekeeping/Implementation Spec.md` for the full problem/spec this serves.

No Jira MCP connector exists in this project. This skill calls the Jira Cloud REST API directly (e.g. via `curl`) using HTTP Basic Auth.

## 0. Setup

1. Read credentials from `Team/CEO/In Progress/Set Up Daily Housekeeping/state/.jira-credentials.json` — keys: `site`, `email`, `api_token`, `account_id`. This file is gitignored; never print the `api_token` in full, never write it into the report, and never commit it.
2. Auth header: HTTP Basic, `email:api_token` base64-encoded (`curl -u "email:token"` handles this automatically).
3. Base URL for all calls: `{site}/rest/api/3`.
4. Sanity-check the connection with `GET {site}/rest/api/3/myself` before querying. If it doesn't return 200, or the credentials file is missing, stop and emit only:
   `COULDN'T CHECK: Jira — connector unavailable ([error]).`
   Do not fabricate ticket data or reuse a previous run's list.

## 1. Assigned to Karen — active sprint only (full rescan every run — no dedup, matches the Asana Today pattern)

**Scope, changed 2026-08-10 per Karen's live feedback:** the original design pulled *every* unresolved ticket ever assigned to her (22 tickets on first live run, mostly stale backlog dating to 2019) — not useful for a daily "what's live right now" brief. This now scopes to tickets assigned to her **in a currently active sprint**, matching how she actually uses Jira day to day. It is normal and expected for this to be empty most days — Karen isn't usually a sprint participant, so an empty section here is a correct result, not a bug. (Verified live 2026-08-10: WEMVP's active Sprint 202 had 50+ tickets, none assigned to Karen.)

1. Discover active sprints: `GET {site}/rest/agile/1.0/board` to list all boards, filter to `type == "scrum"` (only scrum boards run sprints — kanban/simple boards never do). For each scrum board, `GET {site}/rest/agile/1.0/board/{boardId}/sprint?state=active` to get its active sprint(s), if any. Collect all active sprint IDs across all boards — don't hardcode a single board or project, since which board has an active sprint can change over time.
2. If no board has an active sprint at all, report the section as empty with a one-line note ("No active sprint found on any board") rather than silently omitting it.
3. Endpoint: `GET {site}/rest/api/3/search/jql`
   JQL: `sprint in ({sprintId1}, {sprintId2}, ...) AND assignee = currentUser() ORDER BY status`
   Params: `fields=summary,status,priority,updated,duedate,project`, `maxResults=100`.
   Paginate via `nextPageToken` if `isLast` is `false`.
4. List each ticket: key (e.g. `WEMVP-8794`), summary, project name, status, priority, due date (if set), and a link (`{site}/browse/{key}`).
5. Report the total count as a headline stat, and name which sprint(s) were checked (e.g. "Sprint 202 (WEMVP), ends Aug 20") so Karen has context for why the list is what it is.

## 2. New @mentions — capped at 7 days, excluding threads Karen already replied to (refined 2026-08-10 per Karen's live feedback)

**Known limitation, state plainly in the report:** the Jira REST API has no dedicated "mentioned me" endpoint reachable with a standard API token, and Jira's notification-bell "unread" state is internal to the web app — not exposed via any documented API reachable with an API token (checked live 2026-08-10: the closest thing, the legacy `/activity` Atom feed, is instance-wide activity with no personal read/unread concept, so it doesn't help here). This section instead uses a full-text search for Karen's account ID (which Atlassian Document Format stores wherever she's @mentioned). It is a heuristic, not a guarantee — an issue can appear here because something else on it changed after an old mention, not because the mention itself is new. Always include the caveat in the output; never present mention results as certain.

Karen's ask, to keep this from becoming noise: don't re-surface a mention forever, and don't show her a thread she's already responded to.

1. Read `last_checked_at` from `Team/CEO/In Progress/Set Up Daily Housekeeping/state/jira-mentions-state.json`.
2. Compute the effective floor as `MAX(last_checked_at, now - 7 days)` — this caps the lookback at 7 days even if the brief hasn't run in a while (e.g. after downtime), so a gap in runs never dumps a backlog of old mentions.
3. Endpoint: `GET {site}/rest/api/3/search/jql`
   JQL: `text ~ "accountId:{account_id}" AND updated >= "{effective_floor as 'YYYY-MM-DD HH:MM'}" ORDER BY updated DESC`
   (JQL date literals require `"YYYY-MM-DD HH:MM"` — convert the timestamp before building the query.)
   Params: `fields=summary,status,updated,project`, `maxResults=50`.
4. **Filter out threads Karen already replied to:** for each candidate issue, `GET {site}/rest/api/3/issue/{key}/comment` and check whether any comment's `author.accountId` matches Karen's `account_id`. If she has *any* comment on the issue, exclude it — she's already seen and engaged with it, so surfacing it again isn't useful. This is a coarse heuristic (it doesn't try to determine whether her comment came before or after the specific mention), document it as such rather than presenting it as precise.
5. List the remaining issues: key, summary, project, updated, link. Report both the raw match count and the excluded-as-already-replied count so the caveat stays honest (e.g. "3 mentions found, 2 excluded because you already replied — 1 shown below").
6. **First run note:** the state file was seeded to its creation time, so the very first live run will correctly show zero new mentions — that's expected, not a bug.
7. Only after this run's report is successfully handed off to `daily-brief-compose`, update `last_checked_at` in the state file to this run's start time. If the run fails before compose, leave the state file untouched (mirrors the Kari rollup's failure handling).

## 3. Verification pass

- The count of tickets pulled must match the count reported (nothing summarized away).
- Every key/summary/status/date in the output must come from this run's actual API results, never assumed or reused from a prior run.

## 4. Failure handling

- Any individual call failure: include a `COULDN'T CHECK: [what]` line with the real error, and don't update `jira-mentions-state.json` this run.

## Working data

Keep API responses and intermediate results in-memory and hand them to
`daily-brief-compose` directly per the output contract below — don't write
them to files in the repo. If a working file is genuinely unavoidable
(e.g. as a scratch buffer while paginating), write it to the session's
actual scratchpad directory, never to the repo, and delete it before this
skill finishes either way. **2026-08-31: a run left three raw API dump
files (`assigned_tickets_data.json`, `jira_brief_output.json`,
`mentions_data.json`) sitting at the repo root** — this section exists so
it doesn't happen again. See root `Memory.md` item 8.

## Output contract (consumed by `daily-brief-compose`)

```
active_sprints: [{name, project, ends}]      # empty array if no board has an active sprint
assigned: [{key, summary, project, status, priority, due, url}]
assigned_count: N
new_mentions: [{key, summary, project, updated, url}]
mentions_found_count: N
mentions_excluded_replied_count: N
mentions_caveat: "Mentions are best-effort (text-match heuristic, capped at 7 days, excludes threads you've already commented on) — not guaranteed complete or precise."
couldnt_check: [string, ...]
```