# Context ABI

Context ABI is the contract that defines how Skill Apps receive context, produce outputs, declare uncertainty, request permissions, and hand off state.

Traditional software has APIs and ABIs.

Agent systems need a context interface.

Without a Context ABI:

- one agent writes vague commentary
- another agent cannot identify valid conclusions
- a third agent fills gaps by guessing
- the host loses project continuity

With a Context ABI, every Skill App must declare and produce structured work.

## Required interface concepts

A Skill App should declare:

```txt
inputs
outputs
permissions
source policy
uncertainty policy
mutation policy
audit policy
handoff fields
```

## Required output behavior

A Skill App should report:

- completed work
- sources used
- decisions made
- uncertainties
- risks
- next steps
- files changed
- audit requirement

## Goal

Context ABI makes agent work composable.
