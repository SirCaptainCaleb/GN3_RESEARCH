# Article VIII - Antipodally odd edge colorings

## Article setting and orientation

The separate NORI1 problem remains open for arbitrary antipodally odd colorings of undirected physical cube edges. Its significant unconditional results already include the full affine-span theorem for direction-indexed colors along complete antipodal geodesics and universal simultaneous prescription on three selected directions.

The multifacet bridge establishes an exact dimension-prescription equivalence: for each k, general one-switch geodesic closure in an arbitrary k-cube corresponds to prescribing arbitrary colors on any k selected directions in every larger antipodally odd physical-edge cube. With the established finite-dimensional input, this proves universal seven-direction prescription. None of these theorems, by itself, supplies an all-monochromatic full geodesic in arbitrary dimension.

*Full Article composition: [source manuscript](../nori_article_viii_edges.md).*

## Central edge carriers and antipodal topology

The physical-edge problem retains genuine positive theorems independent of any affine modeling hypothesis. Full antipodal geodesic color-profile vectors have affine span equal to the entire binary direction-color space, and every choice of colors on three prescribed original directions occurs on a full geodesic. These results do not yet guarantee the one completely constant color vector.

The multifacet bridging theorem identifies unrestricted k-dimensional one-switch closure with simultaneous prescription on any k selected directions in all larger antipodally odd cubes, preserving physical edge identities. In particular, established dimension-eight closure input yields universal seven-direction prescription; the unrestricted eight-direction case remains open under the theorem's stated equivalence.

*Full Section composition: [source manuscript](nori_edge_central_carriers.md).*

### Full-geodesic color profiles span the entire binary space

# The full-geodesic color-profile span theorem for unrestricted NORI1

Let \(n\ge2\) and let \(c_i(u)\in\mathbb F_2\) be the color of the **physical undirected** edge \(\{u,u\oplus e_i\}\) of the Boolean cube \(Q_n\). Assume the exact NORI1 conditions
\[
c_i(u\oplus e_i)=c_i(u),\qquad
c_i(\bar u)=1\oplus c_i(u)
\tag{1}
\]
for every direction \(i\) and cube vertex \(u\). No linearity, locality, exterior-support, regularity, or direction-independence is assumed.

For a starting root \(u\in Q_n\) and a permutation \(p\) of all \(n\) coordinates, traverse the genuine full antipodal geodesic in the order \(p\). Record its edge-color vector **indexed by original coordinate direction**, independently of the order in which those directions were used:
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
assumes **both** binary values among genuine full antipodal cube geodesics. Thus the attainable full-profile family obeys *no nontrivial universal affine parity identity* for any legal NORI1 coloring, even when the coloring is nonlinear.

**Proof.** Suppose (3) fails. Linear algebra over \(\mathbb F_2\) supplies a nonzero vector \(y=(y_i)\in\mathbb F_2^n\) and a constant \(\kappa\) such that
\[
\bigoplus_i y_iw_i(u,p)=\kappa
\tag{4}
\]
for **every** root \(u\) and full coordinate permutation \(p\).

Give each physical edge in direction \(i\) the mod-two weight
\[
\omega_i(u)=y_i c_i(u).
\tag{5}
\]
Because \(c_i\) is an undirected physical-edge color, \(\omega_i(u\oplus e_i)=\omega_i(u)\).

Fix any physical square with corner \(u\) and distinct directions \(i,j\). Compare two full antipodal geodesics *from the same root* \(u\): the first starts with directions \((i,j)\), the second with \((j,i)\), and both use **the same order of all remaining directions**. They reach the same vertex after two moves, so every later physical edge is identical. Subtracting the two instances of (4) therefore gives the exact square-closedness equation
\[
\omega_i(u)\oplus\omega_j(u\oplus e_i)
\oplus\omega_j(u)\oplus\omega_i(u\oplus e_j)=0.
\tag{6}
\]
Every square is realized by such a pair of genuine full geodesics; no based-window or abstract-face identification has been used.

Since every square has zero mod-two curvature, the edge cochain \(\omega\) is a gradient on the Boolean cube:
\[
\omega_i(u)=\phi(u)\oplus\phi(u\oplus e_i)
\tag{7}
\]
for some vertex potential \(\phi:Q_n\to\mathbb F_2\). For completeness, fix \(\phi(0)=0\), and define \(\phi(u)\) by integrating \(\omega\) along any cube path from \(0\) to \(u\). Any two such paths differ by backtrack cancellations and elementary square swaps; physical edge invariance and (6) make their integrals equal. Thus (7) follows.

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

