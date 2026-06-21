# Agent-Native OS Specification v0.2

Status: Draft  
Codename: Single Host Runtime

## 0. Normative foundation

Agent-Native OS is a context-native operating system architecture for long-running AI agents and installable Skill Apps.

The public core is grounded in five principles:

1. Context is the first-class resource.
2. Contracted natural language is source code.
3. Context Kernel is the runtime.
4. Structured output is the Context ABI.
5. Skill Apps are installable applications.

## 1. Single Host principle

Agent-Native OS has exactly one Host.

```txt
Host = the persistent OS-level controller owned by the mother system.
```

Skill Apps must not claim Host authority. They may define coordinators or workflow controllers, but only the OS Host owns lifecycle control over app runs, subagents, runtime permissions, context allocations, process state, and cross-app bridges.

## 2. System layers

```txt
Agent-Native OS
│
├─ OS Host
├─ Context Kernel
├─ Context Permission Manager
├─ Skill App Runtime
├─ Subagent Scheduler
├─ Workspace Permission Sandbox
├─ Cross-App Bridge Manager
├─ Process Table
├─ Event Bus
├─ Output Contract Engine
├─ Audit Gate
├─ Memory & Archive Layer
└─ Recovery System
```

## 3. Runtime hierarchy

```txt
User
  ↓
ANO Host
  ↓
Skill App / App Coordinator
  ↓
Subagents
```

The user is the highest instruction source. The OS Host is the persistent controller. Apps are mounted capability packages. Subagents are temporary or semi-persistent workers created only through OS authorization.

## 4. Context Permission Request

Before an app runs, it must submit a Context Permission Request.

The request declares:

- app id
- task id
- requested mode
- requested agent roster
- context budget
- workspace read/write scope
- denied paths
- cross-app bridge needs
- output contracts
- lifecycle expectations
- persistent user context writes

The OS Host may approve, deny, reduce, defer, pause, or kill the resulting Runtime Plan.

## 5. Skill App Runtime

A Skill App is an installable capability package.

Recommended package layout:

```txt
ano-<domain>-skill-app/
  manifest.yaml
  INSTALL_CARD.md
  README.md
  CHANGELOG.md
  LICENSE
  app_actions/
  roles/
  protocols/
  templates/
  tests/
```

Recommended naming:

```txt
package_name: ano-<domain>-skill-app
app_id: ano.skill.<domain>
```

A Skill App may define an app coordinator, but the coordinator is not the OS Host.

## 6. Subagent lifecycle

Recommended states:

```txt
CREATED
READY
RUNNING
WAITING
PAUSED
COMPLETED
FAILED
KILLED
ARCHIVED
```

Only the OS Host may transition a subagent into `RUNNING`, `PAUSED`, `KILLED`, or `ARCHIVED`.

## 7. User-defined Agent Topology

Before execution, the OS should display an Agent Runtime Approval Card. The user may modify the proposed agent roster in natural language.

Approved modifications are persisted as user-defined context.

Example:

```txt
Add a troll simulator agent because this novel may explode in the comments.
```

The OS should write the approved customization into the relevant user context profile and merge it into future Runtime Plans.

## 8. Cross-App Bridge

Apps must not directly read another app's private workspace.

When app cooperation is required, the OS Host creates a scoped Cross-App Bridge.

```txt
from_app/outbox/<packet>/
  ↓ approved bridge
to_app/inbox/<packet>/
```

Bridge access is task-scoped, path-scoped, and revocable.

## 9. Workspace structure

Agent-Native OS v0.2.2 defines a clean installed workspace root:

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

Directory roles:

```txt
ano/   system internals: Host policy, kernel docs, runtime, registry, scheduler state, events, locks, bridges
user/  user data: profiles, preferences, memory, projects, imports, app-specific customization
apps/  installed Skill App packages
res/   shared resources
out/   final user-facing outputs and exports
```

App install mapping:

```txt
apps/<package_name>/              # app package code
ano/runtime/apps/<app_id>/        # system-managed app runtime home
user/apps/<app_id>/               # user-defined app customization
ano/registry/apps/<app_id>.json   # registry record
out/<domain-or-app>/              # final outputs
```

Installed workspaces must not use the legacy v0.2.1 roots:

```txt
.agent-os/  # legacy forbidden
skills/     # legacy forbidden
```

Unknown root entries should be moved to `user/imports/_unsorted/` during installation or cleanup.

## 10. Ecosystem model

The Agent-Native OS core should remain open-source and free. Skill Apps may be free, open-source, paid, freemium, subscription-based, enterprise-licensed, or privately deployed.

Every app must declare its commercial model before installation.

## 11. Minimum viable v0.2 kernel

```txt
Agent OS v0.2 MVP
= Single Host
+ Skill App Manifest
+ Context Permission Request
+ Runtime Approval Card
+ Process Table
+ Workspace Permission Sandbox
+ Output Contract
+ Handoff Report
+ Event Bus
```

Recommended extensions:

```txt
+ Cross-App Bridge
+ User-defined Agent Topology
+ App Registry
+ Permission Lock
+ Context Allocation Log
+ Audit Gate
+ Recovery Point
```

## App Package Inbox

The mother system may bundle optional Skill App ZIP packages, but must not auto-install them. A freshly initialized workspace stages pending packages under `apps/_inbox/official/` or `apps/_inbox/community/`. The user installs each app explicitly after reviewing its install card.


## Current-root installation

ANO v0.2.8 installs into the current authorized workspace root only. The OS installer must not create a child workspace directory. OS initialization is a hard stop point: bundled app packages may be staged, but no Skill App may be auto-installed.

## OS Host Command Gate

In v0.2.8+, all post-install user instructions are mediated by `ano.host`. Apps cannot be directly launched by user-facing agents. A compliant App must support a permission-preview/open stage and must not run its main workflow until the Host-mediated approval is complete.
