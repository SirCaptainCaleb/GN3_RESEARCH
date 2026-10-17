# Antipodal multifacet bridge and seven-coordinate universality

# Antipodal multifacet bridging: an  localization theorem for unrestricted NORI1

## Statement and historical context

Let \(k\ge2\). Define \(B_k\) to be the **Leader–Long/Feder–Subi geodesic 2-cp assertion in dimension \(k\)**:

> Every arbitrary binary coloring \(d\) of the *undirected  edges* of \(Q_k\) admits a **full antipodal geodesic** whose edge-color sequence changes at most once.

Unlike NORI1, \(d\) need not satisfy any antipodal relation. For integers \(n>k\), and a fixed \(k\)-set \(S\subseteq[n]\), define \(P_{n,S}\) to be the **full geodesic partial-color prescription assertion**:

> For every antipodally odd coloring \(c\) of the undirected  edges of \(Q_n\), and every target \(t\in\mathbb F_2^S\), there exist a  root \(x\) and a permutation \(p\) of **all \(n\) directions** such that the full antipodal geodesic \(P(x,p)\) traverses its unique edge in each direction \(i\in S\) with color precisely \(t_i\). The colors in the other \(n-k\) directions are unrestricted.

This is an  property of all legal NORI1 colorings, not a condition on affine or direction-only subclasses.

**Theorem 1 (multifacet bridge equivalence).** For every \(k\ge2\), every \(n>k\), and every fixed \(k\)-set \(S\subseteq[n]\),
\[
\boxed{\quad B_k\quad\Longleftrightarrow\quad P_{n,S}.\quad}
\tag{1}
\]
In particular, the property that *every* legal antipodally odd -edge coloring in *any one larger dimension* realizes all prescribed colors on *one specified set of \(k\) directions* is equivalent to the arbitrary-color \(k\)-cube 2-cp geodesic assertion.

The implication \(B_k\Rightarrow P_{n,S}\) uses **all** \(n-k\) exterior directions as a single antipodal bridge between opposite  \(k\)-faces; no colors along the bridge need to be specified.

## Proof of the forward implication

Assume \(B_k\). Fix \(n>k\), \(S\), a legal  antipodally odd edge coloring \(c\) of \(Q_n\), and an arbitrary target \(t=(t_i)_{i\in S}\).

Identify \(Q_n=Q_S\times Q_D\) with \(D=[n]\setminus S\ne\varnothing\); write a cube vertex as \((u,z)\). Fix an **arbitrary** exterior vertex \(z\in Q_D\). On the *lower  \(S\)-face* \(Q_S\times\{z\}\), define an arbitrary undirected-edge coloring
\[
d_i(u):=c_i(u,z)\oplus t_i,\qquad i\in S.
\tag{2}
\]
This is a legal  \(k\)-cube edge coloring because \(c_i(u,z)=c_i(u\oplus e_i,z)\); **no** antipodal oddness is assumed for \(d\).

By \(B_k\), there exists a full antipodal geodesic \(R\) of \(Q_S\) whose \(d\)-color word has at most one change. Reverse its traversal if needed so its word is \(0^a1^{k-a}\), with \(0\le a\le k\). Write
\[
R:\ u_0\xrightarrow{U}u_a\xrightarrow{V}\bar u_0
\tag{3}
\]
where \(U\) and \(V\) denote ordered, disjoint lists of \(S\)-directions whose union is \(S\), with all edges of \(U\) having \(d\)-color 0 and all edges of \(V\) having \(d\)-color 1. Empty \(U\) and \(V\) are permitted.

Now construct a **full \(n\)-direction cube geodesic**, starting at \((u_a,z)\):

1. Traverse the \(U\)-edges in reverse order inside the lower  facet, moving \((u_a,z)\to(u_0,z)\).
2. Traverse *every* direction of \(D\) precisely once, in any order, moving \((u_0,z)\to(u_0,\bar z)\).
3. Follow the **reverse of the \(Q_S\)-antipodal image of the \(V\)-suffix** from (3), inside the upper  facet, moving \((u_0,\bar z)\to(\bar u_a,\bar z)\).

All \(n\) directions are used precisely once, so the constructed path is a full antipodal geodesic. On its \(U\)-edges, the lower-facet formula (2) and the undirected reversal of the 0-block give  \(c\)-color \(t_i\). On its \(V\)-edges, each upper-facet edge is the **global cube antipode** of the corresponding lower-facet  edge of \(R\) (after projecting the \(Q_S\)-antipodal reversal); its  \(c\)-color is therefore the complement of the original lower color \(d_i\oplus t_i=1\oplus t_i\), namely \(t_i\). The intervening \(D\)-edges have arbitrary colors, which do not affect the required prescription. Thus \(P_{n,S}\) holds. \(\square\)

## Proof of the reverse implication

Assume \(P_{n,S}\). Let \(d\) be **any** arbitrary binary coloring of the undirected edges of \(Q_k\). Pick a distinguished exterior direction \(s\in D=[n]\setminus S\). Define a  edge coloring \(c\) of \(Q_n\) using \(d\), with \(u\in Q_S\), \(z\in Q_D\), and one distinguished original coordinate \(i_0\in S\):

