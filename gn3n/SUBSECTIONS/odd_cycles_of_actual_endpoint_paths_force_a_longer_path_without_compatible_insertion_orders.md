# Odd cycles of actual endpoint paths force a longer path without compatible insertion orders

## Metadata

- ID: odd_cycles_of_actual_endpoint_paths_force_a_longer_path_without_compatible_insertion_orders
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 286
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

## Scope and audit

The grand conjecture remains open. Sections 269 and 272 identify a possible closed residue, not an augmentation of it. The proofs in 279–281 correctly use actual path orders. The examples in 282 and 283 block universal compatibility and deletion-criticality shortcuts. The hexadecimal encoding in 283 is read most-significant bit first in the stated lexicographic variable order; direct verification gives no Hamiltonian six-path and deletion counts 8,10,5,5,2,2.

The following augmentation uses dissimilar actual paths and one boundary comparison. It does not require compatible orders on their shared support.

## Lemma: a common endpoint with mutually exterior neighbors gives an extension

Let P and Q be tight paths in a boundary 3-tournament, each of order at least two.

Suppose P=(a,b,p_3,...,p_s), Q=(a,c,q_3,...,q_t), b notin V(Q), and c notin V(P). Exactly one of (b,a,c) and (c,a,b) is tight. In the first case (b,Q) is a tight path of order t+1; in the second case (c,P) is a tight path of order s+1.

Likewise, if P=(...,b,a), Q=(...,c,a) with the same exterior-neighbor conditions, then either (P,c) or (Q,b) is tight, increasing the corresponding path order by one.

Proof. For (b,Q) the only new consecutive triple is (b,a,c); all subsequent triples belong to Q. For (c,P) the only new triple is its boundary reverse. The exterior-neighbor assumptions ensure vertex simplicity. The terminal case has the same two triples as its possible new final triples. QED.

In particular, two globally maximum paths cannot share an initial vertex and have mutually exterior next vertices, or share a terminal vertex and have mutually exterior preceding vertices. Intersection of their supports exactly at a is sufficient for the exterior-neighbor conditions.

This also gives a condition stronger than support intersection alone: for maximum paths beginning at a on supports S,T, it is impossible both to have an attainable next vertex in S-T and to have an attainable next vertex in T-S. The analogous assertion holds for terminal neighbors.

## Theorem: an odd cycle of rooted Hamiltonian supports gives a genuine longer path

Fix integers t>=2 and m>=3 with m odd. Let S_0,...,S_{m-1} be t-element supports containing a common vertex a, with S_i intersect S_{i+1}={a}, indices taken modulo m. Suppose each H[S_i] has a Hamilton path in which a is an endpoint.

Then H has a tight path of order t+1.

Proof. Choose one such actual Hamilton order for each S_i and label i by + if a is first, and - if a is last. A two-sign assignment around an odd cycle has an adjacent equal-sign pair. For that pair the common-endpoint lemma applies, since the other endpoint-neighbors belong to disjoint S_i-{a}. It constructs a vertex-simple (t+1)-path by prepending or appending one of those neighbors. Every inherited triple and the single new triple have been checked. QED.

The theorem also covers an odd closed walk of supports; distinctness of nonadjacent supports is unnecessary.

A stronger formulation records all attainable endpoint roles. Form the graph whose vertices are t-element supports admitting a Hamilton order with a as an endpoint, with adjacency when the supports intersect only at a. If t is the global maximum path order, every nonisolated support has exactly one attainable endpoint role at a, adjacent supports have opposite roles, and this graph is bipartite. Indeed two equal attainable roles would give the extension above; a support with both roles cannot have a neighbor. This conclusion is a proved obstruction to endpoint recurrence, not a claim about the topology of the full support interface.

## Application to the odd uniform residue

Assume n=2r+1, every r-set is Hamiltonian, and every (r+1)-set is non-Hamiltonian. Here r>=2. If an odd rooted-support cycle as above exists with t=r, the theorem constructs an (r+1)-path. Its complement has r vertices and is Hamiltonian, so the construction supplies a spanning two-cover and closes this branch.

