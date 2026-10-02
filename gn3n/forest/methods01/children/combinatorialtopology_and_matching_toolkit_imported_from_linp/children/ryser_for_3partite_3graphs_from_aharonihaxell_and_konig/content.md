# Ryser for 3-partite 3-graphs from Aharoni--Haxell and Konig

## Statement

Every 3-partite 3-uniform hypergraph H satisfies tau(H)<=2 nu(H). A short derivation follows from the Aharoni--Haxell deficiency theorem applied to bipartite link graphs, together with Konig's theorem.

## Body


Let the vertex classes of H be A,B,C; write a=|A| and t=tau(H). For each x in A let H_x be the bipartite graph on B union C whose edges yz are exactly those with xyz in E(H).

For S subset A put G_S=union_{x in S}H_x. By Konig, G_S has a vertex cover of size nu(G_S). Then
  (AS) union (a minimum vertex cover of G_S)
is a vertex cover of H. Therefore
  t <= a-|S|+nu(G_S),
so
  nu(G_S) >= t-a+|S|.                                      (1)

For an ordinary graph G, its matching width satisfies
  mw(G) >= ceil(nu(G)/2).
Indeed, let M be a maximum matching. A single graph edge can meet at most two edges of M, one through each endpoint. Consequently any edge set pinning M has at least ceil(|M|/2) edges.

Combining this with (1),
  mw(G_S) >= ceil((t-a+|S|)/2)
           >= |S|-a+ceil(t/2).
The last inequality uses |S|<=a.

Set d=a-ceil(t/2). Thus every S subset A satisfies
  mw(G_S) >= |S|-d.
By the deficiency form of Aharoni--Haxell, the family (H_x)_{x in A} has a partial system of disjoint representatives of size at least
  a-d = ceil(t/2).
Choosing an edge yz from H_x means choosing the triple xyz in H. Distinct representatives use distinct x in A and pairwise disjoint yz in B union C, hence these triples form a matching of H. Therefore
  nu(H) >= ceil(t/2),
which is equivalent to tau(H)<=2nu(H).

This proof is worth retaining as a reusable template: convert a transversal parameter into lower bounds on matching numbers of bipartite links, turn those into matching-width bounds by the factor-two pinning estimate, and invoke hypergraph Hall to select disjoint representatives.
 