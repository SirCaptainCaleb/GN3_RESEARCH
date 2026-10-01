# Strict pair-union balance improvement

## Statement

Let A and B be vertex-disjoint tight paths in a boundary tournament with |A|>=|B|+2. Then the induced subtournament on V(A) union V(B) has a two-cover R|S satisfying ||R|-|S||<|A|-|B||.

## Body

This is the local balancing statement isolated by the certified reduction 257497a6d724. It is strictly weaker than Astra-002: it asks only for improvement relative to an already displayed imbalanced two-cover, not a balanced two-cover of every boundary tournament.

If true, repeated application removes all component-size imbalance from any three-cover by strict descent of the quadratic potential. The remaining obligation for Astra-003 would then be to escape equitable three-covers by path-order or orientation structure.

The endpoint-transfer lemmas show why this is plausible but nontrivial. If a suitable endpoint block of the larger path Hamiltonizes together with the smaller support, transferring it gives the required improvement. At a hypothetical failure, all such improving transfers are therefore forced non-Hamiltonian, producing a structured family of extension obstructions that should be attacked globally rather than by fixed-order classification.

No proof is asserted here.
