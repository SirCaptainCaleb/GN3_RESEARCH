# Every cross-endpoint pair around a global quadratic minimum with a four-vertex component forms a rigid non-Hamiltonian six-set

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers of H, where X=(x_0,x_1,x_2,x_3), |P|=m>=6, and |Q|=r>=6. Choose any endpoint e of P and any endpoint f of Q, and put S=V(X) union {e,f}. Then: (1) H[S] is non-Hamiltonian; (2) e and f are not Hamiltonian deletions of S; (3) every x_i is a Hamiltonian deletion of S. Thus the Hamiltonian deletions of S are precisely the four vertices of X. Moreover, for every prescribed x_i in X there is x_j in X-{x_i} such that H[S-{x_i,x_j}] is Hamiltonian; and for arbitrary Hamilton paths chosen on the four Hamiltonian five-sets S-{x_i}, some two chosen paths disagree in relative order on common vertices. Hence each cross-endpoint pair carries a Hamiltonian four-overlap together with a reversed-edge, reversing-triple, or tight-cycle witness inside the same six-set.

## Body

Fix an endpoint e of P and an endpoint f of Q, and put
S=V(X) union {e,f}.

By e0c582e375df, adjoining any endpoint of either long path to V(X) gives a non-Hamiltonian five-set. In particular
S-{f}=V(X) union {e}
and
S-{e}=V(X) union {f}
are non-Hamiltonian. Thus e and f are not Hamiltonian deletions of S.

Apply the four-of-six theorem to S. Every six-set has at least four Hamiltonian five-vertex deletions. Two deletions, namely S-{e} and S-{f}, have just been shown non-Hamiltonian. Therefore all four remaining deletions are Hamiltonian:
S-{x_i} is Hamiltonian for i=0,1,2,3.
Thus the Hamiltonian deletions of S are exactly V(X).

It remains to show that S itself is non-Hamiltonian. Suppose instead that S has a Hamilton path. Since e and f are endpoints of the displayed paths P and Q, the endpoint truncations P-e and Q-f are inherited tight paths. Hence
S | (P-e) | (Q-f)
is a spanning three-cover of H with component orders
6, m-1, r-1.
Its quadratic potential is
36+(m-1)^2+(r-1)^2.
The original globally minimal cover has potential
16+m^2+r^2.
Their difference is
[16+m^2+r^2]-[36+(m-1)^2+(r-1)^2]
=2(m+r-11).
Because m,r>=6, this is positive. Thus the displayed three-cover would have strictly smaller Phi, contradicting global minimality. Therefore H[S] is non-Hamiltonian.

Now use the certified bad-six-set structure in extremal01. Since S is non-Hamiltonian and its Hamiltonian deletion set is V(X), the prescribed Hamiltonian-four-overlap theorem says that for every chosen x_i in X there exists x_j in X-{x_i} such that
S-{x_i,x_j}
is Hamiltonian.

Likewise, choose arbitrarily one Hamilton path on each of the four Hamiltonian five-sets S-{x_i}. The bad-six-set order-disagreement theorem in extremal01 says that some two of these paths order two common vertices differently. The path-intersection calculus therefore yields inside S a reversed common ordered edge, a tight triple reversing an ordered edge at an intersection, or a vertex-simple tight cycle.

The argument is independent of which endpoint e of P and which endpoint f of Q were chosen. Hence all four cross-endpoint pairs generate this same six-set pattern, always with V(X) as the complete Hamiltonian-deletion set. ∎