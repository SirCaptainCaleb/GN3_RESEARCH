# A five-side beside a path of order at least seven gives strict descent or a common endpoint-extension four-core

## Statement

Let H be a boundary tournament and let C=X|P|Q be a spanning three-cover, where X is a tight path of order five and P=(p_1,...,p_m) has m>=7. Then either one of the endpoint transfers from P into X gives a legal spanning three-cover with strictly smaller quadratic potential, or there is x in V(X) such that both five-sets (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_m} are Hamiltonian.

## Body

If H[V(X) union {p_1}] is Hamiltonian, replace X|P by a Hamilton path on X union {p_1} together with the inherited path P-p_1. The size pair changes from 5,m to 6,m-1 and the quadratic-potential change is 36+(m-1)^2-(25+m^2)=12-2m<0 for m>=7. The same applies to p_m. Hence, unless strict descent already occurs, both six-sets S_1=V(X) union {p_1} and S_m=V(X) union {p_m} are non-Hamiltonian. By the certified four-of-six theorem, each S_e has at least four Hamiltonian five-vertex deletions. Deleting e itself leaves X, which is Hamiltonian, so for each e in {p_1,p_m} at least three vertices x in V(X) satisfy that (V(X)-{x}) union {e} is Hamiltonian. Let I_1,I_m be the two subsets of V(X), each of size at least three. Since |V(X)|=5, I_1 and I_m intersect. Any x in their intersection gives the asserted common four-core. No global or trapped minimality is used.