**Corollary (arbitrary prescribed colors on two directions).** Fix any **two distinct coordinate directions** \(i,j\) and any pair \((a,b)\in\mathbb F_2^2\). There exists a genuine *full antipodal cube geodesic*, with some starting root and permutation of **all \(n\) directions**, whose edge in direction \(i\) has color \(a\) and whose edge in direction \(j\) has color \(b\).

**Proof.** Projection of (3) onto the \(i,j\) coordinates implies that the attainable pair-profile set has full affine span \(\mathbb F_2^2\). From (1), changing the root from \(u\) to \(\bar u\) while keeping the same direction order replaces every color \(w_i(u,p)\) by its complement. Hence the pair-profile set is closed under
\[
(a,b)\longmapsto(1\oplus a,1\oplus b).
\]
The only complement-invariant subset of \(\mathbb F_2^2\) with full affine span is the entire four-element set. \(\square\)

**Quantitative and constructive formulation.** Every legal coloring has at least \(n+1\) affinely independent realized direction-indexed full-geodesic profiles. For any prescribed nonzero functional \(y\), witnesses of opposite \(y\)-parity can be constructed by one of two physically exact mechanisms:

* If the weighted cochain \(\omega_i=y_ic_i\) has nonzero curvature on some square, the two full orders beginning with that square's directions in opposite orders give opposite \(y\)-parities at the same root.
* If every square has zero curvature, construct the potential \(\phi\) in (7), choose any \(i\) with \(y_i=1\), and use two full paths with the same coordinate order and roots differing by \(e_i\). Equation (9) shows their \(y\)-parities are opposite.

Thus the result is not merely an existential use of linear algebra: the proof isolates an explicit **adjacent-swap versus single-root-flip dichotomy** for every nonzero parity functional.

**Mathematical significance and exact gap.** This theorem is a statement about **every** antipodally odd *physical-edge* NORI1 coloring. It establishes unrestricted two-direction prescription and excludes all affine-linear parity certificates for the nonattainment of full color words. These conclusions rely on global consistency of physical square edges and antipodal oddness, rather than on affine formulas for the edge colors. They sharpen the partial-geodesic and restricted affine-family perspectives by identifying a global algebraic universality property that holds in the entire still-open class.

Full affine **span** of \(\mathcal W(c)\) does not imply \(\mathcal W(c)=\mathbb F_2^n\), nor that either constant vector \(0^n\) or \(1^n\) is attained. Full monochromatic NORI1 remains open. The precise missing implication is an additional *joint higher-order compatibility theorem* raising these independent parity separations and two-coordinate prescriptions to an all-coordinate word realization (or merely a monochromatic full word). The theorem also makes no claim about unrestricted ordinary boundary 3-tournaments; there the colored objects are ordered triples, and the square-gradient identity of physical edges has no direct analogue.


### Universal three-direction edge-color prescription

# Universal three-direction prescription for unrestricted antipodally odd cube-edge colorings

**Theorem.** Let \(n\ge3\) and let \(c_i(x)\in\mathbb F_2\) color each *physical undirected* direction-\(i\) edge of \(Q_n\), satisfying
\[
c_i(x)=c_i(x\oplus e_i),\qquad c_i(\bar x)=1+c_i(x).
\]
For **every** three distinct directions \(i,j,k\) and **every** prescribed color triple \((t_i,t_j,t_k)\in\mathbb F_2^3\), some genuine full antipodal geodesic (root and complete permutation unrestricted) traverses its \(i\)-, \(j\)- and \(k\)-edges in exactly the prescribed colors. Equivalently, the set \(\mathcal W(c)\) of full direction-indexed edge-color profiles projects **surjectively** to \(\mathbb F_2^3\) on every three-coordinate set. There are no restrictions on nonlinearity, exterior dependence, or the colors of the remaining \(n-3\) edges.

**Root-rotation identity.** For a full geodesic with root \(x\) and direction order \(p=(p_1,\ldots,p_n)\), use root \(x\oplus e_{p_1}\) and order \((p_2,\ldots,p_n,p_1)\). The new path traverses the *same physical edges* in all directions other than \(p_1\). Its final \(p_1\)-edge is antipodal to the original first edge; thus its direction-indexed color profile is the original profile with precisely coordinate \(p_1\) complemented. This relies on both undirected physicality and edge antipodal oddness.

