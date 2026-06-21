# Roadmap

## v0.1: Specification Seed

Status: complete.

Goals:

- Define Agent-Native OS theory.
- Define Context Kernel.
- Define Skill App Runtime.
- Provide templates.
- Provide specification documents.
- Provide early sample workspaces.

## v0.2: Single Host Runtime

Status: current.

Goals:

- Define that the OS has exactly one persistent Host.
- Move app-level "host" concepts into app-level coordinators.
- Require apps to submit Context Permission Requests before running.
- Define OS-owned subagent lifecycle control.
- Define Process Table, Context Allocation, Event Bus, and Cross-App Bridge concepts.
- Define User-Defined Agent Topology and Runtime Approval Cards.
- Define open-core/free-system plus app-developer ecosystem model.
- Remove legacy demos and prepare future demos as standard `ano-*-skill-app` packages.

Validation commands:

```bash
python scripts/init_workspace.py
python ano/scripts/validate_workspace.py
```

## v0.2.1: App Manifest and CPR Schema Tightening

Goals:

- Convert draft schemas into stricter machine-checkable YAML/JSON schema files.
- Add manifest compatibility checks.
- Add permission scope checks.
- Add app package smoke-test helper.

## v0.3: Reference Installer and App Runtime CLI

Potential commands:

```bash
agent-os init
agent-os app inspect ./ano-novel-skill-app
agent-os app install ./ano-novel-skill-app
agent-os app run ano.skill.novel --task TASK-001
agent-os app list
agent-os process list
agent-os bridge list
agent-os validate
```

Goals:

- Provide a small reference CLI.
- Keep dependencies minimal.
- Support install cards, manifests, CPR approval, registry writes, and runtime skeleton checks.

## v0.4: Multi-App Scheduling and Bridge Runtime

Goals:

- Support concurrent app Runtime Plans.
- Add bridge request and approval records.
- Add event replay for debugging.
- Add resource throttling rules.

## v0.5: Multi-Agent Runtime Adapters

Potential adapters:

- Generic adapter spec
- Codex adapter
- ChatGPT adapter
- Claude adapter
- Local model adapter
- MCP/tool driver notes

Goal:

- Allow different agents to operate inside the same Agent-Native OS workspace.

## v1.0: Stable Open Architecture

Goals:

- Stable manifest schema.
- Stable CPR and Runtime Plan schemas.
- Stable task, handoff, audit, and recovery schemas.
- Reference implementation.
- Standard demo apps.
- Documentation site.
