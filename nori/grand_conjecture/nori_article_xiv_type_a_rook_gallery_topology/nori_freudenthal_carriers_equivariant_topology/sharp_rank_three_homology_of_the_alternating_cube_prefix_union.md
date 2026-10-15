# Sharp rank-three homology of the alternating cube prefix union

# Sharp rank-three homology of the alternating cube prefix union

This subsection sharpens the relative homology calculation of the preceding alternating rank-three cube construction. All six boundary squares admit complete zero-switch Freudenthal fillings, yet the rank-three relative group is not merely nonzero: it is free of rank two.

Let \(F=[0,1]^3\). Color every edge joining a vertex of Hamming weight \(r\) to one of weight \(r+1\), \(r\in\{0,1,2\}\), with
\[
\boxed{c(e)=a+r\pmod2}
\tag{1}
\]
for a fixed \(a\in\mathbb F_2\). Let \(U\subseteq F\) be the union of all monochromatic rooted Freudenthal prefix simplices, allowing every one of the eight cube roots and both colors. Earlier in Article XIV it was proved that the entire cubical boundary \(\partial F\) lies in \(U\).

For distinct \(i,j,k\in\{1,2,3\}\), write
\[
D_{ijk}=\operatorname{conv}\{e_i,e_i+e_j,e_j,e_j+e_k\}.
\tag{2}
\]
These are the six tetrahedra corresponding to the complete monochromatic dimension-simple geodesics whose edge colors are all \(1-a\). Put \(T=\bigcup_{(i,j,k)}D_{ijk}\).

**Theorem 1 (star-shaped interior and annular trace).** One has
\[
\boxed{U=\partial F\cup T.}
\tag{3}
\]
The polyhedron \(T\) is star-shaped about the cube center \(o=(1/2,1/2,1/2)\) and hence contractible. Its intersection \(A=T\cap\partial F\) is an annulus, triangulated by the following six triangles:
\[
\begin{array}{ll}
F\cap\{t_i=0\}:&
\operatorname{conv}\{e_j,e_k,e_j+e_k\},\\
F\cap\{t_i=1\}:&
\operatorname{conv}\{e_i,e_i+e_j,e_i+e_k\},
\end{array}
\qquad\{i,j,k\}=\{1,2,3\}.
\tag{4}
\]
The annulus has its boundary circles in the level planes \(\sum t_i=1\) and \(\sum t_i=2\).

*Proof.* Every monotone two-edge prefix uses at most two of the three cube directions and hence lies on \(\partial F\). Every length-three monochromatic geodesic must remain entirely between Hamming levels one and two because the two outer edge layers have color \(a\) and the middle layer has color \(1-a\). Such a three-edge path necessarily alternates weights \(1,2,1,2\), so, up to reversal, it has the vertex sequence in (2). Conversely each sequence in (2) is a monochromatic geodesic. Thus the three-dimensional members of \(U\) are precisely the \(D_{ijk}\), proving (3) because the entire boundary is covered by shorter prefixes.

Each tetrahedron \(D_{ijk}\) contains both opposite cube vertices \(e_i\) and \(e_j+e_k\), whose midpoint is \(o\). The tetrahedron is convex and contains \(o\); therefore their union \(T\) is star-shaped about \(o\), and contracts linearly onto \(o\).

A tetrahedron meets a cubical face \(t_i=\epsilon\) in the convex hull of its vertices with that fixed bit. Inspecting the six sequences (2) shows that the maximal intersection in every face is the triangle listed in (4), and that all other intersections are its faces. These six triangles join along the six Hamming-level-one-to-two cube edges. Their remaining exposed edges form two disjoint three-edge loops: one connecting the three weight-one vertices, the other connecting the three weight-two vertices. Thus they form a triangulated annulus, proving the claim. \(\square\)

**Theorem 2 (full homotopy type and sharp relative obstruction).** There are homotopy equivalences and integral homology isomorphisms
\[
\boxed{U\simeq S^2\vee S^2,\qquad
H_3(F,U;\mathbb Z)\cong\mathbb Z^2.}
\tag{5}
\]
All other positive relative homology groups \(H_j(F,U;\mathbb Z)\), \(j\ne3\), vanish.

*Proof.* Write \(S=\partial F\cong S^2\). By Theorem 1, \(U=S\cup T\), where \(T\) is contractible and \(A=S\cap T\) is an annulus, hence homotopy equivalent to \(S^1\). The Mayer–Vietoris sequence contains
\[
0=H_2(A)\to H_2(S)\oplus H_2(T)\cong\mathbb Z
\to H_2(U)\to H_1(A)\cong\mathbb Z
\to H_1(S)\oplus H_1(T)=0.
\]
The resulting short sequence \(0\to\mathbb Z\to H_2(U)\to\mathbb Z\to0\) splits because \(\mathbb Z\) is free, so \(H_2(U)\cong\mathbb Z^2\). The same sequence gives \(H_1(U)=0\), \(H_3(U)=0\), and no higher reduced homology. Van Kampen applies because \(S,T,A\) are path-connected and \(S,T\) are simply connected, giving \(\pi_1(U)=0\). By Hurewicz and the homological form of Whitehead's theorem, a map \(S^2\vee S^2\to U\) representing a basis of \(H_2(U)\) is a homotopy equivalence.

Since \(F\) is contractible, the long sequence for the pair \((F,U)\) identifies \(H_j(F,U)\cong\widetilde H_{j-1}(U)\) for \(j\ge2\). The asserted relative groups follow. \(\square\)

**Corollary 3 (two independent polar defects forced near a counterexample).** Suppose an antipodally odd coloring of \(Q_n\) has no monochromatic full antipodal geodesic but has two monochromatic geodesics of opposite colors between a pair of vertices at distance \(n-3\). The two opposed residual three-faces are forced by the earlier rigidity theorem to have complementary instances of coloring (1). Each such face therefore has zero square-curvature and full zero-switch boundary-square coverage, but carries
\[
H_3(F,U_F^{[0]};\mathbb Z)\cong\mathbb Z^2.
\]
The two independent relative classes arise from the two polar components omitted by the star-shaped interior union.

**Interpretation.** Square-level filling conditions are not enough even when all six squares are filled and have vanishing curvature: the missing rank-three information is a two-dimensional group of obstruction classes. Any dimension-simple Wu--Yang chain correction that fills this residual cube must use chains outside the zero-switch prefix union or a nonlocal cancellation with other cells. The result provides a sharp test for constructions on the half-dimensional antipodal chain tower from the preceding Subsection; it is not a disproof or proof of NORI1.
