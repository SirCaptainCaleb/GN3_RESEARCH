# Maximum average degree three for the ascending terminal graph

## Statement

Let H be a finite linear 3-graph. Form the simple graph T_↑ whose edges are the terminal pairs of the ascending nonspecial hyperedges of H. Then every nonempty subgraph J of T_↑ satisfies 2|E(J)|<=3|V(J)|; equivalently mad(T_↑)<=3.

## Body

This is a strengthening of the global conjecture A<=3|V(H)|/2. Since |E(T_↑)|=A and V(T_↑)⊆V(H), the displayed inequality for J=T_↑ gives A<=3|V(T_↑)|/2<=3|V(H)|/2. The hereditary form is chosen because it isolates the sharp structural claim on terminal pairs themselves. It does not conflict with the unbounded common-last-vertex construction d5e0ab668a51, whose large terminal degree is supported by many low-degree vertices. It is exactly sharp on the family c3e95f4ce77d: there T_↑ is a disjoint union of copies of K_{3,3}, hence 3-regular and 2|E|=3|V| componentwise. The refuted pointwise conjecture asserted Δ(T_↑)<=3; the present conjecture permits arbitrarily large maximum degree while requiring every terminal subgraph to have average degree at most three.
