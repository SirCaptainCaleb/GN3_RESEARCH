# Diagonal products as a possible amplifier of the P5 lower construction

## Statement

For linear 3-graphs H,K define the diagonal product H tensor K on V(H)xV(K) by taking, for every e in E(H), f in E(K), and every bijection sigma:e->f, the triple {(u,sigma(u)):u in e}. This product is linear and has |V|=|V(H)||V(K)| and |E|=6|E(H)||E(K)|. For the 11-vertex 15-edge P5-extremal component G0, its t-fold diagonal power has edge/vertex ratio (1/6)(90/11)^t. Determine the growth of its maximum linear-path length L_t. If (|E|/|V|)/(L_t+1)>1/3+epsilon for infinitely many t, this gives a genuine leading-coefficient lower-bound improvement.

## Body


Linearity is immediate from coordinate projections. Two distinct product triples arising from (e,f,sigma) and (e',f',tau) can share a product vertex only at a pair (u,x) with u in e intersect e' and x in f intersect f'. Since each factor is linear, there is at most one possible first-coordinate intersection and at most one possible second-coordinate intersection; distinct bijections for the same pair (e,f) have at most one fixed matched pair unless they are identical. Hence two distinct product triples intersect in at most one vertex.

The counting formulas are exact: there are |V(H)||V(K)| product vertices, and each ordered factor-edge pair contributes the six distinct bijections between its two 3-sets, so |E(H tensor K)|=6|E(H)||E(K)|.

For G0, n_1=11,m_1=15. Recursively n_t=11^t and m_t=6^{t-1}15^t, hence
 m_t/n_t=(1/6)(90/11)^t.
This is qualitatively different from Cartesian powering, whose density grows only linearly with the number of factors.

The missing obligation is entirely path-theoretic. Let L_t be the maximum linear-path length in G0^{tensor t}. The construction beats the asymptotic 1/3 benchmark precisely if along an infinite sequence
 (m_t/n_t)/(L_t+1)>1/3+epsilon
for some epsilon>0. Already at t=2 the product has 121 vertices and 1350 edges, so L_2<=32 would make it P_33-free and give coefficient (1350/121)/33=450/1331>1/3. Conversely L_2>=33 kills the first square as a >1/3 example at its first forbidden length.

No such path bound is asserted here. A useful next step is a structural analysis of product paths via their two factor projections; exact computation should only be attempted under the LINP computation policy and an appropriate research-mode permit.
