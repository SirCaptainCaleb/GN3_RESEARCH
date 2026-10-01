# Every vertex of a four-vertex component in a global quadratic minimum is noninsertable into both long paths

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers of H, where |X|=4 and |P|,|Q|>=6. Then for every x in V(X), each endpoint truncation of P enlarged by x is non-Hamiltonian, and each endpoint truncation of Q enlarged by x is non-Hamiltonian. Consequently every vertex of X is noninsertable into every position of the displayed orders of both P and Q.

## Body

Write |P|=m and |Q|=r. Fix x in V(X), an endpoint e of P, and an endpoint f of Q.

By b7606848ddee, the five-set
F=(V(X)-{x}) union {e,f}
is Hamiltonian.

Suppose first that
(V(P)-{e}) union {x}
is Hamiltonian. The three supports
F,
(V(P)-{e}) union {x},
V(Q)-{f}
are pairwise disjoint and partition V(H). The third support has the inherited endpoint-truncated tight path of Q. Hence they form a spanning three-cover with component orders
5,m,r-1.

Its quadratic potential is
25+m^2+(r-1)^2.
The original globally minimal cover has potential
16+m^2+r^2.
Thus
Phi(original)-Phi(new)
=16+m^2+r^2-[25+m^2+(r-1)^2]
=2r-10>0
because r>=6. This contradicts global minimality. Therefore every endpoint truncation of P enlarged by x is non-Hamiltonian.

The symmetric argument supposes that
(V(Q)-{f}) union {x}
is Hamiltonian and uses the three supports
F,
V(P)-{e},
(V(Q)-{f}) union {x}.
Their component orders are
5,m-1,r,
and the potential drop from the original cover is
2m-10>0.
Hence every endpoint truncation of Q enlarged by x is also non-Hamiltonian.

Since x was arbitrary, the conclusion holds for all four vertices of X and for both endpoint truncations of each long path.

Finally, if some x in X could be inserted at any position of the displayed order of P, deleting a suitable endpoint of that inserted Hamilton path would preserve the insertion and give a Hamilton path on one of the two endpoint truncations of P enlarged by x: for an extreme insertion delete the opposite endpoint, and for an internal insertion delete an endpoint outside the local insertion. This contradicts the preceding non-Hamiltonicity. Thus x is noninsertable into the displayed order of P. The same argument applies to Q.

Therefore every vertex of X is noninsertable into both displayed long paths. ∎
