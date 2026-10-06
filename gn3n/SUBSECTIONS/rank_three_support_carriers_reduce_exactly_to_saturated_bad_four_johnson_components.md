# Rank-three support carriers reduce exactly to saturated bad-four Johnson components

## Metadata

- ID: rank_three_support_carriers_reduce_exactly_to_saturated_bad_four_johnson_components
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 249
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The first higher carrier obstruction is a saturated Johnson component of bad four-sets

Let W be a finite vertex set. Define X_4(W) to be the simplicial complex containing every subset of W of order at most three, together with a 3-simplex on every Hamiltonian four-set of H[W]. This is well-defined because every set of order at most three is Hamiltonian.

Work over F_2. Let B_4(W) be the family of non-Hamiltonian four-subsets of W.

Then H_2(X_4(W);F_2) has an exact presentation:
- one generator e_B for every B in B_4(W);
- for every five-set U subset W, one relation
  sum_{B subset U, |B|=4, B non-Hamiltonian} e_B = 0.

Proof. Compare X_4(W) with the full simplex Delta(W). In the relative chain complex C_*(Delta,X_4), the groups through degree two vanish. C_3 has basis the missing tetrahedra, exactly the bad four-sets. Every relative 3-boundary is zero because all triangles already lie in X_4. C_4 has basis the five-sets, and its relative boundary is exactly the sum of the bad four-facets of that five-set. Since Delta is contractible, the long exact sequence gives H_2(X_4) isomorphic to H_3(Delta,X_4), yielding the presentation.

Now use the boundary-tournament small-set theorem: every five-set contains at least three Hamiltonian four-subsets. Equivalently, every five-set contains at most two bad four-subsets.

Therefore every relation above has one of only three forms:
0,
e_B=0,
or e_B=e_C.

Define the bad-four Johnson graph J_bad(W): its vertices are the bad four-sets, and two are adjacent when they share three vertices, equivalently when their union is a five-set.

Then each connected component of J_bad contributes at most one F_2-generator to H_2. A component contributes a nonzero generator exactly when none of its vertices is killed by a singleton relation.

Equivalently, a component C survives in H_2 exactly when every B in C is saturated in the following sense:

for every x in W-B, the five-set B union {x} contains exactly two bad four-facets: B and one unique Johnson neighbor of B.

Indeed B is already one bad facet of B union {x}; the at-most-two theorem leaves either no second bad facet, which gives the relation e_B=0 and kills the whole connected component, or exactly one second bad facet C, which gives e_B=e_C. Thus a component survives iff the second alternative occurs for every external x at every vertex of the component.

Consequently:

H_2(X_4(W);F_2) is nonzero iff J_bad(W) contains a connected saturated component.

This is the exact first obstruction to extending the singleton-support carrier beyond rank two. Rank-two filling used only the fact that every set of order at most three is Hamiltonian. Rank-three filling fails only if the non-Hamiltonian four-sets organize into one of these saturated Johnson components.

In particular this turns the next closure obligation into a scale-independent structural theorem:

> Saturated-bad-component target. Prove that no boundary tournament admits a saturated connected component of non-Hamiltonian four-sets on the active carrier block; or prove that any such component can be absorbed by a mixed support-pair carrier using labels outside the block.

This is not a small-order cutoff. It is the universal homological obstruction at carrier dimension three.
