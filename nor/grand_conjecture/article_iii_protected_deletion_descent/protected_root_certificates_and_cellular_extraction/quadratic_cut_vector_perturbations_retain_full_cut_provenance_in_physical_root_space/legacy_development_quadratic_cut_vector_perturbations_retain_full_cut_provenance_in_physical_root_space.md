# Quadratic cut-vector perturbations retain full cut provenance in physical root space — preserved pre-item development

## Development

## A quadratic cut-vector perturbation remembers the full protected cut

The first cut-moment perturbation in root §47 encodes the barrier side but, as audited in root §51, its moment M(C,rho)=Pi_W(z_C odot rho) depends only on the cut size p and the oriented root rho. The cut identity itself is lost. There is a different dimension-preserving perturbation that retains the entire cut.

Let C be a protected p-cut in an n-coordinate state, let
\[
z_C=\mathbf 1_C-\frac pn\mathbf 1\in W,
\]
and let rho=e_a-e_c be a protected crossing root, with a in C and c outside C. Define
\[
q(C,\rho)=\sum_v \rho_v z_C(v)^2.
\]
Since z_C(a)=1-p/n and z_C(c)=-p/n,
\[
q(C,\rho)
=(1-p/n)^2-(p/n)^2
=1-\frac{2p}{n}.
\]
For normalized ternary deletion states, p+q_1=n-3 and p<=q_1, hence p<n/2. Therefore
\[
q(C,\rho)>0.
\]

Define the full-cut perturbation
\[
\Phi_\varepsilon(\rho,C,s)
=
\rho+\varepsilon s q(C,\rho)z_C
\in W.
\]

### Antipodal oddness

Under complement-reversal,
\[
(\rho,C,s)\mapsto(-\rho,C^c,-s),
\qquad
z_{C^c}=-z_C.
\]
Because the square of z is unchanged,
\[
q(C^c,-\rho)=-q(C,\rho).
\]
Hence
\[
(-s)(-q)(-z_C)=-s q z_C,
\]
and therefore
\[
\Phi_\varepsilon(-\rho,C^c,-s)
=
-\Phi_\varepsilon(\rho,C,s).
\]
Thus the perturbation stays in the original physical root space and remains antipodally odd.

Unlike the first cut moment, the perturbation term is a nonzero scalar multiple of z_C itself, so for p<n/2 it determines C exactly.

### No perturbed two-cycle exists in the ternary normalized state space

Suppose two protected states have opposite physical roots and form a positive dependence after perturbation. The physical root coordinates force the two positive coefficients to be equal. Since the cut sizes are the same normalized p, the scalar q=1-2p/n is common and nonzero.

If the side signs are opposite, the perturbation equation becomes
\[
z_C-z_D=0,
\]
so C=D. But rho crosses C from its source to target, while -rho would require the opposite membership relation in the same cut. This is impossible.

If the side signs are equal, the perturbation equation becomes
\[
z_C+z_D=0.
\]
Then D=C^c and in particular |D|=n-p. Since both cuts have size p, this requires p=n/2, excluded for ternary normalized deletion states.

Therefore no positive two-root circuit survives the full-cut perturbation.

This is stronger than the side-only perturbation: the opposite-side two-cycle is removed as well.

### Signed cut-incidence equation for a simple physical cycle

Let
\[
\rho_i=e_{v_i}-e_{v_{i+1}}
\]
be a simple directed physical root cycle of length k, with all states normalized to the same p. In any positive dependence on this simple cycle, all coefficients are equal. If the perturbed labels also sum to zero, cancellation of the physical roots leaves
\[
\sum_{i=1}^k s_i z_{C_i}=0.
\]
Equivalently,
\[
\sum_{i=1}^k s_i\mathbf 1_{C_i}
=
\frac pn\left(\sum_{i=1}^k s_i\right)\mathbf 1.
\]
The left side is an integer vector. Consequently
\[
n\mid p\sum_i s_i.
\]
Writing d=n/\gcd(n,p), every simple perturbed circuit satisfies
\[
d\mid \sum_i s_i.
\]

This gives an arithmetic obstruction to side imbalance. In particular:

1. k=2 is impossible, as proved above.
2. For k=3, a 2-to-1 side split has side sum +/-1 and is impossible. An all-same-side triangle can survive the incidence equation only if n divides 3p; because 0<p<n/2, this forces p=n/3, in which case the three p-cuts must partition the coordinate set.
3. For k=4, a 3-to-1 side split has side sum +/-2 and is impossible because 2p<n. A balanced 2-to-2 circuit must satisfy equality of the positive-side and negative-side cut incidence vectors. An all-same-side four-cycle can survive only at p=n/4, in which case the four cuts partition the coordinate set.

Thus the perturbation converts any support-minimal physical cycle into a rigid signed block-design condition on its protected cuts.

### Consequence for Article III

Common-face A3 circuits are already locally extractable by root §50, so the new perturbation is aimed at the genuinely global case where a topological carrier mixes several protected cuts. Its value is that a zero can no longer hide cut incompatibility: at the level of a simple physical cycle, the cut data must satisfy the exact signed incidence equation above.

A natural next theorem is to combine this incidence equation with the canonical Johnson edge C -> C-rho_source+rho_target. One should show that a support-minimal signed cut design compatible with the oriented cycle contains either a realizable Johnson exchange, a threshold-band enlargement, or a smaller signed design. For short cycles the arithmetic already leaves only partition-type or balanced-incidence configurations.
