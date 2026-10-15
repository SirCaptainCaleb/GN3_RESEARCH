# Disjoint antipodal geodesic packings and independent short-port cocircuit tests

Let \(Q_n\) be the \(n\)-cube, \(n\ge3\), \(\tau(x)=x+\mathbf1_{[n]}\), and \(H_n=L(Q_n/\tau)\), whose \(n2^{n-2}\) vertices correspond to antipodal orbits of cube edges. Fix any order \(\pi=(1,\ldots,n)\) of coordinate directions. For a starting vertex \(x\), let \(C_x^\pi\subseteq H_n\) be the simple length-\(n\) turn cycle of the antipodal geodesic starting at \(x\) and visiting coordinates in order \(\pi\).

**Theorem 1 (geodesic vertex-disjoint packing).** For even \(n\ge4\), choose one representative \(x\) from each antipodal pair of even-parity cube vertices. The family of cycles \(C_x^\pi\), indexed by those \(2^{n-2}\) roots, partitions \(V(H_n)\) into pairwise vertex-disjoint cycles of length \(n\). In particular it is a 2-factor of \(H_n\), all of whose components are shortest odd-monodromy turn cycles.

For odd \(n\ge3\), choose every even-parity cube vertex \(x\) whose first two coordinates are zero. The resulting \(2^{n-3}\) cycles \(C_x^\pi\) are pairwise vertex-disjoint.

*Proof.* Along a fixed order \(\pi\), the state corresponding to direction \(i\) on the path from \(x\) is the cube edge starting at \(x\) translated by the fixed preceding-coordinate prefix. Suppose the projected edge states in direction \(i\) from roots \(x,y\) coincide. Two unoriented cube edges lie in the same antipodal orbit precisely when one is the other, its endpoint reversal, its antipodal translate, or the endpoint reversal of that translate. Translating away the common coordinate prefix gives
\[
\boxed{y\in\{x,\ x+e_i,\ \tau x,\ \tau x+e_i\}.}\tag{1}
\]
For even \(n\), both selected roots have even parity, excluding \(x+e_i\) and \(\tau x+e_i\). The two remaining possibilities are the same selected root or its antipode, and the latter is excluded by choosing one representative from each pair. Thus the cycles are vertex-disjoint. Their number times \(n\) equals \(|V(H_n)|\), proving the partition assertion.

For odd \(n\), \(x+e_i\) and \(\tau x\) have odd parity, so neither is selected. The point \(\tau x+e_i\) has at least one of its first two coordinates equal to one, whether \(i\) belongs to those two directions or not. Since all selected roots have both coordinates zero, this final possibility is also excluded. Their number is \(2^{n-3}\), proving the second assertion. \(\square\)

**Corollary 2 (pointed-cocircuit sunflower).** Let \(D_n\) be the pointed binary turn matroid and \(p\) its distinguished port. Each cycle \(C_x^\pi\) determines a shortest port cocircuit \(Y_x=E(C_x^\pi)\cup\{p\}\). The family of such cocircuits satisfies
\[
\boxed{Y_x\cap Y_y=\{p\}\quad(x\ne y),}\tag{2}
\]
and has cardinality \(2^{n-2}\) when \(n\) is even, and \(2^{n-3}\) when \(n\) is odd.

*Proof.* Disjoint turn-cycle vertex sets give disjoint turn-edge sets, while each port cocircuit contains \(p\). \(\square\)

**Theorem 3 (exponential-probability monochromatic NORI1).** Color each antipodal orbit of cube edges independently with an unbiased bit, giving its antipodal mate the complementary bit. Then the probability that the coloring has a monochromatic full antipodal geodesic obeys
\[
\boxed{
\Pr(\mathrm{NORI1\ witness})
\ge
\begin{cases}
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-2}}
\ge1-e^{-n/2},&n\text{ even},\\[6pt]
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-3}}
\ge1-e^{-n/4},&n\text{ odd}.
\end{cases}}\tag{3}
\]

*Proof.* For one fixed antipodal-geodesic turn cycle, the \(n\) cube-edge states belong to distinct antipodal edge orbits. Their edge colors are therefore independent unbiased bits. The cyclic comparison of consecutive states uses the deck complement of the first bit at the closing seam. The cyclic number of disagreements is one precisely when the linear color word is constant, or changes once between two constant blocks. There are \(2\) constant words and \(2(n-1)\) one-change words, among \(2^n\) equally likely words. Thus
\[
\Pr(w_d(C)=1)=\frac{2n}{2^n}=\frac{n}{2^{n-1}}.
\]
A cycle of cyclic turn weight one can be rerooted at its changed turn to give a monochromatic full antipodal geodesic. By Theorem 1, the cycles in the selected packing have disjoint edge-state orbit sets. Thus their weight-one events are independent. The complement of the event that at least one succeeds has probability \((1-n/2^{n-1})^k\), where \(k\) is the size of the packing. Substituting the two values of \(k\) gives (3); the exponential estimates follow from \(1-z\le e^{-z}\). \(\square\)

**Proposition 4 (why the full 2-factor is restricted to even dimension).** For odd \(n\), the turn graph \(H_n\) cannot have a partition of its vertices into antipodal-geodesic turn cycles, regardless of coordinate ordering.

*Proof.* Such a partition would cover every edge of the folded cube \(G_n=Q_n/\tau\) by edge-disjoint closed geodesic walks. Each component is a graph cycle, so their union would give every vertex of \(G_n\) even degree. But \(G_n\) is \(n\)-regular with \(n\) odd. This is impossible. \(\square\)

The two-factor theorem produces many independently testable shortest port cocircuits, and the probability bound quantifies how unlikely a counterexample is under an unbiased deck-odd coloring. It does not prove the worst-case conjecture: an adversarial coloring could make all members of one packing have at least three disagreements. Relations between different packings, rather than independence within a single packing, would be needed for a deterministic closure.
