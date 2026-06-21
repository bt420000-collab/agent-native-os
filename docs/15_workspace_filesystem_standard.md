# v0.2.2 Workspace Filesystem Standard

Agent-Native OS separates the development repository from the installed user workspace.

The development repository may contain docs, scripts, specs, templates, and official app source packages. The installed workspace must be clean and predictable.

## Installed workspace root

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

## Directory roles

| Path | Role |
| --- | --- |
| `ano/` | System directory: Host rules, kernel docs, registry, runtime, scheduler state, events, locks, bridges, templates, specs, and system logs. |
| `user/` | User-owned data: profiles, preferences, memory, projects, imported files, and app-specific user customization. |
| `apps/` | Installed Skill App packages. App code lives here. |
| `res/` | Shared static resources such as icons, schemas, and reusable assets. |
| `out/` | Final user-facing outputs and exports. |

## Runtime app paths

```txt
apps/<package_name>/                    # installed app package
ano/runtime/apps/<app_id>/              # system-managed app runtime home
user/apps/<app_id>/                     # user customization for this app
out/<domain-or-app>/                    # final outputs
ano/registry/apps/<app_id>.json         # app registry record
```

## Root cleanup rule

The workspace root is user-facing. Apps and subagents must not write arbitrary files to root.

Unknown root entries should be moved to:

```txt
user/imports/_unsorted/<timestamp>/
```

Legacy v0.2.1 paths are forbidden in installed workspaces:

```txt
.agent-os/  # legacy forbidden
skills/     # legacy forbidden
```

## Why this matters

A user should be able to open an ANO workspace and immediately understand where things live:

- `ano/` = system engine room
- `user/` = user materials and memory
- `apps/` = installed apps
- `res/` = shared resources
- `out/` = finished outputs

No root-level confetti cannon. No mystery folders. No haunted attic.
