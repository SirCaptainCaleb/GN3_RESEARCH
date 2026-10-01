# One vertex of a global four-vertex component controls at least three endpoint complement comparisons

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers, with |X|=4 and |P|=m, |Q|=r at least six. Let E be the four displayed endpoints of P and Q. Then there is a vertex x in V(X) and a set E_x subset E with |E_x|>=3 such that, for D=V(X)-{x}, the four-set D union {e} is Hamiltonian for every e in E_x.\n\nFix e in E_x. If e is an endpoint of P, put A_e=(V(P)-{e}) union {x} and B_e=V(Q); if e is an endpoint of Q, define A_e symmetrically on Q and let B_e be the untouched other path support. Then A_e is non-Hamiltonian. Nevertheless the complement H-(D union {e}) has a two-cover U|V. Every such cover has imbalance at least |m-r|. Consequently, after assuming m>=r, either its smaller component has order at most r-1, or its component-order multiset is exactly {m,r}. In the latter case its unordered support partition differs from {A_e,B_e}; hence at least one component of U|V meets both A_e and B_e and contains an ordinary path edge crossing the cut A_e|B_e.\n\nThus one vertex x supplies at least three endpoint comparisons, including both endpoints of one of P,Q. For each comparison, either every chosen complement two-cover has a strictly smaller smaller-component order than r, or a same-Phi complement two-cover has the original component-order multiset but crosses the natural partition A_e|B_e.

## Body

For an endpoint e of P, the five-set V(X) union {e} is non-Hamiltonian. Otherwise a Hamilton path on V(X) union {e}, together with the inherited endpoint truncation P-e and the unchanged path Q, would give a spanning three-cover with component orders 5,m-1,r. Its quadratic potential is smaller than that of X|P|Q by
16+m^2+r^2-[25+(m-1)^2+r^2]=2m-10>0,
contradicting global minimality. The same argument applies to either endpoint of Q.

Now fix any endpoint e in the four-element set E. The five-set V(X) union {e} is non-Hamiltonian, while deleting e leaves the Hamiltonian four-set V(X). By the certified five-vertex small-set structure in smallset01, a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion. Hence for at least three vertices x in V(X),
(V(X)-{x}) union {e}
is Hamiltonian.

Count the incidences (x,e) for which this four-set is Hamiltonian. Each of the four endpoint columns has at least three such incidences, so there are at least twelve incidences among four possible x. Therefore some x is incident with at least three endpoints. Fix such an x, put D=V(X)-{x}, and let E_x be its endpoint set. Since E consists of two endpoints of P and two of Q, any three-element subset contains both endpoints of at least one long path.

Now fix e in E_x; suppose first e is an endpoint of P. Put
F_e=D union {e},
A_e=(V(P)-{e}) union {x},
B_e=V(Q).
The four-set F_e is Hamiltonian by construction. The certified theorem aab7e8e9fe4a proves, in particular, that the endpoint-truncated enlargement A_e is non-Hamiltonian.

Because H is a minimum counterexample and F_e is a proper Hamiltonian set, K_e=H-F_e has path-cover number at most two. It is non-Hamiltonian: otherwise a Hamilton path on K_e together with one on F_e would give a spanning two-cover of H. Hence pc(K_e)=2. Let U|V be any two-cover of K_e, with component orders u,v. Then
F_e|U|V
is a spanning three-cover of H. Global Phi-minimality gives
16+m^2+r^2 <= 16+u^2+v^2,
so
u^2+v^2 >= m^2+r^2.
Also
u+v=m+r.
For two nonnegative integers of fixed sum, the sum of squares is monotone in absolute imbalance. Therefore
|u-v| >= |m-r|.

Assume m>=r. It follows that the smaller component of U|V has order at most r. If it has order at most r-1, we obtain a strict decrease in the smaller component order.

Otherwise the smaller component has order r. Since u+v=m+r, the other component has order m; equivalently the size multiset is exactly {m,r}. In this equality case F_e|U|V is another global Phi-minimum with the same component-order multiset as X|P|Q.

However its complementary support partition cannot be the natural partition {A_e,B_e}. The support B_e is Hamiltonian but A_e is non-Hamiltonian, so A_e|B_e is not a two-cover. Therefore {V(U),V(V)} differs from {A_e,B_e}. Since U|V partitions A_e union B_e, at least one of U,V contains vertices from both A_e and B_e. Any tight path containing vertices from both sides contains at least one ordinary path edge crossing the cut A_e|B_e.

The argument is symmetric when e is an endpoint of Q.

Hence the same vertex x gives at least three endpoint comparisons with the stated alternatives. ∎