The mechanism can be applied directly to sides of dissimilar deletion covers: retain any r-side path with endpoint a, and use the sides from other covers as further rooted supports. Their interior orders need not agree. An odd cycle of intersections exactly at a suffices; two same-role paths with mutually exterior endpoint-neighbors already suffice without an odd cycle.

There is an explicit family of supports on which the endpoint obligation can be tested. Fix a and choose 2r-1 other vertices w_0,...,w_{2r-2}. Set M=2r-1 and
S_i={a} union {w_{i+2j mod M}:0<=j<=r-2},
for i=0,...,M-1.
Each S_i has r vertices and consecutive supports intersect only at a. To check disjointness off a, equality of two indices would give 2(j-k)=1 modulo 2r-1, with |j-k|<=r-2. The even integer on the left cannot equal 1, and cannot equal 1-(2r-1)=-2(r-1), whose magnitude exceeds the allowed range. Thus the displayed supports form an odd closed walk in the required intersection graph.

Consequently, in the unresolved odd residue, for every a and every such choice of 2r-1 other vertices, at least one of these Hamiltonian r-supports has a internal in EVERY Hamilton order. Otherwise the odd-cycle construction would give the forbidden longer path. This is stronger than rejecting one common endpoint insertion order: it permits unrelated Hamilton orders and either endpoint role on each support.

## Audit of the missing endpoint premise

Uniform Hamiltonicity does not by itself supply a prescribed endpoint. In the genuine four-vertex tournament of 282 the only Hamilton orders are
(1,2,3,0) and (2,3,0,1).
Vertex 3 is internal in both. Every three-subset is Hamiltonian, as is automatic for boundary tournaments, yet the Hamiltonian four-support has no order with 3 as an endpoint. This was checked directly against the twelve tight triples in 282.

This example refutes the universal endpoint assertion; it does not refute an endpoint theorem using the full odd uniform counterexample hypotheses.

Remaining obligation: force an odd cycle in one actual endpoint-support graph, force one mutually exterior same-role pair, or show that the resulting unavoidable-interior supports cannot coexist under the ambient uniform hypotheses. Neither endpoint availability nor that last contradiction is proved here. The all-collapsed branch of 272 also remains open. No global terminating improvement is inferred merely from this bipartiteness condition.

## Development

## Scope and audit

The grand conjecture remains open. Sections 269 and 272 identify a possible closed residue, not an augmentation of it. The proofs in 279–281 correctly use actual path orders. The examples in 282 and 283 block universal compatibility and deletion-criticality shortcuts. The hexadecimal encoding in 283 is read most-significant bit first in the stated lexicographic variable order; direct verification gives no Hamiltonian six-path and deletion counts 8,10,5,5,2,2.

The following augmentation uses dissimilar actual paths and one boundary comparison. It does not require compatible orders on their shared support.

## Lemma: a common endpoint with mutually exterior neighbors gives an extension

Let P and Q be tight paths in a boundary 3-tournament, each of order at least two.

Suppose P=(a,b,p_3,...,p_s), Q=(a,c,q_3,...,q_t), b notin V(Q), and c notin V(P). Exactly one of (b,a,c) and (c,a,b) is tight. In the first case (b,Q) is a tight path of order t+1; in the second case (c,P) is a tight path of order s+1.

Likewise, if P=(...,b,a), Q=(...,c,a) with the same exterior-neighbor conditions, then either (P,c) or (Q,b) is tight, increasing the corresponding path order by one.

Proof. For (b,Q) the only new consecutive triple is (b,a,c); all subsequent triples belong to Q. For (c,P) the only new triple is its boundary reverse. The exterior-neighbor assumptions ensure vertex simplicity. The terminal case has the same two triples as its possible new final triples. QED.

In particular, two globally maximum paths cannot share an initial vertex and have mutually exterior next vertices, or share a terminal vertex and have mutually exterior preceding vertices. Intersection of their supports exactly at a is sufficient for the exterior-neighbor conditions.

This also gives a condition stronger than support intersection alone: for maximum paths beginning at a on supports S,T, it is impossible both to have an attainable next vertex in S-T and to have an attainable next vertex in T-S. The analogous assertion holds for terminal neighbors.

