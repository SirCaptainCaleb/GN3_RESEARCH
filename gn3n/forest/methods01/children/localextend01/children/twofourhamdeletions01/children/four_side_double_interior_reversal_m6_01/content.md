# A locally minimal four-side beside a path of order at least six has two interior reversal labels

## Statement

Let H be a boundary tournament and let W|R|Q be a spanning three-cover with |W|=4. Suppose this cover minimizes quadratic potential within its connected pairwise-repartition component and R=(r_1,...,r_m) has order m>=6. Let E_R={r_1,r_m} and let M=(r_2,...,r_{m-1}). Then for at least two distinct vertices w in W, (W-{w}) union E_R is Hamiltonian, w is noninsertable into every position of M, and consequently some tight triple containing w reverses a displayed edge of M.

## Body

Apply twofourhamdeletions01 to the disjoint two-set E_R and four-set W. For at least two distinct w in W, the five-set F_w=(W-{w}) union E_R is Hamiltonian. Fix one. If M union {w} were Hamiltonian, then F_w and M union {w} would partition V(W) union V(R) into two Hamiltonian supports of orders 5 and m-1. Replacing W|R by these two paths is one legal pairwise repartition, with change 25+(m-1)^2-[16+m^2]=10-2m<0 because m>=6, contradicting local Phi-minimality. Hence M+w is non-Hamiltonian, so w is noninsertable into M. Apply acdec36ae3ca to obtain a tight triple containing w that reverses a displayed edge of M. The argument applies to at least two distinct w. No minimum-counterexample or ambient-order hypothesis is used.