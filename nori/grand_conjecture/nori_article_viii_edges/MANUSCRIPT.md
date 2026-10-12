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


Let \(n\ge5\), and let \(c\) color the undirected edges of \(Q_n\) with values in \(\{0,1\}\), subject to \(c(\bar e)=1-c(e)\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\). Let \(\sigma(P)\) denote the number of color changes on a full antipodal geodesic \(P\), and put \(\mu(c)=\min_P\sigma(P)\).

For \(0\le k\le n\) set \(m(k)=\min\{k,n-k\}\) and define
\[
\lambda_n(k)=
\begin{cases}
0,&m(k)=0,\\
\dfrac{4k(n-k)(m(k)-1)}{n(n-1)(n-2)},&0<m(k)<n/2,\\
\dfrac{4k(n-k)(m(k)-2)}{n(n-1)(n-3)},&m(k)=n/2.
\end{cases}\tag{1}
\]
The last case occurs only when \(n\) is even. Set
\[
q_n=\left\lfloor\frac{n-1}{3}\right\rfloor,\qquad
\Phi_n(k)=\frac{2k(n-k)}{n-1}-\frac{q_n}{2}\lambda_n(k).\tag{2}
\]

**Theorem 1 (unrestricted exchange-averaging bound).** Every antipodally odd coloring of the edges of \(Q_n\) satisfies
\[
\boxed{\mu(c)\le
2\left\lfloor
\frac{\max_{0\le k\le n}\Phi_n(k)-1}{2}
\right\rfloor.}\tag{3}
\]
No restriction is imposed on the dependence of an edge color on the other coordinates.

**Corollary 2 (dimension ten).** Every antipodally odd edge coloring of \(Q_{10}\) has a full antipodal geodesic with at most two changes:
\[
\boxed{\mu(c)\le2\qquad(n=10).}\tag{4}
\]

**Corollary 3 (linear bound in all dimensions).** Uniformly over antipodally odd edge colorings,
\[
\mu(c)\le \frac{28\sqrt7-40}{81}\,n+O(1)
       =0.42075354\ldots\,n+O(1).\tag{5}
\]

The proof counts disagreements between incident edge colors and improves the resulting average by exchanging disjoint pairs of consecutive directions.

**Lemma 4 (cyclic comparison identity).** Let \(P\) start at \(x\), traverse directions \(p_1,\ldots,p_n\), and have edge-color word \(w_1,\ldots,w_n\). Put \(v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s}\), and for distinct \(i,j\) write \(d_{ij}(v)=[c_i(v)\ne c_j(v)]\). Define
\[
T(P)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
                         +d_{p_n,p_1}(v_n).\tag{6}
\]
Then
\[
T(P)=\sum_{s=1}^{n-1}[w_s\ne w_{s+1}]
                         +[w_n\ne1-w_1]\tag{7}
\]
is a positive odd integer. A cyclic rotation of \(P\), with its root moved along the geodesic, has \(T(P)-1\) changes. If \(P\) is chosen uniformly among all \(2^n n!\) rooted full geodesics, and \(k_v=|\{i:c_i(v)=1\}|\), then
\[
\mathbb E T(P)=\frac{2}{(n-1)2^n}
                    \sum_{v\in Q_n}k_v(n-k_v).\tag{8}
\]

*Proof.* The first \(n-1\) terms of (6) are the successive comparisons in the word of \(P\). At \(v_n=\bar x\), the incoming \(p_n\)-edge has color \(w_n\), while the \(p_1\)-edge has color \(1-w_1\), by antipodal oddness. This proves (7). The XOR of its \(n\) comparison bits is one, hence \(T(P)\) is odd.

Moving the root across the first \(s\) directions and transferring those directions to the end gives the color word
\[
w_{s+1},\ldots,w_n,1-w_1,\ldots,1-w_s.
\]
Its \(n-1\) comparisons omit one of the \(n\) comparisons of (7), and the omitted position ranges over all \(n\) positions as \(s\) varies. One omitted comparison can be a change, giving \(T(P)-1\).

For a uniformly rooted full geodesic, at each of the \(n\) positions in (6) the vertex is uniform in \(Q_n\), and the incident directions form a uniform ordered pair of distinct directions. At vertex \(v\), there are \(2k_v(n-k_v)\) bichromatic ordered pairs among the \(n(n-1)\) possibilities. Adding their expected contributions over \(n\) positions proves (8). \(\square\)

