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


### Cyclic variation and root selection

#### Boundary one-switch Hamilton paths

Let \(b(a,b,c)\in\{0,1\}\) be a reversal-odd coloring of distinct ordered triples on \([n]\), \(n\ge4\). For a cyclic order \(\pi=(v_1,\ldots,v_n)\), index cyclically and define
\[
t_i=b(v_i,v_{i+1},v_{i+2}),\qquad
d_i=t_i\oplus t_{i+1},\qquad D(\pi)=\sum_{i=1}^n d_i.
\]
The cyclic switch count \(D\) is even.

**Theorem 1 (circular-switch criterion).** Of the \(n\) Hamilton paths obtained by cutting the cyclic order, the minimum binary switch count is
\[
\boxed{D(\pi)-\max_i(d_i+d_{i+1}+d_{i+2}).}
\]
Consequently a reversal-odd boundary tournament has a one-switch Hamilton path if and only if some cyclic order satisfies either \(D\le2\), or \(D=4\) with three consecutive \(d_i\)'s equal to one.

**Proof.** Cutting the cycle retains \(n-2\) consecutive triple bits, hence \(n-3\) consecutive comparisons \(d_i\). The omitted comparisons occupy three consecutive positions, so minimizing the retained sum gives the formula. As \(D\) is even, the minimum is at most one precisely in the two stated cases. \(\square\)

The \(D=4\) case cannot be discarded. When \(n=4\), let \(b(a,b,c)\) be the inversion parity of the four-letter ordering \((a,b,c,d)\), with \(d\) the omitted letter. Reversing \((a,b,c)\) changes parity; rotating a four-letter cyclic ordering changes parity too. Thus every circular triple word alternates, with \(D=4\), but a Hamilton path has only two triple labels and automatically at most one switch.

#### Rooted spectrum in NORI1

For even \(n=2m\ge4\), define an undirected cube-edge coloring by
\[
c_i(x)=\sum_{j\ne i}x_j\pmod2,\qquad \{x,x\oplus e_i\}\in E(Q_n).
\]
This is well defined because it ignores bit \(x_i\), and \(c_i(\bar x)=1-c_i(x)\) because \(n-1\) is odd.

**Theorem 2 (root-fiber minimum).** If the starting cube vertex \(x\) has Hamming weight \(w\), then
\[
\boxed{\min_{\pi\in S_n}\operatorname{sw}(P(x,\pi))
=\max\{0,|n-2w|-1\}.}
\]

**Proof.** Put \(r=\sum_jx_j\pmod2\). The \(k\)-th edge in direction order \(\pi\) has bit
\[
b_k=r+x_{\pi_k}+k-1\pmod2.
\]
Therefore \(b_k\ne b_{k+1}\) precisely when the two corresponding bits of \(x\) are equal. A permutation minimizing switches alternates the zero and one entries of \(x\) as long as possible; the surplus of the majority bit forces exactly \(\max\{0,|n-2w|-1\}\) neighboring equal pairs. \(\square\)

In this coloring, roots admitting a one-switch full geodesic have weights \(m-1,m,m+1\), while roots admitting a monochromatic full geodesic have weight \(m\). In particular every full geodesic from \(0^n\), regardless of direction order, has \(n-1\) switches. Root selection from \(0^n\) requires changing at least \(m-1\) root bits to find a one-switch path; bounded-radius root repair is insufficient.

#### Shared interpretation and limits

Article IX already establishes the antipodal cyclic-rotation identity for NORI1. Extend its \(n\)-bit geodesic word antiperiodically by \(w_{i+n}=1-w_i\). The \(n\) cyclic comparison bits have odd total \(D\), invariant under a root slide; the minimum ordinary switch count within that rotation orbit is \(D-1\). For the boundary problem the triple-bit word is periodic, its \(D\) is even, and cutting discards three comparisons rather than one.

Thus both full-strength targets can be formulated as **small cyclic variation of overlapping complete paths**. Adjacent exchanges alter only bounded intervals of the cyclic label word. Nevertheless strict local descent fails: at cube root \(0^n\), adjacent direction swaps and single root slides preserve the high variation \(n-1\), although elsewhere \(D=1\). A successful common selection theorem needs global root and ordering compatibility.

The NORI1 cyclic identity is already proved in Article IX; Theorems 1 and 2 and the plateau obstruction are detailed in research notes note_a31f3ced5651f1da607b547c, note_52fd24abbc3549954285b0a5, and note_4faa19538adf3c3d215f274d, all attached to Article IX. No unified long-path theorem is asserted.

### Fixed-order freedom and coupled root-order selection

#### The root-fiber realization theorem

**Theorem 1.** Fix \(n\ge2\) and a permutation \(\pi=(i_1,\ldots,i_n)\) of the cube dimensions. For every \(k\), independently choose any function \(F_k:\mathbb F_2^n\to\mathbb F_2\) satisfying
\[
F_k(x\oplus e_{i_k})=F_k(x),
\qquad
F_k(\bar x)=1-F_k(x).
\]
There is a unique antipodally odd coloring \(c\) of the undirected edges of \(Q_n\) such that, for every root \(x\), the \(k\)-th edge of the full \(\pi\)-geodesic beginning at \(x\) has color \(F_k(x)\).

**Proof.** Set \(S_{k-1}=\{i_1,\ldots,i_{k-1}\}\) and define
\[
c_{i_k}(y)=F_k(y\oplus\mathbf1_{S_{k-1}}).
\]
The first condition makes this independent of the selected endpoint of the dimension-\(i_k\) edge. The second gives antipodal oddness. The \(k\)-th edge of the \(\pi\)-geodesic from \(x\) begins at \(y=x\oplus\mathbf1_{S_{k-1}}\), so its bit is \(F_k(x)\). These formulas specify every edge of the cube and prove uniqueness. \(\square\)

