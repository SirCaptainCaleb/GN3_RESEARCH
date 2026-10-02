# Coarse singleton-intersection defect axioms admit arbitrary odd-order abstract models

## Statement

For every odd n=2k+1>=3 there exists an abstract family D of subsets of an n-element set V that is pairwise intersecting and has the property that for every x in V there are A_x,B_x in D with A_x∩B_x={x} and A_x∪B_x=V: take D to be all (k+1)-subsets. Therefore any proposed dual abstraction that retains only pairwise intersection plus such singleton-intersection complementary pairs cannot be contradictory on purely set-theoretic grounds; additional path-realizability, disjointness/ownership, or order data are essential.

## Body

Take D=binom(V,k+1). Since 2(k+1)>2k+1, every two members intersect. For fixed x, partition V-{x} into two k-sets C_x,E_x and put A_x=C_x∪{x}, B_x=E_x∪{x}; then A_x,B_x∈D, A_x∩B_x={x}, and A_x∪B_x=V. This is a conditional fence on coarse dual abstractions, not a claim that the actual family of all path complements in a counterexample satisfies pairwise intersection: path-complement data lose support-overlap information, as recorded in f629e48df9ce.