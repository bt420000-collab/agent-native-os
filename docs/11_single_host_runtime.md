# Single Host Runtime

Agent-Native OS v0.2 defines one persistent Host owned by the mother system.

## Rule

```txt
There is exactly one Host.
The Host is the OS.
Apps are not Hosts.
```

Apps may define coordinators, directors, managers, or workflow controllers. These are app-level roles and do not own lifecycle control.

## Authority split

| Capability | OS Host | App Coordinator | Subagent |
|---|---:|---:|---:|
| approve app run | yes | no | no |
| start subagent | yes | request only | no |
| pause/kill subagent | yes | request only | no |
| allocate context | yes | request only | no |
| write app outputs | governed | yes | governed |
| mutate OS kernel | yes | no | no |
| approve cross-app bridge | yes | request only | no |

## Why this matters

Without a single Host, every app can become a miniature operating system. That leads to role conflicts, context overuse, unsafe file access, broken audits, and multi-app chaos.

With one Host, the OS can run multiple apps at once and schedule them coherently.
