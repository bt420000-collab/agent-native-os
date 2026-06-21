# Changelog

## v0.2.8 - Tiandao Staged Interaction Fix

- Updated bundled Tiandao Furnace app to v0.4.0.
- Fixed the staged interaction problem where external agents could wait for the user to say “continue”; app responses now include `next_user_prompt` and `agent_instruction`.
- Added mandatory previous-draw intake as the first Tiandao runtime stage. The app may request ANO Host web lookup via `host_tool_request`, but never searches directly.
- Added overflow-safe user choices. If a user selects more options than suggested, extras become “炉边余炭” and the flow continues.
- Added feng-shui/weather/direction top-up flow and `tiandao.geomancy_agent` as an official multi-agent demo role.
- Added current-weather lookup request support through ANO Host tool mediation.
- Kept all lottery-like behavior entertainment-only: no prediction claims, no odds improvement, no betting advice.

## v0.2.7 - OS Host Command Gate

- Added hard rule: after OS installation, all user instructions are mediated by the ANO Host/Admin Agent.
- Added `ano_host.py` command gate helper.
- Added OS Agent Command Gate kernel document in installed workspaces.
- Updated bundled Tiandao Furnace app to v0.3.1, which blocks direct one-shot `ritual` execution and requires `open -> stop -> start --yes -> answer` staged flow.
- Updated installation completion notice to tell agents to stop and route future instructions through ANO Host.
- Added docs/spec for OS Host command mediation.

## 0.2.6 - Current Root Install Stop Point

- Enforced current-directory installation: ANO no longer creates or recommends child workspace folders.
- Removed deprecated installer examples that used separate workspace path arguments.
- OS initialization now stops after staging official app packages and explicitly returns control to the user.
- App package installation is preview-only by default and no longer blocks on an interactive yes/no prompt.
- Added post-install app installation guide and basic operation commands to the workspace README and installer output.
- Validator now rejects nested workspace folder names such as `ano-workspace` and `my-workspace`.


## 0.2.5 - Optional App Package Inbox

- Added the App Package Inbox standard: pending Skill App ZIP packages live under `apps/_inbox/official/` or `apps/_inbox/community/`.
- Changed official demo apps from embedded app folders to optional ZIP packages under `app_packages/official/`.
- Updated workspace initialization to stage official app packages without installing them.
- Added runtime scripts copied into initialized workspaces: `ano/scripts/list_app_packages.py`, `ano/scripts/install_app_package.py`, and `ano/scripts/validate_workspace.py`.
- Added `ano/kernel/APP_PACKAGE_INBOX.md`, `docs/16_app_package_inbox.md`, and `spec/app-package-inbox.schema.md`.
- Confirmed the developer flow: install mother system first, list pending app packages, then install each Skill App by user approval.

## v0.2.4 - Tiandao Furnace Ritual Demo

### Changed

- Updated official `ano-tiandao-furnace-skill-app` to v0.2.0.
- Restored original-style staged furnace flow: ask questions, raise heat, then open.
- Added visible subagent trace for every Tiandao subagent.
- Added oracle-style `tiandao.oracle_interpreter` agent for entertainment-only furnace interpretation.
- Added `tiandao.heat_questioner` for dynamic batch questions based on current state.
- Added `tiandao.heat_gatekeeper` requiring furnace heat to reach 75% before sampling.
- Changed `sample` command into a heat-gated compatibility alias, preventing direct result bypass.

### Safety

- Retained entertainment-only boundary: no prediction claims, no odds improvement claims, no betting advice.


## 0.2.3 - Multi-Agent Demo App

- Added `ano-tiandao-furnace-skill-app` as an official free multi-agent Skill App demo.
- Demonstrates app-level coordinator plus multiple subagents under ANO Host scheduling.
- Preserves uploaded Tiandao Hash Furnace React/Vite source under the app's `web_src/source/`.
- Adds entertainment-only safety framing: no prediction claims, no betting advice, no probability-improvement claims.


## 0.2.2 - Clean Workspace Filesystem

- Added the installed workspace filesystem standard: `ano/`, `user/`, `apps/`, `res/`, `out/`.
- Replaced legacy installed workspace paths `ano/` and `apps/` with `ano/` and `apps/`.
- Added `ano/kernel/FILESYSTEM_STANDARD.md` for initialized workspaces.
- Updated `scripts/init_workspace.py` to create a clean user workspace and move unknown root clutter into `user/imports/_unsorted/`.
- Updated `scripts/validate_workspace.py` to reject legacy `ano/` and `apps/` roots.
- Updated the official calculator app to install into `apps/` and `ano/runtime/apps/`.
- Added `docs/15_workspace_filesystem_standard.md` and `spec/workspace-filesystem.schema.md`.


## 0.2.1 - First Official Free App Catalog

- Added the first free reference Skill App, later repackaged as an optional app ZIP in v0.2.5.
- Added `OFFICIAL_APPS.md` to document official first-party apps.
- The calculator app demonstrates the v0.2 Single Host Runtime app contract with zero default subagents, tiny context budget, explicit install prompt, runtime approval card, and sandboxed workspace permissions.


## v0.2.0 - Single Host Runtime

This release reorganizes Agent-Native OS around a true operating-system model.

### Added

- Defined the **Single OS Host** principle: the Host belongs to the mother system and is always persistent.
- Defined **Skill Apps as mounted applications**, not independent hosts.
- Added **Context Permission Request** as the required pre-run memory/context/resource application.
- Added **Agent Runtime Approval Card** so the system can print the proposed agent roster before app execution.
- Added **User-Defined Agent Topology** for natural-language customization of app roles and persistent user context.
- Added **Cross-App Bridge** for OS-approved app-to-app data exchange.
- Added **Process Table**, **Context Allocations**, **Event Bus**, and **Bridge Registry** runtime concepts.
- Added app monetization metadata: apps may be free, open-source, paid, freemium, subscription, or commercial.
- Added `APP_DEVELOPER_GUIDE.md` as the standard guide for external Skill App developers.
- Added new templates for app manifests, context requests, runtime approval, user customization, and bridge requests.
- Added new spec documents for context permission requests, runtime plans, and cross-app bridges.

### Changed

- Updated repository version to `0.2.0`.
- Updated README and README.zh-CN to focus on the app ecosystem instead of bundled demos.
- Updated `scripts/init_workspace.py` to initialize the v0.2 runtime skeleton.
- Updated `scripts/validate_workspace.py` to validate the v0.2 workspace structure.
- Updated `SPEC.md`, `ROADMAP.md`, and Skill App manifest schema for the new Host/App/Subagent model.

### Removed

- Removed legacy demo workspaces from `examples/`.
- Removed `scripts/run_docs_brief_demo.py`.

Demos will be rebuilt later as standard installable Skill Apps using the `ano-*-skill-app` format.

## v0.1.0 - Specification Seed

Initial specification seed.

Included:

- Manifesto
- Core specification
- Roadmap
- Codex handoff
- Templates
- Spec documents
- Example workspaces
- Bootstrap script