## Theorem: an odd cycle of rooted Hamiltonian supports gives a genuine longer path

Fix integers t>=2 and m>=3 with m odd. Let S_0,...,S_{m-1} be t-element supports containing a common vertex a, with S_i intersect S_{i+1}={a}, indices taken modulo m. Suppose each H[S_i] has a Hamilton path in which a is an endpoint.

Then H has a tight path of order t+1.

Proof. Choose one such actual Hamilton order for each S_i and label i by + if a is first, and - if a is last. A two-sign assignment around an odd cycle has an adjacent equal-sign pair. For that pair the common-endpoint lemma applies, since the other endpoint-neighbors belong to disjoint S_i-{a}. It constructs a vertex-simple (t+1)-path by prepending or appending one of those neighbors. Every inherited triple and the single new triple have been checked. QED.

The theorem also covers an odd closed walk of supports; distinctness of nonadjacent supports is unnecessary.

A stronger formulation records all attainable endpoint roles. Form the graph whose vertices are t-element supports admitting a Hamilton order with a as an endpoint, with adjacency when the supports intersect only at a. If t is the global maximum path order, every nonisolated support has exactly one attainable endpoint role at a, adjacent supports have opposite roles, and this graph is bipartite. Indeed two equal attainable roles would give the extension above; a support with both roles cannot have a neighbor. This conclusion is a proved obstruction to endpoint recurrence, not a claim about the topology of the full support interface.

## Application to the odd uniform residue

Assume n=2r+1, every r-set is Hamiltonian, and every (r+1)-set is non-Hamiltonian. Here r>=2. If an odd rooted-support cycle as above exists with t=r, the theorem constructs an (r+1)-path. Its complement has r vertices and is Hamiltonian, so the construction supplies a spanning two-cover and closes this branch.

The mechanism can be applied directly to sides of dissimilar deletion covers: retain any r-side path with endpoint a, and use the sides from other covers as further rooted supports. Their interior orders need not agree. An odd cycle of intersections exactly at a suffices; two same-role paths with mutually exterior endpoint-neighbors already suffice without an odd cycle.

There is an explicit family of supports on which the endpoint obligation can be tested. Fix a and choose 2r-1 other vertices w_0,...,w_{2r-2}. Set M=2r-1 and
S_i={a} union {w_{i+2j mod M}:0<=j<=r-2},
for i=0,...,M-1.
Each S_i has r vertices and consecutive supports intersect only at a. To check disjointness off a, equality of two indices would give 2(j-k)=1 modulo 2r-1, with |j-k|<=r-2. The even integer on the left cannot equal 1, and cannot equal 1-(2r-1)=-2(r-1), whose magnitude exceeds the allowed range. Thus the displayed supports form an odd closed walk in the required intersection graph.

Consequently, in the unresolved odd residue, for every a and every such choice of 2r-1 other vertices, at least one of these Hamiltonian r-supports has a internal in EVERY Hamilton order. Otherwise the odd-cycle construction would give the forbidden longer path. This is stronger than rejecting one common endpoint insertion order: it permits unrelated Hamilton orders and either endpoint role on each support.

## Audit of the missing endpoint premise

Uniform Hamiltonicity does not by itself supply a prescribed endpoint. In the genuine four-vertex tournament of 282 the only Hamilton orders are
(1,2,3,0) and (2,3,0,1).
Vertex 3 is internal in both. Every three-subset is Hamiltonian, as is automatic for boundary tournaments, yet the Hamiltonian four-support has no order with 3 as an endpoint. This was checked directly against the twelve tight triples in 282.

This example refutes the universal endpoint assertion; it does not refute an endpoint theorem using the full odd uniform counterexample hypotheses.

Remaining obligation: force an odd cycle in one actual endpoint-support graph, force one mutually exterior same-role pair, or show that the resulting unavoidable-interior supports cannot coexist under the ambient uniform hypotheses. Neither endpoint availability nor that last contradiction is proved here. The all-collapsed branch of 272 also remains open. No global terminating improvement is inferred merely from this bipartiteness condition.
