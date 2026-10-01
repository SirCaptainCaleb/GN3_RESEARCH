# A five-vertex side has a common four-vertex endpoint extension core

## Statement

Let X|P|Q be a spanning three-path cover minimizing the quadratic potential in a connected component of the pairwise-repartition graph that contains no two-cover. Suppose |X|=5 and P=(p_1,...,p_m) has m>=7. Then there is a vertex x in V(X) such that both induced five-sets (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_m} are Hamiltonian.

## Body

Let X|P|Q minimize the quadratic potential Phi inside a connected component of the pairwise-repartition graph containing no two-cover, where X is a tight path of order five and P=(p_1,...,p_m) with m>=7.

Because m-5>=2, transferring either single endpoint of P to X would strictly improve the size pair (5,m) to (6,m-1). The endpoint-transfer theorem therefore gives that both six-sets
S_1=V(X) union {p_1},  S_m=V(X) union {p_m}
are non-Hamiltonian.

Every six-vertex boundary tournament has at least four Hamiltonian five-vertex induced subtournaments. In S_1, deleting p_1 leaves V(X), which is Hamiltonian because X itself is a tight five-path. Hence among the five vertices x in V(X), at least three satisfy
(V(X)-{x}) union {p_1}
Hamiltonian. Let I_1 be this set of at least three vertices of X.

The same argument for S_m gives a set I_m subseteq V(X), |I_m|>=3, such that
(V(X)-{x}) union {p_m}
is Hamiltonian for every x in I_m.

Since |V(X)|=5, two subsets of sizes at least three intersect. Choose x in I_1 intersect I_m. Then the common four-set V(X)-{x} extends to a Hamiltonian five-set with either endpoint of P, as claimed.

This is a synchronized consequence of quadratic minimality: the two endpoint non-Hamiltonicity constraints cannot behave independently on a five-vertex side. They force a common four-vertex support admitting Hamiltonian replacement by either endpoint of the larger path.
