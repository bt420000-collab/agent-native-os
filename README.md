# Agent-Native OS

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

A context-native operating system architecture for long-running AI agents and installable Skill Apps.

![Spec](https://img.shields.io/badge/spec-v0.2.8-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

<p align="center">
  <a href="./docs/assets/homepage/poster-not-human-desktop.png">
    <img src="./docs/assets/homepage/poster-not-human-desktop.png" alt="Not letting AI take over human computers, but giving AI its own computer" width="88%" />
  </a>
</p>

> **Not teaching AI to use human desktops.**  
> **Giving AI a computer of its own.**

Agent-Native OS is not an operating system for humans. It is a native operating layer for AI agents: a governed workspace where agents can install Skill Apps, request context, isolate workspaces, start subagents through the OS Host, hand off state, and keep long-running work coherent.

Informally, you can think of it as **the operating system layer for AI agents**.

## v0.2 focus: Single Host Runtime

Agent-Native OS v0.2 defines a cleaner ecosystem boundary:

```txt
Agent-Native OS Core = the persistent Host, runtime, scheduler, permissions, and standards
Skill App = an installable capability package mounted by the OS
Subagent = a worker started, paused, killed, or archived by the OS Host
```

The Host belongs to the mother system. Apps are not Hosts. Apps may define coordinators, but only the OS Host owns subagent lifecycle authority and global context scheduling.

## Core doctrine

```txt
Apps do not own context. Apps request context.
The Host owns context, agents, workspace permissions, and scheduling.
```

Before a Skill App runs, it must submit a **Context Permission Request**. The OS prints an **Agent Runtime Approval Card** showing the proposed agent roster, context budget, workspace permissions, cross-app bridges, and commercial status. The user can approve, reject, or modify the plan in natural language.

Example user override:

```txt
This novel may explode in the comments. Add a troll simulator agent.
```

The OS can persist that approved change as user-defined context and inherit it in future runs.

## What Agent-Native OS manages

- Single persistent OS Host
- Context Permission Requests
- Skill App installation and mounting
- Subagent scheduling and lifecycle
- Workspace permission sandboxing
- Process table and context allocations
- Event bus and recovery records
- Cross-App Bridges
- Output contracts and handoff reports
- User-defined Agent Topology

## Ecosystem model

Agent-Native OS Core should remain open-source, free, and continuously updated.

Skill Apps may be developed by official maintainers, community developers, private teams, or commercial vendors. Apps may be free, open-source, paid, freemium, subscription-based, enterprise-licensed, or privately deployed.

```txt
The system provides order.
Apps provide capability.
```

## Quick start

### Current-root rule

ANO v0.2.8 installs into the current authorized directory only. Do not create a child workspace directory. After OS initialization, stop and wait for the user before installing any Skill App.



Initialize a blank v0.2 workspace:

```bash
python scripts/init_workspace.py
```

Validate it:

```bash
python ano/scripts/validate_workspace.py
```

After initialization, list optional app packages staged in the workspace:

```bash
python ano/scripts/list_app_packages.py
```

Install an optional official app only after reviewing its install card:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/ano-calculator-skill-app_v0.1.2.zip
python ano/scripts/install_app_package.py apps/_inbox/official/ano-calculator-skill-app_v0.1.2.zip --yes
```


This repository does not auto-install demos. Official demo apps are staged as optional ZIP packages and must be installed by user approval after workspace initialization.


## v0.2.8 installed workspace filesystem, app inbox, and host gate

The development repository may contain docs, scripts, specs, templates, and official app ZIP packages. A user-installed ANO workspace must stay clean:

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

`ano/` is the system engine room, `user/` is user data, `apps/` contains installed Skill Apps and `apps/_inbox/` contains pending app packages, `res/` contains shared resources, and `out/` contains final exports. Legacy installed paths `.agent-os/` and `skills/` are forbidden after the clean workspace standard.

## Developer entry points

- [APP_DEVELOPER_GUIDE.md](APP_DEVELOPER_GUIDE.md) - standard Skill App development guide
- [SPEC.md](SPEC.md) - core v0.2 specification
- [VERSIONING.md](VERSIONING.md) - version definition and release rules
- [ECOSYSTEM.md](ECOSYSTEM.md) - open core and app ecosystem model
- [templates/APP_MANIFEST.yaml](templates/APP_MANIFEST.yaml) - app manifest template
- [templates/CONTEXT_PERMISSION_REQUEST.yaml](templates/CONTEXT_PERMISSION_REQUEST.yaml) - runtime resource request template

## Repository map

```txt
agent-native-os/
  README.md
  README.zh-CN.md
  SPEC.md
  ROADMAP.md
  CHANGELOG.md
  VERSIONING.md
  ECOSYSTEM.md
  APP_DEVELOPER_GUIDE.md
  CORE_THEORY_AND_GLOSSARY.md
  docs/
  spec/
  templates/
  scripts/
  app_packages/
    official/
```

## Suggested GitHub description

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

## Suggested topics

```txt
ai-agents
agent-os
agent-native
context-engineering
context-native
multi-agent
skill-apps
workflow-automation
agent-framework
ai-native
```

## License

Apache-2.0. See `LICENSE`.

## Official App Packages

The OS release may bundle optional official demo app ZIP packages under `app_packages/official/`. During workspace initialization they are staged into `apps/_inbox/official/`, but they are not installed automatically.

Current official packages:

- `ano-calculator-skill-app_v0.1.2.zip`
- `ano-tiandao-furnace-skill-app_v0.4.0.zip`

See [OFFICIAL_APPS.md](OFFICIAL_APPS.md).

## v0.2.8 OS Host Command Gate

After installation, every user instruction must be handled by the ANO Host/Admin Agent first. Do not bypass the OS by directly running app internals. Use:

```bash
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
```

The Host will resolve installation status, show permission/approval cards, and stop for user approval.


## Tiandao Furnace v0.4.0

The official multi-agent demo now starts with previous-draw intake, supports ANO Host web/weather lookup requests, handles overflow user choices without blocking, and adds feng-shui direction/weather/geography top-up. It remains entertainment-only and does not provide prediction or betting advice.
