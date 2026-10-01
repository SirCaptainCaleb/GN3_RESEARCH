# Pathmaker lemma: linear paths are induced paths in the intersection graph

## Statement

Let G be a linear r-uniform hypergraph and L(G) its intersection graph on E(G). A sequence e_1,...,e_t is the edge sequence of a copy of P_t^(r) in G if and only if e_1...e_t is an induced path in L(G).

## Body

Ported from linear_paths.tex. The forward direction is immediate. Conversely, induct on t. Let v=e_t∩e_{t-1}. By induction e_1,...,e_{t-1} is realized as a linear path P. If t-1>=2, inducedness gives v∉e_{t-2}, so v is among the final r-1 vertices of P and these may be reordered so v is last. The set e_t\{v} is disjoint from V(P): an intersection inside e_{t-1} would violate linearity, and an intersection with an earlier edge would create a chord in the induced path. Appending e_t\{v} in arbitrary order realizes the required hypergraph path.
