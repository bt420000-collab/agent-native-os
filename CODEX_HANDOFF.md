# Codex Handoff

## Current release

```txt
Agent-Native OS v0.2.13
Codename: Official Novel Skill App
```

## Repository identity

Agent-Native OS is a spec-first, natural-language-first operating system architecture for long-running AI agents and installable Skill Apps.

Python scripts are runnable reference helpers for workspace initialization, validation, App installation, and Host command mediation. They are not the core implementation language.

## v0.2 key decisions

- The OS has exactly one persistent Host: `ano.host`.
- Apps are mounted Skill Apps, not Hosts.
- Apps may define coordinators, but coordinators only request resources.
- Subagent lifecycle is owned by the OS Host.
- Apps must submit Context Permission Requests before running.
- The OS prints Agent Runtime Approval Cards before App execution.
- Users may modify Agent rosters in natural language.
- Approved user changes are persisted as user-defined context.
- Cross-App Bridges are required for App-to-App data flow.
- Official reference Apps are optional ZIP packages staged in the App Package Inbox.
- The v0.2.13 workspace uses `ano/`, `user/`, `apps/`, `res/`, and `out/`.
- Installed workspaces must not use `.agent-os/` or `skills/`.

## Current official reference Apps

- Calculator Skill App v0.1.2
- Tiandao Furnace Skill App v0.4.0
- Novel Skill App v0.3.1

## Validation

Run from a fresh authorized directory:

```bash
python /path/to/agent-native-os/scripts/init_workspace.py
python ano/scripts/validate_workspace.py
python ano/scripts/list_app_packages.py
python ano/scripts/ano_host.py "列出应用"
```

Expected result: the workspace skeleton passes, optional official App packages are detected but remain uninstalled, and all App commands continue through the ANO Host gate.
