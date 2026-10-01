# Rainbow connector paths through contracted forest triples double their length

## Statement

In the zero-slack critical-core model 13500728c22f, let F_1,...,F_c be the disjoint forest triples, c=2k/3, and let G be the k-regular properly k-edge-colored graph on X whose colored edge uv of color d represents the hyperedge {d,u,v}. Suppose there are distinct triple-indices i_1,...,i_s and G-edges C_j=u_jv_j, j=1,...,s-1, such that C_j joins F_{i_j} to F_{i_{j+1}}, the colors of the C_j are distinct, and for each internal triple F_{i_j} the two incident connector endpoints in that triple are distinct. Then
F_{i_1}, C_1^H, F_{i_2}, C_2^H,...,C_{s-1}^H,F_{i_s}
is a linear hypergraph path of length 2s-1, where C_j^H is the corresponding DXX hyperedge.

## Body

Each forest triple F_i is a hyperedge wholly in X, and the F_i are pairwise disjoint.

Each connector C_j^H={d_j,u_j,v_j} has one endpoint u_j in F_{i_j}, one endpoint v_j in F_{i_{j+1}}, and color vertex d_j in D. Because G has no edges inside a forest triple in the zero-slack model, these are distinct triples.

Consecutive hyperedges in the displayed alternating sequence intersect exactly once:
- F_{i_j} meets C_j^H in the chosen connector endpoint;
- C_j^H meets F_{i_{j+1}} in the other endpoint;
- at an internal forest triple, the preceding and following connectors meet that triple at distinct vertices by hypothesis, but they are nonconsecutive to one another because F_{i_j} lies between them.

Nonconsecutive forest triples are disjoint. A connector C_j^H cannot meet a nonincident forest triple because its X-endpoints lie in its two designated endpoint triples. Distinct connectors have distinct D-color vertices by the rainbow-color hypothesis. Their X-endpoints are also distinct unless they are consecutive connectors at a common internal triple; there they are explicitly required distinct. Since the triple-indices form a simple path, nonconsecutive connectors have disjoint endpoint triples and hence disjoint X-endpoints.

Thus every nonconsecutive pair of hyperedges in the alternating sequence is disjoint, while every consecutive pair meets once. This is a linear path with s forest edges and s-1 connector edges, hence length 2s-1.