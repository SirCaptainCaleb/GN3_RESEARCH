# Article VIII - Antipodally odd edge colorings

## Central edge carriers and antipodal topology

### The full-geodesic color-profile span theorem for unrestricted NORI1

Let \(n\ge2\) and let \(c_i(u)\in\mathbb F_2\) be the color of the ** undirected** edge \(\{u,u\oplus e_i\}\) of the Boolean cube \(Q_n\). Assume the  NORI1 conditions
\[
c_i(u\oplus e_i)=c_i(u),\qquad
c_i(\bar u)=1\oplus c_i(u)
\tag{1}
\]
for every direction \(i\) and cube vertex \(u\). No linearity, locality, exterior-support, regularity, or direction-independence is assumed.

For a starting root \(u\in Q_n\) and a permutation \(p\) of all \(n\) coordinates, traverse the full antipodal geodesic in the order \(p\). Record its edge-color vector **indexed by original coordinate direction**, independently of the order in which those directions were used:
\[
w_i(u,p)=c_i\bigl(u\oplus\{p_j:j<p^{-1}(i)\}\bigr)
\quad(i=1,\ldots,n).
\tag{2}
\]
Write \(\mathcal W(c)=\{w(u,p):u\in Q_n,\ p\in S_n\}\subseteq\mathbb F_2^n\).

**Theorem (unrestricted full-profile affine span).**
\[
\boxed{\operatorname{aff}_{\mathbb F_2}\mathcal W(c)=\mathbb F_2^n.}
\tag{3}
\]
Equivalently, for every **nonempty set of directions** \(S\subseteq[n]\), the parity
\[
\bigoplus_{i\in S} w_i(u,p)
\]
assumes **both** binary values among full antipodal cube geodesics. Thus the attainable full-profile family obeys *no nontrivial universal affine parity identity* for any legal NORI1 coloring, even when the coloring is nonlinear.

**Proof.** Suppose (3) fails. Linear algebra over \(\mathbb F_2\) supplies a nonzero vector \(y=(y_i)\in\mathbb F_2^n\) and a constant \(\kappa\) such that
\[
\bigoplus_i y_iw_i(u,p)=\kappa
\tag{4}
\]
for **every** root \(u\) and full coordinate permutation \(p\).

Give each  edge in direction \(i\) the mod-two weight
\[
\omega_i(u)=y_i c_i(u).
\tag{5}
\]
Because \(c_i\) is an undirected -edge color, \(\omega_i(u\oplus e_i)=\omega_i(u)\).

Fix any  square with corner \(u\) and distinct directions \(i,j\). Compare two full antipodal geodesics *from the same root* \(u\): the first starts with directions \((i,j)\), the second with \((j,i)\), and both use **the same order of all remaining directions**. They reach the same vertex after two moves, so every later  edge is identical. Subtracting the two instances of (4) therefore gives the  square-closedness equation
\[
\omega_i(u)\oplus\omega_j(u\oplus e_i)
\oplus\omega_j(u)\oplus\omega_i(u\oplus e_j)=0.
\tag{6}
\]
Every square is realized by such a pair of full geodesics; no based-window or abstract-face identification has been used.

Since every square has zero mod-two curvature, the edge cochain \(\omega\) is a gradient on the Boolean cube:
\[
\omega_i(u)=\phi(u)\oplus\phi(u\oplus e_i)
\tag{7}
\]
for some vertex potential \(\phi:Q_n\to\mathbb F_2\). For completeness, fix \(\phi(0)=0\), and define \(\phi(u)\) by integrating \(\omega\) along any cube path from \(0\) to \(u\). Any two such paths differ by backtrack cancellations and elementary square swaps;  edge invariance and (6) make their integrals equal. Thus (7) follows.