\[
c_i(u,z)=
\begin{cases}
d_i(u),&z_s=0,\\
1\oplus d_i(\bar u),&z_s=1,
\end{cases}
\qquad(i\in S),\tag{4}
\]
\[
c_j(u,z)=u_{i_0}\quad(j\in D).\tag{5}
\]
The main \(S\)-edge colors are  because \(d_i\) is invariant under flipping its free \(i\)-bit; the exterior \(j\)-edge color in (5) is independent of its free \(j\)-bit. Antipodality of the *full* \(Q_n\) interchanges the two \(s\)-facets and complements the main colors in (4). It also complements \(u_{i_0}\), verifying \(c_j(\bar u,\bar z)=1\oplus c_j(u,z)\) for each \(j\in D\). Thus \(c\) is a legitimate antipodally odd -edge coloring of \(Q_n\). The colors in (4) depend on exterior coordinates **only through \(z_s\)**.

By \(P_{n,S}\), choose a full antipodal cube geodesic whose edge color is 0 in every direction of \(S\). Reverse its traversal if needed so that the unique \(s\)-step crosses from \(z_s=0\) to \(z_s=1\). Let \(U\) be its ordered \(S\)-direction list before the \(s\)-step, and \(V\) its ordered \(S\)-direction list after the \(s\)-step. Ignore moves in the other exterior directions. The projected \(S\)-word is \(U,V\), a permutation of all \(k\) directions. It begins at some \(u_0\), reaches some \(u_a\) after \(U\), and ends at \(\bar u_0\) after \(V\).

On the \(U\) edges, (4) says precisely \(d\)-color 0. On the \(V\) edges, (4) says precisely that the **\(Q_S\)-antipodal image of the projected \(V\)-suffix** carries \(d\)-color 1. Therefore the projected \(Q_S\) path obtained by reversing \(U\), and then following the reverse \(Q_S\)-antipodal image of \(V\),
\[
u_a\xrightarrow{U^{\mathrm{rev}}}u_0
\xrightarrow{\overline{V}^{\,\mathrm{rev}}}\bar u_a,
\tag{6}
\]
uses every \(S\) direction precisely once and changes \(d\)-color **at most once**: the first block has color 0 and the second block color 1. (When one block is empty, it is monochromatic.) This is a full antipodal \(Q_k\)-geodesic. It proves \(B_k\). \(\square\)

**Additional switch-count transfer.** The forward proof works without assuming the \(d\)-geodesic has only one change. Given an arbitrary \(d\)-antipodal geodesic with \(r\ge1\) switches, choose the \(U|V\) split at **any one of its color changes**. Reversing the first block preserves its internal switch count; antipodally reversing and complementing the second block preserves its internal switch count; the chosen seam changes from a switch to a match. Hence the selected-direction color word on the resulting \(Q_n\) full geodesic, compared with any prescribed directionwise target \(t\), has precisely **\(r-1\)** switches. For \(r=0\), place all \(S\)-directions on one side of the exterior bridge; the selected word remains constant. Thus any upper bound on switches in arbitrary \(k\)-cube colorings transfers to a one-smaller bound for the **selected** direction word of every larger NORI1 coloring (not to the full \(n\)-edge color word, whose exterior bridge colors are uncontrolled).

## Consequence: universal seven-direction color prescription

**Corollary 2 (all \(n\): every seven selected colors are realizable).** For every dimension \(n\ge8\), every legal antipodally odd -edge coloring of \(Q_n\), every set \(S\subseteq[n]\) of size \(k\le7\), and every prescribed color vector \(t\in\mathbb F_2^S\), there exists a **full \(n\)-edge antipodal geodesic** whose \(k\) selected edges have **precisely** the specified colors.

**Proof.** The geodesic Norine conjecture \(A_m\) has been established for **every \(m\le8\)**, including the SAT-certified case \(m=8\) in Kirchweger–Peitl–Subercaseaux–Szeider (2025), *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT*, arXiv:2511.08386, Theorem 1 (the paper explicitly states the *geodesic* conjecture in dimension eight). Leader and Long (2014), *Long geodesics in subgraphs of the cube*, Proposition 3.6 in arXiv:1301.2195v1, proved \(A_{k+1}\Rightarrow B_k\). Thus \(B_k\) holds for \(k\le7\). Theorem 1 above then gives \(P_{n,S}\) for every \(n>k\), as required. \(\square\)

For \(n\le8\), the stronger statement that **all \(n\) prescribed direction colors** can be realized also follows directly from the established full-geodesic result \(A_n\): independently XOR the desired \(t_i\) into each direction's edge color, preserving undirectedness and oddness, then use \(A_n\). Consequently, for **every** \(n\ge2\), arbitrary prescribed colors on any set of size \(\min(n,7)\) are simultaneously attainable, and in dimensions at most eight all \(n\) colors are attainable.

**Boundary of the result.** This uses a previously proved finite-dimensional geodesic theorem and an  new dimension-free bridge implication. It is not a proof of the full NORI1 conjecture in arbitrary dimension; for eight selected directions in \(n\ge9\), the bridge equivalence reduces the question **precisely** to \(B_8\), equivalently to the known Leader–Long dimensional challenge \(A_9\Rightarrow B_8\) in one direction. The argument makes no claim about *ordinary boundary 3-tournaments*: it uses an edge (one-window) color seam, whereas ordered-three-face paths acquire two extra seam windows.

