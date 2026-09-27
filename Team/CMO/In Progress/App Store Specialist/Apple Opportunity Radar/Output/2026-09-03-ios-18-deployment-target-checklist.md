# Confirm iOS/iPadOS Deployment Target Supports iOS 18+; Checklist

Addresses backlog item: "Confirm WeStretch's minimum iOS/iPadOS deployment
target supports iOS 18+ before committing to deep-linked Custom Product
Pages."
Date: 2026-09-03 (nightly-action run)

## Why this matters

Per `Knowledge Base/apple-marketing-opportunities.md` → "Custom Product
Pages": deep links into the app from a Custom Product Page require iOS 18 /
iPadOS 18 or later. The 5 CPPs already planned in
[Output/2026-08-23-cpp-plan-5-pages.md](2026-08-23-cpp-plan-5-pages.md) each
have a deep-link target pending this confirmation; none of them can ship
their deep-link field until this is resolved. It does not block the pages'
screenshots, copy, or keyword targeting, which work today regardless.

## What this skill could not do

This skill has no App Store Connect access and no access to the app's
native build configuration. The `Westretch-UX` repo checked into this
project (`Team/CXO/In Progress/Westretch-UX`) is a Vite/TypeScript/Firebase
web codebase with no `ios/` folder, no Xcode project, and no
`app.json`/`eas.json`; it is not where the native iOS deployment target is
set, and `UNITY-HANDOFF.md` in that same repo (referencing a Unity-based
native build) has no deployment-target mentions either. Wherever the actual
native iOS project lives is outside what this skill can see. This checklist
is for whoever does have access to that project and/or App Store Connect.

## Checklist

1. **Find the native iOS project's minimum deployment target.**
   - If it's a native Xcode project: open the `.xcodeproj`/`.xcworkspace` →
     target → "General" tab → "Minimum Deployments," or grep
     `IPHONEOS_DEPLOYMENT_TARGET` in `project.pbxproj`.
   - If it's Unity-built (per `UNITY-HANDOFF.md` in the Westretch-UX repo):
     check **Unity → Build Settings → iOS → Player Settings → Other
     Settings → Target minimum iOS Version**, since this is what Unity
     writes into the generated Xcode project's deployment target at build
     time.
   - If it's a cross-platform wrapper (Capacitor/Cordova/React Native/
     Expo/Flutter) instead: check that framework's iOS config (e.g.
     `ios/Podfile` `platform :ios` line, or `app.json`/`eas.json`
     `ios.deploymentTarget`).
2. **Pass condition:** the value found is `18.0` or higher.
3. **If it's below 18.0**, two paths, not deciding this unilaterally:
   - Raise the minimum deployment target to iOS 18, check current
     install-base impact first (App Store Connect → App Analytics → App
     Store Engagement, or Xcode Organizer's OS-version adoption data) to
     see what % of the current user base would be cut off.
   - Or keep the lower minimum and ship the 5 CPPs without deep links for
     now (already the fallback recommended in the 2026-08-23 CPP plan),
     revisiting deep links once the install base has migrated further to
     iOS 18+.
4. **Once confirmed either way**, update the 5 CPP deep-link targets in
   [Output/2026-08-23-cpp-plan-5-pages.md](2026-08-23-cpp-plan-5-pages.md)
   accordingly (add real deep links, or explicitly mark them as withheld
   pending a future deployment-target bump) and note the decision in
   `Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Memory.md`
   so it doesn't get re-litigated on a future run.

## Status

Left in "Not started" on `Backlog.md`; this run could only produce the
checklist above, not a confirmed answer, since the native app's build
configuration is outside this skill's access. Needs a human (or an agent
with access to the actual native iOS project) to walk the checklist and
report back the deployment target value.
