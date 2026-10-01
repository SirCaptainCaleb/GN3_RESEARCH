# The common-end residue of adjacent six-side swaps is a singleton support swap or reverse endpoint data

## Statement

Let H be a minimum counterexample and let C=X|P|Q be a Phi-minimal spanning three-cover in its pairwise-repartition component, with
X=U disjoint-union {a,b,c}, |U|=3,
P=(e,M,f)
of order at least eight.
Assume {a,b} and {a,c} are two adjacent common shell edges for the endpoint roots e,f, and assume both edges realize the Phi-neutral swap alternative of 5a58f63e599d. Thus the four supports
U union {c,e,f},  M union {a,b},
U union {b,e,f},  M union {a,c}
are Hamiltonian.

Assume the two long Hamilton paths on M union {a,b} and M union {a,c} induce the same relative order on their common support K=M union {a}, and that the compatible-extension gluing lemma d495c62905f0 lands in its common-endpoint-gap residue for the exceptional labels b,c. Then either:

(1) explicit order disagreement occurs;

(2) two explicit reverse endpoint triples through b,c and one endpoint of the common tight path K occur; or

(3) there is a legal Phi-neutral one-for-one repartition of X|P exchanging a with one displayed endpoint of P. More precisely, if b,c both extend the initial end of K, then either (2) holds or
(X-{a}) union {f} | (P-{f}) union {a}
is a two-component cover of H[V(X) union V(P)];
the terminal-end version exchanges a with e.

Thus the common-endpoint residue of two adjacent neutral shell swaps is not stationary: absent order disturbance it produces a genuine singleton support swap.

## Body

Treat the case in which b and c both extend the initial end of the common tight path K; the other end is symmetric. Because the common K-order contains M in inherited relative order, K is obtained by inserting a into the displayed order M.

First suppose f extends the terminal end of K. Since the d495c62905f0 branch under discussion is the common-endpoint residue, K union {b,c} is non-Hamiltonian. Write K=(k_1,...,k_s). Both (b,K) and (c,K) are tight, and (K,f) is tight. If (b,c,k_1) were tight, then (b,c,K) would be a Hamilton path on K union {b,c}; similarly (c,b,k_1) would Hamiltonize that support. Hence both triples are non-tight. Boundary antisymmetry gives both reverse endpoint triples
(k_1,c,b), (k_1,b,c)
tight. This is (2).

Now suppose f does not extend K. Write M=(m_1,...,m_t). If a were inserted before the last two gaps of M, then the last two vertices of K would still be m_{t-1},m_t, and the inherited tight triple (m_{t-1},m_t,f) from P would make f a terminal extender of K. Therefore a occupies one of the two terminal insertion positions of M. Since t>=6, the first two vertices of K remain m_1,m_2, so the inherited triple (e,m_1,m_2) makes
P'=(e,K)
a tight Hamilton path on (V(P)-{f}) union {a}.

Put
X'=(V(X)-{a}) union {f}=U union {b,c,f}.
The common-shell property for the root f and the two edges {a,b},{a,c} says that U union {c,f} and U union {b,f} are Hamiltonian five-vertex deletions of X'. If X' is non-Hamiltonian, the four-of-six theorem supplies at least four Hamiltonian vertex deletions of X', and astra004fourgooddisagree yields explicit order disagreement. Hence in the no-order-disagreement branch X' is Hamiltonian.

Therefore X'|P' is a two-component cover of H[V(X) union V(P)]. Both new component orders equal the old orders 6 and |P|, so replacing X|P by X'|P' is a legal Phi-neutral repartition. At the support level it exchanges only a and f. This is (3).

The terminal-end case is obtained by reversing the argument: if e does not extend the initial end of K, then a lies in one of the two initial insertion positions of M, K can be followed by f, and the resulting neutral repartition exchanges a with e.