Every full antipodal geodesic telescopes under (7), so (4) implies
\[
\psi(u):=\phi(u)\oplus\phi(\bar u)=\kappa
\quad\text{for every }u.
\tag{8}
\]
But for every coordinate \(i\), the edge-gradient identity and **antipodal oddness** in (1) give
\[
\begin{aligned}
\psi(u\oplus e_i)\oplus\psi(u)
 &=\omega_i(u)\oplus\omega_i(\bar u)\\
 &= y_i\bigl(c_i(u)\oplus c_i(\bar u)\bigr)\\
 &=y_i.
\end{aligned}
\tag{9}
\]
Because \(\psi\) is constant, the left side is zero, forcing \(y_i=0\) for every \(i\), contrary to \(y\ne0\). This proves (3). \(\square\)

**Corollary (arbitrary prescribed colors on two directions).** Fix any **two distinct coordinate directions** \(i,j\) and any pair \((a,b)\in\mathbb F_2^2\). There exists a *full antipodal cube geodesic*, with some starting root and permutation of **all \(n\) directions**, whose edge in direction \(i\) has color \(a\) and whose edge in direction \(j\) has color \(b\).

**Proof.** Projection of (3) onto the \(i,j\) coordinates implies that the attainable pair-profile set has full affine span \(\mathbb F_2^2\). From (1), changing the root from \(u\) to \(\bar u\) while keeping the same direction order replaces every color \(w_i(u,p)\) by its complement. Hence the pair-profile set is closed under
\[
(a,b)\longmapsto(1\oplus a,1\oplus b).
\]
The only complement-invariant subset of \(\mathbb F_2^2\) with full affine span is the entire four-element set. \(\square\)

**Quantitative and constructive formulation.** Every legal coloring has at least \(n+1\) affinely independent realized direction-indexed full-geodesic profiles. For any prescribed nonzero functional \(y\), witnesses of opposite \(y\)-parity can be constructed by one of two edge-geometric mechanisms:

* If the weighted cochain \(\omega_i=y_ic_i\) has nonzero curvature on some square, the two full orders beginning with that square's directions in opposite orders give opposite \(y\)-parities at the same root.
* If every square has zero curvature, construct the potential \(\phi\) in (7), choose any \(i\) with \(y_i=1\), and use two full paths with the same coordinate order and roots differing by \(e_i\). Equation (9) shows their \(y\)-parities are opposite.

Thus the result is not merely an existential use of linear algebra: the proof isolates an explicit **adjacent-swap versus single-root-flip dichotomy** for every nonzero parity functional.

**Mathematical significance and  gap.** This theorem is a statement about **every** antipodally odd *-edge* NORI1 coloring. It establishes unrestricted two-direction prescription and excludes all affine-linear parity certificates for the nonattainment of full color words. These conclusions rely on global consistency of  square edges and antipodal oddness, rather than on affine formulas for the edge colors. They sharpen the partial-geodesic and restricted affine-family perspectives by identifying a global algebraic universality property that holds in the entire still-open class.

Full affine **span** of \(\mathcal W(c)\) does not imply \(\mathcal W(c)=\mathbb F_2^n\), nor that either constant vector \(0^n\) or \(1^n\) is attained. Full monochromatic NORI1 remains open. The precise missing implication is an additional *joint higher-order compatibility theorem* raising these independent parity separations and two-coordinate prescriptions to an all-coordinate word realization (or merely a monochromatic full word). The theorem also makes no claim about unrestricted ordinary boundary 3-tournaments; there the colored objects are ordered triples, and the square-gradient identity of  edges has no direct analogue.


### Universal three-direction prescription for unrestricted antipodally odd cube-edge colorings

**Theorem.** Let \(n\ge3\) and let \(c_i(x)\in\mathbb F_2\) color each * undirected* direction-\(i\) edge of \(Q_n\), satisfying
\[
c_i(x)=c_i(x\oplus e_i),\qquad c_i(\bar x)=1+c_i(x).
\]
For **every** three distinct directions \(i,j,k\) and **every** prescribed color triple \((t_i,t_j,t_k)\in\mathbb F_2^3\), some full antipodal geodesic (root and complete permutation unrestricted) traverses its \(i\)-, \(j\)- and \(k\)-edges in precisely the prescribed colors. Equivalently, the set \(\mathcal W(c)\) of full direction-indexed edge-color profiles projects **surjectively** to \(\mathbb F_2^3\) on every three-coordinate set. There are no restrictions on nonlinearity, exterior dependence, or the colors of the remaining \(n-3\) edges.

