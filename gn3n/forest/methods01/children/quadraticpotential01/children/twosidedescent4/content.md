# Every two-side beside a path of order at least four has an immediate strict quadratic descent

## Statement

Let H be a boundary tournament and let C=E|P|Q be any spanning three-cover, where E is a tight path of order two and P=(p_1,...,p_M) is a tight path of order M>=4. Then one legal pairwise repartition of E|P produces another spanning three-cover with strictly smaller quadratic potential Phi. More precisely, for either displayed endpoint p of P, the three-set V(E) union {p} is Hamiltonian and the inherited path P-p is tight, so the component orders 2,M may be replaced by 3,M-1. The potential decreases by 2M-6.

## Body

Choose a displayed endpoint p of P. Every boundary tournament on three vertices is Hamiltonian: on its unique underlying triple, exactly one of the two reverse ordered triples is tight, and that ordered triple itself is a tight three-vertex path. Hence H[V(E) union {p}] has a Hamilton path. Since p is an endpoint of the displayed path P, deleting p leaves the inherited contiguous path P-p. Replacing E|P by these two paths is a legal pairwise repartition, leaving Q unchanged. The old quadratic contribution is 2^2+M^2 and the new contribution is 3^2+(M-1)^2, whose difference is 6-2M<0 for M>=4. Thus Phi strictly decreases by 2M-6.