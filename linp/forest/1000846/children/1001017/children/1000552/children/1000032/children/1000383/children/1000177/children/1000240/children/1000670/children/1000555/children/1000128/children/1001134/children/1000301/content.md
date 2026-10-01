# A repeated endpoint-on-path intersection gives a linear cycle or a shared last edge

## Statement

Let A and P be linear paths in a linear hypergraph, and let u be the last vertex of P. Assume u belongs to V(A), and P and A have at least one common vertex besides u.

Then at least one of the following holds:

(1) the last edge of P is also an edge of A;

(2) A union P contains a linear cycle.

More precisely, let z be the last common vertex encountered before u when P is oriented toward its last vertex u. If the last edge of P is not an edge of A, then the P-segment from z to u and the A-segment between z and u are internally vertex-disjoint and edge-disjoint, and their union is a linear cycle.

## Body

Choose z as stated. By definition, the open P-segment P(z,u) contains no vertex of A.

Let A[z,u] be the unique A-segment between z and u. If a vertex w belonged to the interiors of both P[z,u] and A[z,u], then w would be a common vertex of P and A occurring on P strictly after z and before u, contradicting the choice of z. Hence the two segments have disjoint interiors and meet only at z and u.

Suppose the two segments shared a hyperedge h. Every vertex of h belongs to both paths. Because the segment interiors are disjoint, h cannot contain a vertex lying strictly inside either segment. Therefore both segment endpoints z,u lie in h and each segment consists only of h near both endpoints. In particular h is the last edge of P and is an edge of A.

Thus, if the last edge of P is not an edge of A, the two segments are edge-disjoint as well as internally vertex-disjoint. Their union consists of two distinct linear paths with common last vertices z,u and no other intersections. By linearity, they cannot both have one edge, since two distinct hyperedges would then contain both z and u. Hence their total number of edges is at least three, and the union is a linear cycle.