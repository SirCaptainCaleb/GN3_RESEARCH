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
Therefore \(b_k\ne b_{k+1}\) precisely when the two corresponding bits of \(x\) are equal. A permutation minimizing switches alternates the zero and one entries of \(x\) as long as possible; the surplus of the majority bit forces precisely \(\max\{0,|n-2w|-1\}\) neighboring equal pairs. \(\square\)

In this coloring, roots admitting a one-switch full geodesic have weights \(m-1,m,m+1\), while roots admitting a monochromatic full geodesic have weight \(m\). In particular every full geodesic from \(0^n\), regardless of direction order, has \(n-1\) switches. Root selection from \(0^n\) requires changing at least \(m-1\) root bits to find a one-switch path; bounded-radius root repair is insufficient.

#### Shared interpretation and limits

Article IX already establishes the antipodal cyclic-rotation identity for NORI1. Extend its \(n\)-bit geodesic word antiperiodically by \(w_{i+n}=1-w_i\). The \(n\) cyclic comparison bits have odd total \(D\), invariant under a root slide; the minimum ordinary switch count within that rotation orbit is \(D-1\). For the boundary problem the triple-bit word is periodic, its \(D\) is even, and cutting discards three comparisons rather than one.

Thus both full-strength targets can be formulated as **small cyclic variation of overlapping complete paths**. Adjacent exchanges alter only bounded intervals of the cyclic label word. Nevertheless strict local descent fails: at cube root \(0^n\), adjacent direction swaps and single root slides preserve the high variation \(n-1\), although elsewhere \(D=1\). A successful common selection theorem needs global root and ordering compatibility.

The NORI1 cyclic identity is already proved in Article IX; Theorems 1 and 2 and the plateau obstruction are detailed in research notes note_a31f3ced5651f1da607b547c, note_52fd24abbc3549954285b0a5, and note_4faa19538adf3c3d215f274d, all attached to Article IX. No unified long-path theorem is asserted.

#### Balanced lifts preserve a linear rootwise switch obstruction

Fix even \(d\ge2\), and take the parity coloring from Theorem 2,
\(f_i(x)=\sum_{j\ne i}x_j\pmod2\).
Its complementary paired lift \(C\) on \(Q_{2d}\) is
\[
C_i(x,y)=f_i(x),\qquad
C_{d+i}(x,y)=1+f_i(x),\qquad 1\le i\le d.
\tag{CV1}
\]
This is a legal antipodally odd vertex-balanced coloring: paired incident edge colors are complementary at every vertex. Every face retaining a union of complete free-direction pairs is balanced.

**Theorem (linear rootwise switch obstruction).** For every vertex \(z=(0^d,y)\) and every direction-simple path \(P\) rooted at \(z\), if \(P\) has length \(\ell\) and \(s\) changes in its temporal color word, then
\[
\boxed{\ell\le d+s+1.}\tag{CV2}
\]
In particular, every full antipodal geodesic rooted at \(z\) has at least \(d-1\) switches; a rooted direction-simple path with at most one switch has length at most \(d+2\). Therefore paths with \(o(d)\) switches from these roots have length at most \(d+o(d)\), while the cube dimension is \(2d\).

*Proof.* Delete from \(P\) every step in a new direction \(d+i\), leaving \(r\) steps in old directions. Since each old direction is used at most once and the old vertex begins at \(0^d\), immediately before the \(k\)-th remaining step precisely \(k-1\) old bits have been flipped and the bit of the current direction is still zero. Its color is therefore
\[
f_{i_k}(x)=k-1\pmod2.
\]
Thus the subsequence of old-step colors alternates \(0101\cdots\), and has \(r-1\) switches for \(r\ge1\). Deleting entries from a binary word cannot increase the number of switches, so \(r\le s+1\); this is also true for \(r=0\). The path uses at most \(d\) new directions, yielding \(\ell\le d+r\le d+s+1\). Setting \(\ell=2d\) proves the full-geodesic claim. \(\square\)

This gives arbitrarily large balanced, paired-face-balanced legal colorings in which no path beginning at a specified root can simultaneously be near spanning and have sublinear switch count. The underlying parity coloring still has monochromatic full geodesics at other roots. Hence existential root selection is indispensable in any asymptotic low-switch route to unrestricted NORI1.