**Lemma 5 (exchange gain from a colored vertex star).** Sample uniformly a vertex \(v\) and four distinct ordered directions \(h,i,j,\ell\). Consider a full geodesic with consecutive directions \(h,i,j,\ell\) such that its vertex after the \(h\)-step is \(v\). Let \(\Delta\) be the change in \(T\) when \(i,j\) are exchanged. Then
\[
\mathbb E|\Delta|\ge\frac1{2^n}\sum_{v\in Q_n}\lambda_n(k_v).\tag{9}
\]

*Proof.* Only the comparisons at the three vertices \(v,v^i\) or \(v^j\), and \(v^{ij}\) can change. Hence, with the sign convention new minus old,
\[
\begin{aligned}
\Delta={}&d_{h,j}(v)-d_{h,i}(v)
+d_{j,i}(v^j)-d_{i,j}(v^i)\\
&+d_{i,\ell}(v^{ij})-d_{j,\ell}(v^{ij}).\tag{10}
\end{aligned}
\]
Fix \(v,i,j,\ell\). The last four terms are independent of \(h\). When \(c_i(v)=c_j(v)\), use the lower bound zero. Otherwise the first two terms total \(+1\) or \(-1\), with the sign determined by \(c_h(v)\).

Let \(a,b\) count the directions of the two colors among the \(n-3\) remaining directions after excluding \(i,j,\ell\). For any real \(K\), the triangle inequality gives
\[
\frac{a|K+1|+b|K-1|}{n-3}
\ge\frac{2\min(a,b)}{n-3}.\tag{11}
\]
This bounds the conditional mean of \(|\Delta|\) over \(h\).

Fix \(k=k_v\), \(m=\min(k,n-k)\). The probability that uniformly chosen distinct \(i,j\) are bichromatic is \(2k(n-k)/(n(n-1))\). Conditional on this event, removal of \(i,j\) leaves color counts \(m-1,n-m-1\). Choose \(\ell\) uniformly from the other \(n-2\) directions. If \(m<n/2\), the mean of the smaller remaining color count after removal of \(\ell\) is \((m-1)(n-3)/(n-2)\). If \(m=n/2\), it is \(m-2\). Combining these quantities with (11) gives the two nonzero cases of \(\lambda_n(k)\) in (1). For \(m=0\), there are no bichromatic pairs. Average over \(v\) to obtain (9). \(\square\)

*Proof of Theorem 1.* Select the \(q=q_n\) adjacent pairs of positions
\[
(2,3),\ (5,6),\ (8,9),\ldots,
(2+3(q-1),3+3(q-1)).\tag{12}
\]
Each has a preceding and following direction. For a full geodesic \(P\), let \(\Delta_s(P)\) be the difference in \(T(P)\) caused by exchanging the directions in pair \(s\).

The three consecutive comparison positions affected by each exchange are disjoint from those affected by the other exchanges in (12). Exchanging a pair also preserves the vertex and used-coordinate set following its second step. Thus the changes are additive. Choosing the exchanges independently, the least comparison count among the resulting \(2^q\) orders is
\[
T(P)+\sum_{s=1}^q\min\{0,\Delta_s(P)\}.\tag{13}
\]
Now choose \(P\) uniformly among all rooted full geodesics. Swapping either specified pair is an involution of this uniform space, so \(\mathbb E\Delta_s(P)=0\). Using \(\min(0,z)=(z-|z|)/2\), equations (8)--(9) give
\[
\begin{aligned}
\mathbb E[\text{quantity in (13)}]
&\le\frac1{2^n}\sum_v
\left(\frac{2k_v(n-k_v)}{n-1}
-\frac q2\lambda_n(k_v)\right)\\
&\le \max_{0\le k\le n}\Phi_n(k).
\end{aligned}\tag{14}
\]
There is therefore a modified full geodesic with \(T\) no larger than the right side. Its \(T\) is odd. Lemma 4 and the parity of \(T\) give (3). \(\square\)

