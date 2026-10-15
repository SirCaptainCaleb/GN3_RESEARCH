## Freudenthal Carriers and Equivariant Topology

### Color-position carriers and a high-rank oscillation obstruction

This subsection strengthens the two-end localization of the dimension-simple second-switch method. The labels need not share a terminal **edge**, or even an endpoint color. A color fixed in any path position beyond the second gives a hemispherical carrier. The resulting equivariant extension leaves only parabolic cells with strong color variation across nearly every word position.

Throughout let \(n\ge5\), let \(c:E(Q_n)\to\mathbb F_2\) satisfy antipodal oddness, and provisionally suppose every full antipodal geodesic has at least two switches. The dual type-\(B_n\) Coxeter complex \(X\cong S^{n-1}\) has vertices \(P(x,\pi)\); the signed second-switch labeling is
\[
L(P)=(-1)^{w_1(P)}e_{s_2(P)}
\in \partial\mathcal O\cong S^{n-3},
\qquad
\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}.
\tag{1}
\]
As established earlier, this map is antipodally odd and maps adjacent dual vertices to nonopposite target vertices.

#### Anchoring any later word position

**Lemma 1 (fixed-position hemisphere).** Fix \(r\in\{3,\ldots,n\}\) and a family \(\mathcal P\) of complete geodesics whose \(r\)-th edge-color bit is the same \(b\). Then
\[
L(\mathcal P)\subseteq
H_{r,b}:=\partial\mathcal O\cap
\{z:(-1)^b z_{r-1}\ge0\}.
\tag{2}
\]
For any family whose first color is constant \(a\), all labels lie in the target simplex
\[
\Delta_a:=\operatorname{conv}\{(-1)^a e_2,\ldots,(-1)^a e_{n-1}\}.
\tag{3}
\]

*Proof.* If \(s_2(P)=r-1\), the first \(r-1\) comparisons in the word contain two switches, so \(w_1(P)=w_r(P)=b\). Hence a label on the \(e_{r-1}\)-axis has the prescribed sign. Every other label has zero component on that axis. The second assertion follows directly from (1). \(\square\)

**Theorem 2 (equivariant anchored-color carrier).** Let \(X_{\mathrm{anc}}\) be the union of all closed dual Coxeter cells \(D\) for which at least one of the bit positions
\[
\mathcal I=\{1,3,4,\ldots,n\}
\tag{4}
\]
is constant over the complete geodesics represented by the vertices of \(D\). Then \(X_{\mathrm{anc}}\) is an antipodally invariant subcomplex containing the entire dual 1-skeleton. The signed second-switch labeling extends to an equivariant continuous map
\[
F_{\mathrm{anc}}:X_{\mathrm{anc}}\longrightarrow S^{n-3}
\tag{5}
\]
via nested contractible target carriers. It also induces an equivariant augmentation-preserving chain map on the corresponding source chains.

*Proof.* Constancy of a word position is inherited by every face of a dual cell; antipodality complements its bit but preserves constancy. Thus \(X_{\mathrm{anc}}\) is an antipodally invariant subcomplex.

For each \(D\subseteq X_{\mathrm{anc}}\), let \(A_D\subseteq\mathcal I\) be its set of constant positions, with values \(b_r(D)\). Define
\[
C_D=
\begin{cases}
\displaystyle \Delta_{b_1(D)}
\cap\bigcap_{r\in A_D\setminus\{1\}}H_{r,b_r(D)},&1\in A_D,\\[2mm]
\displaystyle\bigcap_{r\in A_D}H_{r,b_r(D)},&1\notin A_D.
\end{cases}
\tag{6}
\]
By Lemma 1, every label of a chamber of \(D\) belongs to \(C_D\), so each carrier is nonempty. If the first bit is fixed, the intersection in (6) is a nonempty face of the simplex \(\Delta_{b_1(D)}\) and hence contractible. Otherwise the intersection contains at least one signed hemispherical constraint. Its intersection with the sphere is also contractible: let
\[
v=\sum_{r\in A_D}(-1)^{b_r(D)}e_{r-1}\ne0.
\]
For any \(z\in C_D\), one has \(z\cdot v\ge0\), so normalized linear interpolation from \(z\) to \(v\) never meets the origin and contracts \(C_D\).

If \(D'\) is a face of \(D\), every constant position of \(D\) remains constant with the same bit on \(D'\); additional restrictions only shrink the carrier. Thus \(C_{D'}\subseteq C_D\). Antipodality sends all fixed bits to their complements and each carrier to its negative. On dual edges, the known nonopposition theorem supplies the short target crosspolytope edge, and this edge lies inside the chosen carrier (the carriers are spherical intersections of closed convex cones). Inductively extend higher cell boundary maps inside their contractible carriers, selecting a member of each free antipodal cell pair before defining the opposite filling by antipodality. This produces (5) and the associated equivariant chain map. \(\square\)

#### Consequences for top-dimensional obstruction cells

**Corollary 3 (every surviving primary cell varies at almost every position).** There is an equivariant extension of the second-switch labeling over
\[
X_{\mathrm{anc}}\cup X^{(n-3)}.
\]
Under the hypothetical absence of a monochromatic antipodal geodesic, at least one dual \((n-2)\)-cell outside \(X_{\mathrm{anc}}\) has nonzero attaching-map degree into \(S^{n-3}\). In particular that cell satisfies:

* its parabolic generator set \(J\) contains \(s_1\) and at least one of \(s_0,s_{n-1}\);
* for **every** position \(r\in\{1,3,\ldots,n\}\), two chamber geodesics in that same cell have different colors in position \(r\).

*Proof.* Fill the anchored cells by Theorem 2. Fill any remaining cells of dimension at most \(n-3\) equivariantly, since \(S^{n-3}\) is \((n-4)\)-connected. If every remaining \((n-2)\)-cell boundary had zero degree, the map would extend equivariantly over \(X^{(n-2)}\). This contradicts the nonzero \((n-2)\)-nd power of the first Stiefel-Whitney class of the double covering \(S^{n-1}\to\mathbb RP^{n-1}\); no equivariant map of that skeleton to \(S^{n-3}\) exists. Thus at least one cell not in \(X_{\mathrm{anc}}\) carries an obstruction. Its lack of constant positions yields the stated simultaneous variability. The parabolic condition follows from the previous two-end localization, since every cell avoiding \(s_1\), or avoiding both \(s_0,s_{n-1}\), already has a first or last fixed edge. \(\square\)

**Theorem 4 (mixed-star localization on root-fixed cells).** Let \(D=gW_J\) be a dual \((n-2)\)-cell with \(s_0\notin J\). If \(D\notin X_{\mathrm{anc}}\), then \(J\) omits precisely \(s_0,s_k\) for some \(2\le k\le n-2\). All its geodesics have a common starting cube vertex \(x\), and their dimension orders consist of permutations of a fixed \(k\)-element initial block \(A\), followed by permutations of its complementary block \(B\). Writing
\[
a_i(x)=c(\{x,x\oplus e_i\}),
\]
both sets
\[
\{a_i(x):i\in A\},\qquad
\{a_i(x):i\in B\}
\]
contain both binary colors. In particular there are at least two red and two blue edges incident to \(x\).

*Proof.* A rank-\((n-2)\) parabolic cell omits two of the \(n\) simple generators. With \(s_0\) missing, the remaining missing generator is \(s_k\). Values \(k=1\) and \(k=n-1\) respectively fix the first and last edge and would put \(D\) in \(X_{\mathrm{anc}}\); hence \(2\le k\le n-2\). The subgroup generated by all swaps except \(s_k\) permutes the first and last dimension blocks independently; \(s_0\) is absent, so the root \(x\) is fixed.

For any full geodesic beginning at \(x\), the first bit equals \(a_{\pi_1}(x)\). Its final edge is antipodal to the edge in direction \(\pi_n\) incident to \(x\), so
\[
w_n(P(x,\pi))=1-a_{\pi_n}(x).
\tag{7}
\]
The first and last dimensions range freely over \(A\) and \(B\), respectively. If either block were monochromatic in the star at \(x\), the first or last word bit would be constant throughout \(D\), contradicting \(D\notin X_{\mathrm{anc}}\). As \(A,B\) are disjoint, the final assertion follows. \(\square\)

**Interpretation.** The unrestricted problem is reduced further to cells with strong simultaneous color variability. A root-fixed primary obstruction must involve two disjoint blocks of dimensions, each with both colors at the same cube root. The remaining cells containing the root-flip generator \(s_0\) require a different analysis: the initial root itself varies, so formula (7) no longer supplies a fixed star vector. These are the most promising location for a support-preserving analogue of Wu–Yang's degenerate-face cancellation. No new coloring restrictions, finite-order reductions, or restricted-family hypotheses are used.

### Antipodal separation of local edge data and the global degree obstruction

Let \(n\ge5\), \(X\cong S^{n-1}\) be the dual type-\(B_n\) Coxeter cell complex, and write \(s_0,\ldots,s_{n-1}\) for its simple chamber changes. For a dual cell \(D=gW_J\), let \(E(D)\) be the set of undirected cube edges traversed by all rooted full antipodal geodesics corresponding to its chamber vertices. Write \(\bar E(D)=\{\bar e:e\in E(D)\}\).

#### Primary-cell separation

**Theorem 1 (no antipodal edge pairs inside a primary cell).** For every dual Coxeter cell \(D=gW_J\) of dimension \(n-2\),
\[
E(D)\cap\bar E(D)=\varnothing.
\tag{1}
\]
Consequently any function \(h:E(D)\to\mathbb F_2\) extends to an antipodally odd coloring of all undirected cube edges. Thus antipodal oddness itself imposes no constraints within the family of complete geodesics carried by an individual primary obstruction cell; their only intra-cell constraints are shared-edge identifications.

*Proof.* There are \(n\) simple generators, so \(J\) omits two generators. We distinguish whether \(s_0\) is omitted.

If \(0\notin J\), the initial cube vertex \(x\) is fixed. The other omitted generator is some \(s_k\), \(1\le k\le n-1\). Every order is a concatenation of two nonempty dimension blocks \(A,B\), with \(A\) preceding \(B\) in every order and the entries within each block permuted independently. On every edge traversed in a dimension of \(A\), the bits in all dimensions of \(B\) still equal their starting values at \(x\). On every edge in a dimension of \(B\), the bits in all dimensions of \(A\) have already been flipped and therefore equal the complementary starting values at \(x\). Since antipodal edges have the same dimension but opposite bits in *all other* dimensions, neither an \(A\)-edge nor a \(B\)-edge can have its antipodal mate in \(E(D)\).

If \(0\in J\), the two omitted generators are \(s_a,s_b\), with \(1\le a<b\le n-1\). The dimension order is partitioned into three nonempty consecutive blocks \(A,B,C\), with these blocks occupying positions \(1,\ldots,a\), \(a+1,\ldots,b\), and \(b+1,\ldots,n\). The parabolic group permits arbitrary permutation and initial-root sign changes on dimensions of \(A\), but the initial bits in \(B\cup C\) remain fixed throughout the cell. On an edge in \(A\), all \(B\)-bits remain at their common initial values; on an edge in \(B\), all \(C\)-bits remain at their common initial values; on an edge in \(C\), all \(B\)-bits have their common complemented initial values. Because the comparison block used in each case is nonempty and disjoint from the direction of the edge, the antipodal mate of that edge cannot occur elsewhere within \(E(D)\). This proves (1).

Given \(h\) on \(E(D)\), color the antipodal mates \(\bar e\) with \(1-h(e)\), and choose complementary values independently on every remaining antipodal edge orbit. Equation (1) makes the extension well defined. \(\square\)

**Interpretation.** The result holds for both the root-fixed and root-changing primary cells, including the mixed-star cells remaining after the all-position color-anchor theorem. It does not say that arbitrary assignments are compatible with the *global no-monochromatic-geodesic hypothesis*: the extension can create monochromatic full geodesics in other cells. In particular, any final cancellation proof must exploit relations across different parabolic cells or global consequences of that hypothesis. Applying antipodal oddness within a single primary cell cannot supply a missing local parity equation.

#### An odd global obstruction parity

Retain the hypothetical assumption that *no* monochromatic antipodal geodesic exists. Then the signed second-switch label on complete geodesic chambers is defined, odd, and nonopposite on adjacent chambers. The color-anchor construction extends it equivariantly over the subcomplex \(X_{\mathrm{anc}}\) of cells with a common first color or a common later-position color, and over the entire \((n-3)\)-skeleton. Denote such an extension by \(F\), with target \(S^{n-3}\). Write \(\bar X=X/(\pm1)\cong\mathbb RP^{n-1}\).

For a dual \((n-2)\)-cell \(D\), define its mod-two attaching degree
\[
o_F(D)=\deg_2\bigl(F|_{\partial D}:\partial D\cong S^{n-3}\to S^{n-3}\bigr)\in\mathbb F_2.
\tag{2}
\]
It is well defined on an antipodal cell orbit, as orientation does not affect degree modulo two. On an anchored cell, \(F\) already extends over \(D\), so \(o_F(D)=0\).

**Theorem 2 (global obstruction parity).** Let
\[
Z=\sum_{[D]}\epsilon_D[D]
\]
be any cellular \((n-2)\)-cycle representing the nonzero class of
\[
H_{n-2}(\bar X;\mathbb F_2)\cong\mathbb F_2.
\]
Then
\[
\boxed{
\sum_{\substack{[D]\ {\rm unanchored}\\\dim D=n-2}}
\epsilon_D\,o_F(D)=1\pmod2.
}
\tag{3}
\]
Thus the obstruction is not merely supported on some exceptional cells: its **total contribution over an appropriate projective homology cycle is odd**.

*Proof.* The primary obstruction to extending an equivariant map from the \((n-3)\)-skeleton of the antipodal sphere \(S^{n-1}\) into \(S^{n-3}\) reduces modulo two to
\[
w_1^{n-2}\in H^{n-2}(\mathbb RP^{n-1};\mathbb F_2),
\tag{4}
\]
where \(w_1\) is the first Stiefel–Whitney class of the antipodal double covering. It is the nonzero generator in degree \(n-2\), since the cohomology ring is \(\mathbb F_2[w_1]/(w_1^n)\). The cellular cocycle representing this primary obstruction assigns to each \((n-2)\)-cell the attaching-map degree (2). Evaluation on the nonzero homology class \([Z]\) is therefore one. Anchored cells contribute zero, yielding (3). \(\square\)

#### A precise Wu–Yang-type proof obligation

Equation (3) supplies a quantitative chain target. To contradict the hypothetical absence of a monochromatic full geodesic, it suffices to construct a color-sensitive pairing or mod-two boundary identity showing that the total number of degree-contributing exceptional cells in a projective generator \(Z\), counted with their coefficients, is even. Such a pairing must involve **more than one primary cell**: Theorem 1 shows that the antipodal edge-color relation is invisible within each cell on its own.

One possible chain-level route is to choose compatible subdivisions and evaluate each degree by counting preimages of the interior of a fixed top-dimensional crosspolytope facet. The needed argument would pair those preimages globally through shared-edge and full-rank dimension-exchange relations, analogous to Wu–Yang's dependent-radial cancellation. No such global pairing is established here; (3) is a necessary topological obstruction, not a proof of NORI1.

### Rooted Boolean reachability restores transitivity without repeated dimensions

Wu–Yang's successful antipodal-path argument (arXiv:2607.19276) uses ordinary monochromatic connected-component labels. Those labels forget dimension support. Unrooted monochromatic shortest-path reachability is not transitive, as shown by the earlier \(Q_3\) example in this Article. However, rooting the Boolean lattice and insisting that every step increase Hamming distance from the root restores transitivity and retains every dimension-simplicity constraint.

Let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1-c(e)\), with red \(0\) and blue \(1\). Fix a cube vertex \(x\), and identify each vertex with its flip set \(S\subseteq[n]\), meaning the vertex is \(x\oplus\mathbf1_S\).

For \(a\in\{0,1\}\), define a relation \(S\preceq_x^a T\) when \(S\subseteq T\) and there exists a color-\(a\) path from \(x\oplus\mathbf1_S\) to \(x\oplus\mathbf1_T\) that traverses only the dimensions in \(T\setminus S\), each once. Permit the length-zero path when \(S=T\).

**Theorem 1 (rooted geodesic orders and antipodal duality).** For each \(a\), the relation \(\preceq_x^a\) is a partial order on \(2^{[n]}\). It obeys
\[
\boxed{
S\preceq_x^0 T\quad\Longleftrightarrow\quad
T^c\preceq_x^1 S^c.
}
\tag{1}
\]
Thus Boolean complementation gives an order-reversing isomorphism between the rooted red and blue reachability posets. Every chain of comparable elements can be realized by concatenating monochromatic paths with disjoint dimension supports.

*Proof.* Reflexivity is allowed by zero-length paths; antisymmetry follows from subset containment. If \(S\preceq_x^a T\preceq_x^a U\), the two path segments respectively use only \(T\setminus S\) and \(U\setminus T\). These dimension sets are disjoint; concatenating yields a color-\(a\) geodesic from the vertex for \(S\) to the vertex for \(U\), proving transitivity and the rank-simplicity assertion.

For (1), apply the cube antipode to a red geodesic from \(x\oplus\mathbf1_S\) to \(x\oplus\mathbf1_T\). It becomes a blue geodesic from the vertex for \(S^c\) to the vertex for \(T^c\). Reverse the path, obtaining a blue geodesic from the vertex for \(T^c\) to the vertex for \(S^c\), using precisely \(T\setminus S=S^c\setminus T^c\). The converse follows by the same operation. \(\square\)

Put
\[
\mathcal R_x=\{S\subseteq[n]:\varnothing\preceq_x^0 S\},
\tag{2}
\]
the flip sets of vertices reachable by a red geodesic beginning at \(x\). This family is accessible: any nonempty member has a one-dimension deletion also in \(\mathcal R_x\), by removing the last step of a witnessing path. It need not be downward closed under arbitrary subset deletion.

**Theorem 2 (complementary reachability is equivalent to a one-switch geodesic).** For each fixed root \(x\), the following statements are equivalent:

(i) There exists a full antipodal geodesic beginning at \(x\) whose word is red followed by blue, with either monochromatic segment allowed to be empty.

(ii) The family \(\mathcal R_x\) contains two complementary subsets:
\[
\boxed{\mathcal R_x\cap\{S^c:S\in\mathcal R_x\}\ne\varnothing.}
\tag{3}
\]

*Proof.* A red-then-blue geodesic has a unique intermediate vertex \(x\oplus\mathbf1_S\) at its color boundary, with \(\varnothing\preceq_x^0 S\) and \(S\preceq_x^1[n]\). By (1), the latter relation is equivalent to \(\varnothing\preceq_x^0 S^c\). This proves (i) implies (ii). Conversely, if \(S,S^c\in\mathcal R_x\), take a red geodesic from \(x\) to the vertex for \(S\), and use (1) to obtain a blue geodesic from that vertex to \(\bar x\). Their support sets are respectively \(S\) and \(S^c\), so concatenation traverses all \(n\) dimensions once and changes color at most once. \(\square\)

**Corollary 3 (a complement-free reachability formulation of NORI1).** An antipodally odd cube-edge coloring has a monochromatic full antipodal geodesic from some root if and only if \(\mathcal R_x\) contains a complementary pair of subsets for some root \(x\).

*Proof.* If a complementary pair exists, Theorem 2 gives a one-switch full geodesic, and root-slide rotation at the change produces a monochromatic full geodesic. Conversely, a red monochromatic full geodesic beginning at \(x\) makes both \(\varnothing\) and \([n]\) members of \(\mathcal R_x\). If only a blue monochromatic full geodesic is initially given, reverse its antipodal translate to obtain a red monochromatic full geodesic beginning at the same root. \(\square\)

Under a hypothetical NORI1 counterexample, each \(\mathcal R_x\) is therefore complement-free and has size at most \(2^{n-1}\). This bound is a consequence of the stronger complement-free property, not a proposed route through average-size estimates.

**Proposition 4 (root-change inclusions).** If the cube edge \(\{x,x^i\}\) is red, where \(x^i=x\oplus e_i\), then for every \(S\subseteq[n]\setminus\{i\}\),
\[
S\in\mathcal R_x\quad\Longrightarrow\quad S\cup\{i\}\in\mathcal R_{x^i},
\]
\[
S\in\mathcal R_{x^i}\quad\Longrightarrow\quad S\cup\{i\}\in\mathcal R_x.
\tag{4}
\]
If the given edge is blue, the corresponding implications hold for the red families at the antipodal vertices \(\bar x,\overline{x^i}\).

*Proof.* A red path from \(x\) to the vertex for \(S\) avoids dimension \(i\). Prepend the red edge \(x^i\to x\); the result is a red geodesic from \(x^i\) using dimensions \(S\cup\{i\}\). This proves the first implication. Exchange the roots to prove the second. If the original edge is blue, its antipodal mate is red. \(\square\)

**Implication for Wu–Yang's chain map.** The replacement for ordinary red components need not be another equivalence relation. The rooted red reachability **orders** have associative dimension-simple path concatenation; the red and blue orders are antipodally dual by (1); and across each cube edge one of the paired red reachability families obeys the rank-preserving transport law (4). These are intrinsic local incidences of the unrestricted cube coloring, without any arbitrary choice of path galleries.

The outstanding theorem is to construct from the family \((\preceq_x^0,\preceq_x^1)_x\) an equivariant augmentation-preserving chain map to a target of sufficiently small dimension, or to derive the complementary-pair conclusion through a topological intersection principle. Ordinary rook labels use equality of component indices; the relations (4) provide support-preserving inclusions instead. No full chain map is established here.

### Complementary monochromatic path pairs as common full-rank certificates

The two original one-switch conjectures can be characterized by the existence of **two monochromatic partial paths of the same color** that have complementary dimension or vertex supports. Applying the involutive color reversal to the second path and gluing their compatible boundaries produces a complete one-switch path. This provides a common intrinsic proof certificate inspired by the ordered-pair step of Wu–Yang's construction, without introducing an auxiliary graph of galleries or relaxing dimension-simplicity.

#### NORI1: two red geodesic cones with antipodal ends

Fix an antipodally odd edge coloring of \(Q_n\), a root \(x\), and a bit \(a\in\mathbb F_2\). Let
\[
R_x^a=\{y\in Q_n:\text{some color-}a\text{ geodesic from }x\text{ ends at }y\}.
\tag{1}
\]

**Theorem 1 (opposed endpoints).** The following are equivalent for a fixed root \(x\) and color \(a\):

(i) Some full antipodal geodesic from \(x\) has color word consisting of an initial run of \(a\) followed by a terminal run of \(1-a\), with either run possibly empty.

(ii) The rooted monochromatic reachability cone \(R_x^a\) contains an antipodal pair:
\[
\boxed{\exists y:\quad y,\bar y\in R_x^a.}
\tag{2}
\]

*Proof.* If (ii) holds, take color-\(a\) geodesics \(P:x\to y\) and \(Q:x\to\bar y\). Their dimension supports are respectively \(S=\{i:x_i\ne y_i\}\) and \(S^c\). Apply cube antipodality to \(Q\), producing a color-\((1-a)\) geodesic \(\bar Q:\bar x\to y\); reverse it to get a color-\((1-a)\) path \(y\to\bar x\). The concatenation \(P\cdot(\bar Q)^{\rm rev}\) is a full dimension-simple antipodal geodesic from \(x\), with at most one switch, proving (i).

Conversely, split a geodesic as in (i) at its color boundary \(y\). Its first part is a color-\(a\) geodesic from \(x\) to \(y\). Antipodally translate and reverse the color-\((1-a)\) suffix from \(y\) to \(\bar x\), giving a color-\(a\) geodesic from \(x\) to \(\bar y\). Thus both endpoints belong to \(R_x^a\). \(\square\)

In particular, NORI1 is equivalent to the statement that for some root \(x\) and either color \(a\), the corresponding geodesic reachability cone contains an antipodal pair. Under a hypothetical counterexample, every cone \(R_x^a\) is antipodal-free. The paths in this theorem use disjoint dimension supports, hence the union of their move vectors has full rank \(n\).

#### Boundary tournaments: two same-color paths ending in reversed ordered pairs

Let \(V\) be an \(n\)-element set and \(b(a,h,c)\in\mathbb F_2\) an arbitrary reversal-odd boundary 3-tournament. For an ordered pair \((h,c)\) and color \(a\), define
\[
\mathcal F_{h,c}^a=
\bigl\{\,S\subseteq V\setminus\{h,c\}:\ 
\exists\text{ a vertex-simple color-}a\text{ tight path}
\text{ using }S\cup\{h,c\}
\text{ and ending }(h,c)\,\bigr\}.
\tag{3}
\]
Allow the length-two ordered path \((h,c)\), with no triple colors, so that \(\varnothing\in\mathcal F_{h,c}^a\) for both bits.

**Theorem 2 (opposed-terminal-pair gluing).** The boundary tournament admits a Hamilton tight path whose color word switches at most once if and only if there exist distinct \(h,c\in V\), a color \(a\), and a subset \(S\subseteq V\setminus\{h,c\}\) such that
\[
\boxed{
S\in\mathcal F_{h,c}^a,\qquad
\bigl(V\setminus\{h,c\}\bigr)\setminus S
\in\mathcal F_{c,h}^a.
}
\tag{4}
\]

*Proof.* Suppose (4) holds, witnessed by color-\(a\) tight paths
\[
P=(p_1,\ldots,p_r,h,c),\qquad
Q=(q_1,\ldots,q_s,c,h).
\]
The used vertex sets meet only in \(\{h,c\}\) and together equal \(V\). Reverse \(Q\): by boundary reversal oddness it becomes a color-\((1-a)\) tight path \((h,c,q_s,\ldots,q_1)\). Glue this reversed path to \(P\) along their common ordered terminal/initial pair \((h,c)\):
\[
(p_1,\ldots,p_r,h,c,q_s,\ldots,q_1).
\tag{5}
\]
All vertices are distinct, all are used, and the tight-path color word is an initial run of \(a\) followed by a terminal run of \(1-a\). Either run may be empty. Hence (5) is a one-switch Hamilton path.

Conversely, let a Hamilton ordering have a bit word with at most one switch, and let \(a\) be the initial bit (if the whole word is constant, take that bit). Split it at the switch, with \(P\) the initial color-\(a\) tight path up to the shared boundary pair \((h,c)\). Reverse the remaining color-\((1-a)\) tight suffix, including that same boundary pair. Reversal oddness makes the reversed suffix a color-\(a\) tight path ending in \((c,h)\). The used vertex sets intersect at \(\{h,c\}\) and are complementary elsewhere. This gives (4). \(\square\)

The undirected edges of \(P\) and \(Q\) in (4), with their common \(\{h,c\}\) edge identified, form a spanning tree of \(K_V\). Their type-\(A\) incidence vectors therefore have full graphic-matroid rank \(n-1\). Thus (4) enforces Hamilton vertex-simplicity and cannot be satisfied by a walk that repeats an original vertex.

#### A common rank-preserving gluing principle

Theorems 1 and 2 expose the same selection mechanism:

1. Find two *same-color monochromatic partial paths* with a pair of opposed interfaces.
2. Require their dimension or vertex supports to complement one another in the natural independence geometry.
3. Apply the original reversal/antipodal operation to one path, making its color complementary.
4. Concatenate along the compatible interface. Independence of supports guarantees a full dimension-simple output with at most one color change.

The cube interface consists of a common initial root and antipodal terminal vertices. The boundary interface consists of opposite terminal ordered pairs \((h,c),(c,h)\), with the shared two vertices counted once. The distinct appearances of the interfaces should not be erased by imposing an unjustified extra state-graph axiom.

**Topological proof target.** Wu–Yang's rook-label map records paired red components and uses the involution to obtain an odd map into a type-\(A\) root sphere. Here the relevant paired objects are the rank-sensitive reachable families \(R_x^a\) and \(\mathcal F_{h,c}^a,\mathcal F_{c,h}^a\). A successful extension would prove, by an equivariant chain obstruction, that *some pair has complementary supports*. That would imply the original one-switch conclusions by the above equivalences. The existence of the complementary pair remains unproved in both unrestricted classes; the theorems in this subsection establish the common full-rank decoding certificate, not its topological existence.

### Monochromatic Freudenthal prefix complexes and rank-preserving rook transport

Wu and Yang reduce the ordinary monochromatic antipodal **path** theorem to an ordered pair of connected-component indices. Equality of indices along monochromatic edges supplies the rook property but forgets the dimensions traversed by a connecting walk. This subsection constructs a replacement with contractible *simplicial carriers*, built from monochromatic geodesic prefixes. It retains full dimension-simplicity, has the same color-selective adjacency as Wu–Yang's component pairs, and expresses the desired antipodal path as an intersection of opposite carriers.

Fix an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\), with color \(0\) called red. For each root \(x\in Q_n\), identify a vertex \(x\oplus\mathbf1_S\) with \(S\subseteq[n]\). The **rooted Freudenthal triangulation** \(\mathcal T_x\) of the geometric \(n\)-cube has simplices on chains
\[
S_0\subsetneq S_1\subsetneq\cdots\subsetneq S_r
\quad\text{in }2^{[n]}.
\tag{1}
\]
Geometric central inversion preserves \(\mathcal T_x\), and \(\mathcal T_{\bar x}=\mathcal T_x\). For a color \(a\in\mathbb F_2\), let \(\mathcal K_x^a\) be the subcomplex generated by all saturated chains
\[
\varnothing=S_0\subset S_1\subset\cdots\subset S_k,
\quad |S_j|=j,
\tag{2}
\]
whose corresponding cube edges all have color \(a\), for every possible length \(k\le n\). Include all simplicial faces of these chains.

**Theorem 1 (prefix-cone and full-rank theorem).** For every root \(x\) and color \(a\):

(i) \(\mathcal K_x^a\) is a nonempty contractible simplicial subcomplex of \(\mathcal T_x\), coned with apex \(x\).

(ii) Its vertices are precisely the vertices reachable from \(x\) by color-\(a\) geodesics. Its simplices are precisely the finite chains in the rooted color-\(a\) geodesic-reachability partial order on this vertex set.

(iii) Every simplex of \(\mathcal K_x^a\) has an intrinsic dimension-simple certificate. If its vertices in the \(x\)-subset labeling are \(S_0\subsetneq\cdots\subsetneq S_r\), the nonempty increments
\[
D_j=S_j\setminus S_{j-1},\qquad 1\le j\le r,
\]
are pairwise disjoint. Their indicator vectors \(\mathbf1_{D_j}\in\mathbb F_2^n\) are linearly independent. The simplex can be refined to a saturated monochromatic geodesic using every dimension in each \(D_j\) once.

*Proof.* Every generator (2) contains \(\varnothing\); adjoining \(\varnothing\) to a face of such a generator yields another face of that generator. This proves (i). Each saturated generator is a monochromatic geodesic prefix, and every reached vertex occurs as a generator endpoint, proving the vertex statement.

If \(S_0\prec_x^a\cdots\prec_x^a S_r\) are comparable red-reachability vertices, the paths between consecutive sets can be concatenated because their support differences are disjoint, and a red path from \(\varnothing\) to \(S_0\) can be prepended. A saturated refinement then contains all \(S_j\), so the chain is a simplex of \(\mathcal K_x^a\). The reverse implication follows by reading a generating monochromatic path between the listed vertices. This proves (ii). Strict nesting gives pairwise disjoint nonempty increments, which have independent indicator vectors, proving (iii). \(\square\)

**Theorem 2 (antipodal intersection criterion).** For each \(x\) and \(a\):
\[
\boxed{
\mathcal K_x^a\cap\mathcal K_{\bar x}^a\ne\varnothing
\iff
\text{a monochromatic color-}a\text{ full geodesic joins }x\text{ to }\bar x.
}
\tag{3}
\]
Moreover central inversion \(A\) satisfies
\[
A\mathcal K_x^a=\mathcal K_{\bar x}^{1-a},
\tag{4}
\]
and
\[
\boxed{
\mathcal K_x^a\cap A\mathcal K_x^a\ne\varnothing
\iff
\text{a full geodesic begins at }x
\text{ with an initial color-}a\text{ run followed by a color-}(1-a)\text{ run}.
}
\tag{5}
\]

