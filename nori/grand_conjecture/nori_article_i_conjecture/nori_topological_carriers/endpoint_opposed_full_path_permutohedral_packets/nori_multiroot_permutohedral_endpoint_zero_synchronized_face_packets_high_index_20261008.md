# Borsuk–Ulam synchronizes genuine endpoint-opposed full geodesics from any n−2 cube roots into one proper permutation-order face

# Multi-root Borsuk–Ulam synchronization of genuine endpoint-balanced geodesic orders

Fix \(n\ge7\) and let \(d=n-2\). For every physical cube root \(x\in Q_n\), the established permutohedral endpoint imbalance \(q_x(\pi)=w_1(x,\pi)+w_{n-2}(x,\pi)-1\) has a continuous ODD PL extension \(F_x:\partial P_n\cong S^d\to\mathbb R\) under direction-order reversal \(\pi\mapsto\operatorname{rev}\pi\). It changes by at most one on adjacent permutation vertices. The earlier single-root theorem proved that each zero of \(F_x\) lies in a proper permutohedral face containing an ACTUAL endpoint-opposed full \(x\)-rooted geodesic.

**Theorem 1 (simultaneous true-path face synchronization).** Choose ANY \(t\) physical cube roots \(\mathcal X=(x_1,\ldots,x_t)\), not necessarily adjacent, with \(1\le t\le n-2\). Then there is a **single common proper face** \(H\) of the standard permutohedron such that for EVERY \(s=1,\ldots,t\), this SAME face \(H\) contains a permutation vertex \(\pi_s\) with
\[
w_1(x_s,\pi_s)\ne w_{n-2}(x_s,\pi_s).
\tag{1}
\]
The \(\pi_s\) may differ, but every witness is a genuine rooted FULL antipodal cube geodesic, and all their orders belong to one common proper permutohedral face.

**Proof.** Consider the equivariant odd vector map
\[
F_{\mathcal X}=(F_{x_1},\ldots,F_{x_t}):S^{n-2}\to\mathbb R^t.
\]
Since \(t\le n-2\), Borsuk–Ulam supplies \(z\) with \(F_{\mathcal X}(z)=0\). Let \(H\) be its unique minimal proper face of \(P_n\). The single-root face/actual-path lemma applies separately to each coordinate function \(F_{x_s}\) vanishing at the same \(z\), giving an actual vertex \(\pi_s\in H\) with \(q_{x_s}(\pi_s)=0\). All roots are handled by the same face \(H\). \(\square\)

**Theorem 2 (high-index, ROOT-COUPLED path-packet complex).** Let \(Z_{\mathcal X}=F_{\mathcal X}^{-1}(0)\), and define a simplicial complex \(K_{\mathcal X}\):
- A vertex is a \(t\)-tuple of REAL full-path order certificates \(\mathbf\pi=(\pi_1,\ldots,\pi_t)\) with \(q_{x_s}(\pi_s)=0\) for every \(s\), **and** all \(v_{\pi_s}\) lying in some common proper permutohedral face.
- A finite family of packet vertices \(\mathbf\pi^{(1)},\ldots,\mathbf\pi^{(k)}\) spans a simplex if **all** of their permutation vertices across **all roots and all packet vertices** lie in one common proper face.
- The involution sends every coordinate permutation to its complete reversal.

Then \(K_{\mathcal X}\) is a genuine FREE-antipodal finite complex and
\[
\boxed{w_1(K_{\mathcal X}/\tau)^{\,n-2-t}\ne0,}
\tag{2}
\]
where a zeroth power means merely nonemptiness. In particular its \(\mathbb Z_2\)-index is at least \(n-2-t\).

**Proof.** First, the standard vector-valued odd-map zero-carrier index inequality says: for continuous odd \(F:S^d\to\mathbb R^t\) with \(t\le d\) and suitably triangulable zero locus \(Z\), one has \(w_1(Z/\tau)^{d-t}\ne0\). Here is a self-contained relative cohomology proof. Let \(U\) be a sufficiently small invariant regular neighborhood of \(Z\) equivariantly retracting onto it, and \(B\) a closed invariant complement outside a smaller neighborhood, disjoint from all zeros. On \(B\), normalized \(F/\|F\|\) is an equivariant map to \(S^{t-1}\), so \(w^t|_{B/\tau}=0\). If \(w^{d-t}|_{U/\tau}=0\), the corresponding relative classes in degrees \(t\) and \(d-t\) multiply to \(w^d\) in \(H^d(RP^d,(B\cup U)/\tau)=0\), contradicting the nonzero top generator \(w^d\in H^d(RP^d;\mathbb F_2)\). Hence \(w^{d-t}|_{Z/\tau}\ne0\).

For each permitted packet \(\mathbf\pi\), define its **open common-face star**
\[
U_{\mathbf\pi}
=\bigcap_{s=1}^t\operatorname{ostar}_{\partial P_n}(v_{\pi_s}),
\]
where \(\operatorname{ostar}(v)\) is the union of relative interiors of all proper faces containing \(v\). This is an open set of the permutohedral boundary, and the permitted-packet condition makes it nonempty. By Theorem 1's face-local argument, each \(z\in Z_{\mathcal X}\) lies in the star of at least one \(q_{x_s}=0\) permutation for every root \(x_s\), with all those vertices in its common minimal proper face. Hence the sets \(U_{\mathbf\pi}\cap Z_{\mathcal X}\) cover \(Z_{\mathcal X}\). Central inversion sends \(U_{\mathbf\pi}\) to \(U_{\operatorname{rev}\mathbf\pi}\).

An intersection of several such open stars exists iff all their involved path vertices lie in one common proper permutohedral face. Thus their ambient nerve is exactly \(K_{\mathcal X}\); the restricted zero-locus cover nerve is a subcomplex. An antipodally symmetrized partition of unity gives a continuous equivariant nerve map \(Z_{\mathcal X}\to|K_{\mathcal X}|\). No proper permutohedral face contains both \(v_\pi\) and \(v_{\operatorname{rev}\pi}=-v_\pi+2o\), because its convex hull would contain the central interior point \(o\). Therefore no simplex of \(K_{\mathcal X}\) contains a packet along with its opposite packet. Its involution is free, and the equivariant nerve map transfers nonvanishing of \(w^{d-t}=w^{n-2-t}\) from the vector-zero set into \(K_{\mathcal X}\). \(\square\)

**Corollary 3 (synchronized 2D and higher-dimensional physical-root cubes).** Whenever \(2^k\le n-2\), take \(\mathcal X\) to be the \(2^k\) corners of ANY genuine \(k\)-dimensional cube face of the physical root cube \(Q_n\). Then all its roots simultaneously possess actual endpoint-opposed full geodesics whose orders belong to ONE proper face of \(P_n\). The corresponding genuine rooted-path packet nerve has antipodal index at least \(n-2-2^k\). In particular, for **every \(n\ge7\)**, all FOUR roots of EVERY physical square share such a proper permutation-order face. For \(n\ge7\) this four-root carrier has index at least \(n-6\ge1\).

**Precise global-closure limitation.** Root synchronization here occurs in a common PROPER ORDER FACE, **not in one common direction permutation**, and the endpoint colors are only required to be opposite. A high-index path-packet simplex need not have its paths monochromatic, nor satisfy the exact reversed-two-terminal **complementary-support** collision. The arbitrary prescribed-root NORI strengthening is known false, so treating this topology as direct grand closure would be unjustified. This nevertheless supplies a genuinely **root-coupled high-index carrier whose vertices represent ONLY actual full geodesics at each of the selected roots**, rather than virtual zeros or convex mixtures of witness labels. A missing combinatorial extraction theorem could now analyze *adjacent order-exchange compatibility inside common proper faces* across physical root squares, with the topological nonzero index already established.

## Elevation: a shared physical midpoint set, and many genuinely synchronized packets

A facet of the \((n-1)\)-permutohedron is specified by a nonempty proper coordinate subset \(S\subsetneq[n]\): its permutation vertices are exactly the full direction orders whose FIRST \(|S|\) entries are the directions of \(S\) in some order. Every proper permutohedral face \(H\) lies inside at least one such facet.

**Corollary 4 (same prefix-support cut across arbitrarily chosen roots).** For every set \(\mathcal X=\{x_1,\ldots,x_t\}\subseteq Q_n\), \(1\le t\le n-2\), there exist a **single nonempty proper coordinate subset \(S\)** and, for each root \(x_s\), a genuine endpoint-opposed full antipodal geodesic \((x_s,\pi_s)\) such that
\[
\boxed{\{p^{(s)}_1,\ldots,p^{(s)}_{|S|}\}=S\quad\text{for EVERY }s.}
\tag{3}
\]
Thus all these paths traverse exactly the same *set* of initial directions, although their orders within \(S\) and outside \(S\) may differ. Their physical vertices at this shared progress rank are exactly \(x_s\oplus\chi_S\). In particular if the selected roots are the vertices of a physical \(k\)-face, so are these simultaneous intermediate vertices; the root cube has simply been translated by the SAME coordinate subset \(S\).

**Proof.** Apply Theorem 1, obtaining a common proper face \(H\) supporting one actual endpoint-opposed path order \(\pi_s\) for each root. Pick a facet of \(P_n\) containing \(H\), and let \(S\) be its prescribed first-block direction subset. Every \(\pi_s\in H\) lies in this facet and therefore shares its prefix SUPPORT \(S\). The formula for physical intermediate vertices follows from mod-2 coordinate flips. \(\square\)

**Corollary 5 (quantitative root-coupled witness multiplicity).** For \(1\le t\le n-2\), the path-only packet complex \(K_{\mathcal X}\) contains at least
\[
\boxed{2(n-1-t)}
\tag{4}
\]
distinct vertices, each a compatible \(t\)-tuple of genuine endpoint-opposed full geodesics whose orders share a proper permutohedral face. Indeed, if \(K_{\mathcal X}\) has \(N\) antipodal vertex pairs, mapping each pair to \(\pm e_i\in\mathbb R^N\) yields a nonvanishing simplicial equivariant map \(K_{\mathcal X}\to S^{N-1}\) because its simplices contain no antipodal pair. The nonvanishing \((n-2-t)\)-th cover class from Theorem 2 forces \(N>n-2-t\), or \(N\ge n-1-t\). Hence (4).

**Interpretation.** A proper permutohedral face is not an uninterpretable abstract similarity among order words: it guarantees a **common precise prefix-coordinate support**, a concrete intermediate physical cube vertex at every selected root. This gives a root-mobile cut/belt scaffold suitable for a Hex/KKM-style connector argument. The still-missing step is a compatibility theorem controlling **ordered-face colors** along the distinct prefix and suffix orders; common support alone does not imply any monochromatic reachability intersection.


## Root-coupled median-wall Tucker extraction

Let \(m=n-3\), \(r=\lceil m/2\rceil\), and take any \(t\) roots \(x_1,\ldots,x_t\) with
\[
1\le t\le n-2-r=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
On each vertex \((\pi_1,\ldots,\pi_t)\) of the already defined ACTUAL-root-packet complex \(K_{\mathcal X}\), assign the signed MEDIAN SWITCH Tucker label \(\lambda_{x_1}(\pi_1)\in\{\pm1,\ldots,\pm r\}\) defined in Item \`nori_genuine_endpoint_opposed_permutohedral_tucker_complementary_median_switch_pair_20261008\`. Every first-root path has opposite endpoint colors, hence an odd number of switches and a well-defined median. Reversal of all tuple permutations reverses the first median position and, in the central case, the ordered central middle pair; therefore this is an equivariantly ODD signed labeling.

**Corollary 6 (simultaneous real-root Tucker seam collision).** Under the inequality on \(t\), there are TWO distinct vertex packets
\[
\mathbf\pi=(\pi_1,\ldots,\pi_t),\qquad
\mathbf\sigma=(\sigma_1,\ldots,\sigma_t)
\]
in one simplex of \(K_{\mathcal X}\), such that all \(2t\) ACTUAL full rooted geodesic permutation orders belong to ONE proper permutohedral face (thus share one nontrivial prefix-coordinate SUPPORT \(S\)), all \(2t\) full paths have OPPOSITE first/last ordered-face colors at their respective roots, and the first root's two paths have complementary median-switch labels:
\[
\boxed{\lambda_{x_1}(\pi_1)=-\lambda_{x_1}(\sigma_1).}
\tag{5}
\]
In particular, for **every physical root square** and every \(n\ge9\), four roots can be synchronized into such a path packet with a Tucker-complementary pair of median defects at any designated one of its corners.

**Proof.** Theorem 2 gives \(\operatorname{ind}(K_{\mathcal X})\ge n-2-t\ge r\). If no edge had opposite signed median labels, the standard Tucker vertex map \(\pm j\mapsto\pm e_j\in\mathbb R^r\) extends affinely without zeros over every simplex, because no simplex contains both signs of the same basis vector. Normalizing produces an equivariant map \(K_{\mathcal X}\to S^{r-1}\), contradicting its index \(\ge r\). Thus such an edge exists; its two packet vertices have all permutations in a common proper face by definition. The median complement and shared prefix support follow exactly as in the individual-root Tucker proof. \(\square\)

This is a genuinely ROOT-COUPLED Tucker extraction: the complementary median-wall pair at the designated corner comes with legally witnessed endpoint-opposed full geodesics at ALL other selected physical roots, with one shared progress-support cut. It still does not equate ordered-window colors or force a \(\le1\)-switch geodesic; the additional combinatorial step must propagate color/middle-window constraints across the common face and actual root-square edges. The theorem nevertheless supplies both **topological index** and an **honest physical support framework** in the same finite complex.
