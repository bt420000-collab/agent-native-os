# Agent-Native OS Skill App Developer Guide

This guide defines the standard format for developing Skill Apps for Agent-Native OS v0.2.

## 1. Mental model

Agent-Native OS has exactly one Host:

```txt
Host = Agent-Native OS mother system
```

A Skill App is not a Host. A Skill App is an installable capability package mounted by the OS.

A Skill App may define a coordinator, but the coordinator is an app-level workflow controller only. It does not own subagent lifecycle authority.

```txt
User
  ↓
ANO Host
  ↓
Skill App / Coordinator
  ↓
Subagents
```

## 2. Naming standard

Recommended package name:

```txt
ano-<domain>-skill-app
```

Recommended app id:

```txt
ano.skill.<domain>
```

Examples:

```txt
ano-novel-skill-app        -> ano.skill.novel
ano-comic-skill-app        -> ano.skill.comic
ano-research-skill-app     -> ano.skill.research
ano-code-review-skill-app  -> ano.skill.code_review
```

## 3. Required package layout

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

Recommended optional files:

```txt
  PERMISSIONS.md
  PRICING.md
  SECURITY.md
  examples/
  migration/
```

## 4. Required manifest sections

Every app must declare:

- identity
- display information
- install prompt
- commercial model
- default context permission request
- agent policy
- workspace permissions
- lifecycle policy
- output contracts
- compatibility

See `templates/APP_MANIFEST.yaml`.

## 5. Context Permission Request

Before running, an app must submit a Context Permission Request.

The request tells the OS:

- requested mode
- requested subagents
- context budget
- workspace read/write scope
- cross-app bridge needs
- output contract
- persistent user context writes

The OS Host may approve, deny, reduce, pause, or kill the requested runtime plan.

Apps do not own context. Apps request context.

## 6. Agent Runtime Approval Card

The OS should print a user-facing approval card before executing an app run.

The approval card should show:

- app name
- task purpose
- planned agent roster
- requested context budget
- workspace permissions
- cross-app bridges
- user customizations
- commercial notice, if any

The user can approve, reject, or modify the plan in natural language.

## 7. User-defined Agent Topology

Users may customize an app's agent roster before execution.

Example:

```txt
Add a troll simulator agent because this novel may explode in the comments.
```

The OS should translate the approved modification into persistent user context, such as:

```txt
ano/runtime/apps/ano.skill.novel/user_context/agent_customization.yaml
```

The next run should merge:

```txt
App default manifest
+ global user profile
+ app user profile
+ project user profile
+ this-run user override
= Final Runtime Plan
```

## 8. Cross-App Bridge

Apps must not directly read another app's private workspace.

For app-to-app workflows, use an OS-approved bridge:

```txt
ano.skill.novel/outbox/adaptation_packet/
  ↓ approved by ANO Host
ano.skill.comic/inbox/adaptation_packet/
```

See `spec/cross-app-bridge.schema.md` and `templates/CROSS_APP_BRIDGE_REQUEST.yaml`.

## 9. Permissions

Allowed permissions are explicit. Everything else is denied by default.

Apps may request:

- read access to their own installed package
- read/write access to their own app workspace
- read/write access to task-specific project folders
- limited cross-app access via bridges

Apps must not request direct mutation of:

- `ano/kernel/`
- another app's private workspace
- OS registry files except through the installer
- runtime process tables except through OS APIs

## 10. Commercial declaration

Apps may be free or paid, but must say so before installation.

Manifest examples:

```yaml
commercial:
  pricing_model: free
  license: Apache-2.0
  payment_required: false
```

```yaml
commercial:
  pricing_model: subscription
  license: commercial
  payment_required: true
  trial_available: true
  trial_days: 7
```

## 11. What makes a good Skill App

A good Skill App:

- declares permissions honestly
- requests the smallest useful context
- defines clear subagent roles
- produces contract-bound outputs
- writes useful handoff state
- supports audit and recovery
- can be paused or killed safely
- does not pretend to be the OS Host
- cooperates through bridges instead of rummaging through other apps

## 12. Developer checklist

Before release, verify:

```txt
[ ] package name follows ano-<domain>-skill-app
[ ] manifest.yaml is complete
[ ] INSTALL_CARD.md explains the app clearly
[ ] agent_policy has no Host role
[ ] context_permission_request is declared
[ ] workspace permissions are least-privilege
[ ] commercial model is declared
[ ] output contracts are documented
[ ] tests or smoke checks are included
[ ] app can be installed without modifying OS kernel
[ ] app can be removed without deleting user project data
```


## Installed workspace filesystem

Skill Apps must target the v0.2.2 clean workspace filesystem:

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

App packages install to `apps/<package_name>/`. System-managed app runtime state goes to `ano/runtime/apps/<app_id>/`. User customization goes to `user/apps/<app_id>/`. Final user-facing outputs go to `out/<domain-or-app>/`.

Apps must not create root-level files, must not use legacy `.agent-os/`, and must not install into legacy `skills/`.

## App package inbox and install flow

Developers should test the full ANO flow instead of dropping app folders directly into `apps/`.

1. Build a ZIP package named `ano-<domain>-skill-app_v<version>.zip`.
2. Put it into `apps/_inbox/community/` for local testing, or distribute it for users to place there.
3. Use `ano/scripts/list_app_packages.py` to show the pending package and metadata.
4. Use `ano/scripts/install_app_package.py` to display `INSTALL_CARD.md`, ask for user approval, extract the package into `apps/<package_name>/`, and create runtime/registry/user-context folders.

Official demo packages are staged in `apps/_inbox/official/` during workspace initialization. They are never auto-installed by the mother system.


## Current-root user install flow

Developers should test apps against the v0.2.8 current-root workflow:

```bash
python scripts/init_workspace.py
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
python ano/scripts/validate_workspace.py
```

The preview command must not prompt or block. It only prints the install card.

## OS Host Command Gate requirement

Skill Apps must assume user instructions are delivered through ANO Host, not directly to app agents. Provide an `open` or equivalent preview entrypoint that prints:

- Context Permission Request
- Agent Runtime Approval Card
- visible agent roster
- STOP instruction

The preview entrypoint must not perform the main task. It must return control to the user.