*Proof.* Both carriers in (3) are subcomplexes of the common triangulation \(\mathcal T_x=\mathcal T_{\bar x}\). If they intersect geometrically, they share a simplex, hence a vertex \(y\). Thus monochromatic geodesics \(x\to y\) and \(\bar x\to y\) exist. Their dimension sets are complementary, because \(x,\bar x\) are antipodes. Concatenating the first with the reversal of the second gives a color-\(a\) full geodesic. Conversely its midpoint or any division vertex belongs to both carriers. Antipodal oddness sends every color-\(a\) path from \(x\) to a color-\((1-a)\) path from \(\bar x\), establishing (4). For (5), intersection yields color-\(a\) paths from \(x\) to \(y\) and color-\((1-a)\) from \(\bar x\) to \(y\); reversing the latter gives the complementary segment of a dimension-simple one-switch antipodal geodesic. Conversely split any such full geodesic at its change. \(\square\)

In particular, in a hypothetical NORI1 counterexample, \(\mathcal K_x^0\) and \(\mathcal K_{\bar x}^0\) are disjoint for every \(x\); so are \(\mathcal K_x^0\) and \(A\mathcal K_x^0\). The compact geometric carriers replace the distinct red-component **indices** in Wu–Yang's construction, without replacing rank-preserving reachability by ordinary connectivity.

#### Transport across neighboring roots

For an edge \(xy\) in dimension \(i\), put
\[
H_i(y)=\{z\in[0,1]^n:z_i=y_i\},
\]
the facet containing \(y\) but not \(x\).

**Theorem 3 (cone extension across a colored edge).** If \(xy\) has color \(a\), then
\[
\boxed{
x*\bigl(\mathcal K_y^a\cap H_i(y)\bigr)\ \subseteq\ \mathcal K_x^a.
}
\tag{6}
\]
The expression on the left is the simplicial cone formed by adjoining \(x\) to simplices of \(\mathcal K_y^a\) lying in that facet. It is precisely the subcomplex generated by monochromatic geodesic prefixes starting with \(x\to y\). There is a symmetric inclusion with \(x,y\) interchanged.

*Proof.* A geodesic beginning at \(y\) and ending in \(H_i(y)\) does not traverse dimension \(i\). The same is true of every prefix up to any vertex in this facet. Prepending the color-\(a\) edge \(x\to y\) therefore gives a color-\(a\) geodesic beginning at \(x\) whose dimension supports are disjoint across the join. Every simplex on the left is a face of such a red path simplex, giving (6). Conversely, a red geodesic prefix beginning with \(x\to y\) cannot traverse \(i\) again, so its remaining segment is a color-\(a\) geodesic from \(y\) entirely within \(H_i(y)\). Thus the generated subcomplexes agree. \(\square\)

**Corollary 4 (contractible carrier-valued rook relation).** Put
\[
Q(x)=\bigl(\mathcal K_x^0,\mathcal K_{\bar x}^0\bigr).
\tag{7}
\]
Then \(Q(\bar x)\) swaps the two entries. If \(xy\) is red, the first entries of \(Q(x),Q(y)\) intersect, and satisfy the stronger cone inclusions (6). If \(xy\) is blue, the second entries intersect, and satisfy the corresponding inclusions on the antipodal red edge \(\bar x\bar y\). In the absence of a monochromatic antipodal geodesic, the two entries of each \(Q(x)\) are disjoint contractible subcomplexes of a common Freudenthal triangulation.

This reproduces the color-selective rook incidence of Wu–Yang's reduction with **intersection and compatible coning in place of equality of component labels**. It is a theorem about all unrestricted antipodally odd edge colorings, not a proposed abstract gallery axiom.

#### One-missing-dimension obstruction

For a root \(x\), let
\[
\mathcal R_x=\{S\subseteq[n]:x\oplus\mathbf1_S
\text{ belongs to }\mathcal K_x^0\}.
\]

**Theorem 5 (near-complementary supports force closure).** If \(\mathcal R_x\) contains two disjoint sets \(S,T\) satisfying
\[
S\cap T=\varnothing,\qquad |S\cup T|=n-1,
\tag{8}
\]
then some monochromatic full antipodal geodesic exists, possibly from another root. Indeed, \(\mathcal R_x\) then contains an antipodal pair.

*Proof.* Let \([n]\setminus(S\cup T)=\{i\}\). The two cube edges
\[
\{x\oplus\mathbf1_S,\ x\oplus\mathbf1_{S\cup\{i\}}\},
\quad
\{x\oplus\mathbf1_T,\ x\oplus\mathbf1_{T\cup\{i\}}\}
\]
are antipodal, so one is red. In the first case the red geodesic from \(x\) to \(S\) extends to \(S\cup\{i\}=T^c\); together with the red geodesic to \(T\), this gives an antipodal pair in \(\mathcal R_x\). In the other case \(T\) extends to \(T\cup\{i\}=S^c\), again giving such a pair. Theorem 2 then supplies the required full geodesic after root-slide rotation. \(\square\)

Consequently, if no monochromatic full geodesic exists, each rooted red reachability family excludes not only complementary pairs but also disjoint pairs covering all but one dimension. This additional exclusion uses the local edge-color involution and does not follow from accessibility of the reachability family alone.

#### Why equality labels cannot retain the needed information

**Proposition 6 (no equality-based geodesic replacement).** Any point-valued labeling \(p:V(Q_n)\to A\) satisfying \(p(x)=p(y)\) on every red edge is constant on the ordinary red connected components. Moreover Wu and Yang's proven antipodal-path theorem guarantees that, for every antipodally odd coloring, some red connected component contains antipodal vertices. Hence a component-equality red labeling cannot provide distinct entries \(p(x),p(\bar x)\) at every root when only monochromatic **geodesics** are assumed absent.

*Proof.* Equality along each red edge propagates along arbitrary red walks. Wu and Yang prove that a monochromatic antipodal walk exists. If it is blue, its antipodal image is a red walk between the same two antipodal vertices. Thus some red component has an antipodal pair, forcing equality of its labels. \(\square\)

#### Remaining chain-level problem

The natural replacement for Wu–Yang's rooted pair \((p(x),p(\bar x))\) is the carrier pair \(Q(x)\) of (7). Each entry is a **contractible cone of full-rank monochromatic prefixes**. Their disjointness expresses the hypothetical counterexample; the involution swaps them; colored edges give the stronger cone transport (6). This removes the loss of dimension-simplicity in the component reduction.

What remains unproved is a **carrier-valued type-A root or chain construction**: one must assign compatible equivariant target chains to pairs of disjoint prefix complexes, in a target sphere of dimension below the source, such that face boundaries cancel under the inclusions (6). Arbitrary intersection of contractible carriers is not enough for Wu–Yang's rook-gallery rank lemma, and the number of distinct carriers need not be bounded by \(n\). The missing dimension bound and cancellation theorem are therefore substantive new obligations, not consequences of the present representation.

Alexander duality of two opposed disjoint contractible red prefix cones in the cube boundary yields the mod-two homology of S^(n-2) for the antipodal complement. Under the absence of red-then-blue full geodesics at a root, the two cones are disjoint and both lie in the boundary. A PL regular neighborhood of the image cone in projective space is a ball, so the antipodal quotient of the complement has the homotopy type of RP^(n-2). The missing result is compatibility between these root-dependent complements along colored cube edges; no global chain map is established.

**Theorem (equivariant dimension-drop).** Let \(n\ge3\) and \(K_x\) be the red geodesic-prefix Freudenthal complex rooted at \(x\). If no full geodesic from \(x\) has a red run followed by a blue run, permitting empty runs, then
\[
Y_x=\partial[0,1]^n\setminus(K_x\cup A K_x)
\]
is equivariantly homotopy equivalent to the antipodal sphere \(S^{n-2}\). Consequently
\[
H^*(Y_x/A;\mathbb F_2)=\mathbb F_2[u]/(u^{n-1}),
\]
where \(u\) is the first Stiefel–Whitney class of the restricted antipodal cover.

*Proof.* The earlier gluing theorem makes \(K_x\) and its antipodal image disjoint. Every red prefix has length at most \(n-1\), since one of length \(n\) would be a red full antipodal geodesic. Each simplex of \(K_x\) therefore lies in a proper cubical face. Thus both complexes lie in \(\partial[0,1]^n\cong S^{n-1}\) and are simplicial cones, hence collapsible. Alexander duality applied to their disjoint union gives
\[
\widetilde H_i(Y_x;\mathbb F_2)
=\widetilde H^{n-2-i}(K_x\sqcup AK_x;\mathbb F_2),
\]
which is \(\mathbb F_2\) when \(i=n-2\) and zero otherwise.

For the equivariant assertion put \(m=n-1\). Quotienting the boundary sphere by antipodality yields \(\mathbb RP^m\), and the image \(C\) of \(K_x\) is a PL embedded collapsible cone, since \(K_x\cap AK_x=\varnothing\). A small regular neighborhood \(N\) of \(C\) in \(\mathbb RP^m\) is a PL \(m\)-ball. Its punctured neighborhood deformation retracts to \(\partial N\), so
\(Y_x/A=\mathbb RP^m\setminus C\simeq\mathbb RP^m\setminus\operatorname{int}N\simeq\mathbb RP^{m-1}\).
The restricted antipodal covering class maps to the nonzero \(H^1\) generator. The homotopy equivalence of quotients therefore lifts, by double-cover classification, to an equivariant homotopy equivalence \(Y_x\simeq_{\mathbb Z_2}S^{m-1}\). \(\square\)

**Unproved step.** The target \(Y_x\) changes with \(x\). Independent equivariant sphere models do not form a global chain map. A root-change construction must use the contractible common bridges of monochromatic prefix complexes and supply coherent higher-dimensional fillings.

### Residual-face descent barriers from complementary monochromatic arms

This section combines the rooted geodesic-prefix complexes of Article XIV, Subsection 38, with the projective square-curvature theory of Subsection 28. It proves a local-to-global gluing criterion for **arbitrary residual dimension sets**, and, in codimension two, converts the hypothetical failure of NORI1 into an explicit constraint on every square accessible from complementary red geodesic arms. The conclusion is uniform in dimension and uses no restricted coloring family.

Let \(n\ge3\), \(D=[n]\), and let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\tau e)=1-c(e)\). Write \(\mathcal R_x=\{S\subseteq D:\text{some red geodesic from }x\text{ uses precisely }S\}\), as in Subsections 29 and 38. Suppose \(S,T\in\mathcal R_x\) are disjoint, and put
\[
M=D\setminus(S\cup T),\qquad y_S=x\oplus\mathbf1_S,\qquad y_T=x\oplus\mathbf1_T.
\tag{1}
\]
Let \(F_S\) be the cubical \(|M|\)-face based at \(y_S\) with free dimension set \(M\). Its antipodal mate is the parallel face \(F_T\): indeed
\(\tau y_S=y_T\oplus\mathbf1_M\).

**Theorem 1 (two-arm residual-face gluing).** For every ordering \(\sigma\) of the missing dimensions \(M\), let \(w_{F_S}(\sigma)\) be the color word of the monotone path from \(y_S\) to \(y_S\oplus\mathbf1_M\), traversing \(M\) in that order. Then there is a complete dimension-simple antipodal geodesic whose color word is
\[
\boxed{0^{|S|}\ w_{F_S}(\sigma)\ 1^{|T|}.}
\tag{2}
\]
Consequently, if any \(w_{F_S}(\sigma)\) is nondecreasing (belongs to \(0^*1^*\)), the coloring has a monochromatic full antipodal geodesic from some root.

*Proof.* Choose red monotone geodesics \(P_S:x\to y_S\) and \(P_T:x\to y_T\), using the disjoint dimension sets \(S,T\). Let \(R_\sigma\) traverse the missing face from \(y_S\) to \(y_S\oplus\mathbf1_M\). Antipodally translate \(P_T\) and reverse it; this is a blue geodesic starting at \(\tau y_T=y_S\oplus\mathbf1_M\) and ending at \(\tau x\), using precisely the dimensions of \(T\). Concatenating \(P_S,R_\sigma,(\tau P_T)^{\rm rev}\) gives (2), uses each of the three disjoint dimension sets precisely once, and ends at \(\tau x\). If \(w_{F_S}(\sigma)\) is nondecreasing, the full word has at most one switch. Rotating the starting point across its possible unique switch and using \(c(\tau e)=1-c(e)\) converts the path into a monochromatic full geodesic. \(\square\)

**Corollary 2 (uniform descent barrier in a hypothetical counterexample).** If a legal coloring has no monochromatic full antipodal geodesic, then for every root \(x\) and every pair of disjoint members \(S,T\in\mathcal R_x\), every monotone full path across the residual face \(F_S\) has a color descent \(1\to0\). Equivalently, no such path has a word in \(0^*1^*\). This includes the rank-\((n-1)\) impossibility of Subsection 38 when \(|M|=1\), since a one-edge word has no descent.

**Theorem 3 (the codimension-two blue-out/red-in square gate).** Assume no monochromatic full antipodal geodesic exists. Let \(S,T\in\mathcal R_x\) be disjoint and leave two missing dimensions \(M=\{i,j\}\). Writing \(y=y_S\), the square \(F_S\) satisfies
\[
\boxed{
c_i(y)=c_j(y)=1,\qquad
c_j(y\oplus e_i)=c_i(y\oplus e_j)=0.
}
\tag{3}
\]
Thus **both** dimension-simple paths across the square have word \(10\), and
\[
\boxed{\kappa(F_S)=0,\qquad
\Omega_0(F_S;y)=\Omega_1(F_S;y)=0.}
\tag{4}
\]
The opposite face \(F_T=\tau F_S\) obeys the same blue-out/red-in rule at its lower corner \(y_T\) in the rooted Boolean order.

*Proof.* The only two paths across a square use the orders \(i,j\) and \(j,i\). Theorem 1 forbids the three nondecreasing two-bit words \(00,01,11\); thus each must have word \(10\), proving (3). Their color sums are both one, so the sum of the four square-edge bits is zero, giving \(\kappa=0\). Neither route is monochromatic in either color, so \(\Omega_0=\Omega_1=0\). Antipodal translation reverses colors and interchanges the top and bottom of the square, sending a route word \(10\) to the reversed-complemented word \(10\), proving the statement for the opposite face. \(\square\)

The gate is stronger than ordinary flatness: a flat square can have monochromatic two-step paths, while (3) rules out even a one-switch ascending route compatible with the two red arms. In particular, if a legal coloring contains two disjoint red geodesic arms from a root whose missing pair of dimensions spans a curved square, **then a monochromatic full geodesic exists**, without requiring any no-counterexample hypothesis.

#### Projective reachability coverage

Call a two-face \(F\) **two-arm covered** if for some root \(x\) and disjoint \(S,T\in\mathcal R_x\) with \(S\cup T=D\setminus\{i,j\}\), the face \(F\) is the residual square \(F_S\) in dimensions \(i,j\). Since the same data gives \(F_T=\tau F_S\), coverage is antipodally invariant. Let \(Y=\partial Q_n/\tau\cong\mathbb RP^{n-1}\), and let \(B(c)\subseteq Y\) be the cubical subcomplex consisting of its entire one-skeleton together with all projected two-arm-covered squares and their faces.

**Theorem 4 (homological coverage certificate in odd dimension).** Suppose \(n\ge3\) is odd. If the inclusion
\[
\iota_*:H_2(B(c);\mathbb F_2)\longrightarrow
H_2(Y;\mathbb F_2)\cong\mathbb F_2
\tag{5}
\]
is nonzero, then the unrestricted NORI1 conclusion holds: some monochromatic full antipodal geodesic exists.

Equivalently, **under a hypothetical NORI1 counterexample in odd dimension, the inclusion (5) must be zero**. Furthermore at least \(2^{n-3}\) antipodal square orbits lie outside \(B(c)\); each canonical projected exchange disk contains an odd number of uncovered squares with nonzero curvature.

*Proof.* Suppose there is no monochromatic full geodesic. By Theorem 3, the square curvature \(\bar\kappa\) vanishes on every two-face of \(B(c)\). Article XIV, Subsection 28, proves \([\bar\kappa]=u^2\), the nonzero degree-two class of \(Y\). Therefore every two-cycle supported in \(B(c)\) pairs to zero with \(\bar\kappa\), and cannot represent the nonzero class of \(H_2(Y)\). This proves the claim about (5). The same subsection proves that \(\bar\kappa\) has at least \(2^{n-3}\) supported square orbits; all of them lie outside \(B(c)\). Its antipodal exchange-disk Stokes identity gives odd curvature evaluation on each canonical projected disk, so each disk contains an odd number of curvature squares, all uncovered. \(\square\)

**Proof-search implication.** The theorem translates the topological \(u^2\) obstruction into a **geometrically defined deficiency of dimension-simple monochromatic reachability**. An odd-dimensional counterexample would have to leave enough uncovered squares to prevent the red two-arm coverage subcomplex from carrying any projective two-homology generator. Proving instead that its reachability coverage carries such a generator would settle odd-dimensional NORI1. This is a sufficient structural target, not a new hypothesis defining a restricted graph family. In even dimension, the ordinary curvature class vanishes and this particular \(u^2\)-pairing argument does not apply; the rooted square-gate and residual-face descent theorems remain valid in both parities. A full Wu–Yang chain lift must account for that additional root/order information.

#### Theorem 5 (sharp all-rank descending-turn demand)

Let \(F\) be an arbitrary \(m\)-dimensional Boolean face with a specified starting corner \(y\), \(m\ge2\), and an arbitrary binary undirected-edge coloring (no antipodal condition needed inside \(F\)). Suppose **every** monotone full geodesic in \(F\), starting at \(y\) and using its \(m\) free dimensions once, contains a consecutive color descent \(1\to0\).

Let \(D_{10}(F;y)\) denote the number of distinct directed two-edge monotone paths
\[
y\oplus\mathbf1_A
\longrightarrow y\oplus\mathbf1_{A\cup\{i\}}
\longrightarrow y\oplus\mathbf1_{A\cup\{i,j\}}
\quad(A\subseteq M,\;i,j\in M\setminus A,\;i\ne j)
\]
whose first edge has color \(1\) and second edge color \(0\). Then
\[
\boxed{D_{10}(F;y)\ge m(m-1).}
\tag{6}
\]
Equality is attained for every \(m\): give all edges leaving rank zero color \(1\), all edges leaving rank one color \(0\), and all edges at higher ranks color \(0\). Then every full path has a descent at its first two steps and there are precisely \(m(m-1)\) descending two-edge paths.

*Proof.* There are \(m!\) monotone full dimension orders. A prescribed two-edge turn occurring after a prefix of \(a=|A|\) dimensions is contained in precisely
\[
a!\,(m-a-2)!
\]
full ordered geodesics: the first \(a\) dimensions may be permuted freely before the turn and the remaining \(m-a-2\) afterward. For \(0\le a\le m-2\),
\[
a!\,(m-a-2)!\le(m-2)!.
\]
Every full geodesic contains at least one descending turn by assumption, so counting pairs consisting of a full geodesic and one of its descending turns gives
\[
m!\le D_{10}(F;y)\,(m-2)!,
\]
proving (6). In the exhibited rank coloring, the only descents occur between the first and second edges, and the two dimensions in those positions can be any of the \(m(m-1)\) ordered pairs, giving equality. \(\square\)

**Corollary 6 (quantitative residual-face condition in a hypothetical NORI1 counterexample).** For every root \(x\) and disjoint red-reachable dimension sets \(S,T\) leaving \(m\ge2\) unused dimensions, their residual face \(F_S\) contains at least \(m(m-1)\) distinct descending monotone two-edge turns. At \(m=2\) there are just two possible turns, so the lower bound forces both to descend, recovering Theorem 3's blue-out/red-in square gate.

The inequality is independent of any specialized coloring family, is sharp in every rank, and provides a local turn-count lower bound for future attempts to double count residual-face demands against the global distribution of red and blue incidences. It does not by itself yield a global contradiction.

#### Corollary 7 (rank-weighted descent inequality)

In the setting of Theorem 5, let \(D_r(F;y)\) denote the number of descending two-edge paths whose first edge is traversed after precisely \(r\) preceding dimensions, \(0\le r\le m-2\). Then
\[
\boxed{
\sum_{r=0}^{m-2}
\frac{D_r(F;y)}{m(m-1)\binom{m-2}{r}}\ge1.
}
\tag{7}
\]
The inequality is sharp for all \(m\ge2\). In the absence of a monochromatic full antipodal geodesic, every residual face of two disjoint red-reachable arms obeys (7).

*Proof.* A fixed descent with \(r\) preceding dimensions lies on \(r!(m-r-2)!\) of the \(m!\) full dimension orders, hence on a fraction \(1/[m(m-1)\binom{m-2}{r}]\) of them. The left-hand side is the expected number of descents on a uniformly random monotone full geodesic. Every such geodesic has at least one descent by hypothesis, so the expectation is at least one. The rank-zero blue-then-red coloring from Theorem 5 produces precisely one descent per complete path, attaining equality. \(\square\)

The rank-weighted form distinguishes where in a residual face descending turns occur; a turn in a middle rank lies on fewer complete dimension orders than one near an endpoint. It may be more useful than the unweighted lower bound when combining multiple overlapping residual-face demands.

#### Corollary 8 (unique gate corner and maximal root-sensitive square defects)

Suppose a two-arm-covered square satisfies the gate relation (3). In the square itself, **one corner is distinguished** by having both outward square edges blue and both edges entering its opposite corner red. This corner is unique, independent of the red-arm witness. At that corner and its opposite, the two monochromatic exchange defects both vanish. At either of the two adjacent corners, the two traversals across the square have respective color words \(00\) and \(11\), so
\[
\boxed{\Omega_0=\Omega_1=1\quad\text{at both adjacent corners},}
\tag{8}
\]
while \(\kappa=0\) everywhere on the face.

*Proof.* Write the original gate corner as \(y\). Its incident square edges both have color \(1\); the edges at the opposite corner \(y\oplus e_i\oplus e_j\) both have color \(0\). Each adjacent corner therefore has one incident blue edge and one incident red edge, so no other corner can have the blue-out/red-in pattern. From either adjacent corner, the two increasing routes cross the four square edges in the patterns \(00\) and \(11\). Thus one route is red-monochromatic, the other blue-monochromatic, giving (8). From \(y\), both routes have word \(10\), and from the opposite corner both have word \(01\), so neither is monochromatic. Flatness follows from the two blue and two red edge bits. \(\square\)

This specifies the **additional order-sensitive signal in a flat square**: its rooted monochromatic defects change maximally between adjacent corners even though ordinary curvature is zero. The unique source corner supplies an intrinsic way to label such a gate for any future color-sensitive chain correction. In particular, merely enforcing zero curvature would miss all these defects.

For each red edge xy the contractible prefix bridge B lies in both red prefix cones K_x and K_y. Complementing K_x union its antipode, B union its antipode, and K_y union its antipode inside the cube boundary gives an equivariant zigzag Y_x -> Y_B <- Y_y. Naturality of Alexander duality makes both inclusions integral homology equivalences; since these complements are equivariant homotopy spheres, they are equivariant homotopy equivalences. Coherence around squares remains open.

**Theorem.** Assume that an antipodally odd coloring of \(Q_n\), \(n\ge3\), has no full geodesic with at most one switch. Let \(K_x^a\) be the monochromatic geodesic-prefix complex for root \(x\) and color \(a\), and
\[
Y_x^a=\partial[0,1]^n\setminus(K_x^a\cup AK_x^a).
\]
The dimension-drop theorem gives \(Y_x^a\simeq_{\mathbb Z_2}S^{n-2}\). For an edge \(xy\) of color \(a\) in dimension \(i\), put
\[
B_{xy}^a=(K_x^a\cap H_{i,x_i})\cup[x,y]\cup(K_y^a\cap H_{i,y_i}),
\]
and \(Y_{xy}^a=\partial[0,1]^n\setminus(B_{xy}^a\cup AB_{xy}^a)\).
Then both canonical inclusions
\[
Y_x^a\hookrightarrow Y_{xy}^a\hookleftarrow Y_y^a
\]
are equivariant homotopy equivalences.

*Proof.* Each facet-restricted prefix complex in \(B_{xy}^a\) is a simplicial cone. Collapsing these cones to their apexes reduces \(B_{xy}^a\) to the joining edge; hence it is collapsible. Since \(B_{xy}^a\subseteq K_x^a\) and \(K_x^a\cap AK_x^a=\varnothing\), the bridge and its antipode are disjoint. The dimension-drop theorem applies to its complement.

Naturality of Alexander duality identifies the homology map of \(Y_x^a\hookrightarrow Y_{xy}^a\) with the dual of the cohomology map
\[
B_{xy}^a\sqcup AB_{xy}^a\hookrightarrow K_x^a\sqcup AK_x^a.
\]
Both unions have two contractible components, and the inclusion identifies the components. Their reduced integral cohomology therefore agrees, so the induced map between complements is an integral homology equivalence. The complements have the homotopy type of \(S^{n-2}\); the inclusion is consequently an underlying homotopy equivalence. Equivariant Whitehead for free \(\mathbb Z_2\)-CW spaces upgrades it to an equivariant homotopy equivalence. Repeat with \(y\). \(\square\)

**Corollary.** The bridge inclusions identify the mod-two fundamental classes in \(\widetilde H_{n-2}(Y_x^a)\), \(\widetilde H_{n-2}(Y_{xy}^a)\), and \(\widetilde H_{n-2}(Y_y^a)\) without choosing homeomorphisms with a standard sphere.

**Remaining gap.** Transport of these one-dimensional homology groups does not retain the set of used dimensions. Thus composing such transports along arbitrary monochromatic walks would return to the component-connectivity weakness of Wu–Yang. The needed chain map must retain the support filtration of the bridge: coning a path across an \(i\)-edge is valid only when its existing dimension support avoids \(i\). Compatible higher transports around cubical squares and beyond have not been constructed.

The union of the red and blue prefix complexes at a root is a cone. Its intersection with its antipodal image characterizes a full one-switch geodesic. Every colored edge admits a contractible bridge between these cones and their lower-dimensional antipodal complements. Higher square coherence remains open.

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd undirected edge coloring, \(n\ge3\). For each root \(x\), write \(K_x^a\) for the monochromatic color-\(a\) geodesic-prefix Freudenthal subcomplex of Article XIV. Define
\[
\boxed{C_x=K_x^0\cup K_x^1.}
\]
Both constituents are simplicial cones with apex \(x\), so \(C_x\) is a cone. Every simplex uses disjoint sets of cube dimensions between its consecutive support sets. Every edge incident to \(x\) lies in \(C_x\), regardless of color. Antipodal oddness yields \(AC_x=C_{\bar x}\).

**Theorem 1 (color-blind antipodal intersection).** For each root \(x\),
\[
\boxed{C_x\cap C_{\bar x}\ne\varnothing
\iff\text{a full geodesic beginning at }x\text{ has at most one switch}.}
\]

*Proof.* These two cones are subcomplexes of the same antipodally invariant rooted Freudenthal triangulation. If they intersect, they share a vertex \(y\). There are monochromatic geodesics \(x\to y\) of some color \(a\), and \(\bar x\to y\) of some color \(b\). Their dimension supports are complementary, so concatenating the first with the reversal of the second gives a full geodesic whose word is a run of \(a\) followed by a run of \(b\). Conversely, split any at-most-one-switch full geodesic from \(x\) at its change, or at any intermediate vertex if it is monochromatic. The two segments, one read backward from \(\bar x\), are monochromatic paths meeting at a vertex in both cones. \(\square\)

**Corollary 2 (single sphere target per root).** If no monochromatic full antipodal geodesic exists anywhere, then all \(C_x\) are disjoint from their antipodes and are contained in the cube boundary \(S^{n-1}\). The complements
\[
Z_x=S^{n-1}\setminus(C_x\cup AC_x)
\]
have the equivariant homotopy type of the antipodal sphere \(S^{n-2}\).

*Proof.* By root-slide rotation, one-switch full geodesics are equivalent to monochromatic full geodesics over freely varying roots. Theorem 1 gives disjointness. No monochromatic prefix of either color can use all \(n\) dimensions, so every generating simplex lies in a proper cubical face. The cone \(C_x\) is collapsible. The equivariant Alexander-dual dimension-drop theorem proved earlier applies. \(\square\)

**Theorem 3 (universal colored-edge bridge for the single target family).** If \(xy\) is a cube edge of color \(a\), with varying dimension \(i\), let
\[
B_{xy}^a=(K_x^a\cap H_{i,x_i})\cup[x,y]\cup
(K_y^a\cap H_{i,y_i}).
\]
This contractible bridge is contained in \(K_x^a\cap K_y^a\), and therefore in \(C_x\cap C_y\). Under the same hypothetical NORI1 counterexample, the inclusions
\[
\boxed{
Z_x\hookrightarrow Z_{xy}\hookleftarrow Z_y,\qquad
Z_{xy}=S^{n-1}\setminus(B_{xy}^a\cup AB_{xy}^a),
}
\]
are equivariant homotopy equivalences. This holds for **every** cube edge, regardless of its color, using a single target \(Z_x\) at each root.

*Proof.* The earlier red-edge cone-extension theorem applies to an edge of color \(a\) with that color in place of red. Every prefix being coned uses dimensions other than \(i\), so the added \(i\)-edge preserves independence. The bridge is collapsible, as proved in the canonical bridge lemma. Under Corollary 2, it is disjoint from its antipode and lies in each endpoint cone \(C_x,C_y\). Alexander duality makes both complement inclusions integral homology equivalences, since each inclusion of a bridge together with its antipode into a larger pair of cones identifies the two contractible components. By the equivariant dimension-drop theorem and equivariant Whitehead, these homology equivalences are equivariant homotopy equivalences. \(\square\)

**Theorem 4 (flat integral transport and ordinary homotopy-class coherence).** Under the hypotheses of Corollary 2, choose an orientation of the boundary sphere \(S^{n-1}\). For each cube root \(x\), let
\[
o_x\in\widetilde H_{n-2}(Z_x;\mathbb Z)\cong\mathbb Z
\]
be the class corresponding under integral Alexander duality to the characteristic function of the component \(C_x\) in
\(\widetilde H^0(C_x\sqcup AC_x;\mathbb Z)\). Then:

(i) For every cube edge \(xy\), the canonical bridge zigzag of Theorem 3 carries \(o_x\) to \(o_y\).

