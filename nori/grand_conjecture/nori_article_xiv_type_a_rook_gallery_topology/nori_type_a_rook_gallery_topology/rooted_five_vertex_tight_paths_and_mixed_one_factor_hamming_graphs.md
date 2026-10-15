# Rooted five-vertex tight paths and mixed one-factor Hamming graphs

## A rooted tight-path lemma and mixed Hamming products

Let \(V\) have \(m\) vertices. A binary ordered-triple coloring is a function \(b(a,h,c)\in\mathbb F_2\) on pairwise distinct vertices; for the first theorem no reversal condition is imposed. A Hamilton tight path \(v_1,\ldots,v_m\) has triple word
\[
(b(v_1,v_2,v_3),\ldots,b(v_{m-2},v_{m-1},v_m)).
\]
The switch count is the number of unequal consecutive bits.

**Theorem 1 (rooted five-vertex lemma).** For \(3\le m\le5\), every ordered-triple coloring has a Hamilton tight path beginning at any specified vertex and whose triple word switches at most once. For \(m=5\), the theorem requires no reversal oddness.

*Proof.* The cases \(m\le4\) are immediate since the triple word has at most two entries. Let \(m=5\), and fix the first vertex \(a\). Suppose, toward contradiction, that every ordering \(a,p,q,r,s\) of the vertices has at least two switches. Its three-bit triple word must then alternate. In particular,
\[
b(a,p,q)\ne b(p,q,r),\qquad
b(p,q,r)\ne b(q,r,s).                                   \tag{1}
\]
Put \(U=V\setminus\{a\}\). For distinct \(p,q\in U\), let \(r,s\) be the remaining two members of \(U\). Comparing (1) for the orders \((a,p,q,r,s)\) and \((a,p,q,s,r)\), whose first triple is unchanged, shows
\[
b(p,q,r)=b(p,q,s).
\]
Define \(t(p,q)\) to be this common value. The second inequality of (1) becomes
\[
t(p,q)\ne t(q,r)\qquad(p,q,r\in U\ \text{distinct}).      \tag{2}
\]
For three distinct vertices \(p,q,r\in U\), apply (2) successively to \((p,q,r)\), \((q,r,p)\), and \((r,p,q)\). This asks three binary values \(t(p,q),t(q,r),t(r,p)\) to alternate around a cycle of odd length, a contradiction. \(\square\)

We next state a mixed-path model. Write \(H_{m,d}=K_m\square Q_d\), with vertices \((a,z)\), \(a\in V\), \(z\in\mathbb F_2^d\). Assume \(d\ge2\). For each \(a\), color the undirected edges of the \(Q_d\)-fiber by \(c_a\), subject to
\[
c_a(\bar e)=1-c_a(e).                                    \tag{3}
\]
For each \(z\), color the ordered triples in the \(K_m\)-fiber by \(b_z\), subject to
\[
b_z(c,h,a)=1-b_z(a,h,c),\qquad b_{\bar z}=b_z.             \tag{4}
\]
A **complete factor-block path** is a path traversing every binary dimension once and traversing a Hamilton ordering of the \(K_m\)-factor as one contiguous block. Its color word consists of one bit per binary edge and one bit per consecutive triple in the complete-graph block, taken in traversal order. Both the binary directions and the \(K_m\) vertices are used without repetition. Define the proposed **one-factor Hamming conjecture** to assert that every labeling (3)–(4) admits such a complete path whose combined word switches at most once.

At \(m=1\), the conjecture is the one-switch formulation of NORI1. At \(d=0\), omit the cube coloring and use a single reversal-odd \(K_m\)-coloring; the conjecture is the boundary one-switch Hamiltonian problem. These are limiting cases of the same complete-path model. The general conjecture remains open.

**Lemma 2 (two-dimensional cube).** Every antipodally odd edge coloring of \(Q_2\) has a monochromatic antipodal geodesic. Its antipodal translate is monochromatic in the opposite color.

*Proof.* Label the four consecutive edges of the square by \(\alpha,\beta,1-\alpha,1-\beta\), using antipodal oddness. If \(\alpha=\beta\), the first consecutive pair is monochromatic; otherwise \(\beta=1-\alpha\), and the second consecutive pair is monochromatic. Either pair forms an antipodal geodesic. Antipodal translation complements its two colors. \(\square\)

**Theorem 3 (mixed case).** For \(m\le5\) and \(d=2\), the one-factor Hamming conjecture holds. Indeed, the conclusion holds if each \(b_z\) is an arbitrary ordered-triple coloring satisfying only \(b_{\bar z}=b_z\), with no reversal oddness required.