**Primary sources and scope checks.**
- Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33; https://arxiv.org/abs/1301.2195 .
- Markus Kirchweger, Tomáš Peitl, Bernardo Subercaseaux, Stefan Szeider, *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT* (2025), arXiv:2511.08386, specifically Theorem 1 and the separate SAT geodesic encoding \(\Psi_n\); https://arxiv.org/html/2511.08386 .
- Tomáš Feder and Carlos Subi, *On hypercube labellings and antipodal monochromatic paths*, Discrete Applied Mathematics 161 (2013), 1421–1426 (original unrestricted-edge 2-cp *path* conjecture; the geodesic strengthening is due to Leader–Long).

**Unification scope:** This established NORI1 localization theorem is retained as prior mathematics, not an independent current research target. A later NORI1 paired-start toy theorem, originally published in composition v2, is preserved with its complete proof in note `note_antipodal_paired_start_nori1_toy_unification_probe`; no transfer to ordinary boundary tournaments has been established.


## Near-spanning one-change paths: an unrestricted dimension-uniform closure equivalence

Let \(d\) be an arbitrary binary edge coloring of \(Q_n\), with **no antipodal condition**. Define \(L_1(d)\) to be the maximum length of a direction-simple path (using each direction at most once) whose edge-color word has at most one change. The full-length condition \(L_1(d)=n\) is exactly the arbitrary-color geodesic two-color-path assertion \(B_n\).

**Theorem (asymptotic one-change closure equivalence).** The following assertions are equivalent:

1. Unrestricted antipodally odd NORI1 holds in every dimension.
2. \(B_n\) holds for arbitrary two-edge-colorings of \(Q_n\), for every dimension \(n\).
3. A uniform function \(f(n)=o(n)\) exists such that every arbitrary coloring \(d\) of \(Q_n\) satisfies
   \[
   \boxed{L_1(d)\ge n-f(n).}\tag{NS1}
   \]
4. Some fixed \(C\) exists such that every arbitrary coloring \(d\) of \(Q_n\) satisfies \(L_1(d)\ge n-C\).

Thus a universal \(n-O(\sqrt n)\), \(n-O(\log n)\), or bounded-deficit **one-change** direction-simple path theorem for arbitrary two-edge-colorings would prove NORI1 in every dimension.

*Proof.* To obtain \(1\Rightarrow2\), fix an arbitrary colored \(Q_k\). The already established multifacet bridge theorem gives \(B_k\Longleftrightarrow P_{k+1,S}\), where \(S\) is the \(k\)-set of horizontal directions in a legal antipodally odd coloring of \(Q_{k+1}\). Under NORI1, every directionwise prescribed \(k+1\)-bit profile occurs: reverse all edge colors in each selected direction wherever the target bit is one, apply NORI1, then if necessary antipodally translate a monochromatic-one full path to a monochromatic-zero path. Hence \(P_{k+1,S}\) holds, and the bridge theorem yields \(B_k\).

For \(2\Rightarrow1\), apply \(B_n\) directly to a legal antipodally odd edge coloring of \(Q_n\). This gives a full antipodal geodesic with at most one color change. If it has one change, cyclically slide the root past that change. Antipodal oddness complements the moved prefix colors and makes the resulting full antipodal geodesic monochromatic, as proved in the penultimate-length/root-rotation lemma above. Thus NORI1 holds.

Clearly 2 implies 3 and 4. Conversely, if 2 fails, select a fixed arbitrary colored \(Q_d\) with \(L_1(a)\le d-1\). Form its \(h\)-fold independent Cartesian power \(a^{\boxtimes h}\) on \(Q_{hd}\). A direction-simple path with at most one change in this product projects onto each factor as a direction-simple path whose color word, being a subsequence of the full word, also has at most one change. Each factor therefore contributes at most \(d-1\) moves. Consequently
\[
\boxed{L_1(a^{\boxtimes h})\le h(d-1)=hd-h.}\tag{NS2}
\]
The loss of \(h=n/d\) moves is linear in the ambient dimension \(n=hd\), violating 3 and 4. Therefore either 3 or 4 forces 2. This proves all equivalences. \(\square\)

**Significance and calibration.** This closure-equivalent asymptotic assertion concerns **arbitrary**, potentially imbalanced, nonlinear two-edge-colorings of the cube. The requirement of at most one color change is indispensable: uniformly near-spanning *monochromatic* direction-simple paths are impossible for arbitrary colorings with half the directions permanently assigned to each color. Conversely, the full geodesic 2-cp assertion is sufficient for NORI1 because antipodal root rotation eliminates a single change. The tensor-power argument shows that any genuinely sublinear loss in the weaker partial-path statement automatically collapses to the exact full geodesic theorem. This is a possible approach through an approximate path theorem rather than an induction through individual dimensions.



### Two-phase trace tensorization and multiplicative counterexamples

For any arbitrary undirected binary edge coloring \(d\) of \(Q_q\), let \(R_d\) and \(B_d\) be its color-zero and color-one adjacency matrices, \(P_q\) the antipodal permutation, and define the nonnegative numbers
\[
M_{q,k}(d)=\operatorname{tr}(P_qR_d^kB_d^{q-k}),
\qquad 0\le k\le q.
\tag{TS1}
\]
The Leader--Long full one-change property holds for \(d\) if and only if some \(M_{q,k}(d)\) is positive, because every full path changing from one to zero can be reversed.

