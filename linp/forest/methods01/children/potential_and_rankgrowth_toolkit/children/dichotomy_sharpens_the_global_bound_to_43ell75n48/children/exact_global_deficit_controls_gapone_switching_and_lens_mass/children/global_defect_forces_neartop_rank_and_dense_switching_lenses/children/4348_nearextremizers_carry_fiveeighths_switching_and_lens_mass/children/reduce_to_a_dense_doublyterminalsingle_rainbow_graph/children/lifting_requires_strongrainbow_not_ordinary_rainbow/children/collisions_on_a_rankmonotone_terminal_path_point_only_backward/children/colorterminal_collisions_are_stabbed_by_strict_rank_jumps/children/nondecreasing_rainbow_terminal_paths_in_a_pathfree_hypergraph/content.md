# Rank spread bounds nondecreasing rainbow terminal paths in a path-free hypergraph

## Statement

Let H be a P_ell^(3)-free linear 3-graph. Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial parent edges E_i={x_i,v_{i-1},v_i} with nondecreasing edge ranks r_1<=...<=r_k. If D=r_k-r_1, then
k <= (D+1)(ell-1).
Equivalently, any such rainbow terminal path with k>(D+1)(ell-1) forces an ell-edge linear path in H.

## Body

By 31cb29f347a8, every maximal contiguous constant-rank block is strong-rainbow. By the strong-rainbow lifting criterion 8924e63f61db, a block of ell parent edges would lift, in the displayed order, to an ell-edge linear path in H. Since H is P_ell^(3)-free, each constant-rank block therefore has at most ell-1 edges.

Because the ranks are nondecreasing integers and r_k-r_1=D, there are at most D+1 nonempty constant-rank blocks. Summing their lengths gives
k <= (D+1)(ell-1).