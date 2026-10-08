# Non-rigid maximum supports can avoid any prescribed vertex pair — preserved pre-item development

## Localized majority contrapositive

Assume the odd uniform residue on n=2r+1 vertices and assume there is no tight path of order r+1.

Let W be any subset of V(H) with
|W|>=2r-1.
Every r-subset of W is Hamiltonian by the odd-uniform hypothesis.

Call an r-support S subseteq W initial-rigid if it has at least one Hamilton order
P=(a,b,...)
for which a is a universal source in the centered tournament T_b on the ambient tournament H, i.e.
(a,b,z)
is tight for every z outside {a,b}.

Suppose every r-subset S of W were initial-rigid. Choose one rigid Hamilton order on each such S. The functional-graph majority-coloring proof of
[[a_majority_coloring_closes_universal_endpoint_pair_rigidity_and_yields_an_anchored_three_vertex_prefix]]
uses only:
1. the chosen Hamilton orders on r-subsets of the ground set,
2. the universal-source relation in H, and
3. a color class of size at least r.

Since |W|>=2r-1, the same proof applied to the chosen supports inside W gives such a color class and constructs an actual tight (r+1)-path in H. Contradiction.

Therefore:

> Every W subseteq V(H) with |W|>=2r-1 contains an r-support S such that EVERY Hamilton order on S has a non-universal initial pair.

For n=2r+1 this has the particularly useful pair-avoidance form:

> For every prescribed pair x,y of vertices, there exists an r-support
> S subseteq V(H)-{x,y}
> such that every Hamilton order (a,b,...) on S admits a reversed anchor
> (u,b,a)
> with u distinct from a,b.

The terminal version is identical: after fixing any pair x,y, there is an r-support avoiding them such that every Hamilton order has a non-universal terminal pair.

## Interaction with longest reversed-pair deserts

Let
R=(c_1,c_2,...,b,a)
be a longest path with fixed terminal pair (b,a), as in
[[longest_reversed_pair_paths_force_a_large_endpoint_desert_and_a_two_edge_reversal_fan]].
The localized theorem permits a fully non-rigid maximum support while avoiding ANY two selected vertices of R, for example {a,b}, {c_1,c_2}, or one vertex from each end.

Thus the supportwise non-rigidity is not trapped on one support chosen before the fixed-terminal obstruction is known. It may be reselected after the obstruction is exposed, with two prescribed blockers removed. This is a scale-independent selection principle and is the appropriate input for subsequent seam forcing.