**Theorem (binomial two-phase tensorization).** If \(d=d_1\boxtimes d_2\) is an independent Cartesian product of arbitrary binary edge colorings on \(Q_a,Q_b\), with \(N=a+b\), then
\[
\boxed{
M_{N,k}(d)=
\sum_{r=\max(0,k-b)}^{\min(a,k)}
\binom{k}{r}\binom{N-k}{a-r}
M_{a,r}(d_1)M_{b,k-r}(d_2).
}\tag{TS2}
\]
Thus a product coloring admits a full one-change antipodal geodesic if and only if *both* factors admit such geodesics.

*Proof.* The product matrices satisfy
\[
R_d=R_1\otimes I+I\otimes R_2,\quad
B_d=B_1\otimes I+I\otimes B_2,\quad P_N=P_a\otimes P_b.
\]
Expand both powers binomially; their respective factor summands commute because they act on disjoint coordinates. A term has nonzero antipodal trace in a factor only if its total number of moves in that factor is at least the factor's dimension. Since the total number of moves is exactly \(N=a+b\), each factor must use precisely its own dimension, giving \(r+(a-r)=a\) and \(k-r+(b-k+r)=b\), whence (TS2). Every summand is nonnegative. If both factors have positive mixed traces at seam ranks \(r_1,r_2\), take \(k=r_1+r_2\); the associated binomial coefficient product is strictly positive. Conversely a positive summand implies both factors have a one-change geodesic. \(\square\)

**Corollary (exact multiplicativity of failure).** A fixed arbitrary-color \(B_d\) counterexample generates full one-change geodesic counterexamples in every product dimension \(hd\). The amplification is stronger at the partial-path level: every one-change direction-simple path in the \(h\)-fold product misses at least \(h\) directions, by (NS2). If the original coloring is antipodally odd then all its seam counts are equal by the separate uniform-seam identity (SM1) in the matrix Subsection, and Vandermonde's identity reduces (TS2) to the previously proved monochromatic-trace tensorization.

This exhibits two complementary, exact closure obstructions: multiplicativity of the zero/nonzero full-geodesic two-phase trace, and additivity of the deficit for its partial-path relaxation.



### Exact invariance of the full-path minimum switch number under Cartesian powers

For an arbitrary binary edge coloring \(d\) of \(Q_q\), write \(\mu(d)\) for the minimum number of edge-color changes among full antipodal geodesics of \(Q_q\). Retain \(L_1(d)\), the largest length of a direction-simple path with at most one color change.

**Theorem (switch-minimum product invariance).** For every arbitrary binary edge coloring \(d\) and every \(h\ge1\),
\[
\boxed{\mu(d^{\boxtimes h})=\mu(d).}\tag{SP1}
\]
More generally, if \(d_1,\ldots,d_h\) are distinct independent factors, then
\[
\boxed{\mu(d_1\boxtimes\cdots\boxtimes d_h)\ge\max_j\mu(d_j).}\tag{SP2}
\]

*Proof.* A full product geodesic uses each direction exactly once. Deleting from its direction order all moves outside a given factor leaves a full antipodal geodesic of that factor. Its positional color word is a subsequence of the product path's word, so its number of switches cannot exceed that of the product. Minimizing proves (SP2) and the lower bound in (SP1).

For the upper bound in (SP1), choose a full factor geodesic whose color word has precisely \(s=\mu(d)\) changes, giving \(s+1\) successive monochromatic runs. In each of the \(h\) independent copies choose the identical geodesic with the identical color sequence. Interleave the direction words **run by run**: first traverse the first run of each copy, then the second run of each copy, and so forth. Independence of factors makes this a full product geodesic, and its concatenated color word has the same \(s\) switches. Hence \(\mu(d^{\boxtimes h})\le s\), completing the proof. \(\square\)

**Counterexample-amplification dichotomy.** If an arbitrary-color one-change counterexample \(d\) exists in dimension \(q\), then \(\mu(d)=s\ge2\). For every \(h\),
\[
\boxed{
\mu(d^{\boxtimes h})=s,\qquad
hq-L_1(d^{\boxtimes h})\ge h.
}\tag{SP3}
\]
The first equality is (SP1); the second follows from (NS2). Thus the identical Cartesian powers simultaneously have a **bounded** number of unavoidable full-geodesic color changes and a **linear** deficit in their longest one-change partial geodesic.

**Consequence for approximate proof strategies.** Any dimension-uniform bound of the form
\[
\boxed{n-L_1(d)\le g(\mu(d))}
\tag{SP4}
\]
with finite \(g(s)\) independent of \(n\), if proved for all arbitrary binary cube edge colorings, would imply the entire Leader--Long one-change geodesic conjecture and hence unrestricted NORI1. Indeed a hypothetical counterexample and its powers violate (SP4) by (SP3). Conversely if the grand conjecture holds, the left side vanishes. Therefore (SP4) is itself grand-theorem equivalent, regardless of how rapidly \(g\) grows.

In particular, an \(O(\sqrt n)\) full-geodesic switch bound, such as the theorem of Hollom (2026), does not **by itself** entail an \(n-o(n)\) one-change partial-path bound through a generic compression inequality depending only on the number of switches. Such a compression theorem would need to exclude the tensor-power obstruction using additional global structure, or equivalently settle the conjecture.



### Dual approximation from above: shortest one-change antipodal paths

