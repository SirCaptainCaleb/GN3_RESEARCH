# STS(2ell+1) spanning-path obstruction route

## Statement

If there exists a Steiner triple system S on 2ell+1 vertices containing no spanning linear path P_ell, then disjoint copies of S give ex_L(n,P_ell^(3)) >= (ell/3)n - O(ell^2), and exactly (ell/3)n when 2ell+1 divides n. Thus any infinite family of such non-Hamiltonian Steiner triple systems improves the general lower benchmark (ell-1)n/3 by an additive n/3 on those lengths.

## Body

An STS(2ell+1) has (2ell+1)(2ell)/6 = ell(2ell+1)/3 triples, hence edge/vertex ratio ell/3. A P_ell^(3) has exactly 2ell+1 vertices, so in a component of this order a copy of P_ell is necessarily spanning. Therefore a non-Hamiltonian STS(2ell+1) is P_ell-free. Disjoint copies preserve P_ell-freeness, yielding the stated Turan lower bound. Admissibility requires 2ell+1 congruent to 1 or 3 mod 6, i.e. ell congruent to 0 or 1 mod 3. Current almost-spanning hypertree embedding results do not settle the exact spanning case. The immediate research question is whether infinitely many admissible orders admit an STS with no spanning loose/linear path; failing that, seek a partial STS on 2ell+1 vertices made non-Hamiltonian by deleting fewer than (2ell+1)/3 triples, which would still beat the residue-free (ell-1)/3 benchmark.
