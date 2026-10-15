## Switch-Filtered Chains and Obstructions

### Dimension-simple modifications of the Wu–Yang obstruction

Wu and Yang's chain-level Borsuk–Ulam proof of the unrestricted monochromatic **antipodal path** theorem (arXiv:2607.19276, Sections 2 and 5) begins with ordinary red connected components. That quotient permits concatenating red paths that repeat cube dimensions. The aim here is to retain dimension-simplicity throughout, while replacing the component-pair rook labeling and preserving the original freely chosen geodesic root. The two constructions below give rigorous entry points and expose the remaining topological obstruction.

#### 1. Geodesic reachability replaces ordinary components

Let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1-c(e)\). Use 0 for red and 1 for blue. For any cube vertex \(x\), define
\[
R(x)=\{y\in Q_n:\text{a red shortest path from }x\text{ to }y\text{ exists}\}.
\tag{1}
\]
A shortest cube path uses each of its dimensions once. Write \(\bar x=x\oplus\mathbf1\), \(H_{i,b}=\{y:y_i=b\}\), and \(x^i=x\oplus e_i\).

**Theorem 1 (two-cone meeting criterion).** The following statements are equivalent for each specified root \(x\):

(a) A red full antipodal geodesic begins at \(x\).

(b) There exists \(y\in R(x)\cap R(\bar x)\).

(c) There is a subset \(S\subseteq[n]\) such that a red path from \(x\) to \(x\oplus\mathbf1_S\) traverses precisely \(S\), and a blue path from \(x\) to \(x\oplus\mathbf1_{S^c}\) traverses precisely \(S^c\).

*Proof.* Any red antipodal geodesic can be split at a vertex \(y\), and reversing its second part gives red shortest paths from both \(x\) and \(\bar x\) to \(y\). Conversely, given \(y\in R(x)\cap R(\bar x)\), let \(S=\{i:x_i\ne y_i\}\). A shortest path from \(x\) to \(y\) uses the dimensions of \(S\) once, and a shortest path from \(\bar x\) to \(y\) uses those of \(S^c\) once. Concatenate the first with the reverse of the second: it is a red \(n\)-edge geodesic from \(x\) to \(\bar x\). Under the antipodal map, reversal of the second red path gives a blue shortest path from \(x\) to \(x\oplus\mathbf1_{S^c}=\bar y\). This gives (c), and reversing the construction gives (b). \(\square\)

**Proposition 2 (rank-preserving transport across a colored edge).** If \(c(\{x,x^i\})=0\), then
\[
R(x^i)\cap H_{i,x_i\oplus1}\subseteq R(x),
\qquad
R(x)\cap H_{i,x_i}\subseteq R(x^i).
\tag{2}
\]
If \(c(\{x,x^i\})=1\), the same inclusions hold with \(x,x^i\) replaced by \(\bar x,\overline{x^i}\).

*Proof.* Suppose \(y\in R(x^i)\cap H_{i,x_i\oplus1}\). A red shortest path from \(x^i\) to \(y\) avoids dimension \(i\). Prepending the red edge \(x\to x^i\) gives a red shortest path from \(x\) to \(y\). The other inclusion follows symmetrically by prepending \(x^i\to x\) to a path avoiding \(i\). If the given edge is blue, its antipodal edge is red, so the preceding argument applies there. \(\square\)

Consequently, a hypothetical coloring without any monochromatic antipodal geodesic gives pairs
\[
q(x)=(R(x),R(\bar x)),\qquad q(\bar x)=(R(\bar x),R(x)),
\tag{3}
\]
whose entries are disjoint by Theorem 1. Along a red edge, the first entries overlap and obey the rank-sensitive inclusions (2); along a blue edge the second entries do so. This is a set-valued counterpart of the Wu–Yang component-pair rook labeling, retaining the ranks of joined dimension sets.

**Proposition 3 (intersection alone cannot replace rook equality).** If \(n\ge3\), put
\[
R_1(x)=\{x\}\cup\{x^i:c(\{x,x^i\})=0\}.
\tag{4}
\]
For every antipodally odd coloring of \(Q_n\), the pair labeling \(q_1(x)=(R_1(x),R_1(\bar x))\) has disjoint entries, is swapped by antipodality, and has the property that across each cube edge either its first entries or its second entries intersect. Therefore these three conditions, without geodesic-extension closure such as (2), can hold even when a monochromatic antipodal geodesic exists.

*Proof.* The two sets in a pair are contained in Hamming balls of radius one about antipodal vertices, whose centers are distance \(n\ge3\) apart; the balls are disjoint. An antipodal vertex swaps the entries. If an edge is red, its two endpoints occur in both neighboring first-entry sets. If it is blue, its antipodal edge is red and the same assertion holds for the neighboring second-entry sets. \(\square\)

The critical extra structure beyond Wu–Yang's rook relation is thus **rank-preserving extension of geodesic witnesses**. Ordinary connected-component equality loses this structure; mere intersection of set labels is insufficient.

#### 2. A dimension-simple equivariant labeling of Coxeter chambers

Let \(n\ge4\). The type-\(B_n\) spherical Coxeter complex is a triangulation of \(S^{n-1}\). Its chambers are labeled by \((x,\pi)\), with \(x\in\mathbb F_2^n\) and \(\pi\in S_n\); the chamber represents the full antipodal geodesic \(P(x,\pi)\) using every dimension once. Negation takes \((x,\pi)\) to \((\bar x,\pi)\).

Two chambers share a facet precisely when one of the following holds: (i) the root changes from \(x\) to \(x\oplus e_{\pi_1}\), with the dimension order unchanged; or (ii) two consecutive dimensions in the order are interchanged, with the root unchanged.

For a full geodesic write \(w=(w_1,\ldots,w_n)\) for its edge colors, and let \(s_k(w)\in[k,n-1]\) be the position of its \(k\)-th color change, when it exists. If a coloring had no monochromatic full antipodal geodesic at any root, **every** full-geodesic word would have at least two changes: a one-change word can be cyclically root-slid at its sole change into a monochromatic word, and a zero-change word is already monochromatic. Under this hypothetical assumption define
\[
\ell(x,\pi)=(-1)^{w_1(x,\pi)}e_{s_2(w(x,\pi))}
\in\{\pm e_2,\ldots,\pm e_{n-1}\}\subset\mathbb R^{n-2}.
\tag{5}
\]

**Theorem 4 (second-switch labeling on the Coxeter dual 1-skeleton).** Under the hypothetical absence of monochromatic full antipodal geodesics, the labeling (5) has the following properties:

(i) It is antipodally odd: \(\ell(\bar x,\pi)=-\ell(x,\pi)\).

(ii) Any two chambers sharing a facet receive nonopposite labels.

(iii) Hence, on the 1-skeleton of the dual type-\(B_n\) Coxeter cell decomposition of \(S^{n-1}\), linear interpolation along dual edges yields a continuous antipodally equivariant map to the crosspolytope boundary \(S^{n-3}\).

*Proof.* Complementing the starting vertex complements all word bits under antipodal oddness; it preserves every change position while reversing the sign in (5), proving (i).

Consider two adjacent chambers. If the facet move flips the sign of the first dimension, the two geodesics traverse the same undirected first edge, so their first word bits agree. If it interchanges dimensions in positions \(i,i+1\) with \(i\ge2\), their first edges also agree. Thus their labels have the same sign in both cases and cannot be opposites.

It remains to exchange the first two dimensions. The two geodesics have color words \(w,w'\) agreeing in positions \(j\ge3\), since they reach the same vertex after the two exchanged steps and then traverse identical edges. If their first bits also agree, their labels have the same sign. Otherwise assume for contradiction that their second switches occur at the same index \(r\ge2\). Then each word has two switches among its first \(r\) comparisons, so
\[
w_1\oplus w_{r+1}=0=w'_1\oplus w'_{r+1}.
\]
But \(w_{r+1}=w'_{r+1}\), while \(w_1\ne w'_1\), a contradiction. This proves (ii).

The dual cellulation has one vertex per Coxeter chamber and one edge per shared chamber facet. Each label in (5) is a vertex of the \((n-2)\)-dimensional crosspolytope; any pair of nonopposite vertices spans an edge of its boundary. Linear extension along dual edges therefore gives the required odd continuous map of 1-skeleta. \(\square\)

The same argument applies to a signed \(k\)-th-switch label for every \(k\ge2\), provided each word contains at least \(k\) switches. The second-switch choice is the one supplied by the absence of monochromatic full geodesics and has only \(n-2\) absolute labels.

**Corollary 5 (extension through the lower skeleton).** For \(n\ge5\), the map in Theorem 4 extends antipodally equivariantly over the \((n-3)\)-skeleton of the dual Coxeter cell complex.

*Proof.* The target \(S^{n-3}\) is \((n-4)\)-connected. Inductively, for each dual \(j\)-cell with \(2\le j\le n-3\), its attaching map has domain \(S^{j-1}\), and \(\pi_{j-1}(S^{n-3})=0\). Extend over representatives of antipodal cell pairs and define the other extensions by equivariance. The antipodal action is free on the spherical cellulation, so cells occur in distinct antipodal pairs. \(\square\)

#### 3. The first missing cellwise compatibility

Even though facet-adjacent chambers receive nonopposite second-switch labels, chambers meeting in a codimension-two Coxeter face can receive opposite labels. The following witness demonstrates why Theorem 4 does not automatically extend by radial coning over all dual cells.

**Proposition 6 (codimension-two warning).** In \(Q_4\) there is an antipodally odd edge coloring for which the chambers with root \(0000\) and orders \((1,2,3,4)\) and \((2,3,1,4)\) have respective words
\[
(1,0,1,0)\quad\text{and}\quad(0,1,0,0).
\]
Both have a second switch at position \(2\), so their labels in (5) are \(-e_2\) and \(+e_2\). Yet their type-\(B_4\) chambers meet at the face where the first three absolute-value magnitudes are equal, a codimension-two face.

*Proof.* Start at \(0000\), and specify the following seven undirected edge colors (bits index dimensions \(1,2,3,4\)):
\[
\begin{array}{c|c|c}
\text{edge start}&\text{dimension}&\text{color}\\ \hline
0000&1&1\\
1000&2&0\\
1100&3&1\\
1110&4&0\\
0000&2&0\\
0100&3&1\\
0110&1&0
\end{array}
\]
No two of these edges are antipodal (their dimension names differ or, for parallel edges, at least one other dimension has matching endpoint bits). Give each antipodal edge the complementary bit and color the remaining antipodal pairs arbitrarily. The specified paths have the displayed words. Their orders differ only by permutations of the first three dimensions, so their chambers are incident with the same codimension-two face of the type-B arrangement. \(\square\)

This example asserts a **local obstruction to a naive radial extension**, not a counterexample to NORI1: other root-and-order flags may contain monochromatic geodesics. A full chain-map construction must provide compatible fillings of dual cells even when their sets of chamber labels include opposite vectors. This is the proper analogue of Wu–Yang's dependent-radial cancellation and rook-gallery rank bound, rather than an assumption that all cell labels lie in one positive cone.

#### 4. The revised proof target

Wu and Yang create an equivariant augmentation-preserving chain map from a sphere of dimension \(K-1\) to one of dimension \(K-2\). Their Freudenthal paths use distinct dimensions, but the *component-pair reduction* forgets this rank constraint. Theorems 1–4 replace the lost information by rooted red reachability and by an odd second-switch label on complete type-B chambers. Both approaches preserve arbitrary starting roots and all cube dimensions.

The immediate open obligation is to produce a **color-consistent equivariant extension of the second-switch 1-skeleton map to the full dual cell chain complex**, or an analogous chain assignment built from the rank-preserving inclusions (2). Such a full extension would contradict the Borsuk–Ulam obstruction, since it would give an antipodally equivariant map \(S^{n-1}\to S^{n-3}\). Corollary 5 already provides the extension through the \((n-3)\)-skeleton; the substantive obstructions begin in dimension \(n-2\).

This work is targeted at the unrestricted NORI1 geodesic problem. Boundary tournaments remain a required eventual specialization of a unified theorem, but additional restricted coloring families and finite-order computations are not proposed as the proof mechanism.

### Two-end localization via an equivariant acyclic carrier

Continue the dimension-simple second-switch construction of Article XIV. Let \(n\ge4\), and assume hypothetically that every full rooted antipodal geodesic has at least two switches. Each type-\(B_n\) chamber \(g=(x,\pi)\) receives
\[
L(g)=(-1)^{w_1(g)}e_{s_2(g)}
\in \partial\mathcal O,\qquad
\partial\mathcal O\cong S^{n-3},
\tag{1}
\]
where \(\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}\). The labeling is antipodally odd, and adjacent chambers have nonopposite labels; hence it extends linearly along the dual Coxeter 1-skeleton.

Write \(s_0\) for the generator flipping the sign of the first dimension, and \(s_i\) (\(1\le i<n\)) for exchanging dimensions in positions \(i,i+1\). A dual Coxeter cell \(D=gW_J\) is indexed by a parabolic coset with \(J\subseteq\{0,\ldots,n-1\}\), and its vertices are the chambers in that coset.

**Theorem 1 (fixed-terminal-edge hemisphere).** Let \(\mathcal P\) be any family of complete rooted geodesics such that every member traverses the same undirected edge in its **final** step. If each word has at least two switches, the labels (1) of all members lie in one closed hemisphere of the target crosspolytope sphere. Specifically, if the common final-edge color is \(b\), then
\[
L(\mathcal P)\subseteq
H_b:=\partial\mathcal O\cap
\{z:(-1)^b z_{n-1}\ge0\}.
\tag{2}
\]
This hemisphere is a closed \((n-3)\)-ball. Any boundary map built from these labels and carried inside \(H_b\) admits a filling within the same hemisphere.

*Proof.* A label with second-switch index \(r<n-1\) has zero component along \(e_{n-1}\). If the second switch is at \(r=n-1\), then the full path has two switches and therefore \(w_1=w_n=b\), giving label \((-1)^b e_{n-1}\). Thus no label has the excluded opposite sign of the last axis. The crosspolytope boundary is the union of two closed hemispherical balls cut out by the last-axis hyperplane, and each is contractible. \(\square\)

**Theorem 2 (equivariant acyclic carrier on two-end-stable parabolic cells).** Let \(X_{\mathrm{good}}\) be the union of the closed dual Coxeter cells \(D=gW_J\) satisfying at least one of
\[
1\notin J,\qquad\text{or}\qquad 0\notin J\text{ and }n-1\notin J.
\tag{3}
\]
This is an antipodally invariant subcomplex containing the entire dual 1-skeleton. Under the same hypothetical assumption, the signed second-switch map on its vertices and dual edges extends to an antipodally equivariant continuous map
\[
F_{\mathrm{good}}:X_{\mathrm{good}}\longrightarrow S^{n-3}.
\tag{4}
\]
More precisely the extension admits a family of contractible target carriers, nested under inclusion of source cells, and therefore induces an equivariant augmentation-preserving chain map on the cellular chains of \(X_{\mathrm{good}}\).

*Proof.* If \(1\notin J\), all generators in \(J\) preserve the same initial undirected cube edge: \(s_0\) interchanges its endpoints, and the swaps \(s_i\) for \(i\ge2\) preserve both root and first dimension. Hence the first color bit \(a\) is fixed over the cell, and all its second-switch labels lie in the simplex
\[
\Delta_a=\operatorname{conv}\{(-1)^a e_2,\ldots,(-1)^a e_{n-1}\}
\subset\partial\mathcal O.
\tag{5}
\]

If \(0,n-1\notin J\), then the root and the last dimension are fixed throughout the cell. All permutations in this parabolic coset merely rearrange the first \(n-1\) dimensions, so the endpoint just before the last step is also fixed. Hence its last undirected edge, with color \(b\), is common to every chamber in the cell. Theorem 1 supplies the contractible carrier \(H_b\).

We now choose carriers compatible with **all** face inclusions, including intersections of these two classes of cells. For a cell with only the first-edge invariance, choose \(\Delta_a\). For a cell with last-edge invariance but no first-edge invariance, choose \(H_b\). For a cell with both invariances, choose \(\Delta_a\) if \(a=b\), and otherwise choose the face
\[
\Delta_a'=\operatorname{conv}
\{(-1)^a e_2,\ldots,(-1)^a e_{n-2}\}.
\tag{6}
\]
When \(a\ne b\), no vertex label on that cell can use \(e_{n-1}\), since a second switch at \(n-1\) would force \(w_1=w_n\). Therefore every vertex label lies in the selected carrier. All selected carriers are nonempty and contractible.

