# Third-Party SDK Audit v2: fingerprinting + privacy manifests + SDK signatures

Backlog item: "Fold privacy-manifest and SDK-signature verification into the existing ad/analytics SDK audit item; Apple is expanding software-supply-chain integrity requirements for third-party SDKs."

Date: 2026-09-09

**This supersedes [2026-09-04-ad-analytics-sdk-fingerprinting-audit-checklist.md](2026-09-04-ad-analytics-sdk-fingerprinting-audit-checklist.md).**
That checklist covered one of the three rules below. Run this file instead; it
is the same audit surface, done once.

## Why this is still a checklist, not a completed audit

Unchanged from 2026-09-04, and re-verified this run: this repo contains no
native app source and no dependency manifest. A search for `Podfile*`,
`*.xcodeproj`, `build.gradle`, `pubspec.yaml`, and `PrivacyInfo.xcprivacy`
across the whole repo (both submodules included) returns **nothing**.
`Team/CXO/In Progress/Westretch-UX` is a React/Vite UX prototype, not the
shipping app. Nobody can answer these questions from here; whoever holds the
iOS project has to.

What *is* new this run: the live App Store privacy label is publicly readable,
and it gives the audit a hard pass/fail anchor it did not have before. See
"The declared baseline" below.

## The declared baseline (read live from the storefront, 2026-09-09)

WeStretch's **App Privacy** label on `apps.apple.com/us/app/id1458915362`
currently declares:

| Section | Declared value |
|---|---|
| Data Used to Track You | **absent — nothing declared** |
| Data Linked to You | **absent — nothing declared** |
| Data Not Linked to You | Usage Data → "Other Usage Data" |

That is close to the minimum a paid-subscription app can declare. It is the
audit's yardstick: **every finding below is a pass only if it stays consistent
with that label.** If any SDK in the build tracks, or collects a data type not
listed, the label is wrong — and an inaccurate privacy label is itself a
review-rejection and App Store removal risk, independent of the SDK rules.

Note the asymmetry in effort: the label is cheap to widen and expensive to be
wrong about. Do not "fix" a mismatch by broadening the label reflexively;
first confirm the SDK is actually doing the thing.

## The three rules, one audit

### Rule 1 — no device fingerprinting (Developer Program License Agreement)

An app or SDK may not derive an identifier from browser properties, device
configuration, location, or network connection to uniquely identify a device,
and may not use a hashed email/phone as a tracking identifier without App
Tracking Transparency (ATT) consent. IDFV is the allowed exception, for
analytics across WeStretch's own apps only.

### Rule 2 — privacy manifests (`PrivacyInfo.xcprivacy`)

- **Since 2024-05-01:** an upload is **blocked** if the app's own code uses a
  required-reason API without an approved reason declared in its privacy
  manifest. This is a hard upload gate, not a warning.
- **Since 2025-02-12:** a new app, or an update that *adds* a
  privacy-impacting SDK, must ship that SDK's privacy manifest. Missing one
  triggers an **ITMS-91061 "Missing privacy manifest"** email from App Store
  Connect naming the offending SDK and its path in the bundle.
- Manifest keys, for the reviewer's eye: `NSPrivacyTracking` (Bool),
  `NSPrivacyTrackingDomains` (array), `NSPrivacyCollectedDataTypes` (array of
  dicts with `NSPrivacyCollectedDataType`, `...Linked`, `...Tracking`,
  `...Purposes`), `NSPrivacyAccessedAPITypes` (array of dicts with
  `NSPrivacyAccessedAPIType` + `NSPrivacyAccessedAPITypeReasons`).
- Required-reason API categories to expect: file timestamp, system boot time,
  disk space, active keyboards, `UserDefaults`. Several of these double as
  fingerprinting vectors, which is exactly why Rules 1 and 2 belong in one pass.

### Rule 3 — SDK signatures

When a listed SDK is included as a **binary** dependency, it must be signed by
its vendor. Source-built dependencies (e.g. CocoaPods compiled from source)
are not covered by the signature half, but are still covered by the manifest
half. Apple's list names 86 commonly-used SDKs; any version of a listed SDK
counts, and so does anything that **repackages** one.

## The checklist — for whoever has the iOS project

**Step 0. Establish the stack first.** Apple's 86-SDK list clusters by
ecosystem, so the answer determines where to look:

- **Flutter** → `pubspec.lock`. High-hit entries: `Flutter`,
  `flutter_inappwebview`, `flutter_local_notifications`, `path_provider`,
  `shared_preferences_ios`, `package_info_plus`, `device_info_plus`,
  `connectivity_plus`, `url_launcher_ios`, `image_picker_ios`, `sqflite`,
  `video_player_avfoundation`, `share_plus`, `geolocator_apple`, `wakelock`,
  `webview_flutter_wkwebview`, `file_picker`, `fluttertoast`.
- **React Native** → `package.json` + `Podfile.lock`. High-hit: `hermes`,
  `Firebase*`, `Reachability`, `SDWebImage`, `Lottie`.
