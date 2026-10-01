# Minimum-degree-first convention for the 2/3 route

## Statement

For the main route toward ex_L(n,P_ell^(3))<=floor(2ell/3)n, impose δ(H)>=floor(2ell/3)+1 at the outset by the minimal-counterexample reduction before applying snake, ascending-edge, rank, blocker, or computational attacks.

## Body

This is a methodological convention for the live 2/3 route. A construction or computation with smaller minimum degree may still refute a theorem stated universally for all linear 3-graphs, but it does not refute the version actually needed inside a smallest counterexample to the target Turán bound. Such examples must be labeled 'outside the admissible minimum-degree regime' when used against the main route. Searches intended to falsify the live route should enforce the minimum-degree hypothesis from the beginning. The threshold changes with the exact candidate coefficient d: for |E(H)|<=d|V(H)| the free assumption is δ(H)>d.
