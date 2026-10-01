# A local 4|5|m minimum has a neutral cyclic exchange or three locked five-side labels

## Statement

Let H be a boundary tournament and let C=X|Y|P minimize the quadratic potential Phi within its connected pairwise-repartition component, with |X|=4, |Y|=5, and P=(p_1,...,p_m) of order m>=7. Then at least one of the following holds: (1) there is another spanning three-cover with the same component-order multiset {4,5,m} and hence the same Phi, obtained by a cyclic support exchange x from X to Y, y from Y to P, and one displayed endpoint e of P to X; (2) at least three distinct vertices y of Y are noninsertable into every position of the displayed path P. In case (2), each such y participates in a tight triple reversing some displayed edge of P.

## Body

Apply 8e138afbc628. It gives at least two possible labels x in X; fix one. Both (X-{x}) union {p_1} and (X-{x}) union {p_m} are Hamiltonian, and there is a set J subseteq Y of at least three vertices such that (Y-{y}) union {x} is Hamiltonian for every y in J. Apply 5c95da081ff4 to X|Y|P, this x, and J. For each y in J, either some endpoint truncation of P enlarged by y is Hamiltonian, in which case the three Hamiltonian supports supplied there form a legal equal-size cyclic support exchange and give (1), or y is noninsertable into every position of P. If (1) fails for every y in J, all vertices of J are globally noninsertable into the displayed order of P, proving the first part of (2). Apply noninsertable_family_reversal01 to P and J to obtain one displayed-edge reversal witness for each y in J.