**Root-rotation identity.** For a full geodesic with root \(x\) and direction order \(p=(p_1,\ldots,p_n)\), use root \(x\oplus e_{p_1}\) and order \((p_2,\ldots,p_n,p_1)\). The new path traverses the *same  edges* in all directions other than \(p_1\). Its final \(p_1\)-edge is antipodal to the original first edge; thus its direction-indexed color profile is the original profile with precisely coordinate \(p_1\) complemented. This relies on both undirected undirectedness and edge antipodal oddness.

**Proof.** Suppose some prescribed triple never occurs. Complement the color of *every  edge* in direction \(r\in\{i,j,k\}\) by \(t_r\), leaving all other edge directions alone. Both edge axioms survive, and the impossible triple becomes \(000\). Taking the antipodal root of any full geodesic with the **same** coordinate order complements every direction's color, so \(111\) is also impossible.

Choose an arbitrary root \(x\) and complete direction order \(p=(i,j,k,r_4,\ldots,r_n)\); write \(A,B,D\) for the  edge colors at its first three steps. Rotate the first direction to the end three times, updating the root as above. The four resulting **full antipodal geodesics** have projected triples
\[
(A,B,D),\
(A+1,B,D),\
(A+1,B+1,D),\
(A+1,B+1,D+1).
\tag{1}
\]
None may be \(000\) or \(111\). A three-step geodesic of the three-cube avoiding these two opposite vertices must have starting bits \(010\) or \(101\) in its *step order*: its four successive Hamming weights must be \(1,2,1,2\), or \(2,1,2,1\). Consequently for **every root** and **every full order with prefix \(i,j,k\)** the first three edge colors are
\[
(A,B,D)=(q,1+q,q). \tag{2}
\]

Now compare the two full direction orders \((i,j,k,r_4,\ldots,r_n)\) and \((j,i,k,r_4,\ldots,r_n)\) *from the same arbitrary root \(x\)*. They traverse the **same  \(k\)-edge** at their third step, since in both cases they have already flipped precisely the directions \(i,j\). By (2), the first color on each path equals its common third color. Therefore
\[
c_i(x)=c_j(x)\qquad\text{for every }x\in Q_n. \tag{3}
\]
Apply (3) also at \(x\oplus e_i\) and use that \(c_i\) is the color of an **undirected** \(i\)-edge:
\[
c_j(x\oplus e_i)=c_i(x\oplus e_i)=c_i(x).
\]
But these are precisely the colors of the first and second edges in the original path with prefix \((i,j,k)\), and (2) demands that those two colors are *different*. Contradiction. Thus every prescribed triple occurs. \(\square\)

**Research significance and  limitation.** This strengthens NORI's previously recorded unrestricted **two-direction prescription** corollary to **three-direction prescription** for the *whole* NORI1 class. Full affine span of the profile set by itself does not imply triple surjectivity; the essential new ingredient is that cyclic geodesic root slides realize the three-cube walk (1), whose avoidance of one antipodal pair is rigid. Any failure to realize a *complete* target \(n\)-bit word must therefore involve compatibility among **at least four directions**, not a missing one-, two-, or three-direction marginal. The result does not yet force the all-zero or all-one full profile and does not solve unrestricted NORI1. It also does not prove a statement for ordered-three-face boundary tournaments: here the local colors attach to  edges, and the root slide complements precisely one direction-indexed edge color.

**Consistency check (not used in proof).** Direct enumeration of all \(2^{16}\) legal  antipodally odd edge colorings of \(Q_4\) found complete four-bit profile coverage; separate binary-integer feasibility tests found no obstruction to triple prescription in dimensions five, six, and seven. The argument above is valid in every dimension independently of these checks.

