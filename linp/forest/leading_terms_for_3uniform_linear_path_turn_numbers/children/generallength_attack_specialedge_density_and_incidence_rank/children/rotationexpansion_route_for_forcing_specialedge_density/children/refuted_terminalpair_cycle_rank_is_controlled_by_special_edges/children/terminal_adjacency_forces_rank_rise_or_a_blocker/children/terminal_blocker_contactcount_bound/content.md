# Terminal blocker contact-count bound

## Statement

Let e,f be distinct nonspecial edges of a linear 3-graph sharing a vertex v that is terminal for both. Put p=φ(e), q=φ(f), assume q<=p, and let P be a p-edge path ending in e with last vertex v. If r is the number of distinct vertices of f that occur on P, then 2<=r<=3 and p<=r(q-1). In particular, if p>=2q-1 then all three vertices of f occur on P.

## Body

The edge f is not an edge of P, because it contains the last vertex v and v occurs only in the last edge of P. If f met V(P) only at v, then appending f to P would give a (p+1)-edge path ending in f, contradicting q<=p. Hence f has r=2 or 3 distinct contact vertices on P.

For each contact vertex z of f, the path edges containing z form a block of one or two consecutive edges; nonconsecutive path edges are disjoint. Order the r nonempty contact blocks along P as [a_j,b_j], j=1,...,r, where a_j,b_j are edge indices, b_j-a_j<=1, and the final block is [p,p] because the last contact is the physical terminal v. Put b_0=0. For each j, the segment P_{b_{j-1}+1},...,P_{a_j}, followed by f, is a linear path ending in f and entering f through z_j. Therefore a_j-b_{j-1}<=q-1 if z_j is the unique entrance of f, and <=q-2 if z_j is one of its two terminal vertices. At most one contact is the entrance, while the final contact v is terminal. Thus the sum of these r gaps is at most (q-1)+(r-1)(q-2). The r-1 earlier contact blocks contribute at most one additional path edge each. Consequently p<= (q-1)+(r-1)(q-2)+(r-1)=r(q-1). If p>=2q-1, r=2 is impossible, so r=3 and every vertex of f occurs on P.