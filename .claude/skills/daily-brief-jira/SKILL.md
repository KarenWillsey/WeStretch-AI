---
name: daily-brief-jira
description: Use when running Karen's daily Jira review as part of the daily brief — pulls tickets assigned to her and new @mentions via direct Jira Cloud REST API calls (no Jira MCP connector exists).
---

# Daily Brief — Jira

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md` for the full problem/spec this serves.

No Jira MCP connector exists in this project. This skill calls the Jira Cloud REST API directly (e.g. via `curl`) using HTTP Basic Auth.

## 0. Setup

1. Read credentials from `CEO/In Progress/Set up Daily housing/state/.jira-credentials.json` — keys: `site`, `email`, `api_token`, `account_id`. This file is gitignored; never print the `api_token` in full, never write it into the report, and never commit it.
2. Auth header: HTTP Basic, `email:api_token` base64-encoded (`curl -u "email:token"` handles this automatically).
3. Base URL for all calls: `{site}/rest/api/3`.
4. Sanity-check the connection with `GET {site}/rest/api/3/myself` before querying. If it doesn't return 200, or the credentials file is missing, stop and emit only:
   `COULDN'T CHECK: Jira — connector unavailable ([error]).`
   Do not fabricate ticket data or reuse a previous run's list.

## 1. Assigned to Karen (full rescan every run — no dedup, matches the Asana Today/Recently Assigned pattern)

Endpoint: `GET {site}/rest/api/3/search/jql`
JQL: `assignee = currentUser() AND resolution = Unresolved ORDER BY updated DESC`
Params: `fields=summary,status,priority,updated,duedate,project`, `maxResults=100`.
Paginate via the response's `nextPageToken` if `isLast` is `false` — don't assume one page covers everything.

List each ticket: key (e.g. `WEMVP-8794`), summary, project name, status, priority, due date (if set), and a link (`{site}/browse/{key}`).
Report the total count as a headline stat.

## 2. New @mentions (delta since last check — this is the one Jira section that tracks state, matching the Kari sent-rollup pattern)

**Known limitation, state plainly in the report:** the Jira REST API has no dedicated "mentioned me" endpoint reachable with a standard API token. This uses a full-text search for Karen's account ID (which Atlassian Document Format stores wherever she's @mentioned) combined with "updated since last check" as a proxy for "new." It is a heuristic, not a guarantee — an issue can appear here because something else on it changed after an old mention, not because the mention itself is new. Always include this caveat in the output; never present mention results as certain.

1. Read `last_checked_at` from `CEO/In Progress/Set up Daily housing/state/jira-mentions-state.json`.
2. Endpoint: `GET {site}/rest/api/3/search/jql`
   JQL: `text ~ "accountId:{account_id}" AND updated >= "{last_checked_at as 'YYYY-MM-DD HH:MM'}" ORDER BY updated DESC`
   (JQL date literals require `"YYYY-MM-DD HH:MM"` — convert the stored ISO timestamp before building the query.)
   Params: `fields=summary,status,updated,project`, `maxResults=50`.
3. List each: key, summary, project, updated, link.
4. **First run note:** the state file was seeded to its creation time, so the very first live run will correctly show zero new mentions — that's expected, not a bug.
5. Only after this run's report is successfully handed off to `daily-brief-compose`, update `last_checked_at` in the state file to this run's start time. If the run fails before compose, leave the state file untouched (mirrors the Kari rollup's failure handling).

## 3. Verification pass

- The count of tickets pulled must match the count reported (nothing summarized away).
- Every key/summary/status/date in the output must come from this run's actual API results, never assumed or reused from a prior run.

## 4. Failure handling

- Any individual call failure: include a `COULDN'T CHECK: [what]` line with the real error, and don't update `jira-mentions-state.json` this run.

## Output contract (consumed by `daily-brief-compose`)

```
assigned: [{key, summary, project, status, priority, due, url}]
assigned_count: N
new_mentions: [{key, summary, project, updated, url}]
mentions_caveat: "Mentions are best-effort (text-match heuristic, see skill notes) — not guaranteed complete or precise."
couldnt_check: [string, ...]
```