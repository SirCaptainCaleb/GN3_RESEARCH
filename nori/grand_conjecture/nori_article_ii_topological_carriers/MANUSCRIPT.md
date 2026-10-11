# Article II - Equivariant topology

## Article setting and orientation

The main positive content is a collection of exact equivariant structures built from actual ordered physical geodesics: endpoint-opposed permutohedral packets, balanced root and central-face witness constructions, two-sided Helly-type selection, and physical window and seam-square transport. A topological coincidence and a full monochromatic path are not the same assertion. The surviving Subsections make the known correspondence precise only under their stated witness hypotheses.

Independent attempts to infer a good path from scalar Tucker labels, static nerves, ordered-segment forgetful maps, fixed balanced root-order prisms or root-slide selectors are fully documented as research notes. Those obstructions are mathematically rigorous but chiefly describe what selected extraction methods cannot establish, so they no longer occupy separate Subsection publication units.

*Full Article composition: [source manuscript](../nori_article_ii_topological_carriers.md).*

## Root-coupled topology and physical good-window carriers

Antipodal topology gives strong information about authentic cube geodesics when the underlying simplicial and permutohedral complexes are constructed from the actual root, ordered support and terminal data. The remaining Subsections establish endpoint-opposed full-path packets, canonical high-index permutohedral spheres, balanced-root packets, and two-sided Helly-type selection principles. Their statements distinguish the existence of topological coincidences from actual one-switch color extraction.

A topological zero need not itself be a single physical good geodesic. Method-specific failures of scalar Tucker labels, consecutive-segment carrier collapses, static witness nerves, and balanced root-order prisms have been editorially moved to the linked research note with their full rigorous calculations. Those results inform the hypotheses of future extraction lemmas; they are not separate manuscript achievements. Remaining manuscripts focus on the positive structural and equivariant facts. Any attempted application to NORI1 or boundary tournaments must still prove a genuine common-witness conclusion rather than mere pairwise label agreement.

*Full Section composition: [source manuscript](nori_topological_carriers.md).*

### Endpoint-opposed full-path permutohedral packets

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

### Balanced-root permutohedral packets and Tucker coincidences

# Balanced-root permutohedral packets and Tucker coincidences

At a given root, reversing a full direction order is central antipodality of the permutohedron. Actual first/last color functions and position coordinates become odd labels, so the full sphere forces balanced packets of genuine geodesics. Tucker coincidences locate two path witnesses within this parameter space, but the witnesses may still have different physical middle windows.

## A canonical HIGH-INDEX permutohedral sphere for EVERY physical root: topological endpoint-opposition forcing in NORI

Fix n>=7 and a binary active NORI coloring of ordered physical 3-faces satisfying
  c(bar F,rev(i,j,k)) = 1-c(F,(i,j,k)).
Fix ANY cube root x∈Q_n. Every full n-edge cube geodesic from x is specified by a coordinate permutation pi=(p1,...,pn). Its L=n−2 consecutive actual ordered-three-face window colors are
  w_j(x,pi)∈{0,1}, j=1,...,L.
Let alpha(pi)=w_1(x,pi), beta(pi)=w_L(x,pi), and define the integral ENDPOINT IMBALANCE
  q_x(pi)=alpha(pi)+beta(pi)−1 ∈ {−1,0,+1}.
Thus q=0 iff the FIRST and LAST physical ordered-three-face colors are OPPOSITE.

**THEOREM 1 (literal NORI antipodality on the permutohedron).** Let P_n be the STANDARD (n−1)-dimensional permutohedron in the affine hyperplane sum_i t_i=n(n+1)/2, whose vertex indexed by pi has coordinates
  v_pi(i)=position of direction i in pi.
Its center is o=((n+1)/2,...,(n+1)/2), and reversing a permutation gives
  v_(rev pi)=2o−v_pi.
Therefore ∂P_n is an (n−2)-sphere with a FREE CENTRAL-ANTIPODAL action pi↦rev pi on its vertices.

For a FULL antipodal geodesic from root x, physical complement followed by path reversal has starting root
  bar(x xor [n])=x.
Its direction order is rev pi, and by ACTIVE NORI oddness the COMPLETE color word becomes complemented-reversed:
  w_j(x,rev pi)=1−w_(L+1−j)(x,pi).
Consequently
  q_x(rev pi)=−q_x(pi).
This uses actual physical ordered faces and does not assume a fictitious complement action on direction supports.

