# ANO Context Virtual Memory

Version: 0.3.0  
Status: Experimental reference contract

Agent-Native OS treats context as an operating-system resource, not as a large prompt assembled once at startup.

```txt
User instruction
  → Host compiles a task lease
  → bootstrap frames are pinned
  → App receives a small working set
  → Agent reports a page fault when evidence is missing
  → Host mounts the smallest authorized context object
  → inactive pages become cold references
  → snapshot preserves versions, leases, mounts, and handoff state
```

## What this model shorts

Context Virtual Memory adds a stronger regulator so three failure modes fall:

1. unrelated material competing for attention;
2. stale versions silently contaminating current work;
3. repeated user approval for reads already covered by the task lease.

The goal is not maximum context utilization. The goal is maximum effective work per visible context token.

## Kernel objects

### Context Object

A catalog entry pointing to canonical backing material.

Required metadata:

- `context_id`
- workspace-relative `source`
- `source_version` or content hash
- authority and classification
- estimated token cost

Registration does not make the object visible to an Agent.

### Context Lease

A revocable Host grant for one task and one Agent identity. It defines readable paths, denied paths, token budget, lifecycle, and required bootstrap frames.

A lease is permission, not content. It cannot mount a source outside its scope.

### Working Set

The pages currently visible to an Agent.

- `hot`: active and frequently needed;
- `warm`: mounted but secondary;
- `cold reference`: metadata-only pointer, not prompt-visible;
- `archived`: recoverable state outside the active run.

Task instruction, authoritative laws, and output contract are pinned during an active run. Other pages may be evicted.

### Page Fault

When an Agent cannot continue safely with its current working set, it emits a Page Fault Request describing the missing need and a maximum requested budget. It must not silently scan the whole project.

The Host may:

- mount an existing Context Object;
- register and mount a new object;
- provide a smaller excerpt;
- reject the fault and require a fallback;
- ask the user only when the request exceeds the active lease.

### Snapshot

A snapshot records task lease state, visible mounts, source versions, and handoff/checkpoint references. Resume rehydrates the same logical working set only when backing versions still match. A mismatch becomes a recovery conflict, never a silent substitution.

## Non-negotiable invariants

1. Only `ano.host` grants, reduces, or revokes leases.
2. Apps request context; they never mount private sources directly.
3. Every visible page belongs to one active lease.
4. Denied paths override readable paths.
5. Mounted token estimates may not exceed the lease budget.
6. Registration does not imply permission; permission does not imply mounting.
7. Pinned bootstrap frames cannot be evicted while the task is active.
8. Dirty work must be checkpointed or handed off before eviction.
9. Cross-App material enters only through an approved Bridge and becomes a new scoped Context Object.
10. Audit events record registration, lease changes, mounts, faults, evictions, and snapshots.

## Installed workspace layout

```txt
ano/
  registry/
    context_objects/
  runtime/
    context_vm/
      catalog.json
      leases.json
      page_table.json
      page_faults.jsonl
      events.jsonl
      working_sets/
      cold_refs/
      snapshots/
```

Canonical user files remain under `user/`; installed App files remain under `apps/`; final exports remain under `out/`. Context VM stores control metadata and references, not duplicate canonical content.

## Minimal experiment

Use the Novel Skill App for one continuous six-chapter batch:

- A: preload the full project context;
- B: pin only task, laws, and output contract, then resolve page faults on demand.

Compare user interruptions, visible context tokens, stale-source incidents, unauthorized reads, recovery accuracy, and final quality. The Context VM hypothesis fails if B saves tokens but causes more source mistakes, unrecoverable state, or permission ambiguity.
