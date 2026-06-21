# Versioning Policy

Agent-Native OS follows semantic versioning for the public specification and reference workspace helpers.

## Current version

```txt
0.2.8
```

Codename: **Optional App Package Inbox**

## Version meaning

```txt
MAJOR.MINOR.PATCH
```

- **MAJOR**: breaking changes to core OS concepts, manifest structure, or runtime contracts.
- **MINOR**: new OS capabilities, new standard contracts, or new developer-facing APIs.
- **PATCH**: documentation fixes, template corrections, validator improvements, or non-breaking clarifications.

## Stability levels

| Area | v0.2.8 status | Notes |
|---|---:|---|
| Single OS Host principle | stable draft | Apps must not own Host authority. |
| Skill App package naming | stable draft | Recommended format: `ano-<domain>-skill-app`. |
| Context Permission Request | draft | Required concept, schema may evolve. |
| Runtime Approval Card | draft | User-facing approval format. |
| User-defined Agent Topology | draft | Persistent customization model. |
| Cross-App Bridge | draft | Required for app-to-app cooperation. |
| Installed workspace filesystem | stable draft | Installed workspaces use `ano/`, `user/`, `apps/`, `res/`, `out/`. |
| App package inbox | stable draft | Pending app packages live in `apps/_inbox/` and require user approval before installation. |
| CLI/reference implementation | experimental | Helper scripts are not the OS itself. |

## Release rule

A release should update:

1. `VERSION`
2. `CHANGELOG.md`
3. `PACKAGE_MANIFEST.json`
4. README version references
5. any changed templates or schemas


## 0.2.8 OS Host Command Gate

Current release. Adds post-install OS Host/Admin Agent mediation for all user instructions and updates the official Tiandao demo to the hosted staged flow.

## 0.2.6 Current Root Install Stop Point

Patch release that forbids child workspace installation, makes app installation preview-only by default, and requires agents to stop after OS initialization.
