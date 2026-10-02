# A five-side beside a path of order at least six gives nonincreasing transport or a common endpoint core

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover, where X is a tight path of order five and P=(p_1,...,p_m) has m>=6. Then either one endpoint transfer from P into X gives a legal spanning three-cover whose quadratic potential changes by 12-2m (neutral for m=6 and strictly decreasing for m>=7), or there exists x in V(X) such that both five-sets (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_m} are Hamiltonian.

## Body

If H[V(X) union {p_1}] is Hamiltonian, replace X|P by a Hamilton path on X union {p_1} together with the inherited path P-p_1. The size pair changes from (5,m) to (6,m-1), with Delta Phi=36+(m-1)^2-(25+m^2)=12-2m, which is zero for m=6 and negative for m>=7. The same applies to p_m. Hence if no such nonincreasing endpoint transfer exists, both six-sets S_1=V(X) union {p_1} and S_m=V(X) union {p_m} are non-Hamiltonian. By the four-of-six theorem, each has at least four Hamiltonian five-vertex deletions. Deleting the endpoint p_i leaves X, which is Hamiltonian, so for each endpoint at least three vertices x in X yield a Hamiltonian replacement (X-{x}) union {p_i}. The two good-label subsets of X each have size at least three, hence intersect because |X|=5. Any common x gives the asserted four-core. No extremality or minimum-counterexample hypothesis is used.