*Proof of Corollary 2.* For \(n=10\), \(q_n=3\) and \(\Phi_{10}(k)=\Phi_{10}(10-k)\). Substitution in (1)--(2), for \(k=0,1,2,3,4,5\), gives
\[
0,\quad2,\quad\frac{154}{45},\quad\frac{259}{60},
\quad\frac{71}{15},\quad\frac{305}{63}.
\]
Thus \(\max_k\Phi_{10}(k)=305/63<5\). The odd positive integer \(T\) of the supplied full geodesic is at most three. A root rotation therefore gives \(\mu(c)\le2\). \(\square\)

*Proof of Corollary 3.* Let \(t=\min(k,n-k)/n\in[0,1/2]\). Since \(q_n=n/3+O(1)\), equations (1)--(2) yield uniformly in \(k\)
\[
\frac{\Phi_n(k)}n
=2t(1-t)-\frac23t^2(1-t)+O(n^{-1}).\tag{15}
\]
The polynomial is maximized on \([0,1/2]\) at \(t_*=(4-\sqrt7)/3\), with value \((28\sqrt7-40)/81\). Insert this maximum into (3). \(\square\)

The inequalities constrain every admissible coloring through the degrees of the two colors at its vertices. They combine antipodal root rotation with several simultaneously available path exchanges. The ten-dimensional conclusion does not require an inductive hypothesis or a structural classification of face colorings.

Let \(n\ge5\), and let \(c\) be an antipodally odd coloring of the undirected edges of \(Q_n\). Write \(c_i(v)\) for the color of the edge in direction \(i\) incident with \(v\), and set
\[
d_{ij}(v)=[c_i(v)\ne c_j(v)],\qquad
k_v=\sum_i c_i(v),\qquad m_v=\min(k_v,n-k_v).
\]
For \(i\ne j\), put \(v^{ij}=v\oplus e_i\oplus e_j\) and define the square curvature
\[
\kappa_{ij}(v)=c_i(v)\oplus c_j(v^i)\oplus c_i(v^j)\oplus c_j(v).
\tag{1}
\]
All sums in (1) are modulo two. Since \(c_i(v^j)=c_i(v^{ij})\) and \(c_j(v^i)=c_j(v^{ij})\), we have
\[
\boxed{\kappa_{ij}(v)=d_{ij}(v)\oplus d_{ij}(v^{ij}).}\tag{2}
\]
Thus curvature is the disagreement between the two opposite-vertex bichromatic-turn indicators of a square.

Recall the functions \(\lambda_n(k)\), \(\Phi_n(k)\), and \(q_n=\lfloor(n-1)/3\rfloor\) from the preceding cyclic-turn exchange theorem. Define
\[
\eta_n(k)=
\begin{cases}
0,&\min(k,n-k)=0,\\[1mm]
\dfrac{2(\min(k,n-k)-1)}{n-2}
+\dfrac{\mathbf1_{\{n\ {\rm even},\,k=n/2\}}}{n-3},
&\min(k,n-k)\ge1,
\end{cases}
\tag{3}
\]
and the nonnegative curvature-weighted statistic
\[
\mathcal K_n(c)=
\frac1{2^n n(n-1)}
\sum_{v\in Q_n}\sum_{i\ne j}
[d_{ij}(v)=1,\ d_{ij}(v^{ij})=0]\,
\eta_n(k_v).
\tag{4}
\]

**Theorem 1 (curvature-sensitive all-dimensional exchange bound).** Every antipodally odd edge coloring of \(Q_n\), \(n\ge5\), satisfies
\[
\boxed{\displaystyle
\mu(c)\le 2\left\lfloor
\frac{\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)-1}{2}
\right\rfloor.}
\tag{5}
\]
In particular, a counterexample to \(\mu(c)\le2\) in dimension \(n\) must satisfy
\[
\boxed{\displaystyle
\frac1{2^n}\sum_v\Phi_n(k_v)
-\frac{q_n}{2}\mathcal K_n(c)\ge5.}
\tag{6}
\]
The improvement over the earlier exchange bound is additive and nonnegative for every coloring, with a positive contribution whenever some curved square has a bichromatic corner at which both edge colors occur at least twice.

