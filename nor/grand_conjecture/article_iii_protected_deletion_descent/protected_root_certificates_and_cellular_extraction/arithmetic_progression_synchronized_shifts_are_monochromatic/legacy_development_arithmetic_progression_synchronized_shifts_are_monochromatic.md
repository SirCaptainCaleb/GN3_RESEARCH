# Arithmetic-progression synchronized shifts are monochromatic — preserved pre-item development

Continue with a synchronized Hamiltonian endpoint cycle on k ambient coordinates:
V={x_0,...,x_{k-1}},
rho_i=e_{x_i}-e_{x_{i+1}},
a_i=x_{i+r},
with cyclic indices and 2<=r<=k-1.

Endpoint full curvature gives, for every i,
alpha(x_i,x_{i+r},x_{i+1})=0.

Roots §§111-112 use this when r=2 or r=k-1. There is a third arithmetic-progression case.

Assume
2r congruent 1 mod k.

Then gcd(r,k)=1, since every common divisor of r and k divides 2r-1. Hence
x_0,x_r,x_{2r},...,x_{(k-1)r}
is a Hamiltonian order of all physical coordinates.

For its consecutive ternary window beginning at x_{jr}, the indices are
jr, (j+1)r, (j+2)r.
Put i=jr. Because 2r congruent 1,
(j+2)r congruent jr+2r congruent i+1.
Therefore the window is exactly
(x_i,x_{i+r},x_{i+1}),
whose color is 0 by the endpoint full-curvature identity.

Thus every consecutive ternary window in the step-r Hamiltonian order has color 0. The order is spanning monochromatic and proves NOR.

Equivalently, a synchronized Hamiltonian endpoint residue closes whenever the index triple {0,1,r} is a three-term arithmetic progression in Z/kZ. The three possibilities are:
r=2,
r=k-1,
or 2r congruent 1 mod k.
The first two are the extreme-shift theorem; the third is new.

Hence, conditional on the square-lift reduction to synchronized offsets, any genuinely unresolved Hamiltonian residue must satisfy
3<=r<=k-2
and
2r not congruent 1 mod k.

This is a direct closure theorem from actual endpoint full-curvature provenance; it does not require realization of any additional Johnson corner once synchronization is known.