**THEOREM 2 (discrete endpoint-balance lemma: every root has a REAL opposite-end path).** For n>=7, an edge of the 1-skeleton of P_n corresponds to swapping two ADJACENT POSITIONS in the direction permutation. Such a swap changes AT MOST ONE of alpha(pi),beta(pi):
- the first physical three-face depends on the first three ordered directions (and on root x);
- the last physical three-face depends on the final three ordered directions and the SET of previously flipped directions;
- when n>=7 these first and last three-position blocks have at least one position separating them, and swapping adjacent entries cannot alter both physical faces simultaneously.
Hence for adjacent permutohedron vertices,
  |q_x(pi)−q_x(pi')|<=1.
The graph of P_n is connected. Starting at any pi with q≠0 and following an adjacent-transposition path to rev pi, whose q-value is −q, the integer-valued 1-Lipschitz q must pass through zero at some VERTEX. If q(pi)=0 already, stop. Therefore for EVERY starting root x there exists an ACTUAL full antipodal cube geodesic with opposite first and last ordered-three-face window colors.

Under hypothetical grand failure, every such actual endpoint-opposed full geodesic necessarily has at least THREE window-color changes, because its number of changes is ODD and at most one is prohibited. This provides a physically witnessed, antipodally invariant 'middle defect' on every root's full permutation space.

**THEOREM 3 (canonical HIGH INDEX endpoint-opposition zero carrier).** Define an odd piecewise-linear function F_x:∂P_n→R as follows. Use the barycentric subdivision of the proper nonempty face poset of P_n. At the barycenter b_H of a face H, set F_x(b_H) to the arithmetic MEAN of q_x(pi) over all ORIGINAL permutation vertices v_pi of H, and extend affinely over each barycentric simplex. Central inversion sends H→−H and q→−q, so
  F_x(−z)=−F_x(z).
At the original vertices F_x(v_pi)=q_x(pi).

Let Z_x=F_x^{-1}(0), the literal PL ZERO SET. It is closed, antipodally invariant, and admits a finite antipodally symmetric triangulation as a subpolyhedron. Let w be the first Stiefel–Whitney class of its free antipodal quotient double cover. Then
  w^(n−3) !=0 in H^(n−3)(Z_x/(±1);F2).
Equivalently, the cohomological Z2 index of the endpoint-opposition carrier Z_x is AT LEAST n−3, one dimension below the full permutohedron boundary's index n−2.

**Proof of index bound (relative cup-product form of Borsuk–Ulam).** More generally let S^d carry the antipodal action and let F:S^d→R be any continuous ODD map with zero locus Z. Suppose w^(d−1) vanished on Z/(±1). For our PL Z choose a sufficiently small invariant regular neighborhood U retracting equivariantly onto Z; then w^(d−1) vanishes on U/(±1). Choose a smaller invariant neighborhood U0 whose closure lies in U, and set B=S^d\U0, a closed invariant complement avoiding zeros. On B the SIGN of F defines an equivariant map to S^0, hence the double cover over B is trivial and w|B=0. In the quotient X=RP^d, the vanishing classes lift to relative classes in
  H^(d−1)(X,U/(±1)) and H^1(X,B/(±1)).
Their relative cup product represents w^d in H^d(X,(U∪B)/(±1))=H^d(X,X)=0. But w^d is the NONZERO top generator of H^d(RP^d;F2), contradiction. Therefore w^(d−1)|Z is nonzero. Apply d=n−2. QED.

**COROLLARY 4 (an EXACT topological grand-closure target).** Since ind(Z_x)>=n−3, there is NO antipodally equivariant continuous map Z_x→S^(n−4). Thus a TOPLOGICAL proof of GRAND NORI closure would follow if, under the hypothetical assumption that EVERY full geodesic has at least two changes, one constructs an honest antipodally equivariant LOW-SPHERE MAP
  Phi_x:Z_x→S^(n−4)
from the ordered-face change pattern, with all cellwise extensions justified by physical face/coordinate-swap combinatorics. Such a map would contradict Theorem3.

Concretely, at ACTUAL endpoint-opposed permutation vertices q_x(pi)=0, the color-change vector
  s_j(pi)=w_j(x,pi) xor w_(j+1)(x,pi), j=1,...,n−3,
has ODD Hamming weight, and in a hypothetical counterexample at least THREE 1s. Physical reversal sends this change vector to its position reversal, while keeping the root x fixed. The missing extraction step is to turn this equivariant MULTI-SWITCH LABELING into a continuous sphere map on ALL of Z_x (or a combinatorial Tucker complementary-edge certificate whose physical local repair yields a good path). Merely assigning switch labels at permutation vertices does NOT automatically define such a map on higher-dimensional faces; proving the extension is the essential combinatorial obligation INSIDE the high-index topological frame.



*The exact scoped proof is preserved in research note* note_nori_carrier_requires_joint_actual_geodesic_witnesses.

## Quantitative actual-path separator: at least n−1 endpoint-opposed full permutations per root

**THEOREM 5.** For every n>=7 and EVERY fixed physical cube root x, at least n−1 DISTINCT full antipodal ordered-direction geodesics rooted at x have opposite initial and final ordered-three-face window colors.

**Proof.** Let V_+, V_0, V_- partition the vertex set of the standard (n−1)-dimensional permutohedron P_n according to q_x(pi)=+1,0,−1. Reversal of direction order interchanges V_+ and V_- and preserves V_0. If V_+ is empty, then V_- is also empty, so ALL n! permutation vertices are in V_0 and the assertion is immediate. Otherwise both V_+ and V_- are nonempty. The proved 1-Lipschitz adjacent-swap property of q says there is NO permutohedron GRAPH EDGE directly between V_+ and V_-. Thus deleting V_0 disconnects the 1-skeleton of P_n into at least the two nonempty groups V_+, V_-. Balinski's elementary d-vertex-connectivity theorem for convex d-polytopes says the graph of P_n has vertex connectivity at least d=n−1. Hence |V_0|>=n−1. Every vertex in V_0 is one genuine full rooted cube geodesic with physically opposite endpoint colors. QED.

**Topology inside combinatorics.** The count is a direct finite shadow of the high-index endpoint-zero hypersurface: the genuine zero-LABELED vertices, not merely virtual PL zeros, form an antipodally invariant vertex separator in an (n−1)-connected polytopal graph. This strengthens the nonempty actual balanced-path theorem and quantifies a minimum amount of certified endpoint diversity at EACH root.

This theorem uses the classical convex-polytope graph connectivity result. It does not assert that any of these >=n−1 paths has only one change; under hypothetical grand failure each has at least THREE, an odd number. For a universal grand proof the endpoint-balanced high-index hypersurface must additionally force a defect-removal transition among its actual adjacent-swap witnesses.


## A genuine Tucker connector: odd-dimensional NORI forces two endpoint-opposed full geodesics to meet and have opposite mirror-switch asymmetry

Let n>=7 be ODD, and let c be ANY active NORI coloring of PHYSICAL ORDERED three-faces satisfying c(bar F,rev pi)=1−c(F,pi). Fix ANY physical cube root x. For each full n-direction permutation p, let w(x,p)=(w_1,...,w_{n-2}) be the ACTUAL ordered-face color word and let D=n−3 be its number of switch positions. Because n is odd, D is EVEN. Let
\[
s_j(p)=w_j\oplus w_{j+1},\quad j=1,...,D.
\]
Call p ENDPOINT-OPPOSED if \(w_1\ne w_{n-2}\), equivalently its switch word has ODD Hamming weight.

For each endpoint-opposed p, define its CANONICAL MIRROR-SWITCH SIGNED LABEL:
\[
j(p)=\min\{1\le j\le D/2:s_j(p)\ne s_{D+1-j}(p)\},
\]
\[
\lambda(p)=
\begin{cases}
+j(p),&s_{j(p)}(p)=1,\\
-j(p),&s_{j(p)}(p)=0.
\end{cases}
\]
The label is well-defined: if all D/2 mirror pairs had matching bits, the total switch count would be EVEN, contradicting endpoint opposition. Under the actual full-geodesic NORI antipodal-reversal operation p→rev p at THE SAME root x, the entire window word transforms as \(w(rev p)=1-\operatorname{rev}w(p)\); hence the switch vector transforms as \(s(rev p)=\operatorname{rev}s(p)\), and
\[
\lambda(\operatorname{rev}p)=-\lambda(p).
\]
This is a genuine \(\mathbb Z_2\)-odd vertex labeling on all ACTUAL endpoint-opposed geodesics, with only k=D/2=(n−3)/2 coordinate labels.

**THEOREM (physical root-compatible mirror-switch Tucker pair).** For EVERY odd n>=7 and EVERY root x, there exist TWO ACTUAL full antipodal directed geodesics \(P=(x,p)\) and \(Q=(x,q)\), both endpoint-opposed, such that:
1. Their signed mirror-switch labels are COMPLEMENTARY, \(\lambda(p)=+j\), \(\lambda(q)=-j\), for some \(1\le j\le(n−3)/2\). Thus
\[
s_j(p)=1,\quad s_{n-2-j}(p)=0,\qquad
s_j(q)=0,\quad s_{n-2-j}(q)=1,
\]
where the reflected position is D+1−j=n−2−j.
2. Their direction permutations share SOME proper nonempty INITIAL COORDINATE SUPPORT:
\[
\{p_1,...,p_\ell\}=\{q_1,...,q_\ell\}
\quad\text{for some }1\le\ell\le n−1.
\]
In particular P and Q pass through the SAME genuine physical cube vertex \(y=x\oplus\{p_1,...,p_\ell\}\) at time \ell, as well as their common antipodal endpoints x and bar x.
3. The permutations q and rev p are necessarily DIFFERENT: the pair is not merely the tautological antipodal-reversed copy of one geodesic.

**PROOF.** Let P_n be the standard centered (n−1)-dimensional permutohedron whose original vertices are full direction orders, with antipodal involution p→rev p. Its boundary is a free-antipodal sphere S^(n−2). Use the genuine integer-valued endpoint imbalance \(f(v_p)=w_1(x,p)+w_{n−2}(x,p)-1\in\{-1,0,+1\}\). The NORI antipodal-reversal law makes f ODD; it is 1-Lipschitz on ACTUAL adjacent-transposition edges of the permutohedron, since swapping adjacent positions changes at most one of the first and final ordered three-face colors when n>=7. Let F be the equivariant barycentric piecewise-linear extension averaging f over original vertices of each face and interpolating over flags of faces, and put Z=F^(-1)(0).

The previously proved endpoint-zero index theorem, Item nori_permutohedral_antipodal_sphere_endpoint_color_balance_high_index_20261008, gives
\[
w_1(Z/\tau)^{n−3}\ne0,
\]
so no equivariant continuous map Z→S^(k−1) exists for k=(n−3)/2.

We now construct a GENUINELY CARRIED simplicial labeling of Z. Every point z∈Z lies in a unique relative interior of a PROPER permutohedron face H(z). This face H(z) has an ACTUAL endpoint-opposed original permutation vertex. Indeed, if H(z) had no f=0 original vertex, its connected original 1-skeleton (true for any convex-polytope face) together with the 1-Lipschitz property of f would force f to be CONSTANT +1 or CONSTANT −1 on all vertices of H(z). The barycentric extension F would then be identically that sign on H(z), contradicting F(z)=0.

Choose a finite centrally equivariant triangulation of the PL zero complex Z that refines the barycentric triangulation of ∂P_n. For each triangulation vertex z, choose an actual f=0 permutation p_z contained in the minimal P_n-face H(z). Choose the permutations in antipodal pairs so \(p_{\tau z}=\operatorname{rev}p_z\); this is consistent because proper permutohedron faces come in DISJOINT antipodal pairs, and the involution is free. Assign the signed label \lambda(p_z)∈{±1,...,±k} to z. The labels are genuinely antipodally ODD.

Suppose for contradiction that NO edge of this zero-set triangulation has opposite labels +j and -j. Then every simplex's vertex-label set contains no complementary pair (every pair of simplex vertices is an edge). Map each labeled vertex +j to the standard basis vector e_j∈R^k and -j to -e_j; interpolate linearly on simplices. Since a simplex contains no complementary pair, its positive barycentric combinations of signed basis vectors CANNOT vanish: for each coordinate index the appearing signs are either all + or all −, and at least one nonzero coordinate appears. Normalize to obtain a continuous τ-equivariant map Z→S^(k−1), contradicting the high antipodal index of Z. Therefore some genuine ZERO-SET SIMPLEX EDGE zz' has complementary labels ±j.

Because the triangulation refines the barycentric face-flag triangulation of ∂P_n, the two z,z' lie in a common flag simplex and therefore in a common PROPER polytope face H. Their selected actual f=0 permutations p_z,p_z' lie in the respective minimal faces H(z),H(z')⊆H, hence both lie in H. Every proper permutohedron face is contained in some proper FACET. A facet of the standard permutohedron is given by a nonempty proper subset S of coordinates occupying the first |S| positions of the order (or by its complementary last-block equivalent). Thus any two original vertices p,q in that facet share an exact proper prefix used-coordinate SUPPORT S. Their full geodesics from root x therefore meet at x⊕S. Moreover a proper convex face cannot contain both centrally antipodal original vertices p and rev p: their midpoint is the CENTER of P_n, an interior point. So q≠rev p. Finally their switch labels ±j give the displayed physically verified opposite reflected switch bits. QED.

**INTERPRETATION.** This is a DIMENSION-INDEPENDENT GENUINE TOPOLOGICAL FORCING THEOREM, NOT a virtual barycentric zero only: high index and Tucker's no-complement obstruction force TWO HONEST full physical geodesic witnesses at the SAME ROOT, with a common intermediate cube vertex and opposed mirror-switch patterns. The proof uses physical face locality, active NORI oddness, and the actual permutohedron face incidence. It does NOT YET force either geodesic to have <=1 switch; the remaining combinatorial obligation is to leverage the common-prefix-support connector and opposite mirror-switch orientations to exchange segments or slides while preserving a full geodesic and strictly reducing defects.

**OPEN NEXT STEP.** Strengthen this Tucker pair to a *compatible local exchange*: either force q to be obtained from p by one adjacent transposition with controlled two-window effects, or force a common intermediate vertex at a switch boundary with monochromaticly compatible ordered-two-direction tails, thereby connecting directly to the exact reversed-tail support-overlap NORI closure theorem. No such strengthening is claimed in this item.

## An exact antipodal-root switch-coboundary identity for physical ordered faces

Let \(n\ge5\) and \(c\) be any active NORI coloring of PHYSICAL ordered three-faces, satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
Fix ANY full direction order \(p=(p_1,\ldots,p_n)\) and ANY physical root \(x\). Let \(L=n-2\), and let \(F_j=F_j(x,p)\) be the actual physical three-face at the jth window, with ordered free direction triple \(t_j=(p_j,p_{j+1},p_{j+2})\). Define the same-face **local triple-reversal asymmetry bit**
\[
r_j(x,p)=c(F_j,t_j)\oplus c(F_j,\operatorname{rev}t_j)\in\mathbb F_2.
\tag{1}
\]
Unlike reversal-oddness across *antipodal physical faces*, this is a comparison of two orders ON THE SAME physical face, and may be 0 or 1 independently as the coloring varies.

**Theorem (exact antipodal-root discrete gauge/coboundary identity).** Write the actual ordered-face word \(w_j(x,p)=c(F_j,t_j)\) and switch bits \(s_j(x,p)=w_j(x,p)\oplus w_{j+1}(x,p)\), \(1\le j\le L-1=n-3\). At the ANTIPODAL root \(\bar x=x\oplus[n]\), with the SAME direction order \(p\), one has:
\[
\boxed{w_j(\bar x,p)=1\oplus w_j(x,p)\oplus r_j(x,p),}
\tag{2}
\]
\[
\boxed{s_j(\bar x,p)=s_j(x,p)\oplus r_j(x,p)\oplus r_{j+1}(x,p).}
\tag{3}
\]
Thus the two full switch vectors differ by the \(\mathbb F_2\) discrete coboundary \(\delta r\) of the actual local order-reversal asymmetry 0-cochain along the window-index path:
\[
\boxed{s(\bar x,p)\oplus s(x,p)=\delta r.}
\tag{4}
\]
The reversal-asymmetry word is itself antipodally ROOT-INVARIANT and full-order-reversal covariant:
\[
r_j(\bar x,p)=r_j(x,p),\qquad
r_j(x,\operatorname{rev}p)=r_{L+1-j}(x,p).
\tag{5}
\]
The endpoints of \(r\) agree if and only if the two antipodal-root paths have the SAME switch-count parity:
\[
\bigoplus_{j=1}^{L-1}s_j(\bar x,p)
=\bigoplus_{j=1}^{L-1}s_j(x,p)
\quad\Longleftrightarrow\quad r_1=r_L.
\tag{6}
\]

**Proof.** At the same progress rank, the rooted path from \(\bar x\) has the SAME window free directions and all exterior fixed bits complemented, so its physical window face is literally \(\bar F_j\). The active axiom applied with reversed free order gives
\[
c(\bar F_j,t_j)=1\oplus c(F_j,\operatorname{rev}t_j)
=1\oplus w_j(x,p)\oplus r_j(x,p),
\]
which is (2). XOR consecutive window identities: the two constant 1s cancel, giving (3)-(4). Applying the same argument to the reversed order on \(\bar F_j\) shows
\[
r(\bar F_j,t_j)=c(\bar F_j,t_j)\oplus c(\bar F_j,\operatorname{rev}t_j)
=r(F_j,t_j),
\]
so \(r_j(\bar x,p)=r_j(x,p)\). The actual full-path antipodal reversal at the FIXED root \(x\) sends \(p\mapsto\operatorname{rev}p\) and transforms the physical color word to the reversed complement. Its corresponding reversal-asymmetry comparison therefore gives the reversed \(r\)-word, proving the second identity in (5). Finally XOR (3) across all \(j\); the interior \(r\) terms cancel in pairs, yielding (6). \(\square\)

**Corollary (antipodally synchronized endpoint-balanced paths have a closed reversal gauge).** For a full permutation \(p\) that is endpoint-opposed at BOTH \(x\) and \(\bar x\), the two switch vectors have odd parity, hence
\[
\boxed{r_1(x,p)=r_L(x,p).}
\tag{7}
\]
The synchronized full-path corridors from Item \`nori_same_order_antipodal_root_pairs_endpoint_opposition_disjoint_triple_orbits_20261008\` therefore provide, at every prescribed antipodal root pair in \(n\ge10\), an entire \((n-6)!\)-packet of actual full paths with a CLOSED reversal-asymmetry cochain (identical first/last gauge bits), while their internal switch vectors differ by its exact derivative. Moreover the endpoint-closed condition is EXACTLY the two-root equality of reversal-orbit signatures used in that theorem.

**Why this is mathematically useful.** Earlier permutohedral Tucker labels track internal switch positions but do not control how switches change when ROOT is antipodally complemented. Formula (3) supplies that missing PHYSICAL comparison without inventing an abstract sign-vector action: at any fixed complete order, the antipodal root transfer is a gauge transformation by a same-face reversal asymmetry word. It is compatible with order-reversal and is an actual 1-dimensional chain-complex coboundary identity. It suggests constructing a two-parameter root/order carrier with the switch-change 1-cochain and its cross-root gauge \(r\), then deriving a nontrivial holonomy obstruction when certified cells are glued around root-cube and permutohedral exchange cycles.



*The scope-specific limitation and complete proof are preserved in linked research note note_nori_carrier_requires_joint_actual_geodesic_witnesses.*

### Two-sided Helly root sheets and high-index support selection

# Two-sided Helly root sheets and high-index support selection

A two-sided monochromatic path has an initial root sheet, a terminal sheet and ordered overlap memory. When all admissible path witnesses sharing a physical root are assembled into a nerve, a Helly property may hold for the literal root sheets while failing for the compatibility needed to splice two different paths. This section isolates the corresponding dimension and index phenomena.

## Macroscopic-cut Tucker theorem: genuine endpoint-opposed NORI geodesics meet at a central-rank physical vertex

Let n>=7 and let c be ANY active NORI binary coloring of genuine PHYSICAL ORDERED three-faces on Q_n, with c(bar F,rev pi)=1-c(F,pi). Fix ANY cube root x.

Let K_x be the genuine endpoint-opposed permutohedral face nerve of Item nori_permutohedron_actual_opposite_endpoint_geodesic_star_nerve_high_index_20261008. Its vertices are ACTUAL full rooted geodesics (x,pi) with opposite first/last three-face window colors, and a simplex means that its order-permutation vertices all lie in a common proper face of the (n−1)-dimensional standard permutohedron P_n. Its reversal involution is free, and the established theorem gives
 w^(n−3) != 0 in H^(n−3)(|K_x|/tau;F2).

For each actual endpoint-opposed full geodesic pi, let m=n−3 be the number of internal switch positions and let j_*(pi) denote the MEDIAN of its ODD set of switch positions. Give pi the signed MEDIAN-TUCKER label lambda(pi)∈{±1,...,±r}, r=ceil((n−3)/2), as defined in proved Item nori_genuine_endpoint_opposed_permutohedral_tucker_complementary_median_switch_pair_20261008: the sign records whether its median switch lies before or after the midpoint; at an exact central switch (when n is even) use a signed comparison of the two central direction names to resolve the reversal-fixed median. Then lambda(rev pi)=−lambda(pi). Two opposite median labels imply mirrored median switch positions, or two central switches with opposite signed central-direction comparisons.

**THEOREM (INTERIOR / MACROSCOPIC TUCKER CUT).** Put
 k=floor((n+1)/4).
For EVERY active NORI coloring, EVERY physical root x and EVERY n>=7, there exist TWO actual rooted full endpoint-opposed antipodal geodesics (x,pi),(x,sigma), satisfying:
1. lambda(pi)=−lambda(sigma);
2. their full coordinate permutations possess a COMMON nonempty PROPER PREFIX SUPPORT S with
       k <= |S| <= n−k;
3. the two actual physical paths therefore pass through the SAME intermediate cube vertex y=x XOR S at the SAME time |S|, and each has at least k edges on each side of this cut;
4. sigma != rev pi (indeed a proper permutohedron facet never contains a pair of centrally antipodal permutation vertices).

For n>=11, k>=3, so each of the two sides contains at least ONE genuine internal ordered-three-face window. For n>=15, k>=4, and asymptotically the cut lies between roughly n/4 and 3n/4. This substantially strengthens the earlier unrestricted proper-cut Tucker pair.

**Proof.** We prove a general zero-localization lemma.

Let X=|K_x|, with free involution tau and nonvanishing w^d for d=n−3. Let lambda:X^(0)->{±1,...,±r} be ANY antipodally odd labeling; extend the corresponding signed standard basis vectors ±e_j by affine interpolation to an odd PL map f:X->R^r.

Fix 2<=k<=floor(n/2). Define the OUTER-CUT SUBCOMPLEX O_k⊆K_x as the union, over all nonempty proper direction sets T satisfying either |T|<=k−1 OR |T|>=n−k+1, of the full simplex on the actual endpoint-opposed permutation vertices whose FIRST |T| directions form precisely the set T. Every such simplex lies in the corresponding standard permutohedron facet H_T.

**Lemma A: ind(O_k)<=2k−3.** For each permitted T, write D_T for that full simplex. These finite closed subcomplexes cover O_k. A nonempty intersection D_T1∩...∩D_Ts can exist only when the T_i form a STRICT INCLUSION CHAIN: a full direction permutation can begin with EVERY T_i precisely if the sets are nested. An allowed strict chain uses at most k−1 distinct low ranks and k−1 distinct high ranks, totaling at most 2k−2 vertices. Hence the nerve N of the cover has dimension <=2k−3.

The cover is equivariant under permutation reversal, which carries H_T to H_(T^c). The nerve carries the induced involution T->T^c; no nonempty chain is invariant, since a nonempty proper T and its disjoint complement can never be comparable. Thus N is a free involution complex of dimension <=2k−3.

Using an arbitrarily small equivariant open thickening of the finite compact subcomplexes D_T inside O_k, chosen sufficiently small to preserve ALL intersection patterns (possible because the cover is finite and each forbidden finite intersection has a positive minimum max-distance), an equivariant partition of unity gives a continuous equivariant map |O_k|->|N|. Therefore w^(2k−2) vanishes on O_k/tau. A regular invariant neighborhood U of O_k in X retracts equivariantly onto O_k, so w^(2k−2)|U=0.

**Lemma B: if d >= r+2k−2, an f-zero lies OUTSIDE O_k.** Suppose not: Z=f^(-1)(0)⊆O_k. Let V=X\O_k, an invariant open subset avoiding f-zeros. On V, normalized f/||f|| defines an equivariant map to S^(r−1), forcing w^r|V=0. The open sets U,V cover X, and w^(2k−2) vanishes on U while w^r vanishes on V. The standard relative cohomology cup-product argument then forces
   w^(r+2k−2)=0 on X/tau,
contradicting w^d!=0 whenever r+2k−2<=d. Hence some z in f^(-1)(0) lies outside O_k.

Let sigma_z be the unique minimal supporting simplex of z. Since z lies outside O_k, sigma_z does NOT belong to any outer T-facet simplex D_T. But it belongs to SOME simplex of K_x, so all its actual path permutations lie in a common proper permutohedron face, and hence in at least one facet H_S for a nonempty proper S. Since the supporting simplex is not covered by any outer facet, each such S obeys k<=|S|<=n−k.

At the zero f(z)=0, the positive barycentric weights of the supporting vertices sum to zero signed-coordinate vector. Since each vertex vector is one of ±e_1,...,±e_r, for at least one index j there are TWO supporting actual permutation vertices carrying the COMPLEMENTARY labels +j and −j. Both lie in H_S, so their coordinate words share exact prefix support S. Their physical rooted cube geodesics therefore meet at y=x XOR S after |S| edges, with k edges or more on either side. Their signed median defects are complementary by their labels, and central reversal copies cannot share a proper face. This proves the main theorem.

Finally choose k=floor((n+1)/4). With d=n−3 and r=ceil((n−3)/2), one has d−r=floor((n−3)/2), and the integer inequality 2k−2<=d−r holds exactly for k<=floor((n+1)/4). Hence the claimed optimal bound from this dimension-counting argument. QED.

**Relevance to active NORI GRAND CLOSURE.** This FORCES a Tucker pair of GENUINE same-root, endpoint-opposed full geodesics at a COMMON MACROSCOPIC INTERIOR CUT, even in dimensions where a previously forced shared rank-1 or rank-2 cut would have lacked complete three-face windows on one side. It makes the physical two-seam splice theorem directly applicable for n>=11. The actual color of each new seam window is the color of an ordered physical face through y. There is still NO proof that one of the four prefix-suffix splices has <=1 color change or that y is a hub with the required mixed class selector. The Tucker theorem is UNCONDITIONAL; the color-compatible defect-reducing extraction remains the OPEN grand forcing step.

**General template.** Any genuine free-τ permutohedral face nerve with w^d≠0 and an odd ±r labeling has a complementary-label pair sharing a prefix-coordinate support of size k..n−k whenever r+2k−2<=d. The method may be reused with a SMALLER signed-label alphabet to force cuts even closer to n/2.

## EXACT TWO-SIDED HELLY NERVE OF PHYSICAL NORI PATH WITNESSES — GRAND FIXED POINT AND UNIVERSAL INDEX-FOUR CEILING

Let n>=6 and let c be ANY active binary NORI coloring of actual physical ORDERED 3-faces, c(bar F,rev π)=1−c(F,π). Let P range over ALL ACTUAL directed direction-distinct cube geodesic PATH STATES (root + direction word) of length k between 3 and n inclusive whose consecutive physical ordered-three-face windows have AT MOST ONE color change. (Length3 is always admitted, since its word has one color.) Let ΘP be the physical antipodal complement and vertex-sequence reversal; Θ preserves this path class and is a fixed-point-free involution on its VERTICES.

For each admitted rooted P=(x,π), define its exact certified root sheet
 S(P) = x + span_F2{e_i:i belongs to every ordered-three-face window of π}.
Its real cubical hull |S(P)|⊂[0,1]^n is an axis-aligned coordinate face of dimension m(k)=max(6−k,0), and EVERY binary root in S(P) produces the SAME entire sequence of physical window faces in the SAME direction order and hence the same <=1-switch property. This is the exact physical-face fiber theorem of nori_exact_middle_window_root_fiber_dimension_and_root_support_antipodal_action_20261008. We reuse S for both its finite vertex set and its real cubical hull when no ambiguity arises.

Define the TWO-SIDED PHYSICAL CERTIFICATE BOX
   B(P)= |S(P)| × |S(ΘP)| ⊂ [0,1]^(2n).
It is a coordinate product box of dimension 2m(k)<=6. Let
   U = ⋃_(admitted P) B(P)
and define the actual two-sided HELLY NERVE E whose vertices are the admitted path states P and whose simplices are the finite families σ with ⋂_(P∈σ) B(P) nonempty.

THEOREM 1 (honest flag complex with the CORRECT physical involution). Any family of coordinate product faces of [0,1]^(2n) is 2-Helly: pairwise intersection implies whole-family intersection, because each intersection condition is consistency of prescribed 0/1 values on fixed coordinates. Hence E is the FLAG (clique) complex of its genuine pairwise box-intersection graph. Every E simplex is certified simultaneously by one REAL starting cube root for its original path states and one REAL starting root for all their Θ-images; unlike convex averaging, both roots may be chosen Boolean because the intersection box is a coordinate face. The involution Θ is SIMPLICIAL, since
   B(ΘP)=swap(B(P)),  swap(a,b)=(b,a).
The finite convex-box nerve lemma applies equivariantly: E is Θ-equivariantly homotopy equivalent to U with its factor-swap involution. One can construct the equivariant map E→U explicitly on barycentric subdivision: to the barycenter of a nerve simplex σ assign the coordinate center of ⋂_(P∈σ)B(P); nested simplices have their centers inside the smallest intersection, so linear interpolation stays in U. Every map commutes with swap. The reverse nerve map can be built using sufficiently small swap-symmetric open thickenings of the finitely many coordinate boxes, their contractible intersections, and an equivariant partition of unity.

THEOREM 2 (EXACT grand closure fixed-point equivalence). The following are equivalent:
 (i) there is a FULL n-edge antipodal geodesic of c with at most one window-color change;
 (ii) the geometric union U intersects the swap-fixed DIAGONAL {(r,r):r∈[0,1]^n};
 (iii) E has a Θ-fixed point;
 (iv) E has an edge joining one path state P to its physical Θ-image ΘP.

PROOF. Let W be used directions of P, D=[n]\W. Physical reversal sends its root x to x XOR D and its order to rev π. Every coordinate i∈D is fixed in S(P) to bit x_i and fixed in S(ΘP) to bit 1−x_i. Hence if D nonempty, the two sheets S(P),S(ΘP) are disjoint. If D empty, W=[n], the starting roots of P and ΘP are THE SAME, and their middle-coordinate root-sheet translation sets are identical under reversal, so S(P)=S(ΘP). Thus B(P) meets the diagonal iff P is a FULL good path, and B(P)∩B(ΘP) nonempty iff P is FULL. This proves (i)⇔(ii)⇔(iv). An opposite edge has Θ-fixed midpoint. Conversely a Θ-fixed point in the nerve has a Θ-INVARIANT minimal supporting simplex; any vertex P in that simplex has ΘP there too, forcing their intersection B(P)∩B(ΘP) and hence a FULL good path. QED.

THEOREM 3 (NONSPURIOUS odd unused-sign labeling, with honest simplicial cells). Define the signed-unused-coordinate vector η(P)=bar(endpoint(P))−root(P)∈{-1,0,+1}^n. As previously proved, η(ΘP)=−η(P), and η_i(P) is nonzero precisely for UNUSED coordinate i. For any simplex σ of E, the original sheets S(P), P∈σ, have a COMMON ACTUAL ROOT r. Whenever coordinate i is unused in P and Q it is fixed in both S(P),S(Q), so r_i=x_i(P)=x_i(Q), hence η_i(P)=η_i(Q). Thus NO E simplex ever contains both +1 and−1 at the same coordinate: E is SIGN-COHERENT. Its affine η-map E→R^n is Θ-ODD, and its zero is a LITERAL FULL admissible path certificate, not a spurious averaged coincidence.



*The scope-specific limitation and complete proof are preserved in linked research note note_antipodal_involution_index_and_bichromatic_bad_root_limits.*

## Equivariant obstruction classes and root transport

The active Subsections examine the topology of actual ordered physical window transitions and the two-cap geometry of genuine geodesic witnesses. They prove physical transport statements, seam-square compatibility criteria, and conditional lifting results whose hypotheses retain full ordered-face provenance.

This section does not identify ambient equivariant index with monochromatic geodesic extraction. The precise root-slide selector limitation has been moved to a research note, preserving its proof and exact topological scope. The remaining physical-window and moving-seam results should be read as positive structural inputs and explicitly conditional extraction statements.

*Full Section composition: [source manuscript](nori_topological_obstructions.md).*

### Physical good-window complexes, temporal parity, and root transport

# Physically certified window topology and root transport

Let \(c\) be an antipodal-reversal-odd binary coloring of ordered physical three-faces of \(Q_n\), \(n\ge6\). A direction-distinct geodesic has a window of three successive ordered free directions at each internal position; the window color depends on its physical face and order. A geodesic is *good* if these colors change at most once.

Define \(W=W_c\) as the simplicial complex whose vertices are actual ordered physical three-face windows and whose simplices are sets of windows appearing *jointly in one actual good geodesic*. An antipodal-reversal involution \(\tau\) sends \((F,\pi)\) to \((\bar F,\operatorname{rev}\pi)\). It acts freely: two windows of a direction-distinct path have distinct free-coordinate sets, while a window and its \(\tau\)-mate have the same free set and different ordered physical labels. Pairwise window compatibility alone need not certify a simplex.

## Exact metric extraction

The center \(m(F)\in\{0,\frac12,1\}^n\) of a physical face defines \(d(u,v)=\|m(F_u)-m(F_v)\|_1\). This distance is integer-valued on pairs of three-faces: free coordinates belonging to exactly one face contribute a total of \(3-|\operatorname{free}F_u\cap\operatorname{free}F_v|\), and differing common fixed coordinates contribute integers.

**Lemma.** If two ordered windows occur in positions \(i<j\) of the same geodesic, then \(d(u,v)=j-i\).

**Proof.** Between successive windows one free direction exits and another enters, changing their face center in two coordinates by one half each. Each coordinate moves monotonically during a direction-distinct geodesic, so the successive \(\ell^1\) displacements of size one add without cancellation. \(\square\)

**Theorem (faithful grand extraction).** NORI holds for \(c\) exactly when \(W_c\) has an edge \(\{u,v\}\) satisfying \(d(u,v)=n-3\).

**Proof.** The extreme windows of a good full \(n\)-edge geodesic furnish such an edge. Conversely, an edge has a single actual good-path certificate. Trimming that certificate between the selected windows produces a good path of exactly \(3+d(u,v)=n\) distinct-coordinate edges, hence a full antipodal geodesic. \(\square\)

In constructing edges, metric coincidence by itself is insufficient. Ordered triples separated by one window must overlap in their last/first two directions; those separated by two must overlap in one specified direction. Disjoint triples permit precisely the common fixed coordinates on which the two physical faces differ as intervening directions. Together with consistent exterior fixed bits, these literal incidence rules give an exact test for existence of a common direction-distinct path.

## Temporal cohomology

On every edge of \(W\) define \(\beta(uv)=d(u,v)\bmod2\). Any triangle has a common actual witness, with window positions \(i<j<k\); thus its coboundary equals \((j-i)+(k-j)+(k-i)=0\bmod2\). Consequently \(\beta\) is a \(\tau\)-invariant one-cocycle. Write \(\bar\beta\in H^1(W/\tau;\mathbb F_2)\) for its descent, and \(w\) for the characteristic class of the antipodal double cover. The cocycle \(\alpha(uv)=\beta(uv)+c(u)+c(v)\) is also invariant, and records same-color transitions along consecutive-window edges. Tracking the change of endpoint colors when choosing different lifts of quotient vertices yields
\[
[\bar\alpha]=[\bar\beta]+w. \tag{1}
\]
The universal physical window-shift graph is connected, so the covering class is nonzero; a physical five-window pentagon has \(\beta\)-value one while lifting closed, so \(\bar\beta\) and \(w\) are independent.

## Physical pentagons give genuine good paths

Fix a physical cube vertex \(z\) and five cyclic directions \(p_0,\ldots,p_4\). Let \(u_i\) be the ordered three-face *through \(z\)* with order \((p_i,p_{i+1},p_{i+2})\), with indices mod five. Each consecutive pair is an actual four-edge witness, so the five mandatory edges form a pentagon in \(W\) of odd \(\beta\)-value. Put \(h_i=c(u_i)\) and \(\delta_i=h_i+h_{i+1}\in\mathbb F_2\). Since \(\sum_i\delta_i=0\), the cyclic change count belongs to \(\{0,2,4\}\). Counting cyclic adjacent pairs of changes gives respectively \(0\), at most \(1\), or \(3\) bad consecutive three-window words. Thus exactly \(5,4,\) or \(2\) of the five cyclic three-window words are good.

The word \((h_i,h_{i+1},h_{i+2})\) is witnessed by the physical five-edge geodesic with direction order \((p_i,\ldots,p_{i+4})\) and start \(z\oplus e_{p_i}\oplus e_{p_{i+1}}\). It supplies the chord \(u_i u_{i+2}\) and its triangle exactly when the word is good; an alternating word has no compatible good-path witness because the intervening ordered physical window is uniquely forced. Hence the local induced five-vertex complex is a pentagon plus precisely \(g\in\{2,4,5\}\) free chord–triangle pairs, each collapsing away to the original pentagon.

The 120 orders on any five directions split into 24 cyclic classes; each contributes at least two good two-bit-rerooted paths. Summing over reference vertices \(z\) and using the bijection
\[
(z,p)\mapsto(z\oplus e_{p_1}\oplus e_{p_2},p)
\]
proves that at least **\(2/5\)** of all actual rooted five-edge paths on a fixed five-coordinate support are good. On each physical five-cube this yields at least \(\lceil (2/5)32\rceil=13\) distinct good roots.

The same odd-cycle argument gives equality of two consecutive windows with probability at least \(1/5\) for a uniformly rooted five-block. For a uniformly chosen full root \(X\) and full direction order \(p\), each of its \(n-3\) comparisons has that marginal law after adjoining one unused direction to its actual four-edge block. Linearity, with no independence assumption, yields
\[
\mathbb E D(X,p)\le \tfrac45(n-3),\qquad
\exists (X,p):D(X,p)\le\lfloor\tfrac45(n-3)\rfloor. \tag{2}
\]
This holds for arbitrary physical ordered-three-face colorings, even without oddness. For ordered \(r\)-faces the analogous bound is \((2r-2)(n-r)/(2r-1)\) when \(n\ge2r-1\).

## The dimension bound and the correct closure class

If the maximum length of a good geodesic is \(k\ge5\), a top-dimensional simplex comprises all \(k-2\) ordered windows of a good length-\(k\) witness. Delete an internal window. Consecutive retained ordered triples overlap in at least one direction; the shared direction occurs once along any direction-distinct path, fixing the relative window positions. The extreme retained physical windows then determine their full direction support and root up to free bits common to all windows, which preserve the entire physical window sequence. Thus the deleted internal window is uniquely forced. Its complementary codimension-one face is free. Performing these collapses in \(\tau\)-paired pairs removes all top-dimensional simplices.

For \(n\ge6\), the resulting equivariant collapses give
\[
\operatorname{ind}_{\mathbb Z_2}(W)\le n-4
\quad\text{for every coloring,}\qquad
\operatorname{ind}_{\mathbb Z_2}(W)\le n-5
\quad\text{under grand failure}. \tag{3}
\]
Therefore **any nonzero degree-\((n-4)\) cohomology class** on \(W/\tau\), for example \(w^{n-4}\) or \(\bar\beta\,w^{n-5}\), is a sufficient certificate of a good full geodesic. The formerly proposed degree \(n-3\) is unavailable even when a full good path exists; a direct equivariant map from the entire index-\((n-3)\) endpoint-balanced permutohedral carrier into \(W\) is ruled out.

A physically certified annulus gives a conditional next step. Let \(P\) be a physical odd pentagon and \(Q\) a genuine path in \(W\) joining one of its windows to its antipodal mate. If the loops \(p=[P]\), \(q=[Q]\) commute up to based homotopy in \(W/\tau\) through actual jointly good-path-certified simplices, they induce \(f:T^2\to W/\tau\) with \(f^*\bar\beta=a+\varepsilon b\) and \(f^*w=b\). Hence \(f^*(\bar\beta\smile w)=a\smile b\ne0\). This proves \(\bar\beta\smile w\ne0\) **under the stated physical annulus hypothesis**.

The remaining missing implication is global: the local pentagons, their root transport, and their individually certified triangles must be glued across actual physical roots and orders so as to produce degree-\((n-4)\) cohomology or, directly, a certified edge at distance \(n-3\). The theorems above supply faithful extraction and unconditional local density; they do not yet prove the unrestricted grand conjecture.

## Recent consequences and compatibility conditions

# Genuine good-window carrier has a connected four-sheeted temporal/antipodal voltage cover

Assume n≥5 and an active NORI coloring of actual physical ordered three-faces, with c(bar F,rev pi)=1-c(F,pi). Let W=W_good(c) be the finite simplicial complex whose vertices are ACTUAL ordered physical 3-face windows and whose simplices are finite window sets jointly contained in ONE actual at-most-one-switch geodesic. The antipodal physical reversal tau acts freely simplicially. Let Y=W/tau.

For any edge uv in W set beta(uv)=d_1(m(F_u),m(F_v)) mod 2, with physical face centers m. By the proved intrinsic distance theorem nori_good_window_set_complex_metric_parity_extension_and_full_span_edge_20261009, any simplex has a common actual good path and d_1 between two windows equals their INTEGER window-position separation on that path. Consequently beta is a genuine tau-invariant 1-cocycle: on each triangle at positions i<j<k the sum of the three edge distances equals (j-i)+(k-j)+(k-i)=0 mod2. Let beta_bar be its descended class in H^1(Y;F2). Write w for the first Stiefel–Whitney class of the actual two-fold cover W→Y.

**Theorem 1 (connected physical window-shift graph).** The 1-skeleton of W is connected, independently of the coloring. Indeed the actual ordered-window SHIFT graph H has one edge for each legal pair of overlapping ordered windows along a 4-edge path; every such path is admitted because it has only two color windows and at most one change. For each coordinate direction i, the induced window-shift graph H_i consisting of ordered windows whose free triple contains i and shift edges having i as one of the two middle directions is CONNECTED by the proved coordinate-retaining shift-graph lemma (Item nori_certified_square_complex_connected_antipodal_one_class_20261008). Any H_i and H_j share windows whose free triple contains both i,j; all windows belong to some H_i. Hence H, and therefore W, is connected.

**Theorem 2 (two independent literal holonomies).** The two degree-one cohomology classes beta_bar and w are LINEARLY INDEPENDENT in H^1(Y;F2). More concretely, the covering associated with the character pair
  pi1(Y) → F2×F2,
  [gamma] → ( <beta_bar,gamma>, <w,gamma> )
is SURJECTIVE. There exists a connected regular 4-sheeted cover of Y with deck group Z2×Z2, with a literal path/window lift model given below.

**Proof.** Fix any physical cube vertex z and any five distinct directions p0,...,p4 in cyclic order. Let u_i denote the ACTUAL oriented 3-face through z with free order (p_i,p_(i+1),p_(i+2)), indices mod5. Every consecutive pair (u_i,u_(i+1)) is realized on one genuine 4-edge geodesic and is thus an edge of W regardless of its two colors. These five edges form a LITERAL CLOSED PENTAGON in W. Each edge has physical-window center distance 1, so beta evaluates to 5=1 mod2 on that closed pentagon. This pentagon is a closed LIFT in W, hence its image in Y has w-voltage zero. It therefore witnesses the character pair (beta_bar,w)=(1,0).

Because the connected W is a free antipodal double cover of Y, some edge path P within W joins any chosen window u to tau u. Its image in Y is a loop with w-voltage 1 (lift changes sheets) and beta_bar-voltage epsilon∈F2, depending on P. Together the two loop voltages (1,0) and (epsilon,1) generate all of F2×F2. Thus the joint character pair is surjective and the classes are independent. \(\square\)

**Theorem 3 (explicit path-certified four-sheeted cover).** Form the beta-parity double cover of W as follows. Its vertices are ordered pairs (u,t) with u an ACTUAL physical window of W and t∈F2. Over any simplex σ={u_0,...,u_k} of W, include precisely its two lifted simplices with labels
  t(u_i)=h+beta(u_0,u_i) for some h∈F2.
The cocycle equation makes the lifting independent of the choice of base vertex u_0 and compatible on common faces. The beta-double cover is CONNECTED because W is connected and the literal pentagon has odd beta-voltage. Physical reversal lifts by
  tilde_tau(u,t)=(tau u,t),
while parity-deck change is
  kappa(u,t)=(u,t+1).
These commuting free involutions generate four deck transformations, giving a CONNECTED REGULAR cover
  (beta-cover of W) → Y
with deck group {1,kappa,tilde_tau,kappa tilde_tau}≅(Z2)^2, over each quotient-window vertex exactly four lifted windows. Every cell is the lift of a simplex already certified by ONE actual good geodesic: there are no invented geodesics or simplex fillings.

**Theorem 4 (three genuine nonzero one-classes and a conditional maximum-distance cup-product extraction).** Let alpha be the descended 1-cocycle with edge value
  alpha(uv)=beta(uv)+c(u)+c(v) mod2,
so on consecutive-window edges it is precisely the monochromatic-shift indicator. The cohomology identity from the good-window theorem gives [alpha_bar]=[beta_bar]+w. Since beta_bar and w are independent, the three classes w,beta_bar,alpha_bar are ALL NONZERO and distinct.

For r=3, if ANY homogeneous polynomial P(w,beta_bar) of total cohomological degree n−3 has NONZERO evaluation in H^(n−3)(Y;F2) — for example w^(n−3), beta_bar·w^(n−4), beta_bar^2·w^(n−5), or alpha_bar^(n−3) — then an actual full n-edge NORI geodesic with at most ONE change MUST exist.

**Proof of conditional extraction.** Under hypothetical grand failure every simplex of W comes from an actual admissible path with at most n−1 edges, hence at most n−3 windows and dimension at most n−4. Because the quotient by free simplicial tau has the same dimension, H^(n−3)(Y;F2)=0. Thus nonzero total-degree-(n−3) cup product forces an n−3-dimensional simplex in W, certified by at least n−2 distinct physical windows on ONE actual good geodesic. Since a direction-distinct path with n edges has at most n−2 windows, this certificate must be a FULL good antipodal geodesic. \(\square\)

**Why this is useful, and exact remaining gap.** The temporal/window-index parity and physical antipodal sheet-flip are two genuinely INDEPENDENT topological monodromies, present for EVERY coloring, with an explicit faithful fourfold lift. This does not by itself prove a NONZERO PRODUCT of degree two or higher: a wedge of two circles also has independent H^1 classes with all degree-two cup products zero. The new, mathematically precise topology-first closure target is to show that actual root/order/witness-incidence cells force ONE high-degree MIXED PRODUCT in the good-window complex quotient. Unlike a pure fixed-root Borsuk–Ulam index, such a product could simultaneously detect rooted progression and physical antipodal transport. The physical five-window Möbius band from Item nori_physical_five_window_mobius_band_pairwise_nonhelly_good_window_complex_20261008 realizes the beta-loop geometrically, while the global window-shift connectivity supplies the w-loop. Demonstrating nontrivial higher-dimensional cup products between these loops is the remaining global compatibility theorem, not yet established.

# A higher-dimensional good-window carrier with exact physical metric and parity class

Inputs:
- exact root-sheet fiber and physical reversal formulas;
- nori_window_shift_monochromatic_edges_universal_cohomology_class_20261008;
- nori_good_contiguous_path_flag_complex_equivariantly_collapses_to_window_graph_20261009.

Let c be an active ordered-r-face coloring, n>r, and let W_good be the finite simplicial complex whose vertices are ACTUAL ordered physical r-face windows. A finite set of window vertices spans a simplex precisely when all occur along ONE actual direction-distinct geodesic whose complete window word has at most one color change. Taking faces is allowed; a simplex need not list consecutive windows. Keep the actual good path as its certificate.

Physical antipodal reversal induces a simplicial involution tau. It is FREE: one geodesic cannot contain a window and its antipodal reversed mate, since these have the same free-coordinate set and a direction-distinct path has distinct free-coordinate sets at distinct window positions. The two ordered windows themselves are distinct under the active coloring law.

## 1. Metric positions are intrinsic to physical windows
For an unordered physical face F let m(F) in {0,1/2,1}^n be its center. For two ordered windows u=(F,pi), v=(G,rho) define
 d(u,v)=||m(F)-m(G)||_1.
This is always an INTEGER for two r-faces: each coordinate free in exactly one face contributes 1/2, and there are 2(r-|free(F) intersect free(G)|) such coordinates; the remaining contributions are 0 or 1.

If u and v occur at window positions i<j along a direction-distinct path, then
 d(u,v)=j-i.
Indeed the successive face centers move monotonically in each physical coordinate. Each window shift moves the exiting and entering free coordinates by 1/2 each in their fixed path directions, giving L1 step length one. Coordinatewise monotonicity makes lengths additive.

Thus their window-position separation is determined by their actual physical faces, independently of which compatible path order witnesses them.

## 2. Exact grand extraction is a maximum-distance edge
Grand closure holds iff W_good has an edge {u,v} with
 d(u,v)=n-r.
The first and last windows of a full good path give such an edge. Conversely, an edge has an actual good-path certificate. Trim that path to the interval from its earlier named window through its later named window. The resulting good path has exactly
 r+d(u,v)
edges. At distance n-r it therefore has n distinct directions and is a full grand witness.

In particular, under hypothetical failure every edge distance is <=n-r-1 and
 dim W_good <= n-r-1.
Always dim W_good<=n-r. This elementary dimension bound admits the stronger free-face reduction in section 5 below. That reduction makes the exponent n-r unattainable even when grand paths exist; the useful forcing exponent is n-r-1 (for r>=3 and n>=r+3).

## 3. The window parity class extends to every dimension
Assign each edge the mod-two value
 beta(uv)=d(u,v) mod2.
This is a SIMPLICIAL 1-COCYCLE on W_good. For any triangle, place its three windows in their actual common good path in order i<j<k. The metric identity gives
 beta(uv)+beta(vw)+beta(uw)
 =(j-i)+(k-j)+(k-i)=0 mod2.
The same edge value is used in every witnessing simplex because d is intrinsic.

It is tau-invariant since physical complementation preserves L1 distances. It therefore descends to a cocycle beta_bar on the quotient (equivalently use the associated cellular/Delta-complex quotient or a common subdivision).

For r=3, W_good contains the ENTIRE physical window-shift graph H: every four-edge geodesic has at most one color change. On H every beta-edge value is 1. The established centered pentagon therefore evaluates beta to 1, proving that the graph parity class SURVIVES in this higher-dimensional carrier. In particular these pentagons cannot become boundaries in W_good.

Define
 alpha(uv)=beta(uv)+c(u)+c(v) mod2.
Then alpha is also a tau-invariant cocycle. On consecutive-window edges it is exactly the monochromatic-shift indicator. Thus the actual connector class extends consistently to higher-dimensional good-path cells, with no arbitrary filling of odd pentagons.

Let w be the cover class on W_good/tau. Choosing lifts of quotient vertices and recording the edge voltage gives the exact cohomology identity
 [alpha_bar]=[beta_bar]+w.
On a lifted closed centered pentagon, w evaluates 0 and beta_bar evaluates 1. Using the established connectedness of H (n>=5), its free cover has nonzero w; since H is contained in W_good, w remains nonzero there. Hence beta_bar and w are linearly independent in H^1 of the quotient. Their higher cup products are now well-defined in a genuinely higher-dimensional path-certified carrier. Nonvanishing of a higher product remains to be proved.

## 4. Why this carrier differs from interval flags
There is a natural equivariant simplicial map from the barycentric contiguous-path poset to the barycentric subdivision of W_good, sending a good path to its set of physical windows. Different path orders can map to the same face or have faces intersect along a NONCONTIGUOUS set of shared windows. The fibers of this identification need not be contractible.

These cross-order identifications retain the information discarded by the interval-poset collapse. Each resulting simplex still has one literal good-path certificate, so the maximum-distance edge extraction remains exact. Static root-box incidence and ordinary contiguous-extension incidence alone do not provide these shared-window cells.

## 5. Forced intermediate windows give one further dimension reduction
Suppose r>=3, and restrict to a hereditary family of good paths of maximum length at most k, where k>=r+2. Then the corresponding window complex equivariantly collapses to a complex of dimension at most k-r-1.

Proof. A top-dimensional simplex sigma consists of ALL t=k-r+1>=3 windows of a good length-k path P. Remove one INTERNAL window w_j, retaining the first and last windows. Consecutive retained windows have position gaps one or two, hence their ordered r-tuples overlap in at least r-2>=1 directions. Any path containing two such tuples must place them at their original signed position difference: a shared coordinate can occur only once, and its two prescribed tuple positions determine that difference. Chaining these overlaps fixes the whole retained window order and all k directions of P.

Moreover, the first and last retained physical windows already have free-set intersection M(P). Thus any root producing the retained physical windows differs from P's root only in M(P), which preserves ALL physical windows. The deleted middle window is therefore uniquely forced. No OTHER simplex of maximum size t can contain sigma without w_j, and no larger simplex exists at this rank bound. Hence sigma without w_j is a free codimension-one face of sigma.

The involution pairs the maximum simplices freely. Choose internal windows in paired mirror positions, and perform the elementary collapses in antipodal pairs. Their free faces are distinct and cannot belong to another maximum simplex by the uniqueness just proved. Removing all maximum simplices leaves dimension at most t-2=k-r-1. QED.

For the full good-window complex this gives, for r>=3 and n>=r+3:
 - ALWAYS: ind_Z2(W_good)<=n-r-1;
 - under GRAND FAILURE: ind_Z2(W_good)<=n-r-2.
For the second line, if a length-(n-1) good path exists, apply the collapse with k=n-1; if all good paths are shorter, the raw dimension bound already gives the conclusion.

Therefore the SHARPENED SUFFICIENT INDEX TARGET is
 w_1(W_good/tau)^(n-r-1) !=0  ==> grand closure.
For ordered three-faces the exponent is n-4, while hypothetical failure gives index at most n-5.

This also clarifies the comparison with the endpoint-balanced permutohedral carrier of index at least n-3: no equivariant map of that entire high-index source into W_good can exist, even for colorings with grand witnesses, because W_good ALWAYS has index at most n-4. A source restriction losing one index, or a different cohomological comparison, is required. An additional odd scalar zero locus has the appropriate index lower bound n-4, but no witness-preserving transfer from such a locus is established here.

## 6. Closure frontier
The good-window complex provides:
 - exact extraction through a maximum-distance edge;
 - higher-dimensional continuation of the two independent window/cover classes;
 - an explicit free-face reduction separating the possible index n-4 from the no-grand ceiling n-5 for ordered three-faces.

The remaining forcing task is to prove nonzero w^(n-4), or another sufficient invariant, using physical cross-order and cross-root witness identifications. Static box intersections and ordinary interval inclusions have the separate low-index obstructions proved in the companion items. A common proper permutation face alone does not certify a simplex of W_good. The grand conjecture remains open.


### Two-cap centering and moving physical seam-square directions

# Two-cap centering and moving physical seam-square directions

The antipodal boundary sphere of the full permutohedron supports an odd map formed from projected coordinate positions together with actual central ordered-face colors. Its zero yields a convex packet of complete geodesics in a common proper face. The face leaves at most two endpoint-cap directions, suggesting a physical two-coordinate seam square on which a repair might occur.

## Equivariant suspension-LIFT criterion: witness-compatible fillings generate genuine antipodal cohomological index

Let X be a finite CW complex (e.g. a simplicial/cubical NORI witness complex) with a FREE continuous involution tau, and suppose X=A∪tau(A) for subcomplex A. Write C=A∩tau(A), a tau-invariant genuine intersection subcomplex. Throughout S^k carries the standard antipodal involution and its upper hemisphere in S^(k+1) is a closed (k+1)-ball with equator S^k.

**Theorem 1 (equivariant index LOWER bound from a one-sided filling).** Suppose there exists a continuous equivariant map
  g:S^k -> C,   g(-u)=tau(g(u)),
AND the map g regarded as an ordinary map S^k->A is nullhomotopic, equivalently extends to a continuous map
  G:D^(k+1) -> A
whose boundary restriction is g. Then there exists a continuous tau-equivariant map
  F:S^(k+1) -> X.
In particular, the first Stiefel–Whitney class w∈H¹(X/tau;F2) has
  w^(k+1) != 0.
Thus the cohomological antipodal index of X is at least k+1.

**Proof.** Regard the upper hemisphere H_+ of S^(k+1) as D^(k+1), its equator as S^k, and use G to define F on H_+. On the lower hemisphere H_-= -H_+, define
  F(-z)=tau(G(z))   for z∈H_+.
On the equator, where both hemisphere prescriptions apply, they agree because G(-u)=g(-u)=tau(g(u))=tau(G(u)). Thus the gluing lemma yields a continuous globally equivariant F:S^(k+1)→X. Passing to free-involution quotients gives f:RP^(k+1)→X/tau; the pullback of the cover's w is the tautological generator a∈H¹(RP^(k+1);F2), by equivariance/pullback of principal Z2-bundles. Hence f*(w^(k+1))=a^(k+1)≠0, establishing w^(k+1)≠0. QED.

**Theorem 2 (relative suspension sandwich for CONTRACTIBLE A).** If A is nonempty and contractible (in particular if A is a literal simplex or cone), then every equivariant map g:S^k→C for k>=0 has an ordinary nullhomotopic composite S^k→A, so the suspension lift applies. Consequently
  ind_Z2(C)+1 <= ind_Z2(X)
provided C is nonempty and the index is defined via maximum nonzero w power. The general UPPER index bound from Item nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 says
  ind_Z2(X) <= dim(C)+1.
Thus for a contractible one-shore carrier A,
  ind_Z2(C)+1 <= ind_Z2(X) <= dim(C)+1,
where the left inequality requires an equivariant map from a sphere S^k realizing ind(C); a free complex can have high cohomological index without an equivariant sphere map from that dimension, so in FULL generality replace ind(C) on the left by
  coind(C)=max{k: exists equivariant S^k→C}.
The rigorously valid sandwich is
  coind(C)+1 <= ind(X) <= dim(C)+1.
This proviso distinguishes topological index from coindex; conflating them would be false.

**Corollary 3 (an actionable NORI monochromatic-disk test).** Let X=X_c be the actual cubical center-square witness complex of an active NORI coloring, and A=X_0 be the genuine color-0 certified square subcomplex together with all physical cube vertices. Let C=X_0∩X_1 be its color-overlap subcomplex. Suppose C contains a tau-equivariant closed loop g:S¹→C: geometrically, an antipodally paired physical loop whose full set of edges each admits BOTH-color genuine monochromatic centered four-path certificates. If this loop also bounds a continuous disk in X_0 (for example a finite combinatorial disk tiled by color-0 certified squares with compatible boundaries), then
  w_1(X_c/tau)^2≠0.
This is exactly the missing TOP-DIMENSIONAL counterpart of the previous result: absence of any common-edge certificate forces w1²=0, while the presence of an equivariant common-edge CYCLE which can be capped by honest monochromatic squares forces w1²≠0.

**Important geometric warning.** A cycle being a mod-2 homological boundary in X_0 does NOT automatically give a nullhomotopy; the theorem assumes an actual disk/nullhomotopy. A single isolated common edge, even accompanied by its antipodal mate, gives no equivariant S¹ loop unless there are connecting common edges.

**Corollary 4 (the EXACT root-profile two-shore carrier).** Let K=A∪tau(A) be the exact LABEL-SPACE carrier of nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008 and nori_reversed_tail_mixed_profile_interface_equivariant_suspension_20261008, where A=union_x Delta(L_x), C=A∩tau(A). The universal singleton support labels guarantee that A is a CONE, not generally a simplex, hence contractible. Therefore any equivariant map S^k→C caps in A and induces an equivariant S^(k+1)→K; an equivariant loop in C yields nonzero w1² on K. The SIGNED-ROOT NERVE N is a DIFFERENT complex: its positive and negative vertex shore simplices do not themselves cover the mixed faces, and one must NOT write N=A∪tau(A) with only those shore simplices. Rather, the previously proved equivariant nerve equivalence K≃_tau N transfers the resulting cohomological index statement from K to N. The challenge is to build the equivariant loop inside actual mixed-label C, where each simplex has real common-reachability certificates.

**Research strategy: topology first, combinatorics inside it.** Pursue a growing family of genuine root/terminal-memory witness cells to construct an equivariant circle (and higher sphere) in C. The four-edge opposite-color reversed-tail diamonds are local candidate 1-cells, but they prove SAME support for the two reversed tails, whereas the GRAND fixed point needs COMPLEMENTARY support. They cannot be treated as cells of C until that compatibility is established. If a valid equivariant loop in C is established, the index rises through the cone structure. The remaining high-index-to-fixed-point step must then use the root-probability difference field V(a,b)=a-b and the exact deleted-product dimension obstruction: index or coindex at least p−1 (where p is retained profile count) is too high for a hypothetical no-closure carrier Z⊆S^(p−2). No such high-index lower bound is presently proved.

**No grand-closure claim.** This result is a complete general topological lemma and an exact set of sufficient witness conditions. The major combinatorial problem is supplying honest overlap loops and their fillings from the physical ordered-three-face constraints, and then reaching the required index threshold.

## Odd-dimensional FULL-SPHERE two-cap Tucker theorem: actual opposite central ordered-three-face colors and balanced physical i-edge positions

Let n=2m+1>=7 be ODD, and let c be ANY active NORI ordered-three-face binary coloring satisfying c(bar F,reverse pi)=1-c(F,pi). Fix ANY physical cube root x, ANY distinguished direction i∈[n], and ANY two other distinct directions a,b∈[n]\{i}. Put T=[n]\{i,a,b}, so |T|=n-3.

Let P_n be the genuine centrally symmetric (n−1)-dimensional permutohedron, whose original vertices v_pi correspond to ALL ACTUAL full antipodal cube geodesic direction permutations pi from x, with central antipodal involution pi→rev pi. Its boundary ∂P_n is an actual free antipodal sphere S^(n−2), of cohomological index n−2.

For each actual full order pi, define:
(1) v_i(pi)∈{0,1}^([n]\{i}) to be the projected actual physical i-edge position along its x-rooted full geodesic, namely root bits x_j XOR 1_{j BEFORE i in pi}. Under reversal, v_i(rev pi)=1−v_i(pi).
(2) q(pi)=the ACTUAL binary color of the CENTRAL ordered-three-face window of the full path: its index is j=m=(n−1)/2 out of the n−2=2m−1 windows. Since active NORI full-path physical reversal gives w(x,rev pi)=1−reverse(w(x,pi)), the central position j=m maps to ITSELF while its color complements:
  q(rev pi)=1−q(pi).
Thus epsilon(pi)=(-1)^q(pi)∈{+1,−1} is an honest Θ-ODD signed label of a genuine physical central ordered three-face window.

**THEOREM (FULL-SPHERE TWO-CAP ACTUAL COLOR PACKET).** For EVERY choices of x,i,a,b above, there exist at most n−1 ACTUAL full x-rooted antipodal geodesics with direction orders pi_1,...,pi_s, together with strictly positive weights alpha_r summing to1, such that:
A. ALL selected permutations lie in a common PROPER permutohedron face, hence share one nonempty proper prefix used-direction set S. Necessarily EITHER
  (EARLY CAP) S⊆{a,b}, so 1<=|S|<=2,
OR
  (LATE CAP) [n]\S⊆{a,b}, so n−2<=|S|<=n−1.
Therefore the packet lies in a literal one/two-direction endpoint-cap chart prescribed by a,b, and its full paths share the corresponding early or late physical cube vertex.
B. Their ACTUAL central ordered-three-face window colors include BOTH 0 and1, indeed
  sum_(r:q(pi_r)=0) alpha_r = sum_(r:q(pi_r)=1) alpha_r=1/2.
C. For EVERY coordinate j∈T, the weighted fraction of selected actual orders having j BEFORE i is EXACTLY1/2:
  sum_r alpha_r 1_{j appears before i in pi_r}=1/2.
Hence for each j∈T, at least one selected genuine full path traverses j before i and one traverses it after i.

**PROOF.** At each original permutohedron vertex v_pi prescribe the vector
  F(v_pi)=((v_i(pi)_j−1/2)_{j∈T}, epsilon(pi))∈R^{(n−3)+1}=R^(n−2).
Both blocks transform by NEGATION under central reversal pi→rev pi. Extend these original-vertex values continuously and equivariantly over ∂P_n, for example by taking at each proper face barycenter the arithmetic mean of values on that face's original permutation vertices and interpolating linearly on the antipodally equivariant barycentric face-flag triangulation. All face means and the resulting PL map satisfy F(τz)=−F(z).

By the Borsuk–Ulam theorem for the free antipodal sphere ∂P_n≅S^(n−2), this odd map to R^(n−2) has a zero z. Let H be the unique minimal proper permutohedron face containing z. Every vertex of the face-flag barycentric simplex containing z has F-value which is an arithmetic mean of actual original-permutation-vertex F-values inside H. Therefore 0 is in the CONVEX HULL of the actual vector values F(v_pi) for genuine permutation vertices pi of H. By Carathéodory's theorem in R^(n−2), at most n−1 genuine vertex vectors suffice for a positive convex representation 0=sum alpha_r F(v_pi_r).

The last scalar coordinate of F enforces sum alpha epsilon(pi_r)=0, so there are actual central window colors of BOTH bits and their weights each total1/2, proving B. The projected i-position coordinates enforce exactly the weighted before/after balances C (root bits x_j only complement positions, so centering-zero is equivalent to order fraction1/2).

Any proper permutohedron face H lies in a facet H_S fixing a nonempty proper prefix support S. If i∉S, every coordinate j∈S necessarily precedes i in EVERY permutation of H, so balancing in every j∈T forces S∩T=empty. Since i∉S too, S⊆[n]\(T∪{i})={a,b}, establishing EARLY CAP. If i∈S, each j outside S necessarily comes AFTER i in every permutation of H, so balancing forces T⊆S. Thus [n]\S⊆[n]\(T∪{i})={a,b}, giving LATE CAP. Finally a proper facet cannot contain both pi and rev pi, so the opposite central colors in this packet are not merely tautological full-path reversal copies. QED.

**WHY THIS IS A STRENGTHENING.** The previous index-(n−3) endpoint-opposed path nerve could balance n−3 i-edge coordinates with TWO leftover cap coordinates but could not simultaneously force an additional independent odd signed witness color. For ODD n, the central physical three-face color is itself an odd scalar on the FULL permutohedral boundary S^(n−2), whose index is ONE HIGHER. Consequently one gains genuine opposite-color central three-face windows at NO EXTRA CAP COST. This is a direct dimension-independent topology-first conclusion, with fully physical path/color provenance.

**EXACT REMAINING GRAND GAP.** The resulting central windows of colors 0 and1 can occur on DISTINCT physical three-faces, and their full paths need not have at most one color change. The early/late two-cap support S may be {a,b} (or its complement), not necessarily separate the fixed directions a,b. Therefore the theorem does NOT itself produce the exact same-root complementary reversed-two-tail monochromatic reachability intersection. One must force alignment/transport of the central opposite-color physical faces through the MOVING root/seam square, or show that the genuinely balanced packet contains compatible monochromatic branches. No such unconditional extraction is proved here.

## Odd-dimensional full-sphere TWO-CAP Tucker packet contains opposite CENTRAL face colors at macroscopically separated actual i-edge positions

Let n>=7 be odd, c any active NORI ordered-three-face coloring, x any cube starting root, i any distinguished direction, and a,b any two other distinct directions. Put T=[n]\{i,a,b}, of size k=n−3. The proved actual FULL permutohedron sphere Borsuk–Ulam theorem nori_odd_full_permutohedron_two_cap_actual_opposite_central_face_colors_20261008 (or the all-dimensional theorem's odd specialization) gives ACTUAL full x-rooted cube-geodesic direction orders pi_1,...,pi_s all in ONE common proper permutohedron face, with convex weights alpha_r>0, sum=1, satisfying:
- common EARLY/LATE one- or two-direction used-support cap S⊆{a,b} or complement(S)⊆{a,b};
- each REAL central ordered-three-face color q(pi_r)∈{0,1}, with sum_(q=0)alpha=sum_(q=1)alpha=1/2;
- for each j∈T, sum_r alpha_r 1_{j precedes i in pi_r}=1/2.

**THEOREM (quantitative opposite-color actual physical edge separation).** Among these <=n−1 genuine full-path packet witnesses there exist TWO ACTUAL orders pi_0,pi_1 satisfying ALL:
1. Their CENTRAL physical ordered-three-face windows have OPPOSITE actual NORI colors: q(pi_0)=0, q(pi_1)=1.
2. The unique physical i-edges visited by the two x-rooted full cube geodesics lie at projected cube positions v_i(pi_0),v_i(pi_1) whose Hamming distance, on coordinates in T alone, is at least
\[
\boxed{d_H(v_i(pi_0)|_T,v_i(pi_1)|_T)\ge \left\lceil\frac{n-3}{2}\right\rceil.}
\]
3. Their full permutations still lie in ONE common proper permutohedron face, and so share one actual EARLY or LATE used-direction CAP of at most two coordinate directions, chosen from the arbitrarily prescribed pair a,b. Hence their full geodesics meet at the common early/late physical cube vertex x XOR S. The pair cannot simply be related by full antipodal direction-order reversal, because their orders lie in a proper face together.

**PROOF.** Choose two INDEPENDENT random actual packet permutations P_0,P_1, conditioning P_0 to have actual central color0 and P_1 color1, and sampling within each color class with probabilities 2alpha_r (these sum to1 within each class). For each j∈T let
 u_j=Pr[j appears BEFORE i in P_0],
 v_j=Pr[j appears BEFORE i in P_1].
Because the two color classes each have total original weight1/2 and the unconditional coordinate-before-i probability is1/2,
 (u_j+v_j)/2=1/2, hence v_j=1-u_j.
The probability that the two independently chosen actual orders DISAGREE on the before-i indicator for coordinate j is therefore
 u_j(1-v_j)+(1-u_j)v_j
 =u_j^2+(1-u_j)^2
 \ge 1/2.
Sum these probabilities over all k=n−3 coordinates j∈T:
\[
\mathbb E\left[\#\{j∈T:\text{their orders place j on opposite sides of i}\}\right]\ge k/2.
\]
The Hamming distance of the two literal physical projected i-edge positions equals this disagreement count because each edge location bit is root bit x_j XOR its before-i indicator. The distance is integer-valued; therefore at least one ACTUAL opposite-central-color pair in the packet has distance >=ceil(k/2), proving item2. Items1 and3 hold for every such conditioned pair by construction and the common proper-face property. QED.

**TIGHTNESS OF THE AVERAGING LEMMA.** The inequality u²+(1-u)²>=1/2 is sharp at u=1/2, so one cannot improve this half-coordinate separation constant solely from the conditional central-color balance and individual coordinate-position balance; extra physical NORI compatibility is necessary.

**TOPOLOGICAL RELEVANCE.** For EVERY odd n>=7, EVERY root x and every prescribed three directions i,a,b, one can force TWO ACTUAL full antipodal geodesics sharing a tiny (size<=2) endpoint cap, with genuine opposite physical central ordered-face colors and physical i-edge positions differing on nearly half the remaining cube coordinates. This is a high-dimensional, root-mobile color-separation certificate suitable for a Hartman/Hex connector attempt. It does NOT ensure the two central physical faces intersect, that their orders give monochromatic complementary reversed-two-direction terminal tails, or that either whole path is one-switch. The global grand NORI forcing theorem remains open.

One must allow that physical seam square to move with the chosen permutohedron face: fixing its coordinate pair in advance destroys the required antipodal index. This is an exact limit of the current topological strategy.

## Geodesic pseudomanifolds and maximal-path exchanges

Let K_n be the simplicial complex whose vertices are the vertices of Q_n and whose facets are the unordered vertex sets of all full antipodal cube geodesics. A facet contains n+1 vertices, one at every distance from either endpoint. Each such path has a unique unordered antipodal endpoint pair, because distances along a geodesic strictly increase from its starting endpoint.

For one antipodal pair {x,bar x}, let K_x consist of facets with these endpoints. A full rooted geodesic is specified by a permutation of the n directions. Its internal vertices are the successive nonempty proper supports of that permutation, viewed relative to x. These chains form the barycentric subdivision of the boundary of the (n−1)-simplex on the direction set. Consequently

*Full Section composition: [source manuscript](nori_topological_path_exchanges.md).*

### Root-coupled geodesic pseudomanifold and Hartman connector topology

# Root-coupled geodesic pseudomanifold and Hartman connector topology

Root-coupled order complexes replace a single predetermined cube root by the parameter space of all physical rooted geodesics. This restores the antipodal involution absent from fixed-root selection, while introducing a new obligation: labels must still select paths whose ordered three-face windows can be glued. These foundational results establish the natural root-slide incidence topology, isolate its index, and provide explicit obstructions to the strongest selector and facet-lifting claims.

## The all-root antipodal-geodesic complex

Let \(n\ge2\). Define \(K_n\) to be the abstract simplicial complex on vertex set \(\mathbb F_2^n\) whose facets are the vertex sets of all full antipodal geodesics \(P=(v_0,\ldots,v_n)\). A directed geodesic and its ordinary reversal represent the same facet, so a facet represents an **unoriented** path and has two possible starting endpoints. Fix an antipodal unordered pair \(e_x=\{x,\bar x\}\), and let \(K_x\) be the subcomplex generated by the facets whose endpoints are \(e_x\).

**Theorem (root-coupled closed pseudomanifold).**
1. Every facet has exactly one antipodal pair, its endpoints. Consequently \(K_n=\bigcup_{e_x}K_x\) is a union of \(2^{n-1}\) rooted blocks, with \(2^{n-1}n!\) facets in total.
2. The link of \(e_x\) is the barycentric subdivision of the boundary of an \((n-1)\)-simplex:
\[
\operatorname{lk}_{K_n}(e_x)\cong \operatorname{sd}(\partial\Delta^{n-1})\cong S^{n-2}.
\]
Moreover \(K_x=e_x*\operatorname{lk}_{K_n}(e_x)\), an \(n\)-dimensional simplicial ball.
3. Every codimension-one face of \(K_n\) lies in exactly two facets, and the facet-adjacency graph is connected. Therefore \(K_n\) is a closed, connected, pure \(n\)-dimensional simplicial pseudomanifold (without an assertion that its lower-dimensional links are spheres).
4. Cube antipodality \(\tau(v)=\bar v\) induces a simplicial involution on \(K_n\). Its geometric fixed-point locus is exactly the set of midpoints of the \(2^{n-1}\) antipodal edges \(e_x\). The link of each such fixed midpoint is the suspension of \(\operatorname{sd}(\partial\Delta^{n-1})\), an \((n-1)\)-sphere on which \(\tau\) acts freely and PL-antipodally.

**Proof.** Write a path as \(v_j=x\oplus\{p_1,\ldots,p_j\}\), \(j=0,\ldots,n\), for a permutation \(p\) of the coordinate directions. Among its vertices, \(v_i,v_j\) are antipodal exactly when their Hamming distance \(j-i\) equals \(n\), so only \(v_0,v_n\) form an antipodal pair. There are \(n!\) distinct maximal chains for each unordered antipodal endpoint pair, establishing (1).

For fixed \(x\), identify the interior vertex \(x\oplus S\) with the nonempty proper subset \(S\subset[n]\). A face in the link of \(e_x\) is precisely an inclusion chain of these subsets, since the path is a monotone chain from \(x\) to \(\bar x\). This is the order complex of the proper part of the Boolean lattice, namely \(\operatorname{sd}(\partial\Delta^{n-1})\). Every facet containing the antipodal edge belongs to \(K_x\), proving the join identity and (2).

For (3), let \(P=(v_0,\ldots,v_n)\), with direction word \(p=(p_1,\ldots,p_n)\), and remove one vertex \(v_k\) from its facet. If \(1\le k\le n-1\), the remaining face still contains \(e_x\); its prefix-subset chain lacks only rank \(k\), which has exactly two fillings corresponding to exchanging \(p_k,p_{k+1}\). Hence this ridge has precisely two incident facets. If \(k=0\), its remaining vertices form the \((n-1)\)-edge subpath \(v_1,\ldots,v_n\), whose sole unused coordinate is \(p_1\). There are precisely two full geodesic completions: \(P\) itself, or
\[
P^+=(v_1,v_2,\ldots,v_n,\bar v_1),
\]
whose directions are \((p_2,\ldots,p_n,p_1)\). If \(k=n\), the two completions are \(P\) and
\[
P^-=(\bar v_{n-1},v_0,v_1,\ldots,v_{n-1}),
\]
with directions \((p_n,p_1,\ldots,p_{n-1})\). These are all completions, since the vertices of the given \((n-1)\)-edge subpath are linearly ordered by their mutual cube distances, and inserting an extra path vertex in the middle would force a two-step detour between adjacent vertices, impossible for a geodesic. This proves two-facet incidence. Adjacent transpositions connect all permutations for a fixed root; choosing \(p_1=a\) and applying the \(P^+\) move changes its root from \(x\) to \(x\oplus\{a\}\). Cube connectivity then connects all rooted chambers, establishing the pseudomanifold claim.

Cube antipodality sends a geodesic vertex set to another, so it is simplicial. A point fixed by \(\tau\) has a minimal supporting simplex invariant under vertex complementation. Every vertex in such a support must be accompanied by its antipode. Since a simplex contains at most one antipodal pair, a fixed point must lie in a single antipodal edge, necessarily its midpoint. Conversely, those midpoints are fixed. On the edge link, \(\tau\) sends each subset \(S\) to its complement \([n]\setminus S\); this is the free Coxeter-sphere involution. The link of an interior point of an edge is the suspension of the edge link, with the edge-transverse two poles interchanged by \(\tau\). This proves (4). \(\square\)

**Exact reversible chamber moves and color transport.** Let \(w(P)=(w_1,\ldots,w_{n-2})\) be the ordered-three-face color word of a directed path \(P\), and \(D(P)=\sum_{i=1}^{n-3}(w_i\oplus w_{i+1})\). The root slide \(P\mapsto P^+\) has
\[
w(P^+)=(w_2,\ldots,w_{n-2},b)
\]
for a single new color \(b\), and hence
\[
D(P^+)=D(P)-(w_1\oplus w_2)+(w_{n-2}\oplus b).
\]
The backward root slide analogously prepends one new color and drops the last. These formulas hold for *every* ordered-three-face coloring, with no antipodal or position-independence hypothesis, because the overlapping four-vertex windows are literally identical. The internal adjacent-swap move changes only \(v_k\), so it preserves every window not containing \(v_k\), changing at most four consecutive window colors.

**Hartman/topological significance and exact gap.** The dual graph of the pseudomanifold supplies an actual reversible root-coupled chamber-repair graph, with two types of elementary moves: adjacent direction swaps and endpoint root slides. Every full-dimensional simplex represents one actual antipodal geodesic (up to orientation); a final simplex-extraction step can therefore remain local to one chamber. However the involution on the full complex has fixed antipodal-edge midpoints. An ordinary free Borsuk--Ulam argument on \(K_n\) is unavailable: it must be formulated relative to those fixed points, e.g. on a punctured complex with local antipodal links, or via an explicit Sperner/connector carrier respecting the rooted blocks. In particular, no least-unreachable labeling with the needed boundary and monochromatic-component properties has yet been constructed.

## Root-slice fundamental cycle and exact top homology of the all-root geodesic complex

For \(n\ge2\), let \(K_n\) be the simplicial complex whose facets are the vertex sets of all complete antipodal geodesics of \(Q_n\). Let \(C=I^n_r\times I^n_s\) be the root–progress cube, with vertex map \(q(r,S)=r\oplus S\). Choose the \(2^{n-1}\) roots \(H=\{r:r_1=0\}\), one representative from each antipodal pair.

For each \(r\in H\), let \(\Sigma_r\) be the sum over \(\mathbb F_2\) of all top-dimensional Freudenthal simplices in the vertical face \(C_r=\{r\}\times I^n_s\). The map \(q\), although not simplicial on mixed root/progress chambers, is simplicial on each vertical Freudenthal simplex, and its image is exactly one facet of \(K_n\).

**Theorem (cross-root cancellation and fundamental class).** The chain
\[
Z=\sum_{r\in H}q_\#(\Sigma_r)
\]
is exactly the sum of all \(n\)-dimensional facets of \(K_n\), each appearing once. Every codimension-one face occurs twice in \(\partial Z\), so \(\partial Z=0\). Moreover,
\[
H_n(K_n;\mathbb F_2)\cong\mathbb F_2,
\]
generated by \([Z]\).

**Proof.** A facet of \(K_n\) has a unique antipodal endpoint pair \(\{x,\bar x\}\). Precisely one endpoint belongs to \(H\), and its direction permutation specifies a unique vertical Freudenthal simplex in that rooted slice. Thus each facet occurs exactly once in \(Z\). A ridge missing an intermediate geodesic vertex is contained in two facets with the same endpoint pair, corresponding to swapping adjacent progress directions; these cancel already within one vertical slice. A ridge missing an endpoint is contained in two facets with different endpoint pairs, related by a root slide (cyclically moving the omitted first or final direction); after applying \(q\), the corresponding boundaries from two different vertical slices cancel. Thus \(\partial Z=0\), and \(Z\ne0\).

Because the facet-adjacency graph of \(K_n\) is connected and each ridge belongs to exactly two facets, any \(n\)-cycle \(z=\sum a_P[P]\) satisfies \(a_P=a_{P'}\) for every pair of facets sharing a ridge. Connectivity forces all coefficients to equal one common bit. Therefore \(\ker\partial_n=\{0,Z\}\). As \(K_n\) has dimension \(n\), there are no \((n+1)\)-chains. Hence \(H_n(K_n;\mathbb F_2)\) has dimension one. \(\square\)

**Research significance.** In the doubled cube the selected vertical Freudenthal \(n\)-balls have separate geometric boundaries. After the physical XOR projection, the *endpoint* boundary terms cancel across distinct roots, precisely through root-slide square corridors. This is an exact mod-two chain-level analogue of Hartman-compatible reachability: a full global fundamental cycle exists only because local rooted boundaries glue coherently. A hypothetical proof of NORI could decorate these chains with compatible one-switch reachability data and derive a contradiction to nonzero degree. The new theorem supplies the uncolored chain topology; extending the boundary cancellation to colored, witness-preserving chains is the unresolved mathematical step.

TWO-ROW ROOT-TRANSPORT DICHOTOMY. In Q7 compare full direction orders p=(b,c,d,a,g,f,e) and q=(b,c,d,e,a,g,f). Both have windows T=(b,c,d) and U=(a,g,f). Match all initial coordinates except e across the two rows. Write A(t),B(t) for the respective ordered-face colors on T,U when their exterior e-bit is t (with all remaining exterior values held fixed). In p both windows see e-bit x, giving colors A(x),B(x). In q the T-window sees y and U sees 1+y, giving A(y),B(1+y). There exist x,y with both colors matching between rows if and only if A OR B is constant. Proof: if A constant choose x=1+y to match B; if B constant choose x=y to match A. If both are nonconstant, A(x)=A(y) forces x=y and B(x)=B(1+y) forces x=1+y, impossible. Thus every failed color transport through the specific Q7 table's two-row holonomy certifies simultaneous sensitivity of two disjoint ordered faces to the separating exterior coordinate e. This is a precise obstruction/exchange dichotomy; no grand closure follows without resolving the doubly sensitive case. FOUR-STATE ENDPOINT SURJECTIVITY: If both face colors are sensitive, write A(t)=a XOR t and B(t)=b XOR t. The two choices in row p yield pairs (a,b),(1+a,1+b); the two choices in row q yield (a,1+b),(1+a,b). Together these are all four pairs in F2^2. Thus the apparent two-row transport obstruction actually provides complete INDEPENDENT endpoint-color coverage across the four-state exchange square. A grand-closure proof must arrange a compatible interior colored connector across this square; endpoint freedom itself is sufficient.

These results give exact local and conditional constructions. No conclusion here asserts unrestricted high-dimensional grand closure.
