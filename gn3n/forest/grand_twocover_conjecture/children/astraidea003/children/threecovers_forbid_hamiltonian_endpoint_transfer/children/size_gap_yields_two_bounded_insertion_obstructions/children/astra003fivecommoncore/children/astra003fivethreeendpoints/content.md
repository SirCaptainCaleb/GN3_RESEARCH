# A five-vertex side synchronizes at least three of four surrounding endpoints

## Statement

Let X|P|Q minimize the quadratic potential in a connected component of the pairwise-repartition graph containing no two-cover, with |X|=5, |P|>=7, and |Q|>=7. Then there is x in V(X) such that (V(X)-{x}) union {e} is Hamiltonian for at least three of the four endpoints e of P and Q.

## Body


Write P=(p_1,...,p_m), Q=(q_1,...,q_k), with m,k>=7, and let
E={p_1,p_m,q_1,q_k}.

Fix e in E, and let R be the path among P,Q having endpoint e. Since |R|-|X|>=2, the endpoint-transfer theorem says that V(X) union {e} is non-Hamiltonian: otherwise moving e into X would replace the size pair (5,|R|) by (6,|R|-1) and strictly decrease the quadratic potential.

Every six-vertex boundary tournament contains at least four Hamiltonian five-vertex induced subtournaments. In V(X) union {e}, deleting e leaves V(X), which is Hamiltonian. Therefore for at least three vertices x in V(X), the five-set
(V(X)-{x}) union {e}
is Hamiltonian. Let I_e be this subset of V(X); then |I_e|>=3 for every e in E.

There are at least 4*3=12 incidences (x,e) with x in I_e. Since V(X) has five vertices, some x is incident with at least ceil(12/5)=3 endpoints e. For this x, the same four-set V(X)-{x} extends to a Hamiltonian five-set with at least three of the four endpoints of P and Q.

This strengthens the two-end common-core phenomenon by synchronizing the two larger paths through one common four-vertex support.
