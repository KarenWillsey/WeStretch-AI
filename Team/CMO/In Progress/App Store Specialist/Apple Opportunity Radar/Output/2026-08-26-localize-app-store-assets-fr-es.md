Addresses backlog item: "Localize App Store assets for English, French, and Spanish."
Date: 2026-08-26 (scheduled nightly run)

## Scope note (read this first)

"App Store assets" spans two different things, and only one of them currently
exists in English to localize:

1. **Screenshot / app preview video copy**: exists (see `App Store Image
   Text Copywriting/Output/Default/app-store-copy-default-cold-audience.md`).
   Translated below into French and Spanish.
2. **Product page metadata**: app name, subtitle, keyword field, and
   long-form description; **does not exist yet in English.**
   `App Store Description Copywriting/` is confirmed empty (a stub, per its
   own `CLAUDE.md`). There is nothing to localize because there is no source
   copy. This part of the item is blocked, not done; see "What's still
   blocked" below. A new backlog item has been added for it.

So this run delivers a complete localization of the screenshot/video copy
(the only English App Store asset copy that currently exists), and flags
the metadata gap rather than skipping past it.

Per `Knowledge Base/apple-marketing-opportunities.md`: "Localize metadata
for English, French, and Spanish" (App Store Listing) and "Localize
screenshots for each supported language" (Screenshots and Videos), both
apply here; French and Spanish were the two markets Karen specified.

Translations follow the brand voice guardrails in `Team/CMO/skills/
westretch-core/references/strategic-thesis.md`: second person, no em
dashes, no fabricated outcomes/stats/testimonials, no fear/urgency framing.
Register: formal "vous" in French and "tú" in Spanish (informal but
standard for consumer app marketing), **flagging "tú" vs. "usted" as an
open call for Karen/CMO**, since the WeStretch ICP skews 50+ and "usted"
may read as more respectful for that audience in some Spanish-speaking
markets. Easy to swap once decided; noted so it isn't silently baked in.

---

## App preview video, 7 title cards

| # | English | French | Spanish |
|---|---|---|---|
| 1 | You're not 20 anymore. Your app shouldn't pretend you are. | Vous n'avez plus 20 ans. Votre appli ne devrait pas faire semblant. | Ya no tienes 20 años. Tu aplicación no debería fingir que sí. |
| 2 | A routine for your body. Not a template for everyone. | Une routine pour votre corps. Pas un modèle pour tout le monde. | Una rutina para tu cuerpo. No una plantilla para todos. |
| 3 | Physiotherapist-mapped movement, personalized for you. | Des mouvements cartographiés par un physiothérapeute, personnalisés pour vous. | Movimientos mapeados por un fisioterapeuta, personalizados para ti. |
| 4 | Tell it what hurts. It works around it. | Dites-lui ce qui vous fait mal. Elle s'adapte. | Dile qué te duele. Ella se adapta. |
| 5 | No sketch, no timer. Ada shows every move, live. | Pas de croquis, pas de minuteur. Ada montre chaque mouvement, en direct. | Sin bocetos, sin cronómetro. Ada muestra cada movimiento, en vivo. |
| 6 | Every session adapts to your body, your time, your goals. | Chaque séance s'adapte à votre corps, votre temps, vos objectifs. | Cada sesión se adapta a tu cuerpo, tu tiempo y tus objetivos. |
| 7 | Give it honest minutes a day. Two weeks. Feel it yourself. | Accordez-lui quelques minutes honnêtes par jour. Deux semaines. Ressentez la différence par vous-même. | Dedícale unos minutos honestos al día. Dos semanas. Siéntelo tú mismo. |

## Still screenshots, title + subtitle

