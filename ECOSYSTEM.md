# Agent-Native OS Ecosystem Model

Agent-Native OS separates the free public system from installable Skill Apps.

## Core principle

```txt
The OS is the public standard.
Apps are the capability marketplace.
```

Agent-Native OS Core should remain open-source, free, and continuously updated. It defines the Host, runtime, permission model, context management, scheduling, app installation, and interoperability standards.

Skill Apps are developed by official maintainers, community developers, private teams, or commercial vendors. Each app may choose its own distribution and monetization model.

## Ecosystem layers

```txt
Agent-Native OS Core
  open-source, free, persistent Host, standards, runtime, scheduler

Official Skill Apps
  reference apps maintained by the core project or trusted maintainers

Community Skill Apps
  open or private apps built by the community

Commercial Skill Apps
  paid, freemium, subscription, enterprise, or private-deployment apps
```

## App monetization

Supported app commercial models:

```txt
free
open_source
paid
freemium
subscription
one_time_purchase
enterprise_license
private_deployment
```

The OS does not set app prices. The OS requires apps to declare pricing, permissions, agent roster, and resource needs before installation or execution.

## Trust rule

Every app must show what it wants before it runs:

- what agents it wants to start
- what context budget it needs
- what workspace paths it can read
- what workspace paths it can write
- whether it may request cross-app bridges
- whether it is free or paid
- what persistent user context it may write

## One-line doctrine

```txt
The system sells order; apps sell capability.
```

The public core provides order even when no one charges money for it. App developers provide domain capability and may choose how to fund their work.
