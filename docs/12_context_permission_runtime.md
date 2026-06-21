# Context Permission Runtime

In Agent-Native OS, context is the first-class resource. Apps do not own it. Apps request it.

## Context Permission Request

Before execution, a Skill App submits a Context Permission Request.

The request declares:

- task purpose
- requested runtime mode
- subagent roster
- context budget
- read/write workspace paths
- denied paths
- cross-app bridge needs
- output contracts
- persistent user context writes

## Host decision

The OS Host may:

```txt
approve
approve_with_reductions
deny
defer
pause
kill
archive
```

## Runtime Plan

After approval, the Host turns the request into a Final Runtime Plan.

```txt
App default request
+ global user profile
+ app user profile
+ project user profile
+ this-run user override
+ Host resource decision
= Final Runtime Plan
```

Only the Final Runtime Plan is executable.
