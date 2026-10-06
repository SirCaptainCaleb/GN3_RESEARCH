# The top deletion-cover chain has boundary exactly at unique-extension two-hole states

## Metadata

- ID: the_top_deletion_cover_chain_has_boundary_exactly_at_unique_extension_two_hole_states
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 255
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The top deletion-cover chain has boundary exactly at unique-extension two-hole states

Assume \(H\) has no spanning two-cover.

Let
\[
F=(A,B)
\]
be an oriented pair of disjoint nonempty Hamiltonian supports with
\[
A\sqcup B=V(H)-\{x,y\}.
\]

Define the four one-hole extension indicators
\[
\alpha_x=[H[A+x]\text{ Hamiltonian}],\qquad
\beta_x=[H[B+x]\text{ Hamiltonian}],
\]
\[
\alpha_y=[H[A+y]\text{ Hamiltonian}],\qquad
\beta_y=[H[B+y]\text{ Hamiltonian}].
\]

These are exactly the top support-pair facets containing \(F\): adding one missing label to one of the two sides yields a support pair of total order \(n-1\).

### Cross extensions are forbidden

\[
\alpha_x\beta_y=0,
\qquad
\alpha_y\beta_x=0.
\]

Indeed, if \(\alpha_x=\beta_y=1\), then
\[
(A+x)\mid(B+y)
\]
is a spanning two-cover of \(H\). The other identity is symmetric.

### Odd incidence is exactly unique incidence

Put
\[
d(F)=\alpha_x+\beta_x+\alpha_y+\beta_y.
\]
If \(d(F)\) is odd, then
\[
\boxed{d(F)=1.}
\]

Proof. The only other odd possibility is \(d(F)=3\). But every three-element subset of the four extension positions contains one of the forbidden cross pairs
\[
\{\alpha_x,\beta_y\},\qquad
\{\alpha_y,\beta_x\}.
\]
Hence degree three is impossible. \(\square\)

Thus every two-hole support state has extension degree
\[
0,\ 1,\ 2,
\]
and the degree-two patterns are restricted to:

- both extensions of one hole:
  \[
  \{\alpha_x,\beta_x\}\quad\text{or}\quad
  \{\alpha_y,\beta_y\};
  \]
- both holes into the same side:
  \[
  \{\alpha_x,\alpha_y\}\quad\text{or}\quad
  \{\beta_x,\beta_y\}.
  \]

The two crossed degree-two patterns are exactly the forbidden spanning two-covers.

### Chain interpretation

In a minimum-order counterexample, \(\kappa_2(H)=1\). Let \(C_{\rm top}\) be the mod-two sum of all oriented top-dimensional simplices of the signed support-pair downward-closure complex \(E(H)\), equivalently all support pairs of total order \(n-1\).

A codimension-one face \(F=(A,B)\) of total order \(n-2\) occurs in
\[
\partial C_{\rm top}
\]
iff its number \(d(F)\) of top extensions is odd. By the theorem above,
\[
\boxed{
\operatorname{supp}(\partial C_{\rm top})
=
\{\text{two-hole support states having exactly one one-hole extension}\}.
}
\]

So the failure of the obvious top chain to be a cycle is completely localized: there are no degree-three parity defects, no general high-valence coherence defects, and no need to compare Hamilton orders. The entire boundary is the set of **unique-extension faces**.

Equivalently, every non-unique two-hole state is already parity-balanced at top rank.

This gives a chain-level closure target:

> eliminate, pair, or equivariantly transport the unique-extension faces.

Any successful local theorem doing that supplies an actual correction to the global top chain. This is a more precise role for the late endpoint/reversal and dissimilar-deletion-cover machinery than treating their local configurations as terminal proof states.
