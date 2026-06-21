# 18. OS Host Command Gate

Agent-Native OS v0.2.8 introduces a hard post-install runtime rule:

```txt
After OS installation, every user instruction is received by the ANO Host/Admin Agent first.
Apps and app agents are never addressed directly by the user.
```

A user instruction such as:

```txt
打开 ANO Tiandao Furnace Skill AppAgent
```

is not a direct command to the Tiandao app. It is a command to the OS Host. The Host must respond as the system administrator, identify the target app by its user-facing name, check install status, print the app's permission/request card, and stop for user approval.

## Required behavior

1. The Host acknowledges identity: `I am the ANO Host/Admin Agent handling this request.`
2. The Host resolves the app target from installed apps and pending inbox packages.
3. If the app is not installed, the Host prints the install-card preview path and stops.
4. If the app is installed, the Host opens the app through an OS-mediated entrypoint.
5. The app prints its Context Permission Request and Agent Runtime Approval Card.
6. The app stops. The Host does not proceed to runtime execution unless the user explicitly approves the next step.

## Forbidden behavior

```txt
cd apps/<app>/runtime
python internal_script.py ritual --all --args --already-filled
```

The above bypasses the OS Host, the runtime permission request, staged user interaction, and user approval. It is forbidden for ANO-compliant agents.

## Helper command

A lightweight CLI gate is provided for agents and developers:

```bash
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
python ano/scripts/ano_host.py "列出应用"
```

This CLI is not the whole OS, but it encodes the required Host mediation flow.
