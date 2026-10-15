# Equivariant winding and the Bockstein obstruction

# The universal Bockstein obstruction to equivariant rank-two fillings

Let \(X\) be a finite regular cell decomposition of \(S^m\), \(m\ge2\), with a free cellular involution \(J\), and let \(Y=X/J\). Let \(\alpha\in H^1(Y;\mathbb F_2)\) classify the double cover \(X\to Y\). This setup includes the dual face-flag spheres of the cube and simplex under their geometric opposition involutions.

**Theorem 1 (integral winding class).** Suppose that
\[
f:X^{(1)}\to S^1,\qquad f(Jx)=-f(x)
\tag{1}
\]
is an odd continuous map defined on the one-skeleton. Its quotient \(\bar f:Y^{(1)}\to\mathbb RP^1\cong S^1\) determines an integer cellular one-cochain \(u\) on \(Y\) whose modulo-two class on the one-skeleton is \(\alpha\). Define
\[
\boxed{\omega(D)=\frac{(\delta u)(D)}2\in\mathbb Z}
\tag{2}
\]
for each oriented two-cell \(D\) of \(Y\). Then \(\omega\) is an integral two-cocycle with
\[
\boxed{[\omega]=\beta(\alpha)\ne0\quad\text{in }H^2(Y;\mathbb Z),}
\tag{3}
\]
where \(\beta\) is the connecting homomorphism for \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb F_2\to0\). The value \(\omega(D)\) is the winding number of the map (1) along the boundary of either lift of \(D\) in \(X\). In particular some dual two-cell has nonzero winding: no odd extension of (1) to all of \(X^{(2)}\) exists.

*Proof.* The double covering \(S^1\to\mathbb RP^1\) pulled back along \(\bar f\) is the restriction of \(X\to Y\) to the one-skeleton. Cellular approximation of \(\bar f\) on this graph gives an integral edge-degree one-cochain \(u\). Its reduction modulo two is the covering cocycle \(\alpha\) there. Since the latter extends as a cocycle on \(Y\), the integral coboundary \(\delta u\) is even on every two-cell. Hence (2) is integral, and \(\delta\omega=0\). The degree of \(\bar f\) on the attaching circle of \(D\) is \((\delta u)(D)\); it is twice the degree of its lift under \(f\) because the target map \(S^1\to\mathbb RP^1\) is a two-fold covering. This proves the winding assertion. The cochain construction of the integral Bockstein identifies \([\omega]\) with \(\beta(\alpha)\).

The sphere \(X\) is simply connected for \(m\ge2\), so \(\pi_1(Y)\cong\mathbb Z_2\). Therefore \(H^1(Y;\mathbb Z)=\operatorname{Hom}(\mathbb Z_2,\mathbb Z)=0\), whereas \(\alpha\ne0\). The Bockstein long sequence makes \(\beta\) injective at \(H^1(Y;\mathbb F_2)\); thus (3) is nonzero. If all two-cell windings vanished, \(\omega\) would be zero, contradicting (3). Changing target edge paths by additional full turns changes \(u\) by twice an integral one-cochain and changes \(\omega\) by its coboundary; the class (3) is unchanged. \(\square\)

**Theorem 2 (higher first-obstruction skeleton).** For every \(0\le k<m\), there is no odd continuous map
\[
\boxed{X^{(k+1)}\longrightarrow S^k.}
\tag{4}
\]
Thus an odd map already constructed on the \(k\)-skeleton must fail extension on some \((k+1)\)-cell.

*Proof.* The mod-two cohomology ring of the quotient of a sphere by a free involution is
\[
H^*(Y;\mathbb F_2)=\mathbb F_2[\alpha]/(\alpha^{m+1}).
\tag{5}
\]
This follows from the standard covering/Gysin sequence (or the classifying-space spectral sequence). In particular \(\alpha^{k+1}\ne0\). Restriction to \(Y^{(k+1)}\) retains this nonzero class: adding higher-dimensional cells can only impose further relations in degree \(k+1\). If (4) existed, it would yield a quotient map \(Y^{(k+1)}\to\mathbb RP^k\) pulling the universal double-cover class back to \(\alpha\). But the \((k+1)\)-st power of the class in \(H^1(\mathbb RP^k;\mathbb F_2)\) is zero, contrary to \(\alpha^{k+1}\ne0\). \(\square\)

**NORI1 application.** Suppose an antipodally odd cube-edge coloring had no monochromatic full antipodal geodesic. Then every complete-path color word would have at least two switches. The signed-second-switch construction from Article XIV gives an odd map on the dual type-B Coxeter one-skeleton, with target \(S^{n-3}\), because labels of adjacent complete flags are nonopposite. Theorem 2 forces an extension obstruction on the dual \((n-2)\)-skeleton. At \(n=4\), Theorem 1 says that the target circle has a nonzero winding around the boundary of some rank-two dual cell. The accompanying Article XV note gives a valid cube-edge coloring with winding \(+1\) on the initial eight-flag dihedral residue; it does not assert absence of monochromatic geodesics elsewhere.

**Research consequence.** Dihedral winding defects are not independent local choices. They assemble into the nonzero class (3), which cannot be annihilated simply by rerouting target edges equivariantly. A proof of the monochromatic full-path conjecture through this method must show that the *colored local incidence* supplies additional chain-level cancellations inconsistent with the nonzero obstruction class whenever no favorable complete path exists. In the ordinary boundary-tournament case, a separate starting difficulty remains: opposite complete flags can carry identical self-complement-reversed words, preventing every word-only odd label. The common chain construction must retain flag information as well as switch data.
