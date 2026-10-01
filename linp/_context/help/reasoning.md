
REASONING TREES

Reasoning chains use the ordinary nested object hierarchy plus lightweight reasoning annotations.

Node kinds:
  root, branch, step.

A recomposition is NOT a node kind. Any ordinary reasoning node may carry composition_manifest / composition_status metadata when it summarizes or recomposes source objects. That metadata never constrains where the node may live in the reasoning tree.

Main APIs:
  create_reasoning_child(...)
  mark_reasoning_node(...)
  reasoning_overview(...)
  stage_reasoning_bundle(...)

Reasoning-tree organization does not alter mathematical trust by itself. Exact mathematical edits still bump math_version and invalidate/re-audit as usual. Reparenting and reasoning annotations are organizational operations.

RECOMPOSITION METADATA

bind_composition_v2(...) is retained as a compatibility API for attaching a source manifest to an ordinary reasoning node. It does not require a special node kind or compose lease. Recomposition manifests track source math versions and support state; stale manifests may still trigger proof-rehearsal attention.

UNARY-CHAIN REVIEW IS A JUDGMENT CALL

unary_cleanup_candidates(...) and unary_chain_candidates(...) are structural review heuristics, not compression mandates. A unary shape alone is never sufficient reason to replace or delete mathematical objects.

For every candidate, inspect the exact statements/proofs, mathematical interfaces, consumers, dependencies, descendants, and local exposition. Valid outcomes include:
- if the nodes are authentic sequential reasoning, KEEP the sequential semantics. Do not flatten or turn steps into siblings. If the chain is too granular, recompose the contiguous unary segment into one equivalent-or-stronger replacement node using bind_replacement_composition_v2(...); the replacement occupies the old segment position, terminal children are reattached to it, external logical consumers are rewired, and the old source chain is structurally retired;
- reparent only when a node was genuinely filed under the wrong mathematical parent, never merely to shorten an authentic reasoning chain;
- preserve distinct reusable lemmas/results as standalone objects by rehoming the actual mathematics beneath the canonical Toolkit root.

Useful lemmas often deserve to remain independently addressable. If they are genuinely standalone, rehome them into Toolkit. If they are genuinely sequential proof steps, preserve their nesting unless an equivalent-or-stronger recomposition replaces the whole contiguous segment. Never make sequential steps siblings merely to make the detector empty.

INTENTIONALLY STANDALONE RESULTS

A proved object may be excluded from unary-chain detection by setting unary_chain_standalone=true through update_object(..., p_substantive=>false). Use this only when the result has a distinct reusable statement, proof idea, consumer interface, or conceptual role.