For arbitrary two-edge-colorings \(d\) of \(Q_n\), define \(\ell_1(d)\in\{n,n+2,n+4,\ldots\}\cup\{\infty\}\) to be the minimum length of an antipodal path with at most one edge-color change; assign \(\infty\) if no such path exists. The color word may consist of one or two monochromatic runs. The conjectured full one-change geodesic is equivalent to \(\ell_1(d)=n\), since any antipodal path of length \(n\) is a full geodesic.

**Theorem (shortest one-change antipodal path tensorization).** For every arbitrary edge coloring \(d\) and \(h\ge1\),
\[
\boxed{\ell_1(d^{\boxtimes h})=h\,\ell_1(d),}\tag{AP1}
\]
with the convention \(h\infty=\infty\). Hence unrestricted NORI1 is equivalent to the following *approximation from above*: there exists a uniform function \(f(n)=o(n)\) such that every arbitrary two-edge-coloring of \(Q_n\) admits an antipodal path of at most one color change and length at most \(n+f(n)\). The analogous assertion with \(f(n)=C\), a fixed constant, is also equivalent.

*Proof.* Let \(P\) be a one-change antipodal walk in the product \(Q_{hd}\). Its projection to each \(d\)-dimensional factor is an antipodal walk whose color word is a subsequence of the word of \(P\), and so has at most one change. Erasing any closed subwalk preserves its endpoints and cannot increase the number of color changes, since deletion of a contiguous block from a binary word does not increase its number of changes. Thus each factor projection has at least \(\ell_1(d)\) steps, giving \(|P|\ge h\ell_1(d)\). If \(\ell_1(d)=\infty\), this proves the product likewise admits no one-change antipodal path.

Conversely, choose a shortest one-change antipodal path \(P_d\) in \(Q_d\), with color word \(0^a1^b\) after optional reversal and color renaming (either run may be empty). In all \(h\) factors follow its first monochromatic run, sequentially, then follow its second monochromatic run in all factors, sequentially. This is a simple antipodal path of the product: at every step at least one factor advances along its own simple path, and factor progress is monotone. It has \(h(a+b)=h\ell_1(d)\) edges and at most one change, proving the reverse inequality and (AP1).

If NORI1 holds, then by the earlier exact equivalence the arbitrary-color one-change full geodesic theorem holds, so \(\ell_1(d)=n\) for every \(d\), establishing either asymptotic assertion. Conversely suppose an arbitrary-color \(B_d\) counterexample exists. Either \(\ell_1(d)=\infty\), violating the bound immediately, or parity of antipodal path lengths forces \(\ell_1(d)\ge d+2\). By (AP1), its \(h\)-fold power has \(\ell_1(d^{\boxtimes h})\ge h(d+2)=hd+2h\), giving a fixed positive fractional excess \(2/d\) along dimensions \(hd\), contrary to any uniform \(f(n)=o(n)\) or fixed \(C\). By the already established all-dimensional equivalence of \(B_d\) and NORI1, the assertion follows. \(\square\)

**Two-sided near-geodesic closure targets.** The dimension-uniform NORI1 problem is now equivalently expressible by either of two sublinear approximations to a one-change geodesic for *arbitrary* two-edge-colorings:

- **From below:** a direction-simple path with at most one change of length \(n-o(n)\), by (NS1).
- **From above:** an antipodal path with at most one change of length \(n+o(n)\), by (AP1).

Both implications back to full closure are proved by Cartesian-power amplification. The second formulation asks for quantitative near-geodesicity inside the original Feder--Subi one-change antipodal *path* problem, which remains stronger than the settled unrestricted original Norine monochromatic-antipodal-*path* result. In particular the known existence of a monochromatic antipodal path for odd colorings does not establish (AP1)'s approximating hypothesis for arbitrary colorings. These statements provide global proof targets rather than independent proofs of their hypotheses.


## Strict half-switch and four-direction prescription

# Strict half-switch bound and four-direction prescription

Let d be an arbitrary two-coloring of undirected edges of Q_n. Write r(v), b(v)=n-r(v) for its incident color degrees, and s(P) for the number of color changes on a full antipodal geodesic.

**Lemma.** For a uniformly random root and full direction order,
\[
\mathbb E\,s(P)=\frac{2}{n2^n}\sum_{v\in Q_n}r(v)b(v)
\le \frac2n\left\lfloor\frac{n^2}4\right\rfloor.
\tag{1}
\]
*Proof.* At each of the n-1 intermediate vertices the ordered pair of successive distinct directions is uniform among n(n-1) pairs, and the vertex is uniform over Q_n. At v precisely 2r(v)b(v) of the ordered direction pairs switch color. Summing their probabilities proves (1). \(\square\)

**Theorem (strict half-switch).** For every even n=2h>=4, any arbitrary coloring of Q_n has a full antipodal geodesic with at most h-1 color changes. For odd n, (1) guarantees at most (n-1)/2.

*Proof.* The odd-dimensional claim follows by the integer-valued switch count. When n=2h>=4, (1) gives expectation at most h. If all full geodesics had at least h switches, then all of them would have precisely h. For every vertex x and two distinct directions i,j, start a full path at x with first direction i and last direction j. Parity of its h switches implies
\[
d_i(x)+d_j(\bar x)=h\bmod2.
\tag{2}
\]
For any distinct i,k choose j outside {i,k}; (2) gives d_i(x)=d_k(x). Every vertex therefore has a monochromatic star, hence by connectivity the entire coloring is constant. It then has zero-switch full paths, contradicting h>=2. \(\square\)

