# A global quadratic minimum with a four-vertex component has a complete endpoint-pair Hamiltonian five-set grid

## Statement

Let H be a boundary tournament and let X|P|Q minimize Phi=sum |C_i|^2 among all spanning three-covers of H, with |X|=4 and |P|=m, |Q|=r at least six. Let E be the set consisting of the two displayed endpoints of P and the two displayed endpoints of Q. Then for every x in V(X) and every two-element set {e,f} subset E, the five-set (V(X)-{x}) union {e,f} is Hamiltonian.

Moreover, if e,f lie on different long paths, then V(X) union {e,f} is non-Hamiltonian. If e,f are the two endpoints of one long path of order at least seven, the same conclusion holds. If they are the two endpoints of a long path of order six, then either V(X) union {e,f} is non-Hamiltonian or its Hamiltonicity yields a Phi-neutral repartition replacing the pair of component orders 4,6 by 6,4, with the new four-vertex component equal to the inherited middle four vertices of that long path.

## Body

Put X_0=V(X). First fix any displayed endpoint e of either P or Q. The five-set X_0 union {e} is non-Hamiltonian. Indeed, if e is an endpoint of P and X_0 union {e} were Hamiltonian, then replacing X|P by (X_0 union {e}) | (P-e) would change the pair of component orders 4,m to 5,m-1. The potential drop would be
16+m^2-[25+(m-1)^2]=2m-10>0,
contradicting global minimality. The argument for an endpoint of Q is identical.

Now fix two distinct endpoints e,f in E and put
S=X_0 union {e,f}.
Both five-vertex deletions S-{e}=X_0 union {f} and S-{f}=X_0 union {e} are non-Hamiltonian by the preceding paragraph.

By the certified four-of-six theorem, at least four of the six one-vertex deletions of S are Hamiltonian. The only four deletions not already known to be non-Hamiltonian are
S-{x}=(X_0-{x}) union {e,f},
x in X_0.
Hence all four of these five-sets are Hamiltonian. Since {e,f} was arbitrary, this gives the complete 4 by binom(4,2) grid.

It remains to classify when S itself could be Hamiltonian. Suppose first that e is an endpoint of P and f an endpoint of Q. If S were Hamiltonian, then
S | (P-e) | (Q-f)
would be a spanning three-cover with component orders 6,m-1,r-1. Relative to the original 4,m,r cover, the potential drop is
16+m^2+r^2-[36+(m-1)^2+(r-1)^2]=2(m+r-11)>0,
because m,r>=6. Thus every cross-path endpoint six-set S is non-Hamiltonian.

Next suppose e,f are the two endpoints of P. If S were Hamiltonian, then
S | (P-{e,f}) | Q
would be a spanning three-cover with component orders 6,m-2,r. The potential difference is
16+m^2+r^2-[36+(m-2)^2+r^2]=4m-24.
For m>=7 this is positive, contradicting global minimality. For m=6 it is zero. In that boundary case Hamiltonicity of S gives a legal Phi-neutral repartition of X|P from component orders 4,6 to 6,4, and the new four-vertex component is precisely the inherited middle path P-{e,f}. The argument for the two endpoints of Q is symmetric.

Thus the only endpoint-pair six-sets not forced non-Hamiltonian are same-path endpoint pairs on a six-vertex path, and in that boundary case Hamiltonicity gives the stated Phi-neutral support swap. ∎
