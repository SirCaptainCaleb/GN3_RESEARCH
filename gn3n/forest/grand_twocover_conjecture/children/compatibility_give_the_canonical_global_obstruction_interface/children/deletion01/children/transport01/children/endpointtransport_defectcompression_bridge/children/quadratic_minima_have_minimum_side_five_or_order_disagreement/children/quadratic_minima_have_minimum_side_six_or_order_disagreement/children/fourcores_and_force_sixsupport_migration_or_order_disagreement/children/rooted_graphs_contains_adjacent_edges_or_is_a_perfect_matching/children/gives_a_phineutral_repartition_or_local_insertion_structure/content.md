# An edge common to two rooted graphs gives a Phi-neutral repartition or local insertion structure

## Statement

Let H be a boundary tournament and let C=X|P|Q be a spanning three-cover minimizing Phi in its pairwise-repartition component, where |X|=6 and P=(e,m_1,...,m_t,f) has order at least eight. Let G_e,G_f be the rooted graphs on V(X) defined in 0c8144b5ac80, let {a,b} be an edge of both G_e and G_f, and put D=V(X)-{a,b}, M=(m_1,...,m_t). Then at least one of the following occurs: (1) order disagreement; (2) both S=D union {e,f} and R=V(M) union {a,b} are Hamiltonian, so replacing X|P by S|R is a Phi-neutral repartition with component orders 6 and |P|; (3) at least one of a,b is noninsertable into M and therefore satisfies one of the local alternatives of insert01; (4) {a,b} together with one displayed edge of M is a Hamiltonian four-set; (5) a tight triple (a,m_i,b) or (b,m_i,a) occurs for some m_i in M; (6) a,b insert at the same endpoint of M, and 7b9f6ae39813 gives either a Hamiltonian path on V(M) together with a,b and the opposite endpoint of P, or two explicit reverse endpoint triples.

## Body


By 0c8144b5ac80, the edge common to G_e and G_f gives Hamiltonicity of D union {e} and D union {f}. The same theorem says that the six-set S=D union {e,f} is Hamiltonian unless explicit order disagreement already occurs. Hence assume no order disagreement and S Hamiltonian.

Put R=V(M) union {a,b}. If R is Hamiltonian, S|R is a two-component repartition of V(X) union V(P). Both new component orders equal the old orders: |S|=6=|X| and |R|=|P|. Thus it is a legal Phi-neutral repartition, giving (2).

Assume R is non-Hamiltonian. If either a or b is noninsertable into the displayed path M, apply insert01 to that label and M, giving (3). Hence assume both labels are individually insertable into M.

If either label has two distinct successful insertion positions, the two resulting Hamilton paths on the same one-label enlargement order that label differently relative to some inherited M-vertex, giving order disagreement. Thus in the order-neutral branch each label has a unique insertion position.

If the two unique insertion positions differ by at least two, astra003twoinsertlocal simultaneously inserts a and b into M, Hamiltonizing R, contradiction. Hence the positions are equal or adjacent.

If they are adjacent, astra003uniquegaplocal says either simultaneous insertion succeeds, again contradicting non-Hamiltonicity of R, or the reverse cross triple through the shared old M-vertex is tight. This is (5).

If they are equal at an internal gap u|v, astra003uniquegaplocal gives a Hamiltonian four-set {u,v,a,b}, which is (4).

It remains that both labels have the same endpoint insertion position in M. Suppose first they both left-extend M. The inherited path P supplies the opposite right extension (M,f). Apply 7b9f6ae39813 to a,b,M,f. It yields either a Hamiltonian path on V(M) union {a,b,f}, of order |P|+1, or the two explicit reverse triples through the initial vertex of M. In the Hamiltonian branch, D union {e} is already Hamiltonian from the common-edge hypothesis, so these two paths give a two-component repartition of V(X) union V(P) with orders 5 and |P|+1. The reverse-triple branch is bounded endpoint data. The common right-end insertion case is symmetric, using e as the inherited opposite extender. This is (6).

All possibilities are exhausted.