(ii) Given any two cube-edge walks \(\gamma,\gamma'\) with the same starting and terminal roots, the induced homotopy equivalences \(Z_x\to Z_y\), defined by composing the bridge zigzags and choosing homotopy inverses, are homotopic as ordinary maps. In particular, every cubical square is coherent in the unfiltered homotopy category.

(iii) Antipodal inversion satisfies
\[
\boxed{A_*o_x=(-1)^n o_{\bar x},\qquad o_{\bar x}=-o_x.}
\tag{8}
\]
Since \(o_{\bar x}=-o_x\) in the identical space \(Z_{\bar x}=Z_x\), the intrinsic degree of \(A:Z_x\to Z_x\) is \((-1)^{n+1}=(-1)^{n-1}\), as required for the antipodal sphere \(S^{n-2}\). The transport between antipodal roots instead has intrinsic degree \(-1\). These two maps have different homotopy classes precisely when \(n\) is odd.

*Proof.* Put \(m=n-1\). Integral Alexander duality in the oriented sphere gives natural isomorphisms
\[
\widetilde H_{m-1}(S^m\setminus (D\sqcup AD);\mathbb Z)
\cong \widetilde H^0(D\sqcup AD;\mathbb Z)
\tag{9}
\]
whenever \(D\) and \(AD\) are disjoint nonempty contractible compact polyhedra. The characteristic function of \(D\), considered modulo constant functions on the two components, is a generator of the group on the right.

For an edge \(xy\) of color \(a\), use \(D=B_{xy}^a\) in (9). The bridge and its antipode are disjoint contractible subpolyhedra, and \(B_{xy}^a\subseteq C_x\cap C_y\). Restriction of locally constant functions sends the characteristic functions of \(C_x\) and \(C_y\) to the characteristic function of \(B_{xy}^a\). Naturality of (9) therefore shows that both inclusions \(Z_x,Z_y\hookrightarrow Z_{xy}\) carry their distinguished homology generators to the same generator. This proves (i).

Theorem 3 makes both inclusions homotopy equivalences. Their homotopy inverse classes are unique, so an edge zigzag defines a homotopy class of equivalences \(Z_x\to Z_y\), and every composite along a walk takes \(o_x\) to \(o_y\). Since \(Z_x\) and \(Z_y\) have the homotopy type of \(S^{n-2}\), where \(n-2\ge1\), homotopy classes of maps \(Z_x\to Z_y\) are determined by their integer degree. Thus all root-walk composites with the same endpoints are homotopic. This proves (ii).

Finally, antipodal inversion has degree \((-1)^n\) on the ambient sphere \(S^{n-1}\), and interchanges the two components of \(C_x\sqcup AC_x\). The latter interchange negates the generator of reduced integral zeroth cohomology. Naturality of Alexander duality, including the ambient orientation degree, gives
\[
A_*o_x=(-1)^n o_{\bar x}.
\]
proving (iii). \(\square\)

**Theorem 5 (equivariant flatness).** Under the hypotheses of Theorem 4, any two bridge transports between the same roots are homotopic **through antipode-equivariant maps**. Thus all root squares commute in the equivariant homotopy category of unfiltered complements.

*Proof.* We first establish the equivariant Hopf-degree lemma: two antipode-equivariant maps \(f,g:S^k\to S^k\), \(k\ge1\), with equal integer degrees are equivariantly homotopic. For \(k=1\), the induced maps on the quotient circle have the same odd degree; a homotopy of quotient maps lifts with the prescribed initial lift.

For \(k\ge2\), the quotient maps \(\bar f,\bar g:\mathbb RP^k\to\mathbb RP^k\) both induce the identity on \(\pi_1\). As the universal covering sphere is \((k-1)\)-connected, their sole homotopy obstruction (with the action on \(\pi_1\) fixed) lies in
\[
H^k(\mathbb RP^k;\pi_k(S^k)_{\rm sign})
=H^k(\mathbb RP^k;\mathbb Z_{\rm or})\cong\mathbb Z.
\]
The deck action on \(\pi_k(S^k)\) is multiplication by \((-1)^{k+1}\), the orientation local system. Pullback to the double cover \(S^k\) sends this obstruction to \(\deg(f)-\deg(g)\). Pullback of the top twisted cohomology generator is twice the generator of \(H^k(S^k;\mathbb Z)\), and is injective. Therefore equal degrees annihilate the obstruction. The quotient homotopy lifts to an equivariant homotopy.

By Corollary 2, every \(Z_x\) is equivariantly homotopy equivalent to \(S^{n-2}\). Hence the lemma applies after such identifications. Theorem 4(i) proves that every bridge-walk composite sends the distinguished generator \(o_x\) to \(o_y\), so all composites with the same endpoints have degree \(+1\) under these identifications and are equivariantly homotopic. \(\square\)

**Remaining limitation.** Homotopy-category flatness does not select coherent higher homotopies or preserve the sets of dimensions used by witnesses and their switch filtrations. These remain the missing chain-level ingredients in a dimension-simple Wu--Yang modification.

**Filtration distinction.** The theorem supplies homotopy classes of transport maps and homotopy commutativity of their squares after forgetting dimension-support certificates. It does not construct specified square homotopies, compatible higher homotopies, or filtered chain maps. In particular, these ordinary homotopy classes cannot detect whether an edge prepended to a prefix repeats a dimension. The unresolved Wu–Yang adaptation lies in precisely that stronger coherent, dimension-simple lifting problem.

**The remaining task.** All monochromatic prefix witnesses remain dimension-simple. The construction gives an antipodally symmetric family of contractible carriers and root-changing sphere correspondences over the *entire cube graph*. Passing just to top homology loses dimension support, returning to the connected-component problem in Wu–Yang. A useful chain-map construction must retain the support filtration: a dimension \(i\) may be inserted into a prefix only when it is absent already. Compatible fillings of the mixed-color square exchange defects and higher cubical faces are unproved. This is the new central proof obligation, rather than another specialized coloring class.

**Theorem 6 (degree obstruction on compact models; noncompact fixed-point barrier).** Under the hypothetical absence of an at-most-one-switch full geodesic, let \(\gamma\) be any root walk from \(x\) to \(\bar x\), and let \(T_\gamma:Z_x\to Z_{\bar x}=Z_x\) be a representative of its equivariant bridge-transport class. Then
\[
\boxed{\deg T_\gamma=-1,\qquad \deg(A^{-1}T_\gamma)=(-1)^n.}
\tag{10}
\]
Transport \(f=A^{-1}T_\gamma\) through any equivariant homotopy equivalence \(Z_x\simeq_{\mathbb Z_2}S^{n-2}\) to a self-map \(\widetilde f:S^{n-2}\to S^{n-2}\). This compact-model map has
\[
\boxed{L(\widetilde f)=2.}
\tag{11}
\]
Thus \(\widetilde f\) has an antipodal pair of fixed points; after a generic equivariant perturbation the signed sum of fixed-point indices over antipodal pairs is \(1\).

*Proof.* From Theorem 4(i), \(T_{\gamma*}o_x=o_{\bar x}=-o_x\), proving the first degree. The intrinsic degree of \(A\) is \((-1)^{n-1}\) by corrected Theorem 4(iii), proving the second degree. Let \(k=n-2\). Equivariant homotopy equivalence preserves degree, so \(\deg\widetilde f=(-1)^n=(-1)^k\), and the compact sphere has Lefschetz number
\[
L(\widetilde f)=1+(-1)^k\deg\widetilde f=2.
\]
The Lefschetz fixed point theorem applies to the compact sphere. Equivariance pairs the fixed points; local indices in an antipodal pair agree by conjugation. A generic perturbation yields isolated nondegenerate fixed points, whose pairwise signed sum is therefore \(L/2=1\). \(\square\)

**Proposition 7 (sharp failure of the complement-level coincidence inference).** The degree and symmetry data in Theorem 6 do **not** force \(T_\gamma(z)=Az\) for a point \(z\) in the original open complement \(Z_x\). In fact there is an antipode-equivariant, fixed-point-free homotopy equivalence of the noncompact free antipodal space \(S^1\times\mathbb R\) with Lefschetz number \(2\).

*Proof.* Define the free involution \(A(s,t)=(-s,-t)\) on \(S^1\times\mathbb R\), where \(s=(s_1,s_2)\in S^1\), and let \(R(s_1,s_2)=(s_1,-s_2)\) be reflection. Define
\[
f(s,t)=(Rs,\ t+s_1).
\tag{12}
\]
Then \(fA=Af\), and \(f\) is a homeomorphism with inverse \(f^{-1}(s,t)=(Rs,t-s_1)\). It induces degree \(-1\) on \(H_1(S^1\times\mathbb R;\mathbb Z)\), so its alternating homology trace is \(L(f)=1-(-1)=2\). A fixed point would satisfy \(Rs=s\), which forces \(s=(1,0)\) or \((-1,0)\), and also \(t+s_1=t\), which requires \(s_1=0\). These conditions are incompatible. Finally \(T=Af\) is equivariant with degree \(-1\), while \(T(s,t)=A(s,t)\) would require \(f(s,t)=(s,t)\), which never occurs. \(\square\)

**Research consequence.** The degree and signed parity are valid invariants on compact equivariant sphere models, but moving a forced compact-model fixed point back to the original complement requires geometric control beyond a homotopy equivalence. This exposes a further necessary feature of a Wu--Yang adaptation: a compact, support-preserving carrier construction (or an alternative compactness/properness argument) is required before interpreting topological coincidences as dimension-simple geodesics.

**Proposition 8 (a color-independent countermodel for unfiltered transport).** For every \(n\ge3\), independently of any edge coloring, let
\[
S_x=\bigcup_{i=1}^n[x,x\oplus e_i]\subseteq\partial[0,1]^n
\]
be the cubical one-skeleton star at root \(x\). Then:

(i) Each \(S_x\) is a contractible cone, \(AS_x=S_{\bar x}\), and \(S_x\cap AS_x=\varnothing\).

(ii) For every cube edge \(xy\), the bridge \([x,y]\) lies in \(S_x\cap S_y\); the complement zigzag
\[
\partial I^n\setminus(S_x\cup AS_x)
\ \longrightarrow\
\partial I^n\setminus([x,y]\cup A[x,y])
\ \longleftarrow\
\partial I^n\setminus(S_y\cup AS_y)
\tag{13}
\]
consists of equivariant homotopy equivalences.

(iii) The integral generator transports, path-independence up to equivariant homotopy, and the antipodal signs in Theorems 4--5 hold for these stars, unchanged. Nevertheless the construction carries no edge-color information and has no monochromatic full-path certificate.

*Proof.* A star is a geometric tree with center \(x\), hence collapsible. Every vertex in the star has graph distance at most one from \(x\). Stars centered at antipodes have no common vertex for \(n\ge3\), since antipodal roots have distance \(n>2\); distinct cube edges meet geometrically only at common endpoints. Central inversion carries each incident edge to its antipodal image. For adjacent \(xy\), the common edge belongs to both stars. The two stars and the bridge, together with their antipodal images, are pairs of disjoint compact contractible polyhedra. Integral Alexander duality, as in Theorem 4, makes both complement inclusions in (13) integral homology equivalences. Each complement has the equivariant homotopy type of an antipodal \(S^{n-2}\), by the dimension-drop argument for collapsible carriers, so these maps are equivariant homotopy equivalences. The orientation and degree calculations of Theorems 4--5 require only these properties, proving (iii). No star contains a two-dimensional prefix simplex; the construction is independent of the coloring. \(\square\)

**Corollary 9 (the first color-sensitive distinction occurs at rank two).** For the star model, the union of corner carriers over any square \(F\) meets \(F\) in \(\partial F\) for every square coloring. In the monochromatic-prefix model, the same union fills \(F\) for patterns \(0000\) and \(0011\), and has nontrivial \(H_1\) for patterns \(0001\) and \(0101\), as proved in the rank-two square-carrier subsection of Article XIV. Thus the unfiltered transport axioms of Theorems 3--5 alone cannot imply NORI1 or any switch bound. A successful chain argument must use color-sensitive higher-incidence information absent from the star countermodel.

*Proof.* The union of stars at the four square corners consists of its four boundary edges. The prefix-carrier classification follows from the cited rank-two theorem. The same unfiltered axioms hold in both settings by Proposition 8; therefore those axioms alone cannot constrain the color words of complete paths. \(\square\)

### Monochromatic geodesic endpoint posets and a global rank-bounded target

The monochromatic prefix complexes depend on a chosen root. The following construction places the geodesic certificates from all roots in one finite poset. Its order retains the condition needed for dimension-simple concatenation, while intervals with fixed endpoints provide nested contractible carriers. Under a hypothetical failure of NORI1, this global complex admits an explicit equivariant map to \(S^{n-3}\).

Let \(c\) be any binary coloring of the undirected edges of \(Q_n\). Fix a color \(a\), and let \(\mathcal P_a(c)\) consist of the ordered pairs \((u,v)\) of distinct cube vertices for which a color-\(a\) geodesic from \(u\) to \(v\) exists. Write \(d\) for Hamming distance. Define
\[
(u,v)\preceq(u',v')
\tag{1}
\]
when color-\(a\) geodesics from \(u'\) to \(u\) and from \(v\) to \(v'\) exist, allowing empty paths, and
\[
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{2}
\]
Thus (2) requires the two extensions and the intervening path to use disjoint dimension sets.

**Theorem 1 (a poset with coherent path certificates).** Relation (1) is a partial order. Its rank function
\[
r(u,v)=d(u,v)
\]
strictly increases under strict comparison. Every chain in \(\mathcal P_a(c)\) is witnessed simultaneously by one color-\(a\) geodesic containing all its ordered endpoint pairs as nested subpaths. Endpoint reversal
\[
J(u,v)=(v,u)
\tag{3}
\]
is an order-preserving involution, free on the order complex.

*Proof.* Reflexivity follows by using empty extensions. If two pairs are comparable and have equal rank, (2) forces both extension lengths to vanish, so the pairs agree. This proves antisymmetry and strict rank increase.

To prove transitivity, suppose
\[
(u,v)\preceq(u',v')\preceq(u'',v'').
\]
Choose monochromatic witnesses for the four extensions and for \(u\to v\). Their concatenation is
\[
u''\to u'\to u\to v\to v'\to v''.
\]
The two distance equalities show that its length is \(d(u'',v'')\). Hence it is a cube geodesic: every dimension used in any constituent is used once in the entire path. In particular its initial portion \(u''\to u\) and terminal portion \(v\to v''\) are monochromatic geodesics, proving the required comparison. Repeating this argument proves the simultaneous witness assertion for an arbitrary chain.

Undirected path reversal preserves monochromaticity and reverses the distance decomposition, giving (3). The involution fixes no ordered pair. It also fixes no simplex setwise: the vertices of a chain have distinct ranks, and an invariant chain would have to fix its unique vertex at each represented rank. \(\square\)

**Theorem 2 (nested contractible carriers for fixed endpoints).** For each \(p=(u,v)\in\mathcal P_a(c)\), the order complex of the principal ideal
\[
\mathcal P_{\le p}=\{q:q\preceq p\}
\tag{4}
\]
is a simplicial cone with apex \(p\). If \(p\preceq p'\), these carriers are nested. Every monochromatic geodesic with endpoints \(u,v\), together with all its oriented nonempty subpaths, is represented in the same carrier (4).

*Proof.* The ideal has maximum element \(p\), so adjoining \(p\) to any chain gives another chain. This proves the cone assertion. Ideal inclusion gives nesting. A subpath of a monochromatic geodesic satisfies (2), and the portions before and after it supply the required monochromatic extensions. \(\square\)

For example, when both routes across a square are monochromatic of the same color, their orders define one endpoint pair and lie in its common contractible carrier. Identifying these orders preserves a shortest-path witness with its dimension support. It requires no transitivity of unrestricted unrooted reachability: transitivity in Theorem 1 uses (2) at every composition. When one route changes color, that route supplies no monochromatic certificate to this carrier.

**Theorem 3 (global equivariant dimension bound).** Let \(n\ge3\), and suppose
\[
c(\bar e)=1-c(e).
\]
If \(c\) has no monochromatic full antipodal geodesic, then, for either color \(a\),
\[
\boxed{\dim\Delta\mathcal P_a(c)\le n-3.}
\tag{5}
\]
There is an explicit \(J\)-equivariant simplicial map
\[
\boxed{\Delta\mathcal P_a(c)\longrightarrow
\partial\operatorname{Crosspolytope}_{n-2}\cong S^{n-3}.}
\tag{6}
\]
The assertions include an empty order complex.

*Proof.* A monochromatic geodesic of length \(n-1\) leaves one dimension \(i\) unused. Its endpoints \(u,v\) differ in every other dimension. The two dimension-\(i\) edges incident with \(u,v\) are antipodal, so one has the path's color. Prepending or appending that edge gives a monochromatic full geodesic. Thus the hypothesis excludes every monochromatic geodesic of length \(n-1\), as well as length \(n\). Every pair in \(\mathcal P_a(c)\) has rank between \(1\) and \(n-2\). Strict rank increase bounds the number of vertices in a chain by \(n-2\), proving (5).

Fix an ordering of the cube dimensions. For a pair \(p=(u,v)\), let \(i(p)\) be the first dimension in which \(u,v\) differ, and define
\[
\lambda(p)=(-1)^{u_{i(p)}}e_{r(p)}
\in\{\pm e_1,\ldots,\pm e_{n-2}\}.
\tag{7}
\]
Swapping endpoints negates the label. In a chain all ranks differ, so its labels use distinct axes and span a face of the crosspolytope boundary. Formula (7) therefore defines the simplicial map (6). \(\square\)

The involution in (6) is reversal of ordered monochromatic endpoints. Geometric cube antipodality has the additional color-complementing action
\[
A:\mathcal P_a(c)\longrightarrow\mathcal P_{1-a}(c),
\qquad A(u,v)=(\bar u,\bar v).
\tag{8}
\]
It preserves the order and commutes with \(J\). A source-to-target construction must track both operations.

**Theorem 4 (root transport has one global endpoint certificate).** Let \(xy\) be a color-\(a\) edge in dimension \(i\). Suppose there are color-\(a\) geodesics from \(x\) with support \(S\), and from \(y\) with support \(T\), where
\[
i\notin S\cup T,\qquad S\cap T=\varnothing.
\tag{9}
\]
Then
\[
\boxed{(x\oplus\mathbf1_S,\ y\oplus\mathbf1_T)
\in\mathcal P_a(c)}
\tag{10}
\]
has rank \(|S|+|T|+1\). The certificate is unchanged when the joining edge is included in the first arm or in the second.

*Proof.* Reverse the first arm, traverse \(x\to y\), and traverse the second arm. Conditions (9) make the three dimension sets disjoint, so the result is a monochromatic geodesic between the endpoints in (10). Splitting it at \(x\) or at \(y\) changes only which arm contains dimension \(i\); its ordered endpoints and support remain fixed. \(\square\)

This realizes the support-preserving transport between neighboring prefix constructions within a single global poset. Longer transports remain governed by (2), which requires each concatenation to be a geodesic.

**Proposition 5 (the endpoint involution has nontrivial local topology).** If some vertex has three incident color-\(a\) edges in distinct dimensions, \(\Delta\mathcal P_a(c)\) contains a \(J\)-invariant circle on which \(J\) acts antipodally.

*Proof.* Let the center be \(x\) and the three neighbors be \(u_1,u_2,u_3\). Include the six oriented edge pairs \((u_i,x),(x,u_i)\) of rank one and the six pairs \((u_i,u_j)\), \(i\ne j\), of rank two. The latter are monochromatic geodesics through \(x\). Each rank-two pair is above its two directed edge pairs. The resulting incidence subcomplex is a twelve-cycle. Endpoint reversal sends each vertex to the vertex six steps away. Thus it is an antipodal circle. \(\square\)

**Remaining proof obligation.** Theorems 1–4 supply one global target, a dimension bound, and nested contractible carriers derived solely from the original monochromatic geodesics. They provide an alternative to separately choosing sphere models for root-dependent prefix complements. A proof of NORI1 still requires an equivariant augmentation-preserving chain assignment from the cube's antipodal carrier into this target, using the color-selective edge transports and compatible higher fillings. Such an assignment from \(S^{n-1}\) would contradict (6) by the chain-level Borsuk–Ulam obstruction. The assignment is unproved; the existence of a low-dimensional target alone supplies no contradiction.


### Rank-two monochromatic prefix triangles determine unrestricted edge colorings

For a binary coloring \(c\) of the undirected edges of \(Q_n\), \(n\ge2\), let
\[
C_x=K_x^0\cup K_x^1
\]
be the union of monochromatic geodesic-prefix Freudenthal subcomplexes rooted at \(x\). Its one-dimensional part includes every cube edge incident to \(x\), irrespective of its color. For distinct dimensions \(i,j\), let
\[
\Delta(x;i,j)=[x,x\oplus e_i,x\oplus e_i\oplus e_j]
\]
be the monotone rooted Freudenthal triangle.

**Theorem 1 (rank-two reconstruction).** Two undirected cube-edge binary colorings \(c,c'\) produce the same two-dimensional prefix triangles \(\Delta(x;i,j)\in C_x\), for all \(x\) and all distinct \(i,j\), if and only if \(c'=c\) or \(c'=1-c\) globally. The result holds without any antipodal assumption and therefore applies to the entire unrestricted NORI1 class.

*Proof.* A rooted two-step triangle occurs in \(C_x\) precisely when its two constituent edges are the same color:
\[
\Delta(x;i,j)\in C_x
\iff
c(\{x,x^i\})=c(\{x^i,x^{ij}\}).
\tag{1}
\]
The two edges in (1) are distinct edges incident at \(x^i\). Conversely, any two distinct incident cube edges have different dimensions and can be arranged in this order along some two-step geodesic, so their color equality is encoded by such a triangle. The line graph of \(Q_n\) is connected because \(Q_n\) is connected. Therefore knowledge of equality versus inequality for each pair of incident edges determines all edge colors relative to the color of one arbitrarily chosen edge. Changing that initial bit complements every edge, giving the only ambiguity. Global color complementation preserves every equality in (1), hence all the triangles. \(\square\)

**Theorem 2 (higher monochromatic prefixes are two-local).** Let
\[
x=v_0,v_1,\ldots,v_k
\]
be a cube geodesic using \(k\) distinct dimensions. For \(k\ge2\), its entire color word is monochromatic if and only if
\[
\boxed{
\Delta(v_{j-1};d_j,d_{j+1})\in C_{v_{j-1}}
\quad(1\le j<k),
}
\tag{2}
\]
where the path changes dimension \(d_j\) between \(v_{j-1},v_j\). Consequently the full family of higher-dimensional monochromatic prefix simplices is determined by the two-dimensional rooted triangle data together with the Boolean lattice's condition that each traversed dimension occurs once.

*Proof.* By (1), membership of the triangle indexed by \(j\) asserts equality of the colors of the consecutive \(j\)-th and \((j+1)\)-st edges. All these equalities hold precisely when the full word is constant. Since the dimensions are pairwise distinct, the path forms a legal geodesic prefix. Its corresponding Freudenthal simplex occurs in \(C_x\) precisely when that path has constant color. \(\square\)

**Minimality and proof direction.** The one-skeleton of the rooted prefix-cone family is color-blind, as demonstrated by the uncolored edge-star model of this Article. The anchored rank-two triangles are already sufficient to reconstruct the entire unrestricted coloring up to the irrelevant global exchange of its two bits; higher monochromatic witnesses introduce no new color comparisons, but do introduce **global compatibility of distinct dimensions**. A Wu–Yang-type chain-map modification can therefore seek a support-graded completion of these rank-two equality tests rather than an unbounded collection of auxiliary component labels. The outstanding theorem is the coherent, equivariant filling/cancellation of the resulting square-exchange defects while retaining dimension-simplicity.

### Odd face folding, two-polarity certificates, and transverse curvature oscillation

Select distinct dimensions \(a,b\) of a legally antipodally odd binary-colored \(Q_n\), with \(n\ge4\), and set \(m=n-2\). Let \(F_{00}\cong Q_m\) be the face where the \(a,b\) bits are zero and \(F_{11}\) its opposing face. Antipodality sends \((z,00)\) to \((\bar z,11)\). The coloring \(f\) induced on \(F_{00}\) is arbitrary; its opposing face has the color-complemented antipodal image.

#### Theorem 1 (odd folding and the two-polarity equivalence)

For any \(q:Q_m\to\mathbb F_2\) satisfying \(q(\bar z)=1-q(z)\), identify the two opposite \(m\)-faces with the two sides of a folded \(Q_{m+1}\), and assign color \(q(z)\) to the formal joining edge \((z,00)(z,11)\). The folded cube coloring is antipodally odd.

For an arbitrary coloring \(f\) of \(Q_m\), set
\[
T_f(u)=\{t\in\mathbb F_2:\text{there is an antipodal geodesic from }u
\text{ to }\bar u\text{ with word }t^*(1-t)^*\}.
\tag{1}
\]
Empty runs are permitted. Then
\[
\boxed{\text{the folded cube has a monochromatic full geodesic}
\ \Longleftrightarrow\ \exists u:\ q(u)\in T_f(u),}
\tag{2}
\]
and
\[
\boxed{T_f(\bar u)=\{1-t:t\in T_f(u)\}.}
\tag{3}
\]
For each fixed \(f\),
\[
\boxed{\text{every odd choice of }q\text{ yields a monochromatic folded geodesic}
\ \Longleftrightarrow\ \exists u:\ T_f(u)=\{0,1\}.}
\tag{4}
\]
Consequently **NORI1 in dimension \(m+1\)** is equivalent to: *Every arbitrary binary edge coloring of \(Q_m\) has some vertex supporting both a \(0^*1^*\) and a \(1^*0^*\) antipodal full geodesic.*

*Proof.* A monochromatic folded geodesic may be reversed so that it begins in \(F_{00}\), crosses its formal joining edge at vertex \(u\), and ends in \(F_{11}\). If its color is \(t=q(u)\), let its first segment in \(F_{00}\) run from \(z\) to \(u\) in color \(t\). Reverse that segment to obtain \(u\to z\) in color \(t\). Its last segment \(u\to\bar z\) in the second face transforms, by antipodal translation and reversal, into a color-\((1-t)\) segment \(z\to\bar u\) in \(F_{00}\). These two segments use disjoint dimension sets and concatenate to the certificate in (1). Conversely, given a face path \(u\to z\to\bar u\) with colors \(t\) then \(1-t\), reverse its first segment, traverse the formal joining edge at \(u\) in color \(t=q(u)\), and translate and reverse the second segment to form a folded monochromatic full path. This proves (2). Reversal of a face path proves (3). If \(T_f(u)=\{0,1\}\), any odd assignment \(q\) matches a certificate at that \(u\). If no \(T_f(u)\) contains both colors, choose \(q(u)\) outside \(T_f(u)\) independently on every antipodal vertex pair; (3) makes these choices compatible with oddness, and (2) yields no monochromatic folded full path. This proves (4). Every legally colored \(Q_{m+1}\) is a folded coloring by taking the two facets opposing across one dimension, proving the final equivalence. \(\square\)

#### Theorem 2 (one-exception lifting, conditional on the induction hypothesis)

Assume NORI1 holds in dimension \(n-1=m+1\). Then every legally colored \(Q_n\) has a full dimension-simple geodesic with all but at most one edge of the same color:
\[
\boxed{t^n\quad\text{or}\quad t^p(1-t)t^{n-p-1}.}
\tag{5}
\]
If no monochromatic full geodesic exists, then \(1\le p\le n-2\).

*Proof.* For each \(z\in Q_m\), let \(M(z)\) be the set of colors for which a two-step diagonal path from \((z,00)\) to \((z,11)\) using \(a,b\) once is monochromatic. Antipodal reversal gives \(M(\bar z)=\{1-t:t\in M(z)\}\). Choose the folded joining color \(q(z)\) from \(M(z)\) whenever this set is nonempty, and choose it arbitrarily and oddly elsewhere. The \((n-1)\)-dimensional induction hypothesis gives a folded monochromatic full geodesic of color \(t\) crossing at \(u\), with \(q(u)=t\). If \(M(u)\ne\varnothing\), our choice ensures that a color-\(t\) two-step diagonal path replaces the joining edge, giving an all-\(t\) full geodesic in \(Q_n\). If \(M(u)=\varnothing\), both two-step diagonal paths have one edge of each color, so replacement gives a full geodesic with one exceptional edge, as in (5). The replaced dimensions occur nowhere else in the path. An exceptional edge at the first or last position gives at most one switch, which root-slide rotation converts into a monochromatic full geodesic. \(\square\)

#### Theorem 3 (opposite-majority full paths at a common joining square)

Assume the \((n-1)\)-dimensional induction hypothesis, and suppose there is no monochromatic full geodesic in the original \(Q_n\). At some \(u\in F_{00}\) the arbitrary face coloring satisfies \(T_f(u)=\{0,1\}\). Its joining square in dimensions \(a,b\) cannot have a monochromatic diagonal two-step path of **either** color: combining that route with the corresponding face certificate via Theorem 1 would produce a monochromatic full geodesic in \(Q_n\). Therefore both diagonal routes are bichromatic. Applying the construction for the two face polarities separately gives a full \(n\)-geodesic with \(n-1\) red edges and one blue edge, and another with \(n-1\) blue edges and one red edge, traversing the **same** joining square. The two folded color assignments are allowed to differ.

#### Theorem 4 (gate and stripe obstruction, with run bounds)

Assume the hypotheses of Theorem 3. Since neither diagonal two-step route across the joining square is monochromatic, the two words are either \(10,10\), or \(01,01\), or \(01,10\). Call these respectively *gate 10*, *gate 01*, and *stripe*. Every such square has curvature zero. The gate has opposite colors on each pair of parallel edges and nonzero corner-root defect transport; the stripe has equal-colored parallel pairs and vanishing corner-root transport.

If the two face-polarity certificates at \(u\) have words
\[
0^r1^{m-r},\qquad 1^s0^{m-s},
\]
then, in the absence of a monochromatic full \(Q_n\) geodesic, **every** such pair obeys
\[
\boxed{
\begin{array}{c|c}
\text{joining square}&\text{required conditions}\\
10,10&r\ge1,\quad s\le m-1\\
01,01&r\le m-1,\quad s\ge1\\
01,10&1\le r,s\le m-1.
\end{array}}
\tag{6}
\]

*Proof.* Each two-step diagonal path is bichromatic, so its word is \(01\) or \(10\). The curvature is the xor of both two-step word parities, hence zero. If the first face certificate has word \(0^r1^{m-r}\), its folded color-zero path expands to \(0^r h_1h_2 0^{m-r}\), where \(h_1h_2\) is either available square word. For \(h=10\) this has at most one switch when \(r=0\); for \(h=01\) it has at most one switch when \(r=m\). Similarly the color-one certificate gives \(1^s h_1h_2 1^{m-s}\), which has at most one switch when \(h=10,s=m\) or when \(h=01,s=0\). The root-slide lemma then forbids the corresponding endpoint cases. When both words occur, all endpoint cases are excluded. The gate/stripe parallel-edge assertions follow by direct inspection of the four square-edge colors and the root-defect identity in Subsection 31. \(\square\)

#### Theorem 5 (monochromatic face paths force gates and transverse-curvature oscillation)

Assume no monochromatic full geodesic exists in \(Q_n\). Let \(P=(v_0,\ldots,v_m)\) be a monochromatic **red** full geodesic inside \(F_{00}\), with \(m=n-2\), using all remaining dimensions once. At **every** \(v_j\), the two portions of \(P\), read outward, are red geodesics with disjoint dimension sets partitioning the \(m\) face dimensions. The two-arm residual-square lemma of Article XIV, Subsection 41, therefore forces the joining square in \(a,b\) at each \(v_j\) to be a *gate 10*: both outgoing \(a,b\)-edges are blue, and the two edges entering the opposite corner are red. Stripes are impossible along \(P\).

At either chosen endpoint \(u\) of \(P\), the monochromatic face geodesic supplies **both** face-polarity certificates, by allowing one run to be empty. Choosing \(u=v_0\), the two expansions through the gate may be taken with words
\[
\boxed{0^m10\qquad\text{and}\qquad10\,1^m,}
\tag{7}
\]
whose unique minority edges occur at positions \(n-1\) and \(2\), respectively.

Let \(d_j\) be the dimension of the edge \(v_{j-1}v_j\), and for \(h\in\{a,b\}\) define
\[
W^{(h)}_j=\kappa(F_{\{h,d_j\}}(v_{j-1})),
\qquad 1\le j\le m.
\tag{8}
\]
The gate condition implies that each curvature word \(W^{(h)}\) is the edge-color word of the shifted copy \(P+h\): the side square has one red base edge and two blue connecting edges, whose contributions cancel modulo two. For \(k=\{a,b\}\setminus\{h\}\), adjoining a blue initial \(h\)-edge, traversing \(P+h\), then adjoining the red terminal \(k\)-edge gives a full dimension-simple antipodal geodesic with word
\[
\boxed{1\,W^{(h)}\,0.}
\tag{9}
\]
If \(W^{(h)}\) contains no \(01\), then (9) has at most one switch and gives NORI1 by a root slide. Applying the same construction to reversed \(P\) forces an occurrence of \(10\). Therefore
\[
\boxed{\text{Both }W^{(a)},W^{(b)}\text{ contain }01\text{ and }10.}
\tag{10}
\]
This is the transverse-curvature oscillation theorem from Article XIV, Subsection 47, now shown to be the precise obstruction along the **two transverse paths separating the folded one-exception lifts**. On each side square the red Freudenthal exchange defect is zero and the blue defect equals the curvature, as proved in that subsection.

**Scope.** The folding equivalence does not establish NORI1; Theorems 2–3 require the \((n-1)\)-dimensional NORI1 induction hypothesis. The curvature oscillation in Theorem 5 is conditional on a monochromatic full path within one of the \((n-2)\)-faces, which the induction hypothesis alone does not supply: its two-polarity certificates may have both nonempty color runs. The remaining proof problem is to derive similarly strong strip constraints from two distinct strict one-switch certificates at a common vertex, or to show that the defect-bearing joining squares cannot be compatible across multiple choices of dimension pairs.

#### Proposition 7 (the transverse strip identity for arbitrary face paths)

The curvature connection admits a formula without any monochromatic hypothesis. Let \(P=(v_0,\ldots,v_m)\) be any dimension-simple path contained in the \((n-2)\)-face \(F_{00}\), with edge dimensions \(d_1,\ldots,d_m\) and color word \(w_1,\ldots,w_m\). For either unused dimension \(h\in\{a,b\}\), put
\[
h_j=c(\{v_j,v_j\oplus e_h\}),\qquad
w_j^{(h)}=c(\{v_{j-1}\oplus e_h,v_j\oplus e_h\}),
\]
and let \(\kappa_j^{(h)}\) be the square curvature on the \(\{h,d_j\}\)-face joining the two corresponding edges. Then the following **pointwise strip equation** holds:
\[
\boxed{w_j^{(h)}=w_j+\kappa_j^{(h)}+h_{j-1}+h_j\pmod2.}
\tag{11}
\]
Its sum along the entire strip is
\[
\boxed{\sum_{j=1}^m\kappa_j^{(h)}
=\sum_{j=1}^m(w_j+w_j^{(h)})+h_0+h_m\pmod2.}
\tag{12}
\]

*Proof.* The four boundary edges of the \(j\)-th side square have respective bits \(w_j,w_j^{(h)},h_{j-1},h_j\), whose mod-two sum equals \(\kappa_j^{(h)}\). Solving for \(w_j^{(h)}\) gives (11). Summing (11) cancels every interior connecting-edge color \(h_j\) twice, giving (12). \(\square\)

Thus the **corrected transverse curvature word**
\[
\widehat W_j^{(h)}=\kappa_j^{(h)}+h_{j-1}+h_j
\tag{13}
\]
equals the xor \(w_j+w_j^{(h)}\) of the base and translated color words. The gate corridor from Theorem 5 forces every \(h_j=1\) along a red monochromatic \(P\), so \(\widehat W^{(h)}=\kappa^{(h)}=w^{(h)}\). This is why the earlier two-sided oscillation applies directly to ordinary curvature.

For a **strict one-switch** face certificate obtained only from Theorem 1's induction hypothesis, the transverse connecting-edge bits \(h_j\) need not be constant, and the base word \(w\) is not constant. Equation (11) shows the additional information that must be controlled to extend the oscillation theorem: ordinary curvature alone need not equal the translated color word. The required next statement would couple both one-switch face certificates at the common vertex to force compatible restrictions on the transverse connecting-edge profiles. This is an open step, not a consequence of the folding equivalence.

#### Adjacent face polarities force stripes and gates force empty roots

The two-polarity construction also couples certificates lying in different adjacent faces. This gives a stronger local condition than paired-root exclusion at a gate's neighboring corners.

Fix two omitted directions \(a,b\), put \(R=[n]\setminus\{a,b\}\), and identify each face \(F_{\alpha\beta}\) with \(Q_R\). Let \(g_{\alpha\beta}\) be its ordinary edge coloring. Antipodal oddness gives
\[
g_{11}(r)=1-g_{00}(\bar r),\qquad
g_{10}(r)=1-g_{01}(\bar r)
\]
on corresponding edges. Ordinary path reversal gives \(A_1(g)=\overline{A_0(g)}\). Consequently
\[
\boxed{
A_t(g_{00})=A_t(g_{11}),\qquad
A_t(g_{01})=A_t(g_{10})\quad(t=0,1).
}
\tag{CP1}
\]

Write \(p_0,p_1\) for the \(a\)-edge colors at \(b=0,1\), and \(q_0,q_1\) for the \(b\)-edge colors at \(a=0,1\), in the residual square over \(r\).

**Lemma (two-step certificate lift).** A full face path from \(r\) with word \(t^*(1-t)^*\), together with a color-\(t\) two-step diagonal route in the residual square from that face to its opposite face, gives a monochromatic color-\(t\) full geodesic of \(Q_n\).

*Proof.* Split the face order at its monotone seam. Reverse the first segment, traverse the two omitted directions along the diagonal route at \(r\), and follow the antipodally translated reversed second segment in the opposing face. The original first segment has color \(t\), and the translated second segment has color \(t\) by oddness. The directions of the two horizontal segments are disjoint and exhaust \(R\), and the middle route uses \(a,b\) once each. The endpoints are antipodal. \(\square\)

**Theorem (cross-profile stripe rigidity).** Suppose \(Q_n\) has no monochromatic full geodesic. If
\[
\boxed{r\in A_0(g_{01})\cap A_1(g_{00}),}
\tag{CP2}
\]
then its residual square is a stripe:
\[
\boxed{p_0=p_1,\qquad q_0=q_1,\qquad p_0\ne q_0.}
\tag{CP3}
\]
The same conclusion holds with the orientations reversed, or with any adjacent pair of faces.

*Proof.* The nondecreasing certificate in \(F_{01}\) excludes both color-zero diagonals from corner \(01\). The nonincreasing certificate in \(F_{00}\) excludes both color-one diagonals from corner \(00\). By the lifting lemma these give
\[
(p_1\lor q_1),\quad(q_0\lor p_0),\quad
(\neg p_0\lor\neg q_1),\quad
(\neg q_0\lor\neg p_1).
\tag{CP4}
\]
If \(p_0=0\), the second clause forces \(q_0=1\), the fourth forces \(p_1=0\), and the first forces \(q_1=1\). If \(p_0=1\), the third forces \(q_1=0\), the first forces \(p_1=1\), and the fourth forces \(q_0=0\). These are the two stripes. Reversing color and face roles proves the other cases. \(\square\)

For a coloring with a nonstripe residual square and certificates (CP2), one of the four forbidden monochromatic routes in (CP4) exists. The proof therefore constructs a full monochromatic path with \(a,b\) consecutive; the theorem does not rely on a dimension induction.

**Corollary (paired-to-empty propagation at a gate).** In a bad odd coloring, suppose \(r\in P(g_{00})\) and its joining square is a gate. Then
\[
\boxed{
r,\bar r\notin A_0(g_{01})\cup A_1(g_{01}).
}
\tag{CP5}
\]
The same conclusion holds for the other adjacent face \(g_{10}\).

*Proof.* A nondecreasing adjacent-face certificate would combine with the nonincreasing \(g_{00}\)-certificate to force a stripe. A nonincreasing adjacent certificate would combine with the nondecreasing \(g_{00}\)-certificate to do the same. A gate is not a stripe, so neither adjacent orientation exists. Reversal makes emptiness antipodally invariant; (CP1) handles the opposing adjacent face. \(\square\)

There is also a direct route interpretation: at a gate's adjacent corners, one diagonal route is monochromatic zero and the other monochromatic one. Either face orientation at that corner would therefore lift to a monochromatic full path. Thus the adjacent root is empty even without first supplying a paired certificate at the gate corner.

**Corollary (empty neighboring roots along a monochromatic face corridor).** Under Theorem 5, every vertex \(v_j\) of its monochromatic face geodesic is a root admitting neither monotone orientation in either adjacent translated face. The gate corridor supplies a monochromatic diagonal of each color from the adjacent face corner, and the lifting lemma excludes both orientations.

This strengthens the earlier statement that adjacent gate corners cannot be paired: they cannot support either full monotone orientation. Their rooted interaction structure must therefore evade the rootwise rooted-tree feedback coverage theorem.

##### A local odd-cycle certificate

For a full cube vertex \(x\), make a graph \(K_x\) on the direction set. Join \(a,b\) whenever, at the remaining-bit root of \(x\), the face through \(x\) and an adjacent parallel face have opposite full monotone certificates. By (CP1), toggling \(a\) or \(b\) gives the same adjacent-face profile, so this definition is symmetric in \(a,b\).

In a bad coloring, the stripe theorem forces
\[
\boxed{\{a,b\}\in E(K_x)\Longrightarrow c_a(x)\ne c_b(x).}
\tag{CP6}
\]
Hence \(K_x\) is bipartite, colored by the incident edge bits. Conversely, an odd cycle in some \(K_x\) supplies an edge whose incident bits agree, making its residual square a nonstripe; (CP4) then constructs a monochromatic full path. This is a local contradiction certificate. A proof that such a cycle must occur has not been obtained; full interleaving clauses remain part of the general completion problem.

**Independent reconstruction.** An unrelated evaluator constructed 1338 certificate lifts across two-step routes in odd cubes of dimensions four through six and directly checked their complete direction orders, edge colors, and antipodal endpoints. The stripe and gate statements follow from the four displayed Boolean clauses in every dimension.


**Corollary (antipodal empty-corridor bound).** Put \(m=n-2\ge1\). If a bad odd coloring has a monochromatic full geodesic in one \(m\)-face, then each adjacent parallel \(m\)-face coloring \(g\) satisfies
\[
\boxed{
|\{r:r\notin A_0(g)\cup A_1(g)\}|\ge2m,\qquad
|A_0(g)\cup A_1(g)|\le2^m-2m.
}
\tag{CP7}
\]
In particular \(|A_0(g)|\le2^m-2m\).

*Proof.* Every one of the \(m+1\) corridor vertices is empty by the gate propagation rule. The empty-root set is antipodally invariant. A dimension-simple full geodesic's vertex set intersects its antipodal translate only in its two endpoints: a proper nonempty direction prefix cannot equal the complement of another prefix. Their union therefore has \(2(m+1)-2=2m\) vertices. \(\square\)

Thus an adjacent fiber with every root admitting at least one orientation, including the rootwise rooted-tree feedback class, rules out such a monochromatic corridor in a bad coloring. The bound applies in every dimension and preserves the positions of all corridor roots; it supplies a quantitative constraint for coupling them to the critical repair witnesses.


### Single-root reachability realization and failure of convex antipodal separation

The prefix-carrier route in Article XIV, Subsections 38, 40, 42–43, works with rooted monochromatic geodesic cones \(K_x^a\) whose simplices retain the set of used cube dimensions. Under a hypothetical NORI1 counterexample, the red reachable dimension-set family \(\mathcal R_x\) is accessible, contains no complementary pair, and contains no two disjoint sets whose union omits only one dimension (Subsection 38). We prove these conditions have **no additional single-root realizability obstruction** and construct, in every dimension \(n\ge7\), legally realizable such cones whose convex hulls contain the cube center. Consequently the existing equivariant Alexander-dual carrier framework cannot be replaced by an ordinary affine hyperplane separation of each cone from its antipode.

Write \(D=[n]\) and identify each vertex with a dimension subset \(S\subseteq D\) relative to root \(0^n\). An accessible family \(R\subseteq2^D\) contains \(\varnothing\) and, for every nonempty \(S\in R\), has some \(i\in S\) with \(S\setminus\{i\}\in R\). Say that \(R\) is *complement- and near-complement-free* when
\[
\boxed{
S,T\in R,\quad S\cap T=\varnothing
\quad\Longrightarrow\quad |S\cup T|\le n-2.
}
\tag{1}
\]
This excludes both a complementary pair and a pair omitting only one dimension.

#### Theorem 1 (realization of every admissible accessible family at one root)

For every \(n\ge2\) and every accessible \(R\subseteq2^D\) satisfying (1), there exists an antipodally odd binary coloring of all undirected edges of \(Q_n\) for which the **full red-geodesic reachability family from \(0^n\) is \(R\)**.

*Proof.* Orient Boolean edges upwards in subset rank, \(S\to S\cup\{i\}\). Prescribe an edge **red** if both endpoints lie in \(R\). Prescribe an edge **blue** if its lower endpoint is in \(R\) and its upper endpoint is not in \(R\). Leave the other edges temporarily unassigned.

The antipode maps the increasing edge \(S\to S\cup\{i\}\) to the increasing edge
\[
(D\setminus(S\cup\{i\}))\longrightarrow D\setminus S.
\tag{2}
\]
Two prescribed red edges cannot be antipodal, since their upper endpoints would be complementary members of \(R\), violating (1). Two prescribed blue edges cannot be antipodal either: if both the original lower endpoint \(S\) and the opposing lower endpoint \(D\setminus(S\cup\{i\})\) belonged to \(R\), these would be disjoint members of \(R\) whose union has size \(n-1\), again violating (1). Thus every antipodal edge orbit contains at most one prescribed bit, or two prescribed *opposite* bits. Assign the complementary bit to any unassigned mate, and choose complementary bits freely on unused orbits. This extends the prescription to a legal antipodally odd coloring.

Every red geodesic starting at \(\varnothing\) increases subset rank and cannot exit \(R\), since all upward boundary edges from \(R\) were colored blue. Conversely accessibility provides a saturated chain from \(\varnothing\) to every \(S\in R\) with every intermediate set in \(R\). All its edges were colored red. Hence the red reachability family is \(R\), as asserted. \(\square\)

**Consequence.** Accessibility and the complementary/near-complementary exclusions are all that is required to realize an individual root's putative no-counterexample red reachability pattern in an antipodally odd coloring. This does not realize a global NORI1 counterexample: other roots in the resulting coloring may have a monochromatic full geodesic. Any contradiction must couple distinct roots or use more than the reachable sets of one root.

#### Theorem 2 (convex-hull obstruction in every dimension at least seven)

For every \(n\ge7\), a legal antipodally odd \(Q_n\) coloring exists with root \(x\) whose red prefix complex \(K_x^0\) has the following three properties:
\[
\boxed{
K_x^0\cap A K_x^0=\varnothing,\qquad
\operatorname{conv}(|K_x^0|)\ni(\tfrac12,\ldots,\tfrac12),\qquad
\operatorname{conv}(|A K_x^0|)\ni(\tfrac12,\ldots,\tfrac12).
}
\tag{3}
\]
The red reachability family at \(x\) excludes all complementary and near-complementary pairs. In particular, the two disjoint antipodal prefix cones cannot be separated by a strict affine hyperplane.

*Proof.* Begin in dimension seven. Write subsets as seven-bit strings, with dimensions ordered left to right. Define \(R_7\) to be the union of all prefixes of the following five increasing Boolean paths:
\[
\begin{array}{l}
0000000\to0000001,\\
0000000\to0010000\to0110000\to0110010\to0111010\to0111011,\\
0000000\to0000010\to0000110\to1000110,\\
0000000\to0010000\to0010100\to1010100,\\
0000000\to0100000\to0101000\to0101100\to1101100.
\end{array}
\tag{4}
\]
There are sixteen distinct vertices in \(R_7\). It is accessible by construction. Direct comparison of the sixteen strings gives
\[
S,T\in R_7,\quad S\cap T=\varnothing
\quad\Longrightarrow\quad |S\cup T|\le5.
\tag{5}
\]
For audit, condition (5) may be checked solely from the displayed union of chains by inspecting pairs of binary strings: no pair has disjoint supports covering six or seven positions.

Among these reachable vertices select five:
\[
\begin{array}{c|ccccc}
U&0000001&0111011&1000110&1010100&1101100\\
\text{weight }6\alpha_U&1&2&1&1&1.
\end{array}
\tag{6}
\]
For each of the seven dimensions, the weighted sum of its bits in (6) equals \(3/6=1/2\), so
\[
\boxed{
\sum_{U\text{ in }(6)}\alpha_U\mathbf1_U
=(\tfrac12,\ldots,\tfrac12).
}
\tag{7}
\]
Theorem 1 gives a legal antipodally odd coloring whose red geodesic reachability family from zero is \(R_7\). Hence the red prefix complex contains every listed vertex and its convex hull contains the center. The family is complement-free; both \(K_0^0\) and its antipodal image are subcomplexes of the same rooted Freudenthal triangulation, so their geometric intersection is empty because they have no common vertices. Antipodality fixes the center and preserves convex hulls, proving (3) for \(n=7\).

For \(n>7\), take the product family
\[
R_n=\{S\cup J:S\in R_7,\ J\subseteq\{8,\ldots,n\}\}.
\tag{8}
\]
It is accessible. If two members are disjoint and cover all but at most one of the \(n\) dimensions, their restrictions to the first seven dimensions are disjoint and cover at least six of those seven dimensions, contradicting (5). Thus (1) holds, so Theorem 1 realizes \(R_n\) as a red reachability family for a legal \(n\)-cube coloring. Finally
\[
\operatorname{conv}(R_n)=\operatorname{conv}(R_7)\times[0,1]^{n-7}
\]
contains the center, and the same antipodal-disjointness argument applies. \(\square\)

**Implication for the Wu–Yang modification.** The dimension-simple prefix-carrier complexes have much richer geometry than disjoint convex subsets. Even the full complement-avoidance and one-missing-dimension exclusion constraints, which hold at each root under a hypothetical NORI1 counterexample, do not force an affine linear separation of a carrier from its antipode. A proof cannot simply average reachable endpoints, subtract antipodal barycenters, and normalize to obtain the required low-dimensional odd map: that difference may vanish. The topological complement \(S^{n-1}\setminus(K_x^0\cup A K_x^0)\), its Alexander-dual sphere structure, and support-filtered transport retain information that ordinary convexification destroys. This is a method-specific obstruction, not a counterexample to NORI1; the constructed legal coloring is not asserted to lack full monochromatic geodesics at other roots.

### Boundary carriers: homotopy types and explicit filling classes

Let \(V=A\sqcup B\sqcup C\), where \(A,B,C\) are nonempty, and put
\[
p=|A|,\quad r=|B|,\quad q=|C|,\quad n=p+r+q\ge5,\qquad
W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}.
\]
For \(H\subseteq B\) and signs \(\sigma_h\in\{-1,1\}\), define
\[
\mathcal C(A,B,C;H,\sigma)=
\bigcup_{a\in A,\ c\in C}
\{z\in S(W):z_a=z_c=0,\ \sigma_hz_h\ge0\ (h\in H)\}.
\tag{1}
\]
These are the carriers used by the affine-dependence labels on Hamilton middle vertices. The sets \(A,C\) specify possible first and last vertices; \(B\) consists of vertices that are always middle vertices; \(H\) records their invariant colors.

#### A complete carrier classification

**Theorem 1.** Carrier (1) has the following homotopy type.
\[
\begin{array}{c|c}
\text{condition}&\text{homotopy type}\\ \hline
H=\varnothing&
\displaystyle\bigvee^{(2^p-1)(2^q-1)}S^{n-4}\\
\varnothing\ne H\subsetneq B&\text{contractible}\\
H=B\text{ and both signs occur}&\text{contractible}\\
H=B\text{ and all signs agree},\ p+q>2&S^{p+q-3}\\
H=B\text{ and all signs agree},\ p=q=1&\varnothing.
\end{array}
\tag{2}
\]
In particular, the uncolored boundary carrier is \((n-5)\)-connected.

*Proof of the contractible cases.* Choose \(h\in H\). If \(B\setminus H\ne\varnothing\), choose \(k\) in that set; otherwise choose \(k\in H\) with \(\sigma_k=-\sigma_h\). The vector
\[
v=\sigma_h(e_h-e_k)/\sqrt2
\]
lies in every member of the union (1). Its prescribed entry at \(h\) is strictly positive, so \(-v\) lies in none of them. Normalized interpolation toward \(v\) contracts each member and the union simultaneously. All sign inequalities and both required zero entries persist along this interpolation.

*Proof when \(H=\varnothing\).* Fix \(b_0\in B\), and eliminate \(z_{b_0}\) using the equation defining \(W\). This gives a linear isomorphism
\[
W\cong\mathbb R^A\oplus\mathbb R^C\oplus\mathbb R^{B\setminus\{b_0\}}.
\]
Under it, the cone over (1) becomes
\[
U_p\times U_q\times\mathbb R^{r-1},
\qquad U_t=\{u\in\mathbb R^t:\text{some entry of }u\text{ is zero}\}.
\tag{3}
\]
An invertible linear map induces a homeomorphism of links by radial normalization. The link of a product of cones is the join of their links.

For \(t\ge2\), radial projection in the \(\ell^1\) norm identifies the link of \(U_t\) with the \((t-2)\)-skeleton of the boundary of the \(t\)-crosspolytope. This skeleton is \((t-3)\)-connected, and its reduced integral homology is concentrated in degree \(t-2\), with rank \(2^t-1\). Indeed, the relative cellular chains of the sphere and its skeleton have \(2^t\) generators in degree \(t-1\), and the sphere's fundamental class maps to a rank-one subgroup. The long homology sequence gives the stated rank and vanishing. For \(t=2\) the link consists of four points; for \(t=3\) it is a connected graph. In higher dimensions, the Hurewicz and Whitehead theorems identify the link with a wedge of \(2^t-1\) spheres of dimension \(t-2\). For \(t=1\), the factor \(U_1=\{0\}\) contributes no nonzero direction and is omitted from the join.

The free factor in (3), when nonzero, contributes \(S^{r-2}\). Joining the two crosspolytope skeletons and this sphere gives the first row of (2); joining wedges of spheres multiplies their multiplicities and adds their dimensions plus the join increments. The resulting dimension is \(n-4\). The same computation covers factors of dimension zero by omission.

*Proof when all of \(B\) has one sign.* By negation assume that sign is positive. Cover (1) by the subsets specified by the pair of required zero entries \((a,c)\). An intersection is determined by nonempty sets \(A_0\subseteq A,C_0\subseteq C\) of entries forced to vanish. If \(A_0=A\) and \(C_0=C\), all remaining entries lie in \(B\), are nonnegative, and sum to zero; the spherical intersection is empty. Otherwise choose \(k\in(A\setminus A_0)\cup(C\setminus C_0)\) and \(h\in B\). Normalized interpolation to \((e_h-e_k)/\sqrt2\) contracts the intersection. The finite polyhedral nerve lemma therefore identifies the carrier with the simplicial complex on \(A\times C\) whose simplices omit at least one row or at least one column.

Cover this nerve by the full simplices obtained by omitting a given row or column, discarding empty members. Their intersections are again simplices, and are nonempty precisely when the set of omitted rows is a proper subset of \(A\) and the omitted columns form a proper subset of \(C\). Their nerve is
\[
\partial\Delta_A*\partial\Delta_C\cong S^{p+q-3},
\]
with the empty boundary factor omitted when its set has one element. If \(p=q=1\), the original carrier is empty. This proves the remaining rows. The closed polyhedral covers used here admit common triangulations, so the polyhedral form of the nerve lemma applies. \(\square\)

#### The complement is a complete bipartite graph

Write \(\mathcal C_0=\mathcal C(A,B,C;\varnothing,\varnothing)\), and let
\[
P_A=\{-1,1\}^A,\qquad P_C=\{-1,1\}^C.
\]

**Theorem 2.** There is an antipodally equivariant homotopy equivalence
\[
S(W)\setminus\mathcal C_0\simeq K_{P_A,P_C}=K_{2^p,2^q}.
\tag{4}
\]
The graph involution negates every sign in each of its two vertex classes.

*Proof.* A point lies outside \(\mathcal C_0\) precisely when every entry in \(A\) is nonzero or every entry in \(C\) is nonzero. Cover this complement by
\[
U_\alpha=\{z\in S(W):\operatorname{sgn}(z|_A)=\alpha\},
\qquad
T_\beta=\{z\in S(W):\operatorname{sgn}(z|_C)=\beta\}.
\]
Sets of the same kind with distinct sign vectors are disjoint. Every \(U_\alpha\cap T_\beta\) is nonempty: prescribe the signs and magnitudes on \(A\cup C\), and use an entry of the nonempty set \(B\) to make the total sum zero. Each set and each nonempty intersection is the spherical part of a convex cone with strict sign constraints. Choosing a point in the intersection and using normalized interpolation proves contractibility. The cover nerve is consequently the complete bipartite graph in (4).

Negation permutes the cover by \(\alpha\mapsto-\alpha,\beta\mapsto-\beta\). An invariant partition of unity and the equivariant good-cover construction give the equivariant equivalence. No graph vertex or edge is fixed by this involution. \(\square\)

For a finite set \(P\), let
\[
I_P=\ker\bigl(\mathbb Z^P\xrightarrow{\sum}\mathbb Z\bigr).
\]
Orient every graph edge from \(P_A\) to \(P_C\). A graph one-chain is an integer matrix \((t_{\alpha\beta})\); it is a cycle precisely when every row and every column sum is zero. Thus
\[
H_1(K_{P_A,P_C};\mathbb Z)=I_{P_A}\otimes I_{P_C}.
\tag{5}
\]
Choose \(\alpha_0\in P_A,\beta_0\in P_C\). A basis consists of the rectangle cycles
\[
R_{\alpha\beta}
=E_{\alpha\beta}-E_{\alpha\beta_0}
-E_{\alpha_0\beta}+E_{\alpha_0\beta_0},
\qquad \alpha\ne\alpha_0,\ \beta\ne\beta_0.
\tag{6}
\]
Alexander duality gives
\[
\widetilde H^{n-4}(\mathcal C_0;\mathbb Z)
\cong H_1(S(W)\setminus\mathcal C_0;\mathbb Z)
\cong I_{P_A}\otimes I_{P_C}.
\tag{7}
\]
The carrier is a finite polyhedral complex, so the compactness and local contractibility hypotheses of duality hold. Over \(\mathbb F_2\), this identification commutes with antipodality. Over the integers, naturality includes the ambient orientation sign \((-1)^{n-1}\). The duality used is the ordinary Alexander duality theorem, for example Hatcher, *Algebraic Topology*, Corollary 3.45, https://pi.math.cornell.edu/~Hatcher/AT/ATch3.pdf.

#### Filling classes on full Hamilton residues

A closed dual type-A cell is specified by an ordered partition of \(V\) into consecutive nonempty blocks. Its flags independently permute the entries within each block. If the first and last blocks are \(A,C\), all other vertices form \(B\). The invariant middle-vertex colors give \(H,\sigma\), and the affine-dependence vertex labels lie in carrier (1). Passing to a face shrinks the endpoint sets and adds invariant middle-vertex constraints, so the corresponding carriers are nested.

**Proposition 3 (forced variation in a middle block).** If an interior position block has at least three vertices, none of its vertices belongs to \(H\). In particular, for a primary \((n-3)\)-cell with its three blocks \(A|B|C\), if \(|B|\ge3\), then \(H=\varnothing\).

*Proof.* For a specified \(h\) in such a block, choose distinct \(u,v\) in the same block. Two permissible internal orders contain the consecutive words \(u,h,v\) and \(v,h,u\). Their triples centered at \(h\) have complementary colors by reversal oddness. Thus \(h\)'s color is not invariant. A primary cell has three blocks because a residue with \(k\) blocks has dimension \(n-k\). \(\square\)

Let \(D\) be a primary cell with \(H=\varnothing\), and suppose a color-sensitive boundary assignment has already given
\[
f:\partial D\cong S^{n-4}\longrightarrow\mathcal C_0.
\tag{8}
\]
Let \(\xi_{\alpha\beta}\) be the cohomology classes corresponding to the rectangle basis (6) under (7).

**Corollary 4 (complete integral and chain filling tests).** For \(n\ge7\), map (8) extends continuously over \(D\) inside \(\mathcal C_0\) if and only if
\[
\left\langle f^*\xi_{\alpha\beta},[\,\partial D\,]\right\rangle=0
\quad\text{for every }\alpha\ne\alpha_0,\ \beta\ne\beta_0.
\tag{9}
\]
With coefficients in \(\mathbb F_2\), the corresponding vanishing conditions are necessary and sufficient for the image of the fundamental boundary cycle to bound a chain in \(\mathcal C_0\).

*Proof.* By Theorem 1 the carrier is \((n-5)\)-connected and homotopy equivalent to a wedge of \((n-4)\)-spheres. Hurewicz identifies \(\pi_{n-4}(\mathcal C_0)\) with \(H_{n-4}(\mathcal C_0;\mathbb Z)\). Consequently \(f\) is nullhomotopic precisely when its fundamental homology class vanishes. The integral cohomology basis in (7) detects this class, giving (9). A nullhomotopy is equivalent to a disk extension. Over \(\mathbb F_2\), a cycle bounds precisely when its homology class vanishes, and the reduced cohomology basis detects that class. Modulo-two vanishing alone does not imply continuous extendibility. \(\square\)

These tests apply to complete Hamilton residues in the unrestricted boundary class. They specify the color-sensitive cancellation problem by finitely many endpoint-sign rectangles. The labels on individual flags do not determine the boundary assignment (8); coherent choices over shared faces remain necessary.

The contractibility criterion in Theorem 1 is a statement about each carrier. Its condition need not be inherited by cell faces: an unconstrained middle vertex can acquire the same invariant sign as the other middle vertices. Therefore the new contractible cases may fill a cell when its prescribed boundary lies in that carrier, but do not by themselves enlarge the previously constructed global equivariant map. Likewise, a general extension into the larger sparse target need not remain inside \(\mathcal C_0\).

The affine-dependence label is common to the cube and boundary constructions. Its boundary placement identifies the higher filling groups and their complete bipartite complement. The following results determine the antipodally invariant part of those groups and its canonical chain-tower class.


#### Antipodal norm classes and rectangles with opposite signs

Continue with \(\mathcal C_0\), and assume \(n\ge7\). Put \(d=n-4\), let \(Rz=-z\), and use coefficients in \(\mathbb F_2\) throughout this part. The induced involution on chains, homology and cohomology is also denoted \(R\); write \(N=1+R\). For a vector space \(M\) with involution, its quotient of invariant vectors by norm vectors is
\[
T(M)=\ker(N:M\to M)/\operatorname{im}(N:M\to M).
\tag{10}
\]
Since \(N^2=0\), the quotient is defined.

For \(\alpha\in P_A,\beta\in P_C\), let
\[
Q_{\alpha\beta}=
E_{\alpha\beta}+E_{-\alpha,\beta}
+E_{-\alpha,-\beta}+E_{\alpha,-\beta}
\tag{11}
\]
be the rectangle joining a sign pattern to its opposite in both graph parts. Denote its Alexander-dual class in \(H^d(\mathcal C_0;\mathbb F_2)\) by \(\xi_{\alpha\beta}\). Unlike the previously chosen rectangle basis, (11) is invariant under the graph involution. Modulo two, Alexander duality is equivariant, so \(R\xi_{\alpha\beta}=\xi_{\alpha\beta}\).

**Theorem 5 (one invariant class modulo norms).** The two vector spaces
\[
T\bigl(H^d(\mathcal C_0;\mathbb F_2)\bigr),
\qquad
T\bigl(H_d(\mathcal C_0;\mathbb F_2)\bigr)
\tag{12}
\]
have dimension one. Every class \(\xi_{\alpha\beta}\) from (11) represents the same nonzero element of the first space. Thus, among invariant top cohomology classes, there is one independent class after norm classes are removed.

*Proof.* For a finite set \(P\) with a fixed-point-free involution, let
\[
I_P=\ker\bigl(\mathbb F_2^P\xrightarrow{\sum}\mathbb F_2\bigr).
\]
Choose one representative \(a_j\) of each orbit, with \(a_0\) distinguished. In \(I_P\), the vector
\[
v_0=e_{a_0}+e_{Ra_0}
\]
is invariant. For every other orbit, put \(x_j=e_{a_j}+e_{a_0}\). The vectors
\[
v_0,\quad x_j,\quad Rx_j\quad(j\ne0)
\]
form a basis: entries at \(a_j,Ra_j\) give independence, and their number is \(|P|-1\). Consequently
\[
I_P\cong\mathbb F_2\oplus
\mathbb F_2[\mathbb Z_2]^{\,|P|/2-1}
\tag{13}
\]
as an involution module.

The cohomology module of the carrier is \(I_{P_A}\otimes I_{P_C}\), with the diagonal involution, by (7). A tensor product having one regular summand is regular; the tensor product of two regular two-dimensional summands is the direct sum of two regular summands, as seen by the two orbits of its four basis tensors. Hence this module has one trivial summand, generated by
\[
(e_\alpha+e_{-\alpha})\otimes(e_\beta+e_{-\beta}),
\tag{14}
\]
and all remaining summands are regular. A regular summand has equal invariant and norm subspaces, whereas the one-dimensional trivial summand has zero norm map. This proves the first dimension assertion and nonvanishing of (14).

Replacing \(\alpha\) by \(\alpha'\) changes its first factor by
\(N(e_\alpha+e_{\alpha'})\), where \(e_\alpha+e_{\alpha'}\in I_{P_A}\). Tensoring with the invariant second factor turns this change into a norm for the diagonal action. The same holds for \(\beta\). Formula (14) corresponds to (11), proving independence of the representatives. The homology module is dual to this finite-dimensional cohomology module. Duals of trivial and regular summands have the same types, giving the second dimension assertion. \(\square\)

#### A fixed odd pairing on every antipodal sphere map

**Theorem 6 (the opposite-sign rectangle has unit parity).** For every odd continuous map
\[
f:S^d\longrightarrow\mathcal C_0,
\qquad f(-x)=-f(x),
\]
one has
\[
\boxed{\langle f^*\xi_{\alpha\beta},[S^d]\rangle=1}
\quad\text{for every }\alpha\in P_A,\ \beta\in P_C.
\tag{15}
\]

*Proof.* Choose \(a\in A,c\in C\), and consider the invariant sphere
\[
L=\{z\in S(W):z_a=z_c=0\}\cong S^d
\subseteq\mathcal C_0.
\tag{16}
\]
First compute the pairing for its inclusion \(i\). The complement of \(L\) has a four-sector good cover recording the sign of \(z_a\) or \(z_c\); its nerve is \(K_{2,2}\cong S^1\). The inclusion
\(S(W)\setminus\mathcal C_0\hookrightarrow S(W)\setminus L\)
induces the graph map
\[
P_A\ni\alpha\longmapsto\alpha_a,\qquad
P_C\ni\beta\longmapsto\beta_c.
\]
This follows directly from the sign-sector covers used in Theorem 2. It takes (11) to the four-edge fundamental cycle of \(K_{2,2}\). Naturality of Alexander duality therefore gives
\[
\langle i^*\xi_{\alpha\beta},[L]\rangle=1.
\tag{17}
\]

By Theorem 1, \(\mathcal C_0\) is \((d-1)\)-connected. The restrictions of \(f\) and \(i\) to an antipodal equatorial \(S^{d-1}\) are consequently equivariantly homotopic: construct a homotopy over a free cellular decomposition, extending through cells using the vanishing of homotopy groups through degree \(d-1\). The equivariant homotopy extension property allows us to modify \(f\) equivariantly so that it agrees with \(i\) on that equator.

Glue the two upper-hemisphere maps along their common boundary. They determine a class \(h\in H_d(\mathcal C_0;\mathbb F_2)\). The corresponding lower-hemisphere difference is \(Rh\). Thus
\[
f_*[S^d]+i_*[S^d]=Nh.
\tag{18}
\]
Since \(\xi_{\alpha\beta}\) is invariant, it pairs trivially with \(Nh\). Equations (17)--(18) yield (15). \(\square\)

This fixes the antipodal parity without selecting arbitrary lower-dimensional fillings. It does not reduce the integral single-cell tests (9) to one test: those tests concern ordinary disk fillings. The one-dimensional quotient (12) describes the invariant part that survives changes by antipodal norms.

#### The final equation of a carrier chain tower

An antipodal chain tower of height \(d\) in \(\mathcal C_0\) consists of mod-two chains \(z_j\), \(0\le j\le d\), satisfying
\[
\varepsilon z_0=1,\qquad
\partial z_j=Nz_{j-1}\quad(1\le j\le d).
\tag{19}
\]
Use a finite invariant triangulation of the carrier. The sphere (16) supplies such a tower, for example by the fundamental chains of successive antipodal hemispheres in that sphere.

**Theorem 7 (a canonical final tower obstruction).** For every tower (19), the cycle \(Nz_d\) defines a class
\[
\Theta(\mathcal C_0)=[Nz_d]\pmod{N H_d(\mathcal C_0;\mathbb F_2)}
\in T\bigl(H_d(\mathcal C_0;\mathbb F_2)\bigr).
\tag{20}
\]
This class is independent of every chain choice in the tower, is the nonzero element of the one-dimensional space in (12), and satisfies
\[
\boxed{\langle\xi_{\alpha\beta},[Nz_d]\rangle=1.}
\tag{21}
\]
In particular, no choice of a height-\(d\) tower can be extended through degree \(d+1\).

*Proof.* The chain \(Nz_d\) is invariant and
\[
\partial Nz_d=N\partial z_d=N^2z_{d-1}=0.
\]
Take two towers \(z,z'\), and write \(\delta z_j=z_j+z'_j\). Since their zero-chains have the same odd augmentation and the carrier is connected, choose \(a_1\) with \(\partial a_1=\delta z_0\), and put \(a_0=0\). Inductively choose \(a_{j+1}\), for \(j<d\), with
\[
\delta z_j=\partial a_{j+1}+Na_j.
\tag{22}
\]
The chain \(\delta z_j+Na_j\) is a cycle, since its boundary is
\(N\delta z_{j-1}+N\partial a_j=0\) by the preceding instance of (22). Its class vanishes by the reduced homology vanishing through degree \(d-1\), proving the inductive choice.

At degree \(d\), the chain \(\eta=\delta z_d+Na_d\) is a cycle. Therefore
\[
N\delta z_d=N\eta,
\]
so the two classes in (20) differ by a norm homology class. This proves independence.

For the tower carried by (16), \(Nz_d\) is its fundamental sphere cycle. Equation (17) gives pairing one with every \(\xi_{\alpha\beta}\). Those invariant cohomology classes pair trivially with norms of homology classes, so independence yields (21) for every tower. Thus (20) is nonzero and, by Theorem 5, generates the quotient. A degree-\((d+1)\) chain whose boundary is \(Nz_d\) would make all the pairings zero, contradicting (21). \(\square\)

Theorem 7 gives an explicit higher-dimensional counterpart of the canonical second-stage obstruction in the Smith-transfer analysis: here the lower homology vanishes, every lower chain choice can be absorbed, and the surviving class is detected by the four-edge rectangle (11).


#### Compatibility under changes of endpoint sets

Let \(A'\subseteq A,C'\subseteq C\) be nonempty, and put
\(B'=V\setminus(A'\cup C')\). The uncolored carriers have a natural invariant inclusion
\[
j:\mathcal C_0(A',B',C')\hookrightarrow\mathcal C_0(A,B,C).
\tag{23}
\]

**Theorem 8 (natural transport of the invariant class).** Under the cohomology identifications (7), the restriction \(j^*\) is induced by restricting endpoint sign patterns:
\[
\alpha\longmapsto\alpha|_{A'},\qquad
\beta\longmapsto\beta|_{C'}.
\tag{24}
\]
More explicitly, a cycle matrix is sent to the matrix obtained by summing its entries over fibers of these two restriction maps. In particular,
\[
j^*\xi_{\alpha\beta}
=\xi_{\alpha|_{A'},\,\beta|_{C'}}.
\tag{25}
\]
The maps on both top homology and top cohomology induce isomorphisms of the one-dimensional invariant quotients (12), and
\[
j_*\Theta\bigl(\mathcal C_0(A',B',C')\bigr)
=\Theta\bigl(\mathcal C_0(A,B,C)\bigr).
\tag{26}
\]

*Proof.* Requiring a zero entry in \(A'\) and in \(C'\) implies the corresponding requirements in \(A,C\), proving (23). Its complementary inclusion goes from the complement of the larger carrier to the complement of the smaller one. The sign-sector cover of the former refines that of the latter by (24). The induced nerve map is the complete bipartite graph map given by restriction of signs. Its map on one-chains sums cycle-matrix entries over the indicated fibers; all row and column sums remain zero.

Naturality of Alexander duality identifies that graph map with \(j^*\). Restriction on a nonempty set commutes with sign negation and keeps a sign pattern distinct from its negative. Thus (11) maps to the corresponding four-edge rectangle without collapse, giving (25). It induces a nonzero map, hence an isomorphism, between the one-dimensional cohomology quotients of Theorem 5.

The evaluation pairing between homology and cohomology descends to a perfect pairing on the invariant quotients. This can be checked on the module decomposition in Theorem 5: regular summands have zero quotient, and the remaining trivial summands pair perfectly. Naturality of evaluation and the cohomology isomorphism therefore give the homology isomorphism. Finally, (21) characterizes the nonzero homology quotient class by its pairing with the opposite-sign rectangle. Equations (21) and (25) yield (26). \(\square\)

**Corollary 9 (transport along endpoint rook moves).** For distinct \(a,c\in V\), let \(L_{a,c}\) be the sphere defined in (16). The nonzero invariant quotient classes of all these spheres, and of all uncolored carriers (1), are canonically identified through carrier inclusions. Changing either endpoint to a third vertex preserves the identified class; swapping the endpoint roles also preserves it. The resulting identification is independent of the chosen sequence of such changes.

*Proof.* If \(a'\notin\{a,c\}\), both \(L_{a,c}\) and \(L_{a',c}\) are subspaces of
\[
\mathcal C_0(\{a,a'\},\,V\setminus\{a,a',c\},\,\{c\}).
\]
Each inclusion induces an isomorphism by Theorem 8, giving the identification for a change of first endpoint. The analogous carrier handles changes of the last endpoint. Swapping \(A,C\) leaves the carrier unchanged and interchanges the two graph parts; modulo two this preserves (11). The graph of ordered distinct endpoint pairs under changes of one entry is connected: an unused third vertex permits exchanging the endpoint roles, and changing entries successively connects arbitrary pairs. Every general carrier contains \(L_{a,c}\) for \(a\in A,c\in C\). All the quotient spaces have dimension one over \(\mathbb F_2\), with the distinguished nonzero classes specified by Theorems 5 and 7. Every inclusion preserves these classes, and the only automorphism of such a one-dimensional space is the identity. Hence identifications along different walks agree. \(\square\)

The transport in Theorem 8 concerns the uncolored endpoint-zero conditions. A colored face carrier may have extra invariant-sign constraints and a different homotopy type, as shown in (2). No assertion that its homology quotient is the same is needed or made. Thus the theorem resolves transport of the distinguished class across the raw endpoint carriers while leaving the color-sensitive shared-face chains as a separate proof obligation.

For a primary Hamilton residue \(A|B|C\) and its reversed residue \(C|B|A\), the carrier \(\mathcal C_0\) is the same on both sides and opposition acts by negation. This provides the native setting for paired-face corrections. However, the two residues alone do not form the antipodal sphere required in Theorem 6; their shared-face assignments and their attachments to other residues still have to be constructed. The results identify the forced invariant class once an antipodal sphere or tower is carried by this common target. They do not assert that the coloring already supplies that sphere or tower, or that carriers for different endpoint partitions can be identified.

The next results incorporate fixed colors into this transport and identify the resulting relative classes.


#### Opposed fixed-color carriers

Assume \(n\ge7\). Fix a nonempty \(H\subseteq B\), signs \(\sigma\), and write \(h=|H|\), \(d=n-4\). The carrier belonging to an opposed pair of Hamilton residues is
\[
U(H,\sigma)=
\mathcal C(A,B,C;H,\sigma)
\cup\mathcal C(A,B,C;H,-\sigma).
\tag{27}
\]
It is antipodally invariant. Its points have all their signed entries
\(\sigma_h z_h\), \(h\in H\), nonnegative, or all nonpositive. The intersection of the two pieces has every entry of \(H\) zero.

**Theorem 10 (homotopy type after paired color constraints).** Put \(M=(2^p-1)(2^q-1)\). The homotopy types are
\[
\begin{array}{c|c}
\text{condition}&U(H,\sigma)\\ \hline
H\subsetneq B&
\displaystyle\bigvee^{M}S^{n-h-3}\\
H=B,\ \sigma\text{ constant},\ p+q\ge3&
\displaystyle\bigvee^{M}S^{p+q-3}\\
H=B,\ \sigma\text{ constant},\ p=q=1&\varnothing\\
H=B,\ \sigma\text{ mixed},\ p+q\ge3&
\displaystyle\bigvee^{M-2}S^{p+q-3}\\
H=B,\ \sigma\text{ mixed},\ p=q=1&S^0.
\end{array}
\tag{28}
\]
A wedge of \(M\) zero-spheres denotes \(M+1\) points.

*Proof when \(H\subsetneq B\).* Choose \(b_0\in B\setminus H\). Define a linear projection \(P:W\to W\) by putting
\[
\lambda(z)=\frac1h\sum_{j\in H}\sigma_j z_j,\qquad
(Pz)_j=\lambda(z)\sigma_j\quad(j\in H),
\]
\[
(Pz)_{b_0}=z_{b_0}
+\sum_{j\in H}\bigl(z_j-\lambda(z)\sigma_j\bigr),
\tag{29}
\]
and retaining every other entry. This preserves the total sum and every entry in \(A\cup C\). On either of the two sign cones in (27), interpolation from \(z\) to \(Pz\) retains the same sign inequalities. If an entry of \(H\) is nonzero, \(\lambda\) has the strict sign of that cone, so no interpolation vector is zero. If every entry of \(H\) is zero, \(Pz=z\). Radial normalization therefore gives an odd strong deformation retraction onto the subspace where the \(H\)-entries are proportional to \(\sigma\).

After eliminating \(b_0\), the cone over this retracted space has the form
\[
U_p\times U_q\times\mathbb R^{\,|B\setminus H|},
\]
where \(U_p,U_q\) are the unions of entry hyperplanes in (3). Its link is an uncolored carrier with effective middle-set size \(|B\setminus H|+1\). The cone-link computation in Theorem 1 gives the first row of (28), including its zero-dimensional instances.

*Proof when \(H=B\) and \(\sigma\) is constant.* Negation of the common sign does not change (27). All entries of \(B\) are therefore either nonnegative or nonpositive. Choose \(b_0\in B\), replace its entry by \(\sum_{j\in B}z_j\), and replace the other \(B\)-entries by zero. This is a sum-preserving linear projection. The same normalized interpolation gives an odd strong deformation retraction onto the uncolored carrier with one middle entry. Its cone is \(U_p\times U_q\), giving the second row. If \(p=q=1\), the two endpoint entries must both vanish, and the same-sign middle entries sum to zero; the carrier is empty.

*Proof when \(H=B\) and \(\sigma\) is mixed.* Both constituent carriers are contractible by Theorem 1. Their intersection is
\[
J_{A,C}=\{z\in S(W_{A\cup C}):
\text{some entry in }A\text{ and some entry in }C\text{ vanish}\},
\]
where \(W_{A\cup C}\) imposes total sum zero. Since the inclusions are polyhedral cofibrations, their union is homotopy equivalent to the suspension of \(J_{A,C}\) when that intersection is nonempty; if it is empty, the union has two contractible components.

For \(p+q\ge4\), compute the reduced cohomology of \(J_{A,C}\) by Alexander duality in \(S(W_{A\cup C})\cong S^{p+q-2}\). Its complement has the sign-sector cover of Theorem 2, except that there is no unused entry to compensate the total sum. A sector pair is feasible precisely when its combined signs include a positive and a negative entry. Thus the nerve is
\[
G=K_{2^p,2^q}\setminus
\{E_{+,+},E_{-,-}\}.
\tag{30}
\]
Here \(+\) and \(-\) mean constant sign patterns in the respective sets. Every feasible intersection is contractible by normalized interpolation. The graph is connected for \(p+q\ge3\) and has cycle rank \(M-2\). Duality gives reduced integral homology of \(J_{A,C}\), concentrated in degree \(p+q-4\), free of rank \(M-2\). The homology assertion follows also from the cohomology form of duality and the universal coefficient theorem, since the finite complex has no other cohomology or torsion.

If \(p+q=4\), the intersection consists of \(M-1\) points, and its suspension is a wedge of \(M-2\) circles. If \(p+q\ge5\), the intersection is connected; its suspension is simply connected and has reduced homology only in degree \(p+q-3\). Hurewicz and Whitehead identify that suspension with the stated wedge of spheres. For \(p+q\le3\), the intersection is empty. The union then has the homotopy type \(S^0\), agreeing with the remaining rows of (28). \(\square\)

**Theorem 11 (index and the two-sign vanishing threshold).** Every nonempty space in (28) admits an odd map to \(S^m\) and contains an odd embedded \(S^m\), where
\[
m=
\begin{cases}
n-h-3,&H\subsetneq B,\\
p+q-3,&H=B,\ \sigma\text{ constant},\ p+q\ge3,\\
\max(0,p+q-3),&H=B,\ \sigma\text{ mixed}.
\end{cases}
\tag{31}
\]
Its least possible odd-sphere target dimension is therefore \(m\), and its covering class has nonzero \(m\)-th power and zero \((m+1)\)-st power.

For \(h=1\), one has \(U(H,\sigma)=\mathcal C_0\). For \(h\ge2\), the opposite-sign rectangle class satisfies
\[
\boxed{\xi_{\alpha\beta}|_{U(H,\sigma)}=0
\quad\text{in }H^d(U(H,\sigma);\mathbb F_2).}
\tag{32}
\]

*Proof.* In the first two cases, the odd deformation retractions above land in effective uncolored carriers of dimension \(m\). Their invariant polyhedral structures admit odd maps to \(S^m\): assign to a face of dimension \(j\) an arbitrarily chosen sign times the \((j+1)\)-st crosspolytope vertex, with opposite signs on opposite faces, and extend over the barycentric subdivision. Distinct faces in a chain have distinct dimensions. Setting one specified \(A\)-entry and one specified \(C\)-entry to zero in the effective ambient subspace gives an odd embedded \(S^m\).

In the mixed case with \(p+q\ge4\), the intersection \(J_{A,C}\) has an invariant cell structure of dimension \(m-1\), hence an odd map to \(S^{m-1}\) by the same face-dimension labeling. Extend this map over the positive-sign carrier into the contractible upper hemisphere of \(S^m\). Extend over its opposite by negation. The prescriptions agree on the intersection, giving an odd map on the union. When the intersection is empty, mapping the two pieces to opposite points gives an odd map to \(S^0\).

For the matching embedded sphere, choose a nonzero vector \(v\) supported in \(B\), with total sum zero and strict signs \(\sigma\); such a vector exists since both signs occur. For fixed \(a\in A,c\in C\), the subspace
\[
\{z\in\mathbb R^{A\cup C}:
\sum z_j=0,\ z_a=z_c=0\}\oplus\mathbb Rv
\]
has its unit sphere inside (27). Its dimension is \(m\) when \(p+q\ge3\); when \(p=q=1\), the two points \(\pm v/\|v\|\) give \(S^0\). The embedded antipodal sphere supplies the lower bound on the covering power; the odd map supplies the upper bound.

A single real entry always has one of its two weak signs, proving \(U(H,\sigma)=\mathcal C_0\) when \(h=1\). For \(h\ge2\), every nonempty row of (28) has homotopy dimension at most \(d-1\), because \(n\ge7\). Thus \(H^d(U;\mathbb F_2)=0\), proving (32). The empty case gives the same vanishing. \(\square\)

#### Two fixed signs transgress the rectangle class

The vanishing in (32) has a distinction at \(h=2\): the absolute rectangle class has relative lifts, but none of those lifts is antipodally invariant.

**Theorem 12 (the relative norm extension at two signs).** Suppose \(h=2\), set \(U=U(H,\sigma)\), and use mod-two coefficients. There is an equivariant sequence with each kernel equal to the preceding image
\[
0\longrightarrow H^{d-1}(U)
\xrightarrow{\delta}H^d(\mathcal C_0,U)
\xrightarrow{\rho}H^d(\mathcal C_0)
\longrightarrow0.
\tag{33}
\]
The module \(H^d(\mathcal C_0,U)\) is a direct sum of regular involution modules. Its regular rank is \(M\), except when \(H=B\) and \(\sigma\) is mixed, when its regular rank is \(M-1\). In particular its invariant quotient modulo norms is zero.

For every opposite-sign rectangle class \(\xi=\xi_{\alpha\beta}\), and every lift \(\widetilde\xi\) through \(\rho\), define
\[
\kappa(\xi)=
\delta^{-1}(N\widetilde\xi)
\pmod{N H^{d-1}(U)}.
\tag{34}
\]
This is well-defined, independent of the lift and of \(\alpha,\beta\), and generates
\[
T(H^{d-1}(U))\cong\mathbb F_2.
\tag{35}
\]
Consequently \(\xi\) has no invariant relative lift.

*Proof.* The carrier \(\mathcal C_0\) has zero degree-\((d-1)\) cohomology. Theorem 10 gives zero degree-\(d\) cohomology for \(U\). The cohomology sequence of the pair yields (33).

We first show that no invariant lift of \(\xi\) exists. Restrict the pair to the invariant sphere \(L_{a,c}\cong S^d\) of (16). The two linear entries specified by \(H\) are independent on its ambient subspace: at least one other entry remains available to enforce total sum zero. After a linear change of variables and radial normalization,
\[
L_{a,c}\cap U=\{x\in S^d:x_1x_2\ge0\},
\]
where multiplying the two entries by their prescribed signs is included in the change of variables. Its complement has two open spherical sectors, each an open \(d\)-ball, exchanged by antipodality. Collapsing the intersection gives a wedge of two \(d\)-spheres with those spheres exchanged. Therefore the relative group
\[
H^d(L_{a,c},L_{a,c}\cap U)
\]
is a regular two-dimensional module; its map to \(H^d(L_{a,c})\cong\mathbb F_2\) sums the two entries. Every invariant vector has zero image. But Theorem 6 gives \(\xi|_{L_{a,c}}\ne0\). Naturality of relative restriction therefore rules out an invariant lift in (33).

For the first two cases of (28) at \(h=2\), the equivariant projection identifies \(H^{d-1}(U)\) with the top cohomology of an effective uncolored carrier. Its module has one trivial summand and regular remaining summands, by the proof of Theorem 5. In the mixed case \(H=B\), Mayer–Vietoris identifies it equivariantly, modulo two, with the top cohomology of \(J_{A,C}\), and duality identifies that group with \(H_1(G;\mathbb F_2)\) for the graph (30).

For completeness, the first homology of any connected free involution graph has one trivial summand and regular remaining summands. Its augmented cellular chain sequence
\[
0\to H_1(G)\to C_1(G)\to C_0(G)\to\mathbb F_2\to0
\]
has regular middle modules. Applying the two-periodic complex with differential \(N\) to its two short sequences identifies \(T(H_1(G))\) with \(T(\mathbb F_2)\cong\mathbb F_2\), since regular modules have zero \(N\)-homology. Every finite involution module in characteristic two splits into trivial blocks and regular blocks, by the Jordan form of \(N\), where \(N^2=0\). Thus there is one trivial block. This proves (35) in all cases.

Since \(\xi\) is invariant, \(N\widetilde\xi\) belongs to \(\ker\rho=\operatorname{im}\delta\). Its preimage is invariant because \(\delta\) is injective. Changing the lift by \(\delta a\) changes that preimage by \(Na\), so (34) is independent of the lift. If (34) were zero, changing the lift by such a \(\delta a\) would make it invariant, contrary to the restriction argument. Thus it generates (35). Changing \(\xi\) by a norm \(Nb\) changes a lift by \(N\widetilde b\), whose norm is zero. Theorem 5 therefore makes (34) independent of the rectangle representatives.

Finally write the left and right modules of (33) as a trivial summand plus regular summands. A regular summand in the quotient can be lifted as a regular pair \(x,Nx\), splitting it off. For the remaining trivial quotient, choose its lift \(u\). The nonzero class (34) allows a change of \(u\) by an element of the kernel so that \(Nu\) is its distinguished trivial generator. These two vectors form one regular summand, and the remaining kernel summands are regular. Thus the middle module is entirely regular. Its dimension is \(2M\) in the first two cases of (28) and \(2M-2\) in the mixed case, giving the asserted ranks. \(\square\)

This is a color-sensitive transgression: two fixed middle signs annihilate the absolute top class on the paired carrier, while its relative lift acquires the nonzero degree-\((d-1)\) norm obstruction (34). Selecting opposite fillings independently cannot remove this class.

#### Three fixed signs give natural relative lifts

**Theorem 13 (unique relative transport with at least three signs).** If \(h\ge3\), then
\[
\boxed{H^d(\mathcal C_0,U(H,\sigma))
\xrightarrow{\ \rho\ }H^d(\mathcal C_0)}
\tag{36}
\]
is an equivariant isomorphism. Each opposite-sign rectangle class has a unique relative lift, which is invariant and represents the nonzero invariant quotient modulo norms.

These lifts commute with shared-face inclusions. More precisely, suppose
\(A'\subseteq A,C'\subseteq C\), \(H\subseteq H'\subseteq B'\), the signs agree on \(H\), and both \(h,|H'|\ge3\). Then the carrier inclusion from Theorem 8 is an inclusion of pairs, and its relative pullback sends the unique lift of \(\xi_{\alpha\beta}\) to the unique lift of
\(\xi_{\alpha|_{A'},\,\beta|_{C'}}\).

*Proof.* By (28), \(U(H,\sigma)\) has zero cohomology in degrees \(d-1,d\) when \(h\ge3\), including the empty and zero-dimensional cases. The sequence of the pair gives (36). Equivariance and uniqueness make the lift invariant and identify its invariant quotient with that in Theorem 5.

Stronger endpoint-zero conditions and stronger consistent sign constraints give
\[
U(H',\sigma')\subseteq U(H,\sigma)
\]
under the inclusion of the raw carriers. Thus there is a map of pairs. The ordinary and relative restriction maps commute. Theorem 8 identifies the absolute class after restriction, and the isomorphism (36) on the smaller carrier identifies its relative lift uniquely. \(\square\)

For Hamilton residues these hypotheses come directly from face incidence: possible endpoint sets shrink, invariant middle-vertex sets grow, and their signs persist. Hence Theorem 13 supplies compatible colored relative cohomology classes on every face chain having at least three invariant middle vertices. At two vertices, Theorem 12 specifies the missing lower-degree correction.

#### The same threshold for cube affine-word labels

Let
\[
L_n=\{z\in\mathbb R^n:\sum_i z_i=0,\ \sum_i iz_i=0\},
\qquad D=n-3,
\]
and consider the affine-dependence cube labels in \(S(L_n)\cong S^D\). Fix \(H\subseteq[n]\), \(1\le h=|H|\le n-2\), and prescribed signs \(\sigma\). Define
\[
V(H,\sigma)=
S(L_n)\cap\left(
\{\sigma_i z_i\ge0\ (i\in H)\}
\cup
\{\sigma_i z_i\le0\ (i\in H)\}
\right).
\tag{37}
\]

**Theorem 14 (paired positional constraints).** The space (37) has an odd strong deformation retraction onto a linear sphere
\[
\boxed{S^{D-h+1}=S^{n-h-2}.}
\tag{38}
\]
For \(h=1\) it is the entire sphere \(S(L_n)\). For \(h\ge2\) the fundamental degree-\(D\) cohomology class restricts to zero on it. At \(h=2\), its relative lift has the nonzero norm transgression of Theorem 12, with one regular two-dimensional relative module. At \(h\ge3\), the relative lift is unique and invariant.

*Proof.* Choose distinct \(a,b\notin H\). Replace \(z_i\), \(i\in H\), by
\(\lambda(z)\sigma_i\), where \(\lambda=h^{-1}\sum_{i\in H}\sigma_i z_i\). Adjust only the entries \(a,b\) to restore the two defining equations of \(L_n\). There is a unique linear adjustment, since
\[
\begin{pmatrix}1&1\\a&b\end{pmatrix}
\]
is nonsingular. Retain every other entry. This gives a linear projection onto the subspace of \(L_n\) where the \(H\)-entries lie on the line \(\mathbb R\sigma\). On either sign cone, normalized interpolation to the projection never vanishes: if any \(H\)-entry is nonzero, its signed sum has the strict cone sign and the projected \(H\)-vector is nonzero; otherwise the projection fixes the point.

Prescribing arbitrary entries on \(H\) is possible in \(L_n\) by solving for \(a,b\). Therefore the projected subspace has dimension
\((n-2)-(h-1)=n-h-1\), and its unit sphere gives (38). The one-sign equality and the cohomology vanishing follow.

For two signs, their entry functionals are independent on \(L_n\). The complement of (37) has the same two opposite open sectors used in Theorem 12. Its relative top cohomology is a regular two-dimensional module, whose invariant part maps to zero in the absolute top class. The cohomology sequence
\[
0\to H^{D-1}(V)\to H^D(S(L_n),V)
\to H^D(S(L_n))\to0
\]
therefore has the nonzero norm transgression between its one-dimensional trivial end modules. For at least three signs, (38) has dimension at most \(D-2\), and the relative-to-absolute map in degree \(D\) is an equivariant isomorphism. \(\square\)

For \(h=n-1\) or \(h=n\), assume the first sign cone contains a vector with every prescribed signed entry strictly positive. Each sign cone then contracts by normalized interpolation to that vector or its negative. Their intersection has all \(H\)-entries zero and at most one remaining entry, so both moment equations force it to be empty. Consequently \(V(H,\sigma)\simeq S^0\), and its degree-\(D\) relative lift is again unique and invariant. In the complete-path application, strict feasibility is supplied by any affine-dependence label of a flag in the cell. Thus the same one-, two-, and three-sign distinctions cover all nonempty constant-position families of bad words.

If a cube source cell has \(h\) constant color positions, its affine-dependence labels lie in the first sign cone of (37), and the antipodal cell's labels lie in the other. For boundary residues, the same statement holds after placing the coefficients on the invariant middle vertices, giving (27). Thus the two-sign transgression and the three-sign relative normalization apply to both original complete-path constructions through their existing labels.

These statements concern relative cohomology and the paired color carriers. They preserve every source flag's dimension-simple cube geodesic or vertex-simple Hamilton path. Constructing compatible chain representatives, particularly the lower-degree corrections at two fixed signs and the attachments of cells with no fixed signs, remains necessary for a full color-sensitive Wu–Yang transfer.

Both full existence conjectures remain open.


Let \(Q_n\) have vertex set \(\{0,1\}^n\) and let \(c\) be an arbitrary binary coloring of its undirected edges. Fix a color \(a\). Denote by \(P_a(c)\) the poset of ordered distinct vertex pairs \((u,v)\) joined by a monochromatic color-\(a\) geodesic, with
\[
(u,v)\preceq(u',v')
\]
when there are color-\(a\) geodesics \(u'\to u\) and \(v\to v'\) such that
\[
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{1}
\]
This order and its endpoint-reversal involution \(J(u,v)=(v,u)\) were established earlier in this Article. The distance condition ensures that all concatenated subpaths traverse distinct cube dimensions.

Let \(\mathcal B_n\) be the poset of nonempty *signed dimension sets* \((S^+,S^-)\), where \(S^+,S^-\subseteq[n]\) are disjoint, ordered by inclusion in each part. Its order complex is the barycentric subdivision of the boundary of the \(n\)-crosspolytope:
\[
|\Delta\mathcal B_n|\cong S^{n-1}.
\]
The involution \(j(S^+,S^-)=(S^-,S^+)\) acts antipodally on this sphere.

**Theorem 1 (intrinsic signed-support map).** For every cube-edge coloring and either color, the assignment
\[
\boxed{\rho(u,v)=
\bigl(\{i:u_i=0,\ v_i=1\},\ \{i:u_i=1,\ v_i=0\}\bigr)}
\tag{2}
\]
is an order-preserving map \(P_a(c)\to\mathcal B_n\) satisfying
\[
\boxed{\rho(Jp)=j\rho(p).}
\tag{3}
\]
It induces a simplicial equivariant map
\[
\boxed{\Delta P_a(c)\longrightarrow\operatorname{sd}\partial\mathcal O_n.}
\tag{4}
\]
If the longest color-\(a\) geodesic has length \(L\), its image lies in the barycentric subdivision of the \((L-1)\)-skeleton of \(\partial\mathcal O_n\).

*Proof.* Suppose \(p=(u,v)\preceq p'=(u',v')\). By (1) the concatenated monochromatic paths \(u'\to u\to v\to v'\) form a cube geodesic. Every dimension in which \(u,v\) differ is consequently traversed once on this concatenation, and in the same direction as between \(u',v'\). Thus both signed parts of \(\rho(p)\) are subsets of the corresponding signed parts of \(\rho(p')\). Reversing the ordered endpoints exchanges the two signed parts, giving (3). Passing to chains gives (4). The cardinality of the support of \(\rho(u,v)\) equals \(d(u,v)\); thus the bound \(d(u,v)\le L\) places its image in the stated skeleton. \(\square\)

**Theorem 2 (equivariant retraction on a monochromatic face).** Suppose a cubical \(m\)-face \(F\subseteq Q_n\), with free dimension set \(I\) and \(m\ge1\), has all its edges colored \(a\). Let \(P_a(F)\) denote the induced endpoint poset with both endpoints in \(F\). There is an equivariant order embedding
\[
\boxed{\iota:\mathcal B_I\hookrightarrow P_a(F)}
\tag{5}
\]
such that \(\rho\circ\iota=\operatorname{id}_{\mathcal B_I}\). Consequently
\[
\boxed{S^{m-1}\cong|\Delta\mathcal B_I|
\quad\text{is a \(\mathbb Z_2\)-equivariant retract of }
|\Delta P_a(F)|.}
\tag{6}
\]
In particular, the antipodal characteristic class on the quotient of \(\Delta P_a(F)\) has nonzero \((m-1)\)-st power. Its \(\mathbb Z_2\)-index, defined as the least \(d\) admitting an equivariant map to \(S^d\), is \(m-1\).

*Proof.* Identify the free directions of \(F\) with an \(m\)-cube and use the face vertex \(0^I\) as reference. Given \(S=(S^+,S^-)\in\mathcal B_I\), define endpoints \(u(S),v(S)\) in \(F\) by
\[
\begin{array}{c|ccc}
& i\in S^+&i\in S^-&i\in I\setminus(S^+\cup S^-)\\ \hline
u(S)_i&0&1&0\\
v(S)_i&1&0&0 .
\end{array}
\tag{7}
\]
All edges of \(F\) have color \(a\), so \(\iota(S)=(u(S),v(S))\) belongs to \(P_a(F)\). If \(S\subseteq T\) as signed sets, the geodesic from \(u(T)\) to \(u(S)\) traverses the newly added negative directions, and the geodesic from \(v(S)\) to \(v(T)\) traverses the newly added positive directions. Their supports are disjoint from one another and from the support of \(\iota(S)\), proving \(\iota(S)\preceq\iota(T)\). Conversely, containment of these endpoint intervals forces signed-support inclusion by Theorem 1; thus \(\iota\) is an order embedding.

Equation (7) gives \(\iota(jS)=J\iota(S)\) and \(\rho\iota(S)=S\). Therefore \(\Delta\iota\) and \(\Delta\rho\) exhibit the required equivariant retraction. The classifying map for the free involution on \(\Delta P_a(F)\) restricts along the embedded sphere quotient to that of \(\mathbb{RP}^{m-1}\), where the \((m-1)\)-st power of the degree-one class is nonzero. Hence the same power is nonzero on \(\Delta P_a(F)/J\). The map \(\rho\) supplies an equivariant map to \(S^{m-1}\), establishing the index claim. \(\square\)

**Theorem 3 (translation components of lower fibers).** In the setting of Theorem 2, fix a signed set \(S\in\mathcal B_I\) of cardinality \(k\). The lower fiber
\[
\boxed{\rho^{-1}(\mathcal B_{I,\le S})\subseteq P_a(F)}
\tag{8}
\]
is a disjoint union of \(2^{m-k}\) subposets, each possessing a greatest element. Therefore its order complex has the homotopy type of \(2^{m-k}\) discrete points.

*Proof.* An ordered endpoint pair in the fiber can differ only in the dimensions of \(S\), and every such difference must follow the corresponding orientation sign. The common bits outside \(\operatorname{supp}S\) are constant along comparisons in the fiber; hence the fiber splits into \(2^{m-k}\) subposets, indexed by these bits. In each such \(k\)-face, let \(p_{S,z}\) be the oriented pair differing in all \(k\) directions according to \(S\). It is monochromatically joined because the whole face is color \(a\). Every other interval in that subposet is contained in this full interval as in (1): first traverse the directions whose fixed endpoint bit equals the ending bit of \(p_{S,z}\), then the shorter interval, and finally the remaining directions. Thus \(p_{S,z}\) is a greatest element and each component is a cone. \(\square\)

**Consequences for the equivariant-chain program.** The signed-support map is defined for the unrestricted coloring class and records precisely the orientation and set of dimensions traversed by every monochromatic geodesic. Under a hypothetical NORI1 counterexample, the length-\((n-1)\) extension lemma proved earlier excludes every color-\(a\) geodesic of length \(n-1\) or \(n\), so (4) lands in an \((n-3)\)-dimensional complex. The desired contradiction would follow from an antipodally equivariant chain map from the cubical boundary sphere into \(\Delta P_a(c)\), as explained in the endpoint-poset construction.

Theorems 2–3 identify two constraints on such a construction. A monochromatic \(m\)-face already forces equivariant index \(m-1\) inside the target; consequently the elementary support bound is topologically sharp on these faces. Further, lower fibers of \(\rho\) can be disconnected even for an entirely monochromatic cube. Thus a carrier argument cannot replace the endpoint poset by the signed-face poset through a claim that all lower fibers are contractible. The different translates of a signed subface must be retained in the chain assignments.

Let \(D\) be the cell structure on a circle with vertices \(0,1\) and two edges \(e^+,e^-\) joining them, oriented \(0\to1\) and \(1\to0\), respectively. Let
\[
\mathbb T_n=D^n,\qquad J(e^+)=e^-,\ J(e^-)=e^+,\ J(0)=0,\ J(1)=1
\]
in each factor. The action of \(J\) on the torus is simultaneous reflection and its fixed points are the \(2^n\) product vertices.

To each ordered pair of cube vertices \(u,v\in\{0,1\}^n\) associate the product cell \(C(u,v)\) whose \(i\)-th factor is \(e^+\) for \((u_i,v_i)=(0,1)\), \(e^-\) for \((u_i,v_i)=(1,0)\), and vertex \(u_i\) for \(u_i=v_i\). Thus \(\dim C(u,v)=d(u,v)\). Let \(P_{\rm all}\) be the poset of ordered distinct cube-vertex pairs with
\[
(u,v)\preceq(u',v')
\iff
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{1}
\]

**Theorem 1 (the universal endpoint torus).** The correspondence \((u,v)\mapsto C(u,v)\) identifies \(P_{\rm all}\) with the face poset of the positive-dimensional cells of \(\mathbb T_n\). Endpoint reversal \((u,v)\mapsto(v,u)\) corresponds to \(J\). Hence, for \(n\ge2\),
\[
\boxed{X_n=\Delta P_{\rm all}}
\tag{2}
\]
is the full subcomplex of \(\operatorname{sd}\mathbb T_n\) on barycenters of positive-dimensional cells. It is the complement of the disjoint open barycentric stars of the \(2^n\) product vertices, and has a free \(J\)-action. It is equivariantly homotopy equivalent to an \(n\)-torus with \(2^n\) disjoint open \(n\)-balls removed.

*Proof.* The four local states \(0,1,e^+,e^-\) correspond to the four ordered pairs of bits. The product cell \(C(u,v)\) is a face of \(C(u',v')\) precisely when every direction in which \(u,v\) differ also changes in \(u',v'\), with the same orientation, while the other changing directions of \(u',v'\) are frozen at either endpoint value. These are precisely the conditions for the distance equality (1). Swapping \(u,v\) exchanges each changing arc \(e^+\leftrightarrow e^-\) and fixes the remaining factor vertices. Chains of positive-dimensional cells give all simplices of (2). The omitted open stars are disjoint balls; reflection fixes only their centers, so the action on the complement is free. \(\square\)

**Theorem 2 (homology of the universal endpoint complex).** For \(n\ge2\), the integral homology groups of \(X_n\) are free abelian, with
\[
\boxed{\operatorname{rank}H_k(X_n;\mathbb Z)=
\begin{cases}
\binom nk,&0\le k\le n-2,\\
n+2^n-1,&k=n-1,\\
0,&k\ge n .
\end{cases}}
\tag{3}
\]

*Proof.* Remove \(N=2^n\) disjoint small open \(n\)-balls from the torus and denote the complement by \(M\). It deformation retracts onto \(X_n\). Excision gives \(H_n(\mathbb T_n,M;\mathbb Z)=\mathbb Z^N\), with all other relative homology zero. The fundamental class of the oriented torus maps to a primitive vector \((\pm1,\ldots,\pm1)\in\mathbb Z^N\). The homology sequence of the pair then gives \(H_k(M)\cong H_k(\mathbb T_n)=\mathbb Z^{\binom nk}\) for \(k<n-1\), and a short sequence
\[
0\longrightarrow\mathbb Z^{N-1}\longrightarrow H_{n-1}(M)
\longrightarrow\mathbb Z^n\longrightarrow0.
\]
This splits over \(\mathbb Z\) and yields (3). \(\square\)

Let \(\mathcal B_n\) be the poset of nonempty signed dimension sets, whose order complex is \(\operatorname{sd}\partial\mathcal O_n\cong S^{n-1}\), and define the signed-support map
\[
\rho(u,v)=
\bigl(\{i:(u_i,v_i)=(0,1)\},
\{i:(u_i,v_i)=(1,0)\}\bigr).
\tag{4}
\]
It is \(J\)-equivariant. For each vertex \(z\in\{0,1\}^n\), the barycentric link \(L_z\) of its product zero-cell is an \((n-1)\)-sphere contained in \(X_n\). Given a signed dimension set, choose its specified oriented arcs and fix all other factor states at \(z_i\). This identifies \(L_z\) with \(\Delta\mathcal B_n\) and is inverse to \(\rho|_{L_z}\).

**Theorem 3 (alternating puncture degrees).** Give each \(L_z\) the standard local torus orientation and the target crosspolytope its usual orientation. With the degree at \(z=0\) normalized to one,
\[
\boxed{\deg(\rho|_{L_z})=(-1)^{|z|},\qquad
\sum_{z\in\{0,1\}^n}\deg(\rho|_{L_z})=0.}
\tag{5}
\]

*Proof.* At local vertex \(z_i=0\), the arcs \(e^+,e^-\) point in the positive and negative tangent directions. At \(z_i=1\), their tangent directions are reversed. The map \(\rho\) sends \(e^+\) and \(e^-\) to the positive and negative crosspolytope rays independently of \(z\). Hence changing one bit of \(z\) changes the local mapping degree by a factor of \(-1\). This proves the first identity. The second is \(\sum_z(-1)^{|z|}=(1-1)^n=0\). \(\square\)

**Theorem 4 (unrestricted color-sensitive embedding).** For any binary edge coloring \(c\) and either color \(a\), let \(P_a(c)\) be the ordered-pair poset of monochromatic color-\(a\) geodesics, with comparisons required to have monochromatic endpoint extensions satisfying (1). Then the natural map
\[
\boxed{\Delta P_a(c)\hookrightarrow X_n}
\tag{6}
\]
is an equivariant simplicial embedding. Every simplex has a common monochromatic dimension-simple geodesic witnessing all its ordered endpoint pairs. If the maximum monochromatic color-\(a\) geodesic length is \(L\), its image uses only torus cells of dimension at most \(L\).

*Proof.* Every monochromatic endpoint pair defines a product cell, and every comparison satisfies (1), hence is a product face incidence. Reversing a monochromatic geodesic preserves its color. Repeated application of the distance equality shows that the monochromatic paths witnessing a chain can be concatenated with disjoint sets of traversed dimensions; the resulting geodesic contains all specified endpoint pairs. Since \(\dim C(u,v)=d(u,v)\), the final claim follows. \(\square\)

**Relation to Article XV.** In the angular model \(\mathbb T_n=(\mathbb R/2\mathbb Z)^n\) the involution of this Subsection is \(J(t)=-t\), with fixed points \(t_i\in\{0,1\}\). Translation by \(\tfrac12\mathbf1\) conjugates it to \(R(t)=\mathbf1-t\), whose fixed points \(t_i=\pm\tfrac12\) are removed in Article XV's free reversal carrier. Thus \(X_n\) is an equivariant spine of that punctured affine torus, after translation of its cubical decomposition. Its color-dependent subcomplex (6) makes the original problem intrinsic to this topological space, without losing the dimension-simple geodesic witnesses.

Under a hypothetical failure of NORI1, the known length-\((n-1)\) extension lemma confines the monochromatic subcomplex to torus cells of dimension at most \(n-2\). The ambient complex nevertheless contains the \((n-1)\)-dimensional antipodal link spheres of (5). Producing a color-sensitive equivariant transfer from the ambient carrier to the constrained endpoint complex would contradict the index bound. The alternating sum (5) also explains why an unweighted aggregation of all puncture degrees cannot supply the missing transfer: those degrees already cancel.

Let \(n\ge5\) and let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd coloring. For \(a\in\{0,1\}\), let \(P_a(c)\) be the monochromatic geodesic endpoint poset defined earlier in this Article: its elements are oriented endpoint pairs \((u,v)\) with a color-\(a\) geodesic between them, ordered by monochromatic, support-disjoint endpoint extensions. In the universal oriented-interval torus \(X_n\), put
\[
K_a=\Delta P_a(c),\qquad K=K_0\cup K_1,\qquad I=K_0\cap K_1.
\tag{1}
\]
All are simplicial subcomplexes of the same barycentric subdivision. On oriented pairs define
\[
A(u,v)=(\bar u,\bar v),\quad J(u,v)=(v,u),\quad R=AJ.
\tag{2}
\]
The first involution exchanges \(K_0,K_1\), endpoint reversal preserves each, and therefore \(R(K_0)=K_1\), \(R(I)=I\), and \(R(K)=K\). The rank of an endpoint pair is its Hamming distance.

**Theorem 1 (two-color near-spanning closure).** Suppose distinct cube vertices \(u,v\) have Hamming distance \(n-2\), and there exist both a red geodesic and a blue geodesic joining \(u\) to \(v\). Then \(c\) admits a monochromatic full antipodal geodesic.

More generally, if \(d(u,v)=n-k\), \(1\le k\le n-1\), and there are monochromatic geodesics of both colors joining \(u\) to \(v\), then there is a complete antipodal geodesic with at most \(k-1\) switches.

*Proof.* Let \(D\subseteq[n]\) be the set of dimensions in which \(u,v\) differ, and let \(i_1,\dots,i_k\) be an arbitrary ordering of the unused dimensions. Put \(b=c(\{v,v\oplus e_{i_1}\})\). Choose a color-\(b\) geodesic from \(u\) to \(v\), possible by hypothesis, then traverse \(i_1,\dots,i_k\). The resulting path goes from \(u\) to \(\bar u\) and uses every dimension once. Its first \(n-k+1\) edges have color \(b\); only the remaining \(k-1\) edges can introduce switches. For \(k=2\), the full word has at most one switch. The established cyclic root-slide identity transforms every full word with at most one switch into a monochromatic full word (possibly at a different root). \(\square\)

**Corollary 2 (sharp two-color rank exclusions).** Suppose, toward a contradiction, that \(c\) has no monochromatic full antipodal geodesic. Then:
\[
\begin{array}{ll}
\text{(i)}&\text{Every vertex of \(K\) has rank at most \(n-2\).}\\
\text{(ii)}&\text{Every vertex of \(I\) has rank in \(\{2,\dots,n-3\}\).}
\end{array}
\tag{3}
\]
Consequently
\[
\boxed{\dim K\le n-3,\qquad \dim I\le n-5.}
\tag{4}
\]
The rank-one exclusion in (ii) holds for every coloring, because a single undirected cube edge has only one color.

*Proof.* The near-spanning extension lemma of Article XIV says that a monochromatic length-\((n-1)\) geodesic extends to a full monochromatic geodesic: the two unused-direction edges incident with its endpoints form an antipodal pair and have complementary colors. This excludes ranks \(n-1,n\), proving (i). A vertex of \(I\) belongs to both monochromatic endpoint posets and therefore supports both colors of geodesics between the same endpoints. Rank one is impossible, and rank \(n-2\) is excluded by Theorem 1. Rank is strictly increasing along any nonconstant chain of the endpoint poset, so the number of available ranks bounds simplex dimension as in (4). \(\square\)

**Theorem 3 (explicit low-dimensional odd map on the bi-monochromatic intersection).** Under the hypotheses of Corollary 2, there is a simplicial \(R\)-equivariant map
\[
\boxed{\lambda:I\longrightarrow
\partial\operatorname{Crosspolytope}_{n-4}\cong S^{n-5},}
\tag{5}
\]
where \(R\) acts as the antipodal involution on the target.

For every vertex \(p=(u,v)\) of \(I\), let \(r(p)=d(u,v)\) and let \(i(p)\) be the least dimension for which \(u_i=v_i\). Define
\[
\boxed{\lambda(p)=(-1)^{u_{i(p)}}e_{r(p)-1},
\qquad 2\le r(p)\le n-3.}
\tag{6}
\]

*Proof.* The unused dimension \(i(p)\) exists since \(r(p)\le n-3\). If \(p\preceq q\) within a simplex of \(I\), their ranks differ unless they coincide. Thus the labels of distinct simplex vertices lie on distinct target axes \(e_1,\dots,e_{n-4}\), so they span a simplex of the crosspolytope boundary. Under \(R(u,v)=(\bar v,\bar u)\), rank and unused dimension set are unchanged, while the common bit at \(i(p)\) is complemented. Therefore \(\lambda(Rp)=-\lambda(p)\), establishing equivariance. \(\square\)

**Theorem 4 (sphere suspension for the entire two-color endpoint complex).** Under the same hypotheses there exists a continuous \(R\)-equivariant map
\[
\boxed{F:K_0\cup K_1\longrightarrow S^{n-4}.}
\tag{7}
\]
In particular the free-involution index of \(K\) is at most \(n-4\), and if \(\alpha=w_1(K\to K/R)\) then
\[
\boxed{\alpha^{n-3}=0\quad\text{in }H^{n-3}(K/R;\mathbb F_2).}
\tag{8}
\]

*Proof.* View \(S^{n-4}\) as the suspension of the equatorial \(S^{n-5}\). The closed upper hemisphere is contractible. Since \(I\subseteq K_0\) is a subcomplex of a finite simplicial complex, the map \(\lambda:I\to S^{n-5}\) extends over \(K_0\) to a continuous map
\[
F_0:K_0\longrightarrow D^{n-4}_{+}\subset S^{n-4}
\]
that restricts to \(\lambda\) on the equator. Such an extension follows by cellular induction into the contractible hemisphere. Define \(F=F_0\) on \(K_0\), and
\[
F(x)=-F_0(Rx),\qquad x\in K_1.
\]
For \(x\in I\), both prescriptions agree because \(\lambda(Rx)=-\lambda(x)\). They therefore glue to a continuous map on \(K\), and by construction \(F(Rx)=-F(x)\). This proves (7). Under the absence of a full monochromatic geodesic, \(R\) has no fixed points on \(K\) by the fixed-center Lefschetz characterization proved previously. The equivariant map descends to \(K/R\to\mathbb RP^{n-4}\), pulling back the universal degree-one class to \(\alpha\). Its \((n-3)\)-rd power vanishes on the target, proving (8). \(\square\)

**An intrinsic obstruction problem.** The free reversal carrier \(M_n\) of Article XV, equivariantly modeled by the punctured torus of the preceding Subsection, has covering class \(\beta\) satisfying \(\beta^{n-1}\ne0\), hence \(\beta^{n-3}\ne0\). If the absence of monochromatic full geodesics supplied any \(R\)-equivariant continuous map
\[
M_n\longrightarrow K,
\tag{9}
\]
then composition with (7) would give an equivariant map \(M_n\to S^{n-4}\), contradicting the nonzero \(\beta^{n-3}\). Thus (9) is a sufficient condition for NORI1, and the missing transfer is now a map to a target **three dimensions below** the ambient carrier's \((n-1)\)-sphere links.

Theorem 4 is a new color-sensitive reduction and does not itself construct (9). The suspension extension is topological: it makes no claim that its image remembers individual geodesic witnesses after projection, whereas the posets \(K_0,K_1\) retain those witnesses intrinsically. In particular, pointwise low-switch Freudenthal coverage is not a prerequisite for (7), avoiding the spanning-tree obstruction proved in the immediately preceding subsection of this Article.

Let \(n\ge5\), let \(c:E(Q_n)\to\mathbb F_2\) be antipodally odd, and let \(K_a=\Delta P_a(c)\) be the monochromatic endpoint complexes of the preceding Subsections, embedded in the oriented-interval torus. Write
\[
K=K_0\cup K_1,\qquad I=K_0\cap K_1,\qquad
R(u,v)=(\bar v,\bar u).
\tag{1}
\]
The involution \(R\) exchanges \(K_0\) and \(K_1\) and preserves their intersection. A vertex \(p=(u,v)\) has rank \(r(p)=d(u,v)\). An edge \([p,q]\) belongs to \(I\) when the same oriented endpoint extension is feasible in both colors, with all traversed dimensions disjoint.

**Theorem 1 (two-color rank jump).** If distinct vertices \(p=(u,v)\), \(q=(u',v')\) are comparable in \(I\), then
\[
\boxed{r(q)-r(p)\ge2}
\tag{2}
\]
after ordering them so that \(p\prec q\). Moreover, writing
\[
a=d(u',u),\qquad b=d(v,v'),\qquad
r(q)-r(p)=a+b,
\tag{3}
\]
every nonzero one of \(a,b\) is at least two.

*Proof.* The comparison \(p\prec q\) in each \(K_t\), \(t=0,1\), requires color-\(t\) geodesics \(u'\to u\) and \(v\to v'\), allowing empty paths, with the distance equality (3). If \(a=1\), the edge \(u'u\) would have to have color zero and color one simultaneously. Hence \(a\ne1\). Similarly \(b\ne1\). Since \(p\ne q\), at least one of \(a,b\) is positive, proving the result. \(\square\)

**Theorem 2 (sharpness of the rank jump).** For every \(n\ge5\), put \(m=\lfloor(n-3)/2\rfloor\). There is a legally antipodally odd coloring for which \(I\) contains a simplex with \(m\) vertices of ranks
\[
\boxed{2,4,\ldots,2m.}
\tag{4}
\]
Consequently the rank-jump dimension bound below is sharp as a statement about unrestricted legal colorings.

*Proof.* Put \(v_s=\sum_{i=1}^{2s}e_i\), for \(0\le s\le m\). For \(1\le s\le m\), prescribe on the two-dimensional square based at \(v_{s-1}\), in directions \(2s-1,2s\), that the route traversing \(2s-1\) then \(2s\) has color word \(00\), and that the alternative route has word \(11\). The squares have pairwise disjoint direction sets. Moreover \(2m\le n-3\), so at least three unused dimensions have bit zero on every prescribed edge. No two such edges are antipodal, and these prescriptions therefore extend freely to a legal antipodally odd coloring by giving every antipodal mate the complementary color.

For every \(s\), concatenating the color-zero routes through the first \(s\) squares gives a color-zero geodesic from \(0\) to \(v_s\), and concatenating the color-one routes gives a color-one geodesic with the same endpoints. Hence \(p_s=(0,v_s)\) is a vertex of \(I\). The routes across the \(s\)-th square also supply the color-zero and color-one terminal extensions witnessing \(p_{s-1}\prec p_s\) for \(s\ge2\). Thus the \(p_s\) form a simplex of \(I\) with the asserted ranks. \(\square\)

**Corollary 3 (half-dimensional bi-monochromatic complex).** Suppose that \(c\) has no monochromatic full antipodal geodesic. By the one-missing-dimension extension theorem of Article XIV, \(K\) contains only endpoint pairs of rank at most \(n-2\). By the two-color near-spanning closure theorem of the preceding Subsection, \(I\) contains no pair of rank \(n-2\), and it contains no pair of rank one. Theorem 1 therefore bounds every chain in \(I\) to ranks in \(\{2,\dots,n-3\}\), separated by at least two:
\[
\boxed{\dim I\le m-1,\qquad
m=\left\lfloor\frac{n-3}{2}\right\rfloor.}
\tag{5}
\]

**Theorem 4 (half-dimensional reversal-odd sphere map).** Under the same hypothetical absence of a monochromatic full geodesic, there are \(R\)-equivariant maps
\[
\boxed{I\longrightarrow S^{m-1},\qquad
K_0\cup K_1\longrightarrow S^m,\qquad
m=\left\lfloor\frac{n-3}{2}\right\rfloor,}
\tag{6}
\]
with the antipodal action on both spheres. The covering class \(\alpha\in H^1(K/R;\mathbb F_2)\) satisfies
\[
\boxed{\alpha^{m+1}=0.}
\tag{7}
\]

*Proof.* For a vertex \(p=(u,v)\in I\), let \(i(p)\) be the smallest dimension in which \(u_i=v_i\). Such a dimension exists since \(r(p)\le n-3\). Define
\[
\lambda(p)=(-1)^{u_{i(p)}} e_{\,1+\lfloor(r(p)-2)/2\rfloor}
\in\{\pm e_1,\dots,\pm e_m\}.
\tag{8}
\]
By Theorem 1, consecutive ranks in any chain of \(I\) differ by at least two. The integer indices in (8) are therefore distinct on different vertices of any simplex, and their signed crosspolytope vertices span a face of \(\partial\mathcal O_m\cong S^{m-1}\). Under \(R(u,v)=(\bar v,\bar u)\), rank and unused dimensions are preserved, while the common bit at \(i(p)\) is complemented. Hence \(\lambda(Rp)=-\lambda(p)\), giving the first equivariant map.

View \(S^m\) as the suspension of \(S^{m-1}\). The map on \(I\) extends over \(K_0\) into the contractible closed upper hemisphere: \(I\subseteq K_0\) is a subcomplex, so the extension can be constructed inductively over cells. Define the map on \(K_1=RK_0\) by applying \(R\) to the input and the antipodal map to the output. The two definitions agree on \(I\), since \(\lambda\) is equivariant, and together give the second map in (6). Under the no-closure hypothesis, \(R\) acts freely on \(K\) by the fixed-center theorem of the preceding Subsections. The quotient map \(K/R\to\mathbb RP^m\) identifies \(\alpha\) with the pullback of the canonical degree-one class, whose \((m+1)\)-st cup power vanishes. This proves (7). \(\square\)

**Consequences for the Wu--Yang modification.** The punctured reversal carrier of Article XV has double-cover class \(\beta\) with \(\beta^{n-1}\ne0\), whereas the color-sensitive two-color endpoint union under a hypothetical NORI1 counterexample admits the map (6) to \(S^m\), where \(m\) grows at half the ambient dimension. An equivariant map from the punctured carrier into \(K\) would therefore contradict the cup-power obstruction. The present theorem constructs the low-dimensional target and proves its sharp rank combinatorics; it does not construct that transfer. The adjacent-square carrier obstruction already recorded in this Article shows that any such transfer must use nonlocal compatibility rather than individually selecting monochromatic subintervals of every oriented torus cell.

Theorem 4 substantially strengthens the \(S^{n-4}\) target in the preceding Subsection. The stronger result relies on comparison edges in the **intersection of the two color poset complexes**, not merely on the existence of two differently colored geodesics between individual endpoint pairs. This distinction is essential: a chain in \(I\) carries simultaneous monochromatic extension witnesses of both colors, and it is those witnesses that force the two-rank gap.

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd coloring. Suppose the coloring has no monochromatic full antipodal geodesic. Call an oriented pair \((u,v)\) *bi-monochromatic* if there are dimension-simple geodesics of each color joining \(u\) to \(v\). Let \(D=\{i:u_i\ne v_i\}\) and \(S=[n]\setminus D\). The endpoints agree on all dimensions of \(S\). The restriction to the \(|S|\)-face through \(u\) with directions \(S\) is denoted \(F_u\), and similarly \(F_v\). Antipodal complementation maps \(F_u\) onto \(F_v\).

**Theorem 1 (residual monochromatic-path exclusion).** If \((u,v)\) is bi-monochromatic and \(|S|=k\ge2\), then neither \(F_u\) nor \(F_v\) admits a monochromatic geodesic of length \(k-1\) starting at the respective endpoint \(u\) or \(v\).

*Proof.* Suppose \(F_v\) has a monochromatic color-\(a\) geodesic \(v\to w\) of length \(k-1\), using all but one direction of \(S\). Choose a color-\(a\) geodesic from \(u\) to \(v\), available by bi-monochromaticity. Concatenate it with \(v\to w\) and append the single unused direction of \(S\). The resulting path traverses all \(n\) dimensions once, and its first \(n-1\) edges have color \(a\). Thus it has at most one switch; the established root-slide criterion makes it a monochromatic full antipodal geodesic, contrary to hypothesis. The proof at \(u\) is symmetric: reverse a length-\((k-1)\) monochromatic geodesic starting at \(u\), prepend it to a matching-color geodesic \(u\to v\), and append the remaining direction of \(S\) at \(v\). \(\square\)

The case \(k=2\) recovers the near-spanning bi-monochromatic exclusion of the preceding Subsection, since any positive-length one-step path is monochromatic. The first nontrivial residual case is \(k=3\).

**Lemma 2 (opposite-corner two-step rigidity in a 3-cube).** Let \(F\cong Q_3\) have any binary edge coloring. Suppose that from each of two opposite corners \(p\) and \(p^\dagger\), every geodesic of length two changes color. Then a single bit \(a\) determines the entire coloring of \(F\): an edge whose endpoints have Hamming weights \(r,r+1\) relative to \(p\), for \(r=0,1,2\), has color
\[
\boxed{a+r\pmod2.}
\tag{1}
\]
In particular all six squares of \(F\) have curvature zero, and the three successive Hamming layers of edges have respective colors \(a,1-a,a\).

*Proof.* Label the three directions \(1,2,3\), put \(p=000\), and let \(a_i=c(0,e_i)\). For \(i\ne j\), write \(b_{i,j}=c(e_i,e_i+e_j)\). The no-monochromatic-two-step condition at \(000\) forces
\[
b_{i,j}=1-a_i.
\tag{2}
\]
For each \(k\), let \(t_k\) denote the color of the edge from the doubleton \([3]\setminus\{k\}\) to the top vertex \(111\). Reading a two-step geodesic from \(111\) first in dimension \(k\), then to singleton \(i\), where \(i\ne k\), gives
\[
b_{i,j}=1-t_k,\quad \{i,j,k\}=[3].
\tag{3}
\]
Equations (2)--(3) imply \(a_i=t_k\) whenever \(i\ne k\). With three directions, these equalities force all six values \(a_i,t_k\) to have one common value \(a\). Equation (2) then forces every middle-layer edge to have color \(1-a\). The opposite-layer colors are both \(a\), establishing (1). Every square has two edges of color \(a+r\) and two of color \(1-a-r\), so its edge-color XOR (curvature) vanishes. \(\square\)

**Theorem 3 (codimension-three alternating fence).** Let \(n\ge4\), and suppose \((u,v)\) is bi-monochromatic with \(d(u,v)=n-3\). Under the hypothetical absence of a monochromatic full antipodal geodesic, the colorings of the opposed 3-faces \(F_u,F_v\) are forced into complementary Hamming-layer patterns:
\[
\boxed{
\begin{array}{c|ccc}
\text{layer measured from }u\text{ or }v &0\to1&1\to2&2\to3\\ \hline
F_u &a&1-a&a\\
F_v &1-a&a&1-a
\end{array}}
\tag{4}
\]
for one bit \(a\). Both faces are square-flat: all their 2-face curvatures vanish.

*Proof.* By Theorem 1 with \(k=3\), no length-two geodesic from \(u\) within \(F_u\) is monochromatic. The same holds from \(v\) within \(F_v\). Antipodal oddness maps \(F_u\) onto \(F_v\), and maps \(u^\dagger\), the corner opposite \(u\) within \(F_u\), to \(v\). Therefore the no-monochromatic-two-step property also holds at \(u^\dagger\). Apply Lemma 2 to the two opposite corners of \(F_u\), obtaining its three layer colors \(a,1-a,a\). Antipodal oddness then determines the pattern in \(F_v\): complementation reverses the layer index \(r\mapsto2-r\), and complements the edge bit, giving \(1-a,a,1-a\). Flatness follows from Lemma 2. \(\square\)

**Corollary 4 (local rank-two double-color diamonds).** Under the hypotheses of Theorem 3, for any distinct \(i,j\in S\), the two cube vertices \(u\oplus e_i\) and \(u\oplus e_j\) admit monochromatic geodesics of both colors between them: the route through \(u\) has color \(a\) and the route through \(u\oplus e_i\oplus e_j\) has color \(1-a\). The analogous statement holds on \(F_v\), with its two colors interchanged.

*Proof.* This follows immediately from the three-layer pattern (4). \(\square\)

**Scope and forward implication.** Theorem 3 is an all-dimensional necessary local condition for a hypothetical counterexample possessing a bi-monochromatic interval of rank \(n-3\). It does not show that such an interval exists in every coloring, nor does it contradict the global no-closure hypothesis by itself. Its content is substantially stronger than a switch-count bound: it forces all 24 edges of the two opposed three-faces, and in particular their six square curvatures per face, into an alternating flat pattern. Thus a chain-level Wu--Yang construction can treat high-rank bi-monochromatic intervals as local flat boundary carriers with rigid opposite-polarity phases, rather than arbitrary overlapping red-blue paths. The remaining challenge is to control their attachments to the \((n-3)\)-dimensional interval directions.

### Sharp rank-three homology of the alternating cube prefix union

This subsection sharpens the relative homology calculation of the preceding alternating rank-three cube construction. All six boundary squares admit complete zero-switch Freudenthal fillings, yet the rank-three relative group is not merely nonzero: it is free of rank two.

Let \(F=[0,1]^3\). Color every edge joining a vertex of Hamming weight \(r\) to one of weight \(r+1\), \(r\in\{0,1,2\}\), with
\[
\boxed{c(e)=a+r\pmod2}
\tag{1}
\]
for a fixed \(a\in\mathbb F_2\). Let \(U\subseteq F\) be the union of all monochromatic rooted Freudenthal prefix simplices, allowing every one of the eight cube roots and both colors. Earlier in Article XIV it was proved that the entire cubical boundary \(\partial F\) lies in \(U\).

For distinct \(i,j,k\in\{1,2,3\}\), write
\[
D_{ijk}=\operatorname{conv}\{e_i,e_i+e_j,e_j,e_j+e_k\}.
\tag{2}
\]
These are the six tetrahedra corresponding to the complete monochromatic dimension-simple geodesics whose edge colors are all \(1-a\). Put \(T=\bigcup_{(i,j,k)}D_{ijk}\).

**Theorem 1 (star-shaped interior and annular trace).** One has
\[
\boxed{U=\partial F\cup T.}
\tag{3}
\]
The polyhedron \(T\) is star-shaped about the cube center \(o=(1/2,1/2,1/2)\) and hence contractible. Its intersection \(A=T\cap\partial F\) is an annulus, triangulated by the following six triangles:
\[
\begin{array}{ll}
F\cap\{t_i=0\}:&
\operatorname{conv}\{e_j,e_k,e_j+e_k\},\\
F\cap\{t_i=1\}:&
\operatorname{conv}\{e_i,e_i+e_j,e_i+e_k\},
\end{array}
\qquad\{i,j,k\}=\{1,2,3\}.
\tag{4}
\]
The annulus has its boundary circles in the level planes \(\sum t_i=1\) and \(\sum t_i=2\).

*Proof.* Every monotone two-edge prefix uses at most two of the three cube directions and hence lies on \(\partial F\). Every length-three monochromatic geodesic must remain entirely between Hamming levels one and two because the two outer edge layers have color \(a\) and the middle layer has color \(1-a\). Such a three-edge path necessarily alternates weights \(1,2,1,2\), so, up to reversal, it has the vertex sequence in (2). Conversely each sequence in (2) is a monochromatic geodesic. Thus the three-dimensional members of \(U\) are precisely the \(D_{ijk}\), proving (3) because the entire boundary is covered by shorter prefixes.

Each tetrahedron \(D_{ijk}\) contains both opposite cube vertices \(e_i\) and \(e_j+e_k\), whose midpoint is \(o\). The tetrahedron is convex and contains \(o\); therefore their union \(T\) is star-shaped about \(o\), and contracts linearly onto \(o\).

A tetrahedron meets a cubical face \(t_i=\epsilon\) in the convex hull of its vertices with that fixed bit. Inspecting the six sequences (2) shows that the maximal intersection in every face is the triangle listed in (4), and that all other intersections are its faces. These six triangles join along the six Hamming-level-one-to-two cube edges. Their remaining exposed edges form two disjoint three-edge loops: one connecting the three weight-one vertices, the other connecting the three weight-two vertices. Thus they form a triangulated annulus, proving the claim. \(\square\)

**Theorem 2 (full homotopy type and sharp relative obstruction).** There are homotopy equivalences and integral homology isomorphisms
\[
\boxed{U\simeq S^2\vee S^2,\qquad
H_3(F,U;\mathbb Z)\cong\mathbb Z^2.}
\tag{5}
\]
All other positive relative homology groups \(H_j(F,U;\mathbb Z)\), \(j\ne3\), vanish.

*Proof.* Write \(S=\partial F\cong S^2\). By Theorem 1, \(U=S\cup T\), where \(T\) is contractible and \(A=S\cap T\) is an annulus, hence homotopy equivalent to \(S^1\). The Mayer–Vietoris sequence contains
\[
0=H_2(A)\to H_2(S)\oplus H_2(T)\cong\mathbb Z
\to H_2(U)\to H_1(A)\cong\mathbb Z
\to H_1(S)\oplus H_1(T)=0.
\]
The resulting short sequence \(0\to\mathbb Z\to H_2(U)\to\mathbb Z\to0\) splits because \(\mathbb Z\) is free, so \(H_2(U)\cong\mathbb Z^2\). The same sequence gives \(H_1(U)=0\), \(H_3(U)=0\), and no higher reduced homology. Van Kampen applies because \(S,T,A\) are path-connected and \(S,T\) are simply connected, giving \(\pi_1(U)=0\). By Hurewicz and the homological form of Whitehead's theorem, a map \(S^2\vee S^2\to U\) representing a basis of \(H_2(U)\) is a homotopy equivalence.

Since \(F\) is contractible, the long sequence for the pair \((F,U)\) identifies \(H_j(F,U)\cong\widetilde H_{j-1}(U)\) for \(j\ge2\). The asserted relative groups follow. \(\square\)

**Corollary 3 (two independent polar defects forced near a counterexample).** Suppose an antipodally odd coloring of \(Q_n\) has no monochromatic full antipodal geodesic but has two monochromatic geodesics of opposite colors between a pair of vertices at distance \(n-3\). The two opposed residual three-faces are forced by the earlier rigidity theorem to have complementary instances of coloring (1). Each such face therefore has zero square-curvature and full zero-switch boundary-square coverage, but carries
\[
H_3(F,U_F^{[0]};\mathbb Z)\cong\mathbb Z^2.
\]
The two independent relative classes arise from the two polar components omitted by the star-shaped interior union.

**Interpretation.** Square-level filling conditions are not enough even when all six squares are filled and have vanishing curvature: the missing rank-three information is a two-dimensional group of obstruction classes. Any dimension-simple Wu--Yang chain correction that fills this residual cube must use chains outside the zero-switch prefix union or a nonlocal cancellation with other cells. The result provides a sharp test for constructions on the half-dimensional antipodal chain tower from the preceding Subsection; it is not a disproof or proof of NORI1.

### Forest monochromatic endpoint complexes collapse to turn graphs

Let \(H\subseteq Q_n\) be a forest. Let \(P(H)\) be the poset of directed endpoint pairs \((u,v)\) whose unique \(H\)-path is a cube geodesic, with order given by containment of directed subpaths. This is the monochromatic endpoint poset restricted to a forest component of the color graph.

Let \(N(H)\) be the undirected nonbacktracking arc graph: its vertices are oriented edges \((u,v)\) of \(H\), and it joins \((u,v)\) to \((v,w)\) when \(u\ne w\). Distinct incident cube edges use distinct dimensions, so every such two-step walk is a cube geodesic.

**Theorem 1 (forest reduction).** There is a homotopy equivalence
\[
\boxed{|\Delta P(H)|\simeq |N(H)|.}
\tag{1}
\]
The subcomplex generated by directed endpoint pairs of ranks at most two is the barycentric subdivision of \(N(H)\), and its inclusion into the full complex is a homotopy equivalence.

*Proof.* Rank-one endpoint pairs are the directed edges of \(H\). Each rank-two pair corresponds to one directed two-edge path, uniquely because \(H\) is acyclic, and is above its two constituent directed edges. Thus the rank-at-most-two order complex subdivides \(N(H)\).

Take an endpoint pair \(p=(u,v)\) of rank \(r\ge3\). The forest has a unique \(H\)-path \(u=x_0,\ldots,x_r=v\), a cube geodesic. Every strict lower endpoint interval in the poset is a nonempty proper contiguous segment of that path; each such segment is present. The strict lower interval poset is consequently the poset of proper nonempty consecutive subintervals \([s,t]\subsetneq[1,r]\), ordered by inclusion. Its order complex is the union of the lower ideals of \([1,r-1]\) and \([2,r]\). Each ideal has a greatest element; their intersection is the lower ideal of \([2,r-1]\), also possessing a greatest element for \(r\ge3\). Thus the lower order complex is contractible.

Adjoining the vertex \(p\) cones off this contractible subcomplex, preserving homotopy type. Intervals of the same rank are incomparable, allowing the attachments to be made one by one. Induction on rank proves (1). \(\square\)

**Theorem 2 (Betti numbers of a monochromatic tree component).** Let \(H\) be a tree with \(m\ge1\) edges and degrees \(d_v\). Then \(\widetilde H_i(\Delta P(H);\mathbb Z)=0\) for every \(i\ge2\), and
\[
\boxed{\beta_1(\Delta P(H))=
\sum_{v\in V(H)}d_v(d_v-1)-2m+\kappa,}
\tag{2}
\]
where \(\kappa=2\) if \(H\) is a path and \(\kappa=1\) if it has a vertex of degree at least three. The complex has precisely \(\kappa\) connected components.

*Proof.* \(N(H)\) has \(2m\) directed-edge vertices. At a vertex \(v\), there are \(d_v(d_v-1)\) nonbacktracking ordered two-edge turns, each providing a distinct edge in \(N(H)\). Hence its total number of edges is \(\sum_vd_v(d_v-1)\). The component classification proved in the preceding subsection gives two orientation components for a path and one component for a tree with branching. The standard cycle-rank formula \(\beta_1=|E|-|V|+\kappa\) gives (2), and a graph has no higher homology. Apply Theorem 1. \(\square\)

**Corollary 3 (a tree can create essential directed-interval cycles).** For an embedded star \(H=K_{1,d}\), \(d\ge3\),
\[
\boxed{|\Delta P(H)|\simeq\bigvee^{d^2-3d+1}S^1.}
\tag{3}
\]
In particular a degree-three monochromatic star contributes a circle, despite having an acyclic edge graph.

*Proof.* Every admissible directed geodesic interval in a star has length one or two. The nonbacktracking arc graph is \(K_{d,d}\) with its matching of immediate reversals deleted. It is connected for \(d\ge3\), with \(2d\) vertices and \(d(d-1)\) edges. Its cycle rank is \(d^2-3d+1\). \(\square\)

**Corollary 4 (legal antipodal coloring realizes an isolated star).** For every \(n\ge4\) there is an antipodally odd coloring of \(Q_n\) whose color-zero edge graph has the star at \(0^n\) as an entire connected component. Its endpoint-poset component has first Betti number \(n^2-3n+1\).

*Proof.* Color all edges incident to \(0^n\) zero and all edges between weight-one and weight-two vertices one. For \(n\ge4\), none of these prescribed edges is antipodal to another prescribed edge of the same kind, and the two prescribed collections do not clash with each other's antipodal mates. Extend by complementary values to antipodal edge orbits. Each weight-one vertex is incident with only one zero-colored edge, namely the edge to \(0^n\). The zero-colored component of that corner is therefore precisely its star. Apply Corollary 3. \(\square\)

**Implication.** The first antipodal chain-tower condition can be tested by component incidence. But even a monochromatic tree may support nonzero \(H_1\) in its *directed interval complex*. Its undirected edge-graph homology is therefore an insufficient substitute when analyzing the second tower equation. Higher-rank intervals do not erase these classes when the monochromatic component is a tree; the issue is already present in its turn geometry.

### Equivariant component-nerve map and the fixed-incidence-edge threshold

Let \(K_0,K_1\) be finite simplicial complexes embedded as subcomplexes of a common complex. Let \(K=K_0\cup K_1\) and \(I=K_0\cap K_1\). Assume a simplicial involution \(R\) exchanges \(K_0\) and \(K_1\). For antipodally odd cube-edge colorings, the application is to the red and blue directed geodesic endpoint-poset complexes, with \(R(u,v)=(\bar v,\bar u)\).

Let \(\Gamma\) be the bipartite **component incidence graph**: each vertex is a connected component of one of the two color complexes; for each pair of components that intersect, give \(\Gamma\) an edge joining them. The involution exchanges the two vertex classes. A simplex of \(I\) belongs to one red and one blue component, yielding one incidence edge.

**Theorem 1 (equivariant nerve map).** There is a canonical piecewise-linear map
\[
\boxed{\nu:|K|\longrightarrow|\Gamma|}
\tag{1}
\]
that is \(R\)-equivariant, induces a bijection on connected components, and induces a surjection on the fundamental group and on first integral homology of each connected component.

*Proof.* Use the barycentric subdivision of \(K\). For each nonempty simplex \(\sigma\in K\), assign its barycenter as follows:
- If \(\sigma\in K_0\setminus I\), assign the vertex of \(\Gamma\) representing its component of \(K_0\).
- If \(\sigma\in K_1\setminus I\), assign the corresponding blue vertex.
- If \(\sigma\in I\), assign the midpoint of the incidence edge connecting the red and blue components containing \(\sigma\).

These assignments are compatible with inclusions of simplices. If \(\sigma\subseteq\tau\), then either both are in \(I\), in which case they belong to the same red and blue components and are assigned the same midpoint, or \(\tau\) lies in one color but not in \(I\), in which case the assigned points lie in the closed half-edge incident with its color component. The case of a simplex of one color being a face of a simplex belonging only to the opposite color cannot occur. Affine interpolation over the simplices of the barycentric subdivision therefore defines the continuous piecewise-linear map (1). The rule is symmetric under \(R\), so \(\nu(Rx)=R\nu(x)\).

The component-incidence criterion proved previously establishes that \(\pi_0(K)\cong\pi_0(\Gamma)\). To prove surjectivity on \(\pi_1\), choose a base vertex inside each color component and, for each incidence edge \(e\) of \(\Gamma\), choose a simplex of the corresponding red-blue intersection. A traversal of \(e\) lifts to a path in \(K\) from the chosen base vertex of its red component to that of its blue component, passing through the chosen intersection simplex. Such paths exist because the individual color components are path connected. Their images under \(\nu\) are homotopic relative endpoints to the corresponding incidence edge: within one color component the image stays inside the closed star of its incidence vertex, which is a tree, and the chosen intersection simplex maps to the midpoint of \(e\). Concatenating these lifted paths around any graph loop provides a loop in \(K\) whose image is homotopic to that graph loop. This proves surjectivity of \(\pi_1\), and hence of \(H_1(-;\mathbb Z)\). \(\square\)

**Theorem 2 (free-nerve covering-index collapse).** Suppose \(R\) fixes no incidence edge of \(\Gamma\) setwise. Then it acts freely on \(|\Gamma|\) and on \(|K|\), and the covering class
\[
\alpha=w_1(K\to K/R)\in H^1(K/R;\mathbb F_2)
\]
satisfies
\[
\boxed{\alpha^2=0.}
\tag{2}
\]

*Proof.* The involution exchanges the red and blue vertex sets of \(\Gamma\); hence it fixes no graph vertex. A simplicial involution on a graph without fixed vertices has a fixed point in the realization precisely when some edge is setwise invariant, with its two endpoints exchanged. The hypothesis therefore makes \(\Gamma\) a free \(R\)-graph. Because \(\nu\) is equivariant, any fixed point of \(R\) in \(K\) would map to a fixed point in \(\Gamma\); thus \(R\) is also free on \(K\).

The equivariant map \(\nu\) induces a map \(\bar\nu:K/R\to\Gamma/R\) between orbit spaces, and the cover \(K\to K/R\) is the pullback of the double cover \(\Gamma\to\Gamma/R\). Therefore \(\alpha=\bar\nu^*\beta\), where \(\beta=w_1(\Gamma\to\Gamma/R)\). Since \(\Gamma/R\) is a graph, \(H^2(\Gamma/R;\mathbb F_2)=0\), hence \(\beta^2=0\). Pullback gives (2). \(\square\)

**Corollary 3 (a native red-blue condition for higher covering index).** In an antipodally odd coloring, write \(C_0(p)\) for the red component of a bi-monochromatic endpoint pair \(p\in I\), and let \(A(u,v)=(\bar u,\bar v)\), \(J(u,v)=(v,u)\). An incidence edge is preserved setwise by \(R=AJ\) if and only if
\[
\boxed{C_0(Ap)=J C_0(p).}
\tag{3}
\]
Equivalently, \(p\) and \(Rp\) belong to the same red component and to the same blue component.

If a coloring with no monochromatic full antipodal geodesic has \(\alpha^2\ne0\) on its endpoint quotient, then there must exist a bi-monochromatic pair \(p\) satisfying (3). No other color-incidence configuration can support a nonzero square of the reversal covering class.

*Proof.* Identify blue components with red components by \(A\), as in the preceding odd-walk theorem. An incidence edge is represented by \((C_0(p),0)\sim(C_0(Ap),1)\), while \(R\) maps its endpoints to \((JC_0(p),1)\) and \((JC_0(Ap),0)\). The edge is invariant precisely when \(C_0(Ap)=JC_0(p)\), which also implies the companion equality by applying \(J\) and \(A\). The same condition says the pair \(p,Rp\) lies in each of the red and blue connected components incident with this edge. The final claim is the contrapositive of Theorem 2. \(\square\)

**Research implication.** The equivariant index beyond one is forced to reside near an incidence edge that reversal fixes setwise in the component nerve. Such a fixed *nerve edge* does not mean the original endpoint complex contains a reversal-fixed simplex: distinct intersection simplices may realize the same component incidence and be exchanged freely by \(R\). This distinction prevents a false direct proof of NORI1 from the existence of (3). Theorem 2 nevertheless identifies a precise class of color configurations whose entire endpoint-complex double-cover obstruction collapses in degree two. It refines the general half-dimensional vanishing bound of Article XIV, without claiming that a high index must occur in every coloring.

### Reversal-index localization by unused-dimension signs

Let K be any reversal-stable simplicial subcomplex of a directed geodesic endpoint-poset complex of Q_n. A vertex p=(u,v) uses S(p)={i:u_i≠v_i}; comparable vertices have nested supports and agree on bits of dimensions unused by both. Write R(u,v)=(bar v,bar u), and assume R is free on K.

**Theorem.** For every T⊆[n] the vertex rule s_T(p)_i=0 when i∈S(p), and s_T(p)_i=(-1)^{u_i} otherwise, i∈T, extends affinely over K to an odd continuous map s_T:|K|→R^T. Its zero set is the induced subcomplex K_T on vertices whose supports contain T.

*Proof.* Along a chain, the i-th entry takes only the values 0 and one fixed sign; an affine combination vanishes if and only if every vertex of positive weight uses i. Intersecting these conditions for i∈T identifies the zero locus. R complements the common endpoint bit in unused dimensions, so s_T(Rx)=-s_T(x). □

Let α∈H¹(K/R;F₂) classify the double cover. Put j=|T|. The map s_T descends to a section of j copies of the cover line bundle L. Its top Stiefel–Whitney class equals α^j; this class vanishes off K_T/R because the section there is nowhere zero. Therefore α^j is in the image of H^j(K/R,(K\K_T)/R;F₂)→H^j(K/R;F₂), and α^j≠0 implies K_T≠∅.

**One-component saturation.** If α^j≠0 for j≥1, one R-invariant connected component C⊆K has the property that, for **every** j-subset T⊆[n], some vertex p∈C satisfies T⊆S(p). Indeed α^j restricts nontrivially to one quotient component; its preimage must be connected (a swapped pair of components gives a trivial double cover). Apply the preceding zero-set criterion separately for each T on that same component.

**NORI consequence.** In a hypothetical coloring with no monochromatic full antipodal geodesic, put K=K₀∪K₁ and I=K₀∩K₁. Seam transgression gives α_K^{j+1}=δ(α_I^j). Thus a nonzero (j+1)-st covering power of K requires a single R-invariant connected component of the bi-monochromatic seam I containing a pair using all directions of T, for every j-subset T. In particular α_K²≠0 requires a single connected R-invariant bi-monochromatic family collectively covering every cube direction.

If the largest support occurring in C has size r≥j, the number of distinct supports in C is at least ceil(binomial(n,j)/binomial(r,j)), by counting the j-subsets covered by each support.

These are necessary conditions on any surviving reversal-index class; they do not establish that such classes exist or settle NORI1.

### Bourgin–Yang index descent through prescribed dimension supports

Let \(X\) be a finite simplicial complex with a free involution \(R\), and write \(\alpha=w_1(X\to X/R)\). Suppose there is an odd piecewise-linear map \(s:X\to\mathbb R^t\), with zero set \(Z=s^{-1}(0)\). The cohomological index is measured by powers of \(\alpha\).

**Theorem 1 (zero-set index descent).** For any integer \(k\ge0\),
\[
\boxed{\alpha^{t+k}\ne0\quad\Longrightarrow\quad
\alpha_Z^k\ne0\text{ in }H^k(Z/R;\mathbb F_2),}
\tag{1}
\]
where \(\alpha_Z\) is the covering class restricted to \(Z\). For \(k=0\), the conclusion means \(Z\ne\varnothing\). Equivalently, if \(\alpha_Z^k=0\), then \(\alpha^{t+k}=0\).

*Proof.* Put \(B=X/R\), \(A=Z/R\), and \(U=B\setminus A\). The odd map \(s\) descends to a section of \(L^{\oplus t}\), where \(L\) is the real line bundle of \(X\to B\). The section is nowhere zero on \(U\), so its top Stiefel–Whitney class \(\alpha^t\) vanishes on \(U\). Thus \(\alpha^t\) lifts to a relative class \(e\in H^t(B,U;\mathbb F_2)\).

Assume \(\alpha_Z^k=0\). Choose a sufficiently small neighborhood \(V\) of \(A\) in \(B\) that deformation retracts onto \(A\). Then \(\alpha^k|_V=0\), so \(\alpha^k\) lifts to \(b\in H^k(B,V;\mathbb F_2)\). The relative cup product
\[
e\smile b\in H^{t+k}(B,U\cup V;\mathbb F_2)
\]
vanishes because \(U\cup V=B\). Its image in absolute cohomology is \(\alpha^{t+k}\), which must therefore vanish. This proves the contrapositive. \(\square\)

For a reversal-stable directed geodesic endpoint complex \(K\) as in the preceding unused-dimension section theorem, and a prescribed dimension set \(T\subseteq[n]\), let
\[
K_T=\text{the induced subcomplex on pairs }p=(u,v)
\text{ with }T\subseteq\{i:u_i\ne v_i\}.
\]
The canonical sign section \(s_T\) has rank \(|T|\) and zero set \(K_T\).

**Theorem 2 (support-index inheritance).** Let \(h\ge1\) with \(\alpha_K^h\ne0\). For every \(T\subseteq[n]\) with \(t=|T|\le h\),
\[
\boxed{\alpha_{K_T}^{h-t}\ne0.}
\tag{2}
\]
In particular, for \(t=h-1\), the subcomplex \(K_T\) has a connected component preserved by the reversal involution, not merely one vertex supporting \(T\).

*Proof.* Apply Theorem 1 to the odd section \(s_T\) with \(k=h-t\). For \(k\ge1\), nonvanishing of a degree-one covering class on a quotient component forces that component's double cover to be connected, yielding an \(R\)-invariant connected component of \(K_T\). \(\square\)

**Theorem 3 (one-component recursive saturation of the bi-monochromatic seam).** Let \(c\) be an antipodally odd coloring of \(Q_n\) with no monochromatic full antipodal geodesic. Put \(K=K_0(c)\cup K_1(c)\) and \(I=K_0(c)\cap K_1(c)\), both with their free reversal action. Suppose
\[
\boxed{\alpha_K^{h+1}\ne0\quad(h\ge1).}
\tag{3}
\]
Then one reversal-invariant connected component \(C\subseteq I\) has the following simultaneous property: for every \(T\subseteq[n]\) with \(|T|=t\le h\), the subcomplex \(C_T\) of its bi-monochromatic intervals using all dimensions in \(T\) satisfies
\[
\boxed{\alpha_{C_T}^{h-t}\ne0.}
\tag{4}
\]
In particular, for every \((h-1)\)-element set \(T\), a connected \(R\)-invariant subcomponent of \(C_T\) exists.

*Proof.* The seam transgression identity gives \(\alpha_K^{h+1}=\delta(\alpha_I^h)\), so \(\alpha_I^h\ne0\). Choose one connected quotient component on which \(\alpha_I^h\) remains nonzero, and let \(C\) be its inverse image. The inverse image must be a single connected \(R\)-invariant component, since a swapped pair of components would give a split double cover with vanishing positive-degree class. Apply Theorem 2 to the restricted action on \(C\), for every \(T\). The same \(C\) works for all choices of \(T\). \(\square\)

**Implication for dimension-simple chain transfers.** The earlier section theorem only forced the existence of individual red-and-blue geodesic intervals using prescribed dimension subsets. The present result preserves *residual index* after forcing those dimensions and, in particular, demands connected reversal-invariant families within all nearly maximal prescribed-support strata. This is a strictly stronger necessary condition for high covering index. It does not prove nonvanishing of any such index and does not settle NORI1.

### Two-step bi-monochromatic diamonds and the top-rank reversal parity barrier

Suppose an antipodally odd coloring of Q_n, n>=5, admits no monochromatic full antipodal geodesic. Let I be the intersection of the two monochromatic directed endpoint complexes, with involution R(u,v)=(bar v,bar u). The previous rank-gap result gives ranks 2<=r(p)<=n-3 for its vertices and rank increment at least two for comparable vertices.

**Lemma 1 (two-step comparisons).** If p=(u,v)<q=(u',v') is a comparison in I of rank increment two, then either u'=u or v'=v. At the changed endpoint, the red and blue extension certificates are two monochromatic two-edge routes of opposite colors across the same cube square. Therefore
\[
|u'|_1=|u|_1\pmod2.
\tag{1}
\]

*Proof.* A comparison simultaneously witnessed in both colors cannot insert a single edge before or after the smaller interval, since that edge would require both colors. An insertion of positive length at one endpoint must therefore use at least two dimensions. The total increment is two, so all insertions occur at one endpoint. Its red and blue routes are the two distinct two-edge geodesics of a cube square. The initial endpoint changes by zero or two bits, proving (1).

**Lemma 2 (reversal parity).** For every endpoint pair p=(u,v) of rank r, the first endpoint of Rp=(bar v,bar u) satisfies
\[
|\bar v|_1=|u|_1+n+r\pmod2.
\tag{2}
\]
This follows from the Hamming parity difference r between u and v, together with the parity change n under complementation.

**Theorem 3 (top three rank layers split under reversal).** Let I_top be the induced subcomplex of I on ranks at least n-5. Its connected components are paired by R, with no R-invariant component. Consequently the double-cover class of I_top/R vanishes. The same is true for the support stratum I_T of bi-monochromatic interval pairs using any prescribed set T of n-5 dimensions.

*Proof.* The allowed ranks in I_top are n-5,n-4,n-3, intersected with the universal interval rank bounds. All comparison edges have rank difference at least two, hence join the first and last of these ranks; the middle-rank vertices are isolated. There are no higher simplices. By Lemma 1, the parity of the first endpoint is constant along each comparison edge, hence on each nontrivial graph component. For ranks n-5 and n-3, the value n+r is odd. Lemma 2 shows that R flips the first-endpoint parity and must exchange a connected component with a distinct one. Isolated rank vertices also have distinct R-mates because no rank less than n endpoint pair is fixed by R. The resulting double cover splits componentwise. The support stratum I_T is contained in I_top because its interval ranks are at least n-5, so inherits the splitting.

**Corollary 4.** For n=7 the complete seam I has only ranks 2,3,4, hence I=I_top and alpha_I=0. The seam transgression theorem then yields
\[
\boxed{\alpha_{K_0\cup K_1}^2=0,}
\]
improving the earlier purely rank-derived bound that its third power vanishes. In dimensions five and six, I has no comparison edges, and the same square-zero conclusion holds.

**Meaning.** The top-rank seam alone cannot sustain a reversal-index obstruction. Any invariant connected seam component in higher dimensions must reach lower-rank intervals: rank-two opposite-color extension diamonds near the maximal interval rank cannot connect a vertex to its reversal. The theorem is a conditional obstruction and does not settle NORI1.

### Odd-dimensional top-cohomology cancellation in the bi-monochromatic seam

Let \(n=2k+1\ge7\) be odd. Suppose that an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\) has no monochromatic full antipodal geodesic. Let
\[
K_a=\Delta P_a(c),\qquad I=K_0\cap K_1,\qquad K=K_0\cup K_1,
\]
and let \(R(u,v)=(\bar v,\bar u)\). All their reversal actions are free under the no-closure hypothesis. Set
\[
m=\frac{n-3}{2}=k-1,\qquad d=m-1=\frac{n-5}{2}=k-2\ge1.
\]

By the red-blue interval rank-gap theorem previously proved in Article XIV, every vertex of \(I\) has interval rank in \([2,n-3]\), and each comparability increases rank by at least two. Thus \(\dim I\le d\).

**Lemma 1 (maximal chains have a unique rank sequence).** Every \(d\)-simplex \(\sigma\) of \(I\), if one exists, has vertex ranks
\[
\boxed{2,4,6,\ldots,n-3.}
\tag{1}
\]
Along \(\sigma\), the parity of the initial vertex \(u\) in each directed endpoint pair \((u,v)\) is constant.

*Proof.* A \(d\)-simplex has \(d+1\) vertices and \(d\) successive rank increments, each at least two. Its rank span is therefore at least \(2d=n-5\). The entire permissible rank interval, from 2 to \(n-3\), has span \(n-5\), so all inequalities are equalities: it starts at rank two and every increment is two. In a two-step comparison belonging to both color posets, insertion of a single edge at either endpoint is impossible, since such an edge would have to be red and blue. Consequently both new dimensions must be inserted at one endpoint, changing the initial vertex by zero or two bits. The parity stays constant. \(\square\)

**Lemma 2 (the top-dimensional carrier has a split reversal cover).** Let \(A\subseteq I\) be the simplicial subcomplex generated by all its \(d\)-simplices, including their faces. If there are no such simplices, take \(A=\varnothing\). Then \(A=A^{\rm even}\sqcup A^{\rm odd}\), where every vertex of \(A^{\rm even}\) has even first-endpoint parity and every vertex of \(A^{\rm odd}\) has odd first-endpoint parity. Moreover,
\[
\boxed{R(A^{\rm even})=A^{\rm odd}.}
\tag{2}
\]
Hence the free double cover \(A\to A/R\) splits and its degree-one covering class vanishes.

*Proof.* Lemma 1 ensures that each generating \(d\)-simplex, and therefore every one of its faces, uses vertices of a single first-endpoint parity. Two generating simplices sharing a face or even one vertex must have the same parity. Thus their unions separate into the indicated disjoint subcomplexes. Each vertex of \(A\) has even rank by (1). For a directed pair of rank \(r\), the parity of the first endpoint of its reversal is
\[
|\bar v|_1\equiv |u|_1+n+r\pmod2.
\]
Both \(n\) and \(r\) are respectively odd and even, so reversal flips the parity. It exchanges the two subcomplexes, and the double cover has a section given by the even half. \(\square\)

**Theorem 3 (one-degree improvement of the odd-dimensional reversal-index ceiling).** Let \(\alpha_I\) and \(\alpha_K\) be the degree-one covering classes on \(I/R\) and \(K/R\). Then
\[
\boxed{\alpha_I^d=0,\qquad \alpha_K^{d+1}=\alpha_K^m=0.}
\tag{3}
\]
Equivalently, under the hypothetical absence of a monochromatic full geodesic in odd dimension \(n\ge7\), the two-color endpoint union admits no augmentation-preserving equivariant chain tower through dimension
\[
\boxed{m=(n-3)/2.}
\tag{4}
\]

*Proof.* If \(\dim I<d\), the first assertion follows by dimension. Otherwise all \(d\)-simplices of \(I\) lie in \(A\). The quotient cellular cochain groups \(C^d(I/R;\mathbb F_2)\) and \(C^d(A/R;\mathbb F_2)\) are identified, because the two quotients have the same top-dimensional cells. Moreover every boundary of a top-dimensional simplex uses only \((d-1)\)-cells in \(A/R\). Therefore the images of the preceding coboundary maps into these degree-\(d\) groups coincide: any \((d-1)\)-cochain of \(A/R\) extends to \(I/R\) by zero off \(A/R\), and all degree-\(d\) coboundaries come from its restriction. There are no \((d+1)\)-cells in \(I/R\). Consequently restriction
\[
H^d(I/R;\mathbb F_2)\longrightarrow H^d(A/R;\mathbb F_2)
\]
is injective (indeed an isomorphism). Lemma 2 gives \(\alpha_I|_{A/R}=0\), so its \(d\)-th power restricts to zero. Injectivity forces \(\alpha_I^d=0\).

The seam-transgression theorem established in Article XIV gives
\[
\alpha_K^{d+1}=\delta(\alpha_I^d)=0,
\]
proving the second assertion. Finally the Smith-transfer tower equivalence identifies nonzero \(\alpha_K^m\) with existence of an augmentation-one norm-boundary tower of height \(m\), so this tower is forbidden under the no-closure hypothesis. \(\square\)

**Examples of the strengthened necessary vanishing.** In dimensions \(n=7,9,11,13\), the new ceiling respectively gives
\[
\alpha_K^2=\alpha_K^3=\alpha_K^4=\alpha_K^5=0
\]
(with the four equalities read for their corresponding separate dimensions). The previous all-dimension bound guaranteed vanishing only one power later for odd \(n\).

**Scope and remaining task.** This theorem is conditional on the absence of a monochromatic antipodal geodesic. It makes no assertion that the forbidden height-\(m\) tower can be constructed for every coloring. Constructing it—equivalently forcing the associated reversal index—would prove NORI1 in odd dimension with one fewer chain degree than required by the earlier general criterion. The mechanism is all-dimensional and relies on parity of monochromatic two-step extension diamonds, not on computational verification of small cubes.

### Affine roots, cycle constraints, and odd-degree flag transport

Let \(\sigma\in S_n\) be a derangement and \(a_i\in\mathbb F_2\). Color cube edges by \(c(\{x,x\oplus e_i\})=x_{\sigma(i)}\oplus a_i\). This is independent of the chosen edge endpoint because \(\sigma(i)\ne i\), and it is antipodally odd.

**Theorem 1 (unique root selector and exchange).** Given a full dimension order \(\pi\) and a bit \(b\), there is a unique root \(x_\pi^{(b)}\) making every edge of the full geodesic along \(\pi\) have color \(b\):
\[
\boxed{(x_\pi^{(b)})_{\sigma(i)}
=b\oplus a_i\oplus[\sigma(i)\text{ precedes }i\text{ in }\pi].}
\tag{1}
\]
One has \(x_\pi^{(1)}=\bar x_\pi^{(0)}\) and \(x_{\pi^{rev}}^{(b)}=\bar x_\pi^{(b)}\). If \(\pi'\) swaps consecutive directions \(i,j\), the selected roots can differ only at bit \(j\) if \(\sigma(i)=j\), or bit \(i\) if \(\sigma(j)=i\). If \(\sigma\) has no two-cycle, their Hamming distance is at most one.

*Proof.* By the time the path uses direction \(i\), bit \(\sigma(i)\) has changed from its starting value if and only if \(\sigma(i)\) occurred earlier. Setting its resulting color equal to \(b\) yields (1), prescribing each starting bit once because \(\sigma\) is a permutation. Reversal negates each precedence indicator, and adjacent exchange changes only the relative order of the swapped symbols. \(\square\)

**Theorem 2 (feasible roots and counting).** A fixed root \(x\) admits a monochromatic full geodesic if and only if the binary sequence \((x_{\sigma(i)}\oplus a_i)_{i\in C}\) is nonconstant on every cycle \(C\) of \(\sigma\). Such a root admits geodesics of *both* colors. If the cycle lengths are \(\ell_1,\ldots,\ell_s\), the number of feasible roots is
\[
\boxed{\prod_{t=1}^s(2^{\ell_t}-2).}
\tag{2}
\]
Across all roots there are \(n!\) ordered monochromatic geodesics of either fixed color.

*Proof.* Equation (1) imposes ordering comparisons between \(i\) and \(\sigma(i)\). Within each permutation cycle, these comparisons form an orientation of its cyclic graph. They admit a total order if and only if there is no directed circuit, which occurs if and only if the comparison bits are not all equal. Changing the target color reverses every comparison, preserving the absence of directed circuits. The root-bit assignment to each cycle's comparison bits is bijective, and two constant patterns are excluded among its \(2^{\ell_t}\) patterns. The last assertion follows from uniqueness of the root for each \(\pi,b\). \(\square\)

For two three-cycles and zero offsets, 36 of the 64 roots support full monochromatic geodesics, and each such root has \(\binom63=20\) orders of each color. Nevertheless root \(0^6\) supports none, as in the locally obstructed two-block Grassmannian example of Article XV.

Now suppose \(\sigma\) is one \(n\)-cycle, \(n\ge3\), and all offsets vanish. Write \(x_\pi=x_\pi^{(0)}\). Let \(P_n\) be the centered permutahedron in \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), with vertex \(u_\pi=\sum_j((n+1)/2-j)e_{\pi_j}\). Its boundary is \(S^{n-2}\), with central involution taking \(\pi\) to its reversed order.

**Theorem 3 (equivariant odd-degree root carrier).** The vertex labels \(u_\pi\mapsto x_\pi\) have a canonical antipodal piecewise-linear extension
\[
\boxed{F_\sigma:\partial P_n\longrightarrow
\partial[0,1]^n\setminus\{0^n,1^n\}.}
\tag{3}
\]
After equivariant retraction of its target onto \(S^{n-2}\), this is an antipodal sphere map of odd mod-two degree.

*Proof.* A nonempty proper subset \(S\subset[n]\) indexes a permutahedral facet whose vertex orders put all of \(S\) before its complement. A single \(n\)-cycle has no proper invariant nonempty subset, so some \(i\in S\) satisfies \(\sigma(i)\notin S\). In every refining order, \(i\) precedes \(\sigma(i)\). Equation (1) thus makes bit \(\sigma(i)\) of every corresponding root zero. Hence all root labels on that facet lie in one fixed face of the cube.

On the barycentric subdivision of \(\partial P_n\), send each face barycenter to the arithmetic mean of the root labels of its vertices, then extend affinely across the nested-face simplices. Every simplex lies in a permutahedral facet, where the same cube bit stays zero. This gives the cubical-boundary property.

No root label can be \(0^n\), since this would require \(i\) before \(\sigma(i)\) all around the directed cycle; no label can be \(1^n\) for the reverse reason. Convex combinations cannot equal either extreme cube corner unless every contributing label does. Thus the image avoids the two corners.

By Theorem 1, reversing an order complements its root; averaging over antipodally paired faces makes the map equivariant. Central radial projection identifies the cube boundary with \(S^{n-1}\), and removing the two opposite vertices permits an equivariant retraction to its equatorial \(S^{n-2}\). The resulting map is antipodal between two spheres of dimension \(n-2\). Its quotient preserves the degree-one class and its top cup power in \(H^*(\mathbb RP^{n-2};\mathbb F_2)\), proving odd degree. \(\square\)

**Theorem 4 (multi-cycle obstruction to the same face carrier).** If \(\sigma\) has at least two cycles, choose \(S\) to be a nonempty proper union of full cycles. The facet of orders putting \(S\) first has root labels whose average is the cube center \(\frac12\mathbf1\). Consequently the face-barycenter construction above does not land in the cube boundary.

*Proof.* Every pair \(i,\sigma(i)\) lies within one of the two ordered blocks. As the orders within these blocks range uniformly, either element precedes the other half the time. Formula (1) therefore gives mean root bit \(1/2\) for every bit. The facet barycenter is mapped to the cube center. \(\square\)

**Research interpretation.** An indecomposable cyclic dependency gives an antipodally equivariant, odd-degree, globally coherent selector of monochromatic roots on the type-A flag sphere, with local changes of at most one cube direction. The local Grassmannian obstruction at root zero is resolved in this family through root mobility, not by filling that obstructed top cell. The construction is not extended to arbitrary odd edge colorings and does not settle NORI1.

#### The graphical-zonotope refinement: integral degree one and a sharp connectedness criterion

The antipodal root-carrier map above has a stronger realization through the graphical zonotope of the dependency cycle. The following general theorem applies to any simple graph \(G\) on the dimension set \([n]\), \(n\ge3\), and does not presume that its graphic matroid is connected.

For each edge \(\{i,j\}\), take \(i<j\), and write \(w_{ij}=e_i-e_j\in W=\{z\in\mathbb R^n:\sum z_i=0\}\). Let \(P_n\subset W\) be the centered permutahedron, or equivalently the graphical zonotope of \(K_n\):
\[
P_n=\sum_{\{i,j\}\in E(K_n)}[-w_{ij}/2,w_{ij}/2].
\tag{9}
\]
For an order \(\pi\), put \(\epsilon_{ij}(\pi)=1\) if \(i\) precedes \(j\), and \(-1\) otherwise. Its permutahedral vertex is
\[
u_\pi=\frac12\sum_{E(K_n)}\epsilon_{ij}(\pi)w_{ij}.
\]
For a graph \(G\), define the graphical-zonotope vertex label
\[
z_G(\pi)=\frac12\sum_{E(G)}\epsilon_{ij}(\pi)w_{ij},\qquad
Z_G=\sum_{E(G)}[-w_{ij}/2,w_{ij}/2].
\tag{10}
\]
The label depends only on the orientation of the edges of \(G\) induced by the total order.

**Theorem 5 (connected graphical-zonotope map has integral degree \(+1\)).** Let \(G\) be a connected graph on \([n]\). Map each nonempty face barycenter of \(\partial P_n\) to the arithmetic mean of the \(z_G(\pi)\) over its vertices, and interpolate affinely over the barycentric subdivision. The resulting map
\[
\boxed{\mathcal F_G:\partial P_n\longrightarrow\partial Z_G}
\tag{11}
\]
is continuous, commutes with central inversion, and, after identifying both polytope boundaries with the unit sphere of \(W\) by radial projection, has **integer Brouwer degree \(+1\)**.

*Proof.* For \(t\in[0,1]\), define
\[
Z_t=Z_G+t Z_{K_n\setminus G},\qquad
z_t(\pi)=z_G(\pi)+t z_{K_n\setminus G}(\pi).
\tag{12}
\]
When \(t=1\), \(Z_t=P_n\) and \(z_t(\pi)=u_\pi\). When \(t=0\), these are \(Z_G,z_G(\pi)\). Since \(G\) is connected, its edge-difference vectors span \(W\), so every \(Z_t\) is a centrally symmetric, full-dimensional convex body with the origin in its interior.

A facet \(F_S\) of \(P_n\) is indexed by a nonempty proper \(S\subset[n]\), and its vertices are the orders putting \(S\) before its complement. For every such order,
\[
\sum_{i\in S}z_t(\pi)_i
=\frac12\Bigl(|\partial_G S|+t|\partial_{K_n\setminus G}S|\Bigr),
\tag{13}
\]
the maximum of the same linear functional on \(Z_t\). Connectedness implies \(|\partial_G S|>0\). Therefore all vertex images of \(F_S\) belong to one exposed proper face of \(Z_t\). The barycentric interpolation maps every subdivision simplex in \(F_S\) into that face, giving a continuous map \(\mathcal F_t:\partial P_n\to\partial Z_t\) for all \(t\in[0,1]\). Every image avoids the origin.

At \(t=1\), every source face barycenter maps to the arithmetic mean of that same face's vertices, namely the chosen source barycenter. Thus \(\mathcal F_1\) is the identity on \(\partial P_n\). The normalized maps \(\mathcal F_t/\|\mathcal F_t\|\) form a continuous homotopy from the identity radial sphere map to the normalized map for \(G\). Its degree is therefore \(+1\). Reversing any order reverses every edge-orientation sign, making the construction antipodally equivariant. \(\square\)

**Theorem 6 (sharp necessity of graph connectedness).** If \(G\) is disconnected, the same prescribed face-barycenter formula sends the barycenter of some facet of \(\partial P_n\) to \(0\), so the associated normalized sphere map is undefined. Moreover \(Z_G\) lies in a proper linear subspace of \(W\).

*Proof.* Choose \(S\) to be a nonempty proper union of connected components of \(G\). Every edge of \(G\) lies entirely in \(S\) or its complement. On the facet \(F_S\), internal orders in each block vary independently and uniformly. For each edge \(\{i,j\}\) of \(G\), its two possible orientation signs occur with equal frequency, so the arithmetic average of \(z_G(\pi)\) on this facet is zero. Disconnectedness also means the edge-difference vectors span a subspace of dimension \(n-\#\mathrm{components}(G)<n-1\), so its zonotope has no interior in \(W\). \(\square\)

**Corollary 7 (degree-one strengthening of the cyclic affine root selector).** Suppose the dependency permutation \(\sigma\) is one \(n\)-cycle, \(n\ge3\), with zero offsets. Let \(x_\pi\) be the monochromatic color-zero root of Theorem 1. With the orientation of the cycle edges \(\{\sigma(i),i\}\) chosen consistently, the linear incidence transformation
\[
\boxed{\mathcal B(x)=
\sum_{i=1}^n(x_{\sigma(i)}-\tfrac12)(e_{\sigma(i)}-e_i)}
\tag{14}
\]
sends \(x_\pi\) to \(z_{C_n}(\pi)\). The permutahedron-boundary root-selector interpolation of Theorem 3, followed by \(\mathcal B\) and radial normalization, therefore has **integer degree \(+1\)**. In particular its formerly established odd mod-two degree is the reduction of a unit integral degree.

*Proof.* The root formula gives \(x_{\sigma(i)}=1\) if \(\sigma(i)\) precedes \(i\) and zero otherwise. The summand of (14) is then half of the directed edge vector pointing from the later to the earlier member of the pair, which is the corresponding summand in (10). Linearity of \(\mathcal B\) commutes with face averaging and interpolation. Theorem 5 with \(G=C_n\) therefore applies. \(\square\)

**Meaning and limitation.** The odd-degree root carrier is the \(t=0\) limit of a family of full-dimensional zonotopes, beginning at the original permutahedron. The construction is globally coherent across all Coxeter faces and has signed degree \(+1\), rather than merely nonzero parity. Graph connectedness is necessary and sufficient for this *particular* piecewise-linear carrier to avoid the origin. This provides a robust full-dimensional transport model, but does not prove that an arbitrary antipodally odd edge coloring admits analogous root labels, and does not prove NORI1.

#### General affine root transport: exchange-influence graphs

Let \(M\in\mathbb F_2^{n\times n}\) be invertible with zero diagonal and \(M\mathbf1=\mathbf1\), and color \(i\)-direction edges by \(c_i(x)=a_i+(Mx)_i\). For a total dimension order \(\pi\), define \(t_i(\pi)=\sum_{j\text{ earlier than }i}M_{ij}\). Its unique color-zero root is
\[
\boxed{x_\pi=M^{-1}(a+t(\pi)),\qquad x_{\pi^{rev}}=\bar x_\pi.}
\tag{15}
\]
An adjacent exchange of \(i,j\) changes the root by
\[
\boxed{d_{ij}=M^{-1}(M_{ij}e_i+M_{ji}e_j).}
\tag{16}
\]
For each root bit \(k\), let \(G_k(M)\) be the graph on \([n]\) whose edges are those pairs \(\{i,j\}\) with \((d_{ij})_k=1\).

**Theorem 8 (finite facet-carrier criterion).** For a nonempty proper dimension subset \(S\), root bit \(k\) is constant over all orders listing \(S\) first if and only if *every edge of \(G_k(M)\) crosses the cut* \(S|S^c\). The standard arithmetic-mean barycentric extension of the root labels maps the whole permutahedron boundary into the boundary of the \(n\)-cube if and only if
\[
\boxed{\forall\varnothing\ne S\subsetneq[n],\ \exists k:
E(G_k(M))\subseteq\partial S.}
\tag{17}
\]
If no such \(k\) exists for a facet \(S\), the facet's barycenter is sent to the open cube interior.

*Proof.* Adjacent exchanges within \(S\) or within its complement generate all orders refining the facet indexed by \(S\). They change root bit \(k\) according to (16). Hence \(k\) stays constant throughout precisely when every root-changing exchange pair crosses the cut. A convex hull of cube vertices lies in the cubical boundary only when at least one bit is constant on all its vertices. If each bit varies, the arithmetic mean of its vertex labels has every entry strictly between zero and one, so lies in the open cube interior. This applies on each facet and proves (17). \(\square\)

**Theorem 9 (dense full-rank affine obstruction).** For every even \(n\ge4\), choose \(M=I+J\) and \(a=0\), where \(J\) is the all-ones matrix over \(\mathbb F_2\). Then \(M\) is invertible, has zero diagonal, and has all row sums odd. Its unique roots satisfy
\[
\boxed{(x_\pi)_i=(\operatorname{pos}_\pi(i)-1+n/2)\bmod2.}
\tag{18}
\]
Every such root has Hamming weight \(n/2\). For every facet \(S|S^c\) with \(2\le|S|\le n-2\), its uniform average root lies in the **open cube interior**; if both blocks have even cardinality, this average is the cube center \(\frac12\mathbf1\). Thus all those facets obstruct the standard convex root carrier despite the existence of one monochromatic root for every order.

*Proof.* Since \(n\) is even, \(J^2=nJ=0\) over \(\mathbb F_2\), so \(M^2=I\). We have \(t_i(\pi)=\operatorname{pos}_\pi(i)-1\bmod2\) and \(\sum_i t_i=n(n-1)/2=n/2\bmod2\), yielding (18). Among the \(n\) ranks, half give root bit one. On a two-block facet, each named direction can occupy any rank within its block. If each block contains at least two ranks, these sets contain both parities. Therefore every root bit varies over the refining orders, and its average lies strictly between zero and one. If both blocks have even size, both parities occur equally often within either block, giving mean \(1/2\) in every root bit. \(\square\)

**Interpretation.** The root vertices of this dense family lie in the hypersimplex \(\Delta(n,n/2)\), unlike the punctured-cube root carrier of a connected permutation cycle. For a single-cycle permutation matrix, each influence graph \(G_k(M)\) consists of one edge, so (17) reduces to connectedness of the dependency graph. For \(M=I+J\), each \(G_k(M)\) is the star at \(k\), and no cut with both sides of size at least two makes every edge of that star cross. Consequently invertibility of the affine interaction matrix does not justify the cyclic root-selector interpolation. This is a limitation of a prescribed facewise convex construction, not an obstruction to other color-sensitive root transport or to NORI1.## Functional-reader root census with branching

Fix \(n\ge2\), a function \(r:[n]\to[n]\) with \(r(i)\ne i\), and bits \(a_i\). The coloring \(c_i(x)=x_{r(i)}+a_i\) is antipodally odd. Let \(L_1,\ldots,L_s\ge2\) be the lengths of the directed cycles of \(i\mapsto r(i)\), permitting branches into these cycles.

**Theorem.** The number of roots \(x\in Q_n\) supporting a monochromatic-zero full antipodal geodesic is
\[
\boxed{|R_0|=2^n\prod_{j=1}^s(1-2^{1-L_j})\ge2^{\lceil n/2\rceil}.}
\tag{FR1}
\]
Every such root also supports a monochromatic-one antipodal geodesic. The lower bound is attained by disjoint directed two-cycles, plus an attached tree leaf in odd dimension. The coloring has at least \(2^{\lceil n/2\rceil-1}\) unoriented monochromatic-zero antipodal geodesics.

*Proof.* For an ordering \(\pi\) rooted at \(x\), its step \(i\) has color zero precisely when
\[
[\pi(r(i))<\pi(i)]=x_{r(i)}+a_i.
\]
These equalities orient the functional-graph edges as precedence constraints. A compatible total order exists if and only if their orientation is acyclic. Each component is unicyclic, possibly with a directed two-cycle represented by parallel constraints; attached trees cannot participate in a directed circuit. On a reader cycle of length \(L\), the comparison directions depend independently on its \(L\) root bits. Precisely two of the \(2^L\) patterns create a directed circuit: for \(L\ge3\), the two consistently directed cycle orientations; for \(L=2\), the two assignments requiring both incompatible precedence orders. The other patterns all extend to total orders. Cycle bit sets are disjoint, and tree root bits impose no restrictions, proving the root count.

Complementing \(x\) reverses every precedence edge, preserving acyclicity. A monochromatic-zero antipodal geodesic from \(x\) gives a monochromatic-one geodesic with the same start by antipodal complementation followed by path reversal. Each factor \(1-2^{1-L_j}\ge1/2\) and there are at most \(\lfloor n/2\rfloor\) cycles. The lower bound follows and is attained by two-cycles. Each unoriented monochromatic-zero geodesic has two starting vertices, yielding the stated path-count bound. \(\square\)

For permutation readers this extends the earlier cycle-product result of this Subsection. The contribution is that branching trees leave the root-success fraction unchanged. It combines with the quadratic Walsh minimizer classification to give exponentially many paired roots at every sharp spectral minimizer.

#### Edge-orbit avoidance and restoration resilience for one-reader colorings

Continue with a legal coloring \(c_i(x)=x_{r(i)}+a_i\), where \(r(i)\ne i\), and let \(L=\{j:r^{-1}(j)=\varnothing\}\) be its set of unused reader bits (leaves of the functional graph).

**Theorem (no compulsory antipodal edge pair).** For \(n\ge4\) and every antipodal edge orbit \(q=\{e,\bar e\}\), there is a monochromatic-zero full antipodal geodesic avoiding both members of \(q\). Hence flipping any one antipodal edge pair preserves a monochromatic antipodal geodesic. When \(r\) is a permutation, the avoidance assertion already holds for \(n\ge3\).

*Proof.* Fix the direction \(i\) of \(q\). It suffices to exhibit two monochromatic-zero full geodesics using different direction-\(i\) edge orbits.

Suppose \(L\ne\varnothing\). If a leaf \(j\in L\) is distinct from \(i\), take any monochromatic-zero full path \(P\) rooted at \(x\), whose existence was proved above. Changing the initial bit \(x_j\), while keeping its direction order, leaves every traversed color unchanged: no direction reads bit \(j\). The two resulting paths use different direction-\(i\) edges, since their bit \(j\) values differ when that direction is traversed. Both edges have color zero and thus cannot belong to the same antipodal edge orbit.

It remains to consider \(L=\{i\}\). The colors of every other direction are independent of bit \(i\). Restrict to the \((n-1)\)-cube on directions other than \(i\), still a one-reader coloring. Its monochromatic-zero root set \(R'_0\) is antipodally invariant and has size at least \(2^{\lceil(n-1)/2\rceil}\) by the root census. Let \(j=r(i)\). Precisely half of \(R'_0\) has initial bit \(x_j=1+a_i\). For each of these roots take any monochromatic-zero full path in the smaller cube and append the direction-\(i\) edge. Its color is zero because bit \(j\) has been flipped, and its direction-\(i\) edge is located at the antipode of that smaller-cube root. When \(n\ge4\), there are at least two such roots; they yield different zero-colored direction-\(i\) edges, hence different orbits.

Finally suppose \(L=\varnothing\). Then \(r\) is a permutation without fixed points. For each direction order \(\pi\), the monochromatic-zero root is uniquely prescribed by
\[
x_{r(k)}=a_k+[\pi(r(k))<\pi(k)].
\]
Choose \(j\notin\{i,r(i)\}\), possible for \(n\ge3\), and put \(k=r^{-1}(j)\). The bit in position \(j\) of the direction-\(i\) edge traversed by this root/order pair is
\[
a_k+[\pi(j)<\pi(k)]+[\pi(j)<\pi(i)].
\]
The three symbols \(i,j,k\) are distinct. Choose orders with \(j\) preceding both \(i,k\), and with \(j\) strictly between them; the displayed bit changes. These orders therefore yield different zero-colored direction-\(i\) edge orbits. \(\square\)

**Theorem (leaf-translated Boolean path family).** Suppose \(\ell=|L|\ge1\). Every one-reader coloring has a family of \(2^\ell\) monochromatic-zero full geodesics, obtained from any one path by changing its initial bits in arbitrary subsets of \(L\), while keeping the direction order fixed. For a uniformly selected member of this family, the probability that its direction-\(i\) edge belongs to any prescribed antipodal edge orbit is at most
\[
\boxed{2^{-(\ell-\mathbf1_{i\in L})}\le2^{1-\ell}.}
\tag{AR1}
\]
Therefore any legal recoloring of fewer than \(2^{\ell-1}\) antipodal edge orbits preserves a monochromatic-zero full geodesic.

*Proof.* By the definition of \(L\), no direction color depends on a bit in \(L\). Each changed initial leaf bit therefore translates the entire path without changing its zero word. At its direction-\(i\) step, the edge position records all translated leaf bits except the bit \(i\) itself, if \(i\) is a leaf. Thus each prescribed zero-colored direction-\(i\) edge is encountered by at most a fraction \(2^{-(\ell-\mathbf1_{i\in L})}\) of the translated paths. Since the antipodal mate has color one, the same estimate holds for an antipodal edge orbit. For a set of \(k\) recolored orbits, the expected number hit by a random path in the family is at most \(k2^{1-\ell}\). If \(k<2^{\ell-1}\), this expectation is less than one, so some path avoids every changed orbit and survives monochromatically. \(\square\)

**Consequence for restoration and closure.** For \(n\ge4\), any coloring obtained by changing at most one antipodal edge pair of a one-reader legal coloring is good. More generally, the forbidden Hamming radius around a one-reader template with \(\ell\) unused reader bits is at least \(2^{\ell-1}-1\) orbits, and is at least one orbit regardless of \(\ell\). Thus the universal internal-pivot configuration forced by a hypothetical good-to-bad restoration transition cannot have a one-reader coloring on its good side. The statement is consistent with the sharp dimension-three limitation: one-reader colorings in dimension three can have a common edge orbit in all monochromatic-zero geodesics.

The same-degree path avoidance and leaf-family claims were checked against complete enumeration of one-reader legal colorings in dimensions two through five; the proofs apply at all dimensions.

#### Partial reader paired roots and one unrestricted cube direction

For an arbitrary two-coloring \(g\) of \(Q_m\), let \(A_0(g)\) be the roots admitting full antipodal geodesics with words \(0^*1^*\), and let \(A_1(g)\) use words \(1^*0^*\). Define \(P(g)=A_0(g)\cap A_1(g)\). A *partial reader coloring* has, in every direction \(i\), either a constant edge-color function or one of the form \(a_i+x_{r(i)}\) with \(r(i)\ne i\).

**Lemma (leaf insertion).** If a new direction is appended to an arbitrary colored \(Q_d\), all previous direction colors are independent of its bit, and the new-direction color function is arbitrary, then
\[
\boxed{P(g)\times\mathbb F_2\subseteq P(g^+).}
\tag{PR1}
\]
*Proof.* At each root in \(P(g)\), choose paths with color words \(0^*1^*\) and \(1^*0^*\). Insert the new-direction step at the zero-to-one division in the first path and the one-to-zero division in the second. Either value of the inserted color preserves each respective monotone word. The remaining edge colors do not change after the insertion because they are independent of the new bit. Both constructions work from either new-bit starting value. \(\square\)

**Theorem (partial reader paired-root census).** Given a partial reader coloring \(g\) of \(Q_m\), draw a directed arc \(i\to r(i)\) for each nonconstant direction \(i\). Let its directed cycles have lengths \(L_1,\ldots,L_s\ge2\). Then
\[
\boxed{
|P(g)|\ge2^m\prod_{\nu=1}^s(1-2^{1-L_\nu})
\ge 2^{\lceil m/2\rceil}.}
\tag{PR2}
\]
*Proof.* Every weak component of this partial functional graph is either a directed cycle with trees feeding into it or a constant-direction sink with trees feeding into it. A reader cycle of length \(L\) is an antipodally odd one-reader coloring and has \(2^L-2\) roots supporting monochromatic full geodesics of both colors, by the root census proved above. A constant one-dimensional sink has both of its roots in \(P\), because every one-letter word qualifies for either monotone orientation. Attach the remaining tree vertices outward from the cycle or sink. Each new direction reads a previously present bit, while all earlier direction colors are independent of its own bit, so the leaf-insertion lemma doubles the paired-root count. Different weak components have disjoint dependencies, and the Cartesian factorization of paired roots multiplies their counts. This yields the product in (PR2). There are at most \(\lfloor m/2\rfloor\) directed cycles, and each cycle factor is at least \(1/2\); the second inequality follows. \(\square\)

**Theorem (NORI1 with one unrestricted direction).** Let \(c\) be a legal antipodally odd coloring of \(Q_n\), \(n\ge2\). Suppose some direction \(h\) has an arbitrary antipodally odd edge-color function, but for every other direction \(i\ne h\),
\[
\boxed{c_i(x)=a_i+x_{r(i)},\qquad r(i)\ne i,}
\tag{PR3}
\]
with \(r(i)=h\) permitted. Then \(c\) possesses a monochromatic antipodal full geodesic. If the reader cycles of the coloring induced on the lower \(h\)-facet have lengths \(L_1,\ldots,L_s\), the number of unoriented monochromatic-zero full geodesics satisfies
\[
\boxed{
F_n(c)\ge2^{n-2}\prod_{\nu=1}^s(1-2^{1-L_\nu})
\ge2^{\lceil(n-1)/2\rceil-1}.}
\tag{PR4}
\]

*Proof.* Fix the \(h\)-bit to zero and let \(g\) be the horizontal coloring of that facet. A direction \(i\) reading \(h\) becomes constant, while every other direction remains a one-bit reader. Thus \(g\) is a partial reader coloring, and (PR2) applies to its paired roots. For each antipodal pair \(\{y,\bar y\}\subseteq P(g)\), the two \(h\)-edges above \(y,\bar y\) have opposite colors, so one is zero. Both roots lie in \(A_0(g)\); the universal bridge-splice bijection consequently constructs a monochromatic-zero full geodesic crossing the chosen zero edge. Different selected antipodal root pairs give different crossing edges, hence distinct full geodesics. Therefore \(F_n(c)\ge|P(g)|/2\). Substitute (PR2) with \(m=n-1\). \(\square\)

**Necessary complexity of any counterexample.** Every hypothetical bad legal coloring must have at least two direction functions that are not signed one-bit readers. Equivalently, at least two directions have nonzero Fourier mass at odd degrees at least three: a Boolean antipodally odd function with only degree-one Fourier terms is a signed singleton character. This is a dimension-uniform support condition on the nonlinear part of an obstruction, complementary to the quadratic spectral separation theorem.

The statement permits the exceptional direction to depend in any way on all other cube bits. Neither connectivity nor bounded dimension is assumed for the remaining reader graph. The case of two or more arbitrary direction functions is not settled here.
