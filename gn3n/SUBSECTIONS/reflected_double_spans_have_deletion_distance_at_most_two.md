# Reflected-double spans have deletion distance at most two

## Metadata

- ID: reflected_double_spans_have_deletion_distance_at_most_two
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 61
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

### Deletion distance of a reflected double

Let \(J=C\sqcup\{x,y\}\) be the determining span of a reflected span-two double, where the corridor \(C\) has a two-cover. Deleting \(x\) and \(y\) leaves that corridor cover. Hence
\[
\kappa_2(H[J])\le2.
\]
The only nontrivial terminal residue is therefore the genuine case \(\kappa_2(H[J])=2\).

## Development

## Reflected-double spans have two-cover deletion distance at most two

Let J be the full determining span of a protected positive span-two reflected double. By [[complete_positive_span_two_double_corridor_classification]],
J=C union {x,y},
where the corridor C has a two-cover P|Q. Hence kappa_2(H[J])<=2.

This identifies the unbounded local branch with the first two exact deletion-distance layers rather than with an arbitrary large boundary tournament.

There are three cases.

1. kappa_2(H[J])=0: J already has a two-cover, so the outward replacement is immediate.
2. kappa_2(H[J])=1: the induced tournament H[J] is a one-hole deletion-cover problem, to which the structural machinery of [[kappa_one_role_balance_and_ky_fan]] applies. That machinery does not yet prove pc(H[J])<=2, but it replaces the long corridor by its established four-block/fixed-hole alternatives.
3. kappa_2(H[J])=2: this is the genuinely new reflected-double residue. The attachment-matching and packet lemmas address precisely this case.

Thus the local target can be narrowed to a two-deletion reflected-corridor theorem: under the endpoint relations in [[complete_positive_span_two_double_corridor_classification]], if neither a direct two-cover nor a one-deletion reduction closes the span, construct an outward order or a bounded protected carrier.

This gives a clean bridge between the positive local-witness route and the exact-root deletion-distance route.