### Antipodal multifacet bridging: an  localization theorem for unrestricted NORI1

#### Statement and historical context

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

#### Proof of the forward implication

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

#### Proof of the reverse implication

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

#### Consequence: universal seven-direction color prescription

**Corollary 2 (all \(n\): every seven selected colors are realizable).** For every dimension \(n\ge8\), every legal antipodally odd -edge coloring of \(Q_n\), every set \(S\subseteq[n]\) of size \(k\le7\), and every prescribed color vector \(t\in\mathbb F_2^S\), there exists a **full \(n\)-edge antipodal geodesic** whose \(k\) selected edges have **precisely** the specified colors.

**Proof.** The geodesic Norine conjecture \(A_m\) has been established for **every \(m\le8\)**, including the SAT-certified case \(m=8\) in Kirchweger–Peitl–Subercaseaux–Szeider (2025), *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT*, arXiv:2511.08386, Theorem 1 (the paper explicitly states the *geodesic* conjecture in dimension eight). Leader and Long (2014), *Long geodesics in subgraphs of the cube*, Proposition 3.6 in arXiv:1301.2195v1, proved \(A_{k+1}\Rightarrow B_k\). Thus \(B_k\) holds for \(k\le7\). Theorem 1 above then gives \(P_{n,S}\) for every \(n>k\), as required. \(\square\)

For \(n\le8\), the stronger statement that **all \(n\) prescribed direction colors** can be realized also follows directly from the established full-geodesic result \(A_n\): independently XOR the desired \(t_i\) into each direction's edge color, preserving undirectedness and oddness, then use \(A_n\). Consequently, for **every** \(n\ge2\), arbitrary prescribed colors on any set of size \(\min(n,7)\) are simultaneously attainable, and in dimensions at most eight all \(n\) colors are attainable.

**Boundary of the result.** This uses a previously proved finite-dimensional geodesic theorem and an  new dimension-free bridge implication. It is not a proof of the full NORI1 conjecture in arbitrary dimension; for eight selected directions in \(n\ge9\), the bridge equivalence reduces the question **precisely** to \(B_8\), equivalently to the known Leader–Long dimensional challenge \(A_9\Rightarrow B_8\) in one direction. The argument makes no claim about *ordinary boundary 3-tournaments*: it uses an edge (one-window) color seam, whereas ordered-three-face paths acquire two extra seam windows.

**Primary sources and scope checks.**
- Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33; https://arxiv.org/abs/1301.2195 .
- Markus Kirchweger, Tomáš Peitl, Bernardo Subercaseaux, Stefan Szeider, *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT* (2025), arXiv:2511.08386, specifically Theorem 1 and the separate SAT geodesic encoding \(\Psi_n\); https://arxiv.org/html/2511.08386 .
- Tomáš Feder and Carlos Subi, *On hypercube labellings and antipodal monochromatic paths*, Discrete Applied Mathematics 161 (2013), 1421–1426 (original unrestricted-edge 2-cp *path* conjecture; the geodesic strengthening is due to Leader–Long).

**Unification scope:** This established NORI1 localization theorem is retained as prior mathematics, not an independent current research target. A later NORI1 paired-start toy theorem, originally published in composition v2, is preserved with its complete proof in note `note_antipodal_paired_start_nori1_toy_unification_probe`; no transfer to ordinary boundary tournaments has been established.

### Penultimate-length extension and parallel-face endpoint exclusion

Let \(n\ge3\). Color the undirected edges of \(Q_n\) by \(c:E(Q_n)\to\{0,1\}\), where \(c(\bar e)=1-c(e)\). Write \(x^i\) for the vertex obtained by flipping coordinate \(i\), and \(x^{ij}=(x^i)^j\). For a nonempty geodesic \(P\), let \(\sigma(P)\) be its number of edge-color changes.

