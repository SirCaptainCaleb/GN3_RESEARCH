# A7C3 Research Architecture

## Core split

**GitHub = research record. Slack = research room.**

Slack carries information whose value depends on being recent. GitHub carries mathematics and state that must remain useful regardless of age.

## Slack

Permanent channels:

- `#a7c3-control` — low-volume authoritative changes that can redirect or invalidate another worker's current reasoning: guidance, quarantines, architecture changes, and major strategic pivots.
- `#a7c3-workspace` — mathematics happening now: findings, partial arguments, useful failed branches, questions, and notices that durable material was written to GitHub.
- `#a7c3-audit` — verification, suspected gaps, dependency problems, invalidations, and clearances.

Temporary campaign channels are allowed only when one campaign genuinely overwhelms `#a7c3-workspace`.

Slack is provisional by default. GitHub is durable. A Slack finding may be used cautiously during live work, but if durable mathematics depends on it, promote that dependency first or together with the dependent result.

Important live control guidance should be pinned in Slack when useful.

## GitHub

```text
A7C3/
├── BOOTSTRAP.md
├── ARCHITECTURE.md
├── RESULTS/
│   ├── USABLE/
│   │   ├── ACTIVE/
│   │   └── LEGACY/
│   └── UNUSABLE/
│       ├── QUARANTINED/
│       └── INVALID/
├── WORKSPACE/
├── STRATEGY/
└── REFERENCES/
```

Folder location encodes trust and current relevance:

- `USABLE/ACTIVE`: valid durable results in the current preferred toolbox.
- `USABLE/LEGACY`: valid durable mathematics that is superseded, retired from the current route, or otherwise lower-priority, but remains safe to invoke.
- `UNUSABLE/QUARANTINED`: live repair targets that must not currently be used as premises.
- `UNUSABLE/INVALID`: known-invalid statements. Normally excluded from search and ordinary work.

A move between these directories is itself the durable state change. Announce moves that affect active work in `#a7c3-control`.

## Search

Use folder-scoped GitHub code search. Typical search widths:

1. `path:A7C3/RESULTS/USABLE/ACTIVE/` — highest signal.
2. `path:A7C3/RESULTS/USABLE/` — broad valid-theorem discovery.
3. `path:A7C3/RESULTS/UNUSABLE/QUARANTINED/` — repair archaeology.

Workspace searches should similarly target the relevant `WORKSPACE/` subtree.

## D* workspaces

The old D* documents were active evolving research workspaces, not proofs attached to individual results. Their minute-to-minute role moves to Slack. Their coherent long-form mathematical assembly survives under `WORKSPACE/`, split along natural mathematical section boundaries rather than exported as monoliths.

## Minimal operating rule

Talk and discover in Slack. Write durable mathematics in GitHub. Search GitHub. Check Slack periodically. Add structure only when actual usage demands it.
