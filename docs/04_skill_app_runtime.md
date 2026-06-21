# Skill App Runtime

A Skill App is an installable capability package for Agent-Native OS.

It is not a prompt collection. It is not a separate operating system. It is not the Host.

## Rule

```txt
The Host belongs to Agent-Native OS.
A Skill App may define a Coordinator, but not a Host.
```

## What a Skill App declares

A Skill App declares:

- what it does
- how it should be installed
- whether it is free or paid
- what coordinator it uses
- what subagents it may request
- what context budget it needs
- what workspace paths it can read
- what workspace paths it can write
- what it must not touch
- what outputs it produces
- whether it needs audit
- whether it may request cross-app bridges

## Standard package

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

## Runtime actions

The Skill App Runtime should support:

- inspect
- install
- enable
- disable
- request_context
- print_runtime_approval_card
- run_after_host_approval
- pause
- resume
- audit
- remove
- lock version

## Registry

The registry records installed apps:

```txt
ano/
  registry/
    installed_apps.json
    apps/
      ano.skill.example.json
    mounts/
      ano.skill.example.mount.json
```

## Runtime data

App package code and app runtime data are separate.

```txt
apps/ano-example-skill-app/              # installed package
ano/runtime/apps/ano.skill.example/          # runtime data
```

This separation prevents app updates from destroying project data.

## Philosophy

Developers should not rebuild agent workflows from scratch.

They should build Skill Apps that can be installed into Agent-Native OS and governed by the OS Host.
