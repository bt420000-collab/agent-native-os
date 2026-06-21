# User-Defined Agent Topology

Agent-Native OS allows users to customize app agent rosters in natural language.

## Flow

```txt
App submits proposed agent roster
  ↓
OS prints Agent Runtime Approval Card
  ↓
User approves or modifies roster
  ↓
OS converts approved changes into persistent user context
  ↓
Future runs inherit the customization
```

## Example

User says:

```txt
This novel may explode in the comments. Add a troll simulator agent.
```

The OS records a new role such as:

```txt
role_id: novel.troll_simulator
purpose: detect toxic comment-section risks before publication
```

## Three user context layers

```txt
user/profile/global_profile.yaml
ano/runtime/apps/<app_id>/user_context/app_profile.yaml
ano/runtime/apps/<app_id>/projects/<project>/user_context/project_profile.yaml
```

The OS merges all applicable profiles before building the Final Runtime Plan.

## Principle

```txt
Every app run begins with a visible agent roster.
The user may edit the roster in natural language.
The OS persists approved changes as user-defined context.
```