**Corollary (arbitrary-color four-cube).** Every arbitrary red-blue edge coloring of Q4 has a full antipodal geodesic with at most one switch, without any antipodal relation. Independently, a binary integer feasibility program on the 32 Q4 edges, excluding eight one-switch color words on each of its 192 unoriented full antipodal geodesics, was infeasible under SciPy/HiGHS. The proof does not rely on that audit.

**Theorem (unrestricted four-direction NORI1 prescription).** Let n>=4 and c be any binary undirected-edge coloring of Q_n obeying c_i(x+e_i)=c_i(x), c_i(bar x)=1+c_i(x). For any four distinct directions S and desired t in F2^S, some full antipodal geodesic has direction-indexed colors t on S.

*Proof.* For n>4, apply the previously proved multifacet bridge equivalence B_k iff P_(n,S) in this subsection at k=4. In brief, on a lower S-face recolor each direction i by t_i, take its zero-then-one one-switch full path, reverse the zero prefix, traverse all exterior directions to the opposite face, and traverse the reversal of the antipodal image of the one suffix. This is a full geodesic whose S-edges have colors t_i.

For n=4, directionwise recolor by t_i and use the preceding four-cube corollary to obtain a path from u to bar u with red prefix U and blue suffix V. Starting at the switch vertex, reverse U and then reverse the antipodal image of V. Antipodal oddness makes both parts red; they traverse complementary direction subsets and join antipodal endpoints. Undo the recoloring to obtain prescribed profile t. \(\square\)

The four-direction theorem strengthens the previous three-direction prescription for all legal NORI1 colorings. The small-dimensional one-switch statement is known in the literature; the displayed argument gives an elementary proof. The general switch bound does not settle the arbitrary-color one-switch problem beyond dimension four.

## Passive lift profile factorization and active completion

# Passive lift profile factorization and four-direction-assisted active completion

Let c be any binary undirected-edge coloring of Q_n satisfying c_i(x+e_i)=c_i(x) and c_i(bar x)=1+c_i(x). For any such coloring write W(c) for its set of direction-indexed color profiles of rooted, ordered full antipodal geodesics.

**Theorem 1 (passive paired lift has a product profile support).** Define the conventional paired lift on Q_(2n) by
\[
\widetilde c_i(x,y)=c_i(x),\qquad
\widetilde c_{n+i}(x,y)=1+c_i(x)\quad(1\le i\le n).
\tag{PC1}
\]
Then
\[
\boxed{W(\widetilde c)=W(c)\times\mathbb F_2^n.}\tag{PC2}
\]
The paired lift is legal and antipodally odd, and contains a monochromatic full antipodal geodesic if and only if c does.

*Proof.* Project any full geodesic of the lift to the first n vertex bits and delete the y-steps. The remaining path is a full antipodal geodesic in c with the same old-direction profile, proving the upper containment in (PC2). Conversely, select any full base geodesic starting at x, with direction order pi and old profile u. Given any desired dummy-direction word v, place dummy direction n+i before all old directions if v_i=1+c_i(x), and after all old directions otherwise. Before the base path its dummy color is 1+c_i(x); after the base path, at bar x, its dummy color is c_i(x). Thus its dummy word is v and its old word is u. The starting dummy bits are arbitrary, establishing the product support. Monochromaticity equivalence follows by taking zero targets and by the projection. \(\square\)

**Lemma 2 (one-helper rigidity).** Suppose C is any legal antipodally odd coloring of Q_(n+1) whose old-direction coloring on the face y=0 is c. Then for every old direction i and x,
\[
\boxed{C_i(x,1)=c_i(x)=C_i(x,0).}\tag{PC3}
\]
*Proof.* The global antipode sends (x,1) to (bar x,0), so C_i(x,1)=1+C_i(bar x,0)=1+c_i(bar x)=c_i(x). \(\square\)

**Theorem 3 (universal active completion with n-3 helpers).** Let n>=4 and c be any legal antipodally odd coloring of Q_n. Fix any four-element direction subset S, put T=[n]\setminus S, and choose s in S. Introduce auxiliary bits y_* and y_i for i in T, in total m=1+|T|=n-3 additional cube directions. Define C on Q_(n+m) by
\[
C_i(x,y)=
\begin{cases}
c_i(x),&i\in S,\\
c_i(x)+y_i+y_*,&i\in T,
\end{cases}
\qquad
C_{y_j}(x,y)=x_s\quad(j\in T\cup\{*\}).
\tag{PC4}
\]
Then C is legal and antipodally odd, its restriction to the face y=0 in old directions agrees with c, and
\[
\boxed{W(C)=\mathbb F_2^{n+m}=\mathbb F_2^{2n-3}.}\tag{PC5}
\]
Every target profile is attained using an order in which one selected set of auxiliary directions comes before all original directions, with the remaining auxiliary directions after them.

*Proof.* Each old-direction rule ignores its own original bit; each auxiliary rule x_s ignores its own auxiliary bit. Under the global antipode, c_i flips, the even expressions y_i+y_* do not flip, and x_s flips. Hence C is legal and odd, and at y=0 the old rules equal c.

Fix any target full profile (w,v), with old word w in F2^n and auxiliary word v in F2^m. By the universal four-direction prescription theorem in the previous subsection development, choose a full old-direction geodesic from some x in some order pi whose colors agree with w on S. Let d_i be its old profile for i in T. Define b=x_s. Place auxiliary direction y_j before the entire old geodesic if v_j=b, and after it if v_j=1+b. These helper edges then have precisely their prescribed colors, because the s-th old bit changes from b to 1+b during the old full path.