Let \(D'\) be a face of \(D\). Fixedness of either terminal edge on \(D\) is inherited by \(D'\), with the same bit. If \(D\) has a first-edge carrier, the carrier of \(D'\) is equal to it or one of its faces. If \(D\) has a last-edge hemisphere, the carrier of \(D'\) is either the same hemisphere or a first-color simplex lying inside it; the exclusion in (6) is precisely what guarantees this inclusion when the two endpoint bits differ. Hence the carriers are nested under face inclusion.

The antipodal involution complements first-edge and last-edge colors, and sends every selected carrier to its negative, so the carrier assignment is equivariant. On 0-cells the vertex labels lie in their assigned carriers; on 1-cells their nonopposite endpoint labels span target edges lying in those carriers. Inductively extend an attaching sphere over each higher-dimensional dual cell inside its contractible carrier, choosing representatives of free antipodal cell pairs and translating the extensions by the antipodal map. This constructs (4), with its prescribed 1-skeleton values. Passing to induced cellular chains, or working directly with compatible singular chains inside the carriers, produces an equivariant augmentation-preserving chain map. \(\square\)

**Corollary 3 (where the remaining obstruction can live).** The complement of \(X_{\mathrm{good}}\) among the dual Coxeter cells consists only of cells whose parabolic type \(J\) satisfies
\[
\boxed{1\in J\quad\text{and}\quad(0\in J\ \text{or}\ n-1\in J).}
\tag{7}
\]
In particular, the entire root-preserving parabolic complex that permutes the first \(n-1\) dimensions while fixing the last edge admits the extension of Theorem 2. The rank-two \(s_1,s_2\) braid hexagons are a special case of this last-edge filling, whereas the commuting square \(\{s_1,s_3\}\) in \(B_4\) is outside it, because \(s_3=s_{n-1}\) changes the last edge.

**Research significance and limits.** Wu and Yang's chain-level argument requires a globally equivariant chain map into a sphere of smaller dimension. Theorem 2 constructs a topologically and chain-theoretically valid part of such a map for the unrestricted dimension-simple cube-geodesic flags. The remaining cells must be filled compatibly with the already fixed boundary chains, while retaining the required rank-sensitive coloring relations. It is not legitimate simply to cone them in arbitrary target hemispheres: some have opposite labels and no common fixed first or last edge. The central proof obligation has therefore been localized simultaneously to an **initial exchange** and one of the **two ends of the complete path**. The theorem does not by itself prove NORI1 or settle the corresponding boundary-tournament one-switch conjecture.

### Primary projective obstruction and root-slide monodromy in dimension-simple Coxeter chains

This subsection continues the signed-second-switch construction and the acyclic-carrier theorem for two-end-stable parabolic cells (Article XIV, preceding Subsections 18, 22, and 23). Its point is an **all-dimensional obstruction localization**: all lower-dimensional extension problems can be solved, and the first unavoidable failure defines a cohomology class Poincare dual to the same root-slide monodromy that arises in the cube's Coxeter rotation. Unlike a small-rank calculation, the result is uniform in \(n\).

Let \(n\ge4\). Write \(X\) for the dual CW decomposition of the type-\(B_n\) Coxeter complex on \(S^{n-1}\). Its vertices are complete rooted antipodal cube geodesics \(g=(x,\pi)\), and its closed cells are the parabolic residues \(gW_J\), where \(J\subseteq\{0,\ldots,n-1\}\) and \(\dim(gW_J)=|J|\). The central antipodal involution acts freely and cellularly, with quotient \(Y=X/\langle-\rangle\cong\mathbb{RP}^{n-1}\).

Assume hypothetically that an antipodally odd undirected cube-edge coloring has **no** monochromatic full antipodal geodesic. Each complete geodesic then has at least two switches. Let \(w(g)\) be its \(n\)-bit edge word, let \(s_2(g)\in\{2,\ldots,n-1\}\) be the position of its second switch, and define
\[
\ell(g)=(-1)^{w_1(g)}e_{s_2(g)}
\in\partial\mathcal O\cong S^{n-3},\qquad
\mathcal O=\operatorname{conv}\{\pm e_2,\ldots,\pm e_{n-1}\}.
\tag{1}
\]
The adjacent-chamber nonopposition lemma already established in Article XIV gives an antipodally equivariant map on \(X^{(1)}\), sending each dual edge into the target crosspolytope boundary. The two-end-stable extension theorem from the preceding subsection gives an equivariant extension over the subcomplex
\[
X_{\mathrm{good}}=
\bigcup\{gW_J:1\notin J\ \text{or}\ \{0,n-1\}\cap J=\varnothing\}.
\tag{2}
\]
This subcomplex contains \(X^{(1)}\).

**Theorem 1 (primary-obstruction localization).** There is an antipodally equivariant map
\[
F:X_{\mathrm{good}}\cup X^{(n-3)}\longrightarrow S^{n-3}
\tag{3}
\]
agreeing with the signed-second-switch map on vertices and dual edges and agreeing with the previously constructed map on \(X_{\mathrm{good}}\). For each cell \(D=gW_J\) of dimension \(n-2\), let
\[
o(D)=\deg_2\!\left(F|_{\partial D}:\partial D\cong S^{n-3}\longrightarrow S^{n-3}\right).
\tag{4}
\]
This descends to a mod-two cellular \((n-2)\)-cocycle \(o\) on \(Y\), whose cohomology class is
\[
\boxed{[o]=u^{n-2}\ne0\in H^{n-2}(\mathbb{RP}^{n-1};\mathbb F_2),}
\tag{5}
\]
where \(u\) is the degree-one generator. Thus some dimension-\((n-2)\) parabolic residue has a boundary map of odd degree and cannot be filled equivariantly in the proposed target. Moreover every such residue is of one of the following two parabolic types, described by the **two omitted simple generators**:
\[
\boxed{
\begin{array}{ll}
\{0,j\},& 2\le j\le n-2,\\[2pt]
\{i,j\},&2\le i<j\le n-1.
\end{array}}
\tag{6}
\]
There are \(n(n-3)/2\) possible omitted-generator pairs in (6), compared with \(\binom n2\) pairs in total. For \(n=4\), the two types are respectively \(\{0,2\}\) and \(\{2,3\}\).

*Proof.* The target sphere \(S^{n-3}\) is \((n-4)\)-connected. Attaching a \(k\)-cell with \(k\le n-3\) to a partially defined map presents an attaching sphere of dimension \(k-1\le n-4\), so its boundary map extends. The antipodal involution acts freely on the cells, and extensions may be chosen on one cell in each antipodal pair and transported to the partner. Starting from the compatible map on \(X_{\mathrm{good}}\) therefore yields (3) without altering the already defined cells.

An equivariant map into \(S^{n-3}\), viewed as the unit sphere of the sign representation \(\mathbb R^{n-2}\), is a nowhere-zero section over \(Y\) of the rank-\((n-2)\) real vector bundle
\[
E=(n-2)\gamma,
\tag{7}
\]
where \(\gamma\) denotes the tautological real line bundle over \(\mathbb{RP}^{n-1}\). The mod-two primary obstruction to extending that section over the \((n-2)\)-cells is represented by the degree cocycle (4), and its cohomology class is the top Stiefel-Whitney class
\[
w_{n-2}(E)=w_{n-2}((n-2)\gamma)
=u^{n-2},
\tag{8}
\]
because \(w(E)=(1+u)^{n-2}\). The standard cohomology ring \(H^*(\mathbb{RP}^{n-1};\mathbb F_2)=\mathbb F_2[u]/(u^n)\) makes this class nonzero. This proves (5), including the cocycle relation, and forces an odd-degree boundary on at least one cell.

For each cell of \(X_{\mathrm{good}}\), the map already extends across the cell, so its degree obstruction vanishes. Thus any cell with \(o(D)=1\) has \(1\in J\) and at least one of \(0,n-1\) belonging to \(J\). As \(|J|=n-2\), the complement of \(J\) consists of two generator indices. Avoiding the omission of \(1\), and avoiding the simultaneous omission of \(0,n-1\), gives precisely (6). Counting yields \((n-3)+\binom{n-2}{2}=n(n-3)/2\). \(\square\)

**Theorem 2 (obstruction as a projective one-cycle).** The mod-two Poincare dual of the cocycle \(o\) is a cellular one-cycle \(Z_o\) in a dual subdivision of \(Y\), whose homology class is the unique nonzero element of
\[
\boxed{H_1(\mathbb{RP}^{n-1};\mathbb F_2)\cong\mathbb F_2.}
\tag{9}
\]
It is homologous to the loop obtained from **\(n\) Coxeter root slides**, namely the path from any chamber \(g=(x,\pi)\) to \(-g=(\bar x,\pi)\) under
\[
T(x;i_1,\ldots,i_n)=(x\oplus e_{i_1};i_2,\ldots,i_n,i_1),
\quad T^n g=-g,
\tag{10}
\]
after projection to \(Y\).

*Proof.* In the closed \((n-1)\)-manifold \(Y\), cellular Poincare duality sends a mod-two \((n-2)\)-cocycle to a dual one-cycle. By (5),
\[
[Z_o]=u^{n-2}\frown[Y]\ne0
\quad\text{in }H_1(Y;\mathbb F_2).
\tag{11}
\]
A path on \(S^{n-1}\) joining a point to its antipode projects to a loop representing the nontrivial element of the fundamental group and hence of mod-two first homology of \(\mathbb{RP}^{n-1}\). The \(n\) root slides in (10), with each Coxeter multiplication resolved into adjacent chamber edges, provide such a path. Therefore their projected loop and \(Z_o\) represent the same nonzero homology class. \(\square\)

**Interpretation and proof target.** The nonextendibility of the signed-second-switch map is now concentrated in rank-\((n-2)\) residues of the two types (6), and the parity of their boundary degrees globally forms a projective one-cycle with the *same homology class as root-slide half-turn monodromy*. The theorem applies to any hypothetical no-monochromatic-geodesic coloring and relies only on the existing adjacent-chamber lemma, two-end acyclic carriers, and classical obstruction theory. It does **not** rule out such a coloring by itself: the nonzero class (5) is a consequence of the antipodal topology, not a contradiction.

To finish a dimension-simple adaptation of Wu–Yang, it would suffice to prove that the **color-sensitive incidence identities** force this degree cocycle to be null-cohomologous, or show directly that the odd-degree boundary maps of both residual types in (6) admit coherent fillings after a suitable enrichment of the target that does not destroy the dimension bound. Either statement would contradict (5). In the second formulation, the corrections must confront the projective root-slide cycle globally, rather than filling arbitrary local squares in isolation.

### All-rank antipodal cubical resolution and sharp projective cosystoles

The canonical exchange disks of Article XIV, Subsection 28, are the degree-two part of a uniform **all-rank cubical chain construction**. The construction preserves the set of free dimensions and realizes every nonzero projective cohomology class \(u^k\) by a fixed-dimension incidence cocycle with the minimum possible support. Its degree-one term is a full antipodal geodesic. No edge-color restriction is imposed.

Work with cubical cellular chains over \(\mathbb F_2\). Let \(Q_n=[0,1]^n\), with central antipodal involution \(\tau_n\). Put \(E_0^{(0)}=[*]\), and set \(E_k^{(n)}=0\) for \(k<0\) or \(k>n\). Recursively define
\[
E_0^{(n)}=E_0^{(n-1)}\times\{0\},
\]
\[
\boxed{E_k^{(n)}
=E_k^{(n-1)}\times\{0\}
+\tau_{n-1}E_{k-1}^{(n-1)}\times[0,1],
\qquad k\ge1.}
\tag{1}
\]

**Theorem 1 (antipodal chain resolution).** For every \(n\ge1\) and \(1\le k\le n\),
\[
\boxed{\partial E_k^{(n)}=(1+\tau_n)E_{k-1}^{(n)}.}
\tag{2}
\]
The chain \(E_k^{(n)}\) consists of \(\binom nk\) different \(k\)-faces, containing **one face for every \(k\)-element set of free dimensions**, each with coefficient one.

*Proof.* In (1), the first summand contributes the faces whose free sets omit dimension \(n\), while the second contributes those whose free sets contain \(n\); induction gives precisely one per \(k\)-subset. For the boundary identity, use the cubical product formula:
\[
\begin{aligned}
\partial E_k^{(n)}
={}&(1+\tau_{n-1})E_{k-1}^{(n-1)}\times0\\
&+\tau_{n-1}(1+\tau_{n-1})E_{k-2}^{(n-1)}\times[0,1]\\
&+\tau_{n-1}E_{k-1}^{(n-1)}\times(0+1)\\
={}&E_{k-1}^{(n-1)}\times0+
\tau_{n-1}E_{k-1}^{(n-1)}\times1\\
&+(1+\tau_{n-1})E_{k-2}^{(n-1)}\times[0,1]\\
={}&(1+\tau_n)E_{k-1}^{(n)}.
\end{aligned}
\]
For \(k=1\), replace \(\partial E_0\) by zero in the same calculation; its boundary is the sum of the origin and its antipode. \(\square\)

For any root \(x\) and permutation \(\pi\) of the \(n\) dimensions, transport \(E_k^{(n)}\) under the cube automorphism sending the standard origin to \(x\) and the standard dimension order to \(\pi\). Denote the resulting chain \(E_k(x,\pi)\). Central antipodality commutes with the transport, so (2) remains valid.

**Proposition 2 (recovering the geodesic and exchange disk).** The chain \(E_1(x,\pi)\) is the length-\(n\) antipodal geodesic \(P(x,\pi)\). The chain \(E_2(x,\pi)\) equals the canonical exchange disk
\[
\Sigma_P=\sum_{i<j} F_{\{d_i,d_j\}}
\left(x\oplus\bigoplus_{r=i}^{j-1}e_{d_r}\right)
\tag{3}
\]
from Subsection 28.

*Proof.* At \(k=1\), recursion (1) follows the first \(n-1\) dimensions, and then traverses the final dimension at the antipodal endpoint of the partial geodesic. At \(k=2\), its first summand supplies the squares of (3) not involving the final dimension, while its second is the antipodal image of the partial geodesic crossed with the final interval. These are precisely the squares in (3) involving the final dimension. Induct on \(n\). \(\square\)

#### Theorem 3 (canonical generators in every projective rank)

For \(1\le k\le n-1\), all \(k\)-faces of \(E_k(x,\pi)\) lie on \(B_n=\partial Q_n\). Let \(Y_n=B_n/\tau_n\cong\mathbb{RP}^{n-1}\), with quotient map \(p\), and set
\[
Z_k(x,\pi)=p_*E_k(x,\pi).
\]
Equation (2) shows that \(Z_k\) is a \(k\)-cycle. For any \(I\subseteq[n]\), \(|I|=k\), let \(K_I\) be the invariant cubical \(k\)-cochain which evaluates to one on a \(k\)-face if its free dimension set is \(I\), and zero otherwise. It descends to a cocycle \(\bar K_I\) on \(Y_n\). If \(u\in H^1(Y_n;\mathbb F_2)\) is the canonical generator, then
\[
\boxed{
[\bar K_I]=u^k,\qquad
[Z_k(x,\pi)]\ne0\in H_k(Y_n;\mathbb F_2),\qquad
\langle\bar K_I,Z_k(x,\pi)\rangle=1.
}
\tag{4}
\]

*Proof.* Each \((k+1)\)-face contains either no \(k\)-facets with free dimensions \(I\), or a pair of opposite such facets. Thus \(\delta\bar K_I=0\). By Theorem 1, each \(E_k(x,\pi)\) has one \(k\)-face with free set \(I\), so its pairing with \(K_I\), and hence the downstairs pairing in (4), is one. Both homology and cohomology in degree \(k\) of \(\mathbb{RP}^{n-1}\) are one-dimensional over \(\mathbb F_2\); their nonzero classes are the desired generators. \(\square\)

#### Theorem 4 (sharp projective cocycle support in all degrees)

For every \(1\le k\le n-1\), a cubical \(k\)-cocycle \(\eta\) representing \(u^k\) on \(Y_n\) must have nonzero values on at least
\[
\boxed{2^{n-k-1}}
\tag{5}
\]
antipodal orbits of \(k\)-faces. This bound is sharp, attained by every fixed-free-set indicator \(\bar K_I\).

