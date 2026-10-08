# Minimum-pair edges normalize to near-balanced cuts or bounded four-components

## Composition

(none yet)

## Development

## Minimum-pair edges admit a near-balanced normalization or a bounded four-component certificate

Let \(H\) satisfy \(\kappa_2(H)=2\), and let \(M\) be its minimum-pair graph:
\[
xy\in E(M)\iff H-\{x,y\}\text{ has a two-cover}.
\]

Fix an edge \(xy\). Among all two-covers
\[
H-\{x,y\}=P\mid Q
\]
choose one minimizing
\[
\Psi(P,Q)=|P|^2+|Q|^2.
\]
Write \(s=|P|\le |Q|=t\).

The imbalanced minimum-hole theorem applies to the minimum deletion set \(\{x,y\}\). Hence, if
\[
t\ge s+2,
\]
the edge \(xy\) already produces one of the bounded four-component outputs described in [[imbalanced_minimum_holes_descend_to_four_component_one_hole_cores]]: either an all-old Hamiltonian four-component in a spanning three-cover of the complement, or a canonical deletion-distance-one core with a Hamiltonian four-component containing one restored hole label.

Therefore, after excluding that bounded branch, every edge of \(M\) may be represented by a \(\Psi\)-minimal cover satisfying
\[
\boxed{|\,|P|-|Q|\,|\le1.}
\]

Consequently:
- if \(|V(H)|\) is even, then \(|V(H)-\{x,y\}|\) is even and every hard minimum-pair edge has a genuinely balanced complementary two-cover;
- if \(|V(H)|\) is odd, every hard edge has complementary path orders differing by exactly one.

Thus a difficult cycle in the minimum-pair graph can be studied as a cycle of near-balanced support bipartitions. Arbitrary highly imbalanced support changes are already discharged into the bounded four-component interface.

This normalization is edgewise and uses no minimum-counterexample hypothesis. It is intended to be combined with deletion-cover compatibility: compatible neighboring cuts force a reversal or four-support, while incompatible neighboring cuts now cross near-balanced support partitions rather than unrestricted ones.
