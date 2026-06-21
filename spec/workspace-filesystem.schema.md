# Workspace Filesystem Schema

Version: `0.2.2`

## Root entries

Required root entries:

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

Forbidden root entries in installed workspaces:

```txt
.agent-os/  # legacy forbidden
skills/     # legacy forbidden
```

## Required system files

```txt
ano/VERSION
ano/kernel/HOST.md
ano/kernel/FILESYSTEM_STANDARD.md
ano/kernel/CONTEXT_PERMISSION_MODEL.md
ano/kernel/SCHEDULER.md
ano/registry/installed_apps.json
ano/runtime/process_table.json
ano/runtime/context_allocations.json
ano/runtime/events.jsonl
user/profile/global_profile.yaml
```

## App install mapping

| Concept | Path |
| --- | --- |
| App package | `apps/<package_name>/` |
| App runtime home | `ano/runtime/apps/<app_id>/` |
| App user customization | `user/apps/<app_id>/` |
| App registry | `ano/registry/apps/<app_id>.json` |
| Final outputs | `out/<domain-or-app>/` |
