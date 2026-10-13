# Article IX — Unification of NORI1 and Boundary Tournaments

## Common path symmetry and exchange compatibility

### The common path-symmetry problem

Let \(\mathcal P(X)\) be a family of admissible complete paths in a binary-colored instance \(X\), and let \(w(P)\) denote the color word of \(P\). Both antipodally odd edge colorings of the cube (NORI1) and ordinary reversal-odd boundary 3-tournaments admit an involution \(J\) satisfying
\[
w(JP)=\overline{\operatorname{rev}(w(P))}.
\]
For NORI1, \(J\) reverses a geodesic while complementing its vertices; for boundary tournaments, \(J\) reverses the vertex ordering.

The objective is one intrinsic class \(\mathcal C\), one common witness predicate \(W\), and one quantitative conjecture \(U(\mathcal C)\), with rigorous encodings and decoding theorems yielding both (i) a monochromatic antipodal geodesic for every NORI1 coloring and (ii) a Hamiltonian vertex-simple tight path on all original vertices whose consecutive triple colors change at most once for every ordinary boundary 3-tournament. Both consequences must follow from the same structural axioms. Reversal antisymmetry alone is insufficient: known higher-face colorings possessing such symmetry require unboundedly many color changes.

The principal investigation concerns overlapping complete paths. A NORI1 geodesic is specified by a root and a permutation of coordinate directions; exchanging adjacent directions replaces one two-edge square route, preserving every other edge. A boundary-tournament path is specified by an ordering of the original vertices; exchanging adjacent vertices preserves all ordered triples outside the affected local window. The associated permutation-exchange graphs satisfy commuting and braid relations. The problem is to find a shared, stronger law of local color compatibility that fails for the refuted higher-face constructions.

Path intersections must have compatible witnesses. In NORI1, monochromatic geodesics from antipodal roots meeting at a vertex concatenate because their coordinate supports are complementary. In a boundary tournament, concatenating tight paths additionally requires distinct original vertices and compatible ordered-triple seams. Every proposed topological carrier must support a rigorous decoding theorem.

This Subsection establishes the research problem and asserts no new unification conjecture or theorem. Subsequent work will develop the common class, structural lemmas, quantitative conjecture, specializations, and decisive obstructions.

**Correction: the full-strength common target.** The boundary-tournament conjecture is not merely a long monochromatic tight path. For a reversal-odd binary coloring \(b(u,v,w)\) of ordered distinct triples, the desired **boundary one-change Hamiltonian conjecture** asserts that there exists a permutation \(v_1,\ldots,v_n\) of *all* \(n\) original vertices such that the \(n-2\) consecutive triple colors
\[
b(v_1,v_2,v_3),\ b(v_2,v_3,v_4),\ldots,b(v_{n-2},v_{n-1},v_n)
\]
have **at most one color change**. The established monochromatic \(\Omega(\sqrt n)\) theorem is strictly weaker and does not resolve this spanning assertion. In particular, obtaining only an \(\Omega(\sqrt n)\) path from a proposed common conjecture is not a reduction of the full boundary target.

On the cubical side, the correct *equivalent relaxed witness* is a full \(n\)-edge antipodal geodesic with at most one change of its \(n\) **edge** colors; the following proves that this already yields the monochromatic NORI1 conclusion.

**Theorem (antipodal cyclic-rotation identity and odd-switch elimination; established in Article X).** Let \(c:E(Q_n)\to\mathbb F_2\) be an undirected edge coloring with \(c(\tau e)=1-c(e)\). If a full antipodal geodesic \(P\) uses directions \(d_1,\ldots,d_n\) in that order and has edge-color word \(w=(w_1,\ldots,w_n)\), put
\[
r=\sigma(P)=\sum_{i=1}^{n-1}\mathbf1_{\{w_i\ne w_{i+1}\}}.
\]
For every \(1\le j<n\), there is a full antipodal geodesic \(R_j(P)\) with directions \(d_{j+1},\ldots,d_n,d_1,\ldots,d_j\) and color word
\[
\boxed{w(R_j(P))=(w_{j+1},\ldots,w_n,1-w_1,\ldots,1-w_j).}\tag{R1}
\]
Its switch count obeys
\[
\boxed{\sigma(R_j(P))=
r-\mathbf1_{\{w_j\ne w_{j+1}\}}+
\mathbf1_{\{w_n=w_1\}}.}\tag{R2}
\]
Hence **every full geodesic with an odd positive number \(r\) of color changes can be rotated to a full geodesic with \(r-1\) changes**. Rotation at a color change preserves the switch count if \(r\) is even. In particular, the global minimum
\[
\boxed{\mu(c)=\min\{\sigma(P):P\text{ a full antipodal geodesic}\}}
\]
is even.