**Proof.** For a uniformly chosen vertex \(v\) and distinct ordered directions \(h,i,j,\ell\), form the two full geodesics differing by the exchange of adjacent directions \(i,j\) inside the consecutive block \(h,i,j,\ell\), with \(v\) immediately after \(h\). Let \(\Delta\) be the change in their cyclic turn counts. Set \(w=v^{ij}\). The comparison formula established in the preceding exchange lemma is
\[
\Delta=d_{hj}(v)-d_{hi}(v)
+d_{ij}(v^j)-d_{ij}(v^i)
+d_{i\ell}(w)-d_{j\ell}(w).\tag{7}
\]
Here \(d_{ij}=d_{ji}\). The middle difference is zero if \(d_{ij}(v)=d_{ij}(w)\), and is \(+1\) or \(-1\) otherwise; this follows from the four-corner identity
\[
d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(w)=0.\tag{8}
\]

There are four possibilities for \((d_{ij}(v),d_{ij}(w))\).

When it equals \((0,0)\), all three differences in (7) vanish.

When it equals \((1,1)\), the middle difference vanishes and each outer difference is \(+1\) or \(-1\). Fixing \(\ell\), the first difference takes these two signs as the color of \(h\) varies. There are \(n-3\) choices of \(h\), with color multiplicities \(a,b\) among these directions. The triangle inequality shows that the mean of \(|\Delta|\) over \(h\) is at least \(2\min(a,b)/(n-3)\). Averaging over \(\ell\) yields the lower bound
\[
g_n(k_v)=
\begin{cases}
\dfrac{2(m_v-1)}{n-2},&2m_v<n,\\
\dfrac{2(m_v-2)}{n-3},&2m_v=n,
\end{cases}\tag{9}
\]
provided \(d_{ij}(v)=1\).

