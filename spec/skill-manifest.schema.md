# Skill App Manifest Schema v0.2

A Skill App Manifest declares an installable app for Agent-Native OS.

## Required fields

```yaml
app_id: string
package_name: string
display_name: string
version: semver
type: skill_app
standard: agent-native-os
standard_version: semver
runtime: ano
install: object
commercial: object
compatibility: object
agent_policy: object
context_permission_request: object
lifecycle: object
outputs: list
audit: object
```

## Important rule

The manifest must not declare the app as the Host.

Allowed:

```yaml
agent_policy:
  app_controller:
    role_id: novel.coordinator
    is_host: false
```

Forbidden:

```yaml
agent_policy:
  app_controller:
    role_id: novel.host
    is_host: true
```

## Naming

Recommended:

```yaml
package_name: ano-<domain>-skill-app
app_id: ano.skill.<domain>
```

## Commercial declaration

Apps may choose their own model, but must declare it.

```yaml
commercial:
  pricing_model: free | open_source | paid | freemium | subscription | one_time_purchase | enterprise_license | private_deployment
  payment_required: boolean
```

## Context request

Every app must declare a default context permission request. Runtime requests may be smaller than the default but must not exceed the app's declared maximum without user and Host approval.