*Proof.* Concatenate \(P\), running from \(x\) to \(\tau x\), with the antipodal translate \(\tau P\), running from \(\tau x\) to \(x\). The resulting closed walk has color word
\[
(w_1,\ldots,w_n,1-w_1,\ldots,1-w_n)
\]
and direction word \((d_1,\ldots,d_n,d_1,\ldots,d_n)\). Its \(n\)-edge segment beginning after the first \(j\) moves uses every direction once, so it is an antipodal geodesic with word (R1).

The comparisons inside the two portions of (R1) are those of the original word except the one between \(w_j,w_{j+1}\). Complementation preserves internal color changes. The new seam comparison between \(w_n\) and \(1-w_1\) is a change if and only if \(w_n=w_1\), proving (R2). Since \(r\) is odd if and only if \(w_n\ne w_1\), an odd \(r\) permits a cut \(j\) at a change and then (R2) gives \(r-1\) changes. An odd positive minimum is therefore impossible. \(\square\)

**Corollaries.** (a) A full geodesic with one color change rotates to a monochromatic full geodesic. Thus NORI1's at-most-one-change and monochromatic formulations are equivalent. (b) A theorem guaranteeing a full geodesic with at most \(2s+1\) changes automatically guarantees one with at most \(2s\) changes. (c) A hypothetical failure of monochromatic NORI1 must have an even positive minimum, at least two changes.

**Provenance.** This restores the earlier general parity-reduction result, preserved in Article X, Subsection \`extremal_exterior_cube_rigidity_and_terminal_phase_separation\`, Lemma 1. The previous Article IX one-change lemma was only its first special case.

**Corrected reduction requirement.** A satisfactory unified conjecture must provide a *resource-spanning* path in both cases: rank \(n\) in the cube and rank \(n-1\) in the complete-graph root. It must bound cubical edge-color changes by one and boundary consecutive-triple-color changes by one. These are different observable layers (edges versus turns). Any claimed single Hamming-root formulation must explicitly define a common intrinsic switch-cost or word construction that reduces to both, and must not replace the boundary Hamiltonian conjecture with its established square-root consequence.

**Status of previous Hamming-root formulation.** The weaker conjecture \(\ell\ge\lceil\max\{k,\sqrt{k(q-1)}/2\}\rceil\) with all turn labels zero is a useful auxiliary path-growth problem, but it does **not** imply the boundary one-change Hamiltonian conjecture: for \(H(1,n)=K_n\), it guarantees only \(O(\sqrt n)\) resources, not the full \(n-1\). Its characterization as a complete unification of the two full-strength conjectures was an overstatement.

**Coherence and vertex-resource constraint for line-graph lifts.** A simple path in \(L(K_n)\) is only a sequence of distinct original edges with consecutive pairs intersecting: it need not be a coherently oriented original trail. Example: \(\{1,2\},\{1,3\},\{1,4\}\) cannot be traversed in that order. Even coherent trails can repeat original vertices: the quotient path \(\{1,2\},\{2,3\},\{1,3\}\) corresponds to \(1,2,3,1\). Therefore neither quotient-path simplicity nor cover-path simplicity ensures a simple original vertex word.

**Reconstruction lemma.** Let \(S(V)\) have ordered-pair states \((u,v)\), and directed forward arcs \((u,v)\to(v,w)\) for pairwise distinct \(u,v,w\). Project each state to the *resource* \(\rho(u,v)=\{u,v\}\in E(K_V)\). An arc-coherent state path \(s_1,\ldots,s_{n-1}\) is the lift of a permutation of all original \(n\) vertices if and only if the **multiset** of its \(n-1\) projected resources is a forest (equivalently, independent in a graphic matroid with repeated edges represented as parallel copies). Proof: forward coherence writes \(s_i=(v_i,v_{i+1})\). A repeated original vertex produces a nonempty closed segment of this original walk, which contributes a cycle or duplicate edge to the resource multigraph. Conversely, forest independence rules out all repetitions; the word has \(n\) distinct terms and is Hamiltonian. The path's \(n-2\) forward arcs are colored by the consecutive ordered triples. Note that deck reversal exchanges forward and backward orientations, so admissible paths require an oriented overlap language, not just the undirected covering graph. These two structural constraints are indispensable to any full-strength graph-cover unification.
