# Centered-pentagon parity forces a free antipodal square complex with n−3 local degree and at most eight components

# A free antipodal square complex of genuine monochromatic connectors, with only eight components

Let \(n\ge5\) and color the physical **ordered three-faces** of \(Q_n=\{0,1\}^n\) arbitrarily with two colors; the statements about existence and degree need no antipodal hypothesis. Suppose additionally \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) whenever antipodal equivariance is invoked.

For a cube vertex \(z\) and **four pairwise distinct** directions \((a,b,c,d)\), consider the genuine four-edge path
\[
P_z(a,b,c,d):
\quad z\oplus e_a\oplus e_b
\to z\oplus e_b
\to z
\to z\oplus e_c
\to z\oplus e_c\oplus e_d.
\tag{1}
\]
Its two successive ordered-three-face window colors are \(\gamma_z(a,b,c)\) and \(\gamma_z(b,c,d)\), evaluated on their **actual physical faces**. Call it a centered monochromatic four-connector if these two values coincide.

Define the **middle-pair link** \(M_z\) on the coordinate directions \([n]\): the unordered edge \(\{b,c\}\) belongs to \(M_z\) if (1) is monochromatic for some distinct outer directions \(a,d\notin\{b,c\}\) and one of the two inner orders \(b,c\). Form a cubical two-dimensional subcomplex \(X_c\) of the standard cubical \(Q_n\): include **every cube vertex**; for every \(\{b,c\}\in E(M_z)\), include the physical square
\[
Q(z;b,c)=\{z,z\oplus e_b,z\oplus e_c,z\oplus e_b\oplus e_c\}
\]
together with its boundary edges. Every included square has a genuine monochromatic four-connector certificate.

**Theorem 1 (certified-square incidence and large links).** For every \(n\ge5\) and every ordered-three-face binary coloring:

1. Each certified inner pair \(\{b,c\}\in M_z\) is also in \(M_{z\oplus e_b}\), \(M_{z\oplus e_c}\), and \(M_{z\oplus e_b\oplus e_c}\), *with the same ordered connector and identical physical window faces*. Thus \(X_c\) is unambiguously a cubical square complex, and its link at \(z\) is exactly \(M_z\).
2. \(\alpha(M_z)\le4\): **every five directions contain the inner pair of a genuine monochromatic four-connector centered at \(z\)**.
3. At most **three** directions are isolated vertices of \(M_z\). Hence the certified center-move graph \(G_c=X_c^{(1)}\) satisfies
\[
\boxed{\delta(G_c)\ge n-3}
\tag{2}
\]
at every physical cube vertex.
4. Every link has at least
\[
\boxed{|E(M_z)|\ge n(n-4)/8}
\tag{3}
\]
certified middle pairs, and \(X_c\) has at least \(2^{n-5}n(n-4)\) certified physical squares.

**Proof.** For (1), the two ordered faces of (1) have free directions \((a,b,c)\) and \((b,c,d)\). Both free triples contain \(b,c\). Replacing the center \(z\) by \(z\oplus e_b\), \(z\oplus e_c\), or their sum changes the two path windows only in **free coordinates of each face**, so the physical faces and their free orders are literally unchanged. Their colors remain equal.

For (2), choose five distinct directions \(p_0,\ldots,p_4\) in cyclic order, with indices mod 5. Consider the five centered paths \(P_z(p_i,p_{i+1},p_{i+2},p_{i+3})\). The second physical ordered face of path \(i\) is literally the first physical ordered face of path \(i+1\), because both have ordered free triple \((p_{i+1},p_{i+2},p_{i+3})\) and identical fixed exterior bits, including all five named directions. Let their consecutive common window colors be \(t_i\). If none of these paths were monochromatic, then \(t_i\ne t_{i+1}\) for all five indices, forcing an impossible binary alternation around a 5-cycle. Thus some path is monochromatic and its inner pair \(\{p_{i+1},p_{i+2}\}\) is an edge of \(M_z\). No five coordinates are independent in \(M_z\).

For (3), by (2), \(M_z\) has at least one edge \(\{b,c\}\). If it had four isolated direction vertices, they together with \(b\) would be an independent five-set, contradicting (2). Hence at most three directions are isolated. An incident link edge \(\{b,c\}\) certifies the actual cube edge \(z\leftrightarrow z\oplus e_b\), and likewise for \(c\), so all but at most three coordinate edges at \(z\) belong to \(G_c\), giving (2).

For (4), a graph with \(n\) vertices, \(e\) edges and independence number at most four has \(e\ge n(n-4)/8\). A direct proof: take a uniformly random ordering of vertices and select each vertex preceding all its neighbors. The selected set is independent, so \(4\ge\sum_v 1/(\deg(v)+1)\ge n/(1+2e/n)\), by Jensen, yielding the stated bound. Every certified physical square contributes the same link edge at each of its four vertices by (1). Therefore \(\sum_z |E(M_z)|=4f_2(X_c)\), and summing the link bound across all \(2^n\) vertices gives \(f_2(X_c)\ge 2^{n-5}n(n-4)\). \(\square\)

