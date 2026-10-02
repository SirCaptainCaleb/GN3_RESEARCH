# Static transversals and fixed-multiplicity shared-color lifts cannot beat one third

## Statement


Three related lower-construction fences hold.

(1) If a linear 3-graph H on n vertices has a vertex cover C of size t, then |E(H)|<=t(n-1)/2 and every linear path has at most 2t edges. Thus a path cap certified solely by a fixed t-vertex global transversal has normalized density below 1/4 at ell=2t+1.

(2) This one-quarter ceiling is asymptotically attained by repeated one-factorization lifts: if a graph G has a proper d-edge-coloring in which every two colors occur on incident edges, and H_t is formed from t disjoint copies of G by adjoining one shared vertex for each color and lifting xy of color c to {x,y,c}, then for t>=d the lift contains a 2d-1 edge linear path. In particular repeated lifts of one-factorized K_{2^r} have asymptotic normalized coefficient at most 1/4.

(3) More flexible fixed-multiplicity sharing still cannot beat the one-third benchmark. For fixed r>=3 and even N, let d=N-1 and take r disjoint copies of K_N, each arbitrarily one-factorized by the same d color labels; adjoining one common vertex for each color and lifting the graph edges gives H_{r,N}. Then H_{r,N} contains a linear path of length at least (3r/(2(r+1))-o(1))d. Since |E|/|V|=(r/(2(r+1))+o(1))d, its normalized density at its first forbidden path length is at most 1/3+o(1).


## Body


For the static-transversal bound, fix c in a vertex cover C of size t. By linearity, the edges through c have pairwise disjoint sets of other vertices, so d_H(c)<=floor((n-1)/2). Since C meets every edge,
  |E(H)|<=sum_{c in C}d_H(c)<=t(n-1)/2.
A fixed c can lie in at most two edges of a linear path, because three occurrences would put c in two nonconsecutive path edges. Charging each path edge to a cover vertex gives path length at most 2t. Hence with ell=2t+1 the normalized ratio is strictly below 1/4. This fences only static global pinning; state-dependent or hierarchical pinning remains a different route.

The repeated one-factorization lift shows that this ceiling reflects actual path behavior. Order the d colors c_1,...,c_d. In distinct graph copies, choose two-edge wedges joining consecutive prescribed colors. Listing the lifted edges gives color sequence
  c_1,c_1,c_2,c_2,...,c_{d-1},c_{d-1},c_d,
hence a 2d-1 edge linear path: within a copy consecutive triples meet at the selected graph vertex, while between copies the two consecutive triples of the repeated color meet at the common color vertex. All other intersections are excluded by copy-disjointness and proper coloring. For a d-regular graph G on v vertices, H_t has tv+d vertices and tdv/2 edges, so for large t its density tends to d/2 while ell>=2d; the normalized coefficient is therefore at most 1/4. For one-factorized K_{2^r}, the shared d color vertices are exactly the small global cover.

Now fix r>=3 and consider H_{r,N} from r one-factorized K_N layers sharing the same d=N-1 color vertices. Reserve one layer G_r for a rainbow tail. Put
  alpha=(r-2)/(2(r+1))+epsilon
with alpha<(r-1)/9, and let k=floor(alpha d). Choose k colors B. Delete their one-factors from G_r. The remaining (d-k)-regular properly colored graph has a rainbow path Q of length d-k-o(d) by the asymptotic rainbow-path theorem used in the source argument.

In the other r-1 layers, order B and append the first color c_* of Q. For each consecutive color pair choose a two-edge wedge, scheduling consecutive wedges in different layers and distributing them so that no layer receives more than k/(r-1)+O(1) wedges. Wedges in a fixed layer can be chosen vertex-disjoint: after j previous wedges there are 3j used graph vertices, and for prescribed colors a,b each used vertex forbids at most three possible centers v through v, M_a(v), or M_b(v). Thus fewer than 9j centers are bad, which is below N by the choice alpha<(r-1)/9.

The 2k lifted wedge edges form a linear path prefix whose only repeated colors are the intended consecutive bridge colors. It concatenates with the rainbow tail Q in G_r at c_*; all other tail colors avoid B and all graph vertices lie in the reserved layer. The resulting path has
  2k+(d-k-o(d))=d+k-o(d)
    =(1+alpha-o(1))d.
Letting epsilon tend to zero gives length at least
  (3r/(2(r+1))-o(1))d.
Finally
  |V(H_{r,N})|=rN+d=(r+1)d+r,
  |E(H_{r,N})|=rNd/2,
so its density is (r/(2(r+1))+o(1))d and division by the first forbidden path length gives at most 1/3+o(1).

Thus a single global transversal is capped at one quarter, the repeated-copy lift realizes that obstruction, and even fixed multiplicity r of shared one-factorization layers cannot cross the one-third asymptotic benchmark.
