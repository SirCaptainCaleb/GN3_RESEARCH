# One-factorization lifts are asymptotically inefficient for path lower bounds

## Statement

Let N be even and let phi be a 1-factorization of K_N. Form the linear 3-graph H_phi on V(K_N) union the N-1 colors by replacing each graph edge xy of color c with the triple {x,y,c}. Then |V(H_phi)|=2N-1 and |E(H_phi)|=N(N-1)/2. For all sufficiently large N, H_phi contains a linear path of length N-2. Consequently, if ell(H_phi) is one plus its maximum linear-path length, then |E(H_phi)|/(|V(H_phi)| ell(H_phi)) <= N/[2(2N-1)] = 1/4+o(1). Thus this natural generalization of the P5 extremal G0 cannot improve the asymptotic 1/3 lower coefficient.

## Body

Properness of phi implies H_phi is linear: two lifted triples sharing two vertices would correspond either to two graph edges with the same endpoint and same color, impossible in a proper coloring, or to the same graph edge.

Any rainbow r-edge graph path x_0x_1...x_r in K_N lifts to the hyperedge sequence {x_{i-1},x_i,phi(x_{i-1}x_i)}. Consecutive lifted edges meet in x_i. Nonconsecutive graph-path edges are vertex-disjoint, and rainbow colors are distinct, so nonconsecutive lifted edges are disjoint. Hence the lift is a linear r-edge hypergraph path.

Bowtell, Montgomery, Müyesser and Pokrovskiy (arXiv:2608.06369, 2026) prove that for sufficiently large N every properly edge-colored K_N has a rainbow path on N-1 vertices, hence N-2 edges. Therefore the maximum linear-path length L(H_phi)>=N-2. If H_phi is used as a P_ell-free component at its first possible forbidden length ell=L(H_phi)+1, then ell>=N-1. Since its density is N(N-1)/(2(2N-1)), division by ell gives at most N/[2(2N-1)], tending to 1/4.

For N=6 this construction is exactly Tang-Wu-Zhang's 11-vertex, 15-edge P5-extremal graph G0: the five v_i label the five 1-factors of K_6 on u_1,...,u_6. Thus G0 is a genuine small-order exception and not an asymptotically scalable mechanism.