**Theorem 2 (eight components and extremal rigidity).** Every connected component \(C\) of the certified center-move graph \(G_c\) has at least \(2^{n-3}\) cube vertices. Hence
\[
\boxed{b_0(X_c)=b_0(G_c)\le8.}
\tag{4}
\]
If equality holds (exactly eight components), every component is an \((n-3)\)-dimensional coordinate subcube, **every** ordinary cube edge in each of those subcubes is certified, and **every** ordinary two-dimensional coordinate face within each component is a certified square.

**Proof.** For every \(S\subseteq Q_n\), the induced cube edge count satisfies
\[
|E(Q_n[S])|\le\tfrac12|S|\log_2|S|.
\tag{5}
\]
For completeness, induct on \(n\), splitting by the last coordinate into sizes \(a\ge b\). Cross edges are at most \(b\); the inductive bound gives \(E\le(a\log_2a+b\log_2b)/2+b\). This is at most \((a+b)\log_2(a+b)/2\) because the binary entropy \(H_2(t)\) satisfies \(H_2(t)\ge2\min(t,1-t)\), by concavity between \(0,1/2,1\).

For a connected component \(C\) of \(G_c\), every vertex has at least \(n-3\) certified neighbors, all inside \(C\), by (2). Thus its number of induced cube edges is at least \((n-3)|C|/2\); combining with (5) yields \(|C|\ge2^{n-3}\). Eight such components exhaust the entire \(2^n\)-vertex cube, proving (4).

If there are exactly eight, every component has \(|C|=2^{n-3}\) and (5) is attained with equality. The induction proof of (5), using the strictness of \(H_2(t)>2\min(t,1-t)\) outside \(t\in\{0,\frac12,1\}\), shows that a set of size a power of two attaining (5) is a coordinate subcube: at each coordinate split either all vertices lie on one side, or there are equal identical projected halves with every cross edge. Hence each \(C\) is an \((n-3)\)-subcube. It has exactly \(n-3\) internal cube neighbors per vertex, so all internal edges must be certified, while the three outside directions are isolated in \(M_z\). If any pair of internal directions were missing in \(M_z\), they and these three isolated directions would make an independent five-set, contradicting Theorem 1(2). Thus every internal two-face is certified. \(\square\)

**Theorem 3 (a free antipodal topological carrier with unavoidable 2-homology).** Under antipodal-reversal oddness, physical complementation preserves the certified-square complex \(X_c\) and acts *freely* on its geometric realization for every \(n\ge5\). In dimensions \(n\ge19\), it moreover has a large nontrivial second homology group:
\[
\boxed{\dim_{\mathbb F_2}H_2(X_c;\mathbb F_2)
\ \ge\ 2^{n-5}(n^2-20n+32)-8>0.}
\tag{6}
\]

**Proof.** Antipodal reversal sends a centered monochromatic path with direction order \((a,b,c,d)\) and center \(z\) to a centered monochromatic path with direction order \((d,c,b,a)\) and center \(\bar z\), complementing both window colors. Its inner pair remains \(\{b,c\}\), so the antipodal image of each certified square is certified. Physical antipodality \(x_i\mapsto1-x_i\) on the ambient geometric cube fixes only the all-\(1/2\) center, which lies in no cubical face of dimension at most two when \(n\ge3\). Thus the involution on \(X_c\) is free.

The complex contains all \(2^n\) vertices, at most \(n2^{n-1}\) ordinary cube edges, and at least \(2^{n-5}n(n-4)\) certified squares. Its Euler characteristic therefore obeys
\[
\chi(X_c)=f_0-f_1+f_2
\ge 2^{n-5}(n^2-20n+32).
\]
Since \(X_c\) has dimension two, \(\chi=b_0-b_1+b_2\). The component bound \(b_0\le8\) and \(b_1\ge0\) imply (6); the polynomial factor is positive for integers \(n\ge19\). \(\square\)

**Topological significance and exact nonclosure gap.** The certified square complex is a **free** antipodal cubical complex with almost all local coordinate edges, dense links (\(\alpha\le4\)), at most eight components, and substantial 2-homology in large dimensions. This differs favorably from the all-full-geodesics pseudomanifold, whose antipodal action has fixed edge midpoints. However its squares certify local two-window monochromatic connectors; a connected path of *centers* is not automatically one globally monochromatic geodesic, and nonzero ordinary \(H_2\) is not automatically a nonzero **equivariant** Stiefel–Whitney square. The eight-component extreme models can be antipodally paired and have equivariant index zero despite meeting all the displayed local combinatorial bounds. To reach NORI, one must attach root/terminal-memory witness data or show the certified complex forces the exact complementary-support reversed-tail collision (or the four-facet cap-memory odd cycle). No such extraction is asserted here.

**Research direction.** Look for a certificate-preserving simplicial/cubical map from this free, densely connected local-square complex into the exact signed-root reachability interface. Prove a nonzero equivariant index or relative curvature class *for that map*, and show the forced simplex supplies a same-root complement pair. The theorem supplies an unconditional all-dimensional topological carrier created solely from centered five-cycle parity; its missing link is the global path-extraction theorem.
