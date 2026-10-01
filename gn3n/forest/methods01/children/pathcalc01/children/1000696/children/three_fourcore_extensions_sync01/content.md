# Three Hamiltonian extensions of one four-set force gluing, order disagreement, a Hamiltonian four-set, or reversal

## Statement

Let H be a boundary tournament, let C be a four-vertex set, and let r_1,r_2,r_3 be distinct vertices outside C. For each i choose a Hamilton path P_i on C union {r_i}. Then at least one of the following occurs:
(1) two of P_1,P_2,P_3 have order disagreement on C;
(2) for some i!=j, C union {r_i,r_j} is Hamiltonian;
(3) H contains a Hamiltonian four-vertex set inside C union {r_1,r_2,r_3};
(4) for some i!=j and c in C, a tight triple on {r_i,c,r_j} reverses a displayed root-core edge of P_i or P_j.

## Body

If two chosen paths P_i,P_j order the common vertices of C differently, outcome (1) holds. Hence assume all three induce one common relative order
R=(c_1,c_2,c_3,c_4)
on C. Since each P_i has only one vertex outside C, it is obtained by inserting r_i into one gap g_i of R.

Fix i!=j and apply d495c62905f0 to P_i,P_j.

If |g_i-g_j|>=2, the two insertions glue to a Hamilton path on C union {r_i,r_j}, giving outcome (2).

If the gaps are adjacent, d495c62905f0 gives either the same Hamiltonian six-set or the reverse tight triple through the unique common core vertex between the two gaps. In the latter case that triple reverses the displayed root-core edge of whichever P_i or P_j inserts its root immediately beside the common core vertex, giving outcome (4).

If g_i=g_j is an internal gap u|v, d495c62905f0 gives a Hamiltonian four-set {u,v,r_i,r_j}, giving outcome (3).

Suppose none of (1)-(4) occurs. Then for every pair i!=j the two roots occupy one common endpoint gap of R. Pairwise equality forces all three roots into the same endpoint gap. Deleting any root from its Hamilton path shows that R itself is a tight Hamilton path on C.

Assume first that all three roots left-extend R, so P_i=(r_i,R). For distinct i,j, if either (r_i,r_j,c_1) or (r_j,r_i,c_1) were tight, then (r_i,r_j,R) or (r_j,r_i,R) would be a Hamilton path on C union {r_i,r_j}, giving outcome (2). Hence both triples are non-tight, and boundary antisymmetry gives
(c_1,r_i,r_j)
tight for every ordered pair of distinct roots.

Exactly one of the boundary-flip pair
(r_1,r_2,r_3), (r_3,r_2,r_1)
is tight. In the first case (c_1,r_1,r_2,r_3) is a Hamilton path; in the second, (c_1,r_3,r_2,r_1) is. Thus {c_1,r_1,r_2,r_3} is Hamiltonian, giving outcome (3).

The common right-endpoint case is symmetric: failure of every pair-union forces (r_i,r_j,c_4) tight for every ordered pair i!=j, and one of (r_1,r_2,r_3,c_4), (r_3,r_2,r_1,c_4) is a Hamilton path.

Hence one of (1)-(4) always occurs. ∎