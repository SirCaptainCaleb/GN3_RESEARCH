# Free vertex involution retains a logarithmic one-switch obstruction

- Stable ID: note_nori_xiii_free_vertex_involution_logarithmic_obstruction_20261013
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: counterexample, vertex-involution, parity-reversal
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_1
- Updated session: session_nori_r7442_1
- Disposition: none
- Successor: none

## Related references

- article:nori_article_xiii_binary_involutive_rainbow_paths

## Research note

Theorem (free vertex involution with logarithmic one-switch path bound). Let m>=4 and G=B_m Cartesian product B_m be the connected edge-colored graph of note_nori_xiii_transitive_product_and_short_circuit_classification_20261013. It has minimum color degree k=2m-2, vertex involution T(u,v)=(rho(v),rho(u)) with rho(a,b)=(b,a), and binary edge label b satisfying b(T e)=1-b(e). Every one-switch rainbow path in G has at most L=12 ceil(log_2 m)-6 edges.

Construct H from two copies G_0,G_1. For each x with Tx != x, add the intercopy edge {(x,0),(x,1)}, giving every such edge one fresh ordinary color star. Preserve the earlier colors on edges internal to copies. Define tau(x,s)=(Tx,1-s). This is an involutive vertex automorphism without fixed vertices. It maps each horizontal edge e in copy s to T(e) in copy 1-s, and maps the intercopy edge at x to the intercopy edge at Tx. No edge is setwise fixed: horizontal edges lie in distinct copies after applying tau, and intercopy edges only exist for Tx != x.

Keep the original binary labeling on both horizontal copies. Assign complementary binary labels to each pair of intercopy edges indexed by x and Tx. The resulting labeling obeys chi(tau{u,v})=1-chi({u,v}) for every edge {u,v}; tau acts on edges solely via its vertex action. Ordinary edge colors need not be invariant under tau.

Each horizontal copy is connected and at least one intercopy edge exists, so H is connected. Vertices x fixed by T retain color degree 2m-2; all other vertices have color degree 2m-1. Hence the minimum color degree is k=2m-2.

A rainbow path uses the new color star at most once. Deleting the corresponding edge, if present, splits it into at most two rainbow paths internal to copies of G. Each portion has at most one binary switch, so its length is at most L. Therefore L_1(H)<=2L+1=24 ceil(log_2 m)-11, and L_1(H)/k tends to zero.

Consequently free vertex action by the parity-reversing involutive graph automorphism cannot serve as a sufficient strengthening of Article XIII for a linear one-switch rainbow path guarantee. No assertion of vertex-transitivity or color-degree regularity is made for H.
