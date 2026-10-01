# Safe outer endpoints force repeated noninsertability witnesses from C_0

## Statement

Let H-x=P_0|Q_0 be a deletion cover with P_0=(p_0,...,p_m), Q_0=(q_0,...,q_s), and put C_0={q_1,q_0,x,p_m,p_{m-1}}. Assume the three-cover (p_0,...,p_{m-2}) | (q_1,q_0,x,p_m,p_{m-1}) | (q_2,...,q_s) lies in a connected component ℱ of the pairwise-repartition graph. Suppose ℱ contains a Phi-minimal three-cover X|P|Q with |X|=5 and |P|,|Q|>=7. Among all Phi-minimal covers in ℱ with a five-vertex component, choose X|P|Q maximizing mu=|X-C_0|. Call a displayed endpoint e of P or Q safe when e is not in C_0. Then:

(1) at least 4-mu of the four displayed endpoints are safe;

(2) for every safe endpoint e, at least 3-mu vertices x in X intersect C_0 satisfy H[(X-{x}) union {e}] Hamiltonian;

(3) for every such pair (x,e), if R is the component P or Q having endpoint e, then H[(R-{e}) union {x}] is non-Hamiltonian. Hence x is noninsertable into the inherited displayed order R-e and satisfies one of the bounded local alternatives of insert01.

Consequently, if mu=0, some vertex of C_0 is associated in (2)-(3) with at least three displayed outer endpoints; if mu=1, some vertex of X intersect C_0 is associated with at least two safe endpoints; if mu=2, there are at least two safe-endpoint/vertex incidences, and if no vertex of C_0-X is itself a displayed outer endpoint, then some vertex of X intersect C_0 is associated with at least two endpoints.

## Body


Because X|P|Q is Phi-minimal and each outer component has order at least seven, adjoining any displayed outer endpoint e to X would change pair sizes 5,m to 6,m-1 with strict Phi decrease. Hence X union {e} is non-Hamiltonian.

Fix a safe endpoint e. The six-set X union {e} is non-Hamiltonian while deleting e leaves the Hamiltonian five-set X. By the four-of-six theorem, at least three vertices x in X satisfy
(X-{x}) union {e}
Hamiltonian.

Exactly mu vertices of X lie outside C_0. Therefore among these at least three vertices x, at least 3-mu lie in X intersect C_0. This proves (2).

Fix such x, and let R be the outer component with endpoint e. Suppose for contradiction that
(R-{e}) union {x}
is Hamiltonian. Then the Hamiltonian supports
(X-{x}) union {e}
and
(R-{e}) union {x}
give a legal pairwise repartition of X|R preserving component orders 5 and |R|. Hence the new state is again Phi-minimal in ℱ and still has a five-vertex component
X'=(X-{x}) union {e}.

Because x is in C_0 while the safe endpoint e is not in C_0,
|X'-C_0|=|X-C_0|+1=mu+1,
contradicting maximality of mu. Therefore (R-{e}) union {x} is non-Hamiltonian. Any successful insertion of x into the inherited path R-e would Hamiltonize that support, so x is noninsertable and the noninsertability theorem insert01 supplies one of its bounded local alternatives. This proves (3).

For (1), X contains exactly 5-mu vertices of C_0, so exactly mu vertices of C_0 lie outside X, all in P union Q. Hence among the four displayed endpoints at most mu can belong to C_0.

The incidence consequences are now elementary.

If mu=0, all four endpoints are safe and each has at least three witnesses in the five-element set X=C_0. There are at least 12 incidences, so one label occurs at least ceil(12/5)=3 times.

If mu=1, at least three endpoints are safe and each has at least two witnesses in the four-element set X intersect C_0. Thus there are at least six incidences, so one label occurs at least twice.

If mu=2, at least two endpoints are safe and each has at least one vertex of X intersect C_0. If neither of the two vertices of C_0-X is an outer endpoint, all four endpoints are safe, giving at least four incidences over the three-element set X intersect C_0, so one vertex of X intersect C_0 occurs at least twice. Otherwise a vertex of C_0-X itself appears at an outer endpoint. ∎
