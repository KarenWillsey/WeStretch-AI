# Local LLM usage

This is a portable, text-only agent skill. It does not require a specific model, API, or external tool.

## Skills-compatible harnesses

Copy the complete `westretch-direct-response-marketing` folder into the skill directory used by the local harness. Preserve the folder structure so links from `SKILL.md` to `references/` continue to work.

Invoke it by name when explicit skill invocation is supported:

```text
Use $westretch-direct-response-marketing to create a Meta campaign for the regular WeStretch Pro subscription.
```

Automatic discovery can also use the YAML `name` and `description` in `SKILL.md`.

## Harnesses without skill support

Use `SKILL.md` as the system or project instruction. Make the three reference files available in the same context or retrieval collection:

- `references/westretch-context.md`
- `references/direct-response-method.md`
- `references/output-templates.md`

The model should load `westretch-context.md` for every WeStretch marketing task, then load only the other reference needed for the current deliverable.

## Recommended prompts

```text
Use $westretch-direct-response-marketing to turn these customer comments into a ranked Halo Strategy research report. Separate observed evidence from inference.
```

```text
Use $westretch-direct-response-marketing to create the first 25 static Meta ad concepts for women 50-65. Organize them across five angles and awareness levels.
```

```text
Use $westretch-direct-response-marketing to audit this WeStretch landing page against the 17-step sequence. Give keep, iterate, stop, and test-next decisions.
```

```text
Use $westretch-direct-response-marketing to review this week's funnel data and write five one-variable experiments for next week.
```

## Updating product facts

Update `references/westretch-context.md` when pricing, trial length, product entitlements, or verified proof changes. Keep volatile numbers marked `[VERIFY]` when the skill will be shared across environments without access to current company data.
