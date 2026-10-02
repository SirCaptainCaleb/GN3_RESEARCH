# A one-gap lower square either produces a positioned small window or routes the gap through the opposite top component

## Statement

Assume the one-gap square setting of disturbances_universal_internality_collapses_to_a_onegap_square. Thus a top two-cover of G has displayed form
P=(L,y,m,z,R) | Q,
where L,R,Q are nonempty, y and z are internal in every two-cover of G, and a lower two-cover T of G-{y,z} has exactly two transitions between the four inherited classes V(L), {m}, V(R), V(Q), with each class occurring as one intact block in its inherited order.

Then at least one of the following holds:
(1) T has relative-order disagreement with the top displayed paths;
(2) there is a proper Hamiltonian support of order four or five containing the tight triple (y,m,z) and at least one T-neighbor of m, with non-Hamiltonian path-cover-two complement;
(3) m is incident with exactly one cross-class transition of T, and its neighboring block is Q;
(4) m is a singleton component of T, and the other component has block order L,Q,R.

Consequently, after excluding relative-order disagreement and positioned Hamiltonian four/five-windows, every lower cover in the one-gap residue attaches the singleton gap only through the opposite top component Q: either m is terminal next to Q, or m is isolated while Q bridges L to R.

## Body

Let the two cross-class transitions of T define the adjacency pattern of the four intact blocks L,{m},R,Q.

First suppose both transitions are incident with m. Then m is internal in one displayed component of T; write a,m,b for the three consecutive vertices around it, where a and b lie outside {m}. Consider U={a,y,m,z,b}. If U is Hamiltonian, outcome (2) holds. If U is non-Hamiltonian, the certified five-set small-order theorem says that at most one of its five four-subsets is non-Hamiltonian. Hence the two four-sets U-{a}={y,m,z,b} and U-{b}={a,y,m,z} cannot both be non-Hamiltonian. One is Hamiltonian, giving outcome (2). In a minimum counterexample every such proper Hamiltonian support has non-Hamiltonian path-cover-two complement.

Now suppose exactly one cross-class transition is incident with m. If the neighboring block is L, then either the T-component orders m before L, which reverses the top order L before m and gives outcome (1), or its terminal block sequence is L,m. In the latter case replace that terminal sequence by the top-path segment L,y,m,z. This preserves any earlier block transition in the same T-component, covers the same lower vertices plus y,z, and ends at z. The other T-component is unchanged, producing a two-cover of G with z displayed as an endpoint, contrary to the universal internality of z. The case in which m is adjacent only to R is symmetric: either R precedes m and gives outcome (1), or the initial block sequence m,R can be replaced by y,m,z,R, producing a two-cover of G with y displayed as an endpoint. Therefore, absent (1), a degree-one m can only be adjacent to Q, which is outcome (3).

Finally suppose no cross-class transition is incident with m. Then {m} is one component of T and the other component concatenates L,R,Q using both transitions. If L and R occur in reverse relative order, outcome (1) holds. If L and R are adjacent in their top order L,R, replace that adjacent pair by the top segment L,y,m,z,R. The remaining Q-transition is unchanged, so this creates one Hamilton path covering all of G, contradicting that G is non-Hamiltonian. Hence Q must lie between L and R. Excluding the reverse order leaves exactly the block order L,Q,R, which is outcome (4).