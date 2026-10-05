# Bounded-radius auxiliary neighborhoods have exact outward replacements

## Metadata

- ID: bounded_radius_auxiliary_neighborhoods_have_exact_outward_replacements
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 7
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Center-preserving bounded-radius replacement

Retain the auxiliary extension \(H^+\), a chamber with \(r=v_k\), and the symmetric radius-\(d\) interval
\[
J_d=[k-d-2,\;k+d+2].
\]
Thus \(J_d\) has \(d+2\) original-vertex positions on each side of \(r\), and
\[
K=V(J_d)\setminus\{r\}
\]
has order \(2d+4\).

**Lemma.**
For \(d\in\{1,2,3\}\), the vertices of \(J_d\) can be reordered while leaving \(r\) in position \(k\), so that the resulting chamber has no violation at any radius at most \(d\). Any newly changed boundary-crossing violation has radius strictly larger than \(d\).

**Proof.**
It is enough to partition \(K\) into two Hamiltonian sets of equal order \(d+2\).

- \(d=1\): \(|K|=6\). Partition \(K\) arbitrarily into two triples; every three-set has a tight order.
- \(d=2\): \(|K|=8\). Use the established balanced \(4|4\) theorem.
- \(d=3\): \(|K|=10\). Use the established balanced \(5|5\) theorem.

Choose tight orders \(P,Q\) on the equal sides. Then
\[
(P,r,Q^{\rm rev})
\]
occupies the same interval and leaves \(r\) fixed. Auxiliary exactification gives directed one-change status \(1^*0^*\) throughout \(J_d\), so all violations of radii at most \(d\) disappear. Because the center is fixed, a status window crossing an endpoint of \(J_d\) has radius \(>d\). \(\square\)

The center-preserving condition is essential. An arbitrary unbalanced two-cover of \(K\) moves \(r\), after which a new small-radius window can cross the old boundary.

This lemma completely handles a **given** first active radius \(d\le3\), including the double-nearest / median-wall configurations already localized to radii \(1,2\).

It does **not** combine with a universal large-radius same-face escape. The addendum [[moving_the_auxiliary_center_can_reverse_arbitrary_large_nearest_radii_without_same_face_escape]] shows that on a non-singleton \(r\)-block, opposite nearest labels at arbitrarily large radius can be produced by moving \(r\) while the same absolute positive witnesses persist. Thus the remaining large-radius problem is the auxiliary-center fiber problem, not another bounded-support problem.