**Proof.** Suppose some prescribed triple never occurs. Complement the color of *every physical edge* in direction \(r\in\{i,j,k\}\) by \(t_r\), leaving all other edge directions alone. Both edge axioms survive, and the impossible triple becomes \(000\). Taking the antipodal root of any full geodesic with the **same** coordinate order complements every direction's color, so \(111\) is also impossible.

Choose an arbitrary root \(x\) and complete direction order \(p=(i,j,k,r_4,\ldots,r_n)\); write \(A,B,D\) for the actual edge colors at its first three steps. Rotate the first direction to the end three times, updating the root as above. The four resulting **genuine full antipodal geodesics** have projected triples
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

Now compare the two full direction orders \((i,j,k,r_4,\ldots,r_n)\) and \((j,i,k,r_4,\ldots,r_n)\) *from the same arbitrary root \(x\)*. They traverse the **same physical \(k\)-edge** at their third step, since in both cases they have already flipped exactly the directions \(i,j\). By (2), the first color on each path equals its common third color. Therefore
\[
c_i(x)=c_j(x)\qquad\text{for every }x\in Q_n. \tag{3}
\]
Apply (3) also at \(x\oplus e_i\) and use that \(c_i\) is the color of an **undirected** \(i\)-edge:
\[
c_j(x\oplus e_i)=c_i(x\oplus e_i)=c_i(x).
\]
But these are exactly the colors of the first and second edges in the original path with prefix \((i,j,k)\), and (2) demands that those two colors are *different*. Contradiction. Thus every prescribed triple occurs. \(\square\)

**Research significance and exact limitation.** This strengthens NORI's previously recorded unrestricted **two-direction prescription** corollary to **three-direction prescription** for the *whole* NORI1 class. Full affine span of the profile set by itself does not imply triple surjectivity; the essential new ingredient is that cyclic geodesic root slides realize the three-cube walk (1), whose avoidance of one antipodal pair is rigid. Any failure to realize a *complete* target \(n\)-bit word must therefore involve compatibility among **at least four directions**, not a missing one-, two-, or three-direction marginal. The result does not yet force the all-zero or all-one full profile and does not solve unrestricted NORI1. It also does not prove a statement for ordered-three-face boundary tournaments: here the local colors attach to actual edges, and the root slide complements exactly one direction-indexed edge color.

**Consistency check (not used in proof).** Direct enumeration of all \(2^{16}\) legal physical antipodally odd edge colorings of \(Q_4\) found complete four-bit profile coverage; separate binary-integer feasibility tests found no obstruction to triple prescription in dimensions five, six, and seven. The argument above is valid in every dimension independently of these checks.

### Antipodal multifacet bridge and seven-coordinate universality

# Antipodal multifacet bridging: an exact localization theorem for unrestricted NORI1

## Statement and historical context

Let \(k\ge2\). Define \(B_k\) to be the **Leader–Long/Feder–Subi geodesic one-switch assertion in dimension \(k\)**:

> Every arbitrary binary coloring \(d\) of the *undirected physical edges* of \(Q_k\) admits a **full antipodal geodesic** whose edge-color sequence changes at most once.

Unlike NORI1, \(d\) need not satisfy any antipodal relation. For integers \(n>k\), and a fixed \(k\)-set \(S\subseteq[n]\), define \(P_{n,S}\) to be the **full geodesic partial-color prescription assertion**:

> For every antipodally odd coloring \(c\) of the genuine undirected physical edges of \(Q_n\), and every target \(t\in\mathbb F_2^S\), there exist a physical root \(x\) and a permutation \(p\) of **all \(n\) directions** such that the full antipodal geodesic \(P(x,p)\) traverses its unique edge in each direction \(i\in S\) with color exactly \(t_i\). The colors in the other \(n-k\) directions are unrestricted.

This is an exact property of all legal NORI1 colorings, not a condition on affine or direction-only subclasses.

**Theorem 1 (multifacet bridge equivalence).** For every \(k\ge2\), every \(n>k\), and every fixed \(k\)-set \(S\subseteq[n]\),
\[
\boxed{\quad B_k\quad\Longleftrightarrow\quad P_{n,S}.\quad}
\tag{1}
\]
In particular, the property that *every* legal antipodally odd physical-edge coloring in *any one larger dimension* realizes all prescribed colors on *one specified set of \(k\) directions* is equivalent to the arbitrary-color \(k\)-cube one-switch geodesic assertion.

The implication \(B_k\Rightarrow P_{n,S}\) uses **all** \(n-k\) exterior directions as a single antipodal bridge between opposite physical \(k\)-faces; no colors along the bridge need to be specified.

