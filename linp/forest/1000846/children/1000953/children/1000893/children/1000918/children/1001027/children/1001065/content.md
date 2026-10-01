# Fourfold Boolean lift preserves even spanning additive paths

## Statement

Let B be a finite nonzero subset of an elementary abelian 2-group with |B|=2r+1 and r even. If H(B) contains a spanning P_r, then A=((B union {0}) x F_2^2)\{0} contains a spanning P_{4r+3}. The parity r even is essential to this four-copy construction: the corresponding ordinary path has two leaves in the same bipartition class, exactly the hypothesis in the corrected four-copy set-sequential lemma of Eckels--Gyori--Liu--Nasir (2024).

## Body

Encode the spanning P_r in H(B) as an ordinary path G on r+1 vertices: its ordinary vertex labels and edge labels are exactly the elements of B, each once, and each edge label is the sum of its endpoint labels. Since r is even, G has an odd number r+1 of vertices, so its two leaves u,v lie in the same bipartition class.

Take four copies G_1,...,G_4. Join the corresponding leaves by the three edges
  v_1 v_2,  u_2 u_3,  v_3 v_4.
Because u and v are the two endpoints of a path, the resulting graph is itself a path, traversing G_1, then G_2 in reverse, then G_3, then G_4 in reverse. It has 4(r+1) vertices and 4r+3 edges.

Lemma 3.1 of Eckels--Gyori--Liu--Nasir, "Set-sequential labelings of odd trees", Discuss. Math. Graph Theory 44 (2024), 151--170, gives precisely the four-copy labeling operation for a set-sequential bipartite graph whose chosen two leaves lie in the same color class. Their proof appends two binary coordinates to the four copies, uses the four suffixes 00,01,10,11, and performs a leaf/pendant-edge label swap to make the three connector labels distinct.

The proof transports verbatim from a complete set-sequential label set to our partial additive domain B: it uses only (i) distinctness of the original labels, (ii) the local relation edge-label = sum of endpoint labels, (iii) the two new binary coordinates, and (iv) swapping the labels of a leaf and its pendant edge, which preserves the local sum relation. Thus after extension the labels used on the four copies are exactly
  {(b,alpha): b in B, alpha in F_2^2},
and the three connector labels are the three nonzero vectors
  (0,01),(0,10),(0,11).
Together these are exactly
  A=((B union {0}) x F_2^2)\{0}.

Hence the resulting ordinary path is a set-sequential labeling on A. Translating each ordinary edge with endpoint labels x,y and edge label x+y back to the additive triple {x,y,x+y} gives a spanning linear P_{4r+3} in H(A).

The parity condition cannot be reversed in general. For r=1, B=F_2^2\{0} has a spanning P_1, but its two-bit lift is PG(3,2), which is P_7-free by d593f8024a92.
