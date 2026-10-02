# Minimum-degree local bound implies the 2/3 upper bound

## Statement

Assume the minimum-degree local ascending-neighbor bound 4e1c498f922a holds for a fixed ell. Then every P_ell^(3)-free linear 3-graph H satisfies |E(H)|<=(2ell/3)|V(H)|.

## Body

Suppose not, and choose a counterexample H with the fewest vertices. By the minimal-counterexample minimum-degree reduction, δ(H)>2ell/3, hence δ(H)>=floor(2ell/3)+1. Let T^↑ be the simple graph on V(H) whose edges are the pairs of last vertices of ascending nonspecial hyperedges. We claim T^↑ is 3-degenerate. Indeed, let J be any nonempty subgraph of T^↑ and choose v∈V(J) minimizing φ(v). Every neighbor u of v in J satisfies φ(u)>=φ(v). By 4e1c498f922a, at most three ascending hyperedges have last-vertex pair vu, so d_J(v)<=3. Thus T^↑ is 3-degenerate and therefore A=|E(T^↑)|<=3|V(H)|, where A is the number of ascending edges. The ascending-edge accounting inequality gives 3|E(H)|-A<=(2ell-3)|V(H)|. Hence 3|E(H)|<=2ell|V(H)|, contradicting the choice of H.