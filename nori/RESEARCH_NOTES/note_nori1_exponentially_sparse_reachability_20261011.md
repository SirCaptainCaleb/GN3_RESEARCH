# Exponentially sparse reachability and successful roots in NORI1

- Stable ID: note_nori1_exponentially_sparse_reachability_20261011
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: proved, reachability, obstruction, topological-approach, root-density
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6173_1
- Updated session: session_nori_r6173_1
- Disposition: none
- Successor: none

## Related references

- note:note_antipodal_midpoint_splice_candidate
- note:note_rooted_restriction_and_good_root_density_limitations

## Research note

**Theorem.** For every $h\ge1$, there is an antipodally odd coloring of the undirected edges of $Q_{2h}$ such that
\[
\max_{a\in Q_{2h}}|R(a)|=2\cdot3^h-2^h,
\]
where $R(a)$ consists of vertices reached by monochromatic geodesics rooted at $a$, in either color. In particular $\max_a|R(a)|/2^{2h}\to0$ exponentially. The coloring has a monochromatic antipodal geodesic.

**Proof.** Pair the coordinate directions as $(u_j,v_j)$, $1\le j\le h$, and define $c_{u_j}(x)=x_{v_j}$ and $c_{v_j}(x)=x_{u_j}$. Both rules are invariant under flipping the traversed coordinate and change under antipodal complementation.

For a fixed root $a$, let $u,v,t$ count its coordinate pairs initially in states $(0,0)$, $(1,1)$, and mixed, respectively; $u+v+t=h$. In one pair, the endpoints reachable by a color-zero geodesic number three except when the initial state is $(1,1)$, in which case only the initial state is reachable. For color one, the exceptional state is $(0,0)$. The two local reachability sets intersect in the initial state for equal-bit roots, and in the initial state and its antipode for mixed roots. Since an edge color in a pair depends only on that pair, monochromatic reachable sets factor as products over pairs. Inclusion–exclusion therefore yields
\[
|R(a)|=3^{h-v}+3^{h-u}-2^t. \tag{1}
\]
Changing any equal-bit pair to a mixed pair strictly increases (1): changing one $(0,0)$ pair raises (1) by $2\cdot3^{h-u}-2^t>0$, and changing one $(1,1)$ pair raises it by $2\cdot3^{h-v}-2^t>0$, with the variables on the right referring to the state before replacement. Hence the maximum occurs when $t=h$, giving $2\cdot3^h-2^h$.

At the root with all pairs $(0,1)$, traverse $v_1,u_1,v_2,u_2,\ldots,v_h,u_h$. Every edge has color zero, and the path is antipodal. $\square$

**Consequence.** No uniform positive-density lower bound on $R(a)$, even with the root chosen freely, follows from the NORI1 edge-coloring axioms. Antipodal-pair intersection must be established through structure beyond the cardinality of the reachable set.

**Successful-root theorem.** For this coloring, the number of vertices from which a monochromatic full antipodal geodesic starts is $2^h$, a proportion $2^{-h}$ of all roots.

**Proof.** In one coordinate pair with initial bits $(s,t)$, the orders $(u_j,v_j)$ and $(v_j,u_j)$ give local color words $(t,1-s)$ and $(s,1-t)$, respectively. Either word is constant precisely when $s\ne t$. Since the colors in a coordinate pair depend only on that pair, interleaving other directions cannot alter this condition. Hence a monochromatic full geodesic is possible only when every pair of root bits is unequal. If all pairs are unequal, choose in each pair the order with both edges colored zero, and concatenate these orders. There are two choices of unequal bits in each of the $h$ pairs, giving $2^h$ successful roots. $\square$

The nearest successful root to $0^{2h}$ has Hamming distance $h$.