Let E_j indicate whether helper direction j is in the early group. Choose the auxiliary bit values y_j^{mid} during the old geodesic so that y_*^{mid}=0 and y_i^{mid}=d_i+w_i for i in T. Take the initial auxiliary root values y_j^{start}=y_j^{mid}+E_j. After the early helper moves, the helper values equal the prescribed mid values; they remain fixed throughout the old-direction segment. For every i in T, its color along that segment is c_i+ y_i^{mid}+y_*^{mid}=d_i+(d_i+w_i)=w_i; for i in S, its color is w_i by selection of the base path. The remaining auxiliary moves have color v_j. Every old and auxiliary direction is used once. Thus the target profile is attained. \(\square\)

**Lemma 4 (helper information-capacity bound for frozen-state control).** If a Boolean control map H:F2^m->F2^t obeys H(y+\mathbf1)=H(y), then its image contains at most 2^(m-1) elements. Surjectivity onto F2^t therefore requires m>=t+1. The control map H(y)=(y_i+y_*)_(i in T) used in (PC4), with t=|T|=n-4 and m=t+1, attains this information bound.

*Proof.* An antipodally even H factors through the quotient of F2^m by the two-element subgroup generated by the all-one vector, whose cardinality is 2^(m-1). The displayed H maps onto F2^t by choosing y_*=0 and the y_i independently. \(\square\)

**Computer audit.** For n=4,5,6, four random legal odd base colorings per dimension were tested against 250 independently random full-profile targets, using a brute-force four-direction base witness finder and the construction from Theorem 3. All 3000 targets were attained, and legality was tested separately. The paired-lift factorization (PC2) was checked by full root/order enumeration for four random base colorings in each of dimensions n=2 and n=3.

**Scope.** These statements apply to every legal odd base coloring, regardless of nonlinear dependencies. The passive factorization shows why adding directions that never influence the original color rules cannot erase a missing profile. The active completion supplies enough independent antipodally even phase controls to remove all remaining profile constraints after a four-direction base witness. Since it changes the old-direction rules outside y=0, it is not a counterexample-preserving reduction and does not prove NORI1 in dimension n.

### Seven-direction-assisted control reduction

**Theorem 5 (seven-prescription assisted completion).** Let n>=9 and let c be any legal antipodally odd coloring of Q_n. Choose a set S of seven original directions and write T=[n]\S. Add m=|T|+1=n-6 auxiliary bits, one bit y_i for each i in T and one reference bit y_*. Choose s in S. Define
\[
C_i(x,y)=c_i(x)\ (i\in S),\qquad
C_i(x,y)=c_i(x)+y_i+y_*\ (i\in T),\qquad
C_{y_j}(x,y)=x_s\ (j\in T\cup\{*\}).
\tag{PC6}
\]
Then C is legal and odd, agrees with c on the all-zero auxiliary face, and has every direction-indexed full-geodesic color profile in F2^(2n-6). The number n-6 supersedes the weaker n-3 helper bound from Theorem 3 above, which used only four-direction prescription.

*Proof.* The preexisting universal seven-direction prescription theorem in this subsection follows from the established monochromatic geodesic theorem in Q8 (Kirchweger, Peitl, Subercaseaux and Szeider, 2025) and the multifacet bridge. For a desired original word w, choose a full base geodesic with prescribed colors w on S. As in Theorem 3, place each helper before or after the base full path depending on its desired color and the starting s-th bit. With the helper-state reference value y_* chosen as zero during the old-direction segment, set each auxiliary mid-state bit y_i equal to the discrepancy between c_i along the chosen base path and the target w_i. The auxiliary starts are obtained by undoing the designated early flips. All original and auxiliary target colors follow as in Theorem 3. The two legality identities hold because each phase term y_i+y_* is antipodally even and each auxiliary edge color x_s is odd under antipodality. \(\square\)

The general form is a profile-completion principle: if k designated original directions can be assigned arbitrary colors by a full base geodesic, then n-k+1 antipodally paired phase-control helpers suffice to make every profile realizable in a face-preserving extension, for k<n. The antipodally even phase map uses its 2^(n-k) possible relative helper states fully, attaining the information-capacity limit for independent correction of the remaining n-k edge colors during one frozen helper-state segment.

This is an active extension, not a counterexample-preserving lift. The project already had seven-direction prescription before the present note; that previously known theorem supplies the improved helper budget.

## Sharp one-helper passivity and two-helper universal profile completion

## Sharp one-helper passivity and two-helper universal profile completion

Let n>=2 and let c be any legal antipodally odd binary undirected-edge coloring of Q_n, so c_i(x+e_i)=c_i(x) and c_i(bar x)=1+c_i(x). Write W(c) for the set of direction-indexed binary profiles of full antipodal geodesics.

