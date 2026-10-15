# Matroid-independent tournament paths and terminal growth

Let \(G=(V,E)\) be a finite simple graph with at least one edge, and let \(N\) be a matroid on \(E\). Assume
\[
\tag{1}
\mathcal I(N)\subseteq\mathcal I(M(G)),\qquad
\delta_G(v)\in\mathcal I(N)\quad(v\in V),
\]
where \(M(G)\) is the graphic matroid and \(\delta_G(v)\) is the star at \(v\). At each vertex \(v\), prescribe an arbitrary tournament \(T_v\) on \(\delta_G(v)\). A vertex word \(P=(v_1,\ldots,v_\ell)\) is an *independent tournament path* when its consecutive edges are pairwise distinct, their set is independent in \(N\), and
\[
v_{i-1}v_i\longrightarrow v_iv_{i+1}\quad\text{in }T_{v_i}
\qquad(2\le i<\ell).
\]
Condition (1) implies that an independent tournament path has distinct vertices. Indeed, a closed subwalk with pairwise distinct edges contains a graph cycle, contradicting independence in \(N\).

**Theorem (matroid terminal-growth bound).** Let \(L\) be the maximum number of vertices in an independent tournament path, and let \(\bar d=2|E|/|V|\). Then
\[
\boxed{\quad\frac{\bar d}{2}\le(L-1)^2,\qquad
L\ge1+\sqrt{\frac{\bar d}{2}}.\quad}\tag{2}
\]
The bound holds for arbitrary matroids \(N\), including nonrepresentable matroids.

*Proof.* For every \(e=uv\in E\), let \(r(e)\) be the maximum order of an independent tournament path ending in either \(u,v\) or \(v,u\). Orient \(e\) toward the last vertex of one maximizing path. Some vertex \(v\) receives at least \(\bar d/2\) oriented edges. For \(2\le r\le L\), write \(D_r(v)\) for the incoming edges with \(r(e)=r\), and let \(q=|D_r(v)|\).

For \(q>0\), choose \(e=uv\in D_r(v)\) which beats at least \((q-1)/2\) other members of \(D_r(v)\) in \(T_v\). Let \(P\) be an independent tournament path of order \(r\) ending in \(u,v\), and put \(A=E(P)\). Then \(r_N(A)=r-1\). If \(f=vw\in D_r(v)\) is beaten by \(e\) and \(f\notin\operatorname{cl}_N(A)\), the word obtained by appending \(w\) to \(P\) has independent edge set \(A\cup\{f\}\). By (1), this set is a forest; consequently \(w\) is new to \(P\). The tournament comparison at \(v\) is legal, so the new word is an independent tournament path of order \(r+1\), contradicting \(r(f)=r\).

Thus every member of \(D_r(v)\) beaten by \(e\) belongs to \(\operatorname{cl}_N(A)\). Since \(\delta_G(v)\) is independent in \(N\),
\[
\bigl|\delta_G(v)\cap\operatorname{cl}_N(A)\bigr|
\le r_N(A)=r-1.
\]
One of these edges is \(e\). Hence \((q-1)/2\le r-2\), giving \(q\le2r-3\). Summing over terminal ranks yields
\[
\frac{\bar d}{2}\le d^-(v)
=\sum_{r=2}^{L}|D_r(v)|
\le\sum_{r=2}^{L}(2r-3)
=(L-1)^2.
\]
This proves (2). \(\square\)

**Transitive refinement.** If every \(T_v\) is transitive, then
\[
\boxed{\quad \bar d\le L(L-1),\qquad
L-1\ge\frac{\sqrt{1+4\bar d}-1}{2}.\quad}\tag{3}
\]

*Proof.* In the preceding proof, the tournament induced on \(D_r(v)\) has a vertex beating all \(q-1\) others. Thus \(q-1\le r-2\), so \(q\le r-1\). Summing gives
\[
\bar d/2\le\sum_{r=2}^{L}(r-1)=L(L-1)/2.
\]
Solving this quadratic proves (3). \(\square\)

**Corollary 1 (ordinary reversal-odd boundary tournaments).** Let \(b(a,v,c)\in\{0,1\}\) satisfy \(b(c,v,a)=1-b(a,v,c)\) on distinct triples from an \(n\)-element set. Take \(G=K_n\), \(N=M(K_n)\), and orient the local tournament \(T_v\) by
\[
av\longrightarrow vc\quad\Longleftrightarrow\quad b(a,v,c)=1.
\]
Every independent tournament path is a vertex-simple monochromatic tight path of color one, and conversely. Thus there is such a path on at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{4}
\]
vertices, with integer rounding understood.

*Proof.* Every vertex star of \(K_n\) is a forest, hence independent in its graphic matroid. The condition on \(b\) says precisely that the comparisons at each vertex form a tournament. Along an independent tournament path every triple color is one; ordinary graph paths have independent edge sets in \(M(K_n)\). Apply the theorem with \(\bar d=n-1\). \(\square\)

**Corollary 2 (cube geodesics with at most one switch).** For every binary coloring \(c\) of the edges of \(Q_n\), there exists a coordinate-distinct geodesic of length at least
\[
\boxed{\left\lceil\frac{\sqrt{4n+1}-1}{2}\right\rceil}\tag{5}
\]
whose edge-color word is weakly increasing. In particular it has at most one color change, and this applies to every NORI1 coloring.

*Proof.* On \(E(Q_n)\), let \(N\) be the partition matroid with capacity one in each parallel-coordinate class. Its independent edge sets use each direction at most once, hence contain no graph cycle. At each cube vertex, the \(n\) incident edges use distinct directions, so the whole star is independent. Order each local star with all color-zero edges preceding color-one edges, resolving ties arbitrarily, and let \(T_v\) be the resulting transitive tournament. A path independent in \(N\) uses distinct coordinate directions and is therefore a geodesic. Along every admissible path, the colors are weakly increasing. The chosen local tournaments are transitive, so apply (3) with \(\bar d=n\). \(\square\)

The common mechanism is a rank obstruction to extending a maximum terminal path: a rank-\((r-1)\) flat meets an independent vertex star in at most \(r-1\) edges. In the boundary model, the resource matroid is graphic. In the cube model, it is a coordinate partition matroid subordinate in independence to the graphic matroid of the cube. This supplies one intrinsic matroidal proof of the square-root scale in both models and improves the weaker proper-label cube estimate obtained by separately charging repeated vertices and directions. The passage from a partial low-switch cube geodesic to a full monochromatic antipodal geodesic remains open; (1) alone does not encode antipodal color polarization.
