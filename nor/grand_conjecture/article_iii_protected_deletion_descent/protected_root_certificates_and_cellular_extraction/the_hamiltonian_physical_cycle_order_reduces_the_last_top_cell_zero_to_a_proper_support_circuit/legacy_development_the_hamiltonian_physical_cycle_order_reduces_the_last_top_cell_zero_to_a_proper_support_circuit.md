# The Hamiltonian physical-cycle order reduces the last top-cell zero to a proper-support circuit — preserved pre-item development

## The Hamiltonian physical-cycle order reduces the last top-cell zero to a proper-support circuit

Continue from root §181. Work in a minimum-coordinate pure ternary counterexample and suppose an essential support-minimal top-cell positive root circuit is Hamiltonian:

rho_j=e_{x_j}-e_{x_{j+1}},
j in Z/nZ,

with all x_j distinct and using every physical coordinate.

We show that this circuit is not essential after all.

### Inspect the Hamiltonian coordinate order

Consider the full coordinate order

pi_H=(x_0,x_1,...,x_{n-1}).

Because the ambient instance is a counterexample, its ternary status word is not one-change. Hence it contains an actual 10 descent.

Every ternary slide root carried by pi_H has the form

sigma=e_{x_i}-e_{x_{i+3}}

for some i with 0<=i<=n-4, because consecutive ternary windows drop the coordinate in position i and enter the coordinate three positions later.

### Case n>=5: sigma is a genuine Hamiltonian chord

For n>=5, x_i and x_{i+3} are not consecutive on the cyclic Hamiltonian order in either direction. Thus sigma is not one of the Hamiltonian cycle roots and is not its opposite.

Let

A={rho_i,rho_{i+1},rho_{i+2}}

be the length-three forward arc from x_i to x_{i+3}, and let B be the complementary Hamiltonian arc from x_{i+3} back to x_i.

Then

sigma=rho_i+rho_{i+1}+rho_{i+2},

and because the full Hamiltonian roots sum to zero,

sigma + sum_{rho in B} rho =0.

This is a positive circuit whose endpoint support omits x_{i+1} and x_{i+2}. Hence it is a proper-support circuit.

By root §181, every support-minimal proper-support subcircuit is locally removable by a transverse actual root.

### Why the chord replaces the Hamiltonian zero locally

It remains to justify that removing the chord circuit removes the original Hamiltonian zero rather than merely producing a second unrelated cancellation.

Take the abstract circuit simplex whose vertices are the Hamiltonian root labels rho_0,...,rho_{n-1}; zero lies in its relative interior with equal positive coefficients.

Stellarly subdivide the triangular face spanned by

rho_i,rho_{i+1},rho_{i+2}

and assign the new subdivision vertex the ACTUAL root label sigma from pi_H.

Each maximal simplex in this stellar subdivision contains:
- sigma;
- the entire complementary edge set B;
- exactly two of the three arc roots in A.

View these labels as directed edges on the physical Hamiltonian cycle together with the chord sigma:x_i->x_{i+3}.

In any one maximal subdivided simplex, one of the three forward arc edges in A is absent. Therefore the original Hamiltonian directed cycle is broken. The only directed cycle in this edge set is

sigma together with the complementary arc B.

Equivalently, every positive root dependence in that maximal simplex contains the same smaller circuit

{sigma} union B.

This follows from the graphic-circuit characterization of type-A positive dependencies: a positive dependence is a positive circulation, hence decomposes into directed cycles, and the displayed graph has exactly the one directed cycle sigma+B after one A-edge is removed.

Thus all zeros in the subdivided star are supported on the common smaller chord-circuit face. Perform the transverse actual-root blow-up of root §181 on that proper-support circuit. The whole stellar star becomes zero-free.

Hence the original Hamiltonian zero is locally removable.

### Case n=4

The Hamiltonian coordinate order has only one possible adjacent-window descent root,

sigma=e_{x_0}-e_{x_3}.

The Hamiltonian circuit contains

rho_3=e_{x_3}-e_{x_0}=-sigma.

Therefore any 10 descent in pi_H gives an actual opposite-root pair. Root §176 removes this two-root zero.

If pi_H had no 10 descent, its binary word would already be one-change, contradicting counterexamplehood.

### Case n<=3

A ternary full order has at most one ternary window, so it is automatically NOR-good. No counterexample exists.

### Theorem

Every Hamiltonian support-minimal positive circuit of actual ternary window-slide roots in the top permutahedron cell is locally removable.

Combined with roots §§179 and 181:

- proper-face root circuits are removable;
- top-cell proper-support circuits are removable;
- top-cell Hamiltonian circuits are removable.

Therefore the ACTUAL physical-root carrier admits no essential support-minimal positive zero in the pure ternary minimum-counterexample setting.

Any remaining topological obstruction must come from additional provenance constraints on the carrier/extraction map, not from physical root cancellation itself.
