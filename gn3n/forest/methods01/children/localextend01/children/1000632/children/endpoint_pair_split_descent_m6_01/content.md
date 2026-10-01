# A rigid endpoint-pair 2+2 split beside a path of order at least six gives strict quadratic descent

## Statement

Let H be a boundary tournament and let W|P|Q be a spanning three-cover with |W|=4. Let E_P,E_Q be the displayed endpoint pairs and define A_R={w in W:(W-{w}) union E_R is Hamiltonian}. Suppose A_P and A_Q are disjoint two-subsets of W. If one of P,Q has order m>=6, then W|P|Q admits one legal pairwise repartition with strictly smaller quadratic potential.

## Body

By c0ec8ff0e968, W union {e} is Hamiltonian for every displayed endpoint e of P and Q. Let R be a component of order m>=6 and choose either displayed endpoint e of R. Replace W|R by a Hamilton path on W union {e} and the inherited path R-e. This is a legal pairwise repartition with pair-size change (4,m)->(5,m-1), so its Phi change is 25+(m-1)^2-[16+m^2]=10-2m<0. No minimum-counterexample or total-order hypothesis is used.