# App Package Inbox Schema

Reserved app package locations inside an installed workspace:

```txt
apps/_inbox/official/*.zip
apps/_inbox/community/*.zip
```

A package in `_inbox` is not installed. It must be explicitly installed by the user.

Minimum package requirements:

```txt
<package_name>/manifest.yaml
<package_name>/INSTALL_CARD.md
<package_name>/runtime/health_check.py optional
```

Installer output requirements:

```txt
apps/<package_name>/
ano/registry/apps/<app_id>.json
ano/runtime/apps/<app_id>/
user/apps/<app_id>/
out/<domain>/ optional
```

After successful installation, an inbox ZIP package is moved to `apps/_inbox/installed/` so it no longer appears as pending.
