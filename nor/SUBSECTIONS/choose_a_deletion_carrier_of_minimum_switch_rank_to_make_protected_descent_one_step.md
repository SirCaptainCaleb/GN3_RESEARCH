# Choose a deletion carrier of minimum switch rank to make protected descent one-step

## Metadata

- ID: choose_a_deletion_carrier_of_minimum_switch_rank_to_make_protected_descent_one_step
- Parent Section: directed_nor_union_closed_bridge
- Position: 200
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Extremal protected-descent principle. In a minimum coordinate counterexample, consider the set of all genuine one-change deletion carriers over all omitted coordinates, both reversal orientations, and both global color complements. Normalize each carrier to word 0^p1^q with p,q>0, and choose one minimizing the first-run length p. Then any protected surgery that produces another genuine one-change deletion carrier with normalized first-run length p'<p gives an immediate contradiction; no iterative transport theorem is needed. In particular, for the replacement packet of the protected bridge schema, a packet 0^a1^(r-a) with a<r produces p'=p-r+a<p and contradicts extremality directly. Thus the general bridge lemma can be stated in an extremal form: for a p-minimal deletion carrier, the r-window replacement packet cannot be threshold-compatible with a nonempty second phase. Equivalently every candidate replacement packet must either be all first-phase or contain a forbidden back-change 1->0. This packages the desired topological extraction into a clean obstruction statement and avoids bookkeeping across repeated changes of the omitted coordinate. The flat ternary theorem is recovered because its replacement packet is 111, immediately contradicting p-minimality.

## Frontier

- Development version when composed: None
- Development version now: 1
