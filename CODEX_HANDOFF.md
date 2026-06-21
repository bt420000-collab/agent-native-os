# Codex Handoff

## Current release

```txt
Agent-Native OS v0.2.8
Codename: Optional App Package Inbox
```

## Repository identity

Agent-Native OS is a spec-first, natural-language-first operating system architecture for long-running AI agents and installable Skill Apps.

Python scripts are reference helpers for workspace initialization and validation. They are not the core implementation language.

## v0.2 key decisions

- The OS has exactly one persistent Host: `ano.host`.
- Apps are mounted Skill Apps, not Hosts.
- Apps may define coordinators, but coordinators only request resources.
- Subagent lifecycle is owned by the OS Host.
- Apps must submit Context Permission Requests before running.
- The OS prints Agent Runtime Approval Cards before app execution.
- Users may modify agent rosters in natural language.
- Approved user changes are persisted as user-defined context.
- Cross-App Bridges are required for app-to-app data flow.
- Legacy demos were removed. Future demos should be standard `ano-*-skill-app` packages.
- v0.2.8 workspace filesystem uses `ano/`, `user/`, `apps/`, `res/`, and `out/`; installed workspaces must not use `.agent-os/` or `skills/`.

## Validation

```bash
python scripts/init_workspace.py
python ano/scripts/validate_workspace.py
python ano/scripts/list_app_packages.py
```

Expected result: workspace skeleton passes; optional official app packages are detected but not installed until user approval.
