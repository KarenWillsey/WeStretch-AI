# state/

Machine-written runtime state only — never hand-edit it as if it were
documentation, same rule as
`Team/CEO/In Progress/Set Up Daily Housekeeping/state/`:

- `last-run.log` — shared banner/summary log for both scheduled runs,
  lines prefixed `[nightly-action]` or `[monthly-refresh]`.
- `monthly-refresh-log.json` — structured per-run history for the monthly
  refresh only (URLs checked, changes found).

See `../Implementation Spec.md` "State tracking" and "Reliability bar."
