# OS Host Command Gate Schema

A user instruction handled by ANO Host should produce a gate event with these fields:

```yaml
event: os.user_instruction.received
time: <iso8601>
host_id: ano.host
instruction: <raw user instruction>
resolved_app_id: <app id or null>
resolution_status: installed | pending_package | unknown
required_next_step: preview_install | preview_runtime_approval | ask_user_to_choose | stop
bypass_forbidden: true
```

Required invariant:

```txt
No Skill App runtime execution may occur before the OS Host has resolved the instruction and shown the relevant permission card.
```
