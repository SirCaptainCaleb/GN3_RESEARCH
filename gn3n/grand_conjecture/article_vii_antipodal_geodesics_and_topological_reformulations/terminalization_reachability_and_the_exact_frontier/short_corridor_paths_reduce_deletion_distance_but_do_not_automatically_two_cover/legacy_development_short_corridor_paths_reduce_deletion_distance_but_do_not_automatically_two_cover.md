# Short corridor paths reduce deletion distance but do not automatically two-cover — preserved pre-item development

## Composition

(none yet)

## Development

The short-path deduction in [[genuine_two_deletion_doubles_have_both_corridor_paths_of_order_at_least_four]] is valid as an exclusion of kappa_2=2, but its sentence saying that all short-path cases collapse directly to a two-cover is stronger than the proof.

Let J=P union Q union {x,y}, with P,Q actual tight paths, each of order at least two. If |P|=2, P union {x} is a Hamiltonian three-set. Consequently (P+x)|Q is a two-cover of J-y, proving kappa_2(H[J])<=1. No deduction concerning J itself follows from this cover without absorbing y or repartitioning.

If |P|=3, there are two possibilities. If either P+x or P+y is Hamiltonian, its union with Q gives a two-cover after deleting the other exterior vertex, again proving kappa_2<=1. If both four-extensions are non-Hamiltonian, the two-bad-four-extension theorem in [[localextend01]] makes P+x+y Hamiltonian, yielding a two-cover of all J and hence kappa_2=0. Thus |P|<=3 always gives kappa_2<=1; it gives kappa_2=0 in the specified double-bad case, but not by the argument in every case.

The same assertions hold with P,Q exchanged. In particular the 001/001 and 011/011 disjoint doubles, whose canonical corridor cover has a two-vertex component, belong to the deletion-distance-at-most-one layer. They are not closed merely by this observation. The actual two-cover tests in [[two_bridge_vertices_absorb_a_five_vertex_packet]] and [[successive_bad_five_packets_force_four_cross_endpoint_repairs]] continue to supply nontrivial repairs of these branches.

Therefore a two-deletion interface theorem alone would leave the distance-one double branch unresolved. Conversely any assumed genuine kappa_2=2 residue must have both corridor components of order at least four, exactly as the cited proof establishes. This addendum adjusts the scope, not that conditional result.
