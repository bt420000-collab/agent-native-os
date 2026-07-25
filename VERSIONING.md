# Versioning Policy

Agent-Native OS follows semantic versioning for the public specification and reference workspace helpers.

## Current version

```txt
0.2.13
```

Codename: **Official Novel Skill App**

## Version meaning

```txt
MAJOR.MINOR.PATCH
```

- **MAJOR**: breaking changes to core OS concepts, manifest structure, or runtime contracts.
- **MINOR**: new OS capabilities, new standard contracts, or new developer-facing APIs.
- **PATCH**: documentation fixes, template corrections, validator improvements, or non-breaking clarifications.

## Stability levels

| Area | v0.2.13 status | Notes |
|---|---:|---|
| Single OS Host principle | stable draft | Apps must not own Host authority. |
| Skill App package naming | stable draft | Recommended format: `ano-<domain>-skill-app`. |
| Context Permission Request | draft | Required concept, schema may evolve. |
| Runtime Approval Card | draft | User-facing approval format. |
| User-defined Agent Topology | draft | Persistent customization model. |
| Cross-App Bridge | draft | Required for App-to-App cooperation. |
| Installed workspace filesystem | stable draft | Installed workspaces use `ano/`, `user/`, `apps/`, `res/`, `out/`. |
| App Package Inbox | stable draft | Pending App packages require user approval before installation. |
| CLI/reference implementation | experimental | Helper scripts are a runnable reference layer, not a production OS. |

## Release rule

A release should update:

1. `VERSION`
2. `CHANGELOG.md`
3. `PACKAGE_MANIFEST.json`
4. README version references
5. active helper-script version constants
6. any changed templates or schemas
7. CI smoke-test expectations

## 0.2.13 Official Novel Skill App

Current release. Adds the optional official Novel Skill App, ANO Host support for opening it, and Material Governance workflows while preserving the initialization and approval stop points.

## 0.2.8 OS Host Command Gate

Historical release. Added post-install OS Host/Admin Agent mediation for all user instructions and updated the official Tiandao demo to the hosted staged flow.

## 0.2.6 Current Root Install Stop Point

Historical patch release that forbids child workspace installation, makes App installation preview-only by default, and requires agents to stop after OS initialization.
