# Corrected island packet indices and the empty connector condition — preserved pre-item development

## Exact packet and tail orders

This corrects the indexing and strengthens the genuine-deletion-distance condition in [[rigid_010_island_reduces_to_one_canonical_six_packet]].

For C=(c_1,...,c_N) with status word 1^u010^v, the word has u+v+2 statuses, hence N=u+v+4. Its canonical cover is
\[
P=(c_1,\ldots,c_{u+2}),\qquad Q=(c_N,\ldots,c_{u+3}),
\]
with orders u+2 and v+2. In the genuine kappa_2(H[J])=2 branch, [[one_path_complement_bounds_sharpen_the_genuine_double_corridor_profiles]] proves u,v>=3.

Keep the central packet
\[
S=\{x,y,c_{u+1},c_{u+2},c_{u+3},c_{u+4}\}
\]
and tails
\[
T=(c_1,\ldots,c_u),\qquad
U=(c_N,c_{N-1},\ldots,c_{u+5}).
\]
The exact tail orders are |T|=u and |U|=v, not v+1. They are tight contiguous subpaths, each of order at least three. The packet and tails partition J.

For every z in S, both candidate orders (T,z,U) and (U,z,T) must fail. Indeed either tight order would leave just the five-set S-z uncovered; a Hamiltonian four-subset of that five-set gives a two-cover after one deletion, contradicting kappa_2=2. Thus the residual connector set is empty, rather than merely confined to at most two non-Hamiltonian packet deletions.

The exact necessary clauses are
\[
h(c_{u-1},c_u,z)\,
h(c_u,z,c_N)\,
h(z,c_N,c_{N-1})=0
\]
and
\[
h(c_{u+6},c_{u+5},z)\,
h(c_{u+5},z,c_1)\,
h(z,c_1,c_2)=0,
\qquad z\in S.
\]
All 36 triple tests are supported on S together with the first two and last two vertices of T and U, a set of at most fourteen vertices. This is a finite list of necessary interface constraints. It is not a completeness theorem: the untouched tail interiors can still affect alternative Hamilton orders and other attachment constructions.

At the first possible island order twelve, u=v=3 and the tail orders are 3|3. All six-subsets of J are non-Hamiltonian by the one-path complement bound, so in particular S itself is non-Hamiltonian, while at least four of its five-subsets are Hamiltonian by [[smallset01]]. Attachment of those supports remains an explicit obligation.

The alternative phrasing in which one forces a third connector can be replaced, for the genuine two-deletion branch, by the stronger goal of forcing even one connector. For kappa_2=1, a single connector only reproves deletion distance at most one; its packet complement must still be Hamiltonian to obtain a full two-cover.
