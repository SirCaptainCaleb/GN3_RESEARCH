# Audit: irrational moment coefficients do not separate arbitrary topological zero weights

## Composition

(none yet)

## Development

## Audit: irrational moment coefficients do not separate arbitrary topological zero weights

Root §55 introduces

Xi_epsilon(rho,C,s)
=
rho + epsilon s ( M(C,rho) + theta Q(C,rho) )

with irrational theta, and argues that a positive zero separates into independent M- and Q-equations because the discrete moment vectors have rational coordinates.

That separation is invalid for an arbitrary topological positive zero.

Suppose

sum_i lambda_i Xi_epsilon(rho_i,C_i,s_i)=0,
qquad lambda_i>0.

Even though every rho_i, M_i, and Q_i has rational coordinates, the coefficients lambda_i supplied by a convex/topological zero are arbitrary real numbers. Thus the coordinate vectors

A=sum_i lambda_i s_i M_i,
B=sum_i lambda_i s_i Q_i

need not have rational coordinates. An equality

A + theta B = -(1/epsilon) sum_i lambda_i rho_i

does not split by irrationality; even if the physical-root sum is known to vanish, A+theta B=0 with A,B real does not imply A=B=0.

A one-dimensional model already shows the issue: take arbitrary nonzero real b and a=-theta b.

Therefore the Hamiltonian regular-cut classification in §55 is justified only under an additional hypothesis that the same coefficients already satisfy a rationally constrained physical dependence (for example an equal-coefficient simple root cycle established independently before applying the perturbation), or under a genuinely algebraically independent construction in which the coefficients themselves are controlled. A topological zero of Xi does not supply that hypothesis automatically.

Consequently §§55-59 must not presently be cited as classifying all support-minimal zeroes of the perturbed carrier.

The valid geometric ingredients remain:
- the full-cut vector z_C retains cut identity;
- protected roots are hypersimplex edge vectors;
- a pre-existing physical simple cycle has equal coefficients in its unperturbed positive dependence;
- cut-defect identities apply once such a physical cycle has independently been extracted.

A repair should first extract the limiting physical root dependence, e.g. from a family of perturbed zeroes as epsilon->0, and only then study the first-order moment equation on the limiting kernel.
