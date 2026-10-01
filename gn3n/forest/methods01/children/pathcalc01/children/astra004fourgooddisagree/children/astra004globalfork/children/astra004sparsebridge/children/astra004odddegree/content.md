# Sharp-shell good-deletion degree dictionary and low-degree expansion

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let G be the graph whose vertices are Hamiltonian lambda-subsets, with two supports adjacent when disjoint. For a Hamiltonian lambda-set S, put R=V(H)-S and D(R)={r in R:H[R-r] is Hamiltonian}. Then the map r -> R-r is a bijection from D(R) onto N_G(S), and the edge S--(R-r) has omitted label r. Hence |D(R)|=deg_G(S). Every ambient vertex labels at least one edge of G, so |E(G)|>=|V(H)|. Consequently, if every nonisolated Hamiltonian lambda-support has degree at most three (equivalently every deficient complement has at most three Hamiltonian vertex deletions), then G has at least ceil(2|V(H)|/3) nonisolated vertices. More generally, if all nonisolated degrees are at most d, then G has at least ceil(2|V(H)|/d) nonisolated vertices.

## Body

# Proof

Fix a Hamiltonian lambda-set S and put R=V(H)-S, so |R|=lambda+1. For r in R, the set R-r has order lambda and is disjoint from S. Thus R-r is Hamiltonian exactly when it is a vertex of G adjacent to S. This gives the bijection r -> R-r between D(R) and N_G(S). Since S union (R-r)=V(H)-{r}, the unique omitted vertex on that odd edge is r.

The sharp-shell odd-graph theorem bcfa72bc175f proves that every ambient vertex x occurs as the omitted label of at least one edge of G. Distinct edge labels require distinct edges, so |E(G)|>=|V(H)|=n.

If every nonisolated vertex of G has degree at most d, then
2|E(G)|=sum_{S in V(G)} deg_G(S) <= d |V_+(G)|,
where V_+(G) is the set of nonisolated vertices. Therefore |V_+(G)|>=2|E(G)|/d>=2n/d, and integrality gives the ceiling. Taking d=3 yields at least ceil(2n/3) nonisolated globally-longest supports. ∎