## Proof of the forward implication

Assume \(B_k\). Fix \(n>k\), \(S\), a legal physical antipodally odd edge coloring \(c\) of \(Q_n\), and an arbitrary target \(t=(t_i)_{i\in S}\).

Identify \(Q_n=Q_S\times Q_D\) with \(D=[n]\setminus S\ne\varnothing\); write a cube vertex as \((u,z)\). Fix an **arbitrary** exterior vertex \(z\in Q_D\). On the *lower physical \(S\)-face* \(Q_S\times\{z\}\), define an arbitrary undirected-edge coloring
\[
d_i(u):=c_i(u,z)\oplus t_i,\qquad i\in S.
\tag{2}
\]
This is a legal physical \(k\)-cube edge coloring because \(c_i(u,z)=c_i(u\oplus e_i,z)\); **no** antipodal oddness is assumed for \(d\).

By \(B_k\), there exists a full antipodal geodesic \(R\) of \(Q_S\) whose \(d\)-color word has at most one change. Reverse its traversal if needed so its word is \(0^a1^{k-a}\), with \(0\le a\le k\). Write
\[
R:\ u_0\xrightarrow{U}u_a\xrightarrow{V}\bar u_0
\tag{3}
\]
where \(U\) and \(V\) denote ordered, disjoint lists of \(S\)-directions whose union is \(S\), with all edges of \(U\) having \(d\)-color 0 and all edges of \(V\) having \(d\)-color 1. Empty \(U\) and \(V\) are permitted.

Now construct a **genuine full \(n\)-direction cube geodesic**, starting at \((u_a,z)\):

1. Traverse the \(U\)-edges in reverse order inside the lower physical facet, moving \((u_a,z)\to(u_0,z)\).
2. Traverse *every* direction of \(D\) exactly once, in any order, moving \((u_0,z)\to(u_0,\bar z)\).
3. Follow the **reverse of the \(Q_S\)-antipodal image of the \(V\)-suffix** from (3), inside the upper physical facet, moving \((u_0,\bar z)\to(\bar u_a,\bar z)\).

All \(n\) directions are used exactly once, so the constructed path is a genuine full antipodal geodesic. On its \(U\)-edges, the lower-facet formula (2) and the undirected reversal of the 0-block give actual \(c\)-color \(t_i\). On its \(V\)-edges, each upper-facet edge is the **global cube antipode** of the corresponding lower-facet physical edge of \(R\) (after projecting the \(Q_S\)-antipodal reversal); its actual \(c\)-color is therefore the complement of the original lower color \(d_i\oplus t_i=1\oplus t_i\), namely \(t_i\). The intervening \(D\)-edges have arbitrary colors, which do not affect the required prescription. Thus \(P_{n,S}\) holds. \(\square\)

## Proof of the reverse implication

Assume \(P_{n,S}\). Let \(d\) be **any** arbitrary binary coloring of the undirected edges of \(Q_k\). Pick a distinguished exterior direction \(s\in D=[n]\setminus S\). Define a physical edge coloring \(c\) of \(Q_n\) using \(d\), with \(u\in Q_S\), \(z\in Q_D\), and one distinguished original coordinate \(i_0\in S\):

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
The main \(S\)-edge colors are physical because \(d_i\) is invariant under flipping its free \(i\)-bit; the exterior \(j\)-edge color in (5) is independent of its free \(j\)-bit. Antipodality of the *full* \(Q_n\) interchanges the two \(s\)-facets and complements the main colors in (4). It also complements \(u_{i_0}\), verifying \(c_j(\bar u,\bar z)=1\oplus c_j(u,z)\) for each \(j\in D\). Thus \(c\) is a legitimate antipodally odd physical-edge coloring of \(Q_n\). The colors in (4) depend on exterior coordinates **only through \(z_s\)**.

By \(P_{n,S}\), choose a full antipodal cube geodesic whose edge color is 0 in every direction of \(S\). Reverse its traversal if needed so that the unique \(s\)-step crosses from \(z_s=0\) to \(z_s=1\). Let \(U\) be its ordered \(S\)-direction list before the \(s\)-step, and \(V\) its ordered \(S\)-direction list after the \(s\)-step. Ignore moves in the other exterior directions. The projected \(S\)-word is \(U,V\), a permutation of all \(k\) directions. It begins at some \(u_0\), reaches some \(u_a\) after \(U\), and ends at \(\bar u_0\) after \(V\).