**Sharpness of the full-geodesic rooted switch bound.** In the coloring (CV1), the minimum switch count among all full antipodal geodesics starting at \((0^d,y)\) is \(d-1\) for every even \(d\ge2\) and every \(y\). Thus
\[
\boxed{\min_{\pi\in S_{2d}}\operatorname{sw}_C(P((0^d,y),\pi))=d-1.}\tag{CV3}
\]

*Proof.* The lower bound is (CV2). For the upper bound traverse dimensions in the order
\[
1,d+1,\ 2,d+2,\ \ldots,\ d-2,2d-2,\quad
d-1,\ 2d,\ 2d-1,\ d.
\tag{CV4}
\]
When \(d=2\), the initial repeated pairs are absent and (CV4) is \((1,4,3,2)\). All \(2d\) directions occur once.

The old directions occur in increasing order and their temporal colors alternate, with old step \(i\) colored \(i-1\bmod2\). For \(1\le i\le d-2\), the new direction \(d+i\) immediately follows old step \(i\), at which point \(i\) old bits have been flipped, including bit \(i\). Its color is
\(1+f_i(x)=1+(i-1)=i\bmod2\),
which equals the color of old step \(i+1\).

After old step \(d-1\), the new direction \(2d\) has color
\(1+f_d(x)=1+(d-1)=0\bmod2\),
matching old step \(d-1\). The next step \(2d-1\) has color
\(1+f_{d-1}(x)=1+(d-2)=1\bmod2\),
matching the final old step \(d\). Every inserted new-direction edge therefore belongs to one of the two neighboring constant-color runs. No additional switches are created, and the full path has the \(d-1\) switches already present in its alternating old-direction subsequence. \(\square\)


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

#### Even-root path packets and two-row adjacent-swap transport

This establishes a full and economical state model for **arbitrary** antipodally odd cube-edge colorings. No affine, dependency, or low-switch hypotheses are assumed.

Fix \(n\ge2\), a dimension order \(\pi=(i_0,\ldots,i_{n-1})\), and put \(E_n=\{x\in\mathbb F_2^n:\sum_jx_j=0\pmod2\}\). For \(x\in E_n\) let \(W_x^\pi\in\{0,1\}^n\) be the edge-color word of the rooted geodesic that traverses \(\pi\) from \(x\). The **packet matrix** is \(W^\pi=(W_x^\pi)_{x\in E_n}\).

**Theorem 1 (path partition and packet realization).** For fixed \(\pi\), the rooted geodesics \(\{P_x^\pi:x\in E_n\}\) partition the undirected edges of \(Q_n\). A packet matrix \(W=(W_x(k))\) is the matrix of an antipodally odd coloring if and only if, for every \(k\) and even root \(x\),
\[
\boxed{W_{\rho_k(x)}(k)=1-W_x(k),\qquad
\rho_k(x)=\begin{cases}\bar x,&n\text{ even},\\
\bar x\oplus e_{i_k},&n\text{ odd}.
\end{cases}} \tag{PK1}
\]
For \(n\ge2\), every \(\rho_k\) is a fixed-point-free involution of \(E_n\). There are \(n2^{n-2}\) freely chosen packet entries, one per antipodal edge pair; there are no additional cross-column constraints.

*Proof.* Fix an undirected direction-\(i_k\) edge. Its two prospective roots in the order-\(\pi\) path family are its two endpoints toggled by the preceding prefix \(\{i_0,\ldots,i_{k-1}\}\). These roots differ in one bit, so precisely one belongs to \(E_n\). This proves partition and unrestricted realization of undirected-edge colorings.

If \(n\) is even, antipodal complementation preserves root parity and sends the entire path \(P_x^\pi\) to \(P_{\bar x}^\pi\), making corresponding edge colors opposite. If \(n\) is odd, the antipodal image of a direction-\(i_k\) edge of \(P_x^\pi\) lies on \(P_{\bar x\oplus e_{i_k}}^\pi\), traversed from its other endpoint. These are the two relations (PK1). Conversely, each edge and its antipode are represented in the partition by these two specified packet entries, so (PK1) is sufficient. The involutions have no fixed points since \(n\ge2\). \(\square\)