When the pair is \((1,0)\), the last difference vanishes, and the middle difference has absolute value one. The first difference has the two possible signs according to the color of \(h\). Since \(h\) is uniform among the \(n-2\) directions outside \(\{i,j\}\), the mean satisfies
\[
\mathbb E_{h,\ell}|\Delta|
\ge g_n'(k_v):=\frac{2(m_v-1)}{n-2}.\tag{10}
\]
Thus relative to the bound (9), this case supplies the extra \(g_n'(k_v)-g_n(k_v)\), which is \(1/(n-3)\) when \(n\) is even and \(k_v=n/2\), and zero otherwise.

Finally, when the pair is \((0,1)\), the first difference vanishes and the middle difference has absolute value one. The last difference, as \(\ell\) varies among the \(n-2\) remaining directions, has two possible signs. Consequently
\[
\mathbb E_{h,\ell}|\Delta|\ge g_n'(k_w).\tag{11}
\]
Averaging (11) over uniformly chosen \(v,i,j\) and replacing \(v\) by \(w=v^{ij}\) identifies its contribution with the \((1,0)\) cases, weighted by \(g_n'(k_v)\). Combining the four cases, using (9)--(11), gives
\[
\boxed{
\mathbb E|\Delta|
\ge \frac1{2^n}\sum_v\lambda_n(k_v)+\mathcal K_n(c).
}\tag{12}
\]
Indeed, the first term is the mean over bichromatic ordered pairs at \(v\) of the bound \(g_n(k_v)\), and the remaining two contributions total \(2g_n'-g_n=\eta_n\) on the \((1,0)\) cases.

Apply the \(q_n\) independent position-pair exchanges from the preceding theorem. Their changes in cyclic turn count are additive; each has mean zero and has the absolute-change estimate (12). As before, averaging over the initial rooted geodesic and choosing the better orientation of every exchange gives a full geodesic with odd cyclic turn count at most
\[
\frac1{2^n}\sum_v\Phi_n(k_v)-\frac{q_n}{2}\mathcal K_n(c).
\]
Cyclically rotating its coordinate order removes one changed comparison, proving (5). If \(\mu(c)>2\), then this odd turn count is at least five, yielding (6). \(\square\)

**Corollary 2 (a restriction on eleven-dimensional counterexamples).** Suppose \(n=11\) and every vertex is incident with five or six edges of color one. Let
\[
\delta(c)=
\frac{\#\{\text{two-dimensional faces with odd curvature}\}}
{\binom{11}{2}2^9}.
\tag{13}
\]
Then
\[
\boxed{
\mu(c)\le
2\left\lfloor\frac{58/11-(2/3)\delta(c)-1}{2}\right\rfloor.
}\tag{14}
\]
In particular, \(\delta(c)>9/22\) implies \(\mu(c)\le2\). Every putative four-switch example with balanced incident-color degrees must have \(\delta(c)\le9/22\).

*Proof.* At every vertex, \(\Phi_{11}(k_v)=58/11\) and \(m_v=5\), so \(\eta_{11}(k_v)=8/9\). On each odd-curvature square, precisely two of its four vertices satisfy \(d_{ij}(v)=1\) and \(d_{ij}(v^{ij})=0\). Counting both orders of \(i,j\) gives \(\mathcal K_{11}(c)=(4/9)\delta(c)\). Since \(q_{11}=3\), substitute in (5). \(\square\)

The curvature statistic also obeys an independent parity law.

**Theorem 3 (antipodal reversal holonomy).** Let \(P\) be any full antipodal geodesic, rooted at \(x\), with direction order \(p_1,\ldots,p_n\). Reverse this order at the same root by adjacent exchanges. If \(S_1,\ldots,S_{\binom n2}\) are the successive squares traversed by any reduced adjacent-transposition reversal, then
\[
\boxed{\bigoplus_{r=1}^{\binom n2}\kappa(S_r)=n\pmod2.}\tag{15}
\]
Consequently, in every odd dimension, every such reversal sequence encounters an odd number of curved squares. Writing \(\delta_{ij}\) for the proportion of curved squares parallel to directions \(i,j\), every admissible coloring in odd dimension satisfies
\[
\boxed{\sum_{i<j}\delta_{ij}\ge1,\qquad
\delta(c):=\frac1{\binom n2}\sum_{i<j}\delta_{ij}
\ge \frac1{\binom n2}.}\tag{16}
\]
The second bound is sharp even among colorings for which every vertex is incident with \((n-1)/2\) or \((n+1)/2\) edges of color one.

*Proof.* Let \(w_1,\ldots,w_n\) be the edge colors along \(P\). The geodesic with reversed direction order and the same root has colors \(1-w_n,\ldots,1-w_1\), because each of its edges is antipodal to the corresponding edge of \(P\). Therefore the parity of the sum of its edge colors differs by \(n\pmod2\). Each adjacent transposition replaces a two-edge route across a square by the other two-edge route, changing this parity by the square curvature. Summing over the reversal proves (15).

For odd \(n\), the number of curved squares in every reversal is odd and positive. Choose the root and the original order uniformly. Each unordered direction pair is exchanged once in the reduced reversal, and the square at which it is exchanged is uniform among the \(2^{n-2}\) squares of those directions (by translation symmetry of the sampled root). Hence the expected number of curved squares in the reversal is \(\sum_{i<j}\delta_{ij}\), proving (16).

For sharpness, write \(n=2m+1\), designate the final coordinate by \(u\), and on an edge in direction \(i\) assign
\[
c_{2a-1}(v)=v_u,\qquad c_{2a}(v)=1-v_u
\quad(1\le a\le m),\qquad
c_u(v)=v_1\oplus\cdots\oplus v_{2m-1}.
\tag{17}
\]
These values are independent of the coordinate being traversed, so define undirected-edge colors. All defining functions change under complementation of every coordinate, making the coloring antipodally odd. Every pair \(2a-1,2a\) contributes one edge of each color at every vertex, while direction \(u\) contributes either color; the degree condition follows. The curvature vanishes on every direction pair except \(\{2m,u\}\), and every square in that pair has curvature one. Thus \(\sum_{i<j}\delta_{ij}=1\), proving sharpness. \(\square\)

Theorems 1 and 3 combine two complementary constraints on unrestricted instances: color imbalance at individual vertex stars governs the baseline cyclic turn count, while nonflat two-faces force extra exchange opportunities. The sharpness example shows that parity alone supplies only \(O(n^{-2})\) square-curvature density in odd dimension; stronger dimension-uniform conclusions require additional correlations between these local statistics.

Fix \(n\ge3\), and let \(V=\{0,1\}^n\). For each vertex \(v\) and distinct coordinate directions \(i,j\), consider a symmetric binary array \(D=(d_{ij}(v))\), with \(d_{ij}(v)=d_{ji}(v)\). Write \(v^i=v\oplus e_i\) and \(\bar v=v\oplus(1,\ldots,1)\). We impose the following relations:
\[
\begin{array}{ll}
\text{triangle:}&d_{ij}(v)\oplus d_{jk}(v)\oplus d_{ik}(v)=0
\quad(i,j,k\text{ distinct}),\\
\text{square:}&d_{ij}(v)\oplus d_{ij}(v^i)\oplus
d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0,\\
\text{antipodal:}&d_{ij}(\bar v)=d_{ij}(v).
\end{array}\tag{1}
\]
For a root \(x\) and an ordering \(\pi=(p_1,\ldots,p_n)\) of the directions, put
\[
v_s=x\oplus e_{p_1}\oplus\cdots\oplus e_{p_s},
\quad v_n=\bar x,
\]
and define its cyclic turn sum
\[
\Theta_D(x,\pi)=
\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s)
+d_{p_n,p_1}(\bar x),\tag{2}
\]
where the sum in (2) is over the ordinary integers.

**Theorem 1 (complete reconstruction from incidence disagreements).** Suppose \(D\) satisfies the triangle and square relations of (1). There is an undirected-edge coloring \(c:E(Q_n)\to\{0,1\}\) such that
\[
\boxed{d_{ij}(v)=c_i(v)\oplus c_j(v)
\quad\text{for all }v,\ i\ne j,}\tag{3}
\]
where \(c_i(v)\) is the color of the edge in direction \(i\) incident with \(v\). The coloring is unique up to complementation of all edge colors.

If \(D\) also satisfies the antipodal relation, the reconstructed coloring obeys
\[
c_i(\bar v)=c_i(v)\oplus\varepsilon
\quad\text{for every }v,i,\tag{4}
\]
with one constant \(\varepsilon\in\{0,1\}\). Moreover
\[
\boxed{\Theta_D(x,\pi)\equiv\varepsilon\pmod2
\quad\text{for every root and every ordering}.}\tag{5}
\]
Consequently, \(D\) arises from an antipodally odd edge coloring if and only if it satisfies all three relations of (1) and \(\Theta_D(x,\pi)\) is odd for one (equivalently every) root and ordering. For such an array, the compatible antipodally odd edge colorings are precisely a complementary pair.

*Proof.* Fix a reference direction \(1\), and define vertex functions
\[
r_1(v)=0,\qquad r_i(v)=d_{1i}(v)\quad(i\ne1).\tag{6}
\]
The triangle relation implies \(r_i(v)\oplus r_j(v)=d_{ij}(v)\) for all distinct \(i,j\).

For every direction \(i\), define an edge cochain
\[
a_i(v)=r_i(v)\oplus r_i(v^i).\tag{7}
\]
It has the same value at the two endpoints of an \(i\)-edge. Its sum around any square in directions \(i,j\) equals
\[
\begin{aligned}
&a_i(v)\oplus a_j(v^i)\oplus a_i(v^j)\oplus a_j(v)\\
&\qquad=d_{ij}(v)\oplus d_{ij}(v^i)
\oplus d_{ij}(v^j)\oplus d_{ij}(v^{ij})=0.\tag{8}
\end{aligned}
\]
Thus \(a\) is a gradient on the cube: a binary vertex function \(f\) exists satisfying
\[
f(v)\oplus f(v^i)=a_i(v)\quad\text{for every }v,i.\tag{9}
\]
For completeness, construct \(f(v)\) by summing \(a\) along any path from the zero vertex to \(v\). Backtracking along an edge changes the sum by zero; interchanging two consecutive different coordinate steps changes it by the square sum (8), also zero. Such operations connect any two cube walks with the same endpoints, so the definition is independent of the walk.

Set
\[
c_i(v)=r_i(v)\oplus f(v).\tag{10}
\]
Equations (7) and (9) give \(c_i(v)=c_i(v^i)\), so (10) defines a coloring of undirected edges. Equation (6) and the triangle relation yield
\(c_i(v)\oplus c_j(v)=d_{ij}(v)\), proving existence.

For uniqueness, suppose \(c'\) has the same incidence disagreements. At every vertex, the values \(c_i'(v)\oplus c_i(v)\) are independent of \(i\); call this value \(b(v)\). As both colorings are constant along each edge in its direction, \(b(v)=b(v^i)\) for every \(i\), hence \(b\) is constant on the connected cube. Therefore \(c'=c\) or \(c'=1-c\).

Assume now the antipodal relation of (1). At vertex \(v\),
\[
[c_i(\bar v)\oplus c_i(v)]\oplus
[c_j(\bar v)\oplus c_j(v)]
=d_{ij}(\bar v)\oplus d_{ij}(v)=0.
\]
So \(\varepsilon(v):=c_i(\bar v)\oplus c_i(v)\) is independent of \(i\). Evaluating at vertices \(v,v^i\), using the \(i\)-edge at each and its antipodal edge, gives \(\varepsilon(v^i)=\varepsilon(v)\). Connectivity implies one constant \(\varepsilon\), proving (4).

Let \(w_1,\ldots,w_n\) be the edge-color word on the geodesic rooted at \(x\) with direction order \(\pi\). Each interior term of (2) equals \(w_s\oplus w_{s+1}\). Its final term equals \(w_n\oplus w_1\oplus\varepsilon\), because the \(p_1\)-edge at \(\bar x\) has color \(w_1\oplus\varepsilon\). The XOR of these \(n\) terms is \(\varepsilon\), proving (5). The stated criterion follows. \(\square\)

**Theorem 2 (intrinsic switch-count and counterexample criterion).** Suppose \(D\) satisfies the four requirements of Theorem 1, including odd cyclic turn parity, and let \(c\) be either reconstructed coloring. Then
\[
\boxed{\displaystyle
\mu(c)=\min_{x,\pi}\Theta_D(x,\pi)-1.}\tag{11}
\]
In particular,
\[
\boxed{
\mu(c)\le2\iff
\Theta_D(x,\pi)\le3
\text{ for some }x,\pi,}\tag{12}
\]
and a hypothetical unrestricted counterexample to the two-switch bound is equivalently an array obeying (1) and oddness for which
\[
\boxed{\Theta_D(x,\pi)\ge5\quad
\text{for every }x,\pi.}\tag{13}
\]
The values of \(\mu(c)\), the set of roots of low-switch geodesics, and their endpoint sets are determined by \(D\).

*Proof.* The number of color changes on the path with root \(x\) and order \(\pi\) is
\[
\sigma_c(x,\pi)=\sum_{s=1}^{n-1}d_{p_s,p_{s+1}}(v_s).\tag{14}
\]
Thus \(\Theta_D(x,\pi)\) is \(\sigma_c(x,\pi)\) plus a binary seam comparison, and it is always odd by Theorem 1. Cyclically rotate the direction order, changing the root from \(x\) to one of the intermediate vertices along the original path. As in the cyclic comparison identity, the resulting color words are successive cyclic shifts of
\[
w_1,\ldots,w_n,1-w_1,\ldots,1-w_n.
\]
The rotations preserve \(\Theta_D\) and respectively omit each of its \(n\) seam comparisons. Since \(\Theta_D\) is odd, at least one comparison is a change, and some rotation has \(\Theta_D-1\) changes.

Conversely, every geodesic has \(\sigma_c\ge\Theta_D-1\), because its seam comparison is at most one. Applying the preceding rotation to a geodesic minimizing \(\Theta_D\) proves (11). Oddness of \(\Theta_D\) yields (12)--(13). Equation (14) proves the statement about roots and endpoints. \(\square\)

**Corollary 3 (size of the unrestricted class).** For \(n\ge3\), the arrays \(D\) satisfying (1) and the oddness condition constitute an affine binary space of dimension
\[
\boxed{n\,2^{n-2}-1.}\tag{15}
\]

*Proof.* The \(n2^{n-1}\) undirected edges of \(Q_n\) form \(n2^{n-2}\) disjoint antipodal pairs. Choosing one edge color per pair determines an antipodally odd coloring, so these colorings form an affine binary space of dimension \(n2^{n-2}\). Their passage to \(D\) is linear with a one-dimensional kernel, namely uniform global color complementation, by Theorem 1. Its image therefore has affine dimension \(n2^{n-2}-1\). \(\square\)

The reconstruction identifies local consistency conditions sufficient to recover all unrestricted edge colorings up to their irrelevant global color phase. In particular, the low-switch problem may be phrased entirely in terms of antipodally even vertex-indexed incidence disagreements, subject to triangle, square and one global oddness constraint. The cyclic comparison and curvature-sensitive exchange inequalities then become inequalities intrinsic to \(D\); any low-switch terminal-alignment argument can be formulated in the same data without committing to a choice of edge-color phase.