*Proof.* Every projected chain \(Z_k(x,\pi)\) is a nonzero homology generator, so its pairing with \(\eta\) is one. Hence every lifted chain \(E_k(x,\pi)\) contains at least one face in the lifted support of \(\eta\). There are \(2^nn!\) rooted dimension permutations and \(\binom nk\) faces in each \(E_k\). The cube automorphism group acts transitively on the \(\binom nk2^{n-k}\) \(k\)-faces and permutes the canonical chains. Thus every fixed \(k\)-face occurs in
\[
\frac{(2^nn!)\binom nk}{\binom nk2^{n-k}}=2^kn!
\]
canonical chains, counting root-and-order choices. If the lifted support contains \(M\) faces, double counting gives
\[
2^nn!\le M\,2^kn!,\qquad M\ge2^{n-k}.
\]
All proper cube faces occur in free antipodal pairs, so downstairs there are at least \(M/2\ge2^{n-k-1}\) supported orbits. The indicator \(K_I\) is supported on the \(2^{n-k}\) faces with one prescribed free dimension set \(I\); it attains the bound. \(\square\)

**Corollary 5 (primary obstruction admits a sparse projective representative).** The primary obstruction for the signed-second-switch map in Article XIV, Subsection 25, has cohomology class \(u^{n-2}\). In the antipodal cubical cellulation, the same cohomology class has a representative \(\bar K_I\), \(|I|=n-2\), supported on only **two antipodal orbits** of \((n-2)\)-faces. This is a statement about cohomology classes in different cellulations; it does not assert that the color-dependent obstruction degrees themselves concentrate on those cells.

**Connection to the Wu–Yang adaptation.** The boundary relation (2) realizes the antipodal two-periodic free chain resolution through all dimensions on ordinary cubical faces, retaining a distinct \(k\)-dimensional support for each \(k\)-subset of dimensions. The previously identified antipodal geodesics, canonical exchange disks, and adjacent-swap three-cube corrections belong to this same chain geometry. We no longer need to invent an uncolored, rank-preserving antipodal chain system: the one in (1) is explicit. The remaining research problem is to lift its boundary relation through color-sensitive reachability and ordered-path incidence data while preserving the topological obstruction. None of the results here assumes a specialized coloring or proves the NORI1 existence conjecture.


#### Rigidity of minimum degree-one support

**Theorem 6.** A projective cubical one-cocycle representing the generator \(u\in H^1(\mathbb RP^{n-1};\mathbb F_2)\), \(n\ge3\), has at least \(2^{n-2}\) supported projective edges. Equality holds only for a whole cube-dimension edge class. More precisely, its pullback is the edge boundary of an antipodally odd sign function \(f:Q_n\to\{\pm1\}\), and
\[
|B|=2^{n-2}\left(1+\sum_{\substack{|S|\ge3\\|S|\text{ odd}}}(|S|-1)\widehat f(S)^2\right).
\]
*Proof.* The pullback is a coboundary because \(H^1(S^{n-1};\mathbb F_2)=0\). The nonzero projective period forces \(f(\bar x)=-f(x)\), so its Walsh spectrum contains only odd levels. Counting the lifted boundary edges by Boolean influence, and using Parseval, yields the formula. Equality means that \(f\) has Fourier degree one. The Boolean identity \(f^2=1\) forces at most one linear Fourier coefficient to be nonzero, making \(f=\pm(-1)^{x_i}\). Its boundary is the full dimension-\(i\) edge class. \(\square\)

**Theorem 7 (transversal equality).** A set of projective edges meeting every complete dimension-simple Petrie cycle has at least \(2^{n-2}\) members. At equality it must be one complete dimension class.
*Proof.* Each projective edge occurs in \((n-1)!\) Petrie cycles, and there are \(2^{n-2}(n-1)!\) cycles. Equality in double counting means every cycle meets the set once. The symmetric difference of two cycles obtained by adjacent-dimension exchange is a projective square boundary, so the edge set has zero square coboundary. It has odd period along every Petrie cycle, hence represents \(u\). Apply Theorem 6. \(\square\)

The Fourier identity also gives spectral stability: support at most \((1+\varepsilon)2^{n-2}\) implies total Fourier mass above degree one at most \(\varepsilon/2\).


### Color-filtered Freudenthal chains and exchange defects

Wu and Yang's unrestricted Freudenthal subdivision sums all maximal monotone simplices of a cubical face, so each internal facet cancels in a pair of adjacent permutations. Keeping only those simplices whose complete ordered edge path is monochromatic preserves dimension-simplicity, but introduces a computable obstruction to this cancellation.

Let \(F\) be a \(d\)-dimensional cubical face rooted at a corner \(x\). For each dimension order \(\pi\), let
\[
\sigma_\pi=[v_0=x,v_1,\ldots,v_d],\quad
v_k=x\oplus e_{\pi_1}\oplus\cdots\oplus e_{\pi_k}.
\]
For a bit \(a\), let \(\chi_a(e)=1\) if the undirected cube edge \(e\) has color \(a\), and \(0\) otherwise. Put
\[
r_a(\pi)=\prod_{k=1}^{d}\chi_a(v_{k-1},v_k),\qquad
M_a(F,x)=\sum_{\pi}r_a(\pi)\sigma_\pi
\]
over \(\mathbb F_2\). Every simplex with nonzero coefficient corresponds to a monochromatic geodesic using each of the face's dimensions once.

**Theorem (all-rank exchange-defect identity).** Let \(s_j\pi\) exchange positions \(j,j+1\), \(1\le j<d\), and let \(\tau_{\pi,j}\) be the internal facet shared by \(\sigma_\pi\) and \(\sigma_{s_j\pi}\). Then the internal part of the boundary is
\[
\boxed{
D_a(F,x)=\sum_{j=1}^{d-1}\sum_{\{\pi,s_j\pi\}}
(r_a(\pi)+r_a(s_j\pi))\,\tau_{\pi,j}.
}
\]
If the two exchanged dimensions are \(i,h\), the paths agree up to a vertex \(u\), traverse opposite sides of the dimension-\(\{i,h\}\) square, rejoin at \(u^{ih}=u\oplus e_i\oplus e_h\), and agree thereafter. Let \(A_\pi,B_\pi\) be the products of the red-edge indicators on the shared prefix and suffix. Then
\[
\boxed{
r_a(\pi)+r_a(s_j\pi)=A_\pi B_\pi
\left[
\chi_a(u,u^i)\chi_a(u^i,u^{ih})
+\chi_a(u,u^h)\chi_a(u^h,u^{ih})
\right].
}
\]

*Proof.* Every internal Freudenthal facet is shared by the two maximal simplices obtained by the relevant adjacent exchange, giving the first formula. The two corresponding complete paths have identical outside edges, so their selectors factor through the two alternative length-two square routes, giving the second formula. \(\square\)

**Antipodal covariance.** If \(c(\bar e)=1-c(e)\), the antipode \(A\) gives
\[
A_\#M_a(F,x)=M_{1-a}(\bar F,\bar x),
\quad
A_\#D_a(F,x)=D_{1-a}(\bar F,\bar x).
\]
This follows because antipodal translation preserves dimension order and complements each traversed bit.

**Failure of the naive filtered chain map.** Already on a square, one two-edge route may be entirely red while the other contains a blue edge; then the shared internal diagonal occurs once rather than twice in the boundary. Such local assignments can be extended antipodally in \(Q_n\) for \(n\ge3\).

Therefore the unfiltered Freudenthal cancellation from Wu and Yang does not persist when retaining only dimension-simple monochromatic certificates. Its failure is completely localized to the local square expression above, multiplied by the admissibility of the shared prefix and suffix. A proof must construct correction chains cancelling these interior defects *coherently on higher-dimensional faces*, while also treating the color-dependent exterior facets. The formula and its antipodal covariance are proved; a complete equivariant correction is not.

### Rank-two carrier homology and a switch-budget filtration

Let \(c:E(Q_n)\to\mathbb F_2\) be any undirected cube-edge coloring, \(n\ge2\). Let \(C_x=K_x^0\cup K_x^1\) denote the two-color monochromatic geodesic-prefix complex rooted at \(x\), formed in the rooted Freudenthal triangulation. All constituent paths use pairwise distinct cube dimensions.

#### 1. Fourfold carriers over a cubical square

Let \(F\) be a two-dimensional cube face, with vertices \(x,y,w,z\) in cyclic order. Regard its four boundary edge colors as a cyclic binary word, and define the geometric intersection
\[
I_F=F\cap C_x\cap C_y\cap C_w\cap C_z.
\tag{1}
\]
The four possible color patterns, up to rotating and complementing all four bits, are \(0000,0001,0011,0101\).

**Theorem 1 (rank-two intersection classification).** The intersection \(I_F\) has the following forms:
\[
\begin{array}{c|c|c}
\text{cyclic color type}&I_F\text{ up to PL homeomorphism}&
\widetilde H_0(I_F;\mathbb F_2)\\\hline
0000 &\text{filled square}&0\\
0001 &\text{filled triangle}\sqcup\text{two isolated points}&\mathbb F_2^2\\
0011 &\text{two isolated points}&\mathbb F_2\\
0101 &\varnothing&0
\end{array}
\tag{2}
\]
For the empty case, nonemptiness rather than reduced zeroth homology is the obstruction. In particular, contractibility of all the \(C_v\) and their neighboring-edge bridges does not imply acyclicity of their fourfold square intersections. These obstructions occur already in the full-rank, unrestricted local cube coloring data.

*Proof.* Each root \(v\in F\) has the two adjacent square edges in \(C_v\). It contains a two-simplex joining \(v\), an intermediate neighboring vertex \(u\), and the opposite corner \(v^{ij}\) precisely when the two consecutive edges \(vu,uv^{ij}\) have the same color. Thus its restriction \(C_v\cap F\) is the union of its two incident edges and zero, one or two rooted Freudenthal triangles.

For \(0000\), both two-step routes from every corner are monochromatic; all four complexes contain the entire filled square.

For \(0101\), neither route is monochromatic from any root. Each restricted complex is its two incident edges. Their fourfold intersection is empty.

For \(0011\), two opposite square corners have monochromatic two-step routes in both directions, while the other two have none. The cones rooted at the latter two corners intersect only in the remaining opposite pair of square vertices; the cones at the first two corners contain both vertices, leaving precisely those two isolated points.

For \(0001\), two adjacent corners (those incident to two zero-colored edges) have both-rooted path triangles available toward the opposite corner, while the remaining two corners have only incident edge stars. Directly intersecting the two Freudenthal triangulations, which use opposite square diagonals, shows that the common part is the closed triangle with base the central zero-colored square edge and apex the crossing of the diagonals, together with the two unused square corners as isolated points. All four patterns are related by square symmetries and global complement, proving the claim. \(\square\)

The projective square-curvature cocycle already developed in this Article distinguishes \(0001\), which has odd four-edge parity, from the other patterns. But curvature alone does not detect the nonacyclic \(0011\) carrier or the empty \(0101\) carrier. The complete carrier behavior therefore contains additional information beyond that cohomology class.

#### 2. A dimension-simple filtration by switch count

For \(r\ge0\), let \(\mathcal K_x^{[r]}\) be the simplicial subcomplex generated by all geodesic prefixes beginning at \(x\) and having at most \(r\) switches in their binary edge-color words. Include the trivial prefix. Each such complex is a cone at \(x\), and the inclusions
\[
\mathcal K_x^{[0]}=C_x\subseteq\mathcal K_x^{[1]}
\subseteq\cdots\subseteq\mathcal K_x^{[n-1]}=T_x
\tag{3}
\]
retain full dimension-simplicity. If \(c\) is antipodally odd, central inversion carries \(\mathcal K_x^{[r]}\) to \(\mathcal K_{\bar x}^{[r]}\).

**Theorem 2 (filtered antipodal gluing equivalence).** For every root \(x\) and \(r,s\ge0\),
\[
\boxed{
|\mathcal K_x^{[r]}|\cap|\mathcal K_{\bar x}^{[s]}|\ne\varnothing
\iff
\text{some full antipodal geodesic from }x
\text{ has at most }r+s+1\text{ switches}.
}
\tag{4}
\]

*Proof.* The rooted Freudenthal triangulations for \(x\) and \(\bar x\) coincide as unrooted simplicial complexes. Therefore a nonempty intersection shares a cube vertex \(y\). It has witnessing geodesics \(P:x\to y\) with at most \(r\) switches and \(Q:\bar x\to y\) with at most \(s\). Their dimension supports are complementary: precisely the dimensions where \(y\) differs from \(x\), and where it agrees. Concatenate \(P\) with the reversal of \(Q\). The result uses every dimension once, and has at most \(r+s+1\) color changes, including the possible joining change.

Conversely let a full antipodal geodesic from \(x\) have \(t\le r+s+1\) switches. For \(t=0\), split it anywhere. For \(t\ge1\), choose an integer
\[
\max(0,t-1-s)\le j\le\min(r,t-1);
\]
one exists by the assumed inequality. Split the path at its \((j+1)\)-st color change. The initial piece has \(j\le r\) switches; the terminal piece has \(t-j-1\le s\). Reversing the terminal piece makes a geodesic from \(\bar x\) to the splitting vertex, which therefore lies in both required complexes. \(\square\)

**Corollary 3 (all rank-two holes fill at level one).** For every square \(F\) and each of its corners \(v\),
\[
\boxed{|\mathcal K_v^{[1]}|\cap F=F.}
\tag{5}
\]
Consequently the four level-one rooted complexes share the entire filled square, irrespective of its coloring.

*Proof.* Every length-two geodesic has at most one color switch. Both rooted Freudenthal two-simplices across the square therefore occur in \(\mathcal K_v^{[1]}\), and their union is \(F\). \(\square\)

#### 3. Wu–Yang chain-level interpretation

Theorem 1 pinpoints the first higher-dimensional failure of the contractible-bridge approach: the fourfold intersection of rank-zero root carriers may be disconnected or empty. Theorem 2 gives a faithful switch-budget calculus for correcting it. Level-one cones fill every local square while using independent dimensions, but gluing two level-one witnesses across the antipode yields only a bound of three switches, not the desired one.

A successful chain construction must therefore track its *relative switch filtration* and return an antipodal intersection to filtration bidegree \((0,0)\). It cannot merely enlarge every carrier to level one and invoke an ordinary acyclic-carrier theorem. The color-filtered Freudenthal exchange defects and the already established projective square curvature describe related local information, but no general equivariant mechanism lowering the final switch budget has yet been proved.

### Formal switch deformation and its local quadratic exchange law

Wu–Yang's Freudenthal chain is the sum of all maximal monotone simplices of a cubical face. Every such simplex represents a dimension-simple path. We deform its coefficient to retain the number of color switches, and obtain an all-rank local expression for the failure of adjacent-exchange cancellation.

Let \(F\) be a cubical face of dimension \(d\ge4\), rooted at a corner \(x\). For every order \(\pi\) of the varying dimensions, let \(\sigma_\pi\) be the corresponding Freudenthal simplex, \(w(\pi)\) its ordered edge-color word, and \(S(\pi)\) the integer count of switches. Define the chain over \(\mathbb F_2[u]\)
\[
\boxed{\mathfrak F_u(F,x)=\sum_{\pi}(1+u)^{S(\pi)}\sigma_\pi.}
\tag{1}
\]
At \(u=0\) this recovers the ordinary Freudenthal chain of Wu and Yang.

