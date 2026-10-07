# Coordinate NOR and the endpoint defect reduction

## Metadata

- ID: coordinate_nor_and_the_endpoint_defect_reduction
- Parent Section: protected_coordinate_deletion_descent
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Every minimum counterexample for a reversal-odd coordinate r-tuple label has a bichromatic good order on each single-coordinate deletion. Appending or prepending the missing coordinate preserves all deletion windows, so a full order with exactly one endpoint threshold defect exists. This holds in every translation-invariant coordinate arity r>=2, and does not automatically extend to basepoint-dependent cube colorings.

## Development

Sources: Article II §§162,173. This is a consolidated proof, with coordinate and cube-window scopes separated.

Let V be finite, r>=2, and let h assign a binary value to every ordered r-tuple of distinct elements of V. Assume h(reverse T)=1-h(T). For O=(v_1,...,v_n), its word consists of h(v_i,...,v_{i+r-1}), 1<=i<=n-r+1. A good order has at most one color change. This is the translation-invariant coordinate sector of N_{r+1}; no statement here deletes a coordinate from an unrestricted basepoint-dependent antipodal coloring.

Assume a counterexample of minimum cardinality. Every restriction to V minus {x} is still reversal-odd and hence has a good order. If a deletion good order were monochromatic, appending x would add only one arbitrary bit to that constant word and would give a good full order. Thus every deletion good order is bichromatic.

Write one as 0^p1^q with p,q>0, after reversing the order if necessary. Appending or prepending x preserves all its windows. If either extension were good, the full instance would be solved. Hence prepending produces 1,0^p,1^q and appending produces 0^p,1^q,0. Each extension differs from a one-change threshold word at just one endpoint.

Consequently the global minimum threshold disagreement count is one: an endpoint extension has at most one disagreement, and zero disagreements would solve the instance. The largest contiguous matched threshold band has all but one window. This is a reduction of the spanning problem to a single endpoint defect, with an explicit deletion witness.

It does not imply that every minimum-energy state has an endpoint defect, nor that the minimum-energy locus carries the topology of the entire switch prism.
