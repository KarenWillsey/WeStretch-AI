# Brand System, Memory

Durable facts for this folder only. Cross role facts go in the repo root `Memory.md`.

## Established 2026-09-09 (folder created)

1. **Architecture decision: one brand core, two skins.**
   - **Why:** Karen asked whether in app UI should be separate from global
     branding. Fully separate means the app and the ads drift apart. Identical
     means the app inherits billboard sized type. Two skins on one core is the fix.
   - **How to apply:** `core/` is shared and owned here by the CMO. The app skin
     lives under CXO and imports `core/tokens.css`. Never duplicate a colour or
     font value into a skin.

2. **Brand values are extracted from the official PDF, not invented.**
   - Source: `Knowledge Base/Brand Guildeline.pdf`, 47 pages.
   - Primary: Fire Red `#FC4850`, Midnight Grey `#1F1F1F`, Dark Grey `#4C4C4C`, White.
   - Secondary: Sunshine Gold `#FBBC05`, Lavender Blue `#667FD4`, Light Grey `#E4E4E4`, Medium Grey `#ADACAC`.
   - Type: Work Sans Bold for display, Inter Regular/SemiBold/Bold for everything else.
   - Print CMYK hex values differ from web hex values. Both are recorded in `core/brand-core.json`. Do not use web values on a print job.

3. **RESOLVED 2026-09-09: the app palette was drift, not a new direction.**
   - The Westretch-UX prototype had been running a green system
     (`--variant-accent: #178f78`, `--variant-dark: #0b5f51`, `--variant-soft: #dff6ef`)
     plus a slightly-off red (`#ff3946`, `#e8423a`). None of it appears in the brand book.
   - **Karen's call, verbatim: "red is right, green is drift. update everywhere."**
   - The prototype is now on Fire Red. Full change table is in
     `Team/CXO/In Progress/Westretch-UX/Memory.md`.
   - **How to apply going forward:** `Knowledge Base/Brand Guildeline.pdf` is the
     authority. If any surface disagrees with it, the surface is wrong. Do not treat
     a colour that shipped in a prototype as evidence that it is brand.

4. **The app's red was close but not exact, and that counted as drift too.**
   - The prototype CTA gradient was `#ff7b6b` to `#e8423a`. The brand ramp is
     `#FC7E84` to `#E24048`. Near enough to look right in isolation, wrong when
     placed next to a correctly built asset.
   - **How to apply:** never eyeball a brand colour. Copy the hex out of
     `core/brand-core.json` or `core/tokens.css`.

5. **Open, smaller: the Pro and Lite concept variants are still off brand on purpose.**
   `westretch-pro` uses purple `#7357d8`, `westretch-lite` uses coral `#e25d4f`.
   They are alternate product concepts for different audiences, so being visually
   distinct is the point. Left unchanged in the 2026-09-09 sweep. Karen has not
   said whether they should eventually come onto the brand core.

## Voice merged 2026-09-09

6. **`core/voice.md` is now the single source of truth for voice, company wide.**
   - Based on a staff writer's voice document submitted 2026-09-09, which was
     strong work. Most of it survived intact, including the "if you can film the
     sentence it's specific enough" test and the "when writing starts sounding
     written" anti-formula section, both of which had no equivalent in the repo.
   - Karen approved three corrections before the merge:
     1. **Guilt versus loss aversion, scoped not retired.** Her standing FOMO
        conversion lever survives, reframed from what the reader loses to what
        they keep. See "Progress is an asset, not a debt".
     2. **"Evolves with you" kept, explanation replaced.** The draft's "builds
        from your body" and "keeps adapting as you go" was the banned
        observational-learning framing. Now the prescriptive physio version.
     3. **Ada and Bruce added.** The draft never mentioned them. Bruce is marked
        as the single scoped exception to the hype restraint, in-app celebration
        beats only, never acquisition and never to someone in pain.
   - Smaller alignments: "physio-informed" became **physio backed**; "generally
     over fifty" became **50 to 65**; "tracking" retired alongside "learning";
     the inserted-name comma rule carried in; a Product copy channel section
     added because the draft only covered marketing surfaces.

7. **Three tiers of file. Karen caught the duplication that made this necessary.**
   - **Why:** the first version of `.agents/product-marketing.md` (2026-09-09) was
     189 lines and restated roughly 120 lines of `core/voice.md`: the audience,
     the banned word lists, the film test, Ada and Bruce, the tone rule. Karen
     asked the same day whether it was a duplicate of the voice file. It was.
     Two copies of one fact is exactly how the green palette drifted from the
     red brand book, and how two voice documents nearly diverged.
   - **The structure now:**
     - **Authority.** One home per fact: `core/voice.md` (voice, tone, audience,
       banned words), `core/positioning.md` (product, differentiation,
       competitors, objections, proof, targets), `core/tokens.css` (colour, type).
     - **Bootstrap.** Auto-loaded by a harness, so a short rule floor plus
       pointers is deliberate insurance: root `CLAUDE.md` and `AGENTS.md`.
     - **Router.** Pointers only, zero content: `.agents/product-marketing.md`,
       cut from 189 lines to 51.
   - **`core/positioning.md` was created in this pass** to give the product
     marketing facts a real home in the repo, rather than living inside
     `.agents/` where a package update could take them.
   - **How to apply:** change the authority file, never the bootstrap or router.
     The router gains a line only when a new destination exists, never when a
     fact changes. The four rules repeated in the router (em dashes, no learning
     claim, no blame, no age framing) are a deliberate floor because the cost of
     missing one is a shipped mistake; the router says explicitly that
     `core/voice.md` wins if they ever differ.

8. **`.agents/product-marketing.md` is the bridge to the third-party skill pack.**
   - **Why this matters:** 49 of the installed Corey Haines skills open by
     reading that exact path for brand voice and customer language. Until
     2026-09-09 the file did not exist, so every one of them ran with zero
     WeStretch context.
   - **How to apply:** never edit the vendored `SKILL.md` files to inject
     context. They are overwritten on package update and are out of scope per
     the root `Memory.md` em dash rule. Put context in that one file instead.
   - It is a summary. `core/voice.md` is the authority. If they disagree,
     `core/voice.md` wins. Change it first, then update the summary.

9. **Non-Claude harnesses read `AGENTS.md`, not `CLAUDE.md`.**
   Karen asked (2026-09-09) that the context work in any harness. `AGENTS.md`
   at the repo root now carries the same pointer table and hard rules. Two
   stale facts were corrected while in there: the App Store path had moved to
   `App Store Specialist/`, and it still claimed folders were kebab-case when
   `NAMING-CONVENTION.md` has said Title Case With Spaces since 2026-08-21.
   Keep `AGENTS.md` and `CLAUDE.md` in step.

