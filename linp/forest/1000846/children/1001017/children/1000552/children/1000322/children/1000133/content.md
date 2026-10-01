# Threshold-degree vertices cover every off-witness edge in an edge-minimal counterexample

## Statement

Fix ell>=4 and put k=floor(2ell/3)+1, the least integer strictly larger than 2ell/3. Suppose H is a P_ell-free linear 3-graph with minimum degree at least k and containing a nonspecial edge, chosen edge-minimal among such counterexamples (after any desired vertex-minimal choice). Then delta(H)=k. Moreover, for every nonspecial edge e and every phi(e)-edge witness path P ending in e, every edge f not belonging to P contains a vertex of degree exactly k. Equivalently, the set D={v:d_H(v)=k} is a vertex cover of E(H)\E(P) for every nonspecial witness path P.

## Body

Let e be nonspecial of rank q and let P be a q-edge longest path ending in e.

Take any edge f not in E(P). In H-f the path P remains, so the rank of e is still at least q. Edge deletion cannot create a longer path ending in e, hence its rank remains exactly q. Also edge deletion cannot create a new longest-path entrance label: every q-edge path ending in e in H-f was already such a path in H. Since e was nonspecial in H, all those paths enter e through the same unique entrance. Thus e remains nonspecial in H-f.

The hypergraph H-f is still P_ell-free. Therefore, by edge-minimality of H, H-f must fail the minimum-degree condition delta>=k. Only the three vertices of f lose degree, so at least one vertex of f had degree exactly k in H.

Hence every edge outside P meets
D={v:d_H(v)=k}.

It remains to show delta(H)=k. Suppose instead delta(H)>=k+1. Since H has minimum degree at least k+1 and ell>=4, H cannot consist solely of the edges of the linear path P: a path hypergraph has vertices of degree one and maximum degree two. Thus there exists an edge f not in E(P).

Deleting this f lowers the degrees of its three vertices by one, so H-f still has minimum degree at least k. As shown above, e remains nonspecial and H-f remains P_ell-free. This contradicts edge-minimality.

Therefore delta(H)=k, and the hitting assertion above applies to every nonspecial witness path.