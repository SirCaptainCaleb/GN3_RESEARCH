# The intersection of two rooted graphs contains adjacent edges or is a perfect matching

## Statement

In the setting of 0c8144b5ac80, assume no order disagreement occurs. Fix the two endpoints e,f, let G_e and G_f be the two rooted graphs on V(X) defined there, and put G=G_e intersect G_f. Then every edge {a,b} of G gives a Hamiltonian six-set S_{ab}=(V(X)-{a,b}) union {e,f}, and e(G)>=3. Consequently exactly one of the following holds: (1) G contains two edges sharing a vertex, and the corresponding Hamiltonian six-sets differ in exactly one vertex; (2) G consists of exactly three pairwise disjoint edges and therefore is a perfect matching of V(X).

## Body


By 0c8144b5ac80, absent order disagreement every edge of the intersection graph G=G_e intersect G_f yields a Hamiltonian six-set S_{ab}, and e(G)>=3.

If two edges {a,b} and {a,c} share a vertex a, then
S_{ab}=(X-{a,b}) union {e,f},
S_{ac}=(X-{a,c}) union {e,f}.
Their intersection is (X-{a,b,c}) union {e,f}, of order five, so the two six-supports differ by exchanging b and c. This is outcome (1).

Otherwise G has maximum degree at most one, so G is a matching on the six vertices of X. A matching on six vertices has at most three edges. Since e(G)>=3, G has exactly three edges and they cover all six vertices; hence G is a perfect matching. This is outcome (2).
