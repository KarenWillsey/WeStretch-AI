# Image Catalogue

Approved CMO source images live here, flat (no subfolders needed unless the
catalogue grows large enough to warrant them). This is a source-image
archive, not a delivery folder — finished, sized App Store exports still go
through their own project `output/` folders (see `ada-stretching-phone-image`
and `app-store-image-creation`).

## How images get here

1. A source-image skill (`female-actor-01-image-generator`,
   `male-actor-01-image-generator`, `westretch-ada-image-gen`, or similar)
   saves its reviewed candidate to `Team/CMO/Review ToDo/` by default.
2. Karen reviews it there.
3. On approval, move the file from `Review ToDo/` into this folder. It stays
   here as reusable reference/source material for future generations and
   compositing.
4. If not approved, it does not move here — either discard it or keep
   iterating in `Review ToDo/`.

Keep filenames descriptive (character/subject, pose, setting) since this
folder has no per-project structure to provide that context.