*Proof.* Fix \(a\in V\). By Lemma 2, there is a monochromatic full cube geodesic in its \(Q_2\)-fiber, ending at some \(z\), and its antipodal translate is another such geodesic of the complementary color ending at \(\bar z\). By Theorem 1 (or the immediate shorter-word cases), \(b_z\) has a Hamilton ordering starting at \(a\) whose triple word has at most one switch. Since \(b_{\bar z}=b_z\), the same Hamilton ordering is available in both antipodal complete-graph fibers. If the triple word is nonempty, choose the cube geodesic whose color equals its first triple bit. Concatenate this cube geodesic with the Hamilton ordering in the corresponding terminal complete-graph fiber. There is no switch at their word boundary, and the Hamilton triple word contributes at most one switch. For \(m\le2\), the triple word is empty, so either cube geodesic suffices. The concatenated path uses each binary dimension once and each complete-graph vertex once. \(\square\)

**Corollary 4 (conditional higher-dimensional extension).** Suppose the NORI1 monochromatic full-geodesic conjecture holds for dimension \(d\ge2\). Then the one-factor Hamming conjecture holds on \(K_m\square Q_d\) for every \(m\le5\).

*Proof.* The NORI1 hypothesis supplies the monochromatic full geodesic in the fiber at a fixed \(a\). Its antipodal translate supplies the complementary color and ends at the antipode of the first terminal vertex. Apply the rooted theorem and the common-fiber identity \(b_{\bar z}=b_z\) as in Theorem 3. \(\square\)

The rooted lemma gives a nontrivial mixed existence theorem, while the general conjecture remains an open strengthening of both motivating conjectures. A complete proof for larger \(m\) would require selecting compatible binary and complete-graph portions; Theorem 1 supplies this compatibility for \(m\le5\).

## Gluing through common admissible starting vertices

For each \(z\in\mathbb F_2^d\), define
\[
S_z=\{a\in V:\ \text{some Hamilton ordering of }V\text{ beginning at }a
\text{ has at most one switch under }b_z\}.
\tag{5}
\]
The identity \(b_{\bar z}=b_z\) gives \(S_{\bar z}=S_z\).

**Theorem 5 (root-intersection gluing).** Suppose the NORI1 monochromatic full-geodesic conclusion holds in dimension \(d\), and the complete-graph fiber colorings satisfy (4). If
\[
\bigcap_{[z]\in\mathbb F_2^d/\langle z\mapsto\bar z\rangle}S_{[z]}\ne\varnothing,
\tag{6}
\]
then a complete factor-block path with at most one switch exists in \(K_m\square Q_d\), regardless of the antipodally odd cube-fiber edge colorings.

*Proof.* Select \(a\) in the intersection. Apply NORI1 in the cube fiber at \(a\) to obtain a monochromatic full cube geodesic \(P\), with color \(\varepsilon\), whose endpoint is \(z\). The antipodal translate \(\bar P\) is monochromatic with color \(1-\varepsilon\) and ends at \(\bar z\). By (6), some Hamilton ordering of \(V\) begins at \(a\) and has a triple word with at most one switch in \(b_z\). Since \(b_{\bar z}=b_z\), the same ordering has the same triple word at \(\bar z\). Choose \(P\) or \(\bar P\) according to whether its color equals the first triple bit; this gives a concatenation with no switch at the block boundary. The complete-graph triple word contributes at most one switch. The resulting path uses every cube dimension once and every complete-graph symbol once, proving the claim. If the triple word is empty, either cube geodesic works. \(\square\)

**Corollary 6 (common-order and majority conditions).** Under the NORI1 hypothesis of Theorem 5, each of the following implies its conclusion:

1. All \(b_z\) admit a single Hamilton ordering whose triple word has at most one switch in every fiber (the color words may differ).
2. Every \(b_z\) is obtained from one reversal-odd tournament \(b\) by complementing all its triple bits, with the complement choice constant on antipodal vertex pairs, and \(b\) has a one-switch Hamilton ordering.
3. If \(d=2\), the two sets \(S_{00}=S_{11}\) and \(S_{01}=S_{10}\) have nonempty intersection; in particular this holds whenever both contain more than \(m/2\) vertices.

*Proof.* In the first two cases the initial vertex of a common favorable ordering belongs to every \(S_z\). In the third, (6) is the pairwise intersection condition, and two subsets of an \(m\)-element set each of size exceeding \(m/2\) must intersect. Apply Theorem 5. \(\square\)

This isolates the remaining difficulty of the mixed conjecture: choosing cube-root and Hamilton starting vertex simultaneously when favorable rooted sets of the complete-graph fibers do not share a vertex. The explicit seven-vertex rooted counterexample in research note \`note_a9777ec5fa11e3d5fe120599\` shows that an individual \(S_z\) can be proper even for reversal-odd boundary tournaments. That example has \(|S_z|=6\) of seven vertices. Therefore, when \(d=2\), pairing that example with any second tournament possessing a one-switch Hamilton path automatically satisfies the intersection condition: reversing a one-switch Hamilton path gives a second favorable starting vertex, so the second rooted set has size at least two, and it must meet the six-element set.