**Lemma 1 (penultimate-length parity).** Let \(P\) be an \((n-1)\)-edge geodesic from \(u\) to \(v\), missing direction \(d\), with initial color \(s\), final color \(t\), and \(r=\sigma(P)\). If \(r\) is even, precisely one of the two \(d\)-edge extensions preserves \(r\) changes. If \(r\) is odd, either both preserve \(r\), or both introduce one additional change. For odd \(r\), preservation occurs if and only if \(c(uu^d)=s\).

*Proof.* Since \(v=\bar u^d\), the unused \(d\)-edges at \(u,v\) are antipodal, with colors \(a,1-a\), where \(a=c(uu^d)\). Prepending the edge at \(u\) introduces \([a\ne s]\) changes, while appending the edge at \(v\) introduces \([1-a\ne t]\) changes. Since \(t=s\oplus(r\bmod2)\), these indicators are complementary for even \(r\) and equal for odd \(r\). In particular, a monochromatic penultimate geodesic extends monochromatically. \(\square\)

**Lemma 2 (odd-change rotation).** If a full antipodal geodesic has an odd number \(r\) of color changes, there exists a full antipodal geodesic with \(r-1\) changes. Consequently, the minimum number \(\mu(c)\) of changes among full antipodal geodesics is even. In particular, the existence of a full geodesic with at most one change implies a monochromatic full geodesic.

*Proof.* Let the full geodesic have color word \(w_1,\ldots,w_n\), with \(r\) odd. Choose any change position \(k\), so \(w_k\ne w_{k+1}\). Cyclically move its first \(k\) coordinate directions to the end, using the vertex reached after those directions as the new root. The resulting full antipodal geodesic has color word
\[
(w_{k+1},\ldots,w_n,1-w_1,\ldots,1-w_k).
\]
Its internal changes within the two displayed blocks number \(r-1\). Since \(r\) is odd, \(w_n=1-w_1\), so the new join introduces no change. Thus its total is \(r-1\). A minimum over all full geodesics cannot be positive and odd. \(\square\)

**Theorem 3 (color-change-preserving completion across parallel faces).** Let \(F\) be an \((n-2)\)-face with fixed coordinates \(a,b\). Suppose a monochromatic geodesic \(P\) spans \(F\) and terminates at \(x\in F\). Then either a monochromatic full antipodal geodesic exists, or the following holds simultaneously for both adjacent faces: every geodesic \(Q\) spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\), extends by two edges to a full antipodal geodesic \(R\) satisfying \(\sigma(R)=\sigma(Q)\).

*Proof.* Let \(s\) be the color of \(P\), and assume that no monochromatic full antipodal geodesic exists. By Lemma 1, no monochromatic \((n-1)\)-edge geodesic exists. Appending either \(a\)- or \(b\)-edge at \(x\) to \(P\) therefore forces
\[
c(xx^a)=c(xx^b)=1-s. \tag{1}
\]
The antipodal image of \(P\) spans \(F^{ab}\) and has color \(1-s\). It has \(x^{ab}\) as an endpoint: the other endpoint of \(P\) is \(x^{[n]\setminus\{a,b\}}\), whose antipode is \(x^{ab}\). Applying the same penultimate argument at \(x^{ab}\) yields
\[
c(x^{ab}x^a)=c(x^{ab}x^b)=s. \tag{2}
\]
Let \(Q\) span \(F^a\) and end at \(x^a\), with final color \(t\). If \(t=1-s\), append the route \(x^a,x,x^b\), whose two edges both have color \(t\) by (1). If \(t=s\), append \(x^a,x^{ab},x^b\), whose two edges both have color \(t\) by (2). Each concatenation uses every coordinate once and reaches the antipode of its starting vertex. Both appended edges agree with the terminal color, so no additional change occurs. The argument for \(Q\) spanning \(F^b\) is symmetric. \(\square\)

**Corollary 4 (one-change parallel-face endpoint exclusion).** In a counterexample to the monochromatic antipodal-geodesic assertion, a monochromatic geodesic spanning \(F\) and terminating at \(x\) excludes every geodesic with at most one color change spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\).

