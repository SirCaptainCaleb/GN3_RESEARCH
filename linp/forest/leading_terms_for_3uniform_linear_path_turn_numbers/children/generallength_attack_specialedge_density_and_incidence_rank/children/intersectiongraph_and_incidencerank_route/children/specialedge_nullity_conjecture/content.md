# Special-edge nullity conjecture

## Statement

For every finite linear 3-uniform hypergraph H with incidence matrix N and s special edges in the Devine–Milans snake digraph, nullity_R(N) <= s.

## Body

This is an unproved bridge between the incidence-rank and snake routes. Since m=rank(N)+nullity(N), the conjecture gives m-s<=rank(N). Thus the number b=m-s of nonspecial edges satisfies b<=rank(N)<=n. Combining with the certified hinge 3m-b<=(2ell-3)n for a P_ell-free H would yield 3m<=(2ell-2)n, hence m<=2(ell-1)n/3. The conjecture is deliberately stated without a P_ell-free hypothesis: specialness already depends on globally longest linear paths, and the finite search through n<=7 found no counterexample in arbitrary linear triple systems. A naive stronger route is false: the nonspecial incidence columns need not be independent, so a proof must control nullity dimension globally rather than hit every circuit with a special column.