# Hamiltonian root cycles survive every small perturbation inside physical root space — preserved pre-item development

## Development

There is a structural limitation on every attempt to encode protected provenance by a small perturbation that remains in the physical type-A root space W.

Let v_1,...,v_n be all physical coordinates and let
rho_i=e_{v_{i+1}}-e_{v_i}
cyclically. These n roots form a directed Hamiltonian cycle. Their span is all of W, of dimension n-1, and their only linear dependence up to scale is
sum_i rho_i=0.
The kernel coefficient vector (1,...,1) is strictly positive.

Now assign arbitrary provenance perturbations m_i in W and form
rho_i(epsilon)=rho_i+epsilon m_i.
For sufficiently small epsilon, the n by (n-1)-dimensional column configuration still has a nonzero kernel. Choose any n-1 columns that are independent at epsilon=0; they remain independent for small epsilon. Normalize the remaining kernel coefficient to one and solve linearly for the other n-1 coefficients. The resulting kernel vector depends continuously on epsilon and equals the all-ones vector at epsilon=0. Hence all coefficients remain strictly positive for sufficiently small |epsilon|.

Therefore:

Every sufficiently small W-valued perturbation of a Hamiltonian directed root cycle still has a positive dependence.

This applies to the side moment, full-cut quadratic moment, irrational combinations of moments, and any other provenance perturbation that stays in W. Such perturbations may rigidify or eliminate proper-support circuits, but they cannot topologically remove a Hamiltonian physical root cycle.

The reason is dimensional. A simple physical cycle on k<n coordinates spans a (k-1)-dimensional subspace of W and has transverse directions available for provenance constraints. A Hamiltonian cycle spans all of W, so an in-space perturbation can be absorbed by changing its positive coefficients. To impose an additional independent scalar balance on a Hamiltonian cycle one must either:

1. add an extra target coordinate, as in the direct side lift W plus R;
2. impose provenance through the domain/cut geometry rather than through a W-valued vector perturbation; or
3. use direct combinatorics such as the Johnson cut-defect circulation.

This explains the current Article III architecture. Dimension-preserving moments are useful for local/proper-support extraction and for identifying hypersimplex geometry, but the final Hamiltonian obstruction must be attacked by the explicit cut/shore state, an extra-dimensional topological section, or a terminating cut-defect argument. It should not be expected to disappear from a more ingenious W-valued perturbation.
