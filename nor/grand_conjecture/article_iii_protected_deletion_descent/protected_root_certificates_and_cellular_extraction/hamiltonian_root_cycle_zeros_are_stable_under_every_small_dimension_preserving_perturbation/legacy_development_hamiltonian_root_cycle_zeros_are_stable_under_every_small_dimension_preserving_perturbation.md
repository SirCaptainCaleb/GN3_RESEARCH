# Hamiltonian root-cycle zeros are stable under every small dimension-preserving perturbation — preserved pre-item development

## Hamiltonian root-cycle zeros are stable under every small dimension-preserving perturbation

This identifies a structural limit of the side/cut perturbation program.

Let V={v_1,...,v_n} and work in the type-A space

W={x in R^V: sum_v x_v=0},

of dimension n-1. Consider the Hamiltonian directed root cycle

rho_i=e_{v_i}-e_{v_{i+1}},
i=1,...,n

with cyclic indices.

The n columns rho_i span W and have the unique linear dependence

sum_i rho_i=0.

Let eta_i(epsilon) in W be any continuous perturbations with eta_i(0)=0, and define

R_i(epsilon)=rho_i+eta_i(epsilon).

### Theorem

For all sufficiently small epsilon, the perturbed vectors R_1(epsilon),...,R_n(epsilon) admit a positive linear dependence. If their rank remains n-1, that dependence is unique up to scale and its coefficient vector converges, after normalization, to (1/n,...,1/n).

### Proof

Form the linear map

A_epsilon:R^n -> W,
A_epsilon(lambda)=sum_i lambda_i R_i(epsilon).

At epsilon=0, A_0 has rank n-1 and kernel span{1}, where 1=(1,...,1).

Rank n-1 is an open condition on an (n-1)-by-n matrix. Hence whenever the rank remains n-1 for sufficiently small epsilon, ker A_epsilon is one-dimensional and varies continuously in projective space. Choose the normalized kernel vector lambda(epsilon) with sum_i lambda_i(epsilon)=1 and lambda(0)=(1/n,...,1/n). Continuity gives lambda_i(epsilon)>0 for every i when epsilon is small.

If rank drops along a sequence epsilon_j->0, the kernel dimension increases. The normalized positive kernel vector from nearby full-rank parameters has limit points in ker A_{epsilon_j}; equivalently one may perturb epsilon_j arbitrarily slightly and pass to the limit. Thus zero cannot be robustly removed by a small in-space perturbation; at worst the kernel becomes larger.

For the Article III perturbations rho_i+epsilon xi_i with fixed xi_i, the full-rank alternative holds for all sufficiently small epsilon outside the zero set of finitely many minors, and the positive dependence persists continuously through any isolated rank drops by compactness.

### Consequence

No perturbation that keeps the labels in W can eliminate a Hamiltonian simple root-cycle zero merely by making epsilon small. Side moments, cut moments, quadratic cut vectors, or any finite combination of such in-space corrections can only deform the positive coefficient vector.

This explains the correct scope of the valid proper-support exclusion: an exterior coordinate gives a cokernel constraint and can rule out a short cycle. Once the physical cycle spans all n coordinates, its roots already span W, so there is no remaining linear cokernel in which a dimension-preserving provenance moment can force an independent equation.

### Topological implication

A dimension-preserving fixed-point construction should be designed to extract structure from the surviving Hamiltonian zero, not to hope that perturbation removes it. To eliminate that zero one must either

1. add genuinely new target dimension/provenance;
2. restrict the carrier domain so the Hamiltonian circuit cannot occur;
3. or use nonlinear/combinatorial extraction, such as the hypersimplex Johnson-edge geometry, on the stable positive zero.

For Article III, option 3 is the natural current target.