**Theorem 1 (one-helper extension factorization).** Let C be any legal odd coloring of Q_(n+1), with one new bit z, such that C_i(x,0)=c_i(x) for all original directions i. Then necessarily
\[
C_i(x,z)=c_i(x)\quad\text{for both }z\in F_2,
\tag{EH1}
\]
and
\[
\boxed{W(C)=W(c)\times F_2.}\tag{EH2}
\]
*Proof.* Oddness gives C_i(x,1)=1+C_i(bar x,0)=1+c_i(bar x)=c_i(x). The new-direction edge has rule C_z(x,z)=d(x), independent of z; global oddness forces d(bar x)=1+d(x). Projection of any full extension geodesic onto original directions gives a full base geodesic, proving inclusion in W(c) times F2. Conversely, choose a base geodesic realizing w from root x. Put the new-direction step before all original steps if the desired z-color equals d(x), and after all original steps otherwise. At the latter position its color is d(bar x)=1+d(x). The original profile remains w in either placement. This proves (EH2). \(\square\)

**Theorem 2 (two-helper universal full-profile completion).** Every legal odd coloring c of Q_n, n>=2, admits a legal odd extension C to Q_(n+2), agreeing with c on the auxiliary face (u,v)=00, for which
\[
\boxed{W(C)=F_2^{n+2}.}\tag{EH3}
\]
Such an extension may be defined explicitly by
\[
b_i(x)=x_{i+1\bmod n},\qquad
C_i(x,u,v)=
\begin{cases}
c_i(x),&u=v,\\
b_i(x),&u\ne v,
\end{cases}\ (0\le i<n),
\tag{EH4}
\]
\[
\boxed{C_u(x,u,v)=v,\qquad C_v(x,u,v)=x_0.}\tag{EH5}
\]
For any prescribed target profile, the resulting witness starts in the original auxiliary face 00 and uses just one of the two guard-direction arrangements u, old steps, v or v, old steps, u.

*Proof.* In (EH4), c_i and b_i each ignore their own x_i and are odd under global x complementation; the equality predicate u=v is unchanged when u,v are both flipped. The rule C_u=v ignores u and flips under global antipodality; C_v=x_0 ignores v and flips under global antipodality. Thus C is legal and odd, and agrees with c on the 00 face.

Prescribe an old-direction word w=(w_0,...,w_(n-1)) and new-direction bits (p,q)=(w_u,w_v). Put
\[
\boxed{x_0=1+p+q.}\tag{EH6}
\]
Consider the cyclic-reader coloring b on Q_n. Given any direction permutation pi, its profile equations are
\[
w_i=x_{i+1\bmod n}+[\ i+1\bmod n\text{ appears before }i\text{ in }\pi\ ].
\tag{EH7}
\]
These determine one root x for every pi,w. Choosing pi=(n-1,0,1,...,n-2) gives x_0=w_(n-1), while choosing pi=(0,1,...,n-1) gives x_0=1+w_(n-1). Since n>=2, the two lists are valid, and one of them produces the desired x_0 from (EH6).

Start C at (x,0,0). If p=0, take the complete direction order (u,pi,v). The first new step has color C_u=0, then the original steps are on the face (u,v)=(1,0), where their colors are b and yield w; finally v is used at original endpoint bar x, giving color C_v(bar x,1,0)=1+x_0=q. If p=1, use the order (v,pi,u). Its first new edge has color C_v(x,0,0)=x_0=q; the old steps occur at auxiliary state (0,1), again giving w; the last u-edge has color C_u=1=p. In both cases the path traverses all n+2 directions once, terminates at (bar x,1,1), and realizes (w,p,q). \(\square\)

**Corollary 3 (two auxiliary bits suffice without a partial-prescription theorem).** The active-completion construction in the same subsection that used n-6 helper bits based on the known seven-direction prescription is superseded as an upper bound on the number of helpers: a pair of helpers suffices for all n>=2. In contrast, one-helper extensions have the product property (EH2) and cannot create missing original-direction profiles. In particular, a face-preserving full-profile extension theorem by itself supplies no information about whether W(c) contains a given profile, since (EH3) holds for every legal base c independently of its profile support.

**Finite audit.** The constructive witness formulas were checked against independently generated legal odd base edge colorings for dimensions n=2,3,4,5,6. All 2^(n+2) target profiles were tested for n=2,3,4,5, and 200 sampled targets for n=6, including verification of the returned rooted geodesic endpoint and all edge colors. The dimension-uniform proof does not rely on this enumeration.

**Scope.** The construction requires adding dimensions and modifies old-direction edge colors on auxiliary faces with u different from v. Consequently it is not a counterexample-preserving lift and does not settle unrestricted NORI1. The primary conclusion is a sharp distinction between passive one-helper extensions and programmable two-helper extensions.

### Factorial witness lower bound for two-helper completion

**Corollary 4 (uniform factorial witness multiplicity).** For the two-helper extension C in (EH4)-(EH5), every prescribed profile in F2^(n+2) is attained by at least n! rooted, ordered full antipodal geodesics.

*Proof.* Fix a target (w,p,q). Among all n! permutations pi, half place original direction 0 before direction n-1 and half place it after. Equation (EH7) then determines x_0 as one of the two values w_(n-1) or 1+w_(n-1), respectively. Hence n!/2 direction permutations give the root parity (EH6), and each determines a full geodesic starting on the 00 auxiliary face with the target profile. Reversing these paths gives another n!/2 rooted full geodesics starting on the 11 auxiliary face, with unchanged direction-indexed colors. These two classes are disjoint by starting auxiliary state, yielding n! witnesses. \(\square\)

The result counts rooted, ordered paths. In the absence of any assumptions on c it supplies a uniform positive lower bound for every profile of the extension.