**Theorem 2 (synchronized two-row square exchange).** Let \(\pi'\) be obtained from \(\pi\) by swapping successive directions \(a=i_k,b=i_{k+1}\), and let \(z=e_a\oplus e_b\). For every even root \(x\), its new word is unchanged outside positions \(k,k+1\), while
\[
\boxed{
\bigl(W_x^{\pi'}(k),W_x^{\pi'}(k+1)\bigr)
=\bigl(W_{x\oplus z}^{\pi}(k+1),
       W_{x\oplus z}^{\pi}(k)\bigr).
}\tag{PK2}
\]
Thus each adjacent direction transposition acts on \(W\) by exchanging and reversing the two-letter blocks at the two packet rows \(x,x\oplus z\). The rows are paired by a fixed-point-free involution of \(E_n\). The complete family of packet matrices over all \(\pi\) is obtained from any one realized packet matrix by these deterministic reversible gates.

*Proof.* Let \(S\) be the direction prefix preceding \(a,b\), and \(v=x\oplus\mathbf1_S\). Path \(P_x^\pi\) uses the square route \(v\to v\oplus e_a\to v\oplus e_a\oplus e_b\). Path \(P_{x\oplus z}^\pi\) uses the opposite route \(v\oplus z\to v\oplus e_b\to v\). After swapping \(a,b\), the first rooted path uses the opposite route in reverse and hence reads the old second path's two colors in reverse order. The other positions read the same undirected edges as before. This proves (PK2). Every permutation arises from adjacent transpositions, and both sides of (PK2) are defined by the same underlying coloring. \(\square\)

**Corollary 3 (precise unrestricted closure reformulation).** NORI1 holds in dimension \(n\) if and only if **every** binary packet matrix satisfying (PK1), after some sequence of gates (PK2), has a row with at most one adjacent color change. The at-most-one-change condition suffices because the antipodal root-slide identity turns a one-change word into a monochromatic word. Conversely, if a coloring has a monochromatic geodesic from an odd root, then one cyclic root slide reaches an even root with at most one change; a monochromatic geodesic from an even root is already a witness. Thus all starting-root parities are represented.

**Theorem 4 (order-specific switch moment from local turns).** Let \(\epsilon(v)\) denote Hamming-weight parity. For two distinct directions \(a,b\), set
\[
D_{ab}^{p}
=\sum_{\epsilon(v)=p}
 \mathbf1\{c_a(v)\ne c_b(v\oplus e_a)\},\qquad p\in\{0,1\}.
\tag{PK3}
\]
Then \(D_{ab}^p=D_{ba}^p\). For every dimension order \(\pi=(i_0,\ldots,i_{n-1})\),
\[
\boxed{
\sum_{x\in E_n}\operatorname{sw}(W_x^\pi)
=\sum_{k=0}^{n-2}D_{i_k,i_{k+1}}^{\,k\bmod2}.
}\tag{PK4}
\]
Moreover,
\[
D_{ab}^{p}
=\sum_{\epsilon(v)=1-p}
 \mathbf1\{c_a(v)\ne c_b(v)\}. \tag{PK5}
\]
If \(n\) is odd and the coloring is antipodally odd, then \(D_{ab}^{0}=D_{ab}^{1}\). Consequently for odd \(n\), minimizing the average switch count over fixed direction orders is the minimum-weight Hamiltonian **path** problem on the complete direction graph with symmetric edge weights \(D_{ab}=D_{ab}^0\); for even \(n\), it is the analogous alternating-parity cost along the Hamiltonian path.

*Proof.* For the order-\(\pi\) path rooted at even \(x\), the vertex immediately before the successive \(a,b\) steps equals \(v=x\oplus\mathbf1_{\{i_0,\ldots,i_{k-1}\}}\), which ranges over every vertex of parity \(k\bmod2\) as \(x\) ranges over \(E_n\). The two encountered colors are \(c_a(v),c_b(v\oplus e_a)\), proving (PK4). Replacing \(v\) with \(v\oplus e_a\) gives (PK5), since an undirected direction-\(a\) edge has \(c_a(v\oplus e_a)=c_a(v)\). Replacing \(v\) with \(v\oplus e_a\oplus e_b\) shows that the direction-reversed comparison is the same, proving symmetry. If \(n\) is odd, antipodal complementation exchanges the two vertex parity classes and complements both incident edge colors, leaving their disagreement unchanged, so the two weights coincide. \(\square\)

**Corollary 5 (weighted order certificate).** If some direction order satisfies
\[
\sum_{k=0}^{n-2}D_{i_k,i_{k+1}}^{k\bmod2}<2^n,
\tag{PK6}
\]
then its \(2^{n-1}\) even-root packet words include a word with at most one switch and NORI1 holds for that coloring. Thus any hypothetical bad coloring must make every alternating-parity Hamiltonian path have cost at least \(2^n\). For odd \(n\), these are ordinary symmetric Hamiltonian-path costs with weights determined solely by bichromatic turns at cube vertices.

*Proof.* If every packet word had at least two switches, their sum would be at least \(2|E_n|=2^n\), contradicting (PK6). Apply Corollary 3. \(\square\)

**Scope.** The packet gate is a full realization model, not a local proof of existence: there are arbitrary antiperiodically constrained binary matrices with no constant row before applying gates. The new information is that all inter-order dependencies are captured by a universal, reversible two-row transport rule (PK2), and that its first-switch moment has the closed local-turn formula (PK4). No claim that the weighted Hamiltonian-path criterion always holds is made; for random legal colorings its costs are typically much larger than the threshold.


#### The universal incident-color metric and spanning-tree closure certificate

The even-root packet identity (PK4) has a simpler all-root version, valid for **arbitrary binary undirected edge colorings**, whether or not they are antipodally odd.

For every cube vertex \(v\) and direction \(i\), let \(c_i(v)\in\{0,1\}\) denote the color of the incident direction-\(i\) edge. For distinct directions \(i,j\), define
\[
d_c(i,j)=2^{-n}|\{v\in Q_n:c_i(v)\ne c_j(v)\}|,\qquad
d_c(i,i)=0. \tag{IM1}
\]
Each direction thus has a binary signature \((c_i(v))_{v\in Q_n}\); \(d_c\) is its normalized Hamming pseudometric. In particular it is symmetric, nonnegative, and satisfies the triangle inequality. It may identify two directions whose signatures agree.

**Theorem (fixed-order switch identity).** For every direction order \(\pi=(i_0,\ldots,i_{n-1})\) and uniform starting vertex \(X\in Q_n\),
\[
\boxed{\mathbb E_X\,\operatorname{sw}(W_X^\pi)
=\sum_{k=0}^{n-2}d_c(i_k,i_{k+1}).} \tag{IM2}
\]

*Proof.* Immediately before traversing successive directions \(a=i_k\) and \(b=i_{k+1}\), the current vertex is \(V=X\oplus\mathbf1_{\{i_0,\ldots,i_{k-1}\}}\). Uniformity of \(X\) makes \(V\) uniform over all vertices. The two edge colors are \(c_a(V)\) and \(c_b(V\oplus e_a)\). Changing variables to \(Y=V\oplus e_a\), the first color becomes \(c_a(Y)\), since direction-\(a\) edge colors ignore toggling bit \(a\), while the second becomes \(c_b(Y)\). Thus the expected switch indicator at the \(k\)-th boundary is \(d_c(a,b)\), independently of the other entries of \(\pi\). Sum over all boundaries. \(\square\)

This identity holds without antipodality and without the packet parity restriction. For antipodally odd \(c\), it is the average of the two parity-resolved packet identities (PK4).

**Corollary (metric Hamiltonian-path closure).** Suppose \(c\) is antipodally odd. If the complete weighted graph on the directions, with edge lengths \(d_c(i,j)\), has a Hamiltonian path of total weight less than two, then \(c\) admits a monochromatic full antipodal geodesic.

*Proof.* Use that Hamiltonian path as the direction order. By (IM2), the average over roots of the nonnegative integer number of switches is less than two. Some root has at most one switch, which root-slides to a monochromatic full path by antipodal oddness. \(\square\)

**Theorem (spanning-tree certificate).** Suppose \(c\) is antipodally odd. Let \(T\) be any spanning tree on the \(n\) directions, with weight \(w(T)=\sum_{ij\in T}d_c(i,j)\) and weighted tree diameter
\[
\operatorname{diam}(T)=\max_{u,v}\operatorname{dist}_T(u,v).
\]
If
\[
\boxed{2w(T)-\operatorname{diam}(T)<2,} \tag{IM3}
\]
then \(c\) has a monochromatic antipodal geodesic. In particular \(w(T)<1\) suffices.

*Proof.* Choose tree vertices \(u,v\) separated by a tree-diameter path. Traverse the tree starting at \(u\) and ending at \(v\), visiting every edge outside that path twice and every edge on it once. The walk has length \(2w(T)-\operatorname{diam}(T)\). List the tree vertices in their order of first encounter along this walk and shortcut repeated vertices, preserving the final destination when necessary. By the triangle inequality, one obtains a Hamiltonian path through all directions whose length is at most that of the walk. If (IM3) holds, apply the preceding corollary. \(\square\)

**Corollary (necessary metric expansion in a hypothetical counterexample).** If an antipodally odd coloring has no monochromatic full geodesic, then every Hamiltonian direction path has \(d_c\)-length at least two and, for every spanning tree \(T\),
\[
\boxed{2w(T)-\operatorname{diam}(T)\ge2.} \tag{IM4}
\]
In particular every minimum spanning tree has weight at least one. These are necessary conditions, not a contradiction.

**Scope and provenance of the idea.** The pseudometric is not imposed: it arises directly by viewing each direction's incident-edge colors as a binary vector. The identity (IM2) is an unrestricted combinatorial first-moment formula. It yields a polynomial-time sufficient certificate through tree weights, while the full Hamiltonian path minimization can be harder. Random or highly dispersed direction signatures can make all relevant path lengths much larger than two, so the metric criterion is not expected to prove NORI1 by itself. Its value is an explicit test connecting local vertex color structure to complete geodesic orders, with no unproved gluing step.


#### Permutation-reader witness abundance and a first-moment limitation

For any derangement \(\sigma\) of the direction set and any fixed signs \(\alpha_i\), the coloring \(c_i(x)=x_{\sigma(i)}+\alpha_i\) is antipodally odd. Fix any direction order \(\pi=(i_0,\ldots,i_{n-1})\). Its color word from root \(x\) is
\[
W_x^\pi(k)=x_{\sigma(i_k)}+\alpha_{i_k}
+\mathbf1_{\{\sigma(i_k)\text{ precedes }i_k\text{ in }\pi\}}
\pmod2.\tag{PR1}
\]
As \(x\) ranges over all roots this maps bijectively onto all binary length-\(n\) words, because \(\sigma\) permutes the root bits. Thus every fixed dimension order admits two monochromatic rooted paths, one of each color, and \(2n\) one-change-or-better rooted paths.

Nonetheless, the incident-color pseudometric of (IM1) satisfies \(d_c(i,j)=1/2\) for every distinct pair, since the two direction colors read different uniformly independent vertex bits. Every dimension-order Hamiltonian path therefore has weight \((n-1)/2\), which is at least two when \(n\ge5\). Thus the sufficient first-moment criterion does not detect witnesses even when every direction order has them. This is a rigorous limitation, not an obstruction to NORI1.

Averaging (IM2) over a uniformly random permutation, each unordered direction pair is consecutive with probability \(2/n\), so
\[
\mathbb E_{X,\pi}\operatorname{sw}(W_X^\pi)
=\frac2n\sum_{i<j}d_c(i,j)
=\frac{2^{1-n}}n\sum_{v\in Q_n}s_v(n-s_v),\tag{PR2}
\]
where \(s_v\) is the number of color-one edges incident with \(v\). This recovers the previously published global Petrie local-turn first moment. Formula (IM2) refines it order by order; the root-by-root word information in the packet gate (PK2) is strictly richer than either mean.