- **Native Swift/ObjC** → `Podfile.lock` / SPM `Package.resolved`. High-hit:
  `Alamofire`, `Firebase*`, `GoogleUtilities`, `GoogleSignIn`, `Kingfisher`,
  `SnapKit`, `SDWebImage`, `Lottie`, `RxSwift`, `IQKeyboardManager`,
  `RealmSwift`, `OneSignal*`, `FBSDK*`.
- **Capacitor / Cordova / Unity** → `Capacitor`, `Cordova`, `UnityFramework`
  are each on the list in their own right.

WeStretch's 418.9 MB bundle and iOS 15.2 minimum say nothing about the stack
either way; do not guess, read the lockfile.

**Step 1. Produce the real dependency inventory.** Every third-party binary and
source dependency actually compiled into the shipping build — from the
lockfile, not from a README or a marketing doc.

**Step 2. Cross-reference against Apple's list.** Mark each dependency
present-on-list / not-on-list. Check for repackaging: an internal wrapper pod
that vendors `Firebase` still counts as `Firebase`.

**Step 3. For every on-list dependency, confirm three things:**

   a. the version ships a `PrivacyInfo.xcprivacy` — many vendors added theirs
      in a specific minimum version, and an old pinned version is the usual
      failure mode;
   b. if it is a binary/xcframework, it carries a valid vendor signature;
   c. its declared `NSPrivacyCollectedDataTypes` / `NSPrivacyTracking` are
      consistent with WeStretch's public label above.

**Step 4. Audit the app's own manifest.** WeStretch's own target needs its own
`PrivacyInfo.xcprivacy` declaring required-reason APIs used by first-party
code. `UserDefaults` alone catches nearly every app.

**Step 5. Rule 1 pass on the ad/analytics subset** (carried forward from the
v1 checklist, still required):

   - IDFA only via ATT, with **no** probabilistic-matching / fingerprint
     fallback enabled when ATT is denied;
   - no client-side hashed email/phone sent as a tracking identifier without
     ATT consent;
   - device model / OS build / screen resolution / battery / fonts / IP read
     for diagnostics is fine; composing them into a persistent cross-app
     identifier is not;
   - tracking-capable SDK init deferred until `ATTrackingManager.requestTrackingAuthorization`
     returns `.authorized`, and denial actually suppresses the calls.
   - **Broad definition of tracking:** an SDK that combines WeStretch's data
     with other companies' data for ad targeting or measurement counts as
     tracking requiring ATT **even if WeStretch never uses it that way**. The
     SDK's behaviour is what is judged. Same rule inside an in-app webview.

**Step 6. Generate the Privacy Report in Xcode** (Archive → Generate Privacy
Report). It aggregates every manifest in the bundle into one document. Diff
that document against the live App Store label from "The declared baseline."
**Any line in the report not represented in the label is the finding.**

## What "pass" looks like

One table, filled in, one row per dependency:

| SDK | Version | On Apple's list? | Binary or source | Privacy manifest present | Signed | Declares tracking | ATT-gated | Matches live label |
|---|---|---|---|---|---|---|---|---|

Plus a one-line verdict: *"Xcode Privacy Report matches the live App Store
privacy label"* — or a list of the mismatches, each with a remediation ticket
(bump the SDK version, disable the fingerprint fallback, add ATT gating, drop
the SDK, or correct the label).

## Timing note — this matters more than it looks

The manifest/signature requirements bite **on upload of a new app or an update
that adds a listed SDK**. WeStretch already ships, so a build that changes no
dependencies is unlikely to be blocked today. The trap is that the next update
which happens to add or bump one listed SDK inherits the full requirement, and
finds out at upload time via ITMS-91061 — i.e. at the worst possible moment,
mid-release. **Run this audit on a quiet week, not during a release.**

## Incidental finding — not this item, flagging for the Manager

The same storefront fetch shows, under Accessibility: *"The developer has not
yet indicated which accessibility features this app supports."* **WeStretch's
Accessibility Nutrition Labels are entirely undeclared.** The Knowledge Base
(2026-08-21 entry) flags these as directly relevant to WeStretch's older-adult
positioning — users can filter the App Store by accessibility need, and
WeStretch currently appears in none of those filters. The 2026-08-31
accessibility checklist covered *meeting* the requirements; it did not catch
that the *declaration* is blank, because that field is not visible without
checking the live page. Nine categories are declarable. Recommend this becomes
a backlog item; not adding it myself, per this skill's "do not invent items" rule.

## Sources

- [Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/) — the 86-SDK list
- [Privacy updates for App Store submissions](https://developer.apple.com/news/?id=3d8a9yyh) — the May 1 upload gate
- [Adding a privacy manifest to your app or third-party SDK](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk) — key names
- [Handling ITMS-91061: Missing privacy manifest](https://developer.apple.com/forums/thread/774960) — the 2025-02-12 SDK manifest date
- Knowledge Base `apple-marketing-opportunities.md`, "Privacy and Customer Accounts" (2026-08-21 and 2026-09-01 entries)
- Live storefront `https://apps.apple.com/us/app/id1458915362`, fetched 2026-09-09
