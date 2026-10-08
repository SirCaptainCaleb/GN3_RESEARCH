# Cut-moment perturbations encode side provenance without increasing target dimension — preserved pre-item development

## Composition

(none yet)

## Development

## Cut-moment encoding of protected side provenance in physical root space

Let the physical coordinate set have size n>=3 and let
\[
W=\{x\in\mathbb R^n:\sum_v x_v=0\}.
\]
A protected root state consists of a physical root
\[
\rho=e_a-e_c,
\]
a protected cut C with a\in C and c\notin C, and a side sign s\in\{-1,+1\}. Under complement-reversal the faithful state transforms as
\[
(\rho,C,s)\longmapsto(-\rho,C^c,-s).
\]

Define the centered cut vector
\[
z_C=\mathbf 1_C-\frac{|C|}{n}\mathbf 1\in W
\]
and the cut moment
\[
M(C,\rho)=\Pi_W(z_C\odot\rho),
\]
where \odot is coordinatewise product and \Pi_W subtracts the coordinate mean.

### Lemma 1: the cut moment is antipodally even

For every protected root state,
\[
M(C^c,-\rho)=M(C,\rho).
\]

Indeed z_{C^c}=-z_C, so
\[
z_{C^c}\odot(-\rho)=z_C\odot\rho.
\]
Moreover, because a\in C and c\notin C,
\[
\sum_v (z_C\odot\rho)_v
=(1-|C|/n)+|C|/n=1.
\]
Hence the useful explicit formula is
\[
M(C,\rho)=z_C\odot\rho-\frac1n\mathbf 1.
\]
In particular every coordinate outside \{a,c\} equals -1/n.

### Lemma 2: a same-side opposite-root pair cannot cancel after the perturbation

For any epsilon>0 define
\[
\Psi_\epsilon(\rho,C,s)
=\rho+\epsilon s M(C,\rho)\in W.
\]
Then \Psi_\epsilon is antipodally odd:
\[
\Psi_\epsilon(-\rho,C^c,-s)
=-\Psi_\epsilon(\rho,C,s).
\]

Suppose two genuinely protected states have opposite physical roots but the same side sign:
\[
(\rho,C,s),\qquad(-\rho,D,s).
\]
No positive combination of their perturbed labels is zero.

To see this, write \rho=e_a-e_c and suppose
\[
\lambda\Psi_\epsilon(\rho,C,s)
+\mu\Psi_\epsilon(-\rho,D,s)=0,
\qquad \lambda,\mu>0.
\]
Choose any coordinate j outside \{a,c\}; such a j exists because n>=3. The physical root terms vanish in coordinate j, while both cut moments have j-coordinate -1/n. Therefore the j-coordinate of the displayed positive combination equals
\[
-\frac{\epsilon s}{n}(\lambda+\mu)\ne0,
\]
a contradiction.

Thus the automatic same-side A3 reversal two-cycle can be removed without adjoining an extra target coordinate.

### Opposite sides remain visible

If the two opposite physical roots have opposite side signs, the universal exterior contribution of the cut moments has opposite signs. Hence the preceding obstruction disappears, as it should: the perturbation distinguishes same-side cancellation while retaining the possibility of a genuinely coupled left/right obstruction.

### Topological significance

The earlier side lift (\rho,s) lives in W\oplus\mathbb R and therefore costs one target dimension. The cut-moment perturbation remains in W itself. Consequently any antipodal carrier built from these perturbed labels still has the same ambient dimension as the physical-root carrier, so the even-order tangential fixed-point construction is not lost merely by recording side provenance.

This is not yet a global carrier theorem. One must still build a continuous equivariant face carrier whose local labels use the faithful triples (\rho,C,s), and then audit what a zero or tangential fixed point of the perturbed carrier implies as epsilon tends to zero. In particular, a zero of the perturbed carrier is not literally a positive dependence of the unperturbed physical roots. The gain is narrower but concrete: side provenance can be encoded in the original physical root space, and the spurious same-side opposite-root two-cycle is excluded at every positive epsilon.

### Closure direction

For ternary Article III, apply this perturbation to the terminal threshold-band barrier states. A useful next theorem would construct the continuous perturbed carrier and show that a support-minimal zero or fixed-point limit either yields an opposite-side Johnson-edge obstruction or a strict threshold-band improvement. This would combine the side-sensitive local reduction with the existing fixed-point topology without the dimension penalty of the direct side lift.

### Cycle rigidity for a common minimum phase

Assume now that all protected states in a physical directed cycle use cuts of the same cardinality p. This is the normalized situation for minimum-first-phase Article III states. Put t=p/n.

Let
\[
\rho_i=e_{v_i}-e_{v_{i+1}}
\]
around a simple directed k-cycle, with indices cyclic. Any positive physical dependence on these roots has equal coefficients: from the coordinate equation at v_i, the coefficient of \rho_i equals the coefficient of \rho_{i-1}.

Suppose therefore that the perturbed labels with equal positive coefficient sum to zero:
\[
\sum_i \Psi_\epsilon(\rho_i,C_i,s_i)=0.
\]
The physical roots already sum to zero, so
\[
\sum_i s_i M(C_i,\rho_i)=0.
\]
For a valid crossing root, the cut moment has value
\[
1-t-1/n
\]
at its source, value
\[
t-1/n
\]
at its target, and value -1/n at every other coordinate. Hence at the cycle vertex v_i,
\[
s_i(1-t)+s_{i-1}t-\frac1n\sum_j s_j=0.
\]

If the side labels are balanced, \(\sum_j s_j=0\), this simplifies to
\[
s_i(1-t)+s_{i-1}t=0
\qquad\text{for every }i.
\]

#### Corollary: opposite-root two-cycles are forced to the middle cut

For k=2 a side-balanced pair has opposite side signs. The displayed equation becomes
\[
1-2t=0.
\]
Therefore a perturbed opposite-root two-cycle with common cut size p can survive only when
\[
p=n/2.
\]
So away from the middle cut, the cut-moment perturbation removes even the opposite-side two-cycle.

#### Corollary: balanced four-cycles are forced to alternate sides at the middle cut

For k=4, a side-balanced physical four-cycle can survive the perturbation only when consecutive side signs are opposite and
\[
p=n/2.
\]
Indeed equal consecutive signs make the left side have absolute value 1, while opposite signs give \(\pm(1-2t)\). Thus the only possible balanced four-cycle is the alternating side pattern
\[
+,-,+,-
\]
up to global sign, and only at the perfectly balanced minimum phase.

This sharply narrows the primitive lifted obstruction from root §§37--38. After the perturbation, every side-balanced A3 two-cycle or four-cycle away from p=n/2 is excluded algebraically inside W. At p=n/2, a surviving four-cycle must alternate left and right barriers around the physical cycle.

The result does not yet exclude coupled side-imbalanced cycles, nor does it prove that a continuous perturbed carrier has a zero or fixed point. It identifies the only small balanced circuits compatible with such a carrier.