| Screen | English | French | Spanish |
|---|---|---|---|
| 2 | **Not another one-size-fits-all fitness app**<br>Answer a few questions. It builds a routine for your body. | **Pas une appli de fitness universelle de plus**<br>Répondez à quelques questions. Elle crée une routine pour votre corps. | **No es otra app de fitness genérica**<br>Responde algunas preguntas. Ella crea una rutina para tu cuerpo. |
| 3 | **Physio-informed, every pose**<br>Licensed physiotherapists mapped safe movement for real joints. | **Informée par la physiothérapie, à chaque posture**<br>Des physiothérapeutes agréés ont cartographié des mouvements sûrs pour de vraies articulations. | **Con base fisioterapéutica, en cada postura**<br>Fisioterapeutas licenciados mapearon movimientos seguros para articulaciones reales. |
| 4 | **Works around your problem areas**<br>Tell it what hurts or what to avoid. It adjusts. | **S'adapte à vos zones sensibles**<br>Dites-lui ce qui vous fait mal ou ce qu'il faut éviter. Elle s'ajuste. | **Se adapta a tus zonas problemáticas**<br>Dile qué te duele o qué evitar. Ella se ajusta. |
| 5 | **Guided step by step**<br>Ada shows you every move. No guessing, no keeping up. | **Guidée étape par étape**<br>Ada vous montre chaque mouvement. Pas de suppositions, pas besoin de suivre le rythme. | **Guiada paso a paso**<br>Ada te muestra cada movimiento. Sin adivinar, sin tener que seguirle el ritmo. |
| 6 | **Fits the time you have**<br>A few minutes counts. You pick the length. | **S'adapte au temps que vous avez**<br>Quelques minutes suffisent. Vous choisissez la durée. | **Se ajusta al tiempo que tengas**<br>Unos minutos ya cuentan. Tú eliges la duración. |
| 7 | **It evolves with you**<br>Your routine adapts to your goals, your body, and your history. | **Elle évolue avec vous**<br>Votre routine s'adapte à vos objectifs, votre corps et votre historique. | **Evoluciona contigo**<br>Tu rutina se adapta a tus objetivos, tu cuerpo y tu historial. |
| 8 | **Start exactly where you are**<br>No flexibility required. No experience needed. | **Commencez exactement là où vous en êtes**<br>Aucune souplesse requise. Aucune expérience nécessaire. | **Empieza exactamente donde estás**<br>No se necesita flexibilidad. No se necesita experiencia. |
| 9 | **See what two weeks feels like** (no subtitle) | **Découvrez l'effet de deux semaines** | **Descubre cómo se siente en dos semanas** |

---

## Next step for this copy (asset-shaped, routing elsewhere)

This is translated copy only: not rendered screenshot/video assets. To
actually ship localized App Store images:

1. Hand this table to `Team/CMO/In Progress/App Store Specialist/App Store
   Image Creation/` (the screenshot build pipeline) as the French and
   Spanish text source, alongside the existing English source file.
2. Confirm the pipeline's fonts render French/Spanish accented characters
   (é, è, à, ê, ç, ñ, í, ó, ú) correctly before batch-generating, not
   verified in this run, no image-rendering access from here.
3. Re-check translated line lengths against whatever layout constraints
   the image templates use; French in particular tends to run ~15-20%
   longer than English and may wrap differently than the English source
   was designed for.

## What's still blocked

No English app name, subtitle, keyword-field content, or long-form
description exists anywhere in the repo, confirmed via `App Store
Description Copywriting/` (empty stub) and `Ideas/App Stores/App Store
Keyword Creation/` (empty). Localizing metadata that doesn't exist yet
isn't possible. Added to the backlog:

> Draft English App Store product page metadata (name ≤30 chars, subtitle
> ≤30 chars, keyword field ≤100 chars, promotional text ≤170 chars,
> long-form description), prerequisite for localizing product page
> metadata into French and Spanish. See `Knowledge Base/apple-marketing-
> opportunities.md` "App Store Listing" section for the field limits and
> rules.

Once that exists, a future nightly run can localize it the same way this
run localized the screenshot copy.