*Proof.* Theorem 3 would yield a full antipodal geodesic with at most one change; Lemma 2 would make it monochromatic. \(\square\)



Theorem 3 strengthens parallel-face endpoint exclusion to a monochromatic path paired with a path having one color change.

**Theorem 5 (synchronized opposite-phase switch splicing).** Let \(n\ge4\), let \(F\) be a codimension-two face with fixed coordinates \(a,b\), and put \(D=[n]\setminus\{a,b\}\). Suppose there are two geodesics spanning adjacent faces,
\[
P:\quad u\ \xrightarrow[\text{color }s]{A}\ z\
\xrightarrow[\text{color }1-s]{B}\ x
\quad\text{in }F,
\]
\[
Q:\quad u^a\ \xrightarrow[\text{color }1-s]{A}\ z^a\
\xrightarrow[\text{color }s]{B}\ x^a
\quad\text{in }F^a,
\]
where \(A,B\) are a partition of \(D\) into two nonempty direction sets. The paths may traverse directions within \(A\) and within \(B\) in different orders. All edges within each displayed block have the displayed color. Then the coloring has a monochromatic full antipodal geodesic.

*Proof.* Write \(h=c(zz^a)\).

If \(h=s\), the following two length-\((n-1)\) monochromatic geodesics of color \(s\) exist:
\[
u\ \xrightarrow{P|_A}\ z\ \xrightarrow{a}\ z^a\
\xrightarrow{Q|_B}\ x^a,
\]
and
\[
x^a\ \xrightarrow{(Q|_B)^{\rm rev}}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{(P|_A)^{\rm rev}}\ u.
\]
Both use every direction in \(D\cup\{a\}\) once. Their missing \(b\)-edges at the displayed terminal vertices are \(x^ax^{ab}\) and \(uu^b\), which are antipodal; consequently one has color \(s\). Appending it yields a monochromatic full geodesic.

If \(h=1-s\), use instead the monochromatic \((n-1)\)-edge paths of color \(1-s\)
\[
u^a\ \xrightarrow{Q|_A}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{P|_B}\ x,
\]
and its reversal
\[
x\ \xrightarrow{(P|_B)^{\rm rev}}\ z\
\xrightarrow{a}\ z^a\
\xrightarrow{(Q|_A)^{\rm rev}}\ u^a.
\]
Their terminal missing \(b\)-edges, \(xx^b\) and \(u^au^{ab}\), are antipodal, so one has color \(1-s\). Again appending that edge gives a monochromatic full antipodal geodesic. \(\square\)

**Corollary 6 (phase coherence at a matched switch).** In a counterexample to NORI1, two one-change geodesics spanning adjacent codimension-two faces, with corresponding initial vertices, change vertices, and final vertices, must have the same initial edge color (and hence the same final edge color).

*Proof.* If their initial colors differed, their monochromatic blocks would satisfy Theorem 5. \(\square\)

**Role of the hypotheses.** The paths need only have matching initial, change, and terminal vertices across the \(a\)-translation; their within-block direction orders can differ. The conclusion arises from two competing monochromatic \((n-1)\)-edge routes whose missing edges form an antipodal pair. The central unresolved configuration for this method is two aligned one-change paths with the same phase.


**Theorem 7 (monochromatic-arm interface obstruction).** Continue to assume \(c(\bar e)=1-c(e)\), and fix adjacent \((n-2)\)-faces \(F,F^a\) with remaining fixed direction \(b\). Let \(P\) span \(F\) from \(u\) to \(x\), and let \(Q\) span \(F^a\) from \(u^a\) to \(x^a\). Suppose \(w\) is an interior vertex of \(P\) for which \(w^a\) is an interior vertex of \(Q\). All path portions mentioned below are nonempty.

(i) If \(P[u,w]\) and \(Q[w^a,x^a]\) are both monochromatic in color \(s\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-s\).

(ii) If \(Q[u^a,w^a]\) and \(P[w,x]\) are both monochromatic in color \(t\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-t\).

