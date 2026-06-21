# Bilingual Policy

Agent-Native OS is an international open architecture. English is the default specification language. Simplified Chinese is maintained for the main public-facing documents because the project originated from Chinese-language architecture discussions.

## Required bilingual files

At minimum, keep these paired:

```txt
README.md
README.zh-CN.md
```

## Recommended bilingual files

For major releases, consider adding Chinese versions or bilingual sections for:

```txt
SPEC.md
APP_DEVELOPER_GUIDE.md
ECOSYSTEM.md
VERSIONING.md
```

## Translation rule

English and Chinese documents do not need to be word-for-word identical. They must preserve the same system concepts and normative rules.

Critical terms should stay aligned:

| English | Chinese |
|---|---|
| Agent-Native OS | Agent-Native OS / Agent 原生操作系统 |
| OS Host | OS Host / 系统 Host |
| Skill App | Skill App / 技能应用 |
| Context Permission Request | 上下文权限申请表 |
| Runtime Approval Card | 运行审批卡 |
| User-Defined Agent Topology | 用户自定义 Agent 拓扑 |
| Cross-App Bridge | 跨 App Bridge / 跨 App 桥接 |
| Context Kernel | 上下文内核 |
| Context ABI | 上下文 ABI |

## v0.2 priority

The most important v0.2 bilingual rule is to preserve the Single Host principle:

```txt
There is exactly one Host. The Host is the OS. Apps are not Hosts.
```

```txt
Host 只有一个，Host 属于母系统，App 不是 Host。
```
