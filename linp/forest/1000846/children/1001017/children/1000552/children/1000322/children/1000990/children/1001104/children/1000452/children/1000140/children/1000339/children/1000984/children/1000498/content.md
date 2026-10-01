# Any set of pair-universal vertices generates a dense strong-rainbow matching graph

## Statement

Let Z be pair-universal vertices in a linear triple system. For every A subseteq Z of size a<=(n-1)/2, the hyperedges with one vertex in A and two in B=V\A define a properly edge-colored graph G_A on B, colored by A, with |E(G_A)|>=a(n-2a+1)/2. Every rainbow path in G_A lifts to a linear hypergraph path because the color set A is disjoint from the graph vertex set.

## Body

Let H be an n-vertex linear triple system and let Z be a set of pair-universal vertices: for every z∈Z and every x!=z, the pair {z,x} lies in a unique hyperedge.

Fix any subset A⊆Z of size a with 1<=a<=(n-1)/2, and put
  B=V(H)\A.

Define a graph G_A on B as follows. For each z∈A and each hyperedge
  {z,x,y}
with x,y∈B, add the graph edge xy and color it by z.

This is a simple properly edge-colored graph. For a fixed color z, the edges through z form a perfect matching on V(H)\{z}, hence the retained z-colored graph edges form a matching. If two different colors z,z' produced the same graph edge xy, the hyperedges {z,x,y} and {z',x,y} would share the pair {x,y}, violating linearity.

For a fixed z∈A, its perfect star matching has (n-1)/2 pairs. Removing the a-1 vertices A\{z} can destroy at most a-1 matching edges. Therefore color z retains at least
  (n-1)/2-(a-1)
  =(n-2a+1)/2
edges on B.

Summing over colors,
  |E(G_A)| >= a(n-2a+1)/2.                         (1)

Now let
  x_0x_1...x_t
be a rainbow path in G_A, with edge colors z_1,...,z_t∈A. The corresponding hyperedges
  {z_i,x_{i-1},x_i}
form a t-edge linear hypergraph path: consecutive hyperedges meet in x_i; nonconsecutive graph edges have disjoint graph vertices; the colors are distinct; and every color lies in A while all path vertices lie in B, so a color cannot create an extra nonconsecutive intersection.

Hence every rainbow P_t in G_A lifts to P_t^(3) in H.

This construction applies simultaneously for every A⊆Z. It is the general many-center version of the alternating perfect-matching structures seen in the finite order-11/order-12 critical cases.