On the \(U\) edges, (4) says precisely \(d\)-color 0. On the \(V\) edges, (4) says precisely that the **\(Q_S\)-antipodal image of the projected \(V\)-suffix** carries \(d\)-color 1. Therefore the projected \(Q_S\) path obtained by reversing \(U\), and then following the reverse \(Q_S\)-antipodal image of \(V\),
\[
u_a\xrightarrow{U^{\mathrm{rev}}}u_0
\xrightarrow{\overline{V}^{\,\mathrm{rev}}}\bar u_a,
\tag{6}
\]
uses every \(S\) direction exactly once and changes \(d\)-color **at most once**: the first block has color 0 and the second block color 1. (When one block is empty, it is monochromatic.) This is a genuine full antipodal \(Q_k\)-geodesic. It proves \(B_k\). \(\square\)

**Additional switch-count transfer.** The forward proof works without assuming the \(d\)-geodesic has only one change. Given an arbitrary \(d\)-antipodal geodesic with \(r\ge1\) switches, choose the \(U|V\) split at **any one of its color changes**. Reversing the first block preserves its internal switch count; antipodally reversing and complementing the second block preserves its internal switch count; the chosen seam changes from a switch to a match. Hence the selected-direction color word on the resulting \(Q_n\) full geodesic, compared with any prescribed directionwise target \(t\), has exactly **\(r-1\)** switches. For \(r=0\), place all \(S\)-directions on one side of the exterior bridge; the selected word remains constant. Thus any upper bound on switches in arbitrary \(k\)-cube colorings transfers to a one-smaller bound for the **selected** direction word of every larger NORI1 coloring (not to the full \(n\)-edge color word, whose exterior bridge colors are uncontrolled).

## Consequence: universal seven-direction color prescription

**Corollary 2 (all \(n\): every seven selected colors are realizable).** For every dimension \(n\ge8\), every legal antipodally odd physical-edge coloring of \(Q_n\), every set \(S\subseteq[n]\) of size \(k\le7\), and every prescribed color vector \(t\in\mathbb F_2^S\), there exists a genuine **full \(n\)-edge antipodal geodesic** whose \(k\) selected edges have **exactly** the specified colors.

**Proof.** The geodesic Norine conjecture \(A_m\) has been established for **every \(m\le8\)**, including the SAT-certified case \(m=8\) in Kirchweger–Peitl–Subercaseaux–Szeider (2025), *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT*, arXiv:2511.08386, Theorem 1 (the paper explicitly states the *geodesic* conjecture in dimension eight). Leader and Long (2014), *Long geodesics in subgraphs of the cube*, Proposition 3.6 in arXiv:1301.2195v1, proved \(A_{k+1}\Rightarrow B_k\). Thus \(B_k\) holds for \(k\le7\). Theorem 1 above then gives \(P_{n,S}\) for every \(n>k\), as required. \(\square\)

For \(n\le8\), the stronger statement that **all \(n\) prescribed direction colors** can be realized also follows directly from the established full-geodesic result \(A_n\): independently XOR the desired \(t_i\) into each direction's edge color, preserving physicality and oddness, then use \(A_n\). Consequently, for **every** \(n\ge2\), arbitrary prescribed colors on any set of size \(\min(n,7)\) are simultaneously attainable, and in dimensions at most eight all \(n\) colors are attainable.

**Boundary of the result.** This uses a previously proved finite-dimensional geodesic theorem and an exact new dimension-free bridge implication. It is not a proof of the full NORI1 conjecture in arbitrary dimension; for eight selected directions in \(n\ge9\), the bridge equivalence reduces the question **exactly** to \(B_8\), equivalently to the known Leader–Long dimensional challenge \(A_9\Rightarrow B_8\) in one direction. The argument makes no claim about *ordinary boundary 3-tournaments*: it uses an edge (one-window) color seam, whereas ordered-three-face paths acquire two extra seam windows.

**Primary sources and scope checks.**
- Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33; https://arxiv.org/abs/1301.2195 .
- Markus Kirchweger, Tomáš Peitl, Bernardo Subercaseaux, Stefan Szeider, *From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT* (2025), arXiv:2511.08386, specifically Theorem 1 and the separate SAT geodesic encoding \(\Psi_n\); https://arxiv.org/html/2511.08386 .
- Tomáš Feder and Carlos Subi, *On hypercube labellings and antipodal monochromatic paths*, Discrete Applied Mathematics 161 (2013), 1421–1426 (original unrestricted-edge one-switch *path* conjecture; the geodesic strengthening is due to Leader–Long).
