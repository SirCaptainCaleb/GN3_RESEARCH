# A locally minimal anchored four-window has two distinct interior reversal labels

## Statement

Let H be a minimum counterexample of order n>=15 and let W|P|Q be a spanning three-cover with |W|=4 that minimizes quadratic potential within its connected pairwise-repartition component. Let R be the larger of P,Q, so |R|=m>=6, and let E_R be the two displayed endpoints of R. Then there exist at least two distinct vertices w in W such that (W-{w}) union E_R is Hamiltonian and w is noninsertable into every position of the inherited interior path R-E_R. Consequently, for each of these two distinct labels w, there is a tight triple containing w that reverses a displayed interior edge of R.

## Body

Since |P|+|Q|=n-4>=11, the larger component R has order m>=6. Apply certified twofourhamdeletions01 to the two-set E_R and the four-set W. For at least two distinct w in W, the five-set F_w=(W-{w}) union E_R is Hamiltonian. Fix such w and let M be the inherited interior path obtained from R by deleting both displayed endpoints, so |M|=m-2. If M union {w} were Hamiltonian, then F_w and M+w would partition V(W) union V(R) into two Hamiltonian supports of orders 5 and m-1. Replacing W|R by these two paths is one legal pairwise repartition in the same component. Its potential change is 25+(m-1)^2-[16+m^2]=10-2m<0 because m>=6, contradicting local Phi-minimality. Therefore M+w is non-Hamiltonian. Any insertion of w into the inherited displayed order M would Hamiltonize M+w, so w is noninsertable throughout M. Since |M|>=4, certified acdec36ae3ca applies and gives a tight triple containing w that reverses one displayed edge of M, hence an interior displayed edge of R. The argument applies to at least two distinct w.
