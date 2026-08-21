# Claude Work Review

## Verdict

Claude produced a clear first-pass structure, but I would not use the skills or approve the multiplayer implementation as written. The largest issue is that the "Claude Code Skills" are not discoverable by Claude Code.

## Findings

### [P0] The 30 skills are stored in the wrong location

[`CLAUDE.md`](../../../../../CLAUDE.md) describes `ROLE/skills/...` as invokable Claude Code skills. Claude Code discovers project skills from `.claude/skills/<skill>/SKILL.md`; arbitrary `ROLE/skills` directories are not discovered. Plugin `skills/` directories only work when contained in an installed plugin.

Reference: [Anthropic's skill documentation](https://code.claude.com/docs/en/slash-commands)

Recommendation: place operative skills under `.claude/skills/` with role-prefixed names, for example `cto-tech-architecture-review`. Keep the role folders as business-reference organization if desired.

All ten joke skills also use `name: jokes`. They will conflict if moved into the project skill directory. Use names such as `cto-jokes`, or consolidate them into one `executive-jokes` skill with a role argument.

### [P1] The retention experiment cannot answer its stated question

[`cgo.md`](cgo.md) compares party completers with non-completers. Completion happens after treatment and is self-selected, so that comparison cannot establish the feature's effect.

Additional conflicts:

- Control users can receive invitations; segmenting them afterward does not restore randomization.
- [`coo.md`](coo.md) says launch to all users while the experiment requires a control group.
- CMO targets users with seven-day streaks, while CGO starts exposure on day three.
- A checkpoint exactly 30 days after launch does not provide complete D30 data for users enrolled after launch day.
- There is no baseline, minimum detectable effect, sample-size calculation, eligibility definition, guardrail metric, or experiment duration.

Recommendation: use intention-to-treat on eligible users assigned to see the invitation prompt. Treat party creation and completion as mediator metrics. Either use graph-level randomization or define this as a randomized-encouragement experiment and exclude recipient outcomes from the primary causal result.

### [P1] The invitation architecture contradicts the acquisition plan

[`cpo.md`](cpo.md) assumes a friend graph and push notifications. [`cmo.md`](cmo.md) expects invitations to convert non-users. Non-users do not have an app push token or friend record.

The MVP needs an explicit decision about:

- Existing-user-only invitations versus invitations to non-users.
- Share sheet, SMS, email, or universal/deep links.
- Expiring and single-use invite tokens.
- Signup attribution and account linking.
- Invite cancellation, blocking, abuse controls, and rate limits.

A shareable invitation link may remove the friend-graph requirement from the MVP.

### [P1] The greenlight is based on assumptions rather than discovery

[`cto.md`](cto.md) explicitly assumes the entire current architecture. Despite that, [`synthesis.md`](synthesis.md) concludes that existing infrastructure is sufficient and no hiring is required.

The 3-5 engineer-week estimate, 1-2 designer-week estimate, additional 2-3 weeks for a friend graph, and "minor internal" legal review have no supporting implementation or capacity data.

Recommendation: replace the current greenlight with a short discovery phase covering the actual backend, clients, authentication, push/deep-link infrastructure, analytics, team capacity, pricing, baseline retention, and current privacy disclosures. Estimate only after that review.

### [P1] Privacy and security coverage is incomplete

[`cio.md`](cio.md) concludes that no new regional obligations appear likely without knowing jurisdictions, age groups, or the exact data source. [`cfo.md`](cfo.md) then assumes legal review is minor.

Missing areas include retention and deletion, account deletion, historical visibility after leaving, authorization rules, invite-token security, unwanted invitations, blocking/reporting, minors, and privacy-store disclosures. Muting notifications should not implicitly revoke membership or data access; leaving and muting need separate semantics.

Google explicitly restricts socially sharing data obtained through Android health permissions without informed consent.

Reference: [Google Play health-permissions guidance](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en-GB)

### [P2] The claimed independent consensus is not independent evidence

[`synthesis.md`](synthesis.md) says the roles converged independently. The transcript shows that one Claude session wrote every document sequentially from the same initial premise. The agreement is useful organization, but it is not separate validation.

Recommendation: require each review to identify evidence, assumptions, blockers, confidence, and explicit disagreement. The synthesis should preserve disagreements rather than treating repetition as confirmation.

### [P2] The skills encode unsupported company facts

Several skills assume WeStretch is startup-stage, has a lean team, has established brand language, and should optimize for runway. None of that exists in the repository's source material.

Recommendation: add a small authoritative business context set covering product, architecture, pricing, team, metrics, brand, markets, and constraints. Skills should return "insufficient information" or a discovery checklist when required inputs are absent.

### [P3] Repository cleanup is needed

I found 22 `.DS_Store` files, no `.gitignore`, an empty unreferenced `previous-jokes.md`, and no final newline in `README.md`. The transcripts do not establish that Claude created the `.DS_Store` files, but they should still be excluded.

## What was done well

- All 30 skill files have valid YAML frontmatter.
- All relative links across the 45 Markdown files resolve.
- The async-first approach is a reasonable hypothesis to investigate.
- Privacy and cross-user authorization were considered early.
- Assumptions are often labeled, even though the final recommendation relies too heavily on them.
- Claude did not run `git`, `dotnet`, or make unrelated code changes.

## Recommended order

1. Fix skill discovery and names.
2. Add authoritative business context.
3. Perform technical and product discovery.
4. Redesign the experiment.
5. Rewrite the synthesis as a conditional decision record.

No existing project files were changed during the review. This report is the only file added.
