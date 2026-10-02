# Every vertex of a four-vertex component remains noninsertable after deleting both endpoints of either long path

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover minimizing Phi among all spanning three-covers, with |X|=4 and |P|=m, |Q|=r at least six. Write P=(p_1,...,p_m) and Q=(q_1,...,q_r). Then for every x in X, both induced subtournaments
H[(V(P)-{p_1,p_m}) union {x}]
and
H[(V(Q)-{q_1,q_r}) union {x}]
are non-Hamiltonian. Consequently every x in X is noninsertable into the displayed middle paths (p_2,...,p_{m-1}) and (q_2,...,q_{r-1}).

## Body

We prove the assertion for P; the argument for Q is symmetric. Put e=p_1 and e'=p_m.

First, both five-sets V(X) union {e} and V(X) union {e'} are non-Hamiltonian. If, for example, V(X) union {e} were Hamiltonian, then
(V(X) union {e}) | (P-e) | Q
would be a spanning three-cover with component orders 5,m-1,r. Its quadratic potential is lower than that of X|P|Q by
16+m^2-[25+(m-1)^2]=2m-10>0,
contradicting global minimality. The same calculation applies to e'.

Apply the certified four-of-six theorem to
S=V(X) union {e,e'}.
The deletions S-{e}=V(X) union {e'} and S-{e'}=V(X) union {e} are non-Hamiltonian. Therefore all four remaining one-vertex deletions are Hamiltonian:
S-{x}=(V(X)-{x}) union {e,e'}
is Hamiltonian for every x in V(X).

Fix x in V(X) and suppose
M_x=(V(P)-{e,e'}) union {x}
were Hamiltonian. The three supports
S-{x},
M_x,
V(Q)
are pairwise disjoint and partition V(H), so they form a spanning three-cover with component orders 5,m-1,r. Its quadratic potential is
25+(m-1)^2+r^2,
whereas the original globally minimal cover has potential
16+m^2+r^2.
The difference is
16+m^2+r^2-[25+(m-1)^2+r^2]=2m-10>0
because m>=6, a contradiction. Thus M_x is non-Hamiltonian for every x in V(X).

The same proof with Q shows that
H[(V(Q)-{q_1,q_r}) union {x}]
is non-Hamiltonian for every x in V(X).

Finally, if x were insertable into the displayed middle path (p_2,...,p_{m-1}), the resulting order would be a Hamilton path on M_x, contradiction. Likewise x is noninsertable into the displayed middle path of Q.

Thus every vertex of X remains noninsertable after both displayed endpoints of either long path are removed. ∎