# Audit: a Hamiltonian root simplex has nonzero local degree and cannot be removed relative to its boundary — preserved pre-item development

## Audit: a Hamiltonian root simplex has nonzero local degree and cannot be removed relative to its boundary

This corrects root §183.

Let

rho_i=e_{x_i}-e_{x_{i+1}},
i in Z/nZ,

be a Hamiltonian directed root circuit on all n physical coordinates. Work in the type-A space

W={z in R^V: sum_v z_v=0},

of dimension n-1.

The n root vectors rho_0,...,rho_{n-1} span W and have the unique linear dependence

rho_0+...+rho_{n-1}=0.

Because the coefficients of this dependence sum to n rather than zero, it is NOT an affine dependence. Hence the n points rho_i are affinely independent.

Therefore

Delta=conv{rho_0,...,rho_{n-1}}

is an (n-1)-simplex in W, and 0 lies in its relative interior with barycentric coordinates 1/n.

### Local degree obstruction

The affine label map from the corresponding domain simplex to W is an affine homeomorphism onto Delta. Its restriction to the boundary sphere has degree plus or minus one around 0.

Consequently no continuous modification that keeps the boundary labels/map fixed can make this simplex zero-free. Any relative-boundary filling must contain a zero.

This is exactly the dimension-saturated obstruction predicted by the Hamiltonian stability theorem: the root circuit has d+1 vertices in a d-dimensional target and encloses the origin.

### What the Hamiltonian chord construction actually does

Root §183 correctly observes that in the Hamiltonian coordinate order

(x_0,...,x_{n-1})

any actual ternary 10 descent gives a chord root

sigma=e_{x_i}-e_{x_{i+3}}

for n>=5, and

sigma + sum_{rho in B} rho=0

on the complementary Hamiltonian arc B. This is a genuine proper-support positive circuit.

It is also correct that a stellar subdivision of the three-edge arc face using the chord label sigma can concentrate a zero on the smaller chord circuit.

What is NOT correct is the claim that removing that proper-support chord circuit makes the entire stellar star zero-free. The outer boundary of the original Hamiltonian simplex still has degree plus or minus one. After any local removal of the chord-circuit zero, another zero must occur elsewhere in the subdivided star.

Equivalently, the chord operation can TRANSFER the local degree among zeroes but cannot annihilate the total local degree of the Hamiltonian simplex.

### Correct status

Roots §§179 and 181 remain compatible with topology:

- a proper-face circuit lies in a proper target subspace and can have a transverse blow-up;
- a top-cell circuit with proper endpoint support also lies in the proper subspace W_S and can have a transverse blow-up.

The Hamiltonian circuit is different because W_S=W. No transverse target direction remains, and its circuit simplex is full-dimensional.

Therefore the Hamiltonian top-cell root zero remains the genuine final physical-root obstruction. Any closure must use EXTRA STRUCTURE beyond the bare W-valued physical-root map, for example:

1. witness/cut/side provenance in additional target data;
2. a domain restriction whose boundary degree changes the local index accounting;
3. or a combinatorial extraction from the Hamiltonian zero that directly produces a NOR order rather than attempting to remove the zero.

Do not cite root §183 as eliminating Hamiltonian physical-root zeroes. Its chord identity is valid; its relative-boundary zero-removal conclusion is refuted by local degree.
