# Multi-root Cech chains and the switch filtration

# Multi-root Čech chains and the geodesic switch filtration

Fix an arbitrary edge coloring of \(Q_n\), \(n\ge3\). Let \(K_x^{[r]}\) be the rooted Freudenthal geodesic-prefix complex of paths with at most \(r\) switches. Place all these complexes inside a single barycentric subdivision of the common type-D refinement constructed earlier in this Article. Define
\[
U^{[r]}=\bigcup_{x\in Q_n}K_x^{[r]},\qquad
K_A^{[r]}=\bigcap_{x\in A}K_x^{[r]}
\]
for every nonempty root set \(A\subseteq Q_n\).

**Theorem 1 (multi-root chain resolution).** Put
\[
\boxed{
B_{p,q}^{[r]}=
\bigoplus_{\substack{A\subseteq Q_n\\|A|=p+1}}
C_q(K_A^{[r]};\mathbb F_2).
}
\tag{1}
\]
Equip it with the ordinary simplicial boundary vertically and the alternating-deletion Čech boundary horizontally (signs disappear over \(\mathbb F_2\)). The total differential squares to zero, and augmentation from its total complex to the simplicial chains of \(U^{[r]}\) is a quasi-isomorphism. The associated intersection spectral sequence is
\[
\boxed{
E^1_{p,q}(r)=\bigoplus_{|A|=p+1}
H_q(K_A^{[r]};\mathbb F_2)
\Longrightarrow H_{p+q}(U^{[r]};\mathbb F_2).
}
\tag{2}
\]
Every switch-filtration inclusion induces compatible morphisms of these chain complexes and spectral sequences.

*Proof.* The horizontal and vertical boundaries commute and each squares to zero. For every simplex \(\sigma\in U^{[r]}\), let \(I(\sigma)\) be the nonempty set of roots whose complexes contain it. The horizontal complex contributed by \(\sigma\) is the augmented simplicial chain complex of the full simplex on \(I(\sigma)\); it is contractible. Resolving each simplex in this way proves the augmentation is a quasi-isomorphism. The other filtration gives (2), and nesting in \(r\) gives the functoriality. \(\square\)

**Theorem 2 (free antipodal indexing at switch level zero).** Assume the edge coloring is antipodally odd and, hypothetically, no full geodesic has at most one switch. Then every nonempty root-index intersection \(K_A^{[0]}\) has an index set \(A\) containing no pair \(x,\bar x\). Consequently the antipodal involution acts freely on all nonzero root-index summands of \(B_{\bullet,\bullet}^{[0]}\).

*Proof.* The rank-preserving gluing theorem of this Article says \(K_x^{[0]}\cap K_{\bar x}^{[0]}=\varnothing\) under the hypothesis. An intersection indexed by a set containing both roots is therefore empty. Any index set fixed under root complementation contains an antipodal pair, so no nonempty index summand can be fixed. The antipode maps \(K_A^{[0]}\) to \(K_{\bar A}^{[0]}\), proving the result. \(\square\)

**Proposition 3 (dimension barrier for the ordinary nerve).** The nerve of the rooted monochromatic prefix complexes has dimension at least \(n\), regardless of the coloring.

*Proof.* Fix any cube vertex \(y\). The trivial prefix puts \(y\in K_y^{[0]}\). For every dimension \(i\), the one-edge geodesic from \(y\oplus e_i\) to \(y\) is monochromatic, so \(y\in K_{y\oplus e_i}^{[0]}\). These \(n+1\) distinct root complexes have a common vertex and span an \(n\)-simplex of the nerve. \(\square\)

**Research consequence.** The individual rooted Rees complexes are filtered contractible, so their homology alone cannot reveal the antipodal one-switch obstruction. The intersection complex (1) instead retains the disconnected and empty multi-root square carriers proved earlier. But Proposition 3 rules out a naive dimension-bound argument on its ordinary nerve: that nerve is already at least \(n\)-dimensional, while the cubical boundary source has dimension \(n-1\). A successful Wu–Yang adaptation must cancel higher-root overlap terms using their full-rank path certificates and rank-two color-comparison data, yielding a lower-dimensional equivariant chain target. The present resolution does not establish such a cancellation.
