# Dense-core all-special conjecture

## Statement

For every ell>=4, if H is a P_ell^(3)-free linear 3-uniform hypergraph with minimum degree delta(H)>2ell/3, equivalently delta(H)>=floor(2ell/3)+1, then every edge of H is special in the Devine–Milans snake digraph.

## Body

This is the viable form of the user's all-edges-special conjecture after excluding low-degree star obstructions. Equivalently, every P_ell-free linear triple system containing a nonspecial edge should satisfy delta(H)<=floor(2ell/3). A targeted small-system search found no counterexample above the ratio 2/3 and found an exact equality obstruction at ell=6, delta=4=2ell/3, so the strict inequality is plausibly sharp. If true, the peeling transfer lemma 7a83485f53d4 gives ex_L(n,P_ell^(3))<=floor(2ell/3)n, improving the leading coefficient from 1 to 2/3.