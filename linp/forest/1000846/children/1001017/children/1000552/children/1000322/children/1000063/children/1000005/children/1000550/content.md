# Minimum-degree all-special transfer by peeling

## Statement

Fix ell>=2 and an integer k>=0. Suppose every P_ell^(3)-free linear 3-graph with minimum degree at least k+1 has all edges special. Then ex_L(n,P_ell^(3)) <= max{k,(2ell-3)/3} n. In particular, the dense-core all-special conjecture with k=floor(2ell/3) implies ex_L(n,P_ell^(3))<=floor(2ell/3)n.

## Body

Proof. Let H be P_ell-free. Repeatedly delete a vertex of degree at most k, charging the at most k incident edges deleted at that step. Let H' be the remaining core, with n' vertices and m' edges. The deleted portion contributes at most k(n-n') edges. If H' is empty we are done. Otherwise delta(H')>=k+1, so by hypothesis every edge of H' is special in its own snake digraph. Since H' is still P_ell-free, each vertex has snake indegree at most 2ell-3; summing gives 3m'<= (2ell-3)n'. Hence |E(H)|<=k(n-n')+((2ell-3)/3)n'<=max{k,(2ell-3)/3}n. Taking k=floor(2ell/3), which is at least (2ell-3)/3, gives the stated bound.