Let \(\pi'=s_j\pi\) exchange two successive dimensions, and let \(\tau_{\pi,j}\) be the common internal facet of their two simplices. Its coefficient in \(\partial\mathfrak F_u\) is
\[
E_{\pi,j}(u)=(1+u)^{S(\pi)}+(1+u)^{S(\pi')}.
\tag{2}
\]

**Theorem 1 (switch-deformation factorization).** For every adjacent exchange of complete rooted dimension orders, \(|S(\pi)-S(\pi')|\le2\). Writing \(h=\min(S(\pi),S(\pi'))\), one has
\[
\boxed{
E_{\pi,j}(u)=
\begin{cases}
0,&S(\pi)=S(\pi'),\\
u(1+u)^h,&|S(\pi)-S(\pi')|=1,\\
u^2(1+u)^h,&|S(\pi)-S(\pi')|=2.
\end{cases}}
\tag{3}
\]
For interior exchanges \(2\le j\le d-2\), the first and last edge colors remain fixed, so \(S(\pi)-S(\pi')\) is even. Consequently *all interior Freudenthal facets cancel modulo \(u^2\)*; only the two endpoint exchanges \(j=1,d-1\) may have nonzero first-order defects.

*Proof.* Adjacent exchange alters only the two edge colors in the exchanged positions. For an interior exchange, its affected three neighboring comparisons all share the same flanking bits and hence have the same parity of switch count on the two routes. Their difference is \(0\) or \(\pm2\), since each count lies between zero and three. At an endpoint exchange, at most two comparisons are affected, so the switch difference has absolute value at most two. The factorization is immediate from
\((1+u)^{h+k}+(1+u)^h=(1+u)^h((1+u)^k+1)\) for \(k=0,1,2\), together with \((1+u)^2+1=u^2\) in characteristic two. \(\square\)

**Theorem 2 (quadratic six-bit defect).** For an interior exchange write the affected word segments as
\[
(A,p,q,B)\quad\text{and}\quad(A,r,s,B).
\]
Then
\[
\boxed{
[u^2]E_{\pi,j}(u)
=A(p\oplus r)\oplus B(q\oplus s)
\oplus(p\oplus q\oplus r\oplus s)
\oplus pq\oplus rs.
}
\tag{4}
\]
This depends only on the colors of the four square edges and the two flanking edges, not on any earlier or later colors. It equals one precisely when the interior exchange changes the switch count by two.

*Proof.* Write \(k\) for the number of changes among the three comparisons in \((A,p,q,B)\), and \(k'\) for the alternative segment; both have parity \(A\oplus B\). If \(C\) denotes the number of unaffected switches, the coefficient of \(u^2\) in (2) is
\[
\binom{C+k}{2}+\binom{C+k'}{2}
=\binom k2+\binom{k'}2\pmod2,
\]
because the terms involving \(C\) cancel. With \(\delta_0=A\oplus p\), \(\delta_1=p\oplus q\), \(\delta_2=q\oplus B\), one has
\[
\binom{k}{2}\equiv\delta_0\delta_1+\delta_0\delta_2+\delta_1\delta_2
=AB\oplus Ap\oplus Bq\oplus p\oplus q\oplus pq.
\]
Add the analogous formula with \(r,s\) to obtain (4). The final assertion follows from (3). \(\square\)

**Corollary 3 (flat-square defects survive).** Put \(A=B=p=q=0\), \(r=s=1\). The two four-letter words are \(0000\) and \(0110\), with zero and two switches. The ordinary four-edge square curvature is \(p\oplus q\oplus r\oplus s=0\), but (4) equals one and
\[
E_{\pi,j}(u)=u^2.
\]
Thus the quadratic defect contains coloring information beyond the ordinary cubical square curvature.

**Theorem 4 (interior exchange integrability).** Fix a root and the first and last dimensions of a full monotone path, and consider the graph of permutations of the remaining dimensions, joined by interior adjacent exchanges. The second-order defect function on its edges is a coboundary:
\[
\boxed{\omega(\pi,\pi')=H(\pi)\oplus H(\pi'),\qquad
H(\pi)=\binom{S(\pi)}2\bmod2.}
\tag{5}
\]
Hence its sum along any commuting-square, braid-hexagon, or other closed exchange walk is zero.

*Proof.* The coefficient of \(u^2\) in (2) is precisely \(H(\pi)+H(\pi')\), and the sum telescopes around any closed walk. \(\square\)

**Scope.** These results prove local algebraic compatibility and show that the first nontrivial interior defects arise at *second order*, while endpoint exchanges may obstruct at first order. They do not show that the formal chain (1) is a chain map: the endpoint facets and the external facets of cubical faces still need correction, and higher equivariant root changes must preserve the used-dimension supports. In particular the coboundary identity (5) is an integrability condition on an exchange graph, not a globally constructed Wu–Yang chain homotopy.

### A switch-filtered Rees chain complex with a rank-preserving contraction

The formal switch-weighted Freudenthal chain of the preceding subsection is useful for locating exchange defects, but it is not a chain complex with a switch-sensitive differential. This subsection constructs one. The construction is natural for every unrestricted binary cube-edge coloring and every root, and retains dimension-simple geodesic witnesses for all its simplices.

Fix a root \(x\) of \(Q_n\), and let \(T_x\) denote the rooted Freudenthal triangulation of the entire geometric cube. For a simplex \(\tau\in T_x\), define its **minimum switch grade** by
\[
\nu_x(\tau)=\min\{\operatorname{sw}(P):
P\text{ is a rooted dimension-simple geodesic prefix from }x
\text{ and its Freudenthal simplex contains }\tau\}.
\tag{1}
\]
Every simplex of \(T_x\) occurs in some rooted saturated chain from \(x\), so this minimum exists. The prefix complexes of Article XIV satisfy
\[
K_x^{[r]}=\{\tau\in T_x:\nu_x(\tau)\le r\}.
\tag{2}
\]
The grade is nonincreasing under taking simplicial faces: if \(\eta\subseteq\tau\), then \(\nu_x(\eta)\le\nu_x(\tau)\).

Put \(R=\mathbb F_2[t]\). Define the **Rees chain complex** as the \(R\)-submodule
\[
\boxed{
\mathscr R_xC_k=
\bigoplus_{\substack{\tau\in T_x\\\dim\tau=k}}
R\cdot(t^{\nu_x(\tau)}\tau)
\subseteq C_k(T_x;\mathbb F_2)\otimes R,
}
\tag{3}
\]
and use the ordinary simplicial boundary, extended \(R\)-linearly.

**Theorem 1 (filtered chain structure).** The modules (3), together with the inherited boundary, form an augmented chain complex of free \(R\)-modules. On a weighted simplex generator,
\[
\boxed{
\partial(t^{\nu_x(\tau)}\tau)=
\sum_{\eta\lessdot\tau}
t^{\nu_x(\tau)-\nu_x(\eta)}
\bigl(t^{\nu_x(\eta)}\eta\bigr).
}
\tag{4}
\]
In particular, the boundary never increases the minimum required number of switches. The specialization at \(t=1\) gives the ordinary Freudenthal simplicial chains. The specialization at \(t=0\) gives the associated graded complex of the switch filtration, whose boundary retains only faces with the same minimum switch grade.

*Proof.* Every exponent in (4) is nonnegative by face monotonicity. Thus the ordinary boundary preserves \(\mathscr R_x\). Since it squares to zero in the ambient chain complex, it does so on this submodule. Its generators form a free \(R\)-basis. At \(t=1\), each generator maps to the corresponding unweighted simplex. At \(t=0\), the coefficient in (4) vanishes when \(\nu_x(\eta)<\nu_x(\tau)\), retaining the grade-preserving part of the boundary. This is the usual associated graded chain differential. \(\square\)

**Theorem 2 (rank-preserving filtered cone contraction).** The augmented Rees complex \(\mathscr R_xC_*\) has a chain contraction over \(R\), preserving the minimum switch grade. In particular its augmented homology vanishes, and the associated graded complex at \(t=0\) is also acyclic.

*Proof.* Every generating rooted geodesic-prefix simplex contains the apex \(x\). Hence for every simplex \(\tau\) not containing \(x\), the join \(x*\tau\) is a simplex of \(T_x\) with
\[
\boxed{\nu_x(x*\tau)=\nu_x(\tau).}
\tag{5}
\]
Indeed any admissible prefix simplex witnessing \(\tau\) already contains \(x\), so adjoining \(x\) neither creates nor removes any candidate witnesses. Define the cone operator \(h(\tau)=x*\tau\) when \(x\notin\tau\), and \(h(\tau)=0\) when \(x\in\tau\), with \(h(\varnothing)=[x]\) in the augmented complex. The standard simplicial cone identity over \(\mathbb F_2\) gives
\[
\partial h+h\partial=\mathrm{id}.
\tag{6}
\]
Equation (5) ensures that this homotopy preserves the Rees submodules and requires no extra powers of \(t\). It therefore contracts the augmented Rees chain complex over \(R\). Specializing (6) at \(t=0\) also contracts the associated graded complex. \(\square\)

If the coloring is antipodally odd, antipodal inversion carries the rooted switch filtration for \(x\) to that for \(\bar x\), because every path's color word is complemented without altering its switches. Thus it supplies natural isomorphisms \(\mathscr R_xC_*\to\mathscr R_{\bar x}C_*\).

#### A deterministic one-edge switch update

Let \(xy\) be a cube edge of color \(a\) in dimension \(i\). Suppose \(P\) is a nonempty dimension-simple geodesic prefix from \(y\) avoiding dimension \(i\), with \(r\) switches, first edge color \(b\), and last edge color \(\beta\). Prepending \(x\to y\) preserves independence and yields
\[
\operatorname{sw}\bigl((x,y)\cdot P\bigr)=r+(a\oplus b).
\tag{7}
\]
For every nonempty binary word, \(b\oplus\beta=r\bmod2\). Hence
\[
\boxed{
\operatorname{sw}\bigl((x,y)\cdot P\bigr)
=r+\bigl(a\oplus\beta\oplus(r\bmod2)\bigr).
}
\tag{8}
\]
The last color remains \(\beta\). For an empty \(P\), prepending simply creates a one-edge path of color \(a\), with zero switches.

**Proposition 3 (terminal-color state suffices for root extension).** The integer switch count \(r\), the terminal color \(\beta\), and the prepended edge color \(a\) determine both the new switch count and the new terminal color. No independent initial-color state is needed once the switch parity is recorded.

*Proof.* The bit of the first edge of \(P\) is \(b=\beta\oplus(r\bmod2)\). Substitute this into (7). The terminal edge does not change on prepending. \(\square\)

#### What this resolves and what it does not

The Rees model provides an honest filtered chain complex, with a boundary and contraction that use only full-rank path witnesses. By contrast, multiplying every maximal simplex by the formal unit \((1+u)^{S(\pi)}\) near \(u=0\) is an invertible diagonal basis change over \(\mathbb F_2[[u]]\); that alone cannot create a new homological obstruction. The nonunit parameter \(t\) in (3) retains information at its monochromatic specialization \(t=0\).

Theorem 2 simultaneously shows that **individual rooted filtrations have no homological obstruction at any switch level**: each one has the same apex-preserving contraction. The missing Wu–Yang theorem must therefore concern the relative geometry of different roots, their antipodes, or their intersections, not ordinary homology of a single root filtration.

The update law (8) identifies a two-state endpoint refinement for root-transport maps. It does not yet give an equivariant chain map across mixed-color squares: different witnessing paths for the same Freudenthal simplex can have different terminal colors, and selecting terminal colors is not generally closed under simplicial deletion. A suitable path-flag resolution, or equivalent chain-level correspondence retaining witnesses, is still required.

### Multi-root Čech chains and the geodesic switch filtration

Fix an arbitrary edge coloring of \(Q_n\), \(n\ge3\). Let \(K_x^{[r]}\) be the rooted Freudenthal geodesic-prefix complex of paths with at most \(r\) switches. Place all these complexes inside a single barycentric subdivision of the common type-D refinement constructed earlier in this Article. Define
\[
U^{[r]}=\bigcup_{x\in Q_n}K_x^{[r]},\qquad
K_A^{[r]}=\bigcap_{x\in A}K_x^{[r]}
\]
for every nonempty root set \(A\subseteq Q_n\).

**Theorem 1 (multi-root chain resolution).** Put
\[
\boxed{
B_{p,q}^{[r]}=
\bigoplus_{\substack{A\subseteq Q_n\\|A|=p+1}}
C_q(K_A^{[r]};\mathbb F_2).
}
\tag{1}
\]
Equip it with the ordinary simplicial boundary vertically and the alternating-deletion Čech boundary horizontally (signs disappear over \(\mathbb F_2\)). The total differential squares to zero, and augmentation from its total complex to the simplicial chains of \(U^{[r]}\) is a quasi-isomorphism. The associated intersection spectral sequence is
\[
\boxed{
E^1_{p,q}(r)=\bigoplus_{|A|=p+1}
H_q(K_A^{[r]};\mathbb F_2)
\Longrightarrow H_{p+q}(U^{[r]};\mathbb F_2).
}
\tag{2}
\]
Every switch-filtration inclusion induces compatible morphisms of these chain complexes and spectral sequences.

*Proof.* The horizontal and vertical boundaries commute and each squares to zero. For every simplex \(\sigma\in U^{[r]}\), let \(I(\sigma)\) be the nonempty set of roots whose complexes contain it. The horizontal complex contributed by \(\sigma\) is the augmented simplicial chain complex of the full simplex on \(I(\sigma)\); it is contractible. Resolving each simplex in this way proves the augmentation is a quasi-isomorphism. The other filtration gives (2), and nesting in \(r\) gives the functoriality. \(\square\)

**Theorem 2 (free antipodal indexing at switch level zero).** Assume the edge coloring is antipodally odd and, hypothetically, no full geodesic has at most one switch. Then every nonempty root-index intersection \(K_A^{[0]}\) has an index set \(A\) containing no pair \(x,\bar x\). Consequently the antipodal involution acts freely on all nonzero root-index summands of \(B_{\bullet,\bullet}^{[0]}\).

*Proof.* The rank-preserving gluing theorem of this Article says \(K_x^{[0]}\cap K_{\bar x}^{[0]}=\varnothing\) under the hypothesis. An intersection indexed by a set containing both roots is therefore empty. Any index set fixed under root complementation contains an antipodal pair, so no nonempty index summand can be fixed. The antipode maps \(K_A^{[0]}\) to \(K_{\bar A}^{[0]}\), proving the result. \(\square\)

**Proposition 3 (dimension barrier for the ordinary nerve).** The nerve of the rooted monochromatic prefix complexes has dimension at least \(n\), regardless of the coloring.

*Proof.* Fix any cube vertex \(y\). The trivial prefix puts \(y\in K_y^{[0]}\). For every dimension \(i\), the one-edge geodesic from \(y\oplus e_i\) to \(y\) is monochromatic, so \(y\in K_{y\oplus e_i}^{[0]}\). These \(n+1\) distinct root complexes have a common vertex and span an \(n\)-simplex of the nerve. \(\square\)

**Research consequence.** The individual rooted Rees complexes are filtered contractible, so their homology alone cannot reveal the antipodal one-switch obstruction. The intersection complex (1) instead retains the disconnected and empty multi-root square carriers proved earlier. But Proposition 3 rules out a naive dimension-bound argument on its ordinary nerve: that nerve is already at least \(n\)-dimensional, while the cubical boundary source has dimension \(n-1\). A successful Wu–Yang adaptation must cancel higher-root overlap terms using their full-rank path certificates and rank-two color-comparison data, yielding a lower-dimensional equivariant chain target. The present resolution does not establish such a cancellation.

### Twisted switch count: cyclic root slides and quadratic exchange defects

This subsection extends the switch-deformation and Coxeter exchange work in Article XIV, Subsections 53 and 55. The ordinary switch count has linear-order endpoint exceptions. A root-slide-invariant antiperiodic count removes those exceptions, providing a uniform square-exchange formula and a local rigidity theorem for minimum-switch antipodal geodesics.

Let \(n\ge3\) and let \(c\) be any antipodally odd binary edge coloring of \(Q_n\). For a full rooted dimension-simple geodesic flag \(g=(x;d_1,\ldots,d_n)\), let \(w(g)=(w_1,\ldots,w_n)\) be its edge-color word. Define its **twisted cyclic switch count**
\[
\boxed{\sigma(g)=\sum_{j=1}^{n-1}[w_j\ne w_{j+1}]+[w_n=w_1],\qquad
h(g)=\frac{\sigma(g)-1}{2}.}
\tag{1}
\]
The last comparison is between \(w_n\) and the *complement* of \(w_1\), so the indicator of a change is \([w_n=w_1]\).

**Theorem 1 (root-slide invariance).** The count \(\sigma(g)\) is positive and odd, \(h(g)\) is a nonnegative integer, and
\[
\boxed{\sigma(Tg)=\sigma(g)=\sigma(\tau g),}
\tag{2}
\]
where the root slide \(T\) replaces the word by
\((w_2,\ldots,w_n,1-w_1)\) and \(\tau\) antipodally translates the flag. Furthermore
\[
\boxed{h(g)=0\iff\text{some }T^jg\text{ is monochromatic}.}
\tag{3}
\]
Thus NORI1 is equivalent to \(\min_g h(g)=0\).

*Proof.* The mod-two sum of comparisons around the antiperiodically closed word is one; hence their integer sum is odd. Rotating the twisted cycle preserves the comparisons and gives (2). If only one twisted comparison changes, choose the root-slide window cut there: all \(n\) colors in that window coincide. Conversely a monochromatic word has only the twisted seam change. \(\square\)

**Theorem 2 (uniform Lipschitz law for every dimension exchange).** Let \(g'\) be obtained by interchanging the dimensions at adjacent positions \(j,j+1\), \(1\le j<n\). Let \(pq\), respectively \(rs\), be the two edge-color pairs for the original and exchanged routes. Define flanking bits
\[
A=\begin{cases}w_{j-1},&j>1,\\1-w_n,&j=1,\end{cases}
\qquad
B=\begin{cases}w_{j+2},&j<n-1,\\1-w_1,&j=n-1.\end{cases}
\tag{4}
\]
For \(G(A,p,q,B)=[A\ne p]+[p\ne q]+[q\ne B]\), one has
\[
\boxed{\sigma(g')-\sigma(g)
=G(A,r,s,B)-G(A,p,q,B)\in\{-2,0,2\}.}
\tag{5}
\]
In particular \(\boxed{|h(g')-h(g)|\le1}\), including the exchanges at positions \(1,2\) and \(n-1,n\).

*Proof.* Every edge color outside the exchanged two-edge route is unchanged. The only altered twisted comparisons are the three in (4)–(5). Each local comparison count has parity \(A\oplus B\), independently of the route, and lies between zero and three. Thus their difference is zero or plus/minus two. \(\square\)

**Theorem 3 (uniform quadratic defect for twisted Freudenthal chains).** For each rooted cubical \(d\)-face, \(d\ge3\), weight its complete Freudenthal simplex \(\sigma_\pi\) by \((1+u)^{\sigma(\pi)}\), with \(\sigma(\pi)\) the twisted switch count of that face's ordered color word:
\[
\mathfrak F^{\rm tw}_u(F,x)=\sum_\pi(1+u)^{\sigma(\pi)}\sigma_\pi
\quad\text{over }\mathbb F_2[u].
\tag{6}
\]
An internal facet shared by two neighboring dimension orders has coefficient zero when their twisted switch counts agree, and otherwise has coefficient
\[
\boxed{u^2(1+u)^{\min(\sigma,\sigma')}.}
\tag{7}
\]
Therefore *every internal facet cancels modulo \(u^2\)*, without the endpoint exceptions present for the ordinary switch deformation in Subsection 55.

For local two-edge route bits \(pq\) and \(rs\), and flanking bits \(A,B\) chosen as in (4), the quadratic coefficient of the defect is
\[
\boxed{
A(p\oplus r)+B(q\oplus s)
+(p\oplus q\oplus r\oplus s)+pq+rs
\pmod2.
}
\tag{8}
\]
It equals one precisely when the twisted switch count changes by two. Moreover
\[
\boxed{(1+u)^\sigma=(1+u)(1+u^2)^h.}
\tag{9}
\]
This identifies \(h\) as the root-slide-invariant integer defect relevant to the quadratic order.

*Proof.* Equation (5) shows that the two exponents differ by zero or two. In characteristic two,
\((1+u)^{r+2}+(1+u)^r=u^2(1+u)^r\), proving (7). To find the quadratic coefficient, subtract the two local three-comparison counts from the common unaffected comparisons. Equal parity of the local counts cancels the common contribution to the second binomial coefficient. Expanding their remaining \(\binom G2\) terms over \(\mathbb F_2\) gives (8). It is the six-bit expression previously found for interior exchanges, now valid also at the two ends using the twisted flanks. Equation (9) follows from \(\sigma=2h+1\). \(\square\)

**Theorem 4 (gate rigidity for cyclic switch minimizers).** Choose \(g\) minimizing \(h\) over all full rooted geodesics. For every adjacent exchange, with \(A,p,q,B\) as above:

- If \(G(A,p,q,B)=3\), then the alternative route satisfies \((r,s)=(p,q)\). Thus **both routes through the exchanged square have the same alternating bit word**, a gate \(10,10\) or \(01,01\).
- If \(G(A,p,q,B)=2\), then \(A=B=t\) and the alternative route cannot be \((t,t)\).
- If \(G=0\) or \(1\), no adjacent exchange can decrease \(h\).

These two restrictions for \(G=3,2\) also characterize local nondecrease under all adjacent dimension swaps from a given flag.

*Proof.* A global minimizer cannot admit a swap lowering \(\sigma\) by two. If \(G=3\), then \(A\ne B\), and the unique two-bit route achieving all three comparison changes is \((p,q)=(1-A,A)\); every other route has one change, contradicting minimality. If \(G=2\), then \(A=B=t\), and the unique route with zero changes is \((t,t)\). These are the only possibilities for a decrease, since zero and one are already minimal comparison counts at their respective parities. \(\square\)

**Interpretation and limitations.** Unlike the ordinary switch number, the twisted defect is invariant under root slides and its adjacent-exchange variation has no distinguished endpoints. This allows a single local quadratic formula across the complete cyclic flag geometry. But since \(\sigma\) is always odd, the weights \((1+u)^\sigma\) agree modulo \(u^2\); the first-order cancellation by itself is a normalization, not a proof of NORI1. The uniform defect is the relevant input for a root-slide-compatible switch filtration or Rees-chain construction that couples multiple roots and controls the projective obstruction. The unproved step is showing these local constraints force some flag with \(h=0\).

### Rank-two zero-switch holes and their three-cube coherence defect

We identify the first support-preserving obstruction to filling Freudenthal squares using monochromatic dimension-simple prefixes, and compute its initial three-cube compatibility law.

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary coloring. For a cubical square \(F\) and each corner \(v\), let \(C_v=K_v^0\cup K_v^1\) be the union of monochromatic rooted geodesic-prefix complexes. Put
\[
U_F^{[0]}=\bigcup_{v\in V(F)}(|C_v|\cap F).
\tag{1}
\]
The subcomplexes intersect \(F\) in simplices with all vertices in \(F\), since \(F\) is an exposed face of the geometric cube. Thus (1) depends only on the four edge bits around \(F\).

Write those bits cyclically \(a,b,c,d\), with arithmetic in \(\mathbb F_2\), and define
\[
\kappa(F)=a+b+c+d,\quad
\alpha(F)=(1+a+c)(1+b+d)(a+b),\quad
\theta(F)=\kappa(F)+\alpha(F).
\tag{2}
\]
Here \(\alpha(F)\) is the indicator that the edge bits alternate, and \(\kappa(F)\) is square curvature. These indicators are invariant under square symmetries and simultaneous complementation.

**Theorem 1 (complete square filling classification).** Up to dihedral symmetry and global color complement, the homotopy types and local relative homology groups are
\[
\begin{array}{c|c|c|c}
\text{cyclic bits}&U_F^{[0]}&H_1(U_F^{[0]};\mathbb F_2)&\theta(F)\\ \hline
0000&F&0&0\\
0011&F&0&0\\
0001&\text{two overlapping triangles plus a connecting boundary edge}&\mathbb F_2&1\\
0101&\partial F&\mathbb F_2&1 .
\end{array}
\tag{3}
\]
Consequently
\[
\boxed{\dim_{\mathbb F_2}H_2(F,U_F^{[0]};\mathbb F_2)=\theta(F).}
\tag{4}
\]
At filtration level one, every rooted prefix complex contains both two-step Freudenthal triangles of \(F\). Hence \(U_F^{[1]}=F\), and the nontrivial relative classes of (4) are filled by allowing one switch.

*Proof.* Every incident edge lies in each corner's monochromatic-prefix union. A rooted Freudenthal triangle belongs to it precisely when the associated two-edge route has equal edge bits. For \(0000\), all rooted routes are monochromatic. For \(0011\), a corner admits both opposite routes, of words \(00\) and \(11\), so its two triangles cover \(F\). For \(0001\), the sole monochromatic two-step routes run along the three consecutive equal-colored edges; their triangles on different square diagonals overlap in a contractible region, while the remaining boundary edge completes a circle. For \(0101\), no two-step route is monochromatic, leaving only \(\partial F\). These cases exhaust the square patterns. The first term of \(\theta\) detects odd patterns, the second detects alternating patterns, proving the last column. The long sequence of the pair \((F,U_F^{[0]})\), with \(F\) contractible and \(U_F^{[0]}\) connected, gives (4). Every length-two word has at most one switch, proving the final assertion. \(\square\)

For a legal antipodally odd cube coloring, \(\theta(\bar F)=\theta(F)\). Thus \(\theta\) descends to a projective 2-cochain. Its coboundary is a first three-dimensional coherence defect.

**Theorem 2 (flat three-cube law).** If the square curvature vanishes on every face of a cubical 3-face \(D\), then
\[
\boxed{\sum_{F\lessdot D}\alpha(F)
=\sum_{F\lessdot D}\theta(F)=0\pmod2.}
\tag{5}
\]
Thus \(\theta\) is a cocycle wherever the given coloring is flat.

*Proof.* A flat edge cochain on \(D\) is a coboundary \(\delta h\) of a vertex function. Write \(\Delta_i h(x)=h(x)+h(x+e_i)\) for the Boolean directional difference. Let \(i,j,k\) be the three directions and, at the lowest corner, abbreviate
\[
a=\Delta_i h,\quad b=\Delta_j h,\quad d=\Delta_k h,\quad
p=\Delta_i\Delta_j h,\quad q=\Delta_i\Delta_k h,\quad
r=\Delta_j\Delta_k h,\quad s=\Delta_i\Delta_j\Delta_k h .
\]
On the lower \(ij\) face, the opposite parallel-edge discrepancies both equal \(p\), giving \(\alpha_{ij}(0)=(1+p)(a+b)\) by (2). On the corresponding upper \(ij\) face,
\[
\alpha_{ij}(1)=(1+p+s)(a+b+q+r).
\]
Their sum is \((1+p)(q+r)+s(a+b+q+r)\). The analogous formulas for the \(ik\) faces paired in direction \(j\), and the \(jk\) faces paired in direction \(i\), sum to
\[
\begin{aligned}
\delta\alpha(D)
={}&(1+p)(q+r)+(1+q)(p+r)+(1+r)(p+q)\\
&+s[(a+b+q+r)+(a+d+p+r)+(b+d+p+q)].
\end{aligned}
\tag{6}
\]
Every term occurs an even number of times, so (6) is zero. Since \(\kappa=\delta c\), also \(\delta\kappa=\delta^2c=0\), proving (5). \(\square\)

**Theorem 3 (nonclosed defect in unrestricted legal colorings).** For every \(n\ge4\), there exists a legally antipodally odd coloring and a cubical 3-face \(D\) with
\[
\boxed{(\delta\theta)(D)=1.}
\tag{7}
\]

*Proof.* Choose a 3-face with directions \(i,j,k\). Give the two parallel dimension-\(i\) edges of its \(ij\)-square at \(k=0\) bit one, and give every other edge of \(D\) bit zero. This produces precisely one alternating face: the selected \(ij\) face has cyclic word \(1010\); its opposite face is monochromatic; the two \(ik\) faces each contain one colored edge; and the two \(jk\) faces are monochromatic. Hence \(\delta\alpha(D)=1\). As \(\delta\kappa=0\), equation (7) follows. When \(n\ge4\), the 3-face and its antipodal mate are disjoint. Prescribe the complementary coloring on that mate, then complete the remaining antipodal edge orbits arbitrarily. This yields the stated legal coloring. \(\square\)

**Theorem 4 (classification of all symmetric closed square-local rules).** Let \(f:\mathbb F_2^4\to\mathbb F_2\) be any function of the cyclic edge-color word of a square, invariant under dihedral symmetries and simultaneous color complementation. Assign to every square \(F\) of a cubical 3-face the value \(f(c|_{\partial F})\). The following are equivalent:

(i) For every binary edge coloring of every cubical 3-face \(D\), the sum \(\sum_{F\lessdot D}f(c|_{\partial F})\) vanishes.

(ii) There are constants \(u,v\in\mathbb F_2\) such that
\[
\boxed{f(c|_{\partial F})=u+v\kappa(F)\qquad\text{for every square }F.}
\tag{8}
\]

*Proof.* Dihedral symmetry and color complementation leave four orbits of cyclic square words, represented by \(0000,0001,0011,0101\). Write their values under \(f\) as \(A,B,C,D\).

First consider a cubical 3-face in which precisely two mutually perpendicular edges incident to the same corner have color one, and all ten remaining edges have color zero. Its six squares consist of three \(0000\) faces, two \(0001\) faces, and one \(0011\) face. The closedness condition forces
\[
3A+2B+C=A+C=0.
\]
Next give color one to precisely the two parallel edges in a single square, and zero to every other 3-face edge. This yields three \(0000\) faces, two \(0001\) faces, and one alternating \(0101\) face. Closedness forces \(A+D=0\). Thus \(C=D=A\), while \(B\) is unrestricted.

On the four word orbits, square curvature takes the respective values \(0,1,0,0\). Therefore the resulting rule is \(f=A+(A+B)\kappa\), establishing (ii). Conversely the constant square cochain has zero coboundary because every 3-cube has six square facets, and the curvature cochain is closed since \(\kappa=\delta c\) and \(\delta^2=0\). Every linear combination of these two rules is consequently closed. \(\square\)

**Corollary 5 (sharp limitation of square-only chain repairs).** There is no dihedrally symmetric, color-complement-invariant rule that detects the relative zero-switch hole in every square and is also a 2-cocycle for all unrestricted binary edge colorings. More generally, among all such square-local rules, the only universally closed information is a constant and square curvature. Any filtered Wu--Yang repair encoding the alternating flat-square obstruction must use additional data from roots, adjacent cells, or higher-dimensional incidence. A rooted or orientation-sensitive construction is not excluded by the theorem.

*Proof.* Theorem 1 identifies the desired hole rule as \(\theta\), whose values on the four orbits are \(0,1,0,1\). These fail the necessary equality between the \(0000\) and \(0101\) values in Theorem 4. The classification supplies the stronger assertion. \(\square\)

**Theorem 6 (projective class of the constant square cochain).** For \(n\ge3\), let \(Y_n=\partial[0,1]^n/A\cong\mathbb RP^{n-1}\). The cochain \(\mathbf1_2\in C^2(Y_n;\mathbb F_2)\), assigning one to every projective square, satisfies
\[
\boxed{[\mathbf1_2]=\left(\binom n2\bmod2\right)u^2,}
\tag{9}
\]
where \(u=w_1(S^{n-1}\to Y_n)\). In particular this cochain is a coboundary precisely for \(n\equiv0,1\pmod4\).

*Proof.* Every cubical 3-cell has six square facets, so \(\mathbf1_2\) is closed. Upstairs, define an undirected-edge one-cochain \(b\) by
\[
b_i(x)=\sum_{j<i}x_j\pmod2
\]
on an edge of direction \(i\). Every square has \(\delta b=1\): for \(i<j\), crossing \(i\) changes \(b_j\) and crossing \(j\) leaves \(b_i\) fixed. Let \(\tau x=\bar x\). Then
\[
\tau^*b+b=\delta g,\qquad
g(x)=\sum_{i=1}^n(i-1)x_i.
\tag{10}
\]
If a quotient one-cochain has coboundary \(\mathbf1_2\), its pullback \(d\) is invariant under \(\tau\) and satisfies \(\delta d=\delta b\). Because the covering boundary \(S^{n-1}\) has \(H^1=0\) for \(n\ge3\), we must have \(d=b+\delta h\) for some vertex function \(h\). Invariance is equivalent to
\[
\delta(g+h+\tau^*h)=0,
\]
meaning that \(g+h+\tau^*h\) is constant on the connected cube graph. But \(h+\tau^*h\) is invariant under \(\tau\), whereas
\[
g(\bar x)+g(x)=\sum_{i=1}^n(i-1)=\binom n2\pmod2.
\tag{11}
\]
Thus an invariant primitive is impossible if \(\binom n2\) is odd.

Conversely, if this binomial coefficient is even, \(g\) is invariant. Define \(h\) independently on antipodal vertex pairs so that \(h(x)+h(\bar x)=g(x)\). Then \(d=b+\delta h\) is invariant and has \(\delta d=\mathbf1_2\), giving a quotient primitive. Hence the constant cochain is a coboundary just when \(\binom n2\) is even. Since \(H^2(Y_n;\mathbb F_2)\cong\mathbb F_2\) is generated by \(u^2\), this proves (9). \(\square\)

**Corollary 7 (classification of universal local projective classes).** Let \(c\) be any legal antipodally odd edge coloring, \(n\ge3\). Every dihedrally symmetric, color-complement-invariant square-local rule that is a cocycle for all unrestricted colorings has the form \(f=a+b\kappa\), with \(a,b\in\mathbb F_2\), and
\[
\boxed{[f]=\left(a\binom n2+bn\right)u^2.}
\tag{12}
\]
Thus its projective cohomology class depends only on \(n,a,b\), independently of the edge coloring.

*Proof.* Theorem 4 gives the classification \(f=a+b\kappa\). Theorem 6 computes the constant cochain class, and the established projective-curvature theorem of Article XIV gives \([\bar\kappa]=(n\bmod2)u^2\). Add these classes. \(\square\)

**Implication for Wu--Yang chain corrections.** The indicator \(\theta=\kappa+\alpha\) detects one relative square-filling class for every zero-switch deficiency, including flat alternating squares invisible to curvature. Theorem 3 proves that these classes do not form a universal closed 2-cochain: their square-level cancellation can have a nonzero three-cube defect. A coherent filtered construction must therefore incorporate additional local incidence data and higher fillings. This result supplies a verified obstruction to a curvature-only or independently filled-square repair, while making no claim to resolve unrestricted NORI1 or the Hamilton boundary conjecture.

This subsection exhibits an all-dimensional source of a *three-dimensional* relative switch obstruction that is invisible to every two-dimensional square-filling test. It also applies to the alternating residual three-faces forced by a hypothetical near-spanning bi-monochromatic interval in the preceding subsection.

Let \(F\cong[0,1]^3\), with vertex set \(\{0,1\}^3\). For \(r=0,1,2\), give each edge joining a vertex of Hamming weight \(r\) to one of weight \(r+1\) the bit
\[
\boxed{c(e)=a+r\pmod2,\qquad a\in\{0,1\}.}
\tag{1}
\]
Write \(K_x^b\) for the geometric rooted Freudenthal prefix complex at \(x\in V(F)\), restricted to geodesic prefixes whose edges all have color \(b\). Set
\[
\boxed{U_F^{[0]}=\bigcup_{x\in V(F)} (|K_x^0|\cup|K_x^1|)\subseteq F.}
\tag{2}
\]
The same construction was used to define the square-filling indicator \(\theta\) in Article XIV.

**Theorem 1 (all squares filled but a nonzero relative three-class).** For the coloring (1):

(i) Every one of the six square faces \(G\subseteq F\) has square curvature \(\kappa(G)=0\) and zero-switch relative filling indicator \(\theta(G)=0\). In fact,
\[
\boxed{\partial F\subseteq U_F^{[0]}.}
\tag{3}
\]

(ii) Every monochromatic full length-three geodesic in \(F\) uses only vertices of weights one and two. In particular, every three-simplex in \(U_F^{[0]}\) is contained in the closed slab
\[
\boxed{1\le t_1+t_2+t_3\le2.}
\tag{4}
\]
No point of the interior open corner caps \(0<t_i<1\) with \(\sum_i t_i<1\), or with \(\sum_i t_i>2\), belongs to \(U_F^{[0]}\).

(iii) The integral relative homology has a nonzero free summand:
\[
\boxed{H_3(F,U_F^{[0]};\mathbb Z)\supseteq \mathbb Z.}
\tag{5}
\]
Thus all rank-two squares have zero relative obstruction, while the rank-three cell has a surviving relative filling class.

*Proof.* Consider a square face \(G\). Its two edges from the corner of lower Hamming weight have color \(b\), and its other two edges have color \(1-b\). Its cyclic word is therefore \(b,(1-b),(1-b),b\), a dihedral translate of \(0011\). The XOR of its four edge colors is zero. Moreover, between its two side corners there are two monochromatic two-step routes: one through the bottom vertex, of color \(b\), and one through the top vertex, of color \(1-b\). The corresponding two rooted Freudenthal triangles share the side-corner diagonal and cover the entire square. Thus \(G\subseteq U_F^{[0]}\) for every square, proving (i).

An edge between Hamming levels zero and one, or between levels two and three, has color \(a\), while every edge between levels one and two has color \(1-a\). Any complete antipodal path of length three must cross between levels one and two: its endpoints have complementary Hamming weights, so a path that avoided this middle layer could not connect them. Consequently a monochromatic full path cannot use any edge in the outer Hamming layers, and therefore all its vertices have weights one or two. Conversely the three-step paths alternating between weight-one and weight-two vertices are monochromatic of color \(1-a\), so this constraint is attained. Every three-dimensional simplex in a rooted Freudenthal prefix complex comes from a monochromatic full length-three geodesic and therefore has all vertex weights in \(\{1,2\}\), implying (4). All prefixes of length at most two lie in the geometric boundary \(\partial F\), since at least one dimension remains fixed. Thus no point in either stated interior cap can belong to (2), proving (ii).

Choose a point \(p\) in the first missing cap, for instance \(p=(1/8,1/8,1/8)\). Then \(p\notin U_F^{[0]}\), whereas \(\partial F\subseteq U_F^{[0]}\) by (i). Radial projection from \(p\) gives a continuous map \(r:F\setminus\{p\}\to\partial F\) restricting to the identity on \(\partial F\). Its restriction to \(U_F^{[0]}\) is a retraction onto \(\partial F\). Hence the inclusion of \(\partial F\cong S^2\) in \(U_F^{[0]}\) injects a copy of \(\mathbb Z\) into \(H_2(U_F^{[0]};\mathbb Z)\). The long homology sequence of the pair \((F,U_F^{[0]})\), using contractibility of \(F\), gives
\[
H_3(F,U_F^{[0]};\mathbb Z)
\cong H_2(U_F^{[0]};\mathbb Z)
\supseteq\mathbb Z,
\]
proving (iii). \(\square\)

**Corollary 2 (a forced three-cell defect near a hypothetical counterexample).** Suppose an antipodally odd coloring of \(Q_n\) has no monochromatic full antipodal geodesic, but admits opposite-color monochromatic geodesics between a common ordered pair at distance \(n-3\). By the preceding subsection, both opposed residual three-faces have the alternating layer coloring (1), with complementary phases. Each residual three-face therefore has vanishing rank-two relative switch indicators on all six squares but nonzero relative degree-three homology in its zero-switch prefix union.

*Proof.* The preceding rigidity theorem supplies (1) on each residual face. Apply Theorem 1 independently to the two faces. \(\square\)

**Consequence for dimension-simple Wu--Yang chains.** A repair that tests each square independently for whether its zero-switch rooted prefix union fills the square encounters no obstruction on this example: every square is filled, and all projective square curvatures vanish. Nevertheless the coherent rank-three extension is topologically obstructed. The failure is not merely an inadequacy of a chosen square cocycle; even knowing that each entire boundary square admits a zero-switch filling does not make the three-cell fillable within the same zero-switch prefix union.

The alternating residual face simultaneously exhibits two opposed root corners with no monochromatic two-edge prefix, while monochromatic length-three geodesics exist from other corners in the middle layer. Thus the obstruction respects dimension-simplicity and highlights why cross-root coherence, rather than a scalar square-curvature invariant, is central to the chain-level adaptation of Wu and Yang.

### Bockstein obstruction for truncated equivariant chain transfers

Put \(G=\mathbb Z_2=\{1,\tau\}\) and \(R=\mathbb F_2[G]\). For a finite free \(G\)-simplicial complex \(X\), its simplicial chain complex \(C_*(X;\mathbb F_2)\) consists of free \(R\)-modules. Call an \(R\)-linear chain map *augmented* if it preserves the standard augmentation to \(\mathbb F_2\).

**Theorem 1 (index naturality without a continuous map).** Suppose \(f:C_*(X)\to C_*(Y)\) is an augmented \(G\)-equivariant chain map between finite free \(G\)-complexes. If \(\alpha_X\) and \(\alpha_Y\) are the classes in \(H^1(X/G;\mathbb F_2)\) and \(H^1(Y/G;\mathbb F_2)\) classifying their respective double covers, then the induced cohomology map satisfies
\[
\boxed{f^*(\alpha_Y^j)=\alpha_X^j\quad(j\ge0).}
\tag{1}
\]
Consequently \(\alpha_X^q\ne0\) and \(\alpha_Y^q=0\) prohibit such a chain map.

*Proof.* The group algebra has a non-split short sequence of \(R\)-modules
\[
0\longrightarrow\mathbb F_2
\xrightarrow{1\mapsto1+\tau}R
\xrightarrow{\varepsilon}\mathbb F_2
\longrightarrow0.
\tag{2}
\]
The connecting morphism \(\delta_X\) of the induced cohomology long sequence on \(\operatorname{Hom}_R(C_*(X),-)\) equals cup product with the covering class: \(\delta_X(z)=\alpha_X\smile z\). This follows by identifying (2) as the pullback of the universal degree-one extension class from \(B\mathbb Z_2\). The same holds for \(Y\).

The modules \(C_i(X)\) and \(C_i(Y)\) are free over \(R\), so Hom applied to (2) is a short sequence of cochain complexes. The equivariant chain map \(f\) gives commuting connecting morphisms \(f^*\delta_Y=\delta_Xf^*\). Augmentation preservation gives \(f^*(1)=1\) in degree zero. Consequently
\[
f^*(\alpha_Y^j)=f^*(\delta_Y^j1)
=\delta_X^j f^*(1)=\delta_X^j1=\alpha_X^j.
\]
No multiplicative cochain map or underlying space map is needed. \(\square\)

Let \(\Sigma_n\) be the type-\(A_{n-1}\) Coxeter complex. Its vertices are the proper nonempty subsets \(S\subset[n]\), and its simplices are strict chains of those subsets. Complementation \(S\mapsto[n]\setminus S\) is the antipodal involution on \(|\Sigma_n|\cong S^{n-2}\). The quotient is \(\mathbb RP^{n-2}\), up to equivariant homeomorphism. Its \(q\)-skeleton \(\Sigma_n^{(q)}\) is invariant under this involution and has
\[
\boxed{\alpha_{\Sigma_n^{(q)}}^q\ne0\quad(0\le q\le n-2).}
\tag{3}
\]
Indeed the inclusion of the quotient \(q\)-skeleton into the entire quotient is injective on degree-\(q\) cohomology: both cellular complexes have the same degree-\(q\) cochains and the same incoming coboundary. The restriction of the nonzero projective class remains nonzero.

**Theorem 2 (half-dimensional truncated-chain criterion for NORI1).** Let \(n\ge5\) and let \(c\) be an antipodally odd coloring of \(Q_n\). Put
\[
K_a(c)=\Delta P_a(c),\quad K(c)=K_0(c)\cup K_1(c),
\quad m=\left\lfloor\frac{n-3}{2}\right\rfloor,\quad
q=m+1=\left\lfloor\frac{n-1}{2}\right\rfloor.
\tag{4}
\]
The involution on \(K(c)\) is \(R(u,v)=(\bar v,\bar u)\), which interchanges red and blue endpoint complexes.

If \(c\) has no monochromatic full antipodal geodesic, then **no** augmented \(G\)-equivariant chain map
\[
\boxed{
C_*(\Sigma_n^{(q)};\mathbb F_2)
\longrightarrow
C_*(K(c);\mathbb F_2)
}
\tag{5}
\]
exists. Hence a construction of (5) for every hypothesized counterexample would prove NORI1 in dimension \(n\).

*Proof.* By the two-color rank-jump theorem in Article XIV, the no-closure hypothesis produces an equivariant map \(K(c)\to S^m\). Therefore the covering class \(\alpha_K\) satisfies \(\alpha_K^{m+1}=0\). The involution on \(K(c)\) is free: its fixed interval vertices would represent full antipodal monochromatic geodesics, while interval ranks increase strictly within each chain. On the source, (3) implies \(\alpha_{\Sigma_n^{(q)}}^q\ne0\) because \(q\le n-2\). Since \(q=m+1\), Theorem 1 prohibits (5). \(\square\)

**Smallest required skeleton.** The proof criterion uses chains only through dimension \(q=\lfloor(n-1)/2\rfloor\), not the entire Coxeter sphere of dimension \(n-2\). For \(n=5,6\), \(q=2\); for \(n=7,8\), \(q=3\); and for \(n=9,10\), \(q=4\). This specifies the degree at which any hypothetical compatible chain assignment must fail.

**Connection to the new matroid-Sperner toolkit entry.** On the signed-direction partition matroid with parallel classes \(\{i^+,i^-\}\), independent sets use each dimension at most once and flats are unions of complete classes. Ordered maximal chains of its Boolean lattice of flats form the same type-A Coxeter complex \(\Sigma_n\). This is the natural ordered-flat-chain *source* supplied by the 2015 Andrade–Rodríguez Rey–Ruiz Sandoval construction. The matroid theorem does **not** itself construct (5): independent dimension labels do not force compatible monochromatic ordered paths. The target \(K(c)\) retains such path witnesses, and the missing argument must choose coherent, augmented, equivariant chains across rank exchanges.

**Interpretation.** The full punctured affine torus and a continuous transfer map are sufficient but unnecessary for a chain-level Wu–Yang argument. The stronger, smaller target is a support-respecting mod-two transfer through a half-dimensional skeleton of one type-A Coxeter sphere. The square and polar three-cell obstructions previously found in Article XIV identify possible early failure mechanisms; this theorem supplies a precise cohomological obstruction degree but does not yet construct the transfer or prove NORI1.

### Seam transgression for the two-color endpoint quotient

Let \(K_0,K_1\) be finite simplicial subcomplexes with a free simplicial involution \(R\) exchanging them. Put \(K=K_0\cup K_1\), \(I=K_0\cap K_1\), \(Q=K/R\), and \(J=I/R\). Freeness means no simplex is setwise fixed. Write \(p:K_0\to Q\) for the quotient restriction and \(i:J\hookrightarrow Q\) for inclusion. All cohomology below has coefficients in \(\mathbb F_2\).

**Theorem 1 (seam cochain sequence).** There is a short sequence of cochain complexes, with zero kernel and cokernel,
\[
\boxed{0\to C^*(Q)\xrightarrow{p^*}C^*(K_0)
\xrightarrow{T}C^*(J)\to0,}
\tag{1}
\]
where the second arrow is the orbit trace
\[
\boxed{(Tz)([\sigma])=z(\sigma)+z(R\sigma)}
\tag{2}
\]
for simplices \(\sigma\) of \(I\).

*Proof.* An orbit of simplices outside \(I\) meets \(K_0\) in one member, while an orbit in \(I\) meets \(K_0\) in two. The sequence (1) on each non-seam orbit is \(0\to\mathbb F_2\xrightarrow{=}\mathbb F_2\to0\); on a seam orbit it is
\[
0\to\mathbb F_2\xrightarrow{t\mapsto(t,t)}
\mathbb F_2^2\xrightarrow{(a,b)\mapsto a+b}
\mathbb F_2\to0.
\]
These are short sequences with zero kernel and cokernel. The arrows commute with coboundaries because face relations commute with \(R\). \(\square\)

Write \(\alpha=w_1(K\to Q)\) for the double-cover class, and \(\alpha_I=i^*\alpha=w_1(I\to J)\). Denote the connecting map in the long cohomology sequence of (1) by
\[
\delta:H^{j-1}(J)\to H^j(Q).
\]

**Theorem 2 (transgression of every covering-class power).** For all \(j\ge1\),
\[
\boxed{\alpha^j=\delta(\alpha_I^{j-1}).}
\tag{3}
\]
Moreover,
\[
\boxed{\alpha^j\ne0\iff
\alpha_I^{j-1}\notin\operatorname{im}
\bigl(T:H^{j-1}(K_0)\to H^{j-1}(J)\bigr).}
\tag{4}
\]

*Proof.* Choose a zero-cochain \(h\) on \(K_0\) that assigns complementary values to the two vertices in every \(R\)-orbit of vertices of \(I\). Set its values on other vertices arbitrarily. Then \(Th=1\), and \(T(dh)=0\). Hence \(dh=p^*\omega\) for a unique one-cochain \(\omega\) on \(Q\), representing \(\delta(1)\).

For each quotient vertex, choose a representative \(v\in K_0\), and choose the lift \(R^{h(v)}v\) in \(K\). For an orbit in \(I\), replacing \(v\) by \(Rv\) does not change the chosen lift because the assigned values are complementary. On every edge of \(Q\), represented by an edge in \(K_0\), the chosen endpoint lifts agree with one lifted edge if and only if the two \(h\)-values agree. Thus the edge transition bit is \((dh)(e)=\omega([e])\), proving \([\omega]=\alpha\). We have shown \(\delta(1)=\alpha\).

The trace satisfies the projection rule
\[
T(z\smile p^*b)=(Tz)\smile i^*b
\]
for cochains, since \(p^*b\) takes the same value on both members of an \(R\)-orbit. The connecting map therefore obeys
\(\delta(\gamma\smile i^*b)=\delta(\gamma)\smile b\).
Set \(\gamma=1\) and \(b=\alpha^{j-1}\), obtaining (3). The long cohomology sequence gives (4). When \(J\) is empty, interpret its cohomology and degree-zero unit as zero; the double cover then splits and the same formula holds. \(\square\)

**Corollary 3 (application to unrestricted NORI1).** Let \(n\ge5\), let \(c\) be antipodally odd, and suppose that there is no monochromatic full antipodal geodesic. Take \(K_a=\Delta P_a(c)\), the two monochromatic endpoint poset complexes, and \(R(u,v)=(\bar v,\bar u)\). The involution is free under this assumption: its fixed interval vertices would represent a full monochromatic geodesic, and ranks increase strictly within a simplex. The previously proved two-color comparison gap bounds the dimension of \(I=K_0\cap K_1\) by \(m-1\), where \(m=\lfloor(n-3)/2\rfloor\). Therefore
\[
\boxed{\alpha_I^m=0,\qquad \alpha^{m+1}=0.}
\tag{5}
\]
Theorem 2 recovers the half-dimensional covering-index bound directly from the seam, without requiring the constructed equivariant map to \(S^m\).

**Geometric scope and forward direction.** Every power of the reversal-cover class on \(K/R\) is controlled by a single-color-to-seam trace. Formula (4) identifies its nonvanishing with the failure of a particular seam cup-power to arise from \(K_0\). A chain-level Wu--Yang argument may therefore be phrased as a compatible nontransfer certificate at the two-color intersection, rather than as a continuous map from the punctured affine torus. This result is an identity for finite free involution complexes; it does not provide a source-to-\(K\) transfer and does not settle NORI1.

For colorings with full monochromatic antipodal geodesics, remove all rank-\(n\) vertices from \(K\) and their incident simplices. The resulting proper-rank complex has free \(R\)-action, so Theorems 1 and 2 apply without a no-closure hypothesis.

### A one-chain-per-degree antipodal transfer tower

Fix \(n\ge5\) and an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\). Let \(K=K_0(c)\cup K_1(c)\) be the union of monochromatic geodesic endpoint-poset complexes, with the involution \(R(u,v)=(\bar v,\bar u)\) exchanging colors. Write \(C_j=C_j(K;\mathbb F_2)\), let \(\partial\) be simplicial boundary, and let \(\varepsilon:C_0\to\mathbb F_2\) be augmentation. Put \(q=\lfloor(n-1)/2\rfloor\).

**Definition.** An *antipodal chain tower of height \(q\)* consists of \(z_j\in C_j\), \(0\le j\le q\), with
\[
\boxed{\varepsilon z_0=1,\qquad
\partial z_j=(1+R)z_{j-1}\ (1\le j\le q).}
\tag{1}
\]
All chains have mod-two coefficients.

**Theorem 1 (cellular index detection).** If \(R\) acts freely on \(K\) and a tower (1) exists, then
\[
\boxed{w_1(K\to K/R)^q\ne0.}
\tag{2}
\]

*Proof.* The standard antipodal CW structure on \(S^q\), built by repeated suspension of \(S^0\), has one free \(\mathbb F_2[\mathbb Z_2]\)-generator \(e_j\) in each dimension \(0\le j\le q\), with cellular boundary \(\partial e_j=(1+R)e_{j-1}\). Sending \(e_j\mapsto z_j\), and extending equivariantly, defines an augmentation-preserving chain map into \(C_*(K)\). The Bockstein naturality theorem proved earlier in Article XIV shows that such a chain map preserves the powers of double-cover classes. Since the covering class on \(S^q/\mathbb Z_2=\mathbb RP^q\) has nonzero \(q\)-th power, (2) follows. \(\square\)

**Theorem 2 (equivalence with NORI1 existence).** For every legal antipodally odd coloring \(c\) of \(Q_n\), \(n\ge5\), the following are equivalent:

(i) There is a monochromatic full antipodal geodesic.

(ii) The endpoint complex \(K(c)\) admits a tower (1) of height \(q=\lfloor(n-1)/2\rfloor\).

*Proof.* If a monochromatic antipodal geodesic joins \(u\) to \(\bar u\), then the rank-\(n\) endpoint vertex \(p=(u,\bar u)\) belongs to \(K\) and satisfies \(Rp=p\). Take \(z_0=p\) and \(z_j=0\) for \(j\ge1\).

Conversely suppose (ii) holds and no such geodesic exists. Under this hypothesis \(R\) acts freely on \(K\): any fixed endpoint vertex has rank \(n\), and a simplex cannot be invariant without fixed vertices because ranks increase strictly within chains. The two-color endpoint rank-gap theorem, equivalently the seam-transgression corollary, gives
\[
w_1(K\to K/R)^{m+1}=0,\qquad m=\lfloor(n-3)/2\rfloor.
\]
But \(q=m+1\), contradicting Theorem 1. Thus (i) holds. \(\square\)

**Theorem 3 (homological continuation obstruction).** If \(z_0,\ldots,z_{j-1}\) satisfy the tower equations up to degree \(j-1\), define
\[
\boxed{\omega_{j-1}=(1+R)z_{j-1}.}
\tag{3}
\]
For \(j=1\), this is an augmentation-zero zero-cycle. For \(j\ge2\),
\[
\partial\omega_{j-1}=(1+R)\partial z_{j-1}
=(1+R)^2z_{j-2}=0.
\]
The tower extends through degree \(j\) if and only if the homology class of \(\omega_{j-1}\) vanishes (using reduced degree-zero homology for \(j=1\)). The obstruction may depend on prior chain choices.

**Corollary 4 (necessary homology of a hypothetical counterexample).** Suppose no monochromatic full antipodal geodesic exists. Then either \(K\) has no connected component preserved by \(R\), or every preserved connected component \(C\) has nonzero \(H_j(C;\mathbb F_2)\) for some \(1\le j\le q-1\).

*Proof.* In an \(R\)-preserved component, choose a vertex \(p=z_0\); connectedness supplies \(z_1\) with boundary \(p+Rp\). If all the stated homology groups vanish, the cycles (3) bound successively through degree \(q\), creating a tower forbidden by Theorem 2. \(\square\)

**Implication.** Instead of assigning exponentially many compatible target chains to Coxeter flags, one may seek just \(q+1\) mod-two chains satisfying (1), one per degree. The problem is not thereby solved: existence of a full tower is equivalent to the sought monochromatic complete geodesic, rather than established for every coloring. The advantage is a sequence of explicit homological obstructions at each degree, amenable to the dimension-support filtration and exchange relations already present in Article XIV.

### Nonbacktracking color components and the first antipodal chain equation

Let \(c:E(Q_n)\to\mathbb F_2\) be any binary edge coloring, \(n\ge2\). For \(a\in\{0,1\}\), let \(H_a\) be the spanning subgraph consisting of all edges of color \(a\). Let \(P_a(c)\) be the directed monochromatic geodesic endpoint poset of Article XIV and \(K_a=\Delta P_a(c)\).

For any graph \(H\subseteq Q_n\), define the **nonbacktracking arc graph** \(N(H)\) as the ordinary undirected graph whose vertices are ordered arcs \((u,v)\) for every edge \(uv\in H\), and whose adjacency is
\[
\boxed{(u,v)\sim(v,w)\quad\text{if }uv,vw\in H,\ u\ne w.}
\tag{1}
\]
The condition \(u\ne w\) means that the consecutive edges have different cube directions, so their concatenation is a dimension-simple geodesic of length two.

**Lemma 1 (generation by arc turns and equal-endpoint identifications).** Every vertex \(p=(u,v)\) of \(K_a\) is connected within \(K_a\) to all the directed arcs of every monochromatic geodesic from \(u\) to \(v\). Each edge of \(N(H_a)\) is realized by a two-step monochromatic interval vertex of \(K_a\). Thus the connected components of \(K_a\) are obtained from those of \(N(H_a)\) by identifying directed arc components whenever they occur among the directed arcs of two or more monochromatic geodesics between the same endpoint pair.

*Proof.* A directed arc \((x,y)\) along a monochromatic dimension-simple geodesic from \(u\) to \(v\) is a directed subinterval of \((u,v)\); the prefix and suffix of that geodesic certify its comparison to \((u,v)\) in \(P_a(c)\). Hence an edge of the one-skeleton of \(K_a\) joins their poset vertices. In particular every monochromatic interval is attached to the arc graph, and distinct monochromatic witnesses of the same interval attach through that common vertex. An adjacency (1) consists of consecutive arcs of a red or blue two-step geodesic and is realized by their comparisons to its ordered endpoint pair. Conversely, for each poset comparison, the monochromatic extension certificates can be joined with an interior monochromatic path to realize both comparable intervals in one path, so all their directed arcs lie in a common component after the indicated equal-endpoint identifications. This proves the statement. \(\square\)

**Theorem 2 (component classification).** Let \(H\) be a connected component of \(H_a\) containing at least one edge. Its contribution to \(K_a\) has precisely the following connected-component count:

- **Branching case:** if some vertex of \(H\) has degree at least three, its entire endpoint-poset complex is connected.
- **Path case:** if \(H\) is a nontrivial path, it contributes precisely two components, representing the two orientations along the path.
- **Cycle case:** if \(H\) is a cycle of length \(2k\), it contributes one component if there exist opposite vertices \(u,v\) on that cycle with cube distance \(d_{Q_n}(u,v)=k\), and otherwise it contributes precisely two components.

In the cycle case, the condition says that the two complementary length-\(k\) half-cycles are both cube geodesics; such a pair of geodesics merges the two directed nonbacktracking components.

*Proof.* At a vertex \(v\) of degree \(d\) in \(H\), the local incidence graph in \(N(H)\) between the \(d\) incoming and \(d\) outgoing directed arcs is \(K_{d,d}\) with the \(d\) immediate-reversal pairs removed. If \(d\ge3\), this graph is connected, so both orientations of every incident edge belong to one component. For a neighboring vertex \(w\), both orientations of \(vw\) being in one component propagates this fact to each further incident edge: at degree two its two nonbacktracking continuations connect both orientations of the next edge, and at degree at least three the local graph is connected. Induction along paths in \(H\) shows that all arcs of a connected component containing a branching vertex lie in one component of \(N(H)\), hence of \(K_a\).

If every degree is at most two, \(H\) is a path or a cycle. Its nonbacktracking arc graph has precisely two components corresponding to the forward and reverse cyclic or linear orientations. In a path there is a unique directed simple path between two endpoints; thus no monochromatic interval can merge these components.

In a cycle there are precisely two simple paths between distinct vertices. They have equal length and are both cube geodesics precisely when the vertices separate the cycle into two length-\(k\) arcs and their Hamming distance is \(k\). In that case their shared ordered endpoint pair is a vertex of \(K_a\) incident with arcs of both cyclic orientations, merging the two components. If no such pair exists, every directed geodesic interval is supported in a unique cyclic orientation, and no identification is possible. Apply Lemma 1. \(\square\)

Now assume antipodal oddness, and put \(K=K_0\cup K_1\), \(I=K_0\cap K_1\), with \(R(u,v)=(\bar v,\bar u)\). Define a finite **color-component incidence graph** \(\Gamma_c\) as follows. Its vertices are the connected components of \(K_0\) and of \(K_1\), regarded as two distinct parts. For each directed endpoint pair \(p\) supporting both colors, join the component of \(K_0\) containing \(p\) to the component of \(K_1\) containing \(p\). Multiple such pairs may yield the same graph edge. The involution \(R\) swaps the two parts and acts on the graph.

**Theorem 3 (first antipodal tower criterion).** The connected components of \(K\) are naturally in bijection with the connected components of \(\Gamma_c\), compatibly with \(R\). Furthermore, the following are equivalent:

(i) There are chains \(z_0\in C_0(K;\mathbb F_2)\), \(z_1\in C_1(K;\mathbb F_2)\) satisfying
\[
\boxed{\varepsilon z_0=1,\qquad
\partial z_1=(1+R)z_0.}
\tag{2}
\]

(ii) \(K\) has a connected component preserved setwise by \(R\).

(iii) \(\Gamma_c\) has a connected component preserved setwise by its induced involution.

*Proof.* A connected component of the union of two simplicial complexes is determined by the incidence of their connected components through nonempty intersections. This is precisely \(\Gamma_c\), proving the first assertion and (ii) equivalent to (iii).

If (ii) holds, choose any vertex \(p\) of an \(R\)-preserved component. There is a one-skeleton path from \(p\) to \(Rp\); taking \(z_0=p\) and its mod-two edge chain as \(z_1\) proves (i).

Conversely, assume (i). For a component \(C\) of \(K\), the total parity of vertices in the boundary of a one-chain vanishes. Thus
\[
0=\varepsilon_C\partial z_1
=\varepsilon_C z_0+\varepsilon_{RC}z_0.
\]
If every component came in a distinct \(R\)-pair, this equation would make the total augmentation \(\varepsilon z_0\) even, contradicting its value one. Hence some component is preserved by \(R\). \(\square\)

**Corollary 4 (homological barrier after connectivity).** If \(n\ge5\) and no monochromatic full antipodal geodesic exists, then either the incidence graph \(\Gamma_c\) has no \(R\)-preserved component, or each such component of \(K\) has nontrivial mod-two homology in some positive degree at most \(\lfloor(n-1)/2\rfloor-1\). This follows from Theorem 3 and the antipodal chain-tower theorem of Article XIV.

In dimensions five and six, where the required tower height is two, the condition sharpens: whenever \(p,Rp\) lie in the same component and \(\gamma\) is any one-chain with \(\partial\gamma=p+Rp\), the cycle
\[
\boxed{(1+R)\gamma\in Z_1(K;\mathbb F_2)}
\]
must represent a nonzero homology class under a hypothetical NORI1 failure. Indeed otherwise a two-chain filling it would provide the forbidden tower of height two.

**Scope.** This is a connectivity classification, not a proof that a preserved component exists in every coloring. A monochromatic four-cycle provides a crucial exception to the naive nonbacktracking-component rule: its two orientations are joined by the rank-two monochromatic endpoint pair at its opposite corners. More generally, the cycle-geodesic clause of Theorem 2 cannot be discarded. The incidence graph describes the first chain equation entirely in finite graph-theoretic terms; the remaining higher homology is still sensitive to dimension-simple path compatibility.

### Graded projective Petrie homology and chamber-wall limitations

Two complementary phenomena occur for unrestricted antipodally odd cube colorings. A single type-D chamber wall can carry nonzero projective homology in two different positive switch grades, even with vanishing signed first switch moment. Yet the associated graded homology classes of wall differences form an ordinary coboundary on the full chamber adjacency graph, so their periods always vanish.

Let \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\), \(n\ge3\), and let \(\eta\) be the generator of \(H_1(Y_n;\mathbb F_2)\). A Petrie cycle formed from an antipodal cube geodesic projects to a loop representing \(\eta\), since its lift joins a vertex to its antipode. Fix a legal coloring \(c\). For a type-D chamber tree \(T\), let \(\mathcal B(T)\) be its \(2^{n-2}\) Petrie cycles, \(h_c(C)\) their root-slide-invariant twisted switch grade, and set
\[
\Gamma_r(T)=\sum_{C\in\mathcal B(T):h_c(C)=r}[\bar C],\qquad
p_r(T)=\#\{C\in\mathcal B(T):h_c(C)=r\}\pmod2.
\tag{1}
\]

**Theorem 1 (homological fillability and zero chamber holonomy).** For every \(T,r\),
\[
\boxed{[\Gamma_r(T)]=p_r(T)\eta.}
\tag{2}
\]
A mod-two sum of projective Petrie loops bounds a projective cubical two-chain if and only if its number of summands is even. Every chamber book has \(\sum_rp_r(T)=0\). Along a directed chamber wall \(T\to T'\), the grade-\(r\) homology flux is
\[
\boxed{
\mathcal F_r(T,T')=[\Gamma_r(T')+\Gamma_r(T)]
=(p_r(T')+p_r(T))\eta=(\delta p_r)(T,T')\eta.}
\tag{3}
\]
Therefore the sum of \(\mathcal F_r\) around every closed chamber walk is zero, independently at every switch grade.

*Proof.* Every projected Petrie loop represents \(\eta\), so linearity proves (2). The cubical two-skeleton computes \(H_1(Y_n;\mathbb F_2)\), giving the filling criterion. The cardinality \(2^{n-2}\) is even for \(n\ge3\). Formula (3) is the coboundary of the globally defined chamber function \(p_r\); every closed walk telescopes. \(\square\)

For a central-edge-changing chamber wall, take leading directions \(i,j\), a reference vertex \(g\), and order \(K\) of the remaining \(n-2\) directions. The signed root-wall grade polynomial is
\[
W(t)=\sum_{\sigma\in\mathcal U(K)}\epsilon_K(\sigma)
\bigl(t^{h_c(C(g;i,j,\sigma))}-t^{h_c(C(g;j,i,\sigma))}\bigr).
\tag{4}
\]
Adjacent-exchange variation gives \(\Delta_\sigma=h_{ij}(\sigma)-h_{ji}(\sigma)\in\{-1,0,1\}\) and
\[
\boxed{W(t)=(t-1)\sum_\sigma\epsilon_K(\sigma)\Delta_\sigma
t^{\min(h_{ij}(\sigma),h_{ji}(\sigma))}.}
\tag{5}
\]
The previously proved endpoint theorem determines \(W'(1)\), but not all coefficients of \(W\).

**Theorem 2 (sharp higher-grade obstruction).** If \(4\le n\le6\), all contributing geodesics have positive switch grade, and \(W'(1)=0\), then \(W=0\). In dimension \(7\) the following legal antipodally odd affine coloring gives all contributing paths positive grade while
\[
\boxed{W(t)=-t(t-1)^2=-t+2t^2-t^3\ne0.}
\tag{6}
\]
Index dimensions \(0,\ldots,6\) and set
\[
c(\{x,x\oplus e_d\})=x_{j_d}+a_d\pmod2,\qquad
(j_0,\ldots,j_6)=(4,2,1,1,3,4,2),\quad
(a_0,\ldots,a_6)=(0,1,0,1,0,1,0).
\tag{7}
\]
Take \(g=0,i=0,j=1,K=(2,3,4,5,6)\). The projective grade-one and grade-three wall chains each represent \(\eta\), and cannot bound a projective two-chain separately.

*Proof.* Every \(W\) vanishes at \(t=1\). If all grades are positive, \(W(0)=0\); vanishing derivative at \(1\) means \(t(t-1)^2\mid W\). The largest twisted grade is \(\lfloor(n-1)/2\rfloor\le2\) for \(n\le6\), forcing \(W=0\).

For (7), \(j_d\ne d\), making the bit well-defined on an undirected edge, and vertex complementation flips the bit, proving legal antipodal oddness. Expand the sixteen words of the right-normed Lie bracket on \(K\). Read the edge bit \(x_{j_d}+a_d\) immediately before each dimension \(d\) is toggled. The two signed grade distributions are
\[
\sum_\sigma\epsilon_K(\sigma)t^{h_{01}(\sigma)}=-2t+2t^2,\qquad
\sum_\sigma\epsilon_K(\sigma)t^{h_{10}(\sigma)}=-t+t^3.
\tag{8}
\]
All 32 grades are in \(\{1,2,3\}\). Subtraction yields (6); its first derivative at one vanishes, but its mod-two reduction is \(t+t^3\). In odd dimension \(7\), this is the mod-two projected root-wall chain polynomial. Each of grades one and three is therefore an odd sum of projected Petrie loops and represents \(\eta\), proving the filling obstruction by Theorem 1. \(\square\)

The affine example does not refute NORI1: the rooted path of dimensions \((0,4,5,6,2,1,3)\) is monochromatic with all bits zero.

**Implication for the chain approach.** Theorem 2 rules out universally grade-preserving local wall fillings based solely on first-moment cancellation, even when every path at that wall has positive grade. Theorem 1 rules out obtaining a nonzero ordinary chamber-graph cohomology class merely by accumulating these scalar graded \(H_1\) differences around loops. Further progress needs support-sensitive relative chains, higher incidence information, or suitably twisted equivariant coefficients; scalar homology flux is insufficient.

### Odd-walk characterization of the first antipodal chain lift

Let \(c:E(Q_n)\to\mathbb F_2\) be an antipodally odd coloring. Let \(K_0,K_1\) be the directed monochromatic endpoint-poset complexes, let \(K=K_0\cup K_1\), and put \(I=K_0\cap K_1\). There are two commuting involutions on directed endpoint pairs,
\[
\boxed{A(u,v)=(\bar u,\bar v),\qquad J(u,v)=(v,u),\qquad R=AJ.}
\tag{1}
\]
Antipodality \(A\) exchanges \(K_0,K_1\), while reversal \(J\) preserves each of them. The map \(R\) therefore exchanges colors and acts as the involution in the NORI1 chain-tower construction.

Write \(\mathscr C\) for the finite set of connected components of \(K_0\). Reversal \(J\) acts as an involution on \(\mathscr C\). For a bi-monochromatic directed endpoint pair \(p\in I\), let \(C(p)\in\mathscr C\) denote the red component containing \(p\), and define a (possibly looped, undirected) graph
\[
\boxed{
G_c:\quad
V(G_c)=\mathscr C,\qquad
C(p)\sim C(Ap)\quad(p\in I).
}
\tag{2}
\]
This adjacency is symmetric because \(Ap\in I\) and \(A^2p=p\). Multiple intervals producing the same adjacency may be identified. The graph is preserved by \(J\) because \(Jp\in I\), and the corresponding adjacency is \(JC(p)\sim JC(Ap)\).

**Theorem 1 (two-color incidence as a bipartite double cover).** Let \(\Gamma_c\) be the bipartite incidence graph whose two vertex classes are the connected components of \(K_0\) and \(K_1\), with one edge for every nonempty intersection of a red and a blue component. Under the identification of a blue component \(A(C)\) with \(C\in\mathscr C\), one has an isomorphism
\[
\boxed{
\Gamma_c\cong G_c\times_{\rm bip}K_2,
}
\tag{3}
\]
where the right side is the bipartite double cover with vertices \((C,\epsilon)\), \(\epsilon\in\mathbb F_2\), and an edge \((C,0)\sim(D,1)\) for each graph edge \(C\sim D\). Under this isomorphism the antipodal reversal acts by
\[
\boxed{R(C,\epsilon)=(JC,1-\epsilon).}
\tag{4}
\]

*Proof.* An interval \(p\in I\) belongs to the red component \(C(p)\), and belongs to a blue component \(B(p)\). Since \(A\) maps the blue complex onto the red complex, \(AB(p)=C(Ap)\). Thus \(p\) gives an edge from \((C(p),0)\) to \((C(Ap),1)\) in the double cover. Applying \(A\) to \(p\) gives the reverse sheet edge. Every incidence edge arises from some bi-monochromatic interval, proving (3). Finally \(A\) exchanges sheets, while \(J\) preserves the sheets and sends component \(C\) to \(JC\); they commute, proving (4). \(\square\)

**Theorem 2 (odd-walk criterion).** The first antipodal chain equations
\[
\boxed{
\varepsilon z_0=1,\qquad
\partial z_1=(1+R)z_0
}
\tag{5}
\]
admit a solution in \(C_0(K;\mathbb F_2)\) and \(C_1(K;\mathbb F_2)\) if and only if
\[
\boxed{\text{there is an odd-length walk in }G_c
\text{ from some }C\text{ to }JC.}
\tag{6}
\]

*Proof.* By the first chain-equation theorem in the preceding Subsection, (5) is solvable if and only if \(\Gamma_c\) has a connected component preserved by \(R\), equivalently if some vertex \(v\) is connected to \(Rv\). Choose \(v=(C,0)\) in the double-cover model (3). Its image is \(Rv=(JC,1)\). A walk in \(G_c\) from \(C\) to \(JC\) lifts from \((C,0)\) to \((JC,1)\) precisely when it has odd length, since every edge toggles the sheet. Thus the two conditions are equivalent. \(\square\)

**Corollary 3 (finite parity classification).** The first chain equations (5) are solvable if and only if some connected component \(W\) of \(G_c\) is preserved by \(J\) and satisfies at least one of the following:
\[
\boxed{
\begin{array}{ll}
\text{(a)}&W\text{ is nonbipartite};\\
\text{(b)}&W\text{ is bipartite and }J\text{ exchanges its two bipartition classes}.
\end{array}}
\tag{7}
\]
Loops count as odd cycles in (a).

*Proof.* In a connected nonbipartite graph, any two vertices are joined by walks of either parity, obtained by inserting an odd closed walk. In a connected bipartite graph, the parity of a walk between two vertices is odd precisely when they belong to opposite bipartition classes. An automorphism preserving the connected component either preserves its two bipartition classes individually or swaps them. Apply Theorem 2. \(\square\)

**Connection to color-component classification.** The vertices of \(G_c\) can be determined from the ordinary red edge graph by the preceding nonbacktracking component theorem: every red connected edge subgraph with a branching vertex yields one reversal-fixed node; a red path yields two nodes exchanged by \(J\); and a red cycle yields one node if it has an opposed pair of cube-geodesic half-cycles, otherwise two nodes exchanged by \(J\). Consequently the first equivariant chain equation is governed by an ordinary finite graph with a graph involution, rather than by a higher-dimensional extension problem.

**Limitations and proof direction.** Theorem 2 does not guarantee an odd walk for every legal coloring; that would be a new substantive connectivity assertion. It supplies a lower-complexity necessary and sufficient condition for the first stage. If such an odd walk exists, one can select a first tower chain \(z_1\), but extending the tower requires filling the homology class of \((1+R)z_1\). The forest-collapse theorem shows this higher class may encounter nontrivial directed-turn homology even in acyclic monochromatic edge components.

### Smith transfer equivalence and the canonical second tower obstruction

Let X be a finite simplicial complex carrying a free simplicial involution R, let Q=X/R, and take all chains and cohomology over F₂. Write N=1+R, let π:C_*(X)→C_*(Q) be the orbit projection, and let t:C_*(Q)→C_*(X) send an orbit simplex to the sum of its two lifts. Then

0 → C_*(Q) --t→ C_*(X) --π→ C_*(Q) → 0

is a short sequence of chain complexes, with tπ=N. Its homology connecting operator D:H_j(Q)→H_{j−1}(Q) is the Smith transfer connecting map.

**Lemma (Smith connecting map).** D(h)=α cap h, where α=w₁(X→Q)∈H¹(Q;F₂).

*Proof.* Choose one lift of each quotient simplex and represent the double cover by its sheet-transition one-cocycle α. The boundary of the lifted chain differs from the lift of the boundary by the transfer of the transition-weighted faces. On cycles these transitions give the simplicial cap product with α; changing lift choices changes this representative only by a boundary. Equivalently, the covering chain extension above is the local-system extension classified by α. Therefore D=α cap −. □

**Theorem 1 (full converse to the antipodal chain-tower criterion).** For every integer q≥1, the following are equivalent:

(i) α^q≠0 in H^q(Q;F₂).

(ii) There exist chains z_j∈C_j(X), 0≤j≤q, such that
εz₀=1 and ∂z_j=Nz_{j−1} for 1≤j≤q.

*Proof.* Suppose a tower exists. Set h_j=πz_j for all j. Because πN=0, each h_j for j≥1 is a cycle; h₀ is a zero-cycle. The connecting operator sends [h_j] to [h_{j−1}] since ∂z_j=t h_{j−1}. Hence D^q[h_q]=[h₀]. Its augmentation is εz₀=1. By the lemma, this means ⟨α^q,[h_q]⟩=1, proving (i).

Conversely if α^q≠0, choose a quotient q-cycle h_q with ⟨α^q,[h_q]⟩=1; this is possible over the field F₂. Lift h_q to an arbitrary chain z_q upstairs. Since ∂h_q=0, the boundary ∂z_q is in ker π=im t, so ∂z_q=t h_{q−1} for a unique quotient chain h_{q−1}. Injectivity of t implies ∂h_{q−1}=0. Lift h_{q−1} to z_{q−1}; then ∂z_q=tπz_{q−1}=Nz_{q−1}. Iterate to obtain z_{q−2},...,z₀ with every required norm-boundary equation. At degree zero, εz₀ equals the augmentation of D^q[h_q], which is ⟨α^q,[h_q]⟩=1. This proves (ii). □

In particular the maximal height of such a tower equals the largest nonzero power of the reversal-covering class. This completes the converse missing from the earlier one-chain-per-degree construction in Article XIV. It also shows that producing a tower is a topological index problem, not merely a weaker proxy for one.

**Theorem 2 (a canonical obstruction at degree two).** Let C be an R-invariant connected component of X. Choose a vertex p∈C and a mod-two one-chain γ with ∂γ=p+Rp. Put ζ=γ+Rγ. Then [ζ]∈H₁(C;F₂)^R, and its class
θ(C)=[ζ] mod N H₁(C;F₂)
in the quotient H₁(C;F₂)^R / N H₁(C;F₂)
is independent of both p and γ. Moreover
θ(C)=0 if and only if C admits a tower of height two, equivalently if and only if α_C²≠0.

*Proof.* If γ is changed with p fixed, its difference is a one-cycle η, and ζ changes by Nη. If the root changes from p to p', choose a path-chain η from p to p', replace γ by γ+η+Rη, and observe that ζ stays unchanged because N²=0. Thus θ is canonical.

If θ=0, choose a cycle η with [ζ]=N[η]. Replacing γ with γ+η makes the symmetrized cycle a boundary, say ∂z₂=N(γ+η). With z₀=p and z₁=γ+η this is a height-two tower. Conversely any height-two tower with odd zero-chain in C can be normalized to z₀=p by connecting its zero-chain to p and adding N of the connecting one-chain to z₁. Then its second equation implies θ(C)=0. The last equivalence follows from Theorem 1. □

**NORI interpretation.** For a hypothetical counterexample, apply the theorem to the free reversal action on the two-color directed endpoint complex K. The earlier half-dimensional bound gives α_K^q=0, where q=floor((n−1)/2). By Theorem 1 no height-q tower exists. For n≥5, the first stage is the odd-walk condition on the red-component incidence graph; if an invariant connected component exists, its *second* obstruction is the choice-independent class θ(C), rather than the homology class of any one arbitrarily chosen symmetrized path. At greater degrees, the Smith transfer sequence gives the analogous test through iterated cap products with α.

The result does not prove that the needed tower exists, and it does not close NORI1. Its value is a two-way algebraic characterization and a canonical obstruction that can be computed without making arbitrary root/path choices.

### Seam-component multigraph and the second tower obstruction

Let K=K0 union K1 be finite simplicial complexes, I=K0 intersect K1, and suppose an involution R exchanges the two pieces. Construct a bipartite multigraph Lambda with one vertex per connected component of K0 or K1, and **one edge for each connected component S of I**, joining the two color components containing S. Keep parallel edges. The involution exchanges the color parts and sends edge S to edge RS.

**Theorem 1 (equivariant graph and Mayer–Vietoris).** There is an equivariant piecewise-linear map nu:|K|→|Lambda| inducing bijection on connected components and surjection on first homology over F2. The following homology sequence has zero cokernel and each displayed kernel is the preceding image:
\[
H_1(I)\to H_1(K0)\oplus H_1(K1)\to H_1(K)
\xrightarrow{\nu_*}H_1(Lambda)\to0.
\tag{1}
\]

*Proof.* On the barycentric subdivision, send each simplex exclusively in K0 or K1 to the corresponding color-component vertex; send each simplex of I to the midpoint of the graph edge associated with its connected seam component. Nested simplices in I belong to the same component, and a chain exiting I enters only one color piece, so affine interpolation within a single graph edge is continuous. The rule commutes with R. Each graph walk lifts through its seam components and the adjacent connected color pieces, proving surjectivity on π1 and H1. Finally, the Mayer–Vietoris sequence has consecutive terms H1(I), H1(K0)⊕H1(K1), H1(K), H0(I), H0(K0)⊕H0(K1). The kernel of its last map is the graph cycle space H1(Lambda); the connecting map counts seam crossings and agrees with nu_*. This proves (1). □

**Theorem 2 (fixed seam threshold).** Assume R acts freely on K and let alpha be the double-cover class on K/R. If Lambda has no R-invariant edge, then alpha squared vanishes. An R-invariant edge of Lambda is equivalent to an R-invariant connected component S of I.

*Proof.* R swaps the bipartite vertex parts, so no graph vertex is fixed. If no edge is preserved as a set, Lambda is a free involution graph. Equivariance of nu makes alpha the pullback of the covering class on Lambda/R; its square vanishes because this quotient is a graph. The final equivalence follows from the definition of edges. □

**Theorem 3 (monochromatic location of the second obstruction).** Suppose C⊆K is connected and R-invariant, and contains an R-invariant connected seam component S⊆I. Choose p∈S and a mod-two path-chain gamma⊆S from p to Rp. The one-cycle zeta=gamma+Rgamma represents the canonical second-stage Tate obstruction theta(C), and
\[
\boxed{[zeta]\in\operatorname{im}\bigl(
H_1(K0\cap C)\oplus H_1(K1\cap C)\to H_1(C)\bigr).}
\tag{2}
\]

*Proof.* The preceding Smith-transfer theorem makes any symmetrized path from p to Rp a representative of theta(C). The map nu is constant on the connected seam component S, so it sends zeta to zero already on chains. By (1), its first-homology class belongs to the stated image. □

**Corollary.** If the image of monochromatic first homology in H1(C) vanishes under Theorem 3 (for instance, if both color pieces in C have zero first homology), then theta(C)=0, a tower through degree two exists, and alpha_C squared is nonzero.

For NORI1, this sharpens the separation of tasks: the first tower step is a parity walk in an incidence graph, while, after locating a reversal-invariant seam component, the second obstruction comes from the internal directed-turn homology of monochromatic pieces. It does not assert the required seam component exists in every coloring.
