# Exponentially sparse antipodal reachability in connected legal colorings

- Stable ID: note_nori_affine_connected_sparse_antipodal_root_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction
- Labels: root-density, product, antipodal-path, counterexample-to-density
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_4
- Updated session: session_nori_r10487_4
- Disposition: none
- Successor: none

## Related references

- subsection:zero_turn_contraction_pointed_odd_girth_and_the_cube_geodesic_distance_defect

## Research note

**Theorem (interaction-connected legal colorings with exponentially sparse monochromatic antipodal roots).** For every \(k\ge1\) there is a legal antipodally odd affine edge coloring \(c^{(k)}\) of \(Q_{2k+1}\), whose direction-interaction graph is connected, such that the vertices admitting a monochromatic antipodal path of **either** color (of arbitrary length) are precisely
\[
S_k=\{x\in Q_{2k+1}:x_{2j-1}\ne x_{2j}\text{ for every }1\le j\le k\}.
\]
Every vertex in \(S_k\) has monochromatic full antipodal geodesics of both colors, and
\[
|S_k|=2^{k+1},\qquad |S_k|/2^{2k+1}=2^{-k}.
\]

*Construction.* Number dimensions \(1,\ldots,2k+1\). For \(1\le j\le k\) set
\[
c_{2j-1}(x)=x_{2j},\qquad c_{2j}(x)=x_{2j-1},
\]
and give the last-direction edge the color
\[
c_{2k+1}(x)=\sum_{i=1}^{2k-1}x_i\pmod2.
\]
Every direction rule is independent of its own bit. Complementing all bits toggles each rule: the first \(2k\) rules depend on one foreign bit, and the final one on \(2k-1\) foreign bits, an odd number. Hence the coloring is legal. The interaction graph contains the matching edges \(\{2j-1,2j\}\) and all star edges \(\{i,2k+1\}\) for \(1\le i\le2k-1\); it is connected.

*Necessity.* Project a monochromatic antipodal walk onto the \(j\)-th pair. In the red graph on this pair, \(00\) is adjacent to \(10\) and \(01\), while \(11\) is isolated. In the blue graph, \(11\) is adjacent to \(10\) and \(01\), while \(00\) is isolated. Neither graph connects \(00\) to \(11\); thus every pair of initial bits must be \(01\) or \(10\). The projection argument applies regardless of path length and of where the last dimension is traversed.

*Sufficiency.* From \(01\) or \(10\), the two-bit red path going through \(00\) connects the root to its antipode and traverses both directions once. Concatenate such two-step paths in all \(k\) pairs. Their lifted product path uses each of the first \(2k\) dimensions once, with all edges red. The final-direction rule \(b(x)=\sum_{i=1}^{2k-1}x_i\) flips parity between the beginning and end of this old-direction path, since all its \(2k-1\) arguments are complemented. Consequently \(b=0\) at one of these endpoints. Insert the last-direction step at that endpoint; all old-direction edge colors are independent of the last bit. The resulting path is a red full antipodal geodesic from the prescribed root, for either initial last bit. Its antipodal reflection followed by reversal is a blue full antipodal geodesic from the same root.

*Additional identity.* In every legal coloring, for every root \(x\), the shortest red path joining \(x\) to \(\bar x\) has the same length, possibly infinity, as the shortest blue path joining the same endpoints: antipodal translation followed by reversal exchanges them. Hence the red, blue and either-color root sets always coincide.

*Scope.* The root-density bound is an obstruction to proving NORI1 through a uniform positive fraction of monochromatically antipodally connected roots, even for connected interaction graphs and arbitrary-length paths. The construction has numerous monochromatic full geodesics and is not a counterexample to NORI1. It strengthens the related sparse paired-root phenomenon in Article XV by imposing the antipodally odd condition and treating unrestricted monochromatic antipodal reachability.
