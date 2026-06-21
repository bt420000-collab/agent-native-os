# Cross-App Bridge Schema

A Cross-App Bridge is an OS-approved data channel between two apps.

## Required fields

```yaml
cross_app_bridge:
  bridge_id: string
  task_id: string
  from_app: string
  to_app: string
  status: active | expired | revoked
  approved_by: ano.host
  read_scope: list[path]
  write_scope: list[path]
  expires_after_task: boolean
```

## Rule

Apps must not directly read another app's private workspace. All app-to-app data flow must go through a bridge or a user-approved export/import packet.
