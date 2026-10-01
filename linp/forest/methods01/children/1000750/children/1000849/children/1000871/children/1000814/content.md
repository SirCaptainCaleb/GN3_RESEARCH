# The diagonal square of G0 already contains P33

## Statement

Let G0 be the 11-vertex 15-edge P5-extremal linear triple system represented by a 1-factorization of K6 with five centers. Then the diagonal product G0 tensor G0 contains a 33-edge linear path. Consequently its first forbidden path length is at least 34, and since it has 121 vertices and 1350 edges, its normalized density at its first forbidden length is at most 1350/(121*34)=675/2057<1/3. Thus the diagonal square does not improve the asymptotic 1/3 benchmark.

## Body

Let the six base vertices be 0,...,5 and let centers A,B,C,D,E correspond to the one-factors
 A: 01,25,34;
 B: 02,13,45;
 C: 03,15,24;
 D: 04,12,35;
 E: 05,14,23.
For a center i and base vertex u, write m_i(u) for the mate of u in the corresponding one-factor.

Inside G0 tensor G0 take only the crossed product triples. Put
 X={(i,x): i is a center, x is a base vertex},
 Y={(u,j): u is a base vertex, j is a center},
 Z={(v,y): v,y are base vertices}.
For every (i,x) in X and (u,j) in Y there is the crossed product triple
 {(i,x),(u,j),(m_i(u),m_j(x))}.
Thus these triples are the lift of K_{30,30} with bipartition X,Y, properly edge-colored by the 36 vertices of Z, where
 color((i,x),(u,j))=(m_i(u),m_j(x)).
A rainbow graph path therefore lifts to a linear hypergraph path.

The following 34 alternating X,Y vertices form a 33-edge rainbow path:
 X(0,0),
 Y(0,0),
 X(0,1),
 Y(0,1),
 X(0,4),
 Y(0,2),
 X(0,2),
 Y(1,0),
 X(0,3),
 Y(1,1),
 X(1,0),
 Y(0,3),
 X(1,1),
 Y(1,2),
 X(1,2),
 Y(0,4),
 X(1,4),
 Y(1,3),
 X(0,5),
 Y(1,4),
 X(2,0),
 Y(2,0),
 X(1,5),
 Y(4,0),
 X(1,3),
 Y(4,1),
 X(2,2),
 Y(2,1),
 X(2,1),
 Y(2,2),
 X(4,0),
 Y(3,4),
 X(3,2),
 Y(3,1).

Using center indices 0=A,1=B,2=C,3=D,4=E, the 33 successive colors are
 (1,1),(1,0),(1,3),(1,5),(1,2),(1,4),
 (0,5),(0,4),(0,1),
 (3,2),(2,4),(2,2),(3,5),(3,4),(2,3),(2,1),(3,0),(0,3),(0,0),
 (5,5),(4,1),(0,2),(5,2),(5,4),(5,1),(2,0),(4,0),(4,3),(4,5),(3,3),(2,5),(5,3),(5,0).
They are pairwise distinct. The 34 displayed X,Y vertices are also pairwise distinct. Hence the lifted triples meet consecutively in exactly the displayed X/Y vertex, while nonconsecutive triples have distinct X-endpoints, Y-endpoints, and colors, so are disjoint. This proves the claimed P33.
