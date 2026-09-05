# Ad/Analytics SDK Device-Fingerprinting Audit; Checklist

Backlog item: "Audit current ad/analytics SDKs against Apple's device-fingerprinting prohibition (Developer Program License Agreement), flag any SDK deriving identifiers from browser/device/location/network properties."

Date: 2026-09-04

## Why this is a checklist, not a completed audit

This skill runs against the WeStretch-AI business-planning repo, which does
not contain the production native app's source or dependency manifest.
`Team/CXO/In Progress/Westretch-UX` (the only app-shaped codebase in this
repo) is a static UX prototype/demo (React + Vite, `lucide-react` as its
only real dependency); it has no ad or analytics SDKs and is not the
shipping app. There is no App Store Connect or production-codebase access
from here. So this item can't be confirmed from this repo; it needs to be
run against the actual native app's build.

## The rule being checked

Per Apple's Developer Program License Agreement (see Knowledge Base,
`apple-marketing-opportunities.md` line ~398): device fingerprinting is
prohibited, an app/SDK may not derive an identifier from browser
properties, device configuration, location, or network connection to
uniquely identify a device, and may not use hashed email/phone numbers as
a tracking identifier without App Tracking Transparency (ATT) permission.

## Checklist; for whoever has access to the production app repo/build

1. **List every third-party ad and analytics SDK actually compiled into
   the shipping app.** Check the native project's dependency manifest
   (`Podfile`/`Podfile.lock` for iOS, `build.gradle` for Android, or the
   React Native/Flutter `package.json` if cross-platform), not just
   what's referenced in marketing docs.
2. **For each SDK, check its documented identifier strategy:**
   - Does it use IDFA (via ATT) only, or does it fall back to a
     fingerprint-derived ID when ATT is denied/not requested? (The
     fallback is the prohibited part; many SDKs did this pre-2021 and
     some still offer it as an opt-in "probabilistic matching" feature
     that must be disabled.)
   - Does it hash email/phone/device attributes client-side and send that
     hash as a tracking identifier? If yes, confirm it only fires after
     ATT consent, or remove it.
   - Does it read device model, OS build, screen resolution, battery
     level, installed fonts, or IP/network info specifically to compose a
     device signature? (Legitimate crash/perf diagnostics use is fine;
     using the same data to build a persistent cross-app identifier is
     not.)
3. **Check ATT gating in code:** confirm tracking-capable SDK
   initialization (or at least the tracking-relevant calls within it) is
   deferred until after `ATTrackingManager.requestTrackingAuthorization`
   returns `.authorized`, and that denial actually suppresses tracking
   calls rather than silently falling back to a fingerprint.
4. **Check SDK privacy manifests (`PrivacyInfo.xcprivacy`):** as of recent
   App Store Connect requirements, required-reason APIs (e.g. UserDefaults,
   disk space, active keyboard, system boot time; several of which are
   also fingerprinting vectors) must be declared with an approved reason
   per SDK. Confirm every third-party SDK ships one, or that the app
   supplies one on the SDK's behalf.
5. **Pass/fail bar:** no SDK derives or receives a device/browser/
   location/network-based identifier for cross-app tracking purposes
   without prior ATT consent, and no SDK's fingerprinting fallback path is
   enabled.

## What "pass" looks like

A short written confirmation (or a marked-up SDK list) stating, per SDK:
name, version, tracking-identifier method used, ATT-gated (yes/no), and
privacy-manifest present (yes/no). Anything that fails step 5 needs a
remediation ticket (disable the fallback, add ATT gating, or remove the
SDK) before it's a compliance risk worth flagging to Apple review.

## Related backlog item

The Knowledge Base (2026-09-01 entry) flags that Apple's expanding
software-supply-chain integrity requirements (SDK signatures, privacy
manifests) should be folded into this same audit surface. That's tracked
as its own not-yet-worked backlog item ("Fold privacy-manifest and
SDK-signature verification into the existing ad/analytics SDK audit
item..."), steps 4 above already anticipates it, but the full signature-
verification pass is separate scope.
