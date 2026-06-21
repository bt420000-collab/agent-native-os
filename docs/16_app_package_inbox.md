# App Package Inbox Standard

Agent-Native OS installs the mother system first. Skill Apps are installed later by user approval.

## Rule

The OS package may bundle app **packages**, but it must not auto-install them into the workspace.

A freshly initialized workspace may contain pending app packages under:

```txt
apps/_inbox/official/
apps/_inbox/community/
apps/_inbox/installed/
```

These are not installed apps. They are install candidates.

Installed app code lives at:

```txt
apps/<package_name>/
```

Runtime state lives at:

```txt
ano/runtime/apps/<app_id>/
```

User preferences live at:

```txt
user/apps/<app_id>/
```

Final outputs live at:

```txt
out/<domain>/
```

## User flow

1. Install / initialize the ANO workspace.
2. The system scans `apps/_inbox/**.zip`.
3. The system prints detected app packages and their install cards.
4. The user chooses whether to install each app.
5. The OS Host records install events and app registry entries.

This preserves the full developer and user experience: core first, app second, approval before runtime.

After successful installation, an inbox ZIP package is moved to `apps/_inbox/installed/` so it no longer appears as pending.


## v0.2.7 behavior

The inbox is staged only. OS initialization stops immediately after staging. App installation commands are preview-only by default and require `--yes` after explicit user approval.