Thus a prescribed dimension order imposes no cross-position constraints among the independently selected rooted edge-bit functions; the missing dependencies appear only when comparing distinct direction orders on shared cube edges.

#### A fixed-order obstruction despite global closure

**Theorem 2.** For every \(n\ge4\) and any prescribed direction order \(\pi\), there is an antipodally odd NORI1 edge coloring for which
\[
\min_{x\in Q_n}\operatorname{sw}(P(x,\pi))=n-2,
\]
yet a monochromatic full antipodal geodesic exists.

**Proof.** Rename the prescribed order \(1,\ldots,n\), and color the undirected edges by
\[
c_1(x)=x_2,\qquad c_k(x)=x_1\oplus(k\bmod2)\quad(2\le k\le n).
\]
Each \(c_k\) ignores \(x_k\), and complementing all \(n\) vertex bits reverses every color. On the prescribed order, after the first step the remaining \(n-1\) bits alternate, independently of the root. Thus the \(n-2\) internal comparisons among them all switch; the first comparison can be made equal by selecting the root, giving equality.

For closure choose a root with \(x_1=0,x_2=1\). Traverse all odd-indexed dimensions in \(\{2,\ldots,n\}\), then direction \(1\), then all even-indexed dimensions. The pre-pivot edges have bit \(1\), the pivot bit is \(x_2=1\), and the post-pivot edges also have bit \(1\). \(\square\)

#### Exponential rarity of successful permutation orders

**Theorem 3.** For every \(n\ge4\), put \(N=n-1\). There is an antipodally odd NORI1 edge coloring admitting a monochromatic full geodesic such that the fraction of dimension permutations admitting *any* root with at most one switch is at most
\[
\boxed{\frac{N}{\binom N{\lfloor N/2\rfloor}}}
=O(N^{3/2}2^{-N}).
\]

**Proof.** Modify the preceding coloring to \(c_1(x)=x_2\) and \(c_k(x)=x_1\oplus\alpha_k\) for \(k\ge2\), where \(\alpha_2=0\) and among the \(N\) bits \(\alpha_2,\ldots,\alpha_n\), precisely \(p=\lfloor N/2\rfloor\) are \(1\) and \(q=N-p\) are \(0\). Choosing \(x_1=0,x_2=1\) and following all \(\alpha=1\) dimensions, then dimension \(1\), then all \(\alpha=0\) dimensions gives a color-\(1\) full geodesic.

For any permutation \(\sigma\), delete direction \(1\) and read the resulting ordered sequence \(\beta\) of \(\alpha\)-bits. All edges before direction \(1\) have colors \(x_1\oplus\alpha_k\); all those after it have colors \(1\oplus x_1\oplus\alpha_k\). Thus every transition within \(\beta\) forces a corresponding switch on the full path, except perhaps the one comparison interrupted by direction \(1\). Hence
\[
\min_x\operatorname{sw}(P(x,\sigma))\ge T(\beta)-1,
\]
where \(T(\beta)\) counts changes between consecutive \(\beta\)-bits. A one-switch path therefore requires \(T(\beta)\le2\).

Among the \(\binom Np\) binary words with \(p\) ones and \(q\) zeros, precisely \(N\) have at most two switches. Two have one switch; among words with two switches, there are \(p-1\) of the form \(1^a0^q1^{p-a}\) and \(q-1\) of the form \(0^a1^p0^{q-a}\). A uniform random permutation of dimensions induces a uniform balanced \(\beta\), so the claimed bound follows. \(\square\)

#### Boundary comparison: sparse winning permutations

**Theorem 4.** On ordered triples of distinct vertices \(a,b,c\in[n]\), define \(b(a,b,c)=\mathbf1_{\{a<c\}}\). It is reversal odd and has a monochromatic Hamilton path \(1,2,\ldots,n\). Nevertheless, if \(k=\lceil n/2\rceil\) and \(\ell=\lfloor n/2\rfloor\), a uniformly random Hamilton ordering has a triple-color word with at most one switch with probability at most
\[
\boxed{\frac{2^k-2}{k!}\cdot\frac{2^\ell-2}{\ell!}},
\]
which decays faster than exponentially.

**Proof.** Its consecutive triple labels compare \(v_i\) with \(v_{i+2}\). The odd-position word \(v_1,v_3,\ldots\) and even-position word \(v_2,v_4,\ldots\) have independent uniform relative orders. If the full interleaved comparison word has at most one switch, each of those two subsequences is monotone or changes monotonicity once. For \(h\ge2\), precisely \(2^h-2\) relative permutations have this property: increasing-then-decreasing permutations are determined by the set preceding their maximum (\(2^{h-1}\) choices), decreasing-then-increasing permutations by the set preceding their minimum (another \(2^{h-1}\)), and the two monotone permutations have been counted twice. Multiply the two independent upper probabilities. \(\square\)

#### What this establishes for the common problem

Both motivating families can possess a good complete path while suitable dimension or vertex orders are rare. Their restrictions to a *frozen order* allow extensive independent prescriptions, so neither choosing a root after freezing the order nor selecting a random order is a universal method. A common topological selection theorem must exploit the *overlaps among different complete permutations*, together with root changes in NORI1; its proof cannot rely on favorable behavior of a predetermined chamber. This is an obstruction to proposed selection methods, not an existence proof of the full common conjecture.

Research note with expanded comparisons: note_d7af56d7da1b8654fcf6a404.
