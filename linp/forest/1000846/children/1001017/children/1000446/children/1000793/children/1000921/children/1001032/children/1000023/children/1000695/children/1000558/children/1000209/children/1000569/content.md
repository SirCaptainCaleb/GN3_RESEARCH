# Strict integer form of the ell minus thirteen-sixths upper bound

## Statement

For every ell>=6 and every n, every n-vertex linear 3-uniform hypergraph with no linear P_ell satisfies
  6|E(H)| <= (6ell-13)n-1.
Equivalently,
  |E(H)| <= floor(((6ell-13)n-1)/6).

In particular
  |E(H)| < (ell-13/6)n.

## Body

Suppose for contradiction that a P_ell-free linear 3-graph H has
  m >= (ell-13/6)n.
Among all nonempty subhypergraphs of H choose H0 with maximum edge density rho0=|E(H0)|/|V(H0)|, and subject to that with the fewest vertices. Then rho0>=m/n. If some vertex of H0 had degree at most rho0, deleting it would leave a nonempty subhypergraph of density at least rho0, contradicting the choice of H0 (minimal vertex count among density maximizers). Hence delta(H0)>rho0.

Since ell>=6 and rho0>=ell-13/6>3, we have delta(H0)>=4. The minimum-degree endpoint-potential floor gives phi(v)>=3 for every vertex of H0.

Apply the strict potential theorem 2ef762a38a25 to H0:
  sum_v phi(v) > |E(H0)| + (7/6)|V(H0)|.
Divide by |V(H0)|:
  average(phi) > rho0+7/6
               >= ell-13/6+7/6
               = ell-1.
But H0 is P_ell-free, so every endpoint potential is at most ell-1, contradiction.

Thus
  m < (ell-13/6)n.
Multiplying by six gives the strict integer inequality
  6m < (6ell-13)n.
Both sides are integers, hence
  6m <= (6ell-13)n-1.
The floor formulation is equivalent.
