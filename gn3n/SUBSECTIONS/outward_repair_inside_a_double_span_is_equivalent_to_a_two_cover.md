# Outward repair inside a double span is equivalent to a two-cover

## Metadata

- ID: outward_repair_inside_a_double_span_is_equivalent_to_a_two_cover
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 70
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

### Internal repair criterion

For a reflected double span \(J\), a repair supported entirely on \(J\) that removes the selected positive terminal obstruction exists if and only if \(H[J]\) has a two-cover. Thus a genuine two-deletion double admits no internal outward repair. Any successful terminalization of such a span must use exterior vertices or a larger carrier.

## Development

Let J=[a,b+4] be the full determining span of a protected positive span-two reflected double at witness depth r. Reorder only the vertices in J, fixing every position outside J.

Such a reorder is outward at depth r if and only if its internal status word on J avoids 001,011,0101; hence an outward reorder supported on J exists if and only if H[J] has a two-cover.

Proof. Every internal span-two window starts between a and b, so its unsigned depth is at most r. Every internal alternating window starts between a and b-1; its center lies strictly between the centers of the two outer span-two windows, so its depth is also at most r. Thus outwardness forbids every internal positive word. Conversely all positive windows at depth at most r have their determining vertices inside J. An internally positive-word-free order therefore has no witness at depth at most r. Any changed boundary-crossing positive window is farther outward. The equivalence between a positive-word-free spanning order and a two-cover is the exact inversion-window theorem in [[spanning_orders_and_defect_helly]]. QED.

This strengthens the scope of [[genuine_two_deletion_doubles_admit_no_internal_outward_repair]]: the same impossibility holds whenever kappa_2(H[J])>0, including distance one. The distance-two hypothesis is unnecessary for this particular statement.

It follows that reducing a double from deletion distance two to distance one is useful structural progress, but is not itself a terminalization step in the protected X_r filtration. Nor does a Hamiltonian four-support automatically provide an outward carrier unless the remaining vertices can be covered by the other path or a separate enlarged-window argument is supplied. In particular the common-reverser Hall branch retained in [[double_corridor_hall_failure_reduces_to_one_zero_degree_path_residue]] is not closed merely by exposing its four-support.

There are consequently two distinct outstanding tasks: eliminate the nonzero deletion-distance double spans by actual two-cover proofs (the packet and attachment certificates are sufficient cases), or give an enlarged-support/topological bypass with the required protected and equivariant properties. A theorem only about genuine distance-two residues does not remove the already known distance-one alternative.
