# Current Root Installation Standard

Agent-Native OS v0.2.8 installs into the current authorized directory only.

The installer must not create child workspace folders. Deprecated names such as `ano-workspace/` and `my-workspace/` are forbidden for installed workspaces.

## Correct installation

From the directory the user authorized as the workspace root:

```bash
python agent-native-os-main/scripts/init_workspace.py
```

Or, when already inside the extracted source directory and the user wants that directory to become the workspace root:

```bash
python scripts/init_workspace.py
```

After installation, the workspace root must contain only:

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

## Stop point

OS initialization is a stop point. The agent must not continue into Skill App installation automatically.

Official app packages may be staged in `apps/_inbox/official/`, but they remain pending until the user explicitly asks to install one.

## Non-blocking app installation preview

The app installer is preview-only by default:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
```

It prints the install card and exits. It does not prompt for yes/no.

To install after explicit user approval:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
```
