# Any four-side beside a path of order at least seven forces strict descent or order disagreement

## Statement

Let H be a boundary tournament and let C=X|P|Q be any spanning three-cover, where X=(x_0,x_1,x_2,x_3) is a tight path of order four and P=(p_1,...,p_m) is a tight path of order m>=7. Then either a legal pairwise repartition of X|P strictly decreases quadratic potential, or the six-set U=V(X) union {p_1,p_m} is non-Hamiltonian and Hamilton paths on its four deletions U-{x_i}, i=0,1,2,3, exhibit relative-order disagreement.

## Body

If X union {p_1} or X union {p_m} is Hamiltonian, moving that endpoint from P into X replaces component orders (4,m) by (5,m-1), with quadratic-potential change 10-2m<0, giving strict descent. Assume both endpoint five-sets are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to the four-set V(X) and exterior labels p_1,p_m. It gives that U-{x_i} is Hamiltonian for every i=0,1,2,3. If U is non-Hamiltonian, apply astra004fourgooddisagree to these four Hamiltonian deletions; arbitrary chosen Hamilton paths on them contain a pair with order disagreement. If U is Hamiltonian, replace X|P by U|(p_2,...,p_{m-1}); the component orders change from (4,m) to (6,m-2), and the quadratic-potential change is 36+(m-2)^2-(16+m^2)=24-4m<0 because m>=7. Thus strict descent or the stated order disagreement occurs. No minimum-counterexample hypothesis is used.