In particular, if both (i) and (ii) hold at the same projected vertex with \(s\ne t\), a monochromatic full antipodal geodesic exists.

*Proof.* The coordinate supports of \(P[u,w]\) and \(Q[w^a,x^a]\) are complementary within \(D=[n]\setminus\{a,b\}\), since their projected starts and ends are \(u,x\) and \(w\) occurs along both spanning geodesics. If \(c(ww^a)=s\), concatenating \(P[u,w]\), the \(a\)-edge, and \(Q[w^a,x^a]\) gives a monochromatic geodesic of length \(n-1\), which extends by Lemma 1. Thus failure of the monochromatic full-path conclusion forces \(c(ww^a)=1-s\). The proof of (ii) uses \(Q[u^a,w^a]\), the reverse \(a\)-edge, and \(P[w,x]\). Both directions use every coordinate in \(D\cup\{a\}\) once. When \(s\ne t\), the two required values \(1-s\) and \(1-t\) for the same \(a\)-edge are incompatible. \(\square\)

**Corollary 8 (ordered-switch separator).** Suppose \(P,Q\) are as in Theorem 7, with projected coordinate orders agreeing. Their words have one change each:
\[
w(P)=s^k(1-s)^{m-k},\qquad
w(Q)=(1-s)^\ell s^{m-\ell},
\quad m=n-2,\quad 1\le k,\ell<m.
\]
Let \(z_r\) be their common projected vertex after the first \(r\) coordinate directions. If no monochromatic full antipodal geodesic exists, then:
\[
\begin{cases}
c(z_rz_r^a)=s,&k<\ell,\ k\le r\le\ell,\\
c(z_rz_r^a)=1-s,&\ell<k,\ \ell\le r\le k.
\end{cases}
\]
If \(k=\ell\), a monochromatic full geodesic necessarily exists.

*Proof.* When \(k<\ell\), at each \(r\in[k,\ell]\) the \(Q\)-prefix and \(P\)-suffix are both monochromatic of color \(1-s\). Apply Theorem 7(ii). When \(\ell<k\), at each \(r\in[\ell,k]\) the \(P\)-prefix and \(Q\)-suffix have color \(s\). Apply Theorem 7(i). If \(k=\ell\), both arm conditions hold at \(z_k\), in opposite colors. \(\square\)

**Corollary 9 (oppositely oriented switch-band intersection).** Consider two pairs \((P,Q)\) and \((P',Q')\) of adjacent-face spanning one-change geodesics as in Corollary 8, having the same initial vertex \(u\in F\) and the same initial color \(s\) on their \(F\)-paths. The paired paths within each pair have a common projected coordinate order, though the orders of the two pairs may differ. Suppose the first pair has split indices \(k<\ell\), the second has split indices \(\ell'<k'\), and there is a vertex \(w\in F\) lying on both projected chains at a rank
\[
k\le d_F(u,w)\le\ell,\qquad
\ell'\le d_F(u,w)\le k'.
\]
Then a monochromatic full antipodal geodesic exists.

*Proof.* Corollary 8 applied to the first pair requires \(c(ww^a)=s\) in the absence of a monochromatic full geodesic, while the second pair requires \(c(ww^a)=1-s\). \(\square\)

These interface conditions provide a reachability-based target: in a hypothetical counterexample, switch bands of opposite orientation and initial phase \(s\) must avoid sharing a projected vertex. This moves the problem from single-path endpoint colors to the intersection geometry of entire families of colored maximal chains; obtaining such an intersection unconditionally remains open.


#### Theorem 10 (parallel-face switch bound)

