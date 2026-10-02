# Every saturated endpoint five-side forces complementary support crossing

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing quadratic potential in its pairwise-repartition component, with |X|=4 and P=(p_1,...,p_m), m>=7. Put E={p_1,p_m} and R=(p_2,...,p_{m-1}). Then for every x in X the five-set F_x=E union (X-{x}) is Hamiltonian and H-F_x is non-Hamiltonian with path-cover number two; moreover every two-cover A|B of H-F_x has at least one component meeting both V(Q) and V(R) union {x}. Thus the four endpoint-rooted five-sides force four simultaneous support-crossing families across the inherited cut (R+x)|Q.

## Body

By a_locally_minimal_fourside_saturates_its_twoendpoint_sixshell, for every x in X the five-set
F_x=E union (X-{x})
is Hamiltonian, H-F_x is non-Hamiltonian with path-cover number two, and R union {x} is non-Hamiltonian.

Fix x and let A|B be any two-cover of H-F_x. Its vertex set is the disjoint union
V(H-F_x)=(V(R) union {x}) disjoint-union V(Q).

Suppose neither A nor B meets both sides of this displayed cut. Since A and B partition all vertices and there are exactly two nonempty cover components, one component must have support exactly V(R) union {x} and the other exactly V(Q). But Q is Hamiltonian while H[V(R) union {x}] is non-Hamiltonian, so such a two-cover is impossible.

Hence at least one of A,B crosses the inherited support cut. The argument is uniform for every x in X, giving four endpoint-rooted Hamiltonian five-sides whose complementary two-covers are all forced to rewire the original support partition.