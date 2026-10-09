# Endpoint-opposed full-path permutohedral packets

# Endpoint-opposed full-path permutohedral packets

At a fixed root, full cube geodesics correspond to permutations of all coordinate directions. The permutohedron supplies a centrally antipodal sphere of genuine full path orders under reversal. When its vertices carry the first and last actual ordered-three-face colors, an odd endpoint-imbalance map can force opposite endpoint colors in authentic packets of paths.

## An honest high-index carrier made only of actual endpoint-opposed full geodesics

Let \(n\ge7\), fix ANY cube root \(x\), and consider the standard \((n-1)\)-dimensional permutohedron \(P_n\). Its vertices \(v_\pi\) index all full cube geodesics \((x,\pi)\); central inversion sends \(v_\pi\) to \(v_{\operatorname{rev}\pi}\). For each direction permutation \(\pi\), write its actual ordered-three-face word as \(w_1(x,\pi),\ldots,w_{n-2}(x,\pi)\), and define
\[
q_x(\pi)=w_1(x,\pi)+w_{n-2}(x,\pi)-1\in\{-1,0,1\}.
\tag{1}
\]
The existing permutohedral theorem proves \(q_x(\operatorname{rev}\pi)=-q_x(\pi)\) and \(|q_x(\pi)-q_x(\pi')|\le1\) on each permutohedral 1-skeleton edge (an adjacent transposition), because the first and last triple windows cannot both be affected when \(n\ge7\).

Let \(F_x:\partial P_n\to\mathbb R\) be the odd PL function obtained by assigning at every face barycenter the arithmetic mean of \(q_x\) on that face's permutation vertices and extending linearly on its barycentric subdivision. Let \(Z_x=F_x^{-1}(0)\). By the previously proved odd-map zero-carrier index theorem, the free antipodal quotient satisfies
\[
w_1(Z_x/\tau)^{n-3}\ne0.
\tag{2}
\]

Define the set \(\mathcal B_x=\{\pi:q_x(\pi)=0\}\), consisting of **ACTUAL FULL ANTIPODAL GEODESICS whose first and last ordered-face colors are opposite**. Define a finite abstract simplicial complex \(K_x\) with vertex set \(\mathcal B_x\) by declaring \(\sigma=\{\pi_0,\ldots,\pi_k\}\) a simplex if the corresponding permutation vertices \(v_{\pi_i}\) all lie in **some common proper face** of the permutohedron. The involution \(\pi\mapsto\operatorname{rev}\pi\) is simplicial on \(K_x\).

**Theorem 1 (every interpolated zero has a true path in its carrier face).** If \(z\in Z_x\) and \(H\) is the unique minimal permutohedral face whose relative interior contains \(z\), then \(H\) contains at least one vertex \(v_\pi\) with \(q_x(\pi)=0\).

**Proof.** Suppose no original permutation vertex of \(H\) has \(q=0\). Its 1-skeleton is connected (as the graph of a convex polytope), and adjacent vertices cannot have opposite \(q\) signs because \(q\in\{\pm1\}\) on all vertices of \(H\) and the edge difference is at most one. Consequently EVERY vertex of \(H\) has the SAME sign \(s\in\{\pm1\}\). Every nonempty subface of \(H\) has only vertices of this sign, so all their barycentric means equal \(s\). The barycentric PL extension therefore satisfies \(F_x\equiv s\) on the entire face \(H\), contradicting \(z\in Z_x\). \(\square\)

**Theorem 2 (path-only high-index nerve).** The genuine-geodesic complex \(K_x\) is a FREE antipodal simplicial complex and
\[
\boxed{w_1(K_x/\tau)^{n-3}\ne0.}
\tag{3}
\]
Thus \(\operatorname{ind}_{\mathbb Z_2}(K_x)\ge n-3\), with no interpolated points serving as vertices or fictitious full geodesics.

**Proof.** For every \(v_\pi\) with \(\pi\in\mathcal B_x\), let \(U_\pi\subseteq\partial P_n\) be its *open polyhedral star*: the union of relative interiors of all nonempty proper faces containing \(v_\pi\). These are open in the boundary face-complex topology: a point in a face's relative interior has a neighborhood only among that face and its cofaces. By Theorem 1, the open sets \(U_\pi\cap Z_x\) cover \(Z_x\). They are interchanged by the central antipodal involution, since \(U_{\operatorname{rev}\pi}=-U_\pi\).

A family of such open stars intersects if and only if all their vertices belong to some common proper face \(H\) (a point of the intersection lies in the relative interior of a face containing all the vertices; conversely the relative interior of \(H\) lies in all these stars). Hence the **nerve of the ambient open-star cover** is exactly \(K_x\). The nerve of the restricted cover of \(Z_x\) is a subcomplex of \(K_x\).

Choose a continuous partition of unity subordinate to the finite open cover of compact \(Z_x\). Average it under the antipodal involution to make the weights satisfy \(\lambda_{\operatorname{rev}\pi}(-z)=\lambda_\pi(z)\). The standard nerve map
\[
f:Z_x\longrightarrow |K_x|,\qquad
f(z)=\sum_{\pi\in\mathcal B_x}\lambda_\pi(z)e_\pi
\]
is continuous and antipodally equivariant. No proper face of a centrally symmetric polytope contains both a vertex \(v\) and its opposite \(-v\): otherwise its convexity would include the polytope center, which lies in the interior. Thus NO simplex of \(K_x\) contains both \(\pi\) and \(\operatorname{rev}\pi\). This makes the geometric simplicial involution on \(K_x\) free.

An equivariant map between free involution spaces pulls the antipodal quotient double-cover class back to that of the source. Therefore nonvanishing of \(w_1(Z_x/\tau)^{n-3}\) from (2) implies nonvanishing of \(w_1(K_x/\tau)^{n-3}\), proving (3). \(\square\)

**Corollary 3 (improved number of ACTUAL endpoint-opposed full geodesics at EVERY root).** For any active NORI coloring and every root \(x\) in \(Q_n\), \(n\ge7\),
\[
\boxed{\#\mathcal B_x\ge 2(n-2).}
\tag{4}
\]
These are \(2(n-2)\) DISTINCT physical rooted full geodesics with opposite first/last ordered-face window colors. In a hypothetical grand counterexample, every one of these has at least three color changes.

**Proof.** The free involution on the finite vertex set of \(K_x\) partitions it into \(N=\#\mathcal B_x/2\) pairs \(\{\pi_i,\operatorname{rev}\pi_i\}\). Assign its paired vertices the vectors \(\pm e_i\) in \(\mathbb R^N\). No simplex contains both members of a pair, so on any simplex the PL extension of these signed-coordinate vertices has at most one signed unit vector in each coordinate: its convex combination is never zero. Normalize to give a continuous antipodally equivariant map \(K_x\to S^{N-1}\). Thus \(w_1(K_x/\tau)^N=0\). Theorem 2 gives its \((n-3)\)-rd power nonzero, forcing \(N>n-3\), or \(N\ge n-2\). Hence (4). \(\square\)

**The exact higher-dimensional extraction obligation.** The crucial improvement is that the topological carrier's vertices are **real endpoint-opposed full paths**, and its simplices mean those paths' coordinate orders lie in one common **proper face of the true permutohedron**, not convex hulls of imaginary geodesics. Under hypothetical grand failure every such vertex has an ODD number of changes \(\ge3\). If one can construct from this genuine order-face incidence a simplicial antipodal map \(K_x\to S^{n-4}\) using the internal switch positions, it will contradict (3) and force NORI closure. For a valid map, a cell's assigned labels must avoid zero in every simplex, with the actual face/order incidence checked. Counting switch positions alone is not an extension theorem. Fixed-root NORI strengthening is false, so a uniformly valid low-sphere map cannot arise merely from no-good paths at one fixed root without using actual cross-root face constraints (or else it would contradict known rooted counterexamples). The theorem isolates the high-index **physical path complex**, without claiming that its topology alone settles grand closure.

**Status:** Theorem 1–2 and Corollary 3 are all-dimensional proved consequences of the established 1-Lipschitz endpoint imbalance and odd PL zero-index theorem. They require neither affine-exterior dependence nor a low-dimensional classification.

## Multi-root Borsuk–Ulam synchronization of genuine endpoint-balanced geodesic orders

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


THEOREM A (EXACT PHYSICAL-SQUARE OVERLAP UNDER ONE COORDINATE TRANSPOSITION). Let n>=5 and fix ANY physical cube root x and two full geodesic direction permutations p,p' differing by ONE adjacent transposition (swap positions s,s+1). For any j,k in {1,...,n-3} with |j-k|<=1, consider the genuine four-edge subpaths of P(x,p) starting at directed edge position j and of P(x,p') starting at position k. Each four-edge subpath determines its true MIDDLE physical cube square, free in its second and third directions (its center is the vertex after two of those four steps). Then the two physical middle squares ALWAYS have a COMMON PHYSICAL CUBE EDGE: their vertex sets intersect in at least two adjacent cube vertices. In particular, if both subpaths are monochromatic in DIFFERENT ordered-three-face colors, that common physical edge belongs to TWO actual opposite-color certified middle squares, so alternative A of the active NORI edge-shadow dichotomy is witnessed without any further matching.
PROOF. This is a uniform cubical commutation identity, independent of face colors. By translation/relabeling assume x=0 and p=(1,...,n). For j, let v_{j+1}=e_1+...+e_{j+1}; its middle square is v_{j+1}+span{e_{j+1},e_{j+2}} (1-based j). The adjacent-swapped path differs from the original only along the little commuting square in coordinates p_s,p_(s+1), and its physical vertices AGREE with the old path before index s-1 and after index s+1. Compare the two four-window middle squares at equal or adjacent indices. If the swap is outside their combined 5-edge support, these are the same or consecutive middle squares of one path, which share the intermediate physical edge. If the swap occurs in that support, direct inspection of the relative placements s∈{j-1,j,j+1,j+2,j+3} (and the mirror cases for k=j-1) gives two common vertices differing by one coordinate: the common edge is either the unchanged middle edge or one side of the swapped commuting square. Thus every allowed relative position intersects in a whole edge. This proof is purely a finite local cube identity, not an exhaustive-coloring claim.
THEOREM B (Q7 BAD BALANCED PERMUTATION-GAP BRIDGE). Assume n=7 and active NORI. For a full geodesic P with opposite first/last ordered-three-face window colors, suppose P has at least two switches. Its 5-symbol color word has ODD switch number, hence (under the hypothesis that no good <=1-switch full geodesic exists) EXACTLY THREE switches. There is exactly one equal-color adjacent window pair at seam index j∈{1,2,3,4}, certifying a genuine monochromatic four-edge subpath at starting edge position j. If the first window color is α, the monochromatic pair color is α for ODD j=1,3 and 1−α for EVEN j=2,4.
Now take two such endpoint-balanced BAD geodesics from the same root whose direction permutations differ by one adjacent swap. The first/last endpoint colors of the two paths must be IDENTICAL: an adjacent swap affects at most one endpoint window for n>=7, whereas opposite endpoints would require both endpoint colors to flip simultaneously. Thus their first bits share α. If their unique monochromatic four-window pairs have OPPOSITE colors, their gap indices j,k have opposite parity, so |j-k| is either1 or3. If |j-k|=1, Theorem A forces a COMMON PHYSICAL CUBE EDGE with both color certificates. If |j-k|=3, necessarily {j,k}={1,4}. A direct comparison of the unaffected extreme windows shows this is possible ONLY if the adjacent transposition swaps positions (3,4) or (4,5) of the seven direction list: swaps elsewhere leave either the original second or fourth window physically unchanged, conflicting with the requested first-gap/last-gap three-switch patterns. For either of those two central swaps, the two four-window middle squares have DISJOINT vertex sets; this exceptional physical gap is genuine and is realized by the previously persisted exact local ordered-face color assignment nori_permutohedral_balanced_three_wall_left_right_label_local_jump_20261008 (with j=1,k=4).
CONTRAPOSITIVE TARGET. In a genuine NORI coloring with NO physical edge doubly certified by opposite-color monochromatic four-geodesics, an adjacent permutohedron edge joining two BAD endpoint-balanced geodesics can change the color of their unique four-window monochromatic witness ONLY by the exceptional first-gap-to-last-gap long jump across a CENTRAL adjacent transposition. This sharply constrains any proposed equivariant sign-map discontinuity on the high-index permutohedral endpoint-balanced carrier. The remaining global task is to rule out or topologically absorb these central long jumps; the lemma alone does not prove one-switch closure.

The forced packet is a family of actual rooted geodesics, which is stronger than a formal label collision. Nevertheless, opposite endpoint colors need not determine the intermediate switch count, nor do they automatically certify a legal physical splice.
