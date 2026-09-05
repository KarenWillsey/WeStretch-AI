# CGO; Growth Experiment Design: Multiplayer Stretching

_Skill applied: `Team/CGO/skills/growth-experiment-design`_

## Hypothesis

Users who complete at least one "stretch party" (async social session) in their first 30 days will have higher D30 retention than users who don't, because social accountability reduces the motivation drop-off that drives solo-user churn.

## Design

- **Variant**: users see the "invite a friend to stretch" prompt after completing a routine, starting at day 3 of their lifecycle (once they've formed initial habit signal).
- **Control**: users see the existing solo completion screen with no social prompt.
- Randomize at the user level, not the session level, to avoid contaminating the retention read with within-user variation.

## Success metric and threshold

- **Primary metric**: D30 retention, variant vs. control.
- **Threshold**: pre-register the minimum lift that would justify further investment (e.g., in live sync per [cpo.md](cpo.md)), set this with CFO/CPO before launch, not after seeing results, to avoid post-hoc rationalization.
- **Secondary read**: among variant users, retention delta between those who *sent* an invite vs. those who only *received* one, tells us whether the mechanic works via initiating or via being pulled in by others.

## Risks

- **Contamination**: control-group users may still be invited by variant-group friends, diluting the control's "no social exposure" purity. Mitigate by tracking control users who receive an invite as a separate analysis segment rather than excluding them.
- **Seasonality**: avoid launching the test during a period with unrelated retention-affecting changes (e.g., concurrent pricing test per [cro.md](cro.md)); stack of simultaneous experiments will confound the read.
- **Small early sample**: initial stretch-party usage will be low until enough users have someone to invite; don't call the experiment early, wait for a large enough invited cohort before reading results.