Let \(n\geq 3\), and let \(c\) be an edge coloring of \(Q_n\) satisfying \(c(\bar e)=1-c(e)\). Let \(F\) be an \((n-2)\)-face with exterior directions \(a,b\). Suppose that \(P\subseteq F\) and \(Q\subseteq F^a\) are long geodesics terminating at corresponding vertices \(x\) and \(x^a\), respectively. Write \(r=\sigma(P)\), \(s=\sigma(Q)\), and
\[
\mu(c)=\min\{\sigma(R):R\text{ is a full antipodal geodesic of }Q_n\}.
\]
Then
\[
\boxed{\mu(c)\leq\max\{r,2\lceil s/2\rceil\}.} \tag{10.1}
\]
By interchanging \(F,F^a\), one obtains
\[
\boxed{
\mu(c)\leq
\min\bigl\{\max(r,2\lceil s/2\rceil),\,
\max(s,2\lceil r/2\rceil)\bigr\}.
} \tag{10.2}
\]
In particular, \(\mu(c)\leq\max(r,s)\) unless \(r=s\) is odd, in which case \(\mu(c)\leq r+1\). When \(r\neq s\) and \(\max(r,s)\) is odd, the stronger inequality \(\mu(c)\leq\max(r,s)-1\) holds.

*Proof.* Put \(p=c(\text{last edge of }P)\) and \(q=c(\text{last edge of }Q)\), and label the four edges of the square at \(x\) by
\[
A=c(xx^a),\qquad B=c(xx^b),\qquad
C=c(x^ax^{ab}),\qquad D=c(x^bx^{ab}).
\]
As \(P\) and \(Q\) each traverse every direction other than \(a,b\) once, adjoining either of the two possible two-edge square routes gives a full antipodal geodesic. The resulting switch numbers are
\[
\begin{array}{ll}
r+[p\neq A]+[A\neq C],&
r+[p\neq B]+[B\neq D],\\
s+[q\neq A]+[A\neq B],&
s+[q\neq C]+[C\neq D].
\end{array}\tag{10.3}
\]
By Lemma 2, any full geodesic with \(t\) changes implies \(\mu(c)\leq 2\lfloor t/2\rfloor\).

Set \(M=\max\{r,2\lceil s/2\rceil\}\). If \(r\) is even and \(M\geq r+2\), either completion of \(P\) has at most \(r+2\leq M\) changes. If \(r\) is odd and \(M\geq r+1\), every completion of \(P\) has at most \(r+2\) changes; since \(r+2\) is odd, Lemma 2 yields \(\mu(c)\leq r+1\leq M\). It remains to consider \(M=r\).

First suppose \(r\) is even. If \(\mu(c)>r\), the first two completions in (10.3) must each introduce two new changes: an increase of zero produces at most \(r\) changes, and an increase of one produces \(r+1\) changes, reducible to \(r\) by Lemma 2. Therefore
\[
A=B=1-p,\qquad C=D=p.
\]
One of the two square routes completing \(Q\) has both edges in color \(q\), so it introduces no additional changes. This gives \(\mu(c)\leq s\leq 2\lceil s/2\rceil\leq r\), a contradiction.

Now suppose \(r\) is odd. Then \(2\lceil s/2\rceil\leq r-1\). If \(s\leq r-2\), either completion of \(Q\) has at most \(s+2\leq r\) changes, which by Lemma 2 gives \(\mu(c)\leq r-1\). The remaining possibility is \(s=r-1\), necessarily even. Assuming \(\mu(c)>r\), each of the two completions of \(Q\) in (10.3) must introduce two changes, since at most one new change would give at most \(r\) changes and hence at most \(r-1\) after parity reduction. Thus
\[
A=C=1-q,\qquad B=D=q.
\]
Whichever value \(p\) has, one of the two square routes completing \(P\) consists of two edges of color \(p\). The resulting full geodesic has \(r\) changes; parity reduction gives \(\mu(c)\leq r-1\), again a contradiction.

This proves (10.1). Swapping \(F\) with \(F^a\) proves (10.2), and the final claims follow because \(\mu(c)\) is even. \(\square\)

**Geometric interpretation.** The terminal square has four candidate completions, two from each face. If the two completions of one path are both forced to exceed the proposed bound, their bridge-edge colors force a low-switch completion of the other. The bound is uniform in the dimension of the cube and in both face-path switch counts.
