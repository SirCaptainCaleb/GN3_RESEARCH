# Rank-three coherence defect despite complete square fillings

This subsection exhibits an all-dimensional source of a *three-dimensional* relative switch obstruction that is invisible to every two-dimensional square-filling test. It also applies to the alternating residual three-faces forced by a hypothetical near-spanning bi-monochromatic interval in the preceding subsection.

Let \(F\cong[0,1]^3\), with vertex set \(\{0,1\}^3\). For \(r=0,1,2\), give each edge joining a vertex of Hamming weight \(r\) to one of weight \(r+1\) the bit
\[
\boxed{c(e)=a+r\pmod2,\qquad a\in\{0,1\}.}
\tag{1}
\]
Write \(K_x^b\) for the geometric rooted Freudenthal prefix complex at \(x\in V(F)\), restricted to geodesic prefixes whose edges all have color \(b\). Set
\[
\boxed{U_F^{[0]}=\bigcup_{x\in V(F)} (|K_x^0|\cup|K_x^1|)\subseteq F.}
\tag{2}
\]
The same construction was used to define the square-filling indicator \(\theta\) in Article XIV.

**Theorem 1 (all squares filled but a nonzero relative three-class).** For the coloring (1):

(i) Every one of the six square faces \(G\subseteq F\) has square curvature \(\kappa(G)=0\) and zero-switch relative filling indicator \(\theta(G)=0\). In fact,
\[
\boxed{\partial F\subseteq U_F^{[0]}.}
\tag{3}
\]

(ii) Every monochromatic full length-three geodesic in \(F\) uses only vertices of weights one and two. In particular, every three-simplex in \(U_F^{[0]}\) is contained in the closed slab
\[
\boxed{1\le t_1+t_2+t_3\le2.}
\tag{4}
\]
No point of the interior open corner caps \(0<t_i<1\) with \(\sum_i t_i<1\), or with \(\sum_i t_i>2\), belongs to \(U_F^{[0]}\).

(iii) The integral relative homology has a nonzero free summand:
\[
\boxed{H_3(F,U_F^{[0]};\mathbb Z)\supseteq \mathbb Z.}
\tag{5}
\]
Thus all rank-two squares have zero relative obstruction, while the rank-three cell has a surviving relative filling class.

*Proof.* Consider a square face \(G\). Its two edges from the corner of lower Hamming weight have color \(b\), and its other two edges have color \(1-b\). Its cyclic word is therefore \(b,(1-b),(1-b),b\), a dihedral translate of \(0011\). The XOR of its four edge colors is zero. Moreover, between its two side corners there are two monochromatic two-step routes: one through the bottom vertex, of color \(b\), and one through the top vertex, of color \(1-b\). The corresponding two rooted Freudenthal triangles share the side-corner diagonal and cover the entire square. Thus \(G\subseteq U_F^{[0]}\) for every square, proving (i).

An edge between Hamming levels zero and one, or between levels two and three, has color \(a\), while every edge between levels one and two has color \(1-a\). Any complete antipodal path of length three must cross between levels one and two: its endpoints have complementary Hamming weights, so a path that avoided this middle layer could not connect them. Consequently a monochromatic full path cannot use any edge in the outer Hamming layers, and therefore all its vertices have weights one or two. Conversely the three-step paths alternating between weight-one and weight-two vertices are monochromatic of color \(1-a\), so this constraint is attained. Every three-dimensional simplex in a rooted Freudenthal prefix complex comes from a monochromatic full length-three geodesic and therefore has all vertex weights in \(\{1,2\}\), implying (4). All prefixes of length at most two lie in the geometric boundary \(\partial F\), since at least one dimension remains fixed. Thus no point in either stated interior cap can belong to (2), proving (ii).

Choose a point \(p\) in the first missing cap, for instance \(p=(1/8,1/8,1/8)\). Then \(p\notin U_F^{[0]}\), whereas \(\partial F\subseteq U_F^{[0]}\) by (i). Radial projection from \(p\) gives a continuous map \(r:F\setminus\{p\}\to\partial F\) restricting to the identity on \(\partial F\). Its restriction to \(U_F^{[0]}\) is a retraction onto \(\partial F\). Hence the inclusion of \(\partial F\cong S^2\) in \(U_F^{[0]}\) injects a copy of \(\mathbb Z\) into \(H_2(U_F^{[0]};\mathbb Z)\). The long homology sequence of the pair \((F,U_F^{[0]})\), using contractibility of \(F\), gives
\[
H_3(F,U_F^{[0]};\mathbb Z)
\cong H_2(U_F^{[0]};\mathbb Z)
\supseteq\mathbb Z,
\]
proving (iii). \(\square\)

**Corollary 2 (a forced three-cell defect near a hypothetical counterexample).** Suppose an antipodally odd coloring of \(Q_n\) has no monochromatic full antipodal geodesic, but admits opposite-color monochromatic geodesics between a common ordered pair at distance \(n-3\). By the preceding subsection, both opposed residual three-faces have the alternating layer coloring (1), with complementary phases. Each residual three-face therefore has vanishing rank-two relative switch indicators on all six squares but nonzero relative degree-three homology in its zero-switch prefix union.

*Proof.* The preceding rigidity theorem supplies (1) on each residual face. Apply Theorem 1 independently to the two faces. \(\square\)

**Consequence for dimension-simple Wu--Yang chains.** A repair that tests each square independently for whether its zero-switch rooted prefix union fills the square encounters no obstruction on this example: every square is filled, and all projective square curvatures vanish. Nevertheless the coherent rank-three extension is topologically obstructed. The failure is not merely an inadequacy of a chosen square cocycle; even knowing that each entire boundary square admits a zero-switch filling does not make the three-cell fillable within the same zero-switch prefix union.

The alternating residual face simultaneously exhibits two opposed root corners with no monochromatic two-edge prefix, while monochromatic length-three geodesics exist from other corners in the middle layer. Thus the obstruction respects dimension-simplicity and highlights why cross-root coherence, rather than a scalar square-curvature invariant, is central to the chain-level adaptation of Wu and Yang.
