# Reset Challenge Static Ads

**Nine finished PNGs, ready for review. No ads published.**

- [Preview all nine](contact-sheet.png)
- [Download the PNG and copy package](reset-static-ads-v01.zip)
- [Open the PNG folder](Output/)
- [Copy and launch handoff](copy-handoff.md)
- [Editable copy and photo manifest](manifest.json)
- [Quality checks](qa.md)

Each concept has 1080 x 1080, 1080 x 1350 and 1080 x 1920 versions.
These are three ad concepts, not nine separate tests.

| ID | Concept | Photograph |
|---|---|---|
| R01 | Slept Wrong | Female Actor 02, approved bedroom source |
| R02 | Stiff, Sore + Tight | Female Actor 03, approved living-room source |
| R03 | There's Always Something | Male Actor 02, new car-exit source |

Karen approved the plan and required the CMO actor skills for image production.
The new R03 source was created with `male-actor-02-image-generator`, using its
canonical reference. It remains in CMO `Review ToDo/` for catalogue approval.
R01 and R02 reuse the existing actor photographs selected in the approved plan.

## Editing later

The `Source/` folder contains nine editable HTML layouts. They reference real
fonts and existing source assets in this repository. Keep those paths intact.
They are not standalone files to send outside the repo.

Change copy or photo references in `manifest.json`, and layout rules in
`render.mjs`. Run from the repo root:

```powershell
node 'Team/CMO/In Progress/28 Day Challenge/Static Ads/render.mjs'
```

The renderer uses the already-installed `puppeteer-core` and `sharp` packages
in the website submodule and local Chrome. It writes candidates to the OS temp
folder `westretch-reset-ad-render`; it never overwrites delivery files itself.
Inspect changed candidates before copying them into a new output version.

The ZIP contains the nine PNGs and copy handoff. Editable sources